import tensorflow as tf
import numpy as np

def solve_for_constraints(d, g, w, img):
    """
    d: intensity constraints (1 channel)
    g: gradient constraints (h and v, 2 channels)
    w: weights of d and g (3 channels)
    img: input image (used to adjust the skewed output range)
    """
    gx = g[:,:,0]
    gy = g[:,:,1]
    wd = w[:,:,0]
    wgx = w[:,:,1]
    wgy = w[:,:,2]

    Ad, bd = build_Ad(wd, d)
    Agx, bgx = build_Agx(wgx, gx)
    Agy, bgy = build_Agy(wgy, gy)

    A = tf.concat((Ad, Agx, Agy), axis=0)
    b = tf.concat((bd, bgx, bgy), axis=0)

    res = tf.linalg.lstsq(A, b)
    res = tf.reshape(res, img.shape)

    #correct image range
    input_mean = tf.reduce_mean(img)
    res_mean = tf.reduce_mean(res)

    offset = input_mean - res_mean
    fixed_res = res + offset
    fixed_res = tf.maximum(0, tf.minimum(1, fixed_res))

    return fixed_res

def build_Ad(wd, d):
    """
    creates the part of the equation (Ax = b) responsible for the pixel values
    """
    bd = tf.reshape(d, [-1])
    Ad = tf.linalg.diag(tf.reshape(wd, [-1]))
    return Ad, bd

def build_Agx(wgx, gx):
    """
    builds the equations for the system Ax = b responsible for the x derivative
    omits the outer edge of the image, because the derivative is not well defined there
    """
    bgx = tf.reshape(gx, [-1])
    wgx_0 = tf.concat([wgx[:, :-2], tf.zeros([wgx.shape[0], 1])], axis=1)
    wgx_1 = tf.concat([tf.zeros([wgx.shape[0], 1]), wgx[:, :-2]], axis=1)
    Agx_0 = tf.linalg.diag(tf.reshape(wgx_0, [-1]))
    Agx_1 = tf.linalg.diag(tf.reshape(wgx_1, [-1]))
    Agx = Agx_1 - Agx_0

    return Agx, bgx

def build_Agy(wgy, gy):
    """
    builds the equations for the system Ax = b responsible for the x derivative
    omits the outer edge of the image, because the derivative is not well defined there
    """
    bgy = tf.reshape(gy, [-1])
    wgy_0 = tf.concat([wgy[:-2, :], tf.zeros([1, wgy.shape[1]])], axis=0)
    wgy_1 = tf.concat([tf.zeros([1, wgy.shape[1]]), wgy[:-2, :]], axis=0)
    Agy_0 = tf.linalg.diag(tf.reshape(wgy_0, [-1]))
    Agy_1 = tf.linalg.diag(tf.reshape(wgy_1, [-1]))
    Agy = Agy_1 - Agy_0

    return Agy, bgy

def calc_gradients(img):
    """
    calculate gradients of the image. The method used by this function needs to match the equations of the matrix of equations (in this case, subtracting the right/lower pixel from the left/upper pixel to get the gradient of a pixel)
    """
    img = tf.expand_dims(img, axis=0)
    # img = tf.expand_dims(img, axis=-1)
    gy, gx = tf.image.image_gradients(img)

    gx = tf.squeeze(gx)
    gy = tf.squeeze(gy)

    return gx, gy


def basic_sharpening(img):
    gx, gy = calc_gradients(img)
    cg = 1.5
    wg = 1
    cd = 0.7
    d = img
    g = tf.stack((gx * cg, gy * cg), axis=-1)

    w = tf.stack((np.full(img.shape, cd), np.full(img.shape, wg), np.full(img.shape, wg)), axis=-1)
    res = solve_for_constraints(d, g, w, img)
    return res, None

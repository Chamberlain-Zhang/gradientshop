<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
</head>
<body style='margin:0 5% 0 5%; padding:5%; font-family:Trebuchet MS, Helvetica, sans-serif'>
  <h1>Description</h1>
  An implementation of some ideas from GradientShop, developed by Bhat, Zitnick et al. (https://grail.cs.washington.edu/projects/gradientshop/).

  <h2>Requirements</h2>
Python3.7, numpy, scikit-image, scipy, opencv-python, matplotlib

  <h2>Usage</h2>
  Once everything is installed, pass your images as command line arguments to main_gradients.

  <h2>Examples</h2>
  
  <h3> Salient edge detection </h3>
<table class='center'>
    <tr>
    <td class="tg-s268">original</td>
    <td class="tg-s268">gradients</td>
    <td class="tg-s268">locally normalized gradients</td>
    <td class="tg-s268">calculated lengths</td>
    <td class="tg-s268">salient edges</td>
    </tr>
    <td class="tg-s268">
      <a href="./example_images/pixi.jpg">
      <img src="./example_images/pixi.jpg" height="200"> 
      </a>
    </td>
    <td class="tg-s268">
      <a href="./example_images/pixi_1_gradients.jpg">
      <img src="./example_images/pixi_1_gradients.jpg" height="200"> 
      </a>
    </td>
    <td class="tg-s268">
      <a href="./example_images/pixi_2_normalized_gradients.jpg">
      <img src="./example_images/pixi_2_normalized_gradients.jpg" height="200"> 
      </a>
    </td>
    <td class="tg-s268">
      <a href="./example_images/pixi_3_lengths.jpg">
      <img src="./example_images/pixi_3_lengths.jpg" height="200"> 
      </a>
    </td>
    <td class="tg-s268">
      <a href="./example_images/pixi_4_final.jpg">
      <img src="./example_images/pixi_4_final.jpg" height="200"> 
      </a>
    </td>
    </tr>
</table>
  

  <h3> Salient sharpening </h3>
<table class='center'>
    <tr>
    <td class="tg-s268">original image</td>
    <td class="tg-s268">global sharpening</td>
    <td class="tg-s268">salient sharpening</td>
    <td class="tg-s268">laplacian sharpening</td>
    </tr>
    <tr>
    <td class="tg-s268">
      <a href="./example_images/fish.jpg">
      <img src="./example_images/fish.jpg" width="200"> 
      </a>
    </td>
    <td class="tg-s268">
      <a href="./example_images/fish_1basic.jpg">
      <img src="./example_images/fish_1basic.jpg" width="200"> 
      </a>
    </td>
    <td class="tg-s268">
      <a href="./example_images/fish_2salient.jpg">
      <img src="./example_images/fish_2salient.jpg" width="200"> 
      </a>
    </td>
    <td class="tg-s268">
      <a href="./example_images/frequency_sharpened_fish.jpg">
      <img src="./example_images/frequency_sharpened_fish.jpg" width="200"> 
      </a>
    </td>
    </tr>
</table>

  <h3> Non-photorealistic rendering</h3>
<table class='center'>
  <tr>
    <td class="tg-s268">original</td>
    <td class="tg-s268">non-photorealistic render</td>
  </tr>
  <tr>
    <td class="tg-s268">
      <a href="./example_images/me.jpg">
      <img src="./example_images/me.jpg" width="300"> 
      </a>
    </td>
    <td class="tg-s268">
      <a href="./example_images/me_npr.jpg">
      <img src="./example_images/me_npr.jpg" width="300"> 
      </a>
    </td>
  </tr>
  <tr>
    <td class="tg-s268">
      <a href="./example_images/pixi.jpg">
      <img src="./example_images/pixi.jpg" width="300"> 
      </a>
    </td>
    <td class="tg-s268">
      <a href="./example_images/pixi_npr.jpg">
      <img src="./example_images/pixi_npr.jpg" width="300"> 
      </a>
    </td>
  </tr>
  <tr>
    <td class="tg-s268">
      <a href="./example_images/toronto.jpg">
      <img src="./example_images/toronto.jpg" width="300"> 
      </a>
    </td>
    <td class="tg-s268">
      <a href="./example_images/toronto_npr.jpg">
      <img src="./example_images/toronto_npr.jpg" width="300"> 
      </a>
    </td>
  </tr>
  <tr>
    <td class="tg-s268">
      <a href="./example_images/pferde.jpg">
      <img src="./example_images/pferde.jpg" width="300"> 
      </a>
    </td>
    <td class="tg-s268">
      <a href="./example_images/pferde_npr.jpg">
      <img src="./example_images/pferde_npr.jpg" width="300"> 
      </a>
    </td>
  </tr>
</table>

</body>

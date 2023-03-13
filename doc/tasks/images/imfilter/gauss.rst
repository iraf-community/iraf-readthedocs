.. _gauss:

gauss: Convolve a list of 1 or 2-D images with an elliptical Gaussian
=====================================================================

**Package: imfilter**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  gauss input output sigma
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of images to be convolved with the elliptical Gaussian function.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output images. The number of output images must equal the number of
  input images. If the input image name equals the output image name, the
  convolved image will replace the input image.
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma' Line='sigma' -->
  <dd>The sigma of the Gaussian function in pixels along the direction <i>theta</i>
  of the major axis of the Gaussian function.
  </dd>
  </dl>
  <dl id="l_ratio">
  <dt><b>ratio = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ratio' Line='ratio = 1.' -->
  <dd>The ratio of the sigma in the minor axis direction to the sigma in the major
  axis direction of the Gaussian function.
  If <i>ratio</i> is 1 the Gaussian function is circular.
  </dd>
  </dl>
  <dl id="l_theta">
  <dt><b>theta = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='theta' Line='theta = 0.' -->
  <dd>The position of the major axis of the elliptical Gaussian function.
  <i>Theta</i> is measured counter-clockwise from the x axis and must be between
  0 and 180 degrees.
  </dd>
  </dl>
  <dl id="l_nsigma">
  <dt><b>nsigma = 4.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigma' Line='nsigma = 4.0' -->
  <dd>The distance along the major axis of the Gaussian function at which
  the kernel is truncated in <i>sigma</i> pixels.
  </dd>
  </dl>
  <dl id="l_bilinear">
  <dt><b>bilinear = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bilinear' Line='bilinear = yes' -->
  <dd>Use the fact that the Gaussian function is separable (bilinear) in x and y if
  <i>theta</i> = 0, 90, or 180, to compute the 2D convolution more efficiently?
  <i>Bilinear</i> is always set to <span style="font-family: monospace;">"no"</span> internally, if the position angle of
  the major axis of the Gaussian is other than 0, 90 or 180 degrees.
  </dd>
  </dl>
  <dl id="l_boundary">
  <dt><b>boundary = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary' Line='boundary = "nearest"' -->
  <dd>The algorithm used to compute the values of the out of bounds pixels. The
  options are:
  <dl>
  <dt><b>nearest</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nearest' Line='nearest' -->
  <dd>Use the value of the nearest boundary pixel.
  </dd>
  </dl>
  <dl>
  <dt><b>constant</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='constant' Line='constant' -->
  <dd>Use a constant value.
  </dd>
  </dl>
  <dl>
  <dt><b>reflect</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='reflect' Line='reflect' -->
  <dd>Generate a value by reflecting around the boundary.
  </dd>
  </dl>
  <dl>
  <dt><b>wrap</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='wrap' Line='wrap' -->
  <dd>Generate a value by wrapping around to the opposite side of the image.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_constant">
  <dt><b>constant = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constant' Line='constant = 0.' -->
  <dd>The constant for constant-valued boundary extension.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  GAUSS convolves the list of images in <i>input</i> with the
  Gaussian kernel specified by <i>sigma</i>, <i>ratio</i>, <i>theta</i> and
  <i>nsigma</i> and places the convolved images in <i>output</i>.
  If the image names in <i>input</i> equal the image names in <i>output</i>
  the convolution is performed in place and the original images are
  overwritten. Out of bounds pixels are computed using the algorithm
  specified by <i>boundary</i>.
  </p>
  <p>
  If <i>bilinear</i> is <span style="font-family: monospace;">"yes"</span> and the major axis of the Gaussian kernel
  is aligned along either the x or y axis, GAUSS uses the fact that
  the Gaussian function is mathematically separable (bilinear) in x and y
  to speed up the convolution process. A bilinear 2D convolution kernel
  in x and y is one which can be separated into two equivalent 1D
  convolution kernels in x and y respectively. 
  </p>
  <p>
  Although the bilinear approximation and the full 2D convolution are
  mathematically equivalent, the user will actually see SMALL differences
  between an image convolved with the full 2D kernel and the same image
  convolved with the equivalent bilinear kernel.
  These differences are the result of the finite size of the convolution kernel
  (the integration does not extend to infinity in either direction),
  and the fact that off-axis kernel elements outside the <i>nsigma</i> limit
  cannot be set to 0 in the bilinear case as they are in the full 2D
  case. Therefore the bilinear kernel is less radially symmetric than
  the full 2D kernel.  In most cases the differences are small and more
  than made up for by the greatly decreased execution time.
  </p>
  <p>
  The Gaussian kernel has an elliptical cross-section and Gaussian
  profile and is defined mathematically as follows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  1. Circularly Symmetric Gaussian Function
  
      ratio = 1   theta = 0.0   N = normalization factor
  
      G = N * exp (-0.5 * (r / sigma) ** 2)
  
  2. Elliptical Gaussian Function (Theta = 0, 90 or 180)
  
      sigmax = sigma   sigmay = ratio * sigmax   N = normalization factor
  
      A = cos (theta) ** 2 / sigmax ** 2 + sin (theta) ** 2 / sigmay ** 2
  
      B = 0.0
  
      C = sin (theta) ** 2 / sigmax ** 2 + cos (theta) ** 2 / sigmay ** 2
  
      z = A * x ** 2 + B * x * y + C * y ** 2
  
      G = N * exp (-0.5 * z)
  
  3. Elliptical Gaussian  Function (Arbitrary Theta)
  
      sigmax = sigma   sigmay = ratio * sigmax   N=normalization factor
  
      A = cos (theta) ** 2 / sigmax ** 2 + sin (theta) ** 2 / sigmay ** 2
  
      B = 2 * (1 / sigmax ** 2 - 1 / sigmay ** 2) * sin (theta) * cos (theta)
  
      C = sin (theta) ** 2 / sigmax ** 2 + cos (theta) ** 2 / sigmay ** 2
  
      z = A * x ** 2 + B * x * y + C * y ** 2
  
      G = N * exp (-0.5 * z)
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convolve an image with a circular Gaussian function of sigma 2.0, and
  size 4.0 sigma using nearest neighbor boundary extension and the bilinear
  kernel.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gauss m83 m83.gau 2.0
  </pre></div>
  <p>
  2. Do the same convolution using the full 2D kernel.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gauss m83 m83.gau.2D 2.0 bilinear-
  </pre></div>
  <p>
  3. Convolve an image with an elliptical Gaussian function whose sigma in the
  major and minor axis direction is 2.0 and 1.5 respectively, and whose position
  angle is 45 degrees, using wrap around boundary extension. In this case the
  full 2D kernel is used by default.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gauss m84 m84.gau 2.0 ratio=.75 theta=45. bound=wrap
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  GAUSS requires approximately 30 and 8 cpu seconds to
  convolve a 512 square real image with circularly symmetric Gaussian function
  of sigma 2 pixels, using the full 2D kernel and the bilinear
  kernel respectively, on a Sparc Station 1.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  convolve, gradient, laplace, boxcar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

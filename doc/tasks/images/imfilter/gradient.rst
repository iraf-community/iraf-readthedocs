.. _gradient:

gradient: Convolve a list of 1 or 2-D images with a gradient operator
=====================================================================

**Package: imfilter**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  gradient input output gradient
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of images for which gradient images are to be calculated.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output images. The number of output images must equal the number of
  input images. If the input image name equals the output image name the
  convolved image will replace the input image.
  </dd>
  </dl>
  <dl id="l_gradient">
  <dt><b>gradient</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gradient' Line='gradient' -->
  <dd>The gradient filters are a set of 8 three by three kernels identified by the
  angle of maximum response as measured counter-clockwise to the x axis. The
  kernels approximate the gradient operator, which is defined as the slope of
  the intensity distribution in an image.  The eight supported gradient
  operators are listed below.
  <dl>
  <dt><b><span style="font-family: monospace;">"0"</span>, <span style="font-family: monospace;">"180"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"0", "180"' -->
  <dd>Calculate the gradient image along a 0 or 180 degree angle.
  These options approximate the d/dx operator.
  Option <span style="font-family: monospace;">"0"</span> produces a maximum response for pixel values which
  increase with increasing x, whereas option <span style="font-family: monospace;">"180"</span> produces a maximum
  response for pixel values which decrease with increasing x. 
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"90"</span>, <span style="font-family: monospace;">"270"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"90", "270"' -->
  <dd>Calculate the gradient image along a 90 or 270 degree angle.
  These options approximate the d/dy operator.
  Option <span style="font-family: monospace;">"90"</span> produces a maximum response for pixel values which
  increase with increasing y, whereas option <span style="font-family: monospace;">"270"</span> produces a maximum
  response for pixel values which decrease with increasing y.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"45"</span>, <span style="font-family: monospace;">"225"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"45", "225"' -->
  <dd>Calculate the gradient image along a 45 or 225 degree angle.
  Option <span style="font-family: monospace;">"45"</span> produces a maximum response for pixel values which increase
  along a line at 45 degrees counter-clockwise to the x axis.
  Option <span style="font-family: monospace;">"225"</span> produces
  a maximum response for pixel values which increase along a line at 225
  degrees to the x axis.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"135"</span>, <span style="font-family: monospace;">"315"</span> </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"135", "315" ' -->
  <dd>Calculate the gradient image along a 135 or 315 degree angle.
  Option <span style="font-family: monospace;">"135"</span> produces a maximum response for pixel values which increase
  along a line at 135 degrees counter-clockwise to the x axis.
  Option <span style="font-family: monospace;">"315"</span> produces
  a maximum response for pixel values which increase along a line at 315
  degrees to the x axis.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_boundary">
  <dt><b>boundary = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary' Line='boundary = "nearest"' -->
  <dd>The algorithm used to compute the values of out of bounds pixels. The 
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
  GRADIENT convolves the list of images specified by <i>input</i> with one of
  eight three by three gradient kernels specified by <i>gradient</i> 
  and places the output images in <i>output</i>.
  If the image names in <i>output</i> equal the image names in <i>input</i> the
  gradient operation is performed in place and the original images are
  overwritten. Out of bounds pixels are computed using the algorithm
  specified by <i>boundary</i>.
  </p>
  <p>
  GRADIENT acts like a simple edge detector or high pass filter which is sensitive
  to both the magnitude and direction of changes in intensity in an image.
  For example, if an image's pixel values are specified by the sum of their
  x and y coordinates (z = x + y) and boundary extension effects are ignored,
  the <span style="font-family: monospace;">"0"</span>, <span style="font-family: monospace;">"45"</span>, <span style="font-family: monospace;">"90"</span>, <span style="font-family: monospace;">"135"</span>, <span style="font-family: monospace;">"180"</span>, <span style="font-family: monospace;">"225"</span>, <span style="font-family: monospace;">"270"</span>, and <span style="font-family: monospace;">"315"</span> gradient kernels
  will each produce a constant image containing the numbers 1, sqrt (2), 1, 0,
  -1, -sqrt (2), -1, and 0 respectively. 
  </p>
  <p>
  The eight gradient filters are listed below. The I[*,*] are the elements of
  the input image and the O[*,*] are elements of the output image.
  </p>
  <div class="highlight-default-notranslate"><pre>
                        0
  
           - I[-1,1]          + 0*I[0,1]  + I[1,1]
  O[0,0] = - I[-1,0]*sqrt(2)  + 0*I[0,0]  + I[1,0] * sqrt(2)
           - I[-1,-1]         + 0*I[0,-1] + I[-1,-1]
  
                       45
  
           + I[-1,1]*0          + I[0,1]   + I[1,1]/2/sqrt(2)
  O[0,0] = - I[-1,0]            + I[0,0]*0 + I[1,0]
           - I[-1,-1]/2/sqrt(2) - I[0,-1]  + I[1,-1]*0
  
                       90
  
           + I[-1,1]    + I[0,1]*sqrt(2)  + I[1,1]
  O[0,0] = + I[-1,0]*0  + I[0,0]*0        + I[1,0]
           - I[-1,-1]   - I[0,-1]*sqrt(2) - I[-1,-1]
  
                      135
  
           + I[-1,1]/2/sqrt(2) + I[0,1]   + I[1,1]*0
  O[0,0] = + I[-1,0]           + I[0,0]*0 - I[1,0]
           + I[-1,-1]*0        - I[0,-1]  - I[1,-1]/2/sqrt(2)
  
                       180
  
           + I[-1,1]          + 0*I[0,1]  - I[1,1]
  O[0,0] = + I[-1,0]*sqrt(2)  + 0*I[0,0]  - I[1,0]*sqrt(2)
           + I[-1,-1]         + 0*I[0,-1] - I[-1,-1]
  
                      225
  
           + I[-1,1]*0          - I[0,1]   - I[1,1]/2/sqrt(2)
  O[0,0] = + I[-1,0]            + I[0,0]*0 - I[1,0]
           + I[-1,-1]/2/sqrt(2) + I[0,-1]  + I[1,-1]*0
  
                      270
  
           - I[-1,1]    - I[0,1]*sqrt(2)  - I[1,1]
  O[0,0] = + I[-1,0]*0  + I[0,0]*0        + I[1,0]*0
           + I[-1,-1]   + I[0,-1]*sqrt(2) + I[-1,-1]
  
                     315
  
           - I[-1,1]/2/sqrt(2) - I[0,1]   + I[1,1]*0
  O[0,0] = - I[-1,0]           + I[0,0]*0 + I[1,0]
           + I[-1,-1]*0        + I[0,-1]  + I[1,-1]/2/sqrt(2)
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Calculate the gradient in the 180 degree direction using nearest neighbor
     boundary extension.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gradient m83 m83.odeg 180
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  GRADIENT requires approximately 2.0 cpu seconds to convolve a
  512 square real image with a 3 by 3 gradient kernel on a Sparc Station 1.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  convolve, gauss, laplace, boxcar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

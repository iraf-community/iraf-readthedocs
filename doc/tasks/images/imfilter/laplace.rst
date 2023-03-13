.. _laplace:

laplace: Laplacian filter a list of 1 or 2-D images
===================================================

**Package: imfilter**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  laplace input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of images to be convolved.
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
  <dl id="l_laplace">
  <dt><b>laplace = <span style="font-family: monospace;">"xycentral"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='laplace' Line='laplace = "xycentral"' -->
  <dd>The Laplacian filters are a set of four three by three kernels which
  approximate the Laplacian operator, where a Laplacian operator is defined
  as the sum of the partial second derivatives in x and y.
  The elements of the four Laplacian kernels are shown in detail below.
  <dl>
  <dt><b>xycentral</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='xycentral' Line='xycentral' -->
  <dd>The elements of the central column and row of a 3 by 3 image subraster are
  combined to estimate the Laplacian at the position of the central pixel.
  </dd>
  </dl>
  <dl>
  <dt><b>diagonals</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='diagonals' Line='diagonals' -->
  <dd>The elements of the two diagonals of a 3 by 3 image subraster are combined
  to estimate the Laplacian at the position of the central pixel.
  </dd>
  </dl>
  <dl>
  <dt><b>xyall</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='xyall' Line='xyall' -->
  <dd>The three columns and rows of a three by three image subraster are averaged
  to estimate the Laplacian at the position of the central pixel.
  </dd>
  </dl>
  <dl>
  <dt><b>xydiagonals</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='xydiagonals' Line='xydiagonals' -->
  <dd>The central row and column and the two diagonals of a three by three image
  subraster are combined to estimate the Laplacian at the position of the
  central pixel.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_boundary">
  <dt><b>boundary = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary' Line='boundary = "nearest"' -->
  <dd>The algorithm used to compute the values of the out of bounds pixels.
  The options are:
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
  LAPLACE convolves the list of images specified by <i>input</i> with one of
  four 3 by 3 Laplacian kernels specified by <i>laplace</i>
  and places the convolved images in <i>output</i>. If the image names
  in <i>output</i> equal the image names in <i>input</i> the Laplacian
  operation is performed in place and the original images are overwritten.
  Out of bounds pixels are computed using the algorithm specified by
  <i>boundary</i>.
  </p>
  <p>
  The Laplacian filters are high-pass filters which act as a local edge detector.
  A characteristic of the Laplacian is that it is zero at points where the
  gradient is a maximum or a minimum. Therefore points detected as gradient
  edges would generally not be detected as edge points with the Laplacian
  filter. Another characteristic of Laplacian operators is that a single
  grey level transition may produce two distinct peaks one positive and
  one negative in the Laplacian which may be offset from the gradient location.
  </p>
  <p>
  The four Laplacian filters are listed below. The I[*,*] are the elements of the
  input image and the O[*,*] are the elements of the output image.
  </p>
  <div class="highlight-default-notranslate"><pre>
                          xycenter
  
               0*I[-1,1]  + 1*I[0,1]  + 0*I[1,1]  +
      O[0,0] = 1*I[-1,0]  - 4*I[0,0]  + 1*I[1,0]  +
               0*I[-1,-1] + 1*I[0,-1] + 0*I[1,-1]
  
                         diagonals
  
            I[-1,1]/sqrt(2)  + I[0,1]*0         +  I[1,1]/sqrt(2) +
  O[0,0] =  I[-1,0]*0        - I[0,0]*4/sqrt(2) +  I[1,0]*0       +
            I[-1,-1]/sqrt(2) + I[0,-1]*0        +  I[1,-1]/sqrt(2)
  
                           xyall
  
                 2/3*I[-1,1]  -  1/3*I[0,1]  + 2/3*I[1,1]  +
      O[0,0] = - 1/3*I[-1,0]  -  4/3*I[0,0]  - 1/3*I[1,0]  +
                 2/3*I[-1,-1] -  1/3*I[0,-1] + 2/3*I[1,-1]
  
                         xydiagonals
  
            I[-1,1]/sqrt(2)/2  + I[0,1]/2           + I[1,1]/sqrt(2)/2 +
  O[0,0] =  I[-1,0]/2          - I[0,0]*(2-sqrt(2)) + I[1,0]/2         +
            I[-1,-1]/sqrt(2)/2 + I[0,-1]/2          + I[1,-1]/sqrt(2)
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convolve an image with the Laplacian filter xyall using nearest neighbor
  boundary extension.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; laplace m83 m83.lap xyall
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  LAPLACE requires approximately 1.7 cpu seconds to convolve a
  512 square real image with a 3 by 3 Laplacian kernel on a Sparc
  Station 1.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  convolve, gauss, gradient, boxcar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

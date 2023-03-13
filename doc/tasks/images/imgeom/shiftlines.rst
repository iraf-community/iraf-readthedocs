.. _shiftlines:

shiftlines: Shift the lines of a list of N-D images
===================================================

**Package: imgeom**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  shiftlines input output shift
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of images to be shifted.  Image sections are allowed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output image names.  If the output image name is the same as the input
  image name then the shifted image replaces the input image.
  </dd>
  </dl>
  <dl id="l_shift">
  <dt><b>shift</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shift' Line='shift' -->
  <dd>Shift in pixels.
  </dd>
  </dl>
  <dl id="l_interp_type">
  <dt><b>interp_type = <span style="font-family: monospace;">"linear"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interp_type' Line='interp_type = "linear"' -->
  <dd>The interpolant type use to computed the output shifted image.
  The choices are the following:
  <dl>
  <dt><b>nearest</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nearest' Line='nearest' -->
  <dd>nearest neighbor interpolation.
  </dd>
  </dl>
  <dl>
  <dt><b>linear</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='linear' Line='linear' -->
  <dd>linear interpolation in x.
  </dd>
  </dl>
  <dl>
  <dt><b>poly3</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='poly3' Line='poly3' -->
  <dd>third order interior polynomial in x.
  </dd>
  </dl>
  <dl>
  <dt><b>poly5</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='poly5' Line='poly5' -->
  <dd>fifth order interior polynomial in x.
  </dd>
  </dl>
  <dl>
  <dt><b>spline3</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='spline3' Line='spline3' -->
  <dd>cubic spline in x.
  </dd>
  </dl>
  <dl>
  <dt><b>sinc</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='sinc' Line='sinc' -->
  <dd>sinc interpolation in x. Users can specify the sinc interpolant width by
  appending a width value to the interpolant string, e.g. sinc51 specifies
  a 51 pixel wide sinc interpolant. The sinc width input by the user will
  be rounded up to the nearest odd number. The default sinc width
  is 31 pixels.
  </dd>
  </dl>
  <dl>
  <dt><b>drizzle</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='drizzle' Line='drizzle' -->
  <dd>1D drizzle resampling. Users can specify the drizzle pixel fraction
  by appending a value between 0.0 and 1.0 in square brackets to the
  interpolant string, e.g. drizzle[0.5]. The default value is 1.0. The
  value 0.0 is increased to 0.001. Drizzle resampling with a pixel fraction
  of 1.0 is identical to linear interpolation.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_boundary_type">
  <dt><b>boundary_type = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary_type' Line='boundary_type = "nearest"' -->
  <dd>Boundary condition for shifts outside the input image.
  The minimum match abbreviated choices are:
  <dl>
  <dt><b><span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"nearest"' -->
  <dd>Use the values of the nearest boundary pixel.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"wrap"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"wrap"' -->
  <dd>Generate a value by wrapping around to the opposite boundary.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"reflect"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"reflect"' -->
  <dd>Generate a value by reflecting around the boundary
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"constant"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"constant"' -->
  <dd>Use a user supplied constant pixel value.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_constant">
  <dt><b>constant = <span style="font-family: monospace;">"0.0"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constant' Line='constant = "0.0"' -->
  <dd>The constant for constant boundary extension.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The list of images in <i>input</i> is shifted by the amount <i>shift</i>
  and copied to the list of output images <i>output</i>.
  The number of output image names must be the same as the number of input
  images.  An output image name may be the same as the corresponding
  input image in which case the shifted image replaces the input image.
  </p>
  <p>
  The shift is defined by the following relation.
  </p>
  <p>
      xout = xint + shift
  </p>
  <p>
  Features in the input image are moved to higher columns when the shift
  is positive and to lower columns when the shift is negative.  For example,
  to shift a feature at column 10 to column 12 the shift is 2.0. The task
  has been optimized for integral pixel shifts.
  </p>
  <p>
  There are five choices for the one dimensional image interpolation
  which is selected with the parameter <i>interp_type</i>.
  The value of the output pixels corresponding to input pixel positions
  outside the boundaries of the image is determined by the parameter
  <i>boundary_type</i>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Shift the lines of an image by 0.25 pixels to the right.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; shiftlines imagein imageout 0.25
  </pre></div>
  <p>
  2. Shift the lines of an image by -.3 pixels using cubic spline interpolation
  and replace the input image by the output image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; shiftlines image image -.3 interp=spline3
  </pre></div>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  <p>
  It requires approximately 28 and 59 seconds to shift a 512 square image
  using linear and cubic spline interpolation respectively
  (Vax 11/750 with fpa).
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imshift, magnify, rotate, imlintran, blkrep, blkav, geotran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIMINGS' 'BUGS' 'SEE ALSO'  -->
  

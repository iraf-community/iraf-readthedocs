.. _imshift:

imshift: Shift a list of 1-D or 2-D images
==========================================

**Package: imgeom**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imshift input output xshift yshift
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of images to be transformed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output images.
  </dd>
  </dl>
  <dl id="l_xshift">
  <dt><b>xshift, yshift</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xshift' Line='xshift, yshift' -->
  <dd>Fractional pixel shift in x and y such that xout = xin + xshift and
  yout = yin + yshift.
  </dd>
  </dl>
  <dl id="l_shifts_file">
  <dt><b>shifts_file = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shifts_file' Line='shifts_file = ""' -->
  <dd>The name of the text file containing the shifts for each input image. If no
  file name is supplied each input image is shifted by <i>xshift</i> and
  <i>yshift</i>. Shifts are listed in the text file, 1 set of shifts per image,
  with the x and y shift in columns 1 and 2 respectively. The number of
  shifts in the file must equal the number of input images.
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
  <dd>nearest neighbor.
  </dd>
  </dl>
  <dl>
  <dt><b>linear</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='linear' Line='linear' -->
  <dd>bilinear interpolation in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>poly3</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='poly3' Line='poly3' -->
  <dd>third order interior polynomial in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>poly5</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='poly5' Line='poly5' -->
  <dd>fifth order interior polynomial in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>spline3</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='spline3' Line='spline3' -->
  <dd>bicubic spline.
  </dd>
  </dl>
  <dl>
  <dt><b>sinc</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='sinc' Line='sinc' -->
  <dd>2D sinc interpolation. Users can specify the sinc interpolant width by
  appending a width value to the interpolant string, e.g. sinc51 specifies
  a 51 by 51 pixel wide sinc interpolant. The sinc width input by the
  user will be rounded up to the nearest odd number. The default sinc width
  is 31 by 31.
  </dd>
  </dl>
  <dl>
  <dt><b>drizzle</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='drizzle' Line='drizzle' -->
  <dd>2D drizzle resampling. Users can specify the drizzle pixel fractions in x and y
  by appending values between 0.0 and 1.0 in square brackets to the
  interpolant string, e.g. drizzle[0.5]. The default value is 1.0. The
  value 0.0 is increased to 0.001. Drizzle resampling with a pixel fraction
  of 1.0 in x and y is identical to bilinear interpolation.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_boundary_type">
  <dt><b>boundary_type = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary_type' Line='boundary_type = "nearest"' -->
  <dd>The choices are:
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
  <dd>Generate value by reflecting about the boundary.
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
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IMSHIFT will shift an image in x and y such that:
  </p>
  <div class="highlight-default-notranslate"><pre>
  xout = xin + xshift
  yout = yin + yshift
  </pre></div>
  <p>
  The output image gray levels are determined by interpolating in the input
  image at the positions of the shifted output pixels.
  IMSHIFT uses the routines in the 2-D interpolator package.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Shift an image by (+3.2, -4.5) using a biquintic interior polynomial
     interpolant and boundary extension.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imshift vys70 vys70shift 3.2 -4.5 inter=poly5 bound=neare
  </pre></div>
  <p>
  2. Shift an image by (-6., 1.2) using bilinear interpolation and
     boundary extension.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imshift ugc1040 ugc1040shift -6.0 1.2 bound=neare
  </pre></div>
  <p>
  3. Shift a set of images using shifts listed in the textfile <span style="font-family: monospace;">"shifts"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; page shifts
  
      3.5  4.86
      -2.  8.9
      10.1 7.8
  
  cl&gt; imshift im1,im2,im3 im1.s,im2.s,im3.s shifts_file=shifts
  </pre></div>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  <p>
  The time required to shift a 512 by 512 real image by fractional pixel
  amounts in x and y is approximately 10, 20, 70, 120, and 120 cpu seconds for the
  nearest neighbor, bilinear, bicubic, biquintic and bicubic spline
  interpolants respectively (Vax 11/750 fpa).
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  shiftlines, magnify, rotate, geomap, geotran, imlintran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIMINGS' 'BUGS' 'SEE ALSO'  -->
  

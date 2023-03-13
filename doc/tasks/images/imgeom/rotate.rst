.. _rotate:

rotate: Rotate and shift a list of 2-D images
=============================================

**Package: imgeom**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rotate input output rotation
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of images to be rotated.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output images.
  </dd>
  </dl>
  <dl id="l_rotation">
  <dt><b>rotation</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rotation' Line='rotation' -->
  <dd>Angle of rotation of the image in degrees. Positive angles will rotate
  the image counter-clockwise from the x axis.
  </dd>
  </dl>
  <dl id="l_xin">
  <dt><b>xin = INDEF, yin = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xin' Line='xin = INDEF, yin = INDEF' -->
  <dd>The origin of the rotation in pixels. Xin and yin default to the center of
  the input image.
  </dd>
  </dl>
  <dl id="l_xout">
  <dt><b>xout = INDEF, yout = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xout' Line='xout = INDEF, yout = INDEF' -->
  <dd>The origin of the output image. Xout and yout default to the center of the
  output image.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = INDEF, nlines = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = INDEF, nlines = INDEF' -->
  <dd>The number of columns and rows in the output image. The default is to
  keep the dimensions the same as the input image. If ncols and nrows is
  less then or equal to zero the program will compute the number of columns
  and rows needed to include the whole image, excluding the effects of
  any origin shifts.
  </dd>
  </dl>
  <dl id="l_interpolant">
  <dt><b>interpolant = <span style="font-family: monospace;">"linear"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interpolant' Line='interpolant = "linear"' -->
  <dd>The interpolant. The options are the following:
  <dl>
  <dt><b>nearest</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nearest' Line='nearest' -->
  <dd>Nearest neighbor.
  </dd>
  </dl>
  <dl>
  <dt><b>linear</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='linear' Line='linear' -->
  <dd>Bilinear interpolation in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>poly3</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='poly3' Line='poly3' -->
  <dd>Third order polynomial in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>poly5</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='poly5' Line='poly5' -->
  <dd>Fifth order polynomial in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>spline3</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='spline3' Line='spline3' -->
  <dd>Bicubic spline.
  </dd>
  </dl>
  <dl>
  <dt><b>sinc</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='sinc' Line='sinc' -->
  <dd>2D sinc interpolation. Users can specify the sinc interpolant width by
  appending a width value to the interpolant string, e.g. sinc51 specifies
  a 51 by 51 pixel wide sinc interpolant. The sinc width will be rounded up to
  the nearest odd number.  The default sinc width is 31 by 31.
  </dd>
  </dl>
  <dl>
  <dt><b>lsinc</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='lsinc' Line='lsinc' -->
  <dd>Look-up table sinc interpolation. Users can specify the look-up table sinc
  interpolant width by appending a width value to the interpolant string, e.g.
  lsinc51 specifies a 51 by 51 pixel wide look-up table sinc interpolant. The user
  supplied sinc width will be rounded up to the nearest odd number. The default
  sinc width is 31 by 31 pixels. Users can specify the resolution of the lookup
  table sinc by appending the look-up table size in square brackets to the
  interpolant string, e.g. lsinc51[20] specifies a 20 by 20 element sinc
  look-up table interpolant with a pixel resolution of 0.05 pixels in x and y.
  The default look-up table size and resolution are 20 by 20 and 0.05 pixels
  in x and y respectively.
  </dd>
  </dl>
  <dl>
  <dt><b>drizzle</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='drizzle' Line='drizzle' -->
  <dd>2D drizzle resampling. Users can specify the drizzle pixel fraction in x and y
  by appending a value between 0.0 and 1.0 in square brackets to the
  interpolant string, e.g. drizzle[0.5]. The default value is 1.0.
  The value 0.0 is increased internally to 0.001. Drizzle resampling
  with a pixel fraction of 1.0 in x and y is equivalent to fractional pixel
  rotated block summing (fluxconserve = yes) or averaging (flux_conserve = no)  if
  xmag and ymag are &gt; 1.0.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_boundary">
  <dt><b>boundary = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary' Line='boundary = "nearest"' -->
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
  <dd>The value of the constant for constant boundary extension.
  </dd>
  </dl>
  <dl id="l_nxblock">
  <dt><b>nxblock = 512, nyblock = 512</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxblock' Line='nxblock = 512, nyblock = 512' -->
  <dd>If the dimensions of the output image are less than nxblock and nyblock
  then the entire image is rotated at once. Otherwise nxblock by nyblock
  segments of the image are rotated.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  ROTATE rotates the list of images in input by rotation degrees and writes
  the output to the images specified by output. The origins of the input and
  output images may be specified by setting xin, yin, xout and yout. The
  transformation is described below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xt = (x - xin) * cos (rotation) - (y - yin) * sin (rotation) + xout
  yt = (x - xin) * sin (rotation) + (y - yin) * cos (rotation) + yout
  </pre></div>
  <p>
  The output image gray levels are determined by interpolating in the input
  image at the positions of the transformed output pixels. ROTATE uses the
  routines in the 2-D interpolation package.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  1. Rotate an image 45 degrees around its center.
  
     cl&gt; rotate m51 m51r45 45.0
  
  2. Rotate an image by 45 degrees around (100., 100.) and
     shift the origin to (150., 150.0) using bicubic interpolation.
  
     cl&gt; rotate m92 m92r45 45.0 xin=100. yin=100. xout=150. yout=150.\
     &gt;&gt;&gt; interp=poly3
  
  3. Rotate an image 90 degrees counter-clockwise and clockwise around its
     center. Note the use of imtranspose and image section notation.
  
     cl&gt; imtranspose m92[*,-*] m92d90
  
     cl&gt; imtranspose m92[-*,*] m92d270
  
  4. Rotate an image 180 degrees counter-clockwise. Note the use of imcopy
     and image section notation.
  
     cl&gt; imcopy m92[-*,-*] m92d180
  </pre></div>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  <p>
  It requires approximately 70 and 290 cpu seconds to rotate a 512 by 512
  real image using bilinear and biquintic interpolation respectively
  (Vax 11/750 fpa).
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The interpolation operation is done in real arithmetic. However the output
  type of the pixels is set equal to the input type. This can lead to truncation
  problems for integer images.
  </p>
  <p>
  Simple 90, 180, 270 etc degree rotations are best performed using the
  imtranspose task and/or image section notation.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imtranspose, imshift, magnify, lintran, geotran, geomap
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIMINGS' 'BUGS' 'SEE ALSO'  -->
  

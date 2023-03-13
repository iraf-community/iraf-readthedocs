.. _imlintran:

imlintran: Linearly transform a list of 2-D images
==================================================

**Package: imgeom**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imlintran input output xrotation yrotation xmag ymag
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
  <dl id="l_xrotation">
  <dt><b>xrotation, yrotation</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xrotation' Line='xrotation, yrotation' -->
  <dd>Angle of rotation of points on the image axes in degrees.
  Positive angles rotate in a counter-clockwise sense around the x axis.
  For a normal coordinate axes rotation xrotation and yrotation should
  be the same. A simple y axis flip can be introduced by make yrotation
  equal to xrotation plus 180 degrees. An axis skew can be introduced by
  making the angle between xrotation and yrotation other than a
  multiple of 90 degrees.
  </dd>
  </dl>
  <dl id="l_xmag">
  <dt><b>xmag, ymag</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmag' Line='xmag, ymag' -->
  <dd>The number of input pixels per output pixel in x and y. The magnifications
  must always be positive numbers. Numbers less than 1 magnify the image;
  numbers greater than one reduce the image.
  </dd>
  </dl>
  <dl id="l_xin">
  <dt><b>xin = INDEF, yin = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xin' Line='xin = INDEF, yin = INDEF' -->
  <dd>The origin of the input picture in pixels. Xin and yin default to the center of
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
  keep the dimensions the same as the input image. If ncols and nrows are
  less than or equal to zero then the task computes the number of rows and
  columns required to include the whole input image, excluding the effects
  of any origin shift.
  </dd>
  </dl>
  <dl id="l_interpolant">
  <dt><b>interpolant = <span style="font-family: monospace;">"linear"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interpolant' Line='interpolant = "linear"' -->
  <dd>The choices are the following.
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
  <dd>Third order interior polynomial in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>poly5</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='poly5' Line='poly5' -->
  <dd>Fifth order interior polynomial in x and y.
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
  <dl id="l_constant">
  <dt><b>constant = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constant' Line='constant = 0.' -->
  <dd>The value of the constant for boundary extension.
  </dd>
  </dl>
  <dl id="l_fluxconserve">
  <dt><b>fluxconserve = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fluxconserve' Line='fluxconserve = yes' -->
  <dd>Preserve the total image flux?
  </dd>
  </dl>
  <dl id="l_nxblock">
  <dt><b>nxblock = 512, nyblock = 512</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxblock' Line='nxblock = 512, nyblock = 512' -->
  <dd>If the size of the output image is less than nxblock by nyblock then
  the entire image is transformed at once. Otherwise the output image
  is computed in blocks of nxblock by nxblock pixels.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IMLINTRAN linearly transforms a the list of images in input using rotation
  angles and magnification factors supplied by the user and writes the output
  images into output. The coordinate transformation from input to output
  image is described below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  1. subtract the origin
  
  xt = x(input) - xin
  yt = y(input) - yin
  
  2. scale the image
  
  xt = xt / xmag
  yt = xt / xmag
  
  3. rotate the image
  
  xt = xt * cos (xrotation) - yt * sin (yrotation)
  yt = xt * sin (yrotation) + yt * cos (yrotation)
  
  4. new orgin
  
  x(output) = xt + xout
  y(output) = yt + yout
  </pre></div>
  <p>
  The output image gray levels are determined by interpolating in the input
  image at the positions of the transformed output pixels using the inverse
  of the above transformation.
  IMLINTRAN uses the routines in the 2-D interpolation package.
  </p>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  <p>
  It requires approximately 70 and 290 cpu seconds respectively to linearly
  transform a 512 by 512 real image using bilinear and biquintic
  interpolation respectively (Vax 11/750 fpa).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  1. Rotate an image 45 degrees around its center and magnify
     the image by a factor of 2. in each direction.
  
     cl&gt; imlintran n4151 n4151rm 45.0 45.0 0.50 0.50
  
  2. Rotate the axes of an image by 45 degrees around 100. and 100.,
     shift the orgin to 150. and 150. and flip the y axis.
  
     cl&gt; imlintran n1068 n1068r 45.0 225.0 1.0 1.0 xin=100. yin=100. \
     &gt;&gt;&gt; xout=150. yout=150.
  
  3. Rotate an image by 45 degrees and reduce the scale in x and y
     by a factor of 1.5
  
     cl&gt; imlintran n7026 n7026rm 45.0 45.0 1.5 1.5
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imshift, magnify, rotate, lintran, register, geotran, geomap
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'TIMINGS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

.. _magnify:

magnify: Magnify a list of 1-D or 2-D images
============================================

**Package: imgeom**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  magnify input output xmag ymag
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of one or two dimensional images to be magnified.  Image sections are
  allowed.  Images with an axis containing only one pixel are not magnified.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output image names.  If the output image name is the same as the input
  image name then the magnified image replaces the input image.
  </dd>
  </dl>
  <dl id="l_xmag">
  <dt><b>xmag, ymag</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmag' Line='xmag, ymag' -->
  <dd>The magnification factors for the first and second image dimensions
  respectively.  The magnifications need not be integers.  Magnifications
  greater than 1 increase the size of the image while negative magnifications
  less than -1 decrease the size by the specified factor.  Magnifications
  between -1 and 1 are interpreted as reciprocal magnifications.
  </dd>
  </dl>
  <dl id="l_x1">
  <dt><b>x1 = INDEF, x2 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='x1' Line='x1 = INDEF, x2 = INDEF' -->
  <dd>The starting and ending coordinates in x in the input image which become
  the first and last pixel in x in the magnified image.  The values need not
  be integers.  If indefinite the values default to the first and last pixel
  in x of the input image; i.e. a value of 1 and nx.
  </dd>
  </dl>
  <dl id="l_y1">
  <dt><b>y1 = INDEF, y2 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='y1' Line='y1 = INDEF, y2 = INDEF' -->
  <dd>The starting and ending coordinates in y in the input image which become
  the first and last pixel in y in the magnified image.  The values need not
  be integers.  If indefinite the values default to the first and last pixel
  in y of the input image; i.e. a value of 1 and ny.
  </dd>
  </dl>
  <dl id="l_dx">
  <dt><b>dx = INDEF, dy = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dx' Line='dx = INDEF, dy = INDEF' -->
  <dd>The intervals between the output pixels in terms of the input image.
  The values need not be integers.  If these values are specified they
  override the magnification factors.
  </dd>
  </dl>
  <dl id="l_interpolant">
  <dt><b>interpolant = <span style="font-family: monospace;">"linear"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interpolant' Line='interpolant = "linear"' -->
  <dd>The interpolant used for rebinning the image.
  The choices are the following.
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
  block summing (fluxconserve = yes) or averaging (flux_conserve = no)  if
  xmag and ymag are &lt; 1.0.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_boundary">
  <dt><b>boundary = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary' Line='boundary = "nearest"' -->
  <dd>Boundary extension type for references to pixels outside the bounds of the
  input image. The choices are:
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
  <dd>Constant value for constant boundary extension.
  </dd>
  </dl>
  <dl id="l_fluxconserve">
  <dt><b>fluxconserve = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fluxconserve' Line='fluxconserve = yes' -->
  <dd>Preserve the total image flux.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = STDOUT</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = STDOUT' -->
  <dd>Log file for recording information about the magnification.  A null
  logfile may be used to turn off log information.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The list of input images are expanded or contracted by interpolation
  to form the output images.  The output image names are specified by the
  output list.  The number of output image names must be the
  same as the number of input images.  An output image name may be the same
  as the corresponding input image in which case the magnified image replaces
  the input image.  The input images must be one or two dimensional and each
  axis must be of at least length 2 (i.e. there have to be distinct
  endpoints between which to interpolate).
  </p>
  <p>
  The magnification factor determines the pixel step size or interval.
  Positive magnifications are related to the step size as the reciprocal;
  for example a magnification of 2.5 implies a step size of .4 and a
  magnification of .2 implies a step size of 5.  Negative magnifications
  are related to the step size as the absolute value; for example a
  magnification of -2.2 implies a step size of 2.2.  This definition
  frees the user from dealing with reciprocals and irrational numbers.
  Note that the step size may be specified directly with the parameters
  <i>dx</i> and <i>dy</i>, in which case the magnification factor is
  not required.
  </p>
  <p>
  If fluxconserve = yes, the magnification is approximately flux conserving
  in that the image values are scaled by the ratio of the output to the input
  pixel areas; i.e dx * dy.
  </p>
  <p>
  In the default case with only the magnifications specified the full
  image is expanded or contracted.  By specifying additional parameters
  the size and origin of the output image may be changed.  Only those
  parameters to be fixed need to be specified and the values of the
  remaining parameters are either determined from these values or
  default as indicated in the PARAMETERS section.
  </p>
  <p>
  The user may select the type of two dimensional interpolation and boundary
  extension to be used.  Note that the image interpolation is performed on
  the boundary extended input image.  Thus, boundary extensions which are
  discontinuous (constant and wrap) may introduce interpolation errors.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To expand an image by a factor of 2.5:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; magnify imagein imageout 2.5 2.5
  </pre></div>
  <p>
  2. To subsample the lines of an image in steps of 3.5:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; magnify imagein imageout dx=3.5 dy=1
  </pre></div>
  <p>
  3. To magnify the central part of an image by 2 into a 11 by 31 image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; magnify imagein imageout 2 2 x1=25.3 x2=30.3 \
  &gt;&gt;&gt; y1=20 y2=35
  </pre></div>
  <p>
  4. To use a higher order interpolator with wrap around boundary extension:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; magnify imagein imageout 2 2 x1=-10 y1=-10 \
  &gt;&gt;&gt; interpolation=spline3 boundary=wrap
  </pre></div>
  <p>
  It is important to remember that the magnification affects the pixel intervals!
  This means that the number of pixels in an expanded image is not simply
  a multiple of the original number.   The following example illustrates this
  point.  Begin with an image which is 100 by 10.  This means the
  x coordinates run between 1 and 100 and the y coordinates run between 1 and
  10 with a pixel interval of 1.
  </p>
  <p>
  Let's magnify the x axis by 0.5 and the y axis by 2.
  The output pixel intervals, in terms of the input pixel intervals,
  are then 2 and 0.5.  This means the output x pixels are at
  1, 3, 5, etc. and output y pixels are at 1, 1.5, 2, 2.5, etc., again in
  terms of the input pixel coordinates.  The last output x pixel is then
  at 99 in the input coordinates and the number of pixels is 50.  For the
  y axis the last output pixel is at 10 in the input coordinates and the
  number of pixels between 1 and 10 in intervals of 0.5 is 19!  Thus, the
  final image is 50 by 19 and not 50 by 20 which you would get if you
  multiplied the axis lengths by the magnification factors.
  </p>
  <p>
  A more complex example is given above in which x1=25.3,
  x2=30.3, y1=20, and y2=35 with magnification factors of 2.
  It is important to understand why the output image is 11 by 31 and
  what the pixel coordinates are in terms of the input pixel coordinates.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imshift, blkavg, rotate, imlintran, register, geotran, geomap
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

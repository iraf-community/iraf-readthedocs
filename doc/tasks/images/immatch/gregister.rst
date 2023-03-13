.. _gregister:

gregister: Register 1-D or 2-D images using the geomap transforms
=================================================================

**Package: immatch**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  gregister input output database transforms
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
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>The name of the text file database produced by GEOMAP containing the coordinate
  transformation(s).
  </dd>
  </dl>
  <dl id="l_transforms">
  <dt><b>transforms</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='transforms' Line='transforms' -->
  <dd>The list of the database record(s) containing the transformations. 
  The number of transforms must be 1 or the same as the number of input
  images.  Transforms is usually the name of the
  text file input to GEOMAP which lists the reference and input
  coordinates of the control points.
  </dd>
  </dl>
  <dl id="l_geometry">
  <dt><b>geometry = <span style="font-family: monospace;">"geometric"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='geometry' Line='geometry = "geometric"' -->
  <dd>The type of geometry to be applied: The choices are:
  <dl>
  <dt><b>linear</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='linear' Line='linear' -->
  <dd>The linear part, shifts, scales and rotations are computed.
  </dd>
  </dl>
  <dl>
  <dt><b>geometric</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='geometric' Line='geometric' -->
  <dd>The full transformation is computed.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_xmin">
  <dt><b>xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmin' Line='xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF' -->
  <dd>The minimum and maximum x and y reference values of the output image.
  Xmin, xmax, ymin and ymax default to minimum and maximum values set in GEOMAP,
  and may not extend beyond the bounds of those parameters.
  </dd>
  </dl>
  <dl id="l_xscale">
  <dt><b>xscale = 1.0, yscale = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xscale' Line='xscale = 1.0, yscale = 1.0' -->
  <dd>The output x and y scales in units of reference x and y
  units per pixel, e.g arcsec / pixel or Angstroms / pixel if the reference
  coordinates
  are arc-seconds or Angstroms. If the reference coordinates are in pixels
  then xscale and yscale should be 1.0 to preserve the scale of the reference
  image. The default is set for pixel coordinates.
  If xscale and yscale are undefined (INDEF), xscale and yscale default to the
  range of the reference coordinates over the range in pixels.
  Xscale and yscale override the values of ncols and nlines.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = INDEF, nlines = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = INDEF, nlines = INDEF' -->
  <dd>The number of columns and lines in the output image. Ncols and nlines default
  to the size of the input image. If xscale or yscale are defined ncols or nlines
  are overridden.
  </dd>
  </dl>
  <dl id="l_xsample">
  <dt><b>xsample = 1.0, ysample = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xsample' Line='xsample = 1.0, ysample = 1.0' -->
  <dd>The coordinate surface subsampling factor. The coordinate surfaces are
  evaluated at every xsample-th pixel in x and every ysample-th pixel in y.
  Transformed coordinates  at intermediate pixel values are determined by
  bilinear interpolation in the coordinate surfaces.
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
  <dd>The boundary extension choices are:
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
  <dd>Preserve the total image flux. The output pixel values are multiplied by
  the Jacobian of the coordinate transformation.
  </dd>
  </dl>
  <dl id="l_nxblock">
  <dt><b>nxblock = 512, nyblock = 512</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxblock' Line='nxblock = 512, nyblock = 512' -->
  <dd>If the dimensions of the output image are less than nxblock and nyblock
  then the entire image is transformed at once. Otherwise blocks of size
  nxblock by nyblock are transformed one at a time.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about the progress of the task ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  GREGISTER corrects an image for geometric distortion using the coordinate
  transformation computed by GEOMAP. The transformation is stored as the
  coefficients of a polynomial surface in record <i>transforms</i>,
  in the text file <i>database</i>.
  The coordinate surface is sampled at every <i>xsample</i> and <i>ysample</i>
  pixel in x and y.
  The transformed coordinates at intermediate pixel values are
  determined by bilinear interpolation in the coordinate surface. If
  <i>xsample</i> and <i>ysample</i> = 1, the coordinate
  surface is evaluated at every pixel. Use of <i>xsample</i> and <i>ysample</i>
  are strongly recommended for large images and high order coordinate
  surfaces in order to reduce the execution time.
  </p>
  <p>
  <i>Xmin</i>, <i>xmax</i>, <i>ymin</i> and <i>ymax</i> define the range of
  reference coordinates represented in the output picture. These numbers
  default to the minimum and maximum x and y reference values used by GEOMAP,
  and may not exceed these values.
  The scale and size of the output picture is determined as follows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ncols = ncols(input)
  if (xscale == INDEF)
      xscale = (xmax - xmin ) / (ncols - 1)
  else
      ncols = (xmax - xmin) / xscale + 1
  
  nlines = nlines(input)
  if (yscale == INDEF)
      yscale = (ymax - ymin ) / (nlines - 1)
  else
      nlines = (ymax - ymin) / yscale + 1
  </pre></div>
  <p>
  The output image gray levels are determined by interpolating in the input
  image at the positions of the transformed output pixels. If the
  <i>fluxconserve</i> switch is set the output pixel values are multiplied by
  the Jacobian of the transformation.  GREGISTER uses the routines in the
  2-D interpolation package.
  </p>
  <p>
  The output image is computed in <i>nxblock</i> by <i>nyblock</i> pixel sections.
  If possible users should set these numbers to values larger than the dimensions
  of the output image, in order to minimize the number of disk reads and writes
  required to compute the output image.  If this is not feasible and the image
  rotation is small users should set nxblock to be greater than the number of
  columns in the output image, and nyblock to be as large as machine memory
  will permit.
  </p>
  <p>
  If the environment variable <i>nomwcs</i> is <span style="font-family: monospace;">"no"</span> then the world coordinate
  system of the input image is modified in the output image to reflect the
  effects of the <i>linear</i> portion of the registration operation.
  Support does not yet exist in the IRAF world coordinate system interface
  for the higher order distortion corrections that GREGISTER is capable
  of performing.
  </p>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  <p>
  It requires approximately 70 and 290 cpu seconds to correct a 512 by 512
  square image for geometric distortion using a low order coordinate surface
  and bilinear and biquintic interpolation respectively (Vax 11/750 far).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <dl id="l_1">
  <dt><b>1.</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='1' Line='1.' -->
  <dd>Transform an image to the reference coordinate system of a 512 by 512 pixel
  square image. The output image will have the same scale and size as the
  reference image if the reference coordinates are in pixels.
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geomap coords database 1.0 512.0 1.0 512.0
  cl&gt; gregister input output database coords
  </pre></div>
  </dd>
  </dl>
  <dl id="l_2">
  <dt><b>2.</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='2' Line='2.' -->
  <dd>Repeat the previous example but rescale the output image. The scale of the
  output image will be 2.5 reference units per pixel and its size will be
  determined by the xmin, xmax, ymin, ymax parameters (1.0, 512.0, 1.0, 512.0).
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geomap coords database 1.0 512.0 1.0 512.0
  cl&gt; gregister input output database coords xscale=2.5 yscale=2.5
  </pre></div>
  </dd>
  </dl>
  <dl id="l_3">
  <dt><b>3.</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='3' Line='3.' -->
  <dd>Correct an image for 3rd order geometric distortion using an output scale of 2
  reference units per pixel unit and bicubic spline interpolation with no flux
  correction. 
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geomap coords database 1.0 512.0 1.0 512.0 xxorder=4 xyorder=4 \
  xxterms=yes yxorder=4 yyorder=4 yxterms=yes
  cl&gt; gregister input output database coords xscale=2. yscale=2. \
  &gt;&gt;&gt; inter=spline3 flux-
  </pre></div>
  </dd>
  </dl>
  <dl id="l_4">
  <dt><b>4.</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='4' Line='4.' -->
  <dd>Transform three images using 3 different transformation records stored
  in the database file.
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geomap coord1,coord2,coord3 database 1. 512. 1. 512.
  cl&gt; gregister im1,im2,im3 imout1,imout2,imout3 database \
  &gt;&gt;&gt; coord1,coord2,coords3
  </pre></div>
  </dd>
  </dl>
  <dl id="l_5">
  <dt><b>5.</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='5' Line='5.' -->
  <dd>Repeat the above example using the textfiles inlist, outlist, reclist which
  contain the list of input images, list of output images and list of coordinate
  files respectively.
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geomap @reclist database 1. 512. 1. 512.
  cl&gt; gregister @inlist @outlist database @reclist
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Support does yet exist in the IRAF world coordinate system interface
  for the higher order distortion corrections that GREGISTER is capable
  of performing.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imshift, magnify, rotate, imlintran, geomap, geotran, geoxytran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'TIMINGS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

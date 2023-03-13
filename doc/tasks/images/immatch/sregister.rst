.. _sregister:

sregister: Register 1-D or 2-D images using the image celestial wcs
===================================================================

**Package: immatch**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  sregister input reference output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input images containing the input celestial coordinate wcs.
  </dd>
  </dl>
  <dl id="l_reference">
  <dt><b>reference</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reference' Line='reference' -->
  <dd>The list of reference images containing the reference celestial coordinate wcs.
  The number of reference images must be one or equal to the number of
  input images.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The list of output registered images. The number of output images must
  be equal to the number of input images.
  </dd>
  </dl>
  <dl id="l_xmin">
  <dt><b>xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmin' Line='xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF' -->
  <dd>The minimum and maximum logical x and logical y coordinates used to, generate
  the grid of reference image control points, define the region of validity of
  the spatial transformation, and define the extent of the output image.
  Xmin, xmax, ymin, and
  ymax are assigned defaults of 1, the number of columns in the reference 
  image, 1, and the number of lines in the reference image, respectively.
  </dd>
  </dl>
  <dl id="l_nx">
  <dt><b>nx = 10, ny = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nx' Line='nx = 10, ny = 10' -->
  <dd>The number of points in x and y used to generate the coordinate grid.
  </dd>
  </dl>
  <dl id="l_wcs">
  <dt><b>wcs = <span style="font-family: monospace;">"world"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcs' Line='wcs = "world"' -->
  <dd>The world coordinate system of the coordinates.  The options are:
  <dl>
  <dt><b>physical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='physical' Line='physical' -->
  <dd>Physical coordinates are pixel coordinates which are invariant with
  respect to linear transformations of the physical image data.  For example,
  if the reference 
  image is a rotated section of a larger input image, the physical
  coordinates of an object in the reference image are equal to the physical
  coordinates of the same object in the input image, although the logical
  pixel coordinates are different.
  </dd>
  </dl>
  <dl>
  <dt><b>world</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='world' Line='world' -->
  <dd>World coordinates are image coordinates which are invariant with
  respect to linear transformations of the physical image data and which
  are in decimal degrees for celestial coordinate systems. Obviously if the
  wcs is correct the ra and dec of an object
  should remain the same no matter how the image
  is linearly transformed. The default world coordinate
  system is either 1) the value of the environment variable <span style="font-family: monospace;">"defwcs"</span> if
  set in the user's IRAF environment (normally it is undefined) and present
  in the image header, 2) the value of the <span style="font-family: monospace;">"system"</span>
  attribute in the image header keyword WAT0_001 if present in the
  image header or, 3) the <span style="font-family: monospace;">"physical"</span> coordinate system.
  Care must be taken that the wcs of the input and
  reference images are compatible, e.g. it makes no sense to
  match the coordinates of a 2D sky projection and a 2D spectral wcs.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_xformat">
  <dt><b>xformat = <span style="font-family: monospace;">"%10.3f"</span>, yformat = <span style="font-family: monospace;">"%10.3f"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xformat' Line='xformat = "%10.3f", yformat = "%10.3f"' -->
  <dd>The format of the output logical x and y reference and input pixel
  coordinates in columns 1 and 2 and 3 and 4 respectively. By default the
  coordinates are output right justified in a field of ten spaces with
  3 digits following the decimal point. 
  </dd>
  </dl>
  <dl id="l_rwxformat">
  <dt><b>rwxformat = <span style="font-family: monospace;">""</span>, rwyformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rwxformat' Line='rwxformat = "", rwyformat = ""' -->
  <dd>The format of the output world x and y reference image coordinates
  in columns 5 and 6 respectively. The internal default formats will give
  reasonable output formats and precision for celestial coordinate
  systems.
  </dd>
  </dl>
  <dl id="l_wxformat">
  <dt><b>wxformat = <span style="font-family: monospace;">""</span>, wyformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wxformat' Line='wxformat = "", wyformat = ""' -->
  <dd>The format of the output world x and y input image coordinates
  in columns 7 and 8 respectively. The internal default formats will give
  reasonable output formats and precision for celestial coordinate
  systems.
  </dd>
  </dl>
  <dl id="l_fitgeometry">
  <dt><b>fitgeometry = <span style="font-family: monospace;">"general"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitgeometry' Line='fitgeometry = "general"' -->
  <dd>The fitting geometry to be used. The options are the following.
  <dl>
  <dt><b>shift</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='shift' Line='shift' -->
  <dd>X and y shifts only are fit.
  </dd>
  </dl>
  <dl>
  <dt><b>xyscale</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='xyscale' Line='xyscale' -->
  <dd>X and y shifts and x and y magnification factors are fit. Axis flips are
  allowed for.
  </dd>
  </dl>
  <dl>
  <dt><b>rotate</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='rotate' Line='rotate' -->
  <dd>X and y shifts and a rotation angle are fit. Axis flips are allowed for.
  </dd>
  </dl>
  <dl>
  <dt><b>rscale</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='rscale' Line='rscale' -->
  <dd>X and y shifts, a magnification factor assumed to be the same in x and y, and a
  rotation angle are fit. Axis flips are allowed for.
  </dd>
  </dl>
  <dl>
  <dt><b>rxyscale</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='rxyscale' Line='rxyscale' -->
  <dd>X and y shifts, x and y magnifications factors, and a rotation angle are fit.
  Axis flips are allowed for.
  </dd>
  </dl>
  <dl>
  <dt><b>general</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='general' Line='general' -->
  <dd>A polynomial of arbitrary order in x and y is fit. A linear term and a
  distortion term are computed separately. The linear term includes an x and y
  shift, an x and y scale factor, a rotation and a skew.  Axis flips are also
  allowed for in the linear portion of the fit. The distortion term consists
  of a polynomial fit to the residuals of the linear term. By default the
  distortion terms is set to zero.
  </dd>
  </dl>
  For all the fitting geometries except <span style="font-family: monospace;">"general"</span> no distortion term is fit,
  i.e. the x and y polynomial orders are assumed to be 2 and the cross term
  switches are set to <span style="font-family: monospace;">"none"</span>, regardless of the values of the <i>xxorder</i>,
  <i>xyorder</i>, <i>xxterms</i>, <i>yxorder</i>, <i>yyorder</i> and <i>yxterms</i>
  parameters set by the user.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"polynomial"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "polynomial"' -->
  <dd>The type of analytic coordinate surfaces to be fit. The options are the
  following:
  <dl>
  <dt><b>legendre</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='legendre' Line='legendre' -->
  <dd>Legendre polynomials in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>chebyshev</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='chebyshev' Line='chebyshev' -->
  <dd>Chebyshev polynomials in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>polynomial</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='polynomial' Line='polynomial' -->
  <dd>Power series polynomials in x and y.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_xxorder">
  <dt><b>xxorder = 2, xyorder = 2, yxorder = 2, yyorder = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xxorder' Line='xxorder = 2, xyorder = 2, yxorder = 2, yyorder = 2' -->
  <dd>The order of the polynomials in x and y for the x and y fits respectively.
  The default order and cross term settings define the linear term in x
  and y, where the 6 coefficients can be interpreted in terms of an x and y shift,
  an x and y scale change, and rotations of the x and y axes. The <span style="font-family: monospace;">"shift"</span>,
  <span style="font-family: monospace;">"xyscale"</span>, <span style="font-family: monospace;">"rotation"</span>, <span style="font-family: monospace;">"rscale"</span>, and <span style="font-family: monospace;">"rxyscale"</span>, fitting geometries
  assume that the polynomial order parameters are 2 regardless of the values
  set by the user. If any of the order parameters are higher than 2 and
  <i>fitgeometry</i> is <span style="font-family: monospace;">"general"</span>, then a distortion surface is fit to the
  residuals from the linear portion of the fit.
  </dd>
  </dl>
  <dl id="l_xxterms">
  <dt><b>xxterms = <span style="font-family: monospace;">"half"</span>, yxterms = <span style="font-family: monospace;">"half"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xxterms' Line='xxterms = "half", yxterms = "half"' -->
  <dd>The options are:
  <dl>
  <dt><b>none</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='none' Line='none' -->
  <dd>The individual polynomial terms contain powers of x or powers of y but not
  powers of both.
  </dd>
  </dl>
  <dl>
  <dt><b>half</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='half' Line='half' -->
  <dd>The individual polynomial terms contain powers of x and powers of y, whose
  maximum combined power is MAX (xxorder - 1, xyorder - 1) for the x fit and
  MAX (yxorder - 1, yyorder - 1) for the y fit.
  </dd>
  </dl>
  <dl>
  <dt><b>full</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='full' Line='full' -->
  <dd>The individual polynomial terms contain powers of x and powers of y, whose
  maximum combined power is MAX (xxorder - 1 + xyorder - 1) for the x fit and
  MAX (yxorder - 1 + yyorder - 1) for the y fit.
  </dd>
  </dl>
  The <span style="font-family: monospace;">"shift"</span>, <span style="font-family: monospace;">"xyscale"</span>, <span style="font-family: monospace;">"rotation"</span>, <span style="font-family: monospace;">"rscale"</span>, and <span style="font-family: monospace;">"rxyscale"</span> fitting
  geometries, assume that the cross term switches are set to <span style="font-family: monospace;">"none"</span>regardless
  of the values set by the user.  If either of the cross terms parameters is
  set to <span style="font-family: monospace;">"half"</span> or <span style="font-family: monospace;">"full"</span> and <i>fitgeometry</i> is <span style="font-family: monospace;">"general"</span> then a distortion
  surface is fit to the residuals from the linear portion of the fit.
  </dd>
  </dl>
  <dl id="l_reject">
  <dt><b>reject = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reject' Line='reject = INDEF' -->
  <dd>The rejection limit in units of sigma. The default is no rejection.
  </dd>
  </dl>
  <dl id="l_calctype">
  <dt><b>calctype = <span style="font-family: monospace;">"real"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='calctype' Line='calctype = "real"' -->
  <dd>The precision of coordinate transformation calculations. The options are <span style="font-family: monospace;">"real"</span>
  and <span style="font-family: monospace;">"double"</span>.
  </dd>
  </dl>
  <dl id="l_geometry">
  <dt><b>geometry = <span style="font-family: monospace;">"geometric"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='geometry' Line='geometry = "geometric"' -->
  <dd>The type of geometric transformation.  The options are:
  <dl>
  <dt><b>linear</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='linear' Line='linear' -->
  <dd>Perform only the linear part of the geometric transformation.
  </dd>
  </dl>
  <dl>
  <dt><b>geometric</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='geometric' Line='geometric' -->
  <dd>Compute both the linear and distortion portions of the geometric correction.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_xsample">
  <dt><b>xsample = 1.0, ysample = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xsample' Line='xsample = 1.0, ysample = 1.0' -->
  <dd>The coordinate surface subsampling factor. The coordinate surfaces are
  evaluated at every xsample-th pixel in x and every ysample-th pixel in y.
  Transformed coordinates  at intermediate pixel values are determined by
  bilinear interpolation in the coordinate surfaces. If the coordinate
  surface is of high order setting these numbers to some reasonably high
  value is recommended.
  </dd>
  </dl>
  <dl id="l_interpolant">
  <dt><b>interpolant = <span style="font-family: monospace;">"linear"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interpolant' Line='interpolant = "linear"' -->
  <dd>The interpolant used for rebinning the image.  The choices are the following.
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
  <dd>Use a user supplied constant value.
  </dd>
  </dl>
  <dl>
  <dt><b>reflect</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='reflect' Line='reflect' -->
  <dd>Generate a value by reflecting about the boundary of the image.
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
  <dt><b>constant = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constant' Line='constant = 0.0' -->
  <dd>The value of the constant for boundary extension.
  </dd>
  </dl>
  <dl id="l_fluxconserve">
  <dt><b>fluxconserve = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fluxconserve' Line='fluxconserve = yes' -->
  <dd>Preserve the total image flux? If flux conservation is turned on, the output
  pixel values are multiplied by the Jacobian of the coordinate transformation.
  </dd>
  </dl>
  <dl id="l_nxblock">
  <dt><b>nxblock = 512, nyblock = 512</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxblock' Line='nxblock = 512, nyblock = 512' -->
  <dd>If the size of the output image is less than nxblock by nyblock then
  the entire image is transformed at once. Otherwise the output image
  is computed in blocks nxblock by nyblock pixels.
  </dd>
  </dl>
  <dl id="l_wcsinherit">
  <dt><b>wcsinherit = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcsinherit' Line='wcsinherit = yes' -->
  <dd>Inherit the wcs of the reference image?
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about the progress of the task?
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Run the task interactively ?
  In interactive mode the user may interact with the fitting process, e.g.
  change the order of the fit, delete points, replot the data etc.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>The graphics device.
  </dd>
  </dl>
  <dl id="l_gcommands">
  <dt><b>gcommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gcommands' Line='gcommands = ""' -->
  <dd>The graphics cursor.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  SREGISTER computes the spatial transformation function required to register
  the input image <i>input</i> to the reference image <i>reference</i>,
  and writes the registered input image to the output image <i>output</i>. 
  The input and reference images may be 1D or 2D but must have
  the same dimensionality.  SREGISTER assumes that the world
  coordinate systems in the input and reference
  image headers are accurate and that both systems are compatible, e.g. both
  images have a celestial coordinate system WCS.
  </p>
  <p>
  SREGISTER computes the required spatial transformation by matching the logical
  x and y pixel coordinates of a grid of points 
  in the input image with the logical x and y pixels coordinates
  of the same grid of points in the reference image,
  using world coordinate information stored in the two image headers.
  The coordinate grid consists of <i>nx * ny</i> points evenly distributed
  over the logical pixel space of interest in the reference image defined by the
  <i>xmin</i>, <i>xmax</i>, <i>ymin</i>, <i>ymax</i> parameters.
  The reference image celestial coordinates are transformed to
  input image celestial coordinates using world coordinate
  system information in both the reference and the input image headers.
  Finally the input image celestial coordinates are transformed to logical x and y
  input image pixel coordinates using world coordinate system information
  stored in the input image header. The transformation sequence looks
  like the following for an equatorial celestial coordinate system:
  </p>
  <div class="highlight-default-notranslate"><pre>
     (x,y) reference -&gt; (ra,dec) reference  (reference image wcs)
  (ra,dec) reference -&gt; (ra,dec) input      (reference and input image wcs)
      (ra,dec) input -&gt; (x,y) input         (input image wcs)
  </pre></div>
  <p>
  The computed reference and input logical coordinates and the
  celestial coordinates are written to a temporary output coordinates file
  which is deleted on task termination. The pixel and celestial coordinates
  are output using the <i>xformat</i> and <i>yformat</i> and the <i>rwxformat</i>,
  <i>rwyformat</i>, <i>wxformat</i> and <i>wxformat</i>
  parameters respectively. If these formats are undefined and, in the
  case of the celestial coordinates a format attribute cannot be
  read from either the reference or the input images, the coordinates are
  output in %g format with <i>min_sigdigits</i> digits of precision.
  If the reference and input images are 1D then all the output logical and
  world y coordinates are set to 1.
  </p>
  <p>
  SREGISTER computes a spatial transformation of the following form.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xin = f (xref, yref)
  yin = g (xref, yref)
  </pre></div>
  <p>
  The functions f and g are either a power series polynomial or a Legendre or
  Chebyshev polynomial surface of order
  <i>xxorder</i> and <i>xyorder</i> in x and <i>yxorder</i> and <i>yyorder</i> in y.
  </p>
  <p>
  Several polynomial cross terms options are available. Options <span style="font-family: monospace;">"none"</span>,
  <span style="font-family: monospace;">"half"</span>, and <span style="font-family: monospace;">"full"</span> are illustrated below for a quadratic polynomial in
  x and y.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xxterms = "none", xyterms = "none"
  xxorder = 3, xyorder = 3, yxorder = 3, yyorder = 3
  
     xin = a11 + a21 * xref + a12 * yref +
           a31 * xref ** 2 + a13 * yref ** 2
     yin = a11' + a21' * xref + a12' * yref +
           a31' * xref ** 2 + a13' * yref ** 2
  
  xxterms = "half", xyterms = "half"
  xxorder = 3, xyorder = 3, yxorder = 3, yyorder = 3
  
     xin = a11 + a21 * xref + a12 * yref +
           a31 * xref ** 2 + a22 * xref * yref + a13 * yref ** 2
     yin = a11' + a21' * xref + a12' * yref +
           a31' * xref ** 2 + a22' * xref * yref + a13' * yref ** 2
  
  xxterms = "full", xyterms = "full"
  xxorder = 3, xyorder = 3, yxorder = 3, yyorder = 3
  
     xin = a11 + a21 * xref + a31 * xref ** 2 +
           a12 * yref + a22 * xref * yref +  a32 * xref ** 2 * yref +
           a13 * yref ** 2 + a23 * xref *  yref ** 2 +
           a33 * xref ** 2 * yref ** 2
     yin = a11' + a21' * xref + a31' * xref ** 2 +
           a12' * yref + a22' * xref * yref +  a32' * xref ** 2 * yref +
           a13' * yref ** 2 + a23' * xref *  yref ** 2 +
           a33' * xref ** 2 * yref ** 2
  </pre></div>
  <p>
  The computation can be done in either real or
  double precision by setting the <i>calctype</i> parameter.
  Automatic pixel rejection may be enabled by setting the <i>reject</i>
  parameter to some number &gt; 0.0.
  </p>
  <p>
  The transformation computed by the <span style="font-family: monospace;">"general"</span> fitting geometry is arbitrary
  and does not correspond to a physically meaningful model. However the computed
  coefficients for the linear term can be given a simple geometrical geometric
  interpretation for all the fitting geometries as shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  fitting geometry = general (linear term)
      xin = a + b * xref + c * yref
      yin = d + e * xref + f * yref
  
  fitting geometry = shift
      xin = a + xref
      yin = d + yref
  
  fitting geometry = xyscale
      xin = a + b * xref
      yin = d + f * yref
  
  fitting geometry = rotate
      xin = a + b * xref + c * yref
      yin = d + e * xref + f * yref
      b * f - c * e = +/-1
      b = f, c = -e or b = -f, c = e
  
  fitting geometry = rscale
      xin = a + b * xref + c * yref
      yin = d + e * xref + f * yref
      b * f - c * e = +/- const
      b = f, c = -e or b = -f, c = e
  
  fitting geometry = rxyscale
      xin = a + b * xref + c * yref
      yin = d + e * xref + f * yref
      b * f - c * e = +/- const
  </pre></div>
  <p>
  The coefficients can be interpreted as follows. Xref0, yref0, xin0, yin0
  are the origins in the reference and input frames respectively. Orientation
  and skew are the orientation of the x and y axes and their deviation from
  perpendicularity respectively. Xmag and ymag are the scaling factors in x and
  y and are assumed to be positive.
  </p>
  <div class="highlight-default-notranslate"><pre>
  general (linear term)
      xrotation = rotation - skew / 2
      yrotation = rotation + skew / 2
      b = xmag * cos (xrotation)
      c = ymag * sin (yrotation)
      e = -xmag * sin (xrotation)
      f = ymag * cos (yrotation)
      a = xin0 - b * xref0 - c * yref0 = xshift
      d = yin0 - e * xref0 - f * yref0 = yshift
  
  shift
      xrotation = 0.0,  yrotation = 0.0
      xmag = ymag = 1.0
      b = 1.0
      c = 0.0
      e = 0.0
      f = 1.0
      a = xin0 - xref0 = xshift
      d = yin0 - yref0 = yshift
  
  xyscale
      xrotation 0.0 / 180.0 yrotation = 0.0
      b = + /- xmag
      c = 0.0
      e = 0.0
      f = ymag
      a = xin0 - b * xref0 = xshift
      d = yin0 - f * yref0 = yshift
  
  rscale
      xrotation = rotation + 0 / 180, yrotation = rotation
      mag = xmag = ymag
      const = mag * mag
      b = mag * cos (xrotation)
      c = mag * sin (yrotation)
      e = -mag * sin (xrotation)
      f = mag * cos (yrotation)
      a = xin0 - b * xref0 - c * yref0 = xshift
      d = yin0 - e * xref0 - f * yref0 = yshift
  
  rxyscale
      xrotation = rotation + 0 / 180, yrotation = rotation
      const = xmag * ymag
      b = xmag * cos (xrotation)
      c = ymag * sin (yrotation)
      e = -xmag * sin (xrotation)
      f = ymag * cos (yrotation)
      a = xin0 - b * xref0 - c * yref0 = xshift
      d = yin0 - e * xref0 - f * yref0 = yshift
  </pre></div>
  <p>
  <i>Xmin</i>, <i>xmax</i>, <i>ymin</i> and <i>ymax</i> define the region of
  validity of the transformation as well as the limits of the grid
  in the reference coordinate system.
  </p>
  <p>
  Each computed transformation is written to the a temporary output text database
  file which is deleted on task termination. Otherwise the
  database file is opened in append mode and new records are written
  to the end of the existing file. If more that one record of the same
  name is written to the database file, the last record written is the
  valid record.
  </p>
  <p>
  SREGISTER will terminate with an error if the reference and input images
  are not both either 1D or 2D.
  If the world coordinate system information cannot be read from either
  the reference or input image header, the requested transformations
  from the world &lt;-&gt; logical coordinate systems cannot be compiled for either
  or both images, or the world coordinate systems of the reference and input
  images are fundamentally incompatible in some way, the output logical
  reference and input image coordinates are both set to a grid of points
  spanning the logical pixel space of the input, not the reference image.
  This grid of points defines an identity transformation which results in
  an output image equal to the input image.
  </p>
  <p>
  SREGISTER computes the output image by evaluating the fitted coordinate
  surfaces and interpolating in the input image at position of the transformed
  coordinates. The scale of the output image is the same as the scale of the
  reference image. The extent and size of the output image are determined
  by the <i>xmin</i>, <i>xmax</i>, <i>ymin</i>, and <i>ymax</i> parameters
  as shown below
  </p>
  <div class="highlight-default-notranslate"><pre>
  xmin &lt;= x &lt;= xmax
  ymin &lt;= x &lt;= ymax
  ncols =  xmax - xmin + 1
  nlines = xmax - xmin + 1
  </pre></div>
  <p>
  SREGISTER samples the coordinate surfaces at every <i>xsample</i> and 
  <i>ysample</i> pixels in x and y.
  The transformed coordinates at intermediate pixel values are
  determined by bilinear interpolation in the coordinate surface. If
  <i>xsample</i> and <i>ysample</i> = 1, the coordinate
  surface is evaluated at every pixel. Use of <i>xsample</i> and <i>ysample</i>
  are strongly recommended for large images and high order coordinate
  surfaces in order to reduce the time required to compute the output image.
  </p>
  <p>
  The output image gray levels are determined by interpolating in the input
  image at the positions of the transformed output pixels using the
  interpolant specified by the <i>interpolant</i> parameter. If the
  <i>fluxconserve</i> switch is set the output pixel values are multiplied by
  the Jacobian of the transformation, which preserves the flux of the entire
  image. Out-of-bounds pixels are evaluated using the <i>boundary</i> and
  <i>constant</i> parameters.
  </p>
  <p>
  The output image is computed in <i>nxblock</i> by <i>nyblock</i> pixel sections.
  If possible users should set these number to values larger than the dimensions
  of the output image in order to minimize the number of disk reads and writes
  required to compute the output image. If this is not feasible and the image
  rotation is small, users should set nxblock to be greater than the number of
  columns in the output image, and nyblock to be as large as machine memory
  will permit.
  </p>
  <p>
  If <i>wcsinherit</i> = <span style="font-family: monospace;">"yes"</span>, then the output image will inherit the world
  coordinate system of the reference image.
  Otherwise if the environment variable <i>nomwcs</i> is <span style="font-family: monospace;">"no"</span> the world
  coordinate
  system of the input image is modified in the output image to reflect the
  effects of the <i>linear</i> portion of the registration operation.
  Support does not yet exist in the IRAF world coordinate system interface
  for the higher order distortion corrections that SREGISTER is capable
  of performing.
  </p>
  <p>
  If <i>verbose</i> is <span style="font-family: monospace;">"yes"</span> then messages about the progress of the task
  as well as warning messages indicating potential problems
  are written to the standard output.
  </p>
  <p>
  SREGISTER may be run interactively by setting the <i>interactive</i>
  parameter to <span style="font-family: monospace;">"yes"</span>.
  In interactive mode the user has the option of viewing the fitted
  spatial transformation, changing the
  fit parameters, deleting and undeleting points, and replotting
  the data until a satisfactory
  fit has been achieved.
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  In interactive mode the following cursor commands are currently available.
  </p>
  <div class="highlight-default-notranslate"><pre>
          Interactive Keystroke Commands
  
  ?       Print options
  f       Fit the data and graph with the current graph type (g, x, r, y, s)
  g       Graph the data and the current fit
  x,r     Graph the x fit residuals versus x and y respectively
  y,s     Graph the y fit residuals versus x and y respectively
  d,u     Delete or undelete the data point nearest the cursor
  o       Overplot the next graph
  c       Toggle the constant x, y plotting option
  t       Plot a line of constant x, y through the nearest data point
  l       Print xshift, yshift, xmag, ymag, xrotate, yrotate
  q       Exit the interactive curve fitting
  </pre></div>
  <p>
  The parameters listed below can be changed interactively with simple colon
  commands. Typing the parameter name alone will list the current value.
  </p>
  <div class="highlight-default-notranslate"><pre>
          Colon Parameter Editing Commands
  
  :show                           List parameters
  :fitgeometry                    Fitting geometry (shift,xyscale,rotate,
                                  rscale,rxyscale,general)
  :function [value]               Fitting function (chebyshev,legendre,
                                  polynomial)
  :xxorder :xyorder [value]       X fitting function xorder, yorder
  :yxorder :yyorder [value]       Y fitting function xorder, yorder
  :xxterms :yxterms [n/h/f]       X, Y fit cross term types
  :reject [value]                 Rejection threshold
  </pre></div>
  </section>
  <section id="s_formats">
  <h3>Formats</h3>
  <p>
  A  format  specification has the form <span style="font-family: monospace;">"%w.dCn"</span>, where w is the field
  width, d is the number of decimal places or the number of digits  of
  precision,  C  is  the  format  code,  and  n is radix character for
  format code <span style="font-family: monospace;">"r"</span> only.  The w and d fields are optional.  The  format
  codes C are as follows:
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  b       boolean (YES or NO)
  c       single character (c or '\c' or '\0nnn')
  d       decimal integer
  e       exponential format (D specifies the precision)
  f       fixed format (D specifies the number of decimal places)
  g       general format (D specifies the precision)
  h       hms format (hh:mm:ss.ss, D = no. decimal places)
  m       minutes, seconds (or hours, minutes) (mm:ss.ss)
  o       octal integer
  rN      convert integer in any radix N
  s       string (D field specifies max chars to print)
  t       advance To column given as field W
  u       unsigned decimal integer
  w       output the number of spaces given by field W
  x       hexadecimal integer
  z       complex format (r,r) (D = precision)
  
  Conventions for w (field width) specification:
  
      W =  n      right justify in field of N characters, blank fill
          -n      left justify in field of N characters, blank fill
          0n      zero fill at left (only if right justified)
  absent, 0       use as much space as needed (D field sets precision)
  
  Escape sequences (e.g. "\n" for newline):
  
  \b      backspace   (not implemented)
       formfeed
  \n      newline (crlf)
  \r      carriage return
  \t      tab
  \"      string delimiter character
  \'      character constant delimiter character
  \\      backslash character
  \nnn    octal value of character
  
  Examples
  
  %s          format a string using as much space as required
  %-10s       left justify a string in a field of 10 characters
  %-10.10s    left justify and truncate a string in a field of 10 characters
  %10s        right justify a string in a field of 10 characters
  %10.10s     right justify and truncate a string in a field of 10 characters
  
  %7.3f       print a real number right justified in floating point format
  %-7.3f      same as above but left justified
  %15.7e      print a real number right justified in exponential format
  %-15.7e     same as above but left justified
  %12.5g      print a real number right justified in general format
  %-12.5g     same as above but left justified
  
  %h          format as nn:nn:nn.n
  %15h        right justify nn:nn:nn.n in field of 15 characters
  %-15h       left justify nn:nn:nn.n in a field of 15 characters
  %12.2h      right justify nn:nn:nn.nn
  %-12.2h     left justify nn:nn:nn.nn
  
  %H          / by 15 and format as nn:nn:nn.n
  %15H        / by 15 and right justify nn:nn:nn.n in field of 15 characters
  %-15H       / by 15 and left justify nn:nn:nn.n in field of 15 characters
  %12.2H      / by 15 and right justify nn:nn:nn.nn
  %-12.2H     / by 15 and left justify nn:nn:nn.nn
  
  \n          insert a newline
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Additional  information  on  IRAF  world  coordinate  systems including
  more detailed descriptions of the <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"physical"</span>, and <span style="font-family: monospace;">"world"</span>
  coordinate systems can be found  in  the  help  pages  for  the  WCSEDIT
  and  WCRESET  tasks. Detailed   documentation   for  the  IRAF  world
  coordinate  system interface MWCS can be found in  the  file
  <span style="font-family: monospace;">"iraf$sys/mwcs/MWCS.hlp"</span>.  This  file  can  be  formatted  and  printed
  with the command <span style="font-family: monospace;">"help iraf$sys/mwcs/MWCS.hlp fi+ | lprint"</span>.
  </p>
  <p>
  Details of the FITS header world coordinate system interface can
  be found in the draft paper <span style="font-family: monospace;">"World Coordinate Systems Representations Within the
  FITS Format"</span> by Hanisch and Wells, available from the iraf anonymous ftp
  archive and the draft paper which supersedes it <span style="font-family: monospace;">"Representations of Celestial
  Coordinates in FITS"</span> by Greisen and Calabretta available from the NRAO
  anonymous ftp archives.
  </p>
  <p>
  The spherical astronomy routines employed here are derived from the Starlink
  SLALIB library provided courtesy of Patrick Wallace. These routines
  are very well documented internally with extensive references provided
  where appropriate. Interested users are encouraged to examine the routines
  for this information. Type <span style="font-family: monospace;">"help slalib"</span> to get a listing of the SLALIB
  routines, <span style="font-family: monospace;">"help slalib opt=sys"</span> to get a concise summary of the library,
  and <span style="font-family: monospace;">"help &lt;routine&gt;"</span> to get a description of each routine's calling sequence,
  required input and output, etc. An overview of the library can be found in the
  paper <span style="font-family: monospace;">"SLALIB - A Library of Subprograms"</span>, Starlink User Note 67.7
  by P.T. Wallace, available from the Starlink archives.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Register a radio image to an X-ray image of the same field using
  a 100 point coordinate  grid and a simple linear transformation.  Both
  images have accurate sky projection world coordinate systems. Print the
  output world coordinates in the coords file in hh:mm:ss.ss and dd:mm:ss.s
  format. Display the input and output image and blink them.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sregister radio xray radio.tran rwxformat=%12.2H \
      rwyformat=%12.1h wxformat=%12.2H wyformat=%12.1h
  
  cl&gt; display radio 1 fi+
  
  cl&gt; display radio.tran 2 fi+
  </pre></div>
  <p>
  2. Repeat the previous command but begin with a higher order fit
  and run the task in interactive mode in order to examine the fit
  residuals.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sregister radio xray radio.tran rwxformat=%12.2H \
      rwyformat=%12.1h wxformat=%12.2H wyformat=%12.1h xxo=4 \
      xyo=4 xxt=half yxo=4 yyo=4 yxt=half  inter+
  
      ... a plot of the fit appears
  
      ... type x and r to examine the residuals of the x
          surface fit versus x and y
  
      ... type y and s to examine the residuals of the y
          surface fit versus x and y
  
      ... delete 2 deviant points with the d key and
          recompute the fit with the f key
  
      ... type q to quit, save the fit, and compute the registered
          image
  </pre></div>
  <p>
  3. Mosaic a set of 9 images covering a ~ 1 degree field into a single image
  centered at  12:32:53.1 +43:13:03. Set the output image scale to 0.5
  arc-seconds / pixel which is close the detector scale of 0.51 arc-seconds
  per pixel. Set the orientation to be north up and east to the left.
  The 9 images all have accurate world coordinate information in their headers.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Create a dummy reference image big enough to cover 1 square degree
  
  cl&gt; mkpattern refimage ncols=7200 nlines=7200 ...
  
  # Give the dummy reference image the desired coordinate system
  
  cl&gt; ccsetwcs refimage "" xref=3600.5 yref=3600.5 xmag=-0.5 \
  ymag=0.5 lngref=12:32:53.1 latref=43:13:03 ...
  
  # Register the images using constant boundary extension and set
  # uservalue to some reasonable value outside the good data range.
  # It may be possible to improve performance by increasing nxblock
  # and nyblock.
  
  cl&gt; sregister @inlist refimage @outlist boundary=constant \
  constant=&lt;uservalue&gt; nxblock=7200 nyblock=1024 ...
  
  # Combine the images using imcombine
  
  cl&gt; imcombine @outlist mosaic lthreshold=&lt;uservalue&gt; ...
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imalign,xregister,register,geotran,wregister
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'FORMATS' 'REFERENCES' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

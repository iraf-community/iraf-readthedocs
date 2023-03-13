.. _skymap:

skymap: Compute geometric transforms using the image celestial wcs
==================================================================

**Package: immatch**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  skymap input reference database
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
  <dd>The list of reference images containing the reference celestial coordinate
  wcs. The number of reference images must be one or equal to the number
  of input images.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>The name of the output text database file containing the computed
  transformations.
  </dd>
  </dl>
  <dl id="l_transforms">
  <dt><b>transforms = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='transforms' Line='transforms = ""' -->
  <dd>An option transform name list. If transforms is undefined then the
  transforms are assigned record names equal to the input image names.
  </dd>
  </dl>
  <dl id="l_results">
  <dt><b>results = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='results' Line='results = ""' -->
  <dd>Optional output files containing a summary of the results including a
  description of the transform geometry and a listing of the input coordinates,
  the fitted coordinates, and the fit residuals. The number of results files
  must be one or equal to the number of input files. If results is <span style="font-family: monospace;">"STDOUT"</span> the
  results summary is printed on the standard output.
  </dd>
  </dl>
  <dl id="l_xmin">
  <dt><b>xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmin' Line='xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF' -->
  <dd>The minimum and maximum logical x and logical y coordinates used to generate
  the grid of reference image control points and define the region of
  validity of the spatial transformation. Xmin, xmax, ymin, and
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
  are in degrees for all celestial coordinate
  systems. Obviously if the
  wcs is correct the ra and dec of an object
  should remain the same no matter how the image
  is linearly transformed. The default world coordinate
  system is either 1) the value of the environment variable <span style="font-family: monospace;">"defwcs"</span> if
  set in the user's IRAF environment (normally it is undefined) and present
  in the image header, 2) the value of the <span style="font-family: monospace;">"system"</span>
  attribute in the image header keyword WAT0_001 if present in the
  image header or, 3) the <span style="font-family: monospace;">"physical"</span> coordinate system.
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
  <dd>The format of the output reference image celestial coordinates
  in columns 5 and 6 respectively. The internal default formats will give
  reasonable output formats and precision for all celestial coordinate
  systems.
  </dd>
  </dl>
  <dl id="l_wxformat">
  <dt><b>wxformat = <span style="font-family: monospace;">""</span>, wyformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wxformat' Line='wxformat = "", wyformat = ""' -->
  <dd>The format of the output input image celestial coordinates
  in columns 7 and 8 respectively. The internal default formats will give
  reasonable output formats and precision for all celestial coordinate
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
  switches are set to <span style="font-family: monospace;">"none"</span> regardless of the values of the <i>xxorder</i>,
  <i>xyorder</i>, <i>xxterms</i>, <i>yxorder</i>, <i>yyorder</i> and <i>yxterms</i>
  parameters set by the user.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"polynomial"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "polynomial"' -->
  <dd>The type of analytic coordinate surfaces to be fit. The options are the
  following.
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
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about the progress of the task?
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
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
  SKYMAP computes the spatial transformation function required to map the
  celestial coordinate system of the reference image <i>reference</i> to
  the celestial coordinate
  system of the input image <i>input</i>, and stores the computed function in
  the output text database file <i>database</i>.
  The input and reference images may be 1D or 2D but
  must have the same dimensionality. The input image and output
  text database file can be input to the REGISTER or GEOTRAN tasks to
  perform the actual image registration.  SKYMAP assumes that the world
  coordinate systems in the input and reference
  image headers are accurate and that the two systems are compatible, e.g. both
  images have a celestial coordinate system WCS.
  </p>
  <p>
  SKYMAP computes the required spatial transformation by matching the logical
  x and y pixel coordinates of a grid of points 
  in the input image with the logical x and y pixels coordinates
  of the same grid of points in the reference image,
  using celestial coordinate information stored in the two image headers.
  The coordinate grid consists of <i>nx * ny</i> points evenly distributed
  over the logical pixel space of interest in the reference image defined by the
  <i>xmin</i>, <i>xmax</i>, <i>ymin</i>, <i>ymax</i> parameters.
  The logical x and y reference image pixel coordinates are transformed to
  reference image celestial coordinates using
  world coordinate information stored in the reference image header.
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
  world coordinates are written to temporary coordinates file which is
  deleted on task termination.
  The pixel and celestial coordinates are written using
  the <i>xformat</i> and <i>yformat</i> and the <i>rwxformat</i>, <i>rwyformat</i>,
  <i>wxformat</i> and <i>wxformat</i>
  parameters respectively. If these formats are undefined and, in the
  case of the celestial coordinates a format attribute cannot be
  read from either the reference or the input images, reasonable default
  formats are chosen.
  If the reference and input images are 1D then all the output logical and
  world y coordinates are set to 1.
  </p>
  <p>
  SKYMAP computes a spatial transformation of the following form.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xin = f (xref, yref)
  yin = g (xref, yref)
  </pre></div>
  <p>
  The functions f and g are either a power series polynomial or a Legendre or
  Chebyshev polynomial surface of order <i>xxorder</i> and <i>xyorder</i> in x
  and <i>yxorder</i> and <i>yyorder</i> in y.
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
  If the <b>fitgeometry</b> parameter is anything other than <span style="font-family: monospace;">"general"</span>, the
  order parameters assume the value 2 and the cross terms switches assume
  the value <span style="font-family: monospace;">"none"</span>, regardless of the values set by the user.  The computation
  can be done in either real or double precision by setting the <i>calctype</i>
  parameter. Automatic pixel rejection may be enabled by setting the <i>reject</i>
  parameter to a positive number other than INDEF.
  </p>
  <p>
  The transformation computed by the <span style="font-family: monospace;">"general"</span> fitting geometry is arbitrary
  and does not necessarily correspond to a physically meaningful model.
  However the computed
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
  validity of the fit as well as the limits of the grid
  in the reference coordinate system.  These parameters are also used to
  reject out of range data before the actual fitting is done.
  </p>
  <p>
  Each computed transformation is written to the output file <i>database</i>
  in a record whose name is supplied by the user via the <i>transforms</i>
  parameter or set to the name of the corresponding input image. 
  The database file is opened in append mode and new records are written
  to the end of the existing file. If more that one record of the same
  name is written to the database file, the last record written is the
  valid record, i.e. the one that will be used by the REGISTER or
  GEOTRAN tasks.
  </p>
  <p>
  SKYMAP will terminate with an error if the reference and input images
  are not both either 1D or 2D.
  If the celestial coordinate system information cannot be read from either
  the reference or input image header, the requested transformations
  from the celestial &lt;-&gt; logical coordinate systems cannot be compiled for either
  or both images, or the celestial coordinate systems of the reference and input
  images are fundamentally incompatible in some way, the output logical
  reference and input image coordinates are both set to a grid of points
  spanning the logical pixel space of the input, not the reference image.
  This grid of points defines an identity transformation which will leave
  the input image unchanged if applied by the REGISTER or GEOTRAN tasks.
  </p>
  <p>
  If <i>verbose</i> is <span style="font-family: monospace;">"yes"</span> then messages about the progress of the task
  as well as warning messages indicating potential problems are written to
  the standard output. If <i>results</i> is set to a file name then the input
  coordinates, the fitted coordinates, and the residuals of the fit are
  written to that file.
  </p>
  <p>
  SKYMAP may be run interactively by setting the <i>interactive</i>
  parameter to <span style="font-family: monospace;">"yes"</span>.
  In interactive mode the user has the option of viewing the fit, changing the
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
  :xxterms :yxterms [n/h/f]       X, Y fit cross terms type
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
  1. Compute the spatial transformation required to match a radio image to an
  X-ray image of the same field using a 100 point coordinate  grid
  and a simple linear transformation.  Both images have accurate sky
  equatorial world coordinate systems define at different equinoxes.
  Print the output world coordinates
  in the coords file in hh:mm:ss.ss and dd:mm:ss.s format. Run geotran
  on the results to do the actual registration.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skymap radio xray geodb rwxformat=%12.2H rwyformat=%12.1h \
      wxformat=%12.2H wyformat=%12.1h interactive-
  
  cl&gt; geotran radio radio.tran geodb radio
  </pre></div>
  <p>
  2. Repeat the previous command but begin with a higher order fit
  and run the task in interactive mode in order to examine the fit
  residuals.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skymap radio xray geodb rwxformat=%12.2H rwyformat=%12.1h \
      wxformat=%12.2H wyformat=%12.1h xxo=4 xyo=4 xxt=half \
      yxo=4 yyo=4 yxt=half
  
      ... a plot of the fit appears
  
      ... type x and r to examine the residuals of the x
          surface fit versus x and y
  
      ... type y and s to examine the residuals of the y
          surface fit versus x and y
  
      ... delete 2 deviant points with the d key and
          recompute the fit with the f key
  
      ... type q to quit and save the fit
  
  cl&gt; geotran radio radio.tran geodb radio
  </pre></div>
  <p>
  3. Repeat example 1 but set the transform name specifically.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skymap radio xray geodb trans=m82 rwxformat=%12.2H \
      rwyformat=%12.1h wxformat=%12.2H wyformat=%12.1h \
      interactive-
  
  cl&gt; geotran radio radio.tran geodb m82
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
  wcsctran,register,geotran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'FORMATS' 'REFERENCES' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

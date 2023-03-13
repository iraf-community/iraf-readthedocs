.. _geomap:

geomap: Compute geometric transforms using matched coordinate lists
===================================================================

**Package: immatch**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  geomap input database xmin xmax ymin ymax
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of text files containing the pixel coordinates of control points in
  the reference and input images. The control points are listed
  one per line with xref, yref, xin, and yin in columns 1 through 4 respectively.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>The name of the text file database where the computed transformations will
  be stored.
  </dd>
  </dl>
  <dl id="l_xmin">
  <dt><b>xmin, xmax, ymin, ymax</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmin' Line='xmin, xmax, ymin, ymax' -->
  <dd>The range of reference coordinates over which the computed coordinate
  transformation is valid. If the user is working in pixel units  these limits
  should normally be set to the values of the column and row limits of the
  reference image, e.g xmin = 1.0, xmax = 512, ymin= 1.0, ymax = 512 for
  a 512 x 512 image. The minimum and maximum xref and yref values in <i>input</i>
  are used if xmin, xmax, ymin, or ymax are undefined.
  </dd>
  </dl>
  <dl id="l_transforms">
  <dt><b>transforms = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='transforms' Line='transforms = ""' -->
  <dd>An optional list of transform record names. If transforms is undefined 
  the database record(s) are assigned the names of the
  individual text files specified by <i>input</i>.
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
  distortion term is set to zero.
  </dd>
  </dl>
  For all the fitting geometries except <span style="font-family: monospace;">"general"</span> no distortion term is fit,
  i.e. the x and y polynomial orders are assumed to be 2 and the cross term
  switches are assumed to be <span style="font-family: monospace;">"none"</span>, regardless of the values of the
  <i>xxorder</i>, <i>xyorder</i>, <i>xxterms</i>, <i>yxorder</i>, <i>yyorder</i> and
  <i>yxterms</i> parameters set by the user.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"polynomial"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "polynomial"' -->
  <dd>The type of analytic surface to be fit. The options are the following.
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
  <dd>Power series in x and y.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_xxorder">
  <dt><b>xxorder = 2, xyorder = 2,  yxorder = 2, yyorder = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xxorder' Line='xxorder = 2, xyorder = 2,  yxorder = 2, yyorder = 2' -->
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
  maximum combined power is max (xxorder - 1, xyorder - 1) for the x fit and
  max (yxorder - 1, yyorder - 1) for the y fit. 
  </dd>
  </dl>
  <dl>
  <dt><b>full</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='full' Line='full' -->
  <dd>The individual polynomial terms contain powers of x and powers of y, whose
  maximum combined power is max (xxorder - 1, xyorder - 1) for the x fit and
  max (yxorder - 1, yyorder - 1) for the y fit.
  </dd>
  </dl>
  The <span style="font-family: monospace;">"shift"</span>, <span style="font-family: monospace;">"xyscale"</span>, <span style="font-family: monospace;">"rotation"</span>, <span style="font-family: monospace;">"rscale"</span>, and <span style="font-family: monospace;">"rxyscale"</span> fitting
  geometries, assume that the cross term switches are set to <span style="font-family: monospace;">"none"</span>
  regardless of the values set by the user.  If either of the cross terms
  parameters are set to <span style="font-family: monospace;">"half"</span> or <span style="font-family: monospace;">"full"</span> and <i>fitgeometry</i> is <span style="font-family: monospace;">"general"</span>
  then a distortion surface is fit to the residuals from the linear
  portion of the fit.
  </dd>
  </dl>
  <dl id="l_maxiter">
  <dt><b>maxiter = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxiter' Line='maxiter = 0' -->
  <dd>The maximum number of rejection iterations. The default is no rejection.
  </dd>
  </dl>
  <dl id="l_reject">
  <dt><b>reject = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reject' Line='reject = 3.0' -->
  <dd>The rejection limit in units of sigma.
  </dd>
  </dl>
  <dl id="l_calctype">
  <dt><b>calctype = <span style="font-family: monospace;">"real"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='calctype' Line='calctype = "real"' -->
  <dd>The precision of the coordinate transformation calculations. The options are
  real and double.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about actions taken by the task ?
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>In interactive mode the user may interact with the fitting process, e.g.
  change the order of the fit, reject points, display the data, etc.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>The graphics device.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>The graphics cursor.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  GEOMAP computes the transformation required to map the reference coordinate
  system to the input coordinate system.  The coordinates of points in common
  to the two systems are listed in the input text file(s) <i>input</i>
  one per line in the following format: <span style="font-family: monospace;">"xref yref xin yin"</span>.
  </p>
  <p>
  The computed transforms are stored in the text database file <i>database</i>
  in records with names specified by the parameter <i>transforms</i>. If the
  transforms parameter is undefined the records are assigned the name of
  the input coordinate files.
  </p>
  <p>
  The computed transformation has the form shown below, where the reference
  coordinates must be defined in the coordinate system of the reference image
  system if the user intends to resample an image with gregister or geotran, or
  transform coordinates from the reference coordinate system to the input
  image coordinate system. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  xin = f (xref, yref)
  yin = g (xref, yref)
  </pre></div>
  <p>
  If on the other hand the user wishes to transform coordinates from the
  input image coordinate system to the reference coordinate system then he or she
  must reverse the roles of the reference and input coordinates as defined above,
  and compute the inverse transformation.
  </p>
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
  If the <b>fitgeometry</b> parameter is anything other than <span style="font-family: monospace;">"general"</span>, the  order
  parameters assume the value 2 and the cross terms switches assume the value
  <span style="font-family: monospace;">"none"</span>, regardless of the values set by the user. The computation can be done in
  either real or double precision by setting <i>calctype</i>. Automatic pixel
  rejection may be enabled by setting axiter &gt; 0 and <i>reject</i> to some
  number greater than 0.
  </p>
  <p>
  <i>Xmin</i>, <i>xmax</i>, <i>ymin</i> and <i>ymax</i> define the region of
  validity of the fit in the reference coordinate system and must be set by
  the user. These parameters can be used to reject out of range data before the
  actual fitting is done.
  </p>
  <p>
  GEOMAP may be run interactively by setting <i>interactive</i> = yes and
  inputting commands by the use of simple keystrokes.
  In interactive mode the user has the option of changing the
  fit parameters and displaying the data graphically until a satisfactory
  fit has been achieved. The available keystroke commands are listed
  below.
  </p>
  <div class="highlight-default-notranslate"><pre>
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
  :show                           List parameters
  :fitgeometry                    Fitting geometry (shift,xyscale,rotate,
                                  rscale,rxyscale,general)
  :function [value]               Fitting function (chebyshev,legendre,
                                  polynomial)
  :xxorder :xyorder [value]       X fitting function xorder, yorder
  :yxorder :yyorder [value]       Y fitting function xorder, yorder
  :xxterms :yxterms [n/h/f]       X, Y fit cross terms type
  :maxiter [value]                Maximum number of rejection iterations
  :reject [value]                 Rejection threshold
  </pre></div>
  <p>
  The final fit is stored in a simple text file in a format suitable for use
  by the GREGISTER or GEOTRAN tasks.
  </p>
  <p>
  If <i>verbose</i>  is <span style="font-family: monospace;">"yes"</span>, various pieces of useful information are printed
  to the terminal as the task proceeds. If <i>results</i> is set to a file name
  then the input coordinates, the fitted coordinates, and the residuals of
  the fit are written to that file.
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
  and skew are the rotation of the x and y axes and their deviation from
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
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the linear transformation between coordinate systems.
     A record called <span style="font-family: monospace;">"m51.coo"</span> will be written in the database
     file <span style="font-family: monospace;">"database"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geomap m51.coo database 1. 512. 1. 512.
  </pre></div>
  <p>
  2. Compute the 3rd order transformation in x and y between two
     coordinate systems.  A record called <span style="font-family: monospace;">"m51.coo"</span> will be written in
     the database file <span style="font-family: monospace;">"database"</span>. This record supersedes the one
     of the same name written in example 1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geomap m51.coo database 1. 512. 1. 512. xxo=4 xyo=4 \
  &gt;&gt;&gt; yxo=4 yyo=4 xxt=full yxt=full inter-
  </pre></div>
  <p>
  3. Register a 500 by 500 image of m51 to an 800 by 800 image of the same
  field taken with a different instrument, and display the original
  800 by 800 image and the transformed image. Use the default fitting parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geomap m51.coo database 1.0 800.0 1.0 800.0
  cl&gt; gregister m51.500 m51.500.out database m51.coo
  cl&gt; display m51.800 1 fi+
  cl&gt; display m51.500.out 2 fi+
  </pre></div>
  <p>
  4. Use the above transform to transform a list of object pixel coordinates
  in the m51.800 image to their pixel coordinates in the m51.500 system.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geoxytran m51.800.xy m51.500.xy database m51.coo
  </pre></div>
  <p>
  5. Transform object pixel coordinates in the m51.500 image to their
  pixel coordinates in the m51.800 image. Note that to do this the roles
  of the reference and input coordinates defined in example 3 must be
  reversed and the inverse transform must be computed.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fields m51.coo 3,4,1,2 &gt; m51.coo.inv
  cl&gt; geomap m51.coo.inv database 1.0 512.0 1.0 512.0
  cl&gt; geoxytran m51.512.xy m51.800.xy database m51.coo.inv
  </pre></div>
  <p>
  6. Compute 3 different transforms, store them in the same database file,
  and use them to transform 3 different images.  Use the original image names as
  the database record names.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geomap coo1,coo2,coo3 database 1. 512. 1. 512. \
  &gt;&gt;&gt; transforms=im1,im2,im3
  cl&gt; gregister im1,im2,im3  im1.out,im2.out,im3.out database \
  &gt;&gt;&gt; im1,im2,im3
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The user should be aware that for high order fits the <span style="font-family: monospace;">"polynomial"</span> basis
  functions become very unstable. Switching to the <span style="font-family: monospace;">"legendre"</span> or <span style="font-family: monospace;">"chebyshev"</span>
  polynomials and/or going to double precision will usually cure the problem.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imshift, magnify, rotate, imlintran, gregister, geotran, geoxytran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

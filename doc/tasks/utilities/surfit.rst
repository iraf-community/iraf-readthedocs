.. _surfit:

surfit: Fit a surface, z=f(x,y), to a set of x, y, z points
===========================================================

**Package: utilities**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  surfit input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input text file containing the data to be fit.  The file consists of lines
  with three or four whitespace separated values giving x, y, z, and
  optionally a weight.
  </dd>
  </dl>
  <dl id="l_image">
  <dt><b>image = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image = ""' -->
  <dd>Optional image name in which to create an evenly sampled image of the
  fitted surface.  If no name is specified a image is not created.  If an
  image name is specified then the x range in the input is evenly divided by
  the specified number of image columns, the y range is evenly divided by the
  specified number of lines, and the fitted surface values evaluated at the
  sampled x and y points are written as the pixel values of the image.  A
  linear world coordinate system based on the x and y values is also created
  for the image.
  </dd>
  </dl>
  <dl id="l_coordinates">
  <dt><b>coordinates = <span style="font-family: monospace;">""</span>, fit = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coordinates' Line='coordinates = "", fit = ""' -->
  <dd>The first two columns of the text file specified by the coordinates parameter
  are use to supply x and y values which are evaluated by the surface and
  the resulting x, y, and z values are appended to the specified fit file.
  If either parameter is not specified then this surface evaluation is
  not done.  Note that the input data points are evaluated as part of
  the standard output but one may, if desired, specify the input file
  as the coordinate file to create a separate output.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"polynomial"</span> (chebyshev|legendre|polynomial)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "polynomial" (chebyshev|legendre|polynomial)' -->
  <dd>Surface function type to fit.  The choices are a chebyshev, legendre,
  or simple power series bi-dimensional polynomial.
  </dd>
  </dl>
  <dl id="l_xorder">
  <dt><b>xorder = 2, yorder = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xorder' Line='xorder = 2, yorder = 2' -->
  <dd>The polynomial orders in x and y.
  </dd>
  </dl>
  <dl id="l_xterms">
  <dt><b>xterms = <span style="font-family: monospace;">"full"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xterms' Line='xterms = "full"' -->
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
  maximum combined power is max (xorder - 1, yorder - 1).
  </dd>
  </dl>
  <dl>
  <dt><b>full</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='full' Line='full' -->
  <dd>The individual polynomial terms contain powers of x and powers of y, whose
  maximum combined power is max (xorder - 1 + yorder - 1).
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_weighting">
  <dt><b>weighting = <span style="font-family: monospace;">"user"</span> (uniform|user|statistical|instrumental)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='weighting' Line='weighting = "user" (uniform|user|statistical|instrumental)' -->
  <dd>The type of weighting for the fit. The options are:
  <dl>
  <dt><b>uniform</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='uniform' Line='uniform' -->
  <dd>All weights are 1.  Any input weights are ignored.
  </dd>
  </dl>
  <dl>
  <dt><b>user</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='user' Line='user' -->
  <dd>The weights in the fourth input column are used.  If no weight is given
  a weight of 1 is supplied.
  </dd>
  </dl>
  <dl>
  <dt><b>statistical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='statistical' Line='statistical' -->
  <dd>The reciprocal of the absolute value of z input data is used as the weight.
  Any input weights are ignored.  Z values less than 1e-20 are set to 1e-20.
  </dd>
  </dl>
  <dl>
  <dt><b>instrumental</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='instrumental' Line='instrumental' -->
  <dd>The fourth input column is taken as a sigma and the weight is the
  reciprocal of the sigma squared.  If no sigma is given a sigma of
  1 is supplied.  Sigma values less than 1e-10 are set to 1e-10.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_xmin">
  <dt><b>xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmin' Line='xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF' -->
  <dd>These parameters define the range of input x and y data to be used and
  also define the range over which the surface function is defined.  If
  INDEF then the appropriate limit from the input data points is used.
  If input data points lie outside these limits they are discarded.  The
  range may be given larger than the range of the input data in order
  to all evaluating coordinates outside input data; i.e. to
  allow extrapolation.
  </dd>
  </dl>
  <dl id="l_zmin">
  <dt><b>zmin = INDEF, zmax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zmin' Line='zmin = INDEF, zmax = INDEF' -->
  <dd>These parameters apply threshold limits to the input data.  If INDEF
  the appropriate limit from the input data points is used.  Input
  data points with z values outside this range are discarded.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = 100, nlines = 100</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = 100, nlines = 100' -->
  <dd>The number of columns and lines for the optional surface image.  These
  parameters determine the size of the image and how finely the x and
  y input data range is subdivided.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task fits a surface, a function of two coordinates, to a set of
  possibly irregularly sampled data points specified in a text file.
  The input consists of a file with three or four columns.  The first
  two columns define the two coordinates, called x and y, the third
  column gives the value the function is supposed to fit, called z,
  and the optional fourth column is a weight or sigma.  If a weight or
  sigma is not specified it will have a unit weight or sigma.  The type
  of weighting is selected by a task parameter.
  </p>
  <p>
  The input data points may be restricted by use of the <i>xmin, xmax,
  ymin, ymax, zmin, zmax</i> parameters.  If these parameters are INDEF
  (the default) the full range of the input is used.  The surface function
  is only defined within the specified x and y range.  In order to
  extrapolate outside the range of the input data these limits must
  be specified explicitly.
  </p>
  <p>
  The functions which may be fit are legendre, chebyshev, or simple
  power series bi-dimensional polynomials.  The user selects the
  function type, the order in x and y, and whether to include
  cross terms.  The orders are the number of coefficients which
  is the highest polynomial power plus 1.  For example the default
  values of 2 in each coordinate define a linear sloped plane.
  All computations are done in double precision.
  </p>
  <p>
  Several polynomial cross terms options are available. Options <span style="font-family: monospace;">"none"</span>,
  <span style="font-family: monospace;">"half"</span>, and <span style="font-family: monospace;">"full"</span> are illustrated below for a quadratic polynomial in
  x and y.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xterms = "none"
  xorder = 3, yorder = 3
  
     z = a11 + a21 * x + a12 * y + a31 * x ** 2 + a13 * y ** 2
  
  xterms = "half"
  xorder = 3, yorder = 3
  
     z = a11 + a21 * x + a12 * y + a31 * x ** 2 + a22 * x * y + a13 * y ** 2
  
  xterms = "full"
  xorder = 3, yorder = 3
  
     z = a11 + a21 * x + a31 * x ** 2 +
           a12 * y + a22 * x * y +  a32 * x ** 2 * y +
           a13 * y ** 2 + a23 * x *  y ** 2 +
           a33 * x ** 2 * y ** 2
  </pre></div>
  <p>
  The fit results are written to the standard output; the terminal unless
  redirected.  It consists of the input parameters, the coefficients and
  errors, and the input data plus the fitted values and residuals.  The
  coefficient lines contain four columns.  The first two columns are the x
  and y polynomial powers and then the coefficient and error in the
  coefficient are given.  The coefficients are determined based on a
  normalized coordinate; the range of input x and y values, which is shown in
  the output as xmin, xmax, ymin, and ymax, is mapped to the range -1 to 1.
  The data portion gives the x, y, and z input values followed by the fitted
  value and the residual (z - fit) and finally the weight.
  </p>
  <p>
  There are two types of additional output which may be selected if desired.
  One is a two dimensional image of the surface evenly sampled over the x and
  y data range set by the xmin, xmax, ymin, ymax parameters.  This type of
  output is selected by specifying an image name and the number of columns
  and lines.  The number of columns and lines defines the size of the image
  and also the sampling of the x and y values.  The first pixel in each
  dimension is the minimum x or y value and the sample interval per pixel is
  given by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  dx = (xmax - xmin) / (ncols - 1)
  dy = (ymax - ymin) / (nlines - 1)
  </pre></div>
  <p>
  The fitted surface is evaluated at each pixel and written to the image.
  The linear world coordinate system defining the x and y pixel sampling is
  written to the image header.  This allows tasks such as <b>implot</b> and
  <b>listpixels</b> to show the fitted values in the input x and y units.
  </p>
  <p>
  The second type of output allows the surface to be evaluated at an
  arbitrary set of x and y coordinates.  The coordinates are input
  as a text file.  The first two columns are taken as the x and y values
  and any other columns are ignored.  The x and y values and the fitted
  values are appended to a specified text file.  This output is
  optional and only occurs if both an input coordinate and output
  fit file are specified.  Note that the input data points are
  always evaluated as part of the standard output but the input
  data file may also be used as a coordinate file if desired.
  Also the output data file may be specified as <span style="font-family: monospace;">"STDOUT"</span> to merge
  this output with the basic results output.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  The following example shows use of all the output options using some
  random numbers.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; urand 50 3 scale=100. &gt;sf1
  cl&gt; head sf1 nl=5
   70.87   42.5  99.06
   51.49  42.19  64.86
   70.75  83.34  80.39
    57.1  67.79  30.24
   60.91  49.76  53.32
  
  cl&gt; urand 5 2 scale=100. seed=2 &gt;sf2
  cl&gt; head sf2
   20.62  17.86
   66.39  86.26
   48.08  35.07
   70.39   95.8
   53.64  15.51
  
  cl&gt; surfit sf1 image=sf coord=sf2 fit=sf3 ncols=20 nlines=20
  Surface parameters:
    function = polynomial
    xorder = 2
    yorder = 2
    xterms = full
    weighting = user
    xmin =    0.684
    xmax =    89.74
    ymin =    1.051
    ymax =    95.36
    zmin =    1.217
    zmax =    99.14
  
  Surface coefficients:
     x  y    coeff    error
     0  0  75.7125  17.2504
     1  0 -0.37273 0.356014
     0  1 -0.77194 0.336627
     1  1 0.009884 0.006295
  
  Fitted points:
           x        y        z      fit residual   weight
       70.87     42.5    99.06  46.2611  52.7989       1.
       51.49    42.19    64.86  45.4249  19.4351       1.
       70.75    83.34    80.39  43.2899  37.1001       1.
        57.1    67.79    30.24  40.3604 -10.1204       1.
       60.91    49.76    53.32  44.5562  8.76384       1.
       ...
  
    chisqr = 903.797
  
  cl&gt; head sf3
   20.62    17.86  57.8802
   66.39    86.26  40.9855
   48.08    35.07  47.3864
   53.64    15.51  51.9697
  
  cl&gt; listpix sf[*:10,*:10] wcs=world formats="%5.2f %5.2f"
   0.68  1.05  74.65366
  47.56  1.05  57.66973
   0.68 50.69  36.67273
  47.56 50.69  42.6855
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  apphot.fitsky, apphot.txdump, imsurfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

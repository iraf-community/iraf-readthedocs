.. _imsurfit:

imsurfit: Fit a surface to a 2-D image
======================================

**Package: imfit**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  imsurfit input, output, xorder, yorder
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of images to be fit.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output image(s) of <i>type_output</i>.
  </dd>
  </dl>
  <dl id="l_xorder">
  <dt><b>xorder</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xorder' Line='xorder' -->
  <dd>The order in x of the polynomials (1 = constant) or the number of polynomial
  pieces for the bicubic spline.
  </dd>
  </dl>
  <dl id="l_yorder">
  <dt><b>yorder</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='yorder' Line='yorder' -->
  <dd>The order in y of the polynomials (1 = constant) or the number of polynomial
  pieces for the bicubic spline.
  </dd>
  </dl>
  <dl id="l_cross_terms">
  <dt><b>cross_terms = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cross_terms' Line='cross_terms = yes' -->
  <dd>Cross terms for the polynomials. For example, if <i>xorder</i> = 2 and
  <i>yorder</i> = 2
  then a function of the form z = a + b * x + c * y + d * x * y will be fit.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"leg"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "leg"' -->
  <dd>Functional for of surface to be fit to the image. The available functions
  (with minimum match abbreviation) are:
  <dl>
  <dt><b>legendre</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='legendre' Line='legendre' -->
  <dd></dd>
  </dl>
  <dl>
  <dt><b>chebyshev</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='chebyshev' Line='chebyshev' -->
  <dd></dd>
  </dl>
  <dl>
  <dt><b>spline3</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='spline3' Line='spline3' -->
  <dd></dd>
  </dl>
  <dl>
  <dt><b>spline1</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='spline1' Line='spline1' -->
  <dd></dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_type_output">
  <dt><b>type_output = <span style="font-family: monospace;">"fit"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='type_output' Line='type_output = "fit"' -->
  <dd>The type of output image.  The allowed types (with minimum match abbreviation)
  are:
  <dl>
  <dt><b>clean</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='clean' Line='clean' -->
  <dd>The input image with deviant pixels in the good regions replaced by the
  fitted value.
  </dd>
  </dl>
  <dl>
  <dt><b>fit  </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='fit' Line='fit  ' -->
  <dd>An image created from the surface fits to the image.
  </dd>
  </dl>
  <dl>
  <dt><b>residual</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='residual' Line='residual' -->
  <dd>The difference of the input image and the fitted image.
  </dd>
  </dl>
  <dl>
  <dt><b>response</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='response' Line='response' -->
  <dd>The ratio of the input image to the fitted image.
  All fitted (denominator) pixels below <i>div_min</i> are given a value of 1.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_xmedian">
  <dt><b>xmedian = 1, ymedian = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmedian' Line='xmedian = 1, ymedian = 1' -->
  <dd>The x and y dimensions of the box used for median processing.
  If <i>xmedian</i> &gt; 1 or <i>ymedian</i> is &gt; 1,
  then the median is calculated for each box and used in the surface
  fit instead of the individual pixels.
  </dd>
  </dl>
  <dl id="l_median_percent">
  <dt><b>median_percent = 50.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='median_percent' Line='median_percent = 50.' -->
  <dd>If the number of pixels in the median box is less than <i>median_percent</i> *
  <i>xmedian</i> * <i>ymedian</i> the box will be omitted from the fit.
  </dd>
  </dl>
  <dl id="l_upper">
  <dt><b>upper = 0., lower = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='upper' Line='upper = 0., lower = 0.' -->
  <dd>The number of sigma  limits for pixel rejection. If <i>upper</i> &gt; 0. or
  <i>lower</i> &gt; 0. and median processing is turned off,
  pixel rejection is enabled.
  </dd>
  </dl>
  <dl id="l_ngrow">
  <dt><b>ngrow = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ngrow' Line='ngrow = 0' -->
  <dd>The radius in pixels for region growing.
  Pixels within a distance of <i>ngrow</i> pixels of
  a rejected pixel are also rejected.
  </dd>
  </dl>
  <dl id="l_niter">
  <dt><b>niter = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niter' Line='niter = 0' -->
  <dd>The maximum number of iterations in the rejection cycle.
  Rejection will be terminated if the number of rejected pixels is zero
  or the number of iterations equals <i>niter</i>.
  </dd>
  </dl>
  <dl id="l_regions">
  <dt><b>regions = <span style="font-family: monospace;">"all"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='regions' Line='regions = "all"' -->
  <dd>The available options (with minimum match abbreviation) are:
  <dl>
  <dt><b>all</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='all' Line='all' -->
  <dd>All points in the image are fit.
  </dd>
  </dl>
  <dl>
  <dt><b>rows</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='rows' Line='rows' -->
  <dd>The fit is performed on the image rows specified by <i>rows</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>columns</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='columns' Line='columns' -->
  <dd>The fit is performed on the image columns specified by <i>columns</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>border</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='border' Line='border' -->
  <dd>The fit is performed on a border around the image whose width is specified
  by <i>border</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>sections</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='sections' Line='sections' -->
  <dd>The fit is performed on image sections listed in the file specified
  by <i>sections</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>circle</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='circle' Line='circle' -->
  <dd>The fit is performed on a circular region whose parameters are specified by
  <i>circle</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>invcircle</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='invcircle' Line='invcircle' -->
  <dd>The fit is performed on a region exterior to the circular region whose
  parameters are specified by <i>circle</i>.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_rows">
  <dt><b>rows = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rows' Line='rows = "*"' -->
  <dd>When <i>region_type</i> = 'rows', the string parameter <i>rows</i> specifies
  the rows to be fit.
  </dd>
  </dl>
  <dl id="l_columns">
  <dt><b>columns = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='columns' Line='columns = "*"' -->
  <dd>When <i>region_type</i> = 'columns', the string parameter <i>columns</i>
  specifies the columns to be fit.
  </dd>
  </dl>
  <dl id="l_border">
  <dt><b>border = <span style="font-family: monospace;">"50"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='border' Line='border = "50"' -->
  <dd>When <i>region_type</i> = 'border', the
  string parameter <i>border</i> specifies the width of the border to be fit.
  </dd>
  </dl>
  <dl id="l_sections">
  <dt><b>sections = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sections' Line='sections = ""' -->
  <dd>When <i>region_type</i> = 'sections', the
  string parameter <i>sections</i> is the name of the  file containing the list of
  image sections to be fit, where <i>Sections</i> may be the standard
  input (STDIN).
  The sections must be listed one per line in the following form: x1 x2 y1 y2.
  </dd>
  </dl>
  <dl id="l_circle">
  <dt><b>circle = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='circle' Line='circle = ""' -->
  <dd>The string parameter <i>circle</i> lists the parameter needed to specify
  the circle in the following format: xcenter ycenter radius. The three
  parameters must be integers.
  </dd>
  </dl>
  <dl id="l_div_min">
  <dt><b>div_min = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='div_min' Line='div_min = INDEF' -->
  <dd>When <i>type_output</i> = 'response' all divisions in which the fitted value
  is below <i>div_min</i> are set to the value 1.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A surface is fit to selected portions of the input image.
  The user may elect to fit the whole image, <i>region_type</i> = 'all',
  selected rows, <i>region_type</i> = 'rows', selected columns,
  <i>region_type</i> = 'columns', a
  border around the image, <i>region_type</i> = 'border' or image sections, 
  <i>region_type</i> = 'sections'. If the sections  option is enabled the user
  must supply the name of the file containing a list of sections,
  <i>sections</i> = 'list', or enter them from the standard input. In either case
  the sections must be listed one per line in the following form: x1 x2 y1 y2.
  </p>
  <p>
  The parameter <i>surface_type</i> may be a
  <span style="font-family: monospace;">"legendre"</span> polynomial, <span style="font-family: monospace;">"chebyshev"</span> polynomial,
  a cubic spline (<span style="font-family: monospace;">"spline3"</span>) or a linear spline (<span style="font-family: monospace;">"spline1"</span>).
  The order of the polynomials is selected in both x and y.
  Cross terms for the polynomial surfaces are optional.
  For the cubic spline the parameters <i>xorder</i> and <i>yorder</i> specify
  the number of polynomial pieces to be fit to the surface in
  each direction.
  </p>
  <p>
  The output image may be the fitted image, the difference between the
  input and the fitted image, the ratio of the input to the fitted image
  or the input image with deviant pixels in the fitted regions replaced
  with the fitted values, according to whether <i>type_output</i> =
  'fit', 'residual',
  'response' or 'clean'. If <i>type_output</i> = 'response' then pixels in the
  fitted image with values &lt; <i>div_min</i> are replaced by 1.
  If <i>type_output</i> =
  'clean' then at least one of <i>upper</i> or <i>lower</i> must be &gt; 0.
  </p>
  <p>
  Pixel rejection is enabled if median processing is turned off,
  <i>niter</i> &gt; 0,
  and at least one of the parameters <i>upper</i> and <i>lower</i> is &gt; 0.
  Region growing
  can be turned on by setting <i>ngrow</i> &gt; 0, in which case all pixels within
  a radius ngrow of a deviant pixel will be rejected.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To create a smoothed version of an image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imsurfit m74 m74smooth 5 10 function=spline3
  </pre></div>
  <p>
  2. To create a smoothed version of an image using median processing:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imsurfit m74 m74med 5 10 function=spline3 \
  &gt;&gt;&gt; xmed=5 ymed=5
  </pre></div>
  <p>
  3. To subtract a constant background from an image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imsurfit abell30 abell30bck 1 1 function=leg \
  &gt;&gt;&gt; type=resid
  </pre></div>
  <p>
  4. To make a ratio image using signals above 1000 units:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imsurfit n7006 n7006ratio 20 20 function=spline3 \
  &gt;&gt;&gt; type=response div_min=1000
  </pre></div>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  <p>
  Fitting and subtracting a constant from a 512 by 512 IRAF image requires
  ~35 cpu seconds. Approximately 130 cpu seconds are required to fit a
  second degree polynomial in x and y (including cross-terms) to a
  100 pixel wide border around a 512 by
  512 IRAF image, and to subtract the fitted image from the input image.
  To produce a smooth 512 by 512 IRAF image using a 10 by 10 bicubic spline
  requires ~300 cpu seconds. Timings refer to a VAX 11/750 + fpa.
  </p>
  </section>
  <section id="s_notes">
  <h3>Notes</h3>
  <p>
  The surface fitting code uses the IRAF SURFIT math routines,
  which have been optimized for image fitting .
  The routines which fit selected portions
  of the image, perform pixel rejection and region growing, and create and
  maintain a list of rejected pixels utilize the ranges and pixlist packages
  of routines currently maintained in the images directory. These will be
  replaced by more general ranges and image masking routines in the future.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIMINGS' 'NOTES'  -->
  

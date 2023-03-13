.. _aptrace:

aptrace: Trace positions of spectra
===================================

**Package: echelle**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <div class="highlight-default-notranslate"><pre>
  aptrace images
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images to be traced.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>Apertures to recenter, resize, trace, and extract.  This only applies
  to apertures read from the input or reference database.  Any new
  apertures defined with the automatic finding algorithm or interactively
  are always selected.  The syntax is a list comma separated ranges
  where a range can be a single aperture number, a hyphen separated
  range of aperture numbers, or a range with a step specified by <span style="font-family: monospace;">"x&lt;step&gt;"</span>;
  for example, <span style="font-family: monospace;">"1,3-5,9-12x2"</span>.
  </dd>
  </dl>
  <dl id="l_references">
  <dt><b>references = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='references' Line='references = ""' -->
  <dd>List of reference images to be used to define apertures for the input
  images.  When a reference image is given it supersedes apertures
  previously defined for the input image. The list may be null, <span style="font-family: monospace;">""</span>, or
  any number of images less than or equal to the list of input images.
  There are three special words which may be used in place of an image
  name.  The word <span style="font-family: monospace;">"last"</span> refers to the last set of apertures written to
  the database.  The word <span style="font-family: monospace;">"OLD"</span> requires that an entry exist
  and the word <span style="font-family: monospace;">"NEW"</span> requires that the entry not exist for each input image.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Run this task interactively?  If the task is not run interactively then
  all user queries are suppressed and interactive aperture editing and trace
  fitting are disabled.
  </dd>
  </dl>
  <dl id="l_find">
  <dt><b>find = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='find' Line='find = yes' -->
  <dd>Find the spectra and define apertures automatically?  In order for
  spectra to be found automatically there must be no apertures for the
  input image or reference image defined in the database.
  </dd>
  </dl>
  <dl id="l_recenter">
  <dt><b>recenter = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='recenter' Line='recenter = no' -->
  <dd>Recenter the apertures?
  </dd>
  </dl>
  <dl id="l_resize">
  <dt><b>resize = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='resize' Line='resize = yes' -->
  <dd>Resize the apertures?
  </dd>
  </dl>
  <dl id="l_edit">
  <dt><b>edit = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='edit' Line='edit = yes' -->
  <dd>Edit the apertures?  The <i>interactive</i> parameter must also be yes.
  </dd>
  </dl>
  <dl id="l_trace">
  <dt><b>trace = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trace' Line='trace = yes' -->
  <dd>Trace the apertures?
  </dd>
  </dl>
  <dl id="l_fittrace">
  <dt><b>fittrace = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fittrace' Line='fittrace = yes' -->
  <dd>Interactively fit the traced positions by a function?  The <i>interactive</i>
  parameter must also be yes.
  </dd>
  </dl>
  <dl id="l_line">
  <dt><b>line = INDEF, nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='line' Line='line = INDEF, nsum = 1' -->
  <dd>The dispersion line (line or column perpendicular to the dispersion
  axis) and number of adjacent lines (half before and half after unless
  at the end of the image) used in finding, recentering, resizing,
  and editing operations.  For tracing this is the starting line and
  the same number of lines are summed at each tracing point.  A line of
  INDEF selects the middle of the image along the dispersion axis.
  A positive nsum selects the number of lines to sum while a negative
  value selects a median.  Tracing always uses a sum.
  </dd>
  </dl>
  <dl id="l_step">
  <dt><b>step = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='step' Line='step = 10' -->
  <dd>Step along the dispersion axis between determination of the spectrum
  positions.
  </dd>
  </dl>
  <dl id="l_nlost">
  <dt><b>nlost = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlost' Line='nlost = 3' -->
  <dd>Number of consecutive steps in which the profile is lost before quitting
  the tracing in one direction.  To force tracing to continue through
  regions of very low signal this parameter can be made large.  Note,
  however, that noise may drag the trace away before it recovers.
  </dd>
  </dl>
  <p>
  The following parameters are the defaults used to fit the traced positions
  by a function of the dispersion line.  These parameters are those used by
  the ICFIT package.
  </p>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"legendre"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "legendre"' -->
  <dd>Default trace fitting function.  The fitting function types are
  <span style="font-family: monospace;">"chebyshev"</span> polynomial, <span style="font-family: monospace;">"legendre"</span> polynomial, <span style="font-family: monospace;">"spline1"</span> linear spline, and
  <span style="font-family: monospace;">"spline3"</span> cubic spline.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 2' -->
  <dd>Default trace function order.  The order refers to the number of
  terms in the polynomial functions or the number of spline pieces in the spline
  functions.
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample' Line='sample = "*"' -->
  <dd>Default fitting sample.  The sample is given by a set of colon separated
  ranges each separated by either whitespace or commas.  The string <span style="font-family: monospace;">"*"</span> refers
  to all points.
  </dd>
  </dl>
  <dl id="l_naverage">
  <dt><b>naverage = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='naverage' Line='naverage = 1' -->
  <dd>Default number of points to average or median.  Positive numbers
  average that number of sequential points to form a fitting point.
  Negative numbers median that number, in absolute value, of sequential
  points.  A value of 1 does no averaging and each data point is used in the
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 0' -->
  <dd>Default number of rejection iterations.  If greater than zero the fit is
  used to detect deviant traced positions and reject them before repeating the
  fit.  The number of iterations of this process is given by this parameter.
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 3., high_reject = 3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_reject' Line='low_reject = 3., high_reject = 3.' -->
  <dd>Default lower and upper rejection sigma.  If greater than zero traced
  points deviating from the fit below and above the fit by more than this
  number of times the sigma of the residuals are rejected before refitting.
  </dd>
  </dl>
  <dl id="l_grow">
  <dt><b>grow = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grow' Line='grow = 0.' -->
  <dd>Default reject growing radius.  Traced points within a distance given by this
  parameter of any rejected point are also rejected.
  </dd>
  </dl>
  </section>
  <section id="s_additional_parameters">
  <h3>Additional parameters</h3>
  <p>
  I/O parameters and the default dispersion axis are taken from the
  package parameters, the default aperture parameters from
  <b>apdefault</b>, automatic aperture finding parameters from
  <b>apfind</b>, recentering parameters from <b>aprecenter</b>, resizing
  parameters from <b>apresize</b>, and parameters used for centering and
  editing the apertures from <b>apedit</b>.
  </p>
  <p>
  When this operation is performed from the task <b>apall</b> all parameters
  except the package parameters are included in that task.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  For each image in the input image list the position of the spectrum
  within each aperture are determined at a number of points along the
  dispersion axis and a smooth function is fit to these positions.  The
  fitted curve defines a shift to be added to the aperture center at each
  wavelength.  Other options allow defining apertures using a reference
  image, defining apertures through an automatic finding algorithm (see
  <b>apfind</b>), automatically recentering apertures (see
  <b>aprecenter</b>), automatically resizing apertures (see
  <b>apresize</b>), and interactively editing the apertures prior to
  tracing (see <b>apedit</b>).  Tracing is selected with the parameter
  <i>trace</i>.  If the tracing is done interactively (the
  <i>interactive</i> parameter set to yes) then the user is queried
  whether or not to trace each image.  The responses are <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"no"</span>,
  <span style="font-family: monospace;">"YES"</span>, or <span style="font-family: monospace;">"NO"</span>, where the upper case queries suppress this query
  for the following images.
  </p>
  <p>
  The tracing begins with the specified dispersion line.  A dispersion
  line is a line or column of the image perpendicular to the dispersion
  axis.  The dispersion axis is defined in the image header or by the
  package parameter <i>dispaxis</i>.  If the starting dispersion line is
  INDEF then the middle dispersion line of the image is used.  The
  positions of the spectra are determined using the <b>center1d</b>
  algorithm and the centering parameters from the <b>apedit</b> task.
  (See help under <b>center1d</b> for a description of the one dimensional
  position measuring algorithm.) The positions are redetermined at other
  points along the dispersion axis by stepping from the starting line in
  steps specified by the user.  A number of dispersion lines around each
  dispersion line to be measured may be summed to improve the position
  determinations, particularly for weak profiles.  This number usually is
  set equal to the tracing step.
  </p>
  <p>
  It is important to understand how to set the step size and the
  relationship between the step size and the centering error radius.
  Larger steps reduce the computational time, which is an important
  consideration.  However, if the step is too large then the tracing may
  fail to follow the systematic changes in the positions of the
  spectrum.  The centering error radius, <i>radius</i>, is used to limit
  the maximum position change between two successive steps.  If the
  positions of a spectrum changes by more than the specified amount or
  the data contrast falls below the <i>threshold</i> parameter then
  the position is marked as lost.
  </p>
  <p>
  The centering radius should be large enough to follow changes in the
  spectrum positions from point to point but small enough to detect an error
  in the tracing by a sudden abrupt change in position, such as caused by
  crowding with other spectra or by the disappearance of the spectrum.  The
  <i>nlost</i> parameter determines how many consecutive steps the position
  may fail to be found before tracing in that direction is stopped.  If this
  parameter is small the trace will stop quickly upon loss of the profile
  while if it is very large it will continue to try and recover the profile.
  </p>
  <p>
  The parameter <i>threshold</i> checks for the vanishing of a spectrum by
  requiring a minimum range in the data used for centering.  If the
  tracing fails when the spectra are strong and well defined the problem
  is usually that the step size is too large and/or the centering error
  radius is too small.
  </p>
  <p>
  The traced positions of a spectrum include some measurement variation
  from point to point.  Since the actual position of the spectrum in the
  image should be a smooth curve, a function of the dispersion line is fit
  to the measured points.  The fitted function is stored as part of the
  aperture description.  It is an offset to be added to the aperture's
  center as a function of the dispersion line.  Even if the fitting is not
  done interactively plots of the trace and the fit are recorded in the
  plot file or device specified by the parameter <i>plotfile</i>.
  </p>
  <p>
  Fitting the traced spectrum positions with a smooth function may be
  performed interactively when parameters <i>fittrace</i> and
  <i>interactive</i> are yes.  This allows changing the default fitting
  parameters.  The function fitting is done with the interactive curve
  fitting tools described under the help topic <b>icfit</b>.  There are
  two levels of queries when fitting the spectrum positions
  interactively; prompts for each image and prompts for each aperture in
  an image.  These prompts may be answered individually with the lower
  case responses <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"no"</span> or answered for all further prompts with
  the responses <span style="font-family: monospace;">"YES"</span> or <span style="font-family: monospace;">"NO"</span>.  Responding with <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"YES"</span> to the
  image prompt allows interactive fitting of the traced positions for the
  spectra.  Prompts are then given for each aperture in the image.  When
  an spectrum is not fit interactively the last set of fitting parameters
  are used (initially the default function and order given by the task
  parameters).  Note that answering <span style="font-family: monospace;">"YES"</span> or <span style="font-family: monospace;">"NO"</span> to a aperture prompt
  applies to all further aperture in the current image only.  Responding
  with <span style="font-family: monospace;">"no"</span> or <span style="font-family: monospace;">"NO"</span> to the image prompt fits the spectrum positions for
  all apertures in all images with the last set of fitting parameters.
  </p>
  <p>
  The tracing may also be done from the interactive aperture editor with
  the <span style="font-family: monospace;">'t'</span> key.  The aperture tracing algorithm may be selected from many
  of the tasks in the package with the <i>trace</i> parameter.
  </p>
  </section>
  <section id="s_aptrace_database_coefficients">
  <h3>Aptrace database coefficients</h3>
  <p>
  The path of an aperture is described by a function that gives an additive
  offset relative to the aperture center as stored under the database keyword
  center.  The function is saved in the database as a series of
  coefficients.  The section containing the coefficients starts with the
  keyword <span style="font-family: monospace;">"curve"</span> and the number of coefficients.
  </p>
  <p>
  The first four coefficients define the type of function, the order
  or number of spline pieces, and the range of the independent variable
  (the line or column coordinate along the dispersion).  The first
  coefficient is the function type code with values:
  </p>
  <div class="highlight-default-notranslate"><pre>
  Code    Type
     1    Chebyshev polynomial
     2    Legendre polynomial
     3    Cubic spline
     4    Linear spline
  </pre></div>
  <p>
  The second coefficient is the order (actually the number of terms) of
  the polynomial or the number of pieces in the spline.
  </p>
  <p>
  The next two coefficients are the range of the independent variable over
  which the function is defined.  These values are used to normalize the
  input variable to the range -1 to 1 in the polynomial functions.  If the
  independent variable is x and the normalized variable is n, then
  </p>
  <div class="highlight-default-notranslate"><pre>
  n = (2 * x - (xmax + xmin)) / (xmax - xmin)
  </pre></div>
  <p>
  where xmin and xmax are the two coefficients.
  </p>
  <p>
  The spline functions divide the range into the specified number of
  pieces.  A spline coordinate s and the nearest integer below s,
  denoted as j, are defined by
  </p>
  <div class="highlight-default-notranslate"><pre>
  s = (x - xmin) / (xmax - xmin) * npieces
  j = integer part of s
  </pre></div>
  <p>
  where npieces are the number of pieces.
  </p>
  <p>
  The remaining coefficients are those for the appropriate function.
  The number of coefficients is either the same as the function order
  for the polynomials, npieces+1 for the linear spline, or npieces + 3
  for the cubic spline.
  </p>
  <p>
  1. Chebyshev Polynomial
  </p>
  <p>
  The polynomial can be expressed as the sum
  </p>
  <div class="highlight-default-notranslate"><pre>
  y = sum from i=1 to order {c_i * z_i}
  </pre></div>
  <p>
  where the c_i are the coefficients and the z_i are defined
  interactively as:
  </p>
  <div class="highlight-default-notranslate"><pre>
  z_1 = 1
  z_2 = n
  z_i = 2 * n * z_{i-1} - z_{i-2}
  </pre></div>
  <p>
  2. Legendre Polynomial
  </p>
  <p>
  The polynomial can be expressed as the sum
  </p>
  <div class="highlight-default-notranslate"><pre>
  y = sum from i=1 to order {c_i * z_i}
  </pre></div>
  <p>
  where the c_i are the coefficients and the z_i are defined
  interactively as:
  </p>
  <div class="highlight-default-notranslate"><pre>
  z_1 = 1
  z_2 = n
  z_i = ((2*i-3) * n * z_{i-1} - (i-2) * z_{i-2}) / (i - 1)
  </pre></div>
  <p>
  3. Linear Spline
  </p>
  <p>
  The linear spline is evaluated as
  </p>
  <div class="highlight-default-notranslate"><pre>
  y = c_j * a + c_{j+1} * b
  </pre></div>
  <p>
  where j is as defined earlier and a and b are fractional difference
  between s and the nearest integers above and below
  </p>
  <div class="highlight-default-notranslate"><pre>
  a = (j + 1) - s
  b = s - j
  </pre></div>
  <p>
  4.  Cubic Spline
  </p>
  <p>
  The cubic spline is evaluated as
  </p>
  <div class="highlight-default-notranslate"><pre>
  y = sum from i=0 to 3 {c_{i+j} * z_i}
  </pre></div>
  <p>
  where j is as defined earlier.  The term z_i are computed from
  a and b, as defined earlier, as follows
  </p>
  <div class="highlight-default-notranslate"><pre>
  z_0 = a**3
  z_1 = 1 + 3 * a * (1 + a * b)
  z_2 = 1 + 3 * b * (1 + a * b)
  z_3 = b**3
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_APTRACE">
  <dt><b>APTRACE V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='APTRACE' Line='APTRACE V2.11' -->
  <dd>The <span style="font-family: monospace;">"apertures"</span> parameter can be used to select apertures for resizing,
  recentering, tracing, and extraction.  This parameter name was previously
  used for selecting apertures in the recentering algorithm.  The new
  parameter name for this is now <span style="font-family: monospace;">"aprecenter"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  apdefault, apfind, aprecenter, apresize, apedit, apall,
  center1d, icfit, gtools
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ADDITIONAL PARAMETERS' 'DESCRIPTION' 'APTRACE DATABASE COEFFICIENTS' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

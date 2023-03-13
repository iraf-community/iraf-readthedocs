.. _illumination:

illumination: Determine illumination calibration
================================================

**Package: specred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  illumination images illuminations
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>Images to use in determining illumination calibrations.  These are
  generally sky spectra.  An image section may be used to select only a
  portion of the image.
  </dd>
  </dl>
  <dl id="l_illuminations">
  <dt><b>illuminations</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='illuminations' Line='illuminations' -->
  <dd>Iillumination calibration images to be created.  Each illumination image is
  paired with a calibration image.  If the image exists then it will be modified
  otherwise it is created.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Graph the average spectrum and select the dispersion bins
  and graph and fit the slit profile for each dispersion bin interactively?
  </dd>
  </dl>
  <dl id="l_bins">
  <dt><b>bins = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bins' Line='bins = ""' -->
  <dd>Range string defining the dispersions bins within which the slit profiles
  are determined.  If the range string is null then the dispersion
  bins are determined by the parameter <i>nbins</i>.
  </dd>
  </dl>
  <dl id="l_nbins">
  <dt><b>nbins = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nbins' Line='nbins = 5' -->
  <dd>If the dispersion bins are not specified explicitly by the parameter
  <i>bins</i> then the dispersion range is divided into this number of
  nearly equal bins.
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample' Line='sample = "*"' -->
  <dd>Sample of points to use in fitting each slit profile.
  The sample is selected with a range string.
  </dd>
  </dl>
  <dl id="l_naverage">
  <dt><b>naverage = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='naverage' Line='naverage = 1' -->
  <dd>Number of sample points to average or median before fitting a function.
  If the number is positive the average of each set of naverage sample
  points is formed while if the number is negative then the median of each set
  of points (in absolute value) is formed.  This subsample of points is
  used in fitting the slit profile.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"spline3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "spline3"' -->
  <dd>Function to fit to each dispersion bin to form the illumination function.
  The options are <span style="font-family: monospace;">"spline1"</span>, <span style="font-family: monospace;">"spline3"</span>, <span style="font-family: monospace;">"legendre"</span>, and <span style="font-family: monospace;">"chebyshev"</span>.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 1' -->
  <dd>Order of the fitting function or the number of spline pieces.
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 0., high_reject = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_reject' Line='low_reject = 0., high_reject = 0.' -->
  <dd>Rejection limits below and above the fit in units of the residual sigma.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 1' -->
  <dd>Number of rejection iterations.
  </dd>
  </dl>
  <dl id="l_grow">
  <dt><b>grow = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grow' Line='grow = 0' -->
  <dd>Reject additional points within this distance of points exceeding the
  rejection threshold.
  </dd>
  </dl>
  <dl id="l_interpolator">
  <dt><b>interpolator = <span style="font-family: monospace;">"poly3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interpolator' Line='interpolator = "poly3"' -->
  <dd>Interpolation type.  One of <span style="font-family: monospace;">"nearest"</span>, <span style="font-family: monospace;">"linear"</span>, <span style="font-family: monospace;">"poly3"</span>, <span style="font-family: monospace;">"poly5"</span>, or
  <span style="font-family: monospace;">"spline3"</span>.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Graphics output device.  May be one of the standard devices <span style="font-family: monospace;">"stdgraph"</span>,
  <span style="font-family: monospace;">"stdplot"</span>, or <span style="font-family: monospace;">"stdvdm"</span> or an explicit device.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics input device.  May be either null for the standard graphics cursor
  or a file containing cursor commands.
  </dd>
  </dl>
  </section>
  <section id="s_cursor_keys">
  <h3>Cursor keys</h3>
  <p>
  The interactive curve fitting package <b>icfit</b> is used to fit a function
  to the average calibration spectrum.  Additional help on using this package
  and the cursor keys is available under the name <span style="font-family: monospace;">"icfit"</span>.
  </p>
  <p>
  When the dispersion bins are set graphically the following cursor keys are
  defined.
  </p>
  <dl>
  <dt><b>?</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line='?' -->
  <dd>Clear the screen and print a menu of the cursor options.
  </dd>
  </dl>
  <dl id="l_i">
  <dt><b>i</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='i' Line='i' -->
  <dd>Initialize the sample ranges.
  </dd>
  </dl>
  <dl id="l_q">
  <dt><b>q</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='q' Line='q' -->
  <dd>Exit interactive dispersion bin selection.
  </dd>
  </dl>
  <dl id="l_s">
  <dt><b>s</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='s' Line='s' -->
  <dd>Set a bin with the cursor.  This may be repeated any number of times.
  Two keystrokes are required to mark the two ends of the bin.
  </dd>
  </dl>
  <p>
  The parameters are listed or set with the following commands which may be
  abbreviated.  To list the value of a parameter type the command alone.
  </p>
  <div class="highlight-default-notranslate"><pre>
  :bins value             Iillumination bins
  :show                   Show the values of all the parameters
  </pre></div>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  An illumination calibration, in the form of an image, is created for each
  longslit calibration image, normally a sky spectrum.  The illumination
  calibration is determined by fitting functions across the slit (the slit
  profiles) at a number of points along the dispersion, normalizing each fitted
  function to unity at the center of the slit, and interpolating the illumination
  between the dispersion points.  The fitted data is formed by dividing the
  dispersion points into a set of bins and averaging the slit profiles within
  each bin.  The interpolation type is a user parameter.
  </p>
  <p>
  The image header keyword DISPAXIS must be present with a value of 1 for
  dispersion parallel to the lines (varying with the column coordinate) or 2
  for dispersion parallel to the columns (varying with line coordinate).
  This parameter may be added using <b>hedit</b>.  Note that if the image has
  been transposed (<b>imtranspose</b>) the dispersion axis should still refer
  to the original dispersion axis unless the physical world coordinate system
  is first reset (see <b>wcsreset</b>).  This is done in order to allow images
  which have DISPAXIS defined prior to transposing to still work correctly
  without requiring this keyword to be changed.
  </p>
  <p>
  If the output image does not exist it is first created with unit illumination
  everywhere.  Subsequently the illumination is only modified in those regions
  occupied by the input image.  Thus, an image section in the input image may
  be used to select the data to be used and for which an illumination calibration
  will be determined.  This ability is particularly userful when dealing with
  multiple slits or to exclude regions outside the slit.
  </p>
  <p>
  The dispersion bins may be selected by a range string (<i>bins</i>) or,
  if no range string is given, by the number of bins into which the dispersion
  range is to be divided (<i>nbins</i>).  When the interactive parameter
  is set (<i>interactive</i>) then the average spectrum is graphed and the
  bins may be set using the cursor or with a colon command.  Once the bins
  have been selected exit with (q)uit to continue to the slit profile fitting.
  </p>
  <p>
  Fitting of the slit profiles is done using the interactive curve fitting
  package (<b>icfit</b>).  The parameters determining the fit are the
  sample points, the averaging bin size, the fitting function,
  the order of the function, the rejection sigmas, the number of
  rejection iterations, and the rejection width.
  The sample points for the average slit profile are selected by a range string.  
  Points in the slit profile not in the sample are not used in determining
  the fitted function.  The selected sample points may be binned into a
  set of averages or medians which are used in the function fit instead of the
  sample points with the averaging bin size parameter
  <i>naverage</i>.  This parameter selects the number of sample points to be
  averaged if its value is positive or the number of points to be medianed
  if its value is negative (naturally, the absolute value is used for the
  number of points).  A value of one uses all sample points without binning.
  The fitted function may be used to reject points from the fit using the
  parameters <i>low_reject, high_reject, niterate</i> and <i>grow</i>.  If
  one or both of the rejection limits are greater than zero then the sigma
  of the residuals is computed and points with residuals less than
  <i>-low_reject</i> times the sigma and greater than <i>high_reject</i> times
  the sigma are removed and the function fitted again.  In addition points
  within a distance given by the parameter <i>grow</i> of the a rejected point
  are also rejected.  A value of zero for this parameter rejects only the
  points exceeding the rejection threshold.  Finally, the rejection procedure
  may be iterated the number of times given by the parameter <i>niterate</i>.
  </p>
  <p>
  The fitted functions may be examined and modified interactively when the
  parameter <i>interactive</i> is set.  The user is asked before each dispersion
  bin whether to perform the fit interactively.  The possible response are
  <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"NO"</span>, and <span style="font-family: monospace;">"YES"</span>.  The lower case responses only affect the
  specified dispersion bin while the upper case responses affect all following
  dispersion bins for the current image.  Thus, if the response is <span style="font-family: monospace;">"NO"</span> then
  no further prompts or interactive curve fitting need be performed while if
  the response is <span style="font-family: monospace;">"YES"</span> there are no further prompts but the slit profile
  for each dispersion bin must be graphed and exited with (q)uit.
  Changes to the fitting parameters remain in effect until they are next
  changed.  This allows the fitting parameters to be selected from only the first
  dispersion bin without requiring each dispersion bin to be graphed and
  confirmed.
  </p>
  <p>
  When a dispersion bin is to be fitted interactively the average slit profile
  and the fitted function or the residuals of the fit are graphed.
  Deleted points are marked with an x and rejected points by a diamond.
  The sample regions are indicated along the bottom of the graph.
  The cursor keys and colon commands are used to change the values
  of the fitting parameters, delete points, and window and expand the
  graph.  When the fitted function is satisfactory exit with
  with a carriage return or <span style="font-family: monospace;">'q'</span>.  The prompt for the next dispersion bin will
  then be given until the last dispersion bin has been fit.  The illumination
  calibration image is then created.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To create an illumination image non-interactively:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; illumination sky illum nbins=8 order=20 interactive=no
  </pre></div>
  <p>
  2. To determine independent illuminations for a multislit image determine the
  image sections defining each slit.  Then the illumination functions are
  computed as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; illumination sky[10:20,*],sky[35:45,*] illum,illum
  </pre></div>
  <p>
  3. Generally the slit image sections are prepared in a file which is then
  used to define the lists of input images and illuminations.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; illumination @slits @illums
  </pre></div>
  <p>
  3.  If the DISPAXIS keyword is missing and the dispersion is running
  vertically (varying with the image lines):
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit *.imh dispaxis 2 add+
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  icfit, response
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'CURSOR KEYS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

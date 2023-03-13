.. _response:

response: Determine response calibration
========================================

**Package: longslit**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  response calibration normalization response
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_calibration">
  <dt><b>calibration</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='calibration' Line='calibration' -->
  <dd>Images to use in determining response calibrations.  These are
  generally quartz continuum spectra.  An image section may be used to select
  only a portion of the image.
  </dd>
  </dl>
  <dl id="l_normalization">
  <dt><b>normalization</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='normalization' Line='normalization' -->
  <dd>Images to use determining the normalization spectrum.  In almost all cases
  the normalization images are the same as the calibration images or a
  subsection of the calibration images.
  </dd>
  </dl>
  <dl id="l_responses">
  <dt><b>responses</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='responses' Line='responses' -->
  <dd>Response calibration images to be created.  Each response image is paired
  with a calibration image.  If the image exists then it will be modified
  otherwise it is created.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Graph the average calibration spectrum and fit the normalization spectrum
  interactively?
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = INDEF' -->
  <dd>Set the response to 1 when the normalization spectrum or input image data
  fall below this value.  If INDEF then no threshold is applied.
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample' Line='sample = "*"' -->
  <dd>Sample of points to use in fitting the average calibration spectrum.
  The sample is selected with a range string.
  </dd>
  </dl>
  <dl id="l_naverage">
  <dt><b>naverage = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='naverage' Line='naverage = 1' -->
  <dd>Number of sample points to average or median before fitting the function.
  If the number is positive the average of each set of naverage sample
  points is formed while if the number is negative then the median of each set
  of points (in absolute value) is formed.  This subsample of points is
  used in fitting the normalization spectrum.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"spline3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "spline3"' -->
  <dd>Function to fit to the average image spectrum to form the normalization
  spectrum.  The options are <span style="font-family: monospace;">"spline1"</span>, <span style="font-family: monospace;">"spline3"</span>, <span style="font-family: monospace;">"legendre"</span>, and <span style="font-family: monospace;">"chebyshev"</span>.
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
  </section>
  <section id="s_cursor_keys">
  <h3>Cursor keys</h3>
  <p>
  The interactive curve fitting package <b>icfit</b> is used to fit a function
  to the average calibration spectrum.  Help for this package is found
  under the name <span style="font-family: monospace;">"icfit"</span>.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A response calibration, in the form of an image, is created for each input
  image, normally a quartz spectrum.  The response calibration is formed by
  dividing the calibration image by a normalization spectrum which is the
  same at all points along the spatial axis.  The normalization spectrum is
  obtained by averaging the normalization image across the dispersion to form
  a one dimensional spectrum and smoothing the spectrum by fitting a
  function.  The threshold value does not apply to creating or fitting of
  the normalization spectrum but only the final creation of the response
  values.  When normalizing (that is dividing the data values by the
  fit to the normalization spectrum) only pixels in which both the fitted
  normalization value and the data value are above the threshold are
  computed.  If either the normalization value or the data value is below
  the threshold the output response value is one.
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
  If the output image does not exist it is first created with unit response
  everywhere.  Subsequently the response is only modified in those regions
  occupied by the input calibration image.  Thus, image sections may be used
  to select regions in which the response is desired.  This ability is
  particularly useful when dealing with multiple slits within an image or to
  exclude regions outside the slit.
  </p>
  <p>
  Normally the normalization images are the same as the calibration images.
  In other words the calibration image is normalized by the average spectrum
  of the calibration image itself.  Sometimes, however, the normalization
  image may be a smaller image section of the calibration image to avoid
  contaminating the normalization spectrum by effects at the edge of the
  slit.  Again, this may be quite useful in multi-slit images.
  </p>
  <p>
  The normalization spectrum is smoothed by fitting a function
  using the interactive curve fitting package (<b>icfit</b>).  The
  parameters determining the fitted normalization spectrum are the sample
  points, the averaging bin size, the fitting function, the order of the
  function, the rejection sigmas, the number of rejection iterations, and
  the rejection width.  The sample points for the average spectrum are
  selected by a range string.  Points in the normalization spectrum not in the
  sample are not used in determining the fitted function.  The selected
  sample points may be binned into a set of averages or medians which are
  used in the function fit instead of the sample points with the
  averaging bin size parameter <i>naverage</i>.  This parameter selects
  the number of sample points to be averaged if its value is positive or
  the number of points to be medianed if its value is negative
  (naturally, the absolute value is used for the number of points).  A
  value of one uses all sample points without binning.  The fitted
  function may be used to reject points from the fit using the parameters
  <i>low_reject, high_reject, niterate</i> and <i>grow</i>.  If one or both
  of the rejection limits are greater than zero then the sigma of the
  residuals is computed and points with residuals less than
  <i>-low_reject</i> times the sigma and greater than <i>high_reject</i>
  times the sigma are removed and the function fitted again.  In addition
  points within a distance given by the parameter <i>grow</i> of the a
  rejected point are also rejected.  A value of zero for this parameter
  rejects only the points exceeding the rejection threshold.  Finally,
  the rejection procedure may be iterated the number of times given by
  the parameter <i>niterate</i>.
  </p>
  <p>
  The fitted function may be examined and modified interactively when the
  parameter <i>interactive</i> is set.  In this case the normalization spectrum
  and the fitted function or the residuals of the fit are graphed.
  Deleted points are marked with an x and rejected points by a diamond.
  The sample regions are indicated along the bottom of the graph.
  The cursor keys and colon commands are used to change the values
  of the fitting parameters, delete points, and window and expand the
  graph.  When the fitted function is satisfactory exit with a carriage
  return or <span style="font-family: monospace;">'q'</span> and the calibration image will be created.  Changes in
  the fitted parameters are remembered from image to image within the
  task but not outside the task.
  </p>
  <p>
  When the task finishes creating a response image the fitting parameters
  are updated in the parameter file.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To create a response image non-interactively:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; response quartz quartz response order=20 interactive=no
  </pre></div>
  <p>
  2. To determine independent responses for a multislit image determine the
  image sections defining each slit.  Then the responses are computed as
  follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; response quartz[10:20,*],quartz[35:45,*] \
  &gt;&gt;&gt; quartz[12:18,*],quartz[12:18,*] resp,resp
  </pre></div>
  <p>
  Generally the slit image sections are prepared in a file which is then
  used to define the lists of input images and response.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; response @slits @slits @responses
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
  icfit, iillumination
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'CURSOR KEYS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

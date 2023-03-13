.. _apscatter:

apscatter: Fit and remove scattered light
=========================================

**Package: argus**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  apscatter input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images in which to determine and subtract scattered light.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output scattered light subtracted images.  If no output images
  are specified or the end of the output list is reached before the end 
  of the input list then the output image will overwrite the input image.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>Apertures to recenter, resize, trace, and extract.  All apertures are
  used to define the scattered light region.  This only applies
  to apertures read from the input or reference database.  Any new
  apertures defined with the automatic finding algorithm or interactively
  are always selected.  The syntax is a list comma separated ranges
  where a range can be a single aperture number, a hyphen separated
  range of aperture numbers, or a range with a step specified by <span style="font-family: monospace;">"x&lt;step&gt;"</span>;
  for example, <span style="font-family: monospace;">"1,3-5,9-12x2"</span>.
  </dd>
  </dl>
  <dl id="l_scatter">
  <dt><b>scatter = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scatter' Line='scatter = ""' -->
  <dd>List of scattered light images.  This is the scattered light subtracted
  from the input image.  If no list is given or the end of the list is
  reached before the end of the input list then no scattered light image
  is created.
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
  all user queries are suppressed and interactive aperture editing, trace
  fitting, and interactive scattered light fitting are disabled.
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
  <dt><b>recenter = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='recenter' Line='recenter = yes' -->
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
  <dl id="l_subtract">
  <dt><b>subtract = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subtract' Line='subtract = yes' -->
  <dd>Subtract the scattered light from the input images?
  </dd>
  </dl>
  <dl id="l_smooth">
  <dt><b>smooth = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='smooth' Line='smooth = yes' -->
  <dd>Smooth the cross-dispersion fits along the dispersion?
  </dd>
  </dl>
  <dl id="l_fitscatter">
  <dt><b>fitscatter = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitscatter' Line='fitscatter = yes' -->
  <dd>Fit the scattered light across the dispersion interactively?
  The <i>interactive</i> parameter must also be yes.
  </dd>
  </dl>
  <dl id="l_fitsmooth">
  <dt><b>fitsmooth = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitsmooth' Line='fitsmooth = yes' -->
  <dd>Smooth the cross-dispersion fits along the dispersion?
  The <i>interactive</i> parameter must also be yes.
  </dd>
  </dl>
  <dl id="l_line">
  <dt><b>line = INDEF, nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='line' Line='line = INDEF, nsum = 1' -->
  <dd>The dispersion line (line or column perpendicular to the dispersion
  axis) and number of adjacent lines (half before and half after unless
  at the end of the image) used in finding, recentering, resizing,
  and editing operations.  For tracing this is the starting line and
  the same number of lines are summed at each tracing point.  This is
  also the initial line for interactive fitting of the scattered light.
  A line of INDEF selects the middle of the image along the dispersion
  axis.  A positive nsum takes a sum and a negative value selects a
  median except that tracing always uses a sum.
  </dd>
  </dl>
  <dl id="l_buffer">
  <dt><b>buffer = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='buffer' Line='buffer = 1.' -->
  <dd>Buffer distance from the aperture edges to be excluded in selecting the
  scattered light pixels to be used.
  </dd>
  </dl>
  <dl id="l_apscat1">
  <dt><b>apscat1 = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apscat1' Line='apscat1 = ""' -->
  <dd>Fitting parameters across the dispersion.  This references an additional
  set of parameters for the ICFIT package.  The default is the <span style="font-family: monospace;">"apscat1"</span>
  parameter set.  See below for additional information.
  </dd>
  </dl>
  <dl id="l_apscat2">
  <dt><b>apscat2 = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apscat2' Line='apscat2 = ""' -->
  <dd>Fitting parameters along the dispersion.  This references an additional
  set of parameters for the ICFIT package.  The default is the <span style="font-family: monospace;">"apscat2"</span>
  parameter set.  See below for additional information.
  </dd>
  </dl>
  </section>
  <section id="s_icfit_parameters_for_fitting_the_scattered_light">
  <h3>Icfit parameters for fitting the scattered light</h3>
  <p>
  There are two additional parameter sets which define the parameters used
  for fitting the scattered light across the dispersion and along the
  dispersion.  The default parameter sets are <b>apscat1</b> and <b>apscat2</b>.
  The parameters may be examined and edited by either typing their names
  or by typing <span style="font-family: monospace;">":e"</span> when editing the main parameter set with <b>eparam</b>
  and with the cursor pointing at the appropriate parameter set name.
  These parameters are used by the ICFIT package and a further
  description may be found there.
  </p>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"spline3"</span> (apscat1 and apscat2)</b></dt>
  <!-- Sec='ICFIT PARAMETERS FOR FITTING THE SCATTERED LIGHT' Level=0 Label='function' Line='function = "spline3" (apscat1 and apscat2)' -->
  <dd>Fitting function for the scattered light across and along the dispersion.
  The choices are <span style="font-family: monospace;">"legendre"</span> polynomial, <span style="font-family: monospace;">"chebyshev"</span> polynomial,
  linear spline (<span style="font-family: monospace;">"spline1"</span>), and cubic spline (<span style="font-family: monospace;">"spline3"</span>).
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 1 (apscat1 and apscat2)</b></dt>
  <!-- Sec='ICFIT PARAMETERS FOR FITTING THE SCATTERED LIGHT' Level=0 Label='order' Line='order = 1 (apscat1 and apscat2)' -->
  <dd>Number of polynomial terms or number of spline pieces for the fitting function.
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">"*"</span> (apscat1 and apscat2)</b></dt>
  <!-- Sec='ICFIT PARAMETERS FOR FITTING THE SCATTERED LIGHT' Level=0 Label='sample' Line='sample = "*" (apscat1 and apscat2)' -->
  <dd>Sample regions for fitting points.  Intervals are separated by <span style="font-family: monospace;">","</span> and an
  interval may be one point or a range separated by <span style="font-family: monospace;">":"</span>.
  </dd>
  </dl>
  <dl id="l_naverage">
  <dt><b>naverage = 1 (apscat1 and apscat2)</b></dt>
  <!-- Sec='ICFIT PARAMETERS FOR FITTING THE SCATTERED LIGHT' Level=0 Label='naverage' Line='naverage = 1 (apscat1 and apscat2)' -->
  <dd>Number of points within a sample interval to be subaveraged or submedianed to
  form fitting points.  Positive values are for averages and negative points
  for medians.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 5 (apscat1), niterate = 0 (apscat2)</b></dt>
  <!-- Sec='ICFIT PARAMETERS FOR FITTING THE SCATTERED LIGHT' Level=0 Label='niterate' Line='niterate = 5 (apscat1), niterate = 0 (apscat2)' -->
  <dd>Number of sigma clipping rejection iterations.
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 5. (apscat1) , low_reject = 3. (apscat2)</b></dt>
  <!-- Sec='ICFIT PARAMETERS FOR FITTING THE SCATTERED LIGHT' Level=0 Label='low_reject' Line='low_reject = 5. (apscat1) , low_reject = 3. (apscat2)' -->
  <dd>Lower sigma clipping rejection threshold in units of sigma determined
  from the RMS sigma of the data to the fit.
  </dd>
  </dl>
  <dl id="l_high_reject">
  <dt><b>high_reject = 2. (apscat1) , high_reject = 3. (apscat2)</b></dt>
  <!-- Sec='ICFIT PARAMETERS FOR FITTING THE SCATTERED LIGHT' Level=0 Label='high_reject' Line='high_reject = 2. (apscat1) , high_reject = 3. (apscat2)' -->
  <dd>High sigma clipping rejection threshold in units of sigma determined
  from the RMS sigma of the data to the fit.
  </dd>
  </dl>
  <dl id="l_grow">
  <dt><b>grow = 0. (apscat1 and apscat2)</b></dt>
  <!-- Sec='ICFIT PARAMETERS FOR FITTING THE SCATTERED LIGHT' Level=0 Label='grow' Line='grow = 0. (apscat1 and apscat2)' -->
  <dd>Growing radius for rejected points (in pixels).  That is, any rejected point
  also rejects other points within this distance of the rejected point.
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
  parameters from <b>apresize</b>, parameters used for centering and
  editing the apertures from <b>apedit</b>, and tracing parameters from
  <b>aptrace</b>.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The scattered light outside the apertures defining the two dimensional
  spectra is extracted, smoothed, and subtracted from each input image.  The
  approach is to first select the pixels outside the defined apertures
  and outside a buffer distance from the edge of any aperture at each
  point along the dispersion independently.  A one dimensional function
  is fit using the <b>icfit</b> package.  This fitting uses an iterative
  algorithm to further reject high values and thus fit the minima between
  the spectra.  (This even works reasonably well if no apertures are
  defined).  Because each fit is done independently the scattered light
  thus determined will not be smooth along the dispersion.  If desired
  each line along the dispersion in the scattered light surface may then
  be smoothed by again fitting a one dimensional function using the
  <b>icfit</b> package.  The final scattered light surface is then
  subtracted from the input image to form the output image.  The
  scattered light surface may be output if desired.
  </p>
  <p>
  The reason for using two one dimensional fits as opposed to a surface fit
  is that the actual shape of the scattered light is often not easily modeled
  by a simple two dimensional function.  Also the one dimensional function
  fitting offers more flexibility in defining functions and options as
  provided by the <b>icfit</b> package.
  </p>
  <p>
  The organization of the task is like the other tasks in the package
  which has options for defining apertures using a reference image,
  defining apertures through an automatic finding algorithm (see
  <b>apfind</b>), automatically recentering or resizing the apertures (see
  <b>aprecenter</b> and <b>apresize</b>), interactively editing the
  apertures (see <b>apedit</b>), and tracing the positions of the spectra
  as a function of dispersion position (see <b>aptrace</b>).  Though
  unlikely, the actual scattered light subtraction operation may be
  suppressed when the parameter <i>subtract</i> is no.  If the scattered
  light determination and fitting is done interactively (the
  <i>interactive</i> parameter set to yes) then the user is queried
  whether or not to do the fitting and subtraction for each image.  The
  responses are <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"YES"</span>, or <span style="font-family: monospace;">"NO"</span>, where the upper case
  queries suppress this query for the following images.  When the task is
  interactive there are further queries for each step of the operation
  which may also be answered both individually or collectively for all
  other input images using the four responses.
  </p>
  <p>
  When the scattered light operation is done interactively the user may
  set the fitting parameters for the scattered light functions both
  across and along the dispersion interactively.  Initially the central
  line or column is used but after exiting (with <span style="font-family: monospace;">'q'</span>) a prompt is given
  for selecting additional lines or columns and for changing the buffer
  distance.  Note that the point of the interactive stage is to set the
  fitting parameters.  When the entire image is finally fit the last set
  of fitting parameters are used for all lines or columns.
  </p>
  <p>
  The default fitting parameters are organized as separate parameter sets
  called <b>apscat1</b> for the first fits across the dispersion and
  <b>apscat2</b> for the second smoothing fits along the dispersion.
  Changes to these parameters made interactively during execution of
  this task are updated in the parameter sets.  The general idea for
  these parameters is that when fitting the pixels from between the
  apertures the iteration and rejection thresholds are set to eliminate
  high values while for smoothing along the dispersion a simple smooth
  function is all that is required.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To subtract the scattered light from a set of images to form a
  new set of images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; apscatter raw* %raw%new%*
  </pre></div>
  <p>
  This example uses a substitution in the names from raw to new.
  By default this would be done interactively
  </p>
  <p>
  2.  To subtract the scattered light in place and save the scattered light
  images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; apscatter im* "" scatter="s//im*" ref=im1 interact-
  </pre></div>
  <p>
  The prefix s is added to the original names for the scattered light.
  This operation is done noninteractively using a reference spectrum
  to define the apertures.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_APSCATTER">
  <dt><b>APSCATTER V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='APSCATTER' Line='APSCATTER V2.11' -->
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
  apfind, aprecenter, apresize,  apedit, aptrace, apsum, apmask, icfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ICFIT PARAMETERS FOR FITTING THE SCATTERED LIGHT' 'ADDITIONAL PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

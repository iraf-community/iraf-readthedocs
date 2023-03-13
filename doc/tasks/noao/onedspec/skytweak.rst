.. _skytweak:

skytweak: Sky subtract 1D spectra after tweaking sky spectra
============================================================

**Package: onedspec**

.. raw:: html

  <section id="s_summary">
  <h3>Summary</h3>
  <p>
  Sky spectra are shifted and scaled to best subtract sky features from data
  spectra.  This may be done non-interactively to minimize the RMS in some
  region or regions of the data spectra and interactively with a graphically
  search.
  </p>
  </section>
  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  skytweak input output cal
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input data images containing one dimensional spectra to be
  corrected.  All spectra in each image are corrected. The spectra need not
  be wavelength calibrated.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output corrected images.  The list must either match the input list
  or be an empty list.  If an empty list is specified the input spectra will
  be replaced by the corrected spectra.  The input spectra will also be
  replaced if the input and output image names are the same.  Any other image
  name must be for a new image otherwise a warning message will be given and
  the task will proceed to the next input image.
  </dd>
  </dl>
  <dl id="l_cal">
  <dt><b>cal  </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cal' Line='cal  ' -->
  <dd>List of sky calibration images.  If a single image is specified it
  will apply to all the input images.  Otherwise the list of calibration
  images must match the list of input images.
  </dd>
  </dl>
  <dl id="l_ignoreaps">
  <dt><b>ignoreaps = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ignoreaps' Line='ignoreaps = no' -->
  <dd>Ignore aperture numbers between the input spectra and the calibration
  spectra?  If <span style="font-family: monospace;">"no"</span> then the calibration image must contain a spectrum
  with the same aperture number as each spectrum in the input image.
  Otherwise the first spectrum in the calibration image will be used
  for all spectra in the input image.
  </dd>
  </dl>
  <dl id="l_xcorr">
  <dt><b>xcorr = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcorr' Line='xcorr = yes' -->
  <dd>Cross-correlate each input spectrum with the calibration spectrum to
  determine an shift for the calibration spectrum?  Only regions specified by
  the sample regions parameter will be used in the cross-correlation.
  </dd>
  </dl>
  <dl id="l_tweakrms">
  <dt><b>tweakrms = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tweakrms' Line='tweakrms = yes' -->
  <dd>Search for the minimum RMS in the corrected spectrum by adjusting the
  shifts and scales between the input spectrum and the calibration spectrum?
  The RMS is minimized in the specified sample regions.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Enter an interactive graphical mode to search for the best shift
  and scale between the input spectra and calibration spectra?  This
  is done after the optional automatic cross-correlation and RMS minimization
  step.  A query is made for each input spectrum so that the interactive
  step may be skipped during the execution of the task.
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample' Line='sample = "*"' -->
  <dd>Sample regions to use for cross-correlation, automatic RMS minimization,
  and RMS values.  The sample regions are specified by a list of comma
  separated ranges.  The ranges are colon separate coordinate values.
  For dispersion calibrated spectra the coordinate values are in the
  dispersion units otherwise they are in pixel coordinates.  The string <span style="font-family: monospace;">"*"</span>
  selects the entire spectrum.  The sample regions may be changed
  interactively either with the cursor or with a colon command.
  </dd>
  </dl>
  <dl id="l_lag">
  <dt><b>lag = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lag' Line='lag = 10' -->
  <dd>The cross-correlation lag to use when <i>xcorr</i> = yes.  The lag
  is given in pixels.   This is the distance to either side of the
  initial shift over which the cross-correlation profile is computed.
  If a value of zero is given then the cross-correlation step is not done.
  </dd>
  </dl>
  <dl id="l_shift">
  <dt><b>shift = 0., dshift = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shift' Line='shift = 0., dshift = 1.' -->
  <dd>The initial shift and shift step in pixels.  This initializes the shift
  search parameters for the first spectrum.  If <i>dshift</i> is zero then
  there will be no search for a new shift and the <span style="font-family: monospace;">'x'</span> interactive function is
  disabled.  These parameters may be changed interactively.  After the
  first spectrum subsequent spectra begin with the values from the last
  spectrum.
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = 1., dscale = 0.2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = 1., dscale = 0.2' -->
  <dd>The initial scale and scale step.  This initializes the scale
  search parameters for the first spectrum.  If <i>dscale</i> is zero then
  there will be no search for a new scale and the <span style="font-family: monospace;">'y'</span> interactive function is
  disabled.  These parameters may be changed interactively.  After the
  first spectrum subsequent spectra begin with the values from the last
  spectrum.
  </dd>
  </dl>
  <dl id="l_offset">
  <dt><b>offset = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='offset' Line='offset = 1.' -->
  <dd>The interactive search displays three candidate corrected spectra which
  have been normalized to a mean of one.  The offset is added and subtracted
  to separate the three candidates.  The value may be changed interactively.
  </dd>
  </dl>
  <dl id="l_smooth">
  <dt><b>smooth = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='smooth' Line='smooth = 1' -->
  <dd>The displayed candidate corrected spectra are smoothed by a moving
  boxcar average with a box size specified by this parameter.  The smoothing
  only applies to the displayed spectra and does not affect the measured
  RMS or the output corrected spectra.  The value may be changed interactively.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Input cursor for the interactive graphics.  A null value selects the
  graphics cursor otherwise a file of cursor values may be specified.
  </dd>
  </dl>
  <dl id="l_answer">
  <dt><b>answer</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='answer' Line='answer' -->
  <dd>Query parameter for responding to the interactive question.  This parameter
  should not be specified on the command line.
  </dd>
  </dl>
  <dl id="l_interp">
  <dt><b>interp = poly5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interp' Line='interp = poly5' -->
  <dd>The <b>package</b> parameter specifying the interpolation function for shifting
  the calibration spectra to match the input spectra.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Input one dimensional spectra are corrected to remove sky features by
  subtracting a shifted and scaled sky calibration spectra.
  The shifting
  allows for possible small shifts or errors in the dispersion zeropoints.
  </p>
  <p>
  The following describes the correction.  Let J(x_i) be the calibration
  spectrum at a set of pixels x_i.  An interpolation function is fit to this
  spectrum to give J(x).  The shifted and scaled calibration function
  is then
  </p>
  <div class="highlight-default-notranslate"><pre>
  (1)  J'(x) = J(x+dx) *scale
  </pre></div>
  <p>
  where dx is the pixel shift parameter and
  scale is the scale parameter.
  The output corrected spectrum is then computed as
  </p>
  <div class="highlight-default-notranslate"><pre>
  (2)  I'(x_i) = I(x_i) - J'(x_i)
  </pre></div>
  <p>
  where I' is the corrected spectrum and I is the input spectrum.  If the
  spectra are dispersion calibrated, possibly with different dispersion
  parameters, then the x values in (2) from the input spectrum are converted
  to matching pixels in the calibration spectrum using the dispersion
  functions of the two spectra.
  </p>
  <p>
  The purpose of this task is to determine the best values of the
  shift and scale parameters dx and scale.  There
  are automatic and interactive methods provided.  The automatic
  methods are cross-correlation of the calibration and input spectra
  to find a shift and an iterative search for the in both
  shift and scale that minimizes the RMS of I' in some region.
  The automatic methods are performed first, if selected, followed
  by the interactive, graphical step.  The following describes
  the steps in the order in which they occur.
  </p>
  <p>
  The initial values of the shift and scale are set by the parameters
  <i>shift</i> and <i>scale</i> for the first spectrum.  After that the values
  determined for the previous spectrum, those actually applied to correcting
  that spectrum, are used as the initial values for the next spectrum.  The
  search steps and sample regions are also initialized by task parameters but
  may be modified during the interactive step and the modified values apply
  to subsequent spectra.
  </p>
  <p>
  If the <i>xcorr</i> parameter is yes and the <i>lag</i> parameter is
  not zero the calibration spectrum is cross-correlated against the input
  spectrum.  Each spectrum is prepared as follows.  A large scale continuum
  is fit by a quadratic chebyshev using 5 iterations of sigma clipping with a
  clipping factor of 3 sigma below the fit and 1 sigma above the fit and
  rejecting the deviant points along with one pixel on either side.  This
  attempts to eliminate the effects of absorption lines.  The continuum fit
  is subtracted from the spectrum and the spectrum is extended and tapered by
  a cosine function of length given by the <i>lag</i> parameter.
  </p>
  <p>
  The prepared spectra are then cross-correlated by shifting the calibration
  spectrum plus and minus the specified <i>lag</i> amount about the current
  shift value.  Only the regions in the input spectrum specified by the
  sample regions parameter are used in the correlation.  This produces a
  correlation profile whose peak defines the relative shift between the two
  spectra.  The current shift value is updated.  This method assumes the
  common telluric features dominate within the specified sample regions.  The
  lag size should be roughly the profile widths of the telluric features.
  </p>
  <p>
  If the <i>tweakrms</i> parameter is yes and <i>dshift</i> is greater than
  zero trial corrections at the current shift value and plus and minus one
  shift step with the scale value fixed at its current value are made and the
  RMS in the sample regions computed.  If the RMS is smallest at the current
  shift value the shift step is divided in half otherwise the current shift
  value is set to the shift with the lowest RMS.  The process is then
  repeated with the new shift and shift step values.  This continues until
  either the shift step is less than 0.01 pixels or the shift is more than
  two pixels from the initial shift.  In the latter case the final shift is
  reset to the original shift.
  </p>
  <p>
  The scale factor is then varied if <i>dscale</i> is greater than zero by the
  scale step at a fixed shift in the same way as above to search for a
  smaller RMS in the sample regions.  This search terminates when the scale
  step is less than 0.01 or if the scale value has departed by 100% of the
  initial value.  In the latter case the scale value is left unchanged.
  </p>
  <p>
  The search over the shifts and scales is repeated a second time after which
  the tweak algorithm terminates.
  </p>
  <p>
  After the optional cross-correlation and tweak steps the interactive search
  mode may be entered.  This occurs if <i>interactive</i> = yes.  A query is
  asking whether to search interactively.  The answers may be <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"yes"</span>,
  <span style="font-family: monospace;">"NO"</span>, or <span style="font-family: monospace;">"YES"</span>.  The lower case answers apply to the current spectrum and
  the upper case answers apply to all subsequent spectra.  This means that if
  an answer of <span style="font-family: monospace;">"NO"</span> or <span style="font-family: monospace;">"YES"</span> is given then there will be no further queries
  for the remaining input spectra.
  </p>
  <p>
  If the interactive step is selected a graph of three candidate corrections
  for the input spectrum is displayed.  There also may be a graph of the
  calibration or input spectrum shown for reference.  Initially the
  calibration spectrum is displayed.  The additional graph may be toggled off
  and on and between the input and calibration spectra with the <span style="font-family: monospace;">'c'</span> and <span style="font-family: monospace;">'d'</span>
  keys.  The three candidate corrected spectra will be with the current shift
  and scale in the middle and plus or minus one step in either the shift or
  scale.  Initially the spectra will be at different scale values.
  Information about the current shift and scale and the step used is given in
  the graph title.
  </p>
  <p>
  One may toggle between shift steps and scale steps with the <span style="font-family: monospace;">'x'</span> (for shift)
  or <span style="font-family: monospace;">'y'</span> (for scale) keys.  The RMS in the title is the RMS within the
  currently defined sample regions.  If one of the step values is zero then a
  display of different values of that parameter will not be selected.  The
  step size will need to be set with a colon command to search in that
  parameter.
  </p>
  <p>
  If <span style="font-family: monospace;">'x'</span> is typed when the three spectra are at different shifts then the
  nearest spectrum to the y cursor at the x cursor position will be
  selected.  If the central spectrum is selected the step size is divided in
  half otherwise the current shift is changed and the  selected spectrum
  becomes the middle spectrum.  Three new spectra are then shown.  The same
  applies if <span style="font-family: monospace;">'y'</span> is typed when the three spectra are at different scales.
  This allows an interactive search similar to the iterative tweakrms method
  described previously except the user can use whatever criteria is desired
  to search for the best scale and shift.
  </p>
  <p>
  There are additional keystrokes and colon commands to set or change sample
  regions, reset the current shift, scale, and step sizes, expand the step
  size in the current mode, adjust the offsets between the spectra, and
  get help.  The <span style="font-family: monospace;">'w'</span> key and GTOOLS colon commands are available to window
  the graphs.  Any changes in the x limits apply to both graphs while y limit
  adjustments apply to the graph pointed to by the cursor.
  </p>
  <p>
  Two other commands require a short explanation.  The <span style="font-family: monospace;">'a'</span> key may
  be used to run the tweakrms algorithm starting from the current
  shift, scale, and steps and the current sample regions.  This allows
  one to graphically set or reset the sample regions before doing
  the RMS minimization.  The <span style="font-family: monospace;">":smooth"</span> command and associated
  <i>smooth</i> task parameter allow the corrected spectra to be
  displayed with a boxcar smoothing to better see faint features in
  noise.  It is important to realize that the smoothing is only
  done on the displayed spectra.  The telluric correction and computed RMS
  are done in the unsmoothed data.
  </p>
  <p>
  After the interactive step is quit with <span style="font-family: monospace;">'q'</span> or if the interactive
  step is not done then the final output spectrum is computed and
  written to the output image.  A brief log output is printed for
  each spectrum.
  </p>
  </section>
  <section id="s_cursor_keys_and_colon_commands">
  <h3>Cursor keys and colon commands</h3>
  <div class="highlight-default-notranslate"><pre>
  ? - print help
  a - automatic RMS minimization within sample regions
  c - toggle calibration spectrum display
  d - toggle data spectrum display
  e - expand (double) the step for the current selection
  q - quit
  r - redraw the graphs
  s - add or reset sample regions
  w - window commands (see :/help for additional information)
  x - graph and select from corrected shifted candidates
  y - graph and select from corrected scaled candidates
  
  :help           - print help
  :shift  [value] - print or reset the current shift
  :scale  [value] - print or reset the current scale
  :dshift [value] - print or reset the current shift step
  :dscale [value] - print or reset the current scale step
  :offset [value] - print or reset the current offset between spectra
  :sample [value] - print or reset the sample regions
  :smooth [value] - print or reset the smoothing box size
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To interactively search for a best correction with the default
  cross-correlation and tweak steps:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skytweak spec001.ms skyspec001.ms spec005.ms
  </pre></div>
  <p>
  2.  To search only for a scale factor:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skytweak spec001.ms skyspec001.ms spec005.ms xcorr- dshift=0.
  </pre></div>
  <p>
  3.  To processes a set of spectra non-interactively with the same calibration
  spectrum and to replace the input spectra with the corrected spectra and
  log the processing:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skytweak spec* "" skyspec inter- &gt; log
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_SKYTWEAK">
  <dt><b>SKYTWEAK V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SKYTWEAK' Line='SKYTWEAK V2.11' -->
  <dd>This task is new in this version.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  telluric
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SUMMARY' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR KEYS AND COLON COMMANDS' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

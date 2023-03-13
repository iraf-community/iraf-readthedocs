.. _apnoise:

apnoise: Compute and examine noise characteristics of spectra
=============================================================

**Package: apextract**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  apnoise input dmin dmax nbins
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input spectra to examine.
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
  <dl id="l_dmin">
  <dt><b>dmin, dmax, nbins</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dmin' Line='dmin, dmax, nbins' -->
  <dd>The noise sigma is computed in a set of bins over the specified
  range of image data numbers.
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
  <dl id="l_line">
  <dt><b>line = INDEF, nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='line' Line='line = INDEF, nsum = 1' -->
  <dd>The dispersion line (line or column perpendicular to the dispersion
  axis) and number of adjacent lines (half before and half after unless
  at the end of the image) used in finding, recentering, resizing,
  and editing operations.  For tracing this is the starting line and
  the same number of lines are summed at each tracing point.  A line of
  INDEF selects the middle of the image along the dispersion axis.
  A positive nsum sums the lines and a negative value takes the median.
  However, for tracing only sums are allowed and the absolute value
  is used.
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = 10.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 10.' -->
  <dd>Division threshold.  If a pixel in the two dimensional normalization spectrum
  is less than this value then a flat field value of 1 is output.
  </dd>
  </dl>
  <p>
  The following parameters control the profile and spectrum fitting.
  </p>
  <dl id="l_background">
  <dt><b>background = <span style="font-family: monospace;">"none"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = "none"' -->
  <dd>Type of background subtraction.  The choices are <span style="font-family: monospace;">"none"</span> for no
  background subtraction, <span style="font-family: monospace;">"average"</span> to average the background within the
  background regions, or <span style="font-family: monospace;">"fit"</span> to fit across the dispersion using the
  background within the background regions.  Note that the <span style="font-family: monospace;">"average"</span>
  option does not do any medianing or bad pixel checking; it is faster
  than fitting however.  Background subtraction also requires that the
  background fitting parameters are properly defined.  For the <span style="font-family: monospace;">"average"</span>
  option only the background sample regions parameter is used.
  </dd>
  </dl>
  <dl id="l_pfit">
  <dt><b>pfit = <span style="font-family: monospace;">"fit1d"</span> (fit1d|fit2d)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pfit' Line='pfit = "fit1d" (fit1d|fit2d)' -->
  <dd>Profile fitting algorithm to use with variance weighting or cleaning.
  When determining a profile the two dimensional spectrum is divided by
  an estimate of the one dimensional spectrum to form a normalized two
  dimensional spectrum profile.  This profile is then smoothed by fitting
  one dimensional functions, <span style="font-family: monospace;">"fit1d"</span>, along the lines or columns most closely
  corresponding to the dispersion axis or a special two dimensional
  function, <span style="font-family: monospace;">"fit2d"</span>, described by Marsh (see <b>approfile</b>).
  </dd>
  </dl>
  <dl id="l_clean">
  <dt><b>clean = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clean' Line='clean = no' -->
  <dd>Detect and replace deviant pixels?
  </dd>
  </dl>
  <dl id="l_skybox">
  <dt><b>skybox = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skybox' Line='skybox = 1' -->
  <dd>Box car smoothing length for sky background when using background
  subtraction.  Since the background noise is often the limiting factor
  for good extraction one may box car smooth the sky to improve the
  statistics in smooth background regions at the expense of distorting
  the subtraction near spectral features.  This is most appropriate when
  the sky regions are limited due to a small slit length.
  </dd>
  </dl>
  <dl id="l_saturation">
  <dt><b>saturation = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='saturation' Line='saturation = INDEF' -->
  <dd>Saturation or nonlinearity level.  During variance weighted extractions
  wavelength points having any pixels above this value are excluded from the
  profile determination.
  </dd>
  </dl>
  <dl id="l_readnoise">
  <dt><b>readnoise = <span style="font-family: monospace;">"0."</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='readnoise' Line='readnoise = "0."' -->
  <dd>Read out noise in photons.  This parameter defines the minimum noise
  sigma.  It is defined in terms of photons (or electrons) and scales
  to the data values through the gain parameter.  A image header keyword
  (case insensitive) may be specified to get the value from the image.
  </dd>
  </dl>
  <dl id="l_gain">
  <dt><b>gain = <span style="font-family: monospace;">"1."</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gain' Line='gain = "1."' -->
  <dd>Detector gain or conversion factor between photons/electrons and
  data values.  It is specified as the number of photons per data value.
  A image header keyword (case insensitive) may be specified to get the value
  from the image.
  </dd>
  </dl>
  <dl id="l_lsigma">
  <dt><b>lsigma = 3., usigma = 3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lsigma' Line='lsigma = 3., usigma = 3.' -->
  <dd>Lower and upper rejection thresholds, given as a number of times the
  estimated sigma of a pixel, for cleaning.
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
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  The following cursor keys and colon commands are available during the
  display of the noise sigmas and noise model.  See <b>apedit</b> for
  the commands for that mode.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ?  Print command help
  q  Quit
  r  Redraw
  w  Window the graph (see :/help)
  I  Interupt immediately
  
  :gain &lt;value&gt;           Check or set the gain model parameter
  :readnoise &lt;value&gt;      Check or set the read noise model parameter
  
  Also see the CURSOR MODE commands (:.help) and the windowing commands
  (:/help).
  </pre></div>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Apnoise</b> computes the noise sigma as a function of data value
  using the same profile model used for weighted extraction and
  cosmic ray cleanning.  In particular, the residuals used in computing the
  noise sigma are the same as those during cleanning.  By looking
  at the noise sigma as a function of data value as compared to that
  predicted by the noise model based on the read out noise and gain
  parameters one can then better refine these values for proper
  rejection of cosmic rays without rejection of valid data.
  So this task can be used to check or deduce these values and also
  to adjust them to include additional sources of error such as
  flat field noise and, especially, an additional source of noise due
  to the accuracy of the profile modeling.
  </p>
  <p>
  The first part of this task follows the standard model of allowing
  one to define apertures by finding, recentering, editing, and
  tracing.  If one has previously defined apertures then these
  steps can be skipped.  Once the apertures are defined the apertures
  are internally extracted using the profile modeling (see <b>approfile</b>)
  with the optional background subtraction, cleanning, and choices of
  profile fitting algorithm, <span style="font-family: monospace;">"fit1d"</span> or <span style="font-family: monospace;">"fit2d"</span>.  But rather than
  outputing the extracted spectrum as in <b>apsum</b> or <b>apall</b>
  or various functions of the data and profile model as in <b>apfit</b>,
  <b>apnormalize</b>, or <b>apflatten</b>, the task computes the
  residuals for all points in all apertures (essentially the same
  as the difference output of <b>apfit</b>) and determines the
  sigma (population corrected RMS) as a function of model data value
  in the specified bins.  The bins are defined by a minimum and
  maximum data value (found using <b>minmax</b>, <b>implot</b>, or
  <b>imexamine</b>) and the number of bins.
  </p>
  <p>
  The noise sigma values, with their estimated uncertainties, are then
  plotted as a function of data numer.  A curve representing the specified
  read out noise and gain is also plotted.  The user then has the
  option of varying these two parameters with colon commands.  The
  aim of this is to find a noise model which either represents the
  measure noise sigmas or at least exceeds them so that only valid
  outliers such as cosmic rays will be rejected during cleanning.
  The interactive graphical mode only has this function.  The other
  keys and colon commands are the standard ones for redrawing, windowing,
  and quitting.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To check that the read noise and gain parameters are reasonable for
  cleaning <b>apnoise</b> is run.  In this case it is assumed that the
  apertures have already been defined and traced.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; minmax lsobj
      lsobj  -2.058870315551758  490.3247375488282
  cl&gt; apnoise lsobj 0 500 50 rece- resi- edit- trace-
      A graph of the noise sigma for data between 0 and 500
      data numbers is given with a line showing the
      expected value for the current read noise and gain.
      The read noise and gain may be varied if desired.
      Exit with <span style="font-family: monospace;">'q'</span>
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_APNOISE">
  <dt><b>APNOISE V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='APNOISE' Line='APNOISE V2.11' -->
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
  apbackground, approfile, apvariance, apfit, icfit, minmax,
  apdefault, apfind, aprecenter, apresize, apedit, aptrace, apsum
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ADDITIONAL PARAMETERS' 'CURSOR COMMANDS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

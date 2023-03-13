.. _apfit:

apfit: Fit 2D spectra and output the fit, difference, or ratio
==============================================================

**Package: echelle**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  apfit input output fittype
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images to be fit.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>List of output images to be created with the  fitting results.  If the null
  string is given or the end of the output list is reached before the end
  of the input list then the input image name is used and an extension
  of <span style="font-family: monospace;">".fit"</span>, <span style="font-family: monospace;">".diff"</span>, or <span style="font-family: monospace;">".ratio"</span> is added based on the type of fit.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>Apertures to recenter, resize, trace, and fit.  This only applies
  to apertures read from the input or reference database.  Any new
  apertures defined with the automatic finding algorithm or interactively
  are always selected.  The syntax is a list comma separated ranges
  where a range can be a single aperture number, a hyphen separated
  range of aperture numbers, or a range with a step specified by <span style="font-family: monospace;">"x&lt;step&gt;"</span>;
  for example, <span style="font-family: monospace;">"1,3-5,9-12x2"</span>.
  </dd>
  </dl>
  <dl id="l_fittype">
  <dt><b>fittype = <span style="font-family: monospace;">"difference"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fittype' Line='fittype = "difference"' -->
  <dd>Type of fitted output.  The choices are:
  <dl>
  <dt><b><span style="font-family: monospace;">"fit"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"fit"' -->
  <dd>The fitted spectra are output.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"difference"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"difference"' -->
  <dd>The difference (or residuals) of the data and the fit (data - fit).
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"ratio"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"ratio"' -->
  <dd>The ratio of the data to the fit.  If a fitted pixel goes below a specified
  threshold the ratio is set to 1.
  </dd>
  </dl>
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
  <dl id="l_fit">
  <dt><b>fit = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fit' Line='fit = yes' -->
  <dd>Fit the spectra and produce a fitted output image?
  </dd>
  </dl>
  <p>
  The following two parameters are used in the finding, recentering, resizing,
  editing, and tracing operations.
  </p>
  <dl id="l_line">
  <dt><b>line = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='line' Line='line = INDEF' -->
  <dd>The starting dispersion line (line or column perpendicular to the dispersion
  axis) for the tracing.  A value of INDEF starts at the middle of the image.
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = 1' -->
  <dd>Number of dispersion lines to be summed or medianed at each step along
  the dispersion.  For tracing only summing is done and the sign is
  ignored.
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = 10.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 10.' -->
  <dd>Division threshold for ratio fit type.  If a pixel in the fitted spectrum
  is less than this value then a ratio of 1 is output.
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
  <dt><b>readnoise = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='readnoise' Line='readnoise = 0.' -->
  <dd>Read out noise in photons.  This parameter defines the minimum noise
  sigma.  It is defined in terms of photons (or electrons) and scales
  to the data values through the gain parameter.  A image header keyword
  (case insensitive) may be specified to get the value from the image.
  </dd>
  </dl>
  <dl id="l_gain">
  <dt><b>gain = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gain' Line='gain = 1' -->
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
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The two dimensional spectra within the defined apertures of the input
  images are fit by a model and new output images are created with either
  the model spectra, the difference between the input and model spectra,
  or the ratio of input and model spectra.  The type of output is
  selected by the parameter <i>fittype</i> which may have one of the
  values <span style="font-family: monospace;">"fit"</span>, <span style="font-family: monospace;">"difference"</span>, or <span style="font-family: monospace;">"ratio"</span>.
  </p>
  <p>
  Aperture definitions may be inherited from those of other images by
  specifying a reference image with the <b>references</b> parameter.
  Images in the reference list are matched with those in the
  input list in order.  If the reference image list is shorter than the
  number of input images, the last reference image is used for all
  remaining input images.  Thus, a single reference image may be given
  for all the input images or different reference images may be given for
  each input image.  The special reference name <span style="font-family: monospace;">"last"</span> may be used to
  select the last set apertures used in any of the <b>apextract</b> tasks.
  </p>
  <p>
  If an aperture reference image is not specified or no apertures are
  found for the specified reference image, previously defined apertures
  for the input image are sought in the aperture database.  Note that
  reference apertures supersede apertures for the input image.  If no
  apertures are defined they may be created automatically, the <i>find</i>
  option, or interactively in the aperture editor, if the
  <i>interactive</i> and <i>edit</i> options are set.
  </p>
  <p>
  The functions performed by the task are selected by a set of flag
  parameters.  The functions are an automatic spectrum finding and
  aperture defining algorithm (see <b>apfind</b>) which is ignored if
  apertures are already defined, automatic recentering and resizing
  algorithms (see <b>aprecenter</b> and <b>apresize</b>), an interactive
  aperture editing function (see <b>apedit</b>), a spectrum position tracing
  and trace function fit (see <b>aptrace</b>), and the main function of
  this task, two dimensional model fitting.
  </p>
  <p>
  Each function selection will produce a query for each input spectrum if
  the <i>interactive</i> parameter is set.  The queries are answered by
  <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"YES"</span>, or <span style="font-family: monospace;">"NO"</span>, where the upper case responses suppress
  the query for following images.  There are other queries associated
  with tracing which first ask whether the operation is to be done
  interactively and, if yes, lead to queries for each aperture.  If the
  <i>interactive</i> parameter is not set then aperture editing and
  interactive trace fitting are ignored.
  </p>
  <p>
  The two dimensional spectrum model consists of a smooth two dimensional
  normalized profile multiplied by the variance weighted one dimensional
  spectrum.  The profile is computed by dividing the data within the aperture
  by the one dimensional spectrum, smoothing with either low order function
  fits parallel to the dispersion axis or a special two dimensional function
  as selected by the <i>pfit</i> parameter.  The smooth profile is then used
  to improve the spectrum estimate using variance weighting and to eliminate
  deviant or cosmic ray pixels by sigma tests.  The profile algorithm is
  described in detail in <b>approfiles</b> and the variance weighted spectrum
  is described in <b>apvariance</b>.
  </p>
  <p>
  The process of determining the profile and variance weighted spectrum,
  and hence the two dimensional spectrum model, is identical to that used
  for variance weighted extraction of the one dimensional spectra in the
  tasks <b>apall</b> or <b>apsum</b>.  Most of the parameters of in this
  task are the same as those in the extraction tasks and so further
  information about them may be found in the descriptions of those tasks.
  </p>
  <p>
  Because of the connection with variance weighted extraction and cleaning
  of one dimensional spectra, this task is useful as a diagnostic tool for
  understanding and evaluating the variance weighting algorithm.
  For example the <span style="font-family: monospace;">"difference"</span> image provides the residuals in a
  two dimensional visual form.
  </p>
  <p>
  The <span style="font-family: monospace;">"fit"</span> output image does not include any background determination;
  i.e the fit is background subtracted.  Pixels outside the modeled
  spectra are set to zero.
  </p>
  <p>
  The <span style="font-family: monospace;">"difference"</span> output image is simply the difference between the
  background subtracted <span style="font-family: monospace;">"fit"</span> and the data.  Thus the difference within
  the apertures should approximate the background and outside the
  apertures the difference will be identical with the input image.
  </p>
  <p>
  The <span style="font-family: monospace;">"ratio"</span> output image does include any background in the model
  before taking the ratio of the data and model.  If a model pixel
  is less than the given <i>threshold</i> parameter the output ratio
  is set to one.  This is used to avoid division by zero and set a
  limit to noise in ratio image.  Outside of the apertures the ratio
  output pixels are set to one.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To compute the residuals of a model fit where the image already has
  aperture defined:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; apfit ls1 inter- rec- res- trace- read=3 gain=1 back=fit
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_APFIND">
  <dt><b>APFIND V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='APFIND' Line='APFIND V2.11' -->
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
  apbackground, approfile, apvariance,
  apdefault, apfind, aprecenter, apresize, apedit, aptrace, apsum, apall
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ADDITIONAL PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

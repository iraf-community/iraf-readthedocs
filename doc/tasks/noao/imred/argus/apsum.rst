.. _apsum:

apsum: Extract 1D spectra
=========================

**Package: argus**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  apsum input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images containing apertures to be extracted.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>List of output rootnames for the extracted spectra.  If the null
  string is given or the end of the output list is reached before the end
  of the input list then the input image name is used as the output rootname.
  This will not conflict with the input image since an aperture number
  extension is added for onedspec format, the extension <span style="font-family: monospace;">".ms"</span> for multispec
  format, or the extension <span style="font-family: monospace;">".ec"</span> for echelle format.
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
  <dl id="l_format">
  <dt><b>format = <span style="font-family: monospace;">"multispec"</span> (onedspec|multispec|echelle|strip)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='format' Line='format = "multispec" (onedspec|multispec|echelle|strip)' -->
  <dd>Format for output extracted spectra.  <span style="font-family: monospace;">"Onedspec"</span> format extracts each
  aperture to a separate image while <span style="font-family: monospace;">"multispec"</span> and <span style="font-family: monospace;">"echelle"</span> extract
  multiple apertures for the same image to a single output image.
  The <span style="font-family: monospace;">"multispec"</span> and <span style="font-family: monospace;">"echelle"</span> format selections differ only in the
  extension added.  The <span style="font-family: monospace;">"strip"</span> format produces a separate 2D image in
  which each column or line along the dispersion axis is shifted to
  exactly align the aperture based on the trace information.
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
  <dl id="l_profiles">
  <dt><b>profiles = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='profiles' Line='profiles = ""' -->
  <dd>List of profile images for variance weighting or cleanning.   If variance
  weighting or cleanning a profile of each aperture is computed from the
  input image unless a profile image is specified, in which case the
  profile is computed from the profile image.  The profile image must
  have the same dimensions and dispersion and it is assumed that the
  spectra have the same position and profile shape as in the object
  spectra.  Use of a profile image is generally not required even for
  faint input spectra but the option is available for those who wish
  to use it.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Run this task interactively?  If the task is not run interactively then
  all user queries are suppressed and interactive aperture editing, trace
  fitting, and extraction review are disabled.
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
  <dt><b>resize = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='resize' Line='resize = no' -->
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
  <dl id="l_extract">
  <dt><b>extract = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extract' Line='extract = yes' -->
  <dd>Extract the one dimensional aperture sums?
  </dd>
  </dl>
  <dl id="l_extras">
  <dt><b>extras = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extras' Line='extras = no' -->
  <dd>Extract the raw spectrum (if variance weighting is used), the sky spectrum
  (if background subtraction is used), and variance spectrum (if variance
  weighting is used)?  This information is extracted to the third dimension
  of the output image.
  </dd>
  </dl>
  <dl id="l_review">
  <dt><b>review = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='review' Line='review = yes' -->
  <dd>Review the extracted spectra?  The <i>interactive</i> parameter must also be
  yes.
  </dd>
  </dl>
  <dl id="l_line">
  <dt><b>line = INDEF, nsum = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='line' Line='line = INDEF, nsum = 10' -->
  <dd>The dispersion line (line or column perpendicular to the dispersion
  axis) and number of adjacent lines (half before and half after unless
  at the end of the image) used in finding, recentering, resizing,
  and editing operations.  For tracing this is the starting line and
  the same number of lines are summed at each tracing point.  A line of
  INDEF selects the middle of the image along the dispersion axis.
  A positive nsum takes a sum while a negative value selects a median
  except that tracing always uses a sum.
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background = <span style="font-family: monospace;">"none"</span> (none|average|median|minimum|fit)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = "none" (none|average|median|minimum|fit)' -->
  <dd>Type of background subtraction.  The choices are <span style="font-family: monospace;">"none"</span> for no background
  subtraction, <span style="font-family: monospace;">"average"</span> to average the background within the background
  regions, <span style="font-family: monospace;">"median"</span> to use the median in the background regions, <span style="font-family: monospace;">"minimum"</span> to
  use the minimum in the background regions, or <span style="font-family: monospace;">"fit"</span> to fit across the
  dispersion using the background within the background regions.  Note that
  the <span style="font-family: monospace;">"average"</span> option does not do any medianing or bad pixel checking,
  something which is recommended.  The fitting option is slower than the
  other options and requires additional fitting parameter.
  </dd>
  </dl>
  <dl id="l_weights">
  <dt><b>weights = <span style="font-family: monospace;">"none"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='weights' Line='weights = "none"' -->
  <dd>Type of extraction weighting.  Note that if the <i>clean</i> parameter is
  set then the weights used are <span style="font-family: monospace;">"variance"</span> regardless of the weights
  specified by this parameter.  The choices are:
  <dl>
  <dt><b><span style="font-family: monospace;">"none"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"none"' -->
  <dd>The pixels are summed without weights except for partial pixels at the
  ends.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"variance"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"variance"' -->
  <dd>The extraction is weighted by the variance based on the data values
  and a poisson/ccd model using the <i>gain</i> and <i>readnoise</i>
  parameters.
  </dd>
  </dl>
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
  <dd>Saturation or nonlinearity level in data units.  During variance weighted
  extractions wavelength points having any pixels above this value are
  excluded from the profile determination and the sigma spectrum extraction
  output, if selected by the <i>extras</i> parameter, flags wavelengths with
  saturated pixels with a negative sigma.
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
  <dt><b>lsigma = 4., usigma = 4.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lsigma' Line='lsigma = 4., usigma = 4.' -->
  <dd>Lower and upper rejection thresholds, given as a number of times the
  estimated sigma of a pixel, for cleaning.
  </dd>
  </dl>
  <dl id="l_nsubaps">
  <dt><b>nsubaps = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsubaps' Line='nsubaps = 1' -->
  <dd>During extraction it is possible to equally divide the apertures into
  this number of subapertures.  For multispec format all subapertures will
  be in the same file with aperture numbers of 1000*(subap-1)+ap where
  subap is the subaperture (1 to nsubaps) and ap is the main aperture
  number.  For echelle format there will be a separate echelle format
  image containing the same subaperture from each order.  The name
  will have the subaperture number appended.  For onedspec format
  each subaperture will be in a separate file with extensions and
  aperture numbers as in the multispec format.
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
  <p>
  When this operation is performed from the task <b>apall</b> all
  parameters except the package parameters are included in that task.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  For each image in the input image list, the two dimensional spectra are
  extracted to one dimensional spectra by summing the pixels across the
  dispersion axis at each wavelength along the dispersion axis within a
  set of defined apertures.  The extraction apertures consist of an
  aperture number, a beam number, a title, a center, limits relative to
  the center, a curve describing shifts of the aperture center across the
  dispersion axis as a function of the wavelength, and parameters for
  background fitting and subtraction.  See <b>apextract</b> for a more
  detailed discussion of the aperture structures.
  </p>
  <p>
  The extracted spectra are recorded in one, two, or three dimensional
  images depending on the <i>format</i> and <i>extras</i> parameters.  The
  output image rootnames are specified by the <i>output</i> list. If the
  list is empty or shorter than the input list the missing names are
  taken to be the same as the input image names.  Because the rootnames
  have extensions added it is common to default to the input names in
  order to preserve a naming relation between the input two dimensional
  spectra and the extracted spectra.
  </p>
  <p>
  When the parameter <i>extras</i>=no only the extracted spectra are
  output.  If the format parameter <i>format</i>=<span style="font-family: monospace;">"onedspec"</span> the output
  aperture extractions are one dimensional images with names formed from
  the output rootname and a numeric extension given by the aperture
  number; i.e. root.0001 for aperture 1.  Note that there will be as many
  output images as there are apertures for each input image, all with the
  same output rootname but with different aperture extensions.  The
  aperture beam number associated with each aperture is recorded in the
  output image under the keyword BEAM-NUM.  The output image name format
  and the BEAM-NUM entry in the image are chosen to be compatible with
  the <b>onedspec</b> package.
  </p>
  <p>
  If the format parameter is <span style="font-family: monospace;">"echelle"</span> or <span style="font-family: monospace;">"multispec"</span> the output aperture
  extractions are put into a two dimensional image with a name formed from
  the output rootname and the extension <span style="font-family: monospace;">".ech"</span> or <span style="font-family: monospace;">".ms"</span>.  Each line in
  the output image corresponds to one aperture.  Thus in this format
  there is one output image for each input image.  These are the preferred
  output formats for reasons of compactness and ease of handling.  These
  formats are compatible with the <b>onedspec</b>, <b>echelle</b>, and
  <b>msred</b> packages.  The relation between the line and the aperture
  numbers is given by the header parameter APNUMn where n is the line and
  the value is the aperture number and other numeric information.
  </p>
  <p>
  If the <i>extras</i> parameter is set to yes then the above formats
  become three dimensional.  Each plane in the third dimension contains
  associated information for the spectra in the first plane.  If variance
  weighted extractions are done the unweighted spectra are recorded.  If
  background subtraction is done the background spectra are recorded.  If
  variance weighted extractions are done the sigma spectrum (the
  estimated sigma of each spectrum pixel based on the individual
  variances of the pixels summed) is recorded.  The order of the
  additional information is as given above.  For example, an unweighted
  extraction with background subtraction will have one additional plane
  containing the sky spectra while a variance weighted extraction with
  background subtractions will have the variance weighted spectra, the
  unweighted spectra, the background spectra, and the sigma spectra in
  consecutive planes.
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
  this task, one dimensional spectrum extraction.
  </p>
  <p>
  Each function selection will produce a query for each input spectrum if
  the <i>interactive</i> parameter is set.  The queries are answered by
  <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"YES"</span>, or <span style="font-family: monospace;">"NO"</span>, where the upper case responses suppress
  the query for following images.  There are other queries associated
  with tracing and extracted spectrum review which first ask whether the
  operation is to be done interactively and, if yes, lead to queries for
  each aperture.  The cursor keys available during spectrum review are
  minimal, only the CURSOR MODE keys for expanding and adjusting the
  graph are available and the quit key <span style="font-family: monospace;">'q'</span>.  If the <i>interactive</i>
  parameter is not set then aperture editing, interactive trace fitting,
  and spectrum review are ignored.
  </p>
  <p>
  Background sky subtraction is done during the extraction based on
  background regions and parameters defined by the default parameters or
  changed during the interactive setting of the apertures.  The background
  subtraction options are to do no background subtraction, subtract the
  average, median, or minimum of the pixels in the background regions, or to
  fit a function and subtract the function from under the extracted object
  pixels.  The background regions are specified in pixels from
  the aperture center and follow changes in center of the spectrum along the
  dispersion.  The syntax is colon separated ranges with multiple ranges
  separated by a comma or space.  The background fitting uses the <b>icfit</b>
  routines which include medians, iterative rejection of deviant points, and
  a choice of function types and orders.  Note that it is important to use a
  method which rejects cosmic rays such as using either medians over all the
  background regions (<i>background</i> = <span style="font-family: monospace;">"median"</span>) or median samples during
  fitting (<i>b_naverage</i> &lt; -1).  The background subtraction algorithm and
  options are described in greater detail in <b>apsum</b> and
  <b>apbackground</b>.
  </p>
  <p>
  Since the background noise is often the limiting factor for good
  extraction one may box car smooth the sky to improve the statistics in
  smooth background regions at the expense of distorting the subtraction
  near spectra features.  This is most appropriate when the sky region is
  limited due to small slit length.  The smoothing length is specified by
  the parameter <i>skybox</i>.
  </p>
  <p>
  For a more extended discussion about the background determination see
  <b>apbackground</b>.
  </p>
  <p>
  The aperture extractions consists of summing all the background
  subtracted pixel values at a given wavelength within the aperture
  limits.  The aperture limits form a fixed width aperture but the center
  varies smoothly to follow changes in the position of the spectrum
  across the dispersion axis.  At the ends of the aperture partial pixels
  are used.
  </p>
  <p>
  The pixels in the sum may be weighted as specified by the <i>weights</i>
  parameter.  If the weights parameter is <span style="font-family: monospace;">"none"</span> and the <i>clean</i>
  parameter is no then the simple sum of the pixels (with fractional
  endpoints) is extracted.  If the weights parameter is <span style="font-family: monospace;">"variance"</span> or if
  the <b>clean</b> parameter is yes the pixels are weighted by their
  estimated variance derived from a noise model based on the <i>gain</i>
  and <i>readnoise</i> parameters and a smooth profile function.  Normally
  the profile function is determined from the data being extracted.
  However, one may substitute a <span style="font-family: monospace;">"profile"</span> image as specified by the
  <i>profiles</i> parameter for computing the profile.  This requires that
  the profile image have spectra of identical position and profile as
  the image being extracted.  For example, this would likely be the case
  with fiber spectra and an off-telescope spectrograph and a strong flat
  field or object spectrum could be used for weak spectra.  Note that
  experience has shown that even for very weak spectra there is little
  improvement with using a separate profile image but the user is free
  to experiment.
  </p>
  <p>
  When the <i>clean</i> parameter is set pixels deviating by more than a
  specified number of sigma from the profile function are excluded from the
  variance weighted sum.  Note that the <i>clean</i> parameter always selects
  variance weights.  For a more complete discussion of the extraction sums,
  variance weighting, cleaning, the noise model, and profile function
  determination see <b>apvariance</b> and <b>approfiles</b>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To simply extract the spectra from a multislit observation:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; apsum multislit1
  </pre></div>
  <p>
  The positions of the slits are defined using either automatic finding
  or with the aperture editor.  The positions of the slits are traced if
  necessary and then the apertures are extracted to the image
  <span style="font-family: monospace;">"multslit1.ms"</span>.  The steps of defining the slit positions and tracing
  can be done as part of this command or previously using the other tasks
  in the <b>apextract</b> package.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_APSUM">
  <dt><b>APSUM V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='APSUM' Line='APSUM V2.11' -->
  <dd>The <span style="font-family: monospace;">"apertures"</span> parameter can be used to select apertures for resizing,
  recentering, tracing, and extraction.  This parameter name was previously
  used for selecting apertures in the recentering algorithm.  The new
  parameter name for this is now <span style="font-family: monospace;">"aprecenter"</span>.
  The <span style="font-family: monospace;">"nsubaps"</span> parameter now allows onedspec and echelle output formats.
  The echelle format is appropriate for treating each subaperture as
  a full echelle extraction.
  The dispersion axis parameter was moved to purely a package parameter.
  As a final step when computing a weighted/cleaned spectrum the total
  fluxes from the weighted spectrum and the simple unweighted spectrum
  (excluding any deviant and saturated pixels) are computed and a
  <span style="font-family: monospace;">"bias"</span> factor of the ratio of the two fluxes is multiplied into
  the weighted spectrum and the sigma estimate.  This makes the total
  fluxes the same.  In this version the bias factor is recorded in the logfile
  if one is kept.  Also a check is made for unusual bias factors.
  If the two fluxes disagree by more than a factor of two a warning
  is given on the standard output and the logfile with the individual
  total fluxes as well as the bias factor.  If the bias factor is
  negative a warning is also given and no bias factor is applied.
  In the previous version a negative (inverted) spectrum would result.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  apbackground, apvariance, approfile,
  apdefault, apfind, aprecenter, apresize, apedit, aptrace, apall
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ADDITIONAL PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

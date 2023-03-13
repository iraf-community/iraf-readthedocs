.. _apnormalize:

apnormalize: Normalize 2D apertures by 1D functions
===================================================

**Package: ctioslit**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  apnormalize input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images to be normalized.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output image names for the normalized input images.  If no output
  name is given then the input name is used as a root with the extension
  <span style="font-family: monospace;">".norm"</span> added.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>Apertures to recenter, resize, trace, and normalize.  This only applies
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
  <dl id="l_normalize">
  <dt><b>normalize = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='normalize' Line='normalize = yes' -->
  <dd>Normalize the aperture spectra by a one dimensional function?
  </dd>
  </dl>
  <dl id="l_fitspec">
  <dt><b>fitspec = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitspec' Line='fitspec = yes' -->
  <dd>Fit normalization spectrum interactively?  The <i>interactive</i>
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
  A negative nsum selects a median rather than a sum except that
  tracing always uses a sum.
  </dd>
  </dl>
  <dl id="l_cennorm">
  <dt><b>cennorm = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cennorm' Line='cennorm = no' -->
  <dd>Normalize to the aperture center rather than the mean?
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = 10.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 10.' -->
  <dd>All pixels in the normalization spectrum less than this value are replaced
  by this value.
  </dd>
  </dl>
  <p>
  The following parameters control the normalization spectrum extraction.
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
  <dd>The extraction is weighted by estimated variances of the pixels using
  a poisson noise model.
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
  <p>
  The following parameters are used to fit the normalization spectrum using
  the ICFIT routine.
  </p>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"legendre"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "legendre"' -->
  <dd>Fitting function for the normalization spectra.  The choices are <span style="font-family: monospace;">"legendre"</span>
  polynomial, <span style="font-family: monospace;">"chebyshev"</span> polynomial, linear spline (<span style="font-family: monospace;">"spline1"</span>), and
  cubic spline (<span style="font-family: monospace;">"spline3"</span>).
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 1' -->
  <dd>Number of polynomial terms or number of spline pieces for the fitting function.
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample' Line='sample = "*"' -->
  <dd>Sample regions for fitting points.  Intervals are separated by <span style="font-family: monospace;">","</span> and an
  interval may be one point or a range separated by <span style="font-family: monospace;">":"</span>.
  </dd>
  </dl>
  <dl id="l_naverage">
  <dt><b>naverage = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='naverage' Line='naverage = 1' -->
  <dd>Number of points within a sample interval to be subaveraged or submedianed to
  form fitting points.  Positive values are for averages and negative points
  for medians.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 0' -->
  <dd>Number of sigma clipping rejection iterations.
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 3. , high_reject = 3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_reject' Line='low_reject = 3. , high_reject = 3.' -->
  <dd>Lower and upper sigma clipping rejection threshold in units of sigma determined
  from the RMS sigma of the data to the fit.
  </dd>
  </dl>
  <dl id="l_grow">
  <dt><b>grow = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grow' Line='grow = 0.' -->
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
  For each image in the input image list the two dimensional spectra
  defined by a set of apertures are normalized by a one dimensional
  normalization function derived by extracting and smoothing the spectrum
  by fitting a function with the <b>icfit</b> procedure.  The value of the
  fitting function at each point along the dispersion, divided by the
  aperture width to form a mean or scaled to the same mean as the center
  pixel of the aperture depending on the <i>cennorm</i> parameter, is
  divided into the two dimensional input aperture.  All points outside
  the apertures are set to unity.
  </p>
  <p>
  The purpose of this task is to remove a general shape from the aperture
  spectra.  If low order (order = 1 for instance) functions are used then
  only the amplitudes of the spectra are affected, shifting each aperture
  to approximately unit intensity per pixel.  If high order functions are
  used only the small spatial scale variations are preserved.  This
  is useful for making flat field images with the spectral signature of the
  continuum source removed or for producing two dimensional normalized
  spectra similar to the task <b>onedspec.continuum</b>.  For flat fields
  this algorithm retains the profile shape which may be useful for
  removing the profile response in short slit data.  However, often
  one does not want the profile of the flat fielded observation to be
  modified in which case the task <b>apflatten</b> should be used.
  </p>
  <p>
  The normalization spectrum is first extracted in the same way as is
  the one dimensional extraction in <b>apsum</b> or <b>apall</b>.  In
  particular the same parameters for selecting weighting and cleaning
  are available.  After extraction the spectrum is fit using the
  <b>icfit</b> routine.  This may be done interactively or noninteractively
  depending on the <i>interactive</i> parameter.  The default fitting
  parameters are part of this task.  The goal of the fitting depends
  on the application.  One may be trying to simply continuum normalize,
  in which case one wants to iteratively reject and grow the rejected
  points to exclude the lines and fit the continuum with a
  moderate order function (see <b>continuum</b> for more discussion).  
  If one wants to simply normalize all spectra to a common flux, say to
  remove a blaze function in echelle data, then an order of 1 will
  normalize by a constant.  For flat field and profile correction of
  small slits one wants to fit the large scale shape of the
  spectrum but not fit the small bumps and wiggles due to sensitivity
  variations and fringing.
  </p>
  <p>
  The smoothed extracted spectrum represents the total flux within the
  aperture.  There are two choices for scaling to a normalization per
  pixel.  One is to divide by the aperture width, thus computing an average
  flux normalization.  In this case the peak of the spectrum will be
  greater than unity.  This is done when <i>cennorm</i> = no.  When this
  parameter has the value yes then the mean of the normalization spectrum
  is scaled to the mean of the aperture center, computed by linearly
  interpolating the two pixels about the traced center.  This will give
  values near one for the pixels at the center of the aperture in the
  final output image.
  </p>
  <p>
  Before division of each pixel by the appropriate dispersion point in
  the normalization spectrum, all pixels below the value specified by the
  <i>threshold</i> parameter in the normalization spectrum are replaced by
  the threshold value.  This suppresses division by very small numbers.
  Finally, the pixels within the aperture are divided by the normalization
  function and the pixels outside the apertures are set to 1.
  </p>
  <p>
  The remainder of this description covers the basic steps defining the
  apertures to be used.  These steps and parameter are much the same as
  in any of the other <b>apextract</b> tasks.
  </p>
  <p>
  Aperture definitions may be inherited from those of other images by
  specifying a reference image with the <b>references</b> parameter.
  Images in the reference list are matched with those in the input list
  in order.  If the reference image list is shorter than the number of
  input images, the last reference image is used for all remaining input
  images.  Thus, a single reference image may be given for all the input
  images or different reference images may be given for each input
  image.  The special reference name <span style="font-family: monospace;">"last"</span> may be used to select the
  last set apertures used in any of the <b>apextract</b> tasks.
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
  this task, the one dimensional normalization of the aperture
  profiles.
  </p>
  <p>
  Each function selection will produce a query for each input spectrum if
  the <i>interactive</i> parameter is set.  The queries are answered by
  <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"YES"</span>, or <span style="font-family: monospace;">"NO"</span>, where the upper case responses suppress
  the query for following images.  There are other queries associated
  with tracing which first ask whether the operation is to be done
  interactively and, if yes, lead to queries for each aperture.  If the
  <i>interactive</i> parameter is not set then aperture editing,
  interactive trace fitting, and interactive spectrum shape fitting are ignored.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To make a flat field image which leaves the total counts of the object
  images approximately unchanged from a quartz echelle or slitlet image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; apnormalize qtz001,qtz002 flat001,flat002
  Yes find
  No resize
  No edit
  Yes trace
  Yes trace interactively
  NO
  Yes flatten
  Yes fit interactively
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_APNORMALIZE">
  <dt><b>APNORMALIZE V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='APNORMALIZE' Line='APNORMALIZE V2.11' -->
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
  apbackground, approfile, apvariance, apfit, icfit,
  apdefault, apfind, aprecenter, apresize, apedit, aptrace, apsum
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ADDITIONAL PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

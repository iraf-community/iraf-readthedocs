.. _apall:

apall: Extract 1D spectra (all parameters in one task)
======================================================

**Package: kpnocoude**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  apall input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>List of output root names for extracted spectra.  If the null
  string is given or the end of the output list is reached before the end
  of the input list then the input image name is used as the output root name.
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
  Input images without/with a database entry are skipped silently.
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
  <p style="text-align:center">PROCESSING PARAMETERS
  
  </p>
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
  <dl id="l_extract">
  <dt><b>extract = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extract' Line='extract = yes' -->
  <dd>Extract the one dimensional aperture sums?
  </dd>
  </dl>
  <dl id="l_extras">
  <dt><b>extras = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extras' Line='extras = yes' -->
  <dd>Extract the raw spectrum (if variance weighting is used), the sky spectrum
  (if background subtraction is used), and sigma spectrum (if variance
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
  and editing operations.  A line of INDEF selects the middle of the
  image along the dispersion axis.  A positive nsum selects a sum of
  lines and a negative selects a median of lines.
  </dd>
  </dl>
  <p style="text-align:center">DEFAULT APERTURE PARAMETERS
  
  </p>
  <dl id="l_lower">
  <dt><b>lower = -5., upper = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lower' Line='lower = -5., upper = 5.' -->
  <dd>Default lower and upper aperture limits relative to the aperture center.
  These limits are used for apertures found with <b>apfind</b> and when
  defining the first aperture in <b>apedit</b>.
  </dd>
  </dl>
  <dl id="l_apidtable">
  <dt><b>apidtable = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apidtable' Line='apidtable = ""' -->
  <dd>Aperture identification table.  This may be either a text file or an
  image.  A text file consisting of lines with an aperture number, beam
  number, and aperture title or identification.  An image will contain the
  keywords SLFIBnnn with string value consisting of aperture number, beam
  number, optional right ascension and declination, and aperture title.  This
  information is used to assign aperture information automatically in
  <b>apfind</b> and <b>apedit</b>.
  </dd>
  </dl>
  <p style="text-align:center">DEFAULT BACKGROUND PARAMETERS
  
  </p>
  <dl id="l_b_function">
  <dt><b>b_function = <span style="font-family: monospace;">"chebyshev"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_function' Line='b_function = "chebyshev"' -->
  <dd>Default background fitting function.  The fitting function types are
  <span style="font-family: monospace;">"chebyshev"</span> polynomial, <span style="font-family: monospace;">"legendre"</span> polynomial, <span style="font-family: monospace;">"spline1"</span> linear spline, and
  <span style="font-family: monospace;">"spline3"</span> cubic spline.
  </dd>
  </dl>
  <dl id="l_b_order">
  <dt><b>b_order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_order' Line='b_order = 1' -->
  <dd>Default background function order.  The order refers to the number of
  terms in the polynomial functions or the number of spline pieces in the spline
  functions.
  </dd>
  </dl>
  <dl id="l_b_sample">
  <dt><b>b_sample = <span style="font-family: monospace;">"-10:-6,6:10"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_sample' Line='b_sample = "-10:-6,6:10"' -->
  <dd>Default background sample.  The sample is given by a set of colon separated
  ranges each separated by either whitespace or commas.  The string <span style="font-family: monospace;">"*"</span> refers
  to all points.  Note that the background coordinates are relative to the
  aperture center and not image pixel coordinates so the endpoints need not
  be integer.
  </dd>
  </dl>
  <dl id="l_b_naverage">
  <dt><b>b_naverage = -3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_naverage' Line='b_naverage = -3' -->
  <dd>Default number of points to average or median.  Positive numbers
  average that number of sequential points to form a fitting point.
  Negative numbers median that number, in absolute value, of sequential
  points.  A value of 1 does no averaging and each data point is used in the
  fit.
  </dd>
  </dl>
  <dl id="l_b_niterate">
  <dt><b>b_niterate = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_niterate' Line='b_niterate = 0' -->
  <dd>Default number of rejection iterations.  If greater than zero the fit is
  used to detect deviant fitting points and reject them before repeating the
  fit.  The number of iterations of this process is given by this parameter.
  </dd>
  </dl>
  <dl id="l_b_low_reject">
  <dt><b>b_low_reject = 3., b_high_reject = 3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_low_reject' Line='b_low_reject = 3., b_high_reject = 3.' -->
  <dd>Default background lower and upper rejection sigmas.  If greater than zero
  points deviating from the fit below and above the fit by more than this
  number of times the sigma of the residuals are rejected before refitting.
  </dd>
  </dl>
  <dl id="l_b_grow">
  <dt><b>b_grow = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_grow' Line='b_grow = 0.' -->
  <dd>Default reject growing radius.  Points within a distance given by this
  parameter of any rejected point are also rejected.
  </dd>
  </dl>
  <p style="text-align:center">APERTURE CENTERING PARAMETERS
  
  </p>
  <dl id="l_width">
  <dt><b>width = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='width' Line='width = 5.' -->
  <dd>Width of spectrum profiles.  This parameter is used for the profile
  centering algorithm in this and other tasks.
  </dd>
  </dl>
  <dl id="l_radius">
  <dt><b>radius = 10.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radius' Line='radius = 10.' -->
  <dd>The profile centering error radius for the centering algorithm.
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 0.' -->
  <dd>Centering threshold for the centering algorithm.  The range of pixel intensities
  near the initial centering position must exceed this threshold.
  </dd>
  </dl>
  <p style="text-align:center">AUTOMATIC FINDING AND ORDERING PARAMETERS
  
  </p>
  <dl id="l_nfind">
  <dt><b>nfind</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nfind' Line='nfind' -->
  <dd>Maximum number of apertures to be defined.  This is a query parameter
  so the user is queried for a value except when given explicitly on
  the command line.
  </dd>
  </dl>
  <dl id="l_minsep">
  <dt><b>minsep = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minsep' Line='minsep = 5.' -->
  <dd>Minimum separation between spectra.  Weaker spectra or noise within this
  distance of a stronger spectrum are rejected.
  </dd>
  </dl>
  <dl id="l_maxsep">
  <dt><b>maxsep = 1000.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxsep' Line='maxsep = 1000.' -->
  <dd>Maximum separation between adjacent spectra.  This parameter
  is used to identify missing spectra in uniformly spaced spectra produced
  by fiber spectrographs.  If two adjacent spectra exceed this separation
  then it is assumed that a spectrum is missing and the aperture identification
  assignments will be adjusted accordingly.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = <span style="font-family: monospace;">"increasing"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = "increasing"' -->
  <dd>When assigning aperture identifications order the spectra <span style="font-family: monospace;">"increasing"</span>
  or <span style="font-family: monospace;">"decreasing"</span> with increasing pixel position (left-to-right or
  right-to-left in a cross-section plot of the image).
  </dd>
  </dl>
  <p style="text-align:center">RECENTERING PARAMETERS
  
  </p>
  <dl id="l_aprecenter">
  <dt><b>aprecenter = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='aprecenter' Line='aprecenter = ""' -->
  <dd>List of apertures to be used in shift calculation.
  </dd>
  </dl>
  <dl id="l_npeaks">
  <dt><b>npeaks = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='npeaks' Line='npeaks = INDEF' -->
  <dd>Select the specified number of apertures with the highest peak values
  to be recentered.  If the number is INDEF all apertures will be selected.
  If the value is less than 1 then the value is interpreted as a fraction
  of total number of apertures.
  </dd>
  </dl>
  <dl id="l_shift">
  <dt><b>shift = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shift' Line='shift = yes' -->
  <dd>Use the average shift from recentering the apertures selected by the
  <i>aprecenter</i> parameter to apply to the apertures selected by the
  <i>apertures</i> parameter.  The recentering is then a constant shift for
  all apertures.
  </dd>
  </dl>
  <p style="text-align:center">RESIZING PARAMETERS
  
  </p>
  <dl id="l_llimit">
  <dt><b>llimit = INDEF, ulimit = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='llimit' Line='llimit = INDEF, ulimit = INDEF' -->
  <dd>Lower and upper aperture size limits.  If the parameter <i>ylevel</i> is
  INDEF then these limits are assigned to all apertures.  Otherwise
  these parameters are used as limits to the resizing operation.
  A value of INDEF places the aperture limits at the image edge (for the
  dispersion line used).
  </dd>
  </dl>
  <dl id="l_ylevel">
  <dt><b>ylevel = 0.1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ylevel' Line='ylevel = 0.1' -->
  <dd>Data level at which to set aperture limits.  If it is INDEF then the
  aperture limits are set at the values given by the parameters
  <i>llimit</i> and <i>ulimit</i>.  If it is not INDEF then it is a
  fraction of the peak or an actual data level depending on the parameter
  <i>peak</i>.  It may be relative to a local background or to zero
  depending on the parameter <i>bkg</i>.
  </dd>
  </dl>
  <dl id="l_peak">
  <dt><b>peak = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='peak' Line='peak = yes' -->
  <dd>Is the data level specified by <i>ylevel</i> a fraction of the peak?
  </dd>
  </dl>
  <dl id="l_bkg">
  <dt><b>bkg = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bkg' Line='bkg = yes' -->
  <dd>Subtract a simple background when interpreting the <b>ylevel</b> parameter.
  The background is a slope connecting the first inflection points
  away from the aperture center.
  </dd>
  </dl>
  <dl id="l_r_grow">
  <dt><b>r_grow = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='r_grow' Line='r_grow = 0.' -->
  <dd>Change the lower and upper aperture limits by this fractional amount.
  The factor is multiplied by each limit and the result added to limit.
  </dd>
  </dl>
  <dl id="l_avglimits">
  <dt><b>avglimits = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='avglimits' Line='avglimits = no' -->
  <dd>Apply the average lower and upper aperture limits to all apertures.
  </dd>
  </dl>
  <p style="text-align:center">TRACING PARAMETERS
  
  </p>
  <dl id="l_t_nsum">
  <dt><b>t_nsum = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_nsum' Line='t_nsum = 10' -->
  <dd>Number of dispersion lines to be summed at each step along the dispersion.
  </dd>
  </dl>
  <dl id="l_t_step">
  <dt><b>t_step = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_step' Line='t_step = 10' -->
  <dd>Step along the dispersion axis between determination of the spectrum
  positions.
  </dd>
  </dl>
  <dl id="l_t_nlost">
  <dt><b>t_nlost = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_nlost' Line='t_nlost = 3' -->
  <dd>Number of consecutive steps in which the profile is lost before quitting
  the tracing in one direction.  To force tracing to continue through
  regions of very low signal this parameter can be made large.  Note,
  however, that noise may drag the trace away before it recovers.
  </dd>
  </dl>
  <dl id="l_t_function">
  <dt><b>t_function = <span style="font-family: monospace;">"legendre"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_function' Line='t_function = "legendre"' -->
  <dd>Default trace fitting function.  The fitting function types are
  <span style="font-family: monospace;">"chebyshev"</span> polynomial, <span style="font-family: monospace;">"legendre"</span> polynomial, <span style="font-family: monospace;">"spline1"</span> linear spline, and
  <span style="font-family: monospace;">"spline3"</span> cubic spline.
  </dd>
  </dl>
  <dl id="l_t_order">
  <dt><b>t_order = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_order' Line='t_order = 2' -->
  <dd>Default trace function order.  The order refers to the number of
  terms in the polynomial functions or the number of spline pieces in the spline
  functions.
  </dd>
  </dl>
  <dl id="l_t_sample">
  <dt><b>t_sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_sample' Line='t_sample = "*"' -->
  <dd>Default fitting sample.  The sample is given by a set of colon separated
  ranges each separated by either whitespace or commas.  The string <span style="font-family: monospace;">"*"</span> refers
  to all points.
  </dd>
  </dl>
  <dl id="l_t_naverage">
  <dt><b>t_naverage = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_naverage' Line='t_naverage = 1' -->
  <dd>Default number of points to average or median.  Positive numbers
  average that number of sequential points to form a fitting point.
  Negative numbers median that number, in absolute value, of sequential
  points.  A value of 1 does no averaging and each data point is used in the
  </dd>
  </dl>
  <dl id="l_t_niterate">
  <dt><b>t_niterate = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_niterate' Line='t_niterate = 0' -->
  <dd>Default number of rejection iterations.  If greater than zero the fit is
  used to detect deviant traced positions and reject them before repeating the
  fit.  The number of iterations of this process is given by this parameter.
  </dd>
  </dl>
  <dl id="l_t_low_reject">
  <dt><b>t_low_reject = 3., t_high_reject = 3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_low_reject' Line='t_low_reject = 3., t_high_reject = 3.' -->
  <dd>Default lower and upper rejection sigma.  If greater than zero traced
  points deviating from the fit below and above the fit by more than this
  number of times the sigma of the residuals are rejected before refitting.
  </dd>
  </dl>
  <dl id="l_t_grow">
  <dt><b>t_grow = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_grow' Line='t_grow = 0.' -->
  <dd>Default reject growing radius.  Traced points within a distance given by this
  parameter of any rejected point are also rejected.
  </dd>
  </dl>
  <p style="text-align:center">EXTRACTION PARAMETERS
  
  </p>
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
  <dl id="l_weights">
  <dt><b>weights = <span style="font-family: monospace;">"none"</span> (none|variance)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='weights' Line='weights = "none" (none|variance)' -->
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
  Dispersion axis and I/O parameters are taken from the package parameters.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task provides functions for defining, modifying, tracing, and
  extracting apertures from two dimensional spectra.  The functions
  desired are selected using switch parameters.  When the task is
  run interactively queries are made at each step allowing additional
  control of the operations performed on each input image.
  </p>
  <p>
  The functions, in the order in which they are generally performed, are
  summarized below.
  </p>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Automatically find a specified number of spectra and assign default
  apertures.  Apertures may also be inherited from another image or
  defined using an interactive graphical interface called the <i>aperture
  editor</i>.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Recenter selected reference apertures on the image spectrum profiles.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Resize the selected reference apertures based on spectrum profile width.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Interactively define or adjust aperture definitions using a graphical
  interface called the <i>aperture editor</i>.  All function may also
  be performed from this editor and, so, provides an alternative
  method of processing and extracting spectra.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Trace the positions of the selected spectra profiles from a starting image line
  or column to other image lines or columns and fit a smooth function.
  The trace function is used to shift the center of the apertures
  at each dispersion point in the image.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Extract the flux in the selected apertures into one dimensional spectra in
  various formats.  This includes possible background subtraction, variance
  weighting, and bad pixel rejection.
  </dd>
  </dl>
  <p>
  Each of these functions has different options and parameters.  In
  addition to selecting any of these functions in this task, they may
  also be selected using the aperture editor and as individual
  commands (which themselves allow selection of other functions).  When
  broken down into individual tasks the parameters are also sorted by
  their function though there are then some mutual parameter
  interdependencies.  This functional decomposition is what was available
  prior to the addition of the <b>apall</b> task.  It is recommended that
  this task be used because it collects all the parameters in one
  place eliminating confusion over where a particular parameter
  is defined.  However, documenting the various functions
  is better organized in terms of the separate descriptions given for
  each of the functions; namely under the help topics
  <b>apdefault, apfind, aprecenter, apresize, apedit,
  aptrace</b>, and <b>apsum</b>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  This example may be executed if desired.  First we create an artificial
  spectrum with four spectra and a background.  After it is created you
  can display or plot it.  Next we define the dispersion axis and set the
  verbose flag to better illustrate what is happening.  The task APALL
  is run with the default parameters except for background fitting and
  subtracting added.  The text beginning with # are comments of things to
  try and do.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; artdata
  ar&gt; unlearn artdata
  ar&gt; mk1dspec apdemo1d nl=50
  ar&gt; mk2dspec apdemo2d model=STDIN
  apdemo1d 1. gauss 3 0 20 .01
  apdemo1d .8 gauss 3 0 40 .01
  apdemo1d .6 gauss 3 0 60 .01
  apdemo1d .4 gauss 3 0 80 .01
  [EOF=Control D or Control Z]
  ar&gt; mknoise apdemo2d background=100. rdnoise=3. poisson+
  ar&gt; bye
  # Display or plot the spectrum
  ap&gt; dispaxis=2; verbose=yes
  ap&gt; unlearn apall
  ap&gt; apall apdemo2d back=fit
  Searching aperture database ...
  Find apertures for apdemo2d?  (yes):
  Finding apertures ...
  Number of apertures to be found automatically (1): 4
  Jul 31 16:55: FIND - 4 apertures found for apdemo2d.
  Resize apertures for apdemo2d?  (yes):
  Resizing apertures ...
  Jul 31 16:55: RESIZE - 4 apertures resized for apdemo2d.
  Edit apertures for apdemo2d?  (yes):
  # Get a list of commands with <span style="font-family: monospace;">'?'</span>
  # See all the parameters settings with :par
  # Try deleting and marking a spectrum with <span style="font-family: monospace;">'d'</span> and <span style="font-family: monospace;">'m'</span>
  # Look at the background fitting parameters with <span style="font-family: monospace;">'b'</span> (exit with <span style="font-family: monospace;">'q'</span>)
  # Exit with <span style="font-family: monospace;">'q'</span>
  Trace apertures for apdemo2d?  (yes):
  Fit traced positions for apdemo2d interactively?  (yes):
  Tracing apertures ...
  Fit curve to aperture 1 of apdemo2d interactively  (yes):
  # You can use ICFIT commands to adjust the fit.
  Fit curve to aperture 2 of apdemo2d interactively  (yes): n
  Fit curve to aperture 3 of apdemo2d interactively  (no):
  Fit curve to aperture 4 of apdemo2d interactively  (no): y
  Jul 31 16:56: TRACE - 4 apertures traced in apdemo2d.
  Write apertures for apdemo2d to apdemosdb  (yes):
  Jul 31 16:56: DATABASE - 4 apertures for apdemo2d written to database.
  Extract aperture spectra for apdemo2d?  (yes):
  Review extracted spectra from apdemo2d?  (yes):
  Extracting apertures ...
  Review extracted spectrum for aperture 1 from apdemo2d?  (yes):
  # Type <span style="font-family: monospace;">'q'</span> to quit
  Jul 31 16:56: EXTRACT - Aperture 1 from apdemo2d --&gt; apdemo2d.ms
  Review extracted spectrum for aperture 2 from apdemo2d?  (yes): N
  Jul 31 16:56: EXTRACT - Aperture 2 from apdemo2d --&gt; apdemo2d.ms
  Jul 31 16:56: EXTRACT - Aperture 3 from apdemo2d --&gt; apdemo2d.ms
  Jul 31 16:57: EXTRACT - Aperture 4 from apdemo2d --&gt; apdemo2d.ms
  </pre></div>
  <p>
  2. To extract a series of similar spectra noninteractively using a
  reference for the aperture definitions, then recentering and resizing
  but not retracing:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; apall fib*.imh ref=flat inter- trace-
  </pre></div>
  <p>
  Note that the interactive flag automatically turns off the edit, fittrace,
  and review options and the reference image eliminates the find
  (find only occurs if there are no initial apertures).
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_APALL">
  <dt><b>APALL V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='APALL' Line='APALL V2.11' -->
  <dd>The <span style="font-family: monospace;">"apertures"</span> parameter can be used to select apertures for resizing,
  recentering, tracing, and extraction.  This parameter name was previously
  used for selecting apertures in the recentering algorithm.  The new
  parameter name for this is now <span style="font-family: monospace;">"aprecenter"</span>.
  The aperture ID table information may now be contained in the
  image header under the keywords SLFIBnnn.
  The <span style="font-family: monospace;">"nsubaps"</span> parameter now allows onedspec and echelle output formats.
  The echelle format is appropriate for treating each subaperture as
  a full echelle extraction.
  </dd>
  </dl>
  <dl id="l_APALL">
  <dt><b>APALL V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='APALL' Line='APALL V2.10.3' -->
  <dd>The dispersion axis parameter was moved to purely a package parameter.
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
  apdefault, apfind, aprecenter, apresize, apedit, aptrace, apsum
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ADDITIONAL PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

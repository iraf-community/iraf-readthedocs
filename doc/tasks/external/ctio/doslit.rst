.. _doslit:

doslit: Process CTIO slit spectra
=================================

**Package: ctio**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  doslit objects
  </p>
  </section>
  <section id="s_summary">
  <h3>Summary</h3>
  <p>
  <b>Doslit</b> extracts, sky subtracts, wavelength calibrates, and flux
  calibrates simple two dimensional slit spectra which have been processed to
  remove the detector characteristics; i.e. CCD images have been bias, dark
  count, and flat field corrected.  It is primarily intended for
  spectrophotometry or radial velocities of stellar spectra with the spectra
  aligned with one of the image axes; i.e. the assumption is that extractions
  can be done by summing along image lines or columns.  The alignment does
  not have to be precise but only close enough that the wavelength difference
  across the spectrum profiles is insignificant.  The task is available
  in the <b>ctioslit</b>, <b>kpnoslit</b>, <b>kpnocoude</b>, and <b>specred</b>
  packages.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_objects">
  <dt><b>objects</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='objects' Line='objects' -->
  <dd>List of object images to be processed.  Previously processed spectra are
  ignored unless the <i>redo</i> flag is set or the <i>update</i> flag is set
  and dependent calibration data has changed.  If the images contain the
  keyword IMAGETYP then only those with a value of <span style="font-family: monospace;">"object"</span> or <span style="font-family: monospace;">"OBJECT"</span>
  are used and those with a value of <span style="font-family: monospace;">"comp"</span> or <span style="font-family: monospace;">"COMPARISON"</span> are added
  to the list of arcs.  Extracted spectra are ignored.
  </dd>
  </dl>
  <dl id="l_arcs">
  <dt><b>arcs = <span style="font-family: monospace;">""</span> (at least one if dispersion correcting)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='arcs' Line='arcs = "" (at least one if dispersion correcting)' -->
  <dd>List of arc calibration spectra.  These spectra are used to define
  the dispersion functions.  The first spectrum is used to mark lines
  and set the dispersion function interactively and dispersion functions
  for all other arc spectra are derived from it.  If the images contain
  the keyword IMAGETYP then only those with a value of <span style="font-family: monospace;">"comp"</span> or
  <span style="font-family: monospace;">"COMPARISON"</span> are used.  All others are ignored as are extracted spectra.
  </dd>
  </dl>
  <dl id="l_arctable">
  <dt><b>arctable = <span style="font-family: monospace;">""</span> (optional) (refspectra)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='arctable' Line='arctable = "" (optional) (refspectra)' -->
  <dd>Table defining which arc spectra are to be assigned to which object
  spectra (see <b>refspectra</b>).  If not specified an assignment based
  on a header parameter, <i>sparams.sort</i>, such as the Julian date
  is made.
  </dd>
  </dl>
  <dl id="l_standards">
  <dt><b>standards = <span style="font-family: monospace;">""</span> (at least one if flux calibrating)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='standards' Line='standards = "" (at least one if flux calibrating)' -->
  <dd>List of standard star spectra.  The standard stars must have entries in
  the calibration database (package parameter <i>caldir</i>).
  </dd>
  </dl>
  <dl id="l_readnoise">
  <dt><b>readnoise = <span style="font-family: monospace;">"rdnoise"</span>, gain = <span style="font-family: monospace;">"gain"</span> (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='readnoise' Line='readnoise = "rdnoise", gain = "gain" (apsum)' -->
  <dd>Read out noise in photons and detector gain in photons per data value.
  This parameter defines the minimum noise sigma and the conversion between
  photon Poisson statistics and the data number statistics.  Image header
  keywords (case insensitive) may be specified to obtain the values from the
  image header.
  </dd>
  </dl>
  <dl id="l_datamax">
  <dt><b>datamax = INDEF (apsum.saturation)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datamax' Line='datamax = INDEF (apsum.saturation)' -->
  <dd>The maximum data value which is not a cosmic ray.
  When cleaning cosmic rays and/or using variance weighted extraction
  very strong cosmic rays (pixel values much larger than the data) can
  cause these operations to behave poorly.  If a value other than INDEF
  is specified then all data pixels in excess of this value will be
  excluded and the algorithms will yield improved results.
  This applies only to the object spectra and not the standard star or
  arc spectra.  For more
  on this see the discussion of the saturation parameter in the
  <b>apextract</b> package.
  </dd>
  </dl>
  <dl id="l_width">
  <dt><b>width = 5. (apedit)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='width' Line='width = 5. (apedit)' -->
  <dd>Approximate full width of the spectrum profiles.  This parameter is used
  to define a width and error radius for the profile centering algorithm.
  </dd>
  </dl>
  <dl id="l_crval">
  <dt><b>crval = INDEF, cdelt = INDEF (autoidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crval' Line='crval = INDEF, cdelt = INDEF (autoidentify)' -->
  <dd>These parameters specify an approximate central wavelength and dispersion.
  They may be specified as numerical values, INDEF, or image header keyword
  names whose values are to be used.
  If both these parameters are INDEF then the automatic identification will
  not be done.
  </dd>
  </dl>
  <dl id="l_dispcor">
  <dt><b>dispcor = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispcor' Line='dispcor = yes' -->
  <dd>Dispersion correct spectra?  This may involve either defining a nonlinear
  dispersion coordinate system in the image header or resampling the
  spectra to uniform linear wavelength coordinates as selected by
  the parameter <i>sparams.linearize</i>.
  </dd>
  </dl>
  <dl id="l_extcor">
  <dt><b>extcor = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extcor' Line='extcor = no' -->
  <dd>Extinction correct the spectra?
  </dd>
  </dl>
  <dl id="l_fluxcal">
  <dt><b>fluxcal = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fluxcal' Line='fluxcal = no' -->
  <dd>Flux calibrate the spectra using standard star observations?
  </dd>
  </dl>
  <dl id="l_resize">
  <dt><b>resize = no (apresize)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='resize' Line='resize = no (apresize)' -->
  <dd>Resize the default aperture for each object based on the spectrum profile?
  </dd>
  </dl>
  <dl id="l_clean">
  <dt><b>clean = no (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clean' Line='clean = no (apsum)' -->
  <dd>Detect and correct for bad pixels during extraction?  This is the same
  as the clean option in the <b>apextract</b> package.  If yes this also
  implies variance weighted extraction.  In addition the datamax parameters
  can be useful.
  </dd>
  </dl>
  <dl id="l_splot">
  <dt><b>splot = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='splot' Line='splot = no' -->
  <dd>Plot the final spectra with the task <b>splot</b>?  In quicklook mode
  this is automatic and in non-quicklook mode it is queried.
  </dd>
  </dl>
  <dl id="l_redo">
  <dt><b>redo = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='redo' Line='redo = no' -->
  <dd>Redo operations previously done?  If no then previously processed spectra
  in the object list will not be processed unless required by the
  update option.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = no' -->
  <dd>Update processing of previously processed spectra if the
  dispersion reference image or standard star calibration data are changed?
  </dd>
  </dl>
  <dl id="l_quicklook">
  <dt><b>quicklook = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='quicklook' Line='quicklook = no' -->
  <dd>Extract and calibrate spectra with minimal interaction?  In quicklook mode
  only the initial dispersion function solution and standard star setup are
  done interactively.  Normally the <i>splot</i> option is set in this mode to
  produce an automatic final spectrum plot for each object.  It is
  recommended that this mode not be used for final reductions.
  </dd>
  </dl>
  <dl id="l_batch">
  <dt><b>batch = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='batch' Line='batch = yes' -->
  <dd>Process spectra as a background or batch job provided there are no interactive
  steps remaining.
  </dd>
  </dl>
  <dl id="l_listonly">
  <dt><b>listonly = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listonly' Line='listonly = no' -->
  <dd>List processing steps but don't process?
  </dd>
  </dl>
  <dl id="l_sparams">
  <dt><b>sparams = <span style="font-family: monospace;">""</span> (pset)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sparams' Line='sparams = "" (pset)' -->
  <dd>Name of parameter set containing additional processing parameters.  This
  parameter is only for indicating the link to the parameter set
  <b>sparams</b> and should not be given a value.  The parameter set may be
  examined and modified in the usual ways (typically with <span style="font-family: monospace;">"epar sparams"</span>
  or <span style="font-family: monospace;">":e sparams"</span> from the parameter editor).  The parameters are
  described below.
  </dd>
  </dl>
  <p style="text-align:center">-- GENERAL PARAMETERS --
  
  </p>
  <dl id="l_line">
  <dt><b>line = INDEF, nsum = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='line' Line='line = INDEF, nsum = 10' -->
  <dd>The dispersion line (line or column perpendicular to the dispersion
  axis) and number of adjacent lines (half before and half after unless
  at the end of the image) used in finding, resizing,
  editing, and tracing operations.  A line of INDEF selects the middle of the
  image along the dispersion axis.
  </dd>
  </dl>
  <dl id="l_extras">
  <dt><b>extras = no (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extras' Line='extras = no (apsum)' -->
  <dd>Include raw unweighted and uncleaned spectra, the background spectra, and
  the estimated sigmas in a three dimensional output image format.
  See the discussion in the <b>apextract</b> package for further information.
  </dd>
  </dl>
  <p style="text-align:center">-- DEFAULT APERTURE LIMITS --
  
  </p>
  <dl id="l_lower">
  <dt><b>lower = -3., upper = 3. (apdefault)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lower' Line='lower = -3., upper = 3. (apdefault)' -->
  <dd>Default lower and upper aperture limits relative to the aperture center.
  These limits are used when the apertures are first defined.
  </dd>
  </dl>
  <p style="text-align:center">-- AUTOMATIC APERTURE RESIZING PARAMETERS --
  
  </p>
  <dl id="l_ylevel">
  <dt><b>ylevel = 0.05 (apresize)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ylevel' Line='ylevel = 0.05 (apresize)' -->
  <dd>Fraction of the peak to set aperture limits during automatic resizing.
  </dd>
  </dl>
  <p style="text-align:center">-- TRACE PARAMETERS --
  
  </p>
  <dl id="l_t_step">
  <dt><b>t_step = 10 (aptrace)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_step' Line='t_step = 10 (aptrace)' -->
  <dd>Step along the dispersion axis between determination of the spectrum
  positions.  Note the <i>nsum</i> parameter is also used to enhance the
  signal-to-noise at each step.
  </dd>
  </dl>
  <dl id="l_t_function">
  <dt><b>t_function = <span style="font-family: monospace;">"spline3"</span>, t_order = 1 (aptrace)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_function' Line='t_function = "spline3", t_order = 1 (aptrace)' -->
  <dd>Default trace fitting function and order.  The fitting function types are
  <span style="font-family: monospace;">"chebyshev"</span> polynomial, <span style="font-family: monospace;">"legendre"</span> polynomial, <span style="font-family: monospace;">"spline1"</span> linear spline, and
  <span style="font-family: monospace;">"spline3"</span> cubic spline.  The order refers to the number of terms in the
  polynomial functions or the number of spline pieces in the spline
  functions.
  </dd>
  </dl>
  <dl id="l_t_niterate">
  <dt><b>t_niterate = 1, t_low = 3., t_high = 3. (aptrace)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_niterate' Line='t_niterate = 1, t_low = 3., t_high = 3. (aptrace)' -->
  <dd>Default number of rejection iterations and rejection sigma thresholds.
  </dd>
  </dl>
  <p style="text-align:center">-- APERTURE EXTRACTION PARAMETERS --
  
  </p>
  <dl id="l_weights">
  <dt><b>weights = <span style="font-family: monospace;">"none"</span> (apsum) (none|variance)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='weights' Line='weights = "none" (apsum) (none|variance)' -->
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
  <dt><b>pfit = <span style="font-family: monospace;">"fit1d"</span> (apsum and approfile) (fit1d|fit2d)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pfit' Line='pfit = "fit1d" (apsum and approfile) (fit1d|fit2d)' -->
  <dd>Type of profile fitting algorithm to use.  The <span style="font-family: monospace;">"fit1d"</span> algorithm is
  preferred except in cases of extreme tilt.
  </dd>
  </dl>
  <dl id="l_lsigma">
  <dt><b>lsigma = 3., usigma = 3. (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lsigma' Line='lsigma = 3., usigma = 3. (apsum)' -->
  <dd>Lower and upper rejection thresholds, given as a number of times the
  estimated sigma of a pixel, for cleaning.
  </dd>
  </dl>
  <p style="text-align:center">-- DEFAULT BACKGROUND PARAMETERS --
  
  </p>
  <dl id="l_background">
  <dt><b>background = <span style="font-family: monospace;">"fit"</span> (apsum) (none|average|median|minimum|fit)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = "fit" (apsum) (none|average|median|minimum|fit)' -->
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
  <dl id="l_b_function">
  <dt><b>b_function = <span style="font-family: monospace;">"legendre"</span>, b_order = 1 (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_function' Line='b_function = "legendre", b_order = 1 (apsum)' -->
  <dd>Default background fitting function and order.  The fitting function types are
  <span style="font-family: monospace;">"chebyshev"</span> polynomial, <span style="font-family: monospace;">"legendre"</span> polynomial, <span style="font-family: monospace;">"spline1"</span> linear spline, and
  <span style="font-family: monospace;">"spline3"</span> cubic spline.  The order refers to the number of
  terms in the polynomial functions or the number of spline pieces in the spline
  functions.
  </dd>
  </dl>
  <dl id="l_b_sample">
  <dt><b>b_sample = <span style="font-family: monospace;">"-10:-6,6:10"</span> (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_sample' Line='b_sample = "-10:-6,6:10" (apsum)' -->
  <dd>Default background sample.  The sample is given by a set of colon separated
  ranges each separated by either whitespace or commas.  The string <span style="font-family: monospace;">"*"</span> refers
  to all points.  Note that the background coordinates are relative to the
  aperture center and not image pixel coordinates so the endpoints need not
  be integer.  It is recommended that the background regions be examined
  and set interactively with the <span style="font-family: monospace;">'b'</span> key in the interactive aperture
  definition mode.  This requires <i>quicklook</i> to be no.
  </dd>
  </dl>
  <dl id="l_b_naverage">
  <dt><b>b_naverage = -100 (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_naverage' Line='b_naverage = -100 (apsum)' -->
  <dd>Default number of points to average or median.  Positive numbers
  average that number of sequential points to form a fitting point.
  Negative numbers median that number, in absolute value, of sequential
  points.  A value of 1 does no averaging and each data point is used in the
  fit.
  </dd>
  </dl>
  <dl id="l_b_niterate">
  <dt><b>b_niterate = 1 (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_niterate' Line='b_niterate = 1 (apsum)' -->
  <dd>Default number of rejection iterations.  If greater than zero the fit is
  used to detect deviant fitting points and reject them before repeating the
  fit.  The number of iterations of this process is given by this parameter.
  </dd>
  </dl>
  <dl id="l_b_low_reject">
  <dt><b>b_low_reject = 3., b_high_reject = 3. (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_low_reject' Line='b_low_reject = 3., b_high_reject = 3. (apsum)' -->
  <dd>Default background lower and upper rejection sigmas.  If greater than zero
  points deviating from the fit below and above the fit by more than this
  number of times the sigma of the residuals are rejected before refitting.
  </dd>
  </dl>
  <p style="text-align:center">-- ARC DISPERSION FUNCTION PARAMETERS --
  
  </p>
  <dl id="l_threshold">
  <dt><b>threshold = 10. (autoidentify/identify/reidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 10. (autoidentify/identify/reidentify)' -->
  <dd>In order for a feature center to be determined the range of pixel intensities
  around the feature must exceed this threshold.
  </dd>
  </dl>
  <dl id="l_coordlist">
  <dt><b>coordlist = <span style="font-family: monospace;">"linelists$idhenear.dat"</span> (autoidentify/identify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coordlist' Line='coordlist = "linelists$idhenear.dat" (autoidentify/identify)' -->
  <dd>Arc line list consisting of an ordered list of wavelengths.
  Some standard line lists are available in the directory <span style="font-family: monospace;">"linelists$"</span>.
  </dd>
  </dl>
  <dl id="l_match">
  <dt><b>match = -3. (autoidentify/identify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='match' Line='match = -3. (autoidentify/identify)' -->
  <dd>The maximum difference for a match between the dispersion function computed
  value and a wavelength in the coordinate list.
  </dd>
  </dl>
  <dl id="l_fwidth">
  <dt><b>fwidth = 4. (autoidentify/identify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fwidth' Line='fwidth = 4. (autoidentify/identify)' -->
  <dd>Approximate full base width (in pixels) of arc lines.
  </dd>
  </dl>
  <dl id="l_cradius">
  <dt><b>cradius = 10. (reidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cradius' Line='cradius = 10. (reidentify)' -->
  <dd>Radius from previous position to reidentify arc line.
  </dd>
  </dl>
  <dl id="l_i_function">
  <dt><b>i_function = <span style="font-family: monospace;">"spline3"</span>, i_order = 1 (autoidentify/identify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='i_function' Line='i_function = "spline3", i_order = 1 (autoidentify/identify)' -->
  <dd>The default function and order to be fit to the arc wavelengths as a
  function of the pixel coordinate.  The functions choices are <span style="font-family: monospace;">"chebyshev"</span>,
  <span style="font-family: monospace;">"legendre"</span>, <span style="font-family: monospace;">"spline1"</span>, or <span style="font-family: monospace;">"spline3"</span>.
  </dd>
  </dl>
  <dl id="l_i_niterate">
  <dt><b>i_niterate = 0, i_low = 3.0, i_high = 3.0 (autoidentify/identify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='i_niterate' Line='i_niterate = 0, i_low = 3.0, i_high = 3.0 (autoidentify/identify)' -->
  <dd>Number of rejection iterations and sigma thresholds for rejecting arc
  lines from the dispersion function fits.
  </dd>
  </dl>
  <dl id="l_refit">
  <dt><b>refit = yes (reidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refit' Line='refit = yes (reidentify)' -->
  <dd>Refit the dispersion function?  If yes and there is more than 1 line
  and a dispersion function was defined in the initial arc reference then a new
  dispersion function of the same type as in the reference image is fit
  using the new pixel positions.  Otherwise only a zero point shift is
  determined for the revised fitted coordinates without changing the
  form of the dispersion function.
  </dd>
  </dl>
  <dl id="l_addfeatures">
  <dt><b>addfeatures = no (reidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='addfeatures' Line='addfeatures = no (reidentify)' -->
  <dd>Add new features from a line list during each reidentification?
  This option can be used to compensate for lost features from the
  reference solution.  Care should be exercised that misidentified features
  are not introduced.
  </dd>
  </dl>
  <p style="text-align:center">-- AUTOMATIC ARC ASSIGNMENT PARAMETERS --
  
  </p>
  <dl id="l_select">
  <dt><b>select = <span style="font-family: monospace;">"interp"</span> (refspectra)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='select' Line='select = "interp" (refspectra)' -->
  <dd>Selection method for assigning wavelength calibration spectra.
  Note that an arc assignment table may be used to override the selection
  method and explicitly assign arc spectra to object spectra.
  The automatic selection methods are:
  <dl>
  <dt><b>average</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='average' Line='average' -->
  <dd>Average two reference spectra without regard to any
  sort or group parameters.
  If only one reference spectrum is specified then it is assigned with a
  warning.  If more than two reference spectra are specified then only the
  first two are used and a warning is given.  There is no checking of the
  group values.
  </dd>
  </dl>
  <dl>
  <dt><b>following</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='following' Line='following' -->
  <dd>Select the nearest following spectrum in the reference list based on the
  sort and group parameters.  If there is no following spectrum use the
  nearest preceding spectrum.
  </dd>
  </dl>
  <dl>
  <dt><b>interp</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='interp' Line='interp' -->
  <dd>Interpolate between the preceding and following spectra in the reference
  list based on the sort and group parameters.  If there is no preceding and
  following spectrum use the nearest spectrum.  The interpolation is weighted
  by the relative distances of the sorting parameter (see cautions in
  DESCRIPTION section).
  </dd>
  </dl>
  <dl>
  <dt><b>match</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='match' Line='match' -->
  <dd>Match each input spectrum with the reference spectrum list in order.
  This overrides any group values.
  </dd>
  </dl>
  <dl>
  <dt><b>nearest</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nearest' Line='nearest' -->
  <dd>Select the nearest spectrum in the reference list based on the sort and
  group parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>preceding</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='preceding' Line='preceding' -->
  <dd>Select the nearest preceding spectrum in the reference list based on the
  sort and group parameters.  If there is no preceding spectrum use the
  nearest following spectrum.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_sort">
  <dt><b>sort = <span style="font-family: monospace;">"jd"</span> (setjd and refspectra)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sort' Line='sort = "jd" (setjd and refspectra)' -->
  <dd>Image header keyword to be used as the sorting parameter for selection
  based on order.  The header parameter must be numeric but otherwise may
  be anything.  Common sorting parameters are times or positions.
  </dd>
  </dl>
  <dl id="l_group">
  <dt><b>group = <span style="font-family: monospace;">"ljd"</span> (setjd and refspectra)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='group' Line='group = "ljd" (setjd and refspectra)' -->
  <dd>Image header keyword to be used to group spectra.  For those selection
  methods which use the group parameter the reference and object
  spectra must have identical values for this keyword.  This can
  be anything but it must be constant within a group.  Common grouping
  parameters are the date of observation <span style="font-family: monospace;">"date-obs"</span> (provided it does not
  change over a night) or the local Julian day number.
  </dd>
  </dl>
  <dl id="l_time">
  <dt><b>time = no, timewrap = 17. (refspectra)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='time' Line='time = no, timewrap = 17. (refspectra)' -->
  <dd>Is the sorting parameter a 24 hour time?  If so then the time origin
  for the sorting is specified by the timewrap parameter.  This time
  should precede the first observation and follow the last observation
  in a 24 hour cycle.
  </dd>
  </dl>
  <p style="text-align:center">-- DISPERSION  CORRECTION PARAMETERS --
  
  </p>
  <dl id="l_linearize">
  <dt><b>linearize = yes (dispcor)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linearize' Line='linearize = yes (dispcor)' -->
  <dd>Interpolate the spectra to a linear dispersion sampling?  If yes the
  spectra will be interpolated to a linear or log linear sampling using
  the linear dispersion parameters specified by other parameters.  If
  no the nonlinear dispersion function(s) from the dispersion function
  database are assigned to the input image world coordinate system
  and the spectral data is not interpolated.  Note the interpolation
  function type is set by the package parameter <i>interp</i>.
  </dd>
  </dl>
  <dl id="l_log">
  <dt><b>log = no (dispcor)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='log' Line='log = no (dispcor)' -->
  <dd>Use linear logarithmic wavelength coordinates?  Linear logarithmic
  wavelength coordinates have wavelength intervals which are constant
  in the logarithm of the wavelength.
  </dd>
  </dl>
  <dl id="l_flux">
  <dt><b>flux = yes (dispcor)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flux' Line='flux = yes (dispcor)' -->
  <dd>Conserve the total flux during interpolation?  If <i>no</i> the output
  spectrum is interpolated from the input spectrum at each output
  wavelength coordinate.  If <i>yes</i> the input spectrum is integrated
  over the extent of each output pixel.  This is slower than
  simple interpolation.
  </dd>
  </dl>
  <p style="text-align:center">-- SENSITIVITY CALIBRATION PARAMETERS --
  
  </p>
  <dl id="l_s_function">
  <dt><b>s_function = <span style="font-family: monospace;">"spline3"</span>, s_order = 1 (sensfunc)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='s_function' Line='s_function = "spline3", s_order = 1 (sensfunc)' -->
  <dd>Function and order used to fit the sensitivity data.  The function types
  are <span style="font-family: monospace;">"chebyshev"</span> polynomial, <span style="font-family: monospace;">"legendre"</span> polynomial, <span style="font-family: monospace;">"spline3"</span> cubic spline,
  and <span style="font-family: monospace;">"spline1"</span> linear spline.  Order of the sensitivity fitting function.
  The value corresponds to the number of polynomial terms or the number of
  spline pieces.  The default values may be changed interactively.
  </dd>
  </dl>
  <dl id="l_fnu">
  <dt><b>fnu = no (calibrate)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fnu' Line='fnu = no (calibrate)' -->
  <dd>The default calibration is into units of F-lambda. If <i>fnu</i> = yes then
  the calibrated spectrum will be in units of F-nu.
  </dd>
  </dl>
  <p style="text-align:center">PACKAGE PARAMETERS
  
  </p>
  <p>
  The following package parameters are used by this task.  The default values
  may vary depending on the package.
  </p>
  <dl id="l_dispaxis">
  <dt><b>dispaxis = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispaxis' Line='dispaxis = 2' -->
  <dd>Default dispersion axis.  The dispersion axis is 1 for dispersion
  running along image lines and 2 for dispersion running along image
  columns.  If the image header parameter DISPAXIS is defined it has
  precedence over this parameter.  The default value defers to the
  package parameter of the same name.
  </dd>
  </dl>
  <dl id="l_extinction">
  <dt><b>extinction (standard, sensfunc, calibrate)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extinction' Line='extinction (standard, sensfunc, calibrate)' -->
  <dd>Extinction file for a site.  There are two extinction files in the
  NOAO standards library, onedstds$, for KPNO and CTIO.  These extinction
  files are used for extinction and flux calibration.
  </dd>
  </dl>
  <dl id="l_caldir">
  <dt><b>caldir (standard)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='caldir' Line='caldir (standard)' -->
  <dd>Standard star calibration directory.  A directory containing standard
  star data files.  Note that the directory name must end with <span style="font-family: monospace;">'/'</span>.
  There are a number of standard star calibrations directories in the NOAO
  standards library, onedstds$.
  </dd>
  </dl>
  <dl id="l_observatory">
  <dt><b>observatory = <span style="font-family: monospace;">"observatory"</span> (observatory)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observatory' Line='observatory = "observatory" (observatory)' -->
  <dd>The default observatory to use for latitude dependent computations.
  If the OBSERVAT keyword in the image header it takes precedence over
  this parameter.
  </dd>
  </dl>
  <dl id="l_interp">
  <dt><b>interp = <span style="font-family: monospace;">"poly5"</span> (nearest|linear|poly3|poly5|spline3|sinc) (dispcor)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interp' Line='interp = "poly5" (nearest|linear|poly3|poly5|spline3|sinc) (dispcor)' -->
  <dd>Spectrum interpolation type used when spectra are resampled.  The choices are:
  <div class="highlight-default-notranslate"><pre>
  nearest - nearest neighbor
   linear - linear
    poly3 - 3rd order polynomial
    poly5 - 5th order polynomial
  spline3 - cubic spline
     sinc - sinc function
  </pre></div>
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"database"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "database"' -->
  <dd>Database name used by various tasks.  This is a directory which is created
  if necessary.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Verbose output?  If set then almost all the information written to the
  logfile is also written to the terminal except when the task is a
  background or batch process.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "logfile"' -->
  <dd>If specified detailed text log information is written to this file.
  </dd>
  </dl>
  <dl id="l_plotfile">
  <dt><b>plotfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotfile' Line='plotfile = ""' -->
  <dd>If specified metacode plots are recorded in this file for later review.
  Since plot information can become large this should be used only if
  really desired.
  </dd>
  </dl>
  </section>
  <section id="s_environment_parameters">
  <h3>Environment parameters</h3>
  <p>
  The environment parameter <i>imtype</i> is used to determine the extension
  of the images to be processed and created.  This allows use with any
  supported image extension.  For STF images the extension has to be exact;
  for example <span style="font-family: monospace;">"d1h"</span>.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Doslit</b> extracts, sky subtracts, wavelength calibrates, and flux
  calibrates simple two dimensional slit spectra which have been processed to
  remove the detector characteristics; i.e. CCD images have been bias, dark
  count, and flat field corrected.  It is primarily intended for
  spectrophotometry or radial velocities of stellar spectra with the spectra
  aligned with one of the image axes; i.e. the assumption is that extractions
  can be done by summing along image lines or columns.  The alignment does
  not have to be precise but only close enough that the wavelength difference
  across the spectrum profiles is insignificant.  Extended objects requiring
  accurate geometric alignment over many pixels are reduced using the
  <b>longslit</b> package.
  </p>
  <p>
  The task is a command language script which collects and combines the
  functions and parameters of many general purpose tasks to provide a single,
  complete data reduction path and a degree of guidance, automation, and
  record keeping.  In the following description and in the parameter section
  the various general tasks used are identified.  Further
  information about those tasks and their parameters may be found in their
  documentation.  <b>Doslit</b> also simplifies and consolidates parameters
  from those tasks and keeps track of previous processing to avoid
  duplications.
  </p>
  <p>
  The general organization of the task is to do the interactive setup steps,
  such as the reference dispersion function
  determination, first using representative calibration data and then perform
  the majority of the reductions automatically, possibly as a background
  process, with reference to the setup data.  In addition, the task
  determines which setup and processing operations have been completed in
  previous executions of the task and, contingent on the <i>redo</i> and
  <i>update</i> options, skip or repeat some or all the steps.
  </p>
  <p>
  The description is divided into a quick usage outline followed by details
  of the parameters and algorithms.  The usage outline is provided as a
  checklist and a refresher for those familiar with this task and the
  component tasks.  It presents only the default or recommended usage
  since there are many variations possible.
  </p>
  <p>
  <b>Usage Outline</b>
  </p>
  <dl>
  <dt><b>[1]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[1]' -->
  <dd>The images are first processed with <b>ccdproc</b> for overscan,
  zero level, dark count, and flat field corrections.
  </dd>
  </dl>
  <dl>
  <dt><b>[2]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[2]' -->
  <dd>Set the <b>doslit</b> parameters with <b>eparam</b>.  Specify the object
  images to be processed,
  one or more arc images, and one or more standard
  star images.  If there are many object, arc, or standard star images
  you might prepare <span style="font-family: monospace;">"@ files"</span>.  Set the detector and data
  specific parameters.  Select the processing options desired.
  Finally you might wish to review the <i>sparams</i> algorithm parameters
  though the defaults are probably adequate.
  </dd>
  </dl>
  <dl>
  <dt><b>[3]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[3]' -->
  <dd>Run the task.  This may be repeated multiple times with different
  observations and the task will generally only do the setup steps
  once and only process new images.  Queries presented during the
  execution for various interactive operations may be answered with
  <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"YES"</span>, or <span style="font-family: monospace;">"NO"</span>.  The lower case responses apply just
  to that query while the upper case responses apply to all further
  such queries during the current execution and no further queries of that
  type will be made.
  </dd>
  </dl>
  <dl>
  <dt><b>[4]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[4]' -->
  <dd>Apertures are defined for all the standard and object images.  This is only
  done if there are no previous aperture definitions for the image.
  The highest peak is found and centered and the default aperture limits
  are set.  If the resize option is set the aperture is resized by finding
  the level which  is 5% (the default) of the peak above local background.
  If not using the quicklook option you now have the option
  of entering the aperture editing loop to check the aperture position,
  size, and background fitting parameters, and possibly add additional
  apertures.  This is step is highly recommended.
  It is important to check the background regions with the <span style="font-family: monospace;">'b'</span>
  key.  To exit the background mode and then
  to exit the review mode use <span style="font-family: monospace;">'q'</span>.
  The spectrum positions at a series of points along the dispersion are
  measured and a function is fit to these positions.  If not using the
  quicklook option the traced positions may be examined interactively and the
  fitting parameters adjusted.  To exit the interactive fitting type <span style="font-family: monospace;">'q'</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>[5]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[5]' -->
  <dd>If dispersion correction is selected the first arc in the arc list is
  extracted.  The dispersion function is defined using the task
  <b>autoidentify</b>.  The <i>crval</i> and <i>cdelt</i> parameters are used in
  the automatic identification.  Whether or not the automatic identification
  is successful you will be shown the result of the arc line identification.
  If the automatic identification is not successful identify a few arc lines
  with with <span style="font-family: monospace;">'m'</span> and use the <span style="font-family: monospace;">'l'</span> line list identification command to
  automatically add additional lines and fit the dispersion function.  Check
  the quality of the dispersion function fit with <span style="font-family: monospace;">'f'</span>.  When satisfied exit
  with <span style="font-family: monospace;">'q'</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>[6]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[6]' -->
  <dd>If the flux calibration option is selected the standard star spectra are
  processed (if not done previously).  The images are
  extracted and wavelength calibrated.  The appropriate arc
  calibration spectra are extracted and the dispersion function refit
  using the arc reference spectrum as a starting point.  The standard star
  fluxes through the calibration bandpasses are compiled.  You are queried
  for the name of the standard star calibration data file.
  After all the standard stars are processed a sensitivity function is
  determined using the interactive task <b>sensfunc</b>.  Finally, the
  standard star spectra are extinction corrected and flux calibrated
  using the derived sensitivity function.
  </dd>
  </dl>
  <dl>
  <dt><b>[7]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[7]' -->
  <dd>The object spectra are now automatically
  extracted, wavelength calibrated, and flux calibrated.
  </dd>
  </dl>
  <dl>
  <dt><b>[8]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[8]' -->
  <dd>The option to examine the final spectra with <b>splot</b> may be given.
  To exit type <span style="font-family: monospace;">'q'</span>.  In quicklook mode the spectra are plotted
  noninteractively with <b>bplot</b>.
  </dd>
  </dl>
  <dl>
  <dt><b>[9]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[9]' -->
  <dd>The final spectra will have the same name as the original 2D images
  with a <span style="font-family: monospace;">".ms"</span> extension added.
  </dd>
  </dl>
  <p>
  <b>Spectra and Data Files</b>
  </p>
  <p>
  The basic input consists of two dimensional slit object, standard star, and
  arc calibration spectra stored as IRAF images.
  The type of image format is defined by the
  environment parameter <i>imtype</i>.  Only images with that extension will
  be processed and created.
  The raw CCD images must be
  processed to remove overscan, bias, dark count, and flat field effects.
  This is generally done using the <b>ccdred</b> package.  Lines of constant
  wavelength should be closely aligned with one of the image axes though a
  small amount of misalignment only causes a small loss of resolution.  For
  large misalignments one may use the <b>rotate</b> task.  More complex
  geometric problems and observations of extended objects should be handled
  by the <b>longslit</b> package.
  </p>
  <p>
  The arc
  spectra are comparison arc lamp observations (they must all be of the same
  type).  The assignment of arc calibration exposures to object exposures is
  generally done by selecting the nearest in time and interpolating.
  However, the optional <i>arc assignment table</i> may be used to explicitly
  assign arc images to specific objects.  The format of this file is
  described in task <b>refspectra</b>.
  </p>
  <p>
  The final reduced spectra are recorded in one, two or three dimensional IRAF
  images.  The images have the same name as the original images with an added
  <span style="font-family: monospace;">".ms"</span> extension.  Each line in the reduced image is a one dimensional
  spectrum with associated aperture, wavelength, and identification
  information.  With a single aperture the image will be one dimensional
  and with multiple apertures the image will be two dimensional.
  When the <i>extras</i> parameter is set the images will be three
  dimensional (regardless of the number of apertures) and the lines in the
  third dimension contain additional information (see
  <b>apsum</b> for further details).  These spectral formats are accepted by the
  one dimensional spectroscopy tasks such as the plotting tasks <b>splot</b>
  and <b>specplot</b>.
  </p>
  <p>
  <b>Package Parameters</b>
  </p>
  <p>
  The package parameters set parameters which change
  infrequently and set the standard I/O functions.  The extinction file
  is used for making extinction corrections and the standard star
  calibration directory is used for determining flux calibrations from
  standard star observations.  The calibration directories contain data files
  with standard star fluxes and band passes.  The available extinction
  files and flux calibration directories may be listed using the command:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help onedstds
  </pre></div>
  <p>
  The extinction correction requires computation of an air mass using the
  task <b>setairmass</b>.  The air mass computation needs information
  about the observation and, in particular, the latitude of the observatory.
  This is determined using the OBSERVAT image header keyword.  If this
  keyword is not present the observatory parameter is used.  See the
  task <b>observatory</b> for more on defining the observatory parameters.
  </p>
  <p>
  The spectrum interpolation type is used whenever a spectrum needs to be
  resampled for linearization or performing operations between spectra
  with different sampling.  The <span style="font-family: monospace;">"sinc"</span> interpolation may be of interest
  as an alternative but see the cautions given in <b>onedspec.package</b>.
  </p>
  <p>
  The general direction in which the spectra run is specified by the
  dispersion axis parameter.  Recall that ideally it is the direction
  of constant wavelength which should be aligned with an image axis and
  the dispersion direction may not be exactly aligned because atmospheric
  dispersion.
  </p>
  <p>
  The verbose parameter selects whether to print everything which goes
  into the log file on the terminal.  It is useful for monitoring
  what the <b>doslit</b> task does.  The log and plot files are useful for
  keeping a record of the processing.  A log file is highly recommended.
  A plot file provides a record of the apertures, traces, and extracted
  spectra but can become quite large.
  The plotfile is most conveniently viewed and printed with <b>gkimosaic</b>.
  </p>
  <p>
  <b>Processing Parameters</b>
  </p>
  <p>
  The input images are specified by image lists.  The lists may be
  a list of explicit comma separate image names, @ files, or image
  templates using pattern matching against file names in the directory.
  To allow wildcard image lists to be used safely and conveniently the
  image lists are checked to remove extracted images (the .ms images)
  and to automatically identify object and arc spectra.  Object and arc
  images are identified by the keyword IMAGETYP with values of <span style="font-family: monospace;">"object"</span>,
  <span style="font-family: monospace;">"OBJECT"</span>, <span style="font-family: monospace;">"comp"</span>, or <span style="font-family: monospace;">"COMPARISON"</span> (the current practice at NOAO).
  If arc images are found in the object list they are transferred to the
  arc list while if object images are found in the arc list they are ignored.
  All other image types, such as biases, darks, or flat fields, are
  ignored.  This behavior allows simply specifying all images with a wildcard
  in the object list with automatic selections of arc spectra or a
  wildcard in the arc list to automatically find the arc spectra.
  If the data lack the identifying information it is up to the user
  to explicitly set the proper lists.
  </p>
  <p>
  The arc assignment table is a file which may be used to assign
  specific arc spectra to specific object and standard star spectra.
  For more on this option see <b>refspectra</b>.
  </p>
  <p>
  The next set of parameters describe the noise characteristics and
  spectrum characteristics.  The read out noise and gain are used when
  <span style="font-family: monospace;">"cleaning"</span> cosmic rays and when using variance or optimal weighting.  These
  parameters must be fairly accurate.  Note that these are the effective
  parameters and must be adjusted if previous processing has modified the
  pixel values; such as with an unnormalized flat field.
  The variance
  weighting and cosmic-ray cleanning are sensitive to extremely strong
  cosmic-rays; ones which are hundreds of times brighter than the
  spectrum.  The <i>datamax</i> is used to set an upper limit for any
  real data.  Any pixels above this value will be flagged as cosmic-rays
  and will not affect the extractions.
  </p>
  <p>
  The profile width should be approximately the full width
  at the profile base.  This parameter is used for centering and tracing
  of the spectrum profiles.
  </p>
  <p>
  The approximate central wavelength and dispersion are used for the
  automatic identification of the arc reference.  They may be specified
  as image header keywords or values.  The INDEF values search the
  entire range of the coordinate reference file but the automatic
  line identification algorithm works much better and faster if
  approximate values are given.
  </p>
  <p>
  The next set of parameters select the processing steps and options.  The
  various calibration steps may be done simultaneously, that is at the same
  time as the basic extractions, or in separate executions of the task.
  Typically, all the desired operations are done at the same time.
  Dispersion correction requires at least one arc spectrum and flux
  calibration requires dispersion correction and at least one standard star
  observation.
  </p>
  <p>
  The <i>resize</i> option resets the edges of the extraction aperture based
  on the profile for each object and standard star image.  The default
  resizing is to the 5% point relative to the peak measured above the
  background.  This allows following changes in the seeing.  However, one
  should consider the consequences of this if attempting to flux calibrate
  the observations.  Except in quicklook mode, the apertures for each object
  and standard star observation may be reviewed graphically and
  adjustments made to the aperture width and background regions.
  </p>
  <p>
  The <i>clean</i> option invokes a profile
  fitting and deviant point rejection algorithm as well as a variance weighting
  of points in the aperture.  See the next section for more about
  requirements to use this option.
  </p>
  <p>
  Generally once a spectrum has been processed it will not be reprocessed if
  specified as an input spectrum.  However, changes to the underlying
  calibration data can cause such spectra to be reprocessed if the
  <i>update</i> flag is set.  The changes which will cause an update are a
  new arc reference image and new standard stars.  If all input spectra are to be
  processed regardless of previous processing the <i>redo</i> flag may be
  used.  Note that reprocessing clobbers the previously processed output
  spectra.
  </p>
  <p>
  The final step is to plot the spectra if the <i>splot</i> option is
  selected.  In non-quicklook mode there is a query which may be
  answered either in lower or upper case.  The plotting uses the interactive
  task <b>splot</b>.  In quicklook mode the plot appears noninteractively
  using the task <b>bplot</b>.  
  </p>
  <p>
  The <i>quicklook</i> option provides a simpler, less interactive, mode.
  In quicklook mode a single aperture is defined using default parameters
  without interactive aperture review or trace fitting and
  the <i>splot</i> option selects a noninteractive plot to be
  shown at the end of processing of each object and standard star
  spectrum.  While the algorithms used in quicklook mode are nearly the same
  as in non-quicklook mode and the final results may be the same it is
  recommended that the greater degree of monitoring and review in
  non-quicklook mode be used for careful final reductions.
  </p>
  <p>
  The batch processing option allows object spectra to be processed as a
  background or batch job.  This will occur only if the interactive
  <i>splot</i> option is not active; either not set, turned off during
  processing with <span style="font-family: monospace;">"NO"</span>, or in quicklook mode.  In batch processing the
  terminal output is suppressed.
  </p>
  <p>
  The <i>listonly</i> option prints a summary of the processing steps
  which will be performed on the input spectra without actually doing
  anything.  This is useful for verifying which spectra will be affected
  if the input list contains previously processed spectra.  The listing
  does not include any arc spectra which may be extracted to dispersion
  calibrate an object spectrum.
  </p>
  <p>
  The last parameter (excluding the task mode parameter) points to
  another parameter set for the algorithm parameters.  The default
  parameter set is called <i>sparams</i>.  The algorithm parameters are
  discussed further in the next section.
  </p>
  <p>
  <b>Algorithms and Algorithm Parameters</b>
  </p>
  <p>
  This section summarizes the various algorithms used by the
  <b>doslit</b> task and the parameters which control and modify the
  algorithms.  The algorithm parameters available to you are
  collected in the parameter set <b>sparams</b>.  These parameters are
  taken from the various general purpose tasks used by the <b>doslit</b>
  processing task.  Additional information about these parameters and
  algorithms may be found in the help for the actual
  task executed.  These tasks are identified below.  The aim of this
  parameter set organization is to collect all the algorithm parameters
  in one place separate from the processing parameters and include only
  those which are relevant for slit data.  The parameter values
  can be changed from the defaults by using the parameter editor,
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epar sparams
  </pre></div>
  <p>
  or simple typing <i>sparams</i>.
  The parameter editor can also be entered when editing the <b>doslit</b>
  parameters by typing <i>:e</i> when positioned at the <i>sparams</i>
  parameter.
  </p>
  <p>
  <b>Aperture Definitions</b>
  </p>
  <p>
  The first operation is to define the extraction apertures, which include the
  aperture width, background regions, and position dependence with
  wavelength, for the input slit spectra and, if flux calibration is
  selected, the standard star spectra.  This is done only for spectra which
  do not have previously defined apertures unless the <i>redo</i> option is
  set to force all definitions to be redone.  Thus, apertures may be
  defined separately using the <b>apextract</b> tasks.  This is particularly
  useful if one needs to use reference images to define apertures for very
  weak spectra which are not well centered or traced by themselves.
  </p>
  <p>
  Initially a single spectrum is found and a default aperture defined
  automatically.  If the <i>resize</i> parameter is set the aperture width is
  adjusted to a specified point on the spectrum profile (see
  <b>apresize</b>).  If not in <span style="font-family: monospace;">"quicklook"</span> mode (set by the <i>quicklook</i>
  parameter) a query is printed to select whether to inspect and modify the
  aperture and background aperture definitions using the commands described
  for <b>apedit</b>.  This option allows adding
  apertures for other objects on the slit and adjusting
  background regions to avoid contaminating objects.  The query may be
  answered in lower case for a single spectrum or in upper case to
  permanently set the response for the duration of the task execution.  This
  convention for query responses is used throughout the task.  It is
  recommended that quicklook only be used for initial quick extractions and
  calibration and that for final reductions one at least review the aperture
  definitions and traces.
  </p>
  <p>
  The initial spectrum finding and aperture definitions are done at a specified
  line or column.  The positions of the spectrum at a set of other lines or
  columns is done next and a smooth function is fit to define the aperture
  centers at all points in the image.  In non-quicklook mode the user has the
  option to review and adjust the function fitting parameters and delete bad
  position determinations.  As with the initial aperture review there is a
  query which may be answered either in lower or upper case.
  </p>
  <p>
  The above steps are all performed using tasks from the <b>apextract</b>
  package and parameters from the <b>sparams</b> parameters.  As a quick
  summary, the dispersion direction of the spectra are determined from the
  package <b>dispaxis</b> parameter if not defined in the image header.  The default
  line or column for finding the object position on the slit and the number
  of image lines or columns to sum are set by the <i>line</i> and <i>nsum</i>
  parameters.  A line of INDEF (the default) selects the middle of the image.
  The automatic finding algorithm is described for the task
  <b>apfind</b> and is basically finds the strongest peak.  The default
  aperture size, background parameters, and resizing are described in
  the tasks <b>apdefault</b> and <b>apresize</b> and the
  parameters used are also described there.
  The tracing is done as described in <b>aptrace</b> and consists of
  stepping along the image using the specified <i>t_step</i> parameter.  The
  function fitting uses the <b>icfit</b> commands with the other parameters
  from the tracing section.
  </p>
  <p>
  <b>Extraction</b>
  </p>
  <p>
  The actual extraction of the spectra is done by summing across the
  fixed width apertures at each point along the dispersion.
  The default is to simply sum the pixels using
  partial pixels at the ends.  There is an option to weight the
  sum based on a Poisson variance model using the <i>readnoise</i> and
  <i>gain</i> detector parameters.  Note that if the <i>clean</i>
  option is selected the variance weighted extraction is used regardless
  of the <i>weights</i> parameter.  The sigma thresholds for cleaning
  are also set in the <b>sparams</b> parameters.
  </p>
  <p>
  The cleaning and variance weighting options require knowing the effective
  (i.e. accounting for any image combining) read out noise and gain.  These
  numbers need to be adjusted if the image has been processed such that the
  intensity scale has a different origin (such as applying a separate
  background subtraction operation) or scaling (such as caused by
  unnormalized flat fielding).  These options also require using background
  subtraction if the profile does not go to zero.  For optimal extraction and
  cleaning to work it is recommended that any flat fielding be done using
  normalized flat fields (as is done in <b>ccdproc</b>) and using background
  subtraction if there is any appreciable sky.  For further discussion of
  cleaning and variance weighted extraction see <b>apvariance</b> and
  <b>approfiles</b> as well as  <b>apsum</b>.
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
  <b>Dispersion Correction</b>
  </p>
  <p>
  If dispersion correction is not selected, <i>dispcor</i>=no, then the object
  spectra are simply extracted.  The extracted spectra may be plotted
  by setting the <i>splot</i> option.  This produces a query and uses
  the interactive <b>splot</b> task in non-quicklook mode and uses the
  noninteractive <b>bplot</b> task in quicklook mode.
  </p>
  <p>
  Dispersion corrections are applied to the extracted spectra if the
  <i>dispcor</i> processing parameter is set.  There are three basic steps
  involved; determining the dispersion functions relating pixel position to
  wavelength, assigning the appropriate dispersion function to a particular
  observation, and either storing the nonlinear dispersion function in the
  image headers or resampling the spectra to evenly spaced pixels in
  wavelength.
  </p>
  <p>
  The first arc spectrum in the arc list is used to define the reference
  dispersion solution.  It is extracted at middle of the image with no
  tracing.  Note extractions of arc spectra are not background subtracted.
  The task <b>autoidentify</b> is attempts to define the dispersion function
  automatically using the <i>crval</i> and <i>cdelt</i> parameters.  Whether or
  not it is successful the user is presented with the interactive
  identification graph.  The automatic identifications can be reviewed and a
  new solution or corrections to the automatic solution may be performed.
  </p>
  <p>
  The arc dispersion function parameters are for <b>autoidentify</b> and it's
  related partner <b>reidentify</b>.  The parameters define a line list for
  use in automatically assigning wavelengths to arc lines, a centering width
  (which should match the line widths at the base of the lines), the
  dispersion function type and orders, parameters to exclude bad lines from
  function fits, and defining whether to refit the dispersion function as
  opposed to simply determining a zero point shift.  The defaults should
  generally be adequate and the dispersion function fitting parameters may be
  altered interactively.  One should consult the help for the two tasks for
  additional details of these parameters and the interactive operation of
  <b>autoidentify</b>.
  </p>
  <p>
  The extracted reference arc spectrum is then dispersion corrected.
  If the spectra are to be linearized, as set by the <i>linearize</i>
  parameter, the default linear wavelength parameters are printed and
  you have the option to adjust them.  The dispersion system defined at
  this point will be applied automatically to all other spectra as they
  are dispersion corrected.
  </p>
  <p>
  Once the reference dispersion function is defined other arc spectra are
  extracted as required by the object spectra.  The assignment of arcs is
  done either explicitly with an arc assignment table (parameter
  <i>arctable</i>) or based on a header parameter such as a time.
  This assignments are made by the task
  <b>refspectra</b>.  When two arcs are assigned to an object spectrum an
  interpolation is done between the two dispersion functions.  This makes an
  approximate correction for steady drifts in the dispersion.
  </p>
  <p>
  The tasks <b>setjd</b> and <b>setairmass</b> are automatically run on all
  spectra.  This computes and adds the header parameters for the Julian date
  (JD), the local Julian day number (LJD), the universal time (UTMIDDLE), and
  the air mass at the middle of the exposure.  The default arc assignment is
  to use the Julian date grouped by the local Julian day number.  The
  grouping allows multiple nights of data to be correctly assigned at the
  same time.
  </p>
  <p>
  The assigned arc spectra are then extracted using the object aperture
  definitions (but without background subtraction or cleaning) so that the
  same pixels on the detector are used.  The extracted arc spectra are then
  reidentified automatically against the reference arc spectrum.  Some
  statistics of the reidentification are printed (if not in batch mode) and
  the user has the option of examining the lines and fits interactively if
  not in quicklook mode.  The task which does the reidentification is called
  <b>reidentify</b>.
  </p>
  <p>
  The last step of dispersion correction is setting the dispersion
  of the object image from the arc images.  There are two choices here.
  If the <i>linearize</i> parameter is not set the nonlinear dispersion
  function is stored in the image header.  Other IRAF tasks interpret
  this information when dispersion coordinates are needed for plotting
  or analysis.  This has the advantage of not requiring the spectra
  to be interpolated and the disadvantage that the dispersion
  information is only understood by IRAF tasks and cannot be readily
  exported to other analysis software.
  </p>
  <p>
  If the <i>linearize</i> parameter is set then the spectra are resampled to a
  linear dispersion relation either in wavelength or the log of the
  wavelength using the dispersion coordinate system defined previously
  for the arc reference spectrum.
  </p>
  <p>
  The linearization algorithm parameters allow selecting the interpolation
  function type, whether to conserve flux per pixel by integrating across the
  extent of the final pixel, and whether to linearize to equal linear or
  logarithmic intervals.  The latter may be appropriate for radial velocity
  studies.  The default is to use a fifth order polynomial for interpolation,
  to conserve flux, and to not use logarithmic wavelength bins.  These
  parameters are described fully in the help for the task <b>dispcor</b> which
  performs the correction.
  </p>
  <p>
  <b>Flux Calibration</b>
  </p>
  <p>
  Flux calibration consists of an extinction correction and an instrumental
  sensitivity calibration.  The extinction correction only depends on the
  extinction function defined by the package parameter <i>extinct</i> and
  determination of the airmass from the header parameters (the air mass is
  computed by <b>setairmass</b> as mentioned earlier).  The sensitivity
  calibration depends on a sensitivity calibration spectrum determined from
  standard star observations for which there are tabulated absolute fluxes.
  The task that applies both the extinction correction and sensitivity
  calibration to each extracted object spectrum is <b>calibrate</b>.  Consult
  the manual page for this task for more information.
  </p>
  <p>
  Generation of the sensitivity calibration spectrum is done before
  processing any object spectra since it has two interactive steps and
  requires all the standard star observations.  The first step is tabulating
  the observed fluxes over the same bandpasses as the calibrated absolute
  fluxes.  The standard star tabulations are done after each standard star is
  extracted and dispersion corrected.  You are asked for the name of the
  standard star as tabulated in the absolute flux data files in the directory
  <i>caldir</i> defined by the package parameters.
  The tabulation of the standard star
  observations over the standard bandpasses is done by the task
  <b>standard</b>.  The tabulated data is stored in the file <i>std</i>.  Note
  that if the <i>redo</i> flag is not set any new standard stars specified in
  subsequent executions of <b>doslit</b> are added to the previous data in
  the data file, otherwise the file is first deleted.  Modification of the
  tabulated standard star data, such as by adding new stars, will cause any
  spectra in the input list which have been previously calibrated to be
  reprocessed if the <i>update</i> flag is set.
  </p>
  <p>
  After the standard star calibration bandpass fluxes are tabulated the
  information from all the standard stars is combined to produce a
  sensitivity function for use by <b>calibrate</b>.  The sensitivity function
  determination is interactive and uses the task <b>sensfunc</b>.  This task
  allows fitting a smooth sensitivity function to the ratio of the observed
  to calibrated fluxes verses wavelength.  The types of manipulations one
  needs to do include deleting bad observations, possibly removing variable
  extinction (for poor data), and possibly deriving a revised extinction
  function.  This is a complex operation and one should consult the manual
  page for <b>sensfunc</b>.  The sensitivity function is saved as a one
  dimensional spectrum with the name <i>sens</i>.  Deletion of this image
  will also cause reprocessing to occur if the <i>update</i> flag is set.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  The following example uses artificial data and may be executed
  at the terminal (with IRAF V2.10).  This is similar to the sequence
  performed by the test procedure <span style="font-family: monospace;">"demos doslit"</span>.  The output is with
  the verbose package parameter set.  Normally users use <b>eparam</b>
  rather than the long command line.  All parameters not shown
  for <b>sparams</b> and <b>doslit</b> are the default.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; demos mkdoslit
  Creating example longslit in image demoarc1 ...
  Creating example longslit in image demoobj1 ...
  Creating example longslit in image demostd1 ...
  Creating example longslit in image demoarc2 ...
  cl&gt; doslit demoobj1 arcs=demoarc1,demoarc2 stand=demostd1 \
  &gt;&gt;&gt; extcor=yes, fluxcal=yes resize=yes
  Searching aperture database ...
  Finding apertures ...
  Jan 17 15:52: FIND - 1 apertures found for demoobj1
  Resizing apertures ...
  Jan 17 15:52: APRESIZE  - 1 apertures resized for demoobj1 (-3.50, 3.49)
  Edit apertures for demostd1?  (yes):
  &lt;Check aperture and background definitions (<span style="font-family: monospace;">'b'</span>).  Exit with <span style="font-family: monospace;">'q'</span>&gt;
  Fit traced positions for demostd1 interactively?  (yes):
  Tracing apertures ...
  Fit curve to aperture 1 of demostd1 interactively  (yes):
  &lt;Exit with <span style="font-family: monospace;">'q'</span>&gt;
  Searching aperture database ...
  Finding apertures ...
  Jan 17 15:54: FIND - 1 apertures found for demostd1
  Resizing apertures ...
  Jan 17 15:54: APRESIZE  - 1 apertures resized for demostd1 (-3.35, 3.79)
  Edit apertures for demostd1?  (yes):
  &lt;Exit with <span style="font-family: monospace;">'q'</span>&gt;
  Fit traced positions for demostd1 interactively?  (yes): n
  Tracing apertures ...
  Jan 17 15:55: TRACE - 1 apertures traced in demostd1.
  Jan 17 15:55: DATABASE - 1 apertures for demostd1 written to database
  Extract arc reference image demoarc1
  Searching aperture database ...
  Finding apertures ...
  Jan 17 15:55: FIND - 1 apertures found for demoarc1
  Jan 17 15:55: DATABASE - 1 apertures for demoarc1 written to database
  Extracting apertures ...
  Jan 17 15:55: EXTRACT - Aperture 1 from demoarc1 --&gt; demoarc1.ms
  Determine dispersion solution for demoarc1
  &lt;A dispersion function is automatically determined.&gt;
  &lt;Type <span style="font-family: monospace;">'f'</span> to see the fit residuals&gt;
  &lt;Type <span style="font-family: monospace;">'d'</span> to delete the two deviant lines&gt;
  &lt;Type <span style="font-family: monospace;">'f'</span> to refit with the bad points deleted&gt;
  &lt;Type <span style="font-family: monospace;">'q'</span> to quit fit and then <span style="font-family: monospace;">'q'</span> to exit&gt;
  demoarc1.ms.imh: w1 = 4204.18..., w2 = 7355.37..., dw = 6.16..., nw = 512
    Change wavelength coordinate assignments? (yes|no|NO) (no): n
  Extract standard star spectrum demostd1
  Searching aperture database ...
  Jan 17 15:59: DATABASE  - 1 apertures read for demostd1 from database
  Extracting apertures ...
  Jan 17 15:59: EXTRACT - Aperture 1 from demostd1 --&gt; demostd1.ms
  Assign arc spectra for demostd1
  [demostd1] refspec1='demoarc1 0.403'
  [demostd1] refspec2='demoarc2 0.597'
  Extract and reidentify arc spectrum demoarc1
  Searching aperture database ...
  Jan 17 15:59: DATABASE  - 1 apertures read for demostd1 from database
  Jan 17 15:59: DATABASE - 1 apertures for demoarc1 written to database
  Extracting apertures ...
  Jan 17 15:59: EXTRACT - Aperture 1 from demoarc1 --&gt; demostd1demoarc1.ms
  
  REIDENTIFY: NOAO/IRAF V2.10BETA valdes@puppis Fri 15:59:21 17-Jan-92
    Reference image = demoarc1.ms, New image = demostd1..., Refit = yes
  Image Data    Found     Fit Pix Shift  User Shift  Z Shift      RMS
  demo...       48/48   48/48    2.22E-4     0.00184  5.09E-7    0.225
  Fit dispersion function interactively? (no|yes|NO|YES) (yes):
  demoarc1.ms: w1 = 4211.81, w2 = 7353.58, dw = 6.148, nw = 512, log = no
    Change wavelength coordinate assignments? (yes|no|NO): N
  demo... 48/48   48/48    2.22E-4     0.00184  5.09E-7    0.225
  Extract and reidentify arc spectrum demoarc2
  Searching aperture database ...
  Jan 17 16:01: DATABASE  - 1 apertures read for demostd1 from database
  Jan 17 16:01: DATABASE - 1 apertures for demoarc2 written to database
  Extracting apertures ...
  Jan 17 16:01: EXTRACT - Aperture 1 from demoarc2 --&gt; demostd1demoarc2.ms
  
  REIDENTIFY: NOAO/IRAF V2.10BETA valdes@puppis Fri 16:01:54 17-Jan-92
    Reference image = demoarc1.ms, New image = demostd1..., Refit = yes
  Image Data    Found     Fit Pix Shift  User Shift  Z Shift      RMS
  demo...       48/48   48/48    0.00302      0.0191  3.82E-6    0.244
  Dispersion correct demostd1
  demostd1.ms: ap = 1, w1 = 4204.181, w2 = 7355.375, dw = 6.16..., nw = 512
  Compile standard star fluxes for demostd1
  Star name in calibration list: hz2 &lt;in kpnoslit package&gt;
  demostd1.ms.imh[1]: Example artificial long slit image
  Compute sensitivity function
  Fit aperture 1 interactively? (no|yes|NO|YES) (no|yes|NO|YES) (yes):
  &lt;Exit with <span style="font-family: monospace;">'q'</span>&gt;
  Sensitivity function for all apertures --&gt; sens
  Flux and/or extinction calibrate standard stars
  [demostd1.ms.imh][1]: Example artificial long slit image
    Extinction correction applied
    Flux calibration applied
  Extract object spectrum demoobj1
  Searching aperture database ...
  Jan 17 16:05: DATABASE  - 1 apertures read for demoobj1 from database
  Extracting apertures ...
  Jan 17 16:05: EXTRACT - Aperture 1 from demoobj1 --&gt; demoobj1.ms
  Assign arc spectra for demoobj1
  [demoobj1] refspec1='demoarc1 0.403'
  [demoobj1] refspec2='demoarc2 0.597'
  Extract and reidentify arc spectrum demoarc1
  Searching aperture database ...
  Jan 17 16:05: DATABASE  - 1 apertures read for demoobj1 from database
  Jan 17 16:05: DATABASE - 1 apertures for demoarc1 written to database
  Extracting apertures ...
  Jan 17 16:05: EXTRACT - Aperture 1 from demoarc1 --&gt; demoobj1demoarc1.ms
  
  REIDENTIFY: NOAO/IRAF V2.10BETA valdes@puppis Fri 16:05:39 17-Jan-92
    Reference image = demoarc1.ms, New image = demoobj1..., Refit = yes
  Image Data    Found     Fit Pix Shift  User Shift  Z Shift      RMS
  demo...       48/48   48/48   -2.49E-4    -0.00109  -1.1E-7    0.227
  Extract and reidentify arc spectrum demoarc2
  Searching aperture database ...
  Jan 17 16:05: DATABASE  - 1 apertures read for demoobj1 from database
  Jan 17 16:05: DATABASE - 1 apertures for demoarc2 written to database
  Extracting apertures ...
  Jan 17 16:05: EXTRACT - Aperture 1 from demoarc2 --&gt; demoobj1demoarc2.ms
  
  REIDENTIFY: NOAO/IRAF V2.10BETA valdes@puppis Fri 16:05:42 17-Jan-92
    Reference image = demoarc1.ms, New image = demoobj1..., Refit = yes
  Image Data    Found     Fit Pix Shift  User Shift  Z Shift      RMS
  demo...       48/48   48/48    0.00266      0.0169  3.46E-6     0.24
  Dispersion correct demoobj1
  demoobj1.ms: ap = 1, w1 = 4204.181, w2 = 7355.375, dw = 6.16..., nw = 512
  Extinction correct demoobj1
  Flux calibrate demoobj1
  [demoobj1.ms.imh][1]: Example artificial long slit image
    Extinction correction applied
    Flux calibration applied
  </pre></div>
  <p>
  2.  To redo the above:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; doslit demoobj1 arcs=demoarc1,demoarc2 stand=demostd1 \
  &gt;&gt;&gt; extcor=yes, fluxcal=yes resize=yes redo+
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_DOSLIT">
  <dt><b>DOSLIT V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DOSLIT' Line='DOSLIT V2.11' -->
  <dd>The initial arc line identifications is done with the automatic line
  identification algorithm.
  </dd>
  </dl>
  <dl id="l_DOSLIT">
  <dt><b>DOSLIT V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DOSLIT' Line='DOSLIT V2.10.3' -->
  <dd>The usual output WCS format is <span style="font-family: monospace;">"equispec"</span>.  The image format type to be
  processed is selected with the <i>imtype</i> environment parameter.  The
  dispersion axis parameter is now a package parameter.  Images will only
  be processed if the have the CCDPROC keyword.  A <i>datamax</i> parameter
  has been added to help improve cosmic ray rejection.  The arc reference
  is no longer taken from the center of the image but using the first object
  aperture.  A bug which alphabetized the arc list was fixed.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  apbackground, apedit, apfind, approfiles, aprecenter, apresize, apsum,
  aptrace, apvariance, calibrate, ccdred, center1d, ctioslit, dispcor,
  echelle.doecslit, icfit, autoidentify, identify, kpnocoude, kpnoslit,
  specred, observatory, onedspec.package, refspectra, reidentify, sensfunc,
  setairmass, setjd, splot, standard
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'SUMMARY' 'PARAMETERS' 'ENVIRONMENT PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

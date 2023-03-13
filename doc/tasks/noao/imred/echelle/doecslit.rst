.. _doecslit:

doecslit: Process Echelle slit spectra
======================================

**Package: echelle**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  doecslit objects
  </p>
  </section>
  <section id="s_summary">
  <h3>Summary</h3>
  <p>
  <b>Doecslit</b> subtracts background sky or scattered light, extracts,
  wavelength calibrates, and flux calibrates multiorder echelle slit spectra
  which have been processed to remove the detector characteristics; i.e. CCD
  images have been bias, dark count, and flat field corrected.  The spectra
  should be oriented such that pixels of constant wavelength are aligned with
  the image columns or lines.  Small departures from this alignment are not
  critical resulting in only a small loss of resolution.  Single order
  observations should be reduced with <b>doslit</b>.
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
  <dl id="l_apref">
  <dt><b>apref = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apref' Line='apref = ""' -->
  <dd>Aperture reference spectrum.  This spectrum is used to define the basic
  extraction apertures and is typically a bright star spectrum.
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
  the calibration database (package parameter <i>echelle.caldir</i>).
  </dd>
  </dl>
  <dl id="l_readnoise">
  <dt><b>readnoise = 0., gain = 1. (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='readnoise' Line='readnoise = 0., gain = 1. (apsum)' -->
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
  <dl id="l_norders">
  <dt><b>norders = 10 (apfind)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='norders' Line='norders = 10 (apfind)' -->
  <dd>Number of orders to be found automatically.
  </dd>
  </dl>
  <dl id="l_width">
  <dt><b>width = 5. (apedit)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='width' Line='width = 5. (apedit)' -->
  <dd>Approximate full width of the spectrum profiles.  This parameter is used
  to define a width and error radius for the profile centering algorithm,
  and defaults for the aperture limits and background regions.
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
  <dd>Resize the defaults apertures for each object based on the spectrum profile?
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
  <dl id="l_trace">
  <dt><b>trace = yes (non-quicklook mode only) (aptrace)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trace' Line='trace = yes (non-quicklook mode only) (aptrace)' -->
  <dd>Allow tracing each object spectrum separately?  If not set then the trace
  from the aperture reference is used, with recentering to allow for shifts
  across the dispersion.  If set then each object and standard star
  image is retraced.  Retracing is NOT done in quicklook mode.
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background = <span style="font-family: monospace;">"none"</span> (apsum, apscatter)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = "none" (apsum, apscatter)' -->
  <dd>Type of background light subtraction.  The choices are <span style="font-family: monospace;">"none"</span> for no
  background subtraction, <span style="font-family: monospace;">"scattered"</span> for a global scattered light
  subtraction, <span style="font-family: monospace;">"average"</span> to average the background within background regions,
  <span style="font-family: monospace;">"median"</span> to use the median in background regions, <span style="font-family: monospace;">"minimum"</span> to use the
  minimum in background regions, or <span style="font-family: monospace;">"fit"</span> to fit across the dispersion using
  the background within background regions.  The scattered light option fits
  and subtracts a smooth global background and modifies the input images.
  This is a slow operation and so is NOT performed in quicklook mode.  The
  other background options are local to each aperture.  The <span style="font-family: monospace;">"fit"</span> option uses
  additional fitting parameters from <b>sparams</b> and the <span style="font-family: monospace;">"scattered"</span> option
  uses parameters from <b>apscat1</b> and <b>apscat2</b>.
  </dd>
  </dl>
  <dl id="l_splot">
  <dt><b>splot = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='splot' Line='splot = no' -->
  <dd>Plot the final spectra?  In quicklook mode a noninteractive, stacked plot
  is automatically produced using the task <b>specplot</b> while in
  non-quicklook mode a query is given and the task <b>splot</b> is used for
  interactive plotting.
  </dd>
  </dl>
  <dl id="l_redo">
  <dt><b>redo = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='redo' Line='redo = no' -->
  <dd>Redo operations previously done?  If no then previously processed spectra
  in the objects list will not be processed unless required by the
  update option.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = no' -->
  <dd>Update processing of previously processed spectra if the aperture
  reference image, the dispersion reference image, or standard star
  calibration data are changed?
  </dd>
  </dl>
  <dl id="l_quicklook">
  <dt><b>quicklook = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='quicklook' Line='quicklook = no' -->
  <dd>Extract and calibrate spectra with minimal interaction?  In quicklook mode
  only aperture reference definitions, the initial dispersion function
  solution, and the standard star setup are done interactively.  Scattered
  light subtraction and individual object tracing are not performed.
  Normally the <i>splot</i> option is set in this mode to produce an automatic
  final spectrum plot for each object.  It is recommended that this mode not be
  used for final reductions.
  </dd>
  </dl>
  <dl id="l_batch">
  <dt><b>batch = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='batch' Line='batch = no' -->
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
  examined and modified in the usual ways (typically with <span style="font-family: monospace;">"epar
  sparams"</span> or <span style="font-family: monospace;">":e sparams"</span> from the parameter editor).  The parameters are
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
  at the end of the image) used in finding, recentering, resizing,
  editing, and tracing operations.  A line of INDEF selects the middle of the
  image along the dispersion axis.
  </dd>
  </dl>
  <dl id="l_extras">
  <dt><b>extras = no (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extras' Line='extras = no (apsum)' -->
  <dd>Include raw unweighted and uncleaned spectra, the background spectra, and
  the estimated sigma spectra in a three dimensional output image format.
  See the discussion in the <b>apextract</b> package for further information.
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
  <dt><b>t_function = <span style="font-family: monospace;">"spline3"</span>, t_order = 2 (aptrace)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_function' Line='t_function = "spline3", t_order = 2 (aptrace)' -->
  <dd>Default trace fitting function and order.  The fitting function types are
  <span style="font-family: monospace;">"chebyshev"</span> polynomial, <span style="font-family: monospace;">"legendre"</span> polynomial, <span style="font-family: monospace;">"spline1"</span> linear spline, and
  <span style="font-family: monospace;">"spline3"</span> cubic spline.  The order refers to the number of
  terms in the polynomial functions or the number of spline pieces in the spline
  functions.
  </dd>
  </dl>
  <dl id="l_t_niterate">
  <dt><b>t_niterate = 1, t_low = 3., t_high = 3. (aptrace)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_niterate' Line='t_niterate = 1, t_low = 3., t_high = 3. (aptrace)' -->
  <dd>Default number of rejection iterations and rejection sigma thresholds.
  </dd>
  </dl>
  <p style="text-align:center">-- BACKGROUND AND SCATTERED LIGHT PARAMETERS --
  
  </p>
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
  <dt><b>b_niterate = 0 (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_niterate' Line='b_niterate = 0 (apsum)' -->
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
  <dl id="l_buffer">
  <dt><b>buffer = 1. (apscatter)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='buffer' Line='buffer = 1. (apscatter)' -->
  <dd>Buffer distance from the edge of any aperture for data to be included
  in the scattered light determination.  This parameter may be modified
  interactively.
  </dd>
  </dl>
  <dl id="l_apscat1">
  <dt><b>apscat1 = <span style="font-family: monospace;">""</span>, apscat2 = <span style="font-family: monospace;">""</span> (apscatter)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apscat1' Line='apscat1 = "", apscat2 = "" (apscatter)' -->
  <dd>Parameter sets for the fitting functions across and along the dispersion.
  These parameters are those used by <b>icfit</b>.  These parameters are
  usually set interactively.
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
  <p style="text-align:center">-- ARC DISPERSION FUNCTION PARAMETERS --
  
  </p>
  <dl id="l_threshold">
  <dt><b>threshold = 10. (identify/reidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 10. (identify/reidentify)' -->
  <dd>In order for a feature center to be determined the range of pixel intensities
  around the feature must exceed this threshold.
  </dd>
  </dl>
  <dl id="l_coordlist">
  <dt><b>coordlist = <span style="font-family: monospace;">"linelist$thar.dat"</span> (ecidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coordlist' Line='coordlist = "linelist$thar.dat" (ecidentify)' -->
  <dd>Arc line list consisting of an ordered list of wavelengths.
  Some standard line lists are available in the directory <span style="font-family: monospace;">"linelist$"</span>.
  </dd>
  </dl>
  <dl id="l_match">
  <dt><b>match = 1. (ecidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='match' Line='match = 1. (ecidentify)' -->
  <dd>The maximum difference for a match between the dispersion function computed
  value and a wavelength in the coordinate list.
  </dd>
  </dl>
  <dl id="l_fwidth">
  <dt><b>fwidth = 4. (ecidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fwidth' Line='fwidth = 4. (ecidentify)' -->
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
  <dt><b>i_function = <span style="font-family: monospace;">"legendre"</span>, i_xorder = 3, i_yorder = 3 (ecidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='i_function' Line='i_function = "legendre", i_xorder = 3, i_yorder = 3 (ecidentify)' -->
  <dd>The default function, function order for the pixel position dependence, and
  function order for the aperture number dependence to be fit to the arc
  wavelengths.  The functions choices are <span style="font-family: monospace;">"chebyshev"</span> or <span style="font-family: monospace;">"legendre"</span>.
  </dd>
  </dl>
  <dl id="l_i_niterate">
  <dt><b>i_niterate = 3, i_low = 3.0, i_high = 3.0 (ecidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='i_niterate' Line='i_niterate = 3, i_low = 3.0, i_high = 3.0 (ecidentify)' -->
  <dd>Number of rejection iterations and sigma thresholds for rejecting arc
  lines from the dispersion function fits.
  </dd>
  </dl>
  <dl id="l_refit">
  <dt><b>refit = yes (ecreidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refit' Line='refit = yes (ecreidentify)' -->
  <dd>Refit the dispersion function?  If yes and there is more than 1 line
  and a dispersion function was defined in the arc reference then a new
  dispersion function of the same type as in the reference image is fit
  using the new pixel positions.  Otherwise only a zero point shift is
  determined for the revised fitted coordinates without changing the
  form of the dispersion function.
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
  <dd>Average two reference spectra without regard to any sort parameter.
  If only one reference spectrum is specified then it is assigned with a
  warning.  If more than two reference spectra are specified then only the
  first two are used and a warning is given.
  This option is used to assign two reference spectra, with equal weights,
  independent of any sorting parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>following</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='following' Line='following' -->
  <dd>Select the nearest following spectrum in the reference list based on the
  sorting parameter.  If there is no following spectrum use the nearest preceding
  spectrum.
  </dd>
  </dl>
  <dl>
  <dt><b>interp</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='interp' Line='interp' -->
  <dd>Interpolate between the preceding and following spectra in the reference
  list based on the sorting parameter.  If there is no preceding and following
  spectrum use the nearest spectrum.  The interpolation is weighted by the
  relative distances of the sorting parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>match</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='match' Line='match' -->
  <dd>Match each input spectrum with the reference spectrum list in order.
  This overrides the reference aperture check.
  </dd>
  </dl>
  <dl>
  <dt><b>nearest</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nearest' Line='nearest' -->
  <dd>Select the nearest spectrum in the reference list based on the sorting
  parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>preceding</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='preceding' Line='preceding' -->
  <dd>Select the nearest preceding spectrum in the reference list based on the
  sorting parameter.  If there is no preceding spectrum use the nearest following
  spectrum.
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
  <dt><b>log = no (ecdispcor)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='log' Line='log = no (ecdispcor)' -->
  <dd>Use linear logarithmic wavelength coordinates?  Linear logarithmic
  wavelength coordinates have wavelength intervals which are constant
  in the logarithm of the wavelength.
  </dd>
  </dl>
  <dl id="l_flux">
  <dt><b>flux = yes (ecdispcor)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flux' Line='flux = yes (ecdispcor)' -->
  <dd>Conserve the total flux during interpolation?  If <i>no</i> the output
  spectrum is interpolated from the input spectrum at each output
  wavelength coordinate.  If <i>yes</i> the input spectrum is integrated
  over the extent of each output pixel.  This is slower than
  simple interpolation.
  </dd>
  </dl>
  <p style="text-align:center">-- SENSITIVITY CALIBRATION PARAMETERS --
  
  </p>
  <dl id="l_bandwidth">
  <dt><b>bandwidth = 10., bandsep = 10. (standard)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bandwidth' Line='bandwidth = 10., bandsep = 10. (standard)' -->
  <dd>Interpolated bandpass grid.  If INDEF then the same bandpasses as in the
  calibration files are used otherwise the calibration data is interpolated
  to the specified set of bandpasses.
  </dd>
  </dl>
  <dl id="l_s_interact">
  <dt><b>s_interact = yes (standard)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='s_interact' Line='s_interact = yes (standard)' -->
  <dd>Display the bandpasses on the standard star data and allow interactive
  addition and deletion of bandpasses.
  </dd>
  </dl>
  <dl id="l_s_function">
  <dt><b>s_function = <span style="font-family: monospace;">"spline3"</span>, s_order = 1 (sensfunc)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='s_function' Line='s_function = "spline3", s_order = 1 (sensfunc)' -->
  <dd>Function and order used to fit the sensitivity data.  The function types are
  <span style="font-family: monospace;">"chebyshev"</span> polynomial, <span style="font-family: monospace;">"legendre"</span> polynomial, <span style="font-family: monospace;">"spline3"</span> cubic spline,
  and <span style="font-family: monospace;">"spline1"</span> linear spline.
  Order of the sensitivity fitting function.  The value corresponds to the
  number of polynomial terms or the number of spline pieces.  The default
  values may be changed interactively.
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
  <dt><b>extinction = <span style="font-family: monospace;">"onedstds$kpnoextinct.dat"</span> (standard, sensfunc, calibrate)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extinction' Line='extinction = "onedstds$kpnoextinct.dat" (standard, sensfunc, calibrate)' -->
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
  <b>Doecslit</b> subtracts background sky or scattered light, extracts,
  wavelength calibrates, and flux calibrates multiorder echelle slit spectra
  which have been processed to remove the detector characteristics; i.e. CCD
  images have been bias, dark count, and flat field corrected.  The spectra
  should be oriented such that pixels of constant wavelength are aligned with
  the image columns or lines.  Small departures from this alignment are not
  critical resulting in only a small loss of resolution.  Single order
  observations should be reduced with <b>doslit</b>.
  </p>
  <p>
  The task is a command language script which collects and combines the
  functions and parameters of many general purpose tasks to provide a single,
  complete data reduction path and a degree of guidance, automation, and
  record keeping.  In the following description and in the parameter section
  the various general tasks used are identified.  Further
  information about those tasks and their parameters may be found in their
  documentation.  <b>Doecslit</b> also simplifies and consolidates parameters
  from those tasks and keeps track of previous processing to avoid
  duplications.
  </p>
  <p>
  The general organization of the task is to do the interactive setup steps,
  such as the aperture definitions and reference dispersion function
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
  <dd>Set the <b>doecslit</b> parameters with <b>eparam</b>.  Specify the object
  images to be processed, an aperture reference image (usually a bright
  star spectrum) to use in finding the orders and defining the
  aperture parameters, one or more arc images, and one or more standard
  star images.  If there are many object, arc, or standard star images
  you might prepare <span style="font-family: monospace;">"@ files"</span>.  Set the detector and data
  specific parameters.  Select the processing options desired.
  Finally you might wish to review the <b>sparams</b> algorithm parameters
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
  <dd>The specified number of orders (ranked by peak strength) in the aperture
  reference image are located and default fixed width apertures are
  assigned.  If the resize option is set the apertures are resized by finding
  the level which is 5% (the default) of the peak above local background.
  You then have the option of entering the aperture editing loop to check the
  aperture positions, sizes, and background fitting parameters.  This is
  highly recommended.  Note that it is important that the aperture numbers be
  sequential with the orders and if any orders are skipped the aperture
  numbers should also skip.  It is also important to verify the background
  regions with the <span style="font-family: monospace;">'b'</span> key.  Usually you want any changes made to the
  background definitions to apply to all apertures so use the <span style="font-family: monospace;">'a'</span> key to
  select all apertures before modifying the background parameters.  To exit
  the background mode and then to exit the review mode use <span style="font-family: monospace;">'q'</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>[5]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[5]' -->
  <dd>The order positions at a series of points along the dispersion are measured
  and a function is fit to these positions.  This may be done interactively
  to examine the traced positions and adjust the fitting parameters.  To exit
  the interactive fitting type <span style="font-family: monospace;">'q'</span>.  Not all orders need be examined and the
  <span style="font-family: monospace;">"NO"</span> response will quit the interactive fitting using the last defined
  fitting parameters on the remaining traces.
  </dd>
  </dl>
  <dl>
  <dt><b>[6]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[6]' -->
  <dd>Apertures are now defined for all standard and object images.  This is only
  done if there are no previous aperture definitions for the image.  The
  aperture references previously defined are used as the initial set of
  apertures for each image.  The apertures are then recentered by an average
  shift over all orders and resized if that option is selected.
  The apertures may also be retraced and interactively examined
  for each image if the tracing option is selected and quicklook mode is not.
  </dd>
  </dl>
  <dl>
  <dt><b>[7]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[7]' -->
  <dd>If scattered light subtraction is selected the scattered light parameters
  are set using the aperture reference image and the task <b>apscatter</b>.
  The purpose of this is to interactively define the aperture buffer distance
  for the scattered light and the cross and parallel dispersion fitting
  parameters.  The fitting parameters are taken from and recorded in the
  parameter sets <b>apscat1</b> and <b>apscat2</b>.  All other scattered light
  subtractions are done noninteractively with these parameters.  Note that
  the scattered light correction modifies the input images.  Scattered light
  subtraction is not done in quicklook mode.
  </dd>
  </dl>
  <dl>
  <dt><b>[8]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[8]' -->
  <dd>If dispersion correction is selected the first arc in the arc list is
  extracted.  The dispersion function is defined using the task
  <b>ecidentify</b>.  Identify a few arc lines in a few orders with <span style="font-family: monospace;">'m'</span> and
  <span style="font-family: monospace;">'o'</span> and use the <span style="font-family: monospace;">'l'</span> line list identification command to automatically add
  additional lines and fit the dispersion function.  Check the quality of the
  dispersion function fit with <span style="font-family: monospace;">'f'</span>.  When satisfied exit with <span style="font-family: monospace;">'q'</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>[9]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[9]' -->
  <dd>If the flux calibration option is selected the standard star spectra are
  processed (if not done previously).  The images are background subtracted,
  extracted, and wavelength calibrated.  The appropriate arc
  calibration spectra are extracted and the dispersion function refit
  using the arc reference spectrum as a starting point.  The standard star
  fluxes through the calibration bandpasses are compiled.  You are queried
  for the name of the standard star calibration data file.  Because echelle
  spectra are often at much higher dispersion than the calibration data,
  interpolated bandpasses may be defined with the bandpass parameters in
  <b>sparams</b> and checked or modified interactively.
  After all the standard stars are processed a sensitivity function is
  determined using the interactive task <b>sensfunc</b>.  Finally, the
  standard star spectra are extinction corrected and flux calibrated
  using the derived sensitivity function.
  </dd>
  </dl>
  <dl>
  <dt><b>[10]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[10]' -->
  <dd>The object spectra are now automatically background subtracted
  (an alternative to scattered light subtraction),
  extracted, wavelength calibrated, and flux calibrated.
  </dd>
  </dl>
  <dl>
  <dt><b>[11]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[11]' -->
  <dd>The option to examine the final spectra with <b>splot</b> may be given.
  To exit type <span style="font-family: monospace;">'q'</span>.  In quicklook mode the spectra are plotted
  noninteractively with <b>specplot</b>.
  </dd>
  </dl>
  <dl>
  <dt><b>[12]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[12]' -->
  <dd>The final spectra will have the same name as the original 2D images
  with a <span style="font-family: monospace;">".ec"</span> extension added.
  </dd>
  </dl>
  <p>
  <b>Spectra and Data Files</b>
  </p>
  <p>
  The basic input consists of echelle slit object, standard star, and arc
  calibration spectra stored as IRAF images.
  The type of image format is defined by the
  environment parameter <i>imtype</i>.  Only images with that extension will
  be processed and created.
  The raw CCD images must be
  processed to remove overscan, bias, dark count, and flat field effects.
  This is generally done using the <b>ccdred</b> package.  Flat fields which
  are not contaminated by low counts between the apertures may be prepared
  with the task <b>apflatten</b> (recommended) or <b>apnormalize</b>.  Lines of
  constant wavelength across the orders should be closely aligned with one of
  the image axes.  Sometimes the orders are aligned rather than the spectral
  features.  This will result in a small amount of resolution loss but is
  often acceptable.  In some cases one may correct for misalignment with the
  <b>rotate</b> task.  More complex geometric problems and observations of
  extended objects should be handled by the <b>longslit</b> package and single
  order observations should be processed by <b>doslit</b>.
  </p>
  <p>
  The aperture reference spectrum is generally a bright star.  The arc
  spectra are comparison arc lamp observations (they must all be of the same
  type).  The assignment of arc calibration exposures to object exposures is
  generally done by selecting the nearest in time and interpolating.
  However, the optional <i>arc assignment table</i> may be used to explicitly
  assign arc images to specific objects.  The format of this file is
  described in task <b>refspectra</b>.
  </p>
  <p>
  The final reduced spectra are recorded in two or three dimensional IRAF
  images.  The images have the same name as the original images with an added
  <span style="font-family: monospace;">".ec"</span> extension.  Each line in the reduced image is a one dimensional
  spectrum with associated aperture, order, and wavelength
  information.  When the <i>extras</i> parameter is set the lines in the
  third dimension contain additional information (see
  <b>apsum</b> for further details).  These spectral formats are accepted by the
  one dimensional spectroscopy tasks such as the plotting tasks <b>splot</b>
  and <b>specplot</b>.  The special task <b>scopy</b> may be used to extract
  specific apertures or to change format to individual one dimensional
  images.  The task <b>scombine</b> is used to combine or merge orders into
  a single spectrum.
  </p>
  <p>
  <b>Package Parameters</b>
  </p>
  <p>
  The <b>echelle</b> package parameters set parameters which change
  infrequently and define the standard I/O functions.  The extinction file
  is used for making extinction corrections and the standard star
  calibration directory is used for determining flux calibrations from
  standard star observations.  The calibration directories contain data files
  with standard star fluxes and band passes.  The available extinction
  files and flux calibration directories may be listed using the command:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; page onedstds$README
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
  The verbose parameter selects whether to print everything which goes
  into the log file on the terminal.  It is useful for monitoring
  what the <b>doecslit</b> task does.  The log and plot files are useful for
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
  image lists are checked to remove extracted images (the .ec images)
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
  As mentioned earlier, all the arc images must be of the same type;
  that is taken with the same arc lamp.  The aperture reference parameter
  is a single image name which is usually a bright star.
  </p>
  <p>
  The next set of parameters describe the noise characteristics and the
  general layout of the orders.  The read out noise and gain are used when
  <span style="font-family: monospace;">"cleaning"</span> cosmic rays and when using variance or optimal weighting.  These
  parameters must be fairly accurate.  Note that these are the effective
  parameters and must be adjusted if previous processing has modified the
  pixel values; such as with an unnormalized flat field.
  </p>
  <p>
  The general direction in which the orders run is specified by the
  dispersion axis parameter.  Recall that ideally it is the direction
  of constant wavelength which should be aligned with an image axis and
  the dispersion direction will not be aligned because of the cross-dispersion.
  The <i>norders</i> parameter is used to automatically find the orders.  The
  specified number of the brightest peaks are found.  Generally after finding the
  orders the aperture definitions are reviewed and adjusted interactively.
  The profile width should be approximately the full width at the profile
  base.  The default aperture limits and background regions are all
  derived from this width parameter.
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
  The <i>resize</i> option resets the edges of the extraction apertures based
  on the profile for each object and standard star order.  The default
  resizing is to the 5% point relative to the peak measured above the
  background.  This allows following changes in the seeing.  However, one
  should consider the consequences of this if attempting to flux calibrate
  the observations.  Except in quicklook mode, the apertures for each object
  and standard star observation may be reviewed graphically and further
  adjustments made to the aperture width and background regions.
  </p>
  <p>
  The apertures for each observation are adjusted for small shifts relative
  to the reference aperture definitions.  If you think this is not sufficient,
  say to account for rotation of the detector or for differing atmospheric
  dispersion, the <i>trace</i> option allows redefining the aperture trace
  functions for each observation.  Note this is only allowed in non-quicklook
  mode.
  </p>
  <p>
  The <i>clean</i> option invokes a profile
  fitting and deviant point rejection algorithm as well as a variance weighting
  of points in the aperture.  See the next section for more about
  requirements to use this option.
  </p>
  <p>
  The <i>background</i> option selects a type of correction for background
  or scattered light.  If the type is <span style="font-family: monospace;">"scattered"</span> a global scattered light
  is fit to the data between the apertures  and subtracted from the images.
  <i>Note that the input images are modified by this operation</i>.
  This option is slow and is not allowed in quicklook
  mode.  Alternatively, a local background may be subtracted using
  background regions defined for each aperture.  The background may be
  within the slit for a sky subtraction or outside of the slit for a
  local scattered light subtraction.  The data in the regions
  may be averaged, medianed, or the minimum value used.  Another choice
  is to fit the data in the background regions by a function and interpolate
  to the object aperture.
  </p>
  <p>
  Generally once a spectrum has been processed it will not be reprocessed if
  specified as an input spectrum.  However, changes to the underlying
  calibration data can cause such spectra to be reprocessed if the
  <i>update</i> flag is set.  The changes which will cause an update are a new
  reference image, adding the scattered light subtraction option, a new arc
  reference image, and new standard stars.  If all input spectra are to be
  processed regardless of previous processing the <i>redo</i> flag may be
  used.  Note that reprocessing clobbers the previously processed output
  spectra.
  </p>
  <p>
  The final step is to plot the spectra if the <i>splot</i> option is
  selected.  In non-quicklook mode there is a query which may be
  answered either in lower or upper case.  The plotting uses the interactive
  task <b>splot</b>.  In quicklook mode the plot appears noninteractively
  using the task <b>specplot</b>.  
  </p>
  <p>
  The <i>quicklook</i> option provides a simpler, less interactive, mode.
  The quicklook mode automatically assigns the reference apertures to
  the object and standard star observations without interactive review
  or tracing, does not do the time consuming scattered light correction,
  and the <i>splot</i> option selects a noninteractive plot to be
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
  parameter set is called <b>sparams</b>.  The algorithm parameters are
  discussed further in the next section.
  </p>
  <p>
  <b>Algorithms and Algorithm Parameters</b>
  </p>
  <p>
  This section summarizes the various algorithms used by the
  <b>doecslit</b> task and the parameters which control and modify the
  algorithms.  The algorithm parameters available to you are
  collected in the parameter set <b>sparams</b>.  These parameters are
  taken from the various general purpose tasks used by the <b>doecslit</b>
  processing task.  Additional information about these parameters and
  algorithms may be found in the help for the actual
  task executed.  These tasks are identified below.  The aim of this
  parameter set organization is to collect all the algorithm parameters
  in one place separate from the processing parameters and include only
  those which are relevant for echelle slit data.  The parameter values
  can be changed from the defaults by using the parameter editor,
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epar sparams
  </pre></div>
  <p>
  or simple typing <i>sparams</i>.
  The parameter editor can also be entered when editing the <b>doecslit</b>
  parameters by typing <i>:e</i> when positioned at the <i>sparams</i>
  parameter.
  </p>
  <p>
  <b>Aperture Definitions</b>
  </p>
  <p>
  The first operation is to define the extraction apertures, which include the
  aperture width, background regions, and position dependence with
  wavelength, for the input echelle slit spectra and, if flux calibration is
  selected, the standard star spectra.  This is done only for spectra which
  do not have previously defined apertures unless the <i>redo</i> option is
  set to force all definitions to be redone.  Thus, apertures may be
  defined separately using the <b>apextract</b> tasks.  This is particularly
  useful if one needs to use reference images to define apertures for very
  weak spectra which are not well centered or traced by themselves.
  </p>
  <p>
  Initially apertures are defined for a specified <i>aperture reference</i>
  image.  The selected number of orders are found automatically by selecting
  the highest peaks in a cut across the dispersion.  Apertures are assigned
  with a width given by the <i>width</i> parameter and numbered sequentially.
  The background regions are also defined in terms of the width parameter
  starting at one width distance from the profile center and extending to two
  widths on both sides of the profile.  As an example, if the width parameter
  is 5 pixels the default aperture limits are +/- 2.5 pixels and the
  background sample regions will be <span style="font-family: monospace;">"-10:-5,5:10"</span>.  If the <i>resize</i>
  parameter is set the aperture limits are adjusted to a specified point on
  the spectrum profile (see <b>apresize</b>).
  </p>
  <p>
  A query is then given allowing the aperture definitions to be reviewed and
  modified.  Queries made by <b>doecslit</b> generally may be answered with either
  lower case <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"no"</span> or with upper case <span style="font-family: monospace;">"YES"</span> or <span style="font-family: monospace;">"NO"</span>.  The upper
  case responses apply to all further queries and so are used to eliminate
  further queries of that kind.
  </p>
  <p>
  Reviewing the aperture definitions is highly recommended to check the
  aperture numbering, aperture limits, and background regions.  The aperture
  numbers must be linearly related, with a slope of +/- 1, to the true order
  numbers though absolute order numbers need not be known.  The key point is
  that if an order is skipped the aperture numbers must also skip.  The
  background regions are checked with the <span style="font-family: monospace;">'b'</span> key.  Typically one adjusts all
  the background regions at the same time by selecting all apertures with
  the <span style="font-family: monospace;">'a'</span> key first.  To exit the background and aperture editing steps type
  <span style="font-family: monospace;">'q'</span>.
  </p>
  <p>
  Next the positions of the orders at various points along the dispersion
  are measured and <span style="font-family: monospace;">"trace functions"</span> are fit.  The user is asked whether
  to fit each trace function interactively.  This is selected to adjust
  the fitting parameters such as function type and order.  When
  interactively fitting a query is given for each aperture.  After the
  first aperture one may skip reviewing the other traces.
  </p>
  <p>
  After the aperture reference image is done all the object and standard star
  images are checked for aperture definitions and those without definitions
  are assigned apertures.  The assignment consists of inheriting the aperture
  from the reference aperture image, recentering the apertures based on an
  average shift that best centers all the apertures, resizing the apertures
  if the resize option is selected, and retracing the spectral orders if the
  retracing option is selected.  Retracing is only allowed in non-quicklook
  mode (set by the <i>quicklook</i> parameter).  Also interactive review of
  the aperture definitions is only done in
  non-quicklook mode.  In quicklook mode the aperture definitions are all set
  noninteractively without retracing.  It is recommended that quicklook only
  be used for initial quick extractions and calibration and that for final
  reductions one at least review the aperture definitions and possibly
  retrace each observation.
  </p>
  <p>
  The above steps are all performed using tasks from the <b>apextract</b>
  package and parameters from the <b>sparams</b> parameters.  As a quick
  summary, the dispersion direction of the spectra are determined from the
  package <b>dispaxis</b> parameter if not defined in the image header.  The default
  line or column for finding the object position on the slit and the number
  of image lines or columns to sum are set by the <i>line</i> and <i>nsum</i>
  parameters.  A line of INDEF (the default) selects the middle of the
  image.  The automatic finding algorithm is described for the task
  <b>apfind</b> and basically finds the strongest peaks.  The resizing is
  described in the task <b>apresize</b> and the parameters used are also
  described there.  The tracing is
  done as described in <b>aptrace</b> and consists of stepping along the image
  using the specified <i>t_step</i> parameter.  The function fitting uses the
  <b>icfit</b> commands with the other parameters from the tracing section.
  </p>
  <p>
  <b>Background or Scattered Light Subtraction</b>
  </p>
  <p>
  In addition to not subtracting any sky or scattered light there are two
  approaches to subtracting background light.  The first is to determine
  a smooth global scattered light component.  The second is to subtract
  a locally determined background at each point along the dispersion and
  for each aperture.  This can be either for a sky subtraction if the
  background regions are within the slit or scattered light if the
  background regions are outside of the slit.  Note that background
  subtraction is only done for object and standard star images and not
  for arc spectra.  Also, the global scattered light option is not done
  in quicklook mode.
  </p>
  <p>
  The global scattered light fitting and subtraction is done with the task
  <b>apscatter</b>.  The function fitting parameters are set interactively
  using the aperture reference spectrum.  All other subtractions are done
  noninteractively with the same set of parameters.  The scattered light is
  subtracted from the input images, thus modifying them, and one might wish
  to first make backups of the original images.
  </p>
  <p>
  The scattered light is measured between the apertures using a specified
  buffer distance from the aperture edges.  The scattered light pixels are
  fit by a series of one dimensional functions across the dispersion.  The
  independent fits are then smoothed along the dispersion by again fitting
  low order functions.  These fits then define the smooth scattered light
  surface to be subtracted from the image.  The fitting parameters are
  defined and recorded in the two parameter sets <i>apscat1</i> and
  <i>apscat2</i>.  The scattered light algorithm is described more fully in
  <b>apscatter</b>.  This algorithm is relatively slow.
  </p>
  <p>
  Local background subtraction is done during extraction based on background
  regions and parameters defined by the default background parameters or
  changed during interactive review of the apertures.  The background
  subtraction options are to subtract the average, median, or minimum of the
  pixels in the background regions, or to fit a function and subtract the
  function from under the extracted object pixels.  The background regions
  are specified in pixels from the aperture center and follow changes in
  center of the spectrum along the dispersion.  The syntax is colon separated
  ranges with multiple ranges separated by a comma or space.  The background
  fitting uses the <b>icfit</b> routines which include medians, iterative
  rejection of deviant points, and a choice of function types and orders.
  Note that it is important to use a method which rejects cosmic rays such as
  using either medians over all the background regions (<i>background</i> =
  <span style="font-family: monospace;">"median"</span>) or median samples during fitting (<i>b_naverage</i> &lt; -1).  The
  background subtraction algorithm and options are described in greater
  detail in <b>apsum</b> and <b>apbackground</b>.
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
  (i.e. accounting for any image combining) read out noise and gain.
  These numbers need to be adjusted if the image has been processed
  such that the intensity scale has a different origin (such as
  a scattered light subtraction) or scaling (such as caused by unnormalized
  flat fielding).  These options also require using background subtraction
  if the profile does not go to zero.  For optimal extraction and
  cleaning to work it is recommended that any flat fielding be done
  using flat fields produced by <b>apflatten</b>, no scattered light
  correction, and using background subtraction if there is any
  appreciable sky or to compensate for scattered light.
  For further discussion of cleaning and variance weighted extraction see
  <b>apvariance</b> and <b>approfiles</b> as well as  <b>apsum</b>.
  </p>
  <p>
  <b>Dispersion Correction</b>
  </p>
  <p>
  If dispersion correction is not selected, <i>dispcor</i>=no, then the object
  spectra are simply extracted.  The extracted spectra may be plotted
  by setting the <i>splot</i> option.  This produces a query and uses
  the interactive <b>splot</b> task in non-quicklook mode and uses
  <b>specplot</b> noninteractively in quicklook mode.
  </p>
  <p>
  Dispersion corrections are applied to the extracted spectra if the
  <i>dispcor</i> processing parameter is set.  There
  are three basic steps involved; determining the dispersion functions
  relating pixel position to wavelength, assigning the appropriate
  dispersion function to a particular observation, and either storing
  the nonlinear dispersion function in the image headers or resampling the
  spectra to evenly spaced pixels in wavelength.
  </p>
  <p>
  The first arc spectrum in the arc list is used to define the reference
  dispersion solution.  It is extracted using the reference aperture definition.
  Note extractions of arc spectra are not background or scattered light
  subtracted.  The interactive task <b>ecidentify</b> is used to define the
  dispersion function.  The idea is to mark some lines in a few orders whose
  wavelengths are known (with the line list used to supply additional lines after
  the first few identifications define the approximate wavelengths) and to fit a
  function giving the wavelength from the aperture number and pixel position.
  </p>
  <p>
  The arc dispersion function parameters are for <b>ecidentify</b> and it's
  related partner <b>ecreidentify</b>.  The parameters define a line list for
  use in automatically assigning wavelengths to arc lines, a centering width
  (which should match the line widths at the base of the lines), the
  dispersion function type and orders, parameters to exclude bad lines from
  function fits, and defining whether to refit the dispersion function as
  opposed to simply determining a zero point shift.  The defaults should
  generally be adequate and the dispersion function fitting parameters may be
  altered interactively.  One should consult the help for the two tasks for
  additional details of these parameters and the interactive operation of
  <b>ecidentify</b>.
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
  In non-quicklook mode the arc spectra assigned to each object are
  extracted using the same apertures as the object.  This accounts for
  changes in the recentering, aperture sizes, and tracing functions.
  In quicklook mode the arc spectra are extracted using the reference
  apertures.  When the same arc is used for several object images this
  allows the arc spectrum to only be extracted once.
  </p>
  <p>
  Defining the dispersion function for a new arc extraction is done with
  the task <b>ecreidentify</b>.  This is done noninteractively with log
  information recorded about the line reidentifications and the fit.
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
  wavelength.  For echelle spectra each order is linearized independently so
  that the wavelength interval per pixel is different in different orders.
  This preserves most of the resolution and avoids over or under sampling of
  the highest or lowest dispersion orders.  The wavelength limits are
  taken from the limits determined from the arc reference spectrum and
  the number of pixels is the same as the original images.  The dispersion
  per pixel is then derived from these constraints.
  </p>
  <p>
  The linearization algorithm  parameters allow selecting the interpolation
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
  fluxes.  For very high resolution it may be the case that the measured
  calibration bandpasses are too large or sparse.  In this case one must
  interpolate the calibration data to bandpasses appropriate for the data.
  If the bandpass widths and separations are given as INDEF then the same
  bandpasses as in the calibration file are used.  Otherwise a uniform grid
  of bandpasses is interpolated.  Using interpolated bandpasses is not
  rigorous but is sometimes the only choice for echelle spectra.
  </p>
  <p>
  The standard star tabulations are done after each standard star is
  extracted and dispersion corrected.  You are asked for the name of the
  standard star as tabulated in the absolute flux data files in the directory
  <i>caldir</i> defined by the package parameters.  If the <i>interact</i>
  parameter is yes the bandpasses can be displayed on the data and you can
  interactively add or delete bandpasses. The tabulation of the standard star
  observations over the standard bandpasses is done by the task
  <b>standard</b>.  The tabulated data is stored in the file <i>std</i>.  Note
  that if the <i>redo</i> flag is not set any new standard stars specified in
  subsequent executions of <b>doecslit</b> are added to the previous data in
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
  page for <b>sensfunc</b>.  The sensitivity function is saved as one
  dimensional spectra (one per order) with the root name <i>sens</i>.
  Deletion of these images will also cause reprocessing to occur if the
  <i>update</i> flag is set.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  The following example uses artificial data and may be executed
  at the terminal (with IRAF V2.10).  This is similar to the sequence
  performed by the test procedure <span style="font-family: monospace;">"demos doecslit"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ec&gt; demos mkecslit
  Creating example longslit in image demoobj ...
  Creating example longslit in image demostd ...
  Creating example longslit in image demoarc ...
  ec&gt; echelle.verbose=no
  ec&gt; echelle.caldir=onedstds$spechayescal/
  ec&gt; doecslit Bdemoobj apref=Bdemostd arcs=Bdemoarc stand=Bdemostd \
  &gt;&gt;&gt; norders=3 extcor+ fluxcal+ resize+ splot+
  Set reference aperture for Bdemostd
  Edit apertures for Bdemostd?  (yes):
  &lt;Check background with <span style="font-family: monospace;">'b'</span>, exit background and review with <span style="font-family: monospace;">'q'</span>&gt;
  Fit traced positions for Bdemostd interactively?  (yes):
  Fit curve to aperture 1 of Bdemostd interactively  (yes):
  &lt;Exit with <span style="font-family: monospace;">'q'</span>&gt;
  Fit curve to aperture 2 of Bdemostd interactively  (yes): N
  Edit apertures for Bdemoobj?  (yes):
  &lt;Check background with <span style="font-family: monospace;">'b'</span>, exit background and review with <span style="font-family: monospace;">'q'</span>&gt;
  Fit traced positions for Bdemoobj interactively?  (yes): N
  Extract arc reference image Bdemoarc
  Determine dispersion solution for Bdemoarc
  &lt;Type <span style="font-family: monospace;">'m'</span> at first strong line (pixel 156) and identify it as 4965&gt;
  &lt;Type <span style="font-family: monospace;">'k'</span> to go to next order&gt;
  &lt;Mark 52-&gt;5002, 74-&gt;5003.6, 155-&gt;5009.3&gt;
  &lt;Type <span style="font-family: monospace;">'k'</span> to go to next order and mark 18-&gt;5044.7, 231-&gt;5059.8&gt;
  &lt;Type <span style="font-family: monospace;">'f'</span> to see the fit residuals&gt;
  &lt;Type <span style="font-family: monospace;">'q'</span> to quit fit and then <span style="font-family: monospace;">'q'</span> to exit&gt;
  Extract standard star spectrum Bdemostd
  Assign arc spectra for Bdemostd
  Extract and reidentify arc spectrum Bdemoarc
  Dispersion correct Bdemostd
  B...ec.imh: ap = 1, w1 = 4953.9, w2 = 4972.2, dw = 0.071, nw = 256
  B...ec.imh: ap = 2, w1 = 4998.3, w2 = 5016.5, dw = 0.071, nw = 256
  B...ec.imh: ap = 3, w1 = 5043.5, w2 = 5061.6, dw = 0.070, nw = 256
  Compile standard star fluxes for Bdemostd
  Bdemostd.ec.imh[1]: Artificial Echelle Spectrum
  Star name in calibration list: hz14
  Bdemostd.ec.imh[1]: Edit bandpasses? (no|yes|NO|YES|NO!|YES!) (no): y
  &lt;Exit with <span style="font-family: monospace;">'q'</span>&gt;
  Bdemostd.ec.imh[2]: Artificial Echelle Spectrum
  Bdemostd.ec.imh[2]: Edit bandpasses? (no|yes|NO|YES|NO!|YES!) (y): N
  Bdemostd.ec.imh[3]: Artificial Echelle Spectrum
  Bdemostd.ec.imh[3]: Edit bandpasses? (no|yes|NO|YES|NO!|YES!) (N):
  Compute sensitivity function
  Fit aperture 1 interactively? (no|yes|NO|YES) (no|yes|NO|YES) (yes):
  &lt;Exit with <span style="font-family: monospace;">'q'</span>&gt;
  Sensitivity function for aperture  1 --&gt; sens.0001
  Fit aperture 2 interactively? (no|yes|NO|YES) (no|yes|NO|YES) (yes): N
  Sensitivity function for aperture  2 --&gt; sens.0002
  Sensitivity function for aperture  3 --&gt; sens.0003
  Flux and/or extinction calibrate standard stars
  Standard stars:
  Splot spectrum? (no|yes|NO|YES) (yes):
  Image line/aperture to plot (0:) (1):
  &lt;Exit with <span style="font-family: monospace;">'q'</span>&gt;
  Extract object spectrum Bdemoobj
  Assign arc spectra for Bdemoobj
  Extract and reidentify arc spectrum Bdemoarc
  Dispersion correct Bdemoobj
  B...ec.imh: ap = 1, w1 = 4953.9, w2 = 4972.2, dw = 0.071, nw = 256
  B...ec.imh: ap = 2, w1 = 4998.3, w2 = 5016.5, dw = 0.071, nw = 256
  B...ec.imh: ap = 3, w1 = 5043.5, w2 = 5061.6, dw = 0.070, nw = 256
  Extinction correct Bdemoobj
  Flux calibrate Bdemoobj
  Bdemoobj.ec.imh:
  Splot spectrum? (no|yes|NO|YES) (yes):
  Image line/aperture to plot (0:) (1):
  &lt;Exit with <span style="font-family: monospace;">'q'</span>&gt;
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_DOECSLIT">
  <dt><b>DOECSLIT V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DOECSLIT' Line='DOECSLIT V2.10.3' -->
  <dd>The image format type to be
  processed is selected with the <i>imtype</i> environment parameter.  The
  dispersion axis parameter is now a package parameter.  Images will only
  be processed if the have the CCDPROC keyword.  A <i>datamax</i> parameter
  has been added to help improve cosmic ray rejection.  A bug which
  alphabetized the arc spectra was fixed.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  apbackground, apedit, apfind, approfiles, aprecenter, apresize, apsum, aptrace,
  apvariance, calibrate, ccdred, center1d, ctioslit, dispcor,
  echelle.doecslit, ecidentify, ecreidentify, icfit, kpnocoude, kpnoslit,
  msred, observatory, onedspec.package, refspectra, sensfunc, setairmass, setjd,
  splot, standard
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'SUMMARY' 'PARAMETERS' 'ENVIRONMENT PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

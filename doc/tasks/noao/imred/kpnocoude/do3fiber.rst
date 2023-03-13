.. _do3fiber:

do3fiber: Process KPNO coude three fiber spectra
================================================

**Package: kpnocoude**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  do3fiber objects
  </p>
  </section>
  <section id="s_summary">
  <h3>Summary</h3>
  <p>
  The <b>do3fiber</b> reduction task is specialized for scattered light
  subtraction, extraction, flat
  fielding, and wavelength calibration of multifiber data in which some
  fibers are used to take object spectra and other fibers are used to
  take simultaneous arc spectra.  A three fiber instrument of this
  type (one object and two arc fibers) is available at the KPNO coude feed.
  The default parameters are set for this configuration.
  If there are a large number of fibers and fiber throughput and sky
  fiber subtraction is needed the <b>dofiber</b> task should be used.
  </p>
  <p>
  The <b>do3fiber</b> task is a command language script which collects
  and combines the functions and parameters of many general purpose tasks to
  provide a single complete data reduction path.  The task provides a degree
  of guidance, automation, and record keeping necessary when dealing with
  this type of multifiber data.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_objects">
  <dt><b>objects</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='objects' Line='objects' -->
  <dd>List of object spectra to be processed.  Previously processed spectra are
  ignored unless the <i>redo</i> flag is set or the <i>update</i> flag is set and
  dependent calibration data has changed.  Extracted spectra are ignored.
  </dd>
  </dl>
  <dl id="l_apref">
  <dt><b>apref = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apref' Line='apref = ""' -->
  <dd>Aperture reference spectrum.  This spectrum is used to define the basic
  extraction apertures and is typically a flat field spectrum.
  </dd>
  </dl>
  <dl id="l_flat">
  <dt><b>flat = <span style="font-family: monospace;">""</span> (optional)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flat' Line='flat = "" (optional)' -->
  <dd>Flat field spectrum.  If specified the one dimensional flat field spectra
  are extracted and used to make flat field corrections.
  </dd>
  </dl>
  <dl id="l_arcs">
  <dt><b>arcs = <span style="font-family: monospace;">""</span> (at least one if dispersion correcting)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='arcs' Line='arcs = "" (at least one if dispersion correcting)' -->
  <dd>List of primary, all fiber arc spectra.  These spectra are used to define
  the dispersion functions for each fiber apart from a possible zero point
  correction made with simultaneous arc calibration fibers in the object
  spectra.  One fiber from the first spectrum is used to mark lines and set
  the dispersion function interactively and dispersion functions for all
  other fibers and arc spectra are derived from it.
  </dd>
  </dl>
  <dl id="l_arctable">
  <dt><b>arctable = <span style="font-family: monospace;">""</span> (optional) (refspectra)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='arctable' Line='arctable = "" (optional) (refspectra)' -->
  <dd>Table defining arc spectra to be assigned to object
  spectra (see <b>refspectra</b>).  If not specified an assignment based
  on a header parameter, <i>params.sort</i>, such as the observation time is made.
  </dd>
  </dl>
  <dl id="l_readnoise">
  <dt><b>readnoise = <span style="font-family: monospace;">"RDNOISE"</span> (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='readnoise' Line='readnoise = "RDNOISE" (apsum)' -->
  <dd>Read out noise in photons.  This parameter defines the minimum noise
  sigma.  It is defined in terms of photons (or electrons) and scales
  to the data values through the gain parameter.  A image header keyword
  (case insensitive) may be specified to get the value from the image.
  </dd>
  </dl>
  <dl id="l_gain">
  <dt><b>gain = <span style="font-family: monospace;">"GAIN"</span> (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gain' Line='gain = "GAIN" (apsum)' -->
  <dd>Detector gain or conversion factor between photons/electrons and
  data values.  It is specified as the number of photons per data value.
  A image header keyword (case insensitive) may be specified to get the value
  from the image.
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
  This applies only to the object spectra and not the flat field or arc
  spectra.  For more
  on this see the discussion of the saturation parameter in the
  <b>apextract</b> package.
  </dd>
  </dl>
  <dl id="l_fibers">
  <dt><b>fibers = 3 (apfind)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fibers' Line='fibers = 3 (apfind)' -->
  <dd>Number of fibers.  This number is used during the automatic definition of
  the apertures from the aperture reference spectrum.
  </dd>
  </dl>
  <dl id="l_width">
  <dt><b>width = 6. (apedit)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='width' Line='width = 6. (apedit)' -->
  <dd>Approximate base full width of the fiber profiles.  This parameter is used
  for the profile centering algorithm.
  </dd>
  </dl>
  <dl id="l_crval">
  <dt><b>crval = INDEF, cdelt = INDEF (autoidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crval' Line='crval = INDEF, cdelt = INDEF (autoidentify)' -->
  <dd>These parameters specify an approximate central wavelength and dispersion.
  They may be specified as numerical values, INDEF, or image header keyword
  names whose values are to be used.  If one or both of these parameters are
  specified as INDEF the search for a solution will be slower and more likely
  to fail.
  </dd>
  </dl>
  <dl id="l_objaps">
  <dt><b>objaps = <span style="font-family: monospace;">"2"</span>, arcaps = <span style="font-family: monospace;">"1,3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='objaps' Line='objaps = "2", arcaps = "1,3"' -->
  <dd>List of object and arc aperture numbers.  These are used to
  identify arc apertures for wavelength calibration and object apertures
  for the final results.
  </dd>
  </dl>
  <dl id="l_scattered">
  <dt><b>scattered = no (apscatter)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scattered' Line='scattered = no (apscatter)' -->
  <dd>Smooth and subtracted scattered light from the object and flat field
  images.  This operation consists of fitting independent smooth functions
  across the dispersion using data outside the fiber apertures and then
  smoothing the individual fits along the dispersion.  The initial
  flat field, or if none is given the aperture reference image, are
  done interactively to allow setting the fitting parameters.  All
  subsequent subtractions use the same fitting parameters.
  </dd>
  </dl>
  <dl id="l_fitflat">
  <dt><b>fitflat = yes (flat1d)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitflat' Line='fitflat = yes (flat1d)' -->
  <dd>Fit the composite flat field spectrum by a smooth function and divide each
  flat field spectrum by this function?  This operation removes the average
  spectral signature of the flat field lamp from the sensitivity correction to
  avoid modifying the object fluxes.
  </dd>
  </dl>
  <dl id="l_recenter">
  <dt><b>recenter = yes (aprecenter)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='recenter' Line='recenter = yes (aprecenter)' -->
  <dd>Recenter reference apertures for each object spectrum?
  </dd>
  </dl>
  <dl id="l_edit">
  <dt><b>edit = no (apedit)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='edit' Line='edit = no (apedit)' -->
  <dd>Review aperture definitions for each object spectrum?  Note that this does
  not apply to the initial reference aperture which always allows
  interactive review of the aperture definitions.
  </dd>
  </dl>
  <dl id="l_clean">
  <dt><b>clean = no (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clean' Line='clean = no (apsum)' -->
  <dd>Detect and correct for bad pixels during extraction?  This is the same
  as the clean option in the <b>apextract</b> package.  If yes this also
  implies variance weighted extraction and requires reasonably good values
  for the readout noise and gain.  In addition the datamax parameters
  can be useful.
  </dd>
  </dl>
  <dl id="l_dispcor">
  <dt><b>dispcor = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispcor' Line='dispcor = yes' -->
  <dd>Dispersion correct spectra?  Depending on the <i>params.linearize</i>
  parameter this may either resample the spectra or insert a dispersion
  function in the image header.
  </dd>
  </dl>
  <dl id="l_splot">
  <dt><b>splot = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='splot' Line='splot = yes' -->
  <dd>Plot the final spectra with the task <b>splot</b>?
  </dd>
  </dl>
  <dl id="l_redo">
  <dt><b>redo = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='redo' Line='redo = no' -->
  <dd>Redo operations previously done?  If no then previously processed spectra
  in the objects list will not be processed (unless they need to be updated).
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = yes' -->
  <dd>Update processing of previously processed spectra if aperture, flat
  field, or dispersion reference definitions are changed?
  </dd>
  </dl>
  <dl id="l_batch">
  <dt><b>batch = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='batch' Line='batch = no' -->
  <dd>Process spectra as a background or batch job provided there are no interactive
  options (<i>edit</i> and <i>splot</i>) selected.
  </dd>
  </dl>
  <dl id="l_listonly">
  <dt><b>listonly = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listonly' Line='listonly = no' -->
  <dd>List processing steps but don't process?
  </dd>
  </dl>
  <dl id="l_params">
  <dt><b>params = <span style="font-family: monospace;">""</span> (pset)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='params' Line='params = "" (pset)' -->
  <dd>Name of parameter set containing additional processing parameters.  The
  default is parameter set <b>params</b>.  The parameter set may be examined
  and modified in the usual ways (typically with <span style="font-family: monospace;">"epar params"</span> or <span style="font-family: monospace;">":e params"</span>
  from the parameter editor).  Note that using a different parameter file
  is not allowed.  The parameters are described below.
  </dd>
  </dl>
  <p style="text-align:center">-- PACKAGE PARAMETERS
  
  </p>
  <p>
  Package parameters are those which generally apply to all task in the
  package.  This is also true of <b>do3fiber</b>.
  </p>
  <dl id="l_observatory">
  <dt><b>observatory = <span style="font-family: monospace;">"observatory"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observatory' Line='observatory = "observatory"' -->
  <dd>Observatory at which the spectra were obtained if not specified in the
  image header by the keyword OBSERVAT.  For NOAO data the image headers
  identify the observatory as <span style="font-family: monospace;">"kpno"</span> or <span style="font-family: monospace;">"ctio"</span> so this parameter is not used.
  For data from other observatories this parameter may be used
  as describe in <b>observatory</b>.
  </dd>
  </dl>
  <dl id="l_interp">
  <dt><b>interp = <span style="font-family: monospace;">"poly5"</span> (nearest|linear|poly3|poly5|spline3|sinc)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interp' Line='interp = "poly5" (nearest|linear|poly3|poly5|spline3|sinc)' -->
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
  <dl id="l_dispaxis">
  <dt><b>dispaxis = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispaxis' Line='dispaxis = 2' -->
  <dd>Default dispersion axis.  The dispersion axis is 1 for dispersion
  running along image lines and 2 for dispersion running along image
  columns.  If the image header parameter DISPAXIS is defined it has
  precedence over this parameter.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"database"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "database"' -->
  <dd>Database (directory) used for storing aperture and dispersion information.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print verbose information available with various tasks.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"logfile"</span>, plotfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "logfile", plotfile = ""' -->
  <dd>Text and plot log files.  If a filename is not specified then no log is
  kept.  The plot file contains IRAF graphics metacode which may be examined
  in various ways such as with <b>gkimosaic</b>.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records = ""' -->
  <dd>Dummy parameter to be ignored.
  </dd>
  </dl>
  <dl id="l_version">
  <dt><b>version = <span style="font-family: monospace;">"KPNOCOUDE: ..."</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='version' Line='version = "KPNOCOUDE: ..."' -->
  <dd>Version of the package.
  </dd>
  </dl>
  <p style="text-align:center">PARAMS PARAMETERS
  
  </p>
  <p>
  The following parameters are part of the <b>params</b> parameter set and
  define various algorithm parameters for <b>do3fiber</b>.
  </p>
  <p style="text-align:center">--  GENERAL PARAMETERS --
  
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
  <dd>Include extra information in the output spectra?  When cleaning or using
  variance weighting the cleaned and weighted spectra are recorded in the
  first 2D plane of a 3D image, the raw, simple sum spectra are recorded in
  the second plane, and the estimated sigmas are recorded in the third plane.
  </dd>
  </dl>
  <p style="text-align:center">-- DEFAULT APERTURE LIMITS --
  
  </p>
  <dl id="l_lower">
  <dt><b>lower = -3., upper = 3. (apdefault)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lower' Line='lower = -3., upper = 3. (apdefault)' -->
  <dd>Default lower and upper aperture limits relative to the aperture center.
  These limits are used when the apertures are first found and may be
  resized automatically or interactively.
  </dd>
  </dl>
  <p style="text-align:center">-- AUTOMATIC APERTURE RESIZING PARAMETERS --
  
  </p>
  <dl id="l_ylevel">
  <dt><b>ylevel = 0.05 (apresize)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ylevel' Line='ylevel = 0.05 (apresize)' -->
  <dd>Data level at which to set aperture limits during automatic resizing.
  It is a fraction of the peak relative to a local background.
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
  <p style="text-align:center">-- SCATTERED LIGHT PARAMETERS --
  
  </p>
  <dl id="l_buffer">
  <dt><b>buffer = 1. (apscatter)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='buffer' Line='buffer = 1. (apscatter)' -->
  <dd>Buffer distance from the aperture edges to be excluded in selecting the
  scattered light pixels to be used.
  </dd>
  </dl>
  <dl id="l_apscat1">
  <dt><b>apscat1 = <span style="font-family: monospace;">""</span> (apscatter)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apscat1' Line='apscat1 = "" (apscatter)' -->
  <dd>Fitting parameters across the dispersion.  This references an additional
  set of parameters for the ICFIT package.  The default is the <span style="font-family: monospace;">"apscat1"</span>
  parameter set.
  </dd>
  </dl>
  <dl id="l_apscat2">
  <dt><b>apscat2 = <span style="font-family: monospace;">""</span> (apscatter)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apscat2' Line='apscat2 = "" (apscatter)' -->
  <dd>Fitting parameters along the dispersion.  This references an additional
  set of parameters for the ICFIT package.  The default is the <span style="font-family: monospace;">"apscat2"</span>
  parameter set.
  </dd>
  </dl>
  <p style="text-align:center">-- APERTURE EXTRACTION PARAMETERS --
  
  </p>
  <dl id="l_weights">
  <dt><b>weights = <span style="font-family: monospace;">"none"</span> (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='weights' Line='weights = "none" (apsum)' -->
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
  <dt><b>pfit = <span style="font-family: monospace;">"fit1d"</span> (apsum) (fit1d|fit2d)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pfit' Line='pfit = "fit1d" (apsum) (fit1d|fit2d)' -->
  <dd>Profile fitting algorithm for cleaning and variance weighted extractions.
  The default is generally appropriate for most data but users
  may try the other algorithm.  See <b>approfiles</b> for further information.
  </dd>
  </dl>
  <dl id="l_lsigma">
  <dt><b>lsigma = 3., usigma = 3. (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lsigma' Line='lsigma = 3., usigma = 3. (apsum)' -->
  <dd>Lower and upper rejection thresholds, given as a number of times the
  estimated sigma of a pixel, for cleaning.
  </dd>
  </dl>
  <dl id="l_nsubaps">
  <dt><b>nsubaps = 1 (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsubaps' Line='nsubaps = 1 (apsum)' -->
  <dd>During extraction it is possible to equally divide the apertures into
  this number of subapertures.
  </dd>
  </dl>
  <p style="text-align:center">-- FLAT FIELD FUNCTION FITTING PARAMETERS --
  
  </p>
  <dl id="l_f_interactive">
  <dt><b>f_interactive = yes (fit1d)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='f_interactive' Line='f_interactive = yes (fit1d)' -->
  <dd>Fit the composite one dimensional flat field spectrum interactively?
  This is used if <i>fitflat</i> is set and a two dimensional flat field
  spectrum is specified.
  </dd>
  </dl>
  <dl id="l_f_function">
  <dt><b>f_function = <span style="font-family: monospace;">"spline3"</span>, f_order = 20 (fit1d)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='f_function' Line='f_function = "spline3", f_order = 20 (fit1d)' -->
  <dd>Function and order used to fit the composite one dimensional flat field
  spectrum.  The functions are <span style="font-family: monospace;">"legendre"</span>, <span style="font-family: monospace;">"chebyshev"</span>, <span style="font-family: monospace;">"spline1"</span>, and
  <span style="font-family: monospace;">"spline3"</span>.  The spline functions are linear and cubic splines with the
  order specifying the number of pieces.
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
  <dd>The maximum difference for a match between the dispersion function prediction
  value and a wavelength in the coordinate list.
  </dd>
  </dl>
  <dl id="l_fwidth">
  <dt><b>fwidth = 3.5 (autoidentify/identify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fwidth' Line='fwidth = 3.5 (autoidentify/identify)' -->
  <dd>Approximate full base width (in pixels) of arc lines.
  </dd>
  </dl>
  <dl id="l_cradius">
  <dt><b>cradius = 4. (reidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cradius' Line='cradius = 4. (reidentify)' -->
  <dd>Radius from previous position to reidentify arc line.
  </dd>
  </dl>
  <dl id="l_i_function">
  <dt><b>i_function = <span style="font-family: monospace;">"legendre"</span>, i_order = 3 (autoidentify/identify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='i_function' Line='i_function = "legendre", i_order = 3 (autoidentify/identify)' -->
  <dd>The default function and order to be fit to the arc wavelengths as a
  function of the pixel coordinate.  The functions choices are <span style="font-family: monospace;">"chebyshev"</span>,
  <span style="font-family: monospace;">"legendre"</span>, <span style="font-family: monospace;">"spline1"</span>, or <span style="font-family: monospace;">"spline3"</span>.
  </dd>
  </dl>
  <dl id="l_i_niterate">
  <dt><b>i_niterate = 3, i_low = 3.0, i_high = 3.0 (autoidentify/identify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='i_niterate' Line='i_niterate = 3, i_low = 3.0, i_high = 3.0 (autoidentify/identify)' -->
  <dd>Number of rejection iterations and sigma thresholds for rejecting arc
  lines from the dispersion function fits.
  </dd>
  </dl>
  <dl id="l_refit">
  <dt><b>refit = yes (reidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refit' Line='refit = yes (reidentify)' -->
  <dd>Refit the dispersion function?  If yes and there is more than 1 line
  and a dispersion function was defined in the arc reference then a new
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
  <dt><b>sort = <span style="font-family: monospace;">"jd"</span>, group = <span style="font-family: monospace;">"ljd"</span> (refspectra)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sort' Line='sort = "jd", group = "ljd" (refspectra)' -->
  <dd>Image header keywords to be used as the sorting parameter for selection
  based on order and to group spectra.
  A null string, <span style="font-family: monospace;">""</span>, or the word <span style="font-family: monospace;">"none"</span> may be use to disable the sorting
  or grouping parameters.
  The sorting parameter
  must be numeric but otherwise may be anything.  The grouping parameter
  may be a string or number and must simply be the same for all spectra within
  the same group (say a single night).
  Common sorting parameters are times or positions.
  In <b>do3fiber</b> the Julian date (JD) and the local Julian day number (LJD)
  at the middle of the exposure are automatically computed from the universal
  time at the beginning of the exposure and the exposure time.  Also the
  parameter UTMIDDLE is computed.
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
  spectra will be interpolated to a linear or log linear sampling
  If no the nonlinear dispersion function(s) from the dispersion function
  database are assigned to the input image world coordinate system
  and the spectral data are not interpolated.
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
  The <b>do3fiber</b> reduction task is specialized for scattered light
  subtraction, extraction, flat
  fielding, and wavelength calibration of multifiber data in which some
  fibers are used to take object spectra and other fibers are used to
  take simultaneous arc spectra.  A three fiber instrument of this
  type (one object and two arc fibers) is available at the KPNO coude feed.
  The default parameters are set for this configuration.
  If there are a large number of fibers and fiber throughput and sky
  fiber subtraction is needed the <b>dofiber</b> task should be used.
  </p>
  <p>
  The <b>do3fiber</b> task is a command language script which collects
  and combines the functions and parameters of many general purpose tasks to
  provide a single complete data reduction path.  The task provides a degree
  of guidance, automation, and record keeping necessary when dealing with
  this type of multifiber data.
  </p>
  <p>
  The general organization of the task is to do the interactive setup steps
  first using representative calibration data and then perform the majority
  of the reductions automatically, and possibly as a background process, with
  reference to the setup data.  In addition, the task determines which setup
  and processing operations have been completed in previous executions of the
  task and, contingent on the <i>redo</i> and <i>update</i> options, skip or
  repeat some or all the steps.
  </p>
  <p>
  The description is divided into a quick usage outline followed by details
  of the parameters and algorithms.  The usage outline is provided as a
  checklist and a refresher for those familiar with this task and the
  component tasks.  It presents only the default or recommended usage.  Since
  <b>do3fiber</b> combines many separate, general purpose tasks the
  description given here refers to these tasks and leaves some of the details
  to their help documentation.
  </p>
  <p>
  <b>Usage Outline</b>
  </p>
  <dl>
  <dt><b>[1]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[1]' -->
  <dd>The images are first processed with <b>ccdproc</b> for overscan,
  bias, and dark corrections.
  The <b>do3fibers</b> task will abort if the image header keyword CCDPROC,
  which is added by <b>ccdproc</b>, is missing.  If the data processed outside
  of the IRAF <b>ccdred</b> package then a dummy CCDPROC keyword should be
  added to the image headers; say with <b>hedit</b>.
  </dd>
  </dl>
  <dl>
  <dt><b>[2]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[2]' -->
  <dd>Set the <b>do3fiber</b> parameters with <b>eparam</b>.  Specify the object
  images to be processed, the flat field image as the aperture reference and
  the flat field, and one or more arc images.  If there are many
  object or arc spectra per setup you might want to prepare <span style="font-family: monospace;">"@ files"</span>.
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
  such queries during the execution and no further queries of that
  type will be made.
  </dd>
  </dl>
  <dl>
  <dt><b>[4]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[4]' -->
  <dd>The apertures are defined using the specified aperture reference image
  which is usually a flat field in which both the object and arc fibers are
  illuminated.  The specified number of fibers are found automatically and
  sequential apertures assigned.
  </dd>
  </dl>
  <dl>
  <dt><b>[5]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[5]' -->
  <dd>A query is given allowing the apertures to be interactively reviewed.
  In this mode one may adjust the aperture widths as desired either
  explicitly (:lower and :upper), with the cursor (<span style="font-family: monospace;">'l'</span> and <span style="font-family: monospace;">'u'</span>), at a
  particular flux level (<span style="font-family: monospace;">'y'</span>), or with an automatic algorithm (<span style="font-family: monospace;">'z'</span>)
  as described by <b>apresize</b>.  To exit type <span style="font-family: monospace;">'q'</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>[6]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[6]' -->
  <dd>The fiber positions at a series of points along the dispersion are measured
  and a function is fit to these positions.  This may be done interactively to
  adjust the fitting parameters.  Not all fibers need be examined and the <span style="font-family: monospace;">"NO"</span>
  response will quit the interactive fitting.  To exit the interactive
  fitting type <span style="font-family: monospace;">'q'</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>[7]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[7]' -->
  <dd>If scattered light subtraction is to be done the flat field image is
  used to define the scattered light fitting parameters interactively.
  If one is not specified then the aperture reference image is used for
  this purpose.
  There are two queries for the interactive fitting.  A graph of the
  data between the defined reference apertures separated by a specified
  buffer distance is first shown.  The function order and type may be
  adjusted.  After quiting with <span style="font-family: monospace;">'q'</span> the user has the option of changing
  the buffer value and returning to the fitting, changing the image line
  or column to check if the fit parameters are satisfactory at other points,
  or to quit and accept the fit parameters.  After fitting all points
  across the dispersion another graph showing the scattered light from
  the individual fits is shown and the smoothing parameters along the
  dispersion may be adjusted.  Upon quiting with <span style="font-family: monospace;">'q'</span> you have the option
  of checking other cuts parallel to the dispersion or quiting and finishing
  the scattered light function smoothing and subtraction.
  If there is a throughput image then this is corrected for scattered light
  noninteractively using the previous fitting parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>[8]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[8]' -->
  <dd>If flat fielding is to be done the flat field spectra are extracted.  The
  average spectrum over all fibers is determined and a function is fit
  interactively (exit with <span style="font-family: monospace;">'q'</span>).  This function is generally of sufficiently
  high order that the overall shape is well fit.  This function is then used
  to normalize the individual flat field spectra.
  The final response spectra are normalized to a unit
  mean over all fibers.
  </dd>
  </dl>
  <dl>
  <dt><b>[9]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[9]' -->
  <dd>If dispersion correction is selected the first arc in the arc list is
  extracted.  The middle fiber is used to identify the arc lines and define
  the dispersion function using the task <b>autoidentify</b>.  The
  <i>crval</i> and <i>cdelt</i> parameters are used in the automatic
  identification.  Whether or not the automatic identification is
  successful you will be shown the result of the arc line identification.
  If the automatic identification is not successful identify a few arc
  lines with <span style="font-family: monospace;">'m'</span> and use the <span style="font-family: monospace;">'l'</span> line list identification command to
  automatically add additional lines and fit the dispersion function.  Check
  the quality of the dispersion function fit with <span style="font-family: monospace;">'f'</span>.  When satisfied exit
  with <span style="font-family: monospace;">'q'</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>[10]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[10]' -->
  <dd>The remaining fibers are automatically reidentified.  You have the option
  to review the line identifications and dispersion function for each fiber
  and interactively add or delete arc lines and change fitting parameters.
  This can be done selectively, such as when the reported RMS increases
  significantly.
  </dd>
  </dl>
  <dl>
  <dt><b>[11]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[11]' -->
  <dd>If the spectra are to be resampled to a linear dispersion system
  (which will be the same for all spectra) default dispersion parameters
  are printed and you are allowed to adjust these as desired.
  </dd>
  </dl>
  <dl>
  <dt><b>[12]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[12]' -->
  <dd>The object spectra are now automatically scattered light subtracted,
   extracted, flat fielded, and dispersion corrected.
  The reference apertures are first assigned
  to the object spectra.  If the <i>recenter</i> option is set the apertures
  will have a shift applied based on recentering the fiber profiles.
  If the <i>edit</i> option is set you may review and modify
  the aperture definitions interactively.  Any new
  arcs assigned to the object images are automatically extracted and
  dispersion functions determined.  A zero point wavelength correction
  is computed from the arc fiber spectra and applied to the object spectrum.
  </dd>
  </dl>
  <dl>
  <dt><b>[13]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[13]' -->
  <dd>The option to examine the final spectra with <b>splot</b> may be given.
  To exit type <span style="font-family: monospace;">'q'</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>[14]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[14]' -->
  <dd>If scattered light is subtracted from the input data a copy of the
  original image is made by appending <span style="font-family: monospace;">"noscat"</span> to the image name.
  If the data are reprocessed with the <i>redo</i> flag the original
  image will be used again to allow modification of the scattered
  light parameters.
  The final spectra will have the same name as the original 2D images
  with a <span style="font-family: monospace;">".ms"</span> extension added.
  </dd>
  </dl>
  <p>
  <b>Spectra and Data Files</b>
  </p>
  <p>
  The basic input consists of multifiber object and calibration spectra
  stored as IRAF images.  The type of image format is defined by the
  environment parameter <i>imtype</i>.  Only images with that extension will
  be processed and created.
  There are two types of calibration images.  These
  are flat fields and comparison lamp arc spectra.  The raw CCD images must
  be processed to remove overscan, bias, and dark count effects.  This is
  generally done using the <b>ccdred</b> package.
  The <b>do3fiber</b> task will abort if the image header keyword CCDPROC,
  which is added by <b>ccdproc</b>, is missing.  If the data processed outside
  of the IRAF <b>ccdred</b> package then a dummy CCDPROC keyword should be
  added to the image headers; say with <b>hedit</b>.
  Flat fielding is generally
  not done at this stage but as part of <b>do3fiber</b>.  If for some reason
  the flat field or calibration arc spectra have separate exposures through
  different fibers they may be simply added.
  </p>
  <p>
  The assignment of arc calibration exposures to object exposures is
  generally done by selecting the nearest in time and interpolating.
  However, the optional <i>arc assignment table</i> may be used to explicitly
  assign arc images to specific objects.  The format of this file is
  described in the task <b>refspectra</b>.
  </p>
  <p>
  The final reduced spectra are recorded in one, two or three dimensional IRAF
  images.  The images have the same name as the original images with an added
  <span style="font-family: monospace;">".ms"</span> extension.  Each line in the reduced image is a one dimensional
  spectrum with associated aperture, wavelength, and identification
  information.  With a single object spectrum the image will be one dimensional
  and with multiple object spectra the image will be two dimensional.
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
  The <b>kpnocoude</b> package parameters set parameters affecting all the tasks
  in the package.  Some of the parameters are not applicable to the
  <b>do3fiber</b> task.  The observatory parameter is only required for data
  without an OBSERVAT header parameter (currently included in NOAO data).
  The spectrum interpolation type might be changed to <span style="font-family: monospace;">"sinc"</span> but with the
  cautions given in <b>onedspec.package</b>.  The dispersion axis parameter is
  only needed if a DISPAXIS image header parameter is not defined.  The other
  parameters define the standard I/O functions.  The verbose parameter
  selects whether to print everything which goes into the log file on the
  terminal.  It is useful for monitoring what the <b>do3fiber</b> task does.  The
  log and plot files are useful for keeping a record of the processing.  A
  log file is highly recommended.  A plot file provides a record of
  apertures, traces, and extracted spectra but can become quite large.
  The plotfile is most conveniently viewed and printed with <b>gkimosaic</b>.
  </p>
  <p>
  <b>Processing Parameters</b>
  </p>
  <p>
  The input images are specified by image lists.  The lists may be
  a list of explicit, comma separate image names, @ files, or image
  templates using pattern matching against file names in the directory.
  The aperture reference spectrum is used to find the spectrum profiles and trace
  them.  Thus, this requires an image with good signal in all fibers
  which usually means a flat field spectrum.  It is recommended that
  flat field correction be done using one dimensional extracted spectra
  rather than as two dimensional images.  This is done if a flat field
  spectrum is specified.  The arc assignment table is used to specifically
  assign arc spectra to particular object spectra and the format
  of the file is described in <b>refspectra</b>.
  </p>
  <p>
  The detector read out noise and gain are used for cleaning and variance
  (optimal) extraction.  The dispersion axis defines the wavelength direction
  of spectra in the image if not defined in the image header by the keyword
  DISPAXIS.  The width parameter (in pixels) is used for the profile finding and
  centering algorithm (<b>center1d</b>).
  </p>
  <p>
  The number of fibers is fairly obvious.  It is the number of
  fibers, including the arc fibers, to be automatically found and
  assigned apertures.  The apertures are assigned aperture
  numbers sequentially.  The object and arc fibers are identified
  by these aperture numbers as specified by the <i>objaps</i> and
  <i>arcaps</i> parameters.  The defaults are for the case of three
  fibers in the sequence arc fiber, object fiber, and arc fiber.
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
  scattered light option allows fitting and subtracting a scattered light
  surface from the input object and flat field.  If there is significant
  scattered light which is not subtracted the fiber throughput correction
  will not be accurate.  The
  flat fitting option allows fitting and removing the overall shape of the
  flat field spectra while preserving the pixel-to-pixel response
  corrections.  This is useful for maintaining the approximate object count
  levels and not introducing the reciprocal of the flat field spectrum into
  the object spectra.
  </p>
  <p>
  The apertures defined for the aperture reference image are assigned to
  each image.  For the object images the apertures may be shifted across
  the dispersion by recentering the strongest profiles and averaging
  the individual shifts to form a single shift for all apertures.  This
  corrects for shifts in the detector during the observations.  The
  <i>recenter</i> parameter selects whether to apply this shift or not.
  </p>
  <p>
  The <i>edit</i> option allows you to be queried to review the apertures
  assigned to each object image.  If selected and the query answered
  affirmatively the apertures may be interactively shifted and resized.  The
  query may also be answered with <span style="font-family: monospace;">"NO"</span> to turn off this option during
  processing.  Note that the initial aperture definitions for the aperture
  reference image always allows editing.
  </p>
  <p>
  The <i>clean</i> option invokes a profile fitting and deviant
  point rejection algorithm as well as a variance weighting of points in the
  aperture.  These options require knowing the effective (i.e. accounting for
  any image combining) read out noise and gain.  For a discussion of cleaning
  and variance weighted extraction see <b>apvariance</b> and
  <b>approfiles</b>.
  </p>
  <p>
  The dispersion correction option selects whether to extract arc spectra,
  determine dispersion functions, assign them to the object spectra, and,
  possibly, resample the spectra to a linear (or log-linear) wavelength
  scale.
  </p>
  <p>
  The <i>splot</i> option allows a query (which may be answered with <span style="font-family: monospace;">"YES"</span>
  or <span style="font-family: monospace;">"NO"</span> to eliminate the query) and then plotting of the final object
  spectra if answered affirmatively.  The plotting is done with the
  task <b>splot</b>.
  </p>
  <p>
  Generally once a spectrum has been processed it will not be reprocessed if
  specified as an input spectrum.  However, changes to the underlying
  calibration data can cause such spectra to be reprocessed if the
  <i>update</i> flag is set.  The changes which will cause an update are a new
  reference image, new flat field, and a new arc reference image.  If all
  input spectra are to be processed regardless of previous processing the
  <i>redo</i> flag may be used.  Note that reprocessing clobbers the
  previously processed output spectra.
  </p>
  <p>
  The <i>batch</i> processing option allows object spectra to be processed as
  a background or batch job.  This will only occur if the aperture editing
  and final spectrum plotting have been turned off, either with the task
  option parameter or by answering <span style="font-family: monospace;">"NO"</span> to the queries.  The <i>listonly</i>
  option prints a summary of the processing steps which will be performed on
  the input spectra without actually doing anything.  This is useful for
  verifying which spectra will be affected if the input list contains
  previously processed spectra.  The listing does not include any arc spectra
  which may be extracted to dispersion calibrate an object spectrum.
  </p>
  <p>
  The last parameter (excluding the task mode parameter) points to another
  parameter set for the algorithm parameters.  The way <b>do3fiber</b> works
  this may not have any value and the parameter set <b>params</b> is always
  used.  The algorithm parameters are discussed further in the next section.
  </p>
  <p>
  <b>Algorithms and Algorithm Parameters</b>
  </p>
  <p>
  This section summarizes the various algorithms used by the <b>do3fiber</b>
  task and the parameters which control and modify the algorithms.  The
  algorithm parameters available to the user are collected in the parameter
  set <b>params</b>.  These parameters are taken from the various general
  purpose tasks used by the <b>do3fiber</b> processing task.  Additional
  information about these parameters and algorithms may be found in the help
  for the actual task executed.  These tasks are identified in the parameter
  section listing in parenthesis.  The aim of this parameter set organization
  is to collect all the algorithm parameters in one place separate from the
  processing parameters and include only those which are relevant for
  this type of data.  The parameter values can be changed from the
  defaults by using the parameter editor,
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epar params
  </pre></div>
  <p>
  or simple typing <i>params</i>.  The parameter editor can also be
  entered when editing the <b>do3fiber</b> parameters by typing <i>:e
  params</i> or simply <i>:e</i> if positioned at the <i>params</i>
  parameter.
  </p>
  <p>
  <b>Aperture Definitions</b>
  </p>
  <p>
  The first operation is to define the extraction apertures, which include
  the aperture width and position dependence with wavelength, for the object
  and arc fibers.  This is done on a reference spectrum which is usually a
  flat field taken through both fibers.  Other spectra will inherit the
  reference apertures and may apply a correction for any shift of the orders
  across the dispersion.  The reference apertures are defined only once
  unless the <i>redo</i> option is set.
  </p>
  <p>
  The selected number of fibers are found automatically by selecting the
  highest peaks in a cut across the dispersion.  Apertures are assigned with
  a limits set by the <i>lower</i> and <i>upper</i> parameter and numbered
  sequentially.  A query is then given allowing the apertures to be reviewed
  interactively.  If answered affirmatively a cut across the orders is shown
  with the apertures marked and an interactive aperture editing mode is
  entered (see <b>apedit</b>).  The main thing to be concerned about is that
  the aperture numbers agree with the <i>objaps</i> and <i>arcaps</i>
  definitions.  The aperture numbers may be changed with the <span style="font-family: monospace;">'i'</span> or <span style="font-family: monospace;">'o'</span>
  keys.  The apertures may also be resized from the default limits.
  To exit the background and aperture editing steps type <span style="font-family: monospace;">'q'</span>.
  </p>
  <p>
  Next the positions of the fiber profiles at various points along the
  dispersion are measured and a <span style="font-family: monospace;">"trace function"</span> is fit.  The user is asked
  whether to fit the trace function interactively.  This is selected to
  adjust the fitting parameters such as function type and order.  When
  interactively fitting a query is given for each aperture.  After the first
  aperture one may skip reviewing the other traces by responding with <span style="font-family: monospace;">"NO"</span>.
  Queries made by <b>do3fiber</b> generally may be answered with either lower
  case <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"no"</span> or with upper case <span style="font-family: monospace;">"YES"</span> or <span style="font-family: monospace;">"NO"</span>.  The upper case
  responses apply to all further queries and so are used to eliminate further
  queries of that kind.
  </p>
  <p>
  The above steps are all performed using tasks from the <b>apextract</b>
  package and parameters from the <b>params</b> parameters.  As a quick
  summary, the dispersion direction of the spectra are determined from the
  package <b>dispaxis</b> parameter if not defined in the image header.  The default
  line or column for finding the orders and the number of image lines or
  columns to sum are set by the <i>line</i> and <i>nsum</i> parameters.  A line
  of INDEF (the default) selects the middle of the image.  The automatic
  finding algorithm is described for the task <b>apfind</b> and basically
  finds the strongest peaks.  The tracing is done as described in
  <b>aptrace</b> and consists of stepping along the image using the specified
  <i>t_step</i> parameter.  The function fitting uses the <b>icfit</b> commands
  with the other parameters from the tracing section.
  </p>
  <p>
  <b>Extraction</b>
  </p>
  <p>
  The actual extraction of the spectra is done by summing across the fixed
  width apertures at each point along the dispersion.  The default is to
  simply sum the pixels using partial pixels at the ends.  There is an
  option to weight the sum based on a Poisson noise model using the
  <i>readnoise</i> and <i>gain</i> detector parameters.  Note that if the
  <i>clean</i> option is selected the variance weighted extraction is used
  regardless of the <i>weights</i> parameter.  The sigma thresholds for
  cleaning are also set in the <b>params</b> parameters.
  </p>
  <p>
  The cleaning and variance weighting options require knowing the effective
  (i.e. accounting for any image combining) read out noise and gain.  These
  numbers need to be adjusted if the image has been processed such that the
  intensity scale has a different origin (such as a background light
  subtraction) or scaling (such as caused by unnormalized flat fielding).
  For optimal extraction and cleaning to work it is recommended that
  a <i>datamax</i> value be determined for the data and the
  <i>fitflat</i> option be used.  For further discussion of cleaning and
  variance weighted extraction see <b>apvariance</b> and <b>approfiles</b> as
  well as  <b>apsum</b>.
  </p>
  <p>
  <b>Scattered Light Subtraction</b>
  </p>
  <p>
  Scattered light may be subtracted from the input two dimensional image as
  the first step.  This is done using the algorithm described in
  <b>apscatter</b>.  This can be important if there is significant scattered
  light since the flat field/throughput correction will otherwise be
  incorrect.  The algorithm consists of fitting a function to the data
  outside the defined apertures by a specified <i>buffer</i> at each line or
  column across the dispersion.  The function fitting parameters are the same
  at each line.  Because the fitted functions are independent at each line or
  column a second set of one dimensional functions are fit parallel to the
  dispersion using the evaluated fit values from the cross-dispersion step.
  This produces a smooth scattered light surface which is finally subtracted
  from the input image.  Again the function fitting parameters are the
  same at each line or column though they may be different than the parameters
  used to fit across the dispersion.
  </p>
  <p>
  The first time the task is run with a particular flat field (or aperture
  reference image if no flat field is used) the scattered light fitting
  parameters are set interactively using that image.  The interactive step
  selects a particular line or column upon which the fitting is done
  interactively with the <b>icfit</b> commands.  A query is first issued
  which allows skipping this interactive stage.  Note that the interactive
  fitting is only for defining the fitting functions and orders.  When
  the graphical <b>icfit</b> fitting is exited (with <span style="font-family: monospace;">'q'</span>) there is a second prompt
  allowing you to change the buffer distance (in the first cross-dispersion
  stage) from the apertures, change the line/column, or finally quit.
  </p>
  <p>
  The initial fitting parameters and the final set parameters are recorded
  in the <b>apscat1</b> and <b>apscat2</b> hidden parameter sets.  These
  parameters are then used automatically for every subsequent image
  which is scattered light corrected.
  </p>
  <p>
  The scattered light subtraction modifies the input 2D images.  To preserve
  the original data a copy of the original image is made with the same
  root name and the word <span style="font-family: monospace;">"noscat"</span> appended.  The scattered light subtracted
  images will have the header keyword <span style="font-family: monospace;">"APSCATTE"</span> which is how the task
  avoids repeating the scattered light subtraction during any reprocessing.
  However if the <i>redo</i> option is selected the scattered light subtraction
  will also be redone by first restoring the <span style="font-family: monospace;">"noscat"</span> images to the original
  input names.
  </p>
  <p>
  <b>Flat Field Correction</b>
  </p>
  <p>
  Flat field corrections may be made during the basic CCD processing; i.e.
  direct division by the two dimensional flat field observation.  In that
  case do not specify a flat field spectrum; use the null string <span style="font-family: monospace;">""</span>.  The
  <b>do3fiber</b> task provides an alternative flat field response correction
  based on division of the extracted object spectra by the extracted flat field
  spectra.  A discussion of the theory and merits of flat fielding directly
  verses using the extracted spectra will not be made here.  The
  <b>do3fiber</b> flat fielding algorithm is the <i>recommended</i> method for
  flat fielding since it works well and is not subject to the many problems
  involved in two dimensional flat fielding.
  </p>
  <p>
  The first step is extraction of the flat field spectrum, if specified,
  using the reference apertures.  Only one flat field is allowed so if
  multiple flat fields are required the data must be reduced in groups.
  If the <i>fitflat</i>
  option is selected (the default) the extracted flat field spectra are
  averaged together and a smooth function is fit.  The default fitting
  function and order are given by the parameters <i>f_function</i> and
  <i>f_order</i>.  If the parameter <i>f_interactive</i> is <span style="font-family: monospace;">"yes"</span> then the
  fitting is done interactively using the <b>fit1d</b> task which uses the
  <b>icfit</b> interactive fitting commands.
  </p>
  <p>
  The fitted function is divided into the individual flat field spectra to
  remove the basic shape of the spectrum while maintaining the relative
  individual pixel responses and any fiber to fiber differences.  This step
  avoids introducing the flat field spectrum shape into the object spectra
  and closely preserves the object counts.
  </p>
  <p>
  The final step is to normalize the flat field spectra by the mean counts over
  all the fibers.  This normalization step is simply to preserve the average
  counts of the extracted object and arc spectra after division by the
  response spectra.
  </p>
  <p>
  <b>Dispersion Correction</b>
  </p>
  <p>
  If dispersion correction is not selected, <i>dispcor</i>=no, then the object
  spectra are simply extracted.  If it is selected the arc spectra are used
  to dispersion calibrate the object spectra.  There are four steps involved;
  determining the dispersion functions relating pixel position to wavelength,
  assigning the appropriate dispersion functions to a particular observation,
  determining a zero point wavelength shift from the arc fibers to be applied
  to the object fiber dispersion functions, and either storing the nonlinear
  dispersion function in the image headers or resampling the spectra to
  evenly spaced pixels in wavelength.
  </p>
  <p>
  The first arc spectrum in the arc list is used to define the reference
  dispersion solution.  It is extracted using the reference aperture
  definitions.  The interactive task <b>autoidentify</b> is used to
  automatically define the dispersion function in one fiber.  Whether or not
  it is successful the user is presented with the interactive identification
  graph.  The automatic identifications can be reviewed and a new solution or
  corrections to the automatic solution may be performed.  The dispersion
  functions for the other fibers are then determined automatically by
  reference to the first fiber using the task <b>reidentify</b>.  Except in
  batch mode a query is given allowing the reidentified arc spectra to be
  examined interactively with <b>identify</b>.  This would normally be done
  only if the information about the reidentification printed on the terminal
  indicates a problem such as a large increase in the RMS.  This query may be
  eliminated in the usual way.
  </p>
  <p>
  The set of arc dispersion function parameters are from <b>autoidentify</b> and
  <b>reidentify</b>.  The parameters define a line list for use in
  automatically assigning wavelengths to arc lines, a parameter controlling
  the width of the centering window (which should match the base line
  widths), the dispersion function type and order, parameters to exclude bad
  lines from function fits, and parameters defining whether to refit the
  dispersion function, as opposed to simply determining a zero point shift,
  and the addition of new lines from the line list when reidentifying
  additional arc spectra.  The defaults should generally be adequate and the
  dispersion function fitting parameters may be altered interactively.  One
  should consult the help for the two tasks for additional details of these
  parameters and the operation of <b>autoidentify</b>.
  </p>
  <p>
  If resampling of the spectra is selected by the parameter <i>linearize</i>
  all the arc dispersion functions are combined to provide a default
  starting and ending wavelength and dispersion with the same number of
  pixels is determined and the user is queried for any changes.  This
  linear dispersion system will be applied to all spectra so that all
  the final processed object spectra will have the same dispersion
  sampling.
  </p>
  <p>
  Once the reference dispersion functions are defined other arc spectra are
  extracted as they are assign to the object spectra.  The assignment of
  arcs is done either explicitly with an arc assignment table (parameter
  <i>arctable</i>) or based on a header parameter such as a time.
  The assignments are made by the task <b>refspectra</b>.  When two arcs are
  assigned to an object spectrum an interpolation is done between the two
  dispersion functions.  This makes an approximate correction for steady
  drifts in the dispersion.  Because the arc fibers monitor any zero point
  shifts in the dispersion functions, due to translation and rotation of the
  detector, it is probably only necessary to have one or two arc spectra, one
  at the beginning and/or one at the end of the night.
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
  When the object spectra are extracted so are the simultaneous arc spectra.
  A zero point shift of the arc spectra relative to the dispersion solutions
  of an assigned full arc observation is computed using <b>reidentify</b>.
  The zero point shifts from the arc fibers are then
  interpolated across the detector based on the positions of the arc
  apertures to the positions of the object apertures.  A linear interpolation
  is used which accounts for a rotation of the detector as well as a
  translation along the dispersion.  The interpolated zero point wavelength
  shifts are then added to the dispersion functions from the full arc
  observation for the object fibers.  Note that this does not assume that the
  object and arc fiber dispersion functions are the same or have the same
  wavelength origin, but only that the interpolated shifts in wavelength zero
  point apply to all fibers.  When there are two assigned full arc spectra
  the above steps are done independently and the final pair of zero point
  corrected dispersion functions for each object fiber are combined using the
  assigned weights.  Once the dispersion function correction is determined
  from the extracted arc fiber spectra they are deleted leaving only the
  object spectra.
  </p>
  <p>
  The last step of dispersion correction is setting the dispersion
  of the object spectra.  There are two choices here.
  If the <i>linearize</i> parameter is not set the nonlinear dispersion
  functions are stored in the image header.  Other IRAF tasks interpret
  this information when dispersion coordinates are needed for plotting
  or analysis.  This has the advantage of not requiring the spectra
  to be interpolated and the disadvantage that the dispersion
  information is only understood by IRAF tasks and cannot be readily
  exported to other analysis software.
  </p>
  <p>
  If the <i>linearize</i> parameter is set then the spectra are resampled to a
  linear dispersion relation either in wavelength or the log of the
  wavelength.  The linear dispersion parameters are those defined
  previously for the arc reference image.
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
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  The following example uses artificial data and may be executed
  at the terminal (with IRAF V2.10).  This is also the sequence performed
  by the test procedure <span style="font-family: monospace;">"demos do3fiber"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  kp&gt; demos mkdo3fiber
  Creating image demoobj ...
  Creating image demoflat ...
  Creating image demoarc ...
  kp&gt; do3fiber demoobj apref=demoflat flat=demoflat arcs=demoarc \
  &gt;&gt;&gt; width=4 edit=yes
  Set reference apertures for demoflat
  Resize apertures for demoflat?  (yes):
  Edit apertures for demoflat?  (yes):
  &lt;Exit with <span style="font-family: monospace;">'q'</span>&gt;
  Fit traced positions for demoflat interactively?  (yes):
  Fit curve to aperture 1 of demoflat interactively  (yes):
  &lt;Exit with <span style="font-family: monospace;">'q'</span>&gt;
  Fit curve to aperture 2 of demoflat interactively  (yes): N
  Create response function demoflatnorm.ms
  Extract flat field demoflat
  Fit and ratio flat field demoflat
  Create the normalized response demoflatnorm.ms
  demoflatnorm.ms -&gt; demoflatnorm.ms  using bzero: 0.  and bscale: 1.
      mean: 1.  median: 1.034214  mode: 0.8378798
      upper: INDEF  lower: INDEF
  Average aperture response:
  1.  0.8394014
  2.  1.034403
  3.  1.126194
  Extract arc reference image demoarc
  Determine dispersion solution for demoarc
  &lt;Reset default line list with ":coord linelists$idhenear.dat"&gt;
  &lt;A dispersion solution is found automatically.&gt;
  &lt;Examine the fit with <span style="font-family: monospace;">'f'</span>&gt;
  &lt;Exit fit with <span style="font-family: monospace;">'q'</span> and exit task with <span style="font-family: monospace;">'q'</span>&gt;
  
  REIDENTIFY: NOAO/IRAF V2.10BETA valdes@puppis Fri 11:04:32 06-Mar-92
    Reference image = demoarc.ms, New image = demoarc.ms, Refit = yes
       Image Data Found    Fit Pix Shift  User Shift  Z Shift     RMS
  d...ms - Ap 1   30/30  29/30  -0.00675       -0.04  -6.9E-6   0.252
  Fit dispersion function interactively? (no|yes|NO|YES) (yes): n
  d...ms - Ap 3   30/30  29/30   -0.0154     -0.0928  -1.4E-5   0.303
  Fit dispersion function interactively? (no|yes|NO|YES) (no): y
  &lt;Exit with <span style="font-family: monospace;">'q'</span>&gt;
  d...ms - Ap 3   30/30  29/30   -0.0154     -0.0928  -1.4E-5   0.303
  
  Dispersion correct demoarc
  d...ms: w1 = 5785.86, w2 = 7351.59, dw = 6.14, nw = 256
    Change wavelength coordinate assignments? (yes|no|NO): N
  Extract object spectrum demoobj
  Edit apertures for demoobj?  (yes): n
  Assign arc spectra for demoobj
  [demoobj] refspec1='demoarc'
  Reidentify arc fibers in demoobj with respect to demoarc
  
  REIDENTIFY: NOAO/IRAF V2.10BETA valdes@puppis Fri 11:04:52 06-Mar-92
    Reference image = demoarc.ms, New image = demoobjarc.ms, Refit = no
    Image Data   Found    Fit Pix Shift  User Shift  Z Shift     RMS
  d...ms - Ap 1  27/30  27/27   0.00502      0.0263  3.99E-6   0.175
  d...ms - Ap 3  27/30  27/27   8.62E-4       0.006  5.07E-7   0.248
  Dispersion correct demoobj
  demoobj.ms.imh: REFSHFT1 = 'demoobjarc.ms interp', shift = -0.0050,
  rms = 0.00282813 intercept = -0.0118401, slope = 2.70764E-4
  d...ms: ap = 2, w1 = 5785.86, w2 = 7351.59, dw = 6.14, nw = 256
  demoobj.ms.imh:
  Splot spectrum? (no|yes|NO|YES) (yes):
  &lt;Exit with <span style="font-family: monospace;">'q'</span>&gt;
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_DO3FIBER">
  <dt><b>DO3FIBER V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DO3FIBER' Line='DO3FIBER V2.11' -->
  <dd>The initial arc line identifications is done with the automatic line
  identification algorithm.
  </dd>
  </dl>
  <dl id="l_DO3FIBER">
  <dt><b>DO3FIBER V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DO3FIBER' Line='DO3FIBER V2.10.3' -->
  <dd>The usual output WCS format is <span style="font-family: monospace;">"equispec"</span>.  The image format type to be
  processed is selected with the <i>imtype</i> environment parameter.  The
  dispersion axis parameter is now a package parameter.  Images will only
  be processed if the have the CCDPROC keyword.  A <i>datamax</i> parameter
  has been added to help improve cosmic ray rejection.  A scattered
  light subtraction processing option has been added.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  apedit, apfind, approfiles, aprecenter, apresize, apsum, aptrace, apvariance,
  ccdred, center1d, dispcor, fit1d, icfit, identify, observatory,
  onedspec.package, refspectra, reidentify, setairmass, setjd
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'SUMMARY' 'PARAMETERS' 'ENVIRONMENT PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

.. _dofoe:

dofoe: Process Fiber Optic Echelle (FOE) spectra
================================================

**Package: echelle**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  dofoe objects
  </p>
  </section>
  <section id="s_summary">
  <h3>Summary</h3>
  <p>
  The <b>dofoe</b> reduction task is specialized for scattered light
  subtraction, extraction, flat fielding, and wavelength calibration of Fiber
  Optic Echelle (FOE) spectra.  There may be one fiber or two fibers where
  the second fiber is illuminated by an arc calibration during arc and object
  exposures and a flat field during flat field exposures.  It is a command
  language script which collects and combines the functions and parameters of
  many general purpose tasks to provide a single complete data reduction
  path.  The task provides a degree of guidance, automation, and record
  keeping necessary when dealing with the complexities of reducing this type
  of data.
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
  <dd>Flat field spectrum.  If specified the one dimensional flat field spectrum
  is extracted and used to make flat field calibrations.
  </dd>
  </dl>
  <dl id="l_arcs">
  <dt><b>arcs = <span style="font-family: monospace;">""</span> (at least one if dispersion correcting)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='arcs' Line='arcs = "" (at least one if dispersion correcting)' -->
  <dd>List of arc spectra.  The first arc in the list is used to create a
  dispersion solution interactively.  All other arc spectra will be
  automatically reidentified.
  </dd>
  </dl>
  <dl id="l_arctable">
  <dt><b>arctable = <span style="font-family: monospace;">""</span> (optional) (refspectra)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='arctable' Line='arctable = "" (optional) (refspectra)' -->
  <dd>Table defining arc spectra to be assigned to object spectra (see
  <b>refspectra</b>).  If not specified an assignment based on a header
  parameter, <i>params.sort</i>, such as the observation time is made.
  </dd>
  </dl>
  <dl id="l_readnoise">
  <dt><b>readnoise = <span style="font-family: monospace;">"0."</span> (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='readnoise' Line='readnoise = "0." (apsum)' -->
  <dd>Read out noise in photons.  This parameter defines the minimum noise
  sigma.  It is defined in terms of photons (or electrons) and scales
  to the data values through the gain parameter.  A image header keyword
  (case insensitive) may be specified to get the value from the image.
  </dd>
  </dl>
  <dl id="l_gain">
  <dt><b>gain = <span style="font-family: monospace;">"1."</span> (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gain' Line='gain = "1." (apsum)' -->
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
  This applies only to the object spectra and not the flat field or
  arc spectra.  For more
  on this see the discussion of the saturation parameter in the
  <b>apextract</b> package.
  </dd>
  </dl>
  <dl id="l_norders">
  <dt><b>norders = 12 (apfind)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='norders' Line='norders = 12 (apfind)' -->
  <dd>Number of orders to be found.  This number is used during the automatic
  definition of the apertures from the aperture reference spectrum.  Note
  that when there is a second fiber for simultaneous arcs the specified
  number will be automatically doubled for finding both sets of orders.
  So in either case specify only the number of orders from a single fiber.
  The interactive review of the aperture assignments allows verification
  and adjustments to the automatic aperture definitions.
  </dd>
  </dl>
  <dl id="l_width">
  <dt><b>width = 4. (apedit)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='width' Line='width = 4. (apedit)' -->
  <dd>Approximate base full width of the fiber profiles.  This parameter is used
  for the profile centering algorithm.
  </dd>
  </dl>
  <dl id="l_arcaps">
  <dt><b>arcaps = <span style="font-family: monospace;">"2x2"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='arcaps' Line='arcaps = "2x2"' -->
  <dd>When there is only a single fiber set this parameter to <span style="font-family: monospace;">""</span>.  When there is
  a second fiber used to create simultaneous arcs during the object exposures
  this parameter specifies a list of aperture numbers for the arc fibers.
  Since the object and arc fiber orders are paired the default setting
  expects the even number apertures to be the are apertures.  This should be
  checked interactively.
  </dd>
  </dl>
  <dl id="l_fitflat">
  <dt><b>fitflat = yes (flat1d)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitflat' Line='fitflat = yes (flat1d)' -->
  <dd>Fit and divide the extracted flat field orders by a smooth function
  in order to normalize the wavelength response?  If not done the flat field
  spectral shape (which includes the blaze function) will be divided
  out of the object spectra, thus altering the object data values.
  If done only the small scale response variations are included in the
  flat field and the object spectra will retain their observed flux
  levels and blaze function.
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
  other background options are local to each aperture at each point along the
  dispersion.  The <span style="font-family: monospace;">"fit"</span> option uses additional fitting parameters from
  <b>params</b> and the <span style="font-family: monospace;">"scattered"</span> option uses parameters from <b>apscat1</b>
  and <b>apscat2</b>.
  </dd>
  </dl>
  <dl id="l_clean">
  <dt><b>clean = yes (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clean' Line='clean = yes (apsum)' -->
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
  <dl id="l_redo">
  <dt><b>redo = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='redo' Line='redo = no' -->
  <dd>Redo operations previously done?  If no then previously processed spectra
  in the objects list will not be processed (unless they need to be updated).
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = no' -->
  <dd>Update processing of previously processed spectra if aperture, flat
  field, or dispersion reference definitions are changed?
  </dd>
  </dl>
  <dl id="l_batch">
  <dt><b>batch = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='batch' Line='batch = no' -->
  <dd>Process spectra as a background or batch job.
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
  package.  This is also true of <b>dofoe</b>.
  </p>
  <dl id="l_observatory">
  <dt><b>observatory = <span style="font-family: monospace;">"observatory"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observatory' Line='observatory = "observatory"' -->
  <dd>Observatory at which the spectra were obtained if not specified in the
  image header by the keyword OBSERVAT.  For FOE data the image headers
  identify the observatory as <span style="font-family: monospace;">"kpno"</span> so this parameter is not used.
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
  <dt><b>version = <span style="font-family: monospace;">"ECHELLE: ..."</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='version' Line='version = "ECHELLE: ..."' -->
  <dd>Version of the package.
  </dd>
  </dl>
  <p style="text-align:center">PARAMS PARAMETERS
  
  </p>
  <p>
  The following parameters are part of the <b>params</b> parameter set and
  define various algorithm parameters for <b>dofoe</b>.
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
  <p style="text-align:center">-- DEFAULT BACKGROUND PARAMETERS --
  
  </p>
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
  <dl id="l_b_smooth">
  <dt><b>b_smooth = 10 (apsum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_smooth' Line='b_smooth = 10 (apsum)' -->
  <dd>Box car smoothing length for background when using background
  subtraction.  Since the background noise is often the limiting factor
  for good extraction one may box car smooth the background to improve the
  statistics.
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
  The default is generally appropriate for FOE data but users
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
  <p style="text-align:center">-- FLAT FIELD FUNCTION FITTING PARAMETERS --
  
  </p>
  <dl id="l_f_interactive">
  <dt><b>f_interactive = no (fit1d)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='f_interactive' Line='f_interactive = no (fit1d)' -->
  <dd>Fit the one dimensional flat field order spectra interactively?
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
  <dt><b>cradius = 4. (reidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cradius' Line='cradius = 4. (reidentify)' -->
  <dd>Radius from previous position to reidentify arc line.
  </dd>
  </dl>
  <dl id="l_i_function">
  <dt><b>i_function = <span style="font-family: monospace;">"chebyshev"</span>, i_xorder = 3, i_yorder = 3 (ecidentify)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='i_function' Line='i_function = "chebyshev", i_xorder = 3, i_yorder = 3 (ecidentify)' -->
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
  In <b>dofoe</b> the Julian date (JD) and the local Julian day number (LJD)
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
  The <b>dofoe</b> reduction task is specialized for scattered light
  subtraction, extraction, flat fielding, and wavelength calibration of Fiber
  Optic Echelle (FOE) spectra.  There may be one fiber or two fibers where
  the second fiber is illuminated by an arc calibration during arc and object
  exposures and a flat field during flat field exposures.  When there is
  just one fiber the parameter <i>arcaps</i> is set to <span style="font-family: monospace;">""</span> and when there are
  two fibers the parameter is used to select which of the defined
  apertures are the orders from the simultaneous arc fiber.
  </p>
  <p>
  This task is a command language script which collects and combines the
  functions and parameters of many general purpose tasks to provide a single
  complete data reduction path.  The task provides a degree of guidance,
  automation, and record keeping necessary when dealing with the complexities
  of reducing this type of data.
  </p>
  <p>
  The general organization of the task is to do the interactive setup steps
  first using representative calibration data and then perform the majority
  of the reductions automatically, possibly as a background process, with
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
  <b>dofoe</b> combines many separate, general purpose tasks the description
  given here refers to these tasks and leaves some of the details to their
  help documentation.
  </p>
  <p>
  <b>Usage Outline</b>
  </p>
  <dl>
  <dt><b>[1]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[1]' -->
  <dd>The images must first be processed with <b>ccdproc</b> for overscan,
  bias, and dark corrections.
  </dd>
  </dl>
  <dl>
  <dt><b>[2]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[2]' -->
  <dd>Set the <b>dofoe</b> parameters with <b>eparam</b>.  Specify the object
  images to be processed, the flat field image as the aperture reference and
  the flat field, and one or more arc images.  If there are many
  object or arc spectra per setup you might want to prepare <span style="font-family: monospace;">"@ files"</span>.
  Verify and set the format parameters, particularly the number of orders to be
  extracted and processed.  The processing parameters are set
  for simple extraction and dispersion correction but dispersion correction
  can be turned off for quicklook or background subtraction and cleaning
  may be added.
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
  illuminated.  The specified number of orders are found automatically and
  sequential apertures assigned.  The resize option sets the aperture size to
  the widths of the profiles at a fixed fraction of the peak height.
  </dd>
  </dl>
  <dl>
  <dt><b>[5]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[5]' -->
  <dd>The automatic order identification and aperture assignment is based on peak
  height and may be incorrect.  The interactive aperture editor is entered
  with a plot of the apertures.  When there is a second simultaneous arc
  fiber it is essential that the object and arc
  fiber orders are properly paired with the arc fibers having even aperture
  numbers and the object fibers having odd aperture numbers.  It is also
  required that no orders be skipped in the region of interest.  Missing
  orders are added with the <span style="font-family: monospace;">'m'</span> key.  Once all orders have been marked the
  aperture numbers are resequenced with <span style="font-family: monospace;">'o'</span>.  If local background subtraction
  is selected the background regions should be checked with the <span style="font-family: monospace;">'b'</span> key.
  Preceding this with the <span style="font-family: monospace;">'a'</span> key allows any changes to the background
  regions to be applied to all orders.  To exit type <span style="font-family: monospace;">'q'</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>[6]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[6]' -->
  <dd>The order positions at a series of points along the dispersion are measured
  and a function is fit to these positions.  This may be done interactively to
  adjust the fitting parameters.  Not all orders need be examined and the <span style="font-family: monospace;">"NO"</span>
  response will quit the interactive fitting.  To exit the interactive
  fitting type <span style="font-family: monospace;">'q'</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>[7]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[7]' -->
  <dd>If flat fielding is to be done the flat field spectra are extracted.  A
  smooth function is fit to each flat field spectrum to remove the large
  scale spectral signature.  The final response spectra are normalized to a
  unit mean over all fibers.
  </dd>
  </dl>
  <dl>
  <dt><b>[8]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[8]' -->
  <dd>If scattered light subtraction is selected the scattered light parameters
  are set using the aperture reference image and the task <b>apscatter</b>.
  The purpose of this is to interactively define the aperture buffer distance
  for the scattered light and the cross and parallel dispersion fitting
  parameters.  The fitting parameters are taken from and recorded in the
  parameter sets <b>apscat1</b> and <b>apscat2</b>.  All other scattered light
  subtractions are done noninteractively with these parameters.  Note that
  the scattered light correction modifies the input images.
  </dd>
  </dl>
  <dl>
  <dt><b>[9]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[9]' -->
  <dd>If dispersion correction is selected the first arc in the arc list is
  extracted.  One fiber is used to identify the arc lines and define the
  dispersion function using the task <b>ecidentify</b>.  Identify a few arc
  lines in a few orders with <span style="font-family: monospace;">'m'</span> and <span style="font-family: monospace;">'k'</span> or <span style="font-family: monospace;">'o'</span>, use the <span style="font-family: monospace;">'l'</span> line list
  identification command to automatically add additional lines and fit the
  dispersion function.  Check the quality of the dispersion function fit
  with <span style="font-family: monospace;">'f'</span>.  When satisfied exit with <span style="font-family: monospace;">'q'</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>[10]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[10]' -->
  <dd>If there is a second fiber the dispersion function is automatically
  determined using the task <b>ecreidentify</b>.
  </dd>
  </dl>
  <dl>
  <dt><b>[11]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[11]' -->
  <dd>The arc reference spectrum is dispersion corrected.
  If the spectra are resampled to a linear dispersion system
  (which will be the same for all spectra) the dispersion parameters
  determined from the dispersion solution are printed.
  </dd>
  </dl>
  <dl>
  <dt><b>[12]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[12]' -->
  <dd>The object spectra are now automatically background subtracted (an
  alternative to scattered light subtraction), extracted, flat fielded,
  and dispersion corrected.  Any new dispersion function reference arcs
  assigned to the object images are automatically extracted and
  dispersion functions determined.  A zero point wavelength correction
  is computed from the simultaneous arc fiber spectrum and applied to
  the object spectrum if orders from the second fiber have been identified
  with the <i>arcaps</i> parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>[13]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[13]' -->
  <dd>The final spectra will have the same name as the original 2D images
  with a <span style="font-family: monospace;">".ec"</span> extension added.
  </dd>
  </dl>
  <p>
  <b>Spectra and Data Files</b>
  </p>
  <p>
  The basic input consists of single or dual fiber FOE object and calibration
  spectra stored as IRAF images.  The <i>arcaps</i> parameter is used to
  discriminate between the two cases.  The type of image format is defined by
  the environment parameter <i>imtype</i>.  Only images with that extension
  will be processed and created.  The raw CCD images must be processed to
  remove overscan, bias, and dark count effects.  This is generally done
  using the <b>ccdred</b> package.  Flat fielding is generally not done at
  this stage but as part of <b>dofoe</b>.  The calibration spectra are flat
  field observations in all fibers, comparison arc lamp spectra in all
  fibers, and, for dual fiber model, arc spectra in one fiber while the
  second fiber observes the object.  If for some reason the flat field or
  calibration arc spectra have separate exposures for the two fibers the
  separate exposures may simply be added.
  </p>
  <p>
  The assignment of arc calibration exposures to object exposures is
  generally done by selecting the nearest in time and interpolating.
  However, the optional <i>arc assignment table</i> may be used to explicitly
  assign arc images to specific objects.  The format of this file is
  described in the task <b>refspectra</b>.
  </p>
  <p>
  The final reduced spectra are recorded in two or three dimensional IRAF
  images.  The images have the same name as the original images with an added
  <span style="font-family: monospace;">".ec"</span> extension.  Each line in the reduced image is a one dimensional
  spectrum (an echelle order) with associated aperture and wavelength
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
  The <b>echelle</b> package parameters set parameters affecting all the tasks
  in the package.  Some of the parameters are not applicable to the
  <b>dofoe</b> task.  The observatory parameter is only required for data
  without an OBSERVAT header parameter (currently included in NOAO data).
  The spectrum interpolation type might be changed to <span style="font-family: monospace;">"sinc"</span> but with the
  cautions given in <b>onedspec.package</b>.  The dispersion axis parameter is
  only needed if a DISPAXIS image header parameter is not defined.  The other
  parameters define the standard I/O functions.  The verbose parameter
  selects whether to print everything which goes into the log file on the
  terminal.  It is useful for monitoring what the <b>dofoe</b> task does.  The
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
  The aperture reference spectrum is used to find the orders and trace
  them.  Thus, this requires an image with good signal in both fibers
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
  DISPAXIS.  The width parameter (in pixels) is used for the profile
  centering algorithm (<b>center1d</b>).
  </p>
  <p>
  The number of orders selects the number of orders for a single
  fiber and <span style="font-family: monospace;">"pairs"</span> of object and arc
  fiber profiles for dual fibers.   The number specified will be
  automatically found based on the strongest peaks.
  In the  dual fiber case it is important that both elements of a pair be found,
  so no orders be skipped, and the aperture numbers must be sequential with
  arc profiles having even aperture numbers and object profiles having
  odd numbers in the region of interest, the automatic identification is  
  just a starting point for the interactive review.  The even/odd
  relationship between object and arc profiles is set by the <i>arcaps</i>
  parameter and so may be reversed if desired.
  </p>
  <p>
  The next set of parameters select the processing steps and options.  The
  flat fitting option allows fitting and removing the overall shape of the
  flat field spectra while preserving the pixel-to-pixel response
  corrections.  This is useful for maintaining the approximate object count
  levels, including the blaze function, and not introducing the reciprocal of
  the flat field spectrum into the object spectra.  If not selected the flat
  field will remove the blaze function from the observations and introduce
  some wavelength dependence from the flat field lamp spectrum.
  </p>
  <p>
  The <i>background</i> option selects the type of correction for background or
  scattered light.  If the type is <span style="font-family: monospace;">"scattered"</span> a global scattered light is
  fit to the data between the apertures  and subtracted from the images.
  <i>Note that the input images are modified by this operation</i>.  This
  option is slow.  Alternatively, a local background may be subtracted using
  background regions defined for each aperture.  The data in the regions may
  be averaged, medianed, or the minimum value used.  Another choice is to fit
  the data in the background regions by a function and interpolate to the
  object aperture.
  </p>
  <p>
  The <i>clean</i> option invokes a profile fitting and deviant point rejection
  algorithm as well as a variance weighting of points in the aperture.  These
  options require knowing the effective (i.e. accounting for any image
  combining) read out noise and gain.  For a discussion of cleaning and
  variance weighted extraction see <b>apvariance</b> and <b>approfiles</b>.
  </p>
  <p>
  The dispersion correction option selects whether to extract arc spectra,
  determine a dispersion function, assign them to the object spectra, and,
  possibly, resample the spectra to a linear (or log-linear) wavelength
  scale.
  </p>
  <p>
  Generally once a spectrum has been processed it will not be reprocessed if
  specified as an input spectrum.  However, changes to the underlying
  calibration data can cause such spectra to be reprocessed if the
  <i>update</i> flag is set.  The changes which will cause an update are a new
  reference image, new flat field, adding the scattered light option, and a
  new arc reference image.  If all input spectra are to be processed
  regardless of previous processing the <i>redo</i> flag may be used.  Note
  that reprocessing clobbers the previously processed output spectra.
  </p>
  <p>
  The <i>batch</i> processing option allows object spectra to be processed as
  a background or batch job.  The <i>listonly</i> option prints a summary of
  the processing steps which will be performed on the input spectra without
  actually doing anything.  This is useful for verifying which spectra will
  be affected if the input list contains previously processed spectra.  The
  listing does not include any arc spectra which may be extracted to
  dispersion calibrate an object spectrum.
  </p>
  <p>
  The last parameter (excluding the task mode parameter) points to another
  parameter set for the algorithm parameters.  The way <b>dofoe</b> works
  this may not have any value and the parameter set <b>params</b> is always
  used.  The algorithm parameters are discussed further in the next section.
  </p>
  <p>
  <b>Algorithms and Algorithm Parameters</b>
  </p>
  <p>
  This section summarizes the various algorithms used by the <b>dofoe</b>
  task and the parameters which control and modify the algorithms.  The
  algorithm parameters available to the user are collected in the parameter
  set <b>params</b>.  These parameters are taken from the various general
  purpose tasks used by the <b>dofoe</b> processing task.  Additional
  information about these parameters and algorithms may be found in the help
  for the actual task executed.  These tasks are identified in the parameter
  section listing in parenthesis.  The aim of this parameter set organization
  is to collect all the algorithm parameters in one place separate from the
  processing parameters and include only those which are relevant for
  FOE data.  The parameter values can be changed from the
  defaults by using the parameter editor,
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epar params
  </pre></div>
  <p>
  or simple typing <i>params</i>.  The parameter editor can also be
  entered when editing the <b>dofoe</b> parameters by typing <i>:e
  params</i> or simply <i>:e</i> if positioned at the <i>params</i>
  parameter.
  </p>
  <p>
  <b>Aperture Definitions</b>
  </p>
  <p>
  The first operation is to define the extraction apertures, which include the
  aperture width, background regions, and position dependence with
  wavelength, for the object and arc orders of interest.  This is done
  on a reference spectrum which is usually a flat field taken through
  all fibers.  Other spectra will inherit the reference apertures and
  apply a correction for any shift of the orders across the dispersion.
  The reference apertures are defined only once unless the <i>redo</i>
  option is set.
  </p>
  <p>
  The selected number of orders are found automatically by selecting the
  highest peaks in a cut across the dispersion.  Note that the specified
  number of orders is multiplied by two in defining the apertures when
  there is a second fiber.  Apertures
  are assigned with a limits set by the <i>lower</i> and
  <i>upper</i> parameter and numbered sequentially.  A query is then
  given allowing the aperture limits to be <span style="font-family: monospace;">"resized"</span> based on the profile
  itself (see <b>apresize</b>).
  </p>
  <p>
  A cut across the orders is then shown with the apertures marked and
  an interactive aperture editing mode is entered (see <b>apedit</b>).
  For <b>dofoe</b> the aperture identifications and numbering is particularly
  critical.  When there is a single fiber the aperture numbers must
  be sequential with the order numbers.  If an order is skipped then the
  aperture number must also be skipped.
  </p>
  <p>
  For dual fibers all <span style="font-family: monospace;">"pairs"</span> of object and arc orders in the region of
  interest must be defined without skipping any orders.  The orders must
  also be numbered sequentially (though the direction does not matter)
  so that the arc apertures are either all even or all odd as defined
  by the <i>arcaps</i> parameter (the default is even numbers for the
  arc apertures).  The <span style="font-family: monospace;">'o'</span> key will provide the necessary reordering.
  </p>
  <p>
  If local background subtraction is used the background regions should
  also be checked with the <span style="font-family: monospace;">'b'</span> key.  Typically one adjusts all
  the background regions at the same time by selecting all apertures with
  the <span style="font-family: monospace;">'a'</span> key first.  To exit the background and aperture editing steps type
  <span style="font-family: monospace;">'q'</span>.
  </p>
  <p>
  Next the positions of the orders at various points along the dispersion are
  measured and <span style="font-family: monospace;">"trace functions"</span> are fit.  The user is asked whether to fit
  each trace function interactively.  This is selected to adjust the fitting
  parameters such as function type and order.  When interactively fitting a
  query is given for each aperture.  After the first aperture one may skip
  reviewing the other traces by responding with <span style="font-family: monospace;">"NO"</span>.  Queries made by
  <b>dofoe</b> generally may be answered with either lower case <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"no"</span>
  or with upper case <span style="font-family: monospace;">"YES"</span> or <span style="font-family: monospace;">"NO"</span>.  The upper case responses apply to all
  further queries and so are used to eliminate further queries of that kind.
  </p>
  <p>
  The above steps are all performed using tasks from the <b>apextract</b>
  package and parameters from the <b>params</b> parameters.  As a quick
  summary, the dispersion direction of the spectra are determined from the
  package <b>dispaxis</b> parameter if not defined in the image header.  The
  default line or column for finding the orders and the number of image lines
  or columns to sum are set by the <i>line</i> and <i>nsum</i> parameters.  A
  line of INDEF (the default) selects the middle of the image.  The automatic
  finding algorithm is described for the task <b>apfind</b> and basically
  finds the strongest peaks.  The resizing is described in the task
  <b>apresize</b> and the parameters used are also described there and
  identified in the PARAMETERS section.  The tracing is done as described in
  <b>aptrace</b> and consists of stepping along the image using the specified
  <i>t_step</i> parameter.  The function fitting uses the <b>icfit</b> commands
  with the other parameters from the tracing section.
  </p>
  <p>
  <b>Background or Scattered Light Subtraction</b>
  </p>
  <p>
  In addition to not subtracting any background scattered light there are two
  approaches to subtracting this light.  The first is to determine a smooth
  global scattered light component.  The second is to subtract a locally
  determined background at each point along the dispersion and for each
  aperture.  Note that background subtraction is only done for object images
  and not for arc images.
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
  <span style="font-family: monospace;">"median"</span>) or median samples during fitting (<i>b_naverage</i> &lt; -1).
  The background smoothing parameter <i>b_smooth</i> is may be used
  to provide some additional local smoothing of the background light.
  The background subtraction algorithm and options are described in greater
  detail in <b>apsum</b> and <b>apbackground</b>.
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
  regardless of the <i>weights</i> parameter.  The sigma threshold for
  cleaning are also set in the <b>params</b> parameters.
  </p>
  <p>
  The cleaning and variance weighting options require knowing the effective
  (i.e. accounting for any image combining) read out noise and gain.  These
  numbers need to be adjusted if the image has been processed such that the
  intensity scale has a different origin (such as a scattered light
  subtraction) or scaling (such as caused by unnormalized flat fielding).
  These options also require using background subtraction if the profile does
  not go to zero.  For optimal extraction and cleaning to work it is
  recommended that any scattered light be accounted for by local background
  subtraction rather than with the scattered light subtraction and the
  <i>fitflat</i> option be used.  The <i>b_smooth</i> parameter is also
  appropriate in this application and improves the optimal extraction results
  by reducing noise in the background signal.  For further discussion of
  cleaning and variance weighted extraction see <b>apvariance</b> and
  <b>approfiles</b> as well as  <b>apsum</b>.
  </p>
  <p>
  <b>Flat Field Correction</b>
  </p>
  <p>
  Flat field corrections may be made during the basic CCD processing; i.e.
  direct division by the two dimensional flat field observation.  In that
  case do not specify a flat field spectrum; use the null string <span style="font-family: monospace;">""</span>.  The
  <b>dofoe</b> task provides an alternative flat field response correction
  based on division of the extracted object spectra by the extracted flat field
  spectra.  A discussion of the theory and merits of flat fielding directly
  verses using the extracted spectra will not be made here.  The
  <b>dofoe</b> flat fielding algorithm is the <i>recommended</i> method for
  flat fielding since it works well and is not subject to the many problems
  involved in two dimensional flat fielding.
  </p>
  <p>
  The first step is extraction of the flat field spectrum, if one is specified,
  using the reference apertures.  Only one flat field is allowed so if
  multiple flat fields are required the data must be reduced in groups.  When
  the <i>fitflat</i> option is selected (the default) the extracted flat field
  spectra are fit by smooth functions and the ratio of the flat field spectra
  to the smooth functions define the response spectra.  The default fitting
  function and order are given by the parameters <i>f_function</i> and
  <i>f_order</i>.  If the parameter <i>f_interactive</i> is <span style="font-family: monospace;">"yes"</span> then the
  fitting is done interactively using the <b>fit1d</b> task which uses the
  <b>icfit</b> interactive fitting commands.
  </p>
  <p>
  If the <i>fitflat</i> option is not selected the extracted and globally
  normalized flat field spectra are directly divided in the object spectra.
  This removes the blaze function, thus altering the data counts, and
  introduces the reciprocal of the flat field spectrum in the object
  spectra.
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
  to dispersion calibrate the object spectra.  There are three steps involved;
  determining the dispersion functions relating pixel position to wavelength,
  assigning the appropriate dispersion function to a particular observation,
  and either storing the nonlinear
  dispersion function in the image headers or resampling the spectra to
  evenly spaced pixels in wavelength.  When there are two fibers there is
  also a step of applying a zero point correction to the object fiber based
  on the arc fiber.
  </p>
  <p>
  The first arc spectrum in the arc list is used to define the reference
  dispersion solution.  It is extracted using the reference aperture
  definitions.  Note extractions of arc spectra are not background or
  scattered light subtracted.  The interactive task <b>ecidentify</b> is used
  to define the dispersion function in one fiber.  The idea is to mark some
  lines in a few orders whose wavelengths are known (with the line list used
  to supply additional lines after the first few identifications define the
  approximate wavelengths) and to fit a function giving the wavelength from
  the aperture number and pixel position.  The dispersion function for the
  second fiber, if one is present, is then determined automatically by
  reference to the first fiber using the task <b>ecreidentify</b>.
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
  Once the reference dispersion functions are defined other arc spectra are
  extracted as they are assign to the object spectra.  The assignment of
  arcs is done either explicitly with an arc assignment table (parameter
  <i>arctable</i>) or based on a header parameter such as a time.
  The assignments are made by the task <b>refspectra</b>.  When two arcs are
  assigned to an object spectrum an interpolation is done between the two
  dispersion functions.  This makes an approximate correction for steady
  drifts in the dispersion.
  </p>
  <p>
  When a second arc fiber monitors any zero point shifts in the dispersion
  functions it is probably only necessary to have one or two arc spectra, one
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
  Defining the dispersion function for a new arc extraction is done with
  the task <b>ecreidentify</b>.  This is done noninteractively with log
  information recorded about the line reidentifications and the fit.
  </p>
  <p>
  When there are two fibers there are two full dispersion function from the
  single or pair of arc spectra, one for the object fiber and one for the arc
  fiber.  When an object spectrum is extracted so is the simultaneous arc
  spectrum.  A zero point shift of the arc spectrum relative to the
  dispersion solution of the dual arc observation is computed using
  <b>ecreidentify</b> (<i>refit</i>=no).  This zero point shift is assumed to
  be the same for the object fiber and it is added to the dispersion function
  of the dual arc observation for the object fiber.  Note that this does not
  assume that the object and arc fiber dispersion functions are the same or
  have the same wavelength origin, but only that the same shift in wavelength
  zero point applies to both fibers.  Once the dispersion function correction
  is determined from the extracted arc fiber spectrum it is deleted leaving
  only the object spectrum.
  </p>
  <p>
  The last step of dispersion correction is setting the dispersion
  of the object spectrum.  There are two choices here.
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
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  The following example uses artificial data and may be executed
  at the terminal (with IRAF V2.10).  This is also the sequence performed
  by the test procedure <span style="font-family: monospace;">"demos dofoe"</span>.  Because the images are small the
  dispersion solution is somewhat simplistic.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ec&gt; demos mkdofoe
  Creating image demoobj ...
  Creating image demoflat ...
  Creating image demoarc ...
  ec&gt; echelle.verbose = yes
  ec&gt; dofoe demoobj apref=demoflat flat=demoflat arcs=demoarc \
  &gt;&gt;&gt; norders=3 width=5.
  Set reference apertures for demoflat
  Searching aperture database ...
  Finding apertures ...
  Mar  4  9:39: FIND - 6 apertures found for demoflat
  Resize apertures for demoflat?  (yes):
  Resizing apertures ...
  Mar  4  9:39: RESIZE - 6 apertures resized for demoflat
  &lt;Review aperture assignments.  Exit with <span style="font-family: monospace;">'q'</span>&gt;
  Fit traced positions for demoflat interactively?  (yes):
  Tracing apertures ...
  Fit curve to aperture 1 of demoflat interactively  (yes):
  &lt;Review trace and fit. Exit with <span style="font-family: monospace;">'q'</span>&gt;
  Fit curve to aperture 2 of demoflat interactively  (yes): N
  Mar  4  9:39: TRACE - 6 apertures traced in demoflat.
  Mar  4  9:39: DATABASE - 6 apertures for demoflat written to database
  Create response function demoflatnorm.ec
  Extract flat field demoflat
  Searching aperture database ...
  Mar  4  9:39: DATABASE  - 6 apertures read for demoflat from database
  Extracting apertures ...
  Mar  4  9:39: EXTRACT - Aperture 1 from demoflat --&gt; demoflat.ec
  Mar  4  9:39: EXTRACT - Aperture 2 from demoflat --&gt; demoflat.ec
  Mar  4  9:39: EXTRACT - Aperture 3 from demoflat --&gt; demoflat.ec
  Mar  4  9:39: EXTRACT - Aperture 4 from demoflat --&gt; demoflat.ec
  Mar  4  9:39: EXTRACT - Aperture 5 from demoflat --&gt; demoflat.ec
  Mar  4  9:40: EXTRACT - Aperture 6 from demoflat --&gt; demoflat.ec
  Fit and ratio flat field demoflat
  Create the normalized response demoflatnorm.ec
  demoflatnorm.ec -&gt; demoflatnorm.ec  using bzero: 0.  and bscale: 1.
      mean: 1.  median: 0.9990048  mode: 0.9876572
      upper: INDEF  lower: INDEF
  Extract arc reference image demoarc
  Mar  4  9:40: DATABASE  - 6 apertures read for demoflat from database
  Mar  4  9:40: DATABASE - 6 apertures for demoarc written to database
  Mar  4  9:40: EXTRACT - Aperture 1 from demoarc --&gt; demoarc.ec
  Mar  4  9:40: EXTRACT - Aperture 2 from demoarc --&gt; demoarc.ec
  Mar  4  9:40: EXTRACT - Aperture 3 from demoarc --&gt; demoarc.ec
  Mar  4  9:40: EXTRACT - Aperture 4 from demoarc --&gt; demoarc.ec
  Mar  4  9:40: EXTRACT - Aperture 5 from demoarc --&gt; demoarc.ec
  Mar  4  9:40: EXTRACT - Aperture 6 from demoarc --&gt; demoarc.ec
  Determine dispersion solution for demoarc
  &lt;Mark lines with <span style="font-family: monospace;">'m'</span> and change orders with <span style="font-family: monospace;">'k'</span>
  &lt;<span style="font-family: monospace;">'m'</span> line at pixel 78 and assign 4965.
  &lt;<span style="font-family: monospace;">'k'</span> to order 2
  &lt;<span style="font-family: monospace;">'m'</span> line at pixel 78 and assign 5009
  &lt;<span style="font-family: monospace;">'m'</span> line at pixel 78 and assign 5020
  &lt;<span style="font-family: monospace;">'k'</span> to order 3
  &lt;<span style="font-family: monospace;">'m'</span> line at pixel 78 and assign 5049.8
  &lt;<span style="font-family: monospace;">'m'</span> line at pixel 78 and assign 5050.8
  &lt;<span style="font-family: monospace;">'m'</span> line at pixel 78 and assign 5055.3
  &lt;<span style="font-family: monospace;">'m'</span> line at pixel 78 and assign 5062
  &lt;<span style="font-family: monospace;">'m'</span> line at pixel 78 and assign 5064.9
  &lt;<span style="font-family: monospace;">'f'</span> to fit
  &lt;<span style="font-family: monospace;">'q'</span> to quit fit and <span style="font-family: monospace;">'q'</span> to quit ECIDENTIFY
  
  ECREIDENTIFY: NOAO/IRAF V2.10BETA valdes@puppis Wed 09:54:16 04-Mar-92
    Reference image = demoarc.ec, Refit = yes
     Image    Found     Fit Pix Shift  User Shift  Z Shift      RMS
    d...ec    8/8     8/8        1.48        7.06  2.11E-5  0.00879
  d...ec: ap = 1, w1 = 4959.1, w2 = 4978.5, dw = 0.076, nw = 256
  d...ec: ap = 2, w1 = 5003.4, w2 = 5022.1, dw = 0.073, nw = 256
  d...ec: ap = 3, w1 = 5049.0, w2 = 5067.0, dw = 0.070, nw = 256
  Extract object spectrum demoobj
  Searching aperture database ...
  Mar  4  9:54: DATABASE  - 6 apertures read for demoflat from database
  Recentering apertures ...
  Mar  4  9:54: RECENTER  - 6 apertures shifted by -0.03 for demoobj.
  Mar  4  9:54: DATABASE - 6 apertures for demoobj written to database
  Extracting apertures ...
  Mar  4  9:54: EXTRACT - Aperture 1 from demoobj --&gt; demoobj.ec
  Mar  4  9:54: EXTRACT - Aperture 2 from demoobj --&gt; demoobj.ec
  Mar  4  9:54: EXTRACT - Aperture 3 from demoobj --&gt; demoobj.ec
  Mar  4  9:54: EXTRACT - Aperture 4 from demoobj --&gt; demoobj.ec
  Mar  4  9:54: EXTRACT - Aperture 5 from demoobj --&gt; demoobj.ec
  Mar  4  9:54: EXTRACT - Aperture 6 from demoobj --&gt; demoobj.ec
  Assign arc spectra for demoobj
  [demoobj] refspec1='demoarc'
  Reidentify arc fibers in demoobj with respect to demoarc
  
  ECREIDENTIFY: NOAO/IRAF V2.10BETA valdes@puppis Wed 09:54:28 04-Mar-92
    Reference image = demoarcarc.ec, Refit = no
     Image    Found     Fit Pix Shift  User Shift  Z Shift      RMS
    d...ec    8/8     8/8       0.119       0.566  1.69E-6  0.00834
  Dispersion correct demoobj
  d...ec.imh: ap = 1, w1 = 4959.1, w2 = 4978.5, dw = 0.076, nw = 256
  d...ec.imh: ap = 2, w1 = 5003.4, w2 = 5022.1, dw = 0.073, nw = 256
  d...ec.imh: ap = 3, w1 = 5049.0, w2 = 5067.0, dw = 0.070, nw = 256
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_DOFOE">
  <dt><b>DOFOE V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DOFOE' Line='DOFOE V2.10.3' -->
  <dd>The image format type to be
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
  ccdred, center1d, dispcor, fit1d, icfit, ecidentify, observatory,
  onedspec.package, refspectra, ecreidentify, setairmass, setjd
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'SUMMARY' 'PARAMETERS' 'ENVIRONMENT PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

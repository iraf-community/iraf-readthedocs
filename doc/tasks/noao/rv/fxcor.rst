.. _fxcor:

fxcor: Radial velocities via Fourier cross correlation
======================================================

**Package: rv**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fxcor objects templates
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <p style="text-align:center">INPUT PARAMETERS
  
  </p>
  <dl id="l_objects">
  <dt><b>objects</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='objects' Line='objects' -->
  <dd>The list of image names for the input object spectra.
  </dd>
  </dl>
  <dl id="l_templates">
  <dt><b>templates</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='templates' Line='templates' -->
  <dd>The list of image names that will be used as templates for the cross
  correlation.  This list need not match the object list.  All pairs
  between the two lists will be correlated.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = "*"' -->
  <dd>List of apertures to be correlated in echelle and multispec format spectra.  
  This parameter is used for <i>both</i> the object and reference spectra if both
  spectra are two dimensional, otherwise the aperture list applies to the object
  only if the template is one-dimensional.  Individual apertures from a
  two-dimensional template may be
  extracted to 1-D using the <i>onedspec.scopy</i> task, and these new images may
  then be used in the template list as separate images.  (See the examples for
  how this may be done). The default of <span style="font-family: monospace;">'*'</span> means to process all of the
  apertures in the spectrum.  Note that the sample regions named by the 
  <i>osample</i> and <i>rsample</i> parameters will apply to all apertures.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input.
  </dd>
  </dl>
  <p style="text-align:center">DATA PREPARATION PARAMETERS
  
  </p>
  <dl id="l_continuum">
  <dt><b>continuum = <span style="font-family: monospace;">"both"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='continuum' Line='continuum = "both"' -->
  <dd>Continuum subtract the spectra prior to correlation?  Possible values for
  this parameter are any of the strings (or abbreviations) <span style="font-family: monospace;">"object"</span> (for object 
  spectrum only), <span style="font-family: monospace;">"template"</span> (for template spectrum only), <span style="font-family: monospace;">"both"</span> for 
  continuum flattening both object and template spectra, or <span style="font-family: monospace;">"none"</span> for 
  flattening neither spectrum.  The <i>continpars</i> pset is used to specify 
  the continuum fitting parameters.
  </dd>
  </dl>
  <dl id="l_filter">
  <dt><b>filter = <span style="font-family: monospace;">"none"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filter' Line='filter = "none"' -->
  <dd>Fourier filter the spectra prior to correlation?  Possible values for
  this parameter are any of the strings (or abbreviations) <span style="font-family: monospace;">"object"</span> (for object 
  spectrum only), <span style="font-family: monospace;">"template"</span> (for template spectrum only), <span style="font-family: monospace;">"both"</span> for 
  fourier filtering both object and template spectra, or <span style="font-family: monospace;">"none"</span> for 
  filtering neither spectrum.  The <i>filtpars</i> pset holds the parameters 
  for the filtering (filter type and width).
  </dd>
  </dl>
  <dl id="l_rebin">
  <dt><b>rebin = <span style="font-family: monospace;">"smallest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rebin' Line='rebin = "smallest"' -->
  <dd>Rebin to which spectrum dispersion?  If the input dispersions are not equal
  prior to the correlation,
  one of the two spectra in the pair will be rebinned according to the
  <i>rebin</i> parameter.  Possible values are <span style="font-family: monospace;">"smallest"</span> (to rebin to the
  smaller of the two values), <span style="font-family: monospace;">"largest"</span> (to rebin to the larger of the two
  values), <span style="font-family: monospace;">"object"</span> (to force the template to always be rebinned to the object
  dispersion), and <span style="font-family: monospace;">"template"</span> (to force the object to always be rebinned to the
  template dispersion).  Input spectra <i>must be</i> linearly corrected.
  Support for non-linear input dispersions is not included in this release.
  </dd>
  </dl>
  <dl id="l_pixcorr">
  <dt><b>pixcorr = <span style="font-family: monospace;">"no"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixcorr' Line='pixcorr = "no"' -->
  <dd>Do a pixel-only correlation, ignoring any dispersion information?  If this
  parameter is set to <i>yes</i>, then regardless of whether dispersion
  information is present in the image headers, the correlation will be done
  without rebinning the data to a log-linear dispersion.  This option is useful
  when pixel shifts, not velocities, are the desired output.
  </dd>
  </dl>
  <dl id="l_osample">
  <dt><b>osample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='osample' Line='osample = "*"' -->
  <dd>Sample regions of the object spectrum to be used in the correlation specified
  in pixels if the first character is a <span style="font-family: monospace;">'p'</span>, or angstroms if the first
  character is an <span style="font-family: monospace;">'a'</span>.  The default (i.e. no <span style="font-family: monospace;">'a'</span> or <span style="font-family: monospace;">'p'</span> as the first
  character) if a range is provided, is a range specified in angstroms.
  This string value will be updated in an interactive session as sample
  regions are re-selected in spectrum mode. The default, <span style="font-family: monospace;">'*'</span>, is the entire 
  spectrum.  The region is specified as a starting value, a <span style="font-family: monospace;">'-'</span>, and an ending 
  value.  If the specified range is out of bounds, the endpoints will be 
  modified to the nearest boundary, or else the entire spectrum will be 
  correlated if the whole range is out of bounds.
  </dd>
  </dl>
  <dl id="l_rsample">
  <dt><b>rsample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rsample' Line='rsample = "*"' -->
  <dd>Sample regions of the template spectrum to be used in the correlation specified
  in pixels if the first character is a <span style="font-family: monospace;">'p'</span>, or angstroms if the first
  character is an <span style="font-family: monospace;">'a'</span>.  The default (i.e. no <span style="font-family: monospace;">'a'</span> or <span style="font-family: monospace;">'p'</span> as the first
  character) if a range is provided, is a range specified in angstroms.
  This string value will be updated in an interactive session as sample
  regions are re-selected in spectrum mode. The default, <span style="font-family: monospace;">'*'</span>, is the entire 
  spectrum.  The region is specified as a starting value, a <span style="font-family: monospace;">'-'</span>, and an ending 
  value.  If the specified range is out of bounds, the endpoints will be 
  modified to the nearest boundary, or else the entire spectrum will be 
  correlated if the whole range is out of bounds.
  </dd>
  </dl>
  <dl id="l_apodize">
  <dt><b>apodize = 0.2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apodize' Line='apodize = 0.2' -->
  <dd>Fraction of endpoints to apodize with a cosine bell when preparing the data
  prior to the FFT.
  </dd>
  </dl>
  <p style="text-align:center">CORRELATION PEAK FITTING PARAMETERS
  
  </p>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"gaussian"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "gaussian"' -->
  <dd>Function used to find the center and width of the correlation peak.
  Possible choices are <span style="font-family: monospace;">"gaussian"</span>, <span style="font-family: monospace;">"parabola"</span>, <span style="font-family: monospace;">"lorentzian"</span>, <span style="font-family: monospace;">"center1d"</span>,
  or <span style="font-family: monospace;">"sinc"</span>.  If a center1d fit is selected, then only the center is determined.
  A <span style="font-family: monospace;">"sinc"</span> function uses a sinc interpolator to find the maximum of the 
  peak by interpolating the points selectes.  The FWHM calculation in this
  case is computed empirically by finding the half power point according
  to the computed peak height and the <i>background</i> level.  No FWHM 
  will be computed of the background is not set.  The function fitting options
  all compute the FWHM from the fitted coefficients of the function.
  </dd>
  </dl>
  <dl id="l_width">
  <dt><b>width = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='width' Line='width = INDEF' -->
  <dd>Width of the fitting region in pixels.  The fitting weights are
  zero at the endpoints so the width should be something
  like the expected full width.  If INDEF, then the width is
  set by the <i>height</i> and <i>peak</i> parameters. If other than INDEF, 
  this parameter will override the <i>height</i> and <i>peak</i> parameters.
  </dd>
  </dl>
  <dl id="l_height">
  <dt><b>height = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='height' Line='height = 0.' -->
  <dd>The width of the fitting region is defined by where the correlation
  function crosses this height starting from the peak.  The height is
  specified as either a normalized correlation level (this is like
  the <span style="font-family: monospace;">'y'</span> interactive key) or normalized to the peak.  The type of
  level is selected by the <i>peak</i> parameter.
  </dd>
  </dl>
  <dl id="l_peak">
  <dt><b>peak = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='peak' Line='peak = no' -->
  <dd>Measure the height parameter relative to the correlation peak value
  rather than as a normalized correlation level? If yes, then <i>height</i>
  is a fraction of the peak height with an assumed base of zero.
  </dd>
  </dl>
  <dl id="l_minwidth">
  <dt><b>minwidth = 3., maxwidth = 21.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minwidth' Line='minwidth = 3., maxwidth = 21.' -->
  <dd>The minimum and maximum widths allowed when the width is determined
  from the height.
  </dd>
  </dl>
  <dl id="l_weights">
  <dt><b>weights = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='weights' Line='weights = 1.' -->
  <dd>Power of distance defining the fitting weights.  The points used
  in fitting the correlation peak are weighted by a power of the
  distance from the center as given by the equation
  <div class="highlight-default-notranslate"><pre>
  weight = 1 - (distance / (width/2)) ** <i>weights</i>
  </pre></div>
  Note that a weight parameter of zero is equivalent to uniform weights.
  The center1d fitting algorithm uses it's own weighting function.
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = 0.0' -->
  <dd>Background level, in normalized correlation units, for a Gaussian or 
  Lorentzian fitting function.  If set to INDEF, the background is a free 
  parameter in the fit.
  </dd>
  </dl>
  <dl id="l_window">
  <dt><b>window = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='window' Line='window = INDEF' -->
  <dd>Size of the window in the correlation plot.  The peak will be displayed
  with a window centered on the peak maximum and two times <i>window</i> 
  pixels wide if no dispersion information is present in the image header.
  If dispersion information is present, <i>window</i> is specified in Km/s.
  A value of INDEF results in a default window size of 20 pixels.  If the
  window proves to be too small for the number of points to be fit selected 
  with the <i>width</i>, <i>height</i>, and/or <i>peak</i> parameters, a message
  will be written to the <span style="font-family: monospace;">".log"</span> file and/or screen explaining that points
  outside the window bounds were used in the fit.  The user may wish to
  review this fit or increase the window size.
  </dd>
  </dl>
  <dl id="l_wincenter">
  <dt><b>wincenter = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wincenter' Line='wincenter = INDEF' -->
  <dd>Center of the peak search window specified in pixel lags if no dispersion
  information is present, or specified in Km/s if dispersion information is
  present.  If set to the default INDEF, the maximum peak in the cross-correlation
  function will be fit by default.  If set to other than INDEF, the maximum peak 
  within a window centered on <i>wincenter</i> and two times <i>window</i> 
  lags wide will be used.  Note that this parameter can be used to constrain
  the velocities computed to a certain range in non-interactive mode.
  </dd>
  </dl>
  <p style="text-align:center">OUTPUT PARAMETERS
  
  </p>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>Name of the file to which output will be written.  If no file name is given
  then no log files will be kept, but the user will be queried for a file name
  if a write operation is performed.  Tabular text output will have a <span style="font-family: monospace;">".txt"</span> 
  suffix appended to the <i>output</i> name, a verbose description of each fit
  will have <span style="font-family: monospace;">".log"</span> suffix appended and will be written only if the <i>verbose</i>
  parameter is set, and the graphics metacode file will be appended with 
  a <span style="font-family: monospace;">".gki"</span> suffix. (NOTE: Image names will be truncated to 10 characters in the
  output file because of space considerations.  Verbose output logs will
  truncate the image names to 24 characters.  Object names are similarly
  truncated to 15 characters.  If a relative velocity is calculated with a
  redshift of more than 0.2, output will be redshift z values rather than
  velocities in Km/s.)
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = <span style="font-family: monospace;">"long"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = "long"' -->
  <dd>Set level of verbosity and types of files to create.  The <i>verbose</i>
  parameter is an enumerated string whose values determine the number and type
  of output files created.  Up to three files are created: the <span style="font-family: monospace;">".txt"</span>, <span style="font-family: monospace;">".log"</span>,
  and <span style="font-family: monospace;">".gki"</span> files (see the description for the <i>output</i> parameter).
  Possible values  for <i>verbose</i> and the files created are as follows:
  <div class="highlight-default-notranslate"><pre>
  Value:      Files Created:
  
  short       (an 80-char .txt file and a .gki file)
  long        (a 125-char .txt file, a .log file, a .gki file)
  nolog       (a 125-char .txt file and a .gki file)
  nogki       (a 125-char .txt file and a .log file)
  txtonly     (a 125-char .txt file)
  stxtonly    (an 80-char .txt file)
  </pre></div>
  The <i>fields</i> task 
  may be used to strip out selected columns from the .txt files.  The 125-char
  may be printed without wrapping the lines either in landscape mode for
  a laser printer, or on a 132 column lineprinter.
  </dd>
  </dl>
  <dl id="l_imupdate">
  <dt><b>imupdate = <span style="font-family: monospace;">"no"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imupdate' Line='imupdate = "no"' -->
  <dd>Update the image header with the computed velocities?  If set to yes, then
  the image will be updated with the observed and heliocentric velocities
  by adding the <i>keywpars.vobs</i> and <i>keywpars.vhelio</i> keywords
  respectively.  Two-dimensional spectra cannot be updated.  Additional keywords
  defined in the <i>keywpars</i> pset will also be updated.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Output graphics device.
  </dd>
  </dl>
  <p style="text-align:center">CONTROL PARAMETERS
  
  </p>
  <dl id="l_interactive">
  <dt><b>interactive = <span style="font-family: monospace;">"yes"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = "yes"' -->
  <dd>Process the spectra interactively?  
  </dd>
  </dl>
  <dl id="l_autowrite">
  <dt><b>autowrite = <span style="font-family: monospace;">"yes"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='autowrite' Line='autowrite = "yes"' -->
  <dd>Automatically record the last fit to the log file when moving to the 
  next/previous spectrum or quitting? If set to <span style="font-family: monospace;">"no"</span>, the user will be 
  queried whether to write the results if no write was performed, and 
  possibly queried for a file name if <i>output</i> isn't set.  
  </dd>
  </dl>
  <dl id="l_autodraw">
  <dt><b>autodraw = <span style="font-family: monospace;">"yes"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='autodraw' Line='autodraw = "yes"' -->
  <dd>Automatically redraw the new fit after it changes.  If set to the default
  <span style="font-family: monospace;">"yes"</span> then the old fit is erased and a new one computed and drawn after 
  the <span style="font-family: monospace;">'g'</span>, <span style="font-family: monospace;">'y'</span>, <span style="font-family: monospace;">'d'</span>, or <span style="font-family: monospace;">'b'</span> keystrokes.  If set to <span style="font-family: monospace;">"no"</span>, then old fits are not
  erased and the user must redraw the screen with an <span style="font-family: monospace;">'r'</span> keystroke.
  </dd>
  </dl>
  <dl id="l_ccftype">
  <dt><b>ccftype = <span style="font-family: monospace;">"image"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccftype' Line='ccftype = "image"' -->
  <dd>Type of output to create when writing out the correlation function with
  the <span style="font-family: monospace;">":wccf file"</span> command.  Possible choices are <span style="font-family: monospace;">"text"</span> which will be a
  simple list of (lag,correlation_value) pairs, or <span style="font-family: monospace;">"image"</span> which will be an
  IRAF image whose header would describe the lag limits and selected peak.
  </dd>
  </dl>
  <p style="text-align:center">ADDITIONAL PARAMETER SETS
  
  </p>
  <dl id="l_observatory">
  <dt><b>observatory = <span style="font-family: monospace;">"kpno"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observatory' Line='observatory = "kpno"' -->
  <dd>The location of the observations, as defined by the <i>noao.observatory</i>
  task.  The image header keyword OBSERVAT will override this parameter, thus
  allowing for images which were taken at another observatory to be properly
  corrected.  These values are used in the heliocentric correction routines.
  </dd>
  </dl>
  <dl id="l_continpars">
  <dt><b>continpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='continpars' Line='continpars = ""' -->
  <dd>The continuum subtraction parameters as described in the <i>continpars</i> 
  named pset.
  </dd>
  </dl>
  <dl id="l_filtpars">
  <dt><b>filtpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filtpars' Line='filtpars = ""' -->
  <dd>The parameter set defining the parameters to be used in filtering the
  data prior to the correlation. 
  </dd>
  </dl>
  <dl id="l_keywpars">
  <dt><b>keywpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='keywpars' Line='keywpars = ""' -->
  <dd>The image header keyword translation table as described in 
  the <i>keywpars</i> named pset.
  </dd>
  </dl>
  <p style="text-align:center">RV PACKAGE PARAMETERS
  
  </p>
  <dl id="l_dispaxis">
  <dt><b>dispaxis = 1,  nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispaxis' Line='dispaxis = 1,  nsum = 1' -->
  <dd>Parameters for defining vectors in 2D images.  The
  dispersion axis is 1 for line vectors and 2 for column vectors.
  A DISPAXIS parameter in the image header has precedence over the
  <i>dispaxis</i> parameter. 
  </dd>
  </dl>
  <dl id="l_z_threshold">
  <dt><b>z_threshold = 0.2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='z_threshold' Line='z_threshold = 0.2' -->
  <dd>Redshift value at which the output logs switch from printing velocities in 
  units of Km/s to redshift z values.
  </dd>
  </dl>
  <dl id="l_tolerance">
  <dt><b>tolerance = 1.0e-5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tolerance' Line='tolerance = 1.0e-5' -->
  <dd>Fitting tolerance for Least Squares fitting.
  </dd>
  </dl>
  <dl id="l_maxiters">
  <dt><b>maxiters = 100</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxiters' Line='maxiters = 100' -->
  <dd>Maximum number of iterations for Least Squares fitting or any other iterative
  algorithm.
  </dd>
  </dl>
  <dl id="l_interp">
  <dt><b>interp = <span style="font-family: monospace;">"poly5"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interp' Line='interp = "poly5"' -->
  <dd>Interpolator used when rebinning the data to a log-linear dispersion.   See 
  the section on interpolation for more information.  Possible choices are
  <span style="font-family: monospace;">"nearest"</span>, <span style="font-family: monospace;">"linear"</span>, <span style="font-family: monospace;">"poly3"</span>, <span style="font-family: monospace;">"poly5"</span>, <span style="font-family: monospace;">"spline3"</span>, and <span style="font-family: monospace;">"sinc"</span>.
  </dd>
  </dl>
  <dl id="l_line_color">
  <dt><b>line_color = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='line_color' Line='line_color = 1' -->
  <dd>Color index of overlay plotting vectors.  This parameter has no effect on
  devices which do not support color vectors.
  </dd>
  </dl>
  <dl id="l_text_color">
  <dt><b>text_color = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='text_color' Line='text_color = 1' -->
  <dd>Color index of plot text annotation.  This parameter has no effect on
  devices which do not support color vectors.
  </dd>
  </dl>
  <dl id="l_observatory">
  <dt><b>observatory = <span style="font-family: monospace;">"observatory"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observatory' Line='observatory = "observatory"' -->
  <dd>Observatory at which the spectra were obtained if not specified in the
  image header by the keyword OBSERVAT.  This parameter is used by several
  tasks in the package through parameter redirection so this parameter may be
  used to affect all these tasks at the same time.  The observatory may be
  one of the observatories in the observatory database, <span style="font-family: monospace;">"observatory"</span> to
  select the observatory defined by the environment variable <span style="font-family: monospace;">"observatory"</span> or
  the parameter <b>observatory.observatory</b>, or <span style="font-family: monospace;">"obspars"</span> to select the
  current parameters set in the <b>observatory</b> task.  See help for
  <b>observatory</b> for additional information.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Fxcor</i> performs a Fourier cross-correlation on the input list of object
  and template spectra.  Object spectra may be either one or two dimensional
  (in `echelle' or `multispec' format), and may be correlated against a one
  or two dimensional template.  If the template spectrum is only one dimensional
  but the object is two dimensional, the template is used to correlate each of
  the apertures specified by the <i>apertures</i> parameter in the object 
  spectrum.  Two dimensional templates will correlate corresponding apertures.
  </p>
  <p>
  If the input spectra are not dispersion corrected (DC-FLAG parameter missing
  or less than zero), or the <i>pixcorr</i> parameter is turned on, then only 
  a pixel space correlation is done.  This is
  appropriate for a simple cross-correlation of images whether spectra or not.
  If the spectra are dispersion corrected, a log binned correlation is
  performed and various radial velocity measurements are made. At a minimum,
  a relative velocity between the object and template spectra is produced.
  If the image headers contain sufficient information for heliocentric
  velocity corrections (see help for <b>keywpars</b>), the corrections are
  computed and possibly recorded in the image header (see below for a full
  explanation of the computed velocities).  If the value of the 
  heliocentric velocity is returned as INDEF, the user may use the <span style="font-family: monospace;">'v'</span>
  keystroke to see the full results of the correlation, including errors
  which occured causing the corrections to not be done.
  </p>
  <p>
  A number of operations may be performed to prepare the data for
  correlation.  If a linear wavelength dispersion is defined, the spectra are
  rebinned to a log-linear dispersion using the interpolant set by the package
  parameter <i>interp</i> (See the section on interpolation for details).  
  At this time only linear input dispersions are supported for rebinning.
  The starting and ending wavelength for
  both spectra will remain the same, but the dispersion in log space will be
  determined from the <i>rebin</i> parameter if the input disersions aren't
  equal, or from the spectrum's endpoints and number of pixels if they are
  equal.  For example, assuming <i>rebin</i> is set to <span style="font-family: monospace;">"smallest"</span>, if object
  one and the template have the same input log dispersion of 0.5e-4 A/pix the
  data will not be rebinned.  Object two with a wpc of 0.4e-4 A/pix will force
  the template to be rebinned to a common wpc of 0.4e-4 A/pix.  If the third
  object on the list then has a dispersion of 0.3e-4 A/pix, the template will
  again be rebinned from the original 0.5e-4 A/pix dispersion to a new 0.3e-4
  A/pix dispersion.  If object three and the template are the same star, the
  template spectrum will suffer from interpolation errors that should be
  considered when analyzing the results.  The output .txt file will update
  every time the common dispersion is changed.  The suggested course of action
  is to bin all spectra to the same dispersion, preferably a log-linear one,
  prior to executing this package.
  </p>
  <p>
  If the <i>continuum</i> flag is set to something other than 
  <span style="font-family: monospace;">"none"</span>, the object and/or template data will
  be continuum subtracted using the fitting parameters found in the
  <i>continpars</i> pset on input.  The data are zeroed outside the sample
  region specified by the <i>osample</i> and <i>rsample</i> parameters, 
  the ends of each region are apodized, and the bias is then subtracted.
  If the <i>filter</i> flag is set to something other than
  <span style="font-family: monospace;">"none"</span>, the data are Fourier filtered according to the parameters in 
  the <i>filtpars</i> pset prior to the correlation computation.
  </p>
  <p>
  Once the correlation is computed, the maximum peak within the window
  specified by the <i>wincenter</i> and <i>window</i> parameters is found and
  fit according to the <i>width</i> or <i>height</i> and <i>peak</i> parameters.
  A small, unlabeled plot of the entire cross correlation function (hereafter
  CCF) is drawn above a larger, expanded plot centered on the peak in a window
  of size specified by the <i>window</i> parameter.  The dashed lines in the
  small plot show the limits of the expanded plot.  The bottom axis of the
  expanded plot is labeled with pixel lag and, if dispersion information is
  present, the top axis is labeled with relative velocity.  To choose a
  different peak to fit, move the cursor to the top plot of the whole ccf and
  hit the <span style="font-family: monospace;">'z'</span> keystroke at the desired peak.  The plot will be redrawn with
  the new peak now centered in the window and a fit automatically done.  The
  status line will contain a summary of the pixel shift from the fit and
  optional velocity information.  The <span style="font-family: monospace;">'v'</span> keystroke may be used to suspend
  graphics and get a more detailed description of the correlation and fit, and
  the <span style="font-family: monospace;">'+'</span> keystroke will toggle the status line output.  To view the
  antisymmetric noise component of the correlation function, simply hit the
  <span style="font-family: monospace;">'a'</span> keystroke followed by any keystroke to return to the correlation plot.
  Similarly, the <span style="font-family: monospace;">'e'</span> keystroke may be used to preview the summary plot of the
  correlation, again hitting any key to return to the correlation.  An
  overplot of the subtracted fit (residuals) may be seen with the <span style="font-family: monospace;">'j'</span>
  keystroke.
  </p>
  <p>
  If the user is dissatisfied with the fit to the peak, he can mark the left
  and right side of the peak with the <span style="font-family: monospace;">'g'</span> keystroke to redo the fit, or else
  set the cursor to mark a cutoff with the <span style="font-family: monospace;">'y'</span> keystroke, and all points from
  the peak maximum to the cursor will be fit.  To fix the background of a
  Gaussian fit (i.e. change the <i>background</i> parameter graphically), type
  the <span style="font-family: monospace;">'b'</span> keystroke at the desired level, and a new fit will be done.  The <span style="font-family: monospace;">'r'</span>
  keystroke may be used at any time to redraw the plot, and the <span style="font-family: monospace;">'x'</span> keystroke
  can be used to compute a new correlation if any of the parameters relating
  to the correlation are changed (e.g. the apodize percentage).  New
  correlations are automatically computed when new images are read in, the
  data are continuum subtracted, a different region is selected for
  correlation, or Fourier filtering is done.  Certain colon commands from
  within the Fourier or Spectrum mode will also cause a new correlation to be
  computed when these modes are exited.
  </p>
  <p>
  The <span style="font-family: monospace;">'c'</span> keystroke may be used to get a printout of the cursor position in both 
  lag and relative velocity.  The cursor may be positioned in either the
  unlabeled CCF plot on the top, or in the zoomed plot on the bottom.  This is
  useful for judging the FWHM calculation, or estimating the velocity of a
  peak without using the <span style="font-family: monospace;">'z'</span> keystroke to zoom and fit.  Note that because of
  the plotting implementation, the normal cursor mode keystroke <i>shift-C</i>
  should not be used as it may return erroneous results depending upon cursor
  position.  Note also that velocities printed are only approximate relative
  velocities, and the user should properly fit a peak or use the <span style="font-family: monospace;">":correction"</span>
  command to get a true heliocentric velocity.
  </p>
  <p>
  For binary star work, the user may type the <span style="font-family: monospace;">'d'</span> and/or <span style="font-family: monospace;">'-'</span> keystrokes to fit
  and then subtract up to four Gaussians to the peaks. See the discussion
  below for more deatils on the use of this feature.  If multiple peaks were
  fit, a separate entry will be made in the log file for each peak with a
  comment that it was part of a blended peak.  The metacode file will contain
  only one summary plot with each peak marked with it's heliocentric velocity
  or pixel shift.
  </p>
  <p>
  To move to the next spectrum in a list (of images or apertures), simply hit
  the <span style="font-family: monospace;">'n'</span> keystroke.  Similary, the <span style="font-family: monospace;">'p'</span> keystroke will move to the previous
  spectrum.  These commands have a hitch, though.  By default, the
  next/previous commands will move first to the next template in the template
  image list.  Once the end of the template image list is reached, the next
  spectrum will be the next aperture in the list specified by <i>apertures</i>,
  resetting the template image list automatically and possibly updating the
  aperture in the template image as well.  Finally, after correlating all of
  the templates against all of the apertures, the next/previous command will
  move to the next object image, again resetting the template image and/or
  aperture list.  To override this sequence, the user may use the <span style="font-family: monospace;">":next"</span> or
  <span style="font-family: monospace;">":previous"</span> commands and specify one of <span style="font-family: monospace;">"aperture"</span>, <span style="font-family: monospace;">"object"</span>, or
  <span style="font-family: monospace;">"template"</span>.  If <i>autowrite</i> is set, the results of the last fit will be
  written to the log automatically.  To write any one of the fits explicitly,
  use the <span style="font-family: monospace;">'w'</span> keystroke.
  </p>
  <p>
  The <i>fxcor</i> task also contains three submodes discussed in detail below.
  Briefly, the <span style="font-family: monospace;">'f'</span> keystroke will put the user in the <span style="font-family: monospace;">"fourier mode"</span>,
  where he can examine the Fourier transform of the spectra in various
  ways and change/examine the filtering parameters.  The <span style="font-family: monospace;">'o'</span> and <span style="font-family: monospace;">'t'</span>
  keystrokes let the user examine and fit the continuum for the object
  and template spectra, respectively, using the <b>icfit</b> commands.
  Upon exiting the continuum fitting the spectra are continuum subtracted 
  and a new correlation is computed.  Finally the <span style="font-family: monospace;">'s'</span> keystroke will put
  the user in <span style="font-family: monospace;">"spectrum mode"</span>, in which he may graphically select the
  region to be correlated, compute an approximate shift using the cursor,
  or simply examine the two spectra in a variety of ways.  All of these
  submodes are exited with the <span style="font-family: monospace;">'q'</span> keystroke, after which the correlation
  will be redone, if necessary, and the CCF plot redrawn.
  </p>
  <p>
  Colon commands may also be used to examine or change parameter values in
  any of the <i>filtpars</i>, <i>continpars</i>, or <i>keywpars</i>
  psets.  Simply type a <span style="font-family: monospace;">':'</span> followed by the parameter name and an optional
  new value.  The <i>observatory</i> parameters may only be changed outside
  the task.
  </p>
  <p>
  To exit the task, type <span style="font-family: monospace;">'q'</span>.  Results will be saved
  to the logfile automatically if one was specified, otherwise the user will
  be asked if he wants to save the results, and if so, queried for a file name
  before exiting if no <i>output</i> file was defined.
  </p>
  <p>
  If the <i>output</i> parameter is set, several files will be created
  depending on the value of the <i>verbose</i> parameter (see the parameter
  description for details).  These include a file with a <span style="font-family: monospace;">".gki"</span> suffix
  containing metacode output of a summary plot, a <span style="font-family: monospace;">".txt"</span> suffix file
  containing text output in the standard IRAF 'list' format containing either
  verbose or non-verbose output, and a third file having a <span style="font-family: monospace;">".log"</span> suffix
  containing a verbose description of the correlation and fit, as well as any
  warning messages.  This contents of the <span style="font-family: monospace;">".log"</span> file is identical to what is
  seen with the <span style="font-family: monospace;">'v'</span> keystroke.  If the computed relative velocity exceeds the
  package parameter <i>z_threshold</i>, the <span style="font-family: monospace;">".txt"</span> file will contain redshift Z
  values rather than the default velocities.  Text file output may be have
  selected columns extracted using the iraf <i>fields</i> task (where string
  valued fields will have blank spaces replaced with an underscore), and
  specific metacode plots may be extracted or displayed with the iraf
  <i>gkiextract</i> and/or <i>stdgraph</i>/<i>gkimosaic</i> tasks.
  </p>
  <p>
  (References: Tonry, J. and Davis, M. 1979 <i>Astron. J.</i> <b>84,</b> 1511, 
  and Wyatt, W.F. 1985 in <i>IAU Coll. No 88, Stellar Radial Velocities</i>, 
  p 123).
  </p>
  </section>
  <section id="s_fourier_mode_description">
  <h3>Fourier mode description</h3>
  <p>
  Fourier mode is entered from the main task mode via the <span style="font-family: monospace;">'f'</span> keystroke.  By 
  default, the user is presented with a split plot of the power spectra of
  the object and template spectra (object on top) and the requested filter
  overlayed. The X-axis is double-labeled with wavenumbers on the bottom of
  the screen and frequency on top.  The <span style="font-family: monospace;">":log_scale"</span> command can be used to 
  toggle the log scaling of the Y-axis of the plot, and the <span style="font-family: monospace;">":overlay"</span> command 
  will toggle whether or not the filter function (if specified) is overlayed 
  on the plot.  By default the entire power spectrum is displayed, but 
  the <span style="font-family: monospace;">":zoom"</span> command may be used to specify a blowup factor for the 
  display (e.g. <span style="font-family: monospace;">":zoom 2"</span> will display only the first half of the power 
  spectrum).  Plot scaling and content parameters are learned for the next 
  invocation of this mode.
  </p>
  <p>
  The plot contents may also be changed through various keystroke commands.
  The <span style="font-family: monospace;">'p'</span> keystroke will display the power spectrum (the default) and the <span style="font-family: monospace;">'f'</span>
  keystroke will display the two FFT's.   The <span style="font-family: monospace;">'b'</span> and <span style="font-family: monospace;">'g'</span> 
  keystrokes may be used to examine the power spectra and FFT's 
  respectively <i>before</i> filtering.  The user can determine the period 
  trend in the data by placing the cursor at a particular wavenumber/frequency 
  and hitting the <span style="font-family: monospace;">'i'</span> keystroke (this command will not work on a plot of 
  the filtered spectra).  The <span style="font-family: monospace;">'r'</span> key will redraw whichever plot is currently
  selected and a <span style="font-family: monospace;">'q'</span> will return the user to the mode which called the Fourier
  mode (i.e. either the main task mode or the Spectrum mode).  The Spectrum
  mode may be entered from within Fourier mode via the <span style="font-family: monospace;">'s'</span> keystroke.
  </p>
  <p>
  Colon commands are also used to specify or examine the filtering parameters
  by simply typing a <span style="font-family: monospace;">':'</span> followed by the parameter name found in 
  the <i>filtpars</i> pset.
  </p>
  </section>
  <section id="s_continuum_mode_description">
  <h3>Continuum mode description</h3>
  <p>
  Automatic continuum subtraction is controlled by the <i>continpars</i>
  pset.  These may be reset from the main
  correlation function mode.  To interactively fit and modify the continuum
  fitting parameters the <span style="font-family: monospace;">'o'</span> and <span style="font-family: monospace;">'t'</span> keys are used.  This enters
  the ICFIT package which is described elsewhere (see <i>icfit</i>).  
  Exiting the fitting,
  with <span style="font-family: monospace;">'q'</span>, causes a recomputation of the correlation function and peak
  fit.  To view the flattened spectra use the spectrum review mode
  entered with the <span style="font-family: monospace;">'s'</span> key.  Fitting parameters changed while doing the
  interactive continuum fitting are learned.
  </p>
  </section>
  <section id="s_spectrum_mode_description">
  <h3>Spectrum mode description</h3>
  <p>
  Spectrum mode is entered from the main or fourier mode via the <span style="font-family: monospace;">'s'</span>
  keystroke.  The user may select plots of the original input spectra with the
  <span style="font-family: monospace;">'i'</span> keystroke, or the continuum subtracted spectra with the <span style="font-family: monospace;">'n'</span> keystroke,
  If the data have been rebinned to a log scale, they will still be plotted 
  on a linear wavelength scale for clarity.  Pixel data are plotted identically
  to how they were read.  (NOTE: For rebinned spectra, a slight slope may be
  noticed in the 'original' data because of rebinning effects.)
  In addition, a sample regions (if selected) for the correlation are marked
  on the bottom of both plots.  To select a new sample region, use the <span style="font-family: monospace;">'s'</span>
  keystroke to select the endpoints of the region.  An <span style="font-family: monospace;">'s'</span> keystroke on the
  top plot will select a sample region for the object spectrum, and an <span style="font-family: monospace;">'s'</span> on
  the bottom plot will select a template sample, using the <span style="font-family: monospace;">'b'</span> keystroke will
  select both samples simultaneously.  The regions may be selected
  explicitly by using the <span style="font-family: monospace;">":osample"</span> and <span style="font-family: monospace;">":rsample"</span> commands, and selected
  sample regions may be cleared entirely using the (e.g.) <span style="font-family: monospace;">":osample *"</span> command,
  or individual regions may be unselected by putting the cursor within the
  region and typing <span style="font-family: monospace;">'u'</span>.  See the
  parameter description for syntax of the sample ranges.  Regions will be
  checked and possibly truncated to see if they 
  lie within the range of the spectrum.  The <span style="font-family: monospace;">'d'</span>
  keystroke may be used to print the difference in pixels (and/or velocity)
  between two points on the spectrum.  This is useful for getting an
  approximate shift.  Fourier mode may be entered via the <span style="font-family: monospace;">'f'</span> keystroke.  To
  return to the correlation simply type <span style="font-family: monospace;">'q'</span> or <span style="font-family: monospace;">'x'</span>.
  </p>
  <p>
  In addition to the above commands, the user may examine or change the 
  parameters in the <i>continpars</i> pset by simply typing a <span style="font-family: monospace;">':'</span> followed
  by the parameter name. Changing these values will not cause a new correlation
  until an explicit command is given to redo the continuum subtraction.
  </p>
  <p>
  (NOTE: More functionality is planned for this mode.)
  </p>
  </section>
  <section id="s_interpolation">
  <h3>Interpolation</h3>
  <p>
  The interpolation type is set by the package parameter <i>interp</i>.
  The available interpolation types are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  nearest - nearest neighbor
   linear - linear
    poly3 - 3rd order polynomial
    poly5 - 5th order polynomial
  spline3 - cubic spline
     sinc - sinc function
  </pre></div>
  <p>
  The default interpolation type is a 5th order polynomial (poly5).
  </p>
  <p>
  The choice of interpolation type depends on the type of data, smooth
  verses strong, sharp, undersampled features, and the requirements of
  the user.  The <span style="font-family: monospace;">"nearest"</span> and <span style="font-family: monospace;">"linear"</span> interpolation are somewhat
  crude and simple but they avoid <span style="font-family: monospace;">"ringing"</span> near sharp features.  The
  polynomial interpolations are smoother but have noticible ringing
  near sharp features.  They are, unlike the sinc function described
  below, localized.
  </p>
  <p>
  In V2.10 a <span style="font-family: monospace;">"sinc"</span> interpolation option is available.  This function
  has advantages and disadvantages.  It is important to realize that
  there are disadvantages!  Sinc interpolation approximates applying a phase
  shift to the fourier transform of the spectrum.  Thus, repeated
  interpolations do not accumulate errors (or nearly so) and, in particular,
  a forward and reverse interpolation will recover the original spectrum
  much more closely than other interpolation types.  However, for
  undersampled, strong features, such as cosmic rays or narrow emission or
  absorption lines, the ringing can be more severe than the polynomial
  interpolations.  The ringing is especially a concern because it extends
  a long way from the feature causing the ringing; 30 pixels with the
  truncated algorithm used.  Note that it is not the truncation of the
  interpolation function which is at fault!
  </p>
  <p>
  Because of the problems seen with sinc interpolation it should be used with
  care.  Specifically, if there are no undersampled, narrow features it is a
  good choice but when there are such features the contamination of the
  spectrum by ringing is much more severe than with other interpolation
  types.
  </p>
  </section>
  <section id="s_deblending">
  <h3>Deblending</h3>
  <p>
  When entering the deblending function, two cursor settings define the
  local background, which may be sloping, and the region to be fit.  Note
  that both the x and y of the cursor position are used.  The lines to be
  fit are then entered either with the cursor (<span style="font-family: monospace;">'m'</span>), or by typing the
  shifts (<span style="font-family: monospace;">'t'</span>).  The latter is useful if the shifts of the
  lines are known accurately and if fits restricting the absolute or
  relative positions of the lines will be used (i.e. <span style="font-family: monospace;">'a'</span>, <span style="font-family: monospace;">'b'</span>, <span style="font-family: monospace;">'d'</span>,
  <span style="font-family: monospace;">'e'</span>).  A maximum of four lines may be fit.  If fewer lines are desired,
  exit the marking step with <span style="font-family: monospace;">'q'</span>.
  </p>
  <p>
  There are six types of fits which may be selected.  This covers all
  combinations of fixing the absolute positions, the relative positions,
  the sigmas to be the same, and letting all parameters be determined.
  In all cases the peak intensities are also determined for each line.
  The options are given below with the appropriate key and mnemonic.
  </p>
  <div class="highlight-default-notranslate"><pre>
  a=0p1s      Fit intensities and one sigma with positions fixed
  b=1p1s      Fit intensities, one position, and one sigma with
                      separations fixed
  c=np1s      Fit intensities, positions, and one sigma
  d=0pns      Fit intensities and sigmas with positions fixed
  e=1pns      Fit intensities, one position, and sigmas with
                      separations fixed
  f=npns      Fit intensities, positions, and sigmas
  </pre></div>
  <p>
  This list may also be printed with the <span style="font-family: monospace;">'?'</span> key when in the deblending
  function.
  </p>
  <p>
  As noted above, sometimes the absolute or relative shifts of the
  lines are known a priori and this information may be entered by typing
  the shifts explicitly using the <span style="font-family: monospace;">'t'</span> option during marking.  In
  this case, one should not use the <span style="font-family: monospace;">'c'</span> or <span style="font-family: monospace;">'f'</span> fitting options since they
  will adjust the line positions to improve the fit.  Options <span style="font-family: monospace;">'a'</span> and <span style="font-family: monospace;">'d'</span>
  will not change the lines positions and fit for one or more sigmas.
  Options <span style="font-family: monospace;">'b'</span> and <span style="font-family: monospace;">'e'</span> will maintain the relative positions of the lines
  but allow an other than expected shift.
  </p>
  <p>
  After the fit, the modeled lines are overplotted.  The line center,
  flux, equivalent width, and full width half maximum are printed on the
  status line for the first line.  The values for the other lines and
  the RMS of the fit may be examined by scrolling the status line
  using the <span style="font-family: monospace;">'+'</span>, <span style="font-family: monospace;">'-'</span>, and <span style="font-family: monospace;">'r'</span> keys.  Velocity information is obtained by
  typing the <span style="font-family: monospace;">'v'</span> keystroke.  To continue enter <span style="font-family: monospace;">'q'</span>.
  </p>
  <p>
  The fitting may be repeated with different options until exiting with <span style="font-family: monospace;">'q'</span>.
  </p>
  <p>
  The fitted model may be subtracted from the data (after exiting the
  deblending function) using the <span style="font-family: monospace;">'-'</span> (minus)
  keystroke to delimit the region for which the subtraction is to
  be performed. This allows you to fit a portion of a peak which may
  be contaminated by a blend and then subtract away the entire peak
  to examine the remaining components.
  </p>
  <p>
  The fitting uses an interactive algorithm based on the Levenberg-Marquardt
  method.  The iterations attempt to improve the fit by varying the parameters
  along the gradient of improvement in the chi square.  This method requires
  that the initial values for the parameters be close enough that the
  gradient leads to the correct solution rather than an incorrect local
  minimum in the chi square.  The initial values are determined as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  1.  The initial line centers are those specified by the user
      either by marking with the cursor or entering the shifts.
  2.  The initial peak intensities are the data values at the
      given line centers with the marked continuum subtracted.
  3.  The initial sigmas are obtained by dividing the width of
      the marked fitting region by the number of lines and then
      dividing this width by 4.
  </pre></div>
  <p>
  Note that each time a new fitting options is specified the initial parameters
  are reset.  Thus the results do not depend on the history of previous fits.
  However, within each option an iteration of parameters is performed as
  described next.
  </p>
  <p>
  The iteration is more likely to fail if one initially attempts to fit too
  many parameters simultaneously.  A constrained approach to the solution
  is obtained by iterating starting with a few parameters and then adding
  more parameters as the solution approaches the true chi square minimum.
  This is done by using the solutions from the more constrained options
  as the starting point for the less constrained options.  In particular,
  the following iterative constraints are used during each option:
  </p>
  <div class="highlight-default-notranslate"><pre>
  a: 0p1s
  b: 0p1s, 1p1s
  c: 0p1s, 1p1s, np1s
  d: 0p1s, 0pns
  e: 0p1s, 1p1s, 1pns
  f: 0p1s, 1p1s, np1s, npns
  </pre></div>
  <p>
  For example, the most general fit, <span style="font-family: monospace;">'f'</span>, first fits for only a single sigma
  and the peak intensities, then allows the lines to shift but keeping the
  relative separations fixed. Next, the positions are allowed to vary
  independently but still using a single sigma, and then allows all parameters
  to vary.
  </p>
  <p>
  To conclude, here are some general comments.  The most restrictive <span style="font-family: monospace;">'a'</span>
  key will give odd results if the initial positions are not close to the
  true centers.  The most general <span style="font-family: monospace;">'f'</span> can also lead to incorrect results
  by using unphysically different sigmas to make one line very narrow and
  another very broad in an attempt to fit very blended lines.  The
  algorithm works well when the lines are not severely blended and the
  shapes of the lines are close to Gaussian.
  </p>
  </section>
  <section id="s_peak_fitting_finding_algorithms">
  <h3>Peak fitting/finding algorithms</h3>
  <p>
  Determining the center of the cross correlation peak is the key step in
  measuring a relative shift or velocity between the object and template.
  The width of the correlation peak is also of interest for measuring
  a line broadening between the two samples.  Since people have different
  preferences and prejudices about these important measurements, a variety
  of methods with a range of parameters is provided.
  </p>
  <p>
  In all cases, one must specify the fitting function and a sample width; i.e.
  the range of points about the correlation peak to be used in the
  measurement.  Note that the width defines where the fitting weights vanish
  and should be something like the full width.  For the CENTER1D algorithm the
  maximum weights are at the half width points while for the other methods
  (with the exception of <span style="font-family: monospace;">"sinc"</span>) greater weight is given to data nearer the
  center.
  </p>
  <p>
  The width may be specified in three ways.  The first is as an actual
  width in pixels.  This is the most straightforward and is independent
  of quirks in the actual shape of the peak.  The second way is to find
  where the correlation function crosses a specified height or level.
  The height may be specified in normalized correlation units or as a
  fraction of the peak height.  The former is equivalent to the
  interactive <span style="font-family: monospace;">'y'</span> key setting while the latter may be used to select some
  <span style="font-family: monospace;">"flux"</span> point.  A value of 0.5 in the latter would be approximately the
  full width at half intensity point except that the true zero or base of
  the peak is somewhat uncertain and one needs to keep in mind that the
  weights go to zero at this point.  Note that a level may be negative.
  In this method the actual width may go to zero or include the entire
  data range if the level fall above the peak or below the minimum of the
  correlation.  The minimum and maximum width parameters are applied to
  constrain the fitting region.  The last method is to interactively mark
  the fitting region with the <span style="font-family: monospace;">'g'</span> key.
  </p>
  <p>
  There are five methods for determining the correlation peak position.  The
  CENTER1D algorithm has been heavily used in IRAF and is quite stable and
  reliable.  It is independent of a particular model for the shape of the peak
  or the background determination and is based on bisecting the integral.  It
  uses antisymmetric weights with maxima at points half way between the
  estimated center and the fitting region endpoint.  A parabola fit and sinc
  interpolation is also independent of background determinations.  The
  parabola is included because it is a common method of peak centering.
  </p>
  <p>
  The sinc option uses a sinc interpolator together with a maximization
  (actually a minimization algorithm) function to determine the peak height
  and center.  A width will be computed only if a background level has been
  set and is determined empirically based on the peak height and background.
  Point weighting is not used in this option.
  </p>
  <p>
  The gaussian and lorentzian function fits are model dependent and
  determine a center, width, and peak value.  The background may also
  be determined simultaneously but this extra degree of freedom
  for a function which is not strictly gaussian or lorentzian may
  produce results which are sensitive to details of the shape of the
  correlation function.  The widths reported are the full width at
  half maximum from the fits.
  </p>
  <p>
  The parabola, gaussian, and lorentzian methods use weights which
  vary continuously from 1 at the estimated center to zero at the
  endpoints of the fitting region.  The functional form of the
  weights is a power law with specified exponent.  A value of zero
  for the exponent produces uniform weights.  However, this is
  discontinuous at the endpoints and so is very sensitive to the data
  window.  A value of one (the default) produces linearly decreasing weights.
  </p>
  <p>
  All these methods produce centers which depend on the actual
  data points and weights used.  Thus, it is important to iterate
  using the last determined center as the center of the data window
  with continuous weights in order to find a self-consistent center.
  The methods are iterated until the center does not change by more
  than 0.01 pixels or a maximum of 100 iterations is reached.
  </p>
  <p>
  Errors in the pixel shift are computed from the center parameter of the fitting
  function.  Velocity errors are computed based on the fitted peak height and
  the antisymmetric noise as described in the Tonry &amp; Davis paper (1979,
  <i>Astron. J.</i> <b>84,</b> 1511). Dispersion/pixel-width errors are 
  not computed in this release but are planned for a future release.
  </p>
  <p>
  The initial peak fit will be the maximum of the CCF.  This will be the only 
  peak fit in non-interactive mode but a confidence level will be entered in
  the logfile.  In interactive mode, the user may select a different peak with
  the <span style="font-family: monospace;">'z'</span> keystroke, and the maximum peak within the specified <i>window</i>
  (centered on the cursor) will be fit.  The user has full control in interactive
  mode over the points used in the fit.  Once the endpoints of the peak have
  been selected, the actual data points are shown with <span style="font-family: monospace;">'+'</span> signs on the CCF,
  the fitted curve drawn, and a horizontal bar showing the location of the
  FWHM calculation is displayed.  The status line will show a summary of the 
  fit, and the user may type the <span style="font-family: monospace;">'v'</span> keystroke for a more detailed description
  of the fit and correlation. 
  </p>
  </section>
  <section id="s_velocity_computation_algorithm">
  <h3>Velocity computation algorithm</h3>
  <p>
  Up to three velocities are computed by the task depending on the completeness
  of the images headers and the presence of dispersion information.  If only
  dispersion information is present, a relative velocity, VREL, and an error
  will be computed.  If a full header is present (see the <i>keywpars</i>
  help page), an observed and heliocentric velocity (VOBS and VHELIO
  respectively) will be computed.
  </p>
  <p>
  In short form, here are the equations:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ref_rvobs = catalogue_vel_of_template - H(temp)  # obs. vel. of temp.
  VREL = C * (10 ** (wpc * shift) - 1.)            # relative vel.
  VOBS = ((1+ref_rvobs/C)*(10**(wpc*shift)-1)) * C # observed vel.
  VHELIO = VOBS + H(object)                        # heliocentric vel.
  </pre></div>
  <p>
  where H() is the heliocentric correction for that observation.  The
  equation used for the relative velocity is derived from the standard
  (1+z), and the VOBS equation reflects that the observed velocty is the
  product of (1+z) values for the object and template (this allows for high
  redshift templates to be used).  The date, time, and position of each
  spectrum is found from the image header via the keywords defined in
  <i>keywpars</i>.  In the case of the time the task first looks for a
  keyword defining the UT mid-point of the observation
  (<i>keywpars.utmiddle</i>).   If that is not found any time present in the
  header DATE-OBS (<i>keywpars.date_obs</i>) keyword is used at the UT start
  point, if there is no time in the keyword value then the mid-point UT is
  computed from the exposure time (<i>keywpars.exptime</i>) and UT of
  observation (<i>keywpars.ut</i>) keywords.
  </p>
  <p>
  The keyword added to the template header (as defined by the
  <span style="font-family: monospace;">"vhelio"</span> parameter in the <i>keywpars</i> pset) should be the catalogue velocity 
  of the template.  Since the observation of the template has a slightly
  different heliocentric correction, this is subtracted from the template
  heliocentric velocity so that the <i>observed</i> velocity of the template 
  is used when correcting the relative velocity computed from the shift.  
  This gives the <i>observed</i> velocity of the object wrt the template.  
  Adding the heliocentric correction of the object star then yields the true
  heliocentric velocity of the object.
  </p>
  </section>
  <section id="s_cursor_keys_and_colon_commands_summary">
  <h3>Cursor keys and colon commands summary</h3>
  <p style="text-align:center">CORRELATION MODE COMMANDS
  
  </p>
  <div class="highlight-default-notranslate"><pre>
  ?  Print list of cursor key and colon commands
  -  Subtract blended component from correlation peak
  +  Toggle status line output
  a  Display the antisymmetric noise component of the correlation
  b  Fix the background level for the Gaussian fit
  c  Read out cursor position in pixel lag and velocity
  d  Deblend multiple correlation peak
  e  Preview the summary plot of the correlation
  f  Fourier filtering and FFT display mode
  g  Mark correlation peak lag limits and fit
  I  Interrupt
  j  Plot the residuals of the fit to the peak
  l  Page the current logfile of results
  m  Plot polymarkers of actual CCF points on the plot
  n  Go to next (template --&gt; aperture --&gt; object)
  o  Fit or refit object spectrum continuum for subtraction
  p  Go to previous (template --&gt; aperture --&gt; object)
  q  Quit task
  r  Redraw
  s  Examine object/template spectra and display mode
  t  Fit or refit template spectrum continuum for subtraction
  v  Print full correlation result in text window
  w  Write current correlation results to the log file
  x  Compute correlation
  y  Mark correlation peak lower limit and fit
  z  Expand on different correlation peak using full correlation plot
  
  :apertures [range]               Set/Show list of apertures to process
  :apnum  [aperture]               Set/Show specific aperture to process
  :apodize  [fraction]             Set/Show fraction of endpts to apodize
  :autowrite [y|n]                 Set/Show autowrite param
  :autodraw  [y|n]                 Set/Show autodraw param
  :background  [background|INDEF]  Set/Show background fitting level
  :ccftype  [image|text]           Set/Show type of CCF output
  :comment  [string]               Add a comment to the output logs
  :continuum  [both|obj|temp|none] Set/Show which spectra to normalize
  :correction shift                Convert a pixel shift to a velocity
  :deltav                          Print the velocity per pixel dispersion
  :disp                            Print dispersion info
  :filter  [both|obj|temp|none]    Set/Show which spectra to filter
  :function [gaussian|lorentzian|  Set/Show CCF peak fitting function
                center1d|parabola]
  :height  [height]                Set/SHow CCF peak fit height
  :imupdate  [y|n]                 Set/Show image update flag
  :maxwidth  [width]               Set/Show min fitting width
  :minwidth  [width]               Set/Show max fitting width
  :nbang                           :Next command without a write
  :next [temp|aperture|object]     Go to next correlation pair
  :objects  [list]                 Set/Show object list
  :osample  [range]                Set/Show object regions to correlate
  :output  [fname]                 Set/Show output logfile
  :&lt;parameter&gt; [value]             Set/Show pset parameter value
  :peak  [y|n]                     Set/Show peak height flag
  :pbang                           :Previous command without a write
  :previous [temp|aperture|object] Go to previous correlation pair
  :printz [y|n]                    Toggle output of redshift z values
  :rebin [small|large|obj|temp]    Set/Show the rebin parameter
  :results [file]                  Page results
  :rsample  [range]                Set/Show template regions to correlate
  :show                            List current parameters
  :templates  [list]               Set/Show template list
  :tempvel  [velocity]             Set/Show template velocity
  :tnum  [temp_code]               Move to a specific temp. in the list
  :unlearn                         Unlearn task parameters
  :update                          Update task parameters
  :version                         Show task version number
  :verbose  [y|n]                  Set/Show verbose output flag
  :wccf                            Write out the CCF to an image|file
  :weights  [weight]               Set/Show fitting weights
  :width  [width]                  Set/Show fitting width about peak
  :wincenter  [center]             Set/Show peak window center
  :window  [size]                  Set/Show size of window
  :ymin  [correlation height]      Set/Show lower ccf plot scaling
  :ymax  [correlation height]      Set/Show upper ccf plot scaling
  </pre></div>
  <p style="text-align:center">FOURIER MODE COMMANDS
  
  </p>
  <div class="highlight-default-notranslate"><pre>
  ?  Print list of cursor key and colon commands
  b  Display power spectra before filtering
  f  Enter Fourier mode
  g  Display Fourier transforms before filtering
  i  Print period trend information
  o  Display filtered and unfiltered object spectrum
  p  Display power spectra after filtering
  q  Quit
  r  Redraw
  s  Enter Spectrum mode
  t  Display filtered and unfiltered template spectrum
  x  Return to parent mode
  
  :log_scale [y|n]              Plot on a Log scale?
  :one_image [object|template]  What plot on screen
  :overlay [y|n]                Overlay filt function?
  :&lt;parameter&gt; [value]          Set/Show the FILTERPARS parameter value
  :plot [object|template]       What type of plot to draw on single plot?
  :split_plot [y|n]             Make a split-plot?
  :when [before|after]          Plot before/after filter?
  :zoom [factor]                FFT zoom parameter
  </pre></div>
  <p style="text-align:center">CONTINUUM MODE COMMANDS
  
  </p>
  <p>
  See <b>icfit</b>.
  </p>
  <p style="text-align:center">SPECTRUM MODE COMMANDS
  
  </p>
  <div class="highlight-default-notranslate"><pre>
  ?  Print list of cursor key and colon commands
  b  Select sample regions for both spectra
  d  Print velocity difference between two cursor positions
  f  Enter Fourier mode
  i  Display original input spectra
  n  Display continuum subtracted spectra
  p  Display the prepared spectra prior to correlation
  q  Quit
  r  Redraw
  s  Select sample region endpoints
  u  Unselect a sample region
  x  Return to correlation mode
  
  :&lt;parameter&gt; [value]    Set/Show parameters in CONTINPARS pset
  :osample [list]         List of object sample regions
  :rsample [list]         List of template sample regions
  :show                   List current parameters
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  1. Cross correlate a list of 1-dimensional object spectra against
  three 1-dimensional template spectra, saving results automatically
  and not continuum subtracting or filtering the data:
  
      rv&gt; fxcor.interactive = no              # Do it in batch mode
      rv&gt; fxcor obj* temp1,temp2,temp3 autowrite+ continuum="no"
      &gt;&gt;&gt; filter="no" output="results"
  
  2. Compute a velocity for a list of apertures in a 2-dimensional
  multispec format object image, using only two apertures of a multispec
  image as the templates:
  
      cl&gt; onedspec
      on&gt; scopy object.ms temp apert="8,9" inform="multi" outform="oned"
      on&gt; rv
      rv&gt; fxcor.interactive = no              # Do it in batch mode
      rv&gt; fxcor object.ms temp.0008,temp.0009 apertures="1-7,10,12-35"
  
  In this example, apertures 8 and 9 of the object image will be used
  as the template.  The <i>scopy</i> task is used to extract the aper-
  tures to onedspec format, into two images named "temp.0008" and
  "temp.0009".  The task is then run with all of the apertures in the
  aperture list correlated against the onedspec templates.
  
  3. Compute a velocity by fitting a fixed number of points on the peak,
  using uniform weighting:
  
      rv&gt; fxcor obj temp width=8 weights=0.
  
  4. Compute a velocity by fitting a Gaussian to the points on the CCF
  peak above the 0.1 correlation level.  Constrain the number of points
  to be less than 15, and linearly decrease the weights:
  
      rv&gt; fxcor obj temp func="gaussian" width=INDEF height=0.1
      &gt;&gt;&gt; maxwidth=15 weights=1.
  
  5. Compute a velocity by fitting a Lorentzian to the peak, from the
  peak maximum to it's half power point:
  
      rv&gt; fxcor obj temp func-"lorentz" width=INDEF height=0.5 peak+
      &gt;&gt;&gt; maxwidth=15 weights=1.
  
  6. Process a 1-dimensional object against a 1-dimensional template
  interactively, examining the FFT, and input spectra to define a sample
  region for the correlation:
  
      rv&gt; fxcor obj temp inter+ continuum="both" autowrite- output=""
          Screen is cleared and CCF peak with fit displayed
  
      ... to refit peak, move cursor to left side of peak and type <span style="font-family: monospace;">'g'</span>
      ... move cursor to right side of peak and hit any key
  
          New fit is drawn and results displayed to the status line
  
      ... type the <span style="font-family: monospace;">'v'</span> key for a detailed description of the correlation
  
          Graphics are suspended and the text screen shows various
          parameters of the correlation and fit.
  
      ... type <span style="font-family: monospace;">'q'</span> to get back to graphics mode
  
      ... to examine the FFT's of the spectra, type the <span style="font-family: monospace;">'f'</span> keystroke.
  
          The screen is cleared and a split plot of the two power spectra
          after filtering is drawn with the requested filter (if any)
          overlayed.
      ... type the <span style="font-family: monospace;">'f'</span> keystroke
          The screen is cleared and the absolute value of the two FFT's
          after filtering is plotted, again with the filter overlayed.
      ... type ":overlay no", followed by a <span style="font-family: monospace;">'g'</span> keystroke
          The spectra are redrawn prior to filtering, with no filter over-
          lay
      ... type <span style="font-family: monospace;">'q'</span> to return to correlation mode
  
          The screen is redrawn with the CCF plot and peak fit
  
      ... type <span style="font-family: monospace;">'s'</span> to enter spectrum mode
  
          The screen is cleared and the input spectra displayed
      ... type <span style="font-family: monospace;">'s'</span> to mark the endpoints of sample regions for correl-
      ... ation.  The user can mark either the top or bottom plot to
      ... set sample regions for the object and template respectively.
      ... Then type <span style="font-family: monospace;">'q'</span> to quit this mode
  
          A new correlation is computed and the peak refit automatically
  
      ... type <span style="font-family: monospace;">'q'</span> to quit the task, satisfied with the results
          The user is asked whether he wants to save results
      ... type <span style="font-family: monospace;">'y'</span> or &lt;cr&gt; to save results
          The user is prompted for an output file name since one wasn't
          specified in the parameter set
      ... type in a file name
  
          The task exits.
  
  7. Save the correlation function of two galaxy spectra:
  
      rv&gt; fxcor obj temp inter+ ccftype="text"
          Screen is cleared and CCF peak with fit displayed
  
      ... type ":wccf" to write the CCF
      ... type in a filename for the text output
      ... quit the task
  
      rv&gt; rspectext ccf.txt ccf.fits dtype=interp
      rv&gt; splot ccf.fits
  
     The velocity per-pixel-shift is non-linear and is an approximation
     which works well for low-velocity shifts.  In the case of hi-velocity
     correlations (or when there are many points) it is best to save the
     CCF as a text file where the velocity at each shift is written to
     the file,  then use RSPECTEXT to linearize and convert to an image
     format.  This avoids the task interpolating a saved image CCF in
     cases where it may not be required.
  
  7. Compute a cross-correlation where the template has already been
     corrected to the rest frame and no heliocentric correction is
     required:
  
        Step 1)  Use the HEDIT or HFIX tasks to add the following
                 keywords to the template image:
  
                      DATE-OBS= '1993-03-17T04:56:38.0'
                      RA      = '12:00:00'
                      DEC     = '12:00:00'
                      EPOCH   = 1993.0
                      OBSERVAT= 'KPNO'
                      VHELIO  = 0.0
  
                 These values produce a heliocentric correction of zero
                 to within 5 decimal places.  The VHELIO keyword will
                 default to zero if not present.
  
        Step 2)  Use the HEDIT task to add an OBSERVAT keyword to each
                 of the object spectra.  The OBSERVATORY task can be used
                 get a list of recognized observatories.
  
      Because mixing observatories is not currently well supported, the
      use of the OBSERVAT keyword in <i> both</i> images is the only sure
      way to apply the proper observatory information to each image.  Users
      may wish to derive a zero-valued heliocentric correction for their
      local observatory and use those values instead.
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  continpars, filtpars, observatory, keywpars, onedspec.specwcs, center1d, 
  dispcor, stsdas.fourier
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'FOURIER MODE DESCRIPTION' 'CONTINUUM MODE DESCRIPTION' 'SPECTRUM MODE DESCRIPTION' 'INTERPOLATION' 'DEBLENDING' 'PEAK FITTING/FINDING ALGORITHMS' 'VELOCITY COMPUTATION ALGORITHM' 'CURSOR KEYS AND COLON COMMANDS SUMMARY' 'EXAMPLES' 'SEE ALSO'  -->
  

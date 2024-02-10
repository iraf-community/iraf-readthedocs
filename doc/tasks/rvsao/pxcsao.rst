.. _pxcsao:

pxcsao: Cross-correlate spectra with templates and save results as parameters
=============================================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pxcsao spectra
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_spectra">
  <dt><b>spectra = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectra' Line='spectra = ""' -->
  <dd>List of file names of spectra to analyze.
  @&lt;filename&gt; indicates list should come from file &lt;filename&gt;.
  &lt;filename&gt;[&lt;range&gt;] indicates that a range of apertures in a multispec
  file should be processed, where &lt;range&gt; is a comma- and/or
  hyphen-separated list of numbers.
  </dd>
  </dl>
  <dl id="l_specnum">
  <dt><b>specnum = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specnum' Line='specnum = 0' -->
  <dd>If this is nonzero and <i>spectra</i> contains a single file name, this is
  a range of spectrum numbers in a multispec file which will be cross-
  correlated.  For each spectrum number, n, wavelength dispersion information
  is read from APNUMn, and velocity information is read from APVELn and saved
  in APVELn and APVXCn, the values of which contain multiple values.  If
  specnum is zero, velocity information is in separate keywords for each value.
  </dd>
  </dl>
  <dl id="l_specband">
  <dt><b>specband = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specband' Line='specband = 0' -->
  <dd>Spectrum band if multispec file
  </dd>
  </dl>
  <dl id="l_specext">
  <dt><b>specext = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specext' Line='specext = 0' -->
  <dd>FITS extension containing the spectrum
  </dd>
  </dl>
  <dl id="l_specdir">
  <dt><b>specdir = <span style="font-family: monospace;">"./"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specdir' Line='specdir = "./"' -->
  <dd>Directory containing spectra to analyze.
  </dd>
  </dl>
  <dl id="l_correlate">
  <dt><b>correlate = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='correlate' Line='correlate = yes' -->
  <dd>If <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"velocity"</span>, cross-correlate object spectrum against specified
  template spectrum in log wavelength, displaying spectrum, correlation
  peak (if display mode 1), and detailed results for the best 12 templates.
  If <span style="font-family: monospace;">"wavelength"</span>, cross-correlate object spectrum against specified template
  spectrum in wavelength, displaying spectrum, correlation peak (if display
  mode 1), and detailed results for the best 12 templates.
  If <span style="font-family: monospace;">"pixel"</span>, cross-correlate object spectrum against specified template
  spectrum in pixels, displaying the  spectrum, correlation peak (if display
  mode 1), and detailed results for the best 12 templates.
  If <span style="font-family: monospace;">"no"</span>, display spectrum with previous results read from the spectrum image
  header with no correlation peak plot.  If the spectrum is recorrelated,
  it is processed in log wavelength, and <span style="font-family: monospace;">"velocity"</span> is assumed.
  </dd>
  </dl>
  <dl id="l_templates">
  <dt><b>templates = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='templates' Line='templates = ""' -->
  <dd>Template file or comma-separated list of file names of images to use as
  templates or name of file containing template file names, one per line.
  Apertures of multispec template files can be entered as numbers, lists,
  or ranges enclosed in brackets after each file name in the list or file.
  Wavelength (or pixel) ranges of templates to be correlated can be specified
  by appending :w1-w2 (:p1-p2) to the template name. Multiple pieces of a
  single template spectrum can thus be correlated agains multiple pieces of
  an object spectrum.
  </dd>
  </dl>
  <dl id="l_tempnum">
  <dt><b>tempnum = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tempnum' Line='tempnum = 0' -->
  <dd>If nonzero and <i>templates</i> contains a single file name, this is a range
  of spectrum numbers in a multispec file to be used as templates.
  Wavelength dispersion information is read from APNUMn, and velocity
  information is read from APVELn.
  </dd>
  </dl>
  <dl id="l_tempband">
  <dt><b>tempband = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tempband' Line='tempband = 1' -->
  <dd>Template band if template is multispec file
  </dd>
  </dl>
  <dl id="l_tempdir">
  <dt><b>tempdir = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tempdir' Line='tempdir = ""' -->
  <dd>Directory for template spectra
  </dd>
  </dl>
  <dl id="l_echelle">
  <dt><b>echelle = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='echelle' Line='echelle = no' -->
  <dd>If yes, the spectrum is assumed to be a multispec file containing
  multiple orders.  The range of spectrum numbers (which may not have the
  same numbers as the echelle orders) defined by <i>specnum</i> is used
  for the template rather than the range defined in <i>tempnum</i>.
  </dd>
  </dl>
  <dl id="l_st_lambda">
  <dt><b>st_lambda = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='st_lambda' Line='st_lambda = INDEF' -->
  <dd>Starting wavelength in angstroms of portion of spectrum to correlate.
  If INDEF, use beginning of wavelength overlap between template and
  spectrum.
  </dd>
  </dl>
  <dl id="l_end_lambda">
  <dt><b>end_lambda = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='end_lambda' Line='end_lambda = INDEF' -->
  <dd>Ending wavelength in angstroms of portion of spectrum to correlate.
  If INDEF, use end of wavelength overlap between template and spectrum.
  </dd>
  </dl>
  <dl id="l_obj_plot">
  <dt><b>obj_plot = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obj_plot' Line='obj_plot = yes' -->
  <dd>If yes, a plot of the object spectrum is displayed.  During this time the
  normal IRAF cursor commands are active as well as several more that are
  itemized below.A  If emission lines are chopped, before and after plots
  are displayed, as well as the chopped line(s).
  </dd>
  </dl>
  <dl id="l_xcor_plot">
  <dt><b>xcor_plot = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcor_plot' Line='xcor_plot = yes' -->
  <dd>If yes, a plot of the filtered cross-correlation function is displayed.
  Cursor commands are activated, and a peak other than the maximum
  can be chosen to be the center with the keystroke <i>p</i>.  Hard copies 
  to stdplot may also be made using the <i>@</i> command.
  </dd>
  </dl>
  <dl id="l_xcor_file">
  <dt><b>xcor_file = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcor_file' Line='xcor_file = yes' -->
  <dd>If yes, files are written containing the filtered cross-correlation function
  for each object/template pair.  The name of each file is
  <i>object</i>.<i>template</i>, and there is one line of header containing
  the object and template names and the Julian date of the observation.
  The correlation is listed in ASCII format over the range specified by the
  <i>cvel</i> and <i>dvel</i> parameters as <i>velocity correlation</i> pairs.
  </dd>
  </dl>
  <dl id="l_fixbad">
  <dt><b>fixbad = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fixbad' Line='fixbad = no' -->
  <dd>If yes, replace portions of spectrum given in file <i>badlines</i> with
  a straight line linking the adjacent points.  This feature can be used
  to eliminate emission and absorption features caused by poor removal of
  night sky emission lines. (added in version 2.0)
  </dd>
  </dl>
  <dl id="l_badlines">
  <dt><b>badlines = <span style="font-family: monospace;">"badlines.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='badlines' Line='badlines = "badlines.dat"' -->
  <dd>File containing list of starting and stopping wavelengths in Angstroms for
  removal of portions of all object spectra.  All information after the
  second wavelength is a comment field. This file is assumed to be in the
  directory <i>linedir</i> unless a complete pathname starting with <span style="font-family: monospace;">"/"</span> is
  specified.(added in version 2.0)
  </dd>
  </dl>
  <dl id="l_s_emchop">
  <dt><b>s_emchop = <span style="font-family: monospace;">"no"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='s_emchop' Line='s_emchop = "no"' -->
  <dd>Chop out emission lines from object spectrum before cross-correlating with
  template if <span style="font-family: monospace;">"yes"</span>.  If <span style="font-family: monospace;">"tempfile"</span>, emission lines are removed if the value
  of the CHOPEM keyword in the template image header is T.  If the keyword is
  not present or is F, emission lines are not removed.  If <span style="font-family: monospace;">"specfile"</span>, emission
  lines are removed if the value of the CHOPEM keyword in the object spectrum
  image header is T.  If the keyword is not present or is F, emission lines
  are not removed.  If <span style="font-family: monospace;">"no"</span>, emission lines are never removed.  If EMCHOP
  in the object spectrum file is 1, emission lines are never removed.
  </dd>
  </dl>
  <dl id="l_t_emchop">
  <dt><b>t_emchop = <span style="font-family: monospace;">"no"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_emchop' Line='t_emchop = "no"' -->
  <dd>Chop out emission lines from template spectrum before cross-correlating
  with object if <span style="font-family: monospace;">"yes"</span>.  If <span style="font-family: monospace;">"tempfile"</span>, emission lines are removed if the
  value of the CHOPEM keyword in the template image header is T.  If the
  keyword is not present or is F, emission lines are not removed.  If <span style="font-family: monospace;">"specfile"</span>,
  emission lines are removed if the value of the CHOPEM keyword in the object
  spectrum image header is T.  If the keyword is not present or is F, emission
  lines are not removed.  If <span style="font-family: monospace;">"no"</span>, emission lines are never removed.  If EMCHOP
  in the template spectrum file is 1, emission lines are never removed.
  </dd>
  </dl>
  <dl id="l_s_abs_reject">
  <dt><b>s_abs_reject 100.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='s_abs_reject' Line='s_abs_reject 100.' -->
  <dd>Spectrum absorption line rejection in sigma of fit (0=no rejection)
  </dd>
  </dl>
  <dl id="l_s_em_reject">
  <dt><b>s_em_reject 2.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='s_em_reject' Line='s_em_reject 2.' -->
  <dd>Spectrum emission line rejection in sigma of fit (0=no rejection)
  </dd>
  </dl>
  <dl id="l_t_abs_reject">
  <dt><b>t_abs_reject 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_abs_reject' Line='t_abs_reject 0.' -->
  <dd>Template absorption line rejection in sigma of fit (0=no rejection)
  </dd>
  </dl>
  <dl id="l_t_em_reject">
  <dt><b>t_em_reject 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_em_reject' Line='t_em_reject 0.' -->
  <dd>Template emission line rejection in sigma of fit (0=no rejection)
  </dd>
  </dl>
  <dl id="l_bell_window">
  <dt><b>bell_window = 0.05</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bell_window' Line='bell_window = 0.05' -->
  <dd>A fraction bell_window of the ends of the object and template spectrum are
  multiplied by a cosine bell.  This is to reduce high wave number Fourier
  components that would be produced by abrupt cutoffs at the ends of the spectra.
  </dd>
  </dl>
  <dl id="l_renormalize">
  <dt><b>renormalize = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='renormalize' Line='renormalize = no' -->
  <dd>If yes, the data spectrum is divided by its mean value before being
  transformed. The minimum value (divided by the mean first) is then
  subtracted, and the whole thing is multiplied by an arbitrary factor
  of 1000.0 to put it within normal count levels. This is used on spectra
  which may have unusual values if they have already been flux-calibrated.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = 2048</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = 2048' -->
  <dd>Number of columns into which to rebin data before transforming, must be
  a power of two between 256 and 8192.
  </dd>
  </dl>
  <dl id="l_interp_mode">
  <dt><b>interp_mode = <span style="font-family: monospace;">"spline3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interp_mode' Line='interp_mode = "spline3"' -->
  <dd>Interpolation mode to use when rebinning spectra, must be
  <span style="font-family: monospace;">"linear"</span> or <span style="font-family: monospace;">"spline3"</span> or <span style="font-family: monospace;">"poly3"</span> or <span style="font-family: monospace;">"poly5"</span> or <span style="font-family: monospace;">"sums"</span>.
  </dd>
  </dl>
  <dl id="l_zero_pad">
  <dt><b>zero_pad = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zero_pad' Line='zero_pad = no' -->
  <dd>If yes, pad Fourier transforms of both object and template spectra with
  an equal amount of zeroes to avoid wrap-around correlations.  This usually
  gives better results, but the option of turning it off has been
  kept to allow comparison of results with older versions of XCSAO.
  *If zero_pad=yes, double low_bin, top_low, top_nrun, and nrun.
  </dd>
  </dl>
  <dl id="l_low_bin">
  <dt><b>low_bin = 5, top_low = 10, top_nrun = 80, nrun = 140</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_bin' Line='low_bin = 5, top_low = 10, top_nrun = 80, nrun = 140' -->
  <dd>The Fourier amplitudes are multiplied by a cosine-bell filter function,
  starting at <i>low_bin</i> and running to <i>nrun</i>.
  Values chosen for low_bin and nrun are not critical.  Generally low_bin
  should be about 5 to 10 for a 1024 point spectrum of 2-4 pixel resolution.
  Set nrun based upon the number of points in your spectrum and the resolution.
  For a spectrum of NPTS pixels and resolution FWHM,
  nrun ~ NPTS / (2*PI * FWHM/2.355).  See Tonry and Davis 1979, A.J., 84,
  1511.
  </dd>
  </dl>
  <dl id="l_vel_init">
  <dt><b>vel_init = zero</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vel_init' Line='vel_init = zero' -->
  <dd>Make an inital velocity guess.  It is used to shift the template in
  wavelength to give a better overlap region.The options are: <span style="font-family: monospace;">"zero"</span> to
  use no initial velocity, <span style="font-family: monospace;">"guess"</span> to use <i>czguess</i>, <span style="font-family: monospace;">"correlation"</span>
  to use the correlation velocity in the spectrum header parameter CZXC,
  <span style="font-family: monospace;">"emission"</span> to use the emission line velocity in the spectrum header
  parameter CZEM, and <span style="font-family: monospace;">"combination"</span> to use the velocity in the spectrum header
  parameter VELOCITY. 
  </dd>
  </dl>
  <dl id="l_czguess">
  <dt><b>czguess = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='czguess' Line='czguess = 0' -->
  <dd>Velocity in km/sec used as an initial guess if <i>czinit</i> is yes.
  </dd>
  </dl>
  <dl id="l_nzpass">
  <dt><b>nzpass = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nzpass' Line='nzpass = 0' -->
  <dd>Number of iterations shifting the template to match features with the
  spectrum.  Zero and one both give one pass through.
  </dd>
  </dl>
  <dl id="l_tshift">
  <dt><b>tshift = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tshift' Line='tshift = 0.' -->
  <dd>Night to night velocity zero point shift.  If this is zero, each template
  spectrum header is checked for a TSHIFT parameter, and that is used if
  present.
  </dd>
  </dl>
  <dl id="l_svel_corr">
  <dt><b>svel_corr = <span style="font-family: monospace;">"file"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='svel_corr' Line='svel_corr = "file"' -->
  <dd>Spectrum velocity correction to the solar system barycenter.  Set to
  <span style="font-family: monospace;">"none"</span> if spectrum has already been shifted or if this correction is
  unnecessary.  If <span style="font-family: monospace;">"file"</span>, <i>BCV</i> is used if present in the file header,
  or else <i>HCV</i>.  If <span style="font-family: monospace;">"hfile"</span>, the header parameter <i>HCV</i> is always
  used.  If neither is found, no correction is made.  If <span style="font-family: monospace;">"heliocentric"</span>
  or <span style="font-family: monospace;">"barycentric"</span> corrections are chosen, position and time parameters
  are read from the spectrum data file header.  <i>DATE-OBS</i> (date in
  format 'dd-mm-yy') <i>UT</i> (U.T. at end of exposure as 'hh:mm:ss')
  and <i>UTOPEN</i> (U.T. at start of exposure as 'hh:mm:ss') or
  /fIEXPTIME/fR/<i>EXPOSURE</i> (length of exposure in seconds) are used to compute
  the midtime of the exposure.  <i>RA</i> (right ascension as 'hh:mm:ss.ss'),
  <i>DEC</i> (declination as 'dd:mm:ss.ss'), and <i>EPOCH</i> (epoch of
  coordinates defaults to 1950.0) give the position of the object whose
  spectrum this is.  <i>SITELONG</i> (observatory longitude as 'dd:mm:ss.ss'
  or degrees), <i>SITELAT</i> (observatory latitude as 'dd:mm:ss.ss' or
  degrees), and <i>SITEELEV</i> (observatory altitude in meters) give the
  observatory position.
  </dd>
  </dl>
  <dl id="l_tvel_corr">
  <dt><b>tvel_corr = <span style="font-family: monospace;">"file"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tvel_corr' Line='tvel_corr = "file"' -->
  <dd>Template velocity correction.  Set to <span style="font-family: monospace;">"none"</span> if template is already
  corrected to <span style="font-family: monospace;">"heliocentric"</span>, else <span style="font-family: monospace;">"heliocentric"</span>, <span style="font-family: monospace;">"barycentric"</span>, or
  <span style="font-family: monospace;">"file"</span>.  If <span style="font-family: monospace;">"file"</span>, BCV is used if present in header, else HCV.
  VELOCITY in the template file header is assumed to be the barycentric
  corrected velocity.  If the spectrum is unshifted, this correction must
  be made; if the spectrum has been shifted, this should be <span style="font-family: monospace;">"none"</span> and the
  BCV parameter in the template header should be 0.  If <span style="font-family: monospace;">"barycentric"</span> or
  <span style="font-family: monospace;">"heliocentric"</span>, the same parameters as above must be present in the template
  file header.
  </dd>
  </dl>
  <dl id="l_pkmode">
  <dt><b>pkmode = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pkmode' Line='pkmode = 1' -->
  <dd>Flag for peak fitting: 0=parabola, 1=quartic, 3=cos/(1+x^2), 0=all three
  </dd>
  </dl>
  <dl id="l_pkfrac">
  <dt><b>pkfrac = 0.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pkfrac' Line='pkfrac = 0.5' -->
  <dd>Fraction of peak or number of points for peak fitting.
  If <i>pkfrac</i> is negated, the points used in the fit will be marked.
  (option added in 1.8)
  </dd>
  </dl>
  <dl id="l_pksrch">
  <dt><b>pksrch = 25</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pksrch' Line='pksrch = 25' -->
  <dd>When a correlation peak is manually selected, the position used as the peak
  is the maximum correlation value within this many bins of the cursor-selected
  bin.
  </dd>
  </dl>
  <dl id="l_minvel">
  <dt><b>minvel = -1000.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minvel' Line='minvel = -1000.' -->
  <dd>Minimum allowable correlation peak velocity shift in km/sec.
  </dd>
  </dl>
  <dl id="l_maxvel">
  <dt><b>maxvel = 100000.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxvel' Line='maxvel = 100000.' -->
  <dd>Maximum allowable correlation peak velocity shift in km/sec.
  </dd>
  </dl>
  <dl id="l_report_mode">
  <dt><b>report_mode = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='report_mode' Line='report_mode = 1' -->
  <dd>Mode in which results of fit are reported.
  <dl>
  <dt><b>=1  commented text</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=1  commented text' -->
  <dd></dd>
  </dl>
  <dl>
  <dt><b>=2  one line per spectrum-template combination.</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=2  one line per spectrum-template combination.' -->
  <dd>Includes filenames, R, velocity and error in km/sec, and height and
  width of correlation peak.
  </dd>
  </dl>
  <dl>
  <dt><b>=3 one line per spectrum giving best fit and previous results</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=3 one line per spectrum giving best fit and previous results' -->
  <dd>Previous results are read from the image header and written alternately
  with new results: file, old R, new R, old velocity, new velocity, old
  error, new error, Julian date of observation, and name of best
  template.
  </dd>
  </dl>
  <dl>
  <dt><b>=4  one line per spectrum-template combination.</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=4  one line per spectrum-template combination.' -->
  <dd>Includes filenames, R value, velocity, and error.
  </dd>
  </dl>
  <dl>
  <dt><b>=5  one long line per spectrum-template combination.</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=5  one long line per spectrum-template combination.' -->
  <dd>Includes 4 filter parameters, template file name, tshift from template
  header, spectrum filename, velocity, R value, peak height and width, and
  heliocentric velocity correction.
  </dd>
  </dl>
  <dl>
  <dt><b>=6 One long line per spectrum-template combination, including</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=6 One long line per spectrum-template combination, including' -->
  <dd>spectrum and template names, Julian date, velocity,
  error, R-value, correlation peak height and width, and velocity
  correction to solar system barycenter 
  </dd>
  </dl>
  <dl>
  <dt><b>=7 one long line per spectrum-template combination, including</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=7 one long line per spectrum-template combination, including' -->
  <dd>per template results from current correlation and from previous
  correlation as saved in the spectrum header. Includes filename,
  old and new R-vaule, old and new velocity, old and new error, old
  and new peak height, old and new ARMS, Julian date of observation,
  and old and new template names. 
  </dd>
  </dl>
  <dl>
  <dt><b>=8 one long line per spectrum combination, including spectrum</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=8 one long line per spectrum combination, including spectrum' -->
  <dd>filename, instrument code, object name, Julian date of observation,
  emission line velocity and error, correlation velocity, error, and
  R-value, number of emission lines found and fit, and the name of the
  template giving the highest R-value. 
  </dd>
  </dl>
  <dl>
  <dt><b>=9 one long line per spectrum-template combination, including</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=9 one long line per spectrum-template combination, including' -->
  <dd>observatory code, spectrum filename, template filename, Julian date
  of observation, velocity, error, and R-value, correlation peak height
  and width, barycentric velocity correction.  The sigma of
  the spectrum transform, sigma of the template transform, and name of
  the file containing the correlation vector for this spectrum-template
  combination are added to the end of the line if such a file is written.
  </dd>
  </dl>
  <dl>
  <dt><b>=10 one long line per spectrum, including spectrum filename, Julian</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=10 one long line per spectrum, including spectrum filename, Julian' -->
  <dd>date of observation, number of best template in list, name of best
  template, velocity, error, and R-value for best, and each template. 
  <dl>
  <dt><b>=11 one long line per spectrum, including spectrum filename, Julian</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='' Line='=11 one long line per spectrum, including spectrum filename, Julian' -->
  <dd>date of observation, number of best template in list, filename, velocity,
  error, and R-value for best template, filename, velocity, error, and
  R-value for each template. 
  </dd>
  </dl>
  <dl>
  <dt><b>=12  one long line per spectrum, including spectrum filename,</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='' Line='=12  one long line per spectrum, including spectrum filename,' -->
  <dd>Julian date of observation, number of best template in list, and
  filename, velocity, error, and R-value for each template.
  </dd>
  </dl>
  <dl>
  <dt><b>=13  one long line per spectrum-template combination, including</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='' Line='=13  one long line per spectrum-template combination, including' -->
  <dd>observatory code, spectrum filename, template filename, Julian date of
  observation, velocity (from the searched, not fit, peak), peak height
  and width, barycentric velocity correction.  The sigma of the spectrum
  transform, sigma of the template transform, and name of the file
  containing the correlation vector for this spectrum-template combination
  are added to the end of the line if such a file is written.
  </dd>
  </dl>
  <dl>
  <dt><b>=14  one long line per spectrum, including spectrum filename, Julian</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='' Line='=14  one long line per spectrum, including spectrum filename, Julian' -->
  <dd>date of observation, emission line velocity, error, number of lines found,
  and number of lines fit, number and name of best template in list, and
  filename, velocity, error, and R-value for each template. (mode added in
  version 2.0) 
  </dd>
  </dl>
  <dl>
  <dt><b>=15 one long line per spectrum-template combination, including spectrum</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='' Line='=15 one long line per spectrum-template combination, including spectrum' -->
  <dd>and template names, Julian date, velocity, error, R-value, correlation peak
  height and width, and velocity correction to solar system barycenter. It is
  like mode 6, but with 2 more template name characters and velocities to
  m/sec. (mode added in version 2.0.1) 
  </dd>
  </dl>
  <dl>
  <dt><b>=16 one line per spectrum-template combination, including spectrum and</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='' Line='=16 one line per spectrum-template combination, including spectrum and' -->
  <dd>template names (24 and 16 characters, respectively), R-value, radial velocity
  and error in km/sec, height of correlation peak, template wavelength limits,
  and center wavelength of  correlated template spectrum.  This is used with
  wide synthetic templates of which only portions are used.
  </dd>
  </dl>
  <dl>
  <dt><b>=17 one line per spectrum-template combination for Hectochelle, including</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='' Line='=17 one line per spectrum-template combination for Hectochelle, including' -->
  <dd>aperture, fiber, beam, 24-character spectrum name, last 24 characters of
  template name, heliocentric Julian Day, radial velocity, velocity error,
  R-value, correlation peak height and width, and barycentric velocity correction.
  </dd>
  </dl>
  <dl>
  <dt><b>logfiles = <span style="font-family: monospace;">"STDOUT,xcsao.log"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='logfiles' Line='logfiles = "STDOUT,xcsao.log"' -->
  <dd>All results from XCOR are recorded in these files.
  </dd>
  </dl>
  <dl>
  <dt><b>save_vel = no</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='save_vel' Line='save_vel = no' -->
  <dd>If yes, save emission line velocity and error in IRAF image header as CZXC and
  CZXCERR, and R-value as CZXCR (or APVELn and APVXCn if a multispec file).
  </dd>
  </dl>
  <dl>
  <dt><b>rvcheck = no</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='rvcheck' Line='rvcheck = no' -->
  <dd>Enable header update if not correlate=no (yes or no)
  </dd>
  </dl>
  <dl>
  <dt><b>archive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='archive' Line='archive = no' -->
  <dd>If yes, save emission line results in SAO TDC archive records in the current
  directory.
  </dd>
  </dl>
  <dl>
  <dt><b>nsmooth = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='nsmooth' Line='nsmooth = 0' -->
  <dd>If &gt;0, the data spectrum is smoothed <i>smooth</i> times for the final
  one-page display.  The spectrum is NEVER smoothed for the correlation.
  </dd>
  </dl>
  <dl>
  <dt><b>cvel = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='cvel' Line='cvel = INDEF' -->
  <dd>Center velocity of the summary velocity correlation graph in km/sec.
  This defaults to the velocity from the cross-correlation with the
  highest R value.
  </dd>
  </dl>
  <dl>
  <dt><b>dvel = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='dvel' Line='dvel = INDEF' -->
  <dd>Velocity half-width of the summary velocity correlation graph in km/sec.
  This defaults to 20 times the width of the peak of the cross-correlation
  with the highest R value.
  </dd>
  </dl>
  <dl>
  <dt><b>ablines = <span style="font-family: monospace;">"ablines.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='ablines' Line='ablines = "ablines.dat"' -->
  <dd>Name of file containing an absorption line list.  It is used if the <span style="font-family: monospace;">"l"</span>
  cursor option is selected to label absorption lines.  Each line has
  <br>
          Center wavelength of line in angstroms
  <br>
          Name of line (terminated by end of line or space)
  </dd>
  </dl>
  <dl>
  <dt><b>emlines = <span style="font-family: monospace;">"emlines.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='emlines' Line='emlines = "emlines.dat"' -->
  <dd>Name of file containing an absorption line list.  It is used if the <span style="font-family: monospace;">"l"</span>
  cursor option is selected and the <span style="font-family: monospace;">"e"</span> cursor command is used to identify
  an emission line in the spectrum.  If the filename is preceded by a <span style="font-family: monospace;">"+"</span>,
  emission lines are always labelled.  Each line contains:
  <br>
          Center wavelength of line in angstroms
  <br>
          Starting wavelength in angstroms for continuum for this line
  <br>
          Ending wavelength in angstroms for continuum for this line
  <br>
          Half-width in angstroms for region to fit for this line
  <br>
          Name of line (terminated by end of line or space)
  </dd>
  </dl>
  <dl>
  <dt><b>linedir = rvsao$lib/</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='linedir' Line='linedir = rvsao$lib/' -->
  <dd>Directory for emission and absorption information files.  If the name of
  one of the individual files containis <span style="font-family: monospace;">"/"</span> or <span style="font-family: monospace;">"$"</span>, it is assumed to be a
  full path name, and <i>linedir</i> is not used.
  </dd>
  </dl>
  <dl>
  <dt><b>dispmode = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='dispmode' Line='dispmode = 1' -->
  <dd>Display modes 
  <dl>
  <dt><b>=1 Display spectrum and cross-correlation with template information.</b></dt>
  <!-- Sec='PARAMETERS' Level=3 Label='' Line='=1 Display spectrum and cross-correlation with template information.' -->
  <dd></dd>
  </dl>
  <dl>
  <dt><b>=-1 Display spectrum, plotted from 0, and cross-correlation with</b></dt>
  <!-- Sec='PARAMETERS' Level=3 Label='' Line='=-1 Display spectrum, plotted from 0, and cross-correlation with' -->
  <dd>template information.
  </dd>
  </dl>
  <dl>
  <dt><b>=2 Display spectrum with absorption and known emission lines labelled</b></dt>
  <!-- Sec='PARAMETERS' Level=3 Label='' Line='=2 Display spectrum with absorption and known emission lines labelled' -->
  <dd>and tables of template and emission line information.
  </dd>
  </dl>
  <dl>
  <dt><b>=3 Display spectrum with absorption and known emission lines labelled</b></dt>
  <!-- Sec='PARAMETERS' Level=3 Label='' Line='=3 Display spectrum with absorption and known emission lines labelled' -->
  <dd>using the entire display without the table of results
  </dd>
  </dl>
  <dl>
  <dt><b>=4 Display continuum-subtracted spectrum with absorption and known</b></dt>
  <!-- Sec='PARAMETERS' Level=3 Label='' Line='=4 Display continuum-subtracted spectrum with absorption and known' -->
  <dd>emission lines labelled and tables of template and emission line information.
  </dd>
  </dl>
  <dl>
  <dt><b>=5 Display continuum-subtracted spectrum with absorption and known</b></dt>
  <!-- Sec='PARAMETERS' Level=3 Label='' Line='=5 Display continuum-subtracted spectrum with absorption and known' -->
  <dd>emission lines labelled using the entire display without the table of results.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl>
  <dt><b>displot = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='displot' Line='displot = yes' -->
  <dd>Display graphic summary of results on an interactive display <i>device</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='device' Line='device = "stdgraph"' -->
  <dd>Interactive device on which to display a graphic summary of XCSAO's results.
  </dd>
  </dl>
  <dl>
  <dt><b>curmode = no</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='curmode' Line='curmode = no' -->
  <dd>If yes, wait in cursor mode after each spectrum is processed.  Cursor
  mode commands may be listed by typing <span style="font-family: monospace;">"?"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>hardcopy = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='hardcopy' Line='hardcopy = yes' -->
  <dd>Display graphic summary of results on <i>plotter</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>plotter = <span style="font-family: monospace;">"stdplot"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='plotter' Line='plotter = "stdplot"' -->
  <dd>Second, non-interactive device on which to plot the graphic summary of results.
  </dd>
  </dl>
  <dl>
  <dt><b>besttemp = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='besttemp' Line='besttemp = ""' -->
  <dd>Best template (returned from last cross-correlated spectrum)
  </dd>
  </dl>
  <dl>
  <dt><b>velocity = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='velocity' Line='velocity = 0.' -->
  <dd>Velocity for best template (returned from last cross-correlated spectrum)
  </dd>
  </dl>
  <dl>
  <dt><b>velerr = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='velerr' Line='velerr = 0.' -->
  <dd>Velocity error for best template (returned from last cross-correlated spectrum)
  </dd>
  </dl>
  <dl>
  <dt><b>r = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='r' Line='r = 0.' -->
  <dd>R-value for best template (returned from last cross-correlated spectrum)
  </dd>
  </dl>
  <dl>
  <dt><b>temp_plot = no</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='temp_plot' Line='temp_plot = no' -->
  <dd>Plot the template spectra
  </dd>
  </dl>
  <dl>
  <dt><b>contsub_plot = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='contsub_plot' Line='contsub_plot = yes' -->
  <dd>If yes, plots of the continuum-subtracted object and template spectra are
  displayed.  This is most useful for determining the appropriateness of
  the order of the polynomial chosen to fit the continuum.
  </dd>
  </dl>
  <dl>
  <dt><b>apodize_plot = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='apodize_plot' Line='apodize_plot = yes' -->
  <dd>If yes, plots of the windowed object and template spectra are displayed.
  This is most useful for determining the size of the cosine bell window
  applied to either end of the spectrum.
  </dd>
  </dl>
  <dl>
  <dt><b>fft_plot = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='fft_plot' Line='fft_plot = yes' -->
  <dd>If yes, the power spectrum of the transformed object data is displayed.
  This is useful for setting the low order cutoff for the fits and for seeing
  if any periodic noise is present in the data.
  <dl>
  <dt><b>uxcor_plot = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=3 Label='uxcor_plot' Line='uxcor_plot = yes' -->
  <dd>If yes, the unfiltered cross-correlation data is plotted.
  </dd>
  </dl>
  <dl>
  <dt><b>phase_plot = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=3 Label='phase_plot' Line='phase_plot = yes' -->
  <dd>If yes, the phase of the cross-correlation function is plotted.
  </dd>
  </dl>
  <dl>
  <dt><b>debug = no</b></dt>
  <!-- Sec='PARAMETERS' Level=3 Label='debug' Line='debug = no' -->
  <dd>If yes, values of the parameters fit to the selected peak
  are recorded in the log files.  This is most useful for debugging.
  </dd>
  </dl>
  <dl>
  <dt><b>nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=3 Label='nsum' Line='nsum = 1' -->
  <dd>Number of pixels to sum across dispersion.
  </dd>
  </dl>
  <dl>
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=3 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input.  When null the standard cursor is used otherwise
  the specified file is used.
  </dd>
  </dl>
   
  </section>
  <section id="s_description">
  <h3>Description</h3>
  XCSAO provides an interactive facility to determine redshifts and
  velocity dispersions using the Cross-correlation Technique (e.g.,
  Tonry and Davis 1979, A.J., 84, 1511).
   
  In brief, the cross-correlation technique assumes that a galaxy spectrum is
  simply the convolution of a stellar spectrum with a Gaussian which describes
  the line of sight velocity dispersion of the galaxy's constituent stars.
  Cross-correlating a template spectrum with the galaxy spectrum then produces
  a function with a peak at the redshift of the galaxy with a width related to
  the dispersion of the galaxy.  Peaks in the cross-correlation function are
  identified and fit by parabolas to obtain their position and width and hence
  the redshift and velocity dispersion of the galaxy.
  The templates are read separately for each object.  The wavelength scale
  may be linear or logarithmic; if it is linear, the data will be rebinned
  to a logarythmic scale.  It is specified in the header by the starting
  log or linear wavelength (W0, CRVAL1, or APNUMn) and the delta log or
  linear wavelength per pixel (WPC, CDELT1 or APNUMn).
  The dispersion must run along axis 1 of the image.  The templates should
  have the keyword VELOCITY or APVELn in their headers.  This specifies the
  CORRECTED velocity (km/sec, + =&gt; receding) for the observation.  The
  <i>tvel_corr</i> parameter tells whether and how this heliocentric velocity
  was corrected from an observed velocity.  If VELOCITY is not found, it
  is assumed to be zero.  If the templates have a TSHIFT parameter and
  <i>tshift</i> is zero, that velocity is added to the template velocity.
  The objects are read one at a time.  Each object-template combination
  is rebinned in log-lambda to the designated (power of two) number of points
  over the overlapping wavelength region.  Continua are fit to these rebinned
  log-wavelength spectra using the IRAF interactive curve fitting software, with
  optional emission line removal.  Parameters for these continuum fits are
  set using the <i>contpars</i> pset.  Acceptance limits in sigma can be
  set for both absorption and emission features for the continuum fit and
  point removal for both object and template spectra.  The spectra are then
  optionally renormalized to the average value of the spectrum.  The ends of
  the spectra are windowed by a cosine bell to suppress high frequency noise.
  The object and template are filtered in Fourier space and multiplied together
  to form the transform of the cross-correlation function.  This is transformed
  back into real space.  The largest peak is found and fit by a parabola, quartic,
  or function of the form cos(x)/(1+x^2).  The fitted parameters are saved, and a
  summary output is produced for each object.  In this summary, the redshift is
  corrected for the velocity of the template star.  The redshift is given as
  cz in km/sec.  The quoted errors are one sigma on each parameter.
  </section>
  <section id="s_cursor">
  <h3>Cursor</h3>
  The following keystrokes are active for intermediate spectrum and
  cross-correlation plots in addition to the normal IRAF cursor
  facilities (a list of those is available with the command <span style="font-family: monospace;">":.help"</span>):
  <dl>
  <dt><b>@</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='' Line='@' -->
  <dd>Make a hard copy on the device designated by <i>plotter</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>d</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='d' Line='d' -->
  <dd>Replaces a region between the marked vertical cursors with interpolated
  values from the edges of the marked region.  This is typically used to
  eliminate poorly subtracted night sky lines or emission lines.
  </dd>
  </dl>
  <dl>
  <dt><b>n</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='n' Line='n' -->
  <dd>Smooth spectrum n times before plotting.  This only affects the current
  spectrum display and the final spectrum graph, not the spectrum data.
  </dd>
  </dl>
  <dl>
  <dt><b>p</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='p' Line='p' -->
  <dd>Forces the current vertical cursor location to be chosen as the peak in the
  cross-correlation function which is used to obtain the redshift and dispersion.
  The maximum within 25 pixels of the cursor is actually used.
  </dd>
  </dl>
  <dl>
  <dt><b>q</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='q' Line='q' -->
  <dd>Quit and exit.
  </dd>
  </dl>
  <dl>
  <dt><b>r</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='r' Line='r' -->
  <dd>Forces a replot of the current spectrum at the original scale.
  </dd>
  </dl>
  <dl>
  <dt><b>u</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='u' Line='u' -->
  <dd>Redisplay the entire plot after zooming.
  </dd>
  </dl>
  <dl>
  <dt><b>z</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='z' Line='z' -->
  <dd>Zoom in on the region marked by two successive &lt;z&gt;'s
  </dd>
  </dl>
  The following keystrokes are active for the final plot in addition to
  the normal IRAF cursor facilities (list available with the command <span style="font-family: monospace;">":.help"</span>):
  <dl>
  <dt><b>c</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='c' Line='c' -->
  <dd>Reset correlation peak fitting function and fraction to fit. (1.7)
  </dd>
  </dl>
  <dl>
  <dt><b>f</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='f' Line='f' -->
  <dd>Change transform filter parameters. (1.7)
  </dd>
  </dl>
  <dl>
  <dt><b>g</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='g' Line='g' -->
  <dd>Smooth spectrum n times before plotting.  This only affects the current
  spectrum display and the final spectrum graph, not the spectrum data.  (1.8)
  </dd>
  </dl>
  <dl>
  <dt><b>j</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='j' Line='j' -->
  <dd>Set quality flag to conditional (1.8)
  </dd>
  </dl>
  <dl>
  <dt><b>l</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='l' Line='l' -->
  <dd>Plot spectrum with absorption lines labelled.  Label emission lines
  if the R-value for an emission line template (emission lines not
  chopped) is &gt; 5 or if they have already been fit by EMSAO.
  (<i>dispmode</i>=2)
  </dd>
  </dl>
  <dl>
  <dt><b>n</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='n' Line='n' -->
  <dd>Set quality flag to unacceptable. (1.8)
  </dd>
  </dl>
  <dl>
  <dt><b>p</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='p' Line='p' -->
  <dd>Rerun cross-correlation, stopping in the filtered cross-correlation
  plot to select a peak other than the highest one.
  <dl>
  <dt><b>u</b></dt>
  <!-- Sec='CURSOR' Level=4 Label='u' Line='u' -->
  <dd>Unzoom the spectrum graph if using display mode 2 (1.8)
  </dd>
  </dl>
  </dd>
  </dl>
  <dl>
  <dt><b>v</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='v' Line='v' -->
  <dd>Change the velocity limits within which a correlation peak is allowed. (1.7)
  </dd>
  </dl>
  <dl>
  <dt><b>x</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='x' Line='x' -->
  <dd>Plot the spectrum, without line labels, and the cross-correlation on
  the same page.  (<i>dispmode</i>=1)
  </dd>
  </dl>
  <dl>
  <dt><b>y</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='y' Line='y' -->
  <dd>Set quality flag in header to yes. (1.8)
  </dd>
  </dl>
  <dl>
  <dt><b>z</b></dt>
  <!-- Sec='CURSOR' Level=3 Label='z' Line='z' -->
  <dd>Zoom in on the spectrum graph between two cursor clicks if using
  display mode 2.  (1.8)
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  To obtain the redshift and dispersion of a single galaxy
          cl&gt; xcsao galaxy templates=template
  To obtain redshifts for a whole night's worth of galaxy spectra using 5
  different templates:
          cl&gt; xcsao @nite1.ls templates=@temp.ls
  where the file temp.ls contains the names of the 5 template images and the
  file nite1.ls contains the name of the galaxy images.
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  On-line help is available on the World Wide Web at
  http://tdc-www.harvard.edu/iraf/rvsao/xcsao
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR' 'EXAMPLES' 'SEE ALSO'  -->
  

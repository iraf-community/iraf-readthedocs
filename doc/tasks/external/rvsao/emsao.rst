.. _emsao:

emsao: Find redshifts by measuring emission line shifts
=======================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  emsao spectra
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
  file should be processed, where &lt;range&gt; is a comma- and/or hyphen-separated
  list of numbers.
  The files should be dispersion-corrected and linear in wavelength.
  </dd>
  </dl>
  <dl id="l_specnum">
  <dt><b>specnum = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specnum' Line='specnum = 0' -->
  <dd>If this is nonzero and <i>spectra</i> contains a single file name, this
  is a range of spectrum numbers in a multispec file for which emission
  line velocities will be obtained.  Wavelength dispersion information
  is then read from APNUMn, and velocity information is read from APVELn,
  APVXCn, and APVEMn and saved in APVELn and APVEMn, the values of which
  contain multiple values.  If specnum is zero, velocity information is
  in separate keywords for each value.
  </dd>
  </dl>
  <dl id="l_specband">
  <dt><b>specband = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specband' Line='specband = ""' -->
  <dd>Spectrum band if multispec file
  </dd>
  </dl>
  <dl id="l_skynum">
  <dt><b>skynum = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skynum' Line='skynum = 0' -->
  <dd>If this is nonzero, the sky spectrum, which is used for equivalent width
  errors, is read from this spectrum number of the current spectrum file
  </dd>
  </dl>
  <dl id="l_skyband">
  <dt><b>skyband = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skyband' Line='skyband = 0' -->
  <dd>Sky band if multispec file
  </dd>
  </dl>
  <dl id="l_specdir">
  <dt><b>specdir = <span style="font-family: monospace;">"./"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specdir' Line='specdir = "./"' -->
  <dd>Directory containing spectra to analyze
  </dd>
  </dl>
  <dl id="l_linefit">
  <dt><b>linefit = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linefit' Line='linefit = yes' -->
  <dd>If yes, search for emission lines fit their positions, and average
  them into a weighted mean velocity for the spectrum.  If no, display
  spectrum with labelled emission lines found in a previous application
  of EMSAO and results from any previous XCSAO run which is archived in
  the image header.
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
  directory <i>linedir</i> unless a complete pathname starting with <span style="font-family: monospace;">"/"</span> or
  including a <span style="font-family: monospace;">"$"</span> is specified (added in version 2.0).
  </dd>
  </dl>
  <dl id="l_renormalize">
  <dt><b>renormalize = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='renormalize' Line='renormalize = no' -->
  <dd>If yes, renormalize spectrum before fitting by multiplying each pixel
  by 1000 times the mean pixel value for the spectrum.  .  Set this to <span style="font-family: monospace;">"yes"</span>
  for fluxed spectra.  If set to <span style="font-family: monospace;">"no"</span> and all values of the object spectrum are
  less than 1, the spectrum is renormalized anyway, to avoid crashing the
  program.
  </dd>
  </dl>
  <dl id="l_st_lambda">
  <dt><b>st_lambda INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='st_lambda' Line='st_lambda INDEF' -->
  <dd>Starting wavelength in angstroms of portion of spectrum to use
  If INDEF, start at beginning of spectrum.
  </dd>
  </dl>
  <dl id="l_end_lambda">
  <dt><b>end_lambda INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='end_lambda' Line='end_lambda INDEF' -->
  <dd>Ending wavelength in angstroms of portion of spectrum to use
  If INDEF, end at end of spectrum.
  </dd>
  </dl>
  <dl id="l_nsmooth">
  <dt><b>nsmooth 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsmooth' Line='nsmooth 10' -->
  <dd>Number of times the spectrum is smoothed using a 1-2-1
  sliding box before the emission line search occurs.  This smoothed
  spectrum is also the version which is displayed.
  </dd>
  </dl>
  <dl id="l_vel_init">
  <dt><b>vel_init <span style="font-family: monospace;">"search"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vel_init' Line='vel_init "search"' -->
  <dd>The type of velocity to be used for the initial guess at where the emission
  lines should be.
  If <span style="font-family: monospace;">"search"</span>, look for the lines in the <i>emsearch</i> file.
  If <span style="font-family: monospace;">"guess"</span>, use <i>czguess</i>.
  If <span style="font-family: monospace;">"correlation"</span>, use the <i>CZXC</i> parameter in the file header which
  was set by XCSAO.
  If (<span style="font-family: monospace;">"cortemp"</span>, use the velocity obtained by XCSAO when cross-correlating this
  spectrum against the template specified by <i>cortemp</i>.
  If <span style="font-family: monospace;">"emission"</span>, use the <i>CZEM</i> file header parameter which was set by
  a previous run of EMSAO.
  If <span style="font-family: monospace;">"file"</span>, use the <i>VELOCITY</i> parameter from the header, a combined
  velocity which is set by both EMSAO and XCSAO.
  </dd>
  </dl>
  <dl id="l_czguess">
  <dt><b>czguess 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='czguess' Line='czguess 0.' -->
  <dd>Initial guess at the radial velocity if &gt;1 or z if &lt;1.  It is used only if
  vel_init is <span style="font-family: monospace;">"guess"</span>.
  </dd>
  </dl>
  <dl id="l_cortemp">
  <dt><b>cortemp <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cortemp' Line='cortemp ""' -->
  <dd>Name of template from which to use cross-correlation velocity. (new in 2.0)
  </dd>
  </dl>
  <dl id="l_wspan">
  <dt><b>wspan 10.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wspan' Line='wspan 10.' -->
  <dd>Wavelength in angstroms to search around redshifted line center.  This
  should always be less than the distance between the closest lines for
  which you are searching.
  </dd>
  </dl>
  <dl id="l_linesig">
  <dt><b>linesig 2.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linesig' Line='linesig 2.0' -->
  <dd>A line peak must be this many standard deviations above the continuum to
  qualify as a line.
  </dd>
  </dl>
  <dl id="l_emsearch">
  <dt><b>emsearch <span style="font-family: monospace;">"emsearch.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='emsearch' Line='emsearch "emsearch.dat"' -->
  <dd>File containing list of emission lines used to determine an initial
  velocity guess if <i>vel_init</i> is <span style="font-family: monospace;">"search"</span>.  Each line contains:
  <br>
  	Center wavelength of line in angstroms
  <br>
  	Starting wavelength in angstroms for search for this line
  <br>
  	Ending wavelength in angstroms for search for this line
  <br>
  	Name of line (terminated by end of line or space)
  </dd>
  </dl>
  <dl id="l_emlines">
  <dt><b>emlines <span style="font-family: monospace;">"rvsao$lib/emlines.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='emlines' Line='emlines "rvsao$lib/emlines.dat"' -->
  <dd>File containing list of emission lines, where the each line contains:
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
  <dl id="l_linedir">
  <dt><b>linedir = rvsao$lib/</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linedir' Line='linedir = rvsao$lib/' -->
  <dd>Directory for emission and absorption information files.  If the name of
  one of the individual files containis <span style="font-family: monospace;">"/"</span> or <span style="font-family: monospace;">"$"</span>, it is assumed to be a
  full path name, and <i>linedir</i> is not used.
  </dd>
  </dl>
  <dl id="l_npfit">
  <dt><b>npfit 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='npfit' Line='npfit 2' -->
  <dd>Number of pixels to fit around line peak (+-)
  </dd>
  </dl>
  <dl id="l_nlcont">
  <dt><b>nlcont 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlcont' Line='nlcont 1' -->
  <dd>Number of coefficients in line continuum fit (0-3).  An overall continuum
  fit is subtracted, but the fit may not be good enough to remove the local
  continuum.  If 0, no additional continuum is fit for each line.  If the
  continuum is poorly subtracted using the parameters in <i>contpars</i>,
  values of more than 0 for <i>nlcont</i> can cause trouble.
  </dd>
  </dl>
  <dl id="l_esmooth">
  <dt><b>esmooth 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='esmooth' Line='esmooth 0' -->
  <dd>Number of times the spectrum is smoothed using a 1-2-1 sliding box
  before the emission lines are fit.  Normally 0, it can be set to 1 or 2
  for very noisy data when the fitting subroutine may otherwise be
  unable to fit a continuum.  It should be set no higher to avoid distorting
  the emission line profiles.
  </dd>
  </dl>
  <dl id="l_emcombine">
  <dt><b>emcombine <span style="font-family: monospace;">"emcomb.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='emcombine' Line='emcombine "emcomb.dat"' -->
  <dd>File containing list of groups of emission lines which should be fit together.
  Each entry contains the following information for one group of two to five lines:
  <br>
  	Number of combined emission lines
  <br>
  	Number of angstroms to add to fit beyond left and right line centers
  <br>
  	For each emission line:
  <br>
  		Center wavelength in angstroms
  <br>
  		Relative line height
  </dd>
  </dl>
  <dl id="l_mincont">
  <dt><b>mincont 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mincont' Line='mincont 0.0' -->
  <dd>If continuum is greater than this value, compute the equivalent width
  of the current line, which is the width the line would be if it were as high
  as the continuum is deep.  If the continuum is less than or equal to this
  value, compute the area of the line in counts times wavelength.  When
  working with continuum subtracted spectra or spectra where the emission lines
  are so strong that there is minimal continuum, make this value larger than
  the largest possible continuum fit value to get consistently computed numbers.
  (added in 2.0)
  </dd>
  </dl>
  <dl id="l_lwmin">
  <dt><b>lwmin 0.4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lwmin' Line='lwmin 0.4' -->
  <dd>Minimum fraction of mean line width for individual line (added in 2.0)
  </dd>
  </dl>
  <dl id="l_lwmax">
  <dt><b>lwmax 1.7</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lwmax' Line='lwmax 1.7' -->
  <dd>Maximum fraction of mean line width for individual line (added in 2.0)
  </dd>
  </dl>
  <dl id="l_lsmin">
  <dt><b>lsmin 2.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lsmin' Line='lsmin 2.0' -->
  <dd>Minimum equivalent width in sigma for individual line (added in 2.0)
  </dd>
  </dl>
  <dl id="l_sigline">
  <dt><b>sigline 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigline' Line='sigline 0.0' -->
  <dd>Velocity error if single line found.  Use gaussian fit error if 0 or
  INDEF.  This value may need to be set higher to use a good, but different
  cross-correlation properly when the program computes a combined velocity.
  </dd>
  </dl>
  <dl id="l_disperr">
  <dt><b>disperr = 0.01</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='disperr' Line='disperr = 0.01' -->
  <dd>RMS dispersion error in Angstroms
  </dd>
  </dl>
  <dl id="l_vel_corr">
  <dt><b>vel_corr <span style="font-family: monospace;">"file"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vel_corr' Line='vel_corr "file"' -->
  <dd>Spectrum velocity correction to the solar system barycenter.  Set to
  <span style="font-family: monospace;">"none"</span> if spectrum has already been shifted or if this correction is
  unnecessary.  If <span style="font-family: monospace;">"file"</span>, <i>BCV</i> is used if present in the file header,
  or else <i>HCV</i>.  If <span style="font-family: monospace;">"hfile"</span>, the header parameter <i>HCR</i> is always
  used.  If neither is found, no correction is made.  If <span style="font-family: monospace;">"heliocentric"</span>
  or <span style="font-family: monospace;">"barycentric"</span> corrections are chosen, position and time parameters
  are read from the spectrum data file header.  <i>DATE-OBS</i> (date in
  format 'dd-mm-yy') <i>UT</i> (U.T. at end of exposure as 'hh:mm:ss')
  and <i>UTOPEN</i> (U.T. at start of exposure as 'hh:mm:ss') or
  <i>EXPOSURE</i> (length of exposure in seconds) are used to compute
  the midtime of the exposure.  <i>RA</i> (right ascension as 'hh:mm:ss.ss'),
  <i>DEC</i> (declination as 'dd:mm:ss.ss'), and <i>EPOCH</i> (epoch of
  coordinates defaults to 1950.0) give the position of the object whose
  spectrum this is.  <i>SITELONG</i> (observatory longitude as 'dd:mm:ss.ss'
  or degrees), <i>SITELAT</i> (observatory latitude as 'dd:mm:ss.ss' or
  degrees), and <i>SITEELEV</i> (observatory altitude in meters) give the
  observatory position.
  </dd>
  </dl>
  <dl id="l_report_mode">
  <dt><b>report_mode = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='report_mode' Line='report_mode = 1' -->
  <dd>Format of report sent to <i>logfiles</i>.  A tab table with column headings
  is written if the mode flag is negated.
  <dl>
  <dt><b>=1  Full information on each emission line found</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=1  Full information on each emission line found' -->
  <dd></dd>
  </dl>
  <dl>
  <dt><b>=2  One line per spectrum, with combined, cross-correlation, and</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=2  One line per spectrum, with combined, cross-correlation, and' -->
  <dd>emission line velocities, number of lines found and fit, and a list of
  names and wavelengths of the lines which were used in the fit.
  </dd>
  </dl>
  <dl>
  <dt><b>=3  One line per spectrum, with combined, cross-correlation, and</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=3  One line per spectrum, with combined, cross-correlation, and' -->
  <dd>emission line velocities, number of lines found and fit, and velocities
  for all possible reference lines, with velocities of lines not used in
  the final fit set to 0.
  </dd>
  </dl>
  <dl>
  <dt><b>=4  One line per spectrum, with file name, instrument, object, right</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=4  One line per spectrum, with file name, instrument, object, right' -->
  <dd>ascension, declination, altitude, azimuth, Julian date, exposure, emission
  velocity and error, cross-correlation velocity, error, and R-value (for
  the template specified by cortemp or best template value if cortemp is <span style="font-family: monospace;">""</span>),
  and the combined velocity and error. Following the number of lines found
  and the number of lines fit, the velocity, error, height, width, and
  equivalent width are then given for each line, with zero values indicating
  that the line was not used in the fit. If the continuum under the line is
  less than mincont, the area of the line is given instead of the equivalent
  width.
  </dd>
  </dl>
  <dl>
  <dt><b>=5 Same as mode 2, but emission line template cross-correlation velocity</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=5 Same as mode 2, but emission line template cross-correlation velocity' -->
  <dd>is always given as the cross-correlation velocity.
  </dd>
  </dl>
  <dl>
  <dt><b>=6 Same as mode 3, but emission line template cross-correlation velocity</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=6 Same as mode 3, but emission line template cross-correlation velocity' -->
  <dd>is always given as the cross-correlation velocity.
  </dd>
  </dl>
  <dl>
  <dt><b>=8 Single line report with line offset, error, height, width, and</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=8 Single line report with line offset, error, height, width, and' -->
  <dd>equivalent width for each emission line
  </dd>
  </dl>
  <dl>
  <dt><b>=9 Single line report with line offset for each emission line</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='=9 Single line report with line offset for each emission line' -->
  <dd></dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_archive">
  <dt><b>archive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='archive' Line='archive = no' -->
  <dd>If yes, save emission line results in SAO TDC archive record.
  </dd>
  </dl>
  <dl id="l_save_vel">
  <dt><b>save_vel = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='save_vel' Line='save_vel = no' -->
  <dd>If yes, save results in the IRAF image header.  Combined velocity and
  error are stored as <i>VELOCITY</i> and <i>VELERROR</i>.  Emission line
  velocity and error in IRAF image header as <i>CZEM</i> and <i>CZEMERR</i>,
  and the number of lines used in the fit is in <i>CZEMNLF</i>
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>If yes, results of the emission line search are logged.
  </dd>
  </dl>
  <dl id="l_logfiles">
  <dt><b>logfiles = <span style="font-family: monospace;">"STDOUT,emsao.log"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfiles' Line='logfiles = "STDOUT,emsao.log"' -->
  <dd>All results from <i>emvel</i> are recorded in these files.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "stdgraph"' -->
  <dd>Device on which to display graphic summary of results.
  </dd>
  </dl>
  <dl id="l_hardcopy">
  <dt><b>hardcopy = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hardcopy' Line='hardcopy = no' -->
  <dd>Print graphic summary of results on <i>plotter</i>.
  </dd>
  </dl>
  <dl id="l_displot">
  <dt><b>displot = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='displot' Line='displot = yes' -->
  <dd>If yes, graph data on terminal (yes or no)
  </dd>
  </dl>
  <dl id="l_plotter">
  <dt><b>plotter = <span style="font-family: monospace;">"stdplot"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotter' Line='plotter = "stdplot"' -->
  <dd>If <i>hardcopy</i> is yes, make hardcopies of graphs on this device.
  </dd>
  </dl>
  <dl id="l_dispmode">
  <dt><b>dispmode = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispmode' Line='dispmode = 2' -->
  <dd>Graphical display mode (2=with line list 3=full screen)
  </dd>
  </dl>
  <dl id="l_vel_plot">
  <dt><b>vel_plot <span style="font-family: monospace;">"emission"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vel_plot' Line='vel_plot "emission"' -->
  <dd>The redshift of this velocity is used to compute the positions of the
  absorption and emission lines which are flagged in the display.  Choices
  are emission, correlation, or combination (a weighted combined velocity).
  </dd>
  </dl>
  <dl id="l_curmode">
  <dt><b>curmode = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='curmode' Line='curmode = yes' -->
  <dd>If yes, stop in cursor mode after plotting and labelling spectrum and
  wait for cursor commands described below.
  </dd>
  </dl>
  <dl id="l_dispem">
  <dt><b>dispem = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispem' Line='dispem = yes' -->
  <dd>If yes, flag positions of emission lines which have been found.  Those
  used in the velocity fit are plotted as solid lines.  The <span style="font-family: monospace;">"-"</span> cursor
  command can be used to delete these from the fit.  Those lines found but
  omitted from the fit are plotted as dashed lines.  The <span style="font-family: monospace;">"+"</span> cursor
  command can be used to add them to the fit.
  </dd>
  </dl>
  <dl id="l_dispabs">
  <dt><b>dispabs = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispabs' Line='dispabs = yes' -->
  <dd>If yes, flag positions of absorption lines.
  </dd>
  </dl>
  <dl id="l_ablines">
  <dt><b>ablines <span style="font-family: monospace;">"ablines.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ablines' Line='ablines "ablines.dat"' -->
  <dd>File containing list of absorption lines to plot, where the each line contains:
  <br>
  	Center wavelength of line in angstroms
  <br>
  	Name of line (terminated by end of line or space)
  </dd>
  </dl>
  <dl id="l_velfit">
  <dt><b>velfit = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='velfit' Line='velfit = yes' -->
  <dd>If yes, combine the redshifts found for individual emission lines into a
  single emission line velocity. (eliminated from 1.8 on)
  </dd>
  </dl>
  <dl id="l_obj_plot">
  <dt><b>obj_plot yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obj_plot' Line='obj_plot yes' -->
  <dd>If yes, a plot of the object spectrum is displayed before the emission
  lines are searched for.
  </dd>
  </dl>
  <dl id="l_contsub_plot">
  <dt><b>contsub_plot = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='contsub_plot' Line='contsub_plot = no' -->
  <dd>Plot the continuum-subtracted data
  </dd>
  </dl>
  <dl id="l_debug">
  <dt><b>debug = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='debug' Line='debug = no' -->
  <dd>If yes, intermediate values of the parameters are recorded in the log files.
  Too much information is printed to be useful for anything but debugging.
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = 1' -->
  <dd>Number of pixels to sum across dispersion
  <dl>
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input.  When null the standard cursor is used otherwise
  the specified file is used.
  </dd>
  </dl>
   
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <i>emsao</i> finds emission lines, computes redshifts for each identified line,
  and combines them into a single radial velocity.  The results may be
  graphically displayed or printed.  If <i>curmode</i> is set, the graphic
  cursor remains active after the spectrum is plotted and labelled, and
  the following keystrokes may be used to redisplay and/or rework the
  fit (in addition to the standard IRAF cursor facilities, a menu of which
  can be obtained by typing :.help):
   
  <dl>
  <dt><b>?</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='?' -->
  <dd>Print list of <i>emsao</i> cursor commands.
  </dd>
  </dl>
  <dl>
  <dt><b>a</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='a' Line='a' -->
  <dd>Set redshift guess from an absorption line at the cursor position.  Respond to
  the prompt with either the line name from the ablines.dat file or a specific
  wavelength, which doesn't have to be one of the tabulated lines, in Angstroms.
  It might help to set the smoothing to 0 using <i>n</i> before doing this.
  </dd>
  </dl>
  <dl>
  <dt><b>b</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='b' Line='b' -->
  <dd>Set blue limit of spectrum to be searched to current cursor position. 
  </dd>
  </dl>
  <dl>
  <dt><b>c</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='c' Line='c' -->
  <dd>Force the final velocity to a specific value which may be 
  <dl>
  <dt><b>e the emission line velocity, </b></dt>
  <!-- Sec='DESCRIPTION' Level=2 Label='e' Line='e the emission line velocity, ' -->
  <dd></dd>
  </dl>
  <dl>
  <dt><b>x the cross-correlation velocity as read from the spectrum header, </b></dt>
  <!-- Sec='DESCRIPTION' Level=2 Label='x' Line='x the cross-correlation velocity as read from the spectrum header, ' -->
  <dd></dd>
  </dl>
  <dl>
  <dt><b>c the combination velocity as computed by emsao, </b></dt>
  <!-- Sec='DESCRIPTION' Level=2 Label='c' Line='c the combination velocity as computed by emsao, ' -->
  <dd></dd>
  </dl>
  <dl>
  <dt><b>g the initial guess as set by emsao.vel_init, </b></dt>
  <!-- Sec='DESCRIPTION' Level=2 Label='g' Line='g the initial guess as set by emsao.vel_init, ' -->
  <dd></dd>
  </dl>
  <dl>
  <dt><b>s a specific velocity and error to be typed in. </b></dt>
  <!-- Sec='DESCRIPTION' Level=2 Label='s' Line='s a specific velocity and error to be typed in. ' -->
  <dd></dd>
  </dl>
  </dd>
  </dl>
  <dl>
  <dt><b>d</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='d' Line='d' -->
  <dd>Replaces a region between the marked vertical cursors with interpolated
  values from the edges of the marked region.  This is typically used to
  eliminate poorly subtracted night sky lines or emission lines.
  <i>x</i> can be used to cancel the first <i>d</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>e</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='e' Line='e' -->
  <dd>Set redshift guess from an emission line at the cursor position.  Respond to
  the prompt with either the line name from the ablines.dat file or a specific
  wavelength, which doesn't have to be one of the tabulated lines, in Angstroms.
  It might help to set the smoothing to 0 using <i>n</i> before doing this.
  </dd>
  </dl>
  <dl>
  <dt><b>f</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='f' Line='f' -->
  <dd>Refit the redshift. If lines have been added or deleted, a new weighted
  mean is computed. If a new initial guess has been set or line fitting
  parameters have been modified, a new line search is done. 
  </dd>
  </dl>
  <dl>
  <dt><b>g</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='g' Line='g' -->
  <dd>Change number of times spectrum is smoothed (nsmooth) to the number given
  in response to prompt. It may help to set this to 0 before identifying
  emission or absorption lines using e or a. 
  </dd>
  </dl>
  <dl>
  <dt><b>i</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='i' Line='i' -->
  <dd>Reset the initial velocity for the line search. 
  </dd>
  </dl>
  <dl>
  <dt><b>k</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='k' Line='k' -->
  <dd>Toggle between display with continuum subtracted and display with continuum
  included (default).  This works for both dispmode=1 and dispmode=2.
  </dd>
  </dl>
  <dl>
  <dt><b>l</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='l' Line='l' -->
  <dd>Reset the <i>linesig</i> and <i>wspan</i> parameters which determine the
  the number of standard deviations above the continuum at which to define
  an emission line and the wavelength to search around the redshifted center
  of an individual line. 
  </dd>
  </dl>
  <dl>
  <dt><b>m</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='m' Line='m' -->
  <dd>Change number of times spectrum is smoothed (<i>esmooth</i>) for line fitting
  to the number given in response to the prompt.  This should be zero unless
  high noise levels are preventing good line fits in which case it may be set
  to 1, or at most, 2.
  </dd>
  </dl>
  <dl>
  <dt><b>n</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='n' Line='n' -->
  <dd>Disaprove the final velocity and set the quality flag to X.
  </dd>
  </dl>
  <dl>
  <dt><b>p</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='p' Line='p' -->
  <dd>Replot the current display.
  </dd>
  </dl>
  <dl>
  <dt><b>q</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='q' Line='q' -->
  <dd>Quit and exit.
  </dd>
  </dl>
  <dl>
  <dt><b>r</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='r' Line='r' -->
  <dd>Set the red limit of spectrum to be searched to current cursor position.
  </dd>
  </dl>
  <dl>
  <dt><b>s</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='s' Line='s' -->
  <dd>Set the redshift guess from an entered rest wavelength for the current
  cursor position.
  </dd>
  </dl>
  <dl>
  <dt><b>t</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='t' Line='t' -->
  <dd>Use the velocity from the nth template in the list displayed in a
  emsao.dispmode=1 summary display. 
  </dd>
  </dl>
  <dl>
  <dt><b>u</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='u' Line='u' -->
  <dd>Forces the current spectrum to be replotted at the original scale.
  </dd>
  </dl>
  <dl>
  <dt><b>v</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='v' Line='v' -->
  <dd>Select the source of the redshift at which the absorption and emission
  lines are plotted.  It may be an emission, correlation, or combined
  radial velocity from the image header as <i>CZEM</i>, <i>CZXC</i>, or
  <i>VELOCITY</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>w</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='w' Line='w' -->
  <dd>Show rest and observed wavelength at cursor position.
  </dd>
  </dl>
  <dl>
  <dt><b>x</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='x' Line='x' -->
  <dd>Cancel <i>d</i> and <i>z</i> commands before second keystroke.
  </dd>
  </dl>
  <dl>
  <dt><b>z</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='z' Line='z' -->
  <dd>Replots the region of the spectrum in wavelength between successive
  uses.  <i>x</i> can be used to cancel the first <i>z</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>+</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='+' -->
  <dd>Add closest found emission line to the velocity fit if it has been
  dropped, overriding program's selection criteria.  If this doesn't work,
  use the <i>v</i> command to plot using the emission velocity.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">'-'</span></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line=''-'' -->
  <dd>Drop closest found emission line from the velocity fit if it has been
  used, overriding program's selection criteria.  If this doesn't work,
  use the <i>v</i> command to plot using the emission velocity.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">'.'</span></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line=''.'' -->
  <dd>Cancel delete (d) or zoom (z) command. 
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">'/'</span></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line=''/'' -->
  <dd>Toggle between spectrum plus summary display (dispmode=1) and full screen
  spectrum display (dispmode=2).
  </dd>
  </dl>
  <dl>
  <dt><b>@</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='@' -->
  <dd>Make hard copy of graph to <i>plotter</i>.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  To obtain the redshift and dispersion of a single galaxy
          rvsao&gt; emsao galaxy
  To obtain redshifts for a whole night's worth of galaxy spectra:
          rvsao&gt; emsao @nite1.ls
  where the file nite1.ls contains the name of the galaxy images.
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  rvsao.contpars which sets the continuum fit parameters
  On-line help is available on the World Wide Web at
  http://tdc-www.harvard.edu/iraf/rvsao/emsao
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

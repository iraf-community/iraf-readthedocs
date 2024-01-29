.. _sumspec:

sumspec: Combine multiple spectra into an assigned-velocity spectrum
====================================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  sumspec spectra compfile
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
  a range of spectrum numbers in a multispec file which will be added.
  Wavelength dispersion information is read from APNUMn or the WCS keywords.
  Velocity information is read from APVELn and saved in APVELn and APVXCn.
  In a non-multispec file, radial velocity is read from the VELOCITY header
  parameter. 
  </dd>
  </dl>
  <dl id="l_specband">
  <dt><b>specband = 0 </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specband' Line='specband = 0 ' -->
  <dd>If this is nonzero, it is the band in the multispec file(s) specified by
  spectra which will be summed.  Wavelength dispersion information
  is read from APNUMn, where n is the aperture specified by <i>specnum</i> or the
  WCS keywords. Velocity information is read from APVELn and saved in APVELn
  and APVXCn. (New in version 2.0) 
  </dd>
  </dl>
  <dl id="l_specdir">
  <dt><b>specdir = <span style="font-family: monospace;">"./"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specdir' Line='specdir = "./"' -->
  <dd>Directory containing spectra to analyze.  This part of the pathname is not
  printed at the top of the page, and is assumed to be the same for all
  spectra listed in the spectra parameter. 
  </dd>
  </dl>
  <dl id="l_compfile">
  <dt><b>compfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='compfile' Line='compfile = ""' -->
  <dd>File name for output spectrum.
  </dd>
  </dl>
  <dl id="l_compname">
  <dt><b>compname = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='compname' Line='compname = ""' -->
  <dd>Title for output spectrum.
  </dd>
  </dl>
  <dl id="l_compdir">
  <dt><b>compdir = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='compdir' Line='compdir = ""' -->
  <dd>Directory for output spectrum
  </dd>
  </dl>
  <dl id="l_nspec">
  <dt><b>nspec = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nspec' Line='nspec = 1' -->
  <dd>Number of spectra in output file
  </dd>
  </dl>
  <dl id="l_save_names">
  <dt><b>save_names = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='save_names' Line='save_names = yes' -->
  <dd>Save names of input files in output file header (yes or no)
  </dd>
  </dl>
  <dl id="l_copy_header">
  <dt><b>copy_header = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='copy_header' Line='copy_header = yes' -->
  <dd>Copy output header from first input spectrum (yes or no)
  </dd>
  </dl>
  <dl id="l_normin">
  <dt><b>normin = no </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='normin' Line='normin = no ' -->
  <dd>If yes, the data spectrum is divided by its mean value before being processed.
  Use this on spectra which have unusual data values such as those produced
  by flux calibration.
  </dd>
  </dl>
  <dl id="l_fixbad">
  <dt><b>fixbad = no </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fixbad' Line='fixbad = no ' -->
  <dd>If <span style="font-family: monospace;">"yes"</span>, remove wavelength-delimited regions listed in the file specfied
  by <i>badlines</i>. (added in version 2.0) 
  </dd>
  </dl>
  <dl id="l_badlines">
  <dt><b>badlines = badlines.dat </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='badlines' Line='badlines = badlines.dat ' -->
  <dd>File containing list of starting and stopping wavelengths in Angstroms
  for removal of portions of all object spectra if <i>fixbad</i> is yes.
  All information after the second wavelength is a comment field. This file
  is assumed to be in the directory <i>linedir</i> unless a complete pathname
  starting with <span style="font-family: monospace;">"/"</span> is specified. (added in version 2.0) 
  </dd>
  </dl>
  <dl id="l_linedir">
  <dt><b>linedir = <span style="font-family: monospace;">"rvsao$lib/"</span> </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linedir' Line='linedir = "rvsao$lib/" ' -->
  <dd>Directory containing line list file named by badlines. This parameter is
  ignored if: that filename contains a <span style="font-family: monospace;">"/"</span> in the first column, as it is
  assumed to be a full pathname, if there is a <span style="font-family: monospace;">"/"</span> anywhere else in the
  filename, as it is assumed to be a path relative to the current working
  directory, or if there is a <span style="font-family: monospace;">"$"</span> in the filename, as the part preceding
  the <span style="font-family: monospace;">"$"</span> is assumed to be an IRAF environment parameter (ending in <span style="font-family: monospace;">"/"</span>)
  defining a directory. 
  </dd>
  </dl>
  <dl id="l_cont_remove">
  <dt><b>cont_remove = no </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cont_remove' Line='cont_remove = no ' -->
  <dd>Remove continuum from input spectra if not <span style="font-family: monospace;">"no"</span>. If <span style="font-family: monospace;">"subtract"</span>, subtract
  continuum. If <span style="font-family: monospace;">"divide"</span>, divide by continuum. If <span style="font-family: monospace;">"zerodiv"</span>, divide by
  continuum and subtract 1. This last should be used instead of <span style="font-family: monospace;">"divide"</span>
  if the file is to be cross-correlated. In version 2.0, <span style="font-family: monospace;">"divide"</span> subtracted
  1; in version 2.1b15 and later, it doesn't, and the <span style="font-family: monospace;">"zerodiv"</span> option was added. 
  Parameters used in the fit are mostly set in the contsum pset.
  </dd>
  </dl>
  <dl id="l_cont_split">
  <dt><b>cont_split = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cont_split' Line='cont_split = 1' -->
  <dd>Number of regions into which to split the spectrum for separate continuum fits
  </dd>
  </dl>
  <dl id="l_reject">
  <dt><b>reject = <span style="font-family: monospace;">"no"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reject' Line='reject = "no"' -->
  <dd>Chop out emission lines from object spectra before adding them to the
  composite spectrum if <span style="font-family: monospace;">"yes"</span>.  If <span style="font-family: monospace;">"specfile"</span>, emission lines are removed
  if the value of the CHOPEM keyword in the object spectrum image header is
  T.  If the keyword is not present or is F, emission lines are not removed.
  If <span style="font-family: monospace;">"no"</span>, emission lines are never removed.  If EMCHOP in the input spectrum
  file is 1, emission lines are not removed.
  </dd>
  </dl>
  <dl id="l_abs_reject">
  <dt><b>abs_reject = 100.0 </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='abs_reject' Line='abs_reject = 100.0 ' -->
  <dd>Input spectrum absorption line rejection in sigma of fit 
  </dd>
  </dl>
  <dl id="l_em_reject">
  <dt><b>em_reject = 2.0 </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='em_reject' Line='em_reject = 2.0 ' -->
  <dd>Input spectrum emission line rejection in sigma of fit 
  </dd>
  </dl>
  <dl id="l_contout">
  <dt><b>contout = no </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='contout' Line='contout = no ' -->
  <dd>Remove continuum from output spectrum/spectra if not <span style="font-family: monospace;">"no"</span>.
  If <span style="font-family: monospace;">"subtract"</span>, subtract continuum.
  If <span style="font-family: monospace;">"divide"</span>, divide by continuum.
  If <span style="font-family: monospace;">"zerodiv"</span>, divide by continuum and subtract 1. This last should be
  used instead of <span style="font-family: monospace;">"divide"</span> if the file is to be cross-correlated. In
  version 2.0, <span style="font-family: monospace;">"divide"</span> subtracted 1; in version 2.1b15 and later, it
  doesn't, and the <span style="font-family: monospace;">"zerodiv"</span> option was added. 
  Parameters used in the fit are mostly set in the contsum pset.
  </dd>
  </dl>
  <dl id="l_cont_plot">
  <dt><b>cont_plot = yes </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cont_plot' Line='cont_plot = yes ' -->
  <dd>If yes, plots of the continuum-subtracted input spectra are displayed.
  This is most useful for determining the appropriateness of the continuum
  fitting parameters.
  </dd>
  </dl>
  <dl id="l_cont_add">
  <dt><b>cont_add = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cont_add' Line='cont_add = 0' -->
  <dd>Continuum level added to output spectrum to keep all flux above zero, for
  example
  </dd>
  </dl>
  <dl id="l_spec_smooth">
  <dt><b>spec_smooth = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spec_smooth' Line='spec_smooth = 0' -->
  <dd>If &gt;0, the spectra are smoothed <i>smooth</i> times before graphing them.
  The spectrum is NEVER smoothedvefore adding
  </dd>
  </dl>
  <dl id="l_st_lambda">
  <dt><b>st_lambda = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='st_lambda' Line='st_lambda = INDEF' -->
  <dd>Starting wavelength in angstroms of output spectrum.
  If INDEF, use beginning of wavelength overlap between input spectra.
  </dd>
  </dl>
  <dl id="l_end_lambda">
  <dt><b>end_lambda = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='end_lambda' Line='end_lambda = INDEF' -->
  <dd>Ending wavelength in angstroms of output spectrum.
  If INDEF, use end of wavelength overlap between input spectra.
  </dd>
  </dl>
  <dl id="l_pix_lambda">
  <dt><b>pix_lambda = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pix_lambda' Line='pix_lambda = INDEF' -->
  <dd>Wavelength per pixel in angstroms of output spectrum.
  If INDEF, compute from wavelength range and number of pixels in output spectra.
  </dd>
  </dl>
  <dl id="l_ncol">
  <dt><b>ncol = 2048</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncol' Line='ncol = 2048' -->
  <dd>Number of pixels into which to rebin data.
  </dd>
  </dl>
  <dl id="l_complog">
  <dt><b>complog = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='complog' Line='complog = no' -->
  <dd>Rebin into log wavelength (yes or no)
  </dd>
  </dl>
  <dl id="l_interp_mode">
  <dt><b>interp_mode = <span style="font-family: monospace;">"spline3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interp_mode' Line='interp_mode = "spline3"' -->
  <dd>Interpolation mode to use when rebinning spectra, must be
  <span style="font-family: monospace;">"nearest"</span> or <span style="font-family: monospace;">"linear"</span> or <span style="font-family: monospace;">"spline3"</span> or <span style="font-family: monospace;">"poly3"</span> or <span style="font-family: monospace;">"poly5"</span> or <span style="font-family: monospace;">"sinc"</span> or <span style="font-family: monospace;">"lsinc"</span>
  or <span style="font-family: monospace;">"drizzle"</span> or <span style="font-family: monospace;">"sums"</span>.
  </dd>
  </dl>
  <dl id="l_normout">
  <dt><b>normout = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='normout' Line='normout = no' -->
  <dd>If true, the output spectrum is divided by its mean value before being
  transformed.  This is used on spectra which may have unusual values due
  to their having already been flux-calibrated.
  </dd>
  </dl>
  <dl id="l_spec_plot">
  <dt><b>spec_plot = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spec_plot' Line='spec_plot = yes' -->
  <dd>If yes, plots of the individual spectra are displayed.  During this time the
  normal IRAF cursor commands are active as well as several more that are
  itemized below.  If emission lines are chopped, before and after plots
  are displayed, as well as the chopped line(s).
  </dd>
  </dl>
  <dl id="l_spec_int">
  <dt><b>spec_int = no </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spec_int' Line='spec_int = no ' -->
  <dd>If yes, pause in cursor mode after each input spectrum has been plotted.
  </dd>
  </dl>
  <dl id="l_comp_plot">
  <dt><b>comp_plot = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='comp_plot' Line='comp_plot = yes' -->
  <dd>If yes, a plot of the output spectrum is displayed after each input spectrum is
  added.  Cursor commands are activated for zooming in on a portion of the
  spectrum and hard copies may be made to stdplot using the <i>@</i> command.
  </dd>
  </dl>
  <dl id="l_comp_int">
  <dt><b>comp_int = no </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='comp_int' Line='comp_int = no ' -->
  <dd>If yes, pause in cursor mode after the composite spectrum has been plotted.
  </dd>
  </dl>
  <dl id="l_ymin">
  <dt><b>ymin = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ymin' Line='ymin = INDEF' -->
  <dd>Minimum y value to plot.  Autoscale if INDEF
  </dd>
  </dl>
  <dl id="l_ymax">
  <dt><b>ymax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ymax' Line='ymax = INDEF' -->
  <dd>Maximum y value to plot.  Autoscale if INDEF
  </dd>
  </dl>
  <dl id="l_velcomp">
  <dt><b>velcomp = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='velcomp' Line='velcomp = INDEF' -->
  <dd>Velocity in km/sec to which to shift individual spectra. If INDEF, do not shift
  spectra at all.
  </dd>
  </dl>
  <dl id="l_zcomp">
  <dt><b>zcomp = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zcomp' Line='zcomp = INDEF' -->
  <dd>Velocity of output spectrum as delta lambda / lambda; overrides velcomp if not
  INDEF.
  </dd>
  </dl>
  <dl id="l_svel_corr">
  <dt><b>svel_corr = <span style="font-family: monospace;">"barycentric"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='svel_corr' Line='svel_corr = "barycentric"' -->
  <dd>Spectrum velocity correction to the solar system barycenter.  Set to
  <span style="font-family: monospace;">"none"</span> if spectrum has already been shifted or if this correction is
  unnecessary.  If <span style="font-family: monospace;">"file"</span>, <i>BCV</i> is used if present in the file header,
  or else <i>HCV</i>.  If <span style="font-family: monospace;">"hfile"</span>, the header parameter <i>HCV</i> is always
  used.  If neither is found, no correction is made.  If svel_corr is not
  set to <span style="font-family: monospace;">"none"</span>, but velcomp and zcomp are INDEF, data is shifted to the
  barycentric velocity correction of the first spectrum, if it has one.
  If <span style="font-family: monospace;">"heliocentric"</span> or <span style="font-family: monospace;">"barycentric"</span> corrections are chosen, position and
  time parameters are read from the spectrum data file header.  <i>DATE-OBS</i>
  (date in format 'dd-mm-yy') <i>UT</i> (U.T. at end of exposure as 'hh:mm:ss')
  and <i>UTOPEN</i> (U.T. at start of exposure as 'hh:mm:ss') or
  <i>EXPOSURE</i> (length of exposure in seconds) are used to compute
  the midtime of the exposure.  <i>RA</i> (right ascension as 'hh:mm:ss.ss'),
  <i>DEC</i> (declination as 'dd:mm:ss.ss'), and <i>EPOCH</i> (epoch of
  coordinates defaults to 1950.0) give the position of the object whose
  spectrum this is.  <i>SITELONG</i> (observatory longitude as 'dd:mm:ss.ss'
  or degrees), <i>SITELAT</i> (observatory latitude as 'dd:mm:ss.ss' or
  degrees), and <i>SITEELEV</i> (observatory altitude in meters) give the
  observatory position.  Use bcvcorr task to set BCV in header and use <span style="font-family: monospace;">"file"</span>
  here if header parameters are different.
  </dd>
  </dl>
  <dl id="l_nsmooth">
  <dt><b>nsmooth = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsmooth' Line='nsmooth = 0' -->
  <dd>Number of times to 1-2-1 smooth displayed spectrum
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "stdgraph"' -->
  <dd>Interactive device on which to graphicallly
  </dd>
  </dl>
  <dl id="l_plotter">
  <dt><b>plotter = <span style="font-family: monospace;">"stdplot"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotter' Line='plotter = "stdplot"' -->
  <dd>Second, non-interactive device on which to plot the graphic summary of results.
  </dd>
  </dl>
  <dl id="l_logfiles">
  <dt><b>logfiles = <span style="font-family: monospace;">"STDOUT,sumtemp.log"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfiles' Line='logfiles = "STDOUT,sumtemp.log"' -->
  <dd>All results from SUMTEMP are recorded in these files.
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = 1' -->
  <dd>Number of pixels to sum across dispersion
  </dd>
  </dl>
  <dl id="l_debug">
  <dt><b>debug = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='debug' Line='debug = no' -->
  <dd>If yes, values of the parameters fit to the selected peak
  are recorded in the log files.  This is most useful for debugging.
  </dd>
  </dl>
  <p>
   
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  SUMSPEC combines spectra, shifting them to a common redshift, if either the
  <i>vel_comp</i> or the <i>z_comp</i> parameter is not INDEF.  The
  VELOCITY header parameter of each of these spectra is assumed to be
  a solar-system-barycenter-corrected velocity, and a barycentric
  correction (computed by SUMSPEC or extracted from the BCV or HCV
  header parameter) is subracted to get the redshift of the spectrum.
  Each spectrum is shifted and rebinned to log or linear wavelength, then added
  to the composite spectrum.  Input may be multispec or twodspec format,
  but output is always a one-dimensional file.
   
  </p>
  </section>
  <section id="s_cursor">
  <h3>Cursor</h3>
  <p>
  The following keystrokes are active for graphs of input and output spectra
  in addition to the normal IRAF cursor facilities (a list of those is
  available with the command <span style="font-family: monospace;">":.help"</span>):
  </p>
  <dl>
  <dt><b>@</b></dt>
  <!-- Sec='CURSOR' Level=0 Label='' Line='@' -->
  <dd>Make a hard copy on the device designated by <i>plotter</i>.
  </dd>
  </dl>
  <dl id="l_c">
  <dt><b>c</b></dt>
  <!-- Sec='CURSOR' Level=0 Label='c' Line='c' -->
  <dd>Prints cursor position in x and y.  This is the default.  All other
  undefined keys perform this same function.
  </dd>
  </dl>
  <dl id="l_d">
  <dt><b>d</b></dt>
  <!-- Sec='CURSOR' Level=0 Label='d' Line='d' -->
  <dd>Replaces a region between the marked vertical cursors with interpolated
  values from the edges of the marked region.  This is typically used to
  eliminate poorly subtracted night sky lines or emission lines.
  </dd>
  </dl>
  <dl id="l_n">
  <dt><b>n</b></dt>
  <!-- Sec='CURSOR' Level=0 Label='n' Line='n' -->
  <dd>Smooth spectrum n times before plotting.  This only affects to current
  spectrum display and the final spectrum graph, not the spectrum data.
  </dd>
  </dl>
  <dl id="l_q">
  <dt><b>q</b></dt>
  <!-- Sec='CURSOR' Level=0 Label='q' Line='q' -->
  <dd>Quit and exit.
  </dd>
  </dl>
  <dl id="l_r">
  <dt><b>r</b></dt>
  <!-- Sec='CURSOR' Level=0 Label='r' Line='r' -->
  <dd>Forces a replot of the current spectrum at the original scale.
  </dd>
  </dl>
  <dl id="l_u">
  <dt><b>u</b></dt>
  <!-- Sec='CURSOR' Level=0 Label='u' Line='u' -->
  <dd>Redisplay the entire plot after zooming.
  </dd>
  </dl>
  <dl id="l_z">
  <dt><b>z</b></dt>
  <!-- Sec='CURSOR' Level=0 Label='z' Line='z' -->
  <dd>Zoom in on the region marked by two successive &lt;z&gt;'s
  </dd>
  </dl>
  </section>
  <section id="s_example">
  <h3>Example</h3>
  <p>
  To make a galaxy template by combining a list of galaxy spectra:
  </p>
  <p>
          rvsao&gt; sumspec @galaxies template=galtemp tempvel=1000.0
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rvsao.contsum which sets the continuum fit parameters
  </p>
  <p>
  On-line help is available over the World Wide Web at
  http://tdc-www.harvard.edu/iraf/rvsao/sumspec
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR' 'EXAMPLE' 'SEE ALSO'  -->
  

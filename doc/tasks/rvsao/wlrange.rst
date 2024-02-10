.. _wlrange:

wlrange: Find the overlapping wavelength range in a list of spectra
===================================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  wlrange spectra
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
  <dt><b>ncol = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncol' Line='ncol = INDEF' -->
  <dd>Number of pixels into which to rebin data.
  </dd>
  </dl>
  <dl id="l_wl1">
  <dt><b>wl1 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wl1' Line='wl1 = INDEF' -->
  <dd>Reddest wavelength in Angstroms (returned)
  </dd>
  </dl>
  <dl id="l_wl2">
  <dt><b>wl2 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wl2' Line='wl2 = INDEF' -->
  <dd>Bluest wavelength in Angstroms (returned)
  </dd>
  </dl>
  <dl id="l_dwl">
  <dt><b>dwl = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dwl' Line='dwl = INDEF' -->
  <dd>Wavelength per pixel in Angstroms (returned)
  </dd>
  </dl>
  <dl id="l_npix">
  <dt><b>npix = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='npix' Line='npix = INDEF' -->
  <dd>Number of pixels (from file or set) (returned)
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
  <dl id="l_nsum">
  <dt><b>nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = 1' -->
  <dd>Number of pixels to sum across dispersion
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Display final result (yes or no)
  </dd>
  </dl>
  <dl id="l_debug">
  <dt><b>debug = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='debug' Line='debug = no' -->
  <dd>Display intermediate results (yes or no)
  </dd>
  </dl>
  <p>
   
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  WLRANGE reads a list of spectra, shifting them to a common redshift, if either the
  <i>vel_comp</i> or the <i>z_comp</i> parameter is not INDEF.  The
  VELOCITY header parameter of each of these spectra is assumed to be
  a solar-system-barycenter-corrected velocity, and a barycentric
  correction (computed by SUMSPEC or extracted from the BCV or HCV
  header parameter) is subracted to get the redshift of the spectrum.
  </p>
  <p>
  The wavelength overlap blue and red limits are returned as well as
  the maximum number of pixels per spectrum and a wavelength per pixel
  binning which would match that number to the range.
   
  </p>
  </section>
  <section id="s_example">
  <h3>Example</h3>
  <p>
  Get the overlapping wavelength range for a 300-fiber Hectospec spectrum:
  </p>
  <p>
          rvsao&gt; wlrange comp.ms.fits
          WLRANGE: 4608-point spectra from 3550.852A to 6040.839A by 0.540A
          rvsao&gt; dpar wlrange
          wlrange.spectra = <span style="font-family: monospace;">"comp.ms.fits[1-300]"</span>
          wlrange.specnum = <span style="font-family: monospace;">"0"</span>
          wlrange.specband = 0
          wlrange.specdir = <span style="font-family: monospace;">""</span>
          wlrange.st_lambda = INDEF
          wlrange.end_lambda = INDEF
          wlrange.pix_lambda = INDEF
          wlrange.npts = INDEF
          wlrange.wl1 = 3550.8524067942
          wlrange.wl2 = 6040.838948816
          wlrange.dwl = 0.54047895420487
          wlrange.npix = 4608
          wlrange.velcomp = INDEF
          wlrange.zcomp = INDEF
          wlrange.svel_corr = <span style="font-family: monospace;">"none"</span>
          wlrange.nsum = 1
          wlrange.verbose = yes
          wlrange.debug = no
          wlrange.mode = <span style="font-family: monospace;">"ql"</span>
          # EOF
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  On-line help is available over the World Wide Web at
  http://tdc-www.harvard.edu/iraf/rvsao/wlrange
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLE' 'SEE ALSO'  -->
  

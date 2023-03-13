.. _keywpars:

keywpars: Translate the image header keywords used in RV package
================================================================

**Package: rv**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  keywpars
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_ra">
  <dt><b>ra = <span style="font-family: monospace;">"RA"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ra' Line='ra = "RA"' -->
  <dd>Right Ascension keyword. (Value in HMS format).
  </dd>
  </dl>
  <dl id="l_dec">
  <dt><b>dec = <span style="font-family: monospace;">"DEC"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dec' Line='dec = "DEC"' -->
  <dd>Declination keyword. (Value in HMS format).
  </dd>
  </dl>
  <dl id="l_ut">
  <dt><b>ut = <span style="font-family: monospace;">"UT"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ut' Line='ut = "UT"' -->
  <dd>UT of observation keyword.  This field is the UT start of the observation.
  (Value in HMS Format).
  </dd>
  </dl>
  <dl id="l_utmiddle">
  <dt><b>utmiddle = <span style="font-family: monospace;">"UTMIDDLE"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='utmiddle' Line='utmiddle = "UTMIDDLE"' -->
  <dd>UT mid-point of observation keyword.  This field is the UT mid-point of 
  the observation.  (Value in HMS Format).
  </dd>
  </dl>
  <dl id="l_exptime">
  <dt><b>exptime = <span style="font-family: monospace;">"EXPTIME"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exptime' Line='exptime = "EXPTIME"' -->
  <dd>Exposure time keyword. (Value in Seconds).
  </dd>
  </dl>
  <dl id="l_epoch">
  <dt><b>epoch = <span style="font-family: monospace;">"EPOCH"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='epoch' Line='epoch = "EPOCH"' -->
  <dd>Epoch of coordinates keyword. (Value in Years).
  </dd>
  </dl>
  <dl id="l_date_obs">
  <dt><b>date_obs = <span style="font-family: monospace;">"DATE-OBS"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='date_obs' Line='date_obs = "DATE-OBS"' -->
  <dd>Date of observation keyword.  Format for this field should be
  dd/mm/yy, (old FITS format), yyyy-mm-dd (new FITS format), or
  yyyy-mm-ddThh:mm:ss.sss (new FITS format with time).
  </dd>
  </dl>
  <p style="text-align:center">OUTPUT KEYWORDS
  
  </p>
  <dl id="l_hjd">
  <dt><b>hjd = <span style="font-family: monospace;">"HJD"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hjd' Line='hjd = "HJD"' -->
  <dd>Heliocentric Julian date keyword. (Value in Days).
  </dd>
  </dl>
  <dl id="l_mjd_obs">
  <dt><b>mjd_obs = <span style="font-family: monospace;">"MJD-OBS"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mjd_obs' Line='mjd_obs = "MJD-OBS"' -->
  <dd>Modified Julian Data keyword.  The MJD is defined as the julian date of
  the mid-point of the observation - 2440000.5.  (Value in Days).
  </dd>
  </dl>
  <dl id="l_vobs">
  <dt><b>vobs = <span style="font-family: monospace;">"VOBS"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vobs' Line='vobs = "VOBS"' -->
  <dd>Observed radial velocity keyword.  (Value in Km/sec).
  </dd>
  </dl>
  <dl id="l_vrel">
  <dt><b>vrel = <span style="font-family: monospace;">"VREL"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vrel' Line='vrel = "VREL"' -->
  <dd>Observed radial velocity keyword. (Value in Km/sec).
  </dd>
  </dl>
  <dl id="l_vhelio">
  <dt><b>vhelio = <span style="font-family: monospace;">"VHELIO"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vhelio' Line='vhelio = "VHELIO"' -->
  <dd>Corrected heliocentric radial velocity keyword.  (Value in Km/sec).
  </dd>
  </dl>
  <dl id="l_vlsr">
  <dt><b>vlsr = <span style="font-family: monospace;">"VLSR"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vlsr' Line='vlsr = "VLSR"' -->
  <dd>Local Standard of Rest velocity keyword.  (Value in Km/sec).
  </dd>
  </dl>
  <dl id="l_vsun">
  <dt><b>vsun = <span style="font-family: monospace;">"VSUN"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vsun' Line='vsun = "VSUN"' -->
  <dd>Epoch of solar motion.  (Character string with four real valued fields 
  describing the solar velocity (km/sec), the RA of the solar velocity (hours),
  the declination of the solar velocity (degrees), and the epoch of solar
  coordinates (years)).
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The image header keywords used by the <i>fxcor</i> task can be 
  edited if they differ
  from the NOAO standard keywords.  For example, if the image header keyword
  giving the exposure time for the image is written out as <span style="font-family: monospace;">"EXP-TIME"</span> instead
  of the standard <span style="font-family: monospace;">"OTIME"</span> at a given site, the keyword accessed for 
  that information
  may be changed based on the value of the <i>exptime</i> parameter.
  </p>
  <p>
  The <i>vhelio</i> keywords must be added to the image header of the template 
  spectrum and should contain the known radial velocity of the template star.
  The output keywords may be added to the object image header if the
  tasks <i>fxcor.imudate</i> parameter is set.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the image header keywords.
  </p>
  <div class="highlight-default-notranslate"><pre>
  rv&gt; lpar keywpars
  </pre></div>
  <p>
  2. Edit the image header keywords
  </p>
  <div class="highlight-default-notranslate"><pre>
  rv&gt; keywpars
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fxcor
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

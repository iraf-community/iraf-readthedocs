.. _bcvcorr:

bcvcorr: Compute radial velocity correction to solar system barycenter
======================================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  bcvcorr image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <p>
  # Spectra
  </p>
  <dl id="l_spectra">
  <dt><b>spectra <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectra' Line='spectra ""' -->
  <dd>List of input spectra
  </dd>
  </dl>
  <dl id="l_specnum">
  <dt><b>specnum <span style="font-family: monospace;">"0"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specnum' Line='specnum "0"' -->
  <dd>Spectrum number(s) if multispec file.  This affects how the barycentric
  velocity will be written into the header if savebcv is yes.  If specnum
  is 0, the BCV keyword is used; otherwise, APVELn is used, with the
  barycentric velocity correction in the 4th field: 0.0 0.0 _ bcv .
  </dd>
  </dl>
  <dl id="l_specdir">
  <dt><b>specdir <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specdir' Line='specdir ""' -->
  <dd>Directory for input spectra
  </dd>
  </dl>
  <dl id="l_specsky">
  <dt><b>specsky no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specsky' Line='specsky no' -->
  <dd>If yes, this spectrum is a twilight sky or solar spectrum, and the
  velocity correction is computed from the direction of the sun, not
  the telescope pointing correction.
  </dd>
  </dl>
  <dl id="l_subgrav">
  <dt><b>subgrav no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subgrav' Line='subgrav no' -->
  <dd>If subgrav=yes and specsky=yes, subtract a correction for the sun's
  gravity (0.636) from the barycentric and heliocentric corrections
  computed by the program.  If savebcv=yes, BCV, HCV, and SGRV are
  written to the image header.  HCV, the velocity of the sun relative
  to the spectrograph with the gravitational correction subtracted,
  should be used as the spectrum correction
  (rvsao.svel_corr=heliocentric)
  when cross-correlating twilight spectra with XCSAO.
  # Sky direction
  <dl>
  <dt><b>keyra <span style="font-family: monospace;">"RA"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='keyra' Line='keyra "RA"' -->
  <dd>Right ascension header keyword
  </dd>
  </dl>
  <dl>
  <dt><b>keydec <span style="font-family: monospace;">"DEC"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='keydec' Line='keydec "DEC"' -->
  <dd>Declination header keyword
  </dd>
  </dl>
  <dl>
  <dt><b>keyeqnx <span style="font-family: monospace;">"EPOCH"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='keyeqnx' Line='keyeqnx "EPOCH"' -->
  <dd>Coordinate equinox header keyword
  </dd>
  </dl>
  <dl>
  <dt><b>keyjd <span style="font-family: monospace;">"HJD"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='keyjd' Line='keyjd "HJD"' -->
  <dd>Header keyword for Julian date at middle of observation
  </dd>
  </dl>
  <dl>
  <dt><b>keydate <span style="font-family: monospace;">"DATE-OBS"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='keydate' Line='keydate "DATE-OBS"' -->
  <dd>Header keyword for date of observation (dd/mm/yyyy)
  </dd>
  </dl>
  <dl>
  <dt><b>keystart <span style="font-family: monospace;">"UTOPEN"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='keystart' Line='keystart "UTOPEN"' -->
  <dd>Header keyword for UT at start of observation
  </dd>
  </dl>
  <dl>
  <dt><b>keymid <span style="font-family: monospace;">"UTMID"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='keymid' Line='keymid "UTMID"' -->
  <dd>Header keyword for UT in middle of observation
  </dd>
  </dl>
  <dl>
  <dt><b>keyend <span style="font-family: monospace;">"UT"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='keyend' Line='keyend "UT"' -->
  <dd>Header keyword for UT at end of observation
  </dd>
  </dl>
  <dl>
  <dt><b>keyexp <span style="font-family: monospace;">"EXPOSURE"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='keyexp' Line='keyexp "EXPOSURE"' -->
  <dd>Header keyword for duration of observation in seconds
  </dd>
  </dl>
  <dl>
  <dt><b>obsname <span style="font-family: monospace;">"file"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='obsname' Line='obsname "file"' -->
  <dd>Observatory name. If file to read from image header
  </dd>
  </dl>
  <dl>
  <dt><b>keyobs <span style="font-family: monospace;">"SITENAME"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='keyobs' Line='keyobs "SITENAME"' -->
  <dd>Observatory name header keyword
  </dd>
  </dl>
  <dl>
  <dt><b>keylat <span style="font-family: monospace;">"SITELAT"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='keylat' Line='keylat "SITELAT"' -->
  <dd>Observatory latitude header keyword
  </dd>
  </dl>
  <dl>
  <dt><b>keylong <span style="font-family: monospace;">"SITELONG"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='keylong' Line='keylong "SITELONG"' -->
  <dd>Observatory longitude header keyword
  </dd>
  </dl>
  <dl>
  <dt><b>keyalt <span style="font-family: monospace;">"SITEALT"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='keyalt' Line='keyalt "SITEALT"' -->
  <dd>Observatory altitude header keyword
  </dd>
  </dl>
  <dl>
  <dt><b>obslong 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='obslong' Line='obslong 0.0' -->
  <dd>Observatory longitude, used if obsname is not <span style="font-family: monospace;">"file"</span>
  </dd>
  </dl>
  <dl>
  <dt><b>obslat 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='obslat' Line='obslat 0.0' -->
  <dd>Observatory latitude, used if obsname is not <span style="font-family: monospace;">"file"</span>
  </dd>
  </dl>
  <dl>
  <dt><b>obsalt 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='obsalt' Line='obsalt 0.0' -->
  <dd>Observatory altitude in meters, used if obsname is not <span style="font-family: monospace;">"file"</span>
  </dd>
  </dl>
  <dl>
  <dt><b>savebcv no</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='savebcv' Line='savebcv no' -->
  <dd>Save barycentric velocity correction as BCV and heliocentric velocity
  correction as HCV in data file header (yes or no)
  </dd>
  </dl>
  <dl>
  <dt><b>savejd no</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='savejd' Line='savejd no' -->
  <dd>Save Geocentric Julian Date as GJDN, Heliocentric Julian Date
  as HJDN, and UT midtime of observation as UTMID in data file header (yes or no)
  </dd>
  </dl>
  <dl>
  <dt><b>verbose yes</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='verbose' Line='verbose yes' -->
  <dd>Displays heliocentric and barycentric corrections
  </dd>
  </dl>
  <dl>
  <dt><b>printmode 1</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='printmode' Line='printmode 1' -->
  <dd>If 1, display heliocentric and barycentric corrections and ancillary data;
  if 2, display only barycentric correction
  </dd>
  </dl>
  <dl>
  <dt><b>debug no</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='debug' Line='debug no' -->
  <dd>Displays intermediate results
  </dd>
  </dl>
   
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <i>bcvcorr</i> can be used to set the barycentric velocity correction of
  spectra which do not have the header keywords expected by the correction
  computation subroutine in XCSAO, EMSAO, or SUMSPEC, or use different
  keywords than the program expects.  The time, date, direction, and
  observatory can come from specified keywords or values directly from
  parameters.  In the case of the observatory position, a third option is
  to set the obsname parameter to a string which is looked up in the IRAF
  observatory database.  Either keymid or two of keystart, keyend, and
  keyexp will be used to compute the exact observation time, in conjunction
  with the date from keydate, if keyjd, which is assumed to be the midtime
  of the observation, is not present.
  If savebcv is yes, the barycentric velocity correction is written to the
  image header.  If specnum is 0, the BCV keyword is used; otherwise,
  APVELn is used, with the barycentric velocity correction in the 4th
  field: 0.0 0.0 _ bcv .  No matter what specnum is set to, the midtime
  UT is written to UTMID, and the Julian Date and Heliocentric Julian
  Date are written to GJDN and HJDN respectively, but only to
  those keywords which are not already filled.  The barycentric velocity
  correction is added to the observed redshift of a spectrum to get a
  velocity relative to the solar system barycenter so that a set of
  radial velocities over time have a constant reference point.
   
  </section>
  <section id="s_example">
  <h3>Example</h3>
  To compute a spectrum's barycentric velocity correction, reading everything
  from the spectrum's header:
  <div class="highlight-default-notranslate"><pre>
  RA      = ' 11:04:31.90'       /RIGHT ASCENSION SET BY COMMENT FILE
  DEC     = '-21:07:35.0'        /DECLINATION SET BY COMMENT FILE
  EPOCH   =               2000.0 /SET BY COMMENT FILE
  DATE-OBS= '28/01/100'           /UT DD/MM/YY AT END OF EXPOSURE
  UT      = '08:00:28'           /UT HH:MM:SS AT END OF EXPOSURE
  UTOPEN  = '07:42:26'           /UT HH:MM:SS AT BEGINNING OF EXPOSURE
  EXPTIME =              1081.01 /INTEGRATION TIME, SECONDS
  HJDN    =        2451571.83082 /HELIOCENTRIC JULIAN DAY AT MIDDLE OF EXPOSURE
  SITENAME= 'oro     '
  SITELONG= '+71:33:33.0'        /LONGITUDE, DEGREES WEST OF ZERO
  SITELAT = '+42:30:13.0'        /LATITUDE, DEGREES
  SITEELEV=                137.0 /ELEVATION, METERS
  </pre></div>
  Note that the RVSAO package recognizes nonstandard FITS dates, such as
  this one, which really should be '2000-01-28'.
  <div class="highlight-default-notranslate"><pre>
  rv&gt; bcvcorr spectrum
  0104.H096050.fits: 4096 x 2 x 1 2-D image
  UT start: 7:42:26.0, mid: 7:51:26.5, end: INDEF, exp: 1081
  2000-Jan-28 7:51:26.5 UT
  RA: 11:04:31.9, Dec: -21:07:35.0  2000.0
  28/01/100 lat 42:30:13.0 , long 71:33:33.0, alt 137.0
  Julian date is 2451571.82739 at 2000-Jan-28 7:51:26.5 UT
  Object at ra 11:04:31.900 dec -21:07:35.00 eq 2000
  Heliocentric Julian date: 2451571.83081
  gbcvel = 20.6503  ghcvel = 20.6598  geovel = -0.0394
  bcv = 20.6109  hcv = 20.6204 computed
  bcv = INDEF  hcv = INDEF from file
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  On-line help is available on the World Wide Web at
  http://tdc-www.harvard.edu/iraf/rvsao/bcvcorr
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLE' 'SEE ALSO'  -->
  

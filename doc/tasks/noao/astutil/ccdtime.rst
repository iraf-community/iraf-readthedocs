.. _ccdtime:

ccdtime: Compute time, magnitude, and signal-to-noise for CCDs
==============================================================

**Package: astutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ccdtime
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_time">
  <dt><b>time = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='time' Line='time = INDEF' -->
  <dd>Time in seconds for output of magnitude at the specified signal-to-noise and
  signal-to-noise at the specified magnitude.  This time applies to all
  filters.  If specified as INDEF then no output at fixed exposure time will
  be produced.  If the value is not greater than zero or less than 100000
  an error is reported.
  </dd>
  </dl>
  <dl id="l_magnitude">
  <dt><b>magnitude = 20.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='magnitude' Line='magnitude = 20.' -->
  <dd>Magnitude for output of time at the specified signal-to-noise and
  signal-to-noise at the specified time.  This magnitude applies to all
  filters. If specified as INDEF then no output at fixed magnitude will
  be produced.  If the absolute value of the magnitude is greater than 40
  an error will be reported.
  </dd>
  </dl>
  <dl id="l_snr">
  <dt><b>snr = 20.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='snr' Line='snr = 20.' -->
  <dd>Signal-to-noise ratio for output of time at the specified magnitude and
  magnitude at the specified time.  This signal-to-noise ratio applies to all
  filters. If specified as INDEF then no output at fixed signal-to-noise
  ratio will be produced.  If the value is not greater than zero or less than
  100000 an error is reported.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"ccdtime$kpno.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "ccdtime$kpno.dat"' -->
  <dd>Database file for telescope, filter, and detector information.  The format
  of this file is described elsewhere.  This file is typically a standard
  file from the logical directory <span style="font-family: monospace;">"ccdtime$"</span> or a personal copy in a
  user's directory.
  </dd>
  </dl>
  <dl id="l_telescope">
  <dt><b>telescope = <span style="font-family: monospace;">"?"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='telescope' Line='telescope = "?"' -->
  <dd>Telescope entry from the database.  If <span style="font-family: monospace;">"?"</span> a list of telescopes in the
  database is produced.  The name must match the entry name in the database
  but ignoring case.  If the same telescope has multiple focal ratios then
  there must be multiple entries in the database.
  </dd>
  </dl>
  <dl id="l_detector">
  <dt><b>detector = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='detector' Line='detector = ""' -->
  <dd>Detector entry from the database.  If <span style="font-family: monospace;">"?"</span> a list of detectors in the
  database is produced.  The name must match the entry name in the database
  but ignoring case.
  </dd>
  </dl>
  <dl id="l_sum">
  <dt><b>sum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sum' Line='sum = 1' -->
  <dd>CCD on-chip summing or binning factor.
  </dd>
  </dl>
  <dl id="l_seeing">
  <dt><b>seeing = 1.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='seeing' Line='seeing = 1.5' -->
  <dd>Expected seeing (FWHM) in arc seconds.  The number of pixels used for computing
  the total star counts and the signal-to-noise is given by 1.4 times the square
  of the seeing converted to pixels and rounded up.
  </dd>
  </dl>
  <dl id="l_airmass">
  <dt><b>airmass = 1.2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='airmass' Line='airmass = 1.2' -->
  <dd>Airmass for observation.
  </dd>
  </dl>
  <dl id="l_phase">
  <dt><b>phase = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='phase' Line='phase = 0.' -->
  <dd>Moon phase in days (0-28) for the estimation of sky brightness.  A
  phase of zero is new moon or dark sky conditions and a phase of 14
  is full moon.
  </dd>
  </dl>
  <dl id="l_f1">
  <dt><b>f1 = <span style="font-family: monospace;">"U"</span>, f2 = <span style="font-family: monospace;">"B"</span>, f3 = <span style="font-family: monospace;">"V"</span>, f4 = <span style="font-family: monospace;">"R"</span>, f5 = <span style="font-family: monospace;">"I"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='f1' Line='f1 = "U", f2 = "B", f3 = "V", f4 = "R", f5 = "I"' -->
  <dd>Filters for which to compute the CCD information.  If given as <span style="font-family: monospace;">"?"</span>
  a list of filters in the database is produced.  If the name (ignoring
  case) is not found then it is ignored.  A null name, that is <span style="font-family: monospace;">""</span>,
  is used to eliminate listing of a filter.  There may be many filters
  in the database but the task is currently limited to displaying no
  more than five.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A telescope, CCD detector, and list of filters is selected from a database
  to define the expected photon/electron count rates.  These rates along with
  a specified seeing and airmass are used to estimate the signal-to-noise
  ratio (SNR) for a stellar observation in each filter.  The output provides
  three results per filter; the exposure time to achieve a desired SNR for a
  given magnitude, the magnitude to achieve a desired SNR in a given time, and
  the SNR at a specified magnitude and exposure time.  With each of these,
  the number of star photons (or CCD electrons) in an area 1.4 times the
  square of the seeing, the number of sky photons per pixel, and the RMS noise
  contributions from photon noise in the star, the sky, and the detector
  noise from dark current and read out noise are given.  Note that least two
  of the time, magnitude, and signal-to-noise ratio must be specified but if
  one is INDEF then output with that quantity fixed will be skipped or, in
  other words, only the output where the quantity is computed is produced.
  </p>
  <p>
  The calibration information needed to define the count rates are
  taken from a database file.  This file may be standard ones given in
  the logical directory <span style="font-family: monospace;">"ccdtime$"</span> or the user may create their own.
  The database contains entries organized by telescope name (which may
  include a focal ratio if there are multiple ones), detector name,
  and filter name.  One of the standard files may be used as a template.
  </p>
  <p>
  The file is actually in free format with whitespace and comments ignored.
  However, following the template formatting makes it easy to see the logical
  structure.  All lines, except the <span style="font-family: monospace;">"end"</span> line which separates the different
  categories of entries, consist of a keyword an equal sign, and a value
  separated by whitespace.  An entry begins with one of the keywords
  <span style="font-family: monospace;">"telescope"</span>, <span style="font-family: monospace;">"detector"</span>, or <span style="font-family: monospace;">"filter"</span> and ends with the beginning of
  a new entry or the <span style="font-family: monospace;">"end"</span> separator.
  </p>
  <p>
  A keyword is one of the words shown in the example below.  These keywords
  can also be indexed by the name of a telescope, filter, and/or detector
  entry.  This allows having different transmissions in different filters
  due to correctors, different scales for different detectors which may
  have fore-optics, etc.
  </p>
  <p>
  Specifically a keyword in the telescope section may have arguments
  from the filter or detector entries, a keyword in the filter section may
  have arguments from the telescope and detector entries, and a keyword
  in the detector section may have arguments from the telescope and filter
  entries.  The formats are keyword, keyword(arg), and keyword(arg,arg).
  The arg fields must match an entry name exactly (without the quotes)
  and there can be no whitespace between the keyword and (, between (
  and the argument, between the arguments and the comma, and between the
  last argument and the closing ).  The software will first look for
  keywords with both arguments in either order, then for keywords with
  one argument, and then for keywords with no arguments.
  </p>
  <p>
  Below is an example of each type of entry:
  </p>
  <div class="highlight-default-notranslate"><pre>
  telescope = "0.9m"
          aperture = 0.91
          scale = 30.2
          transmission = 1.0
          transmission(U) = 0.8
          transmission(U,T1KA) = 0.7
  
  filter = "U"
          mag = 20
          star = 18.0
          extinction = 0.2
          sky0 = 22.0
          sky1 = -0.2666
          sky2 = -.00760
  
  detector = "T1KA"
          rdnoise = 3.5
          dark = 0.001
          pixsize = 24
          U = 0.36
          B = 0.61
          V = 0.71
          R = 0.78
          I = 0.60
  </pre></div>
  <p>
  In the example, a transmission of 0.7 will be used if the filter is U
  and the detector is T1KA, a value of 0.8 if the filter is U and the
  detector is not T1KA, and a value of 1 for all other cases.
  </p>
  <p>
  The telescope entry contains the aperture diameter in meters, the
  scale in arcsec/mm, and a transmission factor.  The transmission factor is
  mostly a fudge factor but may be useful if a telescope has various
  configurations with additional mirrors and optics.
  </p>
  <p>
  The filter entry contains a fiducial magnitude and the total photon count
  rate for a star of that magnitude.  The units are photons per second
  per square meter of aperture.  An effective extinction in magnitudes/airmass is
  given here.  The sky is defined by a quadratic
  function of lunar phase in days:
  </p>
  <div class="highlight-default-notranslate"><pre>
  if (phase &lt; 14)
      sky = sky0 + sky1 * phase + sky2 * phase**2
  else
      sky = sky0 + sky1 * (14 - phase) + sky2 * (14 - phase)**2
  </pre></div>
  <p>
  One may set the higher order terms to zero if the moon contribution
  is to be ignored.  The units are magnitudes per square arc second.
  </p>
  <p>
  The detector entry contains the read out noise in electrons, the
  dark current rate in electrons per second, the pixel size in
  microns, and the detective quantum efficiency (DQE); the fraction of
  detected photons converted to electrons.  Note that the actual
  values used are the DQE times the rates given by the filter entries.
  Thus, one may set the DQE values to 1 and adjust the filter values
  or set the star count rates to 1 in the filter and set the actual
  count rates in the DQE values.
  </p>
  <p>
  The computed quantities are formally given as follows.  The
  star count rates for the specified telescope/detector/filter are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  r(star) = star * aperture**2 * transmission *
      10**(0.4*(1-airmass)*extinction) * dqe
  </pre></div>
  <p>
  where the <span style="font-family: monospace;">"star"</span>, <span style="font-family: monospace;">"aperture"</span>, <span style="font-family: monospace;">"transmission"</span>, <span style="font-family: monospace;">"extinction"</span>, are those
  in the database and the <span style="font-family: monospace;">"dqe"</span> is the appropriate filter value.  The sky
  rate per pixel is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  r(sky) = r(star) * 10 ** (0.4 * (mag - sky)) * pixel**2
  pixel = pixsize * scale * sum
  </pre></div>
  <p>
  where mag is the fiducial magnitude, sky is the value computed using
  the quadratic formula for the specified moon phase and the database
  coefficients, the <span style="font-family: monospace;">"pixel"</span> size is computed using the CCD pixel size and
  the telescope scale from the database, and sum is the
  specified CCD binning factor.
  </p>
  <p>
  The number of pixels per star is computed from the seeing as:
  </p>
  <div class="highlight-default-notranslate"><pre>
  npix = 1.4 * (seeing / pixel) ** 2
  </pre></div>
  <p>
  where the number is rounded up to the next integer and a minimum of 9
  pixels is enforced.  This number is a compromise between a large aperture
  for high SNR stars and a smaller aperture for fainter stars.
  </p>
  <p>
  The number of star photons/electrons per star of magnitude m,
  the number of sky photons per pixel, and the number of dark current
  electrons, all in exposure time t, are given by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  nstar = r(star) * 10 ** (0.4 * (mag - m)) * t
  nsky = r(sky) * t
  ndark = dark * t
  </pre></div>
  <p>
  where dark is taken from the detector database entry.
  </p>
  <p>
  Finally the noise contributions, total noise, and signal-to-noise are
  given by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  noise star = nstar ** 1/2
  noise sky = (npix * nsky) ** 1/2
  noise ccd = (npix * (ndark + rdnoise**2)) ** 1/2
  noise total = (nstar+npix*(nsky+ndark+rdnoise**2)) ** 1/2
  SNR = nstar / noise total
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To get a list of the telescopes, filters, and detectors in a database:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdtime telescope=? detector=? f1=?
  Entries for telescope in database ccdtime$kpno.dat:
          0.9m
          ...
          4m
  Entries for detector in database ccdtime$kpno.dat:
          T1KA
          T2KA
          T2KB
          TI2
          TI3
          T5HA
          S2KA
  Entries for filter in database ccdtime$kpno.dat:
          U
          B
          V
          R
          I
  </pre></div>
  <p>
  2.  The following is for the default magnitude and SNR and with
  a 1 second exposure time specified.  The output has some
  whitespace removed to fit on this page.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdtime time=1
  Telescope: 0.9m
  Detector: t1ka
  Database: ccdtime$kpno.dat Telescope: 0.9m    Detector: t1ka
    Sum: 1 Arcsec/pixel: 0.72  Pixels/star: 6.0
    Seeing: 1.5  Airmass: 1.20  Phase: 0.0
  
   Filter  Time   Mag   SNR   Star Sky/pix Noise contributions
                                            Star    Sky    CCD
  
        U  70.2  20.0  10.0  196.6    8.8  14.02   8.90  10.53
        B  13.0  20.0  10.0  208.8   13.0  14.45  10.82  10.51
        V  13.2  20.0  10.0  250.7   29.8  15.83  16.37  10.51
        R  17.3  20.0  10.0  365.8   95.9  19.13  29.38  10.51
        I 126.4  20.0  10.0 1259.2 1609.8  35.49 120.37  10.55
  
        U   1.0  15.6  10.0  166.6    0.1  12.91   1.06  10.50
        B   1.0  17.4  10.0  170.0    1.0  13.04   3.00  10.50
        V   1.0  17.6  10.0  174.6    2.3  13.21   4.50  10.50
        R   1.0  17.6  10.0  186.0    5.5  13.64   7.06  10.50
        I   1.0  16.7  10.0  207.9   12.7  14.42  10.71  10.50
  
        U   1.0  20.0   0.3    2.8    0.1   1.67   1.06  10.50
        B   1.0  20.0   1.4   16.0    1.0   4.00   3.00  10.50
        V   1.0  20.0   1.6   19.0    2.3   4.36   4.50  10.50
        R   1.0  20.0   1.6   21.1    5.5   4.59   7.06  10.50
        I   1.0  20.0   0.7   10.0   12.7   3.16  10.71  10.50
  </pre></div>
  <p>
  Note that the default of 1 second in the last section
  gives the count rates per second for star and sky.
  </p>
  <p>
  3.  Sometimes one may want to vary one parameter easily on the command
  line or query.  This can be done by changing the parameter to query
  mode.  In the following example we want to change the magnitude.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdtime.magnitude.p_mode=query
  cl&gt; ccdtime.telescope="0.9m"
  cl&gt; ccdtime.detector="t1ka"
  cl&gt; ccdtime.f1=""; ccdtime.f5=""
  cl&gt; ccdtime
  Magnitude (20.):
  Database: ccdtime$kpno.dat   Telescope: 0.9m     Detector: t1ka
    Sum: 1 Arcsec/pixel: 0.72  Pixels/star: 6.0
    Seeing: 1.5  Airmass: 1.20  Phase: 0.0
  
   Filter  Time   Mag   SNR  Star Sky/pix  Noise contributions
                                             Star   Sky    CCD
  
        B  13.0  20.0  10.0 208.8    13.0  14.45  10.82  10.51
        V  13.2  20.0  10.0 250.7    29.8  15.83  16.37  10.51
        R  17.3  20.0  10.0 365.8    95.9  19.13  29.38  10.51
  
  cl&gt; ccdtime 21
  ...
  cl&gt; ccdtime 22
  ...
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_CCDTIME">
  <dt><b>CCDTIME V2.11.4</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='CCDTIME' Line='CCDTIME V2.11.4' -->
  <dd>A error will be reported if the requested time or SNR is not greater
  than zero and less than 100000., or if the absolute value
  of the magnitude is greater than 40.
  </dd>
  </dl>
  <dl id="l_CCDTIME">
  <dt><b>CCDTIME V2.11.2</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='CCDTIME' Line='CCDTIME V2.11.2' -->
  <dd>The incorrect usage of a 1 mag/airmass extinction was fixed by adding an
  expected <span style="font-family: monospace;">"extinction"</span> entry in the filter entries.  Note that old files
  will still give the same result by using an extinction of 1 if the keyword
  is not found.
  The database keywords can not be indexed by telescope, filter, and/or
  detector.
  The number of pixels per aperture now has a minimum of 9 pixels.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

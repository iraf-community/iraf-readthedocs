.. _setairmass:

setairmass: Compute effective airmass and middle UT for an exposure
===================================================================

**Package: echelle**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  setairmass images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>The list of images for which to calculate the airmass.  The image headers may
  optionally be updated with the airmass and the mid-UT of the exposure.
  </dd>
  </dl>
  <dl id="l_observatory">
  <dt><b>observatory = <span style="font-family: monospace;">")_.observatory"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observatory' Line='observatory = ")_.observatory"' -->
  <dd>Observatory for which airmasses are to be computed if the observatory is not
  specified in the image header by the keyword OBSERVAT. The default is a
  redirection to look in the parameters for the parent package for a value. The
  observatory may be one of the observatories in the observatory database,
  <span style="font-family: monospace;">"observatory"</span> to select the observatory defined by the environment variable
  <span style="font-family: monospace;">"observatory"</span> or the parameter <b>observatory.observatory</b>, or <span style="font-family: monospace;">"obspars"</span> to
  select the current parameters set in the <b>observatory</b> task. See help for
  <b>observatory</b> for additional information. If the input consists of images
  then the observatory is defined by the OBSERVAT keyword if present.
  </dd>
  </dl>
  <dl id="l_intype">
  <dt><b>intype = <span style="font-family: monospace;">"beginning"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intype' Line='intype = "beginning"' -->
  <dd>The time stamp of the observation as recorded at the telescope for the time
  dependent header keywords.  The choices are the <span style="font-family: monospace;">"beginning"</span>, <span style="font-family: monospace;">"middle"</span> or <span style="font-family: monospace;">"end"</span>
  of the observation.
  </dd>
  </dl>
  <dl id="l_outtype">
  <dt><b>outtype = <span style="font-family: monospace;">"effective"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtype' Line='outtype = "effective"' -->
  <dd>The output time stamp desired for the airmass. The choices are the <span style="font-family: monospace;">"effective"</span>
  airmass, or the airmass at the <span style="font-family: monospace;">"beginning"</span>, <span style="font-family: monospace;">"middle"</span> or <span style="font-family: monospace;">"end"</span> of the
  observation.
  </dd>
  </dl>
  <dl id="l_ra">
  <dt><b>ra = <span style="font-family: monospace;">"ra"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ra' Line='ra = "ra"' -->
  <dd>The name of the keyword that contains the right ascension. The right ascension
  is assumed to be in hours unless ra is one of the standard CRVALn keywords in
  which case it is assumed to be in degrees.
  </dd>
  </dl>
  <dl id="l_dec">
  <dt><b>dec = <span style="font-family: monospace;">"dec"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dec' Line='dec = "dec"' -->
  <dd>The name of the keyword that contains the declination in degrees.
  </dd>
  </dl>
  <dl id="l_equinox">
  <dt><b>equinox = <span style="font-family: monospace;">"epoch"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='equinox' Line='equinox = "epoch"' -->
  <dd>The name of the keyword that contains the equinox of the right ascension and
  declination coordinates in years.
  </dd>
  </dl>
  <dl id="l_st">
  <dt><b>st = <span style="font-family: monospace;">"st"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='st' Line='st = "st"' -->
  <dd>The name of the keyword containing the sidereal time in hours. 
  </dd>
  </dl>
  <dl id="l_ut">
  <dt><b>ut = <span style="font-family: monospace;">"ut"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ut' Line='ut = "ut"' -->
  <dd>The name of the keyword containing the ut time.  This keyword can either
  be in date plus time format or in hours.  Note that this allows setting
  both the <span style="font-family: monospace;">"date-obs"</span> and <span style="font-family: monospace;">"ut"</span>.  If no time is found then
  a time of 0hrs is used.
  </dd>
  </dl>
  <dl id="l_date">
  <dt><b>date = <span style="font-family: monospace;">"date-obs"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='date' Line='date = "date-obs"' -->
  <dd>The name of the keyword that contains the UT date of the observation. The
  format should be `DD/MM/YY' (old FITS format), YYYY-MM-DD (new FITS format),
  or YYYY-MM-DDTHH:MM:SS (new FITS format with time).  If there is a time
  and no time is found in the ut keyword then it is used for the ut.
  </dd>
  </dl>
  <dl id="l_exposure">
  <dt><b>exposure = <span style="font-family: monospace;">"exptime"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exposure' Line='exposure = "exptime"' -->
  <dd>The name of the keyword that contains the exposure time (in seconds) of the
  image.
  </dd>
  </dl>
  <dl id="l_airmass">
  <dt><b>airmass = <span style="font-family: monospace;">"airmass"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='airmass' Line='airmass = "airmass"' -->
  <dd>The name of the output keyword that will receive the computed airmass.
  </dd>
  </dl>
  <dl id="l_utmiddle">
  <dt><b>utmiddle = <span style="font-family: monospace;">"utmiddle"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='utmiddle' Line='utmiddle = "utmiddle"' -->
  <dd>The name of the output keyword that will receive the universal time for
  the middle of the observation.  The format of the keyword will be the same
  as that specifying the universal time.
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = 750.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = 750.0' -->
  <dd>The atmospheric scale height.
  </dd>
  </dl>
  <dl id="l_show">
  <dt><b>show = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='show' Line='show = yes' -->
  <dd>Print the airmasses and mid-UT's for each image?
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = yes' -->
  <dd>Update the image headers with the airmasses and the mid-UT's?
  </dd>
  </dl>
  <dl id="l_override">
  <dt><b>override = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='override' Line='override = yes' -->
  <dd>If updating the image headers, override values that were previously recorded ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  SETAIRMASS will calculate the effective airmass of an astronomical image, as
  described below under <span style="font-family: monospace;">"ALGORITHMS"</span>.  The task requires the instantaneous
  zenith distance at the beginning, middle and end of the exposure. These are
  calculated using the right ascension, declination, and equinox as well as the
  sidereal time, exposure time, UT date, and observatory from the image header.
  If the observatory is not available in the image header under the keyword
  OBSERVAT, the observatory is defined by the <i>observatory</i> parameter. See
  help for <i>observatory</i> for further information.
  </p>
  <p>
  The right ascension and declination will be precessed from the given equinox to
  the date of observation. The name of the right ascension, declination, equinox,
  sidereal time, ut time, exposure time, and date keywords can be specified as
  parameters. These keywords should express the right ascension in hours,
  the declination in degrees, the equinox in years, the sidereal time in hours,
  the universal time in hours, the exposure time in seconds, and the date in
  FITS format. If any of the required keywords are missing from the image
  headers, they can be added using the hedit or asthedit tasks.  Note that
  the universal time keyword may be in either a date plus time format or
  in hours and any output middle universal time will be in the same format.
  </p>
  <p>
  Before using this task, you will need to know the <span style="font-family: monospace;">"time stamp"</span> of the time
  varying header quantities (e.g. sidereal time).  Do the recorded values
  represent the beginning, the middle or the end of the exposure ? This should
  be set in the <b>intype</b> parameter.
  </p>
  <p>
  If for some reason the effective airmass is not desired, the value of the
  airmass at the beginning, middle or end of the exposure can be recorded in the
  header keyword specified by the <i>airmass</i> parameter. The <b>show</b>
  parameter can be used to control the output to the terminal. The <b>update</b>
  and <b>override</b> parameters control the header keyword output.
  </p>
  <p>
  SETAIRMASS will also calculate the universal time of the middle of the exposure
  and place the value in the header keyword specified by the <i>utmiddle</i>
  parameter.  This assumes that the value for the UT is in the date keyword
  or ut keyword, with the same time stamp as the sidereal time. The
  mid-observation UT is useful for interpolating calibration arc dispersion
  solutions using REFSPECTRA, especially when the exposure time is
  long.
  </p>
  </section>
  <section id="s_algorithms">
  <h3>Algorithms</h3>
  <p>
  The mean airmass is calculated uses the formula described in <span style="font-family: monospace;">"Some
  Factors Affecting the Accuracy of Stellar Photometry with CCDs"</span> by P.
  Stetson, DAO preprint, September 1988.  This simple formula is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  AM (eff) = [AM (beginning) + 4*AM (middle) + AM (end)] / 6
  </pre></div>
  <p>
  and is derived by using Simpson's 1/3 rule to approximate the integral
  that represents the mean airmass.
  </p>
  <p>
  The beginning, middle and end airmasses are calculated using the
  relation between airmass and elevation (or zenith distance) in John
  Ball's book on Algorithms for the HP-45:
  </p>
  <div class="highlight-default-notranslate"><pre>
  AM = sqrt (x**2 + 2*scale + 1) - x, where
  
   x = scale * sin(elevation) = scale * cos(ZD)
  </pre></div>
  <p>
  The atmospheric scaling parameter is <i>scale</i> (see <span style="font-family: monospace;">"Astrophysical
  Quantities"</span> by Allen, 1973 p.125,133).
  </p>
  </section>
  <section id="s_keywords">
  <h3>Keywords</h3>
  <p>
  The input keywords are:
  </p>
  <dl id="l_OBSERVAT">
  <dt><b>OBSERVAT</b></dt>
  <!-- Sec='KEYWORDS' Level=0 Label='OBSERVAT' Line='OBSERVAT' -->
  <dd>Observatory at which the data was taken.  If absent the observatory is
  determined using the <i>observatory</i> parameter.
  </dd>
  </dl>
  <dl>
  <dt><b><i>ra</i></b></dt>
  <!-- Sec='KEYWORDS' Level=0 Label='' Line='\fIra\fR' -->
  <dd>Right ascension in hours at the beginning, middle, or end of the observation.
  If ra is one of the CRVALn keywords it is assumed to be in degrees.
  </dd>
  </dl>
  <dl>
  <dt><b><i>dec</i></b></dt>
  <!-- Sec='KEYWORDS' Level=0 Label='' Line='\fIdec\fR' -->
  <dd>Declination in degrees at the beginning, middle, or end of the observation.
  </dd>
  </dl>
  <dl>
  <dt><b><i>equinox</i></b></dt>
  <!-- Sec='KEYWORDS' Level=0 Label='' Line='\fIequinox\fR' -->
  <dd>The equinox of the coordinates.  The right ascension and declination will
  be precessed from this epoch to the date of the observation before being
  used.
  </dd>
  </dl>
  <dl>
  <dt><b><i>st</i></b></dt>
  <!-- Sec='KEYWORDS' Level=0 Label='' Line='\fIst\fR' -->
  <dd>Sidereal time in hours at the beginning, middle, or end of the observation.
  </dd>
  </dl>
  <dl>
  <dt><b><i>ut</i></b></dt>
  <!-- Sec='KEYWORDS' Level=0 Label='' Line='\fIut\fR' -->
  <dd>Universal time in hours at the beginning, middle, or end of the observation.
  This may be in either date plus time format or just in hours.  
  </dd>
  </dl>
  <dl>
  <dt><b><i>date</i></b></dt>
  <!-- Sec='KEYWORDS' Level=0 Label='' Line='\fIdate\fR' -->
  <dd>The value of the date parameter is the keyword name to be used for the date of
  the observation.  The date must be in either the old or new FITS format.
  </dd>
  </dl>
  <dl>
  <dt><b><i>exposure</i></b></dt>
  <!-- Sec='KEYWORDS' Level=0 Label='' Line='\fIexposure\fR' -->
  <dd>The value of the exposure parameter is the keyword name to be used for the
  exposure time in seconds.
  </dd>
  </dl>
  <p>
  The output keywords are:
  </p>
  <dl>
  <dt><b><i>airmass</i></b></dt>
  <!-- Sec='KEYWORDS' Level=0 Label='' Line='\fIairmass\fR' -->
  <dd>The value of the airmass parameter is the keyword name to be used for
  the computed airmass at either the beginning, middle, or end of the
  exposure, or for the weighted effective value over the exposure.
  </dd>
  </dl>
  <dl>
  <dt><b><i>utmiddle</i></b></dt>
  <!-- Sec='KEYWORDS' Level=0 Label='' Line='\fIutmiddle\fR' -->
  <dd>The value of the utmiddle parameter is the keyword name to be used for
  the universal time at the middle of the exposure.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Calculate the effective airmass of the IRAF test picture, dev$pix.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; setairmass dev$pix exposure=itime update-
  </pre></div>
  <p>
  Note that the test picture does not have the correct coordinate epoch
  listed in its header, so no precession will be performed. 
  </p>
  <p>
  2. Calculate the effective airmass of the IRAF test picture dev$ypix in two
  ways.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; setairmass dev$ypix exposure=itime update-
  
  cl&gt; setairmass dev$ypix ra=crval1 dec=crval2 equinox=equinox \
      exposure=itime update-
  </pre></div>
  <p>
  Note the first way gives the same results as example 1. The second way
  uses the J2000 equatorial system rather then the ra and dec at the time
  of observation.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_SETAIRMASS">
  <dt><b>SETAIRMASS V2.11.4</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SETAIRMASS' Line='SETAIRMASS V2.11.4' -->
  <dd>The ut keyword now has precedence over any time in the date keyword
  and it can be either date plus time or hours.
  </dd>
  </dl>
  <dl id="l_SETAIRMASS">
  <dt><b>SETAIRMASS V2.11.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SETAIRMASS' Line='SETAIRMASS V2.11.3' -->
  <dd>The right ascension, declination, equinox, st, and ut keywords were made 
  parameters rather than being hard wired.
  </dd>
  </dl>
  <dl id="l_SETAIRMASS">
  <dt><b>SETAIRMASS V2.11.2</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SETAIRMASS' Line='SETAIRMASS V2.11.2' -->
  <dd>Y2K update: This task was updated to use the new FITS date format.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  airmass, hedit, refspectra, observatory
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'ALGORITHMS' 'KEYWORDS' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

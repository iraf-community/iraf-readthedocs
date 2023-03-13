.. _datapars:

datapars: Edit the image data dependent parameters
==================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  datapars
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_scale">
  <dt><b>scale = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = 1.0' -->
  <dd>The scale of the image in user units, e.g. arcseconds per pixel.  All DAOPHOT
  distance dependent parameters are assumed to be in units of scale. If
  <i>scale</i> = 1.0 these parameters are assumed to be in units of pixels. Most
  DAOPHOT users should leave <i>scale</i> set to 1.0 unless they intend to compare
  their aperture photometry results directly with data in the literature.
  </dd>
  </dl>
  <dl id="l_fwhmpsf">
  <dt><b>fwhmpsf = 2.5 (scale units)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fwhmpsf' Line='fwhmpsf = 2.5 (scale units)' -->
  <dd>The full-width half-maximum of the point spread function in scale units.
  The DAOFIND task and the PHOT task  <span style="font-family: monospace;">"gauss"</span> and <span style="font-family: monospace;">"ofilter"</span> centering algorithms
  depend on the value of fwhmpsf. DAOPHOT users can either determine a value
  for fwhmpsf using an external task such as IMEXAMINE, or make use of the
  interactive capabilities of the DAOPHOT tasks to set and store it.
  </dd>
  </dl>
  <dl id="l_emission">
  <dt><b>emission = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='emission' Line='emission = yes' -->
  <dd>The features to be measured are above sky. By default the DAOPHOT package
  considers all features to be emission features. DAOPHOT users should
  leave this parameter set to <span style="font-family: monospace;">"yes"</span>. 
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma' Line='sigma = 0.0' -->
  <dd>The standard deviation of the sky pixels.  The DAOFIND task and the PHOT task
  <span style="font-family: monospace;">"constant"</span> sky fitting algorithm error estimate depend on the value of sigma. 
  DAOPHOT users should set sigma to a value representative of the noise in
  the sky background.
  </dd>
  </dl>
  <dl id="l_datamin">
  <dt><b>datamin = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datamin' Line='datamin = INDEF' -->
  <dd>The minimum good pixel value. Datamin defaults to -MAX_REAL the minimum
  floating point number supported by the host computer. Datamin is used
  to detect and remove bad data from the sky aperture, detect and flag
  bad data in the aperture photometry aperture, and detect and remove  bad
  data from the PSF fitting aperture.  DAOPHOT users should either leave
  datamin set to INDEF or set it to a number between 5-7 sigma below the
  sky background value.
  </dd>
  </dl>
  <dl id="l_datamax">
  <dt><b>datamax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datamax' Line='datamax = INDEF' -->
  <dd>The maximum good pixel value. Datamax defaults to MAX_REAL the maximum
  floating point number supported by the host computer.  Datamax is used
  to detect and remove bad data from the sky aperture, detect and flag
  bad data in the aperture photometry aperture, and detect and remove  bad
  data from the PSF fitting aperture.  DAOPHOT users should either leave
  datamax set to INDEF or set it to the linearity or saturation
  limit of the detector.
  </dd>
  </dl>
  <dl id="l_noise">
  <dt><b>noise = <span style="font-family: monospace;">"poisson"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='noise' Line='noise = "poisson"' -->
  <dd>The noise model used to estimate the uncertainties in the computed
  magnitudes. DAOPHOT users must leave noise set to <span style="font-family: monospace;">"poisson"</span>.
  </dd>
  </dl>
  <dl id="l_ccdread">
  <dt><b>ccdread = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdread' Line='ccdread = ""' -->
  <dd>The image header keyword defining the readout noise parameter whose units
  are assumed to be electrons.
  </dd>
  </dl>
  <dl id="l_gain">
  <dt><b>gain = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gain' Line='gain = ""' -->
  <dd>The image header keyword defining the gain parameter whose units are assumed to
  be electrons per adu.
  </dd>
  </dl>
  <dl id="l_readnoise">
  <dt><b>readnoise = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='readnoise' Line='readnoise = 0.0' -->
  <dd>The readout noise of the detector in electrons. DAOPHOT users should set
  readnoise or ccdread to its correct value before running any of the DAOPHOT
  package tasks in order to ensure that the PSF fitting weights, magnitude
  error estimates, and chi values are correct.
  </dd>
  </dl>
  <dl id="l_epadu">
  <dt><b>epadu = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='epadu' Line='epadu = 1.0' -->
  <dd>The gain of the detector in electrons per adu. DAOPHOT users should set this
  epadu or gain to its correct value before running any of the DAOPHOT package
  tasks in order to ensure that the PSF fitting weights, magnitude error 
  estimates, and chi values are correct.
  </dd>
  </dl>
  <dl id="l_exposure">
  <dt><b>exposure = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exposure' Line='exposure = ""' -->
  <dd>The image header exposure time keyword. The time units are arbitrary but
  must be consistent for any list of images whose magnitudes are to be compared.
  The computed magnitudes are normalized to  one timeunit by the PHOT task.
  As the magnitude scale of the DAOPHOT package is set by the PHOT task,
  setting exposure can save DAOPHOT users a lot of unnecessary zero point
  corrections in future analysis and calibration steps.
  </dd>
  </dl>
  <dl id="l_airmass">
  <dt><b>airmass = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='airmass' Line='airmass = ""' -->
  <dd>The image header airmass keyword.  The airmass parameter is not used
  directly by DAOPHOT but the airmass value is stored in the output file
  and its presence there will simplify future calibration steps.
  </dd>
  </dl>
  <dl id="l_filter">
  <dt><b>filter = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filter' Line='filter = ""' -->
  <dd>The image header filter id keyword.  The filter parameter is not used
  directly by DAOPHOT but the filter id is stored in the output file
  and its presence there will simplify future calibration steps.
  </dd>
  </dl>
  <dl id="l_obstime">
  <dt><b>obstime = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obstime' Line='obstime = ""' -->
  <dd>The image header time of observation keyword. The obstime parameter is not used
  directly by DAOPHOT but the obstime value is stored in the output file
  and its presence there will simplify future calibration steps.
  </dd>
  </dl>
  <dl id="l_itime">
  <dt><b>itime = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='itime' Line='itime = 1.0' -->
  <dd>The exposure time for the image in arbitrary units. The DAOPHOT magnitudes are
  normalized to 1 timeunit by the PHOT task using the value of exposure in the
  image header if exposure is defined or the value of itime.
  </dd>
  </dl>
  <dl id="l_xairmass">
  <dt><b>xairmass = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xairmass' Line='xairmass = INDEF' -->
  <dd>The airmass value.  The airmass is read from the image header if airmass
  is defined  or from xairmass. The airmass value is stored in the DAOPHOT
  output files.
  </dd>
  </dl>
  <dl id="l_ifilter">
  <dt><b>ifilter = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ifilter' Line='ifilter = "INDEF"' -->
  <dd>The filter id string. The filter id is read from the image header if filter
  is defined otherwise from ifilter. The filter id is stored in the DAOPHOT
  output files.
  </dd>
  </dl>
  <dl id="l_otime">
  <dt><b>otime = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='otime' Line='otime = "INDEF"' -->
  <dd>The value of the time of observation. The time of observation is read from
  the image header if obstime is defined otherwise from otime. The time of
  observation is stored in the DAOPHOT output files.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Datapars</i> sets the image data dependent parameters. These parameters are
  functions, of the instrument optics, the noise characteristics and range of
  linearity of the detector, and the observing conditions. Many of the
  centering, sky fitting, and photometry algorithm parameters in the CENTERPARS,
  FITSKYPARS, PHOTPARS, and DAOPARS  parameter sets scale with the data dependent
  parameters.
  </p>
  <p>
  The parameter <i>scale</i> sets the scale of the apertures used by the
  centering, sky fitting, aperture photometry, and psf fitting  algorithms.
  Scale converts radial distance measurements in pixels to radial distance
  measurements in scale units. The DAOPHOT parameters cbox, maxshift, rclean
  and rclip in the CENTERPARS parameter set; annulus, dannulus, and rgrow in
  FITSKYPARS parameter set; apertures in the PHOTPARS parameter set; and psfrad,
  fitrad, sannulus, wsannulus, and matchrad in the DAOPARS parameter set are
  expressed in units of the scale. The scale parameter is useful in  cases where
  the observations are to be compared to published aperture photometry
  measurements in the literature.
  </p>
  <p>
  The parameter <i>fwhmpsf</i> defines the full-width at half-maximum of the
  stellar point spread function. The DAOFIND task, the PHOT task centering
  algorithms <span style="font-family: monospace;">"gauss"</span> and <span style="font-family: monospace;">"ofilt"</span>, and the PSF modeling task PSF all require
  an accurate estimate for this parameter.
  </p>
  <p>
  By setting the <i>scale</i> and <i>fwhmpsf</i> appropriately the aperture
  sizes and radial distances may be  expressed in terms of the half-width
  at half-maximum of the stellar point spread function.  The way to do this
  is to define the scale parameter in units of the number of half-width at
  half-maximum per pixel, set the fwhmpsf parameter to 2.0, and then
  set the remaining scale dependent centering, sky fitting, aperture photometry,
  and psf fitting algorithm parameters in CENTERPARS, FITSKYPARS, PHOTPARS,
  and DAOPARS to appropriate values in units of the half-width at half-maximum
  of the point-spread function. Once an optimum set of algorithm parameters is
  chosen, the user need only alter the DATAPARS scale parameter before
  executing a DAOPHOT task on a new image.
  </p>
  <p>
  If <i>emission</i> is <span style="font-family: monospace;">"yes"</span>, the features to be measured are assumed to
  be above sky. By default the DAOPHOT package considers all features to be
  emission features. DAOPHOT users should leave this parameter set to <span style="font-family: monospace;">"yes"</span>.
  Although the DAOFIND and PHOT tasks can detect and measure absorption features
  the PSF fitting tasks currently cannot.
  </p>
  <p>
  The parameter <i>sigma</i> estimates the standard deviation of the sky
  background pixels. The star finding algorithm in DAOFIND uses sigma
  and the <i>findpars.threshold</i> parameter to define the stellar
  detection threshold in adu. The PHOT task centering algorithms use sigma,
  1) with the <i>centerpars.kclean</i> parameter to define deviant pixels
  if <i>centerpars.clean</i> is enabled; 2) to estimate the signal to
  noise ratio in the centering box; 3) and with the <i>centerpars.cthreshold</i>
  parameter to define a lower intensity limit for the pixels to be used
  for centering.  If sigma is undefined or &lt;= 0.0 1) no cleaning is performed
  regardless of the value of centerpars.clean; 2) the background noise in the
  centering box is assumed to be 0.0; and 3) default cutoff intensity is used
  for centering.
  </p>
  <p>
  The <i>datamin</i> and <i>datamax</i> parameters define the good data range.
  If datamin or datamax are defined bad data is removed from the sky pixel
  distribution before the sky is fit, data containing bad pixels in the
  photometry apertures is flagged and the corresponding aperture photometry
  magnitudes are set to INDEF, and bad data removed from the PSF fitting
  aperture. DAOPHOT users should set datamin and datamax to appropriate values
  before running the DAOPHOT tasks.
  </p>
  <p>
  DAOPHOT users must leave <i>noise</i> set to <span style="font-family: monospace;">"poisson"</span>.  This model includes
  Poisson noise from the object and both Poisson and readout noise in the sky
  background.
  </p>
  <p>
  The parameters <i>gain</i> and <i>epadu</i> define the image gain.
  The gain parameter specifies which keyword in the image header contains
  the gain value. If gain is undefined or not present in the image header
  the value of epadu is used.  Epadu must be in units of electrons per adu.
  DAOPHOT users should set either gain or epadu to a correct value before
  running any of the DAOPHOT package tasks to ensure that the aperture
  photometry magnitude error estimates, and the PSF fitting weights, chis, and
  magnitude error estimates are computed correctly.
  </p>
  <p>
  The two parameters <i>ccdread</i> and <i>readnoise</i> define the image
  readout noise.  The ccdread parameter specifies which keyword in the
  image header contains the readout noise value. If ccdread is undefined or
  not present in the image header the value of readnoise is used.
  Readnoise is assumed to be in units of electrons.
  DAOPHOT users should set either ccdread or readnoise before running any
  DAOPHOT tasks to insure that the PSF fitting weights, chis, and magnitude
  error estimates are computed correctly.
  </p>
  <p>
  The magnitudes computed by PHOT are normalized to an exposure time of 1 
  timeunit using the value of the exposure time in the image header parameter 
  <i>exposure</i> or <i>itime</i>. If exposure is undefined or not present
  in the image header a warning message is issued and the value of itime
  is used. The itime units are arbitrary but must be consistent for images
  analyzed together. As the magnitude scale in DAOPHOT is determined by the
  PHOT task setting either exposure or itime can save DAOPHOT users a lot
  of unnecessary zero point corrections in future analysis and calibration
  steps.
  </p>
  <p>
  The parameters <i>airmass</i> and <i>xairmass</i> define the airmass
  of the observation. The airmass parameter specifies which keyword in the
  image header contains the airmass value. If airmass is undefined or
  not present in the image header the value of xairmass is used.
  The airmass values are not used in any DAOPHOT computations, however their
  presence in the DAOPHOT output files will simplify future reduction steps.
  </p>
  <p>
  The parameters <i>filter</i> and <i>ifilter</i> define the filter
  of the observation. The filter parameter specifies which keyword in the
  image header contains the filter id. If filter is undefined or not present
  in the image header the value of ifilter is used. The filter id values are
  not used in any DAOPHOT computations, however their presence in the DAOPHOT
  output files can will simplify future reduction steps.
  </p>
  <p>
  The parameters <i>obstime</i> and <i>otime</i> define the time
  of the observation (e.g. UT). The obstime parameter specifies which keyword
  in the image header contains the time stamp of the observation. If obstime is
  undefined or not present in the image header the value of otime is used.
  The time of observations values are not used in any DAOPHOT
  computations, however their presence in the DAOPHOT output files can
  greatly simplify future reduction steps.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the data dependent parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; lpar datapars
  </pre></div>
  <p>
  2. Edit the data dependent parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; datapars
  </pre></div>
  <p>
  3. Edit the data dependent parameters from within the PSF task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; epar psf
  
      ... edit a few parameters
  
      ... move to the datapars parameter and type :e
  
      ... edit the datapars parameters and type :wq
  
      ... finish editing the psf parameter and type :wq
  </pre></div>
  <p>
  4. Save the current DATAPARS parameter set in a text file datnite1.par.
  This can also be done from inside a higher level task as in the previous
  example.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; epar datapars
  
      ... edit a few parameters
  
      ... type ":w datnite1.par"  from within epar
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  epar,lpar,daofind,phot,pstselect,psf,group,peak,nstar,allstar,substar,addstar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _datapars:

datapars: Edit the data dependent parameters
============================================

**Package: irred**

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
  <dd>The scale of the image in user units, e.g arcseconds per pixel.
  All APPHOT distance dependent parameters are assumed to be in units of scale.
  If scale = 1.0 these parameters are assumed to be in units of pixels.
  Most APPHOT users should leave scale set to 1.0 unless they intend to
  compare their aperture photometry results directly with data 
  in the literature.
  </dd>
  </dl>
  <dl id="l_fwhmpsf">
  <dt><b>fwhmpsf = 2.5 (scale units)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fwhmpsf' Line='fwhmpsf = 2.5 (scale units)' -->
  <dd>The full-width at half-maximum of the point spread function in scale units.
  The DAOFIND, FITPSF and WPHOT tasks and the <span style="font-family: monospace;">"gauss"</span> and <span style="font-family: monospace;">"ofilter"</span> centering
  algorithms depend on the value of fwhmpsf. APPHOT users can either determine
  a value for fwhmpsf using an external task such as IMEXAMINE, or make use of
  the interactive capabilities of the APPHOT tasks to set and store it.
  </dd>
  </dl>
  <dl id="l_emission">
  <dt><b>emission = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='emission' Line='emission = yes' -->
  <dd>The features to be measured are above sky. By default the APPHOT package
  considers all features to be emission features. However all the package tasks
  measure absorption features if emission is set to no.
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma' Line='sigma = INDEF' -->
  <dd>The standard deviation of the sky pixels. The DAOFIND task and the <span style="font-family: monospace;">"constant"</span>
  sky fitting algorithm error estimate depend on the value of sigma. APPHOT
  users should set sigma to a value which is representative of the noise
  in the sky background.
  </dd>
  </dl>
  <dl id="l_datamin">
  <dt><b>datamin = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datamin' Line='datamin = INDEF' -->
  <dd>The minimum good pixel value. Datamin defaults to -MAX_REAL, the minimum
  floating point number supported by the host computer.  APPHOT users should
  set this parameter if they wish to remove bad data from the sky pixel
  distribution before the sky is fit or if they wish to flag stars with
  bad data in the centering and / or photometry apertures.
  </dd>
  </dl>
  <dl id="l_datamax">
  <dt><b>datamax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datamax' Line='datamax = INDEF' -->
  <dd>The maximum good pixel value. Datamax defaults to MAX_REAL the maximum
  floating point number supported by the host computer.
  APPHOT users should set this parameter if they wish to flag
  saturated stars or stars with bad data in the centering and / or
  photometry apertures.
  </dd>
  </dl>
  <dl id="l_noise">
  <dt><b>noise = <span style="font-family: monospace;">"poisson"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='noise' Line='noise = "poisson"' -->
  <dd>The noise model used to estimate the uncertainties in the computed APPHOT
  magnitudes. The options are the following:
  <dl>
  <dt><b>poisson</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='poisson' Line='poisson' -->
  <dd>Poisson statistics in the object and the sky background are used to estimate
  the error in the object measurement.  There are two components to the sky 
  noise measurement the sky noise in the object aperture and the mean error
  in the estimated sky value.
  </dd>
  </dl>
  <dl>
  <dt><b>constant</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='constant' Line='constant' -->
  <dd>The standard deviation of the sky background is used to estimate the
  error in the object measurement.  There are two components to the error
  estimate the sky noise in the object aperture and the mean error in the
  estimated sky value.
  </dd>
  </dl>
  Most APPHOT users should use the Poisson model appropriate for CCD detectors.
  APPHOT users should also be aware that one or other of the parameters
  gain or epadu must be set correctly in order to compute the magnitude
  errors correctly.
  </dd>
  </dl>
  <dl id="l_ccdread">
  <dt><b>ccdread = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdread' Line='ccdread = ""' -->
  <dd>The image header keyword defining the readout noise parameter whose units are
  assumed to be electrons.
  </dd>
  </dl>
  <dl id="l_gain">
  <dt><b>gain = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gain' Line='gain = ""' -->
  <dd>The image header keyword defining the gain parameter whose units are assumed
  to be electrons per adu.
  </dd>
  </dl>
  <dl id="l_readnoise">
  <dt><b>readnoise = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='readnoise' Line='readnoise = 0.0' -->
  <dd>The readout noise of the image in electrons.  APPHOT users should set this
  parameter or the ccdread parameter to its correct value before running any
  of the APPHOT tasks.
  </dd>
  </dl>
  <dl id="l_epadu">
  <dt><b>epadu = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='epadu' Line='epadu = 1.0' -->
  <dd>The gain in electrons per adu.  APPHOT users should set epadu or ain to its
  correct value before running any of the APPHOT tasks in order to insure that
  the magnitude error estimates are correct.
  </dd>
  </dl>
  <dl id="l_exposure">
  <dt><b>exposure = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exposure' Line='exposure = ""' -->
  <dd>The image header exposure time keyword. The time units are arbitrary but
  must be consistent for any list of images whose magnitudes are to be compared.
  The computed magnitudes are normalized to 1 timeunit.  Setting the exposure
  parameter will greatly simplify  future reduction steps. The value of exposure
  is recorded in the APPHOT output file.
  </dd>
  </dl>
  <dl id="l_airmass">
  <dt><b>airmass = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='airmass' Line='airmass = ""' -->
  <dd>The image header airmass keyword.  The airmass parameter is not used
  directly by APPHOT but the airmass value is stored in the output file
  and its presence there will simplify future calibration steps.
  </dd>
  </dl>
  <dl id="l_filter">
  <dt><b>filter = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filter' Line='filter = ""' -->
  <dd>The image header filter id keyword.  The filter parameter is not used
  directly by APPHOT but the filter id is stored in the output file
  and its presence there will simplify future calibration steps.
  </dd>
  </dl>
  <dl id="l_obstime">
  <dt><b>obstime = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obstime' Line='obstime = ""' -->
  <dd>The image header time of observation keyword. The obstime parameter is not used
  directly by APPHOT but the obstime value is stored in the output file
  and its presence there will simplify future calibration steps.
  </dd>
  </dl>
  <dl id="l_itime">
  <dt><b>itime = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='itime' Line='itime = 1.0' -->
  <dd>The exposure time for the image in arbitrary units. The APPHOT magnitudes are
  normalized to 1 timeunit  using the value of exposure in the image header
  if exposure is defined or the value of itime.
  </dd>
  </dl>
  <dl id="l_xairmass">
  <dt><b>xairmass = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xairmass' Line='xairmass = INDEF' -->
  <dd>The airmass value.  The airmass is read from the image header if airmass
  is defined  or from xairmass. The airmass value is stored in the APPHOT
  output files.
  </dd>
  </dl>
  <dl id="l_ifilter">
  <dt><b>ifilter = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ifilter' Line='ifilter = "INDEF"' -->
  <dd>The filter id string. The filter id is read from the image header if filter
  is defined otherwise from ifilter. The filter id is stored in the APPHOT
  output files.
  </dd>
  </dl>
  <dl id="l_otime">
  <dt><b>otime = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='otime' Line='otime = "INDEF"' -->
  <dd>The value of the time of observation. The time of observation is read from
  the image header if obstime is defined otherwise from otime. The time of
  observation is stored in the APPHOT output files.
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
  FITSKYPARS and PHOTPARS  parameter sets scale with the data dependent
  parameters.
  </p>
  <p>
  The parameter <i>scale</i> sets the scale of the apertures used by the
  centering, sky fitting and photometry algorithms.  Scale converts radial
  distance measurements in pixel units to radial distance measurements in
  scale units. The APPHOT parameters, cbox, maxshift, rclean and rclip
  in the CENTERPARS parameter set; annulus, dannulus, and rgrow in
  the FITSKYPARS parameter set; and apertures in the PHOTPARS
  parameter set are expressed in units of the scale. The scale parameter is
  useful in cases where the observations are to be compared to published
  aperture photometry measurements in the literature.
  </p>
  <p>
  The parameter <i>fwhmpsf</i> defines the full-width at half-maximum of the
  stellar point spread function.  Most APPHOT tasks and algorithms do not 
  require this parameter. The exceptions are the DAOFIND task, the centering
  algorithms <span style="font-family: monospace;">"gauss"</span> and <span style="font-family: monospace;">"ofilter"</span>, the FITPSF task, and the WPHOT task.
  </p>
  <p>
  By setting the <i>scale</i> and <i>fwhmpsf</i> appropriately the aperture
  sizes and radial distances may be  expressed in terms of the half-width
  at half-maximum of the stellar point spread function.  The way to do this
  is to define the scale parameter in units of the number of half-width at
  half-maximum per pixel, set the fwhmpsf parameter to 2.0, and then
  set the remaining scale dependent centering, sky fitting and photometry
  algorithm parameters in CENTERPARS, FITSKYPARS and PHOTPARS to
  appropriate values in units of the half-width at half-maximum of the
  point-spread function. Once an optimum set of algorithm parameters is
  chosen, the user need only alter the DATAPARS scale parameter before
  executing an APPHOT task on a new image.
  </p>
  <p>
  If  <i>emission</i> is <span style="font-family: monospace;">"yes"</span>, the features to be measured are assumed to be
  above sky. By default the APPHOT package considers all measurements to
  be measurements of emission features. In most cases APPHOT users should
  leave emission set to <span style="font-family: monospace;">"yes"</span>.
  </p>
  <p>
  The parameter <i>sigma</i> estimates the standard deviation of the sky
  background pixels. The star finding algorithm in DAOFIND uses sigma
  and the <i>findpars.threshold</i> parameter to define the stellar
  detection threshold in adu. The centering algorithms uses sigma,
  1) with the <i>centerpars.kclean</i> parameter to define deviant pixels
  if <i>centerpars.clean</i> is enabled; 2) to estimate the signal to
  noise ratio in the centering box; 3) and with the <i>centerpars.cthreshold</i>
  parameter to define the lower intensity limit for the pixels to be used
  for centering.  If sigma is undefined or &lt;= 0.0 1) no cleaning is performed
  regardless of the value of centerpars.clean; 2) the background
  noise in the centering box is assumed to be 0; and 3) default cutoff
  intensity intensity is used for centering. 
  </p>
  <p>
  The <i>datamin</i> and <i>datamax</i> parameters define the  good data range.
  If datamin or datamax are defined bad data is removed from the sky pixel
  distribution before the sky is fit, data containing bad pixels in the 
  photometry apertures is flagged, and the corresponding aperture photometry
  magnitudes are set to INDEF. APPHOT users should set datamin and datamax
  to appropriate values before running the APPHOT tasks.
  </p>
  <p>
  Two noise models are available <span style="font-family: monospace;">"constant"</span> and <span style="font-family: monospace;">"poisson"</span>. If <i>noise</i> =
  constant, the total noise is assumed to be due to noise in the sky background
  alone. If <i>noise</i> = poisson, the total noise includes Poisson noise from
  the object and the sky noise. 
  </p>
  <p>
  The parameters <i>gain</i> and <i>epadu</i> define the image gain.
  The gain parameter specifies which keyword in the image header contains
  the gain value. If gain is undefined or not present in the image header
  the value of epadu is used.  Epadu must be in units of electrons per adu.
  APPHOT users should set either gain or epadu before running any 
  APPHOT tasks to insure the magnitude error computations are correct.
  </p>
  <p>
  The two parameters <i>ccdread</i> and <i>readnoise</i> define the image
  readout noise.  The ccdread parameter specifies which keyword in the
  image header contains the readout noise value. If ccdread is undefined or
  not present in the image header the value of readnoise is used.
  Readnoise is assumed to be in units of electrons.
  APPHOT users should set either ccdread or readnoise before running any 
  APPHOT tasks to insure the magnitude error computations are correct.
  </p>
  <p>
  The magnitudes are normalized to an exposure time of 1 timeunit using
  the value of the exposure time in the image header parameter <i>exposure</i>
  or <i>itime</i>. If exposure is undefined or not present in the image header
  the value of itime is used. Itime can be in arbitrary units.
  Setting either exposure or itime will simplify future analysis steps.
  </p>
  <p>
  The parameters <i>airmass</i> and <i>xairmass</i> define the airmass
  of the observation. The airmass parameter specifies which keyword in the
  image header contains the airmass value. If airmass is undefined or
  not present in the image header the value of xairmass is used.
  The airmass values are not used in any APPHOT computations, however their
  presence in the APPHOT output files will simplify future reduction steps. 
  </p>
  <p>
  The parameters <i>filter</i> and <i>ifilter</i> define the filter
  of the observation. The filter parameter specifies which keyword in the
  image header contains the filter id. If filter is undefined or not present
  in the image header the value of ifilter is used. The filter id values are
  not used in any APPHOT computations, however their presence in the APPHOT
  output files can will simplify future reduction steps. 
  </p>
  <p>
  The parameters <i>obstime</i> and <i>otime</i> define the time 
  of the observation (e.g. UT). The obstime parameter specifies which keyword
  in the image header contains the time stamp of the observation. If obstime is
  undefined or not present in the image header the value of otime is used.
  The time of observations values are not used in any APPHOT 
  computations, however their presence in the APPHOT output files can
  greatly simplify future reduction steps. 
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the data dependent parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; lpar datapars
  </pre></div>
  <p>
  2. Edit the data dependent parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; datapars
  </pre></div>
  <p>
  3. Edit the DATAPARS parameters from within the PHOT task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; epar phot
  
      ... edit a few parameters
  
      ... move to the datapars parameter and type :e
  
      ... edit the datapars parameters and type :wq
  
      ... finish editing the phot parameters and type :wq
  </pre></div>
  <p>
  4. Save the current DATAPARS parameter set in a text file datnite1.par.
  This can also be done from inside a higher level task as in the
  previous example.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; datapars
  
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
  epar,lpar,daofind,center,fitsky,phot,wphot,polyphot,radprof,fitpsf
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _sptime:

sptime: Spectroscopic exposure time calculator
==============================================

**Package: obsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  sptime
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <p>
  The parameters in this task have certain common features.
  </p>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(1)' -->
  <dd>All parameters, except <i>spectrograph</i> and <i>search</i>, may be
  specified as spectrograph table parameters of the same name.  Some
  parameters may also be specified in other tables.  The tables in which the
  paramters may be specified are shown in brackets.  Table values are used
  only if a string parameter is <span style="font-family: monospace;">""</span> or a numeric parameter is INDEF.
  Therefore parameter set values override values in the tables.  To override
  a table specified in the spectrograph file by no file the special value
  <span style="font-family: monospace;">"none"</span> is used.  This task also uses default values, shown below in
  parenthesis, for parameters that have no value specified either in the
  parameter set or in a table.
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(2)' -->
  <dd>Parameters that specify a table take the value of a file or a numeric
  constant.  A constant is like a table with the same values for all value
  of the independent variable(s).
  </dd>
  </dl>
  <dl>
  <dt><b>(3)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(3)' -->
  <dd>Tables which are specified as filenames are sought first in the current
  working directory, then in one of the directories given by the
  <i>search</i> parameter, and finally in the package library directory
  sptimelib$.
  </dd>
  </dl>
  <dl id="l_time">
  <dt><b>time = INDEF (INDEF) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='time' Line='time = INDEF (INDEF) [spectrograph]' -->
  <dd>Total exposure time in seconds.  This time may be divided into shorter
  individual exposure times as defined by the <i>maxexp</i> parameter.  If
  the value is INDEF then the exposure time needed to achieve the
  signal-to-noise per pixel specified by the <i>sn</i> parameter is computed.
  </dd>
  </dl>
  <dl id="l_sn">
  <dt><b>sn = 25. (25.) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sn' Line='sn = 25. (25.) [spectrograph]' -->
  <dd>Desired signal-to-noise per pixel at the central wavelength if the
  exposure <i>time</i> parameter is not specified.
  </dd>
  </dl>
  <p>
  The following parameters define the source and sky/atmosphere background
  spectra.
  </p>
  <dl id="l_spectrum">
  <dt><b>spectrum = <span style="font-family: monospace;">"blackbody"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectrum' Line='spectrum = "blackbody"' -->
  <dd>Source spectrum.  This may be a table or one of the following  special words:
  <dl>
  <dt><b>blackbody</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='blackbody' Line='blackbody' -->
  <dd>Blackbody spectrum with temperature given by the <i>temperature</i>
  parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>flambda_power</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='flambda_power' Line='flambda_power' -->
  <dd>Power law in f(lambda) with index given by the <i>index</i> parameter;
  f(lambda) proportional to lambda^(index).
  </dd>
  </dl>
  <dl>
  <dt><b>fnu_power</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='fnu_power' Line='fnu_power' -->
  <dd>Power law in f(nu) with index given by the <i>index</i> parameter;
  f(nu) proportional to nu^(index).
  </dd>
  </dl>
  The table is a two column text file of wavelength in Angstroms and flux in
  ergs/s/cm^2/A.
  </dd>
  </dl>
  <dl id="l_spectitle">
  <dt><b>spectitle = <span style="font-family: monospace;">""</span> [spectrum|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectitle' Line='spectitle = "" [spectrum|spectrograph]' -->
  <dd>Spectrum title.
  </dd>
  </dl>
  <dl id="l_E">
  <dt><b>E = 0. (0.) [spectrum|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='E' Line='E = 0. (0.) [spectrum|spectrograph]' -->
  <dd>The E(B-V) color excess to apply a reddening to the source spectrum.  The
  reddening maintains the same table or reference flux at the reference
  wavelength.  A value of zero corresponds to no reddening.
  </dd>
  </dl>
  <dl id="l_R">
  <dt><b>R = 3.1 (3.1) [spectrum|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='R' Line='R = 3.1 (3.1) [spectrum|spectrograph]' -->
  <dd>The R(V) = A(V)/E(B-V) for the extinction law.  The extinction law is that
  of Cardelli, Clayton, and Mathis, <b>ApJ 345:245</b>, 1989.  The default
  R(V) is typical of the interstellar medium.
  </dd>
  </dl>
  <dl id="l_sky">
  <dt><b>sky = <span style="font-family: monospace;">""</span> (<span style="font-family: monospace;">"none"</span>) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sky' Line='sky = "" ("none") [spectrograph]' -->
  <dd>Sky or background table.  The table is a two or three column text file
  consisting of wavelength in Angstroms, optional moon phase between 0 (new
  moon) and 14 (full moon), and flux in ergs/s/cm^2/A/arcsec^2.
  </dd>
  </dl>
  <dl id="l_skytitle">
  <dt><b>skytitle = <span style="font-family: monospace;">""</span> [sky|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skytitle' Line='skytitle = "" [sky|spectrograph]' -->
  <dd>Sky title.
  </dd>
  </dl>
  <dl id="l_extinction">
  <dt><b>extinction = <span style="font-family: monospace;">""</span> (<span style="font-family: monospace;">"none"</span>) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extinction' Line='extinction = "" ("none") [spectrograph]' -->
  <dd>Extinction table.  The table is a two column text file consisting of
  wavelength in Angstroms and extinction in magnitudes per airmass.
  </dd>
  </dl>
  <dl id="l_exttitle">
  <dt><b>exttitle = <span style="font-family: monospace;">""</span> [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exttitle' Line='exttitle = "" [spectrograph]' -->
  <dd>Extinction title.
  </dd>
  </dl>
  <p>
  The following parameters are used with the source spectrum is specified
  by the special functions.
  </p>
  <dl id="l_refwave">
  <dt><b>refwave = INDEF (INDEF) [spectrum|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refwave' Line='refwave = INDEF (INDEF) [spectrum|spectrograph]' -->
  <dd>Reference wavelength, in units given by the <i>units</i> parameter, defining
  the flux of the source.  This is also used as the wavelength where
  reddening does not change the spectrum flux.  A value of INDEF uses the
  observation central wavelength.
  </dd>
  </dl>
  <dl id="l_refflux">
  <dt><b>refflux = 10. (10.) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refflux' Line='refflux = 10. (10.) [spectrograph]' -->
  <dd>Reference source flux or magnitude at the reference wavelength for the
  model spectral distributions.  The units are specified by the funits parameter.
  </dd>
  </dl>
  <dl id="l_funits">
  <dt><b>funits = <span style="font-family: monospace;">"AB"</span> (<span style="font-family: monospace;">"AB"</span>) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='funits' Line='funits = "AB" ("AB") [spectrograph]' -->
  <dd>Flux units for the reference flux.  The values are <span style="font-family: monospace;">"AB"</span> for monochromatic
  magnitude, <span style="font-family: monospace;">"F_lambda"</span> for ergs/s/cm^2/A, <span style="font-family: monospace;">"F_nu"</span> for ergs/s/cm^2/Hz,
  and standard bandpasses of U, B, V, R, I, J, H, Ks, K, L, L' and M.
  </dd>
  </dl>
  <dl id="l_temperature">
  <dt><b>temperature = 6000. (6000.) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='temperature' Line='temperature = 6000. (6000.) [spectrograph]' -->
  <dd>Blackbody temperature for a blackbody source spectrum in degrees Kelvin.
  </dd>
  </dl>
  <dl id="l_index">
  <dt><b>index = 0. (0.) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='index' Line='index = 0. (0.) [spectrograph]' -->
  <dd>Power law index for the power law source spectrum.
  </dd>
  </dl>
  <p>
  The following parameters are observational parameters describing either
  the observing conditions or spectrograph setup.
  </p>
  <dl id="l_seeing">
  <dt><b>seeing = 1. (1.) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='seeing' Line='seeing = 1. (1.) [spectrograph]' -->
  <dd>The full width at half maximum (FWHM) of a point source in arc seconds.
  </dd>
  </dl>
  <dl id="l_airmass">
  <dt><b>airmass = 1. (1.) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='airmass' Line='airmass = 1. (1.) [spectrograph]' -->
  <dd>The airmass of the observation.  This is only used if an extinction table
  is specified.
  </dd>
  </dl>
  <dl id="l_phase">
  <dt><b>phase = 0. (0.) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='phase' Line='phase = 0. (0.) [spectrograph]' -->
  <dd>The moon phase running from 0 for new moon to 14 for full moon.  This is
  used if the sky spectrum is given as a function of the moon phase.
  </dd>
  </dl>
  <dl id="l_thermal">
  <dt><b>thermal = 0. (0.) [telescope|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='thermal' Line='thermal = 0. (0.) [telescope|spectrograph]' -->
  <dd>Temperature in degress Kelvin for the thermal background of the telescope
  and spectrograph.  If greater than zero a blackbody surface brightness
  background is computed and multiplied by an emissivity specified by
  the <i>emissivity</i> table.
  </dd>
  </dl>
  <dl id="l_wave">
  <dt><b>wave = INDEF (INDEF) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wave' Line='wave = INDEF (INDEF) [spectrograph]' -->
  <dd>Central wavelength of observation in units given by the <i>units</i>
  parameter.  If the value is INDEF it is determined from the efficiency peak
  of the disperser.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = INDEF (INDEF) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = INDEF (INDEF) [spectrograph]' -->
  <dd>Order for grating or grism dispersers.  If the value is INDEF it is
  determined from the order nearest the desired central wavelength.  If both
  the order and central wavelength are undefined the first order is used.
  </dd>
  </dl>
  <dl id="l_xorder">
  <dt><b>xorder = INDEF (INDEF) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xorder' Line='xorder = INDEF (INDEF) [spectrograph]' -->
  <dd>Order for grating or grism cross dispersers.  If the value is INDEF it
  is determined from the order nearest the desired central wavelength.  If
  both the order and central wavelength are undefined the first order is
  used.
  </dd>
  </dl>
  <dl id="l_width">
  <dt><b>width = INDEF (-2.) [aperture|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='width' Line='width = INDEF (-2.) [aperture|spectrograph]' -->
  <dd>The aperture width (dispersion direction) for rectangular apertures
  such as slits.  Values may be positive to specify in arc seconds or
  negative to specify in projected pixels on the detector.
  </dd>
  </dl>
  <dl id="l_length">
  <dt><b>length = INDEF (-100.) [aperture|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='length' Line='length = INDEF (-100.) [aperture|spectrograph]' -->
  <dd>The aperture length (cross dispersion direction) for rectangular
  apertures such as slits.  Values may be positive to specify in arc seconds
  or negative to specify in projected pixels on the detector.
  </dd>
  </dl>
  <dl id="l_diameter">
  <dt><b>diameter = INDEF (-2.) [fiber|aperture|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='diameter' Line='diameter = INDEF (-2.) [fiber|aperture|spectrograph]' -->
  <dd>The aperture diameter for circular apertures.  Values
  may be positive to specify in arc seconds or negative to specify in
  projected pixels on the detector.  If it is found in the fiber table,
  positive values are treated as mm at the focal plane instead of arc seconds.
  </dd>
  </dl>
  <dl id="l_xbin">
  <dt><b>xbin = 1 (1) [detector|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xbin' Line='xbin = 1 (1) [detector|spectrograph]' -->
  <dd>Detector binning along the dispersion direction.
  </dd>
  </dl>
  <dl id="l_ybin">
  <dt><b>ybin = 1 (1) [detector|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ybin' Line='ybin = 1 (1) [detector|spectrograph]' -->
  <dd>Detector binning along the spatial direction.
  </dd>
  </dl>
  <p>
  The following parameters a miscellaneous parameters for the task.
  </p>
  <dl id="l_search">
  <dt><b>search = <span style="font-family: monospace;">"spectimedb$"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='search' Line='search = "spectimedb$"' -->
  <dd>List of directories to search for the various table files.  The current
  direction is always searched first and the directory sptimelib$ is searched
  last so it is not necessary to include these directories.  The list may be
  a comma delimited list of directories, an @file, or a template.
  </dd>
  </dl>
  <dl id="l_minexp">
  <dt><b>minexp = 0.01 (0.01) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minexp' Line='minexp = 0.01 (0.01) [spectrograph]' -->
  <dd>Minimumm time in seconds per individual exposure time.  This only applies
  when <i>time</i> is INDEF.  Adjustment of the exposure time for saturation
  will not allow the exposure time to fall below this value.
  </dd>
  </dl>
  <dl id="l_maxexp">
  <dt><b>maxexp = 3600. (3600.) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxexp' Line='maxexp = 3600. (3600.) [spectrograph]' -->
  <dd>Maximum time in seconds per individual exposure.  The minimum exposure time
  has precedence over this value.  If the total exposure time exceeds this
  amount by more than 1% then the total exposure time will be divided up into
  the fewest individual exposures with equal exposure time that are less than
  this amount.  Note that by making the minimum and maximum times the same a
  fixed integration time can be defined.
  </dd>
  </dl>
  <dl id="l_units">
  <dt><b>units = <span style="font-family: monospace;">"Angstroms"</span> (<span style="font-family: monospace;">"Angstroms"</span>) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='units' Line='units = "Angstroms" ("Angstroms") [spectrograph]' -->
  <dd>Dispersion units for input and output dispersion coordinates.  The
  units syntax is described in the UNITS section.  The most common units
  are <span style="font-family: monospace;">"Angstroms"</span>, <span style="font-family: monospace;">"nm"</span>, <span style="font-family: monospace;">"micron"</span>, and <span style="font-family: monospace;">"wn"</span>.  Note that this does not
  apply to the dispersion units in the tables which are always in Angstroms.
  </dd>
  </dl>
  <dl id="l_skysub">
  <dt><b>skysub = <span style="font-family: monospace;">""</span> (default based on context) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skysub' Line='skysub = "" (default based on context) [spectrograph]' -->
  <dd>Type of sky and background subtraction.  The values are <span style="font-family: monospace;">"none"</span> for no
  background subtraction, <span style="font-family: monospace;">"longslit"</span> for subtraction using pixels in the
  aperture, <span style="font-family: monospace;">"multiap"</span> for background determined from a number of other
  apertures, and <span style="font-family: monospace;">"shuffle"</span> for shuffled observations.  The multiap case is
  typical for fiber spectrographs.  For shuffle the duty cycle is 50% and the
  exposure times are the sum of both sky and object.  If no sky or thermal
  background is specified then the default is <span style="font-family: monospace;">"none"</span>.  If a fiber table or
  circular aperture is specified the default is <span style="font-family: monospace;">"multiap"</span> otherwise the
  default is <span style="font-family: monospace;">"longslit"</span>.
  </dd>
  </dl>
  <dl id="l_nskyaps">
  <dt><b>nskyaps = 10  (10) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nskyaps' Line='nskyaps = 10  (10) [spectrograph]' -->
  <dd>Number of sky apertures when using <span style="font-family: monospace;">"multiap"</span> sky subtraction.
  </dd>
  </dl>
  <dl id="l_subpixels">
  <dt><b>subpixels = 1 (1) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subpixels' Line='subpixels = 1 (1) [spectrograph]' -->
  <dd>Number of subpixels within each computed pixel.
  The dispersion pixel width is divided into this number of equal
  width subpixels.  The flux at the dispersions represented by the subpixels
  are computed and then summed to form the full pixel flux.  This option is used
  when there is structure in the tables, such as the sky and filter tables to
  simulate instrumental masking of sky lines, which is finer than a pixel
  dispersion width.
  </dd>
  </dl>
  <dl id="l_sensfunc">
  <dt><b>sensfunc = <span style="font-family: monospace;">""</span> [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sensfunc' Line='sensfunc = "" [spectrograph]' -->
  <dd>Sensitivity function table.  This is a two column text file consisting
  of wavelength in Angstroms and sensitivity defined as
  2.5*(log(countrate)-log(flambda)),
  where countrate is the count rate (without extinction) in counts/s/A
  and flambda is the source flux in ergs/s/cm^2/A.  This table is used
  to compute an efficiency correction given a measurement of the
  sensitivity function from standard stars for the instrument.
  </dd>
  </dl>
  <p>
  The following parameters control the output of the task.  The task
  always prints a result page at the central wavelength but additional
  graphical and text output may be produced at a set of equally spaced
  points across the size of the detector.
  </p>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">"object"</span> (<span style="font-family: monospace;">""</span>) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = "object" ("") [spectrograph]' -->
  <dd>List of quantities to output as graphs and/or in a text file.  These are
  given as a function of dispersion (as specified by units parameters)
  sampled across the dispersion coverage of the detector.  The choices are:
  <dl>
  <dt><b>counts</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='counts' Line='counts' -->
  <dd>Object and background counts per individual exposure.
  </dd>
  </dl>
  <dl>
  <dt><b>snr</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='snr' Line='snr' -->
  <dd>Signal-to-noise ratio per pixel per individual exposure.
  </dd>
  </dl>
  <dl>
  <dt><b>object</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='object' Line='object' -->
  <dd>Object counts per individual exposure.  This includes contribution
  from other orders if there is no cross dispersion and the blocking
  filters do not completely exclude other orders.
  </dd>
  </dl>
  <dl>
  <dt><b>rate</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='rate' Line='rate' -->
  <dd>Photons/second/A per individual exposure for the object and background.
  </dd>
  </dl>
  <dl>
  <dt><b>atmosphere</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='atmosphere' Line='atmosphere' -->
  <dd>Percent transmission of the atmosphere.
  </dd>
  </dl>
  <dl>
  <dt><b>telescope</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='telescope' Line='telescope' -->
  <dd>Percent transmission of the telescope.
  </dd>
  </dl>
  <dl>
  <dt><b>adc</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='adc' Line='adc' -->
  <dd>Percent transmission of the ADC if one is used.
  </dd>
  </dl>
  <dl>
  <dt><b>aperture</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='aperture' Line='aperture' -->
  <dd>Percent transmission of the aperture.
  </dd>
  </dl>
  <dl>
  <dt><b>fiber</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='fiber' Line='fiber' -->
  <dd>Percent transmission of the fiber if one is used.
  </dd>
  </dl>
  <dl>
  <dt><b>filter</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='filter' Line='filter' -->
  <dd>Percent transmission of the first filter if one is used.
  </dd>
  </dl>
  <dl>
  <dt><b>filter2</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='filter2' Line='filter2' -->
  <dd>Percent transmission of the second filter if one is used.
  </dd>
  </dl>
  <dl>
  <dt><b>collimator</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='collimator' Line='collimator' -->
  <dd>Percent transmission of the collimator.
  </dd>
  </dl>
  <dl>
  <dt><b>disperser</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='disperser' Line='disperser' -->
  <dd>Percent efficiency of the disperser.
  </dd>
  </dl>
  <dl>
  <dt><b>xdisperser</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='xdisperser' Line='xdisperser' -->
  <dd>Percent efficiency of the cross disperser if one is used.
  </dd>
  </dl>
  <dl>
  <dt><b>corrector</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='corrector' Line='corrector' -->
  <dd>Percent transmission of the corrector if one is used.
  </dd>
  </dl>
  <dl>
  <dt><b>camera</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='camera' Line='camera' -->
  <dd>Percent transmission of the camera.
  </dd>
  </dl>
  <dl>
  <dt><b>detector</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='detector' Line='detector' -->
  <dd>Percent DQE of the detector.
  </dd>
  </dl>
  <dl>
  <dt><b>spectrograph</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='spectrograph' Line='spectrograph' -->
  <dd>Percent transmission of the spectrograph if a transmission
  function is defined.
  </dd>
  </dl>
  <dl>
  <dt><b>emissivity</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='emissivity' Line='emissivity' -->
  <dd>Emissivity of the telescope/spectrograph if an emissivity function
  is defined.
  </dd>
  </dl>
  <dl>
  <dt><b>thruput</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='thruput' Line='thruput' -->
  <dd>Percent system thruput from telescope to detected photons.
  </dd>
  </dl>
  <dl>
  <dt><b>sensfunc</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='sensfunc' Line='sensfunc' -->
  <dd>Sensitivity function values given as 2.5*(log(countrate)-log(flambda)),
  where countrate is the count rate (without extinction) in counts/s/A
  and flambda is the source flux in ergs/s/cm^2/A.
  </dd>
  </dl>
  <dl>
  <dt><b>correction</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='correction' Line='correction' -->
  <dd>Multiplicative correction factor needed to convert the computed
  count rate to that given by an input sensitivity function.
  </dd>
  </dl>
  <dl>
  <dt><b>ALL  </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='ALL' Line='ALL  ' -->
  <dd>All of the above.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_nw">
  <dt><b>nw = 101 (101) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nw' Line='nw = 101 (101) [spectrograph]' -->
  <dd>Number of dispersion points to use in the output graphs and text
  file.  Note that this is generally less than the number of pixels in
  the detector for execution speed.
  </dd>
  </dl>
  <dl id="l_list">
  <dt><b>list = <span style="font-family: monospace;">""</span> [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='list' Line='list = "" [spectrograph]' -->
  <dd>Filename for list output of the selected quantities.  The output
  will be appended if the file already exists.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span> (<span style="font-family: monospace;">"stdgraph"</span>) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph" ("stdgraph") [spectrograph]' -->
  <dd>Graphics output device for graphs of the output quantities.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = <span style="font-family: monospace;">"yes"</span> (<span style="font-family: monospace;">"yes"</span>) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = "yes" ("yes") [spectrograph]' -->
  <dd>Interactive pause after each graph?  If <span style="font-family: monospace;">"yes"</span> then cursor input is
  enabled after each graph otherwise all the graphs will be drawn without
  pause.  When viewing the graphs interactively this should be <span style="font-family: monospace;">"yes"</span> otherwise
  the graphs will flash by rapidly leaving the last graph on the screen.
  When outputing only one graph or when redirecting the graphs to a
  printer or file then setting this parameter to <span style="font-family: monospace;">"no"</span> is suggested.
  </dd>
  </dl>
  <p>
  The last parameter is a <span style="font-family: monospace;">"parameter set"</span> (<span style="font-family: monospace;">"pset"</span>) containing all the
  spectrograph parameters.
  </p>
  <dl id="l_specpars">
  <dt><b>specpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specpars' Line='specpars = ""' -->
  <dd>Spectrograph parameter set.  If <span style="font-family: monospace;">""</span> then the default pset <b>specpars</b>
  is used otherwise the named pset is used.
  </dd>
  </dl>
  <p>
  SPECPARS PARAMETERS
  </p>
  <dl id="l_spectrograph">
  <dt><b>spectrograph = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectrograph' Line='spectrograph = ""' -->
  <dd>Spectrograph efficiency table.  This text file may contain parameters and an
  efficiency table.  The table consists of two columns containing
  wavelengths and efficiencies.  The efficiencies are for all elements
  which are not accounted for by other tables.
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">""</span> [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = "" [spectrograph]' -->
  <dd>Title for the spectrograph.
  </dd>
  </dl>
  <dl id="l_apmagdisp">
  <dt><b>apmagdisp = INDEF (1.), apmagxdisp = INDEF (1.) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apmagdisp' Line='apmagdisp = INDEF (1.), apmagxdisp = INDEF (1.) [spectrograph]' -->
  <dd>Magnification between the entrance aperture and the detector along and
  across the dispersion direction.  This describes any magnification (or
  demagnification) in the spectrograph other than that produced by the ratio
  of the collimator and camera focal lengths and anamorphic magnification
  from the disperser.  The may consist of actual magnification optics or
  projection effects such as tilted aperture plates (when the aperture size
  is specified in the untilted plate).
  </dd>
  </dl>
  <dl id="l_inoutangle">
  <dt><b>inoutangle = INDEF (INDEF) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inoutangle' Line='inoutangle = INDEF (INDEF) [spectrograph]' -->
  <dd>Incident to diffracted grating angle in degrees for grating dispersers.
  For typical spectrographs which are not cross dispersed this is the
  collimator to camera angle.  If the value is INDEF derived from the grating
  parameters.
  </dd>
  </dl>
  <dl id="l_xinoutangle">
  <dt><b>xinoutangle = INDEF (INDEF) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xinoutangle' Line='xinoutangle = INDEF (INDEF) [spectrograph]' -->
  <dd>Incident to diffracted grating angle in degrees for grating cross
  dispersers.  If the value is INDEF it is derived from the grating
  parameters.
  </dd>
  </dl>
  <dl id="l_telescope">
  <dt><b>telescope = <span style="font-family: monospace;">""</span> [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='telescope' Line='telescope = "" [spectrograph]' -->
  <dd>Telescope efficiency table as a function of wavelength.  
  </dd>
  </dl>
  <dl id="l_teltitle">
  <dt><b>teltitle = <span style="font-family: monospace;">""</span> [telescope|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='teltitle' Line='teltitle = "" [telescope|spectrograph]' -->
  <dd>Telescope title.
  </dd>
  </dl>
  <dl id="l_area">
  <dt><b>area = INDEF (1.) [telescope|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='area' Line='area = INDEF (1.) [telescope|spectrograph]' -->
  <dd>Effective collecting area of the telescope in m^2.  The effective area
  includes reductions in the primary area due to obstructions.
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = INDEF (10.) [telescope|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = INDEF (10.) [telescope|spectrograph]' -->
  <dd>Telescope plate scale, in arcsec/mm, at the entrance aperture of the
  spectrograph.
  </dd>
  </dl>
  <dl id="l_emissivity">
  <dt><b>emissivity = <span style="font-family: monospace;">""</span> [telescope|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='emissivity' Line='emissivity = "" [telescope|spectrograph]' -->
  <dd>Emissivity table.  The emissivity is for all elements in the telescope
  and spectrograph.  If an emissivity is specified and an the <i>thermal</i>
  temperature parameter is greater than zero then a thermal background
  is added to the calculation.
  </dd>
  </dl>
  <dl id="l_emistitle">
  <dt><b>emistitle = <span style="font-family: monospace;">""</span> [emissivity|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='emistitle' Line='emistitle = "" [emissivity|spectrograph]' -->
  <dd>Title for the emissivity table used.
  </dd>
  </dl>
  <dl id="l_corrector">
  <dt><b>corrector = <span style="font-family: monospace;">""</span> [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='corrector' Line='corrector = "" [spectrograph]' -->
  <dd>Efficiency table for one or more correctors.
  </dd>
  </dl>
  <dl id="l_cortitle">
  <dt><b>cortitle = <span style="font-family: monospace;">""</span> [corrector|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cortitle' Line='cortitle = "" [corrector|spectrograph]' -->
  <dd>Title for corrector table used.
  </dd>
  </dl>
  <dl id="l_adc">
  <dt><b>adc = <span style="font-family: monospace;">""</span> [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='adc' Line='adc = "" [spectrograph]' -->
  <dd>Efficiency table for atmospheric dispersion compensator.
  </dd>
  </dl>
  <dl id="l_adctitle">
  <dt><b>adctitle = <span style="font-family: monospace;">""</span> [adc|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='adctitle' Line='adctitle = "" [adc|spectrograph]' -->
  <dd>Title for ADC table used.
  </dd>
  </dl>
  <dl id="l_disperser">
  <dt><b>disperser = <span style="font-family: monospace;">""</span> [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='disperser' Line='disperser = "" [spectrograph]' -->
  <dd>Disperser table.  If this file contains an efficiency table it applies
  only to first order.  An alternate first order table and tables for
  other orders are given by table parameters <span style="font-family: monospace;">"effN"</span>, where N is the order.
  </dd>
  </dl>
  <dl id="l_disptitle">
  <dt><b>disptitle = <span style="font-family: monospace;">""</span> [disperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='disptitle' Line='disptitle = "" [disperser|spectrograph]' -->
  <dd>Title for disperser.
  </dd>
  </dl>
  <dl id="l_disptype">
  <dt><b>disptype = <span style="font-family: monospace;">""</span> (<span style="font-family: monospace;">"grating"</span>) [disperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='disptype' Line='disptype = "" ("grating") [disperser|spectrograph]' -->
  <dd>Type of disperser element.  The chocies are <span style="font-family: monospace;">"grating"</span>, <span style="font-family: monospace;">"grism"</span>, or <span style="font-family: monospace;">"generic"</span>.
  The generic setting will simply use the desired central wavelength and
  dispersion without a grating or grism model.  One effect of this is that
  the mapping between detector pixel and wavelength is linear; i.e. a constant
  dispersion per pixel.
  </dd>
  </dl>
  <dl id="l_gmm">
  <dt><b>gmm = INDEF (300.) [disperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gmm' Line='gmm = INDEF (300.) [disperser|spectrograph]' -->
  <dd>Ruling in lines per mm.  If not specified it will be derived from the
  other disperser parameters.  If there is not enough information to
  derive the ruling then an ultimate default of 300 lines/mm is used.
  </dd>
  </dl>
  <dl id="l_blaze">
  <dt><b>blaze = INDEF (6.) [disperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blaze' Line='blaze = INDEF (6.) [disperser|spectrograph]' -->
  <dd>Blaze (grating) or prism (grism) angle in degrees.  If not specified it
  will be derived from the other disperser parameters.  If there is not
  enough information to derive the angle then an ultimate default of 6
  degrees is used.
  </dd>
  </dl>
  <dl id="l_oref">
  <dt><b>oref = INDEF (1) [disperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='oref' Line='oref = INDEF (1) [disperser|spectrograph]' -->
  <dd>When a central (blaze) wavelength is specified this parameter indicates
  which order it is for.
  </dd>
  </dl>
  <dl id="l_wavelength">
  <dt><b>wavelength = INDEF (INDEF) [disperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wavelength' Line='wavelength = INDEF (INDEF) [disperser|spectrograph]' -->
  <dd>Central (blaze) wavelength in Angstroms for the reference order.  This
  parameter only applies to gratings.  If it is not specified it will
  be derived from the other disperser parameters.
  </dd>
  </dl>
  <dl id="l_dispersion">
  <dt><b>dispersion = INDEF (INDEF) [disperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispersion' Line='dispersion = INDEF (INDEF) [disperser|spectrograph]' -->
  <dd>Central dispersion in A/mm for the reference order.  This parameter only
  applies to gratings.  If it is not specified it will be derived from the
  other disperser parameters.
  </dd>
  </dl>
  <dl id="l_indexref">
  <dt><b>indexref = INDEF (INDEF) [disperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='indexref' Line='indexref = INDEF (INDEF) [disperser|spectrograph]' -->
  <dd>Grism index of refraction for the reference order.  This parameter only
  applies to grisms.  If it is not specified it will be derived from
  the other disperser parameters.
  </dd>
  </dl>
  <dl id="l_eff">
  <dt><b>eff = INDEF (1.) [disperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='eff' Line='eff = INDEF (1.) [disperser|spectrograph]' -->
  <dd>Peak efficiency for the theoretical disperser efficiency function.
  When an efficiency table is not specified then a theoretical efficiency
  is computed for the disperser.  This theoretical efficiency is scaled
  to peak efficiency given by this parameter.
  </dd>
  </dl>
  <dl id="l_xdisperser">
  <dt><b>xdisperser = <span style="font-family: monospace;">""</span> [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xdisperser' Line='xdisperser = "" [spectrograph]' -->
  <dd>Crossdisperser table.  If this file contains an efficiency table it applies
  only to first order.  An alternate first order table and tables for
  other orders are given by table parameters <span style="font-family: monospace;">"xeffN"</span>, where N is the order.
  </dd>
  </dl>
  <dl id="l_xdisptitle">
  <dt><b>xdisptitle = <span style="font-family: monospace;">""</span> [xdisperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xdisptitle' Line='xdisptitle = "" [xdisperser|spectrograph]' -->
  <dd>Title for crossdisperser.
  </dd>
  </dl>
  <dl id="l_disptype">
  <dt><b>disptype = <span style="font-family: monospace;">""</span> (<span style="font-family: monospace;">"grating"</span>) [xdisperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='disptype' Line='disptype = "" ("grating") [xdisperser|spectrograph]' -->
  <dd>Type of crossdisperser element.  The chocies are <span style="font-family: monospace;">""</span>, <span style="font-family: monospace;">"grating"</span>, <span style="font-family: monospace;">"grism"</span>,
  or <span style="font-family: monospace;">"generic"</span>.  The empty string eliminates use of a cross disperser.
  The generic setting will simply use the desired central wavelength and
  dispersion without a grating or grism model.  One effect of this is that
  the mapping between detector pixel and wavelength is linear; i.e. a constant
  dispersion per pixel.
  </dd>
  </dl>
  <dl id="l_gmm">
  <dt><b>gmm = INDEF (INDEF) [xdisperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gmm' Line='gmm = INDEF (INDEF) [xdisperser|spectrograph]' -->
  <dd>Ruling in lines per mm.  If not specified it will be derived from the
  other crossdisperser parameters.
  </dd>
  </dl>
  <dl id="l_xblaze">
  <dt><b>xblaze = INDEF (6.) [xdisperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xblaze' Line='xblaze = INDEF (6.) [xdisperser|spectrograph]' -->
  <dd>Blaze (grating) or prism (grism) angle in degrees.  If not specified it
  will be derived from the other crossdisperser parameters.
  </dd>
  </dl>
  <dl id="l_xoref">
  <dt><b>xoref = INDEF (1) [xdisperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xoref' Line='xoref = INDEF (1) [xdisperser|spectrograph]' -->
  <dd>When a central (blaze) wavelength is specified this parameter indicates
  which order it is for.
  </dd>
  </dl>
  <dl id="l_xwavelength">
  <dt><b>xwavelength = INDEF (INDEF) [xdisperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xwavelength' Line='xwavelength = INDEF (INDEF) [xdisperser|spectrograph]' -->
  <dd>Central (blaze) wavelength in Angstroms for the reference order.  This
  parameter only applies to gratings.  If it is not specified it will
  be derived from the other crossdisperser parameters.
  </dd>
  </dl>
  <dl id="l_xdispersion">
  <dt><b>xdispersion = INDEF (INDEF) [xdisperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xdispersion' Line='xdispersion = INDEF (INDEF) [xdisperser|spectrograph]' -->
  <dd>Central dispersion in A/mm for the reference order.  This parameter only
  applies to gratings.  If it is not specified it will be derived from the
  other crossdisperser parameters.
  </dd>
  </dl>
  <dl id="l_xindexref">
  <dt><b>xindexref = INDEF (INDEF) [xdisperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xindexref' Line='xindexref = INDEF (INDEF) [xdisperser|spectrograph]' -->
  <dd>Grism index of refraction for the reference order.  This parameter only
  applies to grisms.  If it is not specified it will be derived from
  the other crossdisperser parameters.
  </dd>
  </dl>
  <dl id="l_xeff">
  <dt><b>xeff = INDEF (1.) [xdisperser|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xeff' Line='xeff = INDEF (1.) [xdisperser|spectrograph]' -->
  <dd>Peak efficiency for the theoretical crossdisperser efficiency function.
  When an efficiency table is not specified then a theoretical efficiency
  is computed for the crossdisperser.  This theoretical efficiency is scaled
  to peak efficiency given by this parameter.
  </dd>
  </dl>
  <dl id="l_aperture">
  <dt><b>aperture = <span style="font-family: monospace;">""</span> (default based on context) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='aperture' Line='aperture = "" (default based on context) [spectrograph]' -->
  <dd>Aperture table.  The text file gives aperture thruput as a function of the
  aperture size in units of seeing FWHM.  For rectangular apertures there are
  two independent variables corresponding to the width and length while for
  circular apertures there is one independent variable corresponding to the
  diameter.  If not specified a default table is supplied.  If a fiber table
  or a diameter is specified then the table <span style="font-family: monospace;">"circle"</span> is used otherwise the
  table <span style="font-family: monospace;">"slit"</span> is used.  Because <span style="font-family: monospace;">"sptimelib$"</span> is the last directory searched
  there are default files with these names in this directory for Gaussian
  seeing profiles passing through a circular or slit aperture.
  </dd>
  </dl>
  <dl id="l_aptitle">
  <dt><b>aptitle = <span style="font-family: monospace;">""</span> [aperture|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='aptitle' Line='aptitle = "" [aperture|spectrograph]' -->
  <dd>Title for aperture used.
  </dd>
  </dl>
  <dl id="l_aptype">
  <dt><b>aptype = <span style="font-family: monospace;">""</span> (default based on context) [aperture|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='aptype' Line='aptype = "" (default based on context) [aperture|spectrograph]' -->
  <dd>The aperture types are <span style="font-family: monospace;">"rectangular"</span> or <span style="font-family: monospace;">"circular"</span>.  If the
  parameter is not specified then if the aperture table has two columns the
  type is <span style="font-family: monospace;">"circular"</span> otherwise it is <span style="font-family: monospace;">"rectangular"</span>.
  </dd>
  </dl>
  <dl id="l_fiber">
  <dt><b>fiber = <span style="font-family: monospace;">""</span> [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fiber' Line='fiber = "" [spectrograph]' -->
  <dd>Fiber transmission table.  The transmission is a function of wavelength
  in Angstroms.  If no fiber transmission is specified then no fiber
  component is included.
  </dd>
  </dl>
  <dl id="l_fibtitle">
  <dt><b>fibtitle = <span style="font-family: monospace;">""</span> [fiber|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fibtitle' Line='fibtitle = "" [fiber|spectrograph]' -->
  <dd>Title for fiber transmission used.
  </dd>
  </dl>
  <dl id="l_filter">
  <dt><b>filter = <span style="font-family: monospace;">""</span> [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filter' Line='filter = "" [spectrograph]' -->
  <dd>Filter transmission table.  The transmission is a function of wavelength
  in Angstroms.  If no filter transmission is specified then no filter
  component is included.
  </dd>
  </dl>
  <dl id="l_ftitle">
  <dt><b>ftitle = <span style="font-family: monospace;">""</span> [filter|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ftitle' Line='ftitle = "" [filter|spectrograph]' -->
  <dd>Title for filter transmission used.
  </dd>
  </dl>
  <dl id="l_filter2">
  <dt><b>filter2 = <span style="font-family: monospace;">""</span> [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filter2' Line='filter2 = "" [spectrograph]' -->
  <dd>Filter transmission table.  The transmission is a function of wavelength
  in Angstroms.  If no filter transmission is specified then no filter
  component is included.
  </dd>
  </dl>
  <dl id="l_f2title">
  <dt><b>f2title = <span style="font-family: monospace;">""</span> [filter|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='f2title' Line='f2title = "" [filter|spectrograph]' -->
  <dd>Title for filter transmission used.
  </dd>
  </dl>
  <dl id="l_block">
  <dt><b>block = <span style="font-family: monospace;">""</span> (<span style="font-family: monospace;">"no"</span>) [filter|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='block' Line='block = "" ("no") [filter|spectrograph]' -->
  <dd>If <span style="font-family: monospace;">"yes"</span> then no check will be made for other orders.
  </dd>
  </dl>
  <dl id="l_collimator">
  <dt><b>collimator = <span style="font-family: monospace;">""</span> (1.) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='collimator' Line='collimator = "" (1.) [spectrograph]' -->
  <dd>Collimator transmission table.  The transmission is a function of
  wavelength in Angstroms.  If no collimator is specified then a unit
  transmission is used.
  </dd>
  </dl>
  <dl id="l_coltitle">
  <dt><b>coltitle = <span style="font-family: monospace;">""</span> [collimator|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coltitle' Line='coltitle = "" [collimator|spectrograph]' -->
  <dd>Title for collimator.
  </dd>
  </dl>
  <dl id="l_colfl">
  <dt><b>colfl = INDEF (1.) [collimator|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='colfl' Line='colfl = INDEF (1.) [collimator|spectrograph]' -->
  <dd>Collimator focal length in meters.  The ratio of the collimator to camera
  focal lengths determines the magnification between the aperture and the
  detector.
  </dd>
  </dl>
  <dl id="l_camera">
  <dt><b>camera = <span style="font-family: monospace;">""</span> (1.) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='camera' Line='camera = "" (1.) [spectrograph]' -->
  <dd>Camera transmission table.  The transmission is a function of wavelength
  in Angstroms.  If no camera is specified then a unit transmission
  is used.
  </dd>
  </dl>
  <dl id="l_camtitle">
  <dt><b>camtitle = <span style="font-family: monospace;">""</span> [camera|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='camtitle' Line='camtitle = "" [camera|spectrograph]' -->
  <dd>Title for camera.
  </dd>
  </dl>
  <dl id="l_camfl">
  <dt><b>camfl = <span style="font-family: monospace;">""</span> (1.) [camera|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='camfl' Line='camfl = "" (1.) [camera|spectrograph]' -->
  <dd>Camera focal length in meters.  The ratio of the collimator to
  camera focal lengths determines the magnification between the aperture
  and the detector.  The camera focal length also determines the dispersion
  scale at the detector.
  </dd>
  </dl>
  <dl id="l_resolution">
  <dt><b>resolution = <span style="font-family: monospace;">""</span> (2 pixels) [camera|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='resolution' Line='resolution = "" (2 pixels) [camera|spectrograph]' -->
  <dd>Camera resolution on the detector in mm.
  </dd>
  </dl>
  <dl id="l_vignetting">
  <dt><b>vignetting = <span style="font-family: monospace;">""</span> (1.) [camera|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vignetting' Line='vignetting = "" (1.) [camera|spectrograph]' -->
  <dd>Vignetting table.  The independent variable is distance from the center
  of the detector in mm.  The value is the fraction the light transmitted.
  If no vignetting table is specified then no vignetting effect is applied.
  </dd>
  </dl>
  <dl id="l_detector">
  <dt><b>detector = <span style="font-family: monospace;">""</span> (1.) [spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='detector' Line='detector = "" (1.) [spectrograph]' -->
  <dd>Detector DQE table.  The DQE is a function of wavelength in Angstroms.
  </dd>
  </dl>
  <dl id="l_dettitle">
  <dt><b>dettitle = <span style="font-family: monospace;">""</span> [detector|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dettitle' Line='dettitle = "" [detector|spectrograph]' -->
  <dd>Title for detector.
  </dd>
  </dl>
  <dl id="l_ndisp">
  <dt><b>ndisp = INDEF (2048) [detector|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ndisp' Line='ndisp = INDEF (2048) [detector|spectrograph]' -->
  <dd>Number of pixels along the dispersion.
  </dd>
  </dl>
  <dl id="l_pixsize">
  <dt><b>pixsize = INDEF (0.02) [detector|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixsize' Line='pixsize = INDEF (0.02) [detector|spectrograph]' -->
  <dd>Pixel size (assumed square) in mm.
  </dd>
  </dl>
  <dl id="l_gain">
  <dt><b>gain = INDEF (1.) [detector|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gain' Line='gain = INDEF (1.) [detector|spectrograph]' -->
  <dd>The conversion between photons and detector data numbers or counts.
  This is given as photons/ADU where ADU is analog-to-digital unit.
  </dd>
  </dl>
  <dl id="l_rdnoise">
  <dt><b>rdnoise = INDEF (0.) [detector|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rdnoise' Line='rdnoise = INDEF (0.) [detector|spectrograph]' -->
  <dd>Readout noise in photons.
  </dd>
  </dl>
  <dl id="l_dark">
  <dt><b>dark = INDEF (0.) [detector|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dark' Line='dark = INDEF (0.) [detector|spectrograph]' -->
  <dd>Dark count rate in photons/s.
  </dd>
  </dl>
  <dl id="l_saturation">
  <dt><b>saturation = INDEF [detector|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='saturation' Line='saturation = INDEF [detector|spectrograph]' -->
  <dd>Number of detected photons in a pixel resulting in saturation.
  The default is no saturation.  The time per exposure will be reduced,
  but no lower than the minimum time per exposure,
  and the number of exposures increased to try and avoid saturation.
  </dd>
  </dl>
  <dl id="l_dnmax">
  <dt><b>dnmax = INDEF [detector|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dnmax' Line='dnmax = INDEF [detector|spectrograph]' -->
  <dd>Maximum data number or ADU allowed.  The default is no maximum.
  The time per exposure will be reduced,
  but no lower than the minimum time per exposure,
  and the number of exposures increased to try and avoid overflow.
  </dd>
  </dl>
  <dl id="l_xbin">
  <dt><b>xbin = 1 (1) [detector|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xbin' Line='xbin = 1 (1) [detector|spectrograph]' -->
  <dd>Detector binning along the dispersion direction.
  </dd>
  </dl>
  <dl id="l_ybin">
  <dt><b>ybin = 1 (1) [detector|spectrograph]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ybin' Line='ybin = 1 (1) [detector|spectrograph]' -->
  <dd>Detector binning along the spatial direction.
  </dd>
  </dl>
  </section>
  <section id="s_discussion">
  <h3>Discussion</h3>
  <p>
  OVERVIEW
  </p>
  <p>
  The spectroscopic exposure time package, <b>SPECTIME</b>, consists of a
  general calculation engine, <b>SPTIME</b>, and a collection of user or
  database defined IRAF scripts.  The scripts are one type of user interface
  for <b>SPTIME</b>.  Other user interfaces are Web-based forms and IRAF
  graphics/window applications.  The user interfaces customize the general
  engine to specific spectrographs by hiding components and parameters not
  applicable to that spectrograph and guiding the user, through menus or
  other facilities, in the choice of filters, gratings, etc.  However,
  <b>SPTIME</b> is a standard IRAF task that can be executed directly.
  </p>
  <p>
  <b>SPTIME</b> takes an input source spectrum (either a reference blackbody,
  a power law, or a user spectrum), a background <span style="font-family: monospace;">"sky"</span> spectrum and a
  instrumental thermal background, reddening to apply to the spectrum,
  observing parameters such as exposure time, central wavelength, seeing,
  airmass, and moon phase, instrument parameters such as aperture sizes and
  detector binning, a description of the spectrograph, and produces
  information about the expected signal and signal-to-noise ratio in the
  extracted one-dimensional spectrum.  The output consists of a description
  of the observation, signal-to-noise statistics, and optional graphs and
  tables of various quantities as a function of wavelength over the
  spectrograph wavelength coverage.
  </p>
  <p>
  <b>SPTIME</b> models a spectroscopic system as a flow of photons from a
  source to the detector through various optical components.  Background
  photons from the sky, atmosphere, and the thermal emission from the
  telescope and spectrograph are added.  It then computes signal-to-noise
  ratios from the detected photons of the source and background and the
  instrumental noise characteristics.  The spectroscopic system components
  are defined at a moderate level of detail.  It is not so detailed that
  every optical element has to be described and modeled and not so coarse
  that a single throughput function is used (though one is free to put all
  the thruput information into one component).  Not all components modeled by
  the task occur in all spectroscopic systems.  Therefore many of the
  components can be left out of the calculation.
  </p>
  <p>
  The components currently included in <b>SPTIME</b> are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  - the atmosphere (extinction and IR transmission)
  - the telescope (all elements considered as a unit)
  - an optional atmospheric dispersion compensator
  - the entrance aperture (slits, fibers, masks, etc.)
  - an optional fiber feed
  - a spectrograph (for components not represented elsewhere)
  - filters
  - a collimator
  - a disperser (grating, grism, prism, etc)
  - a optional cross disperser (grating, grism, prism, etc)
  - a corrector (either in the telescope of spectrograph)
  - a camera
  - a detector
  </pre></div>
  <p>
  Each of these components represent a transmission function specifying the
  fraction of incident light transmitted or detected as a function of some
  parameter or parameters.  Except for the aperture, which is a function of
  the incident source profile (typically the seeing profile) relative to the
  aperture size, the transmissions of the components listed above are all
  functions of wavelength.
  </p>
  <p>
  All the component transmission functions may be specified as either numeric
  values or as tables.  A numeric value is considered to be a special type of
  table which has the same value at all values of the independent parameters.
  By specifying only numeric values the task may be run without any table
  files.  To obtain information at a single wavelength this is all that is
  needed.
  </p>
  <p>
  To specify a dependence on wavelength or other parameter a text file table
  with two or more columns may be specified.  The tables are interpolated in
  the parameter columns to find the desired value in the last column.  The
  tables are searched for in the current directory and then in a list of user
  specified directories.  Thus, users may place files in their work area to
  override system supplied files and observatories can organize the data
  files in a database directory tree.
  </p>
  <p>
  In addition to transmission or DQE functions the spectrograph is described
  by various parameters.  All the parameters are described in the PARAMETERS
  section.  For flexibility parameters may be defined either in the
  parameter set or in one or more table files.  In all cases the parameter
  set values have precedence.   But if the values are <span style="font-family: monospace;">""</span> for string  parameters
  or INDEF for numeric parameters the values are found either in the
  spectrograph table or in a table that is associated with the parameter.
  </p>
  <p>
  Therefore table files provide for interchangeable components, each with
  their own transmission curves, and for organizing parameters for different
  instruments.  Note that a table file may contain only parameters, only
  a table, or both.
  </p>
  <p>
  There is also another way to maintain a separate file for different
  instruments.  The <i>specpars</i> parameter is a <span style="font-family: monospace;">"parameter set"</span> or <span style="font-family: monospace;">"pset"</span>.
  The default value of <span style="font-family: monospace;">""</span> corresponds to the pset task <b>specpars</b>.
  However, using <b>eparam</b> one can edit this pset and then save the
  parameters to a named parameter file with <span style="font-family: monospace;">":e &lt;name&gt;.par"</span>.  This
  pset can be edited with <b>eparam</b> and specified in the
  <i>specpars</i> parameter.  One other point about pset parameters is that
  they can also be included as command line arguments just as any other
  parameter in the main task parameters.
  </p>
  <p>
  Many spectrographs provide a wide variety of wavelength regions and
  dispersions.  For gratings (and to some extent for grisms) this means use
  of different gratings, orders, tilts, and possibly camera angles in the
  spectrograph.  The transmission as a function of wavelength (the grating
  efficiency) changes with these different setups.  If the transmission
  function is given as an interpolation table this would require data files
  for each setup of each disperser.  The structure of <b>SPTIME</b> allows
  for this.
  </p>
  <p>
  However, it is also possible to specify the grating and spectrograph
  parameters and have the task predict the grating efficiency in any
  particular setup.  In many cases it may be easier to use the calculated
  efficiencies rather than measure them.  Depending on the level of accuracy
  desired this may be adequate or deviations from the analytic blaze function
  can be accounted for in another component.
  </p>
  <p>
  TABLES
  </p>
  <p>
  <b>SPTIME</b> uses text files to provide parameters and interpolation
  tables.  The files may contain comments, parameters, and tables.
  </p>
  <p>
  Comment lines begin with <span style="font-family: monospace;">'#'</span> and may contain any text.  They can occur
  anywhere in the file, though normally they are at the beginning of the file.
  </p>
  <p>
  Parameters are comment lines of the form
  </p>
  <div class="highlight-default-notranslate"><pre>
  # [parameter] = [value]
  </pre></div>
  <p>
  where whitespace is required between each field, [parameter] is a single
  word parameter name, and [value] is a single word value.  A quoted string
  is a single word so if the value field contains whitespace, such as in
  titles, it must be quoted.  Any text following the value is ignored and may
  be used for units (not read or used by the program) or comments.
  </p>
  <p>
  The parameters are those described in the PARAMETERS section.  The tables
  in which the parameters may be included are identified in that section
  in the square brackets.  Note that it is generally true that any parameter
  may appear in the spectrograph table.
  </p>
  <p>
  The table data is a multicolumn list of numeric values.  The list must be
  in increasing order in the independent columns.  Only 1D (two columns) and
  2D (three columns) tables are currently supported.  2D tables must form a
  regular grid.  This means that any particular value from column one must
  occur for all values of column 2 and vice versa.   The table is
  interpolated as needed.  The interpolation is linear or bi-linear.
  Extrapolation outside of the table consists of the taking the nearest
  value; thus, a single line may be used to define a constant value for all
  values of the independent variable(s).
  </p>
  <p>
  Normally the table values, the dependent variable in the last column, are
  in fractional transmission or DQE.  There is a special parameter,
  <span style="font-family: monospace;">"tablescale"</span>, which may be specified to multiply the dependent variable
  column.  This would mainly be used to provide tables in percent rather
  than fraction.
  </p>
  <p>
  The independent variable columns depend on the type of table.  Most tables
  are a function of wavelength.  Currently wavelengths must be in Angstroms.
  </p>
  <p>
  The types of tables and the units of the columns are listed below.
  </p>
  <div class="highlight-default-notranslate"><pre>
      spectrum - Angstroms ergs/s/cm^2/A
           sky - Angstroms ergs/s/cm^2/A/arcsec^2
    extinction - Angstroms mag/airmass
  spectrograph - Angstroms transmission
     telescope - Angstroms transmission
    emissivity - Angstroms emissivity
           adc - Angstroms transmission
         fiber - Angstroms transmission
    collimator - Angstroms transmission
        filter - Angstroms transmission
     disperser - Angstroms transmission
    xdisperser - Angstroms transmission
     corrector - Angstroms transmission
        camera - Angstroms transmission
      detector - Angstroms transmission
   sensitivity - Angstroms 2.5*(log(countrate)-log(flambda)),
  
           sky - Angstroms moonphase ergs/s/cm^2/A/arcsec^2
      aperture - diameter/FWHM transmission
      aperture - width/FWHM length/FWHM transmission
    vignetting - mm transmission
  </pre></div>
  <p>
  The disperser and crossdisperser files have an additional feature to allow
  for efficiency curves at different orders.  The parameter <span style="font-family: monospace;">"effN"</span> (or <span style="font-family: monospace;">"xeffN"</span>
  for crossdispersers), where N is the order, may be specified whose value is
  a separate table (or constant).  If there is no <span style="font-family: monospace;">"eff1/xeff1"</span> (efficiency in
  first order) then any efficiency table in the disperser table is used.  In
  other words, any table in the disperser file applies only to first order
  and only if there is no <span style="font-family: monospace;">"eff1/xeff1"</span> parameter defining a separate first
  order efficiency file.
  </p>
  <p>
  DISPERSION UNITS
  </p>
  <p>
  The output results, text file, and graphs are presented in dispersion
  units defined by the <i>units</i> parameter.  In addition the <i>wave</i>
  and <i>refwave</i> input parameters are specified in the selected units.
  All other dispersion values must currently be specified in Angstroms.
  </p>
  <p>
  The dispersion units are specified by strings having a unit type from the
  list below along with the possible preceding modifiers, <span style="font-family: monospace;">"inverse"</span>, to
  select the inverse of the unit and <span style="font-family: monospace;">"log"</span> to select logarithmic units. For
  example <span style="font-family: monospace;">"log angstroms"</span> to select the logarithm of wavelength in Angstroms
  and <span style="font-family: monospace;">"inv microns"</span> to select inverse microns.  The various identifiers may
  be abbreviated as words but the syntax is not sophisticated enough to
  recognize standard scientific abbreviations except for those given
  explicitly below.
  </p>
  <div class="highlight-default-notranslate"><pre>
     angstroms - Wavelength in Angstroms
    nanometers - Wavelength in nanometers
  millimicrons - Wavelength in millimicrons
       microns - Wavelength in microns
   millimeters - Wavelength in millimeters
    centimeter - Wavelength in centimeters
        meters - Wavelength in meters
         hertz - Frequency in hertz (cycles per second)
     kilohertz - Frequency in kilohertz
     megahertz - Frequency in megahertz
      gigahertz - Frequency in gigahertz
           m/s - Velocity in meters per second
          km/s - Velocity in kilometers per second
            ev - Energy in electron volts
           kev - Energy in kilo electron volts
           mev - Energy in mega electron volts
  
            nm - Wavelength in nanometers
            mm - Wavelength in millimeters
            cm - Wavelength in centimeters
             m - Wavelength in meters
            Hz - Frequency in hertz (cycles per second)
           KHz - Frequency in kilohertz
           MHz - Frequency in megahertz
           GHz - Frequency in gigahertz
            wn - Wave number (inverse centimeters)
  </pre></div>
  <p>
  The velocity units require a trailing value and unit defining the
  velocity zero point.  For example to transform to velocity relative to
  a wavelength of 1 micron the unit string would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  km/s 1 micron
  </pre></div>
  <p>
  CALCULATIONS
  </p>
  <p>
  This section describes the calculations, and assumptions behind the
  calculations, performed by <b>SPTIME</b>.  These include the dispersion and
  efficiencies of gratings and grisms, the dispersion resolution, the spatial
  resolution and how it applies to the number of object and sky pixels in the
  apertures, the object and sky detected photons/counts, the signal-to-noise
  ratio , and the exposure time for a given S/N.
  </p>
  <p>
  Gratings
  </p>
  <p>
  Gratings are assumed to tilted only around the axis parallel to the
  groves and with the incident angle greater than the blaze angle.  The
  grating equation is then
  </p>
  <div class="highlight-default-notranslate"><pre>
  g * m * w = sin(tilt+phi/2) + sin(beta)
  </pre></div>
  <p>
  where g is the number of groves per wavelength unit, m is the order, w is
  the wavelength, tilt is the grating tilt measured from the grating normal,
  phi is the angle between the incident and diffracted rays, and beta is the
  diffracted angle.  Phi is a spectrograph parameter and g is a grating
  parameter.  At the desired central wavelength beta is tilt-phi/2 and at the
  blaze peak it is 2*blaze-tilt-phi/2 where blaze is the blaze angle.
  </p>
  <p>
  The tilt is computed from the desired central wavelength.  It is
  also used to compute the grating magnification
  </p>
  <div class="highlight-default-notranslate"><pre>
  magnification = cos(tilt-phi/2) / cos(tilt+phi/2)
  </pre></div>
  <p>
  which is used in calculating the projected slit size at the detector.
  This number is less than zero so the aperture is actually demagnified.
  </p>
  <p>
  The dispersion, treated as constant over the spectrum for the sake of
  simplicity, is given by the derivative of the grating equation at
  the blaze peak,
  </p>
  <div class="highlight-default-notranslate"><pre>
  dispersion = cos(blaze-phi/2) / (g * m * f)
  </pre></div>
  <p>
  where f is the camera focal length.
  </p>
  <p>
  The grating efficiency or blaze function is computed as described by
  Schroeder and Hilliard (Applied Optics, vol 19, 1980, p. 2833).  The
  requirements on the grating noted previously correspond to their case A.
  As they show, use of incident angles less than the blaze angle, their case
  B, significantly degrades the efficiency due to back reflection which is
  why this case is not included.  The efficiency formulation includes
  variation in the peak efficiency due light diffracted into other orders,
  shadowing of the groves, and a reflectance parameter.  The reflectance
  parameter is basically the blaze peak normalization and does not currently
  include a wavelength dependence.  Thus the peak efficiency is near the
  reflectance value but somewhat lower and is order dependent due to the other
  effects.
  </p>
  <p>
  Grisms
  </p>
  <p>
  Grisms are assumed to have a prism angle equal to the blaze angle of
  the inscribed grating.  The index of refraction is treated as constant
  over the wavelength range of an order, though different index of refraction
  values can be specified for each order.
  </p>
  <p>
  The grism formula used is a variation on the grating equation.
  </p>
  <div class="highlight-default-notranslate"><pre>
  g * m * w = n * sin (theta+prism) - sin (beta+prism)
  </pre></div>
  <p>
  where n is the index of refraction, prism is the prism or blaze angle,
  theta is the incident angle relative to the prism face, and beta is the
  refracted angle relative to the prism face.  Theta and beta are defined so
  that at the undeviated wavelength they are zero.  In other words at the
  undeviated wavelength the light path is a straight through transmission.
  </p>
  <p>
  The efficiency is also computed in an analogous manner to the
  reflection grating except that shadowing is not included (a consequence of
  the blaze face being parallel to the prism face and theta being near
  zero).  Instead of a reflectance value normalizing the blaze function a
  transmission value is used.
  </p>
  <p>
  Scales and Sizes
  </p>
  <p>
  The scale between arc seconds on the sky and millimeters at the
  aperture(s) of the spectrograph is specified by the <i>scale</i> parameter.
  This parameter is used to convert aperture sizes between arc seconds and
  millimeters.
  </p>
  <p>
  The aperture sizes are magnified or demagnified by three possible factors.
  The basic magnification is given by the ratio of the collimator focal
  length to the camera focal length.  This magnification applies both along
  and across the dispersion.
  </p>
  <p>
  The camera focal length also determines the dispersion scale on the detector.
  It converts radians of dispersion to mm at the detector.
  </p>
  <p>
  For grating dispersers there is a demagnification along the dispersion
  due to the tilt of the grating(s).  The demagnification is computed (as
  given previously) from the grating parameters and the spectrograph
  parameter giving the angle between the incident and diffracted rays at the
  detector center.
  </p>
  <p>
  The last magnification factor is given by the spectrograph parameters
  <span style="font-family: monospace;">"apmagdisp"</span> and <span style="font-family: monospace;">"apxmagdisp"</span>.  These define magnifications of the aperture
  along and across the dispersion apart from the other two magnifications.
  These parameters are often missing which means no additional
  magnifications.
  </p>
  <p>
  One use for the last magnification parameters is to correct aperture
  sizes given as millimeters or arc seconds on a plane tilted with respect to
  the focal plane.  Such tilted apertures occur with aperture mechanisms
  (usually slits) that reflect light for acquisition and guiding.  Note that
  one only needs to use these terms if users are expected to define the
  apertures sizes on the tilted plane.  If instead the projection factors are
  handled by the spectrograph system and users specify aperture size as
  millimeters or arc seconds on the sky then these terms are not needed.
  </p>
  <p>
  The above scale factors map arc seconds on the sky and aperture sizes
  in millimeter to arc seconds and millimeters projected on the detector.  To
  convert to pixels on the detector requires the pixel size.
  One option in <b>SPTIME</b> is to specify aperture
  sizes as projected pixels on the detector (either in the user parameters or
  in the aperture description file).  Using the detector pixel size and the
  scale factors allows conversion of aperture sizes specified in this way
  back to the actual aperture size.
  </p>
  <p>
  Resolution
  </p>
  <p>
  A camera resolution parameter may be set in the camera description.  If
  a resolution value is not given it is taken to be 2 pixels.  This parameter
  is used to define the dispersion resolution element and the number of
  pixels across the dispersion imaged by the detector for the aperture and
  the object.  The latter usage is discussed in the next section.
  </p>
  <p>
  The dispersion resolution element, in pixels, is given by
  </p>
  <div class="highlight-default-notranslate"><pre>
                               |  2 pixels
  disp resolution = maximum of |  camera resolution
                               |  1 + min (seeing, apsize)
  </pre></div>
  <p>
  where seeing is the FWHM seeing diameter in pixels and apsize is the
  aperture size in pixels.  For circular apertures the aperture size is
  the diameter and for rectangular apertures it is the width.  The first term
  comes from sampling considerations, the second from the camera resolution,
  and the third from the finite resolution of a pixel (the factor of 1) and
  the spread of wavelengths across the aperture or seeing disk.  The
  dispersion resolution is printed for information and the S/N per dispersion
  resolution element is given in addition to the per pixel value.
  </p>
  <p>
  Object and Sky Pixels Across the Dispersion
  </p>
  <p>
  The number of pixels across the dispersion in the object and the sky
  are required to compute the S/N statistics.  The number of pixels
  in the projected aperture image is taken to be
  </p>
  <div class="highlight-default-notranslate"><pre>
                     | diameter + resolution  (circular apertures)
  aperture pixels =  |
                     | length + resolution    (rectangular apertures)
  </pre></div>
  <p>
  where resolution is the camera resolution discussed previously.  The value
  is rounded up to an integer.
  </p>
  <p>
  Objects are assumed to fill circular (fiber) apertures.  Therefore the
  number of object pixels is the same as the number of pixels in the
  aperture.  In rectangular (slit) apertures the number of object pixels is
  taken to be
  </p>
  <div class="highlight-default-notranslate"><pre>
                              | 3*seeing + resolution
  object pixels = minimum of  |
                              | number of aperture pixels
  </pre></div>
  <p>
  where seeing is the FWHM seeing diameter converted to pixels.  The values
  are rounded up to an integer.
  </p>
  <p>
  The number of sky pixels depends on the type of sky subtraction.
  For <span style="font-family: monospace;">"longslit"</span> sky subtraction the number of sky pixels is given
  by the difference of the number of aperture pixels and the number of
  object pixels.  For circular apertures this always comes out to zero so
  it does not make sense to use longslit sky subtraction.  For rectangular
  apertures the number of sky pixels in the aperture depends on the
  aperture size and the seeing.  If the number of sky pixels comes out to
  zero a warning is printed.
  </p>
  <p>
  For <span style="font-family: monospace;">"multiap"</span> sky subtraction the number of sky pixels is the
  number of sky apertures times the number of pixels per aperture.
  </p>
  <p>
  Source Counts
  </p>
  <p>
  The source spectrum flux at each wavelength, either given in a spectrum
  table or as a model distribution, is in units of
  photons per second per Angstrom per square centimeter.  This is multiplied
  by the telescope effective area, the exposure time, and the pixel size in
  Angstroms to give the source photons per dispersion pixel per exposure.
  This is then multiplied by any of the following terms that apply to arrive
  at the number of source photons detected over all spatial pixels.  The
  spatial integration is implicit in the aperture function.
  </p>
  <div class="highlight-default-notranslate"><pre>
  - the extinction using the specified airmass
  - the telescope transmission
  - the ADC transmission
  - the aperture transmission based on the aperture size relative
    to the seeing
  - the fiber transmission
  - the filter transmission (one or two filters)
  - the collimator transmission
  - the disperser efficiency (one or two dispersers)
  - the corrector transmission
  - the camera transmission
  - the detector DQE
  </pre></div>
  <p>
  Background Counts
  </p>
  <p>
  The sky or atmospheric background spectrum, if one is given, defines a
  photon flux per square arc second.  When it is given as a function of the
  moon phase it is interpolated to the specified moon phase.  In addition
  if a thermal temperature and an emissivity are given then a thermal
  background is computed and added to the sky/atmospheric background.
  </p>
  <p>
  The surface brightness of the background is multiplied by the area of the
  aperture occupied by the object (in arc seconds) and divided by the
  aperture transmission of the source.  This is the quantity reported in the
  output for the sky photon flux.  It is comparable to the source photon
  flux.
  </p>
  <p>
  Next this flux is multiplied by the telescope effective area, the
  exposure time, and the pixel size in Angstroms.  Finally it is multiplied
  by the same transmission terms as the object except for the extinction.
  Note that this removes the aperture transmission term included earlier
  giving the background photons as the number passing through the aperture per
  object profile.  The final value is the number of background photons from the
  object.  To get the background photons per spatial pixel the value is divided by
  the number of spatial pixels occupied by the source.
  </p>
  <p>
  If no background subtraction is specified then the background counts are added
  to the source counts to define the final source counts and the background
  counts are set to zero.
  </p>
  <p>
  Signal-to-Noise Ratio
  </p>
  <p>
  The noise attributed to the source and background is based on Poisson
  statistics; namely the noise is the square root of the number of photons.
  The detector noise is given by a dark count component and a readout noise
  component.  The noise from the dark counts is obtain by multiplying the
  dark count rate by the exposure time and the number of spatial pixels used
  in extracting the source and taking the square root.  The readout noise is
  the detector readout noise parameter multiplied by the square root of the
  number of spatial source pixels.
  </p>
  <p>
  If background subtraction is selected and the number of available
  background pixels is greater than zero then the uncertainty in the
  background estimation is computed.  The uncertainty in a single pixel is
  the square root of the background photons per pixel, the dark counts per
  pixel, and the readout noise per pixel.  This is divided by the square root
  of the number of background pixels to get the uncertainty in the background
  estimation for subtraction from the source.
  </p>
  <p>
  The total noise is the combination of the source, background, dark count,
  and readout noise values and the background subtraction uncertainty added
  in quadrature.
  </p>
  <p>
  The signal-to-noise ratio per pixel per exposure is the source counts
  divided by total noise.  This value is multiplied by the square root of
  number of pixels per resolution element to get the S/N per resolution
  element.  If multiple exposures are used to make up the total exposure time
  then the single exposure S/N is multiplied by the square root of the number
  of exposures.
  </p>
  <p>
  Exposure Time From Signal-to-Noise Ratio
  </p>
  <p>
  If no exposure time is specified, that is a value of INDEF, then
  the exposure time required to reach a desired signal-to-noise ratio
  per pixel is determined.  The computation is done at the specified central
  wavelength.  The task iterates, starting with the specified maximum time per
  exposure, by computing the S/N and adjusting the exposure time
  (possibly breaking the total exposure up into subexposures) until
  the computed S/N matches the desired S/N to 0.1%.
  </p>
  <p>
  In addition to breaking the exposure time into individual exposure less
  than the maximum per exposure, the task will break single exposures that
  exceed the specified saturation and maximum data number values at the
  reference wavelength.  If other wavelengths are then saturated or exceed
  the data maximum a warning is printed.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DISCUSSION'  -->
  

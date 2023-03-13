.. _mkechelle:

mkechelle: Make artificial 1D and 2D echelle spectra
====================================================

**Package: artdata**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkechelle images [clobber]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of echelle spectra to create or modify.
  </dd>
  </dl>
  <dl id="l_clobber">
  <dt><b>clobber (query)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clobber' Line='clobber (query)' -->
  <dd>If an existing image is specified the clobber query parameter is used.
  Normally the parameter is not specified on the command line so that
  a query will be made for each image which exists.  Putting a value
  on the command line permanently overrides the query.  This should be
  done if the task is run in the background.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = 512, nlines = 512, norders = 23</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = 512, nlines = 512, norders = 23' -->
  <dd>For two dimensional spectra these parameters define the number of columns
  and lines in the final image and the maximum number of orders (there may be
  orders falling outside the image).  The dispersion is along the columns
  which is the second or line axis (dispersion axis is 2) so the number of
  columns is the number of pixels across the dispersion and the number of
  lines is the number of pixels along the dispersion per order.
  The extracted format turns the number of lines into the number columns
  and the number of orders is the number of lines; i.e the image
  has the specified number of extracted orders, one per image line,
  with the number of pixels along the dispersion specified by the
  <i>nlines</i> parameter.  This is equivalent to what the <b>apextract</b>
  package would  produces for an extracted echelle format with an original
  dispersion axis of 2.  There is no check in this case for orders
  which might fall outside the two dimensional format; i.e. exactly
  the number of orders are created.
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">"Artificial Echelle Spectrum"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = "Artificial Echelle Spectrum"' -->
  <dd>Image title to be given to the spectra.  Maximum of 79 characters.
  </dd>
  </dl>
  <dl id="l_header">
  <dt><b>header = <span style="font-family: monospace;">"artdata$stdheader.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='header' Line='header = "artdata$stdheader.dat"' -->
  <dd>Image or header keyword data file.  If an image is given then the image
  header is copied.  If a file is given then the FITS format cards are
  copied.  The data file consists of lines in FITS format with leading
  whitespace ignored.  A FITS card must begin with an uppercase/numeric
  keyword.  Lines not beginning with a FITS keyword such as comments or lower
  case are ignored.  The user keyword output of <b>imheader</b> is an
  acceptable data file.  See <b>mkheader</b> for further information.
  </dd>
  </dl>
  <dl id="l_list">
  <dt><b>list = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='list' Line='list = no' -->
  <dd>List the grating/instrument parameters?
  </dd>
  </dl>
  <dl id="l_make">
  <dt><b>make = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='make' Line='make = yes' -->
  <dd>Make the artificial spectra?  This is set to no if only the grating
  parameter listing is desired.
  </dd>
  </dl>
  <dl id="l_comments">
  <dt><b>comments = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='comments' Line='comments = yes' -->
  <dd>Include comments recording task parameters in the image header?
  </dd>
  </dl>
  <p style="text-align:center">FORMAT PARAMETERS
  
  </p>
  <dl id="l_xc">
  <dt><b>xc = INDEF, yc = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xc' Line='xc = INDEF, yc = INDEF' -->
  <dd>The column and line position of the blaze peak in the reference order (see
  <i>order</i> parameter.  If INDEF then the middle of the dimension is used.
  This allows setting the image center relative to the center of the echelle
  pattern.  As with the number of lines and columns the interpretation of
  these numbers relative to the image created depends on whether the format
  is extracted or not.
  </dd>
  </dl>
  <dl id="l_pixsize">
  <dt><b>pixsize = 0.027</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixsize' Line='pixsize = 0.027' -->
  <dd>Pixel size in millimeters.  This is used to convert the focal length
  and dispersion to pixels.  If INDEF then these parameters are
  assumed to be in pixels.
  </dd>
  </dl>
  <dl id="l_profile">
  <dt><b>profile = <span style="font-family: monospace;">"gaussian"</span> (extracted|gaussian|slit)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='profile' Line='profile = "gaussian" (extracted|gaussian|slit)' -->
  <dd>The order profile across the dispersion.  If the value is <span style="font-family: monospace;">"extracted"</span>
  then an extracted echelle format spectrum is produced.  Otherwise a
  two dimensional format with a gaussian or slit profile is produced.
  See <b>mk2dspec</b> for a discussion of the profile functions.
  </dd>
  </dl>
  <dl id="l_width">
  <dt><b>width = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='width' Line='width = 5.' -->
  <dd>If two dimensional echelle images are selected this parameter specifies
  the order profile full width at half maximum in pixels.  See <b>mk2dspec</b>
  for a fuller discussion.
  </dd>
  </dl>
  <dl id="l_scattered">
  <dt><b>scattered = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scattered' Line='scattered = 0.' -->
  <dd>Scattered light peak flux per pixel.  A simple scattered light component
  may be included in the two dimensional format.  The scattered light has the
  blaze function shape of the central order along the dispersion and the
  crossdisperser blaze function shape across the dispersion with the peak
  value given by this parameter.  A value of zero indicates no scattered
  light component.
  </dd>
  </dl>
  <p style="text-align:center">GRATING PARAMETERS
  
  </p>
  <p>
  Any of the following parameters may be specified as INDEF.  The missing
  values are resolved using the grating equations described in the
  DESCRIPTION section.  If it is not possible to resolve all the grating
  parameters but the order, wavelength, and dispersion are specified
  then a linear dispersion function is used.  Also in this case the
  extracted format will include dispersion information.
  </p>
  <dl id="l_f">
  <dt><b>f = 590., cf = 590.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='f' Line='f = 590., cf = 590.' -->
  <dd>Echelle and crossdisperser focal lengths in millimeters (if <i>pixsize</i>
  is given) or pixels.  Technically it is defined by the equation x = f * tan
  (theta) where x is distance from the optical axis on the detector and theta
  is the diffraction angle; i.e. it converts angular measures to millimeters
  or pixels on the detector.  If the focal length is specified as INDEF  it
  may be computed from the dispersion, which is required in this case, and
  the other parameters.
  </dd>
  </dl>
  <dl id="l_gmm">
  <dt><b>gmm = 31.6, cgmm = 226.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gmm' Line='gmm = 31.6, cgmm = 226.' -->
  <dd>Echelle and crossdisperser grating grooves per millimeter.  If specified as
  INDEF it may be computed from the order, which is required in this case,
  and the other parameters.
  </dd>
  </dl>
  <dl id="l_blaze">
  <dt><b>blaze = 63., cblaze = 4.53</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blaze' Line='blaze = 63., cblaze = 4.53' -->
  <dd>Echelle and crossdisperser blaze angles in degrees.  It is always specified or printed as a positive
  angle relative to the grating normal.  If specified as INDEF it is
  computed from the other parameters.
  </dd>
  </dl>
  <dl id="l_theta">
  <dt><b>theta = 69., ctheta = -11.97</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='theta' Line='theta = 69., ctheta = -11.97' -->
  <dd>Echelle and crossdisperser angles of incidence in degrees.  The angle of
  incidence must be in the plane perpendicular to face of the grating.  The
  angle of incidence may be specified relative to the grating normal or the
  blaze angle though it is always printed relative to the grating normal.  To
  specify it relative to the blaze angle add 360 degrees; for example to have
  an angle of 15 degrees less than the blaze angle specify 360 - 15 = 345.
  If the angle of incidence is specified as INDEF it is computed from the
  other parameters.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 112</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 112' -->
  <dd>The central or reference echelle order for which the wavelength and
  dispersion are specified.  If specified as INDEF it will be computed from
  the grooves per mm, which is required in this case, and the other
  parameters.  In combination with the number of orders this defines the
  first and last orders.  The highest order is the central order plus
  the integer part of one half the number of orders.  However, the
  lowest order is constrained to be at least 1.  The
  reference order is also used in the definitions of <i>xc</i> and <i>yc</i>.
  </dd>
  </dl>
  <dl id="l_corder">
  <dt><b>corder = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='corder' Line='corder = 1' -->
  <dd>The crossdisperser order for which the crossdisperser blaze wavelength and
  dispersion are specified.  If specified as INDEF it will be computed from
  the grooves per mm, which is required in this case, and the other
  parameters.
  If the order is zero then the other grating parameters are ignored and a
  prism-like dispersion is used with the property that the order spacing is
  constant.  Specifically the dispersion varies as the inverse of the
  wavelength with the <i>cwavelength</i> and <i>cdispersion</i> defining the
  function.
  </dd>
  </dl>
  <dl id="l_wavelength">
  <dt><b>wavelength = 5007.49 cwavelength = 6700.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wavelength' Line='wavelength = 5007.49 cwavelength = 6700.' -->
  <dd>Echelle and crossdisperser blaze wavelengths in Angstroms at the reference
  orders.  If specified as INDEF it will be computed from the other parameters.
  </dd>
  </dl>
  <dl id="l_dispersion">
  <dt><b>dispersion = 2.61 cdispersion = 70.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispersion' Line='dispersion = 2.61 cdispersion = 70.' -->
  <dd>Echelle and crossdisperser blaze dispersions in Angstroms per millimeter
  (if <i>pixsize</i> is specified) or pixels.
  If specified as INDEF it will be computed from the focal length, which is
  required in this case, and the other parameters.
  </dd>
  </dl>
  <p style="text-align:center">SPECTRA PARAMETERS
  
  </p>
  <dl id="l_rv">
  <dt><b>rv = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rv' Line='rv = 0.' -->
  <dd>Radial velocity (km/s) or redshift, as selected by the parameter <i>z</i>,
  applied to line positions and continuum.  Velocities are converted to
  redshift using the relativistic relation 1+z = sqrt ((1+rv/c)/(1-rv/c)).
  Note the shift is not a shift in the dispersion parameters but in the
  underlying artificial spectrum.
  </dd>
  </dl>
  <dl id="l_z">
  <dt><b>z = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='z' Line='z = no' -->
  <dd>Is the velocity parameter a radial velocity or a redshift?
  </dd>
  </dl>
  <dl id="l_continuum">
  <dt><b>continuum = 1000.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='continuum' Line='continuum = 1000.' -->
  <dd>Continuum at the echelle blaze peak in the reference order.
  </dd>
  </dl>
  <dl id="l_temperature">
  <dt><b>temperature = 5700.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='temperature' Line='temperature = 5700.' -->
  <dd>Blackbody continuum temperature in Kelvin.  A value of 0 is used if
  no blackbody continuum is desired.  The intensity level is set by
  scaling to the continuum level at blaze peak reference point.
  </dd>
  </dl>
  <dl id="l_lines">
  <dt><b>lines = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lines' Line='lines = ""' -->
  <dd>List of spectral line files.  Spectral line files contain lines of rest
  wavelength, peak, and widths (see the DESCRIPTION section).
  The latter two parameters may be missing in which case they default to
  the task <i>peak</i> and <i>sigma</i> parameters.  If no file or a new
  (nonexistent) file is specified then a number of random lines given by the
  parameter <i>nlines</i> is generated.  If a new file name is specified then
  the lines generated are recorded in the file.  If the list of spectral
  line files is shorter than the list of input spectra, the last
  spectral line list file is reused.
  </dd>
  </dl>
  <dl id="l_nlines">
  <dt><b>nlines = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlines' Line='nlines = 0' -->
  <dd>If no spectral line file or a new file is specified then the task will
  generate this number of random spectral lines.  The rest wavelengths are
  uniformly random within the limits of the spectrum, the peaks are
  uniformly random between zero and the value of the <i>peak</i> parameter
  and the width is fixed at the value of the <i>sigma</i> parameter.
  If a redshift is applied the rest wavelengths are shifted and repeated
  periodically.
  </dd>
  </dl>
  <dl id="l_peak">
  <dt><b>peak = -0.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='peak' Line='peak = -0.5' -->
  <dd>The maximum spectral line peak value when generating random lines or
  when the peak is missing from the spectral line file.
  This value is relative to the continuum unless the continuum is zero.
  Negative values are absorption lines and positive values are emission lines.
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma' Line='sigma = 1.' -->
  <dd>The default line width as a gaussian sigma in Angstroms when generating
  random lines or when the width is missing from the spectral line file.
  </dd>
  </dl>
  <dl id="l_seed">
  <dt><b>seed = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='seed' Line='seed = 1' -->
  <dd>Random number seed.
  </dd>
  </dl>
  <p>
  PACKAGE PARAMETERS
  </p>
  <dl id="l_nxsub">
  <dt><b>nxsub = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxsub' Line='nxsub = 10' -->
  <dd>Number of pixel subsamples used in computing the gaussian spectral line
  profiles.
  </dd>
  </dl>
  <dl id="l_dynrange">
  <dt><b>dynrange = 100000.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dynrange' Line='dynrange = 100000.' -->
  <dd>The gaussian line profiles extend to infinity so a dynamic range, the ratio
  of the peak intensity to the cutoff intensity, is imposed to cutoff the
  profiles.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task creates or adds to artificial extracted (one dimensional
  <span style="font-family: monospace;">"echelle"</span> format) or two dimensional echelle spectra.  The input spectrum
  (before modification by the spectrograph model) may be a combination of
  doppler shifted blackbody or constant continuum and emission and absorption
  gaussian profile spectral lines.  The lines may have randomly selected
  parameters or be taken from an input file.  Note that the parameters and
  method is similar to the task <b>mk1dspec</b> except that the input line list
  cannot specify a profile type and only Gaussian profiles are currently
  allowed.  The input spectrum is then
  separated out into echelle orders and either recorded as extracted one
  dimensional orders or convolved with a spatial profile and crossdispersed
  into a two dimensional image.  The properties of the echelle grating,
  crossdisperser, and instrumental configuration are modeled described
  later.
  </p>
  <p>
  If an existing image is specified the <i>clobber</i> parameter is used
  to determine whether to add the generated artificial echelle spectrum
  to the image.  Generally the clobber parameter is not specified on the
  command line to cause a query with the image name to be made for
  each image which already exists.  However, it is possible to put
  the clobber parameter on the command line to eliminate the query.
  This is appropriate for running the task in the background.
  </p>
  <p>
  There is <i>no</i> checking for consistency with an existing image;
  i.e. that it is an echelle image, whether it is an extracted format
  or a two dimensional spectrum, and what it's wavelength and order
  coverage is.  The only thing that happens is that the <i>ncols</i>,
  <i>nlines</i>, and <i>norders</i> parameters are replaced by the appropriate
  dimensions of the image with the choice between <i>nlines</i> and
  <i>norders</i> made by the <i>profile</i> parameter (as discussed below)
  and not by the format of the image.
  </p>
  <p>
  The created spectra are two dimensional, real datatype, images.  A title
  may be given and a set of header keywords be added by specifying an image
  or data file with the <i>header</i> parameter (see also <b>mkheader</b>).  If
  a data file is specified lines beginning with FITS keywords are entered in
  the image header.  Leading whitespace is ignored and any lines beginning
  with words having lowercase and nonvalid FITS keyword characters are
  ignored.  In addition to this optional header, various parameters which
  occur during reduction of real echelle spectra, such a wavelength
  coordinates for extracted and dispersion corrected spectra, are added.
  Finally, comments may be added to the image header recording the task
  parameters and any information from the line file which are not line
  definitions.
  </p>
  <p>
  The creation of an artificial echelle spectra has three stages.  First a
  true spectrum is generated; i.e. the spectrum which arrives at the
  spectrograph.  The spectrum is then separated into orders and the
  dispersion and  blaze functions of the echelle and crossdisperser gratings
  (or crossdisperser prism) are applied.  Finally, if a two dimensional
  format is desired it is convolved by an spatial profile (either a gaussian
  or a broader slit-like profile) and the orders are placed as required by
  the crossdispersion relation.
  </p>
  <p>
  Generation of the model spectrum has three parts; defining a continuum,
  adding emission and absorption lines, and applying a doppler shift.  The
  continuum has two parameters; an intensity scale set by the <i>continuum</i>
  parameter and a shape set by the <i>temperature</i> parameter.  The
  intensity scale is set by defining the total, final, extracted intensity in
  a pixel at the blaze peak (rest) wavelength in the reference order; i.e. at
  the wavelength set by the <i>wavelength</i> parameter.  Note this means that
  the efficiency of the gratings at that wavelength is included.  The shape
  of the continuum may be either a blackbody if a positive temperature is
  specified or constant.
  </p>
  <p>
  Spectral lines are modeled by gaussian profiles of specified wavelength,
  peak, and sigma.  The lines are defined in a spectral line file or
  generated randomly.  A spectral line file consists of text lines giving
  rest wavelength, peak, and sigma.  The sigma or the sigma and peak may be
  absent in which case the parameters <i>sigma</i> and <i>peak</i> will be
  used.  If peak values are missing random values between zero and the
  <i>peak</i> value are generated.  Thus, a simple list of wavelengths or a
  list of wavelengths and peaks may be used.
  </p>
  <p>
  If no spectral line file is specified or a new (nonexistent) file is named
  then the number of random lines given by the parameter <i>nlines</i> is
  generated.  The rest wavelengths are uniformly random within the wavelength
  range of the spectrum and extend periodically outside this range in the
  case of an applied velocity shift, the peaks are uniformly random between
  zero and the <i>peak</i> parameter, and the widths are given by the
  <i>sigma</i> parameter.  If a new file is named then the parameters of the
  generated lines will be output.
  </p>
  <p>
  The peak values are taken relative to a positive continuum.  In other words
  the generated line profile is multiplied by the continuum (with a minimum
  of zero for fully saturated absorption lines).  If the continuum is less
  than or equal to zero, as in the case of an artificial arc spectrum or pure
  emission line spectrum, then the peak values are interpreted as absolute
  intensities.  Positive peak values produce emission lines and negative
  values produce absorption lines.  Odd results will occur if the continuum
  has both positive and zero or negative values.
  </p>
  <p>
  The width values are gaussian sigmas given in Angstroms.
  </p>
  <p>
  The underlying rest spectrum may be shifted.  This is used primarily for
  testing radial velocity measuring algorithms and is not intended as a
  complete model of redshift effects.  The observed wavelength coverage as
  defined by the grating parameters and number of orders is not changed by
  redshifting.  Input line wavelengths are specified at rest and then shifted
  into or out of the final spectrum.  To be realistic the line list should
  include wavelengths over a great enough range to cover all desired
  redshifts.  The peaks and sigma are also appropriately modified by a
  redshift.  As an example, if the redshift is 1 the lines will appear
  broader by a factor of 2 and the peaks will be down by a factor of 2 in
  order to maintain the same flux.
  </p>
  <p>
  The random line generation is complicated because one wants to have the
  same set of lines (for a given seed) observed at different redshifts.  What
  is done is that the specified number of random lines is generated within
  the observed wavelength interval taken at rest.  This set is then repeated
  periodical over all wavelengths.  A redshift will then shift these rest
  lines in to or out of the observed spectrum.  If the lines are output to a
  line file, they are given at rest.  <b>Note that this periodicity may be
  important in interpreting cross-correlation redshift tests for large shifts
  between template and object spectra.</b>
  </p>
  <p>
  The definitions of the continuum are also affected by a redshift.  The
  reference point for the continuum level and blackbody shape is the starting
  wavelength taken at rest.  Shifts will then modify the continuum level at
  the reference pixel appropriately.  In particular a large redshift will
  shift the blackbody in such a way that the flux is still given by the
  <i>continuum</i> parameter at the reference wavelength at rest.
  </p>
  <p>
  Once the input spectrum is defined it is modified by the effects of an
  echelle grating and crossdispersion.  This includes the dispersion relation
  between pixel and wavelength, the blaze response function of the gratings,
  and separation into orders.
  </p>
  <p>
  The primary reference for the model of the echelle grating (a
  crossdisperser grating also obeys this model) used in this task is <span style="font-family: monospace;">"Echelle
  efficiencies: theory and experiment"</span> by Schroeder and Hilliard in Applied
  Optics, Vol. 19, No. 16, 1980, p. 2833.  (The nomenclature below is similar
  to that paper except we use theta for alpha, their theta is theta - blaze,
  the reciprocal of the groove spacing which is the grooves per millimeter,
  and the dispersion per linear distance at the detector rather than per
  radian).  This task only treats the case where the incident beam is in the
  plane perpendicular to the grating face (gamma=0).  In this case the basic
  equation is
  </p>
  <div class="highlight-default-notranslate"><pre>
  (1)     m * lambda = (sin(theta) + sin(beta)) / g
  </pre></div>
  <p>
  where m is the order, lambda the wavelength, g the grooves per wavelength
  unit, theta the angle of incidence to the grating normal, and beta the
  angle of diffraction to the normal.  The diffraction angle relative to that
  of the blaze maximum, psi, is given by
  </p>
  <div class="highlight-default-notranslate"><pre>
  (2)     beta = psi + 2 * blaze - theta
  </pre></div>
  <p>
  where blaze is the blaze angle.  The diffraction angle psi is related to
  position on the detector, again measured from the blaze peak, by
  </p>
  <div class="highlight-default-notranslate"><pre>
  (3)     x = f / pixsize * tan(psi)
  </pre></div>
  <p>
  where f is the effective focal length (as defined by this equation) and
  pixsize is the pixel size in millimeters that converts the detector
  positions to pixels.  If a pixel size is not specified then f will be
  taken as being in pixels.
  </p>
  <p>
  The second basic equation is the diffraction pattern or blaze response
  given by
  </p>
  <div class="highlight-default-notranslate"><pre>
  (5)     I = I0 * (sin(delta) / delta) ** 2
  (6)     delta = 2 * pi / lambda * (cos(theta) / g) / cos(epsilon) *
                  sin(psi/2) * cos(epsilon-psi/2)
  (7)     epsilon = theta - blaze
  </pre></div>
  <p>
  where epsilon is the angle between the blaze angle and the angle of
  incidence (the theta of  Shroeder and Hilliard).  When theta = blaze, (6)
  simplifies to
  </p>
  <div class="highlight-default-notranslate"><pre>
  (6a)    delta = pi / lambda * (cos (blaze) / g) * sin (psi)
  </pre></div>
  <p>
  As discussed by Schroeder and Hilliard, the relative intensity at the blaze
  peak, I0, must be reduced by the fraction of light at the same wavelength
  as the blaze peak which is diffracted into other orders.  Furthermore at
  some diffraction angles the light is reflected off the second face of the
  grating giving a different effective diffraction angle to be used in (6).
  This computation is done by the task giving a variation in relative blaze
  response with order and reproducing the calculations of Schroeder and
  Hilliard.  The absolute normalization, including the crossdisperser blaze
  function if any, is such that the response at the blaze peak of the
  reference order is unity.  This insures that specified continuum level at
  the reference wavelength is produced.
  </p>
  <p>
  At the blaze maximum psi = x = 0 and the wavelength and dispersion per
  millimeter on the detector are given by (1) and the derivative of (1) with
  respect to x:
  </p>
  <div class="highlight-default-notranslate"><pre>
  (8)     wavelength = 1E7*(sin(theta)+sin(2*blaze-theta))/(gmm*order)
  (9)     dispersion = 1E7*cos(2*blaze-theta)/(gmm*order*f/pixsize)
  </pre></div>
  <p>
  The variable names are the same as the parameters in this task.   In
  particular, gmm is the echelle grooves per millimeter with the factors of
  1E7 (10 to the seventh power) to convert to Angstroms, the factor of f /
  pixsize to convert the dispersion to per pixel, and order is the reference
  order for the wavelength and dispersion.
  </p>
  <p>
  The <b>mkechelle</b> task provides different ways to define the parameters.
  If there is insufficient information to determine all the grating
  parameters but the wavelength, dispersion, order are specified then
  a simplified grating equation is used which is linear with pixel
  position.  The approximation is that tan(psi) = sin(psi) = psi so
  that
  </p>
  <div class="highlight-default-notranslate"><pre>
  (9)     lambda = (order * wavelength + dispersion * x) / m
                 = (a + b * x) / m
  (10)    delta  = pi * order * dispersion / lambda * x
                 =  c / lambda * x
  </pre></div>
  <p>
  Also in this case the extracted format (described later) includes
  wavelength information in the header so that the spectra appear as fully
  dispersion corrected.
  </p>
  <p>
  If there are at least five of the seven grating parameters specified
  then equations (8) and (9) are used to determine
  unspecified parameters or to override parameters if the equations are
  overspecified.  For example, suppose the grooves per millimeter is known
  but not the blaze angle or focal length.  Then the wavelength and
  dispersion at the reference order are used to compute these quantities.
  </p>
  <p>
  The full set of grating parameters derived and used to create the spectra
  are documented in the image header if the <i>comments</i> parameter is
  specified.  Also the <i>list</i> parameter may be set to print the grating
  parameters and the <i>make</i> parameter may be set to no to check the
  grating parameters without making the spectra.
  </p>
  <p>
  The crossdisperser grating parameters are treated exactly as above except,
  since only one order is used, the relative blaze efficiency is not
  computed.
  </p>
  <p>
  There is a variant on the crossdispersion to allow a prism-like separation
  of the echelle orders.  If the crossdispersion grating order, <i>corder</i>
  is set to zero then the other grating parameters are ignored and a
  prism-like dispersion is used with the property that the order spacing is
  constant.  Specifically the dispersion varies as the inverse of the
  wavelength with the <i>cwavelength</i> and <i>cdispersion</i> defining the
  function.  There is no crossdisperser blaze function in this case either;
  i.e. the relative intensities between orders is solely due to the echelle
  grating blaze response.
  </p>
  <p>
  There is an interesting effect which follows from the above equations but
  which is not obvious at first glance.  When the full grating equation is
  used the dispersion varies with wavelength.  This means the size of a pixel
  in wavelength varies and so the flux in a pixel changes.  The effect is
  such that the order intensity maximum shifts to the blue from the blaze peak
  because the pixel width in Angstroms increases to the blue faster, for a
  while, than the blaze response decreases.
  </p>
  <p>
  Once the spectrum has been separated into orders, modified by the
  grating blaze functions, and sampled into pixels in the dispersion
  direction it may be output as an extracted <span style="font-family: monospace;">"echelle"</span> format spectrum.
  This occurs when the spatial profile is specified as <span style="font-family: monospace;">"extracted"</span>.
  The keywords added by the <b>apextract</b> package are included in
  the image header.  If the dispersion model is linear
  the keywords are the same as those produced by the dispersion
  correction task <b>ecdispcor</b>.
  </p>
  <p>
  If the spatial profile is specified as <span style="font-family: monospace;">"gaussian"</span> or <span style="font-family: monospace;">"slit"</span> then the
  orders are convolved by the profile function and the crossdispersion
  relation is used to determine where the order falls at each wavelength.
  The spatial profiles are defined by the formulas:
  </p>
  <div class="highlight-default-notranslate"><pre>
  gaussian:   I(x) = exp (-ln(2) * (2*(x-xc(w))/width)**2)
      slit:   I(x) = exp (-ln(2) * (2*(x-xc(w))/width)**10)
  </pre></div>
  <p>
  where x is the spatial coordinate, xc(w) is the order center at
  wavelength w, and width is the full width at half maximum specified by
  the parameter of that name.  The <span style="font-family: monospace;">"gaussian"</span> profile
  is the usual gaussian specified in terms of a FWHM.  The <span style="font-family: monospace;">"slit"</span>
  profile is one which is relatively flat and then rapidly drops
  to zero.  The profile is normalized to unit integral so that
  the total flux across the profile is given by the scaled
  1D spectrum flux.  The profile is fully sampled and then binned to
  the pixel size to correctly include sampling effects as a function
  of where in a pixel the order center falls.
  </p>
  <p>
  Note that in this model the orders are always tilted with respect
  to the columns and constant wavelength is exactly aligned with the
  image lines.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create an absorption spectrum with blackbody continuum and scattered
  light using the default grating parameters then add noise.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkechelle ex1 nrand=100 scat=100.
  cl&gt; mknoise ex1 gain=2 rdnoise=5 poisson+
  </pre></div>
  <p>
  2. Create an arc spectrum using the line list noao$lib/onedstds/thorium.dat.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkechelle ex2 cont=10 temp=0 \
  lines=noao$lib/onedstds/thorium.dat peak=1000 sigma=.05
  </pre></div>
  <p>
  Note that the line intensities are random and not realistic.  The peak
  intensities range from 0 to 1000 times the continuum or 10000.
  </p>
  <p>
  3. Create an extracted version of example1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkechelle ex1.ec prof=extracted nrand=100 scat=100.
  cl&gt; mknoise ex1.ec gain=2 rdnoise=5 poisson+
  </pre></div>
  <p>
  Note that the noise is different and greater than would be the case with
  extracting the orders of example 1 because the noise is not summed
  over the order profile but is added after the fact.
  </p>
  <p>
  4. Create an extracted and dispersion corrected version of example1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkechelle ex1.ec prof=extracted nrand=100 scat=100. \
  gmm=INDEF blaze=INDEF theta=INDEF
  Echelle grating: Using linear dispersion
  Warning: Insufficient information to resolve grating parameters
  cl&gt; mknoise ex1.ec gain=2 rdnoise=5 poisson+
  </pre></div>
  <p>
  The warning is expected.  By not specifying all the parameters needed to
  fully model an echelle grating the default action is to use a linear
  dispersion in each order and to set the image header dispersion
  information.  When a complete grating model is specified, as in example 3,
  the extracted spectrum is not given dispersion information so that the
  nonlinear behavior of the dispersion can be applied by <b>ecidentify</b> and
  <b>dispcor</b>.  As with example 3, the noise is different since it is added
  after extraction and dispersion correction.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MKECHELLE">
  <dt><b>MKECHELLE V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MKECHELLE' Line='MKECHELLE V2.10.3' -->
  <dd>The task was updated to produce the current coordinate system format.
  </dd>
  </dl>
  </section>
  <section id="s_see_also_mknoise__mk1dspec__mk2dspec__mkheader__astutil_gratings">
  <h3>See also mknoise, mk1dspec, mk2dspec, mkheader, astutil.gratings</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO mknoise, mk1dspec, mk2dspec, mkheader, astutil.gratings'  -->
  

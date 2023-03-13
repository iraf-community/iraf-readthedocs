.. _mkobjects:

mkobjects: Make/add artificial stars and galaxies to 2D images
==============================================================

**Package: artdata**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkobjects input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Images to create or modify.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>Output images when modifying input images.  If no output images are
  given then existing images in the input list are modified directly.
  If an output image list is given then it must match in number the
  input list.
  </dd>
  </dl>
  <p>
  WHEN CREATING NEW IMAGES
  </p>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = ""' -->
  <dd>Image title to be given to the images.  Maximum of 79 characters.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = 512, nlines = 512</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = 512, nlines = 512' -->
  <dd>Number of columns and lines.
  </dd>
  </dl>
  <dl id="l_header">
  <dt><b>header = <span style="font-family: monospace;">"artdata$stdheader.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='header' Line='header = "artdata$stdheader.dat"' -->
  <dd>Image or header keyword data file.  If an image is given then the image header
  is copied.  If a file is given then the FITS format cards are copied.
  This only applies to new images.   The data file consists of lines
  in FITS format with leading whitespace ignored.  A FITS card must begin
  with an uppercase/numeric keyword.  Lines not beginning with a FITS
  keyword such as comments or lower case are ignored.  The user keyword
  output of <b>imheader</b> is an acceptable data file.  See <b>mkheader</b>
  for further information.
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background = 1000.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = 1000.' -->
  <dd>Default background and poisson noise background.  This is in data numbers
  with the conversion to photons determined by the <i>gain</i> parameter.
  </dd>
  </dl>
  <p>
  OBJECT PARAMETERS
  </p>
  <dl id="l_objects">
  <dt><b>objects = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='objects' Line='objects = ""' -->
  <dd>List of object files.  The number of object files must match the number of
  input images.  The object files contain lines of object coordinates,
  magnitudes, and shape parameters (see the DESCRIPTION section).
  </dd>
  </dl>
  <dl id="l_xoffset">
  <dt><b>xoffset = 0.,  yoffset = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xoffset' Line='xoffset = 0.,  yoffset = 0.' -->
  <dd>X and Y coordinate offset to be added to the object list coordinates.
  </dd>
  </dl>
  <dl id="l_star">
  <dt><b>star = <span style="font-family: monospace;">"moffat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='star' Line='star = "moffat"' -->
  <dd>Type of star and point spread function.  The choices are:
  <dl>
  <dt><b>gaussian</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='gaussian' Line='gaussian' -->
  <dd>An elliptical Gaussian profile with major axis half-intensity radius
  given by the parameter <i>radius</i>, axial ratio given by the parameter
  <i>ar</i>, and position angle given by the parameter <i>pa</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>moffat</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='moffat' Line='moffat' -->
  <dd>An elliptical Moffat profile with major axis half-intensity radius
  given by the parameter <i>radius</i>, model parameter <i>beta</i>,
  axial ratio given by the parameter <i>ar</i>, and position angle given
  by the parameter <i>pa</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>&lt;image&gt;</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='&lt;image&gt;' -->
  <dd>If not one of the profiles above, an image of the specified name is
  sought.  If found the center of the template image is assumed to be the
  center of the star/psf and the image template is scaled so that the
  radius of the template along the first axis is given by the <i>radius</i>
  parameter.  The axial ratio and position angle define an
  elliptical sampling of the template.
  </dd>
  </dl>
  <dl>
  <dt><b>&lt;profile file&gt;</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='&lt;profile file&gt;' -->
  <dd>If not one of the above, a text file is sought giving either an intensity
  per unit area profile or a cumulative flux profile from the center to the
  edge.  The two are differentiated by whether the first profile point is 0
  for a cumulative profile or nonzero for an intensity profile.  An intensity
  profile is recommended.  If found the profile defines an elliptical star/psf
  with the major axis radius to the last profile point given by the parameter
  <i>radius</i>, axial ratio given by the parameter <i>ar</i>, and position
  angle given by the parameter <i>pa</i>.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_radius">
  <dt><b>radius = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radius' Line='radius = 1.' -->
  <dd>Seeing radius/scale in pixels along the major axis.  For the <span style="font-family: monospace;">"gaussian"</span>
  and <span style="font-family: monospace;">"moffat"</span> profiles this is the half-intensity radius of the major
  axis, for image templates this is the template radius along the x dimension,
  specifically one half the number of columns, and for arbitrary user profiles
  this is the radius to the last profile point.
  </dd>
  </dl>
  <dl id="l_beta">
  <dt><b>beta = 2.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='beta' Line='beta = 2.5' -->
  <dd>Moffat model parameter.  See the DESCRIPTION for a definition of the
  Moffat profile.
  </dd>
  </dl>
  <dl id="l_ar">
  <dt><b>ar = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ar' Line='ar = 1.' -->
  <dd>Minor to major axial ratio for the star/psf.
  </dd>
  </dl>
  <dl id="l_pa">
  <dt><b>pa = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pa' Line='pa = 0.' -->
  <dd>Position angle in degrees measured counterclockwise from the X axis
  for the star/psf.
  </dd>
  </dl>
  <dl id="l_distance">
  <dt><b>distance = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='distance' Line='distance = 1.' -->
  <dd>Relative distance to be applied to the object list coordinates,
  magnitudes, and scale sizes.  This factor is divided into the
  object coordinates, after adding the offset factors, to allow expanding
  or contracting about any origin.  The magnitudes scale as the
  square of the distance and the sizes of the galaxies scale
  linearly.  This parameter allows changing image sizes and fluxes
  at a given seeing and sampling with one value.
  </dd>
  </dl>
  <dl id="l_exptime">
  <dt><b>exptime = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exptime' Line='exptime = 1.' -->
  <dd>Relative exposure time.  The object magnitudes and background
  level are scaled by this parameter.  This is comparable to changing the
  magnitude zero point except that it includes changing the background.
  </dd>
  </dl>
  <dl id="l_magzero">
  <dt><b>magzero = 7.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='magzero' Line='magzero = 7.' -->
  <dd>Magnitude zero point defining the conversion from magnitudes in the
  object list to instrumental/image fluxes.
  </dd>
  </dl>
  <p>
  NOISE PARAMETERS
  </p>
  <dl id="l_gain">
  <dt><b>gain = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gain' Line='gain = 1.' -->
  <dd>Gain in electrons per data number.  The gain is used for scaling the
  read noise parameter, the background, and in computing poisson noise.
  </dd>
  </dl>
  <dl id="l_rdnoise">
  <dt><b>rdnoise = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rdnoise' Line='rdnoise = 0.' -->
  <dd>Gaussian read noise in electrons.  For new images this applies to the
  entire image while for existing images this is added only to the objects.
  </dd>
  </dl>
  <dl id="l_poisson">
  <dt><b>poisson = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='poisson' Line='poisson = no' -->
  <dd>Add poisson photon noise?  For new images this applies to the entire image
  while for existing images this is only applied to the objects.  Note
  that in the latter case the background parameter is added before
  computing the new value and then subtracted again.
  </dd>
  </dl>
  <dl id="l_seed">
  <dt><b>seed = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='seed' Line='seed = 1' -->
  <dd>Random number seed.  If a value of <span style="font-family: monospace;">"INDEF"</span> is given then the clock
  time (integer seconds since 1980) is used as the seed yielding
  different random numbers for each execution.
  </dd>
  </dl>
  <dl id="l_comments">
  <dt><b>comments = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='comments' Line='comments = yes' -->
  <dd>Include comments recording task parameters in the image header?
  </dd>
  </dl>
  <p>
  PACKAGE PARAMETERS
  </p>
  <p>
  These parameters define certain computational shortcuts which greatly
  affect the computational speed.  They should be adjusted with care.
  </p>
  <dl id="l_nxc">
  <dt><b>nxc = 5, nyc = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxc' Line='nxc = 5, nyc = 5' -->
  <dd>Number of star and psf centers per pixel in X and Y.  Rather than evaluate
  stars and the psf convolution functions precisely at each subpixel
  coordinate, a set of templates with a grid of subpixel centers is
  computed and then the nearest template to the desired position is chosen.
  The larger the number the more memory and startup time required.
  </dd>
  </dl>
  <dl id="l_nxsub">
  <dt><b>nxsub = 10, nysub = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxsub' Line='nxsub = 10, nysub = 10' -->
  <dd>Number of pixel subsamples in X and Y used in computing the star and
  psf.  This is the subsampling in the central
  pixel and the number of subsamples decreases linearly from the center.
  The larger the numbers the longer it takes to compute the star and psf
  convolution templates.
  </dd>
  </dl>
  <dl id="l_nxgsub">
  <dt><b>nxgsub = 5, nygsub = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxgsub' Line='nxgsub = 5, nygsub = 5' -->
  <dd>Number of pixel subsamples in X and Y used in computing galaxy images.
  This is the subsampling in the central pixel and the number of
  subsamples decreases linearly from the center.  Because galaxy images
  are extended and each subsample is convolved by the psf convolution it
  need not be as finely sampled as the stars.  This is a critical
  parameter in the execution time if galaxies are being modeled.
  The larger the numbers the longer the execution time.
  </dd>
  </dl>
  <dl id="l_dynrange">
  <dt><b>dynrange = 100000., psfrange = 10.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dynrange' Line='dynrange = 100000., psfrange = 10.' -->
  <dd>The intensity profiles of the analytic functions extend to infinity so
  a dynamic range, the ratio of the peak intensity to the cutoff
  intensity, is imposed to cutoff the profiles.  The <i>dynrange</i>
  parameter applies to the stellar templates and to the galaxy profiles.
  The larger this parameter the further the profile extends.
  When modeling galaxies this has a fairly
  strong affect on the time (larger numbers means larger images and more
  execution time).  Only for very high signal-to-noise
  objects will the cutoff be noticeable.  A correction is made to
  the object magnitudes to reflect light lost by this cutoff.
  The psf convolution, used on galaxies, is generally not
  evaluated over as large a dynamic range, given by the parameter
  <i>psfrange</i>, especially since it has a very strong affect on the
  execution time.  The convolution is normalized to unit weight over the
  specified dynamic range.
  </dd>
  </dl>
  <dl id="l_ranbuf">
  <dt><b>ranbuf = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ranbuf' Line='ranbuf = 0' -->
  <dd>Random number buffer size.  When generating readout and poisson noise,
  evaluation of new random values has an affect on the execution time.
  If truly (or computationally truly) random numbers are not needed
  then this number of random values is stored and a simple
  uniform random number is used to select from the stored values.
  To force evaluation of new random values for every pixel set the
  value of this parameter to zero.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task creates or modifies images by adding models of astronomical
  objects, stars and galaxies, as specified in object lists.  New images are
  created with the specified dimensions, background, title, and real datatype.
  Existing images may be modified in place or new images output.  The
  task includes the effects of image scale, pixel sampling, atmospheric
  seeing, and noise.  The object models may be analytic one dimensional
  profiles, user defined one dimensional profiles, and user defined image
  templates.  The profiles and templates are given elliptical shapes by
  specifying a scale radius for the major axis, a minor axis to major
  axis axial ratio, and a position angle.
  </p>
  <p>
  For new images a set of header keywords may be added by specifying an
  image or data file with the <i>header</i> parameter (see also <b>mkheader</b>).
  If a data file is specified lines beginning with FITS keywords are
  entered in the image header.  Leading whitespace is ignored and any
  lines beginning with words having lowercase and nonvalid FITS keyword
  characters are ignored.  In addition to this optional header,
  keywords, parameters for the gain, read noise, and exposure time are
  defined.  Finally, comments may be added to the image header recording the task
  parameters and any information from the objects file which are not
  object definitions; in particular, the <b>starlist</b> and
  <b>gallist</b> parameters are recorded.
  </p>
  <p>
  A completely accurate simulation of the effects of pixel sampling,
  atmospheric seeing, object appearance, luminosity functions, and noise
  can require a large amount of computer time even on
  supercomputers.  This task is intended to allow generation of large
  numbers of objects and images over large image sizes representative of
  current deep optical astronomical images.  All this is to be done
  on typical workstations.  Thus, there are many approximations and
  subtle algorithms used to make this possible to as high a degree of
  accuracy as practical.  The discussion will try to describe these in
  sufficient detail for the user to judge the accuracy of the artificial
  data generated and understand the trade offs with many of the
  parameters.
  </p>
  <p>
  New images are created with the specified dimensions, title, and real
  datatype.  The images have a constant background value given by the
  <i>background</i> parameter (in data numbers) before adding objects and
  noise.  Noise consists of gaussian and poisson components.  For existing
  images, noise is only added to the objects and the background parameter is
  used in the calculation of the poisson noise: specifically, a poisson
  random value with mean given by the sum of the object and the background is
  generated and then the background is subtracted.  For more on how the noise
  is computed and approximations used see <b>mknoise</b>.
  </p>
  <p>
  Objects are specified by a position, magnitude, model, scale, axial
  ratio, and position angle.  Since the point spread function (PSF)
  is assumed constant over the image the star model, size, axial ratio,
  and position angle are specified by the task parameters <i>star</i>,
  <i>radius</i>, <i>ar</i>, and <i>pa</i>.  For galaxies, where the
  intrinsic shapes vary from object to object, these parameters are
  specified as part of the object lists.  For both types of objects the
  positions and magnitudes are specified in the object lists.
  </p>
  <p>
  There is a great deal of flexibility in defining the object models.
  The models are defined either in terms of a one dimensional radial
  intensity or cumulative flux profile
  or an image template.  The flux profiles may be
  analytic functions or a user defined profile given as an equally spaced
  set of values in a text file.  The first point is zero at the center
  for a cumulative profile
  and increases monotonically to the edge.  Note that intensity profiles
  are to be preferred to avoid artifacts in the conversion from cumulative
  flux.  In particular, cumulative flux profiles may give a spike at the
  center.  In either case, the profile should be specified fairly finely,
  many points, to avoid interpolation effects.
  </p>
  <p>
  The functional form of the analytic profiles the user profiles, and
  image template are given below.
  </p>
  <div class="highlight-default-notranslate"><pre>
        gaussian:  I = exp (-ln (2) * (R/radius)**2)
          moffat:  I = (1 + (2**(1/beta)-1) * (R/radius)**2) ** -beta
       sersic&lt;n&gt;:  I = exp (-b * (R/radius)**1/n)
         expdisk:  I = exp (-1.6783 * R/radius)
          devauc:  I = exp (-7.67 * (R/radius)**1/4)
    flux profile:  I = intensity (nprofile * R/radius)
    flux profile:  F = flux (nprofile * R/radius)
  image template:  I = image (nc/2+nc/2*dX/radius, nl/2+nc/2*dY/radius)
  </pre></div>
  <p>
  where R, dX, and dY are defined below, <i>radius</i> is the scale parameter
  and <i>beta</i> is the Moffat parameter specified by the user,
  nprofile is the number of profile points in the user profile, and nc and nl
  are the image template column and line dimensions.  The Gaussian, <span style="font-family: monospace;">"gaussian"</span>,
  and Moffat, <span style="font-family: monospace;">"moffat"</span>, profiles are used for stars and the point spread
  function, while the Sersic (sersic),  exponential disk (expdisk), and
  De Vaucouleurs (devauc) profiles are common models for spiral and elliptical
  galaxies.  The image templates are intended to model images with
  some complex structure.  The usual case is to have a very well sampled
  and high signal-to-noise image be reduced in scale (a more distant
  example), convolved with seeing (loss of detail), and noise (degraded
  signal-to-noise).  This also allows for more complex point spread
  functions.
  </p>
  <p>
  The radial profiles are mapped into two dimensional objects by an elliptical
  transformation.  The image templates are also mapped by an elliptical
  transformation to rotate and stretch them.  If the output image
  coordinates are given by (x, y), and the specified object center
  coordinates are given by (xc, yc) then the transformation is defined
  as shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  dx = x - xc
  dy = y - yc
  dX = dx * cos(pa) + dy * sin(pa)
  dY = (-dx * sin(pa) + dy * cos(pa)) / ar
  R = sqrt (dX ** 2 + dY ** 2)
  </pre></div>
  <p>
  where dx and dy are the object coordinates relative to the object
  center,  dX and dY are the object coordinates in the transformed
  circular coordinates, and R is the circularly symmetric radius.
  The transformation parameters are the axial ratio <i>ar</i>
  defined as the ratio of the minor axis to the major axis,
  and the position angle <i>pa</i> defined counterclockwise from
  the x axis.
  </p>
  <p>
  The <i>radius</i> parameter defines the size, in pixels, of the model
  object (before seeing for the galaxies) in the output image.  It
  consistently refers to the major axis of the object but its meaning
  does depend on the model.  For the gaussian and moffat profiles it is
  defined as the half-intensity radius.  For the sersic, expdisk, and devauc
  profiles it is defined as the half-flux radius.  For the user specified
  profiles it is the radius of the last profile point.  And for the image
  templates it is the radius of the image along the first or x axis given
  by one-half of the image dimension; i.e. nc/2.
  </p>
  <p>
  The profiles of the analytic functions extend to infinity so a dynamic
  range, the ratio of the peak intensity to the cutoff intensity, is imposed
  to cutoff the profiles.  The <i>dynrange</i> package parameter applies to
  the stellar and galaxy analytic profiles.  The larger this parameter the
  further the profile extends, particularly for the large index Sersic and De
  Vaucouleurs models.  When modeling large galaxies this has a fairly strong
  affect on the execution time because the overall extent of the images
  becomes rapidly greater.  Only for very high signal-to-noise objects will
  the cutoff be noticeable.  A correction is made to account for lost light
  (light beyond the modeled dynamic range) so that an aperture magnitude
  will give the correct value for an object of the specified total magnitude.
  This can become quite significant for larger index Sersic profiles and
  for the default dynamic range.
  </p>
  <p>
  The object models are integrated over the size of the image pixels.  This
  is done by subsampling, dividing up a pixel into smaller pieces called
  subpixels.  For the image templates a bilinear surface interpolation
  function is used and integrated analytically over the extent of the
  subpixels.  The user cumulative one dimensional profiles are first
  converted to intensity profiles.  The various intensity profiles are then
  binned into pixel fluxes per subpixel on a grid much finer than the
  subpixel spacing.  Then for any particular radius and object center the
  appropriate subpixel flux can be determined quickly and accurately.
  </p>
  <p>
  The number of subpixels per image pixel is determined by the package
  parameters <i>nxsub</i>, <i>nysub</i>, <i>nxgsub</i>, and <i>nygsub</i>.  The
  first two apply to the stars and the PSF and the latter two apply to the
  galaxies.  Typically the subsampling will be the same in each dimension.
  The galaxies are generally  subsampled less since they will have less
  rapidly changing profiles and are convolved by the PSF.  Also, the stars
  are computed only a few times and then scaled and moved, as described
  below, while each galaxy needs to be computed separately.  Therefore, one
  can afford greater precision in the stars than in the galaxies.
  </p>
  <p>
  Given an image of several hundred pixels subsampled by a factor of 100
  (10 x 10) this will be a very large number of computations.  A
  shortcut to reduce this number of operations is allow the number
  of subpixels to change as a function of distance from the
  profile center.  Since the profile center is where the intensity
  changes most rapidly with position, the greatest subsampling is needed for
  the pixel nearest the center.  Further from the object center the intensity
  changes more slowly and the number of subpixels may be reduced.
  Thus, the number of subpixels in each dimension in each pixel is
  decreased linearly with distance from the profile center.  For example,
  a pixel which is 3.2 pixels from the profile center will have
  <i>nxsub</i> - 3 subpixels in the x dimension.  There is, of course, a
  minimum of one subpixel per pixel or, in other words, no subsampling
  for the outer parts of the objects.  By adjusting the subsampling
  parameters one can set the degree of accuracy desired at the trade off of
  greatly different execution times.
  </p>
  <p>
  The star shapes are assumed constant over the images and only their
  position and magnitude change.  Thus, rather than compute each desired
  star from the model profile or image template, a normalized star
  template is computed once, using the spatial transformation and
  subsampling operations described above, and simply scaled each time to
  achieve the desired magnitude and added at the requested position.
  However, the apparent star shape does vary depending on where its
  center lies within an image pixel.  To handle this a set of
  normalized star templates is precomputed over a grid of centers
  relative to the center of a pixel.  Then the template with center
  nearest to that requested, relative to a pixel center, is used.  The
  number of such templates is set by the package parameters <i>nxc</i> and
  <i>nyc</i> where the two axis typically have the same values.  The
  larger the number of centers the more memory and startup time required
  but the better the representation of this sampling effect.  The choice
  also depends on the scale of the stars since the larger the star
  profile compared to a pixel the smaller the subcentering effect is.
  This technique allows generating images with many stars, such as a
  globular cluster or a low galactic latitude field, quite
  efficiently.
  </p>
  <p>
  Unlike the stars, the galaxies will each have different profiles,
  ellipticities, and position angles and so templates cannot be used (except
  for special test cases as mentioned later).  Another difference is that the
  galaxy models need to be convolved by the PSF; i.e. the shapes are defined
  prior to seeing.  The PSF convolution must also be subsampled and the
  convolution operation requires as many operations as the number of pixels
  in the PSF for each galaxy subpixel.  Thus, computing seeing convolved,
  well subsampled, large galaxy images is the most demanding task of all,
  requiring all the shortcuts described above (larger and variable
  subsampling and the subpixel flux approximation) as well as further ones.
  </p>
  <p>
  The PSF used for convolving galaxies is truncated at a lower dynamic
  range than the stars according to the package parameter
  <i>psfrange</i>.  This reduces the number of elements in the convolution
  dramatically at the expense of losing only a small amount of the flux
  in the wings.  Like the stars, the PSF is precomputed on a grid of
  pixel subcenters and the appropriate PSF template is used for each
  galaxy subpixel convolution.  Unlike the stars, the truncated PSF is
  normalized to unit flux in order to conserve the total flux in the
  galaxies.  For the extended galaxies this approximation has only a very
  small effect.  As with the other approximations one may increase the
  dynamic range of the PSF at the expense of an increase in execution
  time.
  </p>
  <p>
  There is an exception to using the truncated PSF.  If the size of the
  galaxy because very small, 0.01 pixel, then a stellar image is substituted.
  </p>
  <p>
  OBJECT FILES
  </p>
  <p>
  The object files contain lines defining stars and galaxies.  Stars
  are defined by three numbers and galaxies by seven or eight as
  represented symbolically below.
  </p>
  <div class="highlight-default-notranslate"><pre>
     stars:  xc yc magnitude
  galaxies:  xc yc magnitude model radius ar pa &lt;save&gt;
  </pre></div>
  <dl id="l_xc">
  <dt><b>xc, yc:</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='xc' Line='xc, yc:' -->
  <dd>Object center coordinates.  These coordinates are transformed to image
  coordinates as follows.
  <div class="highlight-default-notranslate"><pre>
  xc in image = xoffset + xc / distance
  yc in image = yoffset + yc / distance
  </pre></div>
  where <i>xoffset</i> and <i>yoffset</i> are the task offset parameters.
  Objects whose image centers fall outside the image dimensions are ignored.
  </dd>
  </dl>
  <dl id="l_magnitude">
  <dt><b>magnitude:</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='magnitude' Line='magnitude:' -->
  <dd>Object magnitude.  This is converted to instrumental fluxes as follows.
  <div class="highlight-default-notranslate"><pre>
  flux = exptime/distance**2 * 10**(-0.4*(magnitude-magzero))
  </pre></div>
  where <i>exptime</i>, <i>distance</i>, and <i>magzero</i> are task parameters.
  For the analytic star and galaxy models a correction
  is made for lost light due to the finite extent of the image in the
  sense that the flux added to the image will never quite be that
  requested.
  </dd>
  </dl>
  <dl id="l_model">
  <dt><b>model:</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='model' Line='model:' -->
  <dd>The types of galaxy models are as follows:
  <dl>
  <dt><b>sersic&lt;n&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='sersic' Line='sersic&lt;n&gt;' -->
  <dd>A Sersic model of index n.  The index may real but the value will be rounded
  to the nearest multiple of 0.5 or, equivalently, two times the index value will
  be rounded to an integer.  The index must be between 0.5 and 10.  The Sersic
  model defined as
  <div class="highlight-default-notranslate"><pre>
  I = exp (-b * (R/radius)**1/n)
  </pre></div>
  where radius is the major axis scale length corresponding to half of the
  total flux.  The value of b is computed using the formula of Ciotti and
  Bertin (AA v352, p447, 1999);
  <div class="highlight-default-notranslate"><pre>
  b = 2n - 1/3 + 4/(405n) + 46 / (25515n^2)
  </pre></div>
  </dd>
  </dl>
  <dl>
  <dt><b>expdisk</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='expdisk' Line='expdisk' -->
  <dd>An exponential disk model defined as
  <div class="highlight-default-notranslate"><pre>
  I = exp (-b * R/radius)
  </pre></div>
  where radius is the major axis scale length corresponding to half of the total
  flux and b is computed as with the Sersic model for n=1.  In fact, the
  algorithm is identical with that for the Sersic model using n=1.  Note that
  because of this there will be slight differences with the earlier versions.
  </dd>
  </dl>
  <dl>
  <dt><b>devauc</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='devauc' Line='devauc' -->
  <dd>A De Vaucouleurs profile defined as
  <div class="highlight-default-notranslate"><pre>
  I = exp (-b * (R/radius)**1/4)
  </pre></div>
  where radius is the major axis scale length corresponding to half of the total
  flux and b is computed as with the Sersic model for n=4.  In fact, the
  algorithm is identical with that for the Sersic model using n=4.  Note that
  because of this there will be slight differences with the earlier versions.
  </dd>
  </dl>
  <dl>
  <dt><b>&lt;image&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='&lt;image&gt;' -->
  <dd>If not one of the profiles above an image of the specified name is
  sought.  If found the center of the template image is assumed to be the
  center of the object and the image template is scaled so that the
  radius of the template is given by the major axis scale radius parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>&lt;profile file&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='&lt;profile file&gt;' -->
  <dd>If not one of the above a text file giving a cumulative flux profile from
  the center to the edge is sought.  If found the profile defines
  a model galaxy of extent to the last profile point given by
  the major axis scale radius parameter.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_radius">
  <dt><b>radius:</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='radius' Line='radius:' -->
  <dd>Major axis scale radius parameter in pixels as defined above for the different
  galaxy models.  The actual image radius is modified as follows.
  	radius in image = radius / distance
  </dd>
  </dl>
  <dl id="l_ar">
  <dt><b>ar:</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='ar' Line='ar:' -->
  <dd>Minor to major axis axial ratio.
  </dd>
  </dl>
  <dl id="l_pa">
  <dt><b>pa:</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='pa' Line='pa:' -->
  <dd>Major axis position angle in degrees measured counterclockwise from the X axis.
  </dd>
  </dl>
  <dl id="l_save">
  <dt><b>save:</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='save' Line='save:' -->
  <dd>If a large number of identically shaped galaxies (size, axial ratio,
  and position angle) located at the same subpixel (the same x and y
  fractional part) but with varying magnitudes is desired then by
  putting the word <span style="font-family: monospace;">"yes"</span> as the eighth field the model will be saved
  the first time and reused subsequent times.  This speeds up the execution.
  There may certain algorithm testing situations where this might be useful. 
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create a galaxy cluster with a power law distribution of field galaxies
  and stars as background/foreground.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ar&gt; gallist galaxies.dat 100 spatial=hubble lum=schecter egal=.8
  ar&gt; gallist galaxies.dat 500
  ar&gt; starlist galaxies.dat 100
  ar&gt; mkobjects galaxies obj=galaxies.dat gain=3 rdnoise=10 poisson+
  </pre></div>
  <p>
  Making the image takes about 5 minutes (2.5 min cpu) on a SPARCstation 1.
  </p>
  <p>
  2. Create a uniform artificial starfield of 5000 stars for a 512 square image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ar&gt; starlist starfield.dat 5000
  ar&gt; mkobjects starfield obj=starfield.dat gain=2 rdnoise=10 poisson+
  </pre></div>
  <p>
  This example takes about a minute on a SPARCstation 1.
  </p>
  <p>
  3. Create a globular cluster field of 5000 stars for a 512 square image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ar&gt; starlist gc.dat 5000 spat=hubble lum=bands
  ar&gt; mkobjects gc obj=gc.dat gain=2 rdnoise=10 poisson+
  </pre></div>
  <p>
  This example takes about a minute on a SPARCstation 1.
  </p>
  <p>
  4. Add stars to an existing image for test purposes.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ar&gt; mkobjects starfield obj=STDIN gain=2 pois+ magzero=30
  100 100 20
  100 200 21
  200 100 22
  200 200 23
  [EOF]
  </pre></div>
  <p>
  5. Look at the center of the globular cluster with no noise and very
  good seeing.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkobjects gc1 obj=gc.dat nc=400 nl=400 distance=.5 \
  &gt;&gt;&gt; xo=-313 yo=-313 radius=.1
  </pre></div>
  <p>
  The offset parameters are used to recenter the cluster from
  (256,256) in the data file to (200,200) in the expanded field.
  This example takes 30 sec (5 sec CPU) on a SPARCstation 1.  To expand
  and contract about a fixed point define the object list to have an
  origin at zero.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ar&gt; starlist gc.dat 5000 spat=hubble lum=bands xmin=-256 xmax=256 \
  &gt;&gt;&gt; ymin=-256 ymax=256
  ar&gt; mkobjects gc obj=gc.dat xo=257 yo=257 gain=2 rdnoise=10 poisson+
  ar&gt; mkobjects gc1 obj=gc.dat xo=257 yo=257 gain=2 \
  &gt;&gt;&gt; distance=.5 rdnoise=10 poisson+
  </pre></div>
  <p>
  6. Make an image of dev$pix at various distances and orientation.  First we
  must subtract the background.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imarith dev$pix - 38 pix
  cl&gt; mkobjects pix1 obj=STDIN nc=200 nl=200 back=1000 \
  &gt;&gt;&gt; magzero=30 rd=10 poi+
  50 50 15.0 pix 40 1 0
  150 50 15.6 pix 30 .8 45
  50 150 16.5 pix 20 .6 90
  150 150 17.1 pix 15 .4 135
  [EOF]
  </pre></div>
  <p>
  It would be somewhat more efficient to first block average the
  template since the oversampling in this case is very large.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MKOBJECTS">
  <dt><b>MKOBJECTS V2.11+</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MKOBJECTS' Line='MKOBJECTS V2.11+' -->
  <dd>The random number seed can be set from the clock time by using the value
  <span style="font-family: monospace;">"INDEF"</span> to yield different random numbers for each execution.
  </dd>
  </dl>
  <dl id="l_MKOBJECTS">
  <dt><b>MKOBJECTS V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MKOBJECTS' Line='MKOBJECTS V2.11' -->
  <dd>The default value of <span style="font-family: monospace;">"ranbuf"</span> was changed to zero.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  gallist, starlist, mknoise, mkheader
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

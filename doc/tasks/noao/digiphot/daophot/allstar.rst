.. _allstar:

allstar: Group and fit psf to multiple stars simultaneously
===========================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  allstar image photfile psfimage allstarfile rejfile subimage
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The list of images containing the stars to be fit.
  </dd>
  </dl>
  <dl id="l_photfile">
  <dt><b>photfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='photfile' Line='photfile' -->
  <dd>The input photometry files containing the initial estimates of the positions,
  sky values, and magnitudes of the stars to be fit. There must be one input
  photometry file for every input image.  If photfile is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>,
  or a directory specification, then ALLSTAR looks for a file with the name
  image.mag.? where ? is the highest existing version number. Photfile is usually
  the output of the DAOPHOT PHOT task but may also be the output of the PSF, PEAK
  and NSTAR tasks, or the ALLSTAR task itself.
  </dd>
  </dl>
  <dl id="l_psfimage">
  <dt><b>psfimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='psfimage' Line='psfimage' -->
  <dd>The list of images containing the PSF models computed by the DAOPHOT PSF task.
  The number of PSF images must be equal to the number of input images. If
  psfimage is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory specification, then PEAK
  will look for an image with the name image.psf.?, where ? is the highest
  existing version number.
  </dd>
  </dl>
  <dl id="l_allstarfile">
  <dt><b>allstarfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='allstarfile' Line='allstarfile' -->
  <dd>The list of output photometry files. There must be one output photometry
  file for every input image.  If allstarfile is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a
  directory specification, then ALLSTAR will write an output file with the name
  image.als.? where ? is the next available version number. Allstarfile is a text
  database if the DAOPHOT package parameter text is <span style="font-family: monospace;">"yes"</span>, an STSDAS table
  database if it is <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_rejfile">
  <dt><b>rejfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rejfile' Line='rejfile' -->
  <dd>The list of output rejected photometry files containing the positions and sky
  values of stars that could not be fit. If rejfile is undefined, results for all
  the stars in photfile are written to <i>allstarfile</i>, otherwise only the stars
  which were successfully fit are written to <i>allstarfile</i> and the remainder
  are written to rejfile. If rejfile is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory
  specification ALLSTAR writes an output file with the name image.als.? where ? is
  the next available version number. Otherwise rejfile must specify one output
  photometry file for every input image. Rejfile is a text database if the
  DAOPHOT package parameter <i>text</i> is <span style="font-family: monospace;">"yes"</span>, an STSDAS binary table database
  if it is <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_subimage">
  <dt><b>subimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subimage' Line='subimage' -->
  <dd>The list of output images with the fitted stars subtracted. There must be one
  subtracted image for every input image. If subimage is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>,
  or a directory specification, then ALLSTAR will create an image with the name
  image.sub.? where ? is the next available version number. Otherwise
  <i>subimage</i> must specify one output image for every image in <i>image</i>.
  </dd>
  </dl>
  <dl id="l_datapars">
  <dt><b>datapars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datapars' Line='datapars = ""' -->
  <dd>The name of the file containing the data dependent parameters. The parameters
  <i>scale</i>, <i>datamin</i>, and <i>datamax</i> are located here. If datapars
  is undefined then the default parameter set in uparm directory is used.
  </dd>
  </dl>
  <dl id="l_daopars">
  <dt><b>daopars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='daopars' Line='daopars = ""' -->
  <dd>The name of the file containing the daophot fitting parameters. The parameters
  <i>psfrad</i> and <i>fitrad</i> are located here. If <i>daopars</i> is undefined
  then the default parameter set in uparm directory is used.
  </dd>
  </dl>
  <dl id="l_wcsin">
  <dt><b>wcsin = <span style="font-family: monospace;">")_.wcsin"</span>, wcsout = <span style="font-family: monospace;">")_.wcsout"</span>, wcspsf = <span style="font-family: monospace;">")_.wcspsf"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcsin' Line='wcsin = ")_.wcsin", wcsout = ")_.wcsout", wcspsf = ")_.wcspsf"' -->
  <dd>The coordinate system of the input coordinates read from <i>photfile</i>, of the
  psf model <i>psfimage</i>, and of the output coordinates written to
  <i>allstarfile</i> and <i>rejfile</i> respectively. The image header coordinate
  system is used to transform from the input coordinate system to the <span style="font-family: monospace;">"logical"</span>
  pixel coordinate system used internally, from the internal logical system to
  the PSF model system, and from the internal <span style="font-family: monospace;">"logical"</span> pixel coordinate system
  to the output coordinate system. The input coordinate system options are
  <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, <span style="font-family: monospace;">"physical"</span>, and <span style="font-family: monospace;">"world"</span>. The PSF model and output coordinate
  system options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, and <span style="font-family: monospace;">"physical"</span>. The image cursor coordinate
  system is assumed to be the <span style="font-family: monospace;">"tv"</span> system.
  <dl>
  <dt><b>logical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='logical' Line='logical' -->
  <dd>Logical coordinates are pixel coordinates relative to the current image.
  The  logical coordinate system is the coordinate system used by the image
  input/output routines to access the image data on disk. In the logical
  coordinate system the coordinates of the first pixel of a  2D image, e.g.
  dev$ypix  and a 2D image section, e.g. dev$ypix[200:300,200:300] are
  always (1,1).
  </dd>
  </dl>
  <dl>
  <dt><b>tv</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='tv' Line='tv' -->
  <dd>Tv coordinates are the pixel coordinates used by the display servers. Tv
  coordinates  include  the effects of any input image section, but do not
  include the effects of previous linear transformations. If the input
  image name does not include an image section, then tv coordinates are
  identical to logical coordinates.  If the input image name does include a
  section, and the input image has not been linearly transformed or copied from
  a parent image, tv coordinates are identical to physical coordinates.
  In the tv coordinate system the coordinates of the first pixel of a
  2D image, e.g. dev$ypix and a 2D image section, e.g. dev$ypix[200:300,200:300]
  are (1,1) and (200,200) respectively.
  </dd>
  </dl>
  <dl>
  <dt><b>physical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='physical' Line='physical' -->
  <dd>Physical coordinates are pixel coordinates invariant  with respect to linear
  transformations of the physical image data.  For example, if the current image
  was created by extracting a section of another image,  the  physical
  coordinates of an object in the current image will be equal to the physical
  coordinates of the same object in the parent image,  although the logical
  coordinates will be different.  In the physical coordinate system the
  coordinates of the first pixel of a 2D image, e.g. dev$ypix and a 2D
  image section, e.g. dev$ypix[200:300,200:300] are (1,1) and (200,200)
  respectively.
  </dd>
  </dl>
  <dl>
  <dt><b>world</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='world' Line='world' -->
  <dd>World coordinates are image coordinates in any units which are invariant
  with respect to linear transformations of the physical image data. For
  example, the ra and dec of an object will always be the same no matter
  how the image is linearly transformed. The units of input world coordinates
  must be the same as those expected by the image header wcs, e. g.
  degrees and degrees for celestial coordinate systems.
  </dd>
  </dl>
  The wcsin, wcspsf, and wcsout parameters default to the values of the package
  parameters of the same name. The default values of the package parameters
  wcsin, wcspsf,  and wcsout are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"physical"</span> and <span style="font-family: monospace;">"logical"</span> respectively.
  </dd>
  </dl>
  <dl id="l_cache">
  <dt><b>cache = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cache' Line='cache = yes' -->
  <dd>Cache all the data in memory ? If <i>cache</i> is <span style="font-family: monospace;">"yes"</span>, then ALLSTAR attempts
  to preallocate sufficient space to store the input image plus the two
  image-sized working arrays it requires, plus space for the starlist, in memory.
  This can significantly reduce the total execution time. Users should however
  beware of creating a situation where excessive paging occurs.  If <i>cache</i> =
  <span style="font-family: monospace;">"no"</span>, ALLSTAR operates on subrasters containing the group currently being
  reduced, and writes the intermediate results to temporary scratch images. This
  option will work on any-sized image (unless a single group becomes the size of
  the entire image!) but can become slow of there are a large number of disk
  accesses. Users may wish to experiment to see which mode of operation suits
  their system best.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = <span style="font-family: monospace;">")_.verbose"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = ")_.verbose"' -->
  <dd>Print messages about the progress of the task ? Verbose can be set to the
  DAOPHOT package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = <span style="font-family: monospace;">")_.verify"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = ")_.verify"' -->
  <dd>Verify the critical ALLSTAR task parameters. Verify can be set to the daophot
  package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = <span style="font-family: monospace;">")_.update"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = ")_.update"' -->
  <dd>Update the critical ALLSTAR task parameters if <i>verify</i> = <span style="font-family: monospace;">"yes"</span>.  Update
  can be set to the daophot package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or
  <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  ALLSTAR computes x and y centers, sky values, and magnitudes for the stars in
  <i>photfile</i> by fitting the PSF <i>psfimage</i> to groups of stars in the IRAF
  image  <i>image</i>. Initial estimates of the centers, sky values, and
  magnitudes, are read from the photometry list <i>photfile</i>. ALLSTAR groups
  the stars dynamically, performing a regrouping operation after every iteration.
  The new computed centers, sky values, and magnitudes are written to
  <i>allstarfile</i> along with the number of iterations it took to fit the
  star, the goodness of fit statistic chi, and the image sharpness statistic
  sharp. If <i>rejfile</i> is not null (<span style="font-family: monospace;">""</span>), only stars that are successfully fit
  are written to <i>allstarfile</i>, and the remainder are written to
  <i>rejfile</i>. Otherwise all the stars are written to <i>allstarfile</i>.
  <i>Allstarfile</i> and <i>rejfile</i> are text databases if the DAOPHOT package
  parameter <i>text</i> is <span style="font-family: monospace;">"yes"</span>, STSDAS table databases if it is <span style="font-family: monospace;">"no"</span>. An image
  with all the fitted stars subtracted out is written to <i>subimage</i>. In
  effect ALLSTAR performs the combined operations of GROUP, GRPSELECT, NSTAR,
  and SUBSTAR.
  </p>
  <p>
  The coordinates read from <i>photfile</i> are assumed to be in coordinate
  system defined by <i>wcsin</i>. The options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, <span style="font-family: monospace;">"physical"</span>,
  and <span style="font-family: monospace;">"world"</span> and the transformation from the input coordinate system to the
  internal <span style="font-family: monospace;">"logical"</span> system is defined by the image coordinate system. The
  simplest default is the <span style="font-family: monospace;">"logical"</span> pixel system. Users working on with image
  sections but importing pixel coordinate lists generated from the parent image
  must use the <span style="font-family: monospace;">"tv"</span> or <span style="font-family: monospace;">"physical"</span> input coordinate systems.
  </p>
  <p>
  The coordinate system of the PSF model is the coordinate system defined by the
  <i>wcspsf</i> parameter. Normally the PSF model was derived from the input image
  and this parameter default to <span style="font-family: monospace;">"logical"</span>. However if the PSF model was derived
  from a larger image which is a <span style="font-family: monospace;">"parent"</span> of the input image, then wcspsf should
  be set to <span style="font-family: monospace;">"tv"</span> or <span style="font-family: monospace;">"physical"</span> depending on the circumstances.
  </p>
  <p>
  The coordinates written to <i>allstarfile</i> and <i>rejfile</i> are in the
  coordinate system defined by <i>wcsout</i>. The options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, and
  <span style="font-family: monospace;">"physical"</span>. The simplest default is the <span style="font-family: monospace;">"logical"</span> system.  Users wishing to
  correlate the output coordinates of objects measured in image sections or
  mosaic pieces with coordinates in the parent image must use the <span style="font-family: monospace;">"tv"</span> or
  <span style="font-family: monospace;">"physical"</span> coordinate systems.
  </p>
  <p>
  By default ALLSTAR computes new centers for all the stars in <i>photfile</i>.
  However if the DAOPARS parameter <i>recenter</i> is <span style="font-family: monospace;">"no"</span>, ALLSTAR assumes that
  the x and y centers in <i>photfile</i> are the true centers and does not refit
  them. This option can be quite useful in cases where accurate center values
  have been derived from an image that has been through some non-linear image
  restoration algorithm, but the photometry must be derived from the original
  unrestored image.
  </p>
  <p>
  By default (<i>groupsky</i> = <span style="font-family: monospace;">"yes"</span>) ALLSTAR computes the sky value for each
  group by averaging the individual sky values in <i>photfile</i> for all the
  stars in the group. If <i>groupsky</i> = <span style="font-family: monospace;">"no"</span>, the sky value for each pixel
  which contributes to the group fit is set equal to the mean of the sky values
  for those stars for which the pixel falls within one fitting radius.  If the
  DAOPARS parameter <i>fitksy</i> is <span style="font-family: monospace;">"yes"</span>, then ALLSTAR recomputes the individual
  sky values before averaging over the group, by, every third iteration,
  subtracting off the current best fit for the star and using the pixel values in
  the annulus defined by the DAOPARS parameters <i>sannulus</i> and <i>wsannulus</i>
  to recompute the sky. The actual sky recomputation is done by averaging forty
  percent of the sky pixels centered on the median of the distribution.
  Recomputing the sky can significantly reduce the scatter in the magnitudes in
  regions where the sky background is varying rapidly.
  </p>
  <p>
  Only pixels within the good data range defined by the DATAPARS task parameters
  <i>datamin</i> and <i>datamax</i> are included in the fit.  Most users set
  <i>datamin</i> and <i>datamax</i> so as to exclude pixels outside the linearity
  regime of the detector. By default all the data is fit.  Users are advised to
  determine accurate values for these parameters for their detector and set the
  values in DATAPARS before beginning any DAOPHOT reductions.
  </p>
  <p>
  Only pixels within the fitting radius parameter <i>fitrad</i> / <i>scale</i> are
  included in the fit for each star. <i>Fitrad</i> is located in the DAOPARS task
  and <i>scale</i> is located in the DATAPARS task. Since the non-linear
  least-squares fits normally compute three unknowns, the x and y position of
  the star's centroid and its brightness, the value of <i>fitrad</i>  must be
  sufficiently large to include at least three pixels in the fit for each star.
  To accelerate the convergence of the non-linear least-squares fitting algorithm
  pixels within <i>fitrad</i> are assigned weights which are  inversely
  proportional to the radial distance of the pixel from the x and y centroid of
  the star, falling from a maximum at the centroid to zero at the fitting radius.
  <i>Fitrad</i> must be sufficiently large to include at least three pixels with
  non-zero radial weights in the fit for each star. ALLSTAR arbitrarily imposes a
  minimum number of good pixels limit of four. Values of <i>fitrad</i> close to
  the full-width at half-maxima of the PSF are recommended.
  </p>
  <p>
  ALLSTAR computes a weighted fit to the PSF. The weight of each pixel is
  computed by combining, the radial weighting function described above, with
  weights derived from the random errors ALLSTAR predicts based on the detector
  noise characteristics specified by the DATAPARS parameters <i>readnoise</i> and
  <i>epadu</i>, and the flat-fielding and profile interpolation errors specified
  by the DAOPARS task <i>flaterr</i> and <i>proferr</i> parameters. Both to obtain
  optimal fits, and because ALLSTAR employs a conservative formula for reducing
  the weights of deviant pixels (parametrized by the <i>clipexp</i> and
  <i>cliprange</i> parameters in the DAOPARS task) which do not approach the model
  as the fit proceeds, which depends on <i>readnoise</i>,  <i>epadu</i>,
  <i>flaterr</i>, and <i>proferr</i>, users are strongly advised to determine those
  parameters accurately and to enter their values in DATAPARS and DAOPARS before
  beginning any DAOPHOT reductions.
  </p>
  <p>
  By default for each group of stars to be fit during each iteration, ALLSTAR
  extracts a subraster from <i>image</i> which extends approximately <i>fitrad</i>
  / <i>scale</i> + 1 pixels wide past the limiting values of x and y coordinates
  of the stars in the group. <i>Fitrad</i> is the fitting radius specified in the
  DAOPARS task. <i>Scale</i> is the image scale specified by the DATAPARS task.
  <i>Fitrad</i> may be less than or equal to but can never exceed the value of the
  image header parameter <span style="font-family: monospace;">"PSFRAD"</span> in <i>psfimage</i>.
  </p>
  <p>
  If the <i>cache</i> parameter is set to <span style="font-family: monospace;">"yes"</span> then ALLSTAR attempts to store all
  the vectors and arrays in memory.  This can significantly reduce the system
  overhead but may cause excessive paging on machines with a small amount of
  memory. For large images it may be necessary to set <i>cache</i> to <span style="font-family: monospace;">"no"</span>, and
  use the disk for scratch storage. Users should experiment to see what suits
  them best.
  </p>
  <p>
  As well as the computed x and y centers, sky values, and magnitudes, ALLSTAR
  outputs the number of times the PSF fit had to be iterated before convergence
  was achieved. The minimum number of iterations is four. The maximum number of
  iteration permitted is specified by the <i>maxiter</i> parameter in the DAOPARS
  task. Obviously the results for stars which have reached the maximum iteration
  count should be viewed with suspicion. However since the convergence criteria
  are quite strict, (the computed magnitude must change  by less than .0005
  magnitudes or 0.10 sigma whichever is larger and the x and y centroids must
  change by less than 0.002 pixels from one iteration to the next), even these
  stars may be reasonably well measured.
  </p>
  <p>
  ALLSTAR computes a goodness of fit statistic chi which is essentially the ratio
  of the observed pixel-to-pixel scatter in the fitting residuals to the expected
  scatter. Since the expected scatter is dependent on the DATAPARS task parameters
  <i>readnoise</i> and <i>epadu</i>, and the DAOPARS parameters <i>flaterr</i> and
  <i>proferr</i>, it is important for these values to be set correctly. A plot of
  chi versus magnitude should scatter around unity with little or no trend in chi
  with magnitude, except at the bright end where saturation effects may be
  present.
  </p>
  <p>
  Finally ALLSTAR computes the statistic sharp which estimates the intrinsic
  angular size of the measured object outside the atmosphere.  Sharp is roughly
  defined as the difference between the square of the width of the object and the
  square of the width of PSF. Sharp has values close to zero for single stars,
  large positive values for blended doubles and partially resolved galaxies and
  large negative values for cosmic rays and blemishes.
  </p>
  <p>
  ALLSTAR implements a sophisticated star rejection algorithm. First of all any
  group of stars which is more than a certain size is not reduced. This maximum
  group size is specified by the <i>maxgroup</i> parameter in the DAOPARS task.
  Large groups may run into numerical precision problems during the fits, so
  users should increase this parameter with caution.  ALLSTAR however, in
  contrast to NSTAR, attempts to subdivide large groups. If the group is too
  dense to reduce in size, ALLSTAR throws out the faintest star in the group
  and tries to rereduce it.  If two stars in a group have centroids separated
  by a critical distance currently set arbitrarily to 0.37 * the FWHM of the
  stellar core and their photocentric position and combined magnitude is assigned
  to the brighter of the two and the fainter is eliminated. Any star which
  converges to magnitude  12.5 magnitudes greater than the magnitude of the PSF
  is considered to be non-existent and eliminated from the group.
  </p>
  <p>
  After iteration 5, if the faintest star in the group has a brightness less
  than one sigma above zero it is eliminated.  After iteration 10 if the faintest
  star in the group has a brightness less than 1.5 sigma above zero it is
  eliminated. After iteration 15, or whenever the solutions has converged
  whichever comes first, if the faintest star in the group has a brightness less
  than 2.0 sigma above zero it is eliminated. After iterations 5, 10 and 15 if
  two stars are separated by more than 0.37 * FWHM and less than 1.0 * FWHM and
  if the fainter of the two is more uncertain than 1.0, 1.5 or 2.0 sigma
  respectively the fainter one is eliminated.
  </p>
  <p>
  ALLSTAR replaces the functionality of the GROUP, GRPSELECT, NSTAR and SUBSTAR
  task. However the user has little control over the grouping process and does
  not know at the end which stars were fit together. The grouping process is
  dynamic, as the groups are recomputed after each iteration, and stars can be
  fit and leave the group at any point after the fourth iteration. Therefore the
  quality of the fits may vary over the image as a function of crowding in an
  unknown way. However ALLSTAR is in most cases the routine of choice.  NSTAR
  is the task of choice when a user wants to maintain control over the
  composition of the stellar groups.
  </p>
  </section>
  <section id="s_output">
  <h3>Output</h3>
  <p>
  If <i>verbose</i> = yes, a single line is output to the terminal for each star
  fit or rejected. Full output is written to <i>allstarfile</i> and <i>rejfile</i>.
  At the beginning of these two files a header listing the current values of the
  parameters is written. For each star fit/rejected the following quantities are
  written to the output file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  id  xcenter  ycenter  mag  merr  msky  niter  sharpness  chi
      pier  perr
  </pre></div>
  <p>
  Id is the id number of the star. Xcenter and ycenter are the fitted coordinates
  in pixels. Mag and merr are the fitted magnitude and magnitude error
  respectively. Msky is the individual sky value for the star. Niter is the
  number of iterations it took to fit the star and sharpness and chi are the
  sharpness and goodness of fit statistic respectively.  Pier and perror are the
  photometry error code and accompanying error message respectively.
  </p>
  </section>
  <section id="s_errors">
  <h3>Errors</h3>
  <p>
  If no errors occur during the fitting process then pier is 0. Non-zero
  values of pier flag the following error conditions.
  </p>
  <div class="highlight-default-notranslate"><pre>
  0               # No error
  1               # The star is in a group too large to fit
  2               # The sky is undefined
  3               # There are too few good pixels to fit the star
  4               # The fit is singular
  5               # The star is too faint
  6               # The star has merged with a brighter star
  7               # The star is off the image
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Fit the PSF to a list stars in the test image dev$ypix. Good stars for
  making the PSF model can be found at (442,410), (348,189), and (379,67).
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; datapars.epadu = 14.0
  da&gt; datapars.readnoise = 75.0
  
      ... set the gain and readout noise for the detector
  
  da&gt; daofind dev$ypix default fwhmpsf=2.5 sigma=5.0 threshold=20.0
  
       ... answer verify prompts
  
       ... find stars in the image
  
       ... answer will appear in ypix.coo.1
  
   da&gt; phot dev$ypix default default annulus=10. dannulus=5.       \
       apertures = 3.0
  
       ... answer verify prompts
  
       ... do aperture photometry on the detected stars
  
       ... answer will appear in ypix.mag.1
  
   da&gt; display dev$ypix 1
  
   da&gt; psf dev$ypix default "" default default default psfrad=11.0 \
       fitrad=3.0 mkstars=yes display=imdr
  
       ... verify the critical parameters
  
       ... move the image cursor to a candidate star and hit the a key,
           a plot of the stellar data appears
  
       ... type ? for a listing of the graphics cursor menu
  
       ... type a to accept the star, d to reject it
  
       ... move to the next candidate stars and repeat the previous
           steps
  
       ... type l to list all the psf stars
  
       ... type f to fit the psf
  
       ... move cursor to first psf star and type s to see residuals,
           repeat for all the psf stars
  
       ... type w to save the PSF model
  
       ... type q to quit, and q again to confirm
  
       ... the output will appear in ypix.psf.1.imh, ypix.pst.1 and
           ypix.psg.1
  
   da&gt; allstar dev$ypix default default default default default
  
       ... verify the prompts
  
       ... the results will appear in ypix.als.1 and ypix.arj.1
  
   da&gt; pdump ypix.als.1 sharpness,chi yes | graph
  
       ... plot chi versus sharpness, the stars should cluster around
           sharpness = 0.0 and chi = 1.0, note that the frame does
           not have a lot of stars
  
   da&gt; display ypix.sub.1 2
  
       ... note that the psf stars subtract reasonably well but other
           objects which are not stars don't
  </pre></div>
  <p>
  2. Repeat example 1 but refit the sky using an annulus with an inner sky
  radius of 3.0 and an outer radius of 15.0.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; allstar dev$ypix default default default default default fitsky+ \
      sannulus=3.0 wsannulus=12.0
  
      ... verify the prompts
  
      ... the results will appear in ypix.als.2 and ypix.arj.2
  
  da&gt; pdump ypix.als.2 sharpness,chi yes | graph
  
      ... plot chi versus sharpness, the stars should cluster around
          sharpness = 0.0 and chi = 1.0, note that the frame does
          not have a lot of stars
  
  da&gt; display ypix.sub.2 2
  
      ... note that the psf stars subtract reasonably well but other
          objects which are not stars don't
  </pre></div>
  <p>
  3. Run allstar on a section of the input image using the group file and PSF
  model derived in example 1 for the parent image and writing the results
  in the coordinate system of the parent image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; allstar dev$ypix[150:450,150:450] default default default default \
      default wcsin=tv wcspsf=tv wcsout=tv
  
      ... answer the verify prompts
  
      ... fit the stars
  
      ... the results will appear in ypix.als.3 and ypix.arj.3
  
  da&gt; display dev$ypix[150:450,150:450] 1
  
      ... display the image
  
  da&gt; pdump ypix.als.3 xc,yc yes | tvmark 1 STDIN col=204
  
      ... mark the stars on the original image
  
  da&gt; display ypix.sub.3 2
  
     ... display the subtracted image section
  </pre></div>
  <p>
  4. Run allstar exactly as in example 1 but submit the task to the background.
  Turn off verify and verbose.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; allstar dev$ypix default default default default default verbose- \
      verify- &amp;
  
      ... the results will appear in ypix.als.4 and ypix.arj.4
  </pre></div>
  <p>
  4. Run ALLSTAR exactly as in example 3 but turn caching off.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; allstar m92 m92.grp.1 m92.psf.1 default "" default verb+ veri- \
      cache- &gt; allstar.out &amp;
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
  datapars,daopars,peak,nstar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'OUTPUT' 'ERRORS' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _nstar:

nstar: Fit the psf to predefined groups of stars
================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  nstar image groupfile psfimage nstarfile rejfile
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The list of images containing the stellar groups to be fit.
  </dd>
  </dl>
  <dl id="l_groupfile">
  <dt><b>groupfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='groupfile' Line='groupfile' -->
  <dd>The list of input group photometry files containing the group membership
  information and initial estimates for the positions and magnitudes of the stars
  to be measured. There must be one group file for every input image. If
  groupfile is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory specification then NSTAR
  will look for a file with the name image.grp.? where ? is the highest existing
  version number. Groupfile is usually the output of the DAOPHOT GROUP task, but
  may also be the output of the NSTAR and PSF tasks. Groupfile may be an
  APPHOT/DAOPHOT text database or an STSDAS binary table.
  </dd>
  </dl>
  <dl id="l_psfimage">
  <dt><b>psfimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='psfimage' Line='psfimage' -->
  <dd>The list of images containing the PSF models computed by the DAOPHOT PSF task.
  The number of PSF images must be equal to the number of input images.  If
  psfimage is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory specification,
  then PEAK will look for an image with the name image.psf.?, where
  ? is the highest existing version number.
  </dd>
  </dl>
  <dl id="l_nstarfile">
  <dt><b>nstarfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nstarfile' Line='nstarfile' -->
  <dd>The list of output photometry files. There must be one output photometry
  file for every input image.  If nstarfile is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a
  directory specification, then NSTAR will write an output file with the name
  image.nst.? where ? is the next available version number. Nstarfile is a text
  database if the DAOPHOT package parameter text is <span style="font-family: monospace;">"yes"</span>, an STSDAS table
  database if it is <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_rejfile">
  <dt><b>rejfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rejfile' Line='rejfile' -->
  <dd>The list of output rejected photometry files containing the positions and sky
  values of stars that could not be fit. If rejfile is undefined, results for all
  the stars in photfile are written to <i>nstarfile</i>, otherwise only the stars
  which were successfully fit are written to <i>nstarfile</i> and the remainder are
  written to rejfile. If rejfile is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory
  specification NSTAR writes an output file with the name image.nst.? where ? is
  the next available version number. Otherwise rejfile must specify one output
  photometry file for every input image. Rejfile is a text database if the
  DAOPHOT package parameter <i>text</i> is <span style="font-family: monospace;">"yes"</span>, an STSDAS binary table database
  if it is <span style="font-family: monospace;">"no"</span>.
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
  <dd>The coordinate system of the input coordinates read from <i>groupfile</i>, of the
  psf model <i>psfimage</i>, and of the output coordinates written to
  <i>nstarfile</i> and <i>rejfile</i> respectively. The image header coordinate
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
  <dt><b>cache = <span style="font-family: monospace;">")_.cache"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cache' Line='cache = ")_.cache"' -->
  <dd>Cache the image pixels in memory. Cache may be set to the value of the apphot
  package parameter (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>. By default caching is
  disabled.
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = <span style="font-family: monospace;">")_.verify"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = ")_.verify"' -->
  <dd>Verify the critical NSTAR task parameters? Verify can be set to the DAOPHOT
  package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = <span style="font-family: monospace;">")_.update"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = ")_.update"' -->
  <dd>Update the NSTAR task parameters if <i>verify</i> is <span style="font-family: monospace;">"yes"</span>? Update can be
  set to the default daophot package parameter value, <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = <span style="font-family: monospace;">")_.verbose"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = ")_.verbose"' -->
  <dd>Print messages about the progress of the task ? Verbose can be set to the
  DAOPHOT package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  NSTAR computes x and y centers and magnitudes for all the stellar groups in
  <i>groupfile</i> by fitting the PSF <i>psfimage</i> to the data in <i>image</i>.
  NSTAR reads the group membership information along with initial estimates of
  the centers and magnitudes, and the sky values from the photometry file
  <i>groupfile</i>.  <i>Groupfile</i> is usually the output of the DAOPHOT GROUP
  task but may also be the output of the PSF and NSTAR tasks. The computed
  centers and magnitudes are written to <i>nstarfile</i> along with the sky
  values, the number of iterations it took to fit the star, the goodness of fit
  statistic chi and the image sharpness statistic sharp. If <i>rejfile</i> is
  undefined, only stars that are successfully fit are written to <i>nstarfile</i>,
  and the remainder are written to <i>rejfile</i>. Otherwise all the stars are
  written to <i>nstarfile</i>.  <i>Nstarfile</i> and <i>rejfile</i> are text
  databases if the DAOPHOT package parameter <i>text</i> is <span style="font-family: monospace;">"yes"</span>, an STSDAS table
  database if it is <span style="font-family: monospace;">"no"</span>.
  </p>
  <p>
  The coordinates read from <i>groupfile</i> are assumed to be in coordinate
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
  The coordinates written to <i>nstarfile</i> and <i>rejfile</i> are in the
  coordinate system defined by <i>wcsout</i> with the exception of the psf model
  center coordinates PSFX and PSFY which are always in the logical system of
  the input image. The options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, and <span style="font-family: monospace;">"physical"</span>. The simplest
  default is the <span style="font-family: monospace;">"logical"</span> system.  Users wishing to correlate the output
  coordinates of objects measured in image sections or mosaic pieces with
  coordinates in the parent image must use the <span style="font-family: monospace;">"tv"</span> or <span style="font-family: monospace;">"physical"</span> coordinate
  systems.
  </p>
  <p>
  If <i>cache</i> is yes and the host machine physical memory and working set size
  are large enough, the input image pixels are cached in memory. If caching
  is enabled and NSTAR is run interactively the first measurement will appear
  to take a long time as the entire image must be read in before the measurement
  is actually made. All subsequent measurements will be very fast because NSTAR
  is accessing memory not disk. The point of caching is to speed up random
  image access by making the internal image i/o buffers the same size as the
  image itself. However if the input object lists are sorted close to row order
  and sparse caching may actually worsen not improve the execution time. Also at
  present there is no point in enabling caching for images that are less than
  or equal to 524288 bytes, i.e. the size of the test image dev$ypix, as the
  default image i/o buffer is exactly that size. However if the size of dev$ypix
  is doubled by converting it to a real image with the chpixtype task then the
  effect of caching in interactive is can be quite noticeable if measurements
  of objects in the top and bottom halves of the image are alternated.
  </p>
  <p>
  By default NSTAR computes new centers for all the stars in <i>groupfile</i>.
  However if the DAOPARS parameter <i>recenter</i> is <span style="font-family: monospace;">"no"</span>, NSTAR assumes that the
  x and y centers in <i>groupfile</i> are the true centers and does not refit
  them. This option can be quite useful in cases where accurate center values
  have been derived from an image that has been through some non-linear image
  restoration algorithm, but the photometry must be derived from the original
  unrestored image.
  </p>
  <p>
  By default NSTAR computes the sky value for each group by averaging the
  individual sky values in <i>groupfile</i> for all the stars in the group. If
  <i>groupsky</i> is <span style="font-family: monospace;">"no"</span> then the sky value for a particular pixel which
  contributes to the group fit is set to the mean of the sky values of only those
  stars for which the pixel is within one fitting radius. However if the DAOPARS
  parameter <i>fitksy</i> is <span style="font-family: monospace;">"yes"</span>, then NSTAR computes a new group sky value as
  part of the non-linear least-squares fit. Recomputing the sky can significantly
  reduce the scatter in the magnitudes in regions where the sky background is
  varying rapidly, but users may need to increase <i>fitrad</i> to include more
  sky pixels in the fit. Users should experiment cautiously with this option.
  </p>
  <p>
  Only pixels within the good data range delimited by the DATAPARS task
  parameters <i>datamin</i> and <i>datamax</i> are included in the fit. Most users
  set <i>datamin</i> and <i>datamax</i> so as to exclude pixels outside the
  linearity regime of the detector. By default all the data is fit. Users are
  advised to determine accurate values for these parameters and set the
  appropriate parameters in DATAPARS before beginning any DAOPHOT reductions.
  </p>
  <p>
  Only pixels within the fitting radius <i>fitrad</i> / <i>scale</i> are included
  in the fit for each star. <i>Fitrad</i> is located in the DAOPARS task and
  <i>scale</i> is located in the DATAPARS task. Since the non-linear least-squares
  fitting algorithm determines three unknowns, the x and y position of the star's
   centroid and its brightness, the value of <i>fitrad</i> must be sufficiently
  large to include at least three pixels in the fit for each star. To accelerate
  the convergence of the non-linear least-squares fitting algorithm pixels within
  <i>fitrad</i> are assigned weights which are  inversely proportional to the
  radial distance of the pixel from the x and y centroid of the star, falling
  from a maximum at the centroid to zero at the fitting radius. <i>Fitrad</i> must
   be sufficiently large to include at least three pixels with non-zero weights
  in the fit for each star. Values of <i>fitrad</i> close to the full-width at
  half-maxima of the PSF are recommended. In actual fact NSTAR imposes a minimum
  number of pixel limit of four.
  </p>
  <p>
  NSTAR performs a weighted fit to the PSF. The weight of each pixel is computed
  by combining, the radial weighting function described above, with weights
  derived from the random errors NSTAR predicts based on the values of the
  DATAPARS parameters <i>readnoise</i> and <i>epadu</i>, and the flat-fielding and
  profile interpolation errors specified by the DAOPARS <i>flaterr</i> and
  <i>proferr</i> parameters. To obtain optimal fits, users are strongly advised
  to determine those parameters accurately and to enter their values in DATAPARS
  and DAOPARS before beginning any DAOPHOT reductions.
  </p>
  <p>
  For each group of stars to be fit, NSTAR extracts a subraster from <i>image</i>
  which extends approximately <i>psfrad</i> / <i>scale</i> + 1 pixels wide past
  the limiting values of the x and y coordinates of the stars in the group.
  <i>Psfrad</i> is the PSF radius specified in the DAOPARS task, and <i>scale</i>
  is the image scale specified by the DATAPARS task. <i>Psfrad</i> may be less
  than or equal to but can never exceed the value of the image header parameter
  <span style="font-family: monospace;">"PSFRAD"</span> in <i>psfimage</i>. <i>Psfrad</i> should always be several pixels larger
  than <i>fitrad</i> to permit the x and y centroids to wander during the fitting
  process.
  </p>
  <p>
  As well as the computed x and y centers and magnitudes, NSTAR outputs the number
   of times the PSF fit had to be iterated before reaching convergence. The
  minimum number of iterations is four. The maximum number of iteration permitted
  is specified by the <i>maxiter</i> parameter in the DAOPARS task. Obviously the
  results for stars which have reached the maximum iteration count should be
  viewed with suspicion. However since the convergence criteria are quite strict,
  (the computed magnitude must change  by less than .0005 magnitudes or 0.10
  sigma whichever is larger, and the x and y centroids must change by less than
  0.002 pixels from one iteration to the next), even these stars may be
  reasonably well measured. It must be emphasized that every star in the group
  must individually satisfy the convergence criteria in order for the group to be
   considered adequately reduced.
  </p>
  <p>
  NSTAR computes a goodness of fit statistic chi which is essentially the ratio
  of the observed pixel-to-pixel scatter in the fitting residuals to the expected
  scatter. Since the expected scatter is dependent on the DATAPARS task parameters
  <i>readnoise</i> and <i>epadu</i>, and the DAOPARS parameters <i>flaterr</i> and
  <i>proferr</i> it is important for these values to be set correctly. A plot of
  chi versus magnitude should scatter around unity with little or no trend in
  chi with magnitude, except at the bright end where saturation effects may be
  present.
  </p>
  <p>
  Finally NSTAR computes the statistic sharp which estimates the intrinsic angular
  size of the measured object outside the atmosphere. Sharp is roughly defined as
  the difference between the square of the width of the object and the square of
  the width of PSF. Sharp has values close to zero for single stars, large
  positive values for blended doubles and partially resolved galaxies and large
  negative values for cosmic rays and blemishes.
  </p>
  <p>
  NSTAR implements a highly sophisticated star rejection algorithm. First of all,
   any group of stars which is more than a certain size is simply not fit. The
  maximum group size is specified by the <i>maxgroup</i> parameter in the DAOPARS
  task. Larger groups may run into numerical precision problems during the fits.
  Users should exercise care in increasing the <i>maxgroup</i> parameter. If two
  stars in a group have centroids separated by a critical distance, currently set
  arbitrarily to 0.37 * the FWHM of the stellar core, their photocentric position
  and combined magnitude is assigned to the brighter of the two stars, and the
  fainter is eliminated. Any star which converges to 12.5 magnitudes greater than
   the magnitude of the PSF is considered to be non-existent and eliminated from
  the group.
  </p>
  <p>
  After iteration 5, if the faintest star in the group has a brightness less than
   one sigma above zero, it is eliminated. After iterations 10, if the faintest
  star in the group has a brightness less than 1.5 sigma above zero, it is
  eliminated. After iterations 15 to 50 or whenever the solutions has converged
  whichever comes first, if the faintest star in the group has a brightness less
  than 2.0 sigma above zero, it is eliminated.  After iterations 5, 10 and 15,
  if two stars are separated by more than 0.37 * FWHM and less than 1.0 * FWHM
  and if the fainter of the two is more uncertain than 1.0, 1.5 or 2.0 sigma
  respectively the fainter one is eliminated.
  </p>
  <p>
  Whenever a star is eliminated the iteration counter is backed up by one and
  reduction proceeds with a smaller set of stars. Backing up the counter gives
  the second least certain star in the group two iterations to settle into a new
  fit before its fate is decided.  The star rejection algorithm depends upon the
  DATAPARS <i>readnoise</i> and <i>gain</i> parameters and the DAOPARS parameter
  <i>flaterr</i> and <i>proferr</i>. Therefore these parameters should be set to
  reasonable values before running NSTAR.
  </p>
  <p>
  NSTAR operates in a very similar manner to PEAK. However because it fits groups
   of stars simultaneously it is much more accurate than PEAK in crowded regions.
  The ALLSTAR task also fits groups of stars simultaneously, both  grouping the
  stars dynamically as well as producing a subtracted image. Essentially it
  replaces GROUP, GRPSELECT, NSTAR and SUBSTAR. However the user has little
  control over the grouping process and does not know at the end which stars were
  actually fit together. NSTAR is the task of choice when a user wants to
  maintain rigorous control over the composition of the stellar groups.
  </p>
  </section>
  <section id="s_output">
  <h3>Output</h3>
  <p>
  If <i>verbose</i> = yes, a single line is output to the terminal for each star
  fit or rejected. Full output is written to <i>nstarfile</i> and <i>rejfile</i>.
  At the beginning of these two files a header listing the current values of the
  parameters is written. For each star fit/rejected the following quantities are
  written to the output file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  id  group  xcenter  ycenter  mag  merr  msky  niter  sharpness
      chi  pier  perr
  </pre></div>
  <p>
  Id is the id number of the star and group is its group number. Xcenter and
  ycenter are the fitted coordinates in pixels. Mag and merr are the fitted
  magnitude and magnitude error respectively. Msky is the individual sky value
  for the star. Niter is the number of iterations it took to fit the star and
  sharpness and chi are the sharpness and goodness of fit statistic respectively.
  Pier and perror are the photometry error code and accompanying error message
  respectively.
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
  
   da&gt; group dev$ypix default default default
  
       ... verify the prompts
  
       ... the output will appear in ypix.grp.1
  
   da&gt; nstar dev$ypix default default default default
  
       ... verify the prompts
  
       ... the results will appear in ypix.nst.1 and ypix.nrj.1
  
   da&gt; pdump ypix.nst.1 sharpness,chi yes | graph
  
       ... plot chi versus sharpness, the stars should cluster around
           sharpness = 0.0 and chi = 1.0, note that the frame does
           not have a lot of stars
  
   da&gt; substar dev$ypix default  "" default default
  
       ... subtract the fitted stars
  
   da&gt; display ypix.sub.1 2
  
       ... note that the psf stars subtract reasonably well but other
           objects which are not stars don't
  </pre></div>
  <p>
  2. Run nstar on a section of the input image using the group file and PSF
  model derived in example 1 for the parent image and writing the results
  in the coordinate system of the parent image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; nstar dev$ypix[150:450,150:450] default default default default \
      wcsin=tv wcspsf=tv wcsout=tv
  
      ... answer the verify prompts
  
      ... fit the stars
  
      ... the results will appear in ypix.nst.2 and ypix.nrj.2
  
  da&gt; display dev$ypix[150:450,150:450] 1
  
      ... display the image
  
  da&gt; pdump ypix.nst.2 xc,yc yes | tvmark 1 STDIN col=204
  
      ... mark the stars
  
  da&gt; substar dev$ypix ypix.nst.2 "" default default
  
      ... subtract stars from parent image
  
      ... the output images is ypix.sub.2
  
  da&gt; substar dev$ypix[150:450,150:450] ypix.nst.2 "" default default  \
      wcsin=tv wcspsf=tv wcsout=tv
  
      ... subtract stars from the nstar input image
  
      ... the output images is ypix.sub.3
  </pre></div>
  <p>
  3. Run nstar exactly as in example 1 but submit the task to the background.
  Turn off verify and verbose.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; nstar dev$ypix default default default default verbose- \
      verify- &amp;
  
      ... the results will appear in ypix.nst.3 and ypix.nrj.3
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
  datapars,daopars,peak,allstar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'OUTPUT' 'ERRORS' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

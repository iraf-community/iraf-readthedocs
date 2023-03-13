.. _peak:

peak: Fit the psf to single stars
=================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  peak image photfile psfimage peakfile rejfile
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
  <dd>The list of input photometry files containing initial estimates of the
  positions and magnitudes of the stars to be fit. The number of photometry
  files must be equal to the number of input images. If photfile is <span style="font-family: monospace;">"default"</span>,
  <span style="font-family: monospace;">"dir$default"</span>, or a directory specification  PSF searches for a file called
  dir$image.mag.# where # is the highest available version number for the file.
  Photfile is usually the output of the DAOPHOT PHOT task, but may also be the
   output of PEAK itself, or of the DAOPHOT package GROUP, NSTAR,  ALLSTAR or
  PSF tasks. Photfile may be an APPHOT/DAOPHOT text database or an STSDAS table.
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
  <dl id="l_peakfile">
  <dt><b>peakfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='peakfile' Line='peakfile' -->
  <dd>The list of output photometry files. There must be one output photometry
  file for every input image.  If peakfile is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a
  directory specification, then PEAK will write an output file with the name
  image.pk.? where ? is the next available version number. Peakfile is a text
  database if the DAOPHOT package parameter text is <span style="font-family: monospace;">"yes"</span>, an STSDAS table
  database if it is <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_rejfile">
  <dt><b>rejfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rejfile' Line='rejfile' -->
  <dd>The list of output rejected photometry files containing the positions and sky
  values of stars that could not be fit. If rejfile is undefined, results for all
  the stars in photfile are written to <i>peakfile</i>, otherwise only the stars
  which were successfully fit are written to <i>peakfile</i> and the remainder are
  written to rejfile. If rejfile is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory
  specification PEAK writes an output file with the name image.prj.? where ? is
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
  <dd>The coordinate system of the input coordinates read from <i>photfile</i>, of the
  psf model <i>psfimage</i>, and of the output coordinates written to
  <i>peakfile</i> and <i>rejfile</i> respectively. The image header coordinate
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
  <dd>Verify the critical PEAK task parameters? Verify can be set to the DAOPHOT
  package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = <span style="font-family: monospace;">")_.update"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = ")_.update"' -->
  <dd>Update the PEAK task parameters if <i>verify</i> is <span style="font-family: monospace;">"yes"</span>? Update can be
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
  PEAK computes x and y centers, sky values  and magnitudes for all the stars in
  <i>photfile</i> by fitting the PSF model in <i>psfimage</i> to single stars in
  <i>image</i>. PEAK reads initial estimates of the centers and magnitudes along
  with the sky values from the photometry file <i>photfile</i>. <i>Photfile</i> is
  usually the output of the DAOPHOT PHOT task but may also be the output of PEAK
  itself, NSTAR, ALLSTAR, GROUP or PSF. The computed centers, sky values, and
  magnitudes are written to <i>peakfile</i> along with the number of iterations
  it took to fit the star, the goodness of fit statistic chi, and the image
  sharpness statistic sharp.  If <i>rejfile</i> is defined only stars that are
  successfully fit are written to <i>peakfile</i>. The remainder are written to
  <i>rejfile</i>. Otherwise all the stars are written to <i>peakfile</i>.
  <i>Peakfile</i> and <i>rejfile</i> are APPHOT/DAOPHOT text databases if the
  DAOPHOT package parameter <i>text</i> is <span style="font-family: monospace;">"yes"</span>, STSDAS binary table databases
  if it is <span style="font-family: monospace;">"no"</span>.
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
  The coordinates written to <i>peakfile</i> and <i>rejfile</i> are in the
  coordinate system defined by <i>wcsout</i>. The options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>,
  and <span style="font-family: monospace;">"physical"</span>. The simplest default is the <span style="font-family: monospace;">"logical"</span> system. Users wishing to
  correlate the output coordinates of objects measured in image sections or
  mosaic pieces with coordinates in the parent image must use the <span style="font-family: monospace;">"tv"</span> or
  <span style="font-family: monospace;">"physical"</span> coordinate systems.
  </p>
  <p>
  If <i>cache</i> is yes and the host machine physical memory and working set size
  are large enough, the input image pixels are cached in memory. If caching
  is enabled and the first measurement will appear to take a long time as the
  entire image must be read in before the measurement is actually made. All
  subsequent measurements will be very fast because PEAK is accessing memory not
  disk. The point of caching is to speed up random image access by making the
  internal image i/o buffers the same size as the image itself. However if the
  input object lists are sorted in row order and sparse caching may actually
  worsen not improve the execution time. Also at present there is no point in
  enabling caching for images that are less than or equal to 524288 bytes, i.e.
  the size of the test image dev$ypix, as the default image i/o buffer is exactly
  that size. However if the size of dev$ypix is doubled by converting it to a
  real image with the chpixtype task then the effect of caching in interactive
  is can be quite noticeable if measurements of objects in the top and bottom
  halves of the image are alternated.
  </p>
  <p>
  By default PEAK computes new centers for all the stars in <i>photfile</i>.
  However if the DAOPARS parameter <i>recenter</i> is <span style="font-family: monospace;">"no"</span>, PEAK assumes that the
  x and y centers in <i>photfile</i> are the true centers and does not refit them.
  This option can be quite useful in cases where accurate center values have been
  derived from an image that has been through some non-linear image restoration
  algorithm, but the photometry must be derived from the original unrestored
  image.
  </p>
  <p>
  By default PEAK uses the sky value in <i>photfile</i>. However if the DAOPARS
  parameter <i>fitsky</i> is <span style="font-family: monospace;">"yes"</span>, then PEAK computes a new sky value as part of
  the non-linear least-squares fit. Recomputing the sky can significantly reduce
  the scatter in the magnitudes in regions where the sky background is varying
  rapidly, but users may need to increase the <i>fitrad</i> parameter to include
  more sky pixels in the fit. Users should experiment cautiously with this option.
  </p>
  <p>
  Only pixels within the good data range delimited by the DATAPARS task parameters
  <i>datamin</i> and <i>datamax</i> are included in the fit.  Most users set
  <i>datamin</i> and <i>datamax</i>  to exclude pixels outside the linearity
  regime of the detector. By default all the data is fit.  Users are advised to
  determine the values of these parameters for their detector and set the values
  in DATAPARS before beginning DAOPHOT reductions.
  </p>
  <p>
  Only pixels within the fitting radius set by the DAOPARS task parameter
  <i>fitrad</i> divided by the DATAPARS parameter <i>scale</i> are included in the
  fit. Since the non-linear least-squares fits determine three unknowns, the x
  and y position of the star's centroid and its brightness, the value of
  <i>fitrad</i> must be sufficiently large to include at least three pixels in
  the fit.  To accelerate the convergence of the non-linear least-squares fitting
  algorithm, pixels within <i>fitrad</i> are assigned weights which are inversely
  proportional to the radial distance of the pixel from the x and y centroid of
  the star, falling from a maximum at the centroid to zero at the fitting radius.
  <i>Fitrad</i> must be sufficiently large to include at least three pixels with
  non-zero weights in the fit. Values of <i>fitrad</i> close to the full-width at
  half-maxima of the PSF are recommended.
  </p>
  <p>
  PEAK performs a weighted fit to the PSF. The weight of each pixel is computed
  by combining the radial weighting function described above with weights derived
  from the expected random errors computed using the values of the DATAPARS
  parameters <i>readnoise</i> and <i>epadu</i> specified by the user. Both to
  obtain optimal fits, and because PEAK employs a conservative formula, dependent
  on <i>readnoise</i> and <i>epadu</i>, for reducing the weights of deviant pixels
  which do not approach the model as the fit proceeds, users are strongly
  advised to determine the values of these parameters accurately, and to enter
  these values in DATAPARS before beginning any DAOPHOT reductions.
  </p>
  <p>
  For each star to be fit, PEAK extracts a subraster from <i>image</i> which is N
  by N pixels square where N is approximately 2 * <i>psfrad</i> / <i>scale</i>  + 1
  pixels wide. <i>Psfrad</i> is the PSF radius specified in the DAOPARS task and
  <i>scale</i> is the scale factor specified in the DATAPARS task. <i>Psfrad</i> may
  be less than or equal to, but can never exceed the value of the image header
  parameter <span style="font-family: monospace;">"PSFRAD"</span> in <i>psfimage</i>. <i>Psfrad</i> should be set to a value
  several pixels larger than <i>fitrad</i> in order to permit the x and y
  centroids to wander during the fitting process.
  </p>
  <p>
  Along with the computed x and y centers and magnitudes, PEAK outputs the number
  of times the PSF fit had to be iterated to reach convergence for each star. The
  minimum number of iterations is three. The maximum number of iteration permitted
  is specified by the <i>maxiter</i> parameter in the DAOPARS task.  Obviously the
  results for stars which have reached the maximum iteration count should be
  viewed with suspicion. However since the convergence criteria are quite strict,
  (the computed magnitude must change  by less than .001 magnitudes or 0.05 sigma
  whichever is larger and the x and y centroids must change by less than 0.01
  pixels from one iteration to the next), even these stars may be reasonably well
  measured.
  </p>
  <p>
  PEAK computes a goodness of fit statistic chi which is essentially the ratio of
  the observed pixel-to-pixel scatter in the fit residuals to the expected
  scatter. Since the expected scatter is dependent on the DATAPARS task parameters
  <i>readnoise</i> and <i>epadu</i>, it is important for these values to be set
  correctly. A plot of chi versus magnitude should scatter around unity with
  little or no trend in chi with magnitude, except at the bright end where
  saturation effects may be present.
  </p>
  <p>
  Finally PEAK computes the statistic sharp which estimates the intrinsic angular
  size of the measured object outside the atmosphere. Sharp is roughly defined as
  the difference between the square of the width of the object and the square of
  the width of PSF. Sharp has values close to zero for single stars, large
  positive values for blended doubles and partially resolved galaxies, and large
  negative values for cosmic rays and blemishes.
  </p>
  <p>
  Because PEAK cannot fit stars in crowded fields with overlapped images like the
  NSTAR and ALLSTAR  tasks do, and for sparsely populated frames aperture
  photometry produced by PHOT is often just as good and faster to compute, PEAK
  has few unique functions. PEAK is often useful however for fitting and removing
  single stars in images where the stars are interfering with the real object of
  interest such as a galaxy. In that case the PEAK results can be input to SUBSTAR
  which will then remove the interfering stars. Another potential use of PEAK
  is the removal of stars from sparsely populated sky flats in preparation
  for smoothing.
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
  sharpness and goodness of fit statistic respectively. Pier and perror are the
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
  1               # The sky is undefined
  2               # There are too few good pixels to fit the star
  3               # The fit is singular
  4               # The star is too faint
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the PSF model for the test image dev$ypix. Good stars for making the
  PSF model can be found at (442,410), (348,189), and (379,67).
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
  
   da&gt; peak dev$ypix default default default default
  
       ... the results will appear in ypix.pk.1 and ypix.prj.1
  
   da&gt; pdump ypix.pk.1 sharpness,chi yes | graph
  
       ... plot chi versus sharpness, the stars should cluster around
           sharpness = 0.0 and chi = 1.0, note that the frame does
           not have a lot of stars
  
   da&gt; substar dev$ypix ypix.pk.1 "" default default
  
       ... subtract the fitted stars
  
   da&gt; display ypix.sub.1 2
  
       ... note that the psf stars subtract reasonably well but other
           objects which are not stars don't
  </pre></div>
  <p>
  2. Run peak on a section of the input image using the photometry file and PSF
  model derived in example 1 for the parent image and writing the results
  in the coordinate system of the parent image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; peak dev$ypix[150:450,150:450] default default default default \
      wcsin=tv wcspsf=tv wcsout=tv
  
      ... answer the verify prompts
  
      ... fit the stars
  
      ... the results will appear in ypix.pk.2 and ypix.prj.2
  
  da&gt; display dev$ypix[150:450,150:450] 1
  
      ... display the image
  
  da&gt; pdump ypix.pk.2 xc,yc yes | tvmark 1 STDIN col=204
  
      ... mark the stars
  
  da&gt; substar dev$ypix ypix.pk.2 "" default default
  
      ... subtract stars from parent image
  
      ... the output images is ypix.sub.2
  
  da&gt; substar dev$ypix[150:450,150:450] ypix.pk.2 "" default default  \
      wcsin=tv wcspsf=tv wcsout=tv
  
      ... subtract stars from the peak input image
  
      ... the output images is ypix.sub.3
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
  datapars,daopars,nstar,allstar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'OUTPUT' 'ERRORS' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

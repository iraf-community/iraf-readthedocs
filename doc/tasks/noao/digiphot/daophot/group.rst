.. _group:

group: Group stars based on positional overlap and signal/noise
===============================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  group image photfile psfimage groupfile
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The list of images containing the stars to be grouped.
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
  Photfile is normally the output of the PHOT task but may also be the output of
  the PSF, PEAK, NSTAR and ALLSTAR tasks. Photfile may be an APPHOT/DAOPHOT
  text database or an STSDAS binary table.
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
  <dl id="l_groupfile">
  <dt><b>groupfile = </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='groupfile' Line='groupfile = ' -->
  <dd>The list of output grouped photometry files. There must be one output group
  photometry file for every input image.  If groupfile is <span style="font-family: monospace;">"default"</span>,
  <span style="font-family: monospace;">"dir$default"</span>, or a directory specification then GROUP writes a file called
  image.grp.? where ? is the next available version number. If the DAOPHOT
  package parameter <i>text</i> is <span style="font-family: monospace;">"yes"</span> then an APPHOT/DAOPHOT text database is
  written, otherwise an STSDAS table is written.
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
  <i>groupfile</i>. The image header coordinate system is used to transform from
  the input coordinate system to the <span style="font-family: monospace;">"logical"</span> system used internally, from the
  internal logical system to the PSF model system, and from the internal
  <span style="font-family: monospace;">"logical"</span> pixel coordinate system to the output coordinate system. The input
  coordinate system options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, <span style="font-family: monospace;">"physical"</span>, and <span style="font-family: monospace;">"world"</span>. The PSF
  model and output coordinate system options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, and <span style="font-family: monospace;">"physical"</span>.
  The image cursor coordinate system is assumed to be the <span style="font-family: monospace;">"tv"</span> system.
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
  <dd>Verify the critical GROUP task parameters? Verify can be set to the DAOPHOT
  package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = <span style="font-family: monospace;">")_.update"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = ")_.update"' -->
  <dd>Update the GROUP task parameters if <i>verify</i> is <span style="font-family: monospace;">"yes"</span>? Update can be
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
  GROUP takes the photometry file <i>photfile</i> file containing the stellar
  coordinates and photometry and associates the stars into natural groups based
  upon proximity and the magnitude level at which they overlap. The results are
  written into <i>groupfile</i>.  If the DAOPHOT package parameter <i>text</i> is
  <span style="font-family: monospace;">"yes"</span> then <i>groupfile</i> is a text database, otherwise it is an STSDAS table.
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
  The coordinates written to <i>groupfile</i> are in the coordinate system
  defined by <i>wcsout</i>. The options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, and <span style="font-family: monospace;">"physical"</span>. The
  simplest default is the <span style="font-family: monospace;">"logical"</span> system.  Users wishing to correlate the
  output coordinates of objects measured in image sections or mosaic  pieces
  with coordinates in the parent image must use the <span style="font-family: monospace;">"tv"</span> or <span style="font-family: monospace;">"physical"</span>
  coordinate systems.
  </p>
  <p>
  If <i>cache</i> is yes and the host machine physical memory and working set size
  are large enough, the input image pixels are cached in memory. If caching
  is enabled and the first data access will appear to take a long time as the
  entire image must be read in before the measurement is actually made. All
  subsequent data requests will be very fast because GROUP is accessing memory
  not disk. The point of caching is to speed up random image access by making
  the internal image i/o buffers the same size as the image itself. There is
  no point in turning caching on unless a lot of the input magnitudes are INDEF.
  In that case GROUP must access the image to estimate a magnitude. Also at
  present there is no point in enabling caching for images that are less than
  or equal to 524288 bytes, i.e. the size of the test image dev$ypix, as the
  default image i/o buffer is exactly that size. However if the size of dev$ypix
  is doubled by converting it to a real image with the chpixtype task then the
  effect of caching in interactive is can be quite noticeable if measurements
  of objects in the top and bottom halves of the image are alternated.
  </p>
  <p>
  The algorithm works in the following manner. If two stars are within a
  distance R pixels of one another, where R = <i>psfrad</i> / <i>scale</i> +
  <i>fitrad</i> / <i>scale</i> + 1, the PSF of the brighter one is evaluated at
  a distance d pixels, where d = <i>fitrad</i> / <i>scale</i> + 1 away from the
  fainter. If this value is larger than <i>critsnratio</i> times the expected
  noise per pixel then the two stars are put into the same group since the
  brighter star is capable of affecting the photometry of the fainter.
  <i>Psfrad</i>, <i>fitrad</i> and <i>critsnratio</i> are the psf radius, the
  fitting radius, and the critical S/N ratio respectively and are located
  in the DAOPARS task. <i>Scale</i> is the image scale parameter and is located
  in the DATAPARS task. In order for this algorithm to work correctly it is
  imperative that the DATAPARS readnoise and gain parameters <i>readnoise</i>
  and <i>gain</i> be set correctly as these values are used to compute the
  expected random noise per pixel.
  </p>
  <p>
  The correct value of <i>critsnratio</i> must be determined by trial and error.
  For example if a critical S/N ratio of 0.1 divides all the stars in the image
  into groups smaller than the <i>maxgroup</i> parameter in the DAOPARS task, then
  unavoidable random errors will dominate over crowding errors.  If a critical
  S/N ratio of 1.0 works, then crowding errors will be no worse than the random
  errors. If a critical S/N ratio much greater than 1 is required then in most
  cases crowding will be the dominant source or error.
  </p>
  <p>
  If <i>verbose</i> is set to <span style="font-family: monospace;">"yes"</span>, GROUP will write a table on the terminal
  showing the number of groups as a function of group size. If any group is
  larger than <i>maxgroup</i> then <i>critnsratio</i> must be increased or
  the GRPSELECT task used to cut large groups out of the file. When crowding
  conditions vary across the frame,  GROUP and GRPSELECT can be used together
  to get the best possible photometry for stars in different crowding regimes.
  </p>
  <p>
  If any stars in <i>photfile</i> have INDEF magnitudes, GROUP will attempt
  to estimate a magnitude for them based on the weighted sum of the pixels
  of a radial weighting function and the value of the PSF at that point.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Group the PHOT task output results for the test image dev$ypix using
  a critical S/N ratio of 1 and printing the output summary on the terminal.
  Good stars for making the PSF model can be found at (442,410), (348,189),
  and (379,67).
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
  
   da&gt; group dev$ypix default default default crit=1.0 verbose+
  
       ... verify the critical parameters
  
       ... answers will appear in ypix.grp.1
  </pre></div>
  <p>
  2. Run group on a section of the input image using the photometry file and PSF
  model derived in example 1 for the parent image and writing the results
  in the coordinate system of the parent image. Note that the results for
  example 2 are identical to those in example 1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; group dev$ypix[150:450,150:450] default default default  \
      wcsin=tv wcspsf=tv wcsout=tv
  
      ... answer the verify prompts
  
      ... fit the stars
  
      ... the results will appear in ypix.grp.2
  
  da&gt; display dev$ypix[150:450,150:450] 1
  
      ... display the image
  
  da&gt; pdump ypix.grp.2 xc,yc yes | tvmark 1 STDIN col=204
  
      ... mark the stars
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
  psf,grpselect,nstar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _substar:

substar: Subtract the fitted stars from the original image
==========================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  substar image photfile exfile psfimage subimage
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The list of images from which to subtract the scaled and shifted PSF.
  </dd>
  </dl>
  <dl id="l_photfile">
  <dt><b>photfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='photfile' Line='photfile' -->
  <dd>The list of PSF fitted photometry files. There must be one photometry file
  for every input image. If photfile is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory
  specification, SUBSTAR will look for a file called image.nst.? where the
  question mark stands for the highest existing version number. Photfile is
  usually the output of the NSTAR task but may also be the output of the PEAK
  and ALLSTAR tasks or even the PHOT task. Photfile may be an APPHOT/DAOPHOT text
  database or an STSDAS table.
  </dd>
  </dl>
  <dl id="l_exfile">
  <dt><b>exfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exfile' Line='exfile' -->
  <dd>The list of photometry files containing the ids of stars to be excluded
  from the subtraction. Exfile must be undefined or contain one exclude file
  for every input image. If exfile is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory
  specification, SUBSTAR will look for a file called image.pst.? where the ?
  mark stands for the highest existing version number. Exfile is usually the
  output of the PSTSELECT task but may also be the output of the PEAK, NSTAR and
  ALLSTAR tasks or even the PHOT task. Exfile may be an APPHOT/DAOPHOT text
  database or an STSDAS table.
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
  <dl id="l_subimage">
  <dt><b>subimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subimage' Line='subimage' -->
  <dd>The list of output subtracted images. There must be one output subtracted
  image for every input image.  If subimage is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a
  directory specification, then SUBSTAR will write an image called image.sub.?
  where question mark stands for the next available version number. 
  </dd>
  </dl>
  <dl id="l_datapars">
  <dt><b>datapars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datapars' Line='datapars = ""' -->
  <dd>The name of the file containing the data dependent parameters. The parameters
  <i>scale</i>, <i>datamin</i>, and <i>datamax</i> are located here. If datapars
  is undefined then the default parameter set in uparm directory
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
  the standard output if <i>verbose</i> = <span style="font-family: monospace;">"yes"</span>. The image header coordinate
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
  <dd>Verify the critical SUBSTAR task parameters? Verify can be set to the DAOPHOT
  package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = <span style="font-family: monospace;">")_update"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = ")_update"' -->
  <dd>Update the SUBSTAR task parameters if <i>verify</i> is <span style="font-family: monospace;">"yes"</span>? Update can be
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
  SUBSTAR task takes an input photometry list <i>photfile</i> containing
  the fitted coordinates and magnitudes, and an input PSF <i>psfimage</i>, and
  for each star in the photometry list scales and shifts the PSF and subtracts
  it from the input image <i>image</i>. The final subtracted image is saved in the
  output image <i>subimage</i>.
  </p>
  <p>
  The input photometry list can be the output from of the PEAK, NSTAR or ALLSTAR
  tasks or even the PHOT task although most people would not want to use the PHOT
  output for this purpose.
  </p>
  <p>
  Selected stars may be omitted from the subtraction by supplying their ids in
  the file <i>exfile</i>. <i>Exfile</i> is normally the output the PSTSELECT task
  and is used to tell SUBSTAR to subtract the PSF star neighbors, but not the
  PSF stars themselves.
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
  The coordinates written to the standard output if <i>verbose</i> = yes are in the
  coordinate system defined by <i>wcsout</i>. The options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>,
  and <span style="font-family: monospace;">"physical"</span>. The simplest default is the <span style="font-family: monospace;">"logical"</span> system. Users wishing to
  correlate the output coordinates of objects measured in image sections or
  mosaic pieces with coordinates in the parent image must use the <span style="font-family: monospace;">"tv"</span> or
  <span style="font-family: monospace;">"physical"</span> coordinate systems.
  </p>
  <p>
  If <i>cache</i> is yes and the host machine physical memory and working set size
  are large enough the input and output image pixels are cached in memory. If
  caching is enabled and SUBSTAR is run interactively the first subtraction
  will appear to take a long time as the entire image must be read in before
  the measurement is actually made. All subsequent measurements will be very
  fast because SUBSTAR is accessing memory not disk. The point of caching is
  to speed up random image access by making the internal image i/o buffers the
  same size as the image itself. However if the input object lists are sorted
  in row order which SUBSTAR does internally  and are sparse caching may
  actually worsen not improve the execution time. Also at present there is no
  point in enabling caching for images that are less than or equal to 524288
  bytes, i.e. the size of the test image dev$ypix, as the default image i/o
  buffer is exactly that size. However if the size of dev$ypix is doubled by
  converting it to a real image with the chpixtype task then the effect of
  caching in interactive is can be quite noticeable if measurements
  of objects in the top and bottom halves of the image are alternated.
  </p>
  <p>
  The SUBSTAR task is most commonly used to check on the quality of the PSF
  fitting produced by PEAK and NSTAR, to search for non-stellar objects and close
  binary stars, to generate an improved PSF in crowded fields, and to remove
  neighbors from bright stars which are to be used to determine aperture
  corrections.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Subtract the NSTAR photometry results for the test image dev$ypix from the
  image dev$ypix.
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
  2. Rerun the previous example on a section of the test image  using the group
  file and PSF model derived in example 1 for the parent image and writing the
  results in the coordinate system of the parent image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; nstar dev$ypix[150:450,150:450] default default default default \
      wcsin=tv wcspsf=tv wcsout=tv
  
      ... answer the verify prompts
  
      ... fit the stars
  
      ... the results will appear in ypix.nst.2 and ypix.nst.2
  
  da&gt; display dev$ypix[150:450,150:450] 1
  
      ... display the image
  
  da&gt; pdump ypix.nst.2 xc,yc yes | tvmark 1 STDIN col=204
  
      ... mark the stars
  
  da&gt; substar dev$ypix ypix.nst.2 "" default default
  
      ... subtract stars from parent image
  
      ... the output images is ypix.sub.2
  
  da&gt; substar dev$ypix[150:450,150:450] ypix.nst.2 "" default default  \
      wcsin=tv wcspsf=tv wcsout=tv
  
      ... subtract stars from the nstarinput image
  
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
  datapars,daopars,nstar,peak
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

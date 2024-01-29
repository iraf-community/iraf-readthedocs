.. _guide:

guide: Guide to using xdimsum with the xmosaic task
===================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_introduction">
  <span>1. Introduction</span>
  <p>
  <b>XDIMSUM</b> is a package for creating accurate sky subtracted images from
  sets of dithered observations.  While the observations need not be in the
  infrared, the dominance of the variable sky background in infrared data
  requires the dithering and recombination  of many short carefully sky
  subtracted exposures to produce deep images. Hence the package is called
  <span style="font-family: monospace;">"Experimental Deep Infrared Mosaicing Software"</span> or XDIMSUM.
  </p>
  <p>
  There's no published reference.  Generally people footnote it in the
  text and say something like:
  </p>
  <div class="highlight-default-notranslate"><pre>
  DIMSUM is the Deep Infrared Mosaicing Software package developed by
  Peter Eisenhardt, Mark Dickinson, Adam Stanford, and John Ward, and is
  available via ftp from ftp://iraf.noao.edu/iraf/extern/xdimsum/.
  </pre></div>
  <p>
  XDIMSUM is a variant of the <b>DIMSUM</b> package developed by P. Eisenhardt,
  M. Dickensen, S.A. Stanford, and J. Ward. F. Valdes (IRAF group) added
  FITS image format support, wrote the tutorial task <i>demos</i>, wrote the
  original version of this document, and repackaged DIMSUM for distribution as
  an IRAF external package. More recently L. Davis (IRAF group) rewrote the major
  <i>DIMSUM</i> scripts to improve their clarity, robustness, and efficiency,
  added several new tasks for computing relative offsets, and wrote help pages
  for all the DIMSUM tasks. This new version of DIMSUM uses the same default
  algorithms as the original DIMSUM but has diverged sufficiently from the
  original that it has been renamed XDIMSUM.
  </p>
  <p>
  XDIMSUM is being made available to the community as an external package in the
  hope that some of the enhancements may prove useful to others. Users should
  direct XDIMSUM installation questions, bug reports, questions about technical
  details, and comments and suggestions to the the IRAF group (iraf@noao.edu)
  not the original authors.
  </p>
  <p>
  The main body of this document is a guide to the XDIMSUM <b>xmosaic</b> task
  which executes all the major XDIMSUM processing steps in turn. These processing
  steps are outlined in Section 2.  Each major processing step is executed by
  one or more XDIMSUM tasks. By setting the xmosaic processing switches
  appropriately users can use <b>xmosaic</b> to perform any combination of these
  steps. The input data required by XDIMSUM and  and the output data produced by
  it are described in Section 3. A detailed example is provided in Section 4.
  </p>
  <p>
  The <b>xmosaic</b> task and most of the XDIMSUM subtasks are CL scripts. Users
  are encouraged to examine the scripts in orer to gain an understanding of the
  xmosaic algorithms and default parameter settings. The script source is located
  in the logical directory xdimsum$src and its subdirectories. Older versions
  of the current scripts and obsolete scripts are located in the logical
  directory xdimsum$src/obsolete.
  </p>
  </section>
  <section id="s_outline_of_the_major_xdimsum_processing_steps">
  <span>2. Outline Of the Major XDIMSUM Processing Steps</span>
  <p>
  This section describes the processing steps performed by the main XDIMSUM
  processing task <b>xmosaic</b>. These processing steps divide logically into
  two groups the first pass step and the mask pass step. Both steps perform
  similar operations and produce a sky subtracted, bad pixel corrected, cosmic
  ray corrected, registered, and combined image and exposure map.
  </p>
  <p>
  The first pass step produces a good first estimate of the true combined image
  and exposure map by sky subtracting, bad pixel correcting, and cosmic ray
  correcting the input individual images, and creating a combined image
  fro the corrected input images. The combined image goes deeper than the
  individual images and is used to create an object mask which defines the
  location, size, and shape of all the objects in the combined image. The
  object mask is split or deregistered into a set of individual input image
  object masks. The mask pass step repeats all the first pass step but uses
  the object masks to improve the sky subtraction, cosmic ray correction,
  and image combining steps to produce a more accurate and if desired higher
  resolution version of the combined image. 
  </p>
  <p>
  If first and mask pass processing steps can be executed separately by running
  the <b>xfirstpass</b> and <i>xmaskpass</i> tasks in sequence, which is exactly
  what the <i>xmosaic</i> task itself does.
  </p>
  </section>
  <section id="s_first_pass">
  <span>2.1 First Pass</span>
  <p>
  The first pass processing steps are: sky subtraction, bad pixel correction,
  cosmic ray correction, bad pixel mask updating, and image registration. The
  required input data are a list of dithered input images, a bad pixel, mask,
  and optionally a list of image offsets and scaling factors. If no offset
  list is provided the offsets the user must determine the offsets interactively.
  </p>
  </section>
  <section id="s_sky_subtraction_with_the_xslm_task">
  <span>2.1.1 Sky Subtraction with the Xslm Task</span>
  <p>
  If the <i>fp_xslm</i> switch is yes the xslm task produces a sky subtracted
  image for each images by computing its sky image from a set of neighboring
  images and subtracting this sky image from the input image.
  </p>
  <p>
  The scaling factor for each input image is computed using an <i>nsigrej</i> sigma
  iterated rejection about the mean of the pixels in the image section defined
  by <i>statsec</i>. The number of iterations must be less than or equal to
  <i>maxiter</i>. The scaling factor is the reciprocal of the median of the
  unrejected pixels and is stored in the input and sky subtracted image header
  KEYWORD <span style="font-family: monospace;">"SKYMED"</span>.
  </p>
  <p>
  For each image in the input image list <i>nmean</i> neighboring images
  in the list are selected, scaled, and combined to form the sky image. Except
  at the ends of the list there is usually an equal number of images before and
  after the image to be sky subtracted.  There must be at least <i>nskymin</i>
  images for sky subtraction to be performed. At each pixel <i>nreject</i> low
  and high pixels in the scaled images are rejected and the average of the
  remainder becomes the sky value for that pixel.  The sky values are
  subtracted from the input image to create a sky subtracted image.
  </p>
  </section>
  <section id="s_fixing_bad_pixels_with_the_maskfix_task">
  <span>2.1.2 Fixing Bad Pixels with the Maskfix Task</span>
  <p>
  If the <i>fp_maskfix</i> switch is yes the <i>maskfix</i> task removes known bad
  pixels from the sky subtracted images. The bad pixel mask <i>bpmask</i> is used
  to identify and replace the bad pixels by interpolation. The bad pixel mask is
  an image containing  0's in bad pixel regions and 1's elsewhere.
  </p>
  </section>
  <section id="s_removing_cosmic_rays_with_the_xzap_or_znap_tasks">
  <span>2.1.3 Removing Cosmic Rays with the Xzap or Znap Tasks</span>
  <p>
  If the <i>fp_xzap</i> switch is yes cosmic rays are removed from the sky
  subtracted images using the <i>xzap</i> task if <i>newxzap</i> is no, or the
  <i>xnzap</i> task if it is yes.
  </p>
  <p>
  Xzap creates an internal object mask from the sky subtracted image data which
  is used to locate the strongest objects. The cosmic rays are detected with a
  threshold algorithm applied to the ratio of the original input image to the
  median filtered input image. Only pixels outside the internal object mask are
  considered to be cosmic ray candidates. The detected cosmic rays are replaced
  by the local median and a cosmic ray mask is prodiced which records the
  location of the cosmic rays.
  </p>
  <p>
  Xnzap is a script task which calls the compiled task xcraverage task.
  Xcraverage detects and removes cosmic rays using a moving average combined
  with a central and deviant pixel rejection filter, a local sky estimate equal
  to the running median of the pixels around the averaging filter box, and a
  local sky sigma estimated by dividing the image into blocks and determining
  the percentile points of the pixels in the box. The cosmic rays are replaced
  by the local average and a cosmic ray mask is produced to record the location
  of the cosmic rays.
  </p>
  <p>
  Cosmic ray masks contain 1's at the locations of detected cosmic rays and
  0's elsewhere.
  </p>
  <p>
  If the <i>fp_badpixupdate</i> switch is yes the badpixupdate task and the cosmic
  ray masks are used to update the bad pixel mask. Bad pixel mask pixels are
  updated, i.e.  flagged as bad, if they are detected as cosmic rays in more
  than two images.
  </p>
  </section>
  <section id="s_making_the_shift_list_with_the_xdshifts_task">
  <span>2.1.4 Making the Shift List with the Xdshifts Task</span>
  <p>
  The shift list <i>shiftlist</i> defines the relative offsets between the
  individual input images. If the <i>fp_mkshifts</i> switch is yes 
  the <i>xdshifts</i> task and the image display are used to create it
  interactively. For this method to work there must be at least one object
  common to all the images. Rough offsets are estimated by displaying each image
  and prompting the user to mark and measure the position of a reference object
  common to all the images. True offsets are computed by prompting the user
  to measure and mark a set of registration objects in the reference image
  <i>reference</i>, applying the initial offsets, centroiding on the
  registration objects in each sky subtracted image, and computing final shifts
  relative to the reference image.
  </p>
  <p>
  The final shift list is a file containing four columns. These columns contain
  the image name, the pixel shifts in x and y, and a weight value which by
  default is 1.0. If the weight for an image is &lt; 0,  that image is excluded
  from the final mosaic. 
  </p>
  </section>
  <section id="s_combining_images_with_the_xnregistar_task">
  <span>2.1.5 Combining Images with the Xnregistar Task</span>
  <p>
  If the <i>fp_xnregistar</i> switch is yes the <i>xnregistar</i> task is used
  to combine the images. The input sky subtracted, bad pixel corrected, and
  cosmic ray corrected images are shifted, scaled, combined, and reoriented
  to produce the first guess combined image and exposure map. The corrected
  input images are shifted by integer pixel amounts if <i>fractional</i> is no,
  otherwise they are shifted by the full fractional pixel offset.
  </p>
  </section>
  <section id="s_mask_pass">
  <span>2.2 Mask Pass</span>
  </section>
  <section id="s_making_masks_with_the_mkmask_and_maskdereg_tasks">
  <span>2.2.1 Making Masks with the Mkmask and Maskdereg Tasks</span>
  <p>
  If the <i>mp_mkmask</i> switch is yes  the <i>mkmask</i> task is used to create
  two object masks from the first pass combined image and exposure map. The first
  mask sets the detection threshold to <i>mp_nsigcrmsk</i> and identifies only the
  brighter parts of the objects. This mask is used to check that the cores of
  those objects  in the individual images are not identified as cosmic rays.
  The second mask sets the threshold to <i>mp_nsigobjmsk</i> and identifies
  extended object regions. This mask is used to improve the sky subtraction
  step.
  </p>
  <p>
  The combined image masks are made from the first pass combined image as
  follows. First the combined image is divided by the square root of the
  exposure map to normalize for variations in the sky noise due to varying
  exposure times in each pixel. The sky RMS is computed using iterative sigma
  rejection and a recommended threshold value in terms of this RMS is determined.
  If <i>mp_chkmasks</i> is yes the uniform RMS image is displayed, the user
  examines it with the <b>imexamine</b> task, and determine a suitable
  threshold interactively. An algorithm which tracks and threshold detects
  above the sky is used to create an object mask containing 1's in object
  regions and 0's elsewhere.
  </p>
  <p>
  If the <i>mp_maskdereg</i> switch is yes  the <i>maskdereg</i> task and
  the sections file <i>sections</i> created by <i>xnregistar</i> during the
  first pass, are used to create object masks for the individual input images. 
  </p>
  </section>
  <section id="s_sky_subtraction_with_the_xslm_task_and_object_masks">
  <span>2.2.2 Sky Subtraction with the Xslm Task and Object Masks</span>
  <p>
  If the <i>mp_xslm</i> switch is yes the sky subtraction step is repeated using
  the <i>xslm</i> task and the individual object masks.  The object masks are used
  to, reject object pixels from the scaling factor computation if <i>use_omask</i>
  is yes, and to reject object pixels from the sky image computation.
  </p>
  </section>
  <section id="s_fixing_bad_pixels_with_the_maskfix_task">
  <span>2.2.3 Fixing Bad Pixels with the Maskfix Task</span>
  <p>
  If the <i>mp_maskfix</i> switch the bad pixel mask fixing step is repeated
  using the <i>maskfix</i> task and the bad pixel mask. However in the mask step
  it is probable that the bad pixel mask is different from the one used in the
  first pass having been updated in the first pass step.
  </p>
  </section>
  <section id="s_correcting_cosmic_rays_with_the_xzap_or_xznap_tasks">
  <span>2.2.4 Correcting Cosmic Rays with the Xzap or Xznap Tasks</span>
  <p>
  If the <i>mp_xzap</i> switch is the cosmic ray removal step is repeated
  using either the <i>xzap</i> or <i>xnzap</i> tasks. However in the mask step
  the object core mask created from the first pass combined image is used to
  prevent cosmic rays from being detected in the object core regions.
  </p>
  <p>
  If the <i>mp_badpixupdate</i> switch is set the bad pixel mask updating step
  is removed using the <i>badpixupdate</i> task, the bad pixel mask, and
  the cosmic ray masks.
  </p>
  </section>
  <section id="s_combining_images_with_the_xnregistar_task">
  <span>2.2.5 Combining Images with the Xnregistar Task</span>
  <p>
  If the <i>mp_xnregistar</i> switch is yes then the images combining step is
  repeated using the <i>xnregistar</i> task. The final sky subtracted, bad
  pixel corrected, and cosmic ray corrected images are shifted, scaled, combined,
  and reoriented to create the final mosaic.  In this second, more careful, pass
  subpixel shifts are used by default. The default algorithm block replicates
  each image by a factor of <i>mag</i> and shifts the images to a resolution of
  1/<i>mag</i> of a pixel.  The final mosaic image from the mask pass is,
  therefore, approximately <i>mag</i> times larger in each dimension with
  <i>mag * mag</i> times more pixels than the first pass image.  As before an
  exposure map with the same resolution is also created.
  </p>
  </section>
  <section id="s_data_input_and_data_products">
  <span>3. Data Input and Data Products</span>
  </section>
  <section id="s_individual_input_images">
  <span>3.1 Individual Input Images</span>
  <p>
  The individual images may be of any type supported by IRAF, e.g. <span style="font-family: monospace;">".fits"</span> or
  <span style="font-family: monospace;">".imh"</span> but are assumed to be of the same size. They should have been
  dark and flat field corrected prior to entering xdimsum.
  </p>
  </section>
  <section id="s_the_input_bad_pixel_mask">
  <span>3.2 The Input Bad Pixel Mask</span>
  <p>
  The input bad pixel file is an IRAF mask or <span style="font-family: monospace;">".pl"</span> image consisting of 1's and
  0's where the 0's define the bad pixels. It is assumed to be the same size
  as the input images and to be the same for all the input images. The bad
  pixel mask may be updated during the course of the reductions by the
  badpixupdate task. 
  </p>
  </section>
  <section id="s_the_individual_output_corrected_images">
  <span>3.3 The Individual Output Corrected Images</span>
  <p>
  The output corrected images have been sky subtracted by the xslm task,
  bad pixel corrected by the maskfix task, and cosmic ray corrected by the
  xzap or xnzap tasks. These images should be free of defects with mean
  background values around 0.0.
  </p>
  </section>
  <section id="s_the_output_cosmic_ray_masks">
  <span>3.4 The Output Cosmic Ray Masks</span>
  <p>
  The output cosmic ray masks are IRAF pixel mask, i.e. <span style="font-family: monospace;">".pl"</span> images
  produced by the xzap or xnzap tasks. Cosmic ray masks consist of 1's in
  cosmic ray regions and 0's elsewhere.
  </p>
  </section>
  <section id="s_the_output_shifts_file">
  <span>3.5 The Output Shifts File</span>
  <p>
  The output shifts file contains the image name, x and y shifts relative
  to the reference image, and weight required to combine the individual
  corrected images into a single output image and exposure map. The shifts
  file can be produced with the xdshifts task.
  </p>
  </section>
  <section id="s_the_output_objects_masks">
  <span>3.6 The Output Objects Masks</span>
  <p>
  The output objects masks are IRAF pixel masks, i.e. <span style="font-family: monospace;">".pl"</span> images produced
  by the mkmask and maskdereg tasks from the first pass combined image and
  exposure map. They are of two kinds: the inverse object core masks used
  by the xzap or xnzap tasks to unzap cosmic rays in object cores, and the
  object masks used by the xslm task to improve the sky subtraction. The object
  masks consist of 1's in object regions and 0's elsewhere. The inverse object
  masks are the reverse.
  </p>
  </section>
  <section id="s_the_output_holes_masks">
  <span>3.7 The Output Holes Masks</span>
  <p>
  The output holes masks are IRAF pixel masks, i.e. <span style="font-family: monospace;">".pl"</span> images produced by
  the sky subtraction task xslm during the mask pass. They define regions in the
  individual images where the sky subtraction is undefined. Holes masks consist
  of 0's in undefined regions and 1's elsewhere.
  </p>
  </section>
  <section id="s_the_output_combined_image_and_exposure_map">
  <span>3.8 The Output Combined Image and Exposure Map</span>
  <p>
  The first and maskpass steps each produced a combined image and an associated
  exposure map.
  </p>
  </section>
  <section id="s_example">
  <span>4. Example</span>
  <p>
  The following example uses artificial data created by the <i>demos</i> task
  to illustrate the main features of the <i>xmosaic</i> task. 
  </p>
  <p>
  To load the package type <i>xdimsum</i>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; <b>xdimsum</b>
        badpixupdate  maskfix       xdshifts      xmosaic       xslm
        demos         maskstat      xfirstpass    xmshifts      xzap
        iterstat      mkmask        xfshifts      xnregistar
        makemask      orient        xlist         xnzap
        maskdereg     sigmanorm     xmaskpass     xrshifts
  </pre></div>
  <p>
  The main tasks are <b>demos</b> and <b>xmosaic</b>. The remaining tasks are
  called directly by <b>xmosaic</b>.
  </p>
  <p>
  The artificial demonstration data is created by the <i>demos</i> task. By
  default the image format is <span style="font-family: monospace;">".imh"</span>. The the IRAF environment variable
  <i>imdir</i> which defines where the <span style="font-family: monospace;">".pix"</span> pixel files are stored must be
  set before running xmosaic, as shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set imdir = "HDR$pixels/
  </pre></div>
  <p>
  In this the pixel file directory is the subdirectory of the current
  directory called pixels.
  </p>
  <p>
  To use FITS images set the IRAF environment variable as follows
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set imtype = fits
  cl&gt; flpr
  </pre></div>
  <p>
  Now run the demos script and examine the data directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  xd&gt; <b>demos mkxdimsum</b>
  Creating master field (please be patient) ...
  Creating truth image demo_truth ...
  Creating XDIMSUM bad pixel mask demo.pl ...
  Creating image list demo.list ...
  Creating XDIMSUM shift list demo.slist ...
  Creating imcombine offset file demo.imc ...
  Creating demo01 ...
  Creating demo02 ...
  Creating demo03 ...
  Creating demo04 ...
  Creating demo05 ...
  Creating demo06 ...
  Creating demo07 ...
  Creating demo08 ...
  Creating demo09 ...
  Creating demo10 ...
  Creating demo11 ...
  Creating demo12 ...
  Creating demo13 ...
  Creating demo14 ...
  Creating demo15 ...
  Creating demo16 ...
  Creating demo17 ...
  Creating demo18 ...
  Creating demo19 ...
  Creating demo20 ...
  Creating demo21 ...
  Creating demo22 ...
  Creating demo23 ...
  Creating demo24 ...
  Creating demo25 ...
  
  xd&gt; <b>dir</b>
  demo.imc        demo04.imh      demo11.imh      demo18.imh      demo25.imh
  demo.list       demo05.imh      demo12.imh      demo19.imh      demo_truth.imh
  demo.pl         demo06.imh      demo13.imh      demo20.imh      pixels
  demo.slist      demo07.imh      demo14.imh      demo21.imh
  demo01.imh      demo08.imh      demo15.imh      demo22.imh
  demo02.imh      demo09.imh      demo16.imh      demo23.imh
  demo03.imh      demo10.imh      demo17.imh      demo24.imh
  </pre></div>
  <p>
  The files demo??.imh are 25 dithered 100x100 images with low S/N <span style="font-family: monospace;">"taken"</span> in an
  approximately 5x5 pattern. The dither is small so there are large overlaps
  between adjacent images. Each image has a bad column and a few bad pixels. The
  bad pixel mask is in the file demo.pl. Each image also contains a few cosmic
  rays. The input image list is in the file demo.list. The file demo.slist
  contains the relative offsets and weight for each sky subtracted input image.
  The image demo_truth.imh is the image from which the dithered images were
  extracted.  The goal of <b>xdimsum</b> is to come as close to reproducing this
  image as possible.
  </p>
  <p>
  Set up the <b>xmosaic</b> task parameters as shown below using the <b>eparam</b>
  task.  Note that all the processing options are set to <span style="font-family: monospace;">"yes"</span> and all the
  interactive switches are enabled. Because all the interactive processing
  options are enabled the image display window must be open before xmosaic is
  started.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xd&gt; <b>unlearn xmosaic</b>
  xd&gt; <b>epar xmosaic</b>
                                     I R A F
                      Image Reduction and Analysis Facility
  PACKAGE = xdimsum
     TASK = xmosaic
  
  inlist  =           <i>@demo.list</i>  The list of input images
  referenc=               <i>demo13</i>  The reference image in input image list
  output  =               <i>mosaic</i>  Root name for output combined images
  expmap  =                 .exp  Root name for output exposure map image or suffix
  (statsec=                     ) The image section for computing sky stats
  (nsigrej=                   <i>5.</i>) The nsigma rejection for computing sky stats
  (maxiter=                   <i>10</i>) The maximum number of iterations fo computing sk
  
  (fp_xslm=                  yes) Do the first pass sky subtraction step ?
  (mp_xslm=                  yes) Do the mask pass sky subtraction step ?
  (mp_useo=                  yes) Use object mask to compute sky statistics ?
  (sslist =                 .sub) The output sky-subtracted images or suffix
  (hmasks =                 .hom) The output holes masks or suffix
  (forcesc=                  yes) Force recalculation of image medians ?
  (nmean  =                    6) Number of images to use in sky image
  (nreject=                    1) Number of pixels for sky image minmax reject
  (nskymin=                    3) Minimum number of image to use for sky image
  
  (fp_mask=                  yes) Do first pass bad pixel correction step ?
  (mp_mask=                  yes) Do mask pass bad pixel correction step ?
  (bpmask =              <i>demo.pl</i>) The input pixel mask image
  (forcefi=                  yes) Force bad pixel fixing ?
  
  (fp_xzap=                  yes) Do first pass cosmic ray correction step ?
  (mp_xzap=                  yes) Do mask pass cosmic ray correction step ?
  (crmasks=                 .crm) The output cosmic ray masks or suffix
  (newxzap=                   no) Use new version of xzap ?
  (fp_badp=                  yes) Do first pass bad pixel mask update ?
  (mp_badp=                  yes) Do mask pass bad pixel mask update ?
  
  (fp_mksh=                  <i>yes</i>) Determine shifts interactively ?
  (fp_chks=                  yes) Check and confirm new shifts  ?
  (fp_crad=                   5.) Centroiding radius in pixels for mkshifts
  (fp_maxs=                   5.) Maximum centroiding shift in pixels for mkshifts
  
  (fp_xnre=                  yes) Do first pass image combining step ?
  (mp_xnre=                  yes) Do mask pass image combining step ?
  (mp_mag =                    4) Magnification factor for mask pass output image
  (mp_blk =                  yes) Use block replication to magnify the image ?
  (shiftli=          <i>myshiftlist</i>) Input or output shifts file
  (section=             .corners) The output sections file or suffix
  (fractio=                   no) Use fractional pixel shifts if mag = 1 ?
  (pixin  =                  yes) Are input coords in ref object pixels ?
  (ab_sens=                  yes) Is A through B counterclockwise ?
  (xscale =                   1.) X pixels per A coordinate unit
  (yscale =                   1.) Y pixels per B coordinate unit
  (a2x_ang=                   0.) Angle in degrees from A CCW to X
  (ncoavg =                    1) Number of internal coaverages per frame
  (secpexp=                  <i>60.</i>) Seconds per unit exposure time
  (y2n_ang=                   0.) Angle in degrees from Y to N N through E
  (rotatio=                  yes) Is N through E counterclockwise?
  
  (mp_mkma=                  yes) Create the combined image object mask ?
  (omask  =                 .msk) The output combined image mask or suffix
  (mp_chkm=                 <i>yes</i>) Check the object masks ?
  (mp_kpch=                  yes) Keep checking the object masks ?
  (mp_stat=                     ) The combined image section for computing mask st
  (mp_nsig=                  1.5) The nsigma factor for cosmic ray masking
  (mp_nsig=                  1.1) The nsigma factor for object masking
  
  (mp_mask=                  yes) Deregister masks ?
  (ocrmask=                 .ocm) The output cosmic ray unzapping masks or suffix
  (objmask=                 .obm) The output object masks or suffix
  (mp_npre=                    0) Number of previous object masks to combine
  
  (del_big=                   no) Delete combined image masks at task termination
  (del_sma=                   no) Delete the individual object masks at task termi
  
  (mode   =                   ql)
  
  </pre></div>
  <p>
  The <i>xmosaic</i> parameters have been set to produce the same results as the
  original DIMSUM package <i>reduce</i> task. 
  </p>
  <p>
  Before starting <i>xmosaic|fR make sure that the hidden fInsigrej</i>,
  <i>maxiter</i>, <i>bpmask</i>, <i>shiftlist</i>, <i>secpexp</i>, and <i>ncoavg</i>
  parameters are set correctly.
  </p>
  <p>
  If either of the <i>fp_mkshifts</i> or <i>mp_chkmasks</i> parameters are set
  to yes then make sure the image display server is running before starting
  xmosaic.
  </p>
  <p>
  To view the xmosaic help page use the <i>phelp</i> task as shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; phelp xmosaic
  </pre></div>
  <p>
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  xd&gt; <b>xmosaic</b>
  
  Xmosaic starts by querying for the input image list, the reference image name,
  and the root output image and exposure map names as shown below.
  
  The list of input images (@demo.list):
  The reference image in input image list (demo13):
  Root name for output combined images (mosaic):
  Root name for output exposure map image or suffix (.exp):
  </pre></div>
  <p>
  First some time and data information is printed.
  </p>
  <div class="highlight-default-notranslate"><pre>
  start xmosaic
  Wed 16:24:50 29-Nov-2000
  
  start xfirstpass
  Wed 16:24:54 29-Nov-2000
  </pre></div>
  <p>
  Now the xslm task computes the scaling factor for each input image and
  stores it in the input image header keyword SKYMED.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Begin first pass sky subtraction
  Wed 16:24:55 29-Nov-2000
  -------Sky subtracting images with xslm--------------
  Calculating scaling for demo01
      Setting scaling factor to 1 / 4542.815
  Calculating scaling for demo02
      Setting scaling factor to 1 / 4581.675
  Calculating scaling for demo03
      Setting scaling factor to 1 / 4622.226
  Calculating scaling for demo04
      Setting scaling factor to 1 / 4662.35
  Calculating scaling for demo05
      Setting scaling factor to 1 / 4701.921
  Calculating scaling for demo06
      Setting scaling factor to 1 / 4742.414
  Calculating scaling for demo07
      Setting scaling factor to 1 / 4781.861
  Calculating scaling for demo08
      Setting scaling factor to 1 / 4821.828
  Calculating scaling for demo09
      Setting scaling factor to 1 / 4862.715
  Calculating scaling for demo10
      Setting scaling factor to 1 / 4900.551
  Calculating scaling for demo11
      Setting scaling factor to 1 / 4942.805
  Calculating scaling for demo12
      Setting scaling factor to 1 / 4983.287
  Calculating scaling for demo13
      Setting scaling factor to 1 / 5021.519
  Calculating scaling for demo14
      Setting scaling factor to 1 / 5061.425
  Calculating scaling for demo15
      Setting scaling factor to 1 / 5101.519
  Calculating scaling for demo16
      Setting scaling factor to 1 / 5141.901
  Calculating scaling for demo17
      Setting scaling factor to 1 / 5183.9
  Calculating scaling for demo18
      Setting scaling factor to 1 / 5221.122
  Calculating scaling for demo19
      Setting scaling factor to 1 / 5262.929
  Calculating scaling for demo20
      Setting scaling factor to 1 / 5303.046
  Calculating scaling for demo21
      Setting scaling factor to 1 / 5342.895
  Calculating scaling for demo22
      Setting scaling factor to 1 / 5382.554
  Calculating scaling for demo23
      Setting scaling factor to 1 / 5421.473
  Calculating scaling for demo24
      Setting scaling factor to 1 / 5460.839
  Calculating scaling for demo25
      Setting scaling factor to 1 / 5500.626
  </pre></div>
  <p>
  Once the scaling factors are determined a set of neighboring images and are
  scaled and combined to produce the sky image for each input image. The sky
  image is subtracted from the input image to produce the sky subtracted image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Creating sky subtracted image demo01.sub
      Frame  1  Sky frames:  start = 1   finish = 4   nreject = 1
  Creating sky subtracted image demo02.sub
      Frame  2  Sky frames:  start = 1   finish = 4   nreject = 1
  Creating sky subtracted image demo03.sub
      Frame  3  Sky frames:  start = 1   finish = 5   nreject = 1
  Creating sky subtracted image demo04.sub
      Frame  4  Sky frames:  start = 1   finish = 7   nreject = 1
  Creating sky subtracted image demo05.sub
      Frame  5  Sky frames:  start = 2   finish = 8   nreject = 1
  Creating sky subtracted image demo06.sub
      Frame  6  Sky frames:  start = 3   finish = 9   nreject = 1
  Creating sky subtracted image demo07.sub
      Frame  7  Sky frames:  start = 4   finish = 10   nreject = 1
  Creating sky subtracted image demo08.sub
      Frame  8  Sky frames:  start = 5   finish = 11   nreject = 1
  Creating sky subtracted image demo09.sub
      Frame  9  Sky frames:  start = 6   finish = 12   nreject = 1
  Creating sky subtracted image demo10.sub
      Frame  10  Sky frames:  start = 7   finish = 13   nreject = 1
  Creating sky subtracted image demo11.sub
      Frame  11  Sky frames:  start = 8   finish = 14   nreject = 1
  Creating sky subtracted image demo12.sub
      Frame  12  Sky frames:  start = 9   finish = 15   nreject = 1
  Creating sky subtracted image demo13.sub
      Frame  13  Sky frames:  start = 10   finish = 16   nreject = 1
  Creating sky subtracted image demo14.sub
      Frame  14  Sky frames:  start = 11   finish = 17   nreject = 1
  Creating sky subtracted image demo15.sub
      Frame  15  Sky frames:  start = 12   finish = 18   nreject = 1
  Creating sky subtracted image demo16.sub
      Frame  16  Sky frames:  start = 13   finish = 19   nreject = 1
  Creating sky subtracted image demo17.sub
      Frame  17  Sky frames:  start = 14   finish = 20   nreject = 1
  Creating sky subtracted image demo18.sub
      Frame  18  Sky frames:  start = 15   finish = 21   nreject = 1
  Creating sky subtracted image demo19.sub
      Frame  19  Sky frames:  start = 16   finish = 22   nreject = 1
  Creating sky subtracted image demo20.sub
      Frame  20  Sky frames:  start = 17   finish = 23   nreject = 1
  Creating sky subtracted image demo21.sub
      Frame  21  Sky frames:  start = 18   finish = 24   nreject = 1
  Creating sky subtracted image demo22.sub
      Frame  22  Sky frames:  start = 19   finish = 25   nreject = 1
  Creating sky subtracted image demo23.sub
      Frame  23  Sky frames:  start = 21   finish = 25   nreject = 1
  Creating sky subtracted image demo24.sub
      Frame  24  Sky frames:  start = 22   finish = 25   nreject = 1
  Creating sky subtracted image demo25.sub
      Frame  25  Sky frames:  start = 22   finish = 25   nreject = 1
  </pre></div>
  <p>
  The subtracted images are stored in the  <span style="font-family: monospace;">"*.sub.imh"</span> images.
  </p>
  <p>
  Next the maskfix task uses the bad pixel mask file demo.pl to interpolate
  over the bad pixel regions in the sky subtracted images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Begin first pass bad pixel correction
  Wed 16:28:45 29-Nov-2000
  -------Correcting bad pixels with maskfix------------
  Fixing bad pixels in file demo01.sub using mask demo.pl
  Fixing bad pixels in file demo02.sub using mask demo.pl
  Fixing bad pixels in file demo03.sub using mask demo.pl
  Fixing bad pixels in file demo04.sub using mask demo.pl
  Fixing bad pixels in file demo05.sub using mask demo.pl
  Fixing bad pixels in file demo06.sub using mask demo.pl
  Fixing bad pixels in file demo07.sub using mask demo.pl
  Fixing bad pixels in file demo08.sub using mask demo.pl
  Fixing bad pixels in file demo09.sub using mask demo.pl
  Fixing bad pixels in file demo10.sub using mask demo.pl
  Fixing bad pixels in file demo11.sub using mask demo.pl
  Fixing bad pixels in file demo12.sub using mask demo.pl
  Fixing bad pixels in file demo13.sub using mask demo.pl
  Fixing bad pixels in file demo14.sub using mask demo.pl
  Fixing bad pixels in file demo15.sub using mask demo.pl
  Fixing bad pixels in file demo16.sub using mask demo.pl
  Fixing bad pixels in file demo17.sub using mask demo.pl
  Fixing bad pixels in file demo18.sub using mask demo.pl
  Fixing bad pixels in file demo19.sub using mask demo.pl
  Fixing bad pixels in file demo20.sub using mask demo.pl
  Fixing bad pixels in file demo21.sub using mask demo.pl
  Fixing bad pixels in file demo22.sub using mask demo.pl
  Fixing bad pixels in file demo23.sub using mask demo.pl
  Fixing bad pixels in file demo24.sub using mask demo.pl
  Fixing bad pixels in file demo25.sub using mask demo.pl
  </pre></div>
  <p>
  Next the xzap task is used to detect and remove cosmic rays from the
  sky subtracted images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Begin first pass cosmic ray removal
  Wed 16:29:03 29-Nov-2000
  -------Zapping cosmic rays using xzap   -------------
  Creating cosmic ray corrected image demo01.sub
  Creating cosmic ray corrected image demo02.sub
  Creating cosmic ray corrected image demo03.sub
  Creating cosmic ray corrected image demo04.sub
  Creating cosmic ray corrected image demo05.sub
  Creating cosmic ray corrected image demo06.sub
  Creating cosmic ray corrected image demo07.sub
  Creating cosmic ray corrected image demo08.sub
  Creating cosmic ray corrected image demo09.sub
  Creating cosmic ray corrected image demo10.sub
  Creating cosmic ray corrected image demo11.sub
  Creating cosmic ray corrected image demo12.sub
  Creating cosmic ray corrected image demo13.sub
  Creating cosmic ray corrected image demo14.sub
  Creating cosmic ray corrected image demo15.sub
  Creating cosmic ray corrected image demo16.sub
  Creating cosmic ray corrected image demo17.sub
  Creating cosmic ray corrected image demo18.sub
  Creating cosmic ray corrected image demo19.sub
  Creating cosmic ray corrected image demo20.sub
  Creating cosmic ray corrected image demo21.sub
  Creating cosmic ray corrected image demo22.sub
  Creating cosmic ray corrected image demo23.sub
  Creating cosmic ray corrected image demo24.sub
  Creating cosmic ray corrected image demo25.sub
  
  The cosmic ray masks are stored in the files "*.sub.crm.pl".
  
  Next the badpixupdate task and the cosmic ray masks are used to update the
  bad pixel mask. Pixels that are bad in 3 or more cosmic ray masks are
  assumed to be bad in the bad pixel mask.
  
  Begin first pass bad pixel mask update
  Wed 16:29:43 29-Nov-2000
  -------Updating bad pixel file with badpixupdate ----
  
  </pre></div>
  <p>
  By default the image registration step is non-interactive, i.e. 
  <i>fp_mkshifts</i> = no. In this case the user must supply a shifts file
  <i>shiftlist</i> which contains the image name, xshift, yshift, and weight or
  exposure time of the images to be combined. See the file demo.slist for a
  sample shifts file. In general it is usually easier to determine the shifts
  outside of the main xmosaic script with the <i>xdshifts</i> task than it
  is to determine it inside the xmosaic task where a mistake is more
  costly. Users with time series data,  i.e. data where each image is shifted by a
  comparable amount from the previous one, the <i>xmshifts</i>, <i>xfshifts</i>,
  or <i>xrshifts</i> tasks can be used to compute the required shifts file.
  </p>
  <p>
  The following example shows show to make the shift list interactively from the
  mosaic task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  The first sky subtracted image is loaded into the image display by the
  <b>imexamine</b> task and the n and p keys are used to examine each image in
  order to select an object common to all.
  
  Examine images ...
      Select reference star which is present in all images
      Type n key to display next image
      Type p key to display previous image
      Type q key to quit
  </pre></div>
  <p>
  Examine all the images and select the star above and slightly to the right
  of the galaxy as the reference star. Type <span style="font-family: monospace;">'q'</span> to quit the image examining
  menu.
  </p>
  <p>
  Now the first image in the sky subtracted image list is displayed, the
  temporary file <i>myshiftlist.exam</i> is opened. Mark the reference object
  with the <span style="font-family: monospace;">'a'</span> keystroke, move to the next image with <span style="font-family: monospace;">'n'</span> keystroke, mark the
  reference object with the <span style="font-family: monospace;">'a'</span> key, ... Repeat until all the images have
  been displayed and the reference object marked.  The reference object selected
  must be common to all images. The first image is display automatically and then
  subsequent images are displayed by typing <span style="font-family: monospace;">'n'</span>. DO NOT TYPE <span style="font-family: monospace;">'q'</span> UNTIL ALL IMAGES
  HAVE BEEN MARKED.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Determine relative shifts using above reference star ...
      Move cursor to the selected star
      Type a key to measure the selected star
      Type n key to move to the next image
      Type q key to quit
  
  Log file myshiftlist.exam open
  #   COL    LINE COORDINATES
  #     R    MAG    FLUX     SKY    PEAK    E   PA      ENCLOSED GAUSSIAN DIRECT
    63.90   47.13 63.90 47.13
    13.18  15.80   4778.  -1.094   325.2 INDEF   -6          3.96     4.20   4.16
    57.42   47.25 57.42 47.25
     7.79  16.38   2810.   3.951   424.7 INDEF  -55          3.99     3.38   3.61
    50.86   46.68 50.86 46.68
     9.29  15.93   4244.   5.545   396.2 INDEF    8          3.46     3.21   3.10
    44.51   46.73 44.51 46.73
     7.30  15.58   5837.  -1.388   463.3 0.61   68          3.65     2.93   2.44
    37.93   46.40 37.93 46.40
     8.47  15.70   5257.  -1.161   463.6 INDEF   29          3.36     2.82   2.55
    62.60   40.00 62.60 40.00
    10.79  15.34   7332.   1.875   352.8 0.69  -52          3.94     4.24   3.15
    56.06   39.90 56.06 39.90
     9.33  15.68   5326.   6.569    358. 1.02    5          3.66     3.73   3.88
    51.00   40.90 51.00 40.90
     9.88  15.80   4782.   7.608   408.1 INDEF  -64          3.89     3.26   3.19
    44.88   40.71 44.88 40.71
     6.64  15.79   4829.   6.467   517.4 1.62   28          2.86     2.42   2.16
    38.05   40.83 38.05 40.83
     8.44  15.77   4916. -0.1289   439.2 7.41   76          3.98     2.90   3.17
    63.07   34.29 63.07 34.29
    14.95  15.75   5014.   1.413   378.6 0.08  -22         17.97     3.74  13.72
    56.74   33.84 56.74 33.84
    10.58  15.59   5797.   1.553   384.7 1.19   83          3.83     3.39   3.78
    50.11   33.58 50.11 33.58
    13.60  15.60   5768.   4.054   352.1 49.8  -66          5.24     4.14   6.12
    43.37   33.46 43.37 33.46
     8.73  15.72   5159. -0.7891   381.1 INDEF    5          3.99     3.58   3.25
    39.14   34.82 39.14 34.82
     9.22  15.64   5549.  -1.216   381.9 INDEF   51          4.14     3.38   3.08
    63.10   28.36 63.10 28.36
     9.78  15.24   8045.  -2.753    353. 0.43  -82          6.23     3.74   3.19
    57.05   28.32 57.05 28.32
     7.34  15.48   6430.   1.968   400.7 0.44  -60          4.41     3.28   3.08
    50.47   28.01 50.47 28.01
    17.98  INDEF  -5523.   9.998   INDEF INDEF INDEF         37.04    INDEF  33.41
    43.59   27.71 43.59 27.71
    13.87  16.20   3311.   3.808   353.9 INDEF  -50          7.69     3.61   4.73
    37.66   27.21 37.66 27.21
     7.27  15.39   6972.  0.3169   464.5 0.16  -56          4.07     2.59   2.23
    62.16   21.07 62.16 21.07
     9.41  15.13   8856. -0.9043   415.9 0.14  -30          6.50     3.27   3.22
    57.73   22.19 57.73 22.19
    11.48  16.06   3754.   1.908   346.4 INDEF   80          4.52     3.87   4.43
    51.10   22.17 51.10 22.17
     8.89  15.76   4978.    4.53   420.9 INDEF   86          3.68     3.20   2.92
    44.61   21.66 44.61 21.66
     7.61  15.59   5794.   4.416   376.1 0.88  -81          4.25     3.56   3.28
    38.24   21.86 38.24 21.86
    12.19  16.08   3703.   8.723   319.3 INDEF  -21          8.00     3.85   5.54
  </pre></div>
  <p>
  Because <i>mp_chkshifts</i> = yes the output of <b>imexamine</b> is displayed
  with the editor. This allows deleting multiple measurements or other incorrect
  data. In the above example there are no mistakes and the file does
  not need to be modified. The final file looks like this
  </p>
  <div class="highlight-default-notranslate"><pre>
  # [1] demo01.sub.imh - Example artificial galaxy cluster
  #   COL    LINE COORDINATES      R    MAG    FLUX     SKY    PEAK    E   PA
   ENCLOSED GAUSSIAN DIRECT
    63.90   47.13 63.90 47.13  13.18  15.80   4778.  -1.094   325.2 INDEF   -6
        3.96     4.20   4.16
  # [2] demo02.sub.imh - Example artificial galaxy cluster
    57.42   47.25 57.42 47.25   7.79  16.38   2810.   3.951   424.7 INDEF  -55
        3.99     3.38   3.61
  # [3] demo03.sub.imh - Example artificial galaxy cluster
    50.86   46.68 50.86 46.68   9.29  15.93   4244.   5.545   396.2 INDEF    8
        3.46     3.21   3.10
  # [4] demo04.sub.imh - Example artificial galaxy cluster
    44.51   46.73 44.51 46.73   7.30  15.58   5837.  -1.388   463.3 0.61   68
       3.65     2.93   2.44
  # [5] demo05.sub.imh - Example artificial galaxy cluster
    37.93   46.40 37.93 46.40   8.47  15.70   5257.  -1.161   463.6 INDEF   29
        3.36     2.82   2.55
  # [6] demo06.sub.imh - Example artificial galaxy cluster
    62.60   40.00 62.60 40.00  10.79  15.34   7332.   1.875   352.8 0.69  -52
       3.94     4.24   3.15
  # [7] demo07.sub.imh - Example artificial galaxy cluster
    56.06   39.90 56.06 39.90   9.33  15.68   5326.   6.569    358. 1.02    5
       3.66     3.73   3.88
  # [8] demo08.sub.imh - Example artificial galaxy cluster
    51.00   40.90 51.00 40.90   9.88  15.80   4782.   7.608   408.1 INDEF  -64
        3.89     3.26   3.19
  # [9] demo09.sub.imh - Example artificial galaxy cluster
    44.88   40.71 44.88 40.71   6.64  15.79   4829.   6.467   517.4 1.62   28
       2.86     2.42   2.16
  # [10] demo10.sub.imh - Example artificial galaxy cluster
    38.05   40.83 38.05 40.83   8.44  15.77   4916. -0.1289   439.2 7.41   76
       3.98     2.90   3.17
  # [11] demo11.sub.imh - Example artificial galaxy cluster
    63.07   34.29 63.07 34.29  14.95  15.75   5014.   1.413   378.6 0.08  -22
      17.97     3.74  13.72
  # [12] demo12.sub.imh - Example artificial galaxy cluster
    56.74   33.84 56.74 33.84  10.58  15.59   5797.   1.553   384.7 1.19   83
       3.83     3.39   3.78
  # [13] demo13.sub.imh - Example artificial galaxy cluster
    50.11   33.58 50.11 33.58  13.60  15.60   5768.   4.054   352.1 49.8  -66
       5.24     4.14   6.12
  # [14] demo14.sub.imh - Example artificial galaxy cluster
    43.37   33.46 43.37 33.46   8.73  15.72   5159. -0.7891   381.1 INDEF    5
        3.99     3.58   3.25
  # [15] demo15.sub.imh - Example artificial galaxy cluster
    39.14   34.82 39.14 34.82   9.22  15.64   5549.  -1.216   381.9 INDEF   51
        4.14     3.38   3.08
  # [16] demo16.sub.imh - Example artificial galaxy cluster
    63.10   28.36 63.10 28.36   9.78  15.24   8045.  -2.753    353. 0.43  -82
       6.23     3.74   3.19
  # [17] demo17.sub.imh - Example artificial galaxy cluster
    57.05   28.32 57.05 28.32   7.34  15.48   6430.   1.968   400.7 0.44  -60
       4.41     3.28   3.08
  # [18] demo18.sub.imh - Example artificial galaxy cluster
    50.47   28.01 50.47 28.01  17.98  INDEF  -5523.   9.998   INDEF INDEF INDEF
        37.04    INDEF  33.41
  # [19] demo19.sub.imh - Example artificial galaxy cluster
    43.59   27.71 43.59 27.71  13.87  16.20   3311.   3.808   353.9 INDEF  -50
        7.69     3.61   4.73
  # [20] demo20.sub.imh - Example artificial galaxy cluster
    37.66   27.21 37.66 27.21   7.27  15.39   6972.  0.3169   464.5 0.16  -56
       4.07     2.59   2.23
  # [21] demo21.sub.imh - Example artificial galaxy cluster
    62.16   21.07 62.16 21.07   9.41  15.13   8856. -0.9043   415.9 0.14  -30
       6.50     3.27   3.22
  # [22] demo22.sub.imh - Example artificial galaxy cluster
    57.73   22.19 57.73 22.19  11.48  16.06   3754.   1.908   346.4 INDEF   80
        4.52     3.87   4.43
  # [23] demo23.sub.imh - Example artificial galaxy cluster
    51.10   22.17 51.10 22.17   8.89  15.76   4978.    4.53   420.9 INDEF   86
        3.68     3.20   2.92
  # [24] demo24.sub.imh - Example artificial galaxy cluster
    44.61   21.66 44.61 21.66   7.61  15.59   5794.   4.416   376.1 0.88  -81
       4.25     3.56   3.28
  # [25] demo25.sub.imh - Example artificial galaxy cluster
    38.24   21.86 38.24 21.86  12.19  16.08   3703.   8.723   319.3 INDEF  -21
        8.00     3.85   5.54
  </pre></div>
  <p>
  Next mark as many stars (or compact objects) as can be reliably measured in
  the reference image as instructed below. In this example only the star we
  selected as the reference stars is suitable.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Select reference image registration stars ...
      Move to reference star measured previously
      Type a to measure reference star
      Move to other promising looking stars
      Type a to measure other registration stars
      Type q key to quit
  
  Log file myshiftlist.stars open
  #   COL    LINE COORDINATES
  #     R    MAG    FLUX     SKY    PEAK    E   PA      ENCLOSED GAUSSIAN DIRECT
    50.17   33.61 50.17 33.61
    13.56  15.90   4378.   5027.   376.8 INDEF  -51          4.79     3.84   4.75
  </pre></div>
  <p>
  As before  the marked objects are displayed with the editor and again the file
  does not have to be edited.  The final file appears as shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
   [1] demo13 - Example artificial galaxy cluster
  #   COL    LINE COORDINATES      R    MAG    FLUX     SKY    PEAK    E   PA
   ENCLOSED GAUSSIAN DIRECT
    50.20   33.54 50.20 33.54  13.56  15.88   4439.   5027.   359.3 INDEF  -53
        4.79     4.02   4.75
  </pre></div>
  <p>
  The position of the reference objects in each of the input images
  is measured with the <b>xdimsum.ximcentroid</b> task using the initial shifts
  determined from the object common to all the images and final offsets
  relative to the reference image are computed.  The measurements are recorded
  in the file <i>shiftlist</i>  which can be reviewed using the editor. The final
  shifts file is shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  demo01.sub.imh  13.966 13.554 1.0
  demo02.sub.imh  7.718 13.360 1.0
  demo03.sub.imh  0.751 12.866 1.0
  demo04.sub.imh  -5.438 12.733 1.0
  demo05.sub.imh  -11.825 12.675 1.0
  demo06.sub.imh  12.663 6.243 1.0
  demo07.sub.imh  6.204 5.880 1.0
  demo08.sub.imh  1.320 7.394 1.0
  demo09.sub.imh  -5.090 7.054 1.0
  demo10.sub.imh  -11.789 7.198 1.0
  demo11.sub.imh  13.352 0.354 1.0
  demo12.sub.imh  6.719 0.039 1.0
  demo13.sub.imh  -0.064 -0.073 1.0
  demo14.sub.imh  -6.832 -0.273 1.0
  demo15.sub.imh  -11.140 0.899 1.0
  demo16.sub.imh  13.723 -5.582 1.0
  demo17.sub.imh  6.996 -5.604 1.0
  demo18.sub.imh  0.500 -5.827 1.0
  demo19.sub.imh  -6.102 -6.268 1.0
  demo20.sub.imh  -12.949 -6.568 1.0
  demo21.sub.imh  12.097 -12.923 1.0
  demo22.sub.imh  8.005 -11.602 1.0
  demo23.sub.imh  1.074 -11.789 1.0
  demo24.sub.imh  -5.114 -12.033 1.0
  demo25.sub.imh  -12.087 -11.925 1.0
  </pre></div>
  <p>
  The shifts file  is used to register the images and combine them with
  exposure time weighting.  An exposure map is also created.  These images
  are the first pass mosaic and exposure map.  The images are stored
  in the file mosaic_fp.imh and mosaic_fp.exp.imh. The xnregistar task is
  used to do the image combining step.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ------- Checking the shiftlist---------------------------
  Begin first pass image combining
  Wed 16:29:46 29-Nov-2000
  -------Coadding images using xnregistar --------------
  Creating individual composite masks ...
  Using bad pixel mask file: demo.pl
  Creating mask for image: demo01.sub
  Creating mask for image: demo02.sub
  Creating mask for image: demo03.sub
  Creating mask for image: demo04.sub
  Creating mask for image: demo05.sub
  Creating mask for image: demo06.sub
  Creating mask for image: demo07.sub
  Creating mask for image: demo08.sub
  Creating mask for image: demo09.sub
  Creating mask for image: demo10.sub
  Creating mask for image: demo11.sub
  Creating mask for image: demo12.sub
  Creating mask for image: demo13.sub
  Creating mask for image: demo14.sub
  Creating mask for image: demo15.sub
  Creating mask for image: demo16.sub
  Creating mask for image: demo17.sub
  Creating mask for image: demo18.sub
  Creating mask for image: demo19.sub
  Creating mask for image: demo20.sub
  Creating mask for image: demo21.sub
  Creating mask for image: demo22.sub
  Creating mask for image: demo23.sub
  Creating mask for image: demo24.sub
  Creating mask for image: demo25.sub
  Combining the input images ...
  Combining the exposure time images ...
  
  After registration the final mosaic and exposure map are reoriented so
  that north is up and east is to the left. In this example the images are left
  in their observed orientation.  The effective exposure time and other header
  parameters in the final mosaic are updated.
  
  finish xfirstpass
  Wed 16:30:19 29-Nov-2000
  
  </pre></div>
  <p>
  This marks the end of the first pass.
  </p>
  <p>
  The mask pass begins by calling the mkmask task to create a mask of the object
  cores. Mkmask uses the first pass combined image, first pass exposure map, and
  first pass offsets file, to create the mask object cores mask. The maskdereg
  task <span style="font-family: monospace;">"deregisters"</span> this mask to create object core masks for the individual
  images. The object cores masks are used to unzap cosmic rays detected in
  the cores of images during the first pass.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Wed 16:30:19 29-Nov-2000
  start xmaskpass
  Wed 16:30:19 29-Nov-2000
  
  Begin mask pass inverse object mask creation
  Wed 16:30:20 29-Nov-2000
  -------Making mask for unzapping object cores ------------
  Recommended thresholding level for mask is 0.32639925
  z1=-0.6386976 z2=1.241897
  </pre></div>
  <p>
  By default the main object cores mask is created automatically. However
  if <i>chkmasks</i> is yes the process is interactive.  In this case the first
  pass combined image normalized by the exposure map is displayed with
  <b>imexamine</b> and the recommended threshold value is printed on the terminal,
  and the user is prompted for a new cutoff value which is interpreted as a
  value above the median background. The user can use the imexamine commands
  like <span style="font-family: monospace;">'m'</span>, <span style="font-family: monospace;">'l'</span>, and <span style="font-family: monospace;">'c'</span> to determine this cutoff.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Cutoff point for replacement: <b>.32</b>
  </pre></div>
  <p>
  Now the first pass mosaic image and the computed mask are displayed and the
  user can decide whether or not to make a new mask with a different threshold.
  In the example type <span style="font-family: monospace;">"no"</span>.  The mask is then deregistered.
  </p>
  <div class="highlight-default-notranslate"><pre>
  z1=-1.261593 z2=1.342784
  z1=0. z2=1.
  Keep checking mask? (yes): <b>no</b>
  -------Inverting mask for unzapping ----------------------
  Begin mask pass individual inverse object mask creation
  Wed 16:30:37 29-Nov-2000
  -------Deregistering unzap mask subsections ---------------
  Making object masks for image: demo01
  Making object masks for image: demo02
  Making object masks for image: demo03
  Making object masks for image: demo04
  Making object masks for image: demo05
  Making object masks for image: demo06
  Making object masks for image: demo07
  Making object masks for image: demo08
  Making object masks for image: demo09
  Making object masks for image: demo10
  Making object masks for image: demo11
  Making object masks for image: demo12
  Making object masks for image: demo13
  Making object masks for image: demo14
  Making object masks for image: demo15
  Making object masks for image: demo16
  Making object masks for image: demo17
  Making object masks for image: demo18
  Making object masks for image: demo19
  Making object masks for image: demo20
  Making object masks for image: demo21
  Making object masks for image: demo22
  Making object masks for image: demo23
  Making object masks for image: demo24
  Making object masks for image: demo25
  </pre></div>
  <p>
  The individual object core masks are stored in the file <span style="font-family: monospace;">"*.sub.ocm.pl.
  The master object core mask is stored in the file "</span>mosaic_fp.mski.pl<span style="font-family: monospace;">".
  </p>
  <p>
  Next a lower threshold mask of the full objects is now made.  The same steps of
  image display and threshold adjustment are performed as in the previous step
  and the new object mask is also deregistered.  The object masks are used in a
  second pass of sky subtraction to avoid using pixels covered by faint objects
  as part of the sky.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Begin mask pass object mask creation
  Wed 16:30:39 29-Nov-2000
  -------Making mask for sky subtraction -------------------
  Recommended thresholding level for mask is 0.32639925
  z1=-0.6386976 z2=1.241897
  
  Cutoff point for replacement: <b>.32</b>
  z1=-1.261593 z2=1.342784
  z1=0. z2=1.
  Keep checking mask? (yes): <b>no</b>
  
  Begin mask pass individual object mask creation
  Wed 16:30:59 29-Nov-2000
  -------Deregistering sky subtraction mask subsections -----
  Making object masks for image: demo01
  Making object masks for image: demo02
  Making object masks for image: demo03
  Making object masks for image: demo04
  Making object masks for image: demo05
  Making object masks for image: demo06
  Making object masks for image: demo07
  Making object masks for image: demo08
  Making object masks for image: demo09
  Making object masks for image: demo10
  Making object masks for image: demo11
  Making object masks for image: demo12
  Making object masks for image: demo13
  Making object masks for image: demo14
  Making object masks for image: demo15
  Making object masks for image: demo16
  Making object masks for image: demo17
  Making object masks for image: demo18
  Making object masks for image: demo19
  Making object masks for image: demo20
  Making object masks for image: demo21
  Making object masks for image: demo22
  Making object masks for image: demo23
  Making object masks for image: demo24
  Making object masks for image: demo25
  </pre></div>
  <p>
  The individual object masks are stored in the file <span style="font-family: monospace;">"*.sub.obm.pl"</span> and
  the mask object mask is stored in the file <span style="font-family: monospace;">"mosaic_fp.msk.pl"</span>.
  </p>
  <p>
  Next the sky subtracted images are recomputed using the object masks
  created above to eliminate objects from both the sky statistics computation
  and the image combining step. For some images a holes mask may also be created.
  Holes mask define regions of the sky subtracted data which are undefined,
  i.e. contain no data. The holes mask are used in the image combining
  step to compute the combined image and the exposure map.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Begin mask pass sky subtraction
  Wed 16:31:01 29-Nov-2000
  Calculating scaling for demo01
      Using object mask : demo01.sub.obm.pl
      Setting scaling factor to 1 / 4540.263
  Calculating scaling for demo02
      Using object mask : demo02.sub.obm.pl
      Setting scaling factor to 1 / 4580.704
  Calculating scaling for demo03
      Using object mask : demo03.sub.obm.pl
      Setting scaling factor to 1 / 4621.996
  Calculating scaling for demo04
      Using object mask : demo04.sub.obm.pl
      Setting scaling factor to 1 / 4660.359
  Calculating scaling for demo05
      Using object mask : demo05.sub.obm.pl
      Setting scaling factor to 1 / 4701.139
  Calculating scaling for demo06
      Using object mask : demo06.sub.obm.pl
      Setting scaling factor to 1 / 4739.956
  Calculating scaling for demo07
      Using object mask : demo07.sub.obm.pl
      Setting scaling factor to 1 / 4780.889
  Calculating scaling for demo08
      Using object mask : demo08.sub.obm.pl
      Setting scaling factor to 1 / 4820.484
  Calculating scaling for demo09
      Using object mask : demo09.sub.obm.pl
      Setting scaling factor to 1 / 4860.14
  Calculating scaling for demo10
      Using object mask : demo10.sub.obm.pl
      Setting scaling factor to 1 / 4899.388
  Calculating scaling for demo11
      Using object mask : demo11.sub.obm.pl
      Setting scaling factor to 1 / 4941.429
  Calculating scaling for demo12
      Using object mask : demo12.sub.obm.pl
      Setting scaling factor to 1 / 4981.195
  Calculating scaling for demo13
      Using object mask : demo13.sub.obm.pl
      Setting scaling factor to 1 / 5019.37
  Calculating scaling for demo14
      Using object mask : demo14.sub.obm.pl
      Setting scaling factor to 1 / 5061.904
  Calculating scaling for demo15
      Using object mask : demo15.sub.obm.pl
      Setting scaling factor to 1 / 5100.764
  Calculating scaling for demo16
      Using object mask : demo16.sub.obm.pl
      Setting scaling factor to 1 / 5140.057
  Calculating scaling for demo17
      Using object mask : demo17.sub.obm.pl
      Setting scaling factor to 1 / 5181.636
  Calculating scaling for demo18
      Using object mask : demo18.sub.obm.pl
      Setting scaling factor to 1 / 5220.013
  Calculating scaling for demo19
      Using object mask : demo19.sub.obm.pl
      Setting scaling factor to 1 / 5261.546
  Calculating scaling for demo20
      Using object mask : demo20.sub.obm.pl
      Setting scaling factor to 1 / 5300.255
  Calculating scaling for demo21
      Using object mask : demo21.sub.obm.pl
      Setting scaling factor to 1 / 5340.667
  Calculating scaling for demo22
      Using object mask : demo22.sub.obm.pl
      Setting scaling factor to 1 / 5379.909
  Calculating scaling for demo23
      Using object mask : demo23.sub.obm.pl
      Setting scaling factor to 1 / 5420.455
  Calculating scaling for demo24
      Using object mask : demo24.sub.obm.pl
      Setting scaling factor to 1 / 5460.285
  Calculating scaling for demo25
      Using object mask : demo25.sub.obm.pl
      Setting scaling factor to 1 / 5498.279
  Creating sky subtracted image demo01.sub
      Frame  1  Sky frames:  start = 1   finish = 4   nreject = 1
      Using object mask : demo01.sub.obm.pl
  Creating sky subtracted image demo02.sub
      Frame  2  Sky frames:  start = 1   finish = 4   nreject = 1
      Using object mask : demo02.sub.obm.pl
  Creating sky subtracted image demo03.sub
      Frame  3  Sky frames:  start = 1   finish = 5   nreject = 1
      Using object mask : demo03.sub.obm.pl
  Creating sky subtracted image demo04.sub
      Frame  4  Sky frames:  start = 1   finish = 7   nreject = 1
      Using object mask : demo04.sub.obm.pl
  Creating sky subtracted image demo05.sub
      Frame  5  Sky frames:  start = 2   finish = 8   nreject = 1
      Using object mask : demo05.sub.obm.pl
  Creating sky subtracted image demo06.sub
      Frame  6  Sky frames:  start = 3   finish = 9   nreject = 1
      Using object mask : demo06.sub.obm.pl
  Creating sky subtracted image demo07.sub
      Frame  7  Sky frames:  start = 4   finish = 10   nreject = 1
      Using object mask : demo07.sub.obm.pl
  Creating sky subtracted image demo08.sub
      Frame  8  Sky frames:  start = 5   finish = 11   nreject = 1
      Using object mask : demo08.sub.obm.pl
  Creating sky subtracted image demo09.sub
      Frame  9  Sky frames:  start = 6   finish = 12   nreject = 1
      Using object mask : demo09.sub.obm.pl
  Creating sky subtracted image demo10.sub
      Frame  10  Sky frames:  start = 7   finish = 13   nreject = 1
      Using object mask : demo10.sub.obm.pl
  Creating sky subtracted image demo11.sub
      Frame  11  Sky frames:  start = 8   finish = 14   nreject = 1
      Using object mask : demo11.sub.obm.pl
  Creating sky subtracted image demo12.sub
      Frame  12  Sky frames:  start = 9   finish = 15   nreject = 1
      Using object mask : demo12.sub.obm.pl
  Creating sky subtracted image demo13.sub
      Frame  13  Sky frames:  start = 10   finish = 16   nreject = 1
      Using object mask : demo13.sub.obm.pl
  Creating sky subtracted image demo14.sub
      Frame  14  Sky frames:  start = 11   finish = 17   nreject = 1
      Using object mask : demo14.sub.obm.pl
  Creating sky subtracted image demo15.sub
      Frame  15  Sky frames:  start = 12   finish = 18   nreject = 1
      Using object mask : demo15.sub.obm.pl
  Creating sky subtracted image demo16.sub
      Frame  16  Sky frames:  start = 13   finish = 19   nreject = 1
      Using object mask : demo16.sub.obm.pl
  Creating sky subtracted image demo17.sub
      Frame  17  Sky frames:  start = 14   finish = 20   nreject = 1
      Using object mask : demo17.sub.obm.pl
  Creating sky subtracted image demo18.sub
      Frame  18  Sky frames:  start = 15   finish = 21   nreject = 1
      Using object mask : demo18.sub.obm.pl
  Creating sky subtracted image demo19.sub
      Frame  19  Sky frames:  start = 16   finish = 22   nreject = 1
      Using object mask : demo19.sub.obm.pl
  Creating sky subtracted image demo20.sub
      Frame  20  Sky frames:  start = 17   finish = 23   nreject = 1
      Using object mask : demo20.sub.obm.pl
  Creating sky subtracted image demo21.sub
      Frame  21  Sky frames:  start = 18   finish = 24   nreject = 1
      Using object mask : demo21.sub.obm.pl
  Creating sky subtracted image demo22.sub
      Frame  22  Sky frames:  start = 19   finish = 25   nreject = 1
      Using object mask : demo22.sub.obm.pl
  Creating sky subtracted image demo23.sub
      Frame  23  Sky frames:  start = 21   finish = 25   nreject = 1
      Using object mask : demo23.sub.obm.pl
  Creating sky subtracted image demo24.sub
      Frame  24  Sky frames:  start = 22   finish = 25   nreject = 1
      Using object mask : demo24.sub.obm.pl
  Creating sky subtracted image demo25.sub
      Frame  25  Sky frames:  start = 22   finish = 25   nreject = 1
      Using object mask : demo25.sub.obm.pl
      Creating holes mask: demo25.sub.hom.pl
  </pre></div>
  <p>
  The new sky subtracted images are stored in the files <span style="font-family: monospace;">"*.sub.imh"</span>. The
  holes masks are stored in the file <span style="font-family: monospace;">"*.sub.hom.pl"</span>.
  </p>
  <p>
  As before the bad pixels are interpolated away in the new sky subtracted
  images.  One possible difference is that the bad pixel mask may have
  additional bad pixels due to earlier detection as apparent cosmic
  ray events occurring repeatedly in the same pixel.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Begin mask pass bad pixel correction
  Wed 16:36:21 29-Nov-2000
  -------Correcting bad pixels with maskfix------------------
  Fixing bad pixels in file demo01.sub using mask demo.pl
  Fixing bad pixels in file demo02.sub using mask demo.pl
  Fixing bad pixels in file demo03.sub using mask demo.pl
  Fixing bad pixels in file demo04.sub using mask demo.pl
  Fixing bad pixels in file demo05.sub using mask demo.pl
  Fixing bad pixels in file demo06.sub using mask demo.pl
  Fixing bad pixels in file demo07.sub using mask demo.pl
  Fixing bad pixels in file demo08.sub using mask demo.pl
  Fixing bad pixels in file demo09.sub using mask demo.pl
  Fixing bad pixels in file demo10.sub using mask demo.pl
  Fixing bad pixels in file demo11.sub using mask demo.pl
  Fixing bad pixels in file demo12.sub using mask demo.pl
  Fixing bad pixels in file demo13.sub using mask demo.pl
  Fixing bad pixels in file demo14.sub using mask demo.pl
  Fixing bad pixels in file demo15.sub using mask demo.pl
  Fixing bad pixels in file demo16.sub using mask demo.pl
  Fixing bad pixels in file demo17.sub using mask demo.pl
  Fixing bad pixels in file demo18.sub using mask demo.pl
  Fixing bad pixels in file demo19.sub using mask demo.pl
  Fixing bad pixels in file demo20.sub using mask demo.pl
  Fixing bad pixels in file demo21.sub using mask demo.pl
  Fixing bad pixels in file demo22.sub using mask demo.pl
  Fixing bad pixels in file demo23.sub using mask demo.pl
  Fixing bad pixels in file demo24.sub using mask demo.pl
  Fixing bad pixels in file demo25.sub using mask demo.pl
  </pre></div>
  <p>
  Another round of cosmic ray detection is done using the more sensitive
  object masks based on the first pass mosaic rather than generating a
  mask for each individual observation.  As before any repeated cosmic
  ray detections are flagged as likely bad pixels in the bad pixel file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Begin mask pass cosmic ray correction
  Wed 16:36:39 29-Nov-2000
  -------Zapping cosmic rays using xzap --------------------
  Creating cosmic ray corrected image demo01.sub
      Using object mask : demo01.sub.ocm.pl
  Creating cosmic ray corrected image demo02.sub
      Using object mask : demo02.sub.ocm.pl
  Creating cosmic ray corrected image demo03.sub
      Using object mask : demo03.sub.ocm.pl
  Creating cosmic ray corrected image demo04.sub
      Using object mask : demo04.sub.ocm.pl
  Creating cosmic ray corrected image demo05.sub
      Using object mask : demo05.sub.ocm.pl
  Creating cosmic ray corrected image demo06.sub
      Using object mask : demo06.sub.ocm.pl
  Creating cosmic ray corrected image demo07.sub
      Using object mask : demo07.sub.ocm.pl
  Creating cosmic ray corrected image demo08.sub
      Using object mask : demo08.sub.ocm.pl
  Creating cosmic ray corrected image demo09.sub
      Using object mask : demo09.sub.ocm.pl
  Creating cosmic ray corrected image demo10.sub
      Using object mask : demo10.sub.ocm.pl
  Creating cosmic ray corrected image demo11.sub
      Using object mask : demo11.sub.ocm.pl
  Creating cosmic ray corrected image demo12.sub
      Using object mask : demo12.sub.ocm.pl
  Creating cosmic ray corrected image demo13.sub
      Using object mask : demo13.sub.ocm.pl
  Creating cosmic ray corrected image demo14.sub
      Using object mask : demo14.sub.ocm.pl
  Creating cosmic ray corrected image demo15.sub
      Using object mask : demo15.sub.ocm.pl
  Creating cosmic ray corrected image demo16.sub
      Using object mask : demo16.sub.ocm.pl
  Creating cosmic ray corrected image demo17.sub
      Using object mask : demo17.sub.ocm.pl
  Creating cosmic ray corrected image demo18.sub
      Using object mask : demo18.sub.ocm.pl
  Creating cosmic ray corrected image demo19.sub
      Using object mask : demo19.sub.ocm.pl
  Creating cosmic ray corrected image demo20.sub
      Using object mask : demo20.sub.ocm.pl
  Creating cosmic ray corrected image demo21.sub
      Using object mask : demo21.sub.ocm.pl
  Creating cosmic ray corrected image demo22.sub
      Using object mask : demo22.sub.ocm.pl
  Creating cosmic ray corrected image demo23.sub
      Using object mask : demo23.sub.ocm.pl
  Creating cosmic ray corrected image demo24.sub
      Using object mask : demo24.sub.ocm.pl
  Creating cosmic ray corrected image demo25.sub
      Using object mask : demo25.sub.ocm.pl
  
  begin badpixupdate
  Wed 16:37:34 29-Nov-2000
  -------Updating bad pixel file with badpixupdate ----------
  
  </pre></div>
  <p>
  The final step is to block replicate each image by the factor <i>mag</i> and
  shift and combine with quarter pixel accuracy.  This produces the final mosaic
  image with extension <span style="font-family: monospace;">"_mp"</span> and a final exposure map. The bad pixel mask,
  the final cosmic ray masks, and the holes masks are used to computed the
  final image and exposure map.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Begin mask pass image combining
  Wed 16:37:36 29-Nov-2000
  -------Magnifying and coadding images with xnregistar -----
  Creating individual composite masks ...
  Using bad pixel mask file: demo.pl
  Creating mask for image: demo01.sub
      Cannot find holes mask file: demo01.sub.hom.pl
      Using crmask file: demo01.sub.crm.pl
  Creating mask for image: demo02.sub
      Cannot find holes mask file: demo02.sub.hom.pl
      Using crmask file: demo02.sub.crm.pl
  Creating mask for image: demo03.sub
      Cannot find holes mask file: demo03.sub.hom.pl
      Using crmask file: demo03.sub.crm.pl
  Creating mask for image: demo04.sub
      Cannot find holes mask file: demo04.sub.hom.pl
      Using crmask file: demo04.sub.crm.pl
  Creating mask for image: demo05.sub
      Cannot find holes mask file: demo05.sub.hom.pl
      Using crmask file: demo05.sub.crm.pl
  Creating mask for image: demo06.sub
      Cannot find holes mask file: demo06.sub.hom.pl
      Using crmask file: demo06.sub.crm.pl
  Creating mask for image: demo07.sub
      Cannot find holes mask file: demo07.sub.hom.pl
      Using crmask file: demo07.sub.crm.pl
  Creating mask for image: demo08.sub
      Cannot find holes mask file: demo08.sub.hom.pl
      Using crmask file: demo08.sub.crm.pl
  Creating mask for image: demo09.sub
      Cannot find holes mask file: demo09.sub.hom.pl
      Using crmask file: demo09.sub.crm.pl
  Creating mask for image: demo10.sub
      Cannot find holes mask file: demo10.sub.hom.pl
      Using crmask file: demo10.sub.crm.pl
  Creating mask for image: demo11.sub
      Cannot find holes mask file: demo11.sub.hom.pl
      Using crmask file: demo11.sub.crm.pl
  Creating mask for image: demo12.sub
      Cannot find holes mask file: demo12.sub.hom.pl
      Using crmask file: demo12.sub.crm.pl
  Creating mask for image: demo13.sub
      Cannot find holes mask file: demo13.sub.hom.pl
      Using crmask file: demo13.sub.crm.pl
  Creating mask for image: demo14.sub
      Cannot find holes mask file: demo14.sub.hom.pl
      Using crmask file: demo14.sub.crm.pl
  Creating mask for image: demo15.sub
      Cannot find holes mask file: demo15.sub.hom.pl
      Using crmask file: demo15.sub.crm.pl
  Creating mask for image: demo16.sub
      Cannot find holes mask file: demo16.sub.hom.pl
      Using crmask file: demo16.sub.crm.pl
  Creating mask for image: demo17.sub
      Cannot find holes mask file: demo17.sub.hom.pl
      Using crmask file: demo17.sub.crm.pl
  Creating mask for image: demo18.sub
      Cannot find holes mask file: demo18.sub.hom.pl
      Using crmask file: demo18.sub.crm.pl
  Creating mask for image: demo19.sub
      Cannot find holes mask file: demo19.sub.hom.pl
      Using crmask file: demo19.sub.crm.pl
  Creating mask for image: demo20.sub
      Cannot find holes mask file: demo20.sub.hom.pl
      Using crmask file: demo20.sub.crm.pl
  Creating mask for image: demo21.sub
      Cannot find holes mask file: demo21.sub.hom.pl
      Using crmask file: demo21.sub.crm.pl
  Creating mask for image: demo22.sub
      Cannot find holes mask file: demo22.sub.hom.pl
      Using crmask file: demo22.sub.crm.pl
  Creating mask for image: demo23.sub
      Cannot find holes mask file: demo23.sub.hom.pl
      Using crmask file: demo23.sub.crm.pl
  Creating mask for image: demo24.sub
      Cannot find holes mask file: demo24.sub.hom.pl
      Using crmask file: demo24.sub.crm.pl
  Creating mask for image: demo25.sub
      Using holes mask file: demo25.sub.hom.pl
      Using crmask file: demo25.sub.crm.pl
  Block replicating the input images ...
  Block replicating the exposure time images ...
  Combining the input images ...
  Combining the exposure time images ...
  finish xmaskpass
  Wed 16:40:47 29-Nov-2000
  
  finish xmosaic
  Wed 16:40:47 29-Nov-2000
  </pre></div>
  <p>
  Now examine the results.  Load the truth image, the first pass mosaic, and the
  mask pass mosaic into the image display. Note that the final sizes are
  different so things will not appear exactly registered.
  </p>
  <div class="highlight-default-notranslate"><pre>
  di&gt; <b>display demo_truth 1 fill+</b>
  di&gt; <b>display mosaic_fp 2 fill+</b>
  di&gt; <b>display mosaic_mp 3 fill+</b>
  </pre></div>
  </section>
  <section id="s_appendix_1__summary_of_major_differences_between_xdimsum_and_dimsum">
  <span>5. Appendix 1: Summary of Major Differences between XDIMSUM and DIMSUM</span>
  </section>
  <section id="s_input_and_output_image_and_mask_lists">
  <span>5.1 Input and Output Image and Mask Lists</span>
  <p>
  All input and output image and file names and input and output image and file
  lists are now task parameters rather than being silently passed as keyword
  names, silently assumed to have already been created by a previous step, or
  silently created by the current step. For example the input object mask list
  required by the xslm task is now a parameter. Similarly the output sky
  subtraction and holes mask lists produced the the xslm task are now parameters.
  These changes make tracing the data flow from one processing step to another
  simpler.
  </p>
  </section>
  <section id="s_default_image_and_mask_names">
  <span>5.2 Default Image and Mask Names</span>
  <p>
  In most cases the output images and masks are assigned sensible default names
  if explicit output image and mask lists are not provided. For example in the
  case of the sky subtraction task xslm the suffix <span style="font-family: monospace;">".sub"</span> is appended to the
  input images names  to produce the output sky subtracted image names, and the
  suffixes <span style="font-family: monospace;">".ssm"</span> and <span style="font-family: monospace;">".hom"</span> are appended to sky subtracted image names
  to create the sky subtraction and holes mask names.  In general if an output
  image or mask list parameter value begins with a <span style="font-family: monospace;">'.'</span> it is assumed
  to be a suffix rather than a complete name.  The default image and mask
  name scheme means that users need not concern themselves with the names
  of the intermediate data products.
  </p>
  </section>
  <section id="s_use_of_suffixes_instead_of_prefixes_to_define_default_names">
  <span>5.3 Use of Suffixes instead of Prefixes to Define Default Names</span>
  <p>
  Suffixes instead of prefixes are used to create default names. Using suffixes
  means that the input and output image lists no longer need to be in the same
  directory.
  </p>
  </section>
  <section id="s_new_tasks">
  <span>5.4 New Tasks</span>
  <p>
  A new cosmic ray removal task <i>xnzap</i> has been added to the XDIMSUM
  package.  Xnzap is a script wrapper for the <i>xcraverage</i> task.  Xnzap is an
  alternative to the default xzap task. It is significantly faster than xzap but
  not yet as well tested.  Users are encouraged to experiment with xnzap and / or
  xcraverage on their own. User feedback on their effectiveness is welcome.
  </p>
  <p>
  The code for interactively computing the relative shifts in a set of
  dithered images has been rewritten and moved into a separate task called
  <i>xdshifts</i>.
  </p>
  <p>
  Three new script tasks for computing shifts for images taken in series with
  approximately constant shifts between adjacent images: <i>xmshifts</i>,
  <i>xfshifts</i>, and <i>xrshifts</i>, have been added to XDIMSUM. These scripts
  use modified versions of the existing starfind and imcentroid tasks called
  <i>xstarfind</i> and <i>ximcentroid</i>.
  </p>
  </section>
  <section id="s_new_algorithms">
  <span>5.5 New Algorithms</span>
  <p>
  The main processing scripts <i>xmosaic</i>, <i>xfirstpass</i>, and <i>xmaskpass</i>
  can now be run repeatedly from scratch  without requiring the user to delete
  any intermediate files. It has also been made simpler to restart these scripts
  at an intermediate point in the processing.
  </p>
  <p>
  The mask deregistration task <i>maskdereg</i> now permits the user to create
  individual object masks which are a combination of the current mask and the
  N previous ones. This feature is useful in cases where the detector retains
  significant memory of previous exposures.
  </p>
  <p>
  The image and mask statistics computation parameters used by the sky
  subtraction and cosmic ray removal tasks <i>xslm</i> and <i>xzap</i>,
  <i>statsec</i>, <i>mstatsec</i>, <i>maxiter</i>, and <i>nreject</i> can now be
  set by the user.  Their default values are now <span style="font-family: monospace;">""</span>, <span style="font-family: monospace;">""</span>, 20, and 3.0 respectively,
  instead of being fixed at the values <span style="font-family: monospace;">""</span>, <span style="font-family: monospace;">""</span>, 10, and 5.0. 
  </p>
  <p>
  The <i>maskstat</i> task now outputs the computed mask statistics to the output
  parameters mean, msigma, median, and mmode in the same manner as the
  <i>iterstat</i> itask does.
  </p>
  <p>
  The first pass image combining step performed by the <i>xmosaic</i> or
  <i>xfirstpass</i> tasks now includes an option for doing fractional pixel
  shifts.
  </p>
  <p>
  The mask pass image combining step performed by the <i>xmosaic</i> or
  <i>xmask pass</i> tasks now includes an option for doing image magnification
  using bilinear interpolation rather than block replication. This means
  that non-integer magnification factors are supported. 
  </p>
  </section>
  <section id="s_internal_changes">
  <span>5.6 Internal Changes</span>
  <p>
  Calls to existing IRAF tasks have been reviewed to make sure that all
  the task parameters are set in order to avoid unpleasant surprises
  if these parameters are not set at the expected defaults.
  </p>
  <p>
  Complicated image operations requiring several steps have been replaced
  by a single call to the <i>imexpr</i> task where appropriate.
  </p>
  <p>
  The image registration and combining step has been rewritten to use a
  new version of the imcombine task called <i>xcombine</i> which does not
  suffer from the number of open file limit and has better support for
  pixel masks. The registration should be much faster in most cases.
  </p>
  <p>
  The <i>sections</i>, <i>fileroot</i>, <i>imgets</i>, <i>minmax</i>, <i>iterstat</i>,
  and <i>maskstat</i> tasks which return values to their parameters have been
  cached so that XDIMSUM tasks will work correctly in the background.
  </p>
  <p>
  On normal task termination there are now no temporary files or images left
  either in the tmp$ directory  or in the current working directory.
  </p>
  
  </section>
  
  <!-- Contents: 'Introduction' 'Outline Of the Major XDIMSUM Processing Steps' 'First Pass' 'Sky Subtraction with the Xslm Task' 'Fixing Bad Pixels with the Maskfix Task' 'Removing Cosmic Rays with the Xzap or Znap Tasks' 'Making the Shift List with the Xdshifts Task' 'Combining Images with the Xnregistar Task' 'Mask Pass' 'Making Masks with the Mkmask and Maskdereg Tasks' 'Sky Subtraction with the Xslm Task and Object Masks' 'Fixing Bad Pixels with the Maskfix Task' 'Correcting Cosmic Rays with the Xzap or Xznap Tasks' 'Combining Images with the Xnregistar Task' 'Data Input and Data Products' 'Individual Input Images' 'The Input Bad Pixel Mask' 'The Individual Output Corrected Images' 'The Output Cosmic Ray Masks' 'The Output Shifts File' 'The Output Objects Masks' 'The Output Holes Masks' 'The Output Combined Image and Exposure Map' 'Example' 'Appendix 1: Summary of Major Differences between XDIMSUM and DIMSUM' 'Input and Output Image and Mask Lists' 'Default Image and Mask Names' 'Use of Suffixes instead of Prefixes to Define Default Names' 'New Tasks' 'New Algorithms' 'Internal Changes'  -->
  

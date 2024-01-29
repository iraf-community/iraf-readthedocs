.. _xmaskpass:

xmaskpass: Driver script for mask pass processing steps
=======================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xmaskpass input expinput sections output outexpmap
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The first pass combined image.
  </dd>
  </dl>
  <dl id="l_inexpmap">
  <dt><b>inexpmap</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inexpmap' Line='inexpmap' -->
  <dd>The  first pass exposure map image associated with the input combined image
  <i>input</i>.
  </dd>
  </dl>
  <dl id="l_sections">
  <dt><b>sections</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sections' Line='sections' -->
  <dd>The first pass sections file the location of the individual input images in the
  combined image <i>input</i>.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The name of the final output combined image.
  </dd>
  </dl>
  <dl id="l_outexpmap">
  <dt><b>outexpmap = <span style="font-family: monospace;">".exp"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outexpmap' Line='outexpmap = ".exp"' -->
  <dd>The name of the output exposure map image or the string appended to the output
  image name <i>output</i> to create the output exposure map image name. The
  exposure map contains the total exposure time for each output image pixel after
  rejecting bad pixels, cosmic rays, and undefined pixels.
  </dd>
  </dl>
  <dl id="l_statsec">
  <dt><b>statsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='statsec' Line='statsec = ""' -->
  <dd>The image section used to compute the sky statistics for the individual
  input image in the sky subtraction and cosmic ray removal steps. By default
  the entire input image is used.
  </dd>
  </dl>
  <dl id="l_nsigrej">
  <dt><b>nsigrej = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigrej' Line='nsigrej = 3.0' -->
  <dd>The nsigma rejection limits used to compute the sky statistics in the sky
  subtraction and cosmic ray removal tasks.
  </dd>
  </dl>
  <dl id="l_maxiter">
  <dt><b>maxiter = 20</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxiter' Line='maxiter = 20' -->
  <dd>The maximum number of rejection cycles used to compute the sky statistics
  by the sky subtraction and cosmic ray removal tasks.
  </dd>
  </dl>
  <dl id="l_mkmask">
  <dt><b>mkmask = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mkmask' Line='mkmask = yes' -->
  <dd>Create the combined image object mask and inverse object core mask ? If mkmask
  is no and the object mask or inverse object core mask do not exist the task
  will terminate.
  </dd>
  </dl>
  <dl id="l_omask">
  <dt><b>omask = <span style="font-family: monospace;">".msk"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='omask' Line='omask = ".msk"' -->
  <dd>The output combined image object mask name or the string appended to the input
  image name <i>input</i> to create the output combined object mask name. An
  additional <span style="font-family: monospace;">"i"</span> is added to the combined object mask name to create the inverse
  object core mask name. Object masks consist of 1's in object regions and 0's
  elsewhere. Inverse object masks are the reverse.
  </dd>
  </dl>
  <dl id="l_chkmasks">
  <dt><b>chkmasks = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='chkmasks' Line='chkmasks = no' -->
  <dd>Check the displayed mask and optionally enter a new threshold value ?
  </dd>
  </dl>
  <dl id="l_kpchking">
  <dt><b>kpchking = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='kpchking' Line='kpchking = yes' -->
  <dd>Repeatedly check the mask until satisfied ?
  </dd>
  </dl>
  <dl id="l_mstatsec">
  <dt><b>mstatsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mstatsec' Line='mstatsec = ""' -->
  <dd>The combined image section used to compute the sky statistics in the mask
  creation step. By default the entire input image is used.
  </dd>
  </dl>
  <dl id="l_nsigcrmsk">
  <dt><b>nsigcrmsk = 1.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigcrmsk' Line='nsigcrmsk = 1.5' -->
  <dd>The factor times the recommended threshold used by the mask creation task to
  compute the combined image inverse object core mask for cosmic ray unzapping.
  </dd>
  </dl>
  <dl id="l_nsigobjmsk">
  <dt><b>nsigobjmsk = 1.1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigobjmsk' Line='nsigobjmsk = 1.1' -->
  <dd>The factor times the recommended threshold used by the mask creation task to
  compute the combined input image object mask.
  </dd>
  </dl>
  <dl id="l_negthresh">
  <dt><b>negthresh = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='negthresh' Line='negthresh = no' -->
  <dd>Use negative as well as positive threshold when creating the input image
  object mask ?
  </dd>
  </dl>
  <dl id="l_ngrow">
  <dt><b>ngrow = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ngrow' Line='ngrow = 0' -->
  <dd>The object growing box half-width in pixels.
  </dd>
  </dl>
  <dl id="l_maskdereg">
  <dt><b>maskdereg = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maskdereg' Line='maskdereg = yes' -->
  <dd>Create object masks and inverse object core masks for the individual input
  images by extracting the appropriate sections from the parent combined
  image masks ?
  </dd>
  </dl>
  <dl id="l_ocrmasks">
  <dt><b>ocrmasks = <span style="font-family: monospace;">".ocm"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ocrmasks' Line='ocrmasks = ".ocm"' -->
  <dd>The list of output individual inverse core object masks or the string appended
  to the individual sky subtracted image names to create the individual output
  inverse core object mask names. The inverse object masks consist of 0's in the
  object regions and 1's elsewhere and are used for unzapping cosmic rays detected
  in object regions.
  </dd>
  </dl>
  <dl id="l_objmasks">
  <dt><b>objmasks = <span style="font-family: monospace;">".objm"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='objmasks' Line='objmasks = ".objm"' -->
  <dd>The list of output individual image object masks or the string appended to the
  individual sky subtracted image names to create the individual output object
  mask names. The object masks consist of 1's in the object regions and 0's
  elsewhere and are used for improving the sky subtraction.
  </dd>
  </dl>
  <dl id="l_xslm">
  <dt><b>xslm = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xslm' Line='xslm = yes' -->
  <dd>Do the sky subtraction step using object masking with the xnslm task if
  <i>newslm</i> is yes or <i>xslm</i> is no ? The input images must be sky
  subtracted before the bad pixel correction, cosmic ray correction, and image
  combining steps can be performed.
  </dd>
  </dl>
  <dl id="l_sslist">
  <dt><b>sslist = <span style="font-family: monospace;">".sub"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sslist' Line='sslist = ".sub"' -->
  <dd>The output sky subtracted image list or the string appended to the input image
  names in <i>sections</i> to create the names of the output sky subtracted
  images.
  </dd>
  </dl>
  <dl id="l_hmasks">
  <dt><b>hmasks = <span style="font-family: monospace;">".hom"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hmasks' Line='hmasks = ".hom"' -->
  <dd>The output holes mask list or the string appended to the sky subtracted image
  names to create the names of the output holes masks. Holes mask consist of 
  0's in undefined regions and 1<span style="font-family: monospace;">'s'</span> elsewhere and are only created if object
  masking is enabled.
  </dd>
  </dl>
  <dl id="l_newxslm">
  <dt><b>newxslm = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newxslm' Line='newxslm = no' -->
  <dd>Use the new xnslm task rather than the original xslm task ?
  </dd>
  </dl>
  <dl id="l_forcescale">
  <dt><b>forcescale = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='forcescale' Line='forcescale = yes' -->
  <dd>Force recomputation of the input image statistics regardless of whether or
  not they have been previously computed and stored in the keyword <span style="font-family: monospace;">"SKYMED"</span>.
  </dd>
  </dl>
  <dl id="l_useomask">
  <dt><b>useomask = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='useomask' Line='useomask = yes' -->
  <dd>Use the individual object masks <i>objmasks</i> tocomputw the individual
  image sky statistics ? The object masks are used to create the sky images
  regardless of the value of useomask.
  </dd>
  </dl>
  <dl id="l_nmean">
  <dt><b>nmean = 6</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nmean' Line='nmean = 6' -->
  <dd>The number of neighboring images used by the sky subtraction task to compute
  the sky image for each input image.
  </dd>
  </dl>
  <dl id="l_nskymin">
  <dt><b>nskymin = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nskymin' Line='nskymin = 3' -->
  <dd>The minimum number of input images used by the sky subtraction task to
  compute the sky image.
  </dd>
  </dl>
  <dl id="l_nreject">
  <dt><b>nreject = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nreject' Line='nreject = 1' -->
  <dd>The number of high and low side pixels to reject when the sky image is 
  computed by the sky subtraction task.
  </dd>
  </dl>
  <dl id="l_cache">
  <dt><b>cache = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cache' Line='cache = yes' -->
  <dd>Enable image cacheing for improved efficiency in the new xnslm task ?
  </dd>
  </dl>
  <dl id="l_maskfix">
  <dt><b>maskfix = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maskfix' Line='maskfix = yes' -->
  <dd>Use the bad pixel mask <i>bpmask</i> to fix bad pixels in the sky subtracted
  images ?
  </dd>
  </dl>
  <dl id="l_bpmask">
  <dt><b>bpmask</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bpmask' Line='bpmask' -->
  <dd>The name of the input bad pixel mask used to fix bad pixels in the sky
  subtracted images. Bpmask is assumed to be the same for all the input images
  and to consist of 0's in the bad pixel regions and 1's elsewhere. If bpmask is
  undefined the bad pixel fixing step is skipped.
  </dd>
  </dl>
  <dl id="l_forcefix">
  <dt><b>forcefix = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='forcefix' Line='forcefix = yes' -->
  <dd>Force bad pixel fixing by the even though the image haves been previously
  fixed as indicated by the presense of the keyword <span style="font-family: monospace;">"MASKFIX"</span>.
  </dd>
  </dl>
  <dl id="l_xzap">
  <dt><b>xzap = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xzap' Line='xzap = yes' -->
  <dd>Remove cosmic rays from the sky subtracted images using the xnzap task
  if <i>newxzap</i> = yes or xzap if <i>newxzap</i> is no ? If xzap is no the
  existing cosmic ray masks after unzapping with the individual inverse
  object masks <i>ocrmasks</i> are used in later processing steps.
  </dd>
  </dl>
  <dl id="l_crmasks">
  <dt><b>crmasks = <span style="font-family: monospace;">".crm"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crmasks' Line='crmasks = ".crm"' -->
  <dd>The list of input first pass cosmic ray masks if <i>xzap</i> = no, or the list
  of output cosmic ray masks if <i>xzap</i> = yes. Crmasks may also be
  a string appended to the sky subtracted image names to create the names of
  the input / output cosmic ray masks. Cosmic ray masks consist of 1's in the
  cosmic ray regions and 0's elsewhere. 
  </dd>
  </dl>
  <dl id="l_newxzap">
  <dt><b>newxzap = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newxzap' Line='newxzap = no' -->
  <dd>Use the new xnzap task rather than the original xzap task ?
  </dd>
  </dl>
  <dl id="l_badpixupdate">
  <dt><b>badpixupdate = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='badpixupdate' Line='badpixupdate = yes' -->
  <dd>Update the bad pixel mask <i>bpmask</i>. The bad pixel mask updating task
  adds those bad pixels detected in 3 or more sky subtracted images to the bad
  pixel mask using the current cosmic ray mask list. Bad pixel mask updating
  is only done if <i>xzap</i> is yes.
  </dd>
  </dl>
  <dl id="l_nrepeats">
  <dt><b>nrepeats = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nrepeats' Line='nrepeats = 3' -->
  <dd>If a pixel is detected as a cosmic ray in <i>nrepeats</i> or more images and
  <i>badpixupdate</i> is yes then the pixel is set to bad in the bad pixel
  mask <i>bpmask</i>.
  </dd>
  </dl>
  <dl id="l_xnregistar">
  <dt><b>xnregistar = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xnregistar' Line='xnregistar = yes' -->
  <dd>Compute the final combined output image and exposure map image using offsets and
  exposure time scaling ?
  </dd>
  </dl>
  <dl id="l_shiftlist">
  <dt><b>shiftlist = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shiftlist' Line='shiftlist = ""' -->
  <dd>The input shifts file used to combine the corrected images. Shiftlist
  consists of the corrected image name, the x and y offsets in user units
  (usually pixels), and the exposure time used to scale the image. If shiftlist
  is undefined xmaskpass terminates with a warning message.
  </dd>
  </dl>
  <dl id="l_rmasks">
  <dt><b>rmasks = <span style="font-family: monospace;">".rjm"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rmasks' Line='rmasks = ".rjm"' -->
  <dd>The list of output mask pass rejection masks. Rmasks may also be a string
  appended to the sky subtracted image names to create the names of the output
  rejection masks. Rejection masks consist of 1's in the good data regions and
  0's elsewhere. 
  </dd>
  </dl>
  <dl id="l_nprev_omask">
  <dt><b>nprev_omask = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nprev_omask' Line='nprev_omask = 0' -->
  <dd>The number of previous individual object masks that are combined to create the
  object mask used in the image combine step.
  </dd>
  </dl>
  <dl id="l_fractional">
  <dt><b>fractional = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fractional' Line='fractional = no' -->
  <dd>Use the fractional as well as integer part of the corrected image offsets if
  <i>mag</i> = 1. The imshift task and bilinear interpolation are used to do the
  fractional part of the shift.
  </dd>
  </dl>
  <dl id="l_pixin">
  <dt><b>pixin = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixin' Line='pixin = yes' -->
  <dd>If pixin is yes the input offsets called a and b are assumed to be defined in
  the reference image pixel coordinate system x and y, and ab_sense, xscale,
  yscale, and a2x_angle default to yes, -1.0, -1.0, and 0.0 respectively.
  </dd>
  </dl>
  <dl id="l_ab_sense">
  <dt><b>ab_sense = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ab_sense' Line='ab_sense = yes' -->
  <dd>Is the rotation of the a to b axis counter-clockwise ? The x and b
  axes are the axes along which the input offsets are measured. Ab_sense
  defaults to yes if pixin is yes. 
  </dd>
  </dl>
  <dl id="l_xscale">
  <dt><b>xscale = 1.0, yscale = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xscale' Line='xscale = 1.0, yscale = 1.0' -->
  <dd>The number of pixel coordinates x and y per input coordinates a and b.
  For example if the input offsets are measured in arcseconds and the pixel
  scale is 0.25 arcseconds per pixel then xscale and yscale should be set to 4.0.
  Xscale and yscale default to -1.0 and -1.0 if pixin is yes. 
  </dd>
  </dl>
  <dl id="l_a2x_angle">
  <dt><b>a2x_angle = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='a2x_angle' Line='a2x_angle = 0' -->
  <dd>The angle in degrees of the a offset axis measured counter-clockwise to the
  image x axis. A2x_angle defaults to 0.0 if pixin is yes. 
  </dd>
  </dl>
  <dl id="l_mag">
  <dt><b>mag = 4.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mag' Line='mag = 4.0' -->
  <dd>The factor by which the output image and output exposure map image are block
  replicated with respect to the input image and input exposure map.
  </dd>
  </dl>
  <dl id="l_blkrep">
  <dt><b>blkrep = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blkrep' Line='blkrep = yes' -->
  <dd>Use block replication rather than bilinear interpolation to magnify the
  images if <i>mag</i> &gt; 1.
  </dd>
  </dl>
  <dl id="l_ncoavg">
  <dt><b>ncoavg = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncoavg' Line='ncoavg = 1' -->
  <dd>The number of co-averages per input image. The total exposure time for
  an image is ncoavg * exptime * secpexp where exptime is read from shiftlist.
  </dd>
  </dl>
  <dl id="l_secpexp">
  <dt><b>secpexp = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='secpexp' Line='secpexp = 1.0' -->
  <dd>The number of seconds per unit exposure time. 
  </dd>
  </dl>
  <dl id="l_y2n_angle">
  <dt><b>y2n_angle = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='y2n_angle' Line='y2n_angle = 0.0' -->
  <dd>The angle in degrees from the image y axis to the north axis measured from north
  through east. Y2n_angle can be used to orient the output image to within 45
  degrees of N up and E left if set correctly.
  </dd>
  </dl>
  <dl id="l_rotation">
  <dt><b>rotation = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rotation' Line='rotation = yes' -->
  <dd>Is the rotation of the input image north axis to the east axis
  counter-clockwise ? 
  </dd>
  </dl>
  <dl id="l_del_bigmasks">
  <dt><b>del_bigmasks = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='del_bigmasks' Line='del_bigmasks = no' -->
  <dd>Delete <i>omask</i> and its related inverse mask on task termination ?
  </dd>
  </dl>
  <dl id="l_del_smallmasks">
  <dt><b>del_smallmasks = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='del_smallmasks' Line='del_smallmasks = no' -->
  <dd>Delete <i>ocrmasks</i> and <i>objmasks</i> and their related inverse on task
  termination ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XMASKPASS sky subtracts, bad pixel corrects, and cosmic ray corrects the input
  images in <i>sections</i>, and combines the corrected images into a single
  output image <i>output</i> and accompanying exposure map image <i>outexpmap</i>,
  using the input combined image <i>input</i> and associated exposure map
  <i>inexpmap</i> produced by XFIRSTPASS to derive object masks for the
  combined and individual images. The object mask and inverse object core mask
  for the input combined image are stored in the mask  <i>omask</i>. The
  individual image object masks and inverse object core masks are stored in
  <i>objmasks</i> and <i>ocrmasks</i> respectively. Object masks consist of
  1's in the object regions and 0's elsewhere. Inverse object masks consist of
  0's in the object regions and 1's elsewhere. The final output sky subtracted,
  bad pixel corrected, and cosmic ray corrected images are stored in
  <i>sslist</i>. The output holes masks and cosmic ray masks are stored in
  <i>hmasks</i> and <i>crmasks</i> respectively.
  </p>
  <p>
  If <i>mkmask</i> is yes the combined image object mask <i>omask</i> and
  inverse object core mask <i>omask</i> are created with the MKMASK task
  using thresholding factors <i>nsigobjmask</i> and <i>nsigcrmask</i> times
  the recommand thresholding factor respectively. If <i>negthresh</i> is
  <span style="font-family: monospace;">"yes"</span> both negative and positive thresholds are used to created the combined
  image object mask. The standard deviation of the background is computed using
  pixels in the section specified by <i>mstatsec</i> and iterative rejection with
  parameters <i>nsigrej</i> and <i>maxiter</i>. MKMASK
  uses default values of 2, 15, and 3 for the MKMASK subsampling factor, median
  filter size, and smoothing size respectively. More about the MKMASK task can be
  found in the MKMASK help page. If <i>chkmasks</i> is yes, the recommended
  threshold is printed, the input combined image normalized by the exposure
  time is displayed in the image display, the imexamine task is invloked,
  the user is prompted for a new thresholding value, and the input image
  and new mask are displayed. If <i>kpchking</i> is set to yes the whole
  process is repeated until the user is satisfied and sets it to no.
  If <i>mkmask</i> is no and the combined object mask and inverse object core
  mask do not already exist XMASKPASS terminates.
  </p>
  <p>
  If <i>maskdereg</i> is yes then the individual object masks and inverse object
  core masks <i>objmasks</i> and <i>ocrmasks</i> are created from the combined
  image object masks <i>omask</i> using positional information in the
  <i>sections</i> file. The object masks are used to improve the sky subtraction.
  The inverse object core masks are used to unzap the cosmic rays in object
  regions where the cosmic rays are defined by the cosmic ray masks
  <i>crmasks</i>. The object mask and inverse object core mask names are stored in
  the image header keywords <span style="font-family: monospace;">"OBJMASK"</span> and <span style="font-family: monospace;">"CROBJMAS"</span> respectively.
  If <i>maskdereg</i> is no then the object masks and inverse object core masks
  are assumed to already exist.
  </p>
  <p>
  If <i>xslm</i> is yes XMASKPASS sky substracts the input images using the
  XNSLM task if <i>newxslm</i> is yes and  XSLM task if it is no with object
  masking enabled, and writes the results to the output
  images <i>sslist</i>. Existing sky subtracted images are overwritten.
  The indivdual object masks are assumed to have been created
  by the MASKDEREG task.  XSLM/XNSLM computes the running mean of the <i>nmean</i>
  neighboring images, after scaling them by their median pixel values, and
  rejecting the <i>nreject</i> highest scaled pixels. There must be at least
  <i>nskymin</i> neighboring images for a sky image to be computed and
  subtracted from the input image. The input image medians are computed
  using pixels in the region defined by <i>statsec</i>, the object mask defined
  in <i>objmasks</i> if <i>useomask</i> is yes, and iterative rejection using
  rejection parameters <i>nsigrej</i> and <i>maxiter</i>. The reciprocal of the
  computed median is stored in the image header keyword <span style="font-family: monospace;">"SKYMED"</span>. If
  <i>forcescale</i> is no and the <span style="font-family: monospace;">"SKYMED"</span> keyword already exists in the image
  header then the image medians are not recomputed and the value of SKYMED
  is used as the scaling factor. If use of the object masks results in
  sky background pixels which are undefined then a holes mask <i>hmasks</i>
  is written.  Holes masks consist of 0's in undefined regions and 1's elsewhere.
  If a holes mask was created then the keyword <span style="font-family: monospace;">"HOLES"</span> containing the name of the
  holes mask is written to the sky subtracted image. When sky subtraction
  is complete the keyword SKYSUB is written to the output image headers.  More
  information about the XSLM/XNSLM task can be found in the XSLM/XNSLM help
  pages.
  </p>
  <p>
  If <i>maskfix</i> is yes XMASKPASS removes bad pixels from sky subtracted
  images <i>sslist</i> using the MASKFIX task and the bad pixel mask
  <i>bpmask</i>. The bad pixel mask consists of 0's in bad pixel regions and 1's
  elsewhere and must be the same size as the input sky subtracted image. The bad
  pixels are removed by linearly interpolating across bad columns in each image
  line. When bad pixel removal is complete the keyword <span style="font-family: monospace;">"MASKFIX"</span> is written to
  the header of the sky subtracted image. If <i>forcefix</i> is no and <span style="font-family: monospace;">"MASKFIX"</span>
  exists in the image header then the bad pixel removal step is skipped. More
  information on the MASKFIX task can be found in the MASKFIX help page.
  </p>
  <p>
  If <i>xzap</i> is yes XMASKPASS removes cosmic rays from the sky subtracted
  images <i>sslist</i>  using the XNZAP task if <i>newxzap</i> is yes or the
  XZAP task if it is no, and writes the cosmic ray masks to <i>crmasks</i>.
  Existing cosmic ray masks are overwritten.  The output cosmic ray masks
  contain 1's in the cosmic ray regions and 0's elsewhere. Both XZAP and XNZAP
  write the keyword CRMASK which contains the name of the output cosmic ray MASK
  to the cosmic ray corrected image. If the CRMASK keyword is present in the sky
  subtracted image headers cosmic ray cleaning is skipped. XZAP is the tried and
  true XDIMSUM cosmic ray removal task. XNZAP is experimental but promises to be
  a faster technique. If <i>xzap</i> is no then the cosmic rays masks created
  by XFIRSTPASS are used. Cosmic rays in the cores of objects are unzapped
  using the inverse object core masks <i>ocrlist</i>.
  </p>
  <p>
  XZAP detects and removes cosmic rays by finding pixels which are more than
  5.0 sky sigma above the median of the surrounding box of 5 by 5 pixels
  and are not part of an object, where an object is any pixel located in
  an object region defined by the inverse object masks <i>ocrmasks</i>
  stored in the header keyword <span style="font-family: monospace;">"CROBJMAS"</span>. The cosmic rays in the input sky
  subtracted images are replaced with the local median value.  More information
  on the XZAP task can be found in the XZAP help page.
  </p>
  <p>
  XNZAP detects and removes cosmic rays by finding pixels which are
  more than 5.0 sky sigma above the mean of the surrounding box of 5 by 5
  pixels with the central pixel and the highest pixel removed, and which are
  not part of an object where an object is defined by the inverse object
  mask <i>ocrmasks</i> stored in the image header keyword <span style="font-family: monospace;">"CROBJMAS"</span>.
  The local background is defined as the median of
  the pixels in an annulus 5.0 pixels wide around the averaging box. The
  local sky sigma is estimated by computing the percentile points of pixels
  in 25 by 25 pixel subsections evenly distributed over the image. The cosmic
  ray and object growing radii are set to 0.0 and 0.0 respectively.
  The cosmic rays in the input sky subtracted images are replaced with the
  local average value. More information on the XNZAP task can be found in the
  XNZAP help page.
  </p>
  <p>
  If <i>xzap</i> is yes and <i>badpixupdate</i> is yes then XMASKPASS updates
  the bad pixel mask <i>bpmask</i> using the BADPIXUPDATE task. BADPIXUPDATE
  examines the list of cosmic ray masks produced by XZAP or XNZAP, searches
  for pixels that are bad in 3 or more masks, and sets those pixels in
  <i>bpmask</i> to 0.
  </p>
  <p>
  In preparation for image combining the name of the corrected image, its
  x and y shifts relative to the reference image, and its exposure time are
  read from the file <i>shiftlist</i>. Shiftlist may have been written by the
  XDSHIFTS, XMSHIFTS, XFSHIFTS, or XRSHIFTS tasks.
  </p>
  <p>
  If <i>xnregistar</i> is yes then XMASKPASS combines the corrected images
  into the output combined image <i>output</i> and output exposure map image
  <i>outexpmap</i> using the badpixel mask <i>bpmask</i>, the cosmic ray
  masks <i>crmasks</i>, the holes masks <i>hmasks</i>, the <i>nprev_omask</i>
  objects masks, and  offsets and scaling factors read from <i>shiftlist</i>.
  The combined rejection masks are written to <i>rmasks</i>.
  If <i>fractional</i> is no only the integer parts of the shifts are used.
  XMASKPASS calls the XNREGISTAR task to do the actual image combining. The
  parameters <i>pixin</i>, <i>ab_sense</i>, <i>xscale</i>, <i>yscale</i>, and
  <i>a2x_angle</i> are used to convert shifts from user units, e.g. arseconds
  to units of pixels in the reference image. The magnification factor <i>mag</i> 
  determines the magnification of the final combined image with respect the
  the initial combined image. if <i>blkrep</i> the magnification is done
  via block replication, otherwise it is done using bilinear interpolation.
  The parameters <i>ncoavg</i> and <i>secpexp</i> are used to normalize the
  input exposure times. The parameters <i>y2n_angle</i> and <i>rotation</i> are
  used to orient the final combined image and eposure map to within 45 degrees
  of north up and east to the left.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Perform a first pass image combining operation on the demo images using
  the default shiftlist demo.slist and follow it with a mask pass.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; demos mkdimsum
  
  cl&gt; xfirstpass @demo.list demo13 fpmosaic ".exp" bpmask=demo.pl \
      shiftlist=demo.slist nsigrej=5.0 maxiter=10 secpexp=60.0
  
  cl&gt; xmaskpass fpmosaic fpmosaic.exp fpmosaic.corners mpmosaic   \
      ".exp" bpmask=demo.pl shiftlist=demo.slist nsigrej=5.0      \
      maxiter=10 secpexp=60.0
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
  xslm, xnslm, maskfix, xzap, xnzap, badpixupdate, xnregistar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

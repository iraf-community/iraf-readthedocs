.. _xmosaic:

xmosaic: Driver sript for first pass and mask pass processing steps
===================================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xmosaic inlist reference output expmap
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inlist">
  <dt><b>inlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inlist' Line='inlist' -->
  <dd>The list of input images to be combined.
  </dd>
  </dl>
  <dl id="l_reference">
  <dt><b>reference</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reference' Line='reference' -->
  <dd>The name of the reference image in <i>inlist</i> used to compute shifts if
  <i>fp_mkshifts</i> is yes. If reference is undefined the first image in
  <i>inlist</i> is assigned to be the reference image.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The root name of the output combined first and mask pass images. The 
  suffixes <span style="font-family: monospace;">"_fp"</span> and <span style="font-family: monospace;">"_mp"</span> are appended to the root name to distinguish
  the two images.
  </dd>
  </dl>
  <dl id="l_expmap">
  <dt><b>expmap = <span style="font-family: monospace;">".exp"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expmap' Line='expmap = ".exp"' -->
  <dd>The root name of the output first and mask pass xposure map images or the
  string appended to the output image name <i>output</i> to create the first and
  mask pass output exposure map image names. The suffixes <span style="font-family: monospace;">"_fp"</span> and <span style="font-family: monospace;">"_mp"</span>
  are appended to the root name to distinguish the two images.
  </dd>
  </dl>
  <dl id="l_fp_xslm">
  <dt><b>fp_xslm = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fp_xslm' Line='fp_xslm = yes' -->
  <dd>Perform the first pass sky subtraction step ? The input images must be sky
  subtracted before the bad pixel correction, cosmic ray removal, and
  image combining steps can be performed.
  </dd>
  </dl>
  <dl id="l_fp_maskfix">
  <dt><b>fp_maskfix = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fp_maskfix' Line='fp_maskfix = yes' -->
  <dd>Fix bad pixels in the sky subtracted images during the first pass using the
  bad pixel mask <i>bpmask</i> ?
  </dd>
  </dl>
  <dl id="l_fp_xzap">
  <dt><b>fp_xzap = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fp_xzap' Line='fp_xzap = yes' -->
  <dd>Remove cosmic rays from the sky subtracted images during the first pass
  using the xnzap task if <i>newxzap</i> = yes or xzap if <i>newxzap</i> = no ?
  </dd>
  </dl>
  <dl id="l_fp_badpixupdate">
  <dt><b>fp_badpixupdate = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fp_badpixupdate' Line='fp_badpixupdate = yes' -->
  <dd>Update the bad pixel mask <i>bpmask</i> during the first pass ? The bad pixel
  updating task adds pixels detected in 3 or more sky subtracted images to the
  bad pixel mask using the current cosmic ray masks. Bad pixel mask updating is
  only done if <i>fp_xzap</i> is yes.
  </dd>
  </dl>
  <dl id="l_fp_mkshifts">
  <dt><b>fp_mkshifts = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fp_mkshifts' Line='fp_mkshifts = no' -->
  <dd>Interactively determine the offsets required to combine the corrected images
  during the first and mask passes ?
  </dd>
  </dl>
  <dl id="l_fp_xnregistar">
  <dt><b>fp_xnregistar = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fp_xnregistar' Line='fp_xnregistar = yes' -->
  <dd>Compute the first pass combined output image and exposure map image using
  offsets and exposure time scaling defined in <i>shiftlist</i> ?
  </dd>
  </dl>
  <dl id="l_mp_mkmask">
  <dt><b>mp_mkmask = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_mkmask' Line='mp_mkmask = yes' -->
  <dd>Create the combined image object mask and inverse object core mask task ? If
  fp_mkmask is no and the object mask or inverse object mask do not
  exist the task will terminate.
  </dd>
  </dl>
  <dl id="l_mp_maskdereg">
  <dt><b>mp_maskdereg = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_maskdereg' Line='mp_maskdereg = yes' -->
  <dd>Create object masks and inverse object masks for the individual input images
  by extracting the appropriate sections of the combined image masks ?
  </dd>
  </dl>
  <dl id="l_mp_xslm">
  <dt><b>mp_xslm = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_xslm' Line='mp_xslm = yes' -->
  <dd>Perform the mask pass sky subtraction step using object masking ? The input
  images must be sky subtracted before the bad pixel correction, cosmic ray
  removal, and image combining steps can be performed.
  </dd>
  </dl>
  <dl id="l_mp_maskfix">
  <dt><b>mp_maskfix = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_maskfix' Line='mp_maskfix = yes' -->
  <dd>Fix bad pixels in the sky subtracted images during the mask pass using the
  bad pixel mask <i>bpmask</i> ?
  </dd>
  </dl>
  <dl id="l_mp_xzap">
  <dt><b>mp_xzap = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_xzap' Line='mp_xzap = yes' -->
  <dd>Remove cosmic rays from the sky subtracted images during the mask pass using
  the xnzap task if <i>newxzap</i> = yes or xzap if <i>newxzap</i> = no ? 
  </dd>
  </dl>
  <dl id="l_mp_badpixupdate">
  <dt><b>mp_badpixupdate = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_badpixupdate' Line='mp_badpixupdate = yes' -->
  <dd>Update the bad pixel mask <i>bpmask</i> during the mask pass ? The bad pixel
  updating task adds bad pixels detected in 3 or more sky subtracted
  images to the bad pixel mask using the current cosmic ray masks. Bad pixel
  updating is only done if <i>mp_xzap</i> is yes.
  </dd>
  </dl>
  <dl id="l_mp_xnregistar">
  <dt><b>mp_xnregistar = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_xnregistar' Line='mp_xnregistar = yes' -->
  <dd>Compute the mask pass combined output image and exposure map image using the
  positional offsets and exposure time scaling factors in <i>shiftlist</i>?
  </dd>
  </dl>
  <dl id="l_statsec">
  <dt><b>statsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='statsec' Line='statsec = ""' -->
  <dd>The input image section used to compute the sky statistics for each input
  image in the first and mask pass  sky subtraction and cosmic ray removal
  tasks. By default the entire input image is used.
  </dd>
  </dl>
  <dl id="l_nsigrej">
  <dt><b>nsigrej = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigrej' Line='nsigrej = 3.0' -->
  <dd>The rejection limits used to compute the sky statistics in number of sigma
  by the first and mask pass sky subtraction and cosmic ray removal tasks.
  </dd>
  </dl>
  <dl id="l_maxiter">
  <dt><b>maxiter = 20</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxiter' Line='maxiter = 20' -->
  <dd>The maximum number of rejection cycles used to compute the sky statistics
  by the first and mask pass sky subtraction and cosmic ray removal tasks.
  </dd>
  </dl>
  <dl id="l_sslist">
  <dt><b>sslist = <span style="font-family: monospace;">".sub"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sslist' Line='sslist = ".sub"' -->
  <dd>The output first pass and mask pass sky subtracted image list or the string
  appended to the input image names in <i>inlist</i> to create the output sky
  subtracted images names.
  </dd>
  </dl>
  <dl id="l_hmasks">
  <dt><b>hmasks = <span style="font-family: monospace;">".hom"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hmasks' Line='hmasks = ".hom"' -->
  <dd>The output mask pass holes mask list or the string appended to the sky
  subtracted image names to create the holes mask names.
  </dd>
  </dl>
  <dl id="l_newxslm">
  <dt><b>newxslm = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newxslm' Line='newxslm = no' -->
  <dd>Use the new xnslm task rather than the original xslm task in the first and mask
  passes ?
  </dd>
  </dl>
  <dl id="l_forcescale">
  <dt><b>forcescale = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='forcescale' Line='forcescale = yes' -->
  <dd>Force recalculation of the input image sky statistics during the first and
  mask pass sky subtraction step even though they have been previously computed
  and stored in the keyword <span style="font-family: monospace;">"SKYMED"</span>.
  </dd>
  </dl>
  <dl id="l_nmean">
  <dt><b>nmean = 6</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nmean' Line='nmean = 6' -->
  <dd>The number of neighboring images used by first and mask pass sky subtraction
  task to compute the sky image for each input image.
  </dd>
  </dl>
  <dl id="l_nskymin">
  <dt><b>nskymin = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nskymin' Line='nskymin = 3' -->
  <dd>The minimum number of input images used by the first and mask pass sky
  subtraction task  to compute the sky image.
  </dd>
  </dl>
  <dl id="l_nreject">
  <dt><b>nreject = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nreject' Line='nreject = 1' -->
  <dd>The number of high and low side pixels to reject when the sky image is 
  computed by the first and mask pass sky subtraction task.
  </dd>
  </dl>
  <dl id="l_cache">
  <dt><b>cache = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cache' Line='cache = yes' -->
  <dd>Enable image caching for improved efficiency in the new xnslm task ?
  </dd>
  </dl>
  <dl id="l_mp_useomask">
  <dt><b>mp_useomask = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_useomask' Line='mp_useomask = yes' -->
  <dd>Use object masks to recompute the sky statistics during the mask pass sky
  subtraction step. The object masks are used to create the sky images
  images regardless of the value of mp_useomask.
  </dd>
  </dl>
  <dl id="l_bpmask">
  <dt><b>bpmask</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bpmask' Line='bpmask' -->
  <dd>The name of the input bad pixel mask used to fix bad pixels in the sky
  subtracted images in the first and mask passes. Bpmask is assumed to be the
  same for all the input images and to consist of 0's in the bad pixel regions
  and 1's elsewhere. 
  </dd>
  </dl>
  <dl id="l_forcefix">
  <dt><b>forcefix = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='forcefix' Line='forcefix = yes' -->
  <dd>Force bad pixel fixing during the first and mask passes even though the image
  have been previously fixed as indicated by the presense of the keyword
  <span style="font-family: monospace;">"MASKFIX"</span>.
  </dd>
  </dl>
  <dl id="l_crmasks">
  <dt><b>crmasks = <span style="font-family: monospace;">".crm"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crmasks' Line='crmasks = ".crm"' -->
  <dd>The output first or mask pass cosmic ray mask list or the string appended to
  the sky subtracted image names to create the  output cosmic ray masks names.
  Cosmic ray masks consist of 1's in the cosmic ray regions and 0's elsewhere. 
  </dd>
  </dl>
  <dl id="l_newxzap">
  <dt><b>newxzap = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newxzap' Line='newxzap = yes' -->
  <dd>Use the new xnzap task rather than the original xzap task in the first and mask
  passes ?
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
  <dl id="l_fp_chkshifts">
  <dt><b>fp_chkshifts = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fp_chkshifts' Line='fp_chkshifts = no' -->
  <dd>Check and edit the list of input image reference stars, the list of
  registration stars, and the final offsets computed by the interactive
  offset computing task if <i>fp_mkshifts</i> is yes ?
  </dd>
  </dl>
  <dl id="l_fp_cradius">
  <dt><b>fp_cradius = 5.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fp_cradius' Line='fp_cradius = 5.0' -->
  <dd>The centroiding radius in pixels used by the interactive offset computing task
  if <i>fp_mkshifts</i> is yes.
  </dd>
  </dl>
  <dl id="l_fp_maxshift">
  <dt><b>fp_maxshift = 5.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fp_maxshift' Line='fp_maxshift = 5.0' -->
  <dd>The maximum permitted difference in pixels between the final computed offset and
  the offset predicted by the interactive offset computing task if
  <i>fp_mkshifts</i> is yes.
  </dd>
  </dl>
  <dl id="l_mp_mag">
  <dt><b>mp_mag = 4.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_mag' Line='mp_mag = 4.0' -->
  <dd>The block replication factor for the mask pass combined image and exposure map.
  </dd>
  </dl>
  <dl id="l_mp_blkrep">
  <dt><b>mp_blkrep = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_blkrep' Line='mp_blkrep = yes' -->
  <dd>Use block replication rather than bilinear interpolation to magnify the
  image if <i>mag</i> &gt; 1.0.
  </dd>
  </dl>
  <dl id="l_shiftlist">
  <dt><b>shiftlist = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shiftlist' Line='shiftlist = ""' -->
  <dd>The input shifts file used to combine the corrected images during the
  first and  mask passes. Shiftlist contains the corrected image name,
  the x and y offsets in user units (usually pixels), and the exposure time
  used to scale the image. If <i>fp_mkshifts</i> is yes shiftlist is the
  output of the interactive offset computing task. Otherwise shiftlist
  must be created by the user. 
  </dd>
  </dl>
  <dl id="l_sections">
  <dt><b>sections <span style="font-family: monospace;">".corners"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sections' Line='sections ".corners"' -->
  <dd>The output first pass sections file name or the string appended to the output
  first pass image name <i>output</i> to create the output first pass sections
  file name. The sections file contains the input image name from <i>inlist</i>,
  the coordinates of the lower left corner of the input image in the output
  combined image, and the coordinates of the upper right corner of the
  input image in the output combined image in columns 1 through 5 respectively.
  </dd>
  </dl>
  <dl id="l_rmasks">
  <dt><b>rmasks = <span style="font-family: monospace;">".rjm"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rmasks' Line='rmasks = ".rjm"' -->
  <dd>The output mask pass rejection mask list or the string appended to
  the sky subtracted image names to create the  output rejection mask names.
  Rejection masks consist of 1's in the good regions and 0's elsewhere. 
  </dd>
  </dl>
  <dl id="l_mp_nprev_omask">
  <dt><b>mp_nprev_omask = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_nprev_omask' Line='mp_nprev_omask = 0' -->
  <dd>The number of previous individual object masks that are combined to create
  the final individual object mask.
  </dd>
  </dl>
  <dl id="l_fractional">
  <dt><b>fractional = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fractional' Line='fractional = no' -->
  <dd>Use the fractional as well as integer part of the corrected image offsets if
  mag = 1. Bilinear interpolation is used to do the fractional part of the shift.
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
  <dl id="l_ncoavg">
  <dt><b>ncoavg = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncoavg' Line='ncoavg = 1' -->
  <dd>The number of co-averages per input image. The total exposure time for
  an image is ncoavg * exptime * secpexp where exptime is read from inlist.
  </dd>
  </dl>
  <dl id="l_secpexp">
  <dt><b>secpexp = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='secpexp' Line='secpexp = 1.0' -->
  <dd>The number of seconds per unit exposure time. Secpexp is required by the image
  combining task xnregistar.
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
  <dl id="l_omask">
  <dt><b>omask = <span style="font-family: monospace;">".msk"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='omask' Line='omask = ".msk"' -->
  <dd>The output combined image object mask name or the string appended to the first
  pass output image name <i>output_fp</i> to create the output combined object
  mask name. An additional <span style="font-family: monospace;">"i"</span> is added to the combined object mask name to
  create the inverse object core mask name. Object masks consist of 1's in
  object regions and 0's elsewhere. Inverse object masks are the reverse.
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
  <dl id="l_mp_statsec">
  <dt><b>mp_statsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_statsec' Line='mp_statsec = ""' -->
  <dd>The combined image section used to compute the sky statistics in the mask
  creation step. By default the entire combined image is used.
  </dd>
  </dl>
  <dl id="l_mp_nsigcrmsk">
  <dt><b>mp_nsigcrmsk = 1.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_nsigcrmsk' Line='mp_nsigcrmsk = 1.5' -->
  <dd>The factor times the recommended threshold used by the mask creation task to
  compute the combined image inverse object core  mask for cosmic ray unzapping.
  </dd>
  </dl>
  <dl id="l_mp_nsigobjmsk">
  <dt><b>mp_nsigobjmsk = 1.1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_nsigobjmsk' Line='mp_nsigobjmsk = 1.1' -->
  <dd>The factor times the recommended threshold used by the mask creation task to
  compute the combined input image object mask used for improving the sky
  subtraction.
  </dd>
  </dl>
  <dl id="l_mp_negthresh">
  <dt><b>mp_negthresh = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mp_negthresh' Line='mp_negthresh = no' -->
  <dd>Use negative as well as positive thresholds to create the combined input image
  object mask ?
  </dd>
  </dl>
  <dl id="l_ngrow">
  <dt><b>ngrow = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ngrow' Line='ngrow = 0' -->
  <dd>The object growing box half-width in pixels ?
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
  XMOSAIC sky subtracts, bad pixel corrects, and cosmic ray corrects the input
  images in <i>inlist</i> and combines them into a single combined output image
  <i>output</i> and accompanying exposure map image <i>expmap</i>. The image
  combining is done in two steps. The first step produces a first guess combined
  image which is used to construct the combined image object mask <i>omask</i>.
  The combined object mask is split into the corresponding individual image object
  masks which are used improve the sky subtraction and cosmic ray cleaning
  procedures in the final mask pass step.
  </p>
  <p>
  The output sky subtracted, bad pixel corrected, and cosmic ray corrected
  individual images are stored in <i>sslist</i>, and the output cosmic ray masks
  are stored in <i>crmasks</i>. The bad pixel mask is assumed to be the same for
  all the input images and consists of 0's in bad pixel regions and 1's elsewhere.
  Cosmic ray masks consist of 1's in the cosmic ray regions and 0's elsewhere.
  The locations of the input images in the output combined image are stored in
  <i>sections</i>. The combined object mask and inverse object core mask for the
  first pass combined image are stored in <i>omask</i> and its associated inverse
  mask. The individual image object masks and inverse object core masks are
  stored in <i>objmasks</i> and <i>ocrmasks</i> respectively. Object masks consist
  of 1's in the object regions and 0's elsewhere. Inverse object masks consist of
  0's in the object regions and 1's elsewhere. The output holes masks are stored
  in <i>hmasks</i>. Holes mask consist of 0's in regions where the sky subtraction
  is undefined and 1's elsewhere.
  </p>
  <p>
  If <i>fp_xslm</i> is yes XMOSAIC sky subtracts the input images using the
  XNSLM task if <i>newxslm</i> is yes or XSLM task f it is no, and writes the
  results to the output images <i>sslist</i>. For each input image XSLM/XNSLM
  computes the running mean of the <i>nmean</i> neighboring
  images, after scaling them by the median pixel values and rejecting the
  <i>nreject</i> highest scaled pixels. There must be at least <i>nskymin</i>
  neighboring images for a sky image to be computed and subtracted. The input
  image medians are computed using pixels in the region defined by <i>statsec</i>
  and iterative rejection with rejection parameters <i>nsigrej</i> and
  <i>maxiter</i>. The reciprocal of the computed median is stored in the image
  header keyword <span style="font-family: monospace;">"SKYMED"</span>. If <i>forcescale</i> is no and the <span style="font-family: monospace;">"SKYMED"</span> keyword
  is already defined in the image header, then the image medians are not
  recomputed. When sky subtraction is complete the keyword SKYSUB is written
  to the sky subtracted image header. More information about the XSLM/XNSLM
  task can be found in the XSLM/XNSLM help pages.
  </p>
  <p>
  If <i>fp_maskfix</i> is yes XMOSAIC removes known bad pixels from sky subtracted
  images <i>sslist</i> using the MASKFIX task and the bad pixel mask <i>bpmask</i>.
  The bad pixel mask consists of 0's in bad pixel regions and 1's elsewhere and
  must be the same size as the input sky subtracted images. The bad pixels are
  removed by linearly interpolating across bad columns in each image line. When
  bad pixel removal is complete the keyword <span style="font-family: monospace;">"MASKFIX"</span> is written to the header
  of the sky subtracted image. If <i>forcefix</i> is no and <span style="font-family: monospace;">"MASKFIX"</span> exists in
  the image header then the bad pixel removal step is skipped. More information
  on the MASKFIX task can be found in the MASKFIX help page.
  </p>
  <p>
  If <i>fp_xzap</i> is yes XMOSAIC removes cosmic rays from the sky subtracted
  images <i>sslist</i>  using the XNZAP task if <i>newxzap</i> is yes or the
  XZAP task if it is no, and writes the cosmic ray masks to <i>crmasks</i>.
  The output cosmic ray masks contain 1's in the cosmic ray regions and 0's
  elsewhere.  Both XZAP and XNZAP write the keyword CRMASK which contains the
  name of the output cosmic ray MASK to the cosmic ray corrected image. If the
  CRMASK keyword is present in the sky subtracted image headers cosmic ray
  cleaning is skipped. XZAP is the tried and true XDIMSUM cosmic ray removal
  task. XNZAP is experimental but promises to be a faster technique.
  </p>
  <p>
  XZAP detects and removes cosmic rays by finding pixels which are more than
  5.0 sky sigma above the median of the surrounding box of 5 by 5 pixels,
  and which are not part of an object where an object is any pixel more than
  2.0 sky sigma above the median of the surrounding 15 by 15 box of pixels.
  XZAP uses a sky subsampling factor of 2 and cosmic ray and region growing
  box widths of 0.0 and 0.0 respectively. The sky sigma is computed using
  the region of the input sky subtracted images specified by <i>statsec</i> 
  and iterative rejection with rejection parameters <i>nsigrej</i> and 
  fImaxiter. The cosmic rays in the input sky subtracted images are replaced
  with the local median value.  More information on the XZAP task can be found
  in the XZAP help page.
  </p>
  <p>
  XNZAP detects and removes cosmic rays by finding pixels which are
  more than 5.0 sky sigma above the mean of the surrounding box of 5 by 5
  pixels with the central pixel and the highest pixel removed, and which are
  not part of an object where an object is more than 5.0 sky sigma above
  the local background. The local background is defined as the median of
  the pixels in an annulus 5.0 pixels wide around the averaging box. The
  local sky sigma is estimated by computing the percentile points of pixels
  in 25 by 25 pixel subsections evenly distributed over the image. The cosmic
  ray and object growing radii are set to 0.0 and 0.0 respectively.
  The cosmic rays in the input sky subtracted images are replaced with the
  local average value. More information on the XNZAP task can be found in the
  XNZAP and CRAVERAGE help pages.
  </p>
  <p>
  If <i>fp_xzap</i> is yes and <i>fp_badpixupdate</i> is yes then XMOSAIC updates
  the bad pixel mask <i>bpmask</i>a using the BADPIXUPDATE task. BADPIXUPDATE
  examines the list of cosmic rays image produced by XZAP or XNZAP, searches
  for pixels that are bad in 3 or more images, and sets those pixels in
  <i>bpmask</i> t0 0. More information about BADPIXUPDATE can be found in the
  BADPIXUPDATE help page.
  </p>
  <p>
  If <i>fp_mkshifts</i> = yes then XMOSAIC calls the XDSHIFTS task to determine
  the x and y shifts required to accurately combine the sky subtracted images.
  XDSHIFTS displays the sky subtracted images and requests the user to identify
  a reference object common to all of them, then displays the reference image
  <i>reference</i> and requests the user to identify a set of registration objects.
  The reference objects are used to compute initial offset with respect to the
  reference image. The positions of the registration objects in each image are
  computed using a centroiding algorithm and a centering radius of
  <i>fp_cradius</i> pixels. Objects with offsets that are more than
  <i>fp_maxshifts</i> pixels larger than the initial offsets are rejected from
  the registration list and the shifts of the remaining objects are averaged
  to compute the final shift for each image. If <i>fp_chkshifts</i> is yes the user
  is permitted to edit the reference object list, the registration list,
  and the list of final shifts. Currently XDSHIFTS sets the exposure times of
  the input sky subtracted images to 1.0. More about the XDSHIFTS can
  be found in the XDSHIFTS help page.
  </p>
  <p>
  If <i>fp_mkshifts</i> = no then the name of the sky subtracted image, its x and y
  shifts relative to the reference image and its exposure time are read from
  the file <i>shiftlist</i>. Shiftlist may have been written by the XDSHIFTS,
  XMSHIFTS, XFSHIFTS, or XRSHIFTS tasks.
  </p>
  <p>
  If <i>fp_xnregistar</i> is yes then xmosaic combines the sky subtracted images
  into the first guess output combined image <i>output</i> and output exposure map
  image <i>expmap</i> using the bad pixel mask <i>bpmask</i>, and offsets and
  scaling factors in <i>shiftlist</i> if <i>fp_mkshifts</i> is no, or computed by
  XDSHIFTS if the <i>fp_mkshifts</i> is yes. If <i>fractional</i> is no only the
  integer part of the shifts is used. XMOSAIC calls the XNREGISTAR task to do the
  actual image combining. The parameters <i>pixin</i>, <i>ab_sense</i>,
  <i>xscale</i>, <i>yscale</i>, and <i>a2x_angle</i> are used to convert shifts from
  user units, e.g. arcseconds to units of pixels in the reference image. The
  parameters <i>ncoavg</i> and <i>secpexp</i> are used to normalize the input
  exposure times.  The parameters <i>y2n_angle</i> and <i>rotation</i> are used to
  orient the final combined image and exposure map to within 45 degrees of north
  up and east to the left. The pixel positions of the input images in the output
  combined image are stored stored in the file <i>sections</i> for later use in
  the mask deregistration step.
  </p>
  <p>
  If <i>mp_mkmask</i> is yes the first pass combined image object mask
  <i>omask</i> and its associated inverse object core mask  are created
  by the MKMASK task using thresholding factors <i>mp_nsigobjmask</i> and
  <i>mp_nsigcrmask</i> times the recommended thresholding factor respectively.
  If <i>mp_negthresh</i> is <span style="font-family: monospace;">"yes"</span> then both negative and positive masking
  thresholds are used to create the combined image object mask.
  The recommended threshold is computed using pixels in the section specified
  by <i>mp_statsec</i> and iterative rejection with rejection parameters
  <i>nsigrej</i> and <i>maxiter</i>. If <i>chkmasks</i> is yes the user is permitted
  to examine the combined image and set the threshold level. MKMASK uses default
  values of 2, 15, and 3 for the MKMASK image subsampling factor, median filter
  size, and smoothing size respectively. More about the MKMASK task can be found
  in the task help page.
  </p>
  <p>
  If <i>mp_maskdereg</i> is yes then individual object masks and inverse object
  core masks <i>objmasks</i> and <i>ocrmasks</i> are created from the combined
  image object masks using information in the <i>sections</i> file. If
  <i>mp_nprev_omask</i> &gt; 0 then the object mask for each individual image is the
  sum of its own mask and those of its nprev_omask neighbors. The inverse object
  core masks are used to unzap cosmic rays in object regions where the cosmic ray
  positions are identified in <i>crmasks</i>. The object mask and inverse object
  core mask names are stored in the image header keywords <span style="font-family: monospace;">"OBJMASK"</span> and
  <span style="font-family: monospace;">"CROBJMAS"</span> respectively. If <i>mp_maskdereg</i> is no then the object masks
  are assumed to already exist.
  </p>
  <p>
  If <i>mp_xslm</i> is yes XMOSAIC sky subtracts the input images using the
  XNSLM task if <i>newxslm</i> is yes or XSLM task if it is no and the object
  masks <i>objmasks</i>, and writes the results to the
  output images <i>sslist</i>. Existing sky subtracted images are overwritten.
  The object masks are assumed to have been created by the MASKDEREG task and
  their names tored in the keyword OBJMASK in the input images. XSLM/XNSLM
  computes the running mean of the <i>nmean</i> neighboring images, after scaling
  by their median pixel values and rejecting the <i>nreject</i> highest scaled
  pixels. There must be at least <i>nskymin</i> neighboring images for a sky
  image to be computed and subtracted. The input image medians are computed
  using pixels in the region defined by <i>statsec</i>, the object mask
  <i>objmask</i> if <i>mp_useomask</i> is yes, and iterative rejection with
  rejection parameters <i>nsigrej</i> and <i>maxiter</i>. The reciprocal of the
  computed median is stored in the image header keyword <span style="font-family: monospace;">"SKYMED"</span>. If
  <i>forcescale</i> is no and the <span style="font-family: monospace;">"SKYMED"</span> keyword already exists in the image
  header then the image medians are not recomputed. If use of the object masks
  results in sky image pixels which are undefined then the holes mask <i>hmasks</i>
  is written.  Holes masks consist of 0's in undefined regions and 1's elsewhere.
  If a holes mask was created then the keyword <span style="font-family: monospace;">"HOLES"</span> containing the name of the
  holes mask is written to the output image. More information about the
  XSLM/XNSLM task can be found in the XSLM/XNSLM help pages.
  </p>
  <p>
  If <i>mp_maskfix</i> is yes XMOSAIC removes known bad pixels from sky
  subtracted images <i>sslist</i> using the MASKFIX task and the bad pixel mask
  <i>bpmask</i> exactly as it does in the first pass with the exception that
  the bad pixel mask may have been updated during the first pass. 
  </p>
  <p>
  If <i>mp_xzap</i> is yes XMOSAIC removes cosmic rays from the sky subtracted
  images <i>sslist</i>  using the XNZAP task if <i>newxzap</i> is yes or the
  XZAP task if it is no, and writes the cosmic ray masks to <i>crmasks</i>.
  Existing cosmic ray masks are overwritten.
  </p>
  <p>
  XZAP detects and removes cosmic rays by finding pixels which are more than
  5.0 sky sigma above the median of the surrounding box of 5 by 5 pixels
  and are not part of an object where an object is any pixel located in
  an object region defined by the inverse object masks <i>ocrmasks</i>
  stored in the header keyword <span style="font-family: monospace;">"CROBJMAS"</span>. More information about XZAP can
  be found in the corresponding description for the first pass cosmic ray
  cleaning step and  in the XZAP help page.
  </p>
  <p>
  XNZAP detects and removes cosmic rays by finding pixels which are
  more than 5.0 sky sigma above the mean of the surrounding box of 5 by 5
  pixels with the central pixel and the highest pixel removed and which are
  not part of an object where an object is defined by the inverse object
  mask <i>ocrmasks</i> stored in the image header keyword <span style="font-family: monospace;">"CROBJMAS"</span>. More
  information about XNZAP can be found in the corresponding description for
  the first pass cosmic ray cleaning step and in the XNZAP and CRAVERAGE
  help pages.
  </p>
  <p>
  If <i>mp_xzap</i> is yes and <i>mp_badpixupdate</i> is yes then XMOSAIC updates
  the bad pixel mask <i>bpmask</i> with the BADPIXUPDATE task in exactly the
  same way as it is done in the first pass.
  </p>
  <p>
  In preparation for final image combining the name of the sky subtracted image,
  its x and y shifts relative to the reference image and its exposure time are
  read from the file <i>shiftlist</i>. Shiftlist be a preexisting file written by
  one of the XDSHIFTS, XMSHIFTS, XFSHIFTS, or XRSHIFTS tasks or have been created
  interactively in the first pass with the XDSHIFTS task.
  </p>
  <p>
  If <i>mp_xnregistar</i> is yes then XMOSAIC combines the sky subtracted images
  into the output combined image <i>output</i> and output exposure map image
  <i>expmap</i> using the rejection masks <i>rmasks</i>. Rejection masks consist
  of 1's and 0's with 1's defining the good regions. Rejection masks are
  created by the XMSKCOMBINE task which combines the bad pixel mask <i>bpmask</i>,
  the cosmic ray masks <i>crmasks</i>, the holes masks <i>hmasks</i>, and the
  <i>nprev_omask</i> object masks in <i>objmasks</i> and  offsets
  and scaling factors read from <i>shiftlist</i>. XMOSAIC calls the XNREGISTAR
  task to do the actual image combining. The parameters <i>pixin</i>,
  <i>ab_sense</i>, <i>xscale</i>, <i>yscale</i>, and <i>a2x_angle</i> are used to
  convert shifts from user units, e.g. arcseconds to units of pixels in the
  reference image. The magnification factor <i>mp_mag</i> determines the
  magnification of the final combined image with respect the the initial
  combined image. If mag = 1 and <i>fractional</i> is no only the integer part
  of the shifts is used. If mag &gt; 1 and <i>mp_blkrep</i> is yes then block
  replication is used to do the magnification, otherwise bilinear interpolation
  is used. The parameters <i>ncoavg</i> and <i>secpexp</i> are used
  to normalize the input exposure times. The parameters <i>y2n_angle</i> and
  <i>rotation</i> are used to orient the final combined image and exposure map to
  within 45 degrees of north up and east to the left. 
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Perform a first and mask pass image combining operation on the demo images
  using the default shiftlist demo.slist.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; demos mkxdimsum
  
  cl&gt; xmosaic @demo.list demo13 mosaic ".exp" shiftlist=demo.slist nsigrej=5.0 \
      maxiter=10 bpmask=demo.pl secpexp=60.0
  </pre></div>
  <p>
  2. Repeat the first pass image combining operation on the demo images but
  determine the shifts interactively.
  </p>
  <p>
  cl&gt; xmosaic @demo.list demo13 mosaic <span style="font-family: monospace;">".exp"</span> fp_mkshifts=yes  \<br>
      shiftlist=myshiftlist nsigrej=5.0 maxiter=10 bpmask=demo.pl secpexp=60.0
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  ... do first pass sky subtraction with xslm
  ... do first pass bad pixel correction with maskfix
  ... do first pass cosmic ray cleaning with xzap
  ... do first pass bad pixel mask updating with badpixupdate
  
  ... enter the interactive xdshifts task
  
  ... the first sky subtracted image is displayed and imexamine starts
  ... use the n and p keystrokes to step though the image list
  ... select a reference object common to all image
  ... type q to quit imexamine
  
  ... the first sky subtracted image is displayed and imexamine starts
  ... move cursor to reference object and type a
  ... type n to display next image
  ... repeat previous 2 steps until first image is redisplayed
  ... type q to quit imexamine
  
  ... the reference sky subtracted image is displayed
  ... move cursor to registration objects and type a
  ... type q to quit xdisplay
  
  ... do first pass image combining with xnregistar
  
  
  ... create master object and inverse object masks with mkmask
  ... create individual object and inverse object masks with maskdereg
  ... do mask pass sky subtraction with xslm
  ... do mask pass bad pixel correction with maskfix
  ... do mask pass cosmic ray cleaning with xzap
  ... do mask pass bad pixel mask updating with badpixupdate
  ... do mask pass image combining with xnregistar
  
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
  xfirstpass, xmaskpass, xslm, xnslm, maskfix, xzap, xnzap, badpixupdate, xdshifts
  xnregistar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

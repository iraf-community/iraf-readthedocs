.. _xfirstpass:

xfirstpass: Driver script for first pass processing steps
=========================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xfirstpass inlist reference output expmap
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
  <dd>The name of the reference image used to compute offsets if <i>mkshifts</i> is
  yes. If reference is undefined the first image in <i>inlist</i> is assigned to
  be the reference image.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The name of the output combined image.
  </dd>
  </dl>
  <dl id="l_expmap">
  <dt><b>expmap = <span style="font-family: monospace;">".exp"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expmap' Line='expmap = ".exp"' -->
  <dd>The name of the output exposure map image or the string appended to the output
  combined image name <i>output</i> to create the output exposure map image name.
  </dd>
  </dl>
  <dl id="l_statsec">
  <dt><b>statsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='statsec' Line='statsec = ""' -->
  <dd>The input image section used to compute the sky statistics for each input
  image in the sky subtraction and cosmic ray removal steps. By default the
  entire input image is used.
  </dd>
  </dl>
  <dl id="l_nsigrej">
  <dt><b>nsigrej = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigrej' Line='nsigrej = 3.0' -->
  <dd>The rejection limits used to compute the sky statistics.
  </dd>
  </dl>
  <dl id="l_maxiter">
  <dt><b>maxiter = 20</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxiter' Line='maxiter = 20' -->
  <dd>The maximum number of rejection cycles used to compute the sky statistics.
  </dd>
  </dl>
  <dl id="l_xslm">
  <dt><b>xslm = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xslm' Line='xslm = yes' -->
  <dd>Perform the sky subtraction step using the xnslm task id <i>newxslm</i> is yes
  or the xslm task if it is no ? The input images must be sky subtracted before
  the bad pixel fixing, cosmic ray removal, and image combining steps can be
  performed.
  </dd>
  </dl>
  <dl id="l_sslist">
  <dt><b>sslist = <span style="font-family: monospace;">".sub"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sslist' Line='sslist = ".sub"' -->
  <dd>The output sky subtracted image list or the string appended to the input image
  names in <i>inlist</i> to create the names of the output sky subtracted images.
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
  <dd>Force recalculation of the input image statistics by even though they have
  been computed previously and stored in the keyword <span style="font-family: monospace;">"SKYMED"</span>.
  </dd>
  </dl>
  <dl id="l_nmean">
  <dt><b>nmean = 6</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nmean' Line='nmean = 6' -->
  <dd>The number of neighboring images used by the sky subtraction task to computed
  the sky image for each input image.
  </dd>
  </dl>
  <dl id="l_nskymin">
  <dt><b>nskymin = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nskymin' Line='nskymin = 3' -->
  <dd>The minimum number of input images used by the sky subtraction task to compute
  the sky image.
  </dd>
  </dl>
  <dl id="l_nreject">
  <dt><b>nreject = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nreject' Line='nreject = 1' -->
  <dd>The number of high and low side pixels to be rejected  by the sky subtraction
  task when it computes the sky image.
  </dd>
  </dl>
  <dl id="l_cache">
  <dt><b>cache = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cache' Line='cache = yes' -->
  <dd>Enable image cacheing fro improved efficiency in the new xnslm task ?
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
  <dd>The name of the input image bad pixel mask used to fix bad pixel in the sky
  subtracted images. Bpmask is assumed to be the same for all the input images
  and to consist of 0's in the bad pixel regions and 1's elsewhere. If bpmask is
  undefined the bad pixel fixing step is skipped.
  </dd>
  </dl>
  <dl id="l_forcefix">
  <dt><b>forcefix = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='forcefix' Line='forcefix = yes' -->
  <dd>Force bad pixel fixing even though the images have been previously fixed as
  indicated by the presense of the keyword <span style="font-family: monospace;">"MASKFIX"</span> in their headers.
  </dd>
  </dl>
  <dl id="l_xzap">
  <dt><b>xzap = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xzap' Line='xzap = yes' -->
  <dd>Remove cosmic rays from the sky subtracted images using the xnzap task
  if <i>newxzap</i> = yes or the xzap task if <i>newxzap</i> = no ?
  </dd>
  </dl>
  <dl id="l_crmasks">
  <dt><b>crmasks = <span style="font-family: monospace;">".crm"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crmasks' Line='crmasks = ".crm"' -->
  <dd>The list of output cosmic ray masks or the string appended to the input image
  names in <i>inlist</i> to create the names of the output cosmic ray masks.
  Cosmic ray masks consist of 1's in the cosmic ray regions and 0's elsewhere. 
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
  <dd>Update the bad pixel mask <i>bpmask</i> by adding cosmic ray pixels detected in
  <i>nrepeats</i> or more sky subtracted images to the bad pixel mask. Bad pixel
  mask updating is only done if <i>xzap</i> is yes.
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
  <dl id="l_mkshifts">
  <dt><b>mkshifts = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mkshifts' Line='mkshifts = no' -->
  <dd>Determine the shifts required to combine the sky subtracted images interactively
  using image display and image cursor ? In order to use this option the
  image display server must be running before xfirstpass is called.
  </dd>
  </dl>
  <dl id="l_chkshifts">
  <dt><b>chkshifts = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='chkshifts' Line='chkshifts = no' -->
  <dd>Edit the lists of input image reference stars, the list of registration
  stars, and the final offsets created by the user in the interactive shift
  computation step.
  </dd>
  </dl>
  <dl id="l_cradius">
  <dt><b>cradius = 5.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cradius' Line='cradius = 5.0' -->
  <dd>The centroiding radius in pixels used in the interactive offset computation
  step.
  </dd>
  </dl>
  <dl id="l_maxshift">
  <dt><b>maxshift = 5.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxshift' Line='maxshift = 5.0' -->
  <dd>The maximum permitted difference in pixels between the final computed offset
  and the predicted offset determined in the interactive offset computation
  step.
  </dd>
  </dl>
  <dl id="l_xnregistar">
  <dt><b>xnregistar = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xnregistar' Line='xnregistar = yes' -->
  <dd>Compute the combined output image and exposure map image using offsets and
  exposure time scaling ?
  </dd>
  </dl>
  <dl id="l_shiftlist">
  <dt><b>shiftlist = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shiftlist' Line='shiftlist = ""' -->
  <dd>The input shifts file used to combine the sky subtracted images if
  <i>mkshifts</i> = no or the output shifts file if <i>mkshifts</i> is yes.
  Shiftlist consists of the sky subtracted image
  name, the x and y offsets in user units (usually pixels), and the
  exposure time used to scale the image (usually 1). If shiftlist is undefined
  and <i>mkshifts</i> = no then xfirstpass terminates with a warning message.
  </dd>
  </dl>
  <dl id="l_sections">
  <dt><b>sections = <span style="font-family: monospace;">".corners"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sections' Line='sections = ".corners"' -->
  <dd>The name of the output sections file or the string appended to the output
  image name <i>output</i> to create the output sections file name. The sections
  file contains the input image name from <i>inlist</i>, the coordinates of the
  lower left corner of the input image in the output combined image, and the
  coordinates of the upper right corner of the input image in the output
  combined image in columns 1 through 5 respectively.
  </dd>
  </dl>
  <dl id="l_fractional">
  <dt><b>fractional = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fractional' Line='fractional = no' -->
  <dd>Use the fractional as well as integer part of the sky subtracted image
  offsets. The imshift task and bilinear interpolation are used to do the
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
  <dd>Is the rotation of the a to b axis counter-clockwise ? The a and b
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
  an image is ncoavg * exptime * secpexp where exptime is read from
  <i>shiftlist</i>.
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
  through east. If set correctly y2n_angle can be used to orient the output image
  to within 45 degrees of N up and E left.
  </dd>
  </dl>
  <dl id="l_rotation">
  <dt><b>rotation = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rotation' Line='rotation = yes' -->
  <dd>Is the rotation of the input image north axis to the east axis
  counter-clockwise ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XFIRSTPASS sky subtracts, bad pixel corrects, and cosmic ray corrects the
  input images <i>inlist</i> and combines them into a single output image
  <i>output</i>. The associated exposure map is written to the image <i>expmap</i>.
  The individual output sky subtracted, bad pixel corrected, and cosmic ray
  corrected images are stored in <i>sslist</i>, and associated output cosmic ray
  masks are stored in <i>crmasks</i>. The locations of the input images in the
  output combined image are stored in <i>sections</i> for later use by
  the XMASKPASS task.
  </p>
  <p>
  If <i>xslm</i> is yes XFIRSTPASS sky subtracts the input images using the
  XNSLM task if <i>newxslm</i> is yes or XSLM task if it is no and writes the
  results to the output images <i>sslist</i>. For each input image XNSLM/XSLM
  computes the running mean of the <i>nmean</i> neighboring
  images, after scaling them by the median pixel values, and rejecting the
  <i>nreject</i> highest scaled pixels. There must be at least <i>nskymin</i>
  neighboring images for a sky image to be computed and subtracted from the
  input image. The input image medians are computed using pixels in the region
  defined by <i>statsec</i> and an iterative <i>nsigrej</i> rejection algorithm
  with the maximum number of iterations set to <i>maxiter</i>. The reciprocal of
  the computed median is stored in the image header keyword <span style="font-family: monospace;">"SKYMED"</span>. If
  <i>forcescale</i> is no and the <span style="font-family: monospace;">"SKYMED"</span> keyword already exists in the input
  image header then the image medians are not recomputed. When sky subtraction
  is complete the keyword SKYSUB is written to the output image header. More
  information about the XSLM/XNSLM task can be found in the XSLM/XNSLM help pages.
  </p>
  <p>
  If <i>maskfix</i> is yes XFIRSTPASS removes known bad pixels from the sky
  subtracted images <i>sslist</i> using the MASKFIX task and the bad pixel mask
  <i>bpmask</i>. The bad pixel mask consists of 0's in bad pixel regions and 1's
  elsewhere and must be the same size as the input sky subtracted images. The bad
  pixels are removed by linearly interpolating across bad columns in each image
  line. When bad pixel removal is complete the keyword <span style="font-family: monospace;">"MASKFIX"</span> is written to
  the header of the sky subtracted image. If <i>forcefix</i> is no and <span style="font-family: monospace;">"MASKFIX"</span>
  exists in the image header then the bad pixel removal step is skipped. More
  information on the MASKFIX task can be found in the MASKFIX help page.
  </p>
  <p>
  If <i>xzap</i> is yes XFIRSTPASS removes cosmic rays from the sky subtracted
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
  and iterative <i>nsigrej</i> rejection with the maximum number of rejections
  set to <i>maxiter</i>.  The cosmic rays in the input sky subtracted images are
  replaced with the local median value. More information on the XZAP task
  can be found in the XZAP help page.
  </p>
  <p>
  XNZAP detects and removes cosmic rays by finding pixels which are
  more than 5.0 sky sigma above the mean of the surrounding box of 5 by 5
  pixels with the central pixel and the highest pixel removed, and which are
  not part of an object where an object is als more than 5.0 sky sigma above
  the local background. The local background is defined as the median of
  the pixels in an annulus 5.0 pixels wide around the averaging box. The
  local sky sigma is estimated by computing the percentile points of pixels
  in 25 by 25 pixel subsections evenly distributed over the image. The cosmic
  ray and object growing radii are set to 0.0 and 0.0 respectively.
  The cosmic rays in the input sky subtracted images are replaced with the
  local average value. More information on the XNZAP task can be found in the
  XNZAP help page.
  </p>
  <p>
  If <i>xzap</i> is yes and <i>badpixupdate</i> is yes then XFIRSTPASS updates
  the bad pixel mask <i>bpmask</i> using the BADPIXUPDATE task. BADPIXUPDATE
  examines the list of cosmic rays image produced by XZAP or XNZAP, searches
  for pixels that are bad in 3 or more images, and sets those pixels in
  <i>bpmask</i> to 0.
  </p>
  <p>
  If <i>mkshifts</i> = yes then XFIRSTPASS calls the XDSHIFTS task to determine
  the x and y shifts required to accurately combine the sky subtracted, bad pixel
  corrected, and cosmic ray corrected images. XDSHIFTS displays the corrected
  images and requests the user to identify a reference object common to all of
  them, then displays the reference image <i>reference</i> and requests the user
  to identify a set of registration objects. The reference objects are used to
  compute initial shifts. The positions of the registration objects in each image
  are computed using a centroiding algorithm and a centering radius of
  <i>cradius</i> pixels. Objects with shifts that are more than <i>maxshifts</i>
  pixels larger than the initial shifts are rejected from the registration
  list and the shifts of the remaining objects are averaged to compute
  the final shift for each image. If <i>chkshifts</i> is yes the user
  is permitted to edit the reference object list, the registration list,
  and the list of final shifts. The final shifts are written to <i>shiftfile</i>
  Currently XDSHIFTS sets the exposure times of the input sky subtracted images
  to 1.0.
  </p>
  <p>
  If <i>mkshifts</i> = no then the name of the sky subtracted image, its x and y
  shifts relative to the reference image and its exposure time are read from
  the file <i>shiftlist</i>. Shiftlist may have been written by the XDSHIFTS,
  XMSHIFTS, XFSHIFTS, or XRSHIFTS tasks.
  </p>
  <p>
  If <i>xnregistar</i> is yes then XFIRSTPASS combines the corrected images
  into the output combined image <i>output</i> and output exposure map image
  <i>expmap</i> using the badpixel mask <i>bpmask</i>, offsets and scaling
  factors in <i>shiftlist</i> if <i>mkshifts</i> is no, or computed by
  XDSHIFTS if the <i>mkshifts</i> is yes.  If <i>fractional</i> is no only
  the integer part of the shifts is used. XFIRSTPASS call the XNREGISTAR
  task to do the actual image combining. The parameters <i>pixin</i>,
  <i>ab_sense</i>, <i>xscale</i>, <i>yscale</i>, and <i>a2x_angle</i> are
  used to convert shifts from user units, e.g. arcseconds to units of
  pixels in the reference image. The units of <i>ncoavg</i> and <i>secpexp</i>
  are used to normalize the input exposure times. The parameters 
  <i>y2n_angle</i> and <i>rotation</i> are used to orient the final
  combined image and exposure map to within 45 degrees of north up and east to
  the left. Finally the pixel positions of the input images in the output
  combined images are stored stored in the file <i>sections</i> suffix.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Do a first pass image combining operation on the demo images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; demos mkxdimsum
  
  cl&gt; xfirstpass @demo.list demo13 fpmosaic ".exp" bpmask=demo.pl \
      shiftlist=demo.slist nsigrej=5.0 maxiter=10 secpexp=60.0
  </pre></div>
  <p>
  2. Repeat the first pass image combining operation on the demo images but
  determine the shifts interactively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xfirstpass @demo.list demo13 fpmosaic ".exp" bpmask=demo.pl \
      mkshifts+  nsigrej=5.0 maxiter=10 secpexp=60.0
  
      ... do sky subtraction with xslm
      ... do badpix correction with maskfix
      ... do cosmic ray cleaning with xzap
      ... do bad pixel mask updating with badpixupdate
  
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
      ... the task enters the default editor
      ... edit in any required changes
      ... quit the editor
  
      ... the reference sky subtracted image is displayed
      ... move cursor to registration objects and type a
      ... type q to quit xdisplay
      ... the task enters the default editor
      ... edit in any required changes
      ... quit the editor
  
      ... do image combining with xnregistar
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
  xslm, xnslm, maskfix, xzap, xnzap, badpixupdate, xdshifts, xnregistar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

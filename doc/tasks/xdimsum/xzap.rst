.. _xzap:

xzap: Remove cosmic rays from images using median filtering
===========================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xzap inlist omasks outlist crmasks
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inlist">
  <dt><b>inlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inlist' Line='inlist' -->
  <dd>The list of input sky subtracted images to be cosmic ray corrected.
  </dd>
  </dl>
  <dl id="l_omasks">
  <dt><b>omasks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='omasks' Line='omasks' -->
  <dd>The list of input inverse object core masks used to unzap cosmic rays detected
  in object regions or the input image keyword containing the name of the inverse
  object mask normally CROBJMAS. Inverse object core masks contain 0's in object
  regions and 1's elsewhere. Note that this is the inverse of the usual
  definition of an object mask.
  </dd>
  </dl>
  <dl id="l_outlist">
  <dt><b>outlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outlist' Line='outlist' -->
  <dd>The list of output cosmic ray corrected images. The output image list can
  be the same as the input image list.
  </dd>
  </dl>
  <dl id="l_crmasks">
  <dt><b>crmasks = <span style="font-family: monospace;">".crm"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crmasks' Line='crmasks = ".crm"' -->
  <dd>The list of output cosmic ray masks or the suffix appended to the output
  image name to create the output cosmic ray mask name. Cosmic ray masks contain
  1's in cosmic ray regions and 0's elsewhere. The name of the output cosmic ray
  mask is stored in the input and output image header keyword CRMASK.
  </dd>
  </dl>
  <dl id="l_statsec">
  <dt><b>statsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='statsec' Line='statsec = ""' -->
  <dd>The input image section used to compute the image statistics for each input
  image. By default the entire input image is used.
  </dd>
  </dl>
  <dl id="l_nsigrej">
  <dt><b>nsigrej = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigrej' Line='nsigrej = 3.0' -->
  <dd>The rejection limits used to compute the image statistics in number of sigma.
  </dd>
  </dl>
  <dl id="l_maxiter">
  <dt><b>maxiter = 20</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxiter' Line='maxiter = 20' -->
  <dd>The maximum number of rejection cycles used to compute the image statistics.
  </dd>
  </dl>
  <dl id="l_checklimits">
  <dt><b>checklimits = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='checklimits' Line='checklimits = yes' -->
  <dd>Check the input image data limits for the fast median filter ? If checklimits
  is yes then the lower and upper data limits are set to max (<i>zmin</i>,
  image_min) and min (<i>zmax</i>, image_max) respectively. If checklimits is no
  no image data limits checking is done.
  </dd>
  </dl>
  <dl id="l_zmin">
  <dt><b>zmin = -32768.0, zmax = 32767.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zmin' Line='zmin = -32768.0, zmax = 32767.0' -->
  <dd>The default data limits supplied to the fast median filter if
  <i>checklimits</i> is yes.
  </dd>
  </dl>
  <dl id="l_zboxsz">
  <dt><b>zboxsz = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zboxsz' Line='zboxsz = 5' -->
  <dd>The size in pixels of the fast median filtering box.
  </dd>
  </dl>
  <dl id="l_nsigzap">
  <dt><b>nsigzap = 5.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigzap' Line='nsigzap = 5.0' -->
  <dd>The cosmic ray detection threshold in units of sky sigma.
  </dd>
  </dl>
  <dl id="l_nsigobj">
  <dt><b>nsigobj = 2.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigobj' Line='nsigobj = 2.0' -->
  <dd>The object detection threshold in units of sky sigma. If nsigobj &lt;= 0.0
  only cosmic ray detection is performed.
  </dd>
  </dl>
  <dl id="l_subsample">
  <dt><b>subsample = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subsample' Line='subsample = 1' -->
  <dd>The input image subsampling factor used in the object detection step.
  </dd>
  </dl>
  <dl id="l_skyfiltsize">
  <dt><b>skyfiltsize = 15</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skyfiltsize' Line='skyfiltsize = 15' -->
  <dd>The sky filter size used in the object detection step.
  </dd>
  </dl>
  <dl id="l_ngrowobj">
  <dt><b>ngrowobj = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ngrowobj' Line='ngrowobj = 0' -->
  <dd>The number of pixels to flag as a buffer around objects detected in the
  object detection step.
  </dd>
  </dl>
  <dl id="l_nrings">
  <dt><b>nrings = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nrings' Line='nrings = 0' -->
  <dd>The cosmic ray growing region half-width in pixels.
  </dd>
  </dl>
  <dl id="l_nsigneg">
  <dt><b>nsigneg = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigneg' Line='nsigneg = 0.0' -->
  <dd>The negative deviant pixel detection threshold in units of sky sigma.
  If nsigneg &lt;= 0.0 negative feature detection is not performed.
  </dd>
  </dl>
  <dl id="l_del_crmask">
  <dt><b>del_crmask = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='del_crmask' Line='del_crmask = no' -->
  <dd>Delete the cosmic ray mask at task termination ? By default the cosmic
  ray masks are stored and used in later processing steps.
  </dd>
  </dl>
  <dl id="l_del_wimages">
  <dt><b>del_wimages = yes, del_wmasks = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='del_wimages' Line='del_wimages = yes, del_wmasks = yes' -->
  <dd>Delete the working images and masks ? By default the working median
  filtered image, the cosmic ray image, and the cosmic ray only image are
  deleted as well as the object detection and negative bad pixel detection
  masks if any. 
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XZAP detects detects and removes cosmics rays from the input images
  <i>inlist</i> and writes the corrected images to <i>outlist</i>. The output
  image list may be the same as the input image list. If input object
  masks <i>omasks</i> is defined then only cosmic rays in sky regions are
  detected and removed. These object mask consist of 0's and 1's with 0's
  defining the object regions in contrast to the usual XDIMSUM convention.
  The output cosmic ray mask are written to <i>crmasks</i>. Cosmic
  ray masks consist of 1's and 0's with 1's defining the detected cosmic rays.
  </p>
  <p>
  XZAP computes the input image sigma using iterative rejection, pixels
  in the region defined by <i>statsec</i>, and the rejection parameters
  <i>nsigrej</i> and <i>maxiter</i>. The XDIMSUM task ITERSTAT is used to
  compute the sky sigma. More about the ITERSTAT algorithms can be found
  in the ITERSTAT help page.
  </p>
  <p>
  XZAP detects cosmic rays by median filtering the input image using
  a filter size of <i>zboxsz</i> and data limits determined by the minimum
  and maximum image pixel values, and subtracting it from the input image.
  Objects more than <i>nsigzap</i> sky sigma above the background are
  assumed to be cosmic rays. The median filter can be protected against
  deviant values by setting <i>checklimits</i> to yes and <i>zmin</i> and
  <i>zmax</i> to reasonable values.
  </p>
  <p>
  If <i>nsigobj</i> is &gt; 0.0 then the median filtered image is searched for
  objects with pixel values &gt; <i>nsigobj</i> * sky sigma above the background.
  The object detection code uses a smoothing value of 0, an input image
  subsampling factor of <i>subsample</i>, a sky filter size of <i>skyfiltsize</i>
  pixels which applies to the subsampled image not the original image, and an
  object growing size of <i>ngrowobj</i>. Cosmic rays detected in the object
  regions are removed from the cosmic rays masks. The object region mask
  is created with the XDIMSUM task MAKEMASK. More details about MAKEMASK
  can be found in the task help page.
  </p>
  <p>
  If <i>nrings</i> &gt; 0 then XZAP grows the detected cosmic rays to include
  a box 2 * nrings + 1 pixels wide centered on the detected cosmic ray.
  If <i>nsigneg</i> &gt; 0.0 then pixels more than nsigneg * sky sigma below
  background are considered to be cosmic rays and added to the cosmic ray
  mask. Finally if the input object masks defined by <i>omasks</i> exist
  cosmic rays detected in the input object regions are removed from the
  cosmic ray masks.
  </p>
  <p>
  Finally XSLM multiplies the final cosmic ray mask by the input image
  minus the median filtered image to produce a cosmic rays only image
  and subtracts this image from the input image to produce the cosmic ray
  corrected image.
  </p>
  <p>
  If <i>del_crmask</i> = yes the output cosmic ray mask is deleted on task
  termination. If <i>del_wimages</i> = no then the working median filtered,
  cosmic ray ,and cosmic ray only images are saved for later examination. If 
  <i>del_wmasks</i> the working object detection and negative bad pixel
  detection masks are also saved.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Detect cosmic rays in the demo sky subtracted images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type sdemo.list
  demo01.sub.imh
  demo02.sub.imh
  ...
  demo25.sub.imh
  
  cl&gt; xzap @sdemo.list "" @sdemo.list ".crm" nsigrej=5.0 maxiter=10 \
  subsample=2
  </pre></div>
  <p>
  2. Repeat example 1 but specify an output cosmic ray mask list.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xzap @sdemo.list "" @sdemo.list @crmlist nsigrej=5.0 maxiter=10 \
  subsample=2
  </pre></div>
  <p>
  3. Repeat example 1 but set the input object mask list to the image header
     keyword <span style="font-family: monospace;">"CROBJMAS"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xzap @sdemo.list "CROBJMAS" @sdemo.list @crmlist nsigrej=5.0 \
  maxiter=10 subsample=2
  </pre></div>
  <p>
  4. Repeat example 2 but specify an input inverse object core mask list.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xzap @sdemo.list @ocrmlist  @sdemo.list @crmlist nsigrej=5.0 \
  maxiter=10 subsample=2
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
  xnzap, iterstat, fmedian, makemask
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _xnslm:

xnslm: Sky subtract images using running mean
=============================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xnslm inlist omasks nmean outlist
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inlist">
  <dt><b>inlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inlist' Line='inlist' -->
  <dd>The list of input images to be sky subtracted. The input image list is
  assumed to be in order.
  </dd>
  </dl>
  <dl id="l_omasks">
  <dt><b>omasks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='omasks' Line='omasks' -->
  <dd>The list of object masks associated with each input image or the input
  image keyword containing the name of the object mask normally OBJMASK.
  Object masks contain 1's in object regions and 0's elsewhere.
  </dd>
  </dl>
  <dl id="l_nmean">
  <dt><b>nmean</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nmean' Line='nmean' -->
  <dd>The number of neighboring images used to computed the sky image for
  each input image.
  </dd>
  </dl>
  <dl id="l_outlist">
  <dt><b>outlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outlist' Line='outlist' -->
  <dd>The list of output sky subtracted images.
  </dd>
  </dl>
  <dl id="l_hmasks">
  <dt><b>hmasks = <span style="font-family: monospace;">".hom"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hmasks' Line='hmasks = ".hom"' -->
  <dd>The list of output holes masks or the string appended to the output image name
  to create the holes mask name. The holes masks are only created if the
  input object masks are defined, and there is at least one undefined sky image
  pixel. Holes masks contain 0's in undefined sky regions and 1's elsewhere. The
  holes mask is required by later processing steps and is normally not deleted
  on task termination.
  </dd>
  </dl>
  <dl id="l_forcescale">
  <dt><b>forcescale = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='forcescale' Line='forcescale = no' -->
  <dd>Force recalculation of the input image statistics even though they have
  been previously computed and stored in the keyword <span style="font-family: monospace;">"SKYMED"</span>.
  </dd>
  </dl>
  <dl id="l_useomask">
  <dt><b>useomask = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='useomask' Line='useomask = yes' -->
  <dd>Use the input object masks if any to compute the sky statistics  as well as
  create the sky images ?
  </dd>
  </dl>
  <dl id="l_statsec">
  <dt><b>statsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='statsec' Line='statsec = ""' -->
  <dd>The input image section used to compute the sky statistics for each input
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
  <dl id="l_nskymin">
  <dt><b>nskymin = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nskymin' Line='nskymin = 3' -->
  <dd>The minimum number of input images used to compute the sky image.
  </dd>
  </dl>
  <dl id="l_nreject">
  <dt><b>nreject = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nreject' Line='nreject = 1' -->
  <dd>The number of high and low side pixels to reject when computing the sky
  image.
  </dd>
  </dl>
  <dl id="l_cache">
  <dt><b>cache = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cache' Line='cache = yes' -->
  <dd>Enable the caching the input image data in memory ?
  </dd>
  </dl>
  <dl id="l_del_hmasks">
  <dt><b>del_hmasks = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='del_hmasks' Line='del_hmasks = no' -->
  <dd>Delete the holes masks at task termination ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XNSLM computes the average sky image for each image in the input image list
  <i>inlist</i> and subtracts it from the input image to create the output list
  of sky subtracted images <i>outlist</i>. The input image list is assumed to
  be ordered by time of observation. If the input object masks list
  <i>omasks</i> is defined then input image pixels in object regions are 
  removed from the sky image computation. XSLM also creates a list of holes masks
  <i>hmasks</i>.
  </p>
  <p>
  XNSLM estimates the median for each input image using iterative rejection
  around the mean, pixels in the region defined by <i>statsec</i>, and the
  bad pixel rejection parameters <i>nsigrej</i> and <i>maxiter</i>. If 
  <i>useomask</i> = yes and an object mask is defined for the input image,
  then pixels in object regions are also rejected from the sky statistics
  computation. The reciprocal of the median value is stored in the
  keyword <span style="font-family: monospace;">"SKYMED"</span>. New sky statistics are computed if <i>forcescale</i> is
  yes or if the SKYMED keyword is undefined. The XRSKYSUB task is used to
  compute the image statistics.
  </p>
  <p>
  XNSLM computes the sky image for each input image by multiplying each
  input image by the value of the SKYMED keyword, and then computing the 
  mean of the <i>nmean</i> neighbor images after rejecting the <i>nreject</i>
  high and low pixels. For example if the number of input images is 25 and
  nmean is 6 then images 2-4 are used to compute the sky image for image 1,
  images 10-12 and 14-16 are used to compute the sky for image 13, and images
  22-24 are used to compute the sky image for image 25. There must be a minimum
  of <i>nskymin</i> neighbor images or the sky image will not be computed. If the
  input object masks are defined then pixels in object regions are also rejected
  from the sky image computation. The XRSKYSUUB task is used to compute and
  subtract the sky images.
  </p>
  <p>
  After the sky image is computed XNSLM divides it into the input image
  and computes the median of the ratio image. The final sky subtracted image
  is computing by multiplying the sky image by the median of the ratio image
  and subtracting it from the input image. The XRSKYSUB task does this as well.
  More about XRSKYSUB can be found in the appropriate help page.
  </p>
  <p>
  If input image masking is enabled then it is possible for pixels in the
  sky image and the output sky subtracted image to be undefined. If at least
  one such pixel is undefined in the output image then XNSLM creates a 
  holes mask <i>hmasks</i>. The holes masks are used by the XMSKCOMBINE
  task tp create a combined mask for the XNREGISTAR tas.
  </p>
  <p>
  If <i>cache</i> is yes then XNSLM will attempt to cache image in memory as
  needed. This can significantly speed up the statisticis computation
  and the image combining step.
  </p>
  <p>
  If <i>del_hmasks</i> is enabled then the holes masks are deleted at task
  termination.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Sky subtract the demo images with  object masking.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type demo.list
  demo01
  demo01
  ...
  demo25
  
  cl&gt; xnslm @demo.list "" 6 ".sub" nsigrej=5.0 maxiter=10
  
  cl&gt; dir *.sub.imh
  demo01.sub.imh
  demo01.sub.imh
  ...
  demo25.sub.imh
  </pre></div>
  <p>
  2. Repeat the previous example but specify an output image list.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xnslm @demo.list "" 6 @outlist  nsigrej=5.0 maxiter=10
  </pre></div>
  <p>
  3. Repeat example 1 with object masking assuming that the object
  mask names are stored in the keyword <span style="font-family: monospace;">"OBJMASK"</span>
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xnslm @demo.list "OBJMASK" 6 ".sub"  nsigrej=5.0 maxiter=10
  </pre></div>
  <p>
  4. Repeat example 2 with object masking assuming that the object
  mask names are stored in the image list objmasks.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xnslm @demo.list @objmasks 6 @outlist nsigrej=5.0 maxiter=10
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
  xslm
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

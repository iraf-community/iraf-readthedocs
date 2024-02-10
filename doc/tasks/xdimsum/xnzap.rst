.. _xnzap:

xnzap: Remove cosmis rays from images using averaging filter
============================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xnzap inlist omasks outlist crmasks
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
  <dd>The list of input object masks used to unzap cosmic rays detected in object
  regions or the input image keyword containing the name of the object mask,
  normally <span style="font-family: monospace;">"CROBJMAS"</span>. Object masks contain 0's in object regions and 1's
  elsewhere. Note that this is the inverse of the usual definition of
  an XDIMSUM object mask.
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
  <dd>The name of the output cosmic ray masks or the string appended to the
  output image name to create the output cosmic ray mask name. Cosmic ray masks
  contain 1's in cosmic ray regions and 0's elsewhere. The name of the output
  cosmic ray mask is stored in the input and output image header keyword CRMASK.
  </dd>
  </dl>
  <dl id="l_zboxsz">
  <dt><b>zboxsz = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zboxsz' Line='zboxsz = 5' -->
  <dd>The size in pixels of the moving average filter. The central pixel
  plus <i>nrejzap</i> pixels are rejected from the average.
  </dd>
  </dl>
  <dl id="l_skyfiltsize">
  <dt><b>skyfiltsize = 15</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skyfiltsize' Line='skyfiltsize = 15' -->
  <dd>The sky filter size in pixels. For each point the median of the pixels in
  an annulus of width (<i>skyfiltsize</i> - <i>zboxsz</i>) / 2 pixels is used
  to estimate the local background.
  </dd>
  </dl>
  <dl id="l_sigfiltsize">
  <dt><b>sigfiltsize = 25</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigfiltsize' Line='sigfiltsize = 25' -->
  <dd>Size of box used for local background sigma estimates. The sigma filter
  is not a moving filter. Sigmas are estimated using percentile points of
  of the pixels in the box.
  </dd>
  </dl>
  <dl id="l_nsigzap">
  <dt><b>nsigzap = 5.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigzap' Line='nsigzap = 5.0' -->
  <dd>The cosmic ray detection threshold in units of sky sigma.
  </dd>
  </dl>
  <dl id="l_nsigneg">
  <dt><b>nsigneg = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigneg' Line='nsigneg = 0.0' -->
  <dd>The negative deviant pixel detection threshold in units of sky sigma.
  If nsigneg &lt;= 0.0 negative feature detection is not enabled.
  </dd>
  </dl>
  <dl id="l_nrings">
  <dt><b>nrings = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nrings' Line='nrings = 0' -->
  <dd>The cosmic ray growing region half-width in pixels.
  </dd>
  </dl>
  <dl id="l_nsigobj">
  <dt><b>nsigobj = 2.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigobj' Line='nsigobj = 2.0' -->
  <dd>The object detection threshold in units of sky sigma. If nsigobj &lt;= 0.0
  only cosmic ray detection is performed.
  </dd>
  </dl>
  <dl id="l_ngrowobj">
  <dt><b>ngrowobj = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ngrowobj' Line='ngrowobj = 0' -->
  <dd>The number of pixels to flag as a buffer around objects detected in the
  object detection step.
  </dd>
  </dl>
  <dl id="l_del_crmask">
  <dt><b>del_crmask = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='del_crmask' Line='del_crmask = no' -->
  <dd>Delete the cosmic ray mask at task termination ? By default the cosmic
  ray masks are stored and used in later processing steps.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print messages about actions taken by the task ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XNZAP detects detects and removes cosmics rays from the input images
  <i>inlist</i> and writes the corrected images to <i>outlist</i>. The output
  image list may be the same as the input image list. If input object
  masks <i>omasks</i> are defined then only cosmic rays in sky regions are
  detected and removed. These object mask consist of 0's and 1's with 0's
  defining the object regions in contrast to the usual XDIMSUM convention.
  The output cosmic rays mask are written to <i>crmasks</i>. Cosmic
  ray masks consist of 1's and 0's with 1's defining the detected cosmic rays.
  </p>
  <p>
  At each pixel position XNZAP computes a running average filter of size
  <i>zboxsz</i> excluding the central pixel and the <i>nrejzap</i> highest
  pixels from the average, and a running median in an annulus (<i>skyfiltsize</i>
  - <i>zboxsz</i>) / 2 pixels wide. The local sky sigmas are estimated by dividing
  the image into square blocks which are <i>sigfiltsize</i> pixels wide and
  estimating the percentile points of pixels in the box.
  </p>
  <p>
  A pixel is considered part of an object if the difference between the average
  value and the median background &gt; <i>nsigobj</i> times the background sigma.
  If nsigobj &lt;= 0 then no object detection is performed. If the pixel is NOT
  considered to be part of an object and if the difference between the pixel
  value and the average value exceeds <i>nsigzap</i> times the background sigma
  it is identified as a cosmic ray.  If <i>nsigneg</i> &gt; 0.0 then pixels more
  than nsigneg times the background sigma are also considered to be cosmic
  rays and are added to the cosmic ray mask.
  </p>
  <p>
  If <i>nrings</i> &gt; 0 then XNZAP grows the detected cosmic rays to include
  pixels within a radius of nrings pixels of the detected cosmic ray.
  If <i>nobjgrow</i> is &gt; 0 then the detected object regions are grown to
  include pixels with a radius of nobjgrow pixels of the target object.
  The output cosmic ray mask is not affected by the region growing parameters
  however.
  </p>
  <p>
  XNZAP is a new cosmic ray detection program which can be used as an alternative
  to XZAP. It uses the CRAVERAGE task to detect and remove cosmic rays. Normally
  CRAVERAGE is part of the addon CRUTIL package but a private copy has been
  installed in XDIMSUM. Users can find out more about CRAVERAGE by consulting
  the CRAVERAGE help page.
  </p>
  <p>
  If <i>del_crmask</i> = yes the output cosmic ray mask is deleted on task
  termination
  </p>
  <p>
  If <i>verbose</i> = yes then XNZAP prints messages on the terminal about
  the progress of the task.
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
  
  cl&gt; xnzap @sdemo.list "" @sdemo.list ".crm"
  </pre></div>
  <p>
  2. Repeat example 1 but specify an output cosmic ray mask list.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xnzap @sdemo.list "" @sdemo.list @crmlist
  </pre></div>
  <p>
  3. Repeat example 1 but specify an input inverse object core mask using
  the keyword <span style="font-family: monospace;">"CROBJMAS"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xnzap @sdemo.list "CROBJMAS" @sdemo.list ".crm"
  </pre></div>
  <p>
  4. Repeat example 2 but specify the input inverse object core mask list.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xnzap @sdemo.list @ocrmlist @sdemo.list @crmlist
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
  xzap, craverage
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

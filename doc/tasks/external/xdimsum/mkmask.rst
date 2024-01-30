.. _mkmask:

mkmask: Create the initial master object mask
=============================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkmask input expmap output nthreshold
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The input image name. The input image is assumed but not required to be a
  mosaic of several input images.
  </dd>
  </dl>
  <dl id="l_expmap">
  <dt><b>expmap</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expmap' Line='expmap' -->
  <dd>The input exposure map image which defines the total expsoure per pixel.
  Expmap is used normalize the input image to uniform pixel-to-pixel noise.
  If the exposure map is undefined then a uniform exposure level for all
  the pixels is assumed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The name of the output object mask.
  </dd>
  </dl>
  <dl id="l_nthreshold">
  <dt><b>nthreshold</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nthreshold' Line='nthreshold' -->
  <dd>If interactive = no then the object detection threshold used to create the
  object mask equals nthreshold times the internally computed recommended
  threshold.
  </dd>
  </dl>
  <dl id="l_negthresh">
  <dt><b>negthresh = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='negthresh' Line='negthresh = no' -->
  <dd>Use negative as well as positive masking thresholds ?
  </dd>
  </dl>
  <dl id="l_statsec">
  <dt><b>statsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='statsec' Line='statsec = ""' -->
  <dd>The input image section used to compute the recommended object detection
  threshold.
  </dd>
  </dl>
  <dl id="l_nsigrej">
  <dt><b>nsigrej = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigrej' Line='nsigrej = 3.0' -->
  <dd>The bad pixel rejection criterion used to compute the recommended object
  detection threshold.
  </dd>
  </dl>
  <dl id="l_maxiter">
  <dt><b>maxiter = 20</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxiter' Line='maxiter = 20' -->
  <dd>The maximum number of bad pixel rejection iterations used to compute the
  recommended object detection threshold.
  </dd>
  </dl>
  <dl id="l_subsample">
  <dt><b>subsample = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subsample' Line='subsample = 1' -->
  <dd>The block averaging factor applied to the normalized input image before median
  filtering.
  </dd>
  </dl>
  <dl id="l_filtsize">
  <dt><b>filtsize = 15</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filtsize' Line='filtsize = 15' -->
  <dd>The size of the median filter. The effective size of the median filter
  is <i>subsample</i> * filtsize.
  </dd>
  </dl>
  <dl id="l_nsmooth">
  <dt><b>nsmooth = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsmooth' Line='nsmooth = 3' -->
  <dd>The size of the boxcar smoothing filter applied to the median filtered image.
  </dd>
  </dl>
  <dl id="l_ngrow">
  <dt><b>ngrow = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ngrow' Line='ngrow = 0' -->
  <dd>The half_width of the region growing box. 
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Set the value of the object detection threshold interactively ?
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold' -->
  <dd>The value of threshold if interactive is yes.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MKMASK creates an object mask called <i>output</i> for the
  input image <i>input</i> using an optional exposure map <i>expmap</i> and an
  object detection threshold set by the user if <i>interactive</i> is yes or
  equal to <i>nthreshold</i> times an internally computed recommeded number if
  <i>interactive</i> is no.
  </p>
  <p>
  MKMASK normalizes the input image to a uniform pixel-to-pixel rms by 
  multiplying by a factor of sqrt (expmap / maxexpmap) where maxexpmap is the
  maximum exposure level in the exposure map.
  </p>
  <p>
  The standard deviation of the normalized input image pixels is computed using
  pixels in <i>statsec</i> and iterative rejection  with rejection parameters of
  <i>nsigrej</i> and <i>maxiter</i>. Pixels with 0's in the exposure map are
  excluded from the image statistics computation. If the exposure map is
  undefined then a uniform exposure level is assumed.
  </p>
  <p>
  If <i>interactive</i> = yes the user is prompted for the detection threshold
  <i>threshold</i>. If interactive = no the detection threshold is set to
  <i>nthreshold</i> * the recommended threshold where the recommended threshold
  is defined to be
  </p>
  <div class="highlight-default-notranslate"><pre>
  recthreshold = 4.5 * sigma / nsmooth
  </pre></div>
  <p>
  Sigma is the standard deviation of the sky pixels. If <i>negthresh</i>
  is set to <span style="font-family: monospace;">"yes"</span> then both negative and positive masking threshold are used.  
  </p>
  <p>
  Before median filtering the normalized input image is block-averaged by a
  factor of <i>subsample</i>. The size of the median filter <i>filtsize</i>
  refers to the block-averaged image. Therefore the effective size of
  the median filter is actually subsample * filtsize. After median filtering
  but before thresholding the image block-replicated to its original
  size and is smoothed using a boxcar filter of size <i>nsmooth</i>. 
  </p>
  <p>
  The filtered and smoothed image pixels greater than or equal to the detection
  threshold are set to 1 in the output object mask. The remaining pixels are set
  to 0. If <i>ngrow</i> &gt; 0  pixels within a box of half-width ngrow pixels
  are assumed to be object pixels.
  </p>
  <p>
  The actual mask creation is done by the MAKEMASK task. More information
  on MAKEMASK can be found in the task help page.
  </p>
  <p>
  If <i>interactive</i> is yes then the final object mask is displayed on the
  image display.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create the object mask for the combined image created with xnregistar.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkmask mosaic mosaic.exp mosaic.pl 1.1 statsec="" nsigrej=5.0 \
      maxiter=10 nsmooth=3 subsample=2 filtsize=15 ngrow=0 interactive-
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
  makemask, blkavg, fmedian, boxcar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

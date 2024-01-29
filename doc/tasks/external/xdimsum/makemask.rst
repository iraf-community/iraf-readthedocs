.. _makemask:

makemask: Make an object mask for a single image
================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  makemask inlist outlist
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inlist">
  <dt><b>inlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inlist' Line='inlist' -->
  <dd>The list of input images for which object masks are to be created.
  </dd>
  </dl>
  <dl id="l_outlist">
  <dt><b>outlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outlist' Line='outlist' -->
  <dd>The list of output masks. The number output masks must be the same as the
  number of input images. list of output masks. The number output masks must
  be the same as the number of input images.
  </dd>
  </dl>
  <dl id="l_hinlist">
  <dt><b>hinlist = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hinlist' Line='hinlist = ""' -->
  <dd>The list of images to which BPM keywords containing the name of the output
  maks are to be added. Hinlist may be the same as or different from inlist.
  </dd>
  </dl>
  <dl id="l_subsample">
  <dt><b>subsample = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subsample' Line='subsample = 1' -->
  <dd>The block averaging factor applied to the input image before median filtering.
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
  <dt><b>zmin = -32767, zmax = 32767</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zmin' Line='zmin = -32767, zmax = 32767' -->
  <dd>The default data limits supplied to the fast median filter if
  <i>checklimits</i> is yes.
  </dd>
  </dl>
  <dl id="l_filtsize">
  <dt><b>filtsize = 15</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filtsize' Line='filtsize = 15' -->
  <dd>The size of the fast median filter used to determine the background. The
  effective size of the median filter is <i>subsample</i> * filtsize.
  </dd>
  </dl>
  <dl id="l_nsmooth">
  <dt><b>nsmooth = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsmooth' Line='nsmooth = 3' -->
  <dd>The size of the boxcar smoothing filter applied to the median filtered image.
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
  <dl id="l_threshtype">
  <dt><b>threshtype = <span style="font-family: monospace;">"nsigma"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshtype' Line='threshtype = "nsigma"' -->
  <dd>The threshold setting algorithm. The options are <span style="font-family: monospace;">"nsigma"</span> and <span style="font-family: monospace;">"constant"</span>.
  <dl>
  <dt><b>nsigma</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nsigma' Line='nsigma' -->
  <dd>Set the threshold to the background sky value plus the value of <i>nsigthresh\R
   * the sky background sigma.
  </dd>
  </dl>
  <dl>
  <dt><b>constant</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='constant' Line='constant' -->
  <dd>Set the threshold to the background sky value plus the value of
  fIconstthresh</i>.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_nsigthresh">
  <dt><b>nsigthresh = 2.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigthresh' Line='nsigthresh = 2.0' -->
  <dd>The number of sky background sigma used to defined the threshold value for
  background detection.
  </dd>
  </dl>
  <dl id="l_constthresh">
  <dt><b>constthresh = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constthresh' Line='constthresh = 0.0' -->
  <dd>The constant threshold value
  </dd>
  </dl>
  <dl id="l_negthresh">
  <dt><b>negthresh = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='negthresh' Line='negthresh = no' -->
  <dd>Set a negative as well as a positive masking threshold ?
  </dd>
  </dl>
  <dl id="l_ngrow">
  <dt><b>ngrow = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ngrow' Line='ngrow = 0' -->
  <dd>The half_width of the region growing box. Only positive features are subject
  to region growing.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print messages about the progress of the task.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MAKEMASK creates object masks called <i>outlist</i> for the
  input images <i>inlist</i> using a median filtering and thresholding technique.
  If <i>hinlist</i> is defined the output object mask names are written to image
  header BPM keyword. Hinlist does not have to be the same as <i>inlist</i>.
  </p>
  <p>
  Before median filtering the normalized input image is block-averaged by a
  factor of <i>subsample</i>. The size of the median filter <i>filtsize</i>
  refers to the block-averaged image. Therefore the effective size of
  the median filter is actually subsample * filtsize. The median filter can be
  protected against deviant values by setting <i>checklimits</i> to yes and
  <i>zmin</i> and <i>zmax</i> to reasonable values. If <i>filtsize</i> &lt; 1 then
  no block averaging, median filtering, or block replication is done.
  </p>
  <p>
  The median value of the input image pixels is computed using pixels in
  <i>statsec</i> and iterative rejection  with rejection parameters of
  <i>nsigrej</i> and <i>maxiter</i>.
  </p>
  <p>
  After the image statistics computation but before thresholding the image 
  is smoothed using a boxcar filter of size <i>nsmooth</i>. 
  </p>
  <p>
  If <i>threshtype</i> = <span style="font-family: monospace;">"nsigma"</span> the threshold value is set to
  </p>
  <div class="highlight-default-notranslate"><pre>
  pthreshold = median + <i>nsigthresh</i> * sigma / <i>nsmooth</i>
  if (negthresh)
      nthreshold = median - <i>nsigthresh</i> * sigma / <i>nsmooth</i>
  else
      nthreshold = -1.0e37
  </pre></div>
  <p>
  otherwise it is set to 
  </p>
  <div class="highlight-default-notranslate"><pre>
  pthreshold = median + <i>constthresh</i>
  if (negthresh)
      nthreshold = median - <i>constthresh</i>
  else
      nthreshold = -1.0e37
  </pre></div>
  <p>
  The image pixels greater than or or less than the detection threshold are set to
  1 in the output object mask. The remaining pixels are set to 0. If <i>ngrow</i>
  &gt; 0  pixels within a box of half-width <i>ngrow</i> pixels around positive
  <span style="font-family: monospace;">"objects"</span> are assumed to be object pixels.
  </p>
  <p>
  If <i>verbose R= yes then detailed messages about the progress of the task
  are printed on the screen.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create object masks for a list of sky subtracted images
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type imlist
  demo01.sub
  demo02.sub
  ...
  demo25.sub
  
  cl&gt; type outlist
  demo01.sub.msk
  demo02.sub.msk
  ...
  demo25.sub.msk
  
  cl&gt; makemask @imlist @outlist nsigrej=5.0 maxiter=10
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
  mkmask, blkavg, fmedian, boxcar, imexpr
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

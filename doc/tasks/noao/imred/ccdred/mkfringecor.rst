.. _mkfringecor:

mkfringecor: Make fringe correction images from sky images
==========================================================

**Package: ccdred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkfringecor input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images for making fringe correction images.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output fringe correction images.  If none is
  specified or if the name is the same as the input image then the output
  image replaces the input image.
  </dd>
  </dl>
  <dl id="l_ccdtype">
  <dt><b>ccdtype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdtype' Line='ccdtype = ""' -->
  <dd>CCD image type to select from the input images.  If none is specified
  then all types are used.
  </dd>
  </dl>
  <dl id="l_xboxmin">
  <dt><b>xboxmin = 5, xboxmax = 0.25, yboxmin = 5, yboxmax = 0.25</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xboxmin' Line='xboxmin = 5, xboxmax = 0.25, yboxmin = 5, yboxmax = 0.25' -->
  <dd>Minimum and maximum smoothing box size along the x and y axes.  The
  minimum box size is used at the edges and grows to the maximum size in
  the middle of the image.  This allows the smoothed image to better
  represent gradients at the edge of the image.  If a size is less then 1
  then it is interpreted as a fraction of the image size.  If a size is
  greater than or equal to 1 then it is the box size in pixels.  A size
  greater than the size of image selects a box equal to the size of the
  image.
  </dd>
  </dl>
  <dl id="l_clip">
  <dt><b>clip = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clip' Line='clip = yes' -->
  <dd>Clean the input images of objects?  If yes then a clipping algorithm is
  used to detect and exclude objects from the smoothing.
  </dd>
  </dl>
  <dl id="l_lowsigma">
  <dt><b>lowsigma = 2.5, highsigma = 2.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lowsigma' Line='lowsigma = 2.5, highsigma = 2.5' -->
  <dd>Sigma clipping thresholds above and below the smoothed background.
  </dd>
  </dl>
  <dl id="l_ccdproc">
  <dt><b>ccdproc (parameter set)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdproc' Line='ccdproc (parameter set)' -->
  <dd>CCD processing parameters.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The input blank sky images are automatically processed up through the
  iillumination correction before computing the fringe correction images.
  The fringe corrections are subset dependent.
  The slowly varying background is determined and subtracted leaving only
  the fringe pattern caused by the sky emission lines.  These fringe images
  are then scaled and subtracted from the observations by <b>ccdproc</b>.
  The background is determined by heavily smoothing the image using a
  moving <span style="font-family: monospace;">"boxcar"</span> average.  The effects of the objects and fringes in the
  image is minimized by using a sigma clipping algorithm to detect and
  exclude them from the average.  Note, however, that objects left in the
  fringe image will affect the fringe corrected observations.  Any objects
  in the sky image should be removed using <b>skyreplace</b> (not yet
  available).
  </p>
  <p>
  The smoothing algorithm is a moving average over a two dimensional
  box.  The algorithm is unconvential in that the box size is not fixed.
  The box size is increased from the specified minimum at the edges to
  the maximum in the middle of the image.  This permits a better estimate
  of the background at the edges, while retaining the very large scale
  smoothing in the center of the image.  Note that the sophisticated
  tools of the <b>images</b> package may be used for smoothing but this
  requires more of the user and, for the more sophisticated smoothing
  algorithms such as surface fitting, more processing time.
  </p>
  <p>
  To minimize the effects of the fringes and any objects in the blank sky
  calibration images a sigma clipping algorithm is used to detect and
  exclude features from the background.  This is done by computing the
  rms of the image lines relative to the smoothed background and
  excluding points exceeding the specified threshold factors times the
  rms.  This is done before each image line is added to the moving
  average, except for the first few lines where an iterative process is
  used.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. The two examples below make an fringe correction image from a blank
  sky image, <span style="font-family: monospace;">"sky017"</span>.  In the first example a separate fringe
  image is created and in the second the fringe image replaces the
  sky image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkskycor sky017 Fringe
  cl&gt; mkskycor sky017 frg017
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ccdproc
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

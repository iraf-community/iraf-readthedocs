.. _mkillumflat:

mkillumflat: Make illumination corrected flat fields
====================================================

**Package: quadred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkillumflat input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input flat field images to be illumination corrected.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output illumination corrected flat field images.
  If none is specified or if the name is the same as the
  input image then the output image replaces the input image.
  </dd>
  </dl>
  <dl id="l_ccdtype">
  <dt><b>ccdtype = <span style="font-family: monospace;">"flat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdtype' Line='ccdtype = "flat"' -->
  <dd>CCD image type to select from the input images.
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
  <dd>Sigma clipping thresholds above and below the smoothed illumination.
  </dd>
  </dl>
  <dl id="l_divbyzero">
  <dt><b>divbyzero = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='divbyzero' Line='divbyzero = 1.' -->
  <dd>The illumination flat field is the ratio of the flat field to a
  smoothed flat field.  This may produce division by zero.  A warning is
  given if division by zero takes place and the result (the illumination
  corrected flat field value) is replaced by the value of this
  parameter.
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
  First, the input flat field images are processed as needed.  Then the
  large scale illumination pattern of the images is removed.  The
  illumination pattern is determined by heavily smoothing the image using
  a moving <span style="font-family: monospace;">"boxcar"</span> average.  The output image is the ratio of the input
  image to the illumination pattern.  The illumination pattern is
  normalized by its mean to preserve the mean level of the input image.
  </p>
  <p>
  When this task is applied to flat field images only the small scale
  response effects are retained.  This is appropriate if the flat field
  images have illumination effects which differ from the astronomical
  images and blank sky images are not available for creating sky
  corrected flat fields.  When a high quality blank sky image is
  available the related task <b>mkskyflat</b> should be used.  Note that
  the illumination correction, whether from the flat field or a sky
  image, may be applied as a separate step by using the task
  <b>mkillumcor</b> or <b>mkskycor</b> and applying the illumination
  correction as a separate operation in <b>ccdproc</b>.  However, creating
  an illumination corrected flat field image before processing is more
  efficient since one less operation per image processed is needed.  For
  more discussion about flat fields and illumination corrections see
  <b>flatfields</b>.
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
  To minimize the effects of bad pixels a sigma clipping algorithm is
  used to detect and reject these pixels from the illumination.  This is
  done by computing the rms of the image lines relative to the smoothed
  illumination and excluding points exceeding the specified threshold
  factors times the rms.  This is done before each image line is added to
  the moving average, except for the first few lines where an iterative
  process is used.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Two examples in which a new image is created and in which the
  input flat fields are corrected in place are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkllumflat flat004 FlatV
  cl&gt; mkillumflat flat* ""
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ccdproc, flatfields, mkfringecor, mkillumcor, mkskycor, mkskyflat
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

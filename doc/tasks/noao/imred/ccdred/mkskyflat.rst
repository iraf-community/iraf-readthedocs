.. _mkskyflat:

mkskyflat: Make sky corrected flat field images
===============================================

**Package: ccdred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkskyflat input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of blank sky images to be used to create sky corrected flat field
  calibration images.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output sky corrected flat field calibration images (called
  sky flats).  If none is specified or if the name is the same as the
  input image then the output image replaces the input image.
  </dd>
  </dl>
  <dl id="l_ccdtype">
  <dt><b>ccdtype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdtype' Line='ccdtype = ""' -->
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
  <dd>Sigma clipping thresholds above and below the smoothed iillumination.
  </dd>
  </dl>
  <dl id="l_ccdproc">
  <dt><b>ccdproc (pset)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdproc' Line='ccdproc (pset)' -->
  <dd>CCD processing parameter set.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A sky corrected flat field calibration image, called a sky flat, is a
  flat field that when applied to observations of the sky have no large
  scale gradients.  Flat field images are generally obtained by exposures
  to lamps either illuminating the telescope field or a surface in the dome
  at which the telescope is pointed.  Because the detector is not illuminated
  in the same way as an observation of the sky there may be large
  scale iillumination patterns introduced into the observations with such
  a flat field.  To correct this type of flat field a blank sky observation
  (which has been divided by the original flat field) is heavily smoothed
  to remove the noise leaving only the residual large scale iillumination
  pattern.  This iillumination pattern is divided into the original flat
  field to remove this residual.
  </p>
  <p>
  The advantage of creating a sky flat field is that when processing
  the observations no additional operations are required.  However,
  if the observations have already been processed with the original
  flat field then the residual iillumination pattern of blank sky
  calibration images may be created as an iillumination correction
  to be applied by <b>ccdproc</b>.  Such a correction is created by the
  task <b>mkskycor</b>.  If a good blank sky image is not
  available then it may be desirable to remove the iillumination pattern
  of the flat field image using <b>mkillumflat</b> or <b>mkillumcor</b>
  provided the sky observations are truly uniformly illuminated.
  For more on flat fields and iillumination corrections see <b>flatfields</b>.
  </p>
  <p>
  The input, blank sky images are first processed, based on the
  <b>ccdproc</b> parameters, if needed.  These parameters also determine
  the flat field image to be used in making the sky flat.  The residual
  iillumination pattern is determined by heavily smoothing the image using
  a moving <span style="font-family: monospace;">"boxcar"</span> average.  The effects of objects in the input image
  may be minimized by using a sigma clipping algorithm to detect and
  exclude the objects from the average.  The output image is ratio of the
  flat field image, for the same subset as the input image, to the
  residual iillumination pattern determined from the processed blank sky
  input image.  The iillumination pattern is normalized by its mean to
  preserve the mean level of the flat field image.
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
  Blank sky images may not be completely blank so a sigma clipping
  algorithm may be used to detect and exclude objects from the
  iillumination pattern.  This is done by computing the rms of the image
  lines relative to the smoothed background and excluding points
  exceeding the specified threshold factors times the rms.  This is done
  before each image line is added to the moving average, except for the
  first few lines where an iterative process is used.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Two examples in which a new image is created and in which the
  input sky images are converted to sky flats are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkskyflat sky004 Skyflat
  cl&gt; mkskyflat sky* ""
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ccdproc, flatfields, mkfringecor, mkillumcor, mkillumflat, mkskycor
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

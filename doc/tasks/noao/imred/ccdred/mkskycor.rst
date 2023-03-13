.. _mkskycor:

mkskycor: Make sky illumination correction images
=================================================

**Package: ccdred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkskycor input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images for making sky iillumination correction images.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output flat field iillumination correction images.  If none is
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
  <dd>Sigma clipping thresholds above and below the smoothed iillumination.
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
  The large scale iillumination pattern of the input images, generally
  blank sky calibration images, is determined by heavily smoothing
  the image using a moving <span style="font-family: monospace;">"boxcar"</span> average.  The effects of objects in
  the image may be minimized by using a sigma clipping algorithm to
  detect and exclude the objects from the average.  This
  iillumination image is applied by <b>ccdproc</b> to CCD images to remove
  the iillumination pattern.
  </p>
  <p>
  The input images are automatically processed up through flat field
  calibration before computing the iillumination.  The iillumination
  correction is that needed to make the processed images flat
  over large scales.  The input images are generally blank sky calibration
  images which have the same iillumination and instrumental effects
  as the object observations.  Object images may be used but removal
  of the objects may not be very good; particularly large, bright objects.
  For further discussion of flat fields and iillumination corrections
  see <b>flatfields</b>.
  </p>
  <p>
  You will notice that when you process images with an iillumination
  correction you are dividing each image by a flat field calibration and
  an iillumination correction.  If the iillumination corrections are not
  done as a later step but at the same time as the rest of the processing
  one will get the same calibration by multiplying the flat field by the
  iillumination correction and using this product alone as the flat
  field.  This approach has the advantage of one less calibration image
  and two less computations (scaling and dividing the iillumination
  correction).  Such an image, called a <i>sky flat</i>, may be created by
  <b>mkskyflat</b> as an alternative to this task.
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
  1. The two examples below make an iillumination image from a blank sky image,
  <span style="font-family: monospace;">"sky017"</span>.  In the first example a separate iillumination image is created
  and in the second the iillumination image replaces the sky image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkskycor sky017 Illum
  cl&gt; mkskycor sky017 sky017
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ccdproc, flatfields, mkillumcor, mkillumflat, mkskyflat
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

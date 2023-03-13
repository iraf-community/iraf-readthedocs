.. _craverage:

craverage: Detect CRs against average and avoid objects
=======================================================

**Package: crutil**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  <b>Craverage</b> detects cosmic rays and objects using a moving block
  average filter with the central pixel plus some number of additional high
  pixels  excluded and a median of an annulus around the block average box.
  It avoids identification of the cores of objects as cosmic rays by
  excluding pixels within the detected objects as cosmic ray candidates.
  </p>
  </section>
  <section id="s_usage___">
  <h3>Usage   </h3>
  <div class="highlight-default-notranslate"><pre>
  craverage input output
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images in which to detect cosmic rays and objects.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output images in which cosmic rays are replaced by the block average
  value excluding the cosmic ray.  If no output image name is given then
  no output image will be created.
  </dd>
  </dl>
  <dl id="l_crmask">
  <dt><b>crmask = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crmask' Line='crmask = ""' -->
  <dd>List of input and output cosmic ray and object masks.  If the mask exists
  then the mask values are used to exclude data pixels from the calculations
  and zero mask values are candidates for cosmic rays or objects.
  Detected cosmic rays and objects are identified in the mask with values
  given by the <i>crval</i> and <i>objval</i> parameters.  If no output cosmic
  ray mask is given then no mask will be created.
  </dd>
  </dl>
  <dl id="l_average">
  <dt><b>average = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='average' Line='average = ""' -->
  <dd>List of output block average filtered images.  If no image name is given
  then no image will be created.
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma' Line='sigma = ""' -->
  <dd>List of output sigma images.  If no image name is given then no image
  will be created.
  </dd>
  </dl>
  <dl id="l_navg">
  <dt><b>navg = 5 (minimum of 3)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='navg' Line='navg = 5 (minimum of 3)' -->
  <dd>Square block average filter size given as the number of pixels along an
  edge.  The value will be rounded up to an odd value to be symmetrical
  around the center pixel excluded from the average.
  </dd>
  </dl>
  <dl id="l_nrej">
  <dt><b>nrej = 0 (minimum of 0)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nrej' Line='nrej = 0 (minimum of 0)' -->
  <dd>Number of additional highest pixels to exclude, in addition to the
  central pixel, in the block average.  The value should be small but it
  is needed to deal with cosmic rays that are bigger than a single pixel.
  </dd>
  </dl>
  <dl id="l_nbkg">
  <dt><b>nbkg = 5 (minimum of 1)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nbkg' Line='nbkg = 5 (minimum of 1)' -->
  <dd>Background annulus width around the box average filter in pixels.  The
  median of the pixels in this annulus is used to estimate the background.
  </dd>
  </dl>
  <dl id="l_nsig">
  <dt><b>nsig = 25 (minimum of 10)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsig' Line='nsig = 25 (minimum of 10)' -->
  <dd>Square box size for empirical sigma estimates given as the number of
  pixels along an edge.  The sigma is estimated using percentile points
  of the pixels in the box.  The size of the box should contain
  of order 100 pixels or more.
  </dd>
  </dl>
  <dl id="l_var0">
  <dt><b>var0 = 0., var1 = 0., var2 = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='var0' Line='var0 = 0., var1 = 0., var2 = 0.' -->
  <dd>Variance coefficients for the variance model.  The variance model is
  <div class="highlight-default-notranslate"><pre>
  variance = var0 + var1 * data + var2 * data^2
  </pre></div>
  where data is the maximum of zero and the average filtered pixel value and
  the variance is in data numbers.  All the coefficients must be positive or
  zero.  If they are all zero then empirical data sigmas are estimated by a
  percentile method in boxes of size given by <i>nsig</i>.
  </dd>
  </dl>
  <dl id="l_crval">
  <dt><b>crval = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crval' Line='crval = 1' -->
  <dd>Mask value for detected cosmic rays.  It is legal for the value to be
  zero to not mark the cosmic rays in the output mask.
  </dd>
  </dl>
  <dl id="l_lcrsig">
  <dt><b>lcrsig = 10., hcrsig = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lcrsig' Line='lcrsig = 10., hcrsig = 5.' -->
  <dd>Low and high sigma factors for detecting cosmic rays.  These factors
  multiply the computed or estimated sigma at each pixel and these threshold
  values are compared to the difference between the candidate pixel and the
  block average filter value (average of box around the pixel).  This only
  applies to pixels where the block average filter value is within a
  specified threshold of the background estimate; i.e. the average value is
  not considered as part of an object.
  </dd>
  </dl>
  <dl id="l_crgrow">
  <dt><b>crgrow = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crgrow' Line='crgrow = 0.' -->
  <dd>Cosmic ray growing radius.  Pixels detected and marked in the output cosmic
  ray mask by the <i>crval</i> value are increased in size in the mask (but
  not replaced in the output image) by also flagging all zero valued mask
  pixels within this specified radius with the cosmic ray mask value.  This
  is done after the detection phase is complete.  The separation between
  pixels is the distance between pixel centers computed as a real value.
  Note a value of at least one is required to affect other mask pixels.
  </dd>
  </dl>
  <dl id="l_objval">
  <dt><b>objval = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='objval' Line='objval = 0' -->
  <dd>Mask value for detected objects.  It is legal for the value to be
  zero to not mark the objects in the output mask.
  </dd>
  </dl>
  <dl id="l_lobjsig">
  <dt><b>lobjsig = 10., hobjsig = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lobjsig' Line='lobjsig = 10., hobjsig = 5.' -->
  <dd>Low and high sigma factors for detecting objects.  These factors multiply
  the computed or estimated sigma at each pixel and these threshold values
  are compared to the difference between the block average filter value and
  the background annulus median.  If the values are made very large then
  object detection can be eliminated and cosmic rays will be detected
  everywhere.
  </dd>
  </dl>
  <dl id="l_objgrow">
  <dt><b>objgrow = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='objgrow' Line='objgrow = 0.' -->
  <dd>Object detection growing radius.  Pixels detected and marked in the output
  mask by the <i>objval</i> value are increased in size in the mask by also
  flagging all zero valued mask pixels within this specified radius with the
  cosmic ray mask value.  This is done after the detection phase is complete
  and so object grown pixels are not used in excluding cosmic ray
  candidates.  The separation between pixels is the distance between pixel
  centers computed as a real value.  Note a value of at least one is
  required to affect other mask pixels.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Craverage</b> detects cosmic rays and objects using a moving block
  average filter with the central pixel and a specified number of additional
  highest pixels excluded and a median of an annulus around the block average
  box.  It avoids identification of the cores of objects as cosmic rays by
  excluding pixels within the detected objects as cosmic ray candidates.
  </p>
  <p>
  The block average filter computes the average of pixels in a box with the
  central or target pixel excluded.  In addition the <i>nrej</i> parameter can
  be used to exclude that number of highest remaining pixels as possible
  contamination from cosmic rays which are larger than one pixel or possibly
  a very nearby additional cosmic ray.  The <i>nrej</i> value should be kept
  small relative to the total number of pixels in the average so that the
  average will still be elevated over the median in real underlying objects.
  The resulting average is used as the prediction for the value of the target
  pixel.  The median of the pixels in a square background annulus around the
  block average box provides the prediction for the background at the target
  pixel.
  </p>
  <p>
  The target pixel is considered part of an object if the difference between
  the average value and the median background exceeds a specified threshold.
  If the pixel is NOT considered to be part of an object then if the
  difference between the pixel value and the average value exceeds a
  different specified threshold it is identified as a cosmic ray.
  </p>
  <p>
  The thresholds are defined in terms of sigma factors, which may be
  different for positive and negative deviations and for object and
  cosmic ray identification.  The sigma factors multiply an estimate
  for the statistical sigma of the target pixel.  The estimate is
  either based on a noise model or sigma of pixels in a box near the
  target pixel.
  </p>
  <p>
  The <i>crmask</i> parameter specifies a pixel mask for the image.  If the
  mask exists then non-zero mask values will be used to exclude pixels from
  the average, background median, and empirical sigma estimates.  Also any
  pixels with non-zero mask values will not be altered either in the output
  image or in the final mask.  If the  mask does not exist then it behaves as
  if all mask values are zero.  If all pixels in the average box or median
  annulus are previously flagged then the estimates will be undefined and
  nothing will be done to the output image or mask.  Because the task can
  use an input mask to mark pixels not to be considered it can be used
  in an iterative fashion.
  </p>
  <p>
  The noise model is given by the formula
  </p>
  <div class="highlight-default-notranslate"><pre>
  variance = var0 + var1 * data + var2 * data^2
  </pre></div>
  <p>
  where data is the maximum of zero and the average estimate for the target
  pixel.  The coefficients are all given in terms of the data numbers.  This
  model can be related to common detector parameters.  For CCDs var0 is the
  readout noise expressed as a variance in data numbers and var1 is the
  inverse gain (DN/electrons).  The second order coefficient has the
  interpretation of flat field introduced variance.
  </p>
  <p>
  If all the coefficients are zero then an empirical sigma is estimated as
  follows.  The input image is divided into square blocks of size
  <i>nsig</i>.  The (unmasked) pixel values in a block are sorted and the
  pixel values nearest the 15.9 and 84.1 percentiles are selected.  These are
  the one sigma points in a Gaussian distribution.  The sigma estimate is the
  difference of these two values divided by two.  This algorithm is used to
  avoid contamination of the sigma estimate by the bad pixel values.  The
  block size must be at least 10 pixels in each dimension to provide
  sufficient pixels for a good estimate of the percentile points.  The sigma
  estimate for a pixel is the sigma from the nearest block.  A moving box is
  not used for reasons of efficiency.
  </p>
  <p>
  If an output image name is specified then the output image is produced as a
  copy of the input image but with the identified cosmic ray pixels replaced
  by the average predicted value.  Other optional output images are
  the average filtered values and the sigma values.
  </p>
  <p>
  If a mask is specified the detected cosmic rays will be identified with
  values given by the <i>crval</i> parameter and object pixels will be
  identified with values given by the <i>objval</i> parameter.  Note that one
  does not need to use an output image and the cosmic rays can be replaced by
  interpolation in the data using the tasks <i>crfix</i>, <i>fixpix</i>, or
  <i>ccdproc</i>.
  </p>
  <p>
  One final step may be applied to the output mask.  The mask values
  identified with the <i>crval</i> and <i>objval</i> values may be grown
  by identifying pixel values within a specified radius with the same
  mask value.  Note that this step is done at the end and so any pixels
  in a preexisting input mask with the same values will also be grown.
  Also the grown pixels will not affect the output cosmic ray replaced
  image.  See <i>crgrow</i> for a further discussion.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  This example illustrates using the <b>craverage</b> task to
  create a mask with cosmic rays and objects identified and displayed.
  The image is a CCD image with a readout noise of 5 electrons
  and a gain of 3 electrons per data number.  This implies variance
  model coefficients of
  </p>
  <div class="highlight-default-notranslate"><pre>
  var0 = (5/3)^2 = 2.78
  var1 = 1/3 = 0.34
  </pre></div>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; display obj001 1                  # Display in first frame
  cl&gt; craverage obj001 "" crmask=mask001 var0=2.78 var1=0.34\
  &gt;&gt;&gt; crval=1 objval=2
  cl&gt; display crobj001 2 overlay=mask001 ocol="1=green,2=red"
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  cosmicrays, crnebula, median, crfix, crgrow, crmedian
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE   ' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

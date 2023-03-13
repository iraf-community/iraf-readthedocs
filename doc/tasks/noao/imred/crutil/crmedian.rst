.. _crmedian:

crmedian: Detect and replace cosmic rays with median filter
===========================================================

**Package: crutil**

.. raw:: html

  <section id="s_usage___">
  <h3>Usage   </h3>
  <div class="highlight-default-notranslate"><pre>
  crmedian input output
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input image in which to detect cosmic rays.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output image in which cosmic rays are replaced by the median value.
  If no output image name is given then no output image will be created.
  </dd>
  </dl>
  <dl id="l_crmask">
  <dt><b>crmask = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crmask' Line='crmask = ""' -->
  <dd>Output cosmic ray mask.  Detected cosmic rays (and other deviant pixels)
  are identified in the mask with values of one and good pixels with a values
  of zero.  If no output cosmic ray mask is given then no mask will be
  created.
  </dd>
  </dl>
  <dl id="l_median">
  <dt><b>median = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='median' Line='median = ""' -->
  <dd>Output median filtered image.  If no image name is given then no output will be
  created.
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma' Line='sigma = ""' -->
  <dd>Output sigma image.  If no image name is given then no output will be
  created.
  </dd>
  </dl>
  <dl id="l_residual">
  <dt><b>residual = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='residual' Line='residual = ""' -->
  <dd>Output residual image.  This is the input image minus the median filtered
  image divided by the sigma image.  Thresholds in this image determine the
  cosmic rays detected.  If no image name is given then no output will be
  created.
  </dd>
  </dl>
  <dl id="l_var0">
  <dt><b>var0 = 0., var1 = 0., var2 = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='var0' Line='var0 = 0., var1 = 0., var2 = 0.' -->
  <dd>Variance coefficients for the variance model.  The variance model is
  <div class="highlight-default-notranslate"><pre>
  variance = var0 + var1 * data + var2 * data^2
  </pre></div>
  where data is the maximum of zero and median pixel value and the variance
  is in data numbers.  All the coefficients must be positive or zero.  If
  they are all zero then empirical data sigmas are estimated by a percentile
  method in boxes of size given by <i>ncsig</i> and <i>nlsig</i>.
  </dd>
  </dl>
  <dl id="l_lsigma">
  <dt><b>lsigma = 10, hsigma = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lsigma' Line='lsigma = 10, hsigma = 3' -->
  <dd>Positive sigma factors to use for selecting pixels below and above
  the median level based on the local percentile sigma.  Cosmic rays will
  appear above the median level.
  </dd>
  </dl>
  <dl id="l_ncmed">
  <dt><b>ncmed = 5, nlmed = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncmed' Line='ncmed = 5, nlmed = 5' -->
  <dd>The column and line size of a moving median rectangle used to estimate the
  uncontaminated local image.
  </dd>
  </dl>
  <dl id="l_ncsig">
  <dt><b>ncsig = 25, nlsig = 25</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncsig' Line='ncsig = 25, nlsig = 25' -->
  <dd>The column and line size of regions used to estimate the uncontaminated
  local sigma using a percentile.  The size of the box should contain
  of order 100 pixels or more.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Crmedian</b> detects cosmic rays from pixels deviating by a specified
  statistical amount from the median at each pixel.  It outputs and set of
  the following: a copy of the input image with cosmic rays replaced by the
  median value, a cosmic ray mask identifying the cosmic rays, the median
  filtered image, a sigma image where each pixel has the estimated sigma, and
  the residual image used in detecting the cosmic rays.
  </p>
  <p>
  The residual image is computed by subtracting a median filtered version
  of the input data from the unfiltered input data and dividing by an
  estimate of the pixel sigmas.  The median filter
  box size is given by the <i>ncmed</i> and <i>nlmed</i> parameters.
  If a name for the median image is specified the median filtered image
  will be output.  The variance at each pixel is determined either from
  a variance model or empirically.  If a name for the sigma image is specified
  then the sigma values (the square root of the variance) will be output.
  If a name for the residual image is given then the residual image
  will be output.
  </p>
  <p>
  The empirical variance model is given by the formula
  </p>
  <div class="highlight-default-notranslate"><pre>
  variance = var0 + var1 * data + var2 * data^2
  </pre></div>
  <p>
  where data is the maximum of zero and median pixel value and the variance
  is in data numbers.  This model can be related to common detector
  parameters.  For CCDs var0 is the readout noise expressed as a variance in
  data numbers and var1 is the inverse gain (DN/electrons).  The second order
  coefficient has the interpretation of flat field introduced variance.
  </p>
  <p>
  If all the coefficients are zero then an empirical sigma is estimated
  as follows.  The input image is divided into blocks of size
  <i>ncsig</i> and <i>nlsig</i>.  The pixel values in a block are sorted
  and the pixel values nearest the 15.9 and 84.1 percentiles are
  selected.  These are the one sigma points in a Gaussian distribution.
  The sigma estimate is the difference of these two values divided by
  two.  This algorithm is used to avoid contamination of the sigma
  estimate by the bad pixel values.  The block size must be at least 10
  pixels in each dimension to provide sufficient pixels for a good estimate
  of the percentile points.  The sigma estimate for a pixel is the sigma
  from the nearest block.  A moving box is not used for efficiency.
  </p>
  <p>
  The residual image is divided by the sigma estimate at each pixel.
  Cosmic rays are identified by finding those pixels in the
  residual image which have values greater than <i>hsigma</i> and bad
  pixels with values below <i>lsigma</i> are also identified.
  </p>
  <p>
  If an output image name is specified then the output image is produced as a
  copy of the input image but with the identified cosmic ray pixels replaced
  by the median value.  If an output cosmic ray mask is specified a cosmic
  ray mask will be produced with values of zero for good pixels and one for
  bad pixels.  The cosmic ray mask is used to display the cosmic ray
  positions found and the cosmic rays can be replaced by interpolation (as
  opposed to the median value) using the task <i>crfix</i>.
  </p>
  <p>
  The <b>crmedian</b> detections are very simple and do not take into account
  real structure with scales of a pixel.  Thus this may clip the cores of
  stars and narrow nebular features in the data.  More sophisticated
  algorithms are found in <b>cosmicrays</b>, <i>craverage</i>, and
  <b>crnebula</b>.  The median, sigma, and residual images are available as
  output to evaluate the various aspects of the algorithm.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  This example illustrates using the <b>crmedian</b> task to
  give a cosmic ray removed image and examining the results with an image
  display.  The image is a CCD image with a readout noise of 5 electrons
  and a gain of 3 electrons per data number.  This implies variance
  model coefficients of
  </p>
  <div class="highlight-default-notranslate"><pre>
  var0 = (5/3)^2 = 2.78
  var1 = 1/3 = 0.34
  </pre></div>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; display obj001 1                  # Display in first frame
  cl&gt; # Determine output image, cosmic ray mask, and residual image
  cl&gt; crmedian obj001 crobj001 crmask=mask001 resid=res001\
  &gt;&gt;&gt; var0=2.78 var1=0.34
  cl&gt; display crobj001 2                # Display final image
  cl&gt; display mask001 3 zs- zr- z1=-1 z2=2 # Display mask
  cl&gt; display res001 4 zs- zr- z1=-5 z2=5  # Display residuals
  </pre></div>
  <p>
  By looking at the residual image the sigma clippig threshold can be
  adjusted and the noise parameters can be tweaked to minimize clipping
  of real extended structure.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  cosmicrays, craverage, crnebula, median, crfix, crgrow
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE   ' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

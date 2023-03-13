.. _crnebula:

crnebula: Detect and replace cosmic rays in nebular data
========================================================

**Package: crutil**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  crnebula input output
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input image in which cosmic rays are to be detected.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output image in which cosmic rays are to be replaced by the median.
  If no output image is given (specified as <span style="font-family: monospace;">""</span>) then no output image
  is created.
  </dd>
  </dl>
  <dl id="l_crmask">
  <dt><b>crmask = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crmask' Line='crmask = ""' -->
  <dd>Output cosmic ray mask identifying the cosmic rays found.  The mask
  will have values of one for cosmic rays and zero for non-cosmic rays.
  If no output cosmic ray mask is given (specified as <span style="font-family: monospace;">""</span>) then no mask
  is created.
  </dd>
  </dl>
  <dl id="l_residual">
  <dt><b>residual = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='residual' Line='residual = ""' -->
  <dd>Output residual image.  This is the input image minus the median filtered
  image divided by the estimated sigma at each pixel.  Thresholds in this
  image determine the cosmic rays detected.  If no image name is given then
  no output will be created.
  </dd>
  </dl>
  <dl id="l_rmedresid">
  <dt><b>rmedresid = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rmedresid' Line='rmedresid = ""' -->
  <dd>Output image for the difference between the box median filter image and
  the ring median filtered image divided by the estimated sigma at each
  pixel.  If no image name is given then no output will be created.
  </dd>
  </dl>
  <dl id="l_var0">
  <dt><b>var0 = 0., var1 = 0., var2 = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='var0' Line='var0 = 0., var1 = 0., var2 = 0.' -->
  <dd>Variance coefficients for the variance model.  The variance model is
  <div class="highlight-default-notranslate"><pre>
  variance = var0 + var1 * data + var2 * data^2
  </pre></div>
  where data is the maximum of zero and median pixel value and the variance is in
  data numbers.  All the coefficients must be positive or zero.  If they are
  all zero then empirical data sigmas are estimated by a percentile method in
  boxes of size given by <i>ncsig</i> and <i>nlsig</i>.
  </dd>
  </dl>
  <dl id="l_sigmed">
  <dt><b>sigmed = 3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigmed' Line='sigmed = 3.' -->
  <dd>Sigma clipping factor for the residual image.
  </dd>
  </dl>
  <dl id="l_sigdiff">
  <dt><b>sigdiff = 3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigdiff' Line='sigdiff = 3.' -->
  <dd>Sigma clipping factor for the residuals between the box median and ring median
  filtered images.
  </dd>
  </dl>
  <dl id="l_mbox">
  <dt><b>mbox = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mbox' Line='mbox = 5' -->
  <dd>Box size, in pixels, for the box median filtering.
  </dd>
  </dl>
  <dl id="l_rin">
  <dt><b>rin = 1.5, rout = 6.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rin' Line='rin = 1.5, rout = 6.' -->
  <dd>Inner and outer radii, in pixels, for the ring median filtering.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print some progress information?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task uses a combination of box median filtering to detect cosmic rays
  and the difference between box and ring median filtering to identify
  regions of fine nebular structure which should not be treated as cosmic
  rays.  The output consists of some set of the input image with cosmic rays
  replaced by the median, a cosmic ray mask, the residual image used to
  detect the cosmic rays, and the residual image used to exclude cosmic rays
  in regions of nebular fine structure.  The cosmic ray mask may be used
  later with <b>crgrow</b> and <b>crfix</b> to grow and remove the cosmic rays
  from the data by interpolation rather than the median.
  </p>
  <p>
  The algorithm is as follows.  The input image is median filtered using a
  box of size given by <i>mbox</i>.  The residual image between the unfiltered
  and filter data is computed.  The residuals are divided by the estimated
  sigma of the pixel.  Cosmic rays are those which are more than <i>sigmed</i>
  above zero in the residual image.  This residual image may be output if an
  output name is specified.  This part of the algorithm is identical to that
  of the task <i>crmedian</i> and, in fact, that task is used.
  </p>
  <p>
  The median image not only enhances cosmic rays it also enhances narrow fine
  structure in the input image.  To avoid identifying this structure as
  cosmic rays a second filtered residual image is created which
  preferentially identifies this structure over the cosmic rays.  The input
  image is filtered using a ring median of specified inner and outer radius.
  The inner radius is slightly larger than the scale of the cosmic rays and
  the outer radius is comparable to the box size of the box median filter.  A
  ring filter replaces the center of the ring by the median of the ring.  The
  difference between the input and ring median filtered image divided by the
  estimated sigma will then be very similar to the box median residual image both
  where there are cosmic rays and where there is diffuse structure but will
  be different where there are linear fine structure patterns.  The
  difference between the median residual image and this ring median residual
  image highlights the regions of fine structure. If a image name is specified
  for the difference of the residual images it will be output.
  </p>
  <p>
  The difference of the median residual images is used to exclude any cosmic
  ray candidate pixels determined from sigma clipping the box median residual
  image which lie where the difference of the median residual images is
  greater than <i>sigdiff</i> different from zero (both positive or
  negative).
  </p>
  <p>
  To understand this algorithm it is recommended that the user save the
  residual and residual difference images and display them and blink against
  the original data.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  This example, the same as in <b>crmedian</b>, illustrates using the
  <b>crnebual</b> task to give a cosmic ray removed image and examining the
  results with an image display.  The image is a CCD image with a readout
  noise of 5 electrons and a gain of 3 electrons per data number.  This
  implies variance model coefficients of
  </p>
  <div class="highlight-default-notranslate"><pre>
  var0 = (5/3)^2 = 2.78
  var1 = 1/3 = 0.34
  </pre></div>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; display obj001 1                  # Display in first frame
  cl&gt; # Determine output image, cosmic ray mask, and residual images
  cl&gt; crnebula obj001 crobj001 crmask=mask001 resid=res001\
  &gt;&gt;&gt; rmedresid=rmed001 var0=2.78 var1=0.34
  cl&gt; display crobj001 2                # Display final image
  cl&gt; display res001 3 zs- zr- z1=-5 z2=5  # Display residuals
  cl&gt; display rmed001 4 zs- zr- z1=-5 z2=5
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
  cosmicrays, crmedian, median, rmedian, crfix, crgrow
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

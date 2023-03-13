.. _findpars:

findpars: Edit the star detection parameters
============================================

**Package: apphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  findpars
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_threshold">
  <dt><b>threshold = 4.0 (sigma)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 4.0 (sigma)' -->
  <dd>The object detection threshold above local background in units of
  <i>datapars.sigma</i>.
  </dd>
  </dl>
  <dl id="l_nsigma">
  <dt><b>nsigma = 1.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigma' Line='nsigma = 1.5' -->
  <dd>The semi-major axis of the Gaussian convolution kernel used to computed the
  density enhancement and mean density images in Gaussian sigma. This semi-
  major axis is equal to min (2.0, 0.42466 * <i>nsigma</i> *
  <i>datapars.fwhmpsf</i> / <i>datapars.scale</i>) pixels.
  </dd>
  </dl>
  <dl id="l_ratio">
  <dt><b>ratio = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ratio' Line='ratio = 1.0' -->
  <dd>The ratio of the sigma of the Gaussian convolution kernel along the minor axis
  direction to the sigma along the major axis direction.  <i>Ratio</i> defaults
  to 1.0 in which case the image is convolved with a circular Gaussian.
  </dd>
  </dl>
  <dl id="l_theta">
  <dt><b>theta = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='theta' Line='theta = 0.0' -->
  <dd>The position angle of the major axis of the Gaussian convolution kernel.
  <i>Theta</i> is measured in degrees counter-clockwise from the x axis.
  </dd>
  </dl>
  <dl id="l_sharplo">
  <dt><b>sharplo = .2, sharphi = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sharplo' Line='sharplo = .2, sharphi = 1.0' -->
  <dd><i>Sharplo</i> and <i>sharphi</i> are numerical cutoffs on the image sharpness
  statistic designed to eliminate brightness maxima which are due to bad pixels
  rather than to astronomical objects.
  </dd>
  </dl>
  <dl id="l_roundlo">
  <dt><b>roundlo = -1.0 roundhi = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='roundlo' Line='roundlo = -1.0 roundhi = 1.0' -->
  <dd><i>Roundlo</i> and <i>roundhi</i> are numerical cutoffs on the image roundness
  statistic designed to eliminate brightness maxima which are due to bad rows or
  columns, rather than to astronomical objects.
  </dd>
  </dl>
  <dl id="l_mkdetections">
  <dt><b>mkdetections = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mkdetections' Line='mkdetections = no' -->
  <dd>Mark the positions of the detected objects on the displayed image ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  DAOFIND approximates the stellar point spread function with an elliptical
  Gaussian function, whose sigma along the semi-major axis is 0.42466 *
  <i>datapars.fwhmpsf</i> / <i>datapars.scale</i> pixels, semi-minor to semi-major
  axis ratio is <i>ratio</i>, and major axis position angle is <i>theta</i>.
  Using this model, a convolution kernel, truncated at <i>nsigma</i> sigma,
  and normalized to sum to zero, is constructed.
  </p>
  <p>
  The density enhancement image <i>starmap</i> is computed by convolving the input
  image with the Gaussian kernel. This operation is mathematically equivalent to
  fitting, in the least-squares sense, the image data at each point with a
  truncated, lowered elliptical Gaussian function. After convolution each point
  in <i>starmap</i> contains as estimate of the amplitude of the best fitting
  Gaussian function at that point. Each point in <i>skymap</i>, if the user
  chooses to compute it, contains an estimate of the best fitting sky value
  at that point.
  </p>
  <p>
  After image convolution DAOFIND steps through <i>starmap</i> searching
  for density enhancements greater than <i>findpars.threshold</i> *
  <i>datapars.sigma</i>, and brighter than all other density enhancements
  within a semi-major axis of 0.42466 <i>findpars.nsigma</i> *
  <i>datapars.fwhmpsf</i>. As the program selects candidates, it computes two
  shape characteristics sharpness and roundness.  The sharpness statistic
  measures the ratio of the difference between the height of the central pixel
  and the mean of the surrounding non-bad pixels, to the height of the best
  fitting Gaussian function at that point. The roundness statistics measures
  the ratio of, the difference in the height of the best fitting Gaussian
  function in x minus the best fitting Gaussian function in y, over the average
  of the best fitting Gaussian functions in x and y. The limits on these
  parameters <i>findpars.sharplo</i>, <i>findpars.sharphi</i>,
  <i>findpars.roundlo</i>, and <i>findpars.roundhi</i>, are set to weed out
  non-astronomical objects and brightness enhancements that are elongated in
  x and y respectively.
  </p>
  <p>
  Lastly the x and y centroids of the detected objects are computed by
  estimating the x and y positions of the best fitting 1D Gaussian
  functions in x and y respectively, a rough magnitude is estimated
  by computing the ratio of the amplitude of the best fitting Gaussian at
  the object position to <i>findpars.threshold</i> * <i>datapars.sigma</i>,
  and the object is added to the output coordinate file.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the object detection parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; lpar findpars
  </pre></div>
  <p>
  2. Edit the object detection parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; findpars
  </pre></div>
  <p>
  3. Edit the FINDPARS parameters from within the DAOFIND task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; epar daofind
  
      ... edit a few daofind parameters
  
      ... move to the findpars parameter and type :e
  
      ... edit the findpars parameter and type :wq
  
      ... finish editing the daofind parameters and type :wq
  </pre></div>
  <p>
  4. Save the current FINDPARS parameter set in a text file fndnite1.par.
  This can also be done from inside a higher level task as in the previous
  example.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; findpars
  
      ... edit the parameters
  
      ... type ":w fndnite1.par" from within epar
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  daofind, datapars
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

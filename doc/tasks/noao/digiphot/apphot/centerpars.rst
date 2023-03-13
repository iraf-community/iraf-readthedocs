.. _centerpars:

centerpars: Edit the centering parameters
=========================================

**Package: apphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  centerpars
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_calgorithm">
  <dt><b>calgorithm = <span style="font-family: monospace;">"centroid"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='calgorithm' Line='calgorithm = "centroid"' -->
  <dd>The centering algorithm. The <span style="font-family: monospace;">"gauss"</span> and <span style="font-family: monospace;">"ofilter"</span> options depend critically
  on the value of the fwhmpsf parameter in the DATAPARS task. The centering
  options are:
  <dl>
  <dt><b>none</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='none' Line='none' -->
  <dd>The initial positions are assumed to be the true centers. Users
  may select this option if the initial centers are know to be accurate,
  e.g. they were computed by DAOFIND task.
  </dd>
  </dl>
  <dl>
  <dt><b>centroid</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='centroid' Line='centroid' -->
  <dd>The object centers are determined by computing the intensity weighted means
  of the marginal profiles in x and y.  This is the recommended default algorithm
  for APPHOT users.
  </dd>
  </dl>
  <dl>
  <dt><b>gauss</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='gauss' Line='gauss' -->
  <dd>The object centers are computed by fitting a Gaussian of fixed fwhmpsf,
  specified by the DATAPARS fwhmpsf parameter, to the marginal profiles in
  x and y using non-linear least squares techniques.
  </dd>
  </dl>
  <dl>
  <dt><b>ofilter</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='ofilter' Line='ofilter' -->
  <dd>The object centers are computed using optimal filtering techniques,
  a triangular weighting function of half width equal to fwhmpsf as
  specified by the DATAPARS fwhmpsf parameter, and the marginal distributions
  in x and y.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_cbox">
  <dt><b>cbox = 5.0  (scale units)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cbox' Line='cbox = 5.0  (scale units)' -->
  <dd>The width of the subraster used for object centering in units of the
  DATAPARS scale parameter. Cbox must be big enough to include a reasonable
  number of pixels  for center determination but not so large so as to include
  a lot of noise. Recommended initial values are 2.5-4.0 * the FWHM of the PSF
  value.
  </dd>
  </dl>
  <dl id="l_cthreshold">
  <dt><b>cthreshold = 0.0 (sigma units)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cthreshold' Line='cthreshold = 0.0 (sigma units)' -->
  <dd>Pixels cthreshold * sigma above (emission features) or below (absorption
  features) the data minimum or maximum respectively are used by the centering
  algorithms where sigma is equal to the value of the DATAPARS sigma parameter. 
  Most APPHOT users should leave this value at 0.0 which invokes the appropriate
  default thresholding technique for each centering algorithm. Setting cthreshold
  to INDEF turns off thresholding altogether for all the centering algorithms.
  </dd>
  </dl>
  <dl id="l_minsnratio">
  <dt><b>minsnratio = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minsnratio' Line='minsnratio = 1.0' -->
  <dd>The minimum signal to noise ratio for object centering. If the estimated signal
  to noise ratio is less than minsnratio the computed center will be returned
  with an error flag.
  </dd>
  </dl>
  <dl id="l_cmaxiter">
  <dt><b>cmaxiter = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cmaxiter' Line='cmaxiter = 10' -->
  <dd>The maximum number of iterations performed by the centering algorithm.
  All the centering algorithms use this parameter.
  </dd>
  </dl>
  <dl id="l_maxshift">
  <dt><b>maxshift = 1.0  (scale units)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxshift' Line='maxshift = 1.0  (scale units)' -->
  <dd>The maximum permissible shift of the center with respect to the initial
  coordinates in units of the scale parameter. If the shift produced by the
  centering algorithms is larger than maxshift, the computed center is returned
  with an error flag.
  </dd>
  </dl>
  <dl id="l_clean">
  <dt><b>clean = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clean' Line='clean = no' -->
  <dd>Symmetry-clean the centering subrater before centering? APPHOT users should
  leave clean set to <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_rclean">
  <dt><b>rclean = 1.0  (scale units)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rclean' Line='rclean = 1.0  (scale units)' -->
  <dd>The cleaning radius for the symmetry-clean algorithm in units of the scale
  parameter.
  </dd>
  </dl>
  <dl id="l_rclip">
  <dt><b>rclip = 2.0  (scale units)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rclip' Line='rclip = 2.0  (scale units)' -->
  <dd>The clipping radius for the symmetry-clean algorithm in units of the scale
  parameter.
  </dd>
  </dl>
  <dl id="l_kclean">
  <dt><b>kclean = 3.0  (sigma)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='kclean' Line='kclean = 3.0  (sigma)' -->
  <dd>The number of sky background standard deviations for the symmetry-clean
  algorithm where sigma is the value of the DATAPARS parameter sigma.
  </dd>
  </dl>
  <dl id="l_mkcenter">
  <dt><b>mkcenter = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mkcenter' Line='mkcenter = no' -->
  <dd>Mark the fitted object centers on the displayed image ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The centering algorithm parameters control the action of the centering
  algorithms. The default parameters values have been proven to produce
  reasonable results in the majority of cases. Several of the centering
  parameters are defined in terms of the DATAPARS parameter <i>scale</i>,
  the scale of the image, and <i>sigma</i> the standard deviation of
  the sky pixels. 
  </p>
  <p>
  For each object to be measured a subraster of data <i>cbox</i> / <i>scale</i>
  pixels wide around the initial position supplied by the user is extracted
  from the IRAF image. If scale is defined in units of the number
  the half-width half-maximum of the psf per pixel, then a single value of
  cbox can be used for centering objects in images with different psfs.
  </p>
  <p>
  If <i>clean</i> is <span style="font-family: monospace;">"yes"</span> the symmetry-clean algorithm is applied to the
  centering subraster prior to centering. The cleaning algorithm attempts
  to correct defects in the centering subraster by assuming that the image
  is radially symmetric and comparing pixels on opposite sides of the center
  of symmetry.  The center of symmetry is assumed to be the maximum pixel
  in the subraster, unless the maximum pixel is more than <i>maxshift /
  scale</i> from the initial center, in which case the initial center is used
  as the center of symmetry.  Pixels inside the cleaning radius are not edited.
  Pairs of pixels in the cleaning region, r &gt; <i>rclean</i> / <i>scale</i>
  and r &lt;= <i>rclip</i> / <i>scale</i> and diametrically opposed about the
  center of symmetry are tested for equality. If the difference between the
  pixels is greater than <i>kclean * sigma</i>, the larger value is replaced
  by the smaller.  In the cleaning region the sigma is determined by the
  noise model assumed for the data. Pairs of pixels in the clipping region,
  r &gt; <i>rclip</i> / <i>scale</i> are tested in the same manner as those in
  the cleaning region. However the sigma employed is the sigma of the
  sky background. Most APPHOT users should leave clean set to <span style="font-family: monospace;">"no"</span>.
  </p>
  <p>
  New centers are computed using the centering algorithm specified by
  <i>calgorithm</i>, the data specified by <i>cbox / scale</i>, and pixels
  that are some threshold above (below) an estimate of the local minimum
  (maximum). <i>Cthreshold</i> values of 0.0, a positive number, and INDEF
  invoke the default thresholding algorithm, a threshold equal to the
  local minimum (maximum) plus  (minus) <i>datapars.sigma * cthreshold</i>,
  and a threshold exactly equal to the local minimum (maximum) respectively.
  </p>
  <p>
  After thresholding the signal to noise ratio of the subraster is estimated. 
  If the SNR &lt; <i>minsnratio</i> the new center is still computed but an error
  flag is set.
  </p>
  <p>
  The default centering algorithm is <i>centroid</i>. Centroid computes the
  intensity weighted mean and mean error of the centering box x and y marginal
  distributions using points in the marginal arrays above (below) the minimum
  (maximum) data pixel plus (minus) a threshold value.
  </p>
  <p>
  The threshold value is either the mean, <i>datapars.sigma * cthreshold</i>
  above (below) the local minimum (maximum) if <i>cthreshold</i> is greater
  than zero, or zero above (below) the local minimum (maximum) if
  <i>cthreshold</i> is INDEF.  The centroid algorithm is similar to that
  by the old KPNO Mountain Photometry Code. Note that centroid is the only
  centering algorithm which does not depend on the value of
  <i>datapars.fwhmpsf</i>.
  </p>
  <p>
  The centering algorithm <i>gauss</i> computes the new centers by fitting a
  1D Gaussian function to the marginal distributions in x and y using a
  fixed fwhmpsf set by <i>datapars.fwhmpsf</i>.  Initial guesses for the fit
  parameters are derived from the data. The gauss algorithm iterates until
  a best fit solution is achieved.
  </p>
  <p>
  The final centering algorithm choice <i>ofilter</i> employs a variation of the
  optimal filtering technique in which the profile is simulated by a triangle
  function of width <i>datapars.fwhmpsf</i>.
  </p>
  <p>
  The default thresholding algorithm for all centering algorithms other
  than <span style="font-family: monospace;">"centroid"</span> is no thresholding.
  </p>
  <p>
  If the computed shift in either coordinate &gt; <i>maxshift</i> / <i>scale</i>,
  the new center is returned but an error flag is set.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the centering parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; lpar centerpars
  </pre></div>
  <p>
  2. Edit the centering parameters
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; centerpars
  </pre></div>
  <p>
  3. Edit the CENTERPARS parameters from with the PHOT task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; epar phot
  
      ... edit a few phot parameters
  
      ... move to the centerpars parameter and type :e
  
      ... edit the centerpars parameters and type :wq
  
      ... finish editing the phot parameters and type :wq
  </pre></div>
  <p>
  4. Save the current CENTERPARS parameter set in a text file ctrnite1.par.
  This can also be done from inside a higher level task as in the
  previous example.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; centerpars
  
      ... edit the parameters
  
      ... type ":w ctrnite1.par"  from within epar
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  center,phot,wphot,polyphot,radprof
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

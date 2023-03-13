.. _daopars:

daopars: Edit the daophot algorithms parameter set
==================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  daopars
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"gauss"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "gauss"' -->
  <dd>The functional form of the analytic component of the PSF model computed by the
  DAOPHOT PSF task. The better this function matches the true PSF, especially in
  the cores of the stars, the smaller the interpolation errors will be. The
  choices are the following.
  <dl>
  <dt><b>gauss</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='gauss' Line='gauss' -->
  <dd>An elliptical Gaussian function aligned along the x and y axes of the
  input image.
  </dd>
  </dl>
  <dl>
  <dt><b>moffat15</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='moffat15' Line='moffat15' -->
  <dd>An elliptical Moffat function with a beta parameter of 1.5.
  </dd>
  </dl>
  <dl>
  <dt><b>moffat25</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='moffat25' Line='moffat25' -->
  <dd>An elliptical Moffat function with a beta parameter of 2.5.
  </dd>
  </dl>
  <dl>
  <dt><b>lorentz</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='lorentz' Line='lorentz' -->
  <dd>An elliptical Lorentzian function with beta parameter of 1.0.
  </dd>
  </dl>
  <dl>
  <dt><b>penny1</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='penny1' Line='penny1' -->
  <dd>A Gaussian core with Lorentzian wings function, where the Gaussian core may be
  tilted, but the Lorentzian wings are elongated along the x or y axes.  The
  Lorentzian wings have a beta parameter of 1.0.
  </dd>
  </dl>
  <dl>
  <dt><b>penny2</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='penny2' Line='penny2' -->
  <dd>A Gaussian core with Lorentzian wings function, where the Gaussian core and
  Lorentzian wings may be tilted in different directions.  The Lorentzian wings
  have a beta parameter of 1.0.
  </dd>
  </dl>
  <dl>
  <dt><b>auto</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='auto' Line='auto' -->
  <dd>The PSF task computes the analytic PSF model for each of the six analytic model
  PSFs in turn and selects the one that produces the smallest standard deviation
  for the model fit.
  </dd>
  </dl>
  <dl>
  <dt><b>func1,func2,...</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='func1' Line='func1,func2,...' -->
  <dd>The PSF task computes the analytic PSF model for each of a subset of the six
  defined functions in turn, and selects the one that produces the smallest
  standard deviation for the model fit.
  </dd>
  </dl>
  In general <span style="font-family: monospace;">"gauss"</span> is the best and most efficient choice for a well-sampled
  ground-based image, <span style="font-family: monospace;">"lorentz"</span> is best for old ST images, and <span style="font-family: monospace;">"moffat15"</span> or
  <span style="font-family: monospace;">"moffat25"</span> are best for under-sampled ground-based images. 
  </dd>
  </dl>
  <dl id="l_varorder">
  <dt><b>varorder = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='varorder' Line='varorder = 0' -->
  <dd>The order of variability of the PSF model computed by the DAOPHOT PSF task.
  Varorder sets the number of look-up tables containing the deviations of the
  true PSF from the analytic model PSF that are computed by the model.
  <dl>
  <dt><b><span style="font-family: monospace;">"-1"</span>    </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"-1"    ' -->
  <dd>Only the analytic function specified by <i>function</i> is used to compute
  the PSF model. The PSF model is constant over the image.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"0"</span>   </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"0"   ' -->
  <dd>The analytic function and one look-up table are used to compute the
  PSF model. The  PSF model is constant over the image.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"1"</span>    </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"1"    ' -->
  <dd>The analytic function and three look-up tables are used to compute the PSF
  model. The PSF model is linearly variable over the image, with terms
  proportional to 1, x and y.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"2"</span>    </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"2"    ' -->
  <dd>The analytic function and six look-up tables are used to compute the
  PSF model. The PSF model is quadratically variable over the image, with terms
  proportional to 1, x, y, x**2, xy, y**2.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_nclean">
  <dt><b>nclean = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nclean' Line='nclean = 0' -->
  <dd>The number of additional iterations the PSF task performs to compute the PSF
  look-up tables. If <i>nclean</i> is &gt; 0, stars which contribute deviant
  residuals to the PSF look-up tables in the first iteration, will be
  down-weighted in succeeding iterations.
  </dd>
  </dl>
  <dl id="l_saturated">
  <dt><b>saturated = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='saturated' Line='saturated = no' -->
  <dd>Use saturated stars to improve the signal-to-noise in the wings of the PSF
  model computed by the PSF task? This parameter should only be set to
  <span style="font-family: monospace;">"yes"</span> where there are too few high signal-to-noise unsaturated stars
  in the image to compute a reasonable model for the stellar profile wings.
  </dd>
  </dl>
  <dl id="l_matchrad">
  <dt><b>matchrad = 3.0 (scale units)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='matchrad' Line='matchrad = 3.0 (scale units)' -->
  <dd>The tolerance in scale units for matching the stellar x and y centroids in the
  input photometry file with the image cursor position. Matchrad is currently
  used by the PSTSELECT and PSF tasks to match stars shown on the image display
  with stars in the photometry list.
  </dd>
  </dl>
  <dl id="l_psfrad">
  <dt><b>psfrad = 11.0 (scale units)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='psfrad' Line='psfrad = 11.0 (scale units)' -->
  <dd>The radius of the circle in scale units within which the PSF model is defined.
  Psfrad should be a pixel or two larger than the radius at which the intensity
  of the brightest star of interest fades into the noise. Psfrad can never be
  set larger than the size of the PSF model but may set smaller in tasks
  like GROUP, ALLSTAR, SUBSTAR, and ADDSTAR.
  </dd>
  </dl>
  <dl id="l_fitrad">
  <dt><b>fitrad = 3.0 (scale units)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitrad' Line='fitrad = 3.0 (scale units)' -->
  <dd>The fitting radius in scale units. Only pixels within the fitting radius of
  the center of a star will contribute to the fits computed by the PEAK, NSTAR
  and ALLSTAR tasks. For most images the fitting radius should be approximately
  equal to the FWHM of the PSF. Under severely crowded conditions a somewhat
  smaller value may be used in order to improve the fit. If the PSF is variable,
  the FWHM is very small, or sky fitting is enabled in PEAK and NSTAR on the
  other hand, it may be necessary to increase the fitting radius to achieve a
  good fit.
  </dd>
  </dl>
  <dl id="l_recenter">
  <dt><b>recenter = yes (peak, nstar, and allstar)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='recenter' Line='recenter = yes (peak, nstar, and allstar)' -->
  <dd>Compute new positions as well as magnitudes for all the stars in the input
  photometry list?
  </dd>
  </dl>
  <dl id="l_fitsky">
  <dt><b>fitsky = no (peak, nstar, and allstar)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitsky' Line='fitsky = no (peak, nstar, and allstar)' -->
  <dd>Compute new sky values for the stars in the input list (peak, nstar, allstar).
  If fitsky = <span style="font-family: monospace;">"no"</span>, the PEAK, NSTAR, and ALLSTAR tasks compute a group sky value
  by averaging the sky values of the stars in the group.  If fitsky = <span style="font-family: monospace;">"yes"</span>,
  PEAK and NSTAR fit the group sky simultaneously with the positions and
  magnitudes. If fitsky = yes the ALLSTAR task computes new sky values for each
  star every third iteration by subtracting off the best current fit for the star
  and and estimating the median of the pixels in the annulus defined by
  <i>sannulus</i> and <i>wsannulus</i>. The new group sky value is the average of
  the new individual values.
  </dd>
  </dl>
  <dl id="l_groupsky">
  <dt><b>groupsky = yes (nstar and allstar)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='groupsky' Line='groupsky = yes (nstar and allstar)' -->
  <dd>If groupsky is <span style="font-family: monospace;">"yes"</span>,  then the sky value for every pixel which contributes to
  the fit is identical and equal to the mean of the sky values of all the stars
  in the group.  If <i>groupsky</i> is <span style="font-family: monospace;">"no"</span>,  then the sky value for every pixel
  which contributes to the fit is equal to the mean of the sky values of all the
  stars in the group for which that pixel is within one fitting radius.
  </dd>
  </dl>
  <dl id="l_sannulus">
  <dt><b>sannulus = 0.0 (scale units, allstar)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sannulus' Line='sannulus = 0.0 (scale units, allstar)' -->
  <dd>The inner radius of the sky annulus used by ALLSTAR to recompute the sky 
  values.
  </dd>
  </dl>
  <dl id="l_wsannulus">
  <dt><b>wsannulus = 11 (scale units, allstar)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wsannulus' Line='wsannulus = 11 (scale units, allstar)' -->
  <dd>The width of the sky annulus used by ALLSTAR to recompute the sky values.
  </dd>
  </dl>
  <dl id="l_flaterr">
  <dt><b>flaterr=0.75 (percent, peak, nstar, allstar)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flaterr' Line='flaterr=0.75 (percent, peak, nstar, allstar)' -->
  <dd>The image flat-fielding error in percent used to compute the predicted
  errors of the fit.
  </dd>
  </dl>
  <dl id="l_proferr">
  <dt><b>proferr = 5.0 (percent, peak, nstar, allstar)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='proferr' Line='proferr = 5.0 (percent, peak, nstar, allstar)' -->
  <dd>The profile or interpolation fitting error in percent used to compute
  the predicted errors of the fit.
  </dd>
  </dl>
  <dl id="l_maxiter">
  <dt><b>maxiter = 50 (peak, nstar, allstar)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxiter' Line='maxiter = 50 (peak, nstar, allstar)' -->
  <dd>The maximum number of times that the PSF fitting tasks PEAK, NSTAR, and ALLSTAR
  will iterate on the PSF fit before giving up.
  </dd>
  </dl>
  <dl id="l_cliprange">
  <dt><b>cliprange = 2.5, clipexp = 6.0 (peak, nstar, allstar)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cliprange' Line='cliprange = 2.5, clipexp = 6.0 (peak, nstar, allstar)' -->
  <dd>The parameters of the down-weighting scheme in the fitting code used to resist
  bad data. For values of clipexp greater than 1 a residual small compared to
  cliprange standard deviations does not have its weight significantly altered,
  one with exactly <i>cliprange</i> standard deviations is assigned half its
  normal weight, and large residuals are assigned weights which fall off as the
  standard deviation to the minus clipexp power. For normal applications users
  should leave these parameter at their default value.
  </dd>
  </dl>
  <dl id="l_critsnratio">
  <dt><b>critsnratio = 1.0 (group)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='critsnratio' Line='critsnratio = 1.0 (group)' -->
  <dd>The ratio of the model intensity of the brighter star computed at a distance of
  one fitting radius from the center of the fainter star, to the expected random
  error computed from the readout noise, gain and value of the PSF. The critical
  signal-to-noise ratio parameter is used to group stars. In general if a small
  value such as 0.1 divides all the stars in an image into groups less than
  <i>maxgroup</i>, then the expected random errors will determine the accuracy
  of the photometry. On the other hand if a value of critical overlap much
  greater than one is required to divide up the stars, crowding errors will
  dominate random errors. If a value of 1 is sufficient then crowding and
  random errors are roughly equivalent.
  </dd>
  </dl>
  <dl id="l_mergerad">
  <dt><b>mergerad = INDEF (scale units, nstar, allstar)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mergerad' Line='mergerad = INDEF (scale units, nstar, allstar)' -->
  <dd>The critical separation in scale units between two objects for an object merger
  to be considered. Objects with separations &gt; mergerad will not be merged; faint
  objects with separations &lt;= mergerad will be considered for merging. The
  default value of mergerad is sqrt (2 *(PAR1**2 + PAR2**2)), where PAR1 and PAR2
  are the half-width at half-maximum along the major and minor axes of the psf
  model. Merging can be turned off altogether by setting mergerad to 0.0.
  </dd>
  </dl>
  <dl id="l_maxnstar">
  <dt><b>maxnstar = 10000 (pstselect, psf, group, allstar, substar)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxnstar' Line='maxnstar = 10000 (pstselect, psf, group, allstar, substar)' -->
  <dd>The initial star list buffer size. If there are more than maxnstar stars in the
  input photometry file buffer, DAOPHOT will resize the buffers as needed.
  The only limitation is the memory and configuration of the host computer.
  </dd>
  </dl>
  <dl id="l_maxgroup">
  <dt><b>maxgroup = 60 (nstar, allstar)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxgroup' Line='maxgroup = 60 (nstar, allstar)' -->
  <dd>The maximum numbers of stars that the multiple star fitting tasks NSTAR and
  ALLSTAR will fit simultaneously. NSTAR will not to fit groups large than
  maxgroup. ALLSTAR dynamically regroups the stars in large groups until the
  group is either maxgroup or smaller in size or becomes too dense to group,
  after which the faintest stars are rejected until the group is less than
  maxgroup ins size.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  DAOPARS is a parameter set task which stores the DAOPHOT parameters
  required by all those DAOPHOT tasks which compute the PSF model, fit stars
  to the PSF model, or evaluate the PSF model.
  </p>
  <p>
  Typing DAOPARS on the terminal invokes the EPAR parameter editing task. The
  DAOPARS parameters may also be edited from within an EPAR command on task,
  for example PSF, which references them. The DAOPARS parameters may also
  be changed on the command line in the usual manner when any task which
  references them is executed.
  </p>
  <p>
  Any given set of DAOPARS parameters may stored in a text file along with
  the data being reduced by typing the :w command from within the EPAR task. If
  the user then sets the value of the <i>daopars</i> parameter to the name of
  the file containing the stored parameter set, the stored parameters will be
  used instead of the default set in the uparm directory.
  </p>
  </section>
  <section id="s_algorithms">
  <h3>Algorithms</h3>
  <p>
  The functional forms of the analytic PSF functions are as follows. The
  A is simply an amplitude or normalization constant The Pn are parameters
  which are fit during the PSF model generation process.
  </p>
  <div class="highlight-default-notranslate"><pre>
  z = x ** 2 / p1 ** 2 + y ** 2 / p2 ** 2
  gauss = A * exp (-0.5 * z)
  
  z = x ** 2 / p1 ** 2 + y ** 2 / p2 ** 2 + x * y * p3
  moffat15 = A / (1 + z) ** 1.5
  moffat25 = A / (1 + z) ** 2.5
  
  z = x ** 2 / p1 ** 2 + y ** 2 / p2 ** 2 + x * y * p3
  lorentz = A / (1.0 + z)
  
  z = x ** 2 / p1 ** 2 + y ** 2 / p2 ** 2
  e = x ** 2 / p1 ** 2 + y ** 2 / p2 ** 2 + x * y * p4
  penny1 = A * ((1 - p3) / (1.0 + z) + p3 * exp (-0.693*e))
  
  z = x ** 2 / p1 ** 2 + y ** 2 / p2 ** 2 + p5 * x * y
  e = x ** 2 / p1 ** 2 + y ** 2 / p2 ** 2 + x * y * p4
  penny2 = A * ((1 - p3) / (1.0 + z) + p3 * exp (-0.693*e))
  </pre></div>
  <p>
  The predicted errors in the DAOPHOT photometry are computed per
  pixel as follows, where terms 1, 2, 3, and 4 represent the readout
  noise, the poisson noise, the flat-fielding error, and the interpolation
  error respectively. The quantities readnoise, epadu, I, M, p1, and p2
  are the readout noise in electrons, the gain in electrons per ADU,
  the pixel intensity in ADU, the PSF model intensity in ADU, the FWHM
  in x and the FWHM in y, both in pixels.
  </p>
  <div class="highlight-default-notranslate"><pre>
  error = sqrt (term1 + term2 + term3 + term4)  (ADU)
  term1 = (readnoise / epadu) ** 2
  term2 = I / epadu
  term3 = (.01 * flaterr * I) ** 2
  term4 = (.01 * proferr * M / p1 / p2) ** 2
  </pre></div>
  <p>
  The radial weighting function employed by all the PSF fitting tasks is
  the following, where dx and dy are the distance of the pixel from the
  centroid of the star being fit.
  </p>
  <div class="highlight-default-notranslate"><pre>
  wtr = 5.0 / (5.0 + rsq / (1.0 - rsq))
  rsq = (dx ** 2 + dy ** 2) / fitrad ** 2
  </pre></div>
  <p>
  The weight assigned each pixel in the fit then becomes the following.
  </p>
  <div class="highlight-default-notranslate"><pre>
  wtp = wtr / error ** 2
  </pre></div>
  <p>
  After a few iterations and if clipexp &gt; 0, a clipping scheme to reject bad
  data is enabled.  The weights of the pixels are recomputed as follows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  wt = wtp / (1.0 + (residual / error / chiold /
       cliprange) ** clipexp)
  </pre></div>
  <p>
  Pixels having a residual of cliprange sigma will have their weight reduced
  by half.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print the DAOPARS task parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; lpar daopars
  </pre></div>
  <p>
  2. Edit the DAOPARS parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; daopars
  </pre></div>
  <p>
  3. Edit the DAOPARS parameters from with the PSF task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; epar psf
  
      ... edit a few psf parameters
  
      ... move to the daopars parameter and type :e
  
      ... edit the daopars parameters and type :wq
  
      ... finish editing the psf parameters and type :wq
  </pre></div>
  <p>
  4. Save the current DAOPARS parameter set in a text file daonite1.par.
     This can also be done from inside a higher level task as in the
     above example.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; epar daopars
  
      ... type ":w daonite1.par"  from within epar
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
  pstselect,psf,peak,group,nstar,allstar,substar,addstar,setimpars
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'ALGORITHMS' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _controlpar:

controlpar: Set algorithm control parameters (pset).
====================================================

**Package: isophote**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  controlpar
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This pset is used to set the algorithm control parameters associated with
  the 'ellipse' task. Two basic controls are implemented here:
  </p>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(1)' -->
  <dd>At each given isophotal semi-major axis, a convergency criterion for
  stopping iterations.
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(2)' -->
  <dd>At large semi-major axis lengths, a detection criterion for stopping
  growing the ellipses to regions of too low signal-to-noise ratio.
  </dd>
  </dl>
  <p>
  The in-isophote controls are provided by parameters 'conver', 'minit' and
  'maxit'. Iterations are stopped when either one of the following criteria
  are met:
  </p>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(1)' -->
  <dd>The largest harmonic amplitude is less than 'conver' times the rms residual 
  of the intensity data around the harmonic fit (see discussion in 'samplepar'
  pset).
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(2)' -->
  <dd>'maxit' iterations are reached.
  </dd>
  </dl>
  <dl>
  <dt><b>(3)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(3)' -->
  <dd>More than a given fraction of the elliptical sample points have no
  valid data in then, either because they lie outside the image boundaries 
  or because they where flagged out from the fit (see 'samplepar' pset).
  </dd>
  </dl>
  <p>
  In any case, a minimum number of iterations 'minit' is always performed. 
  A minimum of 10 iterations guarantees that, on average, 2 iterations will 
  be available for fitting each independent parameter (the four harmonic 
  amplitudes and the intensity level). In the first isophote, the minimum
  number of iterations is 2 * 'minit', to ensure that, even departing from
  not-so-good initial values, the algorithm converges to an appropriate 
  solution.
  </p>
  <p>
  The main control for preventing ellipses to grow to regions of too 
  low signal-to-noise ratio is provided by parameter 'maxgerr'. It specifies
  the maximum acceptable relative error in the local radial intensity
  gradient. Experiments (see paper quoted in the 'ellipse' help page) showed
  that the fitting precision relates to that relative error. Its usual
  behavior is to increase with semi-major axis, being larger in outer,
  fainter galaxy regions. 
  </p>
  <p>
  A number of actions may happen when the current gradient error becomes
  larger than 'maxgerr' (or becomes non-significant and thus is set to INDEF)
  in the process of increasing semi-major axis length. If the maximum semi-major 
  axis specified by parameter 'geompar.maxsma' is set to INDEF, semi-major axis 
  grow is stopped and the algorithm proceeds inwards to the galaxy image center. 
  If 'geompar.maxsma' is set to some finite value, and this value is larger than 
  the current semi-major axis length, the algorithm enters non-iterative mode 
  and proceeds outwards until reaching 'geompar.maxsma'.
  </p>
  <p>
  Non-iterative mode can also be entered if the ellipse center wanders from
  its former position by an amount larger than parameter 'wander'. 
  </p>
  <p>
  In non-iterative mode, the ellipse geometry parameters (center, ellipticity, 
  position angle) are kept fixed at their last fitted values. This may be useful 
  for sampling regions of very low surface brightness, where the algorithm may 
  become unstable and unable to recover reliable geometry information from isophotes. Non-iterative mode can be entered also if the ellipticity exceeds 
  1.0 or the ellipse center crosses the image boundaries.
  </p>
  <p>
  The <span style="font-family: monospace;">"soft stop"</span> feature is provided as a help in overcoming premature
  stopping by the 'maxgerr' criterion when measuring complex images that
  may trigger the criterion because of, e.g. contamination due to stars,
  HII regions and the like. The gradient error may become artificially
  large in an <span style="font-family: monospace;">"isophote"</span> with such contamination, despite the fact that outer
  isophotes still exist with enough signal-to-noise to be properly measured.
  When the 'soft' flag is set to 'yes', the 'maxgerr' criterion will be
  triggered only by two consecutive isophotes having their gradient errors
  exceeding 'maxgerr'.
  </p>
  <p>
  Parameters 'hcenter', 'hellip' and 'hpa' are provided for holding the
  ellipse geometry parameters fixed, effectively removing them from the 
  fit process. Note that, if the 'geompar.recenter' parameter is set to
  <span style="font-family: monospace;">"yes"</span>, recentering of the first fitted ellipse will take place even if
  'hcenter' is set to <span style="font-family: monospace;">"yes"</span>.
  </p>
  <p>
  In some cases the object locator algorithm mail fail, even though there
  is enough signal-to-noise to start a fit (e.g. in objects with very
  high ellipticity). In those cases the sensitivity of the algorithm
  can be decreased, or it can even be turned off, by lowering the value 
  of parameter 'olthresh'.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>(conver = 0.05) [real, min=0.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(conver = 0.05) [real, min=0.0]' -->
  <dd>Convergency criterion. Largest harmonic amplitude must be smaller than
  'conver' times the fit rms.
  </dd>
  </dl>
  <dl>
  <dt><b>(minit = 10) [int, min=1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(minit = 10) [int, min=1]' -->
  <dd>Minimum number of iterations at each isophote.
  </dd>
  </dl>
  <dl>
  <dt><b>(maxit = 50) [int, min=2]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(maxit = 50) [int, min=2]' -->
  <dd>Maximum number of iterations at each isophote.
  </dd>
  </dl>
  <dl>
  <dt><b>(hcenter = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(hcenter = no) [boolean]' -->
  <dd>Hold ellipse center fixed during the fit ?
  </dd>
  </dl>
  <dl>
  <dt><b>(hellip = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(hellip = no) [boolean]' -->
  <dd>Hold ellipticity fixed during the fit ?
  </dd>
  </dl>
  <dl>
  <dt><b>(hpa = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(hpa = no) [boolean]' -->
  <dd>Hold position angle fixed during the fit ?
  </dd>
  </dl>
  <dl>
  <dt><b>(wander = INDEF) [real, min=0.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wander = INDEF) [real, min=0.0]' -->
  <dd>Limit for ellipse center wandering (in pixels). INDEF disables this control.
  </dd>
  </dl>
  <dl>
  <dt><b>(maxgerr = 0.5) [real, min=0.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(maxgerr = 0.5) [real, min=0.0]' -->
  <dd>Maximum acceptable gradient relative error.
  </dd>
  </dl>
  <dl>
  <dt><b>(olthresh = 1.0) [real, min=0.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(olthresh = 1.0) [real, min=0.0]' -->
  <dd>Threshold for the object locator algorithm. By lowering this value the 
  object locator becomes less strict, in the sense that it will accept lower
  signal-to-noise data. If set to zero, the 'x0', 'y0' values found in
  the 'geompar' pset are used without questioning.
  </dd>
  </dl>
  <dl>
  <dt><b>(soft = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(soft = no) [boolean]' -->
  <dd>Soft stop ?
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ellipse
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

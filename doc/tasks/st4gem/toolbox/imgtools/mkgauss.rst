.. _mkgauss:

mkgauss: Generate a 2-D image having an object of Gaussian type.
================================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkgauss outim n1 n2 pos1 pos2 amp sigma1 sigma2 fwhm1 fwhm2 rms
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This is a task for generating a 2-D image having an object of Gaussian type
  (Gaussian function). Zero-mean Gaussian white noise may be added. 
  </p>
  <p>
  For the Gaussian function, if `sigma1` is zero, then `fwhm1` 
  will be used and `sigma1` 
  will be ignored. Otherwise `sigma1` will be used 
  and `fwhm1` will be ignored. They are related by 
  `sigma1` = `fwhm1` / sqrt(8ln2).
  Enter a small value, say 1.0E-4, for `sigma1` to virtually set it to
  zero, but `sigma1` is used. This rule is also applicable to 
  `sigma2` and `fwhm2`.
  </p>
  <p>
  This task can be used in conjunction with other tasks to make
  images having simple patterns.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_outim">
  <dt><b>outim [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outim' Line='outim [file name]' -->
  <dd>Output image name.
  </dd>
  </dl>
  <dl id="l_n1">
  <dt><b>n1, n2 [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='n1' Line='n1, n2 [integer]' -->
  <dd>Image sizes in the first (x) and second (y) dimensions.
  </dd>
  </dl>
  <dl id="l_pos1">
  <dt><b>pos1, pos2 [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pos1' Line='pos1, pos2 [real]' -->
  <dd>Gaussian function's central positions in the first and second dimensions.
  </dd>
  </dl>
  <dl id="l_amp">
  <dt><b>amp [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='amp' Line='amp [real]' -->
  <dd>Peak amplitude of the Gaussian function.
  </dd>
  </dl>
  <dl id="l_sigma1">
  <dt><b>sigma1, sigma2 [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma1' Line='sigma1, sigma2 [real]' -->
  <dd>Gaussian function's sigmas in the first and second dimensions.
  </dd>
  </dl>
  <dl id="l_fwhm1">
  <dt><b>fwhm1, fwhm2 [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fwhm1' Line='fwhm1, fwhm2 [real]' -->
  <dd>Gaussian function's full widths at half maximum in the first
  and second dimensions.
  </dd>
  </dl>
  <dl id="l_rms">
  <dt><b>rms [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rms' Line='rms [real]' -->
  <dd>Rms value of Gaussian noise.
  </dd>
  </dl>
  <dl id="l_seed">
  <dt><b>seed=347951 [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='seed' Line='seed=347951 [integer]' -->
  <dd>Seed for generating the noise.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  We do not recommend that you enter parameters on the command line,
  as shown in the example below---use 'epar' instead.
  </p>
  <p>
  1. Generate a 128x128 noise-free point spread function of Gaussian type,
  which is centrally located (at (65,65)) and normalized so that its maximum 
  is one, and has sigmas equal to 2 in the both dimensions. (x: don't care
  about the value.) Use any file name you like for outim.
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; mkgauss outim 128 128 65 65 1 2 2 x x 0
  </pre></div>
  <p>
  2. Generate a point spread function same as in 1., but
  has FWHMs equal to 2 in the both dimensions.
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  me&gt;mkgauss outim 128 128 65 65 1 0 0 2 2 0
  </pre></div>
  <p>
  3. Generate a delta function at the center.
  </p>
  <div class="highlight-default-notranslate"><pre>
  me&gt;mkgauss outim 128 128 65 65 1 0 0 0 0 0
  </pre></div>
  <p>
  4. Generate a noise-free function with zero values everywhere 
  except along a line segment parallel to the x-axis
  (centrally located 1-D Gaussian function with peak=1, sigma=3).
  </p>
  <div class="highlight-default-notranslate"><pre>
  me&gt;mkgauss outim 128 128 65 65 1 3 0 x 0 0
  </pre></div>
  <p>
  5. Same as in 4., but the line segment is now parallel to the y-axis.
  </p>
  <div class="highlight-default-notranslate"><pre>
  me&gt;mkgauss outim 128 128 65 65 1 1e-4 3 x x 0
  </pre></div>
  <p>
  6. Generate a noise-only image with rms=2, seed=919191
  (zero-mean Gaussian white noise).
  </p>
  <div class="highlight-default-notranslate"><pre>
  me&gt;mkgauss outim 128 128 x x 0 x x x x 2 seed=919191
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
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _sigmanorm:

sigmanorm: Renormalize mosaic image to uniform pixel-to-pixel rms
=================================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  sigmanorm input expmap output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The name of the input image.
  </dd>
  </dl>
  <dl id="l_expmap">
  <dt><b>expmap</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expmap' Line='expmap' -->
  <dd>The name of the input exposure map image.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The name of the output normalized image.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  SIGMANORM divides the input image <i>input</i> by a factor equal to the
  square root of the exposure map image <i>expmap</i> divided by the the
  maximum exposure value to create the output normalized image <i>output</i>
  which has a uniform pixel-to-pixel rms noise. 
  </p>
  <p>
  SIGMANORM is currently used by the MKMASK task.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create a normalized input image for a first pass mosaic image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sigmanorm fp_mosaic exp_fp_mosaic norm_fp_mosaic
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
  mkmask
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _quadscale:

quadscale: Scale sections by gain factors
=========================================

**Package: quadred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  quadscale input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input image in <b>quadformat</b> to be scaled.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output scaled image in <b>quadformat</b>.
  </dd>
  </dl>
  <dl id="l_gain11">
  <dt><b>gain11 = 1., gain12 = 1., gain21 = 1., gain22 = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gain11' Line='gain11 = 1., gain12 = 1., gain21 = 1., gain22 = 1.' -->
  <dd>Gain factors for each quadrant.
  </dd>
  </dl>
  <dl id="l_operation">
  <dt><b>operation = <span style="font-family: monospace;">"multiply"</span> (multiply|divide)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='operation' Line='operation = "multiply" (multiply|divide)' -->
  <dd>The operation to apply with the gains.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task multiplies or divides by gain factors for each amplifier in
  <b>quadformat</b>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To multiply by different gain factors.
  </p>
  <div class="highlight-default-notranslate"><pre>
  qu&gt; quadscale quad0072 test gain11=1.2 gain12=1.3 gain21=1.4
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  quadformat
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

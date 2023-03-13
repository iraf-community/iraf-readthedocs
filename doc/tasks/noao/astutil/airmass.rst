.. _airmass:

airmass: Compute the airmass at a given elevation above the horizon
===================================================================

**Package: astutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  airmass elevation
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_elevation">
  <dt><b>elevation</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='elevation' Line='elevation' -->
  <dd>Elevation above horizon in either degrees or radians.
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = 750.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = 750.0' -->
  <dd>Scale factor of the Earth's atmosphere.
  </dd>
  </dl>
  <dl id="l_radians">
  <dt><b>radians = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radians' Line='radians = no' -->
  <dd>Input elevation in radians instead of degrees.
  </dd>
  </dl>
  <dl id="l_airmass">
  <dt><b>airmass</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='airmass' Line='airmass' -->
  <dd>On output, contains the computed airmass.
  </dd>
  </dl>
  </section>
  <section id="s_example">
  <h3>Example</h3>
  <p>
  Compute the airmass at an elevation of 30 degrees above the horizon
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; airmass 30
  airmass 1.996 at an elevation of 30. degrees (0.5236 radians)
  above horizon
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'EXAMPLE'  -->
  

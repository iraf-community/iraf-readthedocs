.. _lumatch:

lumatch: Match the lookup tables of two frames
==============================================

**Package: iis**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  lumatch frame ref_frame
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_frame">
  <dt><b>frame</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='frame' Line='frame' -->
  <dd>Frame whose lookup table is to be adjusted.
  </dd>
  </dl>
  <dl id="l_ref_frame">
  <dt><b>ref_frame</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ref_frame' Line='ref_frame' -->
  <dd>Frame whose lookup table is to be matched.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The lookup tables mapping the display frame values to the grey levels
  on the display monitor are matched in one frame to a reference frame.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To match the lookup tables in frame 3 to those in frame 1:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lumatch 3 1
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  cv
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

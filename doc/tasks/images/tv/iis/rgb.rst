.. _rgb:

rgb: Select true color mode (red, green, and blue frames)
=========================================================

**Package: iis**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rgb red_frame green_frame blue_frame
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_red_frame">
  <dt><b>red_frame</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='red_frame' Line='red_frame' -->
  <dd>Frame to use for the red component.
  </dd>
  </dl>
  <dl id="l_green_frame">
  <dt><b>green_frame</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='green_frame' Line='green_frame' -->
  <dd>Frame to use for the green component.
  </dd>
  </dl>
  <dl id="l_blue_frame">
  <dt><b>blue_frame</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blue_frame' Line='blue_frame' -->
  <dd>Frame to use for the blue component.
  </dd>
  </dl>
  <dl id="l_window">
  <dt><b>window = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='window' Line='window = no' -->
  <dd>Window the rgb lookup tables?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Set the display monitor to display rgb colors by using three frames to
  drive the red, green, and blue guns of the color display monitor.
  Optionally, window the rgb lookup tables.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rgb 1 2 3
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  cv
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

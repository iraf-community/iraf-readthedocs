.. _stdgraph:

stdgraph: Plot metacode on the standard graphics device
=======================================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  stdgraph input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The input metacode, may be a list of files or redirected STDIN.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "stdgraph"' -->
  <dd>The terminal type.
  </dd>
  </dl>
  <dl id="l_generic">
  <dt><b>generic = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='generic' Line='generic = no' -->
  <dd>The remaining parameters are ignored if <b>generic</b> = yes.
  </dd>
  </dl>
  <dl id="l_debug">
  <dt><b>debug = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='debug' Line='debug = no' -->
  <dd>When <b>debug</b> = yes, the decoded plotting instructions are printed
  during processing.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>If <b>verbose</b> = yes, elements of polylines and cell array calls are 
  printed in debug mode.
  </dd>
  </dl>
  <dl id="l_gkiunits">
  <dt><b>gkiunits = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gkiunits' Line='gkiunits = no' -->
  <dd>In debug mode, coordinates can be printed in GKI rather than NDC units.
  </dd>
  </dl>
  <dl id="l_txquality">
  <dt><b>txquality = <span style="font-family: monospace;">"normal"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='txquality' Line='txquality = "normal"' -->
  <dd>The character drawing quality.
  </dd>
  </dl>
  <dl id="l_xres">
  <dt><b>xres = 0, yres= 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xres' Line='xres = 0, yres= 0' -->
  <dd>The number of resolution elements in x and y
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <i>stdgraph</i> translates GKI metacode and draws a plot on a
  graphics terminal.  Input to
  <i>stdgraph</i> is GKI metacode, which can be read from one or more 
  metacode files or redirected from the standard input.  
  </p>
  <p>
  Parameters 
  <b>txquality</b>, <b>xres</b>, and <b>yres</b> are used to override the
  values for text quality, and x and y resolution already in the metacode.
  Values for <b>txquality</b> are chosen from normal, low, medium or high.
  High quality characters are software generated, and can be of any size.
  </p>
  <p>
  If <b>debug</b> is set to yes, the plotting instructions are printed in
  readable form as the metacode is processed.  In debug mode, GKI 
  instructions can be printed in verbose mode, where the elements of
  polylines and cell arrays are printed in addition to the default output.
  Coordinates can be printed in either GKI (0 - 32767) or NDC (0.0 - 1.0)
  units.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Extract the fourth frame from metacode file <span style="font-family: monospace;">"plots.mc"</span> and plot it.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gkiextract plots.mc 4 | stdgraph
  </pre></div>
  <p>
  2. Process file <span style="font-family: monospace;">"one.mc"</span> in debug mode.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stdgraph oned.mc debug+
  </pre></div>
  <p>
  3. Plot file <span style="font-family: monospace;">"oned.mc"</span> with high quality text generation.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stdgraph oned.mc txquality=high
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  gkiextract,  stdplot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

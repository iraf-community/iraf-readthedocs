.. _stdplot:

stdplot: Plot metacode on the standard plotter device
=====================================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  stdplot input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input metacode files.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"stdplot"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "stdplot"' -->
  <dd>The type of plotting device.
  </dd>
  </dl>
  <dl id="l_generic">
  <dt><b>generic = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='generic' Line='generic = no' -->
  <dd>The remaining parameters are ignored when <b>generic</b> = yes.
  </dd>
  </dl>
  <dl id="l_debug">
  <dt><b>debug = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='debug' Line='debug = no' -->
  <dd>If <b>debug</b> = yes, the graphics instructions are decoded and printed
  during processing.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>If <b>verbose</b> = yes, the elements of polylines, cell arrays, etc. will
  be printed in debug mode.
  </dd>
  </dl>
  <dl id="l_gkiunits">
  <dt><b>gkiunits = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gkiunits' Line='gkiunits = no' -->
  <dd>By default, coordinates are printed in NDC rather than GKI units.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <i>stdplot</i> translates metacode and draws it on a plotting
  device.
  Input is GKI metacode, which can be read from one or more binary
  files or redirected from the standard input.
  </p>
  <p>
  If <b>debug</b> is set to yes, the plotting instructions are printed in
  readable form during processing.
  If <b>verbose</b> = yes, elements of polyline and cell array calls are
  printed in addition to the default debug output.
  Coordinates can be printed in either GKI (0 - 32767) or NDC (0.0 - 1.0)
  units.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Extract the fourth frame from metacode file <span style="font-family: monospace;">"oned.mc"</span> and plot it.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gkiextract oned.mc 4 | stdplot
  </pre></div>
  <p>
  2. Plot metacode frame <span style="font-family: monospace;">"contour.demo"</span> in debug mode, so the plotting
  instructions can be read as they are processed.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stdplot contour.demo debug+
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  gkiextract stdgraph
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

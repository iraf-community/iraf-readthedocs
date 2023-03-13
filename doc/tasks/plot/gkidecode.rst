.. _gkidecode:

gkidecode: Decode metacode on the standard output
=================================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  gkidecode input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The input metacode, which can be read from a list of files or
  redirected from the standard input.
  </dd>
  </dl>
  <dl id="l_generic">
  <dt><b>generic = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='generic' Line='generic = no' -->
  <dd>The remaining parameters are ignored when <b>generic</b> = yes.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>If <b>verbose</b> = yes, the elements of polylines, cell arrays, etc. will
  be printed.
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
  Task <b>gkidecode</b> is a debugging tool used to decode GKI metacode
  files.  The plotting instructions are decoded and printed in readable 
  form on the standard output.  The input metacode can be read from one
  or more files or redirected from the standard input.
  </p>
  <p>
  If <b>verbose</b> = yes, elements of polyline and cell array calls are
  printed in addition to the default output.
  Coordinates can be printed in either GKI (0 - 32767) or NDC (0.0 - 1.0)
  units.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Decode the metacode instructions in file crtpict.mc in verbose mode.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gkidecode crtpict.mc verbose+
  </pre></div>
  <p>
  2. Print a shorter listing of the same file on the versatec.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gkidecode crtpict.mc | lprint dev=ver
  </pre></div>
  <p>
  3. Decode the third frame in metacode file <span style="font-family: monospace;">"oned.mc"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gkiextract oned.mc 3 | gkidecode
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  stdgraph stdplot 
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

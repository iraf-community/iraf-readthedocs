.. _sgidecode:

sgidecode: Decode an SGI format metacode file
=============================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  sgidecode input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The input SGI metacode files.
  </dd>
  </dl>
  <dl id="l_generic">
  <dt><b>generic = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='generic' Line='generic = no' -->
  <dd>Ignore remaining parameters?
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print metacode in a verbose format?
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
  Task <i>sgidecode</i> is a debugging tool used to decode SGI metacode
  files.  The plotting instructions are decoded and printed in readable
  form on the standard output.  The input metacode can be read from one
  or more files or redirected from the standard input.
  </p>
  <p>
  Coordinates are printed in NDC units (0-1) by default.  When <b>gkiunits</b>
  = yes, coordinates are printed in gki units (0-32767).  Parameter
  <b>verbose</b> is currently not implemented.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Decode the metacode in file <span style="font-family: monospace;">"home$vdm.sgi"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sgidecode home$vdm.sgi
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  gkidecode sgikern
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

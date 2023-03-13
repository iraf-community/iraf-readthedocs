.. _show:

show: Show an environment variable
==================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  show [varname]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_varname">
  <dt><b>varname</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='varname' Line='varname' -->
  <dd>The name of the environment variable to be displayed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>show</i> command shows the current values of all defined environment
  variables if called with no arguments, or the value of a specific variable
  if an argument is given.  Unlike <i>set</i>, only current values are shown,
  not the entire history of the definitions of environment variables.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Show the current default printer device.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; show printer
  </pre></div>
  <p>
  2. Show all <span style="font-family: monospace;">"std"</span> (standard i/o stream) related variables.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; show | match std
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  set
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

.. _envget:

envget: Get the string value of an environment variable
=======================================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  envget varname
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_varname">
  <dt><b>varname</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='varname' Line='varname' -->
  <dd>The environment variable whose value is to be returned.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Envget</i> returns the string value of the named environment variable.
  The user is prompted for the value if the variable has not yet been defined.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Construct a filename using the value of the environment variable
  <span style="font-family: monospace;">"editor"</span>, and page the file thus named.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; page ("dev$" // envget ("editor") // ".ed")
  </pre></div>
  <p>
  2. Compute and print the center line on the terminal screen.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; = ((int (envget ("ttynlines")) + 1) / 2)
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  set, show
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

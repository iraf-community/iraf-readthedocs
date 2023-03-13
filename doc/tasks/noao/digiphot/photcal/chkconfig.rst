.. _chkconfig:

chkconfig: Check the configuration file for grammar and syntax errors
=====================================================================

**Package: photcal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  chkconfig config
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_config">
  <dt><b>config</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='config' Line='config' -->
  <dd>The name of the configuration file to be checked. <i>Config</i> is the
  text file specifying both the format of the input files, and the form of
  transformation equations.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print detailed diagnostic information on the standard output ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  CHKCONFIG parses the configuration file <i>config</i> line by line,
  searching for syntax and/or semantic errors.  Its primary function is to aid
  the user in setting up a complete and correct set of transformation
  equations to be fit.  CHKCONFIG is run automatically by the task MKCONFIG,
  but can also be run stand-alone at any time.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Check the configuration file for grammar and syntax errors.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; chk config
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mkconfig,fitparams
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

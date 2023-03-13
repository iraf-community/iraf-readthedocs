.. _detab:

detab: Replace tabs with tabs and blanks
========================================

**Package: utilities**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  detab files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>Template specifying files to be processed e.g. <span style="font-family: monospace;">"file1"</span> or <span style="font-family: monospace;">"file*"</span>.
  </dd>
  </dl>
  <dl id="l_tablist">
  <dt><b>tablist = <span style="font-family: monospace;">"9 +8"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tablist' Line='tablist = "9 +8"' -->
  <dd>String containing a list of tabstops separated by blanks or commas.
  Alternatively a two element string of the form m +n will set
  tabstops every n columns beginning in column m.  A null string will
  default to <span style="font-family: monospace;">"9 +8"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_example">
  <h3>Example</h3>
  <p>
  Remove the tabs from file <span style="font-family: monospace;">"cubspl.f"</span>, using the default tab stops.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; detab cubspl.f &gt; temp
  cl&gt; delete cubspl.f
  cl&gt; rename temp cubspl.f
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'EXAMPLE'  -->
  

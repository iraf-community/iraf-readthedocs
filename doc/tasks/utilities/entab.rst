.. _entab:

entab: Replace blanks with tabs and blanks
==========================================

**Package: utilities**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  entab files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>Template specifying the files to be processed, e.g. <span style="font-family: monospace;">"file"</span> or <span style="font-family: monospace;">"file*"</span>.
  </dd>
  </dl>
  <dl id="l_tablist">
  <dt><b>tablist = <span style="font-family: monospace;">"9 +8"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tablist' Line='tablist = "9 +8"' -->
  <dd>String containing a list of tabstops separated by blanks or commas.
  A two element string of the form <span style="font-family: monospace;">"m +n"</span> will set
  tabstops in every n columns beginning in column m.
  A null string defaults to <span style="font-family: monospace;">"9 +8"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_example">
  <h3>Example</h3>
  <p>
  Convert the file <span style="font-family: monospace;">"prog.c"</span>, written using full tabstop indents, to
  an equivalent file with an initial indent of one full tabstop, 
  with 4 space indents thereafter.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; detab prog.c tab='9 +4' | entab &gt; temp
  cl&gt; delete prog.c
  cl&gt; rename temp prog.c
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'EXAMPLE'  -->
  

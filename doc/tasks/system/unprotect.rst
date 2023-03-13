.. _unprotect:

unprotect: Remove delete protection from a file
===============================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  unprotect files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>A template specifying the file or files from which delete protection is
  to be removed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Unprotect</i> removes delete protection from the named files.
  A <span style="font-family: monospace;">"protected"</span> file cannot be deleted or clobbered.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Remove file protection from the listed files.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; unprotect alpha,beta,gamma.x,*.db
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  protect, delete
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

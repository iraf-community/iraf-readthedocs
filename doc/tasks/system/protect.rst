.. _protect:

protect: Protect a file from deletion
=====================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  protect files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>A template specifying the file or files to be protected.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Protect</i> asserts protection from deletion for the specified files.
  A protected file can be deleted only by first <span style="font-family: monospace;">"unprotecting"</span> it.
  File protection is preserved when a file is copied or renamed,
  even when copied or renamed to a remote network node,
  but may be lost when a file is backed up on tape and later restored
  (depending upon what utility one uses).  Note that imagefiles are
  automatically protected to prevent accidental deletion of the header
  file, leaving a <span style="font-family: monospace;">"zombie"</span> pixel file somewhere on disk.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Protect the file <span style="font-family: monospace;">"paper.ms"</span> from deletion, accidental or otherwise.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; protect paper.ms
  </pre></div>
  <p>
  2. Protect all the <span style="font-family: monospace;">".ms"</span> files from deletion.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; protect *.ms
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  unprotect, delete
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

.. _txtbin:

txtbin: Convert an IRAF text file to a binary file
==================================================

**Package: dataio**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  txtbin text_file binary_file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_text_file">
  <dt><b>text_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='text_file' Line='text_file' -->
  <dd>Input file name or template, e.g. <span style="font-family: monospace;">"abc"</span> or <span style="font-family: monospace;">"abc.*"</span>.
  </dd>
  </dl>
  <dl id="l_binary_file">
  <dt><b>binary_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='binary_file' Line='binary_file' -->
  <dd>Output file name. If multiple input files the file_number will be
  added to the output file name.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = <span style="font-family: monospace;">"yes"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = "yes"' -->
  <dd>Print messages about files processed?
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convert a text file on disk to a binary file on disk.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; txtbin text_file binary_file
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  bintxt
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'EXAMPLES' 'SEE ALSO'  -->
  

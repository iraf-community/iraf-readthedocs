.. _bintxt:

bintxt: Convert a binary file to an IRAF text file
==================================================

**Package: dataio**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  bintxt binary_file text_file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_binary_file">
  <dt><b>binary_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='binary_file' Line='binary_file' -->
  <dd>Input file name or template,  e.g. <span style="font-family: monospace;">"file1"</span> or <span style="font-family: monospace;">"file*"</span>.
  </dd>
  </dl>
  <dl id="l_text_file">
  <dt><b>text_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='text_file' Line='text_file' -->
  <dd>The output file name.  If multiple input files the filenumber will
  be concatenated onto the output file name.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages of actions performed?
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convert a binary file on disk to a text file on disk.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bintxt binary_file text_file
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  txtbin
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'EXAMPLES' 'SEE ALSO'  -->
  

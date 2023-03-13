.. _lcase:

lcase: Convert a file to lower case
===================================

**Package: utilities**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  lcase files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>The list of text files to be converted to lower case. If more than one
  text file is specified as input the suffix .lc is appended to the input
  file name to create the output file name.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  LCASE takes input from a list of text files or the standard input, converts
  the text to lower case and prints the result on the standard output.
  If multiple files are specified as input, the suffix .lc is appended to
  the input file name to create the output file name.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convert a list of files to lower case
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lcase *.x
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ucase
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

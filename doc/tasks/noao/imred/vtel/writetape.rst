.. _writetape:

writetape: Cl script to write 5 full disk grams to tape.
========================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  writetape input_root tape_name
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_getname">
  <dt><b>getname</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='getname' Line='getname' -->
  <dd>Root name for input files.
  </dd>
  </dl>
  <dl id="l_getmtape">
  <dt><b>getmtape</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='getmtape' Line='getmtape' -->
  <dd>Tape file descriptor.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Writetape takes as input five(5) full disk grams in IRAF image format
  and writes them to tape in a format identical to the original full disk
  grams produced on the vacuum telescope.  The input image names are expected
  to be the <span style="font-family: monospace;">"input_root"</span> name concatenated with the numbers <span style="font-family: monospace;">"1"</span>, <span style="font-family: monospace;">"2"</span>, ... <span style="font-family: monospace;">"5"</span>.
  Writetape calls 'writevt' and is a cl script file.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To write five files with root name m1585 to tape mta, the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; writetape m1585 mta
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  readvt, writevt
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

.. _head:

head: Print the first few lines of a text file
==============================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  head files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>The list of files to be dealt with, quite possibly given as
  a template, such a <span style="font-family: monospace;">"image*"</span>.
  </dd>
  </dl>
  <dl id="l_nlines">
  <dt><b>nlines = 12</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlines' Line='nlines = 12' -->
  <dd>The number of lines to be printed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Head</i> prints, on the standard output, the first <i>nlines</i> of each
  file that matches the given file list.  If the file list has more than one
  name in it, a short header precedes each listing.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print the first 12 lines of each help file in the current directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; head *.hlp
  </pre></div>
  <p>
  2. Print the first line of each help file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; head *.hlp nl=1
  </pre></div>
  <p>
  3. Print the most recently defined <i>set</i> environment definitions.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set | head
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  tail, page
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

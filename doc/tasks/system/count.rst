.. _count:

count: Count the number of lines, words, characters in a text file
==================================================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  count files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>A template specifying the files to be examined.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  For each file, count determines the number of lines, words, and
  characters in the file.  A word is defined as a sequence of characters
  delimited by one or more blanks or tabs, or by the end of a line.
  If <i>count</i> is run on more than one file, each output line is identified
  by the file name, and a final output line gives the total number
  of lines, words, and characters in all files.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Count the number of lines, words and characters in all files in the
  current directory with the extensions <span style="font-family: monospace;">".x"</span> and <span style="font-family: monospace;">".h"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; count *.[xh]
  </pre></div>
  <p>
  2. Count the number of .x files in the current directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dir *.x op=1 | count
  </pre></div>
  <p>
  3. Count the number of <i>set</i> environment definitions.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set | count
  </pre></div>
  <p>
  4. Count the number of references to the READ function in all .x files in
  the current directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; match "read#(" *.x | count
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  directory
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

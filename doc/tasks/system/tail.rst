.. _tail:

tail: Print the last few lines of a file
========================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tail files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>A template specifying the files to be listed.
  </dd>
  </dl>
  <dl id="l_nlines">
  <dt><b>nlines = 12</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlines' Line='nlines = 12' -->
  <dd>The number of lines to be printed.  If negative, the number
  of lines to be skipped, counting from the beginning of the file.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  For each file in the input file list, <i>tail</i> copies the last <i>nlines</i>
  of the file to the standard output.  If there is more than one file in the
  input file list, as one line header is printed before each file.
  If <span style="font-family: monospace;">"nlines"</span> is negative, then abs(nlines) lines are skipped, and the rest
  of the file is printed, i.e., the tail of the file is still printed, but
  the offset is measured from the beginning of the file rather than the end.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Prints the last 12 lines of each help file in the current directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tail *.hlp
  </pre></div>
  <p>
  2. Print the last line of each help file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tail *.hlp nl=1
  </pre></div>
  <p>
  3. Prints the third through fifth lines of <span style="font-family: monospace;">"file"</span>.  The same thing
  might be done (at least conceptually) by <span style="font-family: monospace;">"head file,nlines=5"</span>
  piped into <span style="font-family: monospace;">"tail ,nlines=3"</span>.  However, <i>tail</i> does not work on STDIN.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tail file nl=-2 | head nl=3
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  <i>Tail</i> does not presently work on standard input, and therefore cannot
  be used in pipes.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  head
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

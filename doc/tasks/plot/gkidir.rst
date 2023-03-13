.. _gkidir:

gkidir: Directory listing of metacode file
==========================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  gkidir input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The metacode file or files to be examined.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <b>gkidir</b> examines GKI metacode files, and prints a directory of
  the plots contained in each input file.  Each plot is listed with its
  size and an identifying title string.  The title string is the MFTITLE
  string if given, or else the longest GTEXT string found (hopefully the
  plot title), or else the string <span style="font-family: monospace;">"(no title)"</span>.  The output format is as
  follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  file1:
      [1] (1234 words)    title_string
      [2] (78364 words)   title_string
  
  file2:
      [1] (874 words)     title_string
          .
          .
          .
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the plots in the GKI metacode file <span style="font-family: monospace;">"file"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gkidir file
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  gkiextract
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

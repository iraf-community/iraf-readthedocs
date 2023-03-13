.. _sort:

sort: Sort a text file
======================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  sort input_file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input_file">
  <dt><b>input_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input_file' Line='input_file' -->
  <dd>The text file to be sorted.  If the standard input is redirected the standard
  input is sorted.
  </dd>
  </dl>
  <dl id="l_column">
  <dt><b>column = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='column' Line='column = 0' -->
  <dd>If 0, sort entire text lines, else sort based on data/text starting
  in the specified column.  Columns are delimited by whitespace.  Thus,
  <div class="highlight-default-notranslate"><pre>
  12   abc   34   56
  </pre></div>
  has four columns, <span style="font-family: monospace;">"abc"</span> being in the second.
  </dd>
  </dl>
  <dl id="l_ignore_whitespace">
  <dt><b>ignore_whitespace = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ignore_whitespace' Line='ignore_whitespace = no' -->
  <dd>Ignore leading whitespace.  Useful only when column = 0 and the sort is
  non-numeric.
  </dd>
  </dl>
  <dl id="l_numeric_sort">
  <dt><b>numeric_sort = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='numeric_sort' Line='numeric_sort = no' -->
  <dd>If set, make numerical (rather than ASCII text) comparisons.
  </dd>
  </dl>
  <dl id="l_reverse_sort">
  <dt><b>reverse_sort = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reverse_sort' Line='reverse_sort = no' -->
  <dd>If set, sort in reverse text/numeric order.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Sort</i> sorts the contents of the given text file, or the
  standard input, either on a textual (based on the ASCII collating
  sequence), or on a numeric basis.  If a numeric sort is requested,
  and either field in any comparison is non-numeric, a string (ASCII)
  comparison will be made instead.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Sort the output of the set command into alphabetic (ASCII collating)
  order.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set | sort
  </pre></div>
  <p>
  2. Sort the contents of <span style="font-family: monospace;">"file"</span>, in reverse ASCII order, ignoring the
  contents of columns 1 through 4.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sort file rev+ col=5
  </pre></div>
  <p>
  3. Print a long form directory listing with the files sorted by size,
  largest files first.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dir | sort num+ rev+ col=3
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Only one file can be sorted per call, and only one column or all columns can
  be used for the sort.  The current program is inefficient for large numeric
  sorting tasks because the same numeric field may be decoded into its
  corresponding binary value many times.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS'  -->
  

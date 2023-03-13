.. _table:

table: Format a list of words into a table
==========================================

**Package: lists**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  table input_files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input_files">
  <dt><b>input_files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input_files' Line='input_files' -->
  <dd>List of files to be formatted, may be STDIN.
  </dd>
  </dl>
  <dl id="l_first_col">
  <dt><b>first_col = 7</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='first_col' Line='first_col = 7' -->
  <dd>Offset to first column of table
  </dd>
  </dl>
  <dl id="l_last_col">
  <dt><b>last_col = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='last_col' Line='last_col = 0' -->
  <dd>Offset to last column of table.  The value <b>last_col</b> = 0 indicates 
  right margin.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = 0' -->
  <dd>Number of columns.  The value <b>ncols</b> = 0 indicates maximum that will fit.
  </dd>
  </dl>
  <dl id="l_maxstrlen">
  <dt><b>maxstrlen = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxstrlen' Line='maxstrlen = 0' -->
  <dd>Maximum string length for table entry.  The value <b>maxstrlen</b> = 0
  indicates no limit.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <b>table</b> reads a list of strings from the standard input or a 
  list of files and assembles a nicely formatted table.  If reading 
  from multiple input files, make a separate table for each.  There is no 
  fixed limit to the size of the table which can be formatted.  The table 
  is not sorted; this should be done as a separate operation if desired.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Format a file containing names into a two column table.  The table is 
  sorted alphabetically first.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sort names | table ncols=2
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  words, tokens
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

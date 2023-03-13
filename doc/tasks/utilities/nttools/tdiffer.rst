.. _tdiffer:

tdiffer: Form a table which is the difference of two tables.
============================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tdiffer intable1 intable2 outtable colnam1 colnam2
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task creates an output table containing all the rows of the first table
  which do not match the rows in the second table.
  The first, second, and output tables are given by the task
  parameters 'intable1', 'intable2', and 'outtable' respectively.
  The match is done on the columns specified by the task parameters 'colnam1'
  and 'colnam2'.
  Other columns are ignored.
  If the two tables are disjoint, the output table will be a copy of
  the first table, except the rows will be sorted.
  If the first table is a subset of the second, the output table will be empty.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable1">
  <dt><b>intable1 [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable1' Line='intable1 [file name]' -->
  <dd>The name of the first input table.
  </dd>
  </dl>
  <dl id="l_intable2">
  <dt><b>intable2 [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable2' Line='intable2 [file name]' -->
  <dd>The name of the second input table.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [file name]' -->
  <dd>The name of the output table.  The output table has the same header parameters
  and column names as the first table. 
  </dd>
  </dl>
  <dl id="l_colnam1">
  <dt><b>colnam1 [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='colnam1' Line='colnam1 [string]' -->
  <dd>The column names in the first table used in the match.  If more than one
  column is used, columns from the first and second
  table are associated with each other based on their position in the list
  and not on their names, i.e., the first column name in 'colnam1' is matched
  to the first column name passed to 'colnam2', regardless of whether the
  names match.
  </dd>
  </dl>
  <dl id="l_colnam2">
  <dt><b>colnam2 [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='colnam2' Line='colnam2 [string]' -->
  <dd>The column names in the second table used in the match.  The same number of
  column names must be passed to both the 'colnam1' and 'colnam2' parameters.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. There are two tables, <span style="font-family: monospace;">"targets.tab"</span>, containing a list of targets
  for observation, and <span style="font-family: monospace;">"images.tab"</span>, containing a list of targets which
  have already been observed.  Create a table named <span style="font-family: monospace;">"new.tab"</span> containing
  those targets which have not previously been observed:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tdiffer targets.tab images.tab new.tab targetid targetid
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Bernie Simon.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  tselect
  </p>
  <p>
  Type <span style="font-family: monospace;">"help tables opt=sys"</span> for a higher-level description of the 'tables' 
  package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

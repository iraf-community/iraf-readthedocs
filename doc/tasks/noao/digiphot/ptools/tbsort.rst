.. _tbsort:

tbsort: Sort a list of apphot/daophot tables databases
======================================================

**Package: ptools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tbsort table columns
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table' -->
  <dd>The list of APPHOT/DAOPHOT table databases to be sorted in-place.
  All tables are sorted on the same column or columns.
  </dd>
  </dl>
  <dl id="l_columns">
  <dt><b>columns</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='columns' Line='columns' -->
  <dd>The list of columns to sort on.  A column template consists of a list of
  either column names, or column patterns containing the usual pattern matching
  meta-characters.  The names or patterns are separated by commas or white space.
  The list can be placed in a file and the name of the file preceeded by a
  <span style="font-family: monospace;">'@'</span> can be given in place of the column template.
  </dd>
  </dl>
  <dl id="l_ascend">
  <dt><b>ascend = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ascend' Line='ascend = yes' -->
  <dd>If <i>ascend</i> = yes, the table is sorted in ascending value order, with the
  first
  row containing the smallest value of the sorted column.  Otherwise, the table
  is sorted in descending order, with the largest value first.
  </dd>
  </dl>
  <dl id="l_casesens">
  <dt><b>casesens = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='casesens' Line='casesens = yes' -->
  <dd>If <i>casesens</i> = yes, sorts on character columns are case sensitive,
  with upper case letters preceding lower case in the sort.
  Otherwise, the sort is case insensitive.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  TBSORT sorts an APPHOT/DAOPHOT STSDAS table database.
  TBSORT operates in place so
  a copy of the unsorted table must be made with the TABLES
  package TCOPY task in order to preserve the original table.
  The column or columns to sort on are specified by the parameter
  <i>columns</i>, which is a list of column names or column name patterns
  separated by
  commas.  The most significant column name is the first in the list. Subsequent
  columns are used to break ties.  There are two flags, <i>ascend</i>
  and <i>casesens</i>.  If <i>ascend</i> is yes,
  the first row in the output table holds the smallest value if
  the sorted column is numeric or the first string in alphabetic order if the
  sorted column is a character string.  If <i>casesens</i> is yes,
  upper case characters
  precede lower case characters in sort order.  Otherwise, case is not significant
  in determining the sort order.  No precedes yes when sorting a boolean column
  in ascending order.  Null table elements always are last in the sort, regardless
  of whether <i>ascend</i> is yes or no. 
  </p>
  <p>
  TBSORT is identical  to the TABLES package sort with the exception that
  it has its own copy of the default parameter set so that users
  can modify the parameters independently of the TBSORT task in TABLES.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Sort the output of the DAOPHOT ALLSTAR task in increasing order of
  magnitude.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; tbsort m92.al.1 MAG
  </pre></div>
  <p>
  2. Sort the output of the DAOPHOT task NSTAR in increasing order of
  the y position.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; tbsort m92.nst.1 YCENTER
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ptools.txsort,ptools.psort,tables.tbsort
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

.. _tsort:

tsort: Sort a table.
====================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tsort table columns
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task sorts an STSDAS-format table.  The sort is done in place, so if you want
  to keep a copy of the unsorted table, you should copy it with the 'tcopy'
  task before you
  do the sort.  The column, or columns, on which to sort are specified
  using the parameter
  'columns', which is a list of column names, or column name templates, 
  separated by
  commas.  The most significant column name is the first in the list---the
  column whose values are sorted; subsequent
  columns are used only to break ties.  There are two flags, 'ascend' and 
  'casesens'.  The 'ascend' parameter determines whether the sort is done
  in ascending or descending order, if
  'ascend = yes', the first row in the output table holds the lowest value (if
  the sorted column is numeric) or the first string in alphabetic order (if the
  sorted column is a character string).  If 'casesens = yes', upper 
  case characters
  precede lower case characters.  Otherwise, case is not significant
  in determining the sort order.  When sorting a boolean column, <span style="font-family: monospace;">"no"</span> precedes
  <span style="font-family: monospace;">"yes"</span>.  Null table elements are always last in the sort, regardless
  of the value of 'ascend'. 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file name template]' -->
  <dd>Name of the table, or tables, to be sorted in-place.
  All tables are sorted on the same column or columns; if more than one table
  is specified all tables must have the column(s) specified by the 'columns'
  parameter.
  </dd>
  </dl>
  <dl id="l_columns">
  <dt><b>columns [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='columns' Line='columns [string]' -->
  <dd>Column name or column name template describing columns on which sort will
  be performed.  A column name template consists of a list of
  column names, or column patterns containing wildcard characters.
  Individual column names, or templates, are separated by commas or white space.
  The list of columns can be placed in a file and the name of the 
  file passed to 'columns' (preceded by a
  <span style="font-family: monospace;">"@"</span> character). 
  </dd>
  </dl>
  <dl>
  <dt><b>(ascend = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ascend = yes) [boolean]' -->
  <dd>Sort the table in ascending order?  If you want the table sorted in descending
  order, set 'ascend = no'.
  </dd>
  </dl>
  <dl>
  <dt><b>(casesens = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(casesens = yes) [boolean]' -->
  <dd>Are sorts on character columns to be case sensitive?  If 'casesens = yes',
  upper case letters will precede lower case letters.  If 'casesens = no',
  case is ignored by the sort operation.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Sort a table of star positions by right ascension and declination:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tsort starcat.tab ra,dec
  </pre></div>
  <p>
  2. Sort a phone list. Make the sort case insensitive:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tsort phone.tab lname,fname case-
  </pre></div>
  <p>
  3. Sort a star catalog so that all binary stars (i.e., a boolean column
  named 'binary') are first:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tsort starcat.tab binary asc-
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
  tcopy
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

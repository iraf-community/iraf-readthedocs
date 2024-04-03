.. _tquery:

tquery: Create a new table from selected rows and columns in a table.
=====================================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tquery intable outtable expr columns sort
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task combines the functions of the tasks 'tselect', 'tproject', and
  'tsort' to create a more powerful task that can produce a sorted table of
  user-selected rows and columns.
  It can be used whenever you want to do more than one of these operations
  without creating intermediate tables.  This task creates a new table
  containing a subset of the rows and columns in an old table.  The rows in the
  new table can be sorted on any column or combination of columns.  The select,
  project, and sort operations are controlled by the parameters 'expr',
  'columns', and 'sort',
  respectively.  If the value of any of these parameters is a null or
  blank string, the corresponding operation is not performed.  Otherwise, the rows
  are selected whenever the row meets the conditions defined by 'expr';
  columns are
  selected by the 'columns' parameter, and rows are
  sorted on the columns named in 'sort'.  The hidden parameter 'uniq' is used
  to eliminate duplicate rows from the output table.  The hidden parameter
  'ascend' sorts the table in ascending order, and the parameter 'casesens'
  specifies whether sort conditions are to be case sensitive.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [file name template]' -->
  <dd>Table(s) from which rows are copied. If input is redirected, this
  parameter will ignored and input will be read from STDIN instead.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [file name template]' -->
  <dd>The new table(s) containing the copied rows.
  The number of output tables must equal the number of input tables.
  </dd>
  </dl>
  <dl id="l_expr">
  <dt><b>expr [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expr' Line='expr [string]' -->
  <dd>The boolean expression which determines which rows are copied to the new
  table.  The expression may be placed in a file and the name of the file
  preceeded by a <span style="font-family: monospace;">'@'</span> can be given in its place.  If the expression is null
  or blank, all rows are selected.  The syntax and method used to define
  this boolean expression is explained in detail in the help file for the
  'tselect' task (type <span style="font-family: monospace;">"help tselect"</span> for more information).
  </dd>
  </dl>
  <dl id="l_columns">
  <dt><b>columns [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='columns' Line='columns [string]' -->
  <dd>Column template describing the columns that are to be selected
  from the old table. A column template consists of a list
  of column names, which can include wildcard characters.
  The column names, or patterns, are separated by commas or white space.
  The list of columns can be placed in a file and then
  the name of that file passed to 'columns' (preceded by
  the <span style="font-family: monospace;">"@"</span> character).  If the first non-white character in the template
  is the negation character (either <span style="font-family: monospace;">"~"</span> or <span style="font-family: monospace;">"!"</span>),
  the new table will contain those columns
  that do NOT match the column template. If the column template
  is null or blank, all columns will be selected.
  </dd>
  </dl>
  <dl id="l_sort">
  <dt><b>sort [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sort' Line='sort [string]' -->
  <dd>Column template describing the columns to be sorted.  The
  first column name is the primary sort key with subsequent columns
  used to break ties.  If this parameter
  is null or blank, no sort will be done.
  </dd>
  </dl>
  <dl>
  <dt><b>(uniq = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(uniq = no) [boolean]' -->
  <dd>Make sure all rows are unique in a table?
  If 'unique' is set to <span style="font-family: monospace;">"yes"</span>, only one of each set of duplicate rows is included
  in the output table.  All columns in the output table must be identical for
  the row to be removed.  String comparisons are case sensitive.  Care should
  be used in setting this option for large tables, as it significantly increases
  the running time.
  </dd>
  </dl>
  <dl>
  <dt><b>(ascend = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ascend = yes) [boolean]' -->
  <dd>Should sorts be performed in ascending order?
  If 'ascend = yes', the table is sorted in ascending order, with the first
  row containing the smallest value of the sorted column.  Otherwise, the table
  is sorted in descending order, with the largest value first.
  </dd>
  </dl>
  <dl>
  <dt><b>(casesens = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(casesens = yes) [boolean]' -->
  <dd>Are sort operations case sensitive?
  If 'casesens = yes', sorts on character columns are case sensitive, with upper
  case letters preceding lower case.  Otherwise, the sort is not case
  sensitive.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Extract all binary stars from a catalog; write their names, magnitudes,
  and colors to a new table, sorted on magnitude:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tquery starcat.tab binary.tab binary name,mag,color mag
  </pre></div>
  <p>
  2. Remove duplicate rows from a set of tables. Otherwise, leave the tables
  unchanged. Using file name editing (i.e., the <span style="font-family: monospace;">"%"</span> characters to delineate
  old strings and new strings), change the file name extensions from <span style="font-family: monospace;">".tab"</span>
  to <span style="font-family: monospace;">".tbl"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tquery *.tab *.%tab%tbl% "" "" "" uniq+
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Column names must be set off from operators by blanks in the expression so
  that they can be correctly parsed by the expression evaluator.
  </p>
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
  tsort, tselect, tproject
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

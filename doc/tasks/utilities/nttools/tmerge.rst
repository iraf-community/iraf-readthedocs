.. _tmerge:

tmerge: Either merge or append tables.
======================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tmerge intable outtable option
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task is used to either merge or append tables,
  depending on the option selected by the 'option' parameter.
  The data type of each column is defined by
  the first table in the input list containing that column.
  If subsequent tables use the same column name,
  then data are converted to the type defined by the first table.
  Problems may occur when numerical data are written to
  a boolean column or a narrow character column.
  </p>
  <p>
  The <span style="font-family: monospace;">"merge"</span> option is normally used for tables containing few,
  if any, common columns.
  When the user selects <span style="font-family: monospace;">"merge"</span>,
  an output table is created containing as many columns
  as there are unique column names in all the input tables.
  (But see the description of the 'allcols' parameter.)
  The output table will have as many rows as the largest
  number of rows in the input tables.
  The input tables are read in order,
  with all values being placed into the output table.
  If different input tables have the same column names
  then the first values put into the output table
  will be overwritten by the later table values.
  For example, if the two input tables both have the column name <span style="font-family: monospace;">"X_VAL"</span>,
  then for each row number,
  the values written to the output table
  will be taken from the second input table.
  See below regarding text tables.
  </p>
  <p>
  On the other hand, if the <span style="font-family: monospace;">"append"</span> option is selected, all rows of
  the first input table are written to the output table, followed by all
  rows of the second table, and so on, until all input tables are written
  to the output table.
  The total number of output rows will be the sum
  of the numbers of rows in the input tables.
  Columns with the same name in different
  input tables will be written into the same output column, but no data
  will be overwritten because they are put into different rows.
  The <span style="font-family: monospace;">"append"</span> option would normally be used for tables that have all
  the same columns.
  </p>
  <p>
  An input table may have no rows.
  Such a table may be used as the first input table
  to control the order and definitions of columns in the output table.
  </p>
  <p>
  Header parameters are appended,
  and parameters with the same keyword name
  in different input tables are overwritten in the output file,
  except for history and comment keywords.
  </p>
  <p>
  Care must be taken with text tables.
  It is very likely that you would want
  'allcols = yes' if 'option = merge' and
  'allcols = no' if 'option = append'.
  See the description of the 'allcols' parameter for details.
  If the output table is a text file,
  the line length may not be longer than 4095 characters,
  which is a limitation for any text table.
  </p>
  <p>
  Column units are not checked.
  If columns with the same name have different units
  in two different input tables,
  the merged (or appended) data are likely to have mixed units.
  In addition, the column definition is taken from the first input table,
  but some and perhaps all of the data would come from the second input table,
  so the units in the output column definition would not be correct
  for those data.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [file name template]' -->
  <dd>Names of the tables to be merged or appended.  This parameter will take
  either a file name template describing several input tables, and may include
  wildcard characters, or it will take the name of a list file preceded by the
  <span style="font-family: monospace;">"@"</span> character; in the latter case the list file contains a list of file names
  with each file name on a separate line.  Wildcard characters should not be
  used for file name extensions because files other than tables will be
  processed, causing the program to crash.  For example, if the directory
  contains files <span style="font-family: monospace;">"table.tab"</span> and <span style="font-family: monospace;">"table.lis"</span>, the command <span style="font-family: monospace;">"tmerge tab*"</span> would
  open both files.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [file name]' -->
  <dd>The name of the output table.
  </dd>
  </dl>
  <dl id="l_option">
  <dt><b>option = <span style="font-family: monospace;">"merge"</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='option' Line='option = "merge" [string]' -->
  <dd>allowed values:  merge | append
  Either merge the columns in each row of each input table--overwriting
  previous values--or append files to each other.
  See also 'allcols' below.
  (These options are discussed in greater detail in the DESCRIPTION section.)
  </dd>
  </dl>
  <dl>
  <dt><b>(allcols = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(allcols = yes) [boolean]' -->
  <dd>Define output table columns using columns from
  all input tables?
  If 'allcols = no', the output table will contain
  only those columns defined in the first input table.
  If 'allcols = yes', the output table will contain
  all columns from all input tables.
  If 'option = merge', then it is likely that 'allcols' should be set to yes.
  For input tables that are simple text tables
  (i.e. that do not contain explicit column definitions),
  the 'allcols' parameter serves an additional function.
  When 'allcols = yes' the name of each column
  in a simple text table is changed
  to be <span style="font-family: monospace;">"c"</span> followed by the column number in the output table.
  This is intended to make the column names unique
  in order to allow merging text tables
  without having the columns overwrite previously written columns.
  Since the column names in simple text tables are just c1, c2, etc.,
  columns would overwrite previously written columns in the output
  if the names were not modified.
  If all input tables are simple text tables,
  and the output is also a text table,
  the new names will be discarded,
  so the net effect of this scheme is just to preserve all input data.
  If the output is a binary table, however,
  the modified column names will be retained.
  If the modified column names turn out not to be unique,
  a warning message will be printed.
  </dd>
  </dl>
  <dl>
  <dt><b>(tbltype = <span style="font-family: monospace;">"default"</span>) [string, allowed values:  default | row | </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(tbltype = "default") [string, allowed values:  default | row | ' -->
  <dd>column | text]
  This parameter specifies the table type.
  Setting 'tbltype' to <span style="font-family: monospace;">"row"</span> or <span style="font-family: monospace;">"column"</span> results in an stsdas binary table,
  the contents of which may be either row ordered or column ordered;
  row order is recommended.
  You can also specify that the output be a text table.
  The default ('tbltype = <span style="font-family: monospace;">"default"</span>') means that the type of the output table
  will be taken from the first input table.
  If the extension of the output file name is <span style="font-family: monospace;">".fits"</span> or <span style="font-family: monospace;">".??f"</span>,
  the table to be created will be a BINTABLE extension in a FITS file,
  regardless of how 'tbltype' is set.
  </dd>
  </dl>
  <dl>
  <dt><b>(allrows = 100) [integer, min=1, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(allrows = 100) [integer, min=1, max=INDEF]' -->
  <dd>The number of rows to allocate.
  This parameter is only used for column-ordered tables
  (specified by the 'tbltype' parameter).
  The 'allrows' parameter is the minimum number of rows an output
  table will contain.
  If the number of rows required by the input tables
  is greater than 'allrows' then the number of rows in the output table will
  be greater than 'allrows'.
  If 'option = merge', then the total number of rows will be
  the larger of 'allrows' or the number of rows in the largest table.
  If 'option = append', the total rows in the output table will be the larger
  of 'allrows' or the total number of rows in all input tables.
  </dd>
  </dl>
  <dl>
  <dt><b>(extracol = 0) [integer, min=0, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(extracol = 0) [integer, min=0, max=INDEF]' -->
  <dd>Extra space to be reserved for columns in the output table.
  This parameter is relevant only for a row-ordered table
  (specified by the 'tbltype' parameter).
  The default value of zero is normally appropriate,
  but if you expect to define additional columns in the output table
  at a later time
  then you can allocate the necessary space
  by specifying a value for 'extracol'.
  One unit of space is taken by each single-precision real value,
  integer value, or boolean value.
  A double-precision column requires two units of allocated space,
  and a character-string column takes one unit of space for each four
  characters, or fraction thereof.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  1. Suppose you have the following two tables.
  
  tbl1.tab:
          one     two     three
          ---     ---     -----
          1       -17     alpha
          2       -19     beta
          3       -23     gamma
  
  tbl2.tab:
          one     three   four
          ---     -----   ----
          27      beta    3.14
          28      delta   2.72
  
  then the statement
  
          cl&gt; tmerge tbl1,tbl2 mrg merge
  
  would create the following output table:
  
  mrg.tab:
          one     two     three   four
          ---     ---     -----   ----
          27      -17     beta    3.14
          28      -19     delta   2.72
          3       -23     gamma   INDEF
  
  while the statement
  
          cl&gt; tmerge tbl1,tbl2 app append
  
  would create the following table:
  
  app.tab:
          one     two     three   four
          ---     ---     -----   ----
          1       -17     alpha   INDEF
          2       -19     beta    INDEF
          3       -23     gamma   INDEF
          27      INDEF   beta    3.14
          28      INDEF   delta   2.72
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Phil Hodge.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  tselect, tproject, and proto.joinlines for text files
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

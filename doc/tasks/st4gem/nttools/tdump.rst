.. _tdump:

tdump: Dump the contents of a table to an ASCII file.
=====================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tdump table
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task converts an STSDAS table to ASCII format.
  The output does not include row numbers or column names;
  use the 'tprint' task for more readable output.
  </p>
  <p>
  The two primary uses for 'tdump' are to allow editing that would be
  difficult or impossible with 'tedit' (such as global substitutions)
  and copying a table over a network to another computer.
  For such purposes the table can be dumped to three separate files
  (i.e., one containing column definitions, one for header parameters,
  and one for table data),
  the data may be edited, column data types changed, etc.,
  and then the 'tcreate' task can be used to reassemble the table 
  from the three ASCII files.
  To prevent loss of information due to truncation,
  floating point data are printed using g format with a wide field.
  A character value with multiple words is printed with enclosing quotes
  to make it clear that it is the value for a single column
  and also for compatibility with 'tcreate'.
  </p>
  <p>
  All rows and columns of the table are dumped by default,
  but ranges of rows and individual columns may be specified.
  </p>
  <p>
  The order of printing the data is as follows.
  The first column of the first row is printed,
  then the second column of the first row is printed,
  then the third column of the first row, etc.
  If any column contains arrays,
  each element of the column array in the current row is printed
  before moving on to the next column.
  If the printed output is wider than a page (see 'pwidth'),
  the output will consist of more than one line per row of the table.
  After printing all columns in the first row,
  the second row is printed in the same way.
  Each row begins with a new line in the output text file.
  Note that this can be different from 'tprint',
  which prints all rows for those columns that will fit on a page,
  then prints all rows for the next set of columns.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file name]' -->
  <dd>The name of the STSDAS table to be dumped.
  </dd>
  </dl>
  <dl>
  <dt><b>(cdfile = STDOUT) [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(cdfile = STDOUT) [file name]' -->
  <dd>If 'cdfile' is not null (i.e., it is not passed a value of <span style="font-family: monospace;">""</span>)
  then the column definitions will be written
  to an output file having the name passed to 'cdfile'.
  (Note:  A space is not null.)  The column definitions consist of
  the column name, data type (<span style="font-family: monospace;">"R"</span> for real,
  <span style="font-family: monospace;">"D"</span> for double, <span style="font-family: monospace;">"I"</span> for integer, <span style="font-family: monospace;">"B"</span> for boolean,
  or <span style="font-family: monospace;">"CH*n"</span> for character strings of length n), print format, and units.
  For columns of arrays,
  the array size is shown in square brackets appended to the data type.
  </dd>
  </dl>
  <dl>
  <dt><b>(pfile = STDOUT) [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(pfile = STDOUT) [file name]' -->
  <dd>If 'pfile' is not null (i.e., it is not passed a value of <span style="font-family: monospace;">""</span>) 
  then the header parameters will be written
  to an output file with the name passed to 'pfile'.
  This file will not be created
  if there are no header parameters in the input file.
  </dd>
  </dl>
  <dl>
  <dt><b>(datafile = STDOUT) [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(datafile = STDOUT) [file name]' -->
  <dd>If 'datafile' is not null (i.e., it is not passed a value of <span style="font-family: monospace;">""</span>) then 
  the table data will be written
  to an output file with the name passed to 'datafile'.
  This file will not be created if the input table is empty.
  </dd>
  </dl>
  <dl>
  <dt><b>(columns = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(columns = "") [string]' -->
  <dd>The names of the columns to be printed.
  A null value causes all columns to be printed.
  A column template consists of a list
  of either column names or column name templates that include wildcards.
  Individual column names or templates are separated by commas or white space.
  This list of column names can be placed in a list file and 'column'
  will then be passed the file name preceded by a <span style="font-family: monospace;">"@"</span> character.
  If the first non-white character in the column template
  is the negation character (either <span style="font-family: monospace;">"~"</span> or <span style="font-family: monospace;">"!"</span>)
  the columns NOT named in the template will be printed.
  The 'tlcol' task (with the 'nlist' parameter set to 1) may be used 
  to generate a list of column names so there is no question about spelling.
  This list may be edited to rearrange or delete columns.
  </dd>
  </dl>
  <dl>
  <dt><b>(rows = <span style="font-family: monospace;">"-"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(rows = "-") [string]' -->
  <dd>The range of rows to be printed.
  The default of <span style="font-family: monospace;">"-"</span> means print all rows.
  The first ten rows could be specified as 'rows=<span style="font-family: monospace;">"1-10"</span>'.
  To print the first ten rows and all rows from 900 through
  the last (inclusive), use 'rows=<span style="font-family: monospace;">"1-10,900-"</span>'.
  Setting 'rows=<span style="font-family: monospace;">"1,3,7,23"</span>' will print only those four rows.
  It is not an error to specify rows larger than the largest row number;
  they will simply be ignored.
  Type <span style="font-family: monospace;">"help xtools.ranges"</span> for more information.
  </dd>
  </dl>
  <dl>
  <dt><b>(pwidth = -1) [integer, min=-1, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(pwidth = -1) [integer, min=-1, max=INDEF]' -->
  <dd>Width of the output for printing the table data.
  The default value of -1 means that
  checking the width should be disabled,
  and each table row will be written to one line in the output file.
  If any column to be printed is wider than 'pwidth',
  a warning message will be displayed,
  and the data will overflow the page width.
  The width of each character column is
  increased by two to allow space for a pair of enclosing quotes,
  which will be used if the value to be printed includes a blank or tab.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Dump the table <span style="font-family: monospace;">"junk.tab"</span> to STDOUT:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tdump junk.tab cdfile=STDOUT pfile=STDOUT datafile=STDOUT
  </pre></div>
  <p>
  2.  Dump <span style="font-family: monospace;">"junk.tab"</span>, but with the order of the columns rearranged:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tlcol junk.tab nlist=1 &gt; colnames.lis
  tt&gt; edit colnames.lis
     (Rearrange the column names and perhaps delete some of them.)
  tt&gt; tdump junk.tab columns=@colnames.lis
  </pre></div>
  <p>
  3.  Dump only the first 100 rows of the file <span style="font-family: monospace;">"big.fits"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tdump big.fits rows="1-100"
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
  tprint, tlcol, tcreate, ranges
  </p>
  <p>
  Type <span style="font-family: monospace;">"help tables opt=sys"</span> for a higher-level description of the 'tables' 
  package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

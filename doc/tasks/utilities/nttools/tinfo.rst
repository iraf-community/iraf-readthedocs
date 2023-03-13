.. _tinfo:

tinfo: Display table size information.
======================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tinfo table
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task is used to display information about a table.
  This information includes
  such things as the number of rows and columns.
  The output is written to STDOUT by default.
  The first line of output for each table in the input list is the table
  name preceded by a # sign.
  The values for the last table in the list are also put into parameters
  for the 'tinfo' task so that other tasks in a script may use the values.
  </p>
  <p>
  The parameters 'nrows', 'ncols', 'npar', 'rowlen', 'rowused', 'allrows',
  'maxpar', 'maxcols', 'tbltype', 'subtype' and 'tblversion'
  are output parameters.
  Since they are set rather than read by 'tinfo',
  any value assigned by the user will be overwritten.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file name template]' -->
  <dd>A list of tables for which size information is to be produced.
  </dd>
  </dl>
  <dl>
  <dt><b>(ttout = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ttout = yes) [boolean]' -->
  <dd>Display information on the terminal screen as it is being placed into
  parameters?  Setting 'ttout = no' will cause information to be placed
  only into task parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>(nrows) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nrows) [integer]' -->
  <dd>The number of rows written to the table.
  This and all subsequent parameters are output task parameters;
  that is, they are written by the 'tinfo' task.
  </dd>
  </dl>
  <dl>
  <dt><b>(ncols) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ncols) [integer]' -->
  <dd>The number of columns in the table.
  </dd>
  </dl>
  <dl>
  <dt><b>(npar) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(npar) [integer]' -->
  <dd>The number of header parameters in the table.
  </dd>
  </dl>
  <dl>
  <dt><b>(rowlen) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(rowlen) [real]' -->
  <dd>For a row-ordered table,
  'rowlen' is the amount of space allocated for each row in the table file.
  The unit of 'rowlen' is the size of a single-precision real number.
  This is only relevant for row-ordered STSDAS format tables.
  </dd>
  </dl>
  <dl>
  <dt><b>(rowused) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(rowused) [real]' -->
  <dd>'rowused' is the amount of the row length ('rowlen')
  that has actually been used
  by the columns that have been defined,
  in units of the size of a real number.
  For example, if a table contains three columns
  with data types integer, real and double precision,
  then 'rowused' would be four.
  If the table contains only one column of data type short,
  then 'rowused' would be 0.5.
  This is only relevant for row-ordered STSDAS format tables.
  </dd>
  </dl>
  <dl>
  <dt><b>(allrows) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(allrows) [integer]' -->
  <dd>The number of allocated rows.
  This is relevant only for column-ordered STSDAS format tables.
  </dd>
  </dl>
  <dl>
  <dt><b>(maxpar) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(maxpar) [integer]' -->
  <dd>The space allocated for header parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>(maxcols) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(maxcols) [integer]' -->
  <dd>The space allocated for column descriptors.
  </dd>
  </dl>
  <dl>
  <dt><b>(tbltype) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(tbltype) [string]' -->
  <dd>The table type, currently either <span style="font-family: monospace;">"stsdas"</span>, <span style="font-family: monospace;">"fits"</span> or <span style="font-family: monospace;">"text"</span>.
  <span style="font-family: monospace;">"stsdas"</span> is a machine dependent binary format,
  the default .tab format.
  <span style="font-family: monospace;">"fits"</span> means that the table is a TABLE or BINTABLE extension
  in a FITS file.
  <span style="font-family: monospace;">"text"</span> is an ASCII file in tabular format.
  See also 'subtype'.
  </dd>
  </dl>
  <dl>
  <dt><b>(subtype) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(subtype) [string]' -->
  <dd>For FITS tables the subtype can be either
  <span style="font-family: monospace;">"ascii"</span> (a TABLE extension) or <span style="font-family: monospace;">"binary"</span> (a BINTABLE extension).
  For text tables the subtype can be either
  <span style="font-family: monospace;">"simple"</span> or <span style="font-family: monospace;">"explicit column definitions"</span>.
  The latter subtype means there are column definition lines in the file,
  in the format:  <span style="font-family: monospace;">"#c column_name datatype print_format units"</span>.
  A simple text table has column names c1, c2, etc., and no units.
  For STSDAS format tables
  the subtype will be either <span style="font-family: monospace;">"row ordered"</span> or <span style="font-family: monospace;">"column ordered"</span>,
  which indicates the way the elements are stored in the table file.
  </dd>
  </dl>
  <dl>
  <dt><b>(tblversion) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(tblversion) [integer]' -->
  <dd>The version code is an integer that identifies the version of
  the tables package that created or last modified the table.
  For STSDAS tables, the version code is stored in the table file;
  for other formats this parameter is just
  the current tables version code number.
  This number is zero for 'stsdas' and 'tables' versions 1.2.3 and earlier,
  the number is one for versions 1.3 through 1.3.3,
  the number is two beginning 1995 March 6,
  and the number is three beginning 1998 April 14.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Get size information about the file 'm87pol.tab',
  but do not print the information to STDOUT,
  just put the values into parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tinfo m87pol ttout=no
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
  tlcol
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

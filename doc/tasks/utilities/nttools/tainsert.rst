.. _tainsert:

tainsert: Copy a column of scalars to an array entry in another table.
======================================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tainsert intable outtable row column
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task reads an entire column from one table
  and inserts those values (presumably more than one)
  at a specified row and column in an output table.
  If the output table exists it will be written to in-place;
  otherwise, it will be created.
  </p>
  <p>
  By default, the same column name is used in both tables.
  If the column does not exist in the output table, the column will be created.
  If the output table and the row and column already exist,
  the array of values at that location will be overwritten.
  The number of elements copied will be the minimum of
  the number of input rows and the output column array size.
  If the number of input rows is larger than the array size,
  a warning message will be printed,
  and the extra rows will be ignored.
  If the number of input rows is smaller than the array size,
  the remaining array elements will be set to INDEF.
  </p>
  <p>
  If the specified row number is less than one or is INDEF,
  'tainsert' looks for the header keyword ORIG_ROW in the input table.
  ORIG_ROW is written by 'taextract'.
  If that keyword exists, its value is used as the row number.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [file name]' -->
  <dd>Name of the input table.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [file name]' -->
  <dd>Name of the output table.
  If this table doesn't exist it will be created.
  </dd>
  </dl>
  <dl id="l_row">
  <dt><b>row = -1 [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='row' Line='row = -1 [integer]' -->
  <dd>This is the row number in the output table.
  The default means that 'tainsert' should use
  the value of the header keyword ORIG_ROW.
  </dd>
  </dl>
  <dl id="l_column">
  <dt><b>column [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='column' Line='column [string]' -->
  <dd>Column name in the input table and, by default, also in the output table.
  If this column does not exist in the output table, it will be created,
  and the array size will be set to the number of rows in the input table.
  See the descriptions for 'outcolumn' and 'size', however.
  It is an error if this column in the input table contains array entries.
  </dd>
  </dl>
  <dl id="l_outcolumn">
  <dt><b>outcolumn = <span style="font-family: monospace;">""</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outcolumn' Line='outcolumn = "" [string]' -->
  <dd>If 'outcolumn' is specified,
  that name will be used for the output table;
  otherwise, 'column' will be used for both input and output tables.
  This provides an easier way to change the name of the output column
  than by running 'tchcol' after running 'taextract'.
  Note that if 'outcolumn' is specified,
  it is used not only for finding the column in the output table
  but also for creating the column if it wasn't found.
  The 'size', 'datatype', 'colunits', and 'colfmt' parameters,
  by contrast, are only used when creating a new column.
  </dd>
  </dl>
  <dl>
  <dt><b>(size = INDEF) [int]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(size = INDEF) [int]' -->
  <dd>When creating a new column in the output table,
  the default is for the array size of that column to be set to
  the number of rows in the input table.
  This may be overridden by specifying a value for 'size'.
  If 'size' is a positive integer, not INDEF,
  this will be used as the array size when creating the new column.
  </dd>
  </dl>
  <dl>
  <dt><b>(datatype = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(datatype = "") [string]' -->
  <dd>When creating a new column in the output table,
  the default is to use the same data type as the column in the input table.
  However, if 'datatype' is specified (i.e. not null or blank),
  this will be used as the data type when creating the new column.
  For numeric and boolean columns, only the first character is used:
  <span style="font-family: monospace;">"r"</span> and <span style="font-family: monospace;">"d"</span> for single and double precision floating point,
  <span style="font-family: monospace;">"s"</span> and <span style="font-family: monospace;">"i"</span> for short integer and integer,
  <span style="font-family: monospace;">"b"</span> for boolean.
  For a character string of maximum length 12 (for example), use <span style="font-family: monospace;">"ch*12"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>(colunits = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(colunits = "") [string]' -->
  <dd>When creating a new column in the output table,
  the units will be set to 'colunits' if it has been specified;
  otherwise, the units will be copied from the column in the input table.
  </dd>
  </dl>
  <dl>
  <dt><b>(colfmt = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(colfmt = "") [string]' -->
  <dd>When creating a new column in the output table,
  the print format will be set to 'colfmt' if it has been specified;
  otherwise, the print format will be copied from the column in the input table.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Copy the entire column <span style="font-family: monospace;">"polar"</span> from table <span style="font-family: monospace;">"scalar.tab"</span>,
  and insert the values into row 5, column <span style="font-family: monospace;">"polar"</span>, of table <span style="font-family: monospace;">"array.tab"</span>.
  If <span style="font-family: monospace;">"array.tab"</span> does not exist it will be created.
  If column <span style="font-family: monospace;">"polar"</span> does not exist in <span style="font-family: monospace;">"array.tab"</span>,
  that column will be created.
  </p>
  <div class="highlight-default-notranslate"><pre>
  at&gt; tainsert scalar.tab array.tab 5 polar
  </pre></div>
  <p>
  2. Copy the arrays from row 5, columns <span style="font-family: monospace;">"wavelength"</span> and <span style="font-family: monospace;">"flux"</span>,
  from <span style="font-family: monospace;">"array.tab"</span> to a temporary table,
  sort them on the wavelength,
  and insert them back where they came from.
  </p>
  <div class="highlight-default-notranslate"><pre>
  at&gt; taextract array temp 5 wavelength
  at&gt; taextract array temp 5 flux
  at&gt; tsort temp wavelength
  at&gt; tainsert temp array 0 wavelength
  at&gt; tainsert temp array 0 flux
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
  taextract
  </p>
  <p>
  Type <span style="font-family: monospace;">"help ttools opt=sysdoc"</span> for a higher-level description of the 'ttools'
  package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

.. _taextract:

taextract: Copy an array entry to a column of scalars in another table.
=======================================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  taextract intable outtable row column
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task extracts one entry (presumably an array of values)
  at a specified row and column
  and writes it as a column of scalar values to another table.
  If the output table exists it will be written to in-place;
  otherwise, it will be created.
  </p>
  <p>
  By default, the same column name is used in both tables.
  If the output table and column already exist,
  the data in that column will be overwritten;
  otherwise, the column will be created.
  If the array size for the specified column in the input table is N,
  then the values will be written to rows 1 through N of the output table.
  If the output column already exists,
  and the output table contains more than N rows,
  then rows N+1 through the last will be set to INDEF for this column.
  </p>
  <p>
  The input row number is written to the header of the output table
  using keyword ORIG_ROW.
  This allows 'tainsert' to put the data back where 'taextract' got them from.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [file name]' -->
  <dd>Name of the input table containing a column with array entries.
  It is not an error for the array length to be one.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [file name]' -->
  <dd>Name of the output table.
  If this table doesn't exist it will be created.
  If the table does exist the column will either be created or overwritten.
  The input and output tables may not be the same,
  and they may not be in the same file if FITS format is used.
  </dd>
  </dl>
  <dl id="l_row">
  <dt><b>row [integer, min=1, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='row' Line='row [integer, min=1, max=INDEF]' -->
  <dd>This is the row number in the input table.
  In the output table there will be as many rows
  as there are elements in the input table entry for 'column'.
  </dd>
  </dl>
  <dl id="l_column">
  <dt><b>column [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='column' Line='column [string]' -->
  <dd>Column name.
  This is used to find the column in the input table,
  and by default the same name is used to create
  (or find, if it already exists)
  the column in the output table.
  See the description for 'outcolumn'.
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
  The 'datatype', 'colunits', and 'colfmt' parameters, by contrast,
  are only used when creating a new column.
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
  1. Extract the array from row 5, column <span style="font-family: monospace;">"polar"</span>, from table <span style="font-family: monospace;">"array.tab"</span>,
  putting the values in column <span style="font-family: monospace;">"polar"</span> of table <span style="font-family: monospace;">"scalar.tab"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  at&gt; taextract array.tab scalar.tab 5 polar
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
  tainsert
  </p>
  <p>
  Type <span style="font-family: monospace;">"help ttools opt=sysdoc"</span> for a higher-level description of the 'ttools'
  package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

.. _tjoin:

tjoin: Perform a relational join of two tables.
===============================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tjoin intable1 intable2 outtable column1 column2
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task combines two tables into a new table on the basis of one or
  more common columns.  Two rows from the input tables are combined to
  form a row of the output table whenever the values in the common
  columns are equal. If a row in one of the input tables matches several
  rows in the other input table, all combinations of the rows are placed
  in the output table. Null table elements are never matched.  Tables
  can be joined on row number as well as on column by setting the column
  name to <span style="font-family: monospace;">"row"</span>.
  </p>
  <p>
  This task has three hidden parameters, 'extrarows', 'tolerance', and
  'casesens'.  By default, if a row in one of the input tables does not
  match any row in the other input table, it is not placed in the output
  table.  However, if the parameter 'extrarows' is set to 'first', rows
  in the first table that are unmatched are added to the output table
  and if 'extrarows' is set to 'both', unmatched rows from both input
  tables are added to the output table.
  </p>
  <p>
  The task parameter 'tolerance' is a comma separated list of
  values. The number of values should either equal to the number of join
  columns or one. If only one value is supplied and there are more than
  one join column, the value is used for all columns.  If the difference
  between two column values is less than or equal to the corresponding
  value of 'tolerance', the values are considered equal and their
  respective rows are placed in the output table.
  </p>
  <p>
  If 'casesens = no', the case of a string is ignored when testing for
  equality. 'tolerance' must be set to zero when comparing string or
  boolean columns.
  </p>
  <p>
  If a value of 'tolerance' is nonzero, the output table will contain the
  corresponding join columns from both tables. If a value of
  'tolerance' is zero, the output table will contain a single join column,
  as both values are identical. If a column name in the first input
  table is the same as a column name in the second input table, this
  task tries to create a unique name by appending <span style="font-family: monospace;">"_1"</span> to the first name
  and <span style="font-family: monospace;">"_2"</span> to the second name. If the task cannot create a unique name
  in this way, it stops with an error.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable1">
  <dt><b>intable1 [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable1' Line='intable1 [file name]' -->
  <dd>First input table. 
  </dd>
  </dl>
  <dl id="l_intable2">
  <dt><b>intable2 [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable2' Line='intable2 [file name]' -->
  <dd>Second input table.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [file name]' -->
  <dd>Output table.  This is the join of the two input tables.
  </dd>
  </dl>
  <dl id="l_column1">
  <dt><b>column1 [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='column1' Line='column1 [string]' -->
  <dd>Names of the common columns in the first table. If there is more than
  one column name, the names should be separated by commas. If a column
  name is <span style="font-family: monospace;">"row"</span>, the join is done on row number instead of the value of
  a column. This only works if there is not column named <span style="font-family: monospace;">"row"</span> in the
  table.
  </dd>
  </dl>
  <dl id="l_column2">
  <dt><b>column2 [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='column2' Line='column2 [string]' -->
  <dd>Comma separated list of names of the common columns in the second
  table. The number of names must match the number of names in column1.
  The name may be <span style="font-family: monospace;">"row"</span>, in which case the join is done on row number.
  </dd>
  </dl>
  <dl>
  <dt><b>(extrarows = <span style="font-family: monospace;">"neither"</span>) [string, allowed values: neither|first|both]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(extrarows = "neither") [string, allowed values: neither|first|both]' -->
  <dd>This parameter controls whether unmatched rows are added to the output 
  table. If it is set to 'neither', unmatched rows are not added. If it
  is set to 'first', unmatched rows from the first table are added. If
  it is set to 'both', unmatched rows from both tables are added. When
  unmatched rows are added to the output table columns in the output
  table derived from the other table have their values left undefined.
  </dd>
  </dl>
  <dl>
  <dt><b>(tolerance = <span style="font-family: monospace;">"0.0"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(tolerance = "0.0") [string]' -->
  <dd>Tolerance used in testing for equality between common columns. The
  values must be greater than or equal to zero. If there is more than
  one common column, this parameter may be a comma separated list of
  values. In this case, the number of tolerance values must equal the
  number of common columns or be one. If there is only one tolerance
  value, the same value is used for all columns.
  </dd>
  </dl>
  <dl>
  <dt><b>(casesens = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(casesens = yes) [boolean]' -->
  <dd>Is case important in testing equality of strings?
  If set to <span style="font-family: monospace;">"yes"</span>, the test for equality is case sensitive.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Combine a table of star positions and a table of star magnitudes to create
  a star catalog. The star name is not case sensitive:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tjoin starpos.tab starmag.tab starcat.tab name name case-
  </pre></div>
  <p>
  2. Create a table of all spectral lines that match a set of reference
  wavelengths within 10 angstroms:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tjoin spectrum.tab reference.tab lines.tab WAVE WAVE tol=10.
  </pre></div>
  <p>
  3. Combine a phone list with an address list where the name is stored
  in two columns, <span style="font-family: monospace;">"last"</span> and <span style="font-family: monospace;">"first"</span>. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tjoin phone.tab address.tab output.tab LAST,FIRST LAST,FIRST
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
  tselect, tproject, tproduct
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

.. _tstat:

tstat: Get mean, standard deviation, min, and max for a column.
===============================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tstat intable column
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task gets the mean, standard deviation, median, minimum and maximum
  values for a table column.
  The output will be written to cl parameters and may also be written either
  to the standard output (STDOUT) or to a table.
  When more than one table is specified as 'intable', the statistics are
  determined for each table separately, not cumulatively.  The values
  in the cl parameters therefore refer to the last table in the list.
  </p>
  <p>
  If an input table contains only one column
  (either in fact or due to the use of a column selector with the table name),
  then the 'column' parameter is ignored,
  and statistics are computed for that one column.
  If 'intable' includes more than one table,
  the 'column' parameter may be required for some tables
  (those with more than one column) but not for others.
  </p>
  <p>
  The range of rows to use for statistics
  may be restricted either by the 'rows' parameter
  or by use of a row selector with the table name.
  Both may be used, in which case 'rows'
  is interpreted to mean selected row numbers,
  rather than rows in the underlying table.
  That is, the row selector with the table name is applied first,
  then the 'rows' parameter is used to further restrict the rows.
  </p>
  <p>
  For a column that contains arrays,
  this task reads all elements of all selected rows
  and computes statistics on all those elements together.
  Typical usage for array columns would be to specify just one row,
  but any number of rows may be included,
  limited only by memory.
  </p>
  <p>
  Lower and upper limits may be set using the parameters 'lowlim' and 'highlim'
  such that table values outside that range are not used when computing
  the statistics.
  Either the lower or upper limit may be set individually.
  If there are no values within the range specified
  and within the range of rows given by the 'rows' parameter,
  then the average, etc, will be printed as INDEF.
  </p>
  <p>
  For some tables, one can get statistics on the data in a row
  by using 'tdump' and piping the output to 'tstat'.
  See the examples for more information.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [file name template]' -->
  <dd>A list of input tables.
  Statistics will be obtained for one column, the same name in every table.
  If the input is redirected,
  this parameter need not be specified;
  that is, if there's only one command-line argument,
  it will be taken to be the column name.
  </dd>
  </dl>
  <dl id="l_column">
  <dt><b>column [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='column' Line='column [string]' -->
  <dd>Column in input tables.
  The statistics are gotten for the values in the column with this name.
  If an input table contains only one column,
  this parameter will be ignored,
  and you will not even be prompted for a value.
  If 'intable' includes more than one table with only one column,
  the column name does not need to be the same in each of these tables.
  For tables containing more than one column,
  this parameter is required,
  and the same column name will be used for each table in the list
  that contains more than one column.
  </dd>
  </dl>
  <dl>
  <dt><b>(outtable = <span style="font-family: monospace;">"STDOUT"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outtable = "STDOUT") [string]' -->
  <dd>Output table, STDOUT, or null.
  If 'outtable' is null (<span style="font-family: monospace;">""</span>) then the results will only be written to cl
  parameters (see 'nrows', 'mean', 'stddev', 'vmin', 'vmax').
  If 'outtable' is <span style="font-family: monospace;">"STDOUT"</span> then the results will be written to
  the standard output preceded by a header line (beginning with #)
  that gives the name of the table and the name of the column.
  If 'outtable' is not <span style="font-family: monospace;">"STDOUT"</span> and is not null then it is interpreted as
  a table name (just one name), and the statistics for the input tables
  will be written to separate rows of the output table.
  If the table already exists,
  the rows will be appended to what is already there.
  The output column names are given by
  the parameters 'n_tab', 'n_nam', 'n_nrows', etc.
  </dd>
  </dl>
  <dl>
  <dt><b>(lowlim = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(lowlim = INDEF) [real]' -->
  <dd>Values below this are ignored.
  </dd>
  </dl>
  <dl>
  <dt><b>(highlim = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(highlim = INDEF) [real]' -->
  <dd>Values above this are ignored.
  </dd>
  </dl>
  <dl>
  <dt><b>(rows = -) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(rows = -) [string]' -->
  <dd>Range of rows to use for statistics.
  The default <span style="font-family: monospace;">"-"</span> means that all rows are used.
  See the help for RANGES in XTOOLS for a description of the syntax.
  </dd>
  </dl>
  <dl>
  <dt><b>(n_tab = table) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(n_tab = table) [string]' -->
  <dd>Column name for name of input table.
  This and other parameters that begin with <span style="font-family: monospace;">"n_"</span> are only used if the output values are
  written to a table.
  </dd>
  </dl>
  <dl>
  <dt><b>(n_nam = column) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(n_nam = column) [string]' -->
  <dd>Column name for name of input column.
  This and other parameters that begin with <span style="font-family: monospace;">"n_"</span> are only used if the output values are
  written to a table.
  </dd>
  </dl>
  <dl>
  <dt><b>(n_nrows = nrows) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(n_nrows = nrows) [string]' -->
  <dd>Column name for number of good rows.
  </dd>
  </dl>
  <dl>
  <dt><b>(n_mean = mean) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(n_mean = mean) [string]' -->
  <dd>Column name for mean.
  </dd>
  </dl>
  <dl>
  <dt><b>(n_stddev = stddev) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(n_stddev = stddev) [string]' -->
  <dd>Column name for standard deviation.
  </dd>
  </dl>
  <dl>
  <dt><b>(n_median = value) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(n_median = value) [string]' -->
  <dd>Column name for median.
  </dd>
  </dl>
  <dl>
  <dt><b>(n_min = min) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(n_min = min) [string]' -->
  <dd>Column name for minimum.
  </dd>
  </dl>
  <dl>
  <dt><b>(n_max = max) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(n_max = max) [string]' -->
  <dd>Column name for maximum.
  </dd>
  </dl>
  <dl>
  <dt><b>(nrows) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nrows) [integer]' -->
  <dd>The number of rows for which the column value was not INDEF and was
  within the range 'lowlim' to 'highlim'.
  This is a task output parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>(mean) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(mean) [real]' -->
  <dd>Mean value (of the last table in the input list 'intable').
  This is a task output parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>(stddev) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(stddev) [real]' -->
  <dd>Standard deviation of the values (not of the mean).
  This is a task output parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>(median) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(median) [real]' -->
  <dd>Median value.
  This is a task output parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>(vmin) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vmin) [real]' -->
  <dd>Minimum.
  This is a task output parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>(vmax) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vmax) [real]' -->
  <dd>Maximum.
  This is a task output parameter.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Get statistics on column <span style="font-family: monospace;">"flux"</span> in all tables, putting the output
  (assuming outtable=<span style="font-family: monospace;">"STDOUT"</span>) in the ASCII file 'flux.lis':
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tstat *.tab flux &gt; flux.lis
  </pre></div>
  <p>
  2.  In order to get statistics on the data
  in a row rather than a column,
  you can use 'tdump' for one row
  and specify pwidth to be so small that
  each value will be printed on a separate line.
  The output of 'tdump' will then be a one-column table
  containing the row from the input table,
  and 'tstat' can be run on that one-column table.
  Since the input is redirected, we don't specify the table name.
  Note also that in this case the input contains only one column,
  so we don't specify the column name either.
  In this example, we get statistics on row 17 of <span style="font-family: monospace;">"bs.fits"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tdump bs.fits cdfile="" pfile="" \
  &gt;&gt;&gt; row=17 pwidth=15 | tstat
  </pre></div>
  <p>
  3.  When the input is redirected and has multiple columns,
  the command-line argument should be the column name to use,
  not the table name.
  The table name in this case will internally be set to <span style="font-family: monospace;">"STDIN"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; dir l+ | tstat c3
  </pre></div>
  <p>
  4.  The statistics on column <span style="font-family: monospace;">"flux"</span> in 'hr465.tab' are put in parameters
  'tstat.nrows', 'tstat.mean', etc.,
  and are not written to STDOUT or to a table.
  We only include rows for which column V is no larger than 12.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tstat "hr465.tab[r:v=:12][c:flux]" outtable=""
  </pre></div>
  <p>
  5.  The output statistics are written to a table.  The default column name
  for the mean value is overridden:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tstat hr465.tab flux outtable=hr465s.tab n_mean="mean_flux"
  </pre></div>
  <p>
  6.  Get statistics on column <span style="font-family: monospace;">"flux"</span> in table 'hr465.tab', but only for
  rows 17 through 116, row 271, and row 952:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tstat hr465.tab[c:flux] outtable="STDOUT" row="17-116,271,952"
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
  thistogram, ranges
  </p>
  <p>
  Type <span style="font-family: monospace;">"help tables opt=sys"</span> for a higher-level description of the 'tables' 
  package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

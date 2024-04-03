.. _trebin:

trebin: Resample a table to uniform spacing.
============================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  trebin intable outtable column start end step
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task resamples tables.
  The grid on which to interpolate an input table
  may be specified either by a table giving explicit values
  or by start, end, and step values for uniform spacing.
  The column names in the output table
  will be the same as in the input table.
  </p>
  <p>
  If the independent variable column ('column')
  in the input table contains scalar values,
  each numeric column in the input table will be rebinned
  to the values of the output independent variable.
  Character and boolean columns
  will not be copied to the output table.
  Columns that contain arrays will also not be copied to output.
  On the other hand,
  if the input independent variable column contains arrays
  rather than scalar values,
  then each row of the input table will be rebinned individually.
  Scalar columns will be copied to output unchanged.
  Array columns which have the same length as 'column'
  will be rebinned and written to the output table;
  if the array size is not the same,
  the column will not be copied to output.
  </p>
  <p>
  Except for function = <span style="font-family: monospace;">"linear"</span>,
  the output values are obtained by interpolation, not by fitting.
  The distinction is important when rebinning to a spacing ('step')
  that is significantly coarser than the spacing of the input data.
  For functions other than linear,
  each interpolated value is obtained as follows.
  The values of the input data
  nearest the current output independent variable value (X) are selected;
  the input data are then interpolated at X
  to obtain the value to write to the output table.
  For function = <span style="font-family: monospace;">"nearest"</span>, only one input point is used;
  for function = <span style="font-family: monospace;">"poly3"</span> or <span style="font-family: monospace;">"spline"</span>, four input points are used.
  This is appropriate for rebinning
  to a spacing not much different from the input data.
  For resampling noisy data
  to a significantly wider spacing than the input data, however,
  these options will give very poor results.
  In the latter case, function = <span style="font-family: monospace;">"linear"</span> (the default) should be used.
  This option uses a linear fit to all the data
  within an interval of width 'step' centered on each output X value.
  If there are fewer than two input points in a given interval, however,
  the value is interpolated the same way as is done for the other functions;
  that is, the two input points nearest to X are selected,
  and the value is interpolated at X
  (note that these two points can be outside the 'step' interval).
  </p>
  <p>
  A significant limitation to this task is that
  there is no option to conserve total counts.
  'trebin' averages the data values,
  rather than summing the input bins.
  What 'trebin' does is appropriate for flux-calibrated spectra,
  or for time series data expressed as count rate,
  but it would not be correct for data in counts,
  or for count rate spectra.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [file name template]' -->
  <dd>List of input tables to be resampled.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [file name template]' -->
  <dd>Output tables or directory.
  The number of output tables must match the number of input tables unless
  'outtable' is a directory name.
  </dd>
  </dl>
  <dl id="l_column">
  <dt><b>column [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='column' Line='column [string]' -->
  <dd>Name of the independent variable column in the input table,
  i.e., the column on which the data are being resampled.
  The same column name is used for all input tables.
  The values in this column must be
  either monotonically increasing or decreasing.
  INDEF values and trailing 'padvalue' (described below) will be ignored.
  The data type of the column is assumed to be a numeric type.
  </dd>
  </dl>
  <dl id="l_start">
  <dt><b>start [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='start' Line='start [real]' -->
  <dd>If the independent variable values at which to interpolate the input values
  are to be uniformly spaced,
  they may be specified using 'start', 'end', and 'step'.
  'start' is the first value of the output independent variable.
  See also 'xtable';
  'start', 'end', and 'step' will be ignored if 'xtable' was specified.
  </dd>
  </dl>
  <dl id="l_end">
  <dt><b>end [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='end' Line='end [real]' -->
  <dd>Last value of the independent variable.
  This may be rounded up by a fraction of 'step' to ensure that the entire
  range from 'start' to 'end' is included in the output table.
  </dd>
  </dl>
  <dl id="l_step">
  <dt><b>step [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='step' Line='step [real]' -->
  <dd>Increment in independent variable.
  The sign of 'step' is ignored;
  internally to 'trebin' the sign will be set to negative
  if 'start' is larger than 'end'.
  If 'start' and 'end' are the same,
  the output table will contain one row,
  and 'step' will only be used for the case of function = <span style="font-family: monospace;">"linear"</span>.
  For other values of 'function',
  since the data will be interpolated at just the one point 'start',
  the step size will not be needed.
  </dd>
  </dl>
  <dl>
  <dt><b>(xtable) [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(xtable) [file name template]' -->
  <dd>The independent variable values at which to interpolate the input values
  can either be specified explicitly with 'xtable'
  or computed using 'start', 'end', 'step'.
  If 'xtable' is specified,
  there must either be just one table name,
  or the number of names must be the same as
  the number of names in 'intable'.
  If there is only one 'xtable',
  it will be used for all input tables.
  'xtable' must contain only one column.
  The name of the column does not matter;
  it does not need to be the same as given by 'column'.
  If the actual table contains more than one column,
  use the column selector syntax to specify which one to use.
  The column may contain either scalar values or arrays.
  If the column contains arrays,
  there must be only one row;
  if the actual table contains more than one row,
  use the row selector syntax to specify which one to use.
  The data type of the column is assumed to be a numeric type.
  </dd>
  </dl>
  <dl>
  <dt><b>(function = <span style="font-family: monospace;">"linear"</span>) [string, allowed values: nearest | linear | </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(function = "linear") [string, allowed values: nearest | linear | ' -->
  <dd>poly3 | spline]
  Interpolation function.
  There must be at least four rows in the input table
  for cubic polynomial or cubic spline interpolation.
  Two rows are required for linear interpolation,
  and only one for nearest-neighbor.
  The <span style="font-family: monospace;">"linear"</span> option uses a linear fit,
  while all other functions are interpolations
  using only the required number of points
  nearest the value of the independent variable.
  If an input table does not contain enough rows,
  or if a column being interpolated contains INDEF values
  so that the total number of values is insufficient for interpolation,
  the output column will be entirely INDEF;
  if verbose = yes, a message will be printed.
  </dd>
  </dl>
  <dl>
  <dt><b>(extrapolate = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(extrapolate = no) [boolean]' -->
  <dd>Extrapolate if out of bounds?  See 'value' below.
  </dd>
  </dl>
  <dl>
  <dt><b>(value = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(value = INDEF) [real]' -->
  <dd>Value to use if out of bounds.
  The independent variable values
  at which the input table is to be interpolated
  may fall outside the range of values
  in the independent variable column in the input table.
  The value to write to the output table
  for out of bounds independent variables depends on
  the 'extrapolate' and 'value' parameters.
  If 'extrapolate' is yes, then 'value' is ignored,
  and the interpolation function is used for extrapolation.
  If 'extrapolate' is no,
  then 'value' is written to each dependent variable column
  for each row that the independent variable
  is outside the range of values in the input table.
  Note that for columns of type integer or short,
  'value' should be within the range of possible values of that type,
  and if 'value' contains a fractional part
  it will be rounded to the nearest integer.
  </dd>
  </dl>
  <dl>
  <dt><b>(padvalue = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(padvalue = INDEF) [real]' -->
  <dd>Trailing INDEF values in the independent variable column
  (either in 'intable' or in 'xtable')
  will be ignored.
  'padvalue' can be used to specify an additional value,
  such as zero,
  which will also be ignored
  if it occurs at the end of an array of independent variable values.
  Values will be trimmed off the end of the array
  until a value that is neither INDEF nor 'padvalue' is encountered.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>If verbose = yes,
  the input and output table names will be printed as they are processed,
  and the names of columns that are not being copied to output
  will also be printed.
  </dd>
  </dl>
  <dl>
  <dt><b>(Version) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(Version) [string]' -->
  <dd>This gives the date of installation of the current version.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Resample all the columns in all tables beginning with <span style="font-family: monospace;">"hr"</span> so the values
  in the <span style="font-family: monospace;">"Wavelength"</span> column range from 3000 to 8000 in steps of 10.
  The output tables will have the same names, but will be written in the
  directory <span style="font-family: monospace;">"home$spec"</span> (which should be different from the default directory).
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; trebin hr*.tab "home$spec/" Wavelength 3000. 8000. 10.
  </pre></div>
  <p>
  2. Interpolate the text table <span style="font-family: monospace;">"in"</span> at a single point,
  where the value in column one is 5,
  and print the results on the standard output.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; trebin in STDOUT c1 5. 5. 0.
  </pre></div>
  <p>
  3. Interpolate the table from example 2
  onto the array of independent variable values
  in column <span style="font-family: monospace;">"wavelength"</span> at row 37 of <span style="font-family: monospace;">"x1d.fits"</span>.
  As in example 2,
  the independent variable in <span style="font-family: monospace;">"in"</span> is the first column, <span style="font-family: monospace;">"c1"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; trebin in STDOUT c1 xtable="x1d.fits[r:row=37][c:wavelength]"
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  A column which contains an integer bit mask
  will be interpolated as if it were an ordinary numeric column,
  which is not the correct behavior.
  </p>
  <p>
  Sometimes a table contains array columns
  where the allocated array size is (or can be)
  larger than the number of elements actually used.
  In this case, a scalar column might be used
  to specify the effective array length.
  The array size in the output table
  will typically be different from the array size in the input table;
  'trebin' will update the allocated array size,
  but it will not modify any scalar column that gives the effective array size.
  </p>
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
  Type <span style="font-family: monospace;">"help tables opt=sys"</span> for a higher-level description of the 'tables'
  package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

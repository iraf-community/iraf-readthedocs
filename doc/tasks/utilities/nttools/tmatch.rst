.. _tmatch:

tmatch: Find closest match between rows in two tables
=====================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tmatch (input1, input2, output, match1, match2, maxnorm)
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task combines rows from two tables into one. Rows are combined by
  looking at each row in the first table and finding the row in the
  second table whose match columns are closest to those in the first.
  The distance between two rows is defined in the usual way to be the
  square root of the sum of the squares of the difference between the
  corresponding match columns. Rows are only written to the output table
  if the distance between them is less than the distance specified by
  maxnorm. This task converts match column units to degrees for the
  purpose of computing the distance if the column units are recognized
  angular units (seconds, minutes, degrees, hours, or radians or any
  abbreviation of these). If the column units are blank or some
  unrecognized string, no conversion is done. Thus, if the match column
  is in some recognized angular units, maxnorm should be specified in
  degrees.
  </p>
  <p>
  Columns named by the parameters 'incol1' and 'incol2' will be copied to
  the output table. If these parameters are left blank, all columns will
  be copied to the output table. Columns will have the same name in the
  output table as in the input table, except that columns with the same
  name in both input tables will have the suffix <span style="font-family: monospace;">"_1"</span> and <span style="font-family: monospace;">"_2"</span> added to
  indicate which table they were copied from.
  </p>
  <p>
  This task optionally allows you to supply a set of weighting factors
  that are multiplied by the difference between corresponding match
  columns when computing the distance. These factors can be used to
  supply units conversion when column units information is missing from
  the input table or as a way to weight information from columns
  containing distinct information. If factors are supplied, any column
  units information is ignored. If the factors are left bank, they are
  ignored and column units information is used to convert to degrees
  when possible.
  </p>
  <p>
  If the match columns contain spherical coordinates, parameter 'sphere'
  should be set to yes so that the distance on a sphere can be computed.
  If the match columns do contain spherical units, the first column
  should be the longitude column (such as right ascension) and the
  second column should be the latitude column (such as declination).
  Columns should also be in some recognized angular units, or a
  conversion factor should be supplied explicitly.
  </p>
  <p>
  The task optionally produces a diagnostic output file if a file name
  is supplied to parameter 'diagfile'. The diagnostic file contains the
  rows from the first table that were not matched, the cases where
  more than one row in the first table matched a single row in the
  second table, and the ten matched rows in the with the largest
  distance between them. Rows in the diagnostic output are identified by
  their table number and row number and optionally by the contents of
  the columns specified by the parameters 'nmcol1' and 'nmcol2'.
  </p>
  <p>
  This task differs from tjoin in two respects. First tjoin combines
  tables on the basis of a single column, while this task can combine
  tables based on multiple columns. Second, tjoin places every
  combination of rows matching within the specified tolerance in the output
  table, while this task only puts the closest match in the output table.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input1">
  <dt><b>input1 [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input1' Line='input1 [string]' -->
  <dd>First input table name.
  </dd>
  </dl>
  <dl id="l_input2">
  <dt><b>input2 [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input2' Line='input2 [string]' -->
  <dd>Second input table name.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [string]' -->
  <dd>Output table name.
  </dd>
  </dl>
  <dl id="l_match1">
  <dt><b>match1 [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='match1' Line='match1 [string]' -->
  <dd>A column template describing columns from the first table used to
  match the two tables. A column name template is a comma or whitespace
  list of strings. Each string may either be a column name a pattern
  containing wildcard characters which matches several column names. This
  parameter will also accept the name of a list file (preceded by the
  <span style="font-family: monospace;">"@"</span> character) containing column names to be matched.
  If the first non-white character in the template
  is the negation character (either <span style="font-family: monospace;">"~"</span> or <span style="font-family: monospace;">"!"</span>),
  all columns NOT appearing in the list will be matched.
  </dd>
  </dl>
  <dl id="l_match2">
  <dt><b>match2 [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='match2' Line='match2 [string]' -->
  <dd>A column name template describing columns from the second table used
  to match the two tables. This parameter follows the same format rules
  as 'match1'. The number of columns must equal those in 'match1'.
  </dd>
  </dl>
  <dl id="l_maxnorm">
  <dt><b>maxnorm min= 0.0, max=INDEF [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxnorm' Line='maxnorm min= 0.0, max=INDEF [real]' -->
  <dd>The distance between two rows must be less than 'maxnorm' in order for
  them to match. Recognized angular units are converted to degrees
  before computing the distance. The recognized units are seconds,
  minutes, degrees, hours, radians, or any abbreviation of these.
  </dd>
  </dl>
  <dl>
  <dt><b>(incol1 = <span style="font-family: monospace;">" "</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(incol1 = " ") [string]' -->
  <dd>A column name template describing the columns to be copied from the
  first input table to the output table. If this parameter is left blank
  (the default) all columns in the first input table will be copied to
  the output.
  </dd>
  </dl>
  <dl>
  <dt><b>(incol2 = <span style="font-family: monospace;">" "</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(incol2 = " ") [string]' -->
  <dd>A column name template describing the columns to be copied from the
  second input table to the output table. If this parameter is left
  blank (the default) all columns in the second input table will be
  copied to the output.
  </dd>
  </dl>
  <dl>
  <dt><b>(factor = <span style="font-family: monospace;">" "</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(factor = " ") [string]' -->
  <dd>A comma or white space separated list of numeric factors multiplied by
  the individual column differences when computing the distance between
  rows in the first and second tables. If this parameter is left blank
  (the default) conversion of angular units to degrees will be
  performed, but not other weighting will be performed. If a list of
  values is supplied, units conversion will NOT be performed, the
  supplied numeric factors will be used instead.
  </dd>
  </dl>
  <dl>
  <dt><b>(diagfile = <span style="font-family: monospace;">" "</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(diagfile = " ") [string]' -->
  <dd>The name of the diagnostic output file. If the name is left blank (the
  default) no diagnostic output is produced. Diagnostic output can be
  sent to the terminal by setting this parameter to STDOUT or STDERR.
  The diagnostic output contains a list of rows that were not matched,
  cases where more than one row in the first table matched a single row
  in the second table, and the ten pairs of rows with the largest
  distance between them.
  </dd>
  </dl>
  <dl>
  <dt><b>(nmcol1 = <span style="font-family: monospace;">" "</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nmcol1 = " ") [string]' -->
  <dd>A column template describing the columns from the first table that are
  printed in the diagnostic output. The table and row number are always
  printed, if this parameter is not blank, the specified columns are
  also printed.
  </dd>
  </dl>
  <dl>
  <dt><b>(nmcol2 = <span style="font-family: monospace;">" "</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nmcol2 = " ") [string]' -->
  <dd>A column template describing the columns from the second table that are
  printed in the diagnostic output.
  </dd>
  </dl>
  <dl>
  <dt><b>(sphere = no) [bool]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(sphere = no) [bool]' -->
  <dd>If this parameter is set to yes, a correction appropriate for
  spherical coordinates will be applied to the first column
  difference. The correction is the cosine of the average of the two
  second column values. In order for this correction to be valid, the
  first column must contain the longitude component and the second
  column the latitude component. Units should be convertable to degrees
  or an explicit conversion factor should be supplied.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Two star catalogs are being matched. They both have the following
  columns:
  </p>
  <div class="highlight-default-notranslate"><pre>
  Name             CH*12      %12s ""
  RA               D        %10.1h hours
  Dec              D        %10.0h degrees
  V                R         %7.2f ""
  B-V              R         %7.2f ""
  U-B              R         %7.2f ""
  </pre></div>
  <p>
  To find the best match between the catalogs within a ten arcsecond
  radius one would use the following command:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tmatch catalog1.tab catalog2.tab match.tab \
  &gt;&gt;&gt; ra,dec ra,dec 0:00:10 sphere+
  </pre></div>
  <p>
  The search radius can either be supplied in sexagesimal notation, as
  above, or in decimal degrees.
  </p>
  <p>
  2. Suppose the input catalogs did not contain units information, as
  would be the case if they were text files. The units conversion could
  then be supplied explicitly through the factor parameter:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tmatch catalog1.tab catalog2.tab match.tab \
  &gt;&gt;&gt; ra,dec ra,dec 0:00:10 factor=15,1 sphere+
  </pre></div>
  <p>
  3. Suppose we want the output table to only contain the name from the
  first catalog and get the rest of its information from the second
  catalog. This could be done with the following command:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tmatch catalog1.tab catalog2.tab match.tab \
  &gt;&gt;&gt; ra,dec ra,dec 0:00:10 incol1=name sphere+
  </pre></div>
  <p>
  4. To get diagnostic output from the task, use the following command:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tmatch catalog1.tab catalog2.tab match.tab ra,dec ra,dec \
  &gt;&gt;&gt; diag=diag.txt nmcol1=name nmcol2=name 0:00:10 sphere+
  </pre></div>
  <p>
  The following is a subset of the diagnostic output produced:
  </p>
  <div class="highlight-default-notranslate"><pre>
  The following objects matched the same object:
  1:163 6601  GEM
  1:164 6601  GEM
  2:163 6601  GEM
  
  The following objects have the largest norms:
  Norm = 0.00253
  1:371 2319  SCO
  2:371 2319  SCO
  
  Norm = 0.00247
  1:368 2101  SCO
  2:368 2101  SCO
  </pre></div>
  <p>
  The number before the colon is the table number, the number after the
  colon is the row number, and the rest of the line is from the name
  column.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by Bernie Simon
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  tjoin
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

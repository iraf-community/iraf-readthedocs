.. _thistogram:

thistogram: Make a histogram of a column in a table.
====================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  thistogram intable outtable column
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task generates a histogram of the values in a column.
  The histogram may be written to STDOUT or to a table.
  If there is more than one table in the input list then a separate histogram
  is generated for each table.
  If there is more than one input table and the histogram of the values
  in all the tables combined is needed, then the tables should first be
  merged using the 'tmerge' task with the 'option' parameter set to <span style="font-family: monospace;">"append"</span>.
  </p>
  <p>
  If x1 and x2 are the lower and upper limits of a particular bin,
  a value X will be included in the bin if x1 &lt;= X &lt; x2.
  Note that this also applies to the upper limit ('highval') of the last bin.
  </p>
  <p>
  There are six interrelated parameters
  having to do with the number of bins, bin width, and bin locations.
  Any number of these may be specified as long as the values are consistent.
  As a minimum, only one value is required, either 'nbins' or 'dx'.
  The task computes what it doesn't have
  based on the parameters that were specified,
  or based on the minimum and maximum data values
  in the table column if necessary.
  If the minimum (maximum) column data value is used,
  that value will normally be reduced (increased) a bit
  before being used as 'lowval' ('highval')
  to ensure that the value is included in the range.
  The relationships between the parameters is as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  dx = (highval - lowval) / nbins
  dx = (chigh - clow) / (nbins - 1)
  clow = lowval + dx / 2
  chigh = highval - dx / 2
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [file name template]' -->
  <dd>A list of input tables.
  A histogram will be generated for one column in the table;
  the same column name is used for each table in the list.
  The name of the column is specified using the 'column' parameter,
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable = STDOUT [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable = STDOUT [file name template]' -->
  <dd>Output tables or STDOUT.
  If the value of this parameter is <span style="font-family: monospace;">"STDOUT"</span>
  then the histogram will be written to the standard output
  preceded by a header line (beginning with <span style="font-family: monospace;">"#"</span>)
  that gives the number of rows included in the histogram
  and the name of the table.
  If 'outtable' is passed a file name,
  then the number of names must match the number of file names in 'intable',
  and the histogram of each input table 
  will be written to an output table of the specified name.
  </dd>
  </dl>
  <dl id="l_column">
  <dt><b>column [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='column' Line='column [string]' -->
  <dd>Column name in input tables that will be used to generate the histogram.
  Only the values in the column with this name will be used.
  The same column name is used for each input table.
  </dd>
  </dl>
  <dl>
  <dt><b>(nbins = 100) [integer, min=1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nbins = 100) [integer, min=1]' -->
  <dd>Number of bins in the histogram.
  Normally either 'nbins' or 'dx' (or both) must be given.
  You could also give both 'lowval' and 'clow',
  or both 'chigh' and 'highval',
  since the bin width can be computed from these.
  </dd>
  </dl>
  <dl>
  <dt><b>(lowval = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(lowval = INDEF) [real]' -->
  <dd>Lower limit for histogram.
  Values below 'lowval' will not be used in generating the histogram.
  If 'lowval = INDEF', then the minimum value in the table column will be used.
  </dd>
  </dl>
  <dl>
  <dt><b>(highval = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(highval = INDEF) [real]' -->
  <dd>Upper limit for histogram.
  Values equal to or greater than 'highval' will not be used in generating
  the histogram.
  If 'highval = INDEF', then the maximum value in the table column will be used.
  </dd>
  </dl>
  <dl>
  <dt><b>(dx = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(dx = INDEF) [real]' -->
  <dd>Bin width.
  </dd>
  </dl>
  <dl>
  <dt><b>(clow = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(clow = INDEF) [real]' -->
  <dd>Value at the center of the first bin.
  </dd>
  </dl>
  <dl>
  <dt><b>(chigh = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(chigh = INDEF) [real]' -->
  <dd>Value at the center of the last bin.
  </dd>
  </dl>
  <dl>
  <dt><b>(rows = -) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(rows = -) [string]' -->
  <dd>Range of rows to use for generating the histogram.
  The default <span style="font-family: monospace;">"-"</span> means that all rows are used.
  (Type <span style="font-family: monospace;">"help xtools.ranges"</span> for more information.)
  </dd>
  </dl>
  <dl>
  <dt><b>(outcolx = value) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outcolx = value) [string]' -->
  <dd>Column name for bin centers.
  If the output is written to a table rather than to STDOUT, then 'outcolx'
  is the column name containing the bin centers.
  This column will be double precision.
  </dd>
  </dl>
  <dl>
  <dt><b>(outcoly = counts) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outcoly = counts) [string]' -->
  <dd>Column name for histogram values.
  If the output is written to a table then 'outcoly' is the column name
  containing the number of counts in the bin.
  This column will be of integer data type.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Generate a histogram of the values in the 'flux' column in every table
  whose name begins with <span style="font-family: monospace;">"hr"</span>; put all the histograms in the ASCII file
  'hist.lis'.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thistogram hr*.tab STDOUT flux &gt; hist.lis
  </pre></div>
  <p>
  2.  Generate the same histograms as in the previous example, but put the
  results in tables rather than displaying them on the terminal screen. 
  One output file is produced for each input table; for example,
  the histogram for an input table 'hr465.tab' would be put in 'hr465h.tab'.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thistogram hr*.tab hr*%%h%.tab flux
  </pre></div>
  <p>
  3.  Plot the histogram of column <span style="font-family: monospace;">'V'</span> in 'bs.tab':
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thistogram bs STDOUT V | sgraph (crvstyle="pseudohist")
  </pre></div>
  <p>
  4.  Plot the same histogram as in the previous example,
  but set the spacing between bins to be 0.1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thistogram bs STDOUT V nbins=INDEF dx=0.1 | \\
  &gt;&gt;&gt;   sgraph (crvstyle="pseudohist")
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
  ranges
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

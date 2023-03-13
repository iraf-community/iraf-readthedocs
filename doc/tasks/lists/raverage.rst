.. _raverage:

raverage: Running average, standard deviation, and envelope
===========================================================

**Package: lists**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  raverage input nwin
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input one or two column list of numbers.  Any line that can't be read
  as one or two numbers is ignored which means comments are allowed.  The
  special name <span style="font-family: monospace;">"STDIN"</span> may be used to read the numbers from the standard
  input pipe or redirection.
  </dd>
  </dl>
  <dl id="l_nwin">
  <dt><b>nwin</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nwin' Line='nwin' -->
  <dd>The number of values in the running average window.
  </dd>
  </dl>
  <dl id="l_sort">
  <dt><b>sort = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sort' Line='sort = no' -->
  <dd>Numerically sort the first column of the input list by increasing value?
  This is done in an temporary file and the
  actual input file is not modified.
  </dd>
  </dl>
  <dl id="l_nsig">
  <dt><b>nsig = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsig' Line='nsig = 0' -->
  <dd>The number of standard deviations below and above the average for the
  envelope columns.  If the value is greater than zero two extra columns
  are output formed by subtracting and adding this number of standard
  deviations to the average value.  If the value is zero then the
  columns not be written.
  </dd>
  </dl>
  <dl id="l_fd1">
  <dt><b>fd1, fd2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fd1' Line='fd1, fd2' -->
  <dd>Internal parameters.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task computes the running average and standard deviation of a
  one or two column list.  For a one column list the ordinal value is
  added.  Note that the ordinal is only for the lines that are successfully
  read so any comments are not counted.  So the internal list is always
  two columns.
  </p>
  <p>
  The input may be a physical file or the standard input.  The standard
  input is specified by the special name <span style="font-family: monospace;">"STDIN"</span>.  All the input values
  are read and stored in a temporary file prior to computing the output.
  A temporary file is also used if the input is to be numerically sorted
  by increasing value of the first column.  Note that the sorting is done
  before adding the implied ordinal for one column lists.
  </p>
  <p>
  The output has four or six columns depending on whether <i>nsig</i> is
  zero or greater than zero.
  </p>
  <div class="highlight-default-notranslate"><pre>
  average1 average1 stddev number [lower upper]
  </pre></div>
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=' ' -->
  <dd>average1
  the running average of the first column
  </dd>
  </dl>
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=' ' -->
  <dd>average2
  the running average of the second column
  </dd>
  </dl>
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=' ' -->
  <dd>stddev
  standard deviation of the second column
  </dd>
  </dl>
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=' ' -->
  <dd>number
  number of values in the statistic
  </dd>
  </dl>
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=' ' -->
  <dd>lower
  optional lower envelope value
  </dd>
  </dl>
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=' ' -->
  <dd>upper
  optional upper envelope value
  </dd>
  </dl>
  <p>
  The <span style="font-family: monospace;">"number"</span> of values may be less than the window if the window size is
  larger than the list.
  </p>
  <p>
  The number of lines will generally be less than the input because there is
  no boundary extension.  In other words the first output value is computed
  after the first <i>nwin</i> values have been read and the last output value
  is computed when the end of the list is reached.
  </p>
  <p>
  The envelope columns are computed when <i>nsig</i> is greater than zero.
  The values are
  </p>
  <div class="highlight-default-notranslate"><pre>
  lower = average2 - nsig * stddev
  upper = average2 + nsig * stddev
  </pre></div>
  <p>
  In many cases the data is intended to represent a scatter plot and one
  wants to show the trend and envelope as a function of the first column.
  This is where the sorting and envelope options are useful.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Compute the running average with a window of 100 values on the list of
  numbers in file <span style="font-family: monospace;">"numbers"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; raverage numbers 100
  </pre></div>
  <p>
  2.  Do this using the standard input.  In this example use random numbers.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; urand 100 1 | raverage STDIN 90
  </pre></div>
  <p>
  3.  Make a scatter plot of a two column list with the trend and envelope
  overplotted.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fields numbers 1,3 | graph point+
  cl&gt; fields numbers 1,3 | raverage STDIN 100 sort+ nsig=3 &gt; tmp
  cl&gt; fields tmp 1,2 | graph append+
  cl&gt; fields tmp 1,5 | graph append+
  cl&gt; fields tmp 1,6 | graph append+
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  average, boxcar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

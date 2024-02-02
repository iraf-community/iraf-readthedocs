.. _xyztable:

xyztable: Interpolate table values, writing results to a table.
===============================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xyztable intable1 intable2 outtable
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This routine reads tables -- or text files in row/column format --
  and writes output tables.
  An input table or file contains columns of X, Y (if 2-D), and Z values.
  This task fits a surface to Z as a polynomial function of X and Y.
  From a second input table,
  the (X, Y) independent variable values are read,
  the fit is evaluated for those arguments,
  and the (X, Y) and function values are written to the output table.
  The function that is to be fit may be expressed as a
  Chebyshev or Legendre polynomial or as an ordinary power series.
  The IRAF gsurfit package is used to fit and evaluate the function.
  </p>
  <p>
  Header parameters are added to the output tables
  to give some information on the fit.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable1">
  <dt><b>intable1 [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable1' Line='intable1 [file name template]' -->
  <dd>List of input tables or text files
  containing the data to which the surface will be fit.
  See also 'xname', 'yname', 'zname',
  which are used to specify the column names.
  The same names are used for all input tables.
  </dd>
  </dl>
  <dl id="l_intable2">
  <dt><b>intable2 [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable2' Line='intable2 [file name template]' -->
  <dd>Names of input tables or text files
  containing the independent variable values
  at which the fitted surface will be evaluated.
  The number of names in this list must be the same as
  the number given in 'intable1'.
  The same column names 'xname' (and 'yname' if 2-D) as for 'intable1'
  are used for the columns of independent variable values,
  but 'zname' need not be present.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [file name template]' -->
  <dd>List of output tables.
  The number of output files must be the same as
  the number of input files given in 'intable1'.
  The output table is created as a copy of 'intable2',
  except that history records are added,
  and the 'zname' column is added to contain the results of the fit.
  </dd>
  </dl>
  <dl>
  <dt><b>(xname = <span style="font-family: monospace;">"c1"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(xname = "c1") [string]' -->
  <dd>Name of column for X values.
  This parameter is used to specify which column
  in the input tables (both 'intable1' and 'intable2')
  contains the X values.
  X and Y are the independent variables (or just X for 1-D),
  and Z is the dependent variable.
  The default of <span style="font-family: monospace;">"c1"</span> is appropriate for the case that 'intable1'
  and 'intable2' are text files with X values in the first column.
  If 'intable1' lists more than one file name,
  the same column names are used for all files.
  </dd>
  </dl>
  <dl>
  <dt><b>(yname = <span style="font-family: monospace;">"c2"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(yname = "c2") [string]' -->
  <dd>Name of column for Y values.
  For a one-dimensional fit,
  you can either set 'yorder' to zero or
  set 'yname' to null or blank.
  Note that 'zname' is the column name for the dependent variable
  regardless of whether a 1-D or 2-D fit is desired.
  See also the description for 'xname'.
  </dd>
  </dl>
  <dl>
  <dt><b>(zname = <span style="font-family: monospace;">"c3"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(zname = "c3") [string]' -->
  <dd>Name of column for Z values.
  This column contains the dependent variable values.
  For a 1-D fit, values should be specified for 'xname' and 'zname',
  and 'yname' will not be used.
  See also the description for 'xname'.
  </dd>
  </dl>
  <dl>
  <dt><b>(xorder = 2 [integer, min=1, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(xorder = 2 [integer, min=1, max=INDEF]' -->
  <dd>Number of coefficients for function in X.
  This number does not include coefficients for cross terms.
  For example, if 'xorder' and 'yorder' are both equal to two,
  the function will be
  <dl>
  <dt><b></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line=' ' -->
  <dd><dl>
  <dt><b>c1 + c2*X + c3*Y   if cross_terms = no,</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='c1' Line='c1 + c2*X + c3*Y   if cross_terms = no,' -->
  <dd></dd>
  </dl>
  </dd>
  </dl>
  and it will be
  <dl>
  <dt><b></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line=' ' -->
  <dd><dl>
  <dt><b>c1 + c2*X + c3*Y + c4*X*Y   if cross_terms = yes,</b></dt>
  <!-- Sec='PARAMETERS' Level=2 Label='c1' Line='c1 + c2*X + c3*Y + c4*X*Y   if cross_terms = yes,' -->
  <dd></dd>
  </dl>
  </dd>
  </dl>
  where c1, c2, c3, and c4 are the coefficients of the fit.
  </dd>
  </dl>
  <dl>
  <dt><b>(yorder = 2 [integer, min=1, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(yorder = 2 [integer, min=1, max=INDEF]' -->
  <dd>Number of coefficients for function in Y.
  For a one-dimensional fit, set 'yorder' to zero.
  </dd>
  </dl>
  <dl>
  <dt><b>(x1 = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(x1 = INDEF) [real]' -->
  <dd>The fit is performed over the range 'x1' to 'x2' and 'y1' to 'y2'.
  If 'x1' is INDEF, the minimum X value in 'intable1' will be used.
  </dd>
  </dl>
  <dl>
  <dt><b>(x2 = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(x2 = INDEF) [real]' -->
  <dd>If 'x2' is INDEF, the maximum X value in 'intable1' will be used.
  </dd>
  </dl>
  <dl>
  <dt><b>(y1 = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(y1 = INDEF) [real]' -->
  <dd>If 'y1' is INDEF, the minimum Y value in 'intable1' will be used.
  In the 1-D case (i.e. if 'yorder' is zero), 'y1' and 'y2' are ignored.
  </dd>
  </dl>
  <dl>
  <dt><b>(y2 = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(y2 = INDEF) [real]' -->
  <dd>If 'y2' is INDEF, the maximum Y value in 'intable1' will be used.
  </dd>
  </dl>
  <dl>
  <dt><b>(cross_terms = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(cross_terms = yes) [boolean]' -->
  <dd>Include cross-terms?  If this is set to no,
  the function will consist of the sum of
  a polynomial in X and a polynomial in Y.
  If cross_terms = yes,
  the function can include terms such as X*Y or (X**2)*Y.
  </dd>
  </dl>
  <dl>
  <dt><b>(function = <span style="font-family: monospace;">"chebyshev"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(function = "chebyshev") [string]' -->
  <dd>[allowed values: chebyshev | legendre | polynomial]
  Function to be fit.
  The default value of <span style="font-family: monospace;">"chebyshev"</span> is almost always appropriate.
  Numerical roundoff may be severe if <span style="font-family: monospace;">"polynomial"</span> is selected,
  so this choice is not recommended.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>Print the names of the input and output tables?
  </dd>
  </dl>
  <dl>
  <dt><b>(coefficients = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(coefficients = no) [boolean]' -->
  <dd>Print the coefficients?  The coefficients are not printed in
  user-friendly format.
  They are the values returned by the dgssave subroutine in gsurfit.
  The first eight numbers describe the fit (e.g. xorder, yorder),
  and the remaining values are the coefficients.
  These may be passed to the dgsrestore subroutine
  in order to restore these coefficients to a gsurfit structure.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Suppose the input file <span style="font-family: monospace;">"test.lis"</span> contains X, Y, and Z values
  in the first three columns as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  #  x    y    z
     0.   0.   0.
     1.   0.   1.
     0.   1.   2.
  </pre></div>
  <p>
  Fit a plane, i.e. polynomial with two coefficients for each axis
  and no cross terms.
  Use the same file <span style="font-family: monospace;">"test.lis"</span> for the list of X, Y values
  at which to evaluate the function.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; xyztable test.lis test.lis test \
  &gt;&gt;&gt; cross_terms=no function="Chebyshev"
  test.lis --&gt; test;  rms = 0.
  </pre></div>
  <p>
  2.  Table <span style="font-family: monospace;">"1d.tab"</span> contains the following:
  </p>
  <div class="highlight-default-notranslate"><pre>
   x    z
  
  -5  17.5
  -4  14.6
  -3  11.9
  -2   9.4
  -1   7.1
   0   5.0
   1   3.1
   2   1.4
   3  -0.1
   4  -1.4
   5  -2.5
   6  -3.4
  </pre></div>
  <p>
  Do a 1-D quadratic fit to these data,
  and evaluate the fit for the same X values,
  writing the output to <span style="font-family: monospace;">"1dout.tab"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; xyztable 1d.tab 1d.tab 1dout.tab \
  &gt;&gt;&gt; xname="x" zname="z" xorder=3 yorder=0
  1d.tab, 1d.tab --&gt; 1dout.tab;  rms = 1.84047E-15
  
  im&gt; tprint 1dout.tab prp+
    Table 1dout.tab  Tue 14:40:19 11-Jan-94
  
  HISTORY  t Created Tue 14:40:14 11-Jan-94
  XORDER   i 3
  RMSERR   d 1.840467264049248E-15
  HISTORY  t input table name 1d.tab
  HISTORY  t X column name x
  HISTORY  t Z column name z
  HISTORY  t a Chebyshev function was fit
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
  xyztoim, gsurfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

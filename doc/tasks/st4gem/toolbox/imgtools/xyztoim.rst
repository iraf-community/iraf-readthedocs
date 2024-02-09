.. _xyztoim:

xyztoim: Interpolate table values, writing results to an image.
===============================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xyztoim intable output
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This routine reads tables -- or text files in row/column format --
  and writes 1-D or 2-D output images.
  Each input table or file contains columns of X, Y (if 2-D), and Z values.
  This task fits a surface to Z as a polynomial function of X and Y
  and evaluates the fit at each pixel of the corresponding output image.
  The function that is to be fit may be expressed as a
  Chebyshev or Legendre polynomial or as an ordinary power series.
  The IRAF gsurfit package is used to fit and evaluate the function.
  </p>
  <p>
  A linear relationship between X &amp; Y and pixel numbers is assumed.
  X and Y cannot be right ascension and declination, for example.
  unless the declination is small.
  </p>
  <p>
  Header parameters are added to the output images
  to give some information on the fit.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [file name template]' -->
  <dd>List of input tables or text files.
  See also 'xname', 'yname', 'zname',
  which are used to specify the column names.
  The same names are used for all input tables.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name template]' -->
  <dd>List of output 1-D or 2-D images.
  The number of output images must be the same as
  the number of input tables or files.
  All images will be 1-D or all will be 2-D,
  depending on whether 'yorder' is zero or not.
  </dd>
  </dl>
  <dl>
  <dt><b>(xname = <span style="font-family: monospace;">"c1"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(xname = "c1") [string]' -->
  <dd>Name of column for X values.
  This parameter is used to specify which column in the input table
  contains the X values.
  X and Y are the independent variables (or just X for 1-D),
  and Z is the dependent variable.
  The default of <span style="font-family: monospace;">"c1"</span> is appropriate for the case that 'intable'
  is a text file with X values in the first column.
  If 'intable' lists more than one file name,
  the same column names are used for all files.
  </dd>
  </dl>
  <dl>
  <dt><b>(yname = <span style="font-family: monospace;">"c2"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(yname = "c2") [string]' -->
  <dd>Name of column for Y values.
  For a one-dimensional fit and 1-D output image,
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
  <dt><b>(nx = 512) [integer, min=1, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nx = 512) [integer, min=1, max=INDEF]' -->
  <dd>Width of image, in pixels.
  </dd>
  </dl>
  <dl>
  <dt><b>(ny = 512) [integer, min=1, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ny = 512) [integer, min=1, max=INDEF]' -->
  <dd>Height of image, in pixels.
  This is ignored if 'yorder' is zero, i.e. for a 1-D fit.
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
  <dt><b>(yorder = 2 [integer, min=0, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(yorder = 2 [integer, min=0, max=INDEF]' -->
  <dd>Number of coefficients for function in Y.
  For a one-dimensional fit and 1-D output image, set 'yorder' to zero.
  </dd>
  </dl>
  <dl>
  <dt><b>(x1 = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(x1 = INDEF) [real]' -->
  <dd>X value at first pixel.
  If 'x1' is INDEF, the minimum X value in the input table will be used.
  The parameters 'x1', 'x2', 'y1' and 'y2' serve two purposes.
  They specify the range over which the fit is to be performed,
  and they specify the values of the independent variables
  at the corners of the image.
  </dd>
  </dl>
  <dl>
  <dt><b>(x2 = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(x2 = INDEF) [real]' -->
  <dd>X value at last pixel.
  If 'x2' is INDEF, the maximum X value in the input table will be used.
  </dd>
  </dl>
  <dl>
  <dt><b>(y1 = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(y1 = INDEF) [real]' -->
  <dd>Y value at first pixel.
  If 'y1' is INDEF, the minimum Y value in the input table will be used.
  In the 1-D case (i.e. if 'yorder' is zero),
  'y1' and 'y2' are ignored.
  </dd>
  </dl>
  <dl>
  <dt><b>(y2 = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(y2 = INDEF) [real]' -->
  <dd>Y value at last pixel.
  If 'y2' is INDEF, the maximum Y value in the input table will be used.
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
  <dd>Print the names of the input table and output image?
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
  Create a 4 by 4 image <span style="font-family: monospace;">"test"</span> with X and Y values
  starting at zero at pixel (1,1) and increasing by 0.5 per pixel.
  Fit a plane, i.e. polynomial with two coefficients for each axis
  and no cross terms.
  We can use the default values for column names and order of fit.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; xyztoim test.lis test nx=4 ny=4 x1=0 y1=0 x2=1.5 y2=1.5 \
  &gt;&gt;&gt; cross_terms=no function="polynomial"
  test.lis --&gt; test;  rms = 2.31111E-16
  </pre></div>
  <p>
  The RMS error in the fit is machine roundoff in this case.
  Use listarea to examine the pixel values:
  </p>
  <div class="highlight-default-notranslate"><pre>
  fo&gt; listarea test[*,-*]
  Image:  test[*,-*]
   Sample    1     2     3     4
  Line
        4  3.0   3.5   4.0   4.5
        3  2.0   2.5   3.0   3.5
        2  1.0   1.5   2.0   2.5
        1  0.0   0.5   1.0   1.5
  </pre></div>
  <p>
  2.  File <span style="font-family: monospace;">"1d.lis"</span> contains the following:
  </p>
  <div class="highlight-default-notranslate"><pre>
  #  z = 0.1*x**2 - 2*x + 5
  # x   z
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
  Create a 1-D output image as follows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; xyztoim 1d.lis 1d.hhh xname="c1" zname="c2" nx=12 \
  &gt;&gt;&gt; xorder=3 yorder=0
  1d.lis --&gt; 1d.hhh;  rms = 1.84047E-15
  </pre></div>
  <p>
  The data values of <span style="font-family: monospace;">"1d.hhh"</span> will be the same as <span style="font-family: monospace;">"1d.lis"</span>,
  and the header will contain:
  </p>
  <div class="highlight-default-notranslate"><pre>
  CRPIX1  =                   1.
  CRVAL1  =                  -5.
  CTYPE1  = 'PIXEL   '
  CD1_1   =                   1.
  XORDER  =                    3
  RMSERR  =  1.8404672640492E-15
  HISTORY   input table name 1d.lis
  HISTORY   column names c1 c2
  HISTORY   a Chebyshev function was fit
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
  xyztable, gsurfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

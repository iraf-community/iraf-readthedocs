.. _gfit1d:

gfit1d: Interactive 1-d linear curve fit to images, tables or lists.
====================================================================

**Package: fitting**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  gfit1d input output
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task fits 1-dimensional functions, by minimizing chi-square,
  to one or more lists, image sections, table columns, or table array
  cells (<span style="font-family: monospace;">"3-D tables"</span>). Supported functions are: polynomials of Chebyshev 
  or Legendre types, linear or cubic splines. The fitting method accumulates 
  and solves the normal equations using Cholesky factorization.
  </p>
  <p>
  Lists and image sections can be mixed in the input list using wildcard
  characters.  Fit results will be written to an STSDAS table. (Table formats
  are described below). If the table does not exist, it will be created.  
  Otherwise, the fit results will be appended as the last row in the table. 
  </p>
  <p>
  If an image section operand has more than one dimension, the projection
  (i.e., average) onto a designated axis will be computed (see 'samplepars'
  pset). If the input data is in the form of image sections, then FITS 
  keywords related to transformation from pixel to world coordinates are 
  read from the image header. Those keywords are used to generate the X and 
  Y variables in physical units. Supported keywords are: 'W0', 'WPC', 
  'CRPIXn', 'CRVALn', 'CDn_n', 'CDELTn', 'DISPAXIS', 'DC-FLAG', 'BSCALE' 
  and 'BZERO' (n is the designated axis). If no suitable keywords are found, 
  then raw values (pixel number and content) are used. 
  </p>
  <p>
  The fitting parameters can be interactively set using the graphics
  cursor.  Each data set may be fitted with different functions and orders
  if the task is used interactively. The dependent variable must be
  provided in linear units. The independent variable do not need to be
  equally spaced, nor ordered. Internal computations are made in double
  precision.
  </p>
  <p>
  List input may be taken from the standard input or from a file, and 
  consists of a sequence of Y values, X and Y values, or X,Y and error 
  values; only one pair of coordinates can be placed on a line.  Blank 
  lines, comment lines, and extra columns are ignored.  The first element 
  in the list determines whether the list is a Y list or an X,Y list; it 
  is an error if an X,Y list has fewer than two coordinates in any 
  element.  INDEF valued elements are ignored.  The list does not
  need to be ordered, nor equally spaced, in X.
  </p>
  <p>
  STSDAS table input is specified by a table name and column name, a table 
  and two columns, or a pair of table and column names.  The table name 
  may be a file name template. The table name may have appended to it a
  row selector. If the specified column(s) store arrays in each cell
  (<span style="font-family: monospace;">"3-D table"</span>) the full array contents at each selected row are read and 
  used to build the 1-D data vectors. When reading from two separate columns, 
  both of them must store either scalars or arrays with same size. See the 
  <span style="font-family: monospace;">"help selectors"</span> help page in the 'tables' package.
  </p>
  <p>
  Error information, needed for properly computing chi-square, can be
  input in a variety of ways. See help page for the 'errorpars' pset.
  </p>
  <p>
  The STSDAS output table contains the information described below. Each
  particular fit will result in a new row being appended to the table.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  Column
  label           Contents
  ======          ========
  file            Name of the file on which the fit was originally performed.
  time            Date and time the fit was performed.
  function        Fitted function.
  ncoeff          Number of function coefficients (degree).
  unit            <span style="font-family: monospace;">'*'</span>
  npoints         Number of data points used in fit.
  xmin, xmax      Limits for function normalization.
  chisq           Chi-square of fit.
  rms             Root mean square of fit.
  coeff1          First coefficient.
  err1            First coefficient error.
  coeff2          Second coefficient.
  err2            Second coefficient error.
  
  </pre></div>
  <p>
  New columns are created as needed to hold any number of coefficients. 
  The total number of columns in the table will depend on the maximum order 
  used in a particular fit. 
  </p>
  <p>
  The 'ps' parameter allows the user to control which coefficients will be 
  written to the output table. If 'ps=yes', then straight power-series 
  polynomial coefficients are output. If 'ps=no', Legendre or Chebyshev 
  orthogonal polynomial coefficients are output instead. This parameter has 
  no effect when fitting splines.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name template]' -->
  <dd>List of operands to be fitted.  This parameter can be set to STDIN, or 
  one or more image sections, tables and columns, or lists. 
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name]' -->
  <dd>Output table that will contain fitting information.
  </dd>
  </dl>
  <dl>
  <dt><b>(function = <span style="font-family: monospace;">"spline3"</span>) [string, allowed values: spline3 | legendre |</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(function = "spline3") [string, allowed values: spline3 | legendre |' -->
  <dd>chebyshev | spline1]
  Fitting function to be used.
  </dd>
  </dl>
  <dl>
  <dt><b>(order = 1) [integer, min=1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(order = 1) [integer, min=1]' -->
  <dd>Order of the fitting function.
  </dd>
  </dl>
  <dl>
  <dt><b>(xmin = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(xmin = INDEF) [real]' -->
  <dd>Value of the independent variable corresponding to the lower limit
  for function normalization. If INDEF, the minimum X will be used.
  The same value holds for all files in the input list.
  </dd>
  </dl>
  <dl>
  <dt><b>(xmax = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(xmax = INDEF) [real]' -->
  <dd>Value of the independent variable corresponding to the upper limit
  for function normalization. If INDEF, the maximum X will be used.
  The same value holds for all files in the input list.
  </dd>
  </dl>
  <dl>
  <dt><b>(ps = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ps = yes) [boolean]' -->
  <dd>Write the coefficients as in a power-series polynomial? (Only when fitting
  Chebyshev and Legendre functions).
  </dd>
  </dl>
  <dl>
  <dt><b>(errorpars = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(errorpars = "") [string]' -->
  <dd>The name of the file containing the error-related parameters (pset).
  </dd>
  </dl>
  <dl>
  <dt><b>(samplepars = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(samplepars = "") [string]' -->
  <dd>The name of the file containing the sampling parameters (pset).
  </dd>
  </dl>
  <dl>
  <dt><b>(interactive = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(interactive = yes) [boolean]' -->
  <dd>Set the fitting parameters interactively?
  </dd>
  </dl>
  <dl>
  <dt><b>(device = <span style="font-family: monospace;">"stdgraph"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(device = "stdgraph") [string]' -->
  <dd>Graphics output device.
  </dd>
  </dl>
  <dl>
  <dt><b>(cursor) [graphics cursor file]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(cursor) [graphics cursor file]' -->
  <dd>Graphics cursor input.  (Type <span style="font-family: monospace;">"help vdisplay.tvcursor"</span> for more 
  information about the IRAF cursor facility.)
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Fit a section of the image 'test' and store the fit results in the 
  table 'testfit.tab' in the user's home directory:
  </p>
  <div class="highlight-default-notranslate"><pre>
  fi&gt; gfit1d test[100:500,256:300] home$testfit
  </pre></div>
  <p>
  2. Fit spectral order 80 to 83 on an echelle STIS extracted spectrum:
  </p>
  <div class="highlight-default-notranslate"><pre>
  fi&gt; gfit1d "file.fits[r:SPORDER=80:83] WAVELENGTH FLUX" output
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  In the graphics window banner, it is not possible to write the chi-square
  of the fit, because these graphics are handled by an internal IRAF 
  library, which can only write the rms of the fit. Use the :chisq colon
  command to see the current chi-square value.
  </p>
  <p>
  See also the BUGS section of the 'errorpars' pset.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by I.Busko
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  errorpars, samplepars, icfit, selectors
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

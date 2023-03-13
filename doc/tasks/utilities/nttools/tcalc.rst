.. _tcalc:

tcalc: Perform arithmetic operations on table columns.
======================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tcalc table outcol equals
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task evaluates an arbitrary expression that includes column names,
  constants, and operators, and creates a specified column in the 
  table---or overwrites an existing column if the specified name already exists.
  Variables in the expression are column names in either case. 
  </p>
  <p>
  Columns
  may be of any type except string. If the column name contains
  non-alphanumeric characters, it should be preceded by a dollar sign
  and followed by a blank. For example, the expression <span style="font-family: monospace;">"date-obs+1."</span>
  contains the column <span style="font-family: monospace;">"date-obs"</span>, but the task thinks that it contains
  two column names, <span style="font-family: monospace;">"date"</span> and <span style="font-family: monospace;">"obs"</span>.  To ensure that the expression is
  evaluated correctly, rewrite it as <span style="font-family: monospace;">"$date-obs +1."</span>. The variable
  <span style="font-family: monospace;">"rownum"</span> may also be used in an expression if there is no column in
  the table of the same name. Its value is the current row number. The
  expression will be evaluated using the data types of the columns and
  constants in the expression, with the usual rules of type promotion used in
  Fortran.  Please remember that integer division truncates.
  </p>
  <p>
  The output value in any row will be set to INDEF if one or more column
  values used in the calculation is equal to INDEF. The result will be
  INDEF if either of the clauses in an if expression contains a row with
  an INDEF value. If the result of an operation is undefined (such as
  division by zero) the output column will also be set to INDEF.
  </p>
  <p>
  The following Fortran-type arithmetic operators are supported.  If the
  second argument of the exponentiation is not an integer, the result
  will be undefined if the first argument is not positive.  Again, 
  remember that integer division truncates.
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  +       addition                -       subtraction
  *       multiplication          /       division
  -       negation                **      exponentiation
  </pre></div>
  <p>
  The following logical operators are supported. Logical operators will
  return a value of 1 if true or 0 if false. Logical operators are
  supported in both their Fortran and SPP form.
  </p>
  <div class="highlight-default-notranslate"><pre>
  .or. ||                logical or      .and.   &amp;&amp;      logical and
  .eq. ==                equality        .ne.    !=      inequality
  .lt. &lt;         less than       .gt.    &gt;       greater than
  .le. &lt;=                less or equal   .ge.    &gt;=      greater or equal
  .not. !                not
  </pre></div>
  <p>
  The following functions are supported. These functions all take a
  single argument, which may be an expression. The argument or result of
  trigonometric functions are in radians.
  </p>
  <div class="highlight-default-notranslate"><pre>
  abs     absolute value          acos    arc cosine
  asin    arc sine                atan    arc tangent
  cos     arc cosine              cosh    hyperbolic cosine
  cube    third power             double  convert to double
  exp     E raised to power       int     convert to integer
  log     natural logarithm       log10   common logarithm
  nint    nearest integer         real    convert to real
  sin     sine                    sinh    hyperbolic sine
  sqr     second power            sqrt    square root
  tan     tangent                 tanh    hyperbolic tangent
  </pre></div>
  <p>
  The following functions take two arguments.
  </p>
  <div class="highlight-default-notranslate"><pre>
  atan2   arc tangent             dim     positive difference
  max     maximum                 min     minimum
  mod     modulus                 sign    sign transfer
  </pre></div>
  <p>
  Conditional expressions of the form <span style="font-family: monospace;">"if expr then expr else expr"</span> are
  supported. The expression after the else may be another conditional
  expression.  The words <span style="font-family: monospace;">"if"</span>, <span style="font-family: monospace;">"then"</span>, and <span style="font-family: monospace;">"else"</span> must be surrounded by
  blanks.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table  [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table  [file name template]' -->
  <dd>The input table, or tables; these files are modified in-place.
  Results will be written to a new column in the table unless an
  existing column name is specified, in which case the existing values
  will be overwritten.
  </dd>
  </dl>
  <dl id="l_outcol">
  <dt><b>outcol [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outcol' Line='outcol [string]' -->
  <dd>Output column name.  This is the column where results are written.
  Caution: if this column already exists, then it will be overwritten
  with the results of the calculation.  Note that column names are not
  case sensitive.
  </dd>
  </dl>
  <dl id="l_equals">
  <dt><b>equals [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='equals' Line='equals [string]' -->
  <dd>The arithmetic expression to evaluate. If the expression is too long
  to pass as a parameter, place the expression in a file and set the
  value of this parameter to the file name preceded by an <span style="font-family: monospace;">"@"</span>, for
  example, <span style="font-family: monospace;">"@filename"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>(datatype = real) [string, allowed values: real | double | int ]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(datatype = real) [string, allowed values: real | double | int ]' -->
  <dd>Type of data stored in the output column, if it is a new column.
  </dd>
  </dl>
  <dl>
  <dt><b>(colunits) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(colunits) [string]' -->
  <dd>Units for the output column, if it is a new column.  This parameter
  may be blank.
  </dd>
  </dl>
  <dl>
  <dt><b>(colfmt) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(colfmt) [string]' -->
  <dd>Print format for the output column, if it is a new column.  If this
  parameter is left blank then a default will be used.  Type <span style="font-family: monospace;">"help
  ttools opt=sysdoc"</span> for more information about print formats.
  </dd>
  </dl>
  </section>
  <section id="s_examples_">
  <h3>Examples </h3>
  <p>
  1.  Create a column called 'FLUX', which will contain a value equal to
  10.0**(-x/2.5) where x is the value in the column 'MAG'.  The new
  column will contain single precision data.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tcalc "intab" "FLUX" "10.0**(-mag/2.5)"
  </pre></div>
  <p>
  2.  Create a column called 'POLY', which will contain a value equal to
  x+x**2 where x is the row number in the table.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tcalc "test" "POLY" "rownum+sqr(rownum)"
  </pre></div>
  <p>
  3.  Set quotient to zero where divison by zero would otherwise occur:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tcalc "test" "QUOT" "if y != 0 then x / y else 0."
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
  imcalc
  </p>
  <p>
  Type <span style="font-family: monospace;">"help ttools opt=sys"</span> for a higher-level description of the 'tables' 
  package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES ' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

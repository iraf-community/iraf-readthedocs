.. _mskexpr:

mskexpr: Create masks using an expression and reference images
==============================================================

**Package: proto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mskexpr expr masks refimages
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_expr">
  <dt><b>expr</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expr' Line='expr' -->
  <dd>The expression to be evaluated.  This may be the actual expression, or the
  string <span style="font-family: monospace;">"@file"</span> in which case the expression is taken from the named file.
  </dd>
  </dl>
  <dl id="l_masks">
  <dt><b>masks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='masks' Line='masks' -->
  <dd>The output masks. The size of the output masks defaults to the size of
  the reference image if any, the size of the reference mask if any, or the
  value of the dims parameter, in that order.
  </dd>
  </dl>
  <dl id="l_refimages">
  <dt><b>refimages</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refimages' Line='refimages' -->
  <dd>The optional list of reference images. If the reference image list is defined
  there must be one reference image for every output mask. The reference image
  operand name is <span style="font-family: monospace;">"i"</span> and the associated reference image keywords are
  referred to as <span style="font-family: monospace;">"i.&lt;keyword&gt;"</span>.
  </dd>
  </dl>
  <dl id="l_refmasks">
  <dt><b>refmasks</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refmasks' Line='refmasks' -->
  <dd>The optional list of reference masks. If the reference mask list is defined
  there must be one reference mask for every output mask. The reference mask
  operand name is <span style="font-family: monospace;">"m"</span> and the associated reference image keywords are
  referred to as <span style="font-family: monospace;">"m.&lt;keyword&gt;"</span>.
  If both a reference image and reference mask are defined the reference mask will
  be matched to reference image as described by the help topic <b>pmmatch</b>.
  The application default is a match in <span style="font-family: monospace;">"logical"</span> coordinates which is
  effectively a trim or pad operation to match the size of the reference image.
  However, by use of the <span style="font-family: monospace;">"pmmatch"</span> environment variable one may match in
  <span style="font-family: monospace;">"physcial"</span> or <span style="font-family: monospace;">"world"</span> coordinates.  Note that the simple expression
  <span style="font-family: monospace;">"m"</span> may be used to create an output mask file from the internal matching.
  </dd>
  </dl>
  <dl id="l_dims">
  <dt><b>dims = <span style="font-family: monospace;">"512,512"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dims' Line='dims = "512,512"' -->
  <dd>The default output mask dimensions. The value of dims is a comma delimited
  list of dimensions.
  </dd>
  </dl>
  <dl id="l_depth">
  <dt><b>depth = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='depth' Line='depth = 0' -->
  <dd>The output mask depth in bits. The maximum depth and current default is
  27.
  </dd>
  </dl>
  <dl id="l_exprdb">
  <dt><b>exprdb = <span style="font-family: monospace;">"none"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exprdb' Line='exprdb = "none"' -->
  <dd>The file name of an optional expression database. An expression database
  may be used to define symbolic constants or a library of custom function
  macros.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print task status messages ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Mskexpr evaluates a mask expression <i>expr</i> and writes the results to an
  output mask <i>masks</i> image. If expr is preceded by an <span style="font-family: monospace;">"@"</span> sign then
  the expression is read from the named file.  The size of the output mask is
  determined by the reference image <i>refimages</i> if any, the reference masks
  <i>refmasks</i> if any, or the values of the <i>dims</i> parameter, in that
  order of precedence.
  </p>
  <p>
  The output mask is an integer image. Therefore any mask expression must
  evaluate to an integer value. The depth of the output mask in bits is defined
  by the <i>depth</i> parameter. The default value is 27 bits.
  </p>
  <p>
  Evaluation of the mask expression is carried out one line at a time. This
  is efficient and permits operations on masks with large reference images
  to be carried out efficiently without using excessive memory. The entire
  expression is evaluated once per line of the output mask.
  </p>
  <p>
  <b>Reference Images and Masks</b>
  </p>
  <p>
  In most cases one wants to make output masks to associate with images.
  The reference image list provides a reference image which is used to
  define the size and some of the header for the output mask.  Note that
  a reference mask may be used for this purpose if no reference image
  is specified.
  </p>
  <p>
  Sometimes one may want to merge previous mask information into the output
  mask.  The reference mask can be used for this purpose using the operand
  <span style="font-family: monospace;">"m"</span> in the expressions.
  </p>
  <p>
  When both a reference image and a reference mask are specified another
  useful feature is provided.  This consists of matching the reference
  mask to the reference image even when the two are of different sizes or
  are related not <span style="font-family: monospace;">"pixel-by-pixel"</span> but through various transformations.
  The matching feature is described in the help topic <b>pmmatch</b>.
  (Note that the default for matching in world coordinates results in
  boolean mask values so if the actual mask values are needed the pmmatch
  setting must be set appropriately.)  The application default is a match
  in <span style="font-family: monospace;">"logical"</span> coordinates which is effectively a trim or pad operation to
  match the size of the reference image.  However, by use of the <span style="font-family: monospace;">"pmmatch"</span>
  environment variable one may match in <span style="font-family: monospace;">"physcial"</span> or <span style="font-family: monospace;">"world"</span> coordinates.
  </p>
  <p>
  This task is one way to create a matched mask for tasks that do not
  do the matching.  The simple expression <span style="font-family: monospace;">"m"</span> when both a reference image
  and reference mask are specified will output a mask from for the reference
  image that is match in logical pixel space.
  </p>
  <p>
  <b>Operands</b>
  </p>
  <p>
  Input operands are represented symbolically in the input expression. Use of
  symbolic operands allows the same expression to be used with different data
  sets, simplifies the expression syntax, and allows a single input image
  to be used several places in the same expression.
  </p>
  <p>
  The following operands are recognized:
  </p>
  <div class="highlight-default-notranslate"><pre>
  i               reference image
  i.itime         reference image keyword
  m               reference mask
  m.itime         reference mask keyword
  1.2345          numeric constant
  </pre></div>
  <p>
  Finally, there is a special builtin type of operand used to represent the
  mask pixel coordinates in a mask expression.  These operands have the
  special reserved names <span style="font-family: monospace;">"I"</span>, <span style="font-family: monospace;">"J"</span>, <span style="font-family: monospace;">"K"</span>, etc., up to the dimensions of the
  output image.  The names must be upper case to avoid confusion to with the
  input operands <span style="font-family: monospace;">"i"</span> and <span style="font-family: monospace;">"m"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  I                x coordinate of pixel (column)
  J                y coordinate of pixel (line)
  K                z coordinate of pixel (band)
  </pre></div>
  <p>
  <b>Operators</b>
  </p>
  <p>
  The expression syntax implemented by mskexpr provides the following
  set of operators:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ( expr )                grouping
  + - * /                 arithmetic
  **                      exponentiation
  //                      concatenate
  expr ? expr1 : expr2    conditional expression
  @ "name"                get operand
  
  &amp;&amp;                      logical and
  ||                      logical or
  !                       logical not
  &lt;                       less than
  &lt;=                      less than or equal
  &gt;                       greater than
  &gt;=                      greater than or equal
  ==                      equals
  !=                      not equals
  ?=                      substring equals
  
  &amp;                       bitwise and
  |                       bitwise or
  ^                       bitwise exclusive or
  ~                       bitwise not
  </pre></div>
  <p>
  The conditional expression has the value <i>expr1</i> if <i>expr</i> is true,
  and <i>expr2</i> otherwise.  Since the expression is evaluated at every pixel
  this permits pixel-dependent operations such as checking for special pixel
  values, or selection of elements from either of two vectors.  For example,
  the command
  </p>
  <p>
          (i &gt; -10 &amp;&amp; i &lt; 32000) ? 0 : 1
  </p>
  <p>
  has the constant value 0 if the reference image is greater than -10 and less
  than 32000, and 1 otherwise. Conditional expressions are general expressions
  and may be nested or used anywhere an expression is permitted.
  </p>
  <p>
  The concatenation operator applies to all types of data, not just strings.
  Concatenating two vectors results in a vector the combined length of the
  two input vectors.
  </p>
  <p>
  The substring equals operator <span style="font-family: monospace;">"?="</span>, used for string comparisons,  is like
  <span style="font-family: monospace;">"=="</span> but checks for the presence of a substring, rather than exact equality
  of the two strings.
  </p>
  <p>
  <b>Region Functions</b>
  </p>
  <p>
  Mskexpr supports a group of boolean region functions which can be used to set
  values inside or outside of certain geometric shapes. The routines may be
  called in two ways. The first way assumes that the output masks are two-
  dimensional. The second way assumes that they are multi-dimensional and
  specifies which dimensions the geometric operator applies to.
  </p>
  <div class="highlight-default-notranslate"><pre>
      point (x1, y1)
     circle (xc, yc, r)
    ellipse (xc, yc, r, ratio, theta)
        box (x1, y1, x2, y2)
  rectangle (xc, yc, r, ratio, theta)
     vector (x1, y1, x2, y2, width)
        pie (xc, yc, theta1, theta2)
    polygon (x1, y1, ..., xn, yn)
       cols (ranges)
      lines (ranges)
   cannulus (xc, yc, r1, r2)
   eannulus (xc, yc, r1, r2, ratio, theta)
   rannulus (xc, yc, r1, r2, ratio, theta)
   pannulus (width, x1, y1, ..., xn, yn)
  
      point (I, J, x1, y1)
     circle (I, J, xc, yc, r)
    ellipse (I, J, xc, yc, r, ratio, theta)
        box (I, J, x1, y1, x2, y2)
  rectangle (I, J, xc, yc, r, ratio, theta)
     vector (I, J, x1, y1, x2, y2, width)
        pie (I, J, xc, yc, theta1, theta2)
    polygon (I, J, x1, y1, .., xn, yn)
       cols (I, ranges)
      lines (J, ranges)
   cannulus (I, J, xc, yc, r1, r2)
   eannulus (I, J, xc, yc, r1, r2, ratio, theta)
   rannulus (I, J, xc, yc, r1, r2, ratio, theta)
   pannulus (I, J, width, x1, y1, ..., xn, yn)
  
      xc,yc - center coordinates in pixels
      r1,r2 - semi-major axis lengths in pixels
      ratio - ratio of semi-minor / semi-major axes
   theta[n] - position angle in degrees
      x1,y1 - starting coordinates in pixels
      x2,y2 - ending coordinates in pixels
  x[n],y[n] - vertices of a polygon
     ranges - string defining a range, e.g. "100-200,300,400-500"
  </pre></div>
  <p>
  <b>Other Functions</b>
  </p>
  <p>
  Where it makes sense all intrinsic functions support all datatypes, with
  some restrictions on <i>bool</i> and <i>char</i>.  Arguments may be scalars or
  vectors. Scalar and vector arguments may be mixed in the same function
  call.  Arguments are automatically type converted upon input as necessary.
  Some functions support a variable number of arguments and the details of
  the the operation to be performed may depend upon how many arguments are
  given.
  </p>
  <p>
  Functions which operate upon vectors are applied to the <i>lines</i> of an
  image.  When applied to an image of dimension two or greater, these
  functions are evaluated separately for every line of the multidimensional
  image.
  </p>
  <p>
  Standard Intrinsic Functions
  </p>
  <div class="highlight-default-notranslate"><pre>
   abs (arg)                       absolute value
   max (arg, 0.0, ...)             maximum value
   min (arg1, arg2, ...)           minimum value
   mod (arg1, arg2)                modulus
  sqrt (arg)                       square root
  </pre></div>
  <p>
  Mathematical or trigonometric functions
  </p>
  <div class="highlight-default-notranslate"><pre>
   acos (arg)                         arc cosine
   asin (arg)                         arc sine
   atan (arg [,arg2])                 arc tangent
  atan2 (arg [,arg2])                 arc tangent
    cos (arg)                         cosine
   cosh (arg)                         hyperbolic cosine
    exp (arg)                         exponential
    log (arg)                         natural logarithm
  log10 (arg)                         logarithm base 10
    sin (arg)                         sine
   sinh (arg)                         hyperbolic sine
    tan (arg)                         tangent
   tanh (arg)                         hyperbolic tangent
  </pre></div>
  <p>
  The trigonometric functions operate in units of radians.  The <i>deg</i> and
  <i>rad</i> intrinsic functions (see below) can be used to convert to and from
  degrees if desired.
  </p>
  <p>
  Type conversion functions
  </p>
  <div class="highlight-default-notranslate"><pre>
    bool (arg)                         coerce to boolean
   short (arg)                         coerce to short
     int (arg)                         truncate to integer
    nint (arg)                         nearest integer
    long (arg)                         coerce to long (same as int)
    real (arg)                         coerce to real
  double (arg)                         coerce to double
     str (arg)                         coerce to string
  </pre></div>
  <p>
  The numeric type conversion functions will convert a string to a number if
  called with a character argument.  The <i>str</i> function will convert any
  number to a string.
  </p>
  <p>
  Projection functions
  </p>
  <div class="highlight-default-notranslate"><pre>
     len (arg)                         length of a vector
     hiv (arg)                         high value of a vector
     lov (arg)                         low value of a vector
    mean (arg [,ksigma])               mean of a vector
  median (arg)                         median of a vector
  stddev (arg [, ksigma])              standard deviation
     sum (arg)                         sum of a vector
  </pre></div>
  <p>
  The projection functions take a vector as input and return a scalar value as
  output.  The functions <i>mean</i> and <i>stddev</i>, used to compute the mean
  and standard deviation of a vector, allow an optional second argument which
  if given causes a K-sigma rejection to be performed.
  </p>
  <p>
  Miscellaneous functions
  </p>
  <div class="highlight-default-notranslate"><pre>
     deg (arg)                         radians to degrees
     rad (arg)                         degrees to radians
  median (arg1, arg2, arg3, ...)       vector median of 3-5 vectors
    repl (arg, n)                      replicate
    sort (arg)                         sort a vector
   shift (arg, npix)                   shift a vector
  </pre></div>
  <p>
  The <i>median</i> function shown here computes the vector median of several
  input vectors, unlike the projection median which computes the median value
  of a vector sample.  <i>sort</i> sorts a vector, returning the sorted vector
  as output (this can be useful for studying the statistics of a sample).
  <i>shift</i> applies an integral pixel shift to a vector, wrapping around at
  the endpoints.  A positive shift shifts data features to the right (higher
  indices).
  </p>
  <p>
  The <i>repl</i> (replicate) function replicates a data element, returning a
  vector of length (n * len(a)) as output.  For example, this can be used to
  create a dummy data array or image by replicating a constant value.
  </p>
  <p>
  <b>The Expression Database</b>
  </p>
  <p>
  The <i>mskexpr</i> expression database provides a macro facility which can be
  used to create custom libraries of functions for specific applications. A
  simple example follows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Sample MSKEXPR expression database file.
  
  # Constants.
  SQRTOF2=        1.4142135623730950488
  PI=             3.1415926535897932385
  
  # Simple bad data functions.
  bdata1          (i &lt; -100 || i &gt; 25000)
  bdata2          (i &lt; -100 || i &gt; 32000)
  
  # New regions functions.
  cmpie(xc,yc,r,t1,t2)    circle (xc, yc, r) &amp;&amp; (! pie (xc, yc, t1, t2))
  </pre></div>
  <p>
  The complete syntax of a macro entry is as follows:
  </p>
  <p>
          &lt;symbol&gt;[<span style="font-family: monospace;">'('</span> arg-list <span style="font-family: monospace;">')'</span>][<span style="font-family: monospace;">':'</span>|<span style="font-family: monospace;">'='</span>]     replacement-text
  </p>
  <p>
  The replacement text may appear on the same line as the macro name or may
  start on the next line, and may extend over multiple input lines if necessary.
  If so, continuation lines must be indented.  The first line with no whitespace
  at the beginning of the line terminates the macro. Macro functions may be
  nested.  Macro functions are indistinguishable from intrinsic functions in
  expressions.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create a 0-valued 512 x 512 mask and set all the pixels inside a circular
  annulus to 1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type expr.dat
  cannulus (256., 256., 20., 40.) ? 1 : 0
  cl&gt; mskexpr @expr.dat mask.pl ""
  </pre></div>
  <p>
  2. Repeat the previous example but set all the pixels outside the circular
  annulus to 1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type expr.dat
  ! cannulus (256., 256., 20., 40.) ? 1 : 0
  cl&gt; mskexpr @expr.dat mask.pl ""
  </pre></div>
  <p>
  3. Create a 0-valued 512 x 512 mask and set all the pixels inside the
  intersection of 2 circles to 1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type expr.dat
  circle (220., 220., 50.) &amp;&amp; circle (240., 220., 50.) ? 1 : 0
  cl&gt; mskexpr @expr.dat mask.pl ""
  </pre></div>
  <p>
  4. Create a 0 valued mask and set all the pixels outside the good
  data range 0 &lt;= pixval &lt;= 10000 in the reference image and outside
  a circle to 1. Note that the i character defines the reference image
  operand.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type expr.dat
  i &lt; 0 || i &gt; 10000 || circle (256., 256., 50.) ? 1 : 0
  cl&gt; mskexpr @expr.dat mask.pl dev$pix
  </pre></div>
  <p>
  5. Create a 0 valued 512 x 512 mask and set all the pixels inside a circle
  excluding a wedge shaped region to 1. The expression cmpie is used defined
  and stored in the expression database <span style="font-family: monospace;">"myexpr.db"</span> 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type myexpr.db
  # Sample MSKEXPR expression database file.
  
  # Constants.
  SQRTOF2=        1.4142135623730950488
  PI=             3.1415926535897932385
  
  # Simple bad data functions.
  bdata1          (i &lt; -100 || i &gt; 25000)
  bdata2          (i &lt; -100 || i &gt; 32000)
  
  # New regions functions.
  cmpie(xc,yc,r,t1,t2)    circle (xc, yc, r) &amp;&amp; (! pie (xc, yc, t1, t2))
  
  cl&gt; type expr.dat
  cmpie (256., 256., 50., 0., 30.) ? 1 : 0
  
  cl&gt; mskexpr @expr.dat mask.pl "" exprdb=myexpr.db
  </pre></div>
  <p>
  6.  A set of dithered images have been transformed to a common world
  coordinate system, stacked, and a mask created for the sources.  To
  create a boolean mask for one of the images from the deep source mask:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set pmmatch="world"
  cl&gt; mskexpr "m" mask1.pl exp1 refmask=stackmask
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imexpr, mskregions, pmmatch
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

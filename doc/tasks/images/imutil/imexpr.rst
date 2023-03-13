.. _imexpr:

imexpr: Evaluate a general image expression
===========================================

**Package: imutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imexpr expr output [a b c ...]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_expr">
  <dt><b>expr</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expr' Line='expr' -->
  <dd>The expression to be evaluated.  This may be the actual expression, or the
  string <span style="font-family: monospace;">"@file"</span> in which case the expression is taken from the named file.
  The input operands (i.e., numeric constants, images, or image header
  parameters) are referred to in the expression symbolically using the letters
  <span style="font-family: monospace;">"a"</span> through <span style="font-family: monospace;">"z"</span>.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output image.  A section may be given to write into a section of an
  existing image.
  </dd>
  </dl>
  <dl id="l_a">
  <dt><b>a - z</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='a' Line='a - z' -->
  <dd>The input operands referenced by the expression.  The value of an operand
  may be an image name or section, a numeric constant, or a reference to an
  image header parameter of the form <i>operand.param</i>, where <i>operand</i>
  is one of the other input operands <span style="font-family: monospace;">"a"</span> through <span style="font-family: monospace;">"z"</span>, corresponding to an input
  image (for example, <span style="font-family: monospace;">"a.itime"</span> is the parameter <span style="font-family: monospace;">"itime"</span> from the image
  assigned to operand <span style="font-family: monospace;">"a"</span>).  An example of an input image operand is
  <span style="font-family: monospace;">"a=dev$pix"</span>.
  </dd>
  </dl>
  <dl id="l_dims">
  <dt><b>dims = <span style="font-family: monospace;">"auto"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dims' Line='dims = "auto"' -->
  <dd>The dimensions of the output image.  If the special value <i>auto</i> is
  given the output image dimensions are computed based on the input operands
  and the expression being evaluated.  Otherwise the value is a list of axis
  lengths, e.g., <span style="font-family: monospace;">"512,512"</span>.
  </dd>
  </dl>
  <dl id="l_intype">
  <dt><b>intype = <span style="font-family: monospace;">"int"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intype' Line='intype = "int"' -->
  <dd>The minimum datatype for an input image operand.  If the special value
  <i>auto</i> is given the operand type will be the same as the pixel type of
  the image.  Otherwise one of the values <span style="font-family: monospace;">"short"</span>, <span style="font-family: monospace;">"int"</span>, <span style="font-family: monospace;">"long"</span>, <span style="font-family: monospace;">"real"</span>,
  or <span style="font-family: monospace;">"double"</span> should be given.  The program will promote the type of the
  input operand to the type specified if the actual type is less precise
  than the value of <i>intype</i>, otherwise the type of the input operand
  is not changed.  For example, if <i>intype</i> is <span style="font-family: monospace;">"int"</span> (the default),
  short integer input operands will be promoted to integer but int, long,
  real or double operands will be unaffected.  Setting <i>intype</i> to real
  will force the expression to be evaluated in floating point.
  </dd>
  </dl>
  <dl id="l_outtype">
  <dt><b>outtype = <span style="font-family: monospace;">"auto"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtype' Line='outtype = "auto"' -->
  <dd>The pixel type of the output image.  If set to the special value <i>auto</i>
  the output image will be the same type as the expression being evaluated.
  If set to <i>ref</i> the output image will have the same type as the
  <span style="font-family: monospace;">"reference"</span> input image (see below), regardless of the expression type.
  If an explicit type is specified such as <span style="font-family: monospace;">"short"</span>, <span style="font-family: monospace;">"ushort"</span>, <span style="font-family: monospace;">"int"</span>, <span style="font-family: monospace;">"real"</span>,
  an image of the indicated type will be created.
  </dd>
  </dl>
  <dl id="l_refim">
  <dt><b>refim = <span style="font-family: monospace;">"auto"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refim' Line='refim = "auto"' -->
  <dd>The reference image to be used to pass the WCS and other image header
  attributes to the output image.  If set to <i>auto</i> the program will
  compute the best reference image, which is the first input image
  with the highest number of dimensions.  To force a particular input image
  to be the reference image the value should be set to the name of an input
  operand (<span style="font-family: monospace;">"a"</span>, <span style="font-family: monospace;">"b"</span>, etc.).  The named operand must refer to an image.
  </dd>
  </dl>
  <dl id="l_bwidth">
  <dt><b>bwidth = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bwidth' Line='bwidth = 0' -->
  <dd>The boundary width in pixels for boundary extension.  Boundary extension
  is enabled by setting this value to a positive nonzero value.  Boundary
  extension is needed when an input image section references out of bounds.
  </dd>
  </dl>
  <dl id="l_btype">
  <dt><b>btype = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='btype' Line='btype = "nearest"' -->
  <dd>The type of boundary extension, chosen from the list <span style="font-family: monospace;">"constant"</span>, <span style="font-family: monospace;">"nearest"</span>,
  <span style="font-family: monospace;">"reflect"</span>, <span style="font-family: monospace;">"wrap"</span>, or <span style="font-family: monospace;">"project"</span>.
  </dd>
  </dl>
  <dl id="l_bpixval">
  <dt><b>bpixval = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bpixval' Line='bpixval = 0.' -->
  <dd>The boundary pixel value if <i>btype</i>=<span style="font-family: monospace;">"constant"</span>.
  </dd>
  </dl>
  <dl id="l_rangecheck">
  <dt><b>rangecheck = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rangecheck' Line='rangecheck = yes' -->
  <dd>If range checking is enabled then the program will check for illegal
  operations such as divide by zero or the square root or logarithm of a
  negative value, substituting a constant value (zero) if such an operation
  is detected.  This may be necessary to avoid aborting the entire operation
  because of a few bad pixels in an image.  A conditional expression may be
  used to detect such pixels and perform any special processing.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Enable or disable informative messages.  If enabled, the program will echo
  the expression to be evaluated after all expansions have been performed,
  and percent-done messages will be printed as the expression is evaluated.
  </dd>
  </dl>
  <dl id="l_exprdb">
  <dt><b>exprdb = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exprdb' Line='exprdb = ""' -->
  <dd>The file name of an optional expression database.  An expression database
  may be used to define symbolic constants or a library of custom function
  macros.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>imexpr</i> evaluates an image expression and writes the result to the
  output image.  Images may be any dimension or size and any datatype except
  complex (complex images may be read but only the real part will be used).
  </p>
  <p>
  If the input images are not all the same size the computation will be
  performed over the largest area which is common to all images.  If the
  images are not all the same dimension the lesser dimension operands will be
  iteratively combined with the higher dimension ones.  For example, when
  both a one and two dimensional image are used in the same expression,
  the vector (one dimensional image) will be applied to all lines of the
  two dimensional image.
  </p>
  <p>
  Evaluation of the image expression is carried out one line at a time.  This
  is efficient and permits operations on arbitrarily large images without
  using excessive memory, but does not allow 2D or higher operations to be
  performed within the expression (e.g., transpose).  The entire expression is
  evaluated once for each line of the output image.
  </p>
  <p>
  <b>Operands</b>
  </p>
  <p>
  Input operands are represented symbolically in the input expression using
  the symbols <span style="font-family: monospace;">"a"</span> through <span style="font-family: monospace;">"z"</span>, corresponding to <i>imexpr</i> task parameters.
  Use of symbolic operands allows the same expression to be used with different
  data sets, simplifies the expression syntax, and allows a single input image
  to be used several places in the same expression.
  </p>
  <p>
  Three classes of input operands are recognized: images, image parameters, and
  numeric constants.
  </p>
  <div class="highlight-default-notranslate"><pre>
  dev$pix[*,55]           image operand
  a.itime                 image parameter
  1.2345                  numeric constant
  </pre></div>
  <p>
  Since the input operands are CL parameters they may be set on the command
  line, or entered in response to parameter prompts when the task executes and
  evaluates the input expression.  For example,
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imexpr "a - a/b" pix
  operand a: dev$pix[*,55]
  operand b: a.itime
  </pre></div>
  <p>
  would evaluate the expression shown, storing the result in the output image
  <span style="font-family: monospace;">"pix"</span>.
  </p>
  <p>
  Operands may also be specified directly in the expression, with the
  exception of image operands.  For example,
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imexpr "a - a / a.itime"
  </pre></div>
  <p>
  is equivalent to the earlier example.
  </p>
  <p>
  If the input operand is not a simple identifier (a simple name like <span style="font-family: monospace;">"itime"</span>
  containing only alphanumeric characters, underscore, <span style="font-family: monospace;">"."</span>, or <span style="font-family: monospace;">"$"</span>) then it
  is necessary to quote the operand name and precede it with an <span style="font-family: monospace;">"@"</span>, e.g.,
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imexpr 'a - a / @"a.i-time"'
  </pre></div>
  <p>
  Finally, there is a special builtin type of operand used to represent the
  image pixel coordinates in an image expression.  These operands have the
  special reserved names <span style="font-family: monospace;">"I"</span>, <span style="font-family: monospace;">"J"</span>, <span style="font-family: monospace;">"K"</span>, etc., up to the dimensions of the
  output image.  The names must be upper case to avoid confusion to with the
  input operands <span style="font-family: monospace;">"i"</span>, <span style="font-family: monospace;">"j"</span>, <span style="font-family: monospace;">"k"</span> and so on.
  </p>
  <div class="highlight-default-notranslate"><pre>
  I                       X coordinate of pixel (column)
  J                       Y coordinate of pixel (line)
  K                       Z coordinate of pixel (band)
  </pre></div>
  <p>
  An example of the use of the pixel coordinate operands is the generation of
  multidimensional analytic functions.
  </p>
  <p>
  <b>Operators</b>
  </p>
  <p>
  The expression syntax implemented by <i>imexpr</i> provides the following
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
  ~                       bitwise not (complement)
  </pre></div>
  <p>
  The conditional expression has the value <i>expr1</i> if <i>expr</i> is true,
  and <i>expr2</i> otherwise.  Since the expression is evaluated at every pixel
  this permits pixel-dependent operations such as checking for special pixel
  values, or selection of elements from either of two vectors.  For example,
  the command
  </p>
  <p>
  	(a &lt; 0) ? 555 : b / a
  </p>
  <p>
  has the constant value 555 if <span style="font-family: monospace;">"a"</span> is less than zero, and <span style="font-family: monospace;">"b / a"</span> otherwise.
  Conditional expressions are general expressions and may be nested or used
  anywhere an expression is permitted.
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
  <b>Functions</b>
  </p>
  <p>
  Where it makes sense all intrinsic functions support all datatypes, with
  some restrictions on <i>bool</i> and <i>char</i>.  Arguments may be scalars or
  vectors and scalar and vector arguments may be mixed in the same function
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
   abs (a)                         absolute value
   max (a, b, ...)                 maximum value
   min (a, b, ...)                 minimum value
   mod (a, b)                      modulus
  sqrt (a)                         square root
  </pre></div>
  <p>
  Mathematical or trigonometric functions
  </p>
  <div class="highlight-default-notranslate"><pre>
   acos (a)                         arc cosine
   asin (a)                         arc sine
   atan (a [,b])                    arc tangent
  atan2 (a [,b])                    arc tangent
    cos (a)                         cosine
   cosh (a)                         hyperbolic cosine
    exp (a)                         exponential
    log (a)                         natural logarithm
  log10 (a)                         logarithm base 10
    sin (a)                         sine
   sinh (a)                         hyperbolic sine
    tan (a)                         tangent
   tanh (a)                         hyperbolic tangent
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
    bool (a)                         coerce to boolean
   short (a)                         coerce to short
     int (a)                         truncate to integer
    nint (a)                         nearest integer
    long (a)                         coerce to long (same as int)
    real (a)                         coerce to real
  double (a)                         coerce to double
     str (a)                         coerce to string
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
     len (a)                         length of a vector
     hiv (a)                         high value of a vector
     lov (a)                         low value of a vector
    mean (a [, ksigma])              mean of a vector
  median (a)                         median of a vector
  stddev (a [, ksigma])              standard deviation
     sum (a)                         sum of a vector
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
     deg (a)                         radians to degrees
     rad (a)                         degrees to radians
  median (a, b, c [, d [, e]])       vector median of 3-5 vectors
    repl (a, n)                      replicate
    sort (a)                         sort a vector
   shift (a, npix)                   shift a vector
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
  The <i>imexpr</i> expression database provides a macro facility which can be
  used to create custom libraries of functions for specific applications. A
  simple example follows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Sample IMEXPR expression database file.
  
  # Constants.
  SQRTOF2=        1.4142135623730950488
  BASE_E=         2.7182818284590452353
  PI=             3.1415926535897932385
  GAMMA=          .57721566490153286061   # Euler's constant
  
  # Functions.
  div10(a)        ((a) / 10)
  divz(a,b)       ((abs(b) &lt; .000001) ? 0 : a / b)
  
  div(a,b)        (div10(b) / a)
  sinx            (cos(I / 30.0))
  sinxy(a,b)      (cos (I / a) + cos (J / b))
  </pre></div>
  <p>
  The complete syntax of a macro entry is as follows:
  </p>
  <p>
  	&lt;symbol&gt;[<span style="font-family: monospace;">'('</span> arg-list <span style="font-family: monospace;">')'</span>][<span style="font-family: monospace;">':'</span>|<span style="font-family: monospace;">'='</span>]     replacement-text
  </p>
  <p>
  The replacement text may appear on the same line as the macro name or may
  start on the next line, and may extend over multiple input lines if
  necessary.  If so, continuation lines must be indented.  The first line
  with no whitespace at the beginning of the line terminates the macro.
  Macro functions may be nested.  Macro functions are indistinguishable from
  intrinsic functions in expressions.
  </p>
  <p>
  <b>IMEXPR and Pixel Masks</b>
  </p>
  <p>
  Although <i>imexpr</i> has no special support for pixel masks, it was
  designed to work with masks and it is important to realize how these can be
  used.  IRAF image i/o includes support for a special type of image, the
  pixel mask or <span style="font-family: monospace;">".pl"</span> type image.  Pixel masks are used for things such as
  region identification in images - any arbitrary region of an image can be
  assigned a constant value in a mask to mark the region.  Masks can then be
  used during image analysis to identify the subset of image pixels to be
  used.  An image mask stored as a <span style="font-family: monospace;">".pl"</span> file is stored in compressed form and
  is typically only a few kilobytes in size.
  </p>
  <p>
  There are many ways to create masks, but in some cases <i>imexpr</i> itself
  can be used for this purpose.  For example, to create a boolean mask with
  <i>imexpr</i> merely evaluate a boolean expression and specify a <span style="font-family: monospace;">".pl"</span> file
  as the output image.  For example,
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imexpr "a &gt; 800" mask.pl
  </pre></div>
  <p>
  will create a boolean mask <span style="font-family: monospace;">"mask.pl"</span> which identifies all the pixels in an
  image with a value greater than 800.
  </p>
  <p>
  An example of the use of masks is the problem of combining portions of two
  images to form a new image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imexpr "c ? a : b"  c=mask.pl
  </pre></div>
  <p>
  This example will select pixels from either image A or B to form the output
  image, using the mask assigned to operand C to control the selection.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Copy an image, changing the datatype to real (there are better ways to
  do this of course).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imexpr a pix2 a=pix outtype=real
  </pre></div>
  <p>
  2. Create a new, empty image with all the pixels set to 0.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imexpr "repl(0,512)" pix dim=512,512
  </pre></div>
  <p>
  3. Create a 1D image containing the sinc function.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imexpr "I == 10 ? 1.0 : sin(I-10.0)/(I-10)" sinc dim=20
  </pre></div>
  <p>
  4. Create a new image containing a simple test pattern consisting of a 5
  element vector repeated 100 times across each image line.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imexpr "repl((9 // 3 // 3 // 11 // 11), 100)" patt dim=500,500
  </pre></div>
  <p>
  5. Subtract the median value from each line of an image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imexpr "a - median(a)" medimage
  </pre></div>
  <p>
  6. Compute the HIV (low value) projection of an image.  The result is a
  transposed 1D image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imexpr "hiv(a)" hvector
  </pre></div>
  <p>
  7. Swap the left and right halves of an image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imexpr "a // b" pix swapimage
  operand a: dev$pix[256:512,*]
  operand b: dev$pix[1:255,*]
  </pre></div>
  <p>
  8. Create a circular mask of a given radius about a user-defined center.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type expr
  (sqrt((I-b)**2 + (J-c)**2) &lt;= d)
  cl&gt; imexpr @expr mask.pl b=256 c=256 d=100 dims=512,512
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The input and output images cannot be the same.
  No support for type complex yet, or operations like the fourier transform.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imarith, imfunction, imcombine
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

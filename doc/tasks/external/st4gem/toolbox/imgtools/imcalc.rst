.. _imcalc:

imcalc: Perform general arithmetic operations on images.
========================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imcalc input output equals
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Arithmetic operations are performed on one or more images,
  and an output image is generated.
  Operations are performed on all groups
  unless a group specifier is explicitly part of the image name.
  All input images must be of the same size, number of dimensions,
  and number of groups.
  The expression contains constants, variable names, or both.
  Constants can be integers or floating point values
  (exponential notation is allowed).
  There are two kinds of variables:  the first type represents
  the first through eighth image and is named 'im1' through 'im8',
  the second type represents the index of the corresponding dimension,
  and is named <span style="font-family: monospace;">'x'</span>, <span style="font-family: monospace;">'y'</span>, or <span style="font-family: monospace;">'z'</span>.
  For example at pixel [12,100,2] in an image, 'x=12', 'y=100', and 'z=2'.
  The expression is evaluated according to the data types of the variables
  and constants in the expression and then converted to the type of the
  output image.
  </p>
  <p>
  The following Fortran-type arithmetic operators are supported.
  If the second argument of the exponentiation is not an integer, the result
  will be undefined if the first argument is not positive.
  Remember that integer division truncates.
  </p>
  <div class="highlight-default-notranslate"><pre>
  +       addition                -       subtraction
  *       multiplication          /       division
  -       negation                **      exponentiation
  </pre></div>
  <p>
  The following logical operators are supported.
  Logical operators will return a value of 1 if true or 0 if false.
  Logical operators are supported in both their Fortran and SPP form.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Fortran  SPP        Operation
  ------------------------------------------
  </dd>
  </dl>
  </pre></div>
  The following functions are supported.
  These functions all take a single argument,
  which may be an expression.
  The argument or result of trigonometric functions are in radians.
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
  The following functions take two arguments.
  <div class="highlight-default-notranslate"><pre>
  atan2   arc tangent             dim     positive difference
  max     maximum                 min     minimum
  mod     modulus                 sign    sign transfer
  </pre></div>
  Conditional expressions of the form <span style="font-family: monospace;">"if expr then expr else expr"</span> are
  supported.
  The expression after the <span style="font-family: monospace;">"else"</span> may be another conditional expression.
  The words <span style="font-family: monospace;">"if"</span>, <span style="font-family: monospace;">"then"</span>, and <span style="font-family: monospace;">"else"</span> must be surrounded by blanks.
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='input' Line='input [file name template]' -->
  <dd><p>
  The image names that are to be used in the arithmetic expression.
  These image names will be substituted for the corresponding strings
  <span style="font-family: monospace;">"im1"</span>, etc., in the expression in the order that they occur in this
  parameter.
  All images (or sections) must be the same size,
  have the same number of dimensions, and number of groups.
  </dd>
  </dl>
  </p>
  <dl id="l_output">
  <dt><b>output  [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='output' Line='output  [file name]' -->
  <dd><p>
  Name of the output image file created by this task.
  The header and data type of 'output' will be that of
  the first image in 'input'.
  </dd>
  </dl>
  </p>
  <dl id="l_equals">
  <dt><b>equals [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='equals' Line='equals [string]' -->
  <dd><p>
  The arithmetic expression to evaluate.
  If the expression is too long to pass as a parameter,
  place the expression in a file and set the value of this parameter to
  the file name preceded by an <span style="font-family: monospace;">"@"</span> character; for example, <span style="font-family: monospace;">"@filename"</span>.
  </dd>
  </dl>
  </p>
  <dl>
  <dt><b>(pixtype = <span style="font-family: monospace;">"old"</span>) [string, allowed values: old | short | ushort | int |</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='' Line='(pixtype = "old") [string, allowed values: old | short | ushort | int |' -->
  <dd><p>
  real | double ]
  </p>
  <p>
  The pixel type of the output image.
  If the type is set to <span style="font-family: monospace;">"old"</span>,
  the output image will have the same type as the first input image.
  </dd>
  </dl>
  </p>
  <dl>
  <dt><b>(nullval = 0.0) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='' Line='(nullval = 0.0) [real]' -->
  <dd><p>
  Whenever a calculation contains an illegal operation,
  this value is substituted for the result of the calculation.
  Examples of illegal operations are division by zero and
  taking the square root of a negative number.
  </dd>
  </dl>
  </p>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='' Line='(verbose = yes) [boolean]' -->
  <dd><p>
  Print a message showing the percent of the calculations done?
  </dd>
  </dl>
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  1. Create a new image in which each pixel is equal to 10.0**(-x/2.5),
  where <span style="font-family: monospace;">"x"</span> represents the corresponding pixel value in the image file
  someimage.hhh.
  This is related to the conversion of stellar magnitude to flux.
  <div class="highlight-default-notranslate"><pre>
  im&gt; imcalc someimage.hhh outim.hhh "10.0**(-im1/2.5)"
  </pre></div>
  2. Replace all values above 200 with the value 200, and all values below
  100 with 100.
  <div class="highlight-default-notranslate"><pre>
  im&gt; imcalc image.fits outim.fits "min(200,max(im1,100))"
  </pre></div>
  3. Take the average of three images:
  <div class="highlight-default-notranslate"><pre>
  im&gt; imcalc image1,image2,image3 out.fits "(im1+im2+im3)/3."
  </pre></div>
  4. Divide in1.fits by in2.fits,
  except that we want the result to be the value from in1.fits
  for any pixel where in2.fits is less than or equal to zero.
  Note that the following will not work as expected:
  <div class="highlight-default-notranslate"><pre>
  im&gt; imcalc in1.fits,in2.fits out.fits \
       "if im2 .gt. 0. then im1/im2 else im1"
  </pre></div>
  The result will be the value from in1.fits where in2.fits is negative,
  as intended, but it will be 'nullval' where in2.fits is zero.
  The division by zero takes precedence, in some sense, over the conditional.
  This can be handled by a two-step process,
  where a temporary image is created that is a copy of in2.fits
  except that it is -1 where in2.fits is zero.
  <div class="highlight-default-notranslate"><pre>
  im&gt; imcalc in2.fits temp.fits "if im1 .eq. 0. then -1. else im1"
  im&gt; imcalc in1.fits,temp.fits out.fits \
       "if im2 .gt. 0. then im1/im2 else im1"
  </pre></div>
  5. Set the 4 border pixels in a 512 by 512 image to zero.
  The expression is stored in the file 'exp.dat':
  <div class="highlight-default-notranslate"><pre>
  im&gt; imcalc image.fits out.fits @exp.dat
  </pre></div>
  The contents of 'exp.dat' are:
  <div class="highlight-default-notranslate"><pre>
  if x .gt. 4 .and. x .lt. 509 .and. y .gt. 4 .and. y .lt. 509
  then im1 else 0.0
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  When an expression involves an invalid operation,
  such as divide by zero,
  the result is likely to be 'nullval' regardless of
  conditional expressions that check for the invalid operation.
  See the examples section for a specific example.
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  tcalc
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

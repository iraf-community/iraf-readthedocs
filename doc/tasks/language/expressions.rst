.. _expressions:

expressions: Standard expression syntax in IRAF tasks
=====================================================

**Package: language**

.. raw:: html

  <section id="s_introduction">
  <h3>Introduction</h3>
  <p>
  Many
  <a href="#s_see_also">IRAF tasks</A>
  use expressions.  These all go through the same basic expression evaluator.
  This provides a standard set of operators and functions with a 
  common syntax similar to the CL.  However, each application can customize
  </p>
  <dl>
  <dt><b>*</b></dt>
  <!-- Sec='Introduction' Level=0 Label='' Line='*' -->
  <dd>how expressions are input; e.g. from files or with special prefixes
  </dd>
  </dl>
  <dl>
  <dt><b>*</b></dt>
  <!-- Sec='Introduction' Level=0 Label='' Line='*' -->
  <dd>how variables (called operands) are specified; e.g. with leading
  special characters such as <span style="font-family: monospace;">'$'</span> or with single letter capitals
  </dd>
  </dl>
  <dl>
  <dt><b>*</b></dt>
  <!-- Sec='Introduction' Level=0 Label='' Line='*' -->
  <dd>where the values are obtained; e.g. from image header keywords or
  from data files
  </dd>
  </dl>
  <dl>
  <dt><b>*</b></dt>
  <!-- Sec='Introduction' Level=0 Label='' Line='*' -->
  <dd>special, application specific functions; e.g. airmass or arcsep
  </dd>
  </dl>
  <p>
  This help topic covers the common features of expressions.  The
  individual task help descriptions may also include this material or
  just describe the customization.
  </p>
  </section>
  <section id="s_expressions">
  <h3>Expressions</h3>
  <p>
  Expressions consist of operands, numeric and string constants, operators,
  and functions.  Parentheses are also used to control the evaluation order
  as in standard algebraic expressions.  String constants are quoted strings
  and numeric constants are pure unquoted numbers.  Numbers may be given in
  sexagesimal notation and are automatically converted to decimal numbers.
  The operators are arithmetic, logical, and string.
  </p>
  </section>
  <section id="s_operands">
  <h3>Operands</h3>
  <p>
  The way applications refer to operands is generally unique to that task.
  Sometimes they are simply alphanumeric identifiers, sometimes they
  have prefixes such <span style="font-family: monospace;">'$'</span>, sometimes they are limited to specific
  identifiers, and sometimes they have additional structure such as
  &lt;image&gt;.&lt;keyword&gt; where &lt;image&gt; is an identifier for an image
  and &lt;keyword&gt; refers to a keyword in the image.  Common types of
  operands refer to images, table columns, and keywords.
  </p>
  <p>
  There is one special common syntax for operands that include characters that
  correspond to the operators in expressions.  In this case the operand
  identifier must be quoted as a string and then referenced using a leading @
  character; e.g.  @'mjd-obs'.
  </p>
  </section>
  <section id="s_operators">
  <h3>Operators</h3>
  <p>
  The following operators are recognized in expressions.  With the exception
  of the operators <span style="font-family: monospace;">"?"</span>, <span style="font-family: monospace;">"?="</span>, and <span style="font-family: monospace;">"@"</span>, the operator set is equivalent to that
  available in the CL.
  </p>
  <div class="highlight-default-notranslate"><pre>
  +  -  *  /              arithmetic operators
  **                      exponentiation
  //                      string concatenation
  !  -                    boolean not, unary negation
  &lt;  &lt;= &gt;  &gt;=             order comparison (works for strings)
  == != &amp;&amp; ||             equals, not equals, and, or
  ?=                      string equals pattern
  ? :                     conditional expression (ternary operator)
  @                       reference a operand
  </pre></div>
  <p>
  The operators <span style="font-family: monospace;">"=="</span>, <span style="font-family: monospace;">"&amp;&amp;"</span>, and <span style="font-family: monospace;">"||"</span> may be abbreviated as <span style="font-family: monospace;">"="</span>, <span style="font-family: monospace;">"&amp;"</span>, and <span style="font-family: monospace;">"|"</span>
  if desired.  The ?= operator performs pattern matching upon strings.
  The pattern syntax is that described for the task
  <a href="match"><b>match</b>.</A>
  The @ operator is required to reference keywords with
  one of the operator characters.  This is most likely to be used as:
  </p>
  <div class="highlight-default-notranslate"><pre>
  @"date-obs"
  </pre></div>
  <p>
  A point to be aware of is that in the ?: conditional expression both
  possible result values are evaluated though the result of the expression
  is only one of them.
  </p>
  </section>
  <section id="s_functions">
  <h3>Functions</h3>
  <p>
  A number of standard intrinsic functions are recognized within
  expressions.  Many of these may not be useful in the context of the
  application but are part of the language.  The set of
  functions currently supported is shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  abs     atan2   deg     log     min     real    sqrt
  acos    bool    double  log10   mod     short   str
  asin    cos     exp     long    nint    sin     tan
  atan    cosh    int     max     rad     sinh    tanh
  </pre></div>
  <p>
  The trigonometric functions operate in units of radians.
  The <i>min</i> and <i>max</i> functions may have any number of arguments up
  to a maximum of sixteen or so (configurable).  The arguments need not all
  be of the same datatype.
  </p>
  <p>
  A function call may take either of the following forms:
  </p>
  <div class="highlight-default-notranslate"><pre>
  &lt;identifier&gt; <span style="font-family: monospace;">'('</span> arglist <span style="font-family: monospace;">')'</span>
  &lt;string_expr&gt; <span style="font-family: monospace;">'('</span> arglist <span style="font-family: monospace;">')'</span>
  </pre></div>
  <p>
  The first form is the conventional form found in all programming languages.
  The second permits the generation of function names by string valued
  expressions and might be useful on rare occasions.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <a href="imexpr"><b>imexpr</b></A>
  <a href="hedit"><b>hedit</b></A>
  <a href="hselect"><b>hselect</b></A>
  <a href="asthedit"><b>asthedit</b></A>
  <a href="astcalc"><b>astcalc</b></A>
  <a href="irproc"><b>irproc</b></A>
  <a href="ircatalog"><b>ircatalog</b></A>
  <a href="ccget"><b>ccget</b></A>
  <a href="mskexpr"><b>mskexpr</b></A>
  <a href="mskreg"><b>mskreg</b></A>
  <a href="import"><b>import</b></A>
  <a href="export"><b>export</b></A>
  <a href="agetcat"><b>agetcat</b></A>
  <a href="pcalc"><b>pcalc</b></A>
  <a href="pconvert"><b>pconvert</b></A>
  <a href="pdump"><b>pdump</b></A>
  <a href="pselect"><b>pselect</b></A>
  <a href="tbcalc"><b>tbcalc</b></A>
  <a href="tbdump"><b>tbdump</b></A>
  <a href="tbselect"><b>tbselect</b></A>
  <a href="txcalc"><b>txcalc</b></A>
  <a href="txdump"><b>txdump</b></A>
  <a href="txselect"><b>txselect</b></A>
  
  </section>
  
  <!-- Contents: 'Introduction' 'Expressions' 'Operands' 'Operators' 'Functions' 'SEE ALSO'  -->
  

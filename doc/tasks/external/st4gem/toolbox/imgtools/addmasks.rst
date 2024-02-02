.. _addmasks:

addmasks: Combine several masks or bad pixel lists.
===================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  addmasks input output expr
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This tasks combines two or more masks into an output mask. 
  </p>
  <p>
  A mask is an image or table that contains information about another
  image.  Each pixel in a mask contains information about the
  corresponding pixel in the image. If the value of the mask pixel is
  zero, no information is recorded about the corresponding image pixel,
  that is, the image pixel is nothing special. If the mask pixel is
  non-zero, this means some information is being recorded. Each of the
  individual non-zero pixel values is called a <span style="font-family: monospace;">"flag"</span>. Flag values
  should be positive for this task to function correctly. The meaning of
  these flag values are instrument- and application-specific.  Different
  kinds of information are stored as different flags in the mask. If a
  mask pixel has several kinds of information associated with it, the
  corresponding flag values are added and their sum is stored in the
  mask pixel.
  </p>
  <p>
  To <span style="font-family: monospace;">"combine masks"</span> means that you are combining the corresponding
  pixels in the masks into a single pixel in the output mask. Pixels are
  combined according to the expression. The variables in the expression
  start with the letters <span style="font-family: monospace;">"im"</span> followed by a number. The number is the
  order of the mask in the input list. For example, im1 refers to the
  first mask in the input list and im3 to the third mask. The expression
  may also contain integer constants, which are treated as if they are
  masks whose pixels are all equal to the constant.  This task supports
  three operators on pixels:
  </p>
  <div class="highlight-default-notranslate"><pre>
  and     &amp;&amp;      im1 &amp;&amp; im2      set flag if both input flags set
  or      ||      im1 || im2      set flag if either input flag set
  not     !       ! im1           set flag if input flag unset
  </pre></div>
  <p>
  Operators can either be used by their name or in their symbolic form.
  If the name of an operator is used in an expression, the name can
  optionally be surrounded by dots, as in Fortran. The expressions
  <span style="font-family: monospace;">"im1 || im2"</span>, im1 or im2<span style="font-family: monospace;">", and "</span>im1 .or. im2<span style="font-family: monospace;">" are all equivalent. The
  expression may contain more than one operator and operators may be
  grouped by parentheses. In addition to the above operators for
  combining pixels, this task supports the usual relational operators.
  The relational operators return values of "</span>true<span style="font-family: monospace;">" or "</span>false<span style="font-family: monospace;">". A "</span>true<span style="font-family: monospace;">"
  pixel has every flag set and a "</span>false<span style="font-family: monospace;">" pixel has every flag unset. The
  value of a "</span>false<span style="font-family: monospace;">" pixel is always zero, but the value of a "</span>true<span style="font-family: monospace;">"
  pixel depends upon which flags are defined. The following is a list of
  the relational operators.
  </p>
  <div class="highlight-default-notranslate"><pre>
  eq      ==      im1 == im2      true if all flags are the same
  ne      !=      im1 != im2      true if one or more flags different
  gt      &gt;       im1 &gt;  im2      true if im1 has higher precedence
  lt      &lt;       im1 &lt;  im2      true if im1 has lower precedence
  ge      &gt;=      im1 &gt;= im2      true if im1 has higher or same prec.
  le      &lt;=      im1 &lt;= im2      true if im1 has lower or same prec.
  </pre></div>
  <p>
  As with the other operators, relational operators can be used either
  by name or in their symbolic form and if used by name, the name may be
  surrounded by dots. Comparison between pixels is done by the
  precedence order of the flags and not by their numeric values. Each
  flag has a precedence, defined by its position in the list of flag
  values. Values earlier in the list have lower precedence than values
  later in the list. The flags for the existing HST instruments are
  defined so that flags with higher precedence also have higher numeric
  values, so the distinction between numeric value and precedence is
  academic for the HST. But if the flags are defined so that precedence
  does not agree with numeric value, this task will compare according to
  precedence. 
  </p>
  <p>
  Each operator has an associated precedence so that unparenthesized 
  expressions can be evaluated unambiguously. The precedence levels used
  in this task are the same as those in Fortran. The precedence level of
  operators is given in the following table, with "</span>or<span style="font-family: monospace;">" having the lowest
  precedence. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  or              ||
  and             &amp;&amp;
  not             !
  eq ne           == !=
  lt gt le ge     &lt; &gt; &lt;= &gt;=
  </pre></div>
  <p>
  This task also supports conditional expressions. Conditional
  expressions take one of the two following forms:
  </p>
  <div class="highlight-default-notranslate"><pre>
  if exp1 then exp2
  if exp1 then exp2 else exp3
  </pre></div>
  <p>
  The terms exp1, exp2 and exp3 stand for arbitrary non-conditional
  expressions, which are combinations of variables, constants and
  operators. If the first expression (exp1) is not false, that is,
  non-zero, the result will be the value of the second expression. If
  the first expression is false (zero), the result will be the value of
  the third expression if there is an else clause and zero if there is
  not.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name template]' -->
  <dd>The list of input mask file names. Wild card characters may be used,
  or the file names may be placed in a file and the name of the file
  preceded by a <span style="font-family: monospace;">'@'</span> character may be given as this parameter. It is an
  error to give a zero length list. The dimensions of all input masks
  must match.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name]' -->
  <dd>The output mask file name. If the file name has no extension, the
  default image extension will be used. The output file name cannot be
  the same as one of the input file names. (In place modification of
  mask files is not allowed.)
  </dd>
  </dl>
  <dl id="l_expr">
  <dt><b>expr [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expr' Line='expr [string]' -->
  <dd>The expression used for combining the masks. If the expression is too
  long to pass as a parameter, place the expression in a file and set
  the value of this parameter to the file name preceded by the <span style="font-family: monospace;">'@'</span>
  character. If the expression is placed in a file, the expression may
  be broken across lines wherever a blank can appear in an expression.
  The file may also contain comments preceded by a <span style="font-family: monospace;">'#'</span> character.
  </dd>
  </dl>
  <dl>
  <dt><b>(flags = "</span> <span style="font-family: monospace;">") [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(flags = " ") [string]' -->
  <dd>The list of flag values. If the list of flags is empty, the task
  assumes that the flags are bit flags; that is, the flag values are the
  powers of two starting with 1, 2, 4, 8, etc. It is not necessary to
  set this parameter for the stis, nicmos, wfpc2, or wfpc, as they all
  use bit flags.
  The flag values are separated by commas or white space, or the values
  may be placed in a file and the file name preceded by a <span style="font-family: monospace;">'@'</span> given as
  the argument (i.e., list files are supported). If values are placed in
  a file, the file may contain comments, which are preceded by a <span style="font-family: monospace;">'#'</span>
  character. If the precedence method is used to combine input masks,
  the first flag has the lowest precedence and the last flag the highest
  precedence. The files fos.dat, hrs.dat, and wfpc.dat in the
  imgtools$data/ directory contain the flags definitions for the
  corresponding HST instruments.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following examples compine two wfpc data quality files according
  to various expressions. The first example combines the two files using
  an "</span>or<span style="font-family: monospace;">". The task parameters are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  addmasks.input =  w05u0e01t.q0h,w05u0e02t.q0h
  addmasks.output =  w05out.q0h
  addmasks.expr = im1.or.im2
  addmasks.flags = 1,2,4,8,16,32
  </pre></div>
  <p>
  The value of the flags parameter is specific to the wfpc. The
  corresponding flag values for the wfpc2 go up to 1024.
  </p>
  <p>
  Following examples only change the value of the expression. To set the
  output data quality file to the greater of the two input mask values,
  use the following expression.
  </p>
  <p>
  if im1 &gt; im2 then im1 else im2
  </p>
  <p>
  To set the output data quality file to 32 whenever the input files are
  non-zero, use the following expression.
  </p>
  <p>
  if im1 || im2 then 32
  </p>
  <p>
  No explicit comparison to zero is needed, because the first expression
  is true whenever it is non-zero. The output data quality file is set
  to zero whwenever both input files are zero, because there is no else
  clause in the expression.
  </p>
  <p>
  To combine the two data quality files but ignore type 1 flags, use the
  following expression.
  </p>
  <p>
  (im1 or im2) and not 1
  </p>
  <p>
  The expression "</span>not 1<span style="font-family: monospace;">" creates a mask which has all flags set except
  the 1 flag. Combining this mask with the two input files using an
  "</span>and<span style="font-family: monospace;">" has the effect of turning off the 1 flag wherever it would
  otherwise occur in the output data quality file.
  </p>
  <p>
  The last example combines three masks using an "</span>and<span style="font-family: monospace;">". This task will
  allow you to combine as many masks as you want. The task
  parameters are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  addmasks.input =  w05u0e01t.q0h,w05u0e02t.q0h,w05u0e03t.q0h
  addmasks.output =  w05out.q0h
  addmasks.expr = im1 &amp;&amp; im2 &amp;&amp; im3
  addmasks.flags = 1,2,4,8,16,32
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by Bernie Simon
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcalc
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

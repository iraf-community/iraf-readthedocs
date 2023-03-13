.. _lroff:

lroff: Lroff (line-roff) text formatter
=======================================

**Package: softools**

.. raw:: html

  <section id="s_purpose">
  <h3>Purpose</h3>
  <p>
  <b>Lroff</b> is a simple text formatter used by the IRAF on-line Help command,
  and other utilities (MANPAGE, LIST), to format text.  
  <b>Lroff</b> style documentation text may be embedded in program source files.
  <b>lroff</b> is line oriented, rather than page oriented,
  and is implemented as a library procedure rather than as a task.
  </p>
  </section>
  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  status = lroff (input, output, left_margin, right_margin)
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>An integer procedure, called by <b>lroff</b> to get lines of input,
  which takes the <b>lroff</b> input buffer as an argument,
  and which returns EOF upon End of File (like GETLINE).
  Each line of input must be terminated by a newline and an EOS
  (End Of String marker).
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>A procedure, called by <b>lroff</b> to output formatted lines of text,
  which takes the <b>lroff</b> output buffer as an argument (<span style="font-family: monospace;">"output (buffer)"</span>).
  </dd>
  </dl>
  <dl id="l_left_margin">
  <dt><b>left_margin</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='left_margin' Line='left_margin' -->
  <dd>The first column to be filled (&gt;= 1).
  </dd>
  </dl>
  <dl id="l_right_margin">
  <dt><b>right_margin</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='right_margin' Line='right_margin' -->
  <dd>The last column to be filled.
  </dd>
  </dl>
  <dl id="l_status">
  <dt><b>status</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='status' Line='status' -->
  <dd>ERR is returned if meaningless margins are specified, or if an unrecoverable
  error occurs during processing.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Lroff</b> input may be bracketed by <span style="font-family: monospace;">".help"</span> and <span style="font-family: monospace;">".endhelp"</span> directives in
  the actual source file of the program being documented (if intended as input
  to the <b>help</b> utility), or may be in a separate file.
  The input text consists
  of a mixture of lines of text and <b>lroff</b> directives.
  <b>Lroff</b> recognizes only a few directives,
  summarized in the <span style="font-family: monospace;">"Request Summary"</span> below.  Whenever a directive
  performs the same function as a UNIX TROFF directive, the name is the same.
  Unrecognized directives are ignored, and are not passed on to the output.
  Directives must be left justified and preceeded by a period.
  </p>
  <p>
  Help text need not be formatted unless desired.  Filling and justification
  are NOT ENABLED unless a legal directive (other than <span style="font-family: monospace;">".nf"</span>) is given on the
  line immediately following the <span style="font-family: monospace;">".help"</span> directive.
  </p>
  <p>
  While filling, embedded whitespace in text IS significant to <b>lroff</b>,
  except at the end of a line.
  <b>lroff</b> recognizes no special characters.
  Blank lines cause a break, and are passed on to the output (a blank line
  is equivalent to <span style="font-family: monospace;">".sp"</span>). 
  Case is not significant in command directives.
  Control characters embedded in text will be passed on to the output.
  </p>
  <p>
  Since both whitespace and blank lines are significant, <b>lroff</b> will properly
  format ordinary paragraphs of text, and single line section headers,
  without need for embedded directives.
  </p>
  <p>
  Since the i/o routines used by <b>lroff</b> are parameterized, pagination can be
  achieved by having the user supplied OUTPUT procedure count output lines.
  Similarly, pagination control directives can be added to the list of
  <b>lroff</b> directives, to be intercepted by the user supplied INPUT procedure.
  See the Manpage command for an example.
  </p>
  <p>
  DIRECTIVES
  </p>
  <p>
  Most of the <b>lroff</b> directives function the same as in the UNIX text
  formatters.  For the benefit of readers without experience with UNIX,
  <span style="font-family: monospace;">"filling"</span> means collecting words of text until an output line has been
  filled, and <span style="font-family: monospace;">"justification"</span> refers to adding extra spaces between words
  to cause the output line to be both left and right justified (as in this
  paragraph).  Filling is disabled with NF, and resumes following a FI.
  While filling is disabled, only the control directives FI and RJ will be
  recognized.  Justification is enabled with JU, and disabled with NJ.
  The filling of an output line may be stopped, and the line output, with BR.
  SP (or a blank line) does the same thing, outputting one or more blank
  lines as well.  CE causes the current line to be broken, and outputs the
  next line of input, centered.
  </p>
  <p>
  The directive <span style="font-family: monospace;">".rj text"</span> breaks the current line, and outputs the next
  line of input, unfilled, with <span style="font-family: monospace;">"text"</span> right justified on the same line.
  RJ is especially useful for numbering equations.  The RJ directive is
  recognized whether or not filling is in effect.
  </p>
  <p>
  SH and IH may be used for section headers.  Both cause a break, followed
  by a couple blank lines, followed by the next line of input,
  left justified on the output line.  The left margin is reset to its
  initial value.  If IH is used, the text following the section header will
  be indented one level in from the left margin.
  The number of lines of blank lines before the heading,
  and the amount of indentation, are optional arguments.
  The default values are shown in the request summary below.  If values
  other than the defaults are desired, they need only be supplied as arguments
  once.  Succeeding calls will continue to use the new values.
  </p>
  <p>
  The IH and LS directives are especially useful in help text (manual pages).
  LS with a label string is useful for parameter lists,
  as shown in the example below.
  LS without a label string is used for relative indenting.
  A following LE restores the previous level of indentation.
  </p>
  <p>
  The LS directive has the form <span style="font-family: monospace;">".ls [n] [stuff]"</span>, where <span style="font-family: monospace;">"n"</span> (optional)
  is the amount by which the following text is to be indented,
  and <span style="font-family: monospace;">"stuff"</span> is the (optional) label for the indented text block.
  LS causes a break, followed by one blank line, then the label string (if given),
  left justified.
  If the length of <span style="font-family: monospace;">"stuff"</span> is less than N-1 characters, the text
  block will start filling on the same line, otherwise on the next line.
  The indented text block may contain anything, including additional LS
  directives if nesting is desired.  A matching LE eventually terminates the
  block, restoring the previous level of indentation.
  </p>
  <p>
  The LS directive takes the most recent argument as the new default
  indentation, allowing the argument to be omitted in subsequent calls.
  To keep the current default value from being changed, use a negative
  argument.
  </p>
  </section>
  <section id="s_example">
  <h3>Example</h3>
  <br>
  <p>
  Many examples of the use of the <b>lroff</b> command directives in help text
  can be found by browsing about in source listings.
  A brief example is included here for convenient reference.
  <br>
  The <span style="font-family: monospace;">".help"</span> directive, used to mark the beginning
  of a block of help text, is used by HELP and MANPAGE rather than <b>lroff</b>.
  The (optional) arguments to <span style="font-family: monospace;">".help"</span> are the keyword name of the help
  text block, and two strings.
  The keyword argument may be a list of the form <span style="font-family: monospace;">".help keyw1,
  keyw2, ..., keywn"</span>, if more than one keyword is appropriate.
  The first keyword in the list is placed in the header of a manual page,
  followed by the first string, in parenthesis.  The second string,
  if given, is centered in the header line.  The strings need not be
  delimited unless they contain whitespace.
  <br>
  The <b>lroff</b>-format help text fragment
  <br>
  </p>
  <div class="highlight-default-notranslate"><pre>
  .help stcopy   2       "string utilities"
  .ih
  NAME
  stcopy -- copy a string.
  .ih
  PURPOSE
  Stcopy is used to copy an EOS delimited character
  string.  The EOS delimiter MUST be present.
  .ih
  USAGE
  stcopy (from, to, maxchar)
  .ih
  PARAMETERS
  .ls from
  The input string.
  .le
  .ls to
  The output string, of length no less than "maxchar"
  characters (excluding the EOS).
  .le
  .ls maxchar
  The maximum number of characters to be copied.
  Note that "maxchar" does not include the EOS.
  Thus, the destination string must contain storage
  for at least (maxchar + 1) characters.
  .le
  .ih
  DESCRIPTION
  ...
  </pre></div>
  <p>
  would be converted by <b>lroff</b> (as called from Help) into something like
  the following.  Remember that the margins are runtime arguments to <b>lroff</b>.
  Help does not print a header line, or break pages.
  <br>
  <br>
  <b>NAME</b>
  <br>
  stcopy -- copy a string.
  <br>
  <br>
  <b>PURPOSE</b>
  <br>
  Stcopy  is  used  to  copy  an  EOS delimited character
  string.  The EOS delimiter MUST be present.
  <br>
  <br>
  <b>USAGE</b>
  <br>
  stcopy (from, to, maxchar)
  <br>
  <br>
  <b>PARAMETERS</b>
  </p>
  <dl id="l_from">
  <dt><b>from</b></dt>
  <!-- Sec='EXAMPLE' Level=0 Label='from' Line='from' -->
  <dd>The input string.
  </dd>
  </dl>
  <dl id="l_to">
  <dt><b>to</b></dt>
  <!-- Sec='EXAMPLE' Level=0 Label='to' Line='to' -->
  <dd>The output string, of length no less than <span style="font-family: monospace;">"maxchar"</span>
  characters (excluding the EOS).
  </dd>
  </dl>
  <dl id="l_maxchar">
  <dt><b>maxchar</b></dt>
  <!-- Sec='EXAMPLE' Level=0 Label='maxchar' Line='maxchar' -->
  <dd>The maximum number of characters to be copied.
  Note that <span style="font-family: monospace;">"maxchar"</span> does not include the EOS.
  Thus, the destination string must contain storage
  for at least (maxchar + 1) characters.
  </dd>
  </dl>
  <br>
  <p>
  <b>DESCRIPTION</b>
  <br>
   ...
  <br>
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  help
  </p>
  <p>
  The reader should note that MANPAGE, which is page oriented,
  recognizes the following directives in addition to those recognized
  by <b>lroff</b>: BP (break page), and KS, KE (start and end keep).  MANPAGE also
  omits blank lines at the top of a page.  These directives may safely
  be included in <b>lroff</b> text, as they will be ignored by <b>lroff</b> if not
  intercepted by the procedure calling <b>lroff</b>.
  </p>
  </section>
  <section id="s_request_summary">
  <h3>Request summary</h3>
  <br>
  <div class="highlight-default-notranslate"><pre>
  Request Initial Default  Break          Meaning
  
    .fi     yes             yes   Begin filling output lines.
    .nf     no              yes   Stop filling output lines.
    .ju     yes             no    Right justify output lines.
    .nj     no              no    Don't right justify.
    .rj text                yes   Rt justify text on next line.
    .sh n           n=2     yes   Skip n lines, start section.
    .ih m n       m=2,n=5   yes   Like SH, but indent n spaces.
    .br                     yes   Stop filling current line.
    .ce                     yes   Center following line.
    .sp n           n=1     yes   Space "n" lines.
    .in n   n=0     n=0     yes   Set left margin to "current+n".
    .ls n label     n=8     yes   Begin labeled text block.
    .le                     yes   End labeled text block.
  
  additional directives provided by MANPAGE:
  
    .bp                     yes   Start a new page of output.
    .tp n   n=4             yes   Break page if &lt; n lines left.
    .ks                     yes   Begin saving output.
    .ke                     yes   Output saved text all on one page.
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'PURPOSE' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLE' 'SEE ALSO' 'REQUEST SUMMARY'  -->
  

.. _commands:

commands: A discussion of the syntax of IRAF commands
=====================================================

**Package: language**

.. raw:: html

  <section id="s_syntax">
  <h3>Syntax</h3>
  <p>
  In <i>command</i> mode (normal interactive commands):
  </p>
  <p>
  	taskname arg1 ... argN par=val ... par=val redir
  </p>
  <p>
  In <i>compute</i> mode (algebraic mode, for expressions and procedures)
  </p>
  <p>
  	taskname (arg1, ... argN, par=val, ... par=val, redir)
  </p>
  </section>
  <section id="s_elements">
  <h3>Elements</h3>
  <dl id="l_taskname">
  <dt><b>taskname</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='taskname' Line='taskname' -->
  <dd>The name of the task to be executed.
  </dd>
  </dl>
  <dl id="l_argN">
  <dt><b>argN</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='argN' Line='argN' -->
  <dd>The positional arguments to the task.  An argument may be any expression;
  in command mode, a parameter name must be enclosed in parenthesis to avoid
  interpretation as a string constant (e.g., filename).
  </dd>
  </dl>
  <dl id="l_param">
  <dt><b>param=value</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='param' Line='param=value' -->
  <dd>Keyword equals value assignment.  The value of the parameter named on the
  left is set equal to the value of the expression on the right.
  Keyword equals value assignments must follow any positional arguments.
  To save typing, boolean (yes/no) parameters may be set with a trailing
  + or -, e.g., <span style="font-family: monospace;">"verbose+"</span> is the same as <span style="font-family: monospace;">"verbose=yes"</span>.
  </dd>
  </dl>
  <dl id="l_redir">
  <dt><b>redir</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='redir' Line='redir' -->
  <dd>A file redirection argument, e.g.:
  <div class="highlight-default-notranslate"><pre>
  &gt; file          spool output in a file
  &lt; file          read input from a file (rather than the terminal)
  &gt;&gt; file         append the output to a file
  &gt;&amp; file         spool both error and regular output in a file
  &gt;&gt;&amp; file        append both error and regular output to a file
  &gt;[GIP]          redirect graphics output to a file, e.g, &gt;G file
  &gt;&gt;[GIP]         append graphics output to a file, e.g, &gt;&gt;G file
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A CL command is an invocation of a predefined CL task.
  A task may be one of the numerous builtin functions
  (e.g. time, lparam, ehistory),
  a task defined in a package supplied to the user automatically,
  (e.g., the <i>directory</i> task in the <i>system</i> package),
  or a task the user has defined himself, using the <i>task</i> directive.
  </p>
  <p>
  The entire argument list of a command, including file redirection arguments
  may be enclosed in parentheses.  This forces all arguments to be evaluated
  in compute mode.  In command mode arguments are delimited by spaces and
  most characters may be included in strings without need to quote the strings.
  In compute mode arguments are delimited by commas, all strings must be
  quoted, and all CL arithmetic and other operators are recognized.
  Command mode is the default everywhere, except within parenthesis, on the
  right hand side of a <span style="font-family: monospace;">"= expr"</span> (inspect statement), or within procedures.
  The sequence #{ &lt;statements&gt; #} may be used to force interpretation of a
  series of statements in compute mode.
  </p>
  <p>
  1. <b>Arguments</b>
  </p>
  <p>
      The task name may be followed by any number of positional arguments
  and/or keyword=value type arguments, switches, or i/o redirection arguments.
  The positional arguments must come first.  Arguments are most commonly simple
  numeric or string constants, but general expressions are allowed.
  Some examples of arguments follow.
  </p>
  <div class="highlight-default-notranslate"><pre>
  "quoted string"
  (cos(.5)**2 + sin(.5)**2)
  "work" // 02
  k + 2                   # valid only in compute mode
  i+3                     # valid in both modes
  (i+3)                   # same answer in both modes
  </pre></div>
  <p>
  Within an argument the treatment of unquoted strings depends upon
  the current mode.  In command mode the string is assumed to be
  a string constant, while in compute mode it is taken to be the
  name of a parameter.  For example, in command mode the expression
  </p>
  <p>
  	i+3
  </p>
  <p>
  is equivalent to the string <span style="font-family: monospace;">"i+3"</span>, while in compute mode this would
  evaluate to the sum of the <i>value</i> of the parameter <span style="font-family: monospace;">"i"</span> plus 3.
  To force evaluation of a string like i+3 as a arithmetic expression,
  enclose it in parenthesis.
  </p>
  <p>
  Positional arguments are assigned to the parameters of the task to
  be executed.  The position of each task parameter is determined by the
  order of the arguments in the <i>procedure</i> declaration of a
  procedure script task, or by the order of declaration of the parameters
  in a parameter file for other tasks.
  </p>
  <p>
  Hidden parameters cannot be assigned values positionally (one must use
  keywork assignment).  It is an error to have more positional arguments
  than there are corresponding parameters in the task, but omitting
  positional arguments is legal.  In compute mode, arguments
  may be skipped using commas to mark the skipped arguments, e.g. a,,b.
  </p>
  <p>
  Following the positional arguments the user may specify keyword
  arguments.  All parameters of a task, including hidden parameters
  may be assigned to using keyword arguments.  The form of a keyword
  argument is
  </p>
  <p>
  	param=expr
  </p>
  <p>
  where <i>param</i> is the name of the task's parameter, and <i>expr</i> is
  any legal CL expression.  If the parameter is boolean an alternative syntax
  called the <span style="font-family: monospace;">"switch"</span> syntax is available:
  </p>
  <div class="highlight-default-notranslate"><pre>
  param+          # same as param=yes
  param-          # same as param=no
  </pre></div>
  <p>
  A given parameter may only be assigned to once in a command line.
  </p>
  <p>
  2. <b>I/O Redirection</b>
  </p>
  <p>
      Following the argument list the user may specify one or more file
  redirection parameters.  This permits the altering of standard i/o streams
  for this command only.  Note that the file name specified is interpreted
  according to the current mode, i.e.
  </p>
  <p>
  	&gt; file
  </p>
  <p>
  sends output to a file with the name <span style="font-family: monospace;">"file"</span> in command mode, but uses
  the <i>value</i> of the parameter <span style="font-family: monospace;">"file"</span> as the filename in compute mode.
  </p>
  <p>
  The output from one command may also be directed to the input of another
  using pipes.  The syntax is
  </p>
  <div class="highlight-default-notranslate"><pre>
      command1 | command2
  or
      command1 |&amp; command2
  </pre></div>
  <p>
  Here command1 and command2 are full commands, including the taskname
  and all arguments.
  In the first example the standard output of command1 becomes
  the standard input of command2, while in the second the both the
  standard and error output are sent to command2.
  </p>
  <p>
  Once two commands have been joined by a pipe they function effectively
  as a single command, and the combined command may be joined by
  pipe to further commands.  The resulting <span style="font-family: monospace;">"command block"</span> is executed
  as a unit, and may be submitted as a background job by following the
  command block with an <span style="font-family: monospace;">"&amp;"</span>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Simple positional arguments only (command mode).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; copy file1 file2
  </pre></div>
  <p>
  2. Simple positional arguments only (compute mode).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; copy ("file1", "file2")
  </pre></div>
  <p>
  3. One positional argument, i.e., the string <span style="font-family: monospace;">"file1,file"</span>, and one keyword=value
  type argument.  Note that string need not be quoted even though it contains
  the comma, provided there are no spaces in the string.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lprint file1,file2 device=versatec
  </pre></div>
  <p>
  4. Syntax for i/o redirection in compute mode, as in a script.
  </p>
  <p>
  	type (<span style="font-family: monospace;">"*.x"</span>, &gt; <span style="font-family: monospace;">"spool"</span>)
  </p>
  <p>
  5. The same command in command mode.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type *.x &gt; spool
  </pre></div>
  <p>
  6. Use of an arithmetic expression in command mode; the scalar value of the
  expression given as the third positional argument is added to the value
  of every pixel in image <span style="font-family: monospace;">"pix1"</span>, writing a new image <span style="font-family: monospace;">"pix2"</span> as output.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imarith pix1 + (log(4.2)+10) pix2
  </pre></div>
  <p>
  Many additional examples may be found in the EXAMPLES section of the
  manual pages throughout the system.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  procedure, parameters
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNTAX' 'ELEMENTS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

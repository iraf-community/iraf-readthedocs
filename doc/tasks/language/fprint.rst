.. _fprint:

fprint: Print a line into a parameter
=====================================

**Package: language**

.. raw:: html

  <div class="highlight-default-notranslate"><pre>
  print  -- print to the standard output
  fprint -- print to a parameter
  printf -- formatted print to the standard output
  </pre></div>
  <section id="s_usage">
  <h3>Usage</h3>
  <div class="highlight-default-notranslate"><pre>
  print  expr [expr ...]
  fprint param expr [expr ...]
  printf format [arg ...]
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_expr">
  <dt><b>expr</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expr' Line='expr' -->
  <dd>Any expression, the string value of which is to be printed.
  </dd>
  </dl>
  <dl id="l_param">
  <dt><b>param</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='param' Line='param' -->
  <dd>The <i>fprint</i> call will deposit the output string in the value field of 
  this parameter.
  </dd>
  </dl>
  <dl id="l_format">
  <dt><b>format</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='format' Line='format' -->
  <dd>A C-like format specification string containing plain characters, which 
  are simply copied into the output string, and conversion specifications,
  each of which causes conversion and printing of zero or more <i>args</i>.
  </dd>
  </dl>
  <dl id="l_arg">
  <dt><b>arg    </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='arg' Line='arg    ' -->
  <dd>Any expression, variable, parameter value or constant to be used in the
  <i>format</i> string's conversion specifications.  One arg is required for
  each conversion specification.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>print</i> and <i>fprint</i> commands format a line of text and write
  it to either the standard output or in the case of <i>fprint</i>,
  the p_value field of the named parameter.  The output is free format although
  spaces may be specifically inserted (as quoted string constants) to make the
  output easier to read.  One space is automatically inserted after each
  numeric argument; this can be defeated by coercing the argument to a string
  with the <i>str</i> intrinsic function.  A newline is automatically output
  at the end of the output line.  I/O redirection may be used with <i>print</i>
  or <i>printf</i> to write to a file or through a pipe to another task.
  </p>
  <p>
  The <i>printf</i> command allows more control over the output format and can
  convert arguments for printing as another type.  The <i>format</i> string
  contains plain text characters and format specifications as well as
  escape sequences for printing tabs, newlines, etc. Unlike the other
  two commands, spaces and newlines must be explicitly given in the format
  string.  
  </p>
  <p>
  A format specification has the form <span style="font-family: monospace;">"%[W][.D]Cn"</span>, where W is  the  field
  width,  D is the number of decimal places or the number of digits of
  precision, C is the format  code,  and  N  is  radix  character  for
  format  code <span style="font-family: monospace;">"r"</span> only.  The W and D fields are optional.  The format
  codes C are as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  b    boolean (YES or NO)
  c    single character (c or '\c' or '\0nnn')
  d    decimal integer
  e    exponential format (D specifies the precision)
  f    fixed format (D specifies the number of decimal places)
  g    general format (D specifies the precision)
  h    hms format (hh:mm:ss.ss, D = no. decimal places)
  m    minutes, seconds (or hours, minutes) (mm:ss.ss)
  o    octal integer
  rN   convert integer in any radix N
  s    string (D field specifies max chars to print)
  t    advance To column given as field W
  u    unsigned decimal integer
  w    output the number of spaces given by field W
  x    hexadecimal integer
  z    complex format (r,r) (D = precision)
  </pre></div>
  <p>
  Conventions for W (field width) specification:
  </p>
  <div class="highlight-default-notranslate"><pre>
  W =  n      right justify in field of N characters, blank fill
      -n      left justify in field of N characters, blank fill
      0n      zero fill at left (only if right justified)
  absent, 0   use as much space as needed (D field sets precision)
  </pre></div>
  <p>
  Escape sequences (e.g. <span style="font-family: monospace;">"\n"</span> for newline):
  </p>
  <div class="highlight-default-notranslate"><pre>
       formfeed
  \n      newline (crlf)
  \r      carriage return
  \t      tab
  \"      string delimiter character
  \'      character constant delimiter character
  \\      backslash character
  \nnn    octal value of character
  </pre></div>
  <p>
  Compute mode (a parenthesized argument list) is recommended for this task
  to avoid surprises.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print the name of the current terminal.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; print ("terminal = ", envget ("terminal"))
  </pre></div>
  <p>
  2. Output a blank line on the standard output, e.g., in a script.
  </p>
  <div class="highlight-default-notranslate"><pre>
  print ("")
  </pre></div>
  <p>
  3. Format a command and send it to the host system.  In this example,
  <span style="font-family: monospace;">"fname"</span> is a string valued parameter.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; print ("!ls -l ", fname) | cl
  </pre></div>
  <p>
  4. Write to a file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  for (x=1.;  x &lt; 1E5;  x *= 10)
      print ("the sqrt of ", x, "is ", sqrt(x), &gt;&gt; "output")
  </pre></div>
  <p>
  5. Print a formatted string.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; printf ("pi = %.6f\n", 2*atan2(1.0,0.0))
  pi = 3.141593
  cl&gt; printf ("RA = %h  DEC = %m\nExptime = %8.2f\n",ra,dec,etime)
  RA = 18:32:33.5 DEC = 23:45.2   Exptime =     1.57
  </pre></div>
  <p>
  6. Print to a parameter.  Note that <i>fprint</i> allows you to create a 
  formatted string, whereas the scan() example requires a struct parameter.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; x = 3.14159
  cl&gt; fprint (s1, "pi = ", x)
  cl&gt; = s1
  pi = 3.14159
  </pre></div>
  <p>
  or 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; printf ("pi = %g\n", x) | scan (line)
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The <i>fprint</i> task is not very useful since the same thing can be
  accomplished by string concatenation and assignment.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  scan, scanf, fscan, fscanf, strings
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

.. _joinlines:

joinlines: Join text files line by line
=======================================

**Package: proto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  joinlines list1 [list2]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_list1">
  <dt><b>list1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='list1' Line='list1' -->
  <dd>List of input text files to be joined.  It is an error if a file does
  not exist.  The special file <span style="font-family: monospace;">"STDIN"</span> may be used to read from the
  terminal, redirected input, or a pipe.
  </dd>
  </dl>
  <dl id="l_list2">
  <dt><b>list2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='list2' Line='list2' -->
  <dd>Optional second list of input text files to be combined with the
  first list.  This only applies when two lists are specified on
  the command line otherwise this parameter is ignored.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">"STDOUT"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = "STDOUT"' -->
  <dd>Output filename.  The result of joining the input lines is appended
  to the specified file.  The special file <span style="font-family: monospace;">"STDOUT"</span> selects the standard
  output stream, which is usually the terminal but which may be redirected.
  </dd>
  </dl>
  <dl id="l_delim">
  <dt><b>delim = <span style="font-family: monospace;">" "</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='delim' Line='delim = " "' -->
  <dd>The delimiter placed between joined input lines.  The default is a space
  (note that this will not be visible when viewed with <b>eparam</b>).
  </dd>
  </dl>
  <dl id="l_missing">
  <dt><b>missing = <span style="font-family: monospace;">"Missing"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='missing' Line='missing = "Missing"' -->
  <dd>This string is substituted for missing lines when going beyond the end
  of shorter input files.
  </dd>
  </dl>
  <dl id="l_maxchars">
  <dt><b>maxchars = 161</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxchars' Line='maxchars = 161' -->
  <dd>Maximum number of characters in output lines.  Longer output lines will
  be truncated and a warning may be given.  Note that this number always
  includes the final newline character.
  </dd>
  </dl>
  <dl id="l_shortest">
  <dt><b>shortest = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shortest' Line='shortest = yes' -->
  <dd>Stop at the end of the shortest file?  If the input files are of unequal
  number of lines then this option provides for stopping at the end
  of the shortest file or the end of the longest file.  In the latter case
  the string specified by the parameter <i>missing</i> is used for input
  from the shorter files.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Warnings are printed to the standard error stream giving the number
  of lines exceeding the maximum number of output characters, the number
  of lines exceeding the IRAF line length limit, and the number of files
  completed in case the files are of unequal length.  If verbose is no
  then no warnings are printed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The task <b>joinlines</b> reads lines from each of the input text files and
  joins them into one line separated by the specified delimiter.  This is useful
  for making multicolumn files from individual files.  The output may
  be directed to the standard output, the default, or appended to a
  file.
  </p>
  <p>
  The list of input files may be given in either <i>list1</i> or with
  <i>list2</i>.  The second list is only used if two arguments are given
  on the command line.  This feature is provided for compatibility with
  an earlier version of this task which only joined two files given separately.
  </p>
  <p>
  There is no limit to the possible number of characters per output line but
  the parameter <i>maxchars</i> may be used to truncate long lines.  This
  can be important because many IRAF tasks read files a line at a time
  with a fixed sized line buffer.  Also other tasks and host programs
  (for example UNIX/vi) have line limits as well.  If an input line
  exceeds these limits incorrect results may occur.  The IRAF limit is 
  SZ_LINE characters (see hlib$iraf.h) and so the default for the maximum 
  number of output characters is set at the current value.  One may 
  chose to go beyond this limit.
  </p>
  <p>
  If the input files do not all have the same number of lines then there
  are two courses of action.  If the <i>shortest</i> parameter is set
  then the join operation is terminated with the last line from the
  shortest file.  If it is not set then the string from the parameter
  <i>missing</i> is substituted for input from the shorter files until
  the end of the longest file is reached.  Note that the delimiter will
  still be placed between input lines even when such lines are missing.
  </p>
  <p>
  There are three types of warnings which may be produced if the verbose
  flag is set.  These are warnings for the number of lines exceeding the
  specified maximum number of characters resulting in truncated output,
  the number of lines exceeding the IRAF line buffer limit, and a warning
  when some input files are shorter than others.  The
  warnings are printed on the standard error stream so that redirection
  of the standard output will still leave the warnings on the user's
  terminal.  To redirect the warnings one must include the standard error
  stream in the redirection syntax.  See the examples for how to do
  this.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Join the two files <span style="font-family: monospace;">"names"</span> and <span style="font-family: monospace;">"titles"</span>, redirecting the output into a third
  file <span style="font-family: monospace;">"personnel_file"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; joinlines names titles &gt; personnel_file
  </pre></div>
  <p>
  2. Join a set of magnitudes given in separate files and place the
  output in <span style="font-family: monospace;">"allmags"</span>.  Separate the columns by tabs.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; joinlines mags* out=allmags delim=" "
  </pre></div>
  <p>
  3. Join a set of files into long lines and redirect the error output
  to a log file.  Set missing lines to INDEF value.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; joinlines tables* out=jointbls miss=INDEF short- ver+ &gt;&amp; log
  </pre></div>
  <p>
  4. Join the second column from the output of a program to the previous
  results.  This illustrates the use of pipes.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; myprog | fields STDIN 2 | joinlines last STDIN &gt; new
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fields
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

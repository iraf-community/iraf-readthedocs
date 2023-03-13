.. _redefine:

redefine: Redefine a task
=========================

**Package: language**

.. raw:: html

  <div class="highlight-default-notranslate"><pre>
  task     -- define a new IRAF task
  redefine -- redefine an IRAF task
  </pre></div>
  <section id="s_usage">
  <h3>Usage</h3>
  <div class="highlight-default-notranslate"><pre>
  task     t1 [t2 ...] = tfile
  redefine t1 [t2 ...] = tfile
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_t1">
  <dt><b>t1, t2, ...</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t1' Line='t1, t2, ...' -->
  <dd>The names of the new logical tasks.  The task name should be prefixed by a $
  if the task has no parameter file.  An optional extension should be appended
  if either the standard input or output of the task is a binary stream, rather
  than text.  For example, <span style="font-family: monospace;">"$mytask.tb"</span> denotes a task with no parameter file,
  a text standard input, and a binary standard output.
  </dd>
  </dl>
  <dl id="l_tfile">
  <dt><b>tfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tfile' Line='tfile' -->
  <dd>The name of the file to be executed or interpreted to run the task.
  The type of the task is determined by the file extension.  An <span style="font-family: monospace;">".e"</span> extension
  indicates an executable task, while <span style="font-family: monospace;">".cl"</span> indicates a CL script task or
  procedure.  The <i>tfile</i> string is prefixed by a $ to define a
  <i>foreign task</i> (see the discussion below).
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>task</i> statement defines a new task to the CL, and is required before
  the task can be run from the CL.  The new task is added to the <span style="font-family: monospace;">"current
  package"</span>, i.e., the package that is listed when <span style="font-family: monospace;">"?"</span> is entered.  Any task
  definitions made since the current package was entered will be discarded
  when the package is exited.
  </p>
  <p>
  In addition to defining a new task, the <i>task</i> statement defines the
  type and attributes of the new task.  Three types of tasks can be defined:
  script (.cl), executable (.e), and foreign ($...).  A task is assumed to
  have a parameter file (<span style="font-family: monospace;">"taskname.par"</span>, in the same directory as <i>tfile</i>),
  unless the taskname is explicitly prefixed by a $.  A suffix or extension
  may optionally be added to the task name to indicate whether the input and
  output streams are text or binary.  The default is text, meaning that if
  output (or input) is redirected to a file, the file will be opened as a
  text file.
  </p>
  <p>
  The <i>foreign task</i> facility allows host system tasks, e.g., host utilities
  or user written Fortran or C programs, to be called from the CL as if they
  were regular IRAF tasks.  The command line of a foreign task is parsed
  like that of any other task (and unlike an OS escape), allowing expression
  evaluation, i/o redirection, and background job submission.  The difference
  between a regular IRAF task and a foreign task is that the foreign tasks have
  little or no access to IRAF facilities, are usually machine dependent
  (and programs which use them are machine dependent), and cannot be cached.
  Nonetheless the foreign task facility is very useful for personalizing and
  extending the IRAF environment with a minimum of effort.
  </p>
  <p>
  The <i>task</i> statement includes facilities for defining how the host system
  argument list for a foreign task will be built when the task is called from
  the CL.  The simplest form of the foreign task statement is the following:
  </p>
  <p>
  	task [$]taskname = <span style="font-family: monospace;">"$host_command_prefix"</span>
  </p>
  <p>
  where <i>host_command_prefix</i> is the first part of the command string to be
  passed to the host system.  Any command line arguments are simply tacked onto
  the end of this string, delimited by blanks.
  </p>
  <p>
  If this is insufficient then argument substitution may be used to define how
  the argument list is to be built up.  The macro <b>$N</b> denotes argument N
  from the CL command line, with the first argument being number 1.  The macro
  <b>$0</b> is a special case, and is replaced the name of the task being
  executed.  Likewise, <b>$*</b> denotes all arguments.  If the character
  following the $ is enclosed in parenthesis, the corresponding argument string
  will be treated as an IRAF virtual filename, with the equivalent host system
  filename being substituted for use in the host command.  Any other character
  sequences are passed on unchanged.  The argument substitution macros are
  summarized in the table below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  $0              task name
  $N              argument N
  $*              all arguments
  $(...)          host system filename translation of "..."
  </pre></div>
  <p>
  When a task is invoked, an executable is run by starting an attached
  sub-process, while a script is run by starting a new level of the CL
  with its standard input set to the script file.
  </p>
  <p>
  An executable image may contain any number of executable CL tasks, hence it
  can be pointed to by multiple task names or in multiple <i>task</i> statements.
  A script file can only contain one script task.
  </p>
  <p>
  <i>Redefine</i> has the same syntax as the <i>task</i> command, but all the
  task names must already be defined in the current package.  It is often
  useful after misspelling the task file name in a task command.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Call up the editor to create a new program (task) mytask.x.  Compile
  the new program.  Declare it using the task statement and then run it.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; edit mytask.x                       # edit
  cl&gt; xc mytask.x                         # compile &amp; link
  cl&gt; task $mytask = mytask.e             # define task
  cl&gt; mytask arg1 arg2                    # run it
  </pre></div>
  <p>
  2. Define a script task with associated parameter file (if the script is
  a <i>procedure</i>, the parameter file is omitted since procedure scripts
  always have defined parameters).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; task myscript = myscript.cl
  </pre></div>
  <p>
  3. Define the four new tasks implot, graph, showcap, and gkiextract.
  All have parameter files except showcap.  The gkiextract task has a
  binary output stream.  All tasks are executable and are stored in the
  executable file <span style="font-family: monospace;">"plot$x_plot.e"</span>.  Note the use of comma argument
  delimiters in this example; this is a compute mode example as would
  be found in a package script task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  task    implot,                 # compute mode syntax
          graph,
          $showcap,
          gkiextract.tb   = "plot$x_plot.e"
  </pre></div>
  <p>
  4. Make the listed UNIX programs available in the IRAF environment as
  foreign tasks.  None of the tasks has a parameter file.  The <span style="font-family: monospace;">"$foreign"</span>
  declares the tasks as foreign, and indicates that the IRAF task name
  is the same as the host system task name.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; task $ls $od $rlogin = $foreign
  </pre></div>
  <p>
  5. Define a couple of foreign tasks for VMS, where the command to be sent
  to VMS is not the same as the IRAF task name.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; task $run   = $run/nodebug
  cl&gt; task $debug = $run/debug
  cl&gt; task $top   = "$show proc/topcpu"
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The distinction between command and compute mode syntax can be confusing.
  When defining tasks in your login.cl or in a package script task, use
  compute mode, with commas between the arguments and all strings quoted
  (there are plenty of examples in the system).  When typing in <i>task</i>
  statements interactively, use command mode.  If you forget and leave in
  the commas, they will be assumed to be part of the task name, causing the
  following error message when the task is run:
  </p>
  <p>
  	ERROR: IRAF Main: command syntax error
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  prcache, flprcache, package
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

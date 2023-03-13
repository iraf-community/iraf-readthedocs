.. _cl:

cl: Execute commands from the standard input
============================================

**Package: language**

.. raw:: html

  <div class="highlight-default-notranslate"><pre>
  cl    -- call the CL as a task
  clbye -- like cl(), but closes current script file too
  </pre></div>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_gcur">
  <dt><b>gcur = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gcur' Line='gcur = ""' -->
  <dd>Global graphics cursor.
  </dd>
  </dl>
  <dl id="l_imcur">
  <dt><b>imcur = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imcur' Line='imcur = ""' -->
  <dd>Global image cursor.
  </dd>
  </dl>
  <dl id="l_abbreviate">
  <dt><b>abbreviate = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='abbreviate' Line='abbreviate = yes' -->
  <dd>Permits minimum match abbreviations of task and parameter names (disabled
  within scripts).
  </dd>
  </dl>
  <dl id="l_echo">
  <dt><b>echo = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='echo' Line='echo = no' -->
  <dd>Echo all commands received by the CL on the terminal.
  </dd>
  </dl>
  <dl id="l_ehinit">
  <dt><b>ehinit = <span style="font-family: monospace;">"standout eol noverify"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ehinit' Line='ehinit = "standout eol noverify"' -->
  <dd>Ehistory options string.  (See <span style="font-family: monospace;">"ehistory"</span>)
  </dd>
  </dl>
  <dl id="l_epinit">
  <dt><b>epinit = <span style="font-family: monospace;">"standout noshowall"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='epinit' Line='epinit = "standout noshowall"' -->
  <dd>Eparam options string.  (See <span style="font-family: monospace;">"eparam"</span>)
  </dd>
  </dl>
  <dl id="l_keeplog">
  <dt><b>keeplog = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='keeplog' Line='keeplog = no' -->
  <dd>Keep a log of all CL commands.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"uparm$logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "uparm$logfile"' -->
  <dd>The name of the logfile, if command logging is enabled.
  </dd>
  </dl>
  <dl id="l_logmode">
  <dt><b>logmode = <span style="font-family: monospace;">"commands nobackground noerrors notrace"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logmode' Line='logmode = "commands nobackground noerrors notrace"' -->
  <dd>Logging mode control parameter.  (See <span style="font-family: monospace;">"logging"</span>)
  </dd>
  </dl>
  <dl id="l_lexmodes">
  <dt><b>lexmodes = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lexmodes' Line='lexmodes = yes' -->
  <dd>Enable automatic mode switching between <span style="font-family: monospace;">"command mode"</span> (used when commands are
  being entered interactively at the terminal), and <span style="font-family: monospace;">"compute mode"</span> (used to
  evaluate arithmetic expressions and argument lists).  If <i>lexmodes</i> is
  disabled command mode is disabled.  Command mode is always disabled within
  scripts and within parenthesis, i.e., expressions or formal argument lists.
  </dd>
  </dl>
  <dl id="l_menus">
  <dt><b>menus = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='menus' Line='menus = yes' -->
  <dd>If <i>menus</i> are enabled, a table will be printed whenever a package is
  entered or exited listing the tasks (or subpackages) in the new package.
  </dd>
  </dl>
  <dl id="l_mode">
  <dt><b>mode = <span style="font-family: monospace;">"ql"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mode' Line='mode = "ql"' -->
  <dd>The parameter mode of the CL, and of any tasks run by the CL which do not
  specify their own mode (i.e., which specify `auto' mode).  A <span style="font-family: monospace;">"q"</span> causes a
  query to be generated whenever a parameter is used which was not set explicitly
  on the command line.  An <span style="font-family: monospace;">"m"</span> (menu mode) causes <i>eparam</i> to be called to
  edit/check a task's parameters when the task is run interactively.  An <span style="font-family: monospace;">"l"</span>
  causes the parameter file for a task to be updated on disk whenever the task
  is run interactively.  Note that changing the mode at the CL level will have
  no affect on the operation of an individual task unless <span style="font-family: monospace;">"auto"</span> mode is set
  at the package, task, and parameter level, causing the mode to defer to the
  global CL mode.
  </dd>
  </dl>
  <dl id="l_notify">
  <dt><b>notify = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='notify' Line='notify = yes' -->
  <dd>If <i>notify</i> is enabled background jobs will print a message on the user
  terminal (or in the logfile for a queued job) notifying the user when the
  job completes.
  </dd>
  </dl>
  <dl id="l_szprcache">
  <dt><b>szprcache = (a small number)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='szprcache' Line='szprcache = (a small number)' -->
  <dd>Controls the size of the process cache.  The value may range from 1 to 10.
  A larger number reduces process spawns but the idle processes may consume
  critical system/job resources.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>cl</i> and <i>clbye</i> commands are used to call the CL as a task.
  The function of the <i>cl</i> task is to read and execute commands from
  its standard input until <i>bye</i> or end of file is reached.  The <i>cl</i>
  task may be called with arguments or executed in the background like any
  other task.  The <i>cl</i> task may be called from within a procedure or
  script to read commands from the command stream which called that procedure
  or task; this is usually the terminal but may be a another script.
  </p>
  <p>
  When the <i>cl</i> or <i>clbye</i> command is invoked, the command language
  interpreter stores information about which tasks and packages are currently
  defined.  When the command is finished any tasks or packages which
  have become defined since invocation are lost, unless the user specifically
  overrides this by using the <i>keep</i> command.
  </p>
  <p>
  The <i>clbye</i> command performs exactly like a <i>cl</i> followed by a
  <i>bye</i>, except that when called from a script the script file is closed
  immediately, freeing its file descriptor for use elsewhere.  If <i>cl</i>
  is used instead of <i>clbye</i> in a script, the file is not closed until
  after the <i>cl</i> returns.  If a <i>clbye</i> is used in a script, any
  commands following the <i>clbye</i> will not be executed.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Execute CL commands from a file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cl &lt; cmdfile
  </pre></div>
  <p>
  2. Execute CL commands from a pipe.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; print ("!type ", fname) | cl
  </pre></div>
  <p>
  3. Execute <i>cl</i>, taking command input from the terminal.  Since command
  input is already from the terminal, the only effect is to mark the state
  of CL memory, to allow <i>task</i>, <i>set</i>, and other definitions to be
  made temporarily and later freed by terminating the <i>cl</i> with a <i>bye</i>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cl
  cl&gt; set pak = "home$tasks/"
  cl&gt; task $mytask = pak$x_mytask.e
          (execute the task)
  cl&gt; bye
  </pre></div>
  <p>
  In the example above, the declarations of the logical directory <span style="font-family: monospace;">"pak"</span> and the
  task <span style="font-family: monospace;">"mytask"</span> are discarded when the <i>bye</i> is entered, terminating the
  <i>cl</i>.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Beware that any changes made to the global CL parameters during the execution
  of a <i>cl</i> remain in effect after the task terminates.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  bye, keep, logout
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

.. _eparam:

eparam: Edit parameters of a task
=================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  eparam task [task ...]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_task">
  <dt><b>task</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='task' Line='task' -->
  <dd>The name of the task whose parameter set is to be edited.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>eparam</i> command calls up an interactive screen editor
  to edit the parameters of the named task or tasks.  The syntax of the
  page editor is controlled by the environment variable `editor' which
  may have the values <span style="font-family: monospace;">"edt"</span>, <span style="font-family: monospace;">"emacs"</span>, or <span style="font-family: monospace;">"vi"</span>.  The user may also customize
  the editor by copying the associated <span style="font-family: monospace;">"dev$*.ed"</span> file to their home
  directory, and editing the file.
  </p>
  <p>
  The CL parameter <span style="font-family: monospace;">"epinit"</span> may be used to set the following options:
  </p>
  <dl>
  <dt><b>[no]standout</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[no]standout' -->
  <dd>Enables or disables use of standout mode (reverse video) in the display.
  </dd>
  </dl>
  <dl>
  <dt><b>[no]showall</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[no]showall' -->
  <dd>Controls whether or not hidden parameters are displayed and edited.
  </dd>
  </dl>
  <p>
  The <i>eparam</i> task may be used to edit either ordinary task parameter
  sets, or named parameter files.
  The presence or absence of a <b>.par</b> filename extension is used to
  determine whether an operand is a taskname or a filename.  For example,
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; eparam skypars.par
  </pre></div>
  <p>
  will edit the parameter <i>file</i> <b>skypars.par</b> in the current directory,
  whereas
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; eparam skypars
  </pre></div>
  <p>
  will edit the parameter set for the pset-task <i>skypars</i>.
  Lastly, since <i>spypars</i> is a pset-task, we could just type
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skypars
  </pre></div>
  <p>
  to edit or review the contents of the pset.
  </p>
  <p>
  The parameter file <b>skypars.par</b> in the above example would probably be
  created using the new colon-command extensions to eparam.  The original
  eparam supported only single keystroke editing commands.  The new colon
  commands are used to enter command lines of arbitrary length to be processed
  by eparam.
  </p>
  <p>
  A colon command is entered by typing the colon character (`<b>:</b>') while
  the cursor is positioned to the starting column of any value field of the
  parameter set being edited.  The colon character is not recognized as a
  special character beyond column one, e.g., when entering the string value
  of a parameter.  When colon command mode is entered, the colon character
  will be echoed at the start of the bottom line on the screen, and the cursor
  will move to the character following the colon, waiting for the command to
  be entered.  The command is read in raw mode, but the usual delete,
  &lt;ctrl/c&gt;, &lt;ctrl/u&gt;, etc. sequences are recognized.
  </p>
  <p>
  The following eparam colon commands are currently supported.  All commands
  are carefully error checked before being executed to avoid having eparam
  abort with a stack trace.  An illegal operation causes colon command entry
  mode to be exited, leaving an error message on the command entry line.
  All commands which cause editing of the current pset to terminate may include
  the <b>!</b> character to avoid updating the current pset before reading in
  the new one or exiting eparam.  The default is to update the current pset.
  In all cases, <i>pset</i> may be either the name of a task or the name of a
  parameter file.  Parameter files are always indicated by a <b>.par</b>
  extension, even though the actual file may be a <b>.cl</b> file:
  only <b>.par</b> files will be written, although either type of file may be
  read.
  </p>
  <dl>
  <dt><b>:e[!] [pset]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':e[!] [pset]' -->
  <dd>Edit a new pset.  If <i>pset</i> is omitted and the cursor was positioned to
  a pset parameter when the colon command was entered then eparam descends into
  the referenced pset; when editing of the sub-pset is complete eparam returns
  to editing the higher level pset at the point at which the '<b>:e</b>'
  command was entered.  If a pset is named the editor context is switched to
  the new pset, updating the current pset first unless the '<b>:e!</b>' command
  was given.
  </dd>
  </dl>
  <dl>
  <dt><b>:q[!]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':q[!]' -->
  <dd>Exit eparam for the current pset; equivalent to a &lt;ctrl/z&gt;.  The variant
  '<b>:q!</b>' causes eparam to be exited without updating the current pset.  
  Entering this command when editing a sub-pset causes an exit to the higher
  level pset.  To abort eparam entirely without updating anything, &lt;ctrl/c&gt;
  should be used.
  </dd>
  </dl>
  <dl>
  <dt><b>:r[!] [pset]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':r[!] [pset]' -->
  <dd>Read in a new pset.  If the command is '<b>:r</b>', an error message is
  printed.  If the command is '<b>:r!</b>' the pset currently being edited
  is reread, canceling any modifications made since the last update.
  If a pset is specified the contents of the named pset are merged into the
  current pset, i.e., the named pset is loaded into the current pset,
  overwriting the contents of the current pset.
  The command '<b>:r pfile.par</b>' is commonly used to load a pset formerly
  saved in a user file with '<b>:w pfile.par</b>' into the UPARM version of
  the parameter set for a task.
  </dd>
  </dl>
  <dl>
  <dt><b>:w[!] pset</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':w[!] pset' -->
  <dd>Write or update a pset.  If <i>pset</i> is omitted the pset currently being
  edited is updated on disk.  If <i>pset</i> is given it should normally be the
  name of a parameter file to be written.  If the file exists an error message
  will be printed unless the command '<b>:w! pfile.par</b>' is given to force
  the file to be overwritten.
  </dd>
  </dl>
  <dl>
  <dt><b>:g[o][!]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':g[o][!]' -->
  <dd>Run the task.  Eparam exits, updating the pset and running the task whose pset
  was being edited.  This is implemented by pushing a command back into the input
  stream of the task which called eparam, hence if eparam was called in a script
  or with other commands on the same line, execution may be delayed until these
  other commands have been edited.  The feature works as expected when used
  interactively.  Since the run command is pushed back into the command input 
  stream it will appear in the history record and in any log files.
  </dd>
  </dl>
  <p>
  To get out of colon command mode without doing anything, simply type delete
  until the colon prompt is deleted and the cursor returns to the parameter
  it was positioned to when colon command entry mode was entered.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Set standout mode and disable the editing of hidden parameters (leaving
  only the positional parameters).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epinit = "standout noshowall"
  </pre></div>
  <p>
  2. Edit the parameters for the <i>delete</i> task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ep delete
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  lparam, ehistory
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

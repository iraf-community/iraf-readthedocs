.. _ehistory:

ehistory: Edit history file to re-execute commands
==================================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ehistory (or just <span style="font-family: monospace;">"e"</span>)
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <p>
  None.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>ehistory</i> command calls up a screen editor to edit previously
  executed commands, executing the edited command when return is typed.
  Interrupt (e.g., &lt;ctrl/c&gt; may be used to escape from the editor at any time.
  The type of editor commands recognized is determined by the value of the
  CL environment variable <i>editor</i>, which may currently be set to
  <span style="font-family: monospace;">"edt"</span>, <span style="font-family: monospace;">"emacs"</span>, or <span style="font-family: monospace;">"vi"</span>.
  </p>
  <p>
  After the <i>ehistory</i> command is entered, the previous command is
  displayed at the bottom of the terminal.  If the previous command was
  a compound statement, or if it extended over more than one line,
  all the lines of the command will be displayed.  To reach a different
  command simply enter the appropriate cursor movement keys for the editor type
  being used.  When the cursor attempts to move above the current command
  the previous command will be displayed.  Similarly when it attempts
  to move below, the next command will appear.  Hitting the return
  key will execute the command currently being edited.
  </p>
  <p>
  The CL parameter <span style="font-family: monospace;">"ehinit"</span> may be used to set the following options:
  </p>
  <dl>
  <dt><b>[no]standout</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[no]standout' -->
  <dd>Controls whether the command to be edited is displayed in reverse or
  normal video.
  </dd>
  </dl>
  <dl id="l_eol">
  <dt><b>eol</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='eol' Line='eol' -->
  <dd>The editor is entered with the cursor positioned to be end of the command line.
  </dd>
  </dl>
  <dl id="l_bol">
  <dt><b>bol</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='bol' Line='bol' -->
  <dd>The editor is entered with the cursor positioned to be beginning of the command
  line.
  </dd>
  </dl>
  <dl>
  <dt><b>[no]verify</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='[no]verify' -->
  <dd>If <i>verify</i> is specified, <i>ehistory</i> will be automatically entered
  when history commands are entered to recall and execute previous commands.
  If <i>noverify</i> is specified, the commands are recalled and immediately
  executed.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Set no standout and verify modes. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ehinit = "nostandout verify".
  </pre></div>
  <p>
  2. Recall the last <span style="font-family: monospace;">"xc"</span> command from the history list and edit it.
  If <i>verify</i> were not enabled the command would simply be repeated.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ^xc
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The command editor really only works well for single line commands;
  multiline command blocks are not easily edited at present.
  VI is poorly emulated at present since only control code editor commands
  are possible.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  eparam
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

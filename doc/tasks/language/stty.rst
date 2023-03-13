.. _stty:

stty: Set/show terminal characteristics
=======================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  stty [terminal]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_terminal">
  <dt><b>terminal</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='terminal' Line='terminal' -->
  <dd>The logical name of the terminal to be used, i.e., the name of the device
  given in the <i>dev$termcap</i> file.
  </dd>
  </dl>
  <dl id="l_baud">
  <dt><b>baud = 9600</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='baud' Line='baud = 9600' -->
  <dd>Set to some nonzero value to inform the VOS of the baud rate; the software
  does not automatically sense the baud rate.  The baud rate must be known to
  accurately generate delays.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = 80</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = 80' -->
  <dd>The logical width of the screen in characters; may be set to some value less
  than the physical width to produce more readable output on very high resolution
  terminals.
  </dd>
  </dl>
  <dl id="l_nlines">
  <dt><b>nlines = 24</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlines' Line='nlines = 24' -->
  <dd>The logical height of the screen in characters.
  </dd>
  </dl>
  <dl id="l_show">
  <dt><b>show = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='show' Line='show = no' -->
  <dd>Show the current terminal driver settings.  The <i>show</i> function is
  automatically enabled if <i>stty</i> is called with no arguments.
  </dd>
  </dl>
  <dl id="l_all">
  <dt><b>all = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='all' Line='all = no' -->
  <dd>Show all terminal driver settings, including those which are not currently
  in use.  Setting <i>all</i> automatically sets <i>show</i>.
  </dd>
  </dl>
  <dl id="l_reset">
  <dt><b>reset = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reset' Line='reset = no' -->
  <dd>Reset the terminal driver settings to their default (login time) values.
  Note that the terminal driver is not a task in the normal sense but is always
  active, and once a parameter is set the new value is retained indefinitely.
  </dd>
  </dl>
  <dl id="l_resize">
  <dt><b>resize = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='resize' Line='resize = no' -->
  <dd>Recompute the terminal screen size parameters, <b>ttyncols</b> and
  <b>ttynlines</b>, and update their values in the environment.
  If the terminal supports runtime querying of the screen size it will be
  queried (allowing the screen size to change dynamically at runtime),
  otherwise the values from the termcap entry for the terminal will be used.
  </dd>
  </dl>
  <dl id="l_clear">
  <dt><b>clear = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clear' Line='clear = no' -->
  <dd>Clear the function(s) which follow on the command line, e.g.,
  <span style="font-family: monospace;">"clear ucasein ucaseout"</span> is equivalent to <span style="font-family: monospace;">"ucasein=no ucaseout=no"</span>.
  </dd>
  </dl>
  <dl id="l_ucasein">
  <dt><b>ucasein = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ucasein' Line='ucasein = no' -->
  <dd>Map terminal input to lower case, e.g., when working on an old monocase
  terminal, or on a modern terminal with the shiftlock key on.
  </dd>
  </dl>
  <dl id="l_ucaseout">
  <dt><b>ucaseout = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ucaseout' Line='ucaseout = no' -->
  <dd>Map terminal output to upper case.
  </dd>
  </dl>
  <dl id="l_login">
  <dt><b>login = <span style="font-family: monospace;">"home$ttyin.log"</span> [off]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='login' Line='login = "home$ttyin.log" [off]' -->
  <dd>Log all input from the terminal to the named text file.
  </dd>
  </dl>
  <dl id="l_logio">
  <dt><b>logio = <span style="font-family: monospace;">"home$ttyio.log"</span> [off]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logio' Line='logio = "home$ttyio.log" [off]' -->
  <dd>Log all terminal i/o to the named text file.  May not be used if either
  <i>login</i> or <i>logout</i> mode is in effect, and vice versa.
  </dd>
  </dl>
  <dl id="l_logout">
  <dt><b>logout = <span style="font-family: monospace;">"home$ttyout.log"</span> [off]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logout' Line='logout = "home$ttyout.log" [off]' -->
  <dd>Log all output to the terminal to the named text file.
  </dd>
  </dl>
  <dl id="l_playback">
  <dt><b>playback = <span style="font-family: monospace;">"home$ttyin.log"</span> [off]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='playback' Line='playback = "home$ttyin.log" [off]' -->
  <dd>Divert terminal driver input to the named <span style="font-family: monospace;">"stty login"</span> style text file,
  i.e., take input from a file instead of from the terminal.  The effect is
  to exactly repeat a previous terminal session executed with <i>login</i>
  mode in effect, e.g., to test or demo software.
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = no' -->
  <dd>If <i>verify</i> is enabled during <i>playback</i> mode the terminal driver
  will read a key from the keyboard before executing each command in the
  logfile.  Tap the space bar to execute the command, <i>q</i> to terminate
  playback mode, or <i>g</i> to continue execution with <i>verify</i> mode
  disabled.  Typing any other key causes a help line to be printed.
  </dd>
  </dl>
  <dl id="l_delay">
  <dt><b>delay = 500 (msec)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='delay' Line='delay = 500 (msec)' -->
  <dd>If <i>verify</i> is disabled during <i>playback</i> mode the terminal driver
  will pause for <i>delay</i> milliseconds before executing each logfile command.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>stty</i> task is used to set or display the terminal device
  characteristics and VOS terminal driver options.
  Without arguments, <i>stty</i> prints the current characteristics of the
  terminal.  The default terminal type can be changed by setting <i>ttyname</i>.
  The terminal characteristics <i>ncols</i>, <i>nlines</i> or <i>baud</i>,
  may be changed by typing new values explicitly on the command line.
  </p>
  <p>
  The most common use of <i>stty</i> is to inform IRAF of the type of terminal
  being used, e.g.,
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stty vt100
  </pre></div>
  <p>
  would set the terminal type to <span style="font-family: monospace;">"vt100"</span>.  An error message will be printed
  unless an entry for the named terminal is present in the <b>termcap</b> file;
  if the named terminal is a graphics terminal, there must also be an entry
  in the <b>graphcap</b> file.
  </p>
  <p>
  To find out about the current terminal settings, type
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stty
  </pre></div>
  <p>
  or
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stty all
  </pre></div>
  <p>
  A limited number of terminal driver options may also be set.  In particular,
  the VOS terminal driver (not to be confused with the host operating system
  terminal driver, a lower level facility) implements facilities for case
  conversion upon input or output, and for logging all i/o to the terminal
  and playing back a terminal session logged in a file.
  </p>
  </section>
  <section id="s_case_conversions">
  <h3>Case conversions</h3>
  <p>
  The <b>ucasein</b> option, if set,
  will cause all upper case terminal input to be mapped to lower
  case (e.g., when working from an old monocase terminal).  In this mode,
  individual upper case characters may be input by preceding them with the
  escape character ^, e.g., <span style="font-family: monospace;">"^MAKEFILE"</span> equates to <span style="font-family: monospace;">"Makefile"</span>.  The full set
  of ^ escapes is summarized below.  The option <b>ucaseout</b> will cause all
  terminal output to be mapped to upper case.  Preceding either or both of
  these option keywords by <b>clear</b> causes the options to be cleared.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ^       shift next character to upper case
  ^+      shift lock (caps lock)
  ^-      clear shift lock
  ^^      the character ^
  </pre></div>
  <p>
  Case shifting is disabled in raw mode, e.g., while in cursor mode, and in
  <b>eparam</b>.  All standard IRAF software, however, will sense that ucase
  mode is set before entering raw mode, and will behave as expected.  Ucase mode
  is also disabled by the STDGRAPH kernel whenever the graphics workstation is
  activated.
  </p>
  <p>
  Note that ^ is also the history meta-character, hence ^^ must be used when
  in <i>ucasein</i> mode to pass a single ^ to the CL history mechanism.
  In cursor mode, upper case keystrokes are intercepted by cursor mode unless
  escaped with a backslash.  Escaped keystrokes are mapped to lower case by
  cursor mode if <i>ucasein</i> mode is in effect, terminating cursor mode and
  returning a lowercase key to the applications program.
  </p>
  </section>
  <section id="s_recording_terminal_i_o">
  <h3>Recording terminal i/o</h3>
  <p>
  The terminal driver options <b>logio</b>, <b>logout</b>, and <b>login</b>
  may be used to log, respectively, all terminal i/o, all output to the terminal,
  or all input from the terminal.  The logfile names are <span style="font-family: monospace;">"home$ttyin.log"</span>,
  <span style="font-family: monospace;">"home$ttyout.log"</span>, or <span style="font-family: monospace;">"home$ttyio.log"</span>, unless a different logfile name is
  specified by the user.  All logfiles are standard textfiles containing only
  printable characters.
  </p>
  <p>
  Terminal i/o logging is especially useful for debugging <i>termcap</i> and
  <i>graphcap</i> entries for new terminals.  All IRAF terminal i/o is logged,
  including raw mode i/o and graphics output.  Terminal i/o from foreign tasks
  or OS escapes is not logged since these tasks bypass the VOS to talk directly
  to the user terminal.
  </p>
  <p>
  Each sequence of characters read from or written to the terminal (via a zgettt
  or zputtt call to the driver) appears as one logical line of text in the
  logfile, delimited by the data character \n (newline).
  When reading from a terminal in raw mode, each input character will appear
  on a separate line in the logfile with no newline, since only a single
  data character is read at a time during raw mode input.
  All control characters embedded in the data, including newline terminators,
  are rendered into printable form.  Long lines are broken near the right margin,
  adding an escaped newline and indenting continuation lines 4 spaces.
  </p>
  <p>
  Terminal i/o logging is intended primarily for debugging purposes, rather
  than for logging user commands; the IRAF command language provides a more
  user friendly facility for command logging (see the <i>language.logging</i>
  manpage for further information on the CL command logging facilities).
  All unprintable ASCII codes are rendered in the logfile in a printable form
  intended to eliminate any ambiguity regarding the exact sequence of characters
  sent to or received from the terminal.  In addition to the standard escape
  sequences \n, \t, \r, etc., the following special escape sequences are used:
  </p>
  <div class="highlight-default-notranslate"><pre>
  \\              \
  \^              ^
  ^@              NUL (ascii 000)
  ^[A-Z]          ctrl/a - ctrl/z (ascii 001 - 032)
  ^[              ESC (ascii 033)
  ^\              FS  (ascii 034)
  ^]              GS  (ascii 035)
  ^^              RS  (ascii 036)
  ^_              US  (ascii 037)
  \s              blank (ascii 040)
  \&lt;newline&gt;      long i/o record continued on next line
  </pre></div>
  <p>
  These special escape sequences, plus any ordinary characters, constitute the
  <i>data</i> recorded in the logfile.  The following additional escape
  sequences are used to record information about the logging session itself in
  the logfile.
  </p>
  <div class="highlight-default-notranslate"><pre>
  \#              rest of line is a comment
  \T              terminal device name at log time
  \G              stdgraph device name at log time
  \O              timestamp written at start of log session
  </pre></div>
  <p>
  Any whitespace (unescaped blanks, tabs, or newlines) appearing
  in the logfile is put there only to make the file more readable, and is not
  considered data.  Blocks of text may be enclosed in a logfile delimited by
  escaped curly brackets, i.e., <span style="font-family: monospace;">"\{ ... \}"</span>.  This is used for the <b>playback</b>
  facility described in the next section.  
  </p>
  </section>
  <section id="s_playback_of_terminal_sessions">
  <h3>Playback of terminal sessions</h3>
  <p>
  The terminal driver has the capability not only of recording terminal i/o
  in a file, but of taking input from a logfile to repeat a sequence of commands
  previously entered by the user with terminal input logging enabled.
  Note that we are not talking about simply playing back recorded output,
  but of actually executing an arbitrary sequence of commands formerly entered
  by the user.  This is different from executing a sequence of commands entered
  into, for example, a CL script, because <i>all</i> input is recorded,
  including not only the commands, but also all responses to parameter queries,
  all rawmode keystroke input, and all graphics cursor input occurring
  interactively during execution of the recorded commands.
  These <b>playback scripts</b> are useful for preparing automated demos or
  tutorials of complex software, and for preparing scripts to be used to
  automatically test software.
  </p>
  <p>
  The basic sequence used to record and later playback a terminal session is as
  follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stty login [= logfilename]
          &lt;execute an arbitrary sequence of commands&gt;
  cl&gt; stty clear login                    # or stty reset
  cl&gt; stty playback [= logfilename]
  </pre></div>
  <p>
  Naturally, the playback script must be executed in the same context as when
  the script was generated, i.e., one must ensure that all necessary packages
  have been loaded, that the current directory has been set to the proper
  value if it matters, and so on.  It is not necessary to execute a playback
  script on the same type of video terminal or graphics terminal as was
  used when the script was recorded; since only the terminal input is being
  recorded, playback scripts are device independent and may be played back on
  any terminal.
  </p>
  <p>
  If desired the commands necessary to establish the starting context may be
  recorded as part of the script.  If the script is going to be repeatedly
  executed it may also be desirable to include commands at the end of the
  recording session to clean up, e.g., deleting any temporary files created
  during the recording session.  If anything has changed which causes a command
  to abort during execution of a playback script, normal terminal input is
  automatically restored, aborting the script.   Note that if the <span style="font-family: monospace;">"stty playback"</span>
  command gets into the playback script for some reason, e.g., because the
  <span style="font-family: monospace;">"stty reset"</span> (or <span style="font-family: monospace;">"stty login=no"</span> etc.) was omitted, then the script will
  repeat indefinitely.  This may or may not be what was desired.
  </p>
  <p>
  Two <b>stty</b> command line arguments are provided for controlling the
  execution of a playback script.  By default, when a script is played back
  the terminal driver will pause for <b>delay</b> milliseconds after echoing
  the command to be executed, to give the user watching the playback a chance
  to read the command.  Aside from this programmed delay, execution is fully
  automated.  For example,
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stty play=filename delay=2000
  </pre></div>
  <p>
  would playback the file <span style="font-family: monospace;">"filename"</span>, with a delay of 2 seconds following echo
  of each line of recorded input text.
  </p>
  <p>
  Alternatively, the user may request that the driver pause and wait for the
  user to type a key before executing each logged command (i.e., before
  returning each input line of text to the application).  This is called the
  <b>verify</b> option.  In verify mode, the following keystrokes may be
  entered to continue execution:
  </p>
  <div class="highlight-default-notranslate"><pre>
  space, return           continue execution
  <span style="font-family: monospace;">'g'</span>                        go: turn verify mode off and continue
  <span style="font-family: monospace;">'q'</span>                        quit: terminate playback mode
  </pre></div>
  <p>
  Verify mode is automatically disabled during raw mode input since the input
  consists of single characters and an inordinate number of verification
  keystrokes would be required from the user.  Either of the <b>verify</b> or
  <b>delay</b> options may be overridden by control directives embedded in the
  playback text, as we shall see in the next section.
  </p>
  </section>
  <section id="s_customizing_playback_scripts">
  <h3>Customizing playback scripts</h3>
  <p>
  Although playback scripts may be and often are generated and played back
  without ever looking at or modifying the actual playback script, there are
  cases where it may be desirable to do so.  For example, when generating a
  script to be used as a demo or tutorial, it may be desirable to insert
  explanatory text into the script to be printed out on the terminal when
  the script is played back, to explain to the person running the script what
  is going on.  Likewise, it may be desirable to control the verify and delay
  options at a granularity finer than the entire script.
  </p>
  <p>
  Explanatory text and/or playback control directives may be inserted into the
  script using the following construct:
  </p>
  <p>
  	<span style="font-family: monospace;">"\{"</span> [&lt;control_directives&gt;] [&lt;text&gt;] <span style="font-family: monospace;">"\}"</span>
  </p>
  <p>
  where <b>control_directive</b> refers to one of the following:
  </p>
  <div class="highlight-default-notranslate"><pre>
  %V+             turn verify on
  %V-             turn verify off
  %NNN            set <b>delay</b> to NNN milliseconds
  </pre></div>
  <p>
  For example,
  </p>
  <div class="highlight-default-notranslate"><pre>
  dir\{%5000
  [list the current directory]\}\n
  </pre></div>
  <p>
  would cause the following to be output, followed after a 5 second delay by a 
  listing of the current directory (the <span style="font-family: monospace;">"&lt;&gt;"</span> is not printed, but shows where
  the cursor will be during the 5 second pause):
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dir
  [list the current directory]&lt;&gt;
  </pre></div>
  <p>
  Note that the newline following the <span style="font-family: monospace;">"\{%5000"</span> in the above example is textual
  data, and will be output to the terminal along with whatever follows, up until
  the closing brace, i.e., <span style="font-family: monospace;">"\}"</span>.  The amount of text to be output may be
  arbitrarily large; there is a builtin limit (currently 4096 characters),
  but it is unlikely that this limit will ever be exceedd, since no more than
  one pageful of text should ever be output in a single call.
  </p>
  <p>
  Normally, a %V or %NNN control directive refers only to the input record
  with which the enclosing \{...\} control block is associated.  The global
  value of <i>verify</i> or <i>delay</i> is temporarily overridden for the
  current record.  If desired, the global value may instead be permanently
  modified by adding a ! after the %, e.g.,
  </p>
  <p>
  	\{%!V-%3000...\}
  </p>
  <p>
  would permanently disable <i>verify</i> (unless a %V+ or %!V+ directive
  follows later in the script) then output the text <span style="font-family: monospace;">"..."</span> followed by a 3
  second delay.
  </p>
  <p>
  To know where to insert the control directives into a script, it is
  important to understand that input from the script is <b>record oriented</b>,
  and that a control directive refers to the input record with which it is
  associated.  An input record is a single <i>logical</i> line of text in the
  input file.  Note that a logical line of text may span multiple physical lines,
  if the newlines are escaped or present as textual data within a control
  directive.  The position of the control directive within the input record
  determines where the explanatory text will be positioned relative to the
  input text, when both are echoed to the terminal.  Any programmed delay or
  pause will always occur after echoing the full record on the terminal.
  </p>
  </section>
  <section id="s_raw_mode_playback">
  <h3>Raw mode playback</h3>
  <p>
  When a program is executing which reads from the terminal in raw mode,
  each character is read from the terminal as soon as it is typed, and
  input characters are not echoed to the terminal unless the application
  explicitly does the echoing.  Examples of programs which use raw mode input are
  <i>eparam</i> and <i>page</i>, which are keystroke driven, and any program
  which reads the <b>graphics cursor</b>, since a graphics cursor read uses raw
  mode input.
  </p>
  <p>
  Playback works much the same for raw input mode as for line input mode,
  except that during raw mode input the input records normally consist of
  single characters, rather than entire lines of text.  By default, <b>verify</b>
  is turned off while reading from the terminal in raw mode, to avoid having
  the user verify each individual character.  Also, the terminal driver will not
  echo text read from the playback file in raw mode, since the text would not
  have been echoed if playback were not in effect.
  </p>
  </section>
  <section id="s_cursor_reads_in_playback_mode">
  <h3>Cursor reads in playback mode</h3>
  <p>
  A typical Tektronix style cursor read will look something like the following,
  as recorded in an <b>stty login</b> script file following a recording session:
  </p>
  <div class="highlight-default-notranslate"><pre>
  K
  3
  )
  '
  *
  \r
  </pre></div>
  <p>
  This six character sequence consists of the key value of the cursor read (K),
  followed by the [x,y] cursor coordinate encoded as four ascii characters
  (<span style="font-family: monospace;">"3)'*"</span> in this case), followed by the <span style="font-family: monospace;">"GIN mode terminator"</span> character or
  characters, normally a single CR (\r).  Of course, if the terminal is not a
  Tektronix compatible terminal (e.g., DEC-Regis), the details will differ
  from this example.
  </p>
  <p>
  The single character per line format of a cursor read reflects the fact that
  each input record is a single character when reading from the terminal in
  raw mode.  For the purposes of playback, however, such a sequence may be
  reformatted on a single line if desired, to improve the readability of a
  script (the extra whitespace in the second example is ignored, since if a
  space were data it would appear as \s).
  </p>
  <div class="highlight-default-notranslate"><pre>
          K3)'*\r
  or
          K 3 ) ' * \r
  or
          K
          3)'*
          \r
  etc.
  </pre></div>
  <p>
  To set the values of the <i>verify</i> or <i>delay</i> parameters for a cursor
  read one may insert the \{...\} sequence anywhere before the \r delimiter
  is returned to the application, e.g.,
  </p>
  <p>
  	K3)'*\r\{%V+\}
  </p>
  <p>
  would do, since the sequence shown forms one logical input record in the
  playback file, and the control directive included will be processed before
  any input data characters from the record are returned to the application.
  If the multi-line form of a cursor read is used, the control directive may
  be tacked onto any of the records K through \r in the example.
  </p>
  <p>
  Output of explanatory text in an interactive graphics session is a little
  more tricky, since if one is not careful the text will come out while in
  graphics mode, causing it to be rendered as random lines drawn all over the
  screen.  A safe technique for outputting comments during playback of a
  graphics session is to output the text to the <b>status line</b>,
  taking care of course to output only a single line of text at once
  (since multiple lines written to the status line would rapidly flash by,
  leaving only the last line visible on the screen).  We can do this by taking
  advantage of the : command sequence, which can be used to put the terminal
  temporarily into status line output mode.
  </p>
  <div class="highlight-default-notranslate"><pre>
  :####\r
  \{%5000
  This is a status line comment\}
  ^U\177
  </pre></div>
  <p>
  For example, insertion of the above sequence between any two cursor reads
  in a recorded interactive graphics session would cause the text
  <span style="font-family: monospace;">"This is a status line comment"</span> to be written to the status line,
  with normal execution of the script occurring after a 5 second delay
  followed by erasure of the status line and exit from status line mode
  (due to the ctrl/u and rubout inserted as data after the colon cursor read).
  </p>
  <p>
  While executing an interactive graphics session via playback, cursor values
  are read from the playback script instead of from the terminal, hence the
  user never sees the actual cursor crosshairs on the screen.  To give the
  user some idea of what is going on, the key values of successive cursor mode
  keystrokes are echoed in ascii down the left side of the screen, starting at
  the upper left.  The keystroke value is also echoed at the position of the
  cursor, to indicate where the cursor crosshairs would have been in an actual
  interactive session.
  </p>
  </section>
  <section id="s_sample_playback_script">
  <h3>Sample playback script</h3>
  <p>
  We conclude with an example of a complete playback script which can be
  entered into a file and played back to demonstrate some of the features of
  the <i>implot</i> task in the PLOT package (the PLOT package must already
  be loaded).
  </p>
  <div class="highlight-default-notranslate"><pre>
  \O=NOAO/IRAF V2.6 iraf@pavo Fri 20:09:21 01-Jan-88
  \T=gterm40
  \G=gterm
  \n
  imheader\sdev$pix\slo+\suser-\n\{%3000
  [Print image header]\}
  \n
  implot\sdev$pix\n
  J3..8\r J3-,)\r J3+)9\r K3)'*\r J3((0\r l3&amp;';\r
  :####\r
  \{%5000
  [use key <span style="font-family: monospace;">`o'</span> to overplot]\}
  ^U\177
  o3&amp;';\r
  K3&amp;';\r K3%*(\r K3#,3\r l3!.?\r
  :####\r
  \{%5000
  [key <span style="font-family: monospace;">`X'</span> expands the plot in x]\}
  ^U\177
  X3!.?\r
  qXXXX\r
  stty\sreset\n
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Show the current terminal type and attributes.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stty
  Terminal=vt640, ncols=80, nlines=24, 9600 baud
  ucasein=no, ucaseout=no, logio=off
  </pre></div>
  <p>
  2. Tell the system that the terminal is a vt100.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stty vt100
  </pre></div>
  <p>
  3. Set the baud rate of the current terminal to 9600 baud.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stty baud=9600
  </pre></div>
  <p>
  4. Set the width of the screen to 80 columns, e.g., to get short menus on a
  workstation where the physical number of columns may be much greater than 80.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stty ncols=80
  </pre></div>
  <p>
  5. Set the terminal type to 4012 and set ucasein and ucaseout modes.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stty 4012 ucasein ucaseout
  </pre></div>
  <p>
  6. Clear the ucasein and ucaseout modes.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stty clear ucasein ucaseout
  </pre></div>
  <p>
  7. Record a terminal session in the default logfile (home$ttyio.log).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stty logio
  </pre></div>
  <p>
  8. Record input from the terminal in the file <span style="font-family: monospace;">"demo"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stty login=demo
  </pre></div>
  <p>
  9. Terminate logging and playback the terminal session recorded in this file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; stty reset
  cl&gt; stty playback=demo
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  1. Note that, when working with a terminal which supports runtime querying
  of the screen size, the screen size is queried when the <b>stty resize</b>
  command is executed, rather than when the terminal screen actually changes size.
  Hence, the screen size parameters printed by a command such as <b>stty show</b>
  will not necessarily reflect the actual screen size.  <b>stty resize show</b>
  queries the terminal for the screen size, hence should always be correct.
  The screen size is automatically queried whenever the <i>page</i> or <i>help</i>
  tasks are run.
  </p>
  <p>
  2. The terminal screen size is determined by querying the terminal for the
  screen size, and reading the response back (this technique has the advantage
  that it works remotely over IPC and network connections, and is host system
  independent).  If the terminal does not respond for some reason, e.g.,
  because the terminal type has been set improperly and the terminal does not
  support the query function, then <b>stty</b> will hang.  Typing a carriage
  return causes execution to resume, after which the error should be corrected.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  language.logging, fio$zfiott.x, etc$sttyco.x
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'Case Conversions' 'Recording Terminal I/O' 'Playback of Terminal Sessions' 'Customizing Playback Scripts' 'Raw Mode Playback' 'Cursor Reads in Playback Mode' 'Sample Playback Script' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

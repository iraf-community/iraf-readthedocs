.. _page:

page: Page through a file
=========================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  page files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>The list of files.  If omitted, text is read from the standard input.
  </dd>
  </dl>
  <dl id="l_map_cc">
  <dt><b>map_cc = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='map_cc' Line='map_cc = yes' -->
  <dd>Map non-printing control characters into printable form, e.g., BEL
  (ctrl/G, ASCII 7) is printed as <span style="font-family: monospace;">"^G"</span>.
  </dd>
  </dl>
  <dl id="l_clear_screen">
  <dt><b>clear_screen = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clear_screen' Line='clear_screen = no' -->
  <dd>If set, the screen is cleared before each page is written.
  </dd>
  </dl>
  <dl id="l_first_page">
  <dt><b>first_page = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='first_page' Line='first_page = 1' -->
  <dd>The first page to be printed.  Pages are defined by form feed characters
  embedded in the text.
  </dd>
  </dl>
  <dl id="l_prompt">
  <dt><b>prompt = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='prompt' Line='prompt = ""' -->
  <dd>Optional prompt string for the end-of-page prompt.  If no prompt string is
  given the name of the file being paged is used.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"terminal"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "terminal"' -->
  <dd>The output device.  The special device <i>text</i> may be specified to
  represent standout mode with upper case rather than reverse video characters.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Page</i> displays a file on the terminal, one page of text at a time,
  pausing between successive pages of output until a key is typed on the
  terminal.  Pages are normally broken when the screen fills, but may also
  be delimited by form feed characters embedded in the input text.
  A prompt is printed after each page of text naming the current file,
  showing the percentage of the file which has been displayed, and the numeric
  order of the file within the file list if a file template was given.
  </p>
  <p>
  When the end of page prompt is displayed any of the following command
  keystrokes may be entered.  Command keystrokes are input in raw mode,
  i.e., no carriage return is required to pass the command to the program.
  </p>
  <div class="highlight-default-notranslate"><pre>
  .               go to the beginning of the current file    [BOF]
  :               colon escape (see below)
  ?               display a one-line command summary
  G               go to the end of the current file          [EOF]
  N,&lt;ctrl/n&gt;      go to the next file
  P,&lt;ctrl/p&gt;      go back to the previous file
  b               back up one page
  d               scroll down half a page of text
  e               edit the current file
  f,space         advance to the next page
  j,return        scroll down one line
  k               back up one line
  n               search for the next occurrence of a pattern
  q               quit
  u               back up half a screen
  
  &lt;ctrl/c&gt;        quit (interrupt)
  &lt;ctrl/z&gt;        quit (EOF)
  &lt;ctrl/d&gt;        quit (EOF)
  </pre></div>
  <p>
  If an unrecognized keystroke is entered the terminal will beep.  The following
  colon commands are recognized in addition to the single keystroke commands
  described above.
  </p>
  <div class="highlight-default-notranslate"><pre>
  :!&lt;clcmd&gt;       send a command to the CL (:!! for host command)
  :/&lt;pattern&gt;     advance to line matching the given pattern
  :file &lt;fname&gt;   display file "fname" (may be abbreviated)
  :help           print summary of colon commands
  :line [+/-]N    goto line N (relative move if +/- given)
  :spool &lt;fname&gt;  spool output to the named file
  </pre></div>
  <p>
  The <i>:clcmd</i> facility is used to send commands to the CL from within
  the context of the pager.  For example, <span style="font-family: monospace;">":!cl"</span> will temporarily suspend the
  pager, allowing CL commands to be entered until the command <span style="font-family: monospace;">"bye"</span> is entered,
  causing execution of the pager to resume.  Note that since the <i>page</i>
  task resides in the system process <i>x_system.e</i>, it will be necessary
  for the CL to connect a second system process if the command issued calls
  another task in the system package, since the first system process will
  still be running, i.e., executing the <i>page</i> task.  This is harmless,
  but the second process may be removed from the process cache with
  <i>flprcache</i> if desired, after exiting the original <i>page</i> task.
  </p>
  <p>
  The sequence <span style="font-family: monospace;">":/"</span> followed by a pattern will cause the current input stream
  to be searched for the next occurrence of the pattern given.  A pattern once
  entered is retained indefinitely and may be used in subsequent searches by
  typing the single keystroke <span style="font-family: monospace;">`n'</span>, without need to reenter the pattern.
  Searching stops at the end of the current file, requiring a <span style="font-family: monospace;">`.'</span> to wrap back
  around to the beginning of the file, or a <span style="font-family: monospace;">`N'</span> to advance to the next file.
  </p>
  <p>
  The <i>:file</i> command is used to change the current position within the
  file list specified by <i>files</i>, and may not be used to page a file not
  specified in the initial template.  Note that the filename may be abbreviated,
  and that searching stops with the first file lexically greater than or equal
  to the given string (hence <span style="font-family: monospace;">":file x"</span> might return file <span style="font-family: monospace;">"y"</span>).
  </p>
  <p>
  The <i>:line N</i> command may be used to randomly position to the indicated line
  within the current file.  If the line number argument N is preceded by a plus
  or minus the argument is taken to be an offset from the current position.
  </p>
  <p>
  The <i>:spool</i> command is used to spool output to a file.  Each time a
  file line is printed on the screen, it is appended to the named file as well.
  One can interactively position to the desired line of the file and then turn
  on spooling to extract a portion of the file or stream being displayed.
  A subsequent <i>:spool</i> command with no filename will turn spooling off.
  Issuing a <i>:spool</i> to begin spooling on a new file when already spooling
  to some other file will cause the old spool file to be closed.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Page through all of the files in the directory <span style="font-family: monospace;">"lib"</span> which have
  the extension <span style="font-family: monospace;">".h"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; page lib$*.h
  </pre></div>
  <p>
  2. Use <i>help</i> to format the text in the file <span style="font-family: monospace;">"doc$spp.hlp"</span>, displaying
  the formatted document beginning on page 5 (the entire document has to be
  formatted first so it takes a minute or so to get any output).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help doc$spp.hlp fi+ | page first=5
  </pre></div>
  <p>
  3. Run <i>rfits</i> to print a long format listing of the headers of a series
  of FITS images from a magnetic tape, directing the output through <i>page</i>
  so that it does not flash by when you aren't looking.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rfits mta make- long+ | page
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Since <i>page</i> does not currently buffer any input text, backwards motions
  and absolute line positioning are not permitted when paging the standard input.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  type, match, head, tail
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

.. _igi:

igi: Interactive Graphics Interpreter.
======================================

**Package: stplot**

.. raw:: html

  <section id="s_description">
  <h3>Description</h3>
  <p>
  'Igi' is an interactive graphics command interpreter that allows a
  user to enter commands to read data, draw plots, and manipulate those
  plots.  The syntax (form of the commands) and semantics of 'igi' are
  based on the MONGO interpreter, but 'igi' runs as an IRAF task and uses
  the IRAF graphics I/O (GIO) and file I/O (FIO) protocols.
  </p>
  <p>
  'Igi' has several significant extensions that are not included in
  MONGO, such as the ability to read ST4GEM tables, new commands such as
  [XY]FLIP, [XYEPLS]EVALUATE, [XYEPLS]SECTION, VPAGE, and EDITCMD, and
  enhancements to MONGO commands such as CURSES.
  </p>
  <dl id="l_Command">
  <dt><b>Command Syntax</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Command' Line='Command Syntax' -->
  <dd>'Igi' commands are read from the standard IRAF input stream (STDIN).
  Therefore, they may be typed interactively, piped or redirected from a
  file on the command line when 'igi' is started.  For example, with igi
  commands in the file mycmd, the following would execute those commands
  just as if they had been typed interactively:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  st&gt; igi &lt;mycmd
  
  </pre></div>
  </dd>
  </dl>
  Typing 'END' or 'BYE' or the end of file on a command file terminates the interpreter.  Type 'HELP' to get
  general information, 'HELP &lt;command&gt;' for information about a specific
  command, or 'APROPOS &lt;keyword&gt;' to list commands associated with the
  keyword.
  When the graphics device is the user's terminal, command interaction
  (user input and single-line information and error messages) takes place in
  the status line (normally, a single scrolling line at the bottom of the
  screen).  Output consisting of more than one line, e.g., paging the
  command buffer, is directed to the text window.  The <span style="font-family: monospace;">"igi&gt; "</span> prompt in
  the status line indicates that 'igi' is ready to interpret a command. 
  Commands names are minimum-matched, that is, they may be abbreviated to
  the extent that the command name is unique.  Commands are
  case-insensitive, i.e., they may be typed in upper or lower case;
  however, note that cl syntax, e.g., filenames and escaped cl commands,
  is case-sensitive.  Also, single-character cursor mode keystrokes and
  IRAF native cursor mode (e.g., <span style="font-family: monospace;">":."</span>) commands are case-sensitive.
  Commands may be followed by positional arguments, separated from the
  command name and each other by white space (spaces or tabs) or a
  comma.  Extra white space at the beginning of a command line or between
  arguments is ignored.  Blank lines and commands beginning with the IRAF
  comment character <span style="font-family: monospace;">"#"</span> are ignored.   More than one command may be
  entered on a single line; if you intend to do this, then a command and
  its arguments should be separated from the next command by a <span style="font-family: monospace;">";"</span>.
  In this text, 'igi' commands are always written in upper case.  Macro
  names are represented in lower case.  Command arguments are written in
  lower case and optional arguments are enclosed in square brackets.
  Many commands belong to a family of commands.  That is they are the
  same in syntax and semantics but operate on a specific instance of some
  category.  For example, the DRAW command is really three commands:
  DRAW, DDRAW, VDRAW.  They all draw a line, but operate in different
  coordinate systems.  Another example is the COLUMN command that reads
  data into a plot buffer.  This comprises six commands:  XCOLUMN,
  YCOLUMN, ECOLUMN, PCOLUMN, LCOLUMN, and SCOLUMN, each filling a
  different plot vector buffer.  These families of commands are usually.
  represented in this text by the prefix characters shown together in
  square brackets followed by the family name, [XYEPLS]COLUMN, for
  example.
  </dd>
  </dl>
  <dl id="l_Standard">
  <dt><b>Standard Input and Standard Output</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Standard' Line='Standard Input and Standard Output' -->
  <dd>Igi uses Standard Input (STDIN) and Standard Output (STDOUT) quite
  explicitly.  Commands to be executed are read from STDIN.  Therefore, a
  command file may be redirected (using the <span style="font-family: monospace;">"&lt; filename"</span> syntax) or piped
  (using the <span style="font-family: monospace;">"task | "</span> syntax) to STDIN on the igi task command line and
  executed just as commands typed interactively.  Thus, a script or
  compiled task may be written to build and execute igi commands for
  drawing plots.
  STDOUT is used to display text containing data values, a status
  summary, or a list of executed commands, among other things.  STDOUT
  may also be redirected (using the <span style="font-family: monospace;">"&gt; filename"</span> syntax) on the task
  command line to save this displayed output.
  </dd>
  </dl>
  <dl id="l_Data">
  <dt><b>Data</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Data' Line='Data' -->
  <dd>Six vector buffers are predefined for the X and Y plot coordinates, errors,
  point style codes, upper or lower limit flags, and a scratch buffer.
  These buffers may be filled from any of several data formats:  an ASCII
  text (list) file with values arranged in columns, an ST4GEM binary
  table, a FITS table, or an IRAF image on any dimensionality.  The
  latter may be an OIF (<span style="font-family: monospace;">"old"</span> IRAF), STF (STScI or GEIS), or QPF (PROS)
  format image.
  The DATA command specifies the name of the table file to read.  Columns
  from either format are read into the buffers using the separate
  explicit commands [XYEPLS]COLUMN.  The text data to be read are
  specified  by the column number and table data are specified by column
  name.  Note that table column names are case-sensitive.  The same
  commands are used to read text and table files; the file format itself
  determines the command syntax and semantics.
  Data may be any single-precision floating point value.  Points with
  either coordinate having the value 'INDEF' will be excluded from
  autoscaling, and will not be plotted. 
  Text files used as input consist of columns of values separated by
  white space (spaces or tabs).  Rows of the input are restricted to a
  single line of the input file.  Column values need not line up row to
  row.  Any blank line or one whose first non-blank character is # is
  ignored and may be used as a comment.
  Image data are handled slightly differently.  The [XYEPLS]SECTION
  command opens an image file and reads data into one of the igi
  vectors.  Neither the DATA nor COLUMN commands are used.  An <span style="font-family: monospace;">"image
  section"</span> may specify some portion of the image to read.  In addition,
  an optional qualifier argument after the image name specifies how to
  treat multi-dimensional images.  The qualifier must be an interger.  If
  zero the image section is read as a single one-dimensional vector
  regardless of the dimensionality of the data.  If the argument is
  non-zero, its value specifies the axis on which to project the data to
  form a single vector.  If positive, igi will average the data
  perpendicular to the specified axis.  If negative, igi will sum instead
  of average.  For example:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; YSECTION myimage 2
  
  </pre></div>
  </dd>
  </dl>
  will average the columns (axis 2) in myimage to form a single vector to
  fill the Y plot buffer.
  Images of any data type may be read.  INDEF values will be ignored
  except when projecting a multi-dimensional image section.
  Data present in the plot buffers may be modified using the
  [XYEPLS]EVALUATE or [XY]LOGARITHM commands.  Note that 'INDEF' values
  operated on in this way may cause 'igi' to crash since they are not
  recognized as INDEF by the expression evaluator but treated as normal
  data values.
  </dd>
  </dl>
  <dl id="l_Image">
  <dt><b>Image Display</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Image' Line='Image Display' -->
  <dd>Some graphics devices are able to display gray-scale images and igi has
  basic image rendering (display) capabilities.  Note that these
  capabilities overlap only partially with those dealing with line
  (vector) plots.
  </dd>
  </dl>
  <dl id="l_Coordinates">
  <dt><b>Coordinates and Scaling</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Coordinates' Line='Coordinates and Scaling' -->
  <dd>Coordinates in most commands (pen position, cursor readback, etc.) are
  specified in World Coordinates or WC, also known as user coordinates.
  The area on which to plot is specified in `Normalized Device
  Coordinates' or NDC, in the range 0:1 in both the X and Y direction.  A
  `virtual page' may be specified as a subset of the physical device
  drawing area by setting the edges in NDC using the VPAGE command, or in
  physical units (inches) using the PHYSICAL command.  The `viewport',
  i.e., the axes of a plot, may fall anywhere within this page and is
  specified as a fraction of the virtual page in the range 0:1 using the
  LOCATION command.
  One additional comand, FITPIX, fixes the virtual page on the device to
  match a 2-D image input with the ZSECTION command.  The edges of the
  viewport are as specified in NDC as with VPAGE, but the actual viewport
  set may be smaller.
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  
  Coordinates      Command   Sets
  
  WC  -- PC        LIMITS    WC on viewport
  PC  -- VPC       LOCATION  Viewport on virtual page
  VPC -- NDC       VPAGE     Virtual page on device
  NDC -- Inches    PHYSICAL  Virtual page on device
  NDC -- Pixels    FITPIX    Virtual page on device
  </pre></div>
  </dd>
  </dl>
  The plot scale is determined by the user coordinates associated with
  the viewport and the size of the viewport on the page.  The LIMITS
  command.  This command associates WC (user coordinate) values with each
  edge of the viewport and thus defines the transformation between the
  user and device coordinates.  The LIMITS command may be used to
  explicitly specify the coordinate scale, or to autoscale based on the
  current X and Y plot vector data values.  In the latter case, the edges
  of the world coordinates will be at the minimum and maximum data value
  of the X and Y arrays and therefore one or more plotted data points
  will fall on an axis.
  To add a border between the plotted curve or points and the axes,
  either explicitly specify the edges of the user coordinates with the
  LIMITS command, or use the MARGIN command to automatically include an
  equal border between the edges of the data and the axes.  The default
  margin is 2.5% the width of the viewport (axis).  However, the MARGIN
  command has an optional argument to specify the border as a fraction of
  the size of the viewport.
  It is possible to use world coordinates from an input image as the X
  values that correspond to Y values input from the image.  This can be
  done with the YSECTION command if the appropriate parameters exist in
  the image header.  By default, these coordinates will not be used and
  you must supply the appropriate independent variable as the X values.
  However, if you use the IMGWCS command and the image contains the
  appropriate transformation parameters, then YSECTION will automatically
  fill in the X plot buffer with the coordinate values.
  Note that in general this works only for inherently one-dimensional
  data, e.g., spectra.  For 2-D data such as images, coordinates are
  rather meaningless for an arbitrary 1-D section of the image.  You will
  get an <span style="font-family: monospace;">"identity"</span> vector if the coordinate parameters are not present
  in the image.  That is, the X values will be the element number of the
  extracted pixels.  This is not exactly the same result as not using the
  WCS, since the coordinate transformation is applied to the image
  section.  That is, the returned coordinates are the coordinates with
  respect to the original full image, not the extracted piece.  For
  example, if you use:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; imgwcs
  igi&gt; ysection dev$pix[10,50,1]
  </pre></div>
  </dd>
  </dl>
  the range of the X values will be 10 to 50 rather than 1 to 41 if you
  do not use IMGWCS and do not otherwise fill in the X vector.  Even if
  the image does not contain a WCS transformation, YSECTION will provide
  an X vector that corresponds to the pixel numbers in the full input
  image.
  The commands requiring a plot position (move and draw) have versions for
  each of the coordinate systems:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
         WC         VPC         PC          NDC
  
  Move   RELOCATE   VRELOCATE   PRELOCATE   DRELOCATE
         MOVE       VMOVE       PMOVE       DMOVE
  
  Draw   DRAW       VDRAW       PDRAW       DDRAW
  </pre></div>
  </dd>
  </dl>
  The current X and Y (logical pen) position is maintained in user (world)
  coordinates.  Several commands change this position and others depend on
  its value.  
  </dd>
  </dl>
  <dl id="l_Axes">
  <dt><b>Axes</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Axes' Line='Axes' -->
  <dd>There are two commands that draw axes, AXIS and BOX.  AXIS is lower
  level and quite general while BOX is more convenient to use but has
  fewer options.
  BOX automatically draws four axes at the current viewport boundaries
  with the current world coordinates.  Optional arguments to the BOX
  command specify how to draw the axis labels.  There are two additional
  commands that alter the way in which the axes are drawn.  TICKSIZE
  specifies the spacing between major and minor ticks and optionally
  specifies logarithmic axes.  NOTATION specifies the range of data
  values within which tick labels will be written in exponential
  notation.
  To fill in a grid of lines between major tick marks use the GRID
  command.  It uses the current line type (see LTYPE) and width (see
  LWEIGHT).  You must use BOX before GRID to compute the tick spacing.
  BOX does not label any axis.  The XLABEL and YLABEL commands allow an
  arbitrary string to be drawn below the bottom horizontal (X) axis and
  to the left of the left vertical (Y) axis, respectively.  To draw any
  other style of axis label, use the LABEL command to draw an arbitrary
  string.  There are two string buffers maintained for the X and Y
  labels.  These are filled by the [XY]COLUMN and [XY]SECTION commands
  with the filenames used as input data.  If the argument to [XY]LABEL is
  a null string, then igi will use the label strings.  Otherwise, it will
  use the string argument.
  AXIS is a lower level command that draws an arbitrary axis.  It does
  not take into account the current viewport and world coordinates.
  Arguments to AXIS specify the position of the axis, it's range of data
  values, the format of the labels and spacing of ticks.  The current
  angle set by the ANGLE command determines the orientation of the axis.
  </dd>
  </dl>
  <dl id="l_Macros">
  <dt><b>Macros</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Macros' Line='Macros' -->
  <dd>Macro text may be defined and expanded as commands and/or arguments.
  Macros are defined with the DEFINE command whose argument is the macro
  name.  The prompt changes to <span style="font-family: monospace;">"macro&gt; "</span>, indicating that subsequent text
  is not interpreted, but saved as macro text.  Macro define mode is
  terminated by typing END at the prompt.  
  Arguments to macros are defined by the <span style="font-family: monospace;">"&amp;"</span> character followed by an
  integer appearing in the macro text.  The argument number specifies the
  position of the replacement argument value when the macro is invoked. 
  The maximum argument value specifies the number of arguments to the
  macro. 
  A macro is invoked using its name, followed by the values to replace its
  positional arguments, if any.  A macro may invoke any 'igi' command or
  other defined macros, but may not invoke itself (i.e., no recursion).
  BYE is not equivalent to END for terminating a macro.  Therefore, BYE
  does not terminate macro define mode, will be stored as part of the
  macro text, and will be expanded into the command stream when the macro
  is invoked. 
  The following example defines and invokes a macro named <span style="font-family: monospace;">"simple"</span> to
  scale and draw a plot:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; define simple
  macro&gt; data &amp;1
  macro&gt; xcolumn &amp;2; ycolumn &amp;3
  macro&gt; limits; box; connect
  macro&gt; end
  igi&gt; simple igi.dat 1 2
  igi&gt; erase
  igi&gt; simple igi.dat 3 4
  </pre></div>
  </dd>
  </dl>
  The size of a macro is limited by the size of the <span style="font-family: monospace;">"pushback"</span> buffer
  used to expand macros before execution.  The IRAF system default for
  the pushback buffer allows only for 512 characters.  For igi, the size
  can be modified using the cl environmental variable <span style="font-family: monospace;">"igi_buflen"</span>.  One
  can use the command
  <div class="highlight-default-notranslate"><pre>
  set igi_buflen = XXXXX
  </pre></div>
  where XXXXX is the number of characters to allow in the pushback
  buffer. This comman can be executed either at the cl prompt, or within
  the login.cl or loginuser.cl file.
  An indication that the buffer size may need to be increased is when
  the error:
  <div class="highlight-default-notranslate"><pre>
  ERROR: Pushback buffer overflow (recursive macro?) (STDIN)
  </pre></div>
  occurs.
  </dd>
  </dl>
  <dl id="l_Command">
  <dt><b>Command Buffer</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Command' Line='Command Buffer' -->
  <dd>Many commands are saved in the `command buffer'.  The commands in the
  buffer may be listed and edited.  The commands may be replayed.
  Commands may be read into the command buffer from a file, commands may
  be executed directly from a file, or the contents of the buffer may be
  written to a file.  The command buffer may be edited during an 'igi'
  session and the edited buffer played back.
  Commands are stored in their full, unabbreviated extent, capitalized,
  one command per line, regardless of how they were typed or read from a
  command file.  String arguments (to LABEL, for example) are delimited
  by double quotes.
  The command memory mechanism operates differently for separate classes
  of commands.  In general, commands dealing with data I/O, data
  manipulation, plot parameters, and drawing commands are saved while
  those dealing with commands themselves are not.
  [XYEPLS]COLUMN, DATA, [XYEPLS]EVALUATE, LINES, and [XY]LOGARITHM are
  stored in the command buffer.  All of the graphics output commands:
  AXIS, BOX, CONNECT, DOT, [DPV]DRAW, ELLIPSE, ERRORBAR, HISTOGRAM, ID,
  LABEL, POINTS, POLYGON, PUTLABEL, STEP, and ULLIM are saved in the command
  buffer.  Parameter (plot attribute) manipulation commands:  ANGLE,
  EXPAND, [XY]FLIP, ID, JUSTIFY, [XY]LABEL, LIMITS, LOCATION, LWEIGHT,
  NOTATION, [DPV]RELOCATE, RESET, [XY]SIXTY TICKSIZE, TITLE, [ELP]TYPE,
  and VPAGE are saved in the plot command buffer.
  Command buffer manipulation commands:  EDITCMD, LIST, PAGECMD, PLAYBACK,
  READ, and WRITE are not saved, except INPUT.  The remaining
  miscellaneous commands:  !, ?, ^, APROPOS, CURSES, DLIST, END, ERASE,
  HELP, MACROS, MINMAX, SHOW, and UNDO are not saved in the command
  buffer. 
  In cursor mode, a RELOCATE (MOVE) command is stored for each cursor
  position read, and commands are saved in the command buffer when
  entered in <span style="font-family: monospace;">":"</span> mode.  Macro invokations rather than the expanded text
  are stored in the command buffer.
  The last command resulting in plotted vectors remains in a single line 
  command buffer.  The UNDO command uses this buffer to erase the result 
  of this instruction on devices supporting vector erase.
  </dd>
  </dl>
  <dl id="l_Cursor">
  <dt><b>Cursor Interaction</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Cursor' Line='Cursor Interaction' -->
  <dd>All of the existing capabilities of the IRAF/GIO graphics cursor for
  manipulating the `graphics buffer' are available within 'igi'.  IRAF/GIO
  cursor interaction may be initiated with the 'igi' command CURSES.  It
  recognizes a number of keystrokes and commands with a broad range of
  capabilities to manipulate the existing plot, including zoom, roam,
  reading and writing binary plot metacode files, generating hard copies,
  etc.  
  After a plot has been produced, the graphics metacode commands remain
  in the IRAF graphics buffer after igi terminates until it is
  explicitily erased with gflush or graphics are opened again.  Cursor
  interaction is still available from the cl to interact with the plot
  using <span style="font-family: monospace;">"=gcur"</span>, in order to obtain hard copies using the <span style="font-family: monospace;">":.snap"</span> cursor
  command, for example.
  In addition to the IRAF/GIO cursor capability, all 'igi' commands are
  available in cursor mode using the colon command capability.  Upon
  typing <span style="font-family: monospace;">":"</span> when the graphics cursor is displayed, the terminal returns
  to text mode with the <span style="font-family: monospace;">":"</span> displayed as a prompt.  At this prompt, any
  valid 'igi' command may be typed.  All of the logical pen movement
  commands (RELOCATE, DRAW, etc.) will use the current cursor position
  regardless of the coordinate system or any arguments input on the
  command, therefore, these coordinate arguments should be ommitted. 
  </section>
  <section id="s_new_features">
  <h3>New features</h3>
  <dl>
  <dt><b>Version Dec 1999</b></dt>
  <!-- Sec='NEW FEATURES' Level=1 Label='Version' Line='Version Dec 1999' -->
  <dd>A new command was created for use by IGI.  The new command, PSCMD, 
  allows a user to insert complete Postscript command strings directly
  into the PostScript output.  The PSCMD command can support any PostScript 
  command, but the PDFMARK commands provide a way to insert Acrobat PDF 
  functions into a PostScript document.  The PDFMARK functions are completely
  transparent to the PostScript (due to an enhanced PostScript prolog in 
  'psikern') but are activated upon conversion from PostScript to PDF format.
  This allows the user to insert bookmarks, links, and other PDF functions
  into a document during initial generation by IGI.  The user, however, must 
  take all responsibility for syntax and usage rules for the commands 
  inserted into the PostScript.
  In addition, the PSFNT and PSCMD commands were revised to only create
  output when the output device uses the 'psikern' kernel.  This avoids
  problems with these commands outputting the strings to a device which
  won't understand them, such as 'stdgraph'.  Thus, the effects of these
  commands are isolated to PostScript devices, and only those PostScript
  devices supported in the graphcap by the 'psikern' kernel.  
  </dd>
  </dl>
  <dl>
  <dt><b>Version May 1997</b></dt>
  <!-- Sec='NEW FEATURES' Level=1 Label='Version' Line='Version May 1997' -->
  <dd>A couple of new capabilities were added to IGI in this version, one for
  working with which have arrays as elements of its
  columns, the other providing greater freedom in the use of PostScript
  fonts.
  The DATA and COLUMN commands were modified to accept arguments for
  working with tables that have arrays contained in table cells.  Row
  selectors can now be added to a filename in the DATA command to
  specifiy which row of the column the array should be pulled from for
  plotting.  Alternatively, a row number can be given as the second
  argument of the COLUMN command to specify which row of the named column
  should be used for plotting.  The two features can also be used in
  conjunction, with a range of rows being specified in the DATA commands
  row selector and the row number in the COLUMN command selecting the row
  from that range to be used.  This allows one range of rows to be read
  in using the DATA command while the COLUMN command is used to step
  through that range of rows.
  Labels in IGI plots can now use more than the usual Times-Roman or
  Symbol font when using the GIO (or HARD) fonts.  A new command, PSFONT,
  has been created to allow a user to specify a new PostScript font to
  use in a label.  
  This font is then used when a new GIO escape sequence, <span style="font-family: monospace;">"<span style="font-family: monospace;">", is seen in 
  in the label text.  Each time the PSFONT command is called, it resets what
  font will be used with the "</span><span style="font-family: monospace;">" command in the text, but the PSFONT command
  can be called as many times in an IGI script as desired.  The only limitations
  of this command is that it only affects labels printed out after setting
  FONTSET to "</span>hard<span style="font-family: monospace;">", only one new font can be used at a time, and only those
  fonts supported by the printer can be used.  
  </dd>
  </dl>
  <dl>
  <dt><b>Version May 1994</b></dt>
  <!-- Sec='NEW FEATURES' Level=1 Label='Version' Line='Version May 1994' -->
  <dd>The command POLYGON has been added to draw arbitrary closed, filled
  polygons.
  </dd>
  </dl>
  <dl>
  <dt><b>Version 3.6  July 1993</b></dt>
  <!-- Sec='NEW FEATURES' Level=1 Label='Version' Line='Version 3.6  July 1993' -->
  <dd>Added the WCSLAB command to provide WCS coordinate labeling identical
  to the stplot.wcslab task.  Optionally, the command may permit editing
  the extensive wlpars parameter set for specifying attributes via
  eparam.  If the ZSECTION command was used to read an image section into
  the Z buffer, then the WCS attributes of that image are used in
  labeling the plot.  Otherwise, the WCS is taken from parameters in the
  wcspars pset.  Note that the psets may be edited before entering igi by
  explicitly assigning parameter values or by using eparam at the cl
  prompt.  In addition, parameter values may be assigned or the psets
  edited from igi using the "</span>!<span style="font-family: monospace;">" escape before using the WCSLAB command.
  Added the VERSION command to show the current version and the date of
  its installation.  This is intended to help in determining the state of
  implementation of features and bug-fixes.  Modified the initial prompt,
  the listing from the SHOW command, and the result of the ID command
  also to show the current version and installation date.
  Modified SAOCMAP to correct a bug which certain colormaps cause igi to
  fail with memory corrupted (crashing the cl as well).  This is an old
  problem that was corrected in playpen.scmapc but not igi.  The code for
  inttab(), the guts of the colormap code, now matches between the tasks,
  except that in scmapc it uses floating point output colormap and igi
  uses shorts.
  </dd>
  </dl>
  <dl>
  <dt><b>Version 3.5.3  April 1993</b></dt>
  <!-- Sec='NEW FEATURES' Level=1 Label='Version' Line='Version 3.5.3  April 1993' -->
  <dd>Modified STEP to correct a bug preventing drawing the curve when one or
  both axes are reversed using the [XY]FLIP command.
  Installed a modified version of SECTION provided by Frank Valdes (NOAO)
  to implement recognition of multispec format images (spectra) with
  IMGWCS enabled.
  </dd>
  </dl>
  <dl>
  <dt><b>Version 3.5.2, March 1993</b></dt>
  <!-- Sec='NEW FEATURES' Level=1 Label='Version' Line='Version 3.5.2, March 1993' -->
  <dd>Modified DLIST to permit writing the plot buffer values to a file
  instead of STDOUT.  An optional argument now specifies the output text
  file.
  Modified LINES to permit resetting the range to the default, using all
  of the input table rows.  An optional argument value of zero returns
  one or both limits to the default.
  Fixed a bug in BARGRAPH (HISTOGRAM) resulting in incorrect plots with
  both X and Y data.
  Changed all explicit INDEF test to use IS_INDEF macros.
  Chanced dummy array declarations to use ARB.
  </dd>
  </dl>
  <dl>
  <dt><b>Version 3.5.1, October 1992</b></dt>
  <!-- Sec='NEW FEATURES' Level=1 Label='Version' Line='Version 3.5.1, October 1992' -->
  <dd>Removed dependence on ST4GEM so the Tables version links and executes
  independently.
  Modified FILLPAT to print the current pattern style if there's no
  argument.
  </dd>
  </dl>
  <dl>
  <dt><b>Version 3.5, September 1992</b></dt>
  <!-- Sec='NEW FEATURES' Level=1 Label='Version' Line='Version 3.5, September 1992' -->
  <dd>Implemented the FILLPAT command to specify a fill pattern style.  The
  argument is an index corresponding to the gio pattern index.  The
  plotted pattern is kernel- and device-dependent and implemented only in
  psikern.
  Added the BARGRAPH command as an alias (preferred) for HISTOGRAM, whose
  name is confusing since it doesn't compute a histogram from data.
  Modified BARGRAPH, HISTOGRAM, DOT, and POINTS to implement filled
  areas.  The current fill pattern as specified by the FILLPAT command
  will be used if the symbol style (set with PTYPE) is "</span>open<span style="font-family: monospace;">" or
  "</span>starred<span style="font-family: monospace;">".  The former result is achieved as long as the fill pattern
  is 1 (outline, the default).
  Implemented the SAOCMAP command to read a colormap as written by
  SAOimage and apply this to the image rendered by PIXMAP.  By default,
  it will scale the entire SAOimage color map to the full output map.
  There is an option force the appropriate elements of the color map to
  match the "</span>graphics<span style="font-family: monospace;">" colors as defined in the servers.  This permits
  rendering an image as dumped directly from a server's display raster
  buffer (using playpen.dstoim, for example).
  </dd>
  </dl>
  <dl>
  <dt><b>Version 3.4.1, August 1992</b></dt>
  <!-- Sec='NEW FEATURES' Level=1 Label='Version' Line='Version 3.4.1, August 1992' -->
  <dd>Fixed a problem with the text justification for gio (hardware) fonts.
  There is a fundamental discrepency in the definition of justification
  between igi and gio.  The gio convention is to specify the
  justification relative to the horizontally aligned bounding box
  surrounding the text, not the string itself.  The fix involves a matrix
  which maps the justification index to one which will render the text
  with the closest applicable justification by gio.  The modified scheme
  should work properly for "</span>cardinal<span style="font-family: monospace;">" angles but not as well for many
  combinations of angle and justification.
  </dd>
  </dl>
  <dl>
  <dt><b>Version 3.4, July 1992</b></dt>
  <!-- Sec='NEW FEATURES' Level=1 Label='Version' Line='Version 3.4, July 1992' -->
  <dd>Implemented the ZSECTION and PIXMAP to read and plot 2-D image
  sections.  This currently really works only with the PostScript kernel,
  psikern (of course).  Added FITPIX to specify a viewport that matches on
  the device the aspect ratio of the pixmap raseter.  Added ZRANGE to
  specify the minimum and maximum pixel value to map to the display
  range.
  The default behavior is an attempt at an analogy with the 1-D case.
  That is, ZSECTION fills the Z buffer with the image section.  LIMITS
  should be used to set the WCS.  Margin may be used to reset the WCS to
  create a margin between the viewport (axes) and the edge of the image.
  FITPIX may be used to specify a viewport that fits the raster.
  Otherwise, the pixmap will fill the viewport.  ZRANGE should be used to
  specify the range of pixel values to map to the range of display
  values.  With no argument, ZRANGE permits autoscaling on the input data.
  Added the "</span>viewport<span style="font-family: monospace;">" commands PDRAW, PMOVE, and PRELOCATE, identical to
  DRAW, MOVE, and RELOCATE except the coordinates are expected to be in
  "</span>viewport coordinates<span style="font-family: monospace;">" (PC).  These are in the range 0:1, relative to
  the edges of the axes.  That is, the same as WC, except always in the
  range 0:1.  The same results may be obtained by explicitly using
  "</span>LIMITS 0 1 0 1<span style="font-family: monospace;">" except of course, these commands avoid that.
  Implemented ZEVALUATE to permit arithmetic operations on the Z buffer.
  Note that there is some ambiguity in dealing with inherently 2-D Z
  data.
  Implement the FILLPAT command to specify the fill pattern for hollow
  symbols and bar charts (HISTOGRAM).  This is kernel-dependent.  Only
  psikern supports it currently, of course.
  Modified HISTOGRAM to accept an argument specifying the relative width
  of the bars.  Simplified the code in the equally-spaced case.  Added
  the BARGRAPH command as an alias for HISTOGRAM.
  Modified LOCATION to permit specifying a square (unity aspect)
  viewport, regardless of the shape of the device or virtual page.  This
  is analagous to the action of FITPIX, signalled with a first argument
  of INDEF.  Modified ig_scale() and ii_location() in ig_scale.x.
  </dd>
  </dl>
  <br>
  <br>
  <dl>
  <dt><b>Version 3.3, June 1992</b></dt>
  <!-- Sec='NEW FEATURES' Level=1 Label='Version' Line='Version 3.3, June 1992' -->
  <dd>Add the FONTSET command to select igi or gio font sets.  The latter
  permits using real PostScript fonts with the PostScript graphics
  kernel, psikern.  Note that the text "</span>escapes<span style="font-family: monospace;">" for doing things like
  changing fonts, super/sub-scripts, etc. are different between the font
  sets.
  Add the `initcmd' task parameter to permit startup with igi commands.
  Among other things, this permits a user to use a constant command file
  but with some variation with each execution, specifying a new data
  file, for example.
  Modified code that pages listings on STDOUT, such as DLIST and SHOW to
  display text without paging if STDOUT is redirected.  This permits
  running igi in "</span>batch<span style="font-family: monospace;">" but using these commands without annoying page
  prompts.
  </dd>
  </dl>
  <br>
  <br>
  <dl>
  <dt><b>Version 3.2, May 1992</b></dt>
  <!-- Sec='NEW FEATURES' Level=1 Label='Version' Line='Version 3.2, May 1992' -->
  <dd>Fixed a bug causing some tick labels to include an extra zero between
  the ones place and decimal point.
  Fixed the NOTATION command, which did not have any effect.  It is now
  possible to change the data range outside which tick labels are plotted
  as exponential.
  Added the NUMBER command to draw the element number at each data
  point.
  Fixed extra line drawn by GRID.
  Added the COLOR command to specify the color index for all subseqeuent
  drawing.  The color index is an integer specifying the device-dependent
  (kernel) color that is rendered.  Currently, only the PostScript
  graphics kernel (psikern) supports color.
  </dd>
  </dl>
  <br>
  <br>
  <dl>
  <dt><b>Version 3.1, November 1991</b></dt>
  <!-- Sec='NEW FEATURES' Level=1 Label='Version' Line='Version 3.1, November 1991' -->
  <dd>Changed the font file to be machine independent binary using mii to
  read it.  There is no longer need for the ASCII font file or anything
  to be done at installation.  The single font file is now
  stplot$miifont.dat.
  Modified the STEP command to draw the vertical connecting lines between
  points even if adjacent points fall outside the viewport.
  Fixed a bug preventing macros invoked in upper case from being
  recognized.
  Fixed axis tick labels that were incorrectly placed when perpendicular
  to the axis.
  Cosmetic changes to SHOW output.
  Fixed a bug in the command parser that showed up in the DEC/Ultrix
  Fortran compiler (and apparently nowhere else) causing no commands to
  be recognized.
  Changed the way help text is paged.  Instead of using the spawned cl
  command directly, we now redirect the help text from the cl command to
  a temporary text file, page the file, then delete it.
  </dd>
  </dl>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>(initcmd = "</span><span style="font-family: monospace;">") [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='(initcmd = "") [string]' -->
  <dd>An igi command string executed upon startup.  This may be any valid igi
  command including command separators ("</span>;<span style="font-family: monospace;">") to execute multiple
  commands.  This may be useful to specify a different input data file
  for multiple executions but use a constant input file otherwise, for
  example.
  </dd>
  </dl>
  <dl>
  <dt><b>(wlpars = "</span><span style="font-family: monospace;">") [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='(wlpars = "") [pset]' -->
  <dd>Parameter set (pset) for modifying the plot and labels produced by the
  WCSLAB command.  These parameters are described in the help file for
  'wlpars' (i.e., type "</span>help wlpars<span style="font-family: monospace;">").
  </dd>
  </dl>
  <dl>
  <dt><b>(usewcs = no) [bool]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='(usewcs = no) [bool]' -->
  <dd>Use the information in the 'wcspars' pset for the world coordinate
  information.  If 'no', the information will come from the image read in
  by the 'zsection' command.
  </dd>
  </dl>
  <dl>
  <dt><b>(wcspars = "</span><span style="font-family: monospace;">") [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='(wcspars = "") [pset]' -->
  <dd>Parameter set (pset) for specifying a WCS for the WCSLAB command.  This is used to specify a different WCS from an image read by ZSECTION.  Type "</span>help
  wcspars<span style="font-family: monospace;">" for more information.
  </dd>
  </dl>
  <dl>
  <dt><b>(device = "</span>stdgraph<span style="font-family: monospace;">") [device name]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='(device = "stdgraph") [device name]' -->
  <dd>The output graphics device.  If device = "</span>file<span style="font-family: monospace;">", the graphics output is
  stored in the file specified by the parameter `metacode'. 
  </dd>
  </dl>
  <dl>
  <dt><b>(metacode = "</span><span style="font-family: monospace;">") [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='(metacode = "") [file name]' -->
  <dd>The name of an output binary GKI metacode file.  This is required if 
  device = "</span>file<span style="font-family: monospace;">".
  </dd>
  </dl>
  <dl>
  <dt><b>(append = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='(append = no) [boolean]' -->
  <dd>Append to existing graphics?  This may be used to run igi several times
  but plot to the same frame (page) or combine igi graphics with plots
  from other IRAF/ST4GEM tasks.  Use the ERASE task to create a new
  frame, even with append=yes.
  If appending graphics to a metacode file you must also use "</span>&gt;&gt;G file<span style="font-family: monospace;">"
  rather than "</span>device=file<span style="font-family: monospace;">".  Using "</span>append=yes<span style="font-family: monospace;">" also permits creating a
  single file if you are creating a PostScript output file.  If you also
  wish to create a new page but use a single file, use the ERASE
  command.  This will not actually erase existing graphics from any
  non-interactive (hard copy) graphics output.
  </dd>
  </dl>
  <dl>
  <dt><b>(debug = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='(debug = no) [boolean]' -->
  <dd>Echo commands and list additional internal information.
  </dd>
  </dl>
  <dl>
  <dt><b>(cursor = "</span><span style="font-family: monospace;">") [graphics cursor]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='(cursor = "") [graphics cursor]' -->
  <dd>Graphics cursor.
  </dd>
  </dl>
  </section>
  <section id="s_menu">
  <h3>Menu</h3>
  <div class="highlight-default-notranslate"><pre>
  !               Escape a command to the cl
  !cl             Spawn a cl process (bye ==&gt; return to igi)
  !!              Escape a command to the host
  !!!             Spawn a host (VMS) process (logout ==&gt; return to igi)
  ?               Page the help summary
  ^               Re-execute a previous command
  ANGLE           Set the marker and text rotation angle
  APROPOS         List commands associated with a keyword
  AXIS            Draw and label an arbitrary axis
  BARGRAPH        Draw a bar graph (histogram-style plot)
  BOX             Draw and label the axes
  BYE             Terminate igi (alias for END)
  COLOR           Set (hardware-dependent) color index
  CONNECT         Draw a (polyline) curve connecting the data coordinates
  CURSES          Read back cursor position (IRAF cursor mode)
  DATA            Specify the input text data file
  DDRAW           Pen down move (draw) in NDC
  DLIST           Print the data values
  DMOVE           Pen up move in NDC (alias for DRELOCATE)
  DOT             Draw a single marker
  DRAW            Pen down move (draw) in WC
  DRELOCATE       Pen up move in NDC
  ECOLUMN         Read errors from a column of the text data file
  EDITCMD         Edit the command buffer or macro text
  EEVALUATE       Operate on error values
  ELLIPSE         Draw an ellipse
  END             Exit igi or terminate macro define (end the current mode)
  ERASE           Erase the screen
  ERRORBAR        Draw error bars
  ETYPE           Change the error bar style
  EXPAND          Set the marker and text size
  FILLPAT         Specify the fill pattern for hollow symbols and bar graphs
  FITPIX          Specify a viewport to match shape of image raster
  FMTICK          Specify the axis tick label format
  FONTSET         Select igi or gio font set
  GRID            Draw lines between major axis ticks
  HELP            Print help
  HISTOGRAM       Draw a histogram-style plot (bar graph)
  ID              Write identification label
  IMGWCS          Toggle using image WCS for X values
  INPUT           Execute commands from a file
  JUSTIFY         Set text justification
  LABEL           Draw text at current position
  LIMITS          Set the plot scale
  LINES           Specify the range of input rows to read
  LIST            List the command buffer or macro text
  LOCATION        Set the viewport on the virtual page
  LTYPE           Set the line style (hardware dependent)
  LWEIGHT         Set the line width (hardware dependent)
  MACROS          List defined macros
  MARGIN          Rescale to include a border between curve and axes
  MENU            Page the help summary
  MINMAX          Print the data range
  MOVE            Pen up move in WC (alias for RELOCATE)
  NOTATION        Set the format for axis labels
  NUMBER          Write the element number at each data coordinate
  PAGECMD         Page the command buffer or macro text
  PCOLUMN         Read point specifications from the input data file
  PDRAW           Pen down move (draw) in viewport coordinates (PC)
  PEVALUATE       Operate on point code values
  PHYSICAL        Set the virtual page in physical device coordinates
  PIXMAP          Render (display) a pixmap raster image
  PLAYBACK        Execute the commands in the command buffer
  PMOVE           Pen up move in PC (alias for PRELOCATE)
  POINTS          Draw a polymarker at input data coordinates
  POLYGON         Draw a closed polygon using the data coordinates
  PRELOCATE       Pen up move in PC (alias for PMOVE)
  PSCMD       Insert a user-specified PostScript command into the PostScript file
  PSFONT          Specify a user-defined PostScript font
  PTYPE           Specify the point marker type
  PUTLABEL        Draw a label with a specified justification
  READ            Read commands into the command buffer without execution
  RELOCATE        Pen up move in WC
  RESET           Return settable plot and data parameters to defaults
  SAOCMAP         Apply a colormap in SAOimage format to a rendered image
  SECTION         Read an image section for a plot buffer
  SHOW            Page the plot limits and attributes
  STEP            Draw a stepped curve (histogram without vertical lines)
  TICKSIZE        Set the axis tick spacing
  TITLE           Specify the plot title
  ULLIM           Draw upper or lower limit symbols
  UNDO            Selectively erase the last plot command
  VDRAW           Pen down move (draw) in VPC
  VERSION         Show igi version and date
  VMOVE           Pen up move in VPC (alias for VRELOCATE)
  VPAGE           Set the virtual page in normalized coordinates
  VRELOCATE       Pen up move in VPC
  WCSLAB          Label the viewport in WCS coordinates
  WINDOW          Divide screen into panes
  WRITE           Write the command buffer to a file
  XCOLUMN         Read X coordinates from a column of the data file
  XEVALUATE       Operate on X data values
  XFLIP           Flip X axis
  XLABEL          Specify the X axis label
  XLOGARITHM      Take common log of X data
  XSECTION        Read X coordinates from an image section
  YCOLUMN         Read Y coordinates from a column of the data file
  YEVALUATE       Operate on Y data values
  YFLIP           Flip Y axis
  YLABEL          Specify the Y axis label
  YLOGARITHM      Take common log of Y data
  YSECTION        Read Y coordinates from an image section
  ZEVALUATE       Operate on Z data values
  ZRANGE          Specify range of pixel values to map to display range
  ZSECTION        Read image section as a pixmap raster
  </pre></div>
  </section>
  <section id="s__">
  <h3>!</h3>
  Arguments:  !text
  Escape a command to the cl.  Input text following the "</span>!<span style="font-family: monospace;">" is passed to
  the cl for interpretation.  The cl environment at the time igi was
  invoked is in effect.  For example:  !dir executes the IRAF directory
  command to list the files in the current directory using the IRAF
  virtual file names.  Note that cl commands are case sensitive.
  The command !cl starts a new cl process complete with the cl prompt and
  with the same environment as when igi started.  To terminate this
  process and return to igi, type bye at the cl prompt.
  Any text preceeded by "</span>!!<span style="font-family: monospace;">" is executed as a host (e.g., VMS, UNIX,
  etc.) command.  The first "</span>!<span style="font-family: monospace;">" escapes the command to the cl, and since
  the remaining text starts with another "</span>!<span style="font-family: monospace;">", this escapes the command to
  the host.  Any valid host command will be interpreted.  The environment
  at the time the cl and igi were invoked is in effect.  For example, the
  command !!dir on VMS (!!ls on UNIX) will list the current default
  directory using the host file names.
  The command !!! on VMS or !!csh on Unix starts a new host process.  To
  terminate this process and return to igi, type "</span>logout<span style="font-family: monospace;">" on VMS and "</span>exit<span style="font-family: monospace;">"
  on Unix.
  </section>
  <section id="s__">
  <h3>?</h3>
  no arguments
  Page the help summary.  Only a list of the commands and their
  meaning is listed.  To get this extended text, use the HELP command.
  </section>
  <section id="s__">
  <h3>^</h3>
  Arguments:  ^[n]
  Execute a previous command.  If no argument follows the character, 
  execute the last command.  The optional argument must be an integer, and 
  if present specifies the sequence number of the command in the command 
  buffer to execute.  See LIST, EDITCMD, and PAGECMD
  </section>
  <section id="s_angle_">
  <h3>Angle </h3>
  Arguments:  ANGLE [ang]
  The orientation for markers and text is specified by the floating point
  parameter in degrees counterclockwise from the horizontal (positive X
  axis).  If no parameter is specified, the value of the currently set
  angle will be listed.
  This command is saved in the command buffer.
  </section>
  <section id="s_apropos">
  <h3>Apropos</h3>
  Arguments:  APROPOS keyword
  List a brief description of the commands associated with the specified 
  keyword.  For example, APROPOS move results in:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='APROPOS' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  DDRAW       Pen down move (draw) in NDC
  DMOVE       Pen up move in NDC (alias for DRELOCATE)
  DRAW        Pen down move (draw) in WC
  DRELOCATE   Pen up move in NDC
  MOVE        Pen up move (alias for RELOCATE)
  RELOCATE    Pen up move in WC
  VDRAW       Pen down move (draw) in VPC
  VMOVE       Pen up move in VPC (alias for VRELOCATE)
  VRELOCATE   Pen up move in VPC
  </pre></div>
  </dd>
  </dl>
  See ? for the command summary and HELP for the full help text.
  </section>
  <section id="s_axis">
  <h3>Axis</h3>
  Arguments:  AXIS w1 w2 minor major x y len label clock
  <dl>
  <dt><b></b></dt>
  <!-- Sec='AXIS' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  w1    -- WC at beginning of axis
  w2    -- WC at end of axis
  minor -- Spacing of minor ticks;  &lt; 0 =&gt; logaritmic
  major -- Spacing of major ticks
  x, y  -- Position of axis (at w1) in VPC
  len   -- Size of axis in VPC
  label -- 0 =&gt; No tick labels
           1 =&gt; Tick labels parallel to axis
           2 =&gt; Tick labels perpendicular to axis
  clock -- 0 =&gt; Ticks and labels counterclockwise
           1 =&gt; Ticks and labels clockwise
  </pre></div>
  </dd>
  </dl>
  Draw an arbitrary axis scaled from w1 to w2 in data coordinates (WCS)
  starting at (x,y) and length len in virtual page coordinates (VPC).  If
  major &gt; 0, use that for the spacing of major ticks.  If minor &lt; 0, draw
  a logarithmic axis;  if minor &gt; 0, try to use that for the spacing of
  minor ticks;  if minor = 0, let igi decide where to put minor ticks.  If
  label = 0, don't draw labels;  if label = 1, draw labels parallel to the
  axis;  if label = 2, draw labels perpendicular to the axis.  If clock =
  1 draw ticks clockwise with respect to the axis, counterclockwise if
  clock = 0.
  The current angle specifies the position angle of the axis with respect
  to horizontal (see ANGLE).  The current tick label format specifies how
  the tick labels will be written (see FMTICK).  The current line width
  specifies how the axis will be drawn (see LWEIGHT).
  See BOX for drawing default axes at the current plot scale.
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_bargraph">
  <h3>Bargraph</h3>
  Arguments:  BARGRAPH width
  Draw a bar graph (histogram-style plot) using the current X and Y
  data.  If no X data exist, the horizontal axis will be scaled on the
  pixel numbers.  This is an alias for the HISTOGRAM command.
  The optional argument specifies the relative width of the bars.  If no
  argument is used or the value is INDEF, the bars fill the available
  space.  For equally spaced data (equally-spaced or no X values), all of
  the bars are as wide as the difference in X between adjacent points.
  For unequally spaced data, the edges of the bars fall halfway between
  adjacent points.  The "</span>width<span style="font-family: monospace;">" argument is a constant factor to apply to
  this width.  For example, "</span>BARGRAPH 0.5<span style="font-family: monospace;">" will draw bars half the
  natural width, leaving an equal space between bars.  It is not possible
  to apply a different factor to each bar separately, except by
  specifying the X data explicitly.
  Bars may be drawn with a fill pattern, specified using the FILLPAT
  command.  Note that the nature of the fill patterns depends on the
  device and kernel used.  See LTYPE and LWEIGHT for specifying the style
  of the curve to draw.  See CONNECT, STEP, POLYGON, and POINTS for different
  curve styles
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_box">
  <h3>Box</h3>
  Arguments:  BOX [xlabel[ ylabel]]
  Draw and label the axes using the current page, viewport, and window
  transformations and any axis label or title specified.  The optional label 
  arguments specify the X and Y tick labels:  0 ==&gt; no labels;  1 ==&gt; 
  labels parallel to the axis;  2 ==&gt; labels perpendicular to the axis.  
  The default is xlabel = 1, ylabel = 2.
  See AXIS for drawing a single arbitrary axis.  See [XY]LABEL for
  annotating the axes with a text label.  See LIMITS for setting the plot
  scale.  See MARGIN for adjusting the scale to include a border between
  curves and axes.
  The current tick label format specifies how the tick labels will be
  written (see FMTICK).  The current line width specifies how the axis
  will be drawn (see LWEIGHT).
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_bye">
  <h3>Bye</h3>
  no arguments
  Terminate igi.  This is an alias for END, except in macro define mode 
  (see DEFINE).
  </section>
  <section id="s_color">
  <h3>Color</h3>
  Arguments:  COLOR index
  Set the color index for all subsequent drawing.  The argument, the
  color index, is a positive integer.  All drawing operations -- lines,
  text, symbols, curves, axes -- will be rendered in the selected color.
  The default color index is 1, rendered as black (or the foreground
  color) on most devices.  The rendered color depends on the device used
  and whether the IRAF kernel supports it.  (Currently, only the psikern
  IRAF kernel supports color for use with color PostScript devices.)
  </section>
  <section id="s_column">
  <h3>Column</h3>
  Arguments:  [XYEPLS]COLUMN column [row number]
  Read a column of data from the file specified by the DATA command.  The
  command prefix indicates which data buffer to fill:  x coordinates, y
  coordinates, errors, point marker styles, limits, or scratch.  If the
  input data is a text (ASCII list) file, 'column' must be an integer
  specifying the column number.  If it is an ST4GEM or FITS table,
  'column' must be a string specifying the column name.  Note that table
  column names are case-sensitive and may not be abbreviated.
  The second argument, row number, provides the ability to plot from
  tables where each element of a column is an array itself.  The row
  number specifies which cell of the column you want to plot out.  Arrays
  from these tables can be plotted by specifying a row selector as
  an extension to the input file (table) name in the DATA command.
  See DATA to specify the input file (table) name.  See [XYEPLS]SECTION
  to read an IRAF image into a buffer.
  This command is saved in the command buffer.
  </section>
  <section id="s_connect">
  <h3>Connect</h3>
  no arguments
  Draw a (polyline) curve in the current line style (see LTYPE) connecting
  the data coordinates.  See POINTS for drawing markers without
  connection.  The current pen position is left on the last point.
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_curses_">
  <h3>Curses </h3>
  Arguments:  CURSES [file]
  Start cursor mode and read back the cursor position.  If the argument
  `file' exists, it is the name of a file to which are written the
  coordinates of positions selected with the cursor.  If no argument
  exists, the positions are written only to STDOUT (the terminal);  the
  coordinates are not saved in a file.  To terminate cursor mode, type "</span>q<span style="font-family: monospace;">"
  or "</span>e<span style="font-family: monospace;">" (lower case!).  Any other lower case character will list the
  cursor position and redisplay the cursor.  Upper case and special
  characters are recognized by IRAF cursor mode.  
  This command invokes the IRAF/GIO cursor facility (see !help cursor). 
  In addition to the IRAF/GIO cursor capability, all igi commands are
  available in cursor mode using the colon command capability.  Upon
  typing "</span>:<span style="font-family: monospace;">" when the graphics cursor is displayed, the terminal returns
  to text mode with the "</span>:<span style="font-family: monospace;">" displayed as a prompt.  At this prompt, any
  valid igi command may be typed.  Commands expecting input coordinates
  ([DPV]RELOCATE and [DPV]DRAW) will use the current cursor position
  regardless of any arguments input on the command, therefore, these
  coordinates may be ommitted. 
  The CURSES command is not stored in the command buffer, but a RELOCATE
  command with the last cursor position is stored on each cursor read or 
  "</span>:<span style="font-family: monospace;">" command.  Therefore, on PLAYBACK, no cursor interaction takes place
  but any commands relying on the interactively specified cursor position
  execute appropriately. 
  Type "</span>!help cursor<span style="font-family: monospace;">" from igi ("</span>help cursor<span style="font-family: monospace;">" from the cl) for help on the
  IRAF cursor facility. 
  </section>
  <section id="s_data_">
  <h3>Data </h3>
  Arguments:  DATA [filename]
  Specify the input data file.  This file may be either an ASCII list
  (text) file whose contents are numerical values arranged in columns, an
  ST4GEM table, or a FITS table.  If no file name is specified, the
  current data file and type is listed on the standard output.
  See [XYEPLS]COLUMN to read an arbitrary column into one of the
  predefined igi arrays.  See [XYEPLS]SECTION to read an IRAF image into
  a buffer.
  A row selector can be appended to the file name for a FITS table with
  arrays as elements of its columns to allow plotting of data from these
  tables.  (For more information on the syntax of row selectors, use
  "</span>help selectors<span style="font-family: monospace;">" in the TABLES package.)
  This command is saved in the command buffer.
  </section>
  <section id="s_ddraw_">
  <h3>Ddraw </h3>
  Arguments:  DDRAW xpos ypos
  Draw a line in the current line style from the current position to the
  normalized device coordinates (NDC) specified by the two floaing point
  parameters.  The ending point of the line becomes the new current
  position. If "</span>:DDRAW<span style="font-family: monospace;">" is used in cursor mode, xpos and ypos are ignored
  and should be omitted. 
  See DRAW to draw in WC and VDRAW to draw in VPC.
  This command is saved in the command buffer.
  </section>
  <section id="s_define">
  <h3>Define</h3>
  Arguments:  DEFINE macro
  Enter macro text.  The argument is the name of the macro.  A defined
  macro may be invoked as any other command, possibly with arguments. 
  DEFINE causes igi to enter macro define mode, in which commands are not
  interpreted (except END) but stored as is.  The prompt "</span>macro&gt; <span style="font-family: monospace;">"
  indicates macro define mode.  To terminate the macro definition, type
  "</span>END<span style="font-family: monospace;">".  The macro is invoked by typing its name.  The name is not case
  sensitive.  It may not be abbreviated.  When the macro is invoked, the
  text is expanded and interpreted just as typed text. 
  Optional macro arguments are positional and are defined by the character
  "</span>&amp;<span style="font-family: monospace;">" and an integer.  Defined arguments are replaced by their values
  typed on the command line in the order specified by their definition.
  The order in which the arguments appear in the macro text is
  unimportant, but the order in which the argument values appear on the
  invoked macro must match the definitions.  The highest numbered argument
  definition specifies how many argument values must appear in the macro
  call. 
  If a macro is defined more than once with the the same name, the new
  text and argument definition will supercede existing text.  Macro text
  may be listed (LIST), edited (EDITCMD), or saved in a text file (WRITE).
  The MACROS command lists the currently defined macro names and the
  number of their arguments. 
  </section>
  <section id="s_dlist">
  <h3>Dlist</h3>
  Arguments:  DLIST [file]
  Print the data values (if any) currently in the X, Y, error, and point
  code buffers.  If there is no argument, print to standard output.  If
  STDOUT is not redirected, uses the IRAF page facility.  The optional
  argument specifies the name of a file in which to save the output.
  This is not redirection, so it's not possible to append to an existing
  file but will always write a new file or overwrite an existing file.
  With no arguments, DLIST is not saved in the command buffer.  With an output file argument, DLIST is saved in the command buffer.
  </section>
  <section id="s_dot___">
  <h3>Dot   </h3>
  no arguments
  Draw a single marker of the current style, size, and angle at the
  current location.
  See PTYPE, EXPAND, and ANGLE to specify the marker style.  To draw a
  single circle or ellipse, see the ELLIPSE command.  To draw markers at
  the data coordinates in the plot buffers, use the POINTS command.
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_draw_">
  <h3>Draw </h3>
  Arguments:  DRAW xpos ypos
  Draw a line in the current line style from the current position to the
  coordinates specified by the two floating point parameters in world
  coordinates (WC).  The ending point of the line becomes the new current
  position.  If "</span>:DRAW<span style="font-family: monospace;">" is used in cursor mode, xpos and ypos are ignored
  and should be omitted.
  See [DPV]RELOCATE (or [DPV]MOVE) to specify the initial position and see
  [DPV]DRAW to specify the position in other coordinates. 
  This command is saved in the command buffer.
  </section>
  <section id="s_drelocate_">
  <h3>Drelocate </h3>
  Arguments:  DRELOCATE xpos ypos
  Pen up move, i.e., change the current position to the normalized device
  coordinates (NDC) specified by the two floating point parameters.  This
  is an alias for DMOVE.  If "</span>:DRELOCATE<span style="font-family: monospace;">" is used in cursor mode, xpos
  and ypos are ignored and may be omitted.  In fact, it is unnecessary to
  use any move command in cursor mode.  Issuing any command or request
  for readback resets the current position to the coordinates of the
  cursor.
  This command is saved in the command buffer.
  </section>
  <section id="s_ecolumn_">
  <h3>Ecolumn </h3>
  Arguments:  ECOLUMN column
  Read error values from the column in the current data file specified by
  the column parameter.  If the input data is a text (ASCII list) file, 
  column must be an integer specifying the column number.  If it is an 
  ST4GEM or FITS table, column must be a string specifying the column name.  Note 
  that table column names are case-sensitive and may not be abbreviated.
  See DATA to specify the input file (table) name.  See ETYPE to specify
  the style of error bars and ERRORBAR for drawing them.
  This command is saved in the command buffer.
  </section>
  <section id="s_editcmd">
  <h3>Editcmd</h3>
  Arguments:  EDITCMD [macro]
  Edit the command buffer or macro text.  The edited text may be invoked 
  as before.
  </section>
  <section id="s_eevaluate">
  <h3>Eevaluate</h3>
  Arguments:  EEVALUATE expression
  Replace the errors data vector by the result of the expression in the string
  argument.  Typical expression syntax may be used to specify operators: 
  +, -, *, /, **, and common functions:  sqrt, sin, cos, log, log10, exp,
  etc.  The current value of any of the four plot data vectors is specified by
  the single (case-insensitive) character:  x, y, e, or p;  the element
  number may be specified by r, and the number of elements in the vector
  by n.  For example, EEVALUATE log10(r**2) will replace each error value by
  the log of the square of the element number.   An array may operate on
  itself.
  This command is saved in the command buffer.
  </section>
  <section id="s_ellipse_">
  <h3>Ellipse </h3>
  Arguments:  ELLIPSE eccentricity
  Draw an ellipse with specified eccentricity.  The major axis is the
  current size multiplied by the default point marker size.  The center of
  the ellipse is at the current location, and it is rotated
  counterclockwize from the horizontal by the current angle. 
  If a negative value is provided for eccentricity, it will be interpreted
  as an ellipticity defined as 1 - b/a where a is the length of the semi-major
  axis, and b is the length of the semi-minor axis.  The absolute value will
  then be converted internally to an eccentricity using 
  e = sqrt(2*abs(eccentricity) - eccentricity^2).  
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_end">
  <h3>End</h3>
  no arguments
  End the current command mode.  In normal interactive command mode, END 
  terminates igi.  END also terminates macro define mode to resume
  interpreting commands.  
  </section>
  <section id="s_erase">
  <h3>Erase</h3>
  no arguments
  Erase the entire screen.  For hardcopy (printer) plots, ERASE will
  start a new frame (page).  All of the parameters retain their values.
  To reset data and plot attribute parameters to defaults, use RESET.
  Note that it is not possible to erase only part of the screen, except
  to UNDO a previous command, if the hardware supports the erase line
  type.
  In the particular case of PostScript output to a file, ERASE will also
  create a new page.  If you wish to run igi several separate times but
  create a single file, you must use "</span>append=yes<span style="font-family: monospace;">" for the second and
  subsequent plots.  Use the ERASE command to create a new frame.  This
  will not actually erase existing graphics from any non-interactive
  (hard copy) graphics output.
  </section>
  <section id="s_errorbar">
  <h3>Errorbar</h3>
  Arguments:  ERRORBAR direction
  Draw error bars at the positions specified by current X and Y coordinate
  buffers.  The integer argument direction specifies the direction of the
  error bars:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='ERRORBAR' Level=1 Label='' Line='' -->
  <dd><div class="highlight-default-notranslate"><pre>
  -2 -- -Y (down)
  -1 -- -X (left)
   1 -- +X (right)
   2 -- +Y (up)
   3 -- -X (left)
   4 -- -Y (down)
  </pre></div>
  </dd>
  </dl>
  ERRORBAR must be used twice to draw a full error bar spanning the data
  coordinate.  For symmetrical errors, use the same data column and change
  the direction argument.  For asymmetrical errors, read new data into the
  errors buffer and respecify the direction arguement. 
  The current text and point size determines the size of the ticks at the
  end of each error bar;  use EXPAND to change the size.  Change the
  default error bar style with ETYPE. 
  See DATA and ECOLUMN to read error data and EEVALUATE to operate on
  them. 
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_etype">
  <h3>Etype</h3>
  Arguments:  ETYPE style
  Change the error bar style.  The argument specifies which style to 
  select:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='ETYPE' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  1 -- Standard error bars with a bar and a tick at the end
  2 -- Bar only, no tick at the end
  3 -- Tick only, no bar
  4 -- Upper or lower limit arrow (pointing away from data coordinate)
  </pre></div>
  </dd>
  </dl>
  See the ERRORBAR command for drawing the error bars.  See the ULLIM
  command for another way to draw upper or lower limit symbols.
  This command is saved in the command buffer.
  </section>
  <section id="s_evaluate">
  <h3>Evaluate</h3>
  Arguments:  [XYEP]EVALUATE expression
  Replace a plot data vector by the result of the expression in the string
  argument.  Typical expression syntax may be used to specify operators: 
  +, -, *, /, **, and common functions: sqrt, sin, cos, log, log10, exp,
  etc.  Note that the trig functions expect arguments in degrees!  The
  current value of any of the four plot vectors is specified by the single
  character:  x, y, e, or p, the element number may be specified by r, and
  the number of elements in the vector by n.  For example, XEVALUATE
  log10(r**2) will replace each X value by the logarithm of the square of
  the element number.  An array may operate on itself.
  [XY]EVALUATE may be used in place of [XY]LOGARITHM.
  This command is saved in the command buffer.
  </section>
  <section id="s_expand_">
  <h3>Expand </h3>
  Arguments:  EXPAND [size]
  Set the marker and text size in units of the default size, 0.0125 times
  the smallest dimension of the device.  Note that this base size is
  constant, regardless of the window, virtual page, or viewport.  That is,
  characters and points will not be scaled to the size of the viewport as
  a fraction of the full page, but will be drawn the same size on a full
  page plot as on a plot in a small window.  So if you wish to retain the
  relative size of objects on a pane of a windowed screen, you must
  manually reset the size using EXPAND.
  If no argument is specified, the current setting of the size is printed, 
  with the resulting character and point sizes in NDC units.
  This command is saved in the command buffer.
  </section>
  <section id="s_fillpat">
  <h3>Fillpat</h3>
  Arguments:  pattern
  Specify the fill pattern for hollow symbols and bar graphs.  The
  integern argument is an index for the device-dependent pattern.  A
  value of zero indicates no fill or hollow pattern with an outline
  only.
  If no argument is specified, the current setting of the pattern index is printed.
  This command is saved in the command buffer.
  </section>
  <section id="s_fitpix">
  <h3>Fitpix</h3>
  Arguments:  FITPIX [left right bottom top]
  Specify the location of the viewport (plot axes) and force the shape of
  the viewport to be the same as the pixmap raster image input by
  ZSECTION.  The resulting viewport will, in general, not actually span
  the edges specified by the command arguments.  The bottom right corner
  is fixed, but the right or top edge will be changed to adjust the
  aspect ratio of the viewport to match the aspect ratio of the image as
  rendered on the output device.
  Note that this is device-dependent in the sense that different devices
  have different aspect ratios and the image, while having the same
  aspect ratio, may not occupy exactly the same location on the page.
  Both device and image pixels are assumed to be square.  The computed
  viewport depends on the shape of the device, the input image, and the
  edges specified to FITPIX.
  For example,
  <div class="highlight-default-notranslate"><pre>
  
  igi&gt; zsection myimage[1:100,1:200]  # Read a "portrait" image
  igi&gt; fitpix .25 .75 .25 .75         # Use a centered, half-size display
  igi&gt; limits;  zrange                # Autoscale
  igi&gt; pixmap                         # Display
  
  </pre></div>
  on a "</span>landscape<span style="font-family: monospace;">" format device would result in a viewport that was
  narrower than the one specified.
  The arguments specify the edges of the viewport as a fraction of the
  virtual page.  If FITPIX is used with no arguments, the edges of the
  current viewport are listed.  If FITPIX is not used, the default is to
  fill the viewport, which in general matches the virtual page, except
  for margins outside the axes for tick labels.  This is useful to smear
  (widen) a narrow image section, such as a spectrum, to cover the
  viewport.  LOCATION or PHYSICAL may be used to specify a viewport in
  this case.  If the first (only) argument is INDEF, then FITPIX will use
  the currently specified viewport but adjust the top right corner to
  match the aspect ratio of the input image.
  Note that the virtual page itself may be a subset of the display area.
  See PHYSICAL, VPAGE, and WINDOW to specify the virtual page.
  This command is saved in the command buffer.
  </section>
  <section id="s_flip">
  <h3>Flip</h3>
  no arguments
  Flip an axis by reversing the upper and lower limits.  The prefix to
  the command (X or Y) determines which axis is modified.  This must be
  used before the axes are drawn (BOX) for the plot to scale to match the
  data.  This is equivalent to specifying LIMITS with the lower and upper
  limits reversed, but operates on the currently set limits, whether set
  manually or automatically.
  [XFY]LIP should be used _after_ LIMITS.  [XY]FLIP only modifies
  whatever is the currently set scaling.  Using LIMITS after [XY]FLIP
  will nullify the flip by resetting the scale to whatever is specified
  in the LIMITS command.
  This command is saved in the command buffer.
  </section>
  <section id="s_fmtick">
  <h3>Fmtick</h3>
  Arguments:  FMTICK [format]
  Specify the print format for axis tick labels.  The optional argument
  format is a string containing a Fortran or SPP print format specifier.
  Note that in general, axis labels are floating point values.  By
  default, igi tries to format the labels logically, including
  superscripts for exponential notation on large numbers.  If there is no
  argument, reset to the default formatting.  Note that overriding the
  default precludes formatting using superscripts.
  See AXIS and BOX for drawing axes and tick labels.
  This command is saved in the command buffer.
  </section>
  <section id="s_fontset_">
  <h3>Fontset </h3>
  Arguments:  FONTSET fonts
  Select the set of fonts to use in drawing text.  The argument is a
  string specifying igi or gio fonts.  If no argument is specified,
  FONTSET shows the current font set in use.  The choices for the "</span>fonts<span style="font-family: monospace;">"
  argument are "</span>soft<span style="font-family: monospace;">" or "</span>igi<span style="font-family: monospace;">", indicating to use the software outline
  (igi) fonts or "</span>hard<span style="font-family: monospace;">" or "</span>gio<span style="font-family: monospace;">" indicating to use hardware (gio) fonts.
  In the former case, the text will appear similar regardless of the
  device used to display or print the plot.  In the latter case, the
  appearance of the fonts depends on the device.  This is primarily
  intended to permit using PostScript fonts resident in a laser printer
  or used by a PostScript interpreter, which can be realized by using the
  PostScript graphics kernel, psikern.
  In both cases, the EXPAND command is used to specify the size, ANGLE
  the rotation, COLOR sets the hardware(kernel)-specific color, and
  JUSTIFY the justification.  LWEIGHT may be used to change the line
  width used to draw igi characters, but does not effect gio characters.
  Embedded control characters specify further attributes of the plotted 
  text.  Note that there are different escapes for the font sets.
  <dl>
  <dt><b></b></dt>
  <!-- Sec='FONTSET ' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi   gio
  ---   ---
  \\          Set mode for rest of string
  \           Set mode for next character only
  
  \r    fBR   Roman plain font
  \g       Greek (Symbol) font
  \s          Script font
  \t          Small sans-serif font
  \i          Toggle italics
        fBI   Italic roman font
        fBB   Bold roman font
           Toggle proportional spacing
  \u          Superscript
  \d          Subscript
  \b          Backspace
  \e          End string
           User-defined PostScript font
  </pre></div>
  </dd>
  </dl>
  Italics (\\i) and proportional spacing (\ behave as toggles for igi
  fonts, enclosing a (sub)string in matching escapes sets the attribute
  for that string only.  Superscript and subscript each ondoes the action
  of the other, to write a substring as a super(sub)script, enclose it in
  matching pairs of \\u...\\d or \\d...\\u.
  The User-defined PostScript font is set using the PSFONT command prior to
  using this escape sequence.  This font will then be active for remainder
  of the string or until another font is selected, like the Roman font with 
  the  escape sequence.
  This command is saved in the command buffer.
  </section>
  <section id="s_grid">
  <h3>Grid</h3>
  No arguments
  Draw lines connecting major tick marks on the axes drawn by the BOX
  command.  Note that BOX must have been used first to compute the tick
  spacing.  GRID uses the current value of the line style (solid, dotted,
  etc.) and the line width in drawing the grid.  See LTYPE to set the
  line type and LWEIGHT to set the line width.
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO.
  </section>
  <section id="s_help">
  <h3>Help</h3>
  Arguments:  HELP [command]
  Page help text.  If the optional argument is present, a description 
  of the command is listed.  See <span style="font-family: monospace;">"!help help"</span> for a description of the 
  IRAF help command.  The optional argument may also be used to list any 
  major section of the igi help text.  For example, HELP description lists 
  the general description of igi.
  See APROPOS for listing commands by keyword and ? for a list of the 
  commands.
  </section>
  <section id="s_histogram">
  <h3>Histogram</h3>
  Arguments:  HISTOGRAM width
  Draw a histogram style plot (bar graph) through the current X and Y
  data.  If no X data exist, the horizontal axis will be scaled on the
  pixel numbers.  Note that this command does NOT compute and plot an
  actual histogram of the data, but plots a bar graph style plot of the
  data in the plot vectors.  This is an alias for the BARGRAPH command.
  The optional argument specifies the relative width of the bars.  If no
  argument is used or the value is INDEF, the bars fill the available
  space.  For equally spaced data (equally-spaced or no X values), all of
  the bars are as wide as the difference in X between adjacent points.
  For unequally spaced data, the edges of the bars fall halfway between
  adjacent points.  The <span style="font-family: monospace;">"width"</span> argument is a constant factor to apply to
  this width.  For example, <span style="font-family: monospace;">"HISTOGRAM 0.5"</span> will draw bars half the
  natural width, leaving an equal space between bars.  It is not possible
  to apply a different factor to each bar separately, except by
  specifying the X data explicitly.
  Bars may be drawn with a fill pattern, specified using the FILLPAT
  command.  Note that the nature of the fill patterns depends on the
  device and kernel used.  See LTYPE and LWEIGHT for specifying the style
  of the curve to draw.  See CONNECT, STEP, and POINTS for different
  curve styles
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_id">
  <h3>Id</h3>
  no arguments
  Draw a standard identification text string vertically to the right of
  the right Y (vertical) axis.  The label includes the user name, time,
  date, etc., for example:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='ID' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi STScI/IRAF V2.5 LEVAY@scivax Fri 10:25:50 15-Apr-88
  </pre></div>
  </dd>
  </dl>
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_imgwcs">
  <h3>Imgwcs</h3>
  no arguments
  Toggle using world coordinates of an image in the X plot buffer (see the
  YSECTION command).  By default SECTION will not fill in the X
  buffer when reading the Y buffer.  If the IMGWCS command is used, the
  next use of YSECTION will do so.  Using IMGWCS again will toggle
  this state.  Note that this command together with YSECTION will modify
  the contents of the plot buffer.
  Note that this toggles an internal parameter.  Therefore if this
  command is used twice consecutively, it will revert to it's previous
  state.
  This command is saved in the command buffer.
  </section>
  <section id="s_input_">
  <h3>Input </h3>
  Arguments:  INPUT filename
  Execute commands from a file.  The commands are executed as they are 
  read.  Only the INPUT command is written to the command buffer, not the 
  individual commands.  Use the READ command to input the commands into 
  the buffer without execution.
  This command is saved in the command buffer.
  </section>
  <section id="s_justify">
  <h3>Justify</h3>
  Arguments:  JUSTIFY [justification]
  Set the justification for text drawn using the LABEL command.   
  <dl>
  <dt><b></b></dt>
  <!-- Sec='JUSTIFY' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
         left  center  right
  above    7      8      9
  center   4      5      6
  below    1      2      3
  </pre></div>
  </dd>
  </dl>
  This command is saved in the command buffer.
  </section>
  <section id="s_label_">
  <h3>Label </h3>
  Arguments:  LABEL string
  Draw text in the parameter string at the current position.  The string
  is assumed to terminate at the end of the line, or may be enclosed in
  single or double quotes to enter more than one command on the line.  The
  size of the text may be specified with the EXPAND command, the
  orientation may be set using the ANGLE command, and the justification
  may be specified with the JUSTIFY command.  Roman, Greek, Script, and 
  small Type fonts may be selected using the \r, \g, \s, or \t escapes. 
  Any font may be italicized by using \i escape, and any font may be 
  printed in fixed rather than proportional spacing by using the 
  escape.  A single backslash (\) sets the attribute for a single
  character only.  Two backslashes (\\) sets the attribute for the
  remainder of the string, or until it's reset by the opposite attribute.
  Embedded control characters specify further attributes of the plotted 
  text:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='LABEL ' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  \\ -- set mode for rest of string
  \  -- set mode for next character only
  
  \r -- roman font
  \g -- greek font
  \s -- script font
  \t -- small sans-serif font
  \i -- toggle italics
  -- toggle proportional spacing
  \u -- superscript
  \d -- subscript
  \b -- backspace
  \e -- end string
  </pre></div>
  </dd>
  </dl>
  Italics (\\i) and proportional spacing (\ behave as toggles, enclosing
  a (sub)string in matching escapes sets the attribute for that string
  only.  Superscript and subscript each ondoes the action of the other, to
  write a substring as a super(sub)script, enclose it in matching pairs of
  \\u...\\d or \\d...\\u.  Note that these are the igi text escapes.
  When using gio fonts (see FONTSET) a different set of escapes applies.
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_lcolumn">
  <h3>Lcolumn</h3>
  Arguments:  LCOLUMN column
  Read a column of limits data from the file specified by the data
  command.  If the input data is a text (ASCII list) file, column must be
  an integer specifying the column number.  If it is an ST4GEM  or FITS table,
  column must be a string specifying the column name.  Note that table
  column names are case-sensitive and may not be abbreviated. 
  See DATA to specify the input file (table) name.  See ULLIM for use of 
  the limits data in drawing upper or lower limit symbols.
  This command is saved in the command buffer.
  </section>
  <section id="s_limits_">
  <h3>Limits </h3>
  Arguments:  LIMITS [left right bottom top]
  Set the plot scale, i.e., the user (world) coordinates assigned to the
  edges of the plot (viewport).  If no arguments are specified, then the
  limits will be set automatically based on the range of current data
  values.  The data used to autoscale depends on which data buffers are
  in use.
  Note that in general, the current viewport is not the entire screen.
  The scaling set by LIMITS may be adjusted to include a border between
  the data extremes and the axes using the MARGIN command.  See BOX for
  drawing axes at the current plot scale.
  This command is saved in the command buffer.
  </section>
  <section id="s_lines_">
  <h3>Lines </h3>
  Arguments:  LINES [first[ last]]
  Specify the range of lines to read from the input data file using the
  DATA and [XYEPLS]COLUMN commands.  This applies to both input text and
  binary tables.  For example:
  <div class="highlight-default-notranslate"><pre>
  
  LINES 10 20
  
  </pre></div>
  will cause lines 10 through 20 to be read using the next COLUMN
  command.
  If no parameters are specified, then the current range will be listed.
  Specifying first = 0 is the same as first = 1;  last = 0 will read to
  the last row in the input file.  Specifying one argument will read only
  that one line.  Therefore, to return the range of lines to the default
  (read all lines in the file) use <span style="font-family: monospace;">"LINES 0"</span>.
  This command does not have any effect on reading image sections (See
  SECTION).
  This command is saved in the command buffer.
  </section>
  <section id="s_list">
  <h3>List</h3>
  Arguments:  LIST [macro]
  List the command buffer.  The optional argument is used to list the text
  of a defined macro.  See MACROS to list defined macro names.
  </section>
  <section id="s_location_">
  <h3>Location </h3>
  Arguments:  LOCATION [left right bottom top]
  Specify the location of the plot axes (viewport) as a fraction of the
  virtual page.  The default is to fill the virtual page except for
  margins outside the axes for tick labels.  Note that the virtual page
  itself may be a subset of the display area.  If the first argument is
  INDEF, then the existing viewport will be adjusted to make it square
  regardless of the device.
  See PHYSICAL, VPAGE, and WINDOW to specify the virtual page.  See
  FITPIX for specifying a viewport that matches an image input with
  ZSECTION.
  This command is saved in the command buffer if arguments are specified.
  </section>
  <section id="s_ltype_">
  <h3>Ltype </h3>
  Arguments:  LTYPE [style]
  Set the line style.  The integer parameter selects a hardware specific 
  line type.
  <dl>
  <dt><b></b></dt>
  <!-- Sec='LTYPE ' Level=1 Label='' Line='' -->
  <dd><div class="highlight-default-notranslate"><pre>
  -1 -- Clear (erase)
   0 -- Solid (default)
   1 -- Dotted
   2 -- Dashed
   3 -- Dashed
   4 -- Dot-dash
   5 -- Dot-dash
   6 -- Dashed
  </pre></div>
  </dd>
  </dl>
  If no parameter is given, the current setting is listed.  The default is
  solid. 
  This command is saved in the command buffer.
  </section>
  <section id="s_lweight_">
  <h3>Lweight </h3>
  Arguments:  LWEIGHT [width]
  Set the line width.  A floating point parameter specifies the factor to 
  multiply the default hardware line width.  Not all devices support 
  selectable line width.
  This command is saved in the command buffer.
  </section>
  <section id="s_macros">
  <h3>Macros</h3>
  no arguments
  Print the names of defined macros and the number of their arguments.
  See DEFINE to define a new macro.
  </section>
  <section id="s_margin">
  <h3>Margin</h3>
  Arguments:  MARGIN [fraction]
  Adjust the current plot scale to provide a border between the data
  extremes and the axes.  The optional argument specifies the size of the
  margin as a fraction of the current viewport.  If the argument is
  missing, the default margin is 0.025, or 2.5% of the size of the
  viewport.
  </section>
  <section id="s_minmax">
  <h3>Minmax</h3>
  no arguments
  Print the range of data values in both the X and Y arrays.
  </section>
  <section id="s_notation">
  <h3>Notation</h3>
  Arguments:  NOTATION xlo xhi ylo yhi
  Set the format for axis labels drawn by BOX.  The parameters [xy]lo and
  [xy]hi specify the range of values within which axis label values will
  be written as floating point values and outside which they will be
  written in exponential notation.  The default is [xy]lo = 1.0E-4 and
  [xy]hi = 1.0E+5.  If xlo = xhi, all values on the X axis will be written
  in exponential notation, and similarly for the Y axis. 
  This command is saved in the command buffer.
  </section>
  <section id="s_number">
  <h3>Number</h3>
  No arguments
  Draw the element number at the coordinates of each data point.  If no X
  vector is defined, then use the element number as the X coordinate.  If
  both an X and Y vector is defined, use those values as the X and Y
  coordinate.  The current size, line width, rotation angle and text
  justification are used for the attributes of the string.
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_pagecmd">
  <h3>Pagecmd</h3>
  Arguments:  PAGECMD [macro]
  Page the command buffer, i.e., invoke the IRAF pager to list the stored 
  commands.  The optional argument is used to page the text of a defined 
  macro.  
  </section>
  <section id="s_pcolumn_">
  <h3>Pcolumn </h3>
  Arguments:  PCOLUMN column
  Read point specifications from the input data file (table).  If the file
  is a text file, the column number must be an integer.  If the file is an
  ST4GEM or FITS table, the column name must be a string.  Note that table column
  names are case-sensitive and may not be abbreviated.  
  See DATA to specify the input file (table) name.
  The floating point data values are assumed to represent a coded marker
  style and size for each data value.  The units digit specifies the
  marker style by the same code as PTYPE:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='PCOLUMN ' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  0 -- Open, vertices connected
  1 -- Skeletal, center connected to vertices
  2 -- Starred
  3 -- Filled
  4 -- Half-filled
  </pre></div>
  </dd>
  </dl>
  Any value larger than 4 is read as 4 (half-filled symbols).
  The tens and up digits specify the number of vertices in the marker, and
  the decimal portion represents a multiplier for the global text and
  marker size.  The global text and marker angle determines the angle of
  all point markers.  For example, if the value in the points column were 
  52.5 the marker would be a five pointed star half the size of the 
  current marker and text size.  If no decimal value is present, the 
  marker size is the global text and marker size.
  This command is saved in the command buffer.
  </section>
  <section id="s_pdraw_">
  <h3>Pdraw </h3>
  Arguments:  PDRAW xpos ypos
  Draw a line in the current line style from the current position to the
  coordinates specified by the two floating point parameters in viewport
  coordinates (PC).  The ending point of the line becomes the new current
  position.  If <span style="font-family: monospace;">":PDRAW"</span> is used in cursor mode, xpos and ypos are
  ignored and should be omitted.
  See [DPV]RELOCATE (or [DPV]MOVE) to specify the initial position and see
  [DPV]DRAW to specify the position in other coordinates. 
  This command is saved in the command buffer.
  </section>
  <section id="s_pevaluate">
  <h3>Pevaluate</h3>
  Arguments:  PEVALUATE expression
  Replace the point marker code data vector by the result of the expression
  in the string argument.  Typical expression syntax may be used to
  specify operators: +, -, *, /, **, and common functions: sqrt, sin, cos,
  log, log10, exp, etc.  The current value of any of the four plot data
  vectors is specified by the single (case-insensitive) character:  x, y,
  e, or p, the element number may be specified by r, and the number of
  elements in the vector by n.  
  This command is saved in the command buffer.
  </section>
  <section id="s_physical">
  <h3>Physical</h3>
  Arguments:  PHYSICAL [left right bottom top]
  Set the plot location on the device in physical units (inches).  This is
  analagous to the VPAGE command that sets the virtual page on the device.
  While VPAGE uses normalized device coordinates (NDC), PHYSICAL uses real
  device coordinates.  The LOCATION command may be used to specify the
  viewport (location of the axes) in normalized coordinates on the virtual
  page.  The LIMITS command defines the transformation between data,
  world, or user coordinates (WC) and the viewport. 
  This command is saved in the command buffer.
  </section>
  <section id="s_pixmap">
  <h3>Pixmap</h3>
  no arguments
  Render (display) an image if data are in the Z buffer, read using ZSECTION.  The image is displayed using the current pixel scaling specified by LIMITS, the brighness scale specified by ZRANGE in the current viewport, set by FITPIX LOCATION, or PHYSICAL.
  </section>
  <section id="s_playback">
  <h3>Playback</h3>
  no arguments
  Execute the commands in the command buffer.  Note that any attributes 
  (point style, size, etc.) set by the already executed commands may
  influence the action of the playback. 
  </section>
  <section id="s_points">
  <h3>Points</h3>
  no arguments
  Draw a marker at each data coordinate according to the code read from
  the data file by PCOLUMN.  The floating point data values are assumed
  to represent the marker style and size for each data value.  See PTYPE
  for coding the marker style.  The size of the markers is specified by
  the current size parameter and may be set using the EXPAND command.
  The marker may be rotated by the current angle parameter, which may be
  set using the ANGLE command.  See the DOT command to draw a single
  marker at the current pen position.  See the ELLIPSE command to draw a
  single ellipse (or circle) at the current pen position.  The current
  pen position is left at the last point drawn.
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_polygon">
  <h3>Polygon</h3>
  no arguments
  Draw a closed, fill polygon connecting
  the data coordinates.  The COLOR command affects the color of the
  filled area and the FILLPAT determines the pattern used to fill the
  polygon.  See CONNECT to draw a curve through the points.
  See POINTS for drawing markers without
  connection.  The current pen position is left on the last point.
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_pscmd">
  <h3>Pscmd</h3>
  Arguments:  PSCMD  [PostScript command string]
  Insert a PostScript command string directly into the PostScript output.
  This command will only pass this string along if the output device will
  use the 'psikern' kernel for output; meanwhile, this command will not do
  anything for any other output device.  The user has complete control over
  the string inserted into the PostScript and assumes all responsibility for
  correct syntax and usage of the PostScript command.  For example, this 
  command works 
  well for inserting PDFMARK commands into the output PostScript files to
  provide Acrobat PDF functionality when converted to PDF format.
  </section>
  <section id="s_psfont_">
  <h3>Psfont </h3>
  Arguments:  PSFONT [font name]
  Set the name of the Postscript font the user wants to use in the following
  label(s).  This font will be used when GIO fonts are specified by setting 
  FONTSET to 'gio' or 'hard' fonts.  A special escape sequence, <span style="font-family: monospace;">"<span style="font-family: monospace;">", signifies
  when this font will be used in the string and will be active for that
  string until reset with another escape sequence.  This font can also be
  redefined as necessary in the IGI script to allow the use of as many fonts
  as needed, although only one additional font may be active at a time.
  Furthermore, only those fonts recognized by the printer you are sending the
  plot to will be output, with each printer handling unrecognizable font names
  differently.
   
  </section>
  <section id="s_ptype_">
  <h3>Ptype </h3>
  Arguments:  PTYPE [vertices style]
  Set the marker type.  The integer parameter vertices specifies how many 
  vertices are in the marker, and the parameter style selects one 
  of the marker styles either as an integer code or a string keyword:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='PTYPE ' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  0  open     -- Polygon outline, open vertices connected
  1  skeletal -- Skeletal, center connected to vertices
  2  starred  -- Starred, lines radiating from the center
  3  solid    -- Filled polygon
  4  half     -- Half filled polygon
  </pre></div>
  </dd>
  </dl>
  Any value larger than 4 is read as 4 (half-filled symbol type).
  Alternately, the style may be specified as a string with the 
  If the number of vertices is -1, 0, or 1, then DOT or POINTS draws the
  smallest plottable point.  If the number of vertices is less than -1,
  PTYPE ignores the style DOT or POINTS draws markers defined by the IRAF
  marker drawing routine as described in the GIO reference manual.
  To draw a circle, use a large number of vertices, 25, e.g.  To draw
  small points, use a small size, EXPAND .1, e.g.  See the POINTS command
  to draw markers at the data coordinates, the DOT command to draw a
  single marker at the current pen position.
  This command is saved in the command buffer.
  </section>
  <section id="s_putlabel_">
  <h3>Putlabel </h3>
  Arguments:  PUTLABEL justify string
  Draw text in the argument string relative to the current coordinates
  according to the argument justify: 
  <dl>
  <dt><b></b></dt>
  <!-- Sec='PUTLABEL ' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
         left  center  right
  above    7      8      9
  center   4      5      6
  below    1      2      3
  </pre></div>
  </dd>
  </dl>
  The size of the text may be specified with the EXPAND command and the
  angle may be set using the ANGLE command. 
  Embedded control characters specify further attributes of the plotted 
  text:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='PUTLABEL ' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  \\ -- set mode for rest of string
  \  -- set mode for next character only
  \r -- roman font
  \g -- greek font
  \s -- script font
  \t -- tiny font
  \i -- toggle italics
  -- toggle proportional spacing
  \u -- superscript
  \d -- subscript
  \b -- backspace
  \e -- end string
  </pre></div>
  </dd>
  </dl>
  Also see the LABEL command.
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_read_">
  <h3>Read </h3>
  Arguments:  READ filename
  Read commands into the command buffer without execution.  Commands come 
  from the command file specified by the filename parameter.  
  See EDITCMD, INPUT, LIST, and PAGECMD.
  </section>
  <section id="s_relocate_">
  <h3>Relocate </h3>
  Arguments:  RELOCATE xpos ypos
  Pen up move, i.e., change the current position to the world (user)
  coordinates (WC) specified by the two floating point parameters.  This
  is an alias for MOVE.  If "</span>:RELOCATE<span style="font-family: monospace;">" is used in cursor mode, xpos and
  ypos are ignored and should be omitted.  In fact, it is unnecessary to
  use any move command in cursor mode.  Issuing any command or request
  for readback resets the current position to the coordinates of the
  cursor.
  See [DPV]RELOCATE to specify the position in NDC, PC and VPC.
  This command is saved in the command buffer.
  </section>
  <section id="s_reset">
  <h3>Reset</h3>
  no arguments
  Return settable plot and data parameters to defaults.
  </section>
  <section id="s_scolumn">
  <h3>Scolumn</h3>
  Arguments:  SCOLUMN column
  Read a column of scratch data from the file specified by the data
  command.  If the input data is a text (ASCII list) file, column must be
  an integer specifying the column number.  If it is an ST4GEM or FITS table,
  column must be a string specifying the column name.  Note that table
  column names are case-sensitive and may not be abbreviated. 
  See DATA to specify the input file (table) name.  See EVALUATE for use
  of the scratch data in manipulating the data buffers. 
  This command is saved in the command buffer.
  </section>
  <section id="s_saocmap">
  <h3>Saocmap</h3>
  Arguments:  SAOCMAP cmapfile
  Apply a colormap to an image rendered using PIXMAP.  The argument is
  the name of a plain text file containing a colormap written by
  SAOimage.  This consists of a functional description of a mapping
  between stored and displayed pixel values for the three display
  colors:  red, green, and blue, as shown in the example below.
  <div class="highlight-default-notranslate"><pre>
  
  # SAOimage color table
  # saodump - SAODUMP[1/1]
  # Fri Mar 13 15:53:40 1992
  PSEUDOCOLOR
  RED: gamma 1.504
  (0.000,0.000)(0.500,1.000)(1.000,1.000)
  GREEN: gamma 1.504
  (0.000,0.000)(0.250,0.000)(0.750,1.000)(1.000,1.000)
  BLUE: gamma 1.504
  (0.000,0.000)(0.500,0.000)(1.000,1.000)
  
  </pre></div>
  Note that the colors displaying correctly depends on the graphics
  kernel and the output device.  Only the PostScript kernel (psikern)
  supports this feature.
  </section>
  <section id="s_section">
  <h3>Section</h3>
  Arguments:  [XYEPLS]SECTION image project
  This family of commands reads a column of data from an IRAF (OIF, or
  STF) image.  The image may be of any dimensionality and data type and
  may include an image section specification that might be a subraster of
  the image or may include a group number.  By default, all of the image
  section pixels are read as a one-dimensional array into the specified
  igi vector.
  There is no capability to draw any multi-dimensional plots or gray
  scale images.  It is not possible to extract an arbitrarily oriented
  vector from a multidimensional image.  (See the pvector task in the
  plot package.)
  [XYEPLS]SECTION overrides the use of the DATA and [XYEPLS]COLUMN
  commands in filling the data arrays.  One array may be filled with an
  image and another by a table column using DATA and [XYEPLS]COLUMN, yet
  another from a text file, also using DATA and [XYEPLS]COLUMN.
  Multi-dimensional images are read pixel by pixel, line by line, plane
  by plane, and so forth.  For example, a 2-D image is read from left to
  right along each line from the bottom to the top.  Optionally, a
  multi-dimensional section may be reduced to a single dimension by
  averaging or summing all of the image lines into a single vector the
  size of the lines in the image section.  The optional argument project
  is an integer.
  For example, the command:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='SECTION' Level=1 Label='' Line=' ' -->
  <dd>igi&gt; XSECTION myimage[1:10,1:10]
  </dd>
  </dl>
  will read 100 pixels from the lower left corner of myimage into the X
  buffer.  The command:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='SECTION' Level=1 Label='' Line=' ' -->
  <dd>igi&gt; XSECTION myimage 1
  </dd>
  </dl>
  will read read all of the pixels but will store the average of all of
  the image lines in the X buffer.
  <dl>
  <dt><b></b></dt>
  <!-- Sec='SECTION' Level=1 Label='' Line=' ' -->
  <dd>igi&gt; YSECTION myimage -2
  </dd>
  </dl>
  will add the columns of myimage and store the result in the Y plot buffer.
  [XY]SECTION saves the input file name string with the section
  specification in the X or Y axis label buffer.  This may be used with
  the [XY]LABEL command with no arguments to label the X or Y axis with
  the section.
  It is possible to use world coordinates from the input image as the X
  values corresponding to Y values read using YSECTION if the appropriate
  parameters exist in the image header.  By default, these coordinates
  will not be used and you must supply the appropriate independent
  variable as the X values.  However, if you use the IMGWCS command and
  the image contains the appropriate transformation parameters, then
  YSECTION will automatically fill in the X plot buffer with the
  coordinate values.
  Note that in general this works only for inherently one-dimensional
  data, e.g., spectra.  For 2-D data such as images, coordinates are
  rather meaningless for an arbitrary 1-D section of the image.  You will
  get an "</span>identity<span style="font-family: monospace;">" vector if the coordinate parameters are not present
  in the image.  That is, the X values will be the element number of the
  extracted pixels.  This is not exactly the same result as not using the
  WCS, since the coordinate transformation is applied to the image
  section.  That is, the returned coordinates are the coordinates with
  respect to the original full image, not the extracted piece.  For
  example, if you use:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='SECTION' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; imgwcs
  igi&gt; ysection dev$pix[10,50,1]
  </pre></div>
  </dd>
  </dl>
  the range of the X values will be 10 to 50 rather than 1 to 41 if you
  do not use IMGWCS and do not otherwise fill in the X vector.  Even if
  the image does not contain a WCS transformation, YSECTION will provide
  an X vector that corresponds to the pixel numbers in the full input
  image.
  WARNING:  This command, if used with IMGWCS, will modify the contents
  of the X plot buffer (see above).
  This command is saved in the command buffer.
  </section>
  <section id="s_show">
  <h3>Show</h3>
  no arguments
  Print the plot limits and attributes using the IRAF page facility.
  </section>
  <section id="s_step">
  <h3>Step</h3>
  no arguments
  Draw a stepped curve, i.e., a histogram or bar graph without vertical
  lines, through the current data values.
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_ticksize">
  <h3>Ticksize</h3>
  Arguments:  TICKSIZE minorx majorx minory majory
  Set the intervals in WC for tick marks on the X and Y axes drawn by BOX.
  The arguments minor[xy] specify the spacing for minor (small, unlabeled)
  ticks;  major[xy] specify the spacing for major (large, optionally
  labeled) ticks.  If minor[xy] &lt; 0, the axis will have logarithmic tick 
  spacing with major ticks at each decade and minor ticks at each integer.
  See BOX for drawing the axes and NOTATION for specifying labels.  See 
  AXIS for drawing an arbitrary axis.
  This command is saved in the command buffer.
  </section>
  <section id="s_title">
  <h3>Title</h3>
  Arguments:  TITLE text
  Draw text centered above the top X (horizontal) axis.  The text escape
  characters may be used to specify different fonts, superscripts and
  subscripts (See LABEL). 
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_ullim">
  <h3>Ullim</h3>
  no arguments
  Draw a limit symbol (an arrow) to indicate upper or lower limits.  The
  base of the arrow is drawn at the coordinates in the X and Y columns. 
  If no X data are specified, the X coordinate is the element number.  The
  direction of the arrow depends on the value in the limits column. 
  Values less than zero indicate lower limits and result in an upward
  arrow.  Values greater than zero indicate upper limits and result in an
  downward arrow.  The current size determines the size of the arrow.
  See the DATA, XCOLUMN, YCOLUMN, LCOLUMN commands.  See the ERRORBAR and
  ETYPE commands for drawing error bars and an alternate way of drawing
  upper or lower limit symbols.
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_undo">
  <h3>Undo</h3>
  no arguments
  Selectively erase the result of the last command that produced plotted 
  output.  This command will not restore the same figure if called again.
  Note that this only works if the device supports erasing vectors.
  </section>
  <section id="s_version">
  <h3>Version</h3>
  No arguments
  Show the current igi version and date of its initial installation.
  This information is also printed in the initial prompt when starting
  igi in an interactive session, in the first line of the result of the
  SHOW command and in the text written to the plot using the ID command.
  For example:
  "</span>Version 3.6 13 July 1993<span style="font-family: monospace;">"
  </section>
  <section id="s_vdraw_">
  <h3>Vdraw </h3>
  Arguments:  VDRAW xpos ypos
  Draw a line in the current line style from the current position to the
  virtual page coordinates (VPC) specified by the two floaing point
  parameters.  The ending point of the line becomes the new current
  position. If "</span>:VDRAW<span style="font-family: monospace;">" is used in cursor mode, xpos and ypos are ignored
  and should be omitted. 
  See DRAW to draw in WC and DDRAW to draw in NDC.
  This command is saved in the command buffer.
  </section>
  <section id="s_vmove">
  <h3>Vmove</h3>
  Arguments:  VMOVE xpos ypos
  Pen up move, i.e., change the current position to the virtual page
  coordinates (VPC) specified by the two floating point parameters.  This
  is an alias for VRELOCATE. 
  If "</span>:VMOVE<span style="font-family: monospace;">" is used in cursor mode, xpos and ypos are ignored and should
  be omitted.  In fact, it is unnecessary to use any move command in
  cursor mode.  Issuing any command or request for readback resets the
  current position to the coordinates of the cursor. 
  See VDRAW to draw in VPC, MOVE to move in WC, and DMOVE to move in NDC. 
  This command is saved in the command buffer.
  </section>
  <section id="s_vpage">
  <h3>Vpage</h3>
  Arguments:  VPAGE [left right bottom top]
  Specify the edges of the virtual page on the plotting area of the 
  device as a fraction of the width and height.  For example, to use only 
  the upper left corner of the frame, use VPAGE 0.5 1.0 0.5 1.0.  The 
  default is the entire plot area.  This does not change the relative 
  location of the axes on this page (see LOCATION). 
  See PHYSICAL to specify the page in device coordinates (inches). 
  This command is saved in the command buffer.
  </section>
  <section id="s_vrelocate_">
  <h3>Vrelocate </h3>
  Arguments:  VRELOCATE xpos ypos
  Pen up move, i.e., change the current position to the virtual page
  coordinates (VPC) specified by the two floating point parameters.  If
  "</span>:VRELOCATE<span style="font-family: monospace;">" is used in cursor mode, xpos and ypos are ignored and
  should be omitted.  In fact, it is unnecessary to use any move command
  in cursor mode.  Issuing any command or request for readback resets the
  current position to the coordinates of the cursor. 
  See VDRAW to draw in VPC, RELOCATE to move in WC, and DRELOCATE to move
  in NDC. 
  This command is saved in the command buffer.
  </section>
  <section id="s_wcslab">
  <h3>Wcslab</h3>
  Arguments:  WCSLAB [edit]
  Label the currently specified viewport with WCS, including equatorial
  (celestial) coordinates as with the ST4GEM stplot.wcslab task.
  The optional command argument is a string that begins with "</span>e<span style="font-family: monospace;">" or "</span>E<span style="font-family: monospace;">".
  This allows editing wlpars parameter set for specifying attributes via
  eparam.
  If the ZSECTION command was used to read an image section into the Z
  buffer, then the WCS attributes of that image are used in labeling the
  plot.  Otherwise, the WCS is taken from parameters in the wcspars
  pset.
  Note that the psets may be edited before entering igi by explicitly
  assigning parameter values or by using eparam at the cl prompt.  In
  addition, the parameter values may be assigned or the psets edited from
  igi using the "</span>!<span style="font-family: monospace;">" escape before using the WCSLAB command.
  WARNING:  Some of the attributes specified in the wlpars pset conflict
  with attributes set using igi commands, such as text size and color.
  Currently, the wlpars parmaeters take precedence over any igi
  attributes.
  </section>
  <section id="s_window_">
  <h3>Window </h3>
  Arguments:  WINDOW [nx ny] [pane]
  Divide the device plotting area into nx by ny windows (tiles or panes)
  and select the pane in which to plot, numbered left to right, bottom to
  top.  For example, WINDOW 3 3 3 will create nine panes and select the
  bottom right pane for subsequent plotting.  If only two arguments are
  given, the current pane number is selected, but with a different
  division.  If only one argument is given, a different pane is selected
  in the same tiling.  WINDOW is an alternative to PHYSICAL or VPAGE to
  specify the virtual page on the device.
  This command is saved in the command buffer.
  </section>
  <section id="s_write_">
  <h3>Write </h3>
  Arguments:  WRITE filename
  Write the command buffer to the file specified by the filename
  parameter. 
  </section>
  <section id="s_xcolumn_">
  <h3>Xcolumn </h3>
  Arguments:  XCOLUMN column
  Read X coordinate data from the specified column in the current input
  data file.  If the file is a text file, the column number must be an
  integer.  If no X data are specified, the Y data are plotted against row
  number.  If the file is an ST4GEM or FITS table, the column name must be a
  string.  Note that table column names are case-sensitive and may not be 
  abbreviated.
  See DATA to specify the input file (table) name.
  This command is saved in the command buffer.
  </section>
  <section id="s_xevaluate">
  <h3>Xevaluate</h3>
  Arguments:  XEVALUATE expression
  Replace the X plot data vector by the result of the expression in the
  string argument.  Typical expression syntax may be used to specify
  operators:  +, -, *, /, **, and common functions:  sqrt, sin, cos, log,
  log10, exp, etc.  The current value of any of the four plot vectors is
  specified by the single character:  x, y, e, or p, the element number
  may be specified by r, and the number of elements in the vector by n.
  For example, XEVALUATE log10(r**2) will replace each X value by the
  logarithm of the square of the element number.  The X array may operate
  on itself. 
  This command is saved in the command buffer.
  </section>
  <section id="s_xflip">
  <h3>Xflip</h3>
  no arguments
  Flip the X axis.  That is, plot horizontal data and axis labels 
  increasing right to left instead of the default left to right.  This 
  must be used before the axes are drawn (BOX) for the plot to scale 
  to match the data.  This is equivalent to specifying LIMITS with the
  lower and upper X limits reversed, but operates on the currently set
  limits, whether set manually or automatically.
  XFLIP should be used _after_ LIMITS.  XFLIP only modifies whatever is
  the currently set scaling.  Using LIMITS after XFLIP will nullify the
  flip by resetting the scale to whatever is specified in the LIMITS
  command.
  This command is saved in the command buffer.
  </section>
  <section id="s_xlabel_">
  <h3>Xlabel </h3>
  Arguments:  XLABEL [text]
  Draw text centered below the bottom X (horizontal) axis.  The text
  escape characters may be used to specify different fonts, superscripts
  and subscripts (See LABEL).  If the optional argument is missing, igi
  uses an internal string.  This is filled by the DATA and XCOLUMN
  commands.  If the DATA command specifies a binary ST4GEM table, then
  the XCOLUMN command appends the column name to the string.
  Note that the label may not appear if the edge of the viewport (the
  axes) falls too close to the edge of the (virtual) page.  Use LOCATION
  to change the placement of the viewport.
  This command is saved in the command buffer.  The results of this
  command may be erased with UNDO. 
  </section>
  <section id="s_xlogarithm">
  <h3>Xlogarithm</h3>
  no arguments
  Take the common logarithm of the X data values.  If any value is less
  than or equal to zero, the result is made INDEF, causing that point to
  be ignored in scaling and plotting.  See XEVALUATE for an alternate way
  of doing this.  You must use [XY]LOGARITHM for ERROBAR to work
  correctly on log data.
  This command is saved in the command buffer.
  </section>
  <section id="s_xsection">
  <h3>Xsection</h3>
  Arguments:  XSECTION image project
  Read an IRAF (OIF, or STF) image as the X column values.  The image may
  be of any dimensionality and data type.  The image name may include an
  image section specification that might be a subraster of the image or
  may include a group number.  By default, all of the image section
  pixels are read as a one-dimensional array into the specified igi
  vector.  There is no capability to draw any multi-dimensional plots or
  gray scale images.
  XSECTION overrides the use of the DATA and XCOLUMN
  commands in filling the X data array.  One array may be filled with an
  image and another by a table column using DATA and [XYEPLS]COLUMN, yet
  another from a text file, also using DATA and [XYEPLS]COLUMN.
  By default, multi-dimensional data are read pixel by pixel, line
  by line, plane by plane, and so forth.  For example, a 2-D image
  is read from left to right along each line from the bottom to the
  top.  Optionally, a multi-dimensional section may be reduced to a
  single dimension by averaging or summing all of the image lines
  into a single vector the size of the lines in the image section.
  The second, optional argument to the XSECTION command is an
  integer which indicates that the section should be summed or
  averaged along an image axis.  The absolute value specifies along
  which axis to collapse the section.  Positive integers cause
  vectors to be averaged, negative integers cause successive vectors
  to be added.
  For example, the command:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='XSECTION' Level=1 Label='' Line=' ' -->
  <dd>igi&gt; XSECTION myimage[1:10,1:10]
  </dd>
  </dl>
  will read 100 pixels from the lower left corner of myimage into the X
  buffer.  The command:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='XSECTION' Level=1 Label='' Line=' ' -->
  <dd>igi&gt; XSECTION myimage 1
  </dd>
  </dl>
  will read read all of the pixels but will store the average of all of
  the image lines in the X buffer.
  <dl>
  <dt><b></b></dt>
  <!-- Sec='XSECTION' Level=1 Label='' Line=' ' -->
  <dd>igi&gt; XSECTION myimage -2
  </dd>
  </dl>
  will read read all of the pixels but will store the sum of all of
  the image columns in the X buffer.
  XSECTION saves the input file name string with the section specification
  in the X axis label buffer.  This may be used with the XLABEL command
  with no arguments to label the X axis with the section.
  This command is saved in the command buffer.
  </section>
  <section id="s_ycolumn_">
  <h3>Ycolumn </h3>
  Arguments:  YCOLUMN column
  Read Y coordinate data from the specified column in the current input
  data file.  If the file is a text file, the column number must be an
  integer.  If the file is an ST4GEM or FITS table, the column name must be a
  string. Note that table column names are case-sensitive and may not be
  abbreviated.  If no X data are specified, the Y data are plotted against
  row number. 
  See DATA to specify the input file (table) name.
  This command is saved in the command buffer.
  </section>
  <section id="s_yevaluate">
  <h3>Yevaluate</h3>
  Arguments:  YEVALUATE expression
  Replace the Y data vector by the result of the expression in the string
  argument.  Typical expression syntax may be used to specify operators:
  +, -, *, /, **, and common functions:  sqrt, sin, cos, log, log10, exp,
  etc.  The current value of any of the four plot data vectors is
  specified by the single (case-insensitive) character:  x, y, e, or p,
  the element number may be specified by r, and the number of elements in
  the vector by n.  For example, YEVALUATE log10(r**2) will replace each Y
  value by the log of the square of the element number.  An array may
  operate on itself. 
  This command is saved in the command buffer.
  </section>
  <section id="s_yflip">
  <h3>Yflip</h3>
  no arguments
  Flip the Y axis.  That is, plot vertical data and axis labels 
  increasing top to bottom instead of the default bottom to top.  This 
  must be used before the axes are drawn (BOX) for the plot to scale 
  correctly.  This is equivalent to specifying LIMITS with the
  lower and upper Y limits reversed, but operates on the currently set
  limits, whether set manually or automatically.
  YFLIP should be used _after_ LIMITS.  YFLIP only modifies whatever is
  the currently set scaling.  Using LIMITS after YFLIP will nullify the
  flip by resetting the scale to whatever is specified in the LIMITS
  command.
  This command is saved in the command buffer.
  </section>
  <section id="s_ylabel">
  <h3>Ylabel</h3>
  Arguments:  YLABEL [text]
  Draw text centered left of the left Y (vertical) axis.  The text escape
  characters may be used to specify different fonts, superscripts and
  subscripts (See LABEL).  If the optional argument is missing, igi uses
  an internal string.  This is filled by the DATA and YCOLUMN commands.
  If the DATA command specifies a binary ST4GEM table, then the YCOLUMN
  command appends the column name to the string.
  This command is saved in the command buffer.
  </section>
  <section id="s_ylogarithm">
  <h3>Ylogarithm</h3>
  no arguments
  Take the common logarithm of the Y data values.  If any value is less
  than or equal to zero, the result is made INDEF, causing that point to
  be ignored in scaling and plotting.  See YEVALUATE for an alternate way
  of doing this.  You must use [XY]LOGARITHM for ERROBAR to work
  correctly on log data.
  This command is saved in the command buffer.
  </section>
  <section id="s_ysection">
  <h3>Ysection</h3>
  Arguments:  YSECTION image project
  Read an IRAF (OIF, or STF) image as the Y column values.  The image may
  be of any dimensionality and data type.  The image name may include an
  image section specification that might be a subraster of the image or
  may include a group number.  By default, all of the image section
  pixels are read as a one-dimensional array into the specified igi
  vector.  There is no capability to draw any multi-dimensional plots or
  gray scale images.
  YSECTION overrides the use of the DATA and YCOLUMN
  commands in filling the Y data array.  One array may be filled with an
  image and another by a table column using DATA and [XYEPLS]COLUMN, yet
  another from a text file, also using DATA and [XYEPLS]COLUMN.
  By default, multi-dimensional data are read pixel by pixel, line
  by line, plane by plane, and so forth.  For example, a 2-D image
  is read from left to right along each line from the bottom to the
  top.  Optionally, a multi-dimensional section may be reduced to a
  single dimension by averaging or summing all of the image lines
  into a single vector the size of the lines in the image section.
  The second, optional argument to the YSECTION command is an
  integer which indicates that the section should be summed or
  averaged along an image axis.  The absolute value specifies along
  which axis to collapse the section.  Positive integers cause
  vectors to be averaged, negative integers cause successive vectors
  to be added.
  For example, the command:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='YSECTION' Level=1 Label='' Line=' ' -->
  <dd>igi&gt; YSECTION myimage[1:10,1:10]
  </dd>
  </dl>
  will read 100 pixels from the lower left corner of myimage into the Y
  buffer.  The command:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='YSECTION' Level=1 Label='' Line=' ' -->
  <dd>igi&gt; YSECTION myimage 1
  </dd>
  </dl>
  will read read all of the pixels but will store the average of all of
  the image lines in the Y buffer.
  <dl>
  <dt><b></b></dt>
  <!-- Sec='YSECTION' Level=1 Label='' Line=' ' -->
  <dd>igi&gt; YSECTION myimage -2
  </dd>
  </dl>
  will read read all of the pixels but will store the sum of all of
  the image columns in the Y buffer.
  YSECTION saves the input file name string with the section specification
  in the Y axis label buffer.  This may be used with the YLABEL command
  with no arguments to label the Y axis with the section.
  It is possible to use world coordinates from the input image as the X
  values corresponding to Y values read using YSECTION if the appropriate
  parameters exist in the image header.  By default, these coordinates
  will not be used and you must supply the appropriate independent
  variable as the X values.  However, if you use the IMGWCS command and
  the image contains the appropriate transformation parameters, then
  YSECTION will automatically fill in the X plot buffer with the
  coordinate values.
  Note that in general this works only for inherently one-dimensional
  data, e.g., spectra.  For 2-D data such as images, coordinates are
  rather meaningless for an arbitrary 1-D section of the image.  You will
  get an "</span>identity<span style="font-family: monospace;">" vector if the coordinate parameters are not present
  in the image.  That is, the X values will be the element number of the
  extracted pixels.  This is not exactly the same result as not using the
  WCS, since the coordinate transformation is applied to the image
  section.  That is, the returned coordinates are the coordinates with
  respect to the original full image, not the extracted piece.  For
  example, if you use:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='YSECTION' Level=1 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; imgwcs
  igi&gt; ysection dev$pix[10,50,1]
  
  </pre></div>
  </dd>
  </dl>
  the range of the X values will be 10 to 50 rather than 1 to 41 if you
  do not use IMGWCS and do not otherwise fill in the X vector.  Even if
  the image does not contain a WCS transformation, YSECTION will provide
  an X vector that corresponds to the pixel numbers in the full input
  image.
  WARNING:  This command, if used with IMGWCS, will modify the contents
  of the X plot buffer (see above).
  This command is saved in the command buffer.
  </section>
  <section id="s_zevaluate">
  <h3>Zevaluate</h3>
  Arguments:  ZEVALUATE expression
  Replace the Z data (raster) buffer by the result of the expression in
  the string argument.  Typical expression syntax may be used to specify
  operators:  +, -, *, /, **, and common functions:  sqrt, sin, cos, log,
  log10, exp, etc.  The current value of any of the four plot data
  vectors is specified by the single (case-insensitive) character:  x, y,
  z, e, or p, the element number may be specified by r, and the number of
  elements in the vector by n.  For example, ZEVALUATE log10(z) will
  replace each Z value by the log of the square of the original value.
  This command is saved in the command buffer.
  </section>
  <section id="s_zrange">
  <h3>Zrange</h3>
  Arguments:  ZRANGE [min max]
  Specify the minimum and maximum image pixel values that map to the
  darkest and brightest display values.  Using no arguments indicates to
  use the range of values in the image data.  In fact, min may be greater
  than max, which will result in the lower-valued pixels rendered
  brighter than the higher-valued pixel -- a negative image.
  </section>
  <section id="s_zsection">
  <h3>Zsection</h3>
  Arguments:  ZSECTION section
  Read an image section (one- or two-dimensional) into the Z buffer.
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  [XYEPLS]EVALUATE does not recognize INDEF values and therefore either
  will crash, or the evaluated column will contain strange values. 
  Not all errors are trapped.  For example, using "</span>!<span style="font-family: monospace;">" to execute a cl 
  command resulting in an error condition will cause igi to abort.
  An extra prompt is printed after a macro is defined (DEFINE) in cursor
  mode (CURSES) and after UNDO.
  UNDO does not erase lines drawn by [ DV]DRAW.
  Error bars are not drawn correctly if [XY]EVALUATE is used to take the 
  logarithm of the data.
  Macros are limited to a relatively small number of commands (something like a dozen or so in practice) because of an inherent internal buffer size limit.
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  The examples fall in two groups.  The first simply shows different ways
  to run the task, interactively or by using input command files and some
  device options.  This is analagous to the usual IRAF/ST4GEM tasks.  The
  larger section shows some specific examples of using igi commands to
  build plots and manage the interaction.  These are examples of the
  unique igi "</span>mini-language.<span style="font-family: monospace;">"
  <dl>
  <dt><b>Running the task</b></dt>
  <!-- Sec='EXAMPLES' Level=1 Label='Running' Line='Running the task' -->
  <dd>There is potentially an infinite number of possible examples of command
  interaction and plotting, of course.  The following attempts to offer
  some common, simple examples of basic plots and demonstrations of some
  of the unique capabilities of igi.  These may be used as templates on
  which to begin building more complete, useful and complex graphics.
  1. Start the interpreter, reading commands from STDIN and displaying 
  graphics output on the standard graphics device: 
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd>pl&gt; igi
  </dd>
  </dl>
  2. Interpret the commands in the file cmd.igi and direct the output to 
  a hardcopy device:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd>pl&gt; igi &lt; cmd.igi dev=stdplot
  </dd>
  </dl>
  In this case, there will be no user interaction.  The task will 
  terminate on encountering the end of the file cmd.igi.
  4. Interpret commands interactively and write the plot instructions to the 
  metacode file igi.vdm but use the device characteristics of a Pericom 
  terminal:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd>pl&gt; igi &gt;G igi.vdm device=pericom
  </dd>
  </dl>
  In this case, command interaction will occur in the text screen and no
  graphics will be drawn.  To display the graphics, you might use the stdgraph task in the plot package.
  5. Combine igi graphics with other IRAF graphics tasks.  In the first
  example, run igi first and then append the additional grpahics.  In the
  second example, run the stplot.newcont task and then append additional
  graphics using igi.  This will work for both terminal/window display as
  well as hardcopy plots.  Note that to properly append graphics, do not
  use gflush between the tasks.  Afterwards, you may use gflush to
  dispose of the plot to a printer.
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  pl&gt; igi &lt; cmd.igi
  pl&gt; newcont image append+
  
  pl&gt; newcont image
  pl&gt; igi &lt; cmd.igi append+
  </pre></div>
  </dd>
  </dl>
  In the particular case of PostScript output to a file, if you wish to
  create a single file but plot on separate frames (pages), you must use
  "</span>append=yes<span style="font-family: monospace;">" for the second and subsequent plots.  To create a new
  frame, use the igi ERASE command.
  </dd>
  </dl>
  <dl>
  <dt><b>Command Interaction</b></dt>
  <!-- Sec='EXAMPLES' Level=1 Label='Command' Line='Command Interaction' -->
  <dd>The following are examples of igi interactions.  That is, the commands
  typed interactively after starting up the igi task.  The prompt ("</span>igi&gt;
  <span style="font-family: monospace;">") is written by igi and the remainder of the line is what would be
  typed by the user.  These are all fairly simple examples that
  demonstrate some of the basic means of drawing plots.  Some of the more
  common kinds of things are demonstrated, with some of the more subtle
  tricks pointed out.
  1. Read data from a text file, scale the plot, draw the axes, and draw the
  curve:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; data igi.dat
  igi&gt; xcolumn 1;  ycolumn 2
  igi&gt; limits
  igi&gt; box;  connect
  </pre></div>
  </dd>
  </dl>
  Note the multiple commands on a line, separated by "</span>;<span style="font-family: monospace;">".
  2. Change the above to plot on an log-log scale:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; data igi.dat
  igi&gt; xcolumn 1;  ycolumn 2
  igi&gt; xlogarithm;  ylogarithm
  igi&gt; limits
  igi&gt; ticksize -1 0 -1 0
  igi&gt; box; connect
  </pre></div>
  </dd>
  </dl>
  3. Read data from a table, scale the plot, draw the axes, and draw
  the curve as the Y elements versus row number: 
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; data table;  ycolumn ycol
  igi&gt; limits;  box;  connect
  </pre></div>
  </dd>
  </dl>
  4. Read data from the third row of FITS table which has an array for
  each cell of a column, scale the plot, draw the axes, and draw the
  curve:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; data table.fits[1]
  igi&gt; xcolumn wavelength 3; ycolumn flux
  igi&gt; limits; box; connect
  </pre></div>
  </dd>
  </dl>
  5.  Using a row selector, choose a range of rows to be plotted from a
  FITS table which has an array for each cell of a column.  The 'column'
  command will then be used to read the data from each row in succession,
  since the row number given will be relative to the rows specified in
  the row selector. Next, scale the plot to the range of the first row's
  data, draw the axes,  plot each curve with a different line style, then
  reset the line style to default:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; data table.fits[1][r:sporder=10:12]
  igi&gt; xcolumn wavelength 1; ycolumn flux
  igi&gt; limits; box; connect
  igi&gt; xcolumn wavelength 2; ycolumn flux; ltype 1; connect
  igi&gt; xcolumn wavlength 3; ycolumn flux; ltype 2; connect
  igi&gt; ltype 0
  </pre></div>
  </dd>
  </dl>
  6. Define a macro named "</span>simple<span style="font-family: monospace;">" to scale and draw a plot and invoke the 
  macro:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; define simple
  macro&gt; data &amp;1
  macro&gt; xcolumn &amp;2; ycolumn &amp;3
  macro&gt; limits; box; connect
  macro&gt; end
  igi&gt; simple igi.dat 1 2
  igi&gt; erase
  igi&gt; simple igi.dat 3 4
  </pre></div>
  </dd>
  </dl>
  7. Print a vertical label (in italics with a special character)
  centered at the current pen position twice the default character size.
  Note the FONTSET command to ensure that igi recognizes the text escapes
  and special characters.
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; expand 2; angle 90; justify 5
  igi&gt; fontset igi
  igi&gt; label \\iWavelength (\gVngstroms)
  </pre></div>
  </dd>
  </dl>
  8. Draw a curve and superimpose symmetrical error bars in the Y data.
  Note that the error values are read with the ECOLUMN command and you
  need to call ERRORBAR twice to get both halves of the symbols.
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; data tdat
  igi&gt; ycolumn 2
  igi&gt; ecolumn 3
  igi&gt; limits
  igi&gt; etype 1
  igi&gt; errorbar  2
  igi&gt; errorbar -2
  </pre></div>
  </dd>
  </dl>
  9. Plot two curves in separate windows (different axis grids), the data as
  read in one, and the log of the data in another:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; window 2 1 1
  igi&gt; limits; box; connect
  igi&gt; window 2
  igi&gt; yevaluate log10(y)
  igi&gt; limits; box; connect
  </pre></div>
  </dd>
  </dl>
  10. Assuming the image named specim contains two lines, one having
  wavelength values and the other intensities, the following would plot
  the spectrum as intensities versus wavelength:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; xsection specim[*,1]
  igi&gt; ysection specim[*,2]
  igi&gt; limits
  igi&gt; box
  igi&gt; connect
  </pre></div>
  </dd>
  </dl>
  a. Label the above plot with the input file names:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; xlabel
  igi&gt; ylabel
  </pre></div>
  </dd>
  </dl>
  11. Use coordinate information in an input image to fill in the X values:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  igi&gt; imgwcs
  igi&gt; ysection spect
  </pre></div>
  </dd>
  </dl>
  <br>
  <br>
  12. The following is an example of an igi command file it includes some
  comments describing what's going on.  Note that the data are totally
  fabricated random numbers and bear no intentional resemlance to any
  real observations or theory.  After the commands listing is the data
  file used as input.  This text could be saved to two text files and
  used as input to igi.
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  # Read data from the first 10 lines of file rand.dat
  data rand.dat;  lines 1 10
  
  # Read column 3 into the Y buffer and operate on it
  ycol 3;  yevaluate y/(r+10)
  
  # Scale the plot with a 4% margin
  limits;  margin 0.04
  
  # Draw data points
  expand 0.5;  ptype 4 3;  points
  
  # Read errors from column 3
  ecol 3
  eev sqrt(y)/5
  etype 1;  errorbar  2;  errorbar -2
  
  # Read the first 20 lines of column 2 into the Y buffer
  lines 1 20;  ycol 2
  yevaluate 1/(r+10)
  limits;  margin 0.04
  connect
  
  # Rescale and draw the axes
  limits 1 50 -1 4;  margin 0.04
  ticksize 1 10 -1 0;  notation 1e-4 1e5 2e-3 2e2
  expand 1.2;  box
  ltype 1;  grid
  
  # Draw the labels, note the embedded text formatting escapes
  xlabel "\\iSample Number"
  ylabel "\gx [\\i\gms \gV\\u-1\\d\\i]"
  title "\\iObserved versus Theoretical Bogus Data"
  </pre></div>
  </dd>
  </dl>
  Data input to the above example may be constructed by using the urand task in the IRAF utilities package.  The following command would create the file rand.dat used in the example:
  <dl>
  <dt><b></b></dt>
  <!-- Sec='EXAMPLES' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  urand 20 5 &gt; rand.dat
  </pre></div>
  </dd>
  </dl>
  13. Display images.  The following draws four windows with 2-D image
  sections in two and a 1-D image section in the others.
  <div class="highlight-default-notranslate"><pre>
  WINDOW 2 2 1
  ZSECTION "dev$pix[*:5,*:5]"
  FITPIX .25 .9 .15 .9
  LIMITS;  margin;  ZRANGE 80 250
  PIXMAP
  ticksize 5 20 5 20
  BOX
  title "Aspect Preserved"
  
  WINDOW 2;  LOCATION .1 .9 .15 .9
  ZRANGE 250 80
  PIXMAP
  
  # Line indicating 1-D cut
  move 0.5 41; draw 103.5 41
  
  # Draw a border only
  limits 0 1 0 1
  move 0 0;  draw 1 0;  draw 1 1;  draw 0 1; draw 0 0
  move .5 1.075;  putlabel 2 "Filled Viewport, Negative Map"
  
  # Widened 1-D section
  WINDOW 3;  LOCATION .1 .9 .2 .75
  ZSECTION "dev$pix[*:5,200]"
  LIMITS;  ZRANGE;  margin
  ticksize 2 10 10 10
  BOX 1 0
  title "1-D Image Section"
  PIXMAP
  
  #  Line plot of 1-D cut
  WINDOW 4;  LOCATION .1 .9 .1 .85
  YSECTION "dev$pix[*:5,200]"
  LIMITS;  margin
  ticksize 5 20 20 100
  BOX
  CONNECT
  </pre></div>
  </dd>
  </dl>
  <dl>
  <dt><b>Buffer Size modification</b></dt>
  <!-- Sec='EXAMPLES' Level=1 Label='Buffer' Line='Buffer Size modification' -->
  <dd>The following example shows how to modify the pushback buffer when a
  macro is too large for the default buffer size.
  <div class="highlight-default-notranslate"><pre>
  cl&gt; show igi_buflen
  0
  cl&gt; igi &lt; large_macro.igi
  ERROR: Pushback buffer overflow (recursive macro?) (STDIN)
  cl&gt; set igi_buflen=10000
  cl&gt; flprc
  cl&gt; igi &lt; large_macro.igi
  ...igi successfully runs
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_references">
  <h3>References</h3>
  Developed as an IRAF application by Zolt Levay, STScI.  The printed
  "</span>IGI Reference Manual<span style="font-family: monospace;">" is available.  It is an expanded version of this
  on-line help and includes figures and additional examples.
  The modifications to work with row selectors, cell arrays, and PostScript
  fonts were performed by Warren Hack.
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  cursor, plot
  
  </section>
  
  <!-- Contents: 'NAME' 'DESCRIPTION' 'NEW FEATURES' 'PARAMETERS' 'MENU' '!' '?' '^' 'ANGLE ' 'APROPOS' 'AXIS' 'BARGRAPH' 'BOX' 'BYE' 'COLOR' 'COLUMN' 'CONNECT' 'CURSES ' 'DATA ' 'DDRAW ' 'DEFINE' 'DLIST' 'DOT   ' 'DRAW ' 'DRELOCATE ' 'ECOLUMN ' 'EDITCMD' 'EEVALUATE' 'ELLIPSE ' 'END' 'ERASE' 'ERRORBAR' 'ETYPE' 'EVALUATE' 'EXPAND ' 'FILLPAT' 'FITPIX' 'FLIP' 'FMTICK' 'FONTSET ' 'GRID' 'HELP' 'HISTOGRAM' 'ID' 'IMGWCS' 'INPUT ' 'JUSTIFY' 'LABEL ' 'LCOLUMN' 'LIMITS ' 'LINES ' 'LIST' 'LOCATION ' 'LTYPE ' 'LWEIGHT ' 'MACROS' 'MARGIN' 'MINMAX' 'NOTATION' 'NUMBER' 'PAGECMD' 'PCOLUMN ' 'PDRAW ' 'PEVALUATE' 'PHYSICAL' 'PIXMAP' 'PLAYBACK' 'POINTS' 'POLYGON' 'PSCMD' 'PSFONT ' 'PTYPE ' 'PUTLABEL ' 'READ ' 'RELOCATE ' 'RESET' 'SCOLUMN' 'SAOCMAP' 'SECTION' 'SHOW' 'STEP' 'TICKSIZE' 'TITLE' 'ULLIM' 'UNDO' 'VERSION' 'VDRAW ' 'VMOVE' 'VPAGE' 'VRELOCATE ' 'WCSLAB' 'WINDOW ' 'WRITE ' 'XCOLUMN ' 'XEVALUATE' 'XFLIP' 'XLABEL ' 'XLOGARITHM' 'XSECTION' 'YCOLUMN ' 'YEVALUATE' 'YFLIP' 'YLABEL' 'YLOGARITHM' 'YSECTION' 'ZEVALUATE' 'ZRANGE' 'ZSECTION' 'BUGS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

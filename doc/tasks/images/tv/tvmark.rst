.. _tvmark:

tvmark: Mark objects on the image display
=========================================

**Package: tv**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tvmark frame coords
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_frame">
  <dt><b>frame</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='frame' Line='frame' -->
  <dd>The frame or image plane number of the display to be marked. 
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords ' -->
  <dd>The text file containing the coordinates of objects to be
  marked, one object per line with x and y in columns 1 and 2 respectively.
  An optional label may be read out of the third column.
  If <i>coords</i> = <span style="font-family: monospace;">""</span>, the coordinate file is undefined.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = ""' -->
  <dd>The text file in which image cursor commands typed in interactive mode
  are logged. If <i>logfile</i> = <span style="font-family: monospace;">""</span> no commands are logged.
  If automatic logging is enabled, all cursor commands
  are logged, otherwise the user must use the interactive keep keystroke
  command to select specific cursor commands for logging.
  Commands are not logged in non-interactive mode.
  </dd>
  </dl>
  <dl id="l_autolog">
  <dt><b>autolog = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='autolog' Line='autolog = no' -->
  <dd>Automatically log all cursor commands in interactive mode.
  </dd>
  </dl>
  <dl id="l_outimage">
  <dt><b>outimage = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outimage' Line='outimage = ""' -->
  <dd>The name of the output snapshot image.
  If tvmark is run in non-interactive mode and no command file is specified,
  a copy of the frame buffer
  is automatically written to the IRAF image <i>outimage</i> after tvmark
  terminates execution.
  If <i>outimage</i> = <span style="font-family: monospace;">""</span> no output image is written.
  In interactive mode or in non-interactive mode if a command file
  is specified, the user can make snapshots of the frame buffer
  with the interactive colon  write command.  In this case the name of the output
  snapped image will be in order of priority, the name specified
  by the user in the colon write ommand,  <span style="font-family: monospace;">"outimage.snap.version"</span>,  or,
  <span style="font-family: monospace;">"imagename.snap.version"</span>.
  </dd>
  </dl>
  <dl id="l_deletions">
  <dt><b>deletions = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='deletions' Line='deletions = ""' -->
  <dd>The extension of the output file containing objects which were deleted
  from the coordinate file in interactive or command file mode.
  By default no output deletions file is written.
  If <i>deletions</i> is not equal to the null string (<span style="font-family: monospace;">""</span>), then deleted
  objects are written to a file called <i>coords.deletions</i>. For
  example if <i>coords</i> = <span style="font-family: monospace;">"nite1"</span> and <i>deletions</i> = <span style="font-family: monospace;">"del"</span>, then the
  deletions file will be called <span style="font-family: monospace;">"nite1.del"</span>.
  </dd>
  </dl>
  <dl id="l_commands">
  <dt><b>commands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='commands' Line='commands = ""' -->
  <dd>The text file containing the marking commands.
  In interactive mode if <i>commands</i> = <span style="font-family: monospace;">""</span>, 
  <i>commands</i> is the image cursor.  In non-interactive mode
  cursor commands may be read from a text file, by setting <i>commands</i> =
  <span style="font-family: monospace;">"textfile"</span>.  This file may be a user
  created command file, or the <i>logfile</i> from a previous run of tvmark.
  If <i>commands</i> = <span style="font-family: monospace;">""</span> in non-interactive mode, the default mark is drawn
  on the display at the positions of all the objects in <i>coords</i>.
  </dd>
  </dl>
  <dl id="l_mark">
  <dt><b>mark = <span style="font-family: monospace;">"point"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mark' Line='mark = "point"' -->
  <dd>The default mark type.  The options are:
  <dl>
  <dt><b>point</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='point' Line='point' -->
  <dd>A point.  To ensure legibility <i>point</i> is actually a square dot whose
  size is specified by <i>pointsize</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>plus</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='plus' Line='plus' -->
  <dd>A plus sign.  The shape of the plus sign is determined by the raster font
  and its size is specified by <i>txsize</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>cross</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='cross' Line='cross' -->
  <dd>An x.  The shape of the x is determined by the raster font and its size is
  is specified by <i>txsize</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>circle</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='circle' Line='circle' -->
  <dd>A set of concentric circles whose radii are specified by the <i>radii</i>
  parameter.  The radii are in image pixel units.  If the magnifications
  used by display are not equal in x and y circles will become ellipses
  when drawn.
  </dd>
  </dl>
  <dl>
  <dt><b>rectangle</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='rectangle' Line='rectangle' -->
  <dd>A set of concentric rectangles whose lengths and width/length ratio are
  specified by the <i>lengths</i> parameter.  The lengths are specified in
  image pixel units.  If the magnifications used by the display are not
  equal in x and y then squares will become rectangles when drawn.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_radii">
  <dt><b>radii = <span style="font-family: monospace;">"0"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radii' Line='radii = "0"' -->
  <dd>If the default mark type is <span style="font-family: monospace;">"circle"</span> than concentric circles of radii
  <span style="font-family: monospace;">"r1,r2,...rN"</span> are drawn around each selected point.
  </dd>
  </dl>
  <dl id="l_lengths">
  <dt><b>lengths = <span style="font-family: monospace;">"0"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lengths' Line='lengths = "0"' -->
  <dd>if the default mark type is <span style="font-family: monospace;">"rectangle"</span> then concentric rectangles of
  length and width / length ratio <span style="font-family: monospace;">"l1,l2,...lN ratio"</span> are drawn around
  each selected point.  If ratio is not supplied, it defaults to 1.0
  and squares are drawn.
  </dd>
  </dl>
  <dl id="l_font">
  <dt><b>font = <span style="font-family: monospace;">"raster"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='font' Line='font = "raster"' -->
  <dd>The name of the font.  At present only a simple raster font is supported.
  </dd>
  </dl>
  <dl id="l_color">
  <dt><b>color = 255</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='color' Line='color = 255' -->
  <dd>The numerical value or  color of the marks drawn.
  Any number between 0 and 255 may be specified.
  The meaning of the color is device dependent.
  In the current version of the Sun/IRAF IMTOOL numbers between 202
  and 217 may be used to display graphics colors.  The current color
  assignments for IMTOOL are summarized later in this help page.
  </dd>
  </dl>
  <dl id="l_label">
  <dt><b>label = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='label' Line='label = no' -->
  <dd>Label the marked coordinates with the string in the third column of
  the text file <i>coords</i>.  <i>label</i> overrides <i>number</i>.
  </dd>
  </dl>
  <dl id="l_number">
  <dt><b>number = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='number' Line='number = no' -->
  <dd>Label the marked objects with their sequence number in the coordinate
  list <i>coords</i>.
  </dd>
  </dl>
  <dl id="l_nxoffset">
  <dt><b>nxoffset = 0, nyoffset = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxoffset' Line='nxoffset = 0, nyoffset = 0' -->
  <dd>The x and y offset in display pixels of the numbers to be drawn.
  Numbers are drawn by default with the lower left corner of the first
  digit at the coordinate list position.
  </dd>
  </dl>
  <dl id="l_pointsize">
  <dt><b>pointsize = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pointsize' Line='pointsize = 3' -->
  <dd>The size of the default mark type <span style="font-family: monospace;">"point"</span>. Point size will be rounded up
  to the nearest odd number.
  </dd>
  </dl>
  <dl id="l_txsize">
  <dt><b>txsize = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='txsize' Line='txsize = 1' -->
  <dd>The size of text, numbers and the plus and cross marks to be written.
  The size is in font units which are 6 display pixels wide and 7 display 
  pixels high.
  </dd>
  </dl>
  <dl id="l_tolerance">
  <dt><b>tolerance = 1.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tolerance' Line='tolerance = 1.5' -->
  <dd>Objects marked by the cursor for deletion from the coordinate list
  <i>coords</i> must be less than or equal to <i>tolerance</i> pixels
  from the cursor position to be deleted. If 1 or more objects
  is closer than <i>tolerance</i>, the closest object is deleted.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Interactive mode.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  TVMARK marks objects on the display by writing directly into
  the frame buffer specified by <i>frame</i>.  TVMARK can draw on
  any devices supported by the IRAF <i>display</i> program.
  After marking, the
  contents of the frame buffer may be written out to the IRAF image
  <i>outimage</i>.  The output image is equal in size and intensity
  to the contents of the frame buffer displayed at the time of writing.
  </p>
  <p>
  In interactive mode objects to be marked may be selected interactively
  using the image cursor or read from the text file <i>coords</i>.
  Objects in the coordinate list
  may be selected individually by number,
  in groups by specifying a range of numbers, or the entire list may
  be read.  New objects may be added to the list interactively
  using the append keystroke command.  In batch mode cursor commands
  may be read from a text file by setting <i>commands</i> to the name
  of the text file.  This may be a user created file of cursor
  commands or a log file from a previous interactive run of TVMARK.
  If no command file is specified then all the objects in the coordinate
  list are marked with the default mark type /fImark/fR.
  </p>
  <p>
  The mark commands entered in interactive mode can be saved in the text
  file <i>logfile</i>.  If <i>autolog</i>
  is enabled and <i>logfile</i> is defined all cursor commands
  are automatically logged.  If <i>autolog</i> is turned off then the user
  can select which commands are to be logged interactively using the
  interactive keep keystroke.
  </p>
  <p>
  The default mark type are currently <span style="font-family: monospace;">"none"</span>, <span style="font-family: monospace;">"point"</span>, <span style="font-family: monospace;">"plus"</span>, <span style="font-family: monospace;">"cross"</span>,
  <span style="font-family: monospace;">"circle"</span>, a
  list of concentric circles, and <span style="font-family: monospace;">"rectangles"</span>, a list of concentric rectangles.
  The size of the <span style="font-family: monospace;">"point"</span> mark is set using the parameter <i>pointsize</i>
  while the sizes of the <span style="font-family: monospace;">"plus"</span> and <span style="font-family: monospace;">"cross"</span> mark types are set by the
  <i>txsize</i> parameter.  Txsize is in font units which for the simple raster
  font currently implemented is six display pixels in x and seven display 
  pixels in y.
  The <i>radii</i> and <i>lengths</i> parameters
  describe the concentric circles and concentric rectangles to be drawn
  respectively.
  If <i>number=yes</i> then objects in the coordinate list will be automatically
  numbered as well as marked.  The position of the number can be altered
  with the <i>nxoffset</i> and <i>nyoffset</i> parameters.
  </p>
  <p>
  In interactive mode tvmark maintains a scratch buffer.  The user opens
  the scratch buffer by issuing a save command which saves the current
  contents of the frame buffer in a temporary IRAF image.
  The user can continue marking and if unsatisfied with the results
  restore the last saved copy of the frame buffer with the restore
  command. Subsections of the saved frame buffer can be restored to the
  current frame buffer with the erase keystroke command.
  Finally a snapshot of the frame buffer can be saved permanently by
  using the write command. These snapped images can be redisplayed
  by setting the display task parameter <i>ztrans</i> = <span style="font-family: monospace;">"none"</span>.
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <div class="highlight-default-notranslate"><pre>
                Interactive TVMARK Keystroke/Colon Commands
  
  The following keystroke commands are available.
  
      ?       Print help
      +       Mark the cursor position with +
      x       Mark the cursor position with x
      .       Mark the cursor position with a dot
      c       Draw defined concentric circles around the cursor position
      r       Draw defined concentric rectangles around the cursor position
      s       Draw line segments, 2 keystrokes
      v       Draw a circle, 2 keystrokes
      b       Draw a rectangle, 2 keystrokes
      f       Draw filled rectangle, 2 keystrokes
      e       Mark region to be erased and restored, 2 keystrokes
  
      -       Move to previous object in the coordinate list
      m       Move to next object in the coordinate list
      p       Mark the previous object in the coordinate list
      n       Mark next object in the coordinate list
      l       Mark all the objects in the coordinate list
      o       Rewind the coordinate list
      a       Append object at cursor position to coordinate list and mark
      d       Delete object nearest the cursor position in the coordinate list
              and mark
  
      k       Keep last cursor command
      q       Exit tvmark
  
  The following colon commands are available.
  
     :show                     List the tvmark parameters
     :move N                   Move to Nth object in coordinate list
     :next N M                 Mark objects N to M in coordinate list
     :text      [string]       Write text at the cursor position
     :save                     Save the current contents of frame buffer
     :restore                  Restore last saved frame buffer
     :write     [imagename]    Write the contents of frame buffer to an image
  
  The following parameters can be shown or set with colon commands.
  
     :frame             [number]
     :outimage          [imagename]
     :coords            [filename]
     :logfile           [filename]
     :autolog           [yes/no]
     :mark              [point|line|circle|rectangle|cross|plus]
     :radii             [r1,...,rN]
     :lengths           [l1,...,lN] [width]
     :font              [raster]
     :color             [number]
     :number            [yes/no]
     :label             [yes/no]
     :txsize            [1,2,..]
     :pointsize         [1,3,5...]
  </pre></div>
  </section>
  <section id="s_current_imtool_colors">
  <h3>Current imtool colors</h3>
  <div class="highlight-default-notranslate"><pre>
        0 = sunview background color (normally white)
    1-200 = frame buffer data values, windowed
      201 = cursor color (white)
  
      202 = black
      203 = white
      204 = red
      205 = green
      206 = blue
      207 = yellow
      208 = cyan
      209 = magenta
      210 = coral
      211 = maroon
      212 = orange
      213 = khaki
      214 = orchid
      215 = turquoise
      216 = violet
      217 = wheat
  
  218-254 = reserved for use by other windows
      255 = black (sunview foreground color)
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Display an image,  mark all the objects in the coordinate file 
  m92.coo.1 with red dots, and save the contents of the frame buffer
  in the iraf image m92r.snap. Redisplay the marked image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; display m92r 1
  cl&gt; tvmark 1 m92.coo.1 outimage=m92r.snap col=204
  cl&gt; display m92r.snap 2 ztrans="none"
  </pre></div>
  <p>
  2. Execute the same command only number the objects in the coordinate
  list instead of marking them.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; display m92r 1
  cl&gt; tvmark 1 m92.coo.1 outimage=m92r.snap mark=none\
  &gt;&gt;&gt;   number+ col=204
  cl&gt; display m92r.snap 2 ztrans="none"
  </pre></div>
  <p>
  3. Display an image and draw concentric circles with radii of 5, 10 and
  20 pixels corresponding to an aperture radius and inner and outer
  sky annulus around the objects in the coordinate list. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; display m92r 1
  cl&gt; tvmark 1 m92.coo.1 mark=circle radii="5,10,20" col=204
  </pre></div>
  <p>
  4. Display an image, mark objects in a coordinate list with dots
  and append new objects to the coordinate file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; display m92r 1
  
  cl&gt; tvmark 1 m92.coo.1 interactive+
      ... type q to quit the help menu ...
      ... type :number yes to turn on numbering ...
      ... type l to mark all objects in the coordinate file
      ... move cursor to desired unmarked objects and type a
      ... type :write to take a snap shot of the frame buffer
      ... type q to quit
  </pre></div>
  <p>
  5. Make a finder chart of a region containing 10 stars by drawing
  a box around the field, marking each of the 10 stars with a dot,
  labeling each with an id and finally labeling the whole field.
  Save all the keystroke commands in a log file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; display m92r 1 log=m92r.log auto+
  
  cl&gt; tvmark 1 "" interactive+
  
      ... type q to quit the help menu ...
  
      ... to draw a box around the finder field move the cursor to the
          lower left corner of the finder field and type b, move the
          cursor the upper right corner of the field and type b again
  
      ... to mark and label each object move to the position of the
          object and type ., next move slightly away from the object
          and type :text id
  
      ... to label the chart with a title first type :txsize 2 for
          bigger text then move the cursor to the position where
          the title should begin and type :text title
  
      ... save the marked image with :write
  
      ... type q to quit the program
  </pre></div>
  <p>
  6. Edit the log file created above to remove any undesired commands
  and rerun tvmark redirecting cursor input to the log file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; display m92r 1
  cl&gt; tvmark 1 "" commands=logfile inter-
  </pre></div>
  <p>
  7. Draw a box on the display with a lower left corner of 101,101 and an
  upper right corner of 200,200 using a simple cursor command file.
  Note than in interactive mode the b key is the one that draws a box.
  </p>
  <div class="highlight-default-notranslate"><pre>
  The command file contains the following 3 lines
  
      101.0 101.0 101 b
      200.0 200.0 101 b
      200.0 200.0 101 q
  
      cl&gt; display m92r 1
      cl&gt; tvmark 1 "" commands=commandfile inter-
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Tvmark is a prototype task which can be expected to undergo considerable
  modification and enhancement in the future. The current version of this
  task does not produce publication quality graphics.
  In particular aliasing is easily visible in the code which draws circles
  and lines.
  </p>
  <p>
  Input from the coordinate list is sequential. No attempt has been made
  to arrange the objects to be marked in order for efficiency of input and
  output.
  </p>
  <p>
  Note that the move command does not currently physically move the image
  cursor. However the next mark drawn will be at the current coordinate
  list position.
  </p>
  <p>
  Users may wish to disable the markcur option in the imtool setup window
  before running tvmark.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  display, imedit, imexamine
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'CURRENT IMTOOL COLORS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

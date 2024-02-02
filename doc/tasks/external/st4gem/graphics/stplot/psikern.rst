.. _psikern:

psikern: IRAF GIO Kernel to produce PostScript output.
======================================================

**Package: stplot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  psikern input
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  psikern is a task that translates, or renders, IRAF graphics into
  PostScript.  Like all IRAF graphics kernels, psikern may be called either
  explicitly as a task, to plot a graphics metacode file, or implicitly
  when the output of a graphics task is directed to a device which uses
  the psikern kernel.  The only difference in how psikern operates when
  called as a task and as a graphics device is that the parameters to
  the psikern task are not available when run as a device.
  </p>
  <p>
  The casual IRAF user will probably not know whether they are using
  psikern to render graphics produced by IRAF graphics.  If the local
  STSDAS system administrator has set up graphics output devices to use
  psikern, usage is no different than any other IRAF graphics device.
  Since the set up of output devices in IRAF are site-specific, one will
  need to talk to their IRAF system administrator to find out what has
  been defined and whether any devices use psikern.  
  </p>
  <p>
  When one knows what devices are available, most of the time that
  device will be used directly by an IRAF graphics task, either by
  setting the cl variable <span style="font-family: monospace;">"stdplot"</span> to the psikern device name, or
  explicitly setting the <span style="font-family: monospace;">"device"</span> parameter of a graphics task to the
  psikern device name.  The usage is exactly the same as with any other
  IRAF graphics device.  For examples, look under the EXAMPLES section,
  especially examples 1, 2, and 3.
  </p>
  <p>
  A general user will run psikern as a task only under <span style="font-family: monospace;">"special"</span>
  circumstances: when there is a specific feature of psikern that the
  user wants to take advantage of and no graphics devices have that
  feature enabled.  Below discusses how to run psikern as a task and
  what options psikern provides for creating graphics output.
  </p>
  <p>
  To run psikern as a task, the graphics output of a task must be saved
  in Graphics Kernel Interface (GKI) metacode file. GKI metacode is
  the basic graphics command language that IRAF uses to draw graphics
  and is what psikern needs as input.  Often, this type of file is
  referred to as a <span style="font-family: monospace;">"metacode file"</span>.  Note that when the graphics is
  redirected to a file in this fashion, the graphics will not appear
  anywhere else.  This file cannot be printed directly or viewed; it is
  a binary file.  The file must be translated by a graphics kernel, such
  as psikern, before it is useful.
  </p>
  <p>
  Once a metacode file has been obtained, psikern can be used to
  translate the graphics into PostScript.  The EXAMPLES section contains
  demonstrations of common operations a user may want to use when
  running psikern as a task.
  </p>
  <p>
  A point of note about redirecting graphics to metacode files.  One
  should keep in mind where the graphics will ultimately be going,
  regardless of whether it is to a file, or to a physical device to be
  printed.  One should specify the same device for both the graphics
  task and the psikern task.  This will ensure that aspect ratios, line
  widths, etc. are consistent.
  </p>
  <dl id="l_COLOR">
  <dt><b>COLOR</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='COLOR' Line='COLOR' -->
  <dd>PostScript has the general capability of specifying any color desired.
  This is especially true of Level-2 PostScript, in which different
  color systems are implemented in PostScript.  However, a particular
  device, which supports PostScript, does not necessarily support a
  general color rendering.  In fact, no colors or grayscale may be
  available at all.  
  GIO itself has a very crude color model.  Color is represented simply
  as an integer, starting at zero.  The only dependable convention is
  that color 0 is the <span style="font-family: monospace;">"background"</span>, while color 1 is the <span style="font-family: monospace;">"foreground"</span>.
  Beyond this, there are no true conventions, except for what the
  'tvmark' task defines, and, more recently, what xgterm uses as the
  default.  Also, a specific task may wish to use its own colormapping,
  appropriate to the problem the task is solving.
  To interface the GIO color model to PostScript, psikern uses the
  <span style="font-family: monospace;">"lookup table"</span> (LUT) approach.  A table is defined which, for each GIO
  color index, a red/green/blue (RGB) color specification is defined.  A
  <span style="font-family: monospace;">"name"</span>, or string identifier may be specified along with the index,
  though GIO currently has no way of using named colors.
  There are two LUT's defined: one for <span style="font-family: monospace;">"graphics"</span>, i.e. almost
  everything produced by IRAF.  The other is for <span style="font-family: monospace;">"images"</span>, or, in GIO
  terminology, <span style="font-family: monospace;">"cells"</span>.  GIO has the ability, through the 'gpcell' call,
  to render images.  psikern will render these images using the image
  LUT.  There are two separate LUT's because line drawing and image
  rendering are two different operations, using the LUT's in different
  ways.  Most graphics applications will only be concerned with the
  graphics LUT.
  A lookup table may either be a text or binary STSDAS table.  If the table
  is a text table, the columns are defined as follows.  Lines that begin
  with a pound sign, <span style="font-family: monospace;">"#"</span>, or totally blank lines, are considered
  comments.  The first four columns must be present.  The last column,
  specifying the color name, is optional.
  <dl>
  <dt><b>First Column - GIO color index</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='First' Line='First Column - GIO color index' -->
  <dd>The GIO color index whose color is being defined.
  </dd>
  </dl>
  <dl>
  <dt><b>Second Column - red component.</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='Second' Line='Second Column - red component.' -->
  <dd>A real number, between 0 (no intensity) to 1 (full intensity)
  specifying the red component of the color for the current index.
  </dd>
  </dl>
  <dl>
  <dt><b>Third Column - green component.</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='Third' Line='Third Column - green component.' -->
  <dd>A real number, between 0 (no intensity) to 1 (full intensity)
  specifying the green component of the color for the current index.
  </dd>
  </dl>
  <dl>
  <dt><b>Fourth Column - blue component.</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='Fourth' Line='Fourth Column - blue component.' -->
  <dd>A real number, between 0 (no intensity) to 1 (full intensity)
  specifying the blue component of the color for the current index.
  </dd>
  </dl>
  <dl>
  <dt><b>Fifth Column - name (optional)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='Fifth' Line='Fifth Column - name (optional)' -->
  <dd>The rest of the row defines the name of the color.  This column is
  optional.
  </dd>
  </dl>
  For binary tables, the format is much the same as for text tables,
  except the columns are named.  Also, both the INDEX and NAME columns
  are optional.  The column names and their definitions are as follows:
  <dl>
  <dt><b>RED</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='RED' Line='RED' -->
  <dd>A real number, between 0 (no intensity) to 1 (full intensity)
  specifying the red component of the color for the current index.
  </dd>
  </dl>
  <dl>
  <dt><b>GREEN</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='GREEN' Line='GREEN' -->
  <dd>A real number, between 0 (no intensity) to 1 (full intensity)
  specifying the green component of the color for the current index.
  </dd>
  </dl>
  <dl>
  <dt><b>BLUE</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='BLUE' Line='BLUE' -->
  <dd>A real number, between 0 (no intensity) to 1 (full intensity)
  specifying the blue component of the color for the current index.
  </dd>
  </dl>
  <dl>
  <dt><b>INDEX (optional)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='INDEX' Line='INDEX (optional)' -->
  <dd>If this column is present, it contains the GIO color indicies for
  which colors are defined.  If not present, the row number defines the
  color index.
  </dd>
  </dl>
  <dl>
  <dt><b>NAME (optional)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='NAME' Line='NAME (optional)' -->
  <dd>A name associated with the color.
  </dd>
  </dl>
  Another feature of psikern and its LUT's is that psikern can
  interpolate colors.  psikern forces that all colors be defined.  In
  other words, all colors 
  between 0 and the maximum index defined in a LUT must be defined.  For
  example, if the largest color index defined in a LUT is 255, all
  colors from 0 to 255 must be defined.  If this is not the case,
  psikern will use linear interpolation to define any intervening colors
  that have not explicitly been defined in the LUT.  This has the advantage
  of being able to specify compact LUT's for potentially large numbers
  of colors.  See the examples below.
  </dd>
  </dl>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input metacode files.
  </dd>
  </dl>
  <dl>
  <dt><b>(device = <span style="font-family: monospace;">"stdplot"</span> [string])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(device = "stdplot" [string])' -->
  <dd>The output device.  The output device should be one setup to use
  psikern as the graphics kernel.  If it is not known what devices are
  available, ask the local IRAF system administrator.
  </dd>
  </dl>
  <dl>
  <dt><b>(generic = no [boolean])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(generic = no [boolean])' -->
  <dd>If 'yes', all subsequent parameters are ignored.  Specifically,
  psikern will only query for the 'input', 'device', and 'generic'
  parameters.  This is the situation when the kernel is called from the
  GIO system. If 'no', then all parameters are queried for.
  </dd>
  </dl>
  <dl>
  <dt><b>(output = <span style="font-family: monospace;">""</span> [file])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(output = "" [file])' -->
  <dd>The file where the PostScript should be written.  If blank, the
  PostScript file will be dealt with according to how the graphics
  device, specified in the <span style="font-family: monospace;">"device"</span> parameter, would normally handle the
  file.
  </dd>
  </dl>
  <dl>
  <dt><b>(roman_font = <span style="font-family: monospace;">""</span> [string])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(roman_font = "" [string])' -->
  <dd>PostScript font to use for rendering the GIO Roman font.  If blank,
  the default PostScript font will be used, Times-Roman.
  </dd>
  </dl>
  <dl>
  <dt><b>(greek_font = <span style="font-family: monospace;">""</span> [string])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(greek_font = "" [string])' -->
  <dd>PostScript font to use for rendering the GIO Greek font.  If blank,
  the default PostScript font will be used, Symbol.
  </dd>
  </dl>
  <dl>
  <dt><b>(bold_font = <span style="font-family: monospace;">""</span> [string])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(bold_font = "" [string])' -->
  <dd>PostScript font to use for rendering the GIO Bold font.  If blank, the
  default PostScript font will be used, Times-Bold.
  </dd>
  </dl>
  <dl>
  <dt><b>(italic_font = <span style="font-family: monospace;">""</span> [string])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(italic_font = "" [string])' -->
  <dd>PostScript font to use for rendering the GIO Italic font.  If blank,
  the default PostScript font will be used, Times-Italic.
  </dd>
  </dl>
  <dl>
  <dt><b>(proportional = yes [boolean])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(proportional = yes [boolean])' -->
  <dd>Use proportional spaced fonts?  If 'yes', proportional spacing will be
  used when writing characters.  If 'no', the spacing of characters will
  be constant.
  </dd>
  </dl>
  <dl>
  <dt><b>(graphics_lut = <span style="font-family: monospace;">""</span> [string])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(graphics_lut = "" [string])' -->
  <dd>Name of the graphics lookup table defining the available colors.  If
  blank, the graphics lookup table will be that normally used by the
  specified device.
  </dd>
  </dl>
  <dl>
  <dt><b>(image_lut = <span style="font-family: monospace;">""</span> [string])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(image_lut = "" [string])' -->
  <dd>Name of the image lookup table defining the available colors for the
  cellarray operation.  If blank, the image lookup table will be that
  normally used by the specified device.
  </dd>
  </dl>
  <dl>
  <dt><b>(linecolor = INDEF [int])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(linecolor = INDEF [int])' -->
  <dd>Set default line color to 'linecolor'.  GIO does not have a real
  concept of a default color, so anytime the color is 1, then it is
  changed to the value of this parameter.
  If 'INDEF', no changes to colors will be made.
  </dd>
  </dl>
  <dl>
  <dt><b>(markercolor = INDEF [int])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(markercolor = INDEF [int])' -->
  <dd>Set default marker color to 'markercolor'.  GIO does not have a real
  concept of a default color, so anytime the color is 1, then it is
  changed to the value of this parameter.
  If 'INDEF', no changes to colors will be made.
  </dd>
  </dl>
  <dl>
  <dt><b>(textcolor = INDEF [int])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(textcolor = INDEF [int])' -->
  <dd>Set default text color to 'textcolor'.  GIO does not have a real
  concept of a default color, so anytime the color is 1, then it is
  changed to the value of this parameter.
  If 'INDEF', no changes to colors will be made.
  </dd>
  </dl>
  <dl>
  <dt><b>(areacolor = INDEF [int])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(areacolor = INDEF [int])' -->
  <dd>Set default area color to 'areacolor'.  GIO does not have a real
  concept of a default color, so anytime the color is 1, then it is
  changed to the value of this parameter.
  If 'INDEF', no changes to colors will be made.
  </dd>
  </dl>
  <dl>
  <dt><b>(debug = no [boolean])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(debug = no [boolean])' -->
  <dd>If 'yes', the graphics instructions are decoded and printed
  during processing.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = no [boolean])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = no [boolean])' -->
  <dd>If 'yes', the elements of polylines, cell arrays, etc. will
  be printed in debug mode.
  </dd>
  </dl>
  <dl>
  <dt><b>(gkiunits = no [boolean])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(gkiunits = no [boolean])' -->
  <dd>By default, coordinates are printed in NDC rather than GKI units.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The first three examples show how to use a psikern device in normal
  IRAF operations.
  </p>
  <p>
  1. Using a psikern device as simply another IRAF graphics device:
  This example demonstrates the create of a PostScript file using the
  <span style="font-family: monospace;">"psi_land"</span> graphics device and the <span style="font-family: monospace;">"prow"</span> task:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prow dev$pix 256 device=psi_land
  cl&gt; gflush
  /tmp/pskxxxx
  </pre></div>
  <p>
  The name of the PostScript file, here <span style="font-family: monospace;">"/tmp/pskxxxx"</span>, is echoed when
  the <span style="font-family: monospace;">"gflush"</span> command is given.  The <span style="font-family: monospace;">"gflush"</span> command tells the
  graphics system that no more information will be appended to the plot,
  thus closing the file and echoing the file name to the screen.
  </p>
  <p>
  2. Using a psikern device which is a printer:  This example
  demonstrates the use of a psikern device when the device is configured
  to use a printer.  This device will be called <span style="font-family: monospace;">"lw"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prow dev$pix 256 device=lw
  gflush
  </pre></div>
  <p>
  A not about the <span style="font-family: monospace;">"gflush"</span>:  IRAF graphics output never occurs
  immediately.  This allows other tasks to append more information to a
  plot.  Therefore, if one knows that the plot is complete and would
  like to get it immediately, a <span style="font-family: monospace;">"gflush"</span> is required to inform the
  graphics system that the plot is complete and to print it.
  </p>
  <p>
  3. Making a psikern device the default plotting device: Many
  interactive tasks use the <span style="font-family: monospace;">"snap"</span> cursor command to create hardcopy
  plots of what is currently on the screen.  The device used for the
  hardcopy is whatever the value of the cl variable <span style="font-family: monospace;">"stdplot"</span> is.
  To change the default output device to a psikern device, simply set
  <span style="font-family: monospace;">"stdplot"</span> to the name of the desired psikern device.  The example
  below shows the use with the graphics cursor <span style="font-family: monospace;">"snap"</span> function from the
  <span style="font-family: monospace;">"splot"</span> task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set stdplot=psi_land
  cl&gt; splot aspectrum
          ...enters graphics interactive mode...
          ...from which the "snap" command can be given...
  :.snap
  q
  cl&gt; gflush
  </pre></div>
  <p>
  A note about the <span style="font-family: monospace;">"stdplot"</span> variable:  If one wants to make a permanent
  change to the value of this variable, the <span style="font-family: monospace;">"set"</span> command should be
  placed in the file <span style="font-family: monospace;">"home$loginuser.cl"</span>.  In this way, everytime the cl
  is started, the variable will have the desired value.
  </p>
  <p>
  The following examples demonstrate how to use the psikern task
  directly to modify the look of a plot.
  </p>
  <p>
  4. Capture the output of the prow task in a metacode file and
  produce a PostScript file.  This example does not demonstrate anything
  that could not be done directly using a graphcape device.  This is
  just meant to show how to redirect graphics to a file, and then render
  that file using a specific graphics kernel.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prow dev$pix 101 &gt;G prow.gki
  cl&gt; psikern prow.gki device=psi_land
  </pre></div>
  <p>
  Note that this could have been done as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prow dev$pix 101 device=psi_land
  cl&gt; gflush
  </pre></div>
  <p>
  5. Produce a PostScript file from a GKI metacode file.  However,
  instead of using the default name generated by psikern itself, place
  the PostScript into a specific file, here <span style="font-family: monospace;">"prow.ps"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prow dev$pix 101 &gt;G prow.gki
  cl&gt; psikern prow.gki device=psi_land output=prow.ps
  </pre></div>
  <p>
  6. Use a different set of fonts than that specified for any device
  defined in the graphcap file.  For example, one may want to use the
  Helvetica family of fonts instead of the Times family.  The font names
  should appear exaclty as they would in a PostScript program.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prow dev$pix 101 &gt;G prow.gki
  cl&gt; psikern prow.gki device=psi_land\
  roman_font=Helvetica bold_font=Helvetica-Bold\
  italic_font=Helvetica-Oblique
  </pre></div>
  <p>
  7. Change the spacing of characters.  By default, psikern renders
  characters using proportional spacing.  However, GIO and many tasks
  assume the character spacing is constant, or monospace.  Render a
  graphics output using monospaced characters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prow dev$pix 101 &gt;G prow.gki
  cl&gt; psikern prow.gki device=psi_land proportional-
  </pre></div>
  <p>
  8. Changing colors of a graphics output from an IRAF task that does
  not provide this functionality.  Most IRAF tasks do not allow or make
  use of colors.  Instead of rendering output using the color
  defined for color 1, use the color defined for color 2, and render
  text using color 3.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prow dev$pix 101 &gt;G prow.gki
  cl&gt; psikern prow.gki device=psi_land\
  linecolor=2 textcolor=3
  </pre></div>
  <p>
  The following examples demonstrate how to define and modify the color
  lookup tables.
  </p>
  <p>
  9. Define and use the color table, <span style="font-family: monospace;">"invxgterm"</span>.  This
  table is a text table distributed with STSDAS in the file
  <span style="font-family: monospace;">"stsdas$lib/invxgterm"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prow dev$pix 101 &gt;G prow.gki
  cl&gt; psikern prow.gki device=psi_land \
  graphics_lut=stsdas$lib/invxterm
  </pre></div>
  <p>
  10.  Define a two-color graphics lookup table.  Many PostScript
  devices are laser printers.  Though they render color as different
  levels of gray, the output may not be pleasing.  One can force black
  on white by using a two-color graphics lookup table.  STSDAS
  distributes this table in the file <span style="font-family: monospace;">"stsdas$lib/mono"</span>
  </p>
  <p>
  11.  A user has written an IGI script which requires a 256 color
  graphics LUT, which mimics a rainbow from red to magenta.  STSDAS
  distributes this table in the file <span style="font-family: monospace;">"stsdas$lib/rain256"</span>.  This
  table demonstrates the use of the color interpolation that psikern
  provides.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; igi &lt;manycolor.igi &gt;G igi.gki
  cl&gt; pskern igi.gki device=apsikerndevice \
  graph_lut=stsdas$lib/rain256
  </pre></div>
  <p>
  12.  A user has written an IGI script which renders an image.  However,
  the user would like to use a 256 color image LUT, which mimics a
  rainbow from red to magenta.  STSDAS distributes this table as
  <span style="font-family: monospace;">"stsdas$lib/imgrain256"</span>.  The only difference between
  the table below and the one in example 11 is that an image LUT need
  not worry about background/foreground colors.  Hence the first two
  entries can be part of the whole color continuum.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; igi &lt;image.igi &gt;G igi.gki
  cl&gt; psikern igi.gki device=apsikerndevice\
  image_lut="imgrain256"
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The kernel does not recognize changes in the txspacing.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  STSDAS Contact: Jonathan Eisenhamer, &lt;eisenhamer@stsci.edu&gt;
  </p>
  <p>
  For a technical/programming description of psikern, including how to
  modify IRAF'S graphcap file to install psikern devices, execute the
  command:
  </p>
  <div class="highlight-default-notranslate"><pre>
  help psikern option=sysdoc
  </pre></div>
  <p>
  For a technical description of IRAF's Graphics Interface (GIO)
  facility, execute the command:
  </p>
  <div class="highlight-default-notranslate"><pre>
  help gio$doc/gio.hlp files+
  </pre></div>
  <p>
  There are many reference manuals available on PostScript.  However,
  since PostScript is a licensed produce of Adobe Systems, the ultimate
  reference is
  </p>
  <div class="highlight-default-notranslate"><pre>
  PostScript language refernce manual / Adobe Systems. - 2nd ed.
          p. cm.
  Includes index.
  ISBN 0-201-18127-4
  1. PostScript (Computer program language) I. Adobe Systems.
  QA76.73.P67P67 1990
  005.13'3-dc20
  
  Addison-Wesley Publishing Company, Inc.
  </pre></div>
  <p>
  A number of color lookup tables are distributed with STSDAS in the
  directory <span style="font-family: monospace;">"stsdas$lib"</span>.  The following tables are currently available:
  </p>
  <div class="highlight-default-notranslate"><pre>
  defxgterm       -- Similar color map as the default xgterm colormap
  gray256         -- Graphics LUT rendering different levels of gray
  imgrain256      -- Image LUT for image operations
  invxgterm       -- xgterm colormap but with a white background
  mono            -- 2 color (monochrome)
  rain256         -- Graphics LUT rendering a version of the rainbow
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  stdgraph, stdplot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

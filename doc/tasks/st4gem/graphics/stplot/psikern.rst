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
  ST4GEM system administrator has set up graphics output devices to use
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
  A lookup table may either be a text or binary ST4GEM table.  If the table
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
  table is a text table distributed with ST4GEM in the file
  <span style="font-family: monospace;">"st4gem$lib/invxgterm"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prow dev$pix 101 &gt;G prow.gki
  cl&gt; psikern prow.gki device=psi_land \
  graphics_lut=st4gem$lib/invxterm
  </pre></div>
  <p>
  10.  Define a two-color graphics lookup table.  Many PostScript
  devices are laser printers.  Though they render color as different
  levels of gray, the output may not be pleasing.  One can force black
  on white by using a two-color graphics lookup table.  ST4GEM
  distributes this table in the file <span style="font-family: monospace;">"st4gem$lib/mono"</span>
  </p>
  <p>
  11.  A user has written an IGI script which requires a 256 color
  graphics LUT, which mimics a rainbow from red to magenta.  ST4GEM
  distributes this table in the file <span style="font-family: monospace;">"st4gem$lib/rain256"</span>.  This
  table demonstrates the use of the color interpolation that psikern
  provides.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; igi &lt;manycolor.igi &gt;G igi.gki
  cl&gt; pskern igi.gki device=apsikerndevice \
  graph_lut=st4gem$lib/rain256
  </pre></div>
  <p>
  12.  A user has written an IGI script which renders an image.  However,
  the user would like to use a 256 color image LUT, which mimics a
  rainbow from red to magenta.  ST4GEM distributes this table as
  <span style="font-family: monospace;">"st4gem$lib/imgrain256"</span>.  The only difference between
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
  ST4GEM Contact: Jonathan Eisenhamer, &lt;eisenhamer@stsci.edu&gt;
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
  A number of color lookup tables are distributed with ST4GEM in the
  directory <span style="font-family: monospace;">"st4gem$lib"</span>.  The following tables are currently available:
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
  
System Documentation
--------------------

.. raw:: html

  <section id="s_description">
  <h3>Description</h3>
  <p>
  For a user-level description of psikern, type <span style="font-family: monospace;">"help psikern"</span>.  This
  help file provides detailed information on how psikern interfaces with
  GKI, how to define a graphcap to use psikern, and the SPP interface to
  the GIO escape function to access features of psikern that cannot be
  accessed through GIO.
  </p>
  <p>
  PSIKern is used to generate Level 1, <span style="font-family: monospace;">"encapsulated"</span> PostScript files
  from the IRAF Graphics Input/Ouput (GIO) graphics system.  When GIO
  draws graphics, it outputs the drawing commands in a language known as
  Graphics Kernel Interface (GKI).  psikern translates the GKI
  datastream into a PostScript program, suitable for output to a
  PostScript device, or for inclusion in a word processing document.
  This kernel implements all the functionality provided by the GKI
  datastream, including color lines, color text, color solid fills,
  arbitrary fill patterns, and the simple imaging model.  There are also
  a number of <span style="font-family: monospace;">"escape"</span> sequences to add some basic functionality that
  the normal GKI datastream does not support.  More explanations of
  these below.
  </p>
  <p>
  For a full discussion of GIO, see the help file <span style="font-family: monospace;">"gio$doc/gio.hlp"</span>
  </p>
  <p>
  Like all IRAF graphics kernels, psikern may be called either
  explicitly as a task, to plot a graphics metacode file, or implicitly
  when the output of a graphics task is directed to a device which uses
  the psikern kernel.  The only difference in how psikern operates when
  called as a task and as a graphics device is that the parameters to
  the psikern task are not available when run as a device.  However, the
  functionality of the parameters can be accessed through the graphcap
  parameters.
  </p>
  <p>
  The rest of the discussion focuses on how color is handled, how to
  define a graphcap, and the programming interface for the GIO escape
  codes.
  </p>
  <dl id="l_COLOR">
  <dt><b>COLOR</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='COLOR' Line='COLOR' -->
  <dd>PostScript has the general capability of specifying any color desired.
  This is especially true of Level 2 PostScript, in which different
  colors systems are implemented in PostScript.  However, a particular
  device, which supports PostScript, does not necessarily support a
  general color rendering.  In fact, no colors or grayscale may be
  available at all.  
  GIO itself has a basic color model.  Color is represented simply
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
  A lookup table may either be a text or binary ST4GEM table.  If the table
  is a text table, the columns are defined as follows.  Lines that begin
  with a pound sign, <span style="font-family: monospace;">"#"</span>, or totally blank lines, are considered
  comments.  The first four columns must be present.  The last column,
  specifying the color name is optional.
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
  <dl id="l_GRAPHCAP">
  <dt><b>GRAPHCAP</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='GRAPHCAP' Line='GRAPHCAP' -->
  <dd>Each GIO graphics device is defined by a <span style="font-family: monospace;">"graphcap"</span> entry.  See the GIO
  documentation for a full explanation of the graphcap.  In short, a
  graphcap entry is made up of two character <span style="font-family: monospace;">"parameters"</span>.  The
  parameters have a type which is indicated by how the parameter is
  defined.  The parameters are separated by colons, <span style="font-family: monospace;">":"</span>.  The types of
  parameters and the form the take are as follows, where <span style="font-family: monospace;">"XX"</span> is the
  parameter name and <span style="font-family: monospace;">"V"</span>'s are the values:
  <dl>
  <dt><b>XX -- Boolean</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='XX' Line='XX -- Boolean' -->
  <dd>A parameter with no associated value is a boolean parameter.  If the
  parameter is listed in the graphcap, the value of that parameter is
  'true'.  If the parameter is not present, the value is 'false'
  </dd>
  </dl>
  <dl>
  <dt><b>XX#VVV -- Numeric (either integer or real)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='XX' Line='XX#VVV -- Numeric (either integer or real)' -->
  <dd>If the parameter is followed by a pound sign, <span style="font-family: monospace;">"#"</span>, the value of the
  parameter is the number following the <span style="font-family: monospace;">"#"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>XX=VVV -- String</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='XX' Line='XX=VVV -- String' -->
  <dd>If the parameter is followed by an equal sign, <span style="font-family: monospace;">"="</span>, the value of the
  parameter is the string, up to the next <span style="font-family: monospace;">":"</span>.
  </dd>
  </dl>
  Again, there are many more features in a graphcap file.  Please refer
  to the GIO documentation for a full description.
  graphcap parameters fall into two classes: generic and
  device-specific.  Generic parameters are represented by lower case
  characters.  These parameters can generally be found for all types of
  devices and should be present (if the capability exists).
  Device-specific parameters are represented by upper case characters.
  They represent specific features of a particular device that does not
  fall under the generic parameters.  Since they are device-specific, a
  task must know what type of device is in use to make use of these
  parameters.
  Below is a list of all the relevent graphcap parameters for a psikern
  device.  The generic parameters are presented first, followed by the
  device-specific parameters.
  <dl>
  <dt><b>ar (real)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='ar' Line='ar (real)' -->
  <dd>The aspect ratio of the GIO plotting area.  This is generally equal
  to:
  <div class="highlight-default-notranslate"><pre>
  ys / xs
  </pre></div>
  where xs and ys are graphcap parameters.  In general, this parameter
  should always be defined since many IRAF graphics tasks use this
  parameter to correct for changes in aspect ratios.
  </dd>
  </dl>
  <dl>
  <dt><b>ca (bool)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='ca' Line='ca (bool)' -->
  <dd>If present, this indicates that the device implements cell arrays
  (images).  
  In general, this parameter should be defined since the PostScript
  language always supports this functionality.  Note though that not all
  PostScript devices support this functionality, or it may be desirable
  to disallow a specific device from providing this functionality.
  If psikern does not find this capability, psikern will not render cell
  arrays.
  </dd>
  </dl>
  <dl>
  <dt><b>ch (real)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='ch' Line='ch (real)' -->
  <dd>The height, in NDC units, of a text character.
  </dd>
  </dl>
  <dl>
  <dt><b>cw (real)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='cw' Line='cw (real)' -->
  <dd>The width, in NDC units, of a text character.
  </dd>
  </dl>
  <dl>
  <dt><b>fa (bool)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='fa' Line='fa (bool)' -->
  <dd>If present, indicates that the device implements fill patterns.
  In general, this parameter should be defined since the PostScript
  language always supports this functionality.  Note though that not all
  PostScript devices support this functionality, or it may be desirable
  to disallow a specific device from providing this functionality.  If
  psikern does not find this capability, psikern will not render filled
  areas.
  </dd>
  </dl>
  <dl>
  <dt><b>fs (int)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='fs' Line='fs (int)' -->
  <dd>The number of fill styles implemented.  psikern provides by default
  six fill styles.  In general, this should always be present.
  </dd>
  </dl>
  <dl>
  <dt><b>kf (string)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='kf' Line='kf (string)' -->
  <dd>The file name of the kernel executable.  The default value is
  <span style="font-family: monospace;">"st4gem$bin/x_psikern.e"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>li (int)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='li' Line='li (int)' -->
  <dd>The number of lines of text that can fit within the GIO plotting area.
  By default, this should be 24.
  </dd>
  </dl>
  <dl>
  <dt><b>pl (bool)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='pl' Line='pl (bool)' -->
  <dd>If present, indicates that the device implements polylines.
  In general, this parameter should be defined since the PostScript
  language always supports this functionality.  Note though that not all
  PostScript devices support this functionality, or it may be desirable
  to disallow a specific device from providing this functionality.
  </dd>
  </dl>
  <dl>
  <dt><b>pm (bool)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='pm' Line='pm (bool)' -->
  <dd>If present, indicates that the device implements polymarkers.
  In general, this parameter should be defined since the PostScript
  language always supports this functionality.  Note though that not all
  PostScript devices support this functionality, or it may be desirable
  to disallow a specific device from providing this functionality.
  </dd>
  </dl>
  <dl>
  <dt><b>se (bool)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='se' Line='se (bool)' -->
  <dd>If present, indicates that the device implements selective erase.  For
  the current version of GIO, this means that the background color, 0,
  will erase previously drawn graphics of other colors.  In general,
  this should always be present.
  </dd>
  </dl>
  <dl>
  <dt><b>tn (string)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='tn' Line='tn (string)' -->
  <dd>The task name of the kernel in the executable.  In general, this
  should always be <span style="font-family: monospace;">"psikern"</span>
  </dd>
  </dl>
  <dl>
  <dt><b>tq (int)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='tq' Line='tq (int)' -->
  <dd>The number of text quality levels.  PostScript provides only one
  quality level, the highest.
  </dd>
  </dl>
  <dl>
  <dt><b>xr (int)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='xr' Line='xr (int)' -->
  <dd>The resolution, in device dots per inch, along the GIO X (horizontal) axis.
  The X dimension is parallel to the horizontal, x, dimension of GIO.  For
  landscape mode, this is along the longest physical dimension of the
  device.  For portrait mode, this is along the shortest physical
  dimension of the device.  In general, this should always be defined.
  </dd>
  </dl>
  <dl>
  <dt><b>xs (real)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='xs' Line='xs (real)' -->
  <dd>The width of the GIO plotting area, in meters, along the GIO X
  (horizontal) axis.
  The X dimension is parallel to the horizontal, x, dimension of GIO.  For
  landscape mode, this is along the longest physical dimension of the
  device.  For portrait mode, this is along the shortest physical
  dimension of the device.  In general, this should always be defined.
  </dd>
  </dl>
  <dl>
  <dt><b>yr (int)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='yr' Line='yr (int)' -->
  <dd>The resolution, in device dots per inch, along the GIO Y (vertical) axis.
  The Y dimension is perpendicular to the horizontal, x, dimension of GIO.  For
  landscape mode, this is along the shortest physical dimension of the
  device.  For portrait mode, this is along the longest physical
  dimension of the device.  In general, this should always be defined.
  </dd>
  </dl>
  <dl>
  <dt><b>ys (real)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='ys' Line='ys (real)' -->
  <dd>The width of the GIO plotting area, in meters, along the GIO Y
  (vertical) axis.
  The resolution, in device dots per inch, along the GIO Y (vertical) axis.
  The Y dimension is perpendicular to the horizontal, x, dimension of GIO.  For
  landscape mode, this is along the shortest physical dimension of the
  device.  For portrait mode, this is along the longest physical
  dimension of the device.  In general, this should always be defined.
  </dd>
  </dl>
  <dl>
  <dt><b>zr (int)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='zr' Line='zr (int)' -->
  <dd>The resolution in z or color levels, of the device.  What this means
  in GIO is not clear.  psikern doesn't use this value.  However, the
  assumption is that this is a maximum level.  Arbitrarily, psikern
  assumes 256 levels.
  </dd>
  </dl>
  The device-specific parameters are as follows:
  <dl>
  <dt><b>BO (bool)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='BO' Line='BO (bool)' -->
  <dd>If present, psikern will <span style="font-family: monospace;">"buffer"</span> the PostScript output.  PostScript
  itself does not consider newlines important, but just as another
  <span style="font-family: monospace;">"whitespace"</span> character.  psikern will fill an 80 character line with
  as many characters as it can before issuing a newline character.  If
  this parameter is not present, implying false, psikern will place
  each PostScript command that it generates on a separate line.  This is
  useful if the user wants to do extensive editing on the PostScript, or
  understand what the PostScript is doing.
  </dd>
  </dl>
  <dl>
  <dt><b>DB (bool)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='DB' Line='DB (bool)' -->
  <dd>If present, psikern will print out debugging information to STDERR.
  This information contains details about what SPP functions are being
  called while the kernel is running.   Useful only if the user is
  actually debugging/modifying the psikern SPP code.
  </dd>
  </dl>
  <dl>
  <dt><b>DD (string)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='DD' Line='DD (string)' -->
  <dd>The <span style="font-family: monospace;">"dispose"</span> parameter.  This is what tells psikern what to do with a
  PostScript file, once it is generated.  In general, there are three,
  comma-separated, fields in the string.  The first is the name of the
  device.  The second field is the rootname for any temporary files
  created by psikern.  The third field is the operating system command
  to execute to dispose/print/rename the PostScript file.  See the
  examples below.
  </dd>
  </dl>
  <dl>
  <dt><b>FB (string)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='FB' Line='FB (string)' -->
  <dd>The PostScript font to use for GIO Bold font.  If not specified, the
  <span style="font-family: monospace;">"Times-Bold"</span> PostScript font will be used.  This can be any font name
  understood by the PostScript device which will be printing/using the
  output.
  </dd>
  </dl>
  <dl>
  <dt><b>FE (bool)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='FE' Line='FE (bool)' -->
  <dd>If present, an extra <span style="font-family: monospace;">"showpage"</span> will be issued at the end of the last
  plot in the file.  In general, this is not necessary for most
  PostScript devices.
  </dd>
  </dl>
  <dl>
  <dt><b>FG (string)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='FG' Line='FG (string)' -->
  <dd>The PostScript font to use for GIO Greek font.  If not specified, the
  <span style="font-family: monospace;">"Symbol"</span> PostScript font will be used.  This can be any font name
  understood by the PostScript device which will be printing/using the
  output.
  </dd>
  </dl>
  <dl>
  <dt><b>FI (string)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='FI' Line='FI (string)' -->
  <dd>The PostScript font to use for GIO Italic font.  If not specified, the
  <span style="font-family: monospace;">"Times-Italic"</span> PostScript font will be used.  This can be any font name
  understood by the PostScript device which will be printing/using the
  output.
  </dd>
  </dl>
  <dl>
  <dt><b>FR (string)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='FR' Line='FR (string)' -->
  <dd>The PostScript font to use for GIO Roman font.  If not specified, the
  <span style="font-family: monospace;">"Times-Roman"</span> PostScript font will be used.  This can be any font name
  understood by the PostScript device which will be printing/using the
  output.
  </dd>
  </dl>
  <dl>
  <dt><b>FS (bool)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='FS' Line='FS (bool)' -->
  <dd>If present, a <span style="font-family: monospace;">"showpage"</span> command will be issued before the first
  plotting instruction is written to the PostScript output.  This is
  generally not necessary for most PostScript devices.
  </dd>
  </dl>
  <dl>
  <dt><b>IF (string)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='IF' Line='IF (string)' -->
  <dd>The file containing the psikern PostScript prolog commands.  Must
  always be specified.  The default value is
  <span style="font-family: monospace;">"st4gem$lib/psikern_prolog.ps"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>LG (string)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='LG' Line='LG (string)' -->
  <dd>The name of the file containing the lookup table (LUT) to use for
  graphics colors.  If not present, psikern will use a default LUT
  similar to that of the 'tvmark' task.
  </dd>
  </dl>
  <dl>
  <dt><b>LI (string)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='LI' Line='LI (string)' -->
  <dd>The name of the file containing the lookup table (LUT) to use for
  images.  If not present, psikern will use a default grayscale mapping.
  </dd>
  </dl>
  <dl>
  <dt><b>MF (int)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='MF' Line='MF (int)' -->
  <dd>The number of frames/plots that can be placed in a single PostScript
  file at a time.  If not present, psikern will place one frame per
  file.
  If MF is less than zero, an evil thing happens.  Some
  background: In the IRAF graphics system, then end of a plot is defined
  as the beginning of the next plot- either through the GKI_CLEAR
  operand, or through the GFLUSH iraf command.  I.e. one doesn't really
  know the end of the plot.  As a result, one can NEVER get a plot to
  come out of a printer immediately after finishing drawing a plot,
  without invoking gflush or starting a new plot.  This is fine and
  proper.  However, user perception is a different thing.  Some people
  insist on getting a plot out.  Hence the evil.  If MF is less than 0,
  the graphics will be flushed to the printer when the current plot is
  closed.  The problem users will then be faced with is the fact that
  they can not append plots together, since the previous plot is now
  <span style="font-family: monospace;">"out the door"</span>.  DO NOT USE this feature except for special
  circumstances. 
  </dd>
  </dl>
  <dl>
  <dt><b>MO (bool)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='MO' Line='MO (bool)' -->
  <dd>If present, text will be written using mono-spaced characters.  If not
  present, text will be written using variable-spaced characters.
  </dd>
  </dl>
  <dl>
  <dt><b>NF (bool)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='NF' Line='NF (bool)' -->
  <dd>If present, store each frame in a seperate spool file.  This has the
  same effect as setting the MF parameter to 1.  This parameter
  overrides any settings of the MF parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>PB (int)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='PB' Line='PB (int)' -->
  <dd>The index of the graphics color to use to paint the background of the
  whole plot area.  This can be used to change the default background
  color to something other than the color of the paper or other output
  device.  If not present, no color is painted on the background.
  </dd>
  </dl>
  <dl>
  <dt><b>PI (real)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='PI' Line='PI (real)' -->
  <dd>The multiplicative increment to increase the linewidth each step.  The
  linewidth is determined by the equation
  <div class="highlight-default-notranslate"><pre>
  drawn width = PW + ((linewidth-1) * PI * PW)
  </pre></div>
  where PW is another graphcap parameter (see below).
  </dd>
  </dl>
  <dl>
  <dt><b>PT (bool)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='PT' Line='PT (bool)' -->
  <dd>If present, paint the plot onto the device in <span style="font-family: monospace;">"portrait"</span> mode.  If not
  present, plots will appear in <span style="font-family: monospace;">"landscape"</span> mode.  Portrait mode is when
  the horizontal axis of the plot is parallel to the shorter dimension
  of the output device.  Landscape mode is when the horizontal axis of
  the plot is parallel to the longer dimension of the output device.
  </dd>
  </dl>
  <dl>
  <dt><b>PW (real)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='PW' Line='PW (real)' -->
  <dd>The size of a drawn line in normalized device coordinates (NDC).  
  NDC coordinates go from 0 (zero width) to 1 (full width of the output
  device).
  </dd>
  </dl>
  <dl>
  <dt><b>RM (bool)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='RM' Line='RM (bool)' -->
  <dd>If present, the temporary file containing the PostScript will be
  deleted after the dispose command, defined in the DD parameter, has
  been executed.  In general, this is not specified because the deletion
  of any files is usually handled by the dispose command or the actual
  printing operation.
  </dd>
  </dl>
  <dl>
  <dt><b>TD (int)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='TD' Line='TD (int)' -->
  <dd>The size, in NDC units, of a dash in a dashed or dashed-dotted line.
  NDC coordinates go from 0 (zero width) to 1 (full width of the output
  device).
  </dd>
  </dl>
  <dl>
  <dt><b>TP (int)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='TP' Line='TP (int)' -->
  <dd>The size, in NDC units, of a dot in a dotted or dashed-dotted line.
  NDC coordinates go from 0 (zero width) to 1 (full width of the output
  device).
  </dd>
  </dl>
  <dl>
  <dt><b>TS (int)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='TS' Line='TS (int)' -->
  <dd>The size, in NDC units, of a space in a dashed, dotted, or
  dashed-dotted line. 
  NDC coordinates go from 0 (zero width) to 1 (full width of the output
  device).
  </dd>
  </dl>
  <dl>
  <dt><b>XO (real)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='XO' Line='XO (real)' -->
  <dd>Offset, in meters, from the corner/zeropoint of the physical display,
  the lower left hand corner of the GIO plotting area starts.  The X
  dimension is parallel to the horizontal, x, dimension of GIO.  For
  landscape mode, this is along the longest physical dimension of the
  device.  For portrait mode, this is along the shortest physical
  dimension of the device.
  </dd>
  </dl>
  <dl>
  <dt><b>YO (real)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='YO' Line='YO (real)' -->
  <dd>Offset, in meters, from the corner/zeropoint of the physical display,
  the lower left hand corner of the GIO plotting area starts.  The Y
  dimension is perpendicular to the horizontal, x, dimension of GIO.  For
  landscape mode, this is along the shortest physical dimension of the
  device.  For portrait mode, this is along the longest physical
  dimension of the device.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_EXTRA">
  <dt><b>EXTRA FUNCTIONALITY: GKI ESCAPE CODES</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='EXTRA' Line='EXTRA FUNCTIONALITY: GKI ESCAPE CODES' -->
  <dd>PSIKern supports a number of <span style="font-family: monospace;">"escape"</span> codes which round-out the
  basic functionality of the GKI interface.  Programs access the escape
  code by including the file <span style="font-family: monospace;">"&lt;psiescape.h&gt;"</span> and using the GIO routine
  'gescape'.  Below is what the different escape codes are and how they
  use the array passed by gescape.  Note that one can check on the type
  of kernel being used by inquiring of the graphcap value 'tn' using
  the 'ggets' GIO routine.  For PSIKern, this value will be <span style="font-family: monospace;">"psikern"</span>.
  <dl>
  <dt><b>PS_CODE</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='PS_CODE' Line='PS_CODE' -->
  <dd>Send raw PostScript code to the output.  The array
  contains the string of PostScript that is to be downloaded into the
  PostScript output.  Any PostScript-valid string is acceptable.  One
  should note that a PostScript file is a program and the user, if
  inserting PostScript code into the program using this escape, should
  beware of any side effects the inserted code may have on the rest of
  the output.
  </dd>
  </dl>
  <dl>
  <dt><b> PS_IMAGE_RED_LUT,  PS_IMAGE_GREEN_LUT,  PS_IMAGE_BLUE_LUT</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line=' PS_IMAGE_RED_LUT,  PS_IMAGE_GREEN_LUT,  PS_IMAGE_BLUE_LUT' -->
  <dd>Download a new lookup table (LUT) for, respectively,
  the red, green, and blue components of the IMAGE lookup table.  The
  imaging model is a very simple one based on strict interpretation of
  the GIO gputcell() call.  A cell consistes of an array of values
  between 0 and 255.  If no image LUT is defined, the cells are
  rendered as grayscale images by the PostScript.  However, through
  these three escapes, an arbitrary LUT may be defined.  Each component
  of the LUT is an array PS_IMAGE_LUT_SIZE long (256).  Each value of
  the array is from 0 (no color) to 255 (saturation).  If the output
  PostScript devices supports color, the image will be rendered using
  the colors defined by the three LUT's.  If it doesn't, then the three
  LUT's are combined to define a grayscale LUT to render the image.
  See also the PS_IMAGE_LUT escape code below.
  </dd>
  </dl>
  <dl>
  <dt><b>PS_GR_RED_LUT, PS_GR_GREEN_LUT, PS_GR_BLUE_LUT</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='PS_GR_RED_LUT' Line='PS_GR_RED_LUT, PS_GR_GREEN_LUT, PS_GR_BLUE_LUT' -->
  <dd>Download a new lookup table (LUT) for, respectively,
  the red, green, and blue components of the graphics LUT.  In GIO,
  graphics color is defined by an arbitrary integer.  That integer is
  used to index into the three LUT's to determine the desired color.
  The default configuration defines a 16 entry LUT containing the color
  definitions defined by the tvmark task.  To change the
  default, use these escape sequences.  The array of length
  PS_GR_LUT_SIZE (16) contains values 0 (no color) to 255 (saturation).
  All three LUT's must be defined.  Though the nominal length is 16, any
  sized arrays can be used, as long as all three arrays are of the same
  length.
  See also the PS_GRAPHICS_LUT escape code below.
  </dd>
  </dl>
  <dl>
  <dt><b>PS_IMAGE_LUT, PS_GRAPHICS_LUT</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='PS_IMAGE_LUT' Line='PS_IMAGE_LUT, PS_GRAPHICS_LUT' -->
  <dd>Define a new graphics/image LUT from the
  specified file name.  The array contains a string with the file
  name containing the LUT.  See the discussion under <span style="font-family: monospace;">"COLOR"</span> for an
  explanation of the LUT table file.
  </dd>
  </dl>
  <dl>
  <dt><b>PS_ROMAN_FONT, PS_GREEK_FONT, PS_ITALIC_FONT, PS_BOLD_FONT</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='PS_ROMAN_FONT' Line='PS_ROMAN_FONT, PS_GREEK_FONT, PS_ITALIC_FONT, PS_BOLD_FONT' -->
  <dd>Specify a new PostScript font for,
  respectively, the GIO Roman, Greek, Italic, and Bold fonts.  The array
  contains a string which has the name of the PostScript font to used
  when the corresponding GIO font is selected.
  </dd>
  </dl>
  <dl>
  <dt><b>PS_VARIABLE_SPACE</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='PS_VARIABLE_SPACE' Line='PS_VARIABLE_SPACE' -->
  <dd>Flag indicating whether characters written out
  by the GIO gtext call should be variable-spaced or mono-spaced.  The
  instruction array should contain just one value, YES or NO to use,
  respectively, variable spacing or not.  The default is to use variable
  spacing.  However, the GIO paradigm is a mono-spaced paradigm and some
  programs may use this feature in placing text.  Using this escape
  sequence will guarantee that the characters are placed correctly.
  </dd>
  </dl>
  <dl>
  <dt><b>PS_DASH, PS_DOT, PS_SPACE</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='PS_DASH' Line='PS_DASH, PS_DOT, PS_SPACE' -->
  <dd>Change the sizes of a dash, a dot, and the space between
  them.   The instruction array contains a single value determining the
  length, in GKI units, of the respective dash, dot, and space patterns.
  By default, the sizes are 400, 40, and 200 respectively.  These sizes
  can also be changed in the graphcap (see below).
  </dd>
  </dl>
  <dl>
  <dt><b>PS_FILL_PATTERN</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='PS_FILL_PATTERN' Line='PS_FILL_PATTERN' -->
  <dd>Add/change fill patterns used by the GIO gfill
  command.  In GIO, the fill pattern is specified by an arbitrary
  integer.  The first three patterns, 0, 1, 2, are always clear, solid,
  and hollow fill patterns and cannot be changed.  However, patterns 3
  and up are arbitrary.  PSIKern defines patterns 3-6 as: verticle line,
  horizontal line, diagonal increasing to the right, diagonal increasing
  to the left.  The PSIKern uses a proto-type filling algorithm,
  specifically program 15 from the _PostScript Language: Tutorial and
  CookBook_.  This program uses 8 values between 0 and 255 to define 8
  rows of bit patterns that create the fill pattern.  Thus, the
  instruction array will have as its first value, the number of the fill
  pattern to be replaced/added.  The next 8 values define the fill
  pattern.
  </dd>
  </dl>
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The first set of examples deal with defining graphcap entries for a
  psikern device.
  </p>
  <p>
  1. Three default graphcap entries for a psikern device.  The common
  graphcap entry is <span style="font-family: monospace;">"psi_def"</span>, and the landscape and portrait modes are
  defined as <span style="font-family: monospace;">"psi_land"</span> and <span style="font-family: monospace;">"psi_port"</span> respectively.  The output device
  is assumed to be a standard 8.5x11 inch paper.  The file is not sent
  to a printer, but the name is simply echoed to standard output when
  the plot is flushed from the GIO buffer (note DD parameter in psi_def).
  </p>
  <div class="highlight-default-notranslate"><pre>
  psi_port|psidbgp|PostScript Kernel default portrait:\
          :ar#1.3241525:ch#.02:cw#.02644:\
          :xr#2313:xs#0.1959:yr#3063:ys#0.2594:PT:
          :tc=psi_def:
  
  psi_def|psi_land|Postscript Kernel Default 8.5x11in 300dpi Landscape:\
          :ar#0.7552:ca:ch#.02644:co#80:cw#.02:fa:fs#6:\
          :kf=develop$psikern/xx_psikern.e:\
          :li#24:lt#4:pl:pm:se:tf#4:tn=psikern:tq#1:tx:xr#3063:xs#0.2594:\
          :yr#2313:ys#0.1959:zr#256:\
          :BO:\
          :DD=psi_def,tmp$psk,!{ echo $F; }&amp;:\
          :FB=Times-Bold:FG=Symbol:FI=Times-Italic:FR=Times-Roman:\
          :IF=develop$psikern_prolog.ps:\
          :LG=st4gem$lib/invxgterm:\
          :MF#100:PI#1.:PW#.00011:TD#.01221:TP#.001221:TS#.006104:\
          :XO#0.01:YO#0.01:
  </pre></div>
  <p>
  Once these entries are placed in the <span style="font-family: monospace;">"dev$graphcap"</span> file, a user can
  use the devices by specifying the device name in a task's <span style="font-family: monospace;">"device"</span>
  parameter.  For example, to get a PostScript file of the output from
  the 'prow' task, a user would do the following:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prow dev$pix 256 device=psi_land
  cl&gt; gflush
  /tmp/pskXXXX
  </pre></div>
  <p>
  The file <span style="font-family: monospace;">"/tmp/pskXXXX"</span> is the PostScript file of the output from
  prow.
  </p>
  <p>
  If the user will always be using a psikern device, they need only
  change their <span style="font-family: monospace;">"login.cl"</span> file or add the following to their
  <span style="font-family: monospace;">"loginuser.cl"</span> file, to change the default graphics output device:
  </p>
  <div class="highlight-default-notranslate"><pre>
  set stdplot=psi_land
  </pre></div>
  <p>
  Then, whenever a user uses the <span style="font-family: monospace;">"snap"</span> feature of the graphics cursor,
  or uses the device <span style="font-family: monospace;">"stdplot"</span>, their output will appear on the
  specified device.	
  </p>
  <p>
  2. Define two graphcap entries, making use of the default entries in
  example 1, where the PostScript file is sent to a printer queue.  The
  host operating system is some flavor of UNIX and the printer queue
  name is <span style="font-family: monospace;">"lw"</span>.  The two entries send the plot in either landscape or
  portrait mode, depending on the entry.  Note that the host operating
  system command will remove the temporary file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  psi_lw_land|PostScript Kernel send output to queue lw, LandScape:\
          :DD=psi_def,tmp$psk,!{ lpr -Plw $F; rm $F ;}&amp;:\
          :tc=psi_land:
  psi_lw_port|PostScript Kernel send output to queue lw, Portrait:\
          :DD=psi_def,tmp$psk,!{ lpr -Plw $F; rm $F ;}&amp;:\
          :tc=psi_port:
  </pre></div>
  <p>
  3. Define two graphcap entries, making use of the entries defined in
  example 2, where the drawn lines are thinner.
  </p>
  <div class="highlight-default-notranslate"><pre>
  psi_lw_land_thin|PostScript Kernel, thin lines, LandScape, queue lw:\
          :PW#0.00008:PI#0.5:tc=psi_lw_land:
  psi_lw_port_thin|PostScript Kernel, thin lines, Portrait, queue lw:\
          :PW#0.00008:PI#0.5:tc=psi_lw_port:
  </pre></div>
  <p>
  4. Define a graphcap entry, using entries in example 1, which has an
  aspect ratio of unity, i.e. a square output device.  Just echo the
  file name.  Such an entry is useful if one wants to include the
  PostScript in another PostScript, TeX, or other word processing
  document that can include PostScript.
  </p>
  <div class="highlight-default-notranslate"><pre>
  psi_square|PostScript Kernel square viewport:\
          :PT:xs#0.1959:ys#0.1959:ar#1:cw#.02:ch#.02:\
          :XO#0.01:YO#0.0581:xr#2313:yr#2313:\
          :tc=psi_def:
  </pre></div>
  <p>
  The following examples demonstrate how to use the psikern as a
  task.
  </p>
  <p>
  5. Capture the output of the prow task in a metacode file and
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
  6. Produce a PostScript file from a GKI metacode file.  However,
  instead of using the default name generated by psikern itself, place
  the PostScript into a specific file, here <span style="font-family: monospace;">"prow.ps"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prow dev$pix 101 &gt;G prow.gki
  cl&gt; psikern prow.gki device=psi_land output=prow.ps
  </pre></div>
  <p>
  7. Use a different set of fonts than that specified for any device
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
  8. Change the spacing of characters.  By default, psikern renders
  characters using proportional spacing.  However, GIO and many tasks
  assume the character spacing is constant, or monospace.  Render a
  graphics output using monospaced characters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prow dev$pix 101 &gt;G prow.gki
  cl&gt; psikern prow.gki device=psi_land proportional-
  </pre></div>
  <p>
  9. Changing colors of a graphics output from an IRAF task that does
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
  10. Define and use the suggested color table, <span style="font-family: monospace;">"invxgterm"</span>.  This
  table is a text table and has the following contents.  Note that this
  table is distributed with ST4GEM in the file
  <span style="font-family: monospace;">"st4gem$lib/invxgterm"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Inverse xgterm colormap for psikern.
  # This is different from the standard xgterm color map
  # where the foreground/background are inverted.
  # This is so the background is white, as is most
  # paper, and the foreground is black, as in most writing on paper.
  #
  # Each color component is specfied from units of 0. (no color)
  # to 1. (full color)
  #
  # The columns are:
  # Index red     green   blue    name (optional)
  #
  # Define the default background/foreground
  #
  0       1.      1.      1.      white
  1       0.      0.      0.      black
  #
  # The following colors are color2 through color9 of xgterm's default
  # coloring.
  #
  2       1.      0.      0.      red
  3       0.      1.      0.      green
  4       0.      0.      1.      blue
  5       0.      1.      1.      cyan
  6       1.      1.      0.      yellow
  7       1.      0.      1.      magenta
  8       0.63    0.13    0.94    purple
  9       0.18    0.31    0.31    darkslategray
  #
  # Just to round things out, finish defining the colors up
  # through color 15.  Use the tvmark colormap for the definition.
  #
  10      1.      0.65    0.      orange
  11      0.94    0.90    0.55    khaki
  12      0.85    0.44    0.84    orchid
  13      0.25    0.88    0.82    turquoise
  14      0.93    0.51    0.93    violet
  15      0.96    0.87    0.70    wheat
  </pre></div>
  <p>
  This table can be accessed either through the <span style="font-family: monospace;">"LG"</span> graphcap parameter
  (see example 1 in the <span style="font-family: monospace;">"psi_def"</span> graphcap entry), or by specifying the
  name of the file in the 'graphics_lut' parameter:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prow dev$pix 101 &gt;G prow.gki
  cl&gt; psikern prow.gki device=psi_land graphics_lut=invxterm
  </pre></div>
  <p>
  11.  Define a two-color graphics lookup table.  Many PostScript
  devices are laser printers.  Though they render color as different
  levels of gray, the output may not be pleasing.  One can force black
  on white by using a two-color graphics lookup table.  The contents of
  such a table would be as follows.  Note that ST4GEM distributes this
  table in the file <span style="font-family: monospace;">"lib$mono"</span>
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Monochrome colormap for psikern output.
  #
  # Each color component is specfied from units of 0. (no color)
  # to 1. (full color)
  #
  # Index red     green   blue    name (optional)
  0       1.      1.      1.      white
  1       0.      0.      0.      black
  </pre></div>
  <p>
  12.  A user has written an IGI script which requires a 256 color
  graphics LUT, which mimics a rainbow from red to magenta.  The
  contents of the LUT would be as follows.  Note that ST4GEM distributes
  this table in the file <span style="font-family: monospace;">"lib$rain256"</span>.  This table demonstrates the
  use of the color interpolation that psikern provides.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # 256 rainbow colormap for psikern
  #
  # Each color component is specfied from units of 0. (no color)
  # to 1. (full color)
  #
  # The columns are:
  # Index red     green   blue    name (optional)
  #
  # Define the default background/foreground
  #
  0       1.      1.      1.      white
  1       0.      0.      0.      black
  #
  # Colors 2-257 define the 256 color rainbow.  Since psikern will
  # interpolate for missing colors, we need only define
  # "control" colors.
  #
  2       1.      0.      0.      red
  53      1.      1.      0.      yellow
  104     0.      1.      0.      green
  155     0.      1.      1.      cyan
  206     0.      0.      1.      blue
  257     1.      0.      1.      magenta
  </pre></div>
  <p>
  13.  A user has written an IGI script which renders an image.  However,
  the user would like to use a 256 color image LUT, which mimics a rainbow from red to magenta.  The
  contents of the LUT would be as follows.  The only difference between
  the table below and the one in example 12 is that an image LUT need
  not worry about background/foreground colors.  Hence the first two
  entries can be a part of the whole color continuum.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # 256 rainbow colormap for psikern for images
  #
  # Each color component is specfied from units of 0. (no color)
  # to 1. (full color)
  #
  # The columns are:
  # Index red     green   blue    name (optional)
  #
  # Colors 0-255 define the 256 color rainbow.  Since psikern will
  # interpolate for missing colors, we need only define
  # "control" colors.
  #
  0       1.      0.      0.      red
  51      1.      1.      0.      yellow
  102     0.      1.      0.      green
  153     0.      1.      1.      cyan
  204     0.      0.      1.      blue
  255     1.      0.      1.      magenta
  </pre></div>
  <p>
  This table would be used as a new graphcap entry which defines the
  <span style="font-family: monospace;">"LI"</span> parameter:
  </p>
  <div class="highlight-default-notranslate"><pre>
  psi_256colorimage|PostScript with 256 color image LUT:\
          :LI="image256rainbow":tc=psi_def:
  </pre></div>
  <p>
  Or, the table could be specified in the <span style="font-family: monospace;">"image_lut"</span> parameter of
  psikern itself:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; igi &lt;image.igi &gt;G igi.gki
  cl&gt; psikern igi.gki device=apsikerndevice\
  image_lut="image256rainbow"
  </pre></div>
  <p>
  The following examples demonstrate SPP code to use the GIO escape
  codes to modify the output from psikern.
  </p>
  <p>
  14. Download an arbitrary string of PostScript to the kernel.  This
  example just downloads some point and drawing commands.
  </p>
  <div class="highlight-default-notranslate"><pre>
  include &lt;psiescape.h&gt;
  ...
  short  sarray[SZ_LINE]
  string pscode "save 100 100 moveto 0 50 rlineto stroke restore"
  ...
  call achtcs (pscode, sarray, strlen(pscode))
  call gescape (gp, PS_CODE, sarray, strlen(pscode))
  </pre></div>
  <p>
  15. Download a new set of image lookup tables.
  </p>
  <div class="highlight-default-notranslate"><pre>
  include &lt;psiescape.h&gt;
  ...
  short   red_lut[PS_IMAGE_LUT_SIZE],
  short   green_lut[PS_IMAGE_LUT_SIZE]
  short   blue_lut[PS_IMAGE_LUT_SIZE]
  ...
  # Fill the LUT arrays.
  ...
  call gescape (gp, PS_IMAGE_RED_LUT,   red_lut,   PS_IMAGE_LUT_SIZE)
  call gescape (gp, PS_IMAGE_GREEN_LUT, green_lut, PS_IMAGE_LUT_SIZE)
  call gescape (gp, PS_IMAGE_BLUE_LUT,  blue_lut,  PS_IMAGE_LUT_SIZE)
  </pre></div>
  <p>
  16. Download a new set of graphics lookup tables.
  </p>
  <div class="highlight-default-notranslate"><pre>
  include &lt;psiescape.h&gt;
  ...
  short   red_lut[PS_GR_LUT_SIZE],
  short   green_lut[PS_GR_LUT_SIZE]
  short   blue_lut[PS_GR_LUT_SIZE]
  ...
  # Fill the LUT arrays.
  ...
  call gescape (gp, PS_GR_RED_LUT,   red_lut,   PS_GR_LUT_SIZE)
  call gescape (gp, PS_GR_GREEN_LUT, green_lut, PS_GR_LUT_SIZE)
  call gescape (gp, PS_GR_BLUE_LUT,  blue_lut,  PS_GR_LUT_SIZE)
  </pre></div>
  <p>
  17. Change the font name associated with the GIO Roman font.
  </p>
  <div class="highlight-default-notranslate"><pre>
  include &lt;psiescape.h&gt;
  ...
  short   sarray[SZ_LINE]
  ...
  call achtcs ("Courier", sarray, strlen("Courier"))
  call gescape (gp, PS_ROMAN_FONT, sarray, strlen("Courier"))
  </pre></div>
  <p>
  18. Change the text writing mode from Variable spaced to Mono-spaced
  and back.
  </p>
  <div class="highlight-default-notranslate"><pre>
  include &lt;psiescape.h&gt;
  ...
  short   flag
  ...
  call gtext (gp, ...
  ...
  flag = NO
  call gescape (gp, PSI_VARIABLE_SPACE, flag, 1)
  ...
  call gtext (gp, ...
  ...
  flag = YES
  call gescape (gp, PSI_VARIABLE_SPACE, flag, 1)
  ...
  call gtext (gp, ...
  </pre></div>
  <p>
  19. Change the size of the dots, dashes, and spaces of the line
  patterns.
  </p>
  <div class="highlight-default-notranslate"><pre>
  include &lt;psiescape.h&gt;
  ...
  short dash_size, dot_size, space_size
  ...
  dash_size  = 400
  dot_size   = 40
  space_size = 200
  call gescape (gp, PS_DASH,  dash_size,  1)
  call gescape (gp, PS_DOT,   dot_size,   1)
  call gescape (gp, PS_SPACE, space_size, 1)
  </pre></div>
  <p>
  20. Add a fill pattern, 6,  that is a horizontal line pattern (same as
  pattern 4 in the default system).
  </p>
  <div class="highlight-default-notranslate"><pre>
  include &lt;psiescape.h&gt;
  ...
  short sarray[PS_FILL_SIZE]
  real x[5], y[5]         # Boundaries of the fill box.
  ...
  sarray[1] = 6           # Fill pattern 6.
  sarray[2] = 0ffx
  sarray[3] = 0
  sarray[4] = 0
  sarray[5] = 0
  sarray[6] = 0ffx
  sarray[7] = 0
  sarray[8] = 0
  sarray[9] = 0
  call gescape (gp, PS_FILL_PATTERN, sarray, PS_FILL_SIZE)
  # Now use it.
  call gfill (gp, x, y, 6)
  </pre></div>
  <p>
  21.  Change both the image and graphics lookup tables.
  </p>
  <div class="highlight-default-notranslate"><pre>
  include &lt;psiescape.h&gt;
  ...
  short  sarray[SZ_LINE]
  char   carray[SZ_LINE]
  ...
  call clgstr ("image_lut", carray, SZ_LINE
  l = strlen (carray)
  call achtcs (carray, sarray, l)
  call gescape (gp, PS_IMAGE_LUT, sarray, l)
  ...
  call clgstr ("graphics_lut", carray, SZ_LINE
  l = strlen (carray)
  call achtcs (carray, sarray, l)
  call gescape (gp, PS_GRAPHICS_LUT, sarray, l)
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The kernel does not recognize changes in the txspacing.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  stdgraph, stdplot, gio$doc/gio.hlp
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

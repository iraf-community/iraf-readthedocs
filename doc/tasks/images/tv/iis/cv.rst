.. _cv:

cv: Control image device, display "snapshot"
============================================

**Package: iis**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  cv
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_snap_file">
  <dt><b>snap_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='snap_file' Line='snap_file' -->
  <dd>Output file for snap image.
  </dd>
  </dl>
  <dl id="l_textsize">
  <dt><b>textsize</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='textsize' Line='textsize' -->
  <dd>Character size for added text strings.
  </dd>
  </dl>
  </section>
  <section id="s_commands">
  <h3>Commands</h3>
  <p>
  The following commands are available.  This list is also available when
  running the task with the commands h(elp) or ?.
  </p>
  <div class="highlight-default-notranslate"><pre>
  --- () : optional; [] : select one; N : number; C/F/Q : see below
  b(link) N F (C Q) (F (C Q)..)   blink   (N = 10 is one second)
  c(ursor) [on off F]             cursor
  di F (C Q) [on off]             display image
  dg C (F Q) [on off]             display graphics
  e(rase) [N a(ll) g(raphics) F]  erase (clear)
  m(atch) (o) F (C) (to) (F) (C)  match (output) lookup table
  o(ffset)  C N                   offset color (N: 0 to +- 4095)
  p(an) (F)                       pan images
  ps(eudo) (o) (F C) (rn sn)      pseudo color mapping
                                  rn/sn: random n/seed n
  r(ange) N (C) (N C ...)         scale image (N: 1-8)
  re(set) [r i t a]               reset display
                                  registers/image/tables/all
  sn(ap) (C)                      snap a picture
  s(plit) [c o px,y nx,y]         split picture
  t(ell)                          tell display state
  w(indow) (o) (F C)              window (output) frames
  wr(ite) [F C] text              write text to frame/graphics
  z(oom) N (F)                    zoom frames (N: 1-8)
  x   or   q                      exit/quit
  --- C: letter c followed by r/g/b/a or, for snap r,g,b,m,bw,rgb,
  ---   or for dg r/g/b/y/p/m/w, as 'cr', 'ca', or 'cgb'
  --- F: f followed by a frame number or <span style="font-family: monospace;">'a'</span> for all
  --- Q: q followed by quadrant number or t,b,l,r for top, bottom,...
  </pre></div>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>cv</i> program is used to control the image display from within
  <i>IRAF</i>.  It differs from most <i>IRAF</i> programs since it has its
  own prompt and its own internal <span style="font-family: monospace;">"language"</span>.  Each of the available commands
  is described in the following paragraphs, but first a few comments on the
  command structure seem in order.  Commands are distinguished by their
  first letter, except for a few instances where the second letter is needed.
  The rest of the command name can be typed if you wish.  Commands often
  require specification of frames numbers, colors, quadrants, or numeric
  values.  In most cases, the order is unimportant,  but, zoom, for instance,
  does require the zoom power right after the command name.  The order given
  in the <i>help</i> command will always work.
  </p>
  <p>
  A frame list is indicated in the <i>help</i> listing with an <b>F</b>.  This
  is to be replaced in the typed command by an <b>f</b> followed (no spaces)
  with a list of the pertinent image planes.  Thus, <b>f1</b> means
  <i>frame 1</i> while <b>f42</b> means <i>frames 4</i>
  and <i>2</i>.  In most cases, the leading <b>f</b> can be omitted.
  The specification <b>fa</b> means <i>all frames</i>.  In those
  cases in the <i>help</i> menu where the frame specification is optional,
  omitting the frame list is the same as typing <b>fa</b>; that is, operate
  on <i>all</i> frames.
  </p>
  <p>
  A color specification is a <b>c</b> followed by a set of letters.
  The letter <b>a</b> means <i>all</i>, just as in the frame specification.
  The letters <b>r, b,</b> and <b>g</b> are the other possibilities for all
  commands other than <i>dg</i> and <i>snap</i>.  For displaying graphics
  planes (<b>dg</b>), the other possibilities are <b>y, p, m, w</b> which
  stand for <i>yellow, purple, mauve,</i> and <i>white</i>.  (<i>Mauve</i> is
  the wrong name and will get changed.)  The <i>snap</i> command accepts, in
  addition to the standard three colors, <b>m, bw,</b> and <b>rgb</b>, which
  stand for <i>monochrome, black and white,</i> and <i>full color</i>.  (See
  the discussion under <i>snap</i> for further explanation.)
  An omitted color specification is the same as <i>all colors</i>.
  </p>
  <p>
  Quadrants are given by a <b>q</b> followed by numbers from the set one through
  four, or the letter <b>a</b> as in the frame and color cases.  Quadrants are
  numbered in the standard way, with the upper right being <i>1</i>, the upper
  left <i>2</i>, etc.  Adjacent quadrants may be referenced by <b>t, b, l,</b>
  and <b>r</b>, standing for <i>top, bottom, left,</i> and <i>right</i>.  An
  omitted quadrant specification is the same as <i>all quadrants</i>.  Quadrants
  are effective only if the split screen command has set the split point to
  something other than the <span style="font-family: monospace;">"origin"</span>.
  </p>
  <dl>
  <dt><b><b>blink</b> N F (C Q) (F C Q)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBblink\fR N F (C Q) (F C Q)' -->
  <dd>The blink rate is given by <b>N</b>, which is in tenths of a second.  Although
  current timing routines in <i>IRAF</i> do not recognize partial seconds,
  for the NOAO 4.2BSD UNIX implementation, a non-portable timing routine is
  used so that tenth seconds are usable.
  Erratic timing is pretty much the rule when the system load is large.
  One frame must be given,
  followed by any color or quadrant specification, and then
  optionally followed by any number of similar triads.  A specification of
  <i>10 f12 f3 f3 f4</i> would display frames one and two for one second, then
  frame three for two one second intervals, then frame 4, and then recycle.
  The first blink cycle may appear somewhat odd as the code <span style="font-family: monospace;">"settles in"</span>,
  but the sequence should become regular after that (except for timing
  problems due to system load).  In split screen mode, it is necessary to
  specify all the frames together with quadrants, which leads to a lot of
  typing:  The reason is that blink simply cycles through a series of
  <b>di</b> commands, and hence it requires the same information as that
  command.
  </dd>
  </dl>
  <dl>
  <dt><b><b>cursor</b> [on off F]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBcursor\fR [on off F]' -->
  <dd>This command is used to turn the cursor on or off, and to read coordinates
  and pixel values from a frame.  Pixel coordinates for a feature are those
  of the image as loaded into the display, and do not change as the image
  is panned or zoomed.  Fractional pixel positions are given for zoomed
  images, with a minimum number of decimal places printed (but the same number
  for both the <i>x</i> and <i>y</i> coordinates).
  For an unpanned, unzoomed image plane, the lower left corner
  of the <i>screen</i> is (1,1)
  even if the image you loaded is smaller than 512x512, occupies only
  a portion of the display screen, and does not extend to the lower left
  corner of the screen.  This defect will likely be remedied
  when the <i>cv</i> package is properly integrated into <i>IRAF</i>.
  Pixel information can be read from a frame that is not being displayed.
  </dd>
  </dl>
  <dl>
  <dt><b><b>di</b> F (C Q) [on off]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBdi\fR F (C Q) [on off]' -->
  <dd>The <i>d</i>isplay <i>i</i>mage command selects frames to be displayed on the
  monitor.  If neither <i>on</i> or <i>off</i> is given, the specified frames
  are turned on and all others are turned off.  Turning a frame on with
  the <i>on</i> specification displays the frames along with whatever else
  is present; that is the new frame is added to the display.  Note that
  turning a frame off does not erase it.  A frame need not have all colors
  turned on, nor appear in all quadrants of a split screen display.
  </dd>
  </dl>
  <dl>
  <dt><b><b>dg</b> C (F Q) [on off]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBdg\fR C (F Q) [on off]' -->
  <dd>The <i>d</i>isplay <i>g</i>raphics command turns specific graphics planes
  on or off.  For the IIS display, neither the frame nor the quadrant
  parameters are relevant.  A side-effect of this command is that it
  resets the graphics hardware to the <i>cv</i> standard: red cursor and
  seven graphics planes, each colored differently.  If the display is in
  a <span style="font-family: monospace;">"weird"</span> state that is not cured with the <i>reset r/t</i> commands,
  and a <i>reset i</i> would destroy images of interest, try a <i>dg ca on</i>
  command followed by <i>dg ca off</i>.
  </dd>
  </dl>
  <dl>
  <dt><b><b>erase</b> [F all graphics]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBerase\fR [F all graphics]' -->
  <dd>This command erases the specified frame, or all the graphics planes, or
  all data planes.  The command <b>clear</b> is a synonym.
  </dd>
  </dl>
  <dl>
  <dt><b><b>match</b> (o) (F) (C) (to) (F) (C)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBmatch\fR (o) (F) (C) (to) (F) (C)' -->
  <dd>This command allows the user to copy a look-up table to a specified set
  of tables, and hence, to match the mapping function of frames (and/or
  colors) to a reference table.  If the <b>o</b> parameter is omitted, the
  match is among the look-up tables associated with particular frames;
  otherwise, the <i>ouput</i> tables are used (hence, the <b>o</b>).  In the
  latter case, only colors are important; the frame information should
  be omitted.  For the individual frame tables, colors can be omitted, in
  which case a match of frame one to two means to copy the three tables
  of frame two (red, green, and blue) to those of frame one.  Only one
  reference frame or color should be given, but <i>match f23 cgb f1 cr</i>
  is legal and means to match the green and blue color tables of both
  frames two and three to the red table of frame one.
  </dd>
  </dl>
  <dl>
  <dt><b><b>offset</b> C N</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBoffset\fR C N' -->
  <dd>The value N, which can range from -4095 to +4095 is added to the data
  pipeline for color <b>C</b>, thus offsetting the data.  This is useful
  if one needs to change the data range that is mapped into the useful part
  of the output tables.
  </dd>
  </dl>
  <dl>
  <dt><b><b>pan</b> (F)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBpan\fR (F)' -->
  <dd>When invoked, this command connects the trackball to the specified frames
  and allows the user to move (pan/roam/scroll) the image about the screen.
  This function is automatically invoked whenever the zoom factor is changed.
  </dd>
  </dl>
  <dl>
  <dt><b><b>pseudo</b> (o) (F C) (rn sn)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBpseudo\fR (o) (F C) (rn sn)' -->
  <dd>Look-up tables are changed with the <i>window</i> and the <i>pseudocolor</i>
  commands.  Windowing provides linear functions and is discussed under that
  command; <i>pseudo</i> provides pseudo-coloring capabilities.  Pseudo-color
  maps are usually best done in the output tables, rather than in the
  look-up tables associated with particular frames; hence, <b>ps o</b> is
  the more likely invocation of the start of the command line.  A color
  (or colors) can be specified for <span style="font-family: monospace;">"output"</span> pseudocolor, in which case, only
  those colors will be affected.  For frame look-up tables,
  the frame must be specified.
  Two mappings are provided.  One uses a set of randomly selected colors
  mapped to a specified number of pixel value ranges.  The other uses
  triangle color mappings.  The former is invoked with the <i>(rn sn)</i>
  options.  In this case, the number following <b>r</b> gives the number of
  ranges/levels into which the input data range is to be divided; to
  each such range, a randomly selected color is assigned.  The number
  following <b>s</b> is a seed for the random number generator;  changing
  this while using the same number of levels gives different color mappings.
  The default seed is the number of levels.  If only the seed is given (<b>r</b>
  omitted), the default number of levels is 8.  This mapping is used when
  a contour type display is desired:  each color represents an intensity range
  whose width is inversely proportional to the number of levels.
  The triangle mapping uses a different triangle in each of the three look-up
  tables (either the sets associated with the specified frames, or the output
  tables).  The initial tables map low intensity to blue, middle values to
  green, and high values to red, as shown in the diagram. (The red and blue
  triangles are truncated as their centers are on a table boundary.)
  Once invoked, the program then allows the user to adjust the triangle
  mapping.  In
  response to the prompt line, select the color to be changed and move the
  trackball:  the center of the triangle is given by the <i>x</i> cursor
  coordinate and the width by the <i>y</i> coordinate.  Narrow functions
  (small <i>y</i>) allow one to map colors to a limited range of intensity.
  When the mapping is satisfactory, a press of any button <span style="font-family: monospace;">"fixes"</span> the
  mapping and the user may then either select another color or exit.
  Before selecting a color, place the cursor at approximately the default
  position for the mapping (or where it was for the last mapping of that
  color under the current command); otherwise, the color map will change
  suddenly when the color is selected via the trackball buttons.
  </dd>
  </dl>
  <dl>
  <dt><b><b>range</b> N (C) (N C ...)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBrange\fR N (C) (N C ...)' -->
  <dd>This command changes the range function in the specified color pipeline
  so that the data is scaled by (divided by) the value <b>N</b>.  For the
  IIS, useful range values are 1,2,4 and 8;  anything else will be changed
  to the next lowest legal value.
  </dd>
  </dl>
  <dl>
  <dt><b><b>reset</b> [r i t a]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBreset\fR [r i t a]' -->
  <dd>Various registers and tables are reset with this command.  If the <b>r</b>
  option is used, the registers are reset.  This means that zoom is set to
  one, all images are centered, split screen is removed, the range values are
  set to one and the offset values are set to zero.  Also, the cursor is
  turned on and its shape is set.  Option <b>i</b> causes all the image and
  graphics planes to be erased and turned off.  Option <b>t</b> resets all
  the look-up tables to their default linear, positive slope, form, and
  removes any color mappings by making all the output tables the same, and
  all the frame specific tables the same.  Option <b>a</b> does <i>all</i>
  the above.
  </dd>
  </dl>
  <dl>
  <dt><b><b>snap</b> (C)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBsnap\fR (C)' -->
  <dd>This command creates an <i>IRAF</i> image file whose contents are a
  512x512 digital snapshot of the image display screen.  If no color
  is specified,
  or if <i>cm</i> (color monochromatic) is given,
  the snapshot is of the <i>blue</i> image, which, if you
  have a black and white image, is the same as the red or the green
  image.  Specifying <b>cg</b> for instance will take a snapshot of the
  image that you would get had you specified <i>cg</i> for each frame
  turned on by the <i>di</i> command.  Color is of interest only when
  the window or pseudo color commands have made the three colors distinguishable.
  If the <span style="font-family: monospace;">"snapped"</span> image is intended to be fed to the Dicomed film
  recorder, a black and white image is all that is usually provided and so
  a color snap is probably not appropriate.
  In the case of the <span style="font-family: monospace;">"no color/monochromatic"</span> snap, the graphics planes are
  all added together, while, if a real color is given, only the graphics
  planes that have some of that color are included in the image.
  The color <b>rgb</b> can be
  given, in which case the red, green, and blue images are weighted equally
  to produce a single image file.  This image does not represent well what
  you see, partly because of the equal weight given all colors: some
  mapping of eye sensitivity is probably what is required, but it is not
  implemented.
  The program operates by first determining zoom, pan, offset, tables, etc,
  and, for each quadrant of the split screen, which images planes are active.
  Then, for each line of the display, those images are read out from the display's
  memory and the transformations done in hardware are duplicated pixel by pixel
  in software.  The word <span style="font-family: monospace;">"active"</span> needs a bit of explanation.  Any image plane
  whose pixels are contributing to the image is active.  No image is active if
  it has been turned off (by the <i>di</i>) command (or if all images were
  turned off and the one of interest not subsequently turned back on).  If the
  image is all zeroes, or if it is not but split screen is active and the
  part of the image being displayed is all zeroes, it is not contributing to
  the output.  However, the snap program cannot tell that an active image is
  not contributing anything useful,
  and so it dutifully reads out each pixel and adds zeroes to the output.
  The moral of this is that frames of no interest should be (turned) off before
  snap is called (unless you don't have anything better to do than wait for
  computer prompts).  When split screen is active, frames are read only for
  the quadrants in which they are active.
  The fastest snaps are for single images that are zoomed but not panned
  and which are displayed (and snapped) in black and white, or snapped
  in a single color.
  </dd>
  </dl>
  <dl>
  <dt><b><b>split</b> [c o px,y nx,y]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBsplit\fR [c o px,y nx,y]' -->
  <dd>This command sets the split screen point.  Option <b>c</b> is shorthand for
  <i>center</i>, which is the normal selection.  Option <b>o</b> stands for
  <i>origin</i>, and is the split position that corresponds to no split screen.
  If you wish to specify the split point in pixels, use the <b>px,y</b> form, in
  which the coordinates are given as integers.  If you prefer to specify
  the point in NDC (which range from 0 though 1.0), use the <b>nx,y</b> form
  in which the coordinates are decimal fractions.
  A peculiarity of the IIS hardware is that if no split screen is desired,
  the split point must be moved to the upper left corner of the display, rather
  than to the lower left (the <i>IRAF</i> 1,1 position).  This means that no
  split screen (the <b>o</b> option, or what you get after <b>re r</b>) is really
  split screen with only quadrant <b>four</b> displayed:  if you use the <i>di</i>
  command with quadrant specification, only quadrant 4 data will be seen.
  </dd>
  </dl>
  <dl>
  <dt><b><b>tell</b></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBtell\fR' -->
  <dd>This command displays what little it knows about the display status.  At
  present, all it can say is whether any image plane is being displayed, and
  if any are, what is the number of one of them.  This rather weak performance
  is the result of various design decisions both within <i>cv</i> and the
  <i>IRAF</i> display code, and may be improved.
  </dd>
  </dl>
  <dl>
  <dt><b><b>window</b> (o) (F C)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBwindow\fR (o) (F C)' -->
  <dd>This command operates just as the <i>pseudo</i> command, except that it
  applies a linear mapping to the output look-up tables (if option <b>o</b>
  is used) or to the frame specific tables.  The mapping is controlled by
  the trackball, with the <i>y</i> cursor coordinate supplying the slope
  of the map, and <i>x</i> the offset.  If different mappings are given to
  each color, a form of pseudo-color is generated.
  </dd>
  </dl>
  <dl>
  <dt><b><b>write</b> [F C] text</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBwrite\fR [F C] text' -->
  <dd>This command writes the given text into either an image plane (or planes)
  or into the specified color graphics bit plane(s).  The user is prompted 
  to place the cursor at the (lower left) corner of the text, which is
  then written to the right in roman font.  The user is also asked for
  a text size (default 1.0).  If the text is written into a graphics
  plane, and a <b>snap</b> is requested with no color specification, then
  text in any graphics plane will be included in the image.  A color snap,
  on the other hand, will include graphics text to the extent that the
  text is displayed in that color.
  Text written into an image plane
  will have the same appearance as any <span style="font-family: monospace;">"full on"</span> pixel; that is, text
  in an image plane is written at maximum intensity,
  overwrites the image data,
  and is affected by look-up tables, offsets,
  and so forth, like any other image pixels.
  </dd>
  </dl>
  <dl>
  <dt><b><b>zoom</b> N (F)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='\fBzoom\fR N (F)' -->
  <dd>This command zooms the display to the power given by <b>N</b>.  For the
  IIS, the power must be 1,2,4, or 8; anything else is changed to the next
  lower legal value.  The model 70 zooms all planes together.  The center
  of the zoom is determined by the cursor position relative to the first
  frame specified (if none, the lowest numbered active one).  Once the zoom
  has taken place, the <i>pan</i> routine is called for the specified frames.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  cvl
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'COMMANDS' 'DESCRIPTION' 'SEE ALSO'  -->
  

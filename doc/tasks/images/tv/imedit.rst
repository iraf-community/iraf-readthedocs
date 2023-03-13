.. _imedit:

imedit: Examine and edit pixels in images
=========================================

**Package: tv**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imedit input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of images to be edited.  Images must be two dimensional.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output images.  The list must match the input list or be empty.
  In the latter case the output image is the same as the input image; i.e.
  the edited image replaces the input image.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>The editing commands are entered via a cursor list.  When the task is
  run interactively this will normally be the standard image cursor
  (stdimcur) specified by a null string.  Commands may be read from
  a file.  The file format may be cursor values including the command
  keys, a simple list of positions with the default command given
  by the <i>default</i> parameter, and a regions file, as used in
  the task <b>fixpix</b> and the <b>ccdred</b> package, selected by
  the <i>fixpix</i> parameter.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = ""' -->
  <dd>File in which to record the editing commands which modify the images.
  The display and statistics commands which don't modify the images are
  not recorded.  This file may be used for keeping a record of the
  modifications.  It may also be used as cursor input for other images
  to replicate the same editing operations.
  </dd>
  </dl>
  <dl id="l_display">
  <dt><b>display = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='display' Line='display = yes' -->
  <dd>Display the image during editing?  If yes then the display command,
  given by the parameter <i>command</i>, is used to display the image.
  Normally the display is used when editing interactively and turned
  off when using file input.
  </dd>
  </dl>
  <dl id="l_autodisplay">
  <dt><b>autodisplay = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='autodisplay' Line='autodisplay = yes' -->
  <dd>Automatically redisplay the image after each change?  If the display
  of the image is rapid enough then each change can be displayed as
  it is made by setting this parameter to yes.  However, it is faster
  to accumulate changes and then explicitly redisplay the image.
  When the parameter is no then the image is only redisplayed by
  explicit command.
  </dd>
  </dl>
  <dl id="l_autosurface">
  <dt><b>autosurface = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='autosurface' Line='autosurface = no' -->
  <dd>Automatically display surface plots after each change?  In addition
  to the image display command, the task can display a before and after
  surface plot of the modified region.  This can be done by explicit
  command or automatically after each change.
  </dd>
  </dl>
  <dl id="l_aperture">
  <dt><b>aperture = <span style="font-family: monospace;">"circular"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='aperture' Line='aperture = "circular"' -->
  <dd>Aperture for aperture editing.  Some commands specify the region to
  be edited by a center and radius.  The shape of the aperture is selected
  by this parameter.  The choices are <span style="font-family: monospace;">"circular"</span> and <span style="font-family: monospace;">"square"</span>.  Note that
  this does not apply to commands in which a rectangle is specified by
  selecting the corners.
  </dd>
  </dl>
  <dl id="l_radius">
  <dt><b>radius = 2.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radius' Line='radius = 2.' -->
  <dd>Radius of the aperture for commands selecting an aperture.  For circular
  apertures this is the radius while for square apertures it is half of the
  side of the square.  Note that partial pixels are not used so that a
  circular aperture is not perfectly circular; i.e. if  the center of a
  pixel is within this distance of the center pixel it is modified and
  otherwise it is not.  A radius of zero may be used to select a single
  pixel (with either aperture type).
  </dd>
  </dl>
  <dl id="l_search">
  <dt><b>search = 2.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='search' Line='search = 2.' -->
  <dd>Search radius for adjusting the position of the region to be edited.
  This applies to both aperture regions and rectangular regions.  The
  center pixel of the region is searched within this radius for the
  maximum or minimum pixel value.  If the value is zero then no searching
  is done and the specified region is used directly.  If the value is
  positive then the specified region is adjusted to be centered on a
  relative maximum.  A relative minimum may be found if the value is
  negative with the absolute value used as the search radius.
  </dd>
  </dl>
  <dl id="l_buffer">
  <dt><b>buffer = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='buffer' Line='buffer = 1.' -->
  <dd>Background buffer width.  A buffer annulus separates the region to be
  edited from a background annulus used for determining the background.
  It has the same shape as the region to be edited; i.e. circular, square,
  rectangular, or line.
  </dd>
  </dl>
  <dl id="l_width">
  <dt><b>width = 2.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='width' Line='width = 2.' -->
  <dd>Width of background annulus.  The pixels used for background determinations
  is taken from an annulus of the same shape as the region to be edited and
  with the specified width in pixels.
  </dd>
  </dl>
  <dl id="l_xorder">
  <dt><b>xorder = 2, yorder = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xorder' Line='xorder = 2, yorder = 2' -->
  <dd>Orders (number of terms) of surface polynomial fit to background pixels
  for statistics and background subtraction.  The orders should generally
  be low with orders of 2 for a plane background.  If either order is
  zero then a median background is used.
  </dd>
  </dl>
  <dl id="l_value">
  <dt><b>value = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='value' Line='value = 0.' -->
  <dd>Value for constant substitution.  One editing command is replacement of
  a region by this value.
  </dd>
  </dl>
  <dl id="l_minvalue">
  <dt><b>minvalue = INDEF, maxvalue = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minvalue' Line='minvalue = INDEF, maxvalue = INDEF' -->
  <dd>Range of values which may be modified.  Value of INDEF map to the minimum
  and maximum possible values.
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma' Line='sigma = INDEF' -->
  <dd>Sigma of noise to be added to substitution values.  If less than or
  equal to zero then no noise is added.  If INDEF then pixel values from
  the background region are randomly selected after subtracting the
  fitted background surface or median.  Finally if a positive value is given than
  a gaussian noise distribution is added.
  </dd>
  </dl>
  <dl id="l_angh">
  <dt><b>angh = -33., angv = 25.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='angh' Line='angh = -33., angv = 25.' -->
  <dd>Horizontal and vertical viewing angles (in degrees) for surface plots.
  </dd>
  </dl>
  <dl id="l_command">
  <dt><b>command = <span style="font-family: monospace;">"display $image 1 erase=$erase fill=yes order=0 &gt;&amp; dev$null"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='command' Line='command = "display $image 1 erase=$erase fill=yes order=0 &gt;&amp; dev$null"' -->
  <dd>Command for displaying images.  This task displays images by executing a
  standard IRAF command.  Two arguments may be substituted by the appropriate
  values; the image name specified by <span style="font-family: monospace;">"$image"</span> and the boolean erase
  flag specified by <span style="font-family: monospace;">"$erase"</span>.  Except for unusual cases the <b>tv.display</b>
  command is used with the fill option.  The fill option is required to
  provide a zoom feature.  See the examples for another possible command.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Graphics device used for surface plots.  Normally this is the standard
  graphics device <span style="font-family: monospace;">"stdgraph"</span> though other possibilities are <span style="font-family: monospace;">"stdplot"</span>
  and <span style="font-family: monospace;">"stdvdm"</span>.  Note the standard graphics output may also be
  redirected to a file with <span style="font-family: monospace;">"&gt;G file"</span> where <span style="font-family: monospace;">"file"</span> is any file name.
  </dd>
  </dl>
  <dl id="l_default">
  <dt><b>default = <span style="font-family: monospace;">"b"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='default' Line='default = "b"' -->
  <dd>Default command option for simple position list input.  If the input
  is a list of column and line positions (x,y) then the command executed
  at each position is given by this parameter.  This should be one of
  the aperture type editing commands, the statistics command, or the
  surface plotting command.  Two keystroke commands would obviously 
  be incorrect.  <i>This parameter is ignored in "fixpix" mode</i>.
  </dd>
  </dl>
  <dl id="l_fixpix">
  <dt><b>fixpix = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fixpix' Line='fixpix = no' -->
  <dd>Fixpix style input?  This type of input consists of rectangular regions
  specified by lines giving the starting and ending column and starting
  and ending line.  This is the same input used by <b>fixpix</b> and in
  the <b>ccdred</b> package.  The feature to refer to <span style="font-family: monospace;">"untrimmed"</span> images
  in the latter package is not available in this task.  When selected
  the editing consists of interpolation across the narrowest dimension
  of the region and the default key is ignored.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Regions of images are examined and edited.  This may be done interactively
  using an image display and cursor or non-interactively using a list of
  positions and commands.  There are a variety of display and editing
  options.  A list of input images and a matching list of output images
  are specified.  The output images are only created if the input image
  is modified (except by an explicit <span style="font-family: monospace;">"write"</span> command).  If no output
  list is specified (an empty list given by <span style="font-family: monospace;">""</span>) then the modified images
  are written back to the input images.  The images are edited in
  a temporary buffer image beginning with <span style="font-family: monospace;">"imedit"</span>.
   
  Commands are given via a cursor list.  When the task is run
  interactively this will normally be the standard image cursor
  (stdimcur).  Commands may be read from a file.  The file format may be
  cursor values including the command keys, a simple list of positions
  with the default command given by the <i>default</i> parameter, and a
  regions file, as used in the task <b>fixpix</b> and the <b>ccdred</b>
  package, selected by the <i>fixpix</i> parameter.
   
  The commands which modify the image may be written to a log file specified
  by parameter <i>logfile</i>.  This file can be used as a record of the
  pixels modified.  The format of this file is also suitable for input
  as a cursor list.  This allows the same commands to be applied to other
  images.  <i>Be careful not to have the cursor input and logfile have the
  same name!</i>
   
  When the <i>display</i> parameter is set the command given by the parameter
  <i>command</i> is executed.  Normally this command loads the image display
  though it could also create a contour map or other graph whose x and y
  coordinates are the same as the image coordinates.  The image is displayed
  when editing interactively and the standard image cursor (which can
  be redefined to be the standard graphics cursor) is used to select
  regions to be edited.  When not editing interactively the display
  flag should be turned off.
   
  It is nice to see changes to the image displayed immediately.  This is
  possible using the <i>autodisplay</i> option.  Note that this requires
  the display parameter to also be set.  If the autodisplay flag is set
  the display command is repeated after each change to the image.  The
  drawback to this is that the full image (or image section) is reloaded
  and so can be slow.  If not set it is still possible to explicitly give
  a redisplay command, <span style="font-family: monospace;">'r'</span>, after a number of changes have been made.
   
  Another display option is to make surface graphs to the specified
  graphics device (normally the standard graphics terminal).  This may
  be done by the commands <span style="font-family: monospace;">'g'</span> and <span style="font-family: monospace;">'s'</span> and automatically after each
  change if the <i>autosurface</i> parameter is set.  The two types of
  surface plots are a single surface of the image at the marked position
  and before and after plots for a change.
   
  Regions of the image to be examined or edited are selected by one
  or two cursor commands.  The single cursor commands define the center
  of an aperture.  The shape of the aperture, circular or square, is
  specified by the <i>aperture</i> parameter and the radius (or half
  the edge of a square) is specified by the <i>radius</i> parameter.
  The radius may be zero to select a single pixel.  The keys <span style="font-family: monospace;">'+'</span> and
  <span style="font-family: monospace;">'-'</span> may be used to quickly increment or decrement the current radius.
  The two keystroke commands either define the corners of a rectangular
  region or the endpoints of a line.
   
  Because it is sometimes difficult to mark cursor position precisely
  the defined region may be shifted so that the center is either
  a local maximum or minimum.  This is usually desired for editing
  cosmicrays, bad pixels, and stars.  The center pixel of the aperture
  is moved within a specified search radius given by parameter
  <i>search</i>.  If the search radius is zero then the region defined
  by the cursor is not adjusted.  The sign of the search radius
  selects whether a maximum (positive value) or a minimum (negative value)
  is sought.  The special key <span style="font-family: monospace;">'t'</span> toggles between the two modes
  in order to quickly edit both low sensitivity bad pixels and
  cosmicrays and stars.
   
  Once a region has been defined a background region may be required
  to estimate the background for replacement.  The background
  region is an annulus of the same shape separated by a buffer width,
  given by the parameter <i>buffer</i>, and having a width given by
  the parameter <i>width</i>.
   
  The replacement options are described below as is a summary of all the
  commands.  Two commands requiring a little more description are the
  space and <span style="font-family: monospace;">'p'</span> commands.  These print the statistics at the cursor
  position for the current aperture and background parameters.  The
  printout gives the x and y position of the aperture center (after the
  search if any), the pixel value (z) at that pixel, the mean background
  subtracted flux in the aperture, the number of pixels in the aperture,
  the mean background <span style="font-family: monospace;">"sky"</span>, the sigma of the background residuals from
  the background fit, and the number of pixels in the background region.
  The <span style="font-family: monospace;">'p'</span> key additionally prints the pixel values in the aperture.
  Beware of apertures with radii greater than 5 since they will wrap
  around in an 80 column terminal.
   
  When done editing or examining an image exit with <span style="font-family: monospace;">'q'</span> or <span style="font-family: monospace;">'Q'</span>.  The
  former saves the modified image in the output image (which might be
  the same as the input image) while the latter does not save the
  modified image.  Note that if the image has not been modified then
  no output occurs.  After exiting the next image in the input
  list is edited.  One may also change input images using the
  <span style="font-family: monospace;">":input"</span> command.  Note that this command sets the output to be the
  same as the input and a subsequent <span style="font-family: monospace;">":output"</span> command should be
  used to define a different output image name.  A final useful
  colon command is <span style="font-family: monospace;">":write"</span> which forces the current editor buffer
  to be written.  This can be used to save partial changes.
  </p>
  </section>
  <section id="s_replacement_algorithms">
  <h3>Replacement algorithms</h3>
  <p>
  The parameters <span style="font-family: monospace;">"minvalue"</span> and <span style="font-family: monospace;">"maxvalue"</span> are may be used to limit the
  range of values modified.  The default is to modify all pixels which
  are selected as described below.
  </p>
  <dl id="l_a">
  <dt><b>a, b</b></dt>
  <!-- Sec='REPLACEMENT ALGORITHMS' Level=0 Label='a' Line='a, b' -->
  <dd>Replace rectangular or aperture regions by background values.  A background
  surface is fit the pixels in the background annulus if the x and y orders
  are greater than zero otherwise a median is computed.  The x and y orders
  of the surface function are given by the <i>xorder</i> and <i>yorder</i>
  parameters.  The median is used or the surface is evaluated for the pixels
  in the replacement region.  If a positive sigma is specified then gaussian
  noise is added.  If a sigma of INDEF is specified then the residuals of the
  background pixels are sorted, the upper and lower 10% are excluded, and the
  remainder are randomly selected as additive noise.
  </dd>
  </dl>
  <dl id="l_c">
  <dt><b>c, f, l</b></dt>
  <!-- Sec='REPLACEMENT ALGORITHMS' Level=0 Label='c' Line='c, f, l' -->
  <dd>Replace rectangular or line regions by interpolation from the nearest
  background column or line.  The <span style="font-family: monospace;">'f'</span> line option interpolates across the
  narrowest dimension; i.e. for lines nearer to the line axis interpolation
  is by lines while for those  nearer to the column axis interpolation is
  by columns.  The buffer region applies but only the nearest background
  pixel at each line or column on either side of the replacement region
  is used for interpolation.  Gaussian noise may be added but background
  sampling is not available.  This method is similar to the method used
  in <b>fixpix</b> or <b>ccdred</b> with no buffer.  For <span style="font-family: monospace;">"fixpix"</span> type
  input the type of interpolation is automatically selected for the
  narrower dimension with column interpolation for square regions.
  </dd>
  </dl>
  <dl id="l_d">
  <dt><b>d, e, v</b></dt>
  <!-- Sec='REPLACEMENT ALGORITHMS' Level=0 Label='d' Line='d, e, v' -->
  <dd>Replace rectangular, aperture, or vector regions by the specified
  constant value.  This may be used to flag pixels or make masks.
  The vector option makes a line between two points with a width
  set by the radius value.
  </dd>
  </dl>
  <dl id="l_j">
  <dt><b>j, k</b></dt>
  <!-- Sec='REPLACEMENT ALGORITHMS' Level=0 Label='j' Line='j, k' -->
  <dd>Replace rectangular or aperture regions in the editor buffer by the data
  from the input image.  This may be used to undo any change.  Note that
  the <span style="font-family: monospace;">'i'</span> command can be used to completely reinitialize the editor
  buffer from the input image.
  </dd>
  </dl>
  <dl id="l_m">
  <dt><b>m, n</b></dt>
  <!-- Sec='REPLACEMENT ALGORITHMS' Level=0 Label='m' Line='m, n' -->
  <dd>Replace an aperture region by another aperture region.  There is no
  centering applied in this option.  The aperture region to copy is
  background subtracted using the background annulus for median or surface
  fitting.  This data may then be added to the destination aperture or
  replace the data in the destination aperture.  In the latter case the
  destination background surface is also computed and added.
  </dd>
  </dl>
  <dl id="l_u">
  <dt><b>u</b></dt>
  <!-- Sec='REPLACEMENT ALGORITHMS' Level=0 Label='u' Line='u' -->
  <dd>Undo the last change.  When a change is made the before and after data
  are saved.  An undo exchanges the two sets of data.  Note that it is
  possible to undo an undo to restore a change.  If any other command is
  used which causes data to be read (including the statistics and surface
  plotting) then the undo is lost.
  </dd>
  </dl>
  <dl>
  <dt><b>=, &lt;, &gt;</b></dt>
  <!-- Sec='REPLACEMENT ALGORITHMS' Level=0 Label='' Line='=, &lt;, &gt;' -->
  <dd>The all pixels with a value equal to that of the pixel at the cursor
  position are replaced by the specified constant value.  This is intended
  for editing detection masks where detected objects have specific mask
  values.
  </dd>
  </dl>
  </section>
  <section id="s_commands">
  <h3>Commands</h3>
  <p style="text-align:center">		IMEDIT CURSOR KEYSTROKE COMMANDS
  
  </p>
  <p>
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  ?       Print help
  :       Colon commands (see below)
  &lt;space&gt; Statistics
  g       Surface graph
  i       Initialize (start over without saving changes)
  q       Quit and save changes
  p       Print box of pixel values and statistics
  r       Redraw image display
  s       Surface plot at cursor
  t       Toggle between minimum and maximum search
  +       Increase radius by one
  -       Decrease radius by one
  I       Interrupt task immediately
  Q       Quit without saving changes
  </pre></div>
  <p>
  The following editing options are available.  Rectangular, line, and
  vector regions are specified with two positions and aperture regions
  are specified by one position.  The current aperture type (circular or
  square) is used in the latter case.  The move option takes two positions,
  the position to move from and the position to move to.
  </p>
  <div class="highlight-default-notranslate"><pre>
  a       Background replacement (rectangle)
  b       Background replacement (aperture)
  c       Column interpolation (rectangle)
  d       Constant value substitution (rectangle)
  e       Constant value substitution (aperture)
  f       Interpolation across line (line)
  j       Replace with input data (rectangle)
  k       Replace with input data (aperture)
  l       Line interpolation (rectangle)
  m       Copy by replacement (aperture)
  n       Copy by addition (aperture)
  u       Undo last change (see also <span style="font-family: monospace;">'i'</span>, <span style="font-family: monospace;">'j'</span>, and <span style="font-family: monospace;">'k'</span>)
  v       Constant value substitution (vector)
  =       Constant value substitution of pixels equal
              to pixel at the cursor position
  &lt;       Constant value substitution of pixels less than or equal
              to pixel at the cursor position
  &gt;       Constant value substitution of pixels greater than or equal
              to pixel at the cursor position
  </pre></div>
  <p>
   
  When the image display provides a fill option then the effect of zoom
  and roam is provided by loading image sections.  This is a temporary
  mechanism which will eventually be replaced by a more sophisticated
  image display interface.
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  E       Expand image display
  P       Pan image display
  R       Redraw image display
  Z       Zoom image display
  0       Redraw image display with no zoom
  1-9     Shift display
  </pre></div>
  <p>
   
  </p>
  <p style="text-align:center">IMEDIT COLON COMMANDS
  
  </p>
  <p>
   
  The colon either print the current value of a parameter when there is
  no value or set the parameter to the specified value.
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  angh [value]            Horizontal viewing angle (degrees)
  angv [value]            Vertical viewing angle (degrees)
  aperture [type]         Aperture type (circular|square)
  autodisplay [yes|no]    Automatic image display?
  autosurface [yes|no]    Automatic surface plots?
  buffer [value]          Background buffer width
  command [string]        Display command
  display [yes|no]        Display image?
  eparam                  Edit parameters
  graphics [device]       Graphics device
  input [image]           New input image to edit (output name = input)
  output [image]          New output image name
  radius [value]          Aperture radius
  search [value]          Search radius
  sigma [value]           Noise sigma (INDEF for histogram replacement)
  value [value]           Constant substitution value
  minvalue [value]        Minimum value for modification (INDEF=minimum)
  maxvalue [value]        Maximum value for modification (INDEF=maximum)
  width [value]           Background annulus width
  write [name]            Write changes to name (default current output)
  xorder [value]          X order for background fitting
  yorder [value]          Y order for background fitting
  </pre></div>
  </section>
  <section id="s_keywords">
  <h3>Keywords</h3>
  <p>
  None
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Interactively edit an image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imedit raw002 ed002
  </pre></div>
  <p>
  2.  Edit pixels non-interactively from an x-y list.  Replace the original images
      by the edited images.
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; head bad
  20 32
  40 91
  &lt;etc&gt;
  cl&gt; imedit raw* "" cursor=bad display-
  </pre></div>
  <p>
   
  3.  It is possible to use a contour plot for image display.  This is really
      not very satisfactory but can be used in desperation.
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; reset stdimcur=stdgraph
  cl&gt; display.command="contour $image &gt;&amp; dev$null"
  cl&gt; imedit raw002 ed002
  </pre></div>
  <p>
   
  4.  Use a <span style="font-family: monospace;">"fixpix"</span> file (without trim option).
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; head fixpix
  20 22 30 80
  99 99 1 500
  &lt;etc&gt;
  cl&gt; imedit raw* %raw%ed%* cursor=fixpix fixpix+ display-
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_IMEDIT">
  <dt><b>IMEDIT V2.13</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IMEDIT' Line='IMEDIT V2.13' -->
  <dd>The <span style="font-family: monospace;">'v'</span> option was added to allow vector replacement.
  The <span style="font-family: monospace;">'='</span>, <span style="font-family: monospace;">'&lt;'</span>, <span style="font-family: monospace;">'&gt;'</span> options were added to replace values matching the pixel
  at the cursor.
  </dd>
  </dl>
  <dl id="l_IMEDIT">
  <dt><b>IMEDIT V2.11.2</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IMEDIT' Line='IMEDIT V2.11.2' -->
  <dd>The temporary editor image was changed to use a unique temporary image
  name beginning with <span style="font-family: monospace;">"imedit"</span> rather than the fixed name of <span style="font-family: monospace;">"epixbuf"</span>.
  </dd>
  </dl>
  <dl id="l_IMEDIT">
  <dt><b>IMEDIT V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IMEDIT' Line='IMEDIT V2.11' -->
  <dd>If xorder or yorder are zero then a median background is computed
  for the <span style="font-family: monospace;">'a'</span> and <span style="font-family: monospace;">'b'</span> keys.
  </dd>
  </dl>
  <dl id="l_IMEDIT">
  <dt><b>IMEDIT V2.10.4</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IMEDIT' Line='IMEDIT V2.10.4' -->
  <dd>The <span style="font-family: monospace;">'u'</span>, <span style="font-family: monospace;">'j'</span>, <span style="font-family: monospace;">'k'</span>, and <span style="font-family: monospace;">'n'</span> keys were added to those recorded in the
  log file.
  </dd>
  </dl>
  <dl id="l_IMEDIT">
  <dt><b>IMEDIT V2.8</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IMEDIT' Line='IMEDIT V2.8' -->
  <dd>This task is a first version of what will be an evolving task.
  Additional features and options will be added as they are suggested.
  It is also a prototype using a very limited display interface; execution
  of a separate display command.  Much better interaction with a variety
  of image displays will be provided after a planned <span style="font-family: monospace;">"image display
  interface"</span> is implemented.  Therefore any deficiencies in this area
  should be excused.
   
  The zoom and roam features provided here are quite useful.  However,
  they depend on a feature of the tv.display program which fills the
  current image display window by pixel replication or interpolation.
  If this is left out of the display command these features will not
  work.  The trick is that this task displays sections of the editor
  buffer whose size and position is based on an internal zoom and
  center and the display program expands the section to fill the
  display.
   
  The surface plotting is done using an imported package.  The limitations
  of this package (actually limitations in the complexity of interfacing
  the application to this sophisticated package) mean that the
  surface plots are always scaled to the range of the data and that
  it is not possible to label the graph or use the graphics cursor to
  point at features for the task.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ccdred.instruments proto.fixpix
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'REPLACEMENT ALGORITHMS' 'COMMANDS' 'KEYWORDS' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

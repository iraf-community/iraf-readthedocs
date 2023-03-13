.. _polymark:

polymark: Create polygon lists for polyphot
===========================================

**Package: apphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  polymark image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>The list of input images used to define the polygons.
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords = <span style="font-family: monospace;">"default"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords = "default"' -->
  <dd>The input / output center positions file. The center positions for each
  polygonal aperture are read from or written to coords. There may more than one
  center position per polygon. Center positions are written to coords 1 center
  position per line. When the current polygon changes POLYMARK inserts a line
  containing a single <span style="font-family: monospace;">';'</span> after the last center position. If coords is
  <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span> or a directory specification then a center position
  file name of the form dir$root.extension.version is constructed, where dir is
  the directory, root is the root image name, extension is <span style="font-family: monospace;">"coo"</span> and version is
  the next available version of the file. 
  </dd>
  </dl>
  <dl id="l_polygons">
  <dt><b>polygons = <span style="font-family: monospace;">"default"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='polygons' Line='polygons = "default"' -->
  <dd>The name of the polygons file. The vertices of each polygon  are read from or
  written to the polygons file. The polygons file contains a list of the
  polygon vertices. Each vertex list is terminated by a line containing a  <span style="font-family: monospace;">';'</span>
  after the last vertex. If polygons is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span> or a directory
  specification then an output name of the form dir$root.extension.version is
  constructed, where dir is the directory, root is the root image name, extension
  is <span style="font-family: monospace;">"ver"</span> and the version is next available version of the file. The number of
  polygon files must be equal to the number of image files.
  </dd>
  </dl>
  <dl id="l_icommands">
  <dt><b>icommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='icommands' Line='icommands = ""' -->
  <dd>The image cursor or image cursor command file.
  </dd>
  </dl>
  <dl id="l_gcommands">
  <dt><b>gcommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gcommands' Line='gcommands = ""' -->
  <dd>The graphics cursor or graphics cursor command file.
  </dd>
  </dl>
  <dl id="l_wcsin">
  <dt><b>wcsin = <span style="font-family: monospace;">")_.wcsin"</span>, wcsout = <span style="font-family: monospace;">")_.wcsout"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcsin' Line='wcsin = ")_.wcsin", wcsout = ")_.wcsout"' -->
  <dd>The coordinate system of the input coordinates read from or written
  to <i>coords</i> and <i>polygons</i>. The image header coordinate system is
  used to transform from the input coordinate system to the <span style="font-family: monospace;">"logical"</span> pixel
  coordinate system used internally, and from the internal <span style="font-family: monospace;">"logical"</span> pixel
  coordinate system to the output coordinate system. The input coordinate
  system options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, <span style="font-family: monospace;">"physical"</span>, and <span style="font-family: monospace;">"world"</span>. The output
  coordinate system options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, and <span style="font-family: monospace;">"physical"</span>. The image
  cursor coordinate system is assumed to be the <span style="font-family: monospace;">"tv"</span> system.
  <dl>
  <dt><b>logical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='logical' Line='logical' -->
  <dd>Logical coordinates are pixel coordinates relative to the current image.
  The  logical coordinate system is the coordinate system used by the image
  input/output routines to access the image data on disk. In the logical
  coordinate system the coordinates of the first pixel of a  2D image, e.g.
  dev$ypix  and a 2D image section, e.g. dev$ypix[200:300,200:300] are
  always (1,1).
  </dd>
  </dl>
  <dl>
  <dt><b>tv</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='tv' Line='tv' -->
  <dd>Tv coordinates are the pixel coordinates used by the display servers. Tv
  coordinates  include  the effects of any input image section, but do not
  include the effects of previous linear transformations. If the input
  image name does not include an image section, then tv coordinates are
  identical to logical coordinates.  If the input image name does include a
  section, and the input image has not been linearly transformed or copied from
  a parent image, tv coordinates are identical to physical coordinates.
  In the tv coordinate system the coordinates of the first pixel of a
  2D image, e.g. dev$ypix and a 2D image section, e.g. dev$ypix[200:300,200:300]
  are (1,1) and (200,200) respectively.
  </dd>
  </dl>
  <dl>
  <dt><b>physical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='physical' Line='physical' -->
  <dd>Physical coordinates are pixel coordinates invariant  with respect to linear
  transformations of the physical image data.  For example, if the current image
  was created by extracting a section of another image,  the  physical
  coordinates of an object in the current image will be equal to the physical
  coordinates of the same object in the parent image,  although the logical
  coordinates will be different.  In the physical coordinate system the
  coordinates of the first pixel of a 2D image, e.g. dev$ypix and a 2D
  image section, e.g. dev$ypix[200:300,200:300] are (1,1) and (200,200)
  respectively.
  </dd>
  </dl>
  <dl>
  <dt><b>world</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='world' Line='world' -->
  <dd>World coordinates are image coordinates in any units which are invariant
  with respect to linear transformations of the physical image data. For
  example, the ra and dec of an object will always be the same no matter
  how the image is linearly transformed. The units of input world coordinates
  must be the same as those expected by the image header wcs, e. g.
  degrees and degrees for celestial coordinate systems.
  </dd>
  </dl>
  The wcsin and wcsout parameters default to the values of the package
  parameters of the same name. The default values of the package parameters
  wcsin and wcsout are <span style="font-family: monospace;">"logical"</span> and <span style="font-family: monospace;">"logical"</span> respectively.
  </dd>
  </dl>
  <dl id="l_cache">
  <dt><b>cache = <span style="font-family: monospace;">")_.cache"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cache' Line='cache = ")_.cache"' -->
  <dd>Cache the image pixels in memory. Cache may be set to the value of the apphot
  package parameter (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>. By default cacheing is 
  disabled.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">")_.graphics"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = ")_.graphics"' -->
  <dd>The standard graphics device.
  </dd>
  </dl>
  <dl id="l_display">
  <dt><b>display = <span style="font-family: monospace;">")_.display"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='display' Line='display = ")_.display"' -->
  <dd>The default display device.  Display may be set to the apphot package
  parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.  By default graphics overlay is
  disabled.  Setting display to one of <span style="font-family: monospace;">"imdr"</span>, <span style="font-family: monospace;">"imdg"</span>, <span style="font-family: monospace;">"imdb"</span>, or <span style="font-family: monospace;">"imdy"</span> enables
  graphics overlay with the IMD graphics kernel.  Setting display to
  <span style="font-family: monospace;">"stdgraph"</span> enables POLYMARK to work interactively from a contour plot.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  POLYMARK creates and / or displays center position and polygons files
  suitable for input to POLYPHOT. For each image in the input list POLYMARK
  creates a polygons file <i>polygons</i> and center positions file <i>coords</i>, 
  if these do not already exist. The format of the polygons and center
  position files is described in the OUTPUT section. 
  </p>
  <p>
  Polygonal apertures are defined and drawn on the image display using
  the image display cursor and then shifted to the desired center
  using the image display cursor. At any point in the marking process
  the user may rewind the polygon and coordinate file and draw the previously
  defined polygons on the display.
  </p>
  <p>
  The coordinates read from <i>polygons</i> or  <i>coords</i> are assumed to be
  in coordinate system defined by <i>wcsin</i>. The options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>,
  <span style="font-family: monospace;">"physical"</span>, and <span style="font-family: monospace;">"world"</span> and the transformation from the input coordinate
  system to the internal <span style="font-family: monospace;">"logical"</span> system is defined by the image coordinate
  system.  The simplest default is the <span style="font-family: monospace;">"logical"</span> pixel system. Users working on
  with image sections but importing pixel coordinate lists generated from the
  parent image must use the <span style="font-family: monospace;">"tv"</span> or <span style="font-family: monospace;">"physical"</span> input coordinate systems.
  Users importing coordinate lists in world coordinates, e.g. ra and dec,
  must use the <span style="font-family: monospace;">"world"</span> coordinate system and may need to convert their
  equatorial coordinate units from hours and degrees to degrees and degrees first.
  </p>
  <p>
  The coordinates written to <i>polygons</i> or <i>coords</i> are in the coordinate
  system defined by <i>wcsout</i>. The options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, and
  <span style="font-family: monospace;">"physical"</span>. The simplest default is the <span style="font-family: monospace;">"logical"</span> system. Users
  wishing to correlate the output coordinates of objects measured in
  image sections or mosaic pieces with coordinates in the parent
  image must use the <span style="font-family: monospace;">"tv"</span> or <span style="font-family: monospace;">"physical"</span> coordinate systems.
  </p>
  <p>
  If <i>cache</i> is yes and the host machine physical memory and working set size
  are large enough, the input image pixels are cached in memory. If cacheing
  is enabled and POLYMARK is run interactively the first measurement will appear
  to take a long time as the entire image must be read in before the measurement
  is actually made. All subsequent measurements will be very fast because POLYMARK
  is accessing memory not disk. The point of cacheing is to speed up random
  image access by making the internal image i/o buffers the same size as the
  image itself. However if the input object lists are sorted in row order and
  sparse cacheing may actually worsen not improve the execution time. Also at
  present there is no point in enabling cacheing for images that are less than
  or equal to 524288 bytes, i.e. the size of the test image dev$ypix, as the
  default image i/o buffer is exactly that size. However if the size of dev$ypix
  is doubled by converting it to a real image with the chpixtype task then the
  effect of cacheing in interactive is can be quite noticeable if measurements
  of objects in the top and bottom halfs of the image are alternated.
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  The following interactive keystroke and colon commands are available.
  </p>
  <div class="highlight-default-notranslate"><pre>
          Interactive Keystroke Commands
  
  ?       Print help
  :       Colon commands
  d       Plot radial profile of star near cursor
  g       Define the current polygonal aperture
  f       Draw the current polygon on the display
  spbar   Draw the current polygon on the display, output the polygon
  r       Rewind the polygon list
  m       Draw the next polygon in the polygon list on the display
  l       Draw all the remaining polygons in the list on the display
  q       Exit
  
          Colon commands
  
  :m [n]  Draw the next [nth] polygon in the polygon list on the display
  </pre></div>
  </section>
  <section id="s_output">
  <h3>Output</h3>
  <p>
  A sample polygons file and accompanying coordinates file is listed below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Sample Polygons File (2 polygons)
  
  200.5  200.5
  300.5  200.5
  300.5  300.5
  200.5  300.5
  ;
  100.4  100.4
  120.4  100.4
  120.4  120.4
  100.4  120.4
  ;
  </pre></div>
  <div class="highlight-default-notranslate"><pre>
  # Sample Coordinates File (2 groups, 1 for each polygon)
  
  123.4  185.5
  110.4  130.4
  150.9  200.5
  ;
  85.6   35.7
  400.5  300.5
  69.5   130.5
  ;
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create a coordinate list and polygon file using the image display and
  image display cursor. Use polymark to both create and display the 
  polygon and polygon center lists.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix 1 fi+
  
  ... display the image
  
  ap&gt; polymark dev$ypix display=imdg
  
  ... type ? for an optional help page
  
  ... type g to enter the "define a polygon" menu
  ... move the cursor to the first vertex, tap the space bar
      to mark the vertex, and repeat for each vertex
  ... type q to quit the "define a polygon" menu
  ... mark each vertex only once, POLYPHOT will close the
      polygon for you
  
  ... move the cursor to the desired polygon center and
      tap the space bar to record the polygon
  ... repeat for all desired polygon centers
  
  ... type g to define the next polygon
  ... move the cursor to the first vertex, tap the space bar
      to mark the vertex and repeat for each vertex
  ... type q to quit the polygon menu
  ... mark each vertex only once, POLYPHOT will close the
      polygon for you
  
  ... move the cursor to the desired polygon center and
      tap the space bar
  ... repeat for all desired polygon centers
  
  ... type q to quit and q to confirm the quit
  
  ... output will appear in ypix.coo.1 and ypix.ver.1
  
  ap&gt; display dev$ypix 2 fi+
  
  ... display the image
  
  ap&gt; polymark dev$ypix coords=ypix.coo.1 polygons=ypix.ver.1 \
      display=imdg
  
  ... type m to mark the first polygon / polygon center on the display
  
  ... type m to mark the next polygon / polygon center on the display
  
  ... type l to mark the remaining polygons
  
  ... type q to quit and q to confirm the quit
  
  ap&gt; display dev$ypix 2 fi+
  
  ... redisplay the image
  
  ap&gt; polymark dev$ypix coords="" polygons=ypix.ver.1 \
      display=imdg
  
  ... type l to mark the polygon list, note that since there is
      no coords file the polygons are not shifted
  
  ... type q to quit and q to confirm the quit
  </pre></div>
  <p>
  2. Repeat the previous example using an image section.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix[150:450,150:450] 1 fi+
  
  ... display the image
  
  ap&gt; polymark dev$ypix[150:450,150:450]] display=imdg wcsout=tv
  
  ... type ? for an optional help page
  
  ... type g to enter the "define a polygon" menu
  ... move the cursor to the first vertex, tap the space bar
      to mark the vertex, and repeat for each vertex
  ... type q to quit the "define a polygon" menu
  ... mark each vertex only once, POLYPHOT will close the
      polygon for you
  
  ... move the cursor to the desired polygon center and
      tap the space bar to record the polygon
  ... repeat for all desired polygon centers
  
  ... type g to define the next polygon
  ... move the cursor to the first vertex, tap the space bar
      to mark the vertex and repeat for each vertex
  ... type q to quit the polygon menu
  ... mark each vertex only once, POLYPHOT will close the
      polygon for you
  
  ... move the cursor to the desired polygon center and
      tap the space bar
  ... repeat for all desired polygon centers
  
  ... type q to quit and q to confirm the quit
  
  ... output will appear in ypix.coo.2 and ypix.ver.2
  
  ap&gt; display dev$ypix[150:450,150:450] 2 fi+
  
  ... display the image
  
  ap&gt; polymark dev$ypix[150:450,150:450] coords=ypix.coo.2 \
      polygons=ypix.ver.2 display=imdg wcsin=tv
  
  ... type m to mark the first polygon / polygon center on the display
  
  ... type m to mark the next polygon / polygon center on the display
  
  ... type l to mark the remaining polygons
  </pre></div>
  <p>
  3. Repeat example 1 using a contour plot instead of the image display.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; show stdimcur
  
  ... record the default value of stdimcur
  
  ap&gt; set stdimcur = stdgraph
  
  ... define the image cursor to be the graphics cursor
  
  ap&gt; contour dev$ypix
  
  ... draw a contour plot on the screen
  
  ap&gt; contour dev$ypix &gt;G ypix.plot1
  
  ... store the contour plot of dev$ypix in the file ypix.plot1
  
  ap&gt; polymark dev$ypix display=stdgraph
  
  ... type g to enter the define a polygon menu
  ... move the cursor to the first vertex, tap the space bar
      to mark the vertex, and repeat for each vertex
  ... type q to quit the define a polygon menu
  ... mark each vertex only once, POLYPHOT will close the
      polygon for you
  
  ... move the cursor to the desired polygon center and
      tap the space bar to record the polygon
  ... repeat for all desired polygon centers
  
  ... type g to define the next polygon
  ... move the cursor to the first vertex, tap the space bar
      to mark the vertex and repeat for each vertex
  ... type q to quit the define a polygon menu
  ... mark each vertex only once, POLYPHOT will close the
      polygon for you
  
  ... move the cursor to the desired polygon center and
      tap the space bar
  ... repeat for all desired polygon centers
  
  ... type r to rewind the coordinate and polygon lists
  
  ... type :.read ypix.plot1 to reread the contour plot
  
  ... type l to display all the polygons ...
  
  ... type q to quit and q again to confirm the  quit
  
  ... output will appear in ypix.ver.3 and ypix.coo.3
  
  ap&gt; contour dev$ypix
  
  ... redraw the contour plot
  
  ap&gt; polymark dev$ypix coords="ypix.coo.3" polygons=ypix.ver.3 \
      display=stdgraph
  
  ap&gt; set stdimcur = &lt;default&gt;
  
  ... reset the value of the stdimcur parameter
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  It is the responsibility of the user to make sure that the image displayed
  in the image display is the same as the image specified by the image parameter.
  </p>
  <p>
  Commands which draw to the image display are disabled by default.  To enable
  graphics overlay on the image display, set the display parameter to <span style="font-family: monospace;">"imdr"</span>,
  <span style="font-family: monospace;">"imdg"</span>, <span style="font-family: monospace;">"imdb"</span>, or <span style="font-family: monospace;">"imdy"</span> to get red, green, blue or yellow overlays. It
  may be necessary to run gflush and to redisplay the image to get the overlays
  position correctly.
  </p>
  <p>
  There are no restrictions on the shape of the polygon but the vertices
  must be listed in order either clockwise or counterclockwise in the
  polygons file.
  </p>
  <p>
  It is not necessary to close the polygon when drawing on the display.
  POLYMARK will complete the polygon for you.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  polyphot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'OUTPUT' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

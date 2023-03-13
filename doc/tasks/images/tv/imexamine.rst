.. _imexamine:

imexamine: Examine images using image display, graphics, and text
=================================================================

**Package: tv**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imexamine [input [frame]]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Optional list of images to be examined.  If specified, images are examined
  in turn, displaying them automatically.  If no images are specified the
  images currently loaded into the image display are examined.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>Rootname for output images created with the <span style="font-family: monospace;">'t'</span> key.  If no name is specified
  then the name of the input image is used.  A three digit number is appended
  to the rootname, such as <span style="font-family: monospace;">".001"</span>, starting with 1 until no image is found with
  that name.  Thus, successive output images with the same rootname will be
  numbered sequentially.
  </dd>
  </dl>
  <dl id="l_ncoutput">
  <dt><b>ncoutput = 101, nloutput = 101</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncoutput' Line='ncoutput = 101, nloutput = 101' -->
  <dd>Size of the output image created with the <span style="font-family: monospace;">'t'</span> key which is centered on the
  position of the cursor.
  </dd>
  </dl>
  <dl id="l_frame">
  <dt><b>frame = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='frame' Line='frame = 1' -->
  <dd>During program execution, a query parameter specifying the frame to be loaded.
  May also be specified on the command line when <i>imexamine</i> is used as a
  task to display a new image, to specify the frame to be loaded.
  </dd>
  </dl>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Query parameter for selecting images to be loaded.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = ""' -->
  <dd>Logfile filename in which to record output of the commands producing text.
  If no filename is given then no logfile will be kept.
  </dd>
  </dl>
  <dl id="l_keeplog">
  <dt><b>keeplog = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='keeplog' Line='keeplog = no' -->
  <dd>Log output results initially?  Logging can be toggled interactively during
  program execution.
  </dd>
  </dl>
  <dl id="l_defkey">
  <dt><b>defkey = <span style="font-family: monospace;">"a"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='defkey' Line='defkey = "a"' -->
  <dd>Default key for cursor x-y input list.  This key is applied to input
  cursor lists which do not have a cursor key specified.  It is used
  to repetitively apply a cursor command to a list of positions typically
  obtained from another task.
  </dd>
  </dl>
  <dl id="l_autoredraw">
  <dt><b>autoredraw = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='autoredraw' Line='autoredraw = yes' -->
  <dd>Automatically redraw graphs after a parameter change?  If no then graphs
  are only drawn when a graph or redraw command is given.
  If yes then colon commands which modify a parameter of the last graph
  will automatically redraw the graph.  A common example of this would
  be changing the graph limits.
  </dd>
  </dl>
  <dl id="l_allframes">
  <dt><b>allframes = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='allframes' Line='allframes = yes' -->
  <dd>Use all frames for displaying images?  If set, images from the input list
  are loaded cycling through the available frames.  If not set the last frame
  loaded is reused.
  </dd>
  </dl>
  <dl id="l_nframes">
  <dt><b>nframes = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nframes' Line='nframes = 0' -->
  <dd>Number of display frames.  When automatically loading images from the input
  list only this number of frames will be used.  This should, of course,
  not exceed the number of frames provided by the display device.
  If the number of frames is set to 0 then the task will query the display
  device to determine how many frames are currently allocated.  New frames may
  be allocated during program execution by displaying images with the <span style="font-family: monospace;">'d'</span> key.
  </dd>
  </dl>
  <dl id="l_ncstat">
  <dt><b>ncstat = 5, nlstat = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncstat' Line='ncstat = 5, nlstat = 5' -->
  <dd>The statistics command computes values from a box centered on the
  specified cursor position with the number of columns and lines
  given by these parameters.
  </dd>
  </dl>
  <dl id="l_graphcur">
  <dt><b>graphcur = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphcur' Line='graphcur = ""' -->
  <dd>Graphics cursor input.  If null the standard graphics cursor is used whenever
  graphics cursor input is requested.  A cursor file in the appropriate
  format may be substituted by specifying the name of the file.
  </dd>
  </dl>
  <dl id="l_imagecur">
  <dt><b>imagecur = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imagecur' Line='imagecur = ""' -->
  <dd>Image display cursor input.  If null the standard image display cursor is
  used whenever image cursor input is requested.  A cursor file in the
  appropriate format may be substituted by specifying the name of the file.
  Also the image cursor may be changed to query the graphics device or
  the terminal by setting the environment parameter <span style="font-family: monospace;">"stdimcur"</span>
  to <span style="font-family: monospace;">"stdgraph"</span> or <span style="font-family: monospace;">"text"</span> respectively.
  </dd>
  </dl>
  <dl id="l_wcs">
  <dt><b>wcs = <span style="font-family: monospace;">"logical"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcs' Line='wcs = "logical"' -->
  <dd>The world coordinate system (<i>wcs</i>) to be used for axis labeling when
  input is from images.
  The following standard world systems are predefined.
  <dl>
  <dt><b>logical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='logical' Line='logical' -->
  <dd>Logical coordinates are image pixel coordinates relative to the image currently
  being displayed.
  </dd>
  </dl>
  <dl>
  <dt><b>physical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='physical' Line='physical' -->
  <dd>The physical coordinate system is invariant with respect to linear
  transformations of the physical image matrix.  For example, if the reference
  image was created by extracting a section of another image, the physical
  coordinates of an object in the reference image will be the pixel coordinates
  of the same object in the original image.  The physical coordinate system
  thus provides a consistent coordinate system (a given object always has the
  same coordinates) for all images, regardless of whether any user world
  coordinate systems have been defined.
  </dd>
  </dl>
  <dl>
  <dt><b>world</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='world' Line='world' -->
  <dd>The <span style="font-family: monospace;">"world"</span> coordinate system is the <i>current default WCS</i>.
  The default world system is the system named by the environment variable
  <i>defwcs</i> if defined in the user environment and present in the reference
  image WCS description, else it is the first user WCS defined for the image
  (if any), else physical coordinates are returned.
  </dd>
  </dl>
  <dl>
  <dt><b>xformat = <span style="font-family: monospace;">""</span>, yformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='xformat' Line='xformat = "", yformat = ""' -->
  <dd>The numerical format for the world coordinate labels in the line and column
  plots and the format for printing world coordinates.  The values may be <span style="font-family: monospace;">""</span>
  (an empty string), %f for decimal format, %h and %H for xx:xx:xx format, and
  %m and %M for xx:xx.x format.  The upper case %H and %M convert degrees
  to hours.  Images sometimes include recommended coordinate formats as
  WCS attributes.  These are used if the format specified by these parameters
  is <span style="font-family: monospace;">""</span>.  Any other value will override the image attribute.
  </dd>
  </dl>
  In addition to these three reserved WCS names, the name of any user WCS
  defined for the reference image may be given.  A user world coordinate system
  may be any linear or nonlinear world system.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Graphics output device.  Normally this is the standard graphics device
  specified by the environment variable <span style="font-family: monospace;">"stdgraph"</span>.
  </dd>
  </dl>
  <dl id="l_display">
  <dt><b>display = <span style="font-family: monospace;">"display(image='$1',frame=$2)"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='display' Line='display = "display(image='$1',frame=$2)"' -->
  <dd>Command template used to display an image.  The image to be displayed is
  substituted for argument $1 and the frame for argument $2.  Any display task
  may be used for image display by modifying this template.
  </dd>
  </dl>
  <dl id="l_use_display">
  <dt><b>use_display = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='use_display' Line='use_display = yes' -->
  <dd>Use the image display?  Set to no to disable all interaction with the
  display device, e.g., when working at a terminal that does not provide image
  display capabilities.
  </dd>
  </dl>
  </section>
  <section id="s_additional_parameters">
  <h3>Additional parameters</h3>
  <p>
  The various graphs and the aperture sum command have parameters defined in
  additional parameter sets.  The parameter sets are hidden tasks with
  the first character being the cursor command graph key that uses the
  parameters followed by <span style="font-family: monospace;">"imexam"</span>.  The parameter sets are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cimexam    Parameters for column plots
  eimexam    Parameters for contour plots
  himexam    Parameters for histogram plots
  jimexam    Parameters for line 1D gaussian fit plots
  kimexam    Parameters for column 1D gaussian fit plots
  limexam    Parameters for line plots
  rimexam    Parameters for radial profile plots and aperture sums
  simexam    Parameters for surface plots
  vimexam    Parameters for vector plots (centered and endpoint)
  </pre></div>
  <p>
  The same  parameters dealing with graph formats occur in many of the parameter
  sets while some are specific only to one parameter set.  In the
  summary below those common to more than one parameter set are shown
  only once.  The characters in parenthesis are the graph key prefixes
  for the parameter sets in which the parameter occurs.
  </p>
  <dl id="l_angh">
  <dt><b>angh = -33., angv = 25.		(s)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='angh' Line='angh = -33., angv = 25.		(s)' -->
  <dd>Horizontal and vertical viewing angles (degrees) for surface plots.
  </dd>
  </dl>
  <dl id="l_autoscale">
  <dt><b>autoscale = yes			(h)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='autoscale' Line='autoscale = yes			(h)' -->
  <dd>In the case of integer data, automatically adjust <i>nbins</i> and
  <i>z2</i> to avoid aliasing effects.
  </dd>
  </dl>
  <dl id="l_axes">
  <dt><b>axes = yes				(s)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='axes' Line='axes = yes				(s)' -->
  <dd>Draw axes along edge of surface plots?
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background = yes			(jkr.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='background' Line='background = yes			(jkr.)' -->
  <dd>Fit and subtract a background for aperture sums, 1D gaussian fits, and
  radial profile plots?
  </dd>
  </dl>
  <dl id="l_banner">
  <dt><b>banner = yes 			 (cehjklrsv.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='banner' Line='banner = yes 			 (cehjklrsv.)' -->
  <dd>Add a standard banner to a graph?  The standard banner includes the
  IRAF user and host identification and time, the image name and title,
  and graph specific parameters.
  </dd>
  </dl>
  <dl id="l_beta">
  <dt><b>beta = INDEF			(ar.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='beta' Line='beta = INDEF			(ar.)' -->
  <dd>Beta value to use for Moffat profile fits.  If the value is INDEF
  the value will be determine as part of the fit otherwise the parameter
  will be fixed at the specified value.
  </dd>
  </dl>
  <dl id="l_boundary">
  <dt><b>boundary = <span style="font-family: monospace;">"constant"</span>		(v)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='boundary' Line='boundary = "constant"		(v)' -->
  <dd>Boundary extension for vector plots in which the averaging width might
  go outside of the image.
  </dd>
  </dl>
  <dl id="l_box">
  <dt><b>box = yes 				(cehjklrv.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='box' Line='box = yes 				(cehjklrv.)' -->
  <dd>Draw graph box and axes?
  </dd>
  </dl>
  <dl id="l_buffer">
  <dt><b>buffer = 5.				(r.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='buffer' Line='buffer = 5.				(r.)' -->
  <dd>Buffer distance from object aperture of background annulus for aperture sums
  and radial profile plots.
  </dd>
  </dl>
  <dl id="l_ceiling">
  <dt><b>ceiling = INDEF			(es)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='ceiling' Line='ceiling = INDEF			(es)' -->
  <dd>Ceiling data value for contour and surface plots.  A value of INDEF does
  not apply a ceiling.  (In contour plots a value of 0. also does not
  apply a ceiling.)
  </dd>
  </dl>
  <dl id="l_center">
  <dt><b>center = yes			(jkr.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='center' Line='center = yes			(jkr.)' -->
  <dd>Apply a centering algorithm for doing aperture sums, 1D gaussian fits,
  and radial profile plots?
  </dd>
  </dl>
  <dl id="l_constant">
  <dt><b>constant = 0.			(v)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='constant' Line='constant = 0.			(v)' -->
  <dd>Boundary extension constant for vector plots in which the averaging width
  might go outside of the image.
  </dd>
  </dl>
  <dl id="l_dashpat">
  <dt><b>dashpat = 528			(e)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='dashpat' Line='dashpat = 528			(e)' -->
  <dd>Dash pattern for negative contours.
  </dd>
  </dl>
  <dl id="l_fill">
  <dt><b>fill = no				(e)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='fill' Line='fill = no				(e)' -->
  <dd>Fill the output viewport regardless of the device aspect ratio?
  </dd>
  </dl>
  <dl id="l_fitplot">
  <dt><b>fitplot = yes			(r.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='fitplot' Line='fitplot = yes			(r.)' -->
  <dd>Overplot the profile fit on the radial profile data?
  </dd>
  </dl>
  <dl id="l_fittype">
  <dt><b>fittype = <span style="font-family: monospace;">"moffat"</span>			(ar.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='fittype' Line='fittype = "moffat"			(ar.)' -->
  <dd>Profile type to fit the radial profile data?  The choices are <span style="font-family: monospace;">"gaussian"</span>
  and <span style="font-family: monospace;">"moffat"</span>.
  </dd>
  </dl>
  <dl id="l_floor">
  <dt><b>floor = INDEF			(es)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='floor' Line='floor = INDEF			(es)' -->
  <dd>Floor data value for contour and surface plots.  A value of INDEF does
  not apply a floor.  (In contour plots a value of 0. also does not
  apply a floor.)
  </dd>
  </dl>
  <dl id="l_interval">
  <dt><b>interval = 0			(e)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='interval' Line='interval = 0			(e)' -->
  <dd>Contour interval.  If 0, a contour interval is chosen which places 20 to 30
  contours spanning the intensity range of the image.
  </dd>
  </dl>
  <dl id="l_iterations">
  <dt><b>iterations = 3			(ar)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='iterations' Line='iterations = 3			(ar)' -->
  <dd>Number of iterations to adjust the fitting radius.
  </dd>
  </dl>
  <dl id="l_label">
  <dt><b>label= no				(e)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='label' Line='label= no				(e)' -->
  <dd>Label the major contours in the contour plot?
  </dd>
  </dl>
  <dl id="l_logx">
  <dt><b>logx = no, logy = no		(chjklrv.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='logx' Line='logx = no, logy = no		(chjklrv.)' -->
  <dd>Plot the x or y axis logarithmically?  The default for histogram plots is
  to plot the y axis logarithmically.
  </dd>
  </dl>
  <dl id="l_magzero">
  <dt><b>magzero = 25.			(r.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='magzero' Line='magzero = 25.			(r.)' -->
  <dd>Magnitude zero point for aperture sums.
  </dd>
  </dl>
  <dl id="l_majrx">
  <dt><b>majrx=5, minrx=5, majry=5, minry=5	(cehjklrv.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='majrx' Line='majrx=5, minrx=5, majry=5, minry=5	(cehjklrv.)' -->
  <dd>Maximum number of major tick marks on each axis and number of minor tick marks
  between major tick marks.
  </dd>
  </dl>
  <dl id="l_marker">
  <dt><b>marker = <span style="font-family: monospace;">"box"</span>			(chjklrv.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='marker' Line='marker = "box"			(chjklrv.)' -->
  <dd>Marker to be drawn if <b>pointmode</b> = yes.  Markers are <span style="font-family: monospace;">"point"</span>, <span style="font-family: monospace;">"box"</span>, 
  <span style="font-family: monospace;">"cross"</span>, <span style="font-family: monospace;">"plus"</span>, <span style="font-family: monospace;">"circle"</span>, <span style="font-family: monospace;">"hebar"</span>, <span style="font-family: monospace;">"vebar"</span>, <span style="font-family: monospace;">"hline"</span>, <span style="font-family: monospace;">"vline"</span> or <span style="font-family: monospace;">"diamond"</span>.
  </dd>
  </dl>
  <dl id="l_naverage">
  <dt><b>naverage = 1			(cjklv)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='naverage' Line='naverage = 1			(cjklv)' -->
  <dd>Number of lines, columns, or width perpendicular to a vector to be averaged.
  </dd>
  </dl>
  <dl id="l_nbins">
  <dt><b>nbins = 512				(h)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='nbins' Line='nbins = 512				(h)' -->
  <dd>The number of bins in, or resolution of, histogram plots.
  </dd>
  </dl>
  <dl id="l_ncolumns">
  <dt><b>ncolumns = 21, nlines = 21		(ehs)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='ncolumns' Line='ncolumns = 21, nlines = 21		(ehs)' -->
  <dd>Number of columns and lines used in contour, histogram, and surface plots.
  </dd>
  </dl>
  <dl id="l_ncontours">
  <dt><b>ncontours = 5			(e)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='ncontours' Line='ncontours = 5			(e)' -->
  <dd>Number of contours to be drawn.  If 0, the contour interval may be specified,
  otherwise 20-30 nicely spaced contours are drawn.  A maximum of 40 contours
  can be drawn.
  </dd>
  </dl>
  <dl id="l_nhi">
  <dt><b>nhi = -1				(e)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='nhi' Line='nhi = -1				(e)' -->
  <dd>If -1, highs and lows are not marked.  If 0, highs and lows are marked
  on the plot.  If 1, the intensity of each pixel is marked on the plot.
  </dd>
  </dl>
  <dl id="l_pointmode">
  <dt><b>pointmode = no			(chlv)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='pointmode' Line='pointmode = no			(chlv)' -->
  <dd>Plot points or marks instead of lines?
  </dd>
  </dl>
  <dl id="l_pointmode">
  <dt><b>pointmode = yes			(jkr.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='pointmode' Line='pointmode = yes			(jkr.)' -->
  <dd>Plot points or marks instead of lines?  For radial profile plots point
  mode should always be yes.
  </dd>
  </dl>
  <dl id="l_radius">
  <dt><b>radius = 5.				(r.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='radius' Line='radius = 5.				(r.)' -->
  <dd>Radius of aperture for aperture sums and centering.
  </dd>
  </dl>
  <dl id="l_round">
  <dt><b>round = no				(cehjklrv.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='round' Line='round = no				(cehjklrv.)' -->
  <dd>Extend the axes up to <span style="font-family: monospace;">"nice"</span> values?
  </dd>
  </dl>
  <dl id="l_rplot">
  <dt><b>rplot = 8.				(jkr.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='rplot' Line='rplot = 8.				(jkr.)' -->
  <dd>Radius to which the radial profile or 1D profile fits are plotted.
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma = 2.				(jk)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='sigma' Line='sigma = 2.				(jk)' -->
  <dd>Initial guess for 1D gaussian fits.  The value is in pixels even if the fitting
  is done in world coordinates.  This must be close to the true value
  for convergence.  Also the four times the initial sigma is used to define
  the distance to the background region for the initial background estimate.
  </dd>
  </dl>
  <dl id="l_szmarker">
  <dt><b>szmarker = 1			(chjklrv.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='szmarker' Line='szmarker = 1			(chjklrv.)' -->
  <dd>Size of mark (except for points).  A positive size less than 1 specifies
  a fraction of the device size.  Values of 1, 2, 3, and 4 signify
  default sizes of increasing size.
  </dd>
  </dl>
  <dl id="l_ticklabels">
  <dt><b>ticklabels = yes			(cehjklrv.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='ticklabels' Line='ticklabels = yes			(cehjklrv.)' -->
  <dd>Label the tick marks?
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">""</span>				(cehjklrsv.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='title' Line='title = ""				(cehjklrsv.)' -->
  <dd>User title.  This is independent of the standard banner title.
  </dd>
  </dl>
  <dl id="l_top_closed">
  <dt><b>top_closed = no			(h)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='top_closed' Line='top_closed = no			(h)' -->
  <dd>Include z2 in the top histogram bin?  Each bin of the histogram is a
  subinterval that is half open at the top.  <i>Top_closed</i> decides whether
  those pixels with values equal to z2 are to be counted in the histogram.  If
  <b>top_closed</b> is yes, the top bin will be larger than the other bins.
  </dd>
  </dl>
  <dl id="l_width">
  <dt><b>width = 5.				(jkr.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='width' Line='width = 5.				(jkr.)' -->
  <dd>Width of background region for background subtraction in aperture sums,
  1D profile fits, and radial profile plots.
  </dd>
  </dl>
  <dl id="l_wcs">
  <dt><b>wcs = <span style="font-family: monospace;">"physical"</span></b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='wcs' Line='wcs = "physical"' -->
  <dd>World coordinate system for axis labeling and coordinate readback.
  </dd>
  </dl>
  <dl id="l_x1">
  <dt><b>x1 = INDEF, x2 = INDEF, y1 = INDEF, y2 = INDEF	(chjklrv.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='x1' Line='x1 = INDEF, x2 = INDEF, y1 = INDEF, y2 = INDEF	(chjklrv.)' -->
  <dd>Range of graph along each axis.  If INDEF the range is determined from
  the data range plus a buffer.  The default y1 for histogram plots is 0.
  </dd>
  </dl>
  <dl id="l_xformat">
  <dt><b>xformat, yformat</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='xformat' Line='xformat, yformat' -->
  <dd>Set world image coordinate formats.  Any format changes take effect on the next
  usage; i.e. there is no automatic redrawing.
  </dd>
  </dl>
  <dl id="l_xlabel">
  <dt><b>xlabel, ylabel			(cehjklrv.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='xlabel' Line='xlabel, ylabel			(cehjklrv.)' -->
  <dd>Axis labels.  Each graph type has an appropriate default.  If the label
  value is <span style="font-family: monospace;">"wcslabel"</span> then the coordinate label from the image WCS
  will be used if defined.
  </dd>
  </dl>
  <dl id="l_xorder">
  <dt><b>xorder = 0				(jk)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='xorder' Line='xorder = 0				(jk)' -->
  <dd>Order for 1D gaussian background.  If 0 then a median is computed.  If
  1 then a constant background is fit simultaneously with the other gaussian
  parameters.  If 2 then a linear background is fit simultaneously with the
  other gaussian parameters.
  </dd>
  </dl>
  <dl id="l_xorder">
  <dt><b>xorder = 0, yorder = 0		(r.)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='xorder' Line='xorder = 0, yorder = 0		(r.)' -->
  <dd>If either parameter is zero then the median value of the
  background annulus is used for background subtraction in aperture sums and
  radial profile plots.  Values greater than zero define polynomial
  surface orders for background subtraction.  The orders are actually the
  number of polynomial terms.  An order of 1 is a constant an order of 2
  is a plane.
  </dd>
  </dl>
  <dl id="l_zero">
  <dt><b>zero = 0.				(e)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='zero' Line='zero = 0.				(e)' -->
  <dd>Greyscale value of the zero contour, i.e., the value of a zero point shift
  to be applied to the image data before plotting.  Does not affect the values
  of the floor and ceiling parameters.
  </dd>
  </dl>
  <dl id="l_z1">
  <dt><b>z1 = INDEF, z2 = INDEF		(h)</b></dt>
  <!-- Sec='ADDITIONAL PARAMETERS' Level=0 Label='z1' Line='z1 = INDEF, z2 = INDEF		(h)' -->
  <dd>Range of pixel values to be used in histogram.  INDEF values default to
  the range in the region being histogramed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Images are examined using an image display, various types of plots, and
  text output.  Commands are given using the image display cursor and/or
  graphics cursor.  This task brings together many of the features of the
  IRAF image display and graphics facilities with some simple image
  analysis capabilities.
  </p>
  <p>
  IMAGE DISPLAY
  </p>
  <p>
  If <i>use_display</i> is yes the image display is used to examine images.
  When no input list is specified images may be loaded with the <span style="font-family: monospace;">'d'</span> key,
  frames selected with <span style="font-family: monospace;">'n'</span>, <span style="font-family: monospace;">'p'</span>, and <span style="font-family: monospace;">":select"</span>, and the scaled contents
  of the display frame buffer examined if the image itself is not available.
  </p>
  <p>
  When an input list is specified the <span style="font-family: monospace;">'n'</span>, <span style="font-family: monospace;">'p'</span>, and <span style="font-family: monospace;">":select"</span> allow
  moving about the list and new images may be added to the end of the
  list with <span style="font-family: monospace;">'d'</span>.  Images are automatically loaded as they are selected if
  not currently loaded.  Two parameters control how the frames are
  loaded.  The <i>nframes</i> parameter determines which frames are
  available.  Within the available frames images may be loaded by cycling
  through them if <i>allframes</i> is yes or in the last loaded frame
  (initially frame 1) if it is no.
  </p>
  <p>
  When reading the image cursor the frame and the name of the image in
  the frame are determined.  Therefore images may also be selected
  by changing the frame externally or if the image cursor input is
  changed from the standard image display to text or file input.
  </p>
  <p>
  The <span style="font-family: monospace;">'d'</span> command displays an image using the template CL command given
  by parameter <i>display</i>.  Usually this is the standard
  IRAF <b>tv.display</b> command though in some circumstances other commands
  like <b>plot.contour</b> may be used.  This command may be used to
  display an image even if <i>use_display</i> is no.
  </p>
  <p>
  This task is generally intended for interactive use with an image
  display.  However it is possible to disable use of the image display
  and change the image cursor input to a graphics cursor, a file,
  or typed in by the user.  In this case an input image list is most
  appropriate but if one is missing, a query will be issued each time
  a command requiring an image is given.
  </p>
  <p>
  CURSOR INPUT
  </p>
  <p>
  Commands are given using cursor input.  Generally the image cursor is
  used to select points in the images to be examined and the key typed
  selects a particular operation.  In addition to the image cursor the
  graphics cursor is sometimes useful.  First, it gives access to the
  graphics cursor mode commands (see <b>cursors</b>) such as annotating,
  saving or printing a graph, expanding and roaming, and printing cursor
  positions.  Second, it can give a better perspective on the data for
  cursor positions than the image cursor.  And lastly, it may be needed
  when an image display is not available.  The commands <span style="font-family: monospace;">'g'</span> and <span style="font-family: monospace;">'i'</span>
  select between the graphics and image cursors.  Initially the image
  cursor is read.
  </p>
  <p>
  Interpretation of the graph coordinate in terms of an image coordinate
  depends on the type of graph as described below.
  </p>
  <dl id="l_contour">
  <dt><b>contour plot</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='contour' Line='contour plot' -->
  <dd>This gives image coordinates directly and both the x and y cursor values
  are used.
  </dd>
  </dl>
  <dl id="l_column">
  <dt><b>column plot</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='column' Line='column plot' -->
  <dd>The x cursor position gives the line coordinate and the column coordinate
  used for the plot (that specified before averaging) gives the column
  coordinate.
  </dd>
  </dl>
  <dl id="l_line">
  <dt><b>line plot</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='line' Line='line plot' -->
  <dd>The x cursor position gives the column coordinate and the line coordinate
  used for the plot (that specified before averaging) gives the line
  coordinate.
  </dd>
  </dl>
  <dl id="l_vector">
  <dt><b>vector plot</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='vector' Line='vector plot' -->
  <dd>The x cursor position defines a column and line coordinate along the vector
  plotted.
  </dd>
  </dl>
  <dl id="l_surface">
  <dt><b>surface plot</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='surface' Line='surface plot' -->
  <dd>No cursor information is available in this plot and the cursor position
  used to make the surface plot (the center of the surface) is used again.
  </dd>
  </dl>
  <dl id="l_histogram">
  <dt><b>histogram plot</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='histogram' Line='histogram plot' -->
  <dd>No cursor information is available in this plot and the cursor position
  used to make the histogram (the center of the box) is used again.
  </dd>
  </dl>
  <dl id="l_radial">
  <dt><b>radial profile plot</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='radial' Line='radial profile plot' -->
  <dd>No cursor information is available in this plot and the cursor position
  used to define the center is used again.
  </dd>
  </dl>
  <p>
  There are some special features associated with cursor input in IRAF
  which might be useful in some circumstances.  The image display cursor
  can be reset to be a text cursor, graphics cursor, or image cursor by
  setting the environment variable <span style="font-family: monospace;">"stdimcur"</span> to <span style="font-family: monospace;">"text"</span>, <span style="font-family: monospace;">"stdgraph"</span>,
  or <span style="font-family: monospace;">"stdimage"</span> respectively.  Text cursor input consists of the x and
  y coordinates, a frame number, and the key or colon command.  Another
  form of text input is to set the value of the cursor input parameter
  to a file containing cursor commands.  There are two special features
  dealing with text cursor input.  If only x and y are entered the default
  key parameter <i>defkey</i> determines the command.  This is particularly
  useful if one has a list of pixel positions prepared by some other
  program.  The second feature is that for commands not requiring coordinates
  they may be left out and the command key or colon command entered.
  </p>
  <p>
  TEXT OUTPUT
  </p>
  <p>
  The following commands produce text output which may also be appended to
  a logfile.
  </p>
  <dl id="l_a">
  <dt><b>a, <span style="font-family: monospace;">','</span></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='a' Line='a, ','' -->
  <dd>Circular aperture photometry is performed at the position of the cursor.
  If the centering option is selected the cursor position is used as the
  initial point for computing the central moments of the marginal
  distributions in x and y.  The marginal distributions are obtained from a
  square aperture with edge dimensions of twice the aperture radius
  parameter.  Only the pixels above the mean are used in computing the
  central moments.  If the central moments are in a different pixel than that
  used for extracting the marginal distributions the computation is repeated
  using the new center.
  The radius of the photometry and fitting aperture is specified by the
  <i>radius</i> parameter and the <i>iteration</i> parameter.  Iteration of the
  fitting radius and printing of the final radius is only done for the <span style="font-family: monospace;">'a'</span>
  key.  If the number of iterations is one then the radius is not adjusted.
  If it is greater than one then the direct FWHM (described) below is used to
  adjust the radius.  At each iteration the new radius is set to three times
  the direct FWHM (which is six times the radius at half-maximum).  The
  radius is printed as part of the output.
  If the background subtraction option is selected a concentric circular
  annulus is defined.  The inner edge is separated from the object
  aperture by a specified buffer distance and the outer edge is defined
  by a width for the annulus.  The type of background used is determined
  by the parameters <i>xorder</i> and <i>yorder</i>.  If either parameter
  is zero then a median of the background annulus is determined.
  If 1 or greater a polynomial surface of the specified number of terms
  is fit.  Typically the orders are 1 for a constant or 2 for a plane.
  The median or fitted surface values within the object aperture are then
  subtracted.
  The flux within the circular aperture is computed by simply summing the
  pixel values with centers within the specified radius of the center
  position.  No partial pixel adjustments are made.  If the flux is
  positive a magnitude is computed as
  	magnitude = magzero - 2.5 * log10 (flux)
  where the magnitude zero point is a user defined parameter.
  In addition to the flux, the second intensity moments are used to compute
  an ellipticity and position angle.  The equations defining the moments and
  related parameters are:
  <div class="highlight-default-notranslate"><pre>
  Mxx = sum (x * x * I) / sum (I)
  Myy = sum (y * y * I) / sum (I)
  Mxy = sum (x * y * I) / sum (I)
  e = sqrt ((Mxx - Myy) ** 2 + (2 * Mxy) ** 2) / (Mxx + Myy)
  pa = 0.5 * atan (2 * Mxy / (Mxx - Myy))
  </pre></div>
  A nonlinear least squares profile of fixed center and zero background is
  fit to the radius and flux values of the background subtracted pixels to
  determine a peak intensity and FWHM.  The profile type is set by the
  <i>fittype</i> parameter.  The choices are <span style="font-family: monospace;">"gaussian"</span> and <span style="font-family: monospace;">"moffat"</span>.  If the
  profile type is <span style="font-family: monospace;">"moffat"</span> there is an additional parameter <span style="font-family: monospace;">"beta"</span>.  This
  value may be specified to fix it or given as INDEF to also be determined.
  The profile equations are:
  <div class="highlight-default-notranslate"><pre>
  I = Ic exp (-0.5 * (r / sigma)**2)      (fittype = "gaussian")
  I = Ic (1 + (r / alpha)**2)**(-beta)    (fittype = "moffat")
  </pre></div>
  where Ic is the peak value, r is the radius, and the parameters are
  sigma, alpha, and beta.  The sigma and alpha values are converted to
  FWHM in the reported results.
  Weights which are the inverse square of the pixel radius are used.  This
  has the effect of giving equal weight to all parts of the profile instead
  of being overwhelmed by the larger number of pixels are larger radii.  An
  additional weighting factor is used for pixels outside the half-maximum
  radius (as determined using the algorithm described below).  The weights
  are
  <div class="highlight-default-notranslate"><pre>
  wt = exp (-(r/rhalf - 1)**2)  for r/rhalf &gt; 1
  </pre></div>
  where rhalf is the radius at half-maximum.  This has the effect
  of reducing the contribution of the profile wings.
  The above fit is done to the individual pixel values with a radius measured
  to the center of the pixel.  For the <span style="font-family: monospace;">'a'</span> key two additional measurements
  are made on a azimuthally averaged radial profile with a finer sampling of
  the radial bins.  This uses the same algorithms for centering, background
  estimation, and FWHM measurement as in the task <b>psfmeasure</b>.  The
  centering is essentially the same as described above but the background
  estimation is a mode of the sky annulus pixels.  Note that the centering
  and background subtraction are done for these measurements regardless of
  the the <i>center</i> and <i>background</i> parameters which apply only to
  the photometry and profile fitting to the individual pixel values.
  To form the radially smoothed profile an image interpolator function is fit
  to the region containing the object.  The enclosed flux profile (total flux
  within a particular radius) is computed.  The sampling is done at a much
  finer resolution than individual pixels.  The subsampling scheme is that
  described in <b>psfmeasure</b> and is such that the center of the profile is
  more finely sampled than the edges of the profile.
  Because the image interpolator function may not be very good for narrow
  profiles a second iteration is done if the radius enclosing half the flux
  is less than two pixels.  In this second iteration an analytic, radially
  symmetric Gaussian profile is subtracted from the image raster and the
  interpolation function is fit to the residuals.  Subpixel values are then
  computed by evaluating the analytic function plus the interpolated residual
  value.
  There are two FWHM measurements computed using the enclosed flux
  radial profile.  One is to fit a Gaussian or Moffat profile to the
  enclosed flux profile.  The type is selected by the same <i>fittype</i>
  parameter used to select the profile to fit to the individual pixel
  values.  As with the direct fit the Moffat beta value may be fixed or
  included in the fit.  The FWHM of the fit is then printed on the
  status line, terminal output, and log file.
  The other FWHM measurement directly measure the FWHM independent of a
  profile model.  The derivative of the enclosed flux profile is computed.
  This derivative is the azimuthally averaged radial profile with the radial
  bin sampling mentioned above.  The peak of this profile is found and the
  FWHM is twice the radius of the profile at half the peak value.  This
  <span style="font-family: monospace;">"direct FWHM"</span> is part of the output and is also used for the iterative
  adjustment of the fitting radius as noted above.
  <dl>
  <dt><b>a</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='a' Line='a' -->
  <dd>The output consists of the image line and column, the coordinates, the
  final radius used for the photometry and fitting, magnitude, flux, mean
  background, peak value of the profile fit, e, pa (in degrees between -90
  and +90 with 0 along the x axis), the Moffat beta value if a Moffat profile
  is fit, and three measures of the FWHM.  The coordinates are those
  specified by the <i>wcs</i> and formatted by the format parameters.  For the
  logical wcs the coordinates will be the same as the column and line
  values.  If a value is numerically undefined then INDEF is printed.  The
  FWHM values are, in order, the profile fit to the enclosed flux, the
  profile fit to the individual pixels, and the direct measurement from the
  derivative of the enclosed flux profile.  Note that except for the direct
  method, the other estimates are not really measurements of the FWHM but are
  quantities which give the correct FWHM for the specified profile type.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">','</span></b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='','' -->
  <dd>The output consists of the image line and column, magnitude, flux, number
  of pixels within the aperture, mean background, r (moment FWHM), e, pa (in
  degrees between -90 and +90 with 0 along the x axis), and the peak value
  and FWHM of the profile fit.  The label GFWHM indicates a Gaussian fit
  while the label MFWHM indicates a Moffat profile fit.  If a quantity is
  numerically undefined then INDEF is printed.
  </dd>
  </dl>
  This aperture photometry and FWHM tool is intended only for general image
  analysis and quick look measurements.  The background fitting, photometry,
  and FWHM techniques used are not intended for serious astronomical
  photometry; other packages, e.g., <i>noao.digiphot.apphot</i>, should be
  used if precise results are desired.
  </dd>
  </dl>
  <dl id="l_b">
  <dt><b>b</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='b' Line='b' -->
  <dd>The integer pixel coordinates defining a region of the image are printed.
  Two cursor positions are used to select the range of columns and lines.
  The output format consists of the starting and ending column
  coordinates and the starting and ending line coordinates.  This format is
  used as input by some tasks and can be used to generate image sections if
  desired.
  </dd>
  </dl>
  <dl id="l_j">
  <dt><b>j, k</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='j' Line='j, k' -->
  <dd>The fitted gaussian center, peak, sigma, full width at half maximum, and
  background at the center is computed and printed.
  </dd>
  </dl>
  <dl id="l_m">
  <dt><b>m</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='m' Line='m' -->
  <dd>Statistics of a rectangular region centered on the cursor position are
  computed and printed.  The size of the statistics box is set by the
  parameters <i>ncstat</i> and <i>nlstat</i>.  The output format consists
  of the image section, the number of pixels, the mean, the median, the
  standard deviation, the minimum, and the maximum.
  </dd>
  </dl>
  <dl id="l_x">
  <dt><b>x, y</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='x' Line='x, y' -->
  <dd>The cursor x and y coordinates and the pixel value nearest this position
  are printed.  The <span style="font-family: monospace;">'y'</span> key may be used define a relative origin.  If
  an origin is defined (is not 0,0) then additional quantities are printed.
  These quantities are origin coordinates, the delta x and delta y distances,
  the radial distance, and the position angle (in degrees counterclockwise from
  the x axis).
  </dd>
  </dl>
  <dl id="l_z">
  <dt><b>z</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='z' Line='z' -->
  <dd>A 10x10 grid of pixel values is printed.  The integer coordinates are
  also printed around the grid.
  </dd>
  </dl>
  <p>
  GRAPHICS OUTPUT
  </p>
  <p>
  The following commands produce graphics output to the specified graphics
  device (normally the graphics terminal).
  </p>
  <dl id="l_c">
  <dt><b>c</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='c' Line='c' -->
  <dd>A plot of a column or average of columns is made with the line number as
  the ordinate and the pixel value as the abscissa.  The averaging number
  and various graph options are specified by the parameters from the
  <b>cimexam</b> parameter set.
  </dd>
  </dl>
  <dl id="l_e">
  <dt><b>e</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='e' Line='e' -->
  <dd>A contour plot of a region centered on the cursor is made.  The
  size of the region and various contouring and labeling options are
  specified by the parameters from the <b>eimexam</b> parameter set.
  </dd>
  </dl>
  <dl id="l_h">
  <dt><b>h</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='h' Line='h' -->
  <dd>A histogram of a region centered on the cursor is made.  The size
  of the region and various binning parameters are specified by
  the parameters from the <b>himexam</b> parameter set.
  </dd>
  </dl>
  <dl id="l_l">
  <dt><b>l</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='l' Line='l' -->
  <dd>A plot of a line or average of lines is made with the column number as
  the ordinate and the pixel value as the abscissa.  The averaging number
  and various graph options are specified by the parameters from the
  <b>limexam</b> parameter set.
  </dd>
  </dl>
  <dl id="l_r">
  <dt><b>r, <span style="font-family: monospace;">'.'</span></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='r' Line='r, '.'' -->
  <dd>A radial profile plot is made.  As with <span style="font-family: monospace;">'a'</span>/<span style="font-family: monospace;">','</span> there are options for centering
  and background subtraction.  There are also graphics option to set the
  radius to be plotted (<i>rplot</i>) and to overplot the profile fit
  (<i>fitplot</i>).  The measurement algorithms are those described for the
  <span style="font-family: monospace;">'a'</span>/<span style="font-family: monospace;">','</span> key and the output is the same except that there is no header line and
  the object center is given in the graph title rather than on the graphics
  status line.  The aperture sum and graph options are specified by the
  parameters from the <b>rimexam</b> parameter set.
  </dd>
  </dl>
  <dl id="l_s">
  <dt><b>s</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='s' Line='s' -->
  <dd>A surface plot of a region centered on the cursor is made.  The size
  of the region and various surface and labeling options are
  specified by the parameters from the <b>simexam</b> parameter set.
  </dd>
  </dl>
  <dl id="l_u">
  <dt><b>u, v</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='u' Line='u, v' -->
  <dd>A plot of a vector defined by two cursor positions is made.  The <span style="font-family: monospace;">'u'</span>
  plot uses the first cursor position to define the center of the vector
  and the second position to define the endpoint.  The vector is extended
  an equal distance in the opposite direction and the graph x coordinates
  are the radial distance from the center position.  The <span style="font-family: monospace;">'v'</span> plot
  uses the two cursor positions as endpoints and the coordinates are
  the radial distance from the first cursor position.  The vector may
  be averaged over a specified number of parallel vectors.  The
  averaging number and various graph options are specified by the parameters
  from the <b>vimexam</b> parameter set.
  </dd>
  </dl>
  <p>
  MISCELLANEOUS COMMANDS
  </p>
  <p>
  The following commands control useful features of the task.
  </p>
  <dl id="l_d">
  <dt><b>d</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='d' Line='d' -->
  <dd>The display command given by the parameter <i>display</i> is given
  with appropriate image name.  By default this loads the image
  display using the <b>tv.display</b> task.  When using an input image
  list this operation also appends new images to the list for subsequent
  <span style="font-family: monospace;">'n'</span> and <span style="font-family: monospace;">'p'</span> commands.
  </dd>
  </dl>
  <dl id="l_f">
  <dt><b>f</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='f' Line='f' -->
  <dd>Redraw the last graph.  If the <i>autoredraw</i> parameter is no then
  this is used to redraw a graph after making parameter changes with
  colon commands.  If the parameter is yes then any colon command which
  affects the current plot will execute a redraw automatically.
  </dd>
  </dl>
  <dl id="l_g">
  <dt><b>g, i</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='g' Line='g, i' -->
  <dd>Cursor input may be selected to be from the graphics cursor (g) or
  image display cursor (i).
  </dd>
  </dl>
  <dl id="l_n">
  <dt><b>n, p</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='n' Line='n, p' -->
  <dd>Go to the next or previous image in the image list or display frames.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Overplot the next graph.  This generally only makes sense with the
  line, column, and histogram plots.
  </dd>
  </dl>
  <dl id="l_q">
  <dt><b>q</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='q' Line='q' -->
  <dd>Quit the task.
  </dd>
  </dl>
  <dl id="l_t">
  <dt><b>t</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='t' Line='t' -->
  <dd>Output an image centered on the cursor position with name and size set
  by the <i>output</i>, <i>ncoutput</i> and <i>nloutput</i> parameters.
  Note that the cursor input might be from a contour, surface, or other
  plot as well as from the image display.
  </dd>
  </dl>
  <dl id="l_w">
  <dt><b>w</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='w' Line='w' -->
  <dd>Toggle output to the logfile.  If no logfile is specified this has no
  effect except to print a message.  If the logfile is specified a message
  is printed indicating that the logfile has been opened or closed.
  Every time the logfile is opened the current image name and title is
  entered as well as when the image is changed.  The logfile name may
  be set or changed by a colon command.
  </dd>
  </dl>
  <dl>
  <dt><b>:select</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':select' -->
  <dd>Select an image.  If an input image list is used the specified index
  number selects an image from the list.  If an input image list is not
  used and the image display is used then the specified display frame
  is selected.  If the new image is different from the previous image
  an identification line is inserted in the logfile if it is open.
  </dd>
  </dl>
  <dl>
  <dt><b>:eparam, :unlearn</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':eparam, :unlearn' -->
  <dd>These colon commands manipulate the various parameter sets as
  described below.
  </dd>
  </dl>
  <dl>
  <dt><b>:c&lt;#&gt;, :l&lt;#&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':c&lt;#&gt;, :l&lt;#&gt;' -->
  <dd>Special colon commands to plot specific columns or lines, symbolically
  shown as &lt;#&gt;, rather than use a cursor position.
  </dd>
  </dl>
  <dl>
  <dt><b>:&lt;column&gt; &lt;line&gt; &lt;key&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':&lt;column&gt; &lt;line&gt; &lt;key&gt;' -->
  <dd>Special colon command syntax to explicitly give image coordinates for
  a cursor command key.
  </dd>
  </dl>
  <p>
  COLON COMMANDS
  </p>
  <p>
  Sometimes one wants to explicitly enter the coordinates for a command.
  This may be done with a colon command having the following syntax:
  </p>
  <p>
  	:&lt;column&gt; &lt;line&gt; &lt;key&gt;
  </p>
  <p>
  where column and line are the coordinates and key is the command.
  If the line is not given then &lt;column&gt; = &lt;line&gt;.  For the frequently
  used line and column plots there is also the simple syntax:
  </p>
  <div class="highlight-default-notranslate"><pre>
  :c&lt;column&gt;      or      :l&lt;line&gt;
  </pre></div>
  <p>
  with no space, e.g., <span style="font-family: monospace;">":l64"</span>.
  </p>
  <p>
  Every parameter except the input image list and the display command
  may be queried or set by a
  colon command.  In addition the parameter sets for the various graphs
  and aperture sum algorithm may be edited using the <b>eparam</b> editor
  and reinitialized to default values using the <b>unlearn</b> command.
  There are a large number of parameters as well as many graph types /
  parameter sets.  To achieve some consistency and order as well as
  simplify the colon commands several things have been done.
  </p>
  <p>
  Many parameters occur in more than one graph type.  This includes things
  like graph labeling, tickmarks, and so forth.  When issuing a colon
  command for one of these parameters the current graph type is assumed
  to be the one affected.  If the graph type is wrong or no graph has
  been made then a warning is given.
  </p>
  <p>
  If the parameter only occurs in one parameter set then the colon command
  may be used with any current graph.  However, if the parameter affects the
  current graph and the automatic redraw option is set then the graph will
  be redrawn.
  </p>
  <p>
  The eparam and unlearn commands also apply by default to the parameters
  for the current graph.  However, they may take the keystroke character
  for the graph as an argument to override this.  If the current graph
  parameters are changed and the automatic redraw option is set then
  the graph will be redrawn.
  </p>
  <p>
  The important colon commands <span style="font-family: monospace;">'x'</span> and <span style="font-family: monospace;">'y'</span> affect the x1, y1, x2, y2
  parameters in most of the graphs.  They are frequently used to override
  the automatic graph scaling.  If no arguments are given the window
  limits are set to INDEF resulting in plotting the full range of the
  data plus a buffer.  If two values are given then only that range of
  the data will be plotted.
  </p>
  </section>
  <section id="s_commands">
  <h3>Commands</h3>
  <p style="text-align:center">Cursor Keys
  
  </p>
  <div class="highlight-default-notranslate"><pre>
  ?       Print help
  a       Aperture sum, moment parameters, and profile fit
  b       Box coordinates for two cursor positions - c1 c2 l1 l2
  c       Column plot
  d       Load the image display
  e       Contour plot
  f       Redraw the last graph
  g       Graphics cursor
  h       Histogram plot
  i       Image cursor
  j       Fit 1D gaussian to image lines
  k       Fit 1D gaussian to image columns
  l       Line plot
  m       Statistics
              image[section] npixels mean median stddev min max
  n       Next frame or image
  o       Overplot
  p       Previous frame or image
  q       Quit
  r       Radial profile plot with fit and aperture sum values
  s       Surface plot
  t       Output image centered on cursor (parameters output, ncoutput, nloutput)
  u       Centered vector plot from two cursor positions
  v       Vector plot between two cursor positions
  w       Toggle write to logfile
  x       Print coordinates
              col line pixval [xorign yorigin dx dy r theta]
  y       Set origin for relative positions
  z       Print grid of pixel values - 10 x 10 grid
  ,       Quick Gaussian/Moffat photometry
  </pre></div>
  <p style="text-align:center">Colon Commands
  
  </p>
  <p>
  Explicit image coordinates may be entered using the colon command syntax:
  </p>
  <p>
  	:&lt;column&gt; &lt;line&gt; &lt;key&gt;
  </p>
  <p>
  where column and line are the image coordinates and the key is one
  of the cursor keys.  A special syntax for line or column plots is also
  available as :c# or :l# where # is a column or line and no space is
  allowed.
  </p>
  <p>
  Other colon commands set or show parameters governing the plots and other
  features of the task.  Each graph type has it's own set of parameters.
  When a parameter applies to more than one graph the current graph is assumed.
  If the current graph is not applicable then a warning is given.  The
  <span style="font-family: monospace;">"eparam"</span> and <span style="font-family: monospace;">"unlearn"</span> commands may be used to change many parameters and
  without an argument the current graph parameters are modified while with
  the graph key as an argument the appropriate parameter set is modified.
  In the list below the graph key(s) to which a parameter applies are shown.
  </p>
  <div class="highlight-default-notranslate"><pre>
  allframes               Cycle through all display frames to display images
  angh        s           Horizontal angle for surface plot
  angv        s           Vertical angle for surface plot
  autoredraw  cehlrsuv    Automatically redraw graph after colon command?
  autoscale   h           Adjust number of histogram bins to avoid aliasing
  axes        s           Draw axes in surface plot?
  background  jkr         Subtract background for radial plot and photometry?
  banner      cehjklrsuv  Include standard banner on plots?
  beta        ar          Moffat beta parameter (INDEF to fit or value to fix)
  boundary    uv          Boundary extension type for vector plots
  box         cehjklruv   Draw box around graph?
  buffer      r           Buffer distance for background subtraction
  ceiling     es          Data ceiling for contour and surface plots
  center      jkr         Find center for radial plot and photometry?
  constant    uv          Constant value for boundary extension in vector plots
  dashpat     e           Dash pattern for contour plot
  eparam      cehjklrsuv  Edit parameters
  fill        e           Fill viewport vs enforce unity aspect ratio?
  fitplot     r           Overplot profile fit on data?
  fittype     ar          Profile fitting type (gaussian|moffat)
  floor       es          Data floor for contour and surface plots
  interval    e           Contour interval (0 for default)
  iterations  ar          Iterations on fitting radius
  label       e           Draw axis labels for contour plot?
  logfile                 Log file name
  logx        chjklruv    Plot x axis logarithmically?
  logy        chjklruv    Plot y axis logarithmically?
  magzero     r           Magnitude zero for photometry
  majrx       cehjklruv   Number of major tick marks on x axis
  majry       cehjklruv   Number of major tick marks on y axis
  marker      chjklruv    Marker type for graph
  minrx       cehjklruv   Number of minor tick marks on x axis
  minry       cehjklruv   Number of minor tick marks on y axis
  naverage    cjkluv      Number of columns, lines, vectors to average
  nbins       h           Number of histogram bins
  ncolumns    ehs         Number of columns in contour, histogram, or surface plot
  ncontours   e           Number of contours (0 for default)
  ncoutput                Number of columns in output image
  ncstat                  Number of columns in statistics box
  nhi         e           hi/low marking option for contours
  nlines      ehs         Number of lines in contour, histogram, or surface plot
  nloutput                Number of lines in output image
  nlstat                  Number of lines in statistics box
  output                  Output image root name
  pointmode   chjkluv     Plot points instead of lines?
  radius      r           Radius of object aperture for radial plot and photometry
  round       cehjklruv   Round axes to nice values?
  rplot       jkr         Radius to plot in 1D and radial profile plots
  select                  Select image or display frame
  sigma       jk          Initial sigma for 1D gaussian fits
  szmarker    chjklruv    Size of marks for point mode
  ticklabels  cehjklruv   Label ticks?
  title       cehjklrsuv  Optional title for graph
  top_closed  h           Close last bin of histogram
  unlearn     cehjklrsuv  Unlearn parameters to default values
  wcs                     World coordinate system for axis labels and readback
  width       jkr         Width of background region
  x [min max] chjklruv    Range of x to be plotted (no values for autoscaling)
  xformat                 Coordinate format for column world coordinates
  xlabel      cehjklrsuv  Optional label for x axis
  xorder      jkr         X order of surface for background subtraction
  y [min max] chjklruv    Range of y to be plotted (no values for autoscaling)
  yformat                 Coordinate format for line world coordinates
  ylabel      cehjklrsuv  Optional label for y axis
  yorder      r           Y order of surface for background subtraction
  z1          h           Lower intensity value limit of histogram
  z2          h           Upper intensity value limit of histogram
  zero        e           Zero level for contour plot
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following  example illustrates many of the features in a descriptive
  way using the standard image dev$pix.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imexam dev$pix nframes=2
  [The image is loaded in the display if not already loaded]
  &lt;Image cursor&gt; l          # Make a line plot
  &lt;Image cursor&gt; e          # Make a contour plot
  &lt;image cursor&gt; d          # Load a new image
  image name: saga
  display frame (1:) (1): 2
  &lt;Image cursor&gt; e          # Make a contour plot
  &lt;Image cursor&gt; g          # Switch to graphics cursor
  &lt;Graph cursor&gt; u          # Mark the center of a vector
  &lt;Graph cursor&gt; u          # Mark endpoint make a vector plot
  &lt;Graph cursor&gt; i          # Go back to display
  &lt;Image cursor&gt; r          # Select star and make radial plot
  &lt;Image cursor&gt; :rplot 10  # Set radius of plot
  &lt;Image cursor&gt; :epar      # Set radius plot parameters
  &lt;Image cursor&gt; c          # Make column plot
  &lt;Image cursor&gt; :100 l     # Line 100 of image 1
  &lt;Image cursor&gt; :20 30 e   # Contour plot at (20,30)
  &lt;Image cursor&gt; p          # Go to previous image
  &lt;Image cursor&gt; n          # Go to next image
  &lt;Image cursor&gt; :sel 1     # Select image 1
  &lt;Image cursor&gt; :log log   # Set log file
  &lt;Image cursor&gt; w          # Begin logging
  Log file log is open
  &lt;Image cursor&gt; a          # Do aperture sum on star 1
  &lt;Image cursor&gt; a          # Do aperture sum on star 2
  &lt;Image cursor&gt; a          # Do aperture sum on star 3
  &lt;Image cursor&gt; a          # Do aperture sum on star 4
  &lt;Image cursor&gt; w          # Close log file
  Log file log is closed
  &lt;Image cursor&gt; y          # Mark position of galaxy center
  &lt;Image cursor&gt; x          # Print position relative to center
  &lt;Image cursor&gt; x          # Print position relative to center
  &lt;Image cursor&gt; s          # Make surface plot
  &lt;Image cursor&gt; q          # Quit
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  If an operation is interrupted, e.g., an image display or surface plot,
  <i>imexamine</i> is terminated rather than the operation in progress.
  </p>
  <p>
  When used on a workstation <i>imexamine</i> attempts to always position the
  cursor to the window (text, image, or graphics) from which input is being
  taken.  Moving the mouse manually while the program is also trying to move
  it can cause the mouse to be positioned to the wrong window, requiring that
  it be manually moved to the window from which input is currently being taken.
  </p>
  <p>
  When entering a colon command in image cursor mode, if one types too fast
  the characters typed before the mouse is moved to the input window
  will be lost.  To avoid this, pause a moment after typing the colon, before
  entering the command, and verify that the mouse has been moved to the correct
  window.  In the future colon command input will be entered without moving
  the mouse out of the image window, which will avoid the problem.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_IMEXAMINE">
  <dt><b>IMEXAMINE V2.11.4</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IMEXAMINE' Line='IMEXAMINE V2.11.4' -->
  <dd>(<span style="font-family: monospace;">'t'</span>): A new cursor key to create an output image.
  </dd>
  </dl>
  <dl id="l_IMEXAMINE">
  <dt><b>IMEXAMINE V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IMEXAMINE' Line='IMEXAMINE V2.11' -->
  <dd>(<span style="font-family: monospace;">'a'</span> and <span style="font-family: monospace;">'r'</span>): The fit to the radial profile points now includes both a
  Gaussian and a Moffat profile.  The Moffat profile exponent parameter,
  beta, may be fixed or left free to be fit.
  (<span style="font-family: monospace;">'a'</span> and <span style="font-family: monospace;">'r'</span>): New estimates of the FWHM were added to the <span style="font-family: monospace;">'a'</span> and <span style="font-family: monospace;">'r'</span>
  keys.  These include the Moffat profile fit noted above, a direct
  measurement of the FWHM from the radially binned profile, and a Gaussian or
  Moffat fit to the radial enclosed flux profile.  The output from these keys
  was modified to include the new information.
  (<span style="font-family: monospace;">'a'</span> and <span style="font-family: monospace;">'r'</span>): The direct FWHM may be used to iteratively adjust the
  fitting radius to lessen the dependence on the initial fitting
  radius value.
  (<span style="font-family: monospace;">','</span> and <span style="font-family: monospace;">'.'</span>): New keys to do the Gaussian or Moffat fitting without
  iteration or the enclosed flux and direct measurements.  The output
  format is the same as the previous version.
  (<span style="font-family: monospace;">'k'</span>): Added a kimexam parameter set.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  cursors, eparam, unlearn, plot.*, tvmark, digiphot.*, apphot.*,
  implot, splot, imedit, radplt, imcntr, imhistogram, imstatistics, display
  psfmeasure.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ADDITIONAL PARAMETERS' 'DESCRIPTION' 'COMMANDS' 'EXAMPLES' 'BUGS' 'REVISIONS' 'SEE ALSO'  -->
  

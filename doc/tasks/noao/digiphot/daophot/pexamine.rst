.. _pexamine:

pexamine: Interactively examine and edit a daophot database
===========================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pexamine input output image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The name of the input photometry catalog. Input may be either an APPHOT/DAOPHOT
  text database file or an STSDAS binary table database.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The name of the edited output catalog. Output is either an APPHOT/DAOPHOT text
  database or an STSDAS binary table database depending on the file type of
  <i>input</i>. If output = <span style="font-family: monospace;">""</span> no output catalog is written.
  </dd>
  </dl>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The name of the input image corresponding to the input photometry catalog. If
  <i>image</i> is <span style="font-family: monospace;">""</span> no image will be attached to PEXAMINE and some interactive
  catalog examining commands will not be available.  All the catalog editing
  commands however are still available.
  </dd>
  </dl>
  <dl id="l_deletions">
  <dt><b>deletions = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='deletions' Line='deletions = ""' -->
  <dd>The name of an optional output deletions photometry catalog. Deletions is either
  an APPHOT/DAOPHOT text database or an STSDAS binary table database depending on
  the file type of <i>input</i>. If deletions is <span style="font-family: monospace;">""</span> no deletions file is written.
  </dd>
  </dl>
  <dl id="l_photcolumns">
  <dt><b>photcolumns = <span style="font-family: monospace;">"daophot"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='photcolumns' Line='photcolumns = "daophot"' -->
  <dd>The list of standard photometry columns that are loaded when pexamine is run.
  The options are listed below.
  <dl>
  <dt><b><span style="font-family: monospace;">"daophot"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"daophot"' -->
  <dd>The standard columns for the DAOPHOT package. The current list is GROUP, ID,
  XCENTER, YCENTER, MSKY, MAG, MERR, CHI, SHARP and NITER. If any of these columns
  are multi-valued, (as in the case of magnitudes measured through more than one
  aperture), the first value is selected. The standard list may easily be
  extended at user request.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"apphot"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"apphot"' -->
  <dd>The standard columns for the APPHOT package. The current list is ID, XCENTER,
  YCENTER, MSKY, MAG, and MERR. If any of these columns are multi-valued, (as in
  the case of magnitudes measured through more than one aperture), the first
  value is selected. The standard list may easily be extended at user request.
  </dd>
  </dl>
  <dl>
  <dt><b>user list</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='user' Line='user list' -->
  <dd>A user supplied list of standard columns. Column names are listed in full in
  either upper or lower case letters, separated by commas. If more than one value
  of a multi-valued column is requested the individual values must be listed
  separately as in the following example ID, XCENTER, YCENTER, MAG[1], MERR[1],
  MAG[2], MERR[2].
  </dd>
  </dl>
  Photcolumns can be changed interactively from within PEXAMINE at the cost
  of rereading the database. 
  </dd>
  </dl>
  <dl id="l_xcolumn">
  <dt><b>xcolumn = <span style="font-family: monospace;">"mag"</span> (magnitude), ycolumn = <span style="font-family: monospace;">"merr"</span> (magnitude error)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcolumn' Line='xcolumn = "mag" (magnitude), ycolumn = "merr" (magnitude error)' -->
  <dd>The names of the two columns which define the default X-Y plot. Xcolumn and
  ycolumn must be listed in <i>photcolumns</i> or <i>usercolumns</i> but may be
  changed interactively by the user. If either xcolumn or ycolumn is a
  multi-valued quantity and more than one value is listed in <i>photcolumns</i>
  or <i>usercolumns</i> then the desired value number must be specified explicitly
  in, e.g. MAG[2] or MERR[2].
  </dd>
  </dl>
  <dl id="l_hcolumn">
  <dt><b>hcolumn = <span style="font-family: monospace;">"mag"</span> (magnitude)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hcolumn' Line='hcolumn = "mag" (magnitude)' -->
  <dd>The name of the column which defines the default histogram plot.  Hcolumn
  must be listed in <i>photcolumns</i> or <i>usercolumns</i> but may be changed
  interactively by the user. If hcolumn is a multi-valued quantity and more than
  one value is listed in <i>photcolumns</i> or <i>usercolumns</i> then the desired
  value must be specified explicitly in hcolumn, e.g. MAG[2].
  </dd>
  </dl>
  <dl id="l_xposcolumn">
  <dt><b>xposcolumn = <span style="font-family: monospace;">"xcenter"</span>, yposcolumn = <span style="font-family: monospace;">"ycenter"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xposcolumn' Line='xposcolumn = "xcenter", yposcolumn = "ycenter"' -->
  <dd>The names of the two columns which define the X and Y coordinates in <i>image</i>
  of the objects in the catalog. This information is required if the image
  display and image cursor are to be used to visually identify objects in the
  image with objects in the catalog or if plots of image data are requested.
  Xposcolumn and yposcolumn must be listed in <i>photcolumns</i> or
  <i>usercolumns</i> but may be changed interactively by the user.
  </dd>
  </dl>
  <dl id="l_usercolumns">
  <dt><b>usercolumns = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='usercolumns' Line='usercolumns = ""' -->
  <dd>The list of columns loaded into memory in addition to the standard photometry
  columns <i>photcolumns</i>. The column names are listed in full in upper or
  lower case letters and separated by commas. Usercolumns can be changed
  interactively from within PEXAMINE at the cost of rereading the database. 
  </dd>
  </dl>
  <dl id="l_first_star">
  <dt><b>first_star = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='first_star' Line='first_star = 1' -->
  <dd>The index of the first object to be read out of the catalog.
  </dd>
  </dl>
  <dl id="l_max_nstars">
  <dt><b>max_nstars = 5000</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='max_nstars' Line='max_nstars = 5000' -->
  <dd>The maximum number of objects that are loaded into memory at task startup time,
  beginning at object <i>first_star</i>. If there are more than max_nstars in the
  catalog only the first max_nstars objects are read in.
  </dd>
  </dl>
  <dl id="l_match_radius">
  <dt><b>match_radius = 2.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='match_radius' Line='match_radius = 2.0' -->
  <dd>The tolerance in pixels to be used for matching objects in the catalog with
  objects marked on the display with the image cursor.
  </dd>
  </dl>
  <dl id="l_use_display">
  <dt><b>use_display = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='use_display' Line='use_display = yes' -->
  <dd>Use the image display? Users without access to an image display should set
  use_display to <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_icommands">
  <dt><b>icommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='icommands' Line='icommands = ""' -->
  <dd>The image display cursor. If null the standard image cursor is used whenever
  image cursor input is requested. A cursor file in the appropriate format may be
  substituted by specifying the name of the file. Also the image cursor may be
  changed to query the graphics device or the terminal by setting the environment
  variable <span style="font-family: monospace;">"stdimcur"</span> to <span style="font-family: monospace;">"stdgraph"</span> or <span style="font-family: monospace;">"text"</span> respectively.
  </dd>
  </dl>
  <dl id="l_gcommands">
  <dt><b>gcommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gcommands' Line='gcommands = ""' -->
  <dd>The graphics cursor. If null the standard graphics cursor is used whenever
  graphics cursor input is requested. A cursor file in the appropriate format may
  be substituted by specifying the name of the file.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>The default graphics device.
  </dd>
  </dl>
  </section>
  <section id="s_plotting_parameters">
  <h3>Plotting parameters</h3>
  <p>
  PEXAMINE supports five types of plots 1) an X-Y column plot 2) a histogram
  column plot 3) a radial profile plot 4) a surface plot and 5) a contour plot.
  Each supported plot type has its own parameter set which controls the
  appearance of the plot.  The names of the five parameter sets are listed below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cntrplot    Parameters for the contour plot
  histplot    Parameters for the column histogram plot
  radplot     Parameters for radial profile plot
  surfplot    Parameters for surface plot
  xyplot      Parameters for the X-Y column plot
  </pre></div>
  <p>
  The same  parameters dealing with graph formats occur in many of the parameter
  sets while some are specific only to one parameter set. In the summary below
  those common to more than one parameter set are shown only once. The characters
  in parenthesis are the graph key prefixes for the parameter sets in which the
  parameter occurs.
  </p>
  <dl id="l_angh">
  <dt><b>angh = -33., angv = 25.		(s)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='angh' Line='angh = -33., angv = 25.		(s)' -->
  <dd>Horizontal and vertical viewing angles in degrees for surface plots.
  </dd>
  </dl>
  <dl id="l_axes">
  <dt><b>axes = yes				(s)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='axes' Line='axes = yes				(s)' -->
  <dd>Draw axes along the edge of surface plots ?
  </dd>
  </dl>
  <dl id="l_banner">
  <dt><b>banner = yes 			 (chrsx)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='banner' Line='banner = yes 			 (chrsx)' -->
  <dd>Add a standard banner to a graph ?  The standard banner includes the IRAF user
  and host identification and the date and time.
  </dd>
  </dl>
  <dl id="l_box">
  <dt><b>box = yes 				(chrx)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='box' Line='box = yes 				(chrx)' -->
  <dd>Draw graph box and axes ?
  </dd>
  </dl>
  <dl id="l_ceiling">
  <dt><b>ceiling = INDEF			(cs)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='ceiling' Line='ceiling = INDEF			(cs)' -->
  <dd>Ceiling data value for contour and surface plots. A value of INDEF does not
  apply a ceiling.  In contour plots a value of 0. also does not apply a ceiling.
  </dd>
  </dl>
  <dl id="l_dashpat">
  <dt><b>dashpat = 528			(c)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='dashpat' Line='dashpat = 528			(c)' -->
  <dd>Dash pattern for negative contours.
  </dd>
  </dl>
  <dl id="l_fill">
  <dt><b>fill = no (yes)			(c) (hrx)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='fill' Line='fill = no (yes)			(c) (hrx)' -->
  <dd>Fill the output viewport regardless of the device aspect ratio ?
  </dd>
  </dl>
  <dl id="l_floor">
  <dt><b>floor = INDEF			(cs)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='floor' Line='floor = INDEF			(cs)' -->
  <dd>Floor data value for contour and surface plots. A value of INDEF does not apply
  a floor. In contour plots a value of 0. also does not apply a floor.
  </dd>
  </dl>
  <dl id="l_grid">
  <dt><b>grid = no				(rx)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='grid' Line='grid = no				(rx)' -->
  <dd>Draw grid lines at major tick marks ?
  </dd>
  </dl>
  <dl id="l_interval">
  <dt><b>interval = 0.0			(c)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='interval' Line='interval = 0.0			(c)' -->
  <dd>Contour interval.  If 0.0, a contour interval is chosen which places 20 to 30
  contours spanning the intensity range of the image.
  </dd>
  </dl>
  <dl id="l_label">
  <dt><b>label= no				(c)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='label' Line='label= no				(c)' -->
  <dd>Label the major contours in the contour plot ?
  </dd>
  </dl>
  <dl id="l_logx">
  <dt><b>logx = no, logy = no		(rx) (hrx)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='logx' Line='logx = no, logy = no		(rx) (hrx)' -->
  <dd>Plot the x or y axis logarithmically ? The default for histogram plots is to
  plot the y axis logarithmically.
  </dd>
  </dl>
  <dl id="l_majrx">
  <dt><b>majrx=5, minrx=5, majry=5, minry=5	(chrx)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='majrx' Line='majrx=5, minrx=5, majry=5, minry=5	(chrx)' -->
  <dd>Maximum number of major tick marks on each axis and number of minor tick marks
  between major tick marks.
  </dd>
  </dl>
  <dl id="l_marker">
  <dt><b>marker = <span style="font-family: monospace;">"box"</span>			(rx)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='marker' Line='marker = "box"			(rx)' -->
  <dd>Marker to be drawn.  Markers are <span style="font-family: monospace;">"point"</span>, <span style="font-family: monospace;">"box"</span>, <span style="font-family: monospace;">"cross"</span>, <span style="font-family: monospace;">"plus"</span>, <span style="font-family: monospace;">"circle"</span>,
  <span style="font-family: monospace;">"hline"</span>, <span style="font-family: monospace;">"vline"</span> or <span style="font-family: monospace;">"diamond"</span>.
  </dd>
  </dl>
  <dl id="l_nbins">
  <dt><b>nbins = 512				(h)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='nbins' Line='nbins = 512				(h)' -->
  <dd>The number of bins in, or resolution of, histogram plots.
  </dd>
  </dl>
  <dl id="l_ncolumns">
  <dt><b>ncolumns = 21, nlines = 21		(cs)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='ncolumns' Line='ncolumns = 21, nlines = 21		(cs)' -->
  <dd>Number of columns and lines used in contour and surface plots.
  </dd>
  </dl>
  <dl id="l_ncontours">
  <dt><b>ncontours = 5			(c)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='ncontours' Line='ncontours = 5			(c)' -->
  <dd>Number of contours to be drawn. If 0, the contour interval may be specified,
  otherwise 20 to 30 nicely spaced contours are drawn. A maximum of 40 contours
  can be drawn.
  </dd>
  </dl>
  <dl id="l_nhi">
  <dt><b>nhi = -1				(c)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='nhi' Line='nhi = -1				(c)' -->
  <dd>If -1, highs and lows are not marked. If 0, highs and lows are marked on the
  plot. If 1, the intensity of each pixel is marked on the plot.
  </dd>
  </dl>
  <dl id="l_rinner">
  <dt><b>rinner = 0, router = 8</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='rinner' Line='rinner = 0, router = 8' -->
  <dd>The inner and outer radius of the region whose radial profile is to be plotted.
  </dd>
  </dl>
  <dl id="l_round">
  <dt><b>round = no				(chrx)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='round' Line='round = no				(chrx)' -->
  <dd>Extend the axes up to <span style="font-family: monospace;">"nice"</span> values ?
  </dd>
  </dl>
  <dl id="l_szmarker">
  <dt><b>szmarker = 1			(rx)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='szmarker' Line='szmarker = 1			(rx)' -->
  <dd>Size of mark except for points. A positive size less than 1 specifies a fraction
  of the device size. Values of 1, 2, 3, and 4 signify default sizes of increasing
  size.
  </dd>
  </dl>
  <dl id="l_ticklabels">
  <dt><b>ticklabels = yes			(chrx)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='ticklabels' Line='ticklabels = yes			(chrx)' -->
  <dd>Label the tick marks ?
  </dd>
  </dl>
  <dl id="l_top_closed">
  <dt><b>top_closed = no			(h)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='top_closed' Line='top_closed = no			(h)' -->
  <dd>Include z2 in the top histogram bin ? Each bin of the histogram is a subinterval
  that is half open at the top. Top_closed decides whether those pixels with
  values equal to z2 are to be counted in the histogram. If top_closed is yes,
  the top bin will be larger than the other bins.
  </dd>
  </dl>
  <dl id="l_x1">
  <dt><b>x1 = INDEF, x2 = INDEF, y1 = INDEF, y2 = INDEF	(hrx)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='x1' Line='x1 = INDEF, x2 = INDEF, y1 = INDEF, y2 = INDEF	(hrx)' -->
  <dd>Range of graph along each axis.  If INDEF the range is determined from the data
  range. The default y1 for histogram plots is 0.
  </dd>
  </dl>
  <dl id="l_zero">
  <dt><b>zero = 0.				(c)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='zero' Line='zero = 0.				(c)' -->
  <dd>Grayscale value of the zero contour, i.e., the value of a zero point shift
  to be applied to the image data before plotting. Does not affect the values
  of the floor and ceiling parameters.
  </dd>
  </dl>
  <dl id="l_z1">
  <dt><b>z1 = INDEF, z2 = INDEF		(h)</b></dt>
  <!-- Sec='PLOTTING PARAMETERS' Level=0 Label='z1' Line='z1 = INDEF, z2 = INDEF		(h)' -->
  <dd>Range of pixel values to be used in histogram. INDEF values default to the
  range in the region being histogramed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  PEXAMINE is a general purpose tool for interactively examining and editing
  photometry catalogs produced by the APPHOT or DAOPHOT packages. It is intended
  to aid the user in assessing the accuracy of the photometry, in diagnosing
  problems with particular catalog objects, in searching the photometry data for
  relationships between the computed quantities, and in editing the catalog
  based on those observed relationships. PEXAMINE is intended to complement the
  more batch oriented editing facilities of the PSELECT task.
  </p>
  <p>
  PEXAMINE takes the input catalog <i>input</i> and the corresponding image
  <i>image</i> (if defined) and produces an output catalog of selected objects
  <i>output</i> (if defined) and an output catalog of deleted objects
  <i>deletions</i> (if defined). The input catalog may be either an APPHOT/DAOPHOT
  text database or an ST binary table database. The file type of the output
  catalogs <i>output</i> and <i>deletions</i> is the same as that of <i>input</i>.
  </p>
  <p>
  READING IN THE DATA
  </p>
  <p>
  PEXAMINE reads the column data specified by <i>photcolumns</i> and
  <i>usercolumns</i> for up to <i>max_nstars</i> into memory. If there are more
  than <i>max_nstars</i> in the input catalog only the data for the first
  <i>max_nstars</i> is read. The <i>photcolumns</i> parameter defines the list of
  standard photometry columns to be loaded. If <span style="font-family: monospace;">"daophot"</span> or <span style="font-family: monospace;">"apphot"</span> is selected
  then the standard columns are GROUP, ID, XCENTER, YCENTER, MSKY, MAG, MERR,
  CHI, SHARP and NITER and ID, XCENTER, YCENTER, MSKY, MAG and MERR respectively.
  Otherwise the user must set <i>photcolumns</i> to his or her own preferred list
  of standard photometry columns. Non-standard columns may also be specified
  using the parameter <i>usercolumns</i>. Valid column lists contain the full
  names of the specified columns in upper or lower case letters, separated by
  commas. Either <i>photcolumns</i> or <i>usercolumns</i> may be redefined
  interactively by the user after the task has started up, but only at the
  expense of rereading the data from <i>input</i>.
  </p>
  <p>
  PEXAMINE will fail to load a specified column if that column is not in the
  photometry database, is of a datatype other than integer or real, or adding
  that column would exceed the maximum number of columns limit currently set at
  twenty. The user can interactively examine the list of requested and loaded
  standard photometry columns, as well as list all the columns in the input after
  the task has started up.
  </p>
  <p>
  GRAPHICS AND IMAGE COMMAND MODE
  </p>
  <p>
  PEXAMINE accepts commands either from the graphics cursor <i>gcommands</i>
  (graphics command mode) or the image display cursor <i>icommands</i> if available
  (image command mode). PEXAMINE starts up in graphics command mode, but all the
  interactive commands are accessible from both modes and the user can switch
  modes at any time assuming that the <i>use_display</i> parameter to <span style="font-family: monospace;">"yes"</span>.
  </p>
  <p>
  PEXAMINE interprets the cursor position in graphics mode differently from how
  it interprets it in image command mode. In graphics command mode the cursor
  coordinates are the position of the cursor in the current plot, whereas in
  image command mode they are the x and y coordinates of the cursor in the
  displayed image. For example, if the user issues a command to PEXAMINE to
  locate the object in the catalog nearest the point in the current X-Y plot
  marked by the graphics cursor, PEXAMINE does so by searching the data for the
  object whose values of <i>xcolumn</i> and <i>ycolumn</i> most closely match those
  of the current cursor position. If the user issues a command  to PEXAMINE to
  locate the object in the catalog corresponding to the object marked on the
  image display with the image cursor, PEXAMINE does so by searching the data for
  the object whose values of <i>xposcolumn</i> and <i>yposcolumn</i> most closely
  match and fall within <i>match_radius</i> of the current cursor position.
  </p>
  <p>
  Input to PEXAMINE is through single keystroke commands or colon commands.
  Keystroke commands are simple commands that may optionally use the cursor
  position but otherwise require no arguments. The PEXAMINE keystroke commands
  fall into three categories, basic commands, data examining commands and data
  editing commands, all described in detail in the following sections. Colon
  commands take an optional argument and function differently depending on the
  presence or absence of that argument. When the argument is absent colon
  commands are used to display the current value of a parameter or list of
  parameters. When the argument is present they change their current value to
  that argument. The basic colon commands are described in detail below. 
  </p>
  <p>
  BASIC KEYSTROKE COMMANDS
  </p>
  <p>
  These keystroke commands are used to display the help page, switch from
  graphics to image command mode and quit the task.
  </p>
  <dl>
  <dt><b>?</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='?' -->
  <dd>Page through the help for the PEXAMINE task
  </dd>
  </dl>
  <dl>
  <dt><b>:</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':' -->
  <dd>Execute a PEXAMINE colon command.
  </dd>
  </dl>
  <dl id="l_g">
  <dt><b>g</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='g' Line='g' -->
  <dd>Change to graphics command mode. Throughout PEXAMINE graphics command mode is
  the default. All PEXAMINE commands are available in graphics command mode.
  </dd>
  </dl>
  <dl id="l_i">
  <dt><b>i</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='i' Line='i' -->
  <dd>Change to image command mode. All the PEXAMINE commands are available in image
  command mode. However if <i>use_display</i> is no and the image cursor has not
  been aliased to the standard input or a text file image command mode is
  disabled.
  </dd>
  </dl>
  <dl id="l_q">
  <dt><b>q</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='q' Line='q' -->
  <dd>Quit PEXAMINE without writing an output catalog. PEXAMINE queries the user for
  confirmation of this option.
  </dd>
  </dl>
  <dl id="l_e">
  <dt><b>e</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='e' Line='e' -->
  <dd>Quit PEXAMINE and write the output catalog.
  </dd>
  </dl>
  <p>
  DATA EXAMINING COMMANDS
  </p>
  <p>
  The data examining commands fall into two categories, those that examine the
  catalog data including <span style="font-family: monospace;">'l'</span> (catalog listing), <span style="font-family: monospace;">'o'</span> (object listing), <span style="font-family: monospace;">'x'</span> (Y
  column versus X column plot) and <span style="font-family: monospace;">'h'</span> (histogram column plot) commands, and
  those which examine the image data around specific catalog objects including
  <span style="font-family: monospace;">'r'</span> (radial profile plotting), <span style="font-family: monospace;">'s'</span> (surface plotting), <span style="font-family: monospace;">'c'</span> (contour plotting)
  and <span style="font-family: monospace;">'m'</span> (pixel dumping). The latter group require that <i>image</i> be defined.
  A brief summary of each data examining command is given below.
  </p>
  <dl id="l_l">
  <dt><b>l</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='l' Line='l' -->
  <dd>Print out the name, datatype, and units for all the columns in the input
  catalog. The list command can be used to check the contents of the input
  catalog and/or determine why a particular column was not loaded.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Print out the names and values of the stored columns of the object nearest the
  cursor. In graphics mode the current plot type must be X-Y. In image command
  mode the object nearest the cursor must also be no more than <i>match-radius</i>
  pixels away from the image cursor to be found. If an object is found and the
  current plot type is X-Y the graphics cursor is moved to the position of the
  selected object in the X-Y plot.
  </dd>
  </dl>
  <dl id="l_x">
  <dt><b>x</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='x' Line='x' -->
  <dd>Plot the data in <i>ycolumn</i> versus the data in <i>xcolumn</i> excluding any
  already deleted points and identifying objects marked for deletion with a
  cross. X-Y plotting is undefined if <i>xcolumn</i> or <i>ycolumn</i> is undefined.
  </dd>
  </dl>
  <dl id="l_h">
  <dt><b>h</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='h' Line='h' -->
  <dd>Plot the histogram of the data in <i>hcolumn</i> excluding any already deleted
  points and those marked for deletion. Histogram plotting is disabled if
  <i>hcolumn</i> is undefined.
  </dd>
  </dl>
  <dl id="l_r">
  <dt><b>r</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='r' Line='r' -->
  <dd>Plot the radial profile of the object nearest the cursor including only pixels
  within a distance of <i>rinner</i> and <i>router</i> of the object center. Radial
  profile plotting is disabled if <i>image</i> or <i>xposcolumn</i> or
  <i>yposcolumn</i> is undefined.
  </dd>
  </dl>
  <dl id="l_s">
  <dt><b>s</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='s' Line='s' -->
  <dd>Plot the surface plot of the object nearest the cursor including only pixels
  within an image section <i>ncols</i> by <i>nlines</i> around the object center.
  Surface plotting is disabled if <i>image</i> or <i>xposcolumn</i> or
  <i>yposcolumn</i> is undefined.
  </dd>
  </dl>
  <dl id="l_c">
  <dt><b>c</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='c' Line='c' -->
  <dd>Plot the contour plot of the object nearest the cursor including only pixels
  within an image section <i>ncols</i> by <i>nlines</i> around the object center.
  Contour plotting is disabled if <i>image</i> or <i>xposcolumn</i> or
  <i>yposcolumn</i> is undefined.
  </dd>
  </dl>
  <dl id="l_m">
  <dt><b>m</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='m' Line='m' -->
  <dd>Dump the pixel values of a grid of 10 by 10 pixels around the object nearest
  the cursor. Pixel value dumping is disabled if <i>image</i> or <i>xposcolumn</i>
  or <i>yposcolumn</i> is undefined.
  </dd>
  </dl>
  <dl id="l_p">
  <dt><b>p</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='p' Line='p' -->
  <dd>Replot the current graph.
  </dd>
  </dl>
  <p>
  DATA EDITING COMMANDS
  </p>
  <p>
  Data points can be deleted from the catalog in either graphics command mode or
  image command mode. In graphics command mode the graphics cursor and either the
  X-Y or histogram plot is used to delete points. In image command mode the image
  cursor and the displayed image are used to delete points. A data point has three
  possible states good, marked for deletion and deleted. Any one of the keystroke
  commands <span style="font-family: monospace;">'d'</span> (delete point), <span style="font-family: monospace;">'('</span> (delete points with x less than x cursor),
  <span style="font-family: monospace;">')'</span> (delete points with x greater than x cursor, <span style="font-family: monospace;">'^'</span> (delete points with y &gt; y
  cursor), <span style="font-family: monospace;">'v'</span> (delete points with y &lt; y cursor) or <span style="font-family: monospace;">'b'</span> (delete points in a box)
  can be used to mark points for deletion. The <span style="font-family: monospace;">'f'</span> key is used to actually delete
  the points and replot the data. In between marking the points for deletion and
  actually deleting the marked points the <span style="font-family: monospace;">'t'</span> (toggle) key can be used to undelete
  the last set marked. The full list of the data editing keystroke commands is
  given below.
  </p>
  <dl id="l_z">
  <dt><b>z</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='z' Line='z' -->
  <dd>Undelete not just unmark all the data points replot.
  </dd>
  </dl>
  <dl id="l_f">
  <dt><b>f</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='f' Line='f' -->
  <dd>Delete points marked for deletion and replot. Points marked for deletion but
  not actually deleted will be written to the output catalog and not written to
  the deletions catalog.
  </dd>
  </dl>
  <dl id="l_d">
  <dt><b>d</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='d' Line='d' -->
  <dd>Mark the point nearest the cursor for deletion.
  </dd>
  </dl>
  <dl id="l_u">
  <dt><b>u</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='u' Line='u' -->
  <dd>Undelete the marked point nearest the cursor.
  </dd>
  </dl>
  <dl>
  <dt><b>(</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(' -->
  <dd>Mark all points with x values less than the x value of the cursor for deletion.
  In graphics command mode points can only be marked for deletion if the current
  plot type is <span style="font-family: monospace;">"xyplot"</span> or <span style="font-family: monospace;">"histplot"</span>. In image command mode <i>xposcolumn</i> and
  <i>yposcolumn</i> must be defined before points can be marked for deletion.
  </dd>
  </dl>
  <dl>
  <dt><b>)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=')' -->
  <dd>Mark all points with x values greater than the x value of the cursor for
  deletion.  In graphics command mode points can only be marked for deletion if
  the current plot type is <span style="font-family: monospace;">"xyplot"</span> or <span style="font-family: monospace;">"histplot"</span>. In image command mode
  <i>xposcolumn</i> and <i>yposcolumn</i> must be defined before points can be
  marked for deletion.
  </dd>
  </dl>
  <dl id="l_v">
  <dt><b>v</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='v' Line='v' -->
  <dd>Mark all points with y values less than the y value of the cursor for deletion.
  In graphics command mode points can only be marked for deletion if the current
  plot type is <span style="font-family: monospace;">"xyplot"</span>. In image command mode <i>xposcolumn</i> and
  <i>yposcolumn</i> must be defined before points can be marked for deletion.
  </dd>
  </dl>
  <dl>
  <dt><b>^</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='^' -->
  <dd>Mark all points with y values greater than the y value of the cursor for
  deletion.  In graphics command mode points can only be marked for deletion if
  the current plot type is <span style="font-family: monospace;">"xyplot"</span>. In image command mode <i>xposcolumn</i> and
  <i>yposcolumn</i> must be defined before points can be marked for deletion.
  </dd>
  </dl>
  <dl id="l_b">
  <dt><b>b</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='b' Line='b' -->
  <dd>Mark all points within a box whose lower left and upper right hand corners are
  marked by the cursor for deletion. In graphics mode points can only be marked
  for deletion if the current plot type is <span style="font-family: monospace;">"xyplot"</span>. In image command mode
  <i>xposcolumn</i> and <i>yposcolumn</i> must be defined before points can be
  marked for deletion.
  </dd>
  </dl>
  <dl id="l_t">
  <dt><b>t</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='t' Line='t' -->
  <dd>Toggle between marking points for deletion or undeletion. The default is to
  mark points for deletion.
  </dd>
  </dl>
  <p>
  BASIC COLON COMMANDS
  </p>
  <p>
  All the PEXAMINE parameters can be changed interactively with colon commands,
  including those which determine which data is read in, which data is plotted
  and the parameters of each plot. A brief description of the basic commands is
  given here. The full list is given in the following section.
  </p>
  <dl>
  <dt><b>:photcolumns [col1,col2,...]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':photcolumns [col1,col2,...]' -->
  <dd>Show or set the list of requested standard photometry columns and the list
  of loaded photometry columns. If the user supplies a new list of columns the
  data will be reread from disk.
  </dd>
  </dl>
  <dl>
  <dt><b>:usercolumns [col1,col2,...]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':usercolumns [col1,col2,...]' -->
  <dd>Show or set the list of requested user columns and the list of loaded user
  columns. If the user supplies a new list of columns the data will be reread
  from disk.
  </dd>
  </dl>
  <dl>
  <dt><b>:xcolumn [colname]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':xcolumn [colname]' -->
  <dd>Show or set the name of the column to be plotted along the x axis of the X-Y
  plot.
  </dd>
  </dl>
  <dl>
  <dt><b>:ycolumn [colname]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':ycolumn [colname]' -->
  <dd>Show or set the name of the column to be plotted along the y axis of the X-Y
  plot.
  </dd>
  </dl>
  <dl>
  <dt><b>:hcolumn [colname]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':hcolumn [colname]' -->
  <dd>Show or set the name of the column to be whose histogram is to be plotted.
  </dd>
  </dl>
  <dl>
  <dt><b>:eparam [cntrplot/histplot/radplot/surfplot/xyplot]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':eparam [cntrplot/histplot/radplot/surfplot/xyplot]' -->
  <dd>Review or edit the list of parameters for the various plot types.
  </dd>
  </dl>
  <dl>
  <dt><b>:unlearn [cntrplot/histplot/radplot/surfplot/xyplot]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':unlearn [cntrplot/histplot/radplot/surfplot/xyplot]' -->
  <dd>Return the list of parameters for the various plot types to their default
  values.
  </dd>
  </dl>
  <dl>
  <dt><b>:x y key cmd</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':x y key cmd' -->
  <dd>Execute any defined keystroke <span style="font-family: monospace;">"key"</span> supplying the appropriate x and y value in
  place of the cursor position. In graphics command mode the x and y position are
  assumed to be the position in the current graph. In image command mode the x
  and y position are assumed to be the x and y coordinate in the image display.
  </dd>
  </dl>
  </section>
  <section id="s_commands">
  <h3>Commands</h3>
  <div class="highlight-default-notranslate"><pre>
          PEXAMINE Interactive Cursor Keystroke Commands
  
                     Basic Commands
  
  ?       Print help for the PEXAMINE task
  :       PEXAMINE colon commands
  g       Activate the graphics cursor
  i       Activate the image cursor
  e       Exit PEXAMINE and save the edited catalog
  q       Quit PEXAMINE and discard the edited catalog
  
                     Data Examining Commands
  
  l       List the name, datatype and units for all columns in the catalog
  o       Print out the names and values of the stored columns for the
              object nearest the cursor
  x       Replot the current y column versus the current x column
  h       Replot the current histogram
  r       Plot the radial profile of the object nearest the cursor
  s       Plot the surface of the object nearest the cursor
  c       Plot the contour plot of the object nearest the cursor
  m       Print the data values of the object nearest the cursor
  p       Replot the current graph
  
                     Data Editing Commands
  
  z       Reinitialize the data by removing all deletions and replot
  d       Mark the point nearest the cursor for deletion
  u       Undelete the marked point nearest the cursor
  t       Toggle between marking points for deletion or undeletion
  (       Mark points with X &lt; X (cursor) for deletion or undeletion
  )       Mark points with X &gt; X (cursor) for deletion or undeletion
  v       Mark points with Y &lt; Y (cursor) for deletion or undeletion
  ^       Mark points with Y &gt; Y (cursor) for deletion or undeletion
  b       Mark points inside a box for deletion or undeletion
  f       Actually delete the marked points and replot
  
                PEXAMINE Interactive Colon Commands
  
  :xcolumn          [name]             Show/set the X-Y plot X axis quantity
  :ycolumn          [name]             Show/set the X-Y plot Y axis quantity
  :hcolumn          [name]             Show/set the histogram plot quantity
  :photcolumns      [col1,col2,...]    Show/set the list of photometry columns
  :usercolumns      [col1,col2,...]    Show/set the list of user columns
  :delete           [yes/no]           Delete or undelete points
  :eparam           [x/h/r/s/c]        Edit/unlearn the specified plot pset
      or
  :unlearn
  
               PEXAMINE Interactive X-Y Plotting Commands
  
  :x1         [value]       Left  world x-coord if not autoscaling
  :x2         [value]       Right world x-coord if not autoscaling
  :y1         [value]       Lower world y-coord if not autoscaling
  :y2         [value]       Upper world y-coord if not autoscaling
  :szmarker   [value]       Marker size
  :marker [point|box|plus|cross|circle|diamond|hline|vline]    Marker type
  :logx       [yes/no]      Log scale the x axis?
  :logy       [yes/no]      Log scale the y axis?
  :box        [yes/no]      Draw box around periphery of window?
  :ticklabels [yes/no]      Label tick marks?
  :grid       [yes/no]      Draw grid lines at major tick marks?
  :majrx      [value]       Number of major divisions along x axis
  :minrx      [value]       Number of minor divisions along x axis
  :majry      [value]       Number of major divisions along y axis
  :minry      [value]       Number of minor divisions along y axis
  :round      [yes/no]      Round axes to nice values?
  :fill       [yes/no]      Fill viewport vs enforce unity aspect ratio?
  
          PEXAMINE Interactive Histogram Plotting Commands
  
  :nbins      [value]       Number of bins in the histogram
  :z1         [value]       Minimum histogram intensity
  :z2         [value]       Maximum histogram intensity
  :top_closed [y/n]         Include z in the top bin?
  :x1         [value]       Left  world x-coord if not autoscaling
  :x2         [value]       Right world x-coord if not autoscaling
  :y1         [value]       Lower world y-coord if not autoscaling
  :y2         [value]       Upper world y-coord if not autoscaling
  :logy       [yes/no]      Log scale the y axis?
  :box        [yes/no]      Draw box around periphery of window?
  :ticklabels [yes/no]      Label tick marks?
  :majrx      [value]       Number of major divisions along x axis
  :minrx      [value]       Number of minor divisions along x axis
  :majry      [value]       Number of major divisions along y axis
  :minry      [value]       Number of minor divisions along y axis
  :round      [yes/no]      Round axes to nice values?
  :fill       [yes/no]      Fill viewport vs enforce unity aspect ratio?
  
          PEXAMINE Interactive Radial Profile Plotting Commands
  
  :rinner     [value]       Inner radius of the region to be plotted
  :router     [value]       Outer radius of the region to be plotted
  :x1         [value]       Left  world x-coord if not autoscaling
  :x2         [value]       Right world x-coord if not autoscaling
  :y1         [value]       Lower world y-coord if not autoscaling
  :y2         [value]       Upper world y-coord if not autoscaling
  :szmarker   [value]       Marker size
  :marker [point|box|plus|cross|circle|diamond|hline|vline]    Marker type
  :logx       [yes/no]      Log scale the x axis?
  :logy       [yes/no]      Log scale the y axis?
  :box        [yes/no]      Draw box around periphery of window?
  :ticklabels [yes/no]      Label tick marks?
  :grid       [yes/no]      Draw grid lines at major tick marks?
  :majrx      [value]       Number of major divisions along x axis
  :minrx      [value]       Number of minor divisions along x axis
  :majry      [value]       Number of major divisions along y axis
  :minry      [value]       Number of minor divisions along y axis
  :round      [yes/no]      Round axes to nice values?
  :fill       [yes/no]      Fill viewport vs enforce unity aspect ratio?
  
          PEXAMINE Interactive Surface Plotting Commands
  
  :ncolumns   [value]       Number of columns to be plotted
  :nlines     [value]       Number of lines to be plotted
  :axes       [yes/no]      Draw axes?
  :angh       [value]       Horizontal viewing angle
  :angv       [value]       Vertical viewing angle
  :floor      [value]       Minimum value to be plotted
  :ceiling    [value]       Maximum value to be plotted
  
          PEXAMINE Interactive Contour Plotting Commands
  
  :ncolumns   [value]       Number of columns to be plotted
  :nlines     [value]       Number of lines to be plotted
  :floor      [value]       Minimum value to be plotted
  :ceiling    [value]       Maximum value to be plotted
  :zero       [value]       Grayscale value of zero contour
  :ncontours  [value]       Number of contours to be drawn
  :interval   [value]       Contour interval
  :nhi        [value]       Hi/low marking option
  :dashpat    [value]       Bit pattern for generating dashed lines
  :label      [yes/no]      Label major contours with their values?
  :box        [yes/no]      Draw box around periphery of window?
  :ticklabels [yes/no]      Label tick marks?
  :majrx      [value]       Number of major divisions along x axis
  :minrx      [value]       Number of minor divisions along x axis
  :majry      [value]       Number of major divisions along y axis
  :minry      [value]       Number of minor divisions along y axis
  :round      [yes/no]      Round axes to nice values?
  :fill       [yes/no]      Fill viewport vs enforce unity aspect ratio?
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Examine and edit an APPHOT aperture photometry catalog and a DAOPHOT
  allstar catalog without either attaching the associated image or using the
  image display.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; pexamine ypix.mag.1 ypix.mag.ed use_display-
  
      ... a plot of magnitude error versus magnitude appears on
          the screen and the graphics cursor comes up ready to accept
          commands
  
      ... the user sees a generally smooth trend of increasing
          magnitude error with increasing magnitude except for a
          single deviant point at the bright end of the plot
  
      ... the user decides to remove the deviant point using the
          <span style="font-family: monospace;">'d'</span> keystroke command to mark the point and the <span style="font-family: monospace;">'f'</span>
          keystroke command to actually delete and replot the graph
  
      ... after examining the plot further the user decides to delete
          all objects for which the magnitude error is &gt; 0.1 magnitudes
          using the <span style="font-family: monospace;">'^'</span> keystroke command, followed by the <span style="font-family: monospace;">'f'</span>
          keystroke command to actually replot and delete the data.
  
      ... after deciding that this new plot is satisfactory the user
          issues the <span style="font-family: monospace;">'e'</span> keystroke command to exit pexamine and save
          the good data in m92.mag.ed
  
  pt&gt; pexamine ypix.als.1 ypix.als.ed use_display-
  
      ... a plot of magnitude error versus magnitude appears on the
          screen and the graphics cursor comes up ready to accept
          commands
  
      ... after looking at the plot the user decides that what they
          really want to see is a plot of the goodness of fit parameter
          chi versus magnitude
  
      ... the user issues the colon command :ycol chi followed by <span style="font-family: monospace;">'p'</span>
          keystroke command to replot the data
  
      ... the user sees a generally smooth trend of increasing
          chi with increasing magnitude
  
      ... after examining the plot further the user decides to delete
          all objects for which the chi value  &gt; 2.0  and the
          magnitude is &gt; 25 using the <span style="font-family: monospace;">'^'</span> key and <span style="font-family: monospace;">')'</span> keystroke
          commands followed by <span style="font-family: monospace;">'f'</span> to save the deletions and replot
          the data
  
      ... after deciding that this new plot is satisfactory the user
          issues the <span style="font-family: monospace;">'e'</span> keystroke command to exit pexamine and save
          the good data in m92.als.ed
  </pre></div>
  <p>
  2. Examine and edit a DAOPHOT allstar catalog using the subtracted image, the
  original image and the image display.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; display ypix.sub.1 1
  
      ... display the subtracted image
  
  pt&gt; pexamine ypix.als.1 ypix.als.ed dev$ypix xcol=mag ycol=chi
  
  ... a plot of the goodness of fit versus magnitude appears
      on the terminal and the graphics cursor comes up ready to
      accept commands
  
  ... the user notices some very anomalous chi values and decides
      to see if these correspond to objects which have poor
      subtraction on the displayed image
  
  ... the user switches to image command mode by tapping the <span style="font-family: monospace;">'i'</span>
      key, moves to the first poorly subtracted object and taps
      the <span style="font-family: monospace;">'o'</span> key
  
  ... a list of the values of the loaded columns including chi
      appears in the text window , the program switches to graphics
      mode and places the graphics cursor on the corresponding
      point in the X-Y plot
  
  ... the point in question indeed has a very high chi value
      and the user decides to try and investigate the reason for the
      anomalous value
  
  ... the user taps the <span style="font-family: monospace;">'r'</span> key to get a radial profile of the
      object in the original image
  
  ... after carefully examining the profile it appears that the
      object's profile is too broad and that it is not a star
  
  ... the user switches back to the X-Y plot with the <span style="font-family: monospace;">'x'</span> key,
      marks the point with the <span style="font-family: monospace;">'d'</span> key and saves the deletions
      and replots with the <span style="font-family: monospace;">'f'</span> key.
  
  ... the user goes back to image command mode with the <span style="font-family: monospace;">'i'</span> key
      and begins investigating the next object
  
  ... finally after examining the image and making all the changes
      the user decides to quit and save the changes with the <span style="font-family: monospace;">'e'</span> key
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  INDEF valued points cannot be accessed by PEXAMINE. INDEF valued points should
  be removed from the input catalog with PSELECT prior to entering PEXAMINE.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ptools.pselect, ptools.txselect,ptools.tselect
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'PLOTTING PARAMETERS' 'DESCRIPTION' 'COMMANDS' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

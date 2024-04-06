.. _graph:

graph: Graph one or more image sections or lists
================================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  graph input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of operands to be graphed.  May be STDIN, or one or more image sections 
  or lists.
  </dd>
  </dl>
  <dl id="l_wx1">
  <dt><b>wx1=0., wx2=0., wy1=0., wy2=0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wx1' Line='wx1=0., wx2=0., wy1=0., wy2=0.' -->
  <dd>The range of user coordinates spanned by the plot.  If the range of values
  in x or y = 0, the plot is automatically scaled from the minimum to
  maximum data value along the degenerate dimension.
  </dd>
  </dl>
  <dl id="l_wcs">
  <dt><b>wcs = <span style="font-family: monospace;">"logical"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcs' Line='wcs = "logical"' -->
  <dd>The world coordinate system (<i>wcs</i>) to be used for axis labeling when
  input is f rom images.
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
  In addition to these three reserved WCS names, the name of any user WCS
  defined for the reference image may be given.  A user world coordinate system
  may be any linear or nonlinear world system.
  </dd>
  </dl>
  <dl id="l_vx1">
  <dt><b>vx1=0., vx2=0., vy1=0., vy2=0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vx1' Line='vx1=0., vx2=0., vy1=0., vy2=0.' -->
  <dd>NDC coordinates (0-1) of the device plotting viewport.  If not set by 
  the user, a suitable viewport which allows sufficient room for all labels 
  is used.
  </dd>
  </dl>
  <dl id="l_pointmode">
  <dt><b>pointmode = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pointmode' Line='pointmode = no' -->
  <dd>If <b>pointmode</b> = yes, plot points or markers at data values, rather than 
  connected lines.
  </dd>
  </dl>
  <dl id="l_marker">
  <dt><b>marker = <span style="font-family: monospace;">"box"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='marker' Line='marker = "box"' -->
  <dd>Marker or line type to be drawn.  If <b>pointmode</b> = yes the markers are
  <span style="font-family: monospace;">"point"</span>, <span style="font-family: monospace;">"box"</span>, <span style="font-family: monospace;">"cross"</span>, <span style="font-family: monospace;">"plus"</span>, <span style="font-family: monospace;">"circle"</span>, <span style="font-family: monospace;">"hebar"</span>, <span style="font-family: monospace;">"vebar"</span>, <span style="font-family: monospace;">"hline"</span>,
  <span style="font-family: monospace;">"vline"</span> or <span style="font-family: monospace;">"diamond"</span>.  Any other value defaults to <span style="font-family: monospace;">"box"</span>.  If drawing lines,
  <b>pointmode</b> = no, the values are <span style="font-family: monospace;">"line"</span>, <span style="font-family: monospace;">"lhist"</span>, <span style="font-family: monospace;">"bhist"</span>.  Any other
  value defaults to <span style="font-family: monospace;">"line"</span>.  <span style="font-family: monospace;">"bhist"</span> (box histogram) draws lines to the
  bottom of the graph while <span style="font-family: monospace;">"lhist"</span> does not.  In both cases the
  horizontal histogram lines run between the half way points (reflected
  at the ends).
  </dd>
  </dl>
  <dl id="l_szmarker">
  <dt><b>szmarker = 0.005</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='szmarker' Line='szmarker = 0.005' -->
  <dd>The size of a marker in NDC coordinates (0 to 1 spans the screen).
  If zero and the input operand is a list, marker sizes are taken individually
  from the third column of each list element.  If positive, all markers are
  of size <b>szmarker</b>.  If negative and the input operand is a list,
  the size of a marker is the third column of each list element times the
  absolute value of <b>szmarker</b>.
  </dd>
  </dl>
  <dl id="l_ltypes">
  <dt><b>ltypes = <span style="font-family: monospace;">""</span>, colors = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ltypes' Line='ltypes = "", colors = ""' -->
  <dd>List of line types and colors to use when graphing multiple data sets.
  The lists are comma or space separate integer numbers.  If no list is
  given the line types and colors will cycle through the range of
  values.  If a list is given then the values are used in order and if
  the list is exhausted before the data the last value is used for all
  remaining data sets.
  The line types have values between 1 and 4:
  <div class="highlight-default-notranslate"><pre>
  1 - solid line
  2 - dashed line
  3 - dotted line
  4 - dot-dash line
  </pre></div>
  The colors have values between 1 and 9.  The colors associated with each
  number depend on the graphics device.  For example <span style="font-family: monospace;">"xgterm"</span> colors are
  assigned by X resources.
  </dd>
  </dl>
  <dl id="l_xlabel">
  <dt><b>xlabel = <span style="font-family: monospace;">"wcslabel"</span>, ylabel = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xlabel' Line='xlabel = "wcslabel", ylabel = ""' -->
  <dd>Label for the X-axis or Y-axis.  if <b>xlabel</b> = <span style="font-family: monospace;">"wcslabel"</span> and the first
  operand in the <b>input</b> is an image, the world coordinate system label
  if defined is used.
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">"imtitle"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = "imtitle"' -->
  <dd>Plot title.  If <b>title</b>  = <span style="font-family: monospace;">"imtitle"</span>
  and the first operand in <b>input</b> is an image, the image title is used
  as the plot title.
  </dd>
  </dl>
  <dl id="l_xformat">
  <dt><b>xformat = <span style="font-family: monospace;">"wcsformat"</span>, yformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xformat' Line='xformat = "wcsformat", yformat = ""' -->
  <dd>The numerical format for the coordinate labels.  The values may be <span style="font-family: monospace;">""</span>
  (an empty string), %f for decimal format, %h and %H for xx:xx:xx format, and
  %m and %M for xx:xx.x format.  The upper case %H and %M convert degrees
  to hours.  For images a recommended x coordinate format may be defined as
  a WCS attribute.  If the xformat value is <span style="font-family: monospace;">"wcsformat"</span> the WCS attribute
  format will be used.  Any other value will override the image attribute.
  </dd>
  </dl>
  <dl id="l_box">
  <dt><b>box = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='box' Line='box = yes' -->
  <dd>Draw axes at the perimeter of the plotting window.
  </dd>
  </dl>
  <dl id="l_fill">
  <dt><b>fill = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fill' Line='fill = yes' -->
  <dd>Fill the output viewport regardless of the device aspect ratio?
  </dd>
  </dl>
  <dl id="l_axis">
  <dt><b>axis = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='axis' Line='axis = 1' -->
  <dd>Axis along which the projection is to be computed, if an input operand is
  an image section of dimension 2 or higher.  Axis 1 is X (line average),
  2 is Y (column average), and so on.
  </dd>
  </dl>
  <dl id="l_transpose">
  <dt><b>transpose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='transpose' Line='transpose = no' -->
  <dd>Swap the X and Y axes of the plot.  If enabled, the axes are transposed 
  after the optional linear transformation of the X-axis.
  </dd>
  </dl>
  <dl id="l_logx">
  <dt><b>logx = no, logy = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logx' Line='logx = no, logy = no' -->
  <dd>Log scale the X or Y axis.  Zero or negative values are indefinite and
  will not be plotted, but are tolerated.
  </dd>
  </dl>
  <dl id="l_ticklabels">
  <dt><b>ticklabels = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ticklabels' Line='ticklabels = yes' -->
  <dd>Label the tick marks.
  </dd>
  </dl>
  <dl id="l_majrx">
  <dt><b>majrx=5, minrx=5, majry=5, minry=5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='majrx' Line='majrx=5, minrx=5, majry=5, minry=5' -->
  <dd>Number of major tick marks on each axis; number of minor tick marks between
  major tick marks.  Ignored if log scaling is in effect for an axis.
  </dd>
  </dl>
  <dl id="l_lintran">
  <dt><b>lintran = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lintran' Line='lintran = no' -->
  <dd>Perform a linear transformation of the X-axis upon input.  Used to assign
  logical coordinates to the indices of pixel data arrays (image sections).
  </dd>
  </dl>
  <dl id="l_p1">
  <dt><b>p1=0, p2=0, q1=0, q2=1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='p1' Line='p1=0, p2=0, q1=0, q2=1' -->
  <dd>If <b>lintran</b> is enabled, pixel index P1 is mapped to Q1, and P2 to Q2.
  If P1 and P2 are zero, P1 is set to 1 and P2 to the number of pixels in
  the input array.
  </dd>
  </dl>
  <dl id="l_round">
  <dt><b>round = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='round' Line='round = no' -->
  <dd>Extend the axes up to <span style="font-family: monospace;">"nice"</span> values.
  </dd>
  </dl>
  <dl id="l_overplot">
  <dt><b>overplot = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='overplot' Line='overplot = no' -->
  <dd>Overplot on an existing plot.  All axis scaling and labeling parameters
  apply.
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = no' -->
  <dd>Append to an existing plot.  The previous axis is used and the axis
  scaling and labeling parameters are ignored.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "stdgraph"' -->
  <dd>The output device.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Graph</b> graphs one or more lists or image sections; lists and image
  sections may be mixed in the input list at will.  If the curves are not
  all the same length the plot will be scaled to the longest curve and all
  curves will be plotted left justified.  If an image section operand has
  more than one dimension the projection (average) along a designated axis
  will be computed and plotted.  By default, a unique dash pattern is used
  for each curve, up to a maximum of 4.
  </p>
  <p>
  List input may be taken from the standard input or from a file,
  and consists of a sequence of Y values, X and Y values, or X, Y,
  and marker size values, one pair of coordinates per line in the list.
  If the third column of a list contains positive numbers, they are
  interpreted as NDC marker sizes, optionally scaled by the absolute
  value of <i>szmarker</i>.  If you want the third column of a list to
  be interpreted as WCS coordinates, indicating errors for example, the
  marker sizes should be entered as negative numbers.
  Blank lines, comment lines, and extra columns are ignored.
  The first element in the list determines whether the list is a Y list
  or and X,Y list; it is an error if an X,Y list has fewer than two
  coordinates in any element.  INDEF valued elements appear as gaps
  in the plot.
  </p>
  <p>
  If <b>append</b> is enabled, previous values for <b>box</b>,
  <b>fill</b>, <b>round</b>, the plotting viewport (<b>vx1</b>, <b>vx2</b>, 
  <b>vy1</b>, <b>vy2</b>), and the plotting window (<b>wx1</b>, <b>wx2</b>, 
  <b>wy1</b>, <b>wy2</b>) are used.  The <b>overplot</b> parameter overplots
  a new plot including any new axis scaling and labeling.
  </p>
  <p>
  By default, the plot drawn will fill the device viewport, if the viewport
  was either specified by the user or automatically calculated by 
  <i>graph</i>.  Setting
  the value of <b>fill</b>  to <span style="font-family: monospace;">"no"</span> means the viewport will be adjusted so 
  that equal numbers of data values in x and y will occupy equal lengths 
  when plotted.  That is, when <b>fill = no</b>, a unity aspect ratio is 
  enforced, and plots
  appear square regardless of the device aspect ratio.  On devices with non 
  square full device viewports (e.g., the vt640), a plot drawn by <i>graph</i>
  appears extended in the x direction unless <b>fill</b> = no.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Plot the output of a list processing filter:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ... list_filter | graph
  </pre></div>
  <p>
  2. Plot a graph entered interactively from the terminal:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; graph STDIN
  </pre></div>
  <p>
  3. Overplot two lists:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; graph list1,list2
  </pre></div>
  <p>
  4. Graph line 128 of image <span style="font-family: monospace;">"pix"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; graph pix[*,128]
  </pre></div>
  <p>
  5. Graph the average of columns 50 through 100:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; graph pix[50:100,*] axis=2
  </pre></div>
  <p>
  6. Graph a list in point plot mode:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; graph list po+
  </pre></div>
  <p>
  7. Annotate a graph:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; graph pix[*,10],pix[*,20] xlabel=column\
  &gt;&gt;&gt; ylabel=intensity title="lines 10 and 20 of pix"
  </pre></div>
  <p>
  8. Direct the graph to the standard plotter device:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; graph list device=stdplot
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Indefinites are not recognized when computing image projections.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  pcol, pcols, prow, prows
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  
System Documentation
--------------------

.. raw:: html

  <section id="s_description">
  <h3>Description</h3>
  <p>
  The `st4gem.graphics' package contains two subpackages of tasks for
  viewing one- and two-dimensional data.  These tasks are not necessarily
  specific to HST data.  They tasks are designed to make use of IRAF
  image formats (OIF, STF and QPOE), and ST4GEM binary tables.  A summary
  of the available packages is given in Table 1 below; a more detailed
  summary can be found in the following sections and the help for each
  package.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
              Table 1.  Graphics Packages
  +--------------------------------------------------------+
  | Package    | Description                               |
  +--------------------------------------------------------+
  | stplot     | General data plotting                     |
  +--------------------------------------------------------+
  
  </pre></div>
  <p>
  There currently remains some separation between the capabilities of
  displaying one-dimensional data (spectra) and two-dimensional data
  (bit-mapped raster images).  In the past, hardware and software
  limitations enforced a rather strict distinction between vector
  graphics and image display.  This distinction is, however,  becoming fuzzier.
  It is possible to draw any vector graphics to the image
  display (using an <span style="font-family: monospace;">"imd"</span> device and SAOimage).  It is also becoming
  possible to draw gray-scale and color images to some vector graphics
  <span style="font-family: monospace;">"devices"</span> (with the PostScript kernel, for example).  Some tasks
  in the 'stplot' package take advantage of this.
  </p>
  </section>
  <section id="s_general_data_plotting">
  <h3>General data plotting</h3>
  <p>
  Tasks in the 'stplot' package support drawing graphs from IRAF data.
  Several tasks also recognize ST4GEM binary tables in addition to the
  various IRAF image formats.
  </p>
  <p>
  The two generic tasks 'igi' and 'sgraph' draw graphs from any recognized
  IRAF data format. (A detailed <span style="font-family: monospace;">"IGI Reference Manual"</span> is available from
  the ST4GEM group by sending e-mail requests to: hotseat@stsci.edu).
  </p>
  <p>
  Other tasks provide more specific capabilities such as contour plots,
  labeling of 2-D images with linear or celestial coordinates, drawing
  vector fields and histograms.  The one task specific to HST is 'siaper',
  which draws the science apertures at the telescope's focal plane at
  arbitrary scale and rotation.
  </p>
  <p>
  The 'psikern' GIO kernel allows any IRAF task that produces graphics to
  fully exploit PostScript capabilities, whether printed directly
  to a PostScript printer, saved as encapsulated PostScript (EPS) and
  imported into a document, or rendered on a workstation using a
  PostScript viewer.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  sdisplay, stplot, vdisplay, tv, tv.display
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'DESCRIPTION' 'GENERAL DATA PLOTTING' 'SEE ALSO'  -->
  

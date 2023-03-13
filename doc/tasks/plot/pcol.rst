.. _pcol:

pcol: Plot a column of an image
===============================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pcol image col
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Input image containing column to be plotted.
  </dd>
  </dl>
  <dl id="l_col">
  <dt><b>col      </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='col' Line='col      ' -->
  <dd>The column to be plotted.
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
  </dd>
  </dl>
  <dl id="l_wx1">
  <dt><b>wx1=0., wx2=0., wy1=0., wy2=0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wx1' Line='wx1=0., wx2=0., wy1=0., wy2=0.' -->
  <dd>The range of window (user) coordinates to be included in the plot.  If
  the range of values in x or y = 0, the plot is automatically scaled
  from the minimum to maximum data values along the degenerate axis.
  </dd>
  </dl>
  <dl id="l_vx1">
  <dt><b>vx1=0., vx2=0., vy1=0., vy2=0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vx1' Line='vx1=0., vx2=0., vy1=0., vy2=0.' -->
  <dd>NDC coordinates (0-1) of the device plotting viewport.  If not set by
  user, a suitable viewport which allows sufficient room for all labels
  is used.
  </dd>
  </dl>
  <dl id="l_pointmode">
  <dt><b>pointmode = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pointmode' Line='pointmode = no' -->
  <dd>Plot individual points instead of a line?
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
  <dd>The size of the marker drawn when <b>pointmode</b> = yes.
  </dd>
  </dl>
  <dl id="l_logx">
  <dt><b>logx = no, logy = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logx' Line='logx = no, logy = no' -->
  <dd>Draw the x or y axis in log units, versus linear?
  </dd>
  </dl>
  <dl id="l_xlabel">
  <dt><b>xlabel = <span style="font-family: monospace;">"wcslabel"</span>, ylabel = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xlabel' Line='xlabel = "wcslabel", ylabel = ""' -->
  <dd>Label for the X-axis or Y-axis.  if <b>xlabel</b> = <span style="font-family: monospace;">"wcslabel"</span>
  the world coordinate system label in the image, if defined, is used.
  </dd>
  </dl>
  <dl id="l_xformat">
  <dt><b>xformat = <span style="font-family: monospace;">"wcsformat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xformat' Line='xformat = "wcsformat"' -->
  <dd>The numerical format for the coordinate labels.  The values may be <span style="font-family: monospace;">""</span>
  (an empty string), %f for decimal format, %h and %H for xx:xx:xx format, and
  %m and %M for xx:xx.x format.  The upper case %H and %M convert degrees
  to hours.  Some images have a recommended x coordinate format defined as
  a WCS attribute.  If the xformat value is <span style="font-family: monospace;">"wcsformat"</span> the WCS attribute
  format will be used.  Any other value will override the image attribute.
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">"imtitle"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = "imtitle"' -->
  <dd>Title for plot.  If not changed from the default, the title string from the
  image header, appended with the columns being plotted, is used.
  </dd>
  </dl>
  <dl id="l_majrx">
  <dt><b>majrx=5, minrx=5, majry=5, minry=5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='majrx' Line='majrx=5, minrx=5, majry=5, minry=5' -->
  <dd>The number of major and minor divisions along the x or y axis.
  </dd>
  </dl>
  <dl id="l_round">
  <dt><b>round = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='round' Line='round = no' -->
  <dd>Round axes up to nice values?
  </dd>
  </dl>
  <dl id="l_fill">
  <dt><b>fill = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fill' Line='fill = yes' -->
  <dd>Fill plotting viewport regardless of device aspect ratio?
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = no' -->
  <dd>Append to an existing plot?
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device=<span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device="stdgraph"' -->
  <dd>Output device.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Plot a specified column of an image.  The user can control the
  plot size and placement, the scaling and labeling of axes.  The column can be
  plotted as a continuous line or individual points with a specified marker.
  </p>
  <p>
  If <b>append</b> is enabled, previous values for <b>box</b>,
  <b>fill</b>, <b>round</b>, the plotting viewport (<b>vx1</b>, <b>vx2</b>, 
  <b>vy1</b>, <b>vy2</b>), and the plotting window (<b>wx1</b>, <b>wx2</b>, 
  <b>wy1</b>, <b>wy2</b>) are used.
  </p>
  <p>
  If the plotting viewport was not set by the user, <b>pcol</b> 
  automatically sets a viewport centered on the device.  The default value
  of <b>fill</b> = yes means the plot spans equal amounts of NDC space in
  x and y.  Setting
  the value of <b>fill</b>  to <span style="font-family: monospace;">"no"</span> means the viewport will be adjusted so 
  that the square plot will span equal physical lengths in x and y
  when plotted.  That is, when <b>fill = no</b>, a unity aspect ratio is 
  enforced, and plots
  appear square regardless of the device aspect ratio.  On devices with non 
  square full device viewports (e.g., the vt640), a plot drawn by <i>pcol</i>
  appears extended in the x direction unless <b>fill</b> = no.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Plot column 128 of image crab.5009 with default parameters:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; pcol crab.5009 128
  </pre></div>
  <p>
  2. Overplot column 128 of crab.red using boxes to mark the added points:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; pcol crab.red 128 append+ pointmode+
  </pre></div>
  <p>
  3. Annotate the axes of a column plot:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; pcol crab.5009 64 xlabel="Row Number" ylabel=Intensity
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  <b>pcol</b> requires about 1.6 cp seconds to plot a column of a 512 square
  image.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  prow, prows, pcols
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

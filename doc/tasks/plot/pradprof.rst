.. _pradprof:

pradprof: Plot or list the radial profile of a stellar object
=============================================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pradprof input xinit yinit
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of images containing the object of interest.
  </dd>
  </dl>
  <dl id="l_xinit">
  <dt><b>xinit, yinit</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xinit' Line='xinit, yinit' -->
  <dd>The initial guess for the  x and y coordinates of the object whose
  profile is to be computed.  If <i>center</i>
  is yes, <i>xinit</i> and <i>yinit</i> are the initial input to the centering 
  algorithm, otherwise <i>xinit</i> and <i>yinit</i> are passed directly to the
  radial profiling algorithm.
  </dd>
  </dl>
  <dl id="l_radius">
  <dt><b>radius = 11</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radius' Line='radius = 11' -->
  <dd>The plotting radius in pixels.
  </dd>
  </dl>
  <dl id="l_az1">
  <dt><b>az1 = 0., az2 = 360.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='az1' Line='az1 = 0., az2 = 360.' -->
  <dd>Azimuth limits for the profile points in degrees.  The azimuth is
  measured from the x or first image axis towards the y or second image
  axis.  Negative azimuths are allowed as are any multiples of 360.
  </dd>
  </dl>
  <dl id="l_center">
  <dt><b>center = yes </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='center' Line='center = yes ' -->
  <dd>Center the initial coordinates before computing the profile?
  </dd>
  </dl>
  <dl id="l_cboxsize">
  <dt><b>cboxsize = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cboxsize' Line='cboxsize = 5' -->
  <dd>The size of the extraction box of pixels to be used by the centering
  algorithm.
  </dd>
  </dl>
  <dl id="l_list">
  <dt><b>list = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='list' Line='list = no' -->
  <dd>Make a list of the radial profile, instead of a plot?
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>The graphics device for plotting.
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = no' -->
  <dd>Append to an existing plot?
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">"imtitle"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = "imtitle"' -->
  <dd>The plot title. If title = <span style="font-family: monospace;">"imtitle"</span>, the image name, <i>xinit</i>, and
  <i>yinit</i> are
  used to construct a default title, otherwise the user specified title is
  used.
  </dd>
  </dl>
  <dl id="l_xlabel">
  <dt><b>xlabel = <span style="font-family: monospace;">"Radius"</span>, ylabel = <span style="font-family: monospace;">"Intensity"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xlabel' Line='xlabel = "Radius", ylabel = "Intensity"' -->
  <dd>The default labels for the X and Y axes.
  </dd>
  </dl>
  <dl id="l_wx1">
  <dt><b>wx1 = INDEF, wx2 = INDEF, wy1 = INDEF, wy2 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wx1' Line='wx1 = INDEF, wx2 = INDEF, wy1 = INDEF, wy2 = INDEF' -->
  <dd>The range of user coordinates spanned by the plot. By default the data is
  used to determine the range.
  </dd>
  </dl>
  <dl id="l_logx">
  <dt><b>logx = no, logy = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logx' Line='logx = no, logy = yes' -->
  <dd>Use log scaling on the x or y axes of the plot?
  </dd>
  </dl>
  <dl id="l_round">
  <dt><b>round = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='round' Line='round = no' -->
  <dd>Round the axes minimum and maximum values up to <span style="font-family: monospace;">"nice"</span> values?
  </dd>
  </dl>
  <dl id="l_box">
  <dt><b>box = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='box' Line='box = yes' -->
  <dd>Draw axes at the perimeter of the plotting window?
  </dd>
  </dl>
  <dl id="l_majrx">
  <dt><b>majrx = 5, minrx = 5, majry = 5, minry = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='majrx' Line='majrx = 5, minrx = 5, majry = 5, minry = 5' -->
  <dd>Number of major tick marks on each axis and number of minor tick marks between
  major tick marks. These quantities are ignored if log scaling is in effect
  for an axis.
  </dd>
  </dl>
  <dl id="l_ticklabels">
  <dt><b>ticklabels = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ticklabels' Line='ticklabels = yes' -->
  <dd>Label the tick marks?
  </dd>
  </dl>
  <dl id="l_fill">
  <dt><b>fill = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fill' Line='fill = yes' -->
  <dd>Fill the output viewport regardless of the device aspect ratio ?
  </dd>
  </dl>
  <dl id="l_vx1">
  <dt><b>vx1 = 0.0, vx2 = 1.0, vy1 = 0.0, vy2 = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vx1' Line='vx1 = 0.0, vx2 = 1.0, vy1 = 0.0, vy2 = 1.0' -->
  <dd>The NDC coordinates (0.0:1.0) of the device plotting viewport.
  </dd>
  </dl>
  <dl id="l_pointmode">
  <dt><b>pointmode = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pointmode' Line='pointmode = yes' -->
  <dd>Plot points instead of lines?
  </dd>
  </dl>
  <dl id="l_marker">
  <dt><b>marker = <span style="font-family: monospace;">"plus"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='marker' Line='marker = "plus"' -->
  <dd>Type of marker used in pointmode.
  </dd>
  </dl>
  <dl id="l_szmarker">
  <dt><b>szmarker = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='szmarker' Line='szmarker = 1.' -->
  <dd>Size of markers used in pointmode.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  PRADPROF computes a radial profile of length <i>radius</i> pixels
  with a range of azimuths (<i>az1</i> to <i>az2</i>),
  for the object near (<i>xinit</i>, <i>yinit</i>) in the input image(s) 
  <i>input</i>, and plots it on the graphics device <i>graphics</i>.
  If the parameter <i>center</i> is
  <span style="font-family: monospace;">"yes"</span>, then pixels in a box <i>cboxwidth</i> wide around the initial
  coordinates and a simple centroiding algorithm  are used to
  compute a more accurate center, before the radial profile is computed.
  </p>
  <p>
  The azimuths are measured from the first image axis towards the second
  image axis.  The limits may be given in any multiple of 360 degrees
  including negative azimuths.
  </p>
  <p>
  If the parameter
  <i>append</i> is yes then the new plot will be appended to an existing plot,
  otherwise the device is cleared and a new plot is made. The
  remainder of the parameters control the details of how
  the plot is displayed. If the parameter <b>list</b> is <span style="font-family: monospace;">"yes"</span> 
  the radial profile is listed on the standard output instead of plotted.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Plot the radial profile of a star near (123, 234).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; pradprof m92red 123 234
  </pre></div>
  <p>
  2. Plot the profile around (123, 234) with centering turned off.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; pradprof m92red 123 234 center=no
  </pre></div>
  <p>
  3. List the radial profile and redirect it to a file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; pradprof m92red 123 234 list=yes &gt; profile
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  proto.imcntr, imexamine
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

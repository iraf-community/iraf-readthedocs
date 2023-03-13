.. _fitcoords:

fitcoords: Fit user coordinates to image coordinates
====================================================

**Package: longslit**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fitcoords images fitname
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images containing the feature coordinates to be fit.  If the
  parameter <i>combine</i> is yes then feature coordinates from all the images
  are combined and fit by a single function.  Otherwise the feature coordinates
  from each image are fit separately.
  </dd>
  </dl>
  <dl id="l_fitname">
  <dt><b>fitname = <span style="font-family: monospace;">""</span> </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitname' Line='fitname = "" ' -->
  <dd>If the input images are combined and fit by a single function then the fit
  is stored under this name.  If the images are not combined then the
  fit for each image is stored under the name formed by appending the image
  name to this name.  A null prefix is acceptable when not combining but it
  is an error if combining a list of images.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Determine coordinate fits interactively?
  </dd>
  </dl>
  <dl id="l_combine">
  <dt><b>combine = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='combine' Line='combine = no' -->
  <dd>Combine the coordinates from all the input images and fit them by a single
  function?  If 'no' then fit the coordinates from each image separately.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"database"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "database"' -->
  <dd>Database containing the feature coordinate information used in fitting the
  coordinates and in which the coordinate fit is recorded.
  </dd>
  </dl>
  <dl id="l_deletions">
  <dt><b>deletions = <span style="font-family: monospace;">"deletions.db"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='deletions' Line='deletions = "deletions.db"' -->
  <dd>Deletion list file.  If not null then points whose coordinates match those in
  this file (if it exists) are initially deleted from the fit.
  If the fitting is done interactively then the coordinates of
  any deleted points (after exiting from the interactive fitting) are recorded
  in this file.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"chebyshev"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "chebyshev"' -->
  <dd>Type of two dimensional function to use in fitting the user coordinates.
  The choices are <span style="font-family: monospace;">"chebyshev"</span> polynomial and <span style="font-family: monospace;">"legendre"</span> polynomial.
  The function may be abbreviated.  If the task is interactive then
  the user may change the function later.
  </dd>
  </dl>
  <dl id="l_xorder">
  <dt><b>xorder = 6</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xorder' Line='xorder = 6' -->
  <dd>Order of the mapping function along the first image axis.
  The order is the number of polynomial terms.  If the task is interactive
  then the user may change the order later.
  </dd>
  </dl>
  <dl id="l_yorder">
  <dt><b>yorder = 6</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='yorder' Line='yorder = 6' -->
  <dd>Order of the mapping function along the second image axis.
  The order is the number of polynomial terms.  If the task is interactive
  then the user may change the order later.
  </dd>
  </dl>
  <dl id="l_logfiles">
  <dt><b>logfiles = <span style="font-family: monospace;">"STDOUT,logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfiles' Line='logfiles = "STDOUT,logfile"' -->
  <dd>List of files in which to keep logs containing information about
  the coordinate fit.  If null then no log is kept.
  </dd>
  </dl>
  <dl id="l_plotfile">
  <dt><b>plotfile = <span style="font-family: monospace;">"plotfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotfile' Line='plotfile = "plotfile"' -->
  <dd>Name of file to contain metacode for log plots.  If null then no log plots
  are kept.  When the fitting is interactive the last graph is recorded in
  the plot file and when not interactive a default plot is recorded.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Graphics output device.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input.  If null the standard graphics cursor is used.
  </dd>
  </dl>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <div class="highlight-default-notranslate"><pre>
  ?  List commands
  c  Print data values for point nearest the cursor
  d  Delete the point or set of points with constant x, y, or z
          nearest the cursor (p, x, y, z,)
  f  Fit surface
  l  Graph the last set of points (in zoom mode)
  n  Graph the next set of points (in zoom mode)
  p  Graph all features
  q  Quit
  r  Redraw a graph
  u  Undelete the point or set of points with constant x, y, or z
          nearest the cursor (p, x, y, z,)
  w  Window the graph.  Type <span style="font-family: monospace;">'?'</span> to the "window:" prompt for more help.
  x  Select data for the x axis (x, y, z, s, r)
  y  Select data for the y axis (x, y, z, s, r)
  z  Zoom on the set of points with constant x, y, or z (x, y, z)
     Unzoom with p
  
  :corners        Show the fitted values for the corners of the image
  :function type  Set the function for the fitted surface
                  (chebyshev, legendre)
  :show           Show the fitting parameters
  :xorder value   Set the x order  for the fitted surface
  :yorder value   Set the y order  for the fitted surface
  </pre></div>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A two dimensional function of the image coordinates is fitted to the user
  coordinates from the specified images;
  </p>
  <div class="highlight-default-notranslate"><pre>
  user coordinate = function (column, line)
  
                  or
  
                z = s (x, y)
  </pre></div>
  <p>
  The coordinates from all the input images may be combined in a single fit or
  the coordinates from each image may be fit separately.  If the
  coordinates from the input images are combined then the fitted function
  is recorded in the database under the specified name.  If
  the coordinates are fit separately the fitted function is recorded under
  a name formed by appending the image name to the specified root name.
  </p>
  <p>
  When the task is interactive the user is first queried whether to perform
  the fitting interactively.  The user may answer <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"YES"</span>, or <span style="font-family: monospace;">"NO"</span>
  to the query.  The lowercase responses apply only to the current fit
  and the uppercase responses apply to all remaining fits.  When the
  fitting is done interactively the user may change the fitted function and
  orders iteratively, delete individual coordinates or entire features,
  and graph the fit and residuals in a number ways.
  The CURSOR COMMANDS section describes the graphics cursor keystrokes
  which are available.  When selecting data for the graph axes the
  follow definitions apply:
  </p>
  <div class="highlight-default-notranslate"><pre>
  x       Input image column positions
  y       Input image line positions
  z       Input user coordinates
  s       Fitted user coordinates
  r       Residuals (s - z)
  </pre></div>
  <p>
  A very useful feature is zooming, deleting, or undeleting a subset of data
  points.  The subsets
  are defined as points with the same x, y, or z value as the point indicated
  by the cursor when typing (z)oom, (d)elete, or (u)ndelete.
  </p>
  <p>
  When a satisfactory coordinate fit has been determined exit with the (q)uit
  key.  The user is asked if the fit is to be recorded in the database.
  </p>
  <p>
  If a deletion list file is specified then the coordinates of any
  points deleted interactively are recorded in this file.  This file then can
  be read by subsequent fits to initially delete points with matching
  coordinates.  This is generally used when fitting a series of images
  non-interactively.
  </p>
  <p>
  Information about the fitted function may be recorded.  Textual information
  is written to the specified log files (which may include the standard
  output STDOUT).  The last interactive plot or a default non-interactive
  plot is written the specified plot file which may be examined and spooled
  at a later time.
  </p>
  <p>
  FITCOORDS DATABASE
  </p>
  <p>
  The FITCOORDS fits are stored in text files in the subdirectory given by
  the <span style="font-family: monospace;">"database"</span> parameter.  The name of the file is fc&lt;fitname&gt; where
  &lt;fitname&gt; is the specified fit name.  The database text file contains
  blocks of lines beginning with a time stamp followed by line with the
  <span style="font-family: monospace;">"begin"</span> keyword.  The value following <span style="font-family: monospace;">"begin"</span> is the fit name, which is
  often the name of the image used for the fit.  If there is more than one
  block with the same fit name then the last one is used.
  </p>
  <p>
  The <span style="font-family: monospace;">"task"</span> keyword will has the value <span style="font-family: monospace;">"fitcoords"</span> and the <span style="font-family: monospace;">"axis"</span> keyword
  identifies the axis to which the surface fit applies.  An axis of 1 refers
  to the first or x axis (the first dimension of the image) and 2 refers to
  the second or y axis.
  </p>
  <p>
  The <span style="font-family: monospace;">"surface"</span> keyword specifies the number of coefficients for the surface
  fit given in the following lines .  The surface fit is produced by an IRAF
  math package called <span style="font-family: monospace;">"gsurfit"</span>.  The coefficients recorded in the database
  are intented to be internal to that package.  However the following
  describes how to interpret the coefficients.
  </p>
  <p>
  The first 8 lines specify:
  </p>
  <div class="highlight-default-notranslate"><pre>
  function - Function type (1=chebyshev, 2=legendre)
    xorder - X "order" (highest power of x)
    yorder - Y "order" (highest power of y)
    xterms - Cross-term type (always 1 for FITCOORDS)
      xmin - Minimum x over which the fit is defined
      xmax - Maximum x over which the fit is defined
      ymin - Minimum y over which the fit is defined
      ymax - Maximum y over which the fit is defined
  </pre></div>
  <p>
  The polynomial coefficients follow in array order with the x index
  varying fastest:
  </p>
  <div class="highlight-default-notranslate"><pre>
  C00
  C10
  C20
  ...
  C&lt;xorder-1&gt;0
  C01
  C11
  C21
  ...
  C&lt;xorder-1&gt;1
  ...
  C&lt;xorder-1&gt;&lt;yorder-1&gt;
  </pre></div>
  <p>
  The surface fitting functions have the form
  </p>
  <div class="highlight-default-notranslate"><pre>
  fit(x,y) = Cmn * Pmn
  </pre></div>
  <p>
  where the Cmn are the coefficients of the polynomials terms Pmn, and the Pmn
  are defined as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  Chebyshev: Pmn = Pm(xnorm) * Pn(ynorm)
  
             xnorm = (2 * x - (xmax + xmin)) / (xmax - xmin)
             ynorm = (2 * y - (ymax + ymin)) / (ymax - ymin)
  
             P0(xnorm) = 1.0
             P1(xnorm) = xnorm
             Pm+1(xnorm) = 2.0 * xnorm * Pm(xnorm) - Pm-1(xnorm)
  
             P0(ynorm) = 1.0
             P1(ynorm) = ynorm
             Pn+1(ynorm) = 2.0 * ynorm * Pn(ynorm) - Pn-1(ynorm)
  
  Legendre:  Pmn = Pm(xnorm) * Pn(ynorm)
  
             xnorm = (2 * x - (xmax + xmin)) / (xmax - xmin)
             ynorm = (2 * y - (ymax + ymin)) / (ymax - ymin)
  
             P0(xnorm) = 1.0
             P1(xnorm) = xnorm
             Pm+1(xnorm) = ((2m+1)*xnorm*Pm(xnorm)-m*Pm-1(xnorm))/(m+1)
  
             P0(ynorm) = 1.0
             P1(ynorm) = ynorm
             Pn+1(ynorm) = ((2n+1)*ynorm*Pn(ynorm)-n*Pn-1(ynorm))/(n+1)
  </pre></div>
  <p>
  Notice that the x and y values are first normalized to the interval -1 to 1
  over the range of the surface as given by the xmin, xmax, ymin, and ymax
  elements of the database description.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  A number of strong arc lines are identified along one column of an arc
  calibration image <span style="font-family: monospace;">"arc001"</span>.  The arc lines are then reidentified at every
  20th column.  A two dimensional dispersion solution is determined as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fitcoords arc001 fit.
  </pre></div>
  <p>
  The fitting is done interactively and deleted points are recorded.
  The fit is recorded under the name fit.arc001.  A set of similar arc
  calibrations are fit non-interactively, with the same points deleted,
  as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fitcoords arc* interactive=no
  </pre></div>
  <p>
  Several stellar spectra are identified at different positions along the slit
  and traced to other lines.  A fit to the geometric distortion is determined
  with the command:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fitcoords star001,star003,star005 fitname=distortion combine=yes
  </pre></div>
  <p>
  In this case the coordinates from all the tracings are combined in a single
  fit called distortion.
  </p>
  <p>
  The plots in the plot file are spooled to the standard plotting device as
  follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gkimosaic plotfile
  </pre></div>
  <p>
  <b>Gkimosaic</b> is in the <b>plot</b> package.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  transform
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'CURSOR COMMANDS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

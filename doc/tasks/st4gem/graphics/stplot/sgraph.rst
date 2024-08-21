.. _sgraph:

sgraph: Graph one or more image sections or lists.
==================================================

**Package: stplot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  sgraph input
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task will graph one or more lists, image sections, table columns or
  array elements from tables with arrays for elements of a column.
  Lists (text files) and image sections can be mixed in the 'input'
  parameter.  If the curves are of different lengths, the plot will be
  scaled to the longest curve and curves will be left justified.  If an
  image section has more than one dimension, the average projection will
  be computed and plotted along a designated axis.  A unique dash pattern
  (up to 4) is used for each curve (by default).
  </p>
  <p>
  Text can be interactively entered from the terminal keyboard, or it can
  come from a file; text input consists of a sequence of Y values, X and
  Y values, or X, Y, and marker size values.  One pair of coordinates can
  be entered on each input line.  Blank lines, comment lines, and extra
  columns are ignored.  The first element in the list determines whether
  the list is a Y list or an X,Y list. An error occurs if an X,Y list has
  less than two coordinates.  'INDEF' values appear as gaps in the plot.
  </p>
  <p>
  STSDAS and FITS tables can be used as input; they must be specified by
  a table name and column name, a table and two columns, or a pair of
  table and column names.  The table name may be a file name template.
  Tables can have arrays as elements of a column.  In
  order to plot these arrays, a row selector must be added to the
  filename to specify which row should be chosen for plotting.  The
  arrays to be plotted would then be pulled from the column specified
  but only from the row given in the row selector.  This imposes a limit
  in that only one row can be selected in the row selector, however, you
  can always specify a pair of table and column names, with each table name
  having a different row specified in the selector.  The syntax of the row
  selectors can be found using <span style="font-family: monospace;">"help selectors"</span> in the 'TABLES' package.
  </p>
  <dl id="l_Plot">
  <dt><b>Plot attributes -- the 'pltpar' pset</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Plot' Line='Plot attributes -- the 'pltpar' pset' -->
  <dd>Plot attributes are defined in the 'pltpar' parameter set (pset).
  These parameters can be modified by using the 'pltpar' command, by
  editing the pset from within 'eparam', or by assigning values from the
  command line.  If you are using the 'eparam sgraph' command to edit
  'sgraph' parameters, only the 'pltpar' pset name appears in the
  parameter list.  Typing <span style="font-family: monospace;">":e"</span> on the 'pltpar' line will bring up the
  'pltpar' parameters for modification; from within this screen, press
  CTRL-Z to return to the 'sgraph' parameter screen.  (For more
  information on modifying 'pltpar' parameters, type <span style="font-family: monospace;">"help pltpar"</span>).
  Parameter sets can be saved for future use; type <span style="font-family: monospace;">":w  &lt;name&gt;"</span> from
  within the 'eparam' screen to save the parameters (<span style="font-family: monospace;">"&lt;name&gt;"</span> is the name
  of the file in which parameters are to be saved).
  </dd>
  </dl>
  <dl id="l_Error">
  <dt><b>Error Bars</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Error' Line='Error Bars' -->
  <dd>There are several ways to draw error bars using 'sgraph'.  Errors can be
  the same size for each data point or variable, different for each data
  point.  In the latter case, they also may be asymmetric.  That is,
  the upper and lower error may differ.  Variable error values may be
  specified from a list (ASCII text) file or STSDAS (binary or text)
  table.
  Note that you need to run 'sgraph' more than once to draw a curve or
  symbols as well as error bars.  The 'sgraph' parameter 'append' should be
  set to <span style="font-family: monospace;">"yes"</span> on the second and subsequent executions.
  In all cases, the input error values specify the width of a single side
  of an error bar, interpreted as a <span style="font-family: monospace;">"sigma"</span> value, as in value +/- error.
  So the full size of the plotted error bar is twice the specified width
  for symmetrical errors in plotted user coordinates or the sum of the
  errors for asymmetric errors.
  Constant error bars are specified using the 'pointmode', 'marker', and
  'szmarker' parameters in the 'pltpar' pset.  For example, the following
  relevant parameter values will specify drawing vertical (in the Y
  direction) error bars of three units amplitude.
  <div class="highlight-default-notranslate"><pre>
  
  pltpar.pointmode = yes
  pltpar.marker = "vebar"
  pltpar.szmarker = -3
  
  </pre></div>
  That is, Y value + or - 3.  Note that the marker size is specified as
  negative, to distinguish the WCS value from NDC.  Positive marker sizes
  refer to a fraction of the display size rather than the scaled plot
  coordinates.
  Variable size error bars must have error values input from a list or
  table.  In both cases, one or two additional values per data point must
  be specified.  The normal X and Y or simply Y values specify the
  coordinate of the error bar and the additional value or values specify
  its size.  In addition, 'pltpar.pointmode' is turned off, and
  'pltpar.erraxis' must be set to 1 for horizontal error bars (parallel to
  the X direction) or 2 for vertical error bars (parallel to the Y
  direction).  You may select an error bar style in the 'pltpar.errtype'
  parameter:
  <div class="highlight-default-notranslate"><pre>
  
  "bartck"  traditional error bars, a line with a
            perpendicular tick at each end.
  "bar"     The bar only, no ticks.
  "tick"    The ticks only, no bar.
  "limit"   Arrows representing upper or lower limits, pointing
            away from the data coordinate.
  
  </pre></div>
  If the input data coordinates are in a list file, then the error values
  are in additional columns of the same file, in a third column or a
  third and fourth column.  If there are three columns in the file, the
  first two are X and Y coordinates and the third is the error value (half
  size of the error bar). If there are four columns, the first two are
  the X and Y coordinate, the third is the lower error (-X or -Y
  direction) and the last column is the upper error (+X or +Y
  direction). Note that because of the ambiguity it is not possible to
  specify only Y values to be plotted against element number with error
  values.  However, if you are not plotting error bars ('erraxis=0'), a
  single column indicates plotting Y values against element number.
  For example, the following relevant parameters will plot vertical error
  bars from data in the file <span style="font-family: monospace;">"ebt3.dat"</span> appended to an existing plot:
  <div class="highlight-default-notranslate"><pre>
  
  sgraph.input = "ebt3.dat"
  dvpar.device = "stdgraph"
  dvpar.append = yes
  sgraph.pltpar = ""
  pltpar.pointmode = no
  pltpar.erraxis = 2
  pltpar.errtype = "bartck"
  
  </pre></div>
  If the input data coordinates are in a table, the error values must be
  in the same table.  The column name or names are specified in the
  'pltpar.errcolumn' parameter.  If this string parameter is a single word
  (no spaces) then it must be the name of a single column whose values
  are interpreted as the half-size of symmetrical error bars.  If there
  two words, they specify the names of two columns whose values are
  interpreted as the lower and upper errors, respectively.
  For example, the following relevant parameters will plot horizontal
  limit symbols from X and Y data in columns <span style="font-family: monospace;">"a"</span> and <span style="font-family: monospace;">"b"</span> and error values
  in columns <span style="font-family: monospace;">"c"</span> and <span style="font-family: monospace;">"d"</span> in the table <span style="font-family: monospace;">"ebt4.tab"</span> appended to an existing
  plot:
  <div class="highlight-default-notranslate"><pre>
  
  sgraph.input = "ebt4 a b"
  dvpar.device = "stdgraph"
  dvpar.append = yes
  sgraph.pltpar = ""
  pltpar.pointmode = no
  pltpar.erraxis = 1
  sgraph.errcolumn = "c d"
  pltpar.errtype = "limit"
  
  </pre></div>
  Note that data plotted as points or a curve need not come from the same
  file or format as the errors since they are overplotted in separate
  executions of 'sgraph'.  However, the coordinates of the error bars
  themselves must be in the same file as the error values.
  </dd>
  </dl>
  <p>
  Different line and curve styles can be selected.  Line styles are
  specified with the 'pattern' parameter, curve styles with the
  'crvstyle' parameter.  The value passed to 'pattern' will designate a
  style for the first line drawn; subsequent lines will alternate among
  the styles.
  </p>
  <p>
  If 'append=yes', previous values for the 'box', 'fill', 'round', and
  viewport ('vx1' through 'vy2')  and window ('wx1' through 'wy2') 
  parameters are used.
  </p>
  <p>
  Plots will fill the output device's viewport unless a viewport is
  specified by the user or calculated by 'sgraph'.  Setting 'fill = no'
  will cause the viewport to be adjusted so that the X and Y scales
  match;  plots will appear square regardless of the device's aspect
  ratio.  On devices with a non-square device viewport (e.g., the
  vt640), a plot drawn by 'sgraph' will appear extended in the X 
  dimension unless 'fill = no'.
  </p>
  <dl id="l_Color">
  <dt><b>Color</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Color' Line='Color' -->
  <dd>The 'sgraph' task can plot in color, as long as you use the appropriate
  device and graphics kernel (driver).  You may specify the color of the
  plotted curve or curves separately from the color of the axes and
  labels.  Use the 'crvcolor' parameter to specify the curve color and the
  'color' parameter to specify the color of everything else.  In addition,
  if you plot several curves on the same viewport (set of axes), each
  curve may automatically plot in one of eight different colors,
  analagous to plotting curves using different line styles.  Use the
  'cycolor' parameter to select this option.
  Currently, only the PostScript kernel 'psikern' plots in color through
  PostScript, to a printer or viewer.
  </dd>
  </dl>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [string]' -->
  <dd>List of operands to graph.
  The input source can be one or more images (or image sections),
  tables and columns, or lists.
  Input can be interactively entered by specifying <span style="font-family: monospace;">"STDIN"</span> for 'input'.
  If text data are piped to 'sgraph',
  the 'input' parameter will automatically be set to <span style="font-family: monospace;">"STDIN"</span>.
  As described in the DESCRIPTION section,
  the task determines the type of input by
  the number of <span style="font-family: monospace;">"words"</span> in 'input':
  <div class="highlight-default-notranslate"><pre>
  "image"
  "text_file"
  "table y_col"
  "table x_col ycol"
  "table1 x_col table2 ycol"
  </pre></div>
  </dd>
  </dl>
  <dl id="l_errcolumn">
  <dt><b>errcolumn [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='errcolumn' Line='errcolumn [string]' -->
  <dd>The table column name containing values interpreted as error values.
  If the source of the data is an STSDAS table, 'errcolumn' specifies the
  name of the column containing the errors.
  </dd>
  </dl>
  <dl>
  <dt><b>(dvpar = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(dvpar = "") [pset]' -->
  <dd>Pset name for device parameters.  Parameters can be individually changed
  from the command line or can be edited as a group using ':e' from
  'eparam sgraph' or from the cl, 'eparam pltpar' or simply 'pltpar'.
  Details about these parameters are available by typing <span style="font-family: monospace;">"help pltpar"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>(pltpar = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(pltpar = "") [pset]' -->
  <dd>Pset name for plot parameters.  Parameters can be individually changed
  from the command line or can be edited as a group using ':e' from
  'eparam sgraph' or from the cl, 'eparam pltpar' or simply 'pltpar'.
  Details about these parameters are available by typing <span style="font-family: monospace;">"help pltpar"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>(axispar = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(axispar = "") [pset]' -->
  <dd>Pset name for axis and scaling parameters.  Parameters can be
  individually changed from the command line or can be edited as a group
  using ':e' from 'eparam sgraph' or from the cl, 'eparam pltpar' or
  simply 'pltpar'. Details about these parameters are available by typing
  <span style="font-family: monospace;">"help axispar"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Plot the output of a list processing filter.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ... list_filter | sgraph
  </pre></div>
  <p>
  2. Plot a graph using data entered interactively from the terminal.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sgraph STDIN
  </pre></div>
  <p>
  3. Overplot two lists.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sgraph list1,list2
  </pre></div>
  <p>
  4. Graph line 128 of image <span style="font-family: monospace;">"pix.imh"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sgraph pix.imh[*,128]
  </pre></div>
  <p>
  5. Graph the average of columns 50 through 100.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sgraph pix.imh[50:100,*] pltpar.axis=2
  </pre></div>
  <p>
  6. Graph two columns from a table against each other.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sgraph "table xcol ycol"
  </pre></div>
  <p>
  7. Graph a list in point plot mode.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sgraph list pointmode+
  </pre></div>
  <p>
  8. Plot a row from a table in which the columns contain arrays.
  </p>
  <div class="highlight-default-notranslate"><pre>
          cl&gt; sgraph "table.fits[sci,1][r:row=10] wavelength flux"
  -or-
          cl&gt; sgraph "table.fits[4][r:sporder=10] wavelength flux"
  </pre></div>
  <p>
  9. Annotate a graph of <span style="font-family: monospace;">"pix.c0h"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sgraph pix.c0h[*,10],pix.c0h[*,20] xlabel=column\
  &gt;&gt;&gt; ylabel=intensity title="lines 10 and 20 of pix.c0h"
  </pre></div>
  <p>
  10. Direct the graph to the standard plotter device.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sgraph list device=stdplot
  </pre></div>
  <p>
  11. Draw a set of points with superimposed error bars.  The data are
  from columns <span style="font-family: monospace;">"x"</span> and <span style="font-family: monospace;">"y"</span> in the STSDAS table 'mydata.tab'.   
  Upper and lower errors are in the columns <span style="font-family: monospace;">"upper"</span> and <span style="font-family: monospace;">"lower"</span>, 
  respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  cl&gt; sgraph "mydata.tab x y" point+ marker=cross
  cl&gt; sgraph "mydata.tab x y" point- erraxis=2 \
  &gt;&gt;&gt; errcol="lower upper" append+
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  'INDEF' values are not recognized when computing image projections.
  </p>
  <p>
  There is an inherent ambiguity between image section notation and file
  name template notation.  'sgraph' uses image name template expansion to
  parse the input list.  Therefore, it will not recognize some file name
  templates, for example: <span style="font-family: monospace;">"file[1-3]"</span> will fail because 'sgraph' thinks
  <span style="font-family: monospace;">"[1-3]"</span> is an invalid image section instead of a range specification.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  The 'sgraph' task was developed primarily by Zolt Levay (STScI) as an
  enhancement and revision to the 'graph' task in the IRAF 'plot' package.
  The modifications to work with cell arrays were performed by Warren Hack.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  pcol, pcols, prow, prows, dvpar, pltpar, axispar, grplot, igi, stdgraph, psikern, sgikern
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

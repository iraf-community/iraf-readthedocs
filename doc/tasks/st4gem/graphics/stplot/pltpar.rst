.. _pltpar:

pltpar: Specify graph parameters (pset for 'sgraph').
=====================================================

**Package: stplot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pltpar
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The 'pltpar' parameters specify the attributes of plots drawn by the
  'sgraph' task.
  </p>
  <p>
  Note that this is a pset, not an executable task;  it defines a set of 
  parameters used by other tasks.  Invoking the pset by name runs
  'eparam' on the parameter set, allowing the user to modify the
  parameters.  Alternatively, the parameters may be modified on the
  command line by specifying the pset name and parameter name, for
  example, you can type <span style="font-family: monospace;">"pltpar.pointmode=yes"</span> to set only the
  'pointmode' parameter.  Parameters can also be edited by using
  'eparam' on the calling task (e.g., by typing <span style="font-family: monospace;">"eparam sgraph"</span>), in 
  which case, 'pltpar' will appear as one of the task parameters; the
  'pltpar' parameters may then be edited by positioning the cursor on
  the line containing the pset name and typing <span style="font-family: monospace;">":e"</span>.  After editing
  the pset parameters, type Control-Z (or :q) to return to the main task parameter menu.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>(stack = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(stack = no) [boolean]' -->
  <dd>Stack multiple curves on separate vertical axes?  
  If this is set to
  <span style="font-family: monospace;">"no"</span>, all curves will be scaled together and plotted on a single set of
  axes.  Otherwise a separate set of axes will be drawn, joined into a
  single vertical column.
  </dd>
  </dl>
  <dl>
  <dt><b>(axis = 1) [integer, min = 1, max = 7]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(axis = 1) [integer, min = 1, max = 7]' -->
  <dd>Axis along which projection is to be taken.  If the input image has
  more than one dimension, the data will be projected to a single
  dimension.  This parameter specifies the axis along which projection
  will occur.  The default is one, i.e., project along the X axis.
  </dd>
  </dl>
  <dl>
  <dt><b>(pointmode = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(pointmode = no) [boolean]' -->
  <dd>Plot points only?  
  If set to <span style="font-family: monospace;">"no"</span>, the task will plot connected curves.  Note that to
  plot error bars, use 'pointmode = no' and 'erraxis = 1' or 'erraxis =
  2'.  See the descriptions of the 'marker' and 'szmarker' parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>(marker = box) [string, allowed values: point | box | plus |</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(marker = box) [string, allowed values: point | box | plus |' -->
  <dd>cross | circle | diamond | hline | vline | hebar | vebar]
  The marker style for each plotted point if 'pointmode=yes'.  See also
  'szmarker'.
  </dd>
  </dl>
  <dl>
  <dt><b>(szmarker = 0.005) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(szmarker = 0.005) [real]' -->
  <dd>The size of the markers if 'pointmode = yes'.  If 'szmarker &gt; 0', use
  this value as the size in normalized device coordinates (NDC) .  If
  'szmarker &lt; 0', use the absolute value as the size in world coordinates
  (WC).  If 'szmarker = 0' and the input comes from a text file, use the
  third column in the input data as the marker size.  If data are from an
  image or a table, then szmarker specifies the same size of every point.
  </dd>
  </dl>
  <dl>
  <dt><b>(erraxis = 0) [integer, min = 0, max = 2]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(erraxis = 0) [integer, min = 0, max = 2]' -->
  <dd>Plot the data as error bars?  
  The following values are allowed:
  <div class="highlight-default-notranslate"><pre>
  0 - Plot data as values rather than error bars
  1 - Plot data as errors parallel to X axis
  2 - Plot data as errors parallel to Y axis
  </pre></div>
  Note that 'erraxis' is ignored if
  'pointmode = yes'.
  </dd>
  </dl>
  <dl>
  <dt><b>(errtype = bartck) [string, allowed values: tckbar | bar | tick |</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(errtype = bartck) [string, allowed values: tckbar | bar | tick |' -->
  <dd>limit]
  The style of error bars (if 'erraxis' is not zero).
  </dd>
  </dl>
  <dl>
  <dt><b>(pattern = solid) [string, allowed values: solid | dashed | </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(pattern = solid) [string, allowed values: solid | dashed | ' -->
  <dd>dotted | dotdash]
  The line pattern style for the curve or the first of multiple curves.
  </dd>
  </dl>
  <dl>
  <dt><b>(crvstyle = straight) [string, allowed values: straight | pseudohist </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(crvstyle = straight) [string, allowed values: straight | pseudohist ' -->
  <dd>| fullhist]
  The curve style.  'straight' means line segments will connect data
  points, 'pseudohist' means that horizontal segments will be placed at
  each value and vertical segments will connect these, 'fullhist' means a
  bar graph, or horizontal segments at each value with vertical lines
  connecting the value with the bottom axis.
  </dd>
  </dl>
  <dl>
  <dt><b>(rejectlog = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(rejectlog = yes) [boolean]' -->
  <dd>Replace invalid logarithmic values with 'INDEF'?  Invalid values will
  be ignored in scaling and plotting.
  </dd>
  </dl>
  <dl>
  <dt><b>(barpat =<span style="font-family: monospace;">"hollow"</span>) [string, allowed values: hollow | solid |</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(barpat ="hollow") [string, allowed values: hollow | solid |' -->
  <dd>ahatch | bhatch | chatch | dhatch]
  Fill pattern for bar plot.  The nature of the pattern depends on the
  device and graphics kernel (driver) used to plot.  Many kernels do not
  support fill patterns.
  </dd>
  </dl>
  <dl>
  <dt><b>(crvcolor = INDEF) [integer, min = 1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(crvcolor = INDEF) [integer, min = 1]' -->
  <dd>Color index of data curve(s).  This color applies only to plotted data
  curves.  The color of any axes, labels, etc., is specified by
  the `color' parameter.  Note that the actual, drawn color will depend
  on the device and graphics kernel (driver) used for plotting.  Many kernels
  do not support color at all.  The usual interpretation of the color
  index is:
  <div class="highlight-default-notranslate"><pre>
  
  1 -- Black
  2 -- White
  3 -- Red
  4 -- Green
  5 -- Blue
  6 -- Yellow
  7 -- Cyan (blue/green)
  8 -- Magenta (red/blue)
  </pre></div>
  </dd>
  </dl>
  <dl>
  <dt><b>(color = INDEF) [integer, min = 1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(color = INDEF) [integer, min = 1]' -->
  <dd>Color index of axis and labels.  The color of the data curve(s) is
  specified by the `crvcolor' parameter.  Note that the actual, drawn
  color will depend on the device and graphics kernel (driver) used to
  plot.  Most kernels do not support color.
  </dd>
  </dl>
  <dl>
  <dt><b>(cycolor = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(cycolor = no) [boolean]' -->
  <dd>Cycle colors instead of line style for multiple curves?  
  If multiple curves are plotted on the same viewport (axes), i.e.,
  'stack=no', then use the color specified by the 'crvcolor' parameter
  for the first curve, and the next available color for each subsequent
  curve.  There are eight available colors, as described in the
  description of the 'crvcolor' parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>(version = 17August92) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(version = 17August92) [string]' -->
  <dd>Date the task was installed.  Do not change this parameter.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  sgraph
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

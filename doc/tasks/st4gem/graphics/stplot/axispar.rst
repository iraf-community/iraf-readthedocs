.. _axispar:

axispar: Specify axis and scaling parameters (pset for 'sgraph')
================================================================

**Package: stplot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  axispar
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The 'axispar' parameters specify the attributes of plot axes.
  </p>
  <p>
  Note that this is a pset, not an executable task;  it defines a set of 
  parameters used by other tasks.  Invoking the pset by name runs
  'eparam' on the parameter set, allowing the user to modify the
  parameters.  Alternatively, the parameters may be modified on the
  command line by specifying the pset name and parameter name, for
  example, you can type <span style="font-family: monospace;">"axispar.xflip=no"</span> to turn off the
  'xflip' parameter.  Parameters can also be edited by using
  'eparam' on the calling task (e.g., by typing <span style="font-family: monospace;">"eparam sgraph"</span>), in 
  which case, 'axispar' will appear as one of the task parameters; the
  'axispar' parameters can then be edited by positioning the cursor on
  the line containing the pset name and typing <span style="font-family: monospace;">":e"</span>.  After editing
  the pset parameters, type ^Z to return to the main task parameter menu.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>(wl = 0.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wl = 0.) [real]' -->
  <dd>Left world X-coordinate if not autoscaling.
  </dd>
  </dl>
  <dl>
  <dt><b>(wr = 0.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wr = 0.) [real]' -->
  <dd>Right world X-coordinate if not autoscaling.
  </dd>
  </dl>
  <dl>
  <dt><b>(wb = 0.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wb = 0.) [real]' -->
  <dd>Lower world Y-coordinate if not autoscaling.
  </dd>
  </dl>
  <dl>
  <dt><b>(wt = 0.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wt = 0.) [real]' -->
  <dd>Upper world Y-coordinate if not autoscaling.
  </dd>
  </dl>
  <dl>
  <dt><b>(xflip = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(xflip = no) [boolean]' -->
  <dd>Flip the autoscaled X axis?
  </dd>
  </dl>
  <dl>
  <dt><b>(yflip = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(yflip = no) [boolean]' -->
  <dd>Flip the autoscaled Y axis?
  </dd>
  </dl>
  <dl>
  <dt><b>(transpose = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(transpose = no) [boolean]' -->
  <dd>Transpose the X and Y axes of the plot?  
  If 'transpose = no', the
  horizontal axis will have the X values or pixel number.
  </dd>
  </dl>
  <dl>
  <dt><b>(logx = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(logx = no) [boolean]' -->
  <dd>Scale the X axis logarithmically?
  </dd>
  </dl>
  <dl>
  <dt><b>(logy = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(logy = no) [boolean]' -->
  <dd>Scale the Y axis logarithmically?
  </dd>
  </dl>
  <dl>
  <dt><b>(box = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(box = yes) [boolean]' -->
  <dd>Draw the box containing the axes and labels around the edge of the
  window?
  </dd>
  </dl>
  <dl>
  <dt><b>(ticklabels = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ticklabels = yes) [boolean]' -->
  <dd>Label major tick marks?
  </dd>
  </dl>
  <dl>
  <dt><b>(grid = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(grid = no) [boolean]' -->
  <dd>Draw grid lines on the plot?
  </dd>
  </dl>
  <dl>
  <dt><b>(xlabel) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(xlabel) [string]' -->
  <dd>X-axis label.
  </dd>
  </dl>
  <dl>
  <dt><b>(ylabel) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ylabel) [string]' -->
  <dd>Y-axis label.
  </dd>
  </dl>
  <dl>
  <dt><b>(title = imtitle) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(title = imtitle) [string]' -->
  <dd>The plot title may consist of one or two lines of text.  If the
  parameter 'sysid' is set to <span style="font-family: monospace;">"yes"</span>, then the first line of the title is
  a standard system-supplied string containing the user's name, date,
  etc.  If the 'title' parameter contains the string <span style="font-family: monospace;">"imtitle"</span> (the
  default), then the plot title will contain a line made up from the
  input file, image, or table name.  The user can supply an optional
  string for the 'title' parameter---this string will replace the string
  resulting from the <span style="font-family: monospace;">"imtitle"</span> specification.
  </dd>
  </dl>
  <dl>
  <dt><b>(sysid = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(sysid = yes) [boolean]' -->
  <dd>Include standard system information in the plot title?  
  If the 'sysid'
  parameter is set to <span style="font-family: monospace;">"yes"</span>, then a string including the user's name, date, host
  name, etc. is included in the plot title.
  </dd>
  </dl>
  <dl>
  <dt><b>(lintran = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(lintran = no) [boolean]' -->
  <dd>Perform a linear transformation of the X axis?
  </dd>
  </dl>
  <dl>
  <dt><b>(p1 = 0.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(p1 = 0.) [real]' -->
  <dd>Starting input pixel value if 'lintran = yes'.
  </dd>
  </dl>
  <dl>
  <dt><b>(p2 = 0.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(p2 = 0.) [real]' -->
  <dd>Ending input pixel value if 'lintran = yes'.
  </dd>
  </dl>
  <dl>
  <dt><b>(q1 = 0.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(q1 = 0.) [real]' -->
  <dd>Starting output pixel value if 'lintran = yes'.
  </dd>
  </dl>
  <dl>
  <dt><b>(q2 = 1.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(q2 = 1.) [real]' -->
  <dd>Ending output pixel value if 'lintran = yes'.
  </dd>
  </dl>
  <dl>
  <dt><b>(majrx = 5) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(majrx = 5) [integer]' -->
  <dd>Number of major divisions along the X grid.
  </dd>
  </dl>
  <dl>
  <dt><b>(minrx = 5) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(minrx = 5) [integer]' -->
  <dd>Number of minor divisions along the X grid.
  </dd>
  </dl>
  <dl>
  <dt><b>(majry = 5) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(majry = 5) [integer]' -->
  <dd>Number of major divisions along the Y grid.
  </dd>
  </dl>
  <dl>
  <dt><b>(minry = 5) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(minry = 5) [integer]' -->
  <dd>Number of minor divisions along the Y grid.
  </dd>
  </dl>
  <dl>
  <dt><b>(round = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(round = no) [boolean]' -->
  <dd>Round axes to nice values?  (Values at tick marks will be significant,
  based on scale of the data.)
  </dd>
  </dl>
  <dl>
  <dt><b>(margin = INDEF) [real, min = 0, max = 1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(margin = INDEF) [real, min = 0, max = 1]' -->
  <dd>The margin between the viewport edges (plot axes) and the limits of the
  plotted curve(s) as a fraction of the viewport (NDC).  If 'margin =
  INDEF', the default, a 2.5% margin will apply.  That is, the plotted
  curve(s) will be inset .025 times the size of the viewport.  Set
  'margin = 0' to plot curves to the axes.
  </dd>
  </dl>
  <br>
  <dl>
  <dt><b>(version = 17August92) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(version = 17August92) [string]' -->
  <dd>Date the task was installed. Do not change this parameter.
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
  sgraph, pltpar, dvpar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

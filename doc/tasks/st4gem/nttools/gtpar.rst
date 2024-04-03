.. _gtpar:

gtpar: Pset to specify graph parameters for 'gtedit' task.
==========================================================

**Package: nttools**

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
  Parameters in the 'gtpar' pset specify the attributes of plots drawn with the
  'gtedit' task.
  </p>
  <p>
  Note that this is a pset, not an executable task.  Invoking the pset by name
  runs 'eparam', enabling the parameters to be interactively edited. 
  Parameters can also be modified on the
  CL command line by specifying the pset name and parameter name,
  for example, <span style="font-family: monospace;">"gtpar.box = no"</span>).
  The pset name will also appear as one of
  the task parameters in the 'gtedit' task;
  to change values in the pset,
  position the cursor to the 'gtpar' pset name and type <span style="font-family: monospace;">":e"</span> to invoke 'eparam'.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>(wx1 = 0) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wx1 = 0) [real]' -->
  <dd>Left world X-coordinate (if autoscaling is not used).
  </dd>
  </dl>
  <dl>
  <dt><b>(wx2 = 0.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wx2 = 0.) [real]' -->
  <dd>Right world X-coordinate (if autoscaling is not used).
  </dd>
  </dl>
  <dl>
  <dt><b>(wy1 = 0.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wy1 = 0.) [real]' -->
  <dd>Lower world Y-coordinate (if no autoscaling is used).
  </dd>
  </dl>
  <dl>
  <dt><b>(wy2 = 0.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wy2 = 0.) [real]' -->
  <dd>Upper world Y-coord (if not autoscaling).
  </dd>
  </dl>
  <dl>
  <dt><b>(marker = box) [string, allowed values:  point | box | plus | </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(marker = box) [string, allowed values:  point | box | plus | ' -->
  <dd>cross | circle | diamond | hline | vline | hebar | vebar]
  The name of the style of marker plotted at each point if 'pointmode=yes'.
  </dd>
  </dl>
  <dl>
  <dt><b>(szmarker = 0.005) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(szmarker = 0.005) [real]' -->
  <dd>The size of the markers if 'pointmode = yes'.  If this parameter is greater 
  than 0, its value represents the marker size in world coordinates (WC).  If it 
  is less than zero, the absolute value will be used, representing size in 
  normalized device coordinates (NDC).  If it is set to exactly zero, and the
  input is from a list file,
  then the third column in the input data is used as the marker size.
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
  <dd>Draw the box containing the axes and labels around periphery of the 
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
  <dd>Draw grid lines on plot?
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
  <dt><b>(title = imtitle)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(title = imtitle)' -->
  <dd>The plot title consists of a standard system-supplied string containing
  the user's name, date, etc.  If the 'title' parameter contains the string
  <span style="font-family: monospace;">"imtitle"</span> (the default), then the plot title will contain a second line
  made up from the input file or table name.  Otherwise, the title will
  contain the string value.
  </dd>
  </dl>
  <dl>
  <dt><b>(vx1 = 0.) [real, min = 0, max = 1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vx1 = 0.) [real, min = 0, max = 1]' -->
  <dd>Left limit of device viewport.
  </dd>
  </dl>
  <dl>
  <dt><b>(vx2 = 0.) [real, min = 0, max = 1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vx2 = 0.) [real, min = 0, max = 1]' -->
  <dd>Right limit of device viewport.
  </dd>
  </dl>
  <dl>
  <dt><b>(vy1 = 0.) [real, min = 0, max = 1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vy1 = 0.) [real, min = 0, max = 1]' -->
  <dd>Bottom limit of device viewport.
  </dd>
  </dl>
  <dl>
  <dt><b>(vy2 = 0.) [real], min = 0, max = 1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vy2 = 0.) [real], min = 0, max = 1]' -->
  <dd>Upper limit of device viewport.
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
  <dd>Round axes to nice values?
  </dd>
  </dl>
  <dl>
  <dt><b>(fill = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fill = yes) [boolean]' -->
  <dd>Fill the viewport rather than enforcing unity aspect ratio?
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
  <p>
  Type <span style="font-family: monospace;">"help tables opt=sys"</span> for a higher-level description of the 'tables' 
  package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

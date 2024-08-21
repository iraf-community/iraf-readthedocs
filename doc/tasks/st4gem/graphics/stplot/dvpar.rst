.. _dvpar:

dvpar: Specify device parameters (pset)
=======================================

**Package: stplot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  dvpar
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The 'dvpar' parameter set (pset) specifies device-related parameters.
  These include the device name, whether plots should be appended to
  existing plots, and the edges of the device viewport---that part of the
  display device on which to draw the plot.
  </p>
  <p>
  Note that this is a parameter set (pset)---not an executable task.  That
  means that if the task is invoked by name on the command line, it will
  start the 'eparam' task to edit the 'dvpar' parameters.  Individual
  parameters may be assigned using CL assignment statements from the
  command line, or through the task parameters for 'fieldplot'.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>(device = <span style="font-family: monospace;">"stdgraph"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(device = "stdgraph") [string]' -->
  <dd>The graphics device name.  The default, <span style="font-family: monospace;">"stdgraph"</span>, uses the CL 
  environment parameter `stdgraph' to find the device name.  For 
  example, if you are using gterm in SunView, you could have set 
  `stdgraph=gterm' or `device=gterm'.  To overlay graphics on an image 
  display, use an <span style="font-family: monospace;">"imd"</span> device, <span style="font-family: monospace;">"imdr"</span> for red, <span style="font-family: monospace;">"imdg"</span> for green, etc.
  </dd>
  </dl>
  <dl>
  <dt><b>(append = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(append = no) [boolean]' -->
  <dd>Append the graph to an existing plot?
  </dd>
  </dl>
  <dl>
  <dt><b>(left = 0) [real, min = 0, max = 1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(left = 0) [real, min = 0, max = 1]' -->
  <dd>The NDC coordinates of the left edge of the plot.
  </dd>
  </dl>
  <dl>
  <dt><b>(right = 0) [real, min = 0, max = 1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(right = 0) [real, min = 0, max = 1]' -->
  <dd>The NDC coordinates of the right edge of the plot.
  </dd>
  </dl>
  <dl>
  <dt><b>(bottom = 0) [real, min = 0, max = 1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(bottom = 0) [real, min = 0, max = 1]' -->
  <dd>The NDC coordinates of the bottom edge of the plot.
  </dd>
  </dl>
  <dl>
  <dt><b>(top = 0) [real, min = 0, max = 1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(top = 0) [real, min = 0, max = 1]' -->
  <dd>The NDC coordinates of the top edge of the plot.
  </dd>
  </dl>
  <dl>
  <dt><b>(fill = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fill = yes) [boolean]' -->
  <dd>Fill the viewport?  
  If set to <span style="font-family: monospace;">"yes"</span>, the plot will fill the area specified by
  the 'left', 'right', 'bottom', and 'top' viewport parameters.  Otherwise, the
  shape of the plot will reflect the aspect of the input data, but will
  not be larger than the specified viewport.  Note that this does not
  apply to all tasks using the 'dvpar' pset.
  </dd>
  </dl>
  <dl>
  <dt><b>(coords) [*gcur]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(coords) [*gcur]' -->
  <dd>Graphics cursor file. This is used if the 
  task supports interaction via the graphics cursor.
  </dd>
  </dl>
  <dl>
  <dt><b>(image_coord) [*imcur]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(image_coord) [*imcur]' -->
  <dd>Image cursor file. This is used if the 
  task supports interaction via the image display cursor.
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
  fieldplot, newcont, sgraph, siaper, wcslab, cursor, plot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

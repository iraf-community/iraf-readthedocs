.. _isomap:

isomap: Plot ellipses superposed over image contours.
=====================================================

**Package: isophote**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  isomap  image table floor ceiling
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The 'isomap' task draws a contour map from a 2-dimensional 
  image and superposes ellipses on it corresponding to 
  intensity levels. Ellipse data is taken from a table 
  created by the 'ellipse' task. 
  </p>
  <p>
  This task is a script which calls the tasks 'tsort' and 
  'trebin' in the 'ttools' package.  These tasks create a 
  temporary table with an interpolated version of the original 
  input table.  This temporary table is then fed to the hidden 
  task 'map', which creates a set of temporary files containing 
  coordinates of ellipse points.  The 'plot.contour' task is 
  then invoked to draw contours, and finally, the 'stplot.sgraph' 
  task uses the temporary ellipse point files to draw the 
  ellipses. 
  </p>
  <p>
  The intensity interval to be contoured is specified by the 
  parameters 'floor' and 'ceiling'.  Care must be taken with 
  these parameters, because the 'trebin' task can also 
  extrapolate from the original data, and meaningless results 
  could be generated in some cases. Linear interpolation is 
  used.  The 'nlevels' parameter specifies the number of levels 
  to be contoured, up to 10.
  </p>
  <p>
  The packages 'ttools', 'stplot', and 'plot' must be loaded 
  before using this task.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image [file name]' -->
  <dd>Input image to be contoured.
  </dd>
  </dl>
  <dl id="l_table">
  <dt><b>table [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file name]' -->
  <dd>Table containing the results of isophotometry analysis 
  (i.e., the table produced by 'ellipse').
  </dd>
  </dl>
  <dl id="l_floor">
  <dt><b>floor [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='floor' Line='floor [real]' -->
  <dd>Minimum level to be contoured.
  </dd>
  </dl>
  <dl id="l_ceiling">
  <dt><b>ceiling [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ceiling' Line='ceiling [real]' -->
  <dd>Maximum level to be contoured.
  </dd>
  </dl>
  <dl>
  <dt><b>(nlevels = 3) [integer, min=2, max=10]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nlevels = 3) [integer, min=2, max=10]' -->
  <dd>Number of contours.
  </dd>
  </dl>
  <dl>
  <dt><b>(device = <span style="font-family: monospace;">"stdgraph"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(device = "stdgraph") [string]' -->
  <dd>Graphics output device.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Supperposition of contours and ellipses may lack precision when using
  image sections with stepping, due to numerical truncation effects.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by I.Busko
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ellipse
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

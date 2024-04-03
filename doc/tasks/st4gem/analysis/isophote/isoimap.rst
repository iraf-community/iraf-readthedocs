.. _isoimap:

isoimap: Plot ellipses superposed over the gray-scale image display.
====================================================================

**Package: isophote**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  isoimap  image table 
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The 'isoimap' task displays the original image in the gray-scale image
  display, and superposes ellipses on it. Ellipse data is taken from a table 
  created by the 'ellipse' task. 
  </p>
  <p>
  This task is a script which calls the tasks 'tsort' and 'trebin' in the
  'ttools' package.  These tasks create a temporary table with an
  interpolated version of the original input table.  This temporary table
  is then fed to the hidden task 'map', which creates a set of temporary
  files containing coordinates of ellipse points.  The 'images.tv.display'
  task is then invoked to load the image display with the original image,
  and finally the 'stplot.sgraph' task uses the temporary ellipse point
  files to draw the ellipses. 
  </p>
  <p>
  The semi-major axis length interval to be plotted is specified by the
  parameters 'minsma' and 'maxsma'. If the 'fulltable' parameter is set to 
  'yes', the full range of semi-major axis lengths available in the table is 
  used instead. Care must be taken with parameters 'minsma' and 'maxsma', 
  because the 'trebin' task can also extrapolate from the original data, 
  and meaningless results could be generated in some cases. Linear
  interpolation is used.  The 'nlevels' parameter specifies the number of
  ellipses to be plotted, up to 10.
  </p>
  <p>
  Parameters available in the 'display' task can be set before running
  this task so that gray-scale manipulation can be controlled. There are,
  however, limitations in the graphics interface so the task assumes that
  the 'fill' parameter is set to <span style="font-family: monospace;">"yes"</span>. This also works only when the
  image display is square (i.e., it has an aspect ratio of 1.0).
  </p>
  <p>
  Packages 'ttools', 'stplot', 'plot', 'images' and 'tv' must be loaded 
  before using this task.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image [file name]' -->
  <dd>Input image to be displayed.
  </dd>
  </dl>
  <dl id="l_table">
  <dt><b>table [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file name]' -->
  <dd>Table containing the results of isophotometry analysis 
  (i.e., the table produced by 'ellipse').
  </dd>
  </dl>
  <dl>
  <dt><b>(fulltable = <span style="font-family: monospace;">"yes"</span>) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fulltable = "yes") [boolean]' -->
  <dd>Use full range of semi-major axis from table?
  </dd>
  </dl>
  <dl>
  <dt><b>(minsma = 1.0) [real, min=0.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(minsma = 1.0) [real, min=0.0]' -->
  <dd>Minimum semi-major axis to be plotted.
  </dd>
  </dl>
  <dl>
  <dt><b>(maxsma = 1.0) [real, min=1.0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(maxsma = 1.0) [real, min=1.0]' -->
  <dd>Maximum semi-major axis to be plotted.
  </dd>
  </dl>
  <dl>
  <dt><b>(nlevels = 3) [integer, min=2, max=10]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nlevels = 3) [integer, min=2, max=10]' -->
  <dd>Number of ellipses.
  </dd>
  </dl>
  <dl>
  <dt><b>(color = <span style="font-family: monospace;">"r"</span>) [string, allowed values: r | g | b | w | y]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(color = "r") [string, allowed values: r | g | b | w | y]' -->
  <dd>Graphics overlay color (colors are red, green, blue, white, or yellow).
  </dd>
  </dl>
  <dl>
  <dt><b>(frame = 1) [int, min=1, max=4]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(frame = 1) [int, min=1, max=4]' -->
  <dd>Display frame to be loaded.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Draw three ellipses taken from an image 
  called 'image' and a table 'table'. Minimum and maximum 
  are 10.0 and 100.0, respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  st&gt; isoimap  image table fulltable=no amin=10. amax=100. nlevels=3
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Graphics overlay may lack precision when using image sections 
  with stepping, due to numerical truncation effects.
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
  isoexam, ellipse, display
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

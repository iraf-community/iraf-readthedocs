.. _isoplot:

isoplot: Plot results of isophotal analysis.
============================================

**Package: isophote**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  isoplot input xaxis yaxis
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task shows, in graphic format, results from the isophote 
  fitting task 'ellipse'. 
  </p>
  <p>
  The input used by 'isoplot' is the main table generated 
  by 'ellipse'.  The 'xaxis' and 'yaxis' parameters specify the 
  table columns containing the data to be plotted.
  </p>
  <p>
  This task is a script which calls the 'sgraph' task to do the 
  actual plotting. The 'stplot' package must, therefore, be 
  loaded before using this task.  All parameters associated with 
  'sgraph' can be used to tailor the plot format (for more 
  information about doing this, type <span style="font-family: monospace;">"help sgraph"</span>). The main
  difference in using this task or 'sgraph' directly is that this
  task takes into account properly the error bars associated with 
  the 'yaxis' data, when appropriate.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name]' -->
  <dd>Table created by 'ellipse'.
  </dd>
  </dl>
  <dl id="l_xaxis">
  <dt><b>xaxis = <span style="font-family: monospace;">""</span>  [string, Allowed values: SMA | RSMA]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xaxis' Line='xaxis = ""  [string, Allowed values: SMA | RSMA]' -->
  <dd>Column name containing abcissa data to be plotted.
  </dd>
  </dl>
  <dl id="l_yaxis">
  <dt><b>yaxis = <span style="font-family: monospace;">""</span>  [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='yaxis' Line='yaxis = ""  [string]' -->
  <dd>Column name containing ordinate data to be plotted.
  </dd>
  </dl>
  <dl>
  <dt><b>(device = <span style="font-family: monospace;">"stdgraph"</span>)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(device = "stdgraph")' -->
  <dd>Graphics device.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Unexpected results may be produced depending on the 'sgraph' parameter
  values. It is recommended to unlear all psets associated with 'sgraph'
  before running this task.
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
  isopall, sgraph, ellipse
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

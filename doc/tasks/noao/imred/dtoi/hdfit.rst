.. _hdfit:

hdfit: Fit a curve to density, log exposure values
==================================================

**Package: dtoi**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  hdfit database 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>Database[s] containing the density, log exposure information.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"power"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "power"' -->
  <dd>Type of curve to fit; chosen from <span style="font-family: monospace;">"power"</span>, <span style="font-family: monospace;">"legendre"</span>, <span style="font-family: monospace;">"chebyshev"</span>, 
  <span style="font-family: monospace;">"spline1"</span> or <span style="font-family: monospace;">"spline3"</span>.  Abbreviations are permitted.
  </dd>
  </dl>
  <dl id="l_transform">
  <dt><b>transform = <span style="font-family: monospace;">"logopacitance"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='transform' Line='transform = "logopacitance"' -->
  <dd>Transformation performed on the density prior to fitting.  Chosen from
  <span style="font-family: monospace;">"none"</span>, <span style="font-family: monospace;">"logopacitance"</span>, <span style="font-family: monospace;">"k50"</span> or <span style="font-family: monospace;">"k75"</span>. 
  </dd>
  </dl>
  <dl id="l_weighting">
  <dt><b>weighting = <span style="font-family: monospace;">"none"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='weighting' Line='weighting = "none"' -->
  <dd>Weights can be assigned to the independent variable for fitting a curve.
  Choices are <span style="font-family: monospace;">"none"</span>, <span style="font-family: monospace;">"user"</span> and <span style="font-family: monospace;">"calculated"</span>.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 4' -->
  <dd>Order of the fit.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Fit the data interactively?
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "stdgraph"' -->
  <dd>Interactive graphics device.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">"stdgcur"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = "stdgcur"' -->
  <dd>Source of cursor input.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <i>hdfit</i> is used to fit a curve to density and log exposure
  values in preparation for transforming an image from density to intensity.
  The log exposure and density are read from <b>database</b>.
  More than one database can be input,
  in which case one curve is fit to the combined data and the results
  written to each database in the list.
  </p>
  <p>
  Weights can be applied to the independent variable of the fit.
  Weights can be changed interactively, and are originally chosen from
  <span style="font-family: monospace;">"none"</span>, <span style="font-family: monospace;">"user"</span> and <span style="font-family: monospace;">"calculated"</span>.  A weights value can
  be calculated from the standard deviations, read from <b>database</b>,
  as weight = (normalized density) / sdev.  If user weights are to be
  used, they are read from <b>database</b> record <span style="font-family: monospace;">"weights"</span> as <span style="font-family: monospace;">"wts_vals"</span>
  entries.  
  </p>
  <p>
  When <b>interactive</b> = yes, the HD curve is plotted and the cursor
  made available for interactively examining and altering the fit.
  The fitting function, transformation and order can be modified; data
  points can be added, deleted or edited.  Four choices of independent
  variable are available in <b>hdfit</b> by means of the parameter 
  <b>transform</b>.  No transformation can take place, in which case
  the independent variable is the density.  Other choices are the log
  opacitance or a Kaiser transform with alpha = 0.50 or 0.75.  The
  default choice is to fit log exposure as a function of the log opacitance; 
  this is traditionally known as the Baker-Seidel function.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  Using the defaults as starting parameters, interactively fit a curve to
  the data points in db1.
  
          cl&gt; hdfit db1
  
  A sixth order power series function is fit in batch mode to the db1 data.
  
          cl&gt; hdfit db1 order=6 interactive-
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  spotlist, dematch, hdtoi
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

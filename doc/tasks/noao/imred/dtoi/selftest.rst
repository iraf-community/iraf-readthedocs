.. _selftest:

selftest: Self test program to check DTOI transformation
========================================================

**Package: dtoi**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  selftest nbits
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_nbits">
  <dt><b>nbits = 12</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nbits' Line='nbits = 12' -->
  <dd>Dymanic range of data to test.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span> </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "stdgraph" ' -->
  <dd>Plotting device for graphical output.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>A table of density, intensity values is printed if <b>verbose</b> = yes.
  </dd>
  </dl>
  <dl id="l_ceiling">
  <dt><b>ceiling = 30000.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ceiling' Line='ceiling = 30000.' -->
  <dd>Maximum intensity to output.
  </dd>
  </dl>
  <dl id="l_max_raw">
  <dt><b>max_raw = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='max_raw' Line='max_raw = 0' -->
  <dd>The maximum raw data value.  Needed only if <i>nbits</i> equals something
  other than 12, 15 or 0.
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = 0.0' -->
  <dd>The raw data value to density scale value.  Needed only if <i>nbits</i>
  equals something other than 12, 15, or 0.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <i>selftest</i> is a test program for the <i>dtoi</i> package.  Its 
  output can be examined to see if numerical errors are introduced during
  the density to intensity transformation.  It also evaluates truncation
  errors produced when an output image with integer pixels is written.  
  </p>
  <p>
  Many different PDS setups can be investigated with task <b>selftest</b>.
  Setting parameter <i>nbits</i> = 12
  indicates PDS format data, with data range 0 to 3071.  Setting <i>nbits</i> = 15 
  indicates FITS format data, with data range 0 to 24575.  The special value of
  <i>nbits</i> = 0 means a small test data range from 1 to 144 is investigated.
  If any other value of <i>nbits</i> is entered, the user is queried for the
  max raw data values and the raw data to density scaling factor.
  </p>
  <p>
  An intensity vector is generated from a density vector in two different ways.  
  The first method uses the density vector and known coefficients to compute
  the intensity.  The second method uses the curfit package to generate a
  look up table of intensities as done in task <b>HDTOI</b>.  The residual
  of the two intensity vectors is plotted.  Ideally, the difference between
  the 'known' intensities and 'calculated' intensities is zero.
  </p>
  <p>
  The second plot output by <b>selftest</b> shows intensity as a function
  of density.  Two lines are overplotted; integer intensity versus density
  and real intensity versus density.  Because truncation errors are most
  pronounced at low density values, the plot covers only the lowest 5%
  of the density range.  The user should investigate the plot with the
  cursor zoom and expand capabilities to determine if truncation errors
  are significant.
  </p>
  <p>
  In verbose mode, <b>selftest</b> produced a three column table of raw
  data value, density and calculated intensity. 
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  Run task selftest for 12 bit data with plots appearing on the terminal.
  
          cl&gt; selftest
  </pre></div>
  <p>
  Run selftest in verbose mode, spooling the output to file 'ditable'.  This
  file is then run through the 'fields' task to extract the density and intensity
  columns which are piped to plot.  The results in a plot of the look up table.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; selftest ver+ &gt; ditable
  cl&gt; fields ditable 2,3 | graph xlab=Density ylab=Intensity
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES'  -->
  

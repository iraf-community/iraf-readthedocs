.. _radplt:

radplt: Plot the radial profile of an object (noao.proto V2.9)
==============================================================

**Package: obsolete**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  radplt input x_init y_init
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>the list of images which contain the star whose profile is to be plotted
  </dd>
  </dl>
  <dl id="l_x_init">
  <dt><b>x_init</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='x_init' Line='x_init' -->
  <dd>the approximate column coordinate as a starting point for the centering
  </dd>
  </dl>
  <dl id="l_y_init">
  <dt><b>y_init</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='y_init' Line='y_init' -->
  <dd>the approximate line (row) coordinate as a starting point for the centering
  </dd>
  </dl>
  <dl id="l_cboxsize">
  <dt><b>cboxsize = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cboxsize' Line='cboxsize = 5' -->
  <dd>the size of the extraction box to be used during the centering process
  </dd>
  </dl>
  <dl id="l_rboxsize">
  <dt><b>rboxsize = 21</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rboxsize' Line='rboxsize = 21' -->
  <dd>the size of the extraction box to be used for the radial profile. The
  profile will extend to sqrt(2) * rboxsize / 2. This is the length
  of the diagonal from the box center to a corner, and corresponds to about
  14 pixels for the default value.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Given the approximate coordinates of the center of a star, (x_init, y_init),
  RADPLT will compute a more accurate center using the algorithms described in
  the Kitt Peak publication <span style="font-family: monospace;">"Stellar Magnitudes from Digital Images"</span> under
  the Mountain Photometry Code section and then plot the intensity values
  in the profile extraction box as a function of distance from the center.
  This is effectively a radial profile.
  </p>
  <p>
  The values for both box sizes should be odd.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following example plots the profile of a star near (123, 234):
  <br>
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; radplt m92red 123 234
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The routine will probably fail if the desired star is within 2 or 3 pixels
  of the image boundary.
  </p>
  </section>
  <section id="s_use_instead">
  <h3>Use instead</h3>
  <p>
  plot.pradprof
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcntr
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'USE INSTEAD' 'SEE ALSO'  -->
  

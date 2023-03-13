.. _imcntr:

imcntr: Locate the center of a stellar image
============================================

**Package: proto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imcntr input x_init y_init
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of images which contain the star to be centered.
  </dd>
  </dl>
  <dl id="l_x_init">
  <dt><b>x_init</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='x_init' Line='x_init' -->
  <dd>The approximate column coordinate as a starting point for the centering.
  </dd>
  </dl>
  <dl id="l_y_init">
  <dt><b>y_init</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='y_init' Line='y_init' -->
  <dd>The approximate line (row) coordinate as a starting point for the centering.
  </dd>
  </dl>
  <dl id="l_cboxsize">
  <dt><b>cboxsize = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cboxsize' Line='cboxsize = 5' -->
  <dd>The size of the extraction box to be used during the centering process.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Given the approximate coordinates of the center of an object, (x_init, y_init),
  IMCNTR will compute a more accurate center using the algorithms described in
  the Kitt Peak publication <span style="font-family: monospace;">"Stellar Magnitudes from Digital Images"</span> under
  the Mountain Photometry Code section. Briefly, this algorithm computes
  the sum of all the rows and the sum of all the columns in the extraction
  box. These are called <span style="font-family: monospace;">"marginal distributions"</span>. The center in x (column
  value) is then the center of gravity of the row marginal, and the center
  in y is the center of gravity of the column marginal.
  If the resultant x or y center value deviates from the original input
  approximate starting points by more than 1 pixel, the process is repeated
  once more around the new center. Only one iteration is attempted to
  avoid runaway if a bright star is nearby.
  </p>
  <p>
  Because the centers are computed independently for x and y, the result
  may be considered inferior to a true two-dimensional centering algorithm.
  Nevertheless, in practice the results appear to be very usable.
  </p>
  <p>
  The value for the box size should be an odd value. If chosen too large,
  nearby objects will affect the result. If too small, the center will be
  poorly defined.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. The following example locates the center of a star near (123, 234)
  in 3 images.
  <br>
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imcntr m92red,m92blu,m92grn 123 234
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The routine will probably fail if the desired object is within 2 or 3 pixels
  of the image boundary.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  pradprof
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

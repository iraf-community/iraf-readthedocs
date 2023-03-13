.. _imjoin:

imjoin: Join images along a given dimension
===========================================

**Package: imutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imjoin input output join_dimension 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input images to be joined. The input images must have the
  same dimensionality and the same size along all dimensions but the join
  dimension.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output combined image.
  </dd>
  </dl>
  <dl id="l_join_dimension">
  <dt><b>join_dimension</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='join_dimension' Line='join_dimension' -->
  <dd>The image dimension along which the input images will be joined.
  </dd>
  </dl>
  <dl id="l_pixtype">
  <dt><b>pixtype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixtype' Line='pixtype = ""' -->
  <dd>The output image pixel type. The options are in order of increasing
  precedence <span style="font-family: monospace;">"s"</span> (short), <span style="font-family: monospace;">"u"</span> (unsigned short), <span style="font-family: monospace;">"i"</span> (integer),
  <span style="font-family: monospace;">"l"</span> (long integer), <span style="font-family: monospace;">"r"</span> (real), <span style="font-family: monospace;">"d"</span> (double), and <span style="font-family: monospace;">"x"</span> (complex).
  If the output image pixel type is not specified, it defaults to highest
  precedence input image datatype.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about actions taken by the task ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IMJOIN creates a single output image <i>output</i>  by joining a list of input
  images <i>input</i> along a specified dimension <i>join_dimension</i>. IMJOIN
  can be used to create a single long 1-dimensional image from a list of shorter
  1-dimensional images, or to piece together a set of 3-dimensional images into
  larger 3-dimensional images along either the x, y, or z directions. The input
  images must all have the same number of dimensions and the same size along
  all dimensions by the join dimension. The output image inherits the
  world coordinates system if any of the first input image.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  1.  Join a list of 1-dimensional spectra into a single long output spectrum.
  
      cl&gt; imjoin @inlist output 1
  
  2.  Join three datacubes along the z direction.
  
      cl&gt; imjoin c1,c2,c3 c123 3
  </pre></div>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  On some systems there are limitations on the number of input images that
  can be joined in a single execution of IMJOIN.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imstack, imslice, imtile
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIMINGS' 'BUGS' 'SEE ALSO'  -->
  

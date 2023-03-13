.. _imjoin:

imjoin: N-dimensional image join along arbitrary axis
=====================================================

**Package: vol**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imjoin input output 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input images or @file
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output joined image
  </dd>
  </dl>
  <dl id="l_joindim">
  <dt><b>joindim = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='joindim' Line='joindim = 1' -->
  <dd>Image dimension along which the input images will be joined.
  </dd>
  </dl>
  <dl id="l_outtype">
  <dt><b>outtype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtype' Line='outtype = ""' -->
  <dd>Output image datatype.  If not specified, defaults to highest precedence
  input image datatype.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IMJOIN concatenates a set of input images into a single output image,
  in a specified dimension only.  For example, it can join a set of one
  dimensional images into a single, long one dimensional image, or a
  set of one dimensional images into a single two dimensional image.
  IMJOIN may be used to piece together datacubes into larger
  datacubes, either in x, y, or z; likewise with higher dimensional images.
  </p>
  <p>
  For joining a set of 1 or 2 dimensional images in both x and y at the same
  time, see IMMOSAIC.  For stacking images of any dimension into an image
  of the next higher dimension, see IMSTACK.  Although IMJOIN can also
  stack a set of images into a single higher dimensional image, IMSTACK
  is more efficient for that operation.  In most cases, IMJOIN must keep
  all input images open at the same time, while IMSTACK does not (there may
  be limitations on the number of files that can be kept open at one time).
  Use IMJOIN primarily when joining a set of images along any dimension that
  is not the next higher one from that of the input images.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  1.  Join a list of one dimensional spectra into a single long image.
  
      cl&gt; imjoin @inlist output 1
  
  2.  Join three datacubes along the z direction.
  
      cl&gt; imjoin c1,c2,c3 fullxcube 3
  </pre></div>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  <p>
  Join 10 5000 column type short spectra into one 50000 column image:
  6 seconds on a diskless Sun-3.  
  </p>
  <p>
  Join 2 512*512 images:  28 seconds on diskless Sun-3.  Join 2 50*50*50
  datacubes in x, y, or z:  15 seconds.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  There may be limitations on the number of input images that can be handled
  in one execution on some systems.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  immosaic, imstack, imslice
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIMINGS' 'BUGS' 'SEE ALSO'  -->
  

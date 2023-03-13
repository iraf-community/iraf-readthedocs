.. _imstack:

imstack: Stack images into a single image of higher dimension
=============================================================

**Package: imutil**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  imstack images output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images to be stacked.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Name of output image created.
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = "*"' -->
  <dd>Title of output image.  If <span style="font-family: monospace;">"*"</span> then the title defaults to that of
  the first input image.
  </dd>
  </dl>
  <dl id="l_pixtype">
  <dt><b>pixtype = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixtype' Line='pixtype = "*"' -->
  <dd>Pixel datatype of output image.  If <span style="font-family: monospace;">"*"</span> then the pixel datatype defaults to
  that of the first input image.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The input <i>images</i> are stacked to form an <i>output</i> image having one
  higher dimension than the input images, and a length of that dimension equal
  to the number of input images.  The input images must all be of the same
  dimension and size.
  </p>
  <p>
  The output image inherits the world coordinate system (WCS) of the first
  input image. If the dimension of the input image WCS is greater than or
  equal to the dimension of the output image, the input WCS is copied to the
  output image WCS without modification. Otherwise the input image WCS
  dimension is incremented by 1 and copied to the output image WCS, the input
  WCS coordinate transformations for each input image axis are copied to the
  output image WCS without modification, and the new output image axis is
  assigned a WCS type of 'linear' and the identity transformation.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Stack a set of four two dimensional images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imstack image* image.3d
  </pre></div>
  <p>
  2. To stack a section of images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imstack image*[1:10,1:10] newimage
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imslice
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

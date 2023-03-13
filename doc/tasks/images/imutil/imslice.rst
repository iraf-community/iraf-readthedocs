.. _imslice:

imslice: Slice images into images of lower dimension
====================================================

**Package: imutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imslice input output slicedim
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input images to be sliced. The input images must have a
  dimensionality greater than one.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The root name of the output images. For each n-dimensional input
  image m (n-1)-dimensional images will be created, where m is the
  length of the axis to be sliced. The sequence number m will
  be appended to the output image name.
  </dd>
  </dl>
  <dl id="l_slice_dimension">
  <dt><b>slice_dimension</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='slice_dimension' Line='slice_dimension' -->
  <dd>The dimension to be sliced.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about actions taken.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The n-dimensional images <i>input</i> are sliced into m (n-1)-dimensional
  images <i>output</i>, where m is the length of the axis of the input
  image to be sliced. A sequence number from 1 to m is appended to output
  to create the output image name.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Slice the 3-D image <span style="font-family: monospace;">"datacube"</span> into a list of 2D images. A list of
  images called plane001, plane002, plane003 ... will be created.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; imslice datacube plane 3
  </pre></div>
  <p>
  2. Slice the list of 2-D images <span style="font-family: monospace;">"nite1,nite2,nite3"</span> into a list of 1-D images.
  A new list of images nite1001, nite1002, ..., nite2001, nite2002, ...,
  nite3001, nite3002 will be created.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; imslice nite1,nite2,nite3 nite1,nite2,nite3 2
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  If the image to be sliced is an image section, the images slices will
  refer to the section not the original image.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imstack, imcopy
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

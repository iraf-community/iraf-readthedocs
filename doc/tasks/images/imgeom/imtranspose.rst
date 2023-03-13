.. _imtranspose:

imtranspose: Transpose a list of 2-D images
===========================================

**Package: imgeom**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  imtranspose input output
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of images to be transposed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output transposed images. If the output image name is the same as
  the input image name then the output image will replace the input image.
  The number of output images must be the same as the number of input images.
  </dd>
  </dl>
  <dl id="l_len_blk">
  <dt><b>len_blk = 512</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='len_blk' Line='len_blk = 512' -->
  <dd>The one dimensional length of the transpose blocks.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Imtranspose transposes the list of images in input by interchanging
  their rows and columns and writing the results to images specified in
  output. The number of input and output images must be the same.
  </p>
  <p>
  The transpose is done in square blocks whose dimensions are equal <i>len_blk</i>.
  </p>
  <p>
  The imtranspose tasks can be used to perform counter-clockwise or
  clockwise ninety degree rotations by flipping the y or x axis respectively
  in the input image section specification.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To transpose an image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imtranspose image1 image2
  </pre></div>
  <p>
  2. To transpose an image in place:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imtranspose image1 image1
  </pre></div>
  <p>
  3. To rotate an image 90 degrees counter-clockwise and clockwise:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imtranspose image1[*,-*] image2
  
  cl&gt; imtranspose image1[-*,*] image2
  </pre></div>
  <p>
  3. To transpose a set of 3 images listed 1 per line in the file imlist to
  the new images trans001, trans002, and trans003:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imtranspose @imlist trans001,trans002,trans003
  </pre></div>
  <p>
  4. To transpose a set of images in place:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imtranspose frame* frame*
  </pre></div>
  <p>
  5. To rotate an image 90 degrees counter-clockwise in place:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imtranspose image[*,-*] image
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  It is currently not legal to transpose images with a wcs type of MULTISPEC.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

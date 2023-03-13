.. _blkavg:

blkavg: Block average or sum a list of N-D images
=================================================

**Package: imgeom**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  blkavg input output b1 b2 b3 b4 b5 b6 b7
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of images to be block averaged.  Image sections are allowed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output image names.  If the output image name is the same as the input
  image name then the block averaged image replaces the input image.
  </dd>
  </dl>
  <dl id="l_b1">
  <dt><b>b1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b1' Line='b1' -->
  <dd>The number of columns to be block averaged (dimension 1, or x).
  </dd>
  </dl>
  <dl id="l_b2">
  <dt><b>b2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b2' Line='b2' -->
  <dd>The number of lines to be block averaged (dimension 2, or y).
  </dd>
  </dl>
  <dl id="l_b3">
  <dt><b>b3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b3' Line='b3' -->
  <dd>The number of bands to be block averaged (dimension 3, or z).
  </dd>
  </dl>
  <dl id="l_b4">
  <dt><b>b4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b4' Line='b4' -->
  <dd>The number of pixels to be block averaged in dimension 4 (... etc. for b5-b7).
  </dd>
  </dl>
  <dl id="l_option">
  <dt><b>option = <span style="font-family: monospace;">"average"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='option' Line='option = "average"' -->
  <dd>Type of block average.  The choices are <span style="font-family: monospace;">"average"</span> and <span style="font-family: monospace;">"sum"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The list of input images are block averaged or summed to form the output images.
  The output image names are specified by the output list.  The number of
  output image names must be the same as the number of input images.
  An output image name may be the same
  as the corresponding input image in which case the block averaged image replaces
  the input image.  The last column, line, etc. of the output image may be
  a partial block.  The option parameter selects whether to block average
  or block sum.
  </p>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  <p>
  It requires approximately 10 cpu seconds to block average a 512 by 512
  short image by a factor of 8 in each direction (Vax 11/750 with fpa).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To block average a 2-d image in blocks of 2 by 3:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; blkavg imagein imageout 2 3
  </pre></div>
  <p>
  2. To block sum two 2-d images in blocks of 5 by 5:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; blkavg image1,image2 out1,out2 5 5 op=sum
  </pre></div>
  <p>
  3. To block average a 3-d image by 4 in x and y and 2 in z:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; blkavg imagein imageout 4 4 2
  </pre></div>
  <p>
  or
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; blkavg imagein imageout b1=4 b2=4 b3=2
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'TIMINGS' 'EXAMPLES'  -->
  

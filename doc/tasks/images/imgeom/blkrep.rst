.. _blkrep:

blkrep: Block replicate a list of N-D images
============================================

**Package: imgeom**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  blkrep input output b1 [b2 b3 b4 b5 b6 b7]
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of images to be block replicated.  Image sections are allowed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output image names.  If the output image name is the same as the input
  image name then the block replicated image replaces the input image.
  </dd>
  </dl>
  <dl id="l_b1">
  <dt><b>b1, b2, b3, b4, b5, b6, b7</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b1' Line='b1, b2, b3, b4, b5, b6, b7' -->
  <dd>Block replication factor for dimensions 1 - 7.  Only the block factors for
  the dimensions of the input image are required.  Dimension 1 is the column
  or x axis, dimension 2 is the line or y axis.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The list of input images are block replicated by the specified factors
  to form the output images.  The output image names are specified by the
  output list.  The number of output image names must be the same as the
  number of input images.  An output image name may be the same as the
  corresponding input image in which case the block averaged image
  replaces the input image.  Only the block factors for the dimensions
  of the input images are used.
  </p>
  <p>
  This task is a complement to <b>blkavg</b> which block averages or sums
  images.  Another related task is <b>magnify</b> which interpolates
  images to arbitrary sizes.  This task, however, is only applicable to
  two dimensional images with at least two pixels in each dimension.
  Finally, in conjunction with <b>imstack</b> a lower dimensional image
  can be replicated to higher dimensions.
  </p>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  <p>
  VAX 11/750 with FPA running UNIX 4.3BSD and IRAF V2.4:
  </p>
  <div class="highlight-default-notranslate"><pre>
       SIZE DATATYPE REPLICATION     CPU  CLOCK
        100    short           5    0.5s     1s
        100     real           5    0.5s     1s
    100x100    short         5x5    1.7s     5s
    100x100     real         5x5    2.1s     6s
  100x100x1     real       5x5x5    9.7s    33s
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <dl id="l_1">
  <dt><b>1.</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='1' Line='1.' -->
  <dd>To block replicate a 1D image in blocks of 3:
  <div class="highlight-default-notranslate"><pre>
  cl&gt; blkrep imagein imageout 3
  </pre></div>
  </dd>
  </dl>
  <dl id="l_2">
  <dt><b>2.</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='2' Line='2.' -->
  <dd>To block replicate a 2D image in blocks of 2 by 3:
  <div class="highlight-default-notranslate"><pre>
  cl&gt; blkrep imagein imageout 2 3
  </pre></div>
  </dd>
  </dl>
  <dl id="l_3">
  <dt><b>3.</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='3' Line='3.' -->
  <dd>To block replicate two 2D images in blocks of 5 by 5:
  <div class="highlight-default-notranslate"><pre>
  cl&gt; blkrep image1,image2 out1,out2 5 5
  </pre></div>
  </dd>
  </dl>
  <dl id="l_4">
  <dt><b>4.</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='4' Line='4.' -->
  <dd>To block replicate a 3D image in place by factors of 2:
  <div class="highlight-default-notranslate"><pre>
  cl&gt; blkrep image1 image1 2 2 2
  </pre></div>
  </dd>
  </dl>
  <dl id="l_5">
  <dt><b>5.</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='5' Line='5.' -->
  <dd>To smooth an image by block averaging and expanding by a factor of 2:
  <div class="highlight-default-notranslate"><pre>
  cl&gt; blkavg imagein imageout 2 2
  cl&gt; blkrep imageout imageout 2 2
  </pre></div>
  </dd>
  </dl>
  <dl id="l_6">
  <dt><b>6.</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='6' Line='6.' -->
  <dd>To take a 1D image and create a 2D image in which each line is the same:
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imstack image1d image2d
  cl&gt; blkrep image2d image2d 1 100
  </pre></div>
  </dd>
  </dl>
  <dl id="l_7">
  <dt><b>7.</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='7' Line='7.' -->
  <dd>To take a 1D image and create a 2D image in which each column is the same:
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imstack image1d image2d
  cl&gt; imtranspose image2d image2d
  cl&gt; blkrep image2d image2d 100 1
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  blkavg, imstack, magnify
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'TIMINGS' 'EXAMPLES' 'SEE ALSO'  -->
  

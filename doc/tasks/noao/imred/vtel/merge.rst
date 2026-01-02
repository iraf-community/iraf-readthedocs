.. _merge:

merge: Merge daily grams into a Carrington map.
===============================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  merge outimage outweight outabs outratio month day year
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_outimage">
  <dt><b>outimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outimage' Line='outimage' -->
  <dd>Name of output image.
  </dd>
  </dl>
  <dl id="l_outweight">
  <dt><b>outweight</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outweight' Line='outweight' -->
  <dd>Output image containing weights, number of pixels per pixel.
  </dd>
  </dl>
  <dl id="l_outabs">
  <dt><b>outabs</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outabs' Line='outabs' -->
  <dd>Output image containing the sums of the absolute values of the flux.
  Not used when merging 10830 maps.
  </dd>
  </dl>
  <dl id="l_outratio">
  <dt><b>outratio</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outratio' Line='outratio' -->
  <dd>Output image containing the ratio of outimage/outabs.
  Not used when merging 10830 maps.
  </dd>
  </dl>
  <dl id="l_month">
  <dt><b>month, day, year</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='month' Line='month, day, year' -->
  <dd>Date of the center of this Carrington rotation.
  </dd>
  </dl>
  <dl id="l_longout">
  <dt><b>longout = 180</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='longout' Line='longout = 180' -->
  <dd>Longitude of the center of this Carrington rotation.
  </dd>
  </dl>
  <dl id="l_mergelist">
  <dt><b>mergelist = <span style="font-family: monospace;">"mergelist"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mergelist' Line='mergelist = "mergelist"' -->
  <dd>File containing list of files to be merged.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Merge adds up daily synoptic grams to produce a Carrington rotation map.
  the input images are 180x180 and the output images are 360x180.  The input
  images are read from the file mergelist.  Merge then weights the input
  image as cos**4 in x where the center of the image corresponds to zero angle
  and the left and right edges of the image correspond to -90 and +90 degrees
  respectively. The input image consists of an unweighted <span style="font-family: monospace;">"data"</span> image,
  a weight image, and an absolute value image.  The summing is done on the
  <span style="font-family: monospace;">"data"</span> image, on the weight image, and on the absolute value image
  separately to produce three output images.  Finally the <span style="font-family: monospace;">"data"</span> image is
  divided by the absolute value image to produce a 4th output image.
  If 10830 data is being merged there are only two(2) images per day, the
  <span style="font-family: monospace;">"data"</span> image and the <span style="font-family: monospace;">"weight"</span> image.  Also there are only two(2) output images,
  the <span style="font-family: monospace;">"data"</span> merged image and the <span style="font-family: monospace;">"weights"</span> merged image.
  A note about the mergelist file, the three grams for each day must be stored
  in the following sequence (data, absolute value, weight) for magnetograms
  and the two grams for each day must be stored as (data, weight) for 10830.
  The filenames must be one file name per line in the mergelist and files
  for different days must be grouped together, for example mergelist might look
  like:
  </p>
  <div class="highlight-default-notranslate"><pre>
  MAG01                                  MAG01
  MAG01a                                 MAG01w
  MAG01w     for magnetograms or         MAG02      for 10830 grams
  MAG02                                  MAG02w
  MAG02a
  MAG02w
  </pre></div>
  <p>
  for merging only two days of data where the first day is MAG01 and the second
  is MAG02. The <span style="font-family: monospace;">'a'</span> extension stands for absolute value and the <span style="font-family: monospace;">'w'</span> for weights.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To merge a number of images on disk into output images called <span style="font-family: monospace;">"im"</span>,
  <span style="font-family: monospace;">"imweight"</span>, <span style="font-family: monospace;">"imabs"</span>, and <span style="font-family: monospace;">"imratio"</span>, where the date corresponding to the
  center of the Carrington map is 3/20/84 the command would be (magnetograms):
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; merge im imweight imabs imratio 3 20 84
  </pre></div>
  <p>
  The same command used for 10830 grams would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; merge im imweight 3 20 84
  </pre></div>
  <p>
  2. If you have the list of files to be merged listed in a file called <span style="font-family: monospace;">"mlist"</span>
  instead of <span style="font-family: monospace;">"mergelist"</span> the command would be modified to read:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; merge im imweight 3 20 84 mergelist="mlist"
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

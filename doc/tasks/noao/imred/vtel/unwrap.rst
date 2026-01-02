.. _unwrap:

unwrap: Remove effects of data wraparound on continuum scans.
=============================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  unwrap listin listout
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_listin">
  <dt><b>listin</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listin' Line='listin' -->
  <dd>List of images to unwrap, this is an IRAF template.
  </dd>
  </dl>
  <dl id="l_listout">
  <dt><b>listout</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listout' Line='listout' -->
  <dd>List of output images, this is an IRAF template.  If the output list
  is the same as the input list, the unwrapping is done in-place.
  </dd>
  </dl>
  <dl id="l_threshold1">
  <dt><b>threshold1 = 128</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold1' Line='threshold1 = 128' -->
  <dd>Data jump threshold for first unwrap pass.
  </dd>
  </dl>
  <dl id="l_wrapval1">
  <dt><b>wrapval1 = 256</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wrapval1' Line='wrapval1 = 256' -->
  <dd>Factor to multiply wrap value by for first unwrap pass.
  </dd>
  </dl>
  <dl id="l_threshold2">
  <dt><b>threshold2 = 128</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold2' Line='threshold2 = 128' -->
  <dd>Data jump threshold for second unwrap pass.
  </dd>
  </dl>
  <dl id="l_wrapval2">
  <dt><b>wrapval2 = 256</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wrapval2' Line='wrapval2 = 256' -->
  <dd>Factor to multiply wrap value by for second unwrap pass.
  </dd>
  </dl>
  <dl id="l_cstart">
  <dt><b>cstart = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cstart' Line='cstart = 2' -->
  <dd>Column of image to start unwrapping.  Columns are numbered from left to right.
  </dd>
  </dl>
  <dl id="l_step">
  <dt><b>step = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='step' Line='step = 5' -->
  <dd>Number of steps (1-5) to perform on image (unwrap1, difference, unwrap2,
  reconstruct, fixlines).
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>If set, program produces progress reports, etc.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Unwrap checks for binary wraparound in IRAF images.
  The algorithm consists of reading the image line by line, unwrapping
  each line, and writing the line out to another image.  The procedure
  for unwraping is a five step process.
  </p>
  <dl id="l_Step">
  <dt><b>Step one: unwrap1</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Step' Line='Step one: unwrap1' -->
  <dd>Unwrapping is accomplished by scanning the data line and looking for
  large jumps in the data values.  Large negative jumps are interpreted
  as data wrapping and large positive jumps are interpreted as data unwrapping.
  The program keeps track of the number of wraps, each data element in the
  array has wrapval1 * wrapnumber added.  This effectively unwraps an image
  in which the point to point variation in the data values is small compared
  to the variation caused by a binary wrap.
  </dd>
  </dl>
  <dl id="l_Step">
  <dt><b>Step two: difference</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Step' Line='Step two: difference' -->
  <dd>A difference image is produced from the above step one image by calculating
  the pixel to pixel difference between all of the pixels in the line.  The
  first column of the image is generally left intact so that the image can
  be reconstructed in a later step.  Step one often produces streaks in the
  image due to data variation large enough to mimic wrapping.  This step
  two difference image eliminates most of these streaks except for their
  point of origin, where the confusion occured.
  </dd>
  </dl>
  <dl id="l_Step">
  <dt><b>Step three: unwrap2</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Step' Line='Step three: unwrap2' -->
  <dd>This is the second unwrapping step.  The image is unwrapped as in step
  one using the second set of unwrap values (threshold2, wrapval2).
  </dd>
  </dl>
  <dl id="l_Step">
  <dt><b>Step four: reconstruct</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Step' Line='Step four: reconstruct' -->
  <dd>The original image is reconstructed from the step three image by
  adding pixel values successively to line pixels.
  </dd>
  </dl>
  <dl id="l_Step">
  <dt><b>Step five: fixlines</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Step' Line='Step five: fixlines' -->
  <dd>If bad lines (streaks) still can be found in the image, they are
  eliminated by replacing the line by the average of the lines above
  and below bad line.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To unwrap an image called <span style="font-family: monospace;">"continuum"</span> and store the resulting image in
  <span style="font-family: monospace;">"unwrapped"</span>, and use the default parameters, the command might be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; unwrap continuum unwrapped
  </pre></div>
  <p>
  2. To unwrap all the images in the directory starting with s1492 and store
  the unwrapped images in s1492*u, to start in column 31, to do four steps,
  and to see verbose output, the command might be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; unwrap s1494* s1492*//u cstart=31 step=4 v+
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

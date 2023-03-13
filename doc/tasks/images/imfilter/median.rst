.. _median:

median: Median box filter a list of 1D or 2D images
===================================================

**Package: imfilter**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  median input output xwindow ywindow
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of filtered images. The number of input images must be the same as
  the number of output images. If the input image name is the same as the
  output image name the original image is replaced by the filtered image.
  </dd>
  </dl>
  <dl id="l_xwindow">
  <dt><b>xwindow, ywindow</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xwindow' Line='xwindow, ywindow' -->
  <dd>The size of the median filter. Xwindow and ywindow are assumed to be
  odd integers. If either xwindow or ywindow are even they will be rounded
  up to the nearest odd integer.
  </dd>
  </dl>
  <dl id="l_zloreject">
  <dt><b>zloreject = INDEF, zhireject = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zloreject' Line='zloreject = INDEF, zhireject = INDEF' -->
  <dd>The minimum and maximum good pixel values. Zloreject and zhireject default to 
  -MAX_REAL and MAX_REAL respectively.
  </dd>
  </dl>
  <dl id="l_boundary">
  <dt><b>boundary = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary' Line='boundary = "nearest"' -->
  <dd>The type of boundary extension. The options are:
  <dl>
  <dt><b>nearest</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nearest' Line='nearest' -->
  <dd>Use the value of the nearest boundary pixel.
  </dd>
  </dl>
  <dl>
  <dt><b>constant</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='constant' Line='constant' -->
  <dd>Use a constant value.
  </dd>
  </dl>
  <dl>
  <dt><b>reflect</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='reflect' Line='reflect' -->
  <dd>Reflect pixel values around the boundary.
  </dd>
  </dl>
  <dl>
  <dt><b>wrap</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='wrap' Line='wrap' -->
  <dd>Wrap pixel values around the boundary.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_constant">
  <dt><b>constant = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constant' Line='constant = 0.' -->
  <dd>The value for constant value boundary extension.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MEDIAN takes a list of input images <i>input</i> and produces a set of filtered
  output images <i>output</i>. The median filter consists of a sliding
  rectangular window  of dimensions <i>xwindow</i>
  by <i>ywindow</i>. The center pixel in the window is replaced by the median
  of all the pixels in the
  window, where the median of a sequence of numbers is defined to be  the value
  of the (n + 1) /2 pixel.  If even the window dimensions are rounded up
  to odd integers.  Out of bounds
  pixel references are handled by setting the parameter <i>boundary</i>.
  </p>
  <p>
  The <i>zloreject</i> and <i>zhireject</i> parameters may be used to reject
  bad data from the median filtering box. If no good 
  data is left in the filtering box, the median is set to zloreject
  if the majority of the pixels are less than zloreject, or to zhireject
  if the majority of pixels are greater than zhireject.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Median filter an image using a 5 by 5 window and nearest pixel boundary
  extension.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; median m74 m74.5by5 5 5
  </pre></div>
  <p>
  2. Median filter an image using a 3 by 3 window and constant boundary extension.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; median m74 m74.5by5 3 3 boun=const const=0.
  </pre></div>
  <p>
  3. Median filter the test image dev$pix, removing all pixels less than 5 or
  greater than 19935 from the filtering box.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; median dev$pix pix77 7 7 zlo=5 zhi=19935
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  Median requires approximately 11 and 19 CPU seconds to filter a 512 by
  512 integer image using a 5 by 5 and 7 by 7 filter window respectively
  (SPARCStation2).
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The sort routine for the smaller kernels has been optimized. It may be
  desirable to optimize higher order kernels in future.
  </p>
  <p>
  The IRAF task FMEDIAN is significantly more efficient than MEDIAN
  and should be used if the image is integer or can be quantized without
  significant loss of precision. 
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fmedian, rmedian, frmedian
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

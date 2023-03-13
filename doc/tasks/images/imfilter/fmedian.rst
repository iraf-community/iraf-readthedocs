.. _fmedian:

fmedian: Quantize and box median filter a list of 1D or 2D images
=================================================================

**Package: imfilter**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fmedian input output xwindow ywindow
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
  <dd>List of output filtered images. The number of input images must be the
  same as the number of output images. If the input image name equals the output
  image name the filtered image replaces the original image.
  </dd>
  </dl>
  <dl id="l_xwindow">
  <dt><b>xwindow, ywindow</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xwindow' Line='xwindow, ywindow' -->
  <dd>The size of the box median filter. Xwindow and ywindow must be odd.
  Even values for xwindow or ywindow will be rounded up to the
  nearest odd integer.
  </dd>
  </dl>
  <dl id="l_hmin">
  <dt><b>hmin = -32768, hmax = 32767</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hmin' Line='hmin = -32768, hmax = 32767' -->
  <dd>The histogram quantization parameters. Hmin and hmax define the minimum
  and maximum permitted values for the integer representation of the input image.
  The default values are appropriate for the 16 bit twos complement data values
  produced by current CCDs. Hmin and hmax should be chosen so as to
  minimize the space required to store the image histogram.
  </dd>
  </dl>
  <dl id="l_zmin">
  <dt><b>zmin = INDEF, zmax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zmin' Line='zmin = INDEF, zmax = INDEF' -->
  <dd>The data quantization parameters. Zmin and zmax default to the minimum and
  maximum pixel values in the input image. Pixel values from zmin to zmax are
  linearly mapped to integer values from hmin to hmax. If zmin = hmin and
  zmax = hmax, the image pixels are converted directly to integers.
  Image values less than or greater than
  zmin or zmax will default to hmin and hmax respectively.
  </dd>
  </dl>
  <dl id="l_zloreject">
  <dt><b>zloreject = INDEF, zhireject = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zloreject' Line='zloreject = INDEF, zhireject = INDEF' -->
  <dd>The minimum and maximum good pixel values. Zloreject and zhireject default
  to zmin and zmax in the input data or equivalently to hmin and hmax in the
  integer representation of the input image.
  </dd>
  </dl>
  <dl id="l_unmap">
  <dt><b>unmap = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='unmap' Line='unmap = yes' -->
  <dd>Fmedian rescales the integer values to numbers between zmin and zmax
  by default. If the user wishes to preserve the median of the quantized
  images the unmap parameter should be set to no.
  </dd>
  </dl>
  <dl id="l_boundary">
  <dt><b>boundary = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary' Line='boundary = "nearest"' -->
  <dd>The type of boundary extension. The options are:
  <dl>
  <dt><b>nearest</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nearest' Line='nearest' -->
  <dd>Use the value of the nearest pixel.
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
  <dd>The value for constant valued boundary extension.
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
  FMEDIAN takes a list of input images <i>input</i> and produces a set of filtered
  output images <i>output</i>. The filter consists of a sliding rectangular
  <i>xwindow</i> by <i>ywindow</i> window whose function is to replace the 
  center pixel in the window with the median of the pixels in the
  window.  The median of a sequence of numbers is defined to be
  the value of the (n + 1) / 2 pixel in the ordered sequence.
  Out-of-bounds pixel references are handled by setting the parameter
  <i>boundary</i>.
  </p>
  <p>
  If <i>zmin</i> = <i>hmin</i> and <i>zmax</i> = <i>hmax</i>,
  FMEDIAN converts the image pixels directly to
  integers.  This operation may result in truncation of the pixel values
  if the input image is not an integer image. Otherwise the
  input pixel values from zmin to zmax are linearly mapped to integer
  values from hmin to hmax. The histogram, median, and number of pixels less
  than the median, are computed for the first window position. These
  quantities are updated as the median filter moves one position.
  The <i>unmap</i> parameter is normally set so as to restore the output
  pixel values to the range defined by zmin and zmax, but may be turned off
  if the user wishes to examine the quantized pixels. The precision of the
  median in integer space and pixel space is 1.0 and  
  (zmax - zmin) / (hmax - hmin) respectively.
  </p>
  <p>
  The <i>zloreject</i> and <i>zhireject</i> parameters may be used to
  reject bad data from the median filtering box. If no good 
  data is left in a give filtering box, then the median is set to zloreject
  if the majority of the pixels are less than zloreject, or to zhireject
  if the majority of pixels are greater than zhireject.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  A description of the fast median algorithm used here can be found in
  <span style="font-family: monospace;">"Topics in Applied Physics: Two-Dimensional Digital Signal Processing II:
  Transforms and Median Filters"</span>, Volume 43, 1981, Springer-Verlag,
  edited by T.S. Huang, p 209.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Median filter a 16 bit CCD image using a 5 by 5 window.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; fmedian input output 5 5 hmin=-32768 hmax=32767 \
  &gt;&gt;&gt; zmin=-32768.  zmax=32767.
  </pre></div>
  <p>
  2. Median filter a KPNO PDS image using a 3 by 3 window.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; fmedian input output 3 3 hmin=0 hmax=4095 zmin=0. zmax=4095.
  </pre></div>
  <p>
  3. Median filter an 8 bit image using a 3 by 3 window.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; fmedian input output 3 3 hmin=0 hmax=255 zmin=0. zmax=255.
  </pre></div>
  <p>
  4. Median filter an image with real values from 0.0 to 1.0 with a precision
  of .003 and leave the output pixels in integer format.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; fmedian input output 5 5 unmap- hmin=0 hmax=1000 zmin=0. \
  &gt;&gt;&gt; zmax=1.
  </pre></div>
  <p>
  5. Median filter the test image dev$pix rejecting any pixels &lt; 5 or
  greater than 19935 from the medianing process.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; fmedian dev$pix output 5 5 hmin=-1 hmax=20000 zmin=-1.0 \
  &gt;&gt;&gt; zmax=20000 zloreject=5 zhireject=20000
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  It requires approximately 4.5 and 5.8 CPU seconds to median filter an
  512 by 512 square integer image with a 5 by 5 and 7 by 7 window respectively.
  (SPARCStation2).
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  This technique is most suitable for integer data or data which has not
  been calibrated. For non-integer data the calculated median may be an
  approximation, not an exact pixel value.
  </p>
  <p>
  If the  dynamic range of the data defined by hmin and hmax is large the
  memory requirements can become very large.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  median, frmedian
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'REFERENCES' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

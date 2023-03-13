.. _frmode:

frmode: Quantize and ring modal filter a list of 1D or 2D images
================================================================

**Package: imfilter**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  frmode input output rinner router
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
  <dd>List of filtered images. The number of input images must be the same as the
  number of output images. If the input image name equals the output image name
  the filtered image replaces the original image.
  </dd>
  </dl>
  <dl id="l_rinner">
  <dt><b>rinner, router</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rinner' Line='rinner, router' -->
  <dd>The inner and outer semi-major axes of the ring filter in pixels. If rinner
  is set to 0.0 then the ring filter becomes a circular filter.
  </dd>
  </dl>
  <dl id="l_ratio">
  <dt><b>ratio = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ratio' Line='ratio = 1.0' -->
  <dd>The ratio of the semi-minor axis to the semi-major axis of the ring filter.
  If ratio is 1.0 the ring filter is circularly symmetric.
  </dd>
  </dl>
  <dl id="l_theta">
  <dt><b>theta = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='theta' Line='theta = 0.0' -->
  <dd>The position angle of the major axis of the ring filter. Theta is measured
  in degrees counter-clockwise from the x axis and must be between 0 and 180
  degrees.
  </dd>
  </dl>
  <dl id="l_hmin">
  <dt><b>hmin = -32768, hmax = 32767</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hmin' Line='hmin = -32768, hmax = 32767' -->
  <dd>The histogram quantization parameters. Hmin and hmax define the minimum
  and maximum permitted values for the integer representation of the input image.
  The default values are those suitable for the 16 bit twos complement data
  produced by current CCDs. Hmin and hmax should be chosen so as to
  minimize the space required to store the image histogram.
  </dd>
  </dl>
  <dl id="l_zmin">
  <dt><b>zmin = INDEF, zmax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zmin' Line='zmin = INDEF, zmax = INDEF' -->
  <dd>The data quantization parameters. Zmin and zmax default to the minimum and
  maximum pixel values in the input image. Pixel values from zmin to zmax
  are linearly mapped to integers from hmin to hmax.
  If zmin = hmin and zmax = hmax, the image pixels are converted directly to
  integers.  Image values less than or greater than
  zmin or zmax will default to hmin and hmax respectively.
  </dd>
  </dl>
  <dl id="l_zloreject">
  <dt><b>zloreject = INDEF, zhireject = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zloreject' Line='zloreject = INDEF, zhireject = INDEF' -->
  <dd>The minimum and maximum good pixel values. Zloreject and zhireject default
  to zmin and zmax in the input data or hmin and hmax in the integer
  representation of the input image.
  </dd>
  </dl>
  <dl id="l_unmap">
  <dt><b>unmap = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='unmap' Line='unmap = yes' -->
  <dd>Frmode rescales the integer values to numbers between zmin and zmax
  by default. If the user wishes to preserve the mode of the quantized images,
  the <i>unmap</i> parameter should be set to no.
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
  FRMODE takes a list of input images <i>input</i> and produces a set of filtered
  output images <i>output</i>. The filter consists of a sliding 
  circular / elliptical or annular circular / elliptical window whose size
  and orientation is determined by the <i>rinner</i>, <i>router</i>, <i>ratio</i>,
  and <i>theta</i> parameters.  The center pixel of the window is replaced by
  the mode of the pixels in the window, where the mode is defined as follows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  mode = 3. * median - 2. * mean
  </pre></div>
  <p>
  The median of a sequence of numbers is defined to be the value of the
  (n + 1) / 2 number in the ordered sequence. Out of bounds pixel references
  are handled by setting the parameter boundary. The principal function of
  the circular / elliptical filters is to smooth an image using a 
  circularly / elliptically symmetric filter. The principal function of the
  circular / elliptical ring filter is to remove objects from the image
  which have a scale length or rinner and replace them with an estimate of
  the local background value.
  </p>
  <p>
  If <i>zmin</i> = <i>hmin</i> and <i>zmax</i> = <i>hmax</i>,
  FRMODE converts the image pixels directly to integers.
  This operation may result in truncation of the pixel values of the
  input image is not an integer image.
  Otherwise the input image values from zmin to zmax are linearly mapped to
  integer values from hmin to hmax.
  The histogram, median, and number of pixels less
  than the median are computed for the first window position. These
  quantities are updated as the median filter moves one position and
  the mode is computed.  The <i>unmap</i> parameter is normally set
  so as to restore the output pixel values to the range defined by
  zmin and zmax, but may be turned off if the user wishes to
  examine the quantized pixels.
  The precision of the mode in integer space and pixel space
  is 1.0 and (zmax - zmin) / (hmax - hmin) respectively.
  </p>
  <p>
  The <i>zloreject</i> and <i>zhireject</i> parameters may be used to reject
  bad data from the modal filtering box.  If no good
  data is left in the filtering box, then the mode is set to zloreject
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
  edited by T.S. Huang, page 209.
  </p>
  <p>
  The properties of the ring median filter and its application to
  astronomical data analysis problems is summarized in the
  article <span style="font-family: monospace;">"A Ring Median Filter  for Digital Images"</span> (Secker, J., 1995,
  PASP, 107, 496-501) and references therein.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Modal filter a 16 bit CCD image using a circular ring filter with an
  inner radius of 4 pixels and a width of 1 pixel.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; frmode input output 4.0 5.0 hmin=-32768 hmax=32767 zmin=-32768. \
  &gt;&gt;&gt; zmax=32767.
  </pre></div>
  <p>
  2. Modal filter a KPNO PDS image using a circular filter of outer radius
  3.0.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; frmode input output 0.0 3.0 hmin=0 hmax=4095 zmin=0. zmax=4095.
  </pre></div>
  <p>
  3. Modal filter an 8 bit image using the same filter as example 2.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; frmode input output 0.0 3.0 hmin=0 hmax=255 zmin=0. zmax=255.
  </pre></div>
  <p>
  4. Modal filter an image with real values from 0.0 to 1.0 with a precision
  of .003 and leave the output pixels in integer format. Use a ring filter
  of inner radius 5.0 and width 0.5 pixels.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; frmode input output 5.0 0.5 unmap- hmin=0 hmax=1000 zmin=0. \
  &gt;&gt;&gt; zmax=1.
  </pre></div>
  <p>
  5. Modal filter the test image dev$pix rejecting any pixels &lt; 5 or
  greater than 19935 from the mode computing process using a circular
  filter of outer radius 5.0.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; frmode dev$pix output 0.0 5.0 hmin=-1 hmax=20000 zmin=-1.0 \
  &gt;&gt;&gt; zmax=20000 zloreject=5 zhireject=20000
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  It requires approximately 39 and 27 CPU seconds to modal filter a
  512 by 512 square integer image with a circular filter of radius 5 pixels
  and a ring filter of inner and outer radii of 4.0 and 5.0 pixels
  respectively (SPARCStation2).
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  This technique is most suitable for integer data and data which has not
  been calibrated. For non-integer data the calculated median is an
  approximation only.
  </p>
  <p>
  If the  dynamic range of the data defined by hmin and hmax is large the
  memory requirements can become very large.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mode, rmode, fmode
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'REFERENCES' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

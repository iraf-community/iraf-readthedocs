.. _rmode:

rmode: Ring modal filter a list of 1D or 2D images
==================================================

**Package: imfilter**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rmode input output rinner router
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
  counter-clockwise in degrees from the x axis and must be between 0 and
  180 degrees.
  </dd>
  </dl>
  <dl id="l_zloreject">
  <dt><b>zloreject = INDEF, zhireject = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zloreject' Line='zloreject = INDEF, zhireject = INDEF' -->
  <dd>The minimum and maximum good pixel values. Zloreject and zhireject default
  to  -MAX_REAL and MAX_REAL respectively.
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
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  RMODE takes a list of input images <i>input</i> and produces a list of
  filtered
  images <i>output</i>. The filter consists of a sliding circular / elliptical or
  annular circular / elliptical window whose size and orientation is determined
  by the <i>rinner</i>, <i>router</i>, <i>ratio</i>, and <i>theta</i> parameters.
  The center pixel in the window is replaced by the mode of the pixel
  distribution where mode is defined below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  mode = 3. * median - 2. * mean
  </pre></div>
  <p>
  The median is defined as the value of the (n + 1) / 2 number in an ordered
  sequence of numbers.
  Out of bounds pixel references are handled by setting the parameter
  <i>boundary</i>. The principal function of the circular / elliptical filter
  is to smooth and image using a circularly / elliptically symmetric filter.
  The principal function of the circular / elliptical ring filter is to
  remove objects from the image which have a scale length of rinner and
  replace them with an estimate of the local background value.
  </p>
  <p>
  The <i>zloreject</i> and <i>zhireject</i> parameters may be used to reject
  bad data from the modal filtering box.  If no good
  data is left in a given filtering box, then the mode is set to zloreject
  if the majority of the pixels are less than zloreject, or to zhireject
  if the majority of pixels are greater than zhireject.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  The properties of the ring median filter and its application to
  astronomical analysis problems is summarized in the
  article <span style="font-family: monospace;">"A Ring Median Filter  for Digital Images"</span> (Secker, J., 1995,
  PASP, 107, 496-501) and references therein.
  </p>
  <p>
  A derivation of the expression for the mode used here can be found in
  <span style="font-family: monospace;">"Statistics in Theory and Practice"</span>, Robert Lupton, 1993, Princeton
  University Press, problem 2.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Modal filter an image using a circular ring filter with an inner radius
  of 4 pixels and a width of 1 pixel.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rmode input output 4.0 5.0
  </pre></div>
  <p>
  2. Modal filter an image using a circular filter of outer radius 3.0.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rmode input output 0.0 3.0
  </pre></div>
  <p>
  3. Modal filter the test image dev$pix rejecting any pixels &lt; 5 or
  greater than 19935 from the modal filter using a circular
  filter of outer radius 5.0.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; rmode dev$pix output 0.0 5.0 zloreject=5 zhireject=19935
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  It requires approximately 59 and 35 CPU seconds to modal filter a
  512 by 512 square integer image with a circular filter of radius 5 pixels
  and a ring filter of inner and outer radii of 4.0 and 5.0 pixels respectively.
  (SPARCStation2).
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mode,fmode,rmode
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'REFERENCES' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _bscale:

bscale: Linearly transform the intensities of a list of images
==============================================================

**Package: proto**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  bscale input output 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input ' -->
  <dd>List of images to be transformed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output transformed images. If the output list is the same as the input
  list the input images are overwritten.
  </dd>
  </dl>
  <dl id="l_bzero">
  <dt><b>bzero = <span style="font-family: monospace;">"0."</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bzero' Line='bzero = "0."' -->
  <dd>The zero point to be subtracted before applying the scale factor.
  The options are a numerical value, <span style="font-family: monospace;">"mean"</span>, <span style="font-family: monospace;">"median"</span>, or <span style="font-family: monospace;">"mode"</span>.
  </dd>
  </dl>
  <dl id="l_bscale">
  <dt><b>bscale = <span style="font-family: monospace;">"1."</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bscale' Line='bscale = "1."' -->
  <dd>The scale factor to be applied.  The options are a numerical value,
  <span style="font-family: monospace;">"mean"</span>, <span style="font-family: monospace;">"median"</span>, or <span style="font-family: monospace;">"mode"</span>.
  </dd>
  </dl>
  <dl id="l_section">
  <dt><b>section = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='section' Line='section = ""' -->
  <dd>The image section to be used for computing the image statistics.  If section
  is <span style="font-family: monospace;">""</span>, <i>step</i> is used to define the default image section. <i>Section</i>
  is used to confine the computation of the mean, median, and mode
  to a specific region of the image.
  </dd>
  </dl>
  <dl id="l_step">
  <dt><b>step = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='step' Line='step = 10' -->
  <dd>The step size in pixels which defines the default image section to be used
  for computing the mean, median, and mode.
  In image section notation the default section is equivalent to [*:10,*:10,...].
  <i>Step</i> is used if
  the sampling along an axis is not defined by <i>section</i>.
  Subsampling can significantly reduce the memory and 
  time required for the computation of the mean, median, and mode.
  </dd>
  </dl>
  <dl id="l_upper">
  <dt><b>upper = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='upper' Line='upper = "INDEF"' -->
  <dd>Upper intensity limit to be used for computing the mean, median, and mode.
  </dd>
  </dl>
  <dl id="l_lower">
  <dt><b>lower = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lower' Line='lower = "INDEF"' -->
  <dd>Lower intensity limit to be used for computing the mean, median, and mode.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about actions taken by the task?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The specified input images <i>input</i>  are linearly transformed in intensity
  and written to the list of output images <i>output</i>, using the
  zero point specified by <i>bzero</i> and the scale factor specified by
  <i>bscale</i>.  If the output image list
  is the same as the input image list the input images will be overwritten.
  </p>
  <p>
  The expression defining the linear transformation is listed below.
  </p>
  <p>
  	NEW = (OLD - BZERO) / BSCALE
  </p>
  <p>
  OLD is the input pixel brightness, NEW is the output
  pixel brightness, BZERO is the zero point offset, and BSCALE is the
  scale factor.  The values of the scaling parameters <i>bzero</i> and
  <i>bscale</i>
  may be specified explicitly or the mean, median, or mode of the image
  may be used for either quantity.  If the input image pixel type
  is short, integer, or long, overflow or truncation may occur.
  </p>
  <p>
  When one of the scaling parameters is the image mean, median,
  or mode, then the image mean, median, and mode are calculated. The statistics
  computation can be restricted to a section of the input image by setting
  the parameter
  <i>section</i>. Otherwise the parameter <i>step</i> is used to
  define a default image section.
  Subsampling the image can significantly reduce the memory
  and time requirements for computing the statistics of large images.
  If numerical values for both the scaling parameters are specified, then
  the image statistics are not computed. The statistics computation can
  be limited to given intensity range by setting the parameters
  <i>lower</i> and <i>upper</i>.
  </p>
  <p>
  The mean, median, and mode are computed using the following algorithm.
  Note that this algorithm requires that all the data to used for computing
  the statistics must be in memory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  1. The data in the specified image section is read into a buffer.
  2. The data is sorted in increasing order of intensity.
  3. The points outside upper and lower are excluded.
  4. The median is set to the data value at the midpoint of the remaining
     data.
  5. The mean and sigma of the remaining data are computed.
  6. The histogram bin width (.1*sigma)  and separation (.01*sigma) are
     computed.
  7. The location of the bin containing the most data points is determined.
  8. The median of the data values in that bin is used to estimate the mode.
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Use the mode to subtract a constant background from a list of images.
  Overwrite the input images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bscale *.imh *.imh bzero=mode
  </pre></div>
  <p>
  2. Scale a list of images to a unit mean. Overwrite the input images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bscale *.imh *.imh bscale=mean
  </pre></div>
  <p>
  3. Scale a list of images to the intensity range 0 to 511,
  where 234. and 1243. are the original data range. Overwrite the input
  images. This example uses the CL to calculate bscale.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bscale.bzero = 234.
  cl&gt; bscale.bscale = (1243. - 234.) / 512.
  cl&gt; bscale *.imh *.imh
  </pre></div>
  <p>
  4. Scale an image using a user specified bzero and bscale and create a new
  output image: 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bscale imagein imageout bzero=0.0 bscale=1.10
  </pre></div>
  <p>
  5. Median subtract a list of input images using the percent replace facility to
  create the output image names.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bscale images*.imh %i%outi%*.imh bzero=median bscale=1.0
  </pre></div>
  <p>
  6. Repeat the previous example but use the @ file facility for specifying
  the input and output image lists.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bscale @infile @outfile bzero=median bscale=1.0
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imarith,imcombine
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

.. _runmed:

runmed: Running median a list of images at each pixel position
==============================================================

**Package: imfilter**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  runmed input output window
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images.  The list is used in the order provided without
  sorting.  All images must be the same dimensionality and size.  There must
  be at least three images.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output images. The number of output images must be the same as
  the number of input images.  If the input image name is the same as the
  output image name the original image is replaced by the filtered image.
  </dd>
  </dl>
  <dl id="l_window">
  <dt><b>window</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='window' Line='window' -->
  <dd>Number of images for the running window.  This must be at least three, and
  less than or equal to the number of images in the input list.
  </dd>
  </dl>
  <dl id="l_masks">
  <dt><b>masks = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='masks' Line='masks = ""' -->
  <dd>List of output masks indicating the number of pixels used in calculating the
  filter value.  If specified the list must match the output list.
  </dd>
  </dl>
  <dl id="l_inmaskkey">
  <dt><b>inmaskkey = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inmaskkey' Line='inmaskkey = ""' -->
  <dd>Keyword in the input image containing a maskname for selecting or ignoring
  pixels.  Pixels to be used are selected by zero values in the mask.
  </dd>
  </dl>
  <dl id="l_outmaskkey">
  <dt><b>outmaskkey = <span style="font-family: monospace;">"HOLES"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outmaskkey' Line='outmaskkey = "HOLES"' -->
  <dd>Keyword in the output image to containing the name of the output mask.
  If no output mask is created or if no keyword is specified then the
  keyword is not added or replaced in the output image.
  </dd>
  </dl>
  <dl id="l_outtype">
  <dt><b>outtype = <span style="font-family: monospace;">"filter"</span> (filter|difference|ratio)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtype' Line='outtype = "filter" (filter|difference|ratio)' -->
  <dd>The type of output values in the images.  The choices are <span style="font-family: monospace;">"filter"</span> for
  the filter value, <span style="font-family: monospace;">"difference"</span> for the difference of the input and
  filter value (input-filter), and <span style="font-family: monospace;">"ratio"</span> for the ratio of the input
  and filter value (input/filter).
  </dd>
  </dl>
  <dl id="l_exclude">
  <dt><b>exclude = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exclude' Line='exclude = no' -->
  <dd>Exclude the input image from the filter.
  </dd>
  </dl>
  <dl id="l_nclip">
  <dt><b>nclip = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nclip' Line='nclip = 0.' -->
  <dd>This parameter allows clipping high values from the median calculation.
  The value multiples the difference between the median and the lowest value
  and rejects values that exceed the median by this amount.  The is done
  after scaling, mask rejections, and image exclusion.
  </dd>
  </dl>
  <dl id="l_navg">
  <dt><b>navg = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='navg' Line='navg = 1' -->
  <dd>Number of central values to average.  A value of 1 is used to compute
  the median.
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = <span style="font-family: monospace;">"none"</span> (none|mode|!&lt;keyword&gt;|@&lt;file&gt;)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = "none" (none|mode|!&lt;keyword&gt;|@&lt;file&gt;)' -->
  <dd>Scale the images with the specified method.  The choices are
  <span style="font-family: monospace;">"none"</span>, <span style="font-family: monospace;">"mode"</span> to compute a mode for each image and divide by the value,
  <span style="font-family: monospace;">"!&lt;keyword&gt;"</span> to find the value to multiple the image from the specified
  keyword in the header, and <span style="font-family: monospace;">"@&lt;file&gt;"</span> to get the values to multiple the
  images from the specified file.  The scales are normalized by the scale
  for the first image to make the scaling relative to the first image.
  The values in a file must be in the same order as the input images.
  </dd>
  </dl>
  <dl id="l_normscale">
  <dt><b>normscale = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='normscale' Line='normscale = yes' -->
  <dd>Normalize the scales to the first image scale?
  </dd>
  </dl>
  <dl id="l_outscale">
  <dt><b>outscale = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outscale' Line='outscale = yes' -->
  <dd>Scale output images?  If yes the output images will be on the system
  defined by the input scale factors.  If no the output is scaled back
  to match the input levels.
  </dd>
  </dl>
  <dl id="l_blank">
  <dt><b>blank = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blank' Line='blank = 0' -->
  <dd>Filter value when all data have been excluded from the calculation.
  </dd>
  </dl>
  <dl id="l_storetype">
  <dt><b>storetype = <span style="font-family: monospace;">"real"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='storetype' Line='storetype = "real"' -->
  <dd>Internal storage type which may be <span style="font-family: monospace;">"real"</span> or <span style="font-family: monospace;">"short"</span>.  The short
  integer type saves memory at the cost of rounding.  Unless memory
  is a problem real storage is recommended.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print progress information to the standard output.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>RUNMED</b> takes a list of input images (<i>input</i>) and produces
  a set of filtered output images (<i>output</i>).  The output images
  are matched with the input images and the header of the output image
  is that of the matching input image.  The output image may be the
  same as the input image if desired.
  </p>
  <p>
  Each input image may have an associated pixel mask.  The mask is specified
  by the keyword in the image specified by the <i>inmaskkey</i> parameter.
  The masks must be of a matching size.  This task matches mask pixel with
  image pixels based on the logical pixel coordinates.  In other words, it
  does not take into account any subsection that may have been applied to the
  input images which was not also applied to the mask images.  A non-zero
  mask value identifies pixels to be excluded from the computation of the
  filter value or the mode of the image.
  </p>
  <p>
  The input images may be scaled (<i>scale</i>) as they are read.
  The scale factors may be normalized relative to the first image in the
  list (<i>normscale</i>).  The scale factors may be given explicitly in a
  file or keyword or computed from an estimate of the mode of the image.
  The mode computation excludes pixels identified by non-zero values in
  the associated input mask.  On output the computed filter value based
  on the set of scaled pixel values maybe scaled back to match that of
  the input image (<i>outscale</i>).
  </p>
  <p>
  The running filter operates independently on the sequence of pixel
  values across the list of input images at each pixel position.  If an
  input mask is specified then non-zero mask values identify pixel values
  to exclude from the calculations.  The <i>exclude</i> parameter may be
  used to exclude the central image of the window.  This is useful to
  avoid unnatural histograms with a spike at for the output image.
  The filter sorts the sequence of unrejected values in a running window
  (<i>window</i>).
  </p>
  <p>
  The median is the central value when the number of unrejected values is
  odd and the average of the two central values.  This median may be used
  with the <i>nclip</i> parameter to exclude high outliers in the sorted
  values at each point.  The clipping computes the difference between
  the median and the lowest value, multiplies by the clipping factor,
  and rejects values more than this threshold above the median.  This is
  only done when <i>nclip</i> is greater than zero and there are at least
  3 unrejected values prior to this clipping step.
  </p>
  <p>
  After the clipping the average, as set by <i>navg</i>, of the central values
  is computed.  Note that an average of one is a median.
  </p>
  <p>
  The number of central values averaged will be even when the number of
  pixels is even and odd when it is odd.  What is done is that high
  and low values are excluded symmetrically until the number of remaining
  pixels is less than or equal to the specified average but with at least
  one or two values remaining.
  </p>
  <p>
  The number of values available to the average is odd when no data is
  excluded because the window size must be odd.  When the <i>exclude</i>
  parameter is selected the number of values will be even.  And when pixel
  masks are used the number be anywhere from zero to the window size.
  When all pixels are excluded the filter value is the <i>blank</i> value.
  Also when the ratio output is selected and the filter value used as the
  denominator is zero the <i>blank</i> value is also used.
  </p>
  <p>
  The output of this task are images of the filter values
  (<i>outtype</i>=<span style="font-family: monospace;">"filter"</span>), the difference of the input image and the
  filter value (<i>outtype</i>=<span style="font-family: monospace;">"difference"</span>), or the ratio of the input
  image and the filter value (<i>outtype</i>=<span style="font-family: monospace;">"ratio"</span>).  The difference
  output is useful as a background subtraction for a background that varies
  systematically through the list of images.  When the difference
  is selected the input and filter value are matched by their scale factors
  either in the scaled system (<i>outscale</i>=yes) or in the input
  system (<i>outscale</i>=no).
  </p>
  <p>
  The <i>exclude</i> option is useful for the background subtraction case.
  Use of this option excludes the input image from the to the filter
  computation value for the matching output.  This insures that the output
  pixel value histogram does not have a spike of zero values when <i>navg</i>
  = 1 and the median pixel value is that of the input image.
  </p>
  <p>
  An output mask list (<i>masks</i>) may be specified to produce masks which
  contain the number of pixels used in computing the filter value.  This
  is most useful to define regions where no pixels were used and the
  blank value was substituted.  The name of the output mask is recorded
  in the output image header under the keyword specified by the
  <i>outmaskkey</i> parameter.  Note that it is valid to specify the
  output mask keyword to be the same as the input mask keyword.  If this
  is not done the input mask keyword, if present, will remain in the
  output header.
  </p>
  <p>
  Normally the filter window is centered on each input image within the list.
  In other words there are an equal number of images before and after the
  input image taken from the input list.  However, at the beginning and end
  of the input list, the window spans the first or last <i>window</i> images.
  The filter value will then be the same except that the <i>exclude</i>
  option applies to the particular input image and the difference and
  ratio output types will be based on the particular input image.
  </p>
  <p>
  This task is designed to be as efficient as possible so that images
  are read only once (or twice if the mode is computed) and added to an
  optimized tree algorithm to avoid completely resorting data as each new
  image is read.  In order to do this it buffers pixel data internally as
  well as having some memory overhead from the tree algorithm.  The memory
  is compressed as much as possible.  The amount of memory required will
  scale with the size of the window, the number of pixels in the images,
  and the storage datatype.  The storage datatype (<i>storetype</i>) may be
  short integer, which is two bytes per pixel, and real, which is four bytes
  per pixel.  If memory limitations are an issue one may chose to use short
  storage which requires of order 75% less memory.  The tradeoff is that
  data will be rounded (not truncated).  In many cases this effect
  will be minor.  Note that even if the input data is integer the pixels
  values may be scaled resulting in fractional scaled values.  The output
  images will be real regardless of the input type.
  </p>
  <p>
  With sufficiently large images and large windows it is possible this task
  will fail to run requiring the user to make adjustments.  The simplest
  method would be to break the images into smaller pieces and run this task
  on each piece.  Note that input image sections can be used to reduce the
  size of the input images being processed and <b>imtile</b>
  can be use to piece the output back together.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcombine, rskysub, irproc
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

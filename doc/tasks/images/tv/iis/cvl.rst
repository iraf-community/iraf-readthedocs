.. _cvl:

cvl: Load image display (newer version of 'display')
====================================================

**Package: iis**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  cvl image frame
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Image to be loaded.
  </dd>
  </dl>
  <dl id="l_frame">
  <dt><b>frame</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='frame' Line='frame' -->
  <dd>Display frame to be loaded.
  </dd>
  </dl>
  <dl id="l_erase">
  <dt><b>erase = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='erase' Line='erase = yes' -->
  <dd>Erase frame before loading image?
  </dd>
  </dl>
  <dl id="l_border_erase">
  <dt><b>border_erase = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='border_erase' Line='border_erase = no' -->
  <dd>Erase unfilled area of window in display frame if the whole frame is not
  erased?
  </dd>
  </dl>
  <dl id="l_select_frame">
  <dt><b>select_frame = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='select_frame' Line='select_frame = yes' -->
  <dd>Display the frame to be loaded?
  </dd>
  </dl>
  <dl id="l_fill">
  <dt><b>fill = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fill' Line='fill = no' -->
  <dd>Interpolate or block average the image to fit the display window?
  </dd>
  </dl>
  <dl id="l_zscale">
  <dt><b>zscale = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zscale' Line='zscale = yes' -->
  <dd>Apply an automatic intensity mapping algorithm when loading the image?
  </dd>
  </dl>
  <dl id="l_contrast">
  <dt><b>contrast = 0.25</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='contrast' Line='contrast = 0.25' -->
  <dd>Contrast factor for the automatic intensity mapping algorithm.
  </dd>
  </dl>
  <dl id="l_zrange">
  <dt><b>zrange = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zrange' Line='zrange = yes' -->
  <dd>If not using the automatic mapping algorithm (<i>zscale = no</i>) map the
  full range of the image intensity to the full range of the display?
  </dd>
  </dl>
  <dl id="l_nsample_lines">
  <dt><b>nsample_lines = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsample_lines' Line='nsample_lines = 5' -->
  <dd>Number of sample lines to use in the automatic intensity mapping algorithm.
  </dd>
  </dl>
  <dl id="l_xcenter">
  <dt><b>xcenter = 0.5, ycenter = 0.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcenter' Line='xcenter = 0.5, ycenter = 0.5' -->
  <dd>Horizontal and vertical centers of the display window in normalized
  coordinates measured from the left and bottom respectively.
  </dd>
  </dl>
  <dl id="l_xsize">
  <dt><b>xsize = 1, ysize = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xsize' Line='xsize = 1, ysize = 1' -->
  <dd>Horizontal and vertical sizes of the display window in normalized coordinates.
  </dd>
  </dl>
  <dl id="l_xmag">
  <dt><b>xmag = 1., ymag = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmag' Line='xmag = 1., ymag = 1.' -->
  <dd>Horizontal and vertical image magnifications when not filling the display
  window.  Magnifications greater than 1 map image pixels into more than 1
  display pixel and magnifications less than 1 map more than 1 image pixel
  into a display pixel.
  </dd>
  </dl>
  <dl id="l_z1">
  <dt><b>z1, z2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='z1' Line='z1, z2' -->
  <dd>Minimum and maximum image intensity to be mapped to the minimum and maximum
  display levels.  These values apply when not using the automatic or range
  intensity mapping methods.
  </dd>
  </dl>
  <dl id="l_ztrans">
  <dt><b>ztrans = <span style="font-family: monospace;">"linear"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ztrans' Line='ztrans = "linear"' -->
  <dd>Transformation of the image intensity levels to the display levels.  The
  choices are:
  <dl>
  <dt><b><span style="font-family: monospace;">"linear"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"linear"' -->
  <dd>Map the minimum and maximum image intensities linearly to the minimum and
  maximum display levels.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"log"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"log"' -->
  <dd>Map the minimum and maximum image intensities linearly to the range 1 to 1000,
  take the logarithm (base 10), and then map the logarithms to the display
  range.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"none"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"none"' -->
  <dd>Apply no mapping of the image intensities (regardless of the values of
  <i>zscale, zrange, z1, and z2</i>).  For most image displays, values exceeding
  the maximum display value are truncated by masking the highest bits.
  This corresponds to applying a modulus operation to the intensity values
  and produces <span style="font-family: monospace;">"wrap-around"</span> in the display levels.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"user"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"user"' -->
  <dd>User supplies a look up table of intensities and their corresponding
  greyscale values.  
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_lutfile">
  <dt><b>lutfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lutfile' Line='lutfile = ""' -->
  <dd>Name of text file containing the look up table when <i>ztrans</i> = user.
  The table should contain two columns per line; column 1 contains the
  intensity, column 2 the desired greyscale output.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The specified image is loaded into the specified frame of the standard
  image display device (<span style="font-family: monospace;">"stdimage"</span>).  For devices with more than one
  frame it is possible to load an image in a frame different than that
  displayed on the monitor.  An option allows the loaded frame to become
  the displayed frame.  The previous contents of the frame may be erased
  (which can be done very quickly on most display devices) before the
  image is loaded.  Without erasing, the image replaces only those pixels
  in the frame defined by the display window and spatial mapping
  described below.  This allows displaying more than one image in a
  frame.  An alternate erase option erases only those pixels in the
  defined display window which are not occupied by the image being
  loaded.  This is generally slower than erasing the entire frame and
  should be used only if a display window is smaller than the entire
  frame.
  </p>
  <p>
  The image is mapped both in intensity and in space.  The intensity is
  mapped from the image pixel values to the range of display values in
  the device.  Spatial interpolation maps the image pixel coordinates
  into a part of the display frame called the display window.  Many of
  the parameters of this task are related to these two transformations.
  </p>
  <p>
  A display window is defined in terms of the full frame.  The lower left
  corner of the frame is (0, 0) and the upper right corner is (1, 1) as viewed on
  the monitor.  The display window is specified by a center (defaulted to the
  center of the frame (0.5, 0.5)) and a size (defaulted to the full size of
  the frame, 1 by 1).  The image is loaded only within the display window and
  does not affect data outside the window; though, of course, an initial
  frame erase erases the entire frame.  By using different windows one may
  load several images in various parts of the display frame.
  </p>
  <p>
  If the option <i>fill</i> is selected the image is spatially interpolated
  to fill the display window in its largest dimension (with an aspect
  ratio of 1:1).  When the display window is not automatically filled
  the image is scaled by the magnification factors (which need not be
  the same) and centered in the display window.  If the number of image
  pixels exceeds the number of display pixels in the window only the central
  portion of the image which fills the window is loaded.  By default
  the display window is the full frame, the image is not interpolated
  (no filling and magnification factors of 1), and is centered in the frame.
  The spatial interpolation algorithm is described in the section
  MAGNIFY AND FILL ALGORITHM.
  </p>
  <p>
  There are several options for mapping the pixel values to the display
  values.  There are two steps; mapping a range of image intensities to
  the full display range and selecting the mapping function or
  transformation.  The mapping transformation is set by the parameter
  <i>ztrans</i>.  The most direct mapping is <span style="font-family: monospace;">"none"</span> which loads the image
  pixel values directly without any transformation or range mapping.
  Most displays only use the lowest bits resulting in a wrap-around
  effect for images with a range exceeding the display range.  This is
  sometimes desirable because it produces a contoured image which is not
  saturated at the brightest or weakest points.  This transformation is
  also the fastest.  Another transformation, <span style="font-family: monospace;">"linear"</span>, maps the selected
  image range linearly to the full display range.  The logarithmic
  transformation, <span style="font-family: monospace;">"log"</span>, maps the image range linearly between 1 and 1000
  and then maps the logarithm (base 10) linearly to the full display
  range.  In the latter transformations pixel values greater than
  selected maximum display intensity are set to the maximum display value
  and pixel values less than the minimum intensity are set to the minimum
  display value.
  </p>
  <p>
  Methods for setting of the range of image pixel values, <i>z1</i> and
  <i>z2</i>, to be mapped to the full display range are arranged in a
  hierarchy from an automatic mapping which gives generally good result
  for typical astronomical images to those requiring the user to specify
  the mapping in detail.  The automatic mapping is selected with the
  parameter <i>zscale</i>.  The automatic mapping algorithm is described
  in the section ZSCALE ALGORITHM and has two parameters,
  <i>nsample_lines</i> and <i>contrast</i>.
  </p>
  <p>
  When <i>ztrans</i> = user, a look up table of intensity values and their
  corresponding greyscale levels is read from the file specified by the
  <i>lutfile</i> parameter.  From this information, a piecewise linear
  look up table containing 4096 discrete values is composed.  The text
  format table contains two columns per line; column 1 contains the
  intensity, column 2 the desired greyscale output.  The greyscale values
  specified by the user must match those available on the output device.
  Task <i>showcap</i> can be used to determine the range of acceptable
  greyscale levels.  When <i>ztrans</i> = user, parameters <i>zscale</i>,
  <i>zrange</i> and <i>zmap</i> are ignored.
  </p>
  <p>
  If the zscale algorithm is not selected the <i>zrange</i> parameter is
  examined.  If <i>zrange</i> is yes then <i>z1</i> and <i>z2</i> are set to
  the minimum and maximum image pixels values, respectively.  This insures
  that the full range of the image is displayed but is generally slower
  than the zscale algorithm (because all the image pixels must be examined)
  and, for images with a large dynamic range, will generally show only the
  brightest parts of the image.
  </p>
  <p>
  Finally, if the zrange algorithm is not selected the user specifies the
  values of <i>z1</i> and <i>z2</i> directly.
  </p>
  </section>
  <section id="s_zscale_algorithm">
  <h3>Zscale algorithm</h3>
  <p>
  The zscale algorithm is designed to display the image values near the median
  image value without the time consuming process of computing a full image
  histogram.  This is particularly useful for astronomical images which
  generally have a very peaked histogram corresponding to the background
  sky in direct imaging or the continuum in a two dimensional spectrum.
  </p>
  <p>
  A subset of the image is examined.  Approximately 600 pixels are
  sampled evenly over the image.  The number of lines is a user parameter,
  <i>nsample_lines</i>.  The pixels are ranked in brightness to
  form the function I(i) where i is the rank of the pixel and I is its value.
  Generally the midpoint of this function (the median) is very near the peak
  of the image histogram and there is a well defined slope about the midpoint
  which is related to the width of the histogram.  At the ends of the
  I(i) function there are a few very bright and dark pixels due to objects
  and defects in the field.  To determine the slope a linear function is fit
  with iterative rejection;
  </p>
  <p>
  	I(i) = intercept + slope * (i - midpoint)
  </p>
  <p>
  If more than half of the points are rejected
  then there is no well defined slope and the full range of the sample
  defines <i>z1</i> and <i>z2</i>.  Otherwise the endpoints of the linear
  function are used (provided they are within the original range of the
  sample):
  </p>
  <div class="highlight-default-notranslate"><pre>
  z1 = I(midpoint) + (slope / contrast) * (1 - midpoint)
  z2 = I(midpoint) + (slope / contrast) * (npoints - midpoint)
  </pre></div>
  <p>
  As can be seen, the parameter <i>contrast</i> may be used to adjust the contrast
  produced by this algorithm.
  </p>
  </section>
  <section id="s_magnify_and_fill_algorithm">
  <h3>Magnify and fill algorithm</h3>
  <p>
  The spatial interpolation algorithm magnifies (or demagnifies) the
  image along each axis by the desired amount.  The fill option is a
  special case of magnification in that the magnification factors are set
  by the requirement that the image just fit the display window in its
  maximum dimension with an aspect ratio (ratio of magnifications) of 1.
  There are two requirements on the interpolation algorithm; all the
  image pixels must contribute to the interpolated image and the
  interpolation must be time efficient.  The second requirement means that
  simple linear interpolation is used.  If more complex interpolation is
  desired then tasks in the IMAGES package must be used to first
  interpolate the image to the desired size before loading the display
  frame.
  </p>
  <p>
  If the magnification factors are greater than 0.5 (sampling step size
  less than 2) then the image is simply interpolated.  However, if the
  magnification factors are less than 0.5 (sampling step size greater
  than 2) the image is first block averaged by the smallest amount such
  that magnification in the reduced image is again greater than 0.5.
  Then the reduced image is interpolated to achieve the desired
  magnifications.  The reason for block averaging rather than simply
  interpolating with a step size greater than 2 is the requirement that
  all of the image pixels contribute to the displayed image.  If this is
  not desired then the user can explicitly subsample using image
  sections.  The effective difference is that with subsampling the
  pixel-to-pixel noise is unchanged and small features may be lost due to
  the subsampling.  With block averaging pixel-to-pixel noise is reduced
  and small scale features still contribute to the displayed image.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  For the purpose of these examples we assume a display with four frames,
  512 x 512 in size, and a display range of 0 to 255.  Also consider two
  images, image1 is 100 x 200 with a range 200 to 2000 and image2 is
  2000 x 1000 with a range -1000 to 1000.  To load the images with the
  default parameters:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cvl image1 1
  cl&gt; cvl image2 2
  </pre></div>
  <p>
  The image frames are first erased and image1 is loaded in the center of
  display frame 1 without spatial interpolation and with the automatic intensity
  mapping.  Only the central 512x512 area of image2 is loaded in display frame 2
  </p>
  <p>
  To load the display without any intensity transformation:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cvl image1 1 ztrans=none
  </pre></div>
  <p>
  The next example interpolates image2 to fill the full 512 horizontal range
  of the frame and maps the full image range into the display range.  Note
  that the spatial interpolation first block averages by a factor of 2 and then
  magnifies by 0.512.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cvl image2 3 fill+ zscale-
  </pre></div>
  <p>
  The next example makes image1 square and sets the intensity range explicitly.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cvl image1 4 zscale- zrange- z1=800 z2=1200 xmag=2
  </pre></div>
  <p>
  The next example loads the two images in the same frame side-by-side.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cvl.xsize=0.5
  cl&gt; cvl image1 fill+ xcen=0.25
  cl&gt; cvl image2 erase- fill+ xcen=0.75
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  display, magnify
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'ZSCALE ALGORITHM' 'MAGNIFY AND FILL ALGORITHM' 'EXAMPLES' 'SEE ALSO'  -->
  

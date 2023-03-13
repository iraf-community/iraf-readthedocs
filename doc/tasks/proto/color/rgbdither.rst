.. _rgbdither:

rgbdither: Create an 8-bit RGB dithered image
=============================================

**Package: color**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rgbdither red green blue rgb
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_red">
  <dt><b>red, green, blue</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='red' Line='red, green, blue' -->
  <dd>Input image names for the red, green, and blue components.  The images
  must all be two dimensional and of the same size.
  </dd>
  </dl>
  <dl id="l_rgb">
  <dt><b>rgb</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rgb' Line='rgb' -->
  <dd>Output image name for the RGB dithered composite image.
  </dd>
  </dl>
  <dl id="l_rz1">
  <dt><b>rz1, rz2, gz1, gz2, bz1, bz2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rz1' Line='rz1, rz2, gz1, gz2, bz1, bz2' -->
  <dd>Range of values in the input images to be mapped to the minimum and maximum
  intensity in each color.  Image pixel values outside the range are mapped
  to the nearest endpoint.  The values correspond to the input image
  intensities even when using logarithmic mapping.
  </dd>
  </dl>
  <dl id="l_blkavg">
  <dt><b>blkavg = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blkavg' Line='blkavg = 3' -->
  <dd>Block average factor for the input images.  The input images may first be
  block averaged before creating the output dithered composite image.  Note
  that the output image will be have dimensions three times larger than the
  block averaged input images so a block average factor of three will produce
  an image which is nearly the same size as the original input images.  A
  factor of 1 will use the pixel values without any averaging.
  </dd>
  </dl>
  <dl id="l_logmap">
  <dt><b>logmap = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logmap' Line='logmap = no' -->
  <dd>Use logarithmic intensity mapping?  The logarithm of the input pixel
  values, in the range given by the z1 and z2 parameters, is taken before
  dividing the range into the 85 display levels.  Logarithmic mapping allows
  a greater dynamic range.
  </dd>
  </dl>
  <dl id="l_pattern">
  <dt><b>pattern = <span style="font-family: monospace;">"rgbgbrbrg"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pattern' Line='pattern = "rgbgbrbrg"' -->
  <dd>Dither pattern given as a list of characters specifying a 3x3 array
  with the column element incrementing fastest.  A character of r is
  the red image, a character of g is the green image, and a character of
  b is the blue image.  Note that each image should occur three times.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Rgbdither</b> takes three input IRAF images and produces a special
  composite IRAF image which may be displayed as an RGB color image using a
  special color map.  The input images are first block averaged by the
  <i>blkavg</i> factor, pixel values outside the specified ranges are mapped
  to the nearest endpoint, converted to logarithmic intensities if desired,
  and the range mapped to 85 integer levels.  The red image is mapped to the
  values 0 to 84, the green image to the values 85 to 169, and the blue image
  to the values 170 to 254.  The corresponding pixels from the three images
  are then replicated in the output image to form a specified 3x3 dither
  pattern such as the default of
  </p>
  <div class="highlight-default-notranslate"><pre>
  brg
  gbr
  rgb
  </pre></div>
  <p>
  where r is the red image pixel, g is the green image pixel, and b is the
  blue image pixel.  This produces a composite image which is three times
  larger in each dimension than the block averaged input images.
  </p>
  <p>
  When the dithered 8-bit composite image is displayed using a color map that
  shows values 0-84 as shades of red, 85-169 as shades of green, and 170-254
  as shades of blue the eye (or camera) will blend the individual pixels into
  a RGB color image.  See <b>rgbdisplay</b> and <b>color</b> for a description of
  how to display the composite image.  A better technique may be to use
  <b>rgbto8</b>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Three 2048x2048 images of the Trifid nebula are obtained in the B, V,
  and R bandpasses.  These images are properly registered.  Examination of
  the histograms leads to selecting the display ranges 1-500 in each band.
  The large scale colors of the extended emission is of interest and so a
  block averaging factor 6 will yield a final composite image of size
  1023x1023 to be displayed.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rgbdither trifidr trifidv trifidb trifidrgb \
  &gt;&gt;&gt; rz1=1 rz2=500 gz1=1 gz2=500 bz1=1 bz2=500 blk=6
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  Example 1 takes 2:20 minutes (33 seconds CPU) on a SparcStation 2.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rgbdisplay, rgbto8, rgbsun, color.package
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'SEE ALSO'  -->
  

.. _rgbto8:

rgbto8: Create an 8-bit RGB image with special color map
========================================================

**Package: color**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rgbto8 red green blue rgb
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
  <dd>Output image name for the RGB 8-bit image.  A color map with the same
  image name but the extension <span style="font-family: monospace;">".sao"</span> or <span style="font-family: monospace;">".imt"</span> will also be created.
  </dd>
  </dl>
  <dl id="l_maptype">
  <dt><b>maptype = <span style="font-family: monospace;">"saoimage"</span> (saoimage|imtool|ximtool)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maptype' Line='maptype = "saoimage" (saoimage|imtool|ximtool)' -->
  <dd>This parameter selects the type of color map file to be produced.  The
  choices are <span style="font-family: monospace;">"saoimage"</span> to produce a map for SAOimage, <span style="font-family: monospace;">"imtool"</span> to produce a
  map for IMTOOL, and <span style="font-family: monospace;">"ximtool"</span> to produce a map for XIMTOOL.  The filenames
  are derived from the output image name with the extension <span style="font-family: monospace;">".sao"</span>, <span style="font-family: monospace;">".imt"</span>,
  or <span style="font-family: monospace;">".xim"</span>.
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
  <dl id="l_logmap">
  <dt><b>logmap = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logmap' Line='logmap = no' -->
  <dd>Use logarithmic intensity mapping?  The logarithm of the input pixel
  values, in the range given by the z1 and z2 parameters, is taken before
  dividing the range into the 85 display levels.  Logarithmic mapping allows
  a greater dynamic range.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Rgbto8</b> takes three input IRAF images and produces an 8-bit color map
  which samples the full range of RGB color values and an associated image
  with values indexing the color map.  The compression algorithm is called
  the Median Cut Algorithm and the image is dithered with this color map
  using the Floyd-Steinberg algorithm.  The resulting image is a short image
  with 199 values.  The color map is output in a format suitable for
  use with SAOimage, IMTOOL or XIMTOOL.  This method is recommended over the
  pixel dithering method.
  </p>
  <p>
  The RGB values are input as three IRAF images.  The images must each be
  scaled to an 8 bit range.  This is done by specifying a range of input
  values to be mapped to the 8 bit range.  In addition the range can be
  mapped logarithmically to allow a greater dynamic range.
  </p>
  <p>
  The output image is displayed with <b>rgbdisplay</b> and SAOimage, IMTOOL,
  or XIMTOOL.  Note that this requires V1.07 of SAOimage.  The color map
  produced by the <b>rgbto8</b> for a particular image must also be loaded
  into the display server manually.  With IMTOOL use the setup panel and set
  the file name in the user1 or user2 field and then select the appropriate
  map.  With SAOimage you select the <span style="font-family: monospace;">"color"</span> main menu function, and then the
  <span style="font-family: monospace;">"cmap"</span> submenu function, and then the <span style="font-family: monospace;">"read"</span> button.  Note that usually a
  full pathname is required since the server is usually started from the
  login directory.  For XIMTOOL the <span style="font-family: monospace;">"XImtool*cmapDir1"</span> resource must be
  set to the directory containing the color map and XIMTOOL must be
  restarted to cause the directory to be searched for color map files.
  </p>
  <p>
  The display server must be setup in it's default contrast mapping (with
  IMTOOL you can use the RESET option, with XIMTOOL the <span style="font-family: monospace;">"normalize"</span> option is
  used, and with SAOimage you must restart) and the contrast mapping must not
  be changed.  There are no adjustments that can be made in IMTOOL or XIMTOOL
  but with SAOimage you can adjust the colors using the <span style="font-family: monospace;">"gamma"</span> selections
  and the mouse.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Three 2048x2048 images of the Trifid nebula are obtained in
  the B, V, and R bandpasses.  These images are properly registered.
  Examination of the histograms leads to selecting the display ranges 1-500
  in each band.  A half size image is created by subsampling using image
  sections.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rgbto8 trifidr[*:2,*:2] trifidv[*:2,*:2] trifidb[*:2,*:2] \
  &gt;&gt;&gt; trifid8 maptype=saoimage rz1=1 rz2=500 gz1=1 gz2=500 \
  &gt;&gt;&gt; bz1=1 bz2=500
  </pre></div>
  <p>
  The file trifid8.sao will be created containing the color map for use
  with the image trifid8.
  </p>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  Example 1 takes 5 minutes on a SparcStation 2.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rgbdisplay, rgbdither, rgbsun, color.package
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'SEE ALSO'  -->
  

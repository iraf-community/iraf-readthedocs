.. _rgbdisplay:

rgbdisplay: Display an RGB image
================================

**Package: color**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rgbdisplay rgb
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_rgb">
  <dt><b>rgb</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rgb' Line='rgb' -->
  <dd>Image name of the 8-bit RGB dithered composite image to be displayed.
  </dd>
  </dl>
  <dl id="l_frame">
  <dt><b>frame = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='frame' Line='frame = 1' -->
  <dd>Image display frame.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Rgbdisplay</b> displays an 8-bit RGB color mapped or dithered image produced
  by the tasks <b>rgbto8</b> or <b>rgbdither</b>.  This task is a simple script
  calling
  the <b>display</b> task with parameters fixed appropriately for the
  images.  The actual display command is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  display rgb frame fill- ztrans=none
  </pre></div>
  <p>
  where rgb and frame are the parameters of this task.
  </p>
  <p>
  In addition to loading the image with the <b>rgbdisplay</b> task
  it is also necessary to adjust the image display server.  Either
  SAOimage or IMTOOL may be used.  SAOimage is to be prefered because
  it is possible to make some adjustments in the color mapping while with
  IMTOOL one must modify the composite image by varying the z1 and z2
  values for the three images.
  </p>
  <p>
  Both display servers must be set so that there is no contrast stretching.
  This is how both programs start initially but it may be difficult to return
  to this state if you adjust the contrast with the right mouse button in
  IMTOOL or the contrast adjustments in the (COLOR) menu of SAOimage.
  </p>
  <p>
  You must first determine where the special color maps are located.
  For the images produced by <b>rgbto8</b> the color map will be in
  the same directory as the image and have the same name with either
  the extension <span style="font-family: monospace;">".sao"</span> or <span style="font-family: monospace;">".imt"</span> depending on the target display server.
  Since the display servers are host programs they require host pathnames.
  </p>
  <p>
  For the images produced by <b>rgbdither</b>
  you can determine the host pathname for the special color map
  from within IRAF using the command
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; path colorlib$saorgb.lut
  puppis!/ursa/iraf/extern/color/lib/saorgb.lut
  
                  or
  
  cl&gt; path colorlib$imtoolrgb.lut
  puppis!/ursa/iraf/extern/color/lib/imtoolrgb.lut
  </pre></div>
  <p>
  You can either remember these names (without the node prefix) or
  more simply copy the one you need to your IRAF home directory
  (or any place else you like) with the command
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; copy colorlib$saorgb.lut home$
  
                  or
  
  cl&gt; copy colorlib$imtoolrgb.lut home$
  </pre></div>
  <p>
  With SAOimage load the appropriate color map look up table by entering the
  (COLOR) menu, then the (CMAP) menu, and then pushing the (READ) button.
  When you are prompted for the map enter the pathname for the file
  saorgb.lut.  For IMTOOL you need to call up the setup menu and set the
  pathname for the file imtoolrgb.lut in either of the user look up tables
  and then select the appropriate map.
  </p>
  <p>
  For IMTOOL that is all you can do.  Beware, don't adjust the contrast (the
  right mouse button) since this destroys the mapping between the composite
  image values and the look up table.
  </p>
  <p>
  In SAOimage there are a couple of things you can do to make adjustments to
  the display.  If you select (GAMMA) in the (COLOR) menu you can then move
  the mouse with a button down and vary the linearity of the color maps.
  This may be used with either of the 8-bit algorithms.
  </p>
  <p>
  For the pixel dithered images you can also directly manipulate the color
  map.  Bring up the color editor by clicking on the color bar.  Even if you
  don't adjust the look up table this can be instructive.  You can also
  adjust the individual colors by clicking the left (red), middle (green), or
  right (blue) buttons to either move the shown points or add and move points
  in the middle.  Note that the abrupt discontinuity between the colors can
  cause sudden jumps in the color map if one point is moved past the other
  but you can recover by bring the point slowly back.  If the map gets too
  messed up you can always reload the color map.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Display a dithered composite image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rgbdisplay tucana!/d1/testdata/rgb/trifid8
  &lt;Load the color map tucana!/d1/testdata/rgb/trifid8.sao or
  &lt;tucana!/d1/testdata/rgb/trifid8.imt. Because the display
  &lt;server is a host program you may need to copy the map
  &lt;first.
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rgbto8, rgbdither, color.package
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

.. _contour:

contour: Make a contour plot of an image
========================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  contour image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Two dimensional image or image section to be contoured.
  </dd>
  </dl>
  <dl id="l_floor">
  <dt><b>floor = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='floor' Line='floor = INDEF' -->
  <dd>Minimum value to be contoured.  If <b>floor = INDEF</b>, the data minimum is
  used for the floor.
  </dd>
  </dl>
  <dl id="l_ceiling">
  <dt><b>ceiling = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ceiling' Line='ceiling = INDEF' -->
  <dd>Maximum value to be contoured.  If <b>ceiling = INDEF</b>, the data maximum
  is used for the ceiling.
  </dd>
  </dl>
  <dl id="l_zero">
  <dt><b>zero = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zero' Line='zero = 0' -->
  <dd>Greyscale value of the zero contour, i.e., the value of a zero point shift
  to be applied to the image data before plotting.  Does not affect the values
  of the floor and ceiling parameters.
  </dd>
  </dl>
  <dl id="l_ncontours">
  <dt><b>ncontours = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncontours' Line='ncontours = 0' -->
  <dd>Number of contours to be drawn.  If 0, the contour interval may be specified,
  otherwise 20-30 nicely spaced contours are drawn.  A maximum of 40 contours
  can be drawn.
  </dd>
  </dl>
  <dl id="l_interval">
  <dt><b>interval = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interval' Line='interval = 0' -->
  <dd>Contour interval.  If 0, a contour interval is chosen which places 20 to 30
  contours spanning the intensity range of the image.
  </dd>
  </dl>
  <dl id="l_nhi">
  <dt><b>nhi = -1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nhi' Line='nhi = -1' -->
  <dd>If -1, highs and lows are not marked.  If 0, highs and lows are marked
  on the plot.  If 1, the intensity of each pixel is marked on the plot.
  </dd>
  </dl>
  <dl id="l_dashpat">
  <dt><b>dashpat = 528</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dashpat' Line='dashpat = 528' -->
  <dd>Dash pattern for negative contours.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "stdgraph"' -->
  <dd>Output device (<b>stdgraph</b>, <b>stdplot</b>, or the name of a physical
  device).
  </dd>
  </dl>
  <dl id="l_xres">
  <dt><b>xres = 64, yres = 64</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xres' Line='xres = 64, yres = 64' -->
  <dd>The input image is block averaged or subsampled to this resolution.
  </dd>
  </dl>
  <dl id="l_preserve">
  <dt><b>preserve = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='preserve' Line='preserve = yes' -->
  <dd>If <b>preserve</b> = yes, the aspect ratio of the image is preserved when 
  achieving the resolution specified by <b>xres</b> and <b>yres</b>.
  </dd>
  </dl>
  <dl id="l_subsample">
  <dt><b>subsample = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subsample' Line='subsample = no' -->
  <dd>The resolution specified by <b>xres</b>, <b>yres</b> is achieved by block 
  averaging unless <b>subsample = yes</b>.
  </dd>
  </dl>
  <dl id="l_perimeter">
  <dt><b>perimeter = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='perimeter' Line='perimeter = yes' -->
  <dd>A <i>crtpict</i> perimeter is drawn around the contour plot with labeled
  tickmarks.
  </dd>
  </dl>
  <dl id="l_label">
  <dt><b>label= yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='label' Line='label= yes' -->
  <dd>By default, the value of each major contour is embedded in the contour
  line.  This can be disabled by setting <b>label=no</b>.
  </dd>
  </dl>
  <dl id="l_vx1">
  <dt><b>vx1 = 0.0, vx2 = 0.0, vy1 = 0.0, vy2 = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vx1' Line='vx1 = 0.0, vx2 = 0.0, vy1 = 0.0, vy2 = 0.0' -->
  <dd>The device viewport, in normalized device coordinates (from 0.0 to 1.0
  inclusive).  If not specified by the user,
  <b>contour</b> automatically centers the plot on the device viewport.
  </dd>
  </dl>
  <dl id="l_fill">
  <dt><b>fill = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fill' Line='fill = no' -->
  <dd>Fill the output viewport regardless of the device aspect ratio?
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">"imtitle"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = "imtitle"' -->
  <dd>A title to be centered above the plot.  The user can specify a title string;
  the default string is the image title.
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = no' -->
  <dd>Append to an existing plot?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Contours are traced, smoothed with splines under tension, and optionally printed
  with embedded intensity labels.  Positive contours are printed as solid
  lines and negative contours as dashed lines.  The plot is generated
  by the NCAR <b>conrec</b> utility, using <b>dashsmth</b> to smooth the
  contours and draw dashed lines.  
  </p>
  <p>
  To speed up the contouring, the resolution of the image to be plotted can
  be decreased to <b>xres</b> by <b>yres</b>.
  When <b>preserve</b> = yes, <b>contour</b> 
  automatically reduces the image in both directions by the same factor, which
  is the larger of [ncolumns / xres or nlines / yres]. If the
  aspect ratio is not being preserved, the x and y dimensions are independently
  reduced to the specified resolution.
  No reduction is done if <b>xres</b> and <b>yres</b> = 0, if the input image is 
  an image section, or if the image is smaller than <b>xres</b> by <b>yres</b>.
  </p>
  <p>
  If the device viewport (plotting area) is not set by the user,
  <i>contour</i> automatically
  sets a viewport centered on the output device.  The default value of
  <b>fill=no</b> means the viewport will be adjusted so that equal
  numbers of image pixels in x and y will occupy equal lengths when plotted.
  That is, when <b>fill = no</b>, a unity aspect ratio is enforced, and square 
  images are represented as square plots regardless of the device aspect ratio.
  On devices with non square full device viewports (e.g., the vt640), a 
  square image will appear extended when <b>fill</b> = yes.  To completely
  fill the device viewport with contour lines, disable perimeter drawing
  and enable fill, and nothing but the contour map will be drawn.
  </p>
  <p>
  Contour plots may be overlaid on a displayed image by setting the output
  <b>device</b> to <span style="font-family: monospace;">"imd"</span> for image display and the contouring parameters
  <b>fill</b> and <b>perimeter</b> to <span style="font-family: monospace;">"yes"</span> and <span style="font-family: monospace;">"no"</span> respectively. By default
  green contours will be drawn on the image display. Other choices for
  <b>device</b> are <span style="font-family: monospace;">"imdr"</span>, <span style="font-family: monospace;">"imb"</span>, <span style="font-family: monospace;">"imdy"</span>, <span style="font-family: monospace;">"imdw"</span> and <span style="font-family: monospace;">"imdg"</span> for red, blue,
  yellow, white and green output contours respectively.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Draw a contour plot of a 512 square image on the graphics terminal.
  With the default values for <b>xres</b> and <b>yres</b>, the image
  would automatically be block averaged by a factor of 8 in x and y.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; contour crab.5009
  </pre></div>
  <p>
  2. The plot could be output to the plotter as a background job:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; contour crab.5009 device=stdplot &amp;
  </pre></div>
  <p>
  3. Place a ceiling at an intensity value of 500 to cut out a noise spike.
  The plot has been moved to the lower left corner of the display.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cont crab.5009 ceil=500 vx1=.1 vx2=.6 vy1=.1 vy2=.6
  </pre></div>
  <p>
  4. Overlay a contour plot of an image on the same image displayed on the
  display device. Note that the CONTOUR parameters <b>fill</b> and <b>perimeter</b>
  must be on and off respectively, the <b>fill</b> parameter should be specified
  for the DISPLAY task to ensure the image fills the frame buffer in the 
  same way.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; display m51 1 fill+
  cl&gt; cont m51 fill+ per- device=imd
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  The time required for <i>contour</i> depends on the number of contours
  being drawn - that is, the size and smoothness of the intensity array.
  A 512 square image of <span style="font-family: monospace;">"average"</span> smoothness, with x and y resolution equal to
  64, requires about 22 cpu seconds with block averaging.  Using subsampling
  rather than block averaging, <i>contour</i> takes 16 seconds.  A noisy
  picture will be plotted more quickly if block averaged rather than
  subsampled.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  If block averaging is used the precision with which a contour is drawn
  will be no better than the blocking factor.  For example, if a contour
  map drawn with a block averaging factor of 8 is overlaid on an image of
  a starfield, contours drawn around stars in the field may not appear to
  be centered.  If this is a problem the solution is to increase the plotting
  resolution using the <i>xres</i> and <i>yres</i> parameters.
  </p>
  <p>
  It should be possible to have list input as well as image section input.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  surface, display, imdkern, imexamine
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _hafton:

hafton: Generate half-tone plots of an image
============================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  hafton image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Two dimensional image or image section to be plotted.
  </dd>
  </dl>
  <dl id="l_z1">
  <dt><b>z1 = 0.0, z2 = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='z1' Line='z1 = 0.0, z2 = 0.0' -->
  <dd>The minimum (z1) and maximum (z2) intensities to be mapped.  If left at the
  default values of 0.0, the full intensity range will be mapped.
  </dd>
  </dl>
  <dl id="l_nlevels">
  <dt><b>nlevels = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlevels' Line='nlevels = 0' -->
  <dd>The number of intensities levels to be shown.  If <b>nlevels = 0</b> or <b>1</b>,
  the maximum of 16 levels is used.
  </dd>
  </dl>
  <dl id="l_mapping_function">
  <dt><b>mapping_function = <span style="font-family: monospace;">"linear"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mapping_function' Line='mapping_function = "linear"' -->
  <dd>A string specifying the image intensity to half tone mapping function.
  The default is linear mapping between <b>z1</b> and <b>z2</b>.  For other
  choices, see the description section below.
  </dd>
  </dl>
  <dl id="l_contrast">
  <dt><b>contrast = 0.25</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='contrast' Line='contrast = 0.25' -->
  <dd>Positive or negative contrast.  Negative contrast is indicated by setting
  <b>contrast</b> to a negative number.  The magnitude of <b>contrast</b> is
  not important unless <b>mapping_function = crtpict</b>.
  </dd>
  </dl>
  <dl id="l_perimeter">
  <dt><b>perimeter = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='perimeter' Line='perimeter = yes' -->
  <dd>Should a <b>crtpict</b> perimeter with labeled tickmarks be drawn around 
  the plot?
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device=<span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device="stdgraph"' -->
  <dd>Output device for plot.
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">"imtitle"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = "imtitle"' -->
  <dd>The title to be centered above the plot.  By default, the title string from
  the image header is used.
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
  <dd>Should the image be subsampled (as opposed to block averaged) to achieve the
  specified resolution?
  </dd>
  </dl>
  <dl id="l_vx1">
  <dt><b>vx1 = 0.0, vx2 = 0.0, vy1 = 0.0, vy2 = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vx1' Line='vx1 = 0.0, vx2 = 0.0, vy1 = 0.0, vy2 = 0.0' -->
  <dd>The device viewport, in normalized device coordinates (from 0.0 to 1.0
  inclusive).  If not specified by the user, the plot is centered on the viewport.
  </dd>
  </dl>
  <dl id="l_fill">
  <dt><b>fill = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fill' Line='fill = no' -->
  <dd>Should the plot fill the viewport regardless of the device aspect ratio?
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
  Task <i>hafton</i> draws a half tone picture of an IRAF image, where varying
  intensities in the image are represented by areas of varying darkness on
  the plot.  Six different mapping functions are available; the desired 
  mapping function is selected with the <b>mapping_function</b> string.
  The types of mapping are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  linear
  exponential - emphasizes high intensity values.
  logarithmic - emphasizes low intensity values.
  sinusoidal  - emphasizes mid-range values.
  arcsine     - extreme values emphasized at the expense of mid-range.
  crtpict     - linear mapping centered on median intensity.  The slope of
                the function is modified by <b>contrast</b>.
  </pre></div>
  <p>
  To speed up the plotting, the resolution of the input image can be 
  decreased to <b>xres</b> by <b>yres</b>.  
  When <b>preserve</b> = yes, <b>hafton</b> automatically reduces the 
  image in both directions by the same factor, which
  is the larger of [ncolumns / xres or nlines / yres].  If the
  aspect ratio is not being preserved, the x and y dimensions are independently
  reduced to the specified resolution.
  No reduction is done if
  <b>xres</b> and <b>yres</b> = 0, if the input image is an image section, or
  if the image is smaller than <b>xres</b> by <b>yres</b>.
  </p>
  <p>
  If the device viewport is not set by the user, <i>hafton</i> automatically
  sets a viewport centered on the output device.  The default value of
  <b>fill=no</b> means the viewport will be adjusted so that equal
  numbers of image pixels in x and y will occupy equal lengths when plotted.
  That is, when <b>fill=no</b>, a unity aspect
  ratio is enforced, and square images are represented as square plots
  regardless of the device aspect ratio.
  On devices with non square full device
  viewports (e.g., the vt640), a square image will appear extended when
  <b>fill=yes</b>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Image <span style="font-family: monospace;">"crab.6563"</span> is plotted in negative contrast, with linear mapping
  between the minimum and maximum image pixel.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hafton crab.6563 contrast=-1
  </pre></div>
  <p>
  2. The image is plotted in negative contrast using the same mapping
  function as used by the <i>crtpict</i> task.  The resulting plot is
  in negative contrast.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hafton crab.6563 mapping_fun=crt contrast =-0.25
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  To produce a <i>hafton</i> plot on the terminal takes just under 9 cpu
  minutes.  If the output device is the imagen or versatec (or another
  nspp device) the total cpu time is about an hour.  
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  A large number of plotter instructions ( &gt; 100,000 polylines) is generated 
  per frame for square images.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS'  -->
  

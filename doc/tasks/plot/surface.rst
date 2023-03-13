.. _surface:

surface: Make a surface plot of an image
========================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  surface image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Image or image section to be plotted.
  </dd>
  </dl>
  <dl id="l_floor">
  <dt><b>floor = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='floor' Line='floor = INDEF' -->
  <dd>Data values below <b>floor</b> are clipped.  If <b>floor = INDEF</b>, the data
  minimum is used for the floor.
  </dd>
  </dl>
  <dl id="l_ceiling">
  <dt><b>ceiling = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ceiling' Line='ceiling = INDEF' -->
  <dd>Data values above <b>ceiling</b> are clipped.  If <b>ceiling = INDEF</b>, the
  data maximum is used for the ceiling.
  </dd>
  </dl>
  <dl id="l_angh">
  <dt><b>angh = -33.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='angh' Line='angh = -33.0' -->
  <dd>Horizontal viewing angle, degrees.
  </dd>
  </dl>
  <dl id="l_angv">
  <dt><b>angv = 25.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='angv' Line='angv = 25.0' -->
  <dd>Vertical viewing angle, degrees.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "stdgraph"' -->
  <dd>Output device (<b>stdgraph</b>, <b>stdplot</b>, or the name of a physical
  device).
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">"imtitle"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = "imtitle"' -->
  <dd>A title string is centered above the plot.  The user can specify a title
  string; the default is the image title.
  </dd>
  </dl>
  <dl id="l_label">
  <dt><b>label = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='label' Line='label = no' -->
  <dd>The axes are drawn and the corner points of the plotting area are labeled 
  if <b>label</b> = yes.
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
  averaging unless <b>subsample</b> = yes.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Surface</b> draws a pseudo-three dimensional perspective of an image
  section.  Hidden lines are removed.  The surface may be viewed from any
  angle.  Subsampling or block averaging is used to achieve the resolution
  specified.  A labeled perimeter is optionally drawn around the plot.
  </p>
  <p>
  To speed up the plot, the resolution of the image can be decreased to
  <b>xres</b> by <b>yres</b>.  When <b>preserve</b> = yes, <b>surface</b> 
  automatically reduces the image in both directions by the same factor, which
  is the larger of [ncolumns / xres or nlines / yres].  If the
  aspect ratio is not being preserved, the x and y dimensions are independently
  reduced to the specified resolution.
  No reduction is done if
  <b>xres</b> and <b>yres</b> = 0, if the input image is an image section, or if
  the image is smaller than <b>xres</b> by <b>yres</b>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Surface plot of a 512 square image.  With the default values of <b>xres</b>
  and <b>yres</b>, the image would be block averaged by a factor of 8 in x and y.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; surface crab.5009
  </pre></div>
  <p>
  2. Look at the bottom of the surface, but subsample rather that block average
  to decrease resolution and speed things up.  Also, the output device will
  be the plotter, and the job will run in the background:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; surface crab.5009 angv=-30 subsample+ device=stdplot &amp;
  </pre></div>
  <p>
  3. Surface plot of band 4 of an image cube.  Since the image is specified using
  image section notation, no block averaging or subsampling will be done.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; surface cube[*,*,4]
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  The time required by <i>surface</i> depends on image size and resolution.
  A surface plot of a
  512 square image block averaged to 64 square requires 30 cpu seconds.  The
  same image subsampled would take 23 seconds to plot.  
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  It should be possible to input the surface in list form. 
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  contour, graph
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

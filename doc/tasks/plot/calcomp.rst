.. _calcomp:

calcomp: Plot metacode on a Calcomp pen plotter
===============================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  calcomp input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Name of input GKI metacode file, file template, or list of files.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"calcomp"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "calcomp"' -->
  <dd>Name of the destination plotter (as referenced in graphcap).
  </dd>
  </dl>
  <dl id="l_generic">
  <dt><b>generic = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='generic' Line='generic = no' -->
  <dd>Ignore remaining kernel dependent parameters -- if yes, then none of the
  following parameters will be used; this is automatically the case, for
  instance, when using <span style="font-family: monospace;">":.snap calcomp"</span> from cursor mode.
  </dd>
  </dl>
  <dl id="l_debug">
  <dt><b>debug = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='debug' Line='debug = no' -->
  <dd>Print decoded graphics instructions during processing -- print each GKI 
  metacode instruction on standard output.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print elements of polylines, etc. in debug mode -- if yes, this is essentially
  all of the information present in the input metacode file.
  </dd>
  </dl>
  <dl id="l_gkiunits">
  <dt><b>gkiunits = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gkiunits' Line='gkiunits = no' -->
  <dd>Print coordinates in GKI rather than NDC units if in debug mode.
  </dd>
  </dl>
  <dl id="l_xscale">
  <dt><b>xscale = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xscale' Line='xscale = INDEF' -->
  <dd>X scale in device units per GKI unit; e.g. 0.0003 is 3 ten-thousandths of an
  inch per GKI unit on a plotter calibrated in inches; normally a plot is 32767
  GKI units wide.  If the plotting task that generated the metacode file generated
  a scale, this will be used if xscale is INDEF.  Specify xscale only if you wish
  to override the scale in the metacode.
  </dd>
  </dl>
  <dl id="l_yscale">
  <dt><b>yscale = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='yscale' Line='yscale = INDEF' -->
  <dd>Y scale in device units per GKI unit -- see xscale.
  </dd>
  </dl>
  <dl id="l_txquality">
  <dt><b>txquality = <span style="font-family: monospace;">"normal"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='txquality' Line='txquality = "normal"' -->
  <dd>Text quality; <span style="font-family: monospace;">"normal"</span> means use the text quality specified in the metacode
  file.  <span style="font-family: monospace;">"Low"</span> means override the metacode font with the Calcomp symbol font,
  while <span style="font-family: monospace;">"medium"</span> and <span style="font-family: monospace;">"high"</span> use IRAF fonts.  There is little difference in speed
  with the different fonts, except if the text is bold, in which case <span style="font-family: monospace;">"high"</span>
  takes twice as long as <span style="font-family: monospace;">"low"</span> or <span style="font-family: monospace;">"medium"</span>.
  </dd>
  </dl>
  <dl id="l_lwtype">
  <dt><b>lwtype = <span style="font-family: monospace;">"ntracing"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lwtype' Line='lwtype = "ntracing"' -->
  <dd>Type of line and text width implementation.  <span style="font-family: monospace;">"Ntracing"</span> causes the pen plotter
  to draw each line or character several times with slight offsets to simulate 
  boldness.  <span style="font-family: monospace;">"Penchange"</span>, if implemented in the local Calcomp library, would
  cause the plotter to pause for an operator to change the pen when bold lines
  or text are requested.
  </dd>
  </dl>
  <dl id="l_ltover">
  <dt><b>ltover = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ltover' Line='ltover = no' -->
  <dd>Line type override, if yes, causes the pen plotter to draw all lines solidly,
  rather than as dashed or dotted lines if these are specified in the metacode.
  This may be desired for previewing a plot quickly.
  </dd>
  </dl>
  <dl id="l_lwover">
  <dt><b>lwover = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lwover' Line='lwover = yes' -->
  <dd>Line width override; causes all lines and text to come out with single width
  in order to speed up plotting.  If bold text, axes, etc. are desired and
  present in the parent plot, then set lwover = no.
  </dd>
  </dl>
  <dl id="l_lcover">
  <dt><b>lcover = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lcover' Line='lcover = no' -->
  <dd>Line color override, if yes, causes the pen plotter to ignore any requests in
  the metacode for a colored pen change.  Pen change is not implemented at all
  sites with Calcomp plotters.
  </dd>
  </dl>
  <dl id="l_dashlen">
  <dt><b>dashlen = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dashlen' Line='dashlen = INDEF' -->
  <dd>Length of the dash in dashed lines in device units, usually inches.  Shorter
  dashes usually take longer to plot but may look nicer.  If left INDEF, a
  local default from dev$graphcap will be used; a good range is 0.1 to 0.5 inches.
  </dd>
  </dl>
  <dl id="l_gaplen">
  <dt><b>gaplen = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gaplen' Line='gaplen = INDEF' -->
  <dd>Length of the gap in dashed or dotted lines, in device units.  Longer gaps 
  result in faster plotting at the expense of clarity.  If left INDEF, a local
  default from dev$graphcap will be used.  A good range is 0.05 to 0.2 inches.
  </dd>
  </dl>
  <dl id="l_plwsep">
  <dt><b>plwsep = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plwsep' Line='plwsep = INDEF' -->
  <dd>Parallel line width separation -- if bold lines are implemented with <span style="font-family: monospace;">"lwtype
  = ntracing"</span>, this is the right-angle distance between adjacent traces.  If
  INDEF, a local default is used from the device table dev$graphcap.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <b>calcomp</b> is an IRAF graphics kernel.  It may be run standalone to
  plot a GKI metacode file, or from cursor mode via <span style="font-family: monospace;">":.snap calcomp"</span>.
  </p>
  <p>
  <b>Calcomp</b> may be used to draw any IRAF plot on a Calcomp pen plotter.  It is
  only available if the local site has a Calcomp library.  Task <b>calcomp</b>
  is an exact-scaling graphics kernel, unlike the NSPP, or STDPLOT kernel.
  This means that if the task that generated the metacode input file passed an
  exact scale into the metacode, data can be plotted to a desired precise scale.
  </p>
  <p>
  The metacode scale may be overridden, or metacode files generated by tasks that
  do not implement exact scales may be plotted to a precise scale, by specifying
  xscale or yscale.  Note, however, that the only coordinates in a metacode file
  are GKI coordinates, usually running from 1 - 32767.  This means that to use
  xscale and yscale, the user must calculate the number of inches per GKI unit,
  not the number of world or data units per inch.
  </p>
  <p>
  <b>Calcomp</b> also implements dashed and dotted lines and bold lines and text.
  Thus high-quality plots may be produced, at the expense of requiring more time.
  If <span style="font-family: monospace;">"lwtype=ntracing"</span> and <span style="font-family: monospace;">"lwover=no"</span>, any bold text or lines in the metacode
  file, such as are produced for axes, tickmarks, titles and axis labels by many
  IRAF plotting tasks, will appear bold on the Calcomp.  If txquality=<span style="font-family: monospace;">"low"</span> or
  <span style="font-family: monospace;">"medium"</span>, and bold text is requested, each character will be drawn 5 times --
  once in the center position and once to the right, top, left, and bottom of
  the original position.  Each of the side positions is drawn <span style="font-family: monospace;">"plwsep"</span> inches
  from the center.  If txquality=<span style="font-family: monospace;">"high"</span>, bold text is implemented with the same
  five tracings plus the four corners upper right, upper left, etc.  For most
  applications txquality=<span style="font-family: monospace;">"normal"</span> or <span style="font-family: monospace;">"medium"</span> is adequate for nice-looking
  plots.
  </p>
  <p>
  When drawing data lines bold (only possible if the task originating the 
  metacode specifically requested it, not the case for most IRAF plotting
  tasks), the bounding parallel line traces are constructed to meet at sharp
  points.  This looks fine for line intersections that are not too acute.  If
  the intersection angle between two lines is very acute, say less than 5
  degrees, the vertex of the parallel lines bounding to the outside may lie
  quite a distance away from the actual vertex.  In the limit, if the 
  intersection angle is zero, the outer vertex will lie at infinity.  For
  this reason, all intersection angles less than 5 degrees are treated as
  though they were exactly 5 degrees.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Plot a metacode file exactly as is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; calcomp metacodefile
  </pre></div>
  <p>
  2. Get the fastest plot you can -- no bold lines or text, no dashed or dotted
  lines:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; calcomp metacodefile lwover+ ltover+ txquality=low
  </pre></div>
  <p>
  3. Get a plot half the size of the original; suppose the original plot had
  metacode scales = 0.0003 inches / GKI unit:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; calcomp metacodefile xscale=0.00015 yscale=0.00015
  </pre></div>
  <p>
  4. Get the highest quality plot you can without having to change pens:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; calcomp metacodefile txqual=high
  </pre></div>
  <p>
  5. Get a high-quality plot where you have to change the pen each time the
  metacode switches from bold to single-width lines or text:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; calcomp metacodefile txqual=high lwtype=penchange
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  Pen plotters vary considerably in their plotting rates.  At NOAO, plotting a
  metacode file from a 1024-pixel image generated by <b>longplot</b>, overriding
  bold lines and text, takes a couple of minutes.  The same plot with txquality
  = <span style="font-family: monospace;">"medium"</span> can take over twice as long due to bold text, axes, and tick labels.
  With txquality = <span style="font-family: monospace;">"high"</span>, it may take 4 or 5 times as long to plot.
  </p>
  <p>
  Plots with dashed and dotted, or both, lines may take 2-5 times as long to 
  plot as single-width lines.  The slowest of all is to produce plots with
  a lot of bold text, or with dashed and dotted AND bold data lines.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  When using multiple tracing to simulate bold lines that intersect at very
  acute angles, i.e. less than 5 degrees, each bold line will thin slightly
  as it approaches the obtuse vertex.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  See task <b>longplot</b>, also in the plot package, for a task designed to
  use the <b>calcomp</b> graphics kernel for exact scaling and/or long, e.g.
  spectral, plots.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

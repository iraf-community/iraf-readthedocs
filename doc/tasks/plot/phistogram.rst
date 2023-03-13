.. _phistogram:

phistogram: Plot or print the histogram of an image or list
===========================================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  phistogram input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The name of the image, image subsection, or the text file containing the
  stream of values whose histogram is to be computed. <i>Input</i> may be
  the standard input <span style="font-family: monospace;">"STDIN"</span>.
  </dd>
  </dl>
  <dl id="l_z1">
  <dt><b>z1 = INDEF, z2 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='z1' Line='z1 = INDEF, z2 = INDEF' -->
  <dd>The minimum and maximum values included in the histogram. The image or data
  minimum and maximum values are used by default.
  </dd>
  </dl>
  <dl id="l_binwidth">
  <dt><b>binwidth = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='binwidth' Line='binwidth = INDEF' -->
  <dd>The resolution of the histogram in data units. If <i>binwidth</i> is not defined,
  the parameters <i>nbins</i>, <i>z1</i>, and <i>z2</i> determine the resolution of
  the histogram.
  </dd>
  </dl>
  <dl id="l_nbins">
  <dt><b>nbins = 512</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nbins' Line='nbins = 512' -->
  <dd>The number of bins in, or resolution of, the histogram. 
  The <i>nbins</i> parameter is overridden if <i>binwidth</i> is defined.
  </dd>
  </dl>
  <dl id="l_autoscale">
  <dt><b>autoscale = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='autoscale' Line='autoscale = yes' -->
  <dd>In the case of integer image data, automatically adjust <i>nbins</i> and
  <i>z2</i> to avoid aliasing effects. Data in text files is not autoscaled.
  </dd>
  </dl>
  <dl id="l_top_closed">
  <dt><b>top_closed = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='top_closed' Line='top_closed = no' -->
  <dd>Include z2 in the top bin?  Each bin of the histogram is a subinterval
  that is half open at the top.  <i>Top_closed</i> decides whether those
  pixels with values equal to z2 are to be counted in the histogram.  If
  <b>top_closed</b> is yes, the top bin will be larger than the other bins.
  </dd>
  </dl>
  <dl id="l_hist_type">
  <dt><b>hist_type = <span style="font-family: monospace;">"normal"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hist_type' Line='hist_type = "normal"' -->
  <dd>The type of histogram to plot or list.  The choices are <span style="font-family: monospace;">"normal"</span>,
  <span style="font-family: monospace;">"cumulative"</span>, <span style="font-family: monospace;">"difference"</span>, or <span style="font-family: monospace;">"second_difference"</span>.  The two
  <span style="font-family: monospace;">"difference"</span> options are calculated as forward differences, i.e.
  diff[n] = hist[n+1] - hist[n].
  </dd>
  </dl>
  <dl id="l_listout">
  <dt><b>listout = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listout' Line='listout = no' -->
  <dd>List instead of plot the histogram?  The list is never log scaled.
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">"imtitle"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = "imtitle"' -->
  <dd>The plot title. If title = <span style="font-family: monospace;">"imtitle"</span>, the image name and title or the
  text file name, and the 
  characteristics of the histogram are included in the title.
  </dd>
  </dl>
  <dl id="l_xlabel">
  <dt><b>xlabel = <span style="font-family: monospace;">"Data values"</span>, ylabel = <span style="font-family: monospace;">"Counts"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xlabel' Line='xlabel = "Data values", ylabel = "Counts"' -->
  <dd>The labels for the X and Y axes.
  </dd>
  </dl>
  <dl id="l_wx1">
  <dt><b>wx1 = INDEF, wx2 = INDEF, wy1 = 0.0, wy2 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wx1' Line='wx1 = INDEF, wx2 = INDEF, wy1 = 0.0, wy2 = INDEF' -->
  <dd>The range of user coordinates spanned by the plot. If either of the x axis
  limits is INDEF the histogram minimum or maximum data values
  are used.  If either of the y axis limits is INDEF,  the 
  minimum or maximum counts in the histogram is used.
  </dd>
  </dl>
  <dl id="l_logx">
  <dt><b>logx = no, logy = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logx' Line='logx = no, logy = yes' -->
  <dd>Use log scaling on the x or y axes of the plot?
  </dd>
  </dl>
  <dl id="l_round">
  <dt><b>round = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='round' Line='round = no' -->
  <dd>Round the axes minimum and maximum values up to <span style="font-family: monospace;">"nice"</span> values?
  </dd>
  </dl>
  <dl id="l_plot_type">
  <dt><b>plot_type = <span style="font-family: monospace;">"line"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plot_type' Line='plot_type = "line"' -->
  <dd>The style of histogram to plot. The options are <span style="font-family: monospace;">"line"</span>, <span style="font-family: monospace;">"box"</span> and <span style="font-family: monospace;">"fullbox"</span>.
  If <i>plot_type</i> is <span style="font-family: monospace;">"line"</span> the histogram data points are connected by
  straight lines; if it is <span style="font-family: monospace;">"box"</span> a stepped histogram is drawn; if it is <span style="font-family: monospace;">"fullbox"</span> 
  the histogram lines are drawn to the base of the plot.
  </dd>
  </dl>
  <dl id="l_box">
  <dt><b>box = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='box' Line='box = yes' -->
  <dd>Draw axes at the perimeter of the plotting window?
  </dd>
  </dl>
  <dl id="l_ticklabels">
  <dt><b>ticklabels = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ticklabels' Line='ticklabels = yes' -->
  <dd>Label the tick marks?
  </dd>
  </dl>
  <dl id="l_majrx">
  <dt><b>majrx = 5, minrx = 5, majry = 5, minry = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='majrx' Line='majrx = 5, minrx = 5, majry = 5, minry = 5' -->
  <dd>Number of major tick marks on each axis and number of minor tick marks between
  major tick marks. These quantities are ignored if log scaling is in effect
  for an axis.
  </dd>
  </dl>
  <dl id="l_fill">
  <dt><b>fill = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fill' Line='fill = yes' -->
  <dd>Fill the output viewport regardless of the device aspect ratio?
  </dd>
  </dl>
  <dl id="l_vx1">
  <dt><b>vx1 = 0.0, vx2 = 1.0, vy1 = 0.0, vy2 = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vx1' Line='vx1 = 0.0, vx2 = 1.0, vy1 = 0.0, vy2 = 1.0' -->
  <dd>The NDC coordinates (0.0:1.0) of the device plotting viewport.
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = no' -->
  <dd>Append to an existing plot?
  </dd>
  </dl>
  <dl id="l_pattern">
  <dt><b>pattern = <span style="font-family: monospace;">"solid"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pattern' Line='pattern = "solid"' -->
  <dd>The type of line used to draw the histogram. The options are <span style="font-family: monospace;">"solid"</span>,
  <span style="font-family: monospace;">"dashed"</span> <span style="font-family: monospace;">"dotted"</span>, and <span style="font-family: monospace;">"dotdash"</span>. <i>Pattern</i> can be changed when
  appending to an existing plot.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "stdgraph"' -->
  <dd>The output graphics device.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Phistogram</i> computes the histogram of the IRAF image or stream
  of values in the text file specified by
  <i>input</i>, using the parameters <i>binwidth</i>, <i>nbins</i>,
  <i>z1</i> and <i>z2</i>.
  If either <i>z1</i> or <i>z2</i> is undefined the data minimum or
  maximum values define the histogram limits.
  If <i>binwidth</i> is undefined, <i>nbins</i>
  determines the resolution of the histogram. If <i>listout</i> = no,
  the histogram is plotted on
  the graphics device <i>device</i> in the style specified by
  <i>plot_type</i>.  The plot may be log scaled if <i>logy</i> = yes (the
  default) and the input is an IRAF image.  If <i>listout</i> = yes,
  the histogram is printed on the standard output.
  </p>
  <p>
  In addition to computing the <span style="font-family: monospace;">"normal"</span> histogram, PHISTOGRAM can also
  calculate the cumulative and the first and second difference histograms
  depending on the value of the <i>hist_type</i> parameter. The options are:
  <span style="font-family: monospace;">"normal"</span>, <span style="font-family: monospace;">"cumulative"</span>, <span style="font-family: monospace;">"difference"</span>, and <span style="font-family: monospace;">"second_difference"</span>.
  </p>
  <p>
  Each bin of the histogram is defined to be half open at the top.  This
  results in an ambiguity in deciding whether those pixels with z=z2 are
  included in the topmost bin.  This decision is left to the user via the
  <i>top_closed</i> parameter.  This is usually only of concern with integer
  image data and histograms with few bins.
  </p>
  <p>
  If <b>append</b> is enabled, previous values for <b>box</b>,
  <b>fill</b>, <b>round</b>, the plotting viewport (<b>vx1</b>, <b>vx2</b>, 
  <b>vy1</b>, <b>vy2</b>), and the plotting window (<b>wx1</b>, <b>wx2</b>, 
  <b>wy1</b>, <b>wy2</b>) are used.
  </p>
  <p>
  By default, the plot drawn will fill the device viewport.  Setting
  the value of <b>fill</b>  to <span style="font-family: monospace;">"no"</span> means the viewport will be adjusted so 
  that equal numbers of data values in x and y will occupy equal lengths 
  when plotted.  That is, when <b>fill = no</b>, a unity aspect ratio is 
  enforced, and plots
  appear square regardless of the device aspect ratio.  On devices with non 
  square full device viewports (e.g., the vt640), a plot drawn by
  PHISTOGRAM appears extended in the x direction unless <b>fill</b> = no.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Output the histogram of an image to a file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; phist M51.imh li+ nbins=100 &gt; fits1.hst
  </pre></div>
  <p>
  2. Plot the histogram of an image using only values from 0 to 2000.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; phist M31.imh nbins=100 z1=0. z2=2000.
  </pre></div>
  <p>
  3. Ditto, but set the histogram resolution explicitly to avoid
  smoothing the histogram.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; phist M31.imh z1=0 z2=2000 nbins=2001
  </pre></div>
  <p>
  4. Plot the cumulative histogram.  This is most useful for images with
  fairly flat <span style="font-family: monospace;">"normal"</span> histograms.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; phist R50.imh hist=cum
  </pre></div>
  <p>
  5. Plot the histogram of a stream of values in the textfile <span style="font-family: monospace;">"list"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; phist list
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  If the resolution of the histogram (number of bins) is a non-integral multiple
  of the intensity resolution of the data (number of possible intensity values),
  then <i>aliasing</i> can occur.  The effect is to cause periodic zero dropouts
  (for an oversampled histogram) or excess-valued bins (for a slightly
  undersampled histogram).  The <i>autoscaling</i> feature, if enabled, will
  adjust the histogram parameters to avoid such aliasing effects for integer
  data.  This is not possible for floating point data, however, in which case
  aliasing is certainly possible and can only be avoided by manually adjusting
  the histogram parameters.  One should also be aware that <i>smoothing</i> of
  the histogram will occur whenever the data range exceeds the histogram
  resolution.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  listpixels, plot.graph, proto.mkhistogram
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

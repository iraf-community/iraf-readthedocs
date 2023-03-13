.. _gkimosaic:

gkimosaic: Condense metacode frames to fit on one page
======================================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  gkimosaic input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The metacode input, which can be redirected from STDIN or read from
  one or more binary metacode files.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>If <b>output</b> is specified, the mosaiced metacode is spooled to this
  file for later plotting.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "stdgraph"' -->
  <dd>Output plotting device.
  </dd>
  </dl>
  <dl id="l_nx">
  <dt><b>nx = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nx' Line='nx = 2' -->
  <dd>The number of plots to draw in the x direction.
  </dd>
  </dl>
  <dl id="l_ny">
  <dt><b>ny = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ny' Line='ny = 2' -->
  <dd>The number of plots to draw in the y direction.
  </dd>
  </dl>
  <dl id="l_fill">
  <dt><b>fill = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fill' Line='fill = no' -->
  <dd>The plots are reduced by equal factors in x and y when <b>fill</b> = no. 
  </dd>
  </dl>
  <dl id="l_rotate">
  <dt><b>rotate = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rotate' Line='rotate = no' -->
  <dd>Output the mosaiced plots rotated by 90 degrees.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>If plotting to <b>stdgraph</b>, interactively examine each page of plots.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">"stdgcur"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = "stdgcur"' -->
  <dd>Source of cursor input.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <b>gkimosaic</b> condenses the plots in a metacode file to fit
  on a single page.  The plots can be examined interactively after
  each pageful.  The number of plots in x and y can be specified.  This
  task is useful for browsing through a large metacode file, and for
  compactly plotting a large number of metacode frames.
  </p>
  <p>
  When <b>fill</b> = no, the plots will be
  reduced by equal factors in x and y; the aspect ratio of the original 
  plot is preserved.  When <b>fill</b> = yes, the transformations in x and
  y are handled separately, meaning that the reduction factors will not
  be equal unless <b>nx</b> = <b>ny</b>.  
  </p>
  <p>
  The mosaiced plots are drawn on the page rotated by 90 degrees
  when <b>rotate</b> = yes.  This means the x axis of the plots can be
  placed along either the page width or length.
  The plots can be output to a plotting <b>device</b>,
  or spooled in file <b>output</b> for later plotting.
  </p>
  <p>
  If plotting to <b>stdgraph</b>, the plot can be interactively
  examined after each page of output by setting <b>interactive</b> = yes.
  The world coordinate system information of the individual plots has 
  been retained for cursor readback.
  Standard cursor mode keystroke commands are available as well as the
  <i>gkimosaic</i> specific commands listed below.  Colon commands :nx, :ny, 
  :fill and :rotate take effect on the next page of output.  Command :skip
  allows you to browse through a metacode file, skipping either forward or
  backward by N input plots.
  </p>
  <div class="highlight-default-notranslate"><pre>
  q                               quit
  return                          quit
  spacebar                        continue
  ?                               print help information
  
  :nx N                           change value of nx to N
  :ny N                           change value of ny to N
  :fill yes, :fill+, :fill        sets fill = yes
  :fill no, :fill-                sets fill = no
  :rotate yes, :rotate+, :rotate  sets rotate = yes
  :rotate no, :rotate-            sets rotate = no
  :skip +/-N                      skip forward/backward N plots
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Plot every frame in the metacode file <span style="font-family: monospace;">"oned.plots"</span>.  There will be 4 plots
  to the page originally, but this can be overridden interactively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gkimosaic oned.plots
  </pre></div>
  <p>
  2. Extract every third plot from the metacode file <span style="font-family: monospace;">"oned.plots"</span> with task
  <i>gkiextract</i> and plot them four to a page.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gkiextract oned.plots 1-99x3 | gkimosaic
  </pre></div>
  <p>
  3. Plot all frames in every metacode file beginning with <span style="font-family: monospace;">"mcode."</span> and
  condense them so 16 fit on a page.  The metacode is being spooled;
  it will be plotted, perhaps, when the computer isn't so busy.  Interactive
  mode is automatically disabled when not plotting to a graphics terminal.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gkimosaic mcode.* nx=4 ny=4 output=plt.spool
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Setting <b>device</b> to <span style="font-family: monospace;">"stdvdm"</span> does not work.  To produce an output file
  of mosaiced metacode, use the <i>output</i> parameter or the <span style="font-family: monospace;">"&gt;G"</span> graphics 
  stream redirection feature of the cl.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  gkidir, gkiextract
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

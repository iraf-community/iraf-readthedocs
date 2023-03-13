.. _mkhistogram:

mkhistogram: List or plot the histogram of a data stream (noao.proto V2.9)
==========================================================================

**Package: obsolete**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkhistogram file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_file">
  <dt><b>file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file' Line='file' -->
  <dd>The name of the text file containing the data (may be STDIN).
  </dd>
  </dl>
  <dl id="l_nbins">
  <dt><b>nbins</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nbins' Line='nbins' -->
  <dd>The number of bins in the histogram.
  </dd>
  </dl>
  <dl id="l_z1">
  <dt><b>z1 = INDEF, z2 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='z1' Line='z1 = INDEF, z2 = INDEF' -->
  <dd>The minimum and maximum histogram intensity. Z1 and z2 default to the data
  minimum and maximum.
  </dd>
  </dl>
  <dl id="l_listout">
  <dt><b>listout = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listout' Line='listout = yes' -->
  <dd>List instead of plot the histogram.
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
  MKHISTOGRAM calculates the histogram of the data in the text
  file <i>file</i> using
  the parameters <i>nbins</i>, <i>z1</i> and <i>z2</i>. If the z1 or z2 are
  undefined the image min or max is used. If <i>listout</i> = no, the
  histogram is plotted on the graphics device specified by <i>device</i>.
  Otherwise the histogram is listed on the standard output.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Output the histogram of data to a file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkhisto magsdata nbins=100 &gt; magsdata.hst
  </pre></div>
  <p>
  2. Plot the histogram of data between the 12.0  and 26.0 with a binsize
     if 0.5 on standard graph. Notice that the extra bin will contain
     points for which z2 is exactly 26.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkhist magsdat nbins=29 z1=12.0 z2=26.0 li-
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_use_instead">
  <h3>Use instead</h3>
  <p>
  plot.phistogram
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  images.imhistogram, fields
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'USE INSTEAD' 'SEE ALSO'  -->
  

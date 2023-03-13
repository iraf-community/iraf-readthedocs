.. _qstatistics:

qstatistics: Calculate image statistics for multi-amplifier CCD images
======================================================================

**Package: quadred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  qstatistics images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of image names in <b>quadformat</b>.
  </dd>
  </dl>
  <dl id="l_window">
  <dt><b>window = <span style="font-family: monospace;">"datasec"</span> (datasec|trimsec|biassec)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='window' Line='window = "datasec" (datasec|trimsec|biassec)' -->
  <dd>Type of section to output.  The choices are <span style="font-family: monospace;">"datasec"</span> for the amplifier
  section which includes the bias if any is present, <span style="font-family: monospace;">"trimsec"</span> for the trim
  section, and <span style="font-family: monospace;">"biassec"</span> for the bias section.
  </dd>
  </dl>
  <p>
  The remaining parameters come from the <b>imstatistics</b> task.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This script tasks uses the <b>quadsections</b> task to break the
  <b>quadformat</b> data into separate sections and runs the <b>imstatistics</b>
  task on the sections.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To compute the mean and stddev of the data section.
  </p>
  <div class="highlight-default-notranslate"><pre>
  qu&gt; qstat quad0072 fields=image,mean,stddev
  #               IMAGE      MEAN    STDDEV
   quad0072[1:1034,1:1024]     5537.     2647.
   quad0072[1163:2196,1:1024]     6210.     5439.
   quad0072[1:1034,1025:2048]     5364.     2535.
   quad0072[1163:2196,1025:2048]     5862.     1327.
  </pre></div>
  <p>
  2. To compute the mean and stdev of the bias section.
  </p>
  <div class="highlight-default-notranslate"><pre>
  qu&gt; qstat quad0072 fields=image,mean,stddev window=biassec
  #               IMAGE      MEAN    STDDEV
   quad0072[1045:1098,1:1024]      713.     1.272
   quad0072[1099:1152,1:1024]     516.2     1.425
   quad0072[1045:1098,1025:2048]     554.3     1.347
   quad0072[1099:1152,1025:2048]     530.3     1.377
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  quadformat, quadsections, imstatistics
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

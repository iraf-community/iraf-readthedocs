.. _qhistogram:

qhistogram: Make histogram of multi-amplifier CCD image
=======================================================

**Package: quadred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  qhistogram images
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
  <dd>Type of section to use for histogram.  The choices are <span style="font-family: monospace;">"datasec"</span> for the
  amplifier section which includes the bias if any is present, <span style="font-family: monospace;">"trimsec"</span> for
  the trim section, and <span style="font-family: monospace;">"biassec"</span> for the bias section.
  </dd>
  </dl>
  <p>
  The remaining parameters come from the <b>imhistogram</b> task.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This script tasks uses the <b>quadsections</b> task to break the
  <b>quadformat</b> data into separate sections and runs the <b>imhistogram</b>
  task on the sections.  The graphics is collected onto a single page.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To graph the histograms (default behavior).
  </p>
  <div class="highlight-default-notranslate"><pre>
  qu&gt; qhist quad0072
  [graph appears]
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  quadformat, quadsections, imhistogram
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

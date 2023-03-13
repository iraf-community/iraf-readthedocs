.. _crcombine:

crcombine: Combine multiple exposures to eliminate cosmic rays
==============================================================

**Package: crutil**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  crcombine input output
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <p>
  See parameters for <b>imcombine</b>.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task is a version of <b>imcombine</b>.  See the help for that task
  for a description of the parameters and algorithms.
  </p>
  <p>
  For the purpose of removing cosmic rays the most useful options
  are the <span style="font-family: monospace;">"crreject"</span> algorithm and/or combining with a median.  Many other
  options may work as well.  The best use of this task depends on the
  number of images available.  If there are more than a few images the
  images should be combined with an <span style="font-family: monospace;">"average"</span> and using a rejection
  algorithm.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To combine two images using the gain and read noise parameters in
  the image header:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; crcombine obj012,obj013 abc gain=gain rdnoise=rdnoise
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcombine
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

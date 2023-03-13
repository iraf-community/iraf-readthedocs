.. _quadsplit:

quadsplit: Split quadformat data into individual single amplifier images
========================================================================

**Package: quadred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  quadsplit input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Image name of <i>quadformat</i> image to be split.  This task does not
  allow a list of input names.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>Output root name to which the AMPLIST amplifier identifiers will be
  appended to form the split images.  If no output name is given then
  the input name is used as the root name.
  </dd>
  </dl>
  <dl id="l_clobber">
  <dt><b>clobber = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clobber' Line='clobber = yes' -->
  <dd>Clobber any existing images?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Images in <span style="font-family: monospace;">"quadformat"</span> (see help topic <b>quadformat</b>) are separated
  into images containing data from only one amplifier.  The output images
  have a common root name and then an extension given by the amplifier
  labels in the AMPLIST keyword.  The output root name may be specified
  or default to the input name.
  </p>
  <p>
  In addition to producing the individual images keywords, are added that
  are understood by the standard <b>ccdproc</b> task for single amplifier
  CCD reductions.
  </p>
  <p>
  The task <b>quadjoin</b> may be used to rejoin images that were split
  by this task.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To spit an image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  qu&gt; quadsplit quad0072
  qu&gt; dir quad0072*
  quad0072.11.imh     quad0072.21.imh     quad0072.imh
  quad0072.12.imh     quad0072.22.imh
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  quadformat, quadjoin
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

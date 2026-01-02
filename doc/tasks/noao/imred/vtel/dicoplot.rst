.. _dicoplot:

dicoplot: Make dicomed plots of carrington maps.
================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  dicoplot input_image1 input_image2 rot_number
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input_image1">
  <dt><b>input_image1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input_image1' Line='input_image1' -->
  <dd>First image to plot on the output.
  </dd>
  </dl>
  <dl id="l_input_image2">
  <dt><b>input_image2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input_image2' Line='input_image2' -->
  <dd>Second image to plot on the output.
  </dd>
  </dl>
  <dl id="l_rot_number">
  <dt><b>rot_number</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rot_number' Line='rot_number' -->
  <dd>Carrington rotation number.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Dicoplot produces plots on the Dicomed.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To make a plot containing a 10830 gram and the associated weight gram where
  the carrington rotation number is 1841, the 10830 gram is <span style="font-family: monospace;">"temp1"</span>,
  and the weight gram is <span style="font-family: monospace;">"carweight"</span> type:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; dicoplot temp1 carweight 1841
  </pre></div>
  <p>
  The program gets information about the dates and longitudes from the image
  headers.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

.. _putsqib:

putsqib: Merge a squibby brightness image into a full disk image.
=================================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  putsqib inputimage sqibimage outputimage
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inputimage">
  <dt><b>inputimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inputimage' Line='inputimage' -->
  <dd>Name of data image to merge with squibby brightness image.
  </dd>
  </dl>
  <dl id="l_sqibimage">
  <dt><b>sqibimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sqibimage' Line='sqibimage' -->
  <dd>Name of squibby brightness image to merge with data image.
  </dd>
  </dl>
  <dl id="l_outputimage">
  <dt><b>outputimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outputimage' Line='outputimage' -->
  <dd>Name of new, merged, output image.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Putsqib accepts as input a data image and a squibby brightness image.  It
  multiplies each pixel in the input data image by 16 and adds the associated
  pixel from the squibby brightness input image.  The pixel is then written
  to the new, output image.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To merge a data image called 'data' and a squibby brightness image called
  'sqib' and store the result in an image called 'complete', the command
  would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; putsqib data sqib complete
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  getsqib
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

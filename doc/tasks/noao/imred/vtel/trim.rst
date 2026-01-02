.. _trim:

trim: Set all pixels outside the limb to 0.0 (use sqib for limb).
=================================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  trim inputimage threshold
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inputimage">
  <dt><b>inputimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inputimage' Line='inputimage' -->
  <dd>Name of data image to trim.
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold' -->
  <dd>Squibby brightness value to use as a threshold in determining the limb.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Trim scans all the pixels in an image and sets those pixels to zero that
  contain a squibby brightness smaller than the threshold value.  This is
  done in place, that is, the input image gets modified.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To trim a data image called 'data' with a squibby brightness threshold
  of 4 (the standard value) the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; trim data 4
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  getsqib, putsqib
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

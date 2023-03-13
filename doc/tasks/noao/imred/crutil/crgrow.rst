.. _crgrow:

crgrow: Grow cosmic rays in cosmic ray masks
============================================

**Package: crutil**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  crgrow input output radius
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of cosmic ray masks to be modified.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output modified cosmic ray masks.  The input and output lists must
  match.  If the input and output cosmic ray masks are specified as the same
  then the input mask will be modified in place.
  </dd>
  </dl>
  <dl id="l_radius">
  <dt><b>radius = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radius' Line='radius = 1.' -->
  <dd>Replacement radius around cosmic rays.
  If a pixel is within this distance of a cosmic ray pixel
  it is identified by a value of 1 in the output cosmic ray mask.  Distances are
  measured between pixel centers which are have integer coordinates.
  </dd>
  </dl>
  <dl id="l_inval">
  <dt><b>inval = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inval' Line='inval = INDEF' -->
  <dd>Mask value to be grown.  A value of INDEF will grow all non-zero values.
  </dd>
  </dl>
  <dl id="l_outval">
  <dt><b>outval = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outval' Line='outval = INDEF' -->
  <dd>Mask value for grown pixels.  A value of INDEF will use the value of the
  pixel being grown for the grown pixel value.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The cosmic ray pixels, identified by the <span style="font-family: monospace;">"inval"</span> parameter, in the input
  mask are located and all unmasked (zero valued) pixels within the specified
  grow radius are set to a value given by the <span style="font-family: monospace;">"outval"</span> parameter. The
  distance between pixels is measured as a cartisian logical pixel coordinate
  distance.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  A radius of 1 will grow cosmic rays in a <span style="font-family: monospace;">"plus"</span> pattern.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; crgrow crmask1 crmask2 1
  </pre></div>
  <p>
  2.  A radius of 1.5 will grow cosmic rays in a box pattern.  The following
  will modify the input mask.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; crgrow crmask crmask 1.5
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imreplace
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

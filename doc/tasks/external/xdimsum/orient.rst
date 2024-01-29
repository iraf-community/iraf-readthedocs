.. _orient:

orient: Reorient image to N up and E left or undo re-orientation
================================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  orient input y2n_angle
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The name of the input image to be reoriented.
  </dd>
  </dl>
  <dl id="l_y2n_angle">
  <dt><b>y2n_angle</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='y2n_angle' Line='y2n_angle' -->
  <dd>The angle in degrees from the image y axis to the north axis measured from north
  through east. Y2n_angle must be between 0.0 and 360.0 degrees.
  </dd>
  </dl>
  <dl id="l_rotation">
  <dt><b>rotation = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rotation' Line='rotation = yes' -->
  <dd>Is the rotation of the input image north axis to the east axis
  counter-clockwise ? 
  </dd>
  </dl>
  <dl id="l_invert">
  <dt><b>invert = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='invert' Line='invert = no' -->
  <dd>Invert the original reorientation ? If invert = yes then the input image
  is returned to its original orientation.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  ORIENT orients the input image <i>input</i>  to within 45 degrees of north
  up and east to the left using the geometry parameters <i>y2n_angle</i> and
  <i>rotation</i>. The reorientation operation can be undone by setting
  <i>invert</i> = yes.
  </p>
  <p>
  ORIENT is used by the XNREGISTAR task to orient the output combined image
  to within 45 degrees of north up and east left, and by the MASKDEREG task
  to return the object mask created from the combined image to the original
  orientation before creating object masks for the individual images.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Reorient an image which is already in the default orientation, i.e.
  do nothing.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; orient ss_demo01 0.0 rotation+ invert-
  </pre></div>
  <p>
  2. Reorient an image with north pointing left and east pointing down.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; orient ss_demo01 90.0 rotation+ invert-
  </pre></div>
  <p>
  3. Reorient an image with north pointing left and east pointing up and
  then return it to the original orientation.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; orient ss_demo01 90.0 rotation- invert-
  cl&gt; orient ss_demo01 90.0 rotation- invert+
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  xnregistar, maskdereg
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _crfix:

crfix: Fix cosmic rays in images using cosmic ray masks
=======================================================

**Package: crutil**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  crfix input output masks
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input two dimensional image to be <span style="font-family: monospace;">"fixed"</span> (modified) by linear interpolation.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output image.  If the output image name exactly matches the input
  image name (including extensions) then the image will be modified in place.
  </dd>
  </dl>
  <dl id="l_crmask">
  <dt><b>crmask</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crmask' Line='crmask' -->
  <dd>Cosmic ray mask identifying the cosmic rays to be fixed.  The mask
  values are zero for good data and non-zero for cosmic rays.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The input and output images are specified by the <i>input</i> and
  <i>output</i> parameters.  If the input and output image names are
  identifical (including extensions) then image is modified in place.  Cosmic
  rays, identified in a cosmic ray mask specified by the <i>crmask</i>
  parameter, are replaced in the output image by linear interpolation along
  lines or columns using the nearest good pixels.  The special mask name
  <span style="font-family: monospace;">"BPM"</span> may be used to select a mask name given in the input image header
  under the keyword <span style="font-family: monospace;">"BPM"</span>.
  </p>
  <p>
  Cosmic ray pixels are <span style="font-family: monospace;">"fixed"</span> by replacing them with values
  by linear interpolation to the nearest pixels not identified as bad.
  The interpolation direction is the shortest length between good pixels
  along columns or lines.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To replace cosmic rays in an image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; crfix obj012 crobj012 crmask012
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fixpix, crmedian, crnebula, cosmicrays, credit, epix
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

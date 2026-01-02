.. _getsqib:

getsqib: Extract the squibby brightness image from a full disk scan.
====================================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  getsqib inputimage outputimage
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inputimage">
  <dt><b>inputimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inputimage' Line='inputimage' -->
  <dd>Name of image to get squibby brightness from.
  </dd>
  </dl>
  <dl id="l_outputimage">
  <dt><b>outputimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outputimage' Line='outputimage' -->
  <dd>Name of new output squibby brightness image.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Getsqib takes as input any full disk image and extracts the lower four bits
  from each pixel and stores this information in a new output image the same
  size as the input image.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To extract the squibby brightness image from the image <span style="font-family: monospace;">"test1"</span> and store
  it in an image called <span style="font-family: monospace;">"test1.sqib"</span> the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; getsqib test1 test1.sqib
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  putsqib
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

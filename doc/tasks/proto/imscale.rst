.. _imscale:

imscale: Scale an image to a specified (windowed) mean
======================================================

**Package: proto**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  imscale input output mean
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input image to be scaled.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output scaled image.
  </dd>
  </dl>
  <dl id="l_mean">
  <dt><b>mean</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mean' Line='mean' -->
  <dd>Scale the output image to this mean value.
  </dd>
  </dl>
  <dl id="l_lower">
  <dt><b>lower = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lower' Line='lower = INDEF' -->
  <dd>Lower limit of window for calculating the input image mean.  INDEF corresponds
  to the minimum possible pixel value.
  </dd>
  </dl>
  <dl id="l_upper">
  <dt><b>upper = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='upper' Line='upper = INDEF' -->
  <dd>Upper limit of window for calculating the input image mean.  INDEF corresponds
  to the maximum possible pixel value.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print the calculated input and output image means.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The mean of the <i>input</i> image between the limits <i>lower</i>
  and <i>upper</i> is computed.  The image is then scaled to the
  specified output <i>mean</i>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To scale an image to a unit mean excluding deviant points below
  1000 and above 5000.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imscale calib flat 1 lower=1000 upper=5000
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES'  -->
  

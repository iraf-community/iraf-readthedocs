.. _normflat:

normflat: Create a flat field by normalizing and replacing low values
=====================================================================

**Package: generic**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  normflat image flatfield
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Calibration image to be used.
  </dd>
  </dl>
  <dl id="l_flatfield">
  <dt><b>flatfield</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flatfield' Line='flatfield' -->
  <dd>Flat field to be created.
  </dd>
  </dl>
  <dl id="l_norm">
  <dt><b>norm = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='norm' Line='norm = INDEF' -->
  <dd>Normalization factor to be used if not INDEF.  If INDEF the normalization
  factor is automatically determined.
  </dd>
  </dl>
  <dl id="l_minflat">
  <dt><b>minflat = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minflat' Line='minflat = INDEF' -->
  <dd>Minimum data value to be used in determining the normalization and in
  creating the flat field.  Values less than or equal to this value are
  replaced with a flat field value of 1.
  </dd>
  </dl>
  <dl id="l_sample_section">
  <dt><b>sample_section = <span style="font-family: monospace;">"[]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample_section' Line='sample_section = "[]"' -->
  <dd>Section of the image to be sampled in determining the normalization if
  norm = INDEF.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A flat field is created from a calibration image by normalizing the calibration
  image.  The normalization is specified with the parameter <i>norm</i>.  If the
  value of <i>norm</i> is INDEF then the normalization is determined by sampling
  the pixels in the sample section with values greater than <i>minflat</i>.
  This task differs from the task <b>normalize</b> in that data values less
  than or equal to <i>minflat</i> are replaced with unity in the normalized
  flat field.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To create a flat field from a calibration image <span style="font-family: monospace;">"quartz"</span> using pixels
  above 1000 and selecting the normalization to be 3500:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; normflat quartz flat norm=3500 minflat=1000
  </pre></div>
  <p>
  To determine a normalization from the pixels above 1000 and sampling
  every fifth pixel in each dimension:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; normflat quartz flat minflat=1000 sample=[*:5,*:5]
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  normalize
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

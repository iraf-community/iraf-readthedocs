.. _flatten:

flatten: Flatten images using a flat field
==========================================

**Package: generic**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  flatten images flatfield
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>Images to be flattened.
  </dd>
  </dl>
  <dl id="l_flatfield">
  <dt><b>flatfield</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flatfield' Line='flatfield' -->
  <dd>Flat field image to be divided into the images.
  </dd>
  </dl>
  <dl id="l_minflat">
  <dt><b>minflat = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minflat' Line='minflat = INDEF' -->
  <dd>All flat field pixels less than or equal to this value are replaced by
  unit response.  If INDEF all the flat field pixels are used.
  </dd>
  </dl>
  <dl id="l_pixtype">
  <dt><b>pixtype = <span style="font-family: monospace;">"real"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixtype' Line='pixtype = "real"' -->
  <dd>The pixel datatype of the flattened image.  The null string (<span style="font-family: monospace;">""</span>) defaults
  the pixel datatype to that of the original image before flattening.
  The other choices are <span style="font-family: monospace;">"short"</span>, <span style="font-family: monospace;">"integer"</span>, <span style="font-family: monospace;">"long"</span>, and <span style="font-family: monospace;">"real"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Each of the <i>images</i> is flatten by dividing by the <i>flatfield</i>
  flat field image.  The flattened images replace the original images.
  The pixel datatype of the flattened images is specified by the
  <i>pixtype</i>.  The null string (<span style="font-family: monospace;">""</span>) leaves the datatype of the images
  unchanged.  Low values in the flat field may be replaced by unit response
  by specifying a <i>minflat</i> value.  All pixels in the flat field less
  than or equal to <i>minflat</i> are given unit response.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To flatten a set of two dimensional images excluding pixels below
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; flatten frame* flat minflat=0.2
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES'  -->
  

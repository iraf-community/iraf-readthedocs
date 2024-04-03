.. _magpar:

magpar: Set magnitude scale parameters (pset).
==============================================

**Package: isophote**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  magpar
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  For the sake of convenience, the 'ellipse' task output includes 
  intensity-related quantities such as isophotal, ellipse and circle-enclosed 
  intensities, expressed in a magnitude scale.  
  This scale is derived from task parameters 'mag0', 'refer', and 
  'zerolevel', and from the corresponding intensity output parameter, 
  according  to the following relation: 
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  m  = mag0  - 2.5 * log10 ((intens - zerolevel) / refer)
  
  </pre></div>
  <p>
  where 'mag0' and 'refer' are used to set the scale's zero-point,
  and 'zerolevel' can be used to subtract any bias-type offset that applies
  to all pixels in the image. 
  </p>
  <p>
  Notice that this magnitude output is provided basically for convenience 
  in visualization (e.g. by tasks 'isoplot' and 'isopall'), and not intended
  for subsequent detailed analysis.
  In particular, negative intensities (from, say, a sky-subtracted image) 
  result in magnitudes being computed by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  m  = mag0  - 2.5 * log10 (1. / refer)
  
  </pre></div>
  <p>
  Any type of pixel data can be input to the fitting algorithm in 'ellipse':
  linear intensity,
  magnitude, photographic density, etc.  However, correct intensity and
  magnitude scales, and harmonic amplitudes, will result only in the case
  of linear intensity pixels.  
  </p>
  <dl>
  <dt><b>(mag0 = 0.0) [real]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(mag0 = 0.0) [real]' -->
  <dd>Magnitude of the reference source.
  </dd>
  </dl>
  <dl>
  <dt><b>(refer = 1.0) [real, min=1.E-5]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(refer = 1.0) [real, min=1.E-5]' -->
  <dd>Intensity of the reference source. 
  </dd>
  </dl>
  <dl>
  <dt><b>(zerolevel = 0.0) [real]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(zerolevel = 0.0) [real]' -->
  <dd>Intensity of the zero (bias) signal.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  An image has an average sky level of 120 ADU/pixel, and it is know that the
  sky brightness is 22.5 mag/arcsec^2. The detector adds a 100 ADU bias level
  at every pixel.
  A magnitude scale roughly calibrated 
  in magnitudes/arcsec^2 can be defined by setting
  </p>
  <div class="highlight-default-notranslate"><pre>
  magpar.mag0      =  22.5
  magpar.refer     = 120.0
  magpar.zerolevel = 100.0
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ellipse, elcursor
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

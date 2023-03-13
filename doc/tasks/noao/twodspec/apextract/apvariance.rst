.. _apvariance:

apvariance: Extractions, variance weighting, cleaning, and noise model
======================================================================

**Package: apextract**

.. raw:: html

  <div class="highlight-default-notranslate"><pre>
      none:   S = sum { I - B }
  variance:   S = sum { (P**2 / V) (I - B) / P } / sum { P**2 / V }
  </pre></div>
  <div class="highlight-default-notranslate"><pre>
  (1) V = max (VMIN, (R**2 + I + VB) / G**2)
          max (VMIN, (R**2 + S * P + B + VB) / G**2)
  
  (2) VB = 0.                 if (B = 0)
         = B / (N - 1)        if (B &gt; 0)
  
  (3) VMIN = 1 / G**2         if (R = 0)
             R**2 / G**2      if (R &gt; 0)
  </pre></div>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  apbackground approfiles apall apsum
  </p>
  
  </section>
  
  <!-- Contents: 'SEE ALSO'  -->
  

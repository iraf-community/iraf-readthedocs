.. _photpars:

photpars: Edit the aperture photometry parameters
=================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  photpars
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_weighting">
  <dt><b>weighting = <span style="font-family: monospace;">"constant"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='weighting' Line='weighting = "constant"' -->
  <dd>The type of weighting. The weighting is ignored by the PHOT task. The options
  are:
  <dl>
  <dt><b>constant</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='constant' Line='constant' -->
  <dd>Uniform weights of 1 for each pixel are used.
  </dd>
  </dl>
  <dl>
  <dt><b>cone</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='cone' Line='cone' -->
  <dd>A conical weighting function of full width half maximum <i>fwhmpsf</i> as
  defined in the DATAPARS parameter set is used.
  </dd>
  </dl>
  <dl>
  <dt><b>gauss</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='gauss' Line='gauss' -->
  <dd>A Gaussian weighting function of full width half maximum <i>fwhmpsf</i> as
  defined in the DATAPARS parameter set is used.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">"3"</span> (scale units)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = "3" (scale units)' -->
  <dd>A list of aperture radii in units of the  scale parameter or the name of the
  file containing the list of apertures. List elements may be separated by
  whitespace or commas. A ranges syntax of the form ap1:apN:apstep is also
  supported. 
  </dd>
  </dl>
  <dl id="l_zmag">
  <dt><b>zmag = 25.00</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zmag' Line='zmag = 25.00' -->
  <dd>The zero point offset for the magnitude scale. 
  </dd>
  </dl>
  <dl id="l_mkapert">
  <dt><b>mkapert = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mkapert' Line='mkapert = no' -->
  <dd>Mark the photometry apertures on the displayed image?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The integral of the flux within the circular apertures specified by
  <i>apertures</i> is computed by summing pixels in the aperture with
  the specified weighting function <i>weighting</i>. The fraction of each pixel
  lying within the aperture is computed by an approximation and all the
  approximations are summed.  The zero point of the magnitude
  scale is determined by <i>zmag</i>.
  </p>
  <p>
  Apertures is specified in units of the image scale. If <i>scale</i>
  is specified in units of the half-width at half-maximum of the point
  spread function the aperture per pixel  a single value of apertures
  will work well on images with differing psfs.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the PHOTPARS parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; lpar photpars
  </pre></div>
  <p>
  2. Edit the PHOTPARS parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; photpars
  </pre></div>
  <p>
  3. Edit the PHOTPARS parameters from with the PHOT task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; epar phot
  
      ... edit a few phot parameters
  
      ... move to the photpars parameter and type :e
  
      ... edit the photpars parameters and type :wq
  
      ... finish editing the phot parameters and type :wq
  </pre></div>
  <p>
  4. Save the current PHOTPARS parameter set in a text file photnite1.par.
     This can also be done from inside a higher level task as in the above
     example.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; photpars
  
      ... type ":w photnite1.par"  from within epar
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
  epar,datapars,centerpars,fitskypars,phot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _polypars:

polypars: Edit the polyphot parameters
======================================

**Package: apphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  polypars
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_zmag">
  <dt><b>zmag = 25.00</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zmag' Line='zmag = 25.00' -->
  <dd>The zero point offset for the magnitude scale.
  </dd>
  </dl>
  <dl id="l_mkpolygon">
  <dt><b>mkpolygon = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mkpolygon' Line='mkpolygon = no' -->
  <dd>Draw the polygons on the screen.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The zero point of the magnitude scale is determined by <i>zmag</i>.
  </p>
  <p>
  If the <i>mkpolygon</i> switch is enabled polygons are marked on the screen.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the polygonal aperture photometry parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; lpar polypars
  </pre></div>
  <p>
  2. Edit the polygonal aperture photometry parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; polypars
  </pre></div>
  <p>
  3. Edit the POLYPARS parameters from within the POLYPHOT task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; epar polyphot
  
      ... edit a few polyphot parameters
  
      ... move to the polypars parameter and type :e
  
      ... edit the polypars parameters and type :wq
  
      ... finish editing the polyphot parameters and type :wq
  </pre></div>
  <p>
  4. Save the current POLYPARS parameter set in a text file polynite1.par.
  This can also be done from inside a higher level task as in the
  above example.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; polypars
  
      ... edit some parameters
  
      ... type ":w polynite1.par"  from within epar
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
  polyphot. polymark
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

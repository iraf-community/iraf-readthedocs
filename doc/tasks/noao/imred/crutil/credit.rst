.. _credit:

credit: Interactively edit cosmic rays using an image display
=============================================================

**Package: crutil**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  credit input output
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <p>
  See parameters for <b>imedit</b>.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task is a version of <b>imedit</b>.  See the help for that task
  for a description of the parameters and algorithms.
  </p>
  <p>
  For the purpose of editing cosmic rays the most useful editing option
  is <span style="font-family: monospace;">'b'</span> to replace cosmic rays in a circular annulus using local sky
  values.  This can be done interactively or using a list of positions
  along with the <i>default</i> parameter value.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To replace cosmic rays interactively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; credit obj012 crobj012 crmask012
  </pre></div>
  <p>
  2.  To use a two column list of positions and remove the cosmic rays using
  the <span style="font-family: monospace;">'b'</span> key algorithm.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; credit obj012 crobj012 cursor=crlist.dat display-
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imedit, epix
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

.. _back:

back: Return to the previous directory (after a chdir)
======================================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  back
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <p>
  None.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Back</i> is used after a call to <i>chdir</i> or <i>cd</i> to return to the
  previous directory.  Repetitive calls to <i>back</i> may be used to toggle
  between two directories.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Go to the logical directory <span style="font-family: monospace;">"dataio"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cd dataio
  </pre></div>
  <p>
  2. Return to the previous directory, and then go back to the dataio directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; back;back
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  chdir, pathnames
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

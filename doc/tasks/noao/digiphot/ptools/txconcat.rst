.. _txconcat:

txconcat: Concatenate a list of apphot/daophot text databases
=============================================================

**Package: ptools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  txconcat textfiles outfile
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_textfiles">
  <dt><b>textfiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='textfiles' Line='textfiles' -->
  <dd>The list of APPHOT/DAOPHOT text databases to be concatenated.
  </dd>
  </dl>
  <dl id="l_outfile">
  <dt><b>outfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outfile' Line='outfile' -->
  <dd>The name of the output APPHOT/DAOPHOT text database.
  </dd>
  </dl>
  <dl id="l_task">
  <dt><b>task = <span style="font-family: monospace;">"TASK"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='task' Line='task = "TASK"' -->
  <dd>The name of the keywords whose value is the name of the task which wrote
  the database.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  TXCONCAT is a simple task which accepts a list of APPHOT/DAOPHOT text
  database files and concatenates them into one resultant output file.
  TXCONCAT checks that all the file are indeed APPHOT/DAOPHOT text
  database files and that they were all written by the same task before
  performing the concatenation.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Concatenate a list of DAOPHOT PHOT task result files into a single
  output file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; txconcat m92r.mag.1,m92r.mag.2,m92r.mag.3 m92rall.mag.1
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
  ptools.tbconcat,ptools.pconcat,tables.tmerge,concatenate
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

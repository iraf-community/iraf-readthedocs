.. _pconcat:

pconcat: Concatenate a list of apphot/daophot databases
=======================================================

**Package: ptools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pconcat infiles outfile
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_infiles">
  <dt><b>infiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='infiles' Line='infiles' -->
  <dd>The list of APPHOT/DAOPHOT databases to be concatenated.
  </dd>
  </dl>
  <dl id="l_outfile">
  <dt><b>outfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outfile' Line='outfile' -->
  <dd>The name of the output APPHOT/DAOPHOT database.
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
  PCONCAT is a simple task which accepts a list of APPHOT/DAOPHOT
  database files and concatenates them into one resultant output file.
  PCONCAT checks that all the file are indeed APPHOT/DAOPHOT
  database files and that they were all written by the same task before
  performing the concatenation.
  </p>
  <p>
  PCONCAT is a simple script which call TXCONCAT in the PTOOLS package
  if the input files are text database files or TBCONCAT in the PTOOLS package
  if the input files are STSDAS database files. TBCONCAT is itself a script
  which call the TABLES package task TMERGE to do the actual work.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Concatenate a list of DAOPHOT package task GROUP output database files
  into a single output file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; pconcat m92r.grp.1,m92r.grp.2,m92r.grp.3 m92rall.grp.1
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
  ptools.txconcat,ptools.tbconcat,tables.tmerge,concatenate
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

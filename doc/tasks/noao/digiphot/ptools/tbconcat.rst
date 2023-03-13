.. _tbconcat:

tbconcat: Concatenate a list of apphot/daophot tables databases
===============================================================

**Package: ptools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tbconcat tables outtable
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_tables">
  <dt><b>tables</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tables' Line='tables' -->
  <dd>The list of APPHOT/DAOPHOT STSDAS databases to be concatenated.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable' -->
  <dd>The name of the output APPHOT/DAOPHOT STSDAS database.
  </dd>
  </dl>
  <dl id="l_task">
  <dt><b>task = <span style="font-family: monospace;">"TASK"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='task' Line='task = "TASK"' -->
  <dd>The name of the keyword whose value is the name of the task which wrote
  the database.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  TBCONCAT is a simple task which accepts a list of APPHOT/DAOPHOT STSDAS
  database files and concatenates them into one resultant database.
  TBCONCAT checks that all the file are indeed APPHOT/DAOPHOT STSDAS
  database files and that they were all written by the same task before
  performing the concatenation.
  </p>
  <p>
  TBCONCAT is a simple script built around the STSDAS TABLES package
  task TMERGE. Users should consult the manual page for TMERGE for
  more details about the inner working of the task.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Concatenate a list of DAOPHOT package GROUP output tables into a
  single file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; tbconcat m92r.grp.1,m92r.grp.2,m92r.grp.3 m92rall.grp.1
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
  ptools.txconcat,ptools.pconcat,tables.tmerge,concatenate
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

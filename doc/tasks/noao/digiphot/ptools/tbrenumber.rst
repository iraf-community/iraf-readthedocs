.. _tbrenumber:

tbrenumber: Renumber a list of  apphot/daophot tables databases
===============================================================

**Package: ptools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tbrenumber tables
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_tables">
  <dt><b>tables</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tables' Line='tables' -->
  <dd>The list of APPHOT/DAOPHOT STSDAS table databases to be renumbered.
  </dd>
  </dl>
  <dl id="l_idoffset">
  <dt><b>idoffset = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='idoffset' Line='idoffset = 0' -->
  <dd>An integer offset  to be added to the id numbers of the stars in
  the output renumbered photometry file. If idoffset is &gt; 0, the output
  id numbers will run from 1 + idoffset to N + idoffset instead of from 1 to N.
  </dd>
  </dl>
  <dl id="l_id">
  <dt><b>id = <span style="font-family: monospace;">"ID"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='id' Line='id = "ID"' -->
  <dd>The name of the keyword whose value is the sequence number of the object
  in the database.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  TBRENUMBER is a simple script task which accepts an APPHOT/DAOPHOT STSDAS
  table database and renumbers the objects from 1 + idoffset to N + idoffset,
  where N is the number
  of objects in the database. TBRENUMBER calls the TABLES package TCALC task
  to actually do the work.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Renumber a concatenated NSTAR photometry file that has been written with
  TBCONCAT.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; tbrenumber m92r.nst
  </pre></div>
  <p>
  2. Renumber a PHOT photometry file of extra stars so as to ensure the
  stars' id numbers are  greater than 4000.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; tbrenumber m92r.mag.extra idoffset=4000
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
  ptools.txrenumber,ptools.prenumber,tables.tcalc
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

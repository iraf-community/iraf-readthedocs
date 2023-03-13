.. _prenumber:

prenumber: Renumber stars in an apphot database
===============================================

**Package: apphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  renumber infile
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_infile">
  <dt><b>infile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='infile' Line='infile' -->
  <dd>The APPHOT/DAOPHOT database to be renumbered.
  </dd>
  </dl>
  <dl id="l_id">
  <dt><b>id = <span style="font-family: monospace;">"ID"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='id' Line='id = "ID"' -->
  <dd>The name of the keyword whose value is the sequence number of the object
  </dd>
  </dl>
  <dl id="l_idoffset">
  <dt><b>idoffset = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='idoffset' Line='idoffset = 0' -->
  <dd>An integer offset  to be added to the id numbers of the stars in
  the output renumbered photometry file. If idoffset is &gt; 0, the output
  id numbers will run from 1 + idoffset to N + idoffset instead of from 1 to N.
  in the database.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  PRENUMBER is a simple task which accepts an APPHOT/DAOPHOT
  database file and renumbers the objects in the file from 1 + idoffset
  to N + idoffset,
  where N is the number of objects in the database. A renumber operation is
  often performed
  after an append operation to insure that the database objects have unique id
  numbers or after a sort to put the id numbers in order.
  </p>
  <p>
  PRENUMBER is a script which executes TXRENUMBER if the APPHOT/DAOPHOT
  database is a text database or TCALC if the file is an STSDAS table
  database.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Renumber a sorted NSTAR database that has been sorted on magnitude.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; prenumber m92r.nst.1
  </pre></div>
  <p>
  2. Renumber a PHOT photometry file of extra stars so as to ensure the
  stars' id numbers are  greater than 4000.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; prenumber m92r.mag.extra idoffset=4000
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
  ptools.txrenumber,ptools.tbrenumber,tables.tcalc
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

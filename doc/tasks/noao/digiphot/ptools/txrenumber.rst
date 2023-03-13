.. _txrenumber:

txrenumber: Renumber a list of apphot/daophot text databases
============================================================

**Package: ptools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  txrenumber textfiles
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_textfiles">
  <dt><b>textfiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='textfiles' Line='textfiles' -->
  <dd>The APPHOT/DAOPHOT text database to be renumbered.
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
  <dd>The name of the keyword whose value is the sequence number of the object in
  the list. After renumbering the original values of the <i>id</i> are replaced
  by numbers 1 through N, where N is the total number of objects in the list.
  The id keyword must denote an integer quantity.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  TXRENUMBER is a simple task which accepts an APPHOT/DAOPHOT text
  database file and renumbers all the objects in the file beginning
  with 1 and ending with the number of objects in the file.
  The renumber operation is performed in place. The original
  values of the  <i>id</i> field are replaced by numbers 1 + idoffset
  through N + idoffset
  where N is the total number of objects in the list.
  A renumber operation is typically performed after another
  list operation such as TXCONCAT or TXSORT.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Renumber the stars in a concatenated file produced by TXCONCAT.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; txrenumber m92rall.mag.1
  </pre></div>
  <p>
  2. Renumber a PHOT photometry file of extra stars so as to ensure the
  stars' id numbers are  greater than 4000.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; txrenumber m92r.mag.extra idoffset=4000
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
  ptools.tbrenumber,ptools.prenumber,tables.tcalc
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

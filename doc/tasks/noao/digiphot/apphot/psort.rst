.. _psort:

psort: Sort an apphot database
==============================

**Package: apphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  psort infiles field
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_infiles">
  <dt><b>infiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='infiles' Line='infiles' -->
  <dd>The input APPHOT/DAOPHOT databases to be sorted. The sort is performed in place.
  </dd>
  </dl>
  <dl id="l_field">
  <dt><b>field</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='field' Line='field' -->
  <dd>The field to be sorted on. If the input file is a text database,
  <i>field</i> may be any quantity defined by
  the APPHOT/DAOPHOT #K and #N keywords. If the input file is an STSDAS
  table database <i>field</i> may be any column name. <i>Field</i> may be
  of type integer or real, in which case a numeric sort is performed,
  boolean, in which case the boolean constant <span style="font-family: monospace;">"no"</span> is assumed to have a
  smaller value than <span style="font-family: monospace;">"yes"</span>, or character in which case an alphabetic sort
  is performed.
  </dd>
  </dl>
  <dl id="l_ascend">
  <dt><b>ascend = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ascend' Line='ascend = yes' -->
  <dd>Sort in increasing value order.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  PSORT is a simple task which accepts an APPHOT/DAOPHOT database file
  and sorts it in place based on the value of the selected quantity
  <i>field</i>. By default the sort is in increasing order of the value
  of field, but a reverse sort can be performed by 
  setting <i>ascend</i> = no.
  </p>
  <p>
  If <i>field</i> is a real or integer the sort is numeric, if boolean
  the constant <span style="font-family: monospace;">"no"</span> is assumed to have a smaller value than <span style="font-family: monospace;">"yes"</span>, if
  character the sort is alphabetic.
  </p>
  <p>
  PSORT is a simple CL script which call TXSORT if the input database is
  a text file and TSORT if the input database is a text file.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Sort the output of the APPHOT task PHOT in increasing order of
  the y coordinate.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; psort m92.mag.1 YCENTER
  </pre></div>
  <p>
  2. Sort the output of the DAOPHOT task ALLSTAR in increasing order of
  magnitude.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; psort m92.al.1 MAG
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
  ptools.txsort,tables.tsort,ptools.tbsort
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _tproduct:

tproduct: Form the Cartesian product of two tables.
===================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tproduct intable1 intable2 outtable
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task creates an output table which is the Cartesian product of two input
  tables. This Cartesian product consists of every possible combination of the
  rows of the two input tables. Therefore, the number of rows in the output table
  is the product of the number of rows in the two input tables. The output table
  will contain all the columns from both input tables. If a column name in the
  first input table is the same as a column name in the second input table, this
  task tries to create a unique name by appending <span style="font-family: monospace;">"_1"</span> to the first name and <span style="font-family: monospace;">"_2"</span>
  to the second name. If the task cannot create a unique name in this way, it
  stops with an error. 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable1">
  <dt><b>intable1 [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable1' Line='intable1 [file name]' -->
  <dd>First input table.
  </dd>
  </dl>
  <dl id="l_intable2">
  <dt><b>intable2 [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable2' Line='intable2 [file name]' -->
  <dd>Second input table.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [file name]' -->
  <dd>Output table containing the possible Cartesian products.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Find all persons sharing a phone from a phone list:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tproduct phone.tab phone.tab phone.tmp
  tt&gt; tselect phone.tmp share.tmp "phone_1 == phone_2 &amp;&amp; name_1 &lt; name_2"
  tt&gt; tproject share.tmp share.tab phone_2 inc-
  tt&gt; delete *.tmp
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Bernie Simon.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  tselect, tproject, tjoin
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

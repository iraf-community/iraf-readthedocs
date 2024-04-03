.. _grafcheck:

grafcheck: Check an instrument graph table for bad rows.
========================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  grafcheck grftable
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task reads an instrument graph table, checks it for four types of errors,
  and displays an error message on the terminal screen (i.e., errors are
  written to STDOUT).
  </p>
  <p>
  The following errors are detected by 'grafcheck':
  </p>
  <dl>
  <dt><b>* Component name, keyword, input node, or output node are undefined.</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='* Component name, keyword, input node, or output node are undefined.' -->
  <dd></dd>
  </dl>
  <dl>
  <dt><b>* Output node number is less than input node number.</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='* Output node number is less than input node number.' -->
  <dd></dd>
  </dl>
  <dl>
  <dt><b>* Two or more nodes with the same input node have the same keywords.</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='* Two or more nodes with the same input node have the same keywords.' -->
  <dd>Leading blanks and case are ignored in determining uniqueness of keyword names,
  names that differ only in case are considered to be identical.
  </dd>
  </dl>
  <dl>
  <dt><b>* A row cannot be reached from the graph's starting node.</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='* A row cannot be reached from the graph's starting node.' -->
  <dd></dd>
  </dl>
  <p>
  When errors are located, a row will be printed for each type of error detected,
  along with the offending row.  When a row is in error, the component name is
  displayed, followed by the keyword, the input node, and the output node.  
  Component name and keyword are converted to lower case in the output
  and are enclosed in quotes.  No output is produced if no errors are located.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_grftable">
  <dt><b>grftable = mtab$*.tmg [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grftable' Line='grftable = mtab$*.tmg [file name]' -->
  <dd>The name of the graph table(s) to be checked. If a filename template
  is specified, the task will check the most recent graph table matching
  the template.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Check the graph table 'hstgraph.tab'.
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; grafcheck hstgraph.tab
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by B.Simon
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  graflist, grafpath, grafplot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

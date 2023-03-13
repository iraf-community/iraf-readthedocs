.. _columns:

columns: Convert multicolumn file to separate files
===================================================

**Package: lists**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  columns filename numcols 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_filename">
  <dt><b>filename</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filename' Line='filename' -->
  <dd>Name of the input table file.
  </dd>
  </dl>
  <dl id="l_numcols">
  <dt><b>numcols</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='numcols' Line='numcols' -->
  <dd>The number of columns in the input file.
  </dd>
  </dl>
  <dl id="l_outroot">
  <dt><b>outroot = <span style="font-family: monospace;">"col."</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outroot' Line='outroot = "col."' -->
  <dd>Root name of the output column files.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <i>columns</i> is used to reformat a multicolumn list file into separate
  files, such that one output file is created for each column in the input
  file.  It is used to break multicolumn tables into simple CL lists.
  Comment lines beginning with  the character <span style="font-family: monospace;">"#"</span> are ignored.  All data
  is transferred as text.  One file <b>outroot</b>n is produced for each
  column in the input table.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Make 3 files named datacol.1, datacol.2 and datacol.3 from the 3 column
  table dtable:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; columns dtable 3 outroot=datacol.
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fields
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

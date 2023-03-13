.. _unique:

unique: Delete redundant elements from a list
=============================================

**Package: lists**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  unique files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>List of files to be processed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <b>unique</b> reads the input comparing adjacent lines.  The second and
  successive copies of a line are removed; the remainder is passed on to the
  standard output.  
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Remove repeated names from a list.  Note the input file has been sorted 
  alphabetically so repeated names are adjacent.  
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sort names | unique &gt; names.final
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  sort
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

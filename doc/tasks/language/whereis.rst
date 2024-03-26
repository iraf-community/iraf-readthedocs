.. _whereis:

whereis: locate all occurences of a task in the package list
============================================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <div class="highlight-default-notranslate"><pre>
  which [task] [...]
  whereis [task] [...]
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_task">
  <dt><b>task</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='task' Line='task' -->
  <dd>Name of task to be located.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>which</i> command returns the first occurrence of a task in the currently
  loaded package list.  The <i>whereis</i> command returns all occurrences of that
  task in the package list.  More than one task may be supplied on the command
  line, unique abbreviations for task names are permitted.
  </p>
  <p>
  These commands are similar to the UNIX commands of the same name.  Users should
  note that <i>only</i> the currently loaded packages are searched.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Find out which package contains the HEAD task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; which head
  system
  </pre></div>
  <p>
  2.  Find all currently loaded package which contain the SPLOT task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; whereis splot
  echelle onedspec
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

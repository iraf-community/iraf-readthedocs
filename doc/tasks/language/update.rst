.. _update:

update: Update a task's parameters (flush to disk)
==================================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  update task [task ...]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_task">
  <dt><b>task</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='task' Line='task' -->
  <dd>An IRAF task name.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Normally when a task terminates the values of the task parameters used
  are stored for the next invocation of the task in a disk file in the
  users UPARM directory.  However if the task parameters have been
  cached by the <i>cache</i> command, this will not be done until the
  CL terminates.  In the case of a background job, automatic updating of
  parameters is disabled.  The <i>update</i> command is used to force the
  parameters for a task to be updated on disk.
  </p>
  </section>
  <section id="s_example">
  <h3>Example</h3>
  <p>
  1. Update the parameters for the <i>page</i> task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; update page
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The parameter set is only updated on disk if a parameter has been modified
  since the last update.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  cache, unlearn
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLE' 'BUGS' 'SEE ALSO'  -->
  

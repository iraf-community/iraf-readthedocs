.. _kill:

kill: Kill a background job
===========================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  kill job [job ...]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_job">
  <dt><b>job</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='job' Line='job' -->
  <dd>A background job number, as returned by <i>jobs</i>, or as printed when
  the job is submitted.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Kill</i> is used to forcibly terminate a background job.
  The user must specify the job number of the task to be killed.
  The job number is displayed when the job is started, and may also
  be seen using the <i>jobs</i> command.
  </p>
  </section>
  <section id="s_example">
  <h3>Example</h3>
  <p>
  1. Kill job number 4.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; kill 4
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  jobs, service
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLE' 'SEE ALSO'  -->
  

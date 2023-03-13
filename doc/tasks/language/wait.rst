.. _wait:

wait: Wait for all background jobs to complete
==============================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  wait [job job ...]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_job">
  <dt><b>job</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='job' Line='job' -->
  <dd>A background job number, as printed when the job is submitted,
  or as given by the <i>jobs</i> command.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>wait</i> task causes the CL to hibernate until a background job or
  jobs terminates.  No arguments, or a job number of 0 means to wait
  until all background jobs finish, while other arguments can be
  specified to wait for a particular job.  If a background job is
  not running the wait returns immediately.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Wait for any background jobs to finish, beeping the terminal when done.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wait;beep
  </pre></div>
  <p>
  2. Wait for job 3 to terminate.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wait 3
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Deadlock is possible.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  jobs, kill, service
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

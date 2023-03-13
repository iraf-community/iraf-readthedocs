.. _service:

service: Service a query from a background job
==============================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  service [job]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_job">
  <dt><b>job</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='job' Line='job' -->
  <dd>A background job number (defaults to 1).
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  When a background job requires input from the terminal (e.g. if it queries
  for a parameter), the job enters a stopped state, and a message is
  displayed on the terminal.  At the user's convenience, he should respond
  with a <i>service</i> command specifying the appropriate job number.  The
  <i>jobs</i> command can also be used to see what jobs require attention.
  </p>
  <p>
  After entering the <i>service</i> command, any prompt sent by the background
  job is displayed, and the user may return a single line
  of input to the background task.  Should more lines be needed several
  <i>service</i> calls may be necessary.  The user may service jobs in
  any order, regardless of how the requests from the background jobs were
  received.
  </p>
  </section>
  <section id="s_example">
  <h3>Example</h3>
  <p>
  1. Respond to a parameter request from job 3.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; service 3
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  If one never responds to a request for service from a background job, the job
  will eventually time out and abort.  In principle it is possible to service
  queued background jobs as well as interactive (subprocess) background jobs,
  but in practice the request for service never reaches the terminal (and thus
  the user), hence all parameters should be specified before submitting a job
  to execute in a queue.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  jobs, kill
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLE' 'BUGS' 'SEE ALSO'  -->
  

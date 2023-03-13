.. _jobs:

jobs: Display status of background jobs
=======================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  jobs
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <p>
  None.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Jobs</i> is used to display the status of background jobs.
  If no job number is specified then all the status of all background
  jobs is displayed.  For each job there is one line of output, e.g.
  </p>
  <p>
      [2]  0:14 +Running  copy file1 file2 &amp;
  </p>
  <p>
  Here 2 is the job number of the job; 0:14 is the clock time in minutes and
  seconds since the job was submitted; `Running' indicates that the task is
  currently running while the <span style="font-family: monospace;">`+'</span> indicates that this was the last background
  job started.   The remainder of the line is a copy of the actual command
  used to start the job.
  </p>
  <p>
  The possible states for a background job are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  Done    -- the job has finished normally
  Exit N  -- the job terminated with exit code N
  Stopped -- the job is waiting for input from the user
                  (see the <i>service</i> command)
  Running -- the job is currently executing
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; jobs
      [1]  21:13  Done      mkhelp &gt;&amp; dev$null &amp;
      [2]   0:05 +Running   count *.hlp &gt; _junk &amp;
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Exit codes are rarely displayed when jobs terminate abnormally.
  The CL checks for background job termination only when a command is
  entered, hence the elapsed time shown will often be greater than it
  should be.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  kill, service
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

.. _sleep:

sleep: Hibernate for a specified time
=====================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  sleep [nsec]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_nsec">
  <dt><b>nsec</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsec' Line='nsec' -->
  <dd>The number of seconds to sleep.  Defaults to 0.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>sleep</i> command causes the task to hibernate for the specified
  amount of time.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Sleep for 10 seconds, and then ring the bell.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sleep 10; beep
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  wait
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

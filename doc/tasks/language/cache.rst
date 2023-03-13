.. _cache:

cache: Cache parameter files, or print the current cache list
=============================================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  cache task [task ...]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_task">
  <dt><b>task</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='task' Line='task' -->
  <dd>The name of a task whose parameter set is to be cached in fast memory.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>cache</i> command loads the parameters of a task in memory.
  The CL normally reads the parameters for a task from disk whenever the
  task is executed.  Cacheing the parameters for frequently executed tasks
  can speed up execution significantly.  This is particularly important when
  the tasks are called from within a loop.
  </p>
  <p>
  If the <i>cache</i> command is entered without any arguments a list of the
  currently <span style="font-family: monospace;">"cached"</span> tasks is printed.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Cache the parameters for the tasks <i>directory</i> and <i>page</i>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cache dir page
  </pre></div>
  <p>
  2. Cache the parameters for the tasks called in a loop within the body of
  a procedure script.  Note the use of command mode in the script.
  </p>
  <div class="highlight-default-notranslate"><pre>
  begin
          cache ("alpha", "beta")
          for (i=1;  i &lt;= 10;  i+=1) {
              alpha (i)
              beta (i)
          }
  end
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The parameter cache should not be confused with the process cache associated
  with the <i>prcache</i> and <i>flprcache</i> commands.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  unlearn, update, lparam, eparam
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

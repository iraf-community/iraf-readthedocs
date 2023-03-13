.. _prcache:

prcache: Show process cache, or lock a process into the cache
=============================================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  prcache task [task ...]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_task">
  <dt><b>task</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='task' Line='task' -->
  <dd>The name of a compiled IRAF task (not the filename of an executable file).
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The CL maintains a small cache to store executable images.  When the
  user invokes a task which calls an executable the cache is searched
  for the image before any attempt to load the executable image from
  disk.  After completion of the task the CL retains the executable image
  in the process cache, until the space is needed by some other
  executable.  Thus if a few commands are being executed frequently,
  the overhead of loading the image into core from disk is bypassed,
  which can result in a significant improvement in the response of the CL.
  </p>
  <p>
  By default, when the cache is full and a new executable must be run,
  the CL searches for the slot containing the task which has remained
  dormant the longest and replaces it with the new task.
  </p>
  <p>
  The <i>prcache</i> command gives the user some control over this process.
  Using it without any arguments shows the tasks which are currently
  stored in the process cache.  For each slot one gets a line like the
  following.
  </p>
  <div class="highlight-default-notranslate"><pre>
  [07] lyra!17763(4563X)           H  bin$x_images.e
  </pre></div>
  <p>
  Here, 07 is the process slot number as required by <i>flprcache</i> to
  disconnect the process.  The name <span style="font-family: monospace;">"lyra"</span> is the name of the node in the
  local network on which the process is executing; this is not normally
  the local node.  In the example, 17763 (hex 4563X) is the process number
  (pid) of the executable.  H indicates that the task is hibernating,
  i.e. the task was waiting in the cache to be invoked.  R would show that
  the task was running.  An L appended to either of these would show that the task
  had been locked into the cache by a previous prcache command.
  The last element on the line is the file name of the executable
  file which was loaded when the task was first invoked.
  </p>
  <p>
  If one or more task names are given as arguments, those tasks are locked
  into the cache, and will not be replaced by the CL without specific user
  intervention.  If these tasks are not already in the cache, the
  corresponding executables are started, and the tasks are loaded into the cache.
  </p>
  <p>
  Note that the `process cache' described here, and the `parameter cache'
  described in the `cache' command are entirely distinct, and a given
  task may be found in either, both, or neither of the two caches.
  </p>
  <p>
  Also note that only executable images reside in the process cache.
  Thus, for example, if the <i>news</i> command is executed, it does not
  appear in the process cache, but the executable
  `system$x_system.e' does, because <i>news</i> calls <i>page</i>,
  which is one of the many entries into the system executable.
  </p>
  <p>
  Locked process cache slots may only be freed with the <i>flprcache</i> command.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Flush the system process and lock it back into the cache.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; flpr dir
  cl&gt; prc dir
  </pre></div>
  <p>
  2. Print the current contents of the process cache.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; prc
      [10] lyra!17764(4564X)           H  bin$x_plot.e
      [07] lyra!17763(4563X)           H  bin$x_images.e
      [04] lyra!17455(442FX)           HL bin$x_system.e
             0
  </pre></div>
  <p>
  3. Flush all processes which are not locked into the cache.  This may be
  necessary after aborting a task to initialize (by re-executing) the
  associated process, which may not have recovered completely from the
  abort.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; flpr
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The user is responsible for making sure that he does not lock all
  the slots in the cache.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  flprcache
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

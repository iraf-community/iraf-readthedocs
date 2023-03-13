.. _hidetask:

hidetask: Make a task invisible to the user
===========================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  hidetask task,[task,...]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_task">
  <dt><b>task</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='task' Line='task' -->
  <dd>The name of a task to be made hidden.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  If a task is only to be called from other tasks, and is not normally
  invoked directly by the user, then it may be useful to `hide' the task,
  i.e., omit it from the list of tasks listed in the <span style="font-family: monospace;">"?"</span> and <span style="font-family: monospace;">"??"</span> commands.
  The <i>hidetask</i> command performs this function.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Define the task <span style="font-family: monospace;">"_rew"</span> and hide it from the user.  The purpose of the
  leading underscore (not required) is to ensure that the user does not
  accidentally run the task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; task $_rew = "home$rew.e"
  cl&gt; hide _rew
  </pre></div>
  <p>
  2. Display the contents of the <i>language</i> package, including all
  hidden tasks (the _ does the trick).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ?_ lan
      language:
        ?             chdir         defpar        history       radix
        ??            cl            deftask       jobs          redefine
        _allocate     clbye         edit          keep          scan
        _curpack      clear         ehistory      kill          service
        _deallocate   clpackage     envget        language      set
        _devstatus    d_f           eparam        logout        show
        access        d_l           error         lparam        sleep
        back          d_off         flprcache     mktemp        task
        beep          d_on          fprint        osfn          time
        bye           d_p           fscan         package       unlearn
        cache         d_t           gflush        prcache       update
        cd            defpac        hidetask      print         wait
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

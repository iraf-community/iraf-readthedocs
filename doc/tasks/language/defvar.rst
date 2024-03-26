.. _defvar:

defvar: Test if an environment variable is defined
==================================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <div class="highlight-default-notranslate"><pre>
  defpac  (pacname)
  deftask (taskname)
  defpar  (param)
  defvar  (variable)
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_pacname">
  <dt><b>pacname</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pacname' Line='pacname' -->
  <dd>An IRAF package name.
  </dd>
  </dl>
  <dl id="l_taskname">
  <dt><b>taskname</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='taskname' Line='taskname' -->
  <dd>An IRAF taskname.  It may be specified as <span style="font-family: monospace;">"taskname"</span> or as
  <span style="font-family: monospace;">"packagename.taskname"</span>.
  </dd>
  </dl>
  <dl id="l_param">
  <dt><b>param</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='param' Line='param' -->
  <dd>An IRAF parameter name.  It may be specified as <span style="font-family: monospace;">"paramname"</span>,
  <span style="font-family: monospace;">"taskname.paramname"</span> or <span style="font-family: monospace;">"packagename.taskname.paramname"</span>.
  </dd>
  </dl>
  <dl id="l_variable">
  <dt><b>variable</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='variable' Line='variable' -->
  <dd>An environment variable name.  It may be specified as <span style="font-family: monospace;">"varname"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  These routines return a boolean value indicating whether the
  relevant parameter, task or package has been defined.
  A task becomes defined when the package to which it belongs is <span style="font-family: monospace;">"loaded"</span>
  by entering the name of the package as a command, or whenever a <i>task</i>
  declaration is input to the CL.  A parameter becomes defined when the
  task to which it belongs is defined; the task need not be currently
  executing for its parameters to be defined.  When a package is exited,
  e.g., after entry of the <i>bye</i> command, all the task and parameter
  declarations for the package are discarded.  Environment variables may
  be either in the host environment, or in the CL environment as a result
  of a <i>set</i> or <i>reset</i> statement.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Test if a task exists.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; if (deftask ("system.page"))
  &gt;&gt;&gt;     print ("task page exists")
  &gt;&gt;&gt; else
  &gt;&gt;&gt;     print ("task page not found")
  task page exists
  cl&gt;
  </pre></div>
  <p>
  2. Add the value of the named parameter into a sum, but only if the parameter
  exists (the example is for a script).
  </p>
  <div class="highlight-default-notranslate"><pre>
  sum = 0
  for (i=0;  i &lt;= 10;  i+=1) {
      parname = "data" // i
      if (defpar (parname)
          sum += parname
  }
  </pre></div>
  <p>
  3. Checked whether the 'IRAFARCH' environment variable is defined.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; if (defvar("IRAFARCH")) {
  &gt;&gt;&gt;    print ("IRAFARCH is " // envget("IRAFARCH")
  &gt;&gt;&gt; }
  &gt;&gt;&gt; ;
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  package, task, redefine, lparam
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

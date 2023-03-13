.. _dparam:

dparam: Dump a pset as a series of task.param=value assignments
===============================================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  dparam pset [pset ...]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_pset">
  <dt><b>pset</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pset' Line='pset' -->
  <dd>The name of the parameter set to be listed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Dparam</i> lists one or more parameter sets.  Psets are specified either by
  the name of the task with which the pset is associated, or by filename (pset
  files have the <span style="font-family: monospace;">".par"</span> extension).  If a file type pset is listed the extension
  must be included, since it is the presence or absence of the filename
  extension which <b>dparam</b> uses to distinguish between task-psets and named
  (file) psets.
  </p>
  <p>
  Each parameter is listed on a single line with the following format.
  The list of assignments is terminated by the string <span style="font-family: monospace;">"# EOF"</span> so that programs
  reading the list from a stream can easily distinguish the end of the variable
  length list of parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  task.param = value
  </pre></div>
  <p>
  Here <span style="font-family: monospace;">"task.param"</span> is the name of the parameter, and <span style="font-family: monospace;">"value"</span> is the current
  value of the parameter.  The assignment is skipped if the value is undefined.
  There is no way to distinguish between hidden parameters and query parameters.
  </p>
  <p>
  The output from <b>dparam</b> is often used as input to programs, whereas
  the output from <b>lparam</b> is formatted in a way which makes it easier for
  humans to read.  For example, the output from <b>dparam</b> may be redirected
  into a file and used on the IRAF main command line to set the task's
  parameters, when debugging a task standalone.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the parameter for the task <i>delete</i>.  Note that the positional
  parameters are listed first, in the order in which they must be specified
  on the command line, followed by the hidden parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dparam delete
  delete.files = "temp"
  delete.go_ahead = yes
  delete.verify = no
  delete.default_action = yes
  delete.allversions = yes
  delete.subfiles = yes
  delete.mode = "ql"
  # EOF
  </pre></div>
  <p>
  2. List the contents of the file pset <span style="font-family: monospace;">"delete.par"</span>.  Named psets such as this
  are most commonly produced using the <b>":w filename"</b> colon command in
  <b>eparam</b>, e.g., to prepare several different versions of the parameter
  set for a task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dparam delete.par
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  You cannot list the parameters of a task that does not have a parameter
  file (e.g., all builtin tasks).
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  eparam, lparam, cache
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

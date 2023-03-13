.. _lparam:

lparam: List the parameters of a task
=====================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  lparam pset [pset ...]
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
  <i>Lparam</i> lists one or more parameter sets.  Psets are specified either by
  the name of the task with which the pset is associated, or by filename (pset
  files have the <span style="font-family: monospace;">".par"</span> extension).  If a file type pset is listed the extension
  must be included, since it is the presence or absence of the filename
  extension which <b>lparam</b> uses to distinguish between task-psets and named
  (file) psets.
  </p>
  <p>
  Each parameter is listed on a single line with the following format:
  </p>
  <div class="highlight-default-notranslate"><pre>
  param = value           prompt string
  </pre></div>
  <p>
  Here <span style="font-family: monospace;">"param"</span> is the name of the parameter, <span style="font-family: monospace;">"value"</span> is the current value of
  the parameter (blank if undefined), and <span style="font-family: monospace;">"prompt string"</span> is the prompt for
  the parameter, if any.  If the parameter is hidden, then the line is enclosed
  in parentheses.  For arrays, instead of the values, a list of the
  dimensionalities is given.  The <i>eparam</i> task may be used to examine
  or edit the contents of an array.  When more than one task is listed the
  task name is prefixed to the list of each tasks parameters.
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
  cl&gt; lparam delete
          files = "temp"          list of files to be deleted
       go_ahead = yes              ?
        (verify = no)             verify operation before deleting each file?
  (default_acti = yes)            default delete action for verify query
   (allversions = yes)            delete all versions of each file
      (subfiles = yes)            delete any subfiles of each file
          (mode = "ql")
  </pre></div>
  <p>
  2. List the contents of the file pset <span style="font-family: monospace;">"delete.par"</span>.  Named psets such as this
  are most commonly produced using the <b>":w filename"</b> colon command in
  <b>eparam</b>, e.g., to prepare several different versions of the parameter
  set for a task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lparam delete.par
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
  eparam, dparam, cache
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

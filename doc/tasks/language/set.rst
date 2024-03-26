.. _set:

set: Set an environment variable
================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <div class="highlight-default-notranslate"><pre>
  set [varname = valuestring]
  reset [varname = valuestring]
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_varname">
  <dt><b>varname</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='varname' Line='varname' -->
  <dd>The environment variable to be defined or set.
  </dd>
  </dl>
  <dl id="l_valuestring">
  <dt><b>valuestring</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='valuestring' Line='valuestring' -->
  <dd>The new string value of the environment variable.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The CL maintains a list of environment variables, each of which consists
  of a keyword = value pair.  The <i>set</i> and <i>reset</i> operators are used
  to define new environment variables, or to set new values for old environment
  variables.  The two operators are equivalent with the exception that if the
  named environment variable is already defined, <i>set</i> will push a new,
  temporary value for the variable, whereas <i>reset</i> will overwrite the most
  recent definition of the variable.  Environment variables may be examined
  using the <i>show</i> task or the <i>envget</i> intrinsic function.
  </p>
  <p>
  A particular use for the environment variables is in the definition
  of IRAF logical names for directories.  If an environment variable is set to
  a string corresponding to a system-dependent directory name,
  then the environment variable may then be used within the CL to
  refer to that directory.
  </p>
  <p>
  For example,
  </p>
  <div class="highlight-default-notranslate"><pre>
  set     testdir = "/usr/iraf/testdir"           # Unix
  set     testdir = "dua2:[iraf.testdir]"         # VMS
  task    tst1 = testdir$tst1.cl
  </pre></div>
  <p>
  New IRAF logicals may be defined in terms or existing IRAF logical names,
  i.e., logical names are recursively expanded.
  </p>
  <div class="highlight-default-notranslate"><pre>
  set     subdir1 = testdir$subdir1/
  task    tst2 = subdir1$tst2.e
  </pre></div>
  <p>
  If the <i>set</i> command is entered without any arguments the current
  environment list is printed in the reverse of the order in which the
  definitions were made.  If a variable has been redefined both the
  final and original definition are shown.   The <i>show</i> command can be
  used to show only the current value.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Define the data directory <span style="font-family: monospace;">"dd"</span> on a remote node, and call <i>implot</i>
  to make plots of an image which resides in the remote directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set dd = lyra!/u2/me/data
  cl&gt; implot dd$picture
  </pre></div>
  <p>
  2. Temporarily change the value of the variable <i>printer</i>.  The new
  value is discarded when the <i>bye</i> is entered.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cl
  cl&gt; set printer = qms
          ...
  cl&gt; bye
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  show, envget
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

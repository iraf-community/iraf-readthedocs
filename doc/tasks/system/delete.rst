.. _delete:

delete: Delete a file or files (use IMDELETE to delete imagefiles)
==================================================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  delete files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>The list of files to be deleted.
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = no' -->
  <dd>Check with the user before deleting a file.  If verify is enabled the file
  name is printed and the user is queried before the default action is taken.
  </dd>
  </dl>
  <dl id="l_default_action">
  <dt><b>default_action = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='default_action' Line='default_action = yes' -->
  <dd>This is the default action to take when operating in <span style="font-family: monospace;">"verify"</span> mode.
  For example, if the default action is <span style="font-family: monospace;">"yes"</span>, one need only type RETURN in
  response to the verify prompt to delete the file.
  </dd>
  </dl>
  <dl id="l_allversions">
  <dt><b>allversions = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='allversions' Line='allversions = yes' -->
  <dd>Delete all versions of a file.  This parameter has no effect on systems like
  UNIX which do not support multiple file versions.
  </dd>
  </dl>
  <dl id="l_subfiles">
  <dt><b>subfiles = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subfiles' Line='subfiles = yes' -->
  <dd>Delete subfiles.  Not currently used.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Delete</i> destroys a file or files and returns the space they occupied to
  the host system, to be reused for other files.  Once a file has been deleted,
  it is gone forever (unless a copy exists somewhere).  Enabling <i>verify</i>
  gives one the opportunity to say yes or no before each file is deleted; this
  is particularly useful when <i>files</i> is a template.  Note that
  <i>protect</i> can be used to protect files from deletion, accidental or
  otherwise.  Imagefiles are automatically protected by the system to remind
  the user to use <i>imdelete</i> to delete images (this is necessary because
  an image is stored in more than one physical file).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Delete all files with extension <span style="font-family: monospace;">".x"</span>, verifying each file deletion before
  it is performed.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; delete *.x ver+
  </pre></div>
  <p>
  2. List all files in the current directory, deleting only those files for
  which the user responds to the verify prompt with <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"y"</span>.  Note that
  <span style="font-family: monospace;">"delete *"</span> is a very dangerous operation.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; delete * ver+ def=no
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  protect, unprotect, imdelete
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

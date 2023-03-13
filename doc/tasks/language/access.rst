.. _access:

access: Test if a file exists
=============================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  bool = access (filename)
  bool = imaccess (imagename)
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_filename">
  <dt><b>filename</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filename' Line='filename' -->
  <dd>The name of the file whose existence is to be tested.
  </dd>
  </dl>
  <dl id="l_imagename">
  <dt><b>imagename</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imagename' Line='imagename' -->
  <dd>The name of the image whose existence is to be tested.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Access</i> is a boolean intrinsic function returning true (<span style="font-family: monospace;">"yes"</span>) if the
  named file exists.  <i>Access</i> can only be called as a function in an
  expression, not as a task.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Type a file if it exists.
  </p>
  <div class="highlight-default-notranslate"><pre>
  if (access ("lib$motd"))
      type ("lib$motd")
  else
      error (11, "File not found")
  </pre></div>
  <p>
  2. Tell if a file and an image exists.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; = access ("lib$motd")
  cl&gt; = imaccess ("dev$pix")
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  An optional second argument should be added to test whether the named file
  can be accessed for reading or writing.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS'  -->
  

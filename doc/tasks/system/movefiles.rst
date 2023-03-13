.. _movefiles:

movefiles: Move files to a directory
====================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  movefiles files directory
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>A template specifying the file or files to be moved.
  </dd>
  </dl>
  <dl id="l_directory">
  <dt><b>directory</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='directory' Line='directory' -->
  <dd>The directory to which the files are to be moved.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>If set to <span style="font-family: monospace;">"yes"</span>, tell user as each file is moved.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This routine moves the specified files to the named directory.
  If a subdirectory and a logical directory both exist with the same
  name as the destination directory, the subdirectory is used.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Move all files whose names start with `im' and end with `ab' to
  the directory `dir'.  Since <span style="font-family: monospace;">"verbose"</span> defaults to <span style="font-family: monospace;">"no"</span>, do the work silently.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; movefiles im*ab dir
  </pre></div>
  <p>
  2. Move all files in the current directory into the directory one level up.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; move * ..
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  copy, rename
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

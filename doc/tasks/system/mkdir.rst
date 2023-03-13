.. _mkdir:

mkdir: Create a new directory
=============================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkdir newdir
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_newdir">
  <dt><b>newdir</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newdir' Line='newdir' -->
  <dd>New directory or subdirectory to be made.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Mkdir</i> creates a new directory with the given name.
  <i>Newdir</i> may be an IRAF virtual directory name (not a logical name)
  or a host directory name.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Make a subdirectory named <span style="font-family: monospace;">"sub1"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkdir sub1
  </pre></div>
  <p>
  2. Make a subdirectory <span style="font-family: monospace;">"sub2"</span> below <span style="font-family: monospace;">"sub1"</span>.  The subdirectory <span style="font-family: monospace;">"sub1"</span> must
  already exist.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkdir sub1/sub2
  </pre></div>
  <p>
  3. Make a directory <span style="font-family: monospace;">"blue"</span> at the same level in the directory hierarchy as
  the current directory (<span style="font-family: monospace;">".."</span> is a synonym for the previous directory).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkdir ../blue
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES'  -->
  

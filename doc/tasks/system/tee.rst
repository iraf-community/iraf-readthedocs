.. _tee:

tee: Tee the standard output into a file
========================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tee file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_file">
  <dt><b>file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file' Line='file' -->
  <dd>The name of the output file.
  </dd>
  </dl>
  <dl id="l_out_type">
  <dt><b>out_type = <span style="font-family: monospace;">"text"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='out_type' Line='out_type = "text"' -->
  <dd>The type of output file to be created, either <span style="font-family: monospace;">"text"</span> or <span style="font-family: monospace;">"binary"</span>.
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = no' -->
  <dd>If set, append to an existing file, otherwise create a new file.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Tee</i> copies its input to both the standard output and the named file.
  Its primary use is in pipes where one wants to capture some intermediate output.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. The results of the <i>set</i> command are captured in the file <span style="font-family: monospace;">"temp"</span>,
  and are also passed on to the <span style="font-family: monospace;">"match"</span> command.  The result is
  a <span style="font-family: monospace;">"temp"</span> file of perhaps 100 lines, with the output to the screen
  only around 5 lines.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set | tee temp | match tty
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Since the processes in an IRAF pipe execute serially rather than concurrently,
  the teed output will not appear until all tasks to the left have completed.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS'  -->
  

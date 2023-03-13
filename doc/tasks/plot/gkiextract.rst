.. _gkiextract:

gkiextract: Extract individual frames from metacode file
========================================================

**Package: plot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  gkiextract input frames
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The metacode source file or files.
  </dd>
  </dl>
  <dl id="l_frames">
  <dt><b>frames</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='frames' Line='frames' -->
  <dd>List of frames to be extracted from each metacode file.
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = no' -->
  <dd>Verify each frame before extraction?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <b>gkiextract</b> will extract individual frames from a metacode file, 
  writing a binary metacode output stream which can be piped to a kernel
  for plotting or redirected to produce a new metacode file.  
  Parameter <i>frames</i> specifies a list of frames to be
  extracted from each input file.  If <i>verify</i>  = yes,
  a <b>gkidir</b> style line will be printed for each specified frame 
  and the user will be queried whether or not to extract the frame.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Extract frames 1, 3 and 5 from metacode file <span style="font-family: monospace;">"mc_file"</span> and
  plot them on the device <span style="font-family: monospace;">"vup"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gkiextract mc_file 1,3,5 | stdplot dev=vup
  </pre></div>
  <p>
  2. Print a directory of the first 99 frames in <span style="font-family: monospace;">"mc_file"</span>, extract
  those files requested by the user and write them to file <span style="font-family: monospace;">"new_mc_file"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gkiextract mc_file 1-99 ver+ &gt; new_mc_file
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  A maximum of 8192 plots in a single metacode file may be processed.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  gkidir
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

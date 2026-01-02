.. _destreak5:

destreak5: First pass processing CL script for 10830 grams.
===========================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  destreak5 input_root output_root
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input_root">
  <dt><b>input_root</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input_root' Line='input_root' -->
  <dd>Root name for input files.
  </dd>
  </dl>
  <dl id="l_output_root">
  <dt><b>output_root</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output_root' Line='output_root' -->
  <dd>Root name of output files.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Destreak5 takes as input the 5 files from a vacuum telescope 10830
  tape and produces 5 nearly identical files but with the streaks
  removed from the solar images and with the best fit ellipse parameters
  added to the image header.  The input files are expected to be in the
  directory 'imdir' and to have the extensions '001' thru '005'.  These
  input files are expected to be mag tape images produced by T2D.  The output
  files are stored in the current directory with the same extensions.
  Destreak5 calls 'readvt<span style="font-family: monospace;">','</span>quickfit', 'destreak', and various other utilities
  and is a cl script file.
  If an input image is not found, the processing for that image is skipped and
  a message is printed telling about the missing image.
  The next step in the 10830 reduction process is 'makehelium' which produces
  the projected daily grams.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To destreak five files with root name m1585 and store the resulting images
  with root name M1585 the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; destreak5 m1585 M1585
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  readvt, destreak, quickfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

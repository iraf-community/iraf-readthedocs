.. _makehelium:

makehelium: Cl script for processing destreaked 10830 grams(second pass).
=========================================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  makehelium input_root output_root
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
  Makehelium takes the files output by 'destreak5' and projects them the
  small [180x180] maps.  The input files are expected to be in the current
  directory and have the extensions <span style="font-family: monospace;">'1'</span> thru <span style="font-family: monospace;">'5'</span>.  The output files are
  stored in the current directory with the extensions 'a1', 'a2', 'a3', 'b1', etc.
  This coding scheme is the same as that used in makeimages.  Note that the
  absolute value images for 10830 grams should be thrown out since they are
  garbage.
  Makehelium calls 'rmap' and 'imdelete' and is a cl script file.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To run makehelium on five files with root name m1585 and store the resulting
  images with root name M1585 the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; makehelium m1585 M1585
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rmap
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

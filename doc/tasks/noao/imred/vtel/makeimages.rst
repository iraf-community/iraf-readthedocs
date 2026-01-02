.. _makeimages:

makeimages: Cl script for processing magnetograms into projected maps
=====================================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  makeimages input_root output_root
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
  Makeimages processes 5 magnetograms from raw data tape images into projected
  small [180x180] maps.  The input images are expected be output from T2D,
  be in the current imdir, and have the extensions '001' through '005'.
  The output files are stored in the current directory with the extensions
  'a1', 'a2', 'a3', 'b1', etc.  The output image coding scheme is the following:
  </p>
  <div class="highlight-default-notranslate"><pre>
  On the filename extensions the first character is a letter
  corresponding to the tape file position.
          a = first file on tape
          b = second
              .
              .
          e = fifth
  
  The second character specifies which type of image this is.
          1 = data
          2 = absolute value
          3 = weights
  </pre></div>
  <p>
  Note: A logical directory called <span style="font-family: monospace;">"scratch"</span> must be set up before this
  program is run.  This logical directory must point to the directory
  containing the input images.  This can be set up as in the following
  example:
  </p>
  <p>
  vt&gt; set scratch = <span style="font-family: monospace;">"scr1:[recely]"</span>
  </p>
  <p>
  where this particular directory is a VAX/VMS type name.  If the image
  files are in the user's home directory then <span style="font-family: monospace;">"scratch"</span> can be set to
  <span style="font-family: monospace;">"home"</span>.
  </p>
  <p>
  Makeimages calls 'readvt', 'quickfit', 'rmap',
  'delete', and 'imdelete' and is a cl script.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To process five magnetograms with root name m1585 and produce output images
  with the root name M1585, the command would be.
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; makeimages m1585 M1585
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  readvt, quickfit, rmap, delete, imdelete
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

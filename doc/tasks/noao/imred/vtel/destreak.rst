.. _destreak:

destreak: Destreak He 10830 grams.
==================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  destreak input_image output_image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input_image">
  <dt><b>input_image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input_image' Line='input_image' -->
  <dd>Image to be destreaked.
  </dd>
  </dl>
  <dl id="l_output_image">
  <dt><b>output_image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output_image' Line='output_image' -->
  <dd>Name to give destreaked output image (must be a separate image).
  </dd>
  </dl>
  <dl id="l_tempim">
  <dt><b>tempim</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tempim' Line='tempim' -->
  <dd>Temporary image used for pixel storage between destreak passes.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose=no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose=no' -->
  <dd>Flag to signal program that it should produce verbose output.
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = 4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 4' -->
  <dd>Squibby brightness threshold to use in determining limb points.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The helium 10830 grams as taken by the vacuum telescope have horizontal
  streaks caused by the detecting apparatus.  Destreak removes these streaks
  and the limb darkening
  using a two pass procedure.  First, for each diode, a function of the form
  'a + b*r**4', where r is the radius from disk center and a, b are parameters,
  is fit to the intensity distribution and is then subtracted from the data.
  Then a spatial filter is applied to the result and the final image is
  written to disk.  The full disk images are 2048 x 2048 and are taken using
  a 512 diode array which is scanned from west to east across the solar disk
  4 times.  Thus, data from a particular diode consists of four lines of the 
  image.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To destreak <span style="font-family: monospace;">"image1"</span>, put the output in <span style="font-family: monospace;">"image2"</span>, put the temporary image in
  <span style="font-family: monospace;">"temp2"</span>, and see verbose output, the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; destreak image1 image2 temp2 v+
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  readvt, writevt, quickfit, getsqib, putsqib
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

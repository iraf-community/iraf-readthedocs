.. _vtblink:

vtblink: Blink daily grams on the IIS to check for registration.
================================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  vtblink 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_imname1">
  <dt><b>imname1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imname1' Line='imname1' -->
  <dd>First image to be mapped.
  </dd>
  </dl>
  <dl id="l_imname2">
  <dt><b>imname2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imname2' Line='imname2' -->
  <dd>Subsequent images to be mapped
  </dd>
  </dl>
  <dl id="l_z1">
  <dt><b>z1 = -3000.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='z1' Line='z1 = -3000.0' -->
  <dd>Minimum grayscale intensity to be mapped during 'display'.
  </dd>
  </dl>
  <dl id="l_z2">
  <dt><b>z2 = 3000.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='z2' Line='z2 = 3000.0' -->
  <dd>Maximum grayscale intensity to be mapped during 'display'.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Vtblink allows the user to blink successive frames of data on the IIS.  The
  program calculates the offset between grams based on the
  longitudes for each image.  Vtblink will ask for each successive image 
  and will display it on the next (mod 4) IIS frame.
  After each image is displayed the user is put back out in the cl so that he/she
  can use any of the images$tv tasks to analyze the data.  The user returns to
  the blink program by typing 'bye' to the cl prompt.  To exit the program the
  user enters the <span style="font-family: monospace;">"end"</span> for the filename.  Images are displayed with the grayscale
  limits set by default to -3000.0 and 3000.0.  These values correspond to the
  parameters z1 and z2 which may be given on the command line.  If the user
  forgets which IIS frame contains which image, he/she can enter <span style="font-family: monospace;">"stat"</span> to the
  <span style="font-family: monospace;">"next image"</span> prompt and will get a list of which images are in which frames.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To run vtblink with the default gray scale parameters just type:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; vtblink
  </pre></div>
  <p>
  2. To run vtblink with gray scale parameters z1=-4000.0, z2=4000.0, the
  command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; vtblink z1=-4000.0 z2=4000.0
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  display, blink, lumatch
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

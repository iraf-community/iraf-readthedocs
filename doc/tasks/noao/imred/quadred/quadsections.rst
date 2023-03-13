.. _quadsections:

quadsections: Produce image section list for sections of quadformat images
==========================================================================

**Package: quadred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  quadsplit images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of image names for images in <b>quadformat</b>.
  </dd>
  </dl>
  <dl id="l_window">
  <dt><b>window = <span style="font-family: monospace;">"datasec"</span> (datasec|trimsec|biassec)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='window' Line='window = "datasec" (datasec|trimsec|biassec)' -->
  <dd>Type of section to output.  The choices are <span style="font-family: monospace;">"datasec"</span> for the amplifier
  section which includes the bias if any is present, <span style="font-family: monospace;">"trimsec"</span> for the trim
  section, and <span style="font-family: monospace;">"biassec"</span> for the bias section.
  </dd>
  </dl>
  <dl id="l_section">
  <dt><b>section = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='section' Line='section = ""' -->
  <dd>Section to be overlapped.  The output sections will be the parts of the
  amplifier windows which are included within this section.
  </dd>
  </dl>
  <dl id="l_template">
  <dt><b>template = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='template' Line='template = ""' -->
  <dd>Template for producing the output.  The template replaces occurs of
  $I with the image name, $S with the section, and $A with the amplifier
  label.  If none is specified then the default template <span style="font-family: monospace;">"$I$S\\n"</span> is
  used which produces the image name with section separated by new-lines.
  The special characters <span style="font-family: monospace;">"\n"</span> is the new-line and the extra <span style="font-family: monospace;">"\"</span> is
  required to pass the new-line through to the formatting routine.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Images in <span style="font-family: monospace;">"quadformat"</span> (see help topic <b>quadformat</b>) are broken down
  in sections and written to the standard output in a specified format.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To print the default data sections.
  </p>
  <div class="highlight-default-notranslate"><pre>
  qu&gt; quadsec quad0072
  quad0072[1:1034,1:1024]
  quad0072[1163:2196,1:1024]
  quad0072[1:1034,1025:2048]
  quad0072[1163:2196,1025:2048]
  </pre></div>
  <p>
  3. To apply an overlap section.
  </p>
  <div class="highlight-default-notranslate"><pre>
  qu&gt; quadsec quad0072 section=[1000:2000,1000:2000]
  quad0072[1000:1034,1000:1024]
  quad0072[1163:2000,1000:1024]
  quad0072[1000:1034,1025:2000]
  quad0072[1163:2000,1025:2000]
  </pre></div>
  <p>
  2. To print the trim sections.
  </p>
  <div class="highlight-default-notranslate"><pre>
  qu&gt; quadsec quad0072 window=trimsec
  quad0072[11:1034,1:1024]
  quad0072[1163:2186,1:1024]
  quad0072[11:1034,1025:2048]
  quad0072[1163:2186,1025:2048]
  </pre></div>
  <p>
  4.  To make a custom output.
  </p>
  <div class="highlight-default-notranslate"><pre>
  qu&gt; quadsec quad0072 template="image=$I, section=$S, amplifier=$A\\n"
  image=quad0072, section=[1:1034,1:1024], amplifier=11
  image=quad0072, section=[1163:2196,1:1024], amplifier=12
  image=quad0072, section=[1:1034,1025:2048], amplifier=21
  image=quad0072, section=[1163:2196,1025:2048], amplifier=22
  qu&gt; quadsec quad0072 template="$I.$A,"
  quad0072.11,quad0072.12,quad0072.21,quad0072.22,
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  quadformat
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

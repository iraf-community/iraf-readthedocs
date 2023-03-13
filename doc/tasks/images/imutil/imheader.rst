.. _imheader:

imheader: Print an image header
===============================

**Package: imutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imheader [images]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of IRAF images.
  </dd>
  </dl>
  <dl id="l_imlist">
  <dt><b>imlist = <span style="font-family: monospace;">"*.imh,*.fits,*.pl,*.qp,*.hhh"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imlist' Line='imlist = "*.imh,*.fits,*.pl,*.qp,*.hhh"' -->
  <dd>The default IRAF image name template.
  </dd>
  </dl>
  <dl id="l_longheader">
  <dt><b>longheader = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='longheader' Line='longheader = no' -->
  <dd>Print verbose image header.
  </dd>
  </dl>
  <dl id="l_userfields">
  <dt><b>userfields = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='userfields' Line='userfields = yes' -->
  <dd>If longheader is set print the information in the user area.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IMHEADER prints header information in various formats for the list of IRAF
  images specified by <i>images</i>, or by the default image name template
  <i>imlist</i>. If <i>longheader</i> = no, the image name,
  dimensions, pixel type and title are printed. If <i>longheader</i> = yes,
  information on the create and modify dates, image statistics and so forth
  are printed. Non-standard IRAF header information can be printed by
  setting <i>userfields</i> = yes.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print the header contents of a list of IRAF fits images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imheader *.fits
  </pre></div>
  <p>
  2. Print the header contents of a list of old IRAF format images in verbose
  mode.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imheader *.imh lo+
  </pre></div>
  <p>
  3. Print short headers for all IRAF images of all types, e.g. imh, fits etc
  in the current directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imheader
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imgets, hedit, hselect
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

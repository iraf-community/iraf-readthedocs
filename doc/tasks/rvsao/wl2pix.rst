.. _wl2pix:

wl2pix: Compute the pixel for a specific wavelength in a spectrum
=================================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  wl2pix spectrum wavelength
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_spectrum">
  <dt><b>spectrum</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectrum' Line='spectrum' -->
  <dd>Spectrum image file with dispersion function
  </dd>
  </dl>
  <dl id="l_specext">
  <dt><b>specext = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specext' Line='specext = 0' -->
  <dd>Spectrum extension number in multiextension FITS image
  </dd>
  </dl>
  <dl id="l_specnum">
  <dt><b>specnum 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specnum' Line='specnum 0' -->
  <dd>Spectrum number in multispec image (order in echelle image)
  </dd>
  </dl>
  <dl id="l_specband">
  <dt><b>specband 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specband' Line='specband 0' -->
  <dd>Spectrum band in multispec image
  </dd>
  </dl>
  <dl id="l_wavelength">
  <dt><b>wavelength INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wavelength' Line='wavelength INDEF' -->
  <dd>Wavelength in Angstroms for pixel
  </dd>
  </dl>
  <dl id="l_pixel">
  <dt><b>pixel INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixel' Line='pixel INDEF' -->
  <dd>Pixel at specified wavelength (returned)
  </dd>
  </dl>
  <dl id="l_pixform">
  <dt><b>pixform <span style="font-family: monospace;">"%8.3f"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixform' Line='pixform "%8.3f"' -->
  <dd>IRAF format for pixel output
  </dd>
  </dl>
  <dl id="l_waveform">
  <dt><b>waveform <span style="font-family: monospace;">"%8.3f"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='waveform' Line='waveform "%8.3f"' -->
  <dd>IRAF format for wavelength output
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = 1' -->
  <dd>Number of pixels to sum across dispersion
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose no' -->
  <dd>If yes, print the pixel value
  </dd>
  </dl>
  <dl id="l_debug">
  <dt><b>debug = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='debug' Line='debug = no' -->
  <dd>If yes, print the file name, transformation, and wavelength per pixel
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Compute the pixel value for a given wavelength in a spectrum, saving the
  value as the pix2wl.pixel parameter.  If verbose=yes, print the pixel
  value using the pix2wl.pixform format.  If debug=yes, print spectrum image
  name, followed by the wavelength value using the pix2wl.waveform format,
  the pixel falue using the pix2wl.pixform format, and the delta wavelength
  per pixel across this pixel.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1) Compute the pixel at a given wavelength for use in a CL script:
  </p>
  <div class="highlight-default-notranslate"><pre>
  rvsao&gt; wl2pix 22572.fits 7000
  rvsao&gt; =wl2pix.pixel
  3982.3984617936
  rvsao&gt;
  </pre></div>
  <p>
  2) Print the pixel at a given wavelength:
  </p>
  <div class="highlight-default-notranslate"><pre>
  rvsao&gt; wl2pix 22572.fits 7000 v+
  3982
  rvsao&gt;
  </pre></div>
  <p>
  3) Print the pixel at a given wavelength more verbosely:
  </p>
  <div class="highlight-default-notranslate"><pre>
  rvsao&gt; wl2pix 22572.fits 7000 d+
  22572.fits:  7000.000 -&gt; 3982 (0.5744/pix)
  rvsao&gt;
  </pre></div>
  <p>
  4) Check the inverse of the dispersion function:
  </p>
  <div class="highlight-default-notranslate"><pre>
  rvsao&gt; wl2pix 22572.fits 7000
  rvsao&gt; pix2wl  22572.fits wl2pix.pixel v+
  7000.000
  rvsao&gt;
  </pre></div>
  </section>
  <section id="s_author">
  <h3>Author</h3>
  <p>
  Doug Mink, Harvard-Smithsonian Center for Astrophysics
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'AUTHOR'  -->
  

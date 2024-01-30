.. _pix2wl:

pix2wl: Compute the wavelength for a specific pixel in a spectrum
=================================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  pix2wl spectrum pixel
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
  <dl id="l_pixel">
  <dt><b>pixel INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixel' Line='pixel INDEF' -->
  <dd>Pixel at specified wavelength (returned)
  </dd>
  </dl>
  <dl id="l_wavelength">
  <dt><b>wavelength INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wavelength' Line='wavelength INDEF' -->
  <dd>Wavelength in Angstroms for pixel
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
  Compute the wavelength at a given pixel in a spectrum, saving the
  value as the pix2wl.wavelength parameter.  If the pixel is zero, the
  wavelength at the start of first pixel (=0.5) is saved as pix2wl.wavelength,
  and the wavelength at the end of the last pixel (=npts+0.5) is saved as
  pix2wl.wave2.  Otherwise, pix2wl.wave2=INDEF.  If verbose=yes, print the
  wavelength of the pixel (or if the pixel is zero, the wavelengths of the
  first and last pixels) using the pix2wl.waveform format.  If debug=yes,
  print spectrum image name, followed by the wavelength value using the
  pix2wl.waveform format, the pixel falue using the pix2wl.pixform format,
  and the delta wavelength per pixel across this pixel.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1) Compute the wavelength at a given pixel for use in a CL script:
  </p>
  <div class="highlight-default-notranslate"><pre>
  rvsao&gt; pix2wl 22572.fits 3000
  rvsao&gt; =pix2wl.wavelength
  6435.7338761065
  rvsao&gt;
  </pre></div>
  <p>
  2) Print the wavelength at a given pixel:
  </p>
  <div class="highlight-default-notranslate"><pre>
  rvsao&gt; pix2wl 22572.fits 3000 v+
  6435.734
  rvsao&gt;
  </pre></div>
  <p>
  3) Print the wavelength at a given pixel more verbosely:
  </p>
  <div class="highlight-default-notranslate"><pre>
  rvsao&gt; pix2wl 22572.fits 3000 d+
  22572.fits: 3000 -&gt; 6435.734 (0.5744/pix)
  rvsao&gt;
  </pre></div>
  <p>
  4) Compute the wavelength range of an image for use in a CL script:
  </p>
  <div class="highlight-default-notranslate"><pre>
  rvsao&gt; pix2wl 22572.fits 0
  rvsao&gt; =pix2wl.wavelength
  4712.8929877685
  rvsao&gt; =pix2wl.wave2
  7065.5371880127
  rvsao&gt;
  </pre></div>
  <p>
  5) Print the wavelength range of an image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  rvsao&gt; pix2wl 22572.fits 0 v+
  4712.893 - 7065.537
  rvsao&gt;
  </pre></div>
  <p>
  6) Print the wavelength range of an image more verbosely:
  </p>
  <div class="highlight-default-notranslate"><pre>
  rvsao&gt; pix2wl 22572.fits 0 d+
  22572.fits: 4712.893-7065.537 (4096 pixels, 0.5742/pix)
  rvsao&gt;
  </pre></div>
  <p>
  7) Check the inverse of the dispersion function:
  </p>
  <div class="highlight-default-notranslate"><pre>
  rvsao&gt; pix2wl 22572.fits 3000
  rvsao&gt; wl2pix 22572.fits pix2wl.wavelength v+
  3000.000
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
  

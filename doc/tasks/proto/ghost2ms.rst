.. _ghost2ms:

ghost2ms: Convert Gemini/DRAGONS GHOST format to IRAF multispec format
======================================================================

**Package: proto**

.. raw:: html

  <section id="s_name_ghost2ms____convert_gemini_dragons_ghost_format_to_iraf_multispec_format">
  <h3>Name ghost2ms -- convert gemini/dragons ghost format to iraf multispec format</h3>
  </section>
  <section id="s_usage_ghost2ms_input_output">
  <h3>Usage ghost2ms input output</h3>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input GHOST file from DRAGONS.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>Output base name.
  </dd>
  </dl>
  <dl id="l_order1">
  <dt><b>order1 = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order1' Line='order1 = 1' -->
  <dd>Starting order to extract.
  </dd>
  </dl>
  <dl id="l_order2">
  <dt><b>order2 = 33</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order2' Line='order2 = 33' -->
  <dd>Ending order to extract.
  </dd>
  </dl>
  <dl id="l_version">
  <dt><b>version = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='version' Line='version = 1' -->
  <dd>Version to extract.
  </dd>
  </dl>
  <dl id="l_clobber">
  <dt><b>clobber = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clobber' Line='clobber = no' -->
  <dd>Clobber existing output?
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Verbose output?
  </dd>
  </dl>
  </section>
  <section id="s_description_the_ghost2ms_task_converts_the_dragons_calibrated_output_for_the">
  <h3>Description the ghost2ms task converts the dragons-calibrated output for the</h3>
  <p>
  red and blue arms on the GHOST instrument to a standard IRAF multispec format
  to permit further analysis and visualization using standard ONEDSPEC tasks.
  It makes use of a task from the artdata package to set up the echelle
  structure and then the linear spectrum WCS and the flux values are added.
  The default is to extract all the orders from extension version 1.
  </p>
  <p>
  For context: this data format is specific to the GHOST instrument. When
  reduced using DRAGONS, two different outputs are produced (for each <span style="font-family: monospace;">"blue"</span>
  and <span style="font-family: monospace;">"red"</span> arms of the spectrograph):
  </p>
  <dl>
  <dt><b>*_calibrated.fits</b></dt>
  <!-- Sec='DESCRIPTION The GHOST2MS task converts the DRAGONS-calibrated output for the' Level=0 Label='' Line='*_calibrated.fits' -->
  <dd>Reduced spectra before stitching the orders. The flux pixels are in a 3D
  array with the first axis of size 2, one for the target, one for the sky,
  then a second axis for the wavelength direction, and finally a third axis
  with several orders. The WAVL extension contains the wavelength at each pixel
  in the wavelength-order array.
  </dd>
  </dl>
  <dl>
  <dt><b>*_dragons.fits</b></dt>
  <!-- Sec='DESCRIPTION The GHOST2MS task converts the DRAGONS-calibrated output for the' Level=0 Label='' Line='*_dragons.fits' -->
  <dd>1D extracted spectrum. Orders have been stitched together. The algorithm
  resamples the order wavelengths to a common log-spaced scale, interpolates
  the orders to that new wavelength scale, and then averages the fluxes from
  each order with an inverse variance weighting.
  </dd>
  </dl>
  <p>
  There are two issues here: the <span style="font-family: monospace;">"*dragons.fits"</span> file opens on <span style="font-family: monospace;">"splot"</span> but
  the wavelength solution is wrong. The DRAGONS team provided a recipe to fix
  that, so we have a file called <span style="font-family: monospace;">"_dragons_irafCompatible.fits"</span>. However, many
  of our users want to normalize the spectra order-by-order, so none of those
  are good options.
  </p>
  <p>
  This task is a script and so users may copy it and modify it as desired.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the ring averages with labels and output to the terminal.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Convert the red arm calibrated frame.
  onedspec&gt; ghost2ms S20230416S0079_red001_calibrated.fits
  S20230416S0079_red_calib[SCI,1][*,1:33] -&gt; S20230416S0079_red_calib_iraf
  
  # Convert the blue arm calibrated frame.
  onedspec&gt; ghost2ms S20240322S0068_blue001_calibrated.fits
  S20240322S0068_blue_calib[SCI,1][*,1:33] -&gt; S20240322S0068_blue_calib_iraf
  
  # Use SPLOT to view the result.
  onedspec&gt; splot S20230416S0079_red_calib_iraf 1 unit=nm
  onedspec&gt; splot S20240322S0068_blue_calib_iraf 1 unit=nm
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mkechelle, sapertures, imcopy
  </p>
  
  </section>
  
  <!-- Contents: 'NAME ghost2ms -- Convert Gemini/DRAGONS GHOST format to IRAF multispec format' 'USAGE ghost2ms input output' 'PARAMETERS' 'DESCRIPTION The GHOST2MS task converts the DRAGONS-calibrated output for the' 'EXAMPLES' 'SEE ALSO'  -->
  

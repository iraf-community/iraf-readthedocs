.. _extinction:

extinction: Apply atmospheric extinction corrections to images (obsolete)
=========================================================================

**Package: longslit**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  extinction images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images to be extinction corrected.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output extinction corrected images.  Output images may be the
  same as the input images.
  </dd>
  </dl>
  <dl id="l_extinction">
  <dt><b>extinction = <span style="font-family: monospace;">"onedstds$kpnoextinct.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extinction' Line='extinction = "onedstds$kpnoextinct.dat"' -->
  <dd>Extinction file to be used.  The standard extinction files:
  <div class="highlight-default-notranslate"><pre>
  onedstds$kpnoextinct.dat - KPNO standard extinction
  onedstds$ctioextinct.dat - CTIO standard extinction
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The specified images are corrected for atmospheric extinction according
  to the formula
  </p>
  <p>
      correction factor = 10 ** (0.4 * airmass * extinction)
  </p>
  <p>
  where the extinction is a tabulated function of the wavelength.  The
  extinction file contains lines of wavelength and extinction at that
  wavelength.  The units of the wavelength must be the same as those of
  the dispersion corrected images; i.e. Angstroms.   If the image is
  dispersion corrected in logarithmic wavelength intervals (DC-FLAG = 1)
  the task will convert to wavelength and so the extinction file must
  still be wavelength.  The table values are interpolated
  to the wavelengths of the image pixels and the correction applied to
  the pixel values.  Note that the image pixel values are modifed.
  </p>
  <p>
  The airmass is sought in the image header under the name AIRMASS.  If the
  airmass is not found then it is computed from the zenith distance (ZD in hours)
  using the approximation formula from Allen's <span style="font-family: monospace;">"Astrophysical Quantities"</span>, 1973,
  page125 and page 133
  </p>
  <p>
  	AIRMASS = sqrt (cos (ZD) ** 2 + 2 * scale + 1)
  </p>
  <p>
  where the atmospheric scale height is set to be 750.  If the parameter ZD
  is not found then it must be computed from the hour angle (HA in hours),
  the declination (DEC in degrees), and the observation latitude (LATITUDE
  in degress).   The hour angle may be computed from the right ascension
  (RA in hours) and siderial time (ST in hours).  Computed quantities are
  recorded in the image header.  Flags indicating extinction correction are
  also set in the image header.
  </p>
  <p>
  The image header keyword DISPAXIS must be present with a value of 1 for
  dispersion parallel to the lines (varying with the column coordinate) or 2
  for dispersion parallel to the columns (varying with line coordinate).
  This parameter may be added using <b>hedit</b>.  Note that if the image has
  been transposed (<b>imtranspose</b>) the dispersion axis should still refer
  to the original dispersion axis unless the physical world coordinate system
  is first reset (see <b>wcsreset</b>).  This is done in order to allow images
  which have DISPAXIS defined prior to transposing to still work correctly
  without requiring this keyword to be changed.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. A set of dispersion corrected images is extinction corrected in-place as
  follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; extinction img* img*
  </pre></div>
  <p>
  2. To keep the uncorrected image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; extinction nite1.004 nite1ext.004
  </pre></div>
  <p>
  3.  If the DISPAXIS keyword is missing and the dispersion is running
  vertically (varying with the image lines):
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit *.imh dispaxis 2 add+
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES'  -->
  

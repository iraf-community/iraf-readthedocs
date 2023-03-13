.. _lcalib:

lcalib: List calibration file data
==================================

**Package: iids**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  lcalib option star_name
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_option">
  <dt><b>option</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='option' Line='option' -->
  <dd>Chooses calibration data to be listed.  Option
  may be: <span style="font-family: monospace;">"bands"</span> to list the bandpasses at each wavelength, <span style="font-family: monospace;">"ext"</span> to
  list the extinction at each wavelength, <span style="font-family: monospace;">"mags"</span>, <span style="font-family: monospace;">"fnu"</span>, or <span style="font-family: monospace;">"flam"</span>
  to list the magnitude, or flux of
  the star (selected by the star_name parameter) at each wavelength, or
  <span style="font-family: monospace;">"stars"</span> to list the star names available in the calibration directory.
  </dd>
  </dl>
  <dl id="l_star_name">
  <dt><b>star_name</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='star_name' Line='star_name' -->
  <dd>Selects which star's magnitude list is chosen if the option parameter
  is <span style="font-family: monospace;">"mags"</span>, <span style="font-family: monospace;">"fnu"</span>, <span style="font-family: monospace;">"flam"</span>, or <span style="font-family: monospace;">"bands"</span>.  Also if <span style="font-family: monospace;">'?'</span> a list of available
  stars in the specified calibration directory is given.
  </dd>
  </dl>
  <p>
  The following three queried parameters apply if the selected calibration
  file is for a blackbody.  See <b>standard</b> for further details.
  </p>
  <dl id="l_mag">
  <dt><b>mag</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mag' Line='mag' -->
  <dd>The magnitude of the observed star in the band given by the
  <i>magband</i> parameter.  If the magnitude is not in the same band as
  the blackbody calibration file then the magnitude may be converted to
  the calibration band provided the <span style="font-family: monospace;">"params.dat"</span> file containing relative
  magnitudes between the two bands is in the calibration directory
  </dd>
  </dl>
  <dl id="l_magband">
  <dt><b>magband</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='magband' Line='magband' -->
  <dd>The standard band name for the input magnitude.  This should generally
  be the same band as the blackbody calibration file.  If it is
  not the magnitude will be converted to the calibration band.
  </dd>
  </dl>
  <dl id="l_teff">
  <dt><b>teff</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='teff' Line='teff' -->
  <dd>The effective temperature (deg K) or the spectral type of the star being
  calibrated.  If a spectral type is specified a <span style="font-family: monospace;">"params.dat"</span> file must exist
  in the calibration directory.  The spectral types are specified in the same
  form as in the <span style="font-family: monospace;">"params.dat"</span> file.  For the standard blackbody calibration
  directory the spectral types are specified as A0I, A0III, or A0V, where A
  can be any letter OBAFGKM, the single digit subclass is between 0 and 9,
  and the luminousity class is one of I, III, or V.  If no luminousity class
  is given it defaults to dwarf.
  </dd>
  </dl>
  <dl id="l_extinction">
  <dt><b>extinction</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extinction' Line='extinction' -->
  <dd>Extinction file.  The current standard extinction files:
  <div class="highlight-default-notranslate"><pre>
  onedstds$kpnoextinct.dat - KPNO standard extinction
  onedstds$ctioextinct.dat - CTIO standard extinction
  </pre></div>
  </dd>
  </dl>
  <dl id="l_caldir">
  <dt><b>caldir</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='caldir' Line='caldir' -->
  <dd>Calibration directory containing standard star data.  The directory name
  must end with /.  The current calibration directories available in the
  onedstds$ may be listed with the command:
  <div class="highlight-default-notranslate"><pre>
  cl&gt; page onedstds$README
  </pre></div>
  </dd>
  </dl>
  <dl id="l_fnuzero">
  <dt><b>fnuzero = 3.68e-20</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fnuzero' Line='fnuzero = 3.68e-20' -->
  <dd>The absolute flux per unit frequency at a magnitude of zero.  This is used
  to convert the calibration  magnitudes to absolute flux by the formula
  	Flux = fnuzero * 10. ** (-0.4 * magnitude)
  The flux units are also determined by this parameter.  However, the
  frequency to wavelength interval conversion assumes frequency in hertz.
  The default value is based on a calibration of Vega at 5556 Angstroms of
  3.52e-20 ergs/cm2/s/hz for a magnitude of 0.048.  This default value
  is that used in earlier versions of this task which did not allow the
  user to change this calibration.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  LCALIB provides a means of checking the flux calibration data.  The calibration
  data consists of extinction, bandpasses, and stellar magnitudes.
  </p>
  <p>
  The extinction is given in an extinction file consisting of lines with
  wavelength and extinction.  The wavelengths must be order in increasing
  wavelength and the wavelengths must be in Angstroms.  There are two
  standard extinction files currently available, <span style="font-family: monospace;">"onedstds$kpnoextinct.dat"</span>,
  and <span style="font-family: monospace;">"onedstds$ctioextinct.dat"</span>.
  </p>
  <p>
  The standard star data are in files in a calibration
  directory specified with the parameter <i>caldir</i>.  A standard star
  file is selected by taking the star name given, by the parameter
  <i>star_name</i>, removing blanks, +'s and -'s, appending <span style="font-family: monospace;">".dat"</span>, and converting
  to lower case.  This file name is appended to the specified calibration
  directory.  A calibration file consists of lines containing a wavelength,
  a stellar magnitude, and a bandpass full width.  The wavelengths are in
  Angstroms.  Comment lines beginning with # may be included in the file.
  The star names printed by this task are just the first line of each file
  in the calibration directory with the first character (#) removed.
  The calibration files may be typed, copied, and printed.  <b>Lcalib</b>
  may also be used to list data from the calibration files.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  # List the extinction table
  cl&gt; lcalib ext
  # Plot the extinction table
  cl&gt; lcalib ext | graph
  # Plot the energy distribution
  cl&gt; lcalib mags "bd+28 4211" | graph
  # List the names of all the stars
  cl&gt; lcalib stars caldir=onedstds$irscal/
  # As above but for IIDS file
  cl&gt; lcalib stars calib_file=onedstds$iidscal/
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_LCALIB">
  <dt><b>LCALIB V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='LCALIB' Line='LCALIB V2.10' -->
  <dd>This task has a more compact listing for the <span style="font-family: monospace;">"stars"</span> option and allows
  paging a list of stars when the star name query is not recognized.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  standard, sensfunc, onedstds$README
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

.. _calibrate:

calibrate: Apply extinction and flux calibrations to spectra
============================================================

**Package: longslit**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  calibrate input output [records]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input spectra to be calibrated.  When using record format
  extensions the root names are specified, otherwise full image names
  are used.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of calibrated spectra.  If no output list is specified or if the
  output name is the same as the input name then the calibrated spectra
  replace the input spectra.  When using record format extensions the output
  names consist of root names to which the appropriate record number
  extension is added.  The record number extension will be the same as the
  input record number extension.  The output spectra are coerced to have
  real datatype pixels regardless of the  pixel type.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records (imred.irs and imred.iids only)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records (imred.irs and imred.iids only)' -->
  <dd>The set of record number extensions to be applied to each input and output
  root name when using record number extension format.  The syntax consists
  of comma separated numbers or ranges of numbers.  A range consists of
  two numbers separated by a hyphen.  This parameter is not queried
  when record number formats are not used.
  </dd>
  </dl>
  <dl id="l_extinct">
  <dt><b>extinct = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extinct' Line='extinct = yes' -->
  <dd>Apply extinction correction if a spectrum has not been previously
  corrected?  When applying an extinction correction, an extinction file
  is required.
  </dd>
  </dl>
  <dl id="l_flux">
  <dt><b>flux = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flux' Line='flux = yes' -->
  <dd>Apply a flux calibration if a spectrum has not been previously calibrated?
  When applying a flux calibration, sensitivity spectra are required.
  </dd>
  </dl>
  <dl id="l_extinction">
  <dt><b>extinction = &lt;no default&gt;</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extinction' Line='extinction = &lt;no default&gt;' -->
  <dd>Extinction file for the observation.  Standard extinction files
  are available in the <span style="font-family: monospace;">"onedstds$"</span> directory.
  </dd>
  </dl>
  <dl id="l_observatory">
  <dt><b>observatory = <span style="font-family: monospace;">")_.observatory"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observatory' Line='observatory = ")_.observatory"' -->
  <dd>Observatory at which the spectra were obtained if not specified in the
  image header by the keyword OBSERVAT.  The default is a redirection to the
  package parameter of the same name.  The observatory may be one of the
  observatories in the observatory database, <span style="font-family: monospace;">"observatory"</span> to select the
  observatory defined by the environment variable <span style="font-family: monospace;">"observatory"</span> or the
  parameter <b>observatory.observatory</b>, or <span style="font-family: monospace;">"obspars"</span> to select the current
  parameters in the <b>observatory</b> task.  See <b>observatory</b> for
  additional information.
  </dd>
  </dl>
  <dl id="l_ignoreaps">
  <dt><b>ignoreaps = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ignoreaps' Line='ignoreaps = no' -->
  <dd>Ignore aperture numbers and apply a single flux calibration to all
  apertures?  Normally multiaperture instruments have separate sensitivity
  functions for each aperture while long slit or Fabry-Perot data use a
  single sensitivity function where the apertures are to be ignored.  The
  sensitivity spectra are obtained by adding the aperture number as an
  extension to the sensitivity spectrum root name.  When apertures are
  ignored the specified sensitivity spectrum name is used without adding an
  extension and applied to all input apertures.
  </dd>
  </dl>
  <dl id="l_sensitivity">
  <dt><b>sensitivity = <span style="font-family: monospace;">"sens"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sensitivity' Line='sensitivity = "sens"' -->
  <dd>The root name for the sensitivity spectra produced by <b>sensfunc</b>.
  Normally with multiaperture instruments, <b>sensfunc</b> will produce a
  spectrum appropriate to each aperture with an aperture number extension.
  If the apertures are ignored (<i>ignoreaps</i> = yes) then the sensitivity
  spectrum specified is used for all apertures and no aperture number is
  appended automatically.
  </dd>
  </dl>
  <dl id="l_fnu">
  <dt><b>fnu = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fnu' Line='fnu = no' -->
  <dd>The default calibration is into units of flux per unit wavelength (F-lambda).
  If <i>fnu</i> = yes then the calibrated spectrum will be in units of
  flux per unit frequency (F-nu).
  </dd>
  </dl>
  <dl id="l_airmass">
  <dt><b>airmass, exptime</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='airmass' Line='airmass, exptime' -->
  <dd>If the airmass and exposure time are not in the header nor can they be
  determined from other keywords in the header then these query parameters
  are used to request the airmass and exposure time.  The values are updated
  in the input and output images.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The input spectra are corrected for extinction and calibrated to a flux
  scale using sensitivity spectra produced by the task <b>sensfunc</b>.
  One or both calibrations may be performed by selecting the appropriate
  parameter flags.  It is an error if no calibration is specified.  Normally
  the spectra should be extinction corrected if also flux calibrating.
  The image header keywords DC-FLAG (or the dispersion type field in the
  <span style="font-family: monospace;">"multispec"</span> world coordinate system), EX-FLAG, and CA-FLAG are checked for
  dispersion solution (required), previous extinction correction, and
  previous flux calibration.  If previously calibrated the spectrum is
  skipped and a new output image is not created.
  </p>
  <p>
  The input spectra are specified by a list of root names (when using record
  extension format) or full image names.  The output calibrated spectra may
  replace the input spectra if no output spectra list is specified or if the
  output name is the same as the input name.  When using record number
  extensions the output spectra will have the same extensions applied to the
  root names as those used for the input spectra.
  </p>
  <p>
  When applying an extinction correction the AIRMASS keyword is sought.
  If the keyword is not present then the airmass at the time defined
  by the other header keywords is computed using the
  latitude of the observatory and observation parameters in the image
  header.  The observatory is first determined from the image under the
  keyword OBSERVAT.  If absent the observatory specified by the task
  parameter <span style="font-family: monospace;">"observatory"</span> is used.  See <b>observatory</b> for further
  details of the observatory database.  If the air mass cannot be
  determined an error results.  Currently a single airmass is used
  and no correction for changing extinction during the observation is
  made and adjustment to the middle of the exposure.  The task
  <b>setairmass</b> provides a correction for the exposure time to compute
  an effective air mass.  Running this task before calibration is
  recommended.
  </p>
  <p>
  If the airmass is not in the header and cannot be computed then
  the user is queried for a value.  The value entered is then
  recorded in both the input and output image headers.  Also if
  the exposure time is not found then it is also queried and
  recorded in the image headers.
  </p>
  <p>
  The extinction correction is given by the factor
  </p>
  <p>
  		10. ** (0.4 * airmass * extinction)
  </p>
  <p>
  where the extinction is the value interpolated from the specified
  extinction file for the wavelength of each pixel.  After extinction
  correction the EX-FLAG is set to 0.
  </p>
  <p>
  When applying a flux calibration the spectra are divided by the
  aperture sensitivity which is represented by a spectrum produced by
  the task <b>sensfunc</b>.  The sensitivity spectrum is in units of:
  </p>
  <p>
  	2.5 * Log10 [counts/sec/Ang / ergs/cm2/sec/Ang].
  </p>
  <p>
  A new spectrum is created in <span style="font-family: monospace;">"F-lambda"</span> units - ergs/cm2/sec/Angstrom
  or <span style="font-family: monospace;">"F-nu"</span> units - ergs/cm2/sec/Hz.  The sensitivity must span the range of
  wavelengths in the spectrum and interpolation is used if the wavelength
  coordinates are not identical.  If some pixels in the spectrum being
  calibrated fall outside the wavelength range of the sensitivity function
  spectrum a warning message giving the number of pixels outside the
  range.  In this case the sensitivity value for the nearest wavelength
  in the sensitivity function is used.
  </p>
  <p>
  Multiaperture instruments typically have
  a separate aperture sensitivity function for each aperture.  The appropriate
  sensitivity function for each input spectrum is selected based on the
  spectrum's aperture by appending this number to the root sensitivity function
  spectrum name.  If the <i>ignoreaps</i> flag is set, however, the aperture
  number relation is ignored and the single sensitivity spectrum (without
  extension) is applied.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To flux calibrates a series of spectra replacing the input spectra by
  the calibrated spectra:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; calibrate nite1 ""
  </pre></div>
  <p>
  2.  To only extinction correct echelle spectra:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; calibrate ccd*.ec.imh new//ccd*.ec.imh flux-
  </pre></div>
  <p>
  3. To flux calibrate a long slit spectrum:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dispaxis = 2
  cl&gt; calibrate obj.imh fcobj.imh
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_CALIBRATE">
  <dt><b>CALIBRATE V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='CALIBRATE' Line='CALIBRATE V2.10.3' -->
  <dd>This task was revised to operate on 2D and 3D spatial spectra; i.e. long
  slit and Fabry-Perot data cubes.  This task now includes the functionality
  previously found in <b>longslit.extinction</b> and <b>longslit.fluxcalib</b>.
  A query for the airmass and exposure time is now made if the information
  is not in the header and cannot be computed from other header keywords.
  </dd>
  </dl>
  <dl id="l_CALIBRATE">
  <dt><b>CALIBRATE V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='CALIBRATE' Line='CALIBRATE V2.10' -->
  <dd>This task was revised to operate on nonlinear dispersion corrected spectra
  and 3D images (the <b>apextract</b> <span style="font-family: monospace;">"extras"</span>).  The aperture selection
  parameter was eliminated (since the header structure does not allow mixing
  calibrated and uncalibrated spectra) and the latitude parameter was
  replaced by the observatory parameter.  The observatory mechanism insures
  that if the observatory latitude is needed for computing an airmass and the
  observatory is specified in the image header the correct calibration will
  be applied.  The record format syntax is available in the <b>irs/iids</b>
  packages.  The output spectra are coerced to have real pixel datatype.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  setairmass, standard, sensfunc, observatory, continuum
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

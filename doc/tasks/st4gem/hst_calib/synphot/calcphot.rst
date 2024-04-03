.. _calcphot:

calcphot: Calculate photometric quantities for spectra and passbands.
=====================================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  calcphot obsmode spectrum form 
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task will calculate predicted count rates or fluxes in a given
  passband for a specified object.  Other information such as average
  wavelength, full width at half-maximum, and rms wavelength can also be
  calculated.  The output may be saved to an ST4GEM table if desired.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_obsmode">
  <dt><b>obsmode [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obsmode' Line='obsmode [string]' -->
  <dd>This is a sequence of commands that create the synthetic
  passband.  The commands can be placed in a file, whose name is passed to 
  this parameter, preceded by a <span style="font-family: monospace;">"@"</span> character, e.g., '@filename'. Each
  line in this command file is treated as a separate set of commands.
  Each command may either be a simple bandpass, which is represented by
  a comma separated string of keywords uniquely specifying an observing
  mode of the telescope, or a more complex command, described in the
  help file for 'calcband'. The keywords which make up the observing
  mode are explained further in the obsmode task.
  </dd>
  </dl>
  <dl id="l_spectrum">
  <dt><b>spectrum [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectrum' Line='spectrum [string]' -->
  <dd>This is a sequence of commands that create the synthetic spectrum.
  The commands can be placed in a file, whose name is passed to this
  parameter, preceded by a <span style="font-family: monospace;">"@"</span> character, e.g., '@filename'. Each line
  in this command file is treated as a separate set of commands.
  The commands that can be passed to this parameter are described in
  detail in the help file for the 'calcspec' task.
  </dd>
  </dl>
  <dl id="l_form">
  <dt><b>form = photlam [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='form' Line='form = photlam [string]' -->
  <dd>Desired output form for the calculation.  The following forms are 
  recognized:
  <div class="highlight-default-notranslate"><pre>
  
  FNU             ergs / s / cm^2 / Hz
  FLAM            ergs / s / cm^2 / A
  PHOTNU          photons / s / cm^2 / Hz
  PHOTLAM         photons / s / cm^2 / A
  COUNTS          photons / s
  ABMAG           -2.5 log_10 (FNU)  - 48.60
  STMAG           -2.5 log_10 (FLAM) - 21.10
  OBMAG           -2.5 log_10 (COUNTS)
  VEGAMAG         -2.5 log_10 (F/F_vega)
  JY              10^-23 ergs / s / cm^2 / Hz
  MJY             10^-26 ergs / s / cm^2 / Hz
  </pre></div>
  Note that if form = counts or obmag, the result will be integrated
  over the passband and normalized to the collecting area of the HST.
  If any of the photometric forms is specified the result of the
  calculation is the flux of the spectrum in 'spectrum' observed in the
  mode 'obsmode' in the units given by 'form'. The task always
  calculates and displays the values of PIVLAM and FWHMLAM in addition
  to the quantity chosen by 'form'.
  A standard magnitude system is VEGAMAG, for which Vega by definition
  has magnitude 0 at all wavelengths. The AB and ST magnitude systems are
  based on constant flux per unit frequency and per unit wavelength,
  respectively.  The zero points for these two systems are set for
  convenience so that Vega has magnitude 0 in both systems for the
  Johnson V passband.
  </dd>
  </dl>
  <dl>
  <dt><b>(func = <span style="font-family: monospace;">"effstim"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(func = "effstim") [string]' -->
  <dd>The desired output function. The default value (effstim) calculates
  the predicted count rate or flux. This is the function most users of
  calcphot will wish to use.
  The other function compute various functions of the product of the
  passband throughput and the spectrum.  The spectrum is first converted
  into the units specified by the parameter 'form' before computing the
  function, so results will be dependent on whether the form has
  frequency or wavelength units. The sole exception is the effective wavelength
  (efflerg), which is always calculated with the flux in units
  of <span style="font-family: monospace;">"flam"</span>.
  The <span style="font-family: monospace;">"efflphot"</span> function is deprecated. It is provided solely to 
  facilitate comparisons with <span style="font-family: monospace;">"efflam"</span> results calculated by earlier
  versions of calcphot, which incorrectly implemented the Koornneef et al
  definition of effective wavelength. 
  <div class="highlight-default-notranslate"><pre>
  NAME            PARAMETER
  =======         =========
  EFFSTIM         effective stimulus      (form)
  AVGLAM          average wavelength      (Angstroms)
  BARLAM          mean log wavelength     (Angstroms)
  FWHMLAM         FWHM bandwidth          (Angstroms)
  RMSLAM          rms bandwidth           (Angstroms)
  EFFLERG         effective wavelength    (Angstroms)
  EFFLPHOT        (deprecated - see above)(Angstroms)
  </pre></div>
  </dd>
  </dl>
  <dl>
  <dt><b>(vzero = <span style="font-family: monospace;">" "</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vzero = " ") [string]' -->
  <dd>A list of values to substitute for variable zero. Each value in the
  list is substituted in turn for the string '$0' wherever it occurs in
  the input spectrum. The values must be real numbers.  Using vzero is
  the equivalent of placing the input spectrum several times in a
  file, with each spectrum containing one of the values in the list. The
  list may contain single values or ranges. The endpoints of the ranges
  are separated by a dash. An optional step size follows the range,
  preceded by the letter <span style="font-family: monospace;">'x'</span>. If the step size is not present, the step
  size defaults to 1 or -1, depending on the order of the endpoints.
  The following table gives several examples of valid lists
  <div class="highlight-default-notranslate"><pre>
  .1,.2,.3,.4     A list of single values
  .1-.4x.1        The same list expressed as a range
  -1 - -4         A range with an implicit step size of -1
  1-9,10-20x2     A list of more than one range
  </pre></div>
  </dd>
  </dl>
  <dl>
  <dt><b>(output = <span style="font-family: monospace;">"none"</span>) [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(output = "none") [file name]' -->
  <dd>Name of the table file in which to store results.
  The name of the first column is COUNTRATE if the effective stimulus is
  computed. Otherwise, it is the name of the functional form. The names
  of the remaining columns are FORM, OBSMODE and TARGETID.  There is one
  table row for each calculation performed.  This table can be used as
  input to the 'plspec' task and other tasks using the pfile (photometry
  file) parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>(wavetab = <span style="font-family: monospace;">" "</span>) [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wavetab = " ") [file name]' -->
  <dd>Name of an optional wavelength table or file. An appropriate table can
  be generated by using the 'genwave' task. If a table is used, the
  wavelength column name must be <span style="font-family: monospace;">"WAVELENGTH"</span>. If an ASCII file is used
  the first column is taken to be the wavelength column.  The
  subdirectory 'synphot$data has ASCII wavelength tables useful for
  specific HST passbands.  
  If no wavelength table is specified, a default wavelength set is
  used. The default wavelength table covers the wavelength range where
  the obsmode and spectrum are non-zero. Wavelengths are spaced
  logarithmically over this range. If there is more than one obsmode and
  spectrum, the range is computed based on the first pair. If the
  wavelength range of the obsmodes and spectra differ significantly, a
  wavelength table should be specified explicitly.
  </dd>
  </dl>
  <dl>
  <dt><b>(result) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(result) [real]' -->
  <dd>The result of the synthetic photometry calculation.  This can be the
  observed flux of the spectrum in the observation mode or it can be an
  average wavelength. See the form parameter for valid forms to be
  calculated.
  This parameter contains the result of the last calculation performed,
  so if several spectra or modes are given in a file, or a list of
  values for vzero is specified, then only the last calculation will be
  saved.
  </dd>
  </dl>
  <dl>
  <dt><b>(refdata = <span style="font-family: monospace;">""</span>) [pset name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(refdata = "") [pset name]' -->
  <dd>Parameter set for reference data used in calculations.
  This pset contains the following parameters:
  <div class="highlight-default-notranslate"><pre>
  
  area = 45238.93416:  HST telescope area in cm**2.
  
  grtbl = "mtab$*.tmg":  HST graph table.  By default, this
          uses the most recent version available.
  
  cmptbl = "mtab$*.tmc":  Instrument component table.  By
          default, this uses the most recent version available.
  
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Calculate the pivot wavelength, full width at half-maximum (FWHM),
  and the total flux (in counts per second) of a 5000 K blackbody in the WFPC 
  F555W passband.  The blackbody spectrum is renormalized to have a V
  magnitude of 18.6.
  </p>
  <p>
  sy&gt; calcphot <span style="font-family: monospace;">"band(wfpc,f555w)"</span> <span style="font-family: monospace;">"rn(bb(5000),band(v),18.6,vegamag)"</span> counts
  </p>
  <p>
  2. Perform the same calculation, only use the abbreviated notation for
  the bandpass.
  </p>
  <p>
  sy&gt; calcphot wfpc,f555w <span style="font-family: monospace;">"rn(bb(5000),band(v),18.6,vegamag)"</span> counts
  </p>
  <p>
  3. Calculate the pivot wavelength and FWHM of a 5000 K blackbody in
  both the WFPC F555W and F785LP passbands.  Find the color difference (in
  instrumental magnitudes) of the blackbody in the two passbands for values
  of E(B-V) of 0.0, 0.25, and 0.5.
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; calcphot "band(wfpc,f555w) - band(wfpc,f785lp)" "bb(5000)*ebmv($0)" \
  &gt;&gt;&gt; obmag vzero="0.0,0.25,0.5"
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by B.Simon based on XCAL code written by Keith Horne.
  Modified by V.Laidler. (effective wavelength modifications)
  </p>
  <p>
  Koornneef et al, 1986, <span style="font-family: monospace;">"Synthetic Photometry and the Calibration of the 
  Hubble Space Telescope"</span>, Highlights of Astronomy vol 7 
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  calcband, calcspec, countrate
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

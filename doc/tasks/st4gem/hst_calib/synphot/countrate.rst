.. _countrate:

countrate: Evaluate the photometric count rate of the HST.
==========================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  countrate instrument
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task computes the predicted flux for a specified source spectrum
  and telescope observing mode. At the user's option, it can also create
  an output spectrum containing the flux as a function of
  wavelength. The observing mode of the HST is specified in several task
  parameters.  These are 'instrument', 'detector', 'spec_elem', and
  'aperture'. The instrument must always be specified, but the other
  three parameters may be blank, depending on which instrument and
  instrument configuration is used. If you set the instrument to <span style="font-family: monospace;">"hrs"</span>
  or <span style="font-family: monospace;">"stis"</span>, you should also specify 'cenwave', the central wavelength
  of the spectrum. This parameter has no effect on any of the other
  instruments. More than one observing mode keyword may be specified in
  a task parameter by separating the keywords with a comma. The obsmode
  task has more information on the legal observing mode keywords.
  </p>
  <p>
  The target spectrum is specified in the spectrum' parameter.  The
  'crcalspec$' and 'crgrid$' directories contain some tables which can be 
  used as source spectra.  The spectrum may also be one of several
  functions. The functions have the form of a function name followed by
  one or more arguments in parentheses.  Here are a few of the supported
  functions. More are described in the help for calcspec.
  </p>
  <div class="highlight-default-notranslate"><pre>
  bb(temp)                A black body at the specified temperature
  hi(temp,colden)         Emission spectrum of an LTE slab of hydrogen at
                          the specified temperature and column density
  pl(refval,exp,units)    Powerlaw spectrum of the form
                          (wavelength/refval)**exp
  </pre></div>
  <p>
  The 'magnitude' parameter is used to normalize the spectrum to a
  chosen absolute flux level by specifying an integrated broadband
  magnitude for the spectrum. This parameter has two words. The first is
  the integrated magnitude, in units of 'magform'. The second is the
  passband over which the magnitude is integrated. This may be fully
  specified in the usual syntax (eg, <span style="font-family: monospace;">"johnson,V"</span> or <span style="font-family: monospace;">"sdss,g"</span>) or
  abbreviated by specifying a single letter. If no system name is given
  for any of the UBVRIJHK bands, the defaults are Johnson UBV, Cousins
  RI, and Bessell JHK.
  </p>
  <p>
  The output table is specified by the parameter 'output'. If this
  parameter is set to <span style="font-family: monospace;">"none"</span> (the default) or left blank, no output
  table will be created. Otherwise, the task will create a table of
  wavelength versus flux.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_spectrum">
  <dt><b>spectrum [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectrum' Line='spectrum [string]' -->
  <dd>A file name or function string specifying the spectrum to be
  evaluated.  If this parameter is a file name, it must be a table
  containing two columns, WAVELENGTH and FLUX. The WAVELENGTH column
  must have units of Angstroms and must be in ascending or descending
  order. If it is a function string, the first word in the string gives
  the functional form of the spectrum and the remaining words are a
  parentehsized list of arguments to the function. The following
  functions are a few of the supported functions:
  <div class="highlight-default-notranslate"><pre>
  bb(temp)                A black body at the specified temperature
  hi(temp,colden)         Emission spectrum of an LTE slab of hydrogen at
                          the specified temperature and column density
  pl(refval,exp,unit)     Powerlaw spectrum of the form
                          (wavelength/refval)**exp
  </pre></div>
  </dd>
  </dl>
  <dl id="l_magnitude">
  <dt><b>magnitude [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='magnitude' Line='magnitude [string]' -->
  <dd>The integrated magnitude of the spectrum. The first word gives the
  magnitude in units of VEGAMAG and the second word specifies the
  desired passband. The passband is generally abbreviated with a single
  letter, although it may be fully specified in the usual syntax (eg,
  <span style="font-family: monospace;">"johnson,V"</span> or <span style="font-family: monospace;">"sdss,g"</span>). If no system name is given for any of the
  UBVRIJHK bands, the defaults are Johnson UBV, Cousins RI, and Bessell
  JHK. If this parameter is left blank or set to <span style="font-family: monospace;">"none"</span>, the spectrum
  will not be renormalized.
  </dd>
  </dl>
  <dl id="l_instrument">
  <dt><b>instrument [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='instrument' Line='instrument [string]' -->
  <dd>The name of the telescope instrument used in the observation.
  </dd>
  </dl>
  <dl>
  <dt><b>(detector = <span style="font-family: monospace;">" "</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(detector = " ") [string]' -->
  <dd>The name of the instrument detector, if there is more than one available
  for the instrument being used.
  </dd>
  </dl>
  <dl>
  <dt><b>(spec_elem = <span style="font-family: monospace;">" "</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(spec_elem = " ") [string]' -->
  <dd>The name of the spectral elements, such as filters or gratings, used
  in the observation.
  </dd>
  </dl>
  <dl>
  <dt><b>(aperture = <span style="font-family: monospace;">" "</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(aperture = " ") [string]' -->
  <dd>The name of the instrument aperture, if there is more than one available 
  for the instrument being used.
  </dd>
  </dl>
  <dl>
  <dt><b>(cenwave = INDEF) [real] [min = 1.0,  max = 200000.]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(cenwave = INDEF) [real] [min = 1.0,  max = 200000.]' -->
  <dd>The central wavelength of the observation, in Angstroms. The output
  spectrum will be centered on this wavelength. If this parameter is set
  to INDEF, the output spectrum will contain the entire wavelength range
  that the observation mode covers. This parameter only effects the HRS
  and STIS, because they are the only instrument where the detector
  cannot cover the entire wavelength range of the observation.
  </dd>
  </dl>
  <dl>
  <dt><b>(exptime = 1.0) [real] [min = 0.0, max = INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(exptime = 1.0) [real] [min = 0.0, max = INDEF]' -->
  <dd>The exposure time in seconds.
  </dd>
  </dl>
  <dl>
  <dt><b>(reddening = 0.0) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(reddening = 0.0) [real]' -->
  <dd>The E(B-V) extinction to be applied to the input spectrum.  Either the
  user spectrum or a synthetic spectrum may be modified by this
  parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>(redlaw = <span style="font-family: monospace;">"gal1"</span>) [string, allowed values: gal1|gal2|gal3|smc|lmc|xgal]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(redlaw = "gal1") [string, allowed values: gal1|gal2|gal3|smc|lmc|xgal]' -->
  <dd>The type of reddening law used to compute the extinction. The task
  supports three galactic reddening laws (gal1 to gal3) and one law each
  for the Small Magellanic Cloud (smc), Large Magellanic Cloud (lmc),
  and extra-galactic objects (xgal). The laws are derived from the
  following papers.
  <div class="highlight-default-notranslate"><pre>
  gal1    Seaton (1979) MNRAS, vol 187, p. 75
  gal2    Savage &amp; Mathis (1979) ARA&amp;A, vol. 17, p. 73-111
  gal3    Cardelli, Clayton &amp; Mathis (1989) ApJ vol. 345, p. 245-256
  smc     Prevot et al. (1984) A&amp;A, vol. 132, p. 389-392
  lmc     Howarth (1983) MNRAS, vol. 203, p. 301
  xgal    Calzetti, Kinney and Storchi-Bergmann, (1994) ApJ, vol. 429, p.582
  </pre></div>
  </dd>
  </dl>
  <dl>
  <dt><b>(output = <span style="font-family: monospace;">"none"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(output = "none") [string]' -->
  <dd>The name of the output spectrum produced by this task. If this
  parameter is set to <span style="font-family: monospace;">"none"</span> (the default) or a blank string, no output
  table will be created. Otherwise, it will create an ST4GEM table with
  two columns, WAVELENGTH and FLUX. The WAVELENGTH column will contain
  wavelengths in Angstroms. The FLUX column will contain the flux at the
  corresponding wavelengths. The table will also contain the header
  parameters GRFTABLE, CMPTABLE, OBSMODE, SPECTRUM, and EXPTIME. These
  will contain the name of the graph table, the component lookup table,
  the observation mode and spectral expression constructed from the task
  parameters, and the exposure time.
  </dd>
  </dl>
  <dl>
  <dt><b>(form = <span style="font-family: monospace;">"counts"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(form = "counts") [string]' -->
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
  A standard magnitude system is VEGAMAG, for which Vega by definition
  has magnitude 0 at all wavelengths. The AB and ST magnitude systems are
  based on constant flux per unit frequency and per unit wavelength,
  respectively.  The zero points for these two systems are set for
  convenience so that Vega has magnitude 0 in both systems for the
  Johnson V passband.
  </dd>
  </dl>
  <dl>
  <dt><b>(magform = <span style="font-family: monospace;">"vegamag"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(magform = "vegamag") [string]' -->
  <dd>Form of the magnitude units. The definition of the units is the same
  as those given above for parameter 'form'.
  </dd>
  </dl>
  <dl>
  <dt><b>(wavecat = <span style="font-family: monospace;">"crmodewave$wavecat.dat"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wavecat = "crmodewave$wavecat.dat") [string]' -->
  <dd>The name of the wavelength catalog. The catalog is a table with two
  columns. The first column contains an observation mode string and the
  second contains a wavelength table name. This task reads the
  wavelength catalog and searches for the observation mode that best
  matches the input observation mode (constructed from task parameters)
  it then uses the wavelength table to resample the spectrum on the
  wavelength grid of the detector.  If the wavelength catalog is an
  ST4GEM table, the observation mode column must be named OBSMODE and
  the wavelength table column must be named FILE. If the wavelength
  catalog is a text table, the observation mode column and the
  wavelength table columns are the first and second columns,
  respectively.
  </dd>
  </dl>
  <dl>
  <dt><b>(refwave = INDEF) [real] [min = 1.0, max = 200000.]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(refwave = INDEF) [real] [min = 1.0, max = 200000.]' -->
  <dd>The reference wavelength in the spectrum. If this parameter is not
  INDEF, the output will contain the flux at this wavelength.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>Write calculated quantities to STDOUT?
  </dd>
  </dl>
  <dl>
  <dt><b>(flux_tot = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(flux_tot = INDEF) [real]' -->
  <dd>The integrated flux combination of observation mode and passband. This
  is an output parameter, the user should not supply a value.
  </dd>
  </dl>
  <dl>
  <dt><b>(flux_ref = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(flux_ref = INDEF) [real]' -->
  <dd>The flux at the reference wavelenth. This parameter will be set to
  INDEF if 'refwave' is set to INDEF. This is an output parameter, the
  user should not supply a value.
  </dd>
  </dl>
  <dl>
  <dt><b>(refdata = <span style="font-family: monospace;">" "</span>) [pset name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(refdata = " ") [pset name]' -->
  <dd>A parameter set containing the HST telescope area, the name of the HST
  graph table, and the name of the component lookup table. These
  parameters have been placed in a pset because they are common to most
  of the tasks in this package.
  </dd>
  </dl>
  </section>
  <section id="s_examples_">
  <h3>Examples </h3>
  <p>
  1. Compute the results of a 100 second observation of a 17th
  magnitude G0V star using the HRS with the large science aperture
  ('lsa') and the G270M grating. Store the result in table 'hrsobs.fits':
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; countrate.spectrum = "crgrid$bpgs/bpgs_36.fits"
  sy&gt; countrate.magnitude = "17 v"
  sy&gt; countrate.instrument = "hrs"
  sy&gt; countrate.spec_elem = "g270m"
  sy&gt; countrate.aperture = "lsa"
  sy&gt; countrate.cenwave = 2700.
  sy&gt; countrate.exptime = 100.
  sy&gt; countrate.output = "hrsobs.fits"
  sy&gt; countrate mode=h
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by B.Simon based on XCAL code written by Keith Horne
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  calcphot, calcspec
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES ' 'REFERENCES' 'SEE ALSO'  -->
  

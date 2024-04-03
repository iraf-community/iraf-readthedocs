.. _thermback:

thermback: Evaluate thermal background count rate for an observing mode.
========================================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  thermback obsmode
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task computes the predicted thermal background flux for a specified 
  telescope observing mode. At the user's option, it can also create
  an output spectrum containing the flux as a function of
  wavelength. The observing mode of the HST is specified in several task
  parameters.  These are 'instrument', 'detector', 'spec_elem', and
  'aperture'. The instrument must always be specified, but the other
  three parameters may be blank, depending on which instrument and
  instrument configuration is used. More than one observing mode keyword may
   be specified in
  a task parameter by separating the keywords with a comma. The obsmode
  task has more information on the legal observing mode keywords.
  </p>
  <p>
  The feature described in this paragraph Thermback extends the usual obsmode to permit the user to optionally specify 
  a temperature associated with any component in the optical chain. For example,
  if the usual obsmode is <span style="font-family: monospace;">"nicmos, 2, f222m"</span>, one can override the default 
  temperature of the primary mirror to 300K with <span style="font-family: monospace;">"nicmos, 2, f222m, primary#300"</span>. (But see Bugs, below.)
  Legal names for specifying the components are contained in the THLMODE keyword
  of the component emissivity file.  
  </p>
  <p>
  At present, CDBS only contains thermal related data files for the NICMOS instrument. Thermback will generate the error <span style="font-family: monospace;">"Component names not found in lookup table"</span> for unsupported instruments.
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
  <dl id="l_obsmode">
  <dt><b>obsmode [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obsmode' Line='obsmode [string]' -->
  <dd>The full specification of the observing mode, with optional per-component temperature overrides.
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
  parameters GRFTABLE, OCMPTBL, TCMPTBL, and OBSMODE. These
  will contain the name of the graph table, the optical component lookup table,
  the thermal component lookup table, and the observation mode.
  </dd>
  </dl>
  <dl>
  <dt><b>(tcmptb = <span style="font-family: monospace;">"mtab$*_tmt.fits"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(tcmptb = "mtab$*_tmt.fits") [string]' -->
  <dd>The name of the thermal lookup table. This table is analogous to 
  refdata.cmptbl: it translates the thermal component names in the graph table
  to the filenames containing the emissivity tables and other relevant data for
  the component.
  </dd>
  </dl>
  <dl>
  <dt><b>(detcat = <span style="font-family: monospace;">"synphot$simulators/data/detectors.dat"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(detcat = "synphot$simulators/data/detectors.dat") [string]' -->
  <dd>The name of a file containing detector properties, including the pixel scale.
  </dd>
  </dl>
  <dl>
  <dt><b>(wavetab = <span style="font-family: monospace;">"crmodewave$wavecat.dat"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wavetab = "crmodewave$wavecat.dat") [string]' -->
  <dd>The name of the wavelength table over which to perform the calculation.
   If blank, synphot will compute a 
  wavelength table that matches the specified obsmode.
  The catalog is a table with two
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
  <dt><b>(verbose = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = no) [boolean]' -->
  <dd>If yes, Thermback will write detailed information including a calculation of the thermal background rate at each component in the optical train.
  </dd>
  </dl>
  <dl>
  <dt><b>(form = <span style="font-family: monospace;">"counts"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(form = "counts") [string]' -->
  <dd>Desired output form for the calculation. The standard set of synphot forms 
  are recognized :
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
  <dt><b>(thermflux = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(thermflux = INDEF) [real]' -->
  <dd>An output parameter containing the calculated thermal flux per pixel in 
  the units specified by <span style="font-family: monospace;">"form"</span>.
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
  1. Compute the thermal background rate for the NICMOS 2 camera using the f222m filter. Store the result in table 'nic2def.fits':
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; thermback.obsmode = "nicmos, 2, f222m"
  sy&gt; thermback.output = "nic2def.fits"
  sy&gt; thermback
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  There is a sporadic bug that may manifest when the temperature override 
  option is used, that causes the program to crash. This appears to be a memory
  problem. Since the cause of the problem is not well understood, use caution
  in relying on results generated with the temperature override parameter.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by V. Laidler based on work by A. Sivaramakrishnan
  SEE ALSO
  synphot opt=sys and refdata for more details of the graph and component tables.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES ' 'BUGS' 'REFERENCES'  -->
  

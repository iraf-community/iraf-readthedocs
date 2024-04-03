.. _plratio:

plratio: Plot the ratio of observed to synthetic spectral or
============================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  plratio obsmode spectrum form spfile
  </p>
  </section>
  <section id="s_description_">
  <h3>Description </h3>
  <p>
  This task will calculate and plot the ratio of observed
  spectrophotometric data to a synthetic HST spectrum.  It also
  optionally plots the ratios of photometric observations to the
  synthetic photometry computed from the synthetic HST spectrum. This
  task produces plots similar to those produced by plspec, except that
  it plots ratios of the observed data (the spectrophotometric and
  photometric tables) to the predicted data (the combination of obsmode
  and spectrum) instead of plotting the data themeselves. The task also
  plots chi quared error of the fit, and the bias and root mean squared
  errors in magnitudes.
  </p>
  <p>
  Spectrophotometric ratios are plotted as histograms if the form is
  counts or obmag and as continuous curves if the form is
  not. Photometric ratios are plotted as horizontal lines whose
  midpoints are marked by a circle. The horizontal line has its x value
  set to the pivot wavelength of the observation mode passband and its y
  value set to the ratio of the effective stimulus taken from the
  photometric table to the effective stimulus calculated from the
  spectrum and obsmode. The length of the line is set to the full width
  half maximum of the equivalent gaussian of the observation mode
  passband. The observation mode passbands are overplotted at the base
  of the plot.
  </p>
  <p>
  Which plots are produced are controlled by the task parameters 'spfile'
  and 'pfile'. If spectophotometric ratios are not desired, 'spfile'
  should be set to <span style="font-family: monospace;">"none"</span> or left blank. If photometric ratios are not
  desired, 'pfile' should be set to <span style="font-family: monospace;">"none"</span> or left blank.
  Spectrophotometric ratios are computed for every combination of
  synthetic spectra and spectrophotometric files. Synthetic spectra are
  matched to rows in the photometic table by matching the obsmode and
  spectrum parameters to the OBSMODE and TARGETID columns in the
  photometric table. The strings must be exactly the same in order to
  make the match.
  </p>
  <p>
  The obsmode string may be set to <span style="font-family: monospace;">"none"</span>. In this case, the task uses
  an observation mode that is one over the wavelength set of the
  spectrum. If photometric errors are being computed, however, the form
  must be set to counts or obmag, because otherwise the task cannot
  compute the effective stimulus of the synthetic spectrum.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_obsmode">
  <dt><b>obsmode [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obsmode' Line='obsmode [string]' -->
  <dd>This is a sequence of commands that creates the synthetic passband.
  The name of a command file can be passed to 'obsmode' by preceding the
  file name with a <span style="font-family: monospace;">"@"</span> character, for example, <span style="font-family: monospace;">"@filename"</span>.
  Each command may either be a simple bandpass, which is represented by
  a comma separated string of keywords uniquely specifying an observing
  mode of the telescope or a more complex command, described in the help
  file for 'calcband'. The keywords which make up the observing mode are
  explained further in the obsmode task. If this parameter is left blank
  or set to <span style="font-family: monospace;">"none"</span>, a default observation mode that is everywhere one
  will be used.
  </dd>
  </dl>
  <dl id="l_spectrum">
  <dt><b>spectrum [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectrum' Line='spectrum [string]' -->
  <dd>This is a sequence of commands that create the synthetic spectrum.
  The commands can be placed in a file, whose name is passed to this
  parameter, preceded by a <span style="font-family: monospace;">"@"</span> character, e.g., '@filename'. Each line
  in this command file is treated as a separate set of commands. If this
  parameter is left blank or set to none, no spectra will be plotted.
  The commands that can be passed to this parameter are described in
  detail in the help file for the 'calcspec' task.
  </dd>
  </dl>
  <dl id="l_form">
  <dt><b>form [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='form' Line='form [string]' -->
  <dd>Desired output form. The following forms are recognized:
  <div class="highlight-default-notranslate"><pre>
  
  FNU             erg / s / cm^2 / Hz
  FLAM            erg / s / cm^2 / A
  PHOTNU          photons / s / cm^2 / Hz
  PHOTLAM         photons / s / cm^2 / A
  COUNTS          photons / s
  ABMAG           -2.5 log_10 (FNU)  - 48.60
  STMAG           -2.5 log_10 (FLAM) - 21.10
  VEGAMAG         -2.5 log_10 (F/F_vega)
  OBMAG           -2.5 log_10 (COUNTS)
  JY              10^-23 erg / s / cm^2 / Hz
  MJY             10^-26 erg / s / cm^2 / Hz
  
  </pre></div>
  A standard magnitude system is VEGAMAG, for which Vega by definition
  has magnitude 0 at all wavelengths. The AB and ST magnitude systems are
  based on constant flux per unit frequency and per unit wavelength,
  respectively.  The zero points for these two systems are set for
  convenience so that Vega has magnitude 0 in both systems for the
  Johnson V passband.
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
  <dl id="l_spfile">
  <dt><b>spfile [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spfile' Line='spfile [file name]' -->
  <dd>A table or ascii file containing spectrophotometry data; a list of one
  or more files can be specified using the <span style="font-family: monospace;">"@filename"</span> syntax.  If the
  value of this parameter is set to <span style="font-family: monospace;">"none"</span> or blank, the ratio of the
  spectrophotometric data to the theoretical spectra will not be
  plotted. In this case, the 'pfile' parameter should have a value other
  than <span style="font-family: monospace;">"none"</span>. The spectrophotometric table can have the columns
  WAVELENGTH, FLUX, STATERROR, and FWHM.  The STATERROR and FWHM columns
  can be missing or all INDEF. The WAVENGTH and FLUX columns contain the
  wavelength and values of flux at that wavelength, respectively. The
  STATERROR and FWHM collumns contain the respective errors of the FLUX
  and WAVELENGTH columns. If the spectrophotometry file is an ascii
  file, the first through fourth columns are the wavelength, flux,
  staterror, and flux and the third and fourth columns are optional.
  </dd>
  </dl>
  <dl>
  <dt><b>(pfile = <span style="font-family: monospace;">"none"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(pfile = "none") [string]' -->
  <dd>A file containing photometric data, generated by the calcphot task. A
  list of files can be passed as <span style="font-family: monospace;">"@filename"</span>.  If the value of this
  parameter is <span style="font-family: monospace;">"none"</span> or blank, the ratio of the photometric data to the
  photometric data generated from the synthtic spectra will not be
  plotted. A table generated by calcphot will have column names DATUM,
  FORM, OBSMODE and TARGETID.  These columns contain the effective
  stimulus, its form, the observation mode, and spectrum passed to
  calcphot. If the photometric file is an ascii file, the file will have
  four columns in the order specified above. This task matches the
  photometic data to the data generated from the spectra by the strings
  in the OBSMODE and TARGETID columns.
  </dd>
  </dl>
  <dl>
  <dt><b>(left = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(left = INDEF) [real]' -->
  <dd>Minimum wavelength to plot. If set to INDEF, the task will set it to
  the minimum wavelength in the wavelength set.
  </dd>
  </dl>
  <dl>
  <dt><b>(right = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(right = INDEF) [real]' -->
  <dd>Maximum wavelength to plot. If set to INDEF, the task will set it to
  the maximum wavelength in the wavelength set.
  </dd>
  </dl>
  <dl>
  <dt><b>(bottom = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(bottom = INDEF) [real]' -->
  <dd>Minimum flux value to plot. If set to INDEF, the task will set it
  to the minimum value of the ratios.
  </dd>
  </dl>
  <dl>
  <dt><b>(top = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(top = INDEF) [real]' -->
  <dd>Maximum flux value to plot. If set to INDEF, the task will set it
  to the maximum value of the ratios.
  </dd>
  </dl>
  <dl>
  <dt><b>(append = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(append = no) [boolean]' -->
  <dd>Append results to an existing plot? 
  </dd>
  </dl>
  <dl>
  <dt><b>(ltype = <span style="font-family: monospace;">"solid"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ltype = "solid") [string]' -->
  <dd>The line type to be used for plotting the mode1 passband.  The allowed
  values are: clear, solid, dashed, dotted, and dotdash.
  </dd>
  </dl>
  <dl>
  <dt><b>(device = <span style="font-family: monospace;">"stdgraph"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(device = "stdgraph") [string]' -->
  <dd>Send output to the designated device.
  </dd>
  </dl>
  <dl>
  <dt><b>(wavetab = <span style="font-family: monospace;">""</span>) [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wavetab = "") [file name]' -->
  <dd>Name of an optional wavelength table or file. An appropriate table can
  be generated by using the 'genwave' task. If a table is used, the
  wavelength column name must be <span style="font-family: monospace;">"WAVELENGTH"</span>. If an ASCII file is used
  the first column is taken to be the wavelength column.  The
  subdirectory 'synphot$data has ASCII wavelength tables useful for
  specific HST passbands.  
  If no wavelength table is specified, the task generates a wavelength
  set which covers the range between the left and right plot limits. If
  there is no wavelength table, and plot limits are not specified, a
  default wavelength set is used. The default wavelength set covers the
  wavelength range where the spectrum is non-zero. Wavelengths are
  spaced logarithmically over this range. If more than one spectrum is
  plotted, the range is computed based on the first spectrum. If the
  wavelength range of the spectra differ significantly, a wavelength
  table should be specified explicitly or plot limits should be set.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl>
  <dt><b>(refdata = <span style="font-family: monospace;">" "</span>) [pset name]</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='' Line='(refdata = " ") [pset name]' -->
  <dd><p>
  Parameter set for reference data used in calculations.  The following 
  parameters are stored in this set.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  area = 45238.93416:  HST telescope area in cm**2.
  
  grtbl = "mtab$*.tmg":  HST graph table.  Uses the
            most recent version by default.
  
  cmptbl = "mtab$*.tmc":  Instrument component table.
             The most recent version is used by default.
  
  </pre></div>
  </dd>
  </dl>
  <dl>
  <dt><b>(device = <span style="font-family: monospace;">"stdgraph"</span>) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='' Line='(device = "stdgraph") [real]' -->
  <dd><p>
  Send output to the designated device.
  <span style="font-family: monospace;">"stdgraph"</span> plots to the screen, <span style="font-family: monospace;">"stdplot"</span> sends output to your
  default laser printer.
  </dd>
  </dl>
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  1.  Calculate the ratio of a 15000 K blackbody spectrum to that of Vega.
  We first renormalize the blackbody spectrum to have magnitude 0 in the
  V passband (to match the absolute flux level of Vega).  The ratio is
  plotted in units of flam.
  <div class="highlight-default-notranslate"><pre>
  sy&gt; plratio none "rn(bb(15000),band(v),0,vegamag)" flam \
  &gt;&gt;&gt; crcalspec$alpha_lyr_stis_002.fits
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  Written by B.Simon based on XCAL code written by Keith Horne
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  plspec
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION ' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

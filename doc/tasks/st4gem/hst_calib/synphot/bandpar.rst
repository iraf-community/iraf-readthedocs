.. _bandpar:

bandpar: Calculate photometric parameters of a passband
=======================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  bandpar obsmode
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task computes the photometric parameters of a passband. The
  passband can either be read from a file, calculated as the combined
  throughputs of the individual HST components, or calculated from
  certain functional forms, such as a Gaussian or a rectangular window.
  The passband is specified by an expression in the 'obsmode' task
  parameter. See the help file for calcband for a description of the
  syntax of this expression.
  </p>
  <p>
  This task computes eleven different photometric parameters. These are:
  </p>
  <div class="highlight-default-notranslate"><pre>
   NAME           PARAMETER
  =======         =========
  URESP           Flux (in flam) of a star that produces a response
                  of one photon per second in this passband
  PIVWV           Passband pivot wavelength
  BANDW           Passband rms width
  FWHM            Full width half max of equivalent gaussian
  WPEAK           Wavelength at peak throughput
  TPEAK           Peak bandpass throughput
  AVGLAM          Passband average wavelength
  QTLAM           Dimensionless efficiency
  EQUVW           Passband equivalent width
  RECTW           Passband rectangular width
  EMFLX           Equivalent monochromatic flux
  
  </pre></div>
  <p>
  In addition to computing these photometric parameters,  this task
  computes two parameters used in the computation of the equivalent
  monochromatic flux:
  </p>
  <div class="highlight-default-notranslate"><pre>
   NAME           PARAMETER
  =======         =========
  REFWAVE         The reference wavelength
  TLAMBDA         The throughput at the reference wavelength
  </pre></div>
  <p>
  Unless specified by the user, the reference wavelength is set to the
  average wavelength of the passband (AVGWV). The photometric
  parameters are defined by the equations:
  </p>
  <div class="highlight-default-notranslate"><pre>
  URESP = H * C / (AREA * INT(THRU * LAM))
  
  PIVWV = SQRT(INT(THRU * LAM) / INT (THRU / LAM))
  
  BANDW = BARLAM * SQRT(INT(THRU * LN(LAM / BARLAM) ** 2 / LAM) /
                        INT(THRU / LAM)
  
  FWHM = SQRT(8 * LOG(2)) * BANDW
  
  BARLAM = INT(THRU * LN(LAM) / LAM) / INT(THRU / LAM)
  
  TPEAK = MAX(THRU)
  
  AVGWV = INT(THRU * LAM) / INT(THRU)
  
  QTLAM = INT(THRU / LAM)
  
  EQUVW = INT(THRU)
  
  RECTW = INT(THRU) / MAX(THRU)
  
  EMFLX = URESP * RECTW * (TPEAK / TLAMBDA)
  
  </pre></div>
  <p>
  In these formulas, INT() denotes the integral with repect to lambda,
  SQRT() denotes square root, LN() the natural logarithm, LOG() the
  common logairthm, and MAX() the maximum function. The variable LAM is
  wavelength, THRU is the total throughput, which is a function of
  wavelength, AREA is the telescope area, and H and C are the usual
  physical constants.
  </p>
  <p>
  The photometric parameters are printed on STDOUT and optionally saved in a
  table. Which parameters are printed and saved is controlled by the
  hidden parameter 'photlist'. By default, all parameters will be
  printed. 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_obsmode">
  <dt><b>obsmode [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obsmode' Line='obsmode [string]' -->
  <dd>The command the specifies the synthetic passband. The command syntax
  is described in the help file for calcband. The photometric parameters
  of more than one passband can be computed by putting the commands in a
  file, one per line, and setting 'obsmode' to the name of the file
  preceded by an <span style="font-family: monospace;">"@"</span> character, e.g. <span style="font-family: monospace;">"@filename"</span>. The keywords which
  form an obsmode are explained further in the obsmode task.
  </dd>
  </dl>
  <dl>
  <dt><b>(output = <span style="font-family: monospace;">"none"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(output = "none") [string]' -->
  <dd>The name of the output table containing the photometric parameters. If
  this parameter is set to <span style="font-family: monospace;">"none"</span> or left blank, no output table will be
  created. But output will still be sent to STDOUT regardless of
  the value of this parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>(photlist = <span style="font-family: monospace;">"all"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(photlist = "all") [string]' -->
  <dd>A comma separated list of the photometric parameters to print. The
  value <span style="font-family: monospace;">"all"</span> prints all the photometric parameters. Placing a <span style="font-family: monospace;">"~"</span> in
  front of the list causes all the parameters except the named
  parameters to be printed. The two auxiliary parameters REFWAVE and
  TLAMBDA are printed by default if EMFLX is printed and not printed by
  default if EMFLX is not printed.
  </dd>
  </dl>
  <dl>
  <dt><b>(refwave = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(refwave = INDEF) [real]' -->
  <dd>The reference wavelength used in the computation of EMFLX. If this
  parameter is set to INDEF, the average wavelength (AVGWAV) will be
  calculated and used in its place. The units of the wavelength must be
  angstroms. 
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
  set which covers the range where the passband is non-zero. Wavelengths
  are spaced logarithmically over this range. If there is more than one
  passband, the range is computed based on all the passbands.
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
          uses the more recent version.
  
  cmptbl = "mtab$*.tmc":  Instrument component table.  By
          default, this uses the more recent version.
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Calculate the photometric parameters for the wfpc and f555w filter.
  </p>
  <p>
  sy&gt; bandpar wfpc,f555w
  </p>
  <p>
  2. Calculate the pivot wavelength and rms bandwidth for each of the
  Johnson passbands.
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; bandpar @ubvri.lis output=johnson.tab phot=pivwv,bandw
  </pre></div>
  <p>
  The file ubvri.lis contains the lines:
  </p>
  <div class="highlight-default-notranslate"><pre>
  band(u)
  band(b)
  band(v)
  band(r)
  band(i)
  </pre></div>
  <p>
  3. Calculate the photometric parameters for the wfpc and the f555w
  filter, setting the reference wavelength to 5500 angstroms. Don't
  print the reference wavelength.
  </p>
  <p>
  sy&gt; bandpar wfpc,f555w refwave=5500 phot=~refwave
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by B.Simon 
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  calcband
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

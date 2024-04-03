.. _calcband:

calcband: Calculate a model passband.
=====================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  calcband obsmode output
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task will create a synthetic passband by combining existing
  passbands, certain functional forms such as a Gaussian or a
  rectangular window, or externally created passbands read in from a
  file.  These data can be multiplied by a function of Legendre
  polynomials to distort the shape, as appropriate.  
  </p>
  <p>
  This task uses the same back end as calcspec, including the expression
  evaluator. This help file only discusses those functions most relevant
  to computing passbands, but the full range of functions described in
  the help file for calcspec can be used. The reson for supplying a
  separate front end to handle passbands is that some of the task
  parameters to calcspec, such as 'form' are not relevant to calcband.
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
  The command interpreter supports addition (+), subtraction (-),
  multiplication (*), division (/), and negation (-). The division
  operator should be surrounded by blanks to keep from being interpreted
  as part of a file name. Operator precedence and associativity is the
  same as Fortran. Precedence can be changed by enclosing subexpressions
  in parentheses. The terms which are operated on are either passband
  files, numeric constants, or functions. As a convenience to users, if
  the expression consists of a single call to the band() function, only
  the arguments to the function need be given. For example, the obsmode
  <span style="font-family: monospace;">"band(wfpc,f555w)"</span> can also be given as <span style="font-family: monospace;">"wfpc,f555w"</span>. The arguments to
  the band() function are explained further in the obsmode task.
  The interpreter supports several functions which return passbands:
  band(), which returns a passband corresponding to an hst observing
  mode, box(), which returns a box passband, gauss() and lgauss(), which
  return gaussian and log gaussian passbands, and poly() and tilt(),
  which return Legendre polynomial passbands. In addition, the thru()
  function can be used to specify the name of an ASCII file from which
  to read the passband data. The following is a more
  detailed description of these functions:
  <div class="highlight-default-notranslate"><pre>
  band(str1, ...)
  str1:   observation mode keyword
  
  A passband associated with a telescope observing mode. The observing
  mode is specified by the arguments to the function. The combination of
  the arguments should uniquely specify an observing mode.to this
  
  box(num1, num2)
  num1:   passband center
  num2:   passband width
  
  A passband that is one inside the specified region and zero outside.
  
  gauss(num1, num2)
  num1:   mean of normal distribution
  num2:   full width half maximum of distribution
  
  A passband with normal distribution. The full width half maximum is
  sqrt(8 * ln(2)) times the standard deviation.
  
  lgauss(num1, num2)
  num1:   mean of distribution
  num2:   full width half maximum of distribution
  
  A passband with normal distribution in the logarithm of the
  wavelength.
  
  poly(num1, num2, num3, ...)
  num1:   mean of polynomial
  num2:   full width half maximum
  num3:   polynomial coefficient
  
  A passband which is a function of legendre polynomials. First, sigma
  is computed from the full width half maximum using the formula:
          sigma = fwhm / sqrt (8 * ln(2))
  Then the independent variable is transformed from wavelength with the
  formula:
          u = (wave - mean) / sigma
  The sum of the legendre polynomials is computed with the formula
          sum = SUM[ coef_n * legendre_n (u)]
  The final passband is given by the formula
          band = sum + 1 if sum &gt;= 0
          band = exp (sum) if sum &lt; 0
  
  thru(str1)
  str1: Name of an ASCII file containing columns of wavelength and
  throughput data.
  
  tilt(band1, num1, ...)
  band1:  passband from which mean and fwhm are computed
  num1:   polynomial coefficient
  
  A passband similar to that produced by poly(), except that the mean
  and full width half maximum are computed from the wavelength.
  </pre></div>
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name]' -->
  <dd>Name of the ST4GEM table to be used as output.  The table has two
  columns, 'WAVELENGTH' and 'THROUGHPUT'. If more than one passband is
  specified via a file, then a separate 'THROUGHPUTn' column will be
  created for the nth passband listed in a file.
  The output table contains the following header keywords:
  <div class="highlight-default-notranslate"><pre>
  
  KEYWORD         PARAMETER
  =======         =========
  GRFTABLE        Name of the instrument graph table.
  CMPTABLE        Name of the component lookup table.
  APERAREA        The HST area, in cm^2, used to compute URESP.
  ZEROPT          Photometric zero point of the STMAG system.
  EXPR            Value of spectrum parameter
  URESP           Flux (in flam) of a star that produces a response
                  of one photon per second in this passband.
  PIVWV           Passband pivot wavelength.
  BANDW           Passband rms width.
  TPEAK           Peak bandpass throughput
  EQUVW           Passband equivalent width
  RECTW           Passband rectangular width
  EMFLX           Equivalent monochromatic flux
  
  </pre></div>
  If more than one passband is input via a file, the last eight header
  keywords will be included once for each passband, with the names
  EXPRn, URESPn, PIVWVn, BANDWn, TPEAKn, EQUVWn, RECTWn, and EMFLXn for
  the nth passband.
  The seven photometric passbands are defined by the following formulas:
  <div class="highlight-default-notranslate"><pre>
  URESP = H * C / (AREA * INT(THRU * LAM))
  
  PIVWV = SQRT(INT(THRU * LAM) / INT (THRU / LAM))
  
  BANDW = BARLAM * SQRT(INT(THRU * LN(LAM / BARLAM) ** 2 / LAM) /
                        INT(THRU / LAM)
  BARLAM = INT(THRU * LN(LAM) / LAM) / INT(THRU / LAM)
  
  TPEAK = MAX(THRU)
  
  EQUVW = INT(THRU)
  
  RECTW = INT(THRU) / MAX(THRU)
  
  EMFLX = URESP * RECTW * (TPEAK / TLAMBDA)
  TLAMBDA = Throughput at AVGWAV
  AVGWAV = INT(THRU * LAM) / INT(THRU)
  
  </pre></div>
  In these fromulas, INT() denotes the integral with repect to lambda,
  SQRT() denotes square root, LN() the natural logarithm, and MAX() the
  maximum function. The variable LAM is wavelength, THRU is the total
  throughput, which is a function of wavelength, AREA is the telescope
  area, and H and C are the usual physical constants.
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
  If no wavelength table is specified, a default wavelength set is
  used. The default wavelength table covers the wavelength range where
  the passband is non-zero. Wavelengths are spaced logarithmically over
  this range. If there is more than one passband, the range is computed
  based on the first passband. If the wavelength range of the spectra
  differ significantly, a wavelength table should be specified
  explicitly.
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
          uses the most recent version.
  
  cmptbl = "mtab$*.tmc"  Instrument component table.  By
          default, this uses the most recent version.
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Calculate the combined instrumental throughput of the HRS using the
  large science aperture (lsa) and the G270M grating.  Store the throughput
  data in a table called 'hrs.tab'.
  </p>
  <p>
  sy&gt; calcband <span style="font-family: monospace;">"band(hrs,lsa,g270m)"</span> hrs
  </p>
  <p>
  2. The following command computes the same combined throughput using
  the abbreviated form of the obsmode string.
  </p>
  <p>
  sy&gt; calcband <span style="font-family: monospace;">"hrs,lsa,g270m"</span> hrs
  </p>
  <p>
  3. Create a Gaussian passband, multiplied by a first-order Legendre polynomial
  and write the results to a table called 'gauss_tilt.tab'.
  </p>
  <p>
  sy&gt; calcband <span style="font-family: monospace;">"tilt(gauss(4800,1300),10)"</span> gauss_tilt
  </p>
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
  plband, calcspec
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

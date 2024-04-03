.. _calcspec:

calcspec: Calculate a model spectrum.
=====================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  calcspec spectrum output
  </p>
  </section>
  <section id="s_description_">
  <h3>Description </h3>
  <p>
  This task writes a synthetic spectrum to a file. Several functions are
  available for creating synthetic spectra. Spectra can also be read
  from files.  Calcspec supports the four basic functions plus negation.
  Expressions can be parenthesized to change the default order of
  evaluation. Spaces are not significant, except for the division
  operator, which must be surrounded by blanks so that it will not be
  mistaken for part of a filename.  Calcspec evaluates expressions
  containing filenames, constants, and variables. When calcspec sees a
  filename, it determines if the file is a passband or a spectrum and
  reads it interpolated on the wavelength grid. Constants are either
  numbers or strings. String constants are NOT surrounded by quote
  marks. Numeric constants are interpreted as real numbers and all
  mathematical operations between filenames and constants are legal.
  </p>
  <p>
  Calcspec prevents physically meaningless expressions from being
  computed by keeping track of the degree of the expression during
  computation.  The degree of the entire expression must be zero or
  one. If the degree of the expression is zero, the result of calcspec
  is a passband. If it is one, the result is a spectrum. Although
  calcspec is primarily intended for producing spectra, it can also to
  compute passbands. 
  </p>
  <p>
  The degree of the entire expression is computed from the
  subexpressions that make it up. Constants and passbands have a degree
  of zero.  Spectra have a degree of one. Each function also has a
  degree, which is either zero or one. Multiplying two subexpressions
  yields a result whose degree is the sum of the degrees of the two
  subexpressions.  Dividing two subexpressions yields a result whose
  degree is the difference between the degrees of the two
  subexpressions. Adding or subtracting two subexpressions yields a
  result whose degree is the same as the degrees of both
  subexpressions. Adding or subtracting two subexpressions whose degrees
  are different is forbidden and causes an error exit. Negation gives a
  result whose degree is the same as the subexpression.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_spectrum">
  <dt><b>spectrum [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectrum' Line='spectrum [string]' -->
  <dd>This is a sequence of commands and arguments that specify the synthetic
  spectrum.  The commands can be placed in a file, whose name is passed to 
  this parameter, preceded by a <span style="font-family: monospace;">"@"</span> character, e.g., '@filename'. Each
  line in such a command file is treated as a separate set of commands.
  Calcspec supports a variety of different functions. The following
  table lists these functions, their degree, amd their arguments. The
  name of the arguments indicate the argument type: NUM for numeric
  constants, STR for string constants, BAND for passbands, and SPEC for
  spectra. Ellipsis marks indicate that an indefinite number of
  arguments of the same type as the last explicitly stated argument may
  be included in the function.
  <div class="highlight-default-notranslate"><pre>
  FUNCTION                        DEG     DESCRIPTION
  ----------------------------------------------------------------------
  band(str1, ...)                 0       Telescope passband
  bb(num1)                        1       Black body spectrum
  box(num1, num2)                 0       Rectangular passband
  cat(str1, ...)                  1       Read from a catalog of spectra
  ebmv(num1)                      0       Galactic extinction curve
  ebmvx(num1, str1)               0       Other extinction curves
  em(num1, num2, num3, str1)      1       Emission line spectrum
  gauss(num1, num2)               0       Normal curve passband
  grid (str1, num1)               1       Interpolated spectrum in grid
  hi(num1, num2)                  1       Hydrogen absorption spectrum
  icat(str1, ...)                 1       Interpolate in a catalog of spectra
  lgauss(num1, num2)              0       Log normal curve passband
  pl(num1, num2, str1)            1       Power law spectrum
  poly(num1, num2, num3, ...)     0       Legendre polynomial
  rn(spec1, band1, num1, str1)    1       Renormalize spectrum
  spec(str1)                      1       Read a spectrum from a file
  thru(str1)                      0       Read a passband from a file
  tilt(band1, num1, ...)          0       Legendre polynomial product
  unit(num1, str1)                1       Constant spectrum
  z(spec1, num1)                  1       Redshift spectrum
  </pre></div>
  The following is a more detailed description of each of the functions.
  <div class="highlight-default-notranslate"><pre>
  band(str1, ...)
  str1:   observation mode keyword
  </pre></div>
  A passband associated with a telescope observing mode. The observing
  mode is specified by the arguments to the function. The combination of
  the arguments should uniquely specify an observing mode. The arguments
  to the band() function are explained further in the obsmode task.
  <div class="highlight-default-notranslate"><pre>
  bb(num1)
  num1:   temperature in Kelvin
  </pre></div>
  A black body spectrum normalized in flux to be equal to a one solar
  radius star at a distance of one kiloparsec.
  <div class="highlight-default-notranslate"><pre>
  box(num1, num2)
  num1:   passband center
  num2:   passband width
  </pre></div>
  A passband that is one inside the specified region and zero outside.
  <div class="highlight-default-notranslate"><pre>
  cat(str1, str2, ...)
  str1: catalog name
  str2: search key
  </pre></div>
  A spectrum selected from a catalog of spectra. The first argument
  specifies the catalog name and the remaining arguments specify the
  spectrum within the catalog. The catalog name must be a subdirectory
  of crgrid$. This directory contains a file named catalog.tab that is
  read by this function. The first column of the table, INDEX, contains
  a comma separated list of keywords used to select the row by matching
  the the second and following arguments of the function. String
  arguments must match exactly (except for case). If there are numeric
  arguments, the function will choose the spectrum with the minimum
  distance.
  <div class="highlight-default-notranslate"><pre>
  ebmv(num1)
  num1:   number of magnitudes of extinction
  </pre></div>
  Interstellar reddening function for our galaxy, according to Seaton's
  paper. This function is equivalent to using ebmvx() with the second
  argument set to gal1.
  <div class="highlight-default-notranslate"><pre>
  ebmvx(num1, str1)
  num1:   number of magnitudes of extinction
  str1:   extinction law used
  </pre></div>
  The extended reddening function, supporting a number of different
  reddening laws. The second argument selects the type of reddening law
  used to compute the extinction. The task supports three galactic
  reddening laws (gal1 to gal3) and one law each for the Small
  Magellanic Cloud (smc), Large Magellanic Cloud (lmc), and
  extra-galactic objects (xgal).  The laws are derived from the
  following papers.
  <div class="highlight-default-notranslate"><pre>
  gal1    Seaton (1979) MNRAS, vol 187, p. 75
  gal2    Savage &amp; Mathis (1979) ARA&amp;A, vol. 17, p. 73-111
  gal3    Cardelli, Clayton &amp; Mathis (1989) ApJ vol. 345, p. 245-256
  smc     Prevot et al. (1984) A&amp;A, vol. 132, p. 389-392
  lmc     Howarth (1983) MNRAS, vol. 203, p. 301
  xgal    Calzetti, Kinney and Storchi-Bergmann, (1994) ApJ, vol. 429, p.582
  </pre></div>
  <div class="highlight-default-notranslate"><pre>
  em(num1, num2, num3, str1)
  num1:   mean wavelength of emission line
  num2:   full width half maximum of emission line
  num3:   total flux in emission line
  str1:   flux units
  </pre></div>
  An emission line with a gaussian profile and specified flux. The
  emission line can be added to another spectrum or subtracted from it
  to create an absorption line.
  <div class="highlight-default-notranslate"><pre>
  gauss(num1, num2)
  num1:   mean of normal distribution
  num2:   full width half maximum of distribution
  </pre></div>
  A passband with normal distribution. The full width half maximum is
  sqrt(8 * ln(2)) times the standard deviation.
  <div class="highlight-default-notranslate"><pre>
  grid (str1, num1)
  str1:   ascii file containing a list of filenames
  num1:   point to interpolate at
  </pre></div>
  A spectrum interpolated in a grid of spectra. The second argument
  gives the interpolation point. For example, 2.3 interpolates .3 of the
  way between the second and third spectra.
  <div class="highlight-default-notranslate"><pre>
  hi(num1, num2)
  num1:   temperature in Kelvin
  num2:   column density in cm^-3
  </pre></div>
  An absorption spectrum for a black body embedded in hydrogen. If the
  column density is less than 80, it is assumed to be a logarithm of the
  column density. Flux is normalized to be equal to a one solar radius
  at one kiloparsec.
  <div class="highlight-default-notranslate"><pre>
  icat(str1, str2, ...)
  str1: catalog name
  str2: search key
  </pre></div>
  A spectrum selected from a catalog of spectra. The first argument
  specifies the catalog name and the remaining arguments specify the
  spectrum within the catalog. The catalog name must be a subdirectory
  of crgrid$. This directory contains a file named catalog.tab that is
  read by this function. The first column of the table, INDEX, contains
  a comma separated list of keywords used to select the row by matching
  the the second and following arguments of the function. String
  arguments must match exactly (except for case). If there are numeric
  arguments, the function will interpolate between spectra which bracket
  the arguments. If there is no complete bracket, the function will
  choose the spectrum with the minimum distance.
  <div class="highlight-default-notranslate"><pre>
  lgauss(num1, num2)
  num1:   mean of distribution
  num2:   full width half maximum of distribution
  </pre></div>
  A passband with normal distribution in the logarithm of the
  wavelength.
  <div class="highlight-default-notranslate"><pre>
  pl(num1, num2, str1)
  num1:   reference wavelength
  num2:   power law exponent
  str1:   flux units
  </pre></div>
  A power law spectrum. The flux is one at the reference wavelength in
  the specified units, unless the units are magnitude units, in which
  case the flux is zero in the specified units.
  <div class="highlight-default-notranslate"><pre>
  poly(num1, num2, num3, ...)
  num1:   mean of polynomial
  num2:   full width half maximum
  num3:   polynomial coefficient
  </pre></div>
  A passband which is a function of legendre polynomials. First, sigma
  is computed from the full width half maximum using the formula:
  	sigma = fwhm / sqrt (8 * ln(2))
  Then the independent variable is transformed from wavelength with the
  formula:  
  <div class="highlight-default-notranslate"><pre>
  u = (wave - mean) / sigma
  </pre></div>
  The sum of the legendre polynomials is computed with the formula
  <div class="highlight-default-notranslate"><pre>
  sum = SUM[ coef_n * legendre_n (u)]
  </pre></div>
  The final passband is given by the formula
  <div class="highlight-default-notranslate"><pre>
  band = sum + 1 if sum &gt;= 0
  band = exp (sum) if sum &lt; 0
  </pre></div>
  <div class="highlight-default-notranslate"><pre>
  rn(spec1, band1, num1, str1)
  spec1:  spectrum to be renormalized
  band1:  passband to normalize spectrum over
  num1:   flux of normalized spectrum
  str1:   flux units
  </pre></div>
  A spectrum normalized to a specified flux value when integrated over a
  specified passband.
  <div class="highlight-default-notranslate"><pre>
  spec(str1)
  str1:   spectrum filename
  </pre></div>
  Read a file as a spectrum. This function is intended for those cases
  where a filename might be interpreted as a number or contain
  arithmetic operators as characters. Otherwise, the filename can be
  placed in the expression without using this function.
  <div class="highlight-default-notranslate"><pre>
  thru(str1)
  str1:   passband filename
  </pre></div>
  Read a file as a passband. This function is intended for those cases
  where a passband file may be mistaken for a spectrum or may be
  interpreted as a number or contain arithmetic operators. Otherwise,
  the filename can be placed in the expression without using this
  function. ASCII files are assumed, by default, to contain spectral 
  data, so this function is particularly useful for forcing an ASCII file 
  to be interpreted as a passband.
  <div class="highlight-default-notranslate"><pre>
  tilt(band1, num1, ...)
  band1:  passband from which mean and fwhm are computed
  num1:   polynomial coefficient
  </pre></div>
  A passband similar to that produced by poly(), except that the mean
  and full width half maximum are computed from the wavelength.
  <div class="highlight-default-notranslate"><pre>
  unit(num1, str1)
  num1:   flux value
  str1:   flux units
  </pre></div>
  A constant spectrum with the specified value and units.
  <div class="highlight-default-notranslate"><pre>
  z(spec1, num1)
  spec1:  spectrum to be redshifted
  num1:   z value used in shift
  </pre></div>
  Redshift a spectrum by the z value given in the second argument.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [string]' -->
  <dd>Output ST4GEM table name. 
  This table has two columns, named
  'WAVELENGTH' and 'FLUX'. If more than one spectrum is specified via a
  file, then a separate 'FLUXn' column will be created for the nth
  spectrum listed in the file.
  The output table contains the following header keywords:
  <div class="highlight-default-notranslate"><pre>
  
  KEYWORD         PARAMETER
  =======         =========
  GRFTABLE        Name of the instrument graph table.
  CMPTABLE        Name of the component lookup table.
  EXPR            Value of spectrum parameter
  
  </pre></div>
  If more than one spectrum is input via a file, each will be listed as
  a header keyword, with the name EXPRn.
  The form of the output table is somewhat different if the result is
  passband. The form of an output table containing a passband is
  discussed in the help file for calcband.
  </dd>
  </dl>
  <dl>
  <dt><b>(form = photlam) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(form = photlam) [string]' -->
  <dd>Desired output form for the calculated spectrum. The form is ignored
  if the output is a passband. The following forms are recognized:
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
  the spectrum is non-zero. Wavelengths are spaced logarithmically over
  this range. If there is more than one spectrum, the range is computed
  based on the first spectrum. If the wavelength range of the spectra
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
  
  cmptbl = "mab$*.tmc":  Instrument component table.  By
          default, this uses the most recent version.
  
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Calculate a blackbody spectrum and renormalize it to have an integrated
  V band magnitude of 18.6.  Store the spectral data in an ST4GEM table
  called 'bb18p6.tab', in units of f-lambda.
  </p>
  <p>
  sy&gt; calcspec <span style="font-family: monospace;">"rn(bb(5000),band(v),18.6,vegamag)"</span> bb18p6 form=flam
  </p>
  <p>
  2. Simulate an observation of BD+75 325 using the FOS blue side with
  the 4.3 arcsec aperture and the G160l grating.  The spectral data for
  BD+75 325 are stored in the table 'bd75d325.tab' in units of STMAG 
  (unit conversion will be performed in real time by calcspec).
  Because this spectrum has been arbitrarily normalized
  in intensity, we must first renormalize it to its proper U magnitude
  of 9.5 and then multiply by the FOS instrument mode passband.
  The spectrum, in units of photlam (photons/sec/cm**2/A), will be stored 
  in table 'bd75.tab'.
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; calcspec "rn(bd75d325,band(u),9.5,vegamag)*band(fos,blue,4.3,g160l)" \
  &gt;&gt;&gt; bd75 form=photlam
  </pre></div>
  <p>
  3. A star observed using the wfpc with filter f555w is observed to
  have 1200 counts per second. What would its spectrum be for various
  assumed black body temperatures? Store the results in table bbody.tab
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; calcspec "rn(bb($0),band(wfpc,f555w),1200,counts)" bbody.tab \
  &gt;&gt;&gt; vzero="5e3-20e3x1e3"
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by B.Simon based on XCAL code written by Keith Horne.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  calcband, plband, plspec
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION ' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

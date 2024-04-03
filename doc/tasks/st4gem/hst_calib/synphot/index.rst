synphot: Tasks for synthetic photometry and modelling instrument response.
==========================================================================

.. toctree:: :maxdepth: 1

   bandpar
   calcband
   calcphot
   calcspec
   countrate
   fitband
   fitgrid
   fitspec
   genwave
   grafcheck
   graflist
   grafpath
   imspec
   mkthru
   obsmode
   plband
   plratio
   plspec
   pltrans
   refdata
   showfiles
   simulators/index
   thermback
.. raw:: html

  <p>
  The synphot package is modeled on Keith Horne's XCAL software, a suite
  of Fortran subroutines designed to be used as a dynamic throughput
  generator using files stored in the HST Calibration Data Base System
  (CDBS).  The need for such a tool arose from the realization that the
  HST observatory has such a vast number of iterrelated observing modes,
  it would be impractical and inefficient to derive and maintain an
  independent calibration for every possible instrument configuration.
  Rather than restrict calibrations to a smaller number of <span style="font-family: monospace;">"core"</span> modes,
  the alternative solution of a software tool with the capability to
  generate the throughput function for any HST observing mode was
  implemented.  Throughput functions and calibration data files for
  specific observing modes are generated dynamically, whenever they are
  needed.  This approach reduces to a manageable level the number of
  calibration data files that must be created and maintained, and
  ultimately saves considerable observing time, since information from
  calibration observations in one mode can be easily <span style="font-family: monospace;">"transferred"</span> to
  other closely related modes.
  </p>
  <p>
  The basic concepts, data structures, and software needed for dynamic
  throughput generation are discussed in detail by Horne, Burrows, and
  Koornneef (1986).  Briefly, the throughput calibration of the HST
  observatory is represented in a framework consisting of
  </p>
  <p>
  1) component throughput functions for every optical component
  (e.g. mirror, filter, polarizer, disperser, detector)
  </p>
  <p>
  2) configuration graph describing the allowed combinations of the
  components.
  </p>
  <p>
  A particular observing mode is specified by a list of keywords, which
  are familiar names of filters, detectors, etc.  The keywords are used
  to trace a path through the observatory configuration graph, thereby
  translating the keyword list into a list of pointers to data files
  that contain the individual component throughput functions.  The grand
  throughput function of the requested observing mode is formed by
  multiplying together the individual component throughputs at each
  wavelength.
  </p>
  <p>
  To retrieve a particular HST passband, a user furnishes the passband
  generator with a couple of keywords, for example <span style="font-family: monospace;">"WFPC F336W"</span>.  The
  passband generator uses the keywords to trace a path through the
  graph, multiplies together the component passbands it encounters along
  the way, and returns the mode passband evaluated on a particular
  wavelength grid.
  </p>
  <p>
  Passbands can then be convolved with spectral data to simulate HST
  observations of particular targets.  Spectra may come from a database
  of spectral atlases and HST calibration targets, or may be dynamically
  generated (individually or in combination) as simple blackbody,
  power-law, or HI emission-line spectra of chosen temperatures and
  slopes.
  </p>
  <p>
  The form of the spectrum to be convolved with the passband is entered
  as an expression. This expression is evaluated by the synphot
  expression evaluator, syncalc.  The expression evaluator is written to
  work like Fortran, so that the format of expressions will be easy to
  understand and use. Syncalc supports the four basic functions plus
  negation, as well as several functions.  Expressions can be
  parenthesized to change the default order of evaluation. Spaces are
  not significant, except that the subtraction and division operators
  must be surrounded by blanks so that they will not be mistaken for
  part of a filename. Here are some examples of expressions:
  </p>
  <div class="highlight-default-notranslate"><pre>
  band(wfpc,f555w,1)
  vega.tab * ebmv(1.0)
  bb(5500)*tilt(band(v),1,2,3)
  rn(pl(1000,-2),band(v),15,stmag)
  </pre></div>
  <p>
  Syncalc evaluates expressions containing filenames, constants, and
  variables. When syncalc sees a filename, it determines if the file is
  a passband or a spectrum and reads it interpolated on the wavelength
  grid. Constants are either numbers or strings. String constants are
  NOT surrounded by quote marks. Numeric constants are interpreted as
  real numbers and all mathematical operations between filenames and
  constants are legal. Variables are dollar signs followed by a positive
  integer, for example, $3. Variables may occur wherever a numeric
  constant is legal in an expression. Variables are used wherever
  repeated evaluation of an expression is necessary, such as the fitting
  routines. Many tasks have a parameter vzero. This parameter takes a
  list of numeric values an substitutes each value into the expression
  wherever the variable $0 occurs. These tasks provide an implicit
  method for evaluating an expression many times with different numeric
  values. 
  </p>
  <p>
  Syncalc prevents physically meaningless expressions from being
  computed by keeping track of the degree of the expression during
  computation. Constants, variables and passbands have a degree of zero.
  Spectra have a degree of one. Each function also has a degree, which
  is either zero or one. Multiplying two subexpressions yields a result
  whose degree is the sum of the degrees of the two subexpressions.
  Dividing two subexpressions yields a result whose degree is the
  difference between the degrees of the two subexpressions. Adding or
  subtracting two subexpressions yields a result whose degree is the
  same as the degrees of both subexpressions. Adding or subtracting two
  subexpressions whose degrees are different is forbidden and causes an
  error exit. Negation gives a result whose degree is the same as the
  subexpression. The degree of the entire expression must either be zero
  or one. An expression with degree zero is a passband and with degree
  one is a spectrum.
  </p>
  <p>
  A filename may have a column name appended in brackets. If it does,
  syncalc will read the flux or throughput from the named column. This
  allows a file to contain more than one spectrum or thoughput, each in
  a separate column. If the filename does not contain a column name
  appended in brackets, the default column name is used. These are FLUX
  for a spectrum and THROUGHPUT for a throughput table.
  </p>
  <p>
  Syncalc determines whether a file contains a passband or a spectrum by
  first trying to open the file as a spectrum. If there is an error, it
  will then try to open it as a throughout file. Ascii files will always
  succeed when opened as spectra, so all ascii files are assumed to be
  spectra. Syncalc has the thru() function, which forces a file to be
  read as a passband. It also has the spec() function, which forces a
  file to be read as a spectrum. The thru() and spec() function are also
  useful for filenames with strange characters or that begin with
  digits.
  </p>
  <p>
  The heart of syncalc is the set of functions it supports. The
  following table lists these functions, their degree, amd their
  arguments. The name of the arguments indicate the argument type: NUM
  for numeric constants, STR for string constants, BAND for passbands,
  and SPEC for spectra. Ellipsis marks indicate that an indefinite
  number of arguments of the same type as the last explicitly stated
  argument may be included in the function
  </p>
  <div class="highlight-default-notranslate"><pre>
  FUNCTION                        DEG     DESCRIPTION
  ----------------------------------------------------------------------
  band(str1, ...)                 0       Telescope passband
  bb(num1)                        1       Black body spectrum
  box(num1, num2)                 0       Rectangular passband
  ebmv(num1)                      0       Galactic extinction curve
  ebmvx(num1, str1)               0       Other extinction curves
  gauss(num1, num2)               0       Normal curve passband
  grid (str1, num1)               1       Interpolated spectrum in grid
  hi(num1, num2)                  1       Hydrogen absorption spectrum
  lgauss(num1, num2)              0       Log normal curve passband
  pl(num1, num2)                  1       Power law spectrum
  poly(num1, num2, num3, ...)     0       Legendre polynomial
  rn(spec1, band1, num1, str1)    1       Renormalize spectrum
  spec(str1)                      1       Read a spectrum
  thru(str1)                      0       Read a passband
  tilt(band1, num1, ...)          0       Legendre polynomial product
  unit(num1, str1)                1       Constant spectrum
  z(spec1, num1)                  1       Redshift spectrum
  </pre></div>
  <p>
  Ascii tables contain no information about column units, so syncalc
  assumes default units of flam. If this assumption is not correct,
  it is quite easy to convert an ascii file to a table with tcreate. All
  that is required is a format file. The following format files can be
  used to convert ascii files into the default table format:
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Spectrum format file
  WAVELENGTH       R          %10.2f ANGSTROMS
  FLUX             R          %12.5g FLAM
  
  # Throughout format file
  WAVELENGTH       R          %10.1f ANGSTROMS
  THROUGHPUT       R          %12.5g TRANSMISSION
  ERROR            R          %12.5g TRANSMISSION
  </pre></div>
  <p>
  There are three main categories of tasks in the synphot package.  The
  primary group of tasks perform calculations and plotting of passbands
  and spectra.
  </p>
  <div class="highlight-default-notranslate"><pre>
  task      function
  
  bandpar   Calculate photometric parameters of a passband
  calcband  Calculate a model passband
  calcspec  Calculate a model spectrum
  calcphot  Calculate synthetic photometry for model spectrum and passband
  countrate Calculate the HST countrate for model spectrum and passband
  plband    Plot a set of passbands
  plspec    Plot spectral and photometric data
  plratio   Plot ratio of observed and synthetic data
  pltrans   Plot photometric transformation (color-color, color-mag) diagrams
  </pre></div>
  <p>
  A second group of task perform fitting of model passbands and spectra
  to spectrophotometric and photometric data.  These tasks are intended
  to be used for passband reconstruction.
  </p>
  <div class="highlight-default-notranslate"><pre>
  task      function
  
  fitband   Fit a model passband to spectrophotometric data
  fitspec   Fit a model spectrum to spectrophotometric data
  fitgrid   Fit a spectrum by interpolating within a grid of spectra
  </pre></div>
  <p>
  A third group of tasks perform auxilliary tasks useful for using the
  other synphot tasks.
  </p>
  <div class="highlight-default-notranslate"><pre>
  task       function
  
  imspec    Convert an IRAF/ST4GEM image to or from an ST4GEM table
  genwave   Generate a wavelength set
  mkthru    Create a throughput table for installation in CDBS
  obsmode   Display observation mode keywords
  showfiles Print a list of filenames used in a synphot expression
  </pre></div>
  <p>
  Finally, there is a group of utility tasks that can be used to check
  or maintain the instrument component tables used by synphot.
  </p>
  <div class="highlight-default-notranslate"><pre>
  task      function
  
  graflist  List the components downstream from a given component
  grafplot  Plot the components downstream from a given component
  grafpath  Print keyword and component names for a path through
            the graph table
  grafcheck Check an instrument graph table for bad rows
  </pre></div>
  <p>
  Several of the tasks in the synphot package generate quantities that
  need to be precisely defined. These quantites are also known by the
  header keyword names they are stored under in calibrated image
  headers. These quantities are the unit stimulus (PHOTFLAM), the
  photometric zero point (PHOTZPT), the pivot wavelength (PHOTPLAM), and
  the root mean square bandwidth (PHOTBW). 
  </p>
  <p>
  The unit stimulus (PHOTFLAM) is the stimulus needed to produce a unit
  response of one count per second. The unit stimulus is defined in
  wavelength units by the formula
  </p>
  <p>
  U(P) =  h * c / [A * INT(P(lam) * lam  * dlam)]
  </p>
  <p>
  In this formula, A is the telescope area and P(lam) is the observation
  mode passband as a function of wavelength.
  </p>
  <p>
  Th photometric zero point (PHOTZPT) of the ST magnitude system is
  defined so that the magnitude of Vega is zero in the Johnson V
  passband. 
  </p>
  <p>
  The pivot wavelength (PHOTPLAM) allows exact conversion of fluxes
  between wavelength and frequency units. It is one measure of the
  average wavelength of a passband. The pivot wavelength is defined by
  the formula
  </p>
  <p>
  lam(P) = sqrt [INT(P(lam) * lam * dlam) / INT(P(lam) * dlam / lam)]
  </p>
  <p>
  The root mean square bandwidth (PHOTBW) is the standard deviation of
  the passband as a function of the logarithm of the wavelength. It is
  defined by the formula
  </p>
  <p>
  sigma(P) = sqrt [ INT(P(lam) * ln(lam/barlam)^2 * dlam/lam) /
  		  INT(P(lam) * dlam/lam) ]
  </p>
  <p>
  In this formula barlam is the bar wavelength, defined by the formula
  </p>
  <p>
  barlam = INT(P(lam) * ln(lam) * dlam/lam) / INT(P(lam) * dlam/lam)
  </p>
  <!-- Contents:  -->
  

.. _aidpars:

aidpars: Automatic line identification parameters and algorithm
===============================================================

**Package: onedspec**

.. raw:: html

  <section id="s_summary">
  <h3>Summary</h3>
  <p>
  The automatic line identification parameters and algorithm used in
  <b>autoidentify</b>, <b>identify</b>, and <b>reidentify</b> are described.
  </p>
  </section>
  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  aidpars
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_reflist">
  <dt><b>reflist = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reflist' Line='reflist = ""' -->
  <dd>Optional reference coordinate list to use in the pattern matching algorithm
  in place of the task coordinate list.  This file is a simple text list of
  dispersion coordinates.  It would normally be a culled and limited list of
  lines for the specific data being identified.
  </dd>
  </dl>
  <dl id="l_refspec">
  <dt><b>refspec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refspec' Line='refspec = ""' -->
  <dd>Optional reference dispersion calibrated spectrum.  This template spectrum
  is used to select the prominent lines for the pattern matching algorithm.
  It need not have the same dispersion increment or dispersion coverage as
  the target spectrum.
  </dd>
  </dl>
  <dl id="l_crpix">
  <dt><b>crpix = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crpix' Line='crpix = "INDEF"' -->
  <dd>Coordinate reference pixel for the coordinate reference value specified by
  the <i>crval</i> parameter.  This may be specified as a pixel coordinate
  or an image header keyword name (with or without a <span style="font-family: monospace;">'!'</span> prefix).  In the
  latter case the value of the keyword in the image header of the spectrum
  being identified is used.  A value of INDEF translates to the middle of
  the target spectrum.
  </dd>
  </dl>
  <dl id="l_crquad">
  <dt><b>crquad = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crquad' Line='crquad = INDEF' -->
  <dd>Quadratic correction to the detected pixel positions to <span style="font-family: monospace;">"linearize"</span> the
  pattern of line spacings.  The corrected positions x' are derived from
  the measured positions x by
  <div class="highlight-default-notranslate"><pre>
  x' = x + crquad * (x - crpix)**2
  </pre></div>
  where crpix is the pixel reference point as defined by the <i>crpix</i>
  parameter.  The measured and corrected positions may be examined by
  using the <span style="font-family: monospace;">'t'</span> debug flag.  The value may be a number or a header
  keyword (with or without a <span style="font-family: monospace;">'!'</span> prefix).  The default of INDEF translates
  to zero; i.e. no quadratic correction.
  </dd>
  </dl>
  <dl id="l_cddir">
  <dt><b>cddir = <span style="font-family: monospace;">"sign"</span> (unknown|sign|increasing|decreasing)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cddir' Line='cddir = "sign" (unknown|sign|increasing|decreasing)' -->
  <dd>The sense of the dispersion increment with respect to the pixel coordinates
  in the input spectrum.  The possible values are <span style="font-family: monospace;">"increasing"</span> or
  <span style="font-family: monospace;">"decreasing"</span> if the dispersion coordinates increase or decrease with
  increasing pixel coordinates, <span style="font-family: monospace;">"sign"</span> to use the sign of the dispersion
  increment (positive is increasing and negative is decreasing), and
  <span style="font-family: monospace;">"unknown"</span> if the sense is unknown and to be determined by the algorithm.
  </dd>
  </dl>
  <dl id="l_crsearch">
  <dt><b>crsearch = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crsearch' Line='crsearch = "INDEF"' -->
  <dd>Coordinate reference value search radius.  The value may be specified
  as a numerical value or as an image header keyword (with or without
  a <span style="font-family: monospace;">'!'</span> prefix) whose value is to be used.  The algorithm will search
  for a final coordinate reference value within this amount of the value
  specified by <i>crval</i>.  If the value is positive the search radius is
  the specified value.  If the value is negative it is the absolute value
  of this parameter times <i>cdelt</i> times the number of pixels in the
  input spectrum; i.e. it is the fraction of dispersion range covered by the
  target spectrum assuming a dispersion increment per pixel of <i>cdelt</i>.
  A value of INDEF translates to -0.1 which corresponds to a search radius
  of 10% of the estimated dispersion range.
  </dd>
  </dl>
  <dl id="l_cdsearch">
  <dt><b>cdsearch = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cdsearch' Line='cdsearch = "INDEF"' -->
  <dd>Dispersion coordinate increment search radius.  The value may be specified
  as a numerical value or as an image header keyword (with or without
  a <span style="font-family: monospace;">'!'</span> prefix) whose value is to be used.  The algorithm will search
  for a dispersion coordinate increment within this amount of the value
  specified by <i>cdelt</i>.  If the value is positive the search radius is
  the specified value.  If the value is negative it is the absolute value of
  this parameter times <i>cdelt</i>; i.e.  it is a fraction of <i>cdelt</i>.
  A value of INDEF translates to -0.1 which corresponds to a search radius
  of 10% of <i>cdelt</i>.
  </dd>
  </dl>
  <dl id="l_ntarget">
  <dt><b>ntarget = 100</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ntarget' Line='ntarget = 100' -->
  <dd>Number of spectral lines from the target spectrum to use in the pattern
  matching.
  </dd>
  </dl>
  <dl id="l_npattern">
  <dt><b>npattern = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='npattern' Line='npattern = 5' -->
  <dd>Initial number of spectral lines in patterns to be matched.  There is a
  minimum of 3 and a maximum of 10.  The algorithm starts with the specified
  number and if no solution is found with that number it is iteratively
  decreased by one to the minimum of 3.  A larger number yields fewer
  and more likely candidate matches and so will produce a result sooner.
  But in order to be thorough the algorithm will try smaller patterns to
  search more possiblities.
  </dd>
  </dl>
  <dl id="l_nneighbors">
  <dt><b>nneighbors = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nneighbors' Line='nneighbors = 10' -->
  <dd>Number of neighbors to use in making patterns of lines.  This parameter
  restricts patterns to include lines which are near each other.
  </dd>
  </dl>
  <dl id="l_nbins">
  <dt><b>nbins = 6</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nbins' Line='nbins = 6' -->
  <dd>Maximum number of bins to divide the reference coordinate list or spectrum
  in searching for a solution.  When there are no weak dispersion constraints
  the algorithm subdivides the full range of the coordinate list or reference
  spectrum into one bin, two bins, etc. up to this maximum.  Each bin is
  searched for a solution.
  </dd>
  </dl>
  <dl id="l_ndmax">
  <dt><b>ndmax = 1000</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ndmax' Line='ndmax = 1000' -->
  <dd>Maximum number of candidate dispersions to examine.  The algorithm ranks
  candidate dispersions by how many candidate spectral lines are fit and the
  the weights assigned by the pattern matching algorithm.  Starting from
  the highest rank it tests each candidate dispersion to see if it is
  a satisfactory solution.  This parameter determines how many candidate
  dispersion in the ranked list are examined.
  </dd>
  </dl>
  <dl id="l_aidord">
  <dt><b>aidord = 3 (minimum of 2)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='aidord' Line='aidord = 3 (minimum of 2)' -->
  <dd>The order of the dispersion function fit by the automatic identification
  algorithm.  This is the number of polynomial coefficients so
  a value of two is a linear function and a value of three is a quadratic
  function.  The order should be restricted to values of two or three.
  Higher orders can lead to incorrect solutions because of the increased
  degrees of freedom if finding incorrect line identifications.
  </dd>
  </dl>
  <dl id="l_maxnl">
  <dt><b>maxnl = 0.02</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxnl' Line='maxnl = 0.02' -->
  <dd>Maximum non-linearity allowed in any trial dispersion function.
  The definition of the non-linearity test is
  <div class="highlight-default-notranslate"><pre>
  maxnl &gt; (w(0.5) - w(0)) / (w(1) - w(0)) - 0.5
  </pre></div>
  where w(x) is the dispersion function value (e.g. wavelength) of the fit
  and x is a normalized pixel positions where the endpoints of the spectrum
  are [0,1].  If the test fails on a trial dispersion fit then a linear
  function is determined.
  </dd>
  </dl>
  <dl id="l_nfound">
  <dt><b>nfound = 6</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nfound' Line='nfound = 6' -->
  <dd>Minimum number of identified spectral lines required in the final solution.
  If a candidate solution has fewer identified lines it is rejected.
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma = 0.05</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma' Line='sigma = 0.05' -->
  <dd>Sigma (uncertainty) in the line center estimates specified in pixels.
  This is used to propagate uncertainties in the line spacings in
  the observed patterns of lines.
  </dd>
  </dl>
  <dl id="l_minratio">
  <dt><b>minratio = 0.1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minratio' Line='minratio = 0.1' -->
  <dd>Minimum spacing ratio used.  Patterns of lines in which the ratio of
  spacings between consecutive lines is less than this amount are excluded.
  </dd>
  </dl>
  <dl id="l_rms">
  <dt><b>rms = 0.1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rms' Line='rms = 0.1' -->
  <dd>RMS goal for a correct dispersion solution.  This is the RMS in the
  measured spectral lines relative to the expected positions from the
  coordinate line list based on the coordinate dispersion solution.
  The parameter is specified in terms of the line centering parameter
  <i>fwidth</i> since for broader lines the pixel RMS would be expected
  to be larger.  A pixel-based RMS criterion is used to be independent of
  the dispersion.  The RMS will be small for a valid solution.
  </dd>
  </dl>
  <dl id="l_fmatch">
  <dt><b>fmatch = 0.2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fmatch' Line='fmatch = 0.2' -->
  <dd>Goal for the fraction of unidentified lines in a correct dispersion
  solution.  This is the fraction of the strong lines seen in the spectrum
  which are not identified and also the fraction of all lines in the
  coordinate line list, within the range of the dispersion solution, not
  identified.  Both fractions will be small for a valid solution.
  </dd>
  </dl>
  <dl id="l_debug">
  <dt><b>debug = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='debug' Line='debug = ""' -->
  <dd>Print or display debugging information.  This is intended for the developer
  and not the user.  The parameter is specified as a string of characters
  where each character displays some information.  The characters are:
  <div class="highlight-default-notranslate"><pre>
      a: Print candidate line assignments.
      b: Print search limits.
      c: Print list of line ratios.
  *   d: Graph dispersions.
  *   f: Print final result.
  *   l: Graph lines and spectra.
      r: Print list of reference lines.
  *   s: Print search iterations.
      t: Print list of target lines.
      v: Print vote array.
      w: Print wavelength bin limits.
  </pre></div>
  The items with an asterisk are the most useful.  The graphs are exited
  with <span style="font-family: monospace;">'q'</span> or <span style="font-family: monospace;">'Q'</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <b>aidpars</b> parameter set contains the parameters for the automatic
  spectral line identification algorithm used in the task <b>autoidentify</b>,
  <b>identify</b>, and <b>reidentify</b>.  These tasks include the parameter
  <i>aidpars</i> which links to this parameters set.  Typing <b>aidpars</b>
  allows these parameters to be edited.  When editing the parameters of the
  other tasks with <b>eparam</b> one can edit the <b>aidpars</b> parameters by
  type <span style="font-family: monospace;">":e"</span> when pointing to the <i>aidpars</i> task parameter.  The values of
  the <b>aidpars</b> parameters may also be set on the command line for the
  task.  The discussion which follows describes the parameters and the
  algorithm.
  </p>
  <p>
  The goal of the automatic spectral line identification algorithm is to
  automate the identification of spectral lines so that given an observed
  spectrum of a spectral line source (called the target spectrum) and a file
  of known dispersion coordinates for the lines, the software will identify
  the spectral lines and use these identifications to determine a
  dispersion function.  This algorithm is quite general so that the correct
  identifications and dispersion function may be found even when there is
  limited or no knowledge of the dispersion coverage and resolution of the
  observation.
  </p>
  <p>
  However, when a general line list, including a large dispersion range and
  many weak lines, is used and the observation covers a much smaller portion
  of the coordinate list the algorithm may take a long to time or even fail
  to find a solution.  Thus, it is highly desirable to provide additional
  input giving approximate dispersion parameters and their uncertainties.
  When available, a dispersion calibrated reference spectrum (not necessarily
  of the same resolution or wavelength coverage) also aids the algorithm by
  indicating the relative strengths of the lines in the coordinate file.  The
  line strengths need not be very similar (due to different lamps or
  detectors) but will still help separate the inherently weak and strong
  lines.
  </p>
  <p>
  The Input
  </p>
  <p>
  The primary inputs to the algorithm are the observed one dimensional target
  spectrum in which the spectral lines are to be identified and a dispersion
  function determined and a file of reference dispersion coordinates.  These
  inputs are provided in the tasks using the automatic line identification
  algorithm.
  </p>
  <p>
  One way to limit the algorithm to a specific dispersion region and to the
  important spectral lines is to use a limited coordinate list.  One may do
  this with the task coordinate list parameter (<i>coordlist</i>).  However,
  it is desirable to use a standard master line list that includes all the
  lines, both strong and weak.  Therefore, one may specify a limited line
  list with the parameter <i>reflist</i>.  The coordinates in this list will
  be used by the automatic identification algorithm to search for patterns
  while using the primary coordinate list for adding weaker lines during the
  dispersion function fitting.
  </p>
  <p>
  The tasks <b>autoidentify</b> and <b>identify</b> also provide parameters to
  limit the search range.  These parameters specify a reference dispersion
  coordinate (<i>crval</i>) and a dispersion increment per pixel (<i>cdelt</i>).
  When these parameters are INDEF this tells the algorithm to search for a
  solution over the entire range of possibilities covering the coordinate
  line list or reference spectrum.
  </p>
  <p>
  The reference dispersion coordinate refers to an approximate coordinate at
  the reference pixel coordinate specified by the parameter <i>crpix</i>.
  The default value for the reference pixel coordinate is INDEF which
  translates to the central pixel of the target spectrum.
  </p>
  <p>
  The parameters <i>crsearch</i> and <i>cdsearch</i> specify the expected range
  or uncertainty of the reference dispersion coordinate and dispersion
  increment per pixel respectively.  They may be specified as an absolute
  value or as a fraction.  When the values are positive they are used
  as an absolute value;
  </p>
  <div class="highlight-default-notranslate"><pre>
  crval(final) = <i>crval</i> +/- <i>crsearch</i>
  cdelt(final) = <i>cdelt</i> +/- <i>cdsearch</i>.
  </pre></div>
  <p>
  When the values are negative they are used as a fraction of the dispersion
  range or fraction of the dispersion increment;
  </p>
  <div class="highlight-default-notranslate"><pre>
  crval(final) = <i>crval</i> +/- abs (<i>crsearch</i> * <i>cdelt</i>) * N_pix
  cdelt(final) = <i>cdelt</i> +/- abs (<i>cdsearch</i> * <i>cdelt</i>)
  </pre></div>
  <p>
  where abs is the absolute value function and N_pix is the number of pixels
  in the target spectrum.  When the ranges are not given explicitly, that is
  they are specified as INDEF, default values of -0.1 are used.
  </p>
  <p>
  The parameters <i>crval</i>, <i>cdelt</i>, <i>crpix</i>, <i>crsearch</i>,
  and <i>cdsearch</i> may be given explicit numerical values or may
  be image header keyword names.  In the latter case the values of the
  indicated keywords are used.  This feature allows the approximate
  dispersion range information to be provided by the data acquisition
  system; either by the instrumentation or by user input.
  </p>
  <p>
  Because sometimes only the approximate magnitude of the dispersion
  increment is known and not the sign (i.e. whether the dispersion
  coordinates increase or decrease with increasing pixel coordinates)
  the parameter <i>cdsign</i> specifies if the dispersion direction is
  <span style="font-family: monospace;">"increasing"</span>, <span style="font-family: monospace;">"decreasing"</span>, <span style="font-family: monospace;">"unknown"</span>, or defined by the <span style="font-family: monospace;">"sign"</span> of the
  approximate dispersion increment parameter (sign of <i>cdelt</i>).
  </p>
  <p>
  The above parameters defining the approximate dispersion of the target
  spectrum apply to <i>autoidentify</i> and <i>identify</i>.  The task
  <b>reidentify</b> does not use these parameters except that the <i>shift</i>
  parameter corresponds to <i>crsearch</i> if it is non-zero.  This task
  assumes that spectra to be reidentified are the same as a reference
  spectrum except for a zero point dispersion offset; i.e. the approximate
  dispersion parameters are the same as the reference spectrum.  The
  dispersion increment search range is set to be 5% and the sign of the
  dispersion increment is the same as the reference spectrum.
  </p>
  <p>
  An optional input is a dispersion calibrated reference spectrum (referred to
  as the reference spectrum in the discussion).  This is specified either in
  the coordinate line list file or by the parameter <i>refspec</i>.  To
  specify a spectrum in the line list file the comment <span style="font-family: monospace;">"# Spectrum &lt;image&gt;"</span>
  is included where &lt;image&gt; is the image filename of the reference spectrum.
  Some of the standard line lists in linelists$ may include a reference
  spectrum.  The reference spectrum is used to select the strongest lines for
  the pattern matching algorithm.
  </p>
  <p>
  The Algorithm
  </p>
  <p>
  First a list of the pixel positions for the strong spectral lines in the
  target spectrum is created.  This is accomplished by finding the local
  maxima, sorting them by pixel value, and then using a centering algorithm
  (<i>center1d</i>) to accurately find the centers of the line profiles.  Note
  that task parameters <i>ftype</i>, <i>fwidth</i>, <i>cradius</i>,
  <i>threshold</i>, and <i>minsep</i> are used for the centering.  The number
  of spectral lines selected is set by the parameter <i>ntarget</i>.
  </p>
  <p>
  In order to insure that lines are selected across the entire spectrum
  when all the strong lines are concentrated in only a part of the
  spectrum, the spectrum is divided into five regions and approximately
  a fifth of the requested number of lines is found in each region.
  </p>
  <p>
  A list of reference dispersion coordinates is selected from the coordinate
  file (<i>coordlist</i> or <i>reflist</i>).  The number of reference
  dispersion coordinates is set at twice the number of target lines found.
  The reference coordinates are either selected uniformly from the coordinate
  file or by locating the strong spectral lines (in the same way as for the
  target spectrum) in a reference spectrum if one is provided.  The selection
  is limited to the expected range of the dispersion as specified by the
  user.  If no approximate dispersion information is provided the range of
  the coordinate file or reference spectrum is used.
  </p>
  <p>
  The ratios of consecutive spacings (the lists are sorted in increasing
  order) for N-tuples of coordinates are computed from both lists.  The size
  of the N-tuple pattern is set by the <i>npattern</i> parameter.  Rather than
  considering all possible combinations of lines only patterns of lines with
  all members within <i>nneighbors</i> in the lists are used; i.e. the first
  and last members of a pattern must be within <i>nneighbors</i> of each other
  in the lists.  The default case is to find all sets of five lines which are
  within ten lines of each other and compute the three spacing ratios.
  Because very small spacing ratios become uncertain, the line patterns are
  limited to those with ratios greater than the minimum specified by the
  <i>minratio</i> parameter.  Note that if the direction of the dispersion is
  unknown then one computes the ratios in the reference coordinates in both
  directions.
  </p>
  <p>
  The basic idea is that similar patterns in the pixel list and the
  dispersion list will have matching spacing ratios to within a tolerance
  derived by the uncertainties in the line positions (<i>sigma</i>) from the
  target spectrum.  The reference dispersion coordinates are assumed to have
  no uncertainty.  All matches in the ratio space are found between patterns
  in the two lists.  When matches are made then the candidate identifications
  (pixel, reference dispersion coordinate) between the elements of the
  patterns are recorded.  After finding all the matches in ratio space a
  count is made of how often each possible candidate identification is
  found.  When there are a sufficient number of true pairs between the lists
  (of order 25% of the shorter list) then true identifications will appear in
  common in many different patterns.  Thus the highest counts of candidate
  identifications are the most likely to be true identifications.
  </p>
  <p>
  Because the relationship between the pixel positions of the lines in the
  target spectrum and the line positions in the reference coordinate space
  is generally non-linear the line spacing ratios are distorted and may
  reduce the pattern matching.  The line patterns are normally restricted
  to be somewhat near each other by the <i>nneighbors</i> so some degree of
  distortion can be tolerated.  But in order to provide the ability to remove
  some of this distortion when it is known the parameter <i>crquad</i> is
  provided.  This parameter applies a quadratic transformation to the measured
  pixel positions to another set of <span style="font-family: monospace;">"linearized"</span> positions  which are used
  in the line ratio pattern matching.  The form of the transformation is
  </p>
  <div class="highlight-default-notranslate"><pre>
  x' = x + crquad * (x - crpix)**2
  </pre></div>
  <p>
  where x is the measured position, x' is the transformed position,
  crquad is the value of the distortion parameter, and crpix is the value
  of the coordinate reference position.
  </p>
  <p>
  If approximate dispersion parameters and search ranges are defined then
  candidate identifications which fall outside the range of dispersion
  function possibilities are rejected.  From the remaining candidate
  identifications the highest vote getters are selected.  The number selected
  is three times the number of target lines.
  </p>
  <p>
  All linear dispersions functions, where dispersion and pixel coordinates
  are related by a zero point and slope, are found that pass within two
  pixels of two or more of the candidate identifications.  The dispersion
  functions are ranked primarily by the number of candidate identifications
  fitting the dispersion and secondarily by the total votes in the
  identifications.  Only the highest ranking candidate linear dispersion
  are kept.  The number of candidate dispersions kept is set by the
  parameter <i>ndmax</i>.
  </p>
  <p>
  The candidate dispersions are evaluated in order of their ranking.  Each
  line in the coordinate file (<i>coordlist</i>) is converted to a pixel
  coordinate based on the dispersion function.  The centering algorithm
  attempts to find a line profile near that position as defined by the
  <i>match</i> parameter.  This may be specified in pixel or dispersion
  coordinates.  All the lines found are used to fit a polynomial dispersion
  function with <i>aidord</i> coefficients.  The order should be linear or
  quadratic because otherwise the increased degrees of freedom allow
  unrealistic dispersion functions to appear to give a good result.  A
  quadratic function (<i>aidord</i> = 3) is allowed since this is the
  approximate form of many dispersion functions.
  </p>
  <p>
  However, to avoid unrealistic dispersion functions a test is made that
  the maximum amplitude deviation from a linear function is less than
  an amount specified by the <i>maxnl</i> parameter.  The definition of
  the test is
  </p>
  <div class="highlight-default-notranslate"><pre>
  maxnl &gt; (w(0.5) - w(0)) / (w(1) - w(0)) - 0.5
  </pre></div>
  <p>
  where w(x) is the dispersion function value (e.g. wavelength) of the fit
  and x is a normalized pixel positions where the endpoints of the spectrum
  are [0,1].  What this relation means is that the wavelength interval
  between one end and the center relative to the entire wavelength interval
  is within maxnl of one-half.  If the test fails then a linear function
  is fit.  The process of adding lines based on the last dispersion function
  and then refitting the dispersion function is iterated twice.  At the end
  of this step if fewer than the number of lines specified by the parameter
  <i>nfound</i> have been identified the candidate dispersion is eliminated.
  </p>
  <p>
  The quality of the line identifications and dispersion solution is
  evaluated based on three criteria.  The first one is the root-mean-square
  of the residuals between the pixel coordinates derived from lines found
  from the dispersion coordinate file based on the dispersion function and
  the observed pixel coordinates.  This pixel RMS is normalized by the target
  RMS set with the <i>rms</i> parameter.  Note that the <i>rms</i> parameter
  is specified in units of the <i>fwidth</i> parameter.  This is because if
  the lines are broader, requiring a larger fwidth to obtain a centroid,
  then the expected uncertainty would be larger.  A good solution will have
  a normalized rms value less than one.  A pixel RMS criterion, as opposed
  to a dispersion coordinate RMS, is used since this is independent of the
  actual dispersion of the spectrum.
  </p>
  <p>
  The other two criteria are the fraction of strong lines from the target
  spectrum list which were not identified with lines in the coordinate file
  and the fraction of all the lines in the coordinate file (within the
  dispersion range covered by the candidate dispersion) which were not
  identified.  These are normalized to a target value given by <i>fmatch</i>.
  The default matching goal is 0.3 which means that less than 30% of
  the lines should be unidentified or greater than 70% should be identified.
  As with the RMS, a value of one or less corresponds to a good solution.
  </p>
  <p>
  The reason the fraction identified criteria are used is that the pixel RMS
  can be minimized by finding solutions with large dispersion increment per
  pixel.  This puts all the lines in the coordinate file into a small range
  of pixels and so (incorrect) lines with very small residuals can be found.
  The strong line identification criterion is clearly a requirement that
  humans use in evaluating a solution.  The fraction of all lines identified,
  as opposed to the number of lines identified, in the coordinate file is
  included to reduce the case of a large dispersion increment per pixel
  mapping a large number of lines (such as the entire list) into the range of
  pixels in the target spectrum.  This can give the appearance of finding a
  large number of lines from the coordinate file.  However, an incorrect
  dispersion will also find a large number which are not matched.  Hence the
  fraction not matched will be high.
  </p>
  <p>
  The three criteria, all of which are normalized so that values less
  than one are good, are combined to a single figure of merit by a weighted
  average.  Equal weights have been found to work well; i.e. each criterion
  is one-third of the figure of merit.  In testing it has been found that all
  correct solutions over a wide range of resolutions and dispersion coverage
  have figures of merit less than one and typically of order 0.2.  All
  incorrect candidate dispersion have values of order two to three.
  </p>
  <p>
  The search for the correct dispersion function terminates immediately,
  but after checking the first five most likely candidates, when
  a figure of merit less than one is found.  The order in which the candidate
  dispersions are tested, that is by rank, was chosen to try the most promising
  first so that often the correct solution is found on the first attempt.
  </p>
  <p>
  When the approximate dispersion is not known or is imprecise it is
  often the case that the pixel and coordinate lists will not overlap
  enough to have a sufficient number true coordinate pairs.  Thus, at a
  higher level the above steps are iterated by partitioning the dispersion
  space searched into bins of various sizes.  The largest size is the
  maximum dispersion range including allowance for the search radii.
  The smallest size bin is obtained by dividing the dispersion range by
  the number specified by the <i>nbins</i> parameter.  The actual number
  of bins searched at each bin size is actually twice the number of
  bins minus one because the bins are overlapped by 50%.
  </p>
  <p>
  The search is done starting with bins in the middle of the size range and
  in the middle of the dispersion range and working outward towards larger
  and smaller bins and larger and smaller dispersion ranges.  This is done to
  improved the chances of finding the correction dispersion function in the
  smallest number of steps.
  </p>
  <p>
  Another iteration performed if no solution is found after trying all the
  candidate dispersion and bins is to reduce the number of lines in the
  pattern.  So the parameter <i>npattern</i> is an initial maximum pattern.
  A larger pattern gives fewer and higher quality candidate identifications
  and so converges faster.  However, if no solution is found the algorithm
  tries more possible matches produced by a lower number of lines in
  the pattern.  The pattern groups are reduced to a minimum of three lines.
  </p>
  <p>
  When a set of line identifications and dispersion solution satisfying the
  figure of merit criterion is found a final step is performed.
  Up to this point only linear dispersion functions are used since higher order
  function can be stretch in unrealistic ways to give good RMS values
  and fit all the lines.  The final step is to use the line identifications
  to fit a dispersion function using all the parameters specified by the
  user (such as function type, order, and rejection parameters).  This
  is iterated to add new lines from the coordinate list based on the
  more general dispersion function and then obtain a final dispersion
  function.  The line identifications and dispersion function are then
  returned to the task using this automatic line identification algorithm.
  </p>
  <p>
  If a satisfactory  solution is not found after searching all the
  possibilities the algorithm will inform the task using it and the task will
  report this appropriately.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lpar aidpars
  </pre></div>
  <p>
  2. Edit the parameters with <b>eparam</b>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; aidpars
  </pre></div>
  <p>
  3. Edit the <b>aidpars</b> parameters from within <b>autoidentify</b>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epar autoid
      [edit the parameters]
      [move to the "aidpars" parameter and type :e]
      [edit the aidpars parameters and type :q or EOF character]
      [finish editing the autoidentify parameters]
      [type :wq or the EOF character]
  </pre></div>
  <p>
  4. Set one of the parameters on the command line.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; autoidentify spec002 5400 2.5 crpix=1
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_AIDPARS">
  <dt><b>AIDPARS V2.12.2</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='AIDPARS' Line='AIDPARS V2.12.2' -->
  <dd>There were many changes made in the paramters and algorithm.  New parameters
  are <span style="font-family: monospace;">"crquad"</span> and <span style="font-family: monospace;">"maxnl"</span>.  Changed definitions are for <span style="font-family: monospace;">"rms"</span>.  Default
  value changes are for <span style="font-family: monospace;">"cddir"</span>, <span style="font-family: monospace;">"ntarget"</span>, <span style="font-family: monospace;">"ndmax"</span>, and <span style="font-family: monospace;">"fmatch"</span>.  The most
  significant changes in the algorithm are to allow for more non-linear
  dispersion with the <span style="font-family: monospace;">"maxnl"</span> parameter, to decrease the <span style="font-family: monospace;">"npattern"</span> value
  if no solution is found with the specified value, and to search a larger
  number of candidate dispersions.
  </dd>
  </dl>
  <dl id="l_AIDPARS">
  <dt><b>AIDPARS V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='AIDPARS' Line='AIDPARS V2.11' -->
  <dd>This parameter set is new in this version.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  autoidentify, identify, reidentify, center1d
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SUMMARY' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

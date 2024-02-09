.. _autoidentify:

autoidentify: Automatically identify lines and fit dispersion
=============================================================

**Package: xonedspec**

.. raw:: html

  <section id="s_summary">
  <h3>Summary</h3>
  <p>
  Spectral lines are automatically identified from a list of coordinates
  by pattern matching.  The identified lines are then used to fit a
  dispersion function which is written to a database for later use
  in dispersion calibration.  After a solution is found the identified
  lines and dispersion function may be examined interactively.
  </p>
  </section>
  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  autoidentify images crval cdelt
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images containing one dimensional spectra in which to identify
  spectral lines and fit dispersion functions.  For two and three dimensional
  spectral and spatial data one may use an image section to select a one
  dimensional spectral vector or use the <i>section</i> parameter.
  </dd>
  </dl>
  <dl id="l_crval">
  <dt><b>crval, cdelt</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crval' Line='crval, cdelt' -->
  <dd>These parameters specify an approximate coordinate value and coordinate
  interval per pixel.  They may be specified as numerical values, INDEF, or
  image header keyword names whose values are to be used.  The coordinate
  reference value is for the pixel specified by the parameter
  <i>aidpars.crpix</i>.  The default reference pixel is INDEF which means the
  middle of the spectrum.  By default only the magnitude of the coordinate
  interval is used and the search will include both increasing and decreasing
  coordinate values with increasing pixel values.  If one or both of these
  parameters are specified as INDEF the search for a solution will be slower
  and more likely to fail.
  </dd>
  </dl>
  <dl id="l_coordlist">
  <dt><b>coordlist = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coordlist' Line='coordlist = ""' -->
  <dd>Coordinate list consisting of an list of spectral line coordinates.
  A comment line of the form <span style="font-family: monospace;">"# units &lt;units&gt;"</span>, where &lt;units&gt; is one of the
  understood units names, defines the units of the coordinate list.  If no units
  are specified then Angstroms are assumed.
  The line list is used for both the final identifications and for the set of
  lines to use in the automatic search.  A restricted search list may be
  specified with the parameter <i>aidpars.reflist</i>.  The line list may
  contain a comment line of the form <span style="font-family: monospace;">"# Spectrum &lt;name&gt;"</span>, where &lt;name&gt; is a
  filename containing a reference spectrum.  The reference spectrum will be
  used in selecting the strong lines for the automatic search.  A reference
  spectrum may also be specified with the parameter <i>aidpars.refspec</i>.
  Some standard line lists are available in the directory <span style="font-family: monospace;">"linelists$"</span>.
  See the help topic <i>linelists</i> for the available line lists.
  </dd>
  </dl>
  <dl id="l_units">
  <dt><b>units = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='units' Line='units = ""' -->
  <dd>The units to use if no database entry exists.  The units are specified as
  described in
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help onedspec.package section=units
  </pre></div>
  If no units are specified and a coordinate list is used then the units of
  the coordinate list are selected.  If a database entry exists then the
  units defined there override both this parameter and the coordinate list.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes (no|yes|NO|YES)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes (no|yes|NO|YES)' -->
  <dd>After automatically identifying the spectral lines and dispersion function
  review and modify the solution interactively?  If <span style="font-family: monospace;">"yes"</span> a query is given
  for each spectrum providing the choice of interactive review.  The
  query may be turned off during execution.  If <span style="font-family: monospace;">"YES"</span> the interactive review
  is entered automatically without a query.  The interactive, graphical
  review is the same as the task <b>identify</b> with a few restriction.
  </dd>
  </dl>
  <dl id="l_aidpars">
  <dt><b>aidpars = <span style="font-family: monospace;">""</span> (parameter set)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='aidpars' Line='aidpars = "" (parameter set)' -->
  <dd>Parameter set for the automatic line identification algorithm.  The
  parameters are described in the help topic <b>aidpars</b>.
  </dd>
  </dl>
  <p>
  For two and three dimensional spectral images the following parameters are
  used to select a one dimensional spectrum.
  </p>
  <dl id="l_section">
  <dt><b>section = <span style="font-family: monospace;">"middle line"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='section' Line='section = "middle line"' -->
  <dd>If an image is not one dimensional or specified as a one dimensional image
  section then the image section given by this parameter is used.  The
  section defines a one dimensional spectrum.  The dispersion direction is
  derived from the vector direction.
  The section parameter may be specified directly as an image section or
  in one of the following forms
  <div class="highlight-default-notranslate"><pre>
  line|column|x|y|z first|middle|last|# [first|middle|last|#]]
  first|middle|last|# [first|middle|last|#] line|column|x|y|z
  </pre></div>
  where each field can be one of the strings separated by | except for #
  which is an integer number.  The field in [] is a second designator which
  is used with three dimensional data.  Abbreviations are allowed though
  beware that <span style="font-family: monospace;">'l'</span> is not a sufficient abbreviation.
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = <span style="font-family: monospace;">"1"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = "1"' -->
  <dd>Number of lines, columns, or bands across the designated dispersion axis to
  be summed when the image is a two or three dimensional image.
  It does not apply to multispec format spectra.  If the image is three
  dimensional an optional second number can be specified for the higher
  dimensional axis  (the first number applies to the lower axis number and
  the second to the higher axis number).  If a second number is not specified
  the first number is used for both axes.
  </dd>
  </dl>
  <p>
  The following parameters are used in finding spectral lines.
  </p>
  <dl id="l_ftype">
  <dt><b>ftype = <span style="font-family: monospace;">"emission"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ftype' Line='ftype = "emission"' -->
  <dd>Type of spectral lines to be identified.  The possibly abbreviated choices are
  <span style="font-family: monospace;">"emission"</span> and <span style="font-family: monospace;">"absorption"</span>.
  </dd>
  </dl>
  <dl id="l_fwidth">
  <dt><b>fwidth = 4.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fwidth' Line='fwidth = 4.' -->
  <dd>Full-width at the base (in pixels) of the spectral lines to be identified.
  </dd>
  </dl>
  <dl id="l_cradius">
  <dt><b>cradius = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cradius' Line='cradius = 5.' -->
  <dd>The maximum distance, in pixels, allowed between a line position
  and the initial estimate when defining a new line.
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 0.' -->
  <dd>In order for a line center to be determined the range of pixel intensities
  around the line must exceed this threshold.
  </dd>
  </dl>
  <dl id="l_minsep">
  <dt><b>minsep = 2.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minsep' Line='minsep = 2.' -->
  <dd>The minimum separation, in pixels, allowed between line positions
  when defining a new line.
  </dd>
  </dl>
  <dl id="l_match">
  <dt><b>match = -3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='match' Line='match = -3.' -->
  <dd>The maximum difference for a match between the line coordinate derived from
  the dispersion function and a coordinate in the coordinate list.  Positive
  values are in user coordinate units and negative values are in units of
  pixels.
  </dd>
  </dl>
  <p>
  The following parameters are used to fit a dispersion function to the user
  coordinates.  The <b>icfit</b> routines are used and further descriptions
  about these parameters may be found under that topic.
  </p>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"spline3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "spline3"' -->
  <dd>The function to be fit to user coordinates as a function of the pixel
  coordinates.  The choices are <span style="font-family: monospace;">"chebyshev"</span>, <span style="font-family: monospace;">"legendre"</span>, <span style="font-family: monospace;">"spline1"</span>, or <span style="font-family: monospace;">"spline3"</span>.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 1' -->
  <dd>Order of the fitting function.  The order is the number of polynomial
  terms (coefficients) or the number of spline pieces.
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample' Line='sample = "*"' -->
  <dd>Sample regions for fitting specified in in pixel coordinates.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 10' -->
  <dd>Number of rejection iterations.
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 3.0, high_reject = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_reject' Line='low_reject = 3.0, high_reject = 3.0' -->
  <dd>Lower and upper residual rejection in terms of the RMS of the fit.
  </dd>
  </dl>
  <dl id="l_grow">
  <dt><b>grow = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grow' Line='grow = 0' -->
  <dd>Distance from a rejected point in which additional points are automatically
  rejected regardless of their residuals.
  </dd>
  </dl>
  <p>
  The following parameters control the input and output.
  </p>
  <dl id="l_dbwrite">
  <dt><b>dbwrite = <span style="font-family: monospace;">"yes"</span>  (no|yes|NO|YES)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dbwrite' Line='dbwrite = "yes"  (no|yes|NO|YES)' -->
  <dd>Automatically write or update the database with the line identifications
  and dispersion function?  If <span style="font-family: monospace;">"no"</span> or <span style="font-family: monospace;">"NO"</span> then there is no database
  output.  If <span style="font-family: monospace;">"YES"</span> the results are automatically written to the database.
  If <span style="font-family: monospace;">"yes"</span> a query is made allowing the user to reply with <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"NO"</span>
  or <span style="font-family: monospace;">"YES"</span>.  The negative responses do not write to the database and the
  affirmative ones do write to the database.  The upper-case responses
  suppress any further queries for any remaining spectra.
  </dd>
  </dl>
  <dl id="l_overwrite">
  <dt><b>overwrite = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='overwrite' Line='overwrite = yes' -->
  <dd>Overwrite previous solutions in the database?  If there is a previous
  solution for the spectrum being identified this parameter selects whether
  to skip the spectrum (<span style="font-family: monospace;">"no"</span>) or find a new solution (<span style="font-family: monospace;">"yes"</span>).  In the later
  case saving the solution to the database will overwrite the previous
  solution.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"database"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "database"' -->
  <dd>Database for reading and writing the line identifications and
  dispersion functions.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print results of the identification on the standard output?
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "logfile"' -->
  <dd>Filename for recording log information about the identifications.
  The null string, <span style="font-family: monospace;">""</span>, may be specified to skip recording the log information.
  </dd>
  </dl>
  <dl id="l_plotfile">
  <dt><b>plotfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotfile' Line='plotfile = ""' -->
  <dd>Filename for recording log plot information as IRAF metacode.  A
  null string, <span style="font-family: monospace;">""</span>, may be specified to skip recording the plot information.
  (Plot output is currently not implemented.)
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Graphics device for the interactive review.  The default is the standard
  graphics device which is generally a graphics terminal.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Cursor input file for the interactive review.  If a cursor file is not
  given then the standard graphics cursor is read.
  </dd>
  </dl>
  <dl id="l_query">
  <dt><b>query</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='query' Line='query' -->
  <dd>Parameter used by the program to query the user.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Autoidentify</b> automatically identifies spectral lines from a list of
  spectral line coordinates (<i>coordlist</i>) and determines a dispersion
  function.  The identified lines and the dispersion function may be reviewed
  interactively (<i>interactive</i>) and the final results are recorded in a
  <i>database</i>.
  </p>
  <p>
  Each image in the input list (<i>images</i>) is considered in turn.  If the
  image is not one dimensional or a one dimensional section of an image then
  the parameter <i>section</i> is used to select a one dimensional
  spectrum.  It defines the dispersion direction and central spatial
  coordinate(s).  If the image is not one dimensional or a set of one
  dimensional spectra n multispec format then the <i>nsum</i> parameter
  selects the number of neighboring lines, columns, and bands to sum.
  </p>
  <p>
  This task is not intended to be used on all spectra in an image since in
  most cases the dispersion functions will be similar though possibly with a
  zero point shift.  Once one spectrum is identified the others may be
  reidentified with <b>reidentify</b>.
  </p>
  <p>
  The coordinate list of spectral lines often covers a much larger dispersion
  range than the spectra being identified.  This is true of the standard line
  lists available in the <span style="font-family: monospace;">"linelists$"</span> directory.  While the algorithm for
  identifying the lines will often succeed with a large line list it is not
  guaranteed nor will it find the solution quickly without additional
  information.  Thus it is highly desirable to provide the algorithm with
  approximate information about the spectra.  Generally this information is
  known by the observer or recorded in the image header.
  </p>
  <p>
  As implied in the previous paragraph, one may use a
  limited coordinate line list that matches the dispersion coverage of the
  spectra reasonably well (say within 100% of the dispersion range).
  This may be done with the <i>coordlist</i> parameter or a second
  coordinate list used only for the automatic search may be specified
  with the parameter <i>aidpars.reflist</i>.  This allows using a smaller
  culled list of lines for finding the matching patterns and a large list
  with weaker lines for the final dispersion function fit.
  </p>
  <p>
  The alternative to a limited list is to use the parameters <i>crval</i> and
  <i>cdelt</i> to specify the approximate coordinate range and dispersion
  interval per pixel.  These parameters may be given explicitly or by
  specifying image header keywords.  The pixel to which <i>crval</i> refers is
  specified by the parameter <i>aidpars.crpix</i>.  By default this is INDEF
  which means use the center of the spectrum.  The direction in which the
  dispersion coordinates increase relative to the pixel coordinates may be
  specified by the <i>aidpars.cddir</i> parameter.  The default is <span style="font-family: monospace;">"unknown"</span>
  to search in either direction.
  </p>
  <p>
  The algorithm used to automatically identify the spectral lines and
  find a dispersion function is described under the help topic
  <b>aidpars</b>.  This topic also describes the various algorithm
  parameters.  The default parameters are adequate for most data.
  </p>
  <p>
  The characteristics of the spectral lines to be found and identified are
  set by several parameters.  The type of spectral lines, whether <span style="font-family: monospace;">"emission"</span>
  or <span style="font-family: monospace;">"absorption"</span>, is set by the parameter <i>ftype</i>.  For arc-line
  calibration spectra this parameter is set to <span style="font-family: monospace;">"emission"</span>.  The full-width
  (in pixels) at the base of the spectral lines is set by the parameter
  <i>fwidth</i>.  This is used by the centering algorithm to define the extent
  of the line profile to be centered.  The <i>threshold</i> parameter defines
  a minimum contrast (difference) between a line peak and the neighboring
  continuum.  This allows noise peaks to be ignored.  Finding the center of a
  possible line begins with an initial position estimate.  This may be an
  interactive cursor position or the expected position from the coordinate
  line list.  The centering algorithm then searches for a line of the
  specified type, width, and threshold within a given distance, specified by
  the <i>cradius</i> parameter.  These parameters and the centering algorithm
  are described by the help topic <b>center1d</b>.
  </p>
  <p>
  To avoid finding the same line multiple times, say when there are two lines
  in the line list which are blended into a single in the observation, the
  <i>minsep</i> parameter rejects any new line position found within that
  distance of a previously defined line.
  </p>
  <p>
  The automatic identification of lines includes matching a line position in
  the spectrum against the list of coordinates in the coordinate line list.
  The <i>match</i> parameter defines how close the measured line position must
  be to a coordinate in the line list to be considered a possible
  identification.  This parameter may be specified either in user coordinate
  units (those used in the line list) by using a positive value or in pixels
  by using a negative value.  In the former case the line position is
  converted to user coordinates based on a dispersion function and in the
  latter the line list coordinate is converted to pixels using the inverse of
  the dispersion function.
  </p>
  <p>
  The dispersion function is determined by fitting a set of pixel positions
  and user coordinate identifications by least squares to a specified
  function type.  The fitting requires a function type, <i>function</i>, and
  the order (number of coefficients or spline pieces), <i>order</i>.
  In addition the fitting can be limited to specified regions, <i>sample</i>,
  and provide for the rejection of points with large residuals.  These
  parameters are set in advance and used during the automatic dispersion
  function determination.  Later the fitting may be modified interactively.
  For additional discussion of these parameters see <b>icfit</b>.
  </p>
  <p>
  The output of this program consists of log information, plot information,
  and the line identifications and dispersion function.  The log information
  may be appended to the file specified by the <i>logfile</i> parameter
  and printed to the standard output (normally the terminal) by
  setting the <i>verbose</i> parameter to yes.  This information consists
  of a banner line, a line of column labels, and results for each spectrum.
  For each spectrum the spectrum name, the number of spectral lines found,
  the dispersion coordinate at the middle of the spectrum, the dispersion
  increment per pixel, and the root-mean-square (RMS) of the residuals for
  the lines used in the dispersion function fit is recorded.  The units of
  the RMS are those of the user (line list) coordinates.  If a solution is
  not found the spectrum name and a message is printed.
  </p>
  <p>
  The line identifications and dispersion function are written to the
  specified <i>database</i>.  The current format of the database is described
  in the help for <i>identify</i>.  If a database entry is already present for
  a spectrum and the parameter <i>overwrite</i> is <span style="font-family: monospace;">"no"</span> then the spectrum is
  skipped and a message is printed to the standard output.   After a solution
  is found and after any interactive review (see below) the results may be
  written to the database.  The <i>dbwrite</i> parameter may be specified as
  <span style="font-family: monospace;">"no"</span> or <span style="font-family: monospace;">"NO"</span> to disable writing to the database (and no queries will be
  made), as <span style="font-family: monospace;">"yes"</span> to query whether to or not to write to the database, or as
  <span style="font-family: monospace;">"YES"</span> to automatically write the results to the database with no queries.
  When a query is given the responses may be <span style="font-family: monospace;">"no"</span> or <span style="font-family: monospace;">"yes"</span> for an individual
  spectrum or <span style="font-family: monospace;">"NO"</span> or <span style="font-family: monospace;">"YES"</span> for all remaining spectra without further
  queries.
  </p>
  <p>
  After a solution is found one may review and modify the line
  identifications and dispersion function using the graphical functions of
  the <b>identify</b> task (with the exception that a new spectrum may not be
  selected).  The review mode is selected with the <i>interactive</i>
  parameter.  If the parameter is <span style="font-family: monospace;">"no"</span> or <span style="font-family: monospace;">"NO"</span> then no interactive review
  will be provided and there will be no queries either.  If the parameter is
  <span style="font-family: monospace;">"YES"</span> then the graphical review mode will be entered after each solution is
  found without any query.  If the parameter is <span style="font-family: monospace;">"yes"</span> then a query will be
  made after a solution is found and after any log information is written to
  the terminal.  One may respond to the query with <span style="font-family: monospace;">"no"</span> or <span style="font-family: monospace;">"yes"</span> for an
  individual spectrum or <span style="font-family: monospace;">"NO"</span> or <span style="font-family: monospace;">"YES"</span> for all remaining spectra without
  further queries.  For <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"YES"</span> the <i>identify</i> review  mode is
  entered.  To exit type <span style="font-family: monospace;">'q'</span>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  The following example finds a dispersion solution for the middle column
  of a long slit spectrum of a He-Ne-Ar arc spectrum using all the
  interactive options.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; autoid arc0022 6000 6 coord=linelists$henear.dat sec="mid col"
  AUTOIDENITFY: NOAO/IRAF IRAFX valdes@puppis Thu 15:50:31 25-Jan-96
    Spectrum                # Found   Midpoint Dispersion        RMS
    arc0022[50,*]                50      5790.       6.17      0.322
  arc0022[50,*]: Examine identifications interactively?  (yes):
  arc0022[50,*]: Write results to database?  (yes): yes
  </pre></div>
  <p>
  2.  The next example shows a non-interactive mode with no queries for
  the middle fiber of an extracted multispec image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; autoid.coordlist="linelists$henear.dat"
  cl&gt; autoid a0003 5300 3.2 interactive- verbose- dbwrite=YES
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_AUTOIDENTIFY">
  <dt><b>AUTOIDENTIFY V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='AUTOIDENTIFY' Line='AUTOIDENTIFY V2.11' -->
  <dd>This task is new in this version.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  identify, reidentify, aidpars, linelists, center1d, icfit, gtools
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SUMMARY' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

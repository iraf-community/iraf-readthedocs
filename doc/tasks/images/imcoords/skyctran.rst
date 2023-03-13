.. _skyctran:

skyctran: Transform coordinates from one celestial wcs to another
=================================================================

**Package: imcoords**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  skyctran input output insystem outsystem
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The source of the input coordinates. The options are:
  <dl>
  <dt><b>&lt;filename&gt;</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='&lt;filename&gt;' -->
  <dd>The list of input coordinate files. Coordinates may be entered by hand by
  setting input to <span style="font-family: monospace;">"STDIN"</span>. A STDIN coordinate list is terminated by typing
  q or &lt;EOF&gt; (usually &lt;ctrl/d&gt; or &lt;ctrl/z&gt;).
  </dd>
  </dl>
  <dl>
  <dt><b>imcursor</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='imcursor' Line='imcursor' -->
  <dd>If the input file name is equal to the reserved keyword <span style="font-family: monospace;">"imcursor"</span> the input
  coordinates are read from the image cursor and the input coordinate system
  is the coordinate system of the image specified by the insystem parameter.
  The coordinate list is terminated by typing q or  &lt;EOF&gt; (usually &lt;ctrl/d&gt; or
  &lt;ctr/z&gt;).
  </dd>
  </dl>
  <dl>
  <dt><b>grid</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='grid' Line='grid' -->
  <dd>If the input file name is equal to the reserved
  keyword <span style="font-family: monospace;">"grid"</span>, an <i>nilng</i> by <i>nilat</i> grid of equally spaced
  input coordinates
  is generating spanning the region defined by <i>ilngmin</i>, <i>ilngmax</i>,
  <i>ilatmin</i>, <i>ilatmax</i>.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The list of output coordinate files. The number of output files must be
  equal to one or the number of input files. Results may be printed on the
  terminal by setting output to <span style="font-family: monospace;">"STDOUT"</span>.
  </dd>
  </dl>
  <dl id="l_insystem">
  <dt><b>insystem, outsystem</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='insystem' Line='insystem, outsystem' -->
  <dd>The input and output celestial coordinate systems. The options are
  the following:
  <dl>
  <dt><b>&lt;imagename&gt; [wcs]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='&lt;imagename&gt; [wcs]' -->
  <dd>The celestial coordinate system is the world coordinate system of the image
  &lt;imagename&gt; and the input or output pixel coordinates may be in the
  <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, <span style="font-family: monospace;">"physical"</span> or <span style="font-family: monospace;">"world"</span> coordinate systems. If wcs is not
  specified <span style="font-family: monospace;">"logical"</span> is assumed, unless the input coordinates are read from the
  image cursor, in which case <span style="font-family: monospace;">"tv"</span> is assumed. The image celestial coordinate
  system must be one of the valid FITS celestial coordinate systems:
  equatorial (FK4, FK4-NO-E, FK5, ICRS, or GAPPT), ecliptic, galactic, or
  supergalactic.
  </dd>
  </dl>
  <dl>
  <dt><b>icrs [equinox] [epoch]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='icrs' Line='icrs [equinox] [epoch]' -->
  <dd>The International Celestial Reverence System where equinox is
  a Julian or Besselian epoch e.g. J2000.0  or B1980.0.
  Equinoxes without the J / j or B / b prefix are treated as Julian epochs.
  The default value of equinox is J2000.0.
  Epoch is a Besselian epoch, a Julian epoch, or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Julian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian date.  If undefined epoch defaults to equinox.
  </dd>
  </dl>
  <dl>
  <dt><b>equinox [epoch]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='equinox' Line='equinox [epoch]' -->
  <dd>The equatorial mean place post-IAU 1976 (FK5) system if equinox is a
  Julian epoch, e.g. J2000.0 or 2000.0, or the equatorial mean place
  pre-IAU 1976 system (FK4) if equinox is a Besselian epoch, e.g. B1950.0
  or 1950.0. Julian equinoxes are prefixed by a J or j, Besselian equinoxes
  by a B or b. Equinoxes without the J / j or B / b prefix are treated as
  Besselian epochs if they are &lt; 1984.0, Julian epochs if they are &gt;= 1984.0.
  Epoch is the epoch of the observation and may be a Julian
  epoch, a Besselian epoch, or a Julian date. Julian epochs
  are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to the epoch type of
  equinox if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian date.  If undefined epoch defaults to equinox.
  </dd>
  </dl>
  <dl>
  <dt><b>fk5 [equinox] [epoch] </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='fk5' Line='fk5 [equinox] [epoch] ' -->
  <dd>The equatorial mean place post-IAU 1976 (FK5) system where equinox is
  a Julian or Besselian epoch e.g. J2000.0  or B1980.0.
  Equinoxes without the J / j or B / b prefix are treated as Julian epochs.
  The default value of equinox is J2000.0.
  Epoch is a Besselian epoch, a Julian epoch, or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Julian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian date.  If undefined epoch defaults to equinox.
  </dd>
  </dl>
  <dl>
  <dt><b>fk4 [equinox] [epoch]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='fk4' Line='fk4 [equinox] [epoch]' -->
  <dd>The equatorial mean place pre-IAU 1976 (FK4) system where equinox is a
  Besselian or Julian epoch e.g. B1950.0  or J2000.0,
  and epoch is the Besselian epoch, the Julian epoch, or the Julian date of the
  observation.
  Equinoxes without the J / j or B / b prefix are treated
  as Besselian epochs. The default value of equinox is B1950.0. Epoch
  is a Besselian epoch, a Julian epoch, or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Besselian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian date.  If undefined epoch defaults to equinox.
  </dd>
  </dl>
  <dl>
  <dt><b>noefk4 [equinox] [epoch]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='noefk4' Line='noefk4 [equinox] [epoch]' -->
  <dd>The equatorial mean place pre-IAU 1976 (FK4) system but without the E-terms
  where equinox is a Besselian or Julian epoch e.g. B1950.0 or J2000.0,
  and epoch is the Besselian epoch, the Julian epoch, or the Julian date of the
  observation.
  Equinoxes without the J / j or B / b prefix are treated
  as Besselian epochs. The default value of equinox is B1950.0.
  Epoch is a Besselian epoch, a Julian epoch, or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Besselian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian day.  If undefined epoch defaults to equinox.
  </dd>
  </dl>
  <dl>
  <dt><b>apparent epoch </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='apparent' Line='apparent epoch ' -->
  <dd>The equatorial geocentric apparent place post-IAU 1976 system where
  epoch is the epoch of observation.
  Epoch is a Besselian epoch, a Julian epoch or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Besselian
  epochs if the epoch value &lt; 1984.0, Julian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian date.
  </dd>
  </dl>
  <dl>
  <dt><b>ecliptic epoch</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='ecliptic' Line='ecliptic epoch' -->
  <dd>The ecliptic coordinate system where epoch is the epoch of observation.
  Epoch is a Besselian epoch, a Julian epoch, or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Besselian epochs
  if the epoch values &lt; 1984.0, Julian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian day.
  </dd>
  </dl>
  <dl>
  <dt><b>galactic [epoch]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='galactic' Line='galactic [epoch]' -->
  <dd>The IAU 1958 galactic coordinate system.
  Epoch is a Besselian epoch, a Julian epoch or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Besselian
  epochs if the epoch value &lt; 1984.0, Julian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian date. The default value of epoch is B1950.0.
  </dd>
  </dl>
  <dl>
  <dt><b>supergalactic [epoch]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='supergalactic' Line='supergalactic [epoch]' -->
  <dd>The deVaucouleurs supergalactic coordinate system.
  Epoch is a Besselian epoch, a Julian epoch or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Besselian
  epochs if the epoch value &lt; 1984.0, Julian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian date. The default value of epoch is B1950.0.
  </dd>
  </dl>
  In all the above cases fields in [] are optional with the defaults as
  described. The epoch field for fk5, icrs, galactic, and supergalactic
  coordinate systems is required only if the input coordinates are in the
  equatorial fk4, noefk4, fk5, or icrs systems and proper motions are defined.
  </dd>
  </dl>
  <dl id="l_transform">
  <dt><b>transform = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='transform' Line='transform = no' -->
  <dd>If transform = no the computed output coordinates are appended to the
  input line and the new extended line is written to the output file. If
  transform = yes the computed output coordinates replace
  the input coordinates in the input line and the edited line is written
  to the output file. Transform is always set to <span style="font-family: monospace;">"no"</span> if the input
  is from the unredirected standard input.
  </dd>
  </dl>
  <dl id="l_lngcolumn">
  <dt><b>lngcolumn = 1, latcolumn = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngcolumn' Line='lngcolumn = 1, latcolumn = 2' -->
  <dd>The columns in the input file containing the x/ra/longitude and
  y/dec/latitude coordinates. Lngcolumn and latcolumn are always 1 and
  2 if the input is from the unredirected standard input.
  </dd>
  </dl>
  <dl id="l_plngcolumn">
  <dt><b>plngcolumn = INDEF, platcolumn = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plngcolumn' Line='plngcolumn = INDEF, platcolumn = INDEF' -->
  <dd>The columns in the input file containing the ra and dec proper motions
  in arcsec / year. If plngcolumn and platcolumn are INDEF the proper motions
  are assumed to be undefined. Proper motions
  are used only if the input coordinate system is equatorial fk4, noefk4,
  fk5, or icrs.  Plngcolumn and platcolumn are always 3 and 4 if the input is from
  the unredirected standard input.
  </dd>
  </dl>
  <dl id="l_pxcolumn">
  <dt><b>pxcolumn = INDEF, rvcolumn = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pxcolumn' Line='pxcolumn = INDEF, rvcolumn = INDEF' -->
  <dd>The columns in the input file containing the parallax and radial velocity in
  in arcsec and km / sec respectively. If pxcolumn and rvcolumn are INDEF, the 
  parallax and radial velocities are assumed to be 0.0 and 0.0.
  Parallaxes and radial velocities are only used if proper motions are
  defined. Pxcolumn and rvcolumn are always 5 and 6 if the input is from the
  unredirected standard input.
  </dd>
  </dl>
  <dl id="l_ilngmin">
  <dt><b>ilngmin = INDEF, ilngmax = INDEF, ilatmin = INDEF, ilatmax = INDEF </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ilngmin' Line='ilngmin = INDEF, ilngmax = INDEF, ilatmin = INDEF, ilatmax = INDEF ' -->
  <dd>The lower and upper limits of the coordinate grid if <i>input</i> =
  <span style="font-family: monospace;">"grid"</span>.
  Ilngmin and ilngmax default to 1.0, 1.0, 0.0, 0.0, 0.0 and, 2048.0, ncols, 24.0,
  360.0, and TWOPI for coordinates in units of INDEF, pixels, hours, degrees,
  and radians respectively. Ilatmin and ilatmax default to 1.0, 1.0,
  -90.0, -90.0, -HALFPI and, 2048.0, nlines, 90.0, 90.0, and HALFPI
  for units of INDEF, pixels, degrees, degrees, and radians respectively.
  </dd>
  </dl>
  <dl id="l_nilng">
  <dt><b>nilng = 10, nilat = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nilng' Line='nilng = 10, nilat = 10' -->
  <dd>The size of the computed coordinate grid if <i>input</i> = <span style="font-family: monospace;">"grid"</span>.
  </dd>
  </dl>
  <dl id="l_ilngunits">
  <dt><b>ilngunits = <span style="font-family: monospace;">""</span>, ilatunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ilngunits' Line='ilngunits = "", ilatunits = ""' -->
  <dd>The units of the input ra/longitude and dec/latitude coordinates.
  The options are:
  <dl>
  <dt><b>hours</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='hours' Line='hours' -->
  <dd>Read the sky coordinates in hours.
  </dd>
  </dl>
  <dl>
  <dt><b>degrees</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='degrees' Line='degrees' -->
  <dd>Read the sky coordinates in degrees.
  </dd>
  </dl>
  <dl>
  <dt><b>radians</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='radians' Line='radians' -->
  <dd>Read the sky coordinates in radians.
  </dd>
  </dl>
  If the input system is the &lt;imagename&gt; [logical/tv/physical]
  system, pixel units are assumed regardless of the values
  of ilngunits or ilatunits.  The default ilngunits and
  ilatunits values are
  hours and degrees for the equatorial coordinate systems and degrees and
  degrees for the remaining sky coordinate systems.
  </dd>
  </dl>
  <dl id="l_ilngformat">
  <dt><b>ilngformat = <span style="font-family: monospace;">""</span>, ilatformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ilngformat' Line='ilngformat = "", ilatformat = ""' -->
  <dd>The output format of the input x/ra/longitude and y/dec/latitude coordinates
  if <i>input</i> = <span style="font-family: monospace;">"grid"</span>.
  The options are discussed in the formats section of the help page below.
  If the input coordinate system is the &lt;imagename&gt; [logical/tv/physical]
  system, default formats of %10.3f and %10.3f are assumed regardless
  of the values of ilngunits and ilatunits. Otherwise default formats
  of %12.3h, %12.2h, and %13.7g are assumed for input units of <span style="font-family: monospace;">"hours"</span>, <span style="font-family: monospace;">"degrees"</span>,
  and <span style="font-family: monospace;">"radians"</span> respectively. For values of <i>input</i> other than <span style="font-family: monospace;">"grid"</span>
  the output formats of the input coordinates are the same as the input
  formats.
  </dd>
  </dl>
  <dl id="l_olngunits">
  <dt><b>olngunits = <span style="font-family: monospace;">""</span>, olatunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='olngunits' Line='olngunits = "", olatunits = ""' -->
  <dd>The units of the output ra/longitude and dec/latitude coordinates.
  The options are:
  <dl>
  <dt><b>hours</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='hours' Line='hours' -->
  <dd>Output the sky coordinates in hours.
  </dd>
  </dl>
  <dl>
  <dt><b>degrees</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='degrees' Line='degrees' -->
  <dd>Output the sky coordinates in degrees.
  </dd>
  </dl>
  <dl>
  <dt><b>radians</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='radians' Line='radians' -->
  <dd>Output the sky coordinates in radians.
  </dd>
  </dl>
  If the output system is the &lt;imagename&gt; [logical/tv/physical]
  system, pixel units are assumed regardless of the values
  of olngunits or olatunits.  The default olngunits and
  olatunits values are
  hours and degrees for the equatorial coordinate systems and degrees and
  degrees for the remaining sky coordinate systems.
  </dd>
  </dl>
  <dl id="l_olngformat">
  <dt><b>olngformat = <span style="font-family: monospace;">""</span>, olatformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='olngformat' Line='olngformat = "", olatformat = ""' -->
  <dd>The format of the computed x/ra/longitude and y/dec/latitude coordinates.
  The options are discussed in the formats section of the help page below.
  If the output coordinate system is the &lt;imagename&gt; [logical/tv/physical]
  system, default formats of %10.3f and %10.3f are assumed regardless
  of the values of olngunits and olatunits. Otherwise default formats
  of %12.3h, %12.2h, and %13.7g are assumed for output units of <span style="font-family: monospace;">"hours"</span>,
  <span style="font-family: monospace;">"degrees"</span>, and <span style="font-family: monospace;">"radians"</span> respectively.
  </dd>
  </dl>
  <dl id="l_icommands">
  <dt><b>icommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='icommands' Line='icommands = ""' -->
  <dd>The default image display cursor.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about actions taken by the task on the standard output?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  SKYCTRAN converts coordinates in the input files
  <i>input</i> from the input celestial coordinate system <i>insystem</i>
  to the output celestial coordinate system <i>outsystem</i> and writes the
  converted coordinates to the output files <i>output</i>. The input
  files may be simple text files, the standard input <span style="font-family: monospace;">"STDIN"</span>,
  the image display cursor <span style="font-family: monospace;">"imcursor"</span>, or a user specified coordinate grid.
  The output files may be simple
  text files or the standard output <span style="font-family: monospace;">"STDOUT"</span>. SKYCTRAN may be used
  to change the units of the input coordinates, e.g. from degrees and degrees
  to hours and degrees, to precess the coordinates, to convert from one
  celestial coordinate system to another, e.g. from equatorial to ecliptic
  coordinates and vice versa, and to locate common objects in
  images whose fundamental coordinate systems are the same but observed at
  different epochs, e.g. FK4 B1950.0 and FK4 B1975.0, or different, e.g.
  equatorial FK4 B1950.0 and galactic.
  </p>
  <p>
  The input data are read from columns <i>lngcolumn</i>, <i>latcolumn</i>,
  <i>plngcolumn</i>, <i>platcolumn</i>, <i>pxcolumn</i>, and <i>rvcolumn</i>
  in the input files and if <i>transform</i> = yes, the converted coordinates are
  written to the same columns in the output files. If <i>transform</i> = <span style="font-family: monospace;">"no"</span>,
  the converted coordinates are appended to the input line creating two
  additional columns in the output file. If the input file is the
  unredirected standard input then transpose is always <span style="font-family: monospace;">"no"</span>. Comment lines, blanks
  lines, and lines for which the input coordinates could not be successfully
  decoded are passed on to the output file without modification.
  </p>
  <p>
  The input and output celestial coordinate systems <i>insystem</i> and
  <i>outsystem</i> must be one of the following: equatorial, ecliptic, galactic, or
  supergalactic.  The equatorial systems must be one of: 1) FK4, the mean
  place pre-IAU 1976 system, 2) FK4-NO-E, the same as FK4 but without the
  E-terms, 3) FK5, the mean place post-IAU 1976 system, 4) ICRS,
  the International Celestial Reference System, 5) GAPPT, the geocentric
  apparent place in the post-IAU 1976 system. 
  </p>
  <p>
  If <i>insystem</i> or <i>outsystem</i> is an image name then the celestial
  coordinate system is read from the image header. SKYCTRAN assumes that
  the celestial coordinate system is represented in the image header by
  the FITS keywords CTYPE, CRPIX, CRVAL, CD (or alternatively CDELT / CROTA),
  RADECSYS, EQUINOX (or EPOCH), and MJD-WCS (or MJD_OBS or DATE-OBS). USERS
  SHOULD TAKE NOTE THAT MJD-WCS IS CURRENTLY NEITHER A STANDARD OR
  PROPOSED FUTS STANDARD KEYWORD. HOWEVER IT OR SOMETHING SIMILAR IS REQUIRED
  TO SPECIFY THE EPOCH OF THE COORDINATE SYSTEM WHICH MAY BE DIFFERENT
  FROM THE EPOCH OF THE OBSERVATION.
  </p>
  <p>
  The first four characters of the values of the ra/longitude and dec/latitude
  axis CTYPE keywords specify the celestial coordinate system.
  The permitted CTYPE values are RA--/DEC- for equatorial coordinate systems,
  ELON/ELAT for the ecliptic coordinate system, GLON/GLAT for the galactic
  coordinate system, and SLON/SLAT for the supergalactic coordinate system,
  </p>
  <p>
  If the image celestial coordinate system is equatorial, the value
  of the RADECSYS keyword specifies the fundamental equatorial system.
  The permitted values of RADECSYS are FK4, FK4-NO-E,
  FK5, ICRS, and GAPPT. If the RADECSYS keyword is not
  present in the image header, the values of the EQUINOX or EPOCH keywords
  in that order of precedence are used to determine the fundamental
  equatorial system. EQUINOX or EPOCH contain the
  epoch of the mean place and equinox for the FK4, FK4-NO-E, FK5, and ICRS
  systems, e.g 1950.0 or 2000.0. The default equatorial system is FK4 if
  EQUINOX or EPOCH &lt; 1984.0, FK5 if EQUINOX or EPOCH &gt;= 1984.0, and FK5 if
  RADECSYS, EQUINOX and EPOCH are undefined.
  If RADECSYS is defined but EQUINOX and EPOCH are not the equinox
  defaults to 1950.0 for the FK4 and FK4-NO-E systems and 2000.0 for the FK5
  and ICRS systems.
  The equinox value is interpreted as a Besselian epoch for the FK4 and
  FK4-NO-E systems and as a Julian epoch for the FK5 and ICRS systems. Users are
  strongly urged to use the EQUINOX keyword in preference to the EPOCH
  keyword if they must enter their own values of the equinox into
  the image header. The FK4 and
  FK4-NO-E systems are not inertial and therefore also require the epoch of the 
  observation (the time when the mean place was correct) in addition to the
  equinox.  The input coordinate system epoch of the observation is also required
  if the input coordinate system is FK4, FK4-NO-E, FK5, or ICRS and proper motions
  are supplied.
  The epoch is specified, in order of precedence, by the values of
  the keywords MJD-WCS or MJD-OBS containing the modified Julian date
  (JD - 2400000.5) of
  the coordinate system, or the DATE-OBS keyword containing
  the date of the observation in the form DD/MM/YY, CCYY-MM-DD, or
  CCYY-MM-DDTHH:MM:SS.S. As the latter quantity may
  only be accurate to a day, the MJD-WCS or MJD-OBS specifications are
  preferable. If both
  keywords are absent the epoch defaults to the value of equinox.
  Equatorial coordinates in the GAPPT system require
  only the specification of the epoch of observation which is supplied
  via the MJD-WCS, MJD-OBS or DATE-OBS keywords as for the FK4, FK4-NO-E, FK5,
  and ICRS systems.
  </p>
  <p>
  If the celestial coordinate system is ecliptic the mean ecliptic and equinox of
  date are required. They are supplied via the MJD-WCS, MJD-OBS or DATE-OBS
  keywords as for the equatorial FK4, FK4-NO-E, FK5, ICRS, and GAPPT systems.
  </p>
  <p>
  If, the output coordinate system is galactic or supergalactic, the input
  coordinate system is FK4, FK4-NO-E, FK5, or ICRS and proper motions are
  supplied with the input coordinates, then the output epoch of the
  observation is also required. This is supplied via the MJD-WCS, MJD-OBS or
  DATE-OBS keywords as for the equatorial FK4, FK4-NO-E, FK5, ICRS, GAPPT,
  and ecliptic systems.
  </p>
  <p>
  USERS NEED TO BE AWARE THAT THE IRAF IMAGE WORLD COORDINATE SYSTEM
  CURRENTLY (IRAF VERSIONS 2.10.4 PATCH 2 AND EARLIER) SUPPORTS ONLY THE
  EQUATORIAL SYSTEM (CTYPE (ra axis) = <span style="font-family: monospace;">"RA--XXXX"</span> CTYPE (dec axis) = <span style="font-family: monospace;">"DEC-XXXX"</span>)
  WHERE XXXX IS THE PROJECTION TYPE, EVEN THOUGH THE SKYCTRAN TASK 
  SUPPORTS GALACTIC, ECLIPTIC, AND SUPERGALACTIC COORDINATES.
  </p>
  <p>
  USERS SHOULD ALSO REALIZE THAT IMAGE WORLD COORDINATE SYSTEM REPRESENTATION
  IN FITS IS STILL IN THE DRAFT STAGE. ALTHOUGH SKYCTRAN TRIES TO CONFORM TO
  THE CURRENT DRAFT PROPOSAL WHERE NO ADOPTED STANDARDS CURRENTLY EXIST, THE
  FINAL FITS STANDARD MAY DIFFER FROM THE ONE ADOPTED HERE.
  </p>
  <p>
  The IRAF builtin world coordinate systems <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, <span style="font-family: monospace;">"physical"</span>, and
  world are also supported. This means for example that users can begin
  with cursor coordinates in image 1, use the image header of image 1
  to transform the pixel coordinates to the celestial coordinate system of
  image 1, convert the image 1 celestial coordinates to celestial coordinates
  in the image 2 celestial coordinate system, and finally transform the
  celestial coordinate system 2 coordinates to pixel coordinates in image 2,
  all in one step.
  </p>
  <p>
  The <i>logical coordinate system</i> is the pixel coordinate system of the
  current image. This coordinate system is the one used by the image
  input/output routines to access the image on disk. In the
  logical coordinate system,
  the coordinates of the pixel centers must lie within the following
  range: 1.0 &lt;= x[i] &lt;= nx[i], where x[i] is the coordinate in dimension i,
  nx[i] is the size of the image in dimension i, and the current maximum
  number of image dimensions is 7. In the case of an image section,
  the nx[i] refer to the dimensions of the section, not the dimensions
  of the full image.
  </p>
  <p>
  The <i>tv coordinate system</i> is the pixel coordinate system used by the
  display servers XIMTOOL, SAOIMAGE, and IMTOOL.
  For images which are not image sections
  the tv and logical coordinate systems are identical. For images which are
  image sections the tv and physical coordinate systems are identical if
  the image has not undergone any prior linear transformations such as
  axis flips, section copies, shifts, scale changes, rotations, etc.
  </p>
  <p>
  The <i>physical coordinate system</i> is the coordinate system in which the
  pixel coordinates of an object are invariant to successive linear
  transformations
  of the image. In this coordinate system, the pixel coordinates of an object
  in an image remain the same, regardless of any section copies, shifts,
  rotations, etc on the image. For example, an object with the
  physical coordinates (x,y) in an image would still have physical
  coordinates (x, y) in an image which is a section of the original image.
  </p>
  <p>
  The <i>world coordinate system</i> is the default coordinate system for the
  image. The default world coordinate system is the one named by the
  environment variable <span style="font-family: monospace;">"defwcs"</span> if defined in the user environment (initially
  it is undefined) and present in the image header; else it is the first
  world coordinate system
  defined for the image (the .imh and .hhh image format support only one wcs
  but the .qp format can support more); else it is the physical coordinate
  system.
  </p>
  <p>
  IF AN ERROR IS ENCOUNTERED WHEN DECODING THE INPUT OR OUTPUT WORLD COORDINATE
  SYSTEMS, THEN AN ERROR FLAG IS PRINTED IN THE OUTPUT FILE AND ON THE STANDARD
  OUTPUT IF <i>VERBOSE</i> IS YES, AND THE INPUT COORDINATES ARE COPIED TO THE
  OUTPUT COORDINATES WITHOUT CHANGE.
  </p>
  <p>
  <i>Ilngunits</i>, <i>ilatunits</i>, <i>olngunits</i>, and <i>olatunits</i>
  set the units of the input and output coordinate systems.
  If the input or output system is the &lt;imagename&gt; [logical/tv/physical]
  system pixel units are assumed regardless of the values
  of &lt;i/o&gt;lngunits or &lt;i/o&gt;latunits.  The default &lt;i/o&gt;lngunits and
  &lt;i/o&gt;latunits values are
  hours and degrees for the equatorial celestial coordinate system and
  degrees and degrees for the remaining celestial coordinate systems.
  </p>
  <p>
  The formats of the computed x/ra/longitude and y/dec/longitude coordinates
  are specified with the <i>olngformat</i> and <i>olatformat</i> parameters.
  The options are discussed in the formats section of the help page below.
  If the output coordinate system is the &lt;imagename&gt; [logical/tv/physical],
  default formats of %10.3f and %10.3f are assumed regardless
  of the values of olngunits and olatunits. Otherwise default formats
  of %12.3h, %12.2h, and %g are assumed for output units of <span style="font-family: monospace;">"hours"</span>, <span style="font-family: monospace;">"degrees"</span>,
  and <span style="font-family: monospace;">"radians"</span> respectively.
  </p>
  </section>
  <section id="s_user_commands">
  <h3>User commands</h3>
  <p>
  If the input file is STDIN the user can type in the input data by hand and
  set the input and output coordinate systems, the input and output coordinate
  units, and the output coordinate format interactively. The available commands
  are listed below.
  </p>
  <div class="highlight-default-notranslate"><pre>
          INTERACTIVE KEYSTROKE COMMANDS
  
  The following commands must be followed by a carriage return.
  
  ?       Print help
  :       Execute colon command
  data    Measure object
  q       Exit task
  
          VALID DATA STRING
  
  x/ra/long y/dec/lat [pmra pmdec [parallax radial velocity]]
  
  
          COLON COMMANDS
  
  The following commands must be followed by a carriage return.
  
  :show                           Show the input and output coordinate systems
  :isystem        [string]        Show / set the input coordinate system
  :osystem        [string]        Show / set the output coordinate system
  :iunits         [string string] Show / set the input coordinate units
  :ounits         [string string] Show / set the output coordinate units
  :oformat        [string string] Show / set the output coordinate format
  
          VALID INPUT AND OUTPUT COORDINATE SYSTEMS
  
  image [logical/tv/physical/world]
  equinox [epoch]
  noefk4 [equinox [epoch]]
  fk4 [equinox [epoch]]
  fk5 [equinox [epoch]]
  icrs [equinox [epoch]]
  apparent epoch
  ecliptic epoch
  galactic [epoch]
  supergalactic [epoch]
  
          VALID INPUT AND OUTPUT CELESTIAL COORDINATE UNITS
                    AND THEIR DEFAULT FORMATS
  
  hours           %12.3h
  degrees         %12.2h
  radians         %13.7h
  </pre></div>
  </section>
  <section id="s_image_cursor_commands">
  <h3>Image cursor commands</h3>
  <p>
  In interactive image cursor mode the user can set the input and output
  coordinate systems, the output coordinate units, and the output coordinate
  formats. The available commands are listed below.
  </p>
  <div class="highlight-default-notranslate"><pre>
          INTERACTIVE KEYSTROKE COMMANDS
  
  ?       Print help
  :       Execute colon command
  spbar   Measure object
  q       Exit task
  
          COLON COMMANDS
  
  :show                           Show the input and output coordinate systems
  :isystem        [string]        Show / set the input coordinate system
  :osystem        [string]        Show / set the output coordinate system
  :ounits         [string string] Show / set the output coordinate units
  :oformat        [string string] Show / set the output coordinate format
  
          VALID INPUT COORDINATE SYSTEMS
  
  image [tv]
  
          VALID OUTPUT COORDINATE SYSTEMS
  
  image [logical/tv/physical/world]
  equinox [epoch]
  noefk4 [equinox [epoch]]
  fk4 [equinox [epoch]]
  fk5 [equinox [epoch]]
  icrs [equinox [epoch]]
  apparent epoch
  ecliptic epoch
  galactic [epoch]
  supergalactic [epoch]
  
          VALID OUTPUT COORDINATE UNITS AND THEIR DEFAULT FORMATS
  
  hours           %12.3h
  degrees         %12.2h
  radians         %13.7g
  </pre></div>
  </section>
  <section id="s_formats">
  <h3>Formats</h3>
  <p>
  A  format  specification has the form <span style="font-family: monospace;">"%w.dCn"</span>, where w is the field
  width, d is the number of decimal places or the number of digits  of
  precision,  C  is  the  format  code,  and  n is radix character for
  format code <span style="font-family: monospace;">"r"</span> only.  The w and d fields are optional.  The  format
  codes C are as follows:
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  b       boolean (YES or NO)
  c       single character (c or '\c' or '\0nnn')
  d       decimal integer
  e       exponential format (D specifies the precision)
  f       fixed format (D specifies the number of decimal places)
  g       general format (D specifies the precision)
  h       hms format (hh:mm:ss.ss, D = no. decimal places)
  m       minutes, seconds (or hours, minutes) (mm:ss.ss)
  o       octal integer
  rN      convert integer in any radix N
  s       string (D field specifies max chars to print)
  t       advance To column given as field W
  u       unsigned decimal integer
  w       output the number of spaces given by field W
  x       hexadecimal integer
  z       complex format (r,r) (D = precision)
  
  Conventions for w (field width) specification:
  
      W =  n      right justify in field of N characters, blank fill
          -n      left justify in field of N characters, blank fill
          0n      zero fill at left (only if right justified)
  absent, 0       use as much space as needed (D field sets precision)
  
  Escape sequences (e.g. "\n" for newline):
  
  \b      backspace   (not implemented)
       formfeed
  \n      newline (crlf)
  \r      carriage return
  \t      tab
  \"      string delimiter character
  \'      character constant delimiter character
  \\      backslash character
  \nnn    octal value of character
  
  Examples
  
  %s          format a string using as much space as required
  %-10s       left justify a string in a field of 10 characters
  %-10.10s    left justify and truncate a string in a field of 10 characters
  %10s        right justify a string in a field of 10 characters
  %10.10s     right justify and truncate a string in a field of 10 characters
  
  %7.3f       print a real number right justified in floating point format
  %-7.3f      same as above but left justified
  %15.7e      print a real number right justified in exponential format
  %-15.7e     same as above but left justified
  %12.5g      print a real number right justified in general format
  %-12.5g     same as above but left justified
  
  %h          format as nn:nn:nn.n
  %15h        right justify nn:nn:nn.n in field of 15 characters
  %-15h       left justify nn:nn:nn.n in a field of 15 characters
  %12.2h      right justify nn:nn:nn.nn
  %-12.2h     left justify nn:nn:nn.nn
  
  %H          / by 15 and format as nn:nn:nn.n
  %15H        / by 15 and right justify nn:nn:nn.n in field of 15 characters
  %-15H       / by 15 and left justify nn:nn:nn.n in field of 15 characters
  %12.2H      / by 15 and right justify nn:nn:nn.nn
  %-12.2H     / by 15 and left justify nn:nn:nn.nn
  
  \n          insert a newline
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Additional information on the IRAF world coordinate systems can be found in
  the help pages for the WCSEDIT and WCRESET tasks.
  Detailed documentation for the IRAF world coordinate system interface MWCS
  can be found in the file <span style="font-family: monospace;">"iraf$sys/mwcs/MWCS.hlp"</span>. This file can be
  formatted and printed with the command <span style="font-family: monospace;">"help iraf$sys/mwcs/MWCS.hlp fi+ |
  lprint"</span>.
  </p>
  <p>
  Details of the FITS header world coordinate system interface can
  be found in the draft paper <span style="font-family: monospace;">"World Coordinate Systems Representations Within the
  FITS Format"</span> by Hanisch and Wells, available from the iraf anonymous ftp
  archive and the draft paper which supersedes it <span style="font-family: monospace;">"Representations of Celestial
  Coordinates in FITS"</span> by Greisen and Calabretta available from the NRAO
  anonymous ftp archives.
  </p>
  <p>
  The spherical astronomy routines employed here are derived from the Starlink
  SLALIB library provided courtesy of Patrick Wallace. These routines
  are very well documented internally with extensive references provided
  where appropriate. Interested users are encouraged to examine the routines
  for this information. Type <span style="font-family: monospace;">"help slalib"</span> to get a listing of the SLALIB
  routines, <span style="font-family: monospace;">"help slalib opt=sys"</span> to get a concise summary of the library,
  and <span style="font-family: monospace;">"help &lt;routine&gt;"</span> to get a description of each routine's calling sequence,
  required input and output, etc. An overview of the library can be found in the
  paper <span style="font-family: monospace;">"SLALIB - A Library of Subprograms"</span>, Starlink User Note 67.7
  by P.T. Wallace, available from the Starlink archives.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Precess the fk4 coordinates typed in by the user to the fk5 system with
  and without the proper motion values.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skyctran STDIN STDOUT fk4 fk5
  
  # Insystem: fk4  Coordinates: equatorial FK4
  #     Equinox: B1950.000 Epoch: B1950.00000000 MJD: 33281.92346
  # Outsystem: fk5  Coordinates: equatorial FK5
  #     Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  
  # Input file: STDIN  Output file: STDOUT
  
  ... not including proper motion
  13:28:43.2 27:18:01.1
  13:28:43.2 27:18:01.1 13:31:03.855  27:02:35.13
  
  ... including proper motion
  13:28:43.2 27:18:01.1 .36 -0.16
  13:28:43.2 27:18:01.1 .36 -0.16 13:31:05.215  27:02:27.37
  
  ... change the output coordinate system to fk5 1975.0 and repeat
  :os fk5 1975.0
  :os
  
  # Outsystem:  fk5 1975.0  Coordinates: equatorial FK5
  #     Equinox: J1975.000 Epoch: J1975.00000000 MJD: 42413.25000
  
  13:28:43.2 27:18:01.1
  13:28:43.2 27:18:01.1 13:29:53.564  27:10:17.69
  
  13:28:43.2 27:18:01.1 .36 -0.16
  13:28:43.2 27:18:01.1 .36 -0.16 13:29:54.244  27:10:13.80
  
  ... type EOF to quit
  &lt;EOF&gt;
  </pre></div>
  <p>
  2. Precess a list of RAS in hours and DECS in degrees in the FK5 system
  equinox 1980.0 to equinox 2000.0 and write both the input coordinates and
  the output coordinates in hours and degrees to the output file. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skyctran inlist outlist j1980.0 j2000.0
  
          ... or equivalently ...
  
  cl&gt; skyctran inlist outlist j1980.0 2000.0
  
          ... or equivalently ...
  
  cl&gt; skyctran inlist outlist "fk5 1980.0" fk5
  </pre></div>
  <p>
  Note that if the coordinate system, e.g. fk5, is not specified explicitly
  then equinoxes &lt; 1984 must be prefixed by J, or a Besselian rather than
  a Julian epoch will be assumed.
  </p>
  <p>
  3. Repeat the previous example but replace the input coordinates with
  the precessed coordinates in the output file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skyctran inlist outlist j1980.0 j2000.0 transform+
  </pre></div>
  <p>
  4. Precess a list of RAS in hours and DECS in degrees in the FK4 system
  equinox 1950.0 to equinox 1975.0 and write both the input coordinates and
  the output coordinates in hours and degrees to the output file. The input
  and output epochs of observation default to the respective equinox
  values.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skyctran inlist outlist 1950.0 1975.0
  
          ... or equivalently ...
  
  cl&gt; skyctran inlist outlist b1950.0 b1975.0
  
          ... or equivalently ...
  
  cl&gt; skyctran inlist outlist fk4 b1975.0
  
          ... or equivalently ...
  
  cl&gt; skyctran inlist outlist fk4 "fk4 1975.0"
  </pre></div>
  <p>
  5. Convert a list of RAS in hours and DECS in degrees in the FK4 system
  equinox 1950.0 to RAS in hours and DECS in degrees in the FK5 system
  equinox 2000.0, and replace the input coordinates with the
  output coordinates in the output file. The Besselian epoch of the
  observation is 1987.25.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skyctran inlist outlist "b1950.0 1987.25" j2000.0 \
      transform+
  </pre></div>
  <p>
  6. Convert a list of RAS in hours and DECS in degrees to RAS in degrees
  and DECS in degrees, and replace the input coordinates with the output
  coordinates in the output file. As the input and output coordinate systems
  and equinoxes are the same no precession is performed.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skyctran inlist outlist 2000.0 2000.0 olngunits=degrees \
      transform+
  </pre></div>
  <p>
  7. Convert a list of RAS in hours and DECS in degrees in the FK4
  system, equinox 1950.0, epoch of observation 1987.24, to galactic
  coordinates, and write both the input and output coordinate to the
  output file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skyctran inlist outlist "b1950.0 1987.25" galactic
  </pre></div>
  <p>
  8. Convert a list of RAS in hours and DECS in degrees in the FK5
  system, equinox 2000.0, to ecliptic coordinates on Julian date
  2449879.5, replacing the input coordinates with the converted
  coordinates in the output file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skyctran inlist outlist j2000 "ecliptic 2449879.5" \
      transform+
  </pre></div>
  <p>
  9. Display an image and use the cursor and image header coordinate
  system, equatorial FK4, equinox 1950.0, epoch 1987.25  to print the pixel
  and galactic coordinates of the marked objects on the image display.
  Note that the test image dev$wpix has an incorrect value of EPOCH (0.0) that
  would have confused skyctran and need to be changed.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imcopy dev$wpix wpix
  cl&gt; hedit wpix epoch 1950.0
  cl&gt; display wpix 1 fi+
  cl&gt; skyctran imcursor STDOUT wpix galactic
  </pre></div>
  <p>
  10. Convert a list of RAS in hours and DECS in degrees measured in the
  image created in example 9 to the FK5 equinox 2000.0 coordinate system.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skyctran inlist outlist "wpix world" j2000.0
  
             ... or equivalently ...
  
  cl&gt; skyctran inlist outlist "b1950.0 1987.25" j2000.0
  </pre></div>
  <p>
  11. Using an image whose header coordinate system is equatorial FK5
  equinox 2000.0 and a different image of the same region whose coordinate
  system is galactic use the image display and cursor to create a list of
  tie points in logical pixel coordinates that can be used as input to the
  registration tasks geomap and geotran. Note that this example  and examples
  12 and 13 below will not work on iraf system earlier than 2.11 because galactic
  image header coordinates are not fully supported. They will work
  however on two images which have equatorial coordinates systems
  which are precessed with respect to each other.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; display image1
  
      ... this is the reference image
  
  cl&gt; skyctran imcursor outlist image1 "image2 logical"
  
      ... mark many widely scattered points on the displayed
          image image1 terminating the input list with
          &lt;EOF&gt; which is usually &lt;ctrl/z&gt; or &lt;ctrl/d&gt;
  </pre></div>
  <p>
  12. Repeat example 11 but use a previously prepared list of image1
  logical pixel coordinates as input to the task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skyctran inlist outlist "image1 logical"\
      "image2 logical"
  </pre></div>
  <p>
  13. Repeat example 11 but have skyctran automatically generate a grid
  of 100 tie points.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skyctran grid outlist "image1 logical"\
      "image2 logical"
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  setjd,precess,galactic,xray.xspatial.skypix,stsdas.toolbox.tools.tprecess
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'USER COMMANDS' 'IMAGE CURSOR COMMANDS' 'FORMATS' 'REFERENCES' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

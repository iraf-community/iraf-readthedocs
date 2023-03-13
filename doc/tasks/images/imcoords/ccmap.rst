.. _ccmap:

ccmap: Compute image plate solutions using matched coordinate lists
===================================================================

**Package: imcoords**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ccmap input database
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The input text files containing the pixel and celestial coordinates of
  points in the input images. The coordinates are listed one per line with x, y,
  ra / longitude, and dec / latitude in the columns specified by the
  <i>xcolumn</i>, <i>ycolumn</i>, <i>lngcolumn</i>, and <i>latcolumn</i> parameters
  respectively.  Whether all files are combined to produce one solution or
  each file produces a separate solution depends on whether there is a
  matching list of output <i>solutions</i> names or <i>results</i> files.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>The text database file where the computed plate solutions are stored.
  </dd>
  </dl>
  <dl id="l_solutions">
  <dt><b>solutions = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='solutions' Line='solutions = ""' -->
  <dd>An optional list of plate solution names. If there are multiple input
  coordinate files and no name or a single name is specified then the
  input coordinates are combined to produce a single solution.  Otherwise
  the list must match the number of input coordinate files.  If no names are
  supplied then the database records are assigned the names of the input
  images <i>images</i>, or the names of the coordinate files <i>input</i>.
  In the case of multiple coordinate files the first image or input is used.
  </dd>
  </dl>
  <dl id="l_images">
  <dt><b>images = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images = ""' -->
  <dd>The images associated with the input coordinate files. The number of images
  must be zero or equal to the number of input coordinate files. If an input
  image exists and the <i>update</i> parameter is enabled, the image wcs will
  be created from the linear component of the computed plate solution
  and written to the image header.
  </dd>
  </dl>
  <dl id="l_results">
  <dt><b>results = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='results' Line='results = ""' -->
  <dd>Optional output files containing a summary of the results including a
  description of the plate geometry and a listing of the input coordinates,
  the fitted coordinates, and the fit residuals. The number of
  results files must be zero, one or equal to the number of input files. If
  results is <span style="font-family: monospace;">"STDOUT"</span> the results summary is printed on the standard output.
  If there are multiple input coordinate files and zero or one output is
  specified then the input coordinates are combined to produce a single solution.
  </dd>
  </dl>
  <dl id="l_xcolumn">
  <dt><b>xcolumn = 1, ycolumn = 2, lngcolumn = 3, latcolumn = 4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcolumn' Line='xcolumn = 1, ycolumn = 2, lngcolumn = 3, latcolumn = 4' -->
  <dd>The input coordinate file columns containing the x, y, ra / longitude and
  dec / latitude values.
  </dd>
  </dl>
  <dl id="l_xmin">
  <dt><b>xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmin' Line='xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF' -->
  <dd>The range of x and y pixel coordinates over which the computed coordinate
  transformation is valid. These limits should be left at INDEF or set to
  the values of the column and row limits of the input images, e.g xmin = 1.0,
  xmax = 512, ymin= 1.0, ymax = 512 for a 512 x 512 image.  If xmin, xmax, ymin,
  or ymax are undefined, they are set to the minimum and maximum x and y
  pixels values in <i>input</i>.
  </dd>
  </dl>
  <dl id="l_lngunits">
  <dt><b>lngunits = <span style="font-family: monospace;">""</span>, latunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngunits' Line='lngunits = "", latunits = ""' -->
  <dd>The units of the input ra / longitude and dec / latitude coordinates. The
  options are <span style="font-family: monospace;">"hours"</span>, <span style="font-family: monospace;">"degrees"</span>, and <span style="font-family: monospace;">"radians"</span> for ra / longitude, and
  <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"radians"</span> for dec / latitude. If the lngunits and latunits
  are undefined they default to the preferred units for the coordinate system
  specified by <i>insystem</i>, e.g. <span style="font-family: monospace;">"hours"</span> and <span style="font-family: monospace;">"degrees"</span> for equatorial
  systems, and <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"degrees"</span> for ecliptic, galactic, and
  supergalactic systems.
  </dd>
  </dl>
  <dl id="l_insystem">
  <dt><b>insystem = <span style="font-family: monospace;">"j2000"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='insystem' Line='insystem = "j2000"' -->
  <dd>The input celestial coordinate system. The <i>insystem</i> parameter
  sets the preferred units for the input celestial coordinates,
  tells CCMAP how to transform the celestial coordinates of the reference
  point from the reference point coordinate system to the input coordinate
  system, and sets the correct values of the image header keywords CTYPE,
  RADECSYS, EQUINOX, and MJD-WCS if the image header wcs is updated. The 
  systems of most interest to users are <span style="font-family: monospace;">"icrs"</span>, <span style="font-family: monospace;">"j2000"</span>, and <span style="font-family: monospace;">"b1950"</span> which
  stand for the ICRS J2000.0, FK5 J2000.0 and FK4 B1950.0 celestial coordinate
  systems respectively.  The full set of options are the following:
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
  <dt><b>icrs [equinox] [epoch]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='icrs' Line='icrs [equinox] [epoch]' -->
  <dd>The International Celestial Reference System where equinox is
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
  described. The epoch field for the icrs, fk5, galactic, and supergalactic
  coordinate systems is only used if the input coordinates are in the
  equatorial fk4, noefk4, fk5, or icrs systems and proper motions are supplied.
  Since CCMAP does not currently support proper motions these fields are
  not required.
  </dd>
  </dl>
  <dl id="l_refpoint">
  <dt><b>refpoint = <span style="font-family: monospace;">"coords"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refpoint' Line='refpoint = "coords"' -->
  <dd>The definition of the sky projection reference point in celestial coordinates,
  e.g. the tangent point in the case of the usual tangent plane projection.
  The options are:
  <dl>
  <dt><b>coords</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='coords' Line='coords' -->
  <dd>The celestial coordinates of the reference point are set to the mean of the 
  input celestial coordinates, e.g. the mean of ra / longitude and dec /
  latitude coordinates. If the true tangent point is reasonably close to
  the center of the input coordinate distribution and the input is not
  too large, this approximation is reasonably accurate.
  </dd>
  </dl>
  <dl>
  <dt><b>user</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='user' Line='user' -->
  <dd>The values of the keywords <i>lngref</i>, <i>latref</i>, <i>refsystem</i>,
  <i>lngrefunits</i>, and <i>latrefunits</i> are used to determine the celestial
  coordinates of the reference point.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_xref">
  <dt><b>xref = <span style="font-family: monospace;">"INDEF"</span>, yref = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xref' Line='xref = "INDEF", yref = "INDEF"' -->
  <dd>The reference pixel may be specified as a value or image header keyword.
  In the latter case a reference image must be specified.  By specifying
  the reference pixel the solution will be constrained to putting the
  reference coordinate at that point.
  </dd>
  </dl>
  <dl id="l_lngref">
  <dt><b>lngref = <span style="font-family: monospace;">"INDEF"</span>, latref = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngref' Line='lngref = "INDEF", latref = "INDEF"' -->
  <dd>The ra / longitude and dec / latitude of the reference point(s).  Lngref
  and latref may be numbers, e.g 13:20:42.3 and -33:41:26 or keywords for the
  appropriate parameters in the image header, e.g. RA/DEC or CRVAL1/CRVAL2.
  Each parameter may be a list to apply different reference points to
  each input coordinate list.  If lngref and latref are undefined then
  the position of the reference point defaults to the mean of the input
  coordinates.
  </dd>
  </dl>
  <dl id="l_refsystem">
  <dt><b>refsystem = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refsystem' Line='refsystem = "INDEF"' -->
  <dd>The celestial coordinate system of the reference point. Refsystem may
  be any one of the options listed under the <i>insystem</i> parameter, e.g.
  <span style="font-family: monospace;">"b1950"</span>, or an image header keyword containing the epoch of the observation
  in years, e.g. EPOCH for NOAO data. In the latter case the coordinate system is
  assumed to be equatorial FK4 at equinox EPOCH. If refsystem is undefined
  the celestial coordinate system of the reference point defaults to the
  celestial coordinate system of the input coordinates <i>insystem</i>.
  </dd>
  </dl>
  <dl id="l_lngrefunits">
  <dt><b>lngrefunits = <span style="font-family: monospace;">""</span>, latrefunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngrefunits' Line='lngrefunits = "", latrefunits = ""' -->
  <dd>The units of the reference point celestial  coordinates. The options
  are <span style="font-family: monospace;">"hours"</span>, <span style="font-family: monospace;">"degrees"</span>, and <span style="font-family: monospace;">"radians"</span> for the ra / longitude coordinates,
  and <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"radians"</span> for the dec /latitude coordinates. 
  If lngunits and latunits are undefined they default to the  units of the
  input coordinate system.
  </dd>
  </dl>
  <dl id="l_projection">
  <dt><b>projection = <span style="font-family: monospace;">"tan"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='projection' Line='projection = "tan"' -->
  <dd>The sky projection geometry. The most commonly used projections in astronomy
  are <span style="font-family: monospace;">"tan"</span>, <span style="font-family: monospace;">"arc"</span>, <span style="font-family: monospace;">"sin"</span>, and <span style="font-family: monospace;">"lin"</span>. Other supported  standard projections
  are <span style="font-family: monospace;">"ait"</span>, <span style="font-family: monospace;">"car"</span>,<span style="font-family: monospace;">"csc"</span>, <span style="font-family: monospace;">"gls"</span>, <span style="font-family: monospace;">"mer"</span>, <span style="font-family: monospace;">"mol"</span>, <span style="font-family: monospace;">"par"</span>, <span style="font-family: monospace;">"pco"</span>, <span style="font-family: monospace;">"qsc"</span>, <span style="font-family: monospace;">"stg"</span>,
  <span style="font-family: monospace;">"tsc"</span>, and <span style="font-family: monospace;">"zea"</span>. A new experimental function <span style="font-family: monospace;">"tnx"</span>, a combination of the
  tangent plate projection and polynomials, is also available.
  </dd>
  </dl>
  <dl id="l_fitgeometry">
  <dt><b>fitgeometry = <span style="font-family: monospace;">"general"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitgeometry' Line='fitgeometry = "general"' -->
  <dd>The plate solution geometry to be used. The options are the following, where
  xi and eta refer to the usual standard coordinates used in astrometry.
  <dl>
  <dt><b>shift</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='shift' Line='shift' -->
  <dd>Xi and eta shifts only are fit.
  </dd>
  </dl>
  <dl>
  <dt><b>xyscale</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='xyscale' Line='xyscale' -->
  <dd>Xi and eta shifts and x and y magnification factors in arcsec / pixel are fit.
  Axis flips are allowed for.
  </dd>
  </dl>
  <dl>
  <dt><b>rotate</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='rotate' Line='rotate' -->
  <dd>Xi and eta shifts and a rotation angle are fit. Axis flips are allowed for.
  </dd>
  </dl>
  <dl>
  <dt><b>rscale</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='rscale' Line='rscale' -->
  <dd>Xi and eta shifts, a magnification factor in arcsec / pixel assumed to be the same
  in x and y, and a rotation angle are fit. Axis flips are allowed for.
  </dd>
  </dl>
  <dl>
  <dt><b>rxyscale</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='rxyscale' Line='rxyscale' -->
  <dd>Xi and eta shifts, x and y magnifications factors in arcsec / pixel, and a rotation
  angle are fit.  Axis flips are allowed for.
  </dd>
  </dl>
  <dl>
  <dt><b>general</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='general' Line='general' -->
  <dd>A polynomial of arbitrary order in x and y is fit. A linear term and a
  distortion term are computed separately. The linear term includes a xi and eta
  shift, an x and y scale factor in arcsec / pixel, a rotation and a skew.  Axis
  flips are also allowed for in the linear portion of the fit. The distortion
  term consists of a polynomial fit to the residuals of the linear term. By
  default the distortion term is set to zero.
  </dd>
  </dl>
  For all the fitting geometries except <span style="font-family: monospace;">"general"</span> no distortion term is fit,
  i.e. the x and y polynomial orders are assumed to be 2 and the cross term
  switches are assumed to be set to <span style="font-family: monospace;">"none"</span>, regardless of the values of the
  <i>xxorder</i>, <i>xyorder</i>, <i>xxterms</i>, <i>yxorder</i>, <i>yyorder</i>
  and <i>yxterms</i> parameters set by the user.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"polynomial"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "polynomial"' -->
  <dd>The type of analytic coordinate surface to be fit. The options are the
  following.
  <dl>
  <dt><b>legendre</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='legendre' Line='legendre' -->
  <dd>Legendre polynomials in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>chebyshev</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='chebyshev' Line='chebyshev' -->
  <dd>Chebyshev polynomials in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>polynomial</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='polynomial' Line='polynomial' -->
  <dd>Power series polynomials in x and y.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_xxorder">
  <dt><b>xxorder = 2, xyorder = 2,  yxorder = 2, yyorder = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xxorder' Line='xxorder = 2, xyorder = 2,  yxorder = 2, yyorder = 2' -->
  <dd>The order of the polynomials in x and y for the xi and eta fits respectively.
  The default order and cross term settings define the linear term in x
  and y, where the 6 coefficients can be interpreted in terms of an xi and eta
  shift, an x and y scaling in arcsec / pixel, and rotations of the x and y axes.
  The <span style="font-family: monospace;">"shift"</span>, <span style="font-family: monospace;">"xyscale"</span>, <span style="font-family: monospace;">"rotation"</span>, <span style="font-family: monospace;">"rscale"</span>, and <span style="font-family: monospace;">"rxyscale"</span>, fitting geometries
  assume that the polynomial order parameters are 2 regardless of the values
  set by the user. If any of the order parameters are higher than 2 and
  <i>fitgeometry</i> is <span style="font-family: monospace;">"general"</span>, then a distortion surface is fit to the
  residuals from the linear portion of the fit.
  </dd>
  </dl>
  <dl id="l_xxterms">
  <dt><b>xxterms = <span style="font-family: monospace;">"half"</span>, yxterms = <span style="font-family: monospace;">"half"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xxterms' Line='xxterms = "half", yxterms = "half"' -->
  <dd>The options are:
  <dl>
  <dt><b>none</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='none' Line='none' -->
  <dd>The individual polynomial terms contain powers of x or powers of y but not
  powers of both.
  </dd>
  </dl>
  <dl>
  <dt><b>half</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='half' Line='half' -->
  <dd>The individual polynomial terms contain powers of x and powers of y, whose
  maximum combined power is MAX (xxorder - 1, xyorder - 1) for the xi fit and
  MAX (yxorder - 1, yyorder - 1) for the eta fit. This is the recommended
  option for higher order plate solutions. 
  </dd>
  </dl>
  <dl>
  <dt><b>full</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='full' Line='full' -->
  <dd>The individual polynomial terms contain powers of x and powers of y, whose
  maximum combined power is MAX (xxorder - 1 + xyorder - 1) for the xi fit and
  MAX (yxorder - 1 + yyorder - 1) for the eta fit.
  </dd>
  </dl>
  The <span style="font-family: monospace;">"shift"</span>, <span style="font-family: monospace;">"xyscale"</span>, <span style="font-family: monospace;">"rotation"</span>,
  <span style="font-family: monospace;">"rscale"</span>, and <span style="font-family: monospace;">"rxyscale"</span> fitting geometries, assume that the
  cross term switches are set to <span style="font-family: monospace;">"none"</span> regardless of the values set by the user.
  If either of the cross-terms parameters is set to <span style="font-family: monospace;">"half"</span> or <span style="font-family: monospace;">"full"</span> and
  <i>fitgeometry</i> is <span style="font-family: monospace;">"general"</span> then a distortion surface is fit to the
  residuals from the linear portion of the fit.
  </dd>
  </dl>
  <dl id="l_maxiter">
  <dt><b>maxiter = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxiter' Line='maxiter = 0' -->
  <dd>The maximum number of rejection iterations. The default is no rejection.
  </dd>
  </dl>
  <dl id="l_reject">
  <dt><b>reject = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reject' Line='reject = INDEF' -->
  <dd>The rejection limit in units of sigma.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = no' -->
  <dd>Update the world coordinate system in the input image headers ?
  The required numerical quantities represented by the keywords CRPIX,
  CRVAL, and CD are computed from the linear portion of the plate solution,
  The values of the keywords CTYPE, RADECSYS, EQUINOX, and MJD-WCS
  are set by the <i>projection</i> and <i>insystem</i> parameters. As there
  is currently no standard mechanism for storing the higher order plate solution
  terms if any in the image header wcs, these terms are currently ignored
  unless the projection function is the experimental function <span style="font-family: monospace;">"tnx"</span>. The <span style="font-family: monospace;">"tnx"</span>
  function is not FITS compatible and can only be understood by IRAF. Any existing
  image wcs represented by the above keywords is overwritten during the update.
  </dd>
  </dl>
  <dl id="l_pixsystem">
  <dt><b>pixsystem = <span style="font-family: monospace;">"logical"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixsystem' Line='pixsystem = "logical"' -->
  <dd>The input pixel coordinate system. The options are:
  <dl>
  <dt><b>logical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='logical' Line='logical' -->
  <dd>The logical pixel coordinate system is the coordinate system of the image
  pixels on disk. Since most users measure the pixel coordinates of objects
  in this system, <span style="font-family: monospace;">"logical"</span> is the system of choice for most applications.
  </dd>
  </dl>
  <dl>
  <dt><b>physical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='physical' Line='physical' -->
  <dd>The physical coordinate system is the pixel coordinate system of the
  parent image if any. This option may be useful for users working on images
  that are pieces of a larger mosaic.
  </dd>
  </dl>
  The choice of pixsystem has no affect on the fitting process, but does 
  determine how the image header wcs is updated.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print detailed messages about the progress of the task on the standard output ?
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Compute the plate solution interactively ?
  In interactive mode the user may interact with the fitting process, e.g.
  change the order of the fit, reject points, display the data and refit, etc.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>The graphics device.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>The graphics cursor.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  CCMAP computes the plate solution for an image or set of images using lists
  of matched pixel and celestial coordinates. The celestial coordinates
  are usually equatorial coordinates, but may also be ecliptic, galactic,
  or supergalactic coordinates.  The input coordinate files <i>input</i> must
  be text file tables whose columns are delimited by whitespace. The pixel
  and celestial coordinates are listed in input, one per line with  x, y,
  ra / longitude, and dec / latitude in columns <i>xcolumn</i>, <i>ycolumn</i>,
  <i>lngcolumn</i>, and <i>latcolumn</i> respectively.
  </p>
  <p>
  The <i>xmin</i>, <i>xmax</i>, <i>ymin</i> and <i>ymax</i> parameters define
  the region of validity of the fit in the pixel coordinate system. They should
  normally either be left set to INDEF, or set to the size of input images
  <i>images</i> if any, e.g. xmin= 1.0, xmax= 512.0, ymin = 1.0, ymax = 512.0
  for a 512 square image. If set these parameters are also used to reject out
  of range pixel data before the actual fitting is done.
  </p>
  <p>
  The <i>lngunits</i> and <i>latunits</i> parameters set the units of the input
  celestial coordinates. If undefined lngunits and latunits assume sensible
  defaults for the input celestial coordinate system set by the <i>insystem</i>
  parameter, e.g. <span style="font-family: monospace;">"hours"</span> and <span style="font-family: monospace;">"degrees"</span> for equatorial coordinates and <span style="font-family: monospace;">"degrees"</span>
  and <span style="font-family: monospace;">"degrees"</span> for galactic coordinates. The input celestial coordinate system
  must be one of the following: equatorial, ecliptic, galactic, or supergalactic.
  The equatorial coordinate systems must be one of: 1) FK4, the mean place
  pre-IAU 1976 system, 2) FK4-NO-E, the same as FK4 but without the E-terms,
  3) FK5, the mean place post-IAU 1976 system, 4) GAPPT, the geocentric apparent
  place in the post-IAU 1976 system.
  </p>
  <p>
  The plate solution computed by CCMAP has the following form, where x and y
  are the pixel coordinates of points in the input image and xi and eta are the
  corresponding standard coordinates in units of arcsec / pixel.
  </p>
  <div class="highlight-default-notranslate"><pre>
   xi = f (x, y)
  eta = g (x, y)
  </pre></div>
  <p>
  The standard coordinates xi and eta are computed from the input celestial
  coordinates using the sky projection geometry <i>projection</i> and
  the celestial coordinates of the projection reference point set by
  the user. The default projection is the tangent plane or gnomonic
  projection commonly used in optical astronomy. The projections most commonly
  used in astronomy are <span style="font-family: monospace;">"sin"</span> (the orthographic projection, used in radio
  aperture synthesis), <span style="font-family: monospace;">"arc"</span> (the zenithal equidistant projection, widely
  used as an approximation for Schmidt telescopes), and <span style="font-family: monospace;">"lin"</span> (linear).
  Other supported projections are <span style="font-family: monospace;">"ait"</span>, <span style="font-family: monospace;">"car"</span>, <span style="font-family: monospace;">"csc"</span>, <span style="font-family: monospace;">"gls"</span>, <span style="font-family: monospace;">"mer"</span>, <span style="font-family: monospace;">"mol"</span>,
  <span style="font-family: monospace;">"par"</span>, <span style="font-family: monospace;">"pco"</span>, <span style="font-family: monospace;">"qsc"</span>, <span style="font-family: monospace;">"stg"</span>, <span style="font-family: monospace;">"tsc"</span>, and <span style="font-family: monospace;">"zea"</span>. The experimental projection
  function <span style="font-family: monospace;">"tnx"</span> combines the <span style="font-family: monospace;">"tan"</span> projection with a polynomial fit
  to the residuals can be used to represent more complicated distortion
  functions.
  </p>
  <p>
  There are two modes in which this task works with multiple input
  coordinate lists.  In one case each input list and possible associated
  image is treated independently and produce separate solutions.  To
  select this option requires specifying a matching list of solution
  names or output results files.  Note that this can also be simply done
  by running the task multiple times with a single input list each time.
  </p>
  <p>
  In the second mode data from multiple input lists are combined to
  produce a single solution.  This is useful when multiple exposures are
  taken to define a higher quality astrometric solution.  This mode is
  selected when there are multiple input lists, and possibly associated
  images, and no solution name or a single solution name is specified.
  </p>
  <p>
  When combining input data each set of coordinates may have different
  reference points which can be specified either as a list or by
  reference to image header keywords.  The different reference points
  are used to convert each set of coordinates to the same coordinate
  frame.  Typically this occurs when a set of exposures, each with the
  same coordinate reference pixel, has slightly different pointing as
  defined by the coordinate reference value.  These different points
  result from a dither and can be useful to more completely sample the
  image pixel space.  In other words, astrometric reference stars can be
  moved around the images to produce many more fitting points than occur
  with a single exposure. The key point to this process is that the
  shifts are mapped by the reference points of the pointing and the
  standard coordinates are independent of the pointing.
  </p>
  <p>
  A particular feature primarily intending for combining multiple
  exposures, but applies to single exposures as well, is an adjustment to
  the specified tangent point value based on the image WCS.  When images,
  reference pixels, and reference coordinates are all defined and the
  images contain a celestial WCS the following computation is performed.
  The reference information replaces the WCS tangent point values, though
  typically the initial reference information is specified as the tangent
  point, and the updated WCS is used to evaluate celestial coordinates
  from the input pixel coordinates. The average difference between the WCS
  evaluated coordinates and the input celestial coordinates is computed.
  This difference is applied to the reference point prior to the standard
  coordinate plate solution calculation.  In other words, the reference
  point is tweaked in the initial image WCS to make it agree on average with
  the input reference coordinates.  If one updates the WCS of the images by
  the plate solution and the repeats the plate solution, particularly when
  using multiple exposures, an iterative convergence to a self-consistent
  WCS of both the tangent point and plate solution can be obtained.
  </p>
  <p>
  Several polynomial cross terms options are available. Options <span style="font-family: monospace;">"none"</span>, 
  <span style="font-family: monospace;">"half"</span>, and <span style="font-family: monospace;">"full"</span> are illustrated below for a quadratic polynomial in
  x and y.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xxterms = "none", xyterms = "none"
  xxorder = 3, xyorder = 3, yxorder = 3, yyorder = 3
  
      xi = a11 + a21 * x + a12 * y +
           a31 * x ** 2 + a13 * y ** 2
     eta = a11' + a21' * x + a12' * y +
           a31' * x ** 2 + a13' * y ** 2
  
  xxterms = "half", xyterms = "half"
  xxorder = 3, xyorder = 3, yxorder = 3, yyorder = 3
  
      xi = a11 + a21 * x + a12 * y +
           a31 * x ** 2 + a22 * x * y + a13 * y ** 2
     eta = a11' + a21' * x + a12' * y +
           a31' * x ** 2 + a22' * x * y + a13' * y ** 2
  
  xxterms = "full", xyterms = "full"
  xxorder = 3, xyorder = 3, yxorder = 3, yyorder = 3
  
      xi = a11 + a21 * x + a31 * x ** 2 +
           a12 * y + a22 * x * y +  a32 * x ** 2 * y +
           a13 * y ** 2 + a23 * x *  y ** 2 + a33 * x ** 2 * y ** 2
     eta = a11' + a21' * x + a31' * x ** 2 +
           a12' * y + a22' * x * y +  a32' * x ** 2 * y +
           a13' * y ** 2 + a23' * x *  y ** 2 + a33' * x ** 2 * y ** 2
  </pre></div>
  <p>
  If <i>refpoint</i> is <span style="font-family: monospace;">"coords"</span>, then the sky projection reference point is set
  to the mean of the input celestial coordinates. For images where the true
  reference point is close to the center of the input coordinate distribution,
  this definition is adequate for many purposes. If <i>refpoint</i> is <span style="font-family: monospace;">"user"</span>,
  the user may either set the celestial coordinates of the reference
  point explicitly, e.g. <i>lngref</i> = 13:41:02.3 and <i>latref</i> = -33:42:20,
  or point these parameters to the appropriate keywords in the input image
  header, e.g. <i>lngref</i> = RA, <i>latref</i> = DEC for NOAO image data.
  If undefined the celestial coordinate system of the reference point
  <i>refsystem</i> defaults to the celestial coordinate system of the input
  coordinates, otherwise it be any of the supported celestial coordinate
  systems described above. The user may also set <i>refsystem</i> to the
  image header keyword containing the epoch of the celestial reference point
  coordinates in years, e.g. EPOCH for NOAO data. In this case the
  reference point coordinates are assumed to be equatorial FK4 coordinates at the
  epoch specified by EPOCH. The units of the reference point celestial
  coordinates are specified by the <i>lngrefunits</i> and <i>latrefunits</i>
  parameters. Lngrefunits and latrefunits default to the values of the input
  coordinate units if undefined by either the user or the <i>refsystem</i>
  parameter. ONCE DETERMINED THE REFERENCE POINT CANNOT BE RESET DURING
  THE FITTING PROCESS.
  </p>
  <p>
  The <i>xref</i> and <i>yref</i> parameters may be used to constrain the
  solution to putting the reference coordinate at the reference pixel.
  Effectively what this does is fix the zero-th order coefficient in the
  linear part of the solution.  If a reference pixel is not specified the
  solution will produce a point determined from the zero-th order
  constant coefficient.  This may not be what is expected based on
  the specified reference celestial coordinate.
  </p>
  <p>
  The fitting functions f and g are specified by the <i>function</i> parameter
  and may be power series polynomials, Legendre polynomials, or Chebyshev
  polynomials of order <i>xxorder</i> and <i>xyorder</i> in x and <i>yxorder</i>
  and <i>yyorder</i> in y. Cross-terms are optional and are turned on and
  off by setting the <i>xxterms</i> and <i>xyterms</i> parameters. If the
  <b>fitgeometry</b> parameter is anything other than <span style="font-family: monospace;">"general"</span>, the order
  parameters assume the value 2 and the cross-terms switches assume the value
  <span style="font-family: monospace;">"none"</span>, regardless of the values set by the user. All computation are done in
  double precision. Automatic pixel rejection may be enabled by setting
  <i>maxiter</i> &gt; 0 and <i>reject</i> to a  positive value, usually something
  in the range 2.5-5.0.
  </p>
  <p>
  CCMAP may be run interactively by setting <i>interactive</i> to <span style="font-family: monospace;">"yes"</span> and
  inputting commands by the use of simple keystrokes. In interactive mode the
  user has the option of changing the fitting parameters and displaying the
  data and fit graphically until a satisfactory fit has been achieved. The
  keystroke commands are listed below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ?       Print options
  f       Fit data and graph fit with the current graph type (g,x,r,y,s)
  g       Graph the data and the current fit
  x,r     Graph the xi residuals versus x and y respectively
  y,s     Graph the eta residuals versus x and y respectively
  d,u     Delete or undelete the data point nearest the cursor
  o       Overplot the next graph
  c       Toggle the line of constant x and y plotting option
  t       Plot a line of constant x and y through nearest data point
  l       Print xishift, etashift, xscale, yscale, xrotate, yrotate
  q       Exit the interactive fitting code
  </pre></div>
  <p>
  The parameters listed below can be changed interactively with simple colon
  commands. Typing the parameter name along will list the current value.
  </p>
  <div class="highlight-default-notranslate"><pre>
  :show                List parameters
  :projection          Sky projection
  :refpoint            Sky projection reference point
  :fit      [value]    Fit type (shift,xyscale,rotate,rscale,rxyscale,general)
  :function [value]    Fitting function (chebyshev,legendre,polynomial)
  :xxorder  [value]    Xi fitting function order in x
  :xyorder  [value]    Xi fitting function order in y
  :yxorder  [value]    Eta fitting function order in x
  :yyorder  [value]    Eta fitting function order in y
  :xxterms  [n/h/f]    The xi fit cross terms type
  :yxterms  [n/h/f]    The eta fit cross terms type
  :maxiter  [value]    Maximum number of rejection iterations
  :reject   [value]    K-sigma rejection threshold
  </pre></div>
  <p>
  The final fit is stored in the text database file <i>database</i> file in a
  format suitable for use by the CCSETWCS and CCTRAN tasks. Each fit is
  stored in a record whose name is the name of the input image <i>image</i>
  if one is supplied, or the name of the input coordinate file <i>input</i>.
  </p>
  <p>
  If the <i>update</i> switch is <span style="font-family: monospace;">"yes"</span> and an input image is specified,
  a new image wcs is derived from the linear component of the computed plate
  solution and written to the image header. The numerical components of
  the new image wcs are written to the standards FITS keywords, CRPIX, CRVAL,
  and CD, with the actual values depending on the input pixel coordinate
  system <i>pixsystem</i>. 
  The FITS keywords which define the image celestial coordinate
  system CTYPE, RADECSYS, EQUINOX, and MJD-WCS are set by the <i>insystem</i> and
  <i>projection</i> parameters. 
  </p>
  <p>
  The first four characters of the values of the ra / longitude and dec / latitude
  axis CTYPE keywords specify the celestial coordinate system. They are set to
  RA-- / DEC- for equatorial coordinate systems, ELON / ELAT for the ecliptic
  coordinate system, GLON / GLAT for the galactic coordinate system, and
  SLON / SLAT for the supergalactic coordinate system.
  </p>
  <p>
  The second four characters of the values of the ra / longitude and dec /
  latitude axis CTYPE keywords specify the sky projection geometry. IRAF
  currently supports the TAN, SIN, ARC, AIT, CAR, CSC, GLS, MER, MOL, PAR, PCO,
  QSC, STG, TSC, and ZEA standard projections, in which case the second 4
  characters of CTYPE are set to  -TAN, -ARC, -SIN, etc. IRAF and CCMAP also
  support the experiment TAN plus polynomials function driver. 
  </p>
  <p>
  If the input celestial coordinate system is equatorial, the value of the
  RADECSYS keyword specifies the fundamental equatorial system, EQUINOX
  specifies the epoch of the mean place, and MJD-WCS specifies the epoch 
  for which the mean place is correct. The permitted values of
  RADECSYS are FK4, FK4-NO-E, FK5, ICRS, and GAPPT. EQUINOX is entered in years
  and interpreted as a Besselian epoch for the FK4 system, a Julian epoch
  for the FK5 system. The epoch of the wcs MJD-WCS is entered as 
  a modified Julian date. Only those keywords necessary to defined the
  new wcs are written. Any existing keywords which are not required to
  define the wcs or are redundant are removed, with the exception of
  DATE-OBS and EPOCH, which are left unchanged for obvious (DATE_OBS) and
  historical (use of EPOCH keyword at NOAO) reasons.
  </p>
  <p>
  If <i>verbose</i> is <span style="font-family: monospace;">"yes"</span>, various pieces of useful information are
  printed to the terminal as the task proceeds. If <i>results</i> is set to a
  file name then the original pixel and celestial coordinates, the fitted
  celestial coordinates, and the residuals of the fit in arcseconds are written
  to that file.
  </p>
  <p>
  The transformation computed by the <span style="font-family: monospace;">"general"</span> fitting geometry is arbitrary
  and does not correspond to a physically meaningful model. However the computed
  coefficients for the linear term can be given a simple geometrical 
  interpretation for all the fitting geometries as shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  fitting geometry = general (linear term)
       xi = a + b * x + c * y
      eta = d + e * x + f * y
  
  fitting geometry = shift
       xi = a + x
      eta = d + y
  
  fitting geometry = xyscale
       xi = a + b * x
      eta = d + f * y
  
  fitting geometry = rotate
       xi = a + b * x + c * y
      eta = d + e * x + f * y
      b * f - c * e = +/-1
      b = f, c = -e or b = -f, c = e
  
  fitting geometry = rscale
       xi = a + b * x + c * y
      eta = d + e * x + f * y
      b * f - c * e = +/- const
      b = f, c = -e or b = -f, c = e
  
  fitting geometry = rxyscale
       xi = a + b * x + c * y
      eta = d + e * x + f * y
      b * f - c * e = +/- const
  </pre></div>
  <p>
  The coefficients can be interpreted as follows. X0, y0, xi0, eta0
  are the origins in the reference and input frames respectively. By definition
  xi0 and eta0 are 0.0 and 0.0 respectively. Rotation and skew are the rotation
  of the x and y axes and their deviation from perpendicularity respectively.
  Xmag and ymag are the scaling factors in x and y in arcsec / pixel and are assumed
  to be positive by definition.
  </p>
  <div class="highlight-default-notranslate"><pre>
  general (linear term)
      xrotation = rotation - skew / 2
      yrotation = rotation + skew / 2
      b = xmag * cos (xrotation)
      c = ymag * sin (yrotation)
      e = -xmag * sin (xrotation)
      f = ymag * cos (yrotation)
      a = xi0 - b * x0 - c * y0 = xshift
      d = eta0 - e * x0 - f * y0 = yshift
  
  shift
      xrotation = 0.0,  yrotation = 0.0
      xmag = ymag = 1.0
      b = 1.0
      c = 0.0
      e = 0.0
      f = 1.0
      a = xi0 - x0 = xshift
      d = eta0 - y0 = yshift
  
  xyscale
      xrotation 0.0 / 180.0 yrotation = 0.0
      b = + /- xmag
      c = 0.0
      e = 0.0
      f = ymag
      a = xi0 - b * x0 = xshift
      d = eta0 - f * y0 = yshift
  
  rscale
      xrotation = rotation + 0 / 180, yrotation = rotation
      mag = xmag = ymag
      const = mag * mag
      b = mag * cos (xrotation)
      c = mag * sin (yrotation)
      e = -mag * sin (xrotation)
      f = mag * cos (yrotation)
      a = xi0 - b * x0 - c * y0 = xshift
      d = eta0 - e * x0 - f * y0 = yshift
  
  rxyscale
      xrotation = rotation + 0 / 180, yrotation = rotation
      const = xmag * ymag
      b = xmag * cos (xrotation)
      c = ymag * sin (yrotation)
      e = -xmag * sin (xrotation)
      f = ymag * cos (yrotation)
      a = xi0 - b * x0 - c * y0 = xshift
      d = eta0 - e * x0 - f * y0 = yshift
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
  1. Compute the plate scale for the test image dev$pix given the following
  coordinate list. Set the tangent point to the mean of the input celestial
  coordinates. Compute the plate scale interactively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type coords
  
  13:29:47.297  47:13:37.52  327.50  410.38
  13:29:37.406  47:09:09.18  465.50   62.10
  13:29:38.700  47:13:36.23  442.01  409.65
  13:29:55.424  47:10:05.15  224.35  131.20
  13:30:01.816  47:12:58.79  134.37  356.33
  
  cl&gt; imcopy dev$pix pix
  
  cl&gt; hedit pix epoch 1987.26
  
  cl&gt; ccmap coords coords.db image=pix xcol=3 ycol=4 lngcol=1 latcol=2
  
      ... a plot of the mapping function appears
      ... type ? to see the list of commands
      ... type x to see the xi fit residuals versus x
      ... type r to see the xi fit residuals versus y
      ... type y to see the eta fit residuals versus x
      ... type s to see the eta fit residuals versus y
      ... type g to return to the default plot
      ... type l to see the computed x and y scales in arcsec / pixel
      ... type q to quit and save fit
  </pre></div>
  <p>
  2. Repeat example 2 but compute the fit non-interactively and list the
  fitted values of the ra and dec and their residuals on the standard
  output.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccmap coords coords.db image=pix results=STDOUT xcol=3 ycol=4 \
  lngcol=1 latcol=2 inter-
  
  # Coords File: coords  Image: pix
  #     Database: coords.db  Record: pix
  # Refsystem: j2000  Coordinates: equatorial FK5
  #     Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  # Insystem: j2000  Coordinates: equatorial FK5
  #     Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  # Coordinate mapping status
  #     XI fit ok.  ETA fit ok.
  #     Ra/Dec or Long/Lat fit rms: 0.229  0.241   (arcsec  arcsec)
  # Coordinate mapping parameters
  #     Sky projection geometry: tan
  #     Reference point: 13:29:48.129  47:11:53.37  (hours  degrees)
  #     Reference point: 318.735  273.900  (pixels  pixels)
  #     X and Y scale: 0.764  0.767  (arcsec/pixel  arcsec/pixel)
  #     X and Y axis rotation: 179.110  358.958  (degrees  degrees)
  # Wcs mapping status
  #     Ra/Dec or Long/Lat wcs rms: 0.229  0.241   (arcsec  arcsec)
  #
  #                     Input Coordinate Listing
  # X      Y       Ra          Dec        Ra(fit)      Dec(fit)    Dra    Ddec
  #
  327.5  410.4  13:29:47.30  47:13:37.5  13:29:47.28  47:13:37.9  0.128 -0.370
  465.5   62.1  13:29:37.41  47:09:09.2  13:29:37.42  47:09:09.2 -0.191 -0.062
  442.0  409.6  13:29:38.70  47:13:36.2  13:29:38.70  47:13:35.9  0.040  0.282
  224.3  131.2  13:29:55.42  47:10:05.2  13:29:55.40  47:10:05.1  0.289  0.059
  134.4  356.3  13:30:01.82  47:12:58.8  13:30:01.84  47:12:58.7 -0.267  0.091
  </pre></div>
  <p>
  3. Repeat the previous example but in this case input the position of the
  tangent point in fk4 1950.0 coordinates.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccmap coords coords.db image=pix results=STDOUT xcol=3 ycol=4 lngcol=1 \
  latcol=2 refpoint=user lngref=13:27:46.9 latref=47:27:16 refsystem=b1950.0 \
  inter-
  
  # Coords File: coords  Image: pix
  #     Database: coords.db  Record: pix
  # Refsystem: b1950.0  Coordinates: equatorial FK4
  #     Equinox: B1950.000 Epoch: B1950.00000000 MJD: 33281.92346
  # Insystem: j2000  Coordinates: equatorial FK5
  #     Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  # Coordinate mapping status
  #     XI fit ok.  ETA fit ok.
  #     Ra/Dec or Long/Lat fit rms: 0.229  0.241   (arcsec  arcsec)
  # Coordinate mapping parameters
  #     Sky projection geometry: tan
  #     Reference point: 13:29:53.273  47:11:48.36  (hours  degrees)
  #     Reference point: 250.256  266.309  (pixels  pixels)
  #     X and Y scale: 0.764  0.767  (arcsec/pixel  arcsec/pixel)
  #     X and Y axis rotation: 179.126  358.974  (degrees  degrees)
  # Wcs mapping status
  #     Ra/Dec or Long/Lat wcs rms: 0.229  0.241   (arcsec  arcsec)
  #
  #                     Input Coordinate Listing
  #  X      Y       Ra         Dec        Ra(fit)      Dec(fit)    Dra    Ddec
  
  327.5  410.4  13:29:47.30  47:13:37.5  13:29:47.28  47:13:37.9  0.128 -0.370
  465.5   62.1  13:29:37.41  47:09:09.2  13:29:37.42  47:09:09.2 -0.191 -0.062
  442.0  409.6  13:29:38.70  47:13:36.2  13:29:38.70  47:13:35.9  0.040  0.282
  224.3  131.2  13:29:55.42  47:10:05.2  13:29:55.40  47:10:05.1  0.289  0.059
  134.4  356.3  13:30:01.82  47:12:58.8  13:30:01.84  47:12:58.7 -0.267  0.091
  </pre></div>
  <p>
  Note the computed image scales are identical in examples 2 and 3 but that
  the assumed position of the tangent point is different (the second estimate
  is more accurate) producing different values for the pixel and celestial
  coordinates of the reference point and small differences in the computed
  rotation angles.
   
  4. Repeat the previous example but in this case extract the position of the
  tangent point in from the image header keywords RA, DEC, and EPOCH. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imheader pix l+
  
  DATE-OBS= '05/04/87'            /  DATE DD/MM/YY
  RA      = '13:29:24.00'         /  RIGHT ASCENSION
  DEC     = '47:15:34.00'         /  DECLINATION
  EPOCH   =              1987.26  /  EPOCH OF RA AND DEC
  
  cl&gt; ccmap coords coords.db image=pix results=STDOUT xcol=3 ycol=4 \
  lngcol=1 latcol=2 refpoint=user lngref=RA latref=DEC refsystem=EPOCH \
  inter-
  
  # Coords File: coords  Image: pix
  #     Database: coords.db  Record: pix
  # Refsystem: fk4 b1987.26  Coordinates: equatorial FK4
  #     Equinox: B1987.260 Epoch: B1987.26000000 MJD: 46890.84779
  # Insystem: j2000  Coordinates: equatorial FK5
  #     Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  # Coordinate mapping status
  #     XI fit ok.  ETA fit ok.
  #     Ra/Dec or Long/Lat fit rms: 0.229  0.241   (arcsec  arcsec)
  # Coordinate mapping parameters
  #     Sky projection geometry: tan
  #     Reference point: 13:29:56.232  47:11:38.19  (hours  degrees)
  #     Reference point: 211.035  252.447  (pixels  pixels)
  #     X and Y scale: 0.764  0.767  (arcsec/pixel  arcsec/pixel)
  #     X and Y axis rotation: 179.135  358.983  (degrees  degrees)
  # Wcs mapping status
  #     Ra/Dec or Long/Lat wcs rms: 0.229  0.241   (arcsec  arcsec)
  #
  #                     Input Coordinate Listing
  #  X      Y       Ra         Dec        Ra(fit)      Dec(fit)    Dra    Ddec
  
  327.5  410.4  13:29:47.30  47:13:37.5  13:29:47.28  47:13:37.9  0.128 -0.370
  465.5   62.1  13:29:37.41  47:09:09.2  13:29:37.42  47:09:09.2 -0.191 -0.062
  442.0  409.6  13:29:38.70  47:13:36.2  13:29:38.70  47:13:35.9  0.040  0.282
  224.3  131.2  13:29:55.42  47:10:05.2  13:29:55.40  47:10:05.1  0.289  0.059
  134.4  356.3  13:30:01.82  47:12:58.8  13:30:01.84  47:12:58.7 -0.267  0.091
  </pre></div>
  <p>
  Note that the position of the tangent point is slightly different again but
  that this does not have much affect on the fitted coordinates for this image.
  </p>
  <p>
  5. Repeat the third example but this time store the computed world coordinate
  system in the image header and check the header update with the imheader and
  skyctran tasks.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imheader pix l+
  DATE-OBS= '05/04/87'            /  DATE DD/MM/YY
  RA      = '13:29:24.00'         /  RIGHT ASCENSION
  DEC     = '47:15:34.00'         /  DECLINATION
  EPOCH   =              1987.26  /  EPOCH OF RA AND DEC
  
  cl&gt; ccmap coords coords.db image=pix results=STDOUT xcol=3 ycol=4  \
  lngcol=1 latcol=2 refpoint=user lngref=13:27:46.9 latref=47:27:16    \
  refsystem=b1950.0 inter- update+
  
  # Coords File: coords  Image: pix
  #     Database: coords.db  Record: pix
  # Refsystem: b1950.0  Coordinates: equatorial FK4
  #     Equinox: B1950.000 Epoch: B1950.00000000 MJD: 33281.92346
  # Insystem: j2000  Coordinates: equatorial FK5
  #     Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  # Coordinate mapping status
  # Coordinate mapping status
  #     XI fit ok.  ETA fit ok.
  #     Ra/Dec or Long/Lat fit rms: 0.229  0.241   (arcsec  arcsec)
  # Coordinate mapping parameters
  #     Sky projection geometry: tan
  #     Reference point: 13:29:53.273  47:11:48.36  (hours  degrees)
  #     Reference point: 250.256  266.309  (pixels  pixels)
  #     X and Y scale: 0.764  0.767  (arcsec/pixel  arcsec/pixel)
  #     X and Y axis rotation: 179.126  358.974  (degrees  degrees)
  # Wcs mapping status
  #     Ra/Dec or Long/Lat wcs rms: 0.229  0.241   (arcsec  arcsec)
  # Updating image header wcs
  #
  #
  #                     Input Coordinate Listing
  #  X      Y       Ra          Dec        Ra(fit)     Dec(fit)    Dra    Ddec
  
  327.5  410.4  13:29:47.30  47:13:37.5  13:29:47.28  47:13:37.9  0.128 -0.370
  465.5   62.1  13:29:37.41  47:09:09.2  13:29:37.42  47:09:09.2 -0.191 -0.062
  442.0  409.6  13:29:38.70  47:13:36.2  13:29:38.70  47:13:35.9  0.040  0.282
  224.3  131.2  13:29:55.42  47:10:05.2  13:29:55.40  47:10:05.1  0.289  0.059
  134.4  356.3  13:30:01.82  47:12:58.8  13:30:01.84  47:12:58.7 -0.267  0.091
  
  cl&gt; imheader pix l+
  DATE-OBS= '05/04/87'            /  DATE DD/MM/YY
  RA      = '13:29:24.00'         /  RIGHT ASCENSION
  DEC     = '47:15:34.00'         /  DECLINATION
  EPOCH   =              1987.26  /  EPOCH OF RA AND DEC
  RADECSYS= 'FK5     '
  EQUINOX =                2000.
  MJD-WCS =              51544.5
  WCSDIM  =                    2
  CTYPE1  = 'RA---TAN'
  CTYPE2  = 'DEC--TAN'
  CRVAL1  =     202.471969550729
  CRVAL2  =     47.1967667056819
  CRPIX1  =     250.255619786203
  CRPIX2  =     266.308757328719
  CD1_1   =  -2.1224568721716E-4
  CD1_2   =  -3.8136850875221E-6
  CD2_1   =  -3.2384199624421E-6
  CD2_2   =  2.12935798198448E-4
  LTM1_1  =                   1.
  LTM2_2  =                   1.
  WAT0_001= 'system=image'
  WAT1_001= 'wtype=tan axtype=ra'
  WAT2_001= 'wtype=tan axtype=dec'
  
  cl&gt; skyctran coords STDOUT "pix log" "pix world" lngcol=3 latcol=4 trans+
  
  # Insystem: pix logical  Projection: TAN  Ra/Dec axes: 1/2
  #     Coordinates: equatorial FK5 Equinox: J2000.000
  #     Epoch: J2000.00000000 MJD: 51544.50000
  # Outsystem: pix world  Projection: TAN  Ra/Dec axes: 1/2
  #     Coordinates: equatorial FK5 Equinox: J2000.000
  #     Epoch: J2000.00000000 MJD: 51544.50000
  
  # Input file: incoords  Output file: STDOUT
  
  13:29:47.297  47:13:37.52 13:29:47.284 47:13:37.89
  13:29:37.406  47:09:09.18 13:29:37.425 47:09:09.24
  13:29:38.700  47:13:36.23 13:29:38.696 47:13:35.95
  13:29:55.424  47:10:05.15 13:29:55.396 47:10:05.09
  13:30:01.816  47:12:58.79 13:30:01.842 47:12:58.70
  </pre></div>
  <p>
  Note that two versions of the rms values are printed, one for the fit
  and one for the wcs fit. For the default fitting parameters these
  two estimates should be identical. If a non-linear high order plate
  solution is requested however, the image wcs will have lower precision
  than the than the full plate solution, because only the linear component
  of the plate solution is preserved in the wcs.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  cctran,ccsetwcs,skyctran,imctran,finder.tfinder,finder.tastrom
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'REFERENCES' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

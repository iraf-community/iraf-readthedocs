.. _ccfind:

ccfind: Find catalog sources in an image
========================================

**Package: imcoords**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ccfind input output image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input celestial coordinate files. Coordinates may be entered
  by hand by setting input to <span style="font-family: monospace;">"STDIN"</span>. A STDIN coordinate list is terminated
  by typing &lt;EOF&gt; (usually &lt;ctrl/d&gt; or &lt;ctrl/z&gt;).
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The list of output matched coordinate files. The computed pixel values
  are appended to the input coordinate file line and written to output. The number
  of output files must equal the number of input files. Results may be
  printed on the terminal by setting output to <span style="font-family: monospace;">"STDOUT"</span>.
  </dd>
  </dl>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The list of input images associated with the input coordinate files. The number
  of input images must equal the number of input coordinate files.
  </dd>
  </dl>
  <dl id="l_lngcolumn">
  <dt><b>lngcolumn = 1, latcolumn = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngcolumn' Line='lngcolumn = 1, latcolumn = 2' -->
  <dd>The input coordinate file columns containing the celestial ra / longitude and
  dec / latitude coordinates respectively.
  </dd>
  </dl>
  <dl id="l_lngunits">
  <dt><b>lngunits = <span style="font-family: monospace;">""</span>, latunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngunits' Line='lngunits = "", latunits = ""' -->
  <dd>The units of the input ra / longitude and dec / latitude coordinates. The
  options are <span style="font-family: monospace;">"hours"</span>, <span style="font-family: monospace;">"degreees"</span>, and <span style="font-family: monospace;">"radians"</span> for ra / longitude and
  <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"radians"</span> for dec / latitude. If lngunits and latunits are
  undefined they default to the preferred units for the coordinates
  system specified by <i>insystem</i>, e.g. <span style="font-family: monospace;">"hours"</span> and <span style="font-family: monospace;">"degrees"</span> for
  equatorial systems and <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"degrees"</span> for ecliptic, galactic, and
  supergalactic systems.
  </dd>
  </dl>
  <dl id="l_insystem">
  <dt><b>insystem = <span style="font-family: monospace;">"j2000"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='insystem' Line='insystem = "j2000"' -->
  <dd>The input celestial coordinate system. The <i>insystem</i> parameter
  sets the preferred units for the input celestial coordinates, and
  tells CCFIND how to transform the input celestial coordinates 
  the input image celestial coordinate system. The systems of most
  interest to users are <span style="font-family: monospace;">"icrs"</span>, <span style="font-family: monospace;">"j2000"</span>, and <span style="font-family: monospace;">"b1950"</span>.  The full set
  of options are the following:
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
  <dd>The International Celestial Reference System (ICRS) where equinox is
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
  <dt><b>fk5 [equinox] [epoch]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='fk5' Line='fk5 [equinox] [epoch]' -->
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
  <dt><b>apparent epoch</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='apparent' Line='apparent epoch' -->
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
  Since CCFIND does not currently support proper motions these fields are
  not required.
  </dd>
  </dl>
  <dl id="l_usewcs">
  <dt><b>usewcs = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='usewcs' Line='usewcs = no' -->
  <dd>Use image header information to compute the input image celestial coordinate
  system ? If usewcs is <span style="font-family: monospace;">"yes"</span>, the image coordinate system is read from the
  image header.  If usewcs is <span style="font-family: monospace;">"no"</span>, the input image celestial coordinates
  system is defined by <i>xref</i>, <i>yref</i>, <i>xmag</i>, <i>ymag</i>,
  <i>xrotation</i>, <i>yrotation</i>, <i>lngref</i>, <i>latref</i>, 
  <i>lngrefunits</i>, <i>latrefunits</i>, <i>refsystem</i>, and <i>projection</i>
  parameters respectively.
  </dd>
  </dl>
  <dl id="l_xref">
  <dt><b>xref = INDEF, yref = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xref' Line='xref = INDEF, yref = INDEF' -->
  <dd>The x and y pixel coordinates of the reference point.
  xref and yref default to the center of the image in pixel coordinates.
  </dd>
  </dl>
  <dl id="l_xmag">
  <dt><b>xmag = INDEF, ymag = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmag' Line='xmag = INDEF, ymag = INDEF' -->
  <dd>The x and y scale factors in arcseconds per pixel.  xmag and ymag default
  to 1.0 and 1.0 arcseconds per pixel.
  </dd>
  </dl>
  <dl id="l_xrotation">
  <dt><b>xrotation = INDEF, yrotation = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xrotation' Line='xrotation = INDEF, yrotation = INDEF' -->
  <dd>The x and y rotation angles in degrees. xrotation and yrotation are
  interpreted as the rotation of the ra / longitude and dec / latitude
  coordinates with respect to the x and y axes, and default 0.0 and 0.0 degrees
  respectively. To set east to the up, down, left, and right directions,
  set xrotation to 90, 270, 180, and 0 respectively. To set north to the
  up, down, left, and right directions, set yrotation to  0, 180, 90, and 270
  degrees respectively. Any global rotation must be added to both the
  xrotation and yrotation values.
  </dd>
  </dl>
  <dl id="l_lngref">
  <dt><b>lngref = <span style="font-family: monospace;">"INDEF"</span>, latref = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngref' Line='lngref = "INDEF", latref = "INDEF"' -->
  <dd>The ra / longitude and dec / latitude of the reference point. Lngref and latref
  may be numbers, e.g 13:20:42.3 and -33:41:26, or keywords for the
  appropriate parameters in the image header, e.g. RA and DEC for NOAO
  image data. If lngref and latref are undefined they default to 0.0 and 0.0
  respectively.
  </dd>
  </dl>
  <dl id="l_lngrefunits">
  <dt><b>lngrefunits = <span style="font-family: monospace;">""</span>, latrefunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngrefunits' Line='lngrefunits = "", latrefunits = ""' -->
  <dd>The units of the reference point celestial  coordinates. The options
  are <span style="font-family: monospace;">"hours"</span>, <span style="font-family: monospace;">"degrees"</span>, and <span style="font-family: monospace;">"radians"</span> for the ra / longitude coordinates,
  and <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"radians"</span> for the dec /latitude coordinates.
  If lngrefunits and latrefunits are undefined they default to the preferred
  units of the reference system.
  </dd>
  </dl>
  <dl id="l_refsystem">
  <dt><b>refsystem = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refsystem' Line='refsystem = "INDEF"' -->
  <dd>The celestial coordinate system of the reference point. Refsystem may
  be any one of the options listed under the <i>insystem</i> parameter, e.g.
  <span style="font-family: monospace;">"b1950"</span>, or an image header keyword containing the epoch of the observation
  in years, e.g. EPOCH for NOAO data.  If refsystem is undefined
  the celestial coordinate system of the reference point defaults to the
  celestial coordinate system of the input coordinates <i>insystem</i>.
  </dd>
  </dl>
  <dl id="l_projection">
  <dt><b>projection = <span style="font-family: monospace;">"tan"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='projection' Line='projection = "tan"' -->
  <dd>The sky projection geometry. The most commonly used projections in
  astronomy are <span style="font-family: monospace;">"tan"</span>, <span style="font-family: monospace;">"arc"</span>, <span style="font-family: monospace;">"sin"</span>, and <span style="font-family: monospace;">"lin"</span>. Other supported projections
  are <span style="font-family: monospace;">"ait"</span>, <span style="font-family: monospace;">"car"</span>, <span style="font-family: monospace;">"csc"</span>, <span style="font-family: monospace;">"gls"</span>, <span style="font-family: monospace;">"mer"</span>, <span style="font-family: monospace;">"mol"</span>, <span style="font-family: monospace;">"par"</span>, <span style="font-family: monospace;">"pco"</span>, <span style="font-family: monospace;">"qsc"</span>, <span style="font-family: monospace;">"stg"</span>,
  <span style="font-family: monospace;">"tsc"</span>, and <span style="font-family: monospace;">"zea"</span>.
  </dd>
  </dl>
  <dl id="l_center">
  <dt><b>center = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='center' Line='center = yes' -->
  <dd>Center the object pixel coordinates using an x and y marginal centroiding
  algorithm ?
  </dd>
  </dl>
  <dl id="l_sbox">
  <dt><b>sbox = 21</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sbox' Line='sbox = 21' -->
  <dd>The search box width in pixels. Sbox defines the region of the input image
  searched and used to compute the initial x and y marginal centroids. Users
  worried about contamination can set sbox = cbox, so that the first
  centering iteration will be the same as the others.
  </dd>
  </dl>
  <dl id="l_cbox">
  <dt><b>cbox = 9</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cbox' Line='cbox = 9' -->
  <dd>The centering box width in pixels. Cbox defines the region of the input
  image used to compute the final x and y marginal centroids.
  </dd>
  </dl>
  <dl id="l_datamin">
  <dt><b>datamin = INDEF, datamax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datamin' Line='datamin = INDEF, datamax = INDEF' -->
  <dd>The minimum and maximum good data values. Values outside this range
  are exclude from the x and y marginal centroid computation.
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = INDEF' -->
  <dd>The background value used by the centroiding algorithm. If background is
  INDEF, a value equal to the mean value of the good data pixels for
  each object is used.
  </dd>
  </dl>
  <dl id="l_maxiter">
  <dt><b>maxiter = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxiter' Line='maxiter = 5' -->
  <dd>The maximum number of centroiding iterations to perform. The centroiding
  algorithm will halt when this limit is reached or when the desired tolerance
  is reached.
  </dd>
  </dl>
  <dl id="l_tolerance">
  <dt><b>tolerance = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tolerance' Line='tolerance = 0' -->
  <dd>The convergence tolerance of the centroiding algorithm. Tolerance is
  defined as the maximum permitted integer shift of the centering box in
  pixels from one iteration to the next.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose' -->
  <dd>Print messages about actions taken by the task?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  CCFIND locates the objects in the input celestial coordinate lists <i>input</i>
  in the input images <i>image</i> using the image world coordinate system,
  and writes the located objects to the output matched coordinates files
  <i>output</i>. CCFIND computes the pixel coordinates of each object by,
  1) transforming the input celestial coordinates to image celestial coordinate
  system, 2) using the image celestial coordinate system to compute the
  initial pixel coordinates, and 3) computing the final pixel coordinates
  using a centroiding algorithm. The image celestial coordinate system may
  be read from the image header or supplied by the user. The CCFIND output
  files are suitable for input to the plate solution computation task CCMAP.
  </p>
  <p>
  The input ra / longitude and dec / latitude coordinates are read from
  columns <i>lngcolumn</i> and <i>latcolumn</i> in the input coordinate
  file respectively.
  </p>
  <p>
  The input celestial coordinate system is set by the <i>insystem</i> parameter,
  and must be one of the following: equatorial, ecliptic, galactic, or
  supergalactic.  The equatorial coordinate systems must be one of: 1) FK4,
  the mean place pre-IAU 1976 system, 2) FK4-NO-E, the same as FK4 but without
  the E-terms, 3) FK5, the mean place post-IAU 1976 system, 4) ICRS the
  International Celestial Reference System, 5) GAPPT, the geocentric apparent
  place in the post-IAU 1976 system.
  </p>
  <p>
  The <i>lngunits</i> and <i>latunits</i> parameters set the units of the input
  celestial coordinates. If undefined, lngunits and latunits assume sensible
  defaults for the input celestial coordinate system set by the <i>insystem</i>
  parameter, e.g. <span style="font-family: monospace;">"hours"</span> and <span style="font-family: monospace;">"degrees"</span> for equatorial coordinates and <span style="font-family: monospace;">"degrees"</span>
  and <span style="font-family: monospace;">"degrees"</span> for galactic coordinates.
  </p>
  <p>
  If the <i>usewcs</i> parameter is <span style="font-family: monospace;">"yes"</span>, the image celestial coordinate
  system is read from the image header keywords CRPIX, CRVAL, CD or CDELT/CROTA,
  RADECSYS, EQUINOX or EPOCH, and MJD-OBS or DATE-OBS, where the mathematical
  part of this transformation is shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
   xi = a + b * x + c * y
  eta = d + e * x + f * y
    b = CD1_1
    c = CD1_2
    e = CD2_1
    f = CD2_2
    a = - b * CRPIX1 - c * CRPIX2
    d = - e * CRPIX1 - f * CRPIX2
  lng = CRVAL1 + PROJ (xi, eta)
  lat = CRVAL2 + PROJ (xi, eta)
  </pre></div>
  <p>
  If usewcs is <span style="font-family: monospace;">"no"</span>, then the image celestial coordinate system is computed
  using the values of the <i>xref</i>, <i>yref</i>, <i>xmag</i>, <i>ymag</i>,
  <i>xrotation</i>, <i>yrotation</i>, <i>lngref</i>, <i>latref</i>,
  <i>lngrefunits</i>, <i>latrefunits</i>, <i>refsystem</i>, and <i>projection</i>
  supplied by the user, where the mathematical part of this transformation is
  shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
   xi = a + b * x + c * y
  eta = d + e * x + f * y
    b = xmag * cos (xrotation)
    c = -ymag * sin (yrotation)
    e = xmag * sin (xrotation)
    f = ymag * cos (yrotation)
    a = - b * xref - c * yref
    d = - e * xref - f * yref
  lng = lngref + PROJ (xi, eta)
  lat = latref + PROJ (xi, eta)
  </pre></div>
  <p>
  In both the above examples, x and y are the pixel coordinates, xi and eta
  are the usual projected (standard) coordinates, lng and lat are the celestial
  coordinates, and PROJ stands for the projection function,  usually
  the tangent plane projection function.
  </p>
  <p>
  Once the image celestial coordinate system is determined, CCFIND transforms
  the input celestial coordinates to the image celestial coordinate system
  using the value of the <i>insystem</i> parameter, and either the values of
  the image header keywords RADECSYS, EQUINOX / EPOCH, and MJD-OBS / DATE-OBS
  (if <i>usewcs</i> = <span style="font-family: monospace;">"yes"</span>), or the value of the <i>refsystem</i> parameter (if
  <i>usewcs</i> = <span style="font-family: monospace;">"no"</span>), and then transforms the image celestial coordinates
  to pixel coordinates using the inverse of the transformation functions
  shown above.
  </p>
  <p>
  If <i>center</i> is yes, CCFIND locates the objects in the input
  image using an  xn and y marginal centroiding algorithm. Pixels
  inside a box <i>sbox</i> pixels wide centered in the initial coordinates,
  are used to locate the objects in the image. Accurate final centering
  is done using pixels inside a region <i>cbox</i> pixels wide centered on
  these initial coordinates. Sbox should be set to a value large enough
  to locate the object, but small enough to exclude other bright sources.
  Cbox should be set to a value small enough to exclude sky values and other
  bright sources, but large enough to include the wings of point sources.
  Bad data can be excluded from the centroiding algorithm by setting
  the <i>datamin</i> and <i>datamax</i> parameters. If <i>background</i> is
  undefined then the centroiding algorithm sets the background value to
  the mean of the good data values inside the centering box.
  The centroiding algorithm iterates until the maximum number of
  iterations <i>maxiter</i> limit is reached, or until the tolerance
  criteria <i>tolerance</i> is achieved.
  </p>
  <p>
  Only objects whose coordinates are successfully located in the 
  input image are written to the output coordinate file. The computed
  output pixel coordinates are appended to the input image line using
  the format parameters <i>xformat</i> and <i>yformat</i> parameters,
  whose default values are <span style="font-family: monospace;">"%10.3f"</span> and <span style="font-family: monospace;">"%10.3f"</span> respectively
  </p>
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
  cctran.hlp-(67%)-line 268-file 1 of 1
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
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Locate the object in the list wpix.coords in the image wpix using
  the existing image header wcs. The input celestial coordinates file
  contains j2000 GSC catalog coordinates of 5 objects in the field.
  The image wcs is in b1950.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imcopy dev$wpix wpix
      ... copy the test image into the current directory
  
  cl&gt; hedit wpix equinox 1950.0 add+
      ... change the epoch keyword value to the correct number
  
  cl&gt; type wpix.coords
  13:29:47.297  47:13:37.52
  13:29:37.406  47:09:09.18
  13:29:38.700  47:13:36.23
  13:29:55.424  47:10:05.15
  13:30:01.816  47:12:58.79
  
  cl&gt; ccfind wpix.coords wpix.match wpix usewcs+
  
  Input File: wpix.coords  Output File: wpix.match
      Image: wpix  Wcs:
  Insystem: j2000  Coordinates: equatorial FK5
      Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  Refsystem: wpix.imh logical  Projection: TAN  Ra/Dec axes: 1/2
      Coordinates: equatorial FK4 Equinox: B1950.000
      Epoch: B1987.25767884 MJD: 46890.00000
  Located 5 objects in image wpix
  
  cl&gt; type wpix.match
  # Input File: wpix.coords  Output File: wpix.match
  #     Image: wpix  Wcs:
  # Insystem: j2000  Coordinates: equatorial FK5
  #     Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  # Refsystem: wpix.imh logical  Projection: TAN  Ra/Dec axes: 1/2
  #     Coordinates: equatorial FK4 Equinox: B1950.000
  #     Epoch: B1987.25767884 MJD: 46890.00000
  
  13:29:47.297  47:13:37.52     327.504    410.379
  13:29:37.406  47:09:09.18     465.503     62.101
  13:29:38.700  47:13:36.23     442.013    409.654
  13:29:55.424  47:10:05.15     224.351    131.200
  13:30:01.816  47:12:58.79     134.373    356.327
  
  cl&gt; ccmap wpix.match ccmap.db xcol=3 ycol=4 lngcol=1 latcol=2 ...
  </pre></div>
  <p>
  2. Repeat the previous example but input the image coordinate system by hand.
  The scale is known to be ~0.77 arcseconds per pixel, north is up, east is left,
  and the center of the image is near ra = 13:27:47, dec = 47:27:14 in 1950
  coordinates.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccfind wpix.coords wpix.match wpix xmag=-0.77 ymag=.77 lngref=13:27:47 \
  latref=47:27:14 refsystem=b1950.
  
  Input File: wpix.coords  Output File: wpix.match.1
      Image: wpix  Wcs:
  Insystem: j2000  Coordinates: equatorial FK5
      Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  Refsystem: b1950  Coordinates: equatorial FK4
      Equinox: B1950.000 Epoch: B1950.00000000 MJD: 33281.92346
  Located 5 objects in image wpix
  
  cl&gt; type wpix.match
  
  # Input File: wpix.coords  Output File: wpix.match
  #     Image: wpix  Wcs:
  # Insystem: j2000  Coordinates: equatorial FK5
  #     Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  # Refsystem: b1950  Coordinates: equatorial FK4
  #     Equinox: B1950.000 Epoch: B1950.00000000 MJD: 33281.92346
  
  13:29:47.297  47:13:37.52     327.504    410.379
  13:29:37.406  47:09:09.18     465.503     62.101
  13:29:38.700  47:13:36.23     442.013    409.654
  13:29:55.424  47:10:05.15     224.351    131.200
  13:30:01.816  47:12:58.79     134.373    356.327
  </pre></div>
  <p>
  3. Repeat the previous example but read the ra, dec, and epoch from the
  image header keywords RA, DEC, and EPOCH. It turns out the telescope
  RA and DEC recorded in the image header are not very accurate and that
  EPOCH is 0.0 instead of 1987.26 so we will fix up the header before
  trying out the example.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit wpix EPOCH 1987.26
  cl&gt; hedit wpix RA '13:29:21'
  cl&gt; hedit wpix DEC '47:15:42'
  
  cl&gt; ccfind wpix.coords wpix.match wpix xmag=-0.77 ymag=.77 lngref=RA \
  latref=DEC refsystem=EPOCH
  
  Input File: wpix.coords  Output File: wpix.match
      Image: wpix  Wcs:
  Insystem: j2000  Coordinates: equatorial FK5
      Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  Refsystem: 1987.26  Coordinates: equatorial FK5
      Equinox: J1987.260 Epoch: J1987.26000000 MJD: 46891.21500
  Located 5 objects in image wpix
  
  # Input File: wpix.coords  Output File: wpix.match
  #     Image: wpix  Wcs:
  # Insystem: j2000  Coordinates: equatorial FK5
  #     Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  # Refsystem: 1987.26  Coordinates: equatorial FK5
  #     Equinox: J1987.260 Epoch: J1987.26000000 MJD: 46891.21500
  
  13:29:47.297  47:13:37.52     327.504    410.379
  13:29:37.406  47:09:09.18     465.503     62.101
  13:29:38.700  47:13:36.23     442.013    409.654
  13:29:55.424  47:10:05.15     224.351    131.200
  13:30:01.816  47:12:58.79     134.373    356.327
  </pre></div>
  <p>
  4. Use ccfind to predict the pixel coordinate in the last example by
  turning off the object centering, and mark the predicted coordinates
  on the image display with red dots.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccfind wpix.coords wpix.match wpix xmag=-0.77 ymag=.77 lngref=RA \
  latref=DEC refsystem=EPOCH center-
  
  Input File: wpix.coords  Output File: wpix.match
      Image: wpix  Wcs:
  Insystem: j2000  Coordinates: equatorial FK5
      Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  Refsystem: 1987.26  Coordinates: equatorial FK5
      Equinox: J1987.260 Epoch: J1987.26000000 MJD: 46891.21500
  Located 5 objects in image wpix
  
  cl&gt; type wpix.match
  
  # Input File: wpix.coords  Output File: wpix.match
  #     Image: wpix  Wcs:
  # Insystem: j2000  Coordinates: equatorial FK5
  #     Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  # Refsystem: 1987.26  Coordinates: equatorial FK5
  #     Equinox: J1987.260 Epoch: J1987.26000000 MJD: 46891.21500
  
  13:29:47.297  47:13:37.52     333.954    401.502
  13:29:37.406  47:09:09.18     465.338     53.175
  13:29:38.700  47:13:36.23     447.687    399.967
  13:29:55.424  47:10:05.15     226.600    125.612
  13:30:01.816  47:12:58.79     141.892    351.084
  
  cl&gt; display wpix 1
  
  cl&gt; fields wpix.match 3,4 | tvmark 1 STDIN col=204
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
  starfind, ccxymatch, ccmap, ccsetwcs, cctran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'FORMATS' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

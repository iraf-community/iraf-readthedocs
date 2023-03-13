.. _ccsetwcs:

ccsetwcs: Create an image celestial wcs from the ccmap plate solution
=====================================================================

**Package: imcoords**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ccsetwcs image database solutions
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>The input images for which the wcs is to be created.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>The text database file written by the ccmap task containing the
  plate solutions. If database is undefined ccsetwcs computes
  the image wcs using the xref, yref, xmag, ymag, xrotation, yrotation,
  lngref, latref, lngrefunits, latrefunits, and projection parameters.
  </dd>
  </dl>
  <dl id="l_solutions">
  <dt><b>solutions</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='solutions' Line='solutions' -->
  <dd>The list of plate solutions. The number of plate solutions must be one
  or equal to the number of input images.  Solutions is either a user name
  supplied to the ccmap task, or the
  name of the ccmap task input image for which the plate solution is valid,
  or the name of the coordinate file that the ccmap task used to compute the
  plate solution. The quantities stored in transform always supersede the
  values of the xref, yref, xmag, ymag, xrotation, yrotation, lngref, latref,
  lnrefunits, latrefunits, and projection parameters.
  </dd>
  </dl>
  <dl id="l_xref">
  <dt><b>xref = INDEF, yref = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xref' Line='xref = INDEF, yref = INDEF' -->
  <dd>The x and y pixel coordinates of the sky projection reference point.
  If database is undefined then xref and yref default to the center of the
  image in pixel coordinates, otherwise these parameters are ignored.
  </dd>
  </dl>
  <dl id="l_xmag">
  <dt><b>xmag = INDEF, ymag = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmag' Line='xmag = INDEF, ymag = INDEF' -->
  <dd>The x and y scale factors in arcseconds per pixel. If database is undefined
  xmag and ymag default to 1.0 and 1.0 arcsec / pixel, otherwise these parameters
  are ignored.
  </dd>
  </dl>
  <dl id="l_xrotation">
  <dt><b>xrotation = INDEF, yrotation = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xrotation' Line='xrotation = INDEF, yrotation = INDEF' -->
  <dd>The x and y rotation angles in degrees measured counter-clockwise with
  respect to the x and y axes. Xrotation and yrotation are interpreted as the
  rotation of the coordinates with respect to the x and y axes and default 0.0
  and 0.0 degrees. For example xrotation and yrotation values of 30.0 and 30.0
  will rotate a point 30 degrees counter-clockwise with respect to the x and y
  axes. To flip the x axis coordinates in this case either set the angles to
  210.0 and 30.0 degrees or leave the angles set to 30.0 and 30.0 and set the
  xmag parameter to a negative value. To set east to the up, down, left, and
  right directions, set xrotation to 90, 270, 180, and 0 respectively. To set
  north to the up, down, left, and right directions, set yrotation to  0, 180,
  90, and 270 degrees respectively. Any global rotation must be added to both the
  xrotation and yrotation values.
  </dd>
  </dl>
  <dl id="l_lngref">
  <dt><b>lngref = INDEF, latref = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngref' Line='lngref = INDEF, latref = INDEF' -->
  <dd>The celestial coordinates of the sky projection reference point, e.g.
  the ra and dec of the reference point for equatorial systems. If database is
  undefined lngref and latref default to 0.0 and 0.0, otherwise these parameters
  are ignored.
  </dd>
  </dl>
  <dl id="l_lngunits">
  <dt><b>lngunits = <span style="font-family: monospace;">""</span>, latunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngunits' Line='lngunits = "", latunits = ""' -->
  <dd>The units of the lngref and latref parameters.
  The options are <span style="font-family: monospace;">"hours"</span>, <span style="font-family: monospace;">"degrees"</span>, <span style="font-family: monospace;">"radians"</span> for the ra / longitude
  coordinates, and <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"radians"</span> for the dec / latitude coordinates.
  If database is undefined then lngunits and latunits default to the preferred
  units for the celestial coordinate system defined by the <i>coosystem</i>
  parameter, otherwise these parameters are ignored.
  </dd>
  </dl>
  <dl id="l_transpose">
  <dt><b>transpose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='transpose' Line='transpose = no' -->
  <dd>Transpose the newly created image wcs ?
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
  <dl id="l_coosystem">
  <dt><b>coosystem = <span style="font-family: monospace;">"j2000"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coosystem' Line='coosystem = "j2000"' -->
  <dd>The celestial coordinate system. The systems of most interest to users
  are <span style="font-family: monospace;">"icrs"</span>, <span style="font-family: monospace;">"j2000"</span> and <span style="font-family: monospace;">"b1950"</span> which stand for the ICRS J2000.0, FK5 J2000.0,
  and FK4 B1950.0 celestial coordinate systems respectively. The full set of
  options are listed below. The celestial coordinate system sets the preferred
  units for the lngref and latref parameters and the correct values of the image
  wcs header keywords CTYPE, RADECSYS, EQUINOX, and MJD-WCS if the image header
  wcs is updated.  If database is undefined the coosystem parameter is used,
  otherwise this parameter is ignored.
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
  described. The epoch field for icrs, fk5, galactic, and supergalactic
  coordinate systems is required only if the input coordinates are in the
  equatorial fk4, noefk4, fk5, or icrs systems and proper motions are defined.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = yes' -->
  <dd>Update the world coordinate system in the input image headers ?
  The numerical quantities represented by the keywords CRPIX,
  CRVAL, and CD are computed from the linear portion of the plate solution.
  The values of the keywords CTYPE, RADECSYS, EQUINOX, and MJD-WCS
  are set by the <i>projection</i> and <i>coosystem</i> parameters if database
  is undefined, otherwise projection and coosystem are read from the plate
  solution. As there is currently no standard mechanism for storing the higher
  order plate solution terms if any in the image header wcs, these terms are
  ignored. Any existing image wcs represented by the above keywords is
  overwritten during the update.
  </dd>
  </dl>
  <dl id="l_pixsystem">
  <dt><b>pixsystem = <span style="font-family: monospace;">"logical"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixsystem' Line='pixsystem = "logical"' -->
  <dd>The pixel coordinate system. The options are:
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
  parent image. This option is useful for users working on images that are
  pieces of a larger mosaic.
  </dd>
  </dl>
  The pixsystem parameter is only used if no database solution is specified.
  Otherwise pixsystem is read from the database file.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print detailed messages about the progress of the task on the standard output ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  CCSETWCS creates an image world coordinate system from the plate solution
  computed by the CCMAP task or supplied by the user, and writes it to the
  headers of the input images <i>images</i> if the <i>update</i> parameter is yes.
  </p>
  <p>
  The plate solution can either be read from record <i>solutions</i> in the
  database file <i>database</i> written by CCMAP, or specified by the user
  via the <i>xref</i>, <i>yref</i>, <i>xmag</i>, <i>ymag</i>, <i>xrotation</i>,
  <i>yrotation</i>, <i>lngref</i>, <i>latref</i>, <i>lngunits</i>, <i>latunits</i>,
  <i>transpose</i>, <i>projection</i>, <i>coosystem</i> and <i>pixsystem</i>
  parameters.
  </p>
  <p>
  The plate solution computed by CCMAP has the following form where x and y
  are the image pixel coordinates and xi and eta are the corresponding standard
  coordinates in arcseconds per pixel. The standard coordinates are computed
  by applying the appropriate sky projection to the celestial coordinates.
  </p>
  <div class="highlight-default-notranslate"><pre>
   xi = f (x, y)
  eta = g (x, y)
  </pre></div>
  <p>
  The functions f and g are either power series, Legendre, or Chebyshev
  polynomials whose order and region of validity were set by the user when
  CCMAP was run. The computed plate solution is somewhat arbitrary and does
  not correspond to any physically meaningful model. However the linear
  component of the plate solution can be given the simple geometrical
  interpretation shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
   xi = a + b * x + c * y
  eta = d + e * x + f * y
    b = xmag * cos (xrotation)
    c = ymag * sin (yrotation)
    e = -xmag * sin (xrotation)
    f = ymag * cos (yrotation)
    a = xi0 - b * xref - c * yref = xshift
    d = eta0 - e * xref - f * yref = yshift
    xi0 = 0.0
    eta0 = 0.0
  </pre></div>
  <p>
  xref, yref, xi0, and eta0 are the origins of the pixel and standard
  coordinate systems respectively. xmag and ymag are the x and y scale factors
  in arcsec / pixel and xrotation and yrotation are the rotation angles measured
  counter-clockwise of the x and y axes.
  </p>
  <p>
  If the CCMAP database is undefined then CCSETWCS computes a linear plate
  solution using the parameters <i>xref</i>, <i>yref</i>, <i>xmag</i>,
  <i>ymag</i>, <i>xrotation</i>, <i>yrotation</i>, <i>lngref</i>, <i>latref</i>,
  <i>lngunits</i>, <i>latunits</i>, <i>transpose</i>,  and
  <i>projection</i> as shown below. Note that in this case
  xrotation and yrotation are interpreted as the rotation of the coordinates
  themselves not the coordinate axes. 
  </p>
  <div class="highlight-default-notranslate"><pre>
   xi = a + b * x + c * y
  eta = d + e * x + f * y
    b = xmag * cos (xrotation)
    c = -ymag * sin (yrotation)
    e = xmag * sin (xrotation)
    f = ymag * cos (yrotation)
    a = xi0 - b * xref - c * yref = xshift
    d = eta0 - e * xref - f * yref = yshift
    xi0 = 0.0
    eta0 = 0.0
  </pre></div>
  <p>
  The <i>transpose</i> parameter can be used to transpose the newly created
  image wcs.
  </p>
  <p>
  If the <i>update</i> switch is <span style="font-family: monospace;">"yes"</span> and an input image is specified,
  a new image wcs is derived from the linear component of the computed plate
  solution and written to the image header. The numerical components of
  the new image wcs are written to the standards FITS keywords, CRPIX, CRVAL,
  and CD, with the actual values depending on the pixel coordinate system
  <i>pixsystem</i> read from the database or set by the user. The FITS keywords
  which define the image celestial coordinate system CTYPE, RADECSYS, EQUINOX,
  and MJD-WCS are set by the <i>coosystem</i> and <i>projection</i> parameters.
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
  latitude axis CTYPE keywords specify the sky projection geometry.
  The second four characters of the values of the ra / longitude and dec /
  latitude axis CTYPE keywords specify the sky projection geometry. IRAF
  currently supports the TAN, SIN, ARC, AIT, CAR, CSC, GLS, MER, MOL, PAR, PCO,
  QSC, STG, TSC, and ZEA standard projections, in which case the second 4
  characters of CTYPE are set to  -TAN, -ARC, -SIN, etc.
  </p>
  <p>
  If the input celestial coordinate system is equatorial, the value of the
  RADECSYS keyword specifies the fundamental equatorial system, EQUINOX
  specifies the epoch of the mean place, and MJD-WCS specifies the epoch
  for which the mean place is correct. The permitted values of
  RADECSYS are FK4, FK4-NO-E, FK5, ICRS, and GAPPT. EQUINOX is entered in years
  and interpreted as a Besselian epoch for the FK4 system, a Julian epoch
  for the FK5 and ICRS system. The epoch of the wcs MJD-WCS is entered as
  a modified Julian date. Only those keywords necessary to defined the
  new wcs are written. Any existing keywords which are not required to
  define the wcs or are redundant are removed, with the exception of
  DATE-OBS and EPOCH, which are left unchanged for obvious (DATE-OBS) and
  historical (use of EPOCH keyword at NOAO) reasons.
  </p>
  <p>
  If <i>verbose</i> is <span style="font-family: monospace;">"yes"</span>, various pieces of useful information are
  printed to the terminal as the task proceeds.
  </p>
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
  1. Compute the plate solution for an image with the ccmap task and then
  use the ccsetwcs task to create the image wcs. Check the results with the
  imheader and skyctran tasks.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type coords
  13:29:47.297  47:13:37.52  327.50  410.38
  13:29:37.406  47:09:09.18  465.50   62.10
  13:29:38.700  47:13:36.23  442.01  409.65
  13:29:55.424  47:10:05.15  224.35  131.20
  13:30:01.816  47:12:58.79  134.37  356.33
  
  cl&gt; ccmap coords coords.db image=pix xcol=3 ycol=4 lngcol=1 latcol=2 \
  inter-
  Coords File: coords  Image: pix
      Database: coords.db  Record: pix
  Refsystem: j2000  Coordinates: equatorial FK5
      Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  Insystem: j2000  Coordinates: equatorial FK5
      Equinox: J2000.000 Epoch: J2000.00000000 MJD: 51544.50000
  Coordinate mapping status
      Ra/Dec or Long/Lat fit rms: 0.229  0.241   (arcsec  arcsec)
  Coordinate mapping parameters
      Sky projection geometry: tan
      Reference point: 13:29:48.129  47:11:53.37  (hours  degrees)
      Reference point: 318.735  273.900  (pixels  pixels)
      X and Y scale: 0.764  0.767  (arcsec/pixel  arcsec/pixel)
      X and Y axis rotation: 179.110  358.958  (degrees  degrees)
  Wcs mapping status
      Ra/Dec or Long/Lat wcs rms: 0.229  0.241   (arcsec  arcsec)
  
  cl&gt; type coords.db
  # Mon 15:10:37 13-May-96
  begin   coords
          xrefmean        318.7460000000001
          yrefmean        273.9320000000001
          lngmean         13.49670238888889
          latmean         47.19815944444444
          coosystem       j2000
          projection      tan
          lngref          13.49670238888889
          latref          47.19815944444444
          lngunits        hours
          latunits        degrees
          xpixref         318.7352667484295
          ypixref         273.9002619912411
          geometry        general
          function        polynomial
          xishift         247.3577084680361
          etashift        -206.1795977453246
          xmag            0.7641733802338992
          ymag            0.7666917500560622
          xrotation       179.1101291109185
          yrotation       358.9582148846163
          wcsxirms        0.2288984454992771
          wcsetarms       0.2411034140453112
          xirms           0.2288984454992771
          etarms          0.2411034140453112
          surface1        11
                          3.      3.
                          2.      2.
                          2.      2.
                          0.      0.
                          134.3700000000001       134.3700000000001
                          465.5000000000002       465.5000000000002
                          62.1    62.1
                          410.3800000000001       410.3800000000001
                          247.3577084680361       -206.1795977453246
                          -0.7640812161068504     -0.011868034832272
                          -0.01393966623835092    0.7665650170136847
          surface2        0
  
  cl&gt; imheader pix l+
  DATE-OBS= '05/04/87'            /  DATE DD/MM/YY
  RA      = '13:29:24.00'         /  RIGHT ASCENSION
  DEC     = '47:15:34.00'         /  DECLINATION
  EPOCH   =              1987.26  /  EPOCH OF RA AND DEC
  
  cl&gt; ccsetwcs pix coords.db pix
  Image: pix  Database: coords.db  Record: pix
  Coordinate mapping parameters
      Sky projection geometry: tan
      Reference point: 13:29:48.129  47:11:53.37  (hours   degrees)
      Ra/Dec logical image axes: 1  2
      Reference point: 318.735  273.900  (pixels  pixels)
      X and Y scale: 0.764  0.767  (arcsec/pixel  arcsec/pixel)
      X and Y coordinate rotation: 179.110  358.958  (degrees  degrees)
  Updating image header wcs
  
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
  CRVAL1  =     202.450535833334
  CRVAL2  =     47.1981594444445
  CRPIX1  =     318.735266748429
  CRPIX2  =     273.900261991241
  CD1_1   =  -2.1224478225190E-4
  CD1_2   =  -3.8721295106530E-6
  CD2_1   =  -3.2966763422978E-6
  CD2_2   =  2.12934726948246E-4
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
  The skyctran task is used to test that the input image wcs is indeed correct.
  Columns 1 and 2 contain the original ra and dec values and columns 3 and 4
  contain the transformed values. The second imheader listing shows what the
  image wcs looks like.
  </p>
  <p>
  2. Repeat the previous example but enter the plate solution parameters by
  hand.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccsetwcs pix "" xref=318.735 yref=273.900 lngref=13:29:48.129 \
  latref=47:11:53.37 xmag=.764 ymag=.767 xrot=180.890 yrot=1.042
  Image: pix
  Coordinate mapping parameters
      Sky projection geometry: tan
      Reference point: 13:29:48.129  47:11:53.37  (hours   degrees)
      Ra/Dec logical image axes: 1  2
      Reference point: 318.735  273.900  (pixels  pixels)
      X and Y scale: 0.764  0.767  (arcsec/pixel  arcsec/pixel)
      X and Y coordinate rotation: 180.890  1.042  (degrees  degrees)
  Updating image header wcs
  
  cl&gt; skyctran coords STDOUT "pix log" "pix world" lngcol=3 latcol=4 trans+
  
  # Insystem: pix logical  Projection: TAN  Ra/Dec axes: 1/2
  #     Coordinates: equatorial FK5 Equinox: J2000.000
  #     Epoch: J2000.00000000 MJD: 51544.50000
  # Outsystem: pix world  Projection: TAN  Ra/Dec axes: 1/2
  #     Coordinates: equatorial FK5 Equinox: J2000.000
  #     Epoch: J2000.00000000 MJD: 51544.50000
  
  # Input file: incoords  Output file: STDOUT
  
  13:29:47.297  47:13:37.52 13:29:47.285 47:13:37.93
  13:29:37.406  47:09:09.18 13:29:37.428 47:09:09.17
  13:29:38.700  47:13:36.23 13:29:38.698 47:13:35.99
  13:29:55.424  47:10:05.15 13:29:55.395 47:10:05.04
  13:30:01.816  47:12:58.79 13:30:01.839 47:12:58.72
  </pre></div>
  <p>
  Note that there are minor differences between the results of examples 1
  and 2 due to precision differences in the input. Note also the difference
  in the way the xrotation and yrotation angles are defined between examples
  1 and 2. In example 2 the rotations are defined as coordinate rotations,
  whereas in example one they are described as axis rotations.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ccmap, cctran, skyctran, imctran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'REFERENCES' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

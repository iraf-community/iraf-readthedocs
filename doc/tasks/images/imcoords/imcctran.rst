.. _imcctran:

imcctran: Transform image header from one celestial wcs to another
==================================================================

**Package: imcoords**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imcctran image outsystem
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The list of images whose celestial coordinate systems are to be converted. The
  image celestial coordinate system must be one of the standard FITS celestial
  coordinate systems: equatorial (FK4, FK4-NO-E, FK5, ICRS, or GAPPT), ecliptic,
  galactic, or supergalactic.
  </dd>
  </dl>
  <dl id="l_outsystem">
  <dt><b>outsystem</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outsystem' Line='outsystem' -->
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
  equatorial (FK4, FK4-NO-E, FK5, or GAPPT), ecliptic, galactic, or
  supergalactic.
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
  described. The epoch field for the fk5, icrs, galactic, and supergalactic
  coordinate systems is required only if the input coordinates are in the
  equatorial fk4, noefk4, fk5, or icrs systems and proper motions are defined.
  </dd>
  </dl>
  <dl id="l_nx">
  <dt><b>nx = 10, ny = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nx' Line='nx = 10, ny = 10' -->
  <dd>The dimensions of the coordinate grid used to compute the rotation angle and,
  optionally, the x and y magnification factors required to transform the input
  image celestial coordinate system to the output celestial coordinate system.
  </dd>
  </dl>
  <dl id="l_longpole">
  <dt><b>longpole = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='longpole' Line='longpole = no' -->
  <dd>If longpole = yes the zenithal projections ARC, SIN, STG, TAN, and ZEA
  will be transformed by updating the longpole and latpole parameters instead
  of rotating the CD matrix in the usual manner.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about actions taken by the task on the standard output ?
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = yes' -->
  <dd>Update the image celestial coordinate system ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IMCCTRAN converts the celestial coordinate system stored in the headers of the
  input images <i>image</i> to the celestial coordinate system specified by
  <i>outsystem</i>, and updates the input image header appropriately. The input
  and output celestial coordinate systems must be one of the following:
  equatorial, ecliptic, galactic, or supergalactic. The equatorial coordinate
  systems must be one of: 1) FK4, the mean place pre-IAU 1976 system, 2) FK4-NO-E,
  the same as FK4 but without the E-terms, 3) FK5, the mean place post-IAU 1976
  system, 4), ICRS, the International Celestial Reference System, 5) GAPPT,
  the geocentric apparent place in the post-IAU 1976 system. 
  </p>
  <p>
  The input celestial coordinate system is read from the input image header.
  IMCCTRAN assumes that the celestial coordinate system is specified by the FITS
  keywords CTYPE, CRPIX, CRVAL, CD (or alternatively CDELT / CROTA), RADECSYS,
  EQUINOX (or EPOCH), MJD-WCS (or MJD-OBS, or DATE-OBS). USERS SHOULD TAKE NOTE
  THAT MJD-WCS IS CURRENTLY NEITHER A STANDARD OR A PROPOSED FITS STANDARD
  KEYWORD. HOWEVER IT OR SOMETHING SIMILAR, IS REQUIRED TO SPECIFY THE EPOCH OF
  THE COORDINATE SYSTEM WHICH MAY BE DIFFERENT FROM THE EPOCH OF THE OBSERVATION.
  </p>
  <p>
  The first four characters of the values of the ra / longitude and dec / latitude
  axis CTYPE keywords specify the celestial coordinate system.  The currently
  permitted values of CTYPE[1:4] are RA-- / DEC- for equatorial coordinate
  systems, ELON / ELAT for the ecliptic coordinate system, GLON / GLAT for the
  galactic coordinate system, and SLON / SLAT for the supergalactic coordinate
  system.
  </p>
  <p>
  The second four characters of the values of the ra / longitude and dec /
  latitude axis CTYPE keywords specify the sky projection geometry. IRAF
  currently supports the AIT, ARC, CAR, CSC, GLS, MER, PAR, PCO, QSC,
  SIN,  STG, TAN, TSC, and ZEA geometries as well as two internal projection
  geometries TNX, and ZPX. Consequently the currently permitted values of
  CTYPE[5:8] are -AIT, -ARC, -CAR, -CSC, -GLS, -MER, -PAR, -PCO, -QSC,
  -SIN, -STG, -TAN, -TSC, -ZEA as well as -ZPX and -TNX. 
  </p>
  <p>
  If the input image celestial coordinate system is equatorial, the value of the
  RADECSYS keyword specifies which fundamental equatorial system is to be
  considered. The permitted values of RADECSYS are FK4, FK4-NO-E, FK5, ICRS,
  and GAPPT.  If the RADECSYS keyword is not present in the image header, the
  values of the EQUINOX / EPOCH keywords (in that order of precedence) are used
  to determine the fundamental equatorial coordinate system. EQUINOX or EPOCH
  contain the epoch of the mean place and equinox for the FK4, FK4-NO-E, FK5,
  and ICRS systems (e.g 1950.0 or 2000.0). The default equatorial system is
  FK4 if EQUINOX or EPOCH &lt; 1984.0, FK5 if EQUINOX or EPOCH &gt;= 1984.0, and FK5
  if RADECSYS, EQUINOX, and EPOCH are undefined. If RADECSYS is defined but
  EQUINOX and EPOCH are not, the equinox defaults to 1950.0 for the FK4 and
  FK4-NO-E systems, and 2000.0 for the FK5 and ICRS systems. The equinox value is
  interpreted as a Besselian epoch for the FK4 and FK4-NO-E systems, and as a
  Julian epoch for the FK5 and ICRS systems.  Users are
  strongly urged to use the EQUINOX keyword in preference to the EPOCH keyword,
  if they must enter their own equinox values into the image header. The FK4 and
  FK4-NO-E systems are not inertial and therefore also require the epoch of the
  observation (the time when the mean place was correct), in addition to the
  equinox. The epoch is specified, in order of precedence, by the values of the
  keywords MJD-WCS or MJD-OBS (which contain the modified Julian date, JD -
  2400000.5, of the coordinate system), or the DATE-OBS keyword (which contains
  the date of the observation in the form DD/MM/YY, CCYY-MM-DD, or
  CCYY-MM-DDTHH:MM:SS.S). As the latter quantity may
  only be accurate to a day, the MJD-WCS or MJD-OBS specification is preferred.
  If all 3 keywords are absent the epoch defaults to the value of equinox.
  Equatorial coordinates in the GAPPT system require only the specification
  of the epoch of observation which is supplied via the MJD-WCS, MJD-OBS,
  or DATE-OBS keywords (in that order of precedence) as for the FK4 and
  FK4-NO-E system.
  </p>
  <p>
  If the input image celestial coordinate system is ecliptic the mean ecliptic
  and equinox of date are required. These are supplied via the MJD-WCS, MJD-OBS,
  or DATE-OBS keywords (in that order or precedence) as for the equatorial FK4,
  FK4-NO-E, and GAPPT systems.
  </p>
  <p>
  The output coordinate system is specified by the <i>outsystem</i> parameter
  as described in the PARAMETERS section.
  </p>
  <p>
  If an error is encountered when decoding the input or output world coordinate
  systems, an error message is printed on the standard output (if <i>verbose</i>
  is <span style="font-family: monospace;">"yes"</span>), and the input image left unmodified.
  </p>
  <p>
  If the input projection is one of the zenithal projections TAN, SIN, STG,
  ARC, or ZEA, then the header coordinate transformation can be preformed by
  transforming the CRVAL parameters and rotating the CD matrix as described in 
  detail below. Otherwise the CRVAL values are transformed, the CD matrix is
  left unmodified, and the LONGPOLE and LATPOLE parameters required to perform
  the rotation are computed. If <i>longpole</i> is yes then the zenithal
  coordinate systems will also be transformed using LONGPOLE and LATPOLE. At
  present IRAF looks for longpole and latpole parameters in the appropriate
  WATN_* keywords. If these are undefined the appropriate default values for
  each projection are assumed and new values are written to the WATN_* keywords.
  </p>
  <p>
  The new image celestial coordinate system is computed as follows.  First a
  grid of <i>nx</i> by <i>ny</i> pixel and celestial coordinates, evenly spaced
  over the input image, is generated using the input image celestial coordinate
  system.  Next these input celestial coordinates are transformed to coordinates
  in the output celestial coordinate system. Next the input celestial coordinates
  of the reference point (stored in degrees in the input image CRVAL keywords)
  are transformed to coordinates in the output celestial coordinate system,
  and new x and y pixel coordinates are computed using the transformed reference
  point coordinates but the original input CD matrix. The differences
  between the predicted and initial x and y pixel coordinates are used to
  compute the x and y axis rotation angles and the x and y magnification factors
  required to transform the original CD matrix to the correct new CD matrix.
  The process is shown schematically below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  1.       x,y(input grid) -&gt; ra,dec(input grid)
  
  2.    ra,dec(input grid) -&gt; ra,dec(output grid)
  
  3. ra_ref,dec_ref(input) -&gt; ra_ref,dec_ref(output)
  
  4.   ra,dec(output grid) -&gt; x,y(predicted grid)
  
  5.      x,y(input  grid) -&gt; F -&gt; x,y(predicted grid)
  
  6.      cd matrix(input) -&gt; F -&gt; cd matrix(output)
  </pre></div>
  <p>
  F is the fitted function of the x and y axis rotation angles and the
  x and y scaling factors required to match the input x and y values to the
  predicted x and y values.
  </p>
  <p>
  For most celestial coordinate transformations the fitted x and y scale factors
  will be very close to 1.0 and the x and y rotation angles will be almost
  identical. However small deviations from unity scale factors and identical 
  x and y axis rotation angles do occur when transforming coordinates systems
  with the skewed axes.
  </p>
  <p>
  The precision of the transformations is usually very high, on the order
  of 10E-10 to 10E-11 in most cases.  However conversions to and from the FK4
  equatorial system are less precise as these transformations
  involve the addition and subtraction of the elliptical aberration
  or E-terms. In this case the x and y scale factors correct for the first
  order E-terms and do significantly improve the precision of the coordinate
  transformation. The quadratic terms, i.e. terms in xy, x**2, and y**2
  however are not corrected for, and their absence does diminish the precision
  of the transformation coordinate transformation. For most practical purposes
  this loss of precision is insignificant.
  </p>
  <p>
  After the fit is completed, the celestial coordinates of the reference point
  in dd:mm:ss.s in the old and new systems, the rotation angle in degrees, the x
  and y scaling factors, and an estimate of the rms error of the x and y
  coordinate transformation are printed on the standard output. 
  </p>
  <p>
  If <i>update</i> is yes, then the image header parameters CRVAL, CD,
  CTYPE, RADECSYS, EQUINOX, EPOCH, and MJD-WCS are modified, deleted, or
  added as appropriate. The position of the reference pixel in the
  image (stored in the CRPIX keywords), and the sky projection geometry, e.g.
  TAN, SIN, ARC, ETC are unchanged.
  </p>
  <p>
  USERS NEED TO BE AWARE THAT THE IRAF IMAGE WORLD COORDINATE SYSTEM
  CURRENTLY (IRAF VERSIONS 2.10.4 PATCH 2 AND EARLIER) SUPPORTS ONLY THE
  EQUATORIAL SYSTEM (CTYPE (ra axis) = <span style="font-family: monospace;">"RA--XXXX"</span> CTYPE (dec axis) = <span style="font-family: monospace;">"DEC-XXXX"</span>)
  WHERE XXXX IS THE PROJECTION TYPE, EVEN THOUGH THE IMCCTRAN TASK 
  SUPPORTS GALACTIC, ECLIPTIC, AND SUPERGALACTIC COORDINATES. IMCCTRAN will
  update the image correctly for non-equatorial systems, but IRAF will
  not be able to read these transformed image coordinate systems correctly.
  </p>
  <p>
  USERS SHOULD ALSO REALIZE THAT IMAGE WORLD COORDINATE SYSTEM REPRESENTATION
  IN FITS IS STILL IN THE DRAFT STAGE. ALTHOUGH IMCCTRAN TRIES TO CONFORM TO
  THE CURRENT DRAFT PROPOSAL AS MUCH AS POSSIBLE, WHERE NO ADOPTED STANDARDS
  CURRENTLY EXIST, THE FINAL FITS STANDARD MAY DIFFER FROM THE ONE ADOPTED HERE.
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
  [1]. Precess the equatorial FK5 J2000 celestial coordinate system of the
  input 512 by 512 pixel square input image to J1975.0.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imcctran image j1975.0
  
  INPUT IMAGE: image
  Insystem: image logical  Projection: TAN  Ra/Dec axes: 1/2
      Coordinates: equatorial FK5 Equinox: J2000.000
      Epoch: J1987.25667351 MJD: 46890.00000
  Outsystem: j1975  Coordinates: equatorial FK5
      Equinox: J1975.000 Epoch: J1975.00000000 MJD: 42413.25000
  Crval1,2: 201:56:43.5, 47:27:16.0 -&gt; 201:40:53.8, 47:35:01.2 dd:mm:ss.s
      Scaling: Xmag: 1.000000 Ymag: 1.000000 Xrot: 359.923 Yrot: 359.923 degrees
      Rms: X fit: 8.465123E-11 pixels  Y fit: 5.204446E-11 pixels
  </pre></div>
  <p>
  Before the transformation the image coordinate system looked like the following.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ...
  EPOCH   =                 2000
  DATE-OBS= '05/04/87'
  CRPIX1  =               257.75
  CRPIX2  =               258.93
  CRVAL1  =      201.94541667302
  CRVAL2  =             47.45444
  CDELT1  =        -2.1277777E-4
  CDELT2  =         2.1277777E-4
  CTYPE1  = 'RA---TAN'
  CTYPE2  = 'DEC--TAN'
  ...
  </pre></div>
  <p>
  After the transformation the header looks like the following.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ...
  DATE-OBS= '05/04/87'
  CRPIX1  =               257.75
  CRPIX2  =               258.93
  CRVAL1  =     201.681616387759
  CRVAL2  =      47.583668865029
  CTYPE1  = 'RA---TAN'
  CTYPE2  = 'DEC--TAN'
  RADECSYS= 'FK5     '
  EQUINOX =                1975.
  MJD-WCS =             42413.25
  WCSDIM  =                    2
  CD1_1   =  -2.1277757990523E-4
  CD1_2   =  2.84421945372844E-7
  CD2_1   =  2.84421945363011E-7
  CD2_2   =  2.12777579905235E-4
  LTM1_1  =                   1.
  LTM2_2  =                   1.
  WAT0_001= 'system=image'
  WAT1_001= 'wtype=tan axtype=ra'
  WAT2_001= 'wtype=tan axtype=dec'
  ...
  </pre></div>
  <p>
  Note the rms of the x and y fits is on the order 10.0e-10 to 10.0e-11 which
  is the expected numerical precision of the transformation.
  </p>
  <p>
  [2]. Convert the input image used in example 1 to the BFK4 1950.0 system. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imcctran image B1950.0
  
  INPUT IMAGE: image
  Insystem: image logical  Projection: TAN  Ra/Dec axes: 1/2
      Coordinates: equatorial FK5 Equinox: J2000.000
      Epoch: J1987.25667351 MJD: 46890.00000
  Outsystem: B1950  Coordinates: equatorial FK4
      Equinox: B1950.000 Epoch: B1950.00000000 MJD: 33281.92346
  Crval1,2: 201:56:43.5, 47:27:16.0 -&gt; 201:25:02.3, 47:42:47.1 dd:mm:ss.s
      Scaling: Xmag: 0.999999 Ymag: 0.999999 Xrot: 359.848 Yrot: 359.848 degrees
      Rms: X fit: 1.302837E-7 pixels  Y fit: 8.545616E-8 pixels
  </pre></div>
  <p>
  Note that precision of the transformation is still good but is significantly
  less that the precision of the previous example. This is due to the fact
  that the quadratic terms in the E-term computation are not included in the
  transformation. 
  </p>
  <p>
  The transformed image header in this case looks like the following.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ...
  DATE-OBS= '05/04/87'
  CRPIX1  =               257.75
  CRPIX2  =               258.93
  CRVAL1  =     201.417300629944
  CRVAL2  =     47.7130749603847
  CTYPE1  = 'RA---TAN'
  CTYPE2  = 'DEC--TAN'
  RADECSYS= 'FK4     '
  EQUINOX =                1950.
  MJD-WCS =       33281.92345905
  WCSDIM  =                    2
  CD1_1   =  -2.1277680505752E-4
  CD1_2   =  5.66226465943254E-7
  CD2_1   =  5.66226470798410E-7
  CD2_2   =  2.12776805056766E-4
  LTM1_1  =                   1.
  LTM2_2  =                   1.
  WAT0_001= 'system=image'
  WAT1_001= 'wtype=tan axtype=ra'
  WAT2_001= 'wtype=tan axtype=dec'
  ...
  </pre></div>
  <p>
  [3].  Transform the celestial coordinate system of the input image used in
  examples 1 and 2 to the galactic coordinate system.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imcctran image galactic
  
  INPUT IMAGE: image
  Insystem: image logical  Projection: TAN  Ra/Dec axes: 1/2
      Coordinates: equatorial FK5 Equinox: J2000.000
      Epoch: J1987.25667351 MJD: 46890.00000
  Outsystem: galactic  Coordinates: galactic
      MJD: 33281.92346 Epoch: J1949.99979044 B1950.00000000
  rval1,2: 201:56:43.5, 47:27:16.0 -&gt; 106:01:19.4, 68:27:46.1 dd:mm:ss.s
      Scaling: Xmag: 1.000000 Ymag: 1.000000 Xrot: 202.510 Yrot: 202.510 degrees
      Rms: X fit: 9.087450E-11 pixels  Y fit: 3.815443E-11 pixels
  </pre></div>
  <p>
  The transformed header looks like the following.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ...
  DATE-OBS= '05/04/87'
  CRPIX1  =               257.75
  CRPIX2  =               258.93
  CRVAL1  =     106.022047915293
  CRVAL2  =     68.4627934475432
  CTYPE1  = 'GLON-TAN'
  CTYPE2  = 'GLAT-TAN'
  MJD-WCS =       33281.92345905
  WCSDIM  =                    2
  CD1_1   =  1.96567112095654E-4
  CD1_2   =  8.14601120181094E-5
  CD2_1   =  8.14601120174619E-5
  CD2_2   =  -1.9656711209802E-4
  LTM1_1  =                   1.
  LTM2_2  =                   1.
  WAT0_001= 'system=image'
  WAT1_001= 'wtype=tan axtype=glon'
  WAT2_001= 'wtype=tan axtype=glat'
  ...
  </pre></div>
  <p>
  Users should not that although imcctran can write a legal galactic coordinate
  system to the image header, it and other iraf tasks cannot currently
  read this coordinate system.
  </p>
  <p>
  [4]. Repeat the previous example but don't update the image header.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imcctran image galactic update-
  
  INPUT IMAGE: image
  Insystem: image logical  Projection: TAN  Ra/Dec axes: 1/2
      Coordinates: equatorial FK5 Equinox: J2000.000
      Epoch: J1987.25667351 MJD: 46890.00000
  Outsystem: galactic  Coordinates: galactic
      MJD: 33281.92346 Epoch: J1949.99979044 B1950.00000000
  
  Current wcs
      Axis            1           2
      Crval    201.9454     47.4544
      Crpix      257.75      258.93
      Cd 1    -2.128E-4          0.
      Cd 2           0.    2.128E-4
  
  New wcs
      Axis            1           2
      Crval    106.0220     68.4628
      Crpix      257.75      258.93
      Cd 1     1.966E-4    8.146E-5
      Cd 2     8.146E-5   -1.966E-4
  
  Crval1,2: 201:56:43.5, 47:27:16.0 -&gt; 106:01:19.4, 68:27:46.1 dd:mm:ss.s
      Scaling: Xmag: 1.000000 Ymag: 1.000000 Xrot: 202.510 Yrot: 202.510 degrees
      Rms: X fit: 9.087450E-11 pixels  Y fit: 3.815443E-11 pixels
  </pre></div>
  <p>
  [5]. Repeat example 1 and check the accuracy of the results by using the
  skyctran task on the original image and on the transformed image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type coords
    1.0   1.0
  512.0   1.0
  512.0 512.0
    1.0 512.0
  
  cl&gt; skyctran coords STDOUT "image logical" J1975.0
  
  Insystem: image logical  Projection: TAN  Ra/Dec axes: 1/2
      Coordinates: equatorial FK5 Equinox: J2000.000
      Epoch: J1987.25667351 MJD: 46890.00000
  Outsystem: j1975  Coordinates: equatorial FK5
      Equinox: J1975.000 Epoch: J1975.00000000 MJD: 42413.25000
  
  Input file: coords  Output file: STDOUT
  
    1.0   1.0  13:27:02.9797 47:31:43.269
  512.0   1.0  13:26:24.3330 47:31:43.793
  512.0 512.0  13:26:24.3448 47:38:15.219
    1.0 512.0  13:27:03.0718 47:38:14.693
  
  cl&gt; imcctran image j1975.0
  
  cl&gt; skyctran coords STDOUT "image logical" "image world"
  
  Insystem: image logical  Projection: TAN  Ra/Dec axes: 1/2
      Coordinates: equatorial FK5 Equinox: J1975.000
      Epoch: J1975.00000000 MJD: 42413.25000
  Outsystem: image world  Projection: TAN  Ra/Dec axes: 1/2
      Coordinates: equatorial FK5 Equinox: J1975.000
      Epoch: J1975.00000000 MJD: 42413.25000
  
  Input file: coords  Output file: STDOUT
  
    1.0   1.0  13:27:02.9797 47:31:43.269
  512.0   1.0  13:26:24.3330 47:31:43.793
  512.0 512.0  13:26:24.3448 47:38:15.219
    1.0 512.0  13:27:03.0718 47:38:14.693
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  At present IRAF requires that the LONGPOLE and or LATPOLE keywords be
  defined in the appropriate WAT_* keywords, e.g. WAT1_* and WAT2_* for
  a 2D image. If these are not present then default values are assumed.
  The new values are computed and added to the WAT1_* and WAT2_* keywords.
  </p>
  <p>
  At present the experimental TNX and ZPX projections cannot be transformed
  with precision. Users should use the SKYCTRAN task to transform individual
  coordinate pairs.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  setjd,precess,galactic,xray.xspatial.skypix,stsdas.toolbox.tools.tprecess
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'REFERENCES' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

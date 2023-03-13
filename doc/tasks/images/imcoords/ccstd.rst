.. _ccstd:

ccstd: Transform to and from standard astrometric coordinates
=============================================================

**Package: imcoords**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ccstd input output database solutions
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The input coordinate files. Coordinates may be entered by hand by setting input
  to <span style="font-family: monospace;">"STDIN"</span>.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output coordinate files. The number of output files must be one or equal
  to the number of input files. Results may be printed on the terminal by
  setting output to <span style="font-family: monospace;">"STDOUT"</span>.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>The text database file written by the ccmap task which contains the
  desired plate solutions. If database is undefined ccstd computes the
  standard coordinates or pixel and celestial coordinates using the current
  values of the xref, yref, xmag ymag, xrotation, yrotation, lngref, latref,
  and projection parameters.
  </dd>
  </dl>
  <dl id="l_solutions">
  <dt><b>solutions</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='solutions' Line='solutions' -->
  <dd>The database record containing the desired plate solution. 
  The number of records must be one or equal to the number of input coordinate
  files. Solutions is either the user name supplied to ccmap, the name of the
  image input to ccmap for which the plate solution is valid, or the name of the
  coordinate file that the ccmap task used to compute the plate solution.
  The quantities stored in solutions always supersede the values of the
  parameters xref, yref, xmag, ymag, xrotation, yrotation, lngref, latref,
  and projection.
  </dd>
  </dl>
  <dl id="l_geometry">
  <dt><b>geometry = <span style="font-family: monospace;">"geometric"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='geometry' Line='geometry = "geometric"' -->
  <dd>The type of geometric transformation. The geometry parameter is
  only requested if database is defined. The options are:
  <dl>
  <dt><b>linear</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='linear' Line='linear' -->
  <dd>Transform the pixel coordinates to standard coordinates or vice versa
  using the linear part of the plate solution.
  only.
  </dd>
  </dl>
  <dl>
  <dt><b>geometric</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='geometric' Line='geometric' -->
  <dd>Transform the pixel coordinates to standard coordinates or vice versa
  using the full plate solution.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_forward">
  <dt><b>forward = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='forward' Line='forward = yes' -->
  <dd>Transform from pixel and celestial coordinates to standard coordinates ? If
  forward is <span style="font-family: monospace;">"no"</span> then the plate solution is inverted and standard coordinates
  are transformed to pixel and celestial coordinates.
  </dd>
  </dl>
  <dl id="l_polar">
  <dt><b>polar = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='polar' Line='polar = no' -->
  <dd>Convert to and from polar standard coordinates instead of Cartesian standard
  coordinates?
  </dd>
  </dl>
  <dl id="l_xref">
  <dt><b>xref = INDEF, yref = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xref' Line='xref = INDEF, yref = INDEF' -->
  <dd>The pixel coordinates of the reference point. If database is undefined
  then xref and yref default to 0.0 and 0.0, otherwise these parameters are
  ignored.
  </dd>
  </dl>
  <dl id="l_xmag">
  <dt><b>xmag = INDEF, ymag = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmag' Line='xmag = INDEF, ymag = INDEF' -->
  <dd>The x and y scale factors in arcseconds per pixel. If database is undefined
  xmag and ymag default to 1.0 and 1.0 arcseconds per pixel, otherwise these
  parameters are ignored.
  </dd>
  </dl>
  <dl id="l_xrotation">
  <dt><b>xrotation = INDEF, yrotation = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xrotation' Line='xrotation = INDEF, yrotation = INDEF' -->
  <dd>The x and y rotation angles in degrees measured counter-clockwise with
  respect to the x and y axes. If database is undefined then xrotation and
  yrotation are interpreted as the rotation of the coordinates with respect
  to the x and y axes and default to 0.0 and 0.0 degrees. For example xrotation
  and yrotation values of 30.0 and 30.0 degrees will rotate a point 30 degrees
  counter-clockwise with respect to the x and y axes. To flip the x axis
  coordinates in this case either set the angles to 210.0 and 30.0 degrees
  or leave the angles at 30.0 and 30.0 and set the xmag parameter to a negative
  value. If database is defined these parameters are ignored. The ccmap task
  computes the x and y rotation angles of the x and y axes, not the rotation
  angle of the coordinates. An celestial coordinate system rotated 30 degrees
  counter-clockwise with respect to the pixel coordinate system will produce
  xrotation and yrotation values o 330.0 and 330.0 or equivalently -30.0 and
  -30.0 degrees in the database file not 30.0 and 30.0.
  </dd>
  </dl>
  <dl id="l_lngref">
  <dt><b>lngref = INDEF, latref = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngref' Line='lngref = INDEF, latref = INDEF' -->
  <dd>The celestial coordinates of the reference point, e.g. the ra and dec
  of the reference point for equatorial systems, galactic longitude and
  latitude of the reference for galactic systems. If database is undefined
  lngref and latref default to 0.0 and 0.0, otherwise these parameters are
  ignored.
  </dd>
  </dl>
  <dl id="l_lngunits">
  <dt><b>lngunits = <span style="font-family: monospace;">""</span>, latunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngunits' Line='lngunits = "", latunits = ""' -->
  <dd>The units of the input or output ra / longitude and dec / latitude coordinates.
  The options are <span style="font-family: monospace;">"hours"</span>, <span style="font-family: monospace;">"degrees"</span>, <span style="font-family: monospace;">"radians"</span> for ra / longitude coordinates,
  and <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"radians"</span> for dec / latitude systems. If lngunits and
  latunits are undefined they default to the values in the database records.
  If database is undefined then lngunits and latunits default to <span style="font-family: monospace;">"hours"</span> and
  <span style="font-family: monospace;">"degrees"</span> respectively.
  </dd>
  </dl>
  <dl id="l_projection">
  <dt><b>projection = <span style="font-family: monospace;">"tan"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='projection' Line='projection = "tan"' -->
  <dd>The sky projection geometry. The options are <span style="font-family: monospace;">"tan"</span>, <span style="font-family: monospace;">"sin"</span>, <span style="font-family: monospace;">"arc"</span> and
  <span style="font-family: monospace;">"lin"</span>. If database is undefined then the value of the projection parameter
  is used, otherwise this parameter is ignored.
  </dd>
  </dl>
  <dl id="l_xcolumn">
  <dt><b>xcolumn = 1, ycolumn = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcolumn' Line='xcolumn = 1, ycolumn = 2' -->
  <dd>The columns in the input coordinate file containing the x and y coordinates
  if the <i>forward</i> parameter is <span style="font-family: monospace;">"yes"</span>, or the corresponding standard
  coordinates xi and eta if the forward parameter is <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_lngcolumn">
  <dt><b>lngcolumn = 3, latcolumn = 4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngcolumn' Line='lngcolumn = 3, latcolumn = 4' -->
  <dd>The columns in the input coordinate file containing the celestial coordinates
  if the <i>forward</i> parameter is <span style="font-family: monospace;">"yes"</span>, or the corresponding standard
  coordinates xi and eta if the forward parameter is <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_lngformat">
  <dt><b>lngformat = <span style="font-family: monospace;">""</span>, latformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngformat' Line='lngformat = "", latformat = ""' -->
  <dd>The default output format of the transformed coordinates in lngcolumn and 
  latcolumn. If forward = yes then the default output format is <span style="font-family: monospace;">"%10.3f"</span>.
  Otherwise the defaults are <span style="font-family: monospace;">"%12.2h"</span> for output coordinates in hours, <span style="font-family: monospace;">"%11.1h"</span>
  for output coordinates in degrees, and <span style="font-family: monospace;">"%13.7g"</span> for output coordinates in
  radians.
  </dd>
  </dl>
  <dl id="l_xformat">
  <dt><b>xformat = <span style="font-family: monospace;">""</span>, yformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xformat' Line='xformat = "", yformat = ""' -->
  <dd>The default output format of the transformed coordinates in xcolumn and
  ycolumn. The default is <span style="font-family: monospace;">"%10.3f"</span>.
  </dd>
  </dl>
  <dl id="l_min_sigdigits">
  <dt><b>min_sigdigits = 7</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='min_sigdigits' Line='min_sigdigits = 7' -->
  <dd>The minimum precision of the output coordinates.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  CCSTD transforms the list of input coordinates in the
  text file <i>input</i> and writes the transformed
  coordinates to the text file <i>output</i>. The input coordinates
  are read from and the output coordinates written to, the columns
  <i>xcolumn</i>, <i>ycolumn</i>, <i>lngcolumn</i>, and <i>latcolumn</i>
  in the input and output
  files. The format of the output coordinates can be specified using the
  <i>xformat</i>, <i>yformat</i>, <i>lngformat</i> and <i>latformat</i> parameters.
  If the output formats are unspecified the coordinates are written  out with
  reasonable default formats, e.g. <span style="font-family: monospace;">"%10.3f"</span> for standard coordinates,
  <span style="font-family: monospace;">"%12.2h"</span> and <span style="font-family: monospace;">"11.1h"</span> for celestial coordinates in hours or degrees,
  and <span style="font-family: monospace;">"%13.7g"</span> for celestial coordinates in radians. All the remaining
  fields in the
  input file are copied to the output file without modification. Blank lines
  and comment lines are also passed to the output file unaltered.
  </p>
  <p>
  The plate solution can either be read from record <i>solutions</i>
  in the database file <i>database</i> written by CCMAP, or specified
  by the user via the <i>xref</i>, <i>yref</i>, <i>xmag</i>, <i>ymag</i>,
  <i>xrotation</i>, <i>yrotation</i>, <i>lngref</i>, <i>latref</i>, 
  and <i>projection</i> parameters. <i>lngunits</i> and <i>latunits</i>
  define the units of the input celestial coordinates. If 
  undefined they default to the values in the database or to
  the quantities <span style="font-family: monospace;">"hours"</span> and <span style="font-family: monospace;">"degrees"</span> respectively. The standard coordinates
  are always written and read in units of arcseconds.
  </p>
  <p>
  If the <i>forward</i>
  parameter is <span style="font-family: monospace;">"yes"</span>, the input coordinates are assumed to be pixel coordinates
  and celestial coordinates. The pixel coordinates are transformed to standard
  coordinates using the plate solution, and celestial coordinates are
  transformed to standard coordinates using the position of the reference
  point <i>lngref</i>, <i>latref</i>, and the projection specified by
  <i>projection</i>. If <i>forward</i> is <span style="font-family: monospace;">"no"</span>, then
  the input coordinates are assumed to be standard coordinates and 
  those in <i>xcolumn</i> and <i>ycolumn</i> are transformed to pixel
  coordinates by inverting the plate solution, and those in <i>lngcolumn</i>
  and <i>latcolumn</i> are transformed to celestial coordinates using the
  position of the reference point and the specified projection.
  </p>
  <p>
  The plate solution computed by CCMAP has the following form where x and y
  are the pixel coordinates and xi and eta are the corresponding fitted standard
  coordinates in arcseconds per pixel. The observed standard coordinates are
  computed by applying the appropriate sky projection to the celestial
  coordinates.
  </p>
  <div class="highlight-default-notranslate"><pre>
   xi = f (x, y)
  eta = g (x, y)
  </pre></div>
  <p>
  The functions f and g are either power series, Legendre, or Chebyshev
  polynomials whose order and region of validity were set by the user when
  CCMAP was run. The plate solution is arbitrary and does not correspond to
  any physically meaningful model. However the first order terms can be given
  the simple geometrical interpretation shown below.
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
  xref, yref, xi0, and eta0 are the origins of the reference and output
  coordinate systems respectively. xi0 and eta0 are both 0.0 by default.
  xmag and ymag are the x and y scales in arcsec / pixel, and xrotation and yrotation
  are the x and y axes rotation angles measured counter-clockwise from original
  x and y axes.
  </p>
  <p>
  If the CCMAP database is undefined then CCSTD computes a linear plate
  solution using the parameters <i>xref</i>, <i>yref</i>, <i>xmag</i>,
  <i>ymag</i>, <i>xrotation</i>, <i>yrotation</i>, <i>lngref</i>, <i>latref</i>,
  <i>lngunits</i>, <i>latunits</i> and <i>projection</i> as shown below. Note
  that in this case xrotation and yrotation are interpreted as the rotation
  of the coordinates not the rotation of the coordinate axes.
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
  Linear plate solutions are evaluated in the forward and reverse sense
  using the appropriate IRAF mwcs system routines. Higher order plate
  solutions are evaluated in the forward sense using straight-forward
  evaluation of the polynomial terms, in the reverse sense by applying
  Newton's method to the plate solution.
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
  <div class="highlight-default-notranslate"><pre>
  1. Compute the standard coordinates in arcseconds per pixel given a list of
  pixel and equatorial coordinates and the position of the reference point in
  pixel and equatorial coordinates.
  
  cl&gt; type coords
  13:29:47.297  47:13:37.52  327.50  410.38
  13:29:37.406  47:09:09.18  465.50   62.10
  13:29:38.700  47:13:36.23  442.01  409.65
  13:29:55.424  47:10:05.15  224.35  131.20
  13:30:01.816  47:12:58.79  134.37  356.33
  
  cl&gt; ccstd coords STDOUT "" xref=256.5 yref=256.5 lngref=13:29:48.1 \
  latref = 47:11:53.4 xcol=3 ycol=4 lngcol=1 latcol=2
    -8.180   104.120    71.000   153.880
  -109.087  -164.189   209.000  -194.400
   -95.753   102.854   185.510   153.150
    74.688  -108.235   -32.150  -125.300
   139.745    65.441  -122.130    99.830
  
  2. Repeat the previous example but output the results in polar coordinates.
  The first and third columns contain the radius coordinate in arcseconds,
  the second and fourth columns contain the position angle in degrees measured
  counter-clockwise with respect to the standard coordinates.
  
  cl&gt; ccstd coords STDOUT "" xref=256.5 yref=256.5 lngref=13:29:48.1 \
  latref = 47:11:53.4 xcol=3 ycol=4 lngcol=1 latcol=2 polar+
  104.441    94.492   169.470    65.231
  197.124   236.400   285.434   317.073
  140.526   132.952   240.560    39.542
  131.504   304.608   129.359   255.609
  154.309    25.093   157.740   140.737
  
  3. Compute the plate solution and use it to evaluate the Cartesian and
  polar standard coordinates for the input coordinate list used in example 1.
  
  cl&gt; ccmap coords coords.db xcol=3 ycol=4 lngcol=1 latcol=2 inter-
  Coords File: coords  Image:
      Database: coords.db  Record: coords
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
  
  cl&gt; type coords.db
  # Mon 10:29:13 24-Nov-97
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
  
  cl&gt; ccstd coords STDOUT coords.db coords xcol=3 ycol=4 lngcol=1 latcol=2
    -8.471   104.146    -8.599   104.517
  -109.378  -164.163  -109.188  -164.100
   -96.044   102.880   -96.084   102.598
    74.397  -108.210    74.107  -108.269
   139.454    65.467   139.721    65.376
  
  cl&gt; ccstd coords STDOUT coords.db coords xcol=3 ycol=4 lngcol=1 latcol=2 \
  polar+
  104.490    94.650   104.870    94.704
  197.264   236.325   197.106   236.361
  140.744   133.032   140.565   133.122
  131.317   304.509   131.202   304.391
  154.056    25.148   154.259    25.075
  
  4. Use the previous plate solution to transform the pixel and equatorial
  coordinates to standard coordinates but enter the plate solution by hand.
  
  cl&gt; ccstd coords STDOUT "" xref=318.735 yref=273.900 lngref=13:29:48.129 \
  latref=47:11:53.37 xmag=.764 ymag=.767 xrot=180.890 yrot=1.042 xcol=3    \
  ycol=4 lngcol=1 latcol=2
    -8.475   104.150    -8.599   104.559
  -109.382  -164.159  -109.161  -164.165
   -96.048   102.884   -96.064   102.640
    74.393  -108.206    74.092  -108.313
   139.450    65.471   139.688    65.401
  
  cl&gt; ccstd coords STDOUT "" xref=318.735 yref=273.900 lngref=13:29:48.129 \
  latref=47:11:53.37 xmag=.764 ymag=.767 xrot=180.890 yrot=1.042 xcol=3    \
  ycol=4 lngcol=1 latcol=2 polar+
  104.494    94.652   104.912    94.702
  197.263   236.324   197.145   236.378
  140.750   133.032   140.582   133.105
  131.311   304.509   131.230   304.374
  154.054    25.150   154.240    25.089
  
  Note that there are minor differences between the results of examples 3 and
  4 due to precision differences in the input, and that the angles input
  to ccstd in example 4 are the coordinate rotation angles not the axes
  rotation angles as printed by ccmap. The difference is exactly 180 degrees
  in both cases.
  
  5. Use the plate solution computed in example 3 to convert a list
  of standard coordinates into the equivalent pixel and celestial coordinates.
  
  cl&gt; type stdcoords
    -8.471   104.146    -8.599   104.517
  -109.378  -164.163  -109.188  -164.100
   -96.044   102.880   -96.084   102.598
    74.397  -108.210    74.107  -108.269
   139.454    65.467   139.721    65.376
  
  cl&gt; ccstd stdcoords STDOUT coords.db coords xcol=3 ycol=4 lngcol=1 latcol=2  \
  forward-
  
  13:29:47.30 47:13:37.5   327.499   410.381
  13:29:37.41 47:09:09.2   465.500    62.101
  13:29:38.70 47:13:36.2   442.010   409.650
  13:29:55.42 47:10:05.1   224.350   131.200
  13:30:01.82 47:12:58.8   134.370   356.330
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ccmap, ccsetwcs, cctran, finder.tastrom, skyctran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'FORMATS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

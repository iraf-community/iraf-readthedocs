.. _cctran:

cctran: Transform coordinate lists using the ccmap plate solution
=================================================================

**Package: imcoords**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  cctran input output database solutions
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The coordinate files to be transformed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output coordinate files. The number of output files must
  be one or equal to the number of input files.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>The text database file written by the ccmap task containing the
  desired plate solution. If database is undefined cctran computes
  a linear plate solution using the current values of the xref, yref, xmag
  ymag, xrotation, yrotation, lngref, latref, and projection parameters.
  </dd>
  </dl>
  <dl id="l_solutions">
  <dt><b>solutions</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='solutions' Line='solutions' -->
  <dd>The database record containing the desired plate solution. 
  The number of records must be one or equal to the number of input coordinate
  files. Solutions is either a user name supplied to ccmap, the name of the
  ccmap task
  input image for which the plate solution is valid, or the name of the
  coordinate file that the ccmap task used to compute the plate solution.
  The quantities stored in
  solutions always supersede the values of xref, yref, xmag, ymag,
  xrotation, yrotation, lngref, latref, and projection.
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
  <dd>Transform the coordinates using only the linear part of the plate solution.
  </dd>
  </dl>
  <dl>
  <dt><b>geometric</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='geometric' Line='geometric' -->
  <dd>Transform the coordinates using the full plate solution.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_forward">
  <dt><b>forward = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='forward' Line='forward = yes' -->
  <dd>Transform from pixel to celestial coordinates ? If forward is <span style="font-family: monospace;">"no"</span> then
  the plate solution is inverted and celestial coordinates are transformed
  to pixel coordinates.
  </dd>
  </dl>
  <dl id="l_xref">
  <dt><b>xref = INDEF, yref = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xref' Line='xref = INDEF, yref = INDEF' -->
  <dd>The x and y pixel coordinates of the reference point. If database is undefined
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
  respect to the x and y axes. Xrotation and yrotation are interpreted as the
  rotation of the coordinates with respect to the x and y axes and default to
  0.0 and 0.0 degrees. For example xrotation and yrotation values of 30.0 and
  30.0 degrees will rotate a point 30 degrees counter-clockwise with respect to
  the x and y axes. To flip the x axis coordinates in this case either set the
  angles to 210.0 and 30.0 degrees or leave the angles at 30.0 and 30.0 and set
  the xmag parameter to a negative value. To set east to the up, down, left, and
  right directions, set xrotation to 90, 270, 180, and 0 respectively. To set
  north to the up, down, left, and right directions, set yrotation to  0, 180,
  90, and 270 degrees respectively. Any global rotation must be added to both the
  xrotation and yrotation values.
  </dd>
  </dl>
  <dl id="l_lngref">
  <dt><b>lngref = INDEF, latref = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngref' Line='lngref = INDEF, latref = INDEF' -->
  <dd>The celestial coordinates of the reference point, e.g. the ra and dec
  of the reference point for equatorial systems, galactic longitude and
  latitude for galactic systems. If database is undefined
  lngref and latred default to 0.0 and 0.0, otherwise these parameters are
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
  <dd>The sky projection geometry. The most commonly used projections in
  astronomy are <span style="font-family: monospace;">"tan"</span>, <span style="font-family: monospace;">"arc"</span>, <span style="font-family: monospace;">"sin"</span>, and <span style="font-family: monospace;">"lin"</span>. Other supported projections
  are <span style="font-family: monospace;">"ait"</span>, <span style="font-family: monospace;">"car"</span>, <span style="font-family: monospace;">"csc"</span>, <span style="font-family: monospace;">"gls"</span>, <span style="font-family: monospace;">"mer"</span>, <span style="font-family: monospace;">"mol"</span>, <span style="font-family: monospace;">"par"</span>, <span style="font-family: monospace;">"pco"</span>, <span style="font-family: monospace;">"qsc"</span>, <span style="font-family: monospace;">"stg"</span>,
  <span style="font-family: monospace;">"tsc"</span>, and <span style="font-family: monospace;">"zea"</span>.
  </dd>
  </dl>
  <dl id="l_xcolumn">
  <dt><b>xcolumn = 1, ycolumn = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcolumn' Line='xcolumn = 1, ycolumn = 2' -->
  <dd>The columns in the input coordinate file containing the x and y coordinates
  if the <i>forward</i> parameter is <span style="font-family: monospace;">"yes"</span>, the celestial ra / longitude and
  dec / latitude if the forward parameter is <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_lngformat">
  <dt><b>lngformat = <span style="font-family: monospace;">""</span>, latformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngformat' Line='lngformat = "", latformat = ""' -->
  <dd>The format of the output coordinates. The defaults are <span style="font-family: monospace;">"%10.3f"</span> for 
  output coordinates in pixels, <span style="font-family: monospace;">"%12.2h"</span> for coordinates in hours,
  <span style="font-family: monospace;">"%11.1h"</span> for coordinates in degrees,
  and <span style="font-family: monospace;">"%13.7g"</span> for coordinates in radians.
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
  CCTRAN applies the plate solution to a list of pixel or celestial
  coordinates in the text file <i>input</i> and writes the transformed
  coordinates to the text file <i>output</i>. The input coordinates
  are read from and the output coordinates written to, the columns
  <i>xcolumn</i> and <i>ycolumn</i> in the input and output
  files. The format of the output coordinates can be specified using the
  <i>lngformat</i> and <i>latformat</i> parameters. If the output formats
  are unspecified the coordinates are written  out with reasonable
  default precisions, e.g. <span style="font-family: monospace;">"%10.3f"</span> for pixel coordinates, <span style="font-family: monospace;">"%12.2h"</span> and <span style="font-family: monospace;">"11.1h"</span>
  for coordinates in hours or degrees,
  and <span style="font-family: monospace;">"%13.7g"</span> for coordinates in radians. All the remaining fields in the
  input file are copied to the output file without modification. Blank lines
  and comment lines are also passed to the output file unaltered.
  </p>
  <p>
  The plate solution is either read from record <i>solutions</i>
  in the database file <i>database</i> written by CCMAP, or specified
  by the user via the <i>xref</i>, <i>yref</i>, <i>xmag</i>, <i>ymag</i>,
  <i>xrotation</i>, <i>yrotation</i>, <i>lngref</i>, <i>latref</i>, 
  and <i>projection</i> parameters. If <i>Lngunits</i> and <i>latunits</i>
  are undefined they default to the values in the database or to
  the quantities <span style="font-family: monospace;">"hours"</span> and <span style="font-family: monospace;">"degrees"</span> respectively.
  If the <i>forward</i>
  parameter is <span style="font-family: monospace;">"yes"</span>, the input coordinates are assumed to be pixel coordinates
  and are transformed to celestial coordinates. If <i>forward</i> is <span style="font-family: monospace;">"no"</span>, then
  the input coordinates are assumed to be celestial coordinates and are
  transformed to pixel coordinates.
  </p>
  <p>
  The transformation computed by CCMAP has the following form where x and y
  are the pixel coordinates and xi and eta are the corresponding standard
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
  If the CCMAP database is undefined then CCTRAN computes a linear plate
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
  <p>
  1. Compute the plate solution and evaluate the forward transformation for
  the following input coordinate list.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type coords
  13:29:47.297  47:13:37.52  327.50  410.38
  13:29:37.406  47:09:09.18  465.50   62.10
  13:29:38.700  47:13:36.23  442.01  409.65
  13:29:55.424  47:10:05.15  224.35  131.20
  13:30:01.816  47:12:58.79  134.37  356.33
  
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
  
  cl&gt; cctran coords STDOUT coords.db coords xcol=3 ycol=4 lngformat=%0.3h \
  latformat=%0.2h
  13:29:47.297  47:13:37.52 13:29:47.284 47:13:37.89
  13:29:37.406  47:09:09.18 13:29:37.425 47:09:09.24
  13:29:38.700  47:13:36.23 13:29:38.696 47:13:35.95
  13:29:55.424  47:10:05.15 13:29:55.396 47:10:05.09
  13:30:01.816  47:12:58.79 13:30:01.842 47:12:58.70
  
  cl&gt; cctran coords STDOUT coords.db coords xcol=1 ycol=2 forward-
  327.341   409.894  327.50  410.38
  465.751    62.023  465.50   62.10
  441.951   410.017  442.01  409.65
  223.970   131.272  224.35  131.20
  134.717   356.454  134.37  356.33
  </pre></div>
  <p>
  Note that for the forward transformation the original ras and decs are in
  columns 1 and 2 and the computed ras and decs are in columns 3 and 4, but
  for the reverse transformation the original x and y values are in columns
  3 and 4 and the computed values are in columns 1 and 2.
  </p>
  <p>
  2. Use the previous plate solution to transform x and y values to
  ra and dec values and vice versa but enter the plate solution by hand.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cctran coords STDOUT "" xcol=3 ycol=4 lngformat=%0.3h latformat=%0.2h \
  xref=318.735 yref=273.900 lngref=13:29:48.129 latref=47:11:53.37 \
  xmag=.764 ymag=.767 xrot=180.890 yrot=1.042
  13:29:47.297  47:13:37.52 13:29:47.285 47:13:37.93
  13:29:37.406  47:09:09.18 13:29:37.428 47:09:09.17
  13:29:38.700  47:13:36.23 13:29:38.698 47:13:35.99
  13:29:55.424  47:10:05.15 13:29:55.395 47:10:05.04
  13:30:01.816  47:12:58.79 13:30:01.839 47:12:58.72
  
  cl&gt; cctran coords STDOUT "" xcol=1 ycol=2 xref=318.735 yref=273.900 \
  lngref=13:29:48.129 latref=47:11:53.37 xmag=.764 ymag=.767 \
  xrot=180.890 yrot=1.042 forward-
  327.347   409.845  327.50  410.38
  465.790    62.113  465.50   62.10
  441.983   409.968  442.01  409.65
  223.954   131.334  224.35  131.20
  134.680   356.426  134.37  356.33
  </pre></div>
  <p>
  Note that there are minor differences between examples 1 and 2 due to
  precision differences in the input, and that the angles input to cctran
  in example 2 are the coordinate rotation angles not the axes rotation angles
  as printed by ccmap. The different is exactly 180 degrees in both cases.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ccmap, ccsetwcs, finder.tastrom, skyctran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'FORMATS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

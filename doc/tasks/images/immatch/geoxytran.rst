.. _geoxytran:

geoxytran: Transform coordinate lists using the geomap transforms
=================================================================

**Package: immatch**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  geoxytran input output database transforms
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input coordinate files to be transformed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The list of output transformed coordinate files. The number of output files must
  be one or equal to the number of input files.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>The name of the text database file written by the geomap task which
  contains the desired spatial transformation.
  If database is undefined geoxytran computes
  a linear transformation using the current
  values of the xref, yref, xout, yout, xshift, yshift, xmag, ymag, xrotation,
  and yrotation parameters.
  </dd>
  </dl>
  <dl id="l_transforms">
  <dt><b>transforms</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='transforms' Line='transforms' -->
  <dd>The database record containing the desired spatial transformation. 
  The number of records must be one or equal to the number of input coordinate
  files. Transforms is usually the name of the coordinate file that the
  geomap task used to compute the spatial transformation.
  If defined the values of xref, yref, xout, yout, xshift, yshift, xmag, ymag,
  xrotation, and yrotation will supersede the computed values in the
  database file.
  </dd>
  </dl>
  <dl id="l_geometry">
  <dt><b>geometry = <span style="font-family: monospace;">"geometric"</span> (linear|geometric)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='geometry' Line='geometry = "geometric" (linear|geometric)' -->
  <dd>The type of geometric transformation. The geometry parameter is
  only requested if database is defined. The options are:
  <dl>
  <dt><b>linear</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='linear' Line='linear' -->
  <dd>Perform only the linear part of the spatial transformation.
  </dd>
  </dl>
  <dl>
  <dt><b>geometric</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='geometric' Line='geometric' -->
  <dd>Compute both the linear and distortion portions of the spatial transformation.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_direction">
  <dt><b>direction = <span style="font-family: monospace;">"forward"</span> (forward|backward)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='direction' Line='direction = "forward" (forward|backward)' -->
  <dd>The transformation direction may be <span style="font-family: monospace;">"forward"</span> or <span style="font-family: monospace;">"backward"</span>.  The forward
  direction directly evaluates the database solution.  The backward
  direction iteratively determines the coordinate which evaluates to the
  specified coordinate.
  </dd>
  </dl>
  <dl id="l_xref">
  <dt><b>xref = INDEF, yref = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xref' Line='xref = INDEF, yref = INDEF' -->
  <dd>The x and y coordinates of the reference origin.
  If the database file is undefined xref and
  yref  default to [0.0,0.0]. Otherwise xref and yref
  default to the mean of minimum and maximum x and y values
  [(xmin + xmax) / 2.0, (ymin + ymax) / 2.0] computed by geomap.
  </dd>
  </dl>
  <dl id="l_xmag">
  <dt><b>xmag = INDEF, ymag = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmag' Line='xmag = INDEF, ymag = INDEF' -->
  <dd>The x and y scale factors in input units
  per reference unit. If database is undefined xmag and ymag
  default to [1.0, 1.0]. Otherwise xmag and ymag default to the values computed
  by geomap. 
  </dd>
  </dl>
  <dl id="l_xrotation">
  <dt><b>xrotation = INDEF, yrotation = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xrotation' Line='xrotation = INDEF, yrotation = INDEF' -->
  <dd>The x and y rotation angles in degrees measured counter-clockwise with
  respect to the x and y axes. If database
  is undefined then xrotation and yrotation are interpreted as the
  rotation of the coordinates with respect to the x and y axes and
  default to [0.0, 0.0]. For example xrotation and yrotation values of
  [30.0, 30.0] will rotate a point 30 counter-clockwise with respect
  to the x and y axes.  Otherwise xrotation and yrotation default to the
  values computed by geomap. Geomap computes the x and y rotation angles
  of the x and y axes, not the rotation angle of the coordinates. An output
  coordinate system rotated 30 degrees counter-clockwise with respect
  to the reference coordinate system will produce xrotation and yrotation
  values of [330.0,330.0] or equivalently [-30.0,-30.0] in the database file
  not [30.0,30.0].
  </dd>
  </dl>
  <dl id="l_xout">
  <dt><b>xout = INDEF, yout = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xout' Line='xout = INDEF, yout = INDEF' -->
  <dd>The x and y coordinates of the output origin.
  If the database file is undefined xout and
  yout  default to [0.0,0.0].
  If database is defined xout and yout
  default to the position that the reference origin [xref,yref]
  occupies in the transformed system.
  </dd>
  </dl>
  <dl id="l_xshift">
  <dt><b>xshift = INDEF, yshift = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xshift' Line='xshift = INDEF, yshift = INDEF' -->
  <dd>The x and y shift of the reference origin in output units.
  If the database file is undefined xshift and yshift default to [0.0,0.0].
  If the database file is defined xshift and yshift default to the
  values computed by geomap. If defined xshift and yshift take precedence over
  the x and y shifts determined from xref, yref, xout and yout.
  </dd>
  </dl>
  <dl id="l_xcolumn">
  <dt><b>xcolumn = 1, ycolumn = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcolumn' Line='xcolumn = 1, ycolumn = 2' -->
  <dd>The columns in the input coordinate file containing the x and y coordinates.
  </dd>
  </dl>
  <dl id="l_calctype">
  <dt><b>calctype = <span style="font-family: monospace;">"real"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='calctype' Line='calctype = "real"' -->
  <dd>The precision of the coordinate transformation calculations. The options
  are <span style="font-family: monospace;">"real"</span> and <span style="font-family: monospace;">"double"</span>.  Note that this only applies to a <span style="font-family: monospace;">"forward"</span>
  transformation.  The <span style="font-family: monospace;">"backward"</span> transformation is done iteratively and
  is always calculated in double precision to get the best convergence.
  </dd>
  </dl>
  <dl id="l_xformat">
  <dt><b>xformat = <span style="font-family: monospace;">""</span>, yformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xformat' Line='xformat = "", yformat = ""' -->
  <dd>The default output format for the computed x and y coordinates. If
  xformat and yformat are undefined geoxytran outputs the coordinates
  using the maximum of the precision of the input coordinates
  and the value of the <i>min_sigdigits</i> parameter.
  </dd>
  </dl>
  <dl id="l_min_sigdigits">
  <dt><b>min_sigdigits = 7</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='min_sigdigits' Line='min_sigdigits = 7' -->
  <dd>The minimum precision of the output x and y coordinates.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  GEOXYTRAN applies  a coordinate transformation to a list of reference
  coordinates in the text file <i>input</i> and writes the transformed
  coordinates to the text file <i>output</i>. The input  coordinates
  are read from, and the output coordinates written to, columns
  <i>xcolumn</i> and <i>ycolumn</i> in the input and output
  files. The format of the output coordinates can be specified using the
  <i>xformat</i> and <i>yformat</i> parameters. If the output formats
  are unspecified the coordinates are written out with a precision
  which is the maximum of the precision of the input coordinates
  and the value of the <i>min_sigdigits</i> parameter. All remaining fields in
  the input file are copied to the output file without modification.
  Blank lines and comment lines are also passed to the output file
  unaltered.
  </p>
  <p>
  The coordinate transformation either be read from record <i>transforms</i>
  in the database file <i>database</i> computed by GEOMAP, or specified
  by the user via the <i>xref</i>, <i>yref</i>, <i>xmag</i>, <i>ymag</i>,
  <i>xrotation</i>, <i>yrotation</i>, <i>xout</i>, <i>yout</i>, <i>xshift</i>,
  and <i>yshift</i> parameters.
  </p>
  <p>
  The transformation computed by GEOMAP has the following form.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xout = f (xref, yref)
  yout = g (xref, yref)
  </pre></div>
  <p>
  The functions f and g are either a power series polynomial or a Legendre
  or Chebyshev polynomial surface whose order and region of validity were
  set by the user when GEOMAP was run. The computed transformation is
  arbitrary and does not correspond to any physically meaningful model.
  However the first order terms can be given the simple geometrical
  interpretation shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xout = a + b * xref + c * yref
  yout = d + e * xref + f * yref
     b = xmag * cos (xrotation)
     c = ymag * sin (yrotation)
     e = -xmag * sin (xrotation)
     f = ymag * cos (yrotation)
     a = x0 - b * xref0 - c * yref0 = xshift
     d = y0 - e * xref0 - f * yref0 = xshift
  </pre></div>
  <p>
  Xref0, yref0, x0, and
  y0 are the origins of the reference and output coordinate systems
  respectively. xmag and ymag are the x and y scale factors in output units
  per reference unit and xrotation and yrotation are the rotation angles measured
  counter-clockwise of the x and y axes.
  </p>
  <p>
  The linear portion of the GEOMAP transformation may be altered after the fact
  by setting some or all of the parameters <i>xref</i>, <i>yref</i>, <i>xout</i>,
  <i>yout</i>, <i>xshift</i>, <i>yshift</i>, <i>xmag</i>, <i>ymag</i>, <i>xrotation</i>,
  and <i>yrotation</i>. If defined these parameters will replace the corresponding
  values in the GEOMAP database file.
  Xref, yref, xshift, yshift, xout and yout can be used to redefine the shift
  where xshift and yshift take precedence over xref, yref, xout and yout.
  Xmag, and ymag can be used to reset the scale of the transformation.
  Xrotation and yrotation can be used to redefine the orientation of the
  transformation. Note that xrotation and yrotation are interpreted as
  the rotation of the coordinate axes not the coordinates.
  The default values of these parameters are.
  </p>
  <div class="highlight-default-notranslate"><pre>
       xref = (xmin + xmax) / 2.0
       yref = (ymin + ymax) / 2.0
       xout = f (xref,yref)
       yout = g (xref,yref)
     xshift = xshift (database) = xout - f(xref,yref)
     yshift = yshift (database) = yout - g(xref,yref)
       xmag = xmag (database)
       ymag = ymag (database)
  xrotation = xrotation (database)
  yrotation = yrotation (database)
  </pre></div>
  <p>
  If the GEOMAP database is undefined then GEOXYTRAN performs a linear
  transformation on the input coordinates using the parameters
  <i>xref</i>, <i>yref</i>, <i>xmag</i>, <i>ymag</i>, <i>xrotation</i>,
  <i>yrotation</i>, <i>xout</i>, <i>yout</i>, <i>xshift</i>, and
  <i>yshift</i> as shown below. Note that in this case xrotation and
  yrotation are interpreted as the rotation of the coordinates
  themselves not the coordinate axes.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xout = a + b * xref + c * yref
  yout = d + e * xref + f * yref
     b = xmag * cos (xrotation)
     c = -ymag * sin (yrotation)
     e = xmag * sin (xrotation)
     f = ymag * cos (yrotation)
     a = xo - b * xref0 - c * yref0 = xshift
     d = yo - e * xref0 - f * yref0 = xshift
  </pre></div>
  </section>
  <section id="s_forward_vs__backward_transformations">
  <h3>Forward vs. backward transformations</h3>
  <p>
  The transformation direction is specified by the <i>direction</i> parameter
  which may take the values <span style="font-family: monospace;">"forward"</span> or <span style="font-family: monospace;">"backward"</span>.  The forward transformation
  is a direct evaluation of the database solution.  The backward
  transformation is an iterative evaluation to obtain the coordinate which
  evaluates to the desired coordinate.
  </p>
  <p>
  When the same solution is used with <b>geotran</b> to transform an image
  to another image matching the <span style="font-family: monospace;">"reference"</span> image is needed to obtain
  coordinates in the transformed image.  This is because the transformation
  is produced with <b>geomap</b> to map <span style="font-family: monospace;">"reference"</span> coordinates to the
  image which is subsequently transformed.  Therefore, if you have coordinates
  in the image which has been transformed then you should use the <span style="font-family: monospace;">"backward"</span>
  transformation to get coordinates for the transformed image.  But if you
  have standard coordinates from the reference image being matched then you
  would use the <span style="font-family: monospace;">"forward"</span> transformation.  If you are not sure then you can
  use <b>tvmark</b> to overlay the results to find which direction produces
  the desired coordinates.
  </p>
  <p>
  Because the backward transformation is performed iteratively it can be
  slow.  If higher speeds are desired, such as when evaluating a very
  large number of coordinates, one might create a transformation solution
  that can be evaluated in the forward direction.  This is done by
  using <b>geomap</b> with the reference and target coordinates reversed.
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
  1. Compute the transformation from the reference system to the output
  system and then evaluate the transformation for both the input list and
  the list of unknowns.
  
     cl&gt; type rtran
  
          1.0000  1.0000 184.1445 -153.0376
          512.0000 1.0000 684.0376 184.1445
          512.0000 512.0000 346.8555 684.0376
          1.0000 512.0000 -153.0380 346.8555
  
      cl&gt; geomap rtran rtran.db 1.0 512.0 1.0 512.0 intera-
  
      cl&gt; type rtran.db
  
          # Tue 14:53:36 18-Apr-95
          begin   rtran
                  output          rtran.db
                  xrefmean        256.5
                  yrefmean        256.5
                  xmean           265.4999
                  ymean           265.5
                  xshift          183.826
                  yshift          -154.6757
                  xmag            1.180001
                  ymag            1.179999
                  xrotation       326.
                  yrotation       326.
                  surface1        11
                                  3.      3.
                                  2.      2.
                                  2.      2.
                                  0.      0.
                                  1.      1.
                                  512.    512.
                                  1.      1.
                                  512.    512.
                                  183.826 -154.6757
                                  0.9782647       0.6598474
                                  -0.6598479      0.9782643
                  surface2        0
  
      cl&gt; geoxytran rtran STDOUT rtran.db rtran
  
          184.1444 -153.038 184.1445 -153.0376
          684.0377 184.1444 684.0376 184.1445
          346.8554 684.0375 346.8555 684.0376
          -153.038 346.8555 -153.038 346.8555
  
      cl&gt; geoxytran unknowns unknowns.tran rtran.db rtran
  
  2.  Evaluate the backward transformation to take coordinates from the
  output system to the reference system.  In this example we use the
  output of the first example to illustrate getting back the coordinates
  used in the original geomap input.
  
      cl&gt; geoxytran rtran STDOUT rtran.db rtran dir=forward |\
      &gt;&gt;&gt; geoxytran STDIN STDOUT rtran.db rtran dir=backward
      0.999798 0.9997257 184.1445 -153.0376
          512. 0.9999674 684.0376 184.1445
          512.     512. 346.8555 684.0376
      0.999918 512.0001 -153.0380 346.8555
  
  3. Evaluate the transform computed in example 1 for the same list of
  unknowns but modify the transformation slightly by setting xmag
  and ymag to 1.18 and 1.18 exactly.
  
      cl&gt; geoxytran unknowns unknowns.tran rtran.db rtran xmag=1.18 \
          ymag=1.18
  
  4. Evaluate the same transformation for the same unknowns as before
  using the linear transformation parameters not the transform computed
  by geomap. Note that the angle is the negative of the one defined
  in the database file.
  
      cl&gt; geoxytran unknowns unknowns.tran "" xmag=1.18 ymag=1.18 \
          xrot=34 yrot=34 xshift=183.826 yshift=-154.6757
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  geomap, lists.lintran, geotran, gregister
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'Forward vs. Backward Transformations' 'FORMATS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

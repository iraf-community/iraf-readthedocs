.. _xyxymatch:

xyxymatch: Match pixel coordinate lists
=======================================

**Package: immatch**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xyxymatch input reference output tolerance
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input coordinate files.  The input file is a whitespace-delimited
  text table containing the coordinates.  The <i>xcolumn</i> and <i>ycolumn</i> 
  parameters define the coordinate columns to be used.
  </dd>
  </dl>
  <dl id="l_reference">
  <dt><b>reference</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reference' Line='reference' -->
  <dd>The list of reference coordinate files. The number of reference coordinate
  files must be one or equal to the number of input coordinate files.
  The reference file is a whitespace-delimited
  text table containing the coordinates.  The <i>xrcolumn</i> and <i>yrcolumn</i> 
  parameters define the coordinate columns to be used.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output matched x-y lists containing three pairs of numbers: the coordinates
  of the object in the reference list in columns 1 and 2, the
  coordinates of the object in the input list in columns 3 and 4, and
  the line number of the objects in the original reference and input
  lists in columns 5 and 6.
  </dd>
  </dl>
  <dl id="l_tolerance">
  <dt><b>tolerance</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tolerance' Line='tolerance' -->
  <dd>The matching tolerance in pixels.
  </dd>
  </dl>
  <dl id="l_refpoints">
  <dt><b>refpoints = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refpoints' Line='refpoints = ""' -->
  <dd>The list of tie points used to compute the linear transformation
  from the input coordinate system to the reference coordinate system. Refpoints
  is a text file containing the x-y coordinates of 1-3 reference list tie points
  in the first line, followed by the x-y coordinates of the 1-3 corresponding
  input tie points in succeeding
  lines. If refpoints is undefined then the parameters <i>xin</i>, <i>yin</i>,
  <i>xmag</i>, <i>ymag</i>, <i>xrotation</i>, <i>yrotataion</i>, <i>xref</i>,
  and <i>yref</i> are used to compute the linear transformation from the
  input coordinate system to the reference coordinate system.
  </dd>
  </dl>
  <dl id="l_xin">
  <dt><b>xin = INDEF, yin = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xin' Line='xin = INDEF, yin = INDEF' -->
  <dd>The x and y origin of the input coordinate system. Xin and yin default to 
  0.0 and 0.0 respectively.
  </dd>
  </dl>
  <dl id="l_xmag">
  <dt><b>xmag = INDEF, ymag = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmag' Line='xmag = INDEF, ymag = INDEF' -->
  <dd>The x and y scale factors in reference pixels per input pixels. Xmag and
  ymag default to 1.0 and 1.0 respectively.
  </dd>
  </dl>
  <dl id="l_xrotation">
  <dt><b>xrotation = INDEF, yrotation = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xrotation' Line='xrotation = INDEF, yrotation = INDEF' -->
  <dd>The x and y rotation angles measured in degrees counter-clockwise with
  respect to the x axis. Xrotation and yrotation default to 0.0 and 0.0
  respectively.
  </dd>
  </dl>
  <dl id="l_xref">
  <dt><b>xref = INDEF, yref = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xref' Line='xref = INDEF, yref = INDEF' -->
  <dd>The x and y origin of the reference coordinate system. Xref and yref default
  to 0.0 and 0.0 respectively.
  </dd>
  </dl>
  <dl id="l_xcolumn">
  <dt><b>xcolumn = 1, ycolumn = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcolumn' Line='xcolumn = 1, ycolumn = 2' -->
  <dd>The columns in the input coordinate list containing the x and y coordinate
  values respectively.
  </dd>
  </dl>
  <dl id="l_xrcolumn">
  <dt><b>xrcolumn = 1, yrcolumn = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xrcolumn' Line='xrcolumn = 1, yrcolumn = 2' -->
  <dd>The columns in the reference coordinate list containing the x and y coordinate
  values respectively.
  </dd>
  </dl>
  <dl id="l_separation">
  <dt><b>separation = 9.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='separation' Line='separation = 9.0' -->
  <dd>The minimum separation for objects in the input and reference coordinate
  lists. Objects closer together than separation pixels
  are removed from the input and reference coordinate lists prior to matching.
  </dd>
  </dl>
  <dl id="l_matching">
  <dt><b>matching = <span style="font-family: monospace;">"triangles"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='matching' Line='matching = "triangles"' -->
  <dd>The matching algorithm. The choices are:
  <dl>
  <dt><b>tolerance</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='tolerance' Line='tolerance' -->
  <dd>A linear transformation is applied to the input coordinate list,
  the transformed input list and the reference list are sorted, 
  points which are too close together are removed, and the input coordinates
  which most closely match the reference coordinates within the
  user specified tolerance are determined.  The tolerance algorithm requires
  an initial estimate for the linear transformation.  This estimate can be
  derived interactively by pointing to common objects in the two displayed
  images, by supplying the coordinates of tie points via the
  <i>refpoints</i> file, or by setting the linear transformation parameters
  <i>xin</i>, <i>yin</i>, <i>xmag</i>, <i>ymag</i>, <i>xrotation</i>,
  <i>yrotation</i>, <i>xref</i>, and <i>yref</i>. Assuming that
  well chosen tie points are supplied, the tolerance algorithm 
  functions well in the presence of any shifts, axis flips, x and y
  scale changes, rotations, and axis skew, between the two coordinate
  systems. The algorithm is sensitive to higher order distortion terms
  in the coordinate transformation.
  </dd>
  </dl>
  <dl>
  <dt><b>triangles</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='triangles' Line='triangles' -->
  <dd>A linear transformation is applied to the input coordinate list,
  the transformed input list and the reference list are sorted, points
  which are too close together are removed, and  the input coordinates
  are matched to the reference coordinates using a triangle pattern
  matching technique and the user specified tolerance parameter.
  The triangles pattern matching algorithm does not require prior knowledge
  of the linear transformation, although it will use one if one is supplied.
  The algorithm functions well in the presence of
  any shifts, axis flips, magnification, and rotation between the two coordinate
  systems as long as both lists have a reasonable number of objects
  in common and the errors in the computed coordinates are small.
  However since the algorithm depends on comparisons of similar triangles, it
  is sensitive to differences in the x and y coordinate scales,
  any skew between the x and y axes, and higher order distortion terms
  in the coordinate transformation.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_nmatch">
  <dt><b>nmatch = 30</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nmatch' Line='nmatch = 30' -->
  <dd>The maximum number of reference and input coordinates used
  by the <span style="font-family: monospace;">"triangles"</span> pattern matching algorithm. If either list contains
  more coordinates than nmatch the lists are subsampled. Nmatch should be
  kept small as the computation and memory requirements of the <span style="font-family: monospace;">"triangles"</span>
  algorithm depend on a high power of the lengths of the respective lists.
  </dd>
  </dl>
  <dl id="l_ratio">
  <dt><b>ratio = 10.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ratio' Line='ratio = 10.0' -->
  <dd>The maximum ratio of the longest to shortest side of the 
  triangles generated by the <span style="font-family: monospace;">"triangles"</span> pattern matching algorithm.
  Triangles with computed longest to shortest side ratios &gt; ratio
  are rejected from the pattern matching algorithm. <i>ratio</i> should never
  be set higher than 10.0 but may be set as low as 5.0.
  </dd>
  </dl>
  <dl id="l_nreject">
  <dt><b>nreject = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nreject' Line='nreject = 10' -->
  <dd>The maximum number of rejection iterations for the <span style="font-family: monospace;">"triangles"</span> pattern
  matching algorithm.
  </dd>
  </dl>
  <dl id="l_xformat">
  <dt><b>xformat = <span style="font-family: monospace;">"%13.3f"</span>, yformat = <span style="font-family: monospace;">"%13.3f"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xformat' Line='xformat = "%13.3f", yformat = "%13.3f"' -->
  <dd>The format of the output reference and input x and y coordinates.
  By default the coordinates are output right justified in a field of
  13 characters with 3 places following the decimal point.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Compute the initial linear transformation required to transform the
  input coordinate coordinates to the reference coordinate system, by defining
  up to three tie points using the image display and the image cursor.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about the progress of the task ?
  </dd>
  </dl>
  <dl id="l_icommands">
  <dt><b>icommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='icommands' Line='icommands = ""' -->
  <dd>The image display cursor.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XYXYMATCH matches the x and y coordinates in the reference coordinate list
  <i>reference</i> to the corresponding x and y coordinates in the input
  coordinate list <i>input</i> to within a user specified tolerance
  <i>tolerance</i>, and writes the matched coordinates to the output
  file <i>output</i>.  The output file is suitable for input to the 
  GEOMAP task which computes the actual transformation required to
  register the corresponding reference and input images.
  </p>
  <p>
  XYXYMATCH matches the coordinate lists by: 1) computing an initial
  guess at the linear transformation required to match the input
  coordinate system to the reference coordinate system, 2) applying
  the computed transformation to the input coordinates, 3) sorting
  the reference and input coordinates and removing points with a
  minimum separation specified by the parameter <i>separation</i>
  from both lists, 4) matching the two lists using either the <span style="font-family: monospace;">"tolerance"</span>
  or <span style="font-family: monospace;">"triangles"</span> algorithm, and 5) writing the matched list to the
  output file.
  </p>
  <p>
  The initial estimate of the linear transformation is computed in one of 
  three ways.  If <i>interactive</i> is <span style="font-family: monospace;">"yes"</span> the user displays the reference and
  input images corresponding to the reference and input coordinate files
  on the image display, and marks up to three objects which the two
  images have in common with the image cursor. The coordinates of these
  tie points are used as tie points to compute the linear transformation.
  If <i>refpoints</i> is defined, the x-y coordinates of up to three tie
  points are read from succeeding lines in the refpoints file. The format
  of two sample refpoints files is shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # First sample refpoints file (1 reference file and N input files)
  
  x1 y1  [x2 y2 [x3 y3]]   # tie points for reference coordinate file
  x1 y1  [x2 y2 [x3 y3]]   # tie points for input coordinate file 1
  x1 y1  [x2 y2 [x3 y3]]   # tie points for input coordinate file 2
  x1 y1  [x2 y2 [x3 y3]]   # tie points for input coordinate file N
  
  # Second sample refpoints file (N reference files and N input files)
  
  x1 y1  [x2 y2 [x3 y3]]   # tie points for reference coordinate file 1
  x1 y1  [x2 y2 [x3 y3]]   # tie points for input coordinate file 1
  x1 y1  [x2 y2 [x3 y3]]   # tie points for reference coordinate file 2
  x1 y1  [x2 y2 [x3 y3]]   # tie points for input coordinate file 2
  x1 y1  [x2 y2 [x3 y3]]   # tie points for reference coordinate file N
  x1 y1  [x2 y2 [x3 y3]]   # tie points for input coordinate file N
  </pre></div>
  <p>
  The coordinates of the tie points can be typed in by hand if <i>refpoints</i>
  is <span style="font-family: monospace;">"STDIN"</span>. If the refpoints file is undefined the parameters
  <i>xin</i>, <i>xin</i>, <i>xmag</i>, <i>ymag</i>, <i>xrotation</i>, <i>yrotation</i>,
  <i>xref</i>, and <i>yref</i> are used to compute the linear transformation
  from the input coordinates [xi,yi] to the reference coordinates [xr,yr]
  as shown below. Orientation and skew are the orientation of the x and y axes
  and their deviation from non-perpendicularity respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xr = a + b * xi + c * yi
  yr = d + e * xi + f * yi
  
  xrotation = orientation - skew / 2
  yrotation = orientation + skew / 2
  b = xmag * cos (xrotation)
  c = -ymag * sin (yrotation)
  e = xmag * sin (xrotation)
  f = ymag * cos (yrotation)
  a = xref - b * xin - c * yin = xshift
  d = yref - e * xin - f * yin = yshift
  </pre></div>
  <p>
  The reference and input coordinates are read from columns <i>xrcolumn</i>,
  <i>yrcolumn</i> in the reference, and <i>xcolumn</i>, and <i>ycolumn</i> in the
  input coordinate lists respectively. The input coordinates are transformed
  using the computed linear transformation and stars closer together than
  <i>separation</i> pixels are removed from both lists.
  </p>
  <p>
  The coordinate lists are matched using the algorithm specified by
  the <i>matching</i>
  parameter. If matching is <span style="font-family: monospace;">"tolerance"</span>, XYXYMATCH searches the sorted
  transformed input coordinate list for the object closest to the current
  reference object within the matching tolerance <i>tolerance</i>.
  The major advantage of the <span style="font-family: monospace;">"tolerance"</span> algorithm is that it can deal
  with x and y scale differences and axis skew in the coordinate
  transformation. The major disadvantage is that the user must supply
  tie point information in all but the simplest case of small x and y
  shifts between the input and reference coordinate systems.
  </p>
  <p>
  If matching is <span style="font-family: monospace;">"triangles"</span> XYXYMATCH constructs a list of triangles
  using up to <i>nmatch</i> reference coordinates and transformed input
  coordinates, and performs a pattern matching operation on the resulting
  triangle lists. If the number of coordinates
  in both lists is less than <i>nmatch</i> the entire list is matched using
  the <span style="font-family: monospace;">"triangles"</span> algorithm directly, otherwise the <span style="font-family: monospace;">"triangles"</span> algorithm
  is used to estimate a new linear transformation, the input coordinate
  list is transformed using the new transformation, and the entire list
  is matched using the <span style="font-family: monospace;">"tolerance"</span> algorithm. The major advantage of the
  <span style="font-family: monospace;">"triangles"</span> algorithm is that it requires no tie point information
  from the user. The major disadvantages are that it is sensitive to
  x and y scale differences and axis skews between the input and reference
  coordinate systems and can be computationally expensive.
  </p>
  <p>
  The matched x and y reference and input coordinate lists are written to
  columns 1 and 2, and 3 and 4 of the output file respectively, in a format
  specified by the <i>xformat</i> and <i>yformat</i> parameters.
  The respective line numbers in the original reference and input
  coordinate files are written to columns 5 and 6 respectively.
  </p>
  <p>
  If <i>verbose</i> is yes, detailed messages about actions taken by the
  task are written to the terminal as the task executes.
  </p>
  </section>
  <section id="s_algorithms">
  <h3>Algorithms</h3>
  <p>
  The <span style="font-family: monospace;">"triangles"</span> algorithm uses a sophisticated pattern matching
  technique which requires no tie point information from the user.
  It is expensive computationally and hence is restricted to a maximum
  of <i>nmatch</i> objects from the reference and input coordinate lists.
  </p>
  <p>
  The <span style="font-family: monospace;">"triangles"</span> algorithm first generates a list
  of all the possible triangles that can be formed from the points in each list.
  For a list of nmatch points this number is the combinatorial factor
  nmatch! / [(nmatch-3)! * 3!] or  nmatch * (nmatch-1) * (nmatch-2) / 6.
  The length of the perimeter, ratio of longest to shortest side, cosine
  of the angle between the longest and shortest side, the tolerances in
  the latter two quantities and the direction of the arrangement of the vertices
  of each triangle are computed and stored in a table.
  Triangles with vertices closer together than <i>tolerance</i> or
  with a ratio of the longest to shortest side greater than <i>ratio</i>
  are discarded. The remaining triangles are sorted in order of increasing
  ratio.  A sort merge algorithm is used to match the triangles using the
  ratio and cosine information, the tolerances in these quantities, and
  the maximum tolerances for both lists. Next the ratios of the
  perimeters of the matched triangles are compared to the average ratio
  for the entire list, and triangles which deviate too widely from the mean
  are discarded. The number of triangles remaining are divided into
  the number which match in the clockwise sense and the number which match
  in the counter-clockwise sense. Those in the minority category
  are eliminated.
  The rejection step can be repeated up to <i>nreject</i> times or until
  no more rejections occur whichever comes first.
  The last step in the algorithm is a voting procedure in which each remaining
  matched triangle casts three votes, one for each matched pair of vertices.
  Points which have fewer than half the maximum number of
  votes are discarded. The final set of matches are written to the output file.
  </p>
  <p>
  The <span style="font-family: monospace;">"triangles"</span> algorithm functions well when the reference and
  input coordinate lists have a sufficient number of objects (~50%, 
  in some cases as low as 25%) of their objects in common, any distortions
  including x and y scale differences and skew between the two systems are small,
  and the random errors in the coordinates are small. Increasing the value of the
  <i>tolerance</i> parameter will increase the ability to deal with distortions but
  will also produce more false matches.
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
  <section id="s_references">
  <h3>References</h3>
  <p>
  A detailed description of the <span style="font-family: monospace;">"triangles"</span> pattern matching algorithm used here
  can be found in the article <span style="font-family: monospace;">"A Pattern-Matching Algorithm for Two-
  Dimensional Coordinate Lists"</span> by E.J. Groth, A.J. 91, 1244 (1986).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Match the coordinate list of an image to the coordinate list of a reference
  image using the triangles matching algorithm and a tolerance of 3 pixels.
  Use the resulting matched list to compute the transformation
  required to register the input image lpix to the reference image.
  For completeness this example demonstrates how the individual input
  and reference coordinate lists can be generated.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imlintran dev$pix[-*,*] lpix xrot=15 yrot=15 xmag=1.2 \
      ymag=1.2 xin=INDEF yin=INDEF xref=265.0 yref=265.0  \
      ncols=INDEF nlines=INDEF
  
  cl&gt; daofind dev$pix fwhm=2.5 sigma=5.0 threshold=100.0
  cl&gt; daofind lpix fwhm=2.5 sigma=5.0 threshold=100.0
  
  cl&gt; xyxymatch lpix.coo.1 pix.coo.1 xymatch toler=3     \
      matching=triangles
  
  cl&gt; geomap xymatch geodb 1.0 512.0 1.0 512.0
  </pre></div>
  <p>
  2. Match the coordinate lists above using the tolerance matching algorithm
  and the image display and cursor.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; display dev$pix 1 fi+
  cl&gt; display lpix 2 fi+
  
  cl&gt; xyxymatch lpix.coo.1 pix.coo.1 xymatch toler=3     \
      matching=tolerance interactive+
  
      ... Mark three points in the reference image dev$pix
      ... Mark three points in the input image lpix
  
  cl&gt; geomap xymatch geodb 1.0 512.0 1.0 512.0
  </pre></div>
  <p>
  3. Repeat example 2 but run xyxymatch non-interactively by setting the
  appropriate linear transformation parameters rather than marking stars
  on the image display.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ...
  
  cl&gt; xyxymatch lpix.coo.1 pix.coo.1 xymatch toler=3     \
      matching=tolerance xmag=1.2 ymag=1.2 xrot=165       \
      yrot=345 xref=646.10 yref=33.38
  
  cl&gt; geomap xymatch geodb 1.0 512.0 1.0 512.0
  </pre></div>
  <p>
  4. Repeat example 2 but run xyxymatch non-interactively
  inputting the appropriate linear transformation via a list of tie points
  rather than marking stars on the image display or creating a refpoints
  file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ...
  
  cl&gt; type refpts
      442.0 409.0   380.0  66.0    69.0 460.0
       82.0 347.0   207.0  84.0   371.0 469.0
  
  cl&gt; xyxymatch lpix.coo.1 pix.coo.1 xymatch toler=3     \
      refpoints=refpts matching=tolerance
  
  cl&gt; geomap xymatch geodb 1.0 512.0 1.0 512.0
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
  daophot.daofind,lintran,imlintran,geomap,register,geotran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'ALGORITHMS' 'FORMATS' 'REFERENCES' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

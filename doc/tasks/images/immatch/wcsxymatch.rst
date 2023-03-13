.. _wcsxymatch:

wcsxymatch: Generate matched pixel lists using the image wcs
============================================================

**Package: immatch**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  wcsxymatch input reference output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input images containing the input wcs.
  </dd>
  </dl>
  <dl id="l_reference">
  <dt><b>reference</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reference' Line='reference' -->
  <dd>The list of reference images containing the reference wcs. The number of
  reference images must be one or equal to the number of input images.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output matched coordinate lists containing:
  1) the logical x-y pixel coordinates of a point
  in the reference image in columns 1 and 2, 2) the logical x-y pixel
  coordinates of the same point in the input image in columns 3 and 4,
  3) the world coordinates of the point in the reference and input
  image in columns 5 and 6. The output coordinate list can be
  input directly to the geomap task. The number of output files must be 
  equal to the number of input images or be the standard output STDOUT.
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords = <span style="font-family: monospace;">"grid"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords = "grid"' -->
  <dd>The source of the coordinate list. The options are:
  <dl>
  <dt><b>grid    </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='grid' Line='grid    ' -->
  <dd>Generate a list of <i>nx * ny</i> coordinates, evenly spaced over
  the reference image, and beginning and ending at logical coordinates
  <i>xmin</i> and <i>xmax</i> in x and <i>ymin</i> and <i>ymax</i> in y.
  </dd>
  </dl>
  <dl>
  <dt><b>&lt;filename&gt;</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='&lt;filename&gt;' -->
  <dd>The name of the text file containing the world coordinates of a set of
  points in the reference image.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_xmin">
  <dt><b>xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmin' Line='xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF' -->
  <dd>The minimum and maximum logical x and logical y coordinates used to generate
  the grid of control points if <i>coords</i> = <span style="font-family: monospace;">"grid"</span>. Xmin, xmax, ymin, and
  ymax default to 1, the number of columns in the reference image, 1, and the
  number of lines in the reference image, respectively.
  </dd>
  </dl>
  <dl id="l_nx">
  <dt><b>nx = 10, ny = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nx' Line='nx = 10, ny = 10' -->
  <dd>The number of points in x and y used to generate the coordinate grid
  if <i>coords</i> = <span style="font-family: monospace;">"grid"</span>.
  </dd>
  </dl>
  <dl id="l_wcs">
  <dt><b>wcs = <span style="font-family: monospace;">"world"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcs' Line='wcs = "world"' -->
  <dd>The world coordinate system of the coordinates.  The options are:
  <dl>
  <dt><b>physical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='physical' Line='physical' -->
  <dd>Physical coordinates are pixel coordinates which are invariant with
  respect to linear transformations of the physical image data.  For example,
  if the reference 
  image is a rotated section of a larger input image, the physical
  coordinates of an object in the reference image are equal to the physical
  coordinates of the same object in the input image, although the logical
  pixel coordinates are different.
  </dd>
  </dl>
  <dl>
  <dt><b>world</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='world' Line='world' -->
  <dd>World coordinates are image coordinates which are invariant with
  respect to linear transformations of the physical image data and which
  are in world units, normally decimal degrees for sky projection coordinate
  systems and angstroms for spectral coordinate systems. Obviously if the
  wcs is correct the ra and dec or wavelength and position of an object
  should remain the same not matter how the image
  is linearly transformed. The default world coordinate
  system is either 1) the value of the environment variable <span style="font-family: monospace;">"defwcs"</span> if
  set in the user's IRAF environment (normally it is undefined) and present
  in the image header, 2) the value of the <span style="font-family: monospace;">"system"</span>
  attribute in the image header keyword WAT0_001 if present in the
  image header or, 3) the <span style="font-family: monospace;">"physical"</span> coordinate system.
  Care must be taken that the wcs of the input and
  reference images are compatible, e.g. it makes no sense to
  match the coordinates of a 2D sky projection and a 2D spectral wcs.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_transpose">
  <dt><b>transpose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='transpose' Line='transpose = no' -->
  <dd>Force a transpose of the reference image world coordinates before evaluating
  the world to logical coordinate transformation for the input image ? This
  option is useful if there is not enough information in the reference and
  input image headers to tell whether or not the images are transposed with
  respect to each other.
  </dd>
  </dl>
  <dl id="l_xcolumn">
  <dt><b>xcolumn = 1, ycolumn = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcolumn' Line='xcolumn = 1, ycolumn = 2' -->
  <dd>The columns in the input coordinate list containing the x and y coordinate
  values if <i>coords</i> = &lt;filename&gt;.
  </dd>
  </dl>
  <dl id="l_xunits">
  <dt><b>xunits = <span style="font-family: monospace;">""</span>, ls yunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xunits' Line='xunits = "", ls yunits = ""' -->
  <dd>The units of the x and y coordinates in the input coordinate list 
  if <i>coords</i> = &lt;filename&gt;, by default decimal degrees for sky projection 
  coordinate systems, otherwise any units.
  The options are:
  <dl>
  <dt><b>hours</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='hours' Line='hours' -->
  <dd>Input coordinates specified in hours are converted to decimal degrees by
  multiplying by 15.0.
  </dd>
  </dl>
  <dl>
  <dt><b>native</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='native' Line='native' -->
  <dd>The internal units of the wcs. No conversions on the input coordinates
  are performed.
  </dd>
  </dl>
  If the units are not specified the default is <span style="font-family: monospace;">"native"</span>.
  </dd>
  </dl>
  <dl id="l_xformat">
  <dt><b>xformat = <span style="font-family: monospace;">"%10.3f"</span>, yformat = <span style="font-family: monospace;">"%10.3f"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xformat' Line='xformat = "%10.3f", yformat = "%10.3f"' -->
  <dd>The format of the output logical x and y reference and input pixel
  coordinates in columns 1 and 2 and 3 and 4 respectively. By default the
  coordinates are output right justified in a field of ten spaces with
  3 digits following the decimal point. 
  </dd>
  </dl>
  <dl id="l_wxformat">
  <dt><b>wxformat = <span style="font-family: monospace;">""</span>, wyformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wxformat' Line='wxformat = "", wyformat = ""' -->
  <dd>The format of the output world x and y reference and input image coordinates
  in columns 5 and 6 respectively. The internal default formats will give
  reasonable output formats and precision for both sky projection coordinates
  and other types, e.g. spectral coordinates.
  </dd>
  </dl>
  <dl id="l_min_sigdigits">
  <dt><b>min_sigdigits = 7</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='min_sigdigits' Line='min_sigdigits = 7' -->
  <dd>The minimum precision of the output coordinates if, the formatting parameters
  are undefined, or the output world coordinate system is <span style="font-family: monospace;">"world"</span> and the wcs
  format attribute is undefined.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about the progress of the task.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  WCSXYMATCH matches the logical x and y pixel coordinates of a set of points 
  in the input image <i>input</i> with the logical x and y pixels coordinates
  of the same points in the reference image <i>reference</i>
  using world coordinate information
  in the respective image headers, and writes the results to a coordinate file
  <i>output</i>  suitable for input to the GEOMAP task.
  The input and reference images may be 1D or 2D but must both have
  the same dimensionality.
  </p>
  <p>
  If <i>coords</i> = <span style="font-family: monospace;">"grid"</span>, WCSXYMATCH computes a grid of <i>nx * ny</i> 
  logical x and y pixel coordinates evenly distributed over the 
  logical pixel space of the reference image as defined by the
  <i>xmin</i>, <i>xmax</i>, <i>ymin</i>, <i>ymax</i> parameters.
  The logical x and y pixel reference image coordinates are transformed to the
  world coordinate system defined by <i>wcs</i> using
  world coordinate information stored in the reference image header.
  The world coordinates are then transformed back to the logical x and y pixel
  input image coordinates, using world coordinate system information stored in
  the input image header. 
  </p>
  <p>
  If <i>coords</i> is a file name, WCSXYMATCH reads a list of x and y 
  reference image world coordinates from columns <i>xcolumn</i> and <i>ycolumn</i>
  in the input coordinates file,  and transforms these coordinates to
  <span style="font-family: monospace;">"native"</span> coordinate units using the <i>xunits</i> and <i>yunits</i> parameters.
  The reference image world coordinates are
  transformed to logical reference and input image coordinates
  using the value of the <i>wcs</i> parameter and world coordinate
  information in the reference and input image headers.
  </p>
  <p>
  WCSXYMATCH will terminate with an error if the reference and input images
  are not both either 1D or 2D.
  If the world coordinate system information cannot be read from either
  the reference or input image header, the requested transformations
  from the world &lt;-&gt; logical coordinate systems cannot be compiled for either
  or both images, or the world coordinate systems of the reference and input
  images are fundamentally incompatible in some way, the output logical
  reference and input image coordinates are both set to a grid of points
  spanning the logical pixel space of the input, not the reference image,
  and defining an identify transformation, is written to the output file.
  </p>
  <p>
  The computed reference and input logical coordinates and the
  world coordinates are written to the output file using
  the <i>xformat</i> and <i>yformat</i>, and the <i>wxformat</i> and <i>wxformat</i>
  parameters respectively. If these formats are undefined and, in the
  case of the world coordinates, a format attribute cannot be
  read from either the reference or the input images, the coordinates are
  output with the %g format and <i>min_sigdigits</i> of precision.
  </p>
  <p>
  If the reference and input images are 1D then the 
  output logical and world y coordinates are
  set to 1.
  </p>
  <p>
  If <i>verbose</i> is <span style="font-family: monospace;">"yes"</span> then a title section is written to the output
  file for each set of computed coordinates, along with messages about
  what if anything went wrong with the computation.
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
  Additional  information  on  IRAF  world  coordinate  systems including
  more detailed descriptions of the <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"physical"</span>, and <span style="font-family: monospace;">"world"</span>
  coordinate systems can be
  found  in  the  help  pages  for  the  WCSEDIT  and  WCRESET  tasks. 
  Detailed   documentation   for  the  IRAF  world  coordinate  system 
  interface MWCS can be found in  the  file  <span style="font-family: monospace;">"iraf$sys/mwcs/MWCS.hlp"</span>.
  This  file  can  be  formatted  and  printed  with the command <span style="font-family: monospace;">"help
  iraf$sys/mwcs/MWCS.hlp fi+ | lprint"</span>.  Information on the spectral
  coordinates systems and their suitability for use with WCSXYMATCH
  can be obtained by typing <span style="font-family: monospace;">"help specwcs | lprint"</span>.
  Details of  the  FITS  header
  world  coordinate  system  interface  can  be  found in the document
  <span style="font-family: monospace;">"World Coordinate Systems Representations Within  the  FITS  Format"</span>
  by Hanisch and Wells, available from our anonymous ftp archive.
      
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute a matched list of 100 logical x and y coordinates for an X-ray 
  and radio image of the same field, both of which have accurate sky
  projection world coordinate systems. Print the output world coordinates
  in hh:mm:ss.ss and dd:mm:ss.s format
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wcsxymatch image refimage coords wxformat=%12.2H \
      wyformat=%12.1h
  </pre></div>
  <p>
  2. Given a list of ras and decs of objects in the reference image,
  compute a list of matched logical x and y coordinates for the two images,
  both of which have a accurate sky projection wcss. The ras and decs are in
  columns 3 and 4 of the input coordinate file and are in hh:mm:ss.ss and
  dd:mm:ss.s format respectively. Print the output world coordinates
  in the same units as the input.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wcsxymatch image refimage coords coords=radecs \
      xcolumn=3 ycolumn=4 xunits=hours wxformat=%12.2H \
      wyformat=%12.1h
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
  tprecess,wcstran,geomap,register,geotran,wcsmap,wregister
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'FORMATS' 'REFERENCES' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

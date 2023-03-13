.. _wcsctran:

wcsctran: Transform coordinates from one iraf image wcs to another
==================================================================

**Package: imcoords**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  wcsctran input output image inwcs outwcs
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input coordinate files. The number of input coordinate
  files must be one or equal to the number of input images. Coordinates
  may be entered by hand by setting input to <span style="font-family: monospace;">"STDIN"</span>.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The list of output coordinate files. The number of coordinate files
  must be one or equal to the number of input images. Results may be printed
  on the terminal by setting output to <span style="font-family: monospace;">"STDOUT"</span>.
  </dd>
  </dl>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The list of input images containing the WCS information.
  </dd>
  </dl>
  <dl id="l_inwcs">
  <dt><b>inwcs, outwcs</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inwcs' Line='inwcs, outwcs' -->
  <dd>The input and output coordinate systems. Coordinates in the input
  file are assumed to be in the input system. Coordinates are written to
  the output file in the output system. The options are:
  <dl>
  <dt><b>logical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='logical' Line='logical' -->
  <dd>Logical coordinates are pixel coordinates relative to the current
  image. The logical coordinate system is the coordinate system used by
  the image input/output routines to access the image data on disk.
  </dd>
  </dl>
  <dl>
  <dt><b>tv    </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='tv' Line='tv    ' -->
  <dd>Tv coordinates are pixel coordinates used by the ximtool and saoimage
  display servers.
  Tv coordinates include the effects of any input image section, but
  do not include the effects of previous linear transformations.
  If the input image name does not include an image section, then tv coordinates
  are identical to logical coordinates. If the input image name does include
  a section, and the input image has not been linearly transformed or 
  copied from a parent image, tv coordinates are identical to physical
  coordinates.
  </dd>
  </dl>
  <dl>
  <dt><b>physical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='physical' Line='physical' -->
  <dd>Physical coordinates are pixel coordinates invariant with respect to linear
  transformations of the physical image data.  For example, if the current
  image was created by extracting a section of another image, the physical
  coordinates of an object in the current image will be equal to the physical
  coordinates of the same object in the parent image, although the logical
  coordinates will be different.
  </dd>
  </dl>
  <dl>
  <dt><b>world</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='world' Line='world' -->
  <dd>World coordinates are image coordinates in any units which are invariant with
  respect to linear transformations of the physical image data. For example, 
  the ra and dec of an object will always be the same no matter how the image
  is linearly transformed. The default world coordinate
  system is either 1) the value of the environment variable <span style="font-family: monospace;">"defwcs"</span> if
  set in the user's IRAF environment (normally it is undefined) and present
  in the image header, 2) the value of the <span style="font-family: monospace;">"system"</span>
  attribute in the image header keyword WAT0_001 if present in the
  image header or, 3) the <span style="font-family: monospace;">"physical"</span> coordinate system.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_columns">
  <dt><b>columns = <span style="font-family: monospace;">"1 2 3 4 5 6 7"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='columns' Line='columns = "1 2 3 4 5 6 7"' -->
  <dd>The list of columns separated by whitespace or commas in the input coordinate
  file containing the coordinate values.
  The number of specified columns must be greater than or equal to the
  dimensionality of the input image. The coordinates are read in the
  order they are specified in the columns parameter.
  </dd>
  </dl>
  <dl id="l_units">
  <dt><b>units = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='units' Line='units = ""' -->
  <dd>The units of the input coordinate values, normally degrees for the sky
  projection coordinate systems and angstroms for spectral coordinate
  systems. 
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
  Units conversions are performed only if the input wcs is <span style="font-family: monospace;">"world"</span>.
  </dd>
  </dl>
  <dl id="l_formats">
  <dt><b>formats = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='formats' Line='formats = ""' -->
  <dd>The format for the computed output coordinates. If the formats
  parameter is undefined then: 1) the value of the wcs format attribute
  is used if the output wcs is <span style="font-family: monospace;">"world"</span> and the attribute is defined, 2)
  %g format is used with the precision set to the maximum of the precision of
  the input coordinates and the value of the min_sigdigits parameter.
  </dd>
  </dl>
  <dl id="l_min_sigdigits">
  <dt><b>min_sigdigits = 7</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='min_sigdigits' Line='min_sigdigits = 7' -->
  <dd>The minimum precision of the output coordinates if, the formats parameter
  is undefined, and the output coordinate system is <span style="font-family: monospace;">"world"</span> but the wcs
  format attribute is undefined.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print comment lines to the output file as the task executes.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  WCSCTRAN transforms a list of coordinates, read from  the input file
  <i>input</i>, from the coordinate system defined by <i>inwcs</i> to the
  coordinate system defined by <i>outwcs</i> using world coordinate system
  information in the input image <i>image</i> header and writes the results
  to the output file <i>output</i>.
  </p>
  <p>
  The input coordinates are read from and written to the
  columns in the input / output file specified by the <i>columns</i> parameter. 
  The units of the input coordinate units are assumed to be the internal
  units of the coordinate system as defined in the image header, normally
  degrees for sky projection coordinate systems and angstroms for
  spectral coordinate systems. For convenience input coordinates in hours
  are accepted and converted to decimal degrees if the <i>units</i> parameter
  is set appropriately.
  </p>
  <p>
  The format of the output units can be set using the
  <i>formats</i> parameter. If the  output formats are unspecified then the
  output coordinates are written using, 1) the value of wcs format attribute if
  outwcs = <span style="font-family: monospace;">"world"</span> and the attribute is defined, or, 2) the %g format and a 
  precision which is the maximum of the precision of the input coordinates
  and the value of the <i>min_sigdigits</i> parameter. All remaining
  fields in the input file are copied to the output file without modification.
  </p>
  <p>
  WCSCTRAN transforms coordinates from one builtin IRAF coordinate system
  to another.  The builtin coordinate systems are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"physical"</span>, and
  <span style="font-family: monospace;">"world"</span>. For convenience WCSCTRAN also supports the <span style="font-family: monospace;">"tv"</span> coordinate system
  which is not a builtin IRAF system, but is used by the display server tasks
  XIMTOOL, SAOIMAGE, and IMTOOL.
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
  In most cases the number of input coordinates is equal to the number of
  output coordinates, and both are equal to the dimensions of the input image.
  In some cases however, the number of output coordinates may be greater or
  less than the number of input coordinates. This situation occurs
  if the input image has been dimensionally-reduced, i.e. is a section
  of a higher-dimensioned parent image, and the input coordinate system
  or the output coordinate system but not both is <span style="font-family: monospace;">"logical"</span> or <span style="font-family: monospace;">"tv"</span>.
  For example, if the input image is a 1D line extracted from a 2D parent
  image with a sky projection world coordinate system, and the user
  specifies a transformation from the <span style="font-family: monospace;">"logical"</span> to <span style="font-family: monospace;">"world"</span> systems, 
  only one input coordinate (column number) is required, but two output
  coordinates (ra and dec) are produced. If the input and output coordinate
  systems are reversed, then two input coordinates (ra and dec) are required,
  but only one output coordinate (column number) is produced. If the number of
  output coordinates is less than the number of input coordinates, the extra
  input coordinate columns in the input file are set to INDEF in the output file.
  If the number of output columns is greater than the number of input columns,
  the extra coordinate columns are added to the end of the output line.
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
  Additional information on IRAF world coordinate systems can be found in
  the help pages for the WCSEDIT and WCRESET tasks.
  Detailed documentation for the IRAF world coordinate system interface MWCS
  can be found in the file <span style="font-family: monospace;">"iraf$sys/mwcs/MWCS.hlp"</span>. This file can be
  formatted and printed with the command <span style="font-family: monospace;">"help iraf$sys/mwcs/MWCS.hlp fi+ |
  lprint"</span>.  Details of the FITS header world coordinate system interface can
  be found in the document <span style="font-family: monospace;">"World Coordinate Systems Representations Within the
  FITS Format"</span> by Hanisch and Wells, available from our anonymous ftp
  archive.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Find the pixel coordinates of a list of objects in an image, given a list
  of their ras and decs in hh:mm:ss.s and dd:mm:ss format. Limit the precision
  of the output coordinates to 3 decimal places. In this example, the input
  ras and decs are assumed to be in columns 1 and 2 of the input coordinate
  file, and the ras must be converted from hours to decimal degrees.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; wcsctran incoords outcoords image world logical units="h n" \
      formats="%8.3f %0.3f"
  </pre></div>
  <p>
  2. Repeat the previous example using the same input coordinate list to
  produce output coordinate lists for a list of input images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; wcsctran incoords @outcoolist @imlist world logical units="h n" \
      formats="%8.3f %8.3f"
  </pre></div>
  <p>
  3. Transform pixel coordinates in a photometry file to ra and dec
  coordinates, writing the output coordinates in hh:mm:ss.ss and dd:mm:ss.s
  format. The input pixel coordinates are stored in columns 3 and 4 of the
  input coordinate file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; wcsctran magfile omagfile image logical world col="3 4" \
      formats="%12.2H %12.1h"
  </pre></div>
  <p>
  4. Given a set of pixel coordinates in the parent image, find the pixel
  coordinates of the same objects in an image which is a shifted, rotated
  and scaled version of the parent image. The input coordinate list
  is created using the displayed parent image and the rimcursor task. 
  The output coordinate lists is marked on the displayed transformed 
  image using the tvmark task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; display parent 1 fi+
  im&gt; rimcursor &gt; coolist
  im&gt; imlintran parent image 45.0 45.0 1.5 1.5 xin=256 yin=256 \
      xout=281 yout=263
  im&gt; wcsctran coolist ocoolist image physical logical
  im&gt; display image 2 fi+
  im&gt; tvmark 2 outcoolist
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
  wcsreset, wcsedit, rimcursor, listpixels, lintran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'FORMATS' 'REFERENCES' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

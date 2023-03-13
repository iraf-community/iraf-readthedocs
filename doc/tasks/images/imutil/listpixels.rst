.. _listpixels:

listpixels: Convert an image section into a list of pixels
==========================================================

**Package: imutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  listpixels images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>Images or list of image sections whose pixels are to be printed.
  </dd>
  </dl>
  <dl id="l_wcs">
  <dt><b>wcs = <span style="font-family: monospace;">"logical"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcs' Line='wcs = "logical"' -->
  <dd>The world coordinate system to be used for coordinate output. The following
  standard systems are defined.
  <dl>
  <dt><b>logical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='logical' Line='logical' -->
  <dd>Logical coordinates are image pixel coordinates relative to the input
  image. For example the pixel coordinates of the lower left corner
  of an image section will always be (1,1) in logical units regardless of
  their values in the original image.
  </dd>
  </dl>
  <dl>
  <dt><b>physical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='physical' Line='physical' -->
  <dd>Physical coordinates are image pixel coordinates with respect to the original
  image. For example the pixel coordinates of the lower left corner
  of an image section will be its coordinates in the original image,
  including the effects of any linear transformations done on that image.
  Physical coordinates are invariant with respect to transformations
  of the physical image matrix.
  </dd>
  </dl>
  <dl>
  <dt><b>world</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='world' Line='world' -->
  <dd>World coordinates are image pixel coordinates with respect to the
  current default world coordinate system. For example in the case
  of spectra world coordinates would most likely be in angstroms.
  The default world coordinate system is the system named by the environment
  variable <i>defwcs</i> if defined in the user environment and present in
  the image world coordinate system description, else it is the first user
  world coordinate system defined for the image, else physical coordinates
  are returned.
  </dd>
  </dl>
  In addition to these three reserved world coordinate system names, the names
  of any user world coordinate system defined for the image may be given.
  </dd>
  </dl>
  <dl id="l_formats">
  <dt><b>formats = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='formats' Line='formats = ""' -->
  <dd>The default output formats for the pixel coordinates, one format
  per axis, with the individual formats separated by whitespace .
  If formats are undefined, listpixels uses the formatting options
  stored with the WCS in the image header. If the WCS formatting options
  are not stored in the image header, then listpixels uses a default
  value.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print a title line for each image whose pixels are to be listed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The pixel coordinates in the world coordinates system specified by
  <i>wcs</i> and using the formats specified by <i>formats</i> are
  printed on the standard output on the standard output followed by
  the pixel value.
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
  1. List the pixels of an image on the standard output.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; listpix m81
  </pre></div>
  <p>
  2. List a subraster of the above image in logical coordinates.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; listpix m81[51:55,151:155]
      1. 1. ...
      2. 1. ...
      3. 1. ...
      4. 1. ...
      5. 1. ...
      1. 2. ...
      .. .. ...
  </pre></div>
  <p>
  3. List the same subraster in physical coordinates.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; listpix m81[51:55,151:155] wcs=physical
      51. 151. ...
      52. 151. ...
      53. 151. ...
      54. 151. ...
      55. 151. ...
      51. 152. ...
      ... .... ...
  </pre></div>
  <p>
  4. List a spectrum that has been dispersion corrected in angstrom units.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; listpix n7027 wcs=world
  </pre></div>
  <p>
  5. List the RA and DEC coordinates in hms and dms format and pixels value
  for an image section where axis 1 is RA and axis 2 is DEC.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; listpix m51 wcs=world formats="%H %h"
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
  imheader, imgets, imhistogram
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'FORMATS' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _starfind:

starfind: Automatically detect stellar objects in a list of images
==================================================================

**Package: imcoords**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  starfind image output hwhmpsf threshold
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The list of input images. The input images must be two-dimensional.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The list of output object files. The number of output files must equal the
  number of input images. If output is <span style="font-family: monospace;">"default"</span>, or <span style="font-family: monospace;">"dir$default"</span>, or a
  directory specification then a default name of the form
  dir$root.extension.version is constructed, where dir$ is the directory name,
  root is the root image name, extension is <span style="font-family: monospace;">"obj"</span>, and version is the next
  available version number.
  </dd>
  </dl>
  <dl id="l_hwhmpsf">
  <dt><b>hwhmpsf</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hwhmpsf' Line='hwhmpsf' -->
  <dd>The half-width half-maximum of the image PSF in pixels.
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold' -->
  <dd>The detection threshold above local background in ADU.
  </dd>
  </dl>
  <dl id="l_datamin">
  <dt><b>datamin = INDEF, datamax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datamin' Line='datamin = INDEF, datamax = INDEF' -->
  <dd>The minimum and maximum good data values in ADU. Datamin and datamax
  default to the constants -MAX_REAL and MAX_REAL respectively.
  </dd>
  </dl>
  <dl id="l_fradius">
  <dt><b>fradius = 2.5 (hwhmpsf)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fradius' Line='fradius = 2.5 (hwhmpsf)' -->
  <dd>The fitting radius in units of hwhmpsf. Fradius defines the size
  of the Gaussian kernel used to compute the density enhancement image, and
  the size of the image region used to do the moment analysis.
  </dd>
  </dl>
  <dl id="l_sepmin">
  <dt><b>sepmin = 5.0 (hwhmpsf)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sepmin' Line='sepmin = 5.0 (hwhmpsf)' -->
  <dd>The minimum separation for detected objects in units of hwhmpsf.
  </dd>
  </dl>
  <dl id="l_npixmin">
  <dt><b>npixmin = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='npixmin' Line='npixmin = 5' -->
  <dd>The minimum area of the detected objects in pixels.
  </dd>
  </dl>
  <dl id="l_maglo">
  <dt><b>maglo = INDEF, maghi = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maglo' Line='maglo = INDEF, maghi = INDEF' -->
  <dd>The minimum and maximum magnitudes of the detected objects. Maglo and maghi
  default to the constants -MAX_REAL and MAX_REAL respectively.
  </dd>
  </dl>
  <dl id="l_roundlo">
  <dt><b>roundlo = 0.0,  roundhi = 0.2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='roundlo' Line='roundlo = 0.0,  roundhi = 0.2' -->
  <dd>The minimum and maximum ellipticity values of the detected objects, where
  ellipticity is defined as 1 - b / a, and a and b are the semi-major and
  semi-minor axis lengths respectively.
  </dd>
  </dl>
  <dl id="l_sharplo">
  <dt><b>sharplo = 0.5, sharphi = 2.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sharplo' Line='sharplo = 0.5, sharphi = 2.0' -->
  <dd>The minimum and maximum sharpness values of the detected objects, where
  sharpness is defined to be the ratio of the object size to the
  hwhmpsf parameter value.
  </dd>
  </dl>
  <dl id="l_wcs">
  <dt><b>wcs = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcs' Line='wcs = ""' -->
  <dd>The world coordinate system.  The options are:
  <dl>
  <dt><b><span style="font-family: monospace;">"     "</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"     "' -->
  <dd>The world coordinate system is undefined. Only logical (pixel) coordinates
  are printed.
  </dd>
  </dl>
  <dl>
  <dt><b>logical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='logical' Line='logical' -->
  <dd>The world coordinate system is the same as the logical (pixel) coordinate
  system,  but two sets of identical logical (pixel) coordinates are printed.
  </dd>
  </dl>
  <dl>
  <dt><b>physical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='physical' Line='physical' -->
  <dd>The world coordinate system is the same as the logical (pixel) coordinate
  system of the parent image if any.
  </dd>
  </dl>
  <dl>
  <dt><b>world</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='world' Line='world' -->
  <dd>The world coordinate system of the image if any.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_wxformat">
  <dt><b>wxformat = <span style="font-family: monospace;">""</span>, wyformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wxformat' Line='wxformat = "", wyformat = ""' -->
  <dd>The output format for the x and y axis world coordinates. If wxformat and
  wyformat are undefined then: 1) the value of the wcs format attribute is
  used if the output wcs is <span style="font-family: monospace;">"world"</span> and the attribute is defined, 2) <span style="font-family: monospace;">"%9.3f"</span>
  is used if the output wcs is <span style="font-family: monospace;">"logical"</span> or <span style="font-family: monospace;">"physical"</span>, and <span style="font-family: monospace;">"%11.8g"</span> is used
  if the output wcs is <span style="font-family: monospace;">"world"</span>. If the input image is a sky projection image and
  the x and y axes are ra and dec respectively, then the formats <span style="font-family: monospace;">"%12.2H"</span> and
  <span style="font-family: monospace;">"%12.1h"</span> will print the world coordinates in hours and degrees respectively.
  </dd>
  </dl>
  <dl id="l_boundary">
  <dt><b>boundary = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary' Line='boundary = "nearest"' -->
  <dd>The boundary extension type. The choices are:
  <dl>
  <dt><b>nearest</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nearest' Line='nearest' -->
  <dd>Use the value of the nearest boundary pixel.
  </dd>
  </dl>
  <dl>
  <dt><b>constant</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='constant' Line='constant' -->
  <dd>Use a constant value.
  </dd>
  </dl>
  <dl>
  <dt><b>reflect</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='reflect' Line='reflect' -->
  <dd>Generate a value by reflecting around the boundary.
  </dd>
  </dl>
  <dl>
  <dt><b>wrap</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='wrap' Line='wrap' -->
  <dd>Generate a value by wrapping around to the other side of the image.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_constant">
  <dt><b>constant = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constant' Line='constant = 0.0' -->
  <dd>The constant for constant boundary extension.
  </dd>
  </dl>
  <dl id="l_nxblock">
  <dt><b>nxblock = INDEF, nyblock = 256</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxblock' Line='nxblock = INDEF, nyblock = 256' -->
  <dd>The working block size. If undefined nxblock and nyblock default
  to the number of columns and rows in the input image respectively.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print messages about the progress of the task ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  STARFIND searches the input images <i>image</i> for local density maxima
  with half-widths at half-maxima of ~ <i>hwhmpsf</i> and peak amplitudes
  greater than ~ <i>threshold</i> above the local background, and writes
  the list of detected objects to <i>output</i>.
  </p>
  <p>
  STARFIND is a modified version of the DAOPHOT package DAOFIND algorithm.
  However STARFIND is intended for use with the IMAGES package image matching
  and image coordinates tasks and is therefore configured somewhat differently
  than the version used in the photometry packages.
  </p>
  </section>
  <section id="s_algorithms">
  <h3>Algorithms</h3>
  <p>
  STARFIND assumes that the point spread function can be approximated by a radial
  Gaussian function whose sigma is 0.84932 * <i>hwhmpsf</i> pixels. STARFIND uses
  this model to construct a convolution kernel which is truncated at
  max (2.0, <i>fradius * hwhmpsf</i>) pixels and normalized to zero power.
  </p>
  <p>
  For each point in the image density enhancement values are computed by
  convolving the input image with the radial Gaussian function. This operation
  is mathematically equivalent to fitting the image data at each point, in the
  least-squares sense, with a truncated, lowered, radial Gaussian function.
  After the convolution each density enhancement value is an estimate of
  the amplitude of the best fitting radial Gaussian function at that point.
  If <i>datamin</i> and <i>datamax</i> are defined then bad data is ignored,
  i.e. rejected from the fit, during the computation of the density enhancement
  values. Out of bounds image pixels are evaluated using the boundary extension
  algorithm parameters <i>boundary</i> and <i>constant</i>. Out of
  bounds density enhancement values are set to zero.
  </p>
  <p>
  After the convolution, STARFIND steps through the density enhancement
  image searching for density enhancements greater then <i>threshold</i>
  and brighter than any density enhancements within a radius of
  <i>sepmin * hwhmpsf</i> pixels. For each potential detection the
  local background is estimated and used, along with the values of
  <i>datamin</i> and <i>datamax</i>, to estimate the position (Xc and Yc),
  size (Area and Hwhm), shape (E and Sharp), orientation (Pa), and
  brightness (Mag) of each object using the second order moments analysis
  shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
     I0 = sum (I)
      N = sum (1.0)
      if (N &lt;= 0)
          Sky = maxdata - maxden
      else
          Sky = I0 / N
  
     M0 = sum (I - Sky)
     Mx = sum (X * (I - Sky))
     My = sum (Y * (I - Sky))
  
     Xc = Mx / M0
     Xc = My / M0
    Mag = -2.5 * log10 (M0)
   Area = N
  
    Mxx = sum ((X - Xc) * (X - Xc) * (I - Sky))
    Mxy = sum ((X - Xc) * (Y - Yc) * (I - Sky))
    Myy = sum ((Y - Yc) * (Y - Yc) * (I - Sky))
  
   Hwhm = sqrt (log (2) * (Mxx + Myy))
      E = sqrt ((Mxx - Myy) ** 2 + 4 * Mxy ** 2) / (Mxx + Myy))
     Pa = 0.5 * atan (2 * Mxy / (Mxx - Myy))
  Sharp = Hmhw / Hwhmpsf
  </pre></div>
  <p>
  The sums are computed using pixels which lie within <i>fradius * hwhmpsf</i> of
  the maximum density enhancement, and whose values are within the good data
  limits defined by <i>datamin</i> and <i>datamax</i>, and which are above the local
  background estimate (Sky).
  </p>
  <p>
  Objects whose magnitude, roundness, and sharpness characteristics are outside
  the values defined by <i>maglo</i>, <i>maghi</i>, <i>roundlo</i>, <i>roundhi</i>,
  <i>sharplo</i>, and <i>sharphi</i> and whose total areas is less than
  <i>npixmin</i> pixels are rejected from the list.
  </p>
  <p>
  If <i>wcs</i> parameter is defined, the world coordinates as well as
  the pixel coordinates of the detected objects are computed and printed
  using the formats defined by <i>wxformat</i> and <i>wyformat</i>.
  </p>
  <p>
  To minimize the memory requirements and increase efficiency, STARFIND
  is configured to operate on data blocks that are <i>nxblock * nyblock</i>
  in size. To keep the image i/o operation to a minimum nxblock is set
  to INDEF and defaults to the number of columns in the input image.
  Setting both parameter to INDEF will force STARFIND to perform the
  whole operation in memory.
  </p>
  </section>
  <section id="s_formats">
  <h3>Formats</h3>
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
   absent, 0      use as much space as needed (D field sets precision)
  
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
  1. Find stellar objects with peak values greater than 100 counts above
  local background in the test image dev$wpix whose fwhm is ~2.5 pixels.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; starfind dev$wpix default 1.25 100.
  cl&gt; display dev$wpix 1 fi+
  cl&gt; tvmark 1 wpix.obj.1 col=204
  </pre></div>
  <p>
  2. Repeat the previous example but tell starfind to compute and print
  world coordinates in hours and degrees as well as pixel coordinates.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; starfind dev$wpix default 1.25 100. wcs=world wxf="%12.2H"\
      wyf="%12.1h"
  cl&gt; display dev$wpix 1 fi+
  cl&gt; tvmark 1 wpix.obj.1 col=204
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  Starfind requires approximately 8 CPU seconds to search a 512 by  512
  image  using  a   7 by 7 pixel convolution kernel (SPARCStation2).
  		
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcentroid, apphot.daofind, daophot.daofind
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'ALGORITHMS' 'FORMATS' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

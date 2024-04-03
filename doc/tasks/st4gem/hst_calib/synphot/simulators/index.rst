simulators: Synthetic photometry simulation package.
====================================================

.. toctree:: :maxdepth: 1

   simbackgd
   simimg
   simnoise
   simspec
.. raw:: html

  <p>
  The tasks in the simulators package simulate the instruments aboard
  the HST. The tasks have been written so that as much information about
  the instruments as possible is stored in data files. This help file
  describe the format of these files.
  </p>
  <dl id="l_Input">
  <dt><b>Input Table of Objects</b></dt>
  <!-- Sec=None Level=0 Label='Input' Line='Input Table of Objects' -->
  <dd>The input table describes the objects to be viewed, and contains one 
  row for each object. There are five fields for each object. The fields
  specify the right ascension, declination, magnitude, spectrum, and
  shape.  The right ascension and declination determine the position
  of the object on the image. Objects are rotated into the coordinate
  frame of the detector, which is specified by the three task 
  parameters: <span style="font-family: monospace;">"det_ra"</span>, <span style="font-family: monospace;">"det_dec"</span>, and <span style="font-family: monospace;">"det_ang"</span>. Any object whose center
  does not lie within the detector is excluded from the output. If no
  objects lie within the detector, the task exits with an error
  message. The magnitude is used to scale the integrated flux of the
  object. The magnitude passband and form are specified by the hidden
  task parameters <span style="font-family: monospace;">"magband"</span> and <span style="font-family: monospace;">"magform"</span>. The spectrum is an expression
  evaluated by the synphot expression evaluator.  (The syntax for a
  synphot expression is described in the help file for `calcspec' and in 
  the Synphot User's Guide.) The spectrum is used to compute the object 
  flux as a function of wavelength. The flux is renormalized to the 
  object magnitude over the magnitude passband. The object shape 
  specifies the shape and extent of non-point source objects. 
  The input table can either be an ST4GEM binary table or a text table. 
  If a binary table, the five columns containing the object description 
  are named by the task parameter <span style="font-family: monospace;">"colnames"</span>.  (The defaults are meant 
  to be self describing.)  If the input table is a text table, the first 
  five columns are the right ascension, declination, magnitude, spectrum, 
  and shape, respectively.  Text table entries (fields) cannot contain 
  embedded spaces unless the fields are enclosed in quotes. The spectrum 
  and shape columns are optional in the input table: in a binary table 
  they would just be left blank, but in a text table they can be either 
  omitted or set to a pair of adjacent quote marks. If the <span style="font-family: monospace;">"spectrum"</span> 
  field for any object is omitted, the spectrum specified by the task 
  parameter <span style="font-family: monospace;">"spectrum"</span> is used in its place. If the shape field is 
  omitted the object is assumed to be a point source, i.e., a star. 
  If the input table is a text table, any extended objects (i.e., objects 
  with a <span style="font-family: monospace;">"shape"</span> field) must be placed first in the table, so that the 
  table library knows the maximum number of columns in the table. 
  Units for the right ascension and declination are read from the column 
  units if the input table is an ST4GEM table. If it is a text table, the 
  units for right ascension are assumed to be hours, and that for 
  declination are assumed to be degrees. Brightness units are read from
  the parameter <span style="font-family: monospace;">"magform"</span>.
  </dd>
  </dl>
  <dl id="l_Object">
  <dt><b>Object Extent/Shape</b></dt>
  <!-- Sec=None Level=0 Label='Object' Line='Object Extent/Shape' -->
  <dd>The shape specification is very much like a function call--that is, 
  the type of the shape is followed by a parenthesized list of 
  function arguments. Most shapes take three arguments. The first is the 
  radius, which is the radius of a circle (or the semi-major axis of an 
  ellipse) containing half the flux of the object. The radius is measured 
  in arcseconds. The second argument is the axial ratio, the ratio 
  between the semimajor and semiminor axes of the ellipse. (Recall that 
  the axial ratio is one for circular objects.) The third argument is the 
  position angle: the angle between the positive (detector) x-axis and
  the semimajor axis. The following is a list of the available shape 
  functions.
  <dl>
  <dt><b>gauss(r,ar,pa)		Gaussian (normal) distribution</b></dt>
  <!-- Sec=None Level=1 Label='gauss' Line='gauss(r,ar,pa)		Gaussian (normal) distribution' -->
  <dd><div class="highlight-default-notranslate"><pre>
  r: radius in seconds
  ar: axial ratio
  pa: position angle
  </pre></div>
  The gaussian distribution is described by the equation
  <div class="highlight-default-notranslate"><pre>
  z = exp (- d ** 2)
  </pre></div>
  where d is the distance from the center of the distribution along the
  major axis
  </dd>
  </dl>
  <dl>
  <dt><b>moffat(r,ar,pa,beta)	Moffat distribution</b></dt>
  <!-- Sec=None Level=1 Label='moffat' Line='moffat(r,ar,pa,beta)	Moffat distribution' -->
  <dd><div class="highlight-default-notranslate"><pre>
  r: radius in seconds
  ar: axial ratio
  pa: position angle
  beta: distribution exponent
  </pre></div>
  The moffat distribution is described by the equation
  <div class="highlight-default-notranslate"><pre>
  z = 1.0 / ((1.0 + d ** 2) ** beta)
  </pre></div>
  </dd>
  </dl>
  <dl>
  <dt><b>exp(r,ar,pa)		Exponential distribution</b></dt>
  <!-- Sec=None Level=1 Label='exp' Line='exp(r,ar,pa)		Exponential distribution' -->
  <dd><div class="highlight-default-notranslate"><pre>
  r: radius in seconds
  ar: axial ratio
  pa: position angle
  </pre></div>
  The exponential distribution is described by the equation
  <div class="highlight-default-notranslate"><pre>
  z = exp (- d)
  </pre></div>
  </dd>
  </dl>
  <dl>
  <dt><b>devauc(r,ar,pa)		Devaucalors distribution</b></dt>
  <!-- Sec=None Level=1 Label='devauc' Line='devauc(r,ar,pa)		Devaucalors distribution' -->
  <dd><div class="highlight-default-notranslate"><pre>
  r: radius in seconds
  ar: axial ratio
  pa: position angle
  </pre></div>
  The Devaucalors distribution is described by the equation
  <div class="highlight-default-notranslate"><pre>
  z = exp (- d  ** 0.25)
  </pre></div>
  </dd>
  </dl>
  <dl>
  <dt><b>prof(tab,r,ar,pa)		Tabulated profile</b></dt>
  <!-- Sec=None Level=1 Label='prof' Line='prof(tab,r,ar,pa)		Tabulated profile' -->
  <dd><div class="highlight-default-notranslate"><pre>
  tab: table name
  r: radius in seconds
  ar: axial ratio
  pa: position angle
  </pre></div>
  The profile an evenly spaced array of points read from a table. The
  first point is the value at the center of the distribution and the last
  point is the value at the specified radius. If the table in a binary
  table, the profile is read from column PROFILE; if it is a text table,
  the profile is read from the first column.
  </dd>
  </dl>
  <dl>
  <dt><b>img(im,r)			Image template</b></dt>
  <!-- Sec=None Level=1 Label='img' Line='img(im,r)			Image template' -->
  <dd><div class="highlight-default-notranslate"><pre>
  im: image name
  r: radius in seconds
  </pre></div>
  An image template is an object shape read from an image. The image
  size is calculated from the world coordinate information (the CD 
  matrix) in the image header and then the image is rescaled so its size 
  is equal to the specified radius.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_Detector">
  <dt><b>Detector Background</b></dt>
  <!-- Sec=None Level=0 Label='Detector' Line='Detector Background' -->
  <dd>The instrument noise is calculated from the NOISE parameter stored in
  the throughput table headers. The NOISE parameter contains an
  expression which is used to compute the mean of a Poisson random
  process. The distribution is sampled and the random noise minus its
  mean is added to each pixel.  If more than one throughput table
  contains a NOISE parameter, the strings will be concatenated with the
  &amp; operator (explained later). The noise expression can contain
  constants and the three variables t, n, and x. These represent the
  exposure time, the number of reads, and the pixel flux. If the noise
  expression is a function of x, the mean of the noise will vary from
  pixel to pixel. Otherwise, the mean will be constant over the
  image. The noise expression may contain the following operators and
  functions:
  <div class="highlight-default-notranslate"><pre>
  +       addition
  -       subtraction or negation
  *       multiplication
  /       division
  **      exponentiation
  &amp;       magnitude (e.g., 3 &amp; 4 = sqrt(3 ** 2 + 4 ** 2) = 5)
  log()   natural logarithm
  sqrt()  square root
  </pre></div>
  Operator precedence and associativity are the same as in Fortran,
  though these can be changed by grouping with parentheses. The
  magnitude operator has lower precedence than any of the other
  operators. 
  The calculated background has contributions due to zodiacal light,
  earthlight, and thermal background. Zodiacal light is a function of
  the relative position of the telescope and sun. The telescope position
  is set by task parameters <span style="font-family: monospace;">"det_ra"</span> and <span style="font-family: monospace;">"det_dec"</span>, the sun position is
  set by task parameter <span style="font-family: monospace;">"time"</span>, which controls the date of the
  observation.  The earthlight background is calculated from task
  parameter <span style="font-family: monospace;">"earthtab"</span>, which specifies the maximum earthlight spectrum,
  and task parameter <span style="font-family: monospace;">"eshine"</span>, which specifies a fraction of the maximum
  eathlight. The thermal background is calculated from <span style="font-family: monospace;">"thermtab"</span>, which
  specifies the spectrum of the thermal background.
  </dd>
  </dl>
  <dl id="l_Aperture">
  <dt><b>Aperture Catalog</b></dt>
  <!-- Sec=None Level=0 Label='Aperture' Line='Aperture Catalog' -->
  <dd>The aperture descriptions are stored in the aperture catalog. The
  catalog has two columns. The first column contains the observation
  mode associated with that aperture. The second column countains a
  string describing the aperture shape. The string is written as a
  function call, that is, the name of the aperture type followed by a
  parenthesized list of numeric arguments. Four types of aperture shapes
  are supported: rectangles, barred rectangles, planetary, and
  multislit. The corresponding function calls are:
  <dl>
  <dt><b>rect(w,l)		Rectangular aperture</b></dt>
  <!-- Sec=None Level=1 Label='rect' Line='rect(w,l)		Rectangular aperture' -->
  <dd><div class="highlight-default-notranslate"><pre>
  w: aperture width
  l: aperture length
  </pre></div>
  The aperture is a simple aperture. The width is the rectangle length
  in the x dimension and the length is the length in the y dimension.
  </dd>
  </dl>
  <dl>
  <dt><b>barred(w,l1,g1,...) Barred aperture</b></dt>
  <!-- Sec=None Level=1 Label='barred' Line='barred(w,l1,g1,...) Barred aperture' -->
  <dd><div class="highlight-default-notranslate"><pre>
  w: aperture width
  l1: length of first part of aperture
  g1: gap between first and second parts of aperture
  </pre></div>
  The lengths and gaps may alternate an arbitrary number of times, but
  must end with a length. The length represents an open area in the
  aperture and the gap an obscured area. The dimensions of the aperture
  parts are listed from left to right.
  </dd>
  </dl>
  <dl>
  <dt><b>planet(w1,l1,w2,l2,w3,l3,ang) Planetary aperture</b></dt>
  <!-- Sec=None Level=1 Label='planet' Line='planet(w1,l1,w2,l2,w3,l3,ang) Planetary aperture' -->
  <dd><div class="highlight-default-notranslate"><pre>
  w1: width of first part of aperture
  l1: length of first part of aperture
  w2: width of second part of aperture
  l2: length of second part of aperture
  w3: width of third part of aperture
  l3: length of third part of aperture
  ang: rotation angle of aperture
  </pre></div>
  The planetary apertures are dumbell shaped, narrower at the middle
  than at the ends. They are also rotated with respect to the dispersion
  axis. The dimensions of the three rectangles making up the dumbell
  shape are specified from the leftmost (unrotated) end, followed by the
  rotation angle. The rotation angle is specified in
  degrees. Counterclockwise rotations from the x axis are positive.
  </dd>
  </dl>
  <dl>
  <dt><b>multi(w,l,y1,x1,...) Multiple aperture</b></dt>
  <!-- Sec=None Level=1 Label='multi' Line='multi(w,l,y1,x1,...) Multiple aperture' -->
  <dd><div class="highlight-default-notranslate"><pre>
  w: width of all apertures
  l: length of all apertures
  y1: y offset to midpoint of first aperture
  x1: x distance between first and second apertures
  </pre></div>
  Multiple apertures are collections of several simple rectangular
  apertures, each which has the same width and length. The location of
  each subaperture is specified by the offset to the midpoint of the
  aperture and distance between successive apertures.
  </dd>
  </dl>
  </dd>
  </dl>
  <!-- Contents:  -->
  

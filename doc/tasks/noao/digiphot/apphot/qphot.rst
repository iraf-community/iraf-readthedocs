.. _qphot:

qphot: Measure quick magnitudes for a list of stars
===================================================

**Package: apphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  qphot image cbox annulus dannulus apertures
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The list of images containing the objects to be measured.
  </dd>
  </dl>
  <dl id="l_cbox">
  <dt><b>cbox</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cbox' Line='cbox' -->
  <dd>The width of the centering box in pixels.
  </dd>
  </dl>
  <dl id="l_annulus">
  <dt><b>annulus</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='annulus' Line='annulus' -->
  <dd>The inner radius of the sky annulus in pixels.
  </dd>
  </dl>
  <dl id="l_dannulus">
  <dt><b>dannulus</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dannulus' Line='dannulus' -->
  <dd>The width of the sky annulus in pixels.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures' -->
  <dd>The list of aperture radii in pixels. Apertures is a string parameter 
  specifying either a single aperture radius e.g. <span style="font-family: monospace;">"3.0"</span>, a list of aperture
  radii separated by commas e.g. <span style="font-family: monospace;">"3.0,5.0,10.0"</span>, or a range of aperture radii
  e.g. <span style="font-family: monospace;">"1.0:20.0:1.0"</span>.
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords = ""' -->
  <dd>The list of text files containing initial coordinates for the objects to
  be measured. Objects are listed in coords one object per line with the
  initial coordinate values in columns one and two. The number of coordinate
  files must be zero, one, or equal to the number of images. If coords is
  <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory specification then a coords file name
  of the form dir$root.extension.version is constructed and searched for,
  where dir is the directory, root is the root image name, extension is <span style="font-family: monospace;">"coo"</span>
  and version is the next available version number for the file.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">"default"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = "default"' -->
  <dd>The name of the results file or results directory. If output is
  <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory specification then an output file name
  of the form dir$root.extension.version is constructed, where dir is the
  directory, root is the root image name, extension is <span style="font-family: monospace;">"mag"</span> and version is
  the next available version number for the file. The number of output files
  must be zero, one, or equal to the number of image files.  In both interactive
  and batch mode full output is written to output. In interactive mode
  an output summary is also written to the standard output.
  </dd>
  </dl>
  <dl id="l_plotfile">
  <dt><b>plotfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotfile' Line='plotfile = ""' -->
  <dd>The name of the file containing radial profile plots of the stars written
  to the output file. If plotfile is defined then a radial profile plot
  is written to plotfile every time a record is written to <i>output</i>.
  The user should be aware that this can be a time consuming operation.
  </dd>
  </dl>
  <dl id="l_zmag">
  <dt><b>zmag = 25.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zmag' Line='zmag = 25.0' -->
  <dd>The zero point of the magnitude scale.
  </dd>
  </dl>
  <dl id="l_exposure">
  <dt><b>exposure = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exposure' Line='exposure = ""' -->
  <dd>The image header keyword containing the exposure time.
  </dd>
  </dl>
  <dl id="l_airmass">
  <dt><b>airmass = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='airmass' Line='airmass = ""' -->
  <dd>The image header keyword containing the airmass of the observation.
  </dd>
  </dl>
  <dl id="l_filter">
  <dt><b>filter = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filter' Line='filter = ""' -->
  <dd>The image header keyword containing the filter id of the observation.
  </dd>
  </dl>
  <dl id="l_obstime">
  <dt><b>obstime = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obstime' Line='obstime = ""' -->
  <dd>The image header keyword containing the time of the observation.
  </dd>
  </dl>
  <dl id="l_epadu">
  <dt><b>epadu = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='epadu' Line='epadu = 1.0' -->
  <dd>The gain in photons per adu. Epadu is used to compute the magnitude errors.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Interactive or batch mode.
  </dd>
  </dl>
  <dl id="l_radplots">
  <dt><b>radplots = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radplots' Line='radplots = no' -->
  <dd>If radplots is <span style="font-family: monospace;">"yes"</span> and QPHOT is run in interactive mode then a radial profile
  of each star is plotted on the screen after it is measured.
  </dd>
  </dl>
  <dl id="l_icommands">
  <dt><b>icommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='icommands' Line='icommands = ""' -->
  <dd>The image display cursor or image cursor command file.
  </dd>
  </dl>
  <dl id="l_gcommands">
  <dt><b>gcommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gcommands' Line='gcommands = ""' -->
  <dd>The graphics cursor or graphics cursor command file.
  </dd>
  </dl>
  <dl id="l_wcsin">
  <dt><b>wcsin = <span style="font-family: monospace;">")_.wcsin"</span>, wcsout = <span style="font-family: monospace;">")_.wcsout"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcsin' Line='wcsin = ")_.wcsin", wcsout = ")_.wcsout"' -->
  <dd>The coordinate system of the input coordinates read from <i>coords</i> and
  of the output coordinates written to <i>output</i> respectively. The image
  header coordinate system is used to transform from the input coordinate
  system to the <span style="font-family: monospace;">"logical"</span> pixel coordinate system used internally,
  and from the internal <span style="font-family: monospace;">"logical"</span> pixel coordinate system to the output
  coordinate system. The input coordinate system options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>,
  <span style="font-family: monospace;">"physical"</span>, and <span style="font-family: monospace;">"world"</span>. The output coordinate system options are <span style="font-family: monospace;">"logical"</span>,
  <span style="font-family: monospace;">"tv"</span>, and <span style="font-family: monospace;">"physical"</span>. The image cursor coordinate system is assumed to
  be the <span style="font-family: monospace;">"tv"</span> system.
  <dl>
  <dt><b>logical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='logical' Line='logical' -->
  <dd>Logical coordinates are pixel coordinates relative to the current image.
  The  logical coordinate system is the coordinate system used by the image
  input/output routines to access the image data on disk. In the logical
  coordinate system the coordinates of the first pixel of a  2D image, e.g.
  dev$ypix  and a 2D image section, e.g. dev$ypix[200:300,200:300] are
  always (1,1).
  </dd>
  </dl>
  <dl>
  <dt><b>tv</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='tv' Line='tv' -->
  <dd>Tv coordinates are the pixel coordinates used by the display servers. Tv
  coordinates  include  the effects of any input image section, but do not
  include the effects of previous linear transformations. If the input
  image name does not include an image section, then tv coordinates are
  identical to logical coordinates.  If the input image name does include a
  section, and the input image has not been linearly transformed or copied from
  a parent image, tv coordinates are identical to physical coordinates.
  In the tv coordinate system the coordinates of the first pixel of a
  2D image, e.g. dev$ypix and a 2D image section, e.g. dev$ypix[200:300,200:300]
  are (1,1) and (200,200) respectively.
  </dd>
  </dl>
  <dl>
  <dt><b>physical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='physical' Line='physical' -->
  <dd>Physical coordinates are pixel coordinates invariant  with respect to linear
  transformations of the physical image data.  For example, if the current image
  was created by extracting a section of another image,  the  physical
  coordinates of an object in the current image will be equal to the physical
  coordinates of the same object in the parent image,  although the logical
  coordinates will be different.  In the physical coordinate system the
  coordinates of the first pixel of a 2D image, e.g. dev$ypix and a 2D
  image section, e.g. dev$ypix[200:300,200:300] are (1,1) and (200,200)
  respectively.
  </dd>
  </dl>
  <dl>
  <dt><b>world</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='world' Line='world' -->
  <dd>World coordinates are image coordinates in any units which are invariant
  with respect to linear transformations of the physical image data. For
  example, the ra and dec of an object will always be the same no matter
  how the image is linearly transformed. The units of input world coordinates
  must be the same as those expected by the image header wcs, e. g.
  degrees and degrees for celestial coordinate systems.
  </dd>
  </dl>
  The wcsin and wcsout parameters default to the values of the package
  parameters of the same name. The default values of the package parameters
  wcsin and wcsout are <span style="font-family: monospace;">"logical"</span> and <span style="font-family: monospace;">"logical"</span> respectively.
  </dd>
  </dl>
  <dl id="l_cache">
  <dt><b>cache = <span style="font-family: monospace;">")_.cache"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cache' Line='cache = ")_.cache"' -->
  <dd>Cache the image pixels in memory. Cache may be set to the value of the apphot
  package parameter (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>. By default cacheing is 
  disabled.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = <span style="font-family: monospace;">")_.verbose"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = ")_.verbose"' -->
  <dd>Print messages in non-interactive mode ? Verbose may be set to the apphot
  package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">")_.graphics"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = ")_.graphics"' -->
  <dd>The default graphics device.  Graphics may be set to the apphot package
  parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_display">
  <dt><b>display = <span style="font-family: monospace;">")_.display"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='display' Line='display = ")_.display"' -->
  <dd>The default display device. Display may be set to the apphot package parameter
  value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>. By default graphics overlay is disabled.
  Setting display to one of <span style="font-family: monospace;">"imdr"</span>, <span style="font-family: monospace;">"imdg"</span>, <span style="font-family: monospace;">"imdb"</span>, or <span style="font-family: monospace;">"imdy"</span> enables graphics
  overlay with the IMD graphics kernel.  Setting display to <span style="font-family: monospace;">"stdgraph"</span> enables
  QPHOT to work interactively from a contour plot.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  QPHOT computes accurate centers, sky values, and magnitudes for a list of
  objects in the IRAF image <i>image</i> whose initial coordinates are
  read from the image cursor or the coordinate file <i>coords</i>,
  and writes the computed x and y coordinates, sky values, and
  magnitudes to the text file <i>output</i>.
  </p>
  <p>
  The coordinates read from <i>coords</i> are assumed to be in coordinate
  system defined by <i>wcsin</i>. The options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, <span style="font-family: monospace;">"physical"</span>,
  and <span style="font-family: monospace;">"world"</span> and the transformation from the input coordinate system to
  the internal <span style="font-family: monospace;">"logical"</span> system is defined by the image coordinate system.
  The simplest default is the <span style="font-family: monospace;">"logical"</span> pixel system. Users working on with
  image sections but importing pixel coordinate lists generated from the parent
  image must use the <span style="font-family: monospace;">"tv"</span> or <span style="font-family: monospace;">"physical"</span> input coordinate systems.
  Users importing coordinate lists in world coordinates, e.g. ra and dec,
  must use the <span style="font-family: monospace;">"world"</span> coordinate system and may need to convert their
  equatorial coordinate units from hours and degrees to degrees and degrees first.
  </p>
  <p>
  The coordinates written to <i>output</i> are in the coordinate
  system defined by <i>wcsout</i>. The options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>,
  and <span style="font-family: monospace;">"physical"</span>. The simplest default is the <span style="font-family: monospace;">"logical"</span> system. Users
  wishing to correlate the output coordinates of objects measured in
  image sections or mosaic pieces with coordinates in the parent
  image must use the <span style="font-family: monospace;">"tv"</span> or <span style="font-family: monospace;">"physical"</span> coordinate systems.
  </p>
  <p>
  In interactive mode the user measure objects interactively with the image
  cursor, or select them interactively from the coordinate list <i>coords</i>.
  In batch mode the coordinates can be read directly from <i>coords</i>, or from 
  the cursor command file specified by the parameter <i>icommands</i>.
  </p>
  <p>
  If <i>cache</i> is yes and the host machine physical memory and working set size
  are large enough, the input image pixels are cached in memory. If cacheing
  is enabled and QPHOT is run interactively the first measurement will appear
  to take a long time as the entire image must be read in before the measurement
  is actually made. All subsequent measurements will be very fast because QPHOT
  is accessing memory not disk. The point of cacheing is to speed up random
  image access by making the internal image i/o buffers the same size as the
  image itself. However if the input object lists are sorted in row order and
  sparse cacheing may actually worsen not improve the execution time. Also at
  present there is no point in enabling cacheing for images that are less than
  or equal to 524288 bytes, i.e. the size of the test image dev$ypix, as the
  default image i/o buffer is exactly that size. However if the size of dev$ypix
  is doubled by converting it to a real image with the chpixtype task then the
  effect of cacheing in interactive is can be quite noticeable if measurements
  of objects in the top and bottom halfs of the image are alternated.
  </p>
  <p>
  QPHOT computes accurate centers for each object using the centroid
  centering algorithm, pixels inside <i>cbox</i> and the default values of the
  <i>centerpars</i> parameters.  Accurate sky values for each object are
  computed using the <i>centroid</i> sky fitting algorithm with histogram
  smoothing turned on, pixels inside the sky annulus defined by <i>annulus</i>
  and <i>dannulus</i>, and the default values of the remaining sky fitting
  parameters as defined in the <i>fitskypars</i> parameter set. Magnitudes
  are computed using pixels inside the apertures defined by <i>apertures</i>.
  The user must set the gain <i>epadu</i> to ensure that the magnitude error
  estimates are correctly computed and <i>exposure</i> to normalize the computed
  magnitudes to an exposure time of 1 time unit. The zero point of the magnitude
  scale can be adjusted by setting <i>zmag</i>. <i>Airmass</i>, <i>filter</i>,
  and <i>obstime</i> are book-keeping parameters. Setting  them to appropriate
  values will simplify future analysis and calibration steps.
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  The following list of cursor commands are currently available.
  </p>
  <div class="highlight-default-notranslate"><pre>
          Interactive Photometry Commands
  
  ?       Print help
  :       Colon commands
  w       Save the current parameters
  d       Plot radial profile of current star
  i       Interactively set parameters using current star
  c       Fit center of current star
  t       Fit sky around the cursor
  a       Average sky values fit around several cursor positions
  s       Fit sky for current centered star
  p       Do photometry for current star, using current sky
  o       Do photometry for current star, using current sky, output results
  f       Do photometry for current star
  spbar   Do photometry for current star, output results
  e       Print error messages
  m       Move to next star in coordinate list
  n       Do photometry for next star in coordinate list, output results
  l       Do photometry for remaining stars in coordinate list, output results
  r       Rewind the coordinate list
  q       Exit task
  
          Colon Commands
  
  :show   List the parameters
  :m [n]  Move to next [nth] star in coordinate list
  :n [n]  Do photometry for next [nth] star in coordinate list, output results
  
          Colon Parameter Editing Commands
  
  :image          [string]        Image name
  :output         [string]        Output file name
  :coords         [string]        Coords file name
  
  :cbox           [value]         Width of the centering box (pixels)
  :annulus        [value]         Inner radius of sky annulus (pixels)
  :dannulus       [value]         Width of sky annulus (pixels)
  :apertures      [string]        List of aperture radii (pixels)
  :zmag           [value]         Zero point of magnitude scale (magnitudes)
  :epadu          [value]         Gain (electrons  per adu)
  
  :exposure       [string]        Exposure time image header keyword
  :airmass        [string]        Airmass image header keyword
  :filter         [string]        Filter image header keyword
  :obstime        [string]        Time of observation image header keyword
  
  :radplot        [y/n]           Plot radial profile of object
  
  The following commands are available from inside the interactive setup menu
  using the i key.
  
                      Interactive Qphot Setup Menu
  
          v       Mark and verify the critical parameters (c,a,d,r)
  
          c       Mark and verify the centering box width
          a       Mark and verify the inner radius of the sky annulus
          d       Mark and verify the width of the sky annulus
          r       Mark and verify the aperture radii
  </pre></div>
  </section>
  <section id="s_output">
  <h3>Output</h3>
  <p>
  In interactive mode the following quantities are printed on the standard
  output as each object is measured. Error is a simple string which indicates
  whether the task encountered an error condition from
  the centering algorithm, the sky fitting algorithm or the photometry
  algorithm respectively. Mag are the magnitudes in
  apertures 1 through N respectively and xcenter, ycenter and msky are the
  x and y centers and the sky value respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  image  xcenter  ycenter  msky  mag[1 ... N]  error
  </pre></div>
  <p>
  In both interactive and batch mode full output is written to the text file
  <i>output</i>. At the beginning of each file is a header listing the
  current values of the parameters when the first stellar record was written.
  These parameters can be subsequently altered. For each star measured the
  following record is written.
  </p>
  <div class="highlight-default-notranslate"><pre>
  image  xinit  yinit  id  coords  lid
     xcenter  ycenter  xshift  yshift  xerr  yerr  cier cerror
     msky  stdev  sskew  nsky  nsrej  sier  serror
     itime  xairmass  ifilter  otime
     rapert  sum  area  flux mag  merr  pier  perror
  </pre></div>
  <p>
  Image and coords are the name of the image and coordinate file respectively.
  Id and lid are the sequence numbers of stars in the output and coordinate
  files respectively. Cier and cerror are the error code and accompanying
  error message for the center computation.  Xinit, yinit, xcenter, ycenter,
  xshift, yshift, and xerr, yerr are self explanatory and output in pixel units.
  The sense of the xshift and yshift definitions is the following.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xshift = xcenter - xinit
  yshift = ycenter - yinit
  </pre></div>
  <p>
  Sier and serror are the sky fitting error code and accompanying error message
  respectively.  Msky, stdev and sskew are the best estimate of the sky value
  (per pixel), standard deviation and skew respectively. Nsky and nsrej are
  the number of sky pixels used and the number of sky pixels rejected
  respectively.
  </p>
  <p>
  Itime is the exposure time, xairmass is self-evident, ifilter is an
  id string used to identify the filter used during the observation, and
  otime is a string containing the time stamp in whatever units the
  user has written into the image header or the otime parameter.
  </p>
  <p>
  Rapert, sum, area, and flux  are the radius of the aperture in pixels, the
  total number of counts including sky in the aperture, the area of the aperture
  in square pixels, and the total number of counts in the aperture excluding
  sky. Mag and merr are the magnitude and error in the magnitude in the aperture.
  </p>
  <div class="highlight-default-notranslate"><pre>
  flux = sum - area * msky
   mag = zmag - 2.5 * log10 (flux) + 2.5 * log10 (itime)
  merr = 1.0857 * err / flux
   err = sqrt (flux / epadu + area * stdev**2 +
         area**2 * stdev**2 / nsky)
  </pre></div>
  <p>
  Pier and perror are photometry error code and accompanying error message.
  </p>
  <p>
  In interactive mode a radial profile of each measured object is plotted
  in the graphics window if <i>radplots</i> is <span style="font-family: monospace;">"yes"</span>.
  </p>
  <p>
  In interactive and batchmode a radial profile plot is written to
  <i>plotfile</i>  if it is defined each time the result of an object
  measurement is written to <i>output</i> .
  </p>
  </section>
  <section id="s_errors">
  <h3>Errors</h3>
  <p>
  If the object centering was error free then the field cier will be zero.
  Non-zero values of cier flag the following error conditions.
  </p>
  <div class="highlight-default-notranslate"><pre>
  0        # No error
  101      # The centering box is off image
  102      # The centering box is partially off the image
  103      # The S/N ratio is low in the centering box
  104      # There are two few points for a good fit
  105      # The x or y center fit is singular
  106      # The x or y center fit did not converge
  107      # The x or y center shift is greater than 1 pixel
  108      # There is bad data in the centering box
  </pre></div>
  <p>
  If all goes well during the sky fitting process then the error code sier
  will be 0. Non-zero values of sier flag the following error conditions.
  </p>
  <div class="highlight-default-notranslate"><pre>
  0         # No error
  201       # There are no sky pixels in the sky annulus
  202       # Sky annulus is partially off the image
  203       # The histogram of sky pixels has no width
  204       # The histogram of sky pixels is flat or concave
  205       # There are too few points for a good sky fit
  206       # The sky fit is singular
  207       # The sky fit did not converge
  208       # The graphics stream is undefined
  209       # The file of sky values does not exist
  210       # The sky file is at EOF
  211       # Cannot read the sky value correctly
  212       # The best fit parameter are non-physical
  </pre></div>
  <p>
  If no error occurs during the measurement of the magnitudes then pier is
  0. Non-zero values of pier flag the following error conditions.
  </p>
  <div class="highlight-default-notranslate"><pre>
  0        # No error
  301      # The aperture is off the image
  302      # The aperture is partially off the image
  303      # The sky value is undefined
  305      # There is bad data in the aperture
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Perform aperture photometry interactively for a few stars in dev$ypix using
  the display and the image cursor.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix 1 fi+
  
  ... display the image
  
  ap&gt; qphot dev$ypix 5. 10. 5. 2.,4.,6.0
  
  ... move image cursor to objects of interest and tap space bar
  
  ... a 1 line summary will be printed on the standard output
      for each object measured
  
  ... type q to quit and q again to confirm the quit
  
  ... full output will appear in ypix.mag.1
  </pre></div>
  <p>
  2. Perform aperture photometry interactively for a few stars in dev$ypix
  using the contour plot and the graphics cursor. This option is only useful
  for those (now very few) users who have access to a graphics terminal but
  not to an image display server. Setup the task parameters using the
  interactive setup menu defined by the i key command as in example 1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; show stdimcur
  
  ... record the default value of stdimcur
  
  ap&gt; set stdimcur = stdgraph
  
  ... define the image cursor to be the graphics cursor
  
  ap&gt; contour dev$ypix
  
  ... make a contour plot of dev$ypix
  
  ap&gt; contour dev$pix &gt;G ypix.plot1
  
  ... store the contour plot of dev$ypix in the file ypix.plot1
  
  ap&gt; qphot dev$ypix 5. 10. 5. 2.,4.,6.0
  
  ... type ? to see the help screen
  
  ... move image cursor to objects of interest and tap space bar
  
  ... a 1 line summary will be printed on the standard output
      for each object measured
  
  ... type q to quit and q again to confirm the quit
  
  ... full output will be written to ypix.mag.2
  
  ap&gt; set stdimcur = &lt;default&gt;
  
  ... reset stdimcur to its previous value
  </pre></div>
  <p>
  3. Setup and run QPHOT interactively on a list of objects temporarily
  overriding the fwhmpsf, sigma, cbox, annulus, dannulus, and apertures
   parameters determined in examples 1 or 2.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; daofind dev$ypix fwhmpsf=2.6 sigma=25.0 verify-
  
  ... make a coordinate list
  
  ... the output will appear in the text file ypix.coo.1
  
  ap&gt; qphot dev$ypix 7.0 12.0 5.0 "3.0,5.0" coords=ypix.coo.1
  
  ... type ? for optional help
  
  ... move the graphics cursor to the stars and tap space bar
  
                          or
  
  ... select stars from the input coordinate list with m / :m #
      and measure with spbar
  
  ... measure stars selected from the input coordinate list
      with n / n #
  
  ... a one line summary of results will appear on the standard output
      for each star measured
  
  ... type q to quit and q again to confirm the quit
  
  ... the output will appear in ypix.mag.3 ...
  </pre></div>
  <p>
  4. Display and measure some stars in an image section and write the output
  coordinates in the coordinate system of the parent image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix[150:450,150:450] 1
  
  ... display the image section
  
  ap&gt; qphot dev$ypix[150:450,150:450] 7.0 12.0 5.0 "3.0,5.0" wcsout=tv
  
  ... move cursor to stars and type spbar
  
  ... type q to quit and q again to confirm quit
  
  ... output will appear in ypix.mag.4
  
  ap&gt; pdump ypix.mag.4 xc,yc yes | tvmark 1 STDIN col=204
  </pre></div>
  <p>
  5. Run QPHOT in batch mode using the coordinate file and the previously
  saved parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; qphot dev$ypix 7. 12.0 5.0 "3.0,5.0" coords=ypix.coo.1 inter-
  
  ... output will appear in ypix.mag.5 ...
  </pre></div>
  <p>
  6. Repeat example 5 but assume that the input coordinate are ra and dec
  in degrees and degrees and submit the task to the background.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix
  
  ap&gt; rimcursor wcs=world &gt; radec.coo
  
  ... move to selected stars and type any key
  
  ... type ^Z to quit
  
  ap&gt; qphot dev$ypix 7.0 12.0 5.0 "3.0,5.0" coords=radec.coo \
      wcsin=world inter- &amp;
  
  ... output will appear in ypix.ctr.6
  
  ap&gt; pdump ypix.mag.6 xc,yc yes | tvmark 1 STDIN col=204
  
  ... mark the stars on the display
  </pre></div>
  <p>
  7. Run QPHOT interactively without using the image display.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; show stdimcur
  
  ... record the default value of stdimcur
  
  ap&gt; set stdimcur = text
  
  ... set the image cursor to the standard input
  
  ap&gt; qphot dev$ypix 7.0 12.0 5.0 "3.0,5.0" coords=ypix.coo.1
  
  ... type ? for optional help
  
  ... type :m 3 to set the initial coordinates to those of the
      third star in the list
  
  ... type "442 409 101 i" to enter the interactive setup menu
  ... enter the maximum radius in pixels for the radial profile or
      accept the default with a CR
  ... type v to enter the default menu
  ... reset cbox, annulus, dannulus, and apertures using the graphics
      cursor and the stellar radial profile plot
  ... typing &lt;CR&gt; after the prompt leaves the parameter at its default
      value
  ... type q to quit the setup menu
  
  ... type r to rewind the coordinate list
  
  ... type l to measure all the stars in the coordinate list
  
  ... a one line summary of the answers will appear on the standard
      output for each star measured
  
  ... type q to quit followed by q to confirm the quit
  
  ... full output will appear in the text file ypix.mag.7
  
  ap&gt; set stdimcur = &lt;default&gt;
  
  ... reset the value of stdimcur
  </pre></div>
  <p>
  8. Use a image cursor command file to drive the qphot task. The cursor command
  file shown below computes the centers, sky values, and magnitudes  for 3 stars
  and quits the task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; type cmdfile
  442 410 101 \040
  349 188 101 \040
  225 131 101 \040
  q
  
  ap&gt; qphot dev$ypix 7.0 12.0 5.0 "3.0,5.0" icommands=cmdfile
  
  ... full output will appear in ypix.mag.8
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  It is the responsibility of the user to make sure that the image displayed
  in the image display is the same as that specified by the image parameter.
  </p>
  <p>
  Commands which draw to the image display are disabled by default.
  To enable graphics overlay on the image display, set the display
  parameter to <span style="font-family: monospace;">"imdr"</span>, <span style="font-family: monospace;">"imdg"</span>, <span style="font-family: monospace;">"imdb"</span>, or <span style="font-family: monospace;">"imdy"</span> to get red, green,
  blue or yellow overlays. It may be necessary to run gflush and to
  redisplay the image to get the overlays position correctly.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  phot,wphot,polyphot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'OUTPUT' 'ERRORS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

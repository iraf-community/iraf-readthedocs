.. _radprof:

radprof: Compute the stellar radial profile of a list of stars
==============================================================

**Package: apphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  radprof image radius step
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The name of the image containing the objects to be measured.
  </dd>
  </dl>
  <dl id="l_radius">
  <dt><b>radius, step</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radius' Line='radius, step' -->
  <dd>The size and resolution of the computed radial profile in scale units which is
  equal to radius * <i>scale</i>  and step * <i>scale</i> in pixels.
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords = ""' -->
  <dd>The list of text files containing initial coordinates for the objects to
  be centered. Objects are listed in coords one object per line with the
  initial coordinate values in columns one and two. The number of coordinate
  files must be zero, one, or equal to the number of images.  If coords is
  <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory specification then a coords file name
  of the form dir$root.extension.version is constructed and searched for,
  where dir is the directory, root is the root image name, extension is <span style="font-family: monospace;">"prf"</span>
  and version is the next available version number for the file.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>The name of the results file or results directory.
  If output is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span> or a directory specification then an
  output file name of the form dir$root.extension.version is constructed, where
  dir is the directory, root is the root image name, extension is <span style="font-family: monospace;">"prf"</span> and
  version is the next available version of the file. If output is undefined,
  then no output file is created. If output is defined, the number of output files
  is either 1 or the same as the number of input images.
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
  <dl id="l_datapars">
  <dt><b>datapars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datapars' Line='datapars = ""' -->
  <dd>The name of the file containing the data dependent parameters. The critical
  parameters <i>fwhmpsf</i> and <i>sigma</i> are located here. If <i>datapars</i>
  is undefined then the default parameter set in uparm directory is used.
  </dd>
  </dl>
  <dl id="l_centerpars">
  <dt><b>centerpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='centerpars' Line='centerpars = ""' -->
  <dd>The name of the file containing the centering parameters. The critical
  parameters <i>calgorithm</i> and <i>cbox</i> are located here.
  If <i>centerpars</i> is undefined then the default parameter set in
  uparm directory is used.
  </dd>
  </dl>
  <dl id="l_fitskypars">
  <dt><b>fitskypars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitskypars' Line='fitskypars = ""' -->
  <dd>The name of the text file containing the sky fitting parameters. The critical
  parameters <i>salgorithm</i>, <i>annulus</i>, and <i>dannulus</i> are located here.
  If <i>fitskypars</i> is undefined then the default parameter set in uparm
  directory is used.
  </dd>
  </dl>
  <dl id="l_photpars">
  <dt><b>photpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='photpars' Line='photpars = ""' -->
  <dd>The name of the file containing the photometry parameters. The critical
  parameter <i>apertures</i> is located here.  If <i>photpars</i> is undefined
  then the default parameter set in uparm directory is used.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 5' -->
  <dd>The number of pieces in the spline fit.
  </dd>
  </dl>
  <dl id="l_nreject">
  <dt><b>nreject = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nreject' Line='nreject = 1' -->
  <dd>The maximum number of rejection cycles.
  </dd>
  </dl>
  <dl id="l_kreject">
  <dt><b>kreject = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='kreject' Line='kreject = 3.0' -->
  <dd>The k-sigma rejection limit for the radial profile fit.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Run the task interactively ?
  </dd>
  </dl>
  <dl id="l_radplots">
  <dt><b>radplots = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radplots' Line='radplots = yes' -->
  <dd>If <i>radplots</i> is <span style="font-family: monospace;">"yes"</span> and RADPROF  is run in interactive mode, a radial
  profile of each star is plotted on the screen after the star is measured.
  </dd>
  </dl>
  <dl id="l_icommands">
  <dt><b>icommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='icommands' Line='icommands = ""' -->
  <dd>The image cursor or image cursor command file.
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
  <dl id="l_verify">
  <dt><b>verify = <span style="font-family: monospace;">")_.verify"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = ")_.verify"' -->
  <dd>Verify the critical parameters in non-interactive mode ? Verify may be set to
  the apphot package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = <span style="font-family: monospace;">")_.update"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = ")_.update"' -->
  <dd>Update the critical parameter in non-interactive mode if verify is yes ?
  Update may be set to the apphot package parameter value (the default), <span style="font-family: monospace;">"yes"</span>,
  or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = <span style="font-family: monospace;">")_.verbose"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = ")_.verbose"' -->
  <dd>Print messages on the screen in non-interactive mode ? Verbose may be set
  to the apphot package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
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
  <dd>The default display device. Display may be set to the apphot package
  parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>. By default graphics overlay
  is disabled.  Setting display to one of <span style="font-family: monospace;">"imdr"</span>, <span style="font-family: monospace;">"imdg"</span>, <span style="font-family: monospace;">"imdb"</span>, or <span style="font-family: monospace;">"imdy"</span>
  enables graphics overlay with the IMD graphics kernel.  Setting display to
  <span style="font-family: monospace;">"stdgraph"</span> enables RADPROF to work interactively from a contour plot.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The radial profiles of objects in the image <i>image</i> are computed
  the object center out to the radius <i>radius * scale</i>, in steps of
  <i>step * scale</i> pixels, and plotted. The initial positions are
  read from the image cursor or the text file <i>coords</i>.
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
  If <i>cache</i> is yes and the host machine physical memory and working set size
  are large enough, the input image pixels are cached in memory. If cacheing
  is enabled and RADPROF is run interactively the first measurement will appear
  to take a long time as the entire image must be read in before the measurement
  is actually made. All subsequent measurements will be very fast because RADPROF
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
  RADPROF can be run either interactively or in batch mode by setting the
  interactive switch to yes. In interactive mode starting x and y coordinates
  can either be read directly from the image cursor or read from the text
  file specified by <i>coords</i>. In interactive mode the results are
  plotted on the terminal. In batch mode the estimated positions
  are read from the text file <i>coords</i> or the image cursor parameter
  <i>icommands</i> is redirected to a text file containing a list of cursor
  commands.
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  The RADPROF cursor commands are listed below.
  </p>
  <div class="highlight-default-notranslate"><pre>
          Interactive Keystroke Commands
  
  ?       Print help
  :       Colon commands
  v       Verify the critical parameters
  w       Store the current parameters
  d       Plot radial profile of current star
  i       Interactively set parameters using current star
  c       Fit center of current star
  t       Fit sky around the cursor position
  a       Average sky values fit around several cursor positions
  s       Fit sky around the current star
  p       Fit star using current sky
  o       Fit star using current sky, output results
  f       Fit current star
  spbar   Fit current star, output results
  m       Move to next star in coordinate list
  n       Fit next star in coordinate list, output results
  l       Fit remaining stars in coordinate list, output results
  r       Rewind the coordinate list
  e       Print error messages
  q       Exit task
  
          Colon Commands
  
  :show   [data/center/sky/fit]   List the parameters
  :m [n]  Move to next [nth] object in coordinate list
  :n [n]  Fit next [nth] object in coordinate list, output results
  
          Colon Parameter Editing Commands
  
  # Image and file name parameters
  
  :image          [string]        Image name
  :coords         [string]        Coordinate file name
  :output         [string]        Output file name
  
  # Data dependent parameters
  
  :scale          [value]         Image scale (units per pixel)
  :fwhmpsf        [value]         Full-width half-maximum of psf (scale units)
  :emission       [y/n]           Emission features (y), absorption (n)
  :sigma          [value]         Standard deviation of sky (counts)
  :datamin        [value]         Minimum good pixel value (counts)
  :datamax        [value]         Maximum good pixel value (counts)
  
  # Noise parameters
  
  :noise          [string]        Noise model (constant|poisson)
  :gain           [string]        Gain image header keyword
  :ccdread        [string]        Readout noise image header keyword
  :epadu          [value]         Gain (electrons per adu)
  :readnoise      [value]         Readout noise (electrons)
  
  # Observing parameters
  
  :exposure       [value]         Exposure time image header keyword
  :airmass        [string]        Airmass image header keyword
  :filter         [string]        Filter image header keyword
  :obstime        [string]        Time of observation image header keyword
  :itime          [value]         Integration time (time units)
  :xairmass       [value]         Airmass value (number)
  :ifilter        [string]        Filter id string
  :otime          [string]        Time of observation (time units)
  
  # Centering algorithm parameters
  
  :calgorithm     [string]        Centering algorithm
  :cbox           [value]         Width of the centering box (scale units)
  :cthreshold     [value]         Centering intensity threshold (sigma)
  :cmaxiter       [value]         Maximum number of iterations
  :maxshift       [value]         Maximum center shift (scale units)
  :minsnratio     [value]         Minimum S/N ratio for centering
  :clean          [y/n]           Clean subraster before centering
  :rclean         [value]         Cleaning radius (scale units)
  :rclip          [value]         Clipping radius (scale units)
  :kclean         [value]         Clean K-sigma rejection limit (sigma)
  
  # Sky fitting algorithm parameters
  
  :salgorithm     [string]        Sky fitting algorithm
  :skyvalue       [value]         User supplied sky value (counts)
  :annulus        [value]         Inner radius of sky annulus (scale units)
  :dannulus       [value]         Width of sky annulus (scale units)
  :khist          [value]         Sky histogram extent (+/- sigma)
  :binsize        [value]         Resolution of sky histogram (sigma)
  :sloclip        [value]         Low-side clipping factor in percent
  :shiclip        [value]         High-side clipping factor in percent
  :smaxiter       [value]         Maximum number of iterations
  :smooth         [y/n]           Lucy smooth the sky histogram
  :snreject       [value]         Maximum number of rejection cycles
  :sloreject      [value]         Low-side pixel rejection limits (sky sigma)
  :shireject      [value]         High-side pixel rejection limits (sky sigma)
  :rgrow          [value]         Region growing radius (scale units)
  
  # Photometry parameters
  
  :apertures      [string]        List of apertures (scale units)
  :zmag           [value]         Zero point of magnitude scale
  
  # Profile fitting parameters
  
  :radius         [value]         Maximum profile radius (scale units)
  :step           [value]         Step size for computed profile (scale units)
  :order          [value]         Number of spline pieces in fit
  :kreject        [value]         K-sigma rejection for fit (fit sigma)
  :nreject        [value]         Maximum number of rejection cycles
  
  # Marking and plotting parameters
  
  :mkcenter       [y/n]           Mark computed centers on display
  :mksky          [y/n]           Mark the sky annuli on the display
  :mkapert        [y/n]           Mark apertures on the display
  :radplot        [y/n]           Plot the radial profile
  
  The following commands are available from inside the interactive setup menu.
  
                      Interactive Radprof Setup Menu
  
          v       Mark and verify the critical parameters (f,c,s,a,d,r,w,x)
  
          f       Mark and verify the psf full-width half-maximum
          s       Mark and verify the standard deviation of the background
          l       Mark and verify the minimum good data value
          u       Mark and verify the maximum good data value
  
          c       Mark and verify the centering box width
          n       Mark and verify the cleaning radius
          p       Mark and verify the clipping radius
  
          a       Mark and verify the inner radius of the sky annulus
          d       Mark and verify the width of the sky annulus
          g       Mark and verify the region growing radius
  
          r       Mark and verify the photometry aperture radii
          w       Mark and verify the radius of the radial profile
          x       Mark and verify the step size of radial profile
  </pre></div>
  </section>
  <section id="s_algorithms">
  <h3>Algorithms</h3>
  <p>
  Prior to computing the radial profile of the star, RADPROF computes the
  center, estimates a sky value, and does aperture photometry on the star
  using the parameters in the DATAPARS, CENTERPARS, FITSKYPARS, and
  PHOTPARS tasks.
  </p>
  <p>
  Next the radial and intensity coordinates of all the pixels inside
  <i>radius * scale</i> are computed using the calculated center and sky
  values and fit to a least squares cubic spline of order <i>order</i> with
  optional bad data rejection.  The fit is interpolated at intervals of
  <i>step_size * scale</i> to derive the output profile and estimate the
  full width at half maximum of the object. The fit noise model parameters
  are defined in DATAPARS.
  </p>
  </section>
  <section id="s_output">
  <h3>Output</h3>
  <p>
  In interactive mode the following quantities are printed on the standard
  output as each object is measured.  Error is a simple string which
  indicates whether an error was encountered in the
  the centering algorithm, the sky fitting algorithm, the photometry
  algorithm or the spline fitting algorithm respectively.
  Mag and merr are the magnitudes and errors in
  aperture N and xcenter, ycenter and msky are the
  x and y centers and the sky value respectively.
  Pfwhm is the fitted full width half maximum of the fitted radial profile.
  </p>
  <div class="highlight-default-notranslate"><pre>
  image  xcenter  ycenter  msky  pfwhm  mag[N]  merr[N] iers
  </pre></div>
  <p>
  In both interactive and batch mode full output is written to the text file
  <i>output</i>. At the beginning of each file is a header listing the
  current values of the parameters when the first stellar record was written.
  These parameters can be subsequently altered. For each star measured the
  following record is written
  </p>
  <div class="highlight-default-notranslate"><pre>
  image  xinit  yinit  id  coords  lid
     xcenter  ycenter  xshift  yshift  xerr  yerr  cier error
     msky  stdev  sskew  nsky  nsrej  sier  serror
     itime  xairmass  ifilter  otime
     rapert  sum  area  flux mag  merr  pier  perr
     pfwhm  inorm  tinorm  rier  rerror
     pradius  intensity  tintensity
  </pre></div>
  <p>
  Image and coords are the name of the image and coordinate file respectively.
  Id and lid are the sequence numbers of stars in the output and coordinate
  files respectively. Cier and cerror are the error code and accompanying
  error message respectively.  Xinit, yinit, xcenter, ycenter, xshift, yshift,
  and xerr, yerr are self explanatory and output in pixel units. The sense of
  the xshift and yshift definitions is the following.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xshift = xcenter - xinit
  yshift = ycenter - yinit
  </pre></div>
  <p>
  Sier and serror are the error code and accompanying error message respectively.
  Msky, stdev and sskew are the best estimate of the sky value (per pixel),
  standard deviation and skew respectively. Nsky and nsrej are the number of
  sky pixels and the number of sky pixels rejected respectively.
  </p>
  <p>
  Itime is the exposure time, xairmass is self-evident, filter is an id
  string specifying the filter used during the observation and otime is
  a string containing the time of observation in whatever units the user
  has defined.
  </p>
  <p>
  Rapert, sum, area and flux are the radius of the aperture in pixels, the total
  number of counts including sky in the aperture, the area of the aperture in
  square pixels, and the total number of counts in the aperture excluding sky.
  Mag and merr are the magnitude and error in the magnitude in the aperture
  (see below).
  </p>
  <div class="highlight-default-notranslate"><pre>
   flux = sum - area * msky
    mag = zmag - 2.5 * log10 (flux) + 2.5 * log10 (itime)
   merr = 1.0857 * error / flux
  error = sqrt (flux / epadu + area * stdev**2 +
          area**2 * stdev**2 / nsky)
  </pre></div>
  <p>
  Pier and perror are photometry error code and accompanying error message.
  </p>
  <p>
  Pfwhm is the full width at half intensity of the fitted profile. Inorm and
  tinorm are the normalization factors for the fitted radial profile and the
  fitted total intensity profile respectively. Rier and rerror are the spline
  fitting error code and accompanying error message. Pradius, intensity
  and tintensity are the computed radii, intensity and total intensity
  values at each radial step.
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
  107      # The x or y center shift is greater than maxshift
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
  <p>
  If no error occurs during the profile fitting then rier is 0.
  Non-zero values of rier flag the following error conditions.
  </p>
  <div class="highlight-default-notranslate"><pre>
  0       # No error
  901     # The profile region is off the image
  902     # The profile region is partially off the image
  903     # There are too few points in the profile
  904     # The fit is singular
  905     # The sky value is undefined
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the radial profiles for a few  stars in dev$ypix using the
  display and the image cursor. Setup the task parameters using the
  interactive setup menu defined by the i key command.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix 1 fi+
  
  ... display the image
  
  ap&gt; radprof dev$ypix 7.0 0.5
  
  ... type ? to print a short help page
  
  ... move the image cursor to a star
  ... type i to enter the interactive setup menu
  ... enter maximum radius in pixels of the radial profile or
      CR to accept the default value
  ... set the fwhmpsf, centering radius, inner and outer sky
      annuli, apertures, sigma, profile radius and step size
      using the graphics cursor and the stellar radial profile
      plot
  ... typing &lt;CR&gt; leaves everything at the default value
  ... type q to quit the setup menu
  
  ... type the v key to verify the parameters
  
  ... type the w key to save the parameters in the parameter files
  
  ... move the image cursor to the star of interest and tap
      the space bar
  
  ... type :order 3 to change the spline order and see if the
       fit improves, if it does type w
  
  ... a radial profile plot will appear on the graphics terminal
  
  ... type q to quit and q to confirm the quit
  
  ... by default radprof does not create an output file
  </pre></div>
  <p>
  2. Compute the radial profiles for a few  stars in dev$ypix using a contour
  plot and the graphics cursor. Setup the task parameters using the interactive
  setup menu defined by the i key command. This option is only useful for
  those users (now very few) who do not have access to an image display server
  but do have access to a graphics terminal. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; show stdimcur
  
  ... determine the default value of stdimcur
  
  ap&gt; set stdimcur = stdgraph
  
  ... define the image cursor to be the graphics cursor
  
  ap&gt; contour dev$ypix
  
  ... make a contour plot of dev$ypix
  
  ap&gt; contour dev$ypix  &gt;G ypix.plot1
  
  ... store the contour plot of dev$ypix in ypix.plot1
  
  ap&gt; radprof dev$ypix 7.0 0.5
  
  ... type ? to print the help page
  
  ... move graphics cursor to a star
  ... type i to enter the interactive setup menu
  ... enter maximum radius in pixels of the radial profile or
      hit CR to accept the default value
  ... set the fwhmpsf, centering radius, inner and outer sky annuli,
      apertures, sigma, profile radius and step size using the
      graphics cursor and the stellar radial profile plot
  ... typing &lt;CR&gt; leaves everything at the default value
  ... type q to quit the setup menu
  
  ... type the v key to verify the parameters
  
  ... type the w key to save the parameters in the parameter files
  
  ... type :.read ypix.plot1 to reload the contour plot
  
  ... move the graphics cursor to the star of interest and tap
      the space bar
  
  ... a radial profile plot will appear on the graphics terminal
  
  ... repeat the above sequence for each additional star
  
  ... type q to quit and q to confirm the quit
  
  ... by default radprof does not create an output file
  </pre></div>
  <p>
  3. Setup and run RADPROF interactively on a list of objects temporarily
  overriding the fwhmpsf, sigma, cbox, annulus, dannulus, apertures,
  radius, and step  parameters determined in examples 1 or 2.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; daofind dev$ypix fwhmpsf=2.6 sigma=25.0 verify-
  
  ... make a coordinate list
  
  ... the output will appear in the text file ypix.coo.1
  
  ap&gt; radprof dev$ypix 7.0 0.5 fwhmpsf=2.6 sigma=5.0 cbox=7.0 \
      annulus=10.0 dannulus=5.0 apertures=5.0 coords=ypix.coo.1
  
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
  
  ... by default radprof does not create an output file
  </pre></div>
  <p>
  4. Display and fit some stars in an image section and write the output
  coordinates in the coordinate system of the parent image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix[150:450,150:450] 1
  
  ... display the image section
  
  ap&gt; radprof dev$ypix[150:450,150:450] 7.0 0.5 output=default \
      wcsout=tv
  
  ... move cursor to stars and type spbar
  
  ... type q to quit and q again to confirm quit
  
  ... output will appear in ypix.prf.1
  
  ap&gt; pdump ypix.prf.1 xc,yc yes | tvmark 1 STDIN col=204
  </pre></div>
  <p>
  5. Run RADPROF in batch mode using the coordinate file and the previously
  saved parameters. Save the text and plot output. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; radprof dev$ypix 7. 0.5 coords=ypix.coo.1 output="default" \
      plotfile=ypix.rplots inter- verify-
  
  ... output will appear in m92.prf.2 and ypix.rplots
  
  ap&gt; gkidir ypix.rplots
  
  ... get a listing of the plots in ypix.rplots
  
  ap&gt; gkiextract ypix.rplots 1-3 | stdplot dev=lw16
  
  ... extract plots 1-3 and plot them on device lw16
  </pre></div>
  <p>
  6. Repeat example 5 but assume that the input coordinates are ra and dec
  in degrees and degrees, turn off verification, and submit the task to to
  the background.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix 1
  
  ap&gt; rimcursor wcs=world &gt; radec.coo
  
  ... move to selected stars and type any key
  
  ... type ^Z to quit
  
  ap&gt; radprof dev$ypix 7.0 0.5 coords=radec.coo output=default \
      plotfile=ypix.rplots2 wcsin=world verify- inter- &amp;
  
  ... output will appear in ypix.prf.3, plots will appear in
      ypix.rplots2
  
  ap&gt; pdump ypix.prf.3 xc,yc yes | tvmark 1 STDIN col=204
  
  ... mark the stars on the display
  </pre></div>
  <p>
  7. Run RADPROF interactively without using the image display.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; show stdimcur
  
  ... record the default value of stdimcur
  
  ap&gt; set stdimcur = text
  
  ... set the image cursor to the standard input
  
  ap&gt; radprof dev$ypix 7.0 0.5 coords=ypix.coo.1
  
  ... type ? for optional help
  
  ... type :m 3 to set the initial coordinates to those of the
      third star in the list
  
  ... type i to enter the interactive setup menu
  ... enter the maximum radius in pixels for the radial profile or
      accept the default with a CR
  ... type v to enter the default menu
  ... set the fwhmpsf, centering radius, inner and outer sky annuli,
      apertures, and sigma using the graphics cursor and the
      stellar radial profile plot
  ... typing &lt;CR&gt; after the prompt leaves the parameter at its default
      value
  ... type q to quit the setup menu
  
  ... type r to rewind the coordinate list
  
  ... type n to measure the next star
  
  ... a one line summary of the answers will appear on the standard
      output for each star measured
  
  ... type q to quit followed by q to confirm the quit
  
  ... by default no output file is written
  
  ap&gt; set stdimcur = &lt;default&gt;
  
  ... reset the value of stdimcur
  </pre></div>
  <p>
  8. Use a image cursor command file to drive the RADPROF task. The cursor
  command file shown below sets the cbox, annulus, dannulus, and apertures
  parameters computes the centers, sky values, magnitudes, and readial profiles
  for 3 stars, updates the parameter files, and quits the task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; type cmdfile
  : cbox 9.0
  : annulus 12.0
  : dannulus 5.0
  : apertures 5.0
  442 410 101 \040
  349 188 101 \040
  225 131 101 \040
  w
  q
  
  ap&gt; radprof dev$ypix 7.0 0.5 icommands=cmdfile  \
      plotfile=ypix.rplots3 verify-
  
  ... by default no output file is written, plots will appear in
      ypix.rplots3
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  It is currently the responsibility of the user to make sure that the
  image displayed in the frame is the same as that specified by the image
  parameter.
  </p>
  <p>
  Commands which draw to the image display are disabled by default.
  To enable graphics overlay on the image display, set the display
  parameter to <span style="font-family: monospace;">"imdr"</span>, <span style="font-family: monospace;">"imdg"</span>, <span style="font-family: monospace;">"imdb"</span>, or <span style="font-family: monospace;">"imdy"</span> to get red, green,
  blue or yellow overlays and set the centerpars mkcenter switch to
  <span style="font-family: monospace;">"yes"</span>, the fitskypars mksky switch to<span style="font-family: monospace;">"yes"</span>, or the photpars mkapert
  witch to <span style="font-family: monospace;">"yes"</span>. It may be necessary to run gflush and to redisplay the image
  to get the overlays position correctly.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  datapars, centerpars, fitskypars, photpars
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'ALGORITHMS' 'OUTPUT' 'ERRORS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

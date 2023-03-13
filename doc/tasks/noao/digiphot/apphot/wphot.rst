.. _wphot:

wphot: Measure magnitudes for a list of stars with weighting
============================================================

**Package: apphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  wphot image
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
  <dl id="l_skyfile">
  <dt><b>skyfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skyfile' Line='skyfile = ""' -->
  <dd>The list of text files containing the sky values, of the measured objects,
  one object per line with x, y, the sky value, sky sigma, sky skew, number of sky
  pixels and number of rejected sky pixels in columns one to seven respectively.
  The number of sky files must be zero, one, or equal to the number of input
  images. A skyfile value is only requested if <i>fitskypars.salgorithm</i> =
  <span style="font-family: monospace;">"file"</span> and if WPHOT is run non-interactively.
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords = ""' -->
  <dd>The list of text files containing initial coordinates for the objects to
  be centered. Objects are listed in coords one object per line with the
  initial coordinate values in columns one and two. The number of coordinate
  files must be zero, one, or equal to the number of images. If coords is
  <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory specification then a coords file name
  of the form dir$root.extension.version is constructed, where dir is the
  directory, root is the root image name, extension is <span style="font-family: monospace;">"coo"</span> and version is
  the next available version number for the file.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">"default"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = "default"' -->
  <dd>The name of the results file or results directory. If output is
  <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory specification then an output file name
  of the form dir$root.extension.version is constructed, where dir is the
  directory, root is the root image name, extension is <span style="font-family: monospace;">"omag"</span> and version is
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
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Run the task interactively ?
  </dd>
  </dl>
  <dl id="l_radplots">
  <dt><b>radplots = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radplots' Line='radplots = no' -->
  <dd>If <i>radplots</i> is <span style="font-family: monospace;">"yes"</span> and PHOT is run in interactive mode, a radial
  profile of each star is plotted on the screen after the star is measured.
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
  <dl id="l_verify">
  <dt><b>verify = <span style="font-family: monospace;">")_.verify"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = ")_.verify"' -->
  <dd>Verify the critical parameters in non-interactive mode.  Verify may be set to
  the apphot package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = <span style="font-family: monospace;">")_.update"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = ")_.update"' -->
  <dd>Update the critical parameters in non-interactive mode if verify is yes.
  Update may be set to the apphot package parameter value (the default), <span style="font-family: monospace;">"yes"</span>,
  or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = <span style="font-family: monospace;">")_.verbose"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = ")_.verbose"' -->
  <dd>Print messages on the terminal about actions taken in non-interactive mode.
  Verbose may be set to the apphot package parameter value (the default), <span style="font-family: monospace;">"yes"</span>,
  or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">")_.graphics"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = ")_.graphics"' -->
  <dd>The default graphics device. Graphics may be set to the apphot package
  parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_display">
  <dt><b>display = <span style="font-family: monospace;">")_.display"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='display' Line='display = ")_.display"' -->
  <dd>The default display device. Graphics may be set to the apphot package
  parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>. By default graphics overlay
  is disabled.  Setting display to one of <span style="font-family: monospace;">"imdr"</span>, <span style="font-family: monospace;">"imdg"</span>, <span style="font-family: monospace;">"imdb"</span>, or <span style="font-family: monospace;">"imdy"</span>
  enables graphics overlay with the IMD graphics kernel.  Setting display to
  <span style="font-family: monospace;">"stdgraph"</span> enables WPHOT to work interactively from a contour plot.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  WPHOT computes accurate centers, sky values, and weighted magnitudes for a
  list of objects in the IRAF image <i>image</i> whose initial coordinates are read
  from the text file <i>coords</i> or image display cursor, and writes the
  computed x and y coordinates, sky values and magnitudes to the text file
  <i>output</i>.
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
  is enabled and WPHOT is run interactively the first measurement will appear
  to take a long time as the entire image must be read in before the measurement
  is actually made. All subsequent measurements will be very fast because WPHOT
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
  In interactive mode the user may either define the list of objects to be
  measured interactively with the image cursor or create an object list prior
  to entering WPHOT.  In either case the user may adjust the centering, sky
  fitting and photometry parameters until a satisfactory fit is achieved and
  only then store the final results in <i>output</i>. In batch
  mode the initial positions are read from the text file <i>coords</i>
  or the image cursor parameter <i>icommands</i> is redirected to a text
  file containing a list of cursor commands.
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
  v       Verify the critical parameters
  w       Store the current parameters
  d       Plot radial profile of current star
  i       Interactively set parameters using current star
  c       Fit center of current star
  t       Fit sky around the cursor
  a       Average sky values fit around several cursor positions
  s       Fit sky around the current star
  p       Do photometry for current star, using current sky
  o       Do photometry for current star, using current sky, output results
  f       Do photometry for current star
  spbar   Do photometry for current star, output results
  m       Move to next star in coordinate list
  n       Do photometry for next star in coordinate list, output results
  l       Do photometry for remaining stars in coordinate list, output results
  r       Rewind the coordinate list
  e       Print error messages
  q       Exit task
  
          Colon Commands
  
  :show   [data/center/sky/fit]   Show parameters
  :m [n]  Move to next [nth] star in the coordinate list
  :n [n]  Do photometry for next [nth] star in coordinate list, output results
  
          Colon Parameter Editing Commands
  
  # Image and file parameters
  
  :image          [string]        Image name
  :coords         [string]        Coordinate file name
  :output         [string]        Output file name
  
  # Data dependent parameters
  
  :scale          [value]         Image scale (units per pixel)
  :fwhmpsf        [value]         Full-width half-maximum of PSF (scale units)
  :emission       [y/n]           Emission features (y), absorption (n)
  :sigma          [value]         Standard deviation of sky (counts)
  :datamin        [value]         Minimum good pixel value (counts)
  :datamax        [value]         Maximum good pixel value (counts)
  
  # Noise parameters
  
  :noise          [string]        Noise model (constant|poisson)
  :gain           [string]        Gain image header keyword
  :ccdread        [string]        Readout noise image header keyword
  :epadu          [value]         Gain (electrons  per adu)
  :readnoise      [value]         Readout noise (electrons)
  
  # Observations parameters
  
  :exposure       [string]        Exposure time image header keyword
  :airmass        [string]        Airmass image header keyword
  :filter         [string]        Filter image header keyword
  :obstime        [string]        Time of observation image header keyword
  :itime          [value]         Integration time (time units)
  :xairmass       [value]         Airmass value (number)
  :ifilter        [string]        Filter id string
  :otime          [string]        Time of observations (time units)
  
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
  :smooth         [y/n]           Lucy smooth the sky histogram
  :sloclip        [value]         Low-side clipping factor in percent
  :shiclip        [value]         High-side clipping factor in percent
  :smaxiter       [value]         Maximum number of iterations
  :snreject       [value]         Maximum number of rejection cycles
  :sloreject      [value]         Low-side pixel rejection limits (sky sigma)
  :shireject      [value]         High-side pixel rejection limits (sky sigma)
  :rgrow          [value]         Region growing radius (scale units)
  
  # Photometry parameters
  
  :weighting      [string]        Weighting function (constant|cone|gauss)
  :apertures      [string]        List of aperture radii (scale units)
  :zmag           [value]         Zero point of magnitude scale
  
  # Plotting and marking parameters
  
  :mkcenter       [y/n]           Mark computed centers on display
  :mksky          [y/n]           Mark the sky annuli on the display
  :mkapert        [y/n]           Mark apertures on the display
  :radplot        [y/n]           Plot radial profile of object
  
  The following commands are available from inside the interactive setup menu.
  
                      Interactive Phot/Wphot Setup Menu
  
          v       Mark and verify the critical parameters (f,s,c,a,d,r)
  
          f       Mark and verify the full-width half-maximum of psf
          s       Mark and verify the standard deviation of the background
          l       Mark and verify the minimum good data value
          u       Mark and verify the maximum good data value
  
          c       Mark and verify the centering box width
          n       Mark and verify the cleaning radius
          p       Mark and verify the clipping radius
  
          a       Mark and verify the inner radius of the sky annulus
          d       Mark and verify the width of the sky annulus
          g       Mark and verify the region growing radius
  
          r       Mark and verify the aperture radii
  </pre></div>
  </section>
  <section id="s_algorithms">
  <h3>Algorithms</h3>
  <p>
  WPHOT computes accurate centers for each object using the centering
  parameters defined in the CENTERPARS task, computes an accurate sky value
  for each object using the sky fitting parameters defined in FITSKYPARS task,
  and computes magnitudes using the photometry parameters defined in the
  PHOTPARS task. The data dependent parameter are defined in the DATAPARS task.
  </p>
  <p>
  Three weighting functions are currently supported: constant, cone and gauss.
  Constant weighting, the default gives identical results to the PHOT task.
  Pixels are weighted by the fraction of their area inside the circular
  aperture. For cone and gauss weighting an additional  triangular or gaussian
  weighting function of full width half maximum equal to <i>fwhmpsf</i> is
  applied to the pixels before aperture summing.
  </p>
  <p>
  This task is currently experimental. Further algorithm work is required.
  </p>
  </section>
  <section id="s_output">
  <h3>Output</h3>
  <p>
  In interactive mode the following quantities are printed on the standard
  output as each object is measured. Error is a simple string which
  indicates whether the task encountered any errors in the
  the centering algorithm, the sky fitting algorithm or the photometry
  algorithm. Mag and merr are the magnitudes and errors in
  apertures 1 through N respectively and xcenter, ycenter and msky are the
  x and y centers and the sky value respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  image  xcenter  ycenter  msky  mag[1 ... N]   error
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
     itime  xairmass  ifilter otime
     rapert  sum  area  flux mag  merr  pier  perr
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
  Itime is the exposure time, xairmass is self-evident, ifilter is an id
  string identifying the filter used during the observation, and otime is
  a string specifying the time of the observation in whatever units the
  user has defined.
  </p>
  <p>
  Rapert, sum, area, and flux are the radius of the aperture in pixels, the total
  number of counts including sky in the aperture, the area of the aperture
  in square pixels, and the total number of counts in the aperture excluding
  sky. Mag and merr are the magnitude and error in the magnitude
  in the aperture (see below).
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
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the magnitudes for a few  stars in dev$ypix using the display
  and the image cursor. Setup the task parameters using the interactive
  setup menu defined by the i key command and a radial profile plot.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix 1 fi+
  
  ... display the image
  
  ap&gt; wphot dev$ypix
  
  ... type ? to print an optional help page
  
  ... move the image cursor to a star
  ... type i to enter the interactive setup menu
  ... enter maximum radius in pixels of the radial profile or hit
      CR to accept the default
  ... set the fwhmpsf, centering radius, inner and outer sky annuli,
      photometry apertures, and sigma using the graphics cursor and the
      stellar radial profile plot
  ... typing &lt;CR&gt; leaves everything at the default value
  ... type q to quit the setup menu
  
  ... type the v key to verify the parameters
  
  ... type the w key to save the parameters in the parameter files
  
  ... move the image cursor to the stars of interest and tap
      the space bar
  
  ... a one line summary of the fitted parameters will appear on the
      standard output for each star measured
  
  ... type q to quit and q again to confirm the quit
  
  ... the output will appear in ypix.omag.1
  </pre></div>
  <p>
  2. Compute the magnitudes for a few stars in dev$ypix using a contour plot
  and the graphics cursor. This option is only useful for those (now very few)
  users who have access to a graphics terminal but not to an image display
  server. Setup the task parameters using the interactive setup menu defined by
  the i key command as in example 1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; show stdimcur
  
  ... record the default value of stdimcur
  
  ap&gt; set stdimcur = stdgraph
  
  ... define the image cursor to be the graphics cursor
  
  ap&gt; contour dev$ypix
  
  ... make a contour plot of dev$ypix
  
  ap&gt; contour dev$ypix &gt;G ypix.plot1
  
  ... store the contour plot of dev$ypix in the file ypix.plot1
  
  ap&gt; wphot dev$ypix display=stdgraph
  
  ... type ? to get an optional help page
  
  ... move graphics cursor to a star
  ... type i to enter the interactive setup menu
  ... enter maximum radius in pixels of the radial profile or CR
      to accept the default value
  ... set the fwhmpsf, centering radius, inner and outer sky annuli,
      apertures, and sigma using the graphics cursor and the
      stellar radial profile plot
  ... typing &lt;CR&gt; leaves everything at the default value
  ... type q to quit the setup menu
  
  ... type the v key to verify the critical parameters
  
  ... type the w key to save the parameters in the parameter files
  
  ... retype :.read ypix.plot1 to reload the contour plot
  
  ... move the graphics cursor to the stars of interest and tap
      the space bar
  
  ... a one line summary of the fitted parameters will appear on the
      standard output for each star measured
  
  ... type q to quit and q again to verify
  
  ... full output will appear in the text file ypix.omag.2
  
  ap&gt; set stdimcur = &lt;default&gt;
  
  ... reset stdimcur to its previous value
  </pre></div>
  <p>
  3. Setup and run PHOT interactively on a list of objects temporarily
  overriding the fwhmpsf, sigma, cbox, annulus, dannulus, and apertures
  parameters determined in examples 1 or 2.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; daofind dev$ypix fwhmpsf=2.6 sigma=25.0 verify-
  
  ... make a coordinate list
  
  ... the output will appear in the text file ypix.coo.1
  
  ap&gt; wphot dev$ypix cbox=7.0 annulus=12.0 dannulus=5.0 \
     apertures="3.0,5.0" coords=ypix.coo.1
  
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
  
  ... the output will appear in ypix.omag.3 ...
  </pre></div>
  <p>
  4. Display and measure some stars in an image section and write the output
  coordinates in the coordinate system of the parent image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix[150:450,150:450] 1
  
  ... display the image section
  
  ap&gt; wphot dev$ypix[150:450,150:450] wcsout=tv
  
  ... move cursor to stars and type spbar
  
  ... type q to quit and q again to confirm quit
  
  ... output will appear in ypix.omag.4
  
  ap&gt; pdump ypix.omag.4 xc,yc yes | tvmark 1 STDIN col=204
  </pre></div>
  <p>
  5. Run PHOT in batch mode using the coordinate file and the previously
  saved parameters. Verify the critical parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; wphot dev$ypix coords=ypix.coo.1 verify+ inter-
  
  ... output will appear in ypix.omag.5 ...
  </pre></div>
  <p>
  6. Repeat example 5 but assume that the input coordinate are ra and dec
  in degrees and degrees, turn off verification, and submit the task to to
  the background.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix 1
  
  ap&gt; rimcursor wcs=world &gt; radec.coo
  
  ... move to selected stars and type any key
  
  ... type ^Z to quit
  
  ap&gt; wphot dev$ypix coords=radec.coo wcsin=world verify- inter- &amp;
  
  ... output will appear in ypix.omag.6
  
  ap&gt; pdump ypix.omag.6 xc,yc yes | tvmark 1 STDIN col=204
  
  ... mark the stars on the display
  </pre></div>
  <p>
  7. Run PHOT interactively without using the image display.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; show stdimcur
  
  ... record the default value of stdimcur
  
  ap&gt; set stdimcur = text
  
  ... set the image cursor to the standard input
  
  ap&gt; wphot dev$ypix coords=ypix.coo.1
  
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
  
  ... type l to measure all the stars in the coordinate list
  
  ... a one line summary of the answers will appear on the standard
      output for each star measured
  
  ... type q to quit followed by q to confirm the quit
  
  ... full output will appear in the text file ypix.omag.7
  
  ap&gt; set stdimcur = &lt;default&gt;
  
  ... reset the value of stdimcur
  </pre></div>
  <p>
  8. Use a image cursor command file to drive the PHOT task. The cursor command
  file shown below sets the cbox, annulus, dannulus, and apertures parameters
  computes the centers, sky values, and magnitudes for 3 stars, updates the
  parameter files, and quits the task.
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
  
  ap&gt; wphot dev$ypix icommands=cmdfile  verify-
  
  ... full output will appear in ypix.omag.8
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  This task is experimental and requires more work.
  </p>
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
  datapars, centerpars, fitskypars, photpars, qphot, phot, polyphot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'ALGORITHMS' 'OUTPUT' 'ERRORS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

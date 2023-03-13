.. _fitpsf:

fitpsf: Model the stellar psf with an analytic function
=======================================================

**Package: apphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fitpsf image box
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
  <dl id="l_box">
  <dt><b>box    </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='box' Line='box    ' -->
  <dd>The width of the fitting box in scale units.
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords = ""' -->
  <dd>The list of text files containing initial coordinates for the objects to
  be centered. Objects are listed in coords one object per line with the
  initial coordinate values in columns one and two. The number of coordinate
  files must be zero, one, or equal to the number of images.
  If coords is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory specification then an
  coords file name of the form dir$root.extension.version is constructed and
  searched for, where dir is the directory, root is the root image name,
  extension is <span style="font-family: monospace;">"coo"</span> and version is the next available version number for the
  file.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">"default"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = "default"' -->
  <dd>The name of the results file or results directory. If output is
  <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory specification then an output file name
  of the form dir$root.extension.version is constructed, where dir is the
  directory, root is the root image name, extension is <span style="font-family: monospace;">"psf"</span> and version is
  the next available version number for the file. The number of output files
  must be zero, one, or equal to the number of image files.  In both interactive
  and batch mode full output is written to output. In interactive mode
  an output summary is also written to the standard output.
  </dd>
  </dl>
  <dl id="l_datapars">
  <dt><b>datapars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datapars' Line='datapars = ""' -->
  <dd>The name of the file containing the data dependent parameters.
  The critical parameters <i>fwhmpsf</i> and <i>sigma</i> are located in
  datapars.  If datapars is undefined then the default parameter set in
  uparm directory is used.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"radgauss"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "radgauss"' -->
  <dd>The function to be fit. The options are:
  <dl>
  <dt><b>radgauss</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='radgauss' Line='radgauss' -->
  <dd>A 2D radial Gaussian function is fit. The parameters of the fitting function
  are: x and y center, sigma of the Gaussian, amplitude of the Gaussian and
  the local sky value.
  </dd>
  </dl>
  <dl>
  <dt><b>elgauss</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='elgauss' Line='elgauss' -->
  <dd>A 2D elliptical Gaussian function is fit. The parameters of the fitting
  function are: x and y center, x and y sigma of the Gaussian, amplitude of
  the Gaussian and the local sky value.
  </dd>
  </dl>
  <dl>
  <dt><b>moments</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='moments' Line='moments' -->
  <dd>The 0th, 1st and 2nd order moments are computed and used to derive
  estimates of the
  x and y center values, radius of gyration, ellipticity and position
  angle of the object.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_maxiter">
  <dt><b>maxiter = 50</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxiter' Line='maxiter = 50' -->
  <dd>The maximum number of iterations that the non-linear fitting routines will
  perform in an attempt to find a satisfactory fit.
  </dd>
  </dl>
  <dl id="l_nreject">
  <dt><b>nreject = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nreject' Line='nreject = 0' -->
  <dd>The maximum number of rejection cycles performed after the fit.
  The default is no rejection.
  </dd>
  </dl>
  <dl id="l_kreject">
  <dt><b>kreject = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='kreject' Line='kreject = 3.0' -->
  <dd>The k-sigma rejection limit in units of sigma.
  </dd>
  </dl>
  <dl id="l_mkbox">
  <dt><b>mkbox = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mkbox' Line='mkbox = no' -->
  <dd>Draw the fitting box on the image display?
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Run the task interactively ?
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
  <dd>Update the critical parameters in non-interactive mode if verify is set of
  <span style="font-family: monospace;">"yes"</span> ? Update may be set to the apphot package parameter value (the default),
  <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = <span style="font-family: monospace;">")_.verbose"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = ")_.verbose"' -->
  <dd>Print messages on the terminal in non-interactive mode ? Verbose may be set
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
  <dd>The default display device.  Display may be set to the apphot package
  parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.  By default graphics overlay
  is disabled.  Setting display to one of <span style="font-family: monospace;">"imdr"</span>, <span style="font-family: monospace;">"imdg"</span>, <span style="font-family: monospace;">"imdb"</span>, or <span style="font-family: monospace;">"imdy"</span>
  enables graphics overlay with the IMD graphics kernel.  Setting display to
  <span style="font-family: monospace;">"stdgraph"</span> enables FITPSF to work interactively from a contour plot.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  FITPSF models the stellar brightness distribution of objects in the IRAF image
  <i>image</i> using non-linear least squares techniques and writes the
  list of model parameters and associated errors to the file <i>output</i>.
  Initial coordinates for the objects are read from the image cursor or
  the text file <i>coords</i>.  Pixels in a subraster of width <i>box * scale</i>
  are extracted and used in the fit.
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
  is enabled and FITPSF is run interactively the first measurement will appear
  to take a long time as the entire image must be read in before the measurement
  is actually made. All subsequent measurements will be very fast because FITPSF
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
  FITPSF can be run either interactively or in batch mode by setting the
  parameter <i>interactive</i>. In interactive mode starting x and y positions
  can either be read directly from the image cursor or read from the text
  file specified by <i>coords</i>. In batch mode the estimated
  positions can be read from the text file <i>coords</i> or the image cursor
  parameter <i>icommands</i> can be redirected to a text file containing
  a list of cursor commands.
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  The currently available cursor commands are listed below.
  </p>
  <div class="highlight-default-notranslate"><pre>
                 Interactive Keystroke Commands
  
  ?       Print help
  :       Colon commands
  v       Verify the critical parameters
  w       Save the current parameters
  d       Plot radial profile of current star
  i       Interactively set parameters using current star
  f       Fit current star
  spbar   Fit current star, output results
  m       Move to next star in coordinate list
  n       Fit next star in coordinate list, output results
  l       Fit remaining stars in coordinate list, output results
  e       Print error messages
  r       Rewind the coordinate list
  q       Exit task
  
                   Colon Commands
  
  :show   [data/fit]      List the parameters
  :m [n]  Move to next [nth] star in coordinate list
  :n [n]  Fit next [nth] star in coordinate list, output results
  
                  Colon Parameter Editing Commands
  
  # Image and file name parameters
  
  :image          [string]        Image name
  :coords         [string]        Coordinate file name
  :output         [string]        Output file name
  
  # Data dependent parameters
  
  :scale          [value]         Image scale (units per pixel)
  :fwhmpsf        [value]         Scale factor (scale units)
  :emission       [y/n]           Emission feature (y), absorption (n)
  :sigma          [value]         Standard deviation of sky (counts)
  :datamin        [value]         Minimum good data value (counts)
  :datamax        [value]         Maximum good data value (counts)
  
  # Noise description parameters
  
  :noise          [string]        Noise model (constant|poisson)
  :gain           [string]        Gain image header keyword
  :ccdread        [string]        Readout noise image header keyword
  :epadu          [value]         Gain (electrons  per adu)
  :readnoise      [value]         Readnoise (electrons)
  
  # Observation parameters
  
  :exposure       [string]        Exposure time image header keyword
  :airmass        [string]        Airmass image header keyword
  :filter         [string]        Filter image header keyword
  :obstime        [string]        Time of observation image header keyword
  :itime          [value]         Exposure time (time units)
  :xairmass       [value]         Airmass value (number)
  :ifilter        [string]        Filter id string
  :otime          [string]        Time of observation (time units)
  
  # Fitting parameters
  
  :function       [string]        PSF model (radgauss|elgauss|moments)
  :box            [value]         Width of the fitting box (scale units)
  :maxiter        [value]         Maximum number of iterations
  :nreject        [value]         Maximum number of rejection cycles
  :kreject        [value]         Rejection limit (sigma)
  
  # Plotting and marking functions
  
  :mkbox          [y/n]           Mark the fitting box on the display
  
  The following command are available from within the interactive setup menu.
  
                      Interactive Fitpsf Setup Menu
  
          v       Mark and verify the critical fitpsf parameters (f,s,b)
  
          f       Mark and verify the full-width half-maximum of the psf
          s       Mark and verify the standard deviation of the background
          l       Mark and verify the minimum good data value
          u       Mark and verify the maximum good data value
  
          b       Mark and verify the half-width of the fitting box
  </pre></div>
  </section>
  <section id="s_algorithms">
  <h3>Algorithms</h3>
  <p>
  The fitting parameters are <i>function</i>, the functional form of the model
  to be fit, <i>maxiter</i>, the maximum number of iterations per fit,
  <i>kreject</i>, the K-sigma rejection limit and <i>nreject</i>, the maximum
  number of rejection cycles. The currently available functions are a 2D
  moments analysis <span style="font-family: monospace;">"moments"</span>, a 2D radial Gaussian <span style="font-family: monospace;">"radgauss"</span>,  and a
  2D elliptical Gaussian <span style="font-family: monospace;">"elgauss"</span>.
  </p>
  <p>
  The weighting of the fit is determined by the parameter <i>noise</i> in the 
  <i>datapars</i> file. The two options are <i>constant</i>, in which all the
  weights are set to 1 and <i>poisson</i> in which the weights are equal to
  the inverse of the counts divided by the image gain read from the datapars
  <i>gain</i> or <i>epadu</i> parameters plus the square of the readout noise
  determined from the datapars parameters <i>ccdread</i> or <i>readnoise</i>.
  If <i>function</i> is either <span style="font-family: monospace;">"radgauss"</span> or <span style="font-family: monospace;">"ellgauss"</span> then the datapars
  parameter <i>fwhmpsf</i> is used to determine the initial guess for the
  Gaussian sigma.  The datapars parameter <i>threshold</i> determines the
  intensity threshold above which the moment analysis is performed.
  </p>
  </section>
  <section id="s_output">
  <h3>Output</h3>
  <p>
  In interactive mode the following quantities are printed on the
  terminal as shown below, for the radial Gaussian, elliptical Gaussian and
  moments functions respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  image  xcenter  ycenter  rsigma  amplitude  sky  err
  
  image  xcenter  ycenter  xsigma  ysigma rot  amplitude  sky  err
  
  image  xcenter  ycenter  rgyrat  ellip  pa amplitude  sky  err
  </pre></div>
  <p>
  In both interactive and batch mode the full output is written to the
  text file <i>output</i>. At the beginning of each file is a header
  listing the values of the parameters when the first stellar
  record was written. These parameters can be subsequently altered.
  For each star measured the following record is written for the radial
  Gaussian, elliptical Gaussian, and moments functions respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  image  xinit  yinit  id  coords  lid
      xcenter  ycenter  rsigma  amplitude  sky
      excenter eycenter ersigma eamplitude esky  ier  error
  
  image  xinit  yinit  id  coords  lid
      xcenter  ycenter  xsigma  ysigma  rot  amplitude  sky
      excenter eycenter exsigma eysigma erot eamplitude esky  ier\
      error
  
  image  xinit  yinit  id  coords  lid
      xcenter  ycenter  rgyrat  ellip  pa amplitude  sky
      excenter eycenter ergyrat eellip epa eamplitude esky  ier\
      error
  </pre></div>
  <p>
  Image and coords are the name of the image and coordinate files respectively.
  Id and lid are the sequence numbers of stars in the output and coordinate
  files respectively and xinit and yinit are the initial positions.
  Xcenter and ycenter are the computed x and y
  positions of the object. Rsigma, xsigma and ysigma are the distance from
  the center of the Gaussian at which the Gaussian is equal to exp (-0.5)
  of its central value. Xsigma and ysigma refer to those values along the major
  and minor axes of the ellipse respectively. The amplitude and sky refer to
  the amplitude of
  the Gaussian function and a constant background value respectively.
  If function = <span style="font-family: monospace;">"moments"</span> amplitude and sky refer to the total intensity
  above threshold and sky is the threshold value. Rot and pa are position angles
  of the major axis measured counter-clockwise with respect to the x axis.
  Rgyrat is the radius
  of gyration of the object and ellip its ellipticity.
  Quantities prefixed by an e represent the errors in the corresponding
  fitted parameters.
  </p>
  </section>
  <section id="s_errors">
  <h3>Errors</h3>
  <p>
  If all went well in the fitting process the error code stored in the ier
  field described above is 0. Non-zero values of ier flag the following error
  conditions.
  </p>
  <div class="highlight-default-notranslate"><pre>
    0     # No error
  401     # The fitting box is off the image
  402     # The fitting box is partially off the image
  403     # There are too few points to fit the function
  404     # The fit is singular
  405     # The fit did not converge
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the radial Gaussian function parameters for a few  stars in dev$ypix
  using the display and the image cursor. Setup the task parameters using
  the interactive setup menu defined by the i key command. Use uniform
  weighting.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix 1 fi+
  
  ... display the image
  
  ap&gt; fitpsf dev$ypix 11 noise=constant
  
  ... type ? to see the help screen
  
  ... move the image cursor to a star
  ... type i to enter the interactive setup menu
  ... enter maximum radius in pixels of the radial profile or type
      CR to accept the default value
  ... set the fitting box width, fwhmpsf, and sigma using the graphics
      cursor and the stellar radial profile plot
  ... typing &lt;CR&gt; leaves everything at the default value
  ... type q to quit the setup menu
  
  ... type the v key to verify the parameters
  
  ... type the w key to save the parameters in the parameter files
  
  ... move the image cursor to the stars of interest and tap
      the space bar
  
  ... a one line summary of the fitted parameters will appear on the
      standard output for each star measured
  
  ... type q to quit and another q to confirm the quit
  
  ... the full output will appear in ypix.psf.1
  </pre></div>
  <p>
  2. Compute the radial Gaussian function  parameters for a few  stars in 
  dev$ypix using the contour plot and the graphics cursor. Setup the task
  parameters using the interactive setup menu defined by the i key command.
  Use uniform weighting.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; show stdimcur
  
  ... save the current value of stdimcur
  
  ap&gt; set stdimcur = stdgraph
  
  ... define the image cursor to be the graphics cursor
  
  ap&gt; contour dev$ypix &gt;G ypix.plot1
  
  ... store the contour plot of dev$ypix in the file ypix.plot1
  
  ap&gt; fitpsf dev$ypix 11.0 noise=constant display=stdgraph
  
  ... type ? to get a short help page on the screen
  
  ... move the graphics cursor to a star
  ... type i to enter the interactive setup menu
  ... enter the maximum radius in pixels of the radial profile or
      type CR to accept the default value
  ... set the fitting box width, fwhmpsf, and sigma using the graphics
      cursor and the stellar radial profile plot
  ... typing &lt;CR&gt; leaves everything at the default value
  ... type q to quit the setup menu
  
  ... type the v key to verify critical parameters
  
  ... type the w key to save the parameters in the parameter files
  
  ... retype :.read ypix.plot1 to reload the contour plot
  
  ... move the graphics cursor to the stars of interest and tap
      the space bar
  
  ... a one line summary of the fitted parameters will appear on the
      standard output for each star measured
  
  ... type q to quit and q again to confirm the quit
  
  ... full output will appear in the text file ypix.psf.2
  </pre></div>
  <p>
  3. Setup and run FITPSF interactively on a list of objects temporarily
  overriding the fwhmpsf and sigma parameters determined in examples 1 or 2.
  Use uniform weighting.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; daofind dev$ypix fwhmpsf=2.6 sigma=25.0 verify-
  
  ... make a coordinate list
  
  ... the output will appear in the text file ypix.coo.1
  
  ap&gt; fitpsf dev$ypix 11.0 fwhmpsf=2.6 noise=constant coords=ypix.coo.1
  
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
  
  ... the output will appear in ypix.psf.3 ...
  </pre></div>
  <p>
  4. Display and fit some stars in an image section and write the output
  coordinates in the coordinate system of the parent image. Use uniform 
  weighting.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix[150:450,150:450] 1
  
  ... display the image section
  
  ap&gt; fitpsf dev$ypix[150:450,150:450] 11.0 noise=constant wcsout=tv
  
  ... move cursor to stars and type spbar
  
  ... type q to quit and q again to confirm quit
  
  ... output will appear in ypix.psf.4
  
  ap&gt; pdump ypix.psf.4 xc,yc yes | tvmark 1 STDIN col=204
  </pre></div>
  <p>
  5. Run FITPSF in batch mode using the coordinate file and the previously
  saved parameters. Use uniform weighting. Verify the critical parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; fitpsf dev$ypix 11.0 coords=ypix.coo.1 noise=constant verify+ \
      inter-
  
  ... output will appear in ypix.psf.5 ...
  </pre></div>
  <p>
  6. Repeat example 5 but assume that the input coordinate are ra and dec
  in degrees and degrees, turn off verification, and submit the task to to
  the background. Use uniform weighting.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix 1
  
  ap&gt; rimcursor wcs=world &gt; radec.coo
  
  ... move to selected stars and type any key
  
  ... type ^Z to quit
  
  ap&gt; fitpsf dev$ypix 11.0 coords=radec.coo noise=constant \
      wcsin=world verify- inter- &amp;
  
  ... output will appear in ypix.psf.6
  
  ap&gt; pdump ypix.psf.6 xc,yc yes | tvmark 1 STDIN col=204
  
  ... mark the stars on the display
  </pre></div>
  <p>
  7. Run FITPSF interactively without using the image display.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; show stdimcur
  
  ... record the default value of stdimcur
  
  ap&gt; set stdimcur = text
  
  ... set the image cursor to the standard input
  
  ap&gt; fitpsf dev$ypix 11.0 coords=ypix.coo.1 noise=constant
  
  ... type ? for optional help
  
  ... type :m 3 to set the initial coordinates to those of the
      third star in the list
  
  ... type i to enter the interactive setup menu
  ... enter the maximum radius in pixels for the radial profile or
      accept the default with a CR
  ... type v to enter the default menu
  ... set the fwhmpsf, sigma, and fitting box size  using the
      graphics cursor and the stellar radial profile plot
  ... typing &lt;CR&gt; after the prompt leaves the parameter at its default
      value
  ... type q to quit the setup menu
  
  ... type r to rewind the coordinate list
  
  ... type l to measure all the stars in the coordinate list
  
  ... a one line summary of the answers will appear on the standard
      output for each star measured
  
  ... type q to quit followed by q to confirm the quit
  
  ... full output will appear in the text file ypix.psf.7
  
  ap&gt; set stdimcur = &lt;default&gt;
  
  ... reset the value of stdimcur
  </pre></div>
  <p>
  8. Use an image cursor command file to drive the FITPSF task. The cursor command
  file shown below sets the fwhmpsf, sigma, and noise, computes the model
  fit parameter values for 3 stars, updates the parameter files, and quits
  the task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; type cmdfile
  : fwhmpsf 2.6
  : sigma 5.0
  : noise constant
  442 410 101 \040
  349 188 101 \040
  225 131 101 \040
  w
  q
  
  ap&gt; fitpsf dev$ypix 11.0 icommands=cmdfile verify-
  
  ... full output will appear in ypix.psf.8
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  In interactive mode the user should not change the type function to be fit
  after the first record is written to the output file. In this case the file
  header and record structure will not match.
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
  blue or yellow overlays and set the  mkbox switch to<span style="font-family: monospace;">"yes"</span>.
  It may be necessary to run gflush and to redisplay the image
  to get the overlays position correctly.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  datapars, radprof
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'ALGORITHMS' 'OUTPUT' 'ERRORS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

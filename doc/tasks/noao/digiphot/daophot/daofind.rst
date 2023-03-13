.. _daofind:

daofind: Find stars in an image using the DAO algorithm
=======================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  daofind image output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The list of images in which objects are to be detected.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output ' -->
  <dd>The name of the results file or the results directory. If output is
  <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span> or a directory specification then a results file
  name of the form dir$root.extension.version is constructed, where
  dir is the directory, root is the root image name, extension is <span style="font-family: monospace;">"coo"</span>
  and version is the next available version number for the file. If the
  output string is undefined then no output file is created. One output
  file is created for every input image.
  </dd>
  </dl>
  <dl id="l_starmap">
  <dt><b>starmap = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='starmap' Line='starmap = ""' -->
  <dd>The name of the image prefix and/or directory where the density enhancement
  image will be stored. If starmap is undefined or a directory,
  DAOFIND will create a temporary image which is deleted on exit from
  the program. Otherwise starmap is prefixed to the image name
  and the density enhancement image will be saved for use in a subsequent
  run of DAOFIND.
  </dd>
  </dl>
  <dl id="l_skymap">
  <dt><b>skymap = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skymap' Line='skymap = ""' -->
  <dd>The name of the image prefix and/or directory where the mean density
  image will be stored.  If skymap is undefined or a directory, no mean density
  image is created. Otherwise skymap is prefixed to the image name
  and the mean density image will be saved on disk. Skymap is not used by
  the DAOFIND algorithms, but may be used by the user as a check on DAOFIND,
  since the sum of starmap and skymap is a type of best fit to the original
  image.
  </dd>
  </dl>
  <dl id="l_datapars">
  <dt><b>datapars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datapars' Line='datapars = ""' -->
  <dd>The name of the file containing the data dependent parameters. The critical
  parameters <i>fwhmpsf</i> and <i>sigma</i> are located here.  If <i>datapars</i>
  is undefined then the default parameter set in the user's uparm directory is
  used.
  </dd>
  </dl>
  <dl id="l_findpars">
  <dt><b>findpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='findpars' Line='findpars = ""' -->
  <dd>The name of the file containing the object detection parameters. The
  parameter <i>threshold</i> is located here. If findpars is undefined then
  the default parameter set in the user's uparm directory is used.
  </dd>
  </dl>
  <dl id="l_boundary">
  <dt><b>boundary = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary' Line='boundary = "nearest"' -->
  <dd>The type of boundary extension. The choices are:
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
  <dt><b>constant = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constant' Line='constant = 0' -->
  <dd>The constant for constant boundary extension.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Interactive or batch mode?
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
  <dl id="l_wcsout">
  <dt><b>wcsout = <span style="font-family: monospace;">")_.wcsout"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcsout' Line='wcsout = ")_.wcsout"' -->
  <dd>The coordinate system of the output coordinates written to <i>output</i>. The
  image header coordinate system is used to transform from the internal <span style="font-family: monospace;">"logical"</span>
  pixel coordinate system to the output coordinate system. The output coordinate
  system options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, and <span style="font-family: monospace;">"physical"</span>. The image cursor coordinate
   system is assumed to be the <span style="font-family: monospace;">"tv"</span> system.
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
  The wcsout parameter defaults to the value of the package parameter of the same
   name. The default values of the package parameters wcsin and wcsout are
  <span style="font-family: monospace;">"logical"</span> and <span style="font-family: monospace;">"logical"</span> respectively.
  </dd>
  </dl>
  <dl id="l_cache">
  <dt><b>cache = <span style="font-family: monospace;">")_.cache"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cache' Line='cache = ")_.cache"' -->
  <dd>Cache the image pixels in memory. Cache may be set to the value of the apphot
  package parameter (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>. By default caching is
  disabled.
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = <span style="font-family: monospace;">")_.verify"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = ")_.verify"' -->
  <dd>Automatically confirm the critical parameters when running in non-interactive
  mode ? Verify may be set to the daophot package parameter value (the default),
  <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = <span style="font-family: monospace;">")_.update"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = ")_.update"' -->
  <dd>Automatically update the parameters when running in non-interactive mode if
  verify is <span style="font-family: monospace;">"yes"</span>? Update may be set to the daophot package parameter value
  (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = <span style="font-family: monospace;">")_.verbose"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = ")_.verbose"' -->
  <dd>Print out information about the progress of the task in non-interactive mode.
  Verbose may be set to the daophot package parameter value (the default), <span style="font-family: monospace;">"yes"</span>,
  or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">")_.graphics"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = ")_.graphics"' -->
  <dd>The standard graphics device.  Graphics may be set to the apphot package
  parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_display">
  <dt><b>display = <span style="font-family: monospace;">")_.display"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='display' Line='display = ")_.display"' -->
  <dd>The standard image display device. Display may be set to the apphot package
  parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>. By default graphics overlay is
  disabled.  Setting display to one of <span style="font-family: monospace;">"imdr"</span>, <span style="font-family: monospace;">"imdg"</span>, <span style="font-family: monospace;">"imdb"</span>, or <span style="font-family: monospace;">"imdy"</span> enables
  graphics overlay with the IMD graphics kernel.  Setting display to <span style="font-family: monospace;">"stdgraph"</span>
  enables DAOFIND to work interactively from a contour plot.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  DAOFIND searches the IRAF images <i>image</i> for local density maxima,
  with a full-width half-maxima of <i>datapars.fwhmpsf</i>, and a peak amplitude
  greater than <i>findpars.threshold</i> * <i>datapars.sigma</i> above the local
  background, and writes a list of detected objects in the file <i>output</i>.
  The detected objects are also listed on the standard output if the program is
  running in interactive mode or if the <i>verbose</i> switch is enabled in
  non-interactive mode.
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
  are large enough, the input and output image pixels are cached in memory. If
  caching is enabled and DAOFIND is run interactively the first measurement
  will appear to take a long time as the entire image must be read in before the
  measurement is actually made. All subsequent measurements will be very fast
  because DAOFIND is accessing memory not disk. The point of caching is to speed
  up random image access by making the internal image i/o buffers the same size
  as the image itself. However if the input object lists are sorted in row order
  and sparse caching may actually worsen not improve the execution time. Also at
  present there is no point in enabling caching for images that are less than
  or equal to 524288 bytes, i.e. the size of the test image dev$ypix, as the
  default image i/o buffer is exactly that size. However if the size of dev$ypix
  is doubled by converting it to a real image with the chpixtype task then the
  effect of caching in interactive is can be quite noticeable if measurements
  of objects in the top and bottom halves of the image are alternated.
  </p>
  <p>
  DAOFIND can be run either interactively or in batch mode by setting the
  parameter <i>interactive</i>. In interactive mode the user can examine,
  adjust and save algorithm parameters, and fit or refit the entire list
  with the chosen parameter set. The <i>verify</i> parameter can be used to
  automatically confirm the critical parameters <i>datapars.fwhmpsf</i> and
  <i>datapars.sigma</i> when running in non-interactive mode.
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <div class="highlight-default-notranslate"><pre>
               Interactive Keystroke Commands
  
  ?       Print help
  :       Colon commands
  v       Verify critical parameters
  w       Save the current parameters
  d       Plot radial profile of star near cursor
  i       Interactively set parameters using star near cursor
  f       Find stars in the image
  spbar   Find stars in the image and output results
  q       Exit task
  
                  Colon Commands
  
  :show           [data/find]     List the parameters
  
                  Colon Commands
  
  # Image and file name parameters
  
  :image          [string]        Image name
  :output         [string]        Output file name
  
  # Data dependent parameters
  
  :scale          [value]         Image scale (units per pixel)
  :fwhmpsf        [value]         Full width half maximum of psf (scale units)
  :emission       [y/n]           Emission feature (y), absorption (n)
  :sigma          [value]         Standard deviation of sky (counts)
  :datamin        [value]         Minimum good data value (counts)
  :datamax        [value]         Maximum good data value (counts)
  
  # Noise description parameters
  
  :noise          [string]        Noise model (constant|poisson)
  :gain           [string]        Gain image header keyword
  :ccdread        [string]        Readout noise image header keyword
  :epadu          [value]         Gain (electrons per adu)
  :readnoise      [value]         Readout noise (electrons)
  
  # Observation parameters
  
  :exposure       [string]        Exposure time image header keyword
  :airmass        [string]        Airmass image header keyword
  :filter         [string]        Filter image header keyword
  :obstime        [string]        Time of observation image header keyword
  :itime          [value]         Exposure time (time units)
  :xairmass       [value]         Airmass value (number)
  :ifilter        [string]        Filter id string
  :otime          [string]        Time of observation (time units)
  
  # Object detection parameters
  
  :nsigma         [value]         Size of Gaussian kernel (sigma)
  :threshold      [value]         Detection intensity threshold (counts)
  :ratio          [value]         Sigmay / sigmax of Gaussian kernel
  :theta          [value]         Position angle of Gaussian kernel
  :sharplo        [value]         Lower bound on sharpness
  :sharphi        [value]         Upper bound on sharpness
  :roundlo        [value]         Lower bound on roundness
  :roundhi        [value]         Upper bound on roundness
  
  # Plotting and marking commands
  
  :mkdetections   [y/n]           Mark detections on the image display
  
  The following commands are available from inside the interactive setup menu.
  
                      Interactive Daofind Setup Menu
  
          v       Mark and verify critical daofind parameters (f,s)
  
          f       Mark and verify the full-width half-maximum of the psf
          s       Mark and verify the standard deviation of the background
          l       Mark and verify the minimum good data value
          u       Mark and verify the maximum good data value
  </pre></div>
  </section>
  <section id="s_algorithms">
  <h3>Algorithms</h3>
  <p>
  DAOFIND approximates the stellar point spread function with an elliptical
  Gaussian function, whose sigma along the semi-major axis is 0.42466 *
  <i>datapars.fwhmpsf</i> / <i>datapars.scale</i> pixels, semi-minor to semi-major
  axis ratio is <i>ratio</i>, and major axis position angle is <i>theta</i>.
  Using this model, a convolution kernel, truncated at <i>nsigma</i> sigma,
  and normalized so as to sum to zero, is constructed.
  </p>
  <p>
  The density enhancement image <i>starmap</i> is computed by convolving the input
  image with the Gaussian kernel. This operation is mathematically equivalent to
  fitting, in the least-squares sense, the image data at each point with a
  truncated, lowered elliptical Gaussian function. After convolution each point
  in <i>starmap</i> contains as estimate of the amplitude of the best fitting
  Gaussian function at that point. Each point in <i>skymap</i>, if the user
  chooses to compute it, contains an estimate of the best fitting sky value
  at that point.
  </p>
  <p>
  After image convolution , DAOFIND steps through <i>starmap</i> searching
  for density enhancements greater than <i>findpars.threshold</i> *
  <i>datapars.sigma</i>, and brighter than all other density enhancements within
  a semi-major axis of 0.42466 <i>findpars.nsigma</i> * <i>datapars.fwhmpsf</i>.
  As the program selects candidates, it computes three shape characteristics,
  sharpness and 2 estimates of roundness.  The sharpness statistic measures the
  ratio of, the difference between the height of the central pixel and the mean
  of the surrounding non-bad pixels, to the height of the best fitting Gaussian
  function at that point. The first roundness characteristic computes the ratio
  of a measure of the bilateral symmetry of the object to a measure of the
  four-fold symmetry of the object. The second roundness statistic measures the
  ratio of, the difference in the height of the best fitting Gaussian function
  in x minus the best fitting Gaussian function in y, over the average of the
  best fitting Gaussian functions in x and y. The limits on these parameters
  <i>findpars.sharplo</i>, <i>findpars.sharphi</i> <i>findpars.roundlo</i>, and
  <i>findpars.roundhi</i>, are set to weed out non-astronomical objects and
  brightness enhancements that are elongated in x and y respectively.
  </p>
  <p>
  Lastly the x and y centroids of the detected objects are computed by estimating
  the x and y positions of the best fitting 1D Gaussian functions in x and y
  respectively, a rough magnitude is estimated by computing the ratio of the
  amplitude of the best fitting Gaussian at the object position to
  <i>findpars.threshold</i> * <i>datapars.sigma</i>, and the object is added to
  the output coordinate file.
  </p>
  </section>
  <section id="s_output">
  <h3>Output</h3>
  <p>
  In interactive mode or in non-interactive with the verbose switch turned on
  the following quantities are written to the terminal as each object is
  detected.
  </p>
  <div class="highlight-default-notranslate"><pre>
  xcenter  ycenter  mag  sharpness  sround  ground id
  
                 where
  
  mag = -2.5 * log10 (peak density / detection threshold)
  </pre></div>
  <p>
  The object centers are in pixels and the magnitude estimate measures the
  ratio of the maximum density enhancement to the detection threshold.
  Sharpness is typically around .5 to .8 for a star with a fwhmpsf similar to
  the pattern star. Both sround and ground are close to zero for a truly
  round star. Id is the sequence number of the star in the list.
  </p>
  <p>
  In both interactive and batch mode the full output is written to the text
  file <i>output</i>. At the beginning of each file is a header, listing
  the current values of the parameters when the first stellar record was
  written. The parameters can subsequently be altered.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Run daofind on the test image dev$ypix.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; daofind dev$ypix default fwhmpsf=2.5 sigma=5.0 threshold=20
  
  ... answer the verify prompts
  
  ... the output will appear in ypix.coo.1
  </pre></div>
  <p>
  2. Run daofind interactively on dev$ypix using the image display
  and image display cursor. Set the fwhmpsf and sigma parameters
  with the graphics cursor,  radial profile plot, and the interactive
  setup key i.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; display dev$ypix 1 fi+
  
  ... display the image
  
  da&gt; daofind dev$ypix default interactive+
  
  ... type ? to see help screen
  
  ... move display cursor to a star
  ... type i to enter the interactive setup menu
  ... enter maximum radius in pixels of the radial profile or
      accept default with a CR
  ... type v to enter the default setup menu
  ... set the fwhmpsf and sigma using the graphics cursor and the
      radial profile plot
  ... typing &lt;CR&gt; leaves the parameters at their default values
  ... type q to quit setup menu
  
  ... type the v key to verify the critical parameters
  
  ... type the w key to save the parameters in the parameter files
  
  ... type the space bar to detect stars in the image
  
  ... a 1 line summary of the answers will appear on the standard
      output for each star measured
  
  ... type q to quit and q again to confirm the quit
  
  ... full output will appear in the text file ypix.coo.2
  </pre></div>
  <p>
  3. Run daofind interactively on a single image using a contour plot in place
  of the image and the graphics cursor in place of the image cursor.
  This option is only useful for those (now very few) users who have access to
  a graphics terminal but not to an image display server. Set the fwhmpsf and
  sigma parameters with the graphics cursor and radial profile plot and the
  interactive setup key i.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; show stdimcur
  
  ... record the default value of stdimcur
  
  da&gt; set stdimcur = stdgraph
  
  ... define the image cursor to be the graphics cursor
  
  da&gt; contour dev$ypix
  
  ... make a contour plot of dev$ypix
  
  da&gt; contour dev$ypix &gt;G ypix.plot1
  
  ... store the contour plot of ypix in the file ypix.plot
  
  da&gt; daofind dev$ypix default display=stdgraph interactive+
  
  ... type ? to see the help screen
  
  ... move graphics cursor to a setup star
  ... type i to enter the interactive setup menu
  ... enter maximum radius in pixels of the radial profile or
      accept the default with a CR
  ... type v to enter the default setup menu
  ... set the fwhmpsf and sigma using the graphics cursor and the
      radial profile plot
  ... typing &lt;CR&gt; leaves the parameters at their default values
  ... type q to quit the setup menu
  
  ... type the v key to confirm the critical parameters
  
  ... type the w key to save the parameters in the parameter files
  
  ... retype :.read ypix.plot1 to reload the contour plot
  
  ... type the space bar to detect stars in the image
  
  ... a 1 line summary of the answers will appear on the standard
      output for each star measured
  
  ... full output will appear in the text file ypix.coo.3
  
  da&gt; set stdimcur = &lt;default&gt;
  
  ... reset the image cursor to its default value
  </pre></div>
  <p>
  4. Run DAOFIND interactively without using the image display cursor.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; show stdimcur
  
  ... record the default value of stdimcur
  
  da&gt; set stdimcur = text
  
  ... set the image cursor to the standard input
  
  da&gt; display dev$ypix 1
  
  ... display the image
  
  da&gt; daofind dev$ypix default interactive+
  
  ... type ? for help
  
  ... type "442 409 101 i" in response to the image cursor query where
      x and y are the coordinates of the star to be used as setup,
      101 is the default world coordinate system, and i enters the
      interactive setup menu.
  ... enter maximum radius in pixels of the radial profile or
      type CR to accept the default
  ... type v to enter the default setup menu
  ... set the fwhmpsf and sigma using the graphics cursor and the
      radial profile plot
  ... typing &lt;CR&gt; leaves the parameters at their default values
  ... type q to quit the setup menu
  
  ... type the v key to verify the parameters
  
  ... type the w key to save the parameters in the parameter files
  
  ... type the space bar to detect stars in the image
  
  ... a 1 line summary of the answers will appear on the standard
      output for each star measured
  
  ... type q to quit and q again to confirm
  
  ... full output will appear in the text file ypix.coo.4
  
  da&gt; set stdimcur = &lt;default&gt;
  
  ... reset the image cursor to its default value
  </pre></div>
  <p>
  5. Run daofind on a list of 3 images contained in the file imlist in batch mode.
  The program will ask the user to verify that the fwhmpsf and the threshold are
  correct before beginning execution.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; type imlist
  dev$ypix
  dev$wpix
  dev$pix
  
  da&gt; daofind @imlist default
  
  ... answer the verify prompts
  
  ... the output will appear in ypix.coo.5, wpix.coo.1, pix.coo.1
  </pre></div>
  <p>
  6. Display and find stars in an image section. Write the output coordinates
  in the coordinate system of the parent image. Mark the detected stars on
  the displayed image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; display dev$ypix[150:450,150:450] 1
  
  ... display the image section
  
  da&gt; daofind dev$ypix[150:450,150:450] default wcsout=tv
  
  ... answer the verify prompts
  
  ... output will appear in ypix.coo.6
  
  da&gt; tvmark 1 ypix.coo.6 col=204
  </pre></div>
  <p>
  7. Repeat example 5 but submit the job to the background  and turn off the
  verify and verbose switches.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; daofind @imlist default verify- verbose- &amp;
  
  ... the output will appear in ypix.coo.7, wpix.coo.2, pix.coo.2
  </pre></div>
  <p>
  8. Use an image cursor command file to drive the daofind task. The cursor
  command file shown below sets the fwhmpsf, sigma, and threshold parameters,
  located stars in the image, updates the parameter files, and quits the task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; type cmdfile
  : fwhmpsf 2.5
  : sigma 5.0
  : threshold 10.0
  \040
  w
  q
  
  da&gt; daofind dev$ypix default icommands=cmdfile verify-
  
  ... full output will appear in ypix.coo.8
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
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
  blue or yellow overlays and set the findpars mkdetections switch to
  <span style="font-family: monospace;">"yes"</span>. It may be necessary to run gflush and to redisplay the image
  to get the overlays position correctly.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  datapars,findpars
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'ALGORITHMS' 'OUTPUT' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

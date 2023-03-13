.. _fitsky:

fitsky: Compute sky values in a list of annular or circular regions
===================================================================

**Package: apphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fitsky image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The list of images containing the sky regions to be fit.
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
  directory, root is the root image name, extension is <span style="font-family: monospace;">"sky"</span> and version is
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
  <dd>The name of the file containing the data dependent parameters.
  The critical parameters <i>fwhmpsf</i> and <i>sigma</i> are located in
  datapars.  If datapars is undefined then the default parameter set in
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
  <dt><b>verify = <span style="font-family: monospace;">")._verify"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = ")._verify"' -->
  <dd>Verify the critical parameters in non-interactive mode ? Verify may be set to
   the apphot package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = <span style="font-family: monospace;">")_.update"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = ")_.update"' -->
  <dd>Update the critical parameters in non-interactive mode if verify is yes ?
  Update may be set to the apphot package parameter value (the default), <span style="font-family: monospace;">"yes"</span>,
  or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = <span style="font-family: monospace;">")_.verbose"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = ")_.verbose"' -->
  <dd>Print messages on the terminal in non-interactive mode ? Verbose may be set to
  the apphot package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
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
  FITSKY to work interactively from a contour plot.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  FITSKY computes accurate sky values for a set of objects in the IRAF image
  <i>image</i>, whose coordinates are read from the text file <i>coords</i> or
  the image display cursor, and writes the computed sky values to the text
  file <i>output</i>.
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
  is enabled and FITSKY is run interactively the first measurement will appear
  to take a long time as the entire image must be read in before the measurement
  is actually made. All subsequent measurements will be very fast because FITSKY
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
  FITSKY can be run either interactively or in batch mode by setting the parameter
  <i>interactive</i>. In interactive mode the user may either define the
  list of objects to be measured interactively with the image cursor or
  create an object list prior to running  FITSKY. In either case the user may
  adjust the sky fitting parameters until a satisfactory measurement is achieved.
  coordinate list with that set of parameters. In batch mode 
  positions are read from the text file <i>coords</i> or the image cursor
  parameter <i>icommands</i> can be redirected to a cursor command file.
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  The following cursor commands are currently available.
  </p>
  <div class="highlight-default-notranslate"><pre>
          Interactive Keystroke Commands
  
  ?       Print help
  :       Colon commands
  v       Verify the critical parameters
  w       Save the current parameters
  d       Plot radial profile of current star
  i       Interactively set parameters using current star
  f       Fit sky for current star
  spbar   Fit sky for current star, output results
  m       Move to next star in coordinate list
  m       Fit sky for next star in coordinate list, output results
  l       Fit sky for remaining stars in coordinate list, output results
  e       Print error messages
  r       Rewind the coordinate list
  q       Exit task
  
          Colon commands
  
  :show   [data/sky]      List the parameters
  :m [n]  Move to the next [nth] star in coordinate list
  :n [n]  Fit sky to next [nth] star in coordinate list, output results
  
          Colon Parameter Editing Commands
  
  # Image and file name parameters
  
  :image          [string]        Image name
  :coords         [string]        Coordinate file name
  :output         [string]        Output file name
  
  # Data dependent parameters
  
  :scale          [value]         Image scale (units per pixel)
  :fwhmpsf        [value]         Full width half maximum PSF (scale units)
  :emission       [y/n]           Emission feature (y), absorption (n)
  :sigma          [value]         Standard deviation of sky (counts)
  :datamin        [value]         Minimum good pixel value (counts)
  :datamax        [value]         Maximum good pixel value (counts)
  
  # Noise parameters
  
  :noise          [string]        Noise model (constant|poisson)
  :gain           [string]        Gain image header keyword
  :ccdread        [string]        Readout noise image header keyword
  :epadu          [value]         Gain (electrons per adu)
  :readnoise      [value]         Readout noise (electrons)
  
  # Observations parameters
  
  :exposure       [string]        Exposure time image header keyword
  :airmass        [string]        Airmass image header keyword
  :filter         [string]        Filter image header keyword
  :obstime        [string]        Time of observation image header keyword
  :itime          [value]         Exposure time (time units)
  :xairmass       [value]         Airmass value (number)
  :ifilter        [string]        Filter id string
  :otime          [string]        Time of observation (time units)
  
  # Sky fitting algorithm parameters
  
  :salgorithm     [string]        Sky fitting algorithm
  :skyvalue       [value]         User supplied sky value (counts)
  :annulus        [value]         Inner radius of sky annulus (scale units)
  :dannulus       [value]         Width of sky annulus (scale units)
  :khist          [value]         Sky histogram extent (+/- sky sigma)
  :smooth         [y/n]           Lucy smooth the sky histogram
  :binsize        [value]         Resolution of sky histogram (sky sigma)
  :smaxiter       [value]         Maximum number of iterations
  :sloclip        [value]         Low side clipping factor (percent)
  :shiclip        [value]         High side clipping factor (percent)
  :snreject       [value]         Maximum number of rejection cycles
  :sloreject      [value]         Low side pixel rejection limits (sky sigma)
  :shireject      [value]         High side pixel rejection limits (sky sigma)
  :rgrow          [value]         Region growing radius (scale units)
  
  # Marking and plotting parameters
  
  :mksky          [y/n]           Mark sky annuli on the display
  :radplot        [y/n]           Plot radial profile of sky pixels
  
  The following commands are available from within the interactive setup menu.
  
                        Interactive Fitsky Setup Menu
  
          v       Mark and verify the critical parameters (a,d,s)
  
          s       Mark and verify the standard deviation of the sky
          l       Mark and verify the minimum good data value
          u       Mark and verify the maximum good data value
  
          a       Mark and verify the inner radius of the sky annulus
          d       Mark and verify the width of the sky annulus
          g       Mark and verify the region growing radius
  </pre></div>
  </section>
  <section id="s_algorithms">
  <h3>Algorithms</h3>
  <p>
  A brief description of the data dependent parameters and the sky fitting
  parameters can be found in the online manual pages for the DATAPARS
  and FITSKYPARS tasks.
  </p>
  </section>
  <section id="s_output">
  <h3>Output</h3>
  <p>
  In interactive mode the following quantities are printed on the standard
  output as each object is measured.
  </p>
  <div class="highlight-default-notranslate"><pre>
  image  xinit  yinit  msky  stdev  sskew  nsky  nsrej  error
  </pre></div>
  <p>
  In both interactive and batch mode full output is written to the 
  text file <i>output</i>. At the beginning of each file is a header listing
  the current values of the parameters when the first stellar record was
  written. These parameters can be subsequently altered. For each star
  measured the following record is written.
  </p>
  <div class="highlight-default-notranslate"><pre>
  image  xinit  yinit  id  coords  lid
      msky  stdev  sskew  nsky  nsrej  sier  error
  </pre></div>
  <p>
  Image and coords are the name of the image and coordinate file respectively.
  Id and lid are the sequence numbers of stars in the output and coordinate
  files respectively. Sier and error are the error code and accompanying
  error message respectively. Xinit and yinit are the center coordinates
  of the sky annulus in pixels. Msky, stdev and sskew are the sky value,
  standard deviation and skew respectively. Nsky and nsrej are the number of
  sky pixels used and the number of sky pixels rejected respectively.
  </p>
  <p>
  In interactive mode a radial profile of each measured object is plotted
  in the graphics window if <i>radplots</i> is <span style="font-family: monospace;">"yes"</span>.
  </p>
  <p>
  In interactive and batch mode a radial profile plot is written to
  <i>plotfile</i>  if it is defined each time the result of an object
  measurement is written to <i>output</i> .
  </p>
  </section>
  <section id="s_errors">
  <h3>Errors</h3>
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
  212       # The best fit parameters are non-physical
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the sky values for a few  stars in dev$ypix using the display
  and the image cursor. Setup the task parameters using the interactive
  setup menu defined by the i key command and a radial profile plot.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix 1 fi+
  
  ... display the image
  
  ap&gt; fitsky dev$ypix
  
  ... type ? to print an optional help page
  
  ... move the image cursor to a star
  ... type i to enter the interactive setup menu
  ... enter maximum radius in pixels of the radial profile or hit
      CR to accept the default
  ... set the inner and outer sky annuli, and sigma  using the
      graphics cursor and the stellar radial profile plot
  ... typing &lt;CR&gt; leaves everything at the default value
  ... type q to quit the setup menu
  
  ... type the v key to verify the parameters
  
  ... type the w key to save the parameters in the parameter files
  
  ... move the image cursor to the stars of interest and tap
      the space bar
  
  ... a one line summary of the fitted parameters will appear on the
      standard output for each star measured
  
  ... type q to quit and q again to confirm the quit
  
  ... the output will appear in ypix.sky.1
  </pre></div>
  <p>
  2. Compute the sky values for a few stars in dev$ypix using a contour plot
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
  
  ap&gt; fitsky dev$ypix display=stdgraph
  
  ... type ? to get an optional help page
  
  ... move graphics cursor to a star
  ... type i to enter the interactive setup menu
  ... enter maximum radius in pixels of the radial profile or CR
      to accept the default value
  ... set the inner and outer sky annuli, and sigma using the
      graphics cursor and the stellar radial profile plot
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
  
  ... full output will appear in the text file ypix.sky.2
  
  ap&gt; set stdimcur = &lt;default&gt;
  
  ... reset stdimcur to its previous value
  </pre></div>
  <p>
  3. Setup and run FITSKY interactively on a list of objects temporarily
  overriding the fwhmpsf, sigma, annulus, and dannulus parameters determined
  in examples 1 or 2.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; daofind dev$ypix fwhmpsf=2.6 sigma=25.0 verify-
  
  ... make a coordinate list
  
  ... the output will appear in the text file ypix.coo.1
  
  ap&gt; fitsky dev$ypix annulus=12.0 dannulus=5.0 coords=ypix.coo.1
  
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
  
  ... the output will appear in ypix.sky.3 ...
  </pre></div>
  <p>
  4. Display and measure some stars in an image section and write the output
  coordinates in the coordinate system of the parent image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; display dev$ypix[150:450,150:450] 1
  
  ... display the image section
  
  ap&gt; fitsky dev$ypix[150:450,150:450] wcsout=tv
  
  ... move cursor to stars and type spbar
  
  ... type q to quit and q again to confirm quit
  
  ... output will appear in ypix.sky.4
  
  ap&gt; pdump ypix.sky.4 xi,yi yes | tvmark 1 STDIN col=204
  </pre></div>
  <p>
  5. Run FITSKY in batch mode using the coordinate file and the previously
  saved parameters. Verify the critical parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; fitsky dev$ypix coords=ypix.coo.1 verify+ inter-
  
  ... output will appear in ypix.sky.5 ...
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
  
  ap&gt; fitsky dev$ypix coords=radec.coo wcsin=world verify- inter- &amp;
  
  ... output will appear in ypix.sky.6
  
  ap&gt; pdump ypix.sky.6 xi,yi yes | tvmark 1 STDIN col=204
  
  ... mark the stars on the display
  </pre></div>
  <p>
  7. Run FITSKY interactively without using the image display.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; show stdimcur
  
  ... record the default value of stdimcur
  
  ap&gt; set stdimcur = text
  
  ... set the image cursor to the standard input
  
  ap&gt; fitsky dev$ypix coords=ypix.coo.1
  
  ... type ? for optional help
  
  ... type :m 3 to set the initial coordinates to those of the
      third star in the list
  
  ... type i to enter the interactive setup menu
  ... enter the maximum radius in pixels for the radial profile or
      accept the default with a CR
  ... type v to enter the default menu
  ... set the inner and outer sky annuli, and sigma using the
      graphics cursor and the stellar radial profile plot
  ... typing &lt;CR&gt; after the prompt leaves the parameter at its default
      value
  ... type q to quit the setup menu
  
  ... type r to rewind the coordinate list
  
  ... type l to measure all the stars in the coordinate list
  
  ... a one line summary of the answers will appear on the standard
      output for each star measured
  
  ... type q to quit followed by q to confirm the quit
  
  ... full output will appear in the text file ypix.sky.7
  
  ap&gt; set stdimcur = &lt;default&gt;
  
  ... reset the value of stdimcur
  </pre></div>
  <p>
  8. Use an image cursor command file to drive the FITSKY task. The cursor command
  file shown below sets the annulus and dannulus parameters, computes the sky
  values for 3 stars, updates the parameter files, and quits the task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ap&gt; type cmdfile
  : annulus 12.0
  : dannulus 5.0
  442 410 101 \040
  349 188 101 \040
  225 131 101 \040
  w
  q
  
  ap&gt; fitsky dev$ypix icommands=cmdfile verify-
  
  ... full output will appear in ypix.sky.8
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
  blue or yellow overlays and set the fitskypars mksky switch to<span style="font-family: monospace;">"yes"</span>.
  It may be necessary to run gflush and to redisplay the image
  to get the overlays position correctly.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  datapars, fitskypars, phot, polyphot, radprof
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'ALGORITHMS' 'OUTPUT' 'ERRORS' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

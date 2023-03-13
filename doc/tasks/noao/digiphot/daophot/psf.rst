.. _psf:

psf: Compute the point spread function
======================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  psf image photfile pstfile psfimage opstfile groupfile
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The images for which the PSF model is to be built.
  </dd>
  </dl>
  <dl id="l_photfile">
  <dt><b>photfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='photfile' Line='photfile' -->
  <dd>The list of input photometry files. The number of photometry files must
  be equal to the number of input images. If photfile is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>,
  or a directory specification  PSF searches for a file called dir$image.mag.# 
  where # is the highest available version number for the file. Photfile is
  normally the output of the PHOT task but may also be the  output of the PSF,
  PEAK, NSTAR and ALLSTAR tasks. Photfile may be an APPHOT/DAOPHOT text database
  or an STSDAS binary table.
  </dd>
  </dl>
  <dl id="l_pstfile">
  <dt><b>pstfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pstfile' Line='pstfile' -->
  <dd>The list of input psf star photometry files. The ids of the psf stars in these
  files must be the same as their ids in <i>photfile</i>. The number of psf
  star files must be zero or equal to the number of input images. If pstfile
  is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span> or a directory specification, PSF searches for
  a file called image.pst.? where ? is the highest existing version number.
  Pstfile is usually the output of the DAOPHOT PSTSELECT task but may also be
  the appropriately edited output psf file produced by PSF itself, or the output
  of the GROUP, NSTAR, PEAK or ALLSTAR tasks.  Photfile may be an APPHOT/DAOPHOT
  text database or an STSDAS table.
  </dd>
  </dl>
  <dl id="l_psfimage">
  <dt><b>psfimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='psfimage' Line='psfimage' -->
  <dd>The output PSF model image names or directory. The must be one PSF image name
  for every input image. If psfimage is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory
  specification, then PSF creates an image called image.psf.? where ? is the next
  available version number.
  </dd>
  </dl>
  <dl id="l_opstfile">
  <dt><b>opstfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='opstfile' Line='opstfile' -->
  <dd>The output psf star files containing lists of the stars actually used to
  compute the PSF model. There must be one output psf star file for every input
  image. If opstfile is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory specification
  then PSF creates a file called image.pst.? where ? is the next available
  version number. If the DAOPHOT package parameter <i>text</i> is <span style="font-family: monospace;">"yes"</span> then an
  APPHOT/DAOPHOT text database is written, otherwise an STSDAS binary table is
  written.
  </dd>
  </dl>
  <dl id="l_groupfile">
  <dt><b>groupfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='groupfile' Line='groupfile' -->
  <dd>The output psf star group files listing the PSF stars and their neighbors that
  were used to create the PSF models. There must be one output group file for
  every input image. If groupfile is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or a directory
  specification then PSF creates a file called image.psg.? where ? is the
  next available version number. If the DAOPHOT package parameter <i>text</i> is
  <span style="font-family: monospace;">"yes"</span> then an APPHOT/DAOPHOT text database is written, otherwise an STSDAS
  table database is written.
  </dd>
  </dl>
  <dl id="l_plotfile">
  <dt><b>plotfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotfile' Line='plotfile = ""' -->
  <dd>The name of the output file containing mesh, contour, or profile plots of the
  selected PSF stars. If plotfile is undefined no plot file is created,
  otherwise a mesh, contour, or profile plot is written to this file for each PSF
  star selected. Plotfile is opened in append mode and may become very large.
  </dd>
  </dl>
  <dl id="l_datapars">
  <dt><b>datapars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datapars' Line='datapars = ""' -->
  <dd>The name of the file containing the data dependent parameters. The parameters
  <i>scale</i>, <i>datamin</i>, and <i>datamax</i> are located here. If datapars
  is undefined then the default parameter set in uparm directory is used.
  </dd>
  </dl>
  <dl id="l_daopars">
  <dt><b>daopars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='daopars' Line='daopars = ""' -->
  <dd>The name of the file containing the daophot fitting parameters. The parameters
  <i>psfrad</i> and <i>fitrad</i> are located here. If <i>daopars</i> is undefined
  then the default parameter set in uparm directory is used.
  </dd>
  </dl>
  <dl id="l_matchbyid">
  <dt><b>matchbyid = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='matchbyid' Line='matchbyid = yes' -->
  <dd>Match the stars in the psf star list(s) if any to the stars in the input
  photometry files using id numbers (matchbyid = yes) or x and y positions
  (matchbyid = no).
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Fit the PSF interactively ? If interactive = yes and <i>icommands</i> is
  undefined, PSF reads selects the initial list of PSF stars from <i>pstfile</i>
  and waits for commands from the user. If interactive = no and <i>icommands</i>
  is undefined, PSF reads in the candidate PSF stars from <i>pstfile</i>, computes
   the PSF, and writes it to <i>psfimage</i> without input from the user. If
  <i>icommands</i> is defined, then interactive = no, and commands are read from
  the image cursor command file.
  </dd>
  </dl>
  <dl id="l_mkstars">
  <dt><b>mkstars = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mkstars' Line='mkstars = no' -->
  <dd>Mark the selected or deleted psf stars on the image display ?
  </dd>
  </dl>
  <dl id="l_showplots">
  <dt><b>showplots = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='showplots' Line='showplots = yes' -->
  <dd>Show plots of the selected PSF stars? After each star is selected
  interactively by the user, a mesh, contour, or profile plot of the data
  subraster around the candidate star is displayed. At this point the user
  can accept or reject the star. In interactive mode the user can set showplots
  to <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"no"</span>.  In non-interactive mode showplots is always <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_plottype">
  <dt><b>plottype = <span style="font-family: monospace;">"mesh"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plottype' Line='plottype = "mesh"' -->
  <dd>The default type of plot displayed when selecting PSF stars. The choices
  are <span style="font-family: monospace;">"mesh"</span>, <span style="font-family: monospace;">"contour"</span>, or <span style="font-family: monospace;">"radial"</span>.
  </dd>
  </dl>
  <dl id="l_icommands">
  <dt><b>icommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='icommands' Line='icommands = ""' -->
  <dd>The image display cursor or the name of the image cursor command file.
  </dd>
  </dl>
  <dl id="l_gcommands">
  <dt><b>gcommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gcommands' Line='gcommands = ""' -->
  <dd>The graphics cursor or the name of the graphics cursor command file.
  </dd>
  </dl>
  <dl id="l_wcsin">
  <dt><b>wcsin = <span style="font-family: monospace;">")_.wcsin"</span>, wcsout = <span style="font-family: monospace;">")_.wcsout"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcsin' Line='wcsin = ")_.wcsin", wcsout = ")_.wcsout"' -->
  <dd>The coordinate system of the input coordinates read from <i>photfile</i> and
  <i>pstfile</i>, and of the output coordinates written to <i>psfimage</i>,
  <i>opstfile</i>, <i>groupfile</i> respectively. The image header coordinate
  system is used to transform from the input coordinate system to the <span style="font-family: monospace;">"logical"</span>
  pixel coordinate system used internally, and from the internal <span style="font-family: monospace;">"logical"</span> pixel
  coordinate system to the output coordinate system. The input coordinate system
  options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, <span style="font-family: monospace;">"physical"</span>, and <span style="font-family: monospace;">"world"</span>. The output coordinate
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
  package parameter (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>. By default caching is
  disabled.
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = <span style="font-family: monospace;">")_.verify"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = ")_.verify"' -->
  <dd>Verify the critical PSF task parameters? Verify can be set to the DAOPHOT
  package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = <span style="font-family: monospace;">")_.update"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = ")_.update"' -->
  <dd>Update the PSF task parameters if <i>verify</i> is <span style="font-family: monospace;">"yes"</span>? Update can be
  set to the default daophot package parameter value, <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = <span style="font-family: monospace;">")_.verbose"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = ")_.verbose"' -->
  <dd>Print messages about the progress of the task ? Verbose can be set to the
  DAOPHOT package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">")_.graphics"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = ")_.graphics"' -->
  <dd>The default graphics device. Graphics can be set to the default DAOPHOT package
  parameter value, <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_display">
  <dt><b>display = <span style="font-family: monospace;">")_.display"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='display' Line='display = ")_.display"' -->
  <dd>The  default  image  display  device.  Display can be set to the DAOPHOT
  package parameter value (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>. By default graphics
  overlay is disabled.  Setting display to one of <span style="font-family: monospace;">"imdr"</span>, <span style="font-family: monospace;">"imdg"</span>, <span style="font-family: monospace;">"imdb"</span>, or
  <span style="font-family: monospace;">"imdy"</span> enables graphics overlay with the IMD graphics kernel. 
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The PSF task builds the point spread function for the IRAF image <i>image</i>
  using stars selected, from the input photometry file <i>photfile</i> with the
  image cursor, and/or by their ids stored in the psf star file <i>pstfile</i>,
  and writes the PSF model out to the IRAF image <i>psfimage</i>, the final
  PSF star list to <i>opstfile</i>, and group membership information for the
  selected PSF stars to <i>groupfile</i>. If the DAOPHOT package parameter
  <i>text</i> is <span style="font-family: monospace;">"yes"</span>, then <i>groupfile</i> is an APPHOT/DAOPHOT text database,
  otherwise it is an STSDAS binary table.
  </p>
  <p>
  The coordinates read from <i>photfile</i> and <i>pstfile</i> are assumed to be
  in coordinate system defined by <i>wcsin</i>. The options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>,
  <span style="font-family: monospace;">"physical"</span>, and <span style="font-family: monospace;">"world"</span> and the transformation from the input coordinate
  system to the internal <span style="font-family: monospace;">"logical"</span> system is defined by the image coordinate
  system. The simplest default is the <span style="font-family: monospace;">"logical"</span> pixel system. Users working on
  with image sections but importing pixel coordinate lists generated from the
  parent image must use the <span style="font-family: monospace;">"tv"</span> or <span style="font-family: monospace;">"physical"</span> input coordinate systems.
  </p>
  <p>
  The coordinates written to <i>psfimage</i>, <i>pstfile</i> and <i>groupfile</i>
  are in the coordinate system defined by <i>wcsout</i> with the exception
  of the psf model center coordinates PSFX and PSFY which are always in the
  logical system of the input image. The options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, and
  <span style="font-family: monospace;">"physical"</span>. The simplest default is the <span style="font-family: monospace;">"logical"</span> system.  Users wishing to
  correlate the output coordinates of objects measured in image sections or
  mosaic pieces with coordinates in the parent image must use the <span style="font-family: monospace;">"tv"</span>
  or <span style="font-family: monospace;">"physical"</span> coordinate systems.
  </p>
  <p>
  Suitable PSF stars are normally selected interactively using the image display
  and image cursor and matched with the stars in <i>photfile</i> using the cursor
  position and a tolerance specified by the <i>matchrad</i> parameter in the
  DAOPARS task. A star must be in the photometry file before it can be used as
  a PSF star. If a match is found, PSF checks that the candidate star is not too
  close to the edge of the image and that it contains no bad pixels as defined
  by <i>datamin</i> and <i>datamax</i> in the DATAPARS task. After selection a
  mesh, contour, or profile plot of the data subraster around the candidate star
  is displayed in the graphics window, PSF enters graphics cursor command mode
  and the user is given the option to accept or reject the star.  If the user
  accepts the star it is added to the PSF star list.  Commands in the graphics
  cursor menu permit the user to manipulate the floor and ceiling levels of the
  contour plot and the viewing angles for the mesh plot interactively.
  </p>
  <p>
  Users who know which stars they wish to use as PSF stars ahead of time or
  who are without access to an image display can also select PSF stars by id
  number, after which mesh, contour, or radial profile plots will be displayed in
  the graphics window in the usual way.
  </p>
  <p>
  If the user does not wish to see any plots of the PSF stars or interact with
  the fitting process, the image cursor may be redirected to a text
  file containing cursor commands <i>icommands</i> which specify the PSF stars
  to be used in the fit. If <i>plotfile</i> is defined contour, mesh, or profile
  plots of the selected psf stars can be saved in a metacode plot file for later
  examination.
  </p>
  <p>
  In interactive mode the PSF star may be initialized by setting <i>pstfile</i>
  to a file created by the PSTSELECT task. If <i>showplot</i> = <span style="font-family: monospace;">"yes"</span> the user is
  asked to accept or delete each star in the input psf star list.  Other stars
  may also be added or deleted from this list at any time with the image cursor.
  If <i>interactive</i>=no or <i>icommands</i> is defined, the PSF stars are read
  in from <i>pstfile</i>, and the PSF model is computed and saved without
  input from the user.
  </p>
  <p>
  If <i>cache</i> is yes and the host machine physical memory and working set size
  are large enough, the input image pixels are cached in memory. If caching
  is enabled and PSF is run interactively the first data access will appear
  to take a long time as the entire image must be read in before the data
  is actually read. All subsequent measurements will be very fast because PSF
  is accessing memory not disk. The point of caching is to speed up random
  image access by making the internal image i/o buffers the same size as the
  image itself. However if the input object lists are sorted in row order and
  sparse caching may actually worsen not improve the execution time. Also at
  present there is no point in enabling caching for images that are less than
  or equal to 524288 bytes, i.e. the size of the test image dev$ypix, as the
  default image i/o buffer is exactly that size. However if the size of dev$ypix
  is doubled by converting it to a real image with the chpixtype task then the
  effect of caching in interactive is can be quite noticeable if measurements
  of objects in the top and bottom halves of the image are alternated.
  </p>
  <p>
  The output PSF image <i>psfimage</i>  is normally a 2D  image containing the
  image header parameters, <span style="font-family: monospace;">"XPSF"</span>, <span style="font-family: monospace;">"YPSF"</span>, <span style="font-family: monospace;">"PSFMAG"</span> and <span style="font-family: monospace;">"PSFRAD"</span> which define the
  centroid, magnitude and size of the PSF model, the parameters <span style="font-family: monospace;">"FUNCTION"</span>,
  <span style="font-family: monospace;">"PSFHEIGH"</span>, <span style="font-family: monospace;">"NPARS"</span>, and <span style="font-family: monospace;">"PAR#"</span> which define the analytic component of the PSF,
  and a single look-up table of residuals from the analytic fit subsampled by a
  factor of 2 with respect to the parent image.
  </p>
  <p>
  If the DAOPARS parameter <i>varorder</i> = -1, the PSF is fit by the analytic
  function and <i>psfimage</i> has no pixel file.
  </p>
  <p>
  If the DAOPARS parameter <i>varorder</i> = 1 or 2, then two or five additional
  lookup tables are computed and <i>psfimage</i> is a 3D image with 3 or 6 planes
  respectively. The first two additional look-up tables contain the first
  derivatives of the PSF wrt the x and y positions in the image (varorder = 1),
  and the next three contains the second derivatives with respect to x ** 2, xy,
  and y ** 2 (varorder = 2).
  </p>
  <p>
  The positions and magnitudes of each of the stars contributing to the PSF model
  are also stored in the PSF image header.
  </p>
  <p>
  <i>Groupfile</i> contains a list of the PSF stars, their nearest neighbors, and
  friends of the neighbors. A neighbor is defined to be any star within a
  distance of 1.5 * <i>psfrad</i> / <i>scale</i> + 2.0 * <i>fitrad</i> /
  <i>scale</i> + 1 pixels of the PSF star. Friends of the neighbors are defined
  to be any stars within 2.0 * <i>fitrad</i> / <i>scale</i> + 1.0 of a neighbor
  star. <i>Fitrad</i> and <i>psfrad</i> are respectively the fitting radius and psf
  radius parameters in the DAOPARS task. <i>Scale</i> is the scale factor defined
  in the DATAPARS task.
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  The following cursor commands are available once the image cursor has
  been activated.
  </p>
  <div class="highlight-default-notranslate"><pre>
          Keystroke Commands
  
  ?       Print help
  p       Print photometry for star nearest the cursor
  l       List the current psf stars
  a       Add star nearest cursor to psf star list
  f       Fit the psf
  r       Review the fit for all the psf stars
  s       Subtract fitted psf from psf star nearest cursor
  d       Delete psf star nearest cursor from psf star list
  w       Write the psf to the psf image
  z       Rebuild the psf from scratch
  q       Quit task
  
          Colon Commands
  
  :p [n]  Print photometry for star n
  :a [n]  Add star n to psf star list
  :d [n]  Delete star n from psf star list
  :s [n]  Subtract fitted psf from psf star n
  
          Colon Parameter Editing Commands
  
  # Data dependent parameters which affect the psf computation
  
  :scale     [value]      Show/set the image scale (units / pixel)
  :fwhmpsf   [value]      Show/set the fwhm of psf (scale units)
  :datamin   [value]      Show/set the minimum good data value (counts)
  :datamax   [value]      Show/set the maximum good data value (counts)
  :matchrad  [value]      Show/set matching radius (scale units)
  
  # Psf computation parameters
  
  :psfimage   [name,name] Show/set the psf image and groupfile
  :function   [string]    Show/set the analytic psf function
  :varorder   [integer]   Show/set order of psf function variability
  :nclean     [integer]   Show/set number of cleaning iterations
  :saturated  [y/n]       Show/set the use saturated star flag
  :psfrad     [value]     Show/set the psf radius (scale units)
  :fitrad     [value]     Show/set the fitting radius (scale units)
  
  The following cursor commands are available once a star has been selected
  and the graphics cursor has been activated.
  
          Interactive Graphics Keystroke Commands
  
  ?       Print help
  p       Print the photometry for this star
  t       Print the plot parameters and data minimum and maximum
  a       Accept star and proceed
  d       Reject star and select another with image cursor
  m       Plot the default mesh plot for this star
  n       Increase vertical angle by 15 degrees (mesh plot only)
  s       Decrease vertical angle by 15 degrees (mesh plot only)
  w       Decrease horizontal angle by 15 degrees (mesh plot only)
  e       Increase horizontal angle by 15 degrees (mesh plot only)
  c       Plot the default contour plot for this star
  r       Plot the radial profile for this star
  
          Colon Graphics Commands
  
  :m [val] [val]  Set the mesh plot vertical and horizontal viewing angles
  :v [val]        Set the mesh plot vertical viewing angle
  :h [val]        Set the mesh plot horizontal viewing angle
  :c [val] [val]  Set the contour plot floor and ceiling levels
  :l [value]      Set the contour plot floor level
  :u [value]      Set the contour plot ceiling level
  </pre></div>
  </section>
  <section id="s_algorithms">
  <h3>Algorithms</h3>
  <p>
  The PSF is determined from the actual observed brightness values as a function
  of x and y 
  for one or more stars in the frame and stored as a two-component model.
  The first component is an analytic function which approximates
  the light distribution in the cores of the PSF stars. There are
  currently 6 choices for the analytic component of the model:
  <span style="font-family: monospace;">"gauss"</span>, <span style="font-family: monospace;">"moffat15"</span>, <span style="font-family: monospace;">"moffat25"</span>, <span style="font-family: monospace;">"lorentz"</span>, <span style="font-family: monospace;">"penny1"</span>, and <span style="font-family: monospace;">"penny2"</span>.
  The parameters of the analytic component of the psf model are stored
  in the psf image header parameters <span style="font-family: monospace;">"FUNCTION"</span>, <span style="font-family: monospace;">"PSFHEIGH"</span>, <span style="font-family: monospace;">"NPARS"</span>,
  and <span style="font-family: monospace;">"PARN"</span>. The magnitude, size, and centroid of the PSF are stored
  in the image header parameters <span style="font-family: monospace;">"PSFMAG"</span>, <span style="font-family: monospace;">"PSFRAD"</span>, 
  <span style="font-family: monospace;">"XPSF"</span>, and <span style="font-family: monospace;">"YPSF"</span>. If <i>matchbyid</i> is <span style="font-family: monospace;">"no"</span> or there is no input psf star list <span style="font-family: monospace;">"PSFMAG"</span> is
  set to the magnitude of the first PSF star in the input photometry file. If <i>matchbyid</i>
  is <span style="font-family: monospace;">"yes"</span>, and there is an input psf star list <span style="font-family: monospace;">"PSFMAG"</span> is set to the magnitude of the first psf star
  in the psf star list. <span style="font-family: monospace;">"XPSF"</span> and <span style="font-family: monospace;">"YPSF"</span> are the center of the image.
  If <i>varorder</i> &gt;= 0,
  the residuals from this fit are stored as a lookup
  table with twice the sampling interval of the original image.
  This lookup table is used as additive corrections from the integrated
  analytic function to actual observed empirical PSF.
  The parameters of the analytic function are computed by fitting
  all the stars weighted by their signal-to-noise.
  so that the signal-to-noise ratio in
  the PSF does not deteriorate as fainter stars are added in. The more
  crowded the field the more PSF stars are required to lower the noise
  generated by neighbor subtraction.
  </p>
  <p>
  If the <i>varorder</i> parameter in the DAOPARS task is set to 1 or 2, two
  or five additional lookup
  tables containing the first derivatives of the PSF in x and y 
  and the second order derivatives of the image with respect to
  x ** 2, x * y, and y ** 2 are also written.
  This model
  permits the PSF fitting process to take account of smooth linear
  or quadratic changes in the PSF across the frame caused for example by a tilt in
  the detector with respect to the optical axis or low order optical
  aberrations.
  Users of this option should ensure that the PSF varies in a systematic
  way across the frame and that the chosen PSF stars span the entire
  region of interest in the frame. To avoid mistaking
  neighbor stars for variations in the PSF it is recommended that the
  first few iterations of PSF be run with a constant PSF. Only after
  neighbor stars have been subtracted reasonably cleanly should
  the variable PSF option be enabled.
  </p>
  <p>
  The brightness of any hypothetical pixel at any arbitrary point within
  the PSF is computed as follows. The analytic function 
  is integrated over the area of the pixel, a correction is determined
  by bicubic interpolation within the lookup table and added to the
  integral. Since the values in the table of residuals differ by smaller
  amounts between adjacent grid points than the original brightness data
  would have, the errors in the interpolation are much less than they would
  have been if one  had tried to interpolate directly within the original
  data.
  </p>
  </section>
  <section id="s_guide_to_computing_a_psf_in_a_crowded_field">
  <h3>Guide to computing a psf in a crowded field</h3>
  <p>
  The following is a rough guide to the methodology of computing the
  PSF in a crowded field. The procedure outlined below assumes
  that the user can either make use of the IRAF display facilities or
  has access to a local display program. At a minimum the display program
  should be able to display an image, read back the coordinates of objects in the
  image, and mark objects in the image.
  </p>
  <p>
  The crowded field PSF fitting procedure makes use of many of the
  DAOPHOT tasks. Details on the setup and operation of each task can be found
  in the appropriate manual pages.
  </p>
  <dl>
  <dt><b>[1]</b></dt>
  <!-- Sec='GUIDE TO COMPUTING A PSF IN A CROWDED FIELD' Level=0 Label='' Line='[1]' -->
  <dd>RUN THE DAOFIND and PHOT TASKS ON THE IMAGE OF INTEREST.
  </dd>
  </dl>
  <dl>
  <dt><b>[2]</b></dt>
  <!-- Sec='GUIDE TO COMPUTING A PSF IN A CROWDED FIELD' Level=0 Label='' Line='[2]' -->
  <dd>EXAMINE THE IMAGE. Load the image on the display with the IRAF display task.
  Using the display itself, the DAOEDIT task, or the IRAF IMEXAMINE task, estimate the radius
  at which
  the stellar light distribution disappears into the noise for the
  brightest candidate PSF star. Call this parameter <i>psfrad</i> and record it.
  Mark the objects detected by DAOFIND with dots on the image display using the
  IRAF TVMARK
  task. Users at sites with display devices not currently supported by
  IRAF should substitute their local versions of DISPLAY and TVMARK.
  </dd>
  </dl>
  <dl>
  <dt><b>[3]</b></dt>
  <!-- Sec='GUIDE TO COMPUTING A PSF IN A CROWDED FIELD' Level=0 Label='' Line='[3]' -->
  <dd>SELECT CANDIDATE PSF STARS.
  Good PSF stars should have no neighbors
  within the fitting radius stored in the DAOPARS task parameter <i>fitrad</i>.
  In addition all stars within 1.5 times the psf radius,
  (stored in the DAOPARS task parameter
  <i>psfrad</i>), should be significantly fainter than the candidate star.
  There should be no bad columns, bad rows or blemishes
  near the candidate star. A sufficient number of stars should be
  selected in order to reduce the increased noise resulting from the
  neighbor subtraction process. Users of the variable PSF option should
  take care that the list of PSF stars span the area of interest on the
  image. Twenty-five to thirty stars is not unreasonable in this case.
  The task PSTSELECT can be used to preselect candidate PSF stars.
  These candidate PSF stars can be marked on the image display using the
  PDUMP, and TVMARK tasks. Be sure to mark the PSF stars in another
  color from the stars found by DAOFIND. Stars can be added to or
  subtracted from this list interactively when PSF is run.
  </dd>
  </dl>
  <dl>
  <dt><b>[4]</b></dt>
  <!-- Sec='GUIDE TO COMPUTING A PSF IN A CROWDED FIELD' Level=0 Label='' Line='[4]' -->
  <dd>EXAMINE THE PSF STARS FOR NEIGHBORS MISSED BY DAOFIND AND ADD THESE TO
  THE PHOT FILE.
  Examine the vicinity of the PSF stars on the display checking for neighbor
  stars which do not have dots on them indicating that they were
  missed by DAOFIND.
  If IRAF supports the local display device simply run PHOT interactively
  selecting the missing stars with the image cursor.
  Be sure to use the same set of PHOT parameters used in step [1] with
  the exception of the CENTERPARS
  task parameter <i>calgorithm</i> which should be temporarily set to <span style="font-family: monospace;">"centroid"</span>.
  If IRAF does not support the
  local display generate a list of the approximate coordinates of the
  missing stars.
  Run PHOT in batch mode with this coordinate list as input and with the
  parameters set as described above.
  Create a new PHOT file by using PCONCAT to add the new PHOT output to the
  PHOT output from [1] and renumber using PRENUMBER. Do not resort.
  </dd>
  </dl>
  <dl>
  <dt><b>[5]</b></dt>
  <!-- Sec='GUIDE TO COMPUTING A PSF IN A CROWDED FIELD' Level=0 Label='' Line='[5]' -->
  <dd>ESTIMATE OF THE PSF.
  Run PSF using the combined PHOT output from [4] and
  the list of candidate stars from [3].
  Write out the PSF image (extension .psf.#) and the psf group file
  (extension .psg.#). The PSF image is the current estimate of the PSF.
  </dd>
  </dl>
  <dl>
  <dt><b>[6]</b></dt>
  <!-- Sec='GUIDE TO COMPUTING A PSF IN A CROWDED FIELD' Level=0 Label='' Line='[6]' -->
  <dd>FIT ALL THE STARS IN EACH PSF STAR GROUP IN THE ORIGINAL IMAGE.
  Run NSTAR on the image using the output group file (extension .psg.#)
  of [5] as the input photometry list. To help prevent the bumps in the initial
  PSF from interfering with the profile fits in NSTAR, it may
  be necessary to temporarily set the psf radius,
  <i>psfrad</i> in the DAOPARS task,
  to about one pixel greater than the separation of the nearest neighbor
  to a PSF star.
  The fitting radius, <i>fitrad</i> in the
  DAOPARS task, should be sufficiently large to include enough
  pixels for a good fit but not so large as to include any neighbors
  inside the fitting radius.
  </dd>
  </dl>
  <dl>
  <dt><b>[7]</b></dt>
  <!-- Sec='GUIDE TO COMPUTING A PSF IN A CROWDED FIELD' Level=0 Label='' Line='[7]' -->
  <dd>SUBTRACT ALL THE FITTED STARS FROM THE ORIGINAL IMAGE.
  Run SUBSTAR to subtract the NSTAR results from the original image.
  Use the IRAF DISPLAY task or the local display program to display
  the subtracted image. If you decreased the value of <i>psfrad</i>
  in [6] use this smaller value when you subtract as well.
  </dd>
  </dl>
  <dl>
  <dt><b>[8]</b></dt>
  <!-- Sec='GUIDE TO COMPUTING A PSF IN A CROWDED FIELD' Level=0 Label='' Line='[8]' -->
  <dd>CHECK FOR PREVIOUSLY INVISIBLE FAINT COMPANIONS.
  Check to see whether the PSF stars and neighbors subtracted
  cleanly or whether there are faint companions that were not previously
  visible before.
  </dd>
  </dl>
  <dl>
  <dt><b>[9]</b></dt>
  <!-- Sec='GUIDE TO COMPUTING A PSF IN A CROWDED FIELD' Level=0 Label='' Line='[9]' -->
  <dd>APPEND THESE COMPANIONS TO THE PHOT FILE.
  Run PHOT on the faint companions in the subtracted image
  and append the results to the PHOT file created in [4] using PCONCAT.
  Renumber the stars using PRENUMBER.
  </dd>
  </dl>
  <dl>
  <dt><b>[10]</b></dt>
  <!-- Sec='GUIDE TO COMPUTING A PSF IN A CROWDED FIELD' Level=0 Label='' Line='[10]' -->
  <dd>SUBTRACT ALL THE PSF NEIGHBOR STARS FROM THE ORIGINAL IMAGE.
  Edit the nstar output file (extension .nst.#) removing all the PSF stars
  from the file. The PSF stars is the first one in each group. In the
  near future this will be done with the PEXAMINE task but at the
  moment the text editor can be used for text databases and the TTOOLS
  package task TEDIT can be used for tables. PSELECT can also be used
  to remove stars with specific id numbers. Run SUBSTAR using the edited
  nstar output file as input.
  </dd>
  </dl>
  <dl>
  <dt><b>[11]</b></dt>
  <!-- Sec='GUIDE TO COMPUTING A PSF IN A CROWDED FIELD' Level=0 Label='' Line='[11]' -->
  <dd>RECOMPUTE THE PSF.
  Run PSF on the subtracted image from [10] using the PHOT file from [9]
  as the input stellar photometry file.
  Temporarily set the minimum good data value, the <i>datamin</i> parameter
  in the DATAPARS task to a large negative number, to avoid the
  enhanced noise where the
  stars were subtracted from triggering the bad pixel detector in PSF.
  A new psf (extension .psf.#) and new psf group file (extension .psg.#)
  will be created. Be sure to increase the <i>psfrad</i> value to the
  original large value found in [2].
  </dd>
  </dl>
  <dl>
  <dt><b>[12]</b></dt>
  <!-- Sec='GUIDE TO COMPUTING A PSF IN A CROWDED FIELD' Level=0 Label='' Line='[12]' -->
  <dd>RERUN NSTAR.
  Rerun NSTAR on the original image with the newly created group file
  (extension .psg.#) as the input stellar photometry file and the newly
  computed PSF image (extension .psf.#).
  It should not be necessary to reduce the psf radius as in [6]
  but the fitting radius should be left at a generous number.
  </dd>
  </dl>
  <dl>
  <dt><b>[13]</b></dt>
  <!-- Sec='GUIDE TO COMPUTING A PSF IN A CROWDED FIELD' Level=0 Label='' Line='[13]' -->
  <dd>REPEAT STEPS [7-12] UNTIL THE PSF FIT IS ACCEPTABLE.
  If any neighbors are still visible iterate on this process by repeating
  steps [7] to [12] until the neighbors completely disappear. The main
  point to remember is that each time through the loop the PSF is obtained
  from an image in which the neighbors but not the PSF stars have been 
  subtracted out while NSTAR and SUBSTAR should be run on the original
  picture with all the stars still in it.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the PSF for the image dev$ypix. Select stars using the display and
  the image cursor and show plots of the data and the residuals from the fit
  for each star. Good stars for making the PSF model can be found at (442,410),
  (348,189), and (379,67).
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; daofind dev$ypix default fwhmpsf=2.5 sigma=5.0 threshold=20.0
  
      ... answer verify prompts
  
      ... find stars in the image
  
      ... answer will appear in ypix.coo.1
  
  da&gt; phot dev$ypix default default annulus=10. dannulus=5.       \
      apertures = 5.0
  
      ... answer verify prompts
  
      ... do aperture photometry on the detected stars
  
      ... answer will appear in ypix.mag.1
  
  da&gt; display dev$ypix 1
  
      ... display the image
  
  da&gt; psf dev$ypix default "" default default default psfrad=9.0 \
      fitrad=3.0 mkstars=yes display=imdr
  
      ... verify the critical parameters
  
      ... move the image cursor to a candidate star and hit the a key,
          a plot of the stellar data appears
  
      ... type ? for a listing of the graphics cursor menu
  
      ... type a to accept the star, d to reject it
  
      ... move to the next candidate stars and repeat the previous
          steps
  
      ... type l to list all the psf stars
  
      ... type f to fit the psf
  
      ... move cursor to first psf star and type s to see residuals,
          repeat for all the psf stars
  
      ... type w to save the PSF model
  
      ... type q to quit, and q again to confirm
  
      ... the output will appear in ypix.psf.1.imh, ypix.pst.1 and
          ypix.psg.1
  </pre></div>
  <p>
  2. Run PSF non-interactively using the photometry file and psf star file
  created in the previous example.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; psf dev$ypix default default default default default \
      psfrad=9.0 fitrad=3.0 interactive- plotfile=psf.plots
  
  ... the output will appear in ypix.psf.2, ypix.psg.2, and
      ypix.pst.2
  
  da&gt; gkidir psf.plots
  
  ... list the plots created by psf
  
  da&gt; gkiextract psf.plots 1 | stdgraph
  
  ... display the surface plots of the first psf star
  
  da&gt; seepsf ypix.psf.2 ypixpsf
  
  ... convert the sampled PSF look-up table to a PSF image
  </pre></div>
  <p>
  3. Setup and run PSF interactively without using the image display cursor.
  Use the photometry file created in example 1. Before running PSF in this
  manner the user should have a list of the candidate PSF star ids.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; show stdimcur
  
  ... store the default value
  
  da&gt; set stdimcur = text
  
  ... define the image cursor to be the standard input
  
  da&gt; epar psf
  
  ... edit the psf parameters
  
  ... move to the datapars line and type :e edit the data dependent
      parameters, type :q to quit the datapars menu
  
  ... move to the daopars line and type :e edit the daophot fitting
      parameters, type :q to quit the daopars menu
  
  ... finish editing the psf parameters
  
  da&gt; psf dev$ypix default "" default default default \
      plottype=radial
  
  ... verify critical parameters
  
  ... type :a # where # stands for the id number of the star,
      a plot of the stellar data appears
  
  ... type a to accept the star, d to reject it
  
  ... repeat for all the PSF stars
  
  ... type l to list the psf stars
  
  ... type f to fit the PSF
  
  ... type :s # where # stands for the id of the psf star, a plot
      of the model residuals appears
  
  ... type w to save the PSF
  
  ... type q to quit PSF and q again to confirm the quit
  
  ... the output will appear in ypix.psf.3, ypix.pst.3, ypix.psg.3
  
  da&gt; set stdimcur = stdimage
  
  ... reset the image cursor
  </pre></div>
  <p>
  4. Run PSF in non-interactive mode using an image cursor  command file of
  instructions called icmds.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; type icmds
      :a 106
      :a 24
      :a 16
      :a 68
      f
      w
      q
  
  da&gt; psf dev$ypix default "" default default default  \
      icommands=icmds
  
  ... verify the critical parameters
  
  ... the PSF will be constructed from stars 106, 24, 16, 68
      in the input photometry file
  
  ... the output will appear in ypix.psf.4, ypix.pst.4, ypix.psg.4
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
  datapars,daopars,pstselect,seepsf
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'ALGORITHMS' 'GUIDE TO COMPUTING A PSF IN A CROWDED FIELD' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

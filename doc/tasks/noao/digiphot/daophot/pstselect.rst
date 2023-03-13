.. _pstselect:

pstselect: Select candidate psf stars based on proximity
========================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pstselect image photfile pstfile maxnpsf
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The list of images containing the candidate psf stars.
  </dd>
  </dl>
  <dl id="l_photfile">
  <dt><b>photfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='photfile' Line='photfile' -->
  <dd>The list of input  photometry files. The number of photometry files must
  be equal to the number of input images. If photfile is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>,
  or a directory specification PSTSELECT searches for a file called 
  dir$image.mag.#  where # is the highest available version number for the file.
  Photfile is normally the output of the PHOT task but may also be the  output
  of  the  PSF,  PEAK,  NSTAR and ALLSTAR tasks. Photfile may be a
  text file or an STSDAS binary table.
  </dd>
  </dl>
  <dl id="l_pstfile">
  <dt><b>pstfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pstfile' Line='pstfile' -->
  <dd>The  list  of  output  psf star photometry files. There must be one output
  psf star photometry file for every input image. If pstfile is <span style="font-family: monospace;">"default"</span>,
  <span style="font-family: monospace;">"dir$default"</span>,  or a  directory  specification  then  PSTSELECT writes
  a file called dir$image.pst.# where # is the next  available  version  number.
  Pstfile  inherits its file type, it may be either an APPHOT/DAOPHOT
  text or STSDAS binary file, from photfile.
  </dd>
  </dl>
  <dl id="l_maxnpsf">
  <dt><b>maxnpsf = 25</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxnpsf' Line='maxnpsf = 25' -->
  <dd>The maximum number of candidate psf stars to be selected.
  </dd>
  </dl>
  <dl id="l_mkstars">
  <dt><b>mkstars = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mkstars' Line='mkstars = no' -->
  <dd>Mark the selected or deleted psf stars on the image display ?
  </dd>
  </dl>
  <dl id="l_plotfile">
  <dt><b>plotfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotfile' Line='plotfile = ""' -->
  <dd>The name of the output file containing mesh, contour, or profile plots of the
  selected PSF stars. If plotfile is undefined no plot file is created; otherwise
  a mesh, contour, or profile plot is written to this file for each PSF star
  selected. Plotfile is opened in append mode and may become very large.
  </dd>
  </dl>
  <dl id="l_datapars">
  <dt><b>datapars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datapars' Line='datapars = ""' -->
  <dd>The name of the file containing the data dependent parameters. The parameter
  <i>scale</i> is located here. If <i>datapars</i> is undefined then the default
  parameter set in uparm directory is used.
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
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Select the psf stars interactively ? If interactive = yes and icommands is
  undefined, PSTSELECT reads in the star list from <i>photfile</i>, sorts the
  stars by magnitude and waits for commands from the user. If interactive = no
  and icommands=<span style="font-family: monospace;">""</span>, PSTSELECT selects candidate PSF stars from <i>photfile</i>
  automatically. If icommands is not undefined then interactive is automatically
  set to <span style="font-family: monospace;">"no"</span>, and commands are read from the image cursor command file.
  </dd>
  </dl>
  <dl id="l_plottype">
  <dt><b>plottype = <span style="font-family: monospace;">"mesh"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plottype' Line='plottype = "mesh"' -->
  <dd>The default plot type displayed when a psf star is selected interactively.
  The choices are <span style="font-family: monospace;">"mesh"</span>, <span style="font-family: monospace;">"contour"</span>, or <span style="font-family: monospace;">"radial"</span>.
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
  <dd>The coordinate system of the input coordinates read from <i>photfile</i> and
  of the output coordinates written to <i>pstfile</i> respectively. The image
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
  <dt><b>tv  </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='tv' Line='tv  ' -->
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
  <dd>Verify the critical PSTSELECT parameters ?
  Verify can be set to the DAOPHOT package parameter value (the default),
  <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = <span style="font-family: monospace;">")_.update"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = ")_.update"' -->
  <dd>Update the algorithm parameters if verify is <span style="font-family: monospace;">"yes"</span>?
  Update can be set to the DAOPHOT package parameter value (the default),
  <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = <span style="font-family: monospace;">")_.verbose"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = ")_.verbose"' -->
  <dd>Print messages about the progress of the task in non-interactive mode ?
  Verbose can be set to the DAOPHOT package parameter value (the default),
  <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line=' ' -->
  <dd>graphics = <span style="font-family: monospace;">")_.graphics"</span>
  The default graphics device.  Graphics can be set to the default
  daophot package parameter value, <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
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
  PSTSELECT reads the input photometry file <i>photfile</i>, extracts the ID,
  XCENTER, YCENTER, MAG, and MSKY fields for up to <i>maxnpsf</i> psf stars,
  and the results to <i>pstfile</i>. <i>Pstfile</i> automatically inherits the
  file format of <i>photfile</i>.
  </p>
  <p>
  The coordinates read from <i>photfile</i> are assumed to be in coordinate
  system defined by <i>wcsin</i>. The options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, <span style="font-family: monospace;">"physical"</span>,
  and <span style="font-family: monospace;">"world"</span> and the transformation from the input coordinate system to
  the internal <span style="font-family: monospace;">"logical"</span> system is defined by the image coordinate system.
  The simplest default is the <span style="font-family: monospace;">"logical"</span> pixel system. Users working on with
  image sections but importing pixel coordinate lists generated from the parent
  image must use the <span style="font-family: monospace;">"tv"</span> or <span style="font-family: monospace;">"physical"</span> input coordinate systems.
  </p>
  <p>
  The coordinates written to <i>pstfile</i> are in the coordinate system defined
  by <i>wcsout</i>. The options are <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"tv"</span>, and <span style="font-family: monospace;">"physical"</span>. The simplest
  default is the <span style="font-family: monospace;">"logical"</span> system. Users wishing to correlate the output
  coordinates of objects measured in image sections or mosaic pieces with
  coordinates in the parent image must use the <span style="font-family: monospace;">"tv"</span> or <span style="font-family: monospace;">"physical"</span> coordinate
  systems.
  </p>
  <p>
  After reading the star list from <i>photfile</i>, PSTSELECT sorts the list in
  order of increasing magnitude, after rejecting any stars that have INDEF
  valued magnitudes, or which lie less than <i>fitrad</i> / <i>scale</i>
  pixels from the edge of the <i>image</i>. From this list the brightest
  <i>maxnpsf</i> stars which have no brighter neighbor stars within (<i>psfrad</i> +
  <i>fitrad</i>) / <i>scale</i> + 1 pixels are selected as candidate psf stars.
  <i>Psfrad</i> and <i>fitrad</i> are the psf radius and fitting radius parameters
  respectively and are stored in the DAOPARS parameter set. <i>Scale</i> is the
  image scale parameter and is located in the DATAPARS parameter set. Plots,
  either mesh, contour or radial profile depending on the value of
  <i>plottype</i>, of the selected stars may be saved in the file <i>plotfile</i>.
  </p>
  <p>
  If <i>interactive</i> = <span style="font-family: monospace;">"no"</span>, PSTSELECT reads the star list in <i>photfile</i>,
  selects the candidate psf stars as described above, and writes the results to
  <i>pstfile</i> automatically. If interactive = <span style="font-family: monospace;">"yes"</span>, PSTSELECT reads
  the star list, selects the candidate psf stars and waits for further
  instruction from the user. At this point the user can step through the stars
  chosen by PSTSELECT, check their surface, contour, or radial profile plots
  for blemishes, neighbors etc, and accept the good candidates and reject
  the poor ones, or use the image cursor and/or id number to select psf
  stars until a maximum of <i>maxnpsf</i> stars is reached. At any point in
  this process a previously selected psf star can be deleted.
  </p>
  <p>
  If <i>cache</i> is yes and the host machine physical memory and working set size
  are large enough, the input image pixels are cached in memory. If caching
  is enabled and PSTSELECT is run interactively the first data access will appear
  to take a long time as the entire image must be read in before the data
  is actually fetched. All subsequent measurements will be very fast because
  PSTSELECT is accessing memory not disk. The point of caching is to speed up
  random image access by making the internal image i/o buffers the same size as
  the image itself. However if the input object lists are sorted in row order and
  sparse caching may actually worsen not improve the execution time. Also at
  present there is no point in enabling caching for images that are less than
  or equal to 524288 bytes, i.e. the size of the test image dev$ypix, as the
  default image i/o buffer is exactly that size. However if the size of dev$ypix
  is doubled by converting it to a real image with the chpixtype task then the
  effect of caching in interactive is can be quite noticeable if measurements
  of objects in the top and bottom halves of the image are alternated.
  </p>
  </section>
  <section id="s_cursors">
  <h3>Cursors</h3>
  <p>
      The  following  cursor  commands are available once the image cursor
      has been activated.
  </p>
  <div class="highlight-default-notranslate"><pre>
          Keystroke Commands
  
  ?       Print help
  p       Print photometry for star nearest the cursor
  l       List the current psf stars
  n       Select the next good candidate psf star from the list
  a       Add star nearest cursor to psf star list
  d       Delete psf star nearest cursor from psf star list
  q       Quit task
  
          Colon Commands
  
  :p [n]  Print photometry for star n
  :a [n]  Add star n to psf star list
  :d [n]  Delete star n from psf star list
  
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
  <section id="s_output">
  <h3>Output</h3>
  <p>
  If <i>verbose</i> = <span style="font-family: monospace;">"yes"</span> a single line is written to the terminal for each
  star added to the candidate psf star list. Full output is written to the
  file <i>pstfile</i>. At the beginning of this file is a header listing the
  values of all the important parameters. For each star included in the candidate
  psf star list the following quantities are written.
  </p>
  <div class="highlight-default-notranslate"><pre>
  id  xcenter ycenter mag msky
  </pre></div>
  <p>
  Id, xcenter, ycenter, mag, and msky are the id, x and y coordinates,
  magnitudes and sky values for the candidate psf stars listed in
  <i>photfile</i>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Select up to 10 psf stars from the PHOT task output non-interactively. 
  Save surface plots of the selected stars in the file <span style="font-family: monospace;">"psf.plots"</span>.
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
  
  da&gt; pstselect dev$ypix default default 10 psfrad=9.0 fitrad=3.0 \
      plotfile=psf.plots
  
      ... answer verify prompts
  
      ... select candidate psf stars
  
      ... the output will appear in ypix.pst.1
  
  da&gt; display dev$ypix 1
  
      ... display the image
  
  da&gt; pdump ypix.pst.1 xc,yc yes | tvmark 1 STDIN col=204
  
      ... mark the stars
  
  da&gt; gkiextract psf.plots 1 | stdgraph
  
      ... make a surface plot of the first candidate psf star
  </pre></div>
  <p>
  2. Repeat the previous results for an image section while preserving the
  coordinate system of the original image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; daofind dev$ypix[150:450,150:450] default wcsout=tv fwhmpsf=2.5 \
      sigma=5.0 threshold=20.0
  
      ... answer verify prompts
  
      ... find stars in the image
  
      ... answer will appear in ypix.coo.2
  
  da&gt; phot dev$ypix[150:450,150:450] default default wcsin=tv wcsout=tv \
      annulus=10.  dannulus=5. apertures = 5.0
  
      ... answer verify prompts
  
      ... do aperture photometry on the detected stars
  
      ... answer will appear in ypix.mag.2
  
  da&gt; pstselect dev$ypix[150:450,150:450] default default 10 wcsin=tv \
      wcsout=tv psfrad=9.0 fitrad=3.0 plotfile=psf.plots2
  
      ... answer verify prompts
  
      ... select candidate psf stars
  
      ... the output will appear in ypix.pst.2
  
  da&gt; display dev$ypix[150:450,150:450] 1
  
      ... display the image
  
  da&gt; pdump ypix.pst.2 xc,yc yes | tvmark 1 STDIN col=204
  
      ... mark the stars
  
  da&gt; gkiextract psf.plots2 4 | stdgraph
  
      ... make a surface plot of the 4th candidate psf star
  </pre></div>
  <p>
  3. Repeat example 1 but run pstselect in interactive mode and do not save the
  plots.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; display dev$ypix 1
  
      ... display the image
  
  da&gt; pstselect dev$ypix ypix.mag.1 default 10 psfrad=9. fitrad=3. \
      interactive+ mkstars+ display=imdr
  
      ... verify the critical parameters as instructed
  
      ... when the image cursor appears type the n keystroke
          command to select the first suitable candidate psf
          star, examine its surface plot, and type a or d to
          accept or reject the candidate
  
      ... repeat the previous command until 10 psf stars have
          been selected, the end of the star list is reached,
          or a sufficient number of stars but fewer than maxnpsf
          have been selected
  
      ... if fewer than maxnpsf stars are found automatically
          add psf stars to the list with the a keystroke command
  
      ... type q to quit
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
  datapars,daopars,phot,psf
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSORS' 'OUTPUT' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

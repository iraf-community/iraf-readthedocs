.. _daoedit:

daoedit: Review/edit algorithm parameters interactively
=======================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  daoedit image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd></dd>
  </dl>
  <dl id="l_icommands">
  <dt><b>icommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='icommands' Line='icommands = ""' -->
  <dd>The image display cursor or image cursor commands file.
  </dd>
  </dl>
  <dl id="l_gcommands">
  <dt><b>gcommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gcommands' Line='gcommands = ""' -->
  <dd>The graphics cursor or graphics cursor commands file.
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
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">")_.graphics"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = ")_.graphics"' -->
  <dd>The standard graphics device.
  </dd>
  </dl>
  <dl id="l_display">
  <dt><b>display = <span style="font-family: monospace;">")_.display"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='display' Line='display = ")_.display"' -->
  <dd>The standard display device.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  DAOEDIT is a general purpose tool for interactively examining and editing
  the DAOPHOT algorithm parameters located in the parameter sets DATAPARS,
  FINDPARS, CENTERPARS, FITSKYPARS, PHOTPARS, and DAOPARS. These five parameter
  sets can be listed, edited, and/or unlearned as a group from within DAOEDIT
  using the IRAF LPAR, EPAR and UNLEARN utilities.  Any parameter in each of
  these five parameter sets can be examined or edited individual using a simple 
  command.  Parameters which are defined in terms of radial distance from the
  center of a star or in terms of image counts can be examined and edited
  interactively using radial profile plots and the graphics cursor.
  </p>
  <p>
  If <i>cache</i> is yes and the host machine physical memory and working set size
  are large enough, the input image pixels are cached in memory. If caching
  is enabled the first data measurement will appear to take a long time as the
  entire image must be read in before the measurement is actually made. All
  subsequent measurements will be very fast because DAOEDIT is accessing memory
  not disk.  The point of caching is to speed up random image access by making
  the internal image i/o buffers the same size as the image itself. At present
  there is no point in enabling caching for images that are less than or equal
  to 524288 bytes, i.e. the size of the test image dev$ypix, as the default image
   i/o buffer is exactly that size. However if the size of dev$ypix is doubled by
   converting it to a real image with the chpixtype task then the effect of
  caching in interactive is can be quite noticeable if measurements of objects
  in the top and bottom halves of the image are alternated.
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <div class="highlight-default-notranslate"><pre>
                        Interactive Keystroke Commands
  
  ?       Print help
  :       Colon commands
  a       Estimate center, sky, skysigma, fwhmpsf and magnitude of a star
  r       Plot the radial profile of a star and its integral
  i       Set selected parameters interactively using a radial profile plot
  g       Toggle between image and graphics cursor
  x       Toggle the radial profile plot between pixel and scale units
  y       Toggle the radial profile plot between counts and normal units
  q       Quit task
  
                        Colon Commands
  
  :lparam/eparam/unlearn  pset    List/edit/unlearn the named pset
  :parameter              [value] List or set an individual pset parameter
  
                        Psets
  
  datapars        The data dependent parameters
  findpars        The daofind task object detection parameters
  centerpars      The phot task centering algorithm parameters
  fitskypars      The phot task sky fitting algorithm parameters
  photpars        The phot task photometry algorithm parameters
  daopars         The psf fitting algorithm parameters
  
  The following commands are available from within the interactive setup
  menu.
  
              Interactive Daoedit Setup Menu
  
  ?       Print help
  spbar   Mark/verify critical parameters (f, s, a, d, r, w, b)
  q       Quit
  
  f       Mark/verify the fwhm of the psf on the radial profile plot
  s       Mark/verify the sky sigma on the radial profile plot
  l       Mark/verify the minimum good data value on the radial profile plot
  u       Mark/verify the maximum good data value on the radial profile plot
  
  c       Mark/verify the centering box half-width on the radial profile plot
  n       Mark/verify the cleaning radius on the radial profile plot
  p       Mark/verify the clipping radius on the radial profile plot
  
  a       Mark/verify the inner sky annulus radius on the radial profile plot
  d       Mark/verify the width of the sky annulus on the radial profile plot
  g       Mark/verify the sky region growing radius on the radial profile plot
  
  r       Mark/verify the photometry aperture(s) on the radial profile plot
  w       Mark/verify the psf function radius on the radial profile plot
  b       Mark/verify the psf fitting radius on the radial profile plot
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Setup the daophot package parameters interactively for the image m92.
  This example assumes that the parameters are all initially at their 
  default values.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; display dev$ypix 1
  da&gt; daoedit dev$ypix
  
      ... type :e datapars to edit the data dependent parameters
      ... leave scale at 1.0 and datamin at INDEF but set the
          datamax, readnoise, epadu, exposure, airmass, filter,
          and obstime parameters to appropriate values
      ... type :l datapars to check the results of the editing
  
      ... type :e findpars to check the object detection parameters
      ... change the findpars threshold parameter from 4.0 to 5.0
          using the command :threshold 5.0
  
      ... type i to enter the interactive setup menu
          set the fwhmpsf, sigma, inner radius of the sky annulus,
          width of the sky annulus, photometry aperture(s), psf
          radius, and fitting radius using the radial profile
          plot and graphics cursor
  
      ... select a bright non-saturated star and check that its
          radial profile is normal using the r keystroke command
      ... note the value of the standard deviation of the sky
          background written in the plot header
      ... set the datapars sigma parameter to this value using
          the command :sigma &lt;value&gt;
  
      ... check the data definition, centering, sky fitting,
          photometry, and psf fitting parameters with the commands
          :l datapars, :l centerpars, :l fitskypars, :l photpars,
          and :l daopars
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
  datapars,findpars,centerpars,fitskypars,photpars,daopars,setimpars
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

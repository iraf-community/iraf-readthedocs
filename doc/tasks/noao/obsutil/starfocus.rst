.. _starfocus:

starfocus: Determine direct focus variations from stellar images
================================================================

**Package: obsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  starfocus images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images.  The images may be either taken at a sequence
  of focus values or be multiple shifted exposures at a sequence of
  focus settings.
  </dd>
  </dl>
  <dl id="l_focus">
  <dt><b>focus = <span style="font-family: monospace;">"1x1"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='focus' Line='focus = "1x1"' -->
  <dd>If the parameter <i>fstep</i> is not set (a <span style="font-family: monospace;">""</span> null string) then this
  parameter is interpreted as either a list of focus values or an
  image header keyword to one focus value per image.  A list may be an explicit
  list of values, a range specification, or an @ file containing the values.
  If there is only a single exposure per image then the focus list gives one
  value per image while if there are multiple exposures per image the list
  applies to the multiple exposures with the same values reused for other
  images.  If the parameter <i>fstep</i> is given then this parameter is
  interpreted as a single starting focus value and the focus step
  defines the increment between subsequent single exposure images or
  for the various exposures in a multiple exposure image.
  </dd>
  </dl>
  <dl id="l_fstep">
  <dt><b>fstep = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fstep' Line='fstep = ""' -->
  <dd>A focus increment value or an image header keyword to the focus increment.
  </dd>
  </dl>
  <dl id="l_nexposures">
  <dt><b>nexposures = <span style="font-family: monospace;">"1"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nexposures' Line='nexposures = "1"' -->
  <dd>The number of exposures per image specified either as a value or as
  an image header keyword.  A double step gap in a multiple
  exposure sequence does not count as an exposure.
  </dd>
  </dl>
  <dl id="l_step">
  <dt><b>step = <span style="font-family: monospace;">"30."</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='step' Line='step = "30."' -->
  <dd>The step in pixels between exposures specified either as a value or
  as an image header keyword.
  </dd>
  </dl>
  <dl id="l_direction">
  <dt><b>direction = <span style="font-family: monospace;">"-line"</span> (-line|+line|-column|+column)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='direction' Line='direction = "-line" (-line|+line|-column|+column)' -->
  <dd>The direction of the exposure sequence in the image.  The values are
  <span style="font-family: monospace;">"-line"</span> for successive object images appearing at smaller line numbers,
  <span style="font-family: monospace;">"+line"</span> for objects appearing at larger line numbers, <span style="font-family: monospace;">"-column"</span> for
  objects appearing at smaller column numbers, and <span style="font-family: monospace;">"+column"</span> for objects
  appearing at larger column numbers.
  </dd>
  </dl>
  <dl id="l_gap">
  <dt><b>gap = <span style="font-family: monospace;">"end"</span> (none|beginning|end)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gap' Line='gap = "end" (none|beginning|end)' -->
  <dd>Location of a double step gap in a sequence with the specified direction.
  The available cases are <span style="font-family: monospace;">"none"</span> for an even sequence with no gap,
  <span style="font-family: monospace;">"beginning"</span> where a double step is taken between the first and
  the second exposure, and <span style="font-family: monospace;">"end"</span> where a double step is taken before
  the last exposure.  Note that <span style="font-family: monospace;">"beginning"</span> and <span style="font-family: monospace;">"end"</span> are defined in
  terms of the <i>direction</i> parameter.
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords = <span style="font-family: monospace;">"mark1"</span> (center|mark1|markall)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords = "mark1" (center|mark1|markall)' -->
  <dd>Method by which the coordinates of objects to be measured are specified.
  If <span style="font-family: monospace;">"center"</span> then a single object at the center of each image is measured.
  If <span style="font-family: monospace;">"mark1"</span> then the <i>imagecur</i> parameter, typically the interactive
  image display cursor, defines the coordinates of one or more objects in the
  first image ending with a <span style="font-family: monospace;">'q'</span> key value and then the same coordinates are
  automatically used in subsequent images.  If <span style="font-family: monospace;">"markall"</span> then the
  <i>imagecur</i> parameter defines the coordinates for objects in each image
  ending with a <span style="font-family: monospace;">'q'</span> key value.
  </dd>
  </dl>
  <dl id="l_wcs">
  <dt><b>wcs = <span style="font-family: monospace;">"logical"</span> (logical|physical|world)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcs' Line='wcs = "logical" (logical|physical|world)' -->
  <dd>Coordinate system for input coordinates.  When using image cursor input
  this will always be <span style="font-family: monospace;">"logical"</span>.  When using cursor input from a file this
  could be <span style="font-family: monospace;">"physical"</span> or <span style="font-family: monospace;">"world"</span>.
  </dd>
  </dl>
  <dl id="l_display">
  <dt><b>display = yes, frame = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='display' Line='display = yes, frame = 1' -->
  <dd>Display the image or images as needed?  If yes the image display is checked
  to see if the image is already in one of the display frames.  If it is not
  the <b>display</b> task is called to display the image in the frame
  specified by the <b>frame</b> parameter.  All other display parameters are
  taken from the current settings of the task.  This option requires that the
  image display be active.  A value of no is typically used when an input
  cursor file is used instead of the image display cursor.  An image display
  need not be active in that case.
  </dd>
  </dl>
  <dl id="l_level">
  <dt><b>level = 0.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='level' Line='level = 0.5' -->
  <dd>The parameter used to quantify an object image size is the radius from the
  image center enclosing the fraction of the total flux given by this
  parameter.  If the value is greater than 1 it is treated as a percentage.
  </dd>
  </dl>
  <dl id="l_size">
  <dt><b>size = <span style="font-family: monospace;">"FWHM"</span> (Radius|FWHM|GFWHM|MFWHM)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='size' Line='size = "FWHM" (Radius|FWHM|GFWHM|MFWHM)' -->
  <dd>There are four ways the PSF size may be shown in graphs and given in
  the output.  These are:
  <div class="highlight-default-notranslate"><pre>
  Radius - the radius enclosing the specified fraction of the flux
  FWHM   - a direct FWHM from the measured radial profile
  GFWHM  - the FWHM of the best fit Gaussian profile
  MFWHM  - the FWHM of the best fit Moffat profile
  </pre></div>
  The labels in the graphs and output will be the value of this parameter
  to distinguish the different types of size measurements.
  </dd>
  </dl>
  <dl id="l_beta">
  <dt><b>beta = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='beta' Line='beta = INDEF' -->
  <dd>For the Moffat profile fit (size = MFWHM) the exponent parameter may
  be fixed at a specified value or left free to be determined from the
  fit.  The exponent parameter is determined by the fit if <i>beta</i>
  task parameter is INDEF.
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = 1.' -->
  <dd>Pixel scale in user units per pixel.  Usually the value is 1 to measure
  sizes in pixels or the image pixel scale in arc seconds per pixel.
  </dd>
  </dl>
  <dl id="l_radius">
  <dt><b>radius = 5., iterations = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radius' Line='radius = 5., iterations = 2' -->
  <dd>Measurement radius in pixels and number of iterations on the radius.  The
  enclosed flux profile is measured out to this radius.  This radius may be
  adjusted if the <i>iteration</i> parameter is greater than 1.  In that case
  after each iteration a new radius is computed from the previous FWHM
  estimate to be the radius the equivalent gaussian enclosing 99.5% of the
  light.  The purpose of this is so that if the initial PSF size of the image
  need not be known.  However, the radius should then be larger than true
  image size since the iterations best converge to smaller values.
  </dd>
  </dl>
  <dl id="l_sbuffer">
  <dt><b>sbuffer = 5, swidth = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sbuffer' Line='sbuffer = 5, swidth = 5.' -->
  <dd>Sky buffer and sky width in pixels.  The buffer is added to the specified
  measurement <i>radius</i> to define the inner radius for a circular sky
  aperture.  The sky width is the width of the circular sky aperture.
  </dd>
  </dl>
  <dl id="l_saturation">
  <dt><b>saturation=INDEF, ignore_sat=no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='saturation' Line='saturation=INDEF, ignore_sat=no' -->
  <dd>Data values (prior to sky subtraction) to be considered saturated within
  measurement radius.  A value of INDEF treats all pixels as unsaturated.  If
  a measurement has saturated pixels there are two actions.  If
  <i>ignore_sat</i>=no then a warning is given but the measurement is saved
  for use.  The object will also be indicated as saturated in the output
  log.  If <i>ignore_sat</i>=yes then a warning is given and the object is
  discarded as if it was not measured.  In a focus sequence only the
  saturated objects are discarded and not the whole sequence.
  </dd>
  </dl>
  <dl id="l_xcenter">
  <dt><b>xcenter = INDEF, ycenter = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcenter' Line='xcenter = INDEF, ycenter = INDEF' -->
  <dd>The optical field center of the image given in image pixel coordinates.
  These values need not lie in the image.  If INDEF the center of the image
  is used.  These values are used to make plots of size verse distance from
  the field center for studies of radial variations.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "logfile"' -->
  <dd>File in which to record the final results.  If no log file is desired a
  null string may be specified.
  </dd>
  </dl>
  <dl id="l_imagecur">
  <dt><b>imagecur = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imagecur' Line='imagecur = ""' -->
  <dd>Image cursor input for the <span style="font-family: monospace;">"mark1"</span> and <span style="font-family: monospace;">"markall"</span> options.  If null then the
  image dispaly cursor is used interactively.  If a file name is specified
  then the coordinates come from this file.  The format of the file are lines
  of x, y, id, and key.  Values of x an y alone may be used to select objects
  and the single character <span style="font-family: monospace;">'q'</span> (or the end of the file) may be used to end
  the list.
  </dd>
  </dl>
  <dl id="l_graphcur">
  <dt><b>graphcur = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphcur' Line='graphcur = ""' -->
  <dd>Graphics cursor input.  If null then the standard graphics cursor
  is used otherwise a standard cursor format file may be specified.
  </dd>
  </dl>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  When selecting objects with the image cursor the following commands are
  available.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ?  Page cursor command summary
  g  Measure object and graph the results.
  m  Measure object.
  q  Quit object marking and go to next image.
     At the end of all images go to analysis of all measurements.
  
  :show  Show current results.
  </pre></div>
  <p>
  When in the interactive graphics the following cursor commands are available.
  All plots may not be available depending on the number of focus values and
  the number of stars.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ?  Page cursor command summary
  a  Spatial plot at a single focus
  b  Spatial plot of best focus values
  d  Delete star nearest to cursor
  e  Enclosed flux for stars at one focus and one star at all focus
  f  Size and ellipticity vs focus for all data
  i  Information about point nearest the cursor
  m  Size and ellipticity vs relative magnitude at one focus
  n  Normalize enclosed flux at x cursor position
  o  Offset enclosed flux to by adjusting background
  p  Radial profiles for stars at one focus and one star at all focus
  q  Quit
  r  Redraw
  s  Toggle magnitude symbols in spatial plots
  t  Size and ellipticity vs radius from field center at one focus
  u  Undelete all deleted points
  x  Delete nearest point, star, or focus (selected by query)
  z  Zoom to a single measurement
  &lt;space&gt; Step through different focus or stars in current plot type
  
  :beta &lt;val&gt;     Beta parameter for Moffat fit
  :level &lt;val&gt;    Level at which the size parameter is evaluated
  :overplot &lt;y|n&gt; Overplot the profiles from the narrowest profile?
  :radius &lt;val&gt;   Change profile radius
  :show &lt;file&gt;    Page all information for the current set of objects
  :size &lt;type&gt;    Size type (Radius|FWHM)
  :scale &lt;val&gt;    Pixel scale for size values
  :xcenter &lt;val&gt;  X field center for radius from field center plots
  :ycenter &lt;val&gt;  Y field center for radius from field center plots
  
  The profile radius may not exceed the initial value set by the task
  parameter.
  </pre></div>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task measures the point-spread function (PSF) width of stars or other
  unresolved objects in digital images.  The width is measured based on the
  circular radius which encloses a specified fraction of the background
  subtracted flux.  The details of this are described in the ALGORITHMS
  section.  When a sequence of images or multiple exposures in a single image
  are made with the focus varied the program provides an estimate of the best
  focus and various views of how the PSF width varies with focus and position
  in the image.  A single star may be measured at each focus or measurements
  of multiple stars may be made and combined.  The task has three stages;
  selecting objects and measuring the PSF width and other parameters, an
  interactive graphical analysis, and a final output of the results to the
  terminal and to a logfile.
  </p>
  <p>
  If a saturation value is specified then all pixels within the specified
  measurement radius are checked for saturation.  If any saturated pixels are
  found a warning is given and <i>ignore_sat</i> parameter may be used ot
  ignore the measurement.  If not ignored the object will still be indicated
  as saturated in the output log.  In a focus sequence only the saturated
  objects are discarded and not the whole sequence.
  </p>
  <p>
  The input images are specified by an image template list.  The list may
  consist of explicit image names, wildcard templates, and @ files.  A
  <span style="font-family: monospace;">"focus"</span> value or values is associated with each image; though this may be
  any numeric quantity (integer or floating point) and not just a focus.  The
  focus values may be specified in several ways.  If each image has a focus
  value recorded in the image header, the keyword name may be specified.  If
  the images consists of multiple exposures the <i>fstep</i> parameter would
  specify a second image header keyword (or constant value) giving the
  focus increment per exposure.  
  </p>
  <p>
  The focus values may also be specified as a range list
  as described in the help topic <b>ranges</b>.  This consists of
  individual values, ranges of values, a starting value and a step, and a
  range with a step.  The elements of the list are separated by commas,
  ranges are separated by hyphens, and a step is indicated by the character
  <span style="font-family: monospace;">'x'</span>.  Long range lists, such as a list of individual focus values, may be
  placed in a file and specified with the @&lt;filename&gt; convention.  The
  assignment of a focus value from a list depends on whether the images
  are single or multiple exposure as specified by the <i>nexposure</i>
  parameter.  Single exposure images are assigned focus values from the
  list in the order in which the images and focus values are given.  If
  the images are multiple exposure focus frames in which each offset exposure
  has a different focus, the focus values from the list are assigned in
  order to the multiple exposures and if there are multiple images the
  assignments are repeated.
  </p>
  <p>
  For a simple sequence of a starting focus value and focus increment,
  either for multiple single exposure images or multiple exposure
  images the <i>focus</i> and <i>fstep</i> parameters by be used
  togther as single values or image header keywords.  Note that if
  <i>fstep</i> is specified then the focus parameter is NOT interpreted
  as a list.
  </p>
  <p>
  There are two common ways of doing focus sequences.  One is to take an
  exposure at each focus value.  In this case the parameter <i>nexposure</i>
  is given the value 1.  The second is to take an image with multiple
  exposures where the objects in the image are shifted between exposures and
  the focus is changed.  In this case <i>nexposure</i> is greater than 1 and
  other parameters are used to specify the shift size and direction.  The
  <i>nexposure</i> parameter may be a number of an image header keyword.
  </p>
  <p>
  Currently the task allows only multiple exposure shifts along either the
  column or line dimension and the shifts must be the same between each
  exposure except that there may be a double shift at either end of the
  sequence.  The shift magnitude, in pixels, is specified as either a number
  or image header keyword.  The shift direction is given by the
  <i>direction</i> parameter.  It is specified relative to the image; i.e. it
  need not be the same as the physical shifts of the telescope or detector
  but depends on how the image was created.  Steps in which the object
  positions decrease in column or line are specified with a leading minus and
  those which increase with a leading plus.  The step is specified as a
  positive number of pixels between exposures.  Often a double shift is made
  at the beginning or end of the sequence.  If this is done the <i>gap</i>
  parameter is used to identify which end the gap is on.  Note that one may
  change the sense of the exposure sequence from that used to make the focus
  frame by properly adjust the direction, the gap, the focus list, and which
  object is marked as the start of the sequence.
  </p>
  <p>
  Identifying the object or objects to be measured may be accomplished in
  several ways.  If a single object near the center of the image is to be
  measured then the <i>coords</i> parameter takes the value <span style="font-family: monospace;">"center"</span>.  This
  may be used with multiple exposure focus frames if the first exposure of
  the object sequence is at the center.  When the <span style="font-family: monospace;">"center"</span> option is used
  the <i>display</i> and <i>imagecur</i> parameters are ignored.
  </p>
  <p>
  If there are multiple objects or the desired object is not at the center of
  the frame the object coordinates are entered with the <i>imagecur</i>
  parameter.  This type of coordinate input is selected by specifying either
  <span style="font-family: monospace;">"mark1"</span> or <span style="font-family: monospace;">"markall"</span> for the <i>coords</i> parameter.  If the value is
  <span style="font-family: monospace;">"mark1"</span> then the coordinates are entered for the first image and the same
  values are automatically used for subsequent images.  If <span style="font-family: monospace;">"markall"</span> is
  specified then the objects in each image are marked.
  </p>
  <p>
  Normally the <i>imagecur</i> parameter would select the interactive image
  display cursor though a standard cursor file could be used to make this
  part noninteractive.  When the image display cursor is used either the
  image must be displayed previously by the user, or the task may be allowed
  to load the image display using the <b>display</b> task by setting the
  parameter <i>display</i> to yes and <i>frame</i> to a display frame.  If yes
  the image display must be active.  The task will look at the image names as
  stored in the image display and only load the display if needed.
  </p>
  <p>
  If one wants to enter a coordinate list rather than use the interactive
  image cursor the list can consist of just the column and line coordinates
  since the key will default to <span style="font-family: monospace;">'m'</span>.  To finish the list either the end
  of file may be encountered or a single <span style="font-family: monospace;">'q'</span> may be given since the
  coordinates are irrelevant.  For the <span style="font-family: monospace;">"markall"</span> option with multiple
  images there would need to be a <span style="font-family: monospace;">'q'</span> at the end of each object except
  possibly the last.
  </p>
  <p>
  When objects are marked interactively with the image cursor there
  are a four keys which may be used as shown in the CURSOR COMMAND section.
  The important distinction is between <span style="font-family: monospace;">'m'</span> to mark and measure an
  object and <span style="font-family: monospace;">'g'</span> to mark, measure, and graph the results.  The former
  accumulates the results until the end while the latter can give an
  immediate result to be examined.  Unless only one object is marked
  the <span style="font-family: monospace;">'g'</span> key also accumulates the results for later graphical analysis.
  It is important to note that the measurements are done as each
  object is marked so there can be a significant delay before the
  next object may be marked.
  </p>
  <p>
  The quantities measured and the algorithms used are described in the
  ALGORITHMS section.  Once all the objects have been measured an
  interactive (unless only one object is measured) graphical presentation
  of the measurements is entered.
  </p>
  <p>
  When the task exits it prints the results to the terminal (STDOUT)
  and also to the <i>logfile</i> if one is specified.  The results may
  also be previewed during the execution of the task with the
  <span style="font-family: monospace;">":show"</span> command.  The results begin with a banner and the overall
  estimate of the best focus and PSF size.  If there are multiple
  stars measured at multiple focus values the best focus estimate
  for each star is printed.  The star is identified by it's position
  (the starting position for multiple exposure images).  The average
  size, relative magnitude, and best focus estimate are then given.
  If there are multiple focus values the average of the
  PSF size over all objects at each focus are listed next.
  Finally, the individual measurements are given.  The columns
  give the image name, the column and line position, the relative
  magnitude, the focus value, the PSF size as either the enclosed
  flux radius or the FWHM, the ellipticity, the position angle, and
  an indication of saturation.
  </p>
  </section>
  <section id="s_algorithms">
  <h3>Algorithms</h3>
  <p>
  The PSF of an object is characterized using a radially symmetric
  enclosed flux profile.  First the center of the object is determined from
  an initial rough coordinate.  The center is computed from marginal profiles
  which are sums of lines or columns centered at the initial coordinate and
  with a width given by the sum of the <i>radius</i>, <i>sbuffer</i>, and
  <i>swidth</i> parameters.  The mean of the marginal profile is determined
  and then the centroid of the profile above this is computed.  The centroids
  from the two marginal profiles define a new object center.  These steps of
  forming the marginal profiles centered at the estimated object position and
  then computing the centroids are repeated until the centroids converge or
  three iterations have been completed.
  </p>
  <p>
  Next a background is determined from the mode of the pixel values in the
  sky annulus defined by the object center and <i>radius</i>, <i>sbuffer</i>,
  and <i>swidth</i> parameters.  The pixel values in the annulus are sorted
  and the mode is estimated as the point of minimum slope in this sorted
  array using a width of 5% of the number of points.  If there are multiple
  regions with the same minimum slope the lowest pixel value is used.
  </p>
  <p>
  The background subtracted enclosed flux profile is determined next.
  To obtain subpixel precision and to give accurate estimates for small
  widths relative to the pixel sampling, several things are done.
  First interpolation between pixels is done using a cubic spline surface.
  The radii measured are in subpixel steps.  To accommodate small and
  large PSF widths (and <i>radius</i> parameters) the steps are nonuniform
  with very fine steps at small radii (steps of 0.05 pixels in the
  central pixel) and coarser steps at larger radii (beyond 9 pixels
  the steps are one pixel) out to the specified <i>radius</i>.  Similarly each
  pixel is subsampled finely near the center and more coarsely at larger
  distances from the object center.  Each subpixel value, as obtained by
  interpolation, is background subtracted and added into the enclosed flux
  profile.  Even with subpixel sampling there is still a point where a
  subpixel straddles a particular radius.  At those points the fraction of
  the subpixel dimension in radius falling within the radius being measured
  is used as the fraction of the pixel value accumulated.
  </p>
  <p>
  Because of errors in the background determination due to noise and
  contaminating objects it is sometimes the case that the enclosed flux
  is not completely monotonic with radius.  The enclosed flux
  normalization, and the magnitude used in plots and reported in
  results, is the maximum of the enclosed flux profile even if it
  occurs at a radius less than the maximum radius.  It is possible
  to change the normalization and subtract or add a background correction
  interactively.
  </p>
  <p>
  Because a very narrow PSF will produce significant errors in the cubic
  spline interpolation due to the steepness and rapid variation in the pixel
  values near the peak, the Gaussian profile with FWHM that encloses the same
  80% of the flux is computed as:
  </p>
  <p>
      FWHM(80%) = 2 * r(80%) * sqrt (ln(2) / (ln (1/.2)))
  </p>
  <p>
  If this is less than five pixels the Gaussian model is subtracted from the
  data.  The Gaussian normalization is chosed to perfectly subtract the
  central pixel.  The resulting subtraction will not be perfect but the
  residual data will have much lower amplitudes and variations.  A spline
  interpolation is fit to this residual data and the enclosed flux profile is
  recomputed in exactly the same manner as previously except the subpixel
  intensity is evaluated as the sum of the analytic Gaussian and the
  interpolation to the residual data.
  </p>
  <p>
  The Gaussian normalization is chosed to perfectly subtract the central
  pixel.  The resulting subtraction will not be perfect but the residual data
  will have much lower amplitudes and variations.  A spline interpolation is
  fit to this residual data and the enclosed flux profile is recomputed in
  exactly the same manner as previously except the subpixel intensity is
  evaluated as the sum of the analytic Gaussian and the interpolation to the
  residual data.  This technique yields accurate FWHM for simulated Gaussian
  PSFs down to at least a FWHM of 1 pixel.
  </p>
  <p>
  In addition to the enclosed flux profile, an estimate of the radially
  symmetric intensity profile is computed from the enclosed flux profile.
  This is based on the equation
  </p>
  <div class="highlight-default-notranslate"><pre>
  F(R) = integral from 0 to R { P(r) r dr }
  </pre></div>
  <p>
  where F(R) is the enclosed flux at radius R and P(r) is the intensity per
  unit area profile.  Thus the derivative of F(R) divided by R gives an
  estimate of P(R).
  </p>
  <p>
  Cubic spline interpolation functions are fit to the normalized enclosed
  flux profile and the intensity profile.  These are used to find the radius
  enclosing any specified fraction of the flux and to find the direct FWHM of
  the intensity profile.  These are output when <i>size</i> is <span style="font-family: monospace;">"Radius"</span> or
  <span style="font-family: monospace;">"FWHM"</span> respectively.
  </p>
  <p>
  In addition to enclosed flux radius and direct FWHM size measurements
  there are also two size measurements based on fitting analytic profiles.
  A Gaussian profile and a Moffat profile are fit to the final enclosed flux
  profile to the points with enclosed flux less than 80%.  The limit is
  included to minimize the effects of poor background values and to make the
  profile fit be representative of the core of the PSF profile.  These profiles
  are fit whether or not the selected <i>size</i> requires it.  This is done
  for simplicity and to allow quickly changing the size estimate with the
  <span style="font-family: monospace;">":size"</span> command.
  </p>
  <p>
  The intensity profile functions (with unit peak) are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  I(r) = exp (-0.5 * (r/sigma)**2)                    Gaussian
  I(r) = (1 + (r/alpha)**2)) ** (-beta)               Moffat
  </pre></div>
  <p>
  with parameters sigma, alpha, and beta.  The normalized enclosed flux
  profiles, which is what is actually fit, are then:
  </p>
  <div class="highlight-default-notranslate"><pre>
  F(r) = 1 - exp (-0.5 * (r/sigma)**2)                Gaussian
  F(r) = 1 - (1 + (r/alpha)**2)) ** (1-beta)          Moffat
  </pre></div>
  <p>
  The fits determine the parameters sigma or alpha and beta (if a
  beta value is not specified by the users).  The reported FWHM values
  are given by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  GFWHM = 2 * sigma * sqrt (2 * ln (2))               Gaussian
  MFWHM = 2 * alpha * sqrt (2 ** (1/beta) - 1)        Moffat
  </pre></div>
  <p>
  were the units are adjusted by the pixel scale factor.
  </p>
  <p>
  In addition to the four size measurements there are several additional
  quantities which are determined.  
  Other quantities which are computed are the relative magnitude,
  ellipticity, and position angle.  The magnitude of an individual
  measurement is obtained from the maximum flux attained in the enclosed
  flux profile computation.  Though the normalization and background may be
  adjusted interactively later, the magnitude is not changed from the
  initial determination.  The relative magnitude of an object is then
  computed as
  </p>
  <div class="highlight-default-notranslate"><pre>
  rel. mag. = -2.5 * log (object flux / maximum star flux)
  </pre></div>
  <p>
  The maximum star magnitude over all stars is used as the zero point for the
  relative magnitudes (hence it is possible for an individual object relative
  magnitude to be less than zero).
  </p>
  <p>
  The ellipticity and positional angle of an object are derived from the
  second central intensity weighted moments.  The moments are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  Mxx = sum { (I - B) * x * x } / sum { I - B }
  Myy = sum { (I - B) * y * y } / sum { I - B }
  Mxy = sum { (I - B) * x * y } / sum { I - B }
  </pre></div>
  <p>
  where x and y are the distances from the object center, I is
  the pixel intensity and B is the background intensity.  The sum is
  over the same subpixels used in the enclosed flux evaluation with
  intensities above an isophote which is slightly above the background.
  The ellipticity and position angles are derived from the moments
  by the equations:
  </p>
  <div class="highlight-default-notranslate"><pre>
  M1 = (Mxx - Myy) / (Mxx + Myy)
  M2 = 2 * Mxy / (Mxx + Myy)
  ellip = (M1**2 + M2**2) ** 1/2
  pa = atan (M2 / M1) / 2
  </pre></div>
  <p>
  where ** is the exponentiation operator and atan is the arc tangent
  operator.  The ellipticity is essentially (a - b) / (a + b) where a
  is a major axis scale length and b is a minor axis scale length.  A
  value of zero corresponds to a circular image.  The position angle is
  given in degrees counterclockwise from the x or column axis.
  </p>
  <p>
  The overall size when there are multiple stars is estimated by averaging
  the individual sizes weighted by the flux of the star as described above.
  Thus, when there are multiple stars, the brighter stars are given greater
  weight in the average size.  This average size is what is given in the
  banner for the graphs and in the printed output.
  </p>
  <p>
  One of the quantities computed for the graphical analysis is the
  FWHM of a Gaussian or Moffat profile that encloses the same flux
  as the measured object as a function of the level.  The equation are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  FWHM = 2 * r(level) * sqrt (ln(2.) / ln (1/(1-level)))  Gaussian
  
  FWHM = 2 * r(level) * sqrt (2**(1/beta)-1) /
         sqrt ((1-level)**(1/(1-beta))-1)                 Moffat
  </pre></div>
  <p>
  where r(level) is the radius that encloses <span style="font-family: monospace;">"level"</span> fraction of the total
  flux.  ln is the natural logarithm and sqrt is the square root.  The beta
  value is either the user specified value or the value determined by fitting
  the enclosed flux profile.
  </p>
  <p>
  This function of level will be a constant if the object profile matches
  the Gaussian or Moffat profile.  Deviations from a constant show
  the departures from the profile model.  The Moffat profile used in making
  the graphs except for the case where the <i>size</i> is GFWHM.
  </p>
  <p>
  The task estimates a value for the best focus and PSF size at that focus
  for each star.  This is done by finding the minimum size at each focus
  value (in case there are multiple measurements of the same star at the same
  focus), sorting them by focus value, finding the focus value with the
  minimum size, and parabolically interpolating using the nearest focus
  values on each side.  When the minimum size occurs at either extreme of the
  focus range the best focus is at that extreme focus; in other words there
  is no extrapolation outside the range of focus values.
  </p>
  <p>
  The overall best focus and size when there are multiple stars are estimated
  by averaging the best focus values for each star weighted by the
  average flux of the star as described above.  Thus, when there are
  multiple stars, the brighter stars are given greater weight in the
  overall best average focus and size.  This best average focus and
  size are what are given in the banner for the graphs and in the
  printed output.
  </p>
  <p>
  The log output also includes an average PSF size for all measurements
  at a single focus value.  This average is also weighted by the
  average flux of each star at that focus.
  </p>
  </section>
  <section id="s_interactive_graphics_mode">
  <h3>Interactive graphics mode</h3>
  <p>
  The graphics part of <b>starfocus</b> consists of a number of different
  plots selected by cursor keys.  The available plots depend on the
  number of stars and the number of focus values.  The various plots
  and the keys which select them are summarized below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  a  Spatial plot at a single focus
  b  Spatial plot of best focus values
  e  Enclosed flux for stars at one focus and one star at all focus
  f  Size and ellipticity vs focus for all data
  m  Size and ellipticity vs relative magnitude at one focus
  p  Radial profiles for stars at one focus and one star at all focus
  t  Size and ellipticity vs radius from field center at one focus
  z  Zoom to a single measurement
  </pre></div>
  <p>
  If there is only one object at a single focus the only available plot is
  the <span style="font-family: monospace;">'z'</span> or zoom plot.  This has three graphs; a graph of the normalized
  enclosed flux verses scaled radius, a graph of the intensity profile verses
  scaled radius, and equivalent Moffat/Gaussian full width at half maximum verses
  enclosed flux fraction.  The latter two graphs are derived from the
  normalized enclosed flux profile as described in the ALGORITHMS section.
  In the graphs the measured points are shown with symbols, a smooth curve is
  drawn through the symbols and dashed lines indicate the measurement level
  and enclosed flux radius at that level.
  </p>
  <p>
  Overplotted on these graphs are the Moffat profile fit or the
  Gaussian profile fit when <i>size</i> is GFWHM.
  </p>
  <p>
  The zoom plot is always available from any other plot.  The cursor position
  when the <span style="font-family: monospace;">'z'</span> key is typed selects a particular object measurement.
  This plot is also the one presented with the <span style="font-family: monospace;">'g'</span> key when marking objects for
  single exposure images.  In that case the graphs are drawn followed by
  a return to image cursor mode.
  </p>
  <p>
  There are three types of symbol plots showing the measured PSF size (either
  enclosed flux radius or FWHM) and ellipticity.  These plot the measurements
  verses focus (<span style="font-family: monospace;">'f'</span> key), relative magnitude (<span style="font-family: monospace;">'m'</span> key), and radius from the
  field center (<span style="font-family: monospace;">'t'</span> key).  The focus plot includes all measurements and shows
  dashed lines at the estimated best focus and size.  This plot is only
  available when there are multiple focus values.  It is the initial plot in
  this case for both the <span style="font-family: monospace;">'g'</span> key when there are multiple exposures and when
  the graphical analysis stage is entered after defining the objects.
  </p>
  <p>
  The magnitude and field radius plots are only available when there are
  multiple objects measured.  The relative magnitude used for a particular
  measurement is the average magnitude of the star over all focus values and
  not the individual object magnitude.  The data shown is for a single focus
  value.  The focus value is selected when typing <span style="font-family: monospace;">'m'</span> or <span style="font-family: monospace;">'t'</span> by the focus of
  the nearest object to the cursor in the preceding plot.  When in one of
  these plots, other focus values may be shown by typing &lt;space&gt;, the space
  bar.  This scrolls through the focus values.  The field center for the
  field radius graph may be changed interactively using the <span style="font-family: monospace;">":xcenter"</span> and
  <span style="font-family: monospace;">":ycenter"</span> commands.
  </p>
  <p>
  Grids of enclosed flux vs. radius, intensity profile vs. radius, and
  FWHM vs. enclosed flux fraction are shown with the <span style="font-family: monospace;">'e'</span>, <span style="font-family: monospace;">'p'</span>, and
  <span style="font-family: monospace;">'g'</span> keys respectively.  If there are multiple objects at multiple focus
  values there are two grids. One grid is all objects at one focus and the
  other is one object at all focuses.  The titles identify the object (by
  location) and focus.  The profiles in the grids have no axis labels or
  ticks.  Within each box are the coordinates of the object or the focus
  value, and the PSF size are given.  When there is only one object at
  multiple focus values or multiple objects at only one focus value then
  there is only one grid and a graph of a one object.  The single object
  graph does have axis labels and  ticks.
  </p>
  <p>
  In the grids there is one profile which is highlighted (by a second
  box or by a color border).  The highlighted profile is the current
  object.  To change the current object, and thus change either
  the contents of the other grid or the single object graphed, one
  can type the space bar to advance to the next object or
  use the cursor and the <span style="font-family: monospace;">'e'</span>, <span style="font-family: monospace;">'p'</span>, or <span style="font-family: monospace;">'g'</span> key again.  Other keys
  will select another plot using the object nearest the cursor to select
  a focus or object.
  </p>
  <p>
  Any of the graphs with enclosed flux or intensity profiles vs radius may
  have the profiles of the object with the smallest size overplotted.  The
  overplot has a dashed line, a different color on color graphics devices,
  and no symbols marking the measurement points.  The overplots may be
  enabled or disabled with the <span style="font-family: monospace;">":overplot"</span> command.  Initially it is
  disabled.
  </p>
  <p>
  The final plots give a spatial representation.  These require more than one
  object.  The <span style="font-family: monospace;">'a'</span> key gives a spatial plot at a single focus.  The space bar
  can be used to advance to another focus.  This plot has a central graph of
  column and line coordinates with symbols indicating the position of an
  object.  The objects are marked with a circle (when plotted at unit aspect
  ratio) whose size is proportional to the measured PSF size.  In addition an
  optional asterisk symbol with size proportional to the relative
  brightness of the object may be plotted.  This symbol is toggled with the
  <span style="font-family: monospace;">'s'</span> key.  On color displays the circles may have two colors, one if object
  size is above the average best size and the other if the size is below the
  best size.  The purpose of this is to look for a spatial pattern in the
  smallest PSF sizes.
  </p>
  <p>
  Adjacent to the central graph are graphs with column or line as one
  coordinate and radius or ellipticity as the other.  The symbols
  are the same as described previously.  These plots can show spatial
  gradients in the PSF size and shape across the image.
  </p>
  <p>
  The <span style="font-family: monospace;">'b'</span> key gives a spatial plot of the best focus estimates for each
  object.  This requires multiple objects and multiple focus values.
  As discussed previously, given more than one focus a best focus
  value and size at the best focus is computed by parabolic interpolation.
  This plot type shows the object positions in the same way as the <span style="font-family: monospace;">'a'</span>
  plot except that the radius is the estimated best radius.  Instead
  of adjacent ellipticity plots there are plots of best focus verses
  columns and lines.  Also the two colors in the symbol plots are
  selected depending on whether the object's best focus estimate is
  above or below the overall best focus estimate.  This allows seeing
  spatial trends in the best focus.
  </p>
  <p>
  In addition to the keys which select plots there are other keys which
  do various things.  These are summarized below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ?  Page cursor command summary
  d  Delete star nearest to cursor
  i  Information about point nearest the cursor
  n  Normalize enclosed flux at x cursor position
  o  Offset enclosed flux by adjusting background
  q  Quit
  r  Redraw
  s  Toggle magnitude symbols in spatial plots
  u  Undelete all deleted points
  x  Delete nearest point, star, or focus (selected by query)
  &lt;space&gt; Step through different focus or stars in current plot type
  </pre></div>
  <p>
  The help, redraw, and quit keys are provide the standard functions.
  The <span style="font-family: monospace;">'s'</span> and space keys were described previously.  The <span style="font-family: monospace;">'i'</span> key
  locates the nearest object to the cursor in whatever plot is shown and
  prints one line of information about the object on the graphics device
  status area.
  </p>
  <p>
  The <span style="font-family: monospace;">'d'</span> key deletes the star nearest the cursor in whatever plot is
  currently displayed.  Deleting a star deletes all measurements of an object
  at different focus values.  To delete all objects from an image, all focus
  values for one star (the same as <span style="font-family: monospace;">'d'</span>), all objects at one focus, or a
  single measurement, the <span style="font-family: monospace;">'x'</span> key is used.  Typing this key produces a query
  for which type of deletion and the user responds with <span style="font-family: monospace;">'i'</span>, <span style="font-family: monospace;">'s'</span>, <span style="font-family: monospace;">'f'</span>, or
  <span style="font-family: monospace;">'p'</span>.  The most common use of this is to delete all objects at the extreme
  focus values.  Deleted measurements do not appear in any subsequent
  graphics, are excluded from all computations, and are not output in the
  results.  The <span style="font-family: monospace;">'u'</span> key allows one to recover deleted measurements.  This
  undeletes all previously deleted data.
  </p>
  <p>
  Due to various sources of error the sky value may be wrong causing
  the enclosed flux profile to not converge properly but instead
  decreases beyond some point (overestimated sky) or linearly
  increases with radius (underestimated sky).  This affects the size
  measurement by raising or lowering the normalization and altering
  the shape of the enclosed flux profile.  The <span style="font-family: monospace;">'n'</span> and <span style="font-family: monospace;">'o'</span> keys allow
  fudging the enclosed flux profiles.  These keys apply only in
  the zoom plot of the enclosed flux profile or the case where
  a single enclosed flux profile is shown with the <span style="font-family: monospace;">'e'</span> key; in other
  words plots of the enclosed flux which have axes labels.
  </p>
  <p>
  The <span style="font-family: monospace;">'n'</span> key normalizes the enclosed flux profile at the point
  set by the x position of the cursor.  The <span style="font-family: monospace;">'o'</span> key increases or
  decreases the background estimate to bring curve up or down to
  the point specified by the cursor.  The effect of this is to
  add or subtract a quadratic function since the number of pixels
  at a particular radius varies as the square of the radius.
  To restore the original profile, type <span style="font-family: monospace;">'n'</span> or <span style="font-family: monospace;">'o'</span> at a radius
  less than zero.
  </p>
  <p>
  The colon commands, shown below, allow checking or changing parameters
  initially set by the task parameters, toggling the overplotting of the
  smallest PSF profiles, and showing the current results.  The overplotting
  option and the contents of the results displayed by :show were described
  previously.
  </p>
  <div class="highlight-default-notranslate"><pre>
  :beta &lt;val&gt;     Beta parameter for Moffat fits
  :level &lt;val&gt;    Level at which the size parameter is evaluated
  :overplot &lt;y|n&gt; Overplot the profiles from the narrowest profile?
  :radius &lt;val&gt;   Change profile radius
  :show &lt;file&gt;    Page all information for the current set of objects
  :size &lt;type&gt;    Size type (Radius|FWHM)
  :scale &lt;val&gt;    Pixel scale for size values
  :xcenter &lt;val&gt;  X field center for radius from field center plots
  :ycenter &lt;val&gt;  Y field center for radius from field center plots
  </pre></div>
  <p>
  The important values which one might want to change interactively are
  the measurement level and the profile radius.  The measurement level
  directly affects the results reported.  When it is changed the sizes
  of all object PSFs are recomputed and the displayed plots and title
  information are updated.  The profile radius is the
  maximum radius shown in plots and used to set the enclosed flux normalization.
  It does not affect the object centering or sky region definition and
  evaluation which are done when the image data is accessed.  Because
  the objects are not remeasured from the image data the radius may
  not be made larger than the radius defined by the task parameter though
  it may be decreased and then increased again.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  A multiple exposure frame is taken with 7 exposures of a bright
  star, each exposure shifted by 50 pixels to lower line positions, with a
  double gap at the end.  The exposure pattern is typical of Kitt Peak and
  the default values for the direction and gap position are applicable.  The
  default focus value numbering and measurements in pixels are also used.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; starfocus focus1 nexp=7 step=50
  &lt;The image is displayed and the image cursor activated&gt;
  &lt;The bright star is marked with <span style="font-family: monospace;">'m'</span>&gt;
  &lt;Marking is finished with <span style="font-family: monospace;">'q'</span>&gt;
  &lt;A graph of FWHM vs focus index is shown&gt;
  &lt;Exit with <span style="font-family: monospace;">'q'</span>&gt;
  NOAO/IRAF IRAFV2.10.3 valdes@puppis Wed 16:09:39 30-Jun-93
    Best focus of 4.12073 with FWHM (at 50% level) of 3.04
  
     Image  Column    Line     Mag   Focus    FWHM   Ellip      PA SAT
    focus1  536.63  804.03    0.07      1.  13.878    0.06     -11
            535.94  753.28   -0.11      2.   8.579    0.09      89
            535.38  703.96   -0.08      3.   5.184    0.11     -87
            537.12  655.36   -0.02      4.   3.066    0.07     -77
            534.20  604.59    0.00      5.   4.360    0.10      74
            534.41  554.99   -0.00      6.   9.799    0.09     -35
            534.83  456.08    0.16      7.  12.579    0.13     -10
  </pre></div>
  <p>
  The estimated best focus is between the 4th and 5th focus setting
  and the best focus FWHM is 3.04 pixels.
  </p>
  <p>
  Note that in more recent Kitt Peak multiple exposure focus images the
  starting focus value, the focus step, the number of exposures, and
  the shift are recorded in the image header with the keywords
  FOCSTART, FOCSTEP, FOCNEXPO, and FOCSHIFT.  Thus the task parameters
  <i>focus</i>, <i>fstep</i>, <i>nexposures</i>, and <i>step</i> may be
  set to those names.  However, rather than use <b>starfocus</b>
  one would use the more convenient <b>kpnofocus</b>.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imexamine, implot, kpnofocus, pprofile, pradprof, psfmeasure, radlist,
  radplt, radprof, ranges, specfocus, splot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'CURSOR COMMANDS' 'DESCRIPTION' 'ALGORITHMS' 'INTERACTIVE GRAPHICS MODE' 'EXAMPLES' 'SEE ALSO'  -->
  

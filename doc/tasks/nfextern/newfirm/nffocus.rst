.. _nffocus:

nffocus: Determine best focus from NEWFIRM exposures
====================================================

**Package: newfirm**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  nffocus images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>This may identify a single exposure in a focus sequence by name
  (e.g. image17418) or number (e.g. 17418) or be a list of images.
  In the case of a single exposure or number the task will identify all
  the exposures in the focus sequence containing that exposure.  A
  list may be the full sequence or a subset.  Typically the exposures
  are unprocessed though reduced exposures may also be used.
  </dd>
  </dl>
  <dl id="l_sky">
  <dt><b>sky = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sky' Line='sky = ""' -->
  <dd>Optional NEWFIRM sky exposure to be subtracted from each focus
  exposure to provide a quick dark subtraction and removal of sky
  structure.  If no explicit exposure is specified then the task will
  identify a sky exposure in the focus sequence.
  </dd>
  </dl>
  <dl id="l_catalog">
  <dt><b>catalog = <span style="font-family: monospace;">"_cat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catalog' Line='catalog = "_cat"' -->
  <dd>Suffix to be added to the exposure filename for the source catalogs.
  </dd>
  </dl>
  <dl id="l_saturate">
  <dt><b>saturate = <span style="font-family: monospace;">"9000"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='saturate' Line='saturate = "9000"' -->
  <dd>A value used to filter out brighter sources which suffer from
  saturation or significant non-linear effects.  Sources whose peak
  value exceeds this value are filtered out of the source lists.  A
  value of $&lt;keyword&gt; may be specified to reference a header keyword value.
  </dd>
  </dl>
  <dl id="l_nmaxrec">
  <dt><b>nmaxrec = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nmaxrec' Line='nmaxrec = INDEF' -->
  <dd>If not INDEF the cataloged compact sources are sorted by peak value (after
  filtering for saturation) and the specified number of brightest
  sources are used.
  </dd>
  </dl>
  <dl id="l_match">
  <dt><b>match = 10.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='match' Line='match = 10.' -->
  <dd>The catalog sources are matched between each focus exposure either in
  celestial coordinates or in pixels.  A positive value specifies a
  maximum matching distance in arc seconds.  A negative value specifies
  that the absolute value be used as the maximum matching distance in
  pixels.
  </dd>
  </dl>
  <dl id="l_sig">
  <dt><b>sig = 2.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sig' Line='sig = 2.5' -->
  <dd>Sigma clipping factor for the radius and focus values.  This allows an
  initial clipping of large outliers typically due to non-stellar sources.
  A value of INDEF is used to skip the sigma clipping.  Also see the <span style="font-family: monospace;">'v'</span>
  key to undelete any sigma clipped objects.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"nffocus.log"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "nffocus.log"' -->
  <dd>Log file for output from the task.  This will include detailed
  information as well as the final global recommendations.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print some processing progress information.  In particular, this shows
  the progress of making the source catalogs.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Analyze the source measurements and focus graphics interactively?
  This must be yes in order to interactively delete bad measurements.
  </dd>
  </dl>
  <dl id="l_focus">
  <dt><b>focus</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='focus' Line='focus' -->
  <dd>Output parameter for the recommended focus.
  </dd>
  </dl>
  <dl id="l_fwhm">
  <dt><b>fwhm</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fwhm' Line='fwhm' -->
  <dd>Output parameter for the estimated best full-width at half-maximum.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  NFFOCUS is a script for analyzing NEWFIRM focus exposure sequences.  It
  combines the steps of cataloging sources, possibly with sky subtraction, in
  each input exposure and running the ACEFOCUS routine for matching the
  sources at different focus values and analyzing the full-width at
  half-maximum (FWHM) measurements.
  </p>
  <p>
  A NEWFIRM focus sequence begins with a sky exposure and then some number of
  exposures at different focus settings.  This task is NEWFIRM specific in
  that it depends on certain keywords and image naming syntax.  These include
  OBSTYPE to identify sky ('sky') and focus ('object') exposures, NOCNO and
  NOCTOT to identify the members of the sequence, TELFOCUS for the focus values.
  Some of these are only used when an single name or sequence number is
  specified.  Use of a sequence number is a particularly simple way to specify
  a sequence while an explicit list, usually in an @file, is useful if some
  exposures are to be excluded.
  </p>
  <p>
  Detection, measuring and catalog of sources is performed by the tasks
  ACECATALOG or ACEDIFF.  The former is used when no sky exposure is specified
  and the latter is used to subtract the sky exposure prior to
  detection.  In either case the same quantities are measured and cataloged.
  The key quantity for focus analysis is the FWHM.  Other quantities are used
  for matching, spatial analysis, and magnitude weighting and display.
  </p>
  <p>
  Briefly, the FWHM measurement is computed as follows.  The half-maximum
  value for a source is defined as one-half of the peak pixel value and the
  source position is defined by the flux weighted centroid.  For each pixel
  with value within 10% of the half-maximum value a gaussian with the same
  centroid, maximum value (even if the maximum and centroid are not
  coincident), and pixel value is used as a simple extrapolator to find the
  half-maximum radius.  Each of these single pixel estimates are averaged with
  weights based on the difference in the pixel value from an exact
  half-maximum value.  Twice this average is then the FWHM value.
  </p>
  <p>
  The first time the task is run the catalogs are created with filenames
  beginning with the image name followed by the user specified catalog suffix.
  There is a catalog for each array.  Depending on the machine speed, creating
  a catalog from a 2K array takes of order 5-10 seconds.  The <i>verbose</i>
  parameter prints a line as each catalog is created to monitor the progress
  of the task.
  </p>
  <p>
  If the task is run again it will check for existing catalogs and, if found,
  will issue a warning but will not recreate the catalogs and getting to the
  focus analysis is fast.  You are free to run the task multiple times.  Note
  this means that changing parameters involving the detection and cataloging,
  such as the sky subtraction, requires first manually deleting the catalogs
  or using a different catalog suffix.
  </p>
  <p>
  The source detection is limited to good signal-to-noise and compact sources.
  The detection threshold is 5 times the background noise sigma with no
  convolution filter used.  A minimum of 8 pixels is required in a source.  A
  first filtering of sources selects those with FWHM value less than 2.5 times
  the mode of the FWHM for all sources and with an ellipticity, based on the
  second moments of the light distribution, less than 0.2.
  </p>
  <p>
  One other selection criteria may be applied to eliminate sources which
  saturate or have significantly non-linear pixels.  If the <i>saturate</i>
  parameter is specified then sources with peak value (without sky
  subtraction) above that value are eliminated.  Note that the special value
  <span style="font-family: monospace;">"$&lt;keyword&gt;"</span> sets a value from a header keyword to allow different values
  for each array.
  </p>
  <p>
  If the exposures contain many sources it may be desirable to limit the
  number catalog using the <i>nmaxrec</i> parameter.  The specified
  maximum number of sources is made using an ordering by the source peak
  values above background, brightest first.  If used the number should
  not be too small to insure sufficient matches across all focus
  exposures.  In other words, there is no assurance that the same set of
  sources will be detected and be in the same peak value order in each
  exposure.
  </p>
  <p>
  The individual source measurements from individual catalogs are matched
  using a simple nearest distance in either pixels or world coordinates (i.e.
  RA and DEC) where the type of maximum matching distance is signaled by the
  sign of <i>match</i> parameter.  Generally one should use a liberal
  matching distance in world coordinates.  This allows focus exposures
  to be dithered if desired; though this is not the recommended way to
  take focus sequences.
  </p>
  <p>
  In the analysis stage only sources which are matched in all focus exposures
  are used which is why it is important not to overly limit the catalogs with
  the <i>nmaxrec</i> parameter.  There is one exception, if no matches are made
  (which can be forced by setting <i>match</i> to zero), then the analysis will
  be done using the median FWHM of all sources at each focus exposure.
  </p>
  <p>
  There is an initial stage of sigma clipping to eliminate outliers.  The
  clipping is done for both the FWHM values and the estimated focus values
  from each source.  This applies to both the matched and no match cases.  In
  the matched case an outlier at one focus eliminates the matched source at
  all focus values.
  </p>
  <p>
  The analysis task estimates a focus and FWHM for each source which has
  not been eliminated or interactively deleted or the median
  points when no individual matched sources are available, The estimates are
  computed by selecting the three lowest FWHM values and averaging the focus
  and FWHM values.  The averaging is weighted where the measurement with the
  lowest FWHM is given a weight of 1 and the other two measurements have
  weights that decrease rapidly with differences in the FWHM and focus.  The
  effect is that if the next smallest FWHM measurements are similar in FWHM
  and focus then the weights are near 1 and if not the weights are
  significantly smaller.
  </p>
  <p>
  The overall best focus is the magnitude-weighted average of the individual
  source best focus estimates.
  </p>
  <p>
  When the <i>interactive</i> parameter is set (recommended) then an
  interactive graphical stage is entered.  This allows visualizing the source
  measurements in various ways.  The initial graph shows FWHM as a
  function of focus.  The cross points are the initial source
  measurements which have not be eliminated or deleted and the boxes
  are the medians with the lower of the two central FWHM in the case
  of an even number of values.  Also shown with dashed lines are the
  estimated best focus and FWHM.
  </p>
  <p>
  Commands are entered in cursor mode (when a cursor is present).  These
  are either single keystrokes or colon commands.  The list of commands
  may be paged by typing <span style="font-family: monospace;">'?'</span>.  This is also given below.
  </p>
  <p>
  An important interactive key is <span style="font-family: monospace;">'d'</span> to delete the source or point
  nearest the cursor.  This applies to any graph.  When sources are
  matched then selecting a point to delete will also delete all other
  points associated with that source.  When the sources are not matched
  then only the single point is deleted.  The <span style="font-family: monospace;">'d'</span> key is particularly
  useful in the FWHM vs focus or best focus spatial points.
  </p>
  <p>
  The best focus spatial plot is available when sources have been
  matched.  This provides for a spatial analysis to see focus trends.
  The plot shows the full mosaic in the center and two pairs of
  projection plots.  The left and bottom show FWHM as a function of
  column and line.  The top and right show the focus estimate for each
  source (as described above) as a function of column and line.
  </p>
  </section>
  <section id="s_cursor_command_options">
  <h3>Cursor command options</h3>
  <div class="highlight-default-notranslate"><pre>
  ? Help            d Delete          q Quit            u Undelete
  &lt;space&gt; Next      f Focus           r Redraw          v Undelete sig clip
  a Spatial         i Info            s Mag symbols     x Delete
  b Best            m Magnitude       t Field radius    y Box delete
  
  :show &lt;file&gt;      :scale &lt;val&gt;      :xcenter &lt;val&gt;    :ycenter &lt;val&gt;
  </pre></div>
  <dl>
  <dt><b>?</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='' Line='?' -->
  <dd>Page this help information
  </dd>
  </dl>
  <dl>
  <dt><b>&lt;space&gt;</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='' Line='&lt;space&gt;' -->
  <dd>Step through different focus or stars in current plot type
  </dd>
  </dl>
  <dl id="l_a">
  <dt><b>a</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='a' Line='a' -->
  <dd>Spatial plot at a single focus (when there are matched points)
  </dd>
  </dl>
  <dl id="l_b">
  <dt><b>b</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='b' Line='b' -->
  <dd>Spatial plot of best focus values (when there are matched points)
  </dd>
  </dl>
  <dl id="l_d">
  <dt><b>d</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='d' Line='d' -->
  <dd>Delete star (when matched) or point (unmatched) nearest to cursor 
  </dd>
  </dl>
  <dl id="l_f">
  <dt><b>f</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='f' Line='f' -->
  <dd>Size vs focus for all data
  </dd>
  </dl>
  <dl id="l_i">
  <dt><b>i</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='i' Line='i' -->
  <dd>Information about point nearest the cursor
  </dd>
  </dl>
  <dl id="l_m">
  <dt><b>m</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='m' Line='m' -->
  <dd>Size vs relative magnitude at one focus
  </dd>
  </dl>
  <dl id="l_q">
  <dt><b>q</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='q' Line='q' -->
  <dd>Quit
  </dd>
  </dl>
  <dl id="l_r">
  <dt><b>r</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='r' Line='r' -->
  <dd>Redraw
  </dd>
  </dl>
  <dl id="l_s">
  <dt><b>s</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='s' Line='s' -->
  <dd>Toggle magnitude symbols in spatial plots
  </dd>
  </dl>
  <dl id="l_t">
  <dt><b>t</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='t' Line='t' -->
  <dd>Size vs radius from field center at one focus
  </dd>
  </dl>
  <dl id="l_u">
  <dt><b>u</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='u' Line='u' -->
  <dd>Undelete points
  </dd>
  </dl>
  <dl id="l_v">
  <dt><b>v</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='v' Line='v' -->
  <dd>Undelete sigma clipped points.
  </dd>
  </dl>
  <dl id="l_x">
  <dt><b>x</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='x' Line='x' -->
  <dd>Delete nearest point, star, focus, or image (selected by query)
  </dd>
  </dl>
  <dl id="l_y">
  <dt><b>y</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='y' Line='y' -->
  <dd>Delete points within box region (two cursor reads)
  </dd>
  </dl>
  <dl>
  <dt><b>:show &lt;file&gt;</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='' Line=':show &lt;file&gt;' -->
  <dd>Page all information for the current set of objects
  </dd>
  </dl>
  <dl>
  <dt><b>:scale &lt;val&gt;</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='' Line=':scale &lt;val&gt;' -->
  <dd>Pixel scale for size values
  </dd>
  </dl>
  <dl>
  <dt><b>:xcenter &lt;val&gt;</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='' Line=':xcenter &lt;val&gt;' -->
  <dd>X field center for radius from field center plots
  </dd>
  </dl>
  <dl>
  <dt><b>:ycenter &lt;val&gt;</b></dt>
  <!-- Sec='CURSOR COMMAND OPTIONS' Level=0 Label='' Line=':ycenter &lt;val&gt;' -->
  <dd>Y field center for radius from field center plots
  </dd>
  </dl>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMAND OPTIONS'  -->
  

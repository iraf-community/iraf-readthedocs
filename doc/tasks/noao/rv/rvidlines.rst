.. _rvidlines:

rvidlines: Measure radial velocities from spectral lines
========================================================

**Package: rv**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rvidlines images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of spectral images in which to identify spectral lines and measure a
  velocity.  The spectra must be dispersion calibrated in Angstroms.
  </dd>
  </dl>
  <dl id="l_section">
  <dt><b>section = <span style="font-family: monospace;">"middle line"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='section' Line='section = "middle line"' -->
  <dd>If an image is not one dimensional or given as a one dimensional image
  section then the image section given by this parameter is used.  The
  section is used to define the initial vector and the direction (columns,
  lines, or <span style="font-family: monospace;">"z"</span>) of the image vectors to be fit.  The image is still considered
  to be two or three dimensional and it is possible to change the data vector
  within the program.
  The section parameter may be specified directly as an image section or
  in one of the following forms
  <div class="highlight-default-notranslate"><pre>
  line|column|x|y|z first|middle|last|# [first|middle|last|#]]
  first|middle|last|# [first|middle|last|#] line|column|x|y|z
  </pre></div>
  where each field can be one of the strings separated by | except for #
  which is an integer number.  The field in [] is a second designator
  which is used with 3D data.  See the example section for examples of
  this syntax.  Abbreviations are allowed though beware
  that <span style="font-family: monospace;">'l'</span> is not a sufficient abbreviation.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"database"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "database"' -->
  <dd>Database in which the feature data and redshifts are recorded.
  </dd>
  </dl>
  <dl id="l_coordlist">
  <dt><b>coordlist = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coordlist' Line='coordlist = ""' -->
  <dd>User coordinate list consisting of an ordered list of rest spectral line
  coordinates.  If a line list is defined lines from the list may be
  automatically found and added to the lines being measured.
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = <span style="font-family: monospace;">"10"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = "10"' -->
  <dd>Number of lines, columns, or bands across the designated vector axis to be
  summed when the image is a two or three dimensional spatial spectrum.
  It does not apply to multispec format spectra.  If the image is three
  dimensional an optional second number can be specified for the higher
  dimensional axis  (the first number applies to the lower axis number and
  the second to the higher axis number).  If a second number is not specified
  the first number is used for both axes.
  </dd>
  </dl>
  <dl id="l_match">
  <dt><b>match = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='match' Line='match = 5.' -->
  <dd>The maximum difference for a match between the measured line coordinate
  and a coordinate in the coordinate list.  The units of this parameter
  is that of the user coordinates.
  </dd>
  </dl>
  <dl id="l_maxfeatures">
  <dt><b>maxfeatures = 50</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxfeatures' Line='maxfeatures = 50' -->
  <dd>Maximum number of the strongest features to be selected automatically from
  the coordinate list (function <span style="font-family: monospace;">'l'</span>) or from the image data (function <span style="font-family: monospace;">'y'</span>).
  </dd>
  </dl>
  <dl id="l_zwidth">
  <dt><b>zwidth = 100.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zwidth' Line='zwidth = 100.' -->
  <dd>Width of graphs, in user coordinates, when in zoom mode (function <span style="font-family: monospace;">'z'</span>).
  </dd>
  </dl>
  <p>
  The following parameters are used in determining feature positions.
  </p>
  <dl id="l_ftype">
  <dt><b>ftype = <span style="font-family: monospace;">"absorption"</span> (emission|absorption|gemission|gabsorption)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ftype' Line='ftype = "absorption" (emission|absorption|gemission|gabsorption)' -->
  <dd>Type of features to be identified.  The possibly abbreviated choices are
  <span style="font-family: monospace;">"emission"</span>, <span style="font-family: monospace;">"absorption"</span>, <span style="font-family: monospace;">"gemission"</span>, and <span style="font-family: monospace;">"gabsorption"</span>.  The first two
  select the <b>center1d</b> centering algorithm while the last two
  select the Gaussian fitting centering algorithm.
  </dd>
  </dl>
  <dl id="l_fwidth">
  <dt><b>fwidth = 4.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fwidth' Line='fwidth = 4.' -->
  <dd>Width in pixels of features to be identified.
  </dd>
  </dl>
  <dl id="l_cradius">
  <dt><b>cradius = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cradius' Line='cradius = 5.' -->
  <dd>The maximum distance, in pixels, allowed between a feature position
  and the initial estimate when defining a new feature.
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 0.' -->
  <dd>In order for a feature center to be determined the range of pixel intensities
  around the feature must exceed this threshold.
  </dd>
  </dl>
  <dl id="l_minsep">
  <dt><b>minsep = 2.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minsep' Line='minsep = 2.' -->
  <dd>The minimum separation, in pixels, allowed between feature positions
  when defining a new feature.
  </dd>
  </dl>
  <p>
  The following parameters control the input and output.
  </p>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "logfile"' -->
  <dd>Log file for recording the results of the velocity measurements.  The
  results are written when exiting or changing input images.  The
  results can be previewed with the <span style="font-family: monospace;">":features"</span> command.  If no log file
  is specified then the results are not saved.
  </dd>
  </dl>
  <dl id="l_autowrite">
  <dt><b>autowrite = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='autowrite' Line='autowrite = no' -->
  <dd>Automatically write or update the logfile and database?  If no then a query
  is given for writing results to the logfile.  A query for writing to the
  database is also given if the feature data have been modified.  If yes
  exiting the program automatically writes to the logfile and updates the
  database.
  </dd>
  </dl>
  <dl id="l_keywpars">
  <dt><b>keywpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='keywpars' Line='keywpars = ""' -->
  <dd>The image header keyword translation table as described in 
  the <i>keywpars</i> named pset.  This defines the header keywords used
  to obtain the observation information needed for computing the
  heliocentric velocity.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Graphics device.  The default is the standard graphics device which is
  generally a graphics terminal.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Cursor input file.  If a cursor file is not given then the standard graphics
  cursor is read.
  </dd>
  </dl>
  </section>
  <section id="s_addtional_parameters">
  <h3>Addtional parameters</h3>
  <p>
  The measured velocities are corrected to a heliocentric frame of reference
  if possible.  This requires determining various parameters about the
  observation.  The latitude, longitude, and altitude of the observation
  are determined from the observatory database.  The observatory is
  defined by either the OBSERVAT image header keyword or the <span style="font-family: monospace;">"observatory"</span>
  package parameter in that order.  See the help for <b>observatory</b>
  for additional information.
  </p>
  <p>
  The date, universal time, right ascension, declination, and coordinate epoch
  for the observation are obtained from the image header.  The keywords
  for these parameters are defined in the <b>keywpars</b> parameter set.
  Note that the parameters used are <span style="font-family: monospace;">"ra"</span>, <span style="font-family: monospace;">"dec"</span>, <span style="font-family: monospace;">"ut"</span>, and <span style="font-family: monospace;">"date-obs"</span>.
  The <span style="font-family: monospace;">"utmiddle"</span> parameter is not used so if you have a keyword for the
  middle of the exposure that you want to use then you must set the
  <span style="font-family: monospace;">"ut"</span> parameter to reference that keyword.
  </p>
  <p>
  Before IRAF V2.12, if the date keyword included a time then that time was
  used and the <span style="font-family: monospace;">"ut"</span> keyword was not used.  In V2.12 this was changed and the
  time is always taken from the keyword specified by <span style="font-family: monospace;">"ut"</span>.  However, the
  value can be in either a single time or a date/time string.  So if you
  want to use both the date and time from the same keyword, say DATE-OBS,
  then point the <span style="font-family: monospace;">"date_obs"</span> and <span style="font-family: monospace;">"ut"</span> parameters in KEYWPARS to the same
  keyword.
  </p>
  </section>
  <section id="s_cursor_keys">
  <h3>Cursor keys</h3>
  <div class="highlight-default-notranslate"><pre>
  ?  Clear the screen and print menu of options
  a  Apply next (c)enter or (d)elete operation to (a)ll features
  b  Mark and de(b)lend features by Gaussian fitting
  c  (C)enter the feature nearest the cursor
  d  (D)elete the  feature nearest the cursor
  f  (F)it redshift and velocity from the fitted and user coordinates
  i  (I)nitialize (delete features and coordinate fit)
  j  Go to the preceding image line/column/band/aperture
  k  Go to the next image line/column/band/aperture
  l  Match coordinates in the coordinate (l)ist
  m  (M)ark new feature near the cursor and enter coord and label
  n  Move the cursor or zoom to the (n)ext feature (same as +)
  o  Go to the specified image line/column/band/aperture
  p  (P)an to user defined window after (z)ooming on a feature
  q  (Q)uit and continue with next image (also carriage return)
  r  (R)edraw the graph
  t  Reset the position of a feature without centering
  u  Enter a new (u)ser coordinate and label for the current feature
  w  (W)indow the graph.  Use <span style="font-family: monospace;">'?'</span> to window prompt for more help.
  y  Automatically find strongest peaks and identify them
  z  (Z)oom on the feature nearest the cursor
  +  Move the cursor or zoom to the next feature
  -  Move the cursor or zoom to the previous feature
  I  Interrupt task and exit immediately
  </pre></div>
  <p>
  The parameters are listed or set with the following commands which may be
  abbreviated.  To list the value of a parameter type the command alone.
  </p>
  <div class="highlight-default-notranslate"><pre>
  :show file              Show the values of all the parameters
  :features file          Write feature list to file (default STDOUT)
  
  :coordlist file         Coordinate list file
  :cradius value          Centering radius in pixels
  :threshold value        Detection threshold for feature centering
  :database name          Database for recording feature records
  :ftype value            Feature type
                            (emission|absorption|gemission|gabsorption)
  :fwidth value           Feature width in pixels
  :image imagename        Set a new image or show the current image
  :labels value           Feature label type
                              (none|index|pixel|coords|user|both)
  :match value            Coordinate list matching distance
  :maxfeatures value      Maximum number of features automatically found
  :minsep value           Minimum separation allowed between features
  :read name ap           Read a record from the database
                            (name/ap default to the current spectrum)
  :write name ap          Write a record to the database
                            (name/ap default to the current spectrum)
  :add name ap            Add features from the database
                            (name/ap default to the current spectrum)
  :zwidth value           Zoom width in user units
  
  Labels:
        none - No labels
       index - Sequential numbers in increasing pixel position
       pixel - Pixel coordinates
      coords - User coordinates such as wavelength
        user - User labels
        both - Combination of coords and user
  </pre></div>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Rvidlines</b> measures radial velocities from spectra by determining the
  wavelength shift in spectral lines relative to specified rest wavelengths.
  The basic usage consists of identifying one or more spectral lines (also
  called features), entering the rest wavelengths, and computing the average
  wavelength shift converted to a radial velocity.  Additional lines can then
  be automatically added from a coordinate list of rest wavelengths.
  </p>
  <p>
  Each dispersion calibrated image in the input list is examined in turn.  If
  the image is not one dimensional or a one dimensional section of an image
  then the image section given by the parameter <i>section</i> is used.  This
  parameter may be specified in several ways as described in the parameter
  and examples sections.  The image section is used to select a starting
  vector and image axis.  The parameter <i>nsum</i> determines the number
  of lines, columns, or bands to sum in a two or three dimensional image.
  </p>
  <p>
  Once a spectrum has been selected it is graphed.  The graph title includes
  the image name, spectrum title, and the current velocity and redshift if
  one has been determined.  An initial feature list is read from the database
  if an entry exists.  The features are marked on the graph by tick marks.
  The features may also be labeled using the <span style="font-family: monospace;">":label"</span> option.  The graph has
  the observed wavelength scale along the bottom and the rest wavelength
  scale along the top (if a velocity has been determined).  The status line
  gives the pixel coordinate, observed wavelength, rest wavelength (as
  computed by the last velocity computation), the true rest wavelength, the
  velocity residual, and an optional identification string for the <span style="font-family: monospace;">"current"</span>
  feature.
  </p>
  <p>
  The graphics cursor is used to select features and perform various
  functions.  A menu of the keystroke options and functions is printed with
  the key <span style="font-family: monospace;">'?'</span>.  The cursor keys and their functions are defined in the CURSOR
  KEYS section and described further below.  The standard cursor mode keys
  are also available to window and redraw the graph and to produce hardcopy
  <span style="font-family: monospace;">"snaps"</span>.
  </p>
  <p>
  There are two types of feature selection functions;  defining new
  features and selecting previously defined features.  The <span style="font-family: monospace;">'m'</span> key marks
  a new feature near the cursor position.  The feature position is
  determined by a centering algorithm.  There are two algorithms;
  a flux bisecting algorithm called <b>center1d</b> and a gaussian
  profile fitting algorithm.  The choice of fitting algorithm and whether the
  feature is an emission or absorption line is set by the <i>ftype</i>
  parameter.
  </p>
  <p>
  The center1d algorithm is described in the help topic <b>center1d</b>.  The
  parameters which control it are <i>fwidth</i>, <i>ftype</i>, <i>cradius</i>,
  and <i>threshold</i>.
  </p>
  <p>
  The gaussian fitting algorithm estimates a linear local background by
  looking for the minimum or maximum, depending on whether the feature type
  is set to absorption or emission, within a distance of the entered cursor
  position of one-half the feature width specified by the <i>fwidth</i>
  parameter plus the centering error radius specified by the <i>cradius</i>
  parameters.  This background estimation is crude but generally is not
  critical for reasonably strong lines.  Once the sloped background is
  defined a non-linear Levenberg-Marquardt algorithm determines the gaussian
  center, peak strength, and sigma.  The initial estimates for these
  parameters are the starting center, the background subtracted pixel value
  at the starting center, and the <i>fwidth</i> value divided by six.  After
  fitting the gaussian model it is overplotted on the data for comparison.  The
  <i>threshold</i> parameter also applies to this algorithm to check for a
  minimum data range and the <i>cradius</i> parameter checks for a maximum
  error in the center from the initial value.
  </p>
  <p>
  For a more critical setting of the background in the gaussian algorithm or
  for the simultaneous solution of multiple gaussian components (deblending)
  the <span style="font-family: monospace;">'b'</span> key is available.  The <span style="font-family: monospace;">'b'</span> key is used to mark the initial
  positions of up to ten features.  The feature marking ends with <span style="font-family: monospace;">'q'</span>.  The
  user is then queried to mark two points for the linear background.  After
  doing the simultaneous fitting the user is queried sequentially for the
  rest wavelengths of each line.  Note that the <span style="font-family: monospace;">'b'</span> key will do the gaussian
  fitting regardless of whether the <i>ftype</i> setting is for a gaussian
  or not and can be used for fitting just a single line.
  </p>
  <p>
  When a feature is defined the value of <i>ftype</i> and <i>fwidth</i> are
  associated with the feature.  Subsequent recentering will use these values
  even if the default values are changed.  This is how a combination of
  absorption and emission lines may be defined.  The only constraint to this
  is that the feature data does not record the combination of lines used in a
  deblending operation so automatic recentering will treat each line
  separately.
  </p>
  <p>
  When a new feature is marked if the wavelength is within a distance given
  by the parameter <i>minsep</i> of a previous feature it is considered to be
  the same feature and replaces the old feature.  The coordinate list is
  searched for a match between the measured wavelength, corrected to rest
  using the current velocity, and a user coordinate in the list.  The
  matching is based on the nearest line within a specified <i>match</i>
  distance.  If a match is found it becomes the default user coordinate which
  the user may override.  The new feature is marked on the graph and it
  becomes the current feature.  The redefinition of a feature which is within
  the minimum separation may be used to set the user coordinate from the
  coordinate list.  The <span style="font-family: monospace;">'t'</span> key allows setting the position of a feature to
  other than that found by the centering algorithms.
  </p>
  <p>
  If at least one feature is marked with it's rest wavelength specified then
  the <span style="font-family: monospace;">'l'</span> key may be used to identify additional features from a coordinate
  list of rest wavelengths.  First a velocity is computed from the initial
  features.  Then each coordinate in the list is corrected to the
  observed velocity and a feature is sought in the data at that point.
  Up to a maximum number of features, set by the parameter <i>maxfeatures</i>,
  may be defined in this way.  A new velocity is computed using all the
  located features.
  </p>
  <p>
  The <span style="font-family: monospace;">'y'</span> key provides another way to add features.  Rather than look for
  features at the coordinates of a list, a peak finding algorithm is used to
  find features up to the specified maximum number.  If there are more
  peaks only the strongest are kept.  The peaks are then matched against the
  coordinate list to find user coordinate values.
  </p>
  <p>
  To select a different feature as the current feature the keys <span style="font-family: monospace;">'.'</span>, <span style="font-family: monospace;">'n'</span>,
  <span style="font-family: monospace;">'+'</span>, and <span style="font-family: monospace;">'-'</span> are used.  The <span style="font-family: monospace;">'.'</span> selects the feature nearest the cursor, the
  <span style="font-family: monospace;">'n'</span> and <span style="font-family: monospace;">'+'</span> select the next feature, and the <span style="font-family: monospace;">'-'</span> selects the previous
  feature relative to the current feature in the feature list as ordered by
  pixel coordinate.  These keys are useful when redefining the user
  coordinate with the <span style="font-family: monospace;">'u'</span> key and when examining features in zoom mode.
  </p>
  <p>
  The key <span style="font-family: monospace;">'f'</span> computes (<span style="font-family: monospace;">"fits"</span>) a velocity to the defined features.
  This is done by taking a weighted average of the redshifts,
  </p>
  <div class="highlight-default-notranslate"><pre>
  z = (measured - true) / true
  </pre></div>
  <p>
  of the individual lines.  The default weights are always one but a different
  weight may be entered with the <span style="font-family: monospace;">'u'</span> key.  The average redshift is
  converted to a Cz velocity (redshift times the speed of light) and
  corrected to a heliocentric frame if possible.
  </p>
  <p>
  The heliocentric correction requires observatory and observation information.
  The observatory is determined either from the OBSERVAT keyword in the
  image header or by the <span style="font-family: monospace;">"rv.observatory"</span> package parameter.  For a
  discussion of how an observatory is defined and used see the help
  for <b>observatory</b>.  In addition to the observatory the right
  ascension, declination, coordinate epoch, and date and time of the
  observation are required.  If the time is in the date string it has
  precedence over the time keyword.  This information is sought in the image
  header using the keywords defined in the <b>keywpars</b> parameter
  file.  If there is insufficient information for the heliocentric
  velocity correction only the observed velocity will be given.  The
  type of velocity (both velocity and redshift) is indicated by
  identifiers such as Vobs and Vhelio.
  </p>
  <p>
  Note that a new velocity is only computed after typing <span style="font-family: monospace;">'f'</span>, <span style="font-family: monospace;">'l'</span>,
  <span style="font-family: monospace;">":features"</span>, or when exiting and writing the results to the database.
  In other words, adding new features or deleting existing features
  does not automatically update the velocity determination.
  </p>
  <p>
  Features may be deleted with the key <span style="font-family: monospace;">'d'</span>.  All features are deleted
  when the <span style="font-family: monospace;">'a'</span> key immediately precedes the delete key.  Deleting the
  features does not reset the velocity.  The <span style="font-family: monospace;">'i'</span> key initializes
  everything by removing all features and reseting the velocity.
  </p>
  <p>
  It is common to transfer the feature identifications and velocities
  from one image to another.  When a new image without a database entry
  is examined, such as when going to the next image in the input list,
  changing image lines or columns with <span style="font-family: monospace;">'j'</span>, <span style="font-family: monospace;">'k'</span> and <span style="font-family: monospace;">'o'</span>, or selecting
  a new image with the <span style="font-family: monospace;">":image"</span> command, the current feature list and
  velocity are kept.  Alternatively, a database record from a different
  image may be read with the <span style="font-family: monospace;">":read"</span> command.  When transferring feature
  identifications between images the feature coordinates will not agree exactly
  with the new image feature positions and several options are available to
  reregister the feature positions.  The key <span style="font-family: monospace;">'c'</span> centers the feature nearest
  the cursor using the current position as the starting point.  When preceded
  with the <span style="font-family: monospace;">'a'</span> key all the features are recentered (the user must refit
  the coordinate function if desired).  As an aside, the recentering
  function is also useful when the parameters governing the feature
  centering algorithm are changed.  An additional options is the <span style="font-family: monospace;">":add"</span>
  command to add features from a database record.  This does not overwrite
  previous features as does <span style="font-family: monospace;">":read"</span>.
  </p>
  <p>
  Note that when a set of spectra all have the same features in nearly
  the same location the task <b>rvreidlines</b> may be used to reidentify
  the lines and compute a new velocity.
  </p>
  <p>
  In addition to the single keystroke commands there are commands initiated
  by the key <span style="font-family: monospace;">':'</span> (colon commands).  As with the keystroke commands there are
  a number of standard graphics features available beginning with <span style="font-family: monospace;">":."</span> (type
  <span style="font-family: monospace;">":.help"</span> for these commands).  The rvidlines colon commands allow the task
  parameter values to be listed and to be reset within the task.  A parameter
  is listed by typing its name.  The colon command <span style="font-family: monospace;">":show"</span> lists all the
  parameters.  A parameter value is reset by typing the parameter name
  followed by the new value; for example <span style="font-family: monospace;">":match 10"</span>.  Other colon commands
  display the feature list and velocities (:features), control reading and
  writing records to the database (:read and :write), and set the graph
  display format.
  </p>
  <p>
  The feature identification process for an image is completed by typing <span style="font-family: monospace;">'q'</span>
  to quit.  Attempting to quit an image without explicitly logging the
  results or recording changes in the feature database produces a warning
  message unless the <i>autowrite</i> parameter is set.  If this parameter is
  not set prompts are given asking whether to save the results to the log
  file and the database, otherwise the results are automatically saved.  As
  an immediate exit the <span style="font-family: monospace;">'I'</span> interrupt key may be used.  This does not save
  the feature information and may leave the graphics in a confused state.
  </p>
  <p>
  The information recorded in the logfile, if one is specified, includes
  information about the observatory used for heliocentric corrections
  (to verify the correct observatory was used), the list of features
  used in the velocity computation, the wavelength and velocity RMS,
  and lines with the observed and heliocentric redshifts and velocities.
  These lines include an error in the mean derived from the weighted
  RMS and the number of lines used, and the number of lines.  This output
  format is designed so that if there are multiple velocities recorded
  in the same log file they can be easily extracted with the match command:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; match Vhelio logfile
  im1 45 : Vhelio = 15.06 km/s, Mean err = 4.593 km/s, Lines = 7
  im1 40 : Vhelio = 17.77 km/s, Mean err = 3.565 km/s, Lines = 7
  im2 45 : Vhelio = 24.44 km/s, Mean err = 3.741 km/s, Lines = 7
  im2 40 : Vhelio = 14.65 km/s, Mean err =  11.2 km/s, Lines = 7
  ...
  </pre></div>
  </section>
  <section id="s_database_records">
  <h3>Database records</h3>
  <p>
  The database specified by the parameter <i>database</i> is a directory of
  simple text files.  The text files have names beginning with 'id' followed
  by the entry name, usually the name of the image.  The database text files
  consist of a number of records.  A record begins with a line starting with the
  keyword <span style="font-family: monospace;">"begin"</span>.  The rest of the line is the record identifier.  Records
  read and written by <b>rvidlines</b> have <span style="font-family: monospace;">"identify"</span> as the first word of the
  identifier.  Following this is a name which may be specified following the
  <span style="font-family: monospace;">":read"</span> or <span style="font-family: monospace;">":write"</span> commands.  If no name is specified then the image name
  is used.  For 1D spectra the database entry includes the aperture number
  and so to read a solution from a aperture different than the current image
  and aperture number must be specified.  For 2D/3D images the entry name
  has the 1D image section which is what is specified to read the entry.
  The lines following the record identifier contain
  the feature information and redshift (without heliocentric correction).
  </p>
  <p>
  The database files have the name <span style="font-family: monospace;">"identify"</span> and the prefix <span style="font-family: monospace;">"id"</span> because
  these files may also be read by the <b>identify</b> task for changing
  the dispersion function based on the rest wavelengths.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  The radial velocity of the  spectrum, kstar1, is to be determined.
  The user creates a list of line features to be used in the file
  klines.dat.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rvidlines kstar1 coord=klines.dat
      a. The spectrum is drawn
      b. A line is marked with <span style="font-family: monospace;">'m'</span>
      c. Enter the rest wavelength
      d. Compute a velocity with <span style="font-family: monospace;">'f'</span>
      e. Find other lines in the list with <span style="font-family: monospace;">'l'</span>
      f. Exit with <span style="font-family: monospace;">'q'</span>
  Write velocity data to the logfile (yes)? y
  Write feature data to the database (yes)? y
  cl&gt; match Vhelio logfile
  kstar1 1 : Vhelio = 25.1 km/s, Mean err = 1.123 km/s, Lines = 10
  </pre></div>
  <p>
  2.  For echelle or multispec spectra the keys <span style="font-family: monospace;">'o'</span>, <span style="font-family: monospace;">'j'</span>, and <span style="font-family: monospace;">'k'</span> may
  be used to switch between spectra.  Note that the inheritance of features
  in echelle orders is not very useful.  So the <span style="font-family: monospace;">'i'</span> can be used to
  initialize.  For similar spectra the <span style="font-family: monospace;">'a'</span><span style="font-family: monospace;">'c'</span> key combination may
  be used to recenter all lines and the a new <span style="font-family: monospace;">'f'</span> fit can be done.
  </p>
  <p>
  3.  For images which are two or three dimensional it is necessary to
  specify the image axis for the data vector and the number of pixels at each
  point across the vector direction to sum.  One way specify a vector is to
  use an image section to define a vector.  For example, to select column
  20:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rvidlines obj[20,*]
  </pre></div>
  <p>
  The alternative is to use the section parameter.  Below are some examples
  of the section parameter syntax for an image <span style="font-family: monospace;">"im2d"</span> which is 100x200
  and <span style="font-family: monospace;">"im3d"</span> which is 100x200x50.  On the left is the section string syntax
  and on the right is the image section
  </p>
  <div class="highlight-default-notranslate"><pre>
  Section parameter |  Image section      |  Description
  ------------------|---------------------|---------------------
  first line        |  im2d[*,1]          |  First image line
  middle column     |  im2d[50,*]         |  Middle image column
  last z            |  im3d[100,200,*]    |  Last image z vector
  middle last y     |  im3d[50,*,50]      |  Image y vector
  line 20           |  im2d[*,20]         |  Line 20
  column 20         |  im2d[20,*]         |  Column 20
  x 20              |  im2d[*,20]         |  Line 20
  y 20              |  im2d[20,*]         |  Column 20
  y 20 30           |  im2d[20,*,30]      |  Column 20
  z 20 30           |  im3d[20,30,*]      |  Image z vector
  x middle          |  im3d[*,100,25]     |  Middle of image
  y middle          |  im3d[50,*,25]      |  Middle of image
  z middle          |  im3d[50,100,*]     |  Middle of image
  </pre></div>
  <p>
  The most common usage should be <span style="font-family: monospace;">"middle line"</span>, <span style="font-family: monospace;">"middle column"</span> or <span style="font-family: monospace;">"middle z"</span>.
  </p>
  <p>
  The summing factors apply to the axes across the specified vector.  For
  3D images there may be one or two values.  The following shows which axes
  are summed, the second and third columns, when the vector axis is that shown
  in the first column.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Vector axis       |   Sum axis in 2D    |  Sum axes in 3D
  ------------------|---------------------|--------------------
       1            |         2           |      2 3
       2            |         1           |      1 3
       3            |         -           |      1 2
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_RVIDLINES">
  <dt><b>RVIDLINES V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='RVIDLINES' Line='RVIDLINES V2.11' -->
  <dd>This task will now work in the units of the input spectra.
  </dd>
  </dl>
  <dl id="l_RVIDLINES">
  <dt><b>RVIDLINES V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='RVIDLINES' Line='RVIDLINES V2.10.3' -->
  <dd>This is a new task in this version. 
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  center1d, fxcor, gtools, identify, keywpars, observatory,
  rvcorrect, rvreidlines
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ADDTIONAL PARAMETERS' 'CURSOR KEYS' 'DESCRIPTION' 'DATABASE RECORDS' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

.. _rvreidlines:

rvreidlines: Reidentify spectral lines and measure radial velocities
====================================================================

**Package: xrv**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rvreidlines reference images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_reference">
  <dt><b>reference</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reference' Line='reference' -->
  <dd>Spectrum with previously identified features to be used as reference for
  other spectra.  If there are multiple apertures, lines, or columns in the
  image a master reference is defined by the <i>section</i> parameter.
  The other apertures, lines, or columns selected by <i>step</i> are
  reidentified if needed.
  </dd>
  </dl>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of dispersion corrected spectral images in which the features in the
  reference image are to be reidentified.  In two and three dimensional
  images the reidentifications are done by matching apertures, lines,
  columns, or bands with those in the reference image.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Examine and fit features and velocities interactively?  If the task is run
  interactively a query (which may be turned off during execution) will be
  given for each vector reidentified after printing the results of the
  automatic determination and the user may chose to enter the interactive
  <b>rvidlines</b> task.
  </dd>
  </dl>
  <dl id="l_section">
  <dt><b>section = <span style="font-family: monospace;">"middle line"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='section' Line='section = "middle line"' -->
  <dd>If the reference image is not one dimensional or given as a one dimensional
  image section then this parameter selects the master reference image
  vector.  The master reference is used when reidentifying other vectors in
  the reference image or when other images contain apertures not present in
  the reference image.  This parameter also defines the direction
  (columns, lines, or z) of the image vectors to be reidentified.
  The section parameter may be specified directly as an image section or
  in one of the following forms
  <div class="highlight-default-notranslate"><pre>
  line|column|x|y|z first|middle|last|# [first|middle|last|#]]
  first|middle|last|# [first|middle|last|#] line|column|x|y|z
  </pre></div>
  where each field can be one of the strings separated by | except for #
  which is an integer number.  The field in [] is a second designator which
  is used with 3D data.  See the example section for <b>rvidlines</b> for
  examples of this syntax.  Abbreviations are allowed though beware that <span style="font-family: monospace;">'l'</span>
  is not a sufficient abbreviation.
  </dd>
  </dl>
  <dl id="l_newaps">
  <dt><b>newaps = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newaps' Line='newaps = yes' -->
  <dd>Reidentify new apertures in the images which are not in the reference
  image?  If no, only apertures found in the reference image will be
  reidentified in the other images.  If yes, the master reference spectrum
  is used to reidentify features in the new aperture and then the
  new aperture features will be added to the reference apertures.  All
  further identifications of the new aperture will then use this result.
  </dd>
  </dl>
  <dl id="l_override">
  <dt><b>override = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='override' Line='override = no' -->
  <dd>Override previous solutions?  If there are previous measurements for a
  particular image vector being identified, because of a previous
  <b>rvidlines</b> or <b>rvreidlines</b>, this parameter selects whether
  to simply skip the reidentification or do a reidentification and
  velocity measurement and overwrite the results in the logfile and database.
  </dd>
  </dl>
  <p>
  The following parameters are used for selecting and reidentifying additional
  lines, columns, or apertures in two dimensional formats.
  </p>
  <dl id="l_trace">
  <dt><b>trace = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trace' Line='trace = no' -->
  <dd>There are two methods for defining additional reference lines, columns, or
  bands in two and three dimensional format images as selected by the
  <i>step</i> parameter.  When <i>trace</i> is no the master reference line or
  column is used for each new reference vector.  When this parameter is yes
  then as the reidentifications step across the image the last reidentified
  features are used as the reference.  This <span style="font-family: monospace;">"tracing"</span> is useful if there is a
  coherent shift in the features such as with long slit spectra.  However,
  any features lost during the tracing will be lost for all subsequent lines
  or columns while not using tracing always starts with the initial set of
  reference features.
  </dd>
  </dl>
  <dl id="l_step">
  <dt><b>step = <span style="font-family: monospace;">"10"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='step' Line='step = "10"' -->
  <dd>The step from the reference aperture, line, column, or band used for
  selecting and/or reidentifying additional lines, columns, or bands in a two
  or three dimensional reference image.  For three dimensional images there
  may be two numbers to allow independent steps along different axes.  For
  multiaperture images the step is typically 1 while for long slit or
  Fabry-Perot images the step is large enough to map any significant changes
  in the feature positions.  If the step is zero then only the reference
  line, column, or band is used.
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
  <dl id="l_shift">
  <dt><b>shift = <span style="font-family: monospace;">"0"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shift' Line='shift = "0"' -->
  <dd>Shift in user coordinates to be added to the reference features before
  centering when stepping to other lines, columns, or bands in the reference
  image.  Generally no shift is used by setting the value to zero.
  The shift is used as a slope with positive values increasing towards
  larger line or column numbers.  This parameter is not used for
  reidentifications from the reference image to other images.
  If the image is three dimensional then two numbers may be specified
  for the two axes.
  </dd>
  </dl>
  <dl id="l_nlost">
  <dt><b>nlost = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlost' Line='nlost = 0' -->
  <dd>When reidentifying features by tracing, if the number of features not found
  in the new image vector exceeds this number then the reidentification
  record is not written to the logfile and database and the trace is terminated.  A warning is printed in the log and in the verbose output.
  </dd>
  </dl>
  <p>
  The following parameters define the finding and recentering of features.
  See also <b>center1d</b> and <b>rvidlines</b>.
  </p>
  <dl id="l_cradius">
  <dt><b>cradius = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cradius' Line='cradius = 5.' -->
  <dd>Centering radius in pixels.  If a reidentified feature falls further
  than this distance from the previous line or column when tracing or
  from the reference feature position when reidentifying a new image
  then the feature is not reidentified.
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = 10.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 10.' -->
  <dd>In order for a feature center to be determined, the range of pixel
  intensities around the feature must exceed this threshold.  This parameter
  is used to exclude noise peaks and terminate tracing when the signal
  disappears.  However, failure to properly set this parameter, particularly
  when the data values are very small due to normalization or flux
  calibration, is a common error leading to failure of the task.
  </dd>
  </dl>
  <p>
  The following parameters select and control the automatic addition of
  new features during reidentification.
  </p>
  <dl id="l_addfeatures">
  <dt><b>addfeatures = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='addfeatures' Line='addfeatures = no' -->
  <dd>Add new features from a line list during each reidentification?  If
  yes then the following parameters are used.  This function can be used
  to compensate for lost features from the reference solution, particularly
  when tracing.  Care should be exercised that misidentified features
  are not introduced.
  </dd>
  </dl>
  <dl id="l_coordlist">
  <dt><b>coordlist = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coordlist' Line='coordlist = ""' -->
  <dd>User coordinate list consisting of an ordered list of rest spectral line
  coordinates.
  </dd>
  </dl>
  <dl id="l_match">
  <dt><b>match = 10.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='match' Line='match = 10.' -->
  <dd>The maximum difference for a match between the feature coordinate function
  value and a coordinate in the coordinate list (after correction by the
  velocity).
  </dd>
  </dl>
  <dl id="l_maxfeatures">
  <dt><b>maxfeatures = 50</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxfeatures' Line='maxfeatures = 50' -->
  <dd>Maximum number of the strongest features to be selected automatically from
  the coordinate list.
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
  The following parameters determine the input and output of the task.
  </p>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"database"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "database"' -->
  <dd>Database containing the feature data for the reference image and in which
  the features for the reidentified images are recorded.
  </dd>
  </dl>
  <dl id="l_logfiles">
  <dt><b>logfiles = <span style="font-family: monospace;">"logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfiles' Line='logfiles = "logfile"' -->
  <dd>List of file in which to record the velocity results and to keep a
  processing log.  If a null file, <span style="font-family: monospace;">""</span>, is given then no log is kept.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print reidentification and velocity information on the standard output?
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
  <p>
  ADDTIONAL PARAMETERS
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
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Rvreidlines</b> takes spectral lines previously identified in a reference
  image and recorded in a database and identifies them in other spectra and
  determines a radial velocity.  If the images are
  two or three dimensional or multiaperture format and a <i>step</i> greater
  than zero is specified then additional vectors
  (lines/columns/bands/apertures) in the reference image will be reidentified
  from the initial master reference vector (as defined by an image section or
  <i>section</i> parameter) provided they have not been reidentified
  previously or the <i>override</i> flag is set.  For multiple aperture
  spectra images, called multiaperture, the step size is typically 1; i.e.
  reidentify features in all spectra.  For two and three dimensional images,
  such as long slit and Fabry-Perot spectra, the step(s) should be large enough
  to minimize execution time and storage requirements but small enough to
  follow shifts in the features (see the discussion below on tracing).  The
  set of reference identifications is applied to other images in the same
  lines, columns, bands, or apertures.  In multiaperture images the same
  apertures are matched in the reference image regardless of actual line
  order; i.e.  the apertures need not be in the same order or even have all
  apertures present.
  </p>
  <p>
  The reidentification of other features in other reference image vectors
  may be done in two ways selected by the parameter <i>trace</i>.  If not
  tracing, the initial reference vector is applied to the other selected
  vectors.  If tracing, the reidentifications are made with respect to the
  last set of identifications as successive steps away from the reference
  vector are made.  The tracing method is appropriate for two and three
  dimensional spatial images, such as long slit and Fabry-Perot spectra, in
  which the positions of features traced vary smoothly.  This allows
  following large displacements from the initial reference by using suitably
  small steps.  It has the disadvantage that features lost during the
  reidentifications will not propagate (unless the <i>addfeatures</i> option
  is used).  By not tracing, the original set of features is used for every
  other vector in the reference image.
  </p>
  <p>
  When reidentifying other vectors in the reference image the parameter
  <b>shift</b> may be used to add a shift(s) to the features positions
  before recentering.  The shift is added to lines, columns, or bands, greater
  than the current line, column, or band and subtracted if less.  If tracing
  the shifts are the same from step to step while if not tracing the
  shifts are added to the shifts from the previous step.  Thus, in both
  cases an approximation of a slope is used.  This allows large
  slopes in the features to be followed even when not tracing but the 
  shift value must be predetermined.
  </p>
  <p>
  When tracing, the parameter <i>nlost</i> is used to terminate the
  tracing whenever this number of features has been lost.  This parameter,
  in conjunction with the other centering parameters which define
  when a feature is not found, may be useful for tracing features
  which disappear before reaching the limits of the image.
  </p>
  <p>
  When reidentifying features in other images, the reference
  features are those from the same aperture, line, column, or band of the
  reference image.  However, if the <i>newaps</i> parameter is set
  apertures in multiaperture spectra which are not in the reference
  image may be reidentified against the master reference aperture and
  added to the list of aperture to be reidentified in other images.
  This is useful when specta with different aperture numbers are
  stored as one dimensional images.
  </p>
  <p>
  There are two centering algorithms; a flux bisecting algorithm called
  <b>center1d</b> and a gaussian fitting algorithm.  These algorithms
  are described in the help for <b>rvidlines</b>.  The algorithm used
  and whether the feature is emission or absorption is the same one used
  in the reference image.  The only caveat is that multiple gaussian
  fitting provided by the interactive <span style="font-family: monospace;">'b'</span> key in <b>rvidlines</b> is
  not done by this task and those lines will be fit by gaussians
  independently.
  </p>
  <p>
  When recentering, if a feature position shifts by more than the
  amount set by the parameter <i>cradius</i> from the starting position
  (possibly after adding a shift) or the feature strength (peak to valley) is
  less than the detection <i>threshold</i> then the new feature is discarded.
  The <i>cradius</i> parameter should be set large enough to find the correct
  peak in the presence of any shifts but small enough to minimize incorrect
  identifications.  The <i>threshold</i> parameter is used to eliminate
  identifications with noise.  Failure to set this parameter properly for the
  data (say if data values are very small due to a calibration or
  normalization operation) is the most common source of problems in using
  this task.
  </p>
  <p>
  In two and three dimensional images, though not multiaperture images, the
  number of lines, columns, or bands given by the parameter <i>nsum</i> are summed
  to form the one dimensional image vector in which the features are
  identified.  This increases the accuracy for reidentifying weak
  features.
  </p>
  <p>
  If the parameter <i>addfeatures</i> is set additional features may be added
  after the initial reidentification and velocity determination using a line
  list of rest wavelengths.  A maximum number of added features, a matching
  distance in user coordinates, and a minimum separation from other features
  are additional parameters.  This option is similar to that available in
  <b>rvidlines</b> and is described more fully in the help for that task.
  </p>
  <p>
  A statistics line is generated for each reidentified vector.  The line
  contains the name of the image being reidentified (which for two
  dimensional images includes the image section and for multiaperture
  spectra includes the aperture number), the number of features found
  relative to the number of features in the reference, the number of
  features used in the velocity determination (currently there is
  no rejection of lines) relative to the number found,  the
  mean pixel and user coordinate shfits relative to the reference
  coordinates, and the measured velocity and RMS in the velocity.
  The velocity is the heliocentric velocity if the necessary observation
  information in the image and observatory database are found.
  </p>
  <p>
  If the task is run with the <i>interactive</i> flag the statistics line
  is printed to the standard output (the terminal) and a query is
  made whether to fit the lines and measure the velocity interactively.
  A response
  of yes or YES will put the user in the interactive graphical mode
  of <b>rvidlines</b>.  See the description of this task for more
  information.  The idea is that one can monitor the statistics information,
  particularly the velocity RMS, and select only those which may be
  questionable to examine interactively.  A response of no or NO will
  continue on to the next spectrum.  The capitalized responses
  turn off the query and act as permanent response for all other
  reidentifications.
  </p>
  <p>
  This statistics line, including headers, is written to any specified
  log files.  The log information includes the image being
  reidentified and the reference image.
  In addition the set of lines, the observatory information used,
  and the computed observed and heliocentric velocities and redshifts
  are recorded.  This is the same information as is produced
  by <b>rvidlines</b>.
  </p>
  </section>
  <section id="s_database_records">
  <h3>Database records</h3>
  <p>
  The database specified by the parameter <i>database</i> is a directory of
  simple text files.  The text files have names beginning with 'id' followed
  by the entry name, usually the name of the image.  The database text files
  consist of a number of records.  A record begins with a line starting with the
  keyword <span style="font-family: monospace;">"begin"</span>.  The rest of the line is the record identifier.  Records
  read and written by <b>rvreidlines</b> have <span style="font-family: monospace;">"identify"</span> as the first word of the
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
  1.  To generate a rotation curve for a long slit spectrum of a
  galaxy first use <b>rvidlines</b> to mark some lines at the center of the
  galaxy.  If the velocities are to be absolute then you give the rest
  wavelengths and do a fit.  However to get velocities relative to the center
  use the measured wavelengths by simply accepting the prompted measured
  wavelengths.  Then run <b>rvreidlines</b>.  The <i>nsum</i> and <i>step</i>
  parameters allow controlling the summing size and spacing.
  </p>
  <div class="highlight-default-notranslate"><pre>
  rv&gt; rvid lsgal sec="mid col" nsum=5
          Mark lines and then quit.
  Write velocity data to the logfile (yes)?
  Write feature data to the database (yes)?
  rv&gt; rvreid lsgal "" sec="mid col" nsum=5 step=5 trace+ v+
  
  RVREIDLINES: NOAO/IRAF V2.10.3 valdes Sat 14:47:55 21-Aug-93
    Reference image = lsgal, New image = lsgal
   Image Data  Found    Fit  Pix Shift  User Shift Velocity    RMS
  lsgal[45,*]    7/7    7/7    -0.0181     -0.0212    -1.37   11.3
  lsgal[40,*]    7/7    7/7     0.0147      0.0193     1.34   8.73
  lsgal[35,*]    7/7    7/7     0.0931       0.116     8.01   9.16
  lsgal[30,*]    7/7    7/7    -0.0224     -0.0265    -1.78   27.6
  lsgal[25,*]    7/7    7/7     0.0558        0.07     4.83   33.7
  lsgal[20,*]    7/7    7/7    -0.0317     -0.0379    -3.08   33.6
  lsgal[15,*]    5/7    5/5      0.015      0.0201    0.799   43.7
  lsgal[10,*]    7/7    7/7      0.395       0.489     33.7   54.9
  lsgal[5,*]     4/7    4/4      -1.22       -1.51    -106.   84.3
  lsgal[55,*]    7/7    7/7      0.014      0.0184     1.41   10.5
  lsgal[60,*]    7/7    7/7    -0.0897      -0.109    -7.59   7.21
  lsgal[65,*]    7/7    7/7    -0.0109     -0.0122   -0.957   10.9
  lsgal[70,*]    7/7    7/7     -0.074     -0.0902    -6.55   14.6
  lsgal[75,*]    7/7    7/7   -0.00203    -0.00136    0.227   54.3
  lsgal[80,*]    6/7    6/6       0.08      0.0997     6.66   96.7
  lsgal[85,*]    6/7    6/6      0.289       0.357     27.2   104.
  lsgal[90,*]    6/7    6/6      0.459       0.568     40.5   33.2
  lsgal[95,*]    6/7    6/6      0.926        1.14     78.5   65.5
  lsgal[100,*    5/7    5/5      0.696        0.86     59.1   44.2
  rv&gt; match Vobs logfile | fields "" 2,6,11 | \
  &gt;&gt;&gt; graph point- mark=vebar szmark=-1
  </pre></div>
  <p>
  The last command extracts the Vobs results from the logfile using
  <b>match</b>, the column number, velocity, and mean error are extract
  using <b>fields</b>, and graphs the points with error bars.  One
  drawback to this method is that the nubmer of columns summed is
  constant and so the signal-to-noise decreases with the galaxy light.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_RVREIDLINES">
  <dt><b>RVREIDLINES V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='RVREIDLINES' Line='RVREIDLINES V2.11' -->
  <dd>This task will now work in the units of the input spectra.
  </dd>
  </dl>
  <dl id="l_RVREIDLINES">
  <dt><b>RVREIDLINES V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='RVREIDLINES' Line='RVREIDLINES V2.10.3' -->
  <dd>This task in new in the version.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  center1d, fxcor, keywpars, observatory, rvcorrect, rvidlines
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'DATABASE RECORDS' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

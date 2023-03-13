.. _observatory:

observatory: Examine and define observatory parameters
======================================================

**Package: noao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  observatory command obsid [images]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_command">
  <dt><b>command = <span style="font-family: monospace;">"list"</span> (set|list|images)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='command' Line='command = "list" (set|list|images)' -->
  <dd>Command option which is one of <span style="font-family: monospace;">"set"</span>, <span style="font-family: monospace;">"list"</span>, or <span style="font-family: monospace;">"images"</span>.  The set command
  sets the default observatory task parameters for the specified
  observatory.  The list command lists the observatory parameters for the
  specified observatory but does not modify the task parameters.  The images
  command lists the observatory parameters for a list of images.  The list
  and images commands examine and verify the observatory parameters applied
  by other tasks using the observatory database facility.
  </dd>
  </dl>
  <dl id="l_obsid">
  <dt><b>obsid = <span style="font-family: monospace;">"?"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obsid' Line='obsid = "?"' -->
  <dd>Observatory identification to be set, listed, or used as the default for
  images without the OBSERVAT keyword.  The observatory ID is one of those in
  the database (case ignored), the special string <span style="font-family: monospace;">"observatory"</span> to default to
  the environment variable <span style="font-family: monospace;">"observatory"</span> or the <i>observatory.observatory</i>
  parameter, <span style="font-family: monospace;">"obspars"</span> to select the parameters in the <b>observatory</b>
  task, or <span style="font-family: monospace;">"?"</span> to list the observatories defined in the database.
  </dd>
  </dl>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images to be examined with the <span style="font-family: monospace;">"images"</span> command.  The images are
  checked for the OBSERVAT keyword to determine the observatory parameters
  to be listed, otherwise the observatory given by <i>obsid</i> is used.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Verbose output?  Because there are a number of different ways in which
  observatory information is determine this option prints detailed
  information on how the observatory database and parameters are
  ultimately selected.
  </dd>
  </dl>
  <dl id="l_observatory">
  <dt><b>observatory</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observatory' Line='observatory' -->
  <dd>The default observatory used by tasks which use the special
  observatory identification <span style="font-family: monospace;">"observatory"</span>.  The value is one of the
  observatory names in the observatory database (case ignored)
  or the special value <span style="font-family: monospace;">"obspars"</span> to select the parameters defined in this
  task.  There is no default to force users to set it at least once.
  </dd>
  </dl>
  <dl id="l_name">
  <dt><b>name</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='name' Line='name' -->
  <dd>Observatory name.
  </dd>
  </dl>
  <dl id="l_longitude">
  <dt><b>longitude</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='longitude' Line='longitude' -->
  <dd>Observatory longitude given in degrees west.
  </dd>
  </dl>
  <dl id="l_latitude">
  <dt><b>latitude</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='latitude' Line='latitude' -->
  <dd>Observatory latitude in degrees.  Positive latitudes are north and negative
  latitudes are south.
  </dd>
  </dl>
  <dl id="l_altitude">
  <dt><b>altitude</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='altitude' Line='altitude' -->
  <dd>Observatory altitude in meters above sea level.
  </dd>
  </dl>
  <dl id="l_timezone">
  <dt><b>timezone</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='timezone' Line='timezone' -->
  <dd>Observatory time zone.  The time zone is the number of hours west of
  Greenwich or the number of hours to be added to local time to obtain
  Greenwich time.
  </dd>
  </dl>
  </section>
  <section id="s_environment_variables">
  <h3>Environment variables</h3>
  <dl id="l_obsdb">
  <dt><b>obsdb</b></dt>
  <!-- Sec='ENVIRONMENT VARIABLES' Level=0 Label='obsdb' Line='obsdb' -->
  <dd>This variable selects the observatory database.  If not defined it defaults
  to noao$lib/obsdb.dat.
  </dd>
  </dl>
  <dl id="l_observatory">
  <dt><b>observatory</b></dt>
  <!-- Sec='ENVIRONMENT VARIABLES' Level=0 Label='observatory' Line='observatory' -->
  <dd>This variable selects the observatory entry whenever a task uses the
  observatory name <span style="font-family: monospace;">"observatory"</span>.  If not defined the value of the task
  parameter <i>observatory.observatory</i> is used.
  </dd>
  </dl>
  </section>
  <section id="s_image_header_keywords">
  <h3>Image header keywords</h3>
  <p>
  The observatory identification for images is first sought under the
  image header keyword OBSERVAT.  This always takes precedence over any
  other means of defining the observatory.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  OBSERVATORY PARAMETERS IN THE NOAO PACKAGE
  </p>
  <p>
  Some astronomical data reduction and analysis tasks perform
  computations requiring information about where the data was observed.
  For example a number of <b>noao</b> tasks make corrections for the
  airmass.  Generally they look for an airmass in the image header and
  if it is not present they attempt to compute it from other image header
  parameters.  The information about time and telescope coordinates
  of the observation are often in the image header but the observatory
  latitude is not.  The task must get this information somehow.
  </p>
  <p>
  Prior to IRAF V2.10 tasks generally had explicit parameters, such as
  latitude, with default values pointing (using parameter redirection) to
  the parameter of the same name in the <b>observatory</b> task.  The
  user was required to know the values of the observatory parameters and
  manually change them for data from different observatories.  In V2.10
  an observatory database has been implemented.  Observatory parameters
  are stored in a simple text file and tasks obtain observatory related
  parameters by specifying an observatory identification.
  </p>
  <p>
  In general the information about the observatory should be directly
  associated with the image data.  Unless stated otherwise in the
  description of a task,  tasks which require observatory information
  will first look for the image header keyword OBSERVAT.  The value of
  this keyword is the observatory identification used to index the
  observatory database.  The task will then look up any observatory
  parameters it needs in the observatory database.  Data from
  observatories that support this keyword will, therefore, always use the
  correct observatory parameters without user intervention.  All
  observatories which export FITS image data are urged to adopt the
  OBSERVAT keyword (a keyword recommended by the FITS standard).
  </p>
  <p>
  For image data which do not identify the observatory in this way
  and in tasks which do not operate on images (such as astronomical
  calculator tools), the observatory must be specified by the user.
  Most tasks provide an <span style="font-family: monospace;">"observatory"</span> parameter which either directly
  selects the observatory or use special values for defining the
  observatory with an environment variable or the parameters
  from the <b>observatory</b> task.
  </p>
  <p>
  An observatory is specified by the identification name used in the
  observatory database.  The names in the database may be listed using
  the <b>observatory</b> task as described below.  If the desired observatory
  is not in the database a user may copy/create their own database and
  select it with the environment variable <span style="font-family: monospace;">"obsdb"</span>, modify the standard
  database if allowed (any changes to the distributed version should
  be forwarded to iraf$noao.edu), or use the special observatory name
  <span style="font-family: monospace;">"obspars"</span>.  The last option directly uses the parameters in the
  <b>observatory</b> task which can be set to any values using the normal
  parameter editing mechanism.
  </p>
  <p>
  The default value for the observatory parameter in a task is generally
  <span style="font-family: monospace;">"observatory"</span>.  This special name directs the task to look first
  for the environment variable of the same name and then at the
  <i>observatory</i> parameter of the <b>observatory</b> task.  The environment
  variable allows users or sites to set the default observatory in their
  login files and site defaults.  Also it is simple to change the
  default observatory either with a <b>reset</b> command or the
  <b>observatory</b> command.
  </p>
  <p>
  The observatory database is selected by the environment variable
  <span style="font-family: monospace;">"obsdb"</span>.  The default when the variable is not defined is the
  <b>noao</b> package library database file <span style="font-family: monospace;">"noao$lib/obsdb.dat"</span>.  The use
  of an environment variable allows users to permanently change the
  default database in the OS environment (when IRAF has access to it such
  as in UNIX systems) or in the startup IRAF environment as set in the
  <span style="font-family: monospace;">"login.cl"</span> or <span style="font-family: monospace;">"loginuser.cl"</span> files.  One can, of course, change it
  during a session with the set or reset commands.  For sites which want
  to customize the observatory mechanism the environment variables can
  also be set and changed in the files <span style="font-family: monospace;">"hlib$zzsetenv.def"</span>,
  <span style="font-family: monospace;">"noao$lib/zzsetenv.def"</span>, and the template login file <span style="font-family: monospace;">"hlib$login.cl"</span>.
  </p>
  <p>
  An observatory database file consist of a simple list of keyword=value
  pairs with arbitrary whitespace allowed.  An observatory entry begins
  with the observatory keyword and extends to the next observatory
  keyword or the end of the file.  The observatory identification should
  be the same as the string used in the OBSERVAT image header parameter
  for data from that observatory.  The default file noao$lib/obsdb.dat
  begins as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Observatory Parameters.  Taken from the Almanac.
  #
  # Observatories wishing to be added or make changes in the default
  # distributed database should send information to iraf@noao.edu.
  
  observatory = "kpno"
          name = "Kitt Peak National Observatory"
          longitude = 111:36.0
          latitude = 31:58.8
          altitude = 2120.
          timezone = 7
  
  observatory = "ctio"
          &lt;etc&gt;
  </pre></div>
  <p>
  In summary, access to observatory parameters is now done by referencing
  the image header keyword OBSERVAT and, if not defined, determine the
  observatory name from a task parameter.  The environment variables
  <span style="font-family: monospace;">"observatory"</span> and <span style="font-family: monospace;">"obsdb"</span> can be set by the user to select alternate
  observatories and observatory database files.  For data without an
  observatory entry the observatory can be set to <span style="font-family: monospace;">"obspars"</span> or the user
  may make their own observatory database.
  </p>
  <p>
  THE OBSERVATORY TASK
  </p>
  <p>
  The <b>observatory</b> task serves a number of functions.  It may be used to
  examine the observatory database, verify the observatory parameters which
  will be used by other tasks, particularly those operating on images, set
  the default observatory if not defined by other means, set observatory
  parameters explicitly, especially when there is no observatory database
  entry, and as a parameter set for tasks which explicitly reference
  observatory parameters.  The <b>verbose</b> parameter also provides a
  detailed check of the steps used to determine the observatory database,
  observatory identification, and observatory parameters.
  </p>
  <p>
  The <i>command</i> parameter takes the values <span style="font-family: monospace;">"set"</span>, <span style="font-family: monospace;">"list"</span>, or <span style="font-family: monospace;">"images"</span>.
  The <i>obsid</i> parameter supplies the observatory identification and the
  <i>images</i> parameter is used to specify a list of images for the <span style="font-family: monospace;">"images"</span>
  command.  The parameters are query parameters and so may be either queried
  or simply typed on the command line.
  </p>
  <p>
  The <span style="font-family: monospace;">"set"</span> command prints the observatory parameters for the specified
  observatory and sets many of these in the <b>observatory</b> task
  parameters.  This command is used to set the default observatory parameters
  for tasks where images are not used, the images do not contain the
  observatory id, or direct references to specific parameters with parameter
  redirection (for example <span style="font-family: monospace;">")observatory.latitude"</span>) are used.
  </p>
  <p>
  The <span style="font-family: monospace;">"list"</span> command is similar to the <span style="font-family: monospace;">"set"</span> command except the task parameters
  are not modified.  It is used to list observatory parameters.  It is also
  use with the special observatory identifications to list the entries in
  an observatory database and verify the observatory to be used by
  tasks which do not operate on images.  The special value <span style="font-family: monospace;">"?"</span> lists
  the entries in the database.  The special value <span style="font-family: monospace;">"observatory"</span> lists
  the observatory defined by the <span style="font-family: monospace;">"observatory"</span> environment variable or
  that given by the <i>observatory.observatory</i> parameter.  The special
  value <span style="font-family: monospace;">"obspars"</span> simply lists the observatory task parameters.
  </p>
  <p>
  The <span style="font-family: monospace;">"images"</span> command lists the observatory information applicable to
  one or more images.  In particular, the observatory identification is
  first sought in OBSERVAT image header keyword and, if not found, the
  <i>obsid</i> parameter is used.  Often the default observatory is
  <span style="font-family: monospace;">"observatory"</span> to follow the same search path used by other tasks.
  </p>
  <p>
  The <i>verbose</i> parameter prints additional detailed information.  It
  prints the database used and whether it is selected by default
  (noao$lib/obsdb.dat) or by the <span style="font-family: monospace;">"obsdb"</span> environment variable.  When the
  observatory is defined as <span style="font-family: monospace;">"observatory"</span> it indicates whether the
  observatory is defined by the environment variable <span style="font-family: monospace;">"observatory"</span> or by the
  observatory task.  When listing images it prints the OBSERVAT keyword or
  the default observatory assigned.
  </p>
  <p>
  For observatories not in a database the name, latitude, longitude,
  altitude, and time zone parameters may be set using <b>eparam</b>.
  The observatory id must be set to <span style="font-family: monospace;">"obspars"</span> in this case.
  These parameters will then be referenced by other tasks in which
  the observatory is specified as <span style="font-family: monospace;">"obspars"</span>.  This allows arbitrary
  observatory parameters to be set without creating or modifying
  an observatory database.  However, it is advisable to create a
  local database and also send the observatory information to the
  IRAF group at NOAO for inclusion in the default database.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  List the observatory entries in the database:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; observatory list ? v+
  Using default observatory database: noao$lib/obsdb.dat
  
  default: Kitt Peak National Observatory
  kpno: Kitt Peak National Observatory
  ctio: Cerro Tololo Interamerican Observatory
  eso: European Southern Observatory
  lick: Lick Observatory
  mmt: Whipple Observatory
  cfht: Canada-France-Hawaii Telescope
  lapalma: Roque de los Mucachos, La Palma
  </pre></div>
  <p>
  2.  Set the observatory parameters for Cerro Tololo:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; observatory set ctio
  Observatory parameters for Cerro Tololo...
          observatory = ctio
          timezone = 5
          altitude = 2215.
          latitude = -30:09.9
          longitude = 70:48.9
           name = 'Cerro Tololo Interamerican Observatory'
  cl&gt; lpar observatory
        command = "set"           Command (set|list|images)
       argument = ctio            Observatory or images
   (observatory = "ctio")         Observatory identification
          (name = "Cerro Tololo...") Observatory name
     (longitude = 70.815)         Observatory longitude (degrees)
      (latitude = -30.165)        Observatory latitude (degrees)
      (altitude = 2215.)          Observatory altitude (meters)
      (timezone = 4)              Observatory time zone
       (verbose = no)             Verbose output?
          (mode = "q")
  </pre></div>
  <p>
  3.  Set the observatory parameters to use the environment variable
  <span style="font-family: monospace;">"observatory"</span> and verify it.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set observatory=cfht
  cl&gt; observatory list observatory
  Observatory parameters for Canada-France-Hawaii Telescope
          observatory = cfht
          timezone = 10
          altitude = 4215
          latitude = 19:49.6
          longitude = 155:28.3
          name = 'Canada-France-Hawaii Telescope'
  </pre></div>
  <p>
  4.  Change the default observatory database and verify verbosely:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set observatory="sco"
  cl&gt; set obsdb="/local/iraf/obsdb.dat"
  cl&gt; type obsdb$
  # Local Observatory Parameters.
  
  observatory = "sco"
          name = "Small College Observatory"
          longitude = 100:20.0
          latitude = 35:58.8
          altitude = 212.
          timezone = 6
  cl&gt; observ set observatory v+
  Using database defined by 'obsdb' environment variable:
          /tmp/test/obsdb.dat
  Using obs... defined by 'obs...' environment variable: sco
  Using observatory parameters for database entry: sco
  Observatory parameters for Small College Observatory
          observatory = sco
          timezone = 6
          altitude = 212.
          latitude = 35:58.8
          longitude = 100:20.0
          name = 'Small College Observatory'
  </pre></div>
  <p>
  5.  List the observatory assigned to some images with a default observatory
  determined either by the <span style="font-family: monospace;">"observatory"</span> environment variable or that set
  in the observatory task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; observ images observatory dev$pix,demoobj1
  Observatory parameters for Small College Observatory
          observatory = sco
          timezone = 6
          altitude = 212.
          latitude = 35:58.8
          longitude = 100:20.0
          name = 'Small College Observatory'
          Images: dev$pix (default observatory)
  Observatory parameters for Kitt Peak National Observatory
          observatory = kpno
          timezone = 7
          altitude = 2120.
          latitude = 31:58.8
          longitude = 111:36.0
          name = 'Kitt Peak National Observatory'
          Images: demoobj1 (OBSERVAT keyword)
  </pre></div>
  <p>
  6.  Set explicit observatory parameters:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epar observatory
  &lt;set observatory parameters&gt;
  cl&gt; observ list obspars
  Observatory parameters for North Pole
          observatory = obspars
          timezone = 0
          altitude = 0.
          latitude = 90.
          longitude = 0.
          name = 'North Pole'
  </pre></div>
  <p>
  7.  Use observatory parameters in expressions:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; observ set kpno
  Observatory parameters for Kitt Peak National Observatory
          observatory = kpno
          timezone = 7
          altitude = 2120.
          latitude = 31:58.8
          longitude = 111:36.0
          name = 'Kitt Peak National Observatory'
  cl&gt; = observ.lat
  31.98
  cl&gt; = sin (3.14159/180 * observ.lat)
  0.52962280742153
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  Tasks in astutil, imred, onedspec, and twodspec.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ENVIRONMENT VARIABLES' 'IMAGE HEADER KEYWORDS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

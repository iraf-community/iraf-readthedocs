.. _ccdinstrument:

ccdinstrument: Review and edit instrument translation files
===========================================================

**Package: quadred**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  ccdinstrument images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images to be verified or used to setup a CCD instrument translation
  file.
  </dd>
  </dl>
  <dl id="l_instrument">
  <dt><b>instrument = <span style="font-family: monospace;">")_.instrument"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='instrument' Line='instrument = ")_.instrument"' -->
  <dd>CCD instrument translation file.  The default is to use the translation
  file defined in the <b>ccdred</b> package parameters.  Note that one would
  need write permission to update this file though the task has a write
  command to save any changes to a different file.
  </dd>
  </dl>
  <dl id="l_ssfile">
  <dt><b>ssfile = <span style="font-family: monospace;">")_.ssfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ssfile' Line='ssfile = ")_.ssfile"' -->
  <dd>Subset translation file.  The default is to use the file defined in
  the <b>ccdred</b> package parameters.
  </dd>
  </dl>
  <dl id="l_edit">
  <dt><b>edit = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='edit' Line='edit = yes' -->
  <dd>Edit the instrument translation file?  If <span style="font-family: monospace;">"yes"</span> an interactive
  mode is entered allowing translation parameters to be modified while if
  <span style="font-family: monospace;">"no"</span> the task is simply used to verify the translations noninteractively.
  </dd>
  </dl>
  <dl id="l_parameters">
  <dt><b>parameters = <span style="font-family: monospace;">"basic"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='parameters' Line='parameters = "basic"' -->
  <dd>Parameters to be displayed.  The choices are <span style="font-family: monospace;">"basic"</span> to display only the
  most basic parameters (those needed for the simplest automation of
  <b>ccdred</b> tasks),  <span style="font-family: monospace;">"common"</span> to display the common parameters used
  by the package (most of these are keywords to be written to the image
  rather than translated), and <span style="font-family: monospace;">"all"</span> to display all the parameters
  referenced by the package including the most obscure.  For most uses
  the <span style="font-family: monospace;">"basic"</span> set is all that is important and the other options are
  included for completeness.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The purpose of this task is to provide an interface to simplify setting
  up CCD instrument translation files and to verify the translations
  for a set of images.  Before this task was written users who needed to
  set up translation files for new instruments and observatories had
  to directly create the files with an editor.  Many people encountered
  difficulties and were prone to errors.  Also there was no task that
  directly verified the translations though <b>ccdlist</b> provided some
  clues.
  </p>
  <p>
  The <b>ccdred</b> package was designed to make intelligent use of
  information in image headers for determining things such as image
  calibration or object type and exposure times.  While the package may
  be used without this capability it is much more convenient to be
  able to use information from the image.  The package was also intended
  to be used with many different instruments, detectors, and observatories.
  The key to providing image header access across different observatories
  is the ability to translate the needs of the package to the appropriate
  keywords in the image header.  This is done through a file called
  an <span style="font-family: monospace;">"instrument translation file"</span>.  For a complete description of
  this file and other instrument setup features of the package see
  <b>ccdred.instruments</b>.
  </p>
  <p>
  The instrument translation file translates the parameter names used by
  the <b>ccdred</b> package into image specific parameters and also
  supplies default values for parameters.  The translation proceeds as
  follows.  When a package task needs a parameter for an image, for
  example <span style="font-family: monospace;">"imagetyp"</span>, it looks in the instrument translation file.  If
  the file is not found or none is specified then the image header
  keyword that is requested is assumed to have the same name.  If an
  instrument translation file is defined then the requested parameter is
  translated to an image header keyword, provided a translation entry is
  given.  If no translation is given the package name is used.  For
  example the package parameter <span style="font-family: monospace;">"imagetyp"</span> might be translated to
  <span style="font-family: monospace;">"data-typ"</span> (the old NOAO CCD keyword).  If the parameter is not found
  then the default value specified in the translation file, if present,
  is returned.
  </p>
  <p>
  For recording parameter information in the header, such
  as processing flags, translation is also used.  For example, if the
  flag specifying that the image has been corrected by a flat field is to
  be set then the package parameter name <span style="font-family: monospace;">"flatcor"</span> might be translated to
  <span style="font-family: monospace;">"ff-flag"</span>.  If no translation is given then the new image header
  parameter is entered as <span style="font-family: monospace;">"flatcor"</span>.
  </p>
  <p>
  The CCD image type requires a second level of translation also defined
  in the translation file.  Once the image keyword which identifies the
  type of CCD image, for example a flat field or object, is translated
  to an imahe keyword the specific
  string value must be translated to one of the CCD image types used
  by the package.  The translation works in the same way, the specific
  string found is translated to the <b>ccdred</b> type and returned to
  the task.  This translation is tricky in that the exact string
  including all spaces and capitalizations must be correctly defined
  in the translation file.  The <b>ccdinstrument</b> allows doing
  this automatically thus minimizing typing errors.
  </p>
  <p>
  The basic display format of the task is a table of five columns
  giving the parameter name used by the package, the image keyword
  to which it is translated, the default value (if any), the value
  the task will receive for the current image after translation,
  and the actual keyword value in the image.  A <span style="font-family: monospace;">"?"</span> is printed if
  a value cannot be determined.  The idea of the task is to make sure
  that the value a <b>ccdred</b> task sees is the correct one and if not
  to modify the translation appropriately.  In verify mode when the
  <b>edit</b> parameter is not set the translation table is simply
  printed for each input image.
  </p>
  <p>
  In edit mode the user interactively gives commands at the ccdinstrument
  prompt to display or modify keywords.  The modifications can then be
  written to the instrument file or saved in a private copy.  The
  list of commands is shown below and may be printed using ? or help.
  </p>
  <div class="highlight-default-notranslate"><pre>
                          CCDINSTRUMENT COMMANDS
  
  ?           Print command summary
  help        Print command summary
  imheader    Page image header
  instrument  Print current instrument translation file
  next        Next image
  newimage    Select a new image
  quit        Quit
  read        Read instrument translation file
  show        Show current translations
  write       Write instrument translation file
  
  translate   Translate image string selected by the imagetyp
              parameter to one of the CCDRED types given as an
              argument or queried:
              object, zero, dark, flat, comp, illum, fringe, other
  </pre></div>
  <p>
  The following are CCDRED parameters which may be translated.  You are
  queried for the image keyword to use or it may be typed after the command.
  An optional default value (returned if the image does not contain the
  keyword) may be typed as the second argument of the command.
  </p>
  <div class="highlight-default-notranslate"><pre>
          BASIC PARAMETERS
  imagetyp        Image type parameter (see also translate)
  subset          Subset or filter parameter
  exptime         Exposure time
  darktime        Dark time (may be same as the exposure time)
  </pre></div>
  <p>
  The commands may be followed by values such as file names for some of
  the general commands or the keyword and default value for the parameters
  to be translated.  Note this is the only way to specify a default value.
  If no arguments are given the user is prompted with the current value
  which may then be changed.
  </p>
  <p>
  The set of parameters shown above are only those considered <span style="font-family: monospace;">"basic"</span>.
  In order to avoid confusion the task can limit the set of parameters
  displayed.  Without going into great detail, it is only the basic
  parameters which are generally required to have valid translations to
  allow the package to work well.  However, for completeness, and if someone
  wants to go wild with translations, further parameters may be displayed
  and changed.  The parameters displayed is controlled by the <i>parameters</i>
  keyword.  The additional parameters not shown above are:
  </p>
  <div class="highlight-default-notranslate"><pre>
          USEFUL DEFAULT GEOMETRY PARAMETERS
  biassec         Bias section (often has a default value)
  trimsec         Trim section (often has a default value)
  
          COMMON PROCESSING FLAGS
  fixpix          Bad pixel replacement flag
  overscan        Overscan correction flag
  trim            Trim flag
  zerocor         Zero level correction flag
  darkcor         Dark count correction flag
  flatcor         Flat field correction flag
  
          RARELY TRANSLATED PARAMETERS
  ccdsec          CCD section
  datasec         Data section
  fixfile         Bad pixel file
  
  fringcor        Fringe correction flag
  illumcor        Ilumination correction flag
  readcor         One dimensional zero level read out correction
  scancor         Scan mode correction flag
  nscanrow        Number of scan rows
  
  illumflt        Ilumination flat image
  mkfringe        Fringe image
  mkillum         Iillumination image
  skyflat         Sky flat image
  
  ccdmean         Mean value
  ccdmeant        Mean value compute time
  fringscl        Fringe scale factor
  ncombine        Number of images combined
  date-obs        Date of observations
  dec             Declination
  ra              Right Ascension
  title           Image title
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To verify the translations for a set of images using the default
  translation file:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; setinst "" review-
  cl&gt; ccdinst dev$pix edit-
  Image: dev$pix
  Instrument file:
  Subset file: subsets
  
  CCDRED    IMAGE     DEFAULT   CCDRED    IMAGE
  PARAM     KEYWORD   VALUE     VALUE     VALUE
  --------------------------------
  imagetyp  imagetyp            none      ?
  subset    subset                        ?
  exptime   exptime             ?         ?
  darktime  darktime            ?         ?
  
  cl&gt; setinst "" site=kpno dir=ccddb$ review-
  cl&gt; ccdinst dev$pix edit-
  Image: dev$pix
  
  Instrument file: ccddb$kpno/camera.dat
  Subset file: subsets
  
  CCDRED    IMAGE     DEFAULT   CCDRED    IMAGE
  PARAM     KEYWORD   VALUE     VALUE     VALUE
  --------------------------------
  imagetyp  data-typ            object    OBJECT (0)
  subset    f1pos               2         2
  exptime   otime               600       600
  darktime  ttime               600       600
  </pre></div>
  <p>
  2.  Set up an  instrument translation file from scratch.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ccdinst ech???.imh instr=myccd edit+
  Warning: OPEN: File does not exist (myccd)
  Image: ech001.imh
  Instrument file: myccd
  Subset file: subsets
  
  CCDRED    IMAGE     DEFAULT   CCDRED    IMAGE
  PARAM     KEYWORD   VALUE     VALUE     VALUE
  ------------------------------------------------------
  imagetyp  imagetyp            none      ?
  subset    subset                        ?
  exptime   exptime             ?         ?
  darktime  darktime            ?         ?
  
  ccdinstrument&gt; imagetyp
  Image keyword for image type (imagetyp): ccdtype
  imagetyp  ccdtype             unknown   BIAS
  ccdinstrument&gt; translate
  CCDRED image type for 'BIAS' (unknown): zero
  imagetyp  ccdtype             zero      BIAS
  ccdinstrument&gt; subset
  Image keyword for subset parameter (subset): filters
  subset    filters             1         1 0
  ccdinstrument&gt; exptime integ
  exptime   integ               0.        0.
  ccdinstrument&gt; darktime integ
  darktime  integ               0.        0.
  ccdinstrument&gt; show
  Image: ech001.imh
  Instrument file: myccd
  Subset file: subsets
  
  CCDRED    IMAGE     DEFAULT   CCDRED    IMAGE
  PARAM     KEYWORD   VALUE     VALUE     VALUE
  ------------------------------------------------------
  imagetyp  ccdtype             zero      BIAS
  subset    filters             1         1 0
  exptime   integ               0.        0.
  darktime  integ               0.        0.
  
  ccdinstrument&gt; next
  Image: ech002.imh
  Instrument file: myccd
  Subset file: subsets
  
  CCDRED    IMAGE     DEFAULT   CCDRED    IMAGE
  PARAM     KEYWORD   VALUE     VALUE     VALUE
  ------------------------------------------------------
  imagetyp  ccdtype             unknown   PROJECTOR FLAT
  subset    filters             1         1 0
  exptime   integ               20.       20.
  darktime  integ               20.       20.
  
  ccdinstrument&gt; trans
  CCDRED image type for 'PROJECTOR FLAT' (unknown): flat
  imagetyp  ccdtype             flat      PROJECTOR FLAT
  ccdinstrument&gt; next
  Image: ech003.imh
  Instrument file: myccd
  Subset file: subsets
  
  CCDRED    IMAGE     DEFAULT   CCDRED    IMAGE
  PARAM     KEYWORD   VALUE     VALUE     VALUE
  ------------------------------------------------------
  imagetyp  ccdtype             unknown   COMPARISON
  subset    filters             1         1 0
  exptime   integ               300       300
  darktime  integ               300       300
  
  ccdinstrument&gt; translate comp
  imagetyp  ccdtype             comp      COMPARISON
  ccdinstrument&gt; next
  Image: ech004.imh
  Instrument file: myccd
  Subset file: subsets
  
  CCDRED    IMAGE     DEFAULT   CCDRED    IMAGE
  PARAM     KEYWORD   VALUE     VALUE     VALUE
  ------------------------------------------------------
  imagetyp  ccdtype             unknown   OBJECT
  subset    filters             1         1 0
  exptime   integ               3600      3600
  darktime  integ               3600      3600
  
  ccdinstrument&gt; translate object
  imagetyp  ccdtype             object    OBJECT
  ccdinstrument&gt; inst
  imagetyp                      ccdtype
  BIAS                          zero
  subset                        filters
  exptime                       integ
  darktime                      integ
  'PROJECTOR FLAT'              flat
  COMPARISON                    comp
  OBJECT                        object
  
  ccdinstrument&gt; next
  Update instrument file myccd (yes)?
  </pre></div>
  <p>
  3.  Set default geometry parameters.  Note that to set a default the
  arguments must be on the command line.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cc&gt; ccdinst ech001 instr=myccd param=common edit+
  Image: ech001
  Instrument file: myccd
  Subset file: subsets
  
  CCDRED    IMAGE     DEFAULT   CCDRED    IMAGE
  PARAM     KEYWORD   VALUE     VALUE     VALUE
  ------------------------------------------------------
  imagetyp  ccdtype             zero      BIAS
  subset    filters             1         1 0
  exptime   integ               0.        0.
  darktime  integ               0.        0.
  
  biassec   biassec             ?         ?
  trimsec   trimsec             ?         ?
  
  fixpix    fixpix              no        ?
  overscan  overscan            no        ?
  trim      trim                no        ?
  zerocor   zerocor             no        ?
  darkcor   darkcor             no        ?
  flatcor   flatcor             no        ?
  
  ccdinstrument&gt; biassec biassec [803:830,*]
  biassec   biassec   [803:830,*]  [803:830,*]  ?
  ccdinstrument&gt; trimsec trimsec [2:798,2:798]
  trimsec   trimsec   [2:798,2:798]  [2:798,2:798]  ?
  ccdinstrument&gt; instr
  trimsec                       trimsec  [2:798,2:798]
  biassec                       biassec  [803:830,*]
  imagetyp                      ccdtype
  BIAS                          zero
  subset                        filters
  exptime                       integ
  darktime                      integ
  'PROJECTOR FLAT'              flat
  COMPARISON                    comp
  OBJECT                        object
  
  ccdinstrument&gt; q
  Update instrument file myccd (yes)?
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  instruments, setinstrument
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

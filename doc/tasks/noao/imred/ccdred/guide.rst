.. _guide:

guide: Introductory guide to using the CCDRED package
=====================================================

**Package: ccdred**

.. raw:: html

  <section id="s_1__introduction">
  <h3>1. introduction</h3>
  <p>
       This guide provides a brief description of the IRAF CCD reduction
  package <b>ccdred</b> and examples of reducing simple CCD data.  It is a
  generic guide in that it is not tied to any particular type of data.
  There may be more specific guides (or <span style="font-family: monospace;">"cookbooks"</span>) for your data.
  Detailed descriptions of the tasks and features of the package are
  provided in the help documentation for the package.
  </p>
  <p>
       The purpose of the CCDRED package is to provide tools for the easy
  and efficient reduction of CCD images.  The standard reduction
  operations are replacement of bad columns and lines by interpolation
  from neighboring columns and lines, subtraction of a bias level
  determined from overscan or prescan columns or lines, subtraction of a
  zero level using a zero length exposure calibration image, subtraction
  of a dark count calibration image appropriately scaled to the dark time
  exposure, division by a scaled flat field calibration image, division
  by an iillumination image (derived from a blank sky image), subtraction
  of a scaled fringe image (also derived from a blank sky image), and
  trimming the image of unwanted lines or columns such as the overscan
  strip.  Any set of operations may be done simultaneously over a list of
  images in a highly efficient manner.  The reduction operations are
  recorded in the image header and may also be logged on the terminal and
  in a log file.
  </p>
  <p>
       The package also provides tools for combining multiple exposures
  of object and calibration images to improve the statistical accuracy of
  the observations and to remove transient bad pixels.  The combining
  operation scales images of different exposure times, adjusts for
  variable sky background, statistically weights the images by their
  signal-to-noise, and provides a number of useful algorithms for
  detecting and rejecting transient bad pixels.
  </p>
  <p>
       Other tasks are provided for listing reduction information about
  the images, deriving secondary calibration images (such as sky
  corrected flat fields or iillumination correction images), and easily
  setting the package parameters for different instruments.
  </p>
  <p>
       There are several important features provided by the package to
  make the reduction of CCD images convenient; particularly to minimize
  record keeping.  One of these is the ability to recognize the different
  types of CCD images.  This ability allows the user to select a certain
  class of images to be processed or listed and allows the processing
  tasks to identify calibration images and process them differently from
  object images.  The standard CCD image types are <i>object</i>,
  <i>zero</i> level, <i>dark</i> count, and <i>flat</i> field.  For more on
  the image types see <b>ccdtypes</b>.
  </p>
  <p>
       The tasks can also identify the different filters (or other subset
  parameter) which require different flat field images.  This means you don't
  have to separate the images by filter and process each set separately.
  This feature is discussed further in <b>subsets</b>.
  </p>
  <p>
       The tasks keep track of the reduction steps completed on each
  image and ignore images which have been processed.  This feature,
  along with recognizing the image types and subsets, makes it possible to
  specify all the images to a task with a wildcard template, such as
  <span style="font-family: monospace;">"*.imh"</span>, rather than indicating each image by name.  You will find this
  extremely important with large sets of observations.
  </p>
  <p>
       A fundamental aspect of the package is that the processing
  modifies the images.  In other words, the reduction operations are
  performed directly on the image.  This <span style="font-family: monospace;">"feature"</span> further simplifies
  record keeping, frees the user from having to form unique output image
  names, and minimizes the amount of disk space required.  There
  are two safety features in this process.  First, the modifications do
  not take effect until the operation is completed on the image.  This
  allows you to abort the task without messing up the image data and
  protects data if the computer crashes.  The second feature is that
  there is a package parameter which may be set to make a backup of the
  input data with a particular prefix such as <span style="font-family: monospace;">"orig"</span> or <span style="font-family: monospace;">"imdir$"</span>.  This
  backup feature may be used when there is sufficient disk space, when learning
  to use the package, or just to be cautious.
  </p>
  <p>
       In a similar effort to efficiently manage disk space, when combining
  images into a master object or calibration image there is an option to
  delete the input images upon completion of the combining operation.
  Generally this is desirable when there are many calibration exposures,
  such as zero level or flat field images, which are not used after they
  are combined into a final calibration image.
  </p>
  <p>
       The following sections guide you through the basic use of the
  <b>ccdred</b> package.  Only the important parameters which you might
  want to change are described.  It is assumed that the support personnel
  have created the necessary instrument files (see <b>instruments</b>)
  which will set the default parameters for the data you will be
  reducing.  If this is not the case you may need to delve more deeply
  into the details of the tasks.  Information about all the parameters
  and how the various tasks operate are given in the help documentation
  for the tasks and in additional special help topics.  Some useful help
  documentation is indicated in the discussion and also in the
  <b>References</b> section.
  </p>
  </section>
  <section id="s_2__getting_started">
  <h3>2. getting started</h3>
  <p>
       The first step is to load <b>ccdred</b>.  This is done by loading
  the <b>noao</b> package, followed by the image reduction package
  <b>imred</b>, and finally the <b>ccdred</b> package.  Loading a
  package consists of typing its name.  Note that some of these packages may be
  loaded automatically when you logon to IRAF.
  </p>
  <p>
       When you load the <b>ccdred</b> package the menu of tasks or commands
  is listed.  This appears as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdred
    badpiximage       ccdtest           mkfringecor       setinstrument
    ccdgroups         combine           mkillumcor        zerocombine
    ccdhedit          cosmicrays        mkillumflat
    ccdlist           darkcombine       mkskycor
    ccdproc           flatcombine       mkskyflat
  </pre></div>
  <p>
  A summary of the tasks and additional help topics is obtained by typing:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help
  </pre></div>
  <p>
  This list and how to get additional help on specific topics is described
  in the <b>References</b> section at the end of this guide.
  </p>
  <p>
       The first command to use is <b>setinstrument</b>, which sets the package
  appropriately for the CCD images to be reduced.  The support personnel
  should tell you the instrument identification, but if not a list
  of known instruments may be listed by using <span style="font-family: monospace;">'?'</span> for the instrument name.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; setinstrument
  Instrument ID (type ? for a list) <i>&lt;enter instrument id or ?&gt;</i>
      &lt;Set ccdred package parameters using eparam&gt;
      &lt;Set ccdproc task parameters using eparam&gt;
  </pre></div>
  <p>
  This task sets the default parameters and then allows you to modify the
  package parameters and the processing parameters using the parameter
  editor <b>eparam</b>.  If you are not familiar with <b>eparam</b> see the
  help or CL introduction documentation.  For most terminals you move up
  and down through the parameters with the terminal arrow keys, you
  change the parameters by simply typing the desired value, and you exit
  with control Z or control D.  Note that you can change parameters for
  any task at any time with <b>eparam</b> and you do not have to run
  <b>setinstrument</b> again, even if you logout, until you need to reduce
  data from a different instrument.
  </p>
  <p>
       The <b>ccdred</b> package parameters control general I/O functions of
  the tasks in the package.  The parameters you might wish to change are
  the output pixel type and the verbose option.  Except when the input
  images are short integers, the noise is significantly greater than one
  digital unit, and disk space is critical, it is probably better to
  allow the processing to convert the images to real pixel datatype.  The
  verbose parameter simply prints the information written to the log file
  on the terminal.  This can be useful when little else is being done and
  you are just beginning.  However, when doing background processing and
  other IRAF reduction tasks it is enough to simply look at the end of
  the logfile with the task <b>tail</b> to see the current state of the
  processing.
  </p>
  <p>
       The <b>ccdproc</b> parameters control the CCD processing.  There are
  many parameters but they all may be conveniently set at this point.
  Many of the parameters have default values set appropriately for the
  instrument you specified.  The images to be processed can be specified
  later.  What needs to be set are the processing operations that you
  want done and the parameters required for each operation.  The
  processing operations are selected by entering yes or no for each one.
  The following items briefly describe each of the possible processing
  operations and the additional parameters required.
  </p>
  <dl>
  <dt><b><i>fixpix</i> - Fix bad CCD lines and columns?</b></dt>
  <!-- Sec='2. Getting Started' Level=0 Label='' Line='\fIfixpix\fR - Fix bad CCD lines and columns?' -->
  <dd>The bad pixels (cosmetic defects) in the detector are given in a file
  specified by the parameter <i>fixfile</i>.  This information is used
  to replace the pixels by interpolating from the neighboring pixels.
  A standard file for your instrument may be set by <b>setinstrument</b>
  or if the word <span style="font-family: monospace;">"image"</span> is given then the file is defined in the instrument
  data file.  For more on the bad pixel file see <b>instruments</b>.
  </dd>
  </dl>
  <dl>
  <dt><b><i>overscan</i> - Apply overscan strip correction?</b></dt>
  <!-- Sec='2. Getting Started' Level=0 Label='' Line='\fIoverscan\fR - Apply overscan strip correction?' -->
  <dd>The overscan or prescan region is specified by the parameter
  <i>biassec</i>.  This is given as an IRAF image section.  Only the
  part of the section corresponding to the readout axis is used and
  the other part is ignored.  The length of the overscan region is
  set by the <i>trimsec</i> parameter.  The overscan
  region is averaged along the readout axis, specified by the parameter
  <i>readaxis</i>, to create a one dimensional bias vector.  This bias is
  fit by a function to remove cosmic rays and noise.  There are a number
  of parameters at the end of the parameter list which control the
  fitting.  The default overscan bias section and fitting parameters for
  your instrument should be set by <b>setinstrument</b>.  If the word
  <span style="font-family: monospace;">"image"</span> is given the overscan bias section is defined in the image
  header or the instrument translation file.  If an overscan section is
  not set you can use <b>implot</b> to determine the columns or rows for
  the bias region and define an overscan image section.  If you are
  unsure about image sections consult with someone or read the
  introductory IRAF documentation.
  </dd>
  </dl>
  <dl>
  <dt><b><i>trim</i> - Trim the image?</b></dt>
  <!-- Sec='2. Getting Started' Level=0 Label='' Line='\fItrim\fR - Trim the image?' -->
  <dd>The image is trimmed to the image section given by the parameter
  <i>trimsec</i>.  A default trim section for your instrument should be
  set by <b>setinstrument</b>, however, you may override this default if
  desired.  If the word <span style="font-family: monospace;">"image"</span> is given the data
  image section is given in the image header or the instrument
  translation file.  As with the overscan image section it is
  straightforward to specify, but if you are unsure consult someone.
  </dd>
  </dl>
  <dl>
  <dt><b><i>zerocor</i> - Apply zero level correction?</b></dt>
  <!-- Sec='2. Getting Started' Level=0 Label='' Line='\fIzerocor\fR - Apply zero level correction?' -->
  <dd>The zero level image to be subtracted is specified by the parameter
  <i>zero</i>.  If none is given then the calibration image will be sought
  in the list of images to be processed.
  </dd>
  </dl>
  <dl>
  <dt><b><i>darkcor</i> - Apply dark count correction?</b></dt>
  <!-- Sec='2. Getting Started' Level=0 Label='' Line='\fIdarkcor\fR - Apply dark count correction?' -->
  <dd>The dark count image to be subtracted is specified by the parameter
  <i>dark</i>.  If none is given then the calibration image will be sought
  in the list of images to be processed.
  </dd>
  </dl>
  <dl>
  <dt><b><i>flatcor</i> - Apply flat field correction?</b></dt>
  <!-- Sec='2. Getting Started' Level=0 Label='' Line='\fIflatcor\fR - Apply flat field correction?' -->
  <dd>The flat field images to be used are specified by the parameter
  <i>flat</i>.  There must be one flat field image for each filter
  or subset (see <b>subsets</b>) to be processed.  If a flat field
  image is not given then the calibration image will be sought
  in the list of images to be processed.
  </dd>
  </dl>
  <dl>
  <dt><b><i>readcor</i> - Convert zero level image to readout correction?</b></dt>
  <!-- Sec='2. Getting Started' Level=0 Label='' Line='\fIreadcor\fR - Convert zero level image to readout correction?' -->
  <dd>If a one dimensional zero level readout correction vector is to be subtracted
  instead of a two dimensional zero level image then, when this parameter is set,
  the zero level images will be averaged to one dimension.  The readout axis
  must be specified by the parameter <i>readaxis</i>.  The default for your
  instrument is set by <b>setinstrument</b>.
  </dd>
  </dl>
  <dl>
  <dt><b><i>scancor</i> - Convert flat field image to scan correction?</b></dt>
  <!-- Sec='2. Getting Started' Level=0 Label='' Line='\fIscancor\fR - Convert flat field image to scan correction?' -->
  <dd>If the instrument is operated in a scan mode then a correction to the
  flat field may be required.  There are two types of scan modes, <span style="font-family: monospace;">"shortscan"</span>
  and <span style="font-family: monospace;">"longscan"</span>.  In longscan mode flat field images will be averaged
  to one dimension and the readout axis must be specified.  Shortscan mode
  is a little more complicated.  The scan correction is used if the flat
  field images are not observed in scan mode.  The number of scan lines
  must be specified by the parameter <i>nscan</i>.  If they are observed in
  scan mode, like the object observations, then the scan correction
  operations should <i>not</i> be specified.  For details of scan mode operations
  see <b>ccdproc</b>.  The scan parameters
  should be set by <b>setinstrument</b>.  If in doubt consult someone
  familiar with the instrument and mode of operation.
  </dd>
  </dl>
  <p>
       This description of the parameters is longer than the actual operation of
  setting the parameters.  The only parameters likely to change during processing
  are the calibration image parameters.
  </p>
  <p>
       When processing many images using the same calibration files a modest
  performance improvement can be achieved by keeping (caching) the
  calibration images in memory to avoid disk accesses.  This option
  is available by specifying the amount of memory available for image
  caching with the parameter <i>max_cache</i>.  If the value is zero then
  the images are accessed from disk as needed while if there is
  sufficient memory the calibration images may be kept in memory during
  the task execution.
  </p>
  </section>
  <section id="s_3__processing_your_data">
  <h3>3. processing your data</h3>
  <p>
       The processing path depends on the type of data, the type of
  instrument, types of calibration images, and the observing
  sequence.  In this section we describe two types of operations common
  in reducing most data; combining calibration images and performing the
  standard calibration and correction operations.  Some additional special
  operations are described in the following section.
  </p>
  <p>
       However, the first thing you might want to try before any
  processing is to get a listing of the CCD images showing the CCD image
  types, subsets, and processing flags.  The task for this is
  <b>ccdlist</b>.  It has three types of output; a short one line per
  image format, a longer format which shows the state of the processing,
  and a format which prints the image names only (used to create files
  containing lists of images of a particular CCD image type).  To get a
  quick listing type:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist *.imh
  ccd001.imh[544,512][short][unknown][V]:FOCUS L98-193
  ccd007.imh[544,512][short][object][V]:N2968 V 600s
  ccd015.imh[544,512][short][object][B]:N3098 B 500s
  ccd024.imh[544,512][short][object][R]:N4036 R 600s
  ccd045.imh[544,512][short][flat][V]:dflat 5s
  ccd066.imh[544,512][short][flat][B]:dflat 5s
  ccd103.imh[544,512][short][flat][R]:dflat 5s
  ccd104.imh[544,512][short][zero][]:bias
  ccd105.imh[544,512][short][dark][]:dark 3600s
  </pre></div>
  <p>
       The example shows only a sample of the images.  The short format
  listing tells you the name of the image, its size and pixel type, the
  CCD image type as seen by the package, the subset identifier (in this
  case the filter), and the title.  If the data had been processed then
  there would also be processing flags.  If the CCD image types do not
  seem right then there may be a problem with the instrument
  specification.
  </p>
  <p>
       Many of the tasks in the <b>ccdred</b> package have the parameter
  <i>ccdtype</i> which selects a particular type of image.  To list
  only the object images from the previous example:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist *.imh ccdtype=object
  ccd007.imh[544,512][short][object][V]:N2968 V 600s
  ccd015.imh[544,512][short][object][B]:N3098 B 500s
  ccd024.imh[544,512][short][object][R]:N4036 R 600s
  </pre></div>
  <p>
  If no CCD image type is specified (by using the null string <span style="font-family: monospace;">""</span>)
  then all image types are selected.  This may be
  necessary if your instrument data does not contain image type identifications.
  </p>
  </section>
  <section id="s_3_1_combining_calibration_images">
  <h3>3.1 combining calibration images</h3>
  <p>
       If you do not need to combine calibration images because you only
  have one image of each type, you can skip this section.  Calibration
  images, particularly zero level and flat field images, are combined in
  order to minimize the effects of noise and reject bad pixels in the
  calibrations.  The basic tool for combining images is the task
  <b>combine</b>.  There are simple variants of this task whose default
  parameters are set appropriately for each type of calibration image.
  These are the ones you will use for calibration images leaving
  <b>combine</b> for combining object images.  Zero level images are
  combined with <b>zerocombine</b>, dark count images with
  <b>darkcombine</b>, and flat field images with <b>flatcombine</b>.
  </p>
  <p>
       For example, to combine flat field images the command is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; flatcombine *.imh
  Jun  1 14:26 combine: maxreject
          Images      N    Exp   Mode  Scale Offset Weight
      ccd045.imh      1    5.0  INDEF  1.000     0.  0.048
      ccd046.imh      1    5.0  INDEF  1.000     0.  0.048
              &lt;... list of files ...&gt;
      ccd065.imh      1    5.0  INDEF  1.000     0.  0.048
      ----------- ------ ------
       FlatV.imh     21    5.0
  </pre></div>
  <p>
  This output is printed when verbose mode is set.  The same information
  is recorded in the log file.  In this case the flat fields are combined
  by rejecting the maximum value at each point in the image (the
  <span style="font-family: monospace;">"maxreject"</span> algorithm).  The images are scaled by the exposure times,
  which are all the same in this example.  The mode is not evaluated for
  exposure scaling and the relative weights are the same because the
  exposure times are the same.  The example only shows part of the
  output; <b>flatcombine</b> automatically groups the flat field images by
  filter to produce the calibration images <span style="font-family: monospace;">"FlatV"</span>, <span style="font-family: monospace;">"FlatB"</span>, and
  <span style="font-family: monospace;">"FlatR"</span>.
  </p>
  </section>
  <section id="s_3_2_calibrations_and_corrections">
  <h3>3.2 calibrations and corrections</h3>
  <p>
       Processing the CCD data is easy and largely automated.
  First, set the task parameters with the following command:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; eparam ccdproc
  </pre></div>
  <p>
  You may have already set the parameters when you ran
  <b>setinstrument</b>, though the calibration image parameters
  <i>zero</i>, <i>dark</i>, and <i>flat</i> may still need to be set or
  changed.  Once this is done simply give the command
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdproc *.imh
  ccd003: Jun  1 15:13 Overscan section is [520:540,*] with mean=485.0
  ccd003: Jun  1 15:14 Trim data section is [3:510,3:510]
  ccd003: Jun  1 15:14 Overscan section is [520:540,*] with mean=485.0
  FlatV:  Jun  1 15:14 Trim data section is [3:510,3:510]
  FlatV:  Jun  1 15:15 Overscan section is [520:540,*] with mean=486.4
  ccd003: Jun  1 15:15 Flat field image is FlatV.imh with scale=138.2
  ccd004: Jun  1 15:16 Trim data section is [3:510,3:510]
  ccd004: Jun  1 15:16 Overscan section is [520:540,*] with mean=485.2
  ccd004: Jun  1 15:16 Flat field image is FlatV.imh with scale=138.2
              &lt;... more ...&gt;
  ccd013: Jun  1 15:22 Trim data section is [3:510,3:510]
  ccd013: Jun  1 15:23 Overscan section is [520:540,*] with mean=482.4
  FlatB:  Jun  1 15:23 Trim data section is [3:510,3:510]
  FlatB:  Jun  1 15:23 Overscan section is [520:540,*] with mean=486.4
  ccd013: Jun  1 15:24 Flat field image is FlatB.imh with scale=132.3
              &lt;... more ...&gt;
  </pre></div>
  <p>
       The output shown is with verbose mode set.  It is the same as
  recorded in the log file.  It illustrates the principle of automatic
  calibration image processing.  The first object image, <span style="font-family: monospace;">"ccd003"</span>, was
  being processed when the flat field image was required.  Since the
  image was taken with the V filter the appropriate flat field was
  determined to be <span style="font-family: monospace;">"FlatV"</span>.  Since it had not been processed, the
  processing of <span style="font-family: monospace;">"ccd003"</span> was interrupted to process <span style="font-family: monospace;">"FlatV"</span>.  The
  processed calibration image may have been cached if there was enough
  memory.  Once <span style="font-family: monospace;">"FlatV"</span> was processed (note that the flat field was not
  flattened because the task knows this image is a flat field) the
  processing of <span style="font-family: monospace;">"ccd003"</span> was completed.  The next image, <span style="font-family: monospace;">"ccd004"</span>, is
  also a V filter image so the already processed, and possibly cached,
  flat field <span style="font-family: monospace;">"FlatV"</span> is used again.  The first B band image is <span style="font-family: monospace;">"ccd013"</span>
  and, as before, the B filter flat field calibration image is processed
  automatically.  The same automatic calibration processing and image
  caching occurs when using zero level and dark count calibration
  images.
  </p>
  <p>
       Commonly the processing is done with the verbose mode turned off
  and the task run as a background job.  This is done with the commands
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdred.verbose=no
  cl&gt; ccdproc *.imh &amp;
  </pre></div>
  <p>
  The already processed images in the input list are recognized as having been
  processed and are not affected.  To check the status of the processing we
  can look at the end of the log file with:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tail logfile
  </pre></div>
  <p>
  After processing we can repeat the <b>ccdlist</b> command to find:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdlist *.imh ccdtype=object
  ccd007.imh[508,508][real][object][V][OTF]:N2968 V 600s
  ccd015.imh[508,508][real][object][B][OTF]:N3098 B 500s
  ccd024.imh[544,512][short][object][R][OTF]:N4036 R 600s
  </pre></div>
  <p>
  The processing flags indicate the images have been overscan corrected,
  trimmed, and flat fielded.
  </p>
  <p>
       As you can see, processing images is very easy.  There is one source
  of minor confusion for beginning users and that is dealing with calibration
  images.  First, there is no reason that calibration images
  may not be processed explicitly with <b>ccdproc</b>, just remember to set
  the <i>ccdtype</i> to the calibration image type or to <span style="font-family: monospace;">""</span>.  When processing
  object images the calibration images to be used may be specified either
  with the task parameter for the particular calibration image or by
  including the calibration image in the list of input images.  Calibration
  images specified by parameter value take precedence and the task
  does not check its CCD image type.  Calibration images given in the
  input list must have a valid CCD image type.  In case too many
  calibration images are specified, say because the calibration images
  combined to make the master calibration images were not deleted and
  so are part of the image list <span style="font-family: monospace;">"*.imh"</span>, only the first one will be used.
  Another point to know is that flat field, iillumination, and fringe images
  are subset (filter) dependent and so a calibration image for each filter
  must be specified.
  </p>
  </section>
  <section id="s_4__special_processing_operations">
  <h3>4. special processing operations</h3>
  <p>
       The special processing operations are mostly concerned with the
  flat field response correction.  There are also special processing
  operations available in <b>ccdproc</b> for one dimensional readout
  corrections in the zero level and flat field calibrations.  These
  were described briefly above and in more detail in <b>ccdproc</b>
  and are not discussed further in this guide.  The processing
  operations described in this section are for preparing flat fields
  for two dimensional spectroscopic data, for correcting flat fields
  for iilluminations effects, for making a separate iillumination correction,
  and for applying corrections for fringe effects.  For additional
  discussion about flat fields and iillumination corrections see the
  help topic <b>flatfields</b>.
  </p>
  </section>
  <section id="s_4_1_spectroscopic_flat_fields">
  <h3>4.1 spectroscopic flat fields</h3>
  <p>
       For spectroscopic data the flat fields may have to be processed to
  remove the general shape of the lamp spectrum and to replace regions outside
  of the aperture where there is no flat field information with values that
  will not cause bad response effects when the flat field is applied to the
  data.  If the shape of the lamp spectrum is not important and if the
  longslit spectra have the regions outside of the slit either off the
  detector or trimmed then you may use the flat field without special
  processing.
  </p>
  <p>
     First you must process the flat field images explicitly with
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdproc *.imh ccdtype=flat
  </pre></div>
  <p>
  where <span style="font-family: monospace;">"*.imh"</span> may be replaced with any list containing the flat fields.
  If zero level and dark count corrections are required these calibration
  images must be available at this time.
  </p>
  <p>
       Load the <b>twodspec</b> package and then either the <b>longslit</b>
  package, for longslit data, or the <b>apextract</b> package, for
  multiaperture data such as echelles, multifiber, or aperture mask
  spectra.  The task for removing the longslit quartz spectrum is
  <b>response</b>.  There is also a task for removing iillumination
  effects, including the slit profile, from longslit spectra called
  <b>iillumination</b>.  For more about processing longslit spectra see the
  help for these tasks and the paper <i>Reduction of Longslit Spectra
  with IRAF</i>.  The cookbook <i>Reduction of Longslit Spectroscopic
  Data Using IRAF (KPNO ICCD and Cryogenic Camera Data)</i> also provides
  a very good discussion even if your data is from a different instrument.
  </p>
  <p>
       For multiaperture data the task for removing the relative shapes of
  the spectra is called <b>apnormalize</b>.  Again, consult the help documentation
  for this task for further details.  Since you will probably also be
  using the package for extracting the spectra you may be interested
  in the document <i>The IRAF APEXTRACT Package</i>.
  </p>
  </section>
  <section id="s_4_2_iillumination_corrections">
  <h3>4.2 iillumination corrections</h3>
  <p>
       The flat field calibration images may not have the same iillumination
  pattern as the observations of the sky due to the way the lamp illuminates the
  optical system.  In this case when the flat field correction is applied
  to the data there will be gradients in the sky background.  To remove
  these gradients a blank sky calibration image is heavily smoothed
  to produce an iillumination image.  The iillumination image
  is then divided into the images during processing to correct for the
  iillumination difference between the flat field and the objects.
  Like the flat fields, the iillumination corrections images may be subset
  dependent so there should be an iillumination image for each subset.
  </p>
  <p>
  The task which makes iillumination correction images is <b>mkskycor</b>.
  Some examples are
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkskycor sky004 Illum004
  cl&gt; mkskycor sky*.imh ""
  </pre></div>
  <p>
  In the first example the sky image <span style="font-family: monospace;">"sky004"</span> is used to make the iillumination
  correction image <span style="font-family: monospace;">"Illum004"</span>.  In the second example the sky images are
  converted to iillumination correction images by specifying no output image
  names.  Like <b>ccdproc</b> if the input images have not been processed they
  are first processed automatically.
  </p>
  <p>
  To apply the iillumination correction
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdproc *.imh ccdtype=object illumcor+ illum=Illum004
  cl&gt; ccdproc *.imh ccdtype=object illumcor+ illum=sky*.imh
  </pre></div>
  <p>
  The iillumination images could also be set using <b>eparam</b> or given
  on the command line.
  </p>
  </section>
  <section id="s_4_3_sky_flat_fields">
  <h3>4.3 sky flat fields</h3>
  <p>
      You will notice that when you process images with an iillumination
  correction you are dividing each image by a flat field calibration and
  an iillumination correction.  If the iillumination corrections are not
  done as a later step but at the same time as the rest of the processing
  one will get the same calibration by multiplying the flat field by
  the iillumination correction and using this product alone as the
  flat field.  Such an image is called a <i>sky flat</i> since it is
  a flat field which has been corrected to yield a flat sky when applied
  to the observations.  This approach has the advantage of one less
  calibration image and two less computations (scaling and dividing the
  iillumination correction).  As an added short cut, rather than compute
  the iillumination image with <b>mkskycor</b> and then multiplying, the
  task <b>mkskyflat</b> does all this in one step.  Thus, <b>mkskyflat</b>
  takes an input blank sky image, processes it if needed, determines the
  appropriate flat field (sky flats are also subset dependent) from the
  <b>ccdproc</b> parameters or the input image list, and produces an
  output sky flat.  Further if no output image is specified the task
  converts the input blank sky calibration image into a sky flat.
  </p>
  <p>
       Two examples in which a new image is created and in which the
  input images are converted to sky flats are
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkskyflat sky004 Skyflat
  cl&gt; mkskyflat sky*.imh ""
  </pre></div>
  </section>
  <section id="s_4_4_iillumination_corrected_flat_fields">
  <h3>4.4 iillumination corrected flat fields</h3>
  <p>
       A third method to account for iillumination problems in the flat fields
  is to remove the large scale pattern from the flat field itself.  This is
  useful if there are no reasonable blank sky calibration images and the
  astronomical exposures are evenly illuminated but the flat fields are not.
  This is done by smoothing the flat field images instead of blank sky
  images.  As with using the sky images there are two methods, creating
  an iillumination correction to be applied as a separate step or fixing
  the original flat field.  The smoothing algorithm is
  the same as that used in the other tasks.  The tasks to make these types
  of corrections are <b>mkillumcor</b> and <b>mkillumflat</b>.  The usage
  is pretty much the same as the other iillumination correction tasks
  except that it is more reasonable to replace the original flat fields
  by the corrected flat fields when fixing the flat field.  Examples
  of an iillumination correction and removing the iillumination pattern
  from the flat field are
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkillumcor flat025 Illum025
  cl&gt; mkillumflat flat*.imh ""
  </pre></div>
  <p>
  As with the other tasks, the input images are processed if necessary.
  </p>
  </section>
  <section id="s_4_5_fringe_corrections">
  <h3>4.5 fringe corrections</h3>
  <p>
      Some CCD detectors suffer from fringing effects due to the night
  sky emission lines which are not removed by the other calibration
  and correction operations.  To correct for the fringing you need a
  really blank sky image.  There is not yet a task to remove objects from
  sky images because this is often done with an interactive image display
  tool (which will soon be added).  The blank sky image is heavily smoothed
  to determine the mean sky background and then this is subtracted from the
  original image.  The image should then be essentially zero except for the
  fringe pattern.  This fringe correction image is scaled to the same
  exposure time as the image to be corrected and then subtracted to remove
  the fringing.  Note that since the night sky lines are variable there
  may need to be an additional scaling applied.  Determining this scaling
  requires either an interactive display tool or a very clever task.
  Such tasks will also be added in the future.
  </p>
  <p>
       The task to make a fringe correction image is <b>mkfringecor</b>.
  the sky background is determined in exactly the same way as the iillumination
  pattern, in fact the same sky image may be used for both the sky
  iillumination and for the fringe correction.  The task works consistently
  with the <span style="font-family: monospace;">"mk"</span> tasks in that the input images are processed first if needed
  and then the output correction image is produced with the specified name
  or replaces the input image if no output image is specified.
  As examples,
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkfringecor sky004 Fringe
  cl&gt; mkfringecor sky*.imh ""
  </pre></div>
  </section>
  <section id="s_5__demonstration">
  <h3>5. demonstration</h3>
  <p>
       A simple demonstration task is available.  To run this demonstration
  load the <b>ccdtest</b> package; this is a subpackage of the main
  <b>ccdred</b> package.  Then simply type
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; demo
  </pre></div>
  <p>
  The demonstration will then create some artificial CCD data and reduce
  them giving descriptive comments as it goes along.  This demonstration uses
  the <span style="font-family: monospace;">"playback"</span> facility of the command language and is actually substituting
  it's own commands for terminal input.  Initially you must type carriage return
  or space after each comment ending with <span style="font-family: monospace;">"..."</span>.  If you wish to have the
  demonstration run completely automatically at it's own speed then type <span style="font-family: monospace;">'g'</span>
  a the <span style="font-family: monospace;">"..."</span> prompt.  Thereafter, it will simple pause long enough to give
  you a chance to read the comments.  When the demo is finished you will
  need to remove the files created.  However, feel free to examine the reduced
  images, the log file, etc.  <i>Note that the demonstration changes the
  setup parameters so be sure to run </i><b>setinstrument</b><i> again and check
  the setup parameters.</i>
  </p>
  </section>
  <section id="s_6__summary">
  <h3>6. summary</h3>
  <p>
       The <b>ccdred</b> package is very easy to use.  First load the package;
  it is in the <b>imred</b> package which is in the <b>noao</b> package.
  If this is your first time reducing data from a particular instrument
  or if you have changed instruments then run <b>setinstrument</b>.
  Set the processing parameters for the operations you want performed.
  If you need to combine calibration images to form a master calibration
  image use one of the combine tasks.  Spectroscopic flat fields may
  need to be processed first in order to remove the lamp spectrum.
  Finally, just type
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdproc *.imh&amp;
  </pre></div>
  </section>
  <section id="s_7__references">
  <h3>7. references</h3>
  <p>
       A general guide to using IRAF is <i>A User's Introduction to the IRAF
  Command Language</i>.  This document may be found in the IRAF documentation
  sets and is available from the National Optical Astronomy Observatories,
  Central Computer Services (NOAO-CCS).
  </p>
  <p>
       A more detailed description of the <b>ccdred</b> package including
  a discussion of the design and some of the algorithms see <i>The IRAF
  CCD Reduction Package -- CCDRED</i> by F. Valdes.  This paper is available
  from NOAO-CCS and appears in the proceedings of the Santa Cruz Summer
  Workshop in Astronomy and Astrophysics, <i>Instrumentation for Ground-Based
  Optical Astronomy: Present and Future</i>, edited by Lloyd B. Robinson and
  published by Springer-Verlag.
  </p>
  <p>
       The task descriptions and supplementary documentation are available
  in printed form in the IRAF documentation sets, a special set
  containing documentation for just the <b>ccdred</b> package, and on-line
  through the help task by typing
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help <i>topic</i>
  </pre></div>
  <p>
  where <i>topic</i> is one of the following.
  </p>
  <div class="highlight-default-notranslate"><pre>
    badpiximage - Create a bad pixel mask image from a bad pixel file
      ccdgroups - Group CCD images into image lists
       ccdhedit - CCD image header editor
        ccdlist - List CCD processing information
        ccdproc - Process CCD images
        ccdtest - CCD test and demonstration package
        combine - Combine CCD images
     cosmicrays - Detect and replace cosmic rays
    darkcombine - Combine and process dark count images
    flatcombine - Combine and process flat field images
    mkfringecor - Make fringe correction images from sky images
     mkillumcor - Make flat field iillumination correction images
    mkillumflat - Make iillumination corrected flat fields
       mkskycor - Make sky iillumination correction images
      mkskyflat - Make sky corrected flat field images
  setinstrument - Set instrument parameters
    zerocombine - Combine and process zero level images
  
            ADDITIONAL HELP TOPICS
  
         ccdred - CCD image reduction package
       ccdtypes - Description of the CCD image types
     flatfields - Discussion of CCD flat field calibrations
          guide - Introductory guide to using the CCDRED package
    instruments - Instrument specific data files
        subsets - Description of CCD subsets
  </pre></div>
  <p>
  Printed copies of the on-line help documentation may be made with the
  command
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help topic | lprint
  </pre></div>
  <p>
       In addition to the package documentation for <b>ccdred</b>,
  <b>longslit</b>, and <b>apextract</b> there may be specific guides for
  certain instruments.  These specific guides, called <span style="font-family: monospace;">"cookbooks"</span>, give
  specific examples and parameter values for the CCD data.
  </p>
  
  </section>
  
  <!-- Contents: '1. Introduction' '2. Getting Started' '3. Processing Your Data' '3.1 Combining Calibration Images' '3.2 Calibrations and Corrections' '4. Special Processing Operations' '4.1 Spectroscopic Flat Fields' '4.2 Iillumination Corrections' '4.3 Sky Flat Fields' '4.4 Iillumination Corrected Flat Fields' '4.5 Fringe Corrections' '5. Demonstration' '6. Summary' '7. References'  -->
  

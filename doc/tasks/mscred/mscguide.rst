.. _mscguide:

mscguide: Introductory guide to using the MSCRED package
========================================================

**Package: mscred**

.. raw:: html

  <section id="s_sections">
  <h3>Sections</h3>
  <div class="highlight-default-notranslate"><pre>
  1. Introduction
  2. Multiextension FITS Files
  3. Examining Mosaic Data
      3.1 Displaying the Data
          2.1.1 On-the-Fly (OTF) Calibration
          2.1.2 Real-Time Display with the DCA
      3.2 Examining the Data
      3.3 Examining the Headers
      3.4 Determining Best Focus
  4. Data Reductions
      4.1 Some Preliminaries
      4.2 Basic CCD Calibration
          4.2.1  Calibration Data to Obtain At the Telescope
          4.2.2  Preparing Calibration Data
          4.2.3 Pupil Image Removal from Flat Fields
              4.2.3.1 Broadband Data
              4.2.3.2 Narrowband Data
          4.2.4 Object Exposure Reductions
          4.2.5 Pupil Image Removal from Object Data
              4.2.5.1 Broadband Data
              4.2.5.2 Narrowband Data
          4.2.6 Dark Sky or Twilight Sky Flat Fields
          4.2.7 The Variable Pixel Scale and Zero Point Uniformity
      4.3 Coordinate Calibration
          4.3.1 Setting Coordinate Zero Points and Measuring Coordinates
          4.3.2 Matching Coordinate Systems
      4.4 Putting the Pieces Together
          4.4.1 Removing Sky Gradients
          4.4.2 Constructing Single Images
          4.4.3 Matching Intensity Scales
          4.4.4 Making the Final Stack Image
  </pre></div>
  </section>
  <section id="s_1__introduction">
  <h3>1. introduction</h3>
  <p>
  This document discusses handling and reducing CCD mosaic data, particularly
  data from the NOAO CCD Mosaic Imager (referred to here as the NOAO Mosaic),
  using IRAF and the <b>mscred</b> package.  It is not a beginner's
  guide and assumes some previous experience with IRAF and CCD reductions.
  </p>
  <p>
  The first section discusses the mosaic data format and how to use it with
  IRAF.  This format is more complex than single CCD images because of the
  multiple CCDs and possibly multiple amplifiers per CCD.  To keep the data
  from each exposure self-contained the multiple CCD images are stored in a
  single file.  This multiple image per file has many advantages but it does
  mean that some commands for dealing with images behave differently.
  </p>
  <p>
  The second section describes the tools used to examine the mosaic data.
  These tools are used during observing as well as during data reductions.
  </p>
  <p>
  The last section describes the reduction of mosaic data.  This includes
  basic CCD instrumental calibration and combining mosaic exposures into
  single images.
  </p>
  </section>
  <section id="s_2__multiextension_fits_files">
  <h3>2. multiextension fits files</h3>
  <p>
  The data format used by the NOAO Mosaic Data Handling Software (MDHS) is a
  multiextension FITS (MEF) file.  This format is produced by the the Data
  Capture Agent (DCA) when observing with the NOAO Mosaic.  The MEF file for
  the NOAO Mosaic currently consists of nine FITS header and data units
  (HDU).  The first HDU, called the primary or global header unit, contains
  only header information which is common to all the CCD images.  The
  remaining eight HDUs, called extensions, contain the images from the eight
  CCDs.
  </p>
  <p>
  The fact that the image data is stored as a FITS file is not significant.
  Starting with IRAF V2.11, FITS files consisting of just a single primary
  image may be used in the same way as any other IRAF image format.  The
  significant feature of the mosaic format is its multi-image structure.
  </p>
  <p>
  With multiextension FITS files you must either use tasks which are
  specifically designed to operate on these files as a unit or explicitly
  specify the image within the file that is to be operated upon by general
  IRAF image processing tasks.  The tasks in the <b>mscred</b> package are
  designed to operate on the mosaic MEF files and so you only need to specify
  the filename.  For image tasks outside the <b>mscred</b> package you must
  specify the image in the MEF file using the syntax
  </p>
  <div class="highlight-default-notranslate"><pre>
  filename[extension]
  </pre></div>
  <p>
  where <span style="font-family: monospace;">"filename"</span> is the name of the MEF file.  The <span style="font-family: monospace;">".fits"</span> filename
  extension is optional provided there is no confusion with other files with
  the same basename.  The image <span style="font-family: monospace;">"extension"</span> is specified either using an
  extension name or the position of the extension in the file (where the
  first extension is 1).  The extension names in the NOAO Mosaic data are
  <span style="font-family: monospace;">"im1"</span> through <span style="font-family: monospace;">"im8"</span> for the eight CCDs.  For a detail discussion of the
  IRAF FITS Image Kernel and the syntax it supports for multiextension
  FITS files see ftp://iraf.noao.edu/iraf/docs/fits_userguide.ps.Z.
  </p>
  <p>
  If you forget to specify an extension to a task that expects only
  single images you will get the following error which is your reminder
  to include an extension.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; imhead obj012 1
  ERROR: FXF: must specify which FITS extension (obj012)
  </pre></div>
  <p>
  Two of the most common tasks that require specifying an image extension
  are <b>display</b> to display a single CCD image (the task <b>mscdisplay</b>
  is used to display all the images at once) and <b>imheader</b> to list
  the header of a particular CCD.  So, for example, the following commands
  might be used.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; display obj012[im2] 1
  ms&gt; imhead obj012[3] l+
  </pre></div>
  <p>
  Other tasks you may use this way are <b>imexam</b> and <b>implot</b>.
  </p>
  <p>
  A common question is how to specify a list of extensions.  Modification of
  the syntax to allow wildcard templates in the extension specification is
  under study.  Currently you must specify each extension explicitly, though
  the filename itself may be a wildcard; for example the first image in a set
  of files can be collectively specified with
  </p>
  <div class="highlight-default-notranslate"><pre>
  obj*[im1]
  </pre></div>
  <p>
  There are two methods for specifying some or all extensions in tasks that
  operate upon lists of images.  One is to make @files.  This can be done
  explicitly with an editor.  However the <b>proto</b> task <b>imextensions</b>
  can expand MEF files into an @file as in the following example.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; imexten obj012,obj13 &gt; list
  ms&gt; imhead @list
  </pre></div>
  <p>
  Read the help page for further information, additional parameters, and
  examples.
  </p>
  <p>
  Another method is to use the special <b>mscred</b> task <b>msccmd</b>.  This
  task can be used on the command line or as a simple interactive command
  interpreter.  The idea is that you use the special designations <span style="font-family: monospace;">"$input"</span>
  and <span style="font-family: monospace;">"$output"</span> for task parameters which allow lists of images.  Then
  lists of MEF filenames are specified for the input and output which are
  expanded and substituted into the task parameters when it is executed.
  For example,
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; msccmd "imhead $input l+" input=obj012,obj013
  </pre></div>
  <p>
  For additional information and examples consult the help page for that task.
  </p>
  <p>
  Note that the tasks <b>imstat</b> and <b>imarith</b> are so useful and common
  that there are specific <b>mscred</b> tasks <b>mscstat</b> and <b>mscarith</b>
  that operate on all or a subset of image extensions.  So these tasks need
  not be used with <b>msccmd</b> or with @files.
  </p>
  <p>
  We conclude with a discussion of the special operations of copying,
  renaming, deleting, and reading and writing FITS tapes as they apply to the
  mosaic MEF files.  To copy a mosaic file as a unit use <b>copy</b>, making
  sure to explicitly specify the <span style="font-family: monospace;">"fits"</span> extension.  If you use <b>imcopy</b>
  it will expect you to specify a particular extension and will copy only
  that extension.  While <b>imcopy</b> is not the way to copy an complete MEF
  file the tasks <b>imrename</b> and <b>imdelete</b> are the commands for
  renaming and deleting these files; though <b>rename</b> and <b>delete</b>
  will also work provided you are explicit with the extension.  Finally the
  mosaic data should be kept as a MEF file and so the special mosaic
  tasks <b>mscwfits</b> and <b>mscrfits</b> should be used.  The current
  <b>wfits</b> and <b>rfits</b> are not intended for this type of data.
  </p>
  </section>
  <section id="s_3__examining_mosaic_data">
  <h3>3. examining mosaic data</h3>
  <p>
  During observing a small set of IRAF commands are commonly used to examine
  the data.  This section describes these commands.  While the discussion is
  oriented towards examining the data at the telescope during the course of
  observing, the tools described here are also used when reducing data at a
  later time.
  </p>
  </section>
  <section id="s_3_1_displaying_the_data">
  <h3>3.1 displaying the data</h3>
  <p>
  The two commands <b>display</b> and <b>mscdisplay</b> are used to display the
  data in a display server window.  The display server is a separate process
  which must be running before displaying the images.  The observing
  environment at the telescope will generally have the XIMTOOL display server
  already running with a window on a separate monitor.  If it is not running
  for some reason it can be started with a menu selection.  Away from the
  telescope you would start XIMTOOL or SAOIMAGE as you do normally.
  </p>
  <p>
  The display server must be told what size <span style="font-family: monospace;">"frame buffer"</span> to allocate for
  holding the display pixels.  This determines how many pixels may be loaded
  at one time.  Note that the display window may be smaller than this size
  and the display server allows you to move the portion viewed and
  zoom/unzoom any region.  If the image size is larger than the frame buffer
  you can display a portion of the image at full resolution or the full image
  at a lower resolution.  The frame buffer size is queried and set with the
  commands:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; show stdimage
  imt4096
  ms&gt; set stdimage=imt2048
  </pre></div>
  <p>
  There are trade-offs in the frame buffer selection.  A large frame buffer
  allows you to have higher resolution for the large mosaic images but it
  uses more memory and takes longer to load.
  </p>
  <p>
  The <b>display</b> task is used to display individual images in the display
  server.  This task is a standard IRAF task about which you are assumed to
  have some basic knowledge.  There are many display options which
  are discussed in the help page.  The only special factor in using this
  task with mosaic data is that you must specify which CCD image to display
  using the image extension syntax discussed previously.  As an example,
  to display the central portion of extension im3 in the first frame
  and the whole image in the second frame:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; display obj123[im3] 1 fill-
  ms&gt; display obj123[im3] 2 fill+
  </pre></div>
  <p>
  The <b>mscdisplay</b> task is based on <b>display</b> with a number of
  specialized enhancements for displaying mosaic data.  It displays the
  entire mosaic observation in a single frame by <span style="font-family: monospace;">"filling"</span> each image in a
  tiled region of the frame buffer.  The default filling (defined by the
  order parameter) subsamples the image by uniform integer steps to fit the
  tile and then replicates pixels to scale to the full tile size.  The
  resolution is set by the frame buffer size.  As mentioned before, trying to
  increase the resolution with a larger buffer size has the penalty of longer
  display times.  An example display command is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; mscdisplay obj123 1
  </pre></div>
  <p>
  The default parameters for <b>mscdisplay</b> are shown below.  Many of the
  parameters are the same as <b>display</b> but there are also a few that are
  specific to the task of displaying a mosaic of CCD images as indicated with
  an asterisk.
  </p>
  <div class="highlight-default-notranslate"><pre>
                                 I R A F
              Image Reduction and Analysis Facility
      PACKAGE = mscred
         TASK = mscdisplay
  
      image   =           root name for image to be displayed
      frame   =        1  frame to be written into
  *   (mimpars=         ) mosaic image parameters
  *   (check  =       no) check if image is loaded
  *   (onepass=       no) load all extensions in one pass?
      (bpmask =      BPM) bad pixel mask
      (bpdispl=     none) bad pixel display (none|overlay|interpolate)
      (bpcolor=      red) bad pixel colors
      (overlay=         ) overlay mask
      (ocolors=    green) overlay colors
      (erase  =      yes) erase frame
      (border_=       no) erase unfilled area of window
      (select_=      yes) display frame being loaded
      (repeat =       no) repeat previous display parameters
      (fill   =       no) scale image to fit display window
      (zscale =      yes) display range of greylevels near median
      (contras=     0.25) contrast adjustment for zscale algorithm
      (zrange =      yes) display full image intensity range
      (zmask  =         ) sample mask
  *   (zcombin=     auto) Algorithm for combining z1 and z2 values...
      (nsample=     1000) maximum number of sample pixels to use
      (order  =        0) spatial interpolator order (0=replicate,...
      (z1     =       0.) minimum greylevel to be displayed
      (z2     =    1000.) maximum greylevel to be displayed
      (ztrans =   linear) greylevel transformation (linear|log|none|user)
      (lutfile=         ) file containing user defined look up table
  </pre></div>
  <p>
  The mapping of the pixel values to grey levels includes the same automatic
  or range scaling algorithms as in <b>display</b>.  This is done for each
  image in the mosaic separately.  The new parameter <span style="font-family: monospace;">"zcombine"</span> then selects
  whether to display each image with it's own independent display range
  (<span style="font-family: monospace;">"none"</span>) or to combine the display ranges into a single display range based
  on the minimum and maximum values (<span style="font-family: monospace;">"minmax"</span>), the average of the minimum
  and maximum values (<span style="font-family: monospace;">"average"</span>), or the median (<span style="font-family: monospace;">"median"</span>) of the minimum and
  maximum values.  The independent scaling is most appropriate for raw data
  while the <span style="font-family: monospace;">"minmax"</span> scaling is recommend for processed data which are gain
  calibrated.  The special value <span style="font-family: monospace;">"auto"</span> (the default) checks if the display
  data has been flat fielded, either by separate processing or with
  on-the-fly calibration, and if so it uses <span style="font-family: monospace;">"minmax"</span> scaling and if not it
  used independent scaling.
  </p>
  <p>
  The <span style="font-family: monospace;">"mimpars"</span> (mosaic image parameters) parameter is actually a reference
  to another set of parameters.  The default with no value is to use the
  parameters from the parameter task <b>mimpars</b>.  These parameters can
  be examined and set with <b>epar</b>  either by typing <span style="font-family: monospace;">":e"</span> when over this
  parameter in <b>mscdisplay</b> or by running <b>epar</b> directly on this
  task; i.e. epar mimpars.  The parameters for NOAO Mosaic data are shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
                         I R A F
          Image Reduction and Analysis Facility
  PACKAGE = mscred
     TASK = mimpars
  
  (extname=         ) extension name pattern
  (exttmpl= _![1-9]![1-9]![1-9].*) extension template
  
  (xgap   =       72) minimum X gap between images
  (ygap   =       36) minimum Y gap between images
  
  (process=       no) do calibration processing?
  (oversca=      yes) do line-by-line overscan subtraction?
  (flatfie=      yes) do flat field correction?
  (caldir = mscdb$noao/kpno/4meter/caldir/) calibration directory
  (filter =  !filter) filter
  </pre></div>
  <p>
  The <span style="font-family: monospace;">"extname"</span> parameter is used to select as subset of the image extensions to
  display.  It is a pattern to match extension image names.  For extensions
  such as im1, im2, etc. the pattern typically uses the character selection
  template such as <span style="font-family: monospace;">"[1256]"</span> to select anything with a 1, 2, 5, or 6 in
  the name.  The pattern matching syntax can be found in the help for
  the task <b>match</b>.
  </p>
  <p>
  The <span style="font-family: monospace;">"exttmplt"</span> parameter is for use with non-MEF data.  The gap parameters
  define the gap size in the display.  The remaining parameters are for
  the on-the-fly calibration discussed below.
  </p>
  </section>
  <section id="s_3_1_1_on_the_fly__otf__calibration">
  <h3>3.1.1 on-the-fly (otf) calibration</h3>
  <p>
  Raw mosaic data can exhibit significant instrumental artifacts which may
  interfere with inspecting the data prior to reductions.  The most significant
  artifact is gain variations both within each CCD image and between the
  CCDs.  In the simplest case of constant gain variations between the CCDs
  the independent display scaling, <span style="font-family: monospace;">"zcombine"</span> of none or auto, may be
  sufficient.  But when there are significant flat field patterns it may
  be desirable to apply a quick, approximate flat field calibration as
  the data are being displayed.
  </p>
  <p>
  <b>Mscdisplay</b> can apply an on-the-fly (OTF) calibration to raw mosaic
  exposures.  This does not change the actual data files and the calibration
  is intended to be quick and approximate.  The calibration steps performed
  are a line-by-line bias subtraction using the overscan region of the data
  and a division by a flat field.  If the data have been overscan corrected
  or flat field corrected by <b>ccdproc</b> then the task will automatically
  skip those steps.  The title of the display will indicate if the data have
  been calibrated by adding <span style="font-family: monospace;">"[bias]"</span> for bias subtraction and
  <span style="font-family: monospace;">"[bias,flat=XXX]"</span> for bias subtraction and flat fielding using an OTF flat
  field called XXX.
  </p>
  <p>
  The bias subtraction is performed by averaging the overscan pixels in a
  line and subtracting this average from all the pixels in the line.  This
  removes the amplifier bias and line-by-line patterns.
  </p>
  <p>
  The flat field or response calibration is performed by reading special
  compact flat field calibration data which provides an approximate relative
  response for each pixel in each amplifier readout.  Depending on how the
  calibration file is derived this will approximately correct for pixel
  sensitivity variations, gain variations between the amplifiers, sky
  illumination variations, and any pupil ghost pattern (as occurs with NOAO
  Mosaic data from the Mayall (KPNO 4meter) telescope).
  </p>
  <p>
  The <span style="font-family: monospace;">"process"</span> parameter in the <b>mimpars</b> parameter set shown
  earlier selects whether to turn on or off the OTF processing.  If it is no
  then regardless of the <span style="font-family: monospace;">"overscan"</span> or <span style="font-family: monospace;">"flatfield"</span> parameter settings
  no calibration is applied.  If it is yes then one or both calibration
  operations can be selected.  Because the <b>mimpars</b> parameters can be
  set on the command line, it is common to leave the <span style="font-family: monospace;">"process"</span> parameter set
  one way, say to <span style="font-family: monospace;">"no"</span>, and then override the value when displaying.  For
  example,
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; mscdisplay obj023 1 proc+
  ms&gt; mscdisplay flat022 2 proc+ flatfield-
  </pre></div>
  <p>
  The flat field calibration requires special calibration files.  The
  <span style="font-family: monospace;">"caldir"</span> parameter defines a directory containing the calibration
  files.  This can be a standard directory or a user directory.  Note
  that if a directory is specified it must end with $ or /.
  </p>
  <p>
  Within the calibration directory the calibration file to apply is selected
  by the <span style="font-family: monospace;">"filter"</span> parameter.  For automatic selection of calibrations, the
  calibrations can be selected by the filter string in the header (or by
  giving the same filter string in the <span style="font-family: monospace;">"filter"</span> parameter).  To use the
  filter string in the header the value of the filter parameter is set to
  <span style="font-family: monospace;">"!&lt;keyword&gt;"</span> where &lt;keyword&gt; is the keyword for the filter string.
  </p>
  <p>
  Creating the a calibration directory and calibration files is done with
  the task <b>mscotfflat</b>.  For the NOAO Mosaic a calibration directory
  is provided.  However you can create your own as described in the help
  for <b>mscotfflat</b>.  The <span style="font-family: monospace;">"filter"</span> parameter
  can be set to one of these names.
  </p>
  </section>
  <section id="s_3_1_2_real_time_display_with_the_dca">
  <h3>3.1.2 real-time display with the dca</h3>
  <p>
  During data acquisition the <b>mscdisplay</b> task can be used to display mosaic
  data as it is being written to disk by the DCA.  It begins execution
  shortly after the readout begins and displays the portion of the recorded
  image which has been written to disk.  It then continually displays
  new data which has been written by the DCA until the exposure is completely
  written to the display.
  </p>
  <p>
  The DCA control panel allows you to select whether to display the data
  during readout and how it is to be displayed.  This includes selecting the
  OTF calibration.  One toggle is equivalent to the <span style="font-family: monospace;">"process"</span> parameter.
  If the processing is turned on the DCA automatically selects only overscan
  bias subtraction for non-object exposures and selects both bias subtraction
  and flat field division for object exposures.  The <span style="font-family: monospace;">"filter"</span> parameter
  is set by passing through the filter string from the data acquisition
  system or by overriding this and using the filter menu to select one of the
  available calibrations.
  </p>
  </section>
  <section id="s_3_2_examining_the_data">
  <h3>3.2 examining the data</h3>
  <p>
  The task <b>mscexamine</b> allows interactive examination of mosaic images.
  It is essentially the same as the standard <b>imexamine</b> task except that
  it translates the cursor position in a tiled mosaic display into the image
  coordinates of the appropriate extension image.  Line and column plots also
  piece together the extensions at the particular line or column of the
  mosaic display.  To enter the task after displaying an image the command
  is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; mscexam
  </pre></div>
  <p>
  As with <b>imexamine</b>, one may specify the mosaic MEF filename to be
  examined and if it is not currently displayed it will be displayed using the
  current parameters of <b>mscdisplay</b>.
  </p>
  <p>
  It is important to realize that this task shares the <b>mimpars</b> parameters
  with <b>mscdisplay</b>.  To get data values back that match what is displayed
  the parameters must agree with those used to display the data.  In particular,
  if the data are display with OTF processing then <b>mscexam</b> must be
  told this either by explicitly setting the process flat in <b>mimpars</b>
  or setting it on the command line,
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; mscexam proc+
  </pre></div>
  </section>
  <section id="s_3_3_examining_the_headers">
  <h3>3.3 examining the headers</h3>
  <p>
  There was discussion earlier concerning the use of generic image tasks with the
  NOAO Mosaic data.  The tasks <b>imheader</b> and <b>hselect</b> fall into
  this category.  The two important points to keep in mind are that you must
  specify either an extension name or the extension position and that the
  headers of an extension are the combination of the global header and the
  extension headers.
  </p>
  <p>
  Often one does not need to list all the headers for all the extensions.
  The image title and many keywords of interest are common to all the
  extensions.  Thus one of the following commands will be sufficient
  to get header information about an exposure or set of exposures:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; imhead obj*[1] l-                       # Title listing
  ms&gt; imhead obj123[1] l+ | page              # Paged long listing
  ms&gt; hselect obj*[1] $I,filter,exptime,obstime yes
  </pre></div>
  <p>
  If you need to list header information from all the extensions then you
  need to take the additional step of creating an @file or using
  <b>msccmd</b>.  For example to get the default read noise and gain values
  for each CCD:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; imextensions obj123 &gt; list123
  ms&gt; hselect @list123 $I,rdnoise,gain yes
          or
  ms&gt; msccmd "hselect $input $I,rdnoise,gain yes" input=obj123
  </pre></div>
  <p>
  The <b>ccdlist</b> task in the <b>mscred</b> package is specialized for the
  mosaic data.  It provides a compact description of the name, title, pixel
  type, filter, amplifier, and processing flags.  The <span style="font-family: monospace;">"extname"</span> parameter may
  be used to select a particular extension, a set of extensions, or all
  extensions.  Because all extensions should generally be at the same state
  of reduction it may be desirable to list only the first extension.  Like
  most of the CCD reduction tasks you can also select only a certain type of
  exposure for listing.  Examples of the two modes are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Summary for all exposures
  ms&gt; ccdlist *.fits extname=im1
  # Summary for all object exposures
  ms&gt; ccdlist *.fits extname=im1 ccdtype=object
  # List of all extensions.
  ms&gt; ccdlist obj123 extname=""
  </pre></div>
  </section>
  <section id="s_3_4_determining_best_focus">
  <h3>3.4 determining best focus</h3>
  <p>
  Focus sequence frames can be evaluated for the best focus using <b>mscexam</b>
  and the <span style="font-family: monospace;">'r'</span> or <span style="font-family: monospace;">'a'</span> keys.  However, there is a special task for measuring
  the sequence of focus images called
  <b>mscfocus</b>.  This displays a focus exposure with <b>mscdisplay</b> (if
  needed) and then lets you select one or more bright stars to measure.  This
  task is customized so that all you need do is mark the top image in any
  CCD.  For NOAO Mosaic data, header information tells the task how many
  exposures, the spacings between the exposures, and the focus values.  After
  the measurements are made they are displayed and analyzed graphically and
  written to the terminal and logfile.  This task is the mosaic analog of the
  <b>kpnofocus</b> and <b>starfocus</b> tasks for single CCD data.
  </p>
  </section>
  <section id="s_4__data_reductions">
  <h3>4. data reductions</h3>
  <p>
  The reduction of CCD mosaic data can be divided into two stages.
  The first is the basic calibration of the individual CCDs.  This stage is
  similar to reducing data from single CCD exposures except that the
  calibration operations are repeated for all the CCDs in the mosaic.  The
  only significant difference is that any scaling of an exposure, such as in
  normalizing the flat field calibration, must be done uniformly over all
  the CCDs.  The details of repeating the calibrations for all CCDs and the
  scaling of the calibration data are taken care of by the software and the
  data format so that these operations appear the same as with single CCD
  data.
  </p>
  <p>
  There are some steps which are not typical for CCD data with smaller
  fields of view or specific to the NOAO Mosaic at the Mayall telescope.
  At the Mayall telescope there are reflections off the corrector that
  produce a visible image of the pupil.  Coating of the corrector minimizes
  this image but it may be desirable to remove this instrumental signature
  which would otherwise cause a small variation of the photometric zero
  point as well as an unwanted visible feature.  There are two sections
  discussing removal of this feature from the flat field data and from
  the object exposures.  If your data is from the KPNO 0.9 meter telescope
  or the image is faint enough that it is not of concern then you can
  skip the extended discussion.
  </p>
  <p>
  A caveat about the pupil removal steps described here is that this document
  was written prior to the latest removal of the corrector for better
  anti-reflection coating.  So the NOAO staff have little experience with
  these corrections though earlier work has shown that these steps will do a
  good job.
  </p>
  <p>
  Another step of the basic CCD calibration stage which has generally been
  ignored or forgotten with smaller single CCD formats is the variable pixel
  scale.  The large field of view provided by a mosaic and the optics
  required to provide it can lead to a significant variation in the pixel
  scale.  This effect is important with the Mayall telescope and is also
  present in the NOAO 0.9 meter data to a smaller degree.  It is likely to be
  present in other telescopes as well.
  </p>
  <p>
  When the pixel scale varies significantly the standard flat field
  calibration operation will cause the photometric zero point to vary.  A
  simple calibration step can be performed to remove this effect.  However,
  if you intend to produce single images from the mosaic of CCDs this step is
  not necessary since the resampling operation naturally accounts for this
  effect.
  </p>
  <p>
  The second stage of data reductions is unique to mosaic data.  This stage
  is the combining of the multiple CCD images and multiple exposures into a
  single image.  Since creating a single image from a single mosaic exposure
  is of marginal value, the thrust of this stage of the reductions is the
  combining of multiple exposures which have been spatially offset or
  <span style="font-family: monospace;">"dithered"</span> to cover both the gaps between the individual CCDs and any
  defects.
  </p>
  <p>
  The steps required to produce a single deep integration from dithered
  exposures consist of accurately registering the images, mosaicing the
  exposures into single images with the same spatial sampling, measuring
  changes in the intensity scale due to variations in transparency and sky
  brightness, and combining the individual images into a single deep image
  with the gaps and bad pixels removed.
  </p>
  </section>
  <section id="s_4_1_some_preliminaries">
  <h3>4.1 some preliminaries</h3>
  <p>
  The command <b>setinstrument</b> is used to set default parameters for the
  tasks in the <b>mscred</b> package appropriate to a particular instrument.
  For users of the NOAO Mosaic it is recommended you run this command the
  first time you reduce data.  Subsequently you should not do this since it
  will reset parameters you later changed.
  </p>
  <p>
  To set the parameters for reducing the NOAO Mosaic data type the command
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; setinstrument kpno 4meter CCDMosaThin1 review-
  </pre></div>
  <p>
  Substitute <span style="font-family: monospace;">"36inch"</span> for <span style="font-family: monospace;">"4meter"</span> if the data is from the Kitt Peak
  0.9 meter telescope.
  </p>
  <p>
  For some of the operations it is useful to specify lists of exposures
  corresponding to a dither set.  The examples in this guide show using
  @files for dither sets.  An @file is simply a list of filenames.  These can
  be created in several ways including using a text editor.  One way is with
  the <b>files</b> command to expand a file template.  For example,
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; files obj021,obj022,obj023,obj024,obj025 &gt; field1
  ms&gt; dir @field1
  obj021  obj002  obj003  obj004 obj005
  </pre></div>
  </section>
  <section id="s_4_2_basic_ccd_calibration">
  <h3>4.2 basic ccd calibration</h3>
  <p>
  Basic CCD instrumental calibrations consist of correcting each CCD for
  electronic bias levels, zero exposure patterns, dark counts, and pixel
  sensitivities.  A cosmetic replacement of bad pixels may also be included.
  For the Mayall telescope the pupil image due to reflections off the
  corrector must be removed from the flat field and object exposures.
  An additional calibration is required to correct for the variable pixel
  scale across the field of view if you intend to do photometry on the
  individual CCD images.
  </p>
  </section>
  <section id="s_4_2_1__calibration_data_to_obtain_at_the_telescope">
  <h3>4.2.1  calibration data to obtain at the telescope</h3>
  <p>
  Good data reductions begin with obtaining good calibration data at the
  telescope.  This section discusses the NOAO Mosaic but the general
  principles will apply to other detectors, though the relative importance of
  different calibrations will depend on the quality of the CCDs and the
  stability of the camera.
  </p>
  <p>
  The standard calibration data are sequences of zero exposures and
  sequences of dome flat field exposures.  While dark count exposures,
  matched to the typical object exposure times, were important for the
  first generation (engineering grade) NOAO Mosaic, dark counts are expected
  to be low in the science grade detectors.  Thus dark count exposures are
  probably not necessary.
  </p>
  <p>
  Dome flat fields (dome flats) provide a fair basic flattening of the data
  to 2% or so, but sky flat fields (sky flats) are required to produce
  dithered data that can be combined without introducing obvious artifacts.
  Good sky flats can flatten the data to 0.1%.  In our experience twilight
  exposures do not work well.  Instead dark sky flat fields are derived from
  unregisted object exposures taken during the night or run.  If your
  observing program consists of only large extended objects or single
  pointings then you should also take some dithered exposures of <span style="font-family: monospace;">"blank"</span>
  sky.
  </p>
  <p>
  At the Mayall telescope there is a pupil image caused by reflections
  off the corrector.  For broadband photometry the effects of the pupil
  image are small but they can be reduced even further by reduction steps
  to remove the image.  One useful calibration for this removal is a
  narrowband dome flat field.  The idea is that the narrowband flat field
  has a more prominent pupil image that can be used as a template for the
  much fainter broadband pupil image.
  </p>
  <p>
  Lastly, good astrometry is required to register and stack the Mosaic
  images.  The NOAO Mosaic data contains previously determined astrometry
  recorded in the headers of the raw exposures.  This is sufficient for most
  purposes.  However, for cameras without astrometry or to generate your own
  astrometry solutions, fields with a reasonable density of stars with
  cataloged accurate coordinates must be taken.  Note that with the new
  generation of large astrometric catalogs and the large field of view of a
  mosaic, it may be that the object exposures already contain sufficient
  information for deriving new astrometric calibrations or corrections.  Note
  that this guide does not yet discuss how to create the astrometric
  coordinate system solutions.
  </p>
  </section>
  <section id="s_4_2_2__preparing_calibration_data">
  <h3>4.2.2  preparing calibration data</h3>
  <p>
  This section describes how to prepare the basic calibration data.  The
  steps are virtually the same as with the <b>ccdred</b> package and, in fact,
  the command names and parameters are the same.  The basic calibration data
  of zero level, dark count, and dome flat fields are generally taken as a
  sequence of identical exposures which are combined to minimize the noise.
  A later section discusses preparing a sky flat field calibration using the
  object exposures.
  </p>
  <p>
  The calibration exposures are individually reduced by <b>ccdproc</b> and
  then combined.  Thus, it is necessary to first set the <b>ccdproc</b>
  parameters.  Because this task knows which operations are appropriate for
  particular types of calibration exposures you can set all the parameters
  for object exposures.  Below is a typical set of parameters.  The main
  optional setting is whether or not to replace bad pixels by interpolation,
  which is purely a cosmetic correction.  However, it is recommended that
  this be done to avoid possible arithmetic problems in the processing.
  </p>
  <div class="highlight-default-notranslate"><pre>
                           I R A F
            Image Reduction and Analysis Facility
  PACKAGE = mscred
     TASK = ccdproc
  
  images  =             List of Mosaic CCD images to process
  (output =           ) List of output processed images
  (ccdtype=     object) CCD image type to process
  (noproc =         no) List processing steps only?
  
  (oversca=        yes) Apply overscan strip correction?
  (trim   =        yes) Trim the image?
  (fixpix =        yes) Apply bad pixel mask correction?
  (zerocor=        yes) Apply zero level correction?
  (darkcor=         no) Apply dark count correction?
  (flatcor=        yes) Apply flat field correction?
  (sflatco=         no) Apply sky flat field correction?
  
  (biassec=   !biassec) Overscan strip image section
  (trimsec=   !trimsec) Trim data section
  (fixfile=        BPM) List of bad pixel masks
  (zero   =       Zero) List of zero level calibration images
  (dark   =       Dark) List of dark count calibration images
  (flat   =      Flat*) List of flat field images
  (sflat  =     Sflat*) List of secondary flat field images
  (minrepl=         1.) Minimum flat field value
  
  (interac=         no) Fit overscan interactively?
  (functio=   legendre) Fitting function
  (order  =          1) Number of polynomial terms or spline pieces
  (sample =          *) Sample points to fit
  (naverag=          1) Number of sample points to combine
  (niterat=          1) Number of rejection iterations
  (low_rej=         3.) Low sigma rejection factor
  (high_re=         3.) High sigma rejection factor
  (grow   =         0.) Rejection growing radius
  
  </pre></div>
  <p>
  The overscan correction has two methods as selected by the fitting function.
  A value of <span style="font-family: monospace;">"legendre"</span> (or <span style="font-family: monospace;">"chebyshev"</span> or <span style="font-family: monospace;">"spline3"</span>) take all the overscan data
  and fit a smooth function along the column direction.  The <span style="font-family: monospace;">"order"</span> value
  of 1 shown above fits a single constant value.  This leaves to the zero
  level calibration to subtract any details of line-by-line structure.  A value
  of <span style="font-family: monospace;">"mean"</span>, <span style="font-family: monospace;">"median"</span>, or <span style="font-family: monospace;">"minmax"</span> take the mean, median, or mean excluding
  the minimum and maximum values, of the overscan at each line and subtract
  that value from that line.  The other fitting parameters are ignored.
  The advantage of this is that systematic line-by-line patterns are
  subtracted.  The disadvantage is, since the sample of overscan pixels
  is small at each line, that this can also introduce a statistical line-by-line
  pattern.  There is currently no recommendation for the NOAO Mosaic.
  </p>
  <p>
  The first step is generally to process and combine sequences of zero, dark,
  and dome flat exposures.  This is done using the tasks <b>zerocombine</b>,
  <b>darkcombine</b>, and <b>flatcombine</b>.  The combining must be done in
  the following order since the processing of later calibration data requires
  the preceding calibration data.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; zerocombine *.fits
  ms&gt; darkcombine *.fits
  ms&gt; flatcombine *.fits
  </pre></div>
  <p>
  Each of these tasks search all the exposures for a particular type so it is
  fine to specify all files, though if the file names code the type, such as
  <span style="font-family: monospace;">"dflatNNN"</span>, then one can use that as the wildcard to shorten the search of
  all the data.  Also <b>flatcombine</b> has the feature that it will combine
  the data separately for each filter.  However, you can use explicit file
  lists, templates, or @files to limit the input files.  The output combined
  names have standard default values which the above settings for
  <b>ccdproc</b> use.
  </p>
  <p>
  It is a good idea to first check that the different calibration types
  and filters are correctly identified by the software.  This is done
  using the <b>ccdlist</b> command
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; ccdlist *.fits
  </pre></div>
  <p>
  Unless you change the parameters <span style="font-family: monospace;">"mscred.backup"</span> and
  <span style="font-family: monospace;">"mscred.bkuproot"</span> the original raw files will be saved in the
  subdirectory <span style="font-family: monospace;">"Raw/"</span>.  If you want to start over, delete the processed files
  and copy the raw files back to the working directory.  If disk space is a
  concern and you are satisfied with the combined calibration files you can
  delete the individual processed calibration files.  There is a parameter in
  the combining tasks that will delete the individual files automatically
  after processing and combining.
  </p>
  </section>
  <section id="s_4_2_3_pupil_image_removal_from_flat_fields">
  <h3>4.2.3 pupil image removal from flat fields</h3>
  <p>
  NOAO Mosaic data taken at the Mayall (4meter) telescope include a pupil
  image caused by reflections off the corrector.  The magnitude of this image
  is a function of the filter and the state of the anti-reflection coatings
  on the corrector.  It is also a function of the total light, including
  from outside the field of view, and somewhat on the location of bright
  stars.
  </p>
  <p>
  It might appear at first that one simply divides the object exposures by
  the flat field as is done for the OTF display calibration.  However this is
  not photometrically correct because the pupil image is an additive light
  effect and not a detector response.  Instead the pupil image must first
  be removed from the flat field before applying it to the object data.
  The object data is then corrected after flat fielding by subtracting the
  extra light from the pupil image.
  </p>
  <p>
  The pupil image is removed from the flat field by dividing by an estimate
  of the pupil image pattern.  The challenge is to determine the pupil image
  contribution in the presence of other flat field structure.
  </p>
  <p>
  There are two current approaches to obtaining the pupil image pattern for
  removal from the data.  One is to use data from another source where the
  pupil pattern is more easily separated from the flat field pattern.  The
  second is to derive the pattern from the data assuming something about the
  form of the pattern.  In particular, to use the difference in scales
  between the larger pupil pattern and the smaller flat field pattern.
  The first approach is preferable since it better preserves fine structure
  in the pupil image but the second is needed when no other data is available.
  </p>
  </section>
  <section id="s_4_2_3_1_broadband_data">
  <h3>4.2.3.1 broadband data</h3>
  <p>
  For broadband data the recommended procedure is to obtain a narrowband
  flat field exposure.  This narrowband exposure will have a stronger pupil
  image relative to the flat field pattern and, when the pupil image
  is scaled down to match the broadband image flat field, the errors from
  the flat field response will be diminished.
  </p>
  <p>
  The pupil image is extracted from the narrowband flat field using the task
  <b>mscpupil</b>.  This task determines the background levels in a ring
  inside and outside the main pupil image and subtracts this background to
  produced the pupil image template.  Outside the outer background ring the
  template is set to zero.  In effect this is like <span style="font-family: monospace;">"scrapping off"</span> the pupil
  image from the exposure.
  </p>
  <p>
  The relevant parameters are
  </p>
  <div class="highlight-default-notranslate"><pre>
                             I R A F
              Image Reduction and Analysis Facility
      PACKAGE = mscred
         TASK = mscpupil
  
      input   =           List of input images
      output  =           List of output images
      (masks  =      BPM) List of masks
      (type   =     data) Output type
      (xc     =      27.) Pattern center offset (pixels)
      (yc     =       9.) Pattern center offset (pixels)
      (rin    =     300.) Radius of inner background ring (pixels)
      (drin   =      20.) Width of inner background ring (pixels)
      (rout   =    1500.) Radius of outer background ring (pixels)
      (drout  =      20.) Width of outer background ring (pixels)
      (funcin =chebyshev) Inner azimuthal background fitting function
      (orderin=        2) Inner azimuthal background fitting order
      (funcout=  spline3) Outer azimuthal background fitting function
      (orderou=        2) Outer azimuthal background fitting order
  *   (rfuncti=  spline3) Radial profile fitting function
  *   (rorder =       40) Radial profile fitting order
  *   (abin   =       0.) Azimuthal bin (deg)
  *   (astep  =       0.) Azimuthal step (deg)
      (niterat=        3) Number of rejection iterations
      (lreject=       3.) Low rejection rms factor
      (hreject=       3.) High rejection rms factor
      (datamin=    INDEF) Minimum good data value
      (datamax=    INDEF) Maximum good data value
      (verbose=      yes) Print information?
  </pre></div>
  <p>
  The output type is set to <span style="font-family: monospace;">"data"</span> to extract the pupil image after
  background subtraction.  The pattern center parameters are offsets from the
  astrometric center and the inner and outer radii are measured from the
  pattern center.  The default values are for the last measured Mayall
  pupil image.  The fitting parameters marked with an asterisk are not
  used when extracting the pupil image directly.
  </p>
  <p>
  The pupil image template is scaled and removed from the flat field using the
  task <b>rmpupil</b>.  The removal is done with the arithmetic
  operation
  </p>
  <div class="highlight-default-notranslate"><pre>
  I(out) = I(in) / (scale * I(template) + 1)
  </pre></div>
  <p>
  where I(out) are the output corrected pixel values, I(in) are the input
  pixel values, I(template) are the pupil image template pixel values, and
  scale is the relative scale factor to be applied.  The parameters for the
  pupil image removal task are
  </p>
  <div class="highlight-default-notranslate"><pre>
                         I R A F
          Image Reduction and Analysis Facility
  PACKAGE = mscred
     TASK = rmpupil
  
  input   =           Input mosaic exposure
  output  =           Output mosaic exposure
  template=           Template mosaic exposure
  (type   =    ratio) Type of removal
  (extname=   [2367]) Extensions for fit
  (blkavg =        8) Block average factor
  (fudge  =      1.6) Fudge factor
  (interac=      yes) Interactive?
  (mscexam=       no) Examine corrections with MSCEXAM?
  </pre></div>
  <p>
  The <span style="font-family: monospace;">"input"</span> is the broadband flat field, the <span style="font-family: monospace;">"output"</span> is the corrected flat
  field, and the <span style="font-family: monospace;">"template"</span> is the narrowband pupil image produced by
  <b>mscpupil</b>.  The type of removal for a flat field is <span style="font-family: monospace;">"ratio"</span> as given
  by the equation above.
  </p>
  <p>
  Determining the optimal scaling of the template pupil image to the input
  pupil image is normally done interactively.  The task makes a guess at
  scaling.  If this task is used non-interactively this will be the scale
  used.  When the task is used interactively the input and corrected mosaic
  exposures are displayed and then a query for a new scale is given.  By
  repeatedly adjusting the scale factor the best visual removal can be
  obtained.  When done the output corrected flat field is created using the
  last specified scale factor.  Note that to quit requires entering dummy
  special values for the scale factor.  A value of zero means to create the
  final output exposure with the last scale factor and a value of -1 means to
  quit without producing any output.
  </p>
  <p>
  Because this operation is fairly slow and iterative there are some steps
  that can be taken to it speed up.  The <span style="font-family: monospace;">"extname"</span> parameter selects just
  those extensions to look at.  For NOAO Mosaic data the default selects the
  central four extensions covered by the pupil image.  The <span style="font-family: monospace;">"blkavg"</span> parameter
  applies a block average to the input exposure and template.  This makes the
  display and iterative corrections faster.  When the best scale factor has
  been determined the entire input image at full resolution is corrected by
  the full resolution template to create the output flat field.  If one wants
  to use the facilities of <b>mscexam</b> to evaluate each iterative
  correction then the <span style="font-family: monospace;">"mscexam"</span> parameter can be set.  However, the most
  powerful estimate for the optimal scale factor is viewing the display and
  possibly blinking between the uncorrected and corrected frames.
  </p>
  </section>
  <section id="s_4_2_3_2_narrowband_data">
  <h3>4.2.3.2 narrowband data</h3>
  <p>
  For narrowband data the pupil image template must be derived from the data
  itself.  This is done by fitting the data with an axially symmetric
  pattern.  The fitting is performed by <b>mscpupil</b> with the parameters
  </p>
  <div class="highlight-default-notranslate"><pre>
                         I R A F
          Image Reduction and Analysis Facility
  PACKAGE = mscred
     TASK = mscpupil
  
  input   =           List of input images
  output  =           List of output images
  (masks  =      BPM) List of masks
  (type   =    ratio) Output type
  (xc     =      27.) Pattern center offset (pixels)
  (yc     =       9.) Pattern center offset (pixels)
  (rin    =     300.) Radius of inner background ring (pixels)
  (drin   =      20.) Width of inner background ring (pixels)
  (rout   =    1500.) Radius of outer background ring (pixels)
  (drout  =      20.) Width of outer background ring (pixels)
  (funcin =chebyshev) Inner azimuthal background fitting function
  (orderin=        2) Inner azimuthal background fitting order
  (funcout=  spline3) Outer azimuthal background fitting function
  (orderou=        2) Outer azimuthal background fitting order
  (rfuncti=  spline3) Radial profile fitting function
  (rorder =       40) Radial profile fitting order
  (abin   =       0.) Azimuthal bin (deg)
  (astep  =       0.) Azimuthal step (deg)
  (niterat=        3) Number of rejection iterations
  (lreject=       3.) Low rejection rms factor
  (hreject=       3.) High rejection rms factor
  (datamin=    INDEF) Minimum good data value
  (datamax=    INDEF) Maximum good data value
  (verbose=      yes) Print information?
  </pre></div>
  <p>
  Note that this only differs from the previously shown parameters by
  setting the <span style="font-family: monospace;">"type"</span> parameter to ratio.  Because the template is
  derived from the data itself there is no need to use <b>rmpupil</b>
  to iteratively determine a scale factor.  The <span style="font-family: monospace;">"output"</span> parameter is
  the corrected flat field.
  </p>
  <p>
  The corrected narrowband flat field will show some artifacts from fine
  structure in the pupil image.  However, a large fraction of the pupil image
  will be removed.  Later reduction steps of applying a sky flat field and
  combining with dithering further eliminate effects of this approximate
  solution to the pupil image.
  </p>
  </section>
  <section id="s_4_2_4_object_exposure_reductions">
  <h3>4.2.4 object exposure reductions</h3>
  <p>
  At this point you will have some subset of combined zero level, dark count,
  and flat field calibration data.  The calibration data is applied to
  the object exposures, either in bulk or as observations are completed,
  using the task <b>ccdproc</b>.  The command is simply
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; ccdproc &lt;files&gt;
  </pre></div>
  </section>
  <section id="s_4_2_5_pupil_image_removal_from_object_data">
  <h3>4.2.5 pupil image removal from object data</h3>
  <p>
  The pupil ring image in the object exposures is removed by subtraction
  since this is excess light.   Again this is only required for data where
  the pupil image occurs, such as from the Mayall telescope.  The tasks for
  modeling and removing the image are the same as for removal from the flat
  field except that the <span style="font-family: monospace;">"type"</span> parameter is set to <span style="font-family: monospace;">"difference"</span>.
  </p>
  </section>
  <section id="s_4_2_5_1_broadband_data">
  <h3>4.2.5.1 broadband data</h3>
  <p>
  Probably the best subtraction will be obtained by using the pupil image
  template from a narrowband flat field.  This would be the same as used
  for the flat field and extracted from the narrowband flat field using
  <b>mscpupil</b> with <span style="font-family: monospace;">"type = data"</span>.  The subtraction is carried out using
  <b>rmpupil</b> with <span style="font-family: monospace;">"type = difference"</span>.
  </p>
  <p>
  An alternative, since the pupil image is weak and the fine structure is
  unimportant, is to use <b>mscpupil</b> with <span style="font-family: monospace;">"type = difference"</span> to determine
  a smooth large scale ring pattern and subtract it from the data.  The
  iterative sigma rejection and the <span style="font-family: monospace;">"datamin"</span> and <span style="font-family: monospace;">"datamax"</span> parameters are
  used to eliminate smaller scale astronomical objects in the field from
  affecting the background fits and the ring profile fits.  For this
  application the <span style="font-family: monospace;">"abin"</span> parameter should be set to a value such as 30
  degrees and the <span style="font-family: monospace;">"astep"</span> parameter to a smaller value such as 5 degrees.
  </p>
  <p>
  The main advantage of this method is that no iterative scaling is required
  since the fit is done directly to the data.  The difficulty, though,
  is if there is a bright star or fairly extended object, particularly
  in the inner background ring, then the fit will be poor and the subtraction
  will show gross artifacts.
  </p>
  <p>
  The last alternative, and the one to use if there is no narrowband flat
  field for the template and the field has bright stars which affect fitting
  directly to the data, is to make a <span style="font-family: monospace;">"sky flat"</span> to generate the pupil image
  template.  This is done as described in the section for creating a sky
  flat.  Once the sky flat is created with the pupil image then
  <b>mscpupil</b> is used to separate the pupil image from the background and
  <b>rmpupil</b> is used to scale and subtract the image from the object
  exposures.  Note that after the pupil image is subtracted then a new
  sky flat should be created.
  </p>
  </section>
  <section id="s_4_2_5_2_narrowband_data">
  <h3>4.2.5.2 narrowband data</h3>
  <p>
  For narrowband data the two alternatives described for the broadband data
  are used.  The first is to fit and subtract a smooth ring model from each
  object exposure using <b>mscpupil</b>.  This is the same as described
  for removing the pupil image from the flat field except the <span style="font-family: monospace;">"type"</span>
  parameter is set to difference.  The second is to create a sky flat
  from disregistered exposures, extract the pupil pattern with
  <b>mscpupil</b>, and then subtract it from each object exposure using
  <b>rmpupil</b>.
  </p>
  </section>
  <section id="s_4_2_6_dark_sky_or_twilight_sky_flat_fields">
  <h3>4.2.6 dark sky or twilight sky flat fields</h3>
  <p>
  You will notice that there are two flat field corrections which can be
  performed by <b>ccdproc</b>.  The first one is for an initial flat field
  such as the dome flat obtained at the beginning of the night, a standard
  flat field from a previous night or run, or a final combined dome flat and
  sky flat from some other night or run.  The second is for a dark sky or
  twilight sky flat field prepared from the object exposures after they have
  been calibrated with the first flat field.
  </p>
  <p>
  Sky flat fields are created by combining object exposures with objects
  removed by using data in each pixel that is only sky.  In principle one
  could use exposures of the twilight sky but our experience is that these do
  not work well.  You are welcome to take some exposures and try using them.
  We have found that dark sky flat fields derived from the object exposures
  do work quite well.
  </p>
  <p>
  Mosaic observations already typically dither a field.  One will do even
  better by combining observations from other fields.  The more data used the
  better the resulting sky flat will be. The main criterion for including
  data is to avoid observations contaminated by varying background light from
  the moon or scattered light from bright stars off the field.  Of course,
  another factor that has to be considered is whether a field has a very
  large extended object which appears in many of the observations.  These
  will not be useful.
  </p>
  <p>
  The sky flat field is created using the task <b>sflatcombine</b> with
  parameters selected to reject objects appearing above a median.  We don't
  have much experience with creating sky flats currently so some
  experimentation with parameters may be required.  Below is one possibly
  set of parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
                           I R A F
            Image Reduction and Analysis Facility
  PACKAGE = mscred
     TASK = sflatcombine
  
  input   =             List of images to combine
  (output =      Sflat) Output sky flat field root name
  (combine=    average) Type of combine operation
  (reject =  avsigclip) Type of rejection
  (ccdtype=     object) CCD image type to combine
  (subsets=        yes) Combine images by subset parameter?
  (scale  =       mode) Image scaling
  (statsec=           ) Image section for computing statistics
  (nkeep  =          1) Minimum to keep (pos) or maximum to reject (neg)
  (nlow   =          1) minmax: Number of low pixels to reject
  (nhigh  =          1) minmax: Number of high pixels to reject
  (mclip  =        yes) Use median in sigma clipping algorithms?
  (lsigma =         6.) Lower sigma clipping factor
  (hsigma =         3.) Upper sigma clipping factor
  (rdnoise=    rdnoise) ccdclip: CCD readout noise (electrons)
  (gain   =       gain) ccdclip: CCD gain (electrons/DN)
  (snoise =         0.) ccdclip: Sensitivity noise (fraction)
  (pclip  =       -0.5) pclip: Percentile clipping parameter
  (blank  =         1.) Value if there are no pixels
  (grow   =         3.) Radius (pixels) for neighbor rejection
  </pre></div>
  <p>
  This task is a combination of <b>ccdproc</b> to first process the images, if
  they have not previously been processed, and <b>combine</b> to combine the
  offset images with rejection of object pixels.  A new feature of this
  task is the <span style="font-family: monospace;">"grow"</span> parameter which now provides a two dimensional
  circular rejection of pixels around pixels rejected by the rejection
  algorithm.  Whatever rejection algorithm is used it is likely that
  the best results will be when the clipping sigmas are non-symmetric as
  shown above.  Note that a very low rejection threshold or very large grow
  radius will make the task quite slow.
  </p>
  <p>
  After producing a good sky flat that has no evidence of objects it may
  be applied directly to the data by using it as the second flat field
  correction.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; ccdproc &lt;files&gt; sflatcor=yes sflat=Sflat*
  </pre></div>
  <p>
  Note that the object exposures used in creating the sky flat will already
  have been processed except for the application of the sky flat so
  <b>ccdproc</b> will only apply the sky flat field calibration.
  </p>
  <p>
  The sky flat field includes corrections at all scales from pixel-to-pixel
  sensitivity variations to large scale illumination differences.  If the
  signal-to-noise is poorer than the dome flat field you might wish to apply
  a filtering/smoothing operation to the sky flat data thus relying on the
  dome flat field for the pixel-to-pixel sensitivity calibration and the sky
  flat field for larger scale illumination corrections.  There are a number
  of filtering tasks in IRAF.  A median is a good filter and there is the
  choice of a ring median or box median.  To apply one of these general
  filtering tasks you would use <b>msccmd</b> to run it on all the CCDs
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; msccmd
  msccmd: median $input $output 10 10
  Input files: SflatV
  Output files: SflatMedV
  msccmd: q
  </pre></div>
  <p>
  Because the object exposures are first processed with the dome flat (or
  other flat field) you would normally run <b>ccdproc</b> again on the data
  using the sky flat and any observations that have not been processed at all
  will use both the dome flat and the sky flat.  However, if you want to make
  a single flat field to apply to raw data, say if starting over or using it
  for a second night, you can combine the two flat field corrections into a
  single flat field to be used as the only flat field correction.  This is
  done by multiplying the two flat fields using <b>mscarith</b>
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; mscarith FlatV * SflatV FinalflatV
  </pre></div>
  </section>
  <section id="s_4_2_7_the_variable_pixel_scale_and_zero_point_uniformity">
  <h3>4.2.7 the variable pixel scale and zero point uniformity</h3>
  <p>
  A key assumption in the traditional reduction of CCD images is that the
  pixel scale is uniform and that a properly reduced blank sky image will
  have a uniform and flat appearance.  Unfortunately, this is not correct
  when the pixel scale varies over the field.  In the case of the NOAO Mosaic
  at the Mayall telescope, the pixel scale decreases approximately
  quadratically from the field center, with the pixels in the field corners
  being 6% smaller in the radial direction, and 8% smaller in area.  Pixels
  in field corners thus would properly detect only 92% of the sky level seen
  in the field center, even with uniform sensitivity.  At the same time the
  same number of <i>total</i> photons would be detected from a star regardless
  of how many pixels the PSF would be distributed over.  Forcing the sky to
  be uniform over the image has the deleterious effect of causing the
  photometric zeropoint to vary from center to field corners by 8%.  Note
  that this effect is different from vignetting where the flux actually
  delivered to the image margins is less than that at the center, an effect
  that <i>is</i> corrected by the flat field.
  </p>
  <p>
  In practice, the photometric effect of the variable pixel scale can be
  ignored provided that the reduced images will be part of a dither-sequence
  to be stacked later on.  As discussed below, prior to stacking the images
  they first must be re-gridded, which produces pixels of essentially
  constant angular scale.  This is done with the <b>mscimage</b> task, which
  re-grids the pixels and has a <span style="font-family: monospace;">"flux conservation"</span> option that can scale the
  pixels photometrically by the associated area change.  If this function is
  disabled, then <span style="font-family: monospace;">"improperly"</span> flattened images will have a uniform zero point
  restored.  In short, the flat field adjusted (if inappropriately) for the
  different pixel sizes, so <b>mscimage</b> would then do no further
  adjustment.  Stars would be too bright in the corners of the flattened
  images, but after re-gridding, their total fluxes would be seen to be
  scaled down to the appropriate values.
  </p>
  <p>
  If the mosaic CCD images are to be analyzed individually, as might be done
  for standard star fields, then after the flat field reductions are complete
  the differential scale effects must be restored.  At present we are
  developing a routine in the <b>mscred</b> package to do this, without
  actually re-gridding the image.  The correction process is simple; the
  scale at any point in the Mosaic field is already known from the astrometry
  so one just calculates and multiplies by the correction.  The final image
  would appear to have a variable sky level, but would be photometrically
  uniform.
  </p>
  </section>
  <section id="s_4_3_coordinate_calibration">
  <h3>4.3 coordinate calibration</h3>
  <p>
  For some projects the basic flux calibrated CCD exposures may be all that
  is required.  However, if you want to obtain coordinate information or
  combine multiple exposures which are dithered on the sky or taken with
  different filters, you must calibrate the celestial world coordinate
  system (WCS) of the data.  This may be done in an absolute or relative
  sense; an absolute calibration ties the data coordinates to catalog
  coordinates while a relative calibration ties multiple exposures to the
  same coordinates.
  </p>
  <p>
  Determining the WCS from scratch is a complicated business and requires
  special observations of astrometry fields.  However, for NOAO Mosaic data a
  standard coordinate calibration determined earlier is automatically
  inserted into your data by the data capture agent.  The default coordinate
  system is sufficiently accurate for most purposes and just requires some
  small adjustments as described below.  To piece a single exposure into a
  single image that does not require registration to any other data you may
  use the default WCS and skip the WCS calibration steps.
  </p>
  <p>
  The WCS is a mapping from pixels in the mosaic data to celestial
  coordinates relative to a reference point on the sky.  The reference point,
  or zero point, is set using the telescope pointing coordinate.  The
  telescope pointing is generally off by a small amount, though it could be
  completely wrong in some hardware/software error situations.  In addition,
  differential atmospheric refraction introduces small axis scale changes and
  rotations, which are significant due to the large field of view of the
  mosaic even during the course of single set of dithered exposured.
  Putting observations from different filters onto the same coordinate system
  also requires mapping small scale changes, since currently there is only a
  single standard WCS solution derived through one filter.  [In the future
  filter dependent solutions will be made available.]
  </p>
  <p>
  The WCS calibration operations consist of adjusting the standard coordinate
  system calibration to a desired zero point and applying small axis
  scale changes and rotations.  This is done using objects (usually stars) in
  the exposures.  Unlike a full WCS calibration, which requires a high
  density of stars with accurate catalog coordinates, the adjustments to the
  default WCS calibration require only a few objects; only one objects is
  needed to provide a zero point correction.
  </p>
  <p>
  The WCS adjustments are determined by specifying coordinates for one or
  more objects in the data.  The coordinates can be obtained from a reference
  catalog or, more commonly, by measuring coordinates from one reference
  exposure to which other exposures are to be <span style="font-family: monospace;">"registered"</span>.  A combination of
  using a catalog coordinate for one object in the field to set the zero
  point in a reference exposure and then measuring the positions of other
  stars in the reference image based on that zero point calibration may also
  be done.
  </p>
  <p>
  The two tasks you will use are <b>msczero</b> and <b>msccmatch</b>.
  <b>Msczero</b> is used to interactively set the zero point of the
  coordinates, register multiple exposures closely, and generate a list of
  coordinates in a reference exposure to which other exposures in a dither
  set are registered.  <b>Msccmatch</b> finds objects at the positions
  specified by a list of coordinates and determines corrections for the zero
  point, axis scale change, and axis rotation.
  </p>
  </section>
  <section id="s_4_3_1_setting_coordinate_zero_points_and_measuring_coordinates">
  <h3>4.3.1 setting coordinate zero points and measuring coordinates</h3>
  <p>
  <b>Msczero</b> is an interactive display task for mosaic exposures that
  allows measuring coordinates and adjusting the WCS zero point.  The task
  parameters are shown below.  The last set of parameters (starting with
  <span style="font-family: monospace;">"ra"</span>) are for the task to query and maintain lists.
  </p>
  <div class="highlight-default-notranslate"><pre>
                           I R A F
            Image Reduction and Analysis Facility
  PACKAGE = mscred
     TASK = msczero
  
  images  =             List of mosaic exposures
  (nframes=          2) Number of frames to use
  (logfile=    default) Log file for measurements
  
  ra      =             RA (hours)
  dec     =             DEC (degrees)
  update  =        yes  Update WCS zero point?
  (fd1    =           )
  (fd2    =           )
  </pre></div>
  <p>
  The task displays each exposure in the list, in turn, and responds to
  cursor key commands.  You can go forward and backward through the input
  list or quit at any point.  The exposures are displayed by cycling through
  the specified number of frames starting with the first frame.  As an aid to
  efficiency, if the exposure is already loaded in the appropriate frame then
  the display step is skipped.
  </p>
  <p>
  This task has several uses (type <span style="font-family: monospace;">'?'</span> to get the list of command options):
  </p>
  <div class="highlight-default-notranslate"><pre>
  1. Set the WCS zero point by specifying the coordinate of a star.
  2. Create a list of coordinates for use with <b>msccmatch</b> and <b>mscimatch</b>.
  3. Report coordinates at the cursor position.
  </pre></div>
  <p>
  It may be that the WCS zero points, based on the telescope
  pointing coordinates, are accurate enough that you can use this task on
  only a reference exposure to generate a list of coordinates for use with
  <b>msccmatch</b> and <b>mscimatch</b>.  However, because it is fairly quick
  to explicitly check and set the zero point of all the exposures in a dither
  set to the same coordinate for a common reference star, it is recommended
  you do this first.
  </p>
  <p>
  To check and set the zero points for a set of dithered exposures run
  <b>msczero</b> with a list of the exposures
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; msczero @field1
  </pre></div>
  <p>
  After the first exposure is displayed either find a reasonably bright
  unsaturated star which will be in all the exposures or find a star whose
  coordinate is known from a catalog such as the HST Guide Star Catalog.
  Move the cursor to the star and type <span style="font-family: monospace;">'z'</span> (zero) to invoke a centering algorithm.
  Note that even though the exposure may be displayed at lower resolution the
  centering is done with the full resolution data.  The task will then tell
  you what it thinks the coordinate is and ask you for a new coordinate.  The
  first time <span style="font-family: monospace;">'z'</span> is typed it will prompt with the measured coordinate and
  thereafter it will prompt with the last entered value.  If you are
  referencing all the exposures to the first exposure in the list accept the
  measured coordinate (and write the value down in case you need it later)
  otherwise enter the desired coordinate.
  </p>
  <p>
  Note that all further measurements of the image will automatically
  apply the measured zero point correction but the exposure WCS is not
  actually updated until you type <span style="font-family: monospace;">'n'</span> (next) or <span style="font-family: monospace;">'q'</span> (quit).  If you want to print
  coordinates without changing the zero point correction use the space bar
  or <span style="font-family: monospace;">'c'</span> (center) to center on an object and print the centered coordinate.
  </p>
  <p>
  If you changed the WCS zero point you will be shown the zero point offsets and
  given the option to update the WCS in the data file when you type <span style="font-family: monospace;">'n'</span>.
  Then the next exposure in the list will be displayed.  Find the same star
  and type <span style="font-family: monospace;">'z'</span> again.  Since it will retain the last entered coordinate you
  should only need to accept the prompted coordinates.  When you have done
  this for all the exposures their coordinate systems will be registered at
  least at that point.
  </p>
  <p>
  The WCS in the dither set may still not be registered over all the field due
  to refraction effects.  Also the intensity scales of the dithered exposures
  may not be the same due to changes in transparency and sky brightness.
  These effects are calibrated by matching objects throughout the
  field in position and brightness.  This requires a list of coordinates
  tied to one of the dithered exposures as a reference.  Usually the
  first exposure in the set is used as the reference.  <b>Msczero</b>
  is used to create a list from objects in the reference exposure.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; msczero obj021
  </pre></div>
  <p>
  Select objects, usually stars, throughout the field and type <span style="font-family: monospace;">'x'</span> for each
  one.  This will center on the object and and record the coordinate in a
  logfile.  The default logfile name <span style="font-family: monospace;">"default"</span> creates a log file
  beginning with <span style="font-family: monospace;">"Coords."</span> and followed by the name of the exposure.
  In the example this will be <span style="font-family: monospace;">"Coords.obj021"</span>.
  </p>
  <p>
  To be useful for coordinate matching this list should have a good
  number of stars, say three or four from each CCD, with emphasis on the
  field edges but allowing for the dithering.  For the intensity matching you
  want to have stars with a range of brightness (though not saturated or
  extremely faint) and which are mostly isolated so that a region around them
  may be used for sky.  The lists for the coordinate and intensity matching
  do not have to be the same but it is reasonable to just create one
  list.
  </p>
  </section>
  <section id="s_4_3_2_matching_coordinate_systems">
  <h3>4.3.2 matching coordinate systems</h3>
  <p>
  The task <b>msccmatch</b> determines and applies a linear correction to the
  WCS to match objects, generally stars, in an exposure
  to a set of reference celestial coordinates.  This correction maintains the
  detector geometry and optical distortions while adjusting for changes in
  apparent sky position such as produced by atmospheric refraction and
  telescope pointing errors.  The linear correction consists of a zero point
  shift, scale changes in the right ascension and declination axes, and
  rotations of the axes.
  </p>
  <p>
  To use this task you need a list of reference celestial coordinates, right
  ascension in hours and declination in degrees, and the mosaic exposure
  coordinate system must be relatively close to the reference coordinate
  system.  The default WCS plus telescope pointing may be close enough, but if
  not you would use <b>msczero</b> to register the zero points at some point
  in the exposures.  Since it is relatively simple to register a set of
  dithered exposures to a common star with <b>msczero</b> this is
  recommended procedure before using <b>msccmatch</b>.
  </p>
  <p>
  The reference coordinates should cover all of the mosaic field of
  view to be sensitive to the small rotation and scale effects.  The
  coordinate list might be obtained from a catalog or measured from one of the
  exposures to which other overlapping exposures will be matched.
  For the purposes of making a well aligned stacked image from a set of
  dithered exposures one generally uses one of the exposures as the
  source of the reference coordinates.
  </p>
  <p>
  <b>Msccmatch</b> operates on a set of input mosaic exposures; each in turn.
  For an exposure it converts each input celestial coordinate to a pixel
  coordinate in one of the extensions using the current WCS.  If the
  coordinate does not fall in any extension the coordinate is not used.  The
  pixel coordinate is used as a starting point for the <b>apphot.center</b>
  task.  If the centering fails for some reason, such as the object being too
  near the edge or the final position being too far from the initial
  position, the coordinate is not used.  For those objects successfully found
  a fit is made between the original celestial coordinates and the measured
  coordinates expressed as arc seconds from the exposure tangent point.  The
  fit is constrained to yield some combination of shift, scale change, and
  rotation for each of the celestial coordinate axes.  These parameters are
  then used to update the exposure WCS so that the adjusted measured
  coordinates best agrees with the reference coordinates.
  </p>
  <p>
  The task parameters are shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
                             I R A F
              Image Reduction and Analysis Facility
  PACKAGE = mscred
      TASK = msccmatch
  
  input   =               List of input mosaic exposures
  coords  =               Coordinate file (ra/dec)
  (nfit   =            4) Min for fit (&gt;0) or max not found (&lt;=0)
  (rms    =           2.) Maximum fit RMS to accept (arcsec)
  (maxshif=           5.) Maximum centering shift (arcsec)
  (fitgeom=     rxyscale) Fitting geometry
  (update =          yes) Update coordinate systems?
  (interac=          yes) Interactive?
  (fit    =          yes) Interactive fitting?
  (verbose=          yes) Verbose?
  accept  =          yes  Accept solution?
  </pre></div>
  <p>
  The input is a list of mosaic exposures and a file of reference
  celestial coordinates.  The exposures should all include a significant
  number of objects from the list of coordinates.
  </p>
  <p>
  The task can be run interactively or non-interactively based on the
  <span style="font-family: monospace;">"interactive"</span> parameter.  In interactive mode you can graphically
  interact with the fitting (selected with the <span style="font-family: monospace;">"fit"</span> parameter) and
  accept or reject a fit based on the printed fit parameters.  The fitting is
  done using the task <b>geomap</b> and the interactive mode allows you to
  view the distribution of coordinates, residuals verses the input
  coordinates, delete bad values, and possibly change the fitting constraints
  (see the help for <b>geomap</b> for more information).
  </p>
  <p>
  The linear transformation may be constrained by the <span style="font-family: monospace;">"fitgeometry"</span>
  parameter as described in the help for <b>geomap</b>.  This may be
  desirable if there are only a few coordinates or if you want to impose
  some physical assumption.  Note that the effects of atmospheric refraction
  actually do cause independent scale changes and rotations in the
  two axes so the default <span style="font-family: monospace;">"rxyscale"</span> should be used.
  </p>
  <p>
  There are some constraints which are placed on the task.  The
  <span style="font-family: monospace;">"maxscale"</span> parameter limits how far the objects may be found from the
  initial coordinates.  This constraint protects against incorrect
  identifications and tells the centering routine how much of the image to
  look at.  This parameter should be as small as possible consistent with the
  errors in the WCS.  If you first zero the coordinates then the objects
  should be found quite close to the initial coordinates.  When the
  <span style="font-family: monospace;">"verbose"</span> parameter is set the results of the centering will be printed
  consisting of the image extension name, the final pixel coordinates, the
  shift in pixel coordinates from the initial value, and the formal
  uncertainties in the pixel coordinates.  If an error occurs one of the
  error codes from <b>apphot.center</b> will be reported such as <span style="font-family: monospace;">"BigShift"</span>
  for objects with too big a shift from the initial position and <span style="font-family: monospace;">"EdgeImage"</span>
  for objects to near the edge of the image.
  </p>
  <p>
  The <span style="font-family: monospace;">"nfit"</span> parameter requires a certain number of coordinates to
  be included in the fit.  If specified as a negative number the parameter
  is interpreted as a maximum number that may be lost from the input
  list due to being off the exposure or failing to be centered.  The
  <span style="font-family: monospace;">"rms"</span> parameter requires that the final RMS of the residuals about
  the fit for each axis be less than a certain value.
  </p>
  </section>
  <section id="s_4_4_putting_the_pieces_together">
  <h3>4.4 putting the pieces together</h3>
  <p>
  This section tells you how to make single images from each multiextension
  exposure and how to combine sets of dithered images into a final deep image
  free from gaps and artifacts.  Obtaining good results depends on having
  well-flattened data, a uniform sky, a dither pattern that samples the gaps
  and bad regions of the detectors, and accurately registered world
  coordinates.  Most difficulties are caused by variable sky conditions or
  scattered light within a dither sequence or the data used to create a sky
  flat.
  </p>
  </section>
  <section id="s_4_4_1_removing_sky_gradients">
  <h3>4.4.1 removing sky gradients</h3>
  <p>
  Any sky level mismatches when combining dithered exposures produce
  artifacts in the final image.  The three sources of such mismatches are sky
  gradients, sky level differences between the CCDs, and sky level
  differences between exposures.  While the flat field calibration,
  particularly with a sky flat, should remove differences in sky levels
  between CCDs, in practice there may still be small errors.  And the flat
  field will not deal with sky gradients across the large field of view.
  Exposure-to-exposure sky brightness variations can be dealt with at a later
  stage but even this is tricky.
  </p>
  <p>
  The best final result is obtained by fitting a low order surface (a plane
  or quadratic) to the sky and subtracting it from each CCD of each object
  exposure at this stage.  This will force the sky to be zero for all CCDs
  and all exposures.  Note that if one wants to preserve a sky level for
  statistical reasons it is possible to add a uniform constant after the
  subtraction to all the data (or add the constant to the final dither
  stacked image).
  </p>
  <p>
  To fit and subtract a sky and sky gradient the combination of
  <b>imsurfit</b> and <b>msccmd</b> is used.  With <b>imsurfit</b> use the
  option to fit to medians in large blocks to remove the effects of objects.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; msccmd
  msccmd: imsurfit $input $output xo=2 yo=2 type=resid xm=100 ym=100
  Input files: obj*
  Output files: obj*
  msccmd: q
  </pre></div>
  <p>
  In this example the input and output are the same, replacing the original
  by the sky subtracted data, but one can create new output files if
  desired.  Note that x and y orders of 2 correspond to a plane and orders of
  3 correspond to a quadratic surface.
  </p>
  </section>
  <section id="s_4_4_2_constructing_single_images">
  <h3>4.4.2 constructing single images</h3>
  <p>
  Making a single image from a mosaic exposure is done by mapping the pixels
  from each extension to a single uniform grid on the sky.  The WCS
  calibrations described in previous sections provide this.  For making
  a single image from a single exposure the WCS calibration is not critical
  and the default WCS is sufficient.  For combining multiple dithered
  exposures all the exposures must be registered to a common coordinate system,
  either relative to one reference exposure or to a set of catalog
  stars, and each exposure must be resampled to the same final
  coordinate system.
  </p>
  <p>
  The task that makes single images from mosaic exposures is <b>mscimage</b>.
  Its parameters are shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
                           I R A F
            Image Reduction and Analysis Facility
  PACKAGE = mscred
     TASK = mscimage
  
  input   =           List of input mosaic exposures
  output  =           List of output images
  (referen=         ) Reference image
  (pixmask=      yes) Create pixel mask?
  (verbose= )_.verbose) Verbose output?
  
                      # Resampling parameters
  (blank  =       0.) Blank value
  (interpo=   linear) Interpolant for data
  (minterp=   linear) Interpolant for mask
  (fluxcon=       no) Preserve flux per unit area?
  (ntrim  =        7) Edge trim in each extension
  (nxblock=     2048) X dimension of working block size in pixels
  (nyblock=     1024) Y dimension of working block size in pixels
  
                                  # Geometric mapping parameters
  (interac=       no) Fit mapping interactively?
  (nx     =       10) Number of x grid points
  (ny     =       20) Number of y grid points
  (fitgeom=  general) Fitting geometry
  (functio=chebyshev) Surface type
  (xxorder=        4) Order of x fit in x
  (xyorder=        4) Order of x fit in y
  (xxterms=     half) X fit cross terms type
  (yxorder=        4) Order of y fit in x
  (yyorder=        4) Order of y fit in y
  (yxterms=     half) Y fit cross terms type
  </pre></div>
  <p>
  An output image is created for each input mosaic exposure.  The output
  image is created with a coordinate system defined by the specified
  <span style="font-family: monospace;">"reference"</span> image.  If no reference image is specified then the first
  input mosaic exposure is used to define a simple tangent plane coordinate
  system with optical distortions removed, and that coordinate system is used
  for all the input mosaic exposures.  The important point is that for a set
  of dithered exposures all the output images must be created with the same
  coordinate system grid so that they may be combined by simple integer
  shifts along the image axes.
  </p>
  <p>
  The normal usage is to specify all the mosaic exposures in a dither set as
  the input, give a matching list of output images, and leave the reference image unspecified.  If all the exposures in a dither set are not done at the
  same time then you must specify one of the earlier output images as the
  reference image to continue to create the output images on the same
  coordinate grid.
  </p>
  <p>
  The output images are created with a size that just covers the input data
  and initially filled with the specified <span style="font-family: monospace;">"blank"</span> value.  This is the
  value that the mosaic gaps will have in the final output image.  Then each
  extension is resampled into the appropriate part of the output image.  The
  coordinate mapping is generated by <b>geomap</b> using the geometric mapping
  parameters which you don't need to change.  The resampling is done with the
  specified interpolation function.  The small rotations in the CCDs produce
  edge effects in the interpolated output pieces so a small trim is required
  to eliminate these.  [At the time this document was prepared the best value
  for the new science grade NOAO Mosaic had not been determined.]
  </p>
  <p>
  Linear interpolation is the fastest and most straightforward.  Other
  interpolation functions are available.  In particular sinc interpolation is
  now available as an add-on option (see the <b>mscred</b> installation
  instructions).  Experience with sinc interpolation shows that it is not
  overly slow and does provide improved results; particularly with
  maintaining the statistical characteristics of the sky noise.  The
  <span style="font-family: monospace;">"minterpolant"</span> parameter allows using a faster and more local interpolation
  function for the mask.  This is particularly useful when using sinc
  interpolation of the data to allow flagging only around the actual bad
  pixels and not extending out as far as the sinc interpolation does.
  </p>
  <p>
  It is useful for the later combining step to make bad pixel masks that
  reflect the interpolation and resampling from the input data.  These
  may be created by setting the <span style="font-family: monospace;">"pixmask"</span> parameter.  If this parameter
  is set and the input mosaic data have bad pixel masks defined through
  the header BPM keywords (default bad pixel masks are provided in
  the NOAO Mosaic data) then the masks will be interpolated in exactly
  the same way as the data.  The interpolated masks will appear in the
  working directory with names related to the output image names and
  with the output images containing the BPM keyword pointing to these
  masks.  The input bad pixel masks are assumed to have zero for good
  data and one for bad data and the output masks have zero for good
  data and values between zero and ten thousand for bad data.  The
  value is the result of interpolation and reflects the relative
  contribution of good and bad data.
  </p>
  <p>
  The <span style="font-family: monospace;">"fluxconserve"</span> parameter applies a pixel area correction if
  selected.  As discussed earlier, standard flat fielding distorts the flux
  per unit area in pixels of different projected size by making them have the
  same flux per pixel.  In effect this applies half of the flux conservation
  operation by adjusting the pixel values without adjusting the pixel sizes.
  <b>Mscimage</b> does the second half by adjusting the pixel sizes.  So for
  standard flat fielded data, the usual route to making a combined dithered
  image, the flux conservation parameter should not be used to arrive at a
  proper final flux per unit area in the resampled data.  Flux conservation
  would only be used if the input mosaic data has previously been corrected
  back to proper flux per unit area through adjustment of the flat field or
  data for the variable pixel size inherent in the mosaic coordinate system.
  </p>
  <p>
  Below are two examples; one using prepared @files and one illustrating
  advanced usage of filename templates.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; mscimage @dither1 @outdither1 pixmask+
  ms&gt; mscimage obj02![2-5]* %obj%mos%02![2-5]* pixmask+
  </pre></div>
  <p>
  In the second example the input template expands to obj022.fits to
  obj025.fits and the output template matches the input template using the
  first part of the %% substitution field and then replaces the <span style="font-family: monospace;">"obj"</span> with
  <span style="font-family: monospace;">"mos"</span> to give output images mos022.fits to mos025.fits.
  </p>
  </section>
  <section id="s_4_4_3_matching_intensity_scales">
  <h3>4.4.3 matching intensity scales</h3>
  <p>
  When stacking dithered exposures (the single images created in the previous
  step) to fill in the mosaic gaps and remove bad pixels and cosmic ray
  events it is critical that the intensity scales of the images match.
  Otherwise you will see artifacts from the gaps, places with bad data, and
  around objects as the combined intensity level jumps when data from an
  exposure is missing or rejected.  Also the rejection algorithms require
  that the image intensities match both at the sky level and in the objects.
  </p>
  <p>
  There are two parameters that must be determined to match the intensity
  scales.  One is a additive offset caused by sky brightness variations.  The
  second is a multiplicative scale change caused by transparency and exposure
  time variations.  Matching the intensity scales for a set of dithered
  exposures consists of determining values for these two scaling parameters
  relative to a reference exposure and setting them in the image headers.
  The actual adjustment of the pixels values occurs when stacking the
  exposures.
  </p>
  <p>
  The intensity matching values are determined by the task <b>mscimatch</b>.
  The task parameters are shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
                         I R A F
          Image Reduction and Analysis Facility
  PACKAGE = mscred
     TASK = mscimatch
  
  input   =           List of images
  coords  =           File of coordinates
  (scale  =      yes) Determine scale?
  (zero   =       no) Determine zero offset?
  (box1   =       21) Inner box size for statistics
  (box2   =       51) Outer box size for statistics
  (lower  =       1.) Lower limit for good data
  (upper  =    INDEF) Upper limit for good data
  (niterat=        3) Number of sigma clipping iterations
  (sigma  =       3.) Sigma clipping factor
  (interac=       no) Interactive?
  (verbose=      yes) Verbose?
  </pre></div>
  <p>
  The input is a list of images to be matched and a file of celestial
  coordinates (RA in hours and DEC in degrees) to use in computing the
  matching parameters.  The input images are the single images constructed
  from the mosaic exposures for a set of dithered observations.
  </p>
  <p>
  The parameters <span style="font-family: monospace;">"scale"</span> and <span style="font-family: monospace;">"zero"</span> select whether to determine the
  multiplicative scale, the zero level offsets, or both.  If the sky has been
  subtracted at an earlier stage (as recommended) then only the
  multiplicative scale difference needs to be determined.  The advantage of
  subtracting the sky earlier is that scale determination becomes better
  constrained.  Also determining the sky from photometry (as done by this
  task) is less robust than the surface fitting which uses all of the sky
  data.
  </p>
  <p>
  The scaling parameters are determined by measuring the mean flux in a set
  of matching regions between each input image.  The centers of the regions
  are specified by their celestial coordinates.  The list of coordinates
  should consist of the positions of objects in the field.  These objects
  should span a range of brightness.  As noted previously, you would normally
  use the same coordinate list as used with <b>msccmatch</b>, which is
  generally obtained using <b>msczero</b>.  However, you can use any IRAF task
  that produces a list of celestial coordinates from images with a WCS.  One
  possibility is to use <b>rimcursor</b> on one of the displayed single images
  with the <span style="font-family: monospace;">"wcs"</span> parameter set to <span style="font-family: monospace;">"world"</span> and the <span style="font-family: monospace;">"wxformat"</span> set to
  <span style="font-family: monospace;">"%.2H"</span> to produce right ascension values in hours instead of degrees.
  </p>
  <p>
  The now accurately aligned coordinate systems in the images are used to
  identify the matching pixel coordinate center in each image.  The regions
  to be measured consist of square boxes of the specified sizes about the
  pixel coordinate center.  There are two boxes, an inner box and an outer
  box which excludes the inner box.  The box sizes are intended to define
  photometry apertures for the objects and nearby background.  It is not
  critical that they exactly fit the objects or that the objects necessarily
  be stars but this is usually how they will be set.  Because of possible PSF
  variations the inner box should be large enough include all the light from
  stars over the whole data set.
  </p>
  <p>
  If the inner box is not fully contained in the input or reference image
  that box is not used for that pair.  Similarly the outer box must be fully
  contained in the images but if only the outer box is outside one or both
  images the measurement for the inner box may still be used.
  </p>
  <p>
  In order to exclude regions that include the gaps or bad data in one or
  both of the pair of images all pixels in a box must have values between the
  specified good data limits.  Those regions with values outside the limits
  are eliminated from the intensity matching.
  </p>
  <p>
  The mean fluxes in each region are used to simultaneously fit the relations
  </p>
  <div class="highlight-default-notranslate"><pre>
  mean_j = A_ij + B_ij * mean_i
  </pre></div>
  <p>
  for all i and j where i and j are any pair of images.  These equations are
  constrained by the fact that the scaling from image i to j, followed by the
  scaling from image j to k, must agree with the scaling from image i to
  image k.  The final scaling coefficients reported and stored in the image
  header are A_1j and B_1j, which correspond to the scalings to the first
  image in the input list.
  </p>
  <p>
  The task will attempt to reject photometry points which are discrepant.
  If the task is run interactively it will also show plots of the photometry
  flux in one image verses another.  It does this for sequential pairs of
  images.  Points can be deleted in these plots and they will be excluded
  from the data used to determine the scaling parameters.
  </p>
  <p>
  When the task is done determining the scaling factors they will be printed
  and a prompt issued to accept or not accept the results.  If the scaling
  parameters are accepted then the keywords <b>msczero</b> and <b>mscscale</b>
  are recorded in the input image header when the <span style="font-family: monospace;">"update"</span> parameter is
  set.  Note that the reference image is assigned values of 0 and 1 for these
  header keywords.
  </p>
  </section>
  <section id="s_4_4_4_making_the_final_stack_image">
  <h3>4.4.4 making the final stack image</h3>
  <p>
  After <b>mscimage</b> produces single images of each of the dithered mosaic
  exposures with a common coordinate system grid, a final image is created
  with the task <b>mscstack</b>.  The task <b>mscimatch</b> is generally used
  to match the intensity scales of the images before this step as described
  in the previous section.  However, for quick reductions or for other
  reasons the images may be stacked either with no intensity matching or
  using the <span style="font-family: monospace;">"scale"</span> and <span style="font-family: monospace;">"zero"</span> options of <b>mscstack</b>.  The task
  parameters are shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
                           I R A F
            Image Reduction and Analysis Facility
  PACKAGE = mscred
     TASK = mscstack
  
  input   =             List of images to combine
  output  =             Output image
  (plfile =           ) List of output pixel list files (optional)
  
  (combine=     median) Type of combine operation (median|average)
  (reject =       none) Type of rejection
  (masktyp=       none) Mask type
  (maskval=         0.) Mask value
  (blank  =         0.) Value if there are no pixels
  
  (scale  =  !mscscale) Image scaling
  (zero   =   !msczero) Image zero point offset
  (weight =       none) Image weights
  (statsec=           ) Image section for computing statistics
  
  (lthresh=         1.) Lower threshold
  (hthresh=      INDEF) Upper threshold
  (nlow   =          1) minmax: Number of low pixels to reject
  (nhigh  =          1) minmax: Number of high pixels to reject
  (nkeep  =          1) Minimum to keep (pos) or maximum to reject (neg)
  (mclip  =        yes) Use median in sigma clipping algorithms?
  (lsigma =         3.) Lower sigma clipping factor
  (hsigma =         3.) Upper sigma clipping factor
  (rdnoise=         0.) ccdclip: CCD readout noise (electrons)
  (gain   =         1.) ccdclip: CCD gain (electrons/DN)
  (snoise =         0.) ccdclip: Sensitivity noise (fraction)
  (sigscal=        0.1) Tolerance for sigma clipping scaling corrections
  (pclip  =       -0.5) pclip: Percentile clipping parameter
  (grow   =          0) Radius (pixels) for 1D neighbor rejection
  </pre></div>
  <p>
  This task is a simple variant of <b>combine</b> that registers the images
  using the coordinate systems and has the default threshold parameters set
  to ignore values below one DN based on the default <span style="font-family: monospace;">"blank"</span>
  value in <b>mscimage</b> for the gaps.  If you have also generated
  bad pixel masks for the resampled images you can exclude them as well by
  setting <span style="font-family: monospace;">"masktype"</span> to <span style="font-family: monospace;">"goodvalue"</span>.
  </p>
  <p>
  The real art in using this task is deciding how to scale and reject
  bad data not covered by the bad pixel masks.  A <span style="font-family: monospace;">"combine"</span> of <span style="font-family: monospace;">"median"</span>
  is the simplest but it does not optimize the signal-to-noise for the
  number of images.  If you <span style="font-family: monospace;">"average"</span> the data you will probably want
  to apply a rejection algorithm such as <span style="font-family: monospace;">"avsigclip"</span>.
  </p>
  <p>
  Careful flat fielding will make each separate image have the same sky
  level across the different CCDs.  However, the sky levels and transparency
  may still be varying from exposure to exposure.  If you simply combine
  such data you will see imprints of the gaps.  So it is generally a
  good idea to scale the images.  This is done using the <span style="font-family: monospace;">"scale"</span>
  and <span style="font-family: monospace;">"zero"</span> parameters which can be set to header keyword values,
  files containing the values, or special values to compute image
  statistics in a particular region of the data.  The recommended
  method for scaling is to use the intensity matching task <b>mscimatch</b>
  described in the previous section and use the image header keywords
  <b>mscscale</b> and <b>msczero</b> produced by that task.
  </p>
  <p>
  An example of using this task to create a final image is given below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; mscstack @field1 Field1 combine=average rej=avsigclip
  </pre></div>
  
  </section>
  
  <!-- Contents: 'Sections' '1. Introduction' '2. Multiextension FITS Files' '3. Examining Mosaic Data' '3.1 Displaying the Data' '3.1.1 On-the-Fly (OTF) Calibration' '3.1.2 Real-Time Display with the DCA' '3.2 Examining the Data' '3.3 Examining the Headers' '3.4 Determining Best Focus' '4. Data Reductions' '4.1 Some Preliminaries' '4.2 Basic CCD Calibration' '4.2.1  Calibration Data to Obtain At the Telescope' '4.2.2  Preparing Calibration Data' '4.2.3 Pupil Image Removal from Flat Fields' '4.2.3.1 Broadband Data' '4.2.3.2 Narrowband Data' '4.2.4 Object Exposure Reductions' '4.2.5 Pupil Image Removal from Object Data' '4.2.5.1 Broadband Data' '4.2.5.2 Narrowband Data' '4.2.6 Dark Sky or Twilight Sky Flat Fields' '4.2.7 The Variable Pixel Scale and Zero Point Uniformity' '4.3 Coordinate Calibration' '4.3.1 Setting Coordinate Zero Points and Measuring Coordinates' '4.3.2 Matching Coordinate Systems' '4.4 Putting the Pieces Together' '4.4.1 Removing Sky Gradients' '4.4.2 Constructing Single Images' '4.4.3 Matching Intensity Scales' '4.4.4 Making the Final Stack Image'  -->
  

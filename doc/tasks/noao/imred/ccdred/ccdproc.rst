.. _ccdproc:

ccdproc: Process CCD images
===========================

**Package: ccdred**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  ccdproc images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of input CCD images to process.  The list may include processed
  images and calibration images.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>List of output images.  If no list is given then the processing will replace
  the input images with the processed images.  If a list is given it must
  match the input image list.  <i>Note that any dependent calibration images
  still be processed in-place with optional backup.</i>
  </dd>
  </dl>
  <dl id="l_ccdtype">
  <dt><b>ccdtype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdtype' Line='ccdtype = ""' -->
  <dd>CCD image type to select from the input image list.  If no type is given
  then all input images will be selected.  The recognized types are described
  in <b>ccdtypes</b>.
  </dd>
  </dl>
  <dl id="l_max_cache">
  <dt><b>max_cache = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='max_cache' Line='max_cache = 0' -->
  <dd>Maximum image caching memory (in Mbytes).  If there is sufficient memory
  the calibration images, such as zero level, dark count, and flat fields,
  will be cached in memory when processing many input images.  This
  reduces the disk I/O and makes the task run a little faster.  If the
  value is zero image caching is not used.
  </dd>
  </dl>
  <dl id="l_noproc">
  <dt><b>noproc = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='noproc' Line='noproc = no' -->
  <dd>List processing steps only?
  </dd>
  </dl>
  <p style="text-align:center">PROCESSING SWITCHES
  
  </p>
  <dl id="l_fixpix">
  <dt><b>fixpix = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fixpix' Line='fixpix = yes' -->
  <dd>Fix bad CCD lines and columns by linear interpolation from neighboring
  lines and columns?  If yes then a bad pixel mask, image, or file must be
  specified.
  </dd>
  </dl>
  <dl id="l_overscan">
  <dt><b>overscan = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='overscan' Line='overscan = yes' -->
  <dd>Apply overscan or prescan bias correction?  If yes then the overscan
  image section and the readout axis must be specified.
  </dd>
  </dl>
  <dl id="l_trim">
  <dt><b>trim = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trim' Line='trim = yes' -->
  <dd>Trim the image of the overscan region and bad edge lines and columns?
  If yes then the data section must be specified.
  </dd>
  </dl>
  <dl id="l_zerocor">
  <dt><b>zerocor = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zerocor' Line='zerocor = yes' -->
  <dd>Apply zero level correction?  If yes a zero level image must be specified.
  </dd>
  </dl>
  <dl id="l_darkcor">
  <dt><b>darkcor = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='darkcor' Line='darkcor = yes' -->
  <dd>Apply dark count correction?  If yes a dark count image must be specified.
  </dd>
  </dl>
  <dl id="l_flatcor">
  <dt><b>flatcor = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flatcor' Line='flatcor = yes' -->
  <dd>Apply flat field correction?  If yes flat field images must be specified.
  </dd>
  </dl>
  <dl id="l_illumcor">
  <dt><b>illumcor = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='illumcor' Line='illumcor = no' -->
  <dd>Apply iillumination correction?  If yes iillumination images must be specified.
  </dd>
  </dl>
  <dl id="l_fringecor">
  <dt><b>fringecor = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fringecor' Line='fringecor = no' -->
  <dd>Apply fringe correction?  If yes fringe images must be specified.
  </dd>
  </dl>
  <dl id="l_readcor">
  <dt><b>readcor = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='readcor' Line='readcor = no' -->
  <dd>Convert zero level images to readout correction images?  If yes then
  zero level images are averaged across the readout axis to form one
  dimensional zero level readout correction images.
  </dd>
  </dl>
  <dl id="l_scancor">
  <dt><b>scancor = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scancor' Line='scancor = no' -->
  <dd>Convert zero level, dark count and flat field images to scan mode flat
  field images?  If yes then the form of scan mode correction is specified by
  the parameter <i>scantype</i>.
  </dd>
  </dl>
  <p style="text-align:center">PROCESSING PARAMETERS
  
  </p>
  <dl id="l_readaxis">
  <dt><b>readaxis = <span style="font-family: monospace;">"line"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='readaxis' Line='readaxis = "line"' -->
  <dd>Read out axis specified as <span style="font-family: monospace;">"line"</span> or <span style="font-family: monospace;">"column"</span>.
  </dd>
  </dl>
  <dl id="l_fixfile">
  <dt><b>fixfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fixfile' Line='fixfile' -->
  <dd>Bad pixel mask, image, or file.  If <span style="font-family: monospace;">"image"</span> is specified then the name is
  specified in the image header or instrument translation file.  If <span style="font-family: monospace;">"BPM"</span> is
  specified then the standard BPM image header keyword defines a bad pixel
  mask.  A bad pixel mask is a compact format (<span style="font-family: monospace;">".pl"</span> extension) with zero
  values indicating good pixels and non-zero values indicating bad pixels.  A
  bad pixel image is a regular image in which zero values are good pixels and
  non-zero values are bad pixels.  A bad pixel file specifies bad pixels or
  rectangular bad pixel regions as described later.  The direction of
  interpolation is determined by the mask value with a value of two
  interpolating across columns, a value of three interpolating across lines,
  and any other non-zero value interpolating along the narrowest dimension.
  </dd>
  </dl>
  <dl id="l_biassec">
  <dt><b>biassec</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='biassec' Line='biassec' -->
  <dd>Overscan bias strip image section.  If <span style="font-family: monospace;">"image"</span> is specified then the overscan
  bias section is specified in the image header or instrument translation file.
  Only the part of the bias section along the readout axis is used.  The
  length of the bias region fit is defined by the trim section.  If one
  wants to limit the region of the overscan used in the fit to be less
  than that of the trim section then the sample region parameter,
  <i>sample</i>, should be used.  It is an error if no section or the
  whole image is specified.
  </dd>
  </dl>
  <dl id="l_trimsec">
  <dt><b>trimsec</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trimsec' Line='trimsec' -->
  <dd>image section for trimming.  If <span style="font-family: monospace;">"image"</span> is specified then the trim
  image section is specified in the image header or instrument translation file.
  </dd>
  </dl>
  <dl id="l_zero">
  <dt><b>zero = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zero' Line='zero = ""' -->
  <dd>Zero level calibration image.  The zero level image may be one or two
  dimensional.  The CCD image type and subset are not checked for these
  images and they take precedence over any zero level calibration images
  given in the input list.
  </dd>
  </dl>
  <dl id="l_dark">
  <dt><b>dark = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dark' Line='dark = ""' -->
  <dd>Dark count calibration image.  The CCD image type and subset are not checked
  for these images and they take precedence over any dark count calibration
  images given in the input list.
  </dd>
  </dl>
  <dl id="l_flat">
  <dt><b>flat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flat' Line='flat = ""' -->
  <dd>Flat field calibration images.  The flat field images may be one or
  two dimensional.  The CCD image type is not checked for these
  images and they take precedence over any flat field calibration images given
  in the input list.  The flat field image with the same subset as the
  input image being processed is selected.
  </dd>
  </dl>
  <dl id="l_illum">
  <dt><b>illum = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='illum' Line='illum = ""' -->
  <dd>Iillumination correction images.  The CCD image type is not checked for these
  images and they take precedence over any iillumination correction images given
  in the input list.  The iillumination image with the same subset as the
  input image being processed is selected.
  </dd>
  </dl>
  <dl id="l_fringe">
  <dt><b>fringe = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fringe' Line='fringe = ""' -->
  <dd>Fringe correction images.  The CCD image type is not checked for these
  images and they take precedence over any fringe correction images given
  in the input list.  The fringe image with the same subset as the
  input image being processed is selected.
  </dd>
  </dl>
  <dl id="l_minreplace">
  <dt><b>minreplace = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minreplace' Line='minreplace = 1.' -->
  <dd>When processing flat fields, pixel values below this value (after
  all other processing such as overscan, zero, and dark corrections) are
  replaced by this value.  This allows flat fields processed by <b>ccdproc</b>
  to be certain to avoid divide by zero problems when applied to object
  images.
  </dd>
  </dl>
  <dl id="l_scantype">
  <dt><b>scantype = <span style="font-family: monospace;">"shortscan"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scantype' Line='scantype = "shortscan"' -->
  <dd>Type of scan format used in creating the CCD images.  The modes are:
  <dl>
  <dt><b><span style="font-family: monospace;">"shortscan"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"shortscan"' -->
  <dd>The CCD is scanned over a number of lines and then read out as a regular
  two dimensional image.  In this mode unscanned zero level, dark count and
  flat fields are numerically scanned to form scanned flat fields comparable
  to the observations.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"longscan"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"longscan"' -->
  <dd>In this mode the CCD is clocked and read out continuously to form a long
  strip.  Flat fields are averaged across the readout axis to
  form a one dimensional flat field readout correction image.  This assumes
  that all recorded image lines are clocked over the entire active area of the
  CCD.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_nscan">
  <dt><b>nscan</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nscan' Line='nscan' -->
  <dd>Number of object scan readout lines used in short scan mode.  This parameter
  is used when the scan type is <span style="font-family: monospace;">"shortscan"</span> and the number of scan lines
  cannot be determined from the object image header (using the keyword
  nscanrows or it's translation).
  </dd>
  </dl>
  <p style="text-align:center">OVERSCAN FITTING PARAMETERS
  
  </p>
  <p>
  There are two types of overscan (or prescan) determinations.  One determines
  a independent overscan value for each line  and is only available for a
  <i>readaxis</i> of 1.  The other averages the overscan along the readout
  direction to make an overscan vector, fits a smoothing function to the vector,
  and then evaluate and then evaluates the smooth function at each readout
  line or column.  The line-by-line determination only uses the
  <i>function</i> parameter and the smoothing determinations uses all
  the following parameters.
  </p>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"legendre"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "legendre"' -->
  <dd>Line-by-line determination of the overscan is specified by:
  <div class="highlight-default-notranslate"><pre>
    mean - the mean of the biassec columns at each line
  median - the median of the biassec columns at each line
  minmax - the mean at each line with the min and max excluded
  </pre></div>
  The smoothed overscan vector may be fit by one of the functions:
  <div class="highlight-default-notranslate"><pre>
   legendre - legendre polynomial
  chebyshev - chebyshev polynomial
    spline1 - linear spline
    spline3 - cubic spline
  </pre></div>
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 1' -->
  <dd>Number of polynomial terms or spline pieces in the overscan fit.
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample' Line='sample = "*"' -->
  <dd>Sample points to use in the overscan fit.  The string <span style="font-family: monospace;">"*"</span> specified all
  points otherwise an <b>icfit</b> range string is used.
  </dd>
  </dl>
  <dl id="l_naverage">
  <dt><b>naverage = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='naverage' Line='naverage = 1' -->
  <dd>Number of points to average or median to form fitting points.  Positive
  numbers specify averages and negative numbers specify medians.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 1' -->
  <dd>Number of rejection iterations to remove deviant points from the overscan fit.
  If 0 then no points are rejected.
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 3., high_reject = 3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_reject' Line='low_reject = 3., high_reject = 3.' -->
  <dd>Low and high sigma rejection factors for rejecting deviant points from the
  overscan fit.
  </dd>
  </dl>
  <dl id="l_grow">
  <dt><b>grow = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grow' Line='grow = 0.' -->
  <dd>One dimensional growing radius for rejection of neighbors to deviant points.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Fit the overscan vector interactively?  If yes and the overscan function type
  is one of the <b>icfit</b> types then the average overscan vector is fit
  interactively using the <b>icfit</b> package.  If no then the fitting parameters
  given below are used.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Ccdproc</b> processes CCD images to correct and calibrate for
  detector defects, readout bias, zero level bias, dark counts,
  response, iillumination, and fringing.  It also trims unwanted
  lines and columns and changes the pixel datatype.  It is efficient
  and easy to use; all one has to do is set the parameters and then
  begin processing the images.  The task takes care of most of the
  record keeping and automatically does the prerequisite processing
  of calibration images.  Beneath this simplicity there is much that
  is going on.  In this section a simple description of the usage is
  given.  The following sections present more detailed discussions
  on the different operations performed and the order and logic
  of the processing steps.  For a user's guide to the <b>ccdred</b>
  package see <b>guide</b>.  Much of the ease of use derives from using
  information in the image header.  If this information is missing
  see section 13.
  </p>
  <p>
  One begins by setting the task parameters.  There are many parameters
  but they may be easily reviewed and modified using the task <b>eparam</b>.
  The input CCD images to be processed are given as an image list.
  Previously processed images are ignored and calibration images are
  recognized, provided the CCD image types are in the image header (see
  <b>instruments</b> and <b>ccdtypes</b>).  Therefore it is permissible to
  use simple image templates such as <span style="font-family: monospace;">"*.imh"</span>.  The <i>ccdtype</i> parameter
  may be used to select only certain types of CCD images to process
  (see <b>ccdtypes</b>).
  </p>
  <p>
  The processing operations are selected by boolean (yes/no) parameters.
  Because calibration images are recognized and processed appropriately,
  the processing operations for object images should be set.
  Any combination of operations may be specified and the operations are
  performed simultaneously.  While it is possible to do operations in
  separate steps this is much less efficient.  Two of the operation
  parameters apply only to zero level and flat field images.  These
  are used for certain types of CCDs and modes of operation.
  </p>
  <p>
  The processing steps selected have related parameters which must be
  set.  These are things like image sections defining the overscan and
  trim regions and calibration images.  There are a number of parameters
  used for fitting the overscan or prescan bias section.  These are
  parameters used by the standard IRAF curve fitting package <b>icfit</b>.
  The parameters are described in more detail in the following sections.
  </p>
  <p>
  In addition to the task parameters there are package parameters
  which affect <b>ccdproc</b>.  These include the instrument and subset
  files, the text and plot log files, the output pixel datatype,
  the amount of memory available for calibration image caching,
  the verbose parameter for logging to the terminal, and the backup
  prefix.  These are described in <b>ccdred</b>.
  </p>
  <p>
  Calibration images are specified by task parameters and/or in the
  input image list.  If more than one calibration image is specified
  then the first one encountered is used and a warning is issued for the
  extra images.  Calibration images specified by
  task parameters take precedence over calibration images in the input list.
  These images also need not have a CCD image type parameter since the task
  parameter identifies the type of calibration image.  This method is
  best if there is only one calibration image for all images
  to be processed.  This is almost always true for zero level and dark
  count images.  If no calibration image is specified by task parameter
  then calibration images in the input image list are identified and
  used.  This requires that the images have CCD image types recognized
  by the package.  This method is useful if one may simply say <span style="font-family: monospace;">"*.imh"</span>
  as the image list to process all images or if the images are broken
  up into groups, in <span style="font-family: monospace;">"@"</span> files for example, each with their own calibration
  frames.
  </p>
  <p>
  When an input image is processed the task first determines the processing
  parameters and calibration images.  If a requested operation has been
  done it is skipped and if all requested operations have been completed then
  no processing takes place.  When it determines that a calibration image
  is required it checks for the image from the task parameter and then
  for a calibration image of the proper type in the input list.
  </p>
  <p>
  Having
  selected a calibration image it checks if it has been processed for
  all the operations selected by the CCDPROC parameters.
  After the calibration images have been identified, and processed if
  necessary, the images may be cached in memory.  This is done when there
  are more than two input images (it is actually less efficient to
  cache the calibration images for one or two input images) and the parameter
  <i>max_cache</i> is greater than zero.  When caching, as many calibration
  images as allowed by the specified memory are read into memory and
  kept there for all the input images.  Cached images are, therefore,
  only read once from disk which reduces the amount of disk I/O.  This
  makes a modest decrease in the execution time.  It is not dramatic
  because the actual processing is fairly CPU intensive.
  </p>
  <p>
  Once the processing parameters and calibration images have been determined
  the input image is processed for all the desired operations in one step;
  i.e. there are no intermediate results or images.  This makes the task
  efficient.  If a matching list of output images is given then the processed
  image is written to the specified output image name.  If no output image
  list is given then the corrected image is output as a temporary image until
  the entire image has been processed.  When the image has been completely
  processed then the original image is deleted (or renamed using the
  specified backup prefix) and the corrected image replaces the original
  image.  Using a temporary image protects the data in the event of an abort
  or computer failure.  Keeping the original image name eliminates much of
  the record keeping and the need to generate new image names.
  </p>
  </section>
  <section id="s_1__fixpix">
  <h3>1. fixpix</h3>
  <p>
  Regions of bad lines and columns may be replaced by linear
  interpolation from neighboring lines and columns when the parameter
  <i>fixpix</i> is set.  This algorithm is the same as used in the
  task <b>fixpix</b>.  The bad pixels may be specified by a pixel mask,
  an image, or a text file.  For the mask or image, values of zero indicate
  good pixels and other values indicate bad pixels to be replaced.
  </p>
  <p>
  The text file consists of lines with four fields, the starting and
  ending columns and the starting and ending lines.  Any number of
  regions may be specified.  Comment lines beginning with the character
  <span style="font-family: monospace;">'#'</span> may be included.  The description applies directly to the input
  image (before trimming) so different files are needed for previously
  trimmed or subsection readouts.  The data in this file is internally
  turned into the same description as a bad pixel mask with values of
  two for regions which are narrower or equal across the columns and
  a value of three for regions narrower across lines.
  </p>
  <p>
  The direction of interpolation is determined from the values in the
  mask, image, or the converted text file.  A value of two interpolates
  across columns, a value of three interpolates across lines, and any
  other value interpolates across the narrowest dimension of bad pixels
  and using column interpolation if the two dimensions are equal.
  </p>
  <p>
  The bad pixel description may be specified explicitly with the parameter
  <i>fixfile</i> or indirectly if the parameter has the value <span style="font-family: monospace;">"image"</span>.  In the
  latter case the instrument file must contain the name of the file.
  </p>
  </section>
  <section id="s_2__overscan">
  <h3>2. overscan</h3>
  <p>
  If an overscan or prescan correction is specified (<i>overscan</i>
  parameter) then the image section (<i>biassec</i> parameter) defines
  the overscan region.
  </p>
  <p>
  There are two types of overscan (or prescan) determinations.  One determines
  a independent overscan value for each line  and is only available for a
  <i>readaxis</i> of 1.  The other averages the overscan along the readout
  direction to make an overscan vector, fits a smoothing function to the vector,
  and then evaluate and then evaluates the smooth function at each readout
  line or column.
  </p>
  <p>
  The line-by-line determination provides an mean, median, or
  mean with the minimum and maximum values excluded.  The median
  is lowest value of the middle two when the number of overscan columns
  is even rather than the mean.
  </p>
  <p>
  The smoothed overscan vector determination uses the <b>icfit</b> options
  including interactive fitting.  The fitting function is generally either a
  constant (polynomial of 1 term) or a high order function which fits the
  large scale shape of the overscan vector.  Bad pixel rejection is also
  available to eliminate cosmic ray events.  The function fitting may be done
  interactively using the standard <b>icfit</b> iteractive graphical curve
  fitting tool.  Regardless of whether the fit is done interactively, the
  overscan vector and the fit may be recorded for later review in a metacode
  plot file named by the parameter <i>ccdred.plotfile</i>.  The mean value of
  the bias function is also recorded in the image header and log file.
  </p>
  </section>
  <section id="s_3__trim">
  <h3>3. trim</h3>
  <p>
  When the parameter <i>trim</i> is set the input image will be trimmed to
  the image section given by the parameter <i>trimsec</i>.  This trim
  should, of course, be the same as that used for the calibration images.
  </p>
  </section>
  <section id="s_4__zerocor">
  <h3>4. zerocor</h3>
  <p>
  After the readout bias is subtracted, as defined by the overscan or prescan
  region, there may still be a zero level bias.  This level may be two
  dimensional or one dimensional (the same for every readout line).  A
  zero level calibration is obtained by taking zero length exposures;
  generally many are taken and combined.  To apply this zero
  level calibration the parameter <i>zerocor</i> is set.  In addition if
  the zero level bias is only readout dependent then the parameter <i>readcor</i>
  is set to reduce two dimensional zero level images to one dimensional
  images.  The zero level images may be specified by the parameter <i>zero</i>
  or given in the input image list (provided the CCD image type is defined).
  </p>
  <p>
  When the zero level image is needed to correct an input image it is checked
  to see if it has been processed and, if not, it is processed automatically.
  Processing of zero level images consists of bad pixel replacement,
  overscan correction, trimming, and averaging to one dimension if the
  readout correction is specified.
  </p>
  </section>
  <section id="s_5__darkcor">
  <h3>5. darkcor</h3>
  <p>
  Dark counts are subtracted by scaling a dark count calibration image to
  the same exposure time as the input image and subtracting.  The
  exposure time used is the dark time which may be different than the
  actual integration or exposure time.  A dark count calibration image is
  obtained by taking a very long exposure with the shutter closed; i.e.
  an exposure with no light reaching the detector.  The dark count
  correction is selected with the parameter <i>darkcor</i> and the dark
  count calibration image is specified either with the parameter
  <i>dark</i> or as one of the input images.  The dark count image is
  automatically processed as needed.  Processing of dark count images
  consists of bad pixel replacement, overscan and zero level correction,
  and trimming.
  </p>
  </section>
  <section id="s_6__flatcor">
  <h3>6. flatcor</h3>
  <p>
  The relative detector pixel response is calibrated by dividing by a
  scaled flat field calibration image.  A flat field image is obtained by
  exposure to a spatially uniform source of light such as an lamp or
  twilight sky.  Flat field images may be corrected for the spectral
  signature in spectroscopic images (see <b>response</b> and
  <b>apnormalize</b>), or for iillumination effects (see <b>mkillumflat</b>
  or <b>mkskyflat</b>).  For more on flat fields and iillumination corrections
  see <b>flatfields</b>.  The flat field response is dependent on the
  wavelength of light so if different filters or spectroscopic wavelength
  coverage are used a flat field calibration for each one is required.
  The different flat fields are  automatically selected by a subset
  parameter (see <b>subsets</b>).
  </p>
  <p>
  Flat field calibration is selected with the parameter <b>flatcor</b>
  and the flat field images are specified with the parameter <b>flat</b>
  or as part of the input image list.  The appropriate subset is automatically
  selected for each input image processed.  The flat field image is
  automatically processed as needed.  Processing consists of bad pixel
  replacement, overscan subtraction, zero level subtraction, dark count
  subtraction, and trimming.  Also if a scan mode is used and the
  parameter <i>scancor</i> is specified then a scan mode correction is
  applied (see below).  The processing also computes the mean of the
  flat field image which is used later to scale the flat field before
  division into the input image.  For scan mode flat fields the ramp
  part is included in computing the mean which will affect the level
  of images processed with this flat field.  Note that there is no check for
  division by zero in the interest of efficiency.  If division by zero
  does occur a fatal error will occur.  The flat field can be fixed by
  replacing small values using a task such as <b>imreplace</b> or
  during processing using the <i>minreplace</i> parameter.  Note that the
  <i>minreplace</i> parameter only applies to flat fields processed by
  <b>ccdproc</b>.
  </p>
  </section>
  <section id="s_7__illumcor">
  <h3>7. illumcor</h3>
  <p>
  CCD images processed through the flat field calibration may not be
  completely flat (in the absence of objects).  In particular, a blank
  sky image may still show gradients.  This residual nonflatness is called
  the iillumination pattern.  It may be introduced even if the detector is
  uniformly illuminated by the sky because the flat field lamp
  iillumination may be nonuniform.  The iillumination pattern is found from a
  blank sky, or even object image, by heavily smoothing and rejecting
  objects using sigma clipping.  The iillumination calibration image is
  divided into the data being processed to remove the iillumination
  pattern.  The iillumination pattern is a function of the subset so there
  must be an iillumination correction image for each subset to be
  processed.  The tasks <b>mkillumcor</b> and <b>mkskycor</b> are used to
  create the iillumination correction images.  For more on iillumination
  corrections see <b>flatfields</b>.
  </p>
  <p>
  An alternative to treating the iillumination correction as a separate
  operation is to combine the flat field and iillumination correction
  into a corrected flat field image before processing the object
  images.  This will save some processing time but does require creating
  the flat field first rather than correcting the images at the same
  time or later.  There are two methods, removing the large scale
  shape of the flat field and combining a blank sky image iillumination
  with the flat field.  These methods are discussed further in the
  tasks which create them; <b>mkillumcor</b> and <b>mkskycor</b>.
  </p>
  </section>
  <section id="s_8__fringecor">
  <h3>8. fringecor</h3>
  <p>
  There may be a fringe pattern in the images due to the night sky lines.
  To remove this fringe pattern a blank sky image is heavily smoothed
  to produce an iillumination image which is then subtracted from the
  original sky image.  The residual fringe pattern is scaled to the
  exposure time of the image to be fringe corrected and then subtracted.
  Because the intensity of the night sky lines varies with time an
  additional scaling factor may be given in the image header.
  The fringe pattern is a function of the subset so there must be
  a fringe correction image for each subset to be processed.
  The task <b>mkfringecor</b> is used to create the fringe correction images.
  </p>
  </section>
  <section id="s_9__readcor">
  <h3>9. readcor</h3>
  <p>
  If a zero level correction is desired (<i>zerocor</i> parameter)
  and the parameter <i>readcor</i> is yes then a single zero level
  correction vector is applied to each readout line or column.  Use of a
  readout correction rather than a two dimensional zero level image
  depends on the nature of the detector or if the CCD is operated in
  longscan mode (see below).  The readout correction is specified by a
  one dimensional image (<i>zero</i> parameter) and the readout axis
  (<i>readaxis</i> parameter).  If the zero level image is two dimensional
  then it is automatically processed to a one dimensional image by
  averaging across the readout axis.  Note that this modifies the zero
  level calibration image.
  </p>
  </section>
  <section id="s_10__scancor">
  <h3>10. scancor</h3>
  <p>
  CCD detectors may be operated in several modes in astronomical
  applications.  The most common is as a direct imager where each pixel
  integrates one point in the sky or spectrum.  However, the design of most CCD's
  allows the sky to be scanned across the CCD while shifting the
  accumulating signal at the same rate.  <b>Ccdproc</b> provides for two
  scanning modes called <span style="font-family: monospace;">"shortscan"</span> and <span style="font-family: monospace;">"longscan"</span>.  The type of scan
  mode is set with the parameter <i>scanmode</i>.
  </p>
  <p>
  In <span style="font-family: monospace;">"shortscan"</span> mode the detector is scanned over a specified number of
  lines (not necessarily at sideral rates).  The lines that scroll off the
  detector during the integration are thrown away.  At the end of the
  integration the detector is read out in the same way as an unscanned
  observation.  The advantage of this mode is that the small scale, zero
  level, dark count and flat field responses are averaged in one dimension
  over the number of lines scanned.  A zero level, dark count or flat field may be
  observed in the same way in which case there is no difference in the
  processing from unscanned imaging and the parameter <i>scancor</i> may be
  no.  If it is yes, though, checking is done to insure that the calibration
  image used has the same number of scan lines as the object being
  processed.  However, one obtains an increase in the statistical accuracy of
  if they are not scanned during the observation but
  digitally scanned during the processing.  In shortscan mode with
  <i>scancor</i> set to yes, zero level, dark count and flat field images are
  digitally scanned, if needed, by the same number of scan lines as the
  object.  The number of scan lines is determined from the object image
  header using the keyword nscanrow (or it's translation).  If not found the
  object is assumed to have been scanned with the value given by the
  <i>nscan</i> parameter.  Zero, dark and flat calibration images are assumed
  to be unscanned if the header keyword is not found.
  </p>
  <p>
  If a scanned zero level, dark count or flat field image is not found
  matching the object then one may be created from the unscanned calibration
  image.  The image will have the root name of the unscanned image with an
  extension of the number of scan rows; i.e. Flat1.32 is created from Flat1
  with a digital scanning of 32 lines.
  </p>
  <p>
  In <span style="font-family: monospace;">"longscan"</span> mode the detector is continuously read out to produce an
  arbitrarily long strip.  Provided data which has not passed over the entire
  detector is thrown away, the zero level, dark count, and flat field
  corrections will be one dimensional.  If <i>scancor</i> is specified and the
  scan mode is <span style="font-family: monospace;">"longscan"</span> then a one dimensional zero level, dark count, and
  flat field correction will be applied.
  </p>
  </section>
  <section id="s_11__processing_steps">
  <h3>11. processing steps</h3>
  <p>
  The following describes the steps taken by the task.  This detailed
  outline provides the most detailed specification of the task.
  </p>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(1)' -->
  <dd>An image to be processed is first checked that it is of the specified
  CCD image type.  If it is not the desired type then go on to the next image.
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(2)' -->
  <dd>A temporary output image is created of the specified pixel data type
  (<b>ccdred.pixeltype</b>).  The header parameters are copied from the
  input image.
  </dd>
  </dl>
  <dl>
  <dt><b>(3)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(3)' -->
  <dd>If trimming is specified and the image has not been trimmed previously,
  the trim section is determined.
  </dd>
  </dl>
  <dl>
  <dt><b>(4)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(4)' -->
  <dd>If bad pixel replacement is specified and this has not been done
  previously, the bad pixel file is determined either from the task
  parameter or the instrument translation file.  The bad pixel regions
  are read.  If the image has been trimmed previously and the bad pixel
  file contains the word <span style="font-family: monospace;">"untrimmed"</span> then the bad pixel coordinates are
  translated to those of the trimmed image.
  </dd>
  </dl>
  <dl>
  <dt><b>(5)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(5)' -->
  <dd>If an overscan correction is specified and this correction has not been
  applied, the overscan section is averaged along the readout axis.  If
  trimming is to be done the overscan section is trimmed to the same
  limits.  A function is fit either interactively or noninteractively to
  the overscan vector.  The function is used to produce the overscan
  vector to be subtracted from the image.  This is done in real
  arithmetic.
  </dd>
  </dl>
  <dl>
  <dt><b>(6)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(6)' -->
  <dd>If the image is a zero level image go to processing step 12.
  If a zero level correction is desired and this correction has not been
  performed, find the zero level calibration image.  If the zero level
  calibration image has not been processed it is processed at this point.
  This is done by going to processing step 1 for this image.  After the
  calibration image has been processed, processing of the input image
  continues from this point.
  The processed calibration image may be
  cached in memory if it has not been previously and if there is enough memory.
  </dd>
  </dl>
  <dl>
  <dt><b>(7)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(7)' -->
  <dd>If the image is a dark count image go to processing step 12.
  If a dark count correction is desired and this correction has not been
  performed, find the dark count calibration image.  If the dark count
  calibration image has not been processed it is processed at this point.
  This is done by going to processing step 1 for this image.  After the
  calibration image has been processed, processing of the input image
  continues from this point.  The ratio of the input image dark time
  to the dark count image dark time is determined to be multiplied with
  each pixel of the dark count image before subtracting from the input
  image.
  The processed calibration image may be
  cached in memory if it has not been previously and if there is enough memory.
  </dd>
  </dl>
  <dl>
  <dt><b>(8)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(8)' -->
  <dd>If the image is a flat field image go to processing step 12.  If a flat
  field correction is desired and this correction has not been performed,
  find the flat field calibration image of the appropriate subset.  If
  the flat field calibration image has not been processed it is processed
  at this point.  This is done by going to processing step 1 for this
  image.  After the calibration image has been processed, processing of
  the input image continues from this point.  The mean of the image
  is determined from the image header to be used for scaling.  If no
  mean is found then a unit scaling is used.
  The processed calibration image may be
  cached in memory if it has not been previously and if there is enough memory.
  </dd>
  </dl>
  <dl>
  <dt><b>(9)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(9)' -->
  <dd>If the image is an iillumination image go to processing step 12.  If an
  iillumination correction is desired and this correction has not been performed,
  find the iillumination calibration image of the appropriate subset.
  The iillumination image must have the <span style="font-family: monospace;">"mkillum"</span> processing flag or the
  <b>ccdproc</b> will abort with an error.  The mean of the image
  is determined from the image header to be used for scaling.  If no
  mean is found then a unit scaling is used.  The processed calibration
  image may be
  cached in memory if it has not been previously and there is enough memory.
  </dd>
  </dl>
  <dl>
  <dt><b>(10)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(10)' -->
  <dd>If the image is a fringe image go to processing step 12.  If a fringe
  correction is desired and this correction has not been performed,
  find the fringe calibration image of the appropriate subset.
  The iillumination image must have the <span style="font-family: monospace;">"mkfringe"</span> processing flag or the
  <b>ccdproc</b> will abort with an error.  The ratio of the input
  image exposure time to the fringe image exposure time is determined.
  If there is a fringe scaling in the image header then this factor
  is multiplied by the exposure time ratio.  This factor is used
  for scaling.  The processed calibration image may be
  cached in memory if it has not been previously and there is enough memory.
  </dd>
  </dl>
  <dl>
  <dt><b>(11)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(11)' -->
  <dd>If there are no processing operations flagged, delete the temporary output
  image, which has been opened but not used, and go to 14.
  </dd>
  </dl>
  <dl>
  <dt><b>(12)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(12)' -->
  <dd>The input image is processed line by line with trimmed lines ignored.
  A line of the input image is read.  Bad pixel replacement and trimming
  is applied to the image.  Image lines from the calibration images
  are read from disk or the image cache.  If the calibration is one
  dimensional (such as a readout zero
  level correction or a longscan flat field correction) then the image
  vector is read only once.  Note that IRAF image I/O is buffered for
  efficiency and accessing a line at a time does not mean that image
  lines are read from disk a line at a time.  Given the input line, the
  calibration images, the overscan vector, and the various scale factors
  a special data path for each combination of corrections is used to
  perform all the processing in the most efficient manner.  If the
  image is a flat field any pixels less than the <i>minreplace</i>
  parameter are replaced by that minimum value.  Also a mean is
  computed for the flat field and stored as the CCDMEAN keyword and
  the time, in a internal format, when this value was calculated is stored
  in the CCDMEANT keyword.  The time is checked against the image modify
  time to determine if the value is valid or needs to be recomputed.
  </dd>
  </dl>
  <dl>
  <dt><b>(13)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(13)' -->
  <dd>The input image is deleted or renamed to a backup image.  The temporary
  output image is renamed to the input image name.
  </dd>
  </dl>
  <dl>
  <dt><b>(14)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(14)' -->
  <dd>If the image is a zero level image and the readout correction is specified
  then it is averaged to a one dimensional readout correction.
  </dd>
  </dl>
  <dl>
  <dt><b>(15)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(15)' -->
  <dd>If the image is a zero level, dark count, or flat field image and the scan
  mode correction is specified then the correction is applied.  For shortscan
  mode a modified two dimensional image is produced while for longscan mode a
  one dimensional average image is produced.
  </dd>
  </dl>
  <dl>
  <dt><b>(16)</b></dt>
  <!-- Sec='11. Processing Steps' Level=0 Label='' Line='(16)' -->
  <dd>The processing is completed and either the next input image is processed
  beginning at step 1 or, if it is a calibration image which is being
  processed for an input image, control returns to the step which initiated
  the calibration image processing.
  </dd>
  </dl>
  </section>
  <section id="s_12__processing_arithmetic">
  <h3>12. processing arithmetic</h3>
  <p>
  The <b>ccdproc</b> task has two data paths, one for real image pixel datatypes
  and one for short integer pixel datatype.  In addition internal arithmetic
  is based on the rules of FORTRAN.  For efficiency there is
  no checking for division by zero in the flat field calibration.
  The following rules describe the processing arithmetic and data paths.
  </p>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='12. Processing Arithmetic' Level=0 Label='' Line='(1)' -->
  <dd>If the input, output, or any calibration image is of type real the
  real data path is used.  This means all image data is converted to
  real on input.  If all the images are of type short all input data
  is kept as short integers.  Thus, if all the images are of the same type
  there is no datatype conversion on input resulting in greater
  image I/O efficiency.
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='12. Processing Arithmetic' Level=0 Label='' Line='(2)' -->
  <dd>In the real data path the processing arithmetic is always real and,
  if the output image is of short pixel datatype, the result
  is truncated.
  </dd>
  </dl>
  <dl>
  <dt><b>(3)</b></dt>
  <!-- Sec='12. Processing Arithmetic' Level=0 Label='' Line='(3)' -->
  <dd>The overscan vector and the scale factors for dark count, flat field,
  iillumination, and fringe calibrations are always of type real.  Therefore,
  in the short data path any processing which includes these operations
  will be coerced to real arithmetic and the result truncated at the end
  of the computation.
  </dd>
  </dl>
  </section>
  <section id="s_13__in_the_absence_of_image_header_information">
  <h3>13. in the absence of image header information</h3>
  <p>
  The tasks in the <b>ccdred</b> package are most convenient to use when
  the CCD image type, subset, and exposure time are contained in the
  image header.  The ability to redefine which header parameters contain
  this information makes it possible to use the package at many different
  observatories (see <b>instruments</b>).  However, in the absence of any
  image header information the tasks may still be used effectively.
  There are two ways to proceed.  One way is to use <b>ccdhedit</b>
  to place the information in the image header.
  </p>
  <p>
  The second way is to specify the processing operations more explicitly
  than is needed when the header information is present.  The parameter
  <i>ccdtype</i> is set to <span style="font-family: monospace;">""</span> or to <span style="font-family: monospace;">"none"</span>.  The calibration images are
  specified explicitly by task parameter since they cannot be recognized
  in the input list.  Only one subset at a time may be processed.
  </p>
  <p>
  If dark count and fringe corrections are to be applied the exposure
  times must be added to all the images.  Alternatively, the dark count
  and fringe images may be scaled explicitly for each input image.  This
  works because the exposure times default to 1 if they are not given in
  the image header.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The user's <b>guide</b> presents a tutorial in the use of this task.
  </p>
  <p>
  1. In general all that needs to be done is to set the task parameters
  and enter
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccdproc *.imh &amp;
  </pre></div>
  <p>
  This will run in the background and process all images which have not
  been processed previously.
  </p>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <div class="highlight-default-notranslate"><pre>
  o SUN-3, 15 MHz 68020 with 68881 floating point hardware (no FPA)
  o 8 Mb RAM, 2 Fuji Eagle disks.
  o Input images = 544 x 512 short
  o Output image = 500 x 500 real
  o Operations are overscan subtraction (O), trimming to 500x500 (T),
    zero level subtraction (Z), dark count scaling and subtraction (D),
    and flat field scaling and subtraction (F).
  o UNIX statistics
    (user, system, and clock time, and misc. memory and i/o statistics):
  
  [OTF] One calibration image and 9 object images:
  No caching:  110.6u 25.5s 3:18 68% 28+ 40K 3093+1645io   9pf+0w
  Caching:     111.2u 23.0s 2:59 74% 28+105K 2043+1618io   9pf+0w
  
  [OTZF] Two calibration images and 9 object images:
  No caching:  119.2u 29.0s 3:45 65% 28+ 50K 4310+1660io   9pf+0w
  Caching:     119.3u 23.0s 3:07 75% 28+124K 2179+1601io   9pf+0w
  
  [OTZDF] Three calibration images and 9 object images:
  No caching:  149.4u 31.6s 4:41 64% 28+ 59K 5501+1680io  19pf+0w
  Caching:     151.5u 29.0s 4:14 70% 27+227K 2346+1637io 148pf+0w
  
  [OTZF] 2 calibration images and 20 images processed:
  No caching:  272.7u 63.8u 8:47 63% 28+ 50K 9598+3713io  12pf+0w
  Caching:     271.2u 50.9s 7:00 76% 28+173K 4487+3613io  51pf+0w
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_CCDPROC">
  <dt><b>CCDPROC V2.11.2</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='CCDPROC' Line='CCDPROC V2.11.2' -->
  <dd>A new <span style="font-family: monospace;">"output"</span> parameter is available to specify an output image leaving
  the input image unchanged.  If this parameter is not specified then
  the previous behavior of <span style="font-family: monospace;">"in-place"</span> operation with an optional backup
  occurs.
  </dd>
  </dl>
  <dl id="l_CCDPROC">
  <dt><b>CCDPROC V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='CCDPROC' Line='CCDPROC V2.11' -->
  <dd>The bad pixel fixing was modified to allow use of pixel masks,
  images, or the text file description.  Bad pixel masks are the
  desired description and use of text files is only supported for
  backward compatibility.  Note that support for the trimmed
  or untrimmed conversion from text files has been eliminated.
  Line-by-line overscan/prescan subtraction is now provided with
  three simple algorithms.
  </dd>
  </dl>
  <dl id="l_CCDPROC">
  <dt><b>CCDPROC: V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='CCDPROC' Line='CCDPROC: V2.10.3' -->
  <dd>The output pixel datatypes (specified by the package parameter
  <i>pixeltype</i> have been extended to include unsigned short
  integers.  Also it was previously possible to have the output
  pixel datatype be of lower precision than the input.  Now the
  output pixel datatype is not allowed to lose precision; i.e.
  a real input image may not be processed to a short datatype.
  For short scan data the task now looks for the number of scan lines in the
  image header.  Also when a calibration image is software scanned a new
  image is created.  This allows processing objects with different numbers of
  scan lines and preserving the unscanned calibration image.
  It is an error if no biassec is specified rather than defaulting to
  the whole image.
  The time, in a internal format, when the CCDMEAN value is calculated is
  stored in the CCDMEANT keyword.  The time is checked against the image
  modify time to determine if the value is valid or needs to be recomputed.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <div class="highlight-default-notranslate"><pre>
  instruments, ccdtypes, flatfields, icfit, ccdred, guide, mkillumcor,
  mkskycor, mkfringecor
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' '1. Fixpix' '2. Overscan' '3. Trim' '4. Zerocor' '5. Darkcor' '6. Flatcor' '7. Illumcor' '8. Fringecor' '9. Readcor' '10. Scancor' '11. Processing Steps' '12. Processing Arithmetic' '13. In the Absence of Image Header Information' 'EXAMPLES' 'TIME REQUIREMENTS' 'REVISIONS' 'SEE ALSO'  -->
  

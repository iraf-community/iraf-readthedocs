.. _ccdproc:

ccdproc: Process mosaic exposures
=================================

**Package: mscred**

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
  <dd>List of mosaic or multiple amplifier CCD data to process.  The data is
  typically in multiextension files though simple single images are allowed.  If
  the input includes processed data requiring no further processing it
  will be silently skipped.  Calibration data may be included in the input
  list and it will be selected and processed as needed provided the data has
  a keyword identifying the type of data.  However, more commonly the
  calibration data is specified separately with the calibration data
  parameters.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>List of output processed data.  If no list is given then the
  processing will replace the input images with the processed images,
  possibly after making a backup of the input if the package <span style="font-family: monospace;">"bkuproot"</span>
  parameter is defined.  If a list is given it must match the input
  list.  <i>Note that dependent calibration data requiring processing will
  be processed in-place (with optional backup).</i>
  </dd>
  </dl>
  <dl id="l_bpmasks">
  <dt><b>bpmasks = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bpmasks' Line='bpmasks = ""' -->
  <dd>List of output bad pixel files or directories to contain bad pixel masks
  created for each input.  If the input is a single image then the output
  is a bad pixel file while if the input is a multiextension file then
  the output is a directory to contain a bad pixel mask file for each
  extension.  If no list is specified then no output masks will be
  produced.  The output mask will be a combination of pixels specified
  in the <span style="font-family: monospace;">"<i>fixfile</i><span style="font-family: monospace;">" parameter and identified as saturated or bleed
  trail pixels.
  </dd>
  </dl>
  <dl id="l_ccdtype">
  <dt><b>ccdtype = "</span><span style="font-family: monospace;">"</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdtype' Line='ccdtype = ""' -->
  <dd>CCD type to select from the input list.  If no type is given
  then all input will be selected.  The recognized types are described
  in <b>ccdtypes</b>.
  </dd>
  </dl>
  <dl id="l_noproc">
  <dt><b>noproc = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='noproc' Line='noproc = no' -->
  <dd>Only list processing steps to be performed for each input file?
  </dd>
  </dl>
  <p style="text-align:center">PROCESSING SWITCHES
  
  </p>
  <dl id="l_xtalkcor">
  <dt><b>xtalkcor = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xtalkcor' Line='xtalkcor = no' -->
  <dd>Apply a crosstalk correction?  The crosstalk file is specified by
  the <span style="font-family: monospace;">"xtalkfile"</span> parameter.
  </dd>
  </dl>
  <dl id="l_fixpix">
  <dt><b>fixpix = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fixpix' Line='fixpix = yes' -->
  <dd>Fix bad CCD pixels by linear interpolation from neighboring
  lines and columns?  If a file is specified by the <span style="font-family: monospace;">"<i>fixfile</i><span style="font-family: monospace;">" parameter
  then the identified pixels will be interpolated upon input either along
  lines or columns depending on the mask value and dimensions of the regions.
  If saturated or bleed trail pixels are defined in this task, these will
  be interpolated on output (i.e. after all other processing) along
  lines.
  </dd>
  </dl>
  <dl id="l_overscan">
  <dt><b>overscan = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='overscan' Line='overscan = yes' -->
  <dd>Apply overscan or prescan bias correction?  If yes then the overscan
  section must be specified with the "</span>biassec<span style="font-family: monospace;">" parameter.
  </dd>
  </dl>
  <dl id="l_trim">
  <dt><b>trim = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trim' Line='trim = yes' -->
  <dd>Trim the image of the overscan region and bad edge lines and columns?
  If yes then the data section must be specified with the "</span>trimsec<span style="font-family: monospace;">" parameter.
  </dd>
  </dl>
  <dl id="l_zerocor">
  <dt><b>zerocor = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zerocor' Line='zerocor = yes' -->
  <dd>Apply zero level correction?  If yes a zero level image must be specified
  with the "</span>zero<span style="font-family: monospace;">" parameter.
  </dd>
  </dl>
  <dl id="l_darkcor">
  <dt><b>darkcor = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='darkcor' Line='darkcor = yes' -->
  <dd>Apply dark count correction?  If yes a dark count image must be specified
  with the "</span>dark<span style="font-family: monospace;">" parameter.
  </dd>
  </dl>
  <dl id="l_flatcor">
  <dt><b>flatcor = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flatcor' Line='flatcor = yes' -->
  <dd>Apply flat field correction?  If yes flat field images must be specified
  with the "</span>flat<span style="font-family: monospace;">" parameter.
  </dd>
  </dl>
  <dl id="l_sflatcor">
  <dt><b>sflatcor = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sflatcor' Line='sflatcor = no' -->
  <dd>Apply sky flat field correction?  If yes sky flat field images must be
  specified with the "</span>sflat<span style="font-family: monospace;">" parameter.
  </dd>
  </dl>
  <dl id="l_merge">
  <dt><b>merge = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='merge' Line='merge = yes' -->
  <dd>Merge amplifiers from the same CCD?  If yes then the amplifier extensions
  with the same CCD name will be merged into a single extension with the
  header and extension name of the first amplifier extension in the file.
  If only a single extension results from the merging then a simple image
  file is produced.  If the input has only one amplifier per CCD then
  nothing is done.  The merging also creates new bad pixel masks if
  an output bad pixel mask is specified and if the merged masks differ from
  the current bad pixel masks.
  </dd>
  </dl>
  <p style="text-align:center">PROCESSING PARAMETERS
  
  </p>
  <p>
  The parameters, "</span>xtalkfile<span style="font-family: monospace;">", "</span>fixfile<span style="font-family: monospace;">", "</span>saturation<span style="font-family: monospace;">", "</span>bleed<span style="font-family: monospace;">", "</span>biassec<span style="font-family: monospace;">",
  "</span>trimsec<span style="font-family: monospace;">", "</span>zero<span style="font-family: monospace;">", "</span>dark<span style="font-family: monospace;">", "</span>flat<span style="font-family: monospace;">", and "</span>sflat<span style="font-family: monospace;">" may reference keywords
  containing the desired value by preceding the keyword name with <span style="font-family: monospace;">'!'</span>.  This
  allows each image or image extension in each input to have different
  values.  Note that keyword name specified may be translated through the
  instrument file to another keyword or to a default value.
  </p>
  <dl id="l_xtalkfile">
  <dt><b>xtalkfile = "</span><span style="font-family: monospace;">"</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xtalkfile' Line='xtalkfile = ""' -->
  <dd>Crosstalk file for the crosstalk correction.  Only one crosstalk file may
  be specified and it applies to all the input data being processed.
  A keyword reference may be used to specify the file by preceding
  the keyword name with <span style="font-family: monospace;">'!'</span>.
  </dd>
  </dl>
  <dl id="l_fixfile">
  <dt><b>fixfile = "</span><span style="font-family: monospace;">"</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fixfile' Line='fixfile = ""' -->
  <dd>Bad pixel mask, image, or file.  specified in the image header or
  instrument translation file.  A bad pixel mask is a compact format ("</span>.pl<span style="font-family: monospace;">"
  extension) with zero values indicating good pixels and non-zero values
  indicating bad pixels.  A bad pixel image is a regular image in which zero
  values are good pixels and non-zero values are bad pixels.  A bad pixel
  file specifies bad pixels or rectangular bad pixel regions as described
  later.  The direction of interpolation is determined by the mask value with
  a value of two interpolating across columns, a value of three interpolating
  across lines, and any other non-zero value interpolating along the
  narrowest dimension.  A keyword reference may be used to specify the mask
  by preceding the keyword name with <span style="font-family: monospace;">'!'</span>.  The special value "</span>BPM<span style="font-family: monospace;">" may also
  be used reference the standard BPM keyword for a bad pixel mask.
  </dd>
  </dl>
  <dl id="l_saturation">
  <dt><b>saturation = "</span>INDEF<span style="font-family: monospace;">"</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='saturation' Line='saturation = "INDEF"' -->
  <dd>Pixels with values equal to or greater than this value in the input data
  are identified as saturated by the mask value 4.  The saturation value is
  specified by two words.  The first word is a number giving the saturation
  pixel value.  The value INDEF is equivalent to positive infinity and will
  identify no pixels as saturated.  The second word is the units which may be
  "</span>ADUs<span style="font-family: monospace;">" or "</span>electrons<span style="font-family: monospace;">".  If the units are "</span>electrons<span style="font-family: monospace;">" then the conversion
  from ADUs to electrons (in electrons per ADU) will be obtained from the
  "</span>gain<span style="font-family: monospace;">" keyword (which may be translated to some other keyword in the
  instrument file.  The units may abbreviated or be omitted, which then
  defaults to "</span>ADUs<span style="font-family: monospace;">".  If the first word is not a number (with or
  without a preceding <span style="font-family: monospace;">'!'</span>) then the word is considered to be a keyword
  reference.  The value of the keyword is interpreted in the same way as a
  number with optional units.  Note that numeric keywords cannot not have a
  units specification so they will always be understood as being in ADUs.
  Since there is only one parameter value a keyword is the way to provide
  different saturation values for the extensions and list of input data.
  </dd>
  </dl>
  <dl id="l_sgrow">
  <dt><b>sgrow = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sgrow' Line='sgrow = 0' -->
  <dd>Number of neighboring pixels along rows and columns from a saturated
  pixel which are also identified as saturated pixels.
  </dd>
  </dl>
  <dl id="l_bleed">
  <dt><b>bleed = "</span>INDEF<span style="font-family: monospace;">"</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bleed' Line='bleed = "INDEF"' -->
  <dd>Threshold for identifying bleed trail pixels.  This may be specified in
  the same way as the saturation value including use of "</span>ADUs<span style="font-family: monospace;">" and "</span>electrons<span style="font-family: monospace;">"
  and reference to a header keyword.  In addition the value may be set
  in relation to the saturation value or the mean of the data with one
  of the following specifications
  <div class="highlight-default-notranslate"><pre>
  saturation-X, saturation/X, mean+X, mean*X
  </pre></div>
  where X is a number and the values are in ADU.  For example the value
  "</span>mean+5000<span style="font-family: monospace;">" would define candidate bleed trail pixels as those which are
  5000 counts above the mean.  Note that for a pixel to actually be
  identified as a bleed pixel there must be a consecutive number of pixels
  (parameter <i>btrail</i>) along a column which are above this threshold.
  </dd>
  </dl>
  <dl id="l_btrail">
  <dt><b>btrail = 20</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='btrail' Line='btrail = 20' -->
  <dd>Number of consecutive pixels with values above the bleed pixel threshold
  along a column to qualify as a bleed trail.  The threshold is specified
  by the <i>bleed</i> parameter.
  </dd>
  </dl>
  <dl id="l_bgrow">
  <dt><b>bgrow = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bgrow' Line='bgrow = 0' -->
  <dd>Number of neighboring pixels along rows and columns from a bleed trail
  pixel which are also identified as bleed trail pixels.
  </dd>
  </dl>
  <p>
  Radius
  </p>
  <dl id="l_biassec">
  <dt><b>biassec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='biassec' Line='biassec = ""' -->
  <dd>Overscan bias image section.  Only the part of the bias section along the
  lines is used.  The column length of the bias region fit is defined by the
  trim section.  If one wants to limit the region of the overscan used in the
  fit to be less than that of the trim section then the sample region
  parameter, <i>sample</i>, should be used.  It is an error if no section or
  the whole image is specified.  A keyword reference may be used to specify
  the file by preceding the keyword name with <span style="font-family: monospace;">'!'</span>.  The older form of the
  special word <span style="font-family: monospace;">"image"</span> to reference the keyword BIASSEC is also allowed.
  </dd>
  </dl>
  <dl id="l_trimsec">
  <dt><b>trimsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trimsec' Line='trimsec = ""' -->
  <dd>Image section defining the trimmed output.  A keyword reference may be used
  to specify the file by preceding the keyword name with <span style="font-family: monospace;">'!'</span>.  The older form
  of the special word <span style="font-family: monospace;">"image"</span> to reference the keyword TRIMSEC is also
  allowed.
  </dd>
  </dl>
  <dl id="l_fixfile">
  <dt><b>fixfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fixfile' Line='fixfile = ""' -->
  <dd>Bad pixel mask, image, or file.  specified in the image header or
  instrument translation file.  A bad pixel mask is a compact format (<span style="font-family: monospace;">".pl"</span>
  extension) with zero values indicating good pixels and non-zero values
  indicating bad pixels.  A bad pixel image is a regular image in which zero
  values are good pixels and non-zero values are bad pixels.  A bad pixel
  file specifies bad pixels or rectangular bad pixel regions as described
  later.  The direction of interpolation is determined by the mask value with
  a value of two interpolating across columns, a value of three interpolating
  across lines, and any other non-zero value interpolating along the
  narrowest dimension.  A keyword reference may be used to specify the mask
  by preceding the keyword name with <span style="font-family: monospace;">'!'</span>.  The special value <span style="font-family: monospace;">"BPM"</span> may also
  be used reference the standard BPM keyword for a bad pixel mask.
  </dd>
  </dl>
  <dl id="l_zero">
  <dt><b>zero = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zero' Line='zero = ""' -->
  <dd>List of zero level calibration files.  The first image or image extension
  matching the amplifier of the input image to be calibrated is used.  The
  CCD type and subset are not checked for these images.  If no calibration
  image is found as specified by this parameter then the input list is
  checked for files of the appropriate CCD type.  The zero level calibration
  images may be one or two dimensional.  If the calibration file has not been
  processed it is processed as approprate for this type of calibration using
  the same parameters as for the input data being processed.  A keyword
  reference may be used to specify the file by preceding the keyword name
  with <span style="font-family: monospace;">'!'</span>.
  </dd>
  </dl>
  <dl id="l_dark">
  <dt><b>dark = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dark' Line='dark = ""' -->
  <dd>List of dark count calibration files.  The first image or image extension
  matching the amplifier of the input image to be calibrated is used.  The
  CCD type and subset are not checked for these images.  If no calibration
  image is found as specified by this parameter then the input list is
  checked for files of the appropriate CCD type.  If the calibration file has
  not been processed it is processed as approprate for this type of
  calibration using the same parameters as for the input data being
  processed.  A keyword reference may be used to specify the file by
  preceding the keyword name with <span style="font-family: monospace;">'!'</span>.
  </dd>
  </dl>
  <dl id="l_flat">
  <dt><b>flat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flat' Line='flat = ""' -->
  <dd>List of flat field calibration files.  The first image or image extension
  matching the amplifier and subset of the input image to be calibrated is
  used.  The CCD type and subset are not checked for these images.  If no
  calibration image is found as specified by this parameter then the input
  list is checked for files of the appropriate CCD type.  If the calibration
  file has not been processed it is processed as approprate for this type of
  calibration using the same parameters as for the input data being
  processed.  The flat field images may be one or two dimensional.  A keyword
  reference may be used to specify the file by preceding the keyword name
  with <span style="font-family: monospace;">'!'</span>.
  </dd>
  </dl>
  <dl id="l_sflat">
  <dt><b>sflat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sflat' Line='sflat = ""' -->
  <dd>List of sky flat field calibration files.  The first image or image
  extension matching the amplifier and subset of the input image to be
  calibrated is used.  The CCD type and subset are not checked for these
  images.  If no calibration image is found as specified by this parameter
  then the input list is checked for files of the appropriate CCD type.  If
  the calibration file has not been processed it is processed as approprate
  for this type of calibration using the same parameters as for the input
  data being processed.  The sky flat field images may be one or two
  dimensional.  A keyword reference may be used to specify the file by
  preceding the keyword name with <span style="font-family: monospace;">'!'</span>.
  </dd>
  </dl>
  <dl id="l_minreplace">
  <dt><b>minreplace = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minreplace' Line='minreplace = 1.' -->
  <dd>When processing flat fields, pixel values below this value (after all other
  processing such as overscan, zero, and dark corrections) are replaced by
  this value.  This allows flat fields processed by <b>ccdproc</b> to be
  certain to avoid divide by zero problems when applied to object images.
  </dd>
  </dl>
  <p style="text-align:center">OVERSCAN BIAS FITTING PARAMETERS
  
  </p>
  <p>
  There are two types of overscan (or prescan) bias determinations.  One
  determines a independent bias value for each line.  The other averages the
  overscan columns to make an overscan vector, fits a smooth bias function to
  the vector, and then evaluates the bias function to get the bias at each
  line.  The line-by-line bias determination only uses the <i>function</i>
  parameter.  The bias function determination uses the <b>icfit</b>
  procedure with the following parameters.
  </p>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Fit the overscan bias vector interactively?  If yes and the bias function
  type is one of the <b>icfit</b> types then the average overscan bias vector
  is fit interactively using the <b>icfit</b> package.  If no then the fitting
  parameters are used in a non-interactive fit.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"legendre"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "legendre"' -->
  <dd>Line-by-line determination of the bias is specified by:
  <div class="highlight-default-notranslate"><pre>
    mean - the mean of the biassec columns at each line
  median - the median of the biassec columns at each line
  minmax - the mean at each line with the min and max excluded
  </pre></div>
  The bias vector may be fit by one of the functions:
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
  <dd>Number of polynomial terms or spline pieces in the overscan fit.  To simply
  use the average bias use a polynomial function of order 1.
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample' Line='sample = "*"' -->
  <dd>Sample points to use in the overscan bias fit.  The string <span style="font-family: monospace;">"*"</span> specifies all
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
  <dd>Number of rejection interations to remove deviant points from the overscan fit.
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
  <p style="text-align:center">PACKAGE PARAMETERS
  
  </p>
  <dl id="l_pixeltype">
  <dt><b>pixeltype = <span style="font-family: monospace;">"real real"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixeltype' Line='pixeltype = "real real"' -->
  <dd>Output pixel datatype and calculation datatype.  When images are processed
  or created, the output pixel datatype is the highest precision of the input
  pixel datatype and the specified output datatype.  The allowed datatypes
  and order of precision are <span style="font-family: monospace;">"short"</span>, <span style="font-family: monospace;">"ushort"</span>, <span style="font-family: monospace;">"int"</span>, <span style="font-family: monospace;">"long"</span>, <span style="font-family: monospace;">"real"</span>, or
  <span style="font-family: monospace;">"double"</span>.  The calculation datatype may either be short or real.
  Real is the default if no calculation type is specified.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print log information to the standard output?
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "logfile"' -->
  <dd>Logfile to append log information.  If no filename is specified then no
  logfile is kept.
  </dd>
  </dl>
  <dl id="l_plotfile">
  <dt><b>plotfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotfile' Line='plotfile = ""' -->
  <dd>Metacode plotfile for appending plots of the overscan bias fits.  If
  no filename is specified then no metacode plotfile is kept.
  </dd>
  </dl>
  <dl id="l_backup">
  <dt><b>backup = <span style="font-family: monospace;">"once"</span> (none|once|all)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='backup' Line='backup = "once" (none|once|all)' -->
  <dd>Backup the input data when the input file is replaced by the processed data?
  If the value is <span style="font-family: monospace;">"none"</span> then no backup of the input data is made.  If the
  value is <span style="font-family: monospace;">"once"</span> then only the first backup of the input is made.  If
  the value is <span style="font-family: monospace;">"all"</span> than if the input is repeatedly replaced by additional
  processing then additional backups will be made.
  </dd>
  </dl>
  <dl id="l_bkuproot">
  <dt><b>bkuproot = <span style="font-family: monospace;">"Raw/"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bkuproot' Line='bkuproot = "Raw/"' -->
  <dd>When a backup of the input data is made the string given by this parameter
  is used as a prefix to the original input data filename.  If the root
  is a directory name (ends with <span style="font-family: monospace;">'$'</span> or <span style="font-family: monospace;">'/'</span>) the directory will be
  created if needed and the input data moved to the directory.  When
  the backup type is <span style="font-family: monospace;">"all"</span> and a second version of the input is backed up
  a digit is prepended to the input filename.
  </dd>
  </dl>
  <dl id="l_instrument">
  <dt><b>instrument = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='instrument' Line='instrument = ""' -->
  <dd>CCD instrument file.  See help for <b>instrument</b>.
  </dd>
  </dl>
  <dl id="l_ampfile">
  <dt><b>ampfile = <span style="font-family: monospace;">"amps"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ampfile' Line='ampfile = "amps"' -->
  <dd>The <span style="font-family: monospace;">"amp"</span> keyword (which may be translated in the instrument file) produces
  a string identifying the amplifier for each image.  A mapping between the
  full string and a short version (based on the first word) is stored in
  this file.
  </dd>
  </dl>
  <dl id="l_ssfile">
  <dt><b>ssfile = <span style="font-family: monospace;">"subsets"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ssfile' Line='ssfile = "subsets"' -->
  <dd>The <span style="font-family: monospace;">"subset"</span> keyword (which may be translated in the instrument file)
  produces a string identifying a subset for each image. A mapping between
  the full string and a short version (based on the first word) is stored
  in this file.
  </dd>
  </dl>
  <dl id="l_im_bufsize">
  <dt><b>im_bufsize = 0.065536</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='im_bufsize' Line='im_bufsize = 0.065536' -->
  <dd>When a line of an image is read a larger block of data is actually read.
  This parameter defines the block size in megabytes.  For large images
  this I/O buffering often makes the processing more efficient.  Note
  however that setting this to the size of the image does not necessarily
  make the processing faster.  Once the block size reaches an optimal size
  for the disk I/O system it does not improve performance further and might
  actually degrade performance if too much memory is tied up.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Graphics output device for interactive graphics.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input.  If null the standard terminal graphics cursor
  is used.
  </dd>
  </dl>
  <dl id="l_version">
  <dt><b>version</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='version' Line='version' -->
  <dd>Package version string.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Ccdproc</b> applies various calibrations and corrections to CCD data in
  multiextension (mosaic or multiamplifier) or single image formats.  The
  calibrations and corrections are for amplifier crosstalk, detector defects,
  electronic bias, zero level bias, dark counts, and pixel responses.  The
  task also identifies saturated pixels and bleed trails, trims unwanted edge
  lines and columns, merges multiple amplfiers from the same CCD into single
  images, and changes the pixel datatype.
  </p>
  <p>
  The task is designed to be efficient and easy to use.  All one has to do is
  set the parameters and begin processing the data.  The task takes care of
  most of the record keeping and automatically does the prerequisite
  processing of calibration images.  Beneath this simplicity there is much
  going on.  In this section a brief description of the usage is given.  The
  following sections present detailed discussions on the different operations
  performed and the order and logic of the processing steps.
  </p>
  <p>
  One begins by setting the task parameters.  There are many parameters but
  they may be easily reviewed and modified using <span style="font-family: monospace;">"<b>eparam</b><span style="font-family: monospace;">".  The CCD
  data to be processed is specified with the "</span>input<span style="font-family: monospace;">" parameter list as a
  combination of filenames, filename templates, and @files.  Previously
  processed data are silently ignored and calibration files are recognized
  provided the CCD image types are identified in the image headers (see
  <b>instruments</b> and <b>ccdtypes</b>).  Therefore it is permissible to use
  simple image templates such as <span style="font-family: monospace;">"*.fits"</span>.   However, it is recommended that
  calibration data by specified explicitly with the appropriated parameters.
  </p>
  <p>
  The <span style="font-family: monospace;">"<i>ccdtype</i><span style="font-family: monospace;">" parameter may be used to select only certain types of
  CCD data to process.  If the data does not contain a CCD type
  identification keyword then the parameter can be set to the null string
  "</span><span style="font-family: monospace;">".  In this case it is the user's responsibility to select the correct
  processing steps for the type of data, and the calibration data cannot be
  determined automatically from the input list.
  </p>
  <p>
  The names for processed data are specified by the "</span><i>output</i><span style="font-family: monospace;">" parameter
  list of names which are matched in order against the input list.  However,
  if no output list is given the processed data replaces the input data with
  an option to make a backup of the original input file (see the package
  "</span><i>bkuproot</i><span style="font-family: monospace;">" parameter).  The output file will be in the same format as
  the input file except that if a multiextension input consists of multiple
  amplifiers from a single CCD and the amplifiers are merged, a single simple
  image will be produced.
  </p>
  <p>
  Other (optional) output includes pixel masks and processing log information.
  Output pixel masks are specified by the "</span><i>bpmasks</i><span style="font-family: monospace;">" parameter.  The
  masks merge any input pixel mask data with identification of saturated or
  non-linear pixels and bleed trails.  The processing information consists of
  a logfile and/or terminal output for text and a plotfile for plots of the
  overscan bias fitting.  These are select with the package "</span><i>logfile</i><span style="font-family: monospace;">",
  "</span><i>verbose</i><span style="font-family: monospace;">", and "</span><i>plotfile</i><span style="font-family: monospace;">" parameters.
  </p>
  <p>
  The processing operations are selected by boolean (yes/no) parameters.
  When the input data includes CCD type identifications the processing
  options may be set for object data and only the appropriate subset of
  operations will be performed on the calibration data.  Any combination of
  operations may be specified.  While it is possible to do operations in
  separate steps some sets of operations are done in a single pass through
  the data and will be more efficiently performed if done at the same time.
  </p>
  <p>
  The processing steps selected have related parameters which must be
  specified.  These are things like image sections defining the electronic
  bias overscan and trim regions, parameters for identifying saturated pixels
  and bleed trails, and calibration files.  There are a number of parameters
  used for fitting the overscan or prescan electronic bias data.  These are
  parameters used by the standard IRAF curve fitting package <b>icfit</b>.
  </p>
  <p>
  Calibration data are specified by task parameters and/or in the input
  list.  The task paramters are lists so more than one calibration file may
  be specified.  Zero and dark count calibrations generally only need one
  file but flat field calibrations need one for each subset which is
  typically the filter.  When more than one calibration file is specified
  then the first one encountered that matches the input is used and a warning
  is issued for the extra files.  Calibration files specified by task
  parameters take precedence over calibration files in the input list.
  </p>
  <p>
  In addition to the task parameters there are package parameters which
  affect <b>ccdproc</b>.  These include the instrument, amplifier, and subset
  files, the verbose, text and plot output log settings, the output and
  calculation pixel datatype, the amount of memory to use for image I/O
  buffering, and the backup option.  The instrument file is used to define
  the keywords to be used, translations of CCD type strings to a standard
  set, and defaults for missing keywords.  The amplifier and subset files
  translate arbitrary keyword values for the amplifier and subset to short
  one word identifiers.  Users may edit these files to change the mapping.
  The image I/O buffering may be increased to improve I/O efficiency.  Note
  that this is just how much is read in one I/O request and is not a means to
  cache an image in memory.  The backup option allows input files to be saved
  with a new name or in a directory when the processed data replaces the
  input.  One may backup once, every time, or not at all.  When a backup is
  requested the prefix string is added to the input name or the input is
  moved to the backup directory.  The datatype parameter determines the type
  of the output pixel and the calculation mode.  Typically raw CCD data is in
  short integers and processed data is saved as real (32-bit floating point)
  values.
  </p>
  <p>
  When an input file is processed the task first determines the processing
  parameters and calibration files.  If a requested operation has been done
  it is skipped and if all requested operations have been completed then no
  processing takes place.  When it determines that a calibration file is
  required it checks for the file from the task parameter and then for a
  calibration file of the proper type in the input list.  Having selected a
  calibration file it checks if it has been processed.  If it has not been
  processed, based on the current settings of the processing options
  appropriate for that type of calibration, it is processed automatically.
  Once the processing parameters and calibration files have been determined
  the input file is processed.  The output processed data will include
  keywords identifying the processing steps and calibration files used.
  </p>
  </section>
  <section id="s_xtalkcor__amplifier_crosstalk_correction">
  <h3>Xtalkcor: amplifier crosstalk correction</h3>
  <p>
  When multiple amplifiers are readout, such as occurs when using multiple
  amplifiers in a single CCD or multiple CCDs in a mosaic, there is the
  possibilty of crosstalk in the controller electronics.  The crosstalk
  causes pixel values produced by one amplifier to be affected by the signal
  in another amplifier.  There are many ways this crosstalk may affect the
  data.  <b>Ccdproc</b> includes a way to correct pixels based on a
  simple crosstalk model.
  </p>
  <p>
  In this model the signal for a pixel in one amplifier, which we call the
  <span style="font-family: monospace;">"source"</span>, adds or subtracts a small amount to the pixel value read at the
  same time in another amplifier, called the <span style="font-family: monospace;">"victim"</span>.  A correction is
  obtained by multiplying the pixel value of the source image by a crosstalk
  coefficient and adding or subtracting it from the matching pixel in the
  victim image.
  </p>
  <p>
  Note that it is possible that a source may also be a victim and that a
  victim may be affected by multiple sources.  In our simple model each pair
  of source and victim are treated independently and the source pixel values
  used to correct a victim are treated as unaffected by other amplifiers.
  </p>
  <p>
  The crosstalk coefficients are given by a crosstalk calibration file.  This
  may be specified explicitly through reference to a keyword.  The correction
  is performed by the task <b>xtalkcor</b> which is called from
  <b>ccdproc</b>.  Information about the format of the crosstalk calibration
  file and details of the algorithm are found in the description for that
  task.  The crosstalk coefficients may provided by the observatory as a
  standard calibration file or they may be estimated from the data using the
  task <b>xtcoeff</b>.
  </p>
  <p>
  The crosstalk correction is performed before any other operation.  The
  simple model of the crosstalk is that the raw data from the amplifier
  readout is used.  Therefore the correction should generally be applied
  only to the raw data.
  </p>
  </section>
  <section id="s_saturated_pixels">
  <h3>Saturated pixels</h3>
  <p>
  Saturated pixels are identified as those pixels with values above a fixed
  threshold in the input image before they are modified by any other
  calibration.  Any pixels identified as bad in a pixel file given by the
  <span style="font-family: monospace;">"\Ifixfile<span style="font-family: monospace;">" parameter are excluded.  Neighboring pixels, those within a
  distance of "</span><i>sgrow</i><span style="font-family: monospace;">" pixels along lines or columns, of the threshold
  selected saturation pixels are also identified as saturated.
  </p>
  <p>
  To identify saturated pixels a saturation threshold is specified by the
  "</span><i>saturation</i><span style="font-family: monospace;">" parameter.  The saturation value may be given in units
  of digital counts as recorded in the image data or as electrons related to
  the digital counts through a gain keyword in the header.  The parameter
  description explains how to specify the saturation threshold.  The term
  "</span>saturated<span style="font-family: monospace;">" can really be used to apply to any pixels which are non-linear
  and not correctable.  Thus the saturation threshold need not be the actual
  saturation of the CCD but some lower value where the pixels become
  uncorrectably non-linear.
  </p>
  <p>
  The identified pixels are recorded in the output bad pixel mask specified
  by the "</span><i>bpmasks</i><span style="font-family: monospace;">" parameter with a mask value of 4.  If the
  "</span><i>fixpix</i><span style="font-family: monospace;">" processing option is selected the saturated pixels are
  replaced by linear interpolation along lines.  If a pixel identified as bad
  in an input mask or file touches a saturated pixel it is also
  interpolated.  This is done to avoid funny effects where the bad pixel is
  first interpolated using data which has not yet been identified as a bleed
  trail or saturated pixel and which is not subsequently replaced by more
  reasonable data values.
  </p>
  <p>
  Note that if no output pixel mask or pixel replacement are specified then
  the saturated pixels will have no effect.  Therefore, the identification of
  such pixels is not done by the task even if the other parameters are set to
  identify saturated pixels.  This operation does not apply to data
  identified as zero, dark, or flat.
  </p>
  </section>
  <section id="s_bleed_trails">
  <h3>Bleed trails</h3>
  <p>
  Bleed trails are identifed as regions with some minimum number of
  consecutive pixels along a columns having values above a fixed threshold.
  The pixel values are before they are modified by any other calibration.
  Neighboring pixels, those within a distance of "</span><i>bgrow</i><span style="font-family: monospace;">" pixels along
  lines or columns, of the threshold selected bleed trail pixels are also
  identified as part of the bleed trail.  Any pixels identified as bad in a
  pixel file given by the "</span>\Ifixfile<span style="font-family: monospace;">" parameter are excluded.
  </p>
  <p>
  To identify bleed trails a threshold is specified by the "</span><i>bleed</i><span style="font-family: monospace;">"
  parameter.  The value may be given in units of digital counts as recorded
  in the image data or as electrons related to the digital counts through a
  gain keyword in the header.  The parameter description explains how to
  specify the bleed threshold.  In addition to an explicit value specified by
  the parameter or in the header the threshold may be specified in relation
  to the saturation threshold or to the mean value in the data.
  </p>
  <p>
  Note that it is not individual pixels above a threshold but a consecutive
  number of pixels.  This means the threshold can be fairly low provided the
  minimum bleed trail length, specified by the "</span><i>btrail</i><span style="font-family: monospace;">" parameter, is
  greater than would occur in objects.  For this reason specifying the
  threshold as some number times the mean or above the mean is very useful.
  A recommendation is to use "</span>mean+5000<span style="font-family: monospace;">" when the data in counts are from 15
  or 16 bit A/D converters.
  </p>
  <p>
  The identified pixels are recorded in the output bad pixel mask specified
  by the "</span><i>bpmasks</i><span style="font-family: monospace;">" parameter with a mask value of 5.  If the
  "</span><i>fixpix</i><span style="font-family: monospace;">" processing option is selected the bleed trails are replaced
  by linear interpolation along lines.  If pixel identified as bad in an
  input mask or file touches the bleed trail it is also interpolated.
  This is done to avoid funny effects where the bad pixel is first interpolated
  using data which has not yet been identified as a bleed trail or saturated
  pixel and which is not subsequently replaced by more reasonable data values.
  </p>
  <p>
  Note that if no output pixel mask or
  pixel replacement are specified then the bleed trails will have no effect.
  Therefore, the identification of such pixels is not done by the task even
  if the other parameters are set to identify saturated pixels.
  This operation does not apply to data identified as zero, dark, or flat.
  </p>
  </section>
  <section id="s_output_pixel_masks">
  <h3>Output pixel masks</h3>
  <p>
  An output pixel mask is created when a name is specified with the
  "</span><i>bpmasks</i><span style="font-family: monospace;">" parameter and the mask does not exist.  If the processing
  does not involved any modification to the input data then only the mask
  will be produced.  The mask is a combination of the input mask specified
  by the "</span><i>fixfile</i><span style="font-family: monospace;">" parameter and pixels identified as saturated and
  bleed trails.  Note that the "</span><i>fixfile</i><span style="font-family: monospace;">" parameter is used even if
  "</span><i>fixpix</i><span style="font-family: monospace;">" is not set.
  </p>
  <p>
  An input bad pixel mask is not required and if none is specified then
  the output will be just the pixels identified as bleed trails or
  saturated.  If the saturated pixels and bleed trails are not identified
  and no input mask is specified then the output will simply be an
  empty mask.
  </p>
  <p>
  The specified output mask is currently used as a directory name.
  It is created if it is not found.  The individual bad pixel masks,
  in pixel list format, are created in this directory.  In a future
  version the multiple pixel masks will be stored as extensions in
  the multiextension file specified by the output mask name.
  </p>
  </section>
  <section id="s_fixpix__replacing_bad_pixels_by_interpolation">
  <h3>Fixpix: replacing bad pixels by interpolation</h3>
  <p>
  Regions of bad lines and columns may be replaced by linear
  interpolation from neighboring lines and columns when the parameter
  <i>fixpix</i> is set.  This algorithm is the same as used in the
  task <b>fixpix</b>.  The bad pixels may be specified by a pixel mask,
  an image, or a text file.  For a mask or image, values of zero indicate
  good pixels and other values indicate bad pixels to be replaced.
  </p>
  <p>
  A text file consists of lines with four fields, the starting and
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
  The bad pixel description may be specified explicitly or by
  reference to a keyword with the name.  The special value <span style="font-family: monospace;">"BPM"</span> or <span style="font-family: monospace;">"image"</span>
  references the keyword BPM.
  </p>
  </section>
  <section id="s_overscan__removing_electronic_bias_using_overscan_prescan_data">
  <h3>Overscan: removing electronic bias using overscan/prescan data</h3>
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
  <section id="s_trim__trimming_unwanted_data">
  <h3>Trim: trimming unwanted data</h3>
  <p>
  When the parameter <i>trim</i> is set the input image will be trimmed to
  the image section given by the parameter <i>trimsec</i>.  This trim
  should, of course, be the same as that used for the calibration images.
  </p>
  </section>
  <section id="s_zerocor__applying_a_zero_bias_calibration">
  <h3>Zerocor: applying a zero bias calibration</h3>
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
  <section id="s_darkcor__applying_a_dark_count_calibration">
  <h3>Darkcor: applying a dark count calibration</h3>
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
  <section id="s_flatcor__applying_a_flat_field_calibration">
  <h3>Flatcor: applying a flat field calibration</h3>
  <p>
  The relative detector pixel response is calibrated by dividing by a
  scaled flat field calibration image.  A flat field image is obtained by
  exposure to a spatially uniform source of light such as an lamp or
  twilight sky.  Flat field images may be corrected for the spectral
  signature in spectroscopic images (see <b>response</b> and
  <b>apnormalize</b>), or for illumination effects (see <b>mkillumflat</b>
  or <b>mkskyflat</b>).  For more on flat fields and illumination corrections
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
  <section id="s_sflatcor__applying_a_sky_flat_field_calibration">
  <h3>Sflatcor: applying a sky flat field calibration</h3>
  <p>
  A sky flat field calibration is just a second flat field derived from
  data which has been flat fielded by the first flat field.  Typically
  a sky flat field is created from sky data.  This is either exposures
  of the twilight sky or combinations of dark sky observations where
  objects are eliminated by stacking disregistered exposures.  The
  operation is similar to the primary flat field in that a scaling
  is determined from the CCDMEAN information in the image or by computing
  a mean value.  The calibration data is scaled and divided into the
  input data.
  </p>
  </section>
  <section id="s_merge__merging_amplifiers_from_the_same_ccd">
  <h3>Merge: merging amplifiers from the same ccd</h3>
  <p>
  When an input file consists of multiple amplifiers from the same
  CCD they may be merged together into a single image or extension.
  If the input file has only one CCD then the output is a simple
  single image otherwise it is a multiextension file with fewer
  extensions.  The image header of the merged output is from the
  first amplifier encountered for each CCD.  For multiextension
  output the merged extension name will be the extension name
  of the first amplifier.
  </p>
  <p>
  If an output mask is specified then the input masks will also be
  merged.  In cases where the masks for the input data are already
  in merged form, where the masks for all the extensions to be merged
  are the same mask, the task will not create a new mask.  
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
  <p>
  	cl&gt; ccdproc *.imh &amp;
  </p>
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
  <dt><b>CCDPROC: MSCRED - V4.5: March 19, 2001</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='CCDPROC' Line='CCDPROC: MSCRED - V4.5: March 19, 2001' -->
  <dd>This help page describes the options for the above version of MSCRED.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <div class="highlight-default-notranslate"><pre>
  mscguide, xtalkcor
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'xtalkcor: Amplifier Crosstalk Correction' 'Saturated Pixels' 'Bleed Trails' 'Output Pixel Masks' 'fixpix: Replacing Bad Pixels by Interpolation' 'overscan: Removing Electronic Bias Using Overscan/Prescan Data' 'trim: Trimming Unwanted Data' 'zerocor: Applying a Zero Bias Calibration' 'darkcor: Applying a Dark Count Calibration' 'flatcor: Applying a Flat Field Calibration' 'sflatcor: Applying a Sky Flat Field Calibration' 'merge: Merging Amplifiers from the Same CCD' 'EXAMPLES' 'TIME REQUIREMENTS' 'REVISIONS' 'SEE ALSO'  -->
  

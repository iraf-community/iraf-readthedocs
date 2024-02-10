.. _nfproc:

nfproc: Apply instrumental calibrations
=======================================

**Package: newfirm**

.. raw:: html

  <section id="s_usage___">
  <h3>Usage   </h3>
  <p>
  nfproc input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images to process.  The files may be multi-extension
  FITS files (MEF) or single images.  The order in which the input images
  and MEF extensions are processed is controlled by the program.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output images, a pattern based on the input filenames, or an
  expression.  An expression begins with <span style="font-family: monospace;">'('</span> and evaluates to a filename.
  If it is not an expression then <span style="font-family: monospace;">'+'</span> characters in the string identify a
  pattern where those characters are substituted with the input filename
  excluding any path and extension.  If the value is neither an expression
  or pattern then it is a list which must match the input list.
  Note that a list can be an image template which also includes a replacement
  syntax (see example 2 of
  <a href="imrename"><b>imrename</b></A>
  ).  The output format will be the
  same as the input format such that input MEF files will produce output
  MEF files.  If the input has non-image extensions they will be ignored
  and excluded from the output.  The special value <span style="font-family: monospace;">"+LIST+"</span> will produce
  log output without processing the input.
  </dd>
  </dl>
  <dl id="l_logfiles">
  <dt><b>logfiles = <span style="font-family: monospace;">"STDOUT"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfiles' Line='logfiles = "STDOUT"' -->
  <dd>List of logfiles for recording processing information.  The special value
  <span style="font-family: monospace;">"STDOUT"</span> may be used to write to the terminal and multiple files may be
  specified to tee the output to more than one file.  The output is appended
  to any existing output.
  </dd>
  </dl>
  <p style="text-align:center">PROCESSING SWITCHES
  
  </p>
  <p>
  The following parameters select the correction and calibration operations
  to be performed.  The allowed operations and the order in which they are
  performed is controlled by the
  <a href="#l_dorder"><i>order</i>,</A>
  <a href="#l_dorder"><i>dorder</i>,</A>
  and
  <a href="#l_dorder"><i>forder</i></A>
  parameters.  A single letter processing code is used to identify an
  operation in the order parameters.  For an operation to be performed the
  processing switch must be enabled AND the operation must be listed in
  the order of operations.  Unless the
  <a href="#l_override"><i>override</i></A>
  parameter is <span style="font-family: monospace;">"yes"</span>,
  steps are skipped that have already been performed as identified in the
  image header keyword PROCDONE.
  </p>
  <dl id="l_trim">
  <dt><b>trim = yes [processing code: T]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trim' Line='trim = yes [processing code: T]' -->
  <dd>Trim the image by removing edge lines and columns?  This requires
  specification of the region to be retained with the
  <a href="#l_trimsec"><i>trimsec</i></A>
  parameter.  The trimming is done on input and so it doesn't matter
  where the code appears in the processing order parameters.  Trimming
  may only be done in the first group of operations.
  </dd>
  </dl>
  <dl id="l_fixpix">
  <dt><b>fixpix = no [processing code: P]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fixpix' Line='fixpix = no [processing code: P]' -->
  <dd>Fix bad pixels using linear interpolation from neighboring pixels?
  Bad pixels are those identified by the input image mask (see
  <a href="#l_bpm"><i>bpm</i></A>
  ).  The interpolation is done on input and so it doesn't matter where the
  code appears in the processing order.  To apply the interpolation after
  other operations the operation may be specified in later order groups or
  with a second invocation of the task.
  </dd>
  </dl>
  <dl id="l_biascor">
  <dt><b>biascor = no [processing code: B]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='biascor' Line='biascor = no [processing code: B]' -->
  <dd>Subtract bias using bias or reference pixels?  This uses the
  the
  <a href="#l_biassec"><i>biassec</i></A>
  and the bias processing parameters.
  </dd>
  </dl>
  <dl id="l_darkcor">
  <dt><b>darkcor = yes [processing code: D]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='darkcor' Line='darkcor = yes [processing code: D]' -->
  <dd>Apply dark exposure correction?  This uses the
  <a href="#l_darks"><i>darks</i></A>
  parameter.
  </dd>
  </dl>
  <dl id="l_lincor">
  <dt><b>lincor = yes [processing code: L]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lincor' Line='lincor = yes [processing code: L]' -->
  <dd>Apply a linearity correction?  This uses the the
  <a href="#l_linexpr"><i>linexpr</i></A>
  and
  <a href="#l_linexpr"><i>linimage</i></A>
  parameters.
  </dd>
  </dl>
  <dl id="l_flatcor">
  <dt><b>flatcor = yes [processing code: F and/or G]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flatcor' Line='flatcor = yes [processing code: F and/or G]' -->
  <dd>Apply flat field correction?  This uses the
  <a href="#l_flats"><i>flats</i>,</A>
  <a href="#l_ftype"><i>ftype</i>,</A>
  <a href="#l_gtype"><i>gtype</i>,</A>
  and
  <a href="#l_flatexpr"><i>flatexpr</i></A>
  parameters.
  </dd>
  </dl>
  <dl id="l_skysub">
  <dt><b>skysub = yes [processing code: S]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skysub' Line='skysub = yes [processing code: S]' -->
  <dd>Subtract a sky image?  This uses the
  <a href="#l_skies"><i>skies</i>,</A>
  <a href="#l_skymatch"><i>skymatch</i>,</A>
  and
  <a href="#l_skymode"><i>skymode</i></A>
  parameters.
  </dd>
  </dl>
  <dl id="l_replace">
  <dt><b>replace = yes [processing code: R]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='replace' Line='replace = yes [processing code: R]' -->
  <dd>Replace pixels.  This uses the
  <a href="#l_repexpr"><i>repexpr</i></A>
  and
  <a href="#l_repimage"><i>repimage</i></A>
  parameters.
  Typically the replacement expression would affect only a subset of the
  pixels using thresholds or masks and the <span style="font-family: monospace;">'?'</span> conditional expression
  operator.
  </dd>
  </dl>
  <dl id="l_normalize">
  <dt><b>normalize = yes [processing code: N]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='normalize' Line='normalize = yes [processing code: N]' -->
  <dd>Normalize the data.  The default expression is <span style="font-family: monospace;">"max(0.1,$I/PROCMEAN)"</span>.
  Since the keyword PROCMEAN is computed by this task (but only for
  flat fields), the normalize
  operation is normally done after the first group of operations.
  </dd>
  </dl>
  <p style="text-align:center">PROCESSING ORDER
  
  </p>
  <dl id="l_dorder">
  <dt><b>dorder = <span style="font-family: monospace;">"PTB"</span>, forder = <span style="font-family: monospace;">"TPBDL,N"</span>, order = <span style="font-family: monospace;">"TPBDLF,S"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dorder' Line='dorder = "PTB", forder = "TPBDL,N", order = "TPBDLF,S"' -->
  <dd>Allowed operations and the order, specified from left to right, in
  which the selected processing steps are to be performed for dark images
  (<i>dorder</i>), flat images (<i>forder</i>), and all other images
  (<i>order</i>).  The image types are identified by the expressions
  specified in the parameters
  <a href="#l_dtype"><i>dtype</i></A>
  and
  <a href="#l_ftype"><i>ftype</i></A>
  for data in the
  input list.  Each processing step has a processing code letter as shown
  in the processing switch section.  For a step to be performed it must
  both be present in the order specification and the processing switch
  must be enabled.  Note that the position of the trim and fixpix codes
  are irrelevant since these operations are applied upon input.
  Groups of operations may be separated by a comma.  The operations in each
  group are performed in the indicated order on each line as a single pass
  through the data for all input images of a particular type.  So by using
  commas and the input ordering feature it is possible to apply operations
  in multiple passes through the data and have dependent images be processed
  in the order darks, flats, and skies.  For example <span style="font-family: monospace;">"DF,S"</span> means do dark
  and flat processing on each line in the input image and then do
  sky subtraction.
  These parameters may be specified by expressions (see help topic
  <a href="procexpr"><b>procexpr</b></A>
  ) to allow header driven application.
  </dd>
  </dl>
  <p style="text-align:center">PROCESSING PARAMETERS
  
  </p>
  <p>
  The processing parameters provide data for the various operations selected
  by the processing switches.  All parameters may be expressions
  (see help topic
  <a href="procexpr"><b>procexpr</b></A>
  ).
  </p>
  <dl id="l_bpm">
  <dt><b>bpm = <span style="font-family: monospace;">"(bpm)"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bpm' Line='bpm = "(bpm)"' -->
  <dd>List of bad pixel masks or an expression evaluating to a bad pixel mask.
  If a list is specified it must either be empty to not use a mask,
  be a single mask to be applied to all input, or a list which matches
  the input list.  If no mask is specified all pixels are assumed to
  be good.  The masks are used for the
  <a href="#l_fixpix"><i>fixpix</i></A>
  operation and/or in
  expressions with the operand $M.  For <i>fixpix</i> only mask values of
  1 are interpolated.  The mask is matched to the input image using
  physical coordinates (those defined by the LTV/LTM keywords) and so
  the mask need not be the same size.  Pixels which do not overlap the
  mask are treated as good having pixel values of 0.
  </dd>
  </dl>
  <dl id="l_obm">
  <dt><b>obm = <span style="font-family: monospace;">"(objmask)"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obm' Line='obm = "(objmask)"' -->
  <dd>List of object masks or an expression evaluating to an object mask.  If a
  list is specified it must either be empty to not use a mask, be a single
  mask to be applied to all input, or a list which matches the input list.
  If no mask is specified all pixels are assumed to be good.  The masks
  are used for the
  <a href="l_skysub"><i>skysub</i></A>
  median option and/or in expressions with
  the operand $O.  For <i>skysub</i> this parameter must be an expression and
  not a list.  The mask could really be any type of mask but it is intended
  to be used for object masking in sky subtraction.  See
  <a href="acesegment"><b>acesegment</b></A>
  for creating object masks.  The mask is matched to the input image using
  physical coordinates (those defined by the LTV/LTM keywords) and so the
  mask need not be the same size.  Pixels which do not overlap the mask
  are treated as good having pixel values of 0.
  </dd>
  </dl>
  <dl id="l_trimsec">
  <dt><b>trimsec = <span style="font-family: monospace;">"(trimsec)"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trimsec' Line='trimsec = "(trimsec)"' -->
  <dd>Image section to apply when the trimming operation is selected.
  This may be specified as an explicit image section or by an expression
  that evaluates to an image section.
  </dd>
  </dl>
  <dl id="l_biassec">
  <dt><b>biassec = <span style="font-family: monospace;">"(biassec)"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='biassec' Line='biassec = "(biassec)"' -->
  <dd>Image section defining the bias reference pixels to apply when the
  bias correction operation is selected.  This may be specified as an
  explicit image section or by an expression that evaluates to an image
  section.  The section must span the input image along one and only one
  dimension.  If it spans all rows in the image a row-wise
  bias correction will be applied and if it spans all columns in the image 
  a column-wise correction will be made.
  </dd>
  </dl>
  <dl id="l_linexpr">
  <dt><b>linexpr = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linexpr' Line='linexpr = ""' -->
  <dd>Linearity expression computing the corrected pixel value given the
  uncorrected pixel value represented by the operand <span style="font-family: monospace;">"$I"</span>.  The expression
  may use any of the standard mathematical operators and functions described
  in
  <a href="procexpr"><b>procexpr</b>.</A>
  If no expression is specified but a linearity correction
  is requested the task will skip the linearity correction.  Linearity
  expressions generally apply coefficients which may constants, defined
  by keywords, or taken from the linearity image.
  </dd>
  </dl>
  <dl id="l_linimage">
  <dt><b>linimage = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linimage' Line='linimage = ""' -->
  <dd>Optional image list or an expression evaluating to an image providing
  per pixel coefficients for the linearity expression.  An image list may
  include MEF files which expand to all image extensions.  When selecting
  a linearity image from a list to apply to a particular input image the
  nearest, based on the
  <a href="#l_sortval"><i>sortval</i></A>
  parameter, which has the same value
  for the
  <a href="#l_imageid"><i>imageid</i></A>
  parameter (e.g. extension in an MEF) is selected.
  Note that typically there is only one linearity file though it must
  be an MEF if the input data is MEF.  When an image is selected by an
  expression there is no check made for the <i>imageid</i> value.  If the file
  is required by the linearity expression and an error occurs accessing it
  then the task will abort.  A selected image must match the input size in
  the first two dimensions.  A third dimnension may be used for expressions
  with multiple coefficients.  The values are referenced with L&lt;index&gt;,
  i.e. L1, L2, etc., where &lt;index&gt; is the index of the third dimension.
  </dd>
  </dl>
  <dl id="l_darks">
  <dt><b>darks = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='darks' Line='darks = ""' -->
  <dd>List of dark calibration images or an expression evaluating to an image.
  If a null list is specified the input list is searched for files that
  satisfy the
  <a href="#l_dtype"><i>dtype</i></A>
  selection expression.  An image list may include
  MEF files which expand to all image extensions.  The list will be searched
  for an image with a matching
  <a href="#l_imageid"><i>imageid</i></A>
  value, the closest
  <a href="#l_exptime"><i>exptime</i></A>
  value to the input image and finally the nearest
  <a href="#l_sortval"><i>sortval</i>.</A>
  Note that
  only requiring a near match in exposure time allows bias or zero exposures
  (those with a zero or very small exposure time) to be used in the absence
  of a dark image obtained with a similar exposure time.  The dark image
  is referred to in expressions by $D.
  </dd>
  </dl>
  <dl id="l_flats">
  <dt><b>flats = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flats' Line='flats = ""' -->
  <dd>List of flat calibration images or an expression evaluating to an image.
  If a null list is specified the input list is searched for files
  that satisfy the
  <a href="#l_ftype"><i>ftype</i></A>
  and
  <a href="#l_gtype"><i>gtype</i></A>
  selection expressions.
  The <i>ftype</i> and <i>gtype</i> expressions are also applied to the images
  in this list to discriminate two types of flat fields (e.g. lamp on and
  lamp off or dome and sky).  However, if an image does not match either
  expression then it is assumed to be an F type flat field.  The list
  may include MEF files which expand to all image extensions.  The list
  will be searched for an image with a matching
  <a href="#l_imageid"><i>imageid</i></A>
  value,
  the same
  <a href="#l_filter"><i>filter</i></A>
  value as the input image and finally the nearest
  <a href="#l_sortval"><i>sortval</i>.</A>
  The flat field images are referred to in expressions by
  $F and $G.
  </dd>
  </dl>
  <dl id="l_flatexpr">
  <dt><b>flatexpr = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flatexpr' Line='flatexpr = ""' -->
  <dd>Optional flat fielding expression (for the F code) which overrides the
  default expression <span style="font-family: monospace;">"($I/$F)"</span> and any expression found in the
  <a href="#l_opdb"><i>opdb</i></A>
  file.  An override is provided to make it easy to combine the $F and $G
  flat field types; i.e. <span style="font-family: monospace;">"($I/($F-$G))"</span> or <span style="font-family: monospace;">"($I/($F*$G))"</span>.
  </dd>
  </dl>
  <dl id="l_skies">
  <dt><b>skies = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skies' Line='skies = ""' -->
  <dd>List of sky images or an expression evaluating to an image.  If a null
  list is specified the input list is searched for files that satisfy
  the
  <a href="#l_stype"><i>stype</i></A>
  selection expression or, if no <i>stype</i> value is
  specified, the entire input list, not identified as dark or flat, is used
  as potential sky images.  The list may include MEF files which expand
  to all image extensions.  The use of the sky images is defined by the
  <a href="#l_skymode"><i>skymode</i></A>
  parameter.  The 
  <a href="#l_skymatch"><i>skymatch</i></A>
  parameter may also apply
  when matching a single sky to an input.  In all cases only images with
  the same 
  <a href="#l_imageid"><i>imageid</i></A>
  and 
  <a href="#l_filter"><i>filter</i></A>
  values as the input will be used.
  In all cases the input image will never be used as a sky for itself.
  </dd>
  </dl>
  <dl id="l_skymatch">
  <dt><b>skymatch = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skymatch' Line='skymatch = ""' -->
  <dd>Sky matching logical expression.  If specified the expression is evaluated
  for each potential sky image against the input image.  If the result is
  true the sky image is used and if it is false it is not used.  The
  expression operands use A_ to refer to a sky image and B_ to refer to
  the target input image.  For example, B_CRVAL1 refers to the CRVAL1 keyword in
  the input image.  This parameter is may be used with the <span style="font-family: monospace;">"arcsep"</span>
  function (see
  <a href="procexpr"><b>procexpr</b></A>
  ) to select skies that are nearby but
  offset by a minimum amount.
  </dd>
  </dl>
  <dl id="l_skymode">
  <dt><b>skymode = <span style="font-family: monospace;">"nearest"</span> (nearest|before|after|median &lt;N&gt; &lt;AVG&gt; &lt;CLIP&gt;)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skymode' Line='skymode = "nearest" (nearest|before|after|median &lt;N&gt; &lt;AVG&gt; &lt;CLIP&gt;)' -->
  <dd>The type of sky background estimation when sky subtraction is enabled.
  This applies when the
  <a href="#l_skies"><i>skies</i></A>
  parameter does not explicitly assign
  a sky image.  As described in the <i>skies</i> parameter, a list of
  sky images which match the input in filter and image ID is defined for
  a particular input image.  The list will also exclude the input image,
  if it is in the list, and will apply the
  <a href="#l_skymatch"><i>skymatch</i></A>
  expression to further define the list.  The final list is sorted by the
  <a href="#l_sortval"><i>sortval</i>.</A>
  The parameter choices are <span style="font-family: monospace;">"nearest"</span> to select the
  nearest image in sort value, <span style="font-family: monospace;">"before"</span> for the nearest before, <span style="font-family: monospace;">"after"</span>
  for the nearest after, and <span style="font-family: monospace;">"median"</span> to form a median from the images.
  The <span style="font-family: monospace;">"median"</span> option takes three optional arguments specifying the number of
  images nearest the input image, in sort value, to be used in the median, the
  number of central values to average, and the clipping factor to eliminate
  positive outliers.  The defaults are 5, 1, and 2.  A value of 0 for
  the clipping factor turns off the clipping as does less than three
  images.  It will also make use of any object mask (
  <a href="#l_obm"><i>obm</i></A>
  ) associated with a sky to exclude sources from the median.  For more
  details on the sky methods see the SKY SUBTRACTION section.
  </dd>
  </dl>
  <dl id="l_repexpr">
  <dt><b>repexpr = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='repexpr' Line='repexpr = ""' -->
  <dd>A general replacement expression for output pixel values.
  Typically the replacement expression would affect only a subset of the
  pixels using thresholds and masks and the <span style="font-family: monospace;">'?'</span> conditional expression
  operator.  If no expression is specified but the replacement option
  is selected the task will skip the operation.  One use for this is to
  replace saturated or underflow pixels by a limit or flag value.
  Saturation values might be specified by a keyword.  An image giving
  values, such as saturation, for each pixel may be used by include
  $R, $R1, $R2, etc in the expression.  The image is given by the
  <a href="#l_repimage"><i>repimage</i></A>
  parameter.
  </dd>
  </dl>
  <dl id="l_repimage">
  <dt><b>repimage = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='repimage' Line='repimage = ""' -->
  <dd>Optional image list or an expression evaluating to an image providing
  per pixel value for the replacement expression.  An image list may
  include MEF files which expand to all image extensions.  When selecting a
  replacement image to apply to a particular input image the nearest based on
  the 
  <a href="#l_sortval"><i>sortval</i></A>
  parameter which has the same value for the 
  <a href="#l_imageid"><i>imageid</i></A>
  parameter is selected.  When an image is selected by an expression there
  is no check made for the 
  <i>imageid</i>
  value.  If the file is required
  by the replacement expression and an error occurs accessing it then the
  task will abort.  A selected image must match the input size in the
  first two dimensions.  A third dimension may be used for expressions
  with multiple parameters.  The values are referenced with R&lt;index&gt;,
  i.e. R1, R2, etc., where &lt;index&gt; is the index of the third dimension.
  </dd>
  </dl>
  <dl id="l_btype">
  <dt><b>btype = <span style="font-family: monospace;">"fit"</span> (fit|ifit|mean|median|minmax)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='btype' Line='btype = "fit" (fit|ifit|mean|median|minmax)' -->
  <dd>The type of bias region algorithm for setting the row or column values to
  subtract.  The bias pixels and the bias subtraction direction (rows or columns)
  are defined by the 
  <a href="#l_biassec"><i>biassec</i></A>
  parameter.  The set of pixels
  at each row or column are collapsed to a single bias value to be subtracted
  from the entire image row or column.  The 
  <a href="#l_btype"><i>btype</i></A>
  parameter selects
  how the pixels are collapsed to a single bias value.  The <span style="font-family: monospace;">"fit"</span>, <span style="font-family: monospace;">"ifit"</span>,
  and <span style="font-family: monospace;">"mean"</span> methods average the pixels.  The <span style="font-family: monospace;">"ifit"</span> and <span style="font-family: monospace;">"fit"</span> choices
  smooth the bias values by fitting a polyomial function interactively or
  non-interactively respectively.  The <span style="font-family: monospace;">"median"</span> choice collapses pixels
  using the median.  The <span style="font-family: monospace;">"minmax"</span> choice rejects the high and low values
  before averaging provided there are at least three pixels.
  </dd>
  </dl>
  <p>
  The following parameters are used for the <span style="font-family: monospace;">"fit"</span> and <span style="font-family: monospace;">"ifit"</span> bias type options.
  </p>
  <dl id="l_bfunction">
  <dt><b>bfunction = <span style="font-family: monospace;">"legendre"</span> (legendre|chebyshev|spline1|spline3)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bfunction' Line='bfunction = "legendre" (legendre|chebyshev|spline1|spline3)' -->
  <dd>Fitting function taken from the following list.
  <div class="highlight-default-notranslate"><pre>
   legendre - legendre polynomial
  chebyshev - chebyshev polynomial
    spline1 - linear spline
    spline3 - cubic spline
  </pre></div>
  </dd>
  </dl>
  <dl id="l_border">
  <dt><b>border = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='border' Line='border = 1' -->
  <dd>Number of polynomial terms or spline pieces in the fit.  Note that an
  order of 1 is a constant when using a polynomial function.
  </dd>
  </dl>
  <dl id="l_bsample">
  <dt><b>bsample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bsample' Line='bsample = "*"' -->
  <dd>Sample lines to use in the fit.  The string <span style="font-family: monospace;">"*"</span> specifies all
  lines otherwise an
  <a href="icfit"><b>icfit</b></A>
  range string is used.
  </dd>
  </dl>
  <dl id="l_bnaverage">
  <dt><b>bnaverage = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bnaverage' Line='bnaverage = 1' -->
  <dd>Number of points to average or median to form fitting points.  Positive
  numbers specify averages and negative numbers specify medians.
  </dd>
  </dl>
  <dl id="l_bniterate">
  <dt><b>bniterate = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bniterate' Line='bniterate = 1' -->
  <dd>Number of rejection interations to remove deviant points from the overscan fit.
  If 0 then no points are rejected.
  </dd>
  </dl>
  <dl id="l_blreject">
  <dt><b>blreject = 3., bhreject = 3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blreject' Line='blreject = 3., bhreject = 3.' -->
  <dd>Low and high sigma rejection factors for rejecting deviant points from the
  overscan fit.
  </dd>
  </dl>
  <dl id="l_bgrow">
  <dt><b>bgrow = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bgrow' Line='bgrow = 0.' -->
  <dd>One dimensional growing radius for rejection of neighbors to deviant points.
  </dd>
  </dl>
  <p style="text-align:center">SELECTION AND GROUPING EXPRESSIONS
  
  </p>
  <p>
  Processing depends on the type of exposure, the the detector, the filter,
  and other characteristics of the instrument.  To make it easy to process
  mixtures of images, to check for proper types of calibrations, and to allow
  configuration for instruments with different characteristics and keywords
  the following parameters are used to interpret the data.  It is an error
  if an input image matches more than one of the 
  <a href="#l_dtype"><i>dtype</i>, </A>
  <a href="#l_ftype"><i>ftype</i>,</A>
  <a href="#l_gtype"><i>gtype</i>,</A>
  and 
  <a href="#l_stype"><i>stype</i></A>
  expressions.
  </p>
  <dl id="l_intype">
  <dt><b>intype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intype' Line='intype = ""' -->
  <dd>Logical expression used to select images from the input image list, such
  as by their observation type keywords.  The null string may be used to
  select all images from the input list.  Note that to select dark, flat
  field, or sky images using the expressions specified with the 
  <a href="#l_dtype"><i>dtype</i>,</A>
  <a href="#l_ftype"><i>ftype</i>, </A>
  <a href="#l_gtype"><i>gtype</i></A>
  or 
  <a href="#l_stype"><i>stype</i></A>
  parameters one can redirect this
  parameter with the value <span style="font-family: monospace;">")&lt;parameter&gt;"</span>.  The <span style="font-family: monospace;">")"</span> is a feature of the
  parameter system to refer to a value from a different parameter.
  </dd>
  </dl>
  <dl id="l_dtype">
  <dt><b>dtype = <span style="font-family: monospace;">"(obstype=='dark')"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dtype' Line='dtype = "(obstype=='dark')"' -->
  <dd>Logical expression used to identify dark exposures in the input list
  for processing and possible use as calibration.  This does not apply
  to images in the 
  <a href="#l_darks"><i>darks</i></A>
  list.  The default expression matches the
  words <span style="font-family: monospace;">"dark"</span> or <span style="font-family: monospace;">"zero"</span> anywhere in the keyword OBSTYPE and ignores case.
  A null expression does not match.
  The processing steps applied to exposures matching this expression are
  specified by the 
  <a href="#l_dorder"><i>dorder</i></A>
  parameter.
  </dd>
  </dl>
  <dl id="l_ftype">
  <dt><b>ftype = <span style="font-family: monospace;">"(obstype=='flat')"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ftype' Line='ftype = "(obstype=='flat')"' -->
  <dd>Logical expression used to identify the F-type flat field exposures
  (e.g. lamp on) in the input list or 
  <a href="#l_flats"><i>flats</i></A>
  list.  The default
  expression matches the word <span style="font-family: monospace;">"flat"</span> anywhere in the keyword OBSTYPE and
  ignores case.  A null expression does not match any images in the input
  list and matches all images in the 
  <a href="#l_flats"><i>flats</i></A>
  list.  The processing
  steps applied to exposures matching this expression are specified by the
  <a href="#l_forder"><i>forder</i></A>
  parameter.
  </dd>
  </dl>
  <dl id="l_gtype">
  <dt><b>gtype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gtype' Line='gtype = ""' -->
  <dd>Logical expression used to identify the G-type flat field exposures
  (e.g lamp off or illumination) in the input list or 
  <a href="#l_flats"><i>flats</i></A>
  list.
  The default expression, the null string, does not match any images.
  The processing steps applied to exposures matching this expression are
  specified by the 
  <a href="#l_forder"><i>forder</i></A>
  parameter.
  </dd>
  </dl>
  <dl id="l_stype">
  <dt><b>stype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='stype' Line='stype = ""' -->
  <dd>Logical expression used to identify sky exposures in the input list for
  processing and use as calibration.  This does not apply to images in the
  <a href="#l_skies"><i>skies</i></A>
  list.  Images identified as sky in the input are processed
  after dark and flat images but before any other types.  If sky images
  are specified by the 
  <a href="#l_skies"><i>skies</i></A>
  list then this parameter is ignored.
  The default expression matches all images which are not identified as
  dark or flat.
  </dd>
  </dl>
  <dl id="l_imageid">
  <dt><b>imageid = <span style="font-family: monospace;">"(imageid)"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imageid' Line='imageid = "(imageid)"' -->
  <dd>String valued expression that groups images from instruments that produce
  multiple image elements from multiple readout streams.  Examples of this
  are multiple CCD amplifiers, multiple section readouts, multiple arrays in
  a mosaic detector.
  </dd>
  </dl>
  <dl id="l_filter">
  <dt><b>filter = <span style="font-family: monospace;">"(filter)"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filter' Line='filter = "(filter)"' -->
  <dd>String valued expression that groups images where the characteristics of
  the calibration depend on the detected photon energies.  Examples of this
  are different filters and different grating settings.  The simplest
  expression is a keyword name that evaluates to the value of the keyword.
  However, an expression can combine the values of several keywords if there
  are multiple filters or gratings.
  </dd>
  </dl>
  <dl id="l_sortval">
  <dt><b>sortval = <span style="font-family: monospace;">"(@'mjd-obs')"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sortval' Line='sortval = "(@'mjd-obs')"' -->
  <dd>Numeric valued expression used to sort images into a sequence.  In the
  absence of an expression, the null string <span style="font-family: monospace;">""</span>, the order in the list
  is used.  Beware of keywords that have periodic boundaries such as time
  of day.  The <span style="font-family: monospace;">"epoch"</span> or <span style="font-family: monospace;">"julday"</span> functions may be used to convert a date
  and time to a running value.  It is a fatal error if a sort expression
  does not evaluate to a numeric value.
  </dd>
  </dl>
  <dl id="l_exptime">
  <dt><b>exptime = <span style="font-family: monospace;">"(exptime)"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exptime' Line='exptime = "(exptime)"' -->
  <dd>Numeric valued expression producing the exposure time.  The units of the
  exposure time are not significant provided it is consistent for the
  dataset and the relative times are linearly related.
  </dd>
  </dl>
  <dl id="l_obdb">
  <dt><b>obdb = <span style="font-family: monospace;">"newfirm$obdb.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obdb' Line='obdb = "newfirm$obdb.dat"' -->
  <dd>Operation database.  This text file allows overriding and customizing
  the definitions of most of the various operations.  It also allows adding
  some custom operations.  See the
  <a href="#s_operation_expressions_and_the_operation_database">OPERATION EXPRESSIONS AND THE OPERATION DATABASE</A>
  section for details.
  </dd>
  </dl>
  <dl id="l_override">
  <dt><b>override = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='override' Line='override = no' -->
  <dd>Override previous processing as given by the PROCDONE keyword?  If set to
  yes then the selected processing will be performed on images which have
  header keywords indicating the operations have been peformed previously.
  </dd>
  </dl>
  <dl id="l_copy">
  <dt><b>copy = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='copy' Line='copy = no' -->
  <dd>Copy the input image to the output if no processing is required.
  This may be needed in processing scripts and pipelines that don't wish to
  deal with the situtation where an expected output is not produced.
  </dd>
  </dl>
  <dl id="l_erraction">
  <dt><b>erraction = <span style="font-family: monospace;">"warn"</span> [warn|abort|quit]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='erraction' Line='erraction = "warn" [warn|abort|quit]' -->
  <dd>Action to take if an ignorable error is encountered.  If <span style="font-family: monospace;">"warn"</span> is set
  then a warning is issued and the task will continue, either skipping the
  operation or skipping the input image depending on the type of error.
  If <span style="font-family: monospace;">"abort"</span> is set then the task will abort with an <span style="font-family: monospace;">"ERROR"</span> message.
  The <span style="font-family: monospace;">"quit"</span> mode prints a error to the standard output and the task exits
  normally.  The purpose of this is allow a calling script to read the error
  without causing the script to abort.  .le .ls gdevice = <span style="font-family: monospace;">"stdgraph"</span> Graphics
  device.  The string <span style="font-family: monospace;">"stdgraph"</span> selects the standard interactive grpahics
  device which is usually the graphics terminal.  This is currently only
  used for interactive bias fitting.  .le .ls gcursor = <span style="font-family: monospace;">""</span> Graphics cursor.
  The value <span style="font-family: monospace;">""</span> selects the standard graphics cursor.  This is currently
  only used for interactive bias fitting.  .le .ls gplotfile = <span style="font-family: monospace;">""</span> Output
  plot file for graphics.  This is currently only used for recording the
  results of fitting the bias.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>NFPROC</b> processes detector array data (CCDs, IR arrays), stored
  as images, to correct or calibrate defects, electronic and detector
  bias, signal dependent linearity, flat field response, and sky background.
  The output images may also be trimmed to specified regions to exclude
  bad edges and non-imaging pixels such as bias or reference pixels.
  </p>
  <p>
  The 
  <a href="#l_input"><i>input</i></A>
  is a list of files to be processed, along with optional
  bad pixel masks (
  <a href="#l_bpm"><i>bpm</i></A>
  ) and object masks (
  <a href="#l_obm"><i>obm</i></A>
  ), and the
  <a href="#l_output"><i>output</i></A>
  is a matching list of output files, a pattern substitution,
  or an expression that returns an output filename.  The input files may
  be simple images or multi-extension FITS (MEF) files.  When an MEF input
  file is specified, the global header (i.e. a data-less primary FITS HDU)
  is copied to the output, the images (which may include a populated primary
  HDU) are processed, and all other extensions are ignored.  The masks are
  associated with the input either through header information, or a single
  mask file to apply to all input files (with matching extension names if
  the inputs are MEFs), or a matching list.
  </p>
  <p>
  The order in which the input images and MEF extensions are processed
  is controlled by the program.  If different types of exposures, such as
  dark, flat field, sky, and object, are in the input list then all the dark
  exposures are done first, followed by the flat exposures, followed by the
  sky exposures, and finally the object exposures.  Other types of ordering
  imposed by the task are by 
  <a href="#l_imageid"><i>imageid</i>,</A>
  <a href="#l_filter"><i>filter</i></A>
  and 
  <a href="#l_sortval"><i>sortval</i>.</A>
  Since 
  <a href="#l_imageid"><i>imageid</i></A>
  is usually the extension in MEF files, the output
  MEF will be built up in multiple passes where all of one extension are
  done before going on to the next extension.  This is done for efficiency
  reasons.
  </p>
  <p>
  The output files are single images or MEF files to match the input.
  Output MEF files are created by appending each processed input image
  extension to the output file.  Global headers and inheritance structure
  are preserved.
  </p>
  <p>
  The output file cannot be the same as the input file because in some case
  the input file is also used as calibrations such as for sky subtraction.
  However, output file names are often variants of the input names and
  a special pattern substitution feature is provided.  The character <span style="font-family: monospace;">'+'</span>
  in the output parameter will be substituted with the name of the input
  image minus any path or extension.  Other types of substitutions include
  prepending and appending with '//' and <span style="font-family: monospace;">'%'</span> (see
  <a href="imrename"><b>imrename</b></A>
  ).
  Alternatively one can use an expression that can build filenames, typically
  by using a keyword in the input image header.
  </p>
  <p>
  Log output (
  <a href="#l_logfiles"><i>logfiles</i></A>
  ) is provided to zero or more text streams or
  files and to the header keywords PROCnnnn (where nnnn is a four digit
  sequence number).  In addition, the special 
  <a href="#l_output"><i>output</i></A>
  value <span style="font-family: monospace;">"+LIST+"</span>
  may be used to produce log output without processing the input.
  </p>
  <p>
  This task is very flexible to accommodate different instruments,
  calibration methods and processing modes.  This flexibility is provided by
  ubiquitous use of expressions.  An expression is a syntax using variables
  and constants that evaluate to logical, numeric, and string values.
  The power lies in variables, also called operands, whose values are keyword
  or pixel values from the input or calibration images.  For a description
  and discussion of expressions see
  <a href="procexpr"><b>procexpr</b>.</A>
  For more specifics of this task see the section
  <a href="#s_operation_expressions_and_the_operation_database">OPERATION EXPRESSIONS AND THE OPERATION DATABASE.</A>
  </p>
  <p>
  Often one wants to process different types or groups of exposures.
  This may be done explicitly by naming only the files to be processed in
  the input list.  Alternatively a larger list, such as <span style="font-family: monospace;">"*.fits"</span> may be used
  and either have the task identify a particular subset of images or group
  the exposures and process them in a standard order.  The 
  <a href="#l_intype"><i>intype</i></A>
  </p>
  <p>
  parameter provides a selection expression (one with a logical result)
  that is applied to each input image.  If no selection expression is
  specified then all the input images are processed.
  </p>
  <p>
  A common type of input selection is to process bias, dark, and
  flat field exposures before combining them into master calibrations
  to be applied to the science exposures.  Because this is so common
  the 
  <a href="#l_dtype"><i>dtype</i>,</A>
  <a href="#l_ftype"><i>ftype</i>,</A>
  <a href="#l_gtype"><i>gtype</i></A>
  and 
  <a href="#l_stype"><i>stype</i></A>
  selection
  parameters may be used with the 
  <a href="#l_intype"><i>intype</i></A>
  parameter by
  using the syntax <span style="font-family: monospace;">")&lt;parameter&gt;"</span> (e.g. <span style="font-family: monospace;">")ftype"</span> to use the flat
  field selection expression).  As discussed later, there are <span style="font-family: monospace;">"order"</span>
  parameters that allow different types of exposures to be processed
  differently.
  </p>
  <p>
  The 
  <a href="#l_dtype"><i>dtype</i>,</A>
  <a href="#l_ftype"><i>ftype</i>,</A>
  <a href="#l_gtype"><i>gtype</i>,</A>
  and 
  <a href="#l_stype"><i>stype</i></A>
  parameters are
  also used for identifying and grouping of input images.  The processing
  of a mixed input list of exposure types is done in the following order.
  First all bias/dark images, then all flat images, then all sky images,
  then all remaining images.
  </p>
  <p>
  Another winnowing of the input list is a check for previous processing.
  The task adds the keyword PROCDONE to the output headers.  When a
  previously processed image is used as an input image the keyword is checked
  to determine what was done.  Therefore, if all the requested steps have
  been done the image will be skipped and if only some have been done
  just the new steps are performed.
  </p>
  <p>
  The 
  <a href="#l_override"><i>override</i></A>
  parameter may be used to override this prohibition
  against repeating operations that have been previously done.  Note that
  a valid, though not recommended, alternative is to delete or edit the
  PROCDONE header keyword.  There are some operations that do make sense to
  repeat, albeit with different parameters or calibrations.  These include
  corrections to the flat field, detecting and fixing additional bad pixels,
  and using additional data for sky subtraction.
  </p>
  <p>
  A related parameter is 
  <a href="#l_copy"><i>copy</i>.</A>
  This tells the task whether to
  create an output image even if there are no steps to be performed;
  either because they have been done or none are selected.  The output
  image would be a copy of the input, hence the parameter name.  This
  may be needed in processing scripts and pipelines that don't wish to
  deal with the situtation where an expected output is not produced.
  </p>
  <p>
  The 
  <a href="#l_erraction"><i>erraction</i></A>
  parameter is provided to control whether an error will
  abort the task, and so any calling scripts that don't catch the abort,
  or if only a warning or error message is printed to the standard error
  output.  The distinction is most useful when processing a list of images.
  In some cases one would like the processing to stop immediately, including
  the parent script, to fix the source of the error.  But in more automated
  situations one may want to continue on to other images in the list and
  deal with the warning messages later.  The <span style="font-family: monospace;">"quit"</span> mode is intermediate
  between an abort and a warning in that it lets the task exit immediately
  but without aborting a parent script.  The script can monitor the standard
  error output to detect the exit.
  </p>
  </section>
  <section id="s_processing">
  <h3>Processing</h3>
  <p>
  Processing consists of applying a set of operations to each input pixel
  in a particular order.  The task defines a set of standard operations
  using common detector calibration nomenclature, along with associated
  parameters, and provides the ability to customize these as well as adding
  additional operations.
  </p>
  <p>
  The standard operations are:
  </p>
  <span id="table1"></span>
  <p>
  <b>Table 1: Standard processing operations.</b>
  </p>
  <div class="highlight-default-notranslate"><pre>
                 trimming - removing bad or non-imaging border areas
  bad pixel interpolation - replacing pixels by interpolation
    bad pixel replacement - replacing pixels by other values
     linearity correction - correct for non-linearity
         bias subtraction - subtraction of bias from reference pixels
         dark subtraction - subtraction of a dark calibration
            flat fielding - division by a flat field calibration
          sky subtraction - subtraction of background sky in various ways
            normalization - divide by a constant and provide a minimum value
  </pre></div>
  <p>
  Applying a processing operation consists of several steps:
  </p>
  <dl id="l_1">
  <dt><b>1.</b></dt>
  <!-- Sec='PROCESSING' Level=0 Label='1' Line='1.' -->
  <dd>Selecting the operation with its processing switch parameter.
  </dd>
  </dl>
  <dl id="l_2">
  <dt><b>2.</b></dt>
  <!-- Sec='PROCESSING' Level=0 Label='2' Line='2.' -->
  <dd>Specifying where in the order of operations it is to be performed.
  </dd>
  </dl>
  <dl id="l_3">
  <dt><b>3.</b></dt>
  <!-- Sec='PROCESSING' Level=0 Label='3' Line='3.' -->
  <dd>Setting parameters associated with the operation.
  </dd>
  </dl>
  <dl id="l_4">
  <dt><b>4.</b></dt>
  <!-- Sec='PROCESSING' Level=0 Label='4' Line='4.' -->
  <dd>Deciding whether an operation previously performed is to be skipped
  or repeated.
  </dd>
  </dl>
  <p>
  In the most common cases the default parameters are sufficient and one
  need only specify the calibration files.
  </p>
  <p>
  In addition to setting up the operations the task also needs information
  about how to:
  </p>
  <dl id="l_1">
  <dt><b>1.</b></dt>
  <!-- Sec='PROCESSING' Level=0 Label='1' Line='1.' -->
  <dd>interpret the exposure type; currently the types are
  dark, two types of flat fields (e.g. lamp on and lamp off dome
  flats or dome and sky flats), sky images for subtraction, and
  science target exposures.
  </dd>
  </dl>
  <dl id="l_2">
  <dt><b>2.</b></dt>
  <!-- Sec='PROCESSING' Level=0 Label='2' Line='2.' -->
  <dd>select the appropriate calibration from a set of alternatives; such
  as by detector (in a mosaic), filter, exposure time, and nearby in
  time or space.
  </dd>
  </dl>
  <p>
  Each potential operation, including user defined operations, has a single
  letter code (see
  <a href="#table2">Table 2</A>
  and the sections below).  The order parameters --
  <a href="#l_dorder"><i>dorder</i>,</A>
  <a href="#l_forder"><i>forder</i>,</A>
  and 
  <a href="#l_order"><i>order</i></A>
  -- are specified as strings
  of operation codes.  There are different order parameters applied
  depending on the observation type of the input image.  Different observation
  types
  have different allowed operations or special operations.  The order of the
  codes defines the order of the operations and the absence or presence of a
  code defines whether or not an operation is allowed.  Note that whether an
  operation is allowed and whether it is to be done are not the same thing.
  Operations to be performed are selected using processing switch (yes/no)
  parameters.  This means that to perform an operation requires that both
  its processing switch is enabled and its operation code appears in in
  the order parameter.
  </p>
  <p>
  The combination of processing switches and order parameters, which may
  be expressions based header keywords, provides flexibililty in how this
  task is used.  Normally the order of operations is rarely changed and
  the operations are controlled through the processing switches.  But by
  setting all the switches to yes the processing steps may be controlled
  by the order parameters.  Because the order parameters may be set by an
  expression it is possible to control processing through header keywords
  as might be desired in a pipeline situation.
  </p>
  <p>
  The sequence of operations are performed on each line of an input image
  before going on to the next line.  However, operations can also be defined
  to occur after all lines are processed by preceeding operations.  This is
  done by delimiting <span style="font-family: monospace;">"groups"</span> of operation codes with commas in the order
  parameters.  In execution, all operations from the first group are applied
  to all lines, followed by all operations of the next group applied to all
  lines, etc.  The operations in the first group result in creating the
  output image and subsequent groups work in-place on the output image.
  </p>
  <p>
  Trimming and bad pixel interpolation are performed when the input image
  read.  Therefore, where the operation codes for these occur in the order
  parameters is not relevant except that bad pixel interpolation can be
  done in any processing group while trimming is limited to just the first
  group because in-place processing cannot alter the size of the image.
  </p>
  <p>
  The different processing operations have related parameters which must
  be set.  These are things like image sections defining the bias pixels
  and trim region and calibration image lists.  These parameters and how the
  various operations are performed are described in the following sections.
  </p>
  </section>
  <section id="s_operation_expressions_and_the_operation_database">
  <h3>Operation expressions and the operation database</h3>
  <p>
  Most of the operations performed by this task are defined by expressions
  that produce pixel values using image and keyword operands (see the
  <a href="#s_expression_operands">EXPRESSION OPERANDS</A>
  section as well as 
  <a href="procexpr"><b>procexpr</b></A>
  ).  The result of one operation is
  used as the input value for the next operation with the final operation
  producing the output image pixel values.
  </p>
  <p>
  The operation expressions are set in three steps.  First the task
  defines default expressions for each operation it provides (see
  <a href="#table2">Table 2</A>
  ).  Then an operation database may be read to override these and also to
  add new expressions which can be referenced in the order parameters.
  The default operation database usually consists of the same expressions as
  the task defaults; see below for the default/sample operation database for
  this task.  Finally, some operations have explicit task parameters, such
  as 
  <a href="#l_linexpr"><i>linexpr</i>,</A>
  to make it convenient to set and override expressions
  without needing to copy and edit an operation database.
  </p>
  <p>
  An operation database is a text file that may be specified with the
  <a href="#l_opdb"><i>opdb</i></A>
  parameter.  This database allows overriding many of the
  operation definitions and adding new operations.  The first word is a
  single letter operation code.  The second word is a label used in the
  logging, and the third word is the expression.  Note that the words must
  be quoted if they contain whitespace.  Null strings, specified as <span style="font-family: monospace;">""</span>,
  leave the current definition unchanged.
  </p>
  <p>
  When defining new operations they may only reference the image operands
  shown in table X.  Remember that the operation code also needs to be
  added to the processing order parameters to be applied.
  </p>
  <p>
  Below is a sample operation database.  The expressions are generally
  the same as the default expressions and so are not actually needed.
  The example shows defining a <span style="font-family: monospace;">"user"</span> expression that combines dark subtraction
  and flat fielding into a single operation.  The example quotes the second
  and third words though this is not strictly necessary in cases where
  there is no whitespace.
  </p>
  <span id="table2"></span>
  <p>
  <b>Table 2: Sample Operation Database</b>
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Operation database.
  
  B  "bias correction"            "($I-$B)"
  D  "dark calibration"           "($I-$D)"
  F  "flat calibration"           "($I/$F)"
  G  "flat calibration"           "($I/$G)"
  N  "normalize"                  "(max(0.1,$I/procmean))"
  S  "sky subtraction"            "($I-$S)"
  U  "user"                       "(($I-$D)/$F)"
  </pre></div>
  </section>
  <section id="s_expression_operands">
  <h3>Expression operands</h3>
  <p>
  Pixel and keyword values are referenced in expressions by
  '$&lt;code&gt;[&lt;index&gt;]' and [&lt;code&gt;.]&lt;keyword&gt;, respectively, where &lt;code&gt;
  is a single letter image operand code and &lt;index&gt; is an optional band
  index.  Table 3 shows the possible image operands available in this task.
  Note that the image, or derived image in some cases, is only accessed when
  an expression is evaluated and requires that various supporting parameters,
  for instance 
  <a href="#l_darks"><i>darks</i>,</A>
  be appropriately specified.  These refer to
  the input image or those associated or assigned to the input image.
  Derived data do not have keywords.
  </p>
  <p>
  Table 3: Image Operands for Expressions
  </p>
  <div class="highlight-default-notranslate"><pre>
  I - input image
  M - bad pixel mask
  O - object mask
  D - dark image
  F - flat field
  G - flat field
  L - linearity image
  R - replacement image
  S - derived or actual sky image
  B - derived bias
  </pre></div>
  <p>
  For pixel values $I refers to the input values after prior operations
  have been applied.
  </p>
  </section>
  <section id="s_standard_processing_operations">
  <h3>Standard processing operations</h3>
  <dl id="l_TRIM">
  <dt><b>TRIM (T)</b></dt>
  <!-- Sec='STANDARD PROCESSING OPERATIONS' Level=0 Label='TRIM' Line='TRIM (T)' -->
  <dd>The input image is trimmed to the image section specified by the
  <a href="#l_trimsec"><i>trimsec</i></A>
  parameter.  This trim should be the same as that used for
  the calibration images.  The trimming is done on input and so it doesn't
  matter where the <span style="font-family: monospace;">'T'</span> code appears in the processing order parameters.
  Trimming may only be done on the first pass set of operations because
  subsequent pass are done in-place on the output image and trimming
  cannot be done in-place.  After trimming the keywords TRIMSEC, BIASSEC,
  and DATASEC are removed if they are present.
  The 
  <a href="#l_trimsec"><i>trimsec</i></A>
  parameter is typically either an explicit trim section
  or an expression pointing to a keyword whose value is the section.  A
  more sophisticated trim section expression might create the section from
  keywords in the header.
  <b>Figure 3: Examples of 
  <a href="#l_trimsec"></b><i>trimsec</i></A>
  expressions
  <div class="highlight-default-notranslate"><pre>
  trimsec = "[2:2023,2:2023]"
  trimsec = "(trimsec)"
  trimsec = "('[2:'//str(naxis1-1)//',2:'//str(naxis2-1)//<span style="font-family: monospace;">']'</span>)"
  </pre></div>
  </dd>
  </dl>
  <dl id="l_FIXPIX">
  <dt><b>FIXPIX (P)</b></dt>
  <!-- Sec='STANDARD PROCESSING OPERATIONS' Level=0 Label='FIXPIX' Line='FIXPIX (P)' -->
  <dd>Bad pixels are replaced by linear interpolation from neighboring lines
  and columns.  The bad pixels are those with values of one in the bad
  pixel mask specified by the 
  <a href="#l_bpm"><i>bpm</i></A>
  parameter.  A mask is matched to an
  input image using physical pixels (the LTV/LTM mapping in the header).
  The interpolation is done when a line is first read at the start of
  a group and does not depend on where the <span style="font-family: monospace;">'P'</span> code is in the order
  parameter.  To apply pixel interpolation after other operations the
  order parameter needs to break the operations into groups and the <span style="font-family: monospace;">'P'</span>
  code is then in a that later group.  For example, the order parameter
  <span style="font-family: monospace;">"DF,P"</span> specified interpolation after the input image has been dark and
  flat field calibrated.
  </dd>
  </dl>
  <dl id="l_BIASCOR">
  <dt><b>BIASCOR (B)</b></dt>
  <!-- Sec='STANDARD PROCESSING OPERATIONS' Level=0 Label='BIASCOR' Line='BIASCOR (B)' -->
  <dd>The bias correction calculates a bias value for an image line or column,
  from either the bias pixels from just that line or column or from all
  the bias pixels, and subtracting that value from all the pixels in the
  line/column.  There are a number of parameters defining this correction.
  The first is the 
  <a href="#l_biassec"><i>biassec</i></A>
  parameter which is an image section
  identifying the bias pixels and whether it applies to lines or columns.
  The section must span the input image along one and only one dimension.
  If it spans all rows in the image a row-wise bias correction will
  be applied and if it spans all columns in the image a column-wise
  correction will be made.  For example, in a 1000x2000 image the section
  <span style="font-family: monospace;">"[1:1000,1937:2000]"</span> is a section along the top of the image and the
  bias correction is column oriented while the section <span style="font-family: monospace;">"[1:64,1:2000]"</span>
  will be row oriented.  Remember <span style="font-family: monospace;">'*'</span> in an image section refers to the
  size of the image along columns or rows depending on where it is used.
  Note that the task requires the bias pixels are recorded in the image
  data as a contiguous strip.
  As with the 
  <a href="#l_trimsec"><i>trimsec</i></A>
  parameter the bias section may be an
  explicit string or an expression.  Expressions are usually a single
  keyword whose value is the section though a section could be built
  up from multiple keywords.
  The 
  <a href="#l_btype"><i>btype</i></A>
  parameter specifies the algorithm.  There two types
  of algorithms.  One is where only the bias pixels for an image line/column
  are used and the other is where all the bias pixels are used.
  The line/column algorithms are <span style="font-family: monospace;">"mean"</span>, <span style="font-family: monospace;">"median"</span>, and <span style="font-family: monospace;">"minmax"</span>.
  The mean algorithm uses the mean of all the bias pixels on the line/column
  for the bias value.  Because there may be bad bias pixels the
  <span style="font-family: monospace;">"median"</span> option uses the median for the bias value.  But the median is
  not a very statistically efficient estimate (meaning for a given sample
  size it has larger uncertainty than the mean if bad data is not present).
  So the another algorithm is to assume that bad pixels are rare so that by
  excluding the highest and lowest values from the mean the statistical
  estimate is not affected by the bad data.  This estimate for the bias value
  has the option name <span style="font-family: monospace;">"minmax"</span>.
  The algorithm that combines all the bias pixels collapses the bias pixels
  at each line/column as mean value.  The collection of mean bias values
  as a function of the line/column is the <span style="font-family: monospace;">"bias vector"</span>.  Because the individual
  mean bias values may be noisy due to small number sampling, the bias
  vector is smoothed by fitting a function.  This assumes that the
  trends in the bias during readout are smooth.  Note that one type of function
  is a constant which is equivalent to averaging all the bias pixels into a
  single value for the image.  The bias types for this algorithm are <span style="font-family: monospace;">"fit"</span>
  and <span style="font-family: monospace;">"ifit"</span> for an interactive and non-interactive fit respectively.
  The fit uses the standard IRAF curve fitting package
  <a href="icfit"><b>icfit</b>.</A>
  </dd>
  </dl>
  <dl id="l_LINEARITY">
  <dt><b>LINEARITY CORRECTION (L)</b></dt>
  <!-- Sec='STANDARD PROCESSING OPERATIONS' Level=0 Label='LINEARITY' Line='LINEARITY CORRECTION (L)' -->
  <dd>The linearity correction replaces pixel values by a new value which is a
  function of the orginal pixel value.  The correction is specified in
  the operation database or the 
  <a href="#l_linexpr"><i>linexpr</i></A>
  parameter.  The latter takes
  precedence over the former.  The linearity expression is in terms of the
  uncorrected pixel value, represented in the expression by the operand $I,
  and the result is the corrected pixel value.
  The expression is typically a monotonically increasing polynomial.
  The coefficients of the polynomial are constants, keywords pointing to
  constants, or pixel values from a coefficient image specified by the
  <a href="#l_linimage"><i>linimage</i></A>
  parameter.  In the first two cases all pixels use the same
  coefficients and in the last case the linearity correction can be different
  for each pixel.  Values from the linearity image are specified by
  $L, $L1, $L2, etc (see
  <a href="#s_expression_operands">EXPRESSION OPERANDS</A>
  ).
  Typical expressions, with and without positional dependence, might be a
  polynomials such as
  <div class="highlight-default-notranslate"><pre>
  "$I * (1 + $L1 * $I)"         # With linearity image
  "$I * (1 + 0.001 * $I)"       # Without linearity image
  "$I * (1 + LINCOEFF * $I)"    # With coefficient in header
  </pre></div>
  Fairly complex expressions can be built up, particularly using the
  conditional evaluation operator:
  <div class="highlight-default-notranslate"><pre>
  "$I*(1+$I*($I&lt;100?$L1:($I&lt;25000?$L1+$L2*($I-100) : 2.5)))"
  "$I*(1+$I*($I&lt;100?0.01 : ($I&lt;25000?0.01+0.0001*($I-100) : 2.5)))"
  </pre></div>
  Long expressions may be put into a file and referenced with the syntax
  <span style="font-family: monospace;">"@(&lt;filename&gt;)"</span>.
  The task will select a linearity image with the same 
  <a href="#l_imageid"><i>imageid</i></A>
  and 
  <a href="#l_filter"><i>filter</i>.</A>
  When there is more than one the the nearest in
  <a href="#l_sortval"><i>sortval</i></A>
  is selected.
  </dd>
  </dl>
  <dl id="l_DARK">
  <dt><b>DARK CORRECTION (D)</b></dt>
  <!-- Sec='STANDARD PROCESSING OPERATIONS' Level=0 Label='DARK' Line='DARK CORRECTION (D)' -->
  <dd>Normally dark correction consists of subtracting
  a dark calibration image which is an average of one or more exposures with
  no light falling on the detector, either because the shutter is closed or
  a dark filter is used.
  There are two common dark correction methods.  One is to use a
  dark calibration image taken with the minimum exposure time.  This is
  sometimes called a zero or bias calibration.  Typically this is used
  when the detector is <span style="font-family: monospace;">"quiet"</span> and signal does not appreciable accumulate
  with time when no light is falling on the detector.  This is common with
  CCD detectors.  The second method is to subtract a calibration taken with
  the same, or nearly the same exposure time, as the image being calibrated.
  Either method may be used with this task.  The expression may also
  apply a scaling based on the ratio of input image dark exposure time and
  the exposure time of the dark calibration.
  When a list of dark calibrations (either from 
  <a href="#l_darks"><i>darks</i></A>
  or 
  <a href="#l_input"><i>input</i></A>
  )
  is used the task will select the one with the same 
  <a href="#l_imageid"><i>imageid</i></A>
  which is nearest in 
  <a href="#l_exptime"><i>exptime</i></A>
  to the input image.  When there is more
  than one the the nearest in 
  <a href="#l_sortval"><i>sortval</i></A>
  is selected.  In other words,
  matching the exposure time has higher precedence but if when there is more
  than one possibility then the nearest in 
  <a href="#l_sortval"><i>sortval</i></A>
  is used where
  the sort value is typically the time of the exposure.
  </dd>
  </dl>
  <dl id="l_FLAT">
  <dt><b>FLAT FIELD CALIBRATIONS (F,G)</b></dt>
  <!-- Sec='STANDARD PROCESSING OPERATIONS' Level=0 Label='FLAT' Line='FLAT FIELD CALIBRATIONS (F,G)' -->
  <dd>Flat fielding consists of applying a relative response correction to
  each pixel.  Typically this is done by dividing by a calibration image
  of an assumed uniform illumination.  These are derived from dome lamp,
  twilight, or dark sky stacked exposures.  Variants in the infrared include
  dividing by the different of exposures with a dome lamp on and off.
  There are two types of flat field calibration images and operations
  that may be identified and used separately or in combination.  Users have
  the flexibility to define these two types and the operations performed.
  Two common cases are dome flats with the lamp on and the lamp off
  and dome flat fields and illumination or sky flat field changes relative
  to the dome flat field.  An example of an operation
  that might be used which combines the lamp on and off flat field types is
  <span style="font-family: monospace;">"($I/($F-$G))"</span>.
  The flat field calibration images are selected using the 
  <a href="#l_flats"><i>flats</i></A>
  parameter or, if the parameter is a null string, from the list of input
  images.  Flat field images are identified by the expressions 
  <a href="#l_ftype"><i>ftype</i></A>
  and 
  <a href="#l_gtype"><i>gtype</i>.</A>
  If images are specified by the 
  <a href="#l_flats"><i>flats</i></A>
  parameter
  and an image does not match either type expression then the image will be
  assumed to be an F-type flat field.  If an images matches both expressions
  then it is an error.
  Flat field images must match the input based on the 
  <a href="#l_imageid"><i>imageid</i></A>
  and
  <a href="#l_filter"><i>filter</i></A>
  expressions.  When there is more than one candidate flat
  field the nearest based on the 
  <a href="#l_sortval"><i>sortval</i></A>
  parameter is selected.
  For instance, when the sort value is time of the exposure the nearest
  in time of the appropriate filter and image element (e.g. mosaic extension)
  is selected.
  For the most common case of a single type of flat field the default
  expression <span style="font-family: monospace;">"($I/$F)"</span> is the one to use.  But having the option to
  identify and use more than one type of flat field, particularly for
  the lamp on and lamp off method, requires flexibility in setting the
  operation.  As with other operations, one can make a personal version
  of the default operation database.  But the task also provides the
  <a href="#l_flatexpr"><i>flatexpr</i></A>
  parameter to make it convenient to set the the F-type
  flat fielding expression.  This expression, if not null, overrides
  the task default and the operation database.
  The default expression <span style="font-family: monospace;">"($I/$F)"</span> does not apply a scale factor or check
  for division by zero.  Therefore, the flat field calibration images should
  be normalized and values near or below zero replaced by a default value.
  These steps (normalization and checking for bad flat field values) can be
  done when first processing the flat field exposures (see the normalize
  operations).  Alternatively, one can modify the expression to include a
  scale factor and threshold.  For example, <span style="font-family: monospace;">"($I/max(0.01,$F/F.procmean)))"</span>
  would normalize the flat field by the value of a keyword PROCMEAN in the
  flat field image header and protect against division by zero or negative
  values).
  </dd>
  </dl>
  <dl id="l_SKY">
  <dt><b>SKY SUBTRACTION (S)</b></dt>
  <!-- Sec='STANDARD PROCESSING OPERATIONS' Level=0 Label='SKY' Line='SKY SUBTRACTION (S)' -->
  <dd>Sky subtraction is selected by the 
  <a href="#l_skysub"><i>skysub</i></A>
  switch and the S operation
  code.  The candidate sky images are specified by the 
  <a href="#l_skies"><i>skies</i></A>
  parameter
  or, if null, selected the input list.  The 
  <a href="#l_skies"><i>skies</i></A>
  parameter may be a
  list of images or an expression resolving to an image for each input image.
  An expression typically selects an image header keyword associating a
  sky image with the input image.  In this case sky subtraction is just a
  simple single image subtraction ignoring the 
  <a href="#l_skymode"><i>skymode</i></A>
  and other sky
  parameters and with no checks on the filter or image ID as described in
  the remainder of this section.
  When the 
  <a href="#l_skies"><i>skies</i></A>
  parameter is null the 
  <a href="#l_stype"><i>stype</i></A>
  expression is used
  to identify sky images from the input list.  This parameter is not used
  otherwise.  If the 
  <a href="#l_stype"><i>stype</i></A>
  expression is null then all images not
  identified as dark or flat field by the other type selection expressions
  are candidate sky images.  This is typically done when sky subtracting from
  dithered sparse-field observations.  Note that if 
  <a href="#l_stype"><i>stype</i></A>
  is not null,
  it is an error if a sky image also matches as a dark or flat field image.
  One or more sky images is then selected for each input image.  Note
  that the sky selection process may include the input image but it is
  excluded as sky for itself.  The sky images must have the same value
  of the 
  <a href="#l_imageid"><i>imageid</i></A>
  and 
  <a href="#l_filter"><i>filter</i></A>
  expressions as the input image.
  In addition, sky images must satistfy the 
  <a href="#l_skymatch"><i>skymatch</i></A>
  expression which
  allows comparing keywords from the input and candidate sky image using the
  references <span style="font-family: monospace;">"A_&lt;keyword&gt;"</span> and <span style="font-family: monospace;">"B_&lt;keyword&gt;"</span>.  One example is to require a
  sky image to be near, but not too near, the position of the input image.
  The following uses a file containing an expression based on the separation
  of the two images in arc seconds.
  <div class="highlight-default-notranslate"><pre>
  skymatch = "@(arcsep.dat)"
  
  where the file arcsep.dat contains
  
  (arcsep(A_RA,A_DEC,B_RA,B_DEC)&gt;600 &amp;&amp;
   arcsep(A_RA,A_DEC_B_RA,B_DEC)&lt;3600))
  
  or
  
  (arcsep(A_CRVAL1/15,A_CRVAL2,B_CRVAL1/15,B_CRVAL2)&gt;600 &amp;&amp;
   arcsep(A_CRVAL1/15,A_CRVAL2,B_CRVAL1/15,B_CRVAL2)&lt;3600))
  </pre></div>
  Note that the CRVAL1 values are right ascension in degrees while the arcsep
  function requires hours.  Note that if the data have offset parameters
  those would be easier to use.
  Another example might be that the sky and input images have different
  nod flags as in the following.
  <div class="highlight-default-notranslate"><pre>
  skymatch = "(A_NOD!=B_NOD)"
  </pre></div>
  Once a set of candidate sky images is selected for a particular input
  image the 
  <a href="#l_skymode"><i>skymode</i></A>
  parameter selects from this list and specifies how
  they are used.  The candidate list is sorted by the 
  <a href="#l_sortval"><i>sortval</i></A>
  values.
  The options <span style="font-family: monospace;">"before"</span>, <span style="font-family: monospace;">"after"</span>, or <span style="font-family: monospace;">"nearest"</span> select a single sky image
  to subtract which has is the nearest before, after, or on either side
  of the input image, respectively.  If there is no image before or
  after as requested then the nearest is used.
  The option <span style="font-family: monospace;">"median [&lt;N&gt; [&lt;AVG&gt;] [&lt;CLIP&gt;]]"</span> (where the default value of N is
  5, of AVG is 1, and of CLIP is 2) selects the nearest N/2 (rounded down to
  an integer) sky images before the input image and the (N-1) subsequent
  images.  When there are not enough images before or after then images are
  added at the other end.  Of course if there are fewer than N images then all
  are used.  Again, note that if the input image is in the candidate list it
  is excluded with the result that median is computed from N-1 images.
  The clipping option computes the difference between the median (before
  clipping) and the lowest value.  This difference multiplied by the
  clipping factor and reflected to values above the median.  Values
  beyond this clipping threshold are excluded from the final median
  calculation.  A clipping value less than or equal to zero may be used
  to skip the clipping.
  The median calculation will make use of any object mask (
  <a href="#l_obm"><i>obm</i></A>
  )
  associated with a sky to exclude sources from the median.  When pixels
  are excluded then the median is taken over a smaller number of pixels.
  After the pixels are sorted the specified average of the central values
  is taken.  Note that if the number of values averaged is rounded
  up to an even number when the number of remaining pixels is even or
  rounded up to an odd number when number of pixels is odd to insure
  a symmetric statistic.  When the average is 1, a classic median,
  this means that for an even number of pixels the average of the central
  two values is the median value.
  Please note that during processing that the input list is processed in
  an order determined by the different observation types and within each
  type by the sort value.  For median sky subtraction this means that
  a running median window can be used with an algorithm optimized to
  make use of this order.
  One observing mode is when the science fields are sparse and
  dithered exposures are taken with the intent that sky will be
  obtained from a median of temporally close exposures.  This would
  use the running median method.  One could process the science
  exposures for instrumental calibrations first and then do the
  running median sky subtraction.  However, using the operation
  grouping feature of the order parameters the two stages can be combined into
  one execution.  The parameters that would result in this type
  of processing are
  <div class="highlight-default-notranslate"><pre>
  skysub = yes               # Apply sky subtraction
  order = "TPBDFL,S"         # Sky subtract after other processing
  skies = ""                 # Use the input list
  stype = ""                 # Use all science exposures
  skymatch = ""              # Use all science exposures
  skymode = "median 10 5"    # Using 10 images near input
  imageid = "(imageid)"      # Match by IMAGEID
  filter = "(filter)"        # Match by FILTER
  sortval = "(@'mjd-obs')"   # Sort by MJD-OBS
  </pre></div>
  </dd>
  </dl>
  <dl id="l_REPLACE">
  <dt><b>REPLACE (R)</b></dt>
  <!-- Sec='STANDARD PROCESSING OPERATIONS' Level=0 Label='REPLACE' Line='REPLACE (R)' -->
  <dd>The replace operation provides a general expression, given by the
  <a href="#l_repexpr"><i>repexpr</i></A>
  parameter, that can be used for
  a variety of purposes.  As its name implies, it is intented for replacing
  input pixels with some characteristic, say saturated, by some other value
  such as a limit or special value.  Typically the expression would only
  modify a subset of the input pixels.  This is accomplished using the
  conditional expression where one branch is the unmodified value $I and
  the other is the modified value.  As an example, suppose there is a
  keyword defining saturation and we want to replace all values above
  the saturation by the saturation threshold.  The expression would be
  <div class="highlight-default-notranslate"><pre>
  repexpr = "($I&gt;saturate ? saturate : $I)"
  </pre></div>
  An image can be used to provide one or more numeric values for each
  pixel.  This image is specified by the 
  <a href="#l_repimage"><i>repimage</i></A>
  parameter and
  referenced in an expression using $R, $R1, $R2, etc.
  Note that another image that might be referenced is the input bad pixel
  mask with $M.  So if instead of using the 
  <a href="#l_fixpix"><i>fixpix</i></A>
  operation to
  interpolate across bad pixels one could replace bad pixels by some
  value. In the following example bad pixels are replaced by the value
  of a BAD keyword.
  <div class="highlight-default-notranslate"><pre>
  repexpr = "($M &gt; 0 ? blank : $I)"
  </pre></div>
  </dd>
  </dl>
  <dl id="l_NORMALIZE">
  <dt><b>NORMALIZE (N)</b></dt>
  <!-- Sec='STANDARD PROCESSING OPERATIONS' Level=0 Label='NORMALIZE' Line='NORMALIZE (N)' -->
  <dd>The normalize operation provides a predefined expression for normalizing
  an input image.  This is typically used for creating normalized flat fields
  using the PROCMEAN keyword computed by this task (see
  <a href="#s_keywords">KEYWORDS</A>
  ).
  Because the PROCMEAN keyword is not defined until after all the pixels
  have been processed during the first <span style="font-family: monospace;">"group"</span> of operations in the
  order definition, the normalize operation based on PROCMEAN is specified
  in a second group of operations.
  The default normalize operation defined by the task and in the default
  operation database is <span style="font-family: monospace;">"(max(0.1,$I/procmean))"</span>.  To apply this
  operation when processing a flat field the following parameters would
  be used and appropriately set.
  <div class="highlight-default-notranslate"><pre>
  normalize = yes
  forder = "TPBDL,N"
  </pre></div>
  In this example the flat field would be processed for the various options
  in the forder parameter before the comma.  The PROCMEAN keyword would be
  set over the pixels values from the first group operations.  Then a
  second pass is made over the data to divide each pixel by the PROCMEAN
  value except that normalized values below 10% would be set to 0.1.
  </section>
  <section id="s_keywords">
  <h3>Keywords</h3>
  This task can be highly header driven using keyword expressions for all
  calibration images and parameters.
  On output any DETSEC, CCDSEC, BIASSEC, and TRIMSEC keywords are removed
  when the trim operation is performed.  The keywords NEXTEND, PROCMEAN,
  PROCAVG, PROCSIG, PROCnnnn, and PROCDONE are added or modified.
  For flat field images, during the first group of order operations, the average and
  sigma of the output pixels is computed.  The computation excludes pixels
  with non-zero bad pixel mask values.
  The average and sigma are recorded in the
  output image header under the keywords PROCAVG and PROCSIG.  For MEF
  input files that then produce output MEF files, a global average over
  all the extensions is computed and recorded under the keyword PROCMEAN
  and the number of extensions is recorded under the NEXTEND keyword.
  Time stamped processing information providing the operation expression
  and operands is recorded under a sequence of PROCxxxx keywords.
  The set of operations performed, using the same syntax of a concatenation
  of operation codes, is recorded under the keyword
  PROCDONE.  The latter is used to identify previous processing when
  output files are operated on by this task as input files.  The
  <a href="#l_override"><i>override</i></A>
  is required to repeat an operation already found in the
  PROCDONE keyword.  New operations are appended to the keyword with a
  comma delimiter.
  The figure below shows typical output for an image in an MEF mosaic
  where the first two keywords are in the global header and the rest
  are in the extension header.
  <div class="highlight-default-notranslate"><pre>
  NEXTEND =                    4
  PROCMEAN=             1442.294
  PROC0001= 'Feb 28  9:08 Trim $I'
  PROC0002= 'Feb 28  9:08 trimsec = [2:2047,2:2047]'
  PROC0003= 'Feb 28  9:08 Fixpix $I'
  PROC0004= 'Feb 28  9:08 $M = CALDIR$bpm0702[im1]'
  PROC0005= 'Feb 28  9:08 dark calibration = ($I-$D)'
  PROC0006= 'Feb 28  9:08 $D = Drk120[im1]'
  PROC0007= 'Feb 28  9:08 flat calibration = ($I/$F)'
  PROC0008= 'Feb 28  9:08 $F = SFH2[im1]'
  PROCDONE= 'TPDF    '
  PROCAVG =              1493.96
  PROCSIG =             110.5403
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <a href="procexpr">procexpr</A>
  <a href="ccdred.ccdproc">ccdred.ccdproc</A>
  <a href="mscred.ccdproc">mscred.ccdproc</A>
  <a href="quadred.ccdproc">quadred.ccdproc</A>
  <a href="fixpix">fixpix</A>
  <a href="icfit">icfit</A>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE   ' 'PARAMETERS' 'DESCRIPTION' 'PROCESSING' 'OPERATION EXPRESSIONS AND THE OPERATION DATABASE' 'EXPRESSION OPERANDS' 'STANDARD PROCESSING OPERATIONS' 'KEYWORDS' 'SEE ALSO'  -->
  

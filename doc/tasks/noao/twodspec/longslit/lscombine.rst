.. _lscombine:

lscombine: Combine longslit images
==================================

**Package: longslit**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  lscombine input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input two-dimensional images to combine.  This task is typically
  used with dispersion calibrated longslit images though it will work with
  any 2D images.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output combined image.
  </dd>
  </dl>
  <dl id="l_headers">
  <dt><b>headers = <span style="font-family: monospace;">""</span> (optional)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='headers' Line='headers = "" (optional)' -->
  <dd>Optional output multiextension FITS file where each extension is a dataless
  headers from each input image.
  </dd>
  </dl>
  <dl id="l_bpmasks">
  <dt><b>bpmasks = <span style="font-family: monospace;">""</span> (optional)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bpmasks' Line='bpmasks = "" (optional)' -->
  <dd>Optional output bad pixel mask with good values of 0 and bad values of 1.
  Output pixels are marked as bad when no input pixels contributed to the
  output pixel.  The file name is also added to the output image header under
  the keyword BPM.
  </dd>
  </dl>
  <dl id="l_rejmask">
  <dt><b>rejmask = <span style="font-family: monospace;">""</span> (optional)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rejmask' Line='rejmask = "" (optional)' -->
  <dd>Optional output mask file identifying rejected or excluded pixels.  The
  pixel mask is the size of the output image but there is one extra dimension
  with length equal to the number of input images.  Each element of the
  highest dimension is a mask corresponding to an input image with values of
  1 for rejected or excluded pixels and values of 0 for pixels which were
  used.  The order of the masks is the order of the input images and image
  header keywords, indexed by the pixel coordinate of the highest dimension
  identify the input images.  Note that the pixel positions are in the output
  pixel coordinate system.
  </dd>
  </dl>
  <dl id="l_nrejmasks">
  <dt><b>nrejmasks = <span style="font-family: monospace;">""</span> (optional)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nrejmasks' Line='nrejmasks = "" (optional)' -->
  <dd>Optional output pixel mask giving the number of input pixels rejected or
  excluded from the input images.
  </dd>
  </dl>
  <dl id="l_expmasks">
  <dt><b>expmasks = <span style="font-family: monospace;">""</span> (optional)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expmasks' Line='expmasks = "" (optional)' -->
  <dd>Optional output exposure mask giving the sum of the exposure values of
  the input images with non-zero weights that contributed to that pixel.
  Since masks are integer, the exposure values may be scaled to preserve
  dynamic range and fractional significance.  The scaling values are given in
  the header under the keywords MASKSCAL and MASKZERO.  Exposure values are
  computed from the mask values by scale * value + zero where scale is the
  value of the MASKSCAL keyword and zero is the value of the MASKZERO
  keyword.
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma = <span style="font-family: monospace;">""</span> (optional)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma' Line='sigma = "" (optional)' -->
  <dd>Optional output sigma image.  The sigma is the standard deviation,
  corrected for a finite population, of the input pixel values (excluding
  rejected pixels) about the output combined pixel values.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"STDOUT"</span> (optional)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "STDOUT" (optional)' -->
  <dd>Optional output log file.  If no file is specified then no log information is
  produced.  The special filename <span style="font-family: monospace;">"STDOUT"</span> prints log information to the
  terminal.
  </dd>
  </dl>
  <dl id="l_interptype">
  <dt><b>interptype = <span style="font-family: monospace;">"spline3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interptype' Line='interptype = "spline3"' -->
  <dd>Image interpolation type for any resampling prior to combining.
  The allowed types are <span style="font-family: monospace;">"nearest"</span> (nearest neighbor), <span style="font-family: monospace;">"linear"</span> (bilinear),
  <span style="font-family: monospace;">"poly3"</span> (bicubic polynomial), <span style="font-family: monospace;">"poly5"</span> (biquintic polynomial), and <span style="font-family: monospace;">"spline3"</span>
  (bicubic polynomial).
  </dd>
  </dl>
  <dl id="l_x1">
  <dt><b>x1 = INDEF, y1 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='x1' Line='x1 = INDEF, y1 = INDEF' -->
  <dd>User coordinates of the first output column and line.  If INDEF then it
  is based on the smallest value over all the images.
  </dd>
  </dl>
  <dl id="l_x2">
  <dt><b>x2 = INDEF, y2 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='x2' Line='x2 = INDEF, y2 = INDEF' -->
  <dd>User coordinates of the last output column and line.  If INDEF then it
  is based on the largest value over all the images.
  </dd>
  </dl>
  <dl id="l_dx">
  <dt><b>dx = INDEF, dy = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dx' Line='dx = INDEF, dy = INDEF' -->
  <dd>User coordinate pixel interval of the output.  If INDEF then the it
  is based on smallest interval (i.e. highest dispersion) over all the images.
  </dd>
  </dl>
  <dl id="l_nx">
  <dt><b>nx = INDEF, ny = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nx' Line='nx = INDEF, ny = INDEF' -->
  <dd>Number of output pixels.  If INDEF then it is based on the values of the
  other coordinate parameters.
  </dd>
  </dl>
  <dl id="l_combine">
  <dt><b>combine = <span style="font-family: monospace;">"average"</span> (average|median|sum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='combine' Line='combine = "average" (average|median|sum)' -->
  <dd>Type of combining operation performed on the final set of pixels (after
  offsetting, masking, thresholding, and rejection).  The choices are
  <span style="font-family: monospace;">"average"</span>, <span style="font-family: monospace;">"median"</span>, or <span style="font-family: monospace;">"sum"</span>.  The median uses the average of the two central
  values when the number of pixels is even.  For the average and sum, the
  pixel values are multiplied by the weights (1 if no weighting is used)
  and summed.  The average is computed by dividing by the sum of the weights.
  If the sum of the weights is zero then the unweighted average is used.
  </dd>
  </dl>
  <dl id="l_reject">
  <dt><b>reject = <span style="font-family: monospace;">"none"</span> (none|minmax|ccdclip|crreject|sigclip|avsigclip|pclip)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reject' Line='reject = "none" (none|minmax|ccdclip|crreject|sigclip|avsigclip|pclip)' -->
  <dd>Type of rejection operation performed on the pixels remaining after offsetting,
  masking and thresholding.  The algorithms are described in the
  DESCRIPTION section.  The rejection choices are:
  <div class="highlight-default-notranslate"><pre>
       none - No rejection
     minmax - Reject the nlow and nhigh pixels
    ccdclip - Reject pixels using CCD noise parameters
   crreject - Reject only positive pixels using CCD noise parameters
    sigclip - Reject pixels using a sigma clipping algorithm
  avsigclip - Reject pixels using an averaged sigma clipping algorithm
      pclip - Reject pixels using sigma based on percentiles
  </pre></div>
  </dd>
  </dl>
  <dl id="l_outtype">
  <dt><b>outtype = <span style="font-family: monospace;">"real"</span> (none|short|ushort|integer|long|real|double)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtype' Line='outtype = "real" (none|short|ushort|integer|long|real|double)' -->
  <dd>Output image pixel datatype.  The pixel datatypes are <span style="font-family: monospace;">"double"</span>, <span style="font-family: monospace;">"real"</span>,
  <span style="font-family: monospace;">"long"</span>, <span style="font-family: monospace;">"integer"</span>, unsigned short <span style="font-family: monospace;">"ushort"</span>, and <span style="font-family: monospace;">"short"</span> with highest
  precedence first.  If <span style="font-family: monospace;">"none"</span> is specified then the highest precedence
  datatype of the input images is used.  When there is a mixture of
  short and unsigned short images the highest precedence become integer.
  The datatypes may be abbreviated to a single character.
  </dd>
  </dl>
  <dl id="l_outlimits">
  <dt><b>outlimits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outlimits' Line='outlimits = ""' -->
  <dd>Output region limits in pixels specified as pairs of whitespace separated
  values.  The first two numbers are the limits along the first output image
  dimension, the next two numbers are the limits along the second dimension,
  and so on.  If the higher dimension limits are not specified they default
  to the full range.  Therefore, if no limits are specified then the full
  output is created.  Note that the output size is computed from all the
  input images including offsets if specified and the coordinates are
  relative to that size.
  </dd>
  </dl>
  <dl id="l_masktype">
  <dt><b>masktype = <span style="font-family: monospace;">"none"</span> (none|goodvalue)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='masktype' Line='masktype = "none" (none|goodvalue)' -->
  <dd>Type of pixel masking to use.  If <span style="font-family: monospace;">"none"</span> then no pixel masking is done
  even if an image has an associated  pixel mask.  Otherwise the
  value <span style="font-family: monospace;">"goodvalue"</span> will use any mask specified for the image under
  the BPM keyword.  The values of the mask will be interpreted as
  zero for good pixels and non-zero for bad pixels.  The mask pixels
  are assumed to be registered with the image pixels.
  </dd>
  </dl>
  <dl id="l_blank">
  <dt><b>blank = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blank' Line='blank = 0.' -->
  <dd>Output value to be used when there are no pixels.
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = <span style="font-family: monospace;">"none"</span> (none|mode|median|mean|exposure|@&lt;file&gt;|!&lt;keyword&gt;)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = "none" (none|mode|median|mean|exposure|@&lt;file&gt;|!&lt;keyword&gt;)' -->
  <dd>Multiplicative image scaling to be applied.  The choices are none, multiply
  by the reciprocal of the mode, median, or mean of the specified statistics
  section, multiply by the reciprocal of the exposure time in the image header,
  multiply by the values in a specified file, or multiply by a specified
  image header keyword.  When specified in a file the scales must be one per
  line in the order of the input images.
  </dd>
  </dl>
  <dl id="l_zero">
  <dt><b>zero = <span style="font-family: monospace;">"none"</span> (none|mode|median|mean|@&lt;file&gt;|!&lt;keyword&gt;)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zero' Line='zero = "none" (none|mode|median|mean|@&lt;file&gt;|!&lt;keyword&gt;)' -->
  <dd>Additive zero level image shifts to be applied.  The choices are none, add
  the negative of the mode, median, or mean of the specified statistics
  section, add the values given in a file, or add the values given by an
  image header keyword.  When specified in a file the zero values must be one
  per line in the order of the input images.  File or keyword zero offset
  values do not allow a correction to the weights.
  </dd>
  </dl>
  <dl id="l_weight">
  <dt><b>weight = <span style="font-family: monospace;">"none"</span> (none|mode|median|mean|exposure|@&lt;file&gt;|!&lt;keyword&gt;)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='weight' Line='weight = "none" (none|mode|median|mean|exposure|@&lt;file&gt;|!&lt;keyword&gt;)' -->
  <dd>Weights to be applied during the final averaging.  The choices are none,
  the mode, median, or mean of the specified statistics section, the exposure
  time, values given in a file, or values given by an image header keyword.
  When specified in a file the weights must be one per line in the order of
  the input images and the only adjustment made by the task is for the number of
  images previously combined.   In this case the weights should be those
  appropriate for the scaled images which would normally be the inverse
  of the variance in the scaled image.
  </dd>
  </dl>
  <dl id="l_statsec">
  <dt><b>statsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='statsec' Line='statsec = ""' -->
  <dd>Section of images to use in computing image statistics for scaling and
  weighting.  If no section is given then the entire region of the input is
  sampled (for efficiency the images are sampled if they are big enough).
  When the images are offset relative to each other one can precede the image
  section with one of the modifiers <span style="font-family: monospace;">"input"</span>, <span style="font-family: monospace;">"output"</span>, <span style="font-family: monospace;">"overlap"</span>.  The first
  interprets the section relative to the input image (which is equivalent to
  not specifying a modifier), the second interprets the section relative to
  the output image, and the last selects the common overlap and any following
  section is ignored.
  </dd>
  </dl>
  <dl>
  <dt><b> expname = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line=' expname = ""' -->
  <dd>Image header keyword to be used with the exposure scaling and weighting
  options.  Also if an exposure keyword is specified that keyword will be
  added to the output image using a weighted average of the input exposure
  values.
  </dd>
  </dl>
  <p style="text-align:center">Algorithm Parameters
  
  </p>
  <dl id="l_lthreshold">
  <dt><b>lthreshold = INDEF, hthreshold = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lthreshold' Line='lthreshold = INDEF, hthreshold = INDEF' -->
  <dd>Low and high thresholds to be applied to the input pixels.  This is done
  before any scaling, rejection, and combining.  If INDEF the thresholds
  are not used.
  </dd>
  </dl>
  <dl id="l_nlow">
  <dt><b>nlow = 1,  nhigh = 1 (minmax)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlow' Line='nlow = 1,  nhigh = 1 (minmax)' -->
  <dd>The number of low and high pixels to be rejected by the <span style="font-family: monospace;">"minmax"</span> algorithm.
  These numbers are converted to fractions of the total number of input images
  so that if no rejections have taken place the specified number of pixels
  are rejected while if pixels have been rejected by masking, thresholding,
  or nonoverlap, then the fraction of the remaining pixels, truncated
  to an integer, is used.
  </dd>
  </dl>
  <dl id="l_nkeep">
  <dt><b>nkeep = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nkeep' Line='nkeep = 1' -->
  <dd>The minimum number of pixels to retain or the maximum number to reject
  when using the clipping algorithms (ccdclip, crreject, sigclip,
  avsigclip, or pclip).  When given as a positive value this is the minimum
  number to keep.  When given as a negative value the absolute value is
  the maximum number to reject.  The latter is in addition to pixels
  missing due to non-overlapping offsets, bad pixel masks, or thresholds.
  </dd>
  </dl>
  <dl id="l_mclip">
  <dt><b>mclip = yes (ccdclip, crreject, sigclip, avsigcliip)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mclip' Line='mclip = yes (ccdclip, crreject, sigclip, avsigcliip)' -->
  <dd>Use the median as the estimate for the true intensity rather than the
  average with high and low values excluded in the <span style="font-family: monospace;">"ccdclip"</span>, <span style="font-family: monospace;">"crreject"</span>,
  <span style="font-family: monospace;">"sigclip"</span>, and <span style="font-family: monospace;">"avsigclip"</span> algorithms?  The median is a better estimator
  in the presence of data which one wants to reject than the average.
  However, computing the median is slower than the average.
  </dd>
  </dl>
  <dl id="l_lsigma">
  <dt><b>lsigma = 3., hsigma = 3. (ccdclip, crreject, sigclip, avsigclip, pclip)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lsigma' Line='lsigma = 3., hsigma = 3. (ccdclip, crreject, sigclip, avsigclip, pclip)' -->
  <dd>Low and high sigma clipping factors for the <span style="font-family: monospace;">"ccdclip"</span>, <span style="font-family: monospace;">"crreject"</span>, <span style="font-family: monospace;">"sigclip"</span>,
  <span style="font-family: monospace;">"avsigclip"</span>, and <span style="font-family: monospace;">"pclip"</span> algorithms.  They multiply a <span style="font-family: monospace;">"sigma"</span> factor
  produced by the algorithm to select a point below and above the average or
  median value for rejecting pixels.  The lower sigma is ignored for the
  <span style="font-family: monospace;">"crreject"</span> algorithm.
  </dd>
  </dl>
  <dl id="l_rdnoise">
  <dt><b>rdnoise = <span style="font-family: monospace;">"0."</span>, gain = <span style="font-family: monospace;">"1."</span>, snoise = <span style="font-family: monospace;">"0."</span> (ccdclip, crreject)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rdnoise' Line='rdnoise = "0.", gain = "1.", snoise = "0." (ccdclip, crreject)' -->
  <dd>CCD readout noise in electrons, gain in electrons/DN, and sensitivity noise
  as a fraction.  These parameters are used with the <span style="font-family: monospace;">"ccdclip"</span> and <span style="font-family: monospace;">"crreject"</span>
  algorithms.  The values may be either numeric or an image header keyword
  which contains the value.  The noise model for a pixel is:
  <div class="highlight-default-notranslate"><pre>
  variance in DN = (rdnoise/gain)^2 + DN/gain + (snoise*DN)^2
  variance in e- = (rdnoise)^2 + (gain*DN) + (snoise*(gain*DN))^2
                 = rdnoise^2 + Ne + (snoise * Ne)^2
  </pre></div>
  where DN is the data number and Ne is the number of electrons.  Sensitivity
  noise typically comes from noise introduced during flat fielding.
  </dd>
  </dl>
  <dl id="l_sigscale">
  <dt><b>sigscale = 0.1 (ccdclip, crreject, sigclip, avsigclip)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigscale' Line='sigscale = 0.1 (ccdclip, crreject, sigclip, avsigclip)' -->
  <dd>This parameter determines when poisson corrections are made to the
  computation of a sigma for images with different scale factors.  If all
  relative scales are within this value of unity and all relative zero level
  offsets are within this fraction of the mean then no correction is made.
  The idea is that if the images are all similarly though not identically
  scaled, the extra computations involved in making poisson corrections for
  variations in the sigmas can be skipped.  A value of zero will apply the
  corrections except in the case of equal images and a large value can be
  used if the sigmas of pixels in the images are independent of scale and
  zero level.
  </dd>
  </dl>
  <dl id="l_pclip">
  <dt><b>pclip = -0.5 (pclip)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pclip' Line='pclip = -0.5 (pclip)' -->
  <dd>Percentile clipping algorithm parameter.  If greater than
  one in absolute value then it specifies a number of pixels above or
  below the median to use for computing the clipping sigma.  If less
  than one in absolute value then it specifies the fraction of the pixels
  above or below the median to use.  A positive value selects a point
  above the median and a negative value selects a point below the median.
  The default of -0.5 selects approximately the quartile point.
  </dd>
  </dl>
  <dl id="l_grow">
  <dt><b>grow = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grow' Line='grow = 0.' -->
  <dd>Radius in pixels for additional pixel to be rejected in an image with a
  rejected pixel from one of the rejection algorithms.  This applies only to
  pixels rejected by one of the rejection algorithms and not the masked or
  threshold rejected pixels.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>LSCOMBINE</b> combines two-dimensional longslit images by first
  resampling them to a common world coordinate system, if not already on
  the same system, and then combining the matching pixels.  The final world
  coordinate system is specified by parameters or by looking at the maximum
  ranges and minimum intervals over the input data.
  </p>
  <p>
  Algorithmically it is a combination of the tasks <b>TRANSFORM</b> (using
  the WCS) and <b>IMCOMBINE</b>.  When executing it will generate temporary
  images (<span style="font-family: monospace;">"lsc*"</span>) and masks (<span style="font-family: monospace;">"mlsc*"</span>) if the images are not already on a
  common world coordinate system.  The user only need be aware of this
  in case of an unexpected abort leaving these files behind.
  </p>
  <p>
  Rather than repeat the details the user should consult the descriptions
  for <b>TRANSFORM</b> and <b>IMCOMBINE</b> ignoring parameters which are
  not part of this task.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lscombine obj* lscomb
  </pre></div>
  </section>
  <section id="s_notes">
  <h3>Notes</h3>
  <dl id="l_LSCOMBINE">
  <dt><b>LSCOMBINE: V2.12.3</b></dt>
  <!-- Sec='NOTES' Level=0 Label='LSCOMBINE' Line='LSCOMBINE: V2.12.3' -->
  <dd>This is a new task in this relese.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  transform, imcombine. odcombine 
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'NOTES' 'SEE ALSO'  -->
  

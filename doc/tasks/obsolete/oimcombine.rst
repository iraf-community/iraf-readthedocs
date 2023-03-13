.. _oimcombine:

oimcombine: IMCOMBINE from V2.11-V2.11.3
========================================

**Package: obsolete**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  oimcombine input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images to combine.  All images must have the same dimensionality
  but they may be of different sizes.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output combined image or list of images.  If the <i>project</i> parameter is
  no then there will be one output image while if it is yes there will be one
  output image for each input image.
  </dd>
  </dl>
  <dl id="l_rejmask">
  <dt><b>rejmask = <span style="font-family: monospace;">""</span> (optional)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rejmask' Line='rejmask = "" (optional)' -->
  <dd>Output mask file to contain identifications of which pixels in which input
  images were rejected or excluded.  The pixel mask will be the size of the
  output image and identified pixels will be in the output image pixel
  coordinate system.  There is on extra dimension with length equal to the
  number of input images.  Each element of this dimension contains the mask
  of the input image.  The order is the order of the input images.
  </dd>
  </dl>
  <dl id="l_plfile">
  <dt><b>plfile = <span style="font-family: monospace;">""</span> (optional)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plfile' Line='plfile = "" (optional)' -->
  <dd>Output pixel list file or list of files.  If no name is given or the
  list ends prematurely then no file is produced.  The pixel list file
  is a map of the number of pixels rejected or, equivalently,
  the total number of input images minus the number of pixels actually used.
  The file name is also added to the output image header under the
  keyword BPM.
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma = <span style="font-family: monospace;">""</span> (optional)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma' Line='sigma = "" (optional)' -->
  <dd>Output sigma image or list of images.  If no name is given or the list ends
  prematurely then no image is produced.  The sigma is standard deviation,
  corrected for a finite population, of the input pixel values (excluding
  rejected pixels) about the output combined pixel values.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"STDOUT"</span> (optional)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "STDOUT" (optional)' -->
  <dd>Output log file.  If no file is specified then no log information is produced.
  The special filename <span style="font-family: monospace;">"STDOUT"</span> prints log information to the terminal.
  </dd>
  </dl>
  <dl id="l_combine">
  <dt><b>combine = <span style="font-family: monospace;">"average"</span> (average|median)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='combine' Line='combine = "average" (average|median)' -->
  <dd>Type of combining operation performed on the final set of pixels (after
  offsetting, masking, thresholding, and rejection).  The choices are
  <span style="font-family: monospace;">"average"</span> or <span style="font-family: monospace;">"median"</span>.  The median uses the average of the two central
  values when the number of pixels is even.
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
  <dl id="l_project">
  <dt><b>project = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='project' Line='project = no' -->
  <dd>Project (combine) across the highest dimension of the input images?  If
  no then all  the input images are combined to a single output image.  If
  yes then the highest dimension elements of each input image are combined to
  an output image and optional pixel list and sigma images.  Each element of
  the highest dimension may have a separate offset but there can only be one
  mask image.
  </dd>
  </dl>
  <dl id="l_outtype">
  <dt><b>outtype = <span style="font-family: monospace;">"real"</span> (short|ushort|integer|long|real|double)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtype' Line='outtype = "real" (short|ushort|integer|long|real|double)' -->
  <dd>Output image pixel datatype.  The pixel datatypes are <span style="font-family: monospace;">"double"</span>, <span style="font-family: monospace;">"real"</span>,
  <span style="font-family: monospace;">"long"</span>, <span style="font-family: monospace;">"integer"</span>, unsigned short <span style="font-family: monospace;">"ushort"</span>, and <span style="font-family: monospace;">"short"</span> with highest
  precedence first.  If none is specified then the highest precedence
  datatype of the input images is used.  When there is a mixture of
  short and unsigned short images the highest precedence become integer.
  The datatypes may be abbreviated to
  a single character.
  </dd>
  </dl>
  <dl id="l_offsets">
  <dt><b>offsets = <span style="font-family: monospace;">"none"</span> (none|wcs|grid|&lt;filename&gt;)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='offsets' Line='offsets = "none" (none|wcs|grid|&lt;filename&gt;)' -->
  <dd>Integer offsets to add to each image axes.  The options are:
  <dl>
  <dt><b><span style="font-family: monospace;">"none"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"none"' -->
  <dd>No offsets are applied.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"wcs"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"wcs"' -->
  <dd>The world coordinate system (wcs) in the image is used to derive the
  offsets.  The nearest integer offset that matches the world coordinate
  at the center of the first input image is used.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"grid"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"grid"' -->
  <dd>A uniform grid of offsets is specified by a string of the form
  <div class="highlight-default-notranslate"><pre>
  grid [n1] [s1] [n2] [s2] ...
  </pre></div>
  where ni is the number of images in dimension i and si is the step
  in dimension i.  For example <span style="font-family: monospace;">"grid 5 100 5 100"</span> specifies a 5x5
  grid with origins offset by 100 pixels.
  </dd>
  </dl>
  <dl>
  <dt><b>&lt;filename&gt;</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='&lt;filename&gt;' -->
  <dd>The offsets are given in the specified file.  The file consists
  of one line per image with the offsets in each dimension forming the
  columns.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_masktype">
  <dt><b>masktype = <span style="font-family: monospace;">"none"</span> (none|goodvalue|badvalue|goodbits|badbits)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='masktype' Line='masktype = "none" (none|goodvalue|badvalue|goodbits|badbits)' -->
  <dd>Type of pixel masking to use.  If <span style="font-family: monospace;">"none"</span> then no pixel masking is done
  even if an image has an associated  pixel mask.  The other choices
  are to select the value in the pixel mask to be treated as good
  (goodvalue) or bad (badvalue) or the bits (specified as a value)
  to be treated as good (goodbits) or bad (badbits).  The pixel mask
  file name comes from the image header keyword BPM.  Note that when
  combining images by projection of the highest dimension only one
  pixel mask is applied to all the images.  <b>Note</b>, if the number of
  input images becomes too large (currently about 250 .imh or 125 .hhh
  images) then the images are temporarily stacked and combined by projection
  which also means the bad pixel mask from the first image will be used
  for all images.
  </dd>
  </dl>
  <dl id="l_maskvalue">
  <dt><b>maskvalue = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maskvalue' Line='maskvalue = 0' -->
  <dd>Mask value used with the <i>masktype</i> parameter.  If the mask type
  selects good or bad bits the value may be specified using IRAF notation
  for decimal, octal, or hexadecimal; i.e 12, 14b, 0cx to select bits 3
  and 4.
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
  See the DESCRIPTION section for further details.
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
  A set of images or the highest dimension elements (for example the planes
  in an image cube) are combined by weighted averaging or medianing.  Pixels
  may be rejected from the combining by using pixel masks, threshold levels,
  and rejection algorithms.  The images may be scaled multiplicatively or
  additively based on image statistics, image header keywords, or text files
  before rejection.  The images may be combined with integer pixel coordinate
  offsets, possibly determined using the world coordinate system of the
  images, to produce an image bigger than any of the input images.
  </p>
  <p>
  The input images to be combined are specified by a list.  If the
  <b>project</b> parameter is yes then the highest dimension elements of each
  input image are combined to make an output image of one lower dimension.
  There is no limit to the number of elements combined in this case.  If
  <b>project</b> is no then the entire input list is combined to form a single
  output image.   In this case the images must all have the same
  dimensionality but they may have different sizes.  There is a software
  limit of approximately 100 images in this case.
  </p>
  <p>
  The output image header is a copy of the first image in the combined set.
  In addition, the number of  images combined is recorded under the keyword
  NCOMBINE, an image header keyword selected by the <i>expname</i> parameters
  (which is usually an exposure time) is updated as the weighted average of
  the input header keywords, and any pixel list file created is recorded
  under the keyword BPM.  The output pixel type is set by the parameter
  <i>outtype</i>.  If left blank then the input datatype of highest precision
  is used.  If there is a mixture of short and unsigned short images then
  the highest precision is integer.
  </p>
  <p>
  In addition to one or more output combined images there are some optional
  output files which may be specified.  A pixel mask identifying each pixel
  rejected or excluded may be created.  This mask will match the output
  image in size except there is one extra dimension.  The extra dimension
  indexes the input images in the order in which they are specified and
  combined.  What this means is that each element of the extra dimension
  is a mask of the pixel rejected in a particular input image (or lower
  dimensional element in the case of projection) but in the offset and
  sized to the output image.  For example, if the input consists of
  two dimensional images then the rejected pixel mask will be three
  dimensional and each plane will be for a particular input image.
  If one wants to separate this file the task <b>imslice</b> may be used.
  If there are no offsets then the masks will also be registered with the
  input image.  If there are offsets then the masks will be offset
  also.
  </p>
  <p>
  Another pixel mask may be produced giving just the total number of pixels
  rejected at each output pixel.  An image containing the sigmas of the
  pixels combined about the final output combined pixels may also be
  created.  The sigma computation is the standard deviation corrected for a
  finite population (the n/(n-1) factor) including weights if a weighted
  average is used.  Finally a log file may be produced.
  </p>
  <p>
  An outline of the steps taken by the program is given below and the
  following sections elaborate on the steps.
  </p>
  <div class="highlight-default-notranslate"><pre>
  o   Set the input image offsets and the final output image size.
  o   Set the input image scales and weights
  o   Write the log file output
  </pre></div>
  <p>
  For each output image line:
  </p>
  <div class="highlight-default-notranslate"><pre>
  o   Get input image lines that overlap the output image line
  o   Reject masked pixels
  o   Reject pixels outside the threshold limits
  o   Reject pixels using the specified algorithm
  o   Reject neighboring pixels along each line
  o   Combine remaining pixels using the weighted average or median
  o   Compute sigmas of remaining pixels about the combined values
  o   Write the output image line, rejected pixel masks, and sigmas
  </pre></div>
  <p>
  OFFSETS
  </p>
  <p>
  The images to be combined need not be of the same size or overlap.  They
  do have to have the same dimensionality which will also be the dimensionality
  of the output image.  Any dimensional images supported by IRAF may be
  used.  Note that if the <i>project</i> flag is yes then the input images
  are the elements of the highest dimension; for example the planes of a
  three dimensional image.
  </p>
  <p>
  The overlap of the images is determined by a set of integer pixel offsets
  with an offset for each dimension of each input image.  For example
  offsets of 0, 10, and 20 in the first dimension of three images will
  result in combining the three images with only the first image in the
  first 10 columns, the first two images in the next 10 columns and
  all three images starting in the 21st column.  At the 21st output column
  the 21st column of the first image will be combined with the 11th column
  of the second image and the 1st column of the third image.
  </p>
  <p>
  The output image size is set by the maximum extent in each dimension
  of any input image after applying the offsets.  In the above example if
  all the images have 100 columns then the output image will have 120
  columns corresponding to the 20 column offset in the third image.
  </p>
  <p>
  The input image offsets are set using the <i>offset</i> parameter.  There
  are four ways to specify the offsets.  If the word <span style="font-family: monospace;">"none"</span> or the empty
  string <span style="font-family: monospace;">""</span> are used then all offsets will be zero and all pixels with the
  same coordinates will be combined.  The output image size will be equal to
  the biggest dimensions of the input images.
  </p>
  <p>
  If <span style="font-family: monospace;">"wcs"</span> offsets are specified then the world coordinate systems (wcs)
  in the image headers are used to derived the offsets.  The world coordinate
  at the center of the first input image is evaluated.  Then integer pixel
  offsets are determined for each image to bring the same world coordinate
  to the same point.  Note the following caveats.  The world coordinate
  systems must be of the same type, orientation, and scale and only the
  nearest integer shift is used.
  </p>
  <p>
  If the input images have offsets in a regular grid or one wants to make
  an output image in which the input images are <span style="font-family: monospace;">"mosaiced"</span> together in
  a grid then the special offset string  beginning with the word <span style="font-family: monospace;">"grid"</span>
  is used.  The format is
  </p>
  <div class="highlight-default-notranslate"><pre>
  grid [n1] [s1] [n2] [s2] ...
  </pre></div>
  <p>
  where ni is the number of images in dimension i and si is the step in
  dimension i.  For example <span style="font-family: monospace;">"grid 5 100 5 100"</span> specifies a 5x5 grid with
  origins offset by 100 pixels.  Note that one must insure that the input
  images are specified in the correct order.  This may best be accomplished
  using a <span style="font-family: monospace;">"@"</span> list.  One useful application of the grid is to make a
  nonoverlapping mosaic of a number of images for display purposes.  Suppose
  there are 16 images which are 100x100.  The offset string <span style="font-family: monospace;">"grid 4 101 4
  101"</span> will produce a mosaic with a one pixel border having the value set
  by <i>blank</i> parameter between the images.
  </p>
  <p>
  The offsets may be defined in a file by specifying the file name
  in the <i>offset</i> parameter.  (Note that the special file name STDIN
  may be used to type in the values terminated by the end-of-file
  character).  The file consists of a line for each input image.  The lines
  must be in the same order as the input images and so an <span style="font-family: monospace;">"@"</span> list may
  be useful.  The lines consist of whitespace separated offsets one for
  each dimension of the images.  In the first example cited above the
  offset file might contain:
  </p>
  <div class="highlight-default-notranslate"><pre>
  0 0
  10 0
  20 0
  </pre></div>
  <p>
  where we assume the second dimension has zero offsets.
  </p>
  <p>
  The offsets need not have zero for one of the images.  The offsets may
  include negative values or refer to some arbitrary common point.
  When the offsets are read by the program it will find the minimum
  value in each dimension and subtract it from all the other offsets
  in that dimension.  The above example could also be specified as:
  </p>
  <div class="highlight-default-notranslate"><pre>
  225 15
  235 15
  245 15
  </pre></div>
  <p>
  There may be cases where one doesn't want the minimum offsets reset
  to zero.  If all the offsets are positive and the comment <span style="font-family: monospace;">"# Absolute"</span>
  appears in the offset file then the images will be combined with
  blank values between the first output pixel and the first overlapping
  input pixel.  Continuing with the above example, the file
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Absolute
  10 10
  20 10
  30 10
  </pre></div>
  <p>
  will have the first pixel of the first image in the 11th pixel of the
  output image.  Note that there is no way to <span style="font-family: monospace;">"pad"</span> the other side of
  the output image.
  </p>
  <p>
  SCALES AND WEIGHTS
  </p>
  <p>
  In order to combine images with rejection of pixels based on deviations
  from some average or median they must be scaled to a common level.  There
  are two types of scaling available, a multiplicative intensity scale and an
  additive zero point shift.  The intensity scaling is defined by the
  <i>scale</i> parameter and the zero point shift by the <i>zero</i>
  parameter.  These parameters may take the values <span style="font-family: monospace;">"none"</span> for no scaling,
  <span style="font-family: monospace;">"mode"</span>, <span style="font-family: monospace;">"median"</span>, or <span style="font-family: monospace;">"mean"</span> to scale by statistics of the image pixels,
  <span style="font-family: monospace;">"exposure"</span> (for intensity scaling only) to scale by the exposure time
  keyword in the image header, any other image header keyword specified by
  the keyword name prefixed by the character <span style="font-family: monospace;">'!'</span>, and the name of a file
  containing the scale factors for the input image prefixed by the
  character <span style="font-family: monospace;">'@'</span>.
  </p>
  <p>
  Examples of the possible parameter values are shown below where
  <span style="font-family: monospace;">"myval"</span> is the name of an image header keyword and <span style="font-family: monospace;">"scales.dat"</span> is
  a text file containing a list of scale factors.
  </p>
  <div class="highlight-default-notranslate"><pre>
  scale = none            No scaling
  zero = mean             Intensity offset by the mean
  scale = exposure        Scale by the exposure time
  zero = !myval           Intensity offset by an image keyword
  scale = @scales.dat     Scales specified in a file
  </pre></div>
  <p>
  The image statistics are computed by sampling a uniform grid of points with
  the smallest grid step that yields less than 10000 pixels; sampling is used
  to reduce the time needed to compute the statistics.  If one wants to
  restrict the sampling to a region of the image the <i>statsec</i> parameter
  is used.  This parameter has the following syntax:
  </p>
  <div class="highlight-default-notranslate"><pre>
  [input|output|overlap] [image section]
  </pre></div>
  <p>
  The initial modifier defaults to <span style="font-family: monospace;">"input"</span> if absent.  The modifiers are useful
  if the input images have offsets.  In that case <span style="font-family: monospace;">"input"</span> specifies
  that the image section refers to each input image, <span style="font-family: monospace;">"output"</span> specifies
  that the image section refers to the output image coordinates, and
  <span style="font-family: monospace;">"overlap"</span> specifies the mutually overlapping region of the input images.
  In the latter case an image section is ignored.
  </p>
  <p>
  The statistics are as indicated by their names.  In particular, the
  mode is a true mode using a bin size which is a fraction of the
  range of the pixels and is not based on a relationship between the
  mode, median, and mean.  Also masked pixels are excluded from the
  computations as well as during the rejection and combining operations.
  </p>
  <p>
  The <span style="font-family: monospace;">"exposure"</span> option in the intensity scaling uses the value of the
  image header keyword specified by the <i>expname</i> keyword.  As implied
  by the parameter name, this is typically the image exposure time since
  intensity levels are linear with the exposure time in CCD detectors.
  Note that the exposure keyword is also updated in the final image
  as the weighted average of the input values.  Thus, if one wants to
  use a nonexposure time keyword and keep the exposure time updating
  feature the image header keyword syntax is available; i.e. !&lt;keyword&gt;.
  </p>
  <p>
  Scaling values may be defined as a list of values in a text file.  The file
  name is specified by the standard @file syntax.  The list consists of one
  value per line.  The order of the list is assumed to be the same as the
  order of the input images.  It is a fatal error if the list is incomplete
  and a warning if the list appears longer than the number of input images.
  Because the scale and zero levels are adjusted only the relative
  values are important.
  </p>
  <p>
  If both an intensity scaling and zero point shift are selected the
  zero point is added first and the scaling is done.  This is
  important if the scale and offset values are specified by
  header keywords or from a file of values.  However,
  in the log output the zero values are given as the scale times
  the offset hence those numbers would be interpreted as scaling
  first and zero offset second.
  </p>
  <p>
  The image statistics and scale factors are recorded in the log file
  unless they are all equal, which is equivalent to no scaling.  The
  intensity scale factors are normalized to a unit mean and the zero
  point shifts are adjust to a zero mean.  When scale factors or
  zero point shifts are specified by the user in an @file or
  by an image header keyword no normalization is done.
  </p>
  <p>
  Scaling affects not only the mean values between images but also the
  relative pixel uncertainties.  For example scaling an image by a
  factor of 0.5 will reduce the effective noise sigma of the image
  at each pixel by the square root of 0.5.  Changes in the zero
  point also changes the noise sigma if the image noise characteristics
  are Poissonian.  In the various rejection algorithms based on
  identifying a noise sigma and clipping large deviations relative to
  the scaled median or mean, one may need to account for the scaling induced
  changes in the image noise characteristics.
  </p>
  <p>
  In those algorithms it is possible to eliminate the <span style="font-family: monospace;">"sigma correction"</span>
  while still using scaling.  The reasons this might be desirable are 1) if
  the scalings are similar the corrections in computing the mean or median
  are important but the sigma corrections may not be important and 2) the
  image statistics may not be Poissonian, either inherently or because the
  images have been processed in some way that changes the statistics.  In the
  first case because computing square roots and making corrections to every
  pixel during the iterative rejection operation may be a significant
  computational speed limit the parameter <i>sigscale</i> selects how
  dissimilar the scalings must be to require the sigma corrections.  This
  parameter is a fractional deviation which, since the scale factors are
  normalized to unity, is the actual minimum deviation in the scale factors.
  For the zero point shifts the shifts are normalized by the mean shift
  before adjusting the shifts to a zero mean.  To always use sigma scaling
  corrections the parameter is set to zero and to eliminate the correction in
  all cases it is set to a very large number.
  </p>
  <p>
  If the final combining operation is <span style="font-family: monospace;">"average"</span> then the images may be
  weighted during the averaging.  The weights are specified in the
  same way as the scale factors.  In addition
  the NCOMBINE keyword, if present, will be used in the weights.
  The weights, scaled to a unit sum, are printed in the log output.
  </p>
  <p>
  The weights are only used for the final weighted average and sigma image
  output.  They are not used to form averages in the various rejection
  algorithms.  For weights in the case of no scaling or only multiplicative
  scaling the weights are used as given or determined so that images with
  lower signal levels will have lower weights.  However, for cases in which
  zero level scaling is used and the zero levels are determined from image
  statistics (not from an input file or keyword) the weights are computed
  from the initial weights (the exposure time, image statistics, or input
  values) using the formula:
  </p>
  <div class="highlight-default-notranslate"><pre>
  weight_final = weight_initial / (scale * sky)
  </pre></div>
  <p>
  where the sky values are those from the image statistics before conversion
  to zero level shifts and adjustment to zero mean over all images.  The
  reasoning is that if the zero level is high the sky brightness is high and
  so the S/N is lower and the weight should be lower.  If any sky value
  determined from the image  statistics comes out to be negative a warning is
  given and the none of the weight are adjusted for sky levels.
  </p>
  <p>
  The weights are not adjusted when the zero offsets are input from a file
  or keyword since these values do not imply the actual image sky value.
  In this case if one wants to account for different sky statistics
  in the weights the user must specify the weights in a file taking
  explicit account of changes in the weights due to different sky
  statistics.
  </p>
  <p>
  PIXEL MASKS
  </p>
  <p>
  A pixel mask is a type of IRAF file having the extension <span style="font-family: monospace;">".pl"</span> which
  identifies an integer value with each pixel of the images to which it is
  applied.  The integer values may denote regions, a weight, a good or bad
  flag, or some other type of integer or integer bit flag.  In the common
  case where many values are the same this file is compacted to be small and
  efficient to use.  It is also most compact and efficient if the majority of
  the pixels have a zero mask value so frequently zero is the value for good
  pixels.  Note that these files, while not stored as a strict pixel array,
  may be treated as images in programs.  This means they may be created by
  programs such as <b>mkpattern</b>, edited by <b>imedit</b>, examined by
  <b>imexamine</b>, operated upon by <b>imarith</b>, graphed by <b>implot</b>,
  and displayed by <b>display</b>.
  </p>
  <p>
  At the time of introducing this task, generic tools for creating
  pixel masks have yet to be written.  There are two ways to create a
  mask in V2.10.  First if a regular integer image can be created
  then it can be converted to pixel list format with <b>imcopy</b>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imcopy template plfile.pl
  </pre></div>
  <p>
  by specifically using the .pl extension on output.  Other programs that
  can create integer images (such <b>mkpattern</b> or <b>ccdred.badpiximage</b>)
  can create the pixel list file directly by simply using the <span style="font-family: monospace;">".pl"</span>
  extension in the output image name.
  </p>
  <p>
  To use pixel masks with <b>oimcombine</b> one must associate a pixel
  mask file with an image by entering the pixel list file name in the
  image header under the keyword BPM (bad pixel mask).  This can be
  done with <b>hedit</b>.  Note that the same pixel mask may be associated
  with more than one image as might be the case if the mask represents
  defects in the detector used to obtain the images.
  </p>
  <p>
  If a pixel mask is associated with an image the mask is used when the
  <i>masktype</i> parameter is set to a value other than <span style="font-family: monospace;">"none"</span>.  Note that
  when it is set to <span style="font-family: monospace;">"none"</span> mask information is not used even if it exists for
  the image.  The values of <i>masktype</i> which apply masks are <span style="font-family: monospace;">"goodvalue"</span>,
  <span style="font-family: monospace;">"badvalue"</span>, <span style="font-family: monospace;">"goodbits"</span>, and <span style="font-family: monospace;">"badbits"</span>.  They are used in conjunction with
  the <i>maskvalue</i> parameter.  When the mask type is <span style="font-family: monospace;">"goodvalue"</span> the
  pixels with mask values matching the specified value are included in
  combining and all others are rejected.  Similarly, for a mask type of
  <span style="font-family: monospace;">"badvalue"</span> the pixels with mask values matching the specified value are
  rejected and all others are accepted.  The bit types are useful for
  selecting a combination of attributes in a mask consisting of bit flags.
  The mask value is still an integer but is interpreted by bitwise comparison
  with the values in the mask file.
  </p>
  <p>
  If a mask operation is specified and an image has no mask image associated
  with it then the mask values are taken as all zeros.  In those cases be
  careful that zero is an accepted value otherwise the entire image will be
  rejected.
  </p>
  <p>
  In the case of combining the higher dimensions of an image into a
  lower dimensional image, the <span style="font-family: monospace;">"project"</span> option, the same pixel mask
  is applied to all of the data being combined; i.e. the same 2D
  pixel mask is applied to every plane of a 3D image.  This is because
  a higher dimensional image is treated as a collection of lower
  dimensional images having the same header and hence the same
  bad pixel mask.  It would be tempting to use a bad pixel mask with
  the same dimension as the image being projected but this is not
  currently how the task works.
  </p>
  <p>
  When the number of input images exceeds the maximum number of open files
  allowed by IRAF (currently about 250 or 125 .hhh images) the input images
  are stacked and combined with the <i>project</i> option.  <b>Note</b> that
  this means that the bad pixel mask from the first input image will be
  applied to all the images.
  </p>
  <p>
  THRESHOLD REJECTION
  </p>
  <p>
  In addition to rejecting masked pixels, pixels in the unscaled input
  images which are below or above the thresholds given by the parameters
  <i>lthreshold</i> and <i>hthreshold</i> are rejected.  Values of INDEF
  mean that no threshold value is applied.  Threshold rejection may be used
  to exclude very bad pixel values or as an alternative way of masking
  images.  In the latter case one can use a task like <b>imedit</b>
  or <b>imreplace</b> to set parts of the images to be excluded to some
  very low or high magic value.
  </p>
  <p>
  REJECTION ALGORITHMS
  </p>
  <p>
  The <i>reject</i> parameter selects a type of rejection operation to
  be applied to pixels not masked or thresholded.  If no rejection
  operation is desired the value <span style="font-family: monospace;">"none"</span> is specified.
  </p>
  <p>
  MINMAX
  A specified fraction of the highest and lowest pixels are rejected.
  The fraction is specified as the number of high and low pixels, the
  <i>nhigh</i> and <i>nlow</i> parameters, when data from all the input images
  are used.  If pixels have been rejected by offsetting, masking, or
  thresholding then a matching fraction of the remaining pixels, truncated
  to an integer, are used.  Thus,
  </p>
  <div class="highlight-default-notranslate"><pre>
  nl = n * nlow/nimages + 0.001
  nh = n * nhigh/nimages + 0.001
  </pre></div>
  <p>
  where n is the number of pixels surviving offsetting, masking, and
  thresholding, nimages is the number of input images, nlow and nhigh
  are task parameters and nl and nh are the final number of low and
  high pixels rejected by the algorithm.  The factor of 0.001 is to
  adjust for rounding of the ratio.
  </p>
  <p>
  As an example with 10 input images and specifying one low and two high
  pixels to be rejected the fractions to be rejected are nlow=0.1 and nhigh=0.2
  and the number rejected as a function of n is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  n   0  1  2  3  4  5  6  7  8  9 10
  nl  0  0  0  0  0  0  0  0  0  0  1
  nh  0  0  0  0  0  1  1  1  1  1  2
  </pre></div>
  <p>
  CCDCLIP
  If the images are obtained using a CCD with known read out noise, gain, and
  sensitivity noise parameters and they have been processed to preserve the
  relation between data values and photons or electrons then the noise
  characteristics of the images are well defined.  In this model the sigma in
  data values at a pixel with true value &lt;I&gt;, as approximated by the median
  or average with the lowest and highest value excluded, is given by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sigma = ((rn / g) ** 2 + &lt;I&gt; / g + (s * &lt;I&gt;) ** 2) ** 1/2
  </pre></div>
  <p>
  where rn is the read out noise in electrons, g is the gain in
  electrons per data value, s is a sensitivity noise given as a fraction,
  and ** is the exponentiation operator.  Often the sensitivity noise,
  due to uncertainties in the pixel sensitivities (for example from the
  flat field), is not known in which case a value of zero can be used.
  See the task <b>stsdas.wfpc.noisemodel</b> for a way to determine
  these values (though that task expresses the read out noise in data
  numbers and the sensitivity noise parameter as a percentage).
  </p>
  <p>
  The read out noise is specified by the <i>rdnoise</i> parameter.  The value
  may be a numeric value to be applied to all the input images or a image
  header keyword containing the value for each image.  Similarly, the
  parameter <i>gain</i> specifies the gain as either a value or image header
  keyword and the parameter <i>snoise</i> specifies the sensitivity
  noise parameter as either a value or image header keyword.
  </p>
  <p>
  The algorithm operates on each output pixel independently.  It starts by
  taking the median or unweighted average (excluding the minimum and maximum)
  of the unrejected pixels provided there are at least two input pixels.  The
  expected sigma is computed from the CCD noise parameters and pixels more
  that <i>lsigma</i> times this sigma below or <i>hsigma</i> times this sigma
  above the median or average are rejected.  The process is then iterated
  until no further pixels are rejected.  If the average is used as the
  estimator of the true value then after the first round of rejections the
  highest and lowest values are no longer excluded.  Note that it is possible
  to reject all pixels if the average is used and is sufficiently skewed by
  bad pixels such as cosmic rays.
  </p>
  <p>
  If there are different CCD noise parameters for the input images
  (as might occur using the image header keyword specification) then
  the sigmas are computed for each pixel from each image using the
  same estimated true value.
  </p>
  <p>
  If the images are scaled and shifted and the <i>sigscale</i> threshold
  is exceedd then a sigma is computed for each pixel based on the
  image scale parameters; i.e. the median or average is scaled to that of the
  original image before computing the sigma and residuals.
  </p>
  <p>
  After rejection the number of retained pixels is checked against the
  <i>nkeep</i> parameter.  If there are fewer pixels retained than specified
  by this parameter the pixels with the smallest residuals in absolute
  value are added back.  If there is more than one pixel with the same
  absolute residual (for example the two pixels about an average
  or median of two will have the same residuals) they are all added
  back even if this means more than <i>nkeep</i> pixels are retained.
  Note that the <i>nkeep</i> parameter only applies to the pixels used
  by the clipping rejection algorithm and does not apply to threshold
  or bad pixel mask rejection.
  </p>
  <p>
  This is the best clipping algorithm to use if the CCD noise parameters are
  adequately known.  The parameters affecting this algorithm are <i>reject</i>
  to select this algorithm, <i>mclip</i> to select the median or average for
  the center of the clipping, <i>nkeep</i> to limit the number of pixels
  rejected, the CCD noise parameters <i>rdnoise, gain</i> and <i>snoise</i>,
  <i>lsigma</i> and <i>hsigma</i> to select the clipping thresholds,
  and <i>sigscale</i> to set the threshold for making corrections to the sigma
  calculation for different image scale factors.
  </p>
  <p>
  CRREJECT
  This algorithm is identical to <span style="font-family: monospace;">"ccdclip"</span> except that only pixels above
  the average are rejected based on the <i>hsigma</i> parameter.  This
  is appropriate for rejecting cosmic ray events and works even with
  two images.
  </p>
  <p>
  SIGCLIP
  The sigma clipping algorithm computes at each output pixel the median or
  average excluding the high and low values.  The sigma is then computed
  about this estimate (without excluding the low and high values).  There
  must be at least three input pixels, though for this method to work well
  there should be at least 10 pixels.  Values deviating by more than the
  specified sigma threshold factors are rejected.  These steps are repeated,
  except that after the first time the average includes all values, until no
  further pixels are rejected or there are fewer than three pixels.
  </p>
  <p>
  After rejection the number of retained pixels is checked against the
  <i>nkeep</i> parameter.  If there are fewer pixels retained than specified
  by this parameter the pixels with the smallest residuals in absolute
  value are added back.  If there is more than one pixel with the same
  absolute residual (for example the two pixels about an average
  or median of two will have the same residuals) they are all added
  back even if this means more than <i>nkeep</i> pixels are retained.
  Note that the <i>nkeep</i> parameter only applies to the pixels used
  by the clipping rejection algorithm and does not apply to threshold
  or bad pixel mask rejection.
  </p>
  <p>
  The  parameters affecting this algorithm are <i>reject</i> to select
  this algorithm, <i>mclip</i> to select the median or average for the
  center of the clipping, <i>nkeep</i> to limit the number of pixels
  rejected, <i>lsigma</i> and <i>hsigma</i> to select the
  clipping thresholds, and <i>sigscale</i> to set the threshold for
  making corrections to the sigma calculation for different image scale
  factors.
  </p>
  <p>
  AVSIGCLIP
  The averaged sigma clipping algorithm assumes that the sigma about the
  median or mean (average excluding the low and high values) is proportional
  to the square root of the median or mean at each point.  This is
  described by the equation:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sigma(column,line) = sqrt (gain(line) * signal(column,line))
  </pre></div>
  <p>
  where the <i>estimated</i> signal is the mean or median (hopefully excluding
  any bad pixels) and the gain is the <i>estimated</i> proportionality
  constant having units of photons/data number.
  </p>
  <p>
  This noise model is valid for images whose values are proportional to the
  number of photons recorded.  In effect this algorithm estimates a
  detector gain for each line with no read out noise component when
  information about the detector noise parameters are not known or
  available.  The gain proportionality factor is computed
  independently for each output line by averaging the square of the residuals
  (at points having three or more input values) scaled by the median or
  mean.  In theory the proportionality should be the same for all rows but
  because of the estimating process will vary somewhat.
  </p>
  <p>
  Once the proportionality factor is determined, deviant pixels exceeding the
  specified thresholds are rejected at each point by estimating the sigma
  from the median or mean.  If any values are rejected the median or mean
  (this time not excluding the extreme values) is recomputed and further
  values rejected.  This is repeated until there are no further pixels
  rejected or the number of remaining input values falls below three.  Note
  that the proportionality factor is not recomputed after rejections.
  </p>
  <p>
  If the images are scaled differently and the sigma scaling correction
  threshold is exceedd then a correction is made in the sigma
  calculations for these differences, again under the assumption that
  the noise in an image scales as the square root of the mean intensity.
  </p>
  <p>
  After rejection the number of retained pixels is checked against the
  <i>nkeep</i> parameter.  If there are fewer pixels retained than specified
  by this parameter the pixels with the smallest residuals in absolute
  value are added back.  If there is more than one pixel with the same
  absolute residual (for example the two pixels about an average
  or median of two will have the same residuals) they are all added
  back even if this means more than <i>nkeep</i> pixels are retained.
  Note that the <i>nkeep</i> parameter only applies to the pixels used
  by the clipping rejection algorithm and does not apply to threshold
  or bad pixel mask rejection.
  </p>
  <p>
  This algorithm works well for even a few input images.  It works better if
  the median is used though this is slower than using the average.  Note that
  if the images have a known read out noise and gain (the proportionality
  factor above) then the <span style="font-family: monospace;">"ccdclip"</span> algorithm is superior.  The two algorithms
  are related in that the average sigma proportionality factor is an estimate
  of the gain.
  </p>
  <p>
  The  parameters affecting this algorithm are <i>reject</i> to select
  this algorithm, <i>mclip</i> to select the median or average for the
  center of the clipping, <i>nkeep</i> to limit the number of pixels
  rejected, <i>lsigma</i> and <i>hsigma</i> to select the
  clipping thresholds, and <i>sigscale</i> to set the threshold for
  making corrections to the sigma calculation for different image scale
  factors.
  </p>
  <p>
  PCLIP
  The percentile clipping algorithm is similar to sigma clipping using the
  median as the center of the distribution except that, instead of computing
  the sigma of the pixels from the CCD noise parameters or from the data
  values, the width of the distribution is characterized by the difference
  between the median value and a specified <span style="font-family: monospace;">"percentile"</span> pixel value.  This
  width is then multiplied by the scale factors <i>lsigma</i> and <i>hsigma</i>
  to define the clipping thresholds above and below the median.  The clipping
  is not iterated.
  </p>
  <p>
  The pixel values at each output point are ordered in magnitude and the
  median is determined.  In the case of an even number of pixels the average
  of the two middle values is used as the median value and the lower or upper
  of the two is the median pixel when counting from the median pixel to
  selecting the percentile pixel.  The parameter <i>pclip</i> selects the
  percentile pixel as the number (if the absolute value is greater
  than unity) or fraction of the pixels from the median in the ordered set.
  The direction of the percentile pixel from the median is set by the sign of
  the <i>pclip</i> parameter with a negative value signifying pixels with
  values less than the median.  Fractional values are internally converted to
  the appropriate number of pixels for the number of input images.  A minimum
  of one pixel and a maximum corresponding to the extreme pixels from the
  median are enforced.  The value used is reported in the log output.  Note
  that the same percentile pixel is used even if pixels have been rejected by
  offsetting, masking, or thresholding; for example, if the 3rd pixel below
  the median is specified then the 3rd pixel will be used whether there are
  10 pixels or 5 pixels remaining after the preliminary steps.
  </p>
  <p>
  After rejection the number of retained pixels is checked against the
  <i>nkeep</i> parameter.  If there are fewer pixels retained than specified
  by this parameter the pixels with the smallest residuals in absolute
  value are added back.  If there is more than one pixel with the same
  absolute residual (for example the two pixels about an average
  or median of two will have the same residuals) they are all added
  back even if this means more than <i>nkeep</i> pixels are retained.
  Note that the <i>nkeep</i> parameter only applies to the pixels used
  by the clipping rejection algorithm and does not apply to threshold
  or bad pixel mask rejection.
  </p>
  <p>
  Some examples help clarify the definition of the percentile pixel.  In the
  examples assume 10 pixels.  The median is then the average of the
  5th and 6th pixels.  A <i>pclip</i> value of 2 selects the 2nd pixel
  above the median (6th) pixel which is the 8th pixel.  A <i>pclip</i>
  value of -0.5 selects the point halfway between the median and the
  lowest pixel.  In this case there are 4 pixels below the median,
  half of that is 2 pixels which makes the percentile pixel the 3rd pixel.
  </p>
  <p>
  The percentile clipping algorithm is most useful for clipping small
  excursions, such as the wings of bright objects when combining
  disregistered observations for a sky flat field, that are missed when using
  the pixel values to compute a sigma.  It is not as powerful, however, as
  using the CCD noise parameters (provided they are accurately known) to clip
  about the median.
  </p>
  <p>
  The  parameters affecting this algorithm are <i>reject</i> to select this
  algorithm, <i>pclip</i> to select the percentile pixel, <i>nkeep</i> to limit
  the number of pixels rejected, and <i>lsigma</i> and <i>hsigma</i> to select
  the clipping thresholds.
  </p>
  <p>
  GROW REJECTION
  </p>
  <p>
  Neighbors of pixels rejected by the rejection algorithms
  may also be rejected.  The number of neighbors to be rejected
  is specified by the <i>grow</i> parameter which is a radius in pixels.
  If too many pixels are rejected in one of the grown pixels positions
  (as defined by the <i>nkeep</i> parameter) then the value of that pixel
  without growing will be used.
  </p>
  <p>
  COMBINING
  </p>
  <p>
  After all the steps of offsetting the input images, masking pixels,
  threshold rejection, scaling, and applying a rejection algorithms the
  remaining pixels are combined and output.  The pixels may be combined
  by computing the median or by computing a weighted average.
  </p>
  <p>
  SIGMA OUTPUT
  </p>
  <p>
  In addition to the combined image and optional sigma image may be
  produced.  The sigma computed is the standard deviation, corrected for a
  finite population by a factor of n/(n-1), of the unrejected input pixel
  values about the output combined pixel values.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To average and median images without any other features:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; oimcombine obj* avg combine=average reject=none
  cl&gt; oimcombine obj* med combine=median reject=none
  </pre></div>
  <p>
  2.  To reject cosmic rays:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; oimcombine obs1,obs2 Obs reject=crreject rdnoise=5.1, gain=4.3
  </pre></div>
  <p>
  3.  To make a grid for display purposes with 21 64x64 images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; oimcombine @list grid offset="grid 5 65 5 65"
  </pre></div>
  <p>
  4.  To apply a mask image with good pixels marked with a zero value and
  bad pixels marked with a value of one:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit ims* bpm badpix.pl add+ ver-
  cl&gt; oimcombine ims* final combine=median masktype=goodval
  </pre></div>
  <p>
  5.  To scale image by the exposure time and then adjust for varying
  sky brightness and make a weighted average:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; oimcombine obj* avsig combine=average reject=avsig \
  &gt;&gt;&gt; scale=exp zero=mode weight=exp  expname=exptime
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_OIMCOMBINE">
  <dt><b>OIMCOMBINE V2.11.4</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='OIMCOMBINE' Line='OIMCOMBINE V2.11.4' -->
  <dd>The version of IMCOMBINE from V2.11-V2.11.3 was moved to OBSOLETE.
  </dd>
  </dl>
  </section>
  <section id="s_limitations">
  <h3>Limitations</h3>
  <p>
  Though the previous limit on the number of images that can be combined
  was removed in V2.11 the method has the limitation that only a single
  bad pixel mask will be used for all images.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  immatch.imcombine ccdred.combine onedspec.scombine, wpfc.noisemodel
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'LIMITATIONS' 'SEE ALSO'  -->
  

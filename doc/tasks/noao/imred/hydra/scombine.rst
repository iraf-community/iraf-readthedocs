.. _scombine:

scombine: Combine spectra having different wavelength ranges
============================================================

**Package: hydra**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  scombine input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images containing spectra to be combined.  The spectra
  in the images to be combined are selected with the <i>apertures</i> and
  <i>group</i> parameters.  Only the primary spectrum is combined and
  the associated band spectra are ignored.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output images to be created containing the combined spectra.
  If the grouping option is <span style="font-family: monospace;">"all"</span>
  or <span style="font-family: monospace;">"apertures"</span> then only one output image will be created.  In the
  first case the image will contain only one spectrum and in the latter case
  there will be a spectrum for each selected aperture.
  If the grouping option is <span style="font-family: monospace;">"images"</span> then there will be one
  output spectrum per input spectrum.
  </dd>
  </dl>
  <dl id="l_noutput">
  <dt><b>noutput = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='noutput' Line='noutput = ""' -->
  <dd>List of output images to be created containing the number of spectra combined.
  The number of images required is the same as the <i>output</i> list.
  Any or all image names may be given as a null string, i.e. <span style="font-family: monospace;">""</span>, in which
  case no output image is created.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"STDOUT"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "STDOUT"' -->
  <dd>File name for recording log information about the combining operation.
  The file name <span style="font-family: monospace;">"STDOUT"</span> is used to write the information to the terminal.
  If the null string is specified then no log information is printed or
  recorded.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>List of apertures to be selected for combining.  If none is specified
  then all apertures are selected.  The syntax is a blank or comma separated
  list of aperture numbers or aperture ranges separated by a hyphen.
  </dd>
  </dl>
  <dl id="l_group">
  <dt><b>group = <span style="font-family: monospace;">"apertures"</span> (all|images|apertures)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='group' Line='group = "apertures" (all|images|apertures)' -->
  <dd>Option for grouping input spectra for combining (after selection by aperture)
  from one or more input images.  The options are:
  <dl>
  <dt><b><span style="font-family: monospace;">"all"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"all"' -->
  <dd>Combine all spectra from all images in the input list into a single output
  spectrum.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"images"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"images"' -->
  <dd>Combine all spectra in each input image into a single spectrum in
  separate output images.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"apertures"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"apertures"' -->
  <dd>Combine all spectra of the same aperture from all input images and put it
  into a single output image with the other selected apertures.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_combine">
  <dt><b>combine = <span style="font-family: monospace;">"average"</span> (average|median|sum)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='combine' Line='combine = "average" (average|median|sum)' -->
  <dd>Option for combining pixels at the same dispersion coordinate.  after any
  rejection operation.  The options are to compute the  <span style="font-family: monospace;">"average"</span>, <span style="font-family: monospace;">"median"</span>,
  or <span style="font-family: monospace;">"sum"</span> of the pixels.  The first two are applied after any pixel
  rejection.  The sum option ignores the rejection and scaling parameters and
  no rejection is performed.  In other words, the <span style="font-family: monospace;">"sum"</span> option is simply the
  direct summation of the pixels.  The median uses the average of the two
  central values when the number of pixels is even.
  </dd>
  </dl>
  <dl id="l_reject">
  <dt><b>reject = <span style="font-family: monospace;">"none"</span> (none|minmax|ccdclip|crreject|sigclip|avsigclip|pclip)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reject' Line='reject = "none" (none|minmax|ccdclip|crreject|sigclip|avsigclip|pclip)' -->
  <dd>Type of rejection operation performed on the pixels which overlap at each
  dispersion coordinate.  The algorithms are discussed in the
  DESCRIPTION section.  The rejection choices are:
  <div class="highlight-default-notranslate"><pre>
       none - No rejection
     minmax - Reject the nlow and nhigh pixels
    sigclip - Reject pixels using a sigma clipping algorithm
  avsigclip - Reject pixels using an averaged sigma clipping algorithm
    ccdclip - Reject pixels using CCD noise parameters
   crreject - Reject only positive pixels using CCD noise parameters
      pclip - Reject pixels using sigma based on percentiles
  </pre></div>
  </dd>
  </dl>
  <dl id="l_first">
  <dt><b>first = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='first' Line='first = no' -->
  <dd>Use the first input spectrum of each set to be combined to define the
  dispersion coordinates for combining and output?  If yes then all other
  spectra to be combined will be interpolated to the dispersion of this
  reference spectrum and that dispersion defines the dispersion of the
  output spectrum.  If no, then all the spectra are interpolated to a linear
  dispersion as determined by the following parameters.  The interpolation
  type is set by the package parameter <i>interp</i>.
  </dd>
  </dl>
  <dl id="l_w1">
  <dt><b>w1 = INDEF, w2=INDEF, dw = INDEF, nw = INDEF, log = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='w1' Line='w1 = INDEF, w2=INDEF, dw = INDEF, nw = INDEF, log = no' -->
  <dd>The output linear or log linear wavelength scale if the dispersion of the
  first spectrum is not used.  INDEF values are filled in from the maximum
  wavelength range and minimum dispersion of the spectra to be combined.  The
  parameters are aways specified in linear wavelength even when the log
  parameter is set to produce constant pixel increments in the log of the
  wavelength.  The dispersion is interpreted in that case as the difference
  in the log of the endpoints divided by the number of pixel increments.
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = <span style="font-family: monospace;">"none"</span> (none|mode|median|mean|exposure|@&lt;file&gt;|!&lt;keyword&gt;)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = "none" (none|mode|median|mean|exposure|@&lt;file&gt;|!&lt;keyword&gt;)' -->
  <dd>Multiplicative image scaling to be applied.  The choices are none,
  multiply by the reciprocal of the mode , median, or mean of the specified
  statistics section, scale by the exposure time in the image header, multiply
  by the values in a specified file, or multiply by a specified image header
  keyword.  When specified in a file the scales must be one per line in the
  order of the input spectra.
  </dd>
  </dl>
  <dl id="l_zero">
  <dt><b>zero = <span style="font-family: monospace;">"none"</span> (none|mode|median|mean|@&lt;file&gt;|!&lt;keyword&gt;)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zero' Line='zero = "none" (none|mode|median|mean|@&lt;file&gt;|!&lt;keyword&gt;)' -->
  <dd>Additive zero level image shifts to be applied.  The choices are none,
  add the negative of the mode, median, or mean of the specified statistics
  section, add the values given in a file, or add values given by an
  image header keyword.  When specified in a file the zero values must be one
  per line in the order of the input spectra. File or keyword zero offset
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
  the input spectra.
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample' Line='sample = ""' -->
  <dd>Wavelength sample regions to use in computing spectrum statistics for
  scaling and weighting.  If no sample regions are given then the entire
  input spectrum is used.  The syntax is colon separated wavelengths
  or a file containing colon separated wavelengths preceded by the
  @ character; i.e. @&lt;file&gt;.
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
  These numbers are converted to fractions of the total number of input spectra
  so that if no rejections have taken place the specified number of pixels
  are rejected while if pixels have been rejected by thresholding
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
  the maximum number to reject.  This is actually converted to a number
  to keep by adding it to the number of images.
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
  <dd>Effective CCD readout noise in electrons, gain in electrons/DN, and
  sensitivity noise as a fraction.  These parameters are used with the
  <span style="font-family: monospace;">"ccdclip"</span> and <span style="font-family: monospace;">"crreject"</span> algorithms.  The values may be either numeric or
  an image header keyword which contains the value.  Note that if the spectra
  have been extracted from a 2D CCD image then the noise parameters must be
  adjusted for background and the aperture summing.
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
  <dt><b>grow = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grow' Line='grow = 0' -->
  <dd>Number of pixels to either side of a rejected pixel
  to also be rejected.  This applies only to pixels rejected by one of
  the rejection algorithms and not the threshold rejected pixels.
  </dd>
  </dl>
  <dl id="l_blank">
  <dt><b>blank = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blank' Line='blank = 0.' -->
  <dd>Value to use when there are no input pixels to combine for an output pixel.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Scombine</b> combines input spectra by interpolating them (if necessary)
  to a common dispersion sampling, rejecting pixels exceeding specified low
  and high thresholds, scaling them in various ways, applying a rejection
  algorithm based on known or empirical noise statistics, and computing the
  sum, weighted average, or median of the remaining pixels.  Note that
  the <span style="font-family: monospace;">"sum"</span> option is the direct summation of the pixels and does not
  perform any rejection or scaling of the data regardless of the parameter
  settings.
  </p>
  <p>
  The input spectra are specified using an image list in which each image
  may contain multiple spectra.  The set of spectra may be restricted
  by the <i>aperture</i> parameter to specific apertures.  The set of input
  spectra may then be grouped using the <i>group</i> parameter and each
  group combined separately into a final output spectrum.  The grouping
  options are to select all the input spectra regardless of the input
  image or aperture number, select all spectra of the same aperture,
  or select all the spectra from the same input image.
  </p>
  <p>
  The output consists of either a single image with one spectrum for each
  combined group or, when grouping by image, an image with the single
  combined spectra from each input image.  The output images and
  combined spectra inherit the header parameters from the first spectrum
  of the combined group.  In addition to the combined spectrum an associated
  integer spectrum containing the number of pixels combined
  and logfile listing the combined spectra, scaling, weights, etc, may
  be produced.
  </p>
  <p>
  The spectral combining is done using pixels at common dispersion
  coordinates rather than physical or logical pixel coordinates.  If the
  spectra to be combined do not have identical dispersion coordinates then
  the spectra are interpolated to a common dispersion sampling before
  combining.  The interpolation conserves pixel values rather pixel fluxes.
  This means that flux calibrated data is treated correctly and that
  spectra in counts are not corrected in the interpolation for changes
  in pixel widths.  
  The default interpolation function is a 5th order polynomial.  The
  choice of interpolation type is made with the package parameter <span style="font-family: monospace;">"interp"</span>.
  It may be set to <span style="font-family: monospace;">"nearest"</span>, <span style="font-family: monospace;">"linear"</span>, <span style="font-family: monospace;">"spline3"</span>, <span style="font-family: monospace;">"poly5"</span>, or <span style="font-family: monospace;">"sinc"</span>.
  Remember that this applies to all tasks which might need to interpolate
  spectra in the <b>onedspec</b> and associated packages.  For a discussion of
  interpolation types see <b>onedspec</b>.
  </p>
  <p>
  There are two choices for the common dispersion coordinate sampling. If the
  <i>first</i> parameter is set then the dispersion sampling of the first
  spectrum is used.  This dispersion system may be nonlinear.  If the
  parameter is not set then the user specified linear or log linear
  dispersion system is used.  Any combination of starting wavelength, ending
  wavelength, wavelength per pixel, and number of output pixels may be
  specified.  Unspecified values will default to reasonable values based on
  the minimum or maximum wavelengths of all spectra, the minimum dispersion,
  and the number of pixels needed to satisfy the other parameters.  If the
  parameters overspecify the linear system then the ending wavelength is
  adjusted based on the other parameters.  Note that for a log linear system
  the wavelengths are still specified in nonlog units and the dispersion is
  finally recalculated using the difference of the log wavelength endpoints
  divided by the number pixel intervals (the number of pixels minus one).
  </p>
  <p>
  There are several stages to combining a selected group of spectra.  The
  first is interpolation to a common dispersion sampling as discussed
  above.  The second stage is to eliminate any pixels outside the specified
  thresholds.  Note that the thresholds apply to the interpolated
  spectra.  Scaling and zero offset factors are computed and applied to the
  spectra if desire.  The computation of these factors as well as weights is
  discussed in the following section.  Next there is a choice of rejection
  algorithms to identify and eliminate deviant pixels.  Some of these are
  based on order statistics and some relative to the distance from an initial
  median or average using a noise model cutoff.  A growing factor may be
  applied to neighbors of rejected pixels to reject additional pixels.  The
  various algorithms are described in detail in a following section.
  Finally, the remaining pixels are combined by summing (which may not be
  appropriate when pixels are rejected), computing a median, or computing a
  weighted or unweighted average.  The combined spectrum is written to an
  output image as well the number of pixels used in the final combining.
  </p>
  <p>
  SCALES AND WEIGHTS
  </p>
  <p>
  In order to combine spectra with rejection of pixels based on deviations
  from some average or median they must be scaled to a common level.  There
  are two types of scaling available, a multiplicative intensity scale and an
  additive zero point shift.  The intensity scaling is defined by the
  <i>scale</i> parameter and the zero point shift by the <i>zero</i>
  parameter.  These parameters may take the values <span style="font-family: monospace;">"none"</span> for no scaling,
  <span style="font-family: monospace;">"mode"</span>, <span style="font-family: monospace;">"median"</span>, or <span style="font-family: monospace;">"mean"</span> to scale by statistics of the spectrum pixels,
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
  The spectrum statistics factors are computed within specified sample
  regions given as a series of colon separated wavelengths.  If no
  regions are specified then all pixels are used.  If the
  wavelength sample list is too long the regions can be defined in a file and
  specified in the <i>sample</i> parameter using the syntax @&lt;file&gt; where file
  is the filename.
  </p>
  <p>
  The statistics are as indicated by their names.  In particular, the
  mode is a true mode using a bin size which is a fraction of the
  range of the pixels and is not based on a relationship between the
  mode, median, and mean.  Also thresholded pixels are excluded from the
  computations as well as during the rejection and combining operations.
  </p>
  <p>
  The <span style="font-family: monospace;">"exposure"</span> option in the intensity scaling uses the value of the image
  header keyword (EXPTIME, EXPOSURE, or ITIME).  Note that the exposure
  keyword is also updated in the final image as the weighted average of the
  input values.  If one wants to use a nonexposure time keyword and keep the
  exposure time updating feature the image header keyword syntax is
  available; i.e. !&lt;keyword&gt;.
  </p>
  <p>
  Scaling values may be defined as a list of values in a text file.  The file
  name is specified by the standard @file syntax.  The list consists of one
  value per line.  The order of the list is assumed to be the same as the
  order of the input spectra.  It is a fatal error if the list is incomplete
  and a warning if the list appears longer than the number of input spectra.
  Consideration of the grouping parameter must be included in
  generating this list since spectra may come from different images,
  some apertures may be missing, and, when there are multiple output spectra
  or images, the same list will be repeatedly used.
  </p>
  <p>
  If both an intensity scaling and zero point shift are selected the
  multiplicative scaling is done first.  Use of both makes sense for images
  if the intensity scaling is the exposure time to correct for
  different exposure times and with the zero point shift allowing for
  sky brightness changes.  This is less relevant for spectra but the option
  is available.
  </p>
  <p>
  The spectrum statistics and scale factors are recorded in the log file
  unless they are all equal, which is equivalent to no scaling.  The
  intensity scale factors are normalized to a unit mean and the zero
  point shifts are adjusted to a zero mean.  When scal factors
  or zero point shifts are specified by the user in an @file or by an
  image header keyword, no normalization is done.
  </p>
  <p>
  Scaling affects not only the mean values between spectra but also the
  relative pixel uncertainties.  For example scaling an spectrum by a
  factor of 0.5 will reduce the effective noise sigma of the spectrum
  at each pixel by the square root of 0.5.  Changes in the zero
  point also changes the noise sigma if the spectrum noise characteristics
  are Poissonian.  In the various rejection algorithms based on
  identifying a noise sigma and clipping large deviations relative to
  the scaled median or mean, one may need to account for the scaling induced
  changes in the spectrum noise characteristics.
  </p>
  <p>
  In those algorithms it is possible to eliminate the <span style="font-family: monospace;">"sigma correction"</span>
  while still using scaling.  The reasons this might be desirable are 1) if
  the scalings are similar the corrections in computing the mean or median
  are important but the sigma corrections may not be important and 2) the
  spectrum statistics may not be Poissonian, either inherently or because the
  spectra have been processed in some way that changes the statistics.  In the
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
  If the final combining operation is <span style="font-family: monospace;">"average"</span> then the spectra may be
  weighted during the averaging.  The weights are specified in the same way
  as the scale factors.  The weights, scaled to a unit sum, are printed in
  the log output.
  </p>
  <p>
  The weights are only used for the final weighted average and sigma image
  output.  They are not used to form averages in the various rejection
  algorithms.  For weights in the case of no scaling or only multiplicative
  scaling the weights are used as given or determined so that images
  with lower signal levels will have lower weights.  However, for
  cases in which zero level scaling is used the weights are computed
  from the initial weights (the exposure time, image statistics, or
  input values) using the formula:
  </p>
  <div class="highlight-default-notranslate"><pre>
  weight_final = weight_initial / (scale * zero)
  </pre></div>
  <p>
  where the zero values are those before adjustment to zero mean over
  all images.  The reasoning is that if the zero level is high the sky
  brightness is high and so the S/N is lower and the weight should be lower.
  </p>
  <p>
  THRESHOLD REJECTION
  </p>
  <p>
  There is an initial threshold rejection step which may be applied.  The
  thresholds are given by the parameters <i>lthreshold</i> and
  <i>hthreshold</i>.  Values of INDEF mean that no threshold value is
  applied.  Threshold rejection may be used to exclude very bad pixel values
  or as a way of masking images.  The former case is useful to exclude very
  bright cosmic rays.  Some of the rejection algorithms, such as <span style="font-family: monospace;">"avsigclip"</span>,
  can perform poorly if very strong cosmic rays are present.  For masking one
  can use a task like <b>imedit</b> or <b>imreplace</b> to set parts of the
  spectra to be excluded to some very low or high magic value.
  </p>
  <p>
  REJECTION ALGORITHMS
  </p>
  <p>
  The <i>reject</i> parameter selects a type of rejection operation to
  be applied to pixels not thresholded.  If no rejection
  operation is desired the value <span style="font-family: monospace;">"none"</span> is specified.  This task is
  closely related to the image combining task <b>imcombine</b> and, in
  particular, has the same rejection algorithms.
  Some the algorithms are more appropriate to images but are available
  in this task also for completeness.
  </p>
  <p>
  MINMAX
  A specified fraction of the highest and lowest pixels are rejected.
  The fraction is specified as the number of high and low pixels, the
  <i>nhigh</i> and <i>nlow</i> parameters, when data from all the input spectra
  are used.  If pixels are missing where there is no overlap or have been
  rejected by thresholding then a matching fraction of the remaining pixels,
  truncated to an integer, are used.  Thus,
  </p>
  <div class="highlight-default-notranslate"><pre>
  nl = n * nlow/nspectra + 0.001
  nh = n * nhigh/nspectra + 0.001
  </pre></div>
  <p>
  where n is the number of pixels to be combined, nspectra is the number
  of input spectra, nlow and nhigh
  are task parameters and nl and nh are the final number of low and
  high pixels rejected by the algorithm.  The factor of 0.001 is to
  adjust for rounding of the ratio.
  </p>
  <p>
  As an example with 10 input spectra and specifying one low and two high
  pixels to be rejected the fractions to be rejected are 0.1 and 0.2
  and the number rejected as a function of n is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  n   0  1  2  3  4  5  6  7  8  9 10
  nl  0  0  0  0  0  1  1  1  1  1  2
  nh  0  0  0  0  0  0  0  0  0  0  1
  </pre></div>
  <p>
  CCDCLIP
  If the noise characteristics of the spectra can be described by fixed
  gaussian noise, a poissonian noise which scales with the square root of
  the intensity, and a sensitivity noise which scales with the intensity,
  the sigma in data values at a pixel with true value &lt;I&gt;,
  as approximated by the median or average with the lowest and highest value
  excluded, is given as:
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
  </p>
  <p>
  This model is typically valid for CCD images.  During extraction of 
  spectra from CCD images the noise parameters of the spectrum pixels
  will be changed from those of the CCD pixels.  Currently it is up to
  the user to determine the proper modifications of the CCD read noise
  gain, and sensitivity noise.
  </p>
  <p>
  The read out noise is specified by the <i>rdnoise</i> parameter.  The value
  may be a numeric value to be applied to all the input spectra or an image
  header keyword containing the value for spectra from each image.
  Similarly, the parameter <i>gain</i> specifies the gain as either a value or
  image header keyword and the parameter <i>snoise</i> specifies the
  sensitivity noise parameter as either a value or image header keyword.
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
  spectrum scale parameters; i.e. the median or average is scaled to that of the
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
  two spectra.
  </p>
  <p>
  SIGCLIP
  The sigma clipping algorithm computes at each output pixel the median or
  average excluding the high and low values and the sigma about this
  estimate.  There must be at least three input pixels, though for this method
  to work well there should be at least 10 pixels.  Values deviating by more
  than the specified sigma threshold factors are rejected.  These steps are
  repeated, except that after the first time the average includes all values,
  until no further pixels are rejected or there are fewer than three pixels.
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
  rejection.
  </p>
  <p>
  The  parameters affecting this algorithm are <i>reject</i> to select
  this algorithm, <i>mclip</i> to select the median or average for the
  center of the clipping, <i>nkeep</i> to limit the number of pixels
  rejected, <i>lsigma</i> and <i>hsigma</i> to select the
  clipping thresholds, and <i>sigscale</i> to set the threshold for
  making corrections to the sigma calculation for different spectrum scale
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
  This noise model is valid for spectra whose values are proportional to the
  number of photons recorded.  In effect this algorithm estimates a
  photon per data value gain for each spectrum.
  The gain proportionality factor is computed
  independently for each output spectrum by averaging the square of the residuals
  (at points having three or more input values) scaled by the median or
  mean.
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
  If the spectra are scaled differently and the sigma scaling correction
  threshold is exceedd then a correction is made in the sigma
  calculations for these differences, again under the assumption that
  the noise in an spectra scales as the square root of the mean intensity.
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
  rejection.
  </p>
  <p>
  This algorithm works well for even a few input spectra.  It works better if
  the median is used though this is slower than using the average.  Note that
  if the spectra have a known read out noise and gain (the proportionality
  factor above) then the <span style="font-family: monospace;">"ccdclip"</span> algorithm is superior.  However, currently
  the CCD noise characteristics are not well propagated during extraction so
  this empirical algorithm is the one most likely to be useful.  The two
  algorithms are related in that the average sigma proportionality factor is
  an estimate of the gain.
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
  width is then multipled by the scale factors <i>lsigma</i> and <i>hsigma</i>
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
  the appropriate number of pixels for the number of input spectra.  A minimum
  of one pixel and a maximum corresponding to the extreme pixels from the
  median are enforced.  The value used is reported in the log output.  Note
  that the same percentile pixel is used even if pixels have been rejected by
  nonoverlap or thresholding; for example, if the 3nd pixel below
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
  excursions, such as the wings of bright lines when combining
  disregistered observations, that are missed when using
  the pixel values to compute a sigma.  It is not as powerful, however, as
  using the CCD noise parameters (provided they are accurately known) to clip
  about the median.  This algorithm is primarily used with direct images
  but remains available for spectra.
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
  may also be rejected.  The number of neighbors to be rejected on either
  side is specified by the <i>grow</i> parameter.
  </p>
  <p>
  This rejection step is also checked against the <i>nkeep</i> parameter
  and only as many pixels as would not violate this parameter are
  rejected.  Unlike it's application in the rejection algorithms at
  this stage there is no checking on the magnitude of the residuals
  and the pixels retained which would otherwise be rejected are randomly
  selected.
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
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Combine orders of echelle images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scombine *.ec *%.ec%% group=images combine=sum
  </pre></div>
  <p>
  2.  Combine all spectra using range syntax and scale by the exposure times.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; names irs 10-42 &gt; irs.dat
  cl&gt; scombine @irs.dat irscombine group=all scale=exptime
  </pre></div>
  <p>
  3.  Combine spectra by apertures using exposure time scaling and weighting.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scombine *.ms combine.ms nout=ncombine.ms \\
  &gt;&gt;&gt; group=apertures scale=exptime weights=exptime
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_SCOMBINE">
  <dt><b>SCOMBINE V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SCOMBINE' Line='SCOMBINE V2.10.3' -->
  <dd>The weighting was changed from using the square root of the exposure time
  or spectrum statistics to using the values directly.  This corresponds
  to variance weighting.  Other options for specifying the scaling and
  weighting factors were added; namely from a file or from a different
  image header keyword.  The <i>nkeep</i> parameter was added to allow
  controlling the maximum number of pixels to be rejected by the clipping
  algorithms.  The <i>snoise</i> parameter was added to include a sensitivity
  or scale noise component to the noise model.
  </dd>
  </dl>
  <dl id="l_SCOMBINE">
  <dt><b>SCOMBINE V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SCOMBINE' Line='SCOMBINE V2.10' -->
  <dd>This task is new.
  </dd>
  </dl>
  </section>
  <section id="s_notes">
  <h3>Notes</h3>
  <p>
  The pixel uncertainties and CCD noise model are not well propagated.  In
  particular it would be desirable to propagate the pixel uncertainties
  and CCD noise parameters from the initial CCD images.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcombine, odcombine, lscombine
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'NOTES' 'SEE ALSO'  -->
  

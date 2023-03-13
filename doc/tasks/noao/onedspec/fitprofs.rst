.. _fitprofs:

fitprofs: Fit gaussian profiles
===============================

**Package: onedspec**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fitprofs input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images to be fit.  The images may be one dimensional
  spectra (one or more spectra per image) or long slit spectra.  Other
  types of nonspectral images may also be used and for two dimensional
  images the fitting direction will be determined from either the keyword
  DISPAXIS in the image header or the <i>dispaxis</i> parameter.
  </dd>
  </dl>
  <dl id="l_lines">
  <dt><b>lines = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lines' Line='lines = ""' -->
  <dd>List of lines, columns, or apertures to be selected from the input image
  format.  The default empty list, <span style="font-family: monospace;">""</span>, selects all vectors in the images.
  The syntax is a list of comma separated numbers or ranges, where a range
  is a pair of hyphen separated numbers.
  </dd>
  </dl>
  <dl id="l_bands">
  <dt><b>bands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bands' Line='bands = ""' -->
  <dd>List of bands for 3D images.  The empty list, <span style="font-family: monospace;">""</span>, selects all bands.
  </dd>
  </dl>
  <dl id="l_dispaxis">
  <dt><b>dispaxis = <span style="font-family: monospace;">")_.dispaxis"</span>, nsum = <span style="font-family: monospace;">")_.nsum"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispaxis' Line='dispaxis = ")_.dispaxis", nsum = ")_.nsum"' -->
  <dd>Parameters for defining vectors in 2D and 3D images.  The
  dispersion axis is 1 for line vectors, 2 for column vectors, and 3 for band
  vectors.  A DISPAXIS parameter in the image header has precedence over the
  <i>dispaxis</i> parameter.  The default values defer to the package
  parameters of the same name.
  </dd>
  </dl>
  <p>
  The following are the fitting parameters.
  </p>
  <dl id="l_region">
  <dt><b>region = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='region' Line='region = ""' -->
  <dd>Region of the input vectors to be fit specified as a pair of space
  separated numbers.  The coordinates are defined in terms of the linear
  image header coordinate parameters.  For dispersion corrected spectra this
  is usually wavelength in Angstroms and for other data it is usually pixels.
  A fitting region must be specified.
  </dd>
  </dl>
  <dl id="l_positions">
  <dt><b>positions = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='positions' Line='positions = ""' -->
  <dd>File of initial or fixed profile positions and (optional) peaks, profile
  types, and widths.  The
  format consists of lines with one or more whitespace separated fields.
  The fields are the position, peak relative to the continuum with
  negative values being absorption, profile type of gaussian, lorentzian,
  or voigt, and the gaussian and/or lorentzian full width at half maximum.
  Trailing fields may be missing and fields to be set from default parameters
  or the image data (the peak value) may be given as INDEF.
  Comments and any additional columns are ignored.  The positions and
  widths are specified in the coordinate units of the image, usually
  wavelength for dispersion corrected spectra and pixels otherwise.
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = ""' -->
  <dd>Background values defining the linear background.  If not specified the
  single pixel values nearest the fitting region endpoints are used.
  Otherwise two whitespace separated values are expected.  If a value is
  a number then that is the background at the lower or upper end of the
  fitting region (ordered in pixel space not wavelength).  The special
  values <span style="font-family: monospace;">"avg(w1,w2,z)"</span> or <span style="font-family: monospace;">"med(w1,w2,z)"</span> (note that there can be no
  whitespace) may be specified, where w1 and w2 are dispersion values, and z
  is a multiplier.  This will take the average or median of pixels within the
  specified range and multiply the result by the third argument.  The
  dispersion point used for that value in computing the linear background is
  the average of the dispersion coordinates of the pixels used.
  </dd>
  </dl>
  <dl id="l_profile">
  <dt><b>profile = <span style="font-family: monospace;">"gaussian"</span> (gaussian|lorentzian|voigt)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='profile' Line='profile = "gaussian" (gaussian|lorentzian|voigt)' -->
  <dd>Default profile type to be fit when a profile type is not specified in
  the positions file.  The type are <span style="font-family: monospace;">"gaussian"</span>, <span style="font-family: monospace;">"lorentzian"</span>, or <span style="font-family: monospace;">"voigt"</span>.
  </dd>
  </dl>
  <dl id="l_gfwhm">
  <dt><b>gfwhm = 20., lfwhm = 20.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gfwhm' Line='gfwhm = 20., lfwhm = 20.' -->
  <dd>Default gaussian and lorentzian full width at half maximum (FWHM).
  These values are used for the initial and/or fixed width when they are
  not specified in the position file.
  </dd>
  </dl>
  <dl id="l_fitbackground">
  <dt><b>fitbackground = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitbackground' Line='fitbackground = yes' -->
  <dd>Fit the background?  If <span style="font-family: monospace;">"yes"</span> a linear background across the fitting region
  will be fit simultaneously with the profiles.  If <span style="font-family: monospace;">"no"</span> the background will
  be fixed.
  </dd>
  </dl>
  <dl id="l_fitpositions">
  <dt><b>fitpositions = <span style="font-family: monospace;">"all"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitpositions' Line='fitpositions = "all"' -->
  <dd>Position fitting option.  This may be <span style="font-family: monospace;">"fixed"</span> to fix all positions at their
  initial values, <span style="font-family: monospace;">"single"</span> to fit a single shift to the positions while
  keeping their separations fixed, or <span style="font-family: monospace;">"all"</span> to independently fit all the
  positions.
  </dd>
  </dl>
  <dl id="l_fitgfwhm">
  <dt><b>fitgfwhm = <span style="font-family: monospace;">"all"</span>, fitlfwhm = <span style="font-family: monospace;">"all"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitgfwhm' Line='fitgfwhm = "all", fitlfwhm = "all"' -->
  <dd>Profile width fitting options.  These may be <span style="font-family: monospace;">"fixed"</span> to fix all widths
  at their initial values, <span style="font-family: monospace;">"single"</span> to fit a single scale factor to the initial
  widths, or <span style="font-family: monospace;">"all"</span> to independently fit all the widths.
  </dd>
  </dl>
  <p>
  The following parameters are used for error estimates as described
  below in the ERROR ESTIMATES section.
  </p>
  <dl id="l_nerrsample">
  <dt><b>nerrsample = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nerrsample' Line='nerrsample = 0' -->
  <dd>Number of samples for the error computation.  A value less than 10 turns
  off the error computation.  A value of ~10 does a rough error analysis, a
  value of ~50 does a reasonable error analysis, and a value &gt;100 does a
  detailed error analysis.  The larger this value the longer the analysis
  takes.
  </dd>
  </dl>
  <dl id="l_sigma0">
  <dt><b>sigma0 = INDEF, invgain = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma0' Line='sigma0 = INDEF, invgain = INDEF' -->
  <dd>The pixel sigmas are modeled by the formula:
  <div class="highlight-default-notranslate"><pre>
  sigma**2 = sigma0**2 + invgain * I
  </pre></div>
  where I is the pixel value and <span style="font-family: monospace;">"**2"</span> means the square of the quantity.  If
  either parameter is specified as INDEF or with a value less than zero then
  no sigma estimates are made and so no error estimates for the measured
  parameters is made.
  </dd>
  </dl>
  <p>
  The following parameters determine the output of the task.
  </p>
  <dl id="l_components">
  <dt><b>components = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='components' Line='components = ""' -->
  <dd>All profiles defined by the position file are simultaneously fit but only
  a subset of the fitted profiles may be selected for output.  A profile
  or component is identified by the order number in the position file;
  i.e. the first entry in the position file is 1, the second is 2, etc.
  The components to be output are specified by a range list.  The empty
  list, <span style="font-family: monospace;">""</span>, selects all profiles.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print fitting results and record of output images created on the
  standard output (normally the terminal).
  The fitting information is printed to the logfile so there is normally
  no need to redirect this output.  The output may be turned off when
  the task is run as a background task.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "logfile"' -->
  <dd>Logfile for fitting results.  If not specified the results will not be
  logged.
  </dd>
  </dl>
  <dl id="l_plotfile">
  <dt><b>plotfile = <span style="font-family: monospace;">"plotfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotfile' Line='plotfile = "plotfile"' -->
  <dd>File to contain plot output.  The plots show the image vector with
  overplots of the total fit, the individual components, and the residuals.
  The plotfile may be examined and manipulated later with tools such as
  <b>gkimosaic</b>.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>List of output images.  If not specified then no output images are created.
  If images are specified the list is matched with the input list.
  </dd>
  </dl>
  <dl id="l_option">
  <dt><b>option = <span style="font-family: monospace;">"fit"</span> (fit|difference)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='option' Line='option = "fit" (fit|difference)' -->
  <dd>Image output option.  The choices are <span style="font-family: monospace;">"fit"</span> to output the fitted image
  vector which is the sum of the fitted profiles (without a background),
  or <span style="font-family: monospace;">"difference"</span> to output the data with the profiles subtracted.
  </dd>
  </dl>
  <dl id="l_clobber">
  <dt><b>clobber = no, merge = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clobber' Line='clobber = no, merge = no' -->
  <dd>Clobber or modify any existing output images?  If clobbering is not
  enabled a warning is printed and any existing output images are not
  modified.  If clobbering is enabled then either new images are created
  if merge is <span style="font-family: monospace;">"no"</span> or the new fits are merged with the existing images.
  Merging is meaningful when only a subset of the input is fit such
  as selected lines or apertures.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Fitprofs</b> fits one dimensional profile functions to image vectors
  and outputs the fitting parameters, plots, and model or residual
  image vectors.  This is done noninteractively using a file of initial
  profile positions and widths.  Interactive profile fitting may be
  done with the deblending option of <b>splot</b> or
  <b>stsdas.fitting.ngaussfit</b>.
  </p>
  <p>
  The input consists of images in a variety of formats.  These include
  all the spectral formats as well as standard images.  For two dimensional
  images (or the first 2D plane of higher dimensional images) either the
  lines or columns may be fit with possible summing of adjacent lines or
  columns to increase the signal-to-noise.  A subset of the image apertures,
  lines, or columns may be specified or all image vectors may be fit.
  </p>
  <p>
  The fitting parameters consist of a fitting region, a list of initial
  positions, peaks, and widths, initial background endpoints, the fitting
  function, and the parameters to be fit or constrained.  The coordinates and
  units used for the positions and widths are those defined by the standard
  linear coordinate header parameters.  For dispersion corrected spectra
  these are generally wavelengths in Angstroms and otherwise they are
  generally pixels.  A fitting region must be specified by a pair of
  numbers.
  </p>
  <p>
  The background parameter may be left empty to select the pixel values at
  the endpoints of the fitting region for defining the initial linear
  background.  Or values at the endpoints of the fitting region may be given
  explicitly in pixel space order (i.e. the first value is for the edge of
  the fitting region which has smaller pixel coordinate0 Values can also be
  computed from the data using the functions <span style="font-family: monospace;">"avg(w1,w2)"</span> or <span style="font-family: monospace;">"med(w1,w2)"</span>
  where w1 and w2 are dispersion coordinates.  The pixels in the specified
  range are average or medianed and the dispersion point for the linear
  background is the average of the dispersion coordinates of the pixels.
  </p>
  <p>
  The position list file consists of one or more columns.
  The format of this file has
  one or more columns.  The columns are the wavelength, the peak value
  (relative to the continuum with negative values being absorption),
  the profile type (gaussian, lorentzian, or voigt), and the
  gaussian and/or lorentzian FWHM.  End columns may be missing
  or INDEF values may be specified to use the default parameter
  values (the profile and widths) or determine the peak from the data.
  Below are examples of the file line formats
  </p>
  <div class="highlight-default-notranslate"><pre>
  wavelength
  wavelength peak
  wavelength peak (gaussian|lorenzian|voigt)
  wavelength peak gaussian gfwhm
  wavelength peak lorentzian lfwhm
  wavelength peak voigt gfwhm
  wavelength peak voigt gfwhm lfwhm
  
  1234.5                  &lt;- Wavelength only
  1234.5 -100             &lt;- Wavelength and peak
  1234.5 INDEF v          &lt;- Wavelength and profile type
  1234.5 INDEF g 12       &lt;- Wavelength and gaussian FWHM
  </pre></div>
  <p>
  where peak is the peak value, gfwhm is the gaussian FWHM, and lfwhm is
  the lorentzian FWHM.  This format is the same as used by <b>splot</b>
  and also by <b>artdata.mk1dspec</b> (except in the latter case the
  peak is normalized to a continuum of 1).
  </p>
  <p>
  The profile parameters fit are the central position, the peak amplitude,
  and the profile widths.  The fitting may be constrained in number of ways.
  The linear background may be fixed or simultaneously fit with the
  profiles.  The profile positions may be fixed, the relative separations
  fixed but a single zero point shift fit, or all positions may be fit
  simultaneously.  The profile widths may also be fixed, the relative ratios
  of the widths fixed while fitting a single scale factor, or all widths fit
  simultaneously.  The profile amplitudes are always fit.
  </p>
  <p>
  The fitting technique uses a nonlinear iterative Levenberg-Marquardt
  algorithm to reduce the Chi-square of the fit.  The execution time
  increases rapidly with the number of profiles fit so there is an
  effective limit to the number of profiles that can be fit at once.
  </p>
  <p>
  The output includes a number of formats.  The fitted parameters  are
  recorded in a logfile (if specified) and printed on the standard
  output (if the verbose flag is set).  This output includes the date,
  image vector, fitting parameters used, and a table of fitted or
  derived quantities.  The parameters included some quantities relevant to
  spectral lines but others apply to any image data.  The quantities are
  the profile center, the background or continuum at the center of the
  profile, the integral or flux of the profile (which is negative for
  profiles below the background), the equivalent width, the profile peak
  amplitude or core value, and the profile full width at half
  maximum.  Pure gaussian and lorentzian profiles will have one of
  the widths set to zero while voigt profiles will have both values.
  </p>
  <p>
  Summary plots are recored in a plotfile (if specified).  The plots
  show the data with the total fit, individual profiles, and residuals
  overplotted.  The plotfile may be examined and printed using the
  task <b>gkimosaic</b> as well as other tasks which interpret GKI metacode.
  </p>
  <p>
  The final output consists of images in the same format as the input.
  The images  may be of the total fit (sum of profiles without background)
  or of the difference (residuals) of the data minus the model.
  </p>
  </section>
  <section id="s_error_estimates">
  <h3>Error estimates</h3>
  <p>
  Error estimates may be computed for the fitted parameters.
  This requires a model for the pixel sigmas.  Currently this
  model is based on a Poisson statistics model of the data.  The model
  parameters are a constant Gaussian sigma and an <span style="font-family: monospace;">"inverse gain"</span> as specified
  by the parameters <i>sigma0</i> and <i>invgain</i>.  These parameters are
  used to compute the pixel value sigma from the following formula:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sigma**2 = sigma0**2 + invgain * I
  </pre></div>
  <p>
  where I is the pixel value and <span style="font-family: monospace;">"**2"</span> means the square of the quantity.
  </p>
  <p>
  If either the constant sigma or the inverse gain are specified as INDEF or
  with values less than zero then no noise model is applied and no error
  estimates are computed.  Also if the number of error samples is less than
  10 then no error estimates are computed.  Note that for processed spectra
  this noise model will not generally be the same as the detector readout
  noise and gain.  These parameters would need to be estimated in some way
  using the statistics of the spectrum.  The use of an inverse gain rather
  than a direct gain was choosed to allow a value of zero for this
  parameters.  This provides a model with constant uncertainties.
  </p>
  <p>
  The error estimates are computed by Monte-Carlo simulation.  The model is
  fit to the data (using the noise sigmas) and this model is used to describe
  the noise-free spectrum.  A number of simulations, given by the
  <i>nerrsample</i>, are created in which random Gaussian noise is added to
  the noise-free spectrum based on the pixel sigmas from the noise model.
  The model fitting is done for each simulation and the absolute deviation of
  each fitted parameter to model parameter is recorded.  The error estimate
  for the each parameter is then the absolute deviation containing 68.3% of
  the parameter estimates.  This corresponds to one sigma if the distribution
  of parameter estimates is Gaussian though this method does not assume
  this.
  </p>
  <p>
  The Monte-Carlo technique automatically includes all effects of
  parameter correlations and does not depend on any approximations.
  However the computation of the errors does take a significant
  amount of time.  The amount of time and the accuracy of the
  error estimates depend on how many simulations are done.  A
  small number of samples (of order 10) is fast but gives crude
  estimates.  A large number (greater than 100) is slow but gives
  very good estimates.  A compromise value of 50 is recommended
  for many applications.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  The following example creates an artificial spectrum and fits it.
  It requires the <b>artdata</b> and <b>proto</b> packages be loaded.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mk1dspec test slope=1 temp=0 lines=testlines nl=20
  cl&gt; mknoise test rdnoise=10 poisson=yes
  cl&gt; fields testlines fields=1,3 &gt; fitlines
  cl&gt; fitprofs test reg="4000 8000" pos=fitlines
  # Jul 27 17:49 test - Ap 1:
  # Nfit=20, background=YES, positions=all, gfwhm=all, lfwhm=all
  #   center      cont      flux      eqw      core   gfwhm   lfwhm
    6832.611  1363.188  -13461.8    9.875  -408.339   30.97      0.
    7963.674  1507.641  -8193.58    5.435  -395.207   19.48      0.
    5688.055   1217.01  -7075.11    5.814  -392.006   16.96      0.
      6831.3   1363.02  -7102.01     5.21  -456.463   14.62      0.
    7217.335  1412.323   -10110.    7.158  -427.797    22.2      0.
    6709.286  1347.437  -4985.06      3.7  -225.346   20.78      0.
    6434.317  1312.319  -7121.03    5.426  -342.849   19.51      0.
    6130.415  1273.506    -6164.     4.84  -224.146   25.83      0.
    4569.375  1074.138   -3904.6    3.635  -183.963   19.94      0.
    5656.645  1212.999  -8202.81    6.762  -303.617   25.38      0.
     4219.53  1029.458  -5161.64    5.014  -241.135   20.11      0.
    4551.424  1071.845  -3802.61    3.548   -139.39   25.63      0.
    4604.649  1078.643  -5539.15    5.135  -264.654   19.66      0.
    6966.557  1380.294  -11717.5    8.489  -600.581   18.33      0.
    4259.019  1034.501  -4280.38    4.138  -213.446   18.84      0.
    5952.958  1250.843  -8006.98    6.401  -318.313   23.63      0.
     4531.89  1069.351  -712.598   0.6664  -155.197   4.313      0.
    7814.418  1488.579  -2926.49    1.966  -164.891   16.67      0.
    5310.929  1168.846  -10132.2    8.669  -487.502   19.53      0.
    5022.948  1132.066   -7532.8    6.654  -325.594   21.73      0.
  </pre></div>
  <p>
  2.  Suppose there is no obvious continuum level near the fitting
  region but you want to specify a flat continuum level as the average
  of pixels in a specified wavelength region.  The background region
  would be specified as
  </p>
  <div class="highlight-default-notranslate"><pre>
  background = "avg(4250,4425.3) avg(4250,4425.3)"
  </pre></div>
  <p>
  Note that the value must be given twice to get a flat continuum.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_FITPROFS">
  <dt><b>FITPROFS V2.11.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='FITPROFS' Line='FITPROFS V2.11.3' -->
  <dd>Modified to allow a more general specification of the background.
  </dd>
  </dl>
  <dl id="l_FITPROFS">
  <dt><b>FITPROFS V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='FITPROFS' Line='FITPROFS V2.11' -->
  <dd>Modified to include lorentzian and voigt profiles.  The parameters and
  positions file format have changed in this version.  A new parameter
  controls the number of Monte-Carlo samples used in the error estimates.
  </dd>
  </dl>
  <dl id="l_FITPROFS">
  <dt><b>FITPROFS V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='FITPROFS' Line='FITPROFS V2.10.3' -->
  <dd>Error estimates based on a simple noise model are now computed.
  </dd>
  </dl>
  <dl id="l_FITPROFS">
  <dt><b>FITPROFS V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='FITPROFS' Line='FITPROFS V2.10' -->
  <dd>This task is new.
  </dd>
  </dl>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  The following CPU times were obtained with a Sun Sparcstation I.  The
  number of pixels in the fitting region and the number of lines fit
  were varied.   The worst case of fitting all parameters and a background
  was considered as well as the constrained case of  fitting line positions
  and a single width with fixed background.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Npixels Nprofs Fitbkg Fitpos  Fitsig   CPU(sec)
    100      5     yes    all     all       1.9
    100     10     yes    all     all       3.3
    100     15     yes    all     all       5.6
    100     20     yes    all     all       9.0
    512      5     yes    all     all       4.7
    512     10     yes    all     all      10.0
    512     15     yes    all     all      17.6
    512     20     yes    all     all      27.8
   1000      5     yes    all     all       8.0
   1000     10     yes    all     all      18.0
   1000     15     yes    all     all      31.8
   1000     20     yes    all     all      50.2
   1000     25     yes    all     all      72.8
   1000     30     yes    all     all     100.2
    512      5      no    all  single       2.8
    512     10      no    all  single       5.3
    512     15      no    all  single       8.6
    512     20      no    all  single      12.8
  </pre></div>
  <p>
  Crudely this implies CPU time goes as the 1.4 power of the number of profiles
  and the 0.75 power of the number of pixels.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  splot, stsdas.fitting.ngaussfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'ERROR ESTIMATES' 'EXAMPLES' 'REVISIONS' 'TIME REQUIREMENTS' 'SEE ALSO'  -->
  

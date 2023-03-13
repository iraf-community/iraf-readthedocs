.. _continuum:

continuum: Fit and normalize the continuum of multispec spectra
===============================================================

**Package: kpnocoude**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  continuum input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input spectra to be continuum normalized.  These may be any combination
  of echelle, multiaperture, one dimensional, long slit, and spectral
  cube images.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output continuum normalized spectra.  The number of output spectra must
  match the number of input spectra.  <b>Output</b> may be omitted if
  <b>listonly</b> is yes.
  </dd>
  </dl>
  <dl id="l_lines">
  <dt><b>lines = <span style="font-family: monospace;">"*"</span>, bands = <span style="font-family: monospace;">"1"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lines' Line='lines = "*", bands = "1"' -->
  <dd>A range specifications for the image lines and bands to be fit.  Unspecified
  lines and bands will be copied from the original.  If the value is <span style="font-family: monospace;">"*"</span>, all of
  the currently unprocessed lines or bands will be fit.  A range consists of
  a first line number and a last line number separated by a hyphen.  A
  single line number may also be a range and multiple ranges may be
  separated by commas.
  </dd>
  </dl>
  <dl id="l_type">
  <dt><b>type = <span style="font-family: monospace;">"ratio"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='type' Line='type = "ratio"' -->
  <dd>Type of output spectra.  The choices are <span style="font-family: monospace;">"fit"</span> for the fitted function,
  <span style="font-family: monospace;">"ratio"</span> for the ratio of the input spectra to the fit, <span style="font-family: monospace;">"difference"</span> for
  the difference between the input spectra and the fit, and <span style="font-family: monospace;">"data"</span> for
  the data minus any rejected points replaced by the fit.
  </dd>
  </dl>
  <dl id="l_replace">
  <dt><b>replace = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='replace' Line='replace = no' -->
  <dd>Replace rejected points by the fit in the difference, ratio, and
  data output types?
  </dd>
  </dl>
  <dl id="l_wavescale">
  <dt><b>wavescale = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wavescale' Line='wavescale = yes' -->
  <dd>Wavelength scale the X axis of the plot?  This option requires that the
  spectra be wavelength calibrated.  If <b>wavescale</b> is no, the plots
  will be in <span style="font-family: monospace;">"channel"</span> (pixel) space.
  </dd>
  </dl>
  <dl id="l_logscale">
  <dt><b>logscale = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logscale' Line='logscale = no' -->
  <dd>Take the log (base 10) of both axes?  This can be used when <b>listonly</b>
  is yes to measure the exponent of the slope of the continuum.
  </dd>
  </dl>
  <dl id="l_override">
  <dt><b>override = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='override' Line='override = no' -->
  <dd>Override previously normalized spectra?  If <b>override</b> is yes and
  <b>interactive</b> is yes, the user will be prompted before each order is
  refit.  If <b>override</b> is no, previously fit spectra are silently
  skipped.
  </dd>
  </dl>
  <dl id="l_listonly">
  <dt><b>listonly = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listonly' Line='listonly = no' -->
  <dd>Don't modify any images?  If <b>listonly</b> is yes, the <b>output</b>
  image list may be skipped.
  </dd>
  </dl>
  <dl id="l_logfiles">
  <dt><b>logfiles = <span style="font-family: monospace;">"logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfiles' Line='logfiles = "logfile"' -->
  <dd>List of log files to which to write the power series coefficients.  If
  <b>logfiles</b> = NULL (<span style="font-family: monospace;">""</span>), the coefficients will not be calculated.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Perform the fit interactively using the icfit commands?  This will allow
  the parameters for each spectrum to be adjusted independently.  A separate
  set of the fit parameters (below) will be used for each spectrum and any
  interactive changes to the parameters for a specific spectrum will be
  remembered when that spectrum is fit in the next image.
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample' Line='sample = "*"' -->
  <dd>The ranges of X values to be used in the continuum fits.  The units will vary
  depending on the setting of the <b>wavescale</b> and <b>logscale</b>
  parameters.  The default units are in wavelength if the spectra have
  been dispersion corrected.
  </dd>
  </dl>
  <dl id="l_naverage">
  <dt><b>naverage = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='naverage' Line='naverage = 1' -->
  <dd>Number of sample points to combined to create a fitting point.
  A positive value specifies an average and a negative value specifies
  a median.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = spline3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = spline3' -->
  <dd>Function to be fit to the spectra.  The functions are
  <span style="font-family: monospace;">"legendre"</span> (legendre polynomial), <span style="font-family: monospace;">"chebyshev"</span> (chebyshev polynomial),
  <span style="font-family: monospace;">"spline1"</span> (linear spline), and <span style="font-family: monospace;">"spline3"</span> (cubic spline).  The functions
  may be abbreviated.  The power series coefficients can only be
  calculated if <b>function</b> is <span style="font-family: monospace;">"legendre"</span> or <span style="font-family: monospace;">"chebyshev"</span>.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 1' -->
  <dd>The order of the polynomials or the number of spline pieces.
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 2., high_reject = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_reject' Line='low_reject = 2., high_reject = 0.' -->
  <dd>Rejection limits below and above the fit in units of the residual sigma.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 10' -->
  <dd>Number of rejection iterations.
  </dd>
  </dl>
  <dl id="l_grow">
  <dt><b>grow = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grow' Line='grow = 1.' -->
  <dd>When a pixel is rejected, pixels within this distance of the rejected pixel
  are also rejected.
  </dd>
  </dl>
  <dl id="l_markrej">
  <dt><b>markrej = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='markrej' Line='markrej = yes' -->
  <dd>Mark rejected points?  If there are many rejected points it might be
  desired to not mark rejected points.
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
  <dd>Graphics cursor input.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A one dimensional function is fit to the continuum of spectra in a list of
  echelle, multispec, or onedspec format images and then divided into the
  spectrum to produce continuum normalized spectra.  The first two formats
  will normalize the spectra or orders (i.e. the lines) in each image.  In
  this description the term <span style="font-family: monospace;">"spectrum"</span> will refer to a line (in whatever
  band) of an image while <span style="font-family: monospace;">"image"</span> will refer to all spectra in an image.  The
  parameters of the fit may vary from spectrum to spectrum within images and
  between images.  The fitted function may be a legendre polynomial,
  chebyshev polynomial, linear spline, or cubic spline of a given order or
  number of spline pieces.  The output image is of pixel type real.
  </p>
  <p>
  The line/band numbers (for two/three dimensional images) are written to a
  list of previously processed lines in the header keywords <i>SFIT</i> and
  <i>SFITB</i> of the output image.  A subsequent invocation of SFIT will only
  process those requested spectra that are not in this list.  This ensures
  that even if the output image is the same as the input image that no
  spectra will be processed twice and permits an easy exit from the task in
  the midst of processing many spectra without losing any work or requiring
  detailed notes.
  </p>
  <p>
  The points to be fit in each spectrum are determined by
  selecting a sample of X values specified by the parameter <i>sample</i>
  and taking either the average or median of the number of points
  specified by the parameter <i>naverage</i>.  The type of averaging is
  selected by the sign of the parameter with positive values indicating
  averaging, and the number of points is selected by the absolute value
  of the parameter.  The sample units will vary depending on the settings
  of the <b>wavescale</b> and the <b>logscale</b> parameters.  Note that a
  sample that is specified in wavelength units may be entirely outside
  the domain of the data (in pixels) if some of the spectra are not
  dispersion corrected.  The syntax of the sample specification is a comma
  separated, colon delimited list similar to the image section notation.
  For example, the <b>sample</b>, <span style="font-family: monospace;">"6550:6555,6570:6575"</span> might be used to
  fit the continuum near H-alpha.
  </p>
  <p>
  If <i>low_reject</i> and/or <i>high_reject</i> are greater than zero the
  sigma of the residuals between the fitted points and the fitted
  function is computed and those points whose residuals are less than
  <i>-low_reject</i> * sigma and greater than <i>high_reject</i> * sigma
  are excluded from the fit.  Points within a distance of <i>grow</i>
  pixels of a rejected pixel are also excluded from the fit.  The
  function is then refit without the rejected points.  This rejection
  procedure may be iterated a number of times given by the parameter
  <i>niterate</i>.  This is how the continuum is determined.
  </p>
  <p>
  If <i>replace</i> is set then any rejected points from the fitting
  are  replaced by the fit in the data before outputing the difference,
  ratio, or data.  For example with replacing the difference will
  be zero at the rejected points and the data output will be cleaned
  of deviant points.
  </p>
  <p>
  A range specification is used to select the <i>lines</i> and <i>bands</i> to be
  fit.  These parameters may either be specified with the same syntax as the
  <b>sample</b> parameter, or with the <span style="font-family: monospace;">"hyphen"</span> syntax used elsewhere in
  IRAF.  Note that a NULL range for <b>lines/bands</b> expands to <b>no</b>
  lines, not to all lines.  An asterisk (*) should be used to represent a
  range of all of the image lines/bands.  The fitting parameters (<i>sample,
  naverage, function, order, low_reject, high_reject, niterate, grow</i>)
  may be adjusted interactively if the parameter <i>interactive</i> is
  yes.  The fitting is performed with the <b>icfit</b> package.  The
  cursor mode commands for this package are described in a separate help
  entry under <span style="font-family: monospace;">"icfit"</span>.  Separate copies of the fitting parameters are
  maintained for each line so that interactive changes to the parameter
  defaults will be remembered from image to image.
  </p>
  </section>
  <section id="s_prompts">
  <h3>Prompts</h3>
  <p>
  If several images or lines/bands are specified, the user is asked whether
  to perform an interactive fit for each spectrum.  The response
  may be <b>yes, no, skip, YES, NO</b> or <b>SKIP</b>.  The meaning of each
  response is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  yes   - Fit the next spectrum interactively.
  no    - Fit the next spectrum non-interactively.
  skip  - Skip the next spectrum in this image.
  
  YES   - Interactively fit all of the spectra of
          all of the images with no further prompts.
  NO      Non-interactively fit all chosen spectra of all images.
  SKIP  - This will produce a second prompt, "Skip what?",
          with the choices:
  
          spectrum - skip this spectrum in all images
          image    - skip the rest of the current image
          all      - <b>exit</b> the program
                     This will <b>unlearn</b> the fit parameters
                     for all spectra!
          cancel  - return to the main prompt
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To normalize all orders of the echelle spectrum for hd221170
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; continuum hd221170.ec nhd221170.ec type=ratio
  </pre></div>
  <p>
  Each order of the spectrum is graphed and the interactive options for
  setting and fitting the continuum are available.  The important
  parameters are low_rejection (for an absorption spectrum), the function
  type, and the order of the function; these fit parameters are
  originally set to the defaults in the <b>continuum</b> parameter file.  A
  <span style="font-family: monospace;">'?'</span> will display a menu of cursor key options.  Exiting with <span style="font-family: monospace;">'q'</span> will
  update the output normalized order for the current image and proceed to
  the next order or image.
  </p>
  <p>
  The parameters of the fit for each order are initialized to the current
  values the first time that the order is fit.  In subsequent images, the
  parameters for a order are set to the values from the previous image.
  The first time an order is fit, the sample region is reset to the
  entire order.  Deleted points are ALWAYS forgotten from order to order
  and image to image.
  </p>
  <p>
  2.  To do several images at the same time
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; continuum spec*.imh c//spec*.imh
  </pre></div>
  <p>
  Note how the image template concatenation operator is used to construct
  the output list of spectra.  Alternatively:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; continuum @inlist @outlist
  </pre></div>
  <p>
  where the two list files could have been created with the sections
  command or by editing.
  </p>
  <p>
  3.  To measure the power law slope of the continuum (fluxed data)
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; continuum uv.* type=ratio logscale+ listonly+ fun=leg order=2
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_CONTINUUM">
  <dt><b>CONTINUUM V2.10.4</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='CONTINUUM' Line='CONTINUUM V2.10.4' -->
  <dd>The task was expanded to include fitting specified bands in 3D multispec
  spectra.
  The task was expanded to include long slit and spectral cube data.
  </dd>
  </dl>
  <dl id="l_CONTINUUM">
  <dt><b>CONTINUUM V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='CONTINUUM' Line='CONTINUUM V2.10' -->
  <dd>This task was changed from a script based on <b>images.fit1d</b> to a
  task based on <b>sfit</b>.  This provides for individual independent
  continuum fitting in multiple spectra images and for additional
  flexibility and record keeping.  The parameters have been largely
  changed.
  </dd>
  </dl>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The errors are not listed for the power series coefficients.
  </p>
  <p>
  Spectra that are updated when <b>logscale</b> is yes are written with a
  linear wavelength scale, but with a log normalized data value.
  </p>
  <p>
  Selection by aperture number is not supported.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  sfit, fit1d, icfit, ranges
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'PROMPTS' 'EXAMPLES' 'REVISIONS' 'BUGS' 'SEE ALSO'  -->
  

.. _sarith:

sarith: Spectrum arithmetic
===========================

**Package: irs**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  sarith input1 op input2 output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input1">
  <dt><b>input1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input1' Line='input1' -->
  <dd>List of input images to be used as operands.
  </dd>
  </dl>
  <dl id="l_op">
  <dt><b>op    </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='op' Line='op    ' -->
  <dd>Operator to be applied to the first operand or to both operands.  The
  unary or single operand operators are:
  <div class="highlight-default-notranslate"><pre>
  abs  - absolute value
  copy - copy (see also <b>scopy</b>)
  dex  - decimal exponentiation (antilog of base 10 logarithm)
  exp  - base e exponentiation (antilog of natural logarithm)
  flam - convert F-nu to F-lambda
  fnu  - convert F-lambda to F-nu
  inv  - inverse
  ln   - natural logarithm
  log  - base 10 logarithm
  lum  - convert magnitude to luminosity
  mag  - convert luminosity to magnitude
  sqrt - square root
  </pre></div>
  The binary or two operand operators are:
  <div class="highlight-default-notranslate"><pre>
  replace - replace first operand values by second operand values
  +       - addition
  -       - subtraction
  *       - multiplication
  /       - division
  ^       - exponentiation
  </pre></div>
  </dd>
  </dl>
  <dl id="l_input2">
  <dt><b>input2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input2' Line='input2' -->
  <dd>Lists of input spectra or constants to be used as second operands for
  binary operations.  If a single value is specified it applies
  to all the first operand input images otherwise the list must match
  the first operand list in number.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of resultant output images or root names.  Image
  sections are ignored and if the output format is <span style="font-family: monospace;">"onedspec"</span> then any record
  extensions are stripped to form the root name.  If no output list is
  specified then the input list is used and the input images are replaced by
  the resultant spectra.  If a single output name is specified then all
  resultant spectra are written to the same output image or image root
  name.  This allows packing or merging multiple spectra and requires
  properly setting the <i>clobber</i>, <i>merge</i>, <i>renumber</i> and
  <i>offset</i> parameters to achieve the desired output.  If more than one
  output image is specified then it must match the input image list in
  number.
  </dd>
  </dl>
  <dl id="l_w1">
  <dt><b>w1 = INDEF, w2 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='w1' Line='w1 = INDEF, w2 = INDEF' -->
  <dd>Starting and ending wavelengths to be copied.  If <i>w1</i> is not specified
  then the wavelength of the starting edge of the first pixel is used
  (wavelength at pixel coordinate 0.5) and if <i>w2</i> is not specified then
  the wavelength of the ending edge of the last pixel is used (wavelength of
  the last pixel plus 0.5).  If both are not specified, that is set to INDEF,
  then the whole spectrum is copied and the <i>rebin</i> parameter is
  ignored.  Note that by specifying both endpoints the copied region can be
  set to have increasing or decreasing wavelength per pixel.  If the spectrum
  only partially covers the specified range only that portion of the spectrum
  within the range is copied.  It is an error if the range is entirely
  outside that of a spectrum.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span>, beams = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = "", beams = ""' -->
  <dd>List of apertures and beams to be selected from the input spectra.  The
  logical intersection of the two lists is selected.  The null list
  selects all apertures or beams.  A list consists of comma separated
  numbers and ranges of numbers.  A range is specified by a hyphen.  An
  optional step size may be given by <span style="font-family: monospace;">'x'</span> followed by a number.
  See <b>xtools.ranges</b> for more information.  If the first character
  is <span style="font-family: monospace;">"!"</span> then the apertures/beams not in the list are selected.  Note
  that a <span style="font-family: monospace;">"!"</span> in either of the lists complements the intersection of the
  two lists.
  For longslit input spectra the aperture numbers
  selects the lines or columns to be extracted.  For 3D Fabry-Perot
  spectra the aperture numbers select the first spatial axis.
  </dd>
  </dl>
  <dl id="l_bands">
  <dt><b>bands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bands' Line='bands = ""' -->
  <dd>List of bands in 3D multispec.
  For 3D spatial spectra the band parameter applies to the second
  spatial axis.
  The null list selects all bands.  The syntax is as described above.
  </dd>
  </dl>
  <dl id="l_apmodulus">
  <dt><b>apmodulus = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apmodulus' Line='apmodulus = 0' -->
  <dd>Modulus to be applied to the input aperture numbers before matching against
  the aperture list.  If zero then no modulus is used.  This is used to
  select apertures which are related by the same modulus, typically a
  factor of 10; for example, 10, 1010, and 2010 with a modulus of 1000 are
  related.
  </dd>
  </dl>
  <dl id="l_reverse">
  <dt><b>reverse = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reverse' Line='reverse = no' -->
  <dd>Reverse the order of the operands in a binary operation?  Because the first
  operand is used as the image header template, dispersion coordinate
  template, and output image in the case of a null output list it  must be an
  image and not a constant.  To allow certain operations, for
  example subtracting a spectra from a constant or using the subtractand as
  the dispersion coordinate template, the reverse option is used to reverse
  the order of the operands in a binary operation.
  </dd>
  </dl>
  <dl id="l_ignoreaps">
  <dt><b>ignoreaps = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ignoreaps' Line='ignoreaps = no' -->
  <dd>Ignore aperture numbers in the second operand?  Normally, spectra in
  binary operations must have matching aperture numbers, otherwise an
  error is printed.  If this parameter is yes then the spectra are matched
  by line number with the last line being used if the second operand spectrum
  has fewer lines than the first operand spectrum.  This is generally
  used to allow using a single spectrum with multiple aperture spectra.
  </dd>
  </dl>
  <dl id="l_format">
  <dt><b>format = <span style="font-family: monospace;">"multispec"</span> (multispec|onedspec)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='format' Line='format = "multispec" (multispec|onedspec)' -->
  <dd>Output image format and name syntax.  The <span style="font-family: monospace;">"multispec"</span> format consists of
  one or more spectra in the same image file.  The <span style="font-family: monospace;">"onedspec"</span> format consists
  of a single spectrum per image with names having a root name and a four
  digit aperture number extension.  Note that converting to <span style="font-family: monospace;">"onedspec"</span> format
  from three dimensional images where the third dimension contains associated
  spectra will not include data from the extra dimension.  Image sections may
  be used in this case.
  </dd>
  </dl>
  <dl id="l_renumber">
  <dt><b>renumber = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='renumber' Line='renumber = no' -->
  <dd>Renumber the output aperture numbers?  If set the output aperture
  numbers, including any preexisting spectra when merging, are renumbered
  beginning with 1.  The <i>offset</i> parameter may be used to
  change the starting number.
  </dd>
  </dl>
  <dl id="l_offset">
  <dt><b>offset = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='offset' Line='offset = 0' -->
  <dd>Offset to be added to the input or renumbered aperture number to form
  the final output aperture number.
  </dd>
  </dl>
  <dl id="l_clobber">
  <dt><b>clobber = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clobber' Line='clobber = no' -->
  <dd>Modify an existing output image either by overwriting or merging?
  </dd>
  </dl>
  <dl id="l_merge">
  <dt><b>merge = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='merge' Line='merge = no' -->
  <dd>Merge apertures into existing spectra?  This
  requires that the <i>clobber</i> parameter be set.  If not merging
  then the selected spectra entirely replace those in existing output images.
  If merging then the input spectra replace those in the output image
  with the same aperture number and new apertures are added if not present.
  </dd>
  </dl>
  <dl id="l_rebin">
  <dt><b>rebin = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rebin' Line='rebin = yes' -->
  <dd>Rebin the spectrum to the exact wavelength range specified by the <i>w1</i>
  and <i>w2</i> parameters?  If the range is given as INDEF for both endpoints
  this parameter does not apply.  If a range is given and this parameter is
  not set then the pixels in the specified range (using the nearest pixels to
  the endpoint wavelengths) are copied without rebinning.  In this case the
  wavelength of the first pixel may not be exactly that specified by <i>w1</i>
  and the dispersion, including non-linear dispersions, is unchanged.  If
  this parameter is set the spectra are interpolated to have the first and
  last pixels at exactly the specified endpoint wavelengths while preserving
  the same number of pixels in the interval.  Linear and log-linear
  dispersion types are maintained while non-linear dispersions are
  linearized.
  </dd>
  </dl>
  <dl id="l_errval">
  <dt><b>errval = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='errval' Line='errval = 0.' -->
  <dd>Value for resultant pixel if an arithmetic error occurs such as dividing
  by zero or the square root of a negative number.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print a record of each operation?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Sarith</b> performs arithmetic operations on spectra.  It is
  distinguished from <b>imarith</b> in that it includes unary operators, like
  <b>imfunction</b> but with some specific to astronomical spectra, and binary
  operations between two spectra are performed in dispersion coordinate space
  (typically wavelength) rather than logical pixel space.  In the latter case
  the spectra are checked for matching dispersion functions (which are not
  necessarily linear) and, if they don't match, the second operand is
  interpolated without flux conservation.  (If flux conservation is desired
  then the task <b>dispcor</b> should be used first.) Thus, the spectra may
  have different dispersion functions but the arithmetic is done at matching
  wavelengths.  The default interpolation function is a 5th order
  polynomial.  The choice of interpolation type is made with the package
  parameter <span style="font-family: monospace;">"interp"</span>.  It may be set to <span style="font-family: monospace;">"nearest"</span>, <span style="font-family: monospace;">"linear"</span>, <span style="font-family: monospace;">"spline3"</span>,
  <span style="font-family: monospace;">"poly5"</span>, or <span style="font-family: monospace;">"sinc"</span>.  Remember that this applies to all tasks which might
  need to interpolate spectra in the <b>onedspec</b> and associated packages.
  For a discussion of interpolation types see <b>onedspec</b>.
  </p>
  <p>
  The unary operators operate on the spectra in the first operand list to
  produce the specified output spectra, which may be the same as the
  input spectra.  The operators include:
  </p>
  <div class="highlight-default-notranslate"><pre>
  abs  - absolute value
  copy - copy (see also <b>scopy</b>)
  dex  - decimal exponentiation (antilog of base 10 logarithm)
  exp  - base e exponentiation (antilog of natural logarithm)
  flam - convert F-nu to F-lambda
  fnu  - convert F-lambda to F-nu
  inv  - inverse
  ln   - natural logarithm
  log  - base 10 logarithm
  lum  - convert magnitude to luminosity
  mag  - convert luminosity to magnitude
  sqrt - square root
  </pre></div>
  <p>
  The luminosity to magnitude and magnitude to luminosity operators are
  based on the standard relation:
  </p>
  <div class="highlight-default-notranslate"><pre>
  mag = -2.5 * log (lum)
  </pre></div>
  <p>
  where the log is base 10.  The F-nu to F-lambda and F-lambda to F-nu
  operators are based on the relation:
  </p>
  <div class="highlight-default-notranslate"><pre>
  F-nu = F-lambda * lambda / nu
  </pre></div>
  <p>
  where lambda is wavelength and nu is frequency (currently the wavelength
  is assumed to be Angstroms and so F-lambda is in units of per Angstrom
  and F-nu is in units of per Hertz).  In all the operators it is the
  responsibility of user as to the appropriateness of the operator to
  the input.
  </p>
  <p>
  The binary operators operate on the spectra in the first operand list
  and the spectra or numerical constants in the second operand.  Numeric
  constants are equivalent to spectra having the specified value at all
  pixels.  The binary operators are the standard arithmetic ones plus
  exponentiation and replacement:
  </p>
  <div class="highlight-default-notranslate"><pre>
  replace - replace first operand values by second operand values
  +       - addition
  -       - subtraction
  *       - multiplication
  /       - division
  ^       - exponentiation
  </pre></div>
  <p>
  If the second operand is a spectrum, as mentioned previously, it is
  interpolated, without flux conservation, to the dispersion
  function of the first operand spectrum if necessary.
  </p>
  <p>
  There is a distinctions between the first operand and the second operand.
  The first operand must always be a spectrum.  It supplies the dispersion
  function to be matched by the second operand spectrum.  It also supplies
  a copy of it's image header when a new output spectrum is created.
  In cases where it is desired to have the second operand be the
  dispersion/header reference and/or the first operand be a constant
  the <i>reverse</i> parameter is used.  For example to subtract a
  spectrum from the constant 1:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sarith 1 - spec invspec reverse+
  </pre></div>
  <p>
  or to subtract two spectra using the subtractand as the dispersion
  reference:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sarith spec1 - spec2 diff reverse+
  </pre></div>
  <p>
  When a binary operation on a pair of spectra is performed the aperture
  numbers may be required to be the same if <i>ignoreaps</i> is no.  For
  images containing multiple spectra the apertures need not be in the
  same order but only that matching apertures exist.  If this parameter
  is set to yes then aperture numbers are ignored when the operation is
  performed.  For multiple spectra images the second operand spectra
  are matched by image line number rather than by aperture.  If the
  second operand image has fewer lines, often just one line, then the
  last line is used repeatedly.  This feature allows multiple spectra
  in the primary operand list to be operated upon by a single spectrum;
  for example to subtract one spectrum from all spectra in the
  in a multiple spectrum image.
  </p>
  <p>
  If it is an error to perform an operation on certain data values, for
  example division by zero or the square root of a negative number,
  then the output value is given the value specified by the parameter
  <i>errval</i>.
  </p>
  <p>
  A log of the operations performed may be printed to the standard
  output, which may then be redirected if desired, if the <i>verbose</i>
  parameter is set.  In the output the last bracketed number is the
  aperture number of the spectrum.
  </p>
  <p>
  INPUT/OUTPUT
  </p>
  <p>
  The arithmetic part of <b>sarith</b> is fairly straightforward and
  intuitive.  The selection of input spectra from input images and
  the placing of output spectra in output images can be more confusing
  because there are many possibilities.  This section concentrates
  on the topics of the input and output.  Since the concepts apply to all
  of the operators it simplifies things to think in terms of copying
  input spectra to output spectra; the <span style="font-family: monospace;">"copy"</span> operator.  Note that the
  task <b>scopy</b> is actually just this case of <b>sarith</b> with
  parameters set for copying.  While the discussion here is similar
  to that in the help for <b>scopy</b>, the examples for that task
  are more focused for illustrating this topic than the <b>sarith</b>
  examples which concentrate more on the arithmetic aspects of 
  the task.
  </p>
  <p>
  Input spectra are specified by an image list which may include explicit
  image names, wildcard templates and @files containing image names.
  The image names may also include image sections such as to select portions of
  the wavelength coverage.  The input images may be either one or two
  dimensional spectra.  One dimensional spectra may be stored in
  individual one dimensional images or as lines in two (or three)
  dimensional images.  The one dimensional spectra are identified by
  an aperture number, which must be unique within an image, and a beam number.
  Two dimensional long slit and three dimensional Fabry-Perot spectra are
  treated, for the purpose of this
  task, as a collection of spectra with dispersion either along any axis
  specified by the DISPAXIS image header parameter
  or the <i>dispaxis</i> package parameter.  The aperture and band
  parameters specify a spatial position.  A number of adjacent
  lines, columns, and bands, specified by the <i>nsum</i> package parameter,
  will be summed to form an aperture spectrum.  If number is odd then the
  aperture/band number refers to the middle and if it is even it refers to the
  lower of the two middle lines or columns.
  </p>
  <p>
  In the case of many spectra each stored in separate one dimensional
  images, the image names may be such that they have a common root name
  and a four digit aperture number extension.  This name syntax is
  called <span style="font-family: monospace;">"onedspec"</span> format.  Including such spectra in an
  input list may be accomplished either with wildcard templates such as
  </p>
  <div class="highlight-default-notranslate"><pre>
  name*
  name.????.imh
  </pre></div>
  <p>
  where the image type extension <span style="font-family: monospace;">".imh"</span> must be given to complete the
  template but the actual extension could also be that for an STF type
  image, or using an @file prepared with the task <b>names</b>.
  To generate this syntax for output images the <i>format</i> parameter
  is set to <span style="font-family: monospace;">"onedspec"</span> (this will be discussed further later).
  </p>
  <p>
  From the input images one may select a range of wavelengths with the
  <i>w1</i> and <i>w2</i> parameters and a subset of spectra based on aperture and
  beam numbers using the <i>aperture</i> and <i>beam</i> parameters.
  If the wavelength range is specified as INDEF the full spectra are
  used without any resampling.  If the aperture and beam lists are not
  specified, an empty list, then all apertures and beams are selected.  The
  lists may be those spectra desired or the complement obtained by prefixing
  the list with <span style="font-family: monospace;">'!'</span>.  Only the selected wavelength range and spectra will
  be operated upon and passed on to the output images.
  </p>
  <p>
  Specifying a wavelength range is fairly obvious except for the question
  of pixel sampling.  Either the pixels in the specified range are used
  without resampling or the pixels are resampled to correspond eactly
  to the requested range.  The choice is made with the <i>rebin</i> parameter.
  In the first case the nearest pixels to the specified wavelength
  endpoints are determined and those pixels and all those in between
  are used.  The dispersion relation is unchanged.  In the second case
  the spectra are reinterpolated to have the specified starting and
  ending wavelengths with the same number of pixels between those points
  as in the original spectrum.  The reinterpolation is done in either
  linear or log-linear dispersion.  The non-linear dispersion functions
  are interpolated to a linear dispersion.
  </p>
  <p>
  Using <b>sarith</b> with long slit and Fabry-Perot images provides a quick
  and simple type of extraction as opposed to using the <b>apextract</b>
  package.  When summing it is often desired to start each aperture after the
  number of lines summed.  To do this specify a step size in the aperture/band
  list.  For example to extract columns 3 to 23 summing every 5 columns you
  would use an aperture list of <span style="font-family: monospace;">"3-23x5"</span> and an <i>nsum</i> of 5.  If you do
  not use the step in the aperture list you would extract the sum of columns
  1 to 5, then columns 2 to 6, and so on.
  </p>
  <p>
  In the special case of subapertures extracted by <b>apextract</b>, related
  apertures are numbered using a modulus; for example apertures
  5, 1005, 2005.  To allow selecting all related apertures using a single
  aperture number the <i>apmodulus</i> parameter is used to specify the
  modulus factor; 1000 in the above example.  This is a very specialized
  feature which should be ignored by most users.
  </p>
  <p>
  The output list of images may consist of an empty list, a single image,
  or a list of images matching the input list in number.  Note that it
  is the number of image names that matters and not the number of spectra
  since there may be any number of spectra in an image.  The empty list
  converts to the same list as the input and is shorthand for replacing
  the input image with the output image upon completion; therefore it
  is equivalent to the case of a matching list.  If the input
  consists of just one image then the distinction between a single
  output and a matching list is moot.  The interesting distinction is
  when there is an input list of two or more images.  The two cases
  are then a mapping of many-to-many or many-to-one.  Note that it is
  possible to have more complex mappings by repeating the same output
  name in a matching list provided clobbering, merging, and possibly
  renumbering is enabled.
  </p>
  <p>
  In the case of a matching list, spectra from different input images
  will go to different output images.  In the case of a single output
  image all spectra will go to the same output image.  Note that in
  this discussion an output image when <span style="font-family: monospace;">"onedspec"</span> format is specified
  is actually a root name for possibly many images.  However,
  it should be thought of as a single image from the point of view
  of image lists.
  </p>
  <p>
  When mapping many spectra to a single output image, which may have existing
  spectra if merging, there may be a conflict with repeated aperture
  numbers.  One option is to consecutively renumber the aperture numbers,
  including any previous spectra in the output image when merging and then
  continuing with the input spectra in the order in which they are selected.
  This is specified with the <i>renumber</i> parameter which renumbers
  beginning with 1.
  </p>
  <p>
  Another options which may be used independently of renumbering or in
  conjunction with it is to add an offset as specified by the <i>offset</i>
  parameter.  This is last step in determining the output aperture
  numbers so that if used with the renumber option the final aperture
  numbers begin with one plus the offset.
  </p>
  <p>
  It has been mentioned that it is possible to write and add to
  existing images.  If an output image exists an error will be
  printed unless the <i>clobber</i> parameter is set.  If clobbering
  is allowed then the existing output image will be replaced by the
  new output.  Rather than replacing an output image sometimes one
  wants to replace certain spectra or add new spectra.  This is
  done by selecting the <i>merge</i> option.  In this case if the output
  has a spectrum with the same aperture number as the input spectrum
  it is replaced by the input spectrum.  If the input spectrum aperture
  number is not in the output then the spectrum is added to the output
  image.  To add spectra with the same aperture number and not
  replace the one in the output use the <i>renumber</i> or
  <i>offset</i> options.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  In addition to the examples in this section there are many examples
  in the help for <b>scopy</b> which illustrate aspects of selecting
  input spectra and producing various types of output.  Those examples
  are equivalent to using the <span style="font-family: monospace;">"copy"</span> operator.  The same examples will
  also apply with other operators where the input spectra are modified
  arithmetically before being copied to the output images.
  </p>
  <p>
  I.  SIMPLE EXAMPLES
  </p>
  <p>
  The simple examples use only a single input image and create a new
  output image.
  </p>
  <p>
  1.  Examples of unary operations:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sarith example1 mag "" magexample
  cl&gt; sarith magexample lum "" example2
  cl&gt; sarith example1 log "" logexample
  </pre></div>
  <p>
  Note that a place holder for the second operand is required on the command
  line which will be ignored.
  </p>
  <p>
  2.  Examples of binary operations using constants:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sarith example1 + 1000 example2
  cl&gt; sarith example1 - 1000 example2 reverse+
  cl&gt; sarith example1 / 1000 example2
  cl&gt; sarith example1 ** 2 example2
  </pre></div>
  <p>
  3.  Examples of binary operations between spectra with matching apertures:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sarith example1 + example2 example3
  cl&gt; sarith example1 - example2 example3
  </pre></div>
  <p>
  4.  Example of binary operations between spectra with the second image
  consisting of a single spectrum:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sarith example1 / flatspec flatexample1 ignore+ errval=1
  </pre></div>
  <p>
  II.  MORE COMPLEX EXAMPLES
  </p>
  <p>
  5.  Unary and constant operations on a list of images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sarith example* fnu "" %example%fnu%
  cl&gt; sarith example* + 1000 %example%fnu%
  </pre></div>
  <p>
  6.  Binary operations on a list of images using a single second operand
  with matching apertures:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sarith example* - skyspec %example%skysub%*
  </pre></div>
  <p>
  7.  Selecting apertures to operate upon:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sarith example* - skyspec %example%skysub%* aper=1,5,9
  </pre></div>
  <p>
  8.  Extract the sum of each 10 columns in a long slit spectrum and normalize
  by the central spectrum:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; nsum = "10"
  cl&gt; sarith longslit copy "" longslit.ms aper=5-500x10
  longslit[5]  --&gt;  longslit.ms[5]
  longslit[15]  --&gt;  longslit.ms[15]
  longslit[25]  --&gt;  longslit.ms[25]
  ...
  cl&gt; sarith longslit.ms / longslit.ms[*,25] norm ignore+
  longslit.ms[5]  /  longslit.ms[*,25][245]  --&gt;  norm[5]
  longslit.ms[15]  /  longslit.ms[*,25][245]  --&gt;  norm[15]
  longslit.ms[25]  /  longslit.ms[*,25][245]  --&gt;  norm[25]
  ...
  </pre></div>
  <p>
  9.  In place operations:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sarith example* + 1000 example* clobber+
  example1[1]  +  1000.  --&gt;  example1[1]
  example1[2]  +  1000.  --&gt;  example1[2]
  ...
  example2[1]  +  1000.  --&gt;  example2[1]
  example2[2]  +  1000.  --&gt;  example2[2]
  ...
  cl&gt; sarith example* flam "" example* clobber+
  example1[1]  -- flam --&gt;  example1[1]
  example1[2]  -- flam --&gt;  example1[2]
  ...
  example2[1]  -- flam --&gt;  example2[1]
  example2[2]  -- flam --&gt;  example2[2]
  ...
  cl&gt; sarith example* - skyspec "" clobber+ ignore+
  example1[1]  +  skyspec[1]  --&gt;  example1[1]
  example1[2]  +  skyspec[1]  --&gt;  example1[2]
  ...
  example2[1]  +  skyspec[1]  --&gt;  example2[1]
  example2[2]  +  skyspec[1]  --&gt;  example2[2]
  ...
  </pre></div>
  <p>
  10.  Merging existing spectra with the results of operations:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; sarith example* / flat "" clobber+ merge+ renum+ ignor+
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_SARITH">
  <dt><b>SARITH V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SARITH' Line='SARITH V2.11' -->
  <dd>Previously both w1 and w2 had to be specified to select a range to
  be used.  Now if only one is specified the second endpoint defaults
  to the first or last pixel.
  The noise band in multispec data is only copied from the primary
  spectrum and not modified.  This is a kludge until the noise is
  handled properly.
  </dd>
  </dl>
  <dl id="l_SARITH">
  <dt><b>SARITH V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SARITH' Line='SARITH V2.10.3' -->
  <dd>Additional support for 3D multispec/equispec or spatial spectra has been
  added.  The <span style="font-family: monospace;">"bands"</span> parameter allows selecting specific bands and
  the onedspec output format creates separate images for each selected
  aperture and band.
  </dd>
  </dl>
  <dl id="l_SARITH">
  <dt><b>SARITH V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SARITH' Line='SARITH V2.10' -->
  <dd>This task is new.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  scopy, splot, imarith, imfunction
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

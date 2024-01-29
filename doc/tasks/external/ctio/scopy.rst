.. _scopy:

scopy: Copy spectra including aperture selection and format changes
===================================================================

**Package: ctio**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  scopy input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images containing spectra to be copied.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output image names or root names.  Image
  sections are ignored and if the output format is <span style="font-family: monospace;">"onedspec"</span> then any record
  extensions are stripped to form the root name.  If no output list is
  specified then the input list is used and the input images are replaced by
  the copied output spectra.  If a single output name is specified then all
  copied spectra are written to the same output image or image root
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
  two lists.  For longslit input spectra the aperture numbers
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
  the aperture list.  If zero then no modulus is used.  This is allows
  selecting apertures which are related by the same modulus, typically a
  factor of 10; for example, 10, 1010 and 2010 with a modulus of 1000 are
  related.
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
  be used in that case.
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
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print a record of each aperture copied?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Scopy</b> selects regions of spectra from an input list of spectral
  images and copies them to output images.  This task can be used to extract
  aperture spectra from long slit and Fabry-Perot images and to select,
  reorganize, merge, renumber, pack, and unpack spectra in many ways.  Below
  is a list of some of the uses and many examples are given in the EXAMPLES
  section.
  </p>
  <div class="highlight-default-notranslate"><pre>
  o Pack many spectra into individual images into a single image
  o Unpack images with multiple spectra into separate images
  o Extract a set of lines or columns from long slit spectra
  o Extract a set of spatial positions from Fabry-Perot spectra
  o Extract specific wavelength regions
  o Select a subset of spectra to create a new image
  o Merge a subset of spectra into an existing image
  o Combine spectra from different images into one image
  o Renumber apertures
  </pre></div>
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
  copied without any resampling.  If the aperture and beam lists are not
  specified, an empty list, then all apertures and beams are selected.  The
  lists may be those spectra desired or the complement obtained by prefixing
  the list with <span style="font-family: monospace;">'!'</span>.  Only the selected wavelength range and spectra will
  be operated upon and passed on to the output images.
  </p>
  <p>
  Specifying a wavelength range is fairly obvious except for the question
  of pixel sampling.  Either the pixels in the specified range are copied
  without resampling or the pixels are resampled to correspond eactly
  to the requested range.  The choice is made with the <i>rebin</i> parameter.
  In the first case the nearest pixels to the specified wavelength
  endpoints are determined and those pixels and all those in between
  are copied.  The dispersion relation is unchanged.  In the second case
  the spectra are reinterpolated to have the specified starting and
  ending wavelengths with the same number of pixels between those points
  as in the original spectrum.  The reinterpolation is done in either
  linear or log-linear dispersion.  The non-linear dispersion functions
  are interpolated to a linear dispersion.
  </p>
  <p>
  Using <b>scopy</b> with long slit or Fabry-Perot images provides a quick and
  simple type of extraction as opposed to using the <b>apextract</b> package.
  When summing it is often desired to start each aperture after the number of
  lines summed.  To do this specify a step size in the aperture/band list.  For
  example to extract columns 3 to 23 summing every 5 columns you would use an
  aperture list of <span style="font-family: monospace;">"3-23x5"</span> and an <i>nsum</i> of 5.  If you do not use the
  step in the aperture list you would extract the sum of columns 1 to 5, then
  columns 2 to 6, and so on.
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
  <p>
  To print a record as each input spectrum is copied the <i>verbose</i>
  parameter may be set.  The syntax is the input image name followed
  by the aperture number in [].  An arrow then points to the output
  image name with the final aperture number also in [], except for
  <span style="font-family: monospace;">"onedspec"</span> format where the image name extension gives the aperture
  number.  It is important to remember that it is the aperture numbers
  which are shown and not the image lines; there is not necessarily any
  relation between image lines and aperture numbers though often they
  are the same.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Because there are so many possiblities there are many examples.  To
  help find examples close to those of interest they are divided into
  three sections; examples involving standard multispec images only, examples
  with onedspec format images, and examples with long slit and Fabry-Perot
  images.  In the examples the verbose flag is set to yes and the output is
  shown.
  </p>
  <p>
  I.   MULTISPEC IMAGES
  </p>
  <p>
  The examples in this section deal with the default spectral format of
  one or more spectra in an image.  Note that the difference between
  a <span style="font-family: monospace;">"onedspec"</span> image and a <span style="font-family: monospace;">"multispec"</span> image with one spectrum is purely
  the image naming syntax.
  </p>
  <p>
  1.  Select a single spectrum (aperture 3):
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy example1 ap3 aperture=3
  example1[3]  --&gt;  ap3[3]
  </pre></div>
  <p>
  2.  Select a wavelength region from a single spectrum:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy example1 ap3 aperture=3 w1=5500 w2=6500
  example1[3]  --&gt;  ap3[3]
  </pre></div>
  <p>
  3.  Select a subset of spectra (apertures 1, 2, 4, 6, and 9): 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy example1 subset apertures="1-2,4,6-9x3"
  example1[1]  --&gt;  subset[1]
  example1[2]  --&gt;  subset[2]
  example1[4]  --&gt;  subset[4]
  example1[6]  --&gt;  subset[6]
  example1[9]  --&gt;  subset[9]
  </pre></div>
  <p>
  This example shows various features of the aperture list syntax.
  </p>
  <p>
  4.  Select the same apertures (1 and 3) from multiple spectra and in the
  same wavelength region:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy example* %example%subset%* apertures=1,3 w1=5500 w2=6500
  example1[1]  --&gt;  subset1[1]
  example1[3]  --&gt;  subset1[3]
  example2[1]  --&gt;  subset2[1]
  example2[3]  --&gt;  subset2[3]
  ...
  </pre></div>
  <p>
  The output list uses the pattern substitution feature of image templates.
  </p>
  <p>
  5.  Select the same aperture from multiple spectra and pack them in a
  a single image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy example* ap2 aperture=2 renumber+
  example1[2]  --&gt;  ap2[1]
  example2[2]  --&gt;  ap2[2]
  example3[2]  --&gt;  ap2[3]
  ...
  </pre></div>
  <p>
  6.  To renumber the apertures sequentially starting with 11:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy example1 renum renumber+
  example1[1]  --&gt;  renum[11]
  example1[5]  --&gt;  renum[12]
  example1[9]  --&gt;  renum[13]
  ...
  </pre></div>
  <p>
  7.  To replace apertures (2) in one image with that from another:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy example1 example2 aperture=2 clobber+ merge+
  example1[2]  --&gt; example2[2]
  </pre></div>
  <p>
  8.  To merge two sets of spectra with different aperture numbers into
      one image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy example![12]* merge
  example1[1]  -&gt;  merge[1]
  example1[3]  -&gt;  merge[3]
  ...
  example2[2]  -&gt;  merge[2]
  example2[4]  -&gt;  merge[4]
  ...
  </pre></div>
  <p>
  The input list uses the ![] character substitution syntax of image templates.
  </p>
  <p>
  9.  To merge a set of spectra with the same aperture numbers into another
  existing image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy example2 example1 clobber+ merge+ renumber+
  example1[5]  --&gt;  example1[2]
  example1[9]  --&gt;  example1[3]
  example2[1]  --&gt;  example1[4]
  example2[5]  --&gt;  example1[5]
  example2[9]  --&gt;  example1[6]
  </pre></div>
  <p>
  Both images contained apertures 1, 5, and 9.  The listing does not show
  the renumbering of the aperture 1 from example1 since the aperture number
  was not changed.
  </p>
  <p>
  10.  Select parts of a 3D image where the first band is the
  variance weighted extraction, band 2 is nonweighted extraction,
  band 3 is the sky, and band 4 is the sigma:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy example3d.ms[*,*,1] var1.ms
  example3d.ms[*,*,1][1]  --&gt;  var1.ms[1]
  example3d.ms[*,*,1][2]  --&gt;  var1.ms[2]
  ...
  cl&gt; scopy example3d.ms[10:400,3,3] skyap3
  example3d.ms[10:400,3,3][3]  --&gt;  skyap3[3]
  cl&gt; scopy example3d.ms[*,*,1] "" clobber+
  example3d.ms[*,*,1][1]  --&gt;  example3d.ms[1]
  example3d.ms[*,*,1][2]  --&gt;  example3d.ms[2]
  ...
  </pre></div>
  <p>
  Note that this could also be done with <b>imcopy</b>.  The last example
  is done in place; i.e. replacing the input image by the output image
  with the other bands eliminatated; i.e. the output image is two dimensional.
  </p>
  <p>
  II.  ONEDSPEC IMAGES
  </p>
  <p>
  1.  Expand a multi-spectrum image to individual single spectrum images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy example1 record format=onedspec
  example1[1]  --&gt;  record.0001
  example1[5]  --&gt;  record.0005
  example1[9]  --&gt;  record.0009
  ...
  </pre></div>
  <p>
  2.  Pack a set of individual 1D spectra into a single image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy record.????.imh record.ms
  record.0001[1]  --&gt;  record.ms[1]
  record.0005[5]  --&gt;  record.ms[5]
  record.0009[9]  --&gt;  record.ms[9]
  ...
  </pre></div>
  <p>
  3.  Copy a set of record syntax spectra to a different rootname and renumber:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy record.????.imh newroot format=onedspec
  record.0001[1]  --&gt;  newroot.0001
  record.0005[5]  --&gt;  newroot.0002
  record.0009[9]  --&gt;  newroot.0003
  ...
  </pre></div>
  <p>
  III. LONG SLIT IMAGES
  </p>
  <p>
  To define the dispersion axis either the image header parameter DISPAXIS
  must be set (using HEDIT for example) or a the package <i>dispaxis</i>
  parameter must be set.  In these examples the output is the default
  multispec format.
  </p>
  <p>
  1.  To extract column 250 into a spectrum:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy longslit1 c250 aperture=250
  longslit1[250]  --&gt;  c250[250]
  </pre></div>
  <p>
  2.  To sum and extract every set of 10 columns:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; nsum = 10  (or epar the package parameters)
  cl&gt; scopy longslit1 sum10 apertures=5-500x10
  longslit1[5]  --&gt;  sum10[5]
  longslit1[15]  --&gt;  sum10[15]
  longslit1[25]  --&gt;  sum10[25]
  ...
  </pre></div>
  <p>
  3.  To extract the sum of 10 columns centered on column 250 from a set
  of 2D images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; nsum = 10  (or epar the package parameters)
  cl&gt; scopy longslit* %longslit%c250.%* aperture=250
  longslit1[250]  --&gt;  c250.1[250]
  longslit2[250]  --&gt;  c250.2[250]
  longslit3[250]  --&gt;  c250.3[250]
  ...
  </pre></div>
  <p>
  4.  To extract the sum of 10 columns centered on column 250 from a set of
  2D images and merge them into a single, renumbered output image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; nsum = 10  (or epar the package parameters)
  cl&gt; scopy longslit* c250 aperture=250 renum+
  longslit1[250]  --&gt;  c250[1]
  longslit2[250]  --&gt;  c250[2]
  longslit3[250]  --&gt;  c250[3]
  ...
  </pre></div>
  <p>
  IV. FABRY-PEROT IMAGES
  </p>
  <p>
  To define the dispersion axis either the image header parameter DISPAXIS
  must be set (using HEDIT for example) or a the package <i>dispaxis</i>
  parameter must be set.  In these examples the output is the default
  multispec format.
  </p>
  <p>
  1.  To extract a spectrum from the spatial position (250,250) where
  dispaxis=3:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; scopy fp1 a250 aperture=250 band=250
  longslit1[250]  --&gt;  a250[250]
  </pre></div>
  <p>
  2.  To sum and extract every set of 10 lines and bands (dispaxis=1):
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; nsum = "10"
  cl&gt; scopy fp1 sum10 apertures=5-500x10 bands=5-500x10
  longslit1[5]  --&gt;  sum10[5]
  longslit1[15]  --&gt;  sum10[15]
  longslit1[25]  --&gt;  sum10[25]
  ...
  </pre></div>
  <p>
  3.  To extract the sum of 10 columns and 20 lines centered on column 250 and
  line 100 from a set of 3D images with dispaxis=3:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; nsum = "10 20"
  cl&gt; scopy longslit* %longslit%c250.%* aperture=250 band=100
  longslit1[250]  --&gt;  c250.1[250]
  longslit2[250]  --&gt;  c250.2[250]
  longslit3[250]  --&gt;  c250.3[250]
  ...
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_SCOPY">
  <dt><b>SCOPY V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SCOPY' Line='SCOPY V2.11' -->
  <dd>Previously both w1 and w2 had to be specified to select a range to
  copy.  Now if only one is specified the second endpoint defaults
  to the first or last pixel.
  </dd>
  </dl>
  <dl id="l_SCOPY">
  <dt><b>SCOPY V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SCOPY' Line='SCOPY V2.10.3' -->
  <dd>Additional support for 3D multispec/equispec or spatial spectra has been
  added.  The <span style="font-family: monospace;">"bands"</span> parameter allows selecting specific bands and
  the onedspec output format creates separate images for each selected
  aperture and band.
  </dd>
  </dl>
  <dl id="l_SCOPY">
  <dt><b>SCOPY V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SCOPY' Line='SCOPY V2.10' -->
  <dd>This task is new.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ranges, sarith, imcopy, dispcor, specshift
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

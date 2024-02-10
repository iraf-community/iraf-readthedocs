.. _mscimage:

mscimage: Reconstruct single images from a mosaic exposures
===========================================================

**Package: mscred**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  Multiextension mosaic exposures are resampled, based on the individual
  extension WCS with distortions, into a single image with a simple WCS.
  This may include a pixel mask identify regions of no data and pixels with
  contributions from bad pixels.  Multiple exposures can be resampled to a
  common reference WCS such that the images can be registered with integer
  pixel shifts.  This task will also work with single images to resample
  to a new output image on a desired coordinate grid.
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  mscimage input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input mosaic exposures to be resampled into a single images.
  Single images may also be used if desired.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output images.  The number of output images must match
  the number of input mosaic exposures or images.
  </dd>
  </dl>
  <dl id="l_reference">
  <dt><b>reference = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reference' Line='reference = ""' -->
  <dd>Reference image for defining the coordinate system.  If no reference image
  is specified then the first input mosaic exposure or image will be used to
  define the output coordinate system.  The purpose of a reference image is
  to create multiple output images with pixel sampling that allows the images
  to be stacked by simple integer pixel shifts.  <b>This must be a single
  image and not a mosaic exposure.</b>
  </dd>
  </dl>
  <dl id="l_pixmask">
  <dt><b>pixmask = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixmask' Line='pixmask = yes' -->
  <dd>Create pixel masks for each output image?  The output mask will have the
  same name as the output image (minus the image type extension) with the 
  extension <span style="font-family: monospace;">"_bpm.pl"</span>.  The output mask name will also be recorded in the
  output image under the keyword BPM.  The output pixel mask will
  identify gap pixels plus any pixels in the output image which have
  contributions from bad pixels associated with each input extension.  The
  input pixel masks are specified by the BPM keyword in the extension.  If
  there is no bad pixel mask, an empty (all good pixels) mask will be
  assumed.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = <span style="font-family: monospace;">")_.verbose"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = ")_.verbose"' -->
  <dd>Print verbose information?  The default value points to the package
  <i>verbose</i> parameter.  The verbose information identifies the reference
  image being used and gives progress information when the empty output
  image is first created and then as each input extension is mapped to the
  output image.
  </dd>
  </dl>
  <dl id="l_blank">
  <dt><b>blank = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blank' Line='blank = 0.' -->
  <dd>The value assigned to regions where there is no data; i.e. the gaps between
  mosaic pieces and edges where small rotations produce no data in the
  output rectangular image.
  </dd>
  </dl>
  <dl id="l_interpolant">
  <dt><b>interpolant = <span style="font-family: monospace;">"linear"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interpolant' Line='interpolant = "linear"' -->
  <dd>The interpolation type used on the image data.  The choices are
  <div class="highlight-default-notranslate"><pre>
  nearest - nearest pixel
   linear - bi-linear interpolation
    poly3 - bi-cubic polynomial interpolation
    poly5 - bi-quintic polynomial interpolation
  spline3 - bi-cubic spline interpolation
     sinc - 2D sinc interpolation
    lsinc - look-up table sinc interpolations
  drizzle - 2D drizzle resampling
  </pre></div>
  For further information about the interpolants see <b>geotran</b>.
  The interpolation type has a major effect on the speed of execution.
  </dd>
  </dl>
  <dl id="l_minterpolant">
  <dt><b>minterpolant = <span style="font-family: monospace;">"linear"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minterpolant' Line='minterpolant = "linear"' -->
  <dd>The interpolation type used on the bad pixel mask.  The choices are the
  same as for the <i>interpolant</i> parameter.  The input bad pixel masks
  are interpolated to create an output bad pixel mask which includes the
  regions with no data such as mosaic gaps.  See the DISCUSSION to
  details about how this is done and how the choice of an interpolant should
  be made.
  </dd>
  </dl>
  <dl id="l_boundary">
  <dt><b>boundary = <span style="font-family: monospace;">"reflect"</span> (nearest|constant|reflect|wrap)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary' Line='boundary = "reflect" (nearest|constant|reflect|wrap)' -->
  <dd>Boundary extension to use to interpolate the data near the boundaries.
  The bad pixel mask interpolation only uses constant boundary extension
  as explained in the DISCUSSION.  The choices are
  <div class="highlight-default-notranslate"><pre>
   nearest - the nearest boundary pixel
  constant - the value supplied by the <i>constant</i> parameter
   reflect - reflect about the boundary
      wrap - wrap around to the opposite side
  </pre></div>
  To avoid ringing in the interpolation the boundary extension should
  not have a sharp discontinuity.  The <span style="font-family: monospace;">"reflect"</span> option is recommended.
  The <i>ntrim</i> parameter can also be used to avoid needing to interpolate
  beyond the image.
  </dd>
  </dl>
  <dl id="l_constant">
  <dt><b>constant = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constant' Line='constant = 0.' -->
  <dd>Constant value for <span style="font-family: monospace;">"constant"</span> boundary extension.
  </dd>
  </dl>
  <dl id="l_fluxconserve">
  <dt><b>fluxconserve = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fluxconserve' Line='fluxconserve = no' -->
  <dd>Conserve the flux per unit area?  If the input exposures have been
  flat-fielded to yield a constant sky per pixel then flux conservation
  should not be used.  If the input exposures have been corrected to observed
  flux per pixel (where the sky varies with the project size of the pixel on
  the sky) then flux conservation should be used.
  </dd>
  </dl>
  <dl id="l_trim">
  <dt><b>trim = 7</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trim' Line='trim = 7' -->
  <dd>Number of pixels to trim around the input image.  This can be used to
  eliminate bad edge data.  It also has the effect of avoiding interpolation
  problems at the image edges.  The piece of the image interpolated is
  trimmed at the edges by the specified amount but the data in the trimmed
  region is still used to interpolate beyond the trimmed edge.  The amount of
  trim will depend on the number of bad columns and lines on the edges
  and on the extent of the interpolant.  In general the edge should be
  at least half of the size of the interpolatant so that for cubics it
  would be at least 1, for quintic 2, and for sinc half the size of
  the sinc kernel.
  </dd>
  </dl>
  <dl id="l_nxblock">
  <dt><b>nxblock = 2048, nyblock = 1024</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxblock' Line='nxblock = 2048, nyblock = 1024' -->
  <dd>Working block size for the interpolation.  The parameters should be set
  as large as possible consistent with the available memory maximize the
  interpolation efficiency.  The x block size should typically correspond
  to the maximum number of columns in an input extension since the
  interpolation is done extension by extension.
  </dd>
  </dl>
  <p>
  The following parameters deal with determining the mapping function
  between input and output pixels.  The defaults should be adequate for
  all cases.  See the DESCRIPTION for the meaning of the transformation
  and <b>geomap</b> for more detailed information about the parameters.
  </p>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Fit the mapping function interactively?  The selects the interactive
  fitting option of <b>geomap</b>.
  </dd>
  </dl>
  <dl id="l_nx">
  <dt><b>nx = 10, ny = 20</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nx' Line='nx = 10, ny = 20' -->
  <dd>Number of x and y grid points to use over the input image (each piece in
  a mosaic) to use in determining
  the mapping function.  The grid separation  in x and y should be about
  equal so the default values are appropriate for input image extensions which
  have twice as many lines as columns.
  </dd>
  </dl>
  <dl id="l_fitgeometry">
  <dt><b>fitgeometry = <span style="font-family: monospace;">"general"</span>  (shift|xyscale|rotate|rscale|rxyscale|general)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitgeometry' Line='fitgeometry = "general"  (shift|xyscale|rotate|rscale|rxyscale|general)' -->
  <dd>Type of fitting geometry for the mapping function.  This should always
  be <span style="font-family: monospace;">"general"</span>.  See <b>geomap</b> for a description of the choices.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"chebyshev"</span> (chebyshev|legendre|polynomial)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "chebyshev" (chebyshev|legendre|polynomial)' -->
  <dd>Type of mapping function to use.  The choices are
  <div class="highlight-default-notranslate"><pre>
   chebyshev - Chebyshev polynomial
    legendre - Legendre polynomial
  polynomial - Power series polynomial
  </pre></div>
  </dd>
  </dl>
  <dl id="l_xxorder">
  <dt><b>xxorder = 4, xyorder = 4, yxorder = 4, yyorder = 4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xxorder' Line='xxorder = 4, xyorder = 4, yxorder = 4, yyorder = 4' -->
  <dd>Orders of fitting function where order means the highest power of
  x or y terms.
  </dd>
  </dl>
  <dl id="l_xxterms">
  <dt><b>xxterms = <span style="font-family: monospace;">"half"</span>, yxterms = <span style="font-family: monospace;">"half"</span> (none|half|full)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xxterms' Line='xxterms = "half", yxterms = "half" (none|half|full)' -->
  <dd>Type of cross terms for x^i*y^j.  The options are <span style="font-family: monospace;">"none"</span> to include
  only terms in which either i or j is zero,
  <span style="font-family: monospace;">"half"</span> to include only terms where i+j is less
  than the maximum for either i or j, and <span style="font-family: monospace;">"full"</span> where i and j 
  take all values less than the maximum for each.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Mscimage</b> takes mosaic exposures, consisting of multiple extensions in
  a multiextension FITS (MEF) file, or single images and resamples them to
  output images with a desired coordinate grid on the sky.  For mosaic
  exposures all the pieces are resampled to create a single output image.  This is
  the common usage of this task.  For single input images this task might be used
  to take images with different spatial sampling and put them on a common
  grid.  By specifying the same output grid on the sky multiple output
  images from multiple input exposures can be stacked with simple integer
  shifts.  The output is designed to be used with <b>mscstack</b> or
  \Bimcombine with <span style="font-family: monospace;">"offset=wcs"</span>.
  </p>
  <p>
  The list of input mosaic exposures or single images is specified with the
  <i>input</i> parameter and a matching list of output images is specified
  with the <i>output</i> parameter.  The coordinate grid for the output
  images is defined by specifying a <i>reference</i> image with the desired
  coordinate grid.  The reference is a single image and not a MEF mosaic
  exposure.  The output of <b>mscimage</b> may be used as a reference image
  to resample other images to the same coordinate grid.
  </p>
  <p>
  If no reference image is specified then the first input exposure is used to
  define the output coordinate grid.  When the input is a mosaic (which
  assumes all the pieces have a common tangent point) the piece nearest the
  tangent point on the sky is used as the reference.  Only the linear
  components of the input image coordinate system are used.  In other words,
  the linear scales and rotation of the coordinate system at the tangent
  point are used along with a standard tangent plane projection for the
  output coordinate system.  The resampling will remove any higher distortion
  terms.
  </p>
  <p>
  It is important to understand that resampling to a common coordinate grid
  does not mean the images are registered in pixel space.  What it means
  is that if one takes the coordinate system of the reference and extends
  it to infinity then the output image will map to pixels in that grid
  and the output image will be trimmed to just include the data.  Thus
  different images will not overlay on a display but will stack into
  a larger image without subpixel errors.  For a set of dithered images
  or mosaic exposures, one common usage is to specify all the exposures
  in the input leaving the reference image blank.  Then all the output
  images will automatically be resampled so that they can be easily stacked
  with <b>mscstack</b>.
  </p>
  <p>
  The resampling involves using the world coordinate system (WCS) of the
  input image or each piece of the input mosaic exposure to interpolate the
  pieces to the appropriate places in the output image.  This task may also
  create a bad pixel mask, selected by the <i>pixmask</i> parameter, from
  the input bad pixel masks given by the <span style="font-family: monospace;">"BPM"</span> keyword in the headers.
  Even if there are no masks for the input images/mosaic exposures an
  output mask is desirable since it will still identify regions with
  no data such as the gaps in a mosaic and regions around the edges that
  don't map into the image rectangle.  This is discussed further later.
  </p>
  <p>
  The resampling of the input pieces to the output image is done piece by
  piece where a single input image is treated as an exposure with a single
  piece.  First an
  empty output image is created with all pixels having the <i>blank</i>
  value.  The output has a size that will just include all the input data.
  Then each input piece is mapped to the appropriate region of the output
  image.  The mapping function maps input pixel coordinates (xin, yin) to
  output pixel coordinates (xout,yout).  The mapping function is used to
  determine which input pixels contribute to each output pixel and an
  interpolation is done to create the output pixel value.
  </p>
  <p>
  The mapping function is determined using the task <b>geomap</b> and
  the interpolation is done using the task <b>geotran</b>.  Many of the
  parameters of this task are for those tasks.
  </p>
  <p>
  The mapping function for an input piece is derived as follows.  A grid of
  points (xin,yin) covering the input piece is generated.  The number of grid
  points in each dimension is set by the <i>nx</i> and <i>ny</i> parameters.
  The grid includes the corners.  The WCS of the input piece is used to
  convert the grid pixel coordinates to sky coordinates (wx,wy).  The
  WCS of the output image is used to convert the sky coordinates to matching
  pixel coordinates in the output image (xout,yout).  The task
  <b>geomap</b> is used to fit a mapping function (actually one function
  for each dimension)
  </p>
  <div class="highlight-default-notranslate"><pre>
  xin = f1(xout,yout)
  yin = f2(xout,yout)
  </pre></div>
  <p>
  where the function parameters are defined by task parameters.  The function
  should be general enough to accurately follow distortions in the mapping
  between the input and output pixel coordinates.  The default values for
  this task should generally be adequate though one might adjust the number
  of grid points according to the ratio of the input extension dimensions.
  </p>
  <p>
  Once the mapping function is determined the task <b>geotran</b> does the
  resampling of the input piece to the output image.  This task requires a
  interpolation type, given by the <i>interpolant</i> parameter, what to do at
  the boundary, given by the <i>boundary</i> and <i>constant</i> parameters,
  whether to adjust the interpolated value by the ratio of the input and
  output pixel areas to conserve flux specified by the <i>fluxconserve</i>
  parameter, and some memory limits specified by <i>nxblock</i> and
  <i>nyblock</i>.
  </p>
  <p>
  Whether or not the flux conservation option should be used depends on
  whether the input data has been calibrated to a constant sky or
  not.  Usually the data is calibrated using a flat-field or sky flat-field
  which has the effect of making the pixel values be uniform for the sky.
  This is done regardless of the project pixel size on the sky.  If
  this is the case then the flux conservation option should not be used
  because the output WCS is defined to have uniform pixel areas on the
  sky and, therefore, uniform pixel values for the sky.
  </p>
  <p>
  However, the input data may be calibrated to have sky pixel values
  corresponding to the projected area of the pixel on the sky.  This
  is typically done by taking the flat-fielded data and apply a pixel
  size correction to the data.  In this case the flux conservation option
  should be used to make the pixel sizes from the input to the output
  with the associated change in pixel values.
  </p>
  <p>
  The output masks are created by taking any input masks and creating
  temporary masks with non-zero values (the bad pixel indication) in the
  input mask mapped to 10000.  If there is no input mask then an empty
  temporary mask is created.  This mask is then interpolated using the same
  coordinate mapping used for the data.  Because the input mask jumps between
  zero and 10000 any interpolated value will generally be 0 where there are
  only good values contributing to the interpolation, 10000 if there are only
  bad pixels, or some value in between when there are contributions from the
  bad pixels.  The value 10000 is used since pixel masks have integer values
  only so any interpolated value with 0.01% effect from a bad pixel will
  still be identified as a bad pixel.  At the edges of the image the pixel
  mask interpolation uses constant value boundary extension with the value of
  10000.  This effectively acts as a mask for the out of bounds regions.
  </p>
  <p>
  The interpolation functions for the data and the mask can be independently
  selected.  One might use the same function for both.  However, some
  desirable interpolation functions, such as sinc interpolation, require a
  large piece of the input for each output pixel.  This would effectively
  mask a large area about any bad pixel.  In this case it is recommended that
  the input data have the bad pixels, including cosmic rays, replaced by
  interpolated data (using <b>ccdproc</b> or <b>fixpix</b> for instance) to
  eliminate sharp features that ring in the interpolators.  By smoothing over
  the bad pixels artificially, the effects on distant pixels from something
  like a sinc interpolation should be minimal and so you might only want only
  the pixels near the marked bad pixels to appear in the output mask.  This
  is done by using an <b>minterpolant</b> of <span style="font-family: monospace;">"linear"</span> or <span style="font-family: monospace;">"poly3"</span> for the mask
  even when using a larger interpolant for the data.
  </p>
  <p>
  There is still the problem of interpolating near the edges of the input
  pieces.  The <span style="font-family: monospace;">"reflect"</span> boundary extension will largely minimize ringing at
  the edges from an interpolator.  But a possibly better method is to use the
  <i>ntrim</i> parameter to mask out the edges of the input pieces.  Even
  though the trimmed pixels are not mapped to the output (where they appear
  with the <i>blank</i>) they are still available for the interpolation.  Thus
  the trim parameter should be set to excludes actual bad edges and then to
  trim in beyond the range of the interpolator.  The value to use would be
  one-half of the order or extent of the interpolator.  For dithered mosaic
  exposures the trimming widens the gaps slightly but insures that there are
  no edge effects to bleed through when stacking the dithers to fill in the
  gaps.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Create images for a set of dithered exposures to be later stacked.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mscimage @dither1 mos//@dither1
  </pre></div>
  <p>
  2.  Create images on a common WCS.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mscimage obj0321 mos0321
  cl&gt; mscimage obj0322 mos0322 ref=mos0321
  cl&gt; mscimage obj0323 mos0323 ref=mos0321
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MSCIMAGE">
  <dt><b>MSCIMAGE - V4.1: September 6, 2000</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MSCIMAGE' Line='MSCIMAGE - V4.1: September 6, 2000' -->
  <dd>The trimming was changed from being done on the output region to being done
  on the input region.  This better insures minimzation of edge effects since
  when masking on the output there is a variable amount of the input edges
  masked (sometimes none) depending on the distortions.
  The parameters <span style="font-family: monospace;">"boundary"</span> and <span style="font-family: monospace;">"constant"</span> were added to allow control over
  the boundary extension.  Previously it was fixed to be constant boundary
  extension with the constant given by the <span style="font-family: monospace;">"blank"</span> parameter.
  Because it was a simple change the task was modified to allow single
  images as input as well as MEF mosaic exposures.
  </dd>
  </dl>
  <dl id="l_MSCIMAGE">
  <dt><b>MSCIMAGE - V2.11 external package</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MSCIMAGE' Line='MSCIMAGE - V2.11 external package' -->
  <dd>First release.
  </dd>
  </dl>
  </section>
  <section id="s_bugs_and_limitations">
  <h3>Bugs and limitations</h3>
  <p>
  The current version requires that the circumscribed boxes containing
  the input extension as projected on the output image do not overlap.
  This means the rotations of the pieces should be small and the output
  coordinate system is not rotated with respected to the mean orientation
  of the input exposure.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  geomap, geotran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'BUGS AND LIMITATIONS' 'SEE ALSO'  -->
  

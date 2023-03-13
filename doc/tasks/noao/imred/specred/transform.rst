.. _transform:

transform: Resample longslit spectra
====================================

**Package: specred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  transform input output fitnames
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images to be transformed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output images.  The number of output images in the list must
  match the number of input images.
  </dd>
  </dl>
  <dl id="l_minput">
  <dt><b>minput = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minput' Line='minput = ""' -->
  <dd>List of input masks or references.  This mask is used to create an output
  mask and is currently not used in the calculation of the output pixel
  values.  The list may be empty, a single element to apply to all input
  images, or a list that matches the input list.  A element in the list
  may be <span style="font-family: monospace;">"BPM"</span> to use the mask referenced by the standard bad pixel mask
  keyword <span style="font-family: monospace;">"BPM"</span>, <span style="font-family: monospace;">"!&lt;keyword&gt;"</span> to use another header keyword pointing to a
  mask, or a mask filename.  The mask file is typically a pixel list file
  but it may also be an image.  The mask values are interpreted as zero and
  greater than zero with the actual values ignored.  The mask is assumed to
  be registered with the input and no coordinate system matching is used.
  The mask maybe smaller or larger than the input image with non-overlapping
  pixels ignored and missing pixels assumed to be zero valued.  The mask
  </dd>
  </dl>
  <dl id="l_moutput">
  <dt><b>moutput = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='moutput' Line='moutput = ""' -->
  <dd>List of output masks to be created.  The list may be empty or must match
  the input list.  Output masks may be specified even if no input mask is
  specified, in which case the output mask will identify pixels which map
  to regions outside the input images (also see the <i>blank</i> parameter).
  If an explicit extension is not specified a FITS mask is extension is
  created unless the environment variable <span style="font-family: monospace;">"masktype"</span> is set to <span style="font-family: monospace;">"pl"</span>.
  </dd>
  </dl>
  <dl id="l_fitnames">
  <dt><b>fitnames  </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitnames' Line='fitnames  ' -->
  <dd>Names of the user coordinate maps in the database to be used in the transform.
  If no names are specified, using the null string <span style="font-family: monospace;">""</span>, the world coordinate
  system (WCS) of the image is used.  This latter case may be used to
  resample previously WCS calibrated images to a different linear range
  or sampling.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"database"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "database"' -->
  <dd>Database containing the coordinate map to be used in transforming the images.
  </dd>
  </dl>
  <dl id="l_interptype">
  <dt><b>interptype = <span style="font-family: monospace;">"spline3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interptype' Line='interptype = "spline3"' -->
  <dd>Image interpolation type.  The allowed types are <span style="font-family: monospace;">"nearest"</span> (nearest neighbor),
  <span style="font-family: monospace;">"linear"</span> (bilinear), <span style="font-family: monospace;">"poly3"</span> (bicubic polynomial), <span style="font-family: monospace;">"poly5"</span> (biquintic
  polynomial), and <span style="font-family: monospace;">"spline3"</span> (bicubic polynomial).
  </dd>
  </dl>
  <dl id="l_flux">
  <dt><b>flux = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flux' Line='flux = yes' -->
  <dd>Conserve flux per pixel?  If <span style="font-family: monospace;">"no"</span> then each output pixel is simply interpolated
  from the input image.  If <span style="font-family: monospace;">"yes"</span> the interpolated output pixel value is
  multiplied by the Jacobean of the transformation (essentially the ratio of
  pixel areas between the output and input images).
  </dd>
  </dl>
  <dl id="l_x1">
  <dt><b>x1 = INDEF, y1 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='x1' Line='x1 = INDEF, y1 = INDEF' -->
  <dd>User coordinates of the first output column and line.  If INDEF then the
  smallest value corresponding to a pixel from the image used to create the
  coordinate map is used.  These values are in user units regardless of whether
  logarithmic intervals are specified or not.
  </dd>
  </dl>
  <dl id="l_x2">
  <dt><b>x2 = INDEF, y2 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='x2' Line='x2 = INDEF, y2 = INDEF' -->
  <dd>User coordinates of the last output column and line.  If INDEF then the
  largest value corresponding to a pixel from the image used to create the
  coordinate map is used.  These values are in user units regardless of whether
  logarithmic intervals are specified or not.
  </dd>
  </dl>
  <dl id="l_dx">
  <dt><b>dx = INDEF, dy = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dx' Line='dx = INDEF, dy = INDEF' -->
  <dd>Output pixel intervals.  If INDEF then the interval is set to yield the
  specified number of pixels.  Note that for logarithmic intervals the
  interval must be specified as a base 10 logarithm (base 10) and not in
  user units.
  </dd>
  </dl>
  <dl id="l_nx">
  <dt><b>nx = INDEF, ny = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nx' Line='nx = INDEF, ny = INDEF' -->
  <dd>Number of output pixels.  If INDEF and if the pixel interval is also INDEF then
  the number of output pixels is equal to the number of input pixels.
  </dd>
  </dl>
  <dl id="l_xlog">
  <dt><b>xlog = no, ylog = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xlog' Line='xlog = no, ylog = no' -->
  <dd>Convert to logarithmic intervals?  If <span style="font-family: monospace;">"yes"</span> the output pixel intervals
  are logarithmic.
  </dd>
  </dl>
  <dl id="l_blank">
  <dt><b>blank = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blank' Line='blank = INDEF' -->
  <dd>Value to put in the output transformed image when it transforms to regions
  outside the input image.  The special value INDEF will use the nearest
  input pixel which is the behavior before the addition of this parameter.
  Using special blank values allows other software to identify such out
  of input pixels.  See also the <i>moutput</i> parameter to identify
  out of input pixels in pixel masks.
  </dd>
  </dl>
  <dl id="l_logfiles">
  <dt><b>logfiles = <span style="font-family: monospace;">"STDOUT,logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfiles' Line='logfiles = "STDOUT,logfile"' -->
  <dd>List of files in which to keep a log.  If null, <span style="font-family: monospace;">""</span>, then no log is kept.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The coordinate maps U(X,Y) and V(X,Y), created by the task <b>fitcoords</b>,
  are read from the specified database coordinate fits or from the
  world coordinate system (WCS) of the image.  X and Y are the original
  untransformed pixel coordinates and U and V are the desired output user or
  world coordinates (i.e. slit position and wavelength).  If a coordinate map
  for only one of the user coordinates is given then a one-to-one mapping
  is assumed for the other such that U=X or V=Y.  The coordinate maps are
  inverted to obtain X(U,V) and Y(U,V) on an even subsampled grid of U and
  V over the desired output image coordinates.  The X and Y at each output
  U and V used to interpolate from the input image are found by linear
  interpolation over this grid.  X(U,V) and Y(U,V) are not determined at
  every output point because this is quite slow and is not necessary since
  the coordinate surfaces are relatively slowly varying over the subsampling
  (every 10th output point).
  </p>
  <p>
  The type of image interpolation is
  selected by the user.  Note that the more accurate the interpolator the
  longer the transformation time required.  The parameter <i>flux</i> selects
  between direct image interpolation and a flux conserving interpolation.
  Flux conservation consists of multiplying the interpolated pixel value by
  the Jacobean of the transformation at that point.  This is essentially
  the ratio of the pixel areas between the output and input images.  Note
  that this is not exact since it is not an integral over the output pixel.
  However, it will be very close except when the output pixel size is much
  greater than the input pixel size.  A log describing the image transformations
  may be kept or printed on the standard output.
  </p>
  <p>
  The output coordinate grid may be defined by the user or allowed to
  default to an image of the same size as the input image spanning the
  full range of user coordinates in the coordinate transformation maps.
  When the coordinate maps are created by the task <b>fitcoords</b> the
  user coordinates at the corners of the image are recorded in the
  database.  By default these values are used to set the limits of the
  output grid.  If a pixel interval is not specified then an interval
  yielding the specified number of pixels is used.  The default number of
  pixels is that of the input image.  Note that if a pixel interval is
  specified then it takes precedence over the number of pixels.
  </p>
  <p>
  The pixel intervals may also be logarithmic if the parameter <i>xlog</i> or
  <i>ylog</i> is <span style="font-family: monospace;">"yes"</span>.  Generally, the number of output pixels is specified
  in this case .  However, if the interval is specified it must be a base
  10 logarithmic interval and not in units of the x and y limits which are
  specified in user units.
  </p>
  <p>
  The transformation from the desired output pixel to the input image may
  fall outside of the input image.  In this case the output pixel may be
  set to the nearest pixel value in the input image or to a particular value
  using the <i>blank</i> parameter.  Also if an output mask is created this
  pixels will have a value of one in the mask.
  </p>
  <p>
  The parameters <i>minput</i> and <i>moutput</i> provide for input and output
  pixel masks.  An input mask is not used in calculating the transformed
  pixel value but is used to identify the output pixels in the output mask
  which make a significant contribution to the interpolated value.  The
  significance is determined as follows.  The input mask values above zero
  are converted to one hundred.  The mask is then interpolated in the same
  way as the input image.  Any interpolated value of ten or greater is then
  given the value one in the output mask.  This means if all the input pixels
  had mask values of zero a result of zero means no bad pixels were used.
  If all the input pixels had values of 100 then the result will be 100 and
  the output mask will flag this as a bad pixel.  Other values are produced
  by a mixture of good and bad pixels weighted by the interpolation kernel.
  The choice of 10% is purely empirical and gives an approximate identification
  of significant affected pixels.
  zero and
  is created with values of 100
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Arc calibration images were used to determine a two dimensional dispersion
  map called dispmap.  Stellar spectra were used to determine a two dimensional
  distortion map call distort.  These maps where made using the task
  <b>fitcoords</b>. To transform a set of input images into linear wavelength
  between 3800 and 6400 Angstroms (the user coordinate units) with a dispersion
  of 3 Angstroms per pixel:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; transform obj001,obj002 out001,out002 dispmap,distort \
  &gt;&gt;&gt; y1=3800 y2=6400 dy=3
  </pre></div>
  <p>
  To use logarithmic intervals in the wavelength to yield the same number of
  pixels in the output images as in the input images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; transform obj001,obj002 out001,out002 dispmap,distort \
  &gt;&gt;&gt; y1=3800 y2=6400 ylog=yes
  </pre></div>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  <p>
  The following timings were obtained for transforming a 511x512 real
  image to another 511x512 real image using two Chebyshev transformation
  surface functions (one for the dispersion axis, <span style="font-family: monospace;">"henear"</span>, and one in
  spatial axis, <span style="font-family: monospace;">"object"</span>) of order 6 in both dimensions created with the
  task <b>fitcoords</b>.  The times are for a UNIX/VAX 11/750.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; $transform input output henear,object interp=linear
  TIME (transform)  173.73  5:13  55%
  cl&gt; $transform input output henear,object interp=poly3
  TIME (transform)  266.63  9:17  42%
  cl&gt; $transform input output henear,object interp=spline3
  TIME (transform)  309.05  6:11  83%
  cl&gt; $transform input output henear,object interp=spline3
  TIME (transform)  444.13  9:44  76%
  cl&gt; $transform input output henear interp=linear
  TIME (transform)  171.32  7:24  38%
  cl&gt; $transform input output henear interp=spline3
  TIME (transform)  303.40  12:17  41%
  cl&gt; $transform input output henear,object interp=spline3 flux=no
  TIME (transform)  262.42  10:42  40%
  </pre></div>
  <p>
  The majority of the time is due to the image interpolation and not evaluating
  the transformation functions as indicated by the last three examples.
  </p>
  </section>
  <section id="s_notes">
  <h3>Notes</h3>
  <dl id="l_TRANSFORM">
  <dt><b>TRANSFORM: V2.12.2</b></dt>
  <!-- Sec='NOTES' Level=0 Label='TRANSFORM' Line='TRANSFORM: V2.12.2' -->
  <dd>The use of bad pixel masks, a specified <span style="font-family: monospace;">"blank"</span> value, and use of a WCS
  to resample a WCS calibrated image was added.
  </dd>
  </dl>
  <dl id="l_TRANSFORM">
  <dt><b>TRANSFORM: V2.6</b></dt>
  <!-- Sec='NOTES' Level=0 Label='TRANSFORM' Line='TRANSFORM: V2.6' -->
  <dd>With Version 2.6 of IRAF the algorithm used to invert the user
  coordinate surfaces, U(X,Y) and V(X,Y) to X(U,V) and Y(U,V), has been
  changed.  Previously surfaces of comparable order to the original
  surfaces were fit to a grid of points, i.e. (U(X,Y), V(X,Y), X) and
  (U(X,Y), V(X,Y), Y), with the same surface fitting routines used in
  <b>fitcoords</b> to obtain the input user coordinate surfaces.  This
  method of inversion worked well in all cases in which reasonable
  distortions and dispersions were used.  It was selected because it was
  relatively fast.  However, it cannot be proved to work in all cases; in
  one instance in which an invalid surface was used the inversion was
  actually much poorer than expected.  Therefore a more direct iterative
  inversion algorithm is now used.  This is guaranteed to give the
  correct inversion to within a set error (0.05 of a pixel in X and Y).
  It is slightly slower than the previous algorithm but it is still not
  as major a factor as the image interpolation itself.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fitcoords
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIMINGS' 'NOTES' 'SEE ALSO'  -->
  

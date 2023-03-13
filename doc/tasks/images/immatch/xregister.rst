.. _xregister:

xregister: Register 1-D or 2-D images using x-correlation techniques
====================================================================

**Package: immatch**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xregister input reference regions shifts
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input images to be registered.
  </dd>
  </dl>
  <dl id="l_reference">
  <dt><b>reference</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reference' Line='reference' -->
  <dd>The list of reference images to which the input images are to be registered.
  The number of reference images must be one or equal to the number of input
  images.
  </dd>
  </dl>
  <dl id="l_regions">
  <dt><b>regions</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='regions' Line='regions' -->
  <dd>The list of reference image region(s) used to compute the 
  x and y shifts.
  <i>Regions</i> may be: 1) a list of one or more image sections
  separated by whitespace, 2) the name of a text file containing a list
  of one or more image sections separated by whitespace and/or newlines,
  3) a string of the form <span style="font-family: monospace;">"grid nx ny"</span> defining a grid of nx by ny
  equally spaced and sized image sections spanning the entire image. Shifts are
  computed for each specified region individually and averaged to produce the
  final x and y shift.
  </dd>
  </dl>
  <dl id="l_shifts">
  <dt><b>shifts</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shifts' Line='shifts' -->
  <dd>The name of the text file where the computed x and y shifts 
  are written. If <i>databasefmt</i> is <span style="font-family: monospace;">"yes"</span>,  a single record containing the
  computed x and y shifts for each image region and the final average x and y
  shift is written to a text database file for each input image.
  If <i>databasefmt</i> = <span style="font-family: monospace;">"no"</span>, a single line containing the image name and the
  final average x and y shift is written to a simple text file
  for each input image.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>The list of output shifted images. If <i>output</i> is the NULL string
  then x and y shifts are computed for each input image and written to
  <i>shifts</i> but no output images are written. If <i>output</i> is not NULL
  then the number of output images must equal the number of input images.
  </dd>
  </dl>
  <dl id="l_databasefmt">
  <dt><b>databasefmt = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='databasefmt' Line='databasefmt = yes' -->
  <dd>If <i>databasefmt</i> is <span style="font-family: monospace;">"yes"</span> the results are written to a text database
  file, otherwise they are written to a simple text file.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records = ""' -->
  <dd>The list of records to be written to or read from <i>shifts</i> for each
  input image. If <i>records</i> is NULL then the output or input record names
  are assumed to be the names of the input images. If <i>records</i> is not NULL
  then the record names in <i>records</i> are used to write / read the
  records. This parameter is useful for users
  who, wish to compute the x and y shifts using images that have been processed
  in some manner (e.g. smoothed), but apply the computed x and y shifts to the
  original unprocessed images. If more then one record
  with the same name exists in <i>shifts</i> then the most recently written
  record takes precedence. The records parameter is ignored if
  <i>databasefmt</i> is <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = yes' -->
  <dd>Append new records to an existing <i>shifts</i> file or start a new shifts
  file for each execution of XREGISTER? The append parameter is ignored
  if <i>databasefmt</i> is <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords = ""' -->
  <dd>An optional list of coordinates files containing the x and y coordinates of
  an object in the reference image on the first line and the x and y coordinates
  of the same object in the input image(s) on succeeding lines. The number
  of coordinate files must be equal to the number of reference images.
  The input coordinates are used to compute initial
  values for the x and y lags between the input image and the reference image,
  and supersede any non-zero values of <i>xlag</i>, <i>ylag</i>, <i>dxlag</i>,
  and <i>dylag</i> supplied by the user.
  </dd>
  </dl>
  <dl id="l_xlag">
  <dt><b>xlag = 0, ylag = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xlag' Line='xlag = 0, ylag = 0' -->
  <dd>The initial x and y lags of the input image with respect to the reference
  image. Positive values imply that the input image is shifted
  in the direction of increasing x and y values with respect to the
  reference image. <i>Xlag</i> and <i>ylag</i> are overridden if an offset
  has been determined using the x and y coordinates in the <i>coords</i> file.
  </dd>
  </dl>
  <dl id="l_dxlag">
  <dt><b>dxlag = 0, dylag = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dxlag' Line='dxlag = 0, dylag = 0' -->
  <dd>The increment in <i>xlag</i> and <i>ylag</i> to be applied to successive input
  images. If <i>dxlag</i> and <i>dylag</i> are set to INDEF then the 
  computed x and y lags for the previous image are used as the initial
  x and y lags for the current image. This option is useful for images which
  were taken as a time sequence and whose x and y the shifts increase or
  decrease in a systematic manner.
  <i>Dxlag</i> and <i>dylag</i> are overridden if an offset
  has been determined using x and y coordinates in the <i>coords</i> file.
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background = none</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = none' -->
  <dd>The default background function to be subtracted from the input
  and reference image data in each region before the
  cross-correlation function is computed. The options are:
  <dl>
  <dt><b>none</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='none' Line='none' -->
  <dd>no background subtraction is done.
  </dd>
  </dl>
  <dl>
  <dt><b>mean</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='mean' Line='mean' -->
  <dd>the mean of the reference and input image region is computed and subtracted
  from the image data.
  </dd>
  </dl>
  <dl>
  <dt><b>median</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='median' Line='median' -->
  <dd>the median of the reference and input image region is computed and subtracted
  from the data.
  </dd>
  </dl>
  <dl>
  <dt><b>plane</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='plane' Line='plane' -->
  <dd>a plane is fit to the reference and input image region and subtracted
  from the data.
  </dd>
  </dl>
  By default the cross-correlation function is computed in a manner
  which removes the mean intensity in the reference and input image regions 
  from the data. For many data sets this <span style="font-family: monospace;">"correction"</span>  is sufficient to
  remove first order background level effects
  from the computed cross-correlation function and  no additional
  background subtraction is required.
  </dd>
  </dl>
  <dl id="l_border">
  <dt><b>border = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='border' Line='border = INDEF' -->
  <dd>The width of the border region around the input and reference image data
  regions used to compute the background function if <i>background</i>
  is not <span style="font-family: monospace;">"none"</span>. By default the entire region is used.
  </dd>
  </dl>
  <dl id="l_loreject">
  <dt><b>loreject = INDEF, ls hireject = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='loreject' Line='loreject = INDEF, ls hireject = INDEF' -->
  <dd>The k-sigma rejection limits for removing the effects of bad data from the
  background fit.
  </dd>
  </dl>
  <dl id="l_apodize">
  <dt><b>apodize = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apodize' Line='apodize = 0.0' -->
  <dd>The fraction of the input and reference image data endpoints in x and y
  to apodize with a
  cosine bell function before the cross-correlation function is computed.
  </dd>
  </dl>
  <dl id="l_filter">
  <dt><b>filter = none</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filter' Line='filter = none' -->
  <dd>The spatial filter to be applied to the reference and input image
  data before the cross-correlation function is computed. The options are:
  <dl>
  <dt><b>none</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='none' Line='none' -->
  <dd>no spatial filtering is performed.
  </dd>
  </dl>
  <dl>
  <dt><b>laplace</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='laplace' Line='laplace' -->
  <dd>a Laplacian filter is applied to the reference and input image data.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_correlation">
  <dt><b>correlation = discrete</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='correlation' Line='correlation = discrete' -->
  <dd>The algorithm used to compute the cross-correlation function. The options
  are:
  <dl>
  <dt><b>discrete</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='discrete' Line='discrete' -->
  <dd>The cross-correlation function is calculated by computing the discrete
  convolution of the reference and input image regions over the x and y 
  window of interest.  This technique is most efficient method for small
  cross-correlation function x and y search windows.
  </dd>
  </dl>
  <dl>
  <dt><b>fourier</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='fourier' Line='fourier' -->
  <dd>The cross-correlation function is calculated by computing the convolution
  of the reference and input image regions  using Fourier techniques.
  This technique is the most efficient method for computing  the
  cross-correlation function for small x and y search windows.
  </dd>
  </dl>
  <dl>
  <dt><b>difference</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='difference' Line='difference' -->
  <dd>The cross-correlation function is calculated by computing the error
  function of the reference and input images as a function of position
  in the x and y search window.
  </dd>
  </dl>
  <dl>
  <dt><b>file</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='file' Line='file' -->
  <dd>No cross-correlation function is computed. Instead the previously
  computed x and y shifts are read from record <i>record</i> in  the text
  database file <i>shifts</i> if <i>databasefmt</i> is <span style="font-family: monospace;">"yes"</span>, or the
  next line of a simple text file if <i>databasefmt</i> is <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_xwindow">
  <dt><b>xwindow = 11, ywindow = 11</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xwindow' Line='xwindow = 11, ywindow = 11' -->
  <dd>The x and y width of the cross-correlation function region
  to be computed and/or searched for peaks. The search window corresponds
  to shifts of - xwindow / 2 &lt;= xshift &lt;= xwindow /2  and - ywindow / 2 &lt;=
  yshift &lt;= ywindow / 2.  <i>Xwindow</i> and <i>ywindow</i>
  are automatically rounded up to the next nearest odd number.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = centroid</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = centroid' -->
  <dd>The algorithm used to compute the x and y position of the cross-correlation
  function peak.  The options are:
  <dl>
  <dt><b>none</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='none' Line='none' -->
  <dd>the position of the cross-correlation function peak is set to
  x and y position of the maximum pixel.
  </dd>
  </dl>
  <dl>
  <dt><b>centroid</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='centroid' Line='centroid' -->
  <dd>the position of the cross-correlation function peak is calculated
  by computing the intensity-weighted mean of the marginal profiles of
  the cross-correlation function in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>sawtooth</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='sawtooth' Line='sawtooth' -->
  <dd>the position of the cross-correlation function peak is calculated
  by  convolving 1D slices in x and y through the cross-correlation function
  with a 1D sawtooth function and using the point at which the peak is
  bisected to determine the x and y position of the cross-correlation
  peak. 
  </dd>
  </dl>
  <dl>
  <dt><b>parabolic</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='parabolic' Line='parabolic' -->
  <dd>a 1D parabola is fit to 1D slices in x and y through the cross-correlation
  function and the fitted coefficients are used to compute the peak of
  the cross-correlation function.
  </dd>
  </dl>
  <dl>
  <dt><b>mark</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='mark' Line='mark' -->
  <dd>mark the peak of the cross-correlation function with the graphics cursor.
  This option will only work if <i>interactive</i> = <span style="font-family: monospace;">"yes"</span>.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_xcbox">
  <dt><b>xcbox = 5, ycbox = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xcbox' Line='xcbox = 5, ycbox = 5' -->
  <dd>The width of the box centered on the peak of the cross-correlation function
  used to compute the fractional pixel x and y center.
  </dd>
  </dl>
  <dl id="l_interp_type">
  <dt><b>interp_type = <span style="font-family: monospace;">"linear"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interp_type' Line='interp_type = "linear"' -->
  <dd>The interpolant type use to computed the output shifted image.
  The choices are the following:
  <dl>
  <dt><b>nearest</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nearest' Line='nearest' -->
  <dd>nearest neighbor.
  </dd>
  </dl>
  <dl>
  <dt><b>linear</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='linear' Line='linear' -->
  <dd>bilinear interpolation in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>poly3</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='poly3' Line='poly3' -->
  <dd>third order interior polynomial in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>poly5</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='poly5' Line='poly5' -->
  <dd>fifth order interior polynomial in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>spline3</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='spline3' Line='spline3' -->
  <dd>bicubic spline.
  </dd>
  </dl>
  <dl>
  <dt><b>sinc</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='sinc' Line='sinc' -->
  <dd>2D sinc interpolation. Users can specify the sinc interpolant width by
  appending a width value to the interpolant string, e.g. sinc51 specifies
  a 51 by 51 pixel wide sinc interpolant. The sinc width input by the
  user will be rounded up to the nearest odd number. The default sinc width
  is 31 by 31.
  </dd>
  </dl>
  <dl>
  <dt><b>drizzle</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='drizzle' Line='drizzle' -->
  <dd>2D drizzle resampling. Users can specify the drizzle pixel fractions in x and y
  by appending values between 0.0 and 1.0 in square brackets to the
  interpolant string, e.g. drizzle[0.5]. The default value is 1.0. The
  value 0.0 is increased to 0.001. Drizzle resampling with a pixel fraction
  of 1.0 in x and y is identical to bilinear interpolation.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_boundary_type">
  <dt><b>boundary_type = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary_type' Line='boundary_type = "nearest"' -->
  <dd>The boundary extension algorithm used to compute the output shifted
  image.  The choices are:
  <dl>
  <dt><b>nearest</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nearest' Line='nearest' -->
  <dd>use the value of the nearest boundary pixel.
  </dd>
  </dl>
  <dl>
  <dt><b>constant</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='constant' Line='constant' -->
  <dd>use a constant value.
  </dd>
  </dl>
  <dl>
  <dt><b>reflect</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='reflect' Line='reflect' -->
  <dd>generate a value by reflecting about the boundary.
  </dd>
  </dl>
  <dl>
  <dt><b>wrap</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='wrap' Line='wrap' -->
  <dd>generate a value by wrapping around to the opposite side of the image.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_constant">
  <dt><b>constant = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constant' Line='constant = 0' -->
  <dd>The default constant for constant boundary extension.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Compute the cross-correlation function and the shifts for each image
  interactively using graphics cursor and optionally image cursor input.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose' -->
  <dd>Print messages about the progress of the task during task execution
  in non-interactive mode.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>The default graphics device.
  </dd>
  </dl>
  <dl id="l_display">
  <dt><b>display = <span style="font-family: monospace;">"stdimage"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='display' Line='display = "stdimage"' -->
  <dd>The default image display device.
  </dd>
  </dl>
  <dl id="l_gcommands">
  <dt><b>gcommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gcommands' Line='gcommands = ""' -->
  <dd>The default graphics cursor.
  </dd>
  </dl>
  <dl id="l_icommands">
  <dt><b>icommands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='icommands' Line='icommands = ""' -->
  <dd>The default image display cursor.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XREGISTER computes the x and y shifts required to register a list of input
  images <i>input</i> to a list of reference images <i>reference</i> using
  cross-correlation techniques. The computed x and y shifts are stored
  in the text file <i>shifts</i>, in the records <i>records</i> if
  <i>databasefmt</i> is <span style="font-family: monospace;">"yes"</span> or a single line of a simple text file
  if <i>databasefmt</i> is <span style="font-family: monospace;">"no"</span>. One entry is made in the shifts file for
  each input image. If a non NULL list of output images
  <i>output</i> is supplied a shifted output image is written for each input
  image. XREGISTER is intended to solve 1D and 2D image registration problems
  where the images have the same size, the same pixel scale, are shifted
  relative to
  each other by simple translations in x and y, and contain one or more
  extended features in common that will produce a peak in the computed
  cross-correlation function.
  </p>
  <p>
  The reference image regions used to compute the cross-correlation
  function shifts are defined by the parameter
  <i>regions</i>. <i>Regions</i> may be:
  1) a list of one or more image sections, e.g.
  <span style="font-family: monospace;">"[100:200,100:200] [400:500,400:500]"</span> separated
  by whitespace, 2) the name of a text file containing a list of one or
  more image sections separated by whitespace and / or newline characters,
  or, 3) a string
  of the form <span style="font-family: monospace;">"grid nx ny"</span> specifying a grid of nx by ny
  image sections spanning the entire reference image.
  All reference image regions should be chosen so as to 
  include at least one well-defined object or feature. Cross-correlation
  functions and x and y shifts are computed independently for each
  reference image region
  and averaged to produce the final x and y shift for each input image.
  </p>
  <p>
  By default the initial x and y lags between the input and reference
  image are assumed to by 0.0 and 0.0
  respectively and each reference image region is cross-correlated
  with the identical region in the input image, e.g reference image
  region [100:200,100:200] is cross-correlated with input image
  region [100:200,100:200].
  </p>
  <p>
  Non-zero initial guesses for
  the x and y shifts for each input image can be input to XREGISTER using
  the coordinates file parameter <i>coords</i>.
  <i>Coords</i> is a simple text file containing the x
  and y coordinates of a  single
  object in the reference image in columns one and two
  of line one, and the x and y coordinates of the same object in the first
  input image in columns one and two of line two, etc. If <i>coords</i>
  is defined there must be one coordinate file for every reference image.
  If there are fewer lines of text in <i>coords</i> than there are 
  numbers of reference plus input images, then x and y shifts of 0.0 are
  assumed for the extra input images. For example,
  if the  user specifies a single input and reference image, sets the
  <i>regions</i> parameter to <span style="font-family: monospace;">"[100:200,100:200]"</span>, and defines
  a coordinates file  which contains the numbers 
  50.0 50.0 in columns one and two of line one,  and the numbers 52.0 and 52.0
  in columns one and two of line two, then the initial x and y
  lags for the input image with respect to the reference image will be 2.0
  and 2.0 respectively, and the reference image region [100:200,100:200] will be
  cross-correlated with the input image region [102:202,102:202]. 
  </p>
  <p>
  If <i>coords</i> is NULL, the parameters <i>xlag</i>, <i>ylag</i>,
  <i>dxlag</i>, and <i>dylag</i> can be used to define initial x and y lags
  for each input image. <i>Xlag</i> and <i>ylag</i> define the x and y lags
  of the first input image with respect to the reference image. In the
  example above they would be set to 2.0 and 2.0 respectively. Initial
  shifts for succeeding images are computed by adding the values of the
  <i>dxlag</i> and <i>dylag</i> parameters  to the values of
  <i>xlag</i> and <i>ylag</i> assumed for the previous image.
  If <i>dxlag</i> and <i>dylag</i> are 0.0 and 0.0
  the same initial x and y lag will be used for all the input
  images. If <i>dxlag</i> and <i>dylag</i> are both finite numbers then these
  numbers will be added to
  the x and y lags assumed for the previous image. If these numbers
  are both INDEF then the computed x and y lags for the previous image
  will be used to compute the initial x and y lags for the current image.
  Both options can be useful for time series images where the x and y
  shifts between successive images display some regular behavior.
  </p>
  <p>
  Prior to computing the cross-correlation function
  large mean background values and gradients should be removed
  from the input and reference image data as either
  can seriously degrade the peak of the cross-correlation
  function.  To first order XREGISTER computes the cross-correlation function
  in a manner which removes
  the effect of large mean background values from the resulting
  function. For many if not most typical data sets the user can safely leave
  the parameter <i>background</i> at its default value of <span style="font-family: monospace;">"none"</span> and
  achieve reasonable results. For more demanding data sets the user should
  experiment with the <span style="font-family: monospace;">"mean"</span>, <span style="font-family: monospace;">"median"</span>, and <span style="font-family: monospace;">"plane"</span> background fitting
  algorithms which compute and subtract, the mean value, median value, and
  a plane from the input and reference image data respectively,
  before computing the
  cross-correlation function. The region used to compute the background fitting
  function can be restricted to a border around the reference and
  input image regions by setting the <i>border</i> parameter. Bad
  data can be rejected from the background fit by setting the <i>loreject</i>
  and <i>hireject</i> parameters.
  </p>
  <p>
  A cosine bell function can be applied to the edges of the input and
  reference image data before
  computing the cross-correlation function by setting the <i>apodize</i>
  parameter.
  </p>
  <p>
  If the <i>filter</i> parameter is set to <span style="font-family: monospace;">"laplace"</span> instead of its default
  value of <span style="font-family: monospace;">"none"</span> then a Laplacian filter is applied to the input and
  reference image data before the cross-correlation function is computed.
  This spatial filtering operation effectively
  removes both a background and a slope from the input and reference image
  data and
  highlights regions of the image where the intensity is changing rapidly.
  The effectiveness of this filtering operation in sharpening the
  correlation peak depends on the degree to
  which the intensity in adjacent pixels is correlated.
  </p>
  <p>
  The cross-correlation function for each region is computed by
  discrete convolution, <i>correlation</i> = <span style="font-family: monospace;">"discrete"</span>,
  Fourier convolution, <i>correlation</i> = <span style="font-family: monospace;">"fourier"</span>, or by computing
  the error function, <i>correlation</i> = <span style="font-family: monospace;">"difference"</span>. The x and y lag
  space in pixels around the initial x and y lag over which the cross-correlation 
  function is searched for the correlation peak, is specified by the
  <i>xwindow</i> and
  <i>ywindow</i>  parameters. These parameter define a range of x and y lags from
  -xwindow / 2 to xwindow / 2 and -ywindow / 2 to ywindow / 2 respectively. For
  a given input and reference image region, the
  execution time of XREGISTER will depend strongly on both the correlation
  algorithm chosen and
  the size of the search window. In general users should use discrete
  or difference correlation for small search windows and fourier
  correlation for large search windows.
  </p>
  <p>
  The x and y lags for each input and reference image
  region are computed by computing
  the position of the peak of the cross-correlation function in the
  search window using
  one of the four centering algorithms: <span style="font-family: monospace;">"none"</span>, <span style="font-family: monospace;">"centroid"</span>, <span style="font-family: monospace;">"sawtooth"</span>,
  and <span style="font-family: monospace;">"parabolic"</span>.
  </p>
  <p>
  The computed x and y shifts for each region and the final x and y shift
  for each input image (where the computed x and y shifts are just the negative
  of the computed x and y lags) are written to the shifts file <i>shifts</i>.
  If <i>databasefmt</i> is <span style="font-family: monospace;">"yes"</span> each results is written in a record whose name
  is either identical to the name of the input
  image or supplied by the user via the <i>records</i> parameter .
  If <i>databasefmt</i> is <span style="font-family: monospace;">"no"</span>, then a single containing the input image
  name and the computed x and y shifts is written to the output shifts file.
  </p>
  <p>
  If a list of output image names have been supplied then the x and y
  shifts will be applied to the input images to compute the output images
  using the interpolant type specified by <i>interp_type</i> and the
  boundary extension algorithm specified by <i>boundary</i> and <i>constant</i>. 
  </p>
  <p>
  If the <i>correlation</i> parameter is set to <span style="font-family: monospace;">"file"</span> then the shifts
  computed in a previous run of XREGISTER will be read from the <i>shifts</i>
  file and applied to the input images to compute the output images.
  If no record list is supplied by the user XREGISTER will for each input
  image search for
  a record whose name is the same as the input image name. If more than
  one record of the same name is found then the most recently written
  record will be used.
  </p>
  <p>
  XREGISTER does not currently trim the input images but it computes and
  prints the region over which they all overlap in the form of an image
  section. Although XREGISTER is designed for use with same sized images,
  it may be used with images of varying size.
  In this case it is possible for the calculated overlap region to be vignetted,
  as XREGISTER currently preserves the size of the input image when it shifts it.
  For example if an image is much smaller than the reference image
  it is possible for the image to be shifted outside of its own borders.
  If the smallest image is used as a reference this will not occur. If
  vignetting is detected the vignetted image section is printed on the 
  screen. Vignetting may also occur for a list of same-sized images
  if the reference image is not included in the input image list, and the
  computed shifts are all positive or negative as may occur in a time
  sequence. Choosing a reference image with  a shift which is in the
  middle of the observed range of shifts in x and y will remove this problem.
  </p>
  <p>
  In non-interactive mode the parameters are set at task startup
  and the input images are processed sequentially. If the <i>verbose</i>
  flag is set messages about the progress of the task are printed on the
  screen as the task is running.
  </p>
  <p>
  In interactive mode the user can mark the regions to be used
  to compute the cross-correlation function on the image display,
  define the initial shifts from the reference image to the input image
  on the image display, show/set the data and algorithm parameters,
  compute, recompute,  and plot the cross-correlation function, experiment
  with the various peak fitting algorithms, and overlay row and column
  plots of the input and reference images with and without the initial and / or
  computed shifts factored in.
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  The following graphics cursor commands are currently available in
  XREGISTER.
  </p>
  <div class="highlight-default-notranslate"><pre>
                  Interactive Keystroke Commands
  
  ?       Print help
  :       Colon commands
  t       Define the offset between the reference and the input image
  c       Draw a contour plot of the cross-correlation function
  x       Draw a column plot of the cross-correlation function
  y       Draw a line plot of the cross-correlation function
  r       Redraw the current plot
  f       Recompute the cross-correlation function
  o       Enter the image overlay plot submenu
  w       Update the task parameters
  q       Exit
  
                  Colon Commands
  
  :mark           Mark regions on the display
  :show           Show the current values of the parameters
  
                  Show/Set Parameters
  
  :reference      [string]    Show/set the current reference image name
  :input          [string]    Show/set the current input image name
  :regions        [string]    Show/set the regions list
  :shifts         {string]    Show/set the shifts database file name
  :coords         [string]    Show/set the current coordinates file name
  :output         [string]    Show/set the current output image name
  :records        [string]    Show/set the current database record name
  :xlag           [value]     Show/set the initial lag in x
  :ylag           [value]     Show/set the initial lag in y
  :dxlag          [value]     Show/set the incremental lag in x
  :dylag          [value]     Show/set the incremental lag in y
  :cregion        [value]     Show/set the current region
  :background     [string]    Show/set the background fitting function
  :border         [value]     Show/set border region for background fitting
  :loreject       [value]     Show/set low side k-sigma rejection
  :hireject       [value]     Show/set high side k-sigma rejection
  :apodize        [value]     Show/set percent of end points to apodize
  :filter         [string]    Show/set the default spatial filter
  :correlation    [string]    Show/set cross-correlation function
  :xwindow        [value]     Show/set width of correlation window in x
  :ywindow        [value]     Show/set width of correlation window in y
  :function       [string]    Show/set correlation peak centering function
  :xcbox          [value]     Show/set the centering box width in x
  :ycbox          [value]     Show/set the centering box width in y
  </pre></div>
  <p>
  The following submenu of image cursor commands is also available.
  </p>
  <div class="highlight-default-notranslate"><pre>
                  Image Overlay Plot Submenu
  
  ?       Print help
  c       Overlay the marked column of the reference image
          with the same column of the input image
  l       Overlay the marked line of the reference image
          with the same line of the input image
  x       Overlay the marked column of the reference image
          with the x and y lagged column of the input image
  y       Overlay the marked line of the reference image
          with the x and y lagged line of the input image
  v       Overlay the marked column of the reference image
          with the x and y shifted column of the input image
  h       Overlay the marked line of the reference image
          with the x and y shifted line of the input image
  q       Quit
  
                  Image Overlay Sub-menu Colon Commands
  
  :c  [m] [n]     Overlay the middle [mth] column of the reference image
                  with the mth [nth] column of the input image
  :l  [m] [n]     Overlay the middle [mth] line of the reference image
                  with the mth [nth]  line of the input image
  :x  [m]         Overlay the middle [mth] column of the reference image
                  with the x and y lagged column of the input image
  :y  [m]         Overlay the middle [mth] line of the reference image
                  with the x and y lagged line of the input image
  :v  [m]         Overlay the middle [mth] column of the reference image
                  with the x and y shifted column of the input image
  :h  [m]         Overlay the middle [mth] line of the reference image
                  with the x and y shifted line of the input image
  </pre></div>
  </section>
  <section id="s_algorithms">
  <h3>Algorithms</h3>
  <p>
  The cross-correlation function is computed in the following manner.
  The symbols I and R refer to the input and reference images respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  correlation = discrete
  
          &lt;I&gt; = SUMj SUMi { I[i+xlag,j+ylag] } / (Nx * Ny)
          &lt;R&gt; = SUMj SUMi { R[i,j] } / (Nx * Ny)
       sumsqI = sqrt (SUMj SUMi { (I[i+xlag,j+ylag] - &lt;I&gt;) ** 2 })
       sumsqR = sqrt (SUMj SUMi { (R[i,j] - &lt;R&gt;) ** 2 })
  
            X = SUMj SUMi { (I[i+xlag,j+ylag] - &lt;I&gt;) * (R[i,j] - &lt;R&gt;) }
                ----------------------------------------------------
                           sumsqI * sumsqR
  
  correlation = fourier
  
          &lt;I&gt; = SUMj SUMi { I[i,j] } / (Nx * Ny)
          &lt;R&gt; = SUMj SUMi { R[i,j] } / (Nx * Ny)
       sumsqI = sqrt (SUMj SUMi { (I[i,j] - &lt;I&gt;) ** 2 })
       sumsqR = sqrt (SUMj SUMi { (R[i,j] - &lt;R&gt;) ** 2 })
         FFTI = FFT { (I - &lt;I&gt;) / sumsqI }
         FFTR = FFT { (R - &lt;R&gt;) / sumsqR }
  
            X = FFTINV { FFTR * conj { FFTI } }
  
  correlation = difference
  
          &lt;I&gt; = SUMj SUMi { I[i+xlag,j+ylag] } / (Nx * Ny)
          &lt;R&gt; = SUMj SUMi { R[i,j] } / (Nx * Ny)
  
            X = SUMj SUMi { abs ((I[i+xlag,j+ylag] - &lt;I&gt;) - (R[i,j] - &lt;R&gt;)) }
            X = 1.0 - X / max { X }
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Register a list of images whose dimensions are all 256 by 256 pixels
  and whose shifts with respect to the reference image are all less than
  5.0 pixels, using the discrete cross-correlation algorithm and a search
  window of 21 pixels in x and y.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xregister @inimlist refimage [*,*] shifts.db out=@outimlist \
      xwindow=21 ywindow=21
  </pre></div>
  <p>
  2. Register the previous list of images, but compute the cross_correlation
  function using boxcar smoothed versions of the input images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xregister @binimlist brefimage [*,*] shifts.db xwindow=21 \
      ywindow=21
  
  cl&gt; xregister @inimlist refimage [*,*] shifts.db out=@outimlist \
      records=@binimlist correlation=file
  </pre></div>
  <p>
  3. Register the previous list of images but write the results to a simple
  text file instead of a text database file and do the actual shifting with
  the imshift task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xregister @binimlist brefimage [*,*] shifts.db xwindow=21 \
      ywindow=21 databasefmt-
  
  cl&gt; fields shifts.db 2,3 &gt; shifts
  
  cl&gt; imshift @inimlist @outimlist shifts_file=shifts
  </pre></div>
  <p>
  4. Register list of 512 by 512 pixel square solar sunspot images that were
  observed as a time series. Compute the cross-correlation function using
  Fourier techniques, a search window of 21 pixels in x and y, an initial
  shift of 10 pixels in x and 1 pixel in y, and use the computed shift of
  the previous image as the initial guess for the current image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; xregister @inimlist refimage [*,*] shifts.db out=@outimlist \
      xlag=10 ylag=1 dxlag=INDEF dylag=INDEF correlation=fourier \
      xwindow=21 ywindow=21
  </pre></div>
  <p>
  5. Register two 2K square images interactively using discrete cross-correlation
  and an initial search window of 15 pixels in x and y.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; display refimage
  
  cl&gt; xregister inimage refimage [900:1100,900:1100] shifts.db \
      xwindow=15 ywindow=15 interactive+
  
      ... a contour plot of the cross-correlation function appears
          with the graphics cursor ready to accept commands
  
      ... type x and y to get line and column plots of the cross-
          correlation function at various points and c to return
          to the default contour plot
  
      ... type ? to get a list of the available commands
  
      ... type :mark to mark a new region on the image display
  
      ... type f to recompute the cross-correlation function using
          the new data
  
      ... increase the search window to 21 pixels in x and y
          with the :xwindow 21 and :ywindow 21 commands
  
      ... type f to recompute the cross-correlation function with the
          new search window
  
      ... type o to enter the image data overlay plot submenu,
          move the cursor to a line in the displayed reference image
          and type l to see of plot of the line in the input and
          reference image, type h to see a plot of the same line in
          the reference image and the x and y shifted line in the input
          image, type q to return to the main menu
  
      ... type q to quit the task, and q again to verify the previous
          q command
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rv.fxcor,proto.imalign,images.imcombine,ctio.immatch,center1d,images.imshift
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'ALGORITHMS' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

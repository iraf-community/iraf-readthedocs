.. _xrshifts:

xrshifts: Compute shifts using x-correlation techniques
=======================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xrshifts inlist output shifts regions xlag ylag window cbox
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inlist">
  <dt><b>inlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inlist' Line='inlist' -->
  <dd>The list of input sky subtracted images. The input image list must be in order
  with each image offset from the previous one by approximately <i>xlag</i>
  pixels in x and <i>ylag</i> pixels in y.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output total offsets file suitable for input to the xnregistar task.
  Output contains the input image name, the total x offset, the total y offset,
  and the default exposure time in columns 1 through 4 respectively. The total
  x and y offsets of image N are defined as the shifts x(N) - x(1) and
  y(N) - y(1) required to place image N in the same coordinate system as image 1.
  The default exposure time is 1 time unit.
  </dd>
  </dl>
  <dl id="l_shifts">
  <dt><b>shifts = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shifts' Line='shifts = ""' -->
  <dd>The optional relative offsets file. Shifts contains the input image name,
  the relative x offset and the relative y offset in columns 1 through 3
  respectively. The relative offsets of image N are defined as the shifts
  x(N-1) - x(N) and y(N-1) - y(N) required to register image N to image N-1.
  </dd>
  </dl>
  <dl id="l_regions">
  <dt><b>regions</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='regions' Line='regions' -->
  <dd>The input image region used to compute the cross-correlation function. Regions
  should be defined so as to exclude areas of obviously bad data. By default the
  entire image is used.
  </dd>
  </dl>
  <dl id="l_xlag">
  <dt><b>xlag, ylag</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xlag' Line='xlag, ylag' -->
  <dd>The approximate relative offsets x(N) - x(N-1) and y(N) - y(N-1) between
  adjacent images in the input image list.
  </dd>
  </dl>
  <dl id="l_window">
  <dt><b>window</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='window' Line='window' -->
  <dd>The width of the cross-correlation function region to be computed and searched
  for peaks. The search window corresponds to shifts of - window / 2 &lt;= shift &lt;=
  window /2.  <i>Window</i> is automatically rounded up to the next nearest odd
  number.
  </dd>
  </dl>
  <dl id="l_cbox">
  <dt><b>cbox</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cbox' Line='cbox' -->
  <dd>The width of the box centered on the peak of the cross-correlation function
  used to compute the fractional pixel x and y center.
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background = <span style="font-family: monospace;">"none"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = "none"' -->
  <dd>The default background function to be subtracted from the input and reference
  image data in the correlation region before the cross-correlation function is
  computed. The options are:
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
  By default the cross-correlation function is computed in a manner which removes
  the mean intensity in the reference and input image regions from the data. For
  many data sets this <span style="font-family: monospace;">"correction"</span> is sufficient to remove first order background
  level effects from the computed cross-correlation function and  no additional
  background subtraction is required.
  </dd>
  </dl>
  <dl id="l_correlation">
  <dt><b>correlation = <span style="font-family: monospace;">"discrete"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='correlation' Line='correlation = "discrete"' -->
  <dd>The algorithm used to compute the cross-correlation function. The options
  are:
  <dl>
  <dt><b>discrete</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='discrete' Line='discrete' -->
  <dd>The cross-correlation function is calculated by computing the discrete
  convolution of the reference and imput image regions over the x and y
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
  </dd>
  </dl>
  <p>
  The algorithm used to compute the x and y position of the cross-correlation
  function peak.  The options are:
  </p>
  <dl id="l_none">
  <dt><b>none</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='none' Line='none' -->
  <dd>the position of the cross-correlation function peak is set to
  x and y position of the maximum pixel.
  </dd>
  </dl>
  <dl id="l_centroid">
  <dt><b>centroid</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='centroid' Line='centroid' -->
  <dd>the position of the cross-correlation function peak is calculated
  by computing the intensity-weighted mean of the marginal profiles of
  the cross-correlation function in x and y.
  </dd>
  </dl>
  <dl id="l_sawtooth">
  <dt><b>sawtooth</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sawtooth' Line='sawtooth' -->
  <dd>the position of the cross-correlation function peak is calculated
  by  convolving 1D slices in x and y through the cross-correlation function
  with a 1D sawtooth function and using the point at which the peak is
  bisected to determine the x and y position of the cross-correlation
  peak.
  </dd>
  </dl>
  <dl id="l_parabolic">
  <dt><b>parabolic</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='parabolic' Line='parabolic' -->
  <dd>a 1D parabola is fit to 1D slices in x and y through the cross-correlation
  function and the fitted coefficients are used to compute the peak of
  the cross-correlation function.
  </dd>
  </dl>
  <dl id="l_mark">
  <dt><b>mark</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mark' Line='mark' -->
  <dd>mark the peak of the cross-correlation function with the graphics cursor.
  This option will only work if <i>interactive</i> = <span style="font-family: monospace;">"yes"</span>.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_tolerance">
  <dt><b>tolerance = 5.0</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='tolerance' Line='tolerance = 5.0' -->
  <dd><p>
  The maximum permitted difference between the computed relative offsets
  and the initial values of <i>xlag\R and fIylag</i>. 
  </dd>
  </dl>
  </p>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='interactive' Line='interactive = no' -->
  <dd><p>
  Compute the cross-correlation function and relative offsets interactively ?
  </dd>
  </dl>
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  XRSHIFTS computes total offsets for the images in the input image list
  <i>inlist</i> and writes the results in a form suitable for input to the
  xnregistar task to <i>output</i>. If the <i>shifts</i> parameter is defined
  the relative offsets for adjacent images are written to the file <i>shifts</i>.
  XRSHIFTS requires the input image list to be ordered and also requires that
  the relative offsets between adjacent images are approximately equal
  to <i>xlag</i> and <i>ylag</i> pixels.
  XRSHIFTS computes the relative offsets between adjacent images by computing
  the peak of the cross-correlation function for each pair of adjacent images
  using the XREGISTER task.
  XREGISTER computes the cross-correlation function of pairs of adjacent images
  using data in <i>regions</i> and a correlation window of width <i>window</i>
  pixels. The maximum detectable shifts is +/- window / 2 pixels.  Window should
  be set large enough to detect the likely range of shifts. If <i>background</i>
  is set then the background is estimated and subtracted from the input image
  data before the cross-correlation function is computed. If <i>correlation</i>
  is <span style="font-family: monospace;">"fourier"</span> the cross-correlation function is computed using fourier
  transform techniques, otherwise it is computed directly. The position of the
  peak of the cross-correlation function is computed using <i>cbox</i> pixels
  centered around the correlation peak and the algorithm specified by
  <i>function</i>.
  If adjacent frames contain no objects in common or the computed shift is
  greater than <i>tolerance</i> the relative offsets are set to <i>xlag</i> and
  <i>ylag</i>. Total offsets are computed by summing the relative offsets.
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  1. Compute the total offsets for a series of 250 ONIS sky subtracted images
  which are offset by approximately 50 pixels in x and 0.5 pixels in y. Output
  both the total and relative offsets. 
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type simlist
  ss_kk07_001
  ss_kk07_002
  ss_kk07_003
  ...
  ...
  ss_kk07_249
  ss_kk07_250
  
  cl&gt; xrshifts @simlist offsets shifts [*,*] 50.0 0.5 31 9 tolerance=2.5
  
  cl&gt; xnregistar offsets "" "" "" kk07.mosaic kk07.corners
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
  xmshifts,xfshifts,xdshifts,xregister
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

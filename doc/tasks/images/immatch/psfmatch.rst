.. _psfmatch:

psfmatch: Match the point-spread functions of 1-D or 2-D images
===============================================================

**Package: immatch**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  psfmatch input reference psfdata kernel 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input images to be matched.
  </dd>
  </dl>
  <dl id="l_reference">
  <dt><b>reference</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reference' Line='reference' -->
  <dd>The list of reference images to which the input images are to be matched if
  <i>convolution</i> = <span style="font-family: monospace;">"image"</span>, or the list of reference image psfs if 
  <i>convolution</i> = <span style="font-family: monospace;">"psf"</span>. The reference image psf must be broader than the
  input image psf in at least one dimension.
  The number of reference images/psfs must be one or equal to the number of
  input images.
  </dd>
  </dl>
  <dl id="l_psfdata">
  <dt><b>psfdata</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='psfdata' Line='psfdata' -->
  <dd>The list of objects used to compute the psf matching function if
  <i>convolution</i> is <span style="font-family: monospace;">"image"</span>, or the list of input image psfs if 
  <i>convolution</i> is <span style="font-family: monospace;">"psf"</span>. In the former case <i>psfdata</i> may be:
  1) a string containing the x and y coordinates of a single object,
  e.g. <span style="font-family: monospace;">"51.0 105.0"</span> or 2) the name of a text file containing a list of
  objects, and the number of objects
  files must equal the number of reference images. In the latter case
  the number of input psf images must equal the number of input images.
  </dd>
  </dl>
  <dl id="l_kernel">
  <dt><b>kernel</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='kernel' Line='kernel' -->
  <dd>The list of input/output psf matching function images to be convolved with the
  input images to produce the output images. The number of kernel images
  must equal the number of input images.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>The list of output matched images. If <i>output</i> is the NULL string
  then the psf matching function is computed for each input image and written to
  <i>kernel</i> but no output images are written. If <i>output</i> is not NULL
  then the number of output images must equal the number of input images.
  </dd>
  </dl>
  <dl id="l_convolution">
  <dt><b>convolution = <span style="font-family: monospace;">"image"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='convolution' Line='convolution = "image"' -->
  <dd>The algorithm used to compute the psf matching function. The options are:
  <dl>
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='image' Line='image' -->
  <dd>The psf matching function is computed directly from the reference and input
  image data using the objects specified in <i>psfdata</i>, the data
  regions specified by <i>dnx</i>, <i>dny</i>, <i>pnx</i>, and <i>pny</i>,
  and the convolution theorem.
  </dd>
  </dl>
  <dl>
  <dt><b>psf   </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='psf' Line='psf   ' -->
  <dd>The psf matching function is computed directly from pre-computed
  reference and input image psfs using the convolution theorem.
  </dd>
  </dl>
  <dl>
  <dt><b>kernel</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='kernel' Line='kernel' -->
  <dd>No psf matching function is computed. Instead the psf matching function
  is  read from the input image <i>kernel</i>.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_dnx">
  <dt><b>dnx = 31, ls dny = 31</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dnx' Line='dnx = 31, ls dny = 31' -->
  <dd>The x and y width of the data region to be extracted around each object. The
  data region should be big enough to include both object and sky data.
  <i>Dnx</i> and <i>dny</i> are not used if <i>convolution</i> is <span style="font-family: monospace;">"psf"</span> or
  <span style="font-family: monospace;">"kernel"</span>.
  </dd>
  </dl>
  <dl id="l_pnx">
  <dt><b>pnx = 15, pny = 15</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pnx' Line='pnx = 15, pny = 15' -->
  <dd>The x and y width of the psf matching function to be computed which must be
  less than <i>dnx</i> and <i>dny</i> respectively. The psf
  matching function should be kept as small as possible to minimize
  the time required to compute the output image.
  <i>Pnx</i> and <i>Pny</i> are not used if <i>convolution</i> is <span style="font-family: monospace;">"psf"</span> or
  <span style="font-family: monospace;">"kernel"</span>.
  </dd>
  </dl>
  <dl id="l_center">
  <dt><b>center = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='center' Line='center = yes' -->
  <dd>Center the objects in <i>psfdata</i> before extracting the data from the
  input and reference images. Centering should be turned off if the objects
  are non-stellar and do not have well-defined centers.
  Centering is turned off if <i>convolution</i> is <span style="font-family: monospace;">"psf"</span> or
  <span style="font-family: monospace;">"kernel"</span>.
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background = median</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = median' -->
  <dd>The default background function to be subtracted from the input
  and reference image data in each object region before the
  psf matching function is computed. The background is computed using
  data inside the data extraction region defined by <i>dnx</i> and <i>dny</i>
  but outside the kernel region defined by <i>pnx</i> and <i>pny</i>.
  Background fitting is turned off if <i>convolution</i> is <span style="font-family: monospace;">"psf"</span> or
  <span style="font-family: monospace;">"kernel"</span>.
  The options are:
  <dl>
  <dt><b>none</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='none' Line='none' -->
  <dd>no background subtraction is done.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"insky refsky"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"insky refsky"' -->
  <dd>the numerical values of insky and refsky are subtracted from the
  input and reference image respectively.
  </dd>
  </dl>
  <dl>
  <dt><b>mean</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='mean' Line='mean' -->
  <dd>the mean of the input and reference image region is computed and subtracted
  from the image data.
  </dd>
  </dl>
  <dl>
  <dt><b>median</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='median' Line='median' -->
  <dd>the median of the input and reference image region is computed and subtracted
  from the data.
  </dd>
  </dl>
  <dl>
  <dt><b>plane</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='plane' Line='plane' -->
  <dd>a plane is fit to the input and reference image region and subtracted
  from the data.
  </dd>
  </dl>
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
  cosine bell function before the psf matching function is computed.
  Apodizing is turned off if <i>convolution</i> is <span style="font-family: monospace;">"psf"</span> or
  <span style="font-family: monospace;">"kernel"</span>.
  </dd>
  </dl>
  <dl id="l_fluxratio">
  <dt><b>fluxratio = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fluxratio' Line='fluxratio = INDEF' -->
  <dd>The ratio of the integrated flux of the reference objects to the integrated
  flux of the input objects.
  By default <i>fluxratio</i> is computed directly from the input data.
  </dd>
  </dl>
  <dl id="l_filter">
  <dt><b>filter = <span style="font-family: monospace;">"replace"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filter' Line='filter = "replace"' -->
  <dd>The filter used to remove high frequency noise from the psf
  matching function. Filtering is not performed if <i>convolution</i>
  is <span style="font-family: monospace;">"kernel"</span>. The options are:
  <dl>
  <dt><b>cosbell</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='cosbell' Line='cosbell' -->
  <dd>apply a cosine bell taper to the psf matching function in frequency space. 
  </dd>
  </dl>
  <dl>
  <dt><b>replace</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='replace' Line='replace' -->
  <dd>replace the high-frequency low signal-to-noise components of the psf matching
  function with a gaussian model computed from the low frequency
  high signal-to-noise components of the matching function.
  </dd>
  </dl>
  <dl>
  <dt><b>model</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='model' Line='model' -->
  <dd>replace the entire psf matching function with a gaussian model fit to the
  low frequency high signal-to-noise components of the matching function.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_sx1">
  <dt><b>sx1 = INDEF, sx2 = INDEF, sy1 = INDEF, sy2 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sx1' Line='sx1 = INDEF, sx2 = INDEF, sy1 = INDEF, sy2 = INDEF' -->
  <dd>The limits of the cosine bell taper in frequency space. Frequency components
  inside sx1 and sy1 are unaltered. Frequency components outside sx2 and sy2
  are set to 0.0. By default sx1 and sy1 are set to 0.0,
  and sx2 and sy2 are set to the largest frequency present in the data.
  </dd>
  </dl>
  <dl id="l_radsym">
  <dt><b>radsym = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radsym' Line='radsym = no' -->
  <dd>Compute a radially symmetric cosine bell function ?
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = 0.2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 0.2' -->
  <dd>The low frequency cutoff in fraction of the total input image spectrum
  power for the filtering options <span style="font-family: monospace;">"replace"</span> and <span style="font-family: monospace;">"model"</span>.
  </dd>
  </dl>
  <dl id="l_normfactor">
  <dt><b>normfactor = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='normfactor' Line='normfactor = 1.0' -->
  <dd>The total power in the computed psf matching function <i>kernel</i>. By default
  the psf matching function is normalized.  If <i>normfactor</i>
  is set to INDEF, then the total power is set to <i>fluxratio</i>.
  <i>Normfactor</i> is not used if <i>convolution</i> is set <span style="font-family: monospace;">"kernel"</span>.
  </dd>
  </dl>
  <dl id="l_boundary_type">
  <dt><b>boundary_type = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary_type' Line='boundary_type = "nearest"' -->
  <dd>The boundary extension algorithm used to compute the output matched
  image.  The options are:
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
  <dt><b>constant = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constant' Line='constant = 0.0' -->
  <dd>The default constant for constant boundary extension.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Compute the psf matching function for each image
  interactively using graphics cursor and, optionally, image cursor input.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose' -->
  <dd>Print messages about the progress of the task in non-interactive mode.
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
  PSFMATCH computes the convolution kernel required to match the
  point-spread functions
  of the input images <i>input</i> to the point-spread functions of
  the reference images <i>reference</i> using either the image data 
  or pre-computed psfs and the convolution theorem.
  The computed psf matching functions are stored in the <i>kernel</i> images.
  If a non-NULL list of output images <i>output</i> is
  specified the input images are
  convolved with the kernel images to produce a list of psf matched output
  images. PSFMATCH requires
  that the input and reference images be spatially registered
  and that the reference images have poorer resolution (broader PSF)
  than the input images in at least one dimension.
  </p>
  <p>
  If <i>convolution</i> = <span style="font-family: monospace;">"image"</span>, the matching function is computed directly
  from the input and reference image data using the objects listed in
  <i>psfdata</i> and the convolution theorem as described in the ALGORITHMS
  section. <i>psfdata</i> is interpreted as either: 1) a
  string defining the coordinates of a single object e.g. <span style="font-family: monospace;">"103.3 189.2"</span> or 2)
  the name of a text file containing the coordinates of one or 
  more objects, one object per line, with the x and y coordinates
  in columns 1 and 2 respectively.  The object coordinates, the
  size of the data region to be extracted <i>dnx</i>
  by <i>dny</i>, and the size of the kernel to be computed <i>pnx</i> and
  <i>pny</i>, determine 
  the input and reference image regions used to compute the psf matching
  function.
  These image regions should be selected with care. Ideal regions 
  contain a single high signal-to-noise unsaturated star which has no close
  neighbors and is well centered on a pixel.
  </p>
  <p>
  If <i>center</i> is <span style="font-family: monospace;">"yes"</span> and <i>convolution</i> is <span style="font-family: monospace;">"image"</span>, the objects
  in <i>psfdata</i> are centered before
  the data region is extracted.  Centering should be on if the objects
  are stellar, particularly if their coordinates were read from the image
  display cursor. Centering should be off if the objects are non-stellar and
  do not have well-defined centers.
  </p>
  <p>
  If the <i>background</i> fitting algorithm is other than <span style="font-family: monospace;">"none"</span> and
  <i>convolution</i> is <span style="font-family: monospace;">"image"</span>, the background for each object is fit using 
  data inside the region defined by
  <i>dnx</i> and <i>dny</i> but outside the region defined by
  <i>pnx</i> by <i>pny</i>. Bad data can be removed from the
  background fit by setting the parameters <i>loreject</i> and <i>hireject</i>.
  A cosine bell function is applied to the edges of the data region
  after background fitting but before computing the psf matching function
  if the <i>apodize</i> parameter is &gt; 0.0.
  </p>
  <p>
  If <i>psfdata</i> contains more than one object, the extracted image data
  is weighted by the total intensity in the extracted region after
  background subtraction, and averaged to produce a single smoothed
  data region for each reference and input image.
  </p>
  <p>
  If <i>convolution</i> = <span style="font-family: monospace;">"psf"</span>,
  the psf matching function is computed directly from the input image
  and reference
  image point-spread functions
  using the convolution theorem as described in the ALGORITHMS section.
  In this case  <i>psfdata</i> is the list of input image psfs  and
  <i>reference</i> are the corresponding reference image psfs written by
  by some external psf modeling task. 
  If <i>convolution</i> is <span style="font-family: monospace;">"psf"</span>,
  centering and background fitting
  are assumed to have been performed by the psf modeling task and are not
  performed by PSFMATCH.
  </p>
  <p>
  PSFMATCH requires that the total power in the psf matching function
  before normalization be the ratio
  of the integrated flux of the reference image/psf over the integrated
  flux of the input image/psf. If <i>fluxratio</i> is INDEF, PSFMATCH
  estimates this number internally as described in the ALGORITHMS section,
  otherwise the <i>fluxratio</i> is set to the value supplied by the user.
  </p>
  <p>
  If <i>convolution</i> is <span style="font-family: monospace;">"kernel"</span>, PSFMATCH reads the psf matching function
  from the images in <i>kernel</i>  which were either
  created during a previous run of PSFMATCH or by a separate task.
  </p>
  <p>
  PSFMATCH provides several options for filtering out the ill-behaved
  noise-dominated high frequency components of the psf matching function
  that are produced when the ratio of reference / input image of psf
  fourier transforms is taken.
  </p>
  <p>
  If <i>filter</i> is set to <span style="font-family: monospace;">"cosbell"</span>, a cosine bell function
  with a taper defined by <i>sx1</i>, <i>sx2</i>, <i>sy1</i>, and <i>sy2</i> and
  symmetry defined by radsym is applied to
  the psf matching function in frequency space. This filter
  sets all the frequency components greater than <i>sx2</i> and <i>sy2</i>
  to 0.0 and leaves all frequency components inside <i>sx1</i> and <i>sy1</i>
  unaltered. Users should exercise this option with caution as the effect
  of the filtering process can be to significantly
  broaden the computed psf matching function as described in the ALGORITHMS
  section.
  </p>
  <p>
  An alternative approach to dealing with the noisy
  high frequency components of the psf
  matching function it is to replace them with a reasonable guess. If the
  matching function is approximately gaussian then its fourier transform is also
  approximately gaussian and the low frequency components can be modeled
  reliably with an elliptical gaussian function. The model derived from the low
  frequency components of the matching can then be used to replace the high
  frequency components.
  If <i>filter</i> is set to <span style="font-family: monospace;">"replace"</span>, those high frequency components
  of the matching function  which have less than a fraction
  <i>threshold</i> of their total power in the equivalent high frequency
  components of the divisor or input image transform,
  are replaced by a model computed by fitting a gaussian to the low frequency
  components of the matching function, as described in the ALGORITHMS section.
  If <i>filter</i> = <span style="font-family: monospace;">"model"</span> then the entire psf matching function
  is replaced with the best fitting gaussian model.
  </p>
  <p>
  Another problem can arise during the computation of the psf matching
  function . Occasionally it is not possible by means of a single execution
  of PSFMATCH to match the reference and input image psfs. An example
  of this situation
  is the case where the seeing of the reference and input images
  was comparable but the declination guiding error in the reference
  image was larger than the error in the input image.
  In this case input image  needs to be convolved to the resolution of 
  the reference image. However it is also the case
  that the guiding error in ra in the input image is greater than the guiding
  error  in ra in the reference image. In this case the reference image needs
  to be convolved to the resolution of the input image along the other axis.
  If no corrective action is taken by the task, the 
  first time PSFMATCH is run the values of the psf matching function along
  the ra axis will be greater than the computed fluxratio, resulting in
  unrealistic action
  along this axis. PSFMATCH avoids this situation by internally limiting
  the psf matching function to a maximum value of fluxratio computed as described
  above. 
  </p>
  <p>
  By default the psf matching function is normalized to unit power before 
  output. This may not be what is desired since if carefully computed the
  internally computed quantity a contains information about differences
  in exposure time, transparency, etc. If <i>normfactor</i> is set to
  a number of INDEF, the total power of the psf matching function will be
  set to that value of <i>fluxratio</i> respectively.
  </p>
  <p>
  If a list of output images names has been supplied then the computed
  psf matching function is applied to the input images to produce
  the output images using the boundary extension algorithm
  defined by <i>boundary</i> and <i>constant</i>.
  </p>
  <p>
  In non-interactive mode the parameters are set at task startup time and
  the input images are processed sequentially. If the <i>verbose</i> flag
  is set messages about the progress of the task are printed on he 
  screen as the task is running.
  </p>
  <p>
  In interactive mode the user can mark the regions to be used to compute
  the psf matching function on the image display, show/set the data
  and algorithm parameters, compute, recompute, and plot the psf matching
  function and its accompanying fourier spectrum, and experiment with the
  various filtering and modeling options.
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  The following graphics cursor commands are currently available in
  PSFMATCH.
  </p>
  <div class="highlight-default-notranslate"><pre>
          Interactive Keystroke Commands
  
  ?       Print help
  :       Colon commands
  k       Draw a contour plot of the psf matching kernel
  p       Draw a contour plot of the psf matching kernel fourier spectrum
  x       Draw a column plot of the psf matching kernel / fourier spectrum
  y       Draw a line plot of the psf matching kernel / fourier spectrum
  r       Redraw the current plot
  f       Recompute the psf matching kernel
  w       Update the task parameters
  q       Exit
  
          Colon Commands
  
  :mark   [file]          Mark objects on the display
  :show                   Show current values of the parameters
  
          Show/Set Parameters
  
  :input      [string]        Show/set the current input image name
  :reference  [string]        Show/set the current reference image/psf name
  :psf        [file/string]   Show/set the objects/input psf list
  :psfimage   [string]        Show/set the current input psf name
  :kernel     [string]        Show/set the current psf matching kernel name
  :output     [string]        Show/set the current output image name
  
  :dnx        [value]         Show/set x width of data region(s) to extract
  :dny        [value]         Show/set y width of data region(s) to extract
  :pnx        [value]         Show/set x width of psf matching kernel
  :pny        [value]         Show/set y width of psf matching kernel
  :center     [yes/no]        Show/set the centering switch
  :background [string]        Show/set the background fitting function
  :loreject   [value]         Show/set low side k-sigma rejection parameter
  :hireject   [value]         Show/set high side k-sigma rejection parameter
  :apodize    [value]         Show/set percent of endpoints to apodize
  
  :filter     [string]        Show/set the filtering algorithm
  :fluxratio  [value]         Show/set the reference/input psf flux ratio
  :sx1        [value]         Show/set inner x frequency for cosbell filter
  :sx2        [value]         Show/set outer x frequency for cosbell filter
  :sy1        [value]         Show/set inner y frequency for cosbell filter
  :sy2        [value]         Show/set outer y frequency for cosbell filter
  :radsym     [yes/no]        Show/set radial symmetry for cosbell filter
  :threshold  [value]         Show/set %threshold for replace/modeling filter
  :normfactor [value]         Show/set the kernel normalization factor
  </pre></div>
  </section>
  <section id="s_algorithms">
  <h3>Algorithms</h3>
  <p>
  The problem of computing the psf matching function can expressed
  via the convolution theorem as shown below.
  In the following expressions r is the reference
  image data or reference image psf, i is the input image data or input image
  psf, k is the unit power psf matching
  function,
  a is a scale factor specifying the ratio of the total
  power in the reference data or psf to the total power in the input data or
  psf, * is the convolution operator, and FT is the fourier transform operator.
  </p>
  <div class="highlight-default-notranslate"><pre>
  r = ak * d
  R = FT (r)
  I = FT (i)
  aK = R / I
  ak = FT (aK)
  </pre></div>
  <p>
  The quantity ak is the desired psf matching function and aK is its fourier
  transform.
  </p>
  <p>
  If the background was accurately removed from the image or psf data before the
  psf matching function was computed, the quantity a is simply the central
  frequency component of the computed psf matching function aK as shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  aK[0,0] = a = sum(r) / sum(i)
  </pre></div>
  <p>
  If the background was not removed from the image or psf data before the
  psf matching function was computed the previous expression is not valid.
  The computed aK[0,0] will include an offset and a must be estimated
  in some other manner. The approach taken by PSFMATCH in this circumstance
  is to fit a gaussian model to the absolute value of 1st and 2nd frequencies
  of R and I along the x and y axes independently, average the fitted x and y
  amplitudes, and set aK[0,0] to the ratio of the resulting fitted amplitudes
  as shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  a = amplitude (R) / amplitude (I)
    = (sum(r) - sum(skyr)) / (sum(i) - sum(skyi))
  aK[0,0] = a
  </pre></div>
  <p>
  This approach will work well as long as the image data or psf is reasonably
  gaussian but may not work well in arbitrary image regions. If the user is
  dissatisfied with either of the techniques described above they can
  set aK[0,0] to a pre-determined value of their own.
  </p>
  <p>
  If a filter is applied to the computed psf matching function in frequency
  space then instead of computing
  </p>
  <div class="highlight-default-notranslate"><pre>
  ak = FT (aK)
  </pre></div>
  <p>
  PSFMATCH actually computes
  </p>
  <div class="highlight-default-notranslate"><pre>
  ak' = FT (aKF) = ak * f
  </pre></div>
  <p>
  where F is the applied filter in frequency space and f is its
  fourier transform. Care should be taken in applying any filter.
  For example if F is the step function, then ak' will be the desired kernel
  ak convolved with f, a sinc function of frequency 2 * PI / hwidth where
  hwidth is the half-width of the step function, and the resulting k'
  will be too broad.
  </p>
  <p>
  If the user chooses to replace the high frequency components of the psf
  matching function with a best guess, PSFMATCH performs the following
  steps:
  </p>
  <div class="highlight-default-notranslate"><pre>
  1) fits an elliptical gaussian to those frequency components of the fourier
  spectrum of aK for which for which the amplitude of I is greater
  than threshold * I[0,0] to determine the geometry of the ellipse
  
  2) uses the fourier shift theorem to preserve the phase information in the
  model and solve for any x and y shifts
  
  3) replace those frequency components of aK for which the fourier spectrum
  of I is less than threshold * I[0,0] with the model values
  
                  or alternatively
  
  replace all of aK with the model values
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Psf match a list of input images taken at different epochs with variable
  seeing conditions to a reference image with the poorest seeing by marking
  several high signal-to-noise isolated stars on the displayed reference image
  and computing the psf matching function directly from the input and reference
  image data. User makes two runs with psfmatch one to compute and check the
  kernel images and one to match the images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; display refimage 1 fi+
  
  cl&gt; rimcursor &gt; objects
  
  cl&gt; psfmatch @inimlist refimage objects @kernels dnx=31 \
      dny=31 pnx=15 pny=15
  
  cl&gt; imstat @kernels
  
  cl&gt; psfmatch @inlist refimage objects @kernels          \
      output=@outlist convolution="kernel"
  </pre></div>
  <p>
  2. Psf match two spectra using a high signal-to-noise portion of the
  data in the middle of the spectrum. Since the spectra are registered
  spatially and there is little data available for background fitting the
  user chooses to turn centering off and set the backgrounds manually.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; psfmatch inspec refspec "303.0 1.0" kernel         \
      output=outspec dnx=31 dny=31 pnx=15 pny=15 center- \
      back="403.6 452.0"
  </pre></div>
  <p>
  3. Psf match two images using psf functions inpsf and refpsf computed with
  the daophot package phot/psf/seepsf tasks. Since the kernel is fairly
  large use the stsdas fourier package task fconvolve to do the actual
  convolution. The boundary extension algorithm in fconvolve is equivalent
  to setting the psfmatch boundary extension parameters boundary and
  constant to <span style="font-family: monospace;">"constant"</span> and <span style="font-family: monospace;">"0.0"</span> respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; psfmatch inimage refpsf inpsf kernel convolution=psf
  
  cl&gt; fconvolve inimage kernel outimage
  </pre></div>
  <p>
  4. Psf match two images interactively using the image data itself to
  compute the psf matching function.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; psfmatch inimage refimage objects kernel interactive+
  
      ... a contour plot of the psf matching function appears
          with the graphics cursor ready to accept commands
  
      ... type x and y to get line and column plots of the psf
          matching function at various points and k to return
          to the default contour plot
  
      ... type ? to get a list of the available commands
  
      ... type :mark to define a new set of objects
  
      ... type f to recompute the psf matching function using
          the new objects
  
      ... increase the data window to 63 pixels in x and y
          with the :dnx 63 and :dny 63 commands, at the
          same time increase the psf function size to 31 with
          the colon commands :pnx 31 and :pny 31
  
      ... type f to recompute the psf matching function using
          the new data and kernel windows
  
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
  convolve, gauss, stsdas.fconvolve, digiphot.daophot.psf
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'ALGORITHMS' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

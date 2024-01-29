.. _xfshifts:

xfshifts: Compute shifts using star finding and centroiding techniques
======================================================================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xfshifts inlist output shifts hwhmpsf threshold xlag ylag cbox
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
  <dl id="l_hwhmpsf">
  <dt><b>hwhmpsf = 1.25</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hwhmpsf' Line='hwhmpsf = 1.25' -->
  <dd>The approximate half-width at half-maximum of the image PSF in pixels. If the
  PSF width varies significantly over the sequence hwhmpsf should be set to the
  average value for the sequence.
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = 50.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 50.0' -->
  <dd>The object detection threshold above local background in ADU. Threshold should
  be set no lower than 4 * sigma where sigma is the standard deviation of the
  background pixels in ADU.
  </dd>
  </dl>
  <dl id="l_xlag">
  <dt><b>xlag = 0.0, ylag = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xlag' Line='xlag = 0.0, ylag = 0.0' -->
  <dd>The approximate relative offsets x(N) - x(N-1) and y(N) - y(N-1) between
  adjacent images in the input image list.
  </dd>
  </dl>
  <dl id="l_cbox">
  <dt><b>cbox = 7.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cbox' Line='cbox = 7.0' -->
  <dd>The centering box size in pixels.
  </dd>
  </dl>
  <dl id="l_fradius">
  <dt><b>fradius = 2.5 (hwhmpsf)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fradius' Line='fradius = 2.5 (hwhmpsf)' -->
  <dd>The fitting radius in units of hwhmpsf. Fradius defines the size of the
  Gaussian kernel used to compute the density enhancement image and the size
  of the image region used to do the moment analysis in the object detection
  step.
  </dd>
  </dl>
  <dl id="l_sepmin">
  <dt><b>sepmin = 5.0 (hwhmpsf)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sepmin' Line='sepmin = 5.0 (hwhmpsf)' -->
  <dd>The minimum separation for detected objects in units of hwhmpsf.
  </dd>
  </dl>
  <dl id="l_datamin">
  <dt><b>datamin = INDEF, datamax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datamin' Line='datamin = INDEF, datamax = INDEF' -->
  <dd>The minimum and maximum good data values in ADU. Datamin and datamax
  default to the constants -MAX_REAL and MAX_REAL respectively.
  </dd>
  </dl>
  <dl id="l_roundlo">
  <dt><b>roundlo = 0.0, roundhi = 0.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='roundlo' Line='roundlo = 0.0, roundhi = 0.5' -->
  <dd>The minimum and maximum ellipticity values for detected objects, where
  ellipticity is defined as 1 - b / a, and a and b are the semi-major and
  semi-minor object axis lengths respectively.
  </dd>
  </dl>
  <dl id="l_sharplo">
  <dt><b>sharplo = 0.5, sharphi = 2.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sharplo' Line='sharplo = 0.5, sharphi = 2.0' -->
  <dd>The minimum and maximum sharpness values of the detected objects, where
  sharpness is defined to be the ratio of the object size determined by
  moments analysis to the hwhmpsf parameter value.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 3' -->
  <dd>The maximum number of centroiding iterations.
  </dd>
  </dl>
  <dl id="l_maxshift">
  <dt><b>maxshift = 5.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxshift' Line='maxshift = 5.0' -->
  <dd>The maximum centroiding x and y shifts in pixels.
  </dd>
  </dl>
  <dl id="l_nxblock">
  <dt><b>nxblock = INDEF, nyblock = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxblock' Line='nxblock = INDEF, nyblock = INDEF' -->
  <dd>The working block size. If undefined nxblock and nyblock default to the number
  of columns and rows in the input image respectively.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XFSHIFTS computes total offsets for the images in the input image list
  <i>inlist</i> and writes the results in a form suitable for input to the
  xnregistar task to <i>output</i>. If the <i>shifts</i> parameter is defined
  the relative offsets for adjacent images are written to the file <i>shifts</i>.
  </p>
  <p>
  XFSHIFTS requires the input image list to be ordered and also requires that
  the relative offsets between adjacent images are approximately equal
  to <i>xlag</i> and <i>ylag</i> pixels.
  </p>
  <p>
  XFSHIFTS computes the relative offsets between adjacent images by first
  detecting objects in each input image using the STARFIND task,  and then
  centroidiing the object lists in adjacent images and computing relative
  shifts using the IMCENTROID task.
  </p>
  <p>
  STARFIND searches the input images for local density maxima with half-widths at
  half-maxima of ~ <i>hwhmpsf</i> and peak amplitudes greater than <i>threshold</i>
  counts above the local background, which are brighter than all surrounding
  objects within a radius of <i>sepmin</i> * <i>hwhmpsf</i> pixels. Data within
  <i>fradius</i> * <i>hwhmpsf</i> pixels of the detected density maximum and within
  the good data range defined by the <i>datamin</i> and <i>datamax</i> parameters
  are used to estimate the object position, shape, and size relative to the PSF.
  Objects outside the shape and size limits specified by the <i>roundlo</i>,
  <i>roundhi</i>, <i>sharplo</i>, and <i>sharphi</i> parameters are eliminated from
  the final object list. By default STARFIND reads the entire input image into
  memory. If the input images become too large or memory is limited the
  <i>nyblock</i> parameter can be set. For the sake of efficiency <i>nxblock</i>
  should be left set to INDEF so that XFSHIFTS always operates on an integral
  number of image lines. More information on the STARFIND algorithms can be found
  in the STARFIND task help page.
  </p>
  <p>
  IMCENTROID computes accurate centers for all the detected objects in 
  adjacent image pairs using a simple centroiding algorithm and a centering box
  size of <i>cbox</i>. Objects that cannot be centered in <i>niterate</i> or
  fewer iterations or whose x and y shifts deviate by more than <i>maxshift</i>
  pixels from the expected shifts in both image are rejected. The remaining
  objects are used to compute the relative offsets between adjacent images.
  If adjacent frames contain no objects in common the relative offsets are set
  to <i>xlag</i> and <i>ylag</i>. Total offsets are computed by summing the
  relative offsets.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the total offsets for a series of 250 ONIS sky subtracted images
  which are offset by approximately 50 pixels in x and 0.5 pixels in y. Output
  both the total and relative offsets. Since the noise in the sky background
  for these images is around 12 ADU use a detection threshold of 50 ADU.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type simlist
  ss_kk07_001
  ss_kk07_002
  ss_kk07_003
  ...
  ...
  ss_kk07_249
  ss_kk07_250
  
  cl&gt; xfshifts @simlist offsets shifts 1.5 50.0 50.0 0.5 9.0
  
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
  <p>
  xmshifts,xrshifts,xdshifts,starfind,imcentroid
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

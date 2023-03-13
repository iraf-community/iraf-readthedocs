.. _imalign:

imalign: Align and register 2-D images using a reference pixel list
===================================================================

**Package: immatch**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imalign input reference coords output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The input images to be shifted and trimmed.  The input image list should
  contain the reference image so that its borders are
  used in the computation of the overlap region.
  </dd>
  </dl>
  <dl id="l_reference">
  <dt><b>reference</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reference' Line='reference' -->
  <dd>The reference image to which the input images will be aligned. 
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords' -->
  <dd>A text file containing the reference image coordinates of the registration
  objects to be centered in each image, one object per line with the x and y
  coordinates in columns one and two respectively.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output images. 
  </dd>
  </dl>
  <dl id="l_shifts">
  <dt><b>shifts = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shifts' Line='shifts = ""' -->
  <dd>A text file containing the initial estimate for each image of the
  shift in each axis relative to the reference image.  These
  estimates are used to modify the coordinates of the registration
  objects prior to centering.  The format of the file is one image per
  line with the x and y shifts in columns one and two respectively.
  The sense of the shifts is such that: <i>Xshift=Xref-Xin</i> and
  <b>Yshift=Yref-Yin</b>.  If <i>shifts</i> is null, a coarse centering
  pass will be made to attempt to determine the initial shifts.
  </dd>
  </dl>
  <dl id="l_boxsize">
  <dt><b>boxsize = 7</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boxsize' Line='boxsize = 7' -->
  <dd>The size in pixels of the box to use for the final centering, during
  which all the sources in <i>coords</i> are recentered in each image
  using the initial estimate of the relative shift for each image.
  Care should be taken to choose an appropriate value for this parameter,
  since it is highly data dependent.
  </dd>
  </dl>
  <dl id="l_bigbox">
  <dt><b>bigbox = 11</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bigbox' Line='bigbox = 11' -->
  <dd>The size in pixels of the box to use for coarse centering.  The coarse
  pass through the centering algorithm is made with the box centered at
  the nominal position of the first source in the coordinate list.
  Coarse centering is performed only if the shifts file is undefined.
  Care should be taken to choose an appropriate value for this parameter,
  since it is highly data dependent.  Large values should be suspect until
  the final results are checked to see that the centering did not converge
  on the wrong coordinates, although the usual result for an inappropriate
  <i>bigbox</i> size is that the algorithm fails to converge and the task
  aborts.
  </dd>
  </dl>
  <dl id="l_negative">
  <dt><b>negative = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='negative' Line='negative = no' -->
  <dd>Are the features negative ?
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background = INDEF' -->
  <dd>The absolute reference level for the marginal centroid calculation.
  If background is INDEF, this is set to the mean value (between the
  thresholds) of the individual sources.
  </dd>
  </dl>
  <dl id="l_lower">
  <dt><b>lower = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lower' Line='lower = INDEF' -->
  <dd>The lower threshold for the data.  Individual pixels less than this
  value will be given zero weight in the centroids.
  </dd>
  </dl>
  <dl id="l_upper">
  <dt><b>upper = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='upper' Line='upper = INDEF' -->
  <dd>The upper threshold for the data.  Individual pixels greater than this
  value will be given zero weight in the centroids.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 3' -->
  <dd>The maximum number of centering iterations to perform.  The centering
  will halt when this limit is reached or when the desired Itolerance
  is achieved.
  </dd>
  </dl>
  <dl id="l_tolerance">
  <dt><b>tolerance = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tolerance' Line='tolerance = 0' -->
  <dd>The tolerance for convergence of the centering algorithm.  This is the
  integral shift of the centering box from one iteration to the next.
  </dd>
  </dl>
  <dl id="l_maxshift">
  <dt><b>maxshift = INDEFR</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxshift' Line='maxshift = INDEFR' -->
  <dd>The maximum permitted difference between the predicted shift and the
  the computed shift for each object. Objects with shifts greater than
  maxshift are ignored. If maxshift is undefined no shift checking is done.
  </dd>
  </dl>
  <dl id="l_shiftimages">
  <dt><b>shiftimages = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shiftimages' Line='shiftimages = yes' -->
  <dd>If shiftimages is yes, the IMSHIFT task will be used to align the
  images.  If shiftimages is no, the images will not be aligned, but
  the coordinates will still be centered.
  </dd>
  </dl>
  <dl id="l_interp_type">
  <dt><b>interp_type = <span style="font-family: monospace;">"spline3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interp_type' Line='interp_type = "spline3"' -->
  <dd>The interpolation function used by the IMSHIFT task.
  </dd>
  </dl>
  <dl id="l_boundary_type">
  <dt><b>boundary_type = <span style="font-family: monospace;">"constant"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary_type' Line='boundary_type = "constant"' -->
  <dd>The boundary extension type used by the IMSHIFT task.
  </dd>
  </dl>
  <dl id="l_constant">
  <dt><b>constant = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constant' Line='constant = 0.' -->
  <dd>The constant used by the IMSHIFT task if <i>boundary_type</i> is <span style="font-family: monospace;">"constant"</span>. 
  </dd>
  </dl>
  <dl id="l_trimimages">
  <dt><b>trimimages = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trimimages' Line='trimimages = yes' -->
  <dd>If trimimages is yes, the output images will be trimmed to
  include only the region over which they all overlap.  The
  trim section that is actually used may differ slightly from that
  reported by IMCENTROID, due to a correction applied to compensate for
  the boundary extension <span style="font-family: monospace;">"contamination"</span> near the edges of the images.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print the centers, shifts, and trim section?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IMALIGN measures the X and Y axis shifts between a list of input images
  <i>input</i> and a reference image <i>reference</i>, registers the
  input images to the reference image using the computed shifts,
  and trims the input images to a common overlap region.
  The task is meant to address the class of two dimensional image
  registration problems in which the images have the same pixel scale,
  are shifted relative to each other by simple x and y translations, and contain
  enough high signal / noise, pointlike sources in common to compute good
  average positions.  The basic operation of the task is to find centers
  for the list of registration objects or features in the coordinate
  frame of each image and then to subtract the corresponding centers
  found in the reference image.  The shifts of the registration objects
  are averaged for each image.
  </p>
  <p>
  IMALIGN is a simple script front end for IMCENTROID, which computes the
  shifts, IMSHIFT, which shifts the images, and
  IMCOPY, which performs the trimming.
  </p>
  <p>
  A list of the X and Y coordinates of the registration objects should be
  provided via the <i>coords</i> parameter.  The registration objects do not
  all have to be common to each frame; only that subset of the
  objects that is contained within the bounds of a given image will be
  centered.  Only the objects that are common to both the given image and
  the reference will be used to calculate the shifts.  The coordinates
  must be measured in the frame of the reference image.  If coarse
  centering is to be done, which is to say, if no <i>shifts</i> file is
  provided, then the first registration source should be separated from
  other sources by at least the maximum expected relative shift.
  </p>
  <p>
  An initial estimate of the shifts between each of the input images and
  the reference image is required for the centering algorithm (a marginal
  centroid) to work.  This estimate can be explicitly supplied in the file
  <i>shifts</i> (<i>Xshift=Xref-Xin</i> and <i>Yshift=Yref-Yin</i>) or can
  be generated from the images by measuring the relative shift of the
  first source listed in the coords file for each image.  This coarse
  centering pass requires that the first source be detached from other
  sources and from the border of each image, by a distance that is at
  least the maximum shift between the reference and input image.  This
  source should be pointlike and have a high signal to noise ratio.  The
  value of the <i>bigbox</i> parameter should be chosen to include the
  location of the source in each of the images to be aligned while
  excluding other sources.  Large values of <i>bigbox</i> should be held
  suspect until the final convergence of the centering algorithm is
  verified, although given a small value for the <i>tolerance</i>, the
  quality of the final centers is independent of the estimate for the
  initial shifts.  Better convergence may also be obtained by increasing
  the <i>niterate</i> parameter, although the default value of three
  should work for most cases.  <i>Niterate</i> should be kept small to
  avoid runaway.
  </p>
  <p>
  The <i>boxsize</i> parameter controls the size of the centering box for
  the fine centering passes and should be chosen so as to exclude sky
  background and other sources while including the wings of the point
  spread function.  The sense of the shifts that are calculated is
  consistent with the file supplied to the <i>shifts</i> parameter and
  with that used with the IMSHIFT task.
  </p>
  <p>
  If <i>shiftimages</i> is yes the images will actually be shifted using
  the IMSHIFT task.  Note that if <i>interp_type</i> is <span style="font-family: monospace;">"nearest"</span> the
  effect on the images is the same as if the shifts were rounded to
  integral values.  In this case, the pixels will be shifted without
  interpolation.  This can be used for data in which it is more important
  to preserve the pixel values than it is to achieve perfect
  registration.
  </p>
  <p>
  If <i>trimimages</i> is yes, the output images will be trimmed to
  include only the region over which they all overlap.  The trim section
  that is actually used may differ slightly from that reported by
  IMCENTROID.  A one or two pixel correction may be applied to each edge
  to compensate for the boundary extension <span style="font-family: monospace;">"contamination"</span> due to
  multi-pixel (e.g., <i>interp_type</i> = poly5) interpolation near the
  edges of the images.
  </p>
  <p>
  IMALIGN may be used with a set of <i>images</i> which vary in size.
  This can result in vignetting of the calculated overlap region because
  of the nature of the IMSHIFT task to preserve the size of an input
  image.  To visualize this, imagine a large reference image and a single
  small image to be aligned to it, both containing the same registration
  object which is at the center of each image.  IMALIGN will cause the
  small image to be shifted such that the object is positioned at the same
  pixel location as in the reference.  In performing the shift, a large
  fraction of the area of the small image may be shifted outside of its
  own borders, whereas the physical overlap of the large and small images
  includes ALL of the pixels of the small image.  In the case of such
  vignetting, IMALIGN will print a warning message and refuse to proceed
  with the trimming although the vignetting will occur whether or not the
  images are trimmed.  Note that the vignetting will not occur if the
  small image is used as the <i>reference</i>.
  </p>
  <p>
  The vignetting message may also be printed if the <i>images</i> are all
  the same size but the <i>reference</i> is not included in the list.
  This will occur if the sense of the measured shifts in a coordinate are
  all positive or all negative since in this case the border of the
  <i>reference</i> would have provided one of the limits to the trim
  section.  The reality of this vignetting depends on your point of view.
  </p>
  <p>
  Trimming will also not be performed if the entire overlap region vanishes.
  </p>
  <p>
  Note that many of these difficulties are due to the intrinsically fuzzy
  nature of the process of image registration.  This all leads to a few
  <span style="font-family: monospace;">"rules of thumb"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  o   Include the reference image in the input image list
  
  o   Use the smallest image as the reference image
  
  o   Choose the reference image such that the input images are
      scattered to either side in the shifts in each axis
  
  o   Align images that are the same size, OR
  
  o   Pad dissimilar sized images with blanks to
      the largest size and disable trimming
  </pre></div>
  </section>
  <section id="s_centering_algorithm">
  <h3>Centering algorithm</h3>
  <p>
  The algorithm is a <span style="font-family: monospace;">"marginal"</span> centroid in which the fit for each axis
  is performed separately upon a vector created by collapsing the
  centering box perpendicular to that axis.  The centroid is calculated
  with respect to the level specified by <i>background</i>.  If
  <i>background</i> is INDEF, the reference level for each source in each
  image is the local mean for those pixels that lie between the
  <i>lower</i> and <i>upper</i> thresholds.  The thresholds are set to the
  local data minimum or maximum if <i>lower</i> or <i>upper</i>,
  respectively, are INDEF.  If <i>negative</i> is yes, than the marginal
  vector will be inverted before being passed to the centroid algorithm.
  </p>
  <p>
  The maximum number of centering iterations and the tolerance for
  convergence are controlled by <i>niterate</i> and <i>tolerance</i>.  Note
  that the tolerance is an integer value that represents the maximum
  movement of the centering box between two successive iterations.  The
  default value of 0 requires that the centroid lie within the center
  pixel of the centering box which is <i>boxsize</i> in extent (note that
  <i>boxsize</i> must be an odd number).  This should normally be the case
  for bright, circularly symmetric point sources in images with a flat
  sky background.  If the registration sources are not circular symmetric
  try increasing the tolerance gingerly.  A sky level that varies across
  the image should be removed before processing.  The centering and
  calculation of the shifts may be performed with <i>shiftimages</i> = no
  (or directly with IMCENTROID) and the calculated shifts applied to the
  images directly with IMSHIFT.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Align three images to the first using the list of registration star
  coordinates in the file <span style="font-family: monospace;">"x1.coords"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imalign x1,x2,x3 x1 x1.coords x1.out,x2.out,x3.out
  </pre></div>
  <p>
  2. Align a list of images contained in the file <span style="font-family: monospace;">"imlist"</span>, overwriting the
  original images with the shifted and trimmed images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imalign @imlist x1 x1.coords @imlist
  </pre></div>
  <p>
  3. Align the images leaving the output images the same size as the input
  images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imalign @imlist x1 x1.coords @outlist trimimages-
  </pre></div>
  <p>
  4. Perform the centering but not the shifts:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imalign @imlist x1 x1.coords shiftimages-
  </pre></div>
  <p>
  5. Perform the centering, but don't calculate the shifts at all,
  and don't shift the image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pr&gt; imalign @imlist "" x1.coords shiftimages-
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The images being shifted must be in the current directory.
  </p>
  <p>
  The coarse centering portion of the algorithm can be fooled if the
  first source on the list is not well separated from other sources, or
  if the first source has a low signal to noise ratio, or if there is a
  complicated shape to the background.
  </p>
  <p>
  The task can produce output images that do not contain the entire
  overlap region.  This can only occur if the images are of varying sizes.
  This behavior is caused by the action of the IMSHIFT task to preserve the
  size of an input image, thus implicitly <span style="font-family: monospace;">"trimming"</span> the image.  A work
  around is to use IMCOPY to place the images into subsections of blank
  images that are the size (in each dimension) of the largest image(s)
  and use IMALIGN with <i>trimimages</i> set to no.  The borders of the output
  images can be trimmed manually.  This is discussed above in more detail.
  </p>
  <p>
  If <i>images</i> does not contain the <i>reference</i> and <i>trimimages</i>
  is set to yes then the set of shifted and trimmed images may no longer
  be aligned to the reference.  This occurs because any place holder
  pixels at the bottom and left edges of the images will be trimmed off.
  This is also discussed above.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcentroid, center, imshift, geomap, geotran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CENTERING ALGORITHM' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

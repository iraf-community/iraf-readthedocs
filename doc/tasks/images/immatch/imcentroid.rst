.. _imcentroid:

imcentroid: Compute and print relative shifts for a list of 2-D images
======================================================================

**Package: immatch**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imcentroid input reference coords
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of images within which sources are to be centered.  If a
  <i>reference</i> image is specified, imcentroid will calculate the mean
  X and Y shifts between the centered sources within each image and those
  same sources within the reference image.  The input image list
  should normally include the reference image so that its borders are
  used in the calculation of the  overlap region.
  </dd>
  </dl>
  <dl id="l_reference">
  <dt><b>reference = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reference' Line='reference = ""' -->
  <dd>The reference image to which the input images will be aligned.  If
  a reference image is specified the mean X and Y shifts between each of
  the input images and the reference image will be calculated, otherwise
  only the centers for the individual sources will be reported.
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords' -->
  <dd>A text file containing the coordinates of the registration objects to
  be centered in each image, one object per line with the x and y
  coordinates in columns one and two respectively.  These coordinates
  should be measured in the frame of the reference image.
  </dd>
  </dl>
  <dl id="l_shifts">
  <dt><b>shifts = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shifts' Line='shifts = ""' -->
  <dd>A text file containing the initial estimate for each image of the
  shift in each axis relative to the reference image.  These
  estimates are used to modify the coordinates of the registration
  objects prior to centering.  The format of the file is one image per
  line with the fractional x and y shifts in columns one and two
  respectively.  The sense of the shifts is such that:
  Xshift =Xref - Xin and shift= Yref - Yin. If shifts is undefined,
  a coarse centering pass will be made to attempt to determine
  the initial shifts.
  </dd>
  </dl>
  <dl id="l_boxsize">
  <dt><b>boxsize = 7</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boxsize' Line='boxsize = 7' -->
  <dd>The size in pixels of the box to use for the final centering, during
  which all the sources in the coords file are recentered in each image
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
  since it is highly data dependent.  Large value should be suspect until
  the final results are checked to see that the centering did not converge
  on the wrong coordinates, although the usual result for an inappropriate
  bigbox size is that the algorithm fails to converge and the task
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
  will halt when this limit is reached or when the desired tolerance
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
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print the centers for the individual objects ?  If verbose is no
  only the shifts relative to the reference coordinates will be reported.
  If no reference image is supplied, verbose is automatically set to yes.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IMCENTROID measures the X and Y coordinates of a list of sources in a
  list of images and finds the mean X and Y shifts between the input
  images <i>input</i> and a <i>reference</i> image, where the shifts are
  defined as the shifts that should be added to the input image coordinates to
  convert them into the reference coordinates.  The task is meant to
  address the class of two dimensional image registration problems in
  which the images have the same pixel scale, are shifted relative to
  each other by simple translations in each axis, and contain enough high
  signal-to-noise, pointlike sources in common to form good average
  positions.  The basic operation of the task is to find centers for the
  list of registration objects in the coordinate frame of each image and
  then to subtract the corresponding centers found in the reference
  image.  The shifts of the objects are averaged for each image.
  </p>
  <p>
  A list of the X and Y coordinates of the registration objects should be
  provided in the coordinates file <i>coords</i>.  The registration objects do not
  all have to be common to each frame, rather only that subset of the
  objects that is contained within the bounds of a given image will be
  centered.  Only the objects that are common to both the given image and
  the reference will be used to calculate the shifts.  The coordinates
  should be measured in the frame of the reference image<i>reference</i>.
  If coarse centering is to be done, which is to say, if no <i>shifts</i> file is
  provided, then the first registration source should be separated from
  other sources by at least the maximum expected relative shift.
  </p>
  <p>
  An initial estimate of the shifts between each of the input images
  <i>input</i> and the reference image <i>reference</i> is required for the
  centering algorithm (a marginal centroid) to work.  This estimate can be
  explicitly supplied in the text file <i>shifts</i> where Xshift = Xref -Xin
  and Yshift = Yref -Y in, or can be generated from the images by measuring
  the relative shift of the first source listed in the coordinates file
  <i>coords</i> for each input image.  This coarse
  centering pass requires that the first source be detached from other
  sources and from the border of each image by a distance that is at
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
  the fine centering pass and should be chosen so as to exclude sky
  background and other sources while including the wings of the point
  spread function.  The sense of the shifts that are calculated is
  consistent with the file supplied to the <i>shifts</i> parameter and
  with that used with the IMSHIFT task.
  </p>
  <p>
  IMCENTROID may be used with a set of input images which vary in size.
  This can result in vignetting of the calculated overlap region because
  of the nature of tasks such as IMSHIFT to preserve the size of an input
  image.  To visualize this, imagine a large reference image and a single
  small image to be aligned to it, both containing the same registration
  object which is at the center of each image.  IMCENTROID will cause the
  coordinate system of the small image to be shifted such that the object 
  will be positioned at the same pixel location as in the reference.  If
  the shift is performed, a large fraction of the area of the small image
  may be shifted outside of its own borders, whereas the physical overlap
  of the large and small images includes ALL of the pixels of the small
  image.  In the case of such vignetting, IMCENTROID will print a warning
  message and both the vignetted and unvignetted trim sections.  Note
  that the vignetting will not occur if the small image is used as the
  reference image.
  </p>
  <p>
  The vignetting message may also be printed if the input images are all
  the same size but the reference image is not included in the list.
  This will occur if the sense of the measured shifts in a coordinate are
  all positive or all negative since in this case the border of the
  reference image would have provided one of the limits to the trim
  section.  The reality of this vignetting depends on your point of view.
  </p>
  <p>
  Note that many of these difficulties are due to the intrinsically fuzzy
  nature of the process of image registration.  This all leads to a few
  guidelines:
  </p>
  <div class="highlight-default-notranslate"><pre>
  o   Include the reference image in the input image list
  
  o   Use the smallest image as the reference image
  
  o   Choose the reference image such that the input images
      are scattered to either side in the shifts in each axis
  
  o   Align images that are the same size, OR
  
  o   Pad dissimilar sized images with blanks to the largest size
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
  try increasing the tolerance gingerly.  If the sky background is not
  flat, but varies across the image, it can be removed before processing.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Calculate the shifts between three images using the first image
  as a reference image and the list of registration star coordinates in
  the file <span style="font-family: monospace;">"x1.coords"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imcentroid x1,x2,x3 x1 x1.coords
  </pre></div>
  <p>
  2. Calculate the shifts between a list of images contained in the file
  <span style="font-family: monospace;">"imlist"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  pr&gt; imcentroid @imlist x1 x1.coords
  </pre></div>
  <p>
  3. Perform the centering, but don't calculate the shifts, i.e., don't
  supply a reference image.  Note that the <i>input</i> list of shifts,
  or a coarse centering pass are still needed:
  </p>
  <div class="highlight-default-notranslate"><pre>
  pr&gt; imcentroid @imlist "" x1.coords
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The coarse centering portion of the algorithm can be fooled if the
  first source on the list is not well separated from other sources, or
  if the first source has a low signal to noise ratio, or if there is a
  complicated shape to the background.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imalign, imshift, xregister, geomap, geotran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CENTERING ALGORITHM' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

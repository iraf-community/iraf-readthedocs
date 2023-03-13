.. _pmmatch:

pmmatch: Pixel mask matching
============================

**Package: immatch**

.. raw:: html

  <section id="s_introduction">
  <h3>Introduction</h3>
  <p>
  Pixel masks are associated with images to identify bad pixels, sources, or
  regions of interest.  In the simplest case the pixel mask <span style="font-family: monospace;">"pixels"</span> (masks
  are generally stored in a compact encoded format but are logically an
  integer image raster) are associated with the image pixels by their raster
  coordinates, called <i>logical coordinates</i> in IRAF.  However, because
  images and pixel masks are stored and handled as independent entities,
  though possibly in the same multi-extension parent file, it is possible
  that one or the other may be transformed so a simple matching in logical
  coordinates is no longer valid.  This topic describes how pixel masks
  may still be associated with the images even after such transformations.
  </p>
  <p>
  There are many transformations which may be applied to images.  Some common
  ones are extracting subimages (often using the IRAF image section syntax),
  subsampling or decimating (again possibly with an image section),
  transposing, block averaging, block summing, and block replication.
  These are all simple linear physical transformations.  A slightly more
  complex linear transformation is image magnification where the axes are
  maintained but the pixel sizes may not have an integer relationship with
  the original image.  These types of linear transformations
  where the axes either the same or transposed are called
  <i>physical coordinate</i> transformations.
  </p>
  <p>
  At the other extreme are arbitrary transformations with coupled axes such
  as rotations, and distortion corrections, and resampling to match another
  image or standard sampling.  These transformations are typically mappings
  in one or more user coordinate systems, called <i>world coordinates</i>
  in IRAF, such as celestial coordinates or spectral coordinates.  The
  transformations are, therefore, called world coordinate transformations.
  </p>
  <p>
  Obviously, one way to deal the pixel masks is to transform both the image
  and mask in the same way.  Some applications provide both image and
  mask outputs for this reason.  In other cases the transformation
  application may be applied to both.
  </p>
  <p>
  This topic decribes another method where a pixel mask is matched to
  an image <span style="font-family: monospace;">"on-the-fly"</span>.  In the discussion the pixel mask to be matched
  is sometimes refered to as the reference pixel mask and the image being
  matched is refered to as the reference image.  The matching may be in one
  of the logical, physical, or world coordinate systems.  Initially only a
  few tasks provide this feature but others will be enhanced in the future.
  Be sure to check the help pages for a task for how pixel masks are
  associated with images.
  </p>
  <p>
  A key to this pixel mask matching method using the various coordinate
  systems is that tasks which transform the image or mask properly update
  the coordinate system information in the header.  This is the case for
  most IRAF tasks, particularly those which do common, simple physical
  transformations, as well as the general resampling or interpolation tasks
  such as <b>geotran</b> and the scripts that use them.  In addition, the
  IRAF system automatically updates the physical coordinate system when
  image sections are used.
  </p>
  </section>
  <section id="s_specifying_the_matching_with_the__span_style__font_family__monospace____pmmatch___span__variable">
  <h3>Specifying the matching with the <span style="font-family: monospace;">"pmmatch"</span> variable</h3>
  <p>
  The tasks providing pixel mask matching first set a default matching
  coordinate system.  Generally this is fixed internally though a task
  parameter may be provided in new tasks.  The usual default is logical
  as this is normally the prior behavior and does not depend on any header
  parameters or coordinate propagation.
  </p>
  <p>
  The user then overrides the default by setting the environment
  variable <i>pmmatch</i>.  This may be set in the environment before
  starting IRAF, in the IRAF login files, in scripts, or interactively.
  The values of this variable may be <span style="font-family: monospace;">"logical"</span>, <span style="font-family: monospace;">"physical"</span>, or <span style="font-family: monospace;">"world"</span>.
  An integer value may follow <span style="font-family: monospace;">"world"</span> as described later.
  A null string, <span style="font-family: monospace;">""</span>, may also be used to select the task default.
  </p>
  <p>
  Since this is an environment variable, it will apply to all tasks run with
  that environment.  So a caveat is that in some cases it may be important
  to realize the same matching will be used in different tasks and so one
  might need to change the value before the task.
  </p>
  </section>
  <section id="s_logical_coordinate_matching">
  <h3>Logical coordinate matching</h3>
  <p>
  The simplest coordinate system is logical.  This is where pixels are
  matched in raster order.  This does not depend on any keywords and is
  intuitive, which is why this is usual default.  One might think this is
  no matching at all, but there is something that happens in this case.
  </p>
  <p>
  The pixel mask may be larger or smaller than the image.  In the former
  the internal matching will trim the pixel mask to the size of the image.
  In the latter case the internal mask will be padded with zero.  In both
  cases the origin is the same and it is the largest columns and lines that
  are affect; that is, trimmed or padded on the left and top when thought
  of as an picture with origin at the lower left.
  </p>
  <p>
  The pixel mask values which overlap the image are left unchanged from
  the reference pixel mask.
  </p>
  </section>
  <section id="s_physical_coordinate_matching">
  <h3>Physical coordinate matching</h3>
  <p>
  The physical coordinates are a pixel or raster coordinate system which
  remains attached to an image or mask through operations of
  subsampling, decimating, blocking, replication, transpose, or magnification.
  Normally, an original image and mask will have a physical and logical
  coordinate system that is the same.  Then as they are transformed they
  differ such that pixel value features remain fixed relative to the
  physical coordinates.  The physical transformation is maintained in the
  header by the keywords LTVi and LTMi_j, where i and j are axis numbers.
  </p>
  <p>
  For example, a star in an image which had an original pixel coordinate
  of (123.4,567.8) will have this physical coordinate in a subraster
  containing it or when the image is magnified or reduced by scale
  changes.
  </p>
  <p>
  When a physical pixel mask matching is selected a reference mask is
  matched internally to the same physical pixels as the image.  For
  simple transformations, such as subrasters the result, is the obvious
  one; the mask pixel values remain associated with any features in the
  image.
  </p>
  <p>
  In the more complicated situation is when the scale is changed
  either by block averaging, decimating, or magnifying to arbitrary
  scales.  The mask pixel values are then the maximum in the reference
  pixel mask that overlaps any part of an image pixel.
  </p>
  </section>
  <section id="s_world_coordinate_matching">
  <h3>World coordinate matching</h3>
  <p>
  World coordinate matching is the most general.  It allows matching pixel
  masks to images which have been rotated or resampled beyond just changing
  the pixel scale.  Often the world coordinate system used with this option
  is celestial and the resampling is done to match another image, to remove
  distortions, or to transform to a standard celestial orientation and
  coordinate system.  However, any 2D world coordinate system is allowed.
  </p>
  <p>
  If a world coordinate system is not defined the physical coordinate
  system is used and, if that is missing, the logical coordinate system
  is used.  So using world coordinate matching covers all cases.
  </p>
  <p>
  In order to do the transformation an internal array of the size of the
  image being matched is allocated.  To minimize this memory usage the
  array packs the mask values into a small number of bits.  To advise the
  algorithm an integer defining the maximum output mask value may be specified
  after the word <span style="font-family: monospace;">"world"</span> in the pmmatch variable.  The value must be
  separated by whitespace.  Any input mask value greater than the maximum
  is mapped to the maximum value.  The default if no maximum is
  specified, pmmatch=<span style="font-family: monospace;">"world"</span>, is a boolean mask with values of 0 and 1.
  </p>
  <p>
  It is recommended that the maximum value be as small as possible consistent
  with the usage.  The relationship between the maximum and
  memory usage is the number of bits needed to represent the maximum value.
  Therefore, the maximum values 1, 3, 7, 15, use 1, 2, 3, 4 bits respectively.
  </p>
  <p>
  Note that while the <span style="font-family: monospace;">"world"</span> matching is the most general, if the
  transformation is only a physical one then use of physical coordinate
  matching avoids the requirement of an internal array and potential
  large memory usage for large images.
  </p>
  </section>
  <section id="s_checking_the_matching">
  <h3>Checking the matching</h3>
  <p>
  The pixel mask matching is performed <span style="font-family: monospace;">"on-the-fly"</span> when the reference pixel
  mask is opened by the application.  One of the benefits of this feature
  to avoid having to generate new copies of pixel masks after operations
  which transform the original image.
  </p>
  <p>
  However, because of the potential for confusion with whether the
  coordinate systems have been correctly defined or propagated, it may be
  useful to check the matching visually.  This can be done using the
  <b>display</b> task with the overlay feature.  This task supports the
  pixel mask matching feature so it is simply a matter of setting the
  <span style="font-family: monospace;">"pmmatch"</span> variable and specifying the input mask with the
  <i>overlay</i> parameter.
  </p>
  </section>
  <section id="s_creating_a_explict_matched_mask">
  <h3>Creating a explict matched mask</h3>
  <p>
  It may be desirable to actually create a pixel mask file which matches
  a reference image.  This may be for applications that don't support
  the internal mask matching feature, to export a mask with the image,
  for efficiency, or simply because you prefer to use mask files rather
  than the internal matching.
  </p>
  <p>
  Any task that implements the pixel matching and produces an output pixel
  mask may be used.  The recommend task is <b>mskexpr</b>.  This
  is a general task that creates output masks based on expressions.
  For creating a mask that matches an image, called the reference image
  in this task, from a mask matched to the image, called the reference
  mask in this application, the command is something like:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mskexpr m matchedmask myimage refmask=mask
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The examples illustrates the pixel mask matching with a simple image,
  the standard IRAF test image, which is
  transformed in various ways and the pixel matching is demonstrated by
  using the <b>display</b> task to overlay the mask.  The creation of an
  matching pixel mask file by <b>mskexpr</b> is also shown.
  </p>
  <p>
  We begin by creating a pixel mask from an image with a
  celestial coordinate system.  New images are generated by extracting a
  subraster, magnifying the image to a new pixel scale, and rotating the
  image by 45 degrees.  In each case the mask is shown as an overlay
  display.
  </p>
  <p>
  1. Create a mask for image wpix and display it as an overlay.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imcopy dev$wpix .
  cl&gt; imexpr "a &gt; 1000 ? 1 : 0" pm.pl wpix
  cl&gt; display wpix 1 overlay=pm
  </pre></div>
  <p>
  2. Overlay the mask with a simple subraster transformation.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set pmmatch = physical
  cl&gt; display wpix[301:428,101:228] 2 overlay=pm
  </pre></div>
  <p>
  3. Overlay the mask with a subraster and scale change physical transformation.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; magnify wpix[301:428,101:228] wpixmag 3 3
  
  wpixmag
    Magnify image wpix[301:428,101:228] to image wpixmag.
    Interpolation is linear.
    Boundary extension is nearest.
    Output coordinates in terms of input coordinates:
      x1 =         1., x2 =       128., dx =   0.333333
      y1 =         1., y2 =       128., dy =   0.333333
  cl&gt; set pmmatch = physical
  cl&gt; display wpixmag 2 overlay=pm
  </pre></div>
  <p>
  4. Overlay the mask after a 45 degree rotation.  Preserve the values 1, 2,
  and 3.
  </p>
  <div class="highlight-default-notranslate"><pre>
  proto&gt; rotate wpix wpix45 45 bound=const
  
  Transforming image wpix to image wpix45
      xshift: -106.25 yshift: 256.50 xmag: 1.00 ymag: 1.00 xrot:
      45.00 yrot: 45.00
  proto&gt; set pmmatch="world 3"
  proto&gt; display wpix45 2 over=pm
  z1=0. z2=456.0118
  </pre></div>
  </section>
  <section id="s_task_supporting_pixel_mask_matching">
  <h3>Task supporting pixel mask matching</h3>
  <p>
  display, imcombine, runmed, fixpix, transform, lscombine, mimstat, mskexpr
  </p>
  
  </section>
  
  <!-- Contents: 'Introduction' 'Specifying the matching with the <span style="font-family: monospace;">"pmmatch"</span> variable' 'Logical Coordinate Matching' 'Physical Coordinate Matching' 'World Coordinate Matching' 'Checking the Matching' 'Creating a Explict Matched Mask' 'Examples' 'TASK SUPPORTING PIXEL MASK MATCHING'  -->
  

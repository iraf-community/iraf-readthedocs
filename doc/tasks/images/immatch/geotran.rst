.. _geotran:

geotran: Transform 1-D or 2-D images using various mapping transforms
=====================================================================

**Package: immatch**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  geotran input output database transforms
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of images to be transformed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output images. If the output image name is the same as the input
  image name the input image is overwritten. The output image may be a section
  of an existing image. The number of output images must equal the number
  of input images.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>The name of the text file containing the coordinate transformation (generally
  the database file produced by GEOMAP).
  If database is the null string then GEOTRAN will perform a linear
  transformation based the values of xin, yin, xout, yout, xshift, yshift,
  xmag, ymag, xrotation and yrotation. If all these parameters have their
  defaults values the transformation is a null transformation. If the geometric
  transformation is linear xin, yin, xout, yout, xshift, yshift, xmag, ymag,
  xrotation and yrotation can be used to override the values in the database
  file.
  </dd>
  </dl>
  <dl id="l_transforms">
  <dt><b>transforms</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='transforms' Line='transforms' -->
  <dd>The list of record name(s) in the file <i>database</i> containing the
  desired transformations.
  This record name is usually the name of the text file input to geomap
  listing the reference and input coordinates of the control points.
  The number of records must be 1 or equal to the number of input images.
  The record names may be listed in a text file 1 record per line.
  The transforms parameter is only
  requested if database is not equal to the null string.
  </dd>
  </dl>
  <dl id="l_geometry">
  <dt><b>geometry = <span style="font-family: monospace;">"geometric"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='geometry' Line='geometry = "geometric"' -->
  <dd>The type of geometric transformation. The geometry parameter is
  only requested if database is not equal to the null string. The options are:
  <dl>
  <dt><b>linear</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='linear' Line='linear' -->
  <dd>Perform only the linear part of the geometric transformation.
  </dd>
  </dl>
  <dl>
  <dt><b>geometric</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='geometric' Line='geometric' -->
  <dd>Compute both the linear and distortion portions of the geometric correction.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_xmin">
  <dt><b>xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmin' Line='xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF' -->
  <dd>The minimum and maximum x and y reference values of the output image.
  If a database file has been defined xmin, xmax, ymin and ymax
  efault to the minimum and maximum values set by
  GEOMAP and may be less than but may not exceed those values.
  </dd>
  </dl>
  <dl id="l_xscale">
  <dt><b>xscale = 1.0, yscale = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xscale' Line='xscale = 1.0, yscale = 1.0' -->
  <dd>The output picture x and y scales in units of
  x and y reference units per output pixel,
  e.g  arcsec / pixel or Angstroms / pixel if the reference coordinates
  are arcsec or Angstroms. If the reference coordinates are in pixels
  then xscale and yscale should be 1.0 to preserve the scale of the reference
  image.
  If xscale and yscale are undefined (INDEF), xscale and yscale default to the
  range of the reference coordinates over the range in pixels.
  Xscale and yscale override the values of ncols and nlines.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = INDEF, nlines = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = INDEF, nlines = INDEF' -->
  <dd>The number of columns and lines in the output image. Ncols and nlines default
  to the size of the input image. If xscale or yscale are defined ncols or nlines
  are overridden.
  </dd>
  </dl>
  <dl id="l_xsample">
  <dt><b>xsample = 1.0, ysample = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xsample' Line='xsample = 1.0, ysample = 1.0' -->
  <dd>The coordinate surface subsampling factor. The coordinate surfaces are
  evaluated at every xsample-th pixel in x and every ysample-th pixel in y.
  Transformed coordinates  at intermediate pixel values are determined by
  bilinear interpolation in the coordinate surfaces. If the coordinate
  surface is of high order setting these numbers to some reasonably high
  value is strongly recommended.
  </dd>
  </dl>
  <dl id="l_interpolant">
  <dt><b>interpolant = <span style="font-family: monospace;">"linear"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interpolant' Line='interpolant = "linear"' -->
  <dd>The interpolant used for rebinning the image.
  The choices are the following.
  <dl>
  <dt><b>nearest</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nearest' Line='nearest' -->
  <dd>Nearest neighbor.
  </dd>
  </dl>
  <dl>
  <dt><b>linear</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='linear' Line='linear' -->
  <dd>Bilinear interpolation in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>poly3</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='poly3' Line='poly3' -->
  <dd>Third order polynomial in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>poly5</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='poly5' Line='poly5' -->
  <dd>Fifth order polynomial in x and y.
  </dd>
  </dl>
  <dl>
  <dt><b>spline3</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='spline3' Line='spline3' -->
  <dd>Bicubic spline.
  </dd>
  </dl>
  <dl>
  <dt><b>sinc</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='sinc' Line='sinc' -->
  <dd>2D sinc interpolation. Users can specify the sinc interpolant width by
  appending a width value to the interpolant string, e.g. sinc51 specifies
  a 51 by 51 pixel wide sinc interpolant. The sinc width will be rounded up to
  the nearest odd number.  The default sinc width is 31 by 31.
  </dd>
  </dl>
  <dl>
  <dt><b>lsinc</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='lsinc' Line='lsinc' -->
  <dd>Look-up table sinc interpolation. Users can specify the look-up table sinc
  interpolant width by appending a width value to the interpolant string, e.g.
  lsinc51 specifies a 51 by 51 pixel wide look-up table sinc interpolant. The user
  supplied sinc width will be rounded up to the nearest odd number. The default
  sinc width is 31 by 31 pixels. Users can specify the resolution of the lookup
  table sinc by appending the look-up table size in square brackets to the
  interpolant string, e.g. lsinc51[20] specifies a 20 by 20 element sinc
  look-up table interpolant with a pixel resolution of 0.05 pixels in x and y.
  The default look-up table size and resolution are 20 by 20 and 0.05 pixels
  in x and y respectively.
  </dd>
  </dl>
  <dl>
  <dt><b>drizzle</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='drizzle' Line='drizzle' -->
  <dd>2D drizzle resampling. Users can specify the drizzle pixel fraction in x and y
  by appending a value between 0.0 and 1.0 in square brackets to the
  interpolant string, e.g. drizzle[0.5]. The default value is 1.0.
  The value 0.0 is increased internally to 0.001. Drizzle resampling
  with a pixel fraction of 1.0 in x and y is equivalent to fractional pixel
  rotated block summing (fluxconserve = yes) or averaging (flux_conserve = no)  if
  xmag and ymag are &gt; 1.0.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_boundary">
  <dt><b>boundary = <span style="font-family: monospace;">"nearest"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boundary' Line='boundary = "nearest"' -->
  <dd>The choices are:
  <dl>
  <dt><b>nearest</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nearest' Line='nearest' -->
  <dd>Use the value of the nearest boundary pixel.
  </dd>
  </dl>
  <dl>
  <dt><b>constant</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='constant' Line='constant' -->
  <dd>Use a user supplied constant value.
  </dd>
  </dl>
  <dl>
  <dt><b>reflect</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='reflect' Line='reflect' -->
  <dd>Generate a value by reflecting about the boundary of the image.
  </dd>
  </dl>
  <dl>
  <dt><b>wrap</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='wrap' Line='wrap' -->
  <dd>Generate a value by wrapping around to the opposite side of the image.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_constant">
  <dt><b>constant = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constant' Line='constant = 0.0' -->
  <dd>The value of the constant for boundary extension.
  </dd>
  </dl>
  <dl id="l_fluxconserve">
  <dt><b>fluxconserve = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fluxconserve' Line='fluxconserve = yes' -->
  <dd>Preserve the total image flux. The output pixel values are multiplied by
  the Jacobian of the coordinate transformation.
  </dd>
  </dl>
  <dl id="l_xin">
  <dt><b>xin = INDEF, yin = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xin' Line='xin = INDEF, yin = INDEF' -->
  <dd>The x and y coordinates in pixel units in the input image which will map to
  xout, yout in the output image. If the database file is undefined these
  numbers default to the center of the input image. 
  </dd>
  </dl>
  <dl id="l_xout">
  <dt><b>xout = INDEF, yout = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xout' Line='xout = INDEF, yout = INDEF' -->
  <dd>The x and y reference coordinates in the output image which correspond
  to xin, yin in the input image. If the database file is undefined, xout and
  yout default to the center of the output image reference coordinates.
  </dd>
  </dl>
  <dl id="l_xshift">
  <dt><b>xshift = INDEF, yshift = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xshift' Line='xshift = INDEF, yshift = INDEF' -->
  <dd>The shift of the input origin in pixels. If the database file is undefined
  then xshift and yshift determine the shift of xin, yin.
  </dd>
  </dl>
  <dl id="l_xmag">
  <dt><b>xmag = INDEF, ymag = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmag' Line='xmag = INDEF, ymag = INDEF' -->
  <dd>The scale factors of the coordinate transformation in units of input pixels
  per reference coordinate unit. If database is undefined xmag and ymag
  default to 1.0; otherwise xmag and ymag default to the values found
  by GEOMAP. If the database file is not null then xmag and ymag override
  the values found by GEOMAP.
  </dd>
  </dl>
  <dl id="l_xrotation">
  <dt><b>xrotation = INDEF, yrotation = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xrotation' Line='xrotation = INDEF, yrotation = INDEF' -->
  <dd>The rotation angles in degrees of the coordinate transformation.
  Positive angles are measured counter-clockwise with respect to the x axis.
  If database
  is undefined then xrotation and yrotation default to 0.0; otherwise
  xrotation and yrotation default to the values found by GEOMAP.
  If database is not NULL then xrotation and yrotation override the values
  found by GEOMAP.
  </dd>
  </dl>
  <dl id="l_nxblock">
  <dt><b>nxblock = 512, nyblock = 512</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxblock' Line='nxblock = 512, nyblock = 512' -->
  <dd>If the size of the output image is less than nxblock by nyblock then
  the entire image is transformed at once. Otherwise the output image
  is computed in blocks of nxblock by nxblock pixels.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about the progress of the task ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  GEOTRAN corrects an image for geometric distortion using the coordinate
  transformation determined by GEOMAP. The transformation is stored as the
  coefficients of a polynomial surface in record <i>transforms</i>,
  in the text file <i>database</i>.
  The coordinate surface is sampled at every <i>xsample</i> and <i>ysample</i>
  pixel in x and y.
  The transformed coordinates at intermediate pixel values are
  determined by bilinear interpolation in the coordinate surface. If
  <i>xsample</i> and <i>ysample</i> = 1, the coordinate
  surface is evaluated at every pixel. Use of <i>xsample</i> and <i>ysample</i>
  are strongly recommended for large images and high order coordinate
  surfaces in order to reduce the execution time.
  </p>
  <p>
  <i>Xmin</i>, <i>xmax</i>, <i>ymin</i> and <i>ymax</i> define the range of
  reference coordinates represented in the output picture. These numbers
  default to the minimum and maximum x and y reference values used by GEOMAP,
  and may not exceed those values.
  The scale and size of the output picture is determined as follows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ncols = ncols (inimage)
  if (xscale == INDEF)
      xscale = (xmax - xmin ) / (ncols - 1)
  else
      ncols = (xmax - xmin) / xscale + 1
  
  nlines = nlines (inimage)
  if (yscale == INDEF)
      yscale = (ymax - ymin ) / (nlines - 1)
  else
      nlines = (ymax - ymin) / yscale + 1
  </pre></div>
  <p>
  The output image gray levels are determined by interpolating in the input
  image at the positions of the transformed output pixels. If the
  <i>fluxconserve</i> switch is set the output pixel values are multiplied by
  the Jacobian of the transformation.
  GEOTRAN uses the routines in the 2-D interpolation package.
  </p>
  <p>
  The linear portion of the transformation may be altered after the fact
  by setting some or all of the parameters <i>xin</i>, <i>yin</i>, <i>xout</i>,
  <i>yout</i>, <i>xshift</i>, <i>yshift</i>, <i>xmag</i>, <i>ymag</i>, <i>xrotation</i>,
  <i>yrotation</i>.
  Xin, yin, xshift, yshift, xout and yout can be used to redefine the shift.
  Xmag, and ymag can be used to reset the x and y scale of the transformation.
  Xrotation and yrotation can be used to reset the orientation of the
  transformation.
  </p>
  <p>
  The output image is computed in <i>nxblock</i> by <i>nyblock</i> pixel sections.
  If possible users should set these numbers to values larger than the dimensions
  of the output image to minimize the number of disk reads and writes required
  to compute the output image.  If this is not feasible and the image rotation is
  small, users should set nxblock to be greater than the number of columns in
  the output image, and nyblock to be as large as machine memory will permit.
  </p>
  <p>
  If the CL environment variable <i>nomwcs</i> is <span style="font-family: monospace;">"no"</span> then the world
  coordinate system of the input image will be modified in the output image
  to reflect the effects of the <i>linear</i> portion of the geometric
  transformation operation.
  Support does not yet exist in the IRAF world coordinate system interface
  for the higher order distortion corrections that GEOTRAN is capable of
  performing.
  </p>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  <p>
  It requires approximately 70 and 290 cpu seconds to correct a 512 by 512
  square image for geometric distortion using a low order coordinate surface
  and bilinear and biquintic interpolation respectively (Vax 11/750 fpa).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Register two images by transforming the coordinate system of the input
  image to the coordinate system of the reference image. The size of the
  reference image is 512 by 512.  The output image scale will be 1.0 and
  its size will be determined by the xmin, xmax, ymin, ymax parameters set
  in the task GEOMAP. The file <span style="font-family: monospace;">"database"</span> containing the record <span style="font-family: monospace;">"m51.coo"</span>
  was produced by GEOMAP.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geomap m51.coo database 1.0 512.0 1.0 512.0
  cl&gt; geotran m51 m51.tran database m51.coo
  </pre></div>
  <p>
  2. Repeat the above command but set the output image scale to 2.0 reference
  images pixels per output image pixel.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geomap m51.coo database 1.0 512.0 1.0 512.0
  cl&gt; geotran m51 m51.tran database m51.coo xscale=2.0 yscale=2.0
  </pre></div>
  <p>
  3. Repeat the previous command using an output scale of
  2 reference units per pixel and bicubic spline interpolation with no
  flux correction. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geomap m51.coo database 1.0 512.0 1.0 512.0
  cl&gt; geotran m51 m51.tran database m51.coo xscale=2. yscale=2. \
  &gt;&gt;&gt; inter=spline3 flux-
  </pre></div>
  <p>
  4. Register a list of 512 by 512 pixel square images using the set of
  transforms computed by GEOMAP. The input images, output images, and coordinate
  lists / transforms are listed in the files inlist, outlist and reclist
  respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geomap @reclist database 1. 512. 1. 512.
  cl&gt; geotran @inlist @outlist database @reclist
  </pre></div>
  <p>
  5. Mosaic 3 512 square images into a larger 512 by 1536 square images after
  applying a shift to each input image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; geotran image1 outimage[1:512,1:512] "" ncols=512 nlines=1536 \
      xshift=5.0 yshift=5.0
  cl&gt; geotran image2 outimage[1:512,513:1024] "" xshift=10.0 yshift=10.0
  cl&gt; geotran image3 outimage[1:512,1025:1536] "" xshift=15.0 yshift=15.0
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Support does not yet exist in the IRAF world coordinate system interface
  for the higher order distortion corrections that GEOTRAN is capable of
  performing.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imshift, magnify, rotate, imlintran, geomap, geoxytran, gregister
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'TIMINGS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

.. _i2sun:

i2sun: Convert IRAF images to Sun rasterfiles
=============================================

**Package: vol**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  i2sun input output z1 z2
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input image template, @file, n-dimensional image, or combination.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Root template for output images, e.g. <span style="font-family: monospace;">"home$ras/frame.%d"</span>.
  </dd>
  </dl>
  <dl id="l_clutfile">
  <dt><b>clutfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clutfile' Line='clutfile' -->
  <dd>Previously saved Sun rasterfile (e.g. output from IMTOOL), containing the
  color/greyscale lookup table information to be passed along to each output
  frame.  Standard ones can be saved and used with any number of images (e.g.
  <span style="font-family: monospace;">"pseudo.ras"</span>).
  </dd>
  </dl>
  <dl id="l_z1">
  <dt><b>z1 = INDEF, z2 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='z1' Line='z1 = INDEF, z2 = INDEF' -->
  <dd>Minimum and maximum pixel/voxel intensities to scale to full output
  color/greyscale range.  Both are required parameters, and will apply to all
  images in the sequence.
  </dd>
  </dl>
  <dl id="l_ztrans">
  <dt><b>ztrans = <span style="font-family: monospace;">"linear"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ztrans' Line='ztrans = "linear"' -->
  <dd>Intensity transformation on input data (linear|log|none|user).
  If <span style="font-family: monospace;">"user"</span>, you must also specify <i>ulutfile</i>.
  </dd>
  </dl>
  <dl id="l_ulutfile">
  <dt><b>ulutfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ulutfile' Line='ulutfile' -->
  <dd>Name of text file containing the look up table when <i>ztrans</i> = user.
  The table should contain two columns per line; column 1 contains the
  intensity, column 2 the desired greyscale output.
  </dd>
  </dl>
  <dl id="l_xsize">
  <dt><b>xsize = INDEF, ysize = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xsize' Line='xsize = INDEF, ysize = INDEF' -->
  <dd>If specified, these will be the dimensions of all output Sun rasterfiles
  in pixels.  The default will be the same size as the input images (which
  could vary, though this would create a jittery movie).
  </dd>
  </dl>
  <dl id="l_xmag">
  <dt><b>xmag = 1.0, ymag = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmag' Line='xmag = 1.0, ymag = 1.0' -->
  <dd>Another way to specify output rasterfile dimensions.  These are the 
  magnification factors to apply to the input image dimensions.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 1' -->
  <dd>Order of the interpolator to be used for spatially interpolating the image.
  The current choices are 0 for pixel replication, and 1 for bilinear
  interpolation.
  </dd>
  </dl>
  <dl id="l_sliceaxis">
  <dt><b>sliceaxis = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sliceaxis' Line='sliceaxis = 3' -->
  <dd>Image axis from which to cut multiple slices when input image dimension is
  greater than 2.  Only x-y sections are allowed, so <i>sliceaxis</i> must
  be 3 or greater.
  </dd>
  </dl>
  <dl id="l_swap">
  <dt><b>swap = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='swap' Line='swap = no' -->
  <dd>Swap rasterfile bytes on output?  Used when rasterfiles are being written
  to a computer with opposite byte-swapping from that of the home computer
  (e.g. between VAX and Sun).
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Given a series of IRAF images, an intensity transformation, and a file
  containing color/greyscale lookup table information, produces one 2d image
  in Sun rasterfile format for each 2D IRAF image.  This is a temporary task
  usually used as a step in creating filmloops for playback by a Sun Movie
  program.
  </p>
  <p>
  The input images may be specified as an image template (<span style="font-family: monospace;">"zoom*.imh"</span>),
  an <span style="font-family: monospace;">"@"</span> file (<span style="font-family: monospace;">"@movie.list"</span>), or as an n-dimensional image from which to
  create multiple 2d rasterfiles.  If any images in a list are nD images,
  all 2d sections from the specified <i>sliceaxis</i> will be written out
  (default = band or z axis).  At present, only x-y sections may be made,
  i.e. the slice axis must be axis 3 or higher.
  </p>
  <p>
  The minimum and maximum pixel/voxel intensities, z1 and z2, must be specified
  as it would be not only inefficient to calculate the full zrange of
  each image in a sequence, but would also make very jumpy movies.
  Between input intensities z1 and z2, the pixel intensities may be transformed
  according to the <i>ztrans</i> parameter: <span style="font-family: monospace;">"linear"</span>, <span style="font-family: monospace;">"log10"</span>, <span style="font-family: monospace;">"none"</span>,
  or <span style="font-family: monospace;">"user"</span>.
  </p>
  <p>
  When <i>ztrans</i> = <span style="font-family: monospace;">"user"</span>, a look up table of intensity values and their
  corresponding greyscale levels is read from the file specified by the
  <i>ulutfile</i> parameter.  From this information, a piecewise linear
  look up table containing 4096 discrete values is composed.  The text
  format table contains two columns per line; column 1 contains the
  intensity, column 2 the desired greyscale output.  The greyscale values
  specified by the user must match those available on the output device.
  Task <i>showcap</i> can be used to determine the range of acceptable
  greyscale levels.  
  </p>
  <p>
  A color table file (<i>clutfile</i>) may be produced on a Sun workstation from
  IMTOOL (see IMTOOL manual page, R_RASTERFILE parameter and Imcopy function).
  This file may be specified to I2SUN as the <i>clutfile</i> parameter.
  Likewise, any rasterfiles previously created with
  I2SUN may be used as input clutfiles.
  </p>
  <p>
  The output rasterfile dimensions may be larger or smaller than the input 
  images (see parameters <i>xsize</i> and <i>ysize</i>, or <i>xmag</i> and
  <i>ymag</i>).  The parameter <i>order</i> controls the mode of interpolation;
  0=pixel replication, 1=bilinear.
  </p>
  <p>
  If the output rasterfiles are being sent to a computer with opposite
  byte-swapping characteristics, set <i>swap</i> = yes (e.g., when running
  I2SUN on a VAX, with output to a Sun).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  1.  Produce a series of Sun rasterfiles in tmp$mydir/movie/,
      using a pseudocolor color table file saved earlier, with
      input greylevels scaled between 10 and 100.
  
      cl&gt; i2sun nzoom*.imh tmp$mydir/movie/frame.%d \
          home$colors/pseudo.ras 10 100
  
  2.  Make a movie through the z, or band, axis of a datacube.
  
      cl&gt; i2sun cube tmp$cubemovie/frame.%d 1 256
  
  3.  Make a movie through the 4th, or hyper-axis of a datacube,
      holding image band 10 constant.
  
      cl&gt; i2sun hypercube[*,*,10,*] tmp$movie/frame.%d 1 256 \
          sliceaxis=4
  
  4.  Run I2SUN on a VAX, with output to a Sun.
  
      cl&gt; i2sun @imlist sunnode!home$ras/frame.%d 1 256 swap+
  </pre></div>
  </section>
  <section id="s_timings">
  <h3>Timings</h3>
  <p>
  49 seconds (1 sec/frame) to produce 50 100*100 rasterfiles from a
  100*100*50 datacube with no magnification, on a diskless Sun-3/110
  using NFS to Eagle disks on a lightly loaded Sun-3/160 fileserver
  (load factor &lt; 1.5).  
  5 minutes for the same with a magnification factor of 2 in both x and y,
  bilinear interpolation.
  20 minutes for the same with a magnification factor of 5 in both x and y.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  display, imtool, volumes.pvol
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIMINGS' 'BUGS' 'SEE ALSO'  -->
  

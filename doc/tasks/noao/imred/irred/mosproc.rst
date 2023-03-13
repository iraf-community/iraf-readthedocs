.. _mosproc:

mosproc: Prepare images for quick look mosaicing
================================================

**Package: irred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mosproc input output nxsub nysub
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input images to be mosaiced. The images are assumed
  to be ordered either by row, column, or in a raster pattern. If
  the image list is not in order then the iraf <b>files</b> task plus
  the <b>editor</b> must be used to construct an image list. The images
  in the input list are assumed to all be the same size.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The name of the output mosaiced image.
  </dd>
  </dl>
  <dl id="l_nxsub">
  <dt><b>nxsub</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxsub' Line='nxsub' -->
  <dd>The number of subrasters along a row of the output image.
  </dd>
  </dl>
  <dl id="l_nysub">
  <dt><b>nysub</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nysub' Line='nysub' -->
  <dd>The number of subrasters along a column of the output image.
  </dd>
  </dl>
  <dl id="l_skysubtract">
  <dt><b>skysubtract = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skysubtract' Line='skysubtract = yes' -->
  <dd>Subtract a sky image from all the input images. The sky image
  to be subtracted is either <i>sky</i> or a sky image computed
  by median filtering selected input images after weighting the images
  by the exposure time..
  </dd>
  </dl>
  <dl id="l_sky">
  <dt><b>sky = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sky' Line='sky = ""' -->
  <dd>The name of the sky image.
  </dd>
  </dl>
  <dl id="l_exclude">
  <dt><b>exclude = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exclude' Line='exclude = ""' -->
  <dd>The input images to be excluded from the computation of the sky image.
  For example if <i>exclude</i>=<span style="font-family: monospace;">"1,3-5"</span> then input images 1, 3, 4, 5 are
  not used for computing the sky frame.
  </dd>
  </dl>
  <dl id="l_expname">
  <dt><b>expname = <span style="font-family: monospace;">"exptime"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expname' Line='expname = "exptime"' -->
  <dd>The image header exposure time keyword. If the sky frame is computed
  internally by median filtering the input images, the individual images
  are weighted by the exposure time defined by the exposure time
  keyword <i>expname</i>. Weights of 1 are assigned when no exposure time
  is given.
  </dd>
  </dl>
  <dl id="l_flatten">
  <dt><b>flatten = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flatten' Line='flatten = yes' -->
  <dd>Divide all the images by a flat field image. Flat fielding is done
  after sky subtraction. If the name of a flat field image <i>flat</i>
  is supplied that image is divided directly into all the input images.
  Otherwise the skyframe computed above is normalized by the mode of the
  pixels and divided into all the input images.
  </dd>
  </dl>
  <dl id="l_flat">
  <dt><b>flat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flat' Line='flat = ""' -->
  <dd>The name of the flat field image.
  </dd>
  </dl>
  <dl id="l_transpose">
  <dt><b>transpose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='transpose' Line='transpose = no' -->
  <dd>Transpose the input images before inserting them into the mosaic.
  </dd>
  </dl>
  <dl id="l_trim_section">
  <dt><b>trim_section = <span style="font-family: monospace;">"[*,*]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trim_section' Line='trim_section = "[*,*]"' -->
  <dd>The section of the input images to be mosaiced into the output
  image. Section can be used to flip and/or trim the individual
  subrasters before adding them to the mosaic. For example if we
  want to flip each subraster around the y axis before adding it
  to the mosaic, then <i>trim_section</i> = <span style="font-family: monospace;">"[*,-*]"</span>.
  </dd>
  </dl>
  <dl id="l_corner">
  <dt><b>corner = <span style="font-family: monospace;">"lr"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='corner' Line='corner = "lr"' -->
  <dd>The starting position in the output image. The four options are <span style="font-family: monospace;">"ll"</span> for
  lower left corner, <span style="font-family: monospace;">"lr"</span> for lower right corner, <span style="font-family: monospace;">"ul"</span> for upper left
  corner and <span style="font-family: monospace;">"ur"</span> for upper right corner.
  </dd>
  </dl>
  <dl id="l_direction">
  <dt><b>direction = <span style="font-family: monospace;">"row"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='direction' Line='direction = "row"' -->
  <dd>Add input images to the output image in row or column order. The options
  are <span style="font-family: monospace;">"row"</span> for row order and <span style="font-family: monospace;">"column"</span> for column order. The direction
  specified must agree with the order of the input list.
  </dd>
  </dl>
  <dl id="l_raster">
  <dt><b>raster = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='raster' Line='raster = no' -->
  <dd>Add the columns or rows to the output image in a raster pattern or return
  to the start of a column or a row.
  </dd>
  </dl>
  <dl id="l_median_section">
  <dt><b>median_section = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='median_section' Line='median_section = ""' -->
  <dd>Compute the median of each input image inserted into the mosaic using the
  specified section.
  </dd>
  </dl>
  <dl id="l_subtract">
  <dt><b>subtract = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subtract' Line='subtract = no' -->
  <dd>Subtract the computed median from each input image before inserting it
  into the mosaic.
  </dd>
  </dl>
  <dl id="l_oval">
  <dt><b>oval = -1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='oval' Line='oval = -1.0' -->
  <dd>The value of border pixels.
  </dd>
  </dl>
  <dl id="l_delete">
  <dt><b>delete = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='delete' Line='delete = yes' -->
  <dd>Delete sky subtracted, flat fielded and transposed images upon exit from
  the script.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = STDOUT</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = STDOUT' -->
  <dd>The name of the log file.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MOSPROC takes the list of input images <i>input</i> of identical dimensions and
  inserts them into a single output image <i>output</i>. Before mosaicing the user
  can optionally sky subtract, flat field or transpose the input images.
  If <i>skysubtract</i> = yes, a single sky
  image is subtracted from all the input images. The sky image
  may be the externally derived image <i>sky</i> or calculated internally 
  by computing the exposure time weighted median of the input images, minus
  those input images specifically excluded by the <i>exclude</i> parameter.
  If <i>flatten</i> = yes, the input images are flat fielded using either
  the externally defined flat field image <i>flat</i> or the internally
  derived sky image normalized by its mode.
  If <i>transpose</i> is enabled all the input images are optionally transposed
  before mosaicing.
  </p>
  <p>
  MOSPROC takes the list of processed images and inserts them into the 
  output image in positions determined by their order in the input list,
  <i>nxsub</i>, <i>nysub</i> and the parameters  <i>corner</i>, <i>direction</i>
  and <i>raster</i>. 
  The orientation and size of each individual subraster in the output image
  may be altered by setting the parameter <i>trim_section</i>. The size
  of the output image is determined by nxsub and nysub and the size of
  the individual input images. A one column wide border is drawn between
  each of the output image subrasters with a pixel value of <i>oval</i>.
  The user may optionally  compute and subtract the median from each input
  image before inserting it into the mosaic.
  </p>
  <p>
  MOSPROC produces an output mosaiced image <i>output</i> and an accompanying
  database file <i>dboutput</i>. These two files plus an interactively
  generated coordinate list comprise the necessary input for the IRALIGN,
  IRMATCH1D and IRMATCH2D tasks.
  The temporary images generated (sky substracted, flat fielded, and
  transposed)
  can be deleted automatically if <b>delete=yes</b>, before the task completes.
  Otherwise they will be left in the same directory of the input images.
  The temporary sky and flat field images if created are not deleted.
  </p>
  <p>
  The computation of the sky frame is done with IMAGES.IMCOMBINE and the
  subsequent sky subraction with IMAGES.IMARITH. The computation of
  the flat field is done with PROTO.BSCALE and the flat field division
  with FLATTEN. The task IMAGES.TRANSPOSE transpose the input.
  The mosaicing itself is done with PROTO.IRMOSAIC.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Mosaic a list of 64 infrared images onto an 8 by 8 grid after sky 
     subtraction and flat fielding. Use an externally derived sky and
     flat field image
  </p>
  <div class="highlight-default-notranslate"><pre>
  ir&gt; mosproc @imlist mosaic 8 8 skysub+ sky=skyimage flatten+ \
  &gt;&gt;&gt;  flat=flatfield
  </pre></div>
  <p>
  2. Mosaic a list of 64 infrared images onto an 8 by 8 grid after sky 
     subtraction and flat fielding. Derive the sky and flat field frames
     from the data excluding image number 5
  </p>
  <div class="highlight-default-notranslate"><pre>
  ir&gt; mosproc @imlist mosaic 8 8 skysub+ exclude="5" flatten+
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
  images.imcombine, images.imarith, proto.bscale, images.imtrans, proto.irmosaic
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

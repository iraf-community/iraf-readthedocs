.. _imtile:

imtile: Tile same sized 2D images into a 2D mosaic
==================================================

**Package: imutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  imtile input output nctile nltile
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input image tiles to be mosaiced. The image tile list is assumed
  to be ordered by row, column, or in a raster pattern. If the image tile list
  is not in order then the files or sections tasks plus the editor must be used
  to construct an ordered image tile list. The images in the input list must
  all be the same size.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The name of the output image.
  </dd>
  </dl>
  <dl id="l_nctile">
  <dt><b>nctile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nctile' Line='nctile' -->
  <dd>The number of image tiles to be placed along a row of the output image.
  </dd>
  </dl>
  <dl id="l_nltile">
  <dt><b>nltile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nltile' Line='nltile' -->
  <dd>The number of image tiles to be placed along a column of the output image.
  </dd>
  </dl>
  <dl id="l_trim_section">
  <dt><b>trim_section = <span style="font-family: monospace;">"[*,*]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trim_section' Line='trim_section = "[*,*]"' -->
  <dd>The section of the input image tiles to be inserted into the output image.
  Trim_section can be used to flip and / or trim the individual image tiles
  before adding them to the mosaic. For example if we want to flip each
  image tile around the y axis before adding it to the mosaic, then
  <i>trim_section</i> should be set to <span style="font-family: monospace;">"[*,-*]"</span>.
  </dd>
  </dl>
  <dl id="l_missing_input">
  <dt><b>missing_input = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='missing_input' Line='missing_input = ""' -->
  <dd>The list of missing image tiles. For example if image tiles 3 to 5 and
  10 from a sequence of image tiles are missing then <i>missing_input</i> =
  <span style="font-family: monospace;">"3-5,10"</span>. This parameter uses the IRAF ranges syntax. The number of missing
  image tiles plus the number of input image tiles must equal <i>nctile</i> *
  <i>nltile</i>.
  </dd>
  </dl>
  <dl id="l_start_tile">
  <dt><b>start_tile = <span style="font-family: monospace;">"ll"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='start_tile' Line='start_tile = "ll"' -->
  <dd>The position of the first input image tile placed in the output image mosaic.
  The four options are <span style="font-family: monospace;">"ll"</span> for lower left corner, <span style="font-family: monospace;">"lr"</span> for lower right corner,
  <span style="font-family: monospace;">"ul"</span> for upper left corner and <span style="font-family: monospace;">"ur"</span> for upper right corner.
  </dd>
  </dl>
  <dl id="l_row_order">
  <dt><b>row_order = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='row_order' Line='row_order = yes' -->
  <dd>Add the input image tiles to the output image in row order. If row_order is
  <span style="font-family: monospace;">"no"</span> then column order is used instead.
  </dd>
  </dl>
  <dl id="l_raster_order">
  <dt><b>raster_order = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='raster_order' Line='raster_order = no' -->
  <dd>Add the input image tiles to the output image in a raster pattern or return
  to the start of a column or a row before adding a new image tile ?
  </dd>
  </dl>
  <dl id="l_median_section">
  <dt><b>median_section = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='median_section' Line='median_section = ""' -->
  <dd>The section of each input image tile used to compute the median value. If
  <i>median_section</i> is the null string then the medians are not computed.
  If <i>median_section</i> is <span style="font-family: monospace;">"[*,*]"</span> the entire input image tile is used to
  compute the median.
  </dd>
  </dl>
  <dl id="l_subtract">
  <dt><b>subtract = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subtract' Line='subtract = no' -->
  <dd>Subtract the median value from each input image tile before placing the
  tile in the output image?
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = INDEF' -->
  <dd>The number of columns in the output image. If <i>ncols</i> is INDEF then
  the program will compute the number of columns using the size of the input
  image tiles, <i>nctile</i>, and <i>ncoverlap</i>.
  </dd>
  </dl>
  <dl id="l_nlines">
  <dt><b>nlines = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlines' Line='nlines = INDEF' -->
  <dd>The number of lines in the output image. If <i>nlines</i> is INDEF then
  the program will compute the number of lines using the size of the input
  image tiles, <i>nltile</i> and <i>nloverlap</i>.
  </dd>
  </dl>
  <dl id="l_ncoverlap">
  <dt><b>ncoverlap = -1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncoverlap' Line='ncoverlap = -1' -->
  <dd>The number of columns between adjacent tiles in the output image. A negative
  value specifies the amount of column space between adjacent tiles. A positive
  value specifies the amount of column overlap on adjacent tiles.
  </dd>
  </dl>
  <dl id="l_nloverlap">
  <dt><b>nloverlap = -1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nloverlap' Line='nloverlap = -1' -->
  <dd>The number of lines between adjacent tiles in the output image. A negative
  value specifies the amount of lines space between adjacent tiles. A positive
  value specifies the amount of line overlap on adjacent tiles.
  </dd>
  </dl>
  <dl id="l_ovalue">
  <dt><b>ovalue = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ovalue' Line='ovalue = 0.0' -->
  <dd>The output image pixel value in regions undefined by the list of input
  image tiles.
  </dd>
  </dl>
  <dl id="l_opixtype">
  <dt><b>opixtype = <span style="font-family: monospace;">"r"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='opixtype' Line='opixtype = "r"' -->
  <dd>The pixel type of the output image. The options are <span style="font-family: monospace;">"s"</span> (short integer),
  <span style="font-family: monospace;">"i"</span> (integer), <span style="font-family: monospace;">"u"</span> (ushort), <span style="font-family: monospace;">"l"</span> (long integer), <span style="font-family: monospace;">"r"</span> (real) and
  <span style="font-family: monospace;">"d"</span> for double precision.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about the progress of the task?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IMTILE takes the list of same size input images (image tiles) specified by
  <i>input</i> and combines them into a tiled output image mosaic <i>output</i>.
  The order in which the input image tiles are placed in the output image is
  determined by the parameters <i>start_tile</i>, <i>row_order</i> and
  <i>raster_order</i>. The orientation of each individual image tile in the
  output image is set by the <i>trim_section</i> parameter.
  </p>
  <p>
  IMTILE uses the input image tile size, the number of image tiles, the
  <i>ncoverlap</i> and nloverlap<i> parameters, and the fInctile</i> and
  <i>nltile</i> parameters to compute the size of the output image. An image
  of size larger than the minimum required can be specified by setting the
  <i>ncols</i> and <i>nlines</i> parameters. The pixel type of the output
  image is specified by the <i>opixtype</i> parameter and undefined
  regions of the output image are assigned the value <i>ovalue</i>.
  </p>
  <p>
  The median of a section of each input image tile is computed by setting
  the <i>median_section</i> parameter,  and the computed median is subtracted
  from the input image tiles if the <i>subtract</i> parameter is set to <span style="font-family: monospace;">"yes"</span>.
  Task action messages will be printed on the standard output
  if <i>verbose</i> is set to yes.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Mosaic a list of 64 images onto an 8 by 8 grid in column order
  starting in the upper right hand corner. Allow one blank column and row
  between each subraster.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imtile @imlist mosaic 8 8 ncoverlap=-1 nloverlap=-1 \
      start_tile="ur" row-
  </pre></div>
  <p>
  2. Mosaic a list of 62 images onto an 8 by 8 grid in column order
  starting in the upper right hand corner. Allow one blank column and row
  between each subraster. Subrasters 3 and 9 in the sequence do not exist
  and are to be replaced in the output image with an unknown value of -1.0.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imtile @imlist mosaic 8 8 nxoverlap=-1 nyoverlap=-1  \
      start_corner="ur" row- missing_input="3,9", ovalue=-1.0
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
  imcombine
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

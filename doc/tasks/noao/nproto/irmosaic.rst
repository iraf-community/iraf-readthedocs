.. _irmosaic:

irmosaic: Mosaic an ordered list of images onto a grid
======================================================

**Package: nproto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mosaic input output database nxsub nysub
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input images to be mosaiced. The images are
  assumed to be ordered either by row,
  column, or in a raster pattern. If the image list is not in
  order then the iraf files task plus the editor must be used
  to construct an image list.  The images in the input list 
  are assumed to all be the same size.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The name of the output image.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>The name of the text file listing the operations performed by irmosaic.
  This list can be used as input for iralign.
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
  <dl id="l_trim_section">
  <dt><b>trim_section = <span style="font-family: monospace;">"[*,*]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trim_section' Line='trim_section = "[*,*]"' -->
  <dd>The section of the input images to be mosaiced into the output image.
  Section can be used to flip and/or trim the individual subrasters before adding
  them to the mosaic. For example if we want to flip each subraster around the
  y axis before adding it to the mosaic, then <i>trim_section</i> = <span style="font-family: monospace;">"[*,-*]"</span>.
  </dd>
  </dl>
  <dl id="l_null_input">
  <dt><b>null_input = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='null_input' Line='null_input = ""' -->
  <dd>The list of unobserved subrasters. For example if the subrasters 3 to 5 and
  10 of a sequence of observations were not observed then
  <i>null_input</i> = <span style="font-family: monospace;">"3-5,10"</span>.
  This parameter follows the ranges notation convention. The number of unobserved
  subrasters plus the number of images must equal <i>nxsub</i> *
  <i>nysub</i>.
  </dd>
  </dl>
  <dl id="l_corner">
  <dt><b>corner = <span style="font-family: monospace;">"ll"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='corner' Line='corner = "ll"' -->
  <dd>The starting position in the output image.
  The four options are <span style="font-family: monospace;">"ll"</span> for lower left corner, <span style="font-family: monospace;">"lr"</span> for lower right corner,
  <span style="font-family: monospace;">"ul"</span> for upper left corner and <span style="font-family: monospace;">"ur"</span> for upper right corner.
  </dd>
  </dl>
  <dl id="l_direction">
  <dt><b>direction = <span style="font-family: monospace;">"row"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='direction' Line='direction = "row"' -->
  <dd>Add subrasters to the output image in row or column order. The options are
  <span style="font-family: monospace;">"row"</span> for row order and <span style="font-family: monospace;">"column"</span> for column order.
  </dd>
  </dl>
  <dl id="l_raster">
  <dt><b>raster = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='raster' Line='raster = no' -->
  <dd>Add subrasters to the output image in a raster pattern or return to the start
  of a column or a row?
  </dd>
  </dl>
  <dl id="l_median_section">
  <dt><b>median_section = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='median_section' Line='median_section = ""' -->
  <dd>The section of each input subraster for which the median is computed. If
  <i>median_section</i> is the null string then the medians are not computed.
  If <i>median_section</i> is <span style="font-family: monospace;">"[*,*]"</span> the whole input subraster is used to
  compute the median.
  </dd>
  </dl>
  <dl id="l_subtract">
  <dt><b>subtract = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subtract' Line='subtract = no' -->
  <dd>Subtract the median value from each input subraster before placing the
  subraster in the output image.
  </dd>
  </dl>
  <dl id="l_nimcols">
  <dt><b>nimcols = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nimcols' Line='nimcols = INDEF' -->
  <dd>The number of columns in the output image. If <i>nimcols</i> is INDEF then
  the program will compute the number of columns using the size of the input
  subrasters, <i>nxsub</i> and <i>nxoverlap</i>.
  </dd>
  </dl>
  <dl id="l_nimrows">
  <dt><b>nimrows = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nimrows' Line='nimrows = INDEF' -->
  <dd>The number of rows in the output image. If <i>nimrows</i> is INDEF then
  the program will compute the number of rows using the size of the input
  subrasters, <i>nysub</i> and <i>nyoverlap</i>.
  </dd>
  </dl>
  <dl id="l_nxoverlap">
  <dt><b>nxoverlap = -1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxoverlap' Line='nxoverlap = -1' -->
  <dd>The number of columns between adjacent frames. A negative value specifies 
  the amount of column space between adjacent subrasters.
  A positive value specifies the amount of column overlap on adjacent
  subrasters.
  </dd>
  </dl>
  <dl id="l_nyoverlap">
  <dt><b>nyoverlap = -1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nyoverlap' Line='nyoverlap = -1' -->
  <dd>The number of rows between adjacent frames. A negative value specifies
  the amount of row space between adjacent subrasters.
  A positive value specifies the amount of row overlap on adjacent subrasters.
  </dd>
  </dl>
  <dl id="l_oval">
  <dt><b>oval = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='oval' Line='oval = 0.0' -->
  <dd>The output image pixel value in regions undefined by the by the list of input
  images.
  </dd>
  </dl>
  <dl id="l_opixtype">
  <dt><b>opixtype = <span style="font-family: monospace;">"r"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='opixtype' Line='opixtype = "r"' -->
  <dd>The pixel type of the output image. The options are <span style="font-family: monospace;">"s"</span> (short integer),
  <span style="font-family: monospace;">"i"</span> (integer), <span style="font-family: monospace;">"l"</span> (long integer), <span style="font-family: monospace;">"r"</span> (real) and <span style="font-family: monospace;">"d"</span> for double
  precision.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about task progress and actions taken.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IRMOSAIC takes a the list of subrasters of identical dimensions specified
  by <i>input</i> and combines them into a single
  output image <i>output</i>. The order in which the subrasters are placed
  in the output image is determined by the parameters <i>corner</i>,
  <i>direction</i> and <i>raster</i>. The orientation of each individual
  subraster in the output image may be altered by setting the <i>trim_section</i>
  parameter.
  </p>
  <p>
  IRMOSAIC uses the subraster size, the number of subrasters, the <i>nxoverlap</i>
  and nyoverlap<i> parameters and the fInxsub</i> and <i>nysub</i> partmeters
  to compute the size of the output image. An image of size larger than the
  minimum required can be specified by setting <i>nimcols</i> and <i>nimrows</i>. 
  The pixel type of the output image is specified by <i>opixtype</i> and undefined
  regions of the output image are given the value <i>oval</i>.
  </p>
  <p>
  The median of a section each subraster may be optionally computed
  and placed in the database file by setting <i>median_section</i>.
  The computed median will be subtracted from the input subrasters if
  <i>subtract</i> is set to yes.
  Task action messages will be printed on the standard output
  if <i>verbose</i> is set to yes.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Mosaic a list of 64 infrared images onto an 8 by 8 grid in column order
  starting in the upper right hand corner. Allow one blank column and row
  between each subraster.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pr&gt; irmosaic @imlist mosaic mosaic.dat nxsub=8 nysub=8 \
      nxoverlap=-1 nyoverlap=-1 corner="ur" direct="column"
  </pre></div>
  <p>
  2. Mosaic a list of 62 infrared images onto an 8 by 8 grid in column order
  starting in the upper right hand corner. Allow one blank column and row
  between each subraster. Subrasters 3 and 9 in the sequence do not exist
  and are to be replaced in the output image with an unknown value of -1.0.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pr&gt; irmosaic @imlist mosaic mosaic.dat nxsub=8 nysub=8 \
      nxoverlap=-1 nyoverlap=-1 corner="ur" direct="column"\
      null_input="3,9", oval=-1.0
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  At present only integral pixel overlaps are allowed in this routine.
  Fine tuning of the alignments can be done with iralign.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  iralign, irmatch1d, irmatch2d
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

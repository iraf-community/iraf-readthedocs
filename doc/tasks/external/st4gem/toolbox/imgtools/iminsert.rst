.. _iminsert:

iminsert: Insert an image into another by either adding,
========================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  iminsert input1 input2 output option coordfile
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task will copy the image passed to 'input1' into an output image. 
  The image passed to 'input2' is then inserted into the output image at 
  the position specified in 'coordfile';
  only the overlapping area will be changed.
  Multiple copies of 'input2' will be inserted into the output image
  if 'coordfile' contains more than one pair of coordinates.
  All images are assumed to be 2-dimensional.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input1">
  <dt><b>input1 [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input1' Line='input1 [file name]' -->
  <dd>Name of the larger input image.
  This is the image into which the smaller image will be inserted. 
  </dd>
  </dl>
  <dl id="l_input2">
  <dt><b>input2 [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input2' Line='input2 [file name]' -->
  <dd>Name of the smaller image that is to be inserted into 'input1'.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name]' -->
  <dd>The output image created by merging 'input2' into 'input1'.
  </dd>
  </dl>
  <dl id="l_option">
  <dt><b>option = replace  [string, allowed values: replace | add | multiply]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='option' Line='option = replace  [string, allowed values: replace | add | multiply]' -->
  <dd> 
  Method used to insert the small image into the larger image.  The option 
  <span style="font-family: monospace;">"replace"</span> will cause pixel values in 'input1' to be replaced by the 
  values in 'input2' at overlapping positions. The <span style="font-family: monospace;">"add"</span> option causes new 
  pixel values to be added to existing values, and the <span style="font-family: monospace;">"multiply"</span> option 
  causes the two values to be multiplied with the result going in the 
  output image. 
  </dd>
  </dl>
  <dl id="l_coordfile">
  <dt><b>coordfile [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coordfile' Line='coordfile [string]' -->
  <dd>A file which gives X and Y coordinates
  at which the insertion is to take place.
  The file may be either a reseau table, a cursor table, or a text file.
  One copy of 'input2' will be inserted into the output image
  for each X,Y pair in 'coordfile'.
  The X,Y values are taken to be the pixel coordinates in the output image
  where the first pixel ([1,1]) of 'input2' is to be placed.
  Real values will be rounded to the nearest integer. 
  See also 'offset1' and 'offset2'.
  For a text file or a cursor table, two columns are read,
  with column names given by the parameters 'xcol' and 'ycol'.
  For a text file <span style="font-family: monospace;">"c1"</span> and <span style="font-family: monospace;">"c2"</span> may be the appropriate column names.
  There may be many rows in the file,
  each one of which results in one copy of 'input2' in the output image.
  For a reseau table, 'xcol' and 'ycol' are ignored,
  and 'entry' is used to determine which row to read.
  The row will typically contain many reseau positions;
  'input2' will be inserted into the output at each reseau position.
  For information about using reseau tables, see the help files in the 
  'focgeom' package.  For information about using a cursor table, see the 
  help file for the 'tvcursor' task in the 'vdisplay' package.
  </dd>
  </dl>
  <dl>
  <dt><b>(offset1 = 0) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(offset1 = 0) [integer]' -->
  <dd>Offset to be added to X coordinates.
  </dd>
  </dl>
  <dl>
  <dt><b>(offset2 = 0) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(offset2 = 0) [integer]' -->
  <dd>Offset to be added to Y coordinates.
  </dd>
  </dl>
  <dl>
  <dt><b>(xcol = c1) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(xcol = c1) [string]' -->
  <dd>This is not used if 'coordfile' is a reseau table.
  Name of the column from which X coordinates will be read.
  The default value <span style="font-family: monospace;">"c1"</span> is appropriate if 'coordfile' is a text file,
  and the X coordinates are in the first column.
  </dd>
  </dl>
  <dl>
  <dt><b>(ycol = c2) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ycol = c2) [string]' -->
  <dd>This is not used if 'coordfile' is a reseau table.
  Name of the column from which Y coordinates will be read.
  The default value <span style="font-family: monospace;">"c2"</span> is appropriate if 'coordfile' is a text file,
  and the Y coordinates are in the second column.
  </dd>
  </dl>
  <dl>
  <dt><b>(entry = *) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(entry = *) [string]' -->
  <dd>Name of the reseau entry to use if 'coordfile' is a reseau table.
  This is ignored if 'coordfile' is a cursor table or text file.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create the image <span style="font-family: monospace;">"out"</span>, which is a copy of the image <span style="font-family: monospace;">"big"</span>, except 
  that at the coordinates specified in the text file <span style="font-family: monospace;">"coords.dat"</span> the 
  values are replaced by the pixel values of the image <span style="font-family: monospace;">"small"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; iminsert big small out replace coords.dat
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  reseau_files, focgeom, tvcursor
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

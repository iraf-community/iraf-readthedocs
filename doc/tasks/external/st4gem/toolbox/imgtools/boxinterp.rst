.. _boxinterp:

boxinterp: Fill areas with smoothed values from surrounding
===========================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  boxinterp input output coords
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task takes each image in turn, and for each specified point, fills 
  in a surrounding rectangle with cosmetic smooth values. The fill values 
  are calculated by fitting a bilinear surface to a  square annulus around 
  the point and evaluating it at each replaced pixel. The X,Y sides of the 
  inner rectangle and surrounding rectangle are specified by the user.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name template]' -->
  <dd>Input image(s) to be cosmetically smoothed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name template]' -->
  <dd>Output image file names. If an output file name is the same as that of 
  the input image, then the file is edited in place. 
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords [file name]' -->
  <dd>Name of the coordinates file. This may be either a reseau file, a binary 
  table, or an ASCII text file. This task will try to read the file first 
  as a reseau file, then as a table, and then as a text file until it 
  successfully reads the data. If the coordinate file is a table, then the 
  names of the columns to read for the X and Y coordinates are specified 
  by the 'xcol' and 'ycol' parameters, respectively.  If coordinates are 
  passed in a text file, then the numbers must be given as free format X,Y 
  coordinate pairs. INDEF values are ignored, as are points for which the 
  outer surrounding rectangle would not lie entirely within the  image.
  </dd>
  </dl>
  <dl>
  <dt><b>(innerx = 1) [integer, min=0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(innerx = 1) [integer, min=0]' -->
  <dd>X side of the inner box to fill. If 'innerx' is even, it will be 
  incremented.
  </dd>
  </dl>
  <dl>
  <dt><b>(outerx = 5) [integer, min=1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outerx = 5) [integer, min=1]' -->
  <dd>X side of the outer box to fill.  If 'outerx' is even, it will be 
  incremented.  The 'outerx' parameter must be greater in value than the
  'innerx' parameter.  If this is not the case, 'outerx' will be set to the value
  of 'innerx' plus 1.
  </dd>
  </dl>
  <dl>
  <dt><b>(innery = 1) [integer, min=0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(innery = 1) [integer, min=0]' -->
  <dd>Y side of the inner box to fill. If 'innery' is even, it will be 
  incremented.
  </dd>
  </dl>
  <dl>
  <dt><b>(outery = 5) [integer, min=1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outery = 5) [integer, min=1]' -->
  <dd>Y side of the outer box to fill. If 'outery' is even, it will be 
  incremented. The 'outery' parameter must be greater in value than the
  'innery' parameter.  If this is not the case, 'outery' will be set to the value
  of 'innery' plus 1.
  </dd>
  </dl>
  <dl>
  <dt><b>(entry = * ) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(entry = * ) [string]' -->
  <dd>Entry name to use if coords is a reseau table.
  </dd>
  </dl>
  <dl>
  <dt><b>(xcol = c1) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(xcol = c1) [string]' -->
  <dd>Name of the X column.  This parameter is used if 'coords' is a table. 
  </dd>
  </dl>
  <dl>
  <dt><b>(ycol = c2) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ycol = c2) [string]' -->
  <dd>Name of the Y column.  This parameter is used if 'coords' is a table. 
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>Print each image pair as processing progresses?
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Fill a rectangle of sides 3 x 5, centered at the point 100,200. The 
  fill data will be interpolated using the rectangle of side 7 x 9, 
  excluding the inner rectangle of 3 x 5.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  to&gt; boxinterp in out STDIN innerx=3 outerx=7 innery=4 outery=9
  100 200
  EOF
  
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_help">
  <h3>Help</h3>
  For assistance using this or any other tasks, please contact help@stsci.edu 
  or call the help desk at 410-338-1082.
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'HELP' 'SEE ALSO'  -->
  

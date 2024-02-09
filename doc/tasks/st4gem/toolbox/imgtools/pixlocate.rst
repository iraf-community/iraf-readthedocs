.. _pixlocate:

pixlocate: Print positions of all points inside (or outside) a
==============================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pixlocate input lowerlimit upperlimit
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task prints the coordinates and value of any pixel in an image
  where the value is within a specified range.
  As an alternative, the user may specify that the coordinates be printed
  when the value is outside the range.
  The user may also disable either end of the range to allow the task to
  look for pixels either above or below a specified value,
  with no limit on the range itself.
  A limit may be set on the number of pixels for which to print coordinates.
  Images with more than two dimensions may be processed.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name]' -->
  <dd>Name of the input image.
  </dd>
  </dl>
  <dl id="l_lowerlimit">
  <dt><b>lowerlimit = INDEF [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lowerlimit' Line='lowerlimit = INDEF [real]' -->
  <dd>Coordinates will be printed if the value is
  greater than or equal to 'lowerlimit'.
  (If 'outside' = yes, however,
  coordinates will be printed if the value is
  less than or equal to 'lowerlimit'.)  If this is INDEF
  then the lower limit is not checked.
  </dd>
  </dl>
  <dl id="l_upperlimit">
  <dt><b>upperlimit = INDEF [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='upperlimit' Line='upperlimit = INDEF [real]' -->
  <dd>Coordinates will be printed if the value is
  less than or equal to 'upperlimit'.
  (If 'outside' = yes, however,
  coordinates will be printed if the value is
  greater than or equal to 'upperlimit'.)  If this is INDEF
  then the upper limit is not checked.
  </dd>
  </dl>
  <dl>
  <dt><b>(maxvals = 1000) [integer, min=1]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(maxvals = 1000) [integer, min=1]' -->
  <dd>Maximum number of points whose coordinates should be printed.
  If more points than this are found,
  the task writes the message <span style="font-family: monospace;">"# maximum exceeded"</span> to STDERR and quits.
  </dd>
  </dl>
  <dl>
  <dt><b>(border = 0) [integer, min=0]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(border = 0) [integer, min=0]' -->
  <dd>Width of the border around all axes.  Pixels closer than this to the ends 
  of the axes are ignored.
  </dd>
  </dl>
  <dl>
  <dt><b>(outside = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outside = no) [boolean]' -->
  <dd>Print pixels with values outside the range ['lowerlimit' to 'upperlimit']?  
  The default value (<span style="font-family: monospace;">"no"</span>) will search for pixels inside the range.
  Pixel values equal to the limits are always marked.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Print the locations and values of all pixels
  greater than or equal to 10000 in dev$pix.imh.
  The first column is the first axis coordinate,
  and the second column is the second axis coordinate.
  The third column is the data value at that pixel.
  Following the command is a sample output from this task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; pixlocate dev$pix 10000 INDEF maxvals=5
  
  347  188  13988
  348  188  14640
  347  189  19530
  348  189  19936
  347  190  10100
  </pre></div>
  <p>
  1.  Print the coordinates and values
  of all points having values between 999 and 1000 
  in the image, with a border of 15 pixels around the axes.
  Sample output is also shown.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; pixlocate foctest$focim6 999 1000 border=15 outside=no
  
  292   52           999.
  224  124          1000.
  224  125          1000.
  224  126           999.
  </pre></div>
  <p>
  2.  Print the coordinates and values of all negative (or zero)
  points in the image,
  ignoring points closer than 10 pixels to the end of any axis.
  Up to 2000 pixels may be marked in this way.
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; pixlocate image 0 INDEF maxval=2000 border=10 outside=yes
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

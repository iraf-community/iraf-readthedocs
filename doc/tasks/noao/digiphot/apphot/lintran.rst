.. _lintran:

lintran: Linearly transform a coordinate list
=============================================

**Package: apphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  lintran files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>List file or files to be transformed.
  </dd>
  </dl>
  <dl id="l_xfield">
  <dt><b>xfield = 1, yfield = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xfield' Line='xfield = 1, yfield = 2' -->
  <dd>Fields containing the x and y coordinates.
  </dd>
  </dl>
  <dl id="l_x1">
  <dt><b>x1 = 0.0, y1 = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='x1' Line='x1 = 0.0, y1 = 0.0' -->
  <dd>Coordinates of current origin.
  </dd>
  </dl>
  <dl id="l_xscale">
  <dt><b>xscale = 1.0, yscale = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xscale' Line='xscale = 1.0, yscale = 1.0' -->
  <dd>Scale factor to be applied to the input coordinates, relative
  to the current origin [x1,y1].
  </dd>
  </dl>
  <dl id="l_angle">
  <dt><b>angle = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='angle' Line='angle = 0.0' -->
  <dd>Rotation angle about the origin [x1,y1].  This angle, measured
  counter clockwise from the positive x axis, is entered in
  degrees, unless <b>radians</b> = yes.
  </dd>
  </dl>
  <dl id="l_x2">
  <dt><b>x2 = 0.0, y2 = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='x2' Line='x2 = 0.0, y2 = 0.0' -->
  <dd>Coordinates of the new origin; input coordinates are shifted by an 
  amount (x2-x1) and (y2-y1).  Positive shifts indicate increasing distance
  from the current origin.  Applied after scaling and rotating the input 
  coordinates.
  </dd>
  </dl>
  <dl id="l_radians">
  <dt><b>radians = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radians' Line='radians = no' -->
  <dd>If this parameter is set to yes, <b>angle</b> is input
  in radians, not degrees.
  </dd>
  </dl>
  <dl id="l_min_sigdigits">
  <dt><b>min_sigdigits = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='min_sigdigits' Line='min_sigdigits = 1' -->
  <dd>The number of significant digits to be output in the transformed fields 
  is the maximum of this parameter and the number of input significant digits. 
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Specified fields from the input list can be scaled, rotated and shifted.
  Two fields of each input line are designated
  as the x and y coordinates to be transformed (default: fields 1, 2).
  All other fields are be preserved across the transformation.  
  For clarification, the equations used in the transformation are shown below:
  </p>
  <p>
  1. Subtract off the current origin:
  </p>
  <div class="highlight-default-notranslate"><pre>
  xt = x - x1
  yt = y - y1
  </pre></div>
  <p>
  2. Scale and rotate the coordinates:
  </p>
  <div class="highlight-default-notranslate"><pre>
  xs = xt * xscale
  ys = yt * yscale
  xt = xs * cos(angle) - ys * sin(angle)
  yt = xs * sin(angle) + ys * cos(angle)
  </pre></div>
  <p>
  3. Shift to the new origin:
  </p>
  <div class="highlight-default-notranslate"><pre>
  xt = xt + x2
  yt = yt + y2
  </pre></div>
  <p>
  Comment lines and blank lines are passed on to the output unmodified
  (a comment line is any line beginning with the character <span style="font-family: monospace;">'#'</span>).
  If either x or y is indefinite
  and no rotation is being performed, the corresponding
  output coordinate will be indefinite.  If either input coordinate is indefinite
  and a rotation is being performed, both output coordinates will be indefinite.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Shift the coordinate list frame1 so it represents positions
  in a second exposure of a star field, not registered with the first.  Take
  the coordinates of a star in frame1 to be the current origin 
  (e.g., [35.7, 389.2]); the new origin is then the coordinates of the same
  star in the second exposure ([36.9, 400.0]).  The shifted list is saved in
  file <span style="font-family: monospace;">"frame2"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lintran frame1 x1=35.7 y1=389.2 x2=36.9 y2=400.0 &gt; frame2
  </pre></div>
  <p>
  2. Apply a shift of +3.4 units in x, -1.3 units in y to the input list
  read from the standard input, writing the output list on the standard
  output.  
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; list_stream | lintran x2=3.4 y2=-1.3
  </pre></div>
  <p>
  3. Rotate a coordinate list of a 800x800 frame by 90 degrees.  The
  rotated coordinate list would represent positions in the field if it had
  been rotated, for example, from East to the right to East to the top.  
  Note that the rotation takes place about the central pixel [400.50,400.50]
  and that the current and new origins are the same:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lintran picture x1=400.5 y1=400.5 x2=400.5 y2=400.5 angle=90
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

.. _rgcursor:

rgcursor: Read the graphics cursor (makes a list)
=================================================

**Package: lists**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  gcursor
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <i>rgcursor</i> iteratively reads the graphics cursor, writing the
  cursor values to the standard output.  The standard output is normally
  redirected into a text file to generate a coordinate list to be used as
  input to one or more other programs.  Any IRAF program which reads the
  graphics cursor may be run taking input from a list prepared in advance
  with <i>rgcursor</i> (as well as interactively, of course).
  </p>
  <p>
  A plot should be drawn on the graphics terminal before running <i>rgcursor</i>.
  When the program is run a loop is entered, reading the global graphics
  cursor until the end of file character (e.g., &lt;ctrl/z&gt;, &lt;ctrl/d&gt;) is typed.
  Each cursor read causes a line to be printed on the standard output, after
  which the cursor is again read.
  </p>
  <p>
  While the program is waiting for the cursor to be read, i.e., whenever
  the cursor crosshairs are displayed, the terminal is said to be in
  <span style="font-family: monospace;">"cursor mode"</span>.  While in cursor mode, various commands may be entered,
  e.g., to zoom in a feature to get a more accurate cursor position, without
  terminating the current cursor read.  To read the cursor position, enter
  any key not recognized as a cursor mode command, i.e., any lower case or
  non-alphanumeric character.  The actual character one should type depends
  upon the program for which the list is intended.  If the program will use
  only the X and Y coordinates of the cursor any character may be typed,
  e.g., tap the space bar.  If the program uses the key to determine what
  action to take, then you must type a specific key.
  </p>
  <p>
  The X and Y coordinates of the cursor position and other information
  comprising the cursor value are printed on the standard output when the
  cursor is read.  The cursor position may optionally be marked whenever the
  cursor is read, by setting the <span style="font-family: monospace;">":.markcur"</span> option when in cursor mode.
  This is useful when preparing long lists to keep track of the objects
  or features that have already been marked.
  </p>
  <p>
  For additional information on <i>cursor mode</i> and the format of a cursor
  value string, type <span style="font-family: monospace;">"help cursor"</span>.  For information on the key and string values
  required by the applications program for which the cursor list is intended,
  consult the documentation for that program.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Interactively generate a starlist (file <span style="font-family: monospace;">"starlist"</span>) to be used as input
  to another program, e.g., for digital photometry.  In this case one would
  probably want to start with a contour plot labeled in image pixel coordinates.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; contour m74                 # make the plot
  cl&gt; rgcursor &gt; starlist         # make the object list
  </pre></div>
  <p>
  At this point, the cursor loop is entered and the terminal is placed
  into cursor mode.  Any of the following commands might be appropriate:
  </p>
  <div class="highlight-default-notranslate"><pre>
  <b>command</b>          <b>action</b>
  
  :.markcur+      enables marking of the cursor position
                      when the cursor is read
  
  :radius 7       set object radius in pixels
  :annulus 10 15  set annulus radii to be used for sky
  space_bar       mark the position of an object
  space_bar       mark the position of an object
                          (etc.)
  
  Z               zoom in on a feature to get a more
                      accurate cursor read
  space_bar       mark the position of the object
  space_bar       mark the position of another object
  0               replot the original plot
  
  &lt;crtl/z&gt;        (EOF) terminates rgcursor
  </pre></div>
  <p>
  Given the above command sequence, the output file <span style="font-family: monospace;">"starlist"</span> might
  contain the following cursor values.
  </p>
  <div class="highlight-default-notranslate"><pre>
  234.435 78.9292 1 : radius 7
  234.475 78.9243 1 : annulus 10 15
  67.2822 282.319 1 \40
  766.252 344.224 1 \40
  822.918 311.748 1 \40
  76.8272 822.139 1 \40
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rimcursor, cursor
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

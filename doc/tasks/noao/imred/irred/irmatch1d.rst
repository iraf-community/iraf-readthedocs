.. _irmatch1d:

irmatch1d: Align and intensity match the image produced by irmosaic (1D)
========================================================================

**Package: irred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  irmatch1d input output database coords
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The mosaiced image to be aligned. This image must have been produced by
  the IRMOSAIC task and have an accompanying database file specified by
  <i>database</i>.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The aligned image produced by IRMATCH1D.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>The database file from the IRMOSAIC task.
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords' -->
  <dd>If <i>alignment</i> = <span style="font-family: monospace;">"coords"</span>, then <b>coords</b> is
  a text file listing the coordinates of objects in the input
  image one object per line in the following
  format: 1) the x and y coordinates of the object in the first subraster
  2) the x and y coordinates of the same object in the second subraster
  3) the x and y coordinates of the next object in the first subraster
  etc.
  If <i>alignment</i> = <span style="font-family: monospace;">"file"</span>, then <b>coords</b> is a text file listing
  the x, y and intensity shifts in columns 1, 2 and 3 respectively,
  of each input subraster relative to the reference subraster. The
  most common use of this option is to make fine adjustments by hand
  to the output of IRMATCH1D by editing the computed shifts slightly and
  rerunning IRMATCH1D with the new shifts.
  </dd>
  </dl>
  <dl id="l_xshift">
  <dt><b>xshift</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xshift' Line='xshift' -->
  <dd>The x shift in pixel units if <i>alignment</i> = <span style="font-family: monospace;">"shifts"</span>.
  </dd>
  </dl>
  <dl id="l_yshift">
  <dt><b>yshift</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='yshift' Line='yshift' -->
  <dd>The y shift in pixel units if <i>alignment</i> = <span style="font-family: monospace;">"shifts"</span>.
  </dd>
  </dl>
  <dl id="l_alignment">
  <dt><b>alignment = <span style="font-family: monospace;">"coords"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='alignment' Line='alignment = "coords"' -->
  <dd>The method of aligning the subraster.
  <dl>
  <dt><b>coords</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='coords' Line='coords' -->
  <dd>The x and y positions of the marker points are listed in a file in the
  format specified by the <i>coords</i> parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>shifts</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='shifts' Line='shifts' -->
  <dd>The x and y shifts of a subraster with respect to its neighbour are
  set to <i>xshift</i> and <i>yshift</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>file</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='file' Line='file' -->
  <dd>The x,  y  and intensity shifts of each input subraster with respect to the
  reference subraster image.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_match">
  <dt><b>match = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='match' Line='match = "*"' -->
  <dd>Match intensities using the overlap region between adjacent subrasters. The
  median intensity is computed in the overlap region
  and the intensity scale of the current subraster is scaled to that of
  the previous subraster. Intensities are matched in one dimension in the order
  in which they
  are placed in the output image. The default is match everything.
  Those subrasters to be matched must be listed by number. For example to
  match intensities for subrasters 1 to 5 and 10 to 20 set match = <span style="font-family: monospace;">"1-5,10-20"</span>.
  To match all the subrasters set match = <span style="font-family: monospace;">"1-999"</span> or match=<span style="font-family: monospace;">"*"</span>.
  </dd>
  </dl>
  <dl id="l_nxrsub">
  <dt><b>nxrsub = INDEF, ls nyrsub = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxrsub' Line='nxrsub = INDEF, ls nyrsub = INDEF' -->
  <dd>The column and line index of the reference subraster.
  This will default to the central subraster.
  </dd>
  </dl>
  <dl id="l_xref">
  <dt><b>xref = 0, yref = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xref' Line='xref = 0, yref = 0' -->
  <dd>The x and y offset of the position of the reference subraster in the
  output image. The default action is to place the reference subraster
  in the same position in the output image as it has in the input image.
  </dd>
  </dl>
  <dl id="l_trimlimits">
  <dt><b>trimlimits = <span style="font-family: monospace;">"[1:1,1:1]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trimlimits' Line='trimlimits = "[1:1,1:1]"' -->
  <dd>The number of columns and rows to be trimmed off each edge of the
  input subraster before it is inserted in the output image in section
  notation. The default is to trim 1 column or row in each direction.
  </dd>
  </dl>
  <dl id="l_nimcols">
  <dt><b>nimcols = INDEF, ls nimlines = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nimcols' Line='nimcols = INDEF, ls nimlines = INDEF' -->
  <dd>The number of columns and rows in the output image. The default is the
  number of columns and rows in the input image.
  </dd>
  </dl>
  <dl id="l_oval">
  <dt><b>oval = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='oval' Line='oval = INDEF' -->
  <dd>The value of undefined pixels in the output image. The default is the value
  in the database file from IRMOSAIC.
  </dd>
  </dl>
  <dl id="l_interpolant">
  <dt><b>interpolant = linear</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interpolant' Line='interpolant = linear' -->
  <dd>The type of interpolant used to shift the subrasters. The options are:
  <dl>
  <dt><b>nearest</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nearest' Line='nearest' -->
  <dd>Nearest neighbour interpolation.
  </dd>
  </dl>
  <dl>
  <dt><b>linear</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='linear' Line='linear' -->
  <dd>Bilinear interpolation.
  </dd>
  </dl>
  <dl>
  <dt><b>poly3</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='poly3' Line='poly3' -->
  <dd>Bicubic polynomial interpolation.
  </dd>
  </dl>
  <dl>
  <dt><b>poly5</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='poly5' Line='poly5' -->
  <dd>Biquintic polynomial interpolation.
  </dd>
  </dl>
  <dl>
  <dt><b>spline3</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='spline3' Line='spline3' -->
  <dd>Bicubic spline interpolation.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print messages on the terminal describing the progress of the task.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IRMATCH1D takes the mosaiced image <i>input</i>, the database file <i>database</i>
  generated by IRMOSAIC and a list of coordinates <i>coords</i> and computes
  an output image <i>output</i> in which all the individual subrasters are aligned.
  If <i>alignment</i> = <span style="font-family: monospace;">"coords"</span>, IRMATCH1D accumulates the relative shifts
  between adjacent subrasters
  into a total shift with respect to the reference subraster. Shifts which
  do not correspond to adjacent subrasters are ignored.
  For subrasters which have no direct shift information, IRMATCH1D makes a best
  guess at the x and y shift based on the shifts of nearby subrasters which
  do have direct shift information.
  If the x and y shifts are sufficiently uniform over the whole input image
  the user may set <i>alignment</i>
  = shifts and input values of <i>xshift</i> and <i>yshift</i>.
  Alternatively the shifts may be read from the file <i>coords</i> if
  <i>alignment</i> = <span style="font-family: monospace;">"file"</span>.
  </p>
  <p>
  Coordinate lists may be generated interactively on the Sun workstations
  using the IRAF imtool facility and centered using the APPHOT CENTER
  and APSELECT tasks.
  </p>
  <p>
  The subrasters are inserted into the output image
  using the interpolation scheme defined by
  <i>interpolant</i> and is made with reference to the subraster defined
  by <i>nxrsub</i> and <i>nyrsub</i>, using the shifts defined by
  the coordinates in the file <i>coords</i> or defined by <i>xshift</i> and
  <i>yshift</i>. Subrasters are placed in the output image in the order
  they were inserted into the original mosaic with pixels in the most
  recently placed subrasters replacing those placed earlier in the overlap
  regions. Undefined pixels in the output image
  are given the value <i>oval</i>. The position of the reference image in the
  output image can be adjusted by setting the parameters <i>xref</i> and
  <i>yref</i>. The edges of each subraster may be trimmed before
  insertion into the output image by setting the <i>trimlimits</i> parameter.
  </p>
  <p>
  Intensities of adjacent subrasters can be matched using the <i>match</i>
  parameters. At present matching is done by computing the median in the
  overlap region between adjacent subrasters and applying difference in
  these two numbers to the subraster in question. Intensity matching is
  done in one dimension  only with the direction of matching following
  the order that the individual subrasters were inserted into the mosaic.
  For example if IRMOSAIC was run with <i>corner</i> = <span style="font-family: monospace;">"ll"</span>, <i>direction</i>
  =<span style="font-family: monospace;">"row"</span> and <i>raster</i> = <span style="font-family: monospace;">"no"</span>, then the matching would start in the
  lower-left corner, proceed along the first row, move to the star of the
  second row and so on.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Align an 8 by 8 mosaic with respect to subraster 6, 5.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pr&gt; irmatch1d mosaic mosaic.al mosaic.db coords nxrsub=6 \
      nyrsub=5
  </pre></div>
  <p>
  2. Align an 8 by 8 mosaic as 1 above but shift the position of the
  reference subraster in the output image by 2 pixels in x and 3 pixels
  in y.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pr&gt; irmatch1d mosaic mosaic.al mosaic.db coords nxrsub=6 \
      nyrsub=5 xref=2 yref=3
  </pre></div>
  <p>
  3. Align an 8 by 8 mosaic as 1 above but trim 2 rows and columns off
  of each input image before inserting into the output image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pr&gt; irmatch1d mosaic mosaic.al mosaic.db coords nxrsub=6 \
      nyrsub=5 trimlimits="[2:2,2:2]"
  </pre></div>
  <p>
  4. Rerun the above example saving the verbose output in a file. Use the 
  PROTO package fields task to select the xshift, yshift and intensity
  shift fields, edit the shifts slightly and rerun irmatch1d with the
  new shifts.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pr&gt; irmatch1d mosaic mosaic.al mosaic.db coords nxrsub=6 \
      nyrsub=5 trimlimits="[2:2,2:2]" &gt; shifts1
  
  pr&gt; fields shifts1 3,4,6 &gt; shifts2
  
  pr&gt; edit shifts2
  
      ... make whatever changes are desired
  
  pr&gt; irmatch1d mosaic mosaic.al mosaic.db shifts2 align=file \
      nxrsub=6 nyrsub=5 trimlimits="[2:2,2:2]"
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
  irmosaic, iralign, irmatch2d, apphot.center, apphot.apselect
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _iralign:

iralign: Align the image produced by irmosaic
=============================================

**Package: irred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  iralign input output database coords
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The mosaiced image written by IRMOSAIC.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output aligned image.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>The database file written by IRMOSAIC.
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords' -->
  <dd>If <i>alignment</i> = <span style="font-family: monospace;">"coords"</span>, then <b>coords</b> is
  a text file containing the x and y coordinates, measured in the input
  mosaiced image, of reference objects common
  to adjacent subrasters in the input mosaiced
  image. The reference coordinates are written with the following format:
  line 1) the x and y coordinates of an object in the any subraster,
  line 2) the x and y coordinates of the same object in any adjacent subraster,
  line 3) the x and y coordinates of another object in the any subraster,
  line 4) the x and y coordinates of the same object in any adjacent subraster,
  etc.
  If <i>alignment</i> = <span style="font-family: monospace;">"file"</span>, then <b>coords</b> is a text file containing
  the x and y shifts in columns 1 and 2 respectively,
  of each subraster relative to the reference subraster, in the order
  in which the subrasters were written into the mosaiced input image.
  This option can be used to make fine adjustments to the output aligned image
  by manually editing the computed shifts and rerunning
  IRALIGN with the new shifts.
  </dd>
  </dl>
  <dl id="l_xshift">
  <dt><b>xshift</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xshift' Line='xshift' -->
  <dd>The x shift in pixels used if <i>alignment</i> = <span style="font-family: monospace;">"shifts"</span>.
  </dd>
  </dl>
  <dl id="l_yshift">
  <dt><b>yshift</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='yshift' Line='yshift' -->
  <dd>The y shift in pixels used if <i>alignment</i> = <span style="font-family: monospace;">"shifts"</span>.
  </dd>
  </dl>
  <dl id="l_alignment">
  <dt><b>alignment = <span style="font-family: monospace;">"coords"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='alignment' Line='alignment = "coords"' -->
  <dd>The method of aligning the subraster.
  <dl>
  <dt><b>coords</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='coords' Line='coords' -->
  <dd>The x and y positions of the reference points common to adjacent subrasters
  in the input mosaiced image are listed in a text file as described
  under the help for the  <i>coords</i> parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>shifts</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='shifts' Line='shifts' -->
  <dd>The x and y shifts of each subraster with respect to its neighbour are
  set to <i>xshift</i> and <i>yshift</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>file</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='file' Line='file' -->
  <dd>The x and y  shifts of each input subraster with respect to the
  reference subraster image are listed in a text file as described
  under the help for the <i>coords</i> parameter.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_nxrsub">
  <dt><b>nxrsub = INDEF, ls nyrsub = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nxrsub' Line='nxrsub = INDEF, ls nyrsub = INDEF' -->
  <dd>The column and row index of the reference subraster.
  The default reference subraster is the central subraster.
  </dd>
  </dl>
  <dl id="l_xref">
  <dt><b>xref = 0, yref = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xref' Line='xref = 0, yref = 0' -->
  <dd>The x and y offset of the reference
  subraster in the output aligned image.
  By default the reference subraster occupies the same position in
  the output image that it does in the input image.
  </dd>
  </dl>
  <dl id="l_trimlimits">
  <dt><b>trimlimits = <span style="font-family: monospace;">"[1:1,1:1]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trimlimits' Line='trimlimits = "[1:1,1:1]"' -->
  <dd>The number of columns or rows to trim off each edge of each input subraster
  before inserting it in the output image, specified in image section notation.
  The default action is to trim 1 column or line at each edge of the subraster.
  </dd>
  </dl>
  <dl id="l_nimcols">
  <dt><b>nimcols = INDEF, nimlines = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nimcols' Line='nimcols = INDEF, nimlines = INDEF' -->
  <dd>The number of columns and lines in the output image. The defaults are  the
  number of columns and lines in the input image.
  </dd>
  </dl>
  <dl id="l_oval">
  <dt><b>oval = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='oval' Line='oval = INDEF' -->
  <dd>The value of undefined pixels in the output image. The default is the value
  stored in the database file written by IRMOSAIC.
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
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages on the terminal describing the progress of the task?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IRALIGN takes the mosaiced image <i>input</i> and database
  <i>database</i> files
  written by IRMOSAIC, and a list of reference object
  coordinates <i>coords</i> created by the user, and writes
  an output image <i>output</i> in which all the subrasters are aligned
  with respect to a reference subraster.
  </p>
  <p>
  If <i>alignment</i> = <span style="font-family: monospace;">"coords"</span>, IRALIGN accumulates the relative shifts
  between adjacent subrasters defined by the data in <i>coords</i>,
  into a total shift for each subraster with respect to the reference subraster.
  Relative shifts defined for non-adjacent subrasters are ignored.
  For those subrasters which have no relative shift information,
  IRALIGN makes a best guess at the relative x and y shifts
  based on the relative x andy shifts of nearby subrasters
  which do have relative shift information.  If the x and y shifts
  are sufficiently uniform over the whole input image the user may set
  <i>alignment</i> to  <span style="font-family: monospace;">"shifts"</span> and supply values for
  <i>xshift</i> and <i>yshift</i>.
  Alternatively the total shifts may be read directly from the  file <i>coords</i>
  if <i>alignment</i> = <span style="font-family: monospace;">"file"</span>.
  </p>
  <p>
  Coordinate lists for the <i>alignment</i> = <span style="font-family: monospace;">"coords"</span> option,
  may be generated interactively using the RIMCURSOR, 
  or APPHOT package CENTER and APSELECT tasks. For example a coordinate list
  written by RIMCURSOR for a 
  4 by 4 mosaic of 51 by 51 pixel square images containing a single
  reference object common to all the subrasters might look like the following.
  </p>
  <div class="highlight-default-notranslate"><pre>
  41.3   42.6     1 \40   # coordinates of ref object in subraster 1
  62.0   38.5     1 \40   # coordinates of ref object in subraster 2
  41.3   42.6     1 \40   # coordinates of ref object in subraster 1
  38.1   95.8     1 \40   # coordinates of ref object in subraster 3
  62.0   38.5     1 \40   # coordinates of ref object in subraster 2
  70.3   89.0     1 \40   # coordinates of ref object in subraster 4
  38.1   95.8     1 \40   # coordinates of ref object in subraster 3
  70.3   89.0     1 \40   # coordinates of ref object in subraster 4
  </pre></div>
  <p>
  In this example subrasters 1 and 2 are in the lower-left and
  lower-right hand corners of
  the mosaiced image respectively, while subrasters 3 and 4 are in the
  upper-left and upper- right hand corner of the mosaiced image.
  Any number of reference objects may be used.
  </p>
  <p>
  The subrasters are inserted into the output image using the
  interpolation scheme defined by
  <i>interpolant</i>, and aligned with reference to the subraster defined
  by <i>nxrsub</i> and <i>nyrsub</i>, using the shifts defined by
  the data in the file <i>coords</i> or defined by <i>xshift</i> and
  <i>yshift</i>. Subrasters are inserted into the output image in the order
  they were placed in the original mosaic with pixels in the most recently
  placed subrasters replacing those in earlier placed ones in the overlap regions.
  Undefined pixels in the output image
  are assigned the value <i>oval</i>. The position of the reference subraster
  in the output image may be adjusted by setting the offset parameters
  <i>xref</i> and <i>yref</i>. The edges of each subraster may be trimmed
  before insertion into the output image by setting the <i>trimlimits</i>
  parameter.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Align an 8 by 8 mosaic with respect to subraster 6, 5.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pr&gt; iralign mosaic mosaic.al mosaic.db coords nxrsub=6 \
      nyrsub=5
  </pre></div>
  <p>
  2. Align an 8 by 8 mosaic as in example 1 above but shift the position of the
  reference subraster in the output image by 2 pixels in x and 3 pixels
  in y.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pr&gt; iralign mosaic mosaic.al mosaic.db coords nxrsub=6 \
      nyrsub=5 xref=2 yref=3
  </pre></div>
  <p>
  3. Align an 8 by 8 mosaic as 1 above but trim 2 rows and columns off
  of each input subraster before inserting it into the output image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pr&gt; iralign mosaic mosaic.al mosaic.db coords nxrsub=6 \
      nyrsub=5 trimlimits="[2:2,2:2]"
  </pre></div>
  <p>
  4. Rerun the above example saving the verbose output in a file. Use the 
  PROTO package FIELDS task to select the xshift, yshift and intensity
  shift fields, edit the shifts manually and rerun IRALIGN with the
  new shifts.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pr&gt; iralign mosaic mosaic.al mosaic.db coords nxrsub=6 \
      nyrsub=5 trimlimits="[2:2,2:2]" &gt; shifts1
  
  pr&gt; fields shifts1 3,4,6 &gt; shifts2
  
  pr&gt; edit shifts2
  
      ... make whatever changes are desired
  
  pr&gt; iralign mosaic mosaic.al.2 mosaic.db shifts2 align=file \
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
  irmosaic, apphot.center, apphot.apselect, irmatch1d, irmatch2d
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

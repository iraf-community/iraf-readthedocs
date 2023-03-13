.. _ofixpix:

ofixpix: Fix bad pixels using text file (proto V2.10.4)
=======================================================

**Package: obsolete**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  ofixpix images badpixels
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>List of two dimensional images to be modified.
  </dd>
  </dl>
  <dl id="l_badpixels">
  <dt><b>badpixels</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='badpixels' Line='badpixels' -->
  <dd>File containing the regions of bad pixels.  A region is described by
  four whitespace separated numbers consisting of the first and last columns
  of the bad region and the first and last lines of the bad region.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print the image names and the bad pixel regions?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Bad pixel regions in the list of two dimensional images are replaced by
  linear interpolation using pixels bordering the bad pixel regions.
  The bad pixel regions are input in the specified file consisting of lines
  of coordinates (x1 x2 y1 y2) where x1 and x2 are the first and last columns
  of the bad region and y1 and y2 are the first and last lines of the
  bad region.  The file may be STDIN to read from the standard input.
  The type of interpolation is determined as follows:
  </p>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(1)' -->
  <dd>If the bad region spans entire lines then the interpolation is from
  neighboring lines.
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(2)' -->
  <dd>If the bad region spans entire columns then the interpolation is from
  neighboring columns.
  </dd>
  </dl>
  <dl>
  <dt><b>(3)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(3)' -->
  <dd>If the bad region contains more lines than columns then the interpolation
  is from neighboring columns.
  </dd>
  </dl>
  <dl>
  <dt><b>(4)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(4)' -->
  <dd>If the bad region contains the same or more columns than lines then the
  interpolation is from neighboring lines.
  </dd>
  </dl>
  <p>
  If the bad region borders the edge of the image then the interpolation
  is by replication of the first good pixel in the direction of interpolation
  and otherwise linear interpolation between the bordering lines or columns
  is used.  The verbose parameter may be used to produce of log of the pixel
  modifications.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  A detector has bad lines 10 and 25 to 27 and a partial bad column
  at column 31 between lines 35 and 50.  A bad region file is created containing
  the lines
  </p>
  <div class="highlight-default-notranslate"><pre>
  1 100 10 10
  1 100 25 27
  31 31 35 50
  </pre></div>
  <p>
  The set of images <span style="font-family: monospace;">"image*"</span> are fixed by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ofixpix image* badpixfile
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_OFIXPIX">
  <dt><b>OFIXPIX V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='OFIXPIX' Line='OFIXPIX V2.11' -->
  <dd>This is the V2.10.4 and earlier version of PROTO.FIXPIX.
  </dd>
  </dl>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  This is a simple minded task which can be improved by using more sophisticated
  interpolation.  The bad pixel file will eventually be replaced by image
  masks and bad pixel lists in the image.  Be careful with image sections because
  the bad pixel regions are relative to the image section.  Also if the image
  is trimmed or rotated then the bad pixel regions must be changed.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  epix, imedit, fixpix
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'BUGS' 'SEE ALSO'  -->
  

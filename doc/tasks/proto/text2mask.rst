.. _text2mask:

text2mask: Convert text description to pixel mask
=================================================

**Package: proto**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  text2mask text mask ncols nlines
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_text">
  <dt><b>text</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='text' Line='text' -->
  <dd>Text file of pixel regions.  The format of this file consists of lines of
  individual pixels (whitespace separated column and line) or rectangular
  regions (whitespace separated starting and ending columns and starting and
  ending lines).
  </dd>
  </dl>
  <dl id="l_mask">
  <dt><b>mask</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mask' Line='mask' -->
  <dd>Pixel mask name to be created.  A pixel list image, .pl extension,
  is created so no extension is necessary.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols, nlines</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols, nlines' -->
  <dd>Dimensions for pixel mask image.
  </dd>
  </dl>
  <dl id="l_linterp">
  <dt><b>linterp = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linterp' Line='linterp = 1' -->
  <dd>Mask code for rectangular regions which are narrower in the line direction
  than the column direction.
  </dd>
  </dl>
  <dl id="l_cinterp">
  <dt><b>cinterp = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cinterp' Line='cinterp = 2' -->
  <dd>Mask code for rectangular regions which are narrower in the column direction
  than the line direction.
  </dd>
  </dl>
  <dl id="l_square">
  <dt><b>square = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='square' Line='square = 3' -->
  <dd>Mask code for square regions which are larger than a single pixel.
  </dd>
  </dl>
  <dl id="l_pixel">
  <dt><b>pixel = 4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixel' Line='pixel = 4' -->
  <dd>Mask code for single pixels.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A text file describing individual pixels or rectangular regions is
  converted to a pixel mask image in pixel list format.  The name of
  the text file, the name of the pixel mask to be created, and the
  dimensions of the pixel mask image are specified.
  </p>
  <p>
  The text file consists of lines of two or four numbers.  If two numbers
  are given, separated by whitespace, they define a single pixel and
  the values are the column and line pixel coordinates.  If four numbers
  are given, separated by whitespace, they define a rectangular region.
  The four numbers are the pixel coordinates for the starting column,
  the ending column, the starting line, and the ending line.  This format
  is the same as the old (pre-V2.11) <span style="font-family: monospace;">"fixpix"</span> format.  This task may
  be used to convert these old <span style="font-family: monospace;">"fixpix"</span> data files to pixel masks (as used
  by the new <b>fixpix</b> task) or to create pixel masks.
  </p>
  <p>
  The different region shapes may be coded by the mask values.  This is
  useful with the <b>fixpix</b> task which can select different replacement
  methods based on the mask codes.  In particular, one may want to interpolate
  along the narrower dimension of a rectangular region.  The region
  shapes that may be coded are individual pixels, square regions, and
  rectangular regions with narrow dimension along lines or columns.
  </p>
  <p>
  In addition to this task,
  pixel mask images may be made in a variety of ways.  Any task which produces
  and modifies image values may be used.  Some useful tasks are
  <b>imexpr, imreplace, imcopy,</b> and <b>mkpattern</b>.  If a new image
  is specified with the explicit <span style="font-family: monospace;">".pl"</span> extension then the pixel mask
  format is produced.  Another way to make masks are with the
  task <b>ccdmask</b>.  The task <b>ccdmask</b> is specialized to make a mask
  of bad pixels from flat fields or, even better, from the ratio of
  two flat fields of different exposure levels.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Convert a text region description into a mask and then use it to
  replace pixels by interpolation along the narrower dimension.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; list2mask fp.dat mask
  cl&gt; fixpix pix mask linterp=1,3,4 cinterp=2
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_TEXT2MASK">
  <dt><b>TEXT2MASK V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='TEXT2MASK' Line='TEXT2MASK V2.11' -->
  <dd>This task is new and appears in conjunction with a new pixel mask
  based version of <b>fixpix</b>.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imreplace, imexpr, imcopy, imedit, fixpix
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

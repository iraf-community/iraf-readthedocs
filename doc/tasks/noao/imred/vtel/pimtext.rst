.. _pimtext:

pimtext: Put text directly into images using a pixel font.
==========================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pimtext iraf_files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_iraf_files">
  <dt><b>iraf_files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='iraf_files' Line='iraf_files' -->
  <dd>Image or images to be written into.  This entry may contain wild cards and
  will be expanded into however many files match the wild card.
  </dd>
  </dl>
  <dl id="l_refim">
  <dt><b>refim</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refim' Line='refim' -->
  <dd>Reference image to pull date and time parameters from in the event the <span style="font-family: monospace;">"ref"</span>
  flag is set.
  </dd>
  </dl>
  <dl id="l_ref">
  <dt><b>ref</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ref' Line='ref' -->
  <dd>Reference flag.  When set, causes the program to take information (date/time)
  from the reference image and write it into the image or images expanded from
  the template <span style="font-family: monospace;">"iraf_images"</span>.
  </dd>
  </dl>
  <dl id="l_x">
  <dt><b>x = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='x' Line='x = 10' -->
  <dd>X position (column) in image to write text.
  </dd>
  </dl>
  <dl id="l_y">
  <dt><b>y = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='y' Line='y = 10' -->
  <dd>Y position (line) in image to write text.
  </dd>
  </dl>
  <dl id="l_xmag">
  <dt><b>xmag = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmag' Line='xmag = 2' -->
  <dd>Factor by which to magnify the text in the x direction.  This must be an
  integer.  The pixelfont is expanded by pixel replication.  The font width
  at xmag=1 is 6.
  </dd>
  </dl>
  <dl id="l_ymag">
  <dt><b>ymag = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ymag' Line='ymag = 2' -->
  <dd>Factor by which to magnify the text in the y direction.  This must be an
  integer.  The pixelfont is expanded by pixel replication.  The font width
  at ymag=1 is 7.
  </dd>
  </dl>
  <dl id="l_val">
  <dt><b>val = -10000</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='val' Line='val = -10000' -->
  <dd>Value to put in text pixels.
  </dd>
  </dl>
  <dl id="l_setbgnd">
  <dt><b>setbgnd = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='setbgnd' Line='setbgnd = yes' -->
  <dd>Boolean parameter to signal the program to fill in the area behind the
  characters with pixels set to bgndval.
  </dd>
  </dl>
  <dl id="l_bgndval">
  <dt><b>bgndval = 10000</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bgndval' Line='bgndval = 10000' -->
  <dd>Pixel value to use to fill in background in text block.
  </dd>
  </dl>
  <dl id="l_date">
  <dt><b>date = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='date' Line='date = yes' -->
  <dd>Flag that instructs the program to look for the date in the 
  image header and write it into the image.  If the date and time
  flags are both set, both will be written into the image as a single
  string.
  </dd>
  </dl>
  <dl id="l_time">
  <dt><b>time = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='time' Line='time = yes' -->
  <dd>Flag that instructs the program to look for the time in the 
  image header and write it into the image.
  </dd>
  </dl>
  <dl id="l_text">
  <dt><b>text</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='text' Line='text' -->
  <dd>Text string to write into image.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Pimtext writes either the date and/or time or the indicated text string into
  the image or images specified.
  Pimtext, by default, writes the date and/or time into the image in the lower
  left corner.  If it cannot find the date or time pimtext will give a warning
  and read a text string from the users terminal.  If the date and time flags are
  set to 'no', pimtext will take the text string to be written from the user.
  The position of the text may be adjusted by setting
  the parameters <span style="font-family: monospace;">'x'</span> and <span style="font-family: monospace;">'y'</span> which set the lower left pixel of
  the text block.  The pixels in the text block behind the characters may
  be set to a particular value when the 'setbgnd' flag is set.  The pixel
  values used to write the text and the background can be set by adjusting
  the parameters 'val' and 'bgndval'.  If the text overlaps the image
  edge in the X direction it will be truncated.  If it overlaps in Y it will
  not be written.
  The user may magnify the text by adjusting the <span style="font-family: monospace;">"xmag"</span> and <span style="font-family: monospace;">"ymag"</span> parameters.
  The default (2,2) is a nice size for display in a 512 by 512 image.  Bigger
  images may need bigger text, smaller images may need smaller text.
  The <span style="font-family: monospace;">"ref"</span> flag is used to write information from one image into another
  image.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To write the date and time into the three images s13_1709_001, v13_1709_001,
  and b13_1709_001 (assuming the directory contains only these three images)
  the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; pimtext ?13*
  </pre></div>
  <p>
  2. To write the text string <span style="font-family: monospace;">"hello world"</span> into the image 'testim' the command
  would be
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; pimtext testim 'hello world' date=no time=no
  </pre></div>
  <p>
  3. To write the date and time into the images s1, s2, s3, s4 and position
  the text at pixel 30,30, and turn off the text background fill, the command
  would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; pimtext s* x=30 y=30 setbgnd=no
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

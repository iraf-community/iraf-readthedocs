.. _rgbsun:

rgbsun: Create a Sun 24-bit RGB rasterfile
==========================================

**Package: color**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rgbsun red green blue rgb
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_red">
  <dt><b>red, green, blue</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='red' Line='red, green, blue' -->
  <dd>Input image names for the red, green, and blue components.  The images
  must all be two dimensional and of the same size.
  </dd>
  </dl>
  <dl id="l_rgb">
  <dt><b>rgb</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rgb' Line='rgb' -->
  <dd>Output file name for the Sun 24-bit RGB rasterfile.
  </dd>
  </dl>
  <dl id="l_rz1">
  <dt><b>rz1, rz2, gz1, gz2, bz1, bz2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rz1' Line='rz1, rz2, gz1, gz2, bz1, bz2' -->
  <dd>Range of values in the input images to be mapped to the minimum and maximum
  intensity in each color.  Image pixel values outside the range are mapped
  to the nearest endpoint.  The values correspond to the input image
  intensities even when using logarithmic mapping.
  </dd>
  </dl>
  <dl id="l_logmap">
  <dt><b>logmap = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logmap' Line='logmap = no' -->
  <dd>Use logarithmic intensity mapping?  The logarithm of the input pixel
  values, in the range given by the z1 and z2 parameters, is taken before
  dividing the range into the 85 display levels.  Logarithmic mapping allows
  a greater dynamic range.
  </dd>
  </dl>
  <dl id="l_swap">
  <dt><b>swap = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='swap' Line='swap = no' -->
  <dd>Swap rasterfile bytes on output?  Used when rasterfiles are being written
  to a computer with opposite byte-swapping from that of the home computer
  (e.g. between VAX and Sun).
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Rgbsun</b> takes three input IRAF images and produces a 24-bit Sun
  rasterfile.  Though this file type was developed by Sun Microcomputers it
  is a relatively simple format which may useful on other machines have
  software designed to use it.  The color image may be display with a variety
  of tools such as <b>xv</b> (a very powerful and generic, public domain
  viewer for X-window systems), <b>xloadimage</b> (another X-window display
  tool), <b>screenload</b> (a simple displayer on Sun computers), and
  <b>snapshot</b> (a Open-Look tool).  Also some color printers can be used
  with this format such as a Shinko color printer.
  </p>
  <p>
  If one wants to display images which have a large dyanmic range it
  may be desirable to first take the logarithm of each image.  This may
  be done with the <i>logmap</i> parameter.  Other types of stretching may
  be accomplished by modifying the individual images first, say with
  <b>imfunction</b>.
  </p>
  <p>
  If the output rasterfiles are being sent to a computer with opposite
  byte-swapping characteristics, set <i>swap</i> = yes (e.g., when running
  <b>rgbsun</b> on a VAX, with output to a Sun).
  </p>
  <p>
  The rasterfile format produced is quite simple.  There is a header with 8
  integer values immediately followed by the data values.  The header has the
  following values of interest:
  </p>
  <p>
  	Word 1:  Magic numer = 1504078485
  	Word 2:  The number of columns
  	Word 3:  The number of lines
  	Word 4:  The number of bits per pixel = 24
  </p>
  <p>
  The data consists of triplets of 8-bit data values in the order blue,
  green, and red.  The triplet pixels are ordered by varying the column
  elements first and then the line elements.  The sequence is continuous
  except that each line is padded, if necessary, to maintain a multiple of 2
  bytes per line (with 3 bytes per pixel this means that images with an odd
  number of columns will have an extra zero byte).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Three 2048x2048 images of the Trifid nebula are obtained in the B, V,
  and R bandpasses.  These images are properly registered.  Examination of
  the histograms leads to selecting the display ranges 1-500 in each band.
  The image is then displayed on a workstation running an X-window system
  using the <b>xv</b> utility.  The file is also printed to a local
  color printer interfaced as a Unix printer (the Shinko at NOAO).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rgbsun trifidr trifidv trifidb trifid.ras \
  &gt;&gt;&gt; rz1=1 rz2=500 gz1=1 gz2=500 bz1=1 bz2=500
  cl&gt; !xv -swap24 trifid.ras
  cl&gt; !lpr -Pclp trifd.ras
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  Example 1 takes 2:20 minutes (33 seconds CPU) on a SparcStation 2.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rgbdither, rgbto8, color.package
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'SEE ALSO'  -->
  

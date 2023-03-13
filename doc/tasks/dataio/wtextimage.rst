.. _wtextimage:

wtextimage: Convert an IRAF image to a text file
================================================

**Package: dataio**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  wtextimage input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>An IRAF image file name or template of file names to be converted.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Name or root_name of output text file.  If more than one IRAF image
  is being converted, the ordinal of the file in the input file list
  is appended to <i>output</i> to generate a unique output file name.
  </dd>
  </dl>
  <dl id="l_header">
  <dt><b>header = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='header' Line='header = yes' -->
  <dd>This parameter determines whether or not a descriptive header precedes
  the pixels written to the text file.  When <i>header = no</i>, only
  pixels values are converted; no header information is included in the
  output.
  </dd>
  </dl>
  <dl id="l_pixels">
  <dt><b>pixels = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixels' Line='pixels = yes' -->
  <dd>This parameter determines whether or not to write the pixels to the
  text file.  This can be set to no to only write out the header.
  </dd>
  </dl>
  <dl id="l_format">
  <dt><b>format = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='format' Line='format = ""' -->
  <dd>Output format for each pixel.  If not set by the user, the appropriate output 
  pixel format is determined by the image data type.
  Acceptable formats are chosen from <span style="font-family: monospace;">"W.D[defgz]"</span> where w is the field width and 
  d specifies the precision.  Fortran formats of the form [iefgz]W.D are also
  acceptable.  If a field width of 0 is specified, (e.g., 0.6g),
  output will be free format with each output line containing as many pixels as
  will fit on the line.  This is the most space efficient format but requires
  that the reader program be able to handle free format (list directed) input.
  </dd>
  </dl>
  <dl id="l_maxlinelen">
  <dt><b>maxlinelen = 80</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxlinelen' Line='maxlinelen = 80' -->
  <dd>The maximum number of characters output per line of text; <b>maxlinelen</b>
  must not exceed 322 characters.  (Note that tasks <i>rtextimage</i> and
  <i>wcardimage</i> cannot read lines of text greater than 161 characters.)
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IRAF images are converted to text files with procedure <b>wtextimage</b>.
  The text file written consists of an optional header optionally followed by
  the pixel values.  The pixels are output in FITS order, that is, the
  leftmost subscript varies most rapidly.  The image header is written in the
  <span style="font-family: monospace;">"keyword = value  / comment"</span> format of FITS.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Write a text file from an image section of dev$pix.  The default maximum
  linelength of 80 is used; an output format is specified.  The header portion 
  of the output text is as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  BITPIX  =                    8  /  8-bit ASCII characters
  NAXIS   =                    2  /  Number of Image Dimensions
  NAXIS1  =                   10  /  Length of axis
  NAXIS2  =                   10  /  Length of axis
  ORIGIN  = 'NOAO-IRAF: WTEXTIMAGE'  /
  IRAF-MAX=               31431.  /  Max image pixel (out of date)
  IRAF-MIN=                  33.  /  Min image pixel (out of date)
  IRAF-B/P=                   16  /  Image bits per pixel
  IRAFTYPE= 'SHORT INTEGER     '  /  Image datatype
  OBJECT  = 'NGC 4147 B 1800   '  /
  FILENAME= 'DEV$PIX[1:10,1:10]'  /  IRAF filename
  FORMAT  = '11I7              '  /  Text line format
  DATA-TYP= '    object (  0 )'   / object,dark,comp,etc.
  ITIME   =                 1800  / integration time secs
  UT      = '11:23:13'            / universal time
  ZD      = '24: 5: 0'            / zenith distance
  DATE-OBS= '15/02/1985'          / dd/mm/yy observation
  ST      = '13:38:31'            / sidereal time
  RA      = '12: 9:20'            / right ascension
  DEC     = '18:35:35'            / declination
  EPOCH   =                   .0  / epoch of RA and DEC
  CAM-TEMP=              -104.95  / camera temperature, deg C
  DEW-TEMP=              -192.96  / dewar temp, deg C
  HISTORY1= 'bt=   590 bp=     0 cr=     0 dk=     0 '
  HISTORY2= 'ff=    55 fg=     0 sc=   .000  bi=   51  '
  COMMENT = 'ngc 4147 b 1800'
  F1POS   =                    2  / filter bolt I position
  F2POS   =                    0  / filter bolt II position
  END
  </pre></div>
  <p>
                                                                                  
  2. Write a series of text files from the IRAF images having root name
  <span style="font-family: monospace;">"reduced"</span>.  One text file is written for each image. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wtext reduced.* txt
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  It takes almost 10 cpu minutes to convert a 512 square image of real pixels.
  A 512 square image of integer pixels takes about 3 cpu minutes.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  wcardimage, rtextimage, noao.onedspec.wspectext
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'SEE ALSO'  -->
  

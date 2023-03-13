.. _rtextimage:

rtextimage: Convert text files to IRAF images
=============================================

**Package: dataio**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rtextimage input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>A list of text files containing image pixels and optional header.  Most likely
  the output from <i>rcardimage</i>, see examples below.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output IRAF image name.  If more than one text file is being
  read, the ordinal of the text file in <b>input</b> 
  is appended to <i>output</i> to generate a unique image name.
  </dd>
  </dl>
  <dl id="l_otype">
  <dt><b>otype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='otype' Line='otype = ""' -->
  <dd>The data type of the output IRAF image pixels.  If left unset and the IRAFTYPE
  keyword is found in the FITS header, output pixels will be of type IRAFTYPE.
  If IRAFTYPE appears more than once in the FITS header, the last value of 
  IRAFTYPE is used.  If left unset and the IRAFTYPE keyword is not provided in
  the FITS header, the output data type is determined from the pixels themselves.
  </dd>
  </dl>
  <dl id="l_header">
  <dt><b>header = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='header' Line='header = yes' -->
  <dd>If <b>header</b> = yes, <i>rtextimage</i> will attempt to read a FITS
  header at the beginning of each text file.  
  </dd>
  </dl>
  <dl id="l_pixels">
  <dt><b>pixels = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixels' Line='pixels = yes' -->
  <dd>Read the pixel values from the input text file.  If no then the
  output image is initialized to zero pixel values.
  </dd>
  </dl>
  <dl id="l_nskip">
  <dt><b>nskip = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nskip' Line='nskip = 0' -->
  <dd>The number of lines to skip before reading pixels.  This is used to
  skip over a non-standard header and is important only when <b>header</b> = no.  
  </dd>
  </dl>
  <dl id="l_dim">
  <dt><b>dim = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dim' Line='dim = ""' -->
  <dd>A string listing the dimension of each axis.  The number of dimensions listed
  equals the number of image dimensions.  This information must be entered unless
  it can be read from a FITS header.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Text files are converted to IRAF images files with procedure
  <b>rtextimage</b>.  The text file consists of an optional header optionally
  followed by the pixel values.  If no pixel values are read the image is
  initialized to all zero pixel values.  If pixel values a given they are
  read in FITS order, that is, the leftmost subscript varies most rapidly.
  The number of image dimensions and the length of each dimension must either
  be read from a FITS header or supplied by the user.  Internally,
  <b>rtextimage</b> determines the format (integer or floating point) of the
  pixels in the text file by reading the first one and assuming all others
  are the same.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Read a file written by <i>wtextimage</i> from the magtape file <span style="font-family: monospace;">"mta[1]"</span> into
  the IRAF image <span style="font-family: monospace;">"picture"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt;  rcard mta[1] | rtext out=picture
  </pre></div>
  <p>
  2. Read a series of text files with no headers preceding the pixels.  The 
  text files were previously read from tape with task <b>rcardimage</b>. 
  The two dimensional images are 512 by 320 pixels, and will be named 
  crab001, crab002, crab003, etc.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rtext text.* crab header- dim=512,320
  </pre></div>
  <p>
  3. Read a file with a non-standard header.  The header is 5 cardimages long.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rcard mta[5] | rtext out=spect.1 head- nskip=5 dim=1024
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  Task <i>rtextimage</i> requires about 145 cpu seconds to write a 512 square
  image (integer or real) from a text file.  
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The text file being read cannot have lines longer than SZ_LINE characters
  (see hlib$iraf.h).
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rcardimage, wtextimage
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

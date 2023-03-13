.. _orfits:

orfits: Convert a FITS image into an IRAF image (dataio V2.10.4)
================================================================

**Package: obsolete**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  orfits fits_file file_list iraf_file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_fits_file">
  <dt><b>fits_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fits_file' Line='fits_file' -->
  <dd>The FITS data source.  This is either a template describing a list of disk files
  or a tape file
  specification of the form mt*[n], where mt indicates a mag tape device,
  * represents a density, and [n] is the tape file number.
  If the tape file number n is specified then only that file
  is converted.  If the general tape device name is given, i.e. mta, mtb800, etc,
  then the files specified by the file_list parameter will be read from the tape.
  </dd>
  </dl>
  <dl id="l_file_list">
  <dt><b>file_list</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file_list' Line='file_list' -->
  <dd>The files to be read from a tape are specified by the file_list string.  The
  string can consist of any sequence of file numbers separated by
  at least one of comma, or dash.
  A dash specifies a range of files.  For example the string
  	<span style="font-family: monospace;">"1,2,3-5,8-6"</span>
  will convert the files 1 through 8.
  </dd>
  </dl>
  <dl id="l_iraf_file">
  <dt><b>iraf_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='iraf_file' Line='iraf_file' -->
  <dd>The IRAF file which will receive the FITS data if the make_image parameter
  switch is set.  Iraf_file can be a template of output image names or
  a root output image name. In the former case one output image name
  must be specified for every input file. In the latter case iraf_file is
  a root output image name to which the input file sequence number or tape
  file number is appended if the number of input files &gt; 1. For example
  reading files 1 and 3 from a FITS tape with a value of iraf_file of <span style="font-family: monospace;">"data"</span>
  will produce the files data0001 and data0003, whereas reading the same
  two files with a value of iraf_file of <span style="font-family: monospace;">"data1,data2"</span> will produce the files
  data1 and data2.
  </dd>
  </dl>
  <dl id="l_make_image">
  <dt><b>make_image = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='make_image' Line='make_image = yes' -->
  <dd>This switch determines whether FITS image data is converted to an IRAF image
  file.  This switch is set to no to obtain just header information with the
  long_header or short_header switches.
  </dd>
  </dl>
  <dl id="l_long_header">
  <dt><b>long_header = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='long_header' Line='long_header = no' -->
  <dd>If this switch is set the full FITS header is printed on the standard output.
  </dd>
  </dl>
  <dl id="l_short_header">
  <dt><b>short_header = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='short_header' Line='short_header = yes' -->
  <dd>If this switch is set only the output filename,
  the title string, and the image dimensions are printed.
  </dd>
  </dl>
  <dl id="l_datatype">
  <dt><b>datatype</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datatype' Line='datatype' -->
  <dd>The IRAF image file may be of a different data type than the FITS image data.
  The data type may be specified as s for short, u for unsigned short,
  i for integer, l for long,
  r for real, and d for double.  The user must beware of truncation problems if an
  inappropriate data type is specified.  If an incorrect data_type or a
  null string is given for this parameter then a default data type is used
  which is the appropriate minimum size for the input pixel values.
  If the bscale and bzero parameters in the FITS header are undefined or equal to 
  1.0 and 0.0 respectively, orfits
  selects datatype s or l depending on bitpix. If bscale and bzero are set to
  other than 1.0 and 0.0, orfits selects datatype r.
  </dd>
  </dl>
  <dl id="l_blank">
  <dt><b>blank = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blank' Line='blank = 0.' -->
  <dd>The IRAF image value of a blank pixel.
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = yes' -->
  <dd>If scale equals no the integers are read directly off the tape.
  Otherwise ORFITS checks the values of bscale and bzero. If these numbers
  are not 1. and 0. respectively, ORFITS scales the data before output.
  </dd>
  </dl>
  <dl id="l_oldirafname">
  <dt><b>oldirafname = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='oldirafname' Line='oldirafname = no' -->
  <dd>If the oldirafname switch is set ORFITS will attempt to restore the image to
  disk with the filename defined by the IRAFNAME parameter in the FITS header.
  </dd>
  </dl>
  <dl id="l_offset">
  <dt><b>offset = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='offset' Line='offset = 0' -->
  <dd>Offset is an integer parameter specifying the offset to the current tape file
  number. For example if offset = 100, iraf_file = <span style="font-family: monospace;">"fits"</span> and file_list = <span style="font-family: monospace;">"1-3"</span>
  then the output file names will be <span style="font-family: monospace;">"fits0101"</span>, <span style="font-family: monospace;">"fits0102"</span> and <span style="font-family: monospace;">"fits0103"</span>
  respectively rather than <span style="font-family: monospace;">"fits0001"</span>, <span style="font-family: monospace;">"fits0002"</span> and <span style="font-family: monospace;">"fits0003"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  FITS data is read from the specified source; either disk or
  magnetic tape.  The FITS header may optionally be printed on the standard
  output as either a full listing or a short description.
  The FITS long blocks option is supported. 
  At present non-standard FITS files (SIMPLE = F) and files containing
  group data are skipped and a warning message is issued.
  A warning message will be issued if the default user area allocated in
  memory is too small
  to hold all the FITS parameter cards being read in by ORFITS.
  Since the default user area is 8000
  characters and a single card image is 81 characters long, the normal
  user area will hold 98 complete card images. ORFITS will not permit
  partial cards to be written. The user can override the default user area
  length by setting the environment variable min_lenuserarea (see example
  below).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convert a set of FITS files on tape to a set of IRAF image files, allowing
  orfits to select the output datatype. Blanks are set to zero.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; orfits mtb1600 1-999 images
  </pre></div>
  <p>
  2. Convert a list of FITS files on disk to a set of IRAF images. In the first
  case the files specified by fits* are written to the images images0001,
  images0002, etc. In the second case the fits disk files listed one per
  line in the text file fitslist are written to the output images listed
  one per line in the file imlist.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; orfits fits* * images
  
  cl. orfits @fitslist * @imlist
  </pre></div>
  <p>
  3. List the contents of a FITS tape on the standard output without creating
  any image files.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; orfits mtb1600 1-999 images ma-
  </pre></div>
  <p>
  4. Convert FITS files directly to IRAF images without scaling.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; orfits mtb1600 1-999 images scal-
  </pre></div>
  <p>
  5. Convert the first three FITS files on tape to IRAF files setting blanks
  to -1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; orfits mta 1-3 images blan=-1
  </pre></div>
  <p>
  6. Read in a FITS file with a header roughly twice the usual IRAF length
  of 8000 characters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set min_lenuserarea = 16300
  cl&gt; orfits mta 1 images
  </pre></div>
  <p>
  7. Read a FITS tape with 5 normal fits records (2880 bytes) to a tape record.
  Notice that no extra parameters are needed.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; orfits mta 1-3 fits
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Blank pixels are counted and set to a user determined value,  but not flagged
  in the image header.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  owfits, reblock, t2d
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

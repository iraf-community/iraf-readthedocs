.. _rfits:

rfits: Convert FITS image data into a list of IRAF images
=========================================================

**Package: dataio**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rfits fits_file file_list iraf_file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_fits_file">
  <dt><b>fits_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fits_file' Line='fits_file' -->
  <dd>The FITS data source.  Fits_file is either a list of disk files or a tape
  device specification of the form mt[*][n], where mt is the mag tape
  device (e.g. mta), * is an optional density (e.g. 1600), and [n] is an
  optional tape file number. If n is specified then only image data in the
  nth tape file is read.
  </dd>
  </dl>
  <dl id="l_file_list">
  <dt><b>file_list</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file_list' Line='file_list' -->
  <dd>The list of FITS extensions to be read from each disk file or from a single
  tape file, or the list of tape files AND FITS extensions to be read from
  an entire tape.  FITS extensions are numbered from 0 to n, tape files are
  numbered from 1 to n. If file_list is <span style="font-family: monospace;">""</span>, only the 0th extension is read
  from each disk file or from a single tape file, but all the files and
  extensions are read from an entire tape. Legal file lists are composed
  of a series of file numbers and / or file ranges separated by commas
  or whitespace.  For example the string
  <div class="highlight-default-notranslate"><pre>
  "1-3,4-8"
  </pre></div>
  will convert ALL the FITS extensions in files 1 through 8 on tape,
  but only FITS extensions 1 through 8 from a disk file or a single tape file.
  For the case of disk input, the same FITS extensions must be read from
  each input file.  For the case of tape input the FITS extensions to be
  read from each file must be specified separately. For example the following
  string
  <div class="highlight-default-notranslate"><pre>
  "1-10[2-4],15-21[1-10]"
  </pre></div>
  tells rfits to convert extensions 2 through 4 in tape files 1 through 10
  and extensions 1 through 10 in tape files 15 through 21. Rfits will only
  convert extensions which contain image data. Other types of fits data
  such as tables will not be converted.
  </dd>
  </dl>
  <dl id="l_iraf_file">
  <dt><b>iraf_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='iraf_file' Line='iraf_file' -->
  <dd>The IRAF file which will receive the FITS image data if the make_image parameter
  switch is set.  Iraf_file may be a template of output image names or
  a single root output image name. In the former case one output image name
  must be specified for every input file. In the latter case iraf_file is
  a root output image name to which the input file sequence number or tape
  file number is appended if the number of input files &gt; 1. For example
  reading files 1 and 3 from a FITS tape with a value of iraf_file of <span style="font-family: monospace;">"data"</span>
  will produce the files data0001 and data0003, whereas reading the same
  two files with a value of iraf_file of <span style="font-family: monospace;">"data1,data2"</span> will produce the files
  data1 and data2. Extension numbers will be appended to the root output
  names if appropriate.
  </dd>
  </dl>
  <dl id="l_make_image">
  <dt><b>make_image = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='make_image' Line='make_image = yes' -->
  <dd>If make_images is <span style="font-family: monospace;">"yes"</span> convert the FITS image data to IRAF image data,
  otherwise simply print the header information using the long_header or
  short_header switches.
  </dd>
  </dl>
  <dl id="l_long_header">
  <dt><b>long_header = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='long_header' Line='long_header = no' -->
  <dd>If long_header is <span style="font-family: monospace;">"yes"</span> the full FITS header is printed on the standard output.
  </dd>
  </dl>
  <dl id="l_short_header">
  <dt><b>short_header = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='short_header' Line='short_header = yes' -->
  <dd>If short_header is <span style="font-family: monospace;">"yes"</span> and long_header is <span style="font-family: monospace;">"no"</span>, only the output filename,
  the title string, and the image dimensions are printed on the standard output.
  </dd>
  </dl>
  <dl id="l_datatype">
  <dt><b>datatype</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datatype' Line='datatype' -->
  <dd>The output image data type. Datatype may be s (short integer), i (integer),
  u (unsigned integer), l (long integer), r (real), or d (double).  Data
  truncation may occur if an inappropriate data type is specified. If an
  unsupported data type or a null string is supplied then a default data
  type is selected based on the value of the fits bitpix, bscale, and bzero
  parameters.  If the bscale and bzero parameters in the FITS header are
  undefined or equal to 1.0 and 0.0 respectively, rfits selects datatype
  s or l depending on bitpix. If bscale and bzero are set to 1.0 and 32768.0,
  rfits selects datatype, otherwise rfits selects datatype r.
  </dd>
  </dl>
  <dl id="l_blank">
  <dt><b>blank = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blank' Line='blank = 0.' -->
  <dd>The IRAF image value assigned to a FITS blank pixel.
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = yes' -->
  <dd>If scale is <span style="font-family: monospace;">"no"</span> then the data values are read directly from the FITS image
  without conversion.  Otherwise rfits scales the data before output using
  the values of bscale and bzero.
  </dd>
  </dl>
  <dl id="l_oldirafname">
  <dt><b>oldirafname = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='oldirafname' Line='oldirafname = no' -->
  <dd>If the oldirafname switch is set rfits will attempt to restore the image to
  disk with the filename defined by the IRAFNAME parameter in the FITS header.
  </dd>
  </dl>
  <dl id="l_offset">
  <dt><b>offset = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='offset' Line='offset = 0' -->
  <dd>An integer parameter specifying the offset to the current tape file
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
  </p>
  <p>
  At present non-standard FITS files (SIMPLE = F) and files containing
  group data are skipped and a warning message is issued.
  Image stored in the FITS standard extension IMAGE can be read.
  Other standard extensions such as TABLE and BINTABLE are currently ignored.
  </p>
  <p>
  A warning message will be issued if the default user area allocated in
  memory is too small
  to hold all the FITS parameter cards being read in by RFITS.
  Since the default user area is 64000
  characters and a single card image is 81 characters long, the normal
  user area will hold ~800 complete card images. RFITS will not permit
  partial cards to be written. The user can override the default user area
  length by setting the environment variable min_lenuserarea (see example
  below).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convert all the image data  on a mag tape to individual IRAF
  images. Allow rfits to select the output datatype  and set blanks
  to zero.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rfits mtb1600 "" images
  </pre></div>
  <p>
  or alternatively
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rfits mtb1600 * images
  </pre></div>
  <p>
  2. Convert FITS files on disk to IRAF images. In the first example case the
  files specified by fits* are written to images images0001, images0002, etc.
  In the second example the fits disk files listed one per line in the text
  file fitslist are written to the output images listed one per line in
  the file imlist. Note that by using 0 or <span style="font-family: monospace;">""</span> for the file_list parameter
  the user has told rfits to read only the primary fits data unit.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rfits fits* "" images
  </pre></div>
  <p>
  or alternatively
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rfits fits* 0 images
  
  cl&gt; rfits @fitslist "" @imlist
  </pre></div>
  <p>
  or alternatively
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rfits @fitslist 0 @imlist
  </pre></div>
  <p>
  3. List the contents of a FITS tape on the standard output without creating
  any image files.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rfits mtb1600 "" images ma-
  </pre></div>
  <p>
  4. Convert FITS files on tape directly to IRAF images without scaling.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rfits mtb1600 "" images scal-
  </pre></div>
  <p>
  5. Convert the first three FITS files on tape to IRAF image converting FITS
  blank values to  -1 in the process. Note that the user will not get what
  he or she expects if the output data type is ushort.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rfits mta 1-3 images blank=-1
  </pre></div>
  <p>
  6. Read in a disk FITS file with a header roughly twice the usual IRAF length
  of 64000 characters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; set min_lenuserarea = 128000
  cl&gt; rfits fitsimage "" image
  </pre></div>
  <p>
  7. Read a FITS tape which has 5 normal fits records (2880 bytes) to a tape
  record.  Notice that no hidden rfits parameters are required to do this.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rfits mta * images
  </pre></div>
  <p>
  8. Convert only the zeroth FITS extension in each of the first 100 files on a
  magnetic tape and try to restore the original IRAF image name in the process.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rfits mta 1-100[0] images old+
  </pre></div>
  <p>
  9. Convert the second, third, and fourth FITS extensions in the first 100
  files of a FITS tape and try to restore the original IRAF name in the process.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rfits mta "1-100[2-4]" images old+
  </pre></div>
  <p>
  10. Convert the second, third, and fourth FITS extensions in each of a list of
  disk files and restore the original IRAF name in the process.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rfits @fitslist "2-4" images old+
  </pre></div>
  <p>
  11. Convert the second, third, and fourth FITS extensions in the fifth
  mag tape file and try to restore the original IRAF name in the process.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rfits mta[5] "2-4" images old+
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Blank pixels are counted and set to a user determined value, but they are not
  records in the output image header.
  </p>
  <p>
  Rfits can read image data only. Other FITS data types such as ASCII and
  binary tables are skipped.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  wfits, reblock, t2d, fits kernel
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

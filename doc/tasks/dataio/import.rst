.. _import:

import: Convert some other format to an IRAF image
==================================================

**Package: dataio**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  import binfiles images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_binfiles">
  <dt><b>binfiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='binfiles' Line='binfiles' -->
  <dd>The list of input binary files to be read.
  </dd>
  </dl>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>The list of output IRAF images to be written. This parameter only needs to
  be specified when generating an output image (see the <i>output</i> parameter
  description).
  </dd>
  </dl>
  <dl id="l_format">
  <dt><b>format = <span style="font-family: monospace;">"sense"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='format' Line='format = "sense"' -->
  <dd>The type of format to be processed. In default mode, i.e. <i>sense</i>,
  the format database is searched for a format identifier that evaluates 
  truly for the current binary file, the input file parameters are then
  derived from the database entry.  A specific format name in the database may
  alternatively be given in which case the input params are derived from that
  entry in the database.  If <i>format</i>=<i>none</i> the task parameters
  are used to describe the input file.
  </dd>
  </dl>
  <p style="text-align:center">INPUT PARAMETERS
  
  </p>
  <dl id="l_dims">
  <dt><b>dims = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dims' Line='dims = ""' -->
  <dd>The input file dimension string.  This is a space or comma delimited string
  containing the length of the file in each dimension, e.g. <span style="font-family: monospace;">"512,512,3"</span>.
  </dd>
  </dl>
  <dl id="l_pixtype">
  <dt><b>pixtype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixtype' Line='pixtype = ""' -->
  <dd>Input pixel type. This is a comma delimited string giving the type and size
  of each pixel, and an optional tag name to be used in the <i>outbands</i>
  expressions.  The syntax for the pixtype entry is
  <dl>
  <dt><b> &lt;type&gt;&lt;nbytes&gt;[:tag],&lt;type&gt;&lt;nbytes&gt;[:tag],[....]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line=' &lt;type&gt;&lt;nbytes&gt;[:tag],&lt;type&gt;&lt;nbytes&gt;[:tag],[....]' -->
  <dd>where
  <div class="highlight-default-notranslate"><pre>
  type = b            # byte (no conversions)
         u            # unsigned integer
         i            # signed integer
         r            # ieee floating point
         n            # native floating point
         x            # ignore (skip)
  
  nbytes = 1, 2, 4, or 8
  
  tag is something like <span style="font-family: monospace;">'r'</span>,<span style="font-family: monospace;">'g'</span>,<span style="font-family: monospace;">'b'</span> (color triplets), <span style="font-family: monospace;">'r'</span>,
      <span style="font-family: monospace;">'i'</span> (complex data), etc.  If no tags are given one will
      automatically be assigned of the form 'b1', 'b2', etc.
  </pre></div>
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_interleave">
  <dt><b>interleave = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interleave' Line='interleave = 0' -->
  <dd>Pixel interleave type. If the <i>pixtype</i> parameter is a composite then
  the input pixel are pixel-interleaved (i.e. each pixel in a band is stored
  together, as with RGB triplets) and this parameter is ignored. If 
  the <i>pixtype</i> is an atomic value and <i>interleave</i> is a positive 
  number the image is line interleaved (e.g. a line of <span style="font-family: monospace;">'R'</span>, followed by a 
  line of <span style="font-family: monospace;">'G'</span>, and so on).  If the <i>pixtype</i> is atomic and <i>interleave</i> 
  is zero, the no data interleaving is assumed and each band in the file 
  is stored sequentially.
  </dd>
  </dl>
  <dl id="l_bswap">
  <dt><b>bswap = <span style="font-family: monospace;">"no"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bswap' Line='bswap = "no"' -->
  <dd>Type of byte-swapping to perform.  By default no byte swapping is done, 
  if <i>bswap</i> is <span style="font-family: monospace;">"yes"</span> then all input values are byte swapped, if <i>bswap</i>
  is <span style="font-family: monospace;">"i2"</span> then only short integers are byte swapped, if <i>bswap</i> is <span style="font-family: monospace;">"i4"</span> then
  only long integers are swapped.  A combination of <span style="font-family: monospace;">"i2,i4"</span> can be used to
  swap only integer values, floating point numbers will not be swapped.
  </dd>
  </dl>
  <dl id="l_hskip">
  <dt><b>hskip = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hskip' Line='hskip = 0' -->
  <dd>Number of bytes preceding pixel data to skip.
  </dd>
  </dl>
  <dl id="l_tskip">
  <dt><b>tskip = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tskip' Line='tskip = 0' -->
  <dd>Number of bytes to skip at end of file.
  </dd>
  </dl>
  <dl id="l_bskip">
  <dt><b>bskip = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bskip' Line='bskip = 0' -->
  <dd>Number of bytes between image bands to skip.
  </dd>
  </dl>
  <dl id="l_lskip">
  <dt><b>lskip = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lskip' Line='lskip = 0' -->
  <dd>Number of bytes to skip at font of each line.
  </dd>
  </dl>
  <dl id="l_lpad">
  <dt><b>lpad = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lpad' Line='lpad = 0' -->
  <dd>Number of bytes to skip at end of each line.
  </dd>
  </dl>
  <p style="text-align:center">OUTPUT PARAMETERS
  
  </p>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">"image"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = "image"' -->
  <dd>Type of output to generate.  Possible values include <span style="font-family: monospace;">"none"</span> process the files
  but not generate an output image (e.g. to check the parameter values for
  correctness), <span style="font-family: monospace;">"image"</span> to generate an output image, <span style="font-family: monospace;">"list"</span> to generate a 
  pixel listing of the file as would be produced by the <i>LISTPIX</i> task
  on the image if were converted (no image is created with this option), 
  or <span style="font-family: monospace;">"info"</span> to print information about the file.  The <i>images</i> parameter
  is only used for <i>output</i>=image.
  </dd>
  </dl>
  <dl id="l_outtype">
  <dt><b>outtype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtype' Line='outtype = ""' -->
  <dd>The data type of the output image.  May be one of <span style="font-family: monospace;">'s'</span> for a short image, <span style="font-family: monospace;">'i'</span>
  for an integer image, <span style="font-family: monospace;">'l'</span> for a long image, <span style="font-family: monospace;">'r'</span> for a real image, and <span style="font-family: monospace;">'d'</span>
  for a double precision image.  If no <i>outtype</i> is specified then the
  datatype of the <i>outbands</i> expression is used.  This parameter is only 
  used when <i>output</i> is set to <span style="font-family: monospace;">"image"</span>.
  </dd>
  </dl>
  <dl id="l_outbands">
  <dt><b>outbands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outbands' Line='outbands = ""' -->
  <dd>Output image band expressions.  If no expressions are given then all of the
  input pixels will be converted.  The number of output bands may be more or
  less than the number of input bands.  See the <i>OUTBANDS EXPRESSIONS</i> 
  section for a more complete description of this parameter.
  </dd>
  </dl>
  <dl id="l_imheader">
  <dt><b>imheader = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imheader' Line='imheader = ""' -->
  <dd>Image or header keyword data file.  If an image is given then the image header
  is copied.  If a file is given then the FITS format cards are copied.
  This only applies to new images.   The data file consists of lines
  in FITS format with leading whitespace ignored.  A FITS card must begin
  with an uppercase/numeric keyword.  Lines not beginning with a FITS
  keyword such as comments or lower case are ignored.  The user keyword
  output of <b>imheader</b> is an acceptable data file.  See <b>mkheader</b>
  for further information.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"imcnv$lib/images.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "imcnv$lib/images.dat"' -->
  <dd>The format database. This may also be a list of files to be searched (e.g.
  so that user-defined databases may be included), which will be treated as 
  a single database.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print verbose output during the conversion?
  </dd>
  </dl>
  <dl id="l_buffer_size">
  <dt><b>buffer_size = 64</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='buffer_size' Line='buffer_size = 64' -->
  <dd>Number of image lines <i>per band</i> to buffer in memory before writing to
  disk.  Image buffering can increase task performance by as much as a factor
  of 30 for some formats but requires more memory.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  	The <i>import</i> task is used to convert arbitrary raster binary
  files to IRAF format images.  The input format may be specified either
  through the task parameters (<i>format</i> set to 'none'), or as an entry 
  in a database of known formats (<i>format</i> set to the name of the entry).
  If the format of the image is not known a priori, the database can be
  searched and each record will be evaluated for an expression which
  identifies the format (<i>format</i> set to <span style="font-family: monospace;">"sense"</span>).  The task will 
  output either an IRAF image, a list of pixel values
  in a manner similar to the <i>LISTPIX</i> task, or information about the
  file format if it is supported in the database. 
  </p>
  </section>
  <section id="s_input_file_specification">
  <h3>Input file specification</h3>
  <p>
  	The input raster is assumed to be at most three dimensional, with
  pixels of various sizes that can be interleaved in a variety of ways.
  No compression schemes are yet supported, except in the case of builtin
  formats where special code has been written to handle to format.
  Byte-swapping and floating point conversion of pixels (from IEEE to
  native) is also supported.
  </p>
  <p>
  	The <i>pixtype</i> and <i>interleave</i> parameters define the pixel
  storage in the binary file.  <i>Pixtype</i> is a comma delimited string,
  the elements of which define the type and size of each pixel.  An optional
  'tag' name may be given to each pixel for use in the <i>outbands</i>
  expressions.  If no tag is given one will automatically be assigned.
  For composite pixtypes (i.e. when more than one element is listed), the
  data are assumed to be pixel interleaved (e.g. stored as { {RGB}, {RGB} ...}
  triplets).  For atomic (i.e. single) pixtypes, a positive value of
  <i>interleave</i> indicates that the data are stored in a line-interleaved
  manner (e.g. a line of R, a line of G, ...).  If <i>interleave</i> is
  zero and <i>pixtype</i> is atomic, then no interleaving is done and the 
  image bands are thought to be stored sequentially.  Minimal error
  checking is done to make sure the 
  combination of these parameters is correct.
  </p>
  <p>
  	The file may contain arbitrary padding around the pixels as
  defined by the <i>tskip</i>, <i>bskip</i>, <i>lskip</i>, and <i>lpad</i>
  parameters, header information may be skipped by setting the <i>hskip</i>
  parameter.  Additionally, pixels may be ignored on input while still
  specifying the full format.
  </p>
  </section>
  <section id="s_output_parameters">
  <h3>Output parameters</h3>
  <p>
  	Once a format has been found, the task may output an IRAF image
  by setting <i>output</i> to <span style="font-family: monospace;">"image"</span>, a list of the pixels in the file
  can be written to STDOUT by setting <i>output</i> to <span style="font-family: monospace;">"list"</span>, or information
  about the input file can be printed by setting <i>output</i> to <span style="font-family: monospace;">"info"</span>.
  If <i>output</i> is set to <span style="font-family: monospace;">"none"</span> then no output will be generated, this 
  can be used to check for read errors on the input file to verify task
  parameters.  The datatype of the output image can be set by specifying 
  the <i>outtype</i> parameter.  
  </p>
  <p>
  	The <i>outbands</i> parameter is a list of expressions which are
  evaluated to compute the pixels in each band of the output image.  Operands
  in these expressions consist of numeric constants and the pixtype tags
  (either user-supplied tags or the automatic tags), general arithmetic
  expressions are supported, which can include any of the special functions
  listed below.  The simplest expression is the name of a tag itself.  
  Regardless of the storage of pixels in the input file, each image band is 
  separated on output unless an expression is given which combines them.
  See below for more details on <i>outbands</i>.
  </p>
  <p>
  	Header information may be added to an output image by naming
  either a keyword file or an existing image header listing in the
  <i>imheader</i> parameter.  A header keyword data file consists of lines 
  of FITS format cards.  Leading whitespace is ignored.  Lines not recognized 
  as FITS cards are ignored.  A valid FITS card is defined as beginning with 
  a keyword of up to 8 uppercase, digit, hyphen, or underscore characters.  If
  less than 8 characters the remaining characters are blanks.  The
  ninth character may be an equal sign but must be immediately followed
  by a blank.  Such value cards should be in FITS format though no
  attempt is made to enforce this.  Any other ninth character is also
  acceptable and the line will be treated as a comment.  Note that this
  way of recognizing FITS parameters excludes the case of comments
  in which the first 8 characters are blank.  The reason for allowing
  leading whitespace and eliminating the blank keyword case is so that
  the long output of <b>imheader</b> may be used directly as input.
  </p>
  </section>
  <section id="s_outbands_expressions">
  <h3>Outbands expressions</h3>
  <p>
          The outbands parameter is a comma delimited list of expressions, the 
  simplest of which is the name of a tag itself (or the default names of the 
  tags if none are provided in the <i>pixtype</i> param).  
  The input pixels, regardless of how they are stored in the binary file,
  are always stored as separate bands in the output IRAF image.
  The outbands expressions will be evaluated to compute the pixels in each
  band of the output image.  This means that e.g. RGB triplets in an input
  file will be separated into different bands in the output image, unless a
  single expression is given that combines them.  The components named 
  in <i>pixtype</i> may be eliminated or re-ordered in <i>outbands</i> to 
  exclude certain input bands, or to change the channel order. For example 
  the commands:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; import file img pixtype="u1:a,u1:r,u1:g,u1:b" outbands="g,r,a"
  cl&gt; import file img pixtype="u1,u1,u1,u1" outbands="b3,b2,b1"
  </pre></div>
  <p>
  both convert an input 32-bit image with ARGB components.  In the first case
  the output image is an IRAF image where the B component has been eliminated
  and the channel order reversed.  The second case is the same as the first but
  uses the automatic tag names.  A combination of user-supplied tags and
  defaults could also be used.
  </p>
  <p>
  	General interpreted arithmetic expressions are supported and can 
  contain any of the standard expression evaluator functions (see 
  the <i>imexpr</i> help page for more details).  Special functions in 
  expressions also include:
  </p>
  <div class="highlight-default-notranslate"><pre>
    flipx (arg)        - flip image in X
    flipy (arg)        - flip image in Y
  gr[ea]y (r,g,b)      - RGB to grayscale using the NTSC Y formula
      red (arg)        - get the red component of a colormap image
    green (arg)        - get the green component of a colormap image
     blue (arg)        - get the blue component of a colormap image
    gamma (arg, gamma) - apply a gamma correction to the image
  </pre></div>
  <p>
  The two flip functions can change the image orientation by reversing the order
  of pixels within a line (a flipx() call), or it can flip an image from top-
  to-bottom (a flipy() call).  The flipping will apply to all bands of the out-
  put image even if it was only used in one expression.  To reverse the channel 
  order simply change the order of the tags in the outbands parameter.  RGB
  images may be converted to a single grayscale image using the NTSC formula:
  </p>
  <div class="highlight-default-notranslate"><pre>
  gray = (0.289 * r) + (0.587 * G) + (0.114 * B)
  </pre></div>
  <p>
  Note that a similar grayscale conversion can be done by explicitly defining
  a similar equation in <i>outbands</i> and supplying different coefficients.
  </p>
  <p>
  	The <i>red()</i>, <i>green()</i>, or <i>blue()</i> functions can be used
  to get a single color component from a colormap image rather than the 
  grayscale equivalent of the colormap.  For example, to separate an 8-bit
  GIF color image into it's RGB components one could specify an outbands
  parameter such as
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; import foo.gif bar format=gif outbands="red(b1),green(b1),blue(b1)"
  </pre></div>
  <p>
          Functions may also be nested in complex expressions such as:
  </p>
  <div class="highlight-default-notranslate"><pre>
  flipy (gray(r,g,b))           - convert to grayscale, flip in Y
  flipx (flipy (gray (r,g,b)))  - convert to grayscale, flip in X &amp; Y
   gray (r,g,255)               - use constant 255 as the B band
   gray (r,g+100,-b)            - add constant to G, negate B
  </pre></div>
  </section>
  <section id="s_format_database">
  <h3>Format database</h3>
  <p>
          The format database is a text file named as a task parameter.  
  Each record of a database entry is of the form:
  </p>
  <div class="highlight-default-notranslate"><pre>
  &lt;format_name&gt;:
  &lt;alias&gt;:
          keyword = &lt;expr&gt;
          keyword = &lt;expr&gt;
             ...and so on
  </pre></div>
  <p>
  A database record begins with the format name at the beginning of a line.
  Whitespace at the beginning of a line is considered the continuation of a
  previous line.  Comments may be inserted in the database using the normal <span style="font-family: monospace;">'#'</span>
  character, the remainder of the line is considered a comment.  Blank lines
  and comments are ignored, a record ends at the next line with a format name
  at the beginning of the line.  The task <i>database</i> parameter 
  defines the text files to be
  scanned as the database.  If the parameter is a list of files then each file
  in the list will be concatenated to a single database file used by the task.
  </p>
  <p>
          The format_name field is a string identifying each entry in the
  database, any number of aliases may also be given to identify the same 
  format possibly known by another name. Supported keywords include:
  </p>
  <div class="highlight-default-notranslate"><pre>
  image_id     - A boolean expression identifying the image type
  id_string    - Verbose name of file format
  bswap        - is file byte-swapped? (See Below)
  dims         - a whitespace/comma delimited string of dimensions
  pixtype      - pixel type, size [and tag], may be a composite
  interleave   - describes how pixels are stored
  hskip        - # of bytes of header info to skip
  tskip        - # of bytes of trailing info to skip at end of file
  bskip        - # of bytes of info to skip between image bands
  lskip        - # of bytes of info to skip at front of each line
  lpad         - # of bytes of info to skip at end of each line
  error        - A condition that would cause a file read error,
                 returns a string with the error message, otherwise
                 returns the string "okay"
  </pre></div>
  <p>
  The 'image_id' string is an expression to be evaluated which, if true,
  uniquely identifies the file format (such as a comparison to a <span style="font-family: monospace;">"magic number"</span>).
  The 'id_string' is a verbose name of the format.  
  The 'error' keywords use the <span style="font-family: monospace;">"? :"</span> conditional syntax to
  define a boolean expression which, when true, returns an error message and is 
  used to indicate a condition in a format which isn't supported.  The remaining
  keywords have the same meaning as the task parameters.  Keywords not present 
  in the database record will take the default parameter value.
  </p>
  <p>
          Expressions consist of any valid string that may be evaluated with the
  standard system expression evaluator evvexpr(). (See the documentation for this
  procedure or the <i>IMEXPR</i> task help page for details of builtin functions 
  and operators.)  Operators within expressions may be boolean, arithmetic,
  or the string operators '?=' (substring equality) and '//' (concatenation).
  Operands may be the special functions named below, previously defined
  keywords, constants (numeric or strings), and the special operands 
  </p>
  <dl>
  <dt><b>$FSIZE </b></dt>
  <!-- Sec='FORMAT DATABASE' Level=0 Label='' Line='$FSIZE ' -->
  <dd>The size of the binary file in bytes.   In expressions this operand has an
  integer datatype.  For formats with variable header sizes this can be used
  to determine the size of the header, since the size of the data can be 
  derived from the image dimensions and subtracted from the total size of the
  file.
  </dd>
  </dl>
  <dl>
  <dt><b>$FNAME</b></dt>
  <!-- Sec='FORMAT DATABASE' Level=0 Label='' Line='$FNAME' -->
  <dd>The name of the binary file.  In expressions this operand has a character
  datatype.  As a last resort for images without any identifying features the
  file name may possibly be used to determine the format from a file name
  extension.
  </dd>
  </dl>
  </section>
  <section id="s_special_functions_">
  <h3>Special functions:</h3>
  <p>
          In addition to the intrinsic functions already provided there are a
  number of input and utility functions for the database.  These are:
  </p>
  <div class="highlight-default-notranslate"><pre>
                       <i>INPUT FUNCTIONS</i>
  
     ctocc ([offset])      - convert byte to printable char constant
      ctod ([offset])      - convert string to double precision real
      ctoi ([offset])      - convert string to integer
      ctol ([offset])      - convert string to long
      ctor ([offset])      - convert string to single precision real
    ctowrd ([offset])      - get 1st white-space delimited word from str
  
    getstr ([offset,] len) - get a string at offset
      getb ([offset])      - get a byte at offset
      getu ([offset])      - get an unsigned short int at offset
  geti[24] ([offset])      - get a signed int at offset
  getr[48] ([offset])      - get an IEEE fp number at offset
  getn[48] ([offset])      - get a native fp number at offset
  
    locate ([offset,] pat) - find an offset to a pattern
      line (n)             - offset of line N
  
                       <i>UTILITY FUNCTIONS</i>
  
       skip (nbytes)       - move offset by N-bytes
      bswap (arg)          - byte swap the argument
     substr (str, c1, c2)  - extract a substring from argument
     stridx (test, str)    - get 1st occurrence of 'test' w/in 'str'
  
  parameter (param)        - return the current task parameter
    default (param)        - return the default task parameter
   lsb_host ()             - returns true if host is little-endian
   msb_host ()             - returns true if host is big-endian
  </pre></div>
  <dl id="l_ctocc">
  <dt><b>ctocc ([offset])			[string]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='ctocc' Line='ctocc ([offset])			[string]' -->
  <dd>Convert byte at the given offset to printable char constant.
  If no offset argument is given the current offset is used.
  </dd>
  </dl>
  <dl id="l_ctod">
  <dt><b>ctod ([offset])			[double]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='ctod' Line='ctod ([offset])			[double]' -->
  <dd>Convert string to double precision real.
  The function reads a string from
  the file and converts it up to the first unrecognized character.
  If no offset argument is given the current offset is used.
  </dd>
  </dl>
  <dl id="l_ctoi">
  <dt><b>ctoi ([offset])			[int]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='ctoi' Line='ctoi ([offset])			[int]' -->
  <dd>Convert string to integer.
  The function reads a string from
  the file and converts it up to the first unrecognized character.
  If no offset argument is given the current offset is used.
  </dd>
  </dl>
  <dl id="l_ctol">
  <dt><b>ctol ([offset])			[long]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='ctol' Line='ctol ([offset])			[long]' -->
  <dd>Convert string to long.
  The function reads a string from
  the file and converts it up to the first unrecognized character.
  If no offset argument is given the current offset is used.
  </dd>
  </dl>
  <dl id="l_ctor">
  <dt><b>ctor ([offset])			[real]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='ctor' Line='ctor ([offset])			[real]' -->
  <dd>Convert string to single precision real.  
  The function reads a string from
  the file and converts it up to the first unrecognized character.
  If no offset argument is given the current offset is used.
  </dd>
  </dl>
  <dl id="l_ctowrd">
  <dt><b>ctowrd ([offset])			[string]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='ctowrd' Line='ctowrd ([offset])			[string]' -->
  <dd>Get 1st white-space delimited word from str, leading whitespace is skipped.
  If no offset argument is given the current offset is used.
  </dd>
  </dl>
  <dl id="l_getstr">
  <dt><b>getstr ([offset,] len)		[string]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='getstr' Line='getstr ([offset,] len)		[string]' -->
  <dd>Get a string at offset.
  If no offset argument is given the current offset is used, the length of
  the string must be specified.
  </dd>
  </dl>
  <dl id="l_getb">
  <dt><b>getb ([offset])			[int]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='getb' Line='getb ([offset])			[int]' -->
  <dd>Get a byte at offset.
  If no offset argument is given the current offset is used.
  </dd>
  </dl>
  <dl id="l_getu">
  <dt><b>getu ([offset])			[int]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='getu' Line='getu ([offset])			[int]' -->
  <dd>Get an unsigned short integer at offset.
  If no offset argument is given the current offset is used.
  </dd>
  </dl>
  <dl id="l_geti">
  <dt><b>geti[24] ([offset])			[int]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='geti' Line='geti[24] ([offset])			[int]' -->
  <dd>Get a signed int at offset.
  If no offset argument is given the current offset is used.
  Long integers values can be read by specifying the function as geti4(),
  the names geti() and geti2() return short integers.
  </dd>
  </dl>
  <dl id="l_getr">
  <dt><b>getr[48] ([offset])			[real/double]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='getr' Line='getr[48] ([offset])			[real/double]' -->
  <dd>Get an IEEE floating point number at an optional offset.
  If no offset argument is given the current offset is used.
  Double precision values can be read by specifying the function as getr8(),
  the names getr() and getr4() return single precision real.
  </dd>
  </dl>
  <dl id="l_getn">
  <dt><b>getn[48] ([offset])			[real/double]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='getn' Line='getn[48] ([offset])			[real/double]' -->
  <dd>Get a native floating point number at an optional offset.
  If no offset argument is given the current offset is used.
  Double precision values can be read by specifying the function as getn8(),
  the names getn() and getn4() return single precision real.
  </dd>
  </dl>
  <dl id="l_locate">
  <dt><b>locate ([offset,] pat)		[int]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='locate' Line='locate ([offset,] pat)		[int]' -->
  <dd>Compute an offset.
  If no offset argument is given the current offset is used.
  </dd>
  </dl>
  <dl id="l_line">
  <dt><b>line (N)				[int]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='line' Line='line (N)				[int]' -->
  <dd>Offset of line N in bytes.  The database is rewound and the offset of the
  requested line number is returned, line are delimited by the '\n' character.
  </dd>
  </dl>
  <dl id="l_skip">
  <dt><b>skip (nbytes)			[int]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='skip' Line='skip (nbytes)			[int]' -->
  <dd>Move current offset by N-bytes. The number of bytes skipped is returned as
  the function value.
  </dd>
  </dl>
  <dl id="l_bswap">
  <dt><b>bswap (arg)				[type of arg]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='bswap' Line='bswap (arg)				[type of arg]' -->
  <dd>Byte swap the argument.
  </dd>
  </dl>
  <dl id="l_substr">
  <dt><b>substr (str, first, last)		[string]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='substr' Line='substr (str, first, last)		[string]' -->
  <dd>Extracts a substring from string <i>str</i>.  The  first  character  in
  the string is at index 1.
  </dd>
  </dl>
  <dl id="l_stridx">
  <dt><b>stridx (test, str)			[int]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='stridx' Line='stridx (test, str)			[int]' -->
  <dd>Finds the position of the first occurrence of any character found
  in <i>test</i> in the string <i>str</i>, returning 0 if the match fails.
  </dd>
  </dl>
  <dl id="l_parameter">
  <dt><b>parameter (param)			[param type]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='parameter' Line='parameter (param)			[param type]' -->
  <dd>Return the current task parameter. The parameter is specified as a string
  containing the name of a task parameter, the type of the returned value is
  the parameter type 
  </dd>
  </dl>
  <dl id="l_default">
  <dt><b>default (param)			[param type]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='default' Line='default (param)			[param type]' -->
  <dd>Return the default task parameter.  The parameter is specified as a string
  containing the name of a task parameter, the type of the returned value is
  the parameter type 
  </dd>
  </dl>
  <dl id="l_lsb_host">
  <dt><b>lsb_host ()				[bool]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='lsb_host' Line='lsb_host ()				[bool]' -->
  <dd>Returns true if host is little-endian.
  This function can be used as the <i>bswap</i> keyword expression for formats
  with a specified byte order.
  </dd>
  </dl>
  <dl id="l_msb_host">
  <dt><b>msb_host ()				[bool]</b></dt>
  <!-- Sec='Special Functions:' Level=0 Label='msb_host' Line='msb_host ()				[bool]' -->
  <dd>Returns true if host is big-endian.
  This function can be used as the <i>bswap</i> keyword expression for formats
  with a specified byte order.
  </dd>
  </dl>
  </section>
  <section id="s_byte_swapping">
  <h3>Byte swapping</h3>
  <p>
  	The 'bswap' database entry is similar to the task parameter,  it may
  be used to set byte swapping for the whole file, or for only certain data
  types.  The value is a string parameter that may be <span style="font-family: monospace;">"yes"</span> to byteswap the
  whole file, <span style="font-family: monospace;">"no"</span> to not swap anything, or a comma delimited string of types
  described below to enable swapping for only those values.
  </p>
  <div class="highlight-default-notranslate"><pre>
  bswap = { no | yes | i2 i4 }
  
          no              # no swapping (default)
          yes             # byte swap whole file
          i2              # byte swap short ints only
          i4              # byte swap long ints only
  </pre></div>
  <p>
  	The <i>bswap</i> task parameter applies only to the pixel data,
  but the bswap keyword in a database record sets byte-swapping 
  for the header information:  arguments to the input and conversion functions
  will be byteswapped prior to being evaluated by the function.  The bswap()
  special function can be used to negate byteswapping for a particular 
  argument if it is or is not set by the keyword (the default is no byte 
  swapping).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  Get a list of known input formats:
  
      cl&gt; import "" "" output=info
  
  Get a list of known input formats, including those defined by the user:
  
      cl&gt; import "" "" output=info database="dev$images.dat,mydb.dat"
  
  Get a list of the file formats of each image in the directory:
  
      cl&gt; import file* "" format="sense" output=info verbose-
      file1.ras               Sun rasterfile
      file1.eps               unknown format
      file1.pgm               8-bit PGM file
          :                           :
  
  Get a list of the file formats of each image in the directory and
  print out some information about each file:
  
      cl&gt; import file* "" format="sense" output=info verbose+
      file1.ras:         Sun Rasterfile
                         Resolution:       320 x 200
                         Pixel type:       8-bit unsigned integer
                         Pixel storage:    non-interleaved
                         Header length:    137 bytes
                         Byte swapped:     no
       ...                    :
  
  Read a raw 8-bit file of pixels into an unsigned short IRAF image:
  
      cl&gt; import file img format="none" dims="512,512" pixtype="b1" \
      &gt;&gt;&gt;     outtype="u" outbands="b1"
  
  Read a JPL VICAR image or 8-bit Sun rasterfile:
  
      cl&gt; import file img format="vicar"
      cl&gt; import file img format="sunras"
  
  Concatenate three separate red, blue, and green images and convert
     to a single grayscale image:
  
      cl&gt; concat pic.[rgb] &gt; rgb
      cl&gt; import rgb img format=none dims="640,480,3" \
      &gt;&gt;&gt;    pixtype="u1" interleave=0 outbands="gray(b1,b2,b3)"
  
  Read an 8-bit colormap GIF image and separate the RGB colors into
     separate bands in the output image:
  
      cl&gt; import file.gif img outbands="red(b1),green(b1),blue(b1)"
  
  Read three 8-bit rasterfiles with 200 byte-headers as if they were
      a single image, and combine the images to a single output band:
  
      cl&gt; concat pix.* &gt; rfiles
      cl&gt; import rfiles img dims="512,512,3" pixtype="b1" \
      &gt;&gt;&gt; hskip=200 bskip=200 interleave=0 outbands="gray(b1,b2,b3)"
  
  Read a FITS image with one header record in which the data bytes
     are incorrectly swapped, but the header info is in the right order:
  
      cl&gt; rfits nite1.fits "" nite1
         File: nite1  1866-A                Size = 640x480
      cl&gt; imheader nite1 l+ &gt; imheader.dat    # Save the header info
      cl&gt; imdel nite1.imh
      cl&gt; import nite1.fits nite1 format="none" dims="640,480" \
      &gt;&gt;&gt; bswap+ hskip=2880 pixtype="i2" outtype="s" imheader="imheader.dat"
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Bitmap images are not yet supported.  Their most logical use would be as
  pixel masks but there hasn't been much call for these formats so they may
  be implemented at a later time.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_IMPORT">
  <dt><b>IMPORT V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IMPORT' Line='IMPORT V2.11' -->
  <dd>This is a new task in this version.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  export. imexpr, hedit, default image database imcnv$lib/images.dat
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'Input File Specification' 'Output Parameters' 'OUTBANDS EXPRESSIONS' 'FORMAT DATABASE' 'Special Functions:' 'BYTE SWAPPING' 'EXAMPLES' 'BUGS' 'REVISIONS' 'SEE ALSO'  -->
  

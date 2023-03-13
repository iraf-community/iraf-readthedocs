.. _export:

export: Convert IRAF images to some other format
================================================

**Package: dataio**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  export images binfiles
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>The list of input IRAF images to be converted.  The list may contain
  either 2-D images  or 3-D images.
  Any number of 2-D images may be combined to a single output file, only
  one 3-D image (or section) at a time may be converted.  See the <i>Builtin 
  Formats</i> section for notes about the number of image expressions required 
  for each builtin format and the handling of 3-D image data.  Images greater
  than three dimensions should be converted using image sections.
  </dd>
  </dl>
  <dl id="l_binfiles">
  <dt><b>binfiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='binfiles' Line='binfiles' -->
  <dd>The list of output binary files to create.  If any of the builtin formats
  is selected for conversion the filename will have an extension added
  reflecting the format (if it is not already given).
  </dd>
  </dl>
  <p style="text-align:center">OUTPUT PARAMETERS
  
  </p>
  <dl id="l_format">
  <dt><b>format = <span style="font-family: monospace;">"raw"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='format' Line='format = "raw"' -->
  <dd>The type of binary file to write.  If the value is <span style="font-family: monospace;">"raw"</span> then the input
  images are converted directly to a raw binary raster using the task 
  parameters.  If the value is <span style="font-family: monospace;">"list"</span> the pixel values will be written
  to the standard output after evaluation of the <i>outbands</i> parameter in
  the same format as would appear from the <i>LISTPIX</i> task.  Finally,
  the value may include any of the currently supported specific builtin formats:
  <div class="highlight-default-notranslate"><pre>
  eps             - Encapsulated PostScript
  gif             - Compuserve's GIF format
  imh             - IRAF OIF image
  miff            - ImageMagick MIFF format image
  pgm             - PBMPlus PGM format image
  ppm             - PBMPlus PPM format image
  ras             - Sun rasterfile format
  rgb             - SGI RGB format image
  xwd             - X11 Window dump file
  </pre></div>
  If any of these builtin formats is selected one or more of the following 
  parameters may be ignored. See the <i>Builtin Formats</i> section for notes 
  about the formats supported by this task.
  </dd>
  </dl>
  <dl id="l_outbands">
  <dt><b>outbands = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outbands' Line='outbands = ""' -->
  <dd>Output image band expressions to write.  This is a comma-delimited list of 
  expressions or an @-file containing the expressions.  Evaluated expressions 
  do not all need to be the same length since the output image will be padded
  to the maximum size.  See below for more information.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no                    </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no                    ' -->
  <dd>Print verbose output to the screen during conversion?
  </dd>
  </dl>
  <p style="text-align:center">RAW BINARY OUTPUT PARAMETERS
  
  </p>
  <dl id="l_header">
  <dt><b>header = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='header' Line='header = yes' -->
  <dd>For raw binary file output only, prepend a header describing how the data 
  are stored?  If set to <span style="font-family: monospace;">"no"</span> then no header will be written.  If set to <span style="font-family: monospace;">"yes"</span>, 
  a standard text header describing how the data were written will be 
  prepended to the output file.  Setting the <i>header</i> parameter to the 
  reserved string <span style="font-family: monospace;">"long"</span> will write the image headers from the IRAF images
  making up the output file in the standard header.  The parameter may also
  be set to a filename that will be prepended to the output file.  This
  parameter is ignored for builtin format output. See below for a description 
  of the header layout.
  </dd>
  </dl>
  <dl id="l_outtype">
  <dt><b>outtype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtype' Line='outtype = ""' -->
  <dd>Output pixel type if <i>format</i> is set to <span style="font-family: monospace;">"raw"</span> or <span style="font-family: monospace;">"list"</span>.  This is a 
  string giving the type and size of each pixel, the syntax for the outtype 
  entry is
  <div class="highlight-default-notranslate"><pre>
                  &lt;type&gt;[&lt;nbytes&gt;]
  where
      type = b            # byte
             u            # unsigned (short) integer
             i            # signed integer
             r            # ieee floating point
             n            # native floating point
  
      nbytes = 1, 2, 4, or 8
  </pre></div>
  If no value for <i>nbytes</i> is given the smallest size for the given type
  (i.e. 1 byte for <span style="font-family: monospace;">'b'</span>, 2 bytes for ints, 4 bytes for floating point) will
  be used.  If no value is entered at all the type of the input image is used, 
  for multiple images used to create a single binary file the type of the first 
  image is used.  This parameter is ignored for builtin format output options.
  </dd>
  </dl>
  <dl id="l_interleave">
  <dt><b>interleave = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interleave' Line='interleave = 0' -->
  <dd>Pixel interleave type.  If the <i>outbands</i> parameter is composite 
  (i.e. a comma-delimited list of expressions) the output file is pixel 
  interleaved and the <i>interleave</i> parameter is ignored.  If the 
  <i>outbands</i> parameter is a single expression the file is line-interleaved 
  when the <i>interleave</i> value is a positive integer.  If the <i>outbands</i> 
  is an empty string or a single expression the binary file is band interleaved 
  if this parameter is zero.  This parameter is ignored for builtin formats 
  where the pixel storage is predefined.
  </dd>
  </dl>
  <dl id="l_bswap">
  <dt><b>bswap = <span style="font-family: monospace;">"no"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bswap' Line='bswap = "no"' -->
  <dd>Type of byte-swapping to perform on output. The default is bswap=no which
  may be abbreviated <span style="font-family: monospace;">"bswap-"</span> (similarly a value of 'yes' can be abbreviated
  <span style="font-family: monospace;">"bswap+"</span>).  If disabled no byte-swapping is performed, if set all integers
  are swapped on output relative to the current machine's byte ordering.
  Values of 'i2' or 'i4' will swap only two or four byte integers respectively,
  floating point values remain unswapped.  This parameter may be used by some
  builtin formats that don't have a specified byte order.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  	The <i>export</i> task will convert one or more images in an
  input list to a binary raster file, a text listing of pixels values,
  or one of several specific file formats.  For general binary
  rasters, various pixel types, data interleaving, and the byte order can be
  specified.  An optional header may be added to the output file.
  Arbitrary arithmetic expressions, using both standard and custom
  functions, may be applied to the images in the
  input list before conversion allowing the user to scale intensity values,
  change image orientation, compute colormaps, or compute output pixel
  values.
  </p>
  <p>
  	The <i>format</i> parameter controls the type of output generated:
  if set to <i>raw</i> a binary file described by the <i>outtype</i>, 
  <i>interleave</i>, and <i>bswap</i> parameters is written with pixel values
  determined from the expressions in the 
  <i>outbands</i> parameter.  The value of <i>outtype</i>
  defines the output pixel size and type (long or short ints, native or IEEE
  reals, see parameter description for details).  The
  <i>bswap</i> parameter can be used to set the byte order (relative to the
  current machine) of integer values, this 
  parameter is ignored for floating point pixels or builtin
  formats with a specified byte order. The <i>outbands</i> and <i>interleave</i> 
  parameters define the pixel storage in the binary file.  For multiple 
  <i>outbands</i>
  expressions the data are assumed to be pixel interleaved (e.g. written 
  as { {RGB}, {RGB} ...} triplets).  For single expressions, a positive value 
  of <i>interleave</i> indicates that the data are written in a line-interleaved
  manner (e.g. a line of R, a line of G, ...).  If <i>interleave</i> is
  zero and <i>outbands</i> is a single expression 
  then no interleaving is done and the image bands are written sequentially.  
  If <i>outbands</i> is the null string, all pixels in a single input image 
  will be written to a single output file.
  Error checking is done to make sure the combination of these 
  parameters is correct.  If the <i>header</i> parameter is <span style="font-family: monospace;">"yes"</span> a text header
  describing how the data were written will be prepended to the file, setting
  the <i>header</i> parameter to the reserved string <span style="font-family: monospace;">"long"</span>
  will cause the image header for each input image
  to be saved in the standard header.  The <i>header</i> parameter may also 
  be the name of a user-defined file to prepend to the output instead of the
  standard header.
  </p>
  <p>
  	If the <i>format</i> parameter is set to <span style="font-family: monospace;">"list"</span> the pixels values 
  will be written to the screen as an ascii list of pixel coordinates 
  followed by the pixel value.   Pixel coordinates are determined using the
  same interleaving scheme as above, values are determined by evaluating
  each <i>outbands</i> expression.
  </p>
  <p>
  	Lastly, the <i>format</i> parameter may be any of the currently
  supported builtin formats.  See the section on <i>Builtin Formats</i> for
  more information and the restrictions or requirements of each format.
  </p>
  </section>
  <section id="s_more_on_outbands_expressions">
  <h3>More on outbands expressions</h3>
  <p>
  	The simplest specification for <i>outbands</i> is a null string, 
  in which case the image is converted directly (i.e. band storage, 
  pixels converted to output type).  Arbitrary interpreted arithmetic 
  expressions using standard and custom functions and operators are also 
  supported.  If the <i>images</i> parameter is a list of 3-D images the 
  operand names are the predefined tags b1, b2, ... bN for the bands in each 
  image, the <i>binfiles</i> parameter must contain an equal number of 
  output files.  To convert multiple 3-D images they must either be sliced 
  to individual 2-D images (or specified as image sections) or stacked into 
  a single image.  If the <i>images</i> parameter is a list of 2-D images 
  (or sections) the operand names are the predefined tags i1, i2, ... iN for 
  the each image in the input list, the b1, b2, etc names are also recognized.
  For more complex or 
  lengthy expressions the <i>outbands</i> parameter may alternatively be an
  @-file containing the expressions.  Within this @-file whitespace and
  newline characters are ignored to allow expressions to be indented in a 
  readable manner.
  </p>
  <p>
  	The image operands determine which input images in the list are
  converted to which output files.  For 3-D input images one IRAF image is
  converted for each output file in the list, for 2-D images multiple images
  may be converted to a single output file.  In the latter case the list 
  pointers are updated automatically to keep track of the images.  For example,
  to convert six images to two output files, the <i>outbands</i> expression
  should contain three images operands.  The first three images in the list
  will be used in evaluating the expressions for the first output file,
  the last three for the second file.
  </p>
  <p>
  	The image tags may be reordered in the expression but still refer to 
  e.g. band-1, band-2 and so on.  For example (where rgbim is a 512x512x3 image, 
  and rim, gim, and bim are 512x512 images),
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export rgbim file outtype="u2" header-                       (1)
  cl&gt; export rgbim file outtype="u2" header- outbands="b3,b2,b1"   (2)
  cl&gt; export rim,gim,bim file outty="u2" outbands="i3,i2,i1"       (3)
  cl&gt; export rim,gim,bim file outty="b" outbands="gray(i1,i2,i3)"  (4)
  </pre></div>
  <p>
  Example (1) converts the input image pixels to a raw binary file of 
  unsigned short integers with no header written as one image band following 
  another.  In example (2) the order of the bands is reversed and the binary 
  file is stored as pixel interleaved BGR triplets of short ints.  
  Example (3) is the same as (2) except that the input images in the list 
  are reordered instead of bands within a single image. When using the image 
  tags the input list is updated to account for this, so it is allowed to have 
  more input images than output binary files.
  In example (4) the three images are converted to a single grayscale image
  before being written as byte data to the binary file.
  More complex and detailed examples are given below.
  </p>
  <p>
  Individual <i>outbands</i> expressions are composed of operators and operands
  in general interpreted arithmetic expressions as follows:
  </p>
  <p>
  <b>Operands</b>
  </p>
  <div class="highlight-default-notranslate"><pre>
  iN                          # image list item
  iN.param                    # image parameter
  @"param"                    # parameter of 3-D image
  bN                          # band within 3-D image
  
  func()                      # function
  constant                    # numeric constant
  </pre></div>
  <p>
      The 'iN.param' and '@<span style="font-family: monospace;">"param"</span>' syntax allows an image header parameter 
  to be accessed.  For example 'i2.otime' refers to the 'otime' image 
  header parameter in the second image of a list and '@<span style="font-family: monospace;">"otime"</span>' refers to the 
  current image if the input list contains 3-D images.  They may
  be used in an outbands expression such as
  </p>
  <div class="highlight-default-notranslate"><pre>
  (i1*(i1.otime/i2.otime)),i2,(i3*(i3.otime/i2.otime))        (1)
  (b1/@"otime")),(b2/@"otime"),(b3/@"otime")                  (2)
  </pre></div>
  <p>
  to normalize the output bands by the exposure time value in the second image
  in the first example, or to normalize by the 'otime' keyword of a 3-D image
  in the second example.
  </p>
  <p>
      In cases where a constant value is used as an outbands expression an 
  alpha channel (an extra 8-bits of constant intensity) will be created 
  consisting of that value.  For example, writing a 32-bit RGB image with an 
  alpha channel of 255 could be written using
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export rgbim file outtype="b1" outbands="b1,b2,b3,255"
  </pre></div>
  <p>
  <b>Operators</b>
  </p>
  <p>
  The expression syntax implemented by <i>export</i> provides the following
  set of operators:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ( expr )                    - grouping
  + - * /                     - arithmetic
  **                          - exponentiation
  //                          - concatenate
  expr ? expr1 : expr2        - conditional expression
  
  &amp;&amp;                          - logical and
  ||                          - logical or
  !                           - logical not
  &lt;                           - less than
  &lt;=                          - less than or equal
  &gt;                           - greater than
  &gt;=                          - greater than or equal
  ==                          - equals
  !=                          - not equals
  ?=                          - substring equals
  </pre></div>
  <p>
  The conditional expression has the value <i>expr1</i> if <i>expr</i> is true,
  and <i>expr2</i> otherwise.  Since the expression is evaluated at every pixel
  this permits pixel-dependent operations such as checking for special pixel
  values, or selection of elements from either of two vectors.  For example,
  the command
  </p>
  <p>
          	(i1 &lt;= 0) ? 0 : 1
  </p>
  <p>
  has the constant value zero if <span style="font-family: monospace;">"i1"</span> is less than or equal to zero, 
  and one otherwise, effectively creating a pixel mask of positive pixels.
  Conditional expressions are general expressions and may be nested or used
  anywhere an expression is permitted.
  </p>
  <p>
  The concatenation operator applies to all types of data, not just
  strings.  Concatenating two vectors results in a vector the 
  combined length of the two input vectors.  An example use of this would
  be to concatenate images side-by-side on output.
  </p>
  <p>
  <b>Special Functions</b>
  </p>
  <p>
  	In addition to the intrinsic functions already provided (see the help
  page for the <i>imexpr</i> task for a list of standard, mathematical and type
  conversion functions) there are a number of custom functions for this task:
  </p>
  <p style="text-align:center"><b>Output Functions:</b>
  
  </p>
  <div class="highlight-default-notranslate"><pre>
   band (args)                - force band interleaved storage
   line (args)                - force line interleaved storage
  flipx (args)                - flip image in X dimension
  flipy (args)                - flip image in Y dimension
  
  block (val,width,height)    - block fill area with a constant
  </pre></div>
  <p>
      These functions define how the output data are written. For builtin 
  formats whose normal orientation and storage format is known these functions 
  are ignored (except where noted).  These functions may not be used as arguments to other functions (except where noted) or as single operands
  within expressions (e.g. <span style="font-family: monospace;">"255 + flipx(i1)"</span>), however their arguments may
  be expressions or (perhaps output) functions themselves.
  </p>
  <dl id="l_band">
  <dt><b>band (args)</b></dt>
  <!-- Sec='MORE ON OUTBANDS EXPRESSIONS' Level=0 Label='band' Line='band (args)' -->
  <dd>Force band storage in the output file regardless of the value of the
  <i>interleave</i> parameter.  This may be used to specify multiple
  expressions for each band while still forcing band storage (the default
  for multiple expressions is pixel-interleaved storage).  This function
  may be used with some builtin formats to write multiple images to the output
  file as if they were a column of images in the original. This function
  is ignored by builtin formats that do not support this scheme (i.e RGB
  format) and may be used as an argument to the <i>setcmap()</i>, <i>psdpi()</i>,
  and <i>psscale()</i> functions only.
  </dd>
  </dl>
  <dl id="l_line">
  <dt><b>line (args)</b></dt>
  <!-- Sec='MORE ON OUTBANDS EXPRESSIONS' Level=0 Label='line' Line='line (args)' -->
  <dd>Force line storage in the output file regardless of the value of the
  <i>interleave</i> parameter.  This may be used to specify multiple
  expressions for each band while still forcing line storage (the default
  for multiple expressions is pixel-interleaved storage).  This function
  is ignored by builtin formats that do not support this scheme.
  </dd>
  </dl>
  <dl id="l_flipx">
  <dt><b>flipx (args)</b></dt>
  <!-- Sec='MORE ON OUTBANDS EXPRESSIONS' Level=0 Label='flipx' Line='flipx (args)' -->
  <dd>Flip the image left-to-right on output.  This function may be used as an
  argument to the <i>band()</i>, <i>setcmap()</i>, <i>psdpi()</i>, or 
  <i>psscale()</i> functions only.
  </dd>
  </dl>
  <dl id="l_flipy">
  <dt><b>flipy (args)</b></dt>
  <!-- Sec='MORE ON OUTBANDS EXPRESSIONS' Level=0 Label='flipy' Line='flipy (args)' -->
  <dd>Flip the image top-to-bottom on output.  Certain builtin formats (such as
  GIF, PGM, PPM, RAS and XWD) have their normal orientation already flipped wrt 
  to IRAF and these will automatically be flipped on output.  Using this
  function with those formats cancels the flip action, writing the image in the
  normal IRAF orientation and not the normal format orientation.
  This function may be used as an argument to the <i>band()</i>, <i>setcmap()</i>,
  <i>psdpi()</i>, or <i>psscale()</i> functions only.
  </dd>
  </dl>
  <dl id="l_block">
  <dt><b>block (value, width, height)</b></dt>
  <!-- Sec='MORE ON OUTBANDS EXPRESSIONS' Level=0 Label='block' Line='block (value, width, height)' -->
  <dd>Fill an area with a constant value.  This function can be used to fill a
  vertical area between images to provide padding of a constant value.  It
  is similar to the <span style="font-family: monospace;">"repl()"</span> intrinsic function which replicates a data element
  a given number of times.
  </dd>
  </dl>
  <p style="text-align:center"><b>Scaling Functions:</b>
  
  </p>
  <div class="highlight-default-notranslate"><pre>
  zscale (arg [,z1, z2 [, nbins]]) - scale to a fixed number of bins
              zscalem (arg1, arg2) - automatic scaling with filtering
          gr[ea]y (arg1,arg2,arg3) - RGB to grayscale conversion
         bscale (arg, zero, scale) - linearly transform intensity scale
      gamma (arg, gamma [, scale]) - apply a gamma correction
  </pre></div>
  <p>
          These functions may be used to scale the intensity values of the
  image before output in order to map image datatypes to a specified range.
  The 'args' value may be a list of image operands or expressions.  These 
  functions may be used as arguments to the output functions above
  or as operands within more complex expressions.
  </p>
  <dl id="l_zscale">
  <dt><b>zscale (arg [,z1,z2 [,nbins]])</b></dt>
  <!-- Sec='MORE ON OUTBANDS EXPRESSIONS' Level=0 Label='zscale' Line='zscale (arg [,z1,z2 [,nbins]])' -->
  <dd>Scale the pixels in a given range to a specified number of bins.  This
  function will map the input pixels within the range z1 to z2 to one of 
  'nbins' values.  Pixels less than z1 are mapped to the lowest output
  intensity value, pixels greater than z2 are mapped to the highest value.
  If no <i>z1</i> and <i>z2</i> arguments are given appropriate values will
  be computed using the same algorithm and default parameters used by 
  the <i>DISPLAY</i> task (see the help page for more information).
  If no <i>nbins</i> value is given 256 bins are assumed.
  If the given value of z1 is greater than z2 the mappings will be inverted,
  i.e. larger pixel values will map to the lower bin numbers, smaller pixel
  values will map to larger bin numbers.  For example, to map the dev$pix
  test image to 200 colors such that there are <span style="font-family: monospace;">"black"</span> stars on a <span style="font-family: monospace;">"white"</span>
  background one could use
  <div class="highlight-default-notranslate"><pre>
  zscale (b1, @"i_maxpixval", @"i_minpixval", 200)
  </pre></div>
  </dd>
  </dl>
  <dl id="l_zscalem">
  <dt><b>zscalem (arg1, arg2)</b></dt>
  <!-- Sec='MORE ON OUTBANDS EXPRESSIONS' Level=0 Label='zscalem' Line='zscalem (arg1, arg2)' -->
  <dd>This is a variant of the zscale operand with automatic scale calculation;
  i.e.  zscale (arg).  The first argument is the same as for zscale to select
  the pixel values.  The second argument is a boolean (true or false)
  expression selecting whether a value in the first argument is to be used in
  the calculation.  This allows limiting the automatic scale calculation to
  pixels specified in a mask or to a certain range to exclude extreme or bad
  values that would otherwise perturb the result.  Typical usages might be
  <div class="highlight-default-notranslate"><pre>
  zscalem (i1, i2==0)
  zscalem (i1, i1&gt;0&amp;&amp;i1&lt;10000)
  </pre></div>
  where i1 are the image pixels and i2 would be pixels from the second
  input argument which defines a mask.  Note that you can't just say i2
  for a mask but must use it in an expression resulting in a true or false
  value.  Also note that the result is always in the range 0 to 255.
  </dd>
  </dl>
  <dl id="l_grey">
  <dt><b>grey (arg1,arg2,arg3) or gray (arg1,arg2,arg3)</b></dt>
  <!-- Sec='MORE ON OUTBANDS EXPRESSIONS' Level=0 Label='grey' Line='grey (arg1,arg2,arg3) or gray (arg1,arg2,arg3)' -->
  <dd>Convert three image operands or expressions to a single grayscale image
  using the standard NTSC equation:
  <div class="highlight-default-notranslate"><pre>
  Gray = 0.3 * arg1 + 0.59 * arg2 + 0.11 * arg3
  </pre></div>
  </dd>
  </dl>
  <dl id="l_bscale">
  <dt><b>bscale (arg, zero, scale)</b></dt>
  <!-- Sec='MORE ON OUTBANDS EXPRESSIONS' Level=0 Label='bscale' Line='bscale (arg, zero, scale)' -->
  <dd>Linearly transform the intensity scale of the image using the equation
  <div class="highlight-default-notranslate"><pre>
  new[i] = (arg[i] - zero) / scale
  </pre></div>
  Pixels are scaled in their input datatype prior to converting to the output
  datatype.
  </dd>
  </dl>
  <dl id="l_gamma">
  <dt><b>gamma (arg, gamma [, scale])</b></dt>
  <!-- Sec='MORE ON OUTBANDS EXPRESSIONS' Level=0 Label='gamma' Line='gamma (arg, gamma [, scale])' -->
  <dd>Apply a gamma correction to the pixels.  Pixel values are scaled according to
  the equation
  <div class="highlight-default-notranslate"><pre>
  new = scale * [ (old/scale) ** (1.0/gamma) ]
  </pre></div>
  If no scale argument is given a value of 255 will be assumed.
  </dd>
  </dl>
  <p>
      <i>Additional functions</i> are supported for specific formats:
  </p>
  <div class="highlight-default-notranslate"><pre>
       Function             Description              Formats
       --------             -----------              -------
     cmap (r,g,b [,ncols])  create 8-bit colormap    GIF,RAS,XWD,EPS
  setcmap (args, [opts])    define a colormap        GIF,RAS,XWD,EPS
    psdpi (args, dpi)       set dpi for output       EPS
  psscale (args, scale)     set scale of output      EPS
  </pre></div>
  <p>
  	These functions may take as arguments some of the output functions
  named above.  For example, one can specify the dpi resolution of EPS output
  and band storage of images using something like
  </p>
  <div class="highlight-default-notranslate"><pre>
  psdpi(band(args), dpi)
  </pre></div>
  <dl id="l_cmap">
  <dt><b>cmap (arg1,arg2,arg3 [, ncolors])</b></dt>
  <!-- Sec='MORE ON OUTBANDS EXPRESSIONS' Level=0 Label='cmap' Line='cmap (arg1,arg2,arg3 [, ncolors])' -->
  <dd>Compute an 8-bit colormap from three image operands or expressions using a
  Median-Cut Algorithm and Floyd-Steinberg dithering.  The computed colormap
  is written to the header of the output file.  The resultant image 
  is an 8-bit color index into the computed colormap.  The <i>ncolors</i> argument
  specifies the number of desired colors, a default value of 256 will be used
  if not provided.  This function is only
  allowed for builtin formats supporting color lookup tables and may not be
  used within another expression or function.
  </dd>
  </dl>
  <dl id="l_setcmap">
  <dt><b>setcmap (args, cmap [, brightness, contrast]) </b></dt>
  <!-- Sec='MORE ON OUTBANDS EXPRESSIONS' Level=0 Label='setcmap' Line='setcmap (args, cmap [, brightness, contrast]) ' -->
  <dd>Define the colormap to be used on output.  This function is only supported
  for formats that support colormaps, the <i>args</i> expressions are used to
  compute the color index values.  The <i>cmap</i> argument may either be the
  filename of a normalized colormap table (such as is used by <i>XImtool</i>)
  or one of the builtin values:
  <div class="highlight-default-notranslate"><pre>
  aips0           - and RGB false color mapping
  blue            - various shades of blue
  color           - standard B/W and RGB colormap
  grayscale       - standard grayscale
  greyscale       - (alias for above)
  green           - various shades of green
  halley          - standard halley mission colormap
  heat            - temperatures as colors
  rainbow         - rainbow colors
  red             - various shades of red
  staircase       - RGB staircase
  standard        - RGB ramps
  overlay         - grayscale with IMDKERN overlay colors
  </pre></div>
  Colormap names must be quoted with either single or double quote characters.
  The optional <i>brightness</i> and <i>contrast</i> arguments have default 
  values of 0.5 and 1.0 respectively corresponding to the default 
  brightness/contrast scaling of the <i>XImtool</i> display server.  
  If the cmap argument is an empty string the default Grayscale LUT will 
  be used, IRAF logical paths may be used in the filename specification. 
  </dd>
  </dl>
  <dl id="l_psdpi">
  <dt><b>psdpi (args, dpi)</b></dt>
  <!-- Sec='MORE ON OUTBANDS EXPRESSIONS' Level=0 Label='psdpi' Line='psdpi (args, dpi)' -->
  <dd>Specify the dots-per-inch resolution of the output image.  The default 
  resolution is 300dpi, this may need to be reset for some printers or if
  the raster rendering produces <span style="font-family: monospace;">"bands"</span> in the output.  This function may
  only be used as an argument to the <i>psscale()</i> function.
  </dd>
  </dl>
  <dl id="l_psscale">
  <dt><b>psscale (args, scale)</b></dt>
  <!-- Sec='MORE ON OUTBANDS EXPRESSIONS' Level=0 Label='psscale' Line='psscale (args, scale)' -->
  <dd>Specify the scale of the output image.  The default value is 1.0 which 
  means that image printed on a 300dpi device is roughly the same size 
  as displayed on a typical 72dpi screen.  Scale values less than one reduce
  the image size on the page, values greater than one increase the size.  The
  scale value will automatically be adjusted if it creates an image that will
  not fit on a 8.5 inch by 11 inch page.  A scale value of 0.25 prints one
  image pixel per 300dpi printer pixel.  This function may
  only be used as an argument to the <i>psdpi()</i> function.
  </dd>
  </dl>
  </section>
  <section id="s_export_header_format">
  <h3>Export header format</h3>
  <p>
  	The header prepended to the binary data is ascii text consisting of
  keyword-value pairs, one per line, terminated with a newline after the
  value, beginning with the magic string 
  <span style="font-family: monospace;">"format = EXPORT"</span>.  Using an ascii header allows the file format to be
  easily determined by the user with a file pager or any program reading 
  the file.
  </p>
  <p>
  Defined keywords are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  date                - date file was written (dd/mm/yy)
  hdrsize             - size of header (bytes)
  ncols               - no. of image columns
  nrows               - no. of image rows
  nbands              - no. of image bands
  datatype            - pixel type (as &lt;type&gt;&lt;nbytes&gt;)
  outbands            - outband expression list
  interleave          - interleave value (same as above)
  bswap               - are ints swapped relative to MII format?
  image1              - image names used in creating file
    :
  imageN
  header1 <span style="font-family: monospace;">'{'</span> &lt;header&gt; <span style="font-family: monospace;">'}'</span>  - image headers of above
    :
  headerN <span style="font-family: monospace;">'{'</span> &lt;header&gt; <span style="font-family: monospace;">'}'</span>
  end                 - terminate header
  </pre></div>
  <p>
  If the <i>header</i> parameter is set to <span style="font-family: monospace;">"long"</span> the image headers for 
  each image used in creating the file is included in the output header, 
  otherwise only the image names are included.
  </p>
  <p>
  A sample (verbose) header might look like:
  </p>
  <div class="highlight-default-notranslate"><pre>
  format = EXPORT
  date = '19/06/94'
  hdrsize = 2084
  nrows = 512
  ncols = 512
  nbands = 1
  datatype = 'i2'
  outbands = ''
  interleave = 0
  bswap = no
  image1 = "dev$pix"
  header1 = {
  IRAF-BPX=                   16  /  DATA BITS/PIXEL
  IRAFTYPE= 'SHORT   '            /  PIXEL TYPE
  CCDPICNO=                   53  /  ORIGINAL CCD PICTURE NUM
  ITIME   =                  600  /  INTEGRATION TIME (SECS)
      :   :           :                       :
  }
  end
  </pre></div>
  </section>
  <section id="s_builtin_formats">
  <h3>Builtin formats</h3>
  <p>
  	While the task provides a way of writing general binary raster
  files there is still a need for converting to specific formats.  
  Implementing most formats is trivial since they usually follow the
  data model and the only <span style="font-family: monospace;">"builtin"</span> knowledge of the format is the minimal
  header required.  More complex formats such as GIF and EPS are implemented 
  as special cases.  Note that all of the builtin formats require 8-bit color
  index or 8-bits per color in RGB or RGBA files, users should be careful
  in how the datatype conversion from IRAF image types is handled. In most
  cases this can be handled with the <i>zscale()</i> or <i>zscalem</i> functions.
  </p>
  <p>
  	For each of the formats listed below the table shows the number
  of <i>outbands</i> expressions required and the type of output file that
  can be written.  Complete examples for the most common cases are shown in
  the <i>Examples</i> section below.  The columns in the table are defined as
  </p>
  <div class="highlight-default-notranslate"><pre>
  #expr               - number of required <i>outbands</i> expressions
  Type                - RGB or 8-bit colormap (index) file
  bitpix              - number of bits-per-pixel
  CLT?                - does the file have a colormap?
  Alpha?              - does the file have an alpha channel?
  Interleaving        - type of pixel interleaving
  Notes               - see explanation below each table
  </pre></div>
  <p>
  A general description and specific restrictions or requirements are given for 
  each format.  An error is generated of the input parameters do not meet the 
  requirements of the requested format.  Unless otherwise noted the values of 
  the <i>header</i>, <i>bswap</i> and <i>interleave</i> parameters will be ignored.
  The value of <i>outtype</i> will be set internally and is also ignored.
  </p>
  <p>
  	If the input image is 3-D and no <i>outbands</i> expressions are
  given, then where supported each band will be written to the output file as 
  a complete image or RGB color component.  For example, a 512x512x3 image 
  will be written as a 512x1536 image with each band comprising one third 
  the height of the output image.  If the output format requires 24-bit pixels 
  then each band of the image will be written as a color component.
  </p>
  <p>
  	The currently supported builtin formats include:
  </p>
  <dl id="l_EPS">
  <dt><b>EPS     - Encapsulated PostScript</b></dt>
  <!-- Sec='BUILTIN FORMATS' Level=0 Label='EPS' Line='EPS     - Encapsulated PostScript' -->
  <dd><div class="highlight-default-notranslate"><pre>
  #expr    Type   bitpix  CLT?  Alpha?  Interleaving  Notes
  -----    -----  ------  ----  ------  ------------  -----
    1      index  8       no    no      none
  </pre></div>
  	The output 8-bit Encapsulated PostScript image
  centered on the page at a default scale of 1.0 at 300dpi (i.e. the image will
  appear on a 300dpi printer about the same size as displayed on a 72dpi 
  screen).  The output scale may be adjusted using 
  the <i>psscale()</i> function, e.g. to set the output for one image pixel
  per 300 dpi printer pixel use <span style="font-family: monospace;">"psscale(b1,0.25)"</span> (one quarter the normal size
  on the page).  The output dpi resolution may be set explicitly with 
  the <i>psdpi()</i> function, this is sometimes necessary if <span style="font-family: monospace;">"bands"</span> appear 
  in the final output image.  Color EPS files may be written as either RGB
  postscript or with a colormap applied to the data (using either the
  <i>cmap()</i> or <i>setcmap()</i> functions).
  </dd>
  </dl>
  <dl id="l_GIF">
  <dt><b>GIF     - Compuserve's GIF format</b></dt>
  <!-- Sec='BUILTIN FORMATS' Level=0 Label='GIF' Line='GIF     - Compuserve's GIF format' -->
  <dd><div class="highlight-default-notranslate"><pre>
  #expr    Type   bitpix  CLT?  Alpha?  Interleaving  Notes
  -----    -----  ------  ----  ------  ------------  -----
    1      index  8       yes   no      none          1
    3      index  8       yes   no      none          2
  
    Notes:
        1) Colormap generation enabled using <i>setcmap()</i> or else
           default grayscale colormap will be used
        2) use of <i>cmap()</i> required to generate colormap
  </pre></div>
  	The output file is a GIF '87 image.  A linear colormap of 256 entries 
  will automatically be generated if only one image or expression is given for
  conversion and no colormap is specified.  
  If three images or expressions are specified a 24-to-8 bit
  conversion can be done using a Median Cut Algorithm and Floyd-Steinberg
  dithering with the required <i>cmap()</i> function.  Since the colormap 
  sizes are limited to 256 entries the maximum pixel value is assumed to 
  be 255, i.e. the output pixel size will be forced to 8-bits or less.
  </dd>
  </dl>
  <dl id="l_IMH">
  <dt><b>IMH     - IRAF image file</b></dt>
  <!-- Sec='BUILTIN FORMATS' Level=0 Label='IMH' Line='IMH     - IRAF image file' -->
  <dd>	The output file is an IRAF OIF format image of the specified datatype.
  Writing the image out as another IRAF image may be used to scale or composite
  several images into a new image that can be annotated with the <i>TVMARK</i>
  task before writing out the final format.
  </dd>
  </dl>
  <dl id="l_MIFF">
  <dt><b>MIFF    - ImageMagick MIFF format image</b></dt>
  <!-- Sec='BUILTIN FORMATS' Level=0 Label='MIFF' Line='MIFF    - ImageMagick MIFF format image' -->
  <dd><div class="highlight-default-notranslate"><pre>
  #expr    Type   bitpix  CLT?  Alpha?  Interleaving  Notes
  -----    -----  ------  ----  ------  ------------  -----
    1      index  8       no    no      none
    1      index  8       yes   no      none          1,2
    3      rgb    24      no    no      pixel
  
    Notes:
        1) Colormap generation enabled using <i>setcmap()</i>
        2) Colormap generation enabled using <i>cmap()</i>
  </pre></div>
  	The output file is a Machine Independent File Format image, with or
  without a colormap or as a 24-bit RGB image.  Although MIFF permits 64K
  colors in a colormap the task only supports 256 colors, no compression is
  used in the image.  The maximum pixel value per color is assumed to be 255.
  </dd>
  </dl>
  <dl id="l_PGM">
  <dt><b>PGM     - PBMPlus PGM format image</b></dt>
  <!-- Sec='BUILTIN FORMATS' Level=0 Label='PGM' Line='PGM     - PBMPlus PGM format image' -->
  <dd><div class="highlight-default-notranslate"><pre>
  #expr    Type   bitpix  CLT?  Alpha?  Interleaving  Notes
  -----    -----  ------  ----  ------  ------------  -----
    1      index  8       no    no      none
    3      index  8       no    no      none          1
  
    Notes:
        1) Grayscale may be produce with <i>gray()</i> function
  </pre></div>
  	The output file is an 8-bit raw (i.e. binary pixels) PGM image.  
  The maximum pixel value is assumed to be 255.
  </dd>
  </dl>
  <dl id="l_PPM">
  <dt><b>PPM     - PBMPlus PPM format image</b></dt>
  <!-- Sec='BUILTIN FORMATS' Level=0 Label='PPM' Line='PPM     - PBMPlus PPM format image' -->
  <dd><div class="highlight-default-notranslate"><pre>
  #expr    Type   bitpix  CLT?  Alpha?  Interleaving  Notes
  -----    -----  ------  ----  ------  ------------  -----
    3      rgb    24      no    no      pixel
  </pre></div>
  	The output file is an 24-bit raw (i.e. binary pixels) PPM image. 
  The maximum pixel value per color is assumed to be 255.
  </dd>
  </dl>
  <dl id="l_RAS">
  <dt><b>RAS     - Sun rasterfile format</b></dt>
  <!-- Sec='BUILTIN FORMATS' Level=0 Label='RAS' Line='RAS     - Sun rasterfile format' -->
  <dd><div class="highlight-default-notranslate"><pre>
  #expr    Type   bitpix  CLT?  Alpha?  Interleaving  Notes
  -----    -----  ------  ----  ------  ------------  -----
    1      index  8       no    no      none
    1      index  8       yes   no      none          1,2
    3      rgb    24      no    no      pixel
    4      rgb    32      no    yes     pixel
  
    Notes:
        1) Colormap generation enabled using <i>setcmap()</i>
        2) Colormap generation enabled using <i>cmap()</i>
  </pre></div>
  	The output file will be a Sun rasterfile.  The header values
  (long integers) may be byte swapped by setting the <i>bswap</i> parameter 
  to <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"i4"</span>.  For 32-bit true-color rasterfiles the
  alpha channel should be specified as the first expression.  The maximum 
  pixel value is assumed to be 255.
  </dd>
  </dl>
  <dl id="l_RGB">
  <dt><b>RGB     - SGI RGB format image</b></dt>
  <!-- Sec='BUILTIN FORMATS' Level=0 Label='RGB' Line='RGB     - SGI RGB format image' -->
  <dd><div class="highlight-default-notranslate"><pre>
  #expr    Type   bitpix  CLT?  Alpha?  Interleaving  Notes
  -----    -----  ------  ----  ------  ------------  -----
    1      index  8       no    no      none
    3      rgb    24      no    no      scanline
  </pre></div>
  	The output file will be an SGI RGB (IRIS) format image.  Although
  this format supports colormaps they are not supported by this task.
  The maximum pixel value is assumed to be 255.
  </dd>
  </dl>
  <dl id="l_XWD">
  <dt><b>XWD     - X11 Window dump file</b></dt>
  <!-- Sec='BUILTIN FORMATS' Level=0 Label='XWD' Line='XWD     - X11 Window dump file' -->
  <dd><div class="highlight-default-notranslate"><pre>
  #expr    Type   bitpix  CLT?  Alpha?  Interleaving  Notes
  -----    -----  ------  ----  ------  ------------  -----
    1      index  8       yes   no      none          1,2,3
    3      rgb    24      no    no      none
  
    Notes:
        1) Linear grayscale colormap automatically generated
        2) Colormap generation enabled using <i>setcmap()</i>
        3) Colormap generation enabled using <i>cmap()</i>
  </pre></div>
  	The output file will be an X11 window dump file.
  A linear colormap of 256 entries will automatically be generated if only 
  one image or expression is given for conversion, the <i>setcmap()</i> function
  may be used to create an alternate colormap.  If three images or expressions 
  are specified a 24-to-8 bit conversion can be done using a Median Cut 
  Algorithm and Floyd-Steinberg dithering if the <i>cmap()</i> function is 
  specified.  Header values (long integers) may be byte swapped by setting the
  task <i>bswap</i> parameter to <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"i4"</span>.  The maximum pixel value is 
  assumed to be 255.
  </dd>
  </dl>
  </section>
  <section id="s_color_output_images">
  <h3>Color output images</h3>
  <p>
  	In theory the colormaps generated by the <i>cmap()</i> and
  <i>setcmap()</i> functions could be written in the header for raw binary
  output and the pixel written out as color indices, but since we also
  support color index formats which are recognized widely by other packages 
  there is no need to do this.  Therefore we limit the use of colormaps to 
  the builtin formats which already support it.
  </p>
  <p>
  	The simplest type of <span style="font-family: monospace;">"color"</span> image is the familiar grayscale image.
  Pixel values represent the display gray level, although for some formats a CLT 
  (color lookup table) is required (e.g. GIF) and these pixel values are 
  actually indices into a grayscale colormap.  Most of the conversion done
  with this task will produce a grayscale image of some sort.  For <span style="font-family: monospace;">"color 
  index"</span> images the pixel values are indices into a colormap containing the 
  RGB components of the color for a pixel with that value.  Colormaps 
  usually permit at most 256 possible colors implying 8-bit pixels.
  In this task the colormap may be computed either with the <i>cmap()</i> (which 
  does a 24-to-8 bit mapping of the colors) or the <i>setcmap()</i> function 
  (which computes the colormap from a display lookup table of colors).  
  <span style="font-family: monospace;">"True color"</span> images are those which have 24-bits of color (8-bit for each
  component) for each pixel, some true color images also contain an alpha 
  channel (an extra 8-bits of constant intensity) which may or may not be 
  used by the software displaying the image.
  </p>
  <p>
  	The <i>cmap()</i> function takes three images and computes a colormap
  using Paul Heckbert's Median Cut Algorithm (<span style="font-family: monospace;">"Color Image Quantization for
  Frame Buffer Display"</span>, SIGGRAPH '82 Proceedings, pg 297) and Floyd-Steinberg 
  dithering technique.  The computed colormap is written to the file header 
  and pixel values are converted to color indices.  By default 256 colors are 
  computed but fewer colors may be requested.  This function is most useful 
  for generating pseudo-color images from three input images taken in different
  filter bands (which is required for some formats like GIF that do not 
  support 24-bit RGB).
  	
  	The <i>setcmap()</i> function, on the other hand, can be used to
  generate a color image from a single input image and a lookup table such as
  the ones used by displays servers like XImtool.  In this case the pixel
  values are indices into a pre-defined colormap which is normalized between
  zero and one (so that it may be scaled to the desired number of colors).
  The <i>brightness</i> argument defines the center of the transfer function, the
  default is 0.5 because it in the middle of the normalized range.  The 
  <i>contrast</i> arguments sets the contrast of the transfer function.  For
  example, the normalized pixel values and default brightness/contrast settings
  will map the pixel values to the corresponding color in the LUT.  Changing
  the brightness to a lower value means that pixel intensities will map to lower
  values in the LUT, doubling the contrast for instance means that the LUT 
  will increment two colors for every unit pixel change.  This is what happens
  when changing a displayed image in IRAF with the mouse by moving the cursor
  left-right (changing the brightness) or up-down (changing the contrast).
  </p>
  <p>
  	An example use of this function would be if one wanted to convert an 
  IRAF image to a color rasterfile with the same colormap and intensity 
  scaling as was displayed in XImtool.  After adjusting the display the 
  brightness/contrast values could be read from the control panel and the 
  rasterfile generated using
  </p>
  <div class="highlight-default-notranslate"><pre>
  setcmap (b1, "aips0", 0.36, 1.2)
  </pre></div>
  <p>
  where the <span style="font-family: monospace;">"aips0"</span> is one of the builtin colormaps and the brightness and
  contrast arguments are those from the ximtool display.  Similarly, the
  expression
  </p>
  <div class="highlight-default-notranslate"><pre>
  setcmap (zscale(i1),"idl15.lut")
  </pre></div>
  <p>
  will save the image with the same intensity scaling and color as would be see
  by displaying it to ximtool using the default DISPLAY task settings,
  normalized XImtool brightness/contrast values and the <span style="font-family: monospace;">"idl15.lut"</span> LUT in the
  current directory.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  	The examples below are divided into several categories showing
  typical usage when creating various raw and builtin output files.  Note
  that the output file will have a filename extension added indicating the 
  format when converting to a builtin format.
  </p>
  <p>
  <i>Creating Raw Binary Files</i>
  </p>
  <p>
  List the pixels being one the standard output, apply a linear scale
  function first:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export dev$pix "" list outbands="bscale(b1,1.0,3.2)"
  </pre></div>
  <p>
  Convert the dev$pix test image to an 8-bit binary file with a gamma 
  correction, write the standard header:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export dev$pix bfil raw header+ outty="u1" outbands="gamma(b1,1.8)"
  </pre></div>
  <p>
  Write the three bands of an IRAF image to a pixel interleaved binary 
  file of short integers, prepend a user-defined header:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export rgbim bfil raw header="hdr.txt" outty="i2" outban="b1,b2,b3"
  </pre></div>
  <p>
  Convert three images representing RGB to a 4-color line-interleaved
  file, the IRAF images don't require scaling, create alpha channel:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export rim,gim,bim bfil raw outty="u1" outban="line(i1,i2,i3,0)"
  </pre></div>
  <p>
  Write the three bands of an IRAF image to a line-interleaved binary 
  file of short integers:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export rgbim binfil raw outtype="i2" outbands="line(b1,b2,b3)"
  cl&gt; export rgbim binfil raw outtype="i2" outbands="" interleave=3
  </pre></div>
  <p>
  Write the three bands of an IRAF image to a grayscale binary file using 
  a custom conversion formula.  Pixel values are truncated to 8-bits:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export rgbim grey raw outty="u1" outban="(.2*b1)+(.5*b2)+(.3*b3)"
  </pre></div>
  <p>
  <i>Creating Specific Formats</i>
  </p>
  <p>
  Convert dev$pix to an 8-bit Sun rasterfile with no colormap, scale the 
  image to 8-bits using the default <i>zscale()</i> intensity mapping:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export dev$pix dpix ras outbands="zscale(i1)"
  </pre></div>
  <p>
  Apply various functions to the data before doing the same conversion:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export dev$pix dpix ras outbands="zscale(log(i1))"
  cl&gt; export dev$pix dpix ras outbands="zscale(sqrt(i1))"
  </pre></div>
  <p>
  Convert dev$pix to an 8-bit Sun rasterfile with no colormap, image pixel
  values are truncated to 8-bits:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export dev$pix dpix ras
  </pre></div>
  <p>
  Convert three images representing RGB to a 24-bit Sun rasterfile, assume
  the IRAF images don't require intensity scaling:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export rim,gim,bim rgb ras outbands="i1,i2,i3"
  </pre></div>
  <p>
  Create a Silicon Graphics RGB format image from a 3-D image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export rgbim bdata rgb outbands="b1,b2,b3"
  </pre></div>
  <p>
  Convert dev$pix to an 8-bit GIF grayscale image, scale the image to map 
  only pixel values between 0 and 320:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export dev$pix dpix gif outbands="zscale(i1,0.0,320.0)"
  </pre></div>
  <p>
  Combine three images representing RGB into an 8-bit X11 window dump
  grayscale image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export rim,gim,bim gray xwd outbands="gray(i1,i2,i3)"
  </pre></div>
  <p>
  Convert dev$pix to an Encapsulated PostScript file at half the normal scale 
  and apply a linear transformation to scale the pixel values:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export dev$pix dpix eps \
  &gt;&gt;&gt;    outbands="psscale(bscale(i1,0.,0.32), 0.5)"
  </pre></div>
  <p>
  Convert three images representing RGB to an 8-bit GIF color image with
  a computed colormap:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export rim,gim,bim rgb gif outbands="cmap(i1,i2,i3)"
  </pre></div>
  <p>
  Convert dev$pix to a color rasterfile using the builtin <span style="font-family: monospace;">"heat"</span> colormap
  and default intensity mapping:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export dev$pix dpix ras outban='setcmap(zscale(i1),"heat")'
  </pre></div>
  <p>
  Convert dev$pix to a color rasterfile using the XImtool <span style="font-family: monospace;">"idl15.lut"</span> 
  LUT file in the current directory and default intensity mapping:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; copy /usr/local/lib/imtoolcmap/idl15.lut .
  cl&gt; export dev$pix dpix ras outbands="setcmap(zscale(i1),'idl15.lut')"
  </pre></div>
  <p>
  <i>Advanced Usage</i>
  </p>
  <p>
  Given a set of DISPLAY task z1/z2 values of 10 and 320 respectively, and
  brightness/contrast values from XImtool of 0.6 and 1.2 respectively, 
  convert an image to an EPS file with the same appearance:
  </p>
  <div class="highlight-default-notranslate"><pre>
  im&gt; type expr
  setcmap ( zscale (i1, 10.0, 320.0), "greyscale", 0.6, 1.2 )
  im&gt; export dev$pix dpix eps outbands="@expr"
  </pre></div>
  <p>
  Concatenate two images side-by-side to a PGM file, normalize each image 
  by it's exposure time and apply a default intensity mapping:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export im1,im2 two pgm \
  &gt;&gt;&gt;     outbands='(zscale(i1/i1.otime)) // (zscale(i2/i2.otime))'
  </pre></div>
  <p>
  Convert dev$pix to a color GIF using the XImtool <span style="font-family: monospace;">"idl15"</span> LUT with a spec-
  ified brightness/contrast scale.  Map only pixel values between 5 and 300 
  to 201 output intensity values.  This should produce and image identical 
  to what one would get by displaying dev$pix to imtool, setting the same 
  brightness/contrast scale, and selecting the idl15 LUT:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; copy /usr/local/lib/imtoolcmap/idl15.lut .
  cl&gt; type expr.dat
        setcmap (
            zscale(i1, 5.0, 320.0, 201),
            "idl15.lut",
            0.41,
            1.35)
  cl&gt; export dev$pix dpix gif outbands="@expr.dat"
  </pre></div>
  <p>
  Combine three images representing RGB to an 8-bit Sun rasterfile with a
  computed colormap.  Scale the intensity value of each image differently.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type expr.dat
        cmap (
            zscale (i1),
            zscale (i2, 0.0, 1200.0),
            zscale (i3, -1.0, 320.0) )
  cl&gt; export im1,im2,im3 rgb ras outbands="@expr.dat"
  </pre></div>
  <p>
  Do the same example but apply a gamma correction to the images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type expr.dat
        cmap (
            gamma (zscale(i1),        2.2),
            gamma (zscale(i2,0,1200), 2.2),
            gamma (zscale(i3,-1,320), 2.2) )
  </pre></div>
  <p>
  Write four images to a grayscale GIF file such that they are tiled in a 
  2x2 grid:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export im1,im2,im3,im4 quad gif \
  &gt;&gt;&gt;        outbands="band( (i1//i2), (i3//i4) )"
  </pre></div>
  <p>
  Do the same example but create a border of 2 gray pixels around each
  of the images and apply the AIPS0 LUT with brightness/contrast values
  to create a color image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; copy /usr/local/lib/imtoolcmap/aips0.lut .
  cl&gt; type expr.dat
        setcmap (
            band(
                128, 128,
                (repl (128,2) // i1// repl (128,2) // i2 // repl (128,2)),
                128, 128,
                (repl (128,2) // i3// repl (128,2) // i4 // repl (128,2)),
                128, 128 ),
            "aips0.lut",
            0.54,
            1.03)
  cl&gt; export im1,im2,im3,im4 cquad gif outbands="@expr.dat"
  </pre></div>
  <p>
  Automatically scale an image ignoring data in a bad pixel mask (bpm), map the
  result to the greyscale part of the <span style="font-family: monospace;">"overlay"</span> color map, and apply a
  overlay pattern given by another mask (pattern).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; export dev$pix,bpm,pattern foo gif \
  &gt;&gt;&gt; outbands = "setcmap(i3==0?(zscalem(i1,i2==0)*200/255.):i3+203,'overlay')"
  </pre></div>
  <p>
  The pattern has values of 1 and 203 is added to get it into the color map
  values of the overlay colors.  The factor of 200/255 is to scale the result
  of zscalem from the range 0-255 to the range 0-200.
  </p>
  </section>
  <section id="s_notes">
  <h3>Notes</h3>
  <p>
  	This task is new with V2.11.
  </p>
  <p>
  	(long int headers in RAS and XWD may cause problems on 64-bit 
  machines like the Alpha where host software expects 64-bit values.  Need to
  see if IRAF on the alpha produces 32 or 64-bit longs, either way exchanging
  images may be a problem)
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  	Output of bitmap images is currently not supported.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  import, tvmark, imexpr
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'MORE ON OUTBANDS EXPRESSIONS' 'EXPORT HEADER FORMAT' 'BUILTIN FORMATS' 'COLOR OUTPUT IMAGES' 'EXAMPLES' 'NOTES' 'BUGS' 'SEE ALSO'  -->
  

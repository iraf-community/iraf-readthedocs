.. _mkpattern:

mkpattern: Make/add patterns to images
======================================

**Package: artdata**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkpattern input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Images to create or modify.  Image sections are allowed to apply a pattern
  to a portion of an image.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = ""' -->
  <dd>Output images when modifying input images.  If no output images are
  given then existing images in the input list are modified directly.
  If an output image list is given then it must match in number the
  input list.
  </dd>
  </dl>
  <dl id="l_pattern">
  <dt><b>pattern = <span style="font-family: monospace;">"constant"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pattern' Line='pattern = "constant"' -->
  <dd>Pattern to be used.  The patterns are:
  <dl>
  <dt><b>constant</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='constant' Line='constant' -->
  <dd>Constant value v1.
  </dd>
  </dl>
  <dl>
  <dt><b>grid</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='grid' Line='grid' -->
  <dd>A grid starting with the first pixel and going in steps of the
  pattern size with value v2.  Pixels between the grid have value v1.
  A minimum grid size of 2 is enforced.
  </dd>
  </dl>
  <dl>
  <dt><b>checker</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='checker' Line='checker' -->
  <dd>A checkerboard with squares of the pattern size alternating between values v1
  and v2 starting with v1.
  </dd>
  </dl>
  <dl>
  <dt><b>coordinates</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='coordinates' Line='coordinates' -->
  <dd>Each pixel is numbered sequentially starting with 1 with the column
  dimension varying fastest.
  </dd>
  </dl>
  <dl>
  <dt><b>slope</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='slope' Line='slope' -->
  <dd>A sloped plane starting with value v1 for the first pixel and value v2 for
  the last pixel in one or two dimensions.
  </dd>
  </dl>
  <dl>
  <dt><b>square</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='square' Line='square' -->
  <dd>A checkerboard pattern in which the size of the squares begin with
  the pattern size and grow as the square of the coordinate.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_option">
  <dt><b>option = <span style="font-family: monospace;">"replace"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='option' Line='option = "replace"' -->
  <dd>Editing option when modifying existing images.  Often this is used
  in conjunction with image sections to modify a part of an image.
  The options are:
  <div class="highlight-default-notranslate"><pre>
   replace - Replace the image with the pattern.
       add - Add the pattern to the image.
  multiply - Multiply the pattern with the image values.
  </pre></div>
  </dd>
  </dl>
  <dl id="l_v1">
  <dt><b>v1 = 0., v2 = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='v1' Line='v1 = 0., v2 = 1.' -->
  <dd>Pattern values used as described for each pattern.
  </dd>
  </dl>
  <dl id="l_size">
  <dt><b>size = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='size' Line='size = 1' -->
  <dd>Pattern size used as described for each pattern.
  </dd>
  </dl>
  <p>
  WHEN CREATING NEW IMAGES
  </p>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = ""' -->
  <dd>Image title to be given to the images.  Maximum of 79 characters.
  </dd>
  </dl>
  <dl id="l_pixtype">
  <dt><b>pixtype = <span style="font-family: monospace;">"real"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixtype' Line='pixtype = "real"' -->
  <dd>Pixel datatype of new images; one of ushort, short, integer, real, double,
  or complex.
  </dd>
  </dl>
  <dl id="l_ndim">
  <dt><b>ndim = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ndim' Line='ndim = 2' -->
  <dd>Number of dimensions between 0 and 7.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = 512, nlines = 512</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = 512, nlines = 512' -->
  <dd>Number of columns (first dimension) and lines (second dimension).
  </dd>
  </dl>
  <dl id="l_n3">
  <dt><b>n3 = 1, n4 = 1, n5 = 1, n6 = 1, n7 = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='n3' Line='n3 = 1, n4 = 1, n5 = 1, n6 = 1, n7 = 1' -->
  <dd>Number of pixels in 3rd-7th  dimensions
  </dd>
  </dl>
  <dl id="l_header">
  <dt><b>header = <span style="font-family: monospace;">"artdata$stdheader.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='header' Line='header = "artdata$stdheader.dat"' -->
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
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task creates or modifies images with a choice of patterns.  New images
  are created with the specified dimensions, datatype, and pattern.
  Existing images may have the pattern replace, add, or multiply the
  pixel values.  Existing images may be modified in place or new images may be
  created and image sections are allowed.
  </p>
  <p>
  For new images a set of header keywords may be added by specifying an
  image or data file with the <i>header</i> parameter (see also <b>mkheader</b>).
  If a data file is specified lines beginning with FITS keywords are
  entered in the image header.  Leading whitespace is ignored and any
  lines beginning with words having lowercase and nonvalid FITS keyword
  characters are ignored.
  </p>
  <p>
  This task is the simplest one for creating empty images to be used for
  mosaicing with <b>imcopy</b> and making patterns for testing display and
  image operators.  The replace option is generally used with image sections
  to place constant values in regions.  The multiply option is useful
  for making masks of the given pattern when the values are 0 and 1.
  </p>
  <p>
  Though the patterns make sense extending to higher dimensions they
  are only defined in two dimensions.  One dimensional images may be
  thought of as the first line of the two dimensional pattern.  Images
  with dimensions greater than 2 simply repeat the two dimensional
  pattern into the higher dimensions.  The reason for stopping at
  two dimensions is simplicity.
  </p>
  <p>
  The patterns have the following precise definitions where P(i,j) is the
  pixel value at column i and line j, v1 and v2 are the pattern
  values, size is the pattern size, ncols and nlines are the number of
  columns and lines in the image, int is the integer function, mod is the
  modulus function, and sqrt is the square root function.
  </p>
  <div class="highlight-default-notranslate"><pre>
                 k = int ((i-1)/size), l = int ((j-1)/size)
                 ksr = int (sqrt (k)), lsr = int (sqrt (l))
                 slope = (v2-v1) / ((ncols+nlines-2)/size)
  
     constant:   P(i,j) = v1
  
         grid:   P(i,j) = v2   when mod(i,size)=1 or mod(j,size)=1
                 P(i,j) = v1   otherwise
  
  coordinates:   P(i,j) = i + j * ncols
  
      checker:   P(i,j) = v1   when mod(k,2)=0 and mod(l,2)=0
                 P(i,j) = v2   when mod(k,2)=1 and mod(l,2)=0
                 P(i,j) = v2   when mod(k,2)=0 and mod(l,2)=1
                 P(i,j) = v1   when mod(k,2)=1 and mod(l,2)=1
  
        slope:   P(i,j) = v1 + slope * (k + l)
  
       square:   P(i,j) = v1   when mod(ksr,2)=0 and mod(lsr,2)=0
                 P(i,j) = v2   when mod(ksr,2)=1 and mod(lsr,2)=0
                 P(i,j) = v2   when mod(ksr,2)=0 and mod(lsr,2)=1
                 P(i,j) = v1   when mod(ksr,2)=1 and mod(lsr,2)=1
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create an empty (constant value of zero) three dimensional image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkpattern cube ndim=3 nc=100 nl=100 n3=100
  </pre></div>
  <p>
  2. Replace a square region of an image with the value -1000.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkpat alpha[201:250,1:50] v1=-1000
  </pre></div>
  <p>
  3. Put a grid pattern on an image to create a new image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkpat dev$pix out=gridpix pat=grid op=mul v1=1 v2=0
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MKPATTERN">
  <dt><b>MKPATTERN V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MKPATTERN' Line='MKPATTERN V2.11' -->
  <dd>Now allows ndim=0 to create dataless header.
  Now allows type ushort pixel type.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imcopy, imreplace
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

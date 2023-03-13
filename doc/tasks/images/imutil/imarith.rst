.. _imarith:

imarith: Simple image arithmetic
================================

**Package: imutil**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  imarith operand1 op operand2 result
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_operand1">
  <dt><b>operand1, operand2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='operand1' Line='operand1, operand2' -->
  <dd>Lists of images and constants to be used as operands.
  Image templates and image sections are allowed.
  </dd>
  </dl>
  <dl id="l_op">
  <dt><b>op    </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='op' Line='op    ' -->
  <dd>Operator to be applied to the operands.  The allowed operators
  are <span style="font-family: monospace;">"+"</span>, <span style="font-family: monospace;">"-"</span>, <span style="font-family: monospace;">"*"</span>, <span style="font-family: monospace;">"/"</span>, <span style="font-family: monospace;">"min"</span>, and <span style="font-family: monospace;">"max"</span>.
  </dd>
  </dl>
  <dl id="l_result">
  <dt><b>result</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='result' Line='result' -->
  <dd>List of resultant images.
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = ""' -->
  <dd>Title for the resultant images.  If null (<span style="font-family: monospace;">""</span>) then the title is taken
  from operand1 if operand1 is an image or from operand2 otherwise.
  </dd>
  </dl>
  <dl id="l_divzero">
  <dt><b>divzero = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='divzero' Line='divzero = 0.' -->
  <dd>Replacement value for division by zero.  When the denominator is zero
  or nearly zero the result is replaced by this value.
  </dd>
  </dl>
  <dl id="l_hparams">
  <dt><b>hparams = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hparams' Line='hparams = ""' -->
  <dd>List of header parameters to be operated upon.  This is primarily
  used for adding exposure times when adding images.
  </dd>
  </dl>
  <dl id="l_pixtype">
  <dt><b>pixtype = <span style="font-family: monospace;">""</span>, calctype = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixtype' Line='pixtype = "", calctype = ""' -->
  <dd>Pixel datatype for the resultant image and the internal calculation datatype.
  The choices are given below.  They may be abbreviated to one character.
  <dl>
  <dt><b><span style="font-family: monospace;">""</span>    </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='""    ' -->
  <dd><i>Calctype</i> defaults to the highest precedence operand datatype.  If the
  highest precedence datatype is an integer type and the operation is
  division then the calculation type will be <span style="font-family: monospace;">"real"</span>.  If the highest
  precedence operand is type <span style="font-family: monospace;">"ushort"</span>, <i>calctype</i> will default to
  <span style="font-family: monospace;">"long"</span>.  <i>Pixtype</i> defaults to <i>calctype</i>. Users who want type
  <span style="font-family: monospace;">"ushort"</span> images on output will need to set <i>pixtype</i> to <span style="font-family: monospace;">"ushort"</span>
  explicitly.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"1"</span>, <span style="font-family: monospace;">"2"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"1", "2"' -->
  <dd>The pixel datatype of the first or second operand.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"short"</span>, <span style="font-family: monospace;">"ushort"</span>, <span style="font-family: monospace;">"integer"</span>, <span style="font-family: monospace;">"long"</span>, <span style="font-family: monospace;">"real"</span>, <span style="font-family: monospace;">"double"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"short", "ushort", "integer", "long", "real", "double"' -->
  <dd>Allowed IRAF pixel datatypes.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print the operator, operands, calculation datatype, and the resultant image
  name, title, and pixel datatype.
  </dd>
  </dl>
  <dl id="l_noact">
  <dt><b>noact = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='noact' Line='noact = no' -->
  <dd>Like the verbose option but the operations are not actually performed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Binary image arithmetic is performed of the form:
  </p>
  <p>
  	operand1 op operand2 = result
  </p>
  <p>
  where the operators are addition, subtraction, multiplication,
  division, and minimum and maximum.  The division operator checks for
  nearly zero denominators and replaces the ratio by the value specified
  by the parameter <i>divzero</i>.  The operands are lists of images and
  numerical constants and the result is a list of images.  The number of
  elements in an operand list must either be one or equal the number of
  elements in the resultant list.  If the number of elements is one then
  it is used for each resultant image.  If the number is equal to the
  number of resultant images then the elements in the operand list are
  matched with the elements in the resultant list.  The only limitation
  on the combination of images and constants in the operand lists is that
  both operands for a given resultant image may not be constants.  The
  resultant images may have the same name as one of the operand images in
  which case a temporary image is created and after the operation is
  successfully completed the image to be replaced is overwritten by the
  temporary image.
  </p>
  <p>
  If both operands are images the lengths of each axis for the common
  dimensions must be the same though the dimensions need not be the
  same.  The resultant image header will be a copy of the operand image
  with the greater dimension.  If the dimensions are the same then image
  header for the resultant image is copied from operand1.  The title of
  the resultant image may be changed using the parameter <i>title</i>.
  The pixel datatype for the resultant image may be set using the
  parameter <i>pixtype</i>.  If no pixel datatype is specified then the
  pixel datatype defaults to the calculation datatype given by the
  parameter <i>calctype</i>.  The calculation datatype defaults to the
  highest precedence datatype of the operand images or constants except
  that a division operation will default to real for integer images.
  The precedence of the datatypes, highest first, is double,
  real, long, integer, and short.  The datatype of a constant operand is
  either short integer or real.  A real constant has a decimal point.
  </p>
  <p>
  Arithmetic on images of unequal dimensions implies that the operation
  is repeated for each element of the higher dimensions.  For example
  subtracting a two dimensional image from a three dimensional image
  consists of subtracting the two dimensional image from each band of the
  three dimensional image.  This works for any combination of image
  dimensions.  As an extreme example dividing a seven dimensional image
  by a one dimension image consists of dividing each line of each plane
  of each band ... by the one dimensional image.
  </p>
  <p>
  There are two points to emphasize when using images of unequal
  dimensions.  First, a one dimensional image operates on a line
  of a two or higher dimension image.  To apply a one dimensional image
  to the columns of a higher dimensional image increase the image
  dimensionality with <b>imstack</b>, transpose the resultant image,
  and then replicate the columns with <b>blkrep</b> (see the EXAMPLE
  section).  The second point of confusion is that an image with a
  size given by <b>imheader</b> of [20,1] is a two dimensional image
  while an image with size of [20] is a one dimensional image.  To
  reduce the dimensionality of an image use <b>imcopy</b>.
  </p>
  <p>
  In addition to operating on the image pixels the image header parameters
  specified by the list <i>hparams</i> are also operated upon.  The operation
  is the same as performed on the pixels and the values are either the
  values associated with named header parameters or the operand constant
  values.  The primary purpose of this feature is to add exposure times
  when adding images.
  </p>
  <p>
  The verbose option is used to record the image arithmetic.  The output
  consists of the operator, the operand image names, the resultant image
  name and pixel datatype, and the calculation datatype.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To add two images and the exposure times:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imarith ccd1 + ccd2 sum
  &gt;&gt;&gt; hparams="itime,otime,ttime,exposure"
  </pre></div>
  <p>
  2. To subtract a constant from an image and replace input image by the
  subtracted image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imarith m31 - 223.2 m31
  </pre></div>
  <p>
  Note that the final pixel datatype and the calculation datatype will be at
  least of type real because the constant operand is real.
  </p>
  <p>
  3. To scale two exposures, divide one by the other, and extract the central
  portion:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imarith exp1[10:90,10:90] * 1.2 temp1
  cl&gt; imarith exp2[10:90,10:90] * 0.9 temp2
  cl&gt; imarith temp1 / temp2 final title='Ratio of exp1 and exp 2'
  cl&gt; imdelete temp1,temp2
  </pre></div>
  <p>
  Note that in this example the images temp1, temp2, and final will be
  of real pixel datatype (or double if either exp1 or exp2 are of pixel
  datatype double) because the numerical constants are real numbers.
  </p>
  <p>
  4. To divide two images of arbitrary pixel datatype using real arithmetic
  and create a short pixel datatype resultant image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imarith image1 / image2 image3 pixtype=short  \
  &gt;&gt;&gt; calctype=real title="Ratio of image1 and image2"
  </pre></div>
  <p>
  5. To divide several images by calibration image using the image pixel type of
  the numerator images to determine the pixel type of the calibrated images
  and the calculation arithmetic type:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imarith image1,image2,image3 / calibration \
  &gt;&gt;&gt; image1a,image2a,image3a pixtype=1 calctype=1
  </pre></div>
  <p>
  The same operation can be done in place with image template expansion by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imarith image* / calibration image* pixtype=1 calctype=1
  </pre></div>
  <p>
  6. To subtract a two dimensional bias from stacked observations (multiple
  two dimensional observations stacked to form a three dimensional image):
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imarith obs* - bias obs*//b
  </pre></div>
  <p>
  Note that the output observations obs101b, ..., will be three dimensional.
  </p>
  <p>
  7. To divide a 50 x 50 image by the average column:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; blkavg img avcol 50 1
  cl&gt; blkrep avcol avcol 50 1
  cl&gt; imarith img / avcol flat
  </pre></div>
  <p>
  8. To subtract a one dimensional image from the lines of a two dimensional
  image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imarith im2d - im1d diff
  </pre></div>
  <p>
  9. To subtract a one dimensional image from the columns of a two dimensional
  image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imstack im1d imcol
  cl&gt; imtranspose imcol imcol
  cl&gt; blkrep imcol imcol 100 1
  cl&gt; imarith im2d - imcol diff
  </pre></div>
  <p>
  Note the need to make a two dimensional image with each column
  replicated since a one dimensional image will operate on the lines
  of a two dimensional image.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  blkrep, imdivide, imfunction, imstack, imtranspose
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

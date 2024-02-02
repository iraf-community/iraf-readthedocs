.. _crosscor:

crosscor: Cross-correlate two images.
=====================================

**Package: fourier**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  crosscor input1 input2 output
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task performs a cross-correlation of 1- or 2-dimensional images.
  </p>
  <p>
  The input images will be padded with zeros,
  enlarging them to a size equal to the sum of
  the sizes of the input images (unless the parameter <span style="font-family: monospace;">"pad"</span> is set to
  no);
  the Fourier transform, product, and inverse transform
  are done using this larger region.
  If the input images have significantly non-zero values at their edges,
  there will be discontinuities between
  the edges of the original images and
  the rest of the image extended with zeros.
  These discontinuities constitute <span style="font-family: monospace;">"features"</span>
  which will bias the cross-correlation.
  Some value should therefore be subtracted from each input image
  to reduce these discontinuities.
  An appropriate value to subtract would be
  a mean of the pixel values near the edges.
  The 'taperedge' task may be used to taper the values near the edges.
  </p>
  <p>
  The discrete Fourier transform regards the first pixel as the <span style="font-family: monospace;">"origin,"</span>
  that is, zero angle or zero spatial frequency,
  and the fourier tasks follow this convention.
  In the case of 'crosscor',
  this means that two images of different size have zero shift
  if their features have the same pixel numbers,
  not that their features are the same distances from
  their respective image centers.
  </p>
  <p>
  If there is no shift between the two images input to 'crosscor',
  the peak in the output will be at the reference pixel,
  given by header keywords CRPIX1 and CRPIX2.
  </p>
  <p>
  Here are some details for interpreting the results in the case of
  a 1-dimensional image.
  </p>
  <div class="highlight-default-notranslate"><pre>
          SHIFT = X - CRPIX1
          DELTA = SHIFT * CDELT1 + CRVAL1
  
  Where:
          X  is the pixel number (not necessarily an integer)
             of the peak in the cross-correlation.
       SHIFT is the shift (in pixels) between the peak and the
             reference pixel, the position at which the peak
             would be located if the two images were identical.
       DELTA is the shift in physical units (same units as CRVAL1).
  
  Parameters in the output image:
      CRPIX1 is the reference pixel for the output image.
      CRVAL1 is the coordinate value at the reference pixel.
       CD1_1 is the increment in physical units
             from one pixel to the next.
  </pre></div>
  <p>
  A positive shift value means that the contents of
  'input1' must be shifted to a larger value of the
  independent variable in order to make 'input1' coincide with 'input2'.
  That is, suppose P1 and P2 are the pixel
  coordinates of the same feature in the first and second
  input files, respectively, then (P1 + SHIFT = P2).
  CRPIX1 is set to 1 if 'center=no', or (1 + npts/2) if 'center=yes'.
  If 'coord_shift=yes', then CRVAL1 is set
  to zero; otherwise CRVAL1 is set according to the
  coordinate information in the input images so that the
  expression above for DELTA will be correct.
  </p>
  <p>
  For 2-D transforms,
  this task has the option of using scratch images for intermediate results.
  Using scratch images may take longer,
  but it allows the task to function even with limited memory.
  If 'coord_shift' is yes, however, 'inmemory' must be set to no,
  so scratch images will always be used in the 2-D case
  if the option of adjust the images based on the coordinates is taken.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input1">
  <dt><b>input1 = <span style="font-family: monospace;">""</span> [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input1' Line='input1 = "" [file name]' -->
  <dd>Name of the first input data file.  This is considered
  to be the reference file or template.
  </dd>
  </dl>
  <dl id="l_input2">
  <dt><b>input2 = <span style="font-family: monospace;">""</span> [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input2' Line='input2 = "" [file name]' -->
  <dd>Name of the second input data file.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">""</span> [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = "" [file name]' -->
  <dd>Name of the output data file to be created by
  'crosscor'.
  </dd>
  </dl>
  <dl>
  <dt><b>(inreal1 = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inreal1 = yes) [boolean]' -->
  <dd>Use the real part of 'input1'?
  </dd>
  </dl>
  <dl>
  <dt><b>(inimag1 = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inimag1 = no) [boolean]' -->
  <dd>Use the imaginary part of 'input1'?
  </dd>
  </dl>
  <dl>
  <dt><b>(inreal2 = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inreal2 = yes) [boolean]' -->
  <dd>Use the real part of 'input2'?
  </dd>
  </dl>
  <dl>
  <dt><b>(inimag2 = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inimag2 = no) [boolean]' -->
  <dd>Use the imaginary part of 'input2'?
  </dd>
  </dl>
  <dl>
  <dt><b>(outreal = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outreal = yes) [boolean]' -->
  <dd>Save the real part of the output data file?
  </dd>
  </dl>
  <dl>
  <dt><b>(outimag = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outimag = no) [boolean]' -->
  <dd>Save the imaginary part of the output data file?
  </dd>
  </dl>
  <dl>
  <dt><b>(coord_shift = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(coord_shift = no) [boolean]' -->
  <dd>Adjust the relative positions of the input files based
  on their coordinate information?
  If the data values of the input files were identical,
  for example, but the coordinate values (CRVALi) at the
  reference pixels (CRPIXi) were not the same, then the
  result would not peak at the first pixel--it would be
  shifted based on the relative values of CRVALi in the
  two input files.
  If 'coord_shift=no', then the coordinate information is ignored.
  For 2-D images, 'coord_shift' and 'inmemory' must not both be set to yes.
  </dd>
  </dl>
  <dl>
  <dt><b>(center = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(center = yes) [boolean]' -->
  <dd>Shift the coordinate origin to the center of the output image?
  If the offset between the input images is small,
  then setting 'center=yes' will cause
  the peak of the cross-correlation to be
  near the middle of the output image.
  Note that if you set 'center=no' and 'chop=yes',
  then the peak may be on a portion of the image that is chopped off.
  </dd>
  </dl>
  <dl>
  <dt><b>(chop = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(chop = yes) [boolean]' -->
  <dd>Truncate the output file to the size of 'input1'?
  The cross-correlation is actually done on images that
  are larger than the input images;
  their size is the sum of the sizes of the two input images,
  and they are padded with zeros.
  If 'chop=no', then the output image(s) will be
  the same size as this enlarged image,
  but if 'chop=yes', then the output will be
  the size of the first input image.
  Note that for some images it is possible that truncating
  will cause the peak in the cross correlation to be chopped off.
  This is especially likely if 'center=no'.
  </dd>
  </dl>
  <dl>
  <dt><b>(pad = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(pad = no) [boolean]' -->
  <dd>If pad = yes (the default case) the correlation is done using an array
  which is the sum of the dimensions of each of the input arrays so that
  each of the input arrays may be padded with zeros to prevent
  <span style="font-family: monospace;">"wrap around"</span> effects. If pad = no then the correlation is done with an
  array size equal to the larger of the two dimensions for the input arrays.
  For large arrays this can lead to a reduction of a factor of 4 in the
  size of the working array, but it also allows <span style="font-family: monospace;">"wrap around"</span> effects so
  the user must use caution in overriding the default.
  </dd>
  </dl>
  <dl>
  <dt><b>(inmemory = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inmemory = yes) [boolean]' -->
  <dd>For two-dimensional input images,
  if 'inmemory = yes' the images will be read into two complex arrays,
  the Fourier transform will be performed on those arrays in-memory,
  the first array will be multiplied by the complex conjugate of the second,
  the inverse Fourier transform will be taken,
  and the array will be written to output images
  for the real and imaginary parts.
  This requires two complex words for each pixel.
  One complex array must fit entirely in memory (i.e. no paging)
  because when performing the Fourier transform
  each array is accessed both by rows and by columns.
  If 'inmemory = no', see the description of 'len_blk'.
  The parameters 'inmemory' and 'coord_shift'
  may not both be set to yes for 2-D images.
  For 1-D images, 'inmemory' is ignored.
  </dd>
  </dl>
  <dl>
  <dt><b>(len_blk = 256) [integer]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(len_blk = 256) [integer]' -->
  <dd>Length of block for transposing 2-D images.
  For 2-dimensional input images, if 'inmemory = no'
  this task transposes each image into scratch images
  before computing the forward and inverse
  Fourier transforms of the second axis.
  This parameter is the length of the side of a square region that is
  transposed in one step.
  The I/O buffers for scratch images can take a lot of memory
  if 'len_blk' is large, e.g., about 8 megabytes for 'len_blk = 512'.
  If you get out-of-memory errors,
  you should flush the process cache (flprcache),
  reduce the size of 'len_blk' and try again.
  This parameter is ignored for 1-D images or if 'inmemory = yes'.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>Print input and output image names?
  Setting 'verbose=yes' shows you the actual names of the image headers,
  including the <span style="font-family: monospace;">"r"</span> and <span style="font-family: monospace;">"i"</span> suffixes for real and imaginary parts.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Cross correlate the images <span style="font-family: monospace;">"file1.hhh"</span> and <span style="font-family: monospace;">"file2.hhh"</span>
  (both of which are real, with no imaginary part).
  Store the output in an image called <span style="font-family: monospace;">"xc.hhh"</span>.
  The output imaginary part will be zero, except for roundoff error,
  so don't keep it.
  </p>
  <div class="highlight-default-notranslate"><pre>
  fo&gt; crosscor file1 file2 xc
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Beginning with STSDAS version 1.3,
  the output from this task is the transpose of the complex conjugate
  of what it used to produce.
  The current output agrees with the definition of cross correlation
  as given by Bracewell.
  For input images with no imaginary part,
  the output is the transpose of the output from earlier versions,
  so the effect of this bug fix is to change the sign of the shift.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Bracewell, R.N.:  <span style="font-family: monospace;">"The Fourier Transform and Its Applications,"</span>
  McGraw-Hill Publishing Co., New York, 1986.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  taperedge, fconvolve
  </p>
  <p>
  Type <span style="font-family: monospace;">"help fourier opt=sys"</span> for a higher-level
  description of the 'fourier' package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

.. _forward:

forward: Compute forward Fourier transform of an image.
=======================================================

**Package: fourier**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  forward input output
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task computes the Fourier transform of a 1- or 2-dimensional image.
  The input may consist of both real and imaginary parts,
  or either part separately.
  </p>
  <p>
  The output of the 'forward' task is not normalized; for example,
  the first pixel of the output will be the sum of the input values.
  The 'inverse' task normalizes by dividing by the number of pixels,
  so applying 'forward' and then 'inverse' returns an image which is
  the same as the original, except for roundoff errors.
  </p>
  <p>
  The output coordinate parameters will be determined from the input parameters.
  Two additional header keywords,
  'OCRPIX1' and 'OCRVAL1', will be included in the output
  in order to save the original (i.e., input) values of
  'CRPIX1' and 'CRVAL1', respectively.
  These are used by the 'inverse' task to restore the original
  values of these keywords.
  For more information about the coordinate parameters,
  type <span style="font-family: monospace;">"help fourier option=sys"</span>.
  </p>
  <p>
  For 2-D transforms,
  this task has the option of using scratch images for intermediate results.
  Using scratch images may take longer,
  but it allows the task to function even with limited memory.
  </p>
  <p>
  It took approximately 104 seconds of CPU time (8:12 elapsed)
  on a VAX 8800 to transform a 1024 x 1024 real*4 image,
  using scratch images, rather than working in-memory.
  There was no input imaginary part,
  but both real and imaginary output parts were created.
  Working in-memory on a Sun IPX
  the transform took 26.4 seconds of CPU time (2:38 elapsed).
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name]' -->
  <dd>Name of the input data file.
  See also 'inreal' and 'inimag',
  which specify whether the real and imaginary parts are to be read.
  If both real and imaginary parts are to be read,
  the letters <span style="font-family: monospace;">"r"</span> and <span style="font-family: monospace;">"i"</span> will be appended to 'input'
  to form the names of the images for real and imaginary parts respectively.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name]' -->
  <dd>Name of the output data file created by 'forward'.
  If both real and imaginary parts are to be created,
  the letters <span style="font-family: monospace;">"r"</span> and <span style="font-family: monospace;">"i"</span> will be appended to 'output' to
  form the names of the images for real and imaginary parts respectively.
  </dd>
  </dl>
  <dl>
  <dt><b>(inreal = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inreal = yes) [boolean]' -->
  <dd>Use the real part of the input data file?  If this is set to yes,
  the real part must exist.
  </dd>
  </dl>
  <dl>
  <dt><b>(inimag = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inimag = no) [boolean]' -->
  <dd>Use the imaginary part of the input data file?  If this is set to yes,
  the imaginary part must exist.
  </dd>
  </dl>
  <dl>
  <dt><b>(outreal = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outreal = yes) [boolean]' -->
  <dd>Save the real part for the output data file?
  </dd>
  </dl>
  <dl>
  <dt><b>(outimag = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outimag = yes) [boolean]' -->
  <dd>Save the imaginary part for the output data file?
  </dd>
  </dl>
  <dl>
  <dt><b>(coord_shift = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(coord_shift = no) [boolean]' -->
  <dd>As indicated in the REFERENCES section,
  the discrete Fourier transform treats the first pixel
  of the image array as the coordinate origin,
  the zero point of time or of angular position in space, for example.
  If 'coord_shift=yes', then the origin for the input image
  is shifted to the location of the reference pixel of that image,
  as given by 'CRPIX1' (and 'CRPIX2' for a 2-D image).
  This is implemented by adding a linear function
  to the phase of the transformed image;
  the function is zero at the origin in the Fourier domain.
  The amplitude is not affected.
  If 'coord_shift=no', then the coordinate information is
  not used to modify the data values.
  For 2-D images, 'coord_shift' and 'inmemory' must not both be set to yes.
  </dd>
  </dl>
  <dl>
  <dt><b>(center = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(center = no) [boolean]' -->
  <dd>Shift the coordinate origin to the middle of the output image?
  </dd>
  </dl>
  <dl>
  <dt><b>(inmemory = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inmemory = yes) [boolean]' -->
  <dd>For a two-dimensional input image,
  if 'inmemory = yes' the image will be read into a complex array,
  the Fourier transform will be performed on that array in-memory,
  and the array will be written to output images
  for the real and imaginary parts.
  This requires one complex word for each pixel.
  The complex array must fit entirely in memory (i.e. no paging)
  because when performing the Fourier transform
  the array is accessed both by rows and by columns.
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
  before computing the Fourier transform of the second axis.
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
  including the <span style="font-family: monospace;">"r"</span> &amp; <span style="font-family: monospace;">"i"</span> suffixes for real &amp; imaginary parts.
  </dd>
  </dl>
  <dl>
  <dt><b>(ftpairs = fourier$ftpairs.dat) [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ftpairs = fourier$ftpairs.dat) [file name]' -->
  <dd>File defining 'CTYPE' transform pairs.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Take the forward Fourier transform of the image
  <span style="font-family: monospace;">"civ"</span> (no imaginary part) and put the output (both real
  and imaginary parts) in the images <span style="font-family: monospace;">"tr"</span> and <span style="font-family: monospace;">"ti"</span>,
  respectively.
  </p>
  <div class="highlight-default-notranslate"><pre>
  fo&gt; forward civ t inimag=no
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  If the task fails---due to lack of memory or disk space, for
  example---the output image and temporary
  images that were created are not deleted.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Bracewell, R.N.:  <span style="font-family: monospace;">"The Fourier Transform and Its Applications,"</span>
  McGraw-Hill Publishing Co., New York, 1986.
  </p>
  <p>
  The implementation of the Fourier transform in the 'forward' task
  differs from the definition given in Bracewell
  in that the output from this task is not normalized.
  In Bracewell the forward transform includes a 1/N factor,
  and we include that factor in the 'inverse' task instead.
  </p>
  <p>
  For a 1-D array g[t], the forward Fourier transform G[f] is
  </p>
  <div class="highlight-default-notranslate"><pre>
  G[f] = sum of g[t] * exp (-2*pi*i * t * f / N)
  from t=0 to t=N-1,
  </pre></div>
  <p>
  where the indexes t and f run from 0 to N-1.
  For a 2-D array, a 1-D transform is done for each row,
  and then the 1-D transform is done for each column.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  Type <span style="font-family: monospace;">"help fourier option=sys"</span> for a higher-level
  description of the 'fourier' package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

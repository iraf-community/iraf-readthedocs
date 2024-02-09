.. _inverse:

inverse: Compute inverse Fourier transform of an image.
=======================================================

**Package: fourier**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  inverse input output
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task computes the inverse Fourier transform of a 1- or 2-dimensional
  image.
  The input may consist of both the real and imaginary parts of an image,
  or either part independently.
  </p>
  <p>
  The 'forward' task does not normalize its output, but
  the 'inverse' task normalizes by dividing by the number of pixels.
  Applying 'forward' and then 'inverse' therefore returns an image
  which is the same as the original, except for roundoff errors.
  </p>
  <p>
  The output coordinate parameters will be determined from the input
  parameters and from the header keywords 'OCRPIX1' and 'OCRVAL1' in the
  input image, if present;
  these keywords were written by the 'forward' task, if it was used.
  </p>
  <p>
  For 2-D transforms,
  this task has the option of using scratch images for intermediate results.
  Using scratch images may take longer,
  but it allows the task to function even with limited memory.
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
  <dd>Name of the output data file.
  Both a real and an imaginary part will be created,
  but only the parts specified by the 'outreal' and 'outimag'
  will actually be saved.
  If both real and imaginary parts are to be saved,
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
  <dt><b>(inimag = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inimag = yes) [boolean]' -->
  <dd>Use the imaginary part of the input data file?  If this is set to yes,
  the imaginary part must exist.
  </dd>
  </dl>
  <dl>
  <dt><b>(outreal = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outreal = yes) [boolean]' -->
  <dd>Save the real part of the output data file?
  </dd>
  </dl>
  <dl>
  <dt><b>(outimag = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outimag = yes) [boolean]' -->
  <dd>Save the imaginary part of the output data file?
  </dd>
  </dl>
  <dl>
  <dt><b>(coord_shift = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(coord_shift = no) [boolean]' -->
  <dd>If 'coord_shift=yes', then the phase of the input image will be modified
  so as to shift the coordinate origin of the output image
  back to its original position,
  as given by the value of 'OCRPIX1' (and 'OCRPIX2' for a 2-D image).
  This is appropriate if the input image was derived from
  the output from 'forward', and 'forward.coord_shift=yes' was used.
  See the help for 'coord_shift' for the 'forward' task for more information.
  If 'coord_shift=no', then the coordinates will not
  affect the value of the inverse transform.
  The coordinate parameters are, however, still updated.
  For 2-D images, 'coord_shift' and 'inmemory' must not both be set to yes.
  </dd>
  </dl>
  <dl>
  <dt><b>(decenter = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(decenter = yes) [boolean]' -->
  <dd>The 'forward' task has the option of shifting the coordinate origin
  of the output image to the center,
  rather than leaving it at the first pixel.
  If this was done, then it is important to correct
  for that shift before doing an inverse transform.
  Setting 'decenter=yes' allows this correction.
  If 'forward.center=no' was used instead,
  then leaving 'inverse.decenter=yes' is harmless;
  therefore, the 'decenter' parameter should almost always be set to yes.
  The decentering is done using the value of the 'CRPIX1' keyword,
  which specifies the location of the coordinate origin
  in the Fourier domain.
  There is no option to center the output of the 'inverse' task,
  since that would not normally make sense.
  </dd>
  </dl>
  <dl>
  <dt><b>(inmemory = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inmemory = yes) [boolean]' -->
  <dd>For a two-dimensional input image,
  if 'inmemory = yes' the image will be read into a complex array,
  the inverse Fourier transform will be performed on that array in-memory,
  and the array will be written to the output image.
  This requires one complex word for each pixel.
  The complex array must fit entirely in memory (i.e. no paging)
  because when performing the inverse Fourier transform
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
  <dd>Length of block for transposing images.
  For 2-dimensional input images, if 'inmemory = no'
  this task transposes each image into scratch images
  before computing the inverse Fourier transform of the second axis.
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
  <dd>Name of the file that defines the type of coordinate in
  a transform pair.  For example, <span style="font-family: monospace;">"LAMBDA"</span>, <span style="font-family: monospace;">"WAVENUMB"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Take the inverse Fourier transform of the images <span style="font-family: monospace;">"tr"</span>
  and <span style="font-family: monospace;">"ti"</span> (i.e., the real and imaginary parts) and put
  the output real part in an image called
  <span style="font-family: monospace;">"civ"</span>--the imaginary part is discarded.
  </p>
  <div class="highlight-default-notranslate"><pre>
  fo&gt; inverse t civ outimag=no
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  If the task fails due to lack of memory or disk space, for example,
  the output image and temporary images that were created are not deleted.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Bracewell, R.N.:  <span style="font-family: monospace;">"The Fourier Transform and Its Applications,"</span>
  McGraw-Hill Publishing Co., New York, 1986.
  </p>
  <p>
  The implementation of the inverse Fourier transform in the 'inverse' task
  differs from the definition given in Bracewell
  in that the output from this task is normalized
  by dividing by the total number of pixels.
  Bracewell includes the normalization in the forward transform instead.
  </p>
  <p>
  For a 1-D array G[f], the inverse Fourier transform g[t] is
  </p>
  <div class="highlight-default-notranslate"><pre>
  g[t] = (1/N) * sum of G[f] * exp (2*pi*i * t * f / N)
  from f=0 to f=N-1,
  </pre></div>
  <p>
  where the indexes f and t run from 0 to N-1.
  For a 2-D array, a 1-D transform is done for each row,
  and then the 1-D transform is done for each column.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  forward
  </p>
  <p>
  Type <span style="font-family: monospace;">"help fourier opt=sys"</span> for a higher-level
  description of the 'fourier' package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

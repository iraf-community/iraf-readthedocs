fourier: Fourier analysis.
==========================

.. toctree:: :maxdepth: 1

   crosscor
   forward
   inverse
   taperedge
.. raw:: html

  <p>
  This package contains tasks for taking the forward or
  inverse Fourier transforms---or for using the Fourier
  transform to compute a power spectrum or perform a cross
  correlation or convolution.
  These tasks currently operate only on images,
  not on tables or lists.
  Data are assumed to be equally spaced.
  </p>
  <p>
  Rather than using complex data type for input and output images,
  tasks in the 'fourier' package adopt the convention that
  the real and imaginary parts are kept in separate images.
  In many cases there will only be a real part,
  and there may only be an imaginary part.
  The user sets the flags 'inreal' &amp; 'inimag' and 'outreal' &amp; 'outimag'
  to specify which parts are to be read as input and created as output.
  When both real and imaginary parts are to be read or written,
  the characters <span style="font-family: monospace;">"r"</span> and <span style="font-family: monospace;">"i"</span> will be appended to the
  root portion of the name specified by the user
  to obtain the actual names of the real and imaginary parts respectively.
  When only the real part or only the imaginary part
  is to be read or written,
  the name specified by the user is taken without modification.
  </p>
  <p>
  The Fourier transform is done in single-precision real
  arithmetic.  The output image is created as a <span style="font-family: monospace;">"new copy"</span>
  of the input, but the output data type is set to real
  regardless of the input data type.  This was done because
  of integer overflow problems with images of type integer or short.
  </p>
  <p>
  A frequently asked question about tasks in the 'fourier' package is,
  <span style="font-family: monospace;">"Which pixel receives the DC signal when taking a forward transform
  or power spectrum?  That is,
  which pixel is zero frequency?"</span>  Zero frequency is at the reference pixel,
  which is given by the value of CRPIX1 (or CRPIX1 &amp; CRPIX2 for a 2-D image).
  This will be pixel 1 (or [1,1] for 2-D)
  if the 'center' parameter was set to no.
  If center=yes,
  the reference pixel will be at [N/2] + 1,
  where N is the length of an image axis.
  The brackets indicate truncation to an integer.
  </p>
  <p>
  The coordinate parameters of the input image are used to compute
  appropriate coordinate parameters for the output image.
  This makes it straightforward to associate a <span style="font-family: monospace;">"world coordinate"</span>
  value with any pixel in the output image.
  For an image produced by the 'forward' or 'powerspec' task,
  the world coordinate at a pixel is the frequency in physical units,
  such as cycles per second.
  As an example,
  consider an image N pixels long with pixel spacing of D seconds per pixel.
  The pixel spacing in the Fourier domain is 1/(N*D) Hz per pixel.
  Suppose the input image contains a periodic signal with period P pixels,
  which is P*D seconds.
  The periodic signal results in a peak in the Fourier domain
  at N/P pixels from the reference pixel.
  The world coordinate (frequency in cycles/sec, in this example) at a pixel
  is the offset from the reference pixel multiplied by the pixel spacing,
  or (N/P) * 1/(N*D) = 1/(P*D) Hz,
  as you would expect for a period of P*D seconds.
  </p>
  <p>
  For a two-dimensional image the pixel spacing changes independently in
  each dimension.
  If the length and pixel spacing are N1 &amp; D1 for the first image axis
  and N2 &amp; D2 for the second image axis,
  then the pixel spacing in the Fourier domain is 1/(N1*D1) for the first
  axis and 1/(N2*D2) for the second axis.
  In general, therefore, the coordinate axes will not be orthogonal
  in the Fourier domain.
  The output CD matrix is obtained by multiplying the input CD matrix
  on the right by the matrix
  </p>
  <div class="highlight-default-notranslate"><pre>
  | 1/(N1*D1**2)       0       |
  |                            |
  |      0        1/(N2*D2**2) |
  </pre></div>
  <!-- Contents:  -->
  

.. _ricepack:

ricepack: Rice compress a FITS file
===================================

**Package: fitsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ricepack images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>A list of images.  The input may be FITS or MEF FITS, or either of these
  gzip-compressed ('.gz'), or may be IRAF '.imh' images.
  </dd>
  </dl>
  <dl id="l_keep">
  <dt><b>keep = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='keep' Line='keep = no' -->
  <dd>Preserve the input images?  By default the input files will be replaced
  by the corresponding tile compressed FITS files.
  </dd>
  </dl>
  <dl id="l_listonly">
  <dt><b>listonly = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listonly' Line='listonly = no' -->
  <dd>List the types and contents (FITS HDUs) of the input files?
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print each operation as it takes place?  Data volume and timing will
  also be reported.
  </dd>
  </dl>
  <dl id="l_quantization">
  <dt><b>quantization = 16</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='quantization' Line='quantization = 16' -->
  <dd>Floating point pixels will be quantized (see discussion below) to
  the background noise divided by the <b>quantization</b> parameter.
  </dd>
  </dl>
  <dl id="l_nimages">
  <dt><b>nimages</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nimages' Line='nimages' -->
  <dd>[Output] The number of images in the input list.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The RICEPACK task will compress a list of images.  The input may be
  FITS or MEF FITS, may be gzip compressed copies of either type of FITS
  files, or may be IRAF <span style="font-family: monospace;">".imh"</span> images.  The output file names will be
  compressed FITS with <span style="font-family: monospace;">".fits.fz"</span> appended.
  </p>
  <p>
  This task is a wrapper script for the CFITSIO fpack command (see [1]).
  RICEPACK implements the FITS tile compression standard[3].  This well
  established FITS convention has several features that make it preferable
  to host file compression such as gzip:  1) Rectangular image
  tiles are separately compressed to preserve rapid random access to the
  image pixels.  2) The FITS headers remain uncompressed for ease of read/write
  access.  3) Individual FITS image extensions (HDUs) are compressed
  separately.
  </p>
  <p>
  FITS tile compression supports multiple compression algorithms.
  The IRAF RICEPACK task by default implements Rice compression.  Compression
  of integer-valued images will be lossless.  The Rice algorithm realizes
  a near optimal compression factor[2] and is much faster than alternatives
  like gzip.  Example 2 describes how to override the choice of algorithm
  using the <b>flags</b> parameter.
  </p>
  <p>
  The <b>keep</b> parameter offers the option of retaining the original
  input files.  By default the IRAF RICEPACK task replaces the input files
  with the output compressed files (else the action of compressing the
  image list would actually consume additional diskspace).  This is
  different than the default behavior of the CFITSIO fpack command.
  </p>
  <p>
  The <b>listonly</b> and <b>verbose</b> control the amount of information
  listed.  If <b>listonly</b> is set to yes, the input data files will
  remain untouched and no compressed output will be created.  If
  <b>verbose</b> is set to no, the task will operate silently.
  </p>
  <p>
  The number of images processed will be reported on output as the value
  of  the <b>nimages</b> parameter.
  </p>
  </section>
  <section id="s_floating_point_handling">
  <h3>Floating point handling</h3>
  <p>
  The compression of floating point data presents a notorious challenge.
  This is as true for astronomical data as for any other.  Compression
  ratios are typically small for such data.  At the same time, floating
  point data often retain unwarranted false precision.  For example, if the
  input of a standard CCD processing pipeline is 16-bit integers, then
  generating 32-bit output is to claim roughly double the precision intrinsic
  to the raw data.
  </p>
  <p>
  A widely adopted solution is to rescale the floating point data into
  an integer range more appropriate to the actual data.  The RICEPACK task
  accomplishes this using the <b>quantization</b> parameter, which
  represents the number of levels into which the measured one-sigma
  background will be divided.  The default value of 16 (see [2] and
  included references) has been shown to have a negligible effect (for
  typical purposes) on derived photometric and astrometric results.
  </p>
  <p>
  Also, bear in mind that the poisson statistics of most astronomical
  detectors means that sampling the background noise into 16 such bins
  may result in oversampling the bright end of the dynamic range by a
  factor of several hundred.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Tile compress a file using the default Rice algorithm
  </p>
  <div class="highlight-default-notranslate"><pre>
  fitsutil&gt; ricepack file3.fits
  </pre></div>
  <p>
     The output file is: file3.fits.fz
  </p>
  <p>
  2. Compress a mixed list of images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  fitsutil&gt; ricepack *.fits,*.imh,*.fits.gz
  </pre></div>
  <p>
  3. Compress a file and retain the original:
  </p>
  <div class="highlight-default-notranslate"><pre>
  fitsutil&gt; ricepack file4.fits keep+
  </pre></div>
  <p>
  4. Uncompress gzipped files and recompress using Rice in one step:
  </p>
  <div class="highlight-default-notranslate"><pre>
  fitsutil&gt; ricepack *.gz
  1.1.3 (March 2009) CFITSIO version  3.140
  
  Wed 15:31:50 19-Aug-2009
  kp1016311.fits.gz -&gt; kp1016311.fits.fz
          ...
  kp1016429.fits.gz -&gt; kp1016429.fits.fz
  Wed 15:31:58 19-Aug-2009
  
  63 images, 0.13 seconds each, 0:00:08.0 elapsed
  
   input:      56.550 MB
  output:      45.701 MB
   saved:      10.849 MB, 19%
  
  relative R = 1.24
  </pre></div>
  <p>
  The Rice compressed files save 19% of the space (10.849 MB in this case)
  required for the gzip files; the relative compression ratio is 1.24
  (output/input).
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  funpack
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  [1] http://heasarc.gsfc.nasa.gov/fitsio/fpack
  </p>
  <p>
  [2] http://arxiv.org/abs/0903.2140
  </p>
  <p>
  [3] http://fits.gsfc.nasa.gov/registry/tilecompression.html
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'FLOATING POINT HANDLING' 'EXAMPLES' 'SEE ALSO' 'REFERENCES'  -->
  

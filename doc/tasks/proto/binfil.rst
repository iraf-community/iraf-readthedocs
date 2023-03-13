.. _binfil:

binfil: Create a binary file from an IRAF image
===============================================

**Package: proto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  binfil input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input images to be converted.
  </dd>
  </dl>
  <dl id="l_scale_fact">
  <dt><b>scale_fact = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale_fact' Line='scale_fact = 1.0' -->
  <dd>A multiplicative scale factor to be applied to each pixel during the
  conversion process.  This parameter provides the means to minimize loss
  of precision when converting from the dynamic range of the IRAF image
  pixels to the dynamic range of the output 16-bit signed integer,
  -32768 to 32767.
  </dd>
  </dl>
  <dl id="l_header">
  <dt><b>header = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='header' Line='header = no' -->
  <dd>Prepend a short descriptive header to the output binary raster file?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  BINFIL generates a simple signed 16-bit binary raster file
  from IRAF images. BINFIL can be useful when programs other than IRAF
  applications are to be used to examine the data. The format of the resulting
  file is a simple string of pixels, with the exception that the first
  90 bytes or 45 words may optionally form a minimal header. 
  </p>
  <p>
  The header elements are stored as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  word 1    : nrows
  word 2    : ncols
  word 3    : IRAF pixel type flag
  word 4-13 : reserved space
  word 14-45: image title (ASCII 64 bytes)
  </pre></div>
  <p>
  Pixels from the input images are converted to short integers after scaling
  by the scale_fact parameter. The resultant pixel values are limited to the
  maximum range of a short integer and then written to the binary file.
  </p>
  <p>
  The output binary file assumes the name of the input image with an appended
  <span style="font-family: monospace;">".b"</span> to indicate binary.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Convert the IRAF image irafimage to the binary file irafimage.b.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; binfil irafimage scale=0.01
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Only the first 64 characters of the image title are placed in the binary file
  header.
  </p>
  <p>
  There is no way to specify the output binary file names.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  irafil
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _badpiximage:

badpiximage: Create a bad pixel mask image from a bad pixel file
================================================================

**Package: ccdred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  badpiximage fixfile template image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_fixfile">
  <dt><b>fixfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fixfile' Line='fixfile' -->
  <dd>Bad pixel file.
  </dd>
  </dl>
  <dl id="l_template">
  <dt><b>template</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='template' Line='template' -->
  <dd>Template image used to define the size of the bad pixel mask image.
  </dd>
  </dl>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Bad pixel mask image to be created.
  </dd>
  </dl>
  <dl id="l_goodvalue">
  <dt><b>goodvalue = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='goodvalue' Line='goodvalue = 1' -->
  <dd>Integer value assigned to the good pixels.
  </dd>
  </dl>
  <dl id="l_badvalue">
  <dt><b>badvalue = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='badvalue' Line='badvalue = 0' -->
  <dd>Integer value assigned to the bad pixels.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A bad pixel mask image is created from the specified bad pixel file.
  The format of the bad pixel file is that used by <b>ccdproc</b> to
  correct CCD defects (see instruments).  The bad pixel image is of pixel type short and
  has the value given by the parameter <b>goodvalue</b> for the good
  pixels and the value given by the parameter <b>badvalue</b> for the bad pixels.
  The image size and header parameters are taken from the specified
  template image.  The bad pixel mask image may be used to view the
  location of the bad pixels and blink against an data image using an
  image display, to mask or flag bad pixels later by image arithmetic,
  and to propagate the positions of the bad pixels through the
  reductions.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To make a bad pixel mask image from the bad pixel file <span style="font-family: monospace;">"cryocambp.dat"</span>
  using the image <span style="font-family: monospace;">"ccd005"</span> as the template:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; badpiximage cryocambp.dat ccd005 cryocambp
  </pre></div>
  <p>
  2. To make the bad pixel mask image with good values of 0 and bad values of 1:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; badpixim cryomapbp.dat ccd005 cryocambp good=0 bad=1
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ccdproc, instruments
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

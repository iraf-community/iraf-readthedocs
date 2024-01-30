.. _mkimage:

mkimage: Make or modify an image with simple values
===================================================

**Package: ccdtest**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkimage image option value [ndim dims]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>Image to create or modify.
  </dd>
  </dl>
  <dl id="l_option">
  <dt><b>option</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='option' Line='option' -->
  <dd>Editing option which is one of the following:
  <dl>
  <dt><b>make</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='make' Line='make' -->
  <dd>Make a new image of the specified size, dimensionality, pixel type, and values.
  </dd>
  </dl>
  <dl>
  <dt><b>replace</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='replace' Line='replace' -->
  <dd>Replace pixel values in the image.
  </dd>
  </dl>
  <dl>
  <dt><b>add</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='add' Line='add' -->
  <dd>Add to the pixel values in the image.
  </dd>
  </dl>
  <dl>
  <dt><b>multiply</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='multiply' Line='multiply' -->
  <dd>Multiply the pixel values in the image.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_value">
  <dt><b>value</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='value' Line='value' -->
  <dd>Mean pixel value to be used.
  </dd>
  </dl>
  <dl id="l_ndim">
  <dt><b>ndim</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ndim' Line='ndim' -->
  <dd>Number of dimensions when creating a new image.
  </dd>
  </dl>
  <dl id="l_dims">
  <dt><b>dims</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dims' Line='dims' -->
  <dd>Image dimensions given as a white space separated string (see the examples).
  </dd>
  </dl>
  <dl id="l_pixtype">
  <dt><b>pixtype = <span style="font-family: monospace;">"real"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pixtype' Line='pixtype = "real"' -->
  <dd>Pixel datatype when creating an image.  The types are <span style="font-family: monospace;">"real"</span>, <span style="font-family: monospace;">"short"</span>,
  <span style="font-family: monospace;">"integer"</span>, <span style="font-family: monospace;">"long"</span>, and <span style="font-family: monospace;">"double"</span>.
  </dd>
  </dl>
  <dl id="l_slope">
  <dt><b>slope = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='slope' Line='slope = 0.' -->
  <dd>Slope of pixel values per pixel.
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma' Line='sigma = 0.' -->
  <dd>Gaussian noise of pixel values if not zero.
  </dd>
  </dl>
  <dl id="l_seed">
  <dt><b>seed = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='seed' Line='seed = 0' -->
  <dd>Seed for random numbers.  If zero then the first time the task is
  called a seed of 1 is used and all subsequent calls while the task is in
  the process cache continue with new random numbers.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  An image is created or modified using simple values.  This task is intended
  for test and demonstration purposes.  A image may be created of a specified
  size, dimensionality, and pixel datatype.  The pixel values used in creating
  or editing an image consist of a sloped plane (which repeats for dimensions
  greater than 2) with pseudo-Gaussian noise. The sloped plane is defined such
  that:
  </p>
  <p>
     pix[i,j] = value + slope * ((ncols + nlines) / 2 - 1) + slope * (i + j)
  </p>
  <p>
  where i and j are the pixel indices (starting with 1) and ncols and nlines
  are the number of columns and lines.  The interpretation of <span style="font-family: monospace;">"value"</span> is that
  it is the mean of the plane.  The Gaussian noise is only approximately random
  for purposes of speed!
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To create an 2 dimensional real image of size 100 x 200 with all zero
  values:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkimage name make 0 2 "100 200"
  </pre></div>
  <p>
  Note that the dimension string is quoted because of the blank separated
  values.
  </p>
  <p>
  2. To add noise with a sigma of 5:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkimage name add 0 sigma=5
  </pre></div>
  <p>
  2. To replace a region of the image with the value 10:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkimage name[10:20,30:40] replace 10
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  artobs, subsection
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

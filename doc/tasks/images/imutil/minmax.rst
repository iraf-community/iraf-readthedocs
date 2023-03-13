.. _minmax:

minmax: Compute the minimum and maximum pixel values in an image
================================================================

**Package: imutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  minmax images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>Image template specifying the images to be examined.
  </dd>
  </dl>
  <dl id="l_force">
  <dt><b>force = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='force' Line='force = no' -->
  <dd>Force recomputation of the minimum and maximum pixel and pixel values even if
  they are noted as up to date in the image header.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = yes' -->
  <dd>Update the image header with the new values (requires write permission).
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print the image name, minimum value, and maximum value of each image
  processed.
  </dd>
  </dl>
  <dl id="l_minval">
  <dt><b>minval = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minval' Line='minval = INDEF' -->
  <dd>Set to the minimum pixel value of the last image processed.
  If the pixel type of the last input image was complex, this is the real
  part of the minimum value.
  </dd>
  </dl>
  <dl id="l_maxval">
  <dt><b>maxval = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxval' Line='maxval = INDEF' -->
  <dd>Set to the maximum pixel value of the last image processed.
  If the pixel type of the last input image was complex, this is the real
  part of the maximum value.
  </dd>
  </dl>
  <dl id="l_iminval">
  <dt><b>iminval = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='iminval' Line='iminval = INDEF' -->
  <dd>Set to the minimum imaginary part of the pixel value of the last image
  processed. Only used if the pixel type of the last input image was complex.
  </dd>
  </dl>
  <dl id="l_imaxval">
  <dt><b>imaxval = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imaxval' Line='imaxval = INDEF' -->
  <dd>Set to the maximum imaginary part of the pixel value of the last image
  processed. Only used if the pixel type of the last input image was complex.
  </dd>
  </dl>
  <dl id="l_minpix">
  <dt><b>minpix = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minpix' Line='minpix = ""' -->
  <dd>Set to the minimum pixel specification of the last image processed.
  </dd>
  </dl>
  <dl id="l_maxpix">
  <dt><b>maxpix = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxpix' Line='maxpix = ""' -->
  <dd>Set to the maximum pixel specification of the last image processed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
      The <i>minmax</i> task computes the minimum and maximum pixel and pixel
  values of
  each of the images or image sections listed in the image template <i>images</i>.
  If the <i>force</i> option is set the extreme values will be recomputed by
  physical examination of the data, otherwise the image is examined only if the
  extreme values stored in the image header are flagged as invalid.
  The minimum and maximum pixel will be printed only if the force option
  is enabled or if the image minimum and maximum is out of date. 
  If the <i>update</i> option is set the image header will be updated with the
  newly computed values.  Updating is not allowed when a section is used to
  compute the new values.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute and print the minimum and maximum values of the images <i>image1</i>
  and <i>image2</i>, updating the image header with the new values when done.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; minmax image1,image2
  </pre></div>
  <p>
  2. Force update the minimum and maximum values in the image headers of all
  images matching the template in the background, without printing the computed
  values on the terminal.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; minmax nite1.* force+ verbose- &amp;
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The minimum and maximum pixel values are stored in the image header as values
  of type real, hence some precision may be lost for images of type long integer
  or double precision floating.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imheader, hedit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

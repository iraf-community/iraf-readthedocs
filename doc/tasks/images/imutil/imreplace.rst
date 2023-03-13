.. _imreplace:

imreplace: Replace a range of pixel values with a constant
==========================================================

**Package: imutil**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  imreplace images value lower upper
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>Images in which the pixels are to be replaced.
  </dd>
  </dl>
  <dl id="l_value">
  <dt><b>value</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='value' Line='value' -->
  <dd>Replacement value for pixels in the window.
  </dd>
  </dl>
  <dl id="l_imaginary">
  <dt><b>imaginary = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imaginary' Line='imaginary = 0.' -->
  <dd>Replacement value for pixels in the windoe for the imaginary part of
  complex data.
  </dd>
  </dl>
  <dl id="l_lower">
  <dt><b>lower = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lower' Line='lower = INDEF' -->
  <dd>Lower limit of window for replacing pixels.  If INDEF then all pixels
  are above <i>lower</i>.  For complex images this is the magnitude
  of the pixel values.  For integer images the value is rounded up
  to the next higher integer.
  </dd>
  </dl>
  <dl id="l_upper">
  <dt><b>upper = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='upper' Line='upper = INDEF' -->
  <dd>Upper limit of window for replacing pixels.  If INDEF then all pixels
  are below <i>upper</i>.  For complex images this is the magnitude
  of the pixel values.  For integer images the value is rounded down
  to the next lower integer.
  </dd>
  </dl>
  <dl id="l_radius">
  <dt><b>radius = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radius' Line='radius = 0.' -->
  <dd>Additional replacement radius around pixels which are in the replacement
  window.  If a pixel is within this distance of a pixel within the replacement
  window it is also replaced with the replacement value.  Distances are
  measured between pixel centers which are have integer coordinates.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The pixels in the <i>images</i> between <i>lower</i> and <i>upper</i>,
  and all other pixels with a distance given by <i>radius</i>,
  are replaced by the constant <i>value</i>.  The special value INDEF in
  <i>lower</i> and <i>upper</i> corresponds to the minimum and maximum
  possible pixel values, respectively.
  </p>
  <p>
  For complex images the replacement value is specified as separate
  real and imaginary and the thresholds are the magnitude.  For
  integer images the thresholds are used as inclusive limits
  so that, for example, the range 5.1-9.9 affets pixels 6-9.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. In a flat field calibration which has been scaled to unit mean replace
  all response values less than or equal to 0.8 by 1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imreplace calib 1 upper=.8
  </pre></div>
  <p>
  2. Set all pixels to zero within a section of an image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imreplace image[1:10,5:100] 0
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_IMREPLACE">
  <dt><b>IMREPLACE V2.11.1</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IMREPLACE' Line='IMREPLACE V2.11.1' -->
  <dd>A replacement radius to replace additional pixels was added.
  </dd>
  </dl>
  <dl id="l_IMREPLACE">
  <dt><b>IMREPLACE V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IMREPLACE' Line='IMREPLACE V2.11' -->
  <dd>The lower value is now rounded up for integer images so that a range
  like 5.1-9.9 affects pixels 6-9 instead of 5-9.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imexpr
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

.. _imfunction:

imfunction: Apply a single argument function to a list of images
================================================================

**Package: imutil**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  imfunction input output function
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The input image list.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output image list. The number of output images must match the number of
  input images. If the output image list equals the input image list
  the input images are overwritten.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function' -->
  <dd>Function to be applied to the input pixels. The options are:
  <dl>
  <dt><b>log10</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='log10' Line='log10' -->
  <dd>Take the logarithm to base 10 of an image. Negative and zero-valued
  pixels will be assigned the value -MAX_EXPONENT.
  </dd>
  </dl>
  <dl>
  <dt><b>alog10</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='alog10' Line='alog10' -->
  <dd>Taken the antilogarithm to base 10 of the image. Positive out-of-bounds
  pixel values will be assigned the value MAX_REAL, negative out-of-bounds
  pixel values will be assigned the value 0.0.
  </dd>
  </dl>
  <dl>
  <dt><b>ln   </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='ln' Line='ln   ' -->
  <dd>Take the natural logarithm of an image. Negative and zero-valued pixels
  will be assigned the value - ln (10.) * MAX_EXPONENT.
  </dd>
  </dl>
  <dl>
  <dt><b>aln   </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='aln' Line='aln   ' -->
  <dd>Take the antilogarithm to base e of an image. Positive out-of-bounds pixel
  values will be assigned the value MAX_REAL, negative out-of-bounds
  pixel values will be assigned the value 0.0
  </dd>
  </dl>
  <dl>
  <dt><b>sqrt</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='sqrt' Line='sqrt' -->
  <dd>Take the square root of an image. Negative pixel values will be assigned
  the value 0.0.
  </dd>
  </dl>
  <dl>
  <dt><b>square</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='square' Line='square' -->
  <dd>Take the square of an image.
  </dd>
  </dl>
  <dl>
  <dt><b>cbrt</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='cbrt' Line='cbrt' -->
  <dd>Take the cube root of an image.
  </dd>
  </dl>
  <dl>
  <dt><b>cube</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='cube' Line='cube' -->
  <dd>Take the cube of an image.
  </dd>
  </dl>
  <dl>
  <dt><b>abs  </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='abs' Line='abs  ' -->
  <dd>Take the absolute value of an image.
  </dd>
  </dl>
  <dl>
  <dt><b>neg  </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='neg' Line='neg  ' -->
  <dd>Take the negative of an image.
  </dd>
  </dl>
  <dl>
  <dt><b>cos  </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='cos' Line='cos  ' -->
  <dd>Take the cosine of an image.
  </dd>
  </dl>
  <dl>
  <dt><b>sin  </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='sin' Line='sin  ' -->
  <dd>Take the sine of an image.
  </dd>
  </dl>
  <dl>
  <dt><b>tan  </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='tan' Line='tan  ' -->
  <dd>Take the tangent of an image.
  </dd>
  </dl>
  <dl>
  <dt><b>acos</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='acos' Line='acos' -->
  <dd>Take the arc-cosine of an image. The output pixels will lie between
  0.0 and PI.
  </dd>
  </dl>
  <dl>
  <dt><b>asin</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='asin' Line='asin' -->
  <dd>Take the arc-sine of an image. The output pixels will lie between -PI/2
  and +PI/2.
  </dd>
  </dl>
  <dl>
  <dt><b>atan</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='atan' Line='atan' -->
  <dd>Take the arc-tangent of an image. The output pixels will lie between
  -PI/2 and +PI/2.
  </dd>
  </dl>
  <dl>
  <dt><b>hcos</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='hcos' Line='hcos' -->
  <dd>Take the hyperbolic cosine of an image. Positive or negative
  out-of-bounds pixels will be assigned the value MAX_REAL.
  </dd>
  </dl>
  <dl>
  <dt><b>hsin</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='hsin' Line='hsin' -->
  <dd>Take the hyperbolic sine of an image. Positive and negative out-of-bounds
  pixel values will be assigned the values MAX_REAL and -MAX_REAL respectively.
  </dd>
  </dl>
  <dl>
  <dt><b>htan</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='htan' Line='htan' -->
  <dd>Take the hyperbolic tangent of an image.
  </dd>
  </dl>
  <dl>
  <dt><b>reciprocal</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='reciprocal' Line='reciprocal' -->
  <dd>Take the reciprocal of an image. Zero-valued pixels will be assigned
  the output value 0.0
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about actions taken by the task?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The selected function <i>function</i> is applied to the pixel values of all
  the input images <i>input</i> to create the pixel values of the output
  images <i>output</i>. The number of output images must equal the number of
  input images. If the output image name is the same as the input image name
  the input image will be overwritten.
  </p>
  <p>
  If the input image is type real or double the output image will
  be of type real or double respectively. If the input image is type
  ushort then the output image will be type real. If the input image is one of
  the remaining integer data types, then the output image will be type
  real, unless function is <span style="font-family: monospace;">"abs"</span> or <span style="font-family: monospace;">"neg"</span>, in which case the output
  data type will be the same as the input data type.
  </p>
  <p>
  Values of the machine dependent constants MAX_REAL and MAX_EXPONENT can be
  found in the file <span style="font-family: monospace;">"hlib$mach.h"</span>. 
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Take the logarithm of the pixel values of images in1 and in2 and write
  the results to out1 and out2.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; imfunction in1,in2 out1,out2 log10
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imarith,imreplace
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

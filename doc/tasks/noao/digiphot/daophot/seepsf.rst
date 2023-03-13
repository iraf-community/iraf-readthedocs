.. _seepsf:

seepsf: Compute an image from the point spread function
=======================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  seepsf psfimage image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_psfimage">
  <dt><b>psfimage</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='psfimage' Line='psfimage' -->
  <dd>The list of input PSF images computed by the PSF task. Each PSF image consists
  of the parameters of a 2D analytic function stored in the image header and an
  optional sampled lookup table of residuals from that fit stored in the image
  pixels.
  </dd>
  </dl>
  <dl id="l_image">
  <dt><b>image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='image' Line='image' -->
  <dd>The list of output PSF images consisting of the sum of the analytic function
  and the residuals in the lookup table. There must be one output PSF image for
  each input PSF image.
  </dd>
  </dl>
  <dl id="l_dimension">
  <dt><b>dimension = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dimension' Line='dimension = INDEF' -->
  <dd>The dimensions of the output PSF image. By default <i>image</i> is a 2D image
  with dimensions of N by N where N = 2 * nint (psfrad / scale)  + 1 with the
  same scale as the original image from which <i>psfimage</i> was derived.
  <i>Psfrad</i> is the PSF fitting radius stored in the <i>psfimage</i> image
  header parameter <span style="font-family: monospace;">"PSFRAD"</span>. <i>Scale</i> is the image scale stored in the image
  header parameter <span style="font-family: monospace;">"SCALE"</span>.
  </dd>
  </dl>
  <dl id="l_xpsf">
  <dt><b>xpsf = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xpsf' Line='xpsf = INDEF' -->
  <dd>The x coordinate of the output PSF. <i>Xpsf</i> is only used if <i>psfimage</i>
  was computed with the variable PSF parameter <i>varorder</i> in the DAOPARS task
  set to &gt; 0.
  </dd>
  </dl>
  <dl id="l_ypsf">
  <dt><b>ypsf = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ypsf' Line='ypsf = INDEF' -->
  <dd>The y coordinate of the output PSF. <i>Ypsf</i> is only used if <i>psfimage</i>
  was computed with the variable PSF parameter <i>varorder</i> in the DAOPARS task
  set to &gt; 0.
  </dd>
  </dl>
  <dl id="l_magnitude">
  <dt><b>magnitude = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='magnitude' Line='magnitude = INDEF' -->
  <dd>The intensity scale of the output PSF. By default the intensity scale is set by
  the magnitude of the first star used by the PSF task to compute <i>psfimage</i>.
  This parameter is stored in the keyword <span style="font-family: monospace;">"PSFMAG"</span> in <i>psfimage</i>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  SEEPSF takes the input PSF <i>psfimage</i> computed by the PSF task, consisting
  of the parameters of a 2D analytic function stored in the image header and an
  optional lookup table of residuals from the fit stored in the image pixels, and
  computes an output PSF, <i>image</i>, consisting of the sum of the analytic
  function and the residuals.
  </p>
  <p>
  By default <i>image</i> is a 2D image of dimensions N by N where N = 2 * nint
  (psfrad) + 1 and the scale of <i>image</i> is the same as the scale of the
  original image from which <i>psfimage</i>  was derived. If <i>dimension</i> is
  greater or less than N then the output PSF is block-averaged or subsampled with
  respect to the original image. <i>Psfrad</i> is the value of the psf radius
  parameter in the task DAOPARS used to compute <i>psfimage</i> and is stored in
  the <i>psfimage</i> header parameter <span style="font-family: monospace;">"PSFRAD"</span>.
  </p>
  <p>
  If <i>psfimage</i> was computed with the variable PSF parameter <i>varorder</i>
  set to &gt; 0, then <i>image</i> is computed at a point (xpsf, ypsf) defined
  relative to the original image.  By default <i>image</i> is computed at the
  centroid of the PSF defined by the <i>psfimage</i> header parameters <span style="font-family: monospace;">"XPSF"</span>
  and <span style="font-family: monospace;">"YPSF"</span>.
  </p>
  <p>
  The intensity scale of <i>image</i> is determined by the value of <i>magnitude</i>
  relative to the magnitude of the PSF. By default the output PSF has the
  magnitude of the first PSF star stored in the <i>psfimage</i> header parameter
  <span style="font-family: monospace;">"PSFMAG"</span>.
  </p>
  <p>
  SEEPSF is most commonly used for visualizing the PSF in image scale coordinates
  and checking the form of any variability as a function of position. However
  <i>image</i> can also be used as input to other image processing program, for
  example it might be used as the kernel in a convolution operation.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Compute the output PSF in image scale coordinates of PSF function
  for image dev$ypix.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; seepsf ypix.psf.3 ypixpsf
  </pre></div>
  <p>
  2. Compute the output PSF in image scale coordinates of the variable
  PSF for the image m92b at position (113.63,50.48) pixels relative to the
  original image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; seepsf m92b.psf.2 m92psf xpsf=113.63 ypsf=50.48
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  datapars,daopars,psf
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

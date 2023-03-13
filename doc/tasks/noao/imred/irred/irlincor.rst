.. _irlincor:

irlincor: Correct IR imager frames for non-linearity
====================================================

**Package: irred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  irlincor input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of images to be corrected for non-linearity
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The list of corrected output images
  </dd>
  </dl>
  <dl id="l_coeff1">
  <dt><b>coeff1 = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coeff1' Line='coeff1 = 1.0' -->
  <dd>The first coefficient of the correction function
  </dd>
  </dl>
  <dl id="l_coeff2">
  <dt><b>coeff2 = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coeff2' Line='coeff2 = 0.0' -->
  <dd>The second coefficient of the correction function
  </dd>
  </dl>
  <dl id="l_coeff3">
  <dt><b>coeff3 = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coeff3' Line='coeff3 = 0.0' -->
  <dd>The third coefficient of the correction function
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The IR imager frames specified by <i>input</i>, which may be a general image
  template including wild cards or an @list, are corrected for non-linearity
  on a pixel by pixel basis and written to <i>output</i>. The number of output
  images must match the number input. The pixel type of the output image(s) will
  match that of the input image(s), however, internally all calculations are 
  performed as type real. The correction is performed assuming 
  that the non-linearity can be represented by the following simple relationship:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ADU' = ADU * [ coeff1 + coeff2 * (ADU / 32767) + coeff3 * (ADU / 32767)**2 ]
  </pre></div>
  <p>
  The coefficients which occur in this expression are specified by the
  parameters <i>coeff1</i>, <i>coeff2</i> and <i>coeff3</i>. Their values are 
  derived from periodic instrumental calibrations and are believed to be
  fairly constant. The  default values specify a <b>null</b> correction.
  You should consult <b>Jay Elias</b> for the latest values.
  Note that the coefficients are expressed in terms of ADU normalised to the
  maximum possible value 32767, in order that their values can be input
  more easily.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Correct input to output using the default values for the coefficients (not a very rewarding operation!)
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; irlincor input output
  </pre></div>
  <p>
  2. Correct a list of images in place using specified values for the coefficients
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; irlincor @list @list coeff1=1.0 coeff2=0.1 coeff3=0.01
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_authors">
  <h3>Authors</h3>
  <p>
  The IRLINCOR task was originally written by Steve Heathcote as part of the
  CTIO package. 
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The form of the correction equation is currently experimental;
  a higher order polynomial or a different functional form could be accommodated
  very easily if required.
  It may be advisable to carry out the calculations in double precision.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  onedspec.coincor, proto.imfunction
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'AUTHORS' 'BUGS' 'SEE ALSO'  -->
  

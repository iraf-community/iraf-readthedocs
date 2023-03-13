.. _fitskypars:

fitskypars: Edit the sky fitting algorithm parameters
=====================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fitskypars
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_salgorithm">
  <dt><b>salgorithm = <span style="font-family: monospace;">"mode"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='salgorithm' Line='salgorithm = "mode"' -->
  <dd>The sky fitting algorithm.  The sky fitting options are:
  <dl>
  <dt><b>constant</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='constant' Line='constant' -->
  <dd>Use a user supplied constant sky value.
  This algorithm is useful for measuring large resolved objects on flat
  backgrounds such as galaxies or comets.
  </dd>
  </dl>
  <dl>
  <dt><b>file</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='file' Line='file' -->
  <dd>Read sky values from a text file. This option is useful for importing
  user determined sky values into DAOPHOT.
  </dd>
  </dl>
  <dl>
  <dt><b>mean</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='mean' Line='mean' -->
  <dd>Compute the mean of the sky pixel distribution. This algorithm is useful
  for computing sky values in regions with few background counts.
  </dd>
  </dl>
  <dl>
  <dt><b>median</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='median' Line='median' -->
  <dd>Compute the median of the sky pixel distribution. This algorithm is a useful
  for computing sky values in regions with rapidly varying sky backgrounds
  and is a good alternative to <span style="font-family: monospace;">"centroid"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>mode</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='mode' Line='mode' -->
  <dd>Compute the mode of the sky pixel distribution using the mean and median.
  This is the recommended algorithm for DAOPHOT users measuring stellar objects in
  crowded stellar fields. Mode may not perform well in regions with
  rapidly varying sky backgrounds.
  </dd>
  </dl>
  <dl>
  <dt><b>centroid</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='centroid' Line='centroid' -->
  <dd>Compute the intensity weighted mean of the sky pixel histogram. This algorithm
  is reasonably robust in regions with rapidly varying or crowded sky backgrounds
  and is a good alternative to <span style="font-family: monospace;">"median"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>gauss</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='gauss' Line='gauss' -->
  <dd>Fit a Gaussian function to the sky pixel histogram using non-linear least-
  squares techniques to determine the peak. 
  </dd>
  </dl>
  <dl>
  <dt><b>ofilter</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='ofilter' Line='ofilter' -->
  <dd>Optimally filter the sky pixel histogram using a triangular weighting
  function to determine the peak.
  </dd>
  </dl>
  <dl>
  <dt><b>crosscor</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='crosscor' Line='crosscor' -->
  <dd>Compute the peak of the cross-correlation function of the pixel distribution
  and a Gaussian noise function to determine the peak.
  </dd>
  </dl>
  <dl>
  <dt><b>histplot</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='histplot' Line='histplot' -->
  <dd>Mark the peak of the sky pixel histogram with the graphics cursor.
  This algorithm is useful for making careful interactive sky measurements
  for a small number of objects in complicated regions or for checking the
  behavior of other sky algorithms. 
  </dd>
  </dl>
  <dl>
  <dt><b>radplot</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='radplot' Line='radplot' -->
  <dd>Mark the sky level on a radial profile plot with the graphics cursor.
  This algorithm is useful for making careful interactive sky measurements
  for a small number of objects in complicated regions or for checking the
  behavior of other sky algorithms. 
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_annulus">
  <dt><b>annulus = 10.0  (scale units)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='annulus' Line='annulus = 10.0  (scale units)' -->
  <dd>The inner radius of the annular sky fitting region in units of the DATAPARS
  scale parameter.
  </dd>
  </dl>
  <dl id="l_dannulus">
  <dt><b>dannulus = 10.0  (scale units)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dannulus' Line='dannulus = 10.0  (scale units)' -->
  <dd>The width of the annular sky fitting region in units of the DATAPARS scale
  parameter.
  </dd>
  </dl>
  <dl id="l_skyvalue">
  <dt><b>skyvalue = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skyvalue' Line='skyvalue = 0.0' -->
  <dd>The constant for constant sky subtraction.
  </dd>
  </dl>
  <dl id="l_smaxiter">
  <dt><b>smaxiter = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='smaxiter' Line='smaxiter = 10' -->
  <dd>The maximum number of iterations performed by the sky fitting algorithm.
  Smaxiter is required by the <span style="font-family: monospace;">"gauss"</span> and <span style="font-family: monospace;">"ofilter"</span> sky fitting algorithms.
  </dd>
  </dl>
  <dl id="l_sloclip">
  <dt><b>sloclip = 0.0, shiclip = 0.0 (percent)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sloclip' Line='sloclip = 0.0, shiclip = 0.0 (percent)' -->
  <dd>The high and low side clipping parameters in percent of the total number
  of pixels. If either of these parameters &gt; 0.0 then the specified
  percentage of the pixels will be removed from the sky pixel distribution
  before any sky fitting is done.
  </dd>
  </dl>
  <dl id="l_snreject">
  <dt><b>snreject = 50</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='snreject' Line='snreject = 50' -->
  <dd>The maximum number of sky pixel rejection cycles.
  </dd>
  </dl>
  <dl id="l_sloreject">
  <dt><b>sloreject = 3.0, shireject = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sloreject' Line='sloreject = 3.0, shireject = 3.0' -->
  <dd>The k-sigma clipping factors for the pixel rejection  phase of the
  sky fitting algorithm. Sloreject and shireject are in units of the
  computed sky sigma.
  </dd>
  </dl>
  <dl id="l_khist">
  <dt><b>khist = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='khist' Line='khist = 3.0' -->
  <dd>The k-sigma clipping factor for computing the sky pixels histogram. Khist is in
  units of sigma of the local sky pixel distribution.  The histogram will be
  2.0 * khist * sigma wide.  Khist is used by the <span style="font-family: monospace;">"centroid"</span>, <span style="font-family: monospace;">"gauss"</span>,
  <span style="font-family: monospace;">"crosscor"</span>, <span style="font-family: monospace;">"ofilter"</span>, and <span style="font-family: monospace;">"histplot"</span> sky fitting algorithms.
  </dd>
  </dl>
  <dl id="l_binsize">
  <dt><b>binsize = 0.10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='binsize' Line='binsize = 0.10' -->
  <dd>The width of a single bin of the sky pixel histogram.  Binsize is in units of
  the sigma of the local sky pixel distribution. Binsize is used by the
  <span style="font-family: monospace;">"centroid"</span>, <span style="font-family: monospace;">"gauss"</span>, <span style="font-family: monospace;">"crosscor"</span>, <span style="font-family: monospace;">"ofilter"</span>, and <span style="font-family: monospace;">"histplot"</span> sky fitting
  algorithms.
  </dd>
  </dl>
  <dl id="l_smooth">
  <dt><b>smooth = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='smooth' Line='smooth = no' -->
  <dd>Boxcar smooth the sky pixel histogram before computing a sky value.
  Smooth is used by the <span style="font-family: monospace;">"centroid"</span>, <span style="font-family: monospace;">"gauss"</span>, <span style="font-family: monospace;">"crosscor"</span>, <span style="font-family: monospace;">"ofilter"</span>, and
  <span style="font-family: monospace;">"histplot"</span> sky fitting algorithms.
  </dd>
  </dl>
  <dl id="l_rgrow">
  <dt><b>rgrow = 0.0  (scale units)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rgrow' Line='rgrow = 0.0  (scale units)' -->
  <dd>The region growing radius for pixel rejection in the sky region in units
  of the DATAPARS scale parameter. When a bad sky_pixel is detected, all pixels
  within rgrow / scale pixels of the bad pixel will be rejected. If rgrow is
  0.0 region growing is disabled.
  </dd>
  </dl>
  <dl id="l_mksky">
  <dt><b>mksky = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mksky' Line='mksky = no' -->
  <dd>Mark the sky annuli on the displayed image ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The sky fitting algorithm parameters control the action of the sky fitting
  algorithms. The default parameter settings should give reasonable results in
  the majority of cases.  Several of the sky fitting parameters scale with
  image scale, <i>scale</i> which is data dependent.
  <i>Scale</i> is defined in the DATAPARS parameter set.
  </p>
  <p>
  Sky pixels in an annular region of inner radius <i>annulus / scale</i> pixels
  and a width of <i>dannulus / scale</i> pixels are extracted from the IRAF image.
  If the <i>scale</i> parameter is defined in terms of the number of half-width
  at half-maximum of the point spread function per pixel, then single values of
  annulus and dannulus will work well for images with different seeing and
  detector characteristics.
  </p>
  <p>
  Pixels outside of the good data range specified by <i>datamin</i> and
  <i>datamax</i> are rejected from the sky pixel distribution. After bad
  data rejection <i>Ploclip</i> and <i>phiclip</i> percent pixels are rejected
  from the low and high sides of the sorted pixel distribution before any
  sky fitting is done.
  </p>
  <p>
  Sky values are computed using the sky fitting algorithm specified by
  <i>salgorithm</i>. The default value is <span style="font-family: monospace;">"centroid"</span>. If <i>salgorithm</i>
  = <span style="font-family: monospace;">"mean"</span>, <span style="font-family: monospace;">"median"</span> or <span style="font-family: monospace;">"mode"</span>, the sky value is computed directly from the
  array of sky pixels.  The remaining sky fitting algorithms use the histogram
  of the object sky pixels. The computed histogram is <i>khist</i> * sigma wide
  with a bin width of <i>binsize</i> * sigma  where sigma is the computed
  standard deviation of the sky pixels for each object. If <i>smooth</i> = yes,
  boxcar smoothing is performed on the computed histogram before sky fitting.
  The mode of the histogram is  computed using, a non-linear least squares
  fit to a Gaussian (salgorithm = <span style="font-family: monospace;">"gauss"</span>), optimal filtering of the histogram
  (salgorithm = <span style="font-family: monospace;">"ofilter"</span>), computing the centroid of the histogram
  (salgorithm = <span style="font-family: monospace;">"centroid"</span>), or by cross-correlation techniques
  (salgorithm = <span style="font-family: monospace;">"crosscor"</span>).
  </p>
  <p>
  Two interactive methods of fitting sky are also available. If <i>salgorithm</i>
  is <span style="font-family: monospace;">"radplot"</span> or <span style="font-family: monospace;">"histplot"</span>, the user must interactively set
  the value of the sky using a radial profile or a histogram plot.
  </p>
  <p>
  Pixels which deviate from the sky value by more than <i>kreject times the
  computed sky sigma are rejected from the fit. If fIrgrow</i> &gt; 0, pixels
  within a radius of rgrow / scale of the rejected pixel are also rejected from
  the fit. The rejection procedure iterates until no further pixels are rejected,
  all pixels are rejected, or the maximum number of rejection cycles
  <i>snreject</i> iterations is reached.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the sky fitting parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; lpar fitskypars
  </pre></div>
  <p>
  2. Edit the sky fitting parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; fitskypars
  </pre></div>
  <p>
  3. Edit the FITSKYPARS parameters from with the PHOT task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; epar phot
  
      ... edit a few phot parameters
  
      ... move to the fitskypars parameter and type :e
  
      ... edit the fitskypars parameters and type :wq
  
      ... finish editing the phot parameters and type :wq
  </pre></div>
  <p>
  4. Save the current FITSKYPARS parameter set in a text file skynite1.par.
  This can also be done from inside a higher level task as in the
  above example.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; epar fitskypars
  
      ... type ":w skynite1.par"  from within epar
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
  epar,lpar,datapars,phot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

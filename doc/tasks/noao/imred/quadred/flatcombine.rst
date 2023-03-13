.. _flatcombine:

flatcombine: Combine and process flat field images
==================================================

**Package: quadred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  flatcombine input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of flat field images to combine.  The <i>ccdtype</i> parameter
  may be used to select the flat field images from a list containing all
  types of data.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output = <span style="font-family: monospace;">"Flat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output = "Flat"' -->
  <dd>Output flat field root image name.  The subset ID is appended.
  </dd>
  </dl>
  <dl id="l_combine">
  <dt><b>combine = <span style="font-family: monospace;">"average"</span> (average|median)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='combine' Line='combine = "average" (average|median)' -->
  <dd>Type of combining operation performed on the final set of pixels (after
  rejection).  The choices are
  <span style="font-family: monospace;">"average"</span> or <span style="font-family: monospace;">"median"</span>.  The median uses the average of the two central
  values when the number of pixels is even.
  </dd>
  </dl>
  <dl id="l_reject">
  <dt><b>reject = <span style="font-family: monospace;">"avsigclip"</span> (none|minmax|ccdclip|crreject|sigclip|avsigclip|pclip)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reject' Line='reject = "avsigclip" (none|minmax|ccdclip|crreject|sigclip|avsigclip|pclip)' -->
  <dd>Type of rejection operation.  See <b>combine</b> for details.
  </dd>
  </dl>
  <dl id="l_ccdtype">
  <dt><b>ccdtype = <span style="font-family: monospace;">"flat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccdtype' Line='ccdtype = "flat"' -->
  <dd>CCD image type to combine.  If no image type is given then all input images
  are combined.
  </dd>
  </dl>
  <dl id="l_process">
  <dt><b>process = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='process' Line='process = yes' -->
  <dd>Process the input images before combining?
  </dd>
  </dl>
  <dl id="l_subsets">
  <dt><b>subsets = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subsets' Line='subsets = yes' -->
  <dd>Combine images by subset parameter?  If yes then the input images are
  grouped by subset parameter and each group combined into a separate output
  image.  The subset identifier is appended to the output and sigma image
  names.  See <b>subsets</b> for more on the subset parameter.  This is generally
  used with flat field images.
  </dd>
  </dl>
  <dl id="l_delete">
  <dt><b>delete = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='delete' Line='delete = no' -->
  <dd>Delete input images after combining?  Only those images combined are deleted.
  </dd>
  </dl>
  <dl id="l_clobber">
  <dt><b>clobber = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='clobber' Line='clobber = no' -->
  <dd>Clobber existing output images?
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = <span style="font-family: monospace;">"mode"</span> (none|mode|median|mean|exposure)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = "mode" (none|mode|median|mean|exposure)' -->
  <dd>Multiplicative image scaling to be applied.  The choices are none, scale
  by the mode, median, or mean of the specified statistics section, or scale
  by the exposure time given in the image header.
  </dd>
  </dl>
  <dl id="l_statsec">
  <dt><b>statsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='statsec' Line='statsec = ""' -->
  <dd>Section of images to use in computing image statistics for scaling.
  If no section is given then the entire region of the image is
  sampled (for efficiency the images are sampled if they are big enough).
  </dd>
  </dl>
  <p style="text-align:center">Algorithm Parameters
  
  </p>
  <dl id="l_nlow">
  <dt><b>nlow = 1,  nhigh = 1 (minmax)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlow' Line='nlow = 1,  nhigh = 1 (minmax)' -->
  <dd>The number of low and high pixels to be rejected by the <span style="font-family: monospace;">"minmax"</span> algorithm.
  </dd>
  </dl>
  <dl id="l_nkeep">
  <dt><b>nkeep = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nkeep' Line='nkeep = 1' -->
  <dd>The minimum number of pixels to retain or the maximum number to reject
  when using the clipping algorithms (ccdclip, crreject, sigclip,
  avsigclip, or pclip).  When given as a positive value this is the minimum
  number to keep.  When given as a negative value the absolute value is
  the maximum number to reject.  This is actually converted to a number
  to keep by adding it to the number of images.
  </dd>
  </dl>
  <dl id="l_mclip">
  <dt><b>mclip = yes (ccdclip, crreject, sigclip, avsigcliip)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mclip' Line='mclip = yes (ccdclip, crreject, sigclip, avsigcliip)' -->
  <dd>Use the median as the estimate for the true intensity rather than the
  average with high and low values excluded in the <span style="font-family: monospace;">"ccdclip"</span>, <span style="font-family: monospace;">"crreject"</span>,
  <span style="font-family: monospace;">"sigclip"</span>, and <span style="font-family: monospace;">"avsigclip"</span> algorithms?  The median is a better estimator
  in the presence of data which one wants to reject than the average.
  However, computing the median is slower than the average.
  </dd>
  </dl>
  <dl id="l_lsigma">
  <dt><b>lsigma = 3., hsigma = 3. (ccdclip, crreject, sigclip, avsigclip, pclip)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lsigma' Line='lsigma = 3., hsigma = 3. (ccdclip, crreject, sigclip, avsigclip, pclip)' -->
  <dd>Low and high sigma clipping factors for the <span style="font-family: monospace;">"ccdclip"</span>, <span style="font-family: monospace;">"crreject"</span>, <span style="font-family: monospace;">"sigclip"</span>,
  <span style="font-family: monospace;">"avsigclip"</span>, and <span style="font-family: monospace;">"pclip"</span> algorithms.  They multiply a <span style="font-family: monospace;">"sigma"</span> factor
  produced by the algorithm to select a point below and above the average or
  median value for rejecting pixels.  The lower sigma is ignored for the
  <span style="font-family: monospace;">"crreject"</span> algorithm.
  </dd>
  </dl>
  <dl id="l_rdnoise">
  <dt><b>rdnoise = <span style="font-family: monospace;">"0."</span>, gain = <span style="font-family: monospace;">"1."</span>, snoise = <span style="font-family: monospace;">"0."</span> (ccdclip, crreject)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rdnoise' Line='rdnoise = "0.", gain = "1.", snoise = "0." (ccdclip, crreject)' -->
  <dd>CCD readout noise in electrons, gain in electrons/DN, and sensitivity noise
  as a fraction.  These parameters are used with the <span style="font-family: monospace;">"ccdclip"</span> and <span style="font-family: monospace;">"crreject"</span>
  algorithms.  The values may be either numeric or an image header keyword
  which contains the value.
  </dd>
  </dl>
  <dl id="l_pclip">
  <dt><b>pclip = -0.5 (pclip)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pclip' Line='pclip = -0.5 (pclip)' -->
  <dd>Percentile clipping algorithm parameter.  If greater than
  one in absolute value then it specifies a number of pixels above or
  below the median to use for computing the clipping sigma.  If less
  than one in absolute value then it specifies the fraction of the pixels
  above or below the median to use.  A positive value selects a point
  above the median and a negative value selects a point below the median.
  The default of -0.5 selects approximately the quartile point.
  See <b>combine</b> for further details.
  </dd>
  </dl>
  <dl id="l_blank">
  <dt><b>blank = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blank' Line='blank = 1.' -->
  <dd>Output value to be used when there are no pixels.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The flat field images in the input image list are combined.  If there
  is more than one subset (such as a filter or grating) then the input
  flat field images are grouped by subset and an combined separately.
  The input images may be processed first if desired.  However if all
  zero level bias effects are linear then this is not necessary and some
  processing time may be saved.  The original images may be deleted
  automatically if desired.  The output pixel datatype will be real.
  </p>
  <p>
  This task is a script which applies <b>ccdproc</b> and <b>combine</b>.  The
  parameters and combining algorithms are described in detail in the help for
  <b>combine</b>.  This script has default parameters specifically set for
  flat field images and simplifies the combining parameters.  There are other
  combining options not included in this task.  For these additional
  features, such as thresholding, offseting, masking, and projecting, use
  <b>combine</b>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. The image data contains four flat field images for three filters.
  To automatically select them and combine them as a background job
  using the default combining algorithm:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; flatcombine ccd*.imh&amp;
  </pre></div>
  <p>
  The final images are <span style="font-family: monospace;">"FlatV"</span>, <span style="font-family: monospace;">"FlatB"</span>, and <span style="font-family: monospace;">"FlatR"</span>.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ccdproc, combine, subsets
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

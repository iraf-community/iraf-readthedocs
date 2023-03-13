.. _findthresh:

findthresh: Estimate a CCD's sky noise from the gain and readnoise
==================================================================

**Package: nproto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  findthresh data
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_data">
  <dt><b>data</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='data' Line='data' -->
  <dd>The level of the sky (or any other data level, for that matter) in A/D
  units, for which the random error is to be estimated.  If this is not
  given on the command line and a list of <b>images</b> is specified then
  the data level will be measured from the images.
  </dd>
  </dl>
  <dl id="l_images">
  <dt><b>images = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images = ""' -->
  <dd>If not NULL (<span style="font-family: monospace;">""</span>) and if <b>data</b> is not specified, this is a list of
  images whose random background error per pixel is to be estimated.
  </dd>
  </dl>
  <dl id="l_section">
  <dt><b>section = <span style="font-family: monospace;">"[*,*]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='section' Line='section = "[*,*]"' -->
  <dd>The selected image section for the statistics.  This should be chosen
  to exclude bad columns or rows, cosmic rays, and other blemishes.
  </dd>
  </dl>
  <dl id="l_gain">
  <dt><b>gain</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gain' Line='gain' -->
  <dd>The CCD gain in electrons/ADU.
  This may be estimated using the FINDGAIN task.
  </dd>
  </dl>
  <dl id="l_readnoise">
  <dt><b>readnoise</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='readnoise' Line='readnoise' -->
  <dd>The CCD read noise in electrons.
  This may be estimated using the FINDGAIN task.
  </dd>
  </dl>
  <dl id="l_nframes">
  <dt><b>nframes = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nframes' Line='nframes = 1' -->
  <dd>The number of raw data frames that were coadded or averaged
  to produce the <b>images</b>.  If this is not set to 1, the
  <b>coaddtype</b> parameter must also be set to the proper value.
  </dd>
  </dl>
  <dl id="l_coaddtype">
  <dt><b>coaddtype = <span style="font-family: monospace;">"average"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coaddtype' Line='coaddtype = "average"' -->
  <dd>For coadded frames (<b>nframes</b> &gt; 1) the type of combination
  that was done, either <span style="font-family: monospace;">"average"</span> or <span style="font-family: monospace;">"sum"</span>.
  </dd>
  </dl>
  <dl id="l_center">
  <dt><b>center = <span style="font-family: monospace;">"mean"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='center' Line='center = "mean"' -->
  <dd>The statistical measure of central tendency that is used to estimate
  the data level of each image.  This can have the values:  <b>mean</b>,
  <b>midpt</b>, or <b>mode</b>.  These are calculated using the same
  algorithm as the IMSTATISTICS task.
  </dd>
  </dl>
  <dl id="l_binwidth">
  <dt><b>binwidth = 0.1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='binwidth' Line='binwidth = 0.1' -->
  <dd>The bin width of the histogram (in sigma) that is used to estimate the
  <b>midpt</b> or <b>mode</b> of the data section in each image.
  The default case of center=<b>mean</b> does not use this parameter.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Label the computed and measured background noise on output,
  rather than print them two per line?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  FINDTHRESH can be used to estimate the expected random error per pixel
  (in ADU) of the sky background of a CCD image, given the <b>gain</b> (in
  electrons per ADU) and <b>readnoise</b> (in electrons) of the CCD.  The
  sky background (or any other data level of interest) can be specified
  directly with the <b>data</b> parameter, or the representative values can
  be measured from a specified list of <b>images</b> as also governed by
  the <b>section</b>, <b>center</b>, and <b>binwidth</b> parameters.
  FINDTHRESH can be used with processed frames that are the coaddition or
  average of several raw images by choosing the correct values for the
  <b>nframes</b> and <b>coaddtype</b> parameters.  In this case
  (<b>nframes</b> &gt; 1), the effective gain and effective readnoise of the
  coadded frames will also be printed out.
  </p>
  <p>
  The section over which the statistics of the <b>images</b> are computed
  should be chosen carefully.  The frames may be displayed and perhaps
  blinked, and IMSTATISTICS, IMHISTOGRAM, IMPLOT, and other tasks may be
  used to compare the statistics of various sections of the images directly.
  </p>
  </section>
  <section id="s_algorithm">
  <h3>Algorithm</h3>
  <p>
  The formula used by the task is:
  </p>
  <div class="highlight-default-notranslate"><pre>
  random error in 1 pixel = sqrt (data*p(N) + r(N)**2) / p(N)
  </pre></div>
  <p>
  Where the effective gain, p(N), is given in electrons per ADU and
  the effective readnoise, r(N), is given in electrons.  The effective
  gain and readnoise are calculated from the intrinsic <b>gain</b> and
  <b>readnoise</b>, specified as parameters to the task, by the relations:
  </p>
  <div class="highlight-default-notranslate"><pre>
  p(N) =      N  * <b>gain</b>        (only if the frames were <b>averaged</b>)
  r(N) = sqrt(N) * <b>readnoise</b>   (whether averaged <b>or</b> summed frames)
  </pre></div>
  <p>
  In our implementation, the level of the sky can be calculated using any
  of the <b>mean</b>, <b>midpt</b> (an estimate of the median), or <b>mode</b>
  as determined by the <b>center</b> parameter.  For the <b>midpt</b> or
  <b>mode</b> choices only, the value of the <b>binwidth</b> parameter
  determines the bin width (in sigma) of the histogram that is used in
  the calculation.  FINDTHRESH uses the IMSTATISTICS task to measure the
  statistics.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To estimate the CCD background noise at a specified data level, gain and
  readnoise (note that you will be prompted for the gain and the readnoise
  if you don't set them either explicitly on the command line, or previously
  using, for example, eparam):
  </p>
  <div class="highlight-default-notranslate"><pre>
  lo&gt; findthresh 100 gain=2.3 readnoise=13.
  </pre></div>
  <p>
  To estimate the CCD background noise within a 100x100 section
  of a list of images, data*.imh:
  </p>
  <div class="highlight-default-notranslate"><pre>
  lo&gt; findthresh data*.imh section="[271:370,361:460]"
  </pre></div>
  <p>
  To estimate the CCD background noise using the mode to estimate the
  sky level for each image section:
  </p>
  <div class="highlight-default-notranslate"><pre>
  lo&gt; findthresh.section="[271:370,361:460]"
  lo&gt; findthresh data*.imh center=mode
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  findgain, imstatistics, imhistogram
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'ALGORITHM' 'EXAMPLES' 'SEE ALSO'  -->
  

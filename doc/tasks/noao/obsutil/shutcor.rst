.. _shutcor:

shutcor: Shutter correction from images of varying exposure times
=================================================================

**Package: obsutil**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  SHUTCOR calculate the shutter correction for a detector given a
  sequence of overscan corrected images of varying durations.  Typically
  these would be flat field exposures.  The shutter correction is the
  intercept on a plot of exposure duration versus exposure level.
  </p>
  </section>
  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  shutcor images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of overscan corrected images.  These would usually be flat
  field exposures.
  </dd>
  </dl>
  <dl id="l_section">
  <dt><b>section = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='section' Line='section = ""' -->
  <dd>The selected image section for the statistics.  This should be chosen
  to exclude bad columns or rows, cosmic rays, and other non-linear
  features.
  </dd>
  </dl>
  <dl id="l_center">
  <dt><b>center = <span style="font-family: monospace;">"mode"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='center' Line='center = "mode"' -->
  <dd>The statistical measure of central tendency that is used to estimate
  the data level of each image.  This can have the values:  <b>mean</b>,
  <b>midpt</b>, or <b>mode</b>.  These are calculated using the same
  algorithm as the IMSTATISTICS task.
  </dd>
  </dl>
  <dl id="l_nclip">
  <dt><b>nclip = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nclip' Line='nclip = 3' -->
  <dd>Number of sigma clipping iterations.  If the value is zero then no clipping
  is performed.
  </dd>
  </dl>
  <dl id="l_lsigma">
  <dt><b>lsigma = 4, usigma = 4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lsigma' Line='lsigma = 4, usigma = 4' -->
  <dd>Lower and upper sigma clipping factors used with the mean value and
  standard deviation to eliminate cosmic rays.
  Since <b>findgain</b> is sensitive to the statistics of the data the
  clipping factors should be symmetric (the same both above and below the
  mean).
  </dd>
  </dl>
  <dl id="l_exposure">
  <dt><b>exposure = <span style="font-family: monospace;">"exptime"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exposure' Line='exposure = "exptime"' -->
  <dd>Keyword giving the exposure time.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Verbose output?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  SHUTCOR calculate the shutter correction for a detector given a
  sequence of overscan corrected images of varying durations.  Typically
  these would be flat field exposures.  The shutter correction is the
  intercept on a plot of exposure duration versus exposure level.
  </p>
  <p>
  The images must contain the keyword OVERSCAN otherwise and error will
  be given.
  </p>
  <p>
  Bad pixels should be eliminated to avoid affecting the statistics.
  This can be done with sigma clipping and/or an image section.
  The sigma clipping should not significantly affect the assumed gaussian
  distribution while eliminating outlyers due to cosmic rays and
  unmasked bad pixels.  This means that clipping factors should be
  symmetric.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  A sequence of flat fields with varying exposure times are taken and
  processed to subtract the overscan.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; shutcor flat*
  
  Shutter correction = 0.538 +/- 0.043 seconds
  
  Information about the mode versus exptime fit:
  
         intercept        slope     (and errors)
          5.347105      9.933618
         0.4288701    0.01519613
  
      chi sqr:  0.2681   ftest: 419428.   correlation:      1.
       nr pts:      4.   std dev res: 0.422769
  
      x(data)     y(calc)     y(data)     sigy(data)
           3.      35.148     34.6725          0.
          12.     124.551     125.015          0.
          27.     273.555     273.778          0.
          48.     482.161     481.949          0.
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imstatistics
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

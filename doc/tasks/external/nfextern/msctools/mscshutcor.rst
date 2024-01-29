.. _mscshutcor:

mscshutcor: Compute shutter correction from a set of mosaic exposures
=====================================================================

**Package: msctools**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  MSCSHUTCOR calculate the shutter correction for a mosaic camera given a
  sequence of overscan corrected images of varying durations.  Typically
  these would be flat field exposures.  The shutter correction is the
  intercept on a plot of exposure duration versus exposure level.
  </p>
  </section>
  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mscshutcor images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of overscan corrected mosaic exposures.  These would usually be flat
  field exposures.
  </dd>
  </dl>
  <dl id="l_extnames">
  <dt><b>extnames = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extnames' Line='extnames = ""' -->
  <dd>List of extension names or patterns matching the full extension name.
  Each comma delimited segment is treated as a pattern so multiple patterns
  may be used.
  </dd>
  </dl>
  <dl id="l_section">
  <dt><b>section = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='section' Line='section = ""' -->
  <dd>The selected image section for the statistics.  This should be chosen
  to exclude bad columns or rows, cosmic rays, and other non-linear
  features.  Note that the section is in pixel coordinates and will be
  used on all the selected extensions.
  </dd>
  </dl>
  <dl id="l_center">
  <dt><b>center = <span style="font-family: monospace;">"mode"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='center' Line='center = "mode"' -->
  <dd>The statistical measure of central tendency that is used to estimate
  the data level of each extension.  This parameter can have the values:
  <b>mean</b>, <b>midpt</b>, or <b>mode</b>.  These are calculated using the same
  algorithm as the IMSTATISTICS task.  When there is more than one extension
  the measured statistics over each extension are averaged.
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
  MSCSHUTCOR calculate the shutter correction for a mosaic camera given a
  sequence of overscan corrected exposures of varying durations.  Typically
  these would be flat field exposures.  For the selected extensions
  the exposure time specified in the EXPTIME keyword is extracted.  A
  photometric measure, given by the <i>center</i> parameter, of the data
  over all the extensions is estimated.  When there are multiple extensions
  in an exposure the statistics obtained separately in each extension are
  averaged.  Note that this is valid even when the extensions have different
  gains provided all exposures have the same gains.
  </p>
  <p>
  The shutter correction is the intercept divided by the slope from a plot
  of the exposure time versus photometirc exposure statistic.  When
  the <i>verbose</i> parameter is set the statistics from each exposure and
  the fit values are output.
  </p>
  <p>
  The first image extension in each exposure must contain the keywords
  OVERSCAN and EXPTIME otherwise an error will be given.  A warning is
  given if the image contains the keyword FLATCOR.
  </p>
  <p>
  Bad pixels should be eliminated to avoid affecting the statistics.  This
  can be done with sigma clipping and/or an image section; though when there
  are multiple extensions the same image section is applied to each one.  The
  sigma clipping should not significantly affect the assumed gaussian
  distribution while eliminating outlyers due to cosmic rays and unmasked bad
  pixels.  This means that clipping factors should be symmetric.
  </p>
  <p>
  This task is a similar to the task <b>obsutil.shutcor</b> except that it
  handles multiextension mosaic files.  However, this task will also work
  with simple single images and so may be used for both mosaic and non-mosaic
  data.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  A sequence of flat fields with varying exposure times are taken and
  processed to subtract the overscan.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mscshutcor flat*
  
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
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  obsutil.shutcor, imstatistics
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

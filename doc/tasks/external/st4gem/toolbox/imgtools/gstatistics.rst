.. _gstatistics:

gstatistics: Compute and print image pixel statistics for all groups.
=====================================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  gstatistics images
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task computes and prints, in tabular form, several statistical quantities,
  either for each individual group, or for an accumulation over a range of 
  groups, of images in the list.  The results for the last image will be saved 
  into corresponding parameters in the pset `gstpar'. The quantities 
  to be printed are those selected by the `fields' parameter, or they may all 
  be selected by setting `fields=<span style="font-family: monospace;">"doall"</span>'.  The user may choose any or 
  all of the following:  
  </p>
  <div class="highlight-default-notranslate"><pre>
   doall - all of the statistical quantities
    npix - the number of pixels used to do the statistics
     min - the minimum pixel value
     max - the maximum pixel value
     sum - sum over all the pixels
    mean - the mean of the pixel distribution
  stddev - the standard deviation of the pixel distribution
   midpt - estimate of the median of the pixel distribution
    mode - estimate of the mode of the pixel distribution
    skew - the skewness of the pixel distribution
    kurt - the kurtosis of the pixel distribution
  </pre></div>
  <p>
  A mask can be used to exclude pixels flagged as bad. The parameter, `masks',
  accepts user specified mask files, which can be a file list, a file
  template, or a blank. The default for the `masks' parameter is a blank and
  no masking will be performed. A mask can be either an IRAF mask pixel lists
  file with an extension of <span style="font-family: monospace;">".pl"</span>, or a mask image.  For example, the Data 
  Quality Files (DQF) associated with the HST data images can be used 
  as mask images. Masks used in this program will exclusively be considered 
  as boolean. Since the <span style="font-family: monospace;">"bad"</span> pixels are flagged by non-zero bits in a DQF image,
  only pixels of an image with a zero value in its DQF file are considered
  as <span style="font-family: monospace;">"good"</span>. It is, therefore, assumed that an image-type mask is constructed in 
  such a way, that a non-zero mask pixel indicates that the pixel will be 
  rejected, while a zero mask pixel means that the pixel will be used.
  It is, however, conventional in a pixel-list-type mask that
  a non-zero mask pixel means to use that pixel. One may wish to use the task
  `images.imcopy' to copy a pixel-list-type mask into a mask image. 
  </p>
  <p>
  The parameter `groups' may be used to specify a range of groups. The default
  value of `groups' is set to <span style="font-family: monospace;">"*"</span> indicating statistics will be done for
  all groups of images. A group range may be specified by a set of three 
  integers, indicating the beginning group, the ending group, and the increment, 
  e.g., 3-11x2 meaning a range of groups starting from group No. 3 through
  group No. 11 with a step of 2 (note: a default step is 1). 
  Several ranges of groups may be specified as range lists separated by
  a delimiter, i.e., a <span style="font-family: monospace;">","</span> or a blank. This range list, however, 
  will be overridden if the input file(s) itself already includes a group 
  specification. Note that the specification of the `groups' parameter
  will be ignored when a mask is a pixel lists file.
  </p>
  <p>
  This task will compute all specified statistical quantities either separately
  for individual groups of an image when `g_accum' is set to <span style="font-family: monospace;">"no"</span>, or 
  accumulatively over all groups specified by the parameter `groups'
  when `g_accum' is set to <span style="font-family: monospace;">"yes"</span>. The default value of `g_accum' is <span style="font-family: monospace;">"no"</span>.
  </p>
  <p>
  The image mean, standard deviation, skewness, and kurtosis, are 
  computed using the expressions listed below.  
  </p>
  <div class="highlight-default-notranslate"><pre>
      mean = sum (x1,...,xN) / N
    dev[i] = x[i] - mean
  variance = sum {dev[i]**2} / (N-1)
    stddev = sqrt (variance)
  skewness = sum {(dev[i] / stddev) ** 3} / N
  kurtosis = [sum {(dev[i] / stddev) ** 4} / N] - 3
  </pre></div>
  <p>
  The median and mode are computed in three passes through the image.  
  In the first pass the flagged data are excluded, and the mean and 
  extreme values are calculated.  In the 
  second pass the standard deviation, skewness, and kurtosis of the pixels 
  are calculated.  The median then is estimated by integrating the data 
  histogram and computing by interpolation the data value at which 
  half the pixels are below that data value and half are above it.  The 
  mode is estimated by locating the maximum of the data histogram and fitting 
  the peak by parabolic interpolation. While a histogram with the number of bins
  up to one fourth of the number of pixels is used to achieve high accuracy,
  re-binning of the histogram to a relatively low resolution may be
  beneficial for searching the peak of the histogram. A successive
  histograms with a bin width twice as broad as the previous one 
  are used to obtain intermediate results
  of the mode. The re-binning of the histograms is ended when either the
  bin width is greater than 0.01 * standard deviation or the number of bins
  becomes less than one tenth of the number of pixels. The final result
  for the mode is an average of all the intermediate results of the mode.
  </p>
  <p>
  The desired statistical quantities of the last group of the last 
  image in the list, if `g_accum' is set to <span style="font-family: monospace;">"no"</span>, are saved 
  into a pset parameter file, `gstpar'.
  When `g_accum' is set to <span style="font-family: monospace;">"yes"</span>, what is saved in `gstpar' is the
  accumulated statistical quantities. For unspecified fields, the values are
  set to INDEF in the pset `gstpar'. These quantities in `gstpar'
  can be passed to other tasks. 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images [string]' -->
  <dd>List of images for which pixel statistics are to be computed.
  </dd>
  </dl>
  <dl>
  <dt><b>(masks = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(masks = "") [string]' -->
  <dd>List of masks which can be either a pixel lists file or a mask image.
  </dd>
  </dl>
  <dl>
  <dt><b>(groups = *) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(groups = *) [string]' -->
  <dd>List of ranges of groups in the images
  </dd>
  </dl>
  <dl>
  <dt><b>(g_accum = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(g_accum = no) [boolean]' -->
  <dd>Accumulate statistics over groups of an image?
  </dd>
  </dl>
  <dl>
  <dt><b>(fields = <span style="font-family: monospace;">"npix,mean,stddev,min,max"</span>)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fields = "npix,mean,stddev,min,max")' -->
  <dd>The statistical quantities to be computed and printed.
  </dd>
  </dl>
  <dl>
  <dt><b>(lower = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(lower = INDEF) [real]' -->
  <dd>Use only pixels with values greater than or equal to this limit.
  All pixels are above the default value of INDEF.
  </dd>
  </dl>
  <dl>
  <dt><b>(upper = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(upper = INDEF) [real]' -->
  <dd>Use only pixels with values less than or equal to this limit.
  All pixels are below the default value of INDEF.
  </dd>
  </dl>
  <dl>
  <dt><b>(gstpar = [pset])</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(gstpar = [pset])' -->
  <dd>Pset name for storing the statistical parameters.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Find the number of pixels, minimum, maximum, and mean  
  of the pixel values in the region [1:20,*] for each group in the image 
  <span style="font-family: monospace;">"w2t.c0h"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gstat w2t.c0h[1:20,*] masks="" fields="npix,min,max,mean" accum-
  
  # Image Statistics for w2t.c0h[1:20,*]
  # GROUP      NPIX       MIN       MAX      MEAN
  [    1]     16000  -101.148   2609.08   34.8566
  [    2]     16000  -54.3591   15069.2    340.44
  [    3]     16000  -67.8204   8499.35   16.7805
  [    4]     16000   -165.57   18697.3   39.1163
  
  </pre></div>
  <p>
  2. Compute the number of <span style="font-family: monospace;">"good"</span> pixels, sum, mean, midpt and stddev 
  for dev$pix with <span style="font-family: monospace;">"bad"</span> pixels excluded by a mask msk.pl
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gstat dev$pix masks="msk.pl" fields="npix,sum,mean,midpt,stddev"
  
  # Image Statistics for dev$pix
  # Bad pixels rejected by mask: msk.pl
        NPIX       SUM      MEAN     MIDPT    STDDEV
        4748   462279.   97.3629   92.9448   37.8867
  cl&gt;
  
  </pre></div>
  <p>
  3. Compute the number of pixels, skewness and kurtosis for a list of groups
  (groups 2 through 4) as a whole with DQF-flagged pixels excluded.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  cl&gt; gstat w4t.c0h masks="w4t.c1h" groups="2-4" fields="npix,skew,kurt" \
  &gt;&gt;&gt; g_accum+
  
  # Image Statistics for w4t.c0h
  # Accumulated over groups: 2-4
  # Bad pixels rejected by mask: w4t.c1h
        NPIX  SKEWNESS  KURTOSIS
     1801794   16.0679    471.94
  cl&gt;
  
  </pre></div>
  </section>
  <section id="s_timing_requirements">
  <h3>Timing requirements</h3>
  <p>
  On a SPARCStation 2, the task takes 37.92 CPU 
  seconds, and 55 sec of elapsed time, to compute all statistical quantities 
  for a 768 x 768 x 12 image.  These times decrease to 30.45 CPU sec and 
  43 elapsed seconds when a pixel-list-type mask excludes 40% pixels.
  It takes 10.267 CPU seconds and 19 sec of elapsed time to compute
  all statistical quantities for a full 800 x 800 WFPC image with 4 groups.
  Accumulating statistics over groups does not significantly influence the times
  required. Obviously, these times will vary with the type of machine 
  used, the amount of memory available, and other factors.  
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  The gstatistics program was based on the IRAF task imstatistics by Frank
  Valdes of the NOAO/IRAF group and the STSDAS task wstatistics
  by Richard A. Shaw of the STScI/STSDAS group. While the algorithms for 
  calculating statistical quantities in gstatistics are adopted from the 
  imstatistics and wstatistics, the gstatistics can deal with the IRAF (OIF)
  format and the STSDAS (GEIS) format images with masking operations.  
  See the source code for further information.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  gstpar, wstatistics, imstatistics, ranges
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'TIMING REQUIREMENTS' 'REFERENCES' 'SEE ALSO'  -->
  

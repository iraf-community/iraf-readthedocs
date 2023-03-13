.. _mimstatistics:

mimstatistics: Do image statistics through a mask
=================================================

**Package: proto**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  imstatistics images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>The input images or image sections for which pixel statistics are to be
  computed. Image sections are automatically applied to the input masks
  <i>imasks</i> if input masks are not mask sections.
  </dd>
  </dl>
  <dl id="l_imasks">
  <dt><b>imasks = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imasks' Line='imasks = ""' -->
  <dd>The list of input masks or input mask sections associated with <i>images</i>.
  Good and bad data values are assumed to be presented by mask values of 0 and
  1 respectively. The number of input masks must be 0, 1, or equal to the number
  of input images. Input mask sections if present override the input image
  sections.
  </dd>
  </dl>
  <dl id="l_omasks">
  <dt><b>omasks = <span style="font-family: monospace;">""</span> </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='omasks' Line='omasks = "" ' -->
  <dd>The list of output masks which are a combination of the input mask if any
  and pixels rejected using the good data limits and / or iterative clipping.
  Data used to compute the statistics are represented by 0 in the output mask,
  rejected data by zero. The number of output masks must be 0 or equal to
  the number of input images.
  </dd>
  </dl>
  <dl id="l_fields">
  <dt><b>fields = <span style="font-family: monospace;">"image,npix,mean,stddev,min,max"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fields' Line='fields = "image,npix,mean,stddev,min,max"' -->
  <dd>The statistical quantities to be computed and printed.
  </dd>
  </dl>
  <dl id="l_lower">
  <dt><b>lower = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lower' Line='lower = INDEF' -->
  <dd>The minimum good data limit.  All pixels are above the default value of INDEF.
  </dd>
  </dl>
  <dl id="l_upper">
  <dt><b>upper = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='upper' Line='upper = INDEF' -->
  <dd>The maximum good data limit.  All pixels are above the default value of INDEF.
  </dd>
  </dl>
  <dl id="l_nclip">
  <dt><b>nclip = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nclip' Line='nclip = 0' -->
  <dd>The maximum number of iterative clipping cycles. By default no clipping is
  performed.
  </dd>
  </dl>
  <dl id="l_lsigma">
  <dt><b>lsigma = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lsigma' Line='lsigma = 3.0' -->
  <dd>The low side clipping factor in sigma.
  </dd>
  </dl>
  <dl id="l_usigma">
  <dt><b>usigma = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='usigma' Line='usigma = 3.0' -->
  <dd>The high side clipping factor in sigma.
  </dd>
  </dl>
  <dl id="l_binwidth">
  <dt><b>binwidth = 0.1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='binwidth' Line='binwidth = 0.1' -->
  <dd>The width of the histogram bins in sigma used for computing the midpoint
  (estimate of the median) and the mode.
  </dd>
  </dl>
  <dl id="l_format">
  <dt><b>format = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='format' Line='format = yes' -->
  <dd>Label the output columns and print the results in fixed format ? If format
  is <span style="font-family: monospace;">"no"</span> no column labels are printed and the output is in free format.
  </dd>
  </dl>
  <dl id="l_cache">
  <dt><b>cache = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cache' Line='cache = no' -->
  <dd>Cache the image data in memory ? This can increase the efficiency of the
  task if nclip &gt; 0 or if either of the midpt or mode statistics is computed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The statistical quantities specified by the parameter <i>fields</i> are
  computed and printed for each image in the list specified by <i>images</i>.
  The results are printed in tabular form with the fields listed in the order
  they are specified in the fields parameter. The available fields are the
  following:
  </p>
  <div class="highlight-default-notranslate"><pre>
     image - the image name
      mask - the mask name
      npix - the number of pixels used to do the statistics
      mean - the mean of the pixel distribution
     midpt - estimate of the median of the pixel distribution
      mode - the mode of the pixel distribution
    stddev - the standard deviation of the pixel distribution
      skew - the skew of the pixel distribution
  kurtosis - the kurtosis of the pixel distribution
       min - the minimum pixel value
       max - the maximum pixel value
  </pre></div>
  <p>
  The mean, standard deviation, skew, kurtosis, min and max are computed in a
  single pass through the image using the expressions listed below.
  Only the quantities selected by the fields parameter are actually computed.
  </p>
  <div class="highlight-default-notranslate"><pre>
      mean = sum (x1,...,xN) / N
         y = x - mean
  variance = sum (y1 ** 2,...,yN ** 2) / (N-1)
    stddev = sqrt (variance)
      skew = sum ((y1 / stddev) ** 3,...,(yN / stddev) ** 3) / (N-1)
  kurtosis = sum ((y1 / stddev) ** 4,...,(yN / stddev) ** 4) / (N-1) - 3
  </pre></div>
  <p>
  The midpoint and mode are computed in two passes through the image. In the
  first pass the standard deviation of the pixels is calculated and used
  with the <i>binwidth</i> parameter to compute the resolution of the data
  histogram. The midpoint is estimated by integrating the histogram and
  computing by interpolation the data value at which exactly half the
  pixels are below that data value and half are above it. The mode is
  computed by locating the maximum of the data histogram and fitting the
  peak by parabolic interpolation.
  </p>
  <p>
  Pixels are rejected from the initial statistics computation by specifying an
  input mask <i>imasks</i> or by setting the good data limits <i>lower</i>
  and <i>upper</i>. Iterative rejection can be performed by setting the
  clipping parameters <i>nclip</i>, <i>lsigma</i>, and <i>usigma</i>.
  </p>
  <p>
  The input masks <i>imasks</i> can be specified in a variety of ways as
  shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
         "" - empty mask, use all the pixels
      EMPTY - empty mask, use all the pixels
   !KEYWORD - use mask specified by  header keyword KEYWORD
  !^KEYWORD - use inverse of mask specified by  header keyword KEYWORD
       mask - use specified mask
      ^mask - use inverse of specified mask
  </pre></div>
  <p>
  In all cases the mask values are assumed to be 0 in good data regions and 
  non-zero in rejected data regions. The input masks may in pixel list, e.g.
  <span style="font-family: monospace;">".pl"</span> format, or integer images format, e.g. <span style="font-family: monospace;">".imh"</span>, <span style="font-family: monospace;">".fits"</span>, etc.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Find the number of pixels, mean, standard deviation and the minimum
  and maximum pixel value of a bias region in an image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mimstat flat*[*,1] ""
  #      IMAGE      NPIX      MEAN    STDDEV       MIN       MAX
    flat1[*,1]       800     999.5     14.09      941.     1062.
    flat2[*,1]       800     999.4     28.87      918.     1413.
  </pre></div>
  <p>
  The string <span style="font-family: monospace;">"flat*"</span> uses a wildcard to select all images beginning with the
  word flat.  The string <span style="font-family: monospace;">"[*,1]"</span> is an image section selecting row 1.
  </p>
  <p>
  2. Compute the mean, midpoint, mode and standard deviation of a pixel
  distribution.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mimstat m51 "" fields="image,mean,midpt,mode,stddev"
  #      IMAGE    PIXELS      MEAN     MIDPT     MODE     STDDEV
           M51    262144     108.3     88.75    49.4       131.3
  </pre></div>
  <p>
  3. Compute the image statistics in an image section using a mask.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mimstat m51[200:400,200:400] imasks=M51.bpm.pl
  
  cl&gt; mimstat m51[200:400,200:400] imasks=M51.bpm.pl[200:400,200:400]
  
  cl&gt; mimstat m51[200:400,200:400] imasks=M51.crm.pl[1:201,1:201]
  </pre></div>
  <p>
  Note that the first two examples are equivalent so there is no need to
  specify the input mask section in the second case.
  </p>
  <p>
  4. Compute the image statistics using interactive rejection and save the
  rejected pixel mask.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mimstat m51 omasks=m51.rej.pl nclip=3
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  When using a very large number of pixels the accumulation of the sums
  of the pixel values to the various powers may encounter roundoff error.
  This is significant when the true standard deviation is small compared
  to the mean.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

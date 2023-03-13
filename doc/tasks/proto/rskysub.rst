.. _rskysub:

rskysub: Sky subtract images using running mean or median
=========================================================

**Package: proto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rskysub input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input images to be sky subtracted in time of observation order.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The list of output sky subtracted images. The number of output images must
  equal the number of input images.  If output is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or
  <span style="font-family: monospace;">"dir$"</span> then for every input image an output image called <span style="font-family: monospace;">"dir$image.sub.?"</span>
  is created, where <span style="font-family: monospace;">"dir$"</span> is the optional directory specification, <span style="font-family: monospace;">"image"</span> is
  the root input image name, and <span style="font-family: monospace;">"?"</span> is the next available version number.
  </dd>
  </dl>
  <dl id="l_imasks">
  <dt><b>imasks = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imasks' Line='imasks = ""' -->
  <dd>The optional list of input image masks. The input image masks are assumed to
  consist of 0's in good pixel regions and &gt; 0 integer values elsewhere. The
  number of input images masks must be 0, 1, or equal to the number of input
  images. If imasks is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or <span style="font-family: monospace;">"dir$"</span> then for every input
  image a default input image mask called <span style="font-family: monospace;">"dir$image.obm.?"</span> is searched for,
  where <span style="font-family: monospace;">"dir$"</span> is the optional directory specification, <span style="font-family: monospace;">"image"</span> is the root
  input image name, and <span style="font-family: monospace;">"?"</span> is the highest available version number.
  </dd>
  </dl>
  <dl id="l_omasks">
  <dt><b>omasks = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='omasks' Line='omasks = ""' -->
  <dd>The optional list of output masks. If output masks are defined they are
  used to created the sky image in place of the input masks. The output masks
  are a combination of the original input mask and pixels masked during the
  input image scale factor computation and consist of 0's in good data regions
  and 1's elsewhere. Output masks are only computed if <i>scale</i> = <span style="font-family: monospace;">"median"</span>.
  The number of output masks must be 0 or equal to the number of input images.
  If imasks is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>, or <span style="font-family: monospace;">"dir$"</span> then for every input image
  an output mask image called <span style="font-family: monospace;">"dir$image.skm.?"</span> is created, where <span style="font-family: monospace;">"dir$"</span> is
  the optional directory specification, <span style="font-family: monospace;">"image"</span> is the root input image name,
  and <span style="font-family: monospace;">"?"</span> is the next available version number.
  </dd>
  </dl>
  <dl id="l_hmasks">
  <dt><b>hmasks = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hmasks' Line='hmasks = ""' -->
  <dd>The list of output holes masks.  The holes masks defined bad pixels in the
  output images, i.e. those for which the underlying sky image was undefined.
  Holes masks are created only if <i>hmasks</i> is defined and there is at least
  1 undefined sky image pixel in the output image.  Holes masks contain 0's in
  undefined sky regions and 1's elsewhere.  If hmasks is <span style="font-family: monospace;">"default"</span>, <span style="font-family: monospace;">"dir$default"</span>,
  or <span style="font-family: monospace;">"dir$"</span> then for every input image an output mask image called
  <span style="font-family: monospace;">"dir$image.hom.?"</span> is created, where <span style="font-family: monospace;">"dir$"</span> is the optional directory
  specification, <span style="font-family: monospace;">"image"</span> is the root input image name, and <span style="font-family: monospace;">"?"</span> is the next
  available version number.
  </dd>
  </dl>
  <dl id="l_rescale">
  <dt><b>rescale = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rescale' Line='rescale = yes' -->
  <dd>Force recomputation of the individual input image scale factors  even though
  they have been previously computed and stored in the keyword <i>skyscale</i>?
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = <span style="font-family: monospace;">"median"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = "median"' -->
  <dd>The method used to compute the individual image scale factors. The options
  are:
  <dl>
  <dt><b>none</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='none' Line='none' -->
  <dd>The individual scale factors are all set to 1.0.
  </dd>
  </dl>
  <dl>
  <dt><b>!&lt;keyword&gt;</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='!&lt;keyword&gt;' -->
  <dd>The individual scale factors are all set to the value of the input image header
  keyword <i>keyword</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>median</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='median' Line='median' -->
  <dd>The individual scale factors are set to 1 / median. The medians are estimated
  using the input masks <i>imasks</i>, input image section <i>statsec</i>,
  the minimum and maximum good data values <i>lower</i> and <i>upper\R, the
  clipping factors fImaxiter</i>, <i>lnsigrej</i>, and <i>unsigrej</i> and the
  histogram binning parameter <i>binwidth</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>@&lt;file&gt;</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='@&lt;file&gt;' -->
  <dd>The individual image scale factors are read from the file <i>file</i>. 
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_skyscale">
  <dt><b>skyscale = <span style="font-family: monospace;">"SKYSCALE"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skyscale' Line='skyscale = "SKYSCALE"' -->
  <dd>The image header keyword containing the computed scaling factor.
  <i>Skyscale</i> is written to both the input and output images.
  </dd>
  </dl>
  <dl id="l_statsec">
  <dt><b>statsec = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='statsec' Line='statsec = ""' -->
  <dd>The input image section used to compute the individual image scaling factors.
  Statsec is independent of the input image section if any.
  </dd>
  </dl>
  <dl id="l_lower">
  <dt><b>lower = INDEF, upper = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lower' Line='lower = INDEF, upper = INDEF' -->
  <dd>The minimum and maximum input image good data values.
  </dd>
  </dl>
  <dl id="l_maxiter">
  <dt><b>maxiter = 20</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxiter' Line='maxiter = 20' -->
  <dd>The maximum number of clipping iterations.
  </dd>
  </dl>
  <dl id="l_lnsigrej">
  <dt><b>lnsigrej = 3.0, unsigrej = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lnsigrej' Line='lnsigrej = 3.0, unsigrej = 3.0' -->
  <dd>The lower and upper side sigma clipping factors.
  </dd>
  </dl>
  <dl id="l_binwidth">
  <dt><b>binwidth = 0.1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='binwidth' Line='binwidth = 0.1' -->
  <dd>The histogram bin width in sigma used in estimating the median value.
  </dd>
  </dl>
  <dl id="l_resubtract">
  <dt><b>resubtract = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='resubtract' Line='resubtract = yes' -->
  <dd>Force recomputation and subtraction of the sky image even though it exists
  already ?
  </dd>
  </dl>
  <dl id="l_combine">
  <dt><b>combine = <span style="font-family: monospace;">"average"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='combine' Line='combine = "average"' -->
  <dd>The method used to create the sky images. The options are <span style="font-family: monospace;">"average"</span> and
  <span style="font-family: monospace;">"median"</span>.
  </dd>
  </dl>
  <dl id="l_ncombine">
  <dt><b>ncombine = 6</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncombine' Line='ncombine = 6' -->
  <dd>The default number of images used to create the sky images.
  </dd>
  </dl>
  <dl id="l_nmin">
  <dt><b>nmin = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nmin' Line='nmin = 3' -->
  <dd>The minimum number of images used to create the sky images.
  </dd>
  </dl>
  <dl id="l_nlorej">
  <dt><b>nlorej = 0, nhirej = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlorej' Line='nlorej = 0, nhirej = 0' -->
  <dd>The number of high and low side pixels to reject if <i>combine</i> is <span style="font-family: monospace;">"average"</span>.
  </dd>
  </dl>
  <dl id="l_blank">
  <dt><b>blank = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blank' Line='blank = 0.0' -->
  <dd>The value assigned to undefined output image pixels, i.e. those for
  which the corresponding sky image pixel is undefined.
  </dd>
  </dl>
  <dl id="l_skysub">
  <dt><b>skysub = <span style="font-family: monospace;">"SKYSUB"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skysub' Line='skysub = "SKYSUB"' -->
  <dd>The sky subtraction processing keyword which is written to the output
  image when processing is complete.
  </dd>
  </dl>
  <dl id="l_holes">
  <dt><b>holes = <span style="font-family: monospace;">"HOLES"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='holes' Line='holes = "HOLES"' -->
  <dd>The homes mask name keyword which is written to the output image if an output
  holes mask is created.
  </dd>
  </dl>
  <dl id="l_cache">
  <dt><b>cache = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cache' Line='cache = yes' -->
  <dd>Cache the input images in memory if possible ?
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about the progress of the task ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  RSKYSUB computes the average sky image for each image in the input image
  list <i>inlist</i> using a running mean or median technique and subtracts
  it from the input image to create the output sky subtracted images
  <i>outlist</i>. The input image list is assumed to be ordered by time of
  observation. If the input image masks list <i>imasks</i> is defined then the
  input image pixels in the bad pixel regions are removed from the sky statistics
  and sky image computation. RSKYSUB optionally creates a list of output pixel
  masks <i>omasks</i> and a list of holes masks <i>hmasks</i>.
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
  <span style="font-family: monospace;">".pl"</span> format, or any supported integer image format, e.g. <span style="font-family: monospace;">".imh"</span>, <span style="font-family: monospace;">".fits"</span>, etc.
  </p>
  <p>
  The optional output pixel masks <i>omasks</i> are a combination of the
  input image masks and the scaling factor computation masks. They consist
  entirely of 0's and 1's with 0's defining the good data regions.
  </p>
  <p>
  The optional output holes masks <i>hmasks</i> which specify those pixels
  in the output images which are undefined consist entirely of 1's and 0's
  with 0's defining the holes.
  </p>
  <p>
  Before beginning the sky subtraction step RSKYSUB computes a scaling factor for
  each individual input image in <i>inlist</i> and stores it in the input image
  header keyword <i>skyscale</i>. If <i>scale</i> is <span style="font-family: monospace;">"median"</span> then the median of
  the input image pixels is computed using the input image masks <i>imasks</i>,
  the good data limits <i>lower</i> and <i>upper</i>, the clipping factors
  <i>maxiter</i>, <i>lnsigrej</i>, and <i>unisgrej</i>, and the histogram
  resolution parameter <i>binwidth</i>. The scaling factor is set to 1 / median.
  If <i>scale</i> is <span style="font-family: monospace;">"none"</span>, <span style="font-family: monospace;">"!&lt;keyword&gt;"</span>, or <span style="font-family: monospace;">"@&lt;file&gt;"</span> the individual
  scale factors are set to 1, read from the input image header keyword
  <i>&lt;keyword&gt;</i>, or from a file <i>@&lt;file&gt;</i> respectively. If <i>rescale</i> is
  yes and <i>scale</i> is <span style="font-family: monospace;">"median"</span> then the scaling computation is  redone
  regardless of whether or not the <i>skyscale</i> keyword is present in the
  input image header.
  </p>
  <p>
  RSKYSUB computes the sky image for each input image by multiplying each
  input image by the value of its scaling factor  and then computing the
  combination of <i>ncombine</i> neighbor images using the algorithm
  specified by <i>combine</i>. If <i>combine</i> is average then the
  <i>nlorej</i> and <i>nhirej</i> lowest and highest pixels are rejected from
  the stack to be combined. For example if the number of input images is 25 and
  ncombine is 6 then images 2-4 are used to compute the sky image for image 1,
  images 10-12 and 14-16 are used to compute the sky for image 13, and images
  22-24 are used to compute the sky image for image 25. There must be a minimum
  of <i>nmin</i> neighbor images or the sky image will not be computed. If the
  input masks are defined then pixels in bad regions are also rejected
  from the final sky image computation. Undefined output image pixels,
  i.e. those for which the corresponding sky image pixel is undefined, are
  assigned the value <i>blank</i>. The sky subtraction processing keyword
  <i>skysub</i> is written to the output image when sky subtraction is complete.
  </p>
  <p>
  If <i>cache</i> is <span style="font-family: monospace;">"yes"</span> then RSKYSUB will attempt to buffer the active images
  in memory and will run significantly faster. If <i>verbose</i> = yes then
  the task prints messages about its actions as it goes along.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Sky subtract a list of 25 images without masking.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rskysub @inlist @outlist maxiter=10 lnsigrej=5.0 unsigrej=5.0
  </pre></div>
  <p>
  2. Sky subtract the same list of 25 images with masking where the masks
  are assumed to be stored in the BPM keyword.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rskysub @inlist @outlist imasks="!BPM" maxiter=10 lnsigrej=5.0 \
  unsigrej=5.0
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
  imcombine, imexpr
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

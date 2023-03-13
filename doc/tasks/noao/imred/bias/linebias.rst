.. _linebias:

linebias: Fit and subtract an average line bias
===============================================

**Package: bias**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  linebias input output
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Images to be bias subtracted.  The images may not contain image sections.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output bias subtracted images.  An output images may be the same as its
  matching input image.  The output image pixel type will real regardless
  of the input image pixel type.
  </dd>
  </dl>
  <dl id="l_bias">
  <dt><b>bias = <span style="font-family: monospace;">"[]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bias' Line='bias = "[]"' -->
  <dd>Bias section appended to the input image to define the bias region.
  The default section or an empty string will use the full image.
  </dd>
  </dl>
  <dl id="l_trim">
  <dt><b>trim = <span style="font-family: monospace;">"[]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='trim' Line='trim = "[]"' -->
  <dd>Trim section appended to the input image to define the region to be
  bias subtracted and output.  The default section or an empty string
  will use the full image.
  </dd>
  </dl>
  <dl id="l_median">
  <dt><b>median = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='median' Line='median = no' -->
  <dd>Take the median of the bias lines?  If no then the bias lines are averaged.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"spline3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "spline3"' -->
  <dd>The function fit to the average bias line.  The functions are <span style="font-family: monospace;">"legendre"</span>,
  <span style="font-family: monospace;">"chebyshev"</span>, <span style="font-family: monospace;">"spline1"</span>, or <span style="font-family: monospace;">"spline3"</span>.  Abbreviations are allowed.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order' -->
  <dd>The order (number of terms or number of spline pieces) in the function.
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_reject' Line='low_reject = 3.0' -->
  <dd>The low sigma rejection factor.
  </dd>
  </dl>
  <dl id="l_high_reject">
  <dt><b>high_reject = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='high_reject' Line='high_reject = 3.0' -->
  <dd>The high sigma rejection factor.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 1' -->
  <dd>The maximum number of rejection iterations.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Fit the average bias line interactively?
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = ""' -->
  <dd>Name of a log file.  If no file name is given then no log file is kept.
  </dd>
  </dl>
  <dl id="l_logfiles">
  <dt><b>logfiles = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfiles' Line='logfiles = ""' -->
  <dd>List of log files.  If no file name is given then no log file is kept.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Graphics output device for interactive graphics.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  For each input image in the input image list an average or median bias line
  is determined from the bias region.  The bias region
  is defined by the bias section applied to the input image.  A function of
  the image columns is fit to the average bias line.  This function is subtracted
  from each image line in the trim region.  The trim region is defined by the
  trim section applied to the input image.  The bias subtracted and trimmed
  image is output to the output image.  The input and output images may not
  contain sections and the number of images in each list must be the same.
  </p>
  <p>
  If the interactive flag is set then the user may interactively examine
  and fit the average bias line.  The interactive fitting is done using the
  interactive curve fitting routine (see icfit).  Before each image is
  processed a prompt of the form <span style="font-family: monospace;">"linebias image (yes)? "</span> is given.
  A response of yes allows interactive fitting for the specified image
  while a response of no uses the last defined fitting parameters.
  The default value is accepted with a carriage return.  The possible
  responses are <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"YES"</span>, or <span style="font-family: monospace;">"NO"</span>.  The capitalized responses
  permanently set the response to yes or no and the prompt is not
  issued again for the remaining images.  Thus, a response of NO processes
  the remaining images non-interactively while a response of YES processes
  the remaining image interactively without prompting.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The bias region for a set of images occupies columns 1 to 800 and lines
  801 to 832.  To subtract the bias and remove the bias region:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; linebias.bias = "[*, 801:832]"
  cl&gt; linebias.trim = "[*, 1:800]"
  cl&gt; linebias ccd* ccd*
  linebias ccd001 (yes)? yes
  linebias ccd002 (yes)?
  linebias ccd003 (no)? NO
  </pre></div>
  <p>
  The first two lines set the bias and trim parameters.  These parameters
  could be temporarily set on the command line but generally these parameters
  are only changed when new instruments are used.  The first image
  is interactively fit and the fitting order is change to 2.  The
  second image is examined and the fit found to be acceptable.  All remaining
  image are then fit non-interactively using the same fitting parameters.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_LINEBIAS">
  <dt><b>LINEBIAS V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='LINEBIAS' Line='LINEBIAS V2.10.3' -->
  <dd>The output pixel type is now real instead of preserving the pixel type
  of the input image.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  icfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

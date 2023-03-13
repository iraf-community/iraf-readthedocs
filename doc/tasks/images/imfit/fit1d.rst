.. _fit1d:

fit1d: Fit a function to image lines or columns
===============================================

**Package: imfit**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  fit1d input output type
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Images to be fit.  The images may contain image sections.  Only the region
  covered by the section will be modified in the output image.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output images to be created or modified.  The number of output images
  must match the number of input images.  If an output image does not exist
  it is first created and initialized to zero for fit types <span style="font-family: monospace;">"fit"</span> and
  <span style="font-family: monospace;">"difference"</span> and to one for fit type <span style="font-family: monospace;">"ratio"</span>.
  </dd>
  </dl>
  <dl id="l_type">
  <dt><b>type</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='type' Line='type' -->
  <dd>Type of output.  The choices are:
  <dl>
  <dt><b>fit      </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='fit' Line='fit      ' -->
  <dd>An image created from the function fits to the image lines.
  </dd>
  </dl>
  <dl>
  <dt><b>difference</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='difference' Line='difference' -->
  <dd>The difference between the image and the fit (i.e. residuals).
  </dd>
  </dl>
  <dl>
  <dt><b>ratio</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='ratio' Line='ratio' -->
  <dd>The ratio of the image and fit.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_bpm">
  <dt><b>bpm = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bpm' Line='bpm = ""' -->
  <dd>List of bad pixel masks.  This may be a null string to not use a
  bad pixel mask, a single mask that applies to all input images, or
  a matching list.  The value may also be !&lt;keyword&gt; to specify a keyword whose
  value is the mask to use.
  </dd>
  </dl>
  <dl id="l_axis">
  <dt><b>axis = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='axis' Line='axis = 1' -->
  <dd>Axis along which the one dimensional fitting is done.  Axis 1 corresponds
  to fitting the image lines and axis 2 corresponds to fitting the columns.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>If <b>interactive</b> is set to yes, a plot of the fit is drawn and the
  cursor is available for interactively examining and adjusting the fit.
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample' Line='sample = "*"' -->
  <dd>Lines or columns to be used in the fits.
  </dd>
  </dl>
  <dl id="l_naverage">
  <dt><b>naverage = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='naverage' Line='naverage = 1' -->
  <dd>Number of sample points to combined to create a fitting point.
  A positive value specifies an average and a negative value specifies
  a median.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = spline3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = spline3' -->
  <dd>Function to be fit to the image lines or columns.  The functions are
  <span style="font-family: monospace;">"legendre"</span> (legendre polynomial), <span style="font-family: monospace;">"chebyshev"</span> (chebyshev polynomial),
  <span style="font-family: monospace;">"spline1"</span> (linear spline), and <span style="font-family: monospace;">"spline3"</span> (cubic spline).  The functions
  may be abbreviated.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 1' -->
  <dd>The order of the polynomials or the number of spline pieces.
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 0., high_reject = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_reject' Line='low_reject = 0., high_reject = 0.' -->
  <dd>Rejection limits below and above the fit in units of the residual sigma.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 1' -->
  <dd>Number of rejection iterations.
  </dd>
  </dl>
  <dl id="l_grow">
  <dt><b>grow = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grow' Line='grow = 0.' -->
  <dd>When a pixel is rejected, pixels within this distance of the rejected pixel
  are also rejected.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Graphics output device for interactive graphics.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">"stdgcur"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = "stdgcur"' -->
  <dd>Graphics cursor input.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A one dimensional function is fit to each line or column of the input images.
  The function may be a legendre polynomial, chebyshev polynomial,
  linear spline, or cubic spline of a given order or number of spline pieces.
  The output image is of pixel type real and is formed from the fitted
  function values, the difference or residuals of the fit (pixel value -
  fitted value), or the ratio between the pixel values and the fitted values.
  </p>
  <p>
  The output image may exist in which case a section in the input image is
  applied to the output image.  Thus, a section on the input image causes only
  that part of the output image to be changed.  If the output image does not
  exist it is first created with a size given by the full (without a section)
  input image and initialized to zero for fit and difference output types
  and one for ratio output types.
  </p>
  <p>
  A bad pixel mask may be specified to exclude data from the fitting.  Any
  non-zero value in the mask is excluded.   It appears in the interactive
  fitting in the same way as manually deleted points.  The mask is matched to
  the input image(s) as described by <b>pmmatch</b>.  The default is matching
  in physical coordinates.
  </p>
  <p>
  The points fit are determined by selecting a sample of lines or columns
  specified by the parameter <i>sample</i> and taking either the average or
  median of the number of points specified by the parameter <i>naverage</i>.
  The type of averaging is selected by the sign of the parameter and the number
  of points is selected by the absolute value of the parameter.
  The sample points are specified relative to any image sections.
  </p>
  <p>
  If <i>low_reject</i> and/or <i>high_reject</i> are greater than zero the sigma
  of the residuals between the fitted points and the fitted function is computed
  and those points whose residuals are less than <i>-low_reject</i> * sigma
  and greater than <i>high_reject</i> * sigma are excluded from the fit.
  Points within a distance of <i>grow</i> pixels of a rejected pixel are also
  excluded from the fit.  The function is then refit without the rejected points.
  This rejection procedure may be iterated a number of times given by the
  parameter <i>niterate</i>.
  </p>
  <p>
  The fitting parameters (<i>sample, naverage, function, order, low_reject,
  high_reject, niterate, grow</i>)
  may be adjusted interactively if the parameter <i>interactive</i> is yes.
  Lines or columns from the image are selected to be fit with the <b>icfit</b>
  package.  A single column or line may be chosen or a blank-separated range
  may be averaged.  Note that the averaging applies only to the graphed
  data used to set the fitting parameters.  The actual image lines and columns
  are fit individually.  The interactive cursor mode commands for this package
  are described in a separate help entry under <span style="font-family: monospace;">"icfit"</span>.  Line 1 is automatically
  selected for one dimensional images and any number of lines or columns may be
  selected for two dimensional images.  Note that the lines or columns are
  relative to the input image section; for example line 1 is the first line of
  the image section and not the first line of the image.  When an end-of-file or
  no line(s) or column(s) are given then the last selected fitting parameters
  are used on each line or column of the image.  This step is repeated for
  each image in the input list.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To create a smoothed version of an image by fitting the image lines:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fit1d image fitimage fit
  </pre></div>
  <p>
  If the interactive flag is set and the image is two dimensional then a prompt
  for an image line is printed:
  </p>
  <div class="highlight-default-notranslate"><pre>
  image: Fit line = 100 200
  </pre></div>
  <p>
  The selected lines are averaged, graphed, and the interactive options for
  setting and fitting the line are used.  Exiting with <span style="font-family: monospace;">'q'</span> or return prompts for
  another line if the image is two dimensional.  When the fitting parameters
  are suitably set then respond with end-of-file or return to fit all the lines
  of the image and create the output image.
  </p>
  <p>
  2.  To subtract a linear function fit to columns 10 to 20 and 80 to 100 from
  columns 10 to 100 and to subtract another linear function fit to lines
  110 to 120 and 180 to 200 from columns 110 to 200:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fit1d image1[10:100,*] output diff axis=2 sample="1:11,71:91"
  cl&gt; fit1d image1[110:200,*] output diff axis=2 sample="1:11,71:91"
  </pre></div>
  <p>
  Pixels outside columns 10 to 100 and 110 to 200 are not affected.  Note that the
  sample points are specified relative to the image sections.  The script
  <b>background</b> is available in other packages for doing background
  subtractions.
  </p>
  <p>
  3.  To determine a small scale response image:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fit1d image1 flat ratio
  </pre></div>
  <p>
  The task <b>imred.generic.flat1d</b> is available for making flat field images
  by this method with the addition of an extra parameter to limit the data values
  for which the ratio is computed.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  imred.generic.background, imred.generic.flat1d
  xtools.icfit, lineclean, imsurfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

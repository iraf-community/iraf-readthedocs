.. _lineclean:

lineclean: Replace deviant pixels in image lines
================================================

**Package: imfit**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <div class="highlight-default-notranslate"><pre>
  lineclean input output
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input images to be cleaned.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output cleaned images.  The number of output images must be the same as the
  number of input images.
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample' Line='sample = "*"' -->
  <dd>Columns to be used in fitting the cleaning function.
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
  <dd>Cleaning function to be fit to the image lines.  The functions are:
  <dl>
  <dt><b>legendre</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='legendre' Line='legendre' -->
  <dd>Legendre polynomial of the specified order.
  </dd>
  </dl>
  <dl>
  <dt><b>chebyshev</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='chebyshev' Line='chebyshev' -->
  <dd>Chebyshev polynomial of the specified order.
  </dd>
  </dl>
  <dl>
  <dt><b>spline1</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='spline1' Line='spline1' -->
  <dd>Linear spline of the specified number of pieces.
  </dd>
  </dl>
  <dl>
  <dt><b>spline3</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='spline3' Line='spline3' -->
  <dd>Cubic spline of the specified number of pieces.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 1' -->
  <dd>The order of the polynomials or the number of spline pieces.
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 2.5, high_reject = 2.5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_reject' Line='low_reject = 2.5, high_reject = 2.5' -->
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
  <dt><b>grow = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grow' Line='grow = 1.' -->
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
  A one dimensional function is fit to each line of the input images.
  The function may be a legendre polynomial, chebyshev polynomial,
  linear spline, or cubic spline of a given order or number of spline pieces.
  If <i>low_reject</i> and/or <i>high_reject</i> are greater than zero the sigma
  of the residuals between the fitted points and the fitted function is computed
  and those points whose residuals are less than <i>-low_reject</i> * sigma
  and greater than <i>high_reject</i> * sigma are excluded from the fit.
  Points within a distance of <i>grow</i> pixels of a rejected pixel are also
  excluded from the fit.  The function is then refit without the rejected points.
  This rejection procedure may be iterated a number of times given by the
  parameter <i>niterate</i>.  Finally, the
  rejected points in the input image are replaced by the fitted values
  to create the output image lines.
  </p>
  <p>
  The output image may exist in which case a section in the input image is
  applied to the output image.  Thus, a section on the input image causes only
  that part of the output image to be cleaned.  If the output image does not
  exist it is first created by making a copy of the full (without a section)
  input image.
  </p>
  <p>
  The points fit are determined by selecting a sample of columns specified by
  the parameter <i>sample</i> and taking either the average or median of
  the number of points specified by the parameter <i>naverage</i>.
  The type of averaging is selected by the sign of the parameter and the number
  of points is selected by the absolute value of the parameter.
  The sample points are specified relative to any image section.
  </p>
  <p>
  The fitting parameters (<i>sample, naverage, function, order, low_reject,
  high_reject, niterate, grow</i>)
  may be adjusted interactively if the parameter <i>interactive</i> is yes.
  Lines from the image are selected to be fit with the <b>icfit</b> package.
  For images of greater than two dimensions sets of numbers giving the
  2nd, 3rd, etc. coordinates are entered.
  The image lines are specified relative to any image section.
  When an end-of-file or no line is given then the last selected fitting
  parameters are used on each line of the image.  This step is repeated for
  each image in the input list.  The interactive options are described
  in the help information <b>icfit</b>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To clean pixels deviating by more than 2.5 sigma:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lineclean image cleanimage
  </pre></div>
  <p>
  If the interactive flag is set then a prompt for an image line is
  printed:
  </p>
  <div class="highlight-default-notranslate"><pre>
  image: Fit line = 100
  </pre></div>
  <p>
  For a one or two dimensional image the line number is entered (1 for a one
  dimensional image).  For a three dimensional image two numbers are entered.
  For example:
  </p>
  <div class="highlight-default-notranslate"><pre>
  image: Fit line = 10 2
  </pre></div>
  <p>
  for line 10 of the second image plane.
  </p>
  <p>
  The selected line is graphed and the interactive options for setting and
  fitting the line are used.  Data points marked with diamonds indicate
  points to be replaced by the fitted value.  Exiting with <span style="font-family: monospace;">'q'</span> or return
  prompts for another line.  When the fitting parameters are suitably set
  then respond with end-of-file or return to fit all the lines of the image
  and create the output image.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fit1d, xtools.icfit, imsurfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

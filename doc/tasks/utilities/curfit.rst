.. _curfit:

curfit: Fit data with Chebyshev, Legendre or spline curve
=========================================================

**Package: utilities**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  curfit input 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The data to be fit.  May be an image section, STDIN or a list of file names.
  </dd>
  </dl>
  <dl id="l_function">
  <dt><b>function = legendre</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = legendre' -->
  <dd>The type of function with which to fit the data.  Choices are 
  legendre, chebyshev, spline1 (linear spline) or spline3 (cubic spline).
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 4' -->
  <dd>The order of the fit or number of spline pieces. 
  </dd>
  </dl>
  <dl id="l_weighting">
  <dt><b>weighting = uniform</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='weighting' Line='weighting = uniform' -->
  <dd>The type of weighting for the fit. The options are:
  <dl>
  <dt><b>uniform</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='uniform' Line='uniform' -->
  <dd>The weight w = 1.0.  This option may be used for both list input and image
  input.
  </dd>
  </dl>
  <dl>
  <dt><b>user</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='user' Line='user' -->
  <dd>The weights are supplied by the user. This option may be used for list input
  only.
  </dd>
  </dl>
  <dl>
  <dt><b>statistical</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='statistical' Line='statistical' -->
  <dd>The weight w = 1.0 / y. This option can be used for both list and image data.
  </dd>
  </dl>
  <dl>
  <dt><b>instrumental</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='instrumental' Line='instrumental' -->
  <dd>The user supplies the sigmay for each point and w = 1.0 / sigmay ** 2.
  This option may be used for list input only.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>If <b>interactive</b> is set to yes, a plot of the fit is drawn and the
  cursor is available for interactively examining and adjusting the fit.
  </dd>
  </dl>
  <dl id="l_axis">
  <dt><b>axis = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='axis' Line='axis = 1' -->
  <dd>If <b>input</b> names an image or image section, this parameter specifies
  the axis along which the image is projected for fitting.
  </dd>
  </dl>
  <dl id="l_listdata">
  <dt><b>listdata = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listdata' Line='listdata = no' -->
  <dd>If <b>listdata</b> is set to yes, the only printed output will be the calculated 
  values for the X,Y pairs. This is useful as input to <i>graph</i> or some
  other list oriented program.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>If <b>verbose</b> is set to yes, the fitted (X,Y) pairs are listed in addition 
  to the default output of filename, function type, order, rejection parameters, 
  coefficients and their errors.
  </dd>
  </dl>
  <dl id="l_power">
  <dt><b>power = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='power' Line='power = no' -->
  <dd>If <b>power</b> is set to yes, the coefficients of the legendre or
  chebyshev polynomials will be converted to power series coefficients.
  </dd>
  </dl>
  <dl id="l_calctype">
  <dt><b>calctype = <span style="font-family: monospace;">"double"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='calctype' Line='calctype = "double"' -->
  <dd>Calculation datatype.  The two datatypes are <span style="font-family: monospace;">"real"</span> (single precision) and
  <span style="font-family: monospace;">"double"</span> (double precision).
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "stdgraph"' -->
  <dd>The output device for interactive graphics.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">"stdgcur"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = "stdgcur"' -->
  <dd>The source of graphics cursor input.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A curve is fit to data read from either an image section or a list.
  The type of curve is set by the <b>function</b> parameter as either
  a legendre polynomial, chebyshev polynomial, linear spline or cubic
  spline, with the order of the fit (or number of spline pieces) set by
  <b>order</b>.  If data is read from an image, the <b>axis</b> parameter
  is used to reduce the dimensionality of the image; it specifies the
  axis along which the image is projected.  For example, when <b>axis</b>
  = 1, the image is compressed to a column.  <b>Axis</b> = 2 would project
  the image along a line; <b>axis</b> = 3 indicates projection in the z
  direction, etc.
  </p>
  <p>
  The input data must be ordered in x because of a restriction in the
  interactive plotting package.  If the input is from a list, the data
  are sorted prior to fitting; image input data are assumed to be ordered
  in x and are not explicitly sorted by <i>curfit</i>.
  </p>
  <p>
  If the input is from a list the user may specify a set of weights,
  <b>weighting</b> = user or a set of errors, <b>weighting</b> =
  instrumental. An additional weighting option <b>weighting</b> = statistical
  can be used for both list and image data. The default is <b>weighting</b> =
  uniform.
  </p>
  <p>
  When <b>interactive</b> = yes, the curve is plotted and cursor commands allow
  for interactive examining and adjustment of the fit. 
  The full range of interactive cursor commands is available
  including those for changing the function type, order, and rejection criteria,
  and examining the residuals.
  </p>
  <p>
  The final fit parameters are written to STDOUT with the
  format controlled by parameters <b>verbose</b> and <b>listdata</b>.
  By default, the function type, order, and resulting chi-square are 
  printed as well as the coefficients and their standard deviations.  
  If <b>verbose</b> is set to yes, a list of X, Y_calculated, Y_input,
  and W_input is also printed.
  If <b>listdata</b> is set to yes, the only printed output will
  be a listing of X, Yc, Y and W. This provides a list suitable as input to
  <b>graph</b> or any other list oriented utility.  Setting <b>listdata</b> 
  to yes overrides the verbose option.
  </p>
  <p>
  When <b>power</b> = yes, the coefficients are converted to power series
  coefficients of the form a0 + a1*X + a2*X**2 +a3*X**3 ....
  Only legendre and chebyshev coefficients are converted; a conversion
  of spline coefficients is meaningless.  Also, errors in the coefficients
  are not converted.
  </p>
  <p>
  The user has a choice of single or double precision calculations.  Generally
  double precisions is used since the calculation time is only slightly
  longer.  The single precision calculation is used in many other tasks
  which do many fits.  This task provides a test tool to compare the
  results between the two levels of precision.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  The x,y pairs in file test.data are interactively fit with a fourth 
  order legendre polynomial.  The printed output is shown.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; curfit test.data
  NOAO/IRAF V2.0 Hammond@lyra Fri 11:45:41 13-Dec-85
  file = test.data
  function = legendre
  grow = 0.
  naverage = 1
  order = 4
  low_reject = 0., high_reject = 0.
  niterate = 1
  sample = *
  total points = 8
  sample points = 8
  nrejected = 0
  deleted = 0
  square root of reduced chi square = 3.008706E-6
          coefficient       error
  1          2.633E1        1.098E-6
  2          3.150E1        1.820E-6
  3          8.167E0        1.896E-6
  4        -1.621E-6        2.117E-6
  </pre></div>
  <p>
  2.  Fit a cubic spline to the last 12 columns of image <span style="font-family: monospace;">"m74"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; curfit m74[501:512,1:512] axis=2 func=spline3 order=5
  </pre></div>
  <p>
  3. Use <i>curfit</i> as a filter to overplot a smoothed curve to an existing
  plot of the data points.  The command line for <b>graph</b> is shown as
  well as the <b>curfit</b> command.  Note the interactive flag for 
  <b>curfit</b> is turned off.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; graph points.list point+ mark=box wx1=.13 xlab="X VALUES"\
  &gt;&gt;&gt; ylab="Y VALUES" title="Legendre fit to points.list"
  cl&gt; type points.list | curfit list+ inter- | graph append+
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  icfit,  polyfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

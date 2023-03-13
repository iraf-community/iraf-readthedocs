.. _continpars:

continpars: Edit continuum subtraction parameters
=================================================

**Package: rv**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  continpars
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_c_sample">
  <dt><b>c_sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='c_sample' Line='c_sample = "*"' -->
  <dd>Lines or columns to be used in the fits.  The default value (<span style="font-family: monospace;">"*"</span>) selects
  all pixels.  Type <i>help ranges</i> for a complete description of the
  syntax.
  </dd>
  </dl>
  <dl id="l_c_function">
  <dt><b>c_function = <span style="font-family: monospace;">"spline3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='c_function' Line='c_function = "spline3"' -->
  <dd>Continuum function to be fit to the image lines or columns.  The functions are
  <span style="font-family: monospace;">"legendre"</span> (Legendre polynomial), <span style="font-family: monospace;">"chebyshev"</span> (Chebyshev polynomial),
  <span style="font-family: monospace;">"spline1"</span> (linear spline), and <span style="font-family: monospace;">"spline3"</span> (cubic spline).  The functions
  may be abbreviated.
  </dd>
  </dl>
  <dl id="l_c_interactive">
  <dt><b>c_interactive = <span style="font-family: monospace;">"no"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='c_interactive' Line='c_interactive = "no"' -->
  <dd>Interactively fit the continuum? If set to yes, each spectrum will be fit
  interactively as they are read into the task if the <i>fxcor.continuum</i>
  parameter requires it.  The <i>fxcor</i> keystroke commands <span style="font-family: monospace;">'o'</span> and <span style="font-family: monospace;">'t'</span> will
  automatically fit the continuum interactively.
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
  <dl id="l_order">
  <dt><b>order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 1' -->
  <dd>The order of the polynomials or the number of spline pieces.
  </dd>
  </dl>
  <dl id="l_replace">
  <dt><b>replace = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='replace' Line='replace = no' -->
  <dd>Replace rejected data points with continuum fit points prior to the
  subtraction?  If set to yes, points lying outside the <i>low_reject</i> or
  <i>high_reject</i> limits are replaced by the fit values prior to the 
  continuum subtraction.  This can be useful in removing emission features 
  or cosmic ray events, but great care must be taken in setting other parameters
  in order to get satisfactory results.  Adjusting the <i>grow</i> or 
  <i>average</i> parameters, and using a low order function usually provide
  a good result. 
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 2.,  high_reject = 2.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_reject' Line='low_reject = 2.,  high_reject = 2.' -->
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
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>continpars</i> pset is used to control the continuum subtraction from 
  the data.  When the <i>fxcor</i> task is run in a batch mode, 
  the parameters are used to
  automatically process the data without intervention from the user.  In an
  interactive session, the user may experiment with different parameter values by
  changing them with the allowed colon commands.
  </p>
  <p>
  Continuum subtraction is done exactly as with the <i>onedspec.continuum</i>
  task.  (Details of the operation are described in the <i>continuum</i> 
  documentation.)  The fit to the spectra is subtracted from the data, thus 
  producing a continuum subtracted spectrum suitable for input to the correlation
  routines.  
  </p>
  <p>
  Users who require the full ability of the <i>onedspec.continuum</i> task to
  supply another form of output spectrum, such as the ratio of the fit, or
  who wish to make use of the <span style="font-family: monospace;">"clean"</span> option, should use that task and disable
  continuum subtraction in the <i>rv</i> package tasks.  More functionality is
  planned for this pset in the future.
  </p>
  </section>
  <section id="s_task_colon_commands">
  <h3>Task colon commands</h3>
  <p>
  The values of the <i>continpars</i> pset may be changed, displayed, or updated
  from within tasks that use them by means of various colon commands.  Simply 
  typing the parameter name will have the default action of printing the current
  value of that parameter. 
  </p>
  <dl>
  <dt><b>:unlearn	continpars</b></dt>
  <!-- Sec='TASK COLON COMMANDS' Level=0 Label='' Line=':unlearn	continpars' -->
  <dd>Reset the continpars pset parameters with their default values.
  The argument <span style="font-family: monospace;">"continpars"</span> must be present or else the command will default
  to the <i>fxcor</i> task command.
  </dd>
  </dl>
  <dl>
  <dt><b>:update	continpars</b></dt>
  <!-- Sec='TASK COLON COMMANDS' Level=0 Label='' Line=':update	continpars' -->
  <dd>Update the continpars pset parameters with the current values.
  The argument <span style="font-family: monospace;">"continpars"</span> must be present or else the command will default
  to the <i>fxcor</i> task command.
  </dd>
  </dl>
  <dl>
  <dt><b>:show	continpars</b></dt>
  <!-- Sec='TASK COLON COMMANDS' Level=0 Label='' Line=':show	continpars' -->
  <dd>Show the current values of the continpars pset parameters.
  The argument <span style="font-family: monospace;">"continpars"</span> must be present or else the command will default
  to the <i>fxcor</i> task command.
  </dd>
  </dl>
  <p>
  The following parameters will be displayed if it's name it typed, and a new 
  value accepted if an argument is given.
  </p>
  <div class="highlight-default-notranslate"><pre>
  :c_sample       [range_string]
  :naverage       [int_value]
  :c_function     [spline3|legendre|chebyshev|spline1]
  :order          [int_value]
  :low_reject     [int_value]
  :high_reject    [int_value]
  :niterate       [int_value]
  :grow           [int_value]
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the continuum parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  rv&gt; lpar continpars
  </pre></div>
  <p>
  2. Edit the continuum parameters
  </p>
  <div class="highlight-default-notranslate"><pre>
  rv&gt; continpars
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fxcor, onedspec.continuum, icfit, sfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'TASK COLON COMMANDS' 'EXAMPLES' 'SEE ALSO'  -->
  

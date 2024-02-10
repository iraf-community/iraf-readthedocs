.. _contsum:

contsum: Set continuum removal parameters for template making
=============================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  contsum
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_c_interactive">
  <dt><b>c_interactive no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='c_interactive' Line='c_interactive no' -->
  <dd>Fit continuum interactively (yes or no).  If yes, a graph of the spectrum
  and the continuum fit is plotted to stdgraph, with rejected points flagged.
  <span style="font-family: monospace;">"q"</span> accepts the fit and continues the main task, <span style="font-family: monospace;">"?"</span> prints options,
  <span style="font-family: monospace;">"d"</span> deletes points, <span style="font-family: monospace;">"u"</span> undeletes points, <span style="font-family: monospace;">"f"</span> refits and redraws the data.
  </dd>
  </dl>
  <dl id="l_c_sample">
  <dt><b>c_sample <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='c_sample' Line='c_sample "*"' -->
  <dd>Sample of points to use in fit. <span style="font-family: monospace;">"*"</span> = all.
  </dd>
  </dl>
  <dl id="l_c_function">
  <dt><b>c_function spline3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='c_function' Line='c_function spline3' -->
  <dd>Continuum fitting function (spline3 or legendre or chebyshev or spline1)
  </dd>
  </dl>
  <dl id="l_naverage">
  <dt><b>naverage 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='naverage' Line='naverage 1' -->
  <dd>Number of points in sample averaging
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order 1' -->
  <dd>Order of fitting function
  </dd>
  </dl>
  <dl id="l_s_low_reject">
  <dt><b>s_low_reject 2.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='s_low_reject' Line='s_low_reject 2.' -->
  <dd>Spectrum continuum fit minimum acceptance limit in sigma of fit
  </dd>
  </dl>
  <dl id="l_s_high_reject">
  <dt><b>s_high_reject 2.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='s_high_reject' Line='s_high_reject 2.' -->
  <dd>Spectrum continuum fit maximum acceptance limit in sigma of fit
  </dd>
  </dl>
  <dl id="l_t_low_reject">
  <dt><b>t_low_reject 2.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_low_reject' Line='t_low_reject 2.' -->
  <dd>Template continuum fit minimum acceptance limit in sigma of fit
  </dd>
  </dl>
  <dl id="l_t_high_reject">
  <dt><b>t_high_reject 2.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t_high_reject' Line='t_high_reject 2.' -->
  <dd>Template continuum fit maximum acceptance limit in sigma of fit
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate 10' -->
  <dd>Number of rejection iterations
  </dd>
  </dl>
  <dl id="l_grow">
  <dt><b>grow 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grow' Line='grow 1.' -->
  <dd>Rejection growing radius
  </dd>
  </dl>
  <p>
   
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>contsum</i> sets the parameters to be used to fit the continuum of
  spectra on which SUMSPEC is being run.
   
  </p>
  </section>
  <section id="s_example">
  <h3>Example</h3>
  <p>
  To set continuum fit parameters,
   
  	rvsao&gt; contsum
   
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  sumspec
   
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLE' 'SEE ALSO'  -->
  

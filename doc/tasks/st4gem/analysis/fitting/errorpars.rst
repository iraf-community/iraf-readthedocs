.. _errorpars:

errorpars: Pset with error-related parameters.
==============================================

**Package: fitting**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  errorpars
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The chi-square computation used in all tasks in the 'fitting' package
  depends on the availability of error estimates for each input datum. These 
  can be defined using a variety of sources. Also, when using the amoeba
  fitting method, some knowledge of data errors is needed for properly 
  computing estimates for the non-linear fit coefficient errors. 
  </p>
  <p>
  Individual error bars for each datum can be input from tables or lists.
  If the input data come from a list, then the third column specifies the 
  error bars' amplitude.  
  If the input data are taken from a table, then the 'errcolumn' parameter 
  specifies the error source.  If 'errcolumn' contains a single word, it is 
  taken as the name of the column that contains amplitudes of symmetrical 
  errors in the input table.  
  If the X and Y data come from different tables, then the table containing 
  Y data is also assumed to contain error data.  If 'errcolumn' is left as an
  empty string (<span style="font-family: monospace;">""</span>), it is assumed that there is no input error column. In
  this case, a default error bar of length 1.0 is applied to all data points.
  This makes the chi-square minimization to be equivalent to the unweighted
  root-mean-square (rms) residual minimization. The chi-square value output 
  by the fitting tasks in the case of constant 1.0 error bars will be related 
  to rms by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  
           d - 1
  chisq = ------- rms**2
           d - c
  
  </pre></div>
  <p>
  where d is the number of data points and c the number of fitted coefficients.
  </p>
  <p>
  If an error bar in the error column is set to INDEF, the data point will
  be discarded from the fit. No individual error bars can be input from 
  image data.
  </p>
  <p>
  If no error column is available, or when inputing image data, an estimate
  for the data error can nonetheless be input to the tasks trough parameter 
  'sigma'. This error will be applied equally to all data points, thus
  having the same effect on the minimization routine as the one described 
  above for a <span style="font-family: monospace;">"no error column"</span> input (that is, unweighted fit), but making
  the chi-square values output by the tasks look more realistic. If 'sigma' 
  is set 
  to anything different from INDEF and there is an input error column, the 
  value of 'sigma' will supersede the column input. 
  </p>
  <p>
  The 'errtype' parameter has dual meaning. It is used for both building
  input data error bars, as well as to control non-linear coefficient error 
  computation.
  In its first role, if set to either <span style="font-family: monospace;">"uniform"</span> or <span style="font-family: monospace;">"bars"</span>, input data error
  bars will be constructed as described above. If however 'errtype' is set
  to <span style="font-family: monospace;">"ccd"</span>, each individual datum error bar will be defined as a combination 
  of Poisson and readout errors. This will supersede any eventual input error 
  bar, either coming from a tabel column or from parameter 'sigma'. This 
  feature might be useful e.g. when inputing image data that otherwise can't 
  be properly weighted.
  </p>
  <p>
  The second use of the 'errtype' parameter is related to the internal
  algorithms used by the non-linear fitting tasks to estimate the coefficient
  errors. The Levenberg-Marquardt method computes the coefficient errors
  directly from the covariance matrix and these errors are output by the 
  tasks when the 'resample' parameter is set to <span style="font-family: monospace;">"no"</span>. 
  But the downhill simplex method (amoeba) is unable, by itself, to calculate 
  errors for the fitted function coefficients. The tasks thus resort to an 
  independent Monte Carlo resampling technique to allow estimation of those 
  errors. The resampling technique can be used also with the 
  Levenberg-Marquardt method. In that case the coefficient errors thus
  computed supersede the internal errors obtained from the covariance
  matrix.
  </p>
  <p>
  This resampling technique works as follows: after fitting the function, 
  the independent variable vector is replicated N times, each data point 
  being replaced by the fitted function value plus noise with dispersion 
  given by one of three criteria: (i) directly the dispersion of the original 
  data around the fit; (ii) error bar of each point, or (iii) ccd-type error. 
  For each replication, the function is re-fitted, and the error estimate for 
  each coefficient is the dispersion of the N obtained values. Parameter 
  'errtype' tells the tasks which one of the above ways must be used to 
  generate the replicas's scatter. The <span style="font-family: monospace;">"uniform"</span> option uses the rms of the 
  fit. The <span style="font-family: monospace;">"bars"</span> option uses the Y error bar of each datum, taken either from 
  column specified by the 'errcolumn' parameter, or from the 'sigma' parameter.
  The <span style="font-family: monospace;">"ccd"</span> option assumes that the independent variable values are subject 
  to counting statistics and may have an added component of readout noise.
  </p>
  <p>
  Both <span style="font-family: monospace;">"bars"</span> and <span style="font-family: monospace;">"ccd"</span> modes use independent error information, so the
  coefficient errors thus computed should be representative of the <span style="font-family: monospace;">"true"</span> 
  errors. The <span style="font-family: monospace;">"uniform"</span> mode must be used as a last resort, since it in
  some way <span style="font-family: monospace;">"re-uses"</span> the information already present in the data (and model)
  to generate the replicas. Thus, coefficient errors computed with <span style="font-family: monospace;">"uniform"</span> 
  error type should be taken with a little more caution.
  </p>
  <p>
  It must be emphasized that coefficient errors obtained in that way are
  estimates which have a different nature from errors obtained from a 
  covariance matrix. In particular, the error values will show a 
  dependency on N, being more close to the <span style="font-family: monospace;">"true"</span> value the larger the N. 
  Usually the errors estimated by resampling are larger than errors 
  derived from the covariance matrix.
  </p>
  <p>
  Since the process of re-fitting the function several times can be time
  consuming, two more parameters are provided to control the error
  computation. Parameter 'resample' allows enabling/disabling of the
  tasks' resampling error feature. Parameter 'replicas' specifies the number
  of replicas to use in resampling. It is good practice to disable
  error computation until an acceptable solution is found, and then re-fit
  with error computation enabled. Extensive testing with artificial data
  showed that the fitted coefficient's statistical distribution is reasonably
  well sampled when 'replicas' is set to ~15-20.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>(errcolumn = <span style="font-family: monospace;">""</span> ) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(errcolumn = "" ) [string]' -->
  <dd>Column name for the error column, if fitting from a table. 
  </dd>
  </dl>
  <dl>
  <dt><b>(errtype = uniform) [string, allowed values: uniform | bars | ccd]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(errtype = uniform) [string, allowed values: uniform | bars | ccd]' -->
  <dd><br>
  Error type. Used to both generate replicas in the resampling for 
  coefficient error estimation (non-linear fit only), and to interpret input 
  error bars. 
  </dd>
  </dl>
  <dl>
  <dt><b>(resample = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(resample = no) [boolean]' -->
  <dd>Estimate coefficient errors on each non-linear fit ? 
  </dd>
  </dl>
  <dl>
  <dt><b>(sigma = INDEF) [real, min=1.E-10]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(sigma = INDEF) [real, min=1.E-10]' -->
  <dd>Error bar to be applied to all data points. If set to anything different
  from INDEF, it supersedes eventual error bars defined by 'errcolumn'
  parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>(epadu = 1.) [real, min=0.]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(epadu = 1.) [real, min=0.]' -->
  <dd>Gain, in electrons per ADU, for 'ccd' noise model.
  </dd>
  </dl>
  <dl>
  <dt><b>(readnoise = 0.) [real, min=0.]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(readnoise = 0.) [real, min=0.]' -->
  <dd>Read-out noise in electrons, for 'ccd' noise model.
  </dd>
  </dl>
  <dl>
  <dt><b>(replicas = 15) [integer, min=2]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(replicas = 15) [integer, min=2]' -->
  <dd>Number of replications in non-linear fit resampling.
  </dd>
  </dl>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  A detailed error analysis using artificial data sets showed that the 
  coefficient error estimates generated by the resampling technique
  may under or overestimate the <span style="font-family: monospace;">"true"</span> errors measured in the data set 
  ensembles by factors of up to 20 percent, in particular when Poisson
  noise is involved.
  On the other hand, the error estimates generated by the linear fitting task 
  'gfit1d', for power-series polynomials and when using either ccd-type data 
  or inputing data error bars to properly compute chi-square, underestimate 
  the true errors by large factors (2-5). When error information is not 
  input to 'gfit1d', however, the power-series coefficient errors show the 
  same behavior as in the non-linear case.
  </p>
  <p>
  Some bias, in the range of 0.5-2 percent, may also affect the coefficients.
  This seems to be highly dependent on functional form and signal-to-noise
  ratio.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  <span style="font-family: monospace;">"Error and bias in the ST4GEM fitting package"</span>, I. Busko, ADASS VI,
  PASP Conf. Series 1997. 
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  nfit1d, ngaussfit, n2gaussfit, gfit1d
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

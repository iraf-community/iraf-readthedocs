.. _fitband:

fitband: Fit a passband model to data using Amoeba simplex method.
==================================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fitband input obsmode
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The task will fit a model passband to an observed throughput stored in
  a throughput table. You specify an expression containing free
  variables and initial values of these variables. The task then
  searches for values of those variables which minimize the squared
  difference between the model passband and the passband stored in the
  table. When the task finds the optimized solution, it writes the
  fitted values of the free variables back to the parameter file and
  prints the expression with the fitted values substituted for the free
  variables. 
  </p>
  <p>
  The name of the throughput table is given by the task parameter
  'input'. The model passband is specified by task parameter 'obsmode'.
  If the model passband is too long to fit in the task parameter (63
  characters max), the model passband can be placed in a file. The task
  parameter should then be set to the file name preceded by an <span style="font-family: monospace;">"@"</span>. If
  the model passband is placed in a file, the expression may be split
  over more than one line wherever a blank is a legal character in the
  expression. The variables in the model passband are indicated by a
  dollar sign followed by a digit. The initial values of these variables are
  given by setting task parameters vone through vnine. All variables not
  used should be set to INDEF. The model passband expression
  should not skip variables, for example, if the model contains three
  free variables, they should be named $1, $2, and $3, not $1, $2, and
  $4. Upon exiting the task these vone through vnine will contain the
  final fitted values of the free variables.
  </p>
  <p>
  The task can use two different methods to compute the least squares
  fit: the Levenberg Marquardt method and the downhill simplex method,
  sometimes called the amoeba method. The method used is selected by the
  task parameter 'slow'. The downhill simplex method is used if slow is
  set to yes. The downhill simplex method is slow because it requires
  more iterations to converge to a solution. In compensation, however,
  it converges to the solution over a larger range of initial values
  than the Levenberg Marquardt method. However, the initial values of
  the free variables should always be as accurate as possible as neither
  method will converge to a solution from arbitrarily chosen initial
  values of the free variables. If the inital values are outside the
  range of convergence, the task may either compute a false solution or
  wander outside the range where the model expession is defined and
  terminate with an error.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name]' -->
  <dd>The name of a throughput file. The throughput table can have the
  columns WAVELENGTH, THROUGHPUT, and ERROR. These columns contain the
  wavelength, throughput at that wavelength, and error in the
  measurement of throughput, respectively. The ERROR column is optional.
  If the throughput file is an ascii file, the first and second columns
  are the wavelength and throughput with an optional third column
  containing the error. 
  </dd>
  </dl>
  <dl id="l_spectrum">
  <dt><b>spectrum [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectrum' Line='spectrum [string]' -->
  <dd>The model passband expression to be fitted to the throughput
  data. The free variables in the expression are indicated by a dollar
  sign followed by a digit. The model passband can be placed in a file,
  whose name is passed to this parameter, preceded by a <span style="font-family: monospace;">"@"</span> character,
  command. Newlines may be placed in the expression wherever blanks are
  legal in a synphot expression. The form of a synphot expression is
  discussed in detail in the help file for the 'calcband' task.
  </dd>
  </dl>
  <dl>
  <dt><b>(output = <span style="font-family: monospace;">"none"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(output = "none") [string]' -->
  <dd>The name of the output table containing the fitted passband. If
  'output' is set to <span style="font-family: monospace;">"none"</span> or left blank, no table will be produced.
  The output table contains the model passband expression evaluated with
  the fitted values of the free variables. The header of the table
  contains the names of the graph and component lookup tables and the
  model expression.
  </dd>
  </dl>
  <dl>
  <dt><b>(ftol = 1.0e-5) [real, min = 0.0,  max = INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ftol = 1.0e-5) [real, min = 0.0,  max = INDEF]' -->
  <dd>The fractional tolerance convergence criterion. Iteration of the least
  square fit ceases when the scaled distance between two successive
  estimates of the free variables is less than this value. Each
  component of the scaled distance is scaled by dividing the difference
  between the two estimates by half their sum. Please note that the fit
  soulution may not converge to an arbitrarily small value, instead it
  may cycle between several values, so setting 'ftol' to too small a
  value may result in failure of the solution to converge.
  </dd>
  </dl>
  <dl>
  <dt><b>(maxiter = 500) [int, min = 1, max = INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(maxiter = 500) [int, min = 1, max = INDEF]' -->
  <dd>The maximum number of iterations to be performed. If convergence is
  not achieved in this number of iterations, then the task stops
  execution with a warning message to that effect.
  </dd>
  </dl>
  <dl>
  <dt><b>(nprint = 0) [int, min = 0, max = INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nprint = 0) [int, min = 0, max = INDEF]' -->
  <dd>The number of iterations between diagnostic prints. If 'nprint' is set
  to zero, there will be no diagnostic prints. Diagnostic prints are
  sent to STDERR and contain the number of the iteration, the chi
  squared value, and the model passband with the trial values of the
  free variables.
  </dd>
  </dl>
  <dl>
  <dt><b>(slow = no) [bool]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(slow = no) [bool]' -->
  <dd>Select which method to use to compute the least squares fit. If 'slow'
  is set to no, it uses the Levenberg Marquardt method and if it is set to
  yes, it uses the downhill simplex method. The Levenberg Marquardt
  method computes an approximation to the matrix of second derivatives
  of the model in order to extrapolate to the point where the chi
  squared is a minimum. The downhill simplex method constructs a polygon
  of trial points and replaces the point with the highest chi squared
  with a new point with a lower chi squared, chosen by one of a set of
  strategies. The Levenberg Marquardt method usually converges on the
  solution in a fewer number of iterations, but the downhill simplex
  method will converge to the solution from a wider range of initial
  estimates of the free variables. 
  </dd>
  </dl>
  <dl>
  <dt><b>(equal = no) [bool]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(equal = no) [bool]' -->
  <dd>Select whether to weight the data points when computing the chi
  squared. If 'equal' is set to no and the input table contains the
  error column, data points will be weighted according to their
  errors. Points with indefinite, negative, or zero errors are not used
  in the fit. If 'equal' is set to yes or the error column is zero,
  the data points will not be weighted.
  </dd>
  </dl>
  <dl>
  <dt><b>(vone = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vone = INDEF) [real]' -->
  <dd>The value of the first free variable. Before running this task, this
  parameter should contain the initial estimate of the first free
  variable and on exit it will contain the final fitted value. If this
  variable is not in the equation, it should be set to INDEF.
  </dd>
  </dl>
  <dl>
  <dt><b>(vtwo = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vtwo = INDEF) [real]' -->
  <dd>The value of the second free variable.
  </dd>
  </dl>
  <dl>
  <dt><b>(vthree = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vthree = INDEF) [real]' -->
  <dd>The value of the third free variable.
  </dd>
  </dl>
  <dl>
  <dt><b>(vfour = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vfour = INDEF) [real]' -->
  <dd>The value of the fourth free variable.
  </dd>
  </dl>
  <dl>
  <dt><b>(vfive = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vfive = INDEF) [real]' -->
  <dd>The value of the fifth free variable.
  </dd>
  </dl>
  <dl>
  <dt><b>(vsix = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vsix = INDEF) [real]' -->
  <dd>The value of the sixth free variable.
  </dd>
  </dl>
  <dl>
  <dt><b>(vseven = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vseven = INDEF) [real]' -->
  <dd>The value of the seventh free variable.
  </dd>
  </dl>
  <dl>
  <dt><b>(veight = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(veight = INDEF) [real]' -->
  <dd>The value of the eighth free variable.
  </dd>
  </dl>
  <dl>
  <dt><b>(vnine = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vnine = INDEF) [real]' -->
  <dd>The value of the ninth free variable.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Fit a gaussian to the f555w filter of the wfpc2. Equal is set to yes
  because the errors for the f555w filter are all zero.
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; fitband crwfpc2comp$wfpc2_f555w_001.tab "gauss($1,$2)*$3" \
  &gt;&gt;&gt; out=fit555w.tab nprint=1 vone=5500 vtwo=500 vthree=1 equal+
  
  irep = 1 chisq = 0.070178 exp = gauss(5500.,500.)*1.01
  irep = 2 chisq = 0.038999 exp = gauss(5446.848,1049.767)*0.6572117
  irep = 3 chisq =  0.01281 exp = gauss(5203.743,1899.694)*0.8564375
  irep = 4 chisq = 0.008162 exp = gauss(5317.004,1231.655)*1.021223
  irep = 5 chisq = 0.005793 exp = gauss(5250.328,1477.763)*0.9997244
  irep = 6 chisq = 0.005556 exp = gauss(5265.959,1366.362)*1.053696
  irep = 7 chisq =  0.00552 exp = gauss(5256.392,1402.267)*1.04326
  irep = 8 chisq = 0.005519 exp = gauss(5259.122,1389.024)*1.04894
  irep = 9 chisq = 0.005518 exp = gauss(5258.048,1393.428)*1.04723
  irep = 14 chisq = 0.005518 exp = gauss(5258.108,1393.239)*1.047264
  irep = 15 chisq = 0.005505 exp = gauss(5258.134,1393.157)*1.036914
  
  Final solution:
  gauss(5258.108,1393.239)*1.036895
  </pre></div>
  <p>
  Plot the ratio of the fit to the throughput table to see how good the
  fit is.
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; plband "crwfpc2comp$wfpc2_f555w_001.tab / fit555w.tab" \
  &gt;&gt;&gt; left=4000 right=8000
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by Bernie Simon based on XCAL code written by Keith Horne. The
  Levenberg Marquardt code was taken from the minpack library at Argonne
  National Laboratory. The downhill simplex code was adapted from
  Numerical Recipes.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  calcband
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

.. _fitspec:

fitspec: Fit a spectrum model to data using Amoeba simplex method.
==================================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fitspec input spectrum
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task will fit a model spectrum to an observed spectrum stored in
  a spectrophotometric table. You specify an expression containing free
  variables and initial values of these variables. The task then
  searches for values of those variables which minimize the squared
  difference between the model spectrum and the spectrum stored in the
  table. When the task finds the optimized solution, it writes the
  fitted values of the free variables back to the parameter file and
  prints the expression with the fitted values substituted for the free
  variables. 
  </p>
  <p>
  The name of the spectrophotometric table is given by the task
  parameter 'input'. The model spectrum is specified by task parameter
  'spectrum'. If the model spectrum is too long to fit in the task
  parameter (63 chracters max), the model spectrum can be placed in a
  file. The task parameter should then be set to the file name preceded
  by an <span style="font-family: monospace;">"@"</span>. If the model spectrum is placed in a file, the expression
  may be split over more than one line wherever a blank is a legal
  character in the expression. The variables in the model spectrum are
  indicated by a dollar sign followed by a digit. There are nine legal
  variables, $1 through $9. The initial values of these variables are
  given by setting task parameters vone through vnine. All variables not
  used should be set to INDEF. The model spectrum expression
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
  <dd>The name of a spectrophotometry file. The spectrophotometric table can
  have the columns WAVELENGTH, FLUX, STATERROR, and FWHM. The WAVELENGTH
  and FLUX columns contain the wavelength and values of flux at that
  wavelength, respectively. The STATERROR and FWHM columns contain the
  respective errors of the FLUX and WAVELENGTH columns. If the
  spectrophotometry file is an ascii file, the first through fourth
  columns are the wavelength, flux, staterror, and fwhm and the third
  and fourth columns are optional. The contents of the STATERROR column
  are used in weighting the data points if they are present and if
  'equal' is set to no. The FWHM column is not used by this task.
  </dd>
  </dl>
  <dl id="l_spectrum">
  <dt><b>spectrum [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectrum' Line='spectrum [string]' -->
  <dd>The model spectrum expression to be fitted to the spectrophotometric
  data. The free variables in the expression are indicated by a dollar
  sign followed by a digit. The model spectrum can be placed in a file,
  whose name is passed to this parameter, preceded by a <span style="font-family: monospace;">"@"</span> character,
  command. Newlines may be placed in the expression wherever blanks are
  legal in a synphot expression. The form of a synphot expression is
  discussed in detail in the help file for the 'calcspec' task.
  </dd>
  </dl>
  <dl>
  <dt><b>(output = <span style="font-family: monospace;">"none"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(output = "none") [string]' -->
  <dd>The name of the output table containing the fitted spectrum. If
  'output' is set to <span style="font-family: monospace;">"none"</span> or left blank, no table will be produced.
  The output table contains the model spectrum expression evaluated with
  the fitted values of the free variables. The flux units are the same
  as the input spectrophotmetry file. The header of the table contains
  the names of the graph and component lookup tables and the model
  expression. 
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
  squared value, and the model spectrum with the trial values of the
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
  staterror column, data points will be weighted according to their
  errors. Points with indefinite, negative, or zero errors are not used
  in the fit. If 'equal' is set to yes or the staterror column is zero,
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
  Fit a black body temperature, visual magnitude, and reddening to the
  spectrum of eta ursa majoris. Equal is set to yes because the visual
  region of this spectrum does not contain error estimates.
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; fitspec crcalspec$eta_uma_002.tab \
  &gt;&gt;&gt; "rn(bb($1),band(v),$2,vegamag)*ebmv($3)" \
  &gt;&gt;&gt; out="umafit.tab" nprint=1 vone=20000 vtwo=2 vthree=0 equal+
  </pre></div>
  <p>
  The task produces the following output:
  </p>
  <div class="highlight-default-notranslate"><pre>
  irep = 1 chisq = 25306.82 exp = rn(bb(20000.),band(v),2.,vegamag)
  *ebmv(0.01)
  irep = 2 chisq = 16473.78 exp = rn(bb(22098.21),band(v),2.162239,
  vegamag)*ebmv(0.01375842)
  irep = 3 chisq = 10925.13 exp = rn(bb(26996.77),band(v),2.250071,
  vegamag)*ebmv(0.06069669)
  irep = 4 chisq = 8347.195 exp = rn(bb(30768.06),band(v),2.076039,
  vegamag)*ebmv(0.1018063)
  irep = 5 chisq = 8064.211 exp = rn(bb(31439.05),band(v),2.074771,
  vegamag)*ebmv(0.1028053)
  irep = 6 chisq = 8062.454 exp = rn(bb(31473.2),band(v),2.078477,
  vegamag)*ebmv(0.1025254)
  irep = 7 chisq = 8062.335 exp = rn(bb(31474.32),band(v),2.078932,
  vegamag)*ebmv(0.1024742)
  irep = 8 chisq = 8062.316 exp = rn(bb(31474.33),band(v),2.078977,
  vegamag)*ebmv(0.1024683)
  irep = 9 chisq = 8048.326 exp = rn(bb(31474.1),band(v),2.078995,
  vegamag)*ebmv(0.1014501)
  
  Final solution:
  rn(bb(31473.12),band(v),2.057049,vegamag)*ebmv(0.1015078)
  </pre></div>
  <p>
  In order to see how good the fit is, plot the ratio of the spectrum to
  the fit:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; plband "crcalspec$eta_uma_002.tab / umafit.tab"
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
  calcspec
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

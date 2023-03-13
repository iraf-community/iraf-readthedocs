.. _fitparams:

fitparams: Compute the parameters of the transformation equations
=================================================================

**Package: photcal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fitparams observations catalogs config parameters
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_observations">
  <dt><b>observations</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observations' Line='observations' -->
  <dd>The list of files containing the observational data.  Observations files are
  multi-column text files whose columns are delimited by whitespace, and
  whose first column is usually reserved for the object id.
  All observations files in the list must have the same format.
  The format of legal observations files is described in further detail in
  the description section.
  </dd>
  </dl>
  <dl id="l_catalogs">
  <dt><b>catalogs</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catalogs' Line='catalogs' -->
  <dd>The list of files containing the catalog data.  Catalog files are
  multi-column text files whose columns are delimited by whitespace,
  and whose first column is always reserved for the object id.
  If more than one entry with the same id exists in the list of catalogs,
  only the first entry is used.
  All catalog files in the list must have the same format.
  The format of legal catalog files is described in further detail in
  the description section.
  </dd>
  </dl>
  <dl id="l_config">
  <dt><b>config</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='config' Line='config' -->
  <dd>The name of the configuration file. The configuration file is a text file
  specifying the format of the input catalog and observations files, and the
  form of the transformation
  equations. A brief description of the syntax and grammar of this file
  is given in the configuration file section.
  </dd>
  </dl>
  <dl id="l_parameters">
  <dt><b>parameters</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='parameters' Line='parameters' -->
  <dd>The name of the output database file.
  Parameters is a text database file to which the error analysis of the fit
  and the parameter values and errors for each transformation equation are
  written. 
  The output of fitparams is appended to parameters as a set of new records,
  one for each of the transformation equations. 
  If more than one record exists with the same record name, the 
  last record written takes precedence.
  </dd>
  </dl>
  <dl id="l_weighting">
  <dt><b>weighting = <span style="font-family: monospace;">"uniform"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='weighting' Line='weighting = "uniform"' -->
  <dd>The following weighting schemes are supported.
  <dl>
  <dt><b>uniform</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='uniform' Line='uniform' -->
  <dd>The data points are all assigned a weight of one.
  </dd>
  </dl>
  <dl>
  <dt><b>photometric</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='photometric' Line='photometric' -->
  <dd>The total error squared for each data point is set to the total error in the
  catalog variables squared plus the total error in the observations variables
  squared and the weight for each data point is set to 1.0 / error ** 2.
  This option assumes that all the sources of error are in the photometric
  indices (magnitudes and colors), that error columns (see the description
  of the configuration file below) have been declared for at least one
  photometric index, and that the contribution of each catalog or observations
  variable to the total error is weighted by the number of times it occurs
  in the transformation equation.
  If <i>addscatter</i> is <span style="font-family: monospace;">"yes"</span> then an additional <span style="font-family: monospace;">"scatter"</span> term is fit and
  added to the weights.
  </dd>
  </dl>
  <dl>
  <dt><b>equations</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='equations' Line='equations' -->
  <dd>The weight equation (see the description of the configuration file below)
  is evaluated for each point and the weight for that point is set to that
  value.  If there is no weight equation the weights are all set to one.
  If <i>addscatter</i> is <span style="font-family: monospace;">"yes"</span> then an additional <span style="font-family: monospace;">"scatter"</span> term is fit and
  added to the weights.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_addscatter">
  <dt><b>addscatter = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='addscatter' Line='addscatter = yes' -->
  <dd>Add an additional scatter term to the weights if the average error in the fit
  is much greater than the average error in the measurements? <i>Addscatter</i>
  has no effect if <i>weighting</i> is <span style="font-family: monospace;">"uniform"</span>. <i>Addscatter</i> is recommended
  if <i>weighting</i> is <span style="font-family: monospace;">"photometric"</span> as the intrinsic error in the
  transformations is often much greater than the formal errors of
  measurement and the scatter term stabilizes the fit.
  Users of the <i>weighting</i> equals <span style="font-family: monospace;">"equations"</span> option
  may wish to turn off <i>addscatter</i>.
  </dd>
  </dl>
  <dl id="l_tolerance">
  <dt><b>tolerance = 3.0e-5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tolerance' Line='tolerance = 3.0e-5' -->
  <dd>The convergence tolerance for the non-linear least squares fit.
  The fit will stop iterating 
  when the fractional change in the reduced chi-square of the residuals from 
  iteration to iteration is less than <i>tolerance</i>. 
  </dd>
  </dl>
  <dl id="l_maxiter">
  <dt><b>maxiter = 15</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxiter' Line='maxiter = 15' -->
  <dd>The maximum number of iterations for the non-linear least squares fit.
  When this number is reached the fitting process will terminate even
  if the fit has not converged.
  </dd>
  </dl>
  <dl id="l_nreject">
  <dt><b>nreject = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nreject' Line='nreject = 0' -->
  <dd>The maximum number of bad data rejection iterations. If <i>nreject</i> is
  greater than zero the initial fit is used
  to detect and reject deviant points before performing the final fit.
  No rejection is performed if <i>nreject</i> is less than or equal
  to zero.
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 3.0, high_reject = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_reject' Line='low_reject = 3.0, high_reject = 3.0' -->
  <dd>The lower and upper rejection limits in units of the rms of the fit.
  Points deviating from the initial fit by more than this amount are rejected
  before performing the final fit.  No rejection is done if both limits
  are zero.
  </dd>
  </dl>
  <dl id="l_grow">
  <dt><b>grow = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grow' Line='grow = 0.0' -->
  <dd>The default rejection growing radius. Points within a distance given
  by this parameter of any rejected point are also rejected.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Fit equations interactively ? When this parameter is <i>yes</i>, the user will 
  be presented with plots of the data and can interact with the fitting 
  process.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"STDOUT"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "STDOUT"' -->
  <dd>The name of the output text file to which selected detailed results of the
  fitting process are written.  By default logfile is the standard output.
  If logfile is <span style="font-family: monospace;">""</span>, logging is turned off altogether. Otherwise new
  output is appended to logfile which can therefor become quite large.
  </dd>
  </dl>
  <dl id="l_log_unmatched">
  <dt><b>log_unmatched = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='log_unmatched' Line='log_unmatched = yes' -->
  <dd>Write the list of observations with no corresponding catalog entries to
  logfile? This option is useful for checking for errors in the observed
  object id names and for users who like to run fitparams in non-interactive
  mode.
  </dd>
  </dl>
  <dl id="l_log_fit">
  <dt><b>log_fit = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='log_fit' Line='log_fit = no' -->
  <dd>Write the error analysis of the final fit in logfile? This option is
  useful for users who like to run fitparams in non-interactive mode.
  </dd>
  </dl>
  <dl id="l_log_results">
  <dt><b>log_results = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='log_results' Line='log_results = no' -->
  <dd>Write the results of the current fit to logfile? This option is
  useful for users who like to run fitparams in non-interactive mode.
  </dd>
  </dl>
  <dl id="l_catdir">
  <dt><b>catdir = <span style="font-family: monospace;">")_.catdir"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catdir' Line='catdir = ")_.catdir"' -->
  <dd>The directory containing the supported standard star catalogs.
  The default parameter value  redirects <i>catdir</i>
  to a package parameter of the same name. A list of standard
  catalogs may be obtained by printing the file <span style="font-family: monospace;">"photcal$catalogs/README"</span>.
  Alternatively the user may create their own standard star catalogs 
  and standard star catalog directory.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>The default graphics device. 
  This parameter is used only if <b>interactive=yes</b>.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input. When null the standard graphics cursor is used.
  Otherwise the specified cursor command file is used.
  This parameter is used only if <b>interactive=yes</b>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  FITPARAMS parses the configuration file <i>config</i> checking for
  grammar and syntax errors.  FITPARAMS attempts to recover from any
  errors and to finish parsing the configuration
  file, but it will not process the input data if errors are present.
  The configuration file is described briefly in the configuration file
  section and in detail in the help page for the configuration file.
  </p>
  <p>
  Once the configuration file is successfully parsed, FITPARAMS reads the list
  of catalog files and loads the values of the catalog variables
  declared in <i>config</i> into memory.
  If no catalog section is declared in <i>config</i>, if the catalog section
  is empty, or if catalogs is <span style="font-family: monospace;">""</span>, no catalog data is read
  and all the required input data is assumed to be in <i>observations</i>.
  After the catalog data is read, FITPARAMS reads the observations files
  <i>observations</i>, matches the object ids of the observations with the
  corresponding catalog object ids, and loads all the observations
  variables declared in <i>config</i> into memory. Id matching is disabled
  if no catalog
  data is read, otherwise only those observations which have a matching catalog
  entry will be used in the fit. If a catalog section declaration was made
  in <i>config</i>, even an empty one, FITPARAMS assumes that the object ids
  are in column 1 of <i>observations</i>.
  </p>
  <p>
  Legal <i>catalog</i> and <i>observations</i> files are multi-column text
  files whose columns are delimited by whitespace.
  The first column of a catalog file is <i>always</i> reserved for an object id.
  The first column of an observations file is <i>usually</i> reserved for an
  object id which can be
  used to match the observational data with the corresponding catalog data.
  All other columns may contain any quantity which can be
  expressed as an integer or real number.  Sexagesimal format numbers
  (hh:mm:ss) are interpreted internally as real numbers. The constant
  INDEF can be used to represent data that is missing or undefined.
  Double precision and complex data are
  not supported. Lines beginning with <span style="font-family: monospace;">"#"</span> are treated as comment lines.
  </p>
  <p>
  FITPARAMS solves the fit
  for each equation in the configuration file either interactively 
  or non-interactively depending on the value of <i>interactive</i>,
  and writes the solution in the output file <i>parameters</i> for later
  use by the evaluation routines EVALFIT or INVERTFIT.
  Selected results can also be written to <i>logfile</i> if
  any of the switches <i>log_unmatched</i>, <i>log_fit</i>, or <i>log_results</i>
  are enabled.
  In interactive mode the user can use all the interactive capabilities
  of the interactive non-linear least squares package INLFIT.
  INLFIT is described more fully below. 
  </p>
  </section>
  <section id="s_the_configuration_file">
  <h3>The configuration file</h3>
  <p>
  The configuration file is a text file which specifies how the data is
  organized in the input files and how the transformation
  equations are to be fit.
  </p>
  <p>
  The input data are assumed to come from two different sources that may
  be either in the same input file or in different input files.
  These sources are known as the <i>catalog</i> and the <i>observations</i>
  respectively.
  </p>
  <p>
  The <i>catalog</i> contains values indexed by a name called the
  matching name. This name must be in the first column of the
  catalog and is also assumed to be unique, i.e, each catalog
  entry is assumed to be unique.
  </p>
  <p>
  The <i>observations</i> are values that may be either indexed by a matching
  name if a catalog section is specified in the configuration file, or a
  stream of input values in an ordinary text file.
  If a catalog section is specified and non-empty, each observation is
  matched against the
  catalog entries, and only observations whose matching names are found in the
  catalog are used to compute the transformation equations.
  Otherwise all values are used.
  </p>
  <p>
  The configuration file is divided in three sections: the <i>catalog
  section</i> which describes the format of the catalog files, the
  <i>observations section</i> which describes the format of the observation 
  files, and the <i>transformation section</i> which defines the
  transformation equations in that order.
  </p>
  <p>
  The catalog and observations sections permit the user to assign
  names to the input file 
  columns. These columns can later be referenced by name in the configuration
  file by using these assigned names
  as if they were variables in a programming language.
  </p>
  <p>
  The transformation section is used to define the equations to solve,
  and assign initial values to the fitting parameters.
  The user may also optionally define equations for the derivatives of
  the transformation equations with respect to the parameters,
  the weights to be used in the fit, 
  the errors of the fit and the default equations to be
  plotted in the interactive fitting process.
  It is possible to specify any number of transformation equations in
  this section.
  </p>
  <p>
  SAMPLE CONFIGURATION FILES
  </p>
  <p>
  Example 1. Configuration file for reducing UBV photoelectric photometry.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Configuration file for reducing UBV photoelectric photometry.
  
  catalog
  
  V       2               # V magnitude
  BV      3               # B - V color
  UB      4               # U - B color
  
  observation
  
  v       2               # v instrumental magnitude
  b       3               # b instrumental magnitude
  u       4               # u instrumental magnitude
  ev      5               # error in v instrumental magnitude
  eb      6               # error in b instrumental magnitude
  eu      7               # error in u instrumental magnitude
  X       8               # airmass
  
  transformation
  
  fit   v1 = 0.0, v2=0.16, v3=-0.043
  VFIT: V = v1 + v - v2 * X + v3 * (b - v)
        weight(VFIT) = 1.0 / ev ** 2
        plot(VFIT) = V, V - (v1 + v - v2 * X + v3 * (b - v))
  
  fit    b1 = 0.0, b2=0.09, b3=1.21
  BVFIT: BV = b1 - b2 * X + b3 * (b - v)
         weight (BVFIT) = 1.0 / (eb ** 2 + ev ** 2)
         plot(BVFIT) = BV, BV - (b1 - b2 * X + b3 * (b - v))
  
  fit    u1 = 0.0, u2=0.300, u3=0.861
  UBFIT: UB = u1 - u2 * X + u3 * (u - b)
         weight (UBFIT) = 1.0 / (eu ** 2 + eb ** 2)
         plot(UBFIT) = UB, UB - (u1 - u2 * X + u3 * (u - b))
  </pre></div>
  <p>
  Example 2. Configuration file for reducing UBV CCD photometry.
  </p>
  <div class="highlight-default-notranslate"><pre>
  catalog
  
  V               2       # V magnitude
  BV              3       # B - V color
  UB              4       # U - B color
  error(V)        5       # error in V magnitude
  error(BV)       6       # error in B-V color
  error(UB)       7       # error in U-B color
  
  observation
  
  m1              2       # filter 1 instrumental magnitude
  error(m1)       3       # error in filter 1 instrumental magnitude
  Xm1             4       # airmass of filter 1  observation
  m2              6       # filter 2 instrumental magnitude
  error(m2)       7       # error in filter 2 instrumental magnitude
  Xm2             8       # airmass of filter 2 observation
  m3              10      # filter 3 instrumental magnitude
  error(m3)       11      # error in filter 3 instrumental magnitude
  Xm3             12      # airmass of filter 3 observation
  
  transformation
  
  fit   u1 = 27.0, u2=0.68, u3=0.05
  UFIT: m3 = u1 + V + BV + UB + u2 * Xm3 + u3 * UB
  
  fit   b1 = 26.0, b2=0.30, b3=0.18
  BFIT: m2 = b1 + V + BV + b2 * Xm2 + b3 * BV
  
  fit   v1 = 25.0, v2=0.17, v3=-0.02
  VFIT: m1 = v1 + V + v2 * Xm1 + v3 * BV
  </pre></div>
  </section>
  <section id="s_the_non_linear_interactive_fitting_package">
  <h3>The non-linear interactive fitting package</h3>
  <p>
  DESCRIPTION
  </p>
  <p>
  INLFIT fits an n-dimensional function to a set data
  points, iterating until the reduced chi-squared changes
  by less than <i>tolerance</i> percent between successive iterations, or
  machine precision is reached and the fit converges, or until the maximum number
  of iterations <i>maxiter</i> is reached.  If the maximum number
  of iterations is reached before convergence a status flag
  is set.
  </p>
  <p>
  After computing an initial fit, INLFIT presents the user with a plot of
  the fit and activates the graphics cursor.
  At this point the user may examine and/or interact with the fit by,
  for example, reprogramming the default graph keys,
  editing the default convergence or bad data rejection parameters,
  deleting and undeleting points, 
  altering which parameters in the fitting function are actually to be
  fit and which are to be held constant, and refitting the data.
  </p>
  <p>
  If <i>nreject</i> is greater than zero the RMS of the residuals is computed
  and points whose residuals are less than <i>low_reject</i> * RMS
  or <i>high_reject</i> * RMS value are excluded from the fit. Points within
  a distance <i>grow</i> of a rejected point are also excluded from
  the fit. The function is then refit without the rejected points.
  The rejection algorithm is executed until the number of rejection
  iterations reaches <i>nreject</i> or no more points are rejected.
  </p>
  <p>
  ALGORITHMS
  </p>
  <p>
  INLFIT uses the standard Levenberg-Marquardt non-linear least squares
  algorithm to fit the data. Detailed descriptions of the algorithm can
  be found in the following two references.
  </p>
  <div class="highlight-default-notranslate"><pre>
  1. Bevington, P.R., 1969, Data Reduction and Error Analysis for the
     Physical Sciences, Chapter 11, page 235.
  
  2. Press, W.H. et al., 1986, Numerical Recipes: The Art of Scientific
     Computing, Chapter 14, page 523.
  </pre></div>
  <p>
  CURSOR COMMANDS
  </p>
  <p>
  The following interactive cursor keystroke commands are available from
  with the INLFIT package.
  </p>
  <dl>
  <dt><b>?</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line='?' -->
  <dd>The terminal is cleared and a menu of cursor keystroke and colon commands
  is printed.
  </dd>
  </dl>
  <dl id="l_c">
  <dt><b>c</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='c' Line='c' -->
  <dd>The id, coordinates of the data point nearest the cursor, along with the
  function value, the fitted value and the residual, are printed on the status
  line.
  </dd>
  </dl>
  <dl id="l_d">
  <dt><b>d</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='d' Line='d' -->
  <dd>The data point nearest the cursor and not previously deleted is marked with an
  X. It will not be used in further fits until it is undeleted.
  </dd>
  </dl>
  <dl id="l_f">
  <dt><b>f</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='f' Line='f' -->
  <dd>The function is fit to the data and the fit is graphed using the default
  plot type.
  </dd>
  </dl>
  <dl id="l_g">
  <dt><b>g</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='g' Line='g' -->
  <dd>Redefine the graph keys <span style="font-family: monospace;">"h-l"</span> from their defaults. A prompt is issued for the
  graph key to be redefined. Another prompt is issued for the data to be
  plotted at which point the user must enter the x and y axis data to plot,
  delimited by a comma. The data types are the following (they can be
  abbreviated to up to three characters).
  <div class="highlight-default-notranslate"><pre>
  function    Dependent variable or function
  fit         Fitted value
  residuals   Residuals (function - fit)
  ratio       Ratio (function / fit)
  nonlinear   Nonlinear component
  identifier  Independent variable named "identifier" (if defined)
  var n       Independent variable number "n"
  user n      User defined plot equation "n"  (if defined)
  </pre></div>
  The application program can define independent variable names and user plot 
  functions, aside from the standard options provided. If variable names are 
  supplied, the user can reference them by their names. Otherwise they can be 
  always referenced by <span style="font-family: monospace;">"var n"</span>, where <span style="font-family: monospace;">"n"</span> is the variable number (the user has 
  to know the variable order in this case). The <span style="font-family: monospace;">":variables"</span> command will
  list the currently defined variables by name and number.
  The application program may
  define any number of plot equations aside from the defaults provided. In this 
  case the user may reference them by <span style="font-family: monospace;">"user n"</span>, where <span style="font-family: monospace;">"n"</span> is the plot function 
  number (the user must know the equation order in this case). 
  </dd>
  </dl>
  <dl id="l_h">
  <dt><b>h, i, j, k, l</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='h' Line='h, i, j, k, l' -->
  <dd>By default each key produces a different graph. The graphs are described by
  the data which is graphed along each axis as defined above. The default graph
  keys,
  which may be redefined by the application program or interactively by using 
  the <span style="font-family: monospace;">'g'</span> key, are the following.
  <div class="highlight-default-notranslate"><pre>
  h       function, fit
  i       function, residuals
  j       function, ratio
  k       var 1, function
  l       user 1, user 2 (default)
  </pre></div>
  The initial graph key, if not redefined by the application program is <span style="font-family: monospace;">'h'</span>.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='o' Line='o' -->
  <dd>Overplot the next fit provided the graph format has not changed.
  </dd>
  </dl>
  <dl id="l_q">
  <dt><b>q</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='q' Line='q' -->
  <dd>Exit from the interactive curve fitting package.
  </dd>
  </dl>
  <dl id="l_r">
  <dt><b>r</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='r' Line='r' -->
  <dd>Redraw the current graph.
  </dd>
  </dl>
  <dl id="l_t">
  <dt><b>t</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='t' Line='t' -->
  <dd>Toggle fit overplotting on and off. If this option is on the data
  and fitted values are overplotted. Otherwise only data points are plotted.
  The fitted values are marked using boxes.
  </dd>
  </dl>
  <dl id="l_u">
  <dt><b>u</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='u' Line='u' -->
  <dd>Undelete the data point nearest the cursor which has been previously deleted.
  This option does not work over points marked as deleted by the application
  program before calling inlfit.
  </dd>
  </dl>
  <dl id="l_w">
  <dt><b>w [key]</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='w' Line='w [key]' -->
  <dd>Set the graph window or data range along each axis to be graphed.. This is a 
  <b>gtools</b> option which prints the prompt <span style="font-family: monospace;">"window:"</span>. The available cursor
  keystroke commands are printed with <span style="font-family: monospace;">'?'</span> and on-line help is available by
  typing <span style="font-family: monospace;">"help gtools"</span>.
  </dd>
  </dl>
  <dl id="l_I">
  <dt><b>I</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='I' Line='I' -->
  <dd>Interrupt the task immediately without saving the current fit.
  </dd>
  </dl>
  <p>
  Colon commands are used to show or set the values of parameters.
  The application program calling <b>inlfit</b> can add more commands.
  Parameter names can be abbreviated. The following commands are supported. 
  </p>
  <dl>
  <dt><b>:show [file]</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':show [file]' -->
  <dd>Show the current values of the fitting parameters high_reject, 
  low_reject, niterate, grow, tol, itmax. The default output device
  is the terminal (STDOUT) and the screen is cleared before the information
  is output. If a file is specified then the information is appended
  to the named file.
  </dd>
  </dl>
  <dl>
  <dt><b>:variables [file]</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':variables [file]' -->
  <dd>List the currently loaded variables. The number, id, minimum value and maximum
  value of each variable is printed. The default output device is the terminal
  (STDOUT) and the screen is cleared before the information is output.
  If a file is specified then the information is appended to the named file.
  </dd>
  </dl>
  <dl>
  <dt><b>:data [file]</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':data [file]' -->
  <dd>List the raw data. The value of each standard catalog and observations
  catalog variable  for each data point is printed. The default output device
  is the terminal (STDOUT) and the screen is cleared before the information
  is output.  If a file is specified then the information is appended to
  the named file.
  </dd>
  </dl>
  <dl>
  <dt><b>:errors [file]</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':errors [file]' -->
  <dd>Show the error analysis of the current fit.  The number of iterations,
  total number of points, the number of rejected and deleted points,
  the standard deviation, the reduced chi, average error (always = 1.0 if
  weight = 1.0,  otherwise = 1.0 / &lt;weight&gt;),
  average scatter (always = 0.0 if no weights scatter term is fit) 
  and the rms value are
  printed on the screen.
  The fitted parameters and their errors are also printed. The default output is 
  the terminal (STDOUT) and the screen is cleared before the information is 
  output. If a file is specified then the information is appended to
  the named file.
  </dd>
  </dl>
  <dl>
  <dt><b>:results [file]</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':results [file]' -->
  <dd>List the results of the current fit. The function value, the fitted value,
  the residual, and the weight are printed for each data point. The default
  output device is the terminal (STDOUT) and the screen is cleared before
  the information is output. If a file is specified then the information is
  appended to the named file.
  </dd>
  </dl>
  <dl>
  <dt><b>:vshow [file]</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':vshow [file]' -->
  <dd>A verbose version of <span style="font-family: monospace;">":show"</span> which is equivalent to a <span style="font-family: monospace;">":show"</span> plus a <span style="font-family: monospace;">":errors"</span>
  plus a <span style="font-family: monospace;">":results"</span>. The default output device is the terminal (STDOUT)
  and the screen is cleared before the information is output.
  If a file is specified then the information is appended to the named file.
  </dd>
  </dl>
  <dl>
  <dt><b>:page file</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':page file' -->
  <dd>Page through the named file.
  </dd>
  </dl>
  <dl>
  <dt><b>:tolerance [value]</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':tolerance [value]' -->
  <dd>Show or set the value of the fitting tolerance. Tolerance is the maximum
  fraction by which the reduced chi-squared can change from one iteration to the
  next for the fit to meet the convergence criteria.
  </dd>
  </dl>
  <dl>
  <dt><b>:maxiter [value]</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':maxiter [value]' -->
  <dd>Show or set the maximum number of fitting iterations.
  </dd>
  </dl>
  <dl>
  <dt><b>:nreject [value]</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':nreject [value]' -->
  <dd>Show or set the maximum number of rejection iterations. A value of zero
  means that automatic bad data rejection is turned off. 
  </dd>
  </dl>
  <dl>
  <dt><b>:low_reject [value], :high_reject [value]</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':low_reject [value], :high_reject [value]' -->
  <dd>Show or set the values of the bad data rejection limits.
  If both low_reject and high_reject are zero then automatic bad data
  rejection is turned off.
  If either of the high or low rejection limits are greater than zero,
  and nreject is greater than zero, the rms of the initial fit is computed.
  Points with residuals
  more than low_reject * rms below zero and high_reject * rms above zero
  are removed before the final fit. Rejected points are marked on the 
  graphs with diamonds. 
  </dd>
  </dl>
  <dl>
  <dt><b>:grow [value]</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':grow [value]' -->
  <dd>Show or set the value of the rejection growing radius. Any points
  within this distance of a rejected point are also rejected. 
  </dd>
  </dl>
  <dl>
  <dt><b>:fit [parameter] [value]</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':fit [parameter] [value]' -->
  <dd>Set the starting guess value for the named coefficient and allow the 
  parameter value to change (converge) during the fit.
  If the value is not specified inlfit will use the last starting guess.
  </dd>
  </dl>
  <dl>
  <dt><b>:const [parameter] [value]</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':const [parameter] [value]' -->
  <dd>Set the named parameter to be a constant with the specified value, i.e,
  its value won't change during the fit.
  If the value is not specified inlfit will use its last starting value.
  </dd>
  </dl>
  <dl>
  <dt><b>:/help</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':/help' -->
  <dd>Print help for the graph formatting options (the w key).
  </dd>
  </dl>
  <dl>
  <dt><b>:.help</b></dt>
  <!-- Sec='THE NON-LINEAR INTERACTIVE FITTING PACKAGE' Level=0 Label='' Line=':.help' -->
  <dd>Print help for the general IRAF graphics options.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Fit a set of UBV standard star data non-interactively using the automatic
  bad data rejection algorithm and the configuration file shown in example
  2 under the configuration file section.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; fitparams m92.obs m92.cat m92.config m92.fit nreject=10 inter-
  
      ... compute valued for the parameters in all the transformation
          equations
  
  ph&gt; page m92.fit
  
      ... check that the fitted parameter values are reasonable
  
  ph&gt; invertfit m92.obs m92.cat m92.config m92.fit m92.out
  
      ... evaluate the transformation equations for all the standard
          stars
  </pre></div>
  <p>
  2. Fit the same set of data interactively but deleting bad points by
  eye instead of using the automatic rejection algorithm.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; fitparams m92.obs m92.cat m92.config m92.fit
  
      ... a default plot of the UFIT equation comes up on the screen
          (the fit or right-hand side of the equation is plotted
          versus the function or left-hand side of the equation)
  
      ... type <span style="font-family: monospace;">'?'</span> to show the available commands
  
      ... type <span style="font-family: monospace;">'i'</span> to plot the residuals versus the function (LHS of
          the equation)
  
      ... delete bad points with the <span style="font-family: monospace;">'d'</span> key and refit using the <span style="font-family: monospace;">'f'</span>
          key
  
      ... check for any dependencies of the residuals on the color
          term by reprogramming the graph key <span style="font-family: monospace;">'l'</span> using the <span style="font-family: monospace;">'g'</span> key
          (type <span style="font-family: monospace;">'g'</span> to enter the reprogramming menu, <span style="font-family: monospace;">'l'</span> after the
          prompt to reprogram the <span style="font-family: monospace;">'l'</span> key, and "UB, residuals" in
          response to the question of which axes to plot
  
      ... list the plot windowing menu by typing <span style="font-family: monospace;">'w'</span> followed by <span style="font-family: monospace;">'?'</span>
          after the "window:" prompt
  
      ... type <span style="font-family: monospace;">'w'</span> followed by <span style="font-family: monospace;">'z'</span> after the ":window" prompt to zoom
          up on an interesting area in the plot, a <span style="font-family: monospace;">'w'</span> followed by <span style="font-family: monospace;">'a'</span>
          will return to normal scaling
  
      ... type <span style="font-family: monospace;">'q'</span> to quit the fit for this equation
  
      ... answer "yes" to the question about saving the fit
  
      ... proceed to the next fit by typing "next" in response to the
          prompt
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  chkconfig,mkconfig,gtools,inlfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'THE CONFIGURATION FILE' 'THE NON-LINEAR INTERACTIVE FITTING PACKAGE' 'EXAMPLES' 'SEE ALSO'  -->
  

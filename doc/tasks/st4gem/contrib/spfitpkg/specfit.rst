.. _specfit:

specfit: Fitting spectra with non-linear chi-square minimization
================================================================

**Package: spfitpkg**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  specfit spectra
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_spectra">
  <dt><b>spectra</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectra' Line='spectra' -->
  <dd>The input spectrum to be fit.  This input file must be either a 1D  or 2D
  IRAF image or an ASCII file formatted as described
  below.
  </dd>
  </dl>
  <dl id="l_debug">
  <dt><b>debug = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='debug' Line='debug = no' -->
  <dd>Debugging mode on or off.  (Totally useless for the typical user.)
  </dd>
  </dl>
  <dl id="l_interact">
  <dt><b>interact = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interact' Line='interact = yes' -->
  <dd>Selects interactive or non-interactive fitting modes.
  </dd>
  </dl>
  <dl id="l_gridfit">
  <dt><b>gridfit = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='gridfit' Line='gridfit = no' -->
  <dd>If you are in non-interactive mode and gridfit = yes it will use a grid type of
  fitting algorithm.  This algorithm will take one or two parameters.  Then it 
  will give these parameters a user specified lower limit value and then increase
  this value by a certain user specified step size until an upper limit is
  reached.  For each combination of values it reaches it will call one of the
  other fitting algorithms (see type_of_fit).  This algorithm will remember 
  the best combination of values and then output the entire grid to the log 
  files.  Note that this is a very slow algorithm.
  </dd>
  </dl>
  <dl id="l_errors_from_model">
  <dt><b>errors_from_model = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='errors_from_model' Line='errors_from_model = no' -->
  <dd>Compute expected variances from the Model?
  If so, the PROS approximation for low count rates is used,
  sigma=1.+sqrt(n+0.75).  The default, <span style="font-family: monospace;">"no"</span>, is to use the user-supplied
  errors in the data file.
  </dd>
  </dl>
  <dl id="l_plotdata">
  <dt><b>plotdata = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotdata' Line='plotdata = no' -->
  <dd>Determines whether an ASCII file suitable for plotting with MONGO is
  produced upon exit.  This file contains the wavelengths, the data, the errors,
  the model, and the values of the individual components of the model.
  </dd>
  </dl>
  <dl id="l_type_of_fit">
  <dt><b>type_of_fit = <span style="font-family: monospace;">"numrecipe"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='type_of_fit' Line='type_of_fit = "numrecipe"' -->
  <dd>In non-interactive mode, selects whether the Simplex, Marquardt, Numrecipe
  minimization algorithms are to be used.
  The Numrecipes algorithm is recommended.
  </dd>
  </dl>
  <dl id="l_logfiles">
  <dt><b>logfiles = STDOUT</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfiles' Line='logfiles = STDOUT' -->
  <dd>Specifies a list of file names for logging the results.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"sfdb"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "sfdb"' -->
  <dd>Relative pathname to the database directory.
  </dd>
  </dl>
  <dl id="l_initial_fit">
  <dt><b>initial_fit = <span style="font-family: monospace;">"initial"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='initial_fit' Line='initial_fit = "initial"' -->
  <dd>Specifies that the file <span style="font-family: monospace;">"sfdb/sfinitial"</span> is the database file containing the
  initial guesses for the parameters.
  </dd>
  </dl>
  <dl id="l_final_fit">
  <dt><b>final_fit = <span style="font-family: monospace;">"final"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='final_fit' Line='final_fit = "final"' -->
  <dd>Specifies that the file <span style="font-family: monospace;">"sfdb/sffinal"</span> is the database file containing the
  final best fit values.
  </dd>
  </dl>
  <dl id="l_plot_file">
  <dt><b>plot_file = <span style="font-family: monospace;">"specfit.plt"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plot_file' Line='plot_file = "specfit.plt"' -->
  <dd>File name for the plot file.  Not used unless plotdata=yes.
  </dd>
  </dl>
  <dl id="l_flux_intervals">
  <dt><b>flux_intervals = <span style="font-family: monospace;">"fluxes"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flux_intervals' Line='flux_intervals = "fluxes"' -->
  <dd>Specifies that the database file <span style="font-family: monospace;">"sfdb/sffluxes"</span> should be used to select
  spectral regions for integrating fluxes in lines and the continuum.
  If no integrations are desired, enter the null string.
  </dd>
  </dl>
  <dl id="l_Sample_ranges">
  <dt><b>Sample_ranges = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='Sample_ranges' Line='Sample_ranges = "*"' -->
  <dd>Wavelength intervals to be used in fitting the spectrum.  An asterisk <span style="font-family: monospace;">"*"</span> means
  use all the data.  A list such as <span style="font-family: monospace;">"3200.5-3290.1,3300-3400"</span> specifies separate
  regions.  This can be used to avoid noisy data or regions that are otherwise
  unsuitable for fitting.  Either real or integer values may be entered.
  </dd>
  </dl>
  <dl id="l_max_iterations">
  <dt><b>max_iterations = 100</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='max_iterations' Line='max_iterations = 100' -->
  <dd>Maximum number of iterations to be used by the minimizing routine.  This
  frequently constrains when a minimization process exits when one is starting
  a fit, so choose a low number initially to avoid seemingly endless waits.
  </dd>
  </dl>
  <dl id="l_fit_tolerance">
  <dt><b>fit_tolerance = 1.e-5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fit_tolerance' Line='fit_tolerance = 1.e-5' -->
  <dd>One of several tolerance parameters governing when a fit exits.  The fractional
  change in chi-square must be less than this value for a fit to exit on its own.
  </dd>
  </dl>
  <dl id="l_v0">
  <dt><b>v0 = 0., v1 = 1.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='v0' Line='v0 = 0., v1 = 1.0' -->
  <dd>Offset and slope used for calculating the variance if a 1D IRAF image is the
  input.  Errors in the flux will be calculated with the formula
  	Err = sqrt( v0 + v1 * Flux ).
  If you want uniform weighting, set v0 to an appropriate value (perhaps 10% of
  the mean flux) and v1 = 0.0.  For a spectrum containing raw counts following
  a Poisson error distribution, use v0 = 0.0 and v1 = 1.0.
  </dd>
  </dl>
  <dl id="l_low_mult">
  <dt><b>low_mult = .1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_mult' Line='low_mult = .1' -->
  <dd>This value is used when you are entering the information about a new component
  in interactive mode.  It multiplies this number and the new parameter value
  together to get the default lower bound to the newly entered parameter.
  </dd>
  </dl>
  <dl id="l_high_mult">
  <dt><b>high_mult = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='high_mult' Line='high_mult = 10' -->
  <dd>This variable is used much the same as the previous variable low_mult except 
  that it is used to determine the new upper bound on the parameter.
  </dd>
  </dl>
  <dl id="l_step_mult">
  <dt><b>step_mult = .01</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='step_mult' Line='step_mult = .01' -->
  <dd>Same as before this variable is used to determine the default step size
  when entering a new component.
  </dd>
  </dl>
  <dl id="l_key_file">
  <dt><b>key_file = /home/hut4/student/grimes/specfit/spec8/</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='key_file' Line='key_file = /home/hut4/student/grimes/specfit/spec8/' -->
  <dd>This important value specifies where the file named specfit.key can be found.  
  This file is used in the interactive mode to list what key strokes are 
  allowed.
  </dd>
  </dl>
  <p>
  The next group of parameters are all used by the gridfit algorithm only.
  </p>
  <dl id="l_grid_num">
  <dt><b>grid_num = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grid_num' Line='grid_num = 2' -->
  <dd>This parameter can only have two values, either 1 or 2.  It specifies 
  whether you'd like to use the grid fit algorithm on one or two parameters.
  </dd>
  </dl>
  <dl id="l_grid_comp1">
  <dt><b>grid_comp1 = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grid_comp1' Line='grid_comp1 = 5' -->
  <dd>This is the number of the component that the first parameter that you want
  to grid can be found in.
  </dd>
  </dl>
  <dl id="l_grid_par1">
  <dt><b>grid_par1 = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grid_par1' Line='grid_par1 = 2' -->
  <dd>This is the number of the first parameter that you want to grid.
  </dd>
  </dl>
  <dl id="l_grid_blim1">
  <dt><b>grid_blim1 = 1E-16</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grid_blim1' Line='grid_blim1 = 1E-16' -->
  <dd>This is the value that the first parameter will start incrementing from.
  </dd>
  </dl>
  <dl id="l_grid_tlim1">
  <dt><b>grid_tlim1 = 1E-15</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grid_tlim1' Line='grid_tlim1 = 1E-15' -->
  <dd>This is the value that the first parameter will stop incrementing at.
  </dd>
  </dl>
  <dl id="l_grid_step1">
  <dt><b>grid_step1 = 1E-16</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grid_step1' Line='grid_step1 = 1E-16' -->
  <dd>This is the value that the first parameter will be incremented by.
  </dd>
  </dl>
  <dl id="l_grid_comp2">
  <dt><b>grid_comp2, grid_par2, grid_blim2, grid_tlim2, grid_step2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grid_comp2' Line='grid_comp2, grid_par2, grid_blim2, grid_tlim2, grid_step2' -->
  <dd>These parameters are used exactly as above except that these are for the 
  second parameter if two is specified as the value of grid_num.
  </dd>
  </dl>
  <p>
  The following parameters are used in response to particular keystrokes in
  interactive cursor mode:
  </p>
  <dl id="l_plot_ranges">
  <dt><b>plot_ranges = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plot_ranges' Line='plot_ranges = "*"' -->
  <dd>In the interactive mode you can select which components you would like to see
  plotted.  Default is all (<span style="font-family: monospace;">"*"</span>).
  </dd>
  </dl>
  <dl id="l_new_sample">
  <dt><b>new_sample</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_sample' Line='new_sample' -->
  <dd>Specify new sample ranges for fitting the data.
  </dd>
  </dl>
  <dl id="l_comp_number">
  <dt><b>comp_number</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='comp_number' Line='comp_number' -->
  <dd>Component number to be changed.
  </dd>
  </dl>
  <dl id="l_param_number">
  <dt><b>param_number</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='param_number' Line='param_number' -->
  <dd>Parameter number of comp_number to be changed.
  </dd>
  </dl>
  <dl id="l_new_par_value">
  <dt><b>new_par_value</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_par_value' Line='new_par_value' -->
  <dd>New value for the parameter being changed.
  </dd>
  </dl>
  <dl id="l_lower_limit">
  <dt><b>lower_limit</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lower_limit' Line='lower_limit' -->
  <dd>New lower limit for a parameter.
  </dd>
  </dl>
  <dl id="l_upper_limit">
  <dt><b>upper_limit</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='upper_limit' Line='upper_limit' -->
  <dd>New upper limit for a parameter.
  </dd>
  </dl>
  <dl id="l_step_size">
  <dt><b>step_size</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='step_size' Line='step_size' -->
  <dd>New step size for a parameter.
  </dd>
  </dl>
  <dl id="l_param_tolerance">
  <dt><b>param_tolerance</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='param_tolerance' Line='param_tolerance' -->
  <dd>New tolerance for fitting a parameter.
  </dd>
  </dl>
  <dl id="l_fix_or_free">
  <dt><b>fix_or_free</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fix_or_free' Line='fix_or_free' -->
  <dd>New value for letting a variable vary freely (0), remain fixed at its current
  value (-1), or be linked (n) to the value of the corresponding parameter of
  parameter n.
  </dd>
  </dl>
  <dl id="l_change_iterations">
  <dt><b>change_iterations</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='change_iterations' Line='change_iterations' -->
  <dd>New number for max_iterations.
  </dd>
  </dl>
  <dl id="l_choice">
  <dt><b>choice</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='choice' Line='choice' -->
  <dd>Used to answer a YES or NO question.
  </dd>
  </dl>
  <dl id="l_comp_name">
  <dt><b>comp_name</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='comp_name' Line='comp_name' -->
  <dd>The name of the new component type to be entered.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  SPECFIT provides an interactive facility to fit wide varieties of emission line,
  absorption line, and continuum models to an input spectrum.
  A brief description is given by G. Kriss in the proceedings of the 3rd
  ADASS Conference (1994, PASP Conf. Series, Vol. 61, p. 437).
  The input spectrum
  can either be an IRAF image file or an ASCII file whose format is described
  below.  By selecting a combination of functional forms for various components,
  the user can fit complex spectra with multiple continuum components, blended
  emission lines and absorption lines, absorption edges, and extinction.
  All emission components are assumed to sum linearly.  For each absorption
  component the transmission function is calculated and applied to all PRECEDING
  components in the database file.  This allows the user to specify overlying,
  unabsorbed emission components (e.g., airglow lines) in the model.
  User-provided components supplied as ASCII tables of wavelength and value
  can also be used to model the continuum, emission line profiles, and
  absorption components.  Overall input to SPECFIT is controlled by the usual
  IRAF parameter file system.  However, the complex inputs necessary to specify a
  model are handled via ASCII database files described below.
  </p>
  <p>
  Fitting is done via Chi-square minimization using one of five different
  algorithms.  The iraf routine based on a marquardt type algorithm from
  numrecipes called Numrecipe seems to be usually the most effective and the
  fastest.  However in some cases the stability and procedures of the Simplex
  algorithm are superior.  The other three algorithms are Marquardt, Gridfit
  (see explanation above with the gridfit parameter), and Alternate
  (which alternates between calling Numrecipe and Simplex).
  The Marquardt algorithm does
  occasionally encounter floating point exceptions in complex non-linear 
  models.  Also, occasionally, both the marquardt and numrecipe algorithms can
  get lost when your initial fit is very far from the minimum.  This can
  be fixed by using the simplex algorithm.  Once the minimization has exited 
  either by meeting the tolerance requirements specified (rare) or by hitting the
  maximum number of iterations, errors for each freely varying parameter are 
  determined by evaluating the curvature matrix around the final value of
  Chi-square with a finite difference calculation.  The curvature matrix is
  inverted to obtain the error matrix.  The error matrix is re-scaled by the
  reduced Chi-square before evaluating the errors, which are one sigma for a
  single interesting parameter.  The user is warned that additional upward
  scalings may be necessary for multi-parameter fits where one is interested 
  in all parameters simultaneously.  (See Lampton, Margon, and Bowyer 1976, 
  Ap.J., 208, 177, and Avni 1976, Ap.J., 210, 642.  The paper by Avni discusses
  a more general case that makes the important distinction between <span style="font-family: monospace;">"interesting"</span>
  and <span style="font-family: monospace;">"uninteresting"</span> parameters.)  Best fit values and error bars are reported
  in a user-specified log file.
  </p>
  <p>
  N.B., errors are calculated under the assumption that the errors on the input
  spectrum follow a Gaussian distribution.  If your data do not satisfy this
  assumption, be wary of the error bars returned by SPECFIT.  Poisson-distributed
  data in the small-number limit are a typical example that causes problems.
  </p>
  <p>
  One may also request that the program perform integrations over various
  line or continuum portions of the fit.  This will give total fluxes with
  error bars for blended emission lines or portions of the continuum.
  The selected regions for integration are specified in an ASCII database file
  described below.
  </p>
  <p>
  If desired, an ASCII file suitable for plotting with MONGO or SMONGO is also
  produced.  This file has multiple columns in the following format:
  </p>
  <p>
  Wave Data Errors Model Comp1 Comp2 Comp3 . . . CompN
  </p>
  <p>
  Where the columns <span style="font-family: monospace;">"CompN"</span> are the values of the individual components and
  <span style="font-family: monospace;">"Model"</span> is the full model.
  </p>
  </section>
  <section id="s_interactive_mode">
  <h3>Interactive mode</h3>
  <p>
  the following keystrokes are active in addition to the normal IRAF
  cursor facilities (available with <span style="font-family: monospace;">":.help"</span>):
  </p>
  <dl>
  <dt><b></b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=0 Label='' Line=' ' -->
  <dd><dl>
  <dt><b>I</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='I' Line='I' -->
  <dd>Enter the interactive component addition facility.  This allows you to
  add a new component to the fit while running the program.  
  </dd>
  </dl>
  <dl>
  <dt><b>S</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='S' Line='S' -->
  <dd>Delete a component.  Given a component number it will delete the component
  from the fit.
  </dd>
  </dl>
  <dl>
  <dt><b>G</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='G' Line='G' -->
  <dd>List the types of components.
  </dd>
  </dl>
  <dl>
  <dt><b>a</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='a' Line='a' -->
  <dd>Change the fitting tolerance on a parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>c</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='c' Line='c' -->
  <dd>Change the value of a parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>e</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='e' Line='e' -->
  <dd>Evaluate the current fit and display the value of Chi-square.
  </dd>
  </dl>
  <dl>
  <dt><b>f</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='f' Line='f' -->
  <dd>Minimize Chi-square using the simplex method.
  </dd>
  </dl>
  <dl>
  <dt><b>m</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='m' Line='m' -->
  <dd>Minimize Chi-square using a Marquardt algorithm.
  </dd>
  </dl>
  <dl>
  <dt><b>n</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='n' Line='n' -->
  <dd>Minimize Chi-square using Numrecipe, an optimal Marquardt algorithm.
  </dd>
  </dl>
  <dl>
  <dt><b>i</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='i' Line='i' -->
  <dd>Inquire about the value of a parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>l</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='l' Line='l' -->
  <dd>Change the lower limit on a parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>p</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='p' Line='p' -->
  <dd>Overplot the fit on the data.  It is best to first use <span style="font-family: monospace;">"r"</span> to refresh the
  screen.
  </dd>
  </dl>
  <dl>
  <dt><b>o</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='o' Line='o' -->
  <dd>Specify which components to plot (p). 
  </dd>
  </dl>
  <dl>
  <dt><b>q</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='q' Line='q' -->
  <dd>Exit SPECFIT.  This may actually take a while if the model has many free
  parameters since the error matrix must be calculated to obtain the error bars.
  If you wish to exit quickly in such a case and re-run the fit in the background,
  simply type <span style="font-family: monospace;">"^C"</span> after you have typed <span style="font-family: monospace;">"q"</span>.  This will leave the database file
  for the final fit updated but the log files incomplete.
  Also during program execution typing ^C or killing the specfit process if it 
  running in the background will cause specfit to quit but will also save to the 
  final database file the current status of the fit.  This will not work for all
  forms of the kill function, however (i.e. <span style="font-family: monospace;">"kill -9 pid"</span>),
  so just using <span style="font-family: monospace;">"kill pid"</span> is recommended. 
  </dd>
  </dl>
  <dl>
  <dt><b>s</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='s' Line='s' -->
  <dd>Select new sample ranges for the fit.
  </dd>
  </dl>
  <dl>
  <dt><b>t</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='t' Line='t' -->
  <dd>Change the maximum number of iterations permitted in minimization.
  </dd>
  </dl>
  <dl>
  <dt><b>u</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='u' Line='u' -->
  <dd>Change the upper limit on a parameter.
  </dd>
  </dl>
  <dl>
  <dt><b>x</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='x' Line='x' -->
  <dd>Change the fix_or_free status of a parameter.  0 = free to vary; -1 = fixed at
  current value; n = link to the corresponding parameter of component n at a
  ratio given by the step size.
  </dd>
  </dl>
  <dl>
  <dt><b>z</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='z' Line='z' -->
  <dd>Change the step size for a parameter.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"space"</span></b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='' Line='"space"' -->
  <dd>Hitting the space bar (or any other unrecognized key) displays the current
  cursor position in user coordinates.
  </dd>
  </dl>
  <dl>
  <dt><b>d</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='d' Line='d' -->
  <dd>Plot the distribution of Chi-square with wavelength.
  Make sure the window is displayed full scale before issuing this command, or
  the plot will bomb.  Enter the window system with w, then give an <span style="font-family: monospace;">"a"</span> for all.
  You can re-window after the Chi-square plot appears.
  </dd>
  </dl>
  <dl>
  <dt><b>-</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='' Line='-' -->
  <dd>The minus key <span style="font-family: monospace;">"-"</span> will plot the residuals of the fit.
  </dd>
  </dl>
  <dl>
  <dt><b>+</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='' Line='+' -->
  <dd>The <span style="font-family: monospace;">"plus"</span> key will plot the model alone.
  </dd>
  </dl>
  <dl>
  <dt><b>w</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='w' Line='w' -->
  <dd>Enter the IRAF windowing function to adjust the region plotted.
  </dd>
  </dl>
  <dl>
  <dt><b>:</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='' Line=':' -->
  <dd>Issue an IRAF colon command, e.g. :.snap or :.gflush.
  </dd>
  </dl>
  <dl>
  <dt><b>?</b></dt>
  <!-- Sec='INTERACTIVE MODE' Level=1 Label='' Line='?' -->
  <dd>Print a help screen summarizing the functions of these cursor commands.
  </dd>
  </dl>
  </dd>
  </dl>
  </section>
  <section id="s_input_file_formats">
  <h3>Input file formats</h3>
  <p>
  SPECFIT will accept either an IRAF image file or an ASCII file for the
  input spectrum.  It ascertains the file type by looking for the <span style="font-family: monospace;">".**h"</span> extension
  of an IRAF image file.  If the <span style="font-family: monospace;">".**h"</span> is absent from the given filename, the
  file is assumed to be an ASCII input file as described below.  If the file is an
  IRAF image, the wavelength scale is set using CRVAL1, CDELT1 or W0, WPC.
  If these are missing, the default is to use pixel numbers for the x coordinate.
  For 1D images errors are calculated using the parameters v0 and v1 to
  calculate a scaled variance from the input fluxes.  2D images are assumed to be
  in the format produced by the HUT ballistic process -- fluxes in the first line
  of the image, and corresponding errors in the second line.
  </p>
  <p>
  The ASCII input file has two header lines followed by the data.  The data
  are in three columns giving wavelength, value, and error bar.  Be certain that
  error bars != 0.0, or you will get floating point errors.  The first line of the
  header is interpreted as purely informational, and is used only to label the
  plots.  The first field of the second line is critical -- it is an integer
  listing the number of points in the spectrum (the number of points is limited
  only by the available memory since data storage is dynamically allocated).
  The second field is optional, and it gives the integration time.
  A portion of a sample file is shown here:
  </p>
  <div class="highlight-default-notranslate"><pre>
  NGC4151 HUT 2188s
      440 2188.
   923.87    -0.1380    0.6260
   924.39     0.8460    0.3615
   924.90     0.3400    0.4426
   925.41    -0.5610    0.6260
   925.93     1.9960    0.2555
   926.44    -0.1080    0.6260
   926.95     1.4390    0.2799
   927.47     0.6400    0.3615
  </pre></div>
  </section>
  <section id="s_database_format_for_initial_parameter_values">
  <h3>Database format for initial parameter values</h3>
  <p>
  SPECFIT relies on the IRAF database format for inputting and maintaining the
  large number of parameters necessary to describe the model to be fit to the
  data.  Parameters are allowed to vary freely, be fixed at a value selected by
  the user, or to be linked to the value of the corresponding parameter in
  another component of the model.  For example, a model for deblending H alpha
  and the [N II] lines might have three components with the shorter wavelength
  [N II] has its flux, wavelength, and velocity width fixed relative to the
  corresponding parameters in the brighter, longer wavelength component.
  Note that the order of the components in this file is significant since
  absorption components apply only to components preceding them in the database
  file.
  </p>
  <p>
  Up to 100 components containing a total of 500 parameters are permitted.
  Twenty one different component types are recognized by SPECFIT, and each has
  a specific number of associated parameters:
  </p>
  <div class="highlight-default-notranslate"><pre>
  linear - a linear continuum, 2 parameters
          1 - flux at 1000 Angstroms
          2 - continuum slope (change in flux per Angstrom)
  
  powerlaw - a power law continuum (Flambda), 2 parameters
          1 - flux at 1000 Angstroms
          2 - power law index alpha for f = (x/1000)^(-alpha)
  
  bpl     - a broken power law continuum (Flambda), 4 parameters
          1 - flux at the break wavelength
          2 - the break wavelength (Angstroms)
          3 - power law index below the break
          4 - power law index above the break
  
  blackbody - blackbody continuum in Flambda, 2 parameters
          1 - Flux at 5500 Angstroms (Flambda)
          2 - temperature (Kelvin)
  
  gaussian - Gaussian line profile, 4 parameters
          1 - flux, or area under the Gaussian
          2 - centroid of the line
          3 - FWHM of the line in km/sec
          4 - Skew.  1 == symmetric
  
  logarith - Power-law line profile, 4 parameters
             F = I0 * ( x/centroid )**alpha,
                  I0 and alpha evaluated from flux and FWHM
          1 - flux, or area under the line
          2 - centroid of the line
          3 - FWHM of the line in km/sec
          4 - Skew.  1 == symmetric
  
  labsorp - absorption line described by a Gaussian
          1 - Equivalent width of the line
          2 - centroid
          3 - FWHM in km/sec
  
  tauabs  - absorption line described by a Gaussian in optical depth
          1 - Optical depth at line center
          2 - centroid
          3 - FWHM in km/sec
  
  eabsorp - absorption edge; optical depth ~ (lambda/lambda0)^3
          1 - optical depth at the edge
          2 - wavelength of the edge (lambda0 above)
  
  recomb - optically thin recombination continuum, 3 parameters
          1 - flux at the edge
          2 - wavelength of the edge
          3 - electron temperature (K)
          4 - FWHM in km/s
  
  extcor - Mean galactic extinction, Seaton law, 1 parameter
          1 - E(B-V)
  
  usercont - user-supplied continuum, 4 parameters
          1 - normalization (1 if model fluxes match data perfectly)
          2 - linear shift in wavelength
          3 - redshift
          4 - value of the "key" parameter (see below)
          (N.B. 2 and 3 should generally be mutually exclusive)
          Filenames plus "key" values must be in "continuum.ls".
  
  userline - user-supplied line profile, 4 parameters
          1 - normalization (1.0 gives input values from file)
          2 - linear shift in wavelength
          3 - redshift
          4 - value of the "key" parameter (see below)
          (N.B. 2 and 3 should generally be mutually exclusive)
          Filenames plus "key" values must be in "profile.ls".
  
  userabs - user-supplied absorption, 4 parameters
              User supplies tau vs. lambda.  Program computes
                  abs = exp( -norm * tau(lambda) )
          1 - normalization (1.0 gives input values from file)
          2 - linear shift in wavelength
          3 - redshift
          4 - value of the "key" parameter (see below)
          (N.B. 2 and 3 should generally be mutually exclusive)
          Filenames plus "key" values must be in "absorption.ls".
  
  lorentz - Modified Lorentzian line profile, 4 parameters
              F = flux * FWHM/2PI / ( (x-centroid)**alpha + FWHM**2/4)
          1 - flux, or area under the line (only for alpha = 2)
          2 - centroid of the line
          3 - FWHM of the line in km/sec (only for alpha = 2)
          4 - alpha -- exponent of (x - centroid) in denominator
  
  dampabs - Damped absorption line, 3 parameters
          1 - Column density times the oscillator strength
          2 - centroid of the line
          3 - Lifetime of the transition (Gamma, sec)
  
  logabs  - absorption line with tau~|lambda-lambda0|^alpha, 3 params
          1 - optical depth at line center
          2 - centroid of the line
          3 - FWHM of the line in km/sec
  
  ffree - F = Norm * ( 5500/x )**2 * exp(-1.43E8/x/temp), 2 params
          1 - Normalization in Flambda at 5500A
          2 - Temperature in Kelvin
  
  extdrude - Drude extinction curve, for UV spectra below 3200A.
                  See paper by Fitzpatrick and Massa ( ApJ, 1988,
                  vol. 328, p. 734 ) for more information, 7 params
          1 - E(B-V)
          2 - w0
          3 - Gamma
          4 - c1
          5 - c2
          6 - c3
          7 - c4
  
  disk - F = Norm * ( x**-Beta ) * exp ( -hc/(k * Temp * x ) )
          1 - Normalized Flux
          2 - Beta Value
          3 - Temperature in Kelvins
  
  ccmext - Extinction Curve using the Cardelli, Clayton, and Mathis
                  method.  (ApJ, 1989, vol 345, pp 245), 2 params
          1 - E(B-V)
          2 - RV
  
  
  </pre></div>
  </section>
  <section id="s_formats_for_user_supplied_models">
  <h3>Formats for user-supplied models</h3>
  <p>
  A list of filenames for the user-supplied models must be in the files
  <span style="font-family: monospace;">"continuum.ls"</span>, <span style="font-family: monospace;">"profile.ls"</span>, or <span style="font-family: monospace;">"absorption.ls"</span>, as appropriate,
  in the current directory.  On the same line with each file name there must be a
  <span style="font-family: monospace;">"key"</span> value which is the physical parameter that varies from file to file.
  The key values are assumed to be given in increasing order.
  SPECFIT calculates the model value by linear interpolation between the model
  files listed.  Key values below the smallest model key return the value in the
  first model file.  Key values greater than the largest model key return values
  from the last model file.  Values are not extrapolated.
  Single model files with a fixed key value are analogous to the previous
  method SPECFIT used for user-supplied models.
  Up to 20 files and associated key parameters may be given. 
  The model files may reside in any directory, but full path names must be
  specified.  Model files are free-format ASCII lists of wavelength and value.
  The wavelengths must increase monotonically at a fixed delta lambda.
  Model files may contain up to 10000 points.  Each model may contain a differing
  number of points.
  </p>
  <p>
  Note that the list of user-supplied models need not be physically related if
  the values of the key parameters are fixed to identically match a given file.
  This permits one to use several different user-supplied models simultaneously
  by making more than one <span style="font-family: monospace;">"usercont"</span> entry in the input database file, each with
  a different, fixed, value of its key parameter.  One then could, for example,
  fit an accretion disk model plus host galaxy starlight to the spectrum of a
  Seyfert galaxy as shown below for NGC 4151.
  </p>
  </section>
  <section id="s_sample_database_file">
  <h3>Sample database file</h3>
  <p>
  A sample database file is illustrated here, used for fitting a portion of the
  HUT NGC 4151 spectrum:
  </p>
  <div class="highlight-default-notranslate"><pre>
  begin   n4151
          task    specfit
  components      7
                  powerlaw
                  gaussian
                  labsorp
                  labsorp
                  userabs
                  usercont
                  usercont
                  powerlaw1       2 #Comments can be placed here
                          1.143721 0. 2. 0.1 0.001 0
                          1.328607 -5. 5. 0.04 0.001 0
                  gaussian2       4 #and here
                          3.666615 0. 10. 0.5 0.001 0
                          1040.954 1035. 1045. 1. 0.001 0
                          2.5466 2.5 15. 0.3 0.001 0
                          1. 0. 1. 0.1 0.001 -1
                  labsorp3        3 # and so on, ...
                          1.364428 0. 4. 0.2 0.001 0
                          1032.501 1032. 1042. 0.99647 0.001 4
                          1.3 1. 2.5 0.1 0.001 -1
                  labsorp4        3
                          1.364428 0. 4. 0.2 0.001 0
                          1039.069 1032. 1042. 0.5 0.001 0
                          1.3 1. 2.5 0.1 0.001 -1
                  userabs5        4       # Molecular hydrogen absorption
                          1.0   0. 1.1 0.02 0.001 0
                          0.0 -10.0 10.0 0.1 0.001 -1
                          3.300000E-4 0. 0.005 1.000000E-4 0.001 0
                          18.50  17.00  20.00  0.5  0.001  0
                  usercont6       4               # accretion disk spectrum
                          1.0   0. 1.1 0.02 0.001 0
                          0.0 -10.0 10.0 0.1 0.001 -1
                          3.300000E-4 0. 0.005 1.000000E-4 0.001 0
                          1.0  1.0  1.0  0.5  0.001  -1
                  usercont7       4               # host galaxy starlight
                          1.0   0. 1.1 0.02 0.001 0
                          0.0 -10.0 10.0 0.1 0.001 -1
                          3.300000E-4 0. 0.005 1.000000E-4 0.001 0
                          2.0  2.0  2.0  0.5  0.001  -1
  </pre></div>
  <p>
  This says to fit the spectrum with seven components: a powerlaw continuum,
  a Gaussian emission line, two absorption features, a user-specified
  absorption spectrum, and two user-supplied continuum spectra.
  Note some of the special features used here: the skew of the Gaussian is
  fixed at 1.0 (symmetric); the widths of the two absorption features (O VI) are
  initially fixed at the HUT resolution, 900 km/sec; the wavelength of the
  shorter wavelength absorption feature is fixed relative to component 4 in the
  ratio of the separation of the O VI doublet by specifying a link to
  component 4 in the last column of the wavelength entry for labsorp3.
  The file <span style="font-family: monospace;">"absorption.ls"</span> for this case looks like this:
  </p>
  <div class="highlight-default-notranslate"><pre>
  nh170b50.dat    17.0
  nh180b50.dat    18.0
  nh190b50.dat    19.0
  nh200b50.dat    20.0
  </pre></div>
  <p>
  The listed file names each contain two columns giving wavelength and optical
  depth for the value of log Nh given as the <span style="font-family: monospace;">"key"</span> parameter in <span style="font-family: monospace;">"absorption.ls"</span>.
  The user-supplied continuum models in <span style="font-family: monospace;">"continuum.ls"</span> are completed unrelated,
  and their <span style="font-family: monospace;">"key"</span> parameters have no physical meaning -- here they merely serve
  as an index for a model to choose.  Note that these key parameters are fixed
  (-1) in the input database file.  The file <span style="font-family: monospace;">"continuum.ls"</span> looks like this
  </p>
  <div class="highlight-default-notranslate"><pre>
  m70mdot02.dat   1.0
  b0star.dat      2.0
  </pre></div>
  <p>
  The parameter entries for a given component have these meanings:
  </p>
  <div class="highlight-default-notranslate"><pre>
  componentN      Npar
          value1 lowerlimit upperlimit stepsize tolerance fix/free
  </pre></div>
  <p>
  Lower and upper limits are treated as <span style="font-family: monospace;">"soft"</span> walls: a parameter may go
  outside these limits on a final iteration, but it is pulled back one step away
  from the limit at the start of the next iteration.
  </p>
  <p>
  The stepsize is the initial step size used by the minimization algorithms.
  This should generally be less than 10%-20% of the parameter value.
  The stepsize also serves the dual function of supplying the ratio factor
  when one parameter is linked to another as described below.
  </p>
  <p>
  The tolerance is used to evaluate when a fit is <span style="font-family: monospace;">"finished"</span>.  This is the
  absolute value of the maximum fractional error permitted before halting
  the minimization process.  ALL parameters plus Chi-square must be within
  their tolerance limits for a fit to exit, so it is usually best to specify
  a maximum number of iterations.
  </p>
  <p>
  The fix/free column says whether a parameter should vary freely (0), be fixed
  at the value given (-1), or be linked to another parameter (N, where 0 &lt; N &lt;
  Ncomponents).  If linked to another parameter, the step size is used to
  supply the ratio to be applied to the linked parameter to derive the value of
  this parameter.  For example, if I want to fix the wavelength, flux and width
  of [O III] 4959 relative to [O III] 5007, I link parameters 1, 2, and 3 of
  the 4959 component to the component number of 5007, specify a step size of
  0.33 for the flux ratio, a step size of 0.994 = 4959/5007 for the wavelength,
  and a step size of 1.0 for the width.
  </p>
  </section>
  <section id="s_database_format_for_flux_interval_computations">
  <h3>Database format for flux interval computations</h3>
  <p>
  The following example shows how to specify flux measurements for two
  different emission line intervals plus one continuum interval:
  </p>
  <div class="highlight-default-notranslate"><pre>
  begin   NeVflux
          task    specfit
  intervals       3
          3310.0  3390.0  1       4       NeV1
          2
          3
          4
          5
          3420.0  3510.0  1       4       NeV2
          6
          7
          8
          9
          3395.0  3415.0  1       0       F3400
  </pre></div>
  <p>
  This says to integrate the flux above the fitted continuum (component 1) over
  the specified wavelength intervals, and also to sum the flux in the 4
  separate components used to fit each of the NeV lines -- components 2, 3, 4, and
  5 for NeV1, and components 6, 7, 8, 9 for NeV2.  The continuum interval
  specified at the end has no emission line components (0 in the 4th column).
  </p>
  <p>
  If one does not wish any integrations performed, the database filename in the
  parameter file must be set to the null string <span style="font-family: monospace;">""</span>.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The Marquardt minimization algorithm occasionally produces floating point
  exception errors.  The best solution is to start again with fewer iterations,
  then switch to simplex minimization to get the solution past the region giving
  the Marquardt algorithm problems.  One could then switch back, if desired.
  </p>
  <p>
  The Numrecipes algorithm occasionally gets Matrix Inversion Errors or Singular
  Matrix errors.  Usually this is caused by some incorrectly entered data.
  Singular matrices are often traceable to free parameters that have no effect on
  the fit -- e.g., a Gaussian component whose flux is fixed at zero but whose
  wavelength and FWHM are permitted to vary freely.
  </p>
  <p>
  The ^C interrupts handler that is invoked when the user hits ^C instead of 
  exiting the program usually correctly saves the current status of the 
  database file to the output database.  However it occasionally does not
  output the corresponding message informing the user that it has done this.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'INTERACTIVE MODE' 'INPUT FILE FORMATS' 'DATABASE FORMAT FOR INITIAL PARAMETER VALUES' 'FORMATS FOR USER-SUPPLIED MODELS' 'SAMPLE DATABASE FILE' 'DATABASE FORMAT FOR FLUX INTERVAL COMPUTATIONS' 'BUGS'  -->
  

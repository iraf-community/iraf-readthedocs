.. _ntcontour:

ntcontour: Plot contours of N_e- or T_e-sensitive line ratios
=============================================================

**Package: nebular**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  ntcontour atom spectrum primary
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task computes and plots curves that show the range of electron 
  temperatures (T_e), electron densities (N_e), and/or intensity 
  ratios that are consistent with a specified diagnostic. A family of 
  secondary curves may optionally be plotted, where each curve may be 
  specified explicitly or as a set of successive, small differences 
  from the reference ratio, giving the appearance of contours. Though 
  for most ions there are default diagnostics for N_e and T_e, it is 
  possible to customize the diagnostic to the ratio of any of the 
  supported transitions. This task may be run interactively, so that 
  it is possible to investigate any number of diagnostics quickly.
  This task is particularly useful for determining the range of N_e 
  and T_e where a particular diagnostic is sensitive, for 
  investigating non-traditional diagnostics, and for estimating the 
  consequences of a given level of uncertainty in an observed line 
  ratio. The diagnostics are computed within the N-level atom 
  approximation. For more details about this approximation, type 
  <span style="font-family: monospace;">"help nlevel"</span>. 
  </p>
  <p>
  The user specifies the name and the spectrum number of the ion, and 
  an expression for the fixed value of interest (i.e., the N_e, T_e, 
  or the reddening-corrected diagnostic line ratio, as appropriate). 
  The output will be a plot with a curve of the specified type, with 
  the abscissa axis being either N_e or T_e, and the ordinate axis 
  being either T_e or the intensity ratio depending upon the setting 
  of the <span style="font-family: monospace;">"plot_type"</span> parameter. For plot_types of <span style="font-family: monospace;">"IN"</span> or <span style="font-family: monospace;">"IT"</span> the 
  intended type of diagnostic is apparent (density or temperature, 
  respectively) and the default ratio can be determined, but for 
  plot_type=TN it is possible that the selected ion could serve as 
  either a density or a temperature indicator. In this case the type 
  of diagnostic will be determined from the value of the <span style="font-family: monospace;">"diag_type"</span> 
  parameter. The default diagnostic line ratios for the various ions 
  can be viewed in the on-line help for <span style="font-family: monospace;">"nlevel"</span>. It is possible to 
  customize the line ratio using the <span style="font-family: monospace;">"transition"</span> parameter and an 
  expression for the ratio of interest. For details, see the 
  explanation for this parameter and the examples below. 
  </p>
  <p>
  Secondary curves may in addition be plotted, and are specified in 
  one of two ways. The most direct way is to provide a list of values 
  in the <span style="font-family: monospace;">"clist"</span> parameter which (like the <span style="font-family: monospace;">"primary"</span> value) specify 
  the fixed quantities for the curves. The user may alternatively 
  specify both a multiplicative increment (in dex, the decimal 
  exponent) to the primary (or reference) ratio, and the number of 
  desired contour pairs above/below the reference curve. In this case 
  the task will plot a pair of curves for each value/increment of the 
  diagnostic. The number of pairs plotted is set with the <span style="font-family: monospace;">"ncontours"</span> 
  task parameter. 
  </p>
  <p>
  A number of optional parameters specify the appearance of the 
  initial plot. A dotted curve denotes the reference value of 
  interest, and the solid curves denote secondary contours.  The user 
  may specify the color of each type of curve, provided the output 
  device supports color. Note that if the reference ratio falls out 
  of bounds (i.e., is unphysical), those points on the curve(s) will 
  not be plotted; if no points can be plotted on the reference curve, 
  the task will report an error. 
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  This task will by default run interactively, allowing the plot 
  axes, the appearance, and the selected ion to be changed with a set 
  of simple cursor and colon commands. 
  </p>
  <dl id="l_NTCONTOUR">
  <dt><b>NTCONTOUR CURSOR KEYS</b></dt>
  <!-- Sec='CURSOR COMMANDS' Level=0 Label='NTCONTOUR' Line='NTCONTOUR CURSOR KEYS' -->
  <dd><div class="highlight-default-notranslate"><pre>
  c    Report the world coordinates of the cursor
  q    Quit the task
  r    Redraw the graph
  I    Interrupt task immediately
  ?    Display this help document
  :    Enter command/value pairs
  </pre></div>
  </dd>
  </dl>
  <dl id="l_NTCONTOUR">
  <dt><b>NTCONTOUR COLON COMMANDS</b></dt>
  <!-- Sec='CURSOR COMMANDS' Level=0 Label='NTCONTOUR' Line='NTCONTOUR COLON COMMANDS' -->
  <dd>Each colon command takes one argument and may be abbreviated. 
  Multiple command/value pairs may be entered at a time. If no 
  argument is given then the current value is printed. String 
  values must be quoted if they contain spaces or special 
  characters.
  <div class="highlight-default-notranslate"><pre>
  :atom       [string]    Set the atom
  :clist      [string]    Set the list of secondary contours
  :diagtype   [string]    Set the diagnostic type (density|temperature)
  :dmin       [real]      Set the minimum density plot limit
  :dmax       [real]      Set the maximum density plot limit
  :dscale     [string]    Select log/linear plot scale for N_e
  :imin       [real]      Set the minimum intensity plot limit
  :imax       [real]      Set the maximum intensity plot limit
  :iscale     [string]    Select log/linear plot scale for intensity
  :interval   [real]      Set the interval (in dex) between contours
  :ion        [int]       Set the ion
  :ncontours  [int]       Set no. contours above/below primary curve
  :plottype   [string]    Set the type of plot: TN, IN, IT
  :primary    [string]    Set the expression for the primary contour
  :refcolor   [int]       Set color of the reference curve
  :resolution [int]       Set the curve resolution
  :title      [string]    Set the title ("default" selects default title)
  :tmin       [real]      Set the minimum temperature plot limit
  :tmax       [real]      Set the maximum temperature plot limit
  :tscale     [string]    Select log/linear plot scale for T_e
  :transition [string]    Set the transition for a custom diagnostic
  
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_atom">
  <dt><b>atom = <span style="font-family: monospace;">"oxygen"</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='atom' Line='atom = "oxygen" [string]' -->
  <dd>Name of ion, which is one of: carbon, nitrogen, oxygen, neon, 
  sodium, magnesium, aluminum, silicon, sulfur, chlorine, argon, 
  potassium, or calcium.
  </dd>
  </dl>
  <dl id="l_spectrum">
  <dt><b>spectrum = 2 [int]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectrum' Line='spectrum = 2 [int]' -->
  <dd>Spectrum number of the atom, e.g. <span style="font-family: monospace;">"3"</span> for [O III], <span style="font-family: monospace;">"2"</span> for [S II], 
  etc.  Must lie in the range 1 &lt;= spectrum &lt;= 8.  
  </dd>
  </dl>
  <dl id="l_primary">
  <dt><b>primary = <span style="font-family: monospace;">""</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='primary' Line='primary = "" [string]' -->
  <dd>Algebraic expression for the ratio of the diagnostic line flux. 
  The expression is evaluated with FORTRAN-like rules for 
  supported operators and the order of their evaluation.  
  </dd>
  </dl>
  <dl>
  <dt><b>(output = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(output = "") [string]' -->
  <dd>Name of an output table to contain the computed curves (NOT YET 
  IMPLEMENTED). 
  </dd>
  </dl>
  <dl id="l_plot_type">
  <dt><b>plot_type = <span style="font-family: monospace;">"TN"</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plot_type' Line='plot_type = "TN" [string]' -->
  <dd>Type of plot to generate: <span style="font-family: monospace;">"TN"</span> for T_e vs. N_e, <span style="font-family: monospace;">"IN"</span> for intensity 
  vs. N_e, <span style="font-family: monospace;">"IT"</span> for intensity vs. T_e.
  </dd>
  </dl>
  <dl>
  <dt><b>(diag_type = <span style="font-family: monospace;">"density"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(diag_type = "density") [string]' -->
  <dd>If plotting T_e vs. N_e, select the type of diagnostic (<span style="font-family: monospace;">"density"</span> 
  or <span style="font-family: monospace;">"temperature"</span>) corresponding to the transition. That is, if the 
  diagnostic is density-sensitive, solve for T_e, and vice versa.
  </dd>
  </dl>
  <dl>
  <dt><b>(transition = <span style="font-family: monospace;">"default"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(transition = "default") [string]' -->
  <dd>Expression for the transition, if not the <span style="font-family: monospace;">"default"</span>. Transitions
  are specified with the special function <span style="font-family: monospace;">"J"</span> (for the emissivity): 
  the arguments are the upper and lower levels of the transition. For 
  example, the traditional density diagnostic of [O II] is the ratio 
  of the intensities for the transition I(3-&gt;1) to that of 
  I(2-&gt;1)--i.e., I(3726)/I(3729). The corresponding expression for 
  would be <span style="font-family: monospace;">"J(3,1)/J(2,1)"</span>. The expression is evaluated with 
  FORTRAN-like expression rules.
  </dd>
  </dl>
  <dl>
  <dt><b>(clist = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(clist = "") [string]' -->
  <dd>List of diagnostic values for secondary curves. 
  </dd>
  </dl>
  <dl>
  <dt><b>(interval = 0.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(interval = 0.) [real]' -->
  <dd>If <span style="font-family: monospace;">"clist"</span> is blank and <span style="font-family: monospace;">"ncontours"</span> is non-zero, the secondary 
  contour intervals will be derived from this parameter, which 
  is a multiplicative deviation from the primary diagnostic 
  value, in dex. 
  </dd>
  </dl>
  <dl>
  <dt><b>(ncontours = 0) [int]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ncontours = 0) [int]' -->
  <dd>If <span style="font-family: monospace;">"clist"</span> is blank and <span style="font-family: monospace;">"interval"</span> is non-zero, this parameter 
  specifies the number of contour pairs to plot on the high/low sides 
  of the reference curve.  
  </dd>
  </dl>
  <dl>
  <dt><b>(min_dens = 10.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(min_dens = 10.) [real]' -->
  <dd>Minimum density for initial plot, in units of 1/cm^3; must lie in 
  the range 1 to 1.e+7, and must be less than <span style="font-family: monospace;">"max_dens"</span>.  
  </dd>
  </dl>
  <dl>
  <dt><b>(max_dens = 1.e+8) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(max_dens = 1.e+8) [real]' -->
  <dd>Maximum density for initial plot, in units of 1/cm^3; must lie in 
  the range 10 to 1.e+8, and must exceed <span style="font-family: monospace;">"min_dens"</span>.  
  </dd>
  </dl>
  <dl>
  <dt><b>(log_ne = yes) [boolean] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(log_ne = yes) [boolean] ' -->
  <dd>Plot the electron density with a log scale? 
  </dd>
  </dl>
  <dl>
  <dt><b>(min_temp = 2000.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(min_temp = 2000.) [real]' -->
  <dd>Minimum temperature for initial plot, in units of Kelvins; must 
  lie in the range 500 to 50,000 K, and must be less than <span style="font-family: monospace;">"max_temp"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>(max_temp = 3.0e+4) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(max_temp = 3.0e+4) [real]' -->
  <dd>Maximum temperature for initial plot, in units of Kelvins; must 
  lie in the range 1,000 to 100,000 K, and must exceed <span style="font-family: monospace;">"min_temp"</span>.  
  </dd>
  </dl>
  <dl>
  <dt><b>(log_te = no) [boolean] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(log_te = no) [boolean] ' -->
  <dd>Plot the electron temperature with a log scale? 
  </dd>
  </dl>
  <dl>
  <dt><b>(min_intens = 1.e-2) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(min_intens = 1.e-2) [real]' -->
  <dd>Minimum intensity for initial plot, in arbitrary units; must 
  exceed 1.e-7 and must be less than <span style="font-family: monospace;">"max_intens"</span>.  
  </dd>
  </dl>
  <dl>
  <dt><b>(max_intens = 10.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(max_intens = 10.) [real]' -->
  <dd>Maximum intensity for initial plot, in arbitrary units; must 
  exceed 1.e-7 and <span style="font-family: monospace;">"min_intens"</span>. 
  </dd>
  </dl>
  <dl>
  <dt><b>(log_intens = no) [boolean] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(log_intens = no) [boolean] ' -->
  <dd>Plot the line intensity ratio with a log scale? 
  </dd>
  </dl>
  <dl>
  <dt><b>(resolution = 51) [int]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(resolution = 51) [int]' -->
  <dd>Max number of data points to plot for the range of abscissae.  
  Increasing this number improves the fidelity of the curve, at 
  the expense of execution time.  
  </dd>
  </dl>
  <dl>
  <dt><b>(ref_color = 3) [int]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ref_color = 3) [int]' -->
  <dd>Color for the curve corresponding to the primary, or reference 
  value of the diagnostic ratio.  Even if the output device supports 
  color, the rendered color may vary with different output hardware.
  </dd>
  </dl>
  <dl>
  <dt><b>(delta_color = 1) [int]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(delta_color = 1) [int]' -->
  <dd>Color for the secondary, or <span style="font-family: monospace;">"delta"</span> curves; the default value is 
  the <span style="font-family: monospace;">"foreground"</span> color, which is often rendered as either black or 
  white.  Even if the output device supports color, the rendered 
  color may vary with different output hardware.
  </dd>
  </dl>
  <dl>
  <dt><b>(title = <span style="font-family: monospace;">"default"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(title = "default") [string]' -->
  <dd>Optional plot title. 
  </dd>
  </dl>
  <dl>
  <dt><b>(interactive = yes) [boolean] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(interactive = yes) [boolean] ' -->
  <dd>Run this task interactively? 
  </dd>
  </dl>
  <dl>
  <dt><b>(device = stdgraph) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(device = stdgraph) [string]' -->
  <dd>Output device for the plot. 
  </dd>
  </dl>
  <dl>
  <dt><b>(cursor = <span style="font-family: monospace;">""</span>) [*gcur]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(cursor = "") [*gcur]' -->
  <dd>Input for list-directed cursor commands. 
  </dd>
  </dl>
  <dl>
  <dt><b>(append = no) [boolean] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(append = no) [boolean] ' -->
  <dd>Append next plot to previous? 
  </dd>
  </dl>
  <dl>
  <dt><b>(at_data = <span style="font-family: monospace;">"at_data"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(at_data = "at_data") [string]' -->
  <dd>Pathname for atomic data reference tables. 
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Plot 5 curves in the N_e, T_e plane that are consistent with the 
  [S II] density diagnostic ratio centered at ~0.7, in increments of 
  dex(0.05), and adjust the default plot limits such that N_e &lt; 
  1.e+6/cm^3 and T_e &lt; 50,000 K. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ntcontour sulfur 2 3.2/4.51 diag_type=density delta=0.05 \
  &gt;&gt;&gt; ncont=2 max_dens=1.E6 max_temp=5.e+4 interact-
  </pre></div>
  <p>
  2. Plot curves in the N_e, intensity plane that are consistent 
  with the [O II] density diagnostic ratio for T_e=10000. K, with 
  secondary curves corresponding to T_e=5000 and T_e=15000. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ntcontour oxygen 2 1.e4 plot_type=IN clist="5000. 1.5e4"
  </pre></div>
  <p>
  Once in interactive mode, change the plot limits to intensity &lt; 4,
  1.e2 &lt; N_e &lt; 1.e6, then replot:
  </p>
  <div class="highlight-default-notranslate"><pre>
  :imax 4 dmin 1.e2 dmax 1.e6
  r
  </pre></div>
  <p>
  Now change the plot to T_e vs. N_e; set the diagnostic ratio to 
  2.0 and the secondary curves to 1.0 and 3.0, then replot:
  </p>
  <div class="highlight-default-notranslate"><pre>
  :plottype TN primary 2. clist "1. 3."
  r
  </pre></div>
  <p>
  3. Investigate the utility of a custom temperature diagnostic for   
  O III. Plot curves in the N_e, T_e plane that are consistent with 
  the ratio I(1661+1666)/I(4363) for values of 1.0 (primary), 0.5 and
  1.5 (secondary). (Note that the transitions corresponding to these 
  wavelengths can be found by running the <span style="font-family: monospace;">"ionic"</span> task first.) 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ntcont oxygen 3 1. diag_type=temperature clist="0.5 1.5" \
  &gt;&gt;&gt; transition="(j(6,3)+j(6,2))/j(5,4)" interact-
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  The 5-level atom program, upon which this package is based, was 
  originally written by M.M. DeRobertis, R. Dufour, and R. Hunt.  
  This package was written by R.A. Shaw (STScI).  A description was 
  published by R.A. Shaw &amp; R.J. Dufour (1994).  Type <span style="font-family: monospace;">"help nlevel"</span> 
  for additional information about the N-level atom approximation, 
  and for references to the atomic parameters and the other 
  literature references.  Support for this software development was 
  provided by the Astrophysics Data Program through NASA grant 
  NAG5-1432, and through STScI internal research funds.  
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  nlevel, temden, ntplot 
  </p>
  <p>
  For general information about this package, type <span style="font-family: monospace;">"help nebular 
  opt=sysdoc"</span>.  
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'DESCRIPTION' 'CURSOR COMMANDS' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

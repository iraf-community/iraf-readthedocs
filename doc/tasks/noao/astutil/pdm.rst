.. _pdm:

pdm: Find periods in light curves by Phase Dispersion Minimization
==================================================================

**Package: astutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pdm infile
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_infiles">
  <dt><b>infiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='infiles' Line='infiles' -->
  <dd>Input file template.  If more than one file matches the template, data
  from all the files will be concatenated to produce the working data set.
  </dd>
  </dl>
  <dl id="l_metafile">
  <dt><b>metafile = <span style="font-family: monospace;">"pdmmeta"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='metafile' Line='metafile = "pdmmeta"' -->
  <dd>File in which to store metacode when running in batch mode.  All of the
  plots saved will be put here with formfeeds between them.
  </dd>
  </dl>
  <dl id="l_batchfile">
  <dt><b>batchfile = <span style="font-family: monospace;">"pdmbatch"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='batchfile' Line='batchfile = "pdmbatch"' -->
  <dd>File in which to store information about the period, amplitude, epoch
  and fit function when running in batch mode.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "stdgraph"' -->
  <dd>The output device for interactive graphics.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Interactive flag.  If set to no, the analysis is done in batch mode with output
  to a file and no interactive graphics.  Metacode will be saved for the data
  plot, the theta plot, and the phase plot.  If set to yes, various types of
  plots can be made on the user's terminal and cursor commands are available.
  </dd>
  </dl>
  <dl id="l_flip">
  <dt><b>flip = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flip' Line='flip = no' -->
  <dd>Flag to tell the program to flip the y-axis.  This is useful when the y-scale
  is in magnitudes (decreasing numbers mean increasing brightness).
  </dd>
  </dl>
  <dl id="l_minp">
  <dt><b>minp = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minp' Line='minp = 0' -->
  <dd>Minimum period to be searched.  This parameter, if set, tells the program
  the bottom end of the period window to be searched.   If not set, the
  program uses as a value the smallest chronological distance between
  any two adjacent data points.  When the program is run, it writes a value
  into this parameter as stored in the uparm directory.  This means the
  next time the program is run, the default minp will be the value assigned
  or calculated the last time the program was run by this user.  We say the
  program 'remembers' the last value used.
  </dd>
  </dl>
  <dl id="l_maxp">
  <dt><b>maxp = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxp' Line='maxp = 0' -->
  <dd>Maximum period to be searched.  This parameter, if set, tells the program
  the top end of the period window to be searched.  If not set, the program
  uses as a value 4 times the distance between the first and last data
  point.  This parameter is remembered as minp is.
  </dd>
  </dl>
  <dl id="l_ntheta">
  <dt><b>ntheta = 200</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ntheta' Line='ntheta = 200' -->
  <dd>Resolution of the theta plot.  This parameter tells how many points in
  the period window should have their theta statistic calculated.  The points
  are spaced equidistant from one another in frequency space.
  </dd>
  </dl>
  <dl id="l_pluspoint">
  <dt><b>pluspoint = 50</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pluspoint' Line='pluspoint = 50' -->
  <dd>Maximum number of data points for which to use plus symbols.  If there
  are more data points then points are plotted.
  </dd>
  </dl>
  <dl id="l_autoranges">
  <dt><b>autoranges = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='autoranges' Line='autoranges = no' -->
  <dd>This flag, when set, instructs the program to look for gaps in
  the data and, if large gaps are found, divide the data up into ranges
  discarding the gaps and doing the analysis only on the ranges.  This
  helps remove side lobes from the spectra.
  </dd>
  </dl>
  <dl id="l_nsigma">
  <dt><b>nsigma = 3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsigma' Line='nsigma = 3' -->
  <dd>Number of standard deviations for autorange break.  If ranges are to 
  be automatically calculated, this parameter tells how large a gap in
  the data should constitute a division between ranges.  The mean
  and standard deviation of the distribution of chronological spacing
  of input points are calculated.  Then the points are scanned in
  increasing order and if an inter-data gap bigger than nsigma
  standard deviations is found, a new range is started.
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
  Pdm applies a phase dispersion minimization algorithm (R. F. Stellingwerf,
  <span style="font-family: monospace;">"Period Determination by Phase Dispersion Minimization"</span>, ApJ 224, 1978,
  953) to lightcurve data to determine periodicities in the data.  It also
  calculates amplitude and epoch information.
  </p>
  <p>
  Pdm can be used in batch or interactive mode.  In batch
  mode the
  output is period, amplitude, and epoch for the minimum found within
  the period window.  Metacode will be produced for the data plot,
  the theta statistic plot, and the phasecurve plot.
  The metacode will be saved in the metafile.  In interactive mode the user
  can plot the data at different stages in the analysis, fit and remove
  curves from the data, reject points, set data ranges, plot and fit
  phasecurves, etc.
  </p>
  <p>
  Pdm guesses at the period/frequency window to be searched unless
  the minimum
  and maximum period for the window are specified using minp and maxp.  The
  minimum period is taken as twice the chronological distance between the closest
  two points in the data.  The maximum period is taken as 4 times the distance
  between the first and last data points.
  </p>
  <p>
  Pdm will work on one object at a time and the input data may
  be contained in multiple input files if desired.  The program will
  concatenate data in all the files which match the input template.
  The input files are text files containing one (x,y) pair per line or
  just a (y) value per line.  If only one value per line is found the
  program will number x sequentially (1,2,3,4,...).  If a third value
  is included on each line it will be read as the error in that
  measurement.   (The <span style="font-family: monospace;">'e'</span> key is used to toggle error bars on the phase
  plot.)
  </p>
  <p>
  At startup, if the interactive flag is set, the user will be presented
  with a plot of the data and the cursor will be turned on.
  </p>
  <p>
  When the user plots a phasecurve, points that are deleted or undeleted from
  the phasecurve plot will be deleted or undeleted from the working data set.
  </p>
  <p>
  The ICFIT keystrokes are described elsewhere. (see help for icfit)
  </p>
  <p>
  Phase Dispersion Minimization User Interface (keystrokes)
  </p>
  <p>
  When the program starts up it reads the data file(s) and displays
  the data on the screen as a standard mark plot.  The user is
  then placed in a graphics cursor loop with the following options
  available in addition to the standard graphics commands:
  </p>
  <p>
  Note:
  The remembered period is for the last minimum found.  This
  minimum calculation is done whenever a new theta plot is graphed
  and whenever the <span style="font-family: monospace;">"m"</span> key is used.
  </p>
  <dl>
  <dt><b>? -- list options</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='? -- list options' -->
  <dd>Print out the menu.
  </dd>
  </dl>
  <dl id="l_h">
  <dt><b>h -- graph data</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='h' Line='h -- graph data' -->
  <dd>Make a plot on the screen, using marks, of observation time vs observed
  value. If there are more than 50 points, use dots, else use pluses.  If
  points have been deleted, draw an x through them on the plot.  If ranges
  are in effect, draw range bars along the abscissa of the plot marking
  the ranges.
  </dd>
  </dl>
  <dl id="l_e">
  <dt><b>e -- toggle error bars on or off</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='e' Line='e -- toggle error bars on or off' -->
  <dd>When the phase plot is on the screen and error data has been supplied,
  this key will toggle the drawing of error bars on the phase plot so that
  the user can determine how well the period found works with the data
  including this error information.
  </dd>
  </dl>
  <dl id="l_i">
  <dt><b>i,k -- graph frequency or period respectively versus theta</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='i' Line='i,k -- graph frequency or period respectively versus theta' -->
  <dd>Calculate the theta statistic in the period/frequency range specified
  previously.  If no period/frequency range has been specified,
  pdm guesses one.  The minimum period is taken as twice the chronological
  distance between the closest two points in the data.  The maximum
  period is taken as 4 times the distance between the first and last
  data points.  The number of theta points in this range is also a
  parameter which can be specified.
  Next, plot theta on the screen using line drawing mode.  Plot
  either period vs theta or frequency vs theta.  Calculate the minimum
  value of theta displayed, turn the cursor back on (clgcur) and put
  the cursor x position at that minimum.
  </dd>
  </dl>
  <dl id="l_p">
  <dt><b>p -- graph phase curve for period/frequency at cursor position</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='p' Line='p -- graph phase curve for period/frequency at cursor position' -->
  <dd>Calculate the phase curve for the period/frequency under the
  cursor.  This assumes the user has a theta plot on the screen and
  an error message will be given otherwise.
  The phase curve will be plotted in mark mode with two copies displayed
  and placed end to end to clarify the plot by providing continuity at
  all phases.  The amplitude and epoch values for this period are calculated
  and the phases are plotted relative to this epoch.
  </dd>
  </dl>
  <dl id="l_d">
  <dt><b>d,u -- delete/undelete respectively point nearest the cursor</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='d' Line='d,u -- delete/undelete respectively point nearest the cursor' -->
  <dd>Points deleted will have an x drawn through them.  The x will be
  erased when the point is undeleted.
  </dd>
  </dl>
  <dl id="l_f">
  <dt><b>f -- call ICFIT on displayed data</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='f' Line='f -- call ICFIT on displayed data' -->
  <dd>ICFIT is used for interactive curve fitting.
  It is called with either the data values or the phase values,
  depending on which type of plot is on the screen at the time.
  Any point deleted in ICFIT will be removed from consideration in
  all subsequent calculations until restored.
  The fit curve is retained by PDM after the return from ICFIT and
  may be subsequently subtracted from the data using the j command.
  Note: The user must exit ICFIT using the q key before he is placed
  back into PDM.
  </dd>
  </dl>
  <dl id="l_j">
  <dt><b>j -- subtract fit from data, use residuals</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='j' Line='j -- subtract fit from data, use residuals' -->
  <dd>Just as it says. The original data is retained and can be reinstated
  with the :origdata command.  This command only applies to the data.
  The user cannot subtract a fit from the phase plot.
  </dd>
  </dl>
  <dl id="l_s">
  <dt><b>s -- set sample range for calculations</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='s' Line='s -- set sample range for calculations' -->
  <dd>This command is used to set ranges of data to be used.  The cursor is
  first positioned to the beginning of the range of interest, an s is
  struck, the program prints the prompt again:, the cursor is
  repositioned to the end of the range and a second s is struck
  completing the command.  Multiple ranges may be set and all the data
  inside the union of the ranges will be used.  Data points outside the
  ranges will be ignored until the data is reset with an :alldata
  or an :origdata command.
  This also forces the boolean flag segments to be set true.
  </dd>
  </dl>
  <dl>
  <dt><b>,, -- Set minp or minf to cursor x position</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=',, -- Set minp or minf to cursor x position' -->
  <dd>When the theta plot is on the screen, this keystroke can be used
  to set the minimum period (frequency) to the current cursor position.
  </dd>
  </dl>
  <dl>
  <dt><b>. -- Set maxp or maxf to cursor x position</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='. -- Set maxp or maxf to cursor x position' -->
  <dd>When the theta plot is on the screen, this keystroke can be used
  to set the maximum period (frequency) to the current cursor position.
  </dd>
  </dl>
  <dl id="l_g">
  <dt><b>g -- significance of theta at cursor x position</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='g' Line='g -- significance of theta at cursor x position' -->
  <dd>The statistical significance of the period/frequency under the
  cursor is calculated by Fisher's method of randomization.
  This value is printed at the bottom of the screen.
  This assumes that a theta plot is on the screen.
  </dd>
  </dl>
  <dl id="l_a">
  <dt><b>a -- amplitude and epoch at cursor x position</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='a' Line='a -- amplitude and epoch at cursor x position' -->
  <dd>For the period/frequency under the cursor or of the plot, the amplitude
  and epoch are calculated and returned to the user.
  This assumes that a theta plot is on the screen.
  </dd>
  </dl>
  <dl id="l_m">
  <dt><b>m -- mark range and find minimum in this range</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='m' Line='m -- mark range and find minimum in this range' -->
  <dd>This command is used exactly like the s command but has a different
  effect.  After the user has positioned the cursor and struck the m
  key twice, defining the range, the minimum value of theta is found
  in this range and its associated period/frequency is returned.
  </dd>
  </dl>
  <dl id="l_r">
  <dt><b>r -- replot</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='r' Line='r -- replot' -->
  <dd>Redraw the plot on the screen.
  </dd>
  </dl>
  <dl id="l_x">
  <dt><b>x -- remove a trend from the data by removing a bestfit line</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='x' Line='x -- remove a trend from the data by removing a bestfit line' -->
  <dd>This command calls the curfit package to fit a straight line to the
  data and then subtracts it point by point from the data.
  </dd>
  </dl>
  <dl id="l_z">
  <dt><b>z -- flip the y-axis scale</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='z' Line='z -- flip the y-axis scale' -->
  <dd>This command toggles a y-axis flip for the plots.  This is useful when
  the user is plotting magnitudes where the smaller the ordinate value the
  larger the intensity.
  </dd>
  </dl>
  <dl id="l_q">
  <dt><b>q -- quit</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='q' Line='q -- quit' -->
  <dd>Exit PDM.
  </dd>
  </dl>
  <p>
  The following commands may be abbreviated.  If entered without an
  argument; :minp, :maxp, :minf, :maxf, and :ntheta will display the named
  parameter; :show, :vshow will print to STDOUT; :signif, :ampep, and :phase,
  will do the calculation at the remembered period.
  </p>
  <dl>
  <dt><b>:show [file]		show parameter settings</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':show [file]		show parameter settings' -->
  <dd>Print on the screen the min/max period, the remembered minimum,
  the range if it is in effect, the start and end of the ranges
  if they are defined, the mean and variance of the data in each
  range. If file is specified, the output will go there.
  </dd>
  </dl>
  <dl>
  <dt><b>:vshow [file]		show verbose information</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':vshow [file]		show verbose information' -->
  <dd>This command will display all the information displayed by the :show
  command plus curfit information if the any curves have been fit.  Also,
  the residual data will be shown if residuals have been calculated. If
  file is specified, the output will go there.
  </dd>
  </dl>
  <div class="highlight-default-notranslate"><pre>
  :minp :maxp [period]            set min/max search period
  :minf :maxf [frequency]         set min/max search frequency
  </pre></div>
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=' ' -->
  <dd>These commands are self explanatory.  Whichever value is set,
  period or frequency, the corresponding frequency or period is
  automatically calculated and remembered.
  </dd>
  </dl>
  <dl>
  <dt><b>:ntheta [num]		set number of points for theta</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':ntheta [num]		set number of points for theta' -->
  <dd>Set the number of equally spaced points in the period window for
  which theta should be calculated.  This is really a setting of
  the resolution of the theta plot and defaults to 200 since
  the calculation time for 200 points is only a few seconds.  Very
  large numbers entered here will cause the program to warn the user
  that the theta calculation may take some time.
  </dd>
  </dl>
  <dl>
  <dt><b>:sample [value]		set/show the sample ranges</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':sample [value]		set/show the sample ranges' -->
  <dd>The start and end values for the ranges will be printed on the screen.
  If value is present, it has the form begin:end where begin
  and end are real numbers specifying a new range.
  </dd>
  </dl>
  <dl>
  <dt><b>:signif [period]		find theta significance</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':signif [period]		find theta significance' -->
  <dd>Same as the g key.  The colon command allows the user to 
  set the period exactly, instead of using the cursor.  If no period
  is entered, the calculation will be done using the remembered period.
  </dd>
  </dl>
  <dl>
  <dt><b>:ampep [period]		amplitude and epoch</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':ampep [period]		amplitude and epoch' -->
  <dd>Same as the e key.  Without an argument, use remembered minima.
  </dd>
  </dl>
  <dl>
  <dt><b>:phase [period]		graph phase curve</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':phase [period]		graph phase curve' -->
  <dd>Same as the h key.  Without an argument, use remembered minima.
  </dd>
  </dl>
  <dl>
  <dt><b>:unreject			unreject all points</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':unreject			unreject all points' -->
  <dd>This tells the program to use all of the data points. If a fit
  has been subtracted from a subset of the data points then this command
  causes the original data set to be restored since, otherwise, we would
  restore a mixture of data and residuals.
  </dd>
  </dl>
  <dl>
  <dt><b>:alldata			reset range to entire dataset</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':alldata			reset range to entire dataset' -->
  <dd>The effect of this command is to turn off the range settings.  All
  of the data will be used if the ranges settings are off.  Rejected
  points remain rejected though.  Again, if these data are residuals,
  the original data are restored.
  </dd>
  </dl>
  <dl>
  <dt><b>:origdata			reset data to original dataset</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':origdata			reset data to original dataset' -->
  <dd>Copy the original data vector into the working data vector.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To find the main period in the data contained in the file 'vstar645',
  whose period is within the bounds (200., 800.) interactively
  the command might be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; pdm vstar645 minp=200. maxp=800.
  </pre></div>
  <p>
  2. To do the same thing in batch mode, allowing the program to guess the 
  period window, with no lightcurve analysis, and saving the metacode
  in vstar645.m, the command might be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; pdm vstar645 inter=no meta="vstar645.m"
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Pdm has some problems with data sets containing a small number (&lt;20)
  points.  Generally, it will do fairly well but the theta curve may look
  strange.
  </p>
  <p>
  The amplitude and epoch calculation might be improved by fitting a parabola
  to the phase curve near the minimum and near the maximum and using points
  on these parabolas for the min and max points instead of actual data points.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  icfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

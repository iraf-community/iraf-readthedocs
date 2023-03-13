.. _splot:

splot: Preliminary spectral plot/analysis
=========================================

**Package: irs**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  splot images [line [band]]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images (spectra) to plot.  If the image is 2D or 3D the line
  and band parameters are used.  Successive images are plotted
  following each <span style="font-family: monospace;">'q'</span> cursor command.  One may use an image section
  to select a desired column, line, or band but the full image will
  be in memory and any updates to the spectrum will be part of the
  full image.
  </dd>
  </dl>
  <dl id="l_line">
  <dt><b>line, band</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='line' Line='line, band' -->
  <dd>The image line/aperture and band to plot in two or three dimensional
  images.  For multiaperture spectra the aperture specified by the line
  parameter is first sought and if not found the specified image line is
  selected.  For other two dimensional images, such as long slit spectra, the
  line parameter specifies a line or column.  Note that if
  the line and band parameters are specified on the command line it will not
  be possible to change them interactively.
  </dd>
  </dl>
  <dl id="l_units">
  <dt><b>units = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='units' Line='units = ""' -->
  <dd>Dispersion coordinate units for the plot.  If the spectra have known units,
  currently this is generally Angstroms, the units may be converted
  to other units for plotting as specified by this task parameter.
  If this parameter is the null string and the world coordinate system
  attribute <span style="font-family: monospace;">"units_display"</span> is defined then that will
  be used.  If both this task parameters and <span style="font-family: monospace;">"units_display"</span> are not
  given then the spectrum dispersion units will be used.
  The units
  may also be changed interactively.  See the units section of the
  <b>package</b> help for a further description and available units.
  </dd>
  </dl>
  <dl id="l_options">
  <dt><b>options = <span style="font-family: monospace;">"auto"</span> [auto,zero,xydraw,histogram,nosysid,wcreset,flip,overplot]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='options' Line='options = "auto" [auto,zero,xydraw,histogram,nosysid,wcreset,flip,overplot]' -->
  <dd>A list of zero or more, possibly abbreviated, options.  The options can
  also be toggled with colon commands.  The currently defined options are
  <span style="font-family: monospace;">"auto"</span>, <span style="font-family: monospace;">"zero"</span>, <span style="font-family: monospace;">"xydraw"</span>, <span style="font-family: monospace;">"histogram"</span>, <span style="font-family: monospace;">"nosysid"</span>, <span style="font-family: monospace;">"wreset"</span>, <span style="font-family: monospace;">"flip"</span>, and
  <span style="font-family: monospace;">"overplot"</span>.  Option <span style="font-family: monospace;">"auto"</span> automatically replots the graph whenever changes
  are made.  Otherwise the graph is replotted with keystrokes <span style="font-family: monospace;">'c'</span> or <span style="font-family: monospace;">'r'</span>.
  Option <span style="font-family: monospace;">"zero"</span> makes the initial minimum y of the graphs occur at zero.
  Otherwise the limits are set automatically from the range of the data or
  the <i>ymin</i> parameter.  Option <span style="font-family: monospace;">"xydraw"</span> changes the <span style="font-family: monospace;">'x'</span> draw key to use
  both x and y cursor values for drawing rather than the nearest pixel value
  for the y value.  Option <span style="font-family: monospace;">"histogram"</span> plots the spectra in a histogram style
  rather than connecting the pixel centers.  Option <span style="font-family: monospace;">"nosysid"</span> excludes the
  system banner from the graph title.  Option <span style="font-family: monospace;">"wreset"</span> resets the graph
  limits to those specified by the <i>xmin, xmax, ymin, ymax</i> parameters
  whenever a new spectrum is plotted.  The <span style="font-family: monospace;">"flip"</span> option selects that
  initially the spectra be plotted with decreasing wavelengths.  The options
  may be queried and changed interactively.  The <span style="font-family: monospace;">"overplot"</span> options overplots
  all graphs and a screen erase only occurs with the redraw key.
  </dd>
  </dl>
  <dl id="l_xmin">
  <dt><b>xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmin' Line='xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF' -->
  <dd>The default limits for the initial graph.  If INDEF then the limit is
  determined from the range of the data (autoscaling).  These values can
  be changed interactively with <span style="font-family: monospace;">'w'</span> window key options or the cursor commands
  <span style="font-family: monospace;">":/xwindow"</span> and <span style="font-family: monospace;">":/ywindow"</span> (see <b>gtools</b>).
  </dd>
  </dl>
  <dl id="l_save_file">
  <dt><b>save_file = <span style="font-family: monospace;">"splot.log"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='save_file' Line='save_file = "splot.log"' -->
  <dd>The file to contain any results generated by the equivalent width or
  deblending functions.  Results are added to this file until the file is
  deleted.  If the filename is null (<span style="font-family: monospace;">""</span>), then no results are saved.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Output graphics device: one of <span style="font-family: monospace;">"stdgraph"</span>, <span style="font-family: monospace;">"stdplot"</span>, <span style="font-family: monospace;">"stdvdm"</span>, or device
  name.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input.  When null the standard cursor is used otherwise
  the specified file is used.
  </dd>
  </dl>
  <p>
  The following parameters are used for error estimates in the <span style="font-family: monospace;">'d'</span>,
  <span style="font-family: monospace;">'k'</span>, and <span style="font-family: monospace;">'e'</span> key measurements.  See the ERROR ESTIMATES section for a
  discussion of the error estimates.
  </p>
  <dl id="l_nerrsample">
  <dt><b>nerrsample = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nerrsample' Line='nerrsample = 0' -->
  <dd>Number of samples for the error computation.  A value less than 10 turns
  off the error computation.  A value of ~10 does a rough error analysis, a
  value of ~50 does a reasonable error analysis, and a value &gt;100 does a
  detailed error analysis.  The larger this value the longer the analysis
  takes.
  </dd>
  </dl>
  <dl id="l_sigma0">
  <dt><b>sigma0 = INDEF, invgain = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma0' Line='sigma0 = INDEF, invgain = INDEF' -->
  <dd>The pixel sigmas are modeled by the formula:
  <div class="highlight-default-notranslate"><pre>
  sigma**2 = sigma0**2 + invgain * I
  </pre></div>
  where I is the pixel value and <span style="font-family: monospace;">"**2"</span> means the square of the quantity.  If
  either parameter is specified as INDEF or with a value less than zero then
  no sigma estimates are made and so no error estimates for the measured
  parameters are made.
  </dd>
  </dl>
  <p>
  The following parameters are for the interactive curve fitting function
  entered with the <span style="font-family: monospace;">'t'</span> key.  This function is usually used for continuum
  fitting.  The values of these parameters are updated during the fitting.
  See <b>icfit</b> for additional details on interactive curve fitting.
  </p>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"spline3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "spline3"' -->
  <dd>Function to be fit to the spectra.  The functions are
  <span style="font-family: monospace;">"legendre"</span> (legendre polynomial), <span style="font-family: monospace;">"chebyshev"</span> (chebyshev polynomial),
  <span style="font-family: monospace;">"spline1"</span> (linear spline), and <span style="font-family: monospace;">"spline3"</span> (cubic spline).  The functions
  may be abbreviated.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 1' -->
  <dd>The order of the polynomials or the number of spline pieces.
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 2., high_reject = 4.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_reject' Line='low_reject = 2., high_reject = 4.' -->
  <dd>Rejection limits below and above the fit in units of the residual sigma.
  Unequal limits are used to reject spectral lines on one side of the continuum
  during continuum fitting.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 10' -->
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
  <dl id="l_markrej">
  <dt><b>markrej = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='markrej' Line='markrej = yes' -->
  <dd>Mark rejected points?  If there are many rejected points it might be
  desired to not mark rejected points.
  </dd>
  </dl>
  <p>
  The following parameters are used to overplot standard star fluxes with
  the <span style="font-family: monospace;">'y'</span> key.  See <b>standard</b> for more information about these parameters.
  </p>
  <dl id="l_star_name">
  <dt><b>star_name</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='star_name' Line='star_name' -->
  <dd>Query parameter for the standard star fluxes to be overplotted.
  Unrecognized names or a <span style="font-family: monospace;">"?"</span> will print a list of the available stars
  in the specified calibration directory.
  </dd>
  </dl>
  <dl id="l_mag">
  <dt><b>mag</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mag' Line='mag' -->
  <dd>The magnitude of the observed star in the band given by the
  <i>magband</i> parameter.  If the magnitude is not in the same band as
  the blackbody calibration file then the magnitude may be converted to
  the calibration band provided the <span style="font-family: monospace;">"params.dat"</span> file containing relative
  magnitudes between the two bands is in the calibration directory
  </dd>
  </dl>
  <dl id="l_magband">
  <dt><b>magband</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='magband' Line='magband' -->
  <dd>The standard band name for the input magnitude.  This should generally
  be the same band as the blackbody calibration file.  If it is
  not the magnitude will be converted to the calibration band.
  </dd>
  </dl>
  <dl id="l_teff">
  <dt><b>teff</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='teff' Line='teff' -->
  <dd>The effective temperature (deg K) or the spectral type of the star being
  calibrated.  If a spectral type is specified a <span style="font-family: monospace;">"params.dat"</span> file must exist
  in the calibration directory.  The spectral types are specified in the same
  form as in the <span style="font-family: monospace;">"params.dat"</span> file.  For the standard blackbody calibration
  directory the spectral types are specified as A0I, A0III, or A0V, where A
  can be any letter OBAFGKM, the single digit subclass is between 0 and 9,
  and the luminousity class is one of I, III, or V.  If no luminousity class
  is given it defaults to dwarf.
  </dd>
  </dl>
  <dl id="l_caldir">
  <dt><b>caldir = <span style="font-family: monospace;">")_.caldir"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='caldir' Line='caldir = ")_.caldir"' -->
  <dd>The standard star calibration directory.  The default value redirects the
  value to the parameter of the same name in the package parameters.
  </dd>
  </dl>
  <dl id="l_fnuzero">
  <dt><b>fnuzero = 3.68e-20</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fnuzero' Line='fnuzero = 3.68e-20' -->
  <dd>The absolute flux per unit frequency at a magnitude of zero used to
  to convert the calibration magnitudes to absolute flux.
  </dd>
  </dl>
  <p>
  The following parameters are used for queries in response to particular
  keystrokes.
  </p>
  <dl id="l_next_image">
  <dt><b>next_image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='next_image' Line='next_image' -->
  <dd>In response to <span style="font-family: monospace;">'g'</span> (get next image) this parameter specifies the image.
  </dd>
  </dl>
  <dl id="l_new_image">
  <dt><b>new_image</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_image' Line='new_image' -->
  <dd>In response to <span style="font-family: monospace;">'i'</span> (write current spectrum) this parameter specifies the
  name of a new image to create or existing image to overwrite.
  </dd>
  </dl>
  <dl id="l_overwrite">
  <dt><b>overwrite = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='overwrite' Line='overwrite = no' -->
  <dd>Overwrite an existing output image?  If set to yes it is possible to write
  back into the input spectrum or to some other existing image.  Otherwise
  the user is queried again for a new image name.
  </dd>
  </dl>
  <dl id="l_spec2">
  <dt><b>spec2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spec2' Line='spec2' -->
  <dd>When adding, subtracting, multiplying, or dividing by a second spectrum
  (<span style="font-family: monospace;">'+'</span>, <span style="font-family: monospace;">'-'</span>, <span style="font-family: monospace;">'*'</span>, <span style="font-family: monospace;">'/'</span> keys in the <span style="font-family: monospace;">'f'</span> mode) this parameter is used to get
  the name of the second spectrum.
  </dd>
  </dl>
  <dl id="l_constant">
  <dt><b>constant</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='constant' Line='constant' -->
  <dd>When adding or multiplying by a constant (<span style="font-family: monospace;">'p'</span> or <span style="font-family: monospace;">'m'</span> keys in the <span style="font-family: monospace;">'f'</span> mode)
  the parameter is used to get the constant.
  </dd>
  </dl>
  <dl id="l_wavelength">
  <dt><b>wavelength</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wavelength' Line='wavelength' -->
  <dd>This parameter is used to get a dispersion coordinate value during deblending or
  when changing the dispersion coordinates with <span style="font-family: monospace;">'u'</span>.
  </dd>
  </dl>
  <dl id="l_linelist">
  <dt><b>linelist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linelist' Line='linelist' -->
  <dd>During deblending this parameter is used to get a list of line positions,
  peak values, profile types, and widths.
  </dd>
  </dl>
  <dl id="l_wstart">
  <dt><b>wstart, wend, dw</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wstart' Line='wstart, wend, dw' -->
  <dd>In response to <span style="font-family: monospace;">'p'</span> (convert to a linear wavelength scale) these parameters
  specify the starting wavelength, ending wavelength, and wavelength per pixel.
  </dd>
  </dl>
  <dl id="l_boxsize">
  <dt><b>boxsize</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='boxsize' Line='boxsize' -->
  <dd>In response to <span style="font-family: monospace;">'s'</span> (smooth) this parameter specifies the box size in pixels
  to be used for the boxcar smooth.  The value must be odd.  If an even
  value is specified the next larger odd value is actually used.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Splot</b> provides an interactive facility to display and analyze
  spectra.  See also <b>bplot</b> for a version of this task useful for making
  many plots noninteractively.  Each spectrum in the image list is displayed
  successively.  To quit the current image and go on to the next the <span style="font-family: monospace;">'q'</span>
  cursor command is used.  If an image is two-dimensional, such as with
  multiple aperture or long slit spectra, the aperture or image column/line
  to be displayed is needed.  If the image is three-dimensional, such as with
  the extra information produced by <b>apextract</b>, the band is needed.
  These parameters are queried unless specified on the command line.  If
  given on the command line it will not be possible to change them
  interactively.
  </p>
  <p>
  The plots are made on the specfied graphics device which is usually to
  the graphics terminal.  The initial plot limits are set with the parameters
  <i>xmin, xmax, ymin</i>, and <i>ymax</i>.  If a limit is INDEF then that limit
  is determined from the range of the data.  The <span style="font-family: monospace;">"zero"</span> option may also
  be set in the <i>options</i> parameter to set the lower intensity limit
  to zero.  Other options that may be set to control the initial plot
  are to exclude the system identification banner, and to select a
  histogram line type instead of connecting the pixel centers.
  The dispersion units used in the plot are set by the <i>units</i>
  parameter.  This allows converting to units other than those in which the
  dispersion coordinates are defined in the spectra.
  </p>
  <p>
  The <i>option</i> parameter, mentioned in the previous paragraph, is a
  a list of zero or more options.  As previously noted, some of the options
  control the initial appearance of the plots.  The <span style="font-family: monospace;">"auto"</span> option determines
  how frequently plots are redrawn.  For slow terminals or via modems one
  might wish to minimize the redrawing.  The default, however, is to redraw
  when changes are made.  The <span style="font-family: monospace;">"xydraw"</span> parameter is specific to the <span style="font-family: monospace;">'x'</span>
  key.
  </p>
  <p>
  After the initial graph is made an interactive cursor loop is entered.
  The <i>cursor</i> parameter may be reset to read from a file but generally
  the graphics device cursor is read.  The cursor loop takes single
  keystroke commands and typed in commands begun with a colon, called
  colon commands.  These commands are described below and a summary of
  the commands may be produced interactively with the <span style="font-family: monospace;">'?'</span> key or
  a scrolling help on the status line with the <span style="font-family: monospace;">'/'</span> key.
  </p>
  <p>
  Modifications to the spectra being analyzed may be saved using the <span style="font-family: monospace;">'i'</span> key
  in a new, the current, or other existing spectra.  A new image is created
  as a new copy of the current spectrum and so if the current spectrum is
  part of a multiple spectrum image (including a long slit spectrum) the
  other spectra are copied.  If other spectra in the same image are then
  modified and saved use the overwrite option to replace then in the new
  output image.  If the output spectrum already exists then the
  <i>overwrite</i> flag must be set to allow modifying the data.  This
  includes the case when the output spectrum is the same as the input
  spectrum.  The only odd case here is when the input spectrum is one
  dimensional and the output spectrum is two dimensional.  In this case the
  user is queried for the line to be written.
  </p>
  <p>
  The other form of output, apart from that produced on the terminal, are
  measurements of equivalent widths, and other analysis functions.  This
  information will be recorded in the <i>save_file</i> if specified.
  </p>
  <p>
  The following keystrokes are active in addition to the normal IRAF
  cursor facilities (available with <span style="font-family: monospace;">":.help"</span>):
  </p>
  <dl>
  <dt><b>?</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='?' -->
  <dd>Page help information.
  </dd>
  </dl>
  <dl>
  <dt><b>/</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='/' -->
  <dd>Cycle through short status line help.
  </dd>
  </dl>
  <dl>
  <dt><b>&lt;space&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='&lt;space&gt;' -->
  <dd>The space bar prints the cursor position and value of the nearest
  pixel.
  </dd>
  </dl>
  <dl id="l_a">
  <dt><b>a</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='a' Line='a' -->
  <dd>Expand and autoscale to the data range between two cursor positions.
  See also <span style="font-family: monospace;">'w'</span>, and <span style="font-family: monospace;">'z'</span>.  Selecting no range, that is the two
  cursor positions the same, produces an autoscale of the whole spectrum.
  </dd>
  </dl>
  <dl id="l_b">
  <dt><b>b</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='b' Line='b' -->
  <dd>Set the plot base level to zero rather than autoscaling.
  </dd>
  </dl>
  <dl id="l_c">
  <dt><b>c</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='c' Line='c' -->
  <dd>Clear all windowing and redraw the full current spectrum.  This redraws the
  spectrum and cancels any effects of the <span style="font-family: monospace;">'a'</span>, <span style="font-family: monospace;">'z'</span>, and <span style="font-family: monospace;">'w'</span> keys.  The <span style="font-family: monospace;">'r'</span>
  key is used to redraw the spectrum with the current windowing.
  </dd>
  </dl>
  <dl id="l_d">
  <dt><b>d</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='d' Line='d' -->
  <dd>Mark two continuum points and fit (deblend) multiple line profiles.
  The center, continuum at the center, core intensity, integrated flux,
  equivalent width, FWHMs for each profile are printed and saved
  in the log file.  See <span style="font-family: monospace;">'k'</span> for fitting a single profile and
  <span style="font-family: monospace;">'-'</span> to subtract the fitted profiles.
  </dd>
  </dl>
  <dl id="l_e">
  <dt><b>e</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='e' Line='e' -->
  <dd>Measure equivalent width by marking two continuum points around the line
  to be measured.  The linear continuum is subtracted and the flux is
  determined by simply summing the pixels with partial pixels at the ends.
  Returned values are the line center, continuum at the region center,
  flux above or below the continuum, and the equivalent width.
  </dd>
  </dl>
  <dl id="l_f">
  <dt><b>f</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='f' Line='f' -->
  <dd>Enter arithmetic function mode. This mode allows arithmetic functions to be
  applied to the spectrum. The pixel values are modified according to the
  function request and may be saved as a new spectrum with the <span style="font-family: monospace;">'i'</span>
  command.  Operations with a second spectrum are done in wavelength
  space and the second spectrum is automatically resampled if necessary.
  If one spectrum is longer than the other, only the smaller number of
  pixels are affected.  To exit this mode type <span style="font-family: monospace;">'q'</span>.
  The following keystrokes are available in the function mode.  Binary
  operations with a constant or a second spectrum produce a query for the
  constant value or spectrum name.
  <dl>
  <dt><b>a</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='a' Line='a' -->
  <dd>Absolute value
  </dd>
  </dl>
  <dl>
  <dt><b>d</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='d' Line='d' -->
  <dd>Power of base 10 (inverse log base 10)
  </dd>
  </dl>
  <dl>
  <dt><b>e</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='e' Line='e' -->
  <dd>Power of base e (inverse log base e)
  </dd>
  </dl>
  <dl>
  <dt><b>i</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='i' Line='i' -->
  <dd>Inverse/reciprocal (values equal to zero are set to 0.0 in the inverse)
  </dd>
  </dl>
  <dl>
  <dt><b>l</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='l' Line='l' -->
  <dd>Log base 10 (values less than or equal to 0.0 are set to -0.5)
  </dd>
  </dl>
  <dl>
  <dt><b>m</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='m' Line='m' -->
  <dd>Multiply by a constant (constant is queried)
  </dd>
  </dl>
  <dl>
  <dt><b>n</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='n' Line='n' -->
  <dd>Log base e (values less than or equal to 0.0 are set to -0.5)
  </dd>
  </dl>
  <dl>
  <dt><b>p</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='p' Line='p' -->
  <dd>Add by a constant (constant is queried)
  </dd>
  </dl>
  <dl>
  <dt><b>q</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='q' Line='q' -->
  <dd>Quit Function mode
  </dd>
  </dl>
  <dl>
  <dt><b>s</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='s' Line='s' -->
  <dd>Square root (values less than 0.0 are set to 0.0)
  </dd>
  </dl>
  <dl>
  <dt><b>+</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='+' -->
  <dd>Add another spectrum
  </dd>
  </dl>
  <dl>
  <dt><b>-</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='-' -->
  <dd>Subtract another spectrum
  </dd>
  </dl>
  <dl>
  <dt><b>*</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='*' -->
  <dd>Multiply by another spectrum
  </dd>
  </dl>
  <dl>
  <dt><b>/</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='/' -->
  <dd>Divide by another spectrum
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_g">
  <dt><b>g</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='g' Line='g' -->
  <dd>Get another spectrum. The current spectrum is replaced by the new spectrum.
  The aperture/line and band are queried is necessary.
  </dd>
  </dl>
  <dl id="l_h">
  <dt><b>h</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='h' Line='h' -->
  <dd>Measure equivalent widths assuming a gaussian profile with the width
  measured at a specified point.  Note that this is not a gaussian fit (see
  <span style="font-family: monospace;">'k'</span> to fit a gaussian)!  The gaussian profile determined here may be
  subtracted with the <span style="font-family: monospace;">'-'</span> key.  A second cursor key is requested with one of
  the following values:
  <dl>
  <dt><b>a</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='a' Line='a' -->
  <dd>Mark the continuum level at the line center and use the LEFT half width
  at the half flux point.
  </dd>
  </dl>
  <dl>
  <dt><b>b</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='b' Line='b' -->
  <dd>Mark the continuum level at the line center and use the RIGHT half width
  at the half flux point.
  </dd>
  </dl>
  <dl>
  <dt><b>c</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='c' Line='c' -->
  <dd>Mark the continuum level at the line center and use the FULL width
  at the half flux point.
  </dd>
  </dl>
  <dl>
  <dt><b>l</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='l' Line='l' -->
  <dd>Mark a flux level at the line center relative to a normalized continuum
  and use the LEFT width at that flux point.
  </dd>
  </dl>
  <dl>
  <dt><b>r</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='r' Line='r' -->
  <dd>Mark a flux level at the line center relative to a normalized continuum
  and use the RIGHT width at that flux point.
  </dd>
  </dl>
  <dl>
  <dt><b>k</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='k' Line='k' -->
  <dd>Mark a flux level at the line center relative to a normalized continuum
  and use the FULL width at that flux point.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_i">
  <dt><b>i</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='i' Line='i' -->
  <dd>Write the current spectrum out to a new or existing image.  The image
  name is queried and overwriting must be confirmed.
  </dd>
  </dl>
  <dl id="l_j">
  <dt><b>j</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='j' Line='j' -->
  <dd>Set the value of the nearest pixel to the x cursor to the y cursor position.
  </dd>
  </dl>
  <dl id="l_k">
  <dt><b>k + (g, l or v)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='k' Line='k + (g, l or v)' -->
  <dd>Mark two continuum points and fit a single line profile.  The second key
  selects the type of profile: g for gaussian, l for lorentzian, and v for
  voigt.  Any other second key defaults to gaussian.  The center, continuum
  at the center, core intensity, integrated flux, equivalent width, and FWHMs
  are printed and saved in the log file.  See <span style="font-family: monospace;">'d'</span> for fitting multiple
  profiles and <span style="font-family: monospace;">'-'</span> to subtract the fit.
  </dd>
  </dl>
  <dl id="l_l">
  <dt><b>l</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='l' Line='l' -->
  <dd>Convert to flux per unit wavelength (f-lambda). The spectrum is assumed
  to be flux calibrated in flux per unit frequency (f-nu).  See also <span style="font-family: monospace;">'n'</span>.
  </dd>
  </dl>
  <dl id="l_m">
  <dt><b>m</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='m' Line='m' -->
  <dd>Compute the mean, RMS, and signal-to-noise over a region marked with two
  x cursor positions.
  </dd>
  </dl>
  <dl id="l_n">
  <dt><b>n</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='n' Line='n' -->
  <dd>Convert to flux per unit frequency (f-nu). The spectrum is assumed
  to be flux calibrated in flux per unit wavelength (f-lambda).  See also <span style="font-family: monospace;">'l'</span>.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='o' Line='o' -->
  <dd>Set overplot flag.  The next plot will overplot the current plot.
  Normally this key is immediately followed by one of <span style="font-family: monospace;">'g'</span>, <span style="font-family: monospace;">'#'</span>, <span style="font-family: monospace;">'%'</span>, <span style="font-family: monospace;">'('</span>, or <span style="font-family: monospace;">')'</span>.
  The <span style="font-family: monospace;">":overplot"</span> colon command and overplot parameter option may be
  used to set overplotting to be permanently on.
  </dd>
  </dl>
  <dl id="l_p">
  <dt><b>p</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='p' Line='p' -->
  <dd>Define a linear wavelength scale.  The user is queried for a starting
  wavelength and an ending wavelength.  If either (though not both)
  are specified as INDEF a dispersion is queried for and used to compute
  an endpoint.  A wavelength scale set this way will be used for
  other spectra which are not dispersion corrected.
  </dd>
  </dl>
  <dl id="l_q">
  <dt><b>q</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='q' Line='q' -->
  <dd>Quit and go on to next input spectrum.  After the last spectrum exit.
  </dd>
  </dl>
  <dl id="l_r">
  <dt><b>r</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='r' Line='r' -->
  <dd>Redraw the spectrum with the current windowing.  To redraw the full
  spectrum and cancel any windowing use the <span style="font-family: monospace;">'c'</span> key.
  </dd>
  </dl>
  <dl id="l_s">
  <dt><b>s</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='s' Line='s' -->
  <dd>Smooth via a boxcar.  The user is prompted for the box size.
  </dd>
  </dl>
  <dl id="l_t">
  <dt><b>t</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='t' Line='t' -->
  <dd>Fit a function to the spectrum using the ICFIT mode.  Typically
  interactive rejection is used to exclude spectra lines from the fit
  in order to fit a smooth continuum.  A second keystroke
  selects what to do with the fit.
  <dl>
  <dt><b>/</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='/' -->
  <dd>Normalize by the fit.  When fitting the continuum this continuum
  normalizes the spectrum.
  </dd>
  </dl>
  <dl>
  <dt><b>-</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='-' -->
  <dd>Subtract the fit.  When fitting the continuum this continuum subtracts
  the spectrum.
  </dd>
  </dl>
  <dl>
  <dt><b>f</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='f' Line='f' -->
  <dd>Replace the spectrum by the fit.
  </dd>
  </dl>
  <dl>
  <dt><b>c</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='c' Line='c' -->
  <dd>Clean the spectrum by replacing any rejected points by the fit.
  </dd>
  </dl>
  <dl>
  <dt><b>n</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='n' Line='n' -->
  <dd>Do the fitting but leave the spectrum unchanged (a NOP on the spectrum).
  This is useful to play with the spectrum using the capabilities of ICFIT.
  </dd>
  </dl>
  <dl>
  <dt><b>q</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='q' Line='q' -->
  <dd>Quit and don't do any fitting.  The spectrum is not modified.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_u">
  <dt><b>u</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='u' Line='u' -->
  <dd>Adjust the user coordinate scale.  There are three options, <span style="font-family: monospace;">'d'</span> mark a
  position with the cursor and doppler shift it to a specified value,
  <span style="font-family: monospace;">'z'</span> mark a position with the cursor and zeropoint shift it to a specified
  value, or <span style="font-family: monospace;">'l'</span> mark two postions and enter two values to define a linear
  (in wavelength) dispersion scale.  The units used for input are those
  currently displayed.  A wavelength scale set this way will be used for
  other spectra which are not dispersion corrected.
  </dd>
  </dl>
  <dl id="l_v">
  <dt><b>v</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='v' Line='v' -->
  <dd>Toggle to a velocity scale using the position of the cursor as the
  velocity origin and back.
  </dd>
  </dl>
  <dl id="l_w">
  <dt><b>w</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='w' Line='w' -->
  <dd>Window the graph.  For further help type <span style="font-family: monospace;">'?'</span> to the <span style="font-family: monospace;">"window:"</span> prompt or
  see help under <b>gtools</b>.  To cancel the windowing use <span style="font-family: monospace;">'a'</span>.
  </dd>
  </dl>
  <dl id="l_x">
  <dt><b>x</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='x' Line='x' -->
  <dd><span style="font-family: monospace;">"Etch-a-sketch"</span> mode. Straight lines are drawn between successive
  positions of the cursor. Requires 2 cursor settings in x.  The nearest pixels
  are used as the endpoints.  To draw a line between arbitrary y values first
  use <span style="font-family: monospace;">'j'</span> to adjust the endpoints or set the <span style="font-family: monospace;">"xydraw"</span> option.
  </dd>
  </dl>
  <dl id="l_y">
  <dt><b>y</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='y' Line='y' -->
  <dd>Overplot standard star values from a calibration file.
  </dd>
  </dl>
  <dl id="l_z">
  <dt><b>z</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='z' Line='z' -->
  <dd>Zoom the graph by a factor of 2 in x.
  </dd>
  </dl>
  <dl>
  <dt><b>(</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(' -->
  <dd>In multiaperture spectra go to the spectrum in the preceding image line.
  If there is only one line go to the spectrum in the preceding band.
  </dd>
  </dl>
  <dl>
  <dt><b>)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=')' -->
  <dd>In multiaperture spectra go to the spectrum in the following image line.
  If there is only one line go to the spectrum in the following band.
  </dd>
  </dl>
  <dl>
  <dt><b>#</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='#' -->
  <dd>Get a different line in multiaperture spectra or two dimensional images.
  The aperture/line/column is queried.
  </dd>
  </dl>
  <dl>
  <dt><b>%</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='%' -->
  <dd>Get a different band in a three dimensional image.
  </dd>
  </dl>
  <dl>
  <dt><b>$</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='$' -->
  <dd>Switch between physical pixel coordinates and world (dispersion) coordinates.
  </dd>
  </dl>
  <dl>
  <dt><b>-</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='-' -->
  <dd>Subtract the fits generated by the <span style="font-family: monospace;">'d'</span> (deblend), <span style="font-family: monospace;">'k'</span> (single profile fit),
  and <span style="font-family: monospace;">'h'</span> (gaussian of specified width).  The region to be subtracted is
  marked with two cursor positions.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">','</span></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='','' -->
  <dd>Shift the graph window to the left.
  </dd>
  </dl>
  <dl>
  <dt><b>.</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='.' -->
  <dd>Shift the graph window to the right.
  </dd>
  </dl>
  <dl id="l_I">
  <dt><b>I</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='I' Line='I' -->
  <dd>Force a fatal error interupt to leave the graph.  This is used because
  the normal interupt character is ignored in graphics mode.
  </dd>
  </dl>
  <dl>
  <dt><b>:show</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':show' -->
  <dd>Page the full output of the previous deblend and equivalent width
  measurements.
  </dd>
  </dl>
  <dl>
  <dt><b>:log</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':log' -->
  <dd>Enable logging of measurements to the file specified by the parameter
  <i>save_file</i>.  When the program is first entered logging is enabled
  (provided a log file is specified).  There is no way to change the file
  name from within the program.
  </dd>
  </dl>
  <dl>
  <dt><b>:nolog</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':nolog' -->
  <dd>Disable logging of measurements.
  </dd>
  </dl>
  <dl>
  <dt><b>:dispaxis &lt;val&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':dispaxis &lt;val&gt;' -->
  <dd>Show or change dispersion axis for 2D images.
  </dd>
  </dl>
  <dl>
  <dt><b>:nsum &lt;val&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':nsum &lt;val&gt;' -->
  <dd>Show or change summing for 2D images.
  </dd>
  </dl>
  <dl>
  <dt><b>:units &lt;value&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':units &lt;value&gt;' -->
  <dd>Change the coordinate units in the plot.  See below for more information.
  </dd>
  </dl>
  <dl>
  <dt><b>:# &lt;comment&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':# &lt;comment&gt;' -->
  <dd>Add comment to logfile.
  </dd>
  </dl>
  <dl id="l_Labels">
  <dt><b>Labels:</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='Labels' Line='Labels:' -->
  <dd><dl>
  <dt><b>:label &lt;label&gt; &lt;format&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line=':label &lt;label&gt; &lt;format&gt;' -->
  <dd>Add a label at the cursor position.
  </dd>
  </dl>
  <dl>
  <dt><b>:mabove &lt;label&gt; &lt;format&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line=':mabove &lt;label&gt; &lt;format&gt;' -->
  <dd>Add a tick mark and label above the spectrum at the cursor position.
  </dd>
  </dl>
  <dl>
  <dt><b>:mbelow &lt;label&gt; &lt;format&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line=':mbelow &lt;label&gt; &lt;format&gt;' -->
  <dd>Add a tick mark and label below the spectrum at the cursor position.
  </dd>
  </dl>
  The label must be quoted if it contains blanks.  A label beginning
  with % (i.e. %.2f) is treated as a format for the x cursor position.
  The optional format is a gtext string (see help on <span style="font-family: monospace;">"cursors"</span>).
  The labels are not remembered between redraws.
  </dd>
  </dl>
  <dl>
  <dt><b>:auto [yes|no]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':auto [yes|no]' -->
  <dd>Enable/disable autodraw option
  </dd>
  </dl>
  <dl>
  <dt><b>:zero [yes|no]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':zero [yes|no]' -->
  <dd>Enable/disable zero baseline option
  </dd>
  </dl>
  <dl>
  <dt><b>:xydraw [yes|no]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':xydraw [yes|no]' -->
  <dd>Enable/disable xydraw option
  </dd>
  </dl>
  <dl>
  <dt><b>:hist [yes|no]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':hist [yes|no]' -->
  <dd>Enable/disable histogram line type option
  </dd>
  </dl>
  <dl>
  <dt><b>:nosysid [yes|no]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':nosysid [yes|no]' -->
  <dd>Enable/disable system ID option
  </dd>
  </dl>
  <dl>
  <dt><b>:wreset [yes|no]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':wreset [yes|no]' -->
  <dd>Enable/disable window reset for new spectra option
  </dd>
  </dl>
  <dl>
  <dt><b>:flip [yes|no]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':flip [yes|no]' -->
  <dd>Enable/disable the flipped coordinates option
  </dd>
  </dl>
  <dl>
  <dt><b>:overplot [yes|no]</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':overplot [yes|no]' -->
  <dd>Enable/disable the permanent overplot option
  </dd>
  </dl>
  <dl>
  <dt><b>:/help</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':/help' -->
  <dd>Get help on GTOOLS options.
  </dd>
  </dl>
  <dl>
  <dt><b>:.help</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=':.help' -->
  <dd>Get help on standard cursor mode options
  </dd>
  </dl>
  </section>
  <section id="s_profile_fitting_and_deblending">
  <h3>Profile fitting and deblending</h3>
  <p>
  The single profile (<span style="font-family: monospace;">'k'</span>) and multiple profile deblending (<span style="font-family: monospace;">'d'</span>) commands fit
  gaussian, lorentzian, and voigt line profiles with a linear background.
  The single profile fit, <span style="font-family: monospace;">'k'</span> key, is a special case of the multiple profile
  fitting designed to be simple to use.  Two cursor positions define the
  region to be fit and a fixed linear continuum.  The second key is used to
  select the type of profile to fit with <span style="font-family: monospace;">'g'</span> for gaussian, <span style="font-family: monospace;">'l'</span> for
  lorentzian, and <span style="font-family: monospace;">'v'</span> for voigt.  Any other second key will default to a
  gaussian profile.  The profile center, peak strength, and width(s) are then
  determined and the results are printed on the status line and in the log
  file.  The meaning of these quantities is described later.  The fit is also
  overplotted and may be subtracted from the spectrum subsequently with
  the <span style="font-family: monospace;">'-'</span> key.
  </p>
  <p>
  The more complex deblending function, <span style="font-family: monospace;">'d'</span> key, defines the fitting region
  and initial linear continuum in the same way with two cursor positions.
  The continuum may be included in the fitting as an option.  The lines to be
  fit are entered with the cursor near the line center (<span style="font-family: monospace;">'g'</span> for gaussian, <span style="font-family: monospace;">'l'</span>
  for lorentzian, <span style="font-family: monospace;">'v'</span> for voigt), by typing the wavelengths (<span style="font-family: monospace;">'t'</span>), or read
  from a file (<span style="font-family: monospace;">'f'</span>).  The latter two methods are useful if the wavelengths of
  the lines are known accurately and if fits restricting the absolute or
  relative positions of the lines will be used.  The <span style="font-family: monospace;">'t'</span> key is
  restricted to gaussian fits only.
  </p>
  <p>
  The <span style="font-family: monospace;">'f'</span> key asks for a line list file.  The format of this file has
  one or more columns.  The columns are the wavelength, the peak value
  (relative to the continuum with negative values being absorption),
  the profile type (gaussian, lorentzian, or voigt), and the
  gaussian and/or lorentzian FWHM.  End columns may be missing
  or INDEF values may be used to have values be approximated.
  Below are examples of the file line formats
  </p>
  <div class="highlight-default-notranslate"><pre>
  wavelength
  wavelength peak
  wavelength peak (gaussian|lorenzian|voigt)
  wavelength peak gaussian gfwhm
  wavelength peak lorentzian lfwhm
  wavelength peak voigt gfwhm
  wavelength peak voigt gfwhm lfwhm
  
  1234.5                  &lt;- Wavelength only
  1234.5 -100             &lt;- Wavelength and peak
  1234.5 INDEF v          &lt;- Wavelength and profile type
  1234.5 INDEF g 12       &lt;- Wavelength and gaussian FWHM
  </pre></div>
  <p>
  where peak is the peak value, gfwhm is the gaussian FWHM, and lfwhm is
  the lorentzian FWHM.  This format is the same as used by <b>fitprofs</b>
  and also by <b>artdata.mk1dspec</b> (except in the latter case the
  peak is normalized to a continuum of 1).
  </p>
  <p>
  There are four queries made to define the set of parameters to be fit or
  constrained.  The positions may be held <span style="font-family: monospace;">"fixed"</span> at their input values,
  allowed to shift by a <span style="font-family: monospace;">"single"</span> offset from the input values, or <span style="font-family: monospace;">"all"</span>
  positions may be fit independently.  The widths may be
  constrained to a <span style="font-family: monospace;">"single"</span> value or <span style="font-family: monospace;">"all"</span> fit independently.  The linear
  background may be included in the fit or kept fixed at that input using the
  cursor.
  </p>
  <p>
  As noted above, sometimes the absolute or relative wavelengths of the lines
  are known a priori and this information may be entered by typing the
  wavelengths explicitly using the <span style="font-family: monospace;">'t'</span> option or read from a file using the
  <span style="font-family: monospace;">'f'</span> option during marking.  In this case one should fix or fit a single
  shift for the position.  The latter may be useful if the lines are known
  but there is a measurable doppler shift.
  </p>
  <p>
  After the fit, the modeled lines are overplotted.  The line center,
  flux, equivalent width, and full width half maxima are printed on the
  status line for the first line.  The values for the other lines and
  the RMS of the fit may be examined by scrolling the status line
  using the <span style="font-family: monospace;">'+'</span>, <span style="font-family: monospace;">'-'</span>, and <span style="font-family: monospace;">'r'</span> keys.  To continue enter <span style="font-family: monospace;">'q'</span>.
  </p>
  <p>
  The fitting may be repeated with different options until exited with <span style="font-family: monospace;">'q'</span>.
  For each line in the blend the line center, continuum intensity at the
  line center, the core intensity above or below the continuum, the
  FWHM for the gaussian and lorentzian parts, the flux above or below the continuum, and the
  equivalent width are recorded in the log file.  All these parameters
  except the continuum are based on the fitted analytic profiles.
  Thus, even though the fitted region may not extend into the wings of a line
  the equivalent width measurements include the wings in the fitted profile.
  For direct integration of the flux use the <span style="font-family: monospace;">'e'</span> key.
  </p>
  <p>
  The fitted model may be subtracted from the data (after exiting the
  deblending function) using the <span style="font-family: monospace;">'-'</span> (minus) keystroke to delimit the region
  for which the subtraction is to be performed. This allows you to fit a
  portion of a line which may be contaminated by a blend and then subtract
  away the entire line to examine the remaining components.
  </p>
  <p>
  The fitting uses an interactive algorithm based on the Levenberg-Marquardt
  method.  The iterations attempt to improve the fit by varying the parameters
  along the gradient of improvement in the chi square.  This method requires
  that the initial values for the parameters be close enough that the
  gradient leads to the correct solution rather than an incorrect local
  minimum in the chi square.  The initial values are determined as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  1.  If the lines are input from a data file then those values
      in the file are used.  Missing information is determined
      as below.
  2.  The line centers are those specified by the user
      either by marking with the cursor, entering the wavelenths,
      for read from a file.
  3.  The initial widths are obtained by dividing the width of
      the marked fitting region by the number of lines and then
      dividing this width by a factor depending on the profile
      type.
  4.  The initial peak intensities are the data values at the
      given line centers with the marked continuum subtracted.
  </pre></div>
  <p>
  Note that each time a new fitting option is specified the initial parameters
  are those from the previous fits.
  Thus the results do depend on the history of previous fits until the
  fitting is exited.
  Within each fit an iteration of parameters is performed as
  described next.
  </p>
  <p>
  The iteration is more likely to fail if one initially attempts to fit too
  many parameters simultaneously.  A constrained approach to the solution
  is obtained by iterating starting with a few parameters and then adding
  more parameters as the solution approaches the true chi square minimum.
  This is done by using the solutions from the more constrained options
  as the starting point for the less constrained options.  In particular,
  the positions and a single width are fit first with fixed background.
  Then multiple widths and the background are added.
  </p>
  <p>
  To conclude, here are some general comments.  The most restrictive
  (fixed positions and single width(s)) will give odd results if the initial
  positions are not close to the true centers.  The most general
  (simultaneous positions, widths, and background) can also lead to
  incorrect results by using unphysically different widths to make one
  line very narrow and another very broad in an attempt to fit very
  blended lines.  The algorithm works well when the lines are not
  severely blended and the shapes of the lines are close to the profile
  type.
  </p>
  </section>
  <section id="s_centroid__flux__and_equivalent_width_determinations">
  <h3>Centroid, flux, and equivalent width determinations</h3>
  <p>
  There are currently five techniques in SPLOT to measure equivalent widths
  and other line profile parameters. The simplest (conceptually) is by
  integration of the pixel values between two marked pixels. This is
  invoked  with the <span style="font-family: monospace;">'e'</span> keystroke.  The user marks the two edges of the line
  at the continuum.  The measured line center, contiuum value, line flux, and
  equivalent width are given by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  center = sum (w(i) * (I(i)-C(i))**3/2) / sum ((I(i)-C(i))**3/2)
  continuum = C(midpoint)
  flux = sum ((I(i)-C(i)) * (w(i2) - w(i1)) / (i2 - i2)
  eq. width = sum (1 - I(i)/C(i))
  </pre></div>
  <p>
  where w(i) is the wavelength of pixel i,  i1 and i2 are the nearest integer
  pixel limits of the integrated wavelength range, I(i) is the data value of
  pixel i, C(i) is the continuum at pixel (i), and the sum is over the marked
  range of pixels.  The continuum is a linear function between the two points
  marked.  The factor mulitplying the continuum subtracted pixel values
  in the flux calculation is the wavelength interval per pixel so that
  the flux integration is done in wavelength units.  (See the discussion
  at the end of this section concerning flux units).
  </p>
  <p>
  The most complex method for computing line profile parameters is performed
  by the profile fitting and deblending commands which compute a non-linear
  least-squares fit to the line(s).  These are invoked with the <span style="font-family: monospace;">'d'</span> or <span style="font-family: monospace;">'k'</span>
  keystroke.  These were described in detail previously.
  </p>
  <p>
  The fourth and fifth methods, selected with the <span style="font-family: monospace;">'h'</span> key, determine the
  equivalent width from a gaussian profile defined by a constant continuum
  level <span style="font-family: monospace;">"cont"</span>, a core depth <span style="font-family: monospace;">"core"</span>, and the width of the line <span style="font-family: monospace;">"dw"</span> at some
  intermediate level <span style="font-family: monospace;">"Iw"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  I(w) = cont + core * exp (-0.5*((w-center)/sigma)**2)
  sigma = dw / 2 / sqrt (2 * ln (core/Iw))
  fwhm = 2.355 * sigma
  flux = core * sigma * sqrt (2*pi)
  eq. width = abs (flux) / cont
  </pre></div>
  <p>
  where w is wavelength.
  </p>
  <p>
  For ease of use with a large number of lines only one cursor position is
  used to mark the center of the line and one flux level.  Note that both
  the x any y cursor positions are read simultaneously.  From the x cursor
  position the line center and core intensity are determined.  The region around
  the specified line position is searched for a minimum or maximum and a
  parabola is fit to better define the extremum.
  </p>
  <p>
  The two methods based on the simple gaussian profile model differ in how
  they use the y cursor position and what part of the line is used.  After
  typing <span style="font-family: monospace;">'h'</span> one selects the method and whether to use the left, right, or
  both sides of the line by a second keystroke.  The <span style="font-family: monospace;">'l'</span>, <span style="font-family: monospace;">'r'</span>, and <span style="font-family: monospace;">'k'</span> keys
  require a continuum level of one.  The y cursor position defines where the
  width of the line is determined.  The <span style="font-family: monospace;">'a'</span>, <span style="font-family: monospace;">'b'</span>, and <span style="font-family: monospace;">'c'</span> keys use the y
  cursor position to define the continuum and the line width is determined at
  the point half way between the line core and the continuum.  In both cases
  the width at the appropriate level is determined by the interception of the
  y level with the data using linear interpolation between pixels.  The
  one-sided measurements use the half-width on the appropriate side and
  the two-sided measurements use the full-width.
  </p>
  <p>
  The adopted gaussian line profile is drawn over the spectrum and the
  horizontal and vertical lines show the measured line width and the depth of
  the line center from the continuum.  This model may also be subtracted
  from the spectrum using the <span style="font-family: monospace;">'-'</span> key.
  </p>
  <p>
  The major advantages of these methods are that only a single cursor setting
  (both the x and y positions are used) is required and they are fast.  The
  <span style="font-family: monospace;">'l'</span>, <span style="font-family: monospace;">'r'</span>, and <span style="font-family: monospace;">'k'</span> keys give more flexibility in adjusting the width of the
  gaussian line at the expense or requiring that the spectrum be normalized
  to a unit continuum.  The <span style="font-family: monospace;">'a'</span>, <span style="font-family: monospace;">'b'</span>, and <span style="font-family: monospace;">'c'</span> keys allow measurements at any
  continuum level at the expense of only using the half flux level to
  determine the gaussian line width.
  </p>
  <p>
  All these methods print and record in the log file the line center,
  continuum intensity at the line center, the flux, and the equivalent
  width.  For the <span style="font-family: monospace;">'e'</span> key the flux is directly integrated while for the other
  methods the fitted gaussian is integrated.  In addition, for the profile
  fitting methods the core intensity above or below the continuum, and the
  FWHMs are also printed.  A zero value is record for the gaussian or
  lorentzian width if the value is not determined by profile fit.  A brief
  line of data for each measurement is printed on the graphics status line.
  To get the full output and the output from previous measurements use the
  command <span style="font-family: monospace;">":show"</span>.  This pages the output on the text output which may
  involve erasing the graphics.
  </p>
  <p>
  The integrated fluxes for all the methods  are in the same units as the
  intensities and the integration is done in the same units as the
  plotted scale.  It is the user's responsibility to keep track of the flux
  units.  As a caution, if the data is in flux per unit frequency, say
  ergs/cm2/sec/hz, and the dispersion in Angstroms then the integrated
  flux will not be in the usual units but will be A-ergs/cm2/sec/hz.
  For flux in wavelength units, ergs/cm2/sec/A and the dispersion scale
  in Angstroms the integrated flux will be correct; i.e. ergs/cm2/sec.
  </p>
  <p>
  Note that one can compute integrated flux in pixel units  by using the <span style="font-family: monospace;">'$'</span>
  to plot in pixels.  This is appropriate if the pixel values are in
  data numbers or photon counts to get total data number or photons.
  </p>
  </section>
  <section id="s_error_estimates">
  <h3>Error estimates</h3>
  <p>
  The deblending (<span style="font-family: monospace;">'d'</span>), single profile fitting (<span style="font-family: monospace;">'k'</span>), and profile integration and
  equivalent width (<span style="font-family: monospace;">'e'</span>) functions provide error estimates for the measured
  parameters.  This requires a model for the pixel sigmas.  Currently this
  model is based on a Poisson statistics model of the data.  The model
  parameters are a constant gaussian sigma and an <span style="font-family: monospace;">"inverse gain"</span> as specified
  by the parameters <i>sigma0</i> and <i>invgain</i>.  These parameters are
  used to compute the pixel value sigma from the following formula:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sigma**2 = sigma0**2 + invgain * I
  </pre></div>
  <p>
  where I is the pixel value and <span style="font-family: monospace;">"**2"</span> means the square of the quantity.
  </p>
  <p>
  If either the constant sigma or the inverse gain are specified as INDEF or
  with values less than zero then no noise model is applied and no error
  estimates are computed.  Also if the number of error samples is less than
  10 then no error estimates are computed.  Note that for processed spectra
  this noise model will not generally be the same as the detector readout
  noise and gain.  These parameters would need to be estimated in some way
  using the statistics of the spectrum.  The use of an inverse gain rather
  than a direct gain was choosed to allow a value of zero for this
  parameters.  This provides a model with constant uncertainties.
  </p>
  <p>
  The direct profile integration error estimates are computed by error
  propagation assuming independent pixel sigmas.  Also it is assumed that the
  marked linear background has no errors.  The error estimates are one sigma
  estimates.  They are given in the log output (which may also be view
  without exiting the program using the :show command) below the value to
  which they apply and in parenthesis.
  </p>
  <p>
  The deblending and profile fit error estimates are computed by Monte-Carlo
  simulation.  The model is fit to the data (using the sigmas) and this model
  is used to describe the noise-free spectrum.  A number of simulations,
  given by the <i>nerrsample</i> parameter, are created in which random
  gaussian noise is added to the noise-free spectrum using the pixel
  sigmas from the noise model.  The model fitting is done for each simulation
  and the absolute deviation of each fitted parameter to model parameter is
  recorded.  The error estimate for the each parameter is then the absolute
  deviation containing 68.3% of the parameter estimates.  This corresponds to
  one sigma if the distribution of parameter estimates is gaussian though
  this method does not assume this.
  </p>
  <p>
  The Monte-Carlo technique automatically includes all effects of
  parameter correlations and does not depend on any approximations.
  However the computation of the errors does take a significant
  amount of time.  The amount of time and the accuracy of the
  error estimates depend on how many simulations are done.  A
  small number of samples (of order 10) is fast but gives crude
  estimates.  A large number (greater than 100) is slow but gives
  good estimates.  A compromise value of 50 is recommended
  for many applications.
  </p>
  </section>
  <section id="s_units">
  <h3>Units</h3>
  <p>
  The dispersion units capability of <b>splot</b> allows specifying the
  units with the <i>units</i> parameter and interactively changing the units
  with the <span style="font-family: monospace;">":units"</span> command.  In addition the <span style="font-family: monospace;">'v'</span> key allows plotting in
  velocity units with the zero point velocity defined by the cursor
  position.
  </p>
  <p>
  The units are specified by strings having a unit type from the list below
  along with the possible preceding modifiers, <span style="font-family: monospace;">"inverse"</span>, to select the
  inverse of the unit and <span style="font-family: monospace;">"log"</span> to select logarithmic units. For example <span style="font-family: monospace;">"log
  angstroms"</span> to plot the logarithm of wavelength in Angstroms and <span style="font-family: monospace;">"inv
  microns"</span> to plot inverse microns.  The various identifiers may be
  abbreviated as words but the syntax is not sophisticated enough to
  recognized standard scientific abbreviations except as noted below.
  </p>
  <div class="highlight-default-notranslate"><pre>
     angstroms - Wavelength in Angstroms
    nanometers - Wavelength in nanometers
  millimicrons - Wavelength in millimicrons
       microns - Wavelength in microns
   millimeters - Wavelength in millimeters
    centimeter - Wavelength in centimeters
        meters - Wavelength in meters
         hertz - Frequency in hertz (cycles per second)
     kilohertz - Frequency in kilohertz
     megahertz - Frequency in megahertz
      gigahertz - Frequency in gigahertz
           m/s - Velocity in meters per second
          km/s - Velocity in kilometers per second
            ev - Energy in electron volts
           kev - Energy in kilo electron volts
           mev - Energy in mega electron volts
  
            nm - Wavelength in nanometers
            mm - Wavelength in millimeters
            cm - Wavelength in centimeters
             m - Wavelength in meters
            Hz - Frequency in hertz (cycles per second)
           KHz - Frequency in kilohertz
           MHz - Frequency in megahertz
           GHz - Frequency in gigahertz
            wn - Wave number (inverse centimeters)
  </pre></div>
  <p>
  The velocity units require a trailing value and unit defining the
  velocity zero point.  For example to plot velocity relative to
  a wavelength of 1 micron the unit string would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  km/s 1 micron
  </pre></div>
  <p>
  Some additional examples of units strings are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  milliang
  megahertz
  inv mic
  log hertz
  m/s 3 inv mic
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  This task has a very large number of commands and capabilities which
  are interactive and  graphical.  Therefore it these examples are
  fairly superficial.  The user is encouraged to simply experiment with
  the task.  To get some help use the <span style="font-family: monospace;">'?'</span> or <span style="font-family: monospace;">'/'</span> keys.
  </p>
  <p>
  1.  To plot a single spectrum and record any measurements in the file
  'ngc7662':
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; splot spectrum save_file=ngc7662
  </pre></div>
  <p>
  2.  To force all plots to display zero as the minimum y value:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; splot spectrum options="auto, zero"
  </pre></div>
  <p>
  Note that the options auto and zero can be abbreviated to one character.
  </p>
  <p>
  3.  To successively display graphs for a set of spectra with the wavelength
  limits set to 3000 to 6000 angstroms:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; splot spec* xmin=3000 xmax=6000
  </pre></div>
  <p>
  4.  To make batch plots create a file containing the simple cursor command
  </p>
  <div class="highlight-default-notranslate"><pre>
  0 0 0 q
  </pre></div>
  <p>
  or an empty file and then execute one of the following:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; splot spec* graphics=stdplot cursor=curfile
  cl&gt; set stdvdm=splot.mc
  cl&gt; splot spec* graphics=stdvdm cursor=curfile
  cl&gt; splot spec* cursor=curfile &gt;G splot.mc
  </pre></div>
  <p>
  The first example sends the plots to the standard plot device specified
  by the environment variable <span style="font-family: monospace;">"stdplot"</span>.  The next example sends the plots
  to the standard virtual display metacode file specified by the
  environment variable <span style="font-family: monospace;">"stdvdm"</span>.  The last example redirects the
  standard graphics to the metacode file splot.mc.  To spool the metacode
  file the tasks <b>stdplot</b> and <b>gkimosaic</b> may be used.
  For a large number of plots <b>gkimosaic</b> is prefered since it places
  many plots on one page instead of one plot per page.
  The other GKI tasks in the <b>plot</b> package may be used to examine
  the contents of a metacode file.  A simple script call <b>bplot</b> is provided
  which has the default cursor file given above and default device of <span style="font-family: monospace;">"stdplot"</span>.
  </p>
  <p>
  5.  More complex plots may be produced both interactively using the
  <span style="font-family: monospace;">'='</span> key or the <span style="font-family: monospace;">":.snap"</span>  or <span style="font-family: monospace;">":.write"</span> commands or by preparing a script
  of cursor commands.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_SPLOT">
  <dt><b>SPLOT V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SPLOT' Line='SPLOT V2.11' -->
  <dd>The profile fitting and deblending was expanded to include lorentzian
  and voigt profiles.  A new parameter controls the number of Monte-Carlo
  samples used in the error estimates.
  Added colon commands for labeling.
  </dd>
  </dl>
  <dl id="l_SPLOT">
  <dt><b>SPLOT V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SPLOT' Line='SPLOT V2.10.3' -->
  <dd>The <span style="font-family: monospace;">'u'</span> key now allows three ways to adjust the dispersion scale.  The
  old method of setting a linear dispersion scale is retained as well
  as adding a doppler and zeropoint adjustment.  The coordinates are
  input in the currently displayed units.
  If a wavelength scale is set with either <span style="font-family: monospace;">'p'</span> or <span style="font-family: monospace;">'u'</span> then any other
  spectra which are not dispersion corrected will adopt this wavelength
  scale.
  The <span style="font-family: monospace;">'('</span> and <span style="font-family: monospace;">')'</span> keys cycle through bands if there is only one spectrum.
  A new option, <span style="font-family: monospace;">"flip"</span>, has been added to the options parameter to select
  that the spectra are plotted in decreasing wavelength.
  A new options <span style="font-family: monospace;">"overplot"</span> has been added to the options parameters and
  colon commands to permanently set overplotting.  This allows quickly
  overplotting many spectra.
  This task will now write out the current display units in the <span style="font-family: monospace;">"units_display"</span>
  WCS attribute.  The default task units have been changed to <span style="font-family: monospace;">""</span> to allow
  picking up the <span style="font-family: monospace;">"units_display"</span> units if defined.
  The deblending and gaussian fitting code now subsamples the profile by
  a factor of 3 and fits the data pixels to the sum of the three
  subsamples.  This accounts for finite sampling of the data.
  Error estimates are provided for the deblending (<span style="font-family: monospace;">'d'</span>), gaussian fitting
  (<span style="font-family: monospace;">'k'</span>), and profile integration (<span style="font-family: monospace;">'e'</span>) results.
  </dd>
  </dl>
  <dl id="l_SPLOT">
  <dt><b>SPLOT V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SPLOT' Line='SPLOT V2.10' -->
  <dd>This is a new version with a significant number of changes.  In addition to
  the task changes the other general changes to the spectroscopy packages
  also apply.  In particular, long slit spectra and spectra with nonlinear
  dispersion functions may be used with this task.  The image header or
  package dispaxis and nsum parameters allow automatically extracting spectra
  from 2D image.  The task parameters have been modified primarily to obtain
  the desired initial graph without needing to do it interactively.  In
  particular, the new band parameter selects the band in 3D images, the units
  parameter selects the dispersion units, and the new histogram, nosysid, and
  xydraw options select histogram line type, whether to include a system ID
  banner, and allow editing a spectrum using different endpoint criteria.
  Because nearly every key is used there has been some shuffling,
  consolidating, or elimination of keys.  One needs to check the run time <span style="font-family: monospace;">'?'</span>
  help or the help to determine the key changes.
  Deblending may now use any number of components and simultaneous fitting of
  a linear background.  A new simplified version of Gaussian fitting for a
  single line has been added in the <span style="font-family: monospace;">'k'</span> key.  The old <span style="font-family: monospace;">'k'</span>, <span style="font-family: monospace;">'h'</span>, and <span style="font-family: monospace;">'v'</span>
  equivalent width commands are all part of the single <span style="font-family: monospace;">'h'</span> command using a
  second key to select a specific option.  The Gaussian line model from these
  modes may now be subtracted from the spectrum in the same way as the
  Gaussian fitting.  The one-sided options, in particular, are interesting in
  this regard as a new capability.
  The arithmetic functions between two spectra are now done in wavelength
  with resampling to a common dispersion done automatically.  The <span style="font-family: monospace;">'t'</span> key now
  provides for the full power of the ICFIT package to be used on a spectrum
  for continuum normalization, subtraction, or line and cosmic ray removal.
  The <span style="font-family: monospace;">'x'</span> editing key may now use the nearest pixel values rather than only
  the y cursor position to replace regions by straight line segments.  The
  mode is selected by the task option parameter <span style="font-family: monospace;">"xydraw"</span>.
  Control over the graph window (plotting limits) is better integrated so
  that redrawing, zooming, shifting, and the GTOOLS window commands all work
  well together.  The new <span style="font-family: monospace;">'c'</span> key resets the window to the full spectrum
  allowing the <span style="font-family: monospace;">'r'</span> redraw key to redraw the current window to clean up
  overplots from the Gaussian fits or spectrum editing.
  The dispersion units may now be selected and changed to be from hertz to
  Mev and the log or inverse (for wave numbers) of units taken.  As part of
  the units package the <span style="font-family: monospace;">'v'</span> key or colon commands may be used to plot in
  velocity relative to some origin.  The $ key now easily toggles between the
  dispersion units (whatever they may be) and pixels coordinates.
  Selection of spectra has become more complex with multiaperture and long
  slit spectra.  New keys allow selecting apertures, lines, columns, and
  bands as well as quickly scrolling through the lines in multiaperture
  spectra.  Overplotting is also more general and consistent with other tasks
  by using the <span style="font-family: monospace;">'o'</span> key to toggle the next plot to be overplotted.  Overplots,
  including those of the Gaussian line models, are now done in a different
  line type.
  There are new colon commands to change the dispersion axis and summing
  parameters for 2D image, to toggle logging, and also to put comments
  into the log file.  All the options may also be set with colon commands.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  bplot, gtools, icfit, standard, package, specplot, graph, implot, fitprofs
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'PROFILE FITTING AND DEBLENDING' 'CENTROID, FLUX, AND EQUIVALENT WIDTH DETERMINATIONS' 'ERROR ESTIMATES' 'UNITS' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

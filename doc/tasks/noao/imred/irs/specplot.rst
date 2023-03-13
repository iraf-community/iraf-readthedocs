.. _specplot:

specplot: Stack and plot multiple spectra
=========================================

**Package: irs**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  specplot spectra
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_spectra">
  <dt><b>spectra</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectra' Line='spectra' -->
  <dd>List of spectra to plot.  The spectra are assigned index numbers increasing
  from one in the order of the list.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>List of apertures to plot.  An empty list selects all apertures.
  An aperture list consists of a comma separated list of aperture numbers or
  hyphen separated range of numbers.  A step size may also be specified preceded
  by <span style="font-family: monospace;">'x'</span>.  See <b>ranges</b> for more.
  </dd>
  </dl>
  <dl id="l_bands">
  <dt><b>bands = <span style="font-family: monospace;">"1"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bands' Line='bands = "1"' -->
  <dd>List of bands to plot if the image is three dimensional.  The list has
  the same syntax as for the apertures.
  </dd>
  </dl>
  <dl id="l_dispaxis">
  <dt><b>dispaxis = 1, nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispaxis' Line='dispaxis = 1, nsum = 1' -->
  <dd>Parameters for defining vectors in 2D images.  The
  dispersion axis is 1 for line vectors and 2 for column vectors.
  A DISPAXIS parameter in the image header has precedence over the
  <i>dispaxis</i> parameter.  These may be changed interactively.
  </dd>
  </dl>
  <dl id="l_autolayout">
  <dt><b>autolayout = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='autolayout' Line='autolayout = yes' -->
  <dd>Automatically layout the spectra by shifting or scaling to a common mean
  and determining a separation step which does overlaps the spectra
  by the specified fraction?  The algorithm uses the following parameters.
  <dl>
  <dt><b>autoscale = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='autoscale' Line='autoscale = yes' -->
  <dd>Scale the spectra to a common mean?  If no then the spectra are shifted
  to a common mean and if yes they are scaled to a common mean.
  </dd>
  </dl>
  <dl>
  <dt><b>fraction = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='fraction' Line='fraction = 1.' -->
  <dd>The separation step which just avoids overlapping the spectra is multiplied
  by this number.  Numbers greater than 1 increase the separation while numbers
  less than 1 decrease the separation and provide some amount of overlap.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_units">
  <dt><b>units = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='units' Line='units = ""' -->
  <dd>Dispersion coordinate units.  If the spectra have known units, currently
  this is generally Angstroms, the plotted units may be converted
  for plotting to other units as specified by this parameter.
  If this parameter is the null string then the units specified by the
  world coordinate system attribute <span style="font-family: monospace;">"units_display"</span> is used.  If neither
  is specified than the units of the coordinate system are used.
  The units
  may also be changed interactively.  See the units section of the
  <b>onedspec</b> help for a further description and available units.
  </dd>
  </dl>
  <dl id="l_transform">
  <dt><b>transform = <span style="font-family: monospace;">"none"</span> (none|log)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='transform' Line='transform = "none" (none|log)' -->
  <dd>Transform for the input pixel values.  Currently only <span style="font-family: monospace;">"log"</span> is implemented.
  If all pixels are negative the spectrum values will be unchanged and if
  some pixels are negative they are mapped to the lowest non-negative value in
  the spectrum.  Note that this cannot be changed interactively or applied
  independently for each spectrum.  To change the setting one must exit
  the task and execute it with the new value.
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = 1., offset = 0. (value, @file, keyword)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = 1., offset = 0. (value, @file, keyword)' -->
  <dd>The scale and offset to apply to each spectrum.  The value of the parameter
  may be a constant value applying to all spectra, a file containing the
  values specified as @&lt;file&gt; where &lt;file&gt; is the filename, or an image
  header keyword whose value is to be used.
  </dd>
  </dl>
  <dl id="l_step">
  <dt><b>step = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='step' Line='step = 0' -->
  <dd>The step separating spectra when not using the autolayout option.
  The value of this parameter depends on the range of the data.
  </dd>
  </dl>
  <dl id="l_ptype">
  <dt><b>ptype = <span style="font-family: monospace;">"1"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ptype' Line='ptype = "1"' -->
  <dd>Default plotting type for the spectra.  A numeric value selects line plots
  while marker type strings select marker plots.  The sign of the line type
  number selects histogram style lines when negative or connected pixel
  values when positive.  The absolute value selects the line type with 0
  being an invisible line, 1 being a solid line, and higher integers
  different types of lines depending on the capabilities of the graphics
  device.  The marker type strings are <span style="font-family: monospace;">"point"</span>, <span style="font-family: monospace;">"box"</span>, <span style="font-family: monospace;">"plus"</span>, <span style="font-family: monospace;">"cross"</span>,
  <span style="font-family: monospace;">"diamond"</span>, <span style="font-family: monospace;">"hline"</span>, <span style="font-family: monospace;">"vline"</span>, <span style="font-family: monospace;">"hebar"</span>, <span style="font-family: monospace;">"vebar"</span>, and <span style="font-family: monospace;">"circle"</span>.
  The types for individual spectra may be changed interactively.
  </dd>
  </dl>
  <dl id="l_labels">
  <dt><b>labels = <span style="font-family: monospace;">"user"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='labels' Line='labels = "user"' -->
  <dd>Spectrum labels to be used.  If the null string or the word <span style="font-family: monospace;">"none"</span> is
  given then the spectra are not labeled.  The word <span style="font-family: monospace;">"imname"</span> labels the
  spectra with the image name, the word <span style="font-family: monospace;">"imtitle"</span> labels them wih the
  image title, the word <span style="font-family: monospace;">"index"</span> labels them with the index number, and
  the word <span style="font-family: monospace;">"user"</span> labels them with user defined labels.  The user labels
  may be given in the file specified by the parameter <i>ulabels</i>, which
  are matched with the list of spectra, and also added interactively.
  </dd>
  </dl>
  <dl id="l_ulabels">
  <dt><b>ulabels = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ulabels' Line='ulabels = ""' -->
  <dd>File containing user labels.
  </dd>
  </dl>
  <dl id="l_xlpos">
  <dt><b>xlpos = 1.02, ylpos = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xlpos' Line='xlpos = 1.02, ylpos = 0.0' -->
  <dd>The starting position for the spectrum labels in fractions of the
  graph limits.  The horizontal (x) position is measured from the left
  edge while the vertical position is measured from the mean value of the
  spectrum.  For vertical positions a negative value may be used to label
  below the spectrum.  The default is off the right edge of the graph at
  the mean level of the spectrum.
  </dd>
  </dl>
  <dl id="l_sysid">
  <dt><b>sysid = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sysid' Line='sysid = yes' -->
  <dd>Include system banner and separation step label?  This may be changed
  interactively using <span style="font-family: monospace;">":/sysid"</span>.
  </dd>
  </dl>
  <dl id="l_yscale">
  <dt><b>yscale = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='yscale' Line='yscale = no' -->
  <dd>Draw a Y axis scale?  Since stacked plots are relative labeling the Y
  axes may not be useful.  This parameter allows adding the Y axis scale
  if desired.  The default is to not have a Y axis scale.
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = <span style="font-family: monospace;">""</span>, xlabel = <span style="font-family: monospace;">""</span>, ylabel = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = "", xlabel = "", ylabel = ""' -->
  <dd>Title, x axis label, and y axis label for graphs.  These may be changed
  interactively using <span style="font-family: monospace;">":/title"</span>, <span style="font-family: monospace;">":/xlabel"</span>, and <span style="font-family: monospace;">":/ylabel"</span>.
  </dd>
  </dl>
  <dl id="l_xmin">
  <dt><b>xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmin' Line='xmin = INDEF, xmax = INDEF, ymin = INDEF, ymax = INDEF' -->
  <dd>The default limits for the initial graph.  If INDEF then the limit is
  determined from the range of the data (autoscaling).  These values can
  be changed with <span style="font-family: monospace;">'w'</span> cursor key or the cursor commands <span style="font-family: monospace;">":/xwindow"</span> and
  <span style="font-family: monospace;">":/ywindow"</span>.
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = ""' -->
  <dd>Logfile to record the final set of spectra and scale factors displayed.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Output graphics device.  One of <span style="font-family: monospace;">"stdgraph"</span>, <span style="font-family: monospace;">"stdplot"</span>, <span style="font-family: monospace;">"stdvdm"</span>,
  @(enviroment variable), or actual device.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input.  When null the standard cursor is used otherwise
  the specified file is used.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Specplot</b> plots multiple spectra with provisions for scaling them,
  separating them vertically, shifting them horizontally, and labeling them.
  The layout can be defined by an automatic algorithm or explicitly and
  adjusted noninteractively (with some limitations) or interactively.  The
  plotting units can be selected and the vertical axis scale can be shown or
  not as desired.  This task is used for compressing many spectra to a page
  for review, intercomparison of spectra, classification against standards,
  and final display.
  </p>
  <p>
  The input list of spectra consists of one, two, or three dimensional images.
  The set of spectra may be restricted to specific apertures using the
  <i>apertures</i> parameter.  Note that for true 2D images, such as long slit
  spectra, the aperture number corresponds to the line or column to be plotted
  and the dispersion axis and nsum parameter are determined either from the
  image header or the package parameters.  Spectra extracted
  with the <b>apextract</b> package may be three dimensional where the 3rd
  dimension corresponds to related data.  The higher dimensional data is
  also plotted though it may be restricted with the <i>bands</i>
  parameter.
  </p>
  <p>
  Each spectrum has a number of associated parameters which are initially
  assigned default values but which may be changed interactively.  First each
  spectrum is assigned an index number.  This is generally sequential
  starting from 1.  Spectra added interactively are assigned the next higher
  or lower index relative to the spectrum being appended or inserted.  The
  index is used for refering to parameters of a particular spectrum and for
  separating the spectra vertically.  The spectra are scaled and shifted by
  the equation
  </p>
  <p>
  	I = value * scale + offset + (index - 1) * step
  </p>
  <p>
  where <span style="font-family: monospace;">"I"</span> is the final plotted value, <span style="font-family: monospace;">"value"</span> is the pixel value, <span style="font-family: monospace;">"scale"</span>
  is a multiplicative scaling, <span style="font-family: monospace;">"offset"</span> is a additive offset, and <span style="font-family: monospace;">"step"</span> is
  an additive separation step used to stack spectra vertically.
  </p>
  <p>
  The default values of the vertical scaling parameters may be set by an
  automatic layout algorithm or with explicit constants (the same for all
  spectra).  The automatic mode is selected with the parameter
  <i>autolayout</i> and works as follows.  All spectra are scaled or shifted
  to a common mean (depending on the parameter <i>autoscale</i>) relative to
  the lowest indexed spectrum.  A step size is then computed to just avoid
  overlapping of the minimum of one spectrum with the maximum of another.
  Note that this may not yield a good layout if the spectra have large
  continuum slopes.  Finally, to add some extra space between the spectra or
  to allow some overlap, the minimum step is multiplied by a specified
  overlap factor, <i>fraction</i>.
  </p>
  <p>
  In nonautomatic mode the user specifies the intensity scale, offset,
  and separation step explicitly with the parameters, <i>scale, offset</i>
  and <i>step</i>.  If the step is zero then spectra will be directly
  overplotted while a positive or negative value will separate the
  spectra either upward or downward with the index 1 spectrum having no
  offset.  The scale and offset parameters may be specified as either
  constant values, the name of file containing the values (one per line)
  preceded by the <span style="font-family: monospace;">'@'</span> character, or the name of an image header keyword.
  This parameter as well as the scale and offset may be set or
  changed interactively via colon commands and the <span style="font-family: monospace;">"offset"</span> may also be
  set using the cursor to shift a spectrum vertically.
  </p>
  <p>
  In addition to shifting spectra vertically they may also be shifted
  horizontally as a velocity/redshift or a zero point change with either
  cursor or colon commands.  The dispersion, inteval per pixel, may be
  modified, either with the <span style="font-family: monospace;">'t'</span> key or the <span style="font-family: monospace;">"wpc"</span> command, in which case if
  the dispersion is nonlinear the spectra will be linearized.
  </p>
  <p>
  Each spectrum may have a label associated with it.  The label type may
  be the image name, the image title, the index number, or a user defined
  label.  The default label type is specified by the parameter
  <i>labels</i>.  For user labels the initial labels may be specified in a
  file.  Interactively the label type may be changed using the <span style="font-family: monospace;">":labels"</span>
  command and the user assigned labels may be defined by a colon command
  or by using the cursor to mark the position for the label.  The label
  position is given relative to the range of the graph and the mean
  intensity.  The default values are set by the parameters <i>xlpos</i>
  and <i>ylpos</i>.  The positions may be changed interactively for all
  the spectra or individually.  The latter may be done using the cursor
  to mark exactly where the label is to go.
  </p>
  <p>
  Each spectrum has an associated plotting type.  The default type which
  applies to all spectra initially is specified by the parameter
  <i>ptype</i>.  This parameter specifies both whether line mode or
  marker mode is used and the line type, line style, or marker type to use.
  The line
  mode and types are given by a small integers with the style, connected
  pixel centers or histogram style, chosed by the sign of the integer.
  The type of lines produced depend on the capabilities of the terminal.  In most
  cases a zero line type is invisible.  (This may be used interactively
  to temporarily eliminate a spectrum from a plot instead of deleting the
  spectrum from the list of spectra).  A line type of 1 is a solid line
  and additional line types are specified by higher numbers.
  The marker types are given by name as described in the parameter
  section.  There is currently no combination of line and marker (such as
  connected points with vertical bars) or histogram type plotting.  The
  plotting type may be changed interactively for individual spectra or
  for all spectra using colon commands.
  </p>
  <p>
  The cursor and colon commands generally apply to the spectrum nearest
  the cursor.  This is determined by finding the nearest data point to
  the cursor.  For the colon commands the spectrum may also be specified
  explicitly by the index number using an optional suffix <span style="font-family: monospace;">"[index]"</span>, where
  index is the index number for the spectrum.  Also the special index <span style="font-family: monospace;">"*"</span>
  may be specified to apply to all spectra.
  </p>
  <p>
  The operations of adding, deleting, moving, or shifting spectra affect
  the index numbers of the other spectra.  When deleting a spectrum the
  index numbers of all spectra with greater index numbers are decreased
  by one resulting in the plotted spectra moving down (positive step).
  When adding a spectrum the index numbers above the inserted spectrum
  are increased by one resulting in the spectra moving up.  Moving a
  spectrum to a new index number is equivalent to deleting the spectrum
  and then inserting it at the new index position.  Spectra may be
  shifted to insert gaps in the plotted spectra.  The specified value is
  added to all spectra above and including the one indicated if the value
  is positive to all spectra below and including the one indicated if the
  value is negative.
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <p>
  The indicated spectrum is the one with a point closest to the cursor position.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ? - Print help summary
  a - Append a new spectrum following the indicated spectrum
  i - Insert a new spectrum before the indicated spectrum
  d - Delete the indicated spectrum
  e - Insert last deleted spectrum before indicated spectrum
  f - Toggle between world coordinates and logical pixel coordinates
  l - Define the user label at the indicated position
  p - Define the label position at the indicated position
  o - Reorder the spectra to eliminate gaps
  q - Quit
  r - Redraw the plot
  s - Repeatedly shift the indicated spectrum position with the cursor
       q - Quit shift                      x - Shift horizontally in velocity
       s - Shift vertically in scale       y - Shift vertically in offset
       t - Shift horizontally in velocity  z - Shift horizontally in velocity
           and vertically in scale             and vertically in offset
  t - Set a wavelength scale using the cursor
  u - Set a wavelength point using the cursor
  v - Set velocity plot with zero point at cursor
  w - Window the plot
  x - Cancel all scales and offsets
  y - Automatically layout the spectra with offsets to common mean
  z - Automatically layout the spectra scaled to common mean
  </pre></div>
  </section>
  <section id="s_colon_commands">
  <h3>Colon commands</h3>
  <p>
  A command without a value generally shows the current value of the
  parameter while with a value it sets the value of the parameter.  The show
  commands print to the terminal unless a file is given.  For the spectrum
  parameters the index specification, <span style="font-family: monospace;">"[index]"</span>, is optional.  If absent the
  nearest spectrum to the cursor when the command is given is selected except
  for the <span style="font-family: monospace;">"units"</span> command which selects all spectra.  The index is either a
  number or the character *.  The latter applies the command to all the
  spectra.
  </p>
  <div class="highlight-default-notranslate"><pre>
  :show &lt;file&gt;               Show spectrum parameters (file optional)
  :vshow &lt;file&gt;              Show verbose parameters (file optional)
  :step &lt;value&gt;              Set or show step
  :fraction &lt;value&gt;          Set or show autolayout fraction
  :label &lt;value&gt;             Set or show label type
                                  (none|imtitle|imname|index|user)
  
  :move[index] &lt;to_index&gt;    Move spectrum to new index position
  :shift[index|*] &lt;value&gt;    Shift spectra by adding to index
  :w0[index|*] &lt;value&gt;       Set or show zero point wavelength
  :wpc[index|*] &lt;value&gt;      Set or show wavelength per channel
  :velocity[index|*] &lt;value&gt; Set or show radial velocity (km/s)
  :redshift[index|*] &lt;value&gt; Set or show redshift
  :offset[index|*] &lt;value&gt;   Set or show intensity offset
  :scale[index|*] &lt;value&gt;    Set or show intensity scale
  :xlpos[index|*] &lt;value&gt;    Set or show X label position
  :ylpos[index|*] &lt;value&gt;    Set or show Y label position
  :ptype[index|*] &lt;value&gt;    Set or show plotting type
  :color[index|*] &lt;value&gt;    Set or show color (1-9)
  :ulabel[index|*] &lt;value&gt;   Set or show user labels
  :units[index|*] &lt;value&gt;    Change coordinate units
  
  :/title &lt;value&gt;            Set the title of the graph
  :/xlabel &lt;value&gt;           Set the X label of the graph
  :/ylabel &lt;value&gt;           Set the Y label of the graph
  :/xwindow &lt;min max&gt;        Set the X graph range
                                  (use INDEF for autoscaling)
  :/ywindow &lt;min max&gt;        Set the X graph range
                                  (use INDEF for autoscaling)
  </pre></div>
  <p>
  Examples:
  </p>
  <div class="highlight-default-notranslate"><pre>
  w0            Print value of wavelength zero point
  w0 4010       Set wavelength zero point of spectrum nearest the cursor
  w0[3] 4010    Set wavelength zero point of spectrum with index 3
  w0[*] 4010    Set wavelength zero point of all spectra
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To make a nice plot of a set of spectra with the default layout:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; specplot spec*
  </pre></div>
  <p>
  2.  To set the colors or line types for multiple spectra in a batch
  mode application create a cursor file like:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type cursor.dat
  :color[1] 2
  :color[2] 3
  :color[3] 4
  r
  cl&gt; specplot im1,im2,im3 cursor=cursor.dat
  </pre></div>
  <p>
  Note that the <span style="font-family: monospace;">'r'</span> key is necessary redraw the graph with the changed
  attributes.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_SPECPLOT">
  <dt><b>SPECPLOT V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SPECPLOT' Line='SPECPLOT V2.11' -->
  <dd>The scale and offset parameters may now be a value, a filename, or
  and image header keyword.
  The <span style="font-family: monospace;">'f'</span> key was added to toggle between world and logical pixel coordinates.
  </dd>
  </dl>
  <dl id="l_SPECPLOT">
  <dt><b>SPECPLOT V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SPECPLOT' Line='SPECPLOT V2.10.3' -->
  <dd>A color parameter was added for graphics terminals supporting color.
  The :units command was extended to have an optional spectrum specifier.
  This is primarily intended to plot different (or the same) spectra in
  velocity but with different velocity zeros.
  The default task units parameter has been changed to <span style="font-family: monospace;">""</span> to allow picking
  up a <span style="font-family: monospace;">"units_display"</span> WCS attribute if defined.
  </dd>
  </dl>
  <dl id="l_SPECPLOT">
  <dt><b>SPECPLOT V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SPECPLOT' Line='SPECPLOT V2.10' -->
  <dd>New parameters were added to select apertures and bands, plot
  additional dimensions (for example the additional output from the extras
  option in <b>apextract</b>), suppress the system ID banner, suppress the Y
  axis scale, output a logfile, and specify the plotting units.  The <i>ptype</i>
  parameter now allows negative numbers to select histogram style lines.
  Interactively, the plotting units may be changed and the <span style="font-family: monospace;">'v'</span> key allows
  setting a velocity scale zero point with the cursor.  The new version
  supports the new spectral WCS features including nonlinear dispersion
  functions.
  </dd>
  </dl>
  </section>
  <section id="s_notes">
  <h3>Notes</h3>
  <p>
  The automatic layout algorithm is relatively simple and may not
  provide visually satisfactory results in all cases.  The fonts and Y axis
  scale capabilities are not as good as might be desired for publication
  quality plots.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  bplot, splot, onedspec, gtools, ranges
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'COLON COMMANDS' 'EXAMPLES' 'REVISIONS' 'NOTES' 'SEE ALSO'  -->
  

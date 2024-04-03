.. _pltrans:

pltrans: Plot photometric transformation diagrams (e.g., color-color
====================================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pltrans spectrum xmode ymode xform yform
  </p>
  </section>
  <section id="s_description_">
  <h3>Description </h3>
  <p>
  This task plots general photometric transformation diagrams, such as
  Color-Color and Color-Magnitude diagrams.  The user specifies a set of
  spectra and a mode and a form for each axis. Most usually the
  'spectrum' parameter is a filename preceded by a <span style="font-family: monospace;">"@"</span> character. The
  file contains one filename or synphot spectral expression per
  line. The parameter 'vzero' can also be used to generate a set of
  spectra. Precalculated photometric data for plotting can be read in
  from the file specified by the 'input' parameter and results can be
  saved in table specified by the'output' parameter.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_spectrum">
  <dt><b>spectrum [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectrum' Line='spectrum [string]' -->
  <dd>This is a sequence of commands that create the synthetic spectrum.
  The commands can be placed in a file, whose name is passed to this
  parameter, preceded by a <span style="font-family: monospace;">"@"</span> character, e.g., '@filename'. Each line
  in this command file is treated as a separate set of commands. If this
  parameter is left blank or set to none, the only points plotted will
  be those read from the table specified in parameter 'input'
  The commands that can be passed to this parameter are described in
  detail in the help file for the 'calcspec' task.
  </dd>
  </dl>
  <dl id="l_xmode">
  <dt><b>xmode [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xmode' Line='xmode [string]' -->
  <dd>Mode for the X-axis of the plot.  This can be either a single mode or
  a color difference. Single modes are specified using the syntax
  <span style="font-family: monospace;">"band(mode)"</span>, or simply <span style="font-family: monospace;">"mode"</span>. Color differences are specified using
  the syntax <span style="font-family: monospace;">"band(mode1) - band(mode2)"</span>. <span style="font-family: monospace;">"Mode"</span>, <span style="font-family: monospace;">"mode1"</span>, and <span style="font-family: monospace;">"mode2"</span>
  are comma separated lists of observation mode keywords. These keywords
  are described in the obsmode task. If this parameter is left blank or
  set to <span style="font-family: monospace;">"none"</span>, a default observation mode that is everywhere one will
  be used.
  </dd>
  </dl>
  <dl id="l_ymode">
  <dt><b>ymode [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ymode' Line='ymode [string]' -->
  <dd>Mode for the Y-axis. This can also be either a single mode or a color 
  difference. The syntax is the same as used by xmode.
  </dd>
  </dl>
  <dl id="l_xform">
  <dt><b>xform [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xform' Line='xform [string]' -->
  <dd>Form of the X data. The following forms are recognized:
  <div class="highlight-default-notranslate"><pre>
  
  FNU             erg / s / cm^2 / Hz
  FLAM            erg / s / cm^2 / A
  PHOTNU          photons / s / cm^2 / Hz
  PHOTLAM         photons / s / cm^2 / A
  COUNTS          photons / s
  ABMAG           -2.5 log_10 (FNU)  - 48.60
  STMAG           -2.5 log_10 (FLAM) - 21.10
  VEGAMAG         -2.5 log_10 (F/F_vega)
  OBMAG           -2.5 log_10 (COUNTS)
  JY              10^-23 erg / s / cm^2 / Hz
  MJY             10^-26 erg / s / cm^2 / Hz
  
  </pre></div>
  A standard magnitude system is VEGAMAG, for which Vega by definition
  has magnitude 0 at all wavelengths. The AB and ST magnitude systems are
  based on constant flux per unit frequency and per unit wavelength,
  respectively.  The zero points for these two systems are set for
  convenience so that Vega has magnitude 0 in both systems for the
  Johnson V passband.
  </dd>
  </dl>
  <dl id="l_yform">
  <dt><b>yform [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='yform' Line='yform [string]' -->
  <dd>Form of the Y data. The same forms recognized for xform are also
  recognized for yform.
  </dd>
  </dl>
  <dl>
  <dt><b>(vzero = <span style="font-family: monospace;">" "</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(vzero = " ") [string]' -->
  <dd>A list of values to substitute for variable zero. Each value in the
  list is substituted in turn for the string '$0' wherever it occurs in
  the input spectrum. The values must be real numbers.  Using vzero is
  the equivalent of placing the input spectrum several times in a
  file, with each spectrum containing one of the values in the list. The
  list may contain single values or ranges. The endpoints of the ranges
  are separated by a dash. An optional step size follows the range,
  preceded by the letter <span style="font-family: monospace;">'x'</span>. If the step size is not present, the step
  size defaults to 1 or -1, depending on the order of the endpoints.
  The following table gives several examples of valid lists
  <div class="highlight-default-notranslate"><pre>
  
  .1,.2,.3,.4     A list of single values
  .1-.4x.1        The same list expressed as a range
  -1 - -4         A range with an implicit step size of -1
  1-9,10-20x2     A list of more than one range
  </pre></div>
  </dd>
  </dl>
  <dl>
  <dt><b>(input = <span style="font-family: monospace;">"none"</span>) [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(input = "none") [file name]' -->
  <dd>Name of a file containing calculated X-Y pairs of points for 
  plotting. The x and y coordinates of the points are read frum columns
  <span style="font-family: monospace;">"FLUX1"</span> and <span style="font-family: monospace;">"FLUX2"</span>, if the file is an SDAS table and the first and
  second columns if the file is an ascii file. If the file is an SDAS
  table, the values of xmode, ymode, xform, and yform will be read from
  table header parameters of the same name and these values will
  supersede the values in the parameter file. If the value of this
  parameter is <span style="font-family: monospace;">"none"</span> or blank, no file will be read.
  </dd>
  </dl>
  <dl>
  <dt><b>(output = <span style="font-family: monospace;">"none"</span>) [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(output = "none") [file name]' -->
  <dd>Name of the SDAS table used for output. The table has two columns,
  <span style="font-family: monospace;">"FLUX1"</span> and <span style="font-family: monospace;">"FLUX2"</span>, containing the x and y coordinates of the data
  points. It has four header parameters, <span style="font-family: monospace;">"XFORM"</span>, <span style="font-family: monospace;">"YFORM"</span>, <span style="font-family: monospace;">"XMODE"</span>, and
  <span style="font-family: monospace;">"YMODE"</span>, containing the values of the respective task parameters. If
  the value of append is set to yes and a table of the same name already
  exists, the data will be appended to the existing table. Otherwise it
  will overwrite it. This table has the same format as the table read
  'input', so output generated from this task can be replotted later
  without recalculating it. If the value of this parameter is <span style="font-family: monospace;">"none"</span> or
  blank, no file will be written.
  </dd>
  </dl>
  <dl>
  <dt><b>(left = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(left = INDEF) [real]' -->
  <dd>Minimum x value to plot. If set to INDEF, the task will set it
  to the minimum x value.
  </dd>
  </dl>
  <dl>
  <dt><b>(right = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(right = INDEF) [real]' -->
  <dd>Maximum x value to plot. If set to INDEF, the task will set it
  to the maximum x value.
  </dd>
  </dl>
  <dl>
  <dt><b>(bottom = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(bottom = INDEF) [real]' -->
  <dd>Minimum y value to plot. If set to INDEF, the task will set it
  to the minimum y value.
  </dd>
  </dl>
  <dl>
  <dt><b>(top = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(top = INDEF) [real]' -->
  <dd>Maximum y value to plot. If set to INDEF, the task will set it
  to the maximum y value.
  </dd>
  </dl>
  <dl>
  <dt><b>(append = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(append = no) [boolean]' -->
  <dd>Append results to an existing plot? 
  </dd>
  </dl>
  <dl>
  <dt><b>(mktype = <span style="font-family: monospace;">"plus"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(mktype = "plus") [string]' -->
  <dd>The marker type to be used for plotting the results. The value of this
  parameter is either a text string preceded by an exclamation point, in
  which case the text minus the exclamation point will be plotted at
  each data point; a line symbol (clear, solid, dashed, dotted, or
  dotdash), in which case a line will be plotted through the data
  points, or a point symbol (point, fill, box, plus, cross, diamond,
  hline, vline, hebar, vebar, or circle), in which case the indicated
  symbol will be plotted at the data point.
  </dd>
  </dl>
  <dl>
  <dt><b>(device = <span style="font-family: monospace;">"stdgraph"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(device = "stdgraph") [string]' -->
  <dd>Send output to the designated device.
  </dd>
  </dl>
  <dl>
  <dt><b>(wavetab = <span style="font-family: monospace;">""</span>) [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wavetab = "") [file name]' -->
  <dd>Name of an optional wavelength table or file. An appropriate table can
  be generated by using the 'genwave' task. If a table is used, the
  wavelength column name must be <span style="font-family: monospace;">"WAVELENGTH"</span>. If an ASCII file is used
  the first column is taken to be the wavelength column.  The
  subdirectory 'synphot$data has ASCII wavelength tables useful for
  specific HST passbands.  
  If no wavelength table is specified, the task generates a wavelength
  set which covers the range between the left and right plot limits. If
  there is no wavelength table, and plot limits are not specified, a
  default wavelength set is used. The default wavelength set covers the
  wavelength range where the spectrum is non-zero. Wavelengths are
  spaced logarithmically over this range. If more than one spectrum is
  plotted, the range is computed based on the first spectrum. If the
  wavelength range of the spectra differ significantly, a wavelength
  table should be specified explicitly or plot limits should be set.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl>
  <dt><b>(refdata = <span style="font-family: monospace;">" "</span>) [pset name]</b></dt>
  <!-- Sec='PARAMETERS' Level=-1 Label='' Line='(refdata = " ") [pset name]' -->
  <dd><p>
  Parameter set for reference data used in calculations.  The following 
  parameters are stored in this set.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  area = 45238.93416:  HST telescope area in cm**2.
  
  grtbl = "mtab$*.tmg":  HST graph table.  Uses the
            most recent version by default.
  
  cmptbl = "mtab$*.tmc":  Instrument component table.
             The most recent version is used by default.
  
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  1. Produce a color magnitude diagram of a list of stars:
  sy&gt; pltrans @bpgs.lis <span style="font-family: monospace;">"band(v)"</span> <span style="font-family: monospace;">"band(b)-band(v)"</span> stmag stmag
  2. Show how the counts through the wfpc f555w filter vary with the
  color of the star:
  sy&gt; pltrans <span style="font-family: monospace;">"rn(bb($0),band(v),10,stmag)"</span> <span style="font-family: monospace;">"band(b)-band(v)"</span> \<br>
  &gt;&gt;&gt; <span style="font-family: monospace;">"band(wfpc,f555w)"</span> stmag counts vzero=<span style="font-family: monospace;">"3e3-2e4x1e3"</span>
  </section>
  <section id="s_references">
  <h3>References</h3>
  Written by B.Simon based on XCAL code written by Keith Horne
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  plspec
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION ' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

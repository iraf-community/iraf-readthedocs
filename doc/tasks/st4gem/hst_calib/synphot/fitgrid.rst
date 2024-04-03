.. _fitgrid:

fitgrid: Fit a spectrum model to a grid of spectral data.
=========================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fitgrid input spectrum
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task reads an input spectrum from a table. It then computes each
  spectrum in a list of spectra, scales them to the same flux as the
  input spectrum, and computes the squared difference between it and the
  input spectrum. The two spectra with the smallest squared difference
  are then selected and a least squares solution is performed to get the
  best linear interpolation between these two spectra. The resulting fit
  can optionally be saved in a table by setting the parameter 'output'
  to a filename.
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
  <dd>A list of spectra to be compared to the input spectrum. The list can
  be placed in a file, whose name is passed to this parameter, preceded
  by a <span style="font-family: monospace;">"@"</span> character, .e.g., '@filename'. Each line in the file is
  treated as a separate spectrun. Alternatively, the string '$0' can be
  placed in the expression and the values of vzero will be substituted
  for the string, creating a list of spectra. The form of a synphot
  expression is discussed in detail in the help file for the 'calcspec'
  task.
  </dd>
  </dl>
  <dl>
  <dt><b>(output = <span style="font-family: monospace;">"none"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(output = "none") [string]' -->
  <dd>The name of the output table containing the fitted spectrum. If
  'output' is set to <span style="font-family: monospace;">"none"</span> or left blank, no table will be produced.
  The output table contains the best fit from the list of spectra to the
  input spectrum. The flux units are the same as the input
  spectrophotmetry file. The header of the table contains the names of
  the graph and component lookup tables and the model expression.
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
  <dt><b>(ftol = 1.0e-5) [real, min = 0.0,  max = INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ftol = 1.0e-5) [real, min = 0.0,  max = INDEF]' -->
  <dd>The fractional tolerance convergence criterion. Iteration of the least
  square fit ceases when the scaled distance between two successive
  estimates of the fit variables is less than this value. Each
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
  fit variables.
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
  estimates.
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
  <dt><b>(refdata = <span style="font-family: monospace;">""</span>) [pset name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(refdata = "") [pset name]' -->
  <dd>Parameter set for reference data used in calculations.
  This pset contains the following parameters:
  <div class="highlight-default-notranslate"><pre>
  
  area = 45238.93416:  HST telescope area in cm**2.
  
  grtbl = "mtab$*.tmg":  HST graph table.  By default, this
          uses the most recent version.
  
  cmptbl = "mtab$*.tmc":  Instrument component table.  By
          default, this uses the most recent version.
  
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Fit a series of model spectra to the spectrum of Eta Ursa Majoris.
  The model spectra are contained in the file grid.lis:
  </p>
  <div class="highlight-default-notranslate"><pre>
  crrefer$grid/bpgs/bpgs_4.tab
  crrefer$grid/bpgs/bpgs_9.tab
  crrefer$grid/bpgs/bpgs_13.tab
  crrefer$grid/bpgs/bpgs_20.tab
  </pre></div>
  <p>
  The resulting fit will be saved in fitgrid.tab.
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; fitgrid crcalspec$eta_uma_002.tab @grid.lis out=fitgrid.tab
  
  Final solution:
  0.6101387 * 0.1324818 * (crrefer$grid/bpgs/bpgs_9.tab) + (1. -
  0.6101387) * 0.4985421 * (crrefer$grid/bpgs/bpgs_13.tab)
  </pre></div>
  <p>
  2. Fit a black body to the spectrum of Eta Ursa Majoris instead:
  </p>
  <p>
  sy&gt; fitgrid crcalspec$eta_uma_002.tab <span style="font-family: monospace;">"bb($0)"</span> out=fitgrid.tab \      
  &gt;&gt;&gt; vz=10e3-30e3x1e3
  </p>
  <p>
  Final solution:
  0.6134695 * 4711.343 * (bb(19000.)) + (1. - 0.6134695) * 
  3840.553 * (bb(20000.))
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by B.Simon based on XCAL code written by Keith Horne.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  calcspec, fitspec
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

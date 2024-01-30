.. _eqwidth:

eqwidth: Compute equivalent widths for specified lines in spectra
=================================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  eqwidth input output bands
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Input list of spectra to be measured.  These may be one dimensional
  spectra in individual or <span style="font-family: monospace;">"multispec"</span> format or calibrated spatial spectra such
  as long slit or Fabry-Perot images.  The dispersion axis and summing
  parameters are specified by package parameters for the spatial spectra.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output file for the results.  This may be a filename or <span style="font-family: monospace;">"STDOUT"</span> to
  write to the terminal.
  </dd>
  </dl>
  <dl id="l_bands">
  <dt><b>bands</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bands' Line='bands' -->
  <dd>Bandpass file consisting of lines with one, two, or three bandpasses per
  line.  A bandpass is specified by an identification string (quoted if it is
  null or contains whitespace), the central wavelength, the width of the
  bandpass in wavelength, and a filter filename with the special value <span style="font-family: monospace;">"none"</span>
  if there is no filter (a flat unit response).    This format is described
  further in the description section.
  </dd>
  </dl>
  <dl id="l_banddir">
  <dt><b>banddir = <span style="font-family: monospace;">"rvsao$lib/"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='banddir' Line='banddir = "rvsao$lib/"' -->
  <dd>Bandpass directory
  </dd>
  </dl>
  <dl id="l_specnum">
  <dt><b>specnum = <span style="font-family: monospace;">"1"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specnum' Line='specnum = "1"' -->
  <dd>List of apertures to select from the input spectra.  For one dimensional
  spectra this is the aperture number and for spatial spectra it is
  the column or line.  If the null string is specified all apertures are
  selected.  The aperture list syntax is a range list which includes
  intervals and steps (see <b>ranges</b>).
  </dd>
  </dl>
  <dl id="l_specband">
  <dt><b>specband = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specband' Line='specband = 0' -->
  <dd>Spectrum band to use if input is an IRAF multispec spectrum
  </dd>
  </dl>
  <dl id="l_skyband">
  <dt><b>skyband = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skyband' Line='skyband = 0' -->
  <dd>Spectrum band containing sky spectrum removed from object if this is
  and IRAF multispec spectrum.  This is used to compute the error.
  </dd>
  </dl>
  <dl id="l_bandfilt">
  <dt><b>bandfilt = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bandfilt' Line='bandfilt = no' -->
  <dd>Filter names follow wavelength limits in bandpass file if yes
  </dd>
  </dl>
  <dl id="l_bandcont">
  <dt><b>bandcont = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bandcont' Line='bandcont = no' -->
  <dd>Continuum names precede wavelength limits in bandpass file if yes
  </dd>
  </dl>
  <dl id="l_bindim">
  <dt><b>bindim = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bindim' Line='bindim = 0' -->
  <dd>Number of rows in unbinned (bin by one) spectrum.  Bin by 4 if less than
  half this; bin by 2 if less than this; else bin by 1.
  </dd>
  </dl>
  <dl id="l_normalize">
  <dt><b>normalize = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='normalize' Line='normalize = yes' -->
  <dd>Normalize the bandpass fluxes by the bandpass response?  If no then
  the results will depend on the bandpass widths and filter function
  values.  If yes then fluxes will be comparable to an average pixel
  value.  When computing indices and equivalent widths the flux must
  either be normalized or the bandpasses and filter response functions
  must be the same.
  </dd>
  </dl>
  <dl id="l_fitcont">
  <dt><b>fitcont = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitcont' Line='fitcont = no' -->
  <dd>Fit continuum instead of computing at specific points (yes or no)
  </dd>
  </dl>
  <dl id="l_netflux">
  <dt><b>netflux = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='netflux' Line='netflux = no' -->
  <dd>Compute the net flux from the emission region instead of equivalent
  width by subtracting the mean continuum per pixel times the number
  of pixels in the region if yes.
  </dd>
  </dl>
  <dl id="l_byexp">
  <dt><b>byexp = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='byexp' Line='byexp = no' -->
  <dd>Convert to counts per second (exposure normalization) if yes
  </dd>
  </dl>
  <dl id="l_bypix">
  <dt><b>bypix = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bypix' Line='bypix = no' -->
  <dd>Convert to counts per row (spatial normalization) if yes
  </dd>
  </dl>
  <dl id="l_torest">
  <dt><b>torest = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='torest' Line='torest = no' -->
  <dd>Shift spectrum from observed velocity to zero velocity if yes.  Set no
  for night sky lines.  Set to yes to remove redshift from observed object
  spectra before computing equivalent widths
  </dd>
  </dl>
  <dl id="l_mag">
  <dt><b>mag = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mag' Line='mag = no' -->
  <dd>Output the bandpass fluxes as magnitudes with the magnitude zero point
  specified by <i>magzero</i> if yes
  </dd>
  </dl>
  <dl id="l_magzero">
  <dt><b>magzero = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='magzero' Line='magzero = 0.' -->
  <dd>Magnitude zero point used if <i>mag</i> = yes
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "stdgraph"' -->
  <dd>Display device
  </dd>
  </dl>
  <dl id="l_plot_obj">
  <dt><b>plot_obj = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plot_obj' Line='plot_obj = no' -->
  <dd>Plot the raw object data
  </dd>
  </dl>
  <dl id="l_int_obj">
  <dt><b>int_obj = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='int_obj' Line='int_obj = no' -->
  <dd>Interact with plot of raw object data
  </dd>
  </dl>
  <dl id="l_plot_fitcont">
  <dt><b>plot_fitcont = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plot_fitcont' Line='plot_fitcont = no' -->
  <dd>Plot the continuum fit to the data
  </dd>
  </dl>
  <dl id="l_plot_contsub">
  <dt><b>plot_contsub = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plot_contsub' Line='plot_contsub = no' -->
  <dd>Plot the continuum-subtracted data
  </dd>
  </dl>
  <dl id="l_int_contsub">
  <dt><b>int_contsub = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='int_contsub' Line='int_contsub = no' -->
  <dd>Interact with plot of continuum-subtracted data
  </dd>
  </dl>
  <dl id="l_nsmooth">
  <dt><b>nsmooth = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsmooth' Line='nsmooth = 0' -->
  <dd>Number of times to 1-2-1 smooth plotted spectra
  </dd>
  </dl>
  <dl id="l_report_mode">
  <dt><b>report_mode = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='report_mode' Line='report_mode = 1' -->
  <dd>Mode for output:
  Each line starts with the file name, followed by this information for each line:
  1: line name, line flux, continuum name, continuum flux, index, equivalent width
  2: line flux, continuum flux, index, index error (line names in column heading)
  3: line flux, equivalent width, equivalent width error (line names in column heading)
  4: index, index error (line names in column heading)
  5: equivalent width, equivalent width error (line names in column heading)
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = 1' -->
  <dd>Number of pixels to sum across dispersion
  </dd>
  </dl>
  <dl id="l_hardcopy">
  <dt><b>hardcopy = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hardcopy' Line='hardcopy = no' -->
  <dd>Automatic hardcopy of results (yes or no)
  </dd>
  </dl>
  <dl id="l_plotter">
  <dt><b>plotter = <span style="font-family: monospace;">"stdplot"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plotter' Line='plotter = "stdplot"' -->
  <dd>Hardcopy output device
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Include a verbose header giving a banner, the parameters used,
  the bandpasses, and column headings?
  </dd>
  </dl>
  <dl id="l_debug">
  <dt><b>debug = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='debug' Line='debug = no' -->
  <dd>Print debugging info?
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>eqwidth</b> performs bandpass spectrophotometry with one or more bandpasses
  on one or more spectra.  A list of input spectra is specified.  The spectra
  may be of any type acceptible in the <b>noao.onedspec</b> package including
  multispec format with nonlinear dispersion, long slit spectra, and even
  3D cubes with one dispersion axis.  The <i>apertures</i> parameter allows
  selecting a subset of the spectra by aperture number.
  </p>
  <p>
  The bandpasses are specified in a text file.  A bandpass consists of four
  fields; an identification name, the wavelength of the bandpass center, a
  bandpass width, and an optional filename for a filter.  The identification is a
  string which must be quoted if a null name or a name with whitespace is
  desired.  The identification could be given as the central wavelength if
  nothing else is appropriate.  The filter field is a filename for a text
  file containing the filter values.  A filter file consists of a wavelength
  ordered list of wavelength and relative response.  Extrapolation uses the
  end point values and interpolation is linear.  The special name <span style="font-family: monospace;">"none"</span> is
  used if there is no filter, though if the parameter <i>bandfilt</i> is set to
  no, this column can be omitted entirely.  Both of these options are equivalent
  to unit response at all wavelengths.
  </p>
  <p>
  In the bandpass file there may be one, two, or three bandpasses on
  a line.  Below are some examples of the three cases:
  </p>
  <div class="highlight-default-notranslate"><pre>
  alpha 5000 10 myalpha.dat
  beta1 4000 100 none       beta2 4100 100 none
  line  4500 100 none       red   4000 200 none blue 5000 200 none
  </pre></div>
  <p>
  The flux in each bandpass is measured by summing each pixel in the interval
  multiplied by the interpolated filter response at that pixel.  At the edges
  of the bandpass the fraction of the pixel in the bandpass is used.  If the
  bandpass goes outside the range of the data an INDEF value will be reported.
  If the <i>normalize</i> option is yes then the total flux is divided by
  the sum of the filter response values.  If the <i>mag</i> option is
  yes the flux will be converted to a magnitude (provided it is positive)
  using the formula
  </p>
  <div class="highlight-default-notranslate"><pre>
  magnitude = magzero - 2.5 * log10 (flux)
  </pre></div>
  <p>
  where <i>magzero</i> is a parameter for the zero point magnitude and log10
  is the base 10 logarithm.  Note that there is no attempt to deal with the
  pixel flux units.  This is the responsiblity of the user.
  </p>
  <p>
  If there is only one bandpass (on one line of the band file) then only
  the band flux or magnitude is reported.  If there are two bandpasses
  the fluxes or magnitudes for the two bands are reported as well as a
  band index, the flux ratio or magnitude difference (depending on the <i>mag</i>)
  flag, and an equivalent width using the second band as the continuum.
  If there are three bandpasses then a continuum bandpass flux is computed
  as the interpolation between the bandpass centers to the center of the
  first bandpass.  The special bandpass identification <span style="font-family: monospace;">"cont"</span> will
  be reported.
  </p>
  <p>
  The equivalent width is obtained from the two bandpasses by the
  formala
  </p>
  <div class="highlight-default-notranslate"><pre>
  eq. width = (1 - flux1 / flux2) * width1
  </pre></div>
  <p>
  where flux1 and flux2 are the two bandpass fluxes and width1 is the
  width of the first bandpass.  Note that for this to be meaningful
  the bandpasses should be normalized or have the same width/response.
  </p>
  <p>
  The results of measuring each bandpass in each spectrum are written
  to the specified output file.  This file may be given as <span style="font-family: monospace;">"STDOUT"</span> to
  write the results to the terminal.  The output file contains lines
  with the spectrum name and aperture, the band identifications and
  fluxes or magnitudes, and the band index and equivalent width (if
  appropriate).  The <i>verbose</i> option allows creating a more
  documented output by including a commented header with the task
  name and parameters, the bandpass definitions, and column labels.
  The examples below show the form of the output.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following examples use artificial data and arbitrary bands.
  </p>
  <p>
  1.  Show example results with one, two, and three bandpass entries in
  the bandpass file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type bands
  test 6125 50 none red 6025 100 none blue 6225 100 none
  test 6125 50 none red 6025 100 none
  test 6125 50 none blue 6225 100 none
  test 6125 50 none
  cl&gt; eqwidth oned STDOUT bands
  
  # EQWIDTH: NOAO/IRAF IRAFX valdes@puppis Mon 15:31:45 01-Nov-93
  #   bands = bands, norm = yes, mag = no
  #       band     filter wavelength      width
  #       test       none      6125.        50.
  #        red       none      6025.       100.
  #       blue       none      6225.       100.
  #       test       none      6125.        50.
  #        red       none      6025.       100.
  #       test       none      6125.        50.
  #       blue       none      6225.       100.
  #       test       none      6125.        50.
  #
  #       spectrum    band    flux    band    flux   index eqwidth
           oned(1)    test   44.33    cont   97.97    0.45   27.37
           oned(1)    test   44.33     red   95.89    0.46   26.89
           oned(1)    test   44.33    blue  100.04    0.44   27.84
           oned(1)    test   44.33
  </pre></div>
  <p>
  2.  This example shows measurments on a long slit spectrum with an
  aperture selection and magnitude output.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type leqwidth.dat
  band1 4500 40 none
  band2 4600 40 none
  band3 4700 40 none
  cl&gt; nsum=5
  cl&gt; eqwidth ls STDOUT leqwidth.dat apertures=40-60x5 mag+ magzero=10.1
  
  # EQWIDTH: NOAO/IRAF IRAFX valdes@puppis Mon 15:37:18 01-Nov-93
  #   bands = leqwidth.dat, norm = yes, mag = yes, magzero = 10.10
  #       band     filter wavelength      width
  #      band1       none      4500.        40.
  #      band2       none      4600.        40.
  #      band3       none      4700.        40.
  #
  #       spectrum    band     mag
   ls[38:42,*](40)   band1    3.14
   ls[38:42,*](40)   band2    3.19
   ls[38:42,*](40)   band3    3.15
   ls[43:47,*](45)   band1    3.13
   ls[43:47,*](45)   band2    3.15
   ls[43:47,*](45)   band3    3.14
   ls[48:52,*](50)   band1    2.34
   ls[48:52,*](50)   band2    2.43
   ls[48:52,*](50)   band3    2.43
   ls[53:57,*](55)   band1    3.10
   ls[53:57,*](55)   band2    3.15
   ls[53:57,*](55)   band3    3.12
   ls[58:62,*](60)   band1    3.14
   ls[58:62,*](60)   band2    3.19
   ls[58:62,*](60)   band3    3.15
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_EQWIDTH">
  <dt><b>EQWIDTH V2.3.0</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='EQWIDTH' Line='EQWIDTH V2.3.0' -->
  <dd>New in this release, almost all code is from noao.onedspec.sbands
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  splot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

.. _ndprep:

ndprep: Make neutral density filter calibration image
=====================================================

**Package: xonedspec**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ndprep filter_curve output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_filter_curve">
  <dt><b>filter_curve</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filter_curve' Line='filter_curve' -->
  <dd>Neutral density filter curve.  The directory specified by the parameter
  <i>directory</i> is prepended to this name so if a directory is specified
  then it should not be given here.  If <span style="font-family: monospace;">'?'</span> a list of filter curves
  in the specified directory is typed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output neutral density filter image.
  </dd>
  </dl>
  <dl id="l_w0">
  <dt><b>w0   </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='w0' Line='w0   ' -->
  <dd>Starting wavelength for the output image in Angstroms.
  </dd>
  </dl>
  <dl id="l_dw">
  <dt><b>dw   </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dw' Line='dw   ' -->
  <dd>Wavelength increment for the output image in Angstroms.
  </dd>
  </dl>
  <dl id="l_nw">
  <dt><b>nw   </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nw' Line='nw   ' -->
  <dd>Number of wavelength points for the output image (i.e. the size of the
  output image).
  </dd>
  </dl>
  <dl id="l_nspace">
  <dt><b>nspace = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nspace' Line='nspace = 0' -->
  <dd>Number of spatial points for a two dimensional image.  If the value is
  zero then a one dimensional image is created.
  </dd>
  </dl>
  <dl id="l_logarithm">
  <dt><b>logarithm = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logarithm' Line='logarithm = no' -->
  <dd>Use logarithmic wavelengths and intervals?  If yes then the wavelengths
  will have the same starting and ending points and number of pixels but
  the wavelength intervals will be logarithmic.
  </dd>
  </dl>
  <dl id="l_flux">
  <dt><b>flux = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flux' Line='flux = yes' -->
  <dd>Conserve flux when rebinning to logarithmic wavelength intervals?
  </dd>
  </dl>
  <dl id="l_dispaxis">
  <dt><b>dispaxis = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispaxis' Line='dispaxis = 1' -->
  <dd>Dispersion axis for two dimensional images.  Dispersion along the lines
  is 1 and dispersion along the columns is 2.
  </dd>
  </dl>
  <dl id="l_directory">
  <dt><b>directory = <span style="font-family: monospace;">"onedstds$ctio/"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='directory' Line='directory = "onedstds$ctio/"' -->
  <dd>Directory containing neutral density filter curves.  This directory is
  prepended to the specified fiter curve file (and so must end with <span style="font-family: monospace;">'/'</span>
  or <span style="font-family: monospace;">'$'</span>).
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A neutral density (ND) filter curve is converted to a calibration image
  with the same size and wavelength range as the images to be calibrated.
  A list of standard neutral density curves is typed if the filter
  curve name is given as <span style="font-family: monospace;">'?'</span>.  The ND curves are text files containing
  wavelength and filter transmission pairs.  Comments begin with <span style="font-family: monospace;">'#'</span>.
  A plot of the ND curve can be obtained using <b>graph</b>.
  </p>
  <p>
  The ND curve is first interpolated to a one dimensional image of
  <i>nw</i> wavelength points with starting wavelength <i>wO</i> and
  wavelength increment <i>dw</i> using the task <b>sinterp</b>.  The
  wavelength parameters must be in the same units as the filter curves
  (currently Angstroms) even if the final calibration image is to be in
  logarithmic wavelength intervals.  If logarithmic wavelength format
  is specified the image is rebinned over the same wavelength range with
  the same number of points using the task <b>dispcor</b>.  The rebinning
  may include flux conservation to account for the changing size of
  pixels or simply interpolate.  Note that flux conservation will
  change the apparent shape of the ND curve.
  </p>
  <p>
  If the number of points across the dispersion, <i>nspace</i> is zero then
  the final calibration image is one dimensional.  If it is greater than
  zero the one dimensional ND image is expanded to the specified number
  of spatial points with the dispersion axis specified by the parameter
  <i>dispaxis</i> (1 = dispersion along the lines, 2 = dispersion along
  the columns).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To get a list of standard ND filter curves:
  </p>
  <p>
  	cl&gt; ndprep ?
  </p>
  <p>
  To graph the ND filter curve:
  </p>
  <p>
  	cl&gt; graph onedstds$ctio/nd1m.100mag.dat
  </p>
  <p>
  Naturally, if a calibration image is made then the image plotting tasks
  such as <b>graph</b>, <b>implot</b>, and <b>splot</b> may also be used.
  </p>
  <p>
  To make a one dimensional ND calibration spectrum:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ndprep w0=4000 dw=1.2 nw=512
  Input ND filter curve:  onedstds$ctio/nd1m.100mag.dat
  Output calibration image: NDimage
  </pre></div>
  <p>
  To make a two dimensional ND calibration spectrum in logarithmic wavelength:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ndprep w0=4000 dw=1.2 nw=512 nspace=200 log+
  Input ND filter curve:  onedstds$ctio/nd4m.u000mag.dat
  Output calibration image: NDimage
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_NDPREP">
  <dt><b>NDPREP V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='NDPREP' Line='NDPREP V2.10' -->
  <dd>This task was moved from the <b>proto</b> package.  It was originally
  written at CTIO for CTIO data.  It's functionality is largely unchanged
  though it has been updated for changes in the <b>onedspec</b> package.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  sinterp, dispcor
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

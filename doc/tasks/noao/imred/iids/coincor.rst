.. _coincor:

coincor: Correct spectra for detector count rates
=================================================

**Package: iids**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  coincor input records
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The root file name of the input spectra.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records' -->
  <dd>The range of spectra.
  The names of the spectra will be formed by appending the range
  elements to the input root name.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>This is the root file name for the corrected spectra.  If no root name
  is specified (specified with the null string <span style="font-family: monospace;">""</span>) then the operation
  is done in place.
  </dd>
  </dl>
  <dl id="l_start_rec">
  <dt><b>start_rec = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='start_rec' Line='start_rec = 1' -->
  <dd>The starting record number to be appended to the root name of the
  created spectra.
  </dd>
  </dl>
  <dl id="l_ccmode">
  <dt><b>ccmode = )_.ccmode</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ccmode' Line='ccmode = )_.ccmode' -->
  <dd>The mode used to model the detector count rate corrections.
  In the following C(obs) is the observed count rate and C(cor) is the
  corrected count rate.
  <dl>
  <dt><b><span style="font-family: monospace;">"photo"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"photo"' -->
  <dd>Photoelectric photometer with discriminator mode.  The count rate
  correction is
      C(cor) = C(obs) * exp (C(obs) * deadtime)
      
  where the parameter <i>deadtime</i> is the representative deadtime in seconds.
  </dd>
  </dl>
  <dl>
  <dt><b><span style="font-family: monospace;">"iids"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='"iids"' -->
  <dd>IIDS correction given by
      C(cor) = (-ln(1-C(obs)*deadtime)/deadtime)**power
  where <b>deadtime</b> is a parameter related to the sweep time used to
  correct for coincidence losses and <b>power</b> is a power law coefficient.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_deadtime">
  <dt><b>deadtime = )_.deadtime</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='deadtime' Line='deadtime = )_.deadtime' -->
  <dd>For the <span style="font-family: monospace;">"photo"</span> mode this parameter is the period, in seconds, during
  which no counts can be registered by the detector.  Note that this is
  based on a per pixel basis.  So if the discriminator dead period is of
  order 50 nanoseconds and 2000 pixels are observed per readout, the
  effective deadtime is about 10E-4 seconds.  For the <span style="font-family: monospace;">"iids"</span> mode this
  parameter defines the sweep time correction and has a value of 1.424E-3
  seconds.
  </dd>
  </dl>
  <dl id="l_power">
  <dt><b>power = )_.power</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='power' Line='power = )_.power' -->
  <dd>The IIDS power law coefficient.  The standard value is 0.975.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The input spectra are corrected for detector count rate errors.  If no
  output root name is given then the operation is done in place.  The type
  of correction is specified by the parameter <i>ccmode</i>.  The available
  modes are for a general photomultiplier with discriminator coincidence
  correction, and the NOAO IIDS.  The parameters for these modes are
  <i>deadtime</i> and <i>power</i>.  The exposure time, in seconds, is a
  required image header parameter (keyword = EXPOSURE).
  </p>
  <p>
  The default mode is for the NOAO IIDS.  The IIDS correction includes a
  power law correction for a nonlinear effect in the IIDS image tube chain
  which is not included by the mountain reduction software at the telescope.
  If the spectra have been coincidence corrected at the telescope
  then only the nonlinear power law correction is applied.
  </p>
  <p>
  The coincidence correction flag may take the values -1 for no correction,
  0 for the IIDS correction with <i>power</i> = 1 (the correction
  applied by the mountain reduction software), 1 for the full IIDS
  correction, and 2 for the photomuliplier mode correction.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following example corrects a series of IIDS spectra:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; coincor nite1 1-250 output=nite1cc start_rec=1
  </pre></div>
  <p>
  The following example corrects a series of spectra from the
  Lick ITS:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; coincor its 1-250 output=itscc start=1 ccmode=photo \
  &gt;&gt;&gt; deadtime=2.4E-4 power=1
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  <b>Coincor</b> requires approximately 1 second per spectrum of length 1024.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <div class="highlight-default-notranslate"><pre>
  The <b>imred.iids</b> package is designed for reducing NOAO IIDS spectra.
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'SEE ALSO'  -->
  

.. _powercor:

powercor: Apply power law correction to mountain reduced spectra
================================================================

**Package: iids**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  powercor input records
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
  <dd>This is the root file name for the corrected spectra.
  </dd>
  </dl>
  <dl id="l_start_rec">
  <dt><b>start_rec = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='start_rec' Line='start_rec = 1' -->
  <dd>The starting record number to be appended to the root name of the
  created spectra.
  </dd>
  </dl>
  <dl id="l_power">
  <dt><b>power = )iids.power</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='power' Line='power = )iids.power' -->
  <dd>The power law coefficient.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A power law correction to the IIDS count rates is applied to the input
  spectra.  The mountain reduction software applies a coincidence correction
  to the observed IIDS count rates but does not correct for a nonlinear effect
  in the image tube chain.  This second correction takes the form of a
  power law
  </p>
  <p>
  	C(out) = C(in) ** power
  </p>
  <p>
  where C(in) is the input, coincidence corrected, count rate and C(out)
  is the corrected count rate.  The power is a parameter of the task
  which defaults to the <b>iids</b> package parameter set to the appropriate
  value for the IIDS.  The exposure time, in seconds, is a required
  image header parameter (keyword = EXPOSURE) used to convert the
  total counts to count rates.
  </p>
  <p>
  Note that if the original raw spectra are being reduced then the either
  <b>coincor</b> or <b>powercor</b> may be used to apply both the coincidence
  correction and the power law correction at the same time.  In other words,
  the tasks apply the coincidence correction if the coincidence flag (CO-FLAG) is
  -1 (uncorrected) and the power law correction alone if the flag is zero
  (coincidence corrected only).  The flag is 1 when both the coincidence and
  nonlinear correction have been applied.
  </p>
  <p>
  This task is a script calling <b>coincor</b> with <i>ccmode</i> = <span style="font-family: monospace;">"iids"</span>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following example corrects a series of IIDS spectra:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; powercor nite1 1-250 output=nite1cc start_rec=1
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  coincor
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

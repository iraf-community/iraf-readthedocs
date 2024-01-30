.. _zvel:

zvel: Run emsao and xcsao on list of spectra
============================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  zvel spectra
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_imagelist">
  <dt><b>imagelist = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imagelist' Line='imagelist = ""' -->
  <dd>List of file names of spectra to analyze.
  @&lt;filename&gt; indicates list should come from file &lt;filename&gt;.
  &lt;filename&gt;[&lt;range&gt;] indicates that a range of apertures in a multispec
  file should be processed, where &lt;range&gt; is a comma- and/or
  hyphen-separated list of numbers.
  </dd>
  </dl>
  <dl id="l_imagext">
  <dt><b>imagext=<span style="font-family: monospace;">".imh"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imagext' Line='imagext=".imh"' -->
  <dd>Image header file name extension
  </dd>
  </dl>
  <dl id="l_emis_vel">
  <dt><b>emis_vel=yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='emis_vel' Line='emis_vel=yes' -->
  <dd>Compute emission line velocities (yes or no)
  </dd>
  </dl>
  <dl id="l_corr_vel">
  <dt><b>corr_vel=yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='corr_vel' Line='corr_vel=yes' -->
  <dd>Compute cross correlation velocities (yes or no)
  </dd>
  </dl>
  <dl id="l_plot">
  <dt><b>plot=yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='plot' Line='plot=yes' -->
  <dd>Plot results on display (yes or no)
  </dd>
  </dl>
  <dl id="l_hard_copy">
  <dt><b>hard_copy=no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hard_copy' Line='hard_copy=no' -->
  <dd>Make printer hard copies (yes or no)
  </dd>
  </dl>
  <dl id="l_curmode">
  <dt><b>curmode = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='curmode' Line='curmode = no' -->
  <dd>If yes, wait in cursor mode after each spectrum is processed.  Cursor
  mode commands may be listed by typing <span style="font-family: monospace;">"?"</span>.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>If yes, values of the parameters fit to the selected peak
  are recorded in the log files.  This is most useful for debugging.
  </dd>
  </dl>
  <p>
   
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  ZVEL runs either XCSAO or EMSAO or both, so the user doesn't have to
  type a file name in twice.  Set parameters in XCSAO, EMSAO, and CONTPARS.
  curmode, hard_copy, plot, and verbose override the equivalent parameters
  in XCSAO and EMSAO.  If both XCSAO and EMSAO are being run, the image
  files should be writeable so the cross-correlation velocity can be saved
  to be used as an initial guess at the emission line velocity.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To obtain the redshift and dispersion of a single galaxy
  </p>
  <p>
          cl&gt; zvel galaxy
  </p>
  <p>
  To obtain redshifts for a whole night's worth of galaxy spectra:
  </p>
  <p>
          cl&gt; zvel @nite1.ls
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS'  -->
  

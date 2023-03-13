.. _mkms:

mkms: Create multispec from 1D spectra including associated bands
=================================================================

**Package: nproto**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkms output spectra raw background sigma
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Name of output multispec image.
  </dd>
  </dl>
  <dl id="l_spectra">
  <dt><b>spectra</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectra' Line='spectra' -->
  <dd>List of primary 1D spectra to be included in multispec image.
  </dd>
  </dl>
  <dl id="l_raw">
  <dt><b>raw</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='raw' Line='raw' -->
  <dd>List of 1D raw or secondary spectra.  If none specify <span style="font-family: monospace;">""</span> otherwise
  the list must match the list of primary spectra.
  </dd>
  </dl>
  <dl id="l_background">
  <dt><b>background</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='background' Line='background' -->
  <dd>List of 1D background spectra.  If none specify <span style="font-family: monospace;">""</span> otherwise
  the list must match the list of primary spectra.
  </dd>
  </dl>
  <dl id="l_sigma">
  <dt><b>sigma</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sigma' Line='sigma' -->
  <dd>List of 1D sigma spectra.  If none specify <span style="font-family: monospace;">""</span> otherwise
  the list must match the list of primary spectra.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MKMS creates a multispec format from 1D spectra.  Unlike SCOPY it
  can include associated spectra.  There can be any number of primary 1D
  spectra and the associated spectra are optional.  However, when
  associated spectra are specified the list must match the primary spectra
  list and the arrays must have the same number of pixels and dispersion
  as the primary spectrum.  The different spectra may have different
  dispersions.
  </p>
  <p>
  This is a simple script using SCOPY and IMSTACK.  It has minimal error
  checking.  In particular, if the set of input is not consistent the
  task will abort with an error leaving temporary files behind.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To create an image with one spectrum and each of the associated types:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkms out.ms spec rawspec bkgspec sigspec
  </pre></div>
  <p>
  2. To create an image with three primary spectra and error arrays:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkms out.ms spec1,spec2,spec3 "" "" err1,err2,err3
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MKMS">
  <dt><b>MKMS V2.12.2</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MKMS' Line='MKMS V2.12.2' -->
  <dd>This prototype task added for this release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  scopy, imstack
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

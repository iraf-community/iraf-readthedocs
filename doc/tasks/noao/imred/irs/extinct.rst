.. _extinct:

extinct: Use BSWITCH for extinction correction
==============================================

**Package: irs**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  extinct root records output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_root">
  <dt><b>root</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='root' Line='root' -->
  <dd>The root name for the input spectra to be corrected.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records' -->
  <dd>The range of spectra to be included in the extinction operation.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The root name for the output corrected spectra
  </dd>
  </dl>
  <dl id="l_start_rec">
  <dt><b>start_rec</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='start_rec' Line='start_rec' -->
  <dd>The starting record number for the output corrected spectra.
  </dd>
  </dl>
  <dl id="l_nr_aps">
  <dt><b>nr_aps = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nr_aps' Line='nr_aps = 2' -->
  <dd>The number of instrument apertures for this data set.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The input spectra are corrected for atmospheric extinction. 
  EXTINCT redirects the spectra through the task BSWITCH so all
  procedures are identical to those described for that task.
  </p>
  <p>
  Because BSWITCH attempts to perform a beam-switch operation
  unless the subset parameter is equal to the number of
  instrument apertures (in which case beam-switching degenerates
  to a copy operation), the hidden parameter nr_aps should be set
  appropriately to the instrument. For IIDS and IRS data, this
  is 2.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; extinct  nite1 1001-1032 nite1ex
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The input string of spectra must be ordered so that only
  one spectrum from each aperture is present among substrings
  of length nr_aps.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  bswitch
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

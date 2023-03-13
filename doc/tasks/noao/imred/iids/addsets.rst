.. _addsets:

addsets: Add subsets of strings of spectra
==========================================

**Package: iids**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  addsets input records
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The root file name for the input spectra in the string.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records' -->
  <dd>The range of spectra indicating the elements of the string.
  The names of the spectra will be formed by appending the range
  elements to the input root name.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>This is the root file name for the names of the spectra which will
  be created by the addset operation.
  </dd>
  </dl>
  <dl id="l_start_rec">
  <dt><b>start_rec = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='start_rec' Line='start_rec = 1' -->
  <dd>The starting record number to be appended to the root name of the
  created spectra.
  </dd>
  </dl>
  <dl id="l_subset">
  <dt><b>subset = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subset' Line='subset = 2' -->
  <dd>The length of the substring of spectra which will be added together.
  For IIDS/IRS data which has been processed through BSWITCH, this
  parameter should be 2. This implies that spectra will be taken 
  2 at a time, added, and the sum written as a new spectrum.
  </dd>
  </dl>
  <dl id="l_weighting">
  <dt><b>weighting = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='weighting' Line='weighting = yes' -->
  <dd>If set to yes, an average of the substring of spectra is generated
  (if flux calibrated) weighted by the integration times of the
  individual spectra. If set to no, a simple average is generated.
  If not flux calibrated, this parameter has no effect - a simple
  sum is generated.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Every <span style="font-family: monospace;">"subset"</span> group of spectra will be accumulated and the sum will be
  written as a new spectrum. For example, if the input string contains
  100 spectra, and subset=2, then 50 new spectra will be created. Each
  new spectrum will be the sum of the consecutive pairs in the original string.
  </p>
  <p>
  If there are insufficient spectra to complete a subset accumulation,
  the sum is written out anyway and a warning printed. For example,
  if the input string contains 23 spectra, and subset=4, there will be
  6 new spectra created, but the last one will be based on only 3 spectra.
  </p>
  <p>
  Subset may be set to 1 to allow a copy operation although this is not
  a very efficient way to do so.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following three examples are those described above.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; addsets nite1 2001-2100
  cl&gt; addsets nite1 2001-2023 subset=4
  cl&gt; addsets nite1 2001-2010 subset=1 output=nite2 \
  &gt;&gt;&gt; start_rec=2001
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  bswitch
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

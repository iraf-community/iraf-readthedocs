.. _subsets:

subsets: Subtract pairs in strings of spectra
=============================================

**Package: irs**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  subsets input records
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
  be created by the subtraction operation.
  </dd>
  </dl>
  <dl id="l_start_rec">
  <dt><b>start_rec</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='start_rec' Line='start_rec' -->
  <dd>The starting record number to be appended to the root name of the
  created spectra.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Pairs of spectra are formed from the input string in the order that
  the record numbers would suggest. 
  The first spectrum in the pair is assumed to be the
  principle spectrum and the second spectrum in the pair is subtracted
  from the first. The result is written out as a new spectrum.
  </p>
  <p>
  No compensation is made for exposure time during the subtraction.
  The header from the principle spectrum is assigned to the output
  spectrum.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following example forms 50 new spectra from nite1.2001-nite1.2002,
  nite1.2003-nite1.2004, ...
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; subsets nite1 2001-2100
  </pre></div>
  <p>
  The following example creates new spectra from the pairs nite2.2001-nite2.2002,
  nite2.2003-nite2.2004 in spite of the order of the record numbers entered.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; subsets nite2 2001,2003,2002,2004
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES'  -->
  

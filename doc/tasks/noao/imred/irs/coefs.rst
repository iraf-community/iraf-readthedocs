.. _coefs:

coefs: Extract mtn reduced coefficients from henear scans
=========================================================

**Package: irs**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  coefs input records database
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The input image root name for the spectral images containing the
  dispersion coefficients.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records' -->
  <dd>The range of records for which the root name applies.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>The database file name which will contain the coefficients.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The spectra specified by the combination of the root name
  and the records are scanned for the presence of dispersion
  coefficients. If present, the coefficients and necessary
  information are written to the file indicated by the database
  parameter. This file an then be used by the linearization
  program DISPCOR to correct any spectra for which the
  database is appropriate.
  </p>
  <p>
  Each invocation of COEFS appends to the database file, or
  creates a new file if necessary.
  </p>
  <p>
  The following assumptions are made concerning the coefficients,
  which are always correct for IIDS and IRS mountain reduced
  data at Kitt Peak.
  </p>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(1)' -->
  <dd>The coefficients represent Legendre polynomials.
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(2)' -->
  <dd>The coefficients apply to pixels 1 through 1024 in the original data.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following example reads the coefficients from the headers
  for nite1 arc spectra taken near the beginning and end of the
  night and creates a database file called nite1.db:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; coefs nite1 3-4,201-202 nite1.db
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  Approximately 1 second per spectrum is required. This is primarily
  overhead due to file access.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  dispcor, identify
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'SEE ALSO'  -->
  

.. _deredden:

deredden: Apply interstellar extinction corrections
===================================================

**Package: kpnocoude**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  deredden input output [records] value
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input spectra to be dereddened.  When using record
  format extensions the root names are specified, otherwise full
  image names are used.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of derreddened spectra.  If no output list is specified then
  the input spectra are modified.  Also the output name may be
  the same as the input name to replace the input spectra by the
  calibrated spectra.  When using record format extensions the
  output names consist of root names to which the appropriate
  record number extension is added.  The record number extension
  will be the same as the input record number extension.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records (imred.irs and imred.iids only)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records (imred.irs and imred.iids only)' -->
  <dd>The set of record number extensions to be applied to each input
  and output root name when using record number extension 
  format.  The syntax consists of comma separated numbers or
  ranges of numbers.  A range consists of two numbers separated
  by a hyphen.  This parameter is not queried when record number
  formats are not used.
  </dd>
  </dl>
  <dl id="l_value">
  <dt><b>value</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='value' Line='value' -->
  <dd>Extinction parameter value as selected by the type parameter.
  This value may be a visual extinction, A(V), the color excess between
  B and V, E(B-V), or the logarithmic H beta extinction.
  These quantities are discussed further below.
  </dd>
  </dl>
  <dl id="l_R">
  <dt><b>R = 3.1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='R' Line='R = 3.1' -->
  <dd>The ratio of extinction at V, A(V), to color excess between B and V, E(B-V).
  </dd>
  </dl>
  <dl id="l_type">
  <dt><b>type = <span style="font-family: monospace;">"E(B-V)"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='type' Line='type = "E(B-V)"' -->
  <dd>The type of extinction parameter used.  The values may be:
  <dl>
  <dt><b>A(V)</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='A' Line='A(V)' -->
  <dd>The absolute extinction at the V band at 5550 Angstroms.
  </dd>
  </dl>
  <dl>
  <dt><b>E(B-V)</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='E' Line='E(B-V)' -->
  <dd>The color excess between the B and V bands.
  </dd>
  </dl>
  <dl>
  <dt><b>c     </b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='c' Line='c     ' -->
  <dd>The logarithmic H beta extinction.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>List of apertures to be selected from input one dimensional spectra
  to be calibrated.  If no list is specified then all apertures are
  corrected.  The syntax is the same as the record number
  extensions.  This parameter is ignored for N-dimensional spatial
  spectra such as calibrated long slit and Fabry-Perot data.
  </dd>
  </dl>
  <dl id="l_override">
  <dt><b>override = no, uncorrect = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='override' Line='override = no, uncorrect = yes' -->
  <dd>If a spectrum has been previously corrected it will contain the header
  parameter DEREDDEN.  If this parameter is present and the override
  parameter is no then a warning will be issued and no further correction
  will be applied.  The override parameter permits overriding this check.  If
  overriding a previous correction the <i>uncorrect</i> parameter determines
  whether the spectra are first uncorrected to the original values before
  applying the new correction.  If <i>uncorrect</i> is yes then the image
  header DEREDDEN parameter will refer to a correction from the original data
  while if it is no then the new correction is differential and the keyword
  will only reflect the last correction.  When correcting individual spectra
  separately in a multispectra image with different extinction parameters the
  uncorrect parameter should be no.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The input spectra are corrected for interstellar extinction, or
  reddening, using the empirical selective extinction function of
  Cardelli, Clayton, and Mathis, <b>ApJ 345:245</b>, 1989, (CCM).
  The function is defined over the range 0.3-10 inverse microns
  or 100-3333 nanometers.  If the input data extend outside this
  range an error message will be produced.
  </p>
  <p>
  The extinction function requires two parameters, the absolute extinction at
  5550A, A(V), and the ratio, R(V), of this extinction to the color excess
  between 4350A and 5550A, E(B-V).
  </p>
  <p>
  One of the input task parameters is R(V).  If it is not known one
  may use the default value of 3.1 typical of the average 
  interstellar extinction.  The second input parameter is chosen by
  the parameter <i>type</i> which may take the values <span style="font-family: monospace;">"A(V)"</span>, <span style="font-family: monospace;">"E(B-V)"</span>, or
  <span style="font-family: monospace;">"c"</span>.  The value of the parameter is specified by the parameter
  <i>value</i>.
  </p>
  <p>
  If A(V) is used then the CCM function can be directly evaluated.  If
  E(B-V) is used then A(V) is derived by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  (1)     A(V) = R(V) * E(B-V)
  </pre></div>
  <p>
  For planetary nebula studies the logarithmic extinction at H beta,
  denoted as c, is often determined instead of E(B-V).  If this type
  of input is chosen then A(V) is derived by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  (2)     A(V) = R(V) * c * (0.61 + 0.024 * c).
  </pre></div>
  <p>
  This relation is based on the relation betwen E(B-V) and c computed
  by Kaler and Lutz, <b>PASP 97:700</b>, 1985 to include corrections between
  the monochromatic parameter c and the broadband parameter E(B-V).
  In particular the function is a least squares fit to the values of
  c and E(B-V) in Table III of the form:
  </p>
  <div class="highlight-default-notranslate"><pre>
  (3)     E(B-V) = c * (A + B * c)
  </pre></div>
  <p>
  The input spectra are specified by a list of root names (when using record
  extension format) or full image names.  They are required to be dispersion
  corrected (DC-FLAG &gt;= 0) and not previously corrected (DEREDDEN absent).
  Spectra not satisfying these requirements are skipped with a warning.  The
  DEREDDEN flag may be overridden with the <i>override</i> parameter.  This
  may be done if different extinction parameters are required for different
  spectra in the same multiple spectrum image or if a new correction is
  to be applied.  The <i>uncorrect</i> parameter determines whether the
  previous correction is removed so that the final correction is relative
  to the original data or if the new correction is differential on the
  previous correction.  Note that if applying separate corrections to
  different spectra in a single multispectral image then override should
  be yes and uncorrect should be no.
  </p>
  <p>
  A subset of apertures to be corrected may be selected from one dimensional
  spectra with the <i>apertures</i> parameter.  Long slit or other higher
  dimensional spatially sampled spectra are treated as a unit.  The output
  calibrated spectra may replace the input spectra if no output spectra list
  is specified or if the output name is the same as the input name.  When
  using record number extensions the output spectra will have the same
  extensions applied to the root names as those used for the input spectra.
  </p>
  <p>
  Note that by specifying a negative extinction parameter this task may
  be used to add interstellar extinction.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To deredden a spectrum with an extinction of 1.2 magnitudes at V:
      
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; deredden obj1.ms drobj1.ms 1.2 type=A
  </pre></div>
  <p>
  2.  To deredden a spectrum in place with a color excess of 0.65 and
  and R(V) value of 4.5:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; deredden obj2.ms obj2.ms R=4.5
  E(B-V): .65
  </pre></div>
  <p>
  3.  To deredden a series of IRS planetary nebula spectra using the
  H beta extinction in the irs package:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; deredden pn12 drpn12 1-5,12-14 type=c
  c: 1.05
  </pre></div>
  <p>
  4.  To redden a spectrum:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; deredden artspec artspec -1.2 type=A
  </pre></div>
  <p>
  5. To deredden a long slit or Fabry-Perot spectrum either DISPAXIS
  must be in the image header or be specified in the package parameters.
  The summing parameters are ignored.
      
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; deredden obj1 drobj1 1.2 type=A
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_DEREDDEN">
  <dt><b>DEREDDEN V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DEREDDEN' Line='DEREDDEN V2.10.3' -->
  <dd>Extended to operate on two and three dimensional spatial spectra such as
  calibrated long slit and Fabry-Perot data.
  An option was added to allow a previous correction to be undone in order
  to keep the DEREDDEN information accurate relative to the original
  data.
  </dd>
  </dl>
  <dl id="l_DEREDDEN">
  <dt><b>DEREDDEN V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DEREDDEN' Line='DEREDDEN V2.10' -->
  <dd>This task is new.
  </dd>
  </dl>
  </section>
  <section id="s_notes">
  <h3>Notes</h3>
  <p>
  Since there can be only one deredding flag in multispectral images
  one needs to override the flag if different spectra require different
  corrections and then only the last correction will be recorded.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  calibrate
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'NOTES' 'SEE ALSO'  -->
  

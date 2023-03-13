.. _apdefault:

apdefault: Set the default aperture parameters
==============================================

**Package: kpnoslit**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  apdefault
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_lower">
  <dt><b>lower = -5., upper = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lower' Line='lower = -5., upper = 5.' -->
  <dd>Default lower and upper aperture limits relative to the aperture center.
  These limits are used for apertures found with <b>apfind</b> and when
  defining the first aperture in <b>apedit</b>.
  </dd>
  </dl>
  <dl id="l_apidtable">
  <dt><b>apidtable = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apidtable' Line='apidtable = ""' -->
  <dd>Aperture identification table.  This may be either a text file or an
  image.  A text file consisting of lines with an aperture number, beam
  number, and aperture title or identification.  An image will contain the
  keywords SLFIBnnn with string value consisting of aperture number, beam
  number, optional right ascension and declination, and aperture title.  This
  information is used to assign aperture information automatically in
  <b>apfind</b> and <b>apedit</b>.
  </dd>
  </dl>
  <p style="text-align:center">Default Background Subtraction Parameters
  
  </p>
  <dl id="l_b_function">
  <dt><b>b_function = <span style="font-family: monospace;">"chebyshev"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_function' Line='b_function = "chebyshev"' -->
  <dd>Default background fitting function.  The fitting function types are
  <span style="font-family: monospace;">"chebyshev"</span> polynomial, <span style="font-family: monospace;">"legendre"</span> polynomial, <span style="font-family: monospace;">"spline1"</span> linear spline, and
  <span style="font-family: monospace;">"spline3"</span> cubic spline.
  </dd>
  </dl>
  <dl id="l_b_order">
  <dt><b>b_order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_order' Line='b_order = 1' -->
  <dd>Default background function order.  The order refers to the number of
  terms in the polynomial functions or the number of spline pieces in the spline
  functions.
  </dd>
  </dl>
  <dl id="l_b_sample">
  <dt><b>b_sample = <span style="font-family: monospace;">"-10:-6,6:10"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_sample' Line='b_sample = "-10:-6,6:10"' -->
  <dd>Default background sample.  The sample is given by a set of colon separated
  ranges each separated by either whitespace or commas.  The string <span style="font-family: monospace;">"*"</span> refers
  to all points.  Note that the background coordinates are relative to the
  aperture center and not image pixel coordinates so the endpoints need not
  be integer.
  </dd>
  </dl>
  <dl id="l_b_naverage">
  <dt><b>b_naverage = -3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_naverage' Line='b_naverage = -3' -->
  <dd>Default number of points to average or median.  Positive numbers
  average that number of sequential points to form a fitting point.
  Negative numbers median that number, in absolute value, of sequential
  points.  A value of 1 does no averaging and each data point is used in the
  fit.
  </dd>
  </dl>
  <dl id="l_b_niterate">
  <dt><b>b_niterate = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_niterate' Line='b_niterate = 0' -->
  <dd>Default number of rejection iterations.  If greater than zero the fit is
  used to detect deviant fitting points and reject them before repeating the
  fit.  The number of iterations of this process is given by this parameter.
  </dd>
  </dl>
  <dl id="l_b_low_reject">
  <dt><b>b_low_reject = 3., b_high_reject = 3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_low_reject' Line='b_low_reject = 3., b_high_reject = 3.' -->
  <dd>Default background lower and upper rejection sigmas.  If greater than zero
  points deviating from the fit below and above the fit by more than this
  number of times the sigma of the residuals are rejected before refitting.
  </dd>
  </dl>
  <dl id="l_b_grow">
  <dt><b>b_grow = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='b_grow' Line='b_grow = 0.' -->
  <dd>Default reject growing radius.  Points within a distance given by this
  parameter of any rejected point are also rejected.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task sets the values of the default aperture parameters for the
  tasks <b>apedit</b> and <b>apfind</b> which define new apertures.  For a
  description of the components of an aperture see the paper <b>The
  APEXTRACT Package</b>.  In <b>apedit</b> the default aperture limits and
  background parameters are only used if there are no other
  apertures defined.  The aperture identification table is used when
  reordering the apertures with the <span style="font-family: monospace;">'o'</span> key.  When run the parameters are
  displayed and modified using the <b>eparam</b> task.
  </p>
  <p>
  The aperture limits and background fitting sample regions are defined
  relative to the center of the aperture.  The background fitting parameters
  are those used by the ICFIT package.  They may be modified interactively
  with the <span style="font-family: monospace;">'b'</span> key in the task <b>apedit</b>.  For more on background fitting
  and subtracting see <b>apbackground</b>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To review and modify the default aperture parameters:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; apdefault
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_APDEFAULT">
  <dt><b>APDEFAULT V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='APDEFAULT' Line='APDEFAULT V2.11' -->
  <dd>The aperture ID table information may now be contained in the
  image header under the keywords SLFIBnnn.
  </dd>
  </dl>
  <p>
  SEE ALSO
  apbackground, apedit, apfind, icfit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS'  -->
  

.. _slist:

slist: List spectrum headers
============================

**Package: ctioslit**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  slist1d input records
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The image root name for the spectra to be listed.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records' -->
  <dd>The record string for the spectra to be listed. The records will be appended
  to the root name to form image names of the type <span style="font-family: monospace;">"root.xxxx"</span>.
  </dd>
  </dl>
  <dl id="l_long_header">
  <dt><b>long_header = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='long_header' Line='long_header = no' -->
  <dd>If set to yes, then a complete listing of the header elements
  is given. If set to no, then a single line per spectrum is given which lists
  in the following order: the image name, object or sky spectrum, exposure
  time, spectrum length, and image title.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Each spectrum in the list implied by the root name and the record string
  is opened and the header is read. The pixel file is not accessed in order
  to save time. The header listing is directed to STDOUT and may be
  redirected for printing.
  </p>
  <p>
  A warning message is issued if
  a requested image is not found, but otherwise proceeds.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following example lists 8 spectral headers in long form on the printer:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; slist1d nite1 1001-1008 | lprint
  </pre></div>
  <p>
  The next example lists the same spectral headers but in short form
  on the terminal
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; slist1d nite1 1001-1008 long-
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_SLIST1D">
  <dt><b>SLIST1D V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SLIST1D' Line='SLIST1D V2.10' -->
  <dd>This task is the same as V2.9 <b>slist</b> and applies only to the older
  IRS/IIDS record extension spectra.  In V2.10 <b>slist</b>
  has been revised for multiaperture spectra.
  </dd>
  </dl>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  SLIST1D does not inform the user if the pixel file can or cannot be read.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  slist, imheader
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'BUGS' 'SEE ALSO'  -->
  

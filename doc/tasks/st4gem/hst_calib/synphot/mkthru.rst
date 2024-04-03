.. _mkthru:

mkthru: Create a throughput table for installation in CDBS
==========================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkthru input
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task will convert an ascii file or st4gem binary table to the
  fits format currently used for synphot throughput tables. The table
  will have the required header keywords, column names, column units,
  and column formats. To run the task, pass the name of the file or
  files to be converted on the command line. File name templates may be
  used. Output files have the same root name as the input files, and
  have the extension <span style="font-family: monospace;">"fits"</span>.
  </p>
  <p>
  The task queries the user for header keywords if they are not present
  in the imput file. Because the task parameters that read this
  information use query mode, you will be queried for this information
  even if you set them in the parameter editor. (Though the values you
  set will be displayed as default values.)
  </p>
  <p>
  Column names can be specified in ascii files by placing them on the
  first line and setting the hidden parameter title to yes. The task
  uses default values for the column information if it is not present in
  the input file. The default column names are WAVELENGTH, THROUGHPUT,
  and ERROR. The default column units are ANGSTROMS, TRANSMISSION, and
  TRANSMISSION. The default print formats are %10.1f, %12.5g, and
  %12.5g. Any of these values can be changed by tchcol after this task
  is run if they are not correct.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [string]' -->
  <dd>List of input file names. File names may include wild cards. Output
  files have the same names as the input files, but their exyension is
  changed to fits.
  </dd>
  </dl>
  <dl id="l_instrument">
  <dt><b>instrument [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='instrument' Line='instrument [string]' -->
  <dd>The name of the telescope instrument used in the observation. Only
  used if this header keyword is not found in the input file.
  </dd>
  </dl>
  <dl id="l_compname">
  <dt><b>compname [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='compname' Line='compname [string]' -->
  <dd>The name of the component associated with the throughput file. Only
  used if this header keyword is not found in the input file.
  </dd>
  </dl>
  <dl id="l_useafter">
  <dt><b>useafter [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='useafter' Line='useafter [string]' -->
  <dd>The start of the date range for which the throughput file is
  valid. The date should be in the form <span style="font-family: monospace;">"mmm dd yyyy"</span> where <span style="font-family: monospace;">"mmm"</span> is a
  three letter month abbreviation. Only used if this header keyword is
  not found in the input file.
  </dd>
  </dl>
  <dl id="l_pedigree">
  <dt><b>pedigree [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pedigree' Line='pedigree [string]' -->
  <dd>The source of the information in the throughput file. Should have one
  of the following values: INFLIGHT, GROUND, MODEL, or DUMMY. Only used
  if this header keyword is not found in the input file.
  </dd>
  </dl>
  <dl id="l_descip">
  <dt><b>descip [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='descip' Line='descip [string]' -->
  <dd>A short description of the throughput file. Only used if this header
  keyword is not found in the input file.
  </dd>
  </dl>
  <dl id="l_comment">
  <dt><b>comment [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='comment' Line='comment [string]' -->
  <dd>A comment on the throughput file. Only used if this header keyword is
  not found in the input file.
  </dd>
  </dl>
  <dl>
  <dt><b>(title = no) [bool]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(title = no) [bool]' -->
  <dd>If set to yes, the column names are taken from the first line of the
  input file.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = no) [bool]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = no) [bool]' -->
  <dd>If set to yes, display a message after each file is converted to fits.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convert a set of ascii files to fits format:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; mkthru *.dat
  </pre></div>
  <p>
  The task will prompt for all the header keyword values.
  </p>
  <p>
  2. Convert an st4gem binary format table to fits format:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; mkthru hst_dark.tab
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by B. Simon
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  tchcol
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

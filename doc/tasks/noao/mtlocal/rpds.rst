.. _rpds:

rpds: Convert a PDS image into an IRAF image
============================================

**Package: mtlocal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rpds pds_file file_list iraf_file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_pds_file">
  <dt><b>pds_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pds_file' Line='pds_file' -->
  <dd>The PDS data source. The data source may be a template specifying
  a list of disk files, e.g. pds* or a mag tape file specification of
  the form mtl*[n], e.g. <span style="font-family: monospace;">"mta1600"</span> or <span style="font-family: monospace;">"mtb800[1]"</span>. The mt specifies magtape,
  l specifies the drive, a,b,c etc, * specifies the density and [n]
  the tape file number. If no tape file number is specified rpds reads
  the tape files specified by file_list.
  </dd>
  </dl>
  <dl id="l_file_list">
  <dt><b>file_list</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file_list' Line='file_list' -->
  <dd>A string parameter containing the list of tape files to be processed.
  File_list is only requested if no tape file number is specified in pds_file.
  For example the string
  	<span style="font-family: monospace;">"1,2,3-5,8-6"</span>
  will convert files 1 through 8.
  </dd>
  </dl>
  <dl id="l_iraf_file">
  <dt><b>iraf_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='iraf_file' Line='iraf_file' -->
  <dd>The IRAF file which will receive the PDS data if the make_image
  switch is set. If multiple files are input from tape or disk, the tape file
  number or disk sequence number will be appended to the output file name.
  </dd>
  </dl>
  <dl id="l_make_image">
  <dt><b>make_image = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='make_image' Line='make_image = yes' -->
  <dd>If make_image is not set, the PDS image headers are listed on the standard
  output and no image file is created.
  </dd>
  </dl>
  <dl id="l_long_header">
  <dt><b>long_header = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='long_header' Line='long_header = no' -->
  <dd>If this switch is set the full PDS header is printed on the standard output.
  </dd>
  </dl>
  <dl id="l_short_header">
  <dt><b>short_header = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='short_header' Line='short_header = yes' -->
  <dd>If this switch is set only the output filename,
  the title string, and the image dimensions for each image are printed
  on the standard output.
  </dd>
  </dl>
  <dl id="l_datatype">
  <dt><b>datatype = <span style="font-family: monospace;">"s"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datatype' Line='datatype = "s"' -->
  <dd>The IRAF image data type, s (short integer), i (integer), l (long integer),
   r (real) or d (double).
  </dd>
  </dl>
  <dl id="l_tenbit">
  <dt><b>tenbit = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tenbit' Line='tenbit = no' -->
  <dd>Old ten bit format?
  </dd>
  </dl>
  <dl id="l_ninetrack">
  <dt><b>ninetrack = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ninetrack' Line='ninetrack = yes' -->
  <dd>Ninetrack or old seven track tapes?
  </dd>
  </dl>
  <dl id="l_offset">
  <dt><b>offset = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='offset' Line='offset = 0' -->
  <dd>Offset is an integer parameter which is added to the tape file number
  or disk sequence number and
  appended to the parameter iraf_file. For example if offset = 100,
  iraf_file = <span style="font-family: monospace;">"pds"</span> and file_list = <span style="font-family: monospace;">"1-3"</span> the output file names will be
  <span style="font-family: monospace;">"pds101"</span>, <span style="font-family: monospace;">"pds102"</span> and <span style="font-family: monospace;">"pds103"</span> respectively, instead of <span style="font-family: monospace;">"pds001"</span>, <span style="font-family: monospace;">"pds002"</span>
  and <span style="font-family: monospace;">"pds003"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Kitt Peak PDS data is read into IRAF from either a
  list of disk files or magnetic tape.
  The PDS header may optionally be printed on the standard output as either a
  full listing or a short description.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Convert a ninetrack PDS image tape to a set of IRAF images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; pdsread mtb1600 1-999 images
  </pre></div>
  <p>
  List the contents of a nintrack PDS tape on the standard output.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; pdsread mtb1600 1-999 images ma-
  </pre></div>
  <p>
  Convert a list of pds file on disk to IRAF images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; pdsread pds* 1 images
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS'  -->
  

.. _readvt:

readvt: Read a full disk tape and produce an IRAF image.
========================================================

**Package: vtel**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  readvt input_fd files output_image
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input_fd">
  <dt><b>input_fd</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input_fd' Line='input_fd' -->
  <dd>File or device template, e.g. <span style="font-family: monospace;">"mta1600[1]"</span> or <span style="font-family: monospace;">"mtb800"</span> or <span style="font-family: monospace;">"junk"</span> or <span style="font-family: monospace;">"s*"</span>
  </dd>
  </dl>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>List of tape file numbers or ranges delimited by commas, e.g. <span style="font-family: monospace;">"1-3,5-8"</span>.
  `Files' is requested only if no file number is given in `input'.
  Files will be read in ascending order, regardless of the order of the list.
  Reading will terminate if EOT is reached, thus a list such as <span style="font-family: monospace;">"1-999"</span>
  may be used to read all the files on the tape.
  </dd>
  </dl>
  <dl id="l_output_image">
  <dt><b>output_image template</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output_image' Line='output_image template' -->
  <dd>Name to give output image.  If the input file template is not a magtape
  specification then this can be an IRAF filename template to be
  expanded into a list of files.  If the number of files in the input
  template and in the output template do not match and if the output
  template expands to one filename then that filename is used as a
  root name to which filenumbers are appended for each input file.
  i.e. <span style="font-family: monospace;">"junk"</span> becomes <span style="font-family: monospace;">"junk001"</span>, <span style="font-family: monospace;">"junk002"</span>, etc.  If the input template
  is a magtape without a filenumber attached, i.e. <span style="font-family: monospace;">"mta"</span>, the
  output name is used as a root name and the file number is appended
  for each file read.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Flag to signal program that it should produce verbose output.  This includes
  header information and progress reports.
  </dd>
  </dl>
  <dl id="l_headeronly">
  <dt><b>headeronly = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='headeronly' Line='headeronly = no' -->
  <dd>Flag to signal the program that it should only print out header information
  and quit without reading the data.  The 'verbose' flag must be set to yes
  to use this flag since otherwise the header information will not be printed.
  This flag is used to look at headers on the tape to check dates, times
  and observation types.
  </dd>
  </dl>
  <dl id="l_robust">
  <dt><b>robust = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='robust' Line='robust = no' -->
  <dd>Flag to signal program that it should ignore a wrong observation type in the
  image header.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Readvt reads any one of the grams on a vacuum telescope tape and puts the
  data into an IRAF image.  The IRAF image is 2048x2048 short integers.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. To read the second image from mta at 1600 bpi, store the image into <span style="font-family: monospace;">"image1"</span>
  and see verbose output the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; readvt mta1600[2] image1 v+
  </pre></div>
  <p>
  2. To look at the header information of the 4th file on a tape which is on
  mtb and which was written at 1600 bpi, the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; readvt mtb1600[4] v+ h+
  </pre></div>
  <p>
  3. To read the disk files <span style="font-family: monospace;">"s001"</span>, <span style="font-family: monospace;">"s002"</span>, <span style="font-family: monospace;">"s003"</span>, <span style="font-family: monospace;">"s004"</span> and put the output
  images into the files <span style="font-family: monospace;">"s001i"</span>, <span style="font-family: monospace;">"s002i"</span>, <span style="font-family: monospace;">"s003i"</span>, <span style="font-family: monospace;">"s004i"</span> without
  verbose output (assuming no other file in the directory starts with <span style="font-family: monospace;">"s"</span>)
  the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; readvt s* s*//i
  </pre></div>
  <p>
  4. To read the first five files on mta and put the output images into files
  images with root name HHH the command would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  vt&gt; readvt mta 1-5 HHH
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  writevt
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

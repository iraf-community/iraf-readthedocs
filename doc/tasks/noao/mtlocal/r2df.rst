.. _r2df:

r2df: Convert a CTIO 2-d frutti image into an IRAF image
========================================================

**Package: mtlocal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  r2df r2df_file file_list iraf_file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_r2df_file">
  <dt><b>r2df_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='r2df_file' Line='r2df_file' -->
  <dd>The 2D-Frutti data source.  If the data source is a disk file or an explicit
  tape file
  specification of the form mt*[n] where n is a file number then only that file
  is converted.  If the general tape device name is given, i.e. mta, mtb800, etc,
  then the files specified by the files parameter will be read from the tape.
  </dd>
  </dl>
  <dl id="l_file_list">
  <dt><b>file_list</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file_list' Line='file_list' -->
  <dd>The files to be read from a tape are specified by the file_list string.  The
  string can consist of any sequence of file numbers separated by
  at least one of comma, or dash.
  A dash specifies a range of files.  For example the string
  <div class="highlight-default-notranslate"><pre>
  "1,2,3-5,8-6"
  </pre></div>
  will convert the files 1 through 8.
  </dd>
  </dl>
  <dl id="l_iraf_file">
  <dt><b>iraf_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='iraf_file' Line='iraf_file' -->
  <dd>The IRAF image file which will receive the 2D-Frutti data if the make_image
  parameter switch is set.  For tape files specified by the file_list parameter
  the filename will be used as a prefix and the file number will be appended.
  Otherwise, the file will be named as specified.  Thus,
  reading files 1 and 3 from a 2D-Frutti tape with a filename of data will produce
  the files data1 and data3.  It is legal to use a null filename.
  </dd>
  </dl>
  <dl id="l_make_image">
  <dt><b>make_image = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='make_image' Line='make_image = yes' -->
  <dd>This switch determines if 2D-Frutti image data is converted to an IRAF image
  file.  This switch is set to no to obtain just header information with the
  long_header or short_header switches.
  </dd>
  </dl>
  <dl id="l_long_header">
  <dt><b>long_header = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='long_header' Line='long_header = no' -->
  <dd>If this switch is set the full 2D-Frutti header is printed on standard output.
  </dd>
  </dl>
  <dl id="l_short_header">
  <dt><b>short_header = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='short_header' Line='short_header = yes' -->
  <dd>If this switch is set only the output filename,
  the title string, and the image dimensions are printed.
  </dd>
  </dl>
  <dl id="l_standard_format">
  <dt><b>standard_format = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='standard_format' Line='standard_format = yes' -->
  <dd>The 2D-Frutti standard format has least significant byte first.  Some 2D-Frutti
  data, however, does not follow this byte order convention.  Thus, to read
  the non-standard 2D-Frutti data this parameter is set to no.
  </dd>
  </dl>
  <dl id="l_datatype">
  <dt><b>datatype = <span style="font-family: monospace;">"s"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datatype' Line='datatype = "s"' -->
  <dd>The IRAF image file may be of a different data type than 2D-Frutti image data.
  The data type may be specified as s for short, l for long, r for real, and
  d for double.  The user must beware of truncation problems if an
  inappropriate data type is specified.  If an incorrect data_type or a
  null string is given for this parameter then a default data type is used
  which is the appropriate minimum size for the input pixel values.
  </dd>
  </dl>
  <dl id="l_offset">
  <dt><b>offset = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='offset' Line='offset = 0' -->
  <dd>Offset is an integer parameter specifying the offset to the tape file number
  appended to iraf_file.  For example if the user specifies offset = 100,
  iraf_file = <span style="font-family: monospace;">"r2d"</span> and file_list = <span style="font-family: monospace;">"1-3"</span>, the output file names produced
  will be <span style="font-family: monospace;">"r2d101"</span>, <span style="font-family: monospace;">"r2d102"</span> and <span style="font-family: monospace;">"r2d103"</span> respectively, instead of <span style="font-family: monospace;">"r2d001"</span>,
  <span style="font-family: monospace;">"r2d002"</span> and <span style="font-family: monospace;">"r2d003"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Cerro Tololo 2D-Frutti format image data is read from the specified source;
  either a disk file or magnetic tape.
  The 2D-Frutti header may optionally be printed on the standard
  output as either a full listing or a short description.  Image data may
  optionally be converted to an IRAF image of specified data type.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convert a 2D-Frutti image tape to a set of IRAF images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; r2df mtb1600 1-999 r2dfile
  </pre></div>
  <p>
  2. List the contents of a 2D-Frutti tape on the standard output without
  creating an image file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; r2df mtb1600 1-999 r2dfile ma-
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  t2d, mtexamine, rewind
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

.. _rdumpf:

rdumpf: Convert IPPS rasters from a DUMPF tape to IRAF images
=============================================================

**Package: mtlocal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rdumpf dumpf_file file_list iraf_file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_dumpf_file">
  <dt><b>dumpf_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dumpf_file' Line='dumpf_file' -->
  <dd>The dumpf data source, i.e., the name of a magtape device.
  </dd>
  </dl>
  <dl id="l_file_list">
  <dt><b>file_list</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file_list' Line='file_list' -->
  <dd>A string listing the permanent files to be read from the DUMPF tape.  
  </dd>
  </dl>
  <dl id="l_iraf_file">
  <dt><b>iraf_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='iraf_file' Line='iraf_file' -->
  <dd>The IRAF file which will receive the image data if the <i>make_image</i>
  parameter
  is set.  If more then one raster is being read, the output
  filename is concatenated from the <i>iraf_file</i> parameter, the tape
  file number and the raster sequence number.  That is, reading rasters 1 - 3
  from files 3 and 4 with iraf_file = <i>pic</i> would generate a sequence of 
  files:
  pic3.001, pic3.002, pic3.003, pic4.001, pic4.002, pic4.003.
  </dd>
  </dl>
  <dl id="l_raster_list">
  <dt><b>raster_list = <span style="font-family: monospace;">"1-999"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='raster_list' Line='raster_list = "1-999"' -->
  <dd>A string listing the IPPS rasters to be read from each file specified by
  the <i>file_list</i> parameter.
  </dd>
  </dl>
  <dl id="l_make_image">
  <dt><b>make_image = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='make_image' Line='make_image = yes' -->
  <dd>This switch determines whether the IPPS rasters are converted to IRAF images.
  When this switch is set to <i>no</i>, only a listing of the IPPS rasters is 
  produced, no output image is written.
  </dd>
  </dl>
  <dl id="l_print_header">
  <dt><b>print_header = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='print_header' Line='print_header = yes' -->
  <dd>This switch determines if the IPPS header information will be listed for those
  rasters being read.
  </dd>
  </dl>
  <dl id="l_data_type">
  <dt><b>data_type = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='data_type' Line='data_type = ""' -->
  <dd>The data type of the output IRAF image.  If an incorrect data_type or null
  string is entered, the default data type used is determined by the number
  of bits per pixel in the IPPS raster.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IPPS rasters stored in DUMPF format are read and optionally converted to
  IRAF images.  The IPPS ID and other header information is printed.
  The rasters to be converted are specified by both a file
  number and then a raster number within that file.  It may be helpful to
  first run task <b>ldumpf</b> to list the contents of the DUMPF tape; only
  IPPS rasters can be converted.  
  <br>
  Some dumpf volumes are written on more than one tape.
  Task <i>rdumpf</i> cannot recover a file that is split across two tapes on 
  a <span style="font-family: monospace;">"multi-volume-set"</span> dumpf tape.  It is, however, possible to read the files
  beyond the leading partial file; this is done by incrementing the 
  <b>file_list</b> parameter by 1.  For example, the first complete file 
  on the second tape of a multi-volume-set is indicated by <b>file_list</b> = 2.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  [1] Convert all rasters in the 3rd permanent file on tape:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rdumpf mta 3 ipps
  </pre></div>
  <p>
  [2] Convert all rasters in all permanent files:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rdumpf mta 1-999 ipps
  </pre></div>
  <p>
  [3] List the first 10 IPPS rasters of the first permanent file:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rdumpf mta 1 raster_list=1-10 make_image=no
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The Cyber format readers, including <i>rdumpf</i>, have not been implemented
  on SUN/IRAF and AOS/IRAF.
  </p>
  <p>
  The current version of IRAF magtape I/O does not read beyond the first
  volume of a multivolume tape.  As described above, <i>rdumpf</i> cannot
  read a file split across two tapes.
  <br>
  The record structure of a DUMPF tape is used to
  filter out noise records and extraneous bits that fill out a tape byte;
  this tape structure information is lost when the tape is copied to disk,
  and so <b>rdumpf</b> may not be able to convert some DUMPF format disk files.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ldumpf
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

.. _ridsout:

ridsout: Convert a text file in IDSOUT format to IRAF images
============================================================

**Package: mtlocal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ridsout idsout_file iraf_file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_idsout_file">
  <dt><b>idsout_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='idsout_file' Line='idsout_file' -->
  <dd>The text file or files containing the IDSOUT format data.  This will most likely
  be the redirected output from task <b>rcardimage</b>.
  </dd>
  </dl>
  <dl id="l_iraf_file">
  <dt><b>iraf_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='iraf_file' Line='iraf_file' -->
  <dd>The IRAF file which will receive the data if the <i>make_image</i> parameter
  is set.  If multiple records are being converted, the output
  filename is concatenated from this parameter and the IDS record number.
  That is, images with these names would be created if <i>iraf_file</i> = <span style="font-family: monospace;">"ids"</span>:
  ids.1001, ids.1002, ids.1003, ..., ids.2001, ids.2002, ..., ids.3001 ....
  </dd>
  </dl>
  <dl id="l_record_numbers">
  <dt><b>record_numbers = <span style="font-family: monospace;">"1001-9999"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='record_numbers' Line='record_numbers = "1001-9999"' -->
  <dd>A string listing the IDS records to be read.
  </dd>
  </dl>
  <dl id="l_make_image">
  <dt><b>make_image = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='make_image' Line='make_image = yes' -->
  <dd>This switch determines whether the IDS records are converted to IRAF images.
  When <i>make_image</i> = no, only a listing of the headers is produced, 
  no output image is written.
  </dd>
  </dl>
  <dl id="l_print_pixels">
  <dt><b>print_pixels = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='print_pixels' Line='print_pixels = no' -->
  <dd>When this parameter is set to yes, the values of the ids pixels are printed.
  </dd>
  </dl>
  <dl id="l_long_header">
  <dt><b>long_header = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='long_header' Line='long_header = yes' -->
  <dd>This parameter determines whether a long or short header is printed.  When
  <i>long_header</i> = no, a short header is printed.  The
  short header contains only the record number and ID string; the long header
  contains all information available 
  including the RA, Dec, HA, ST, UT, reduction flags, airmass, integration time,
  starting wavelength and wavelength per channel information.
  </dd>
  </dl>
  <dl id="l_data_type">
  <dt><b>data_type = <span style="font-family: monospace;">"r"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='data_type' Line='data_type = "r"' -->
  <dd>The data type of the output IRAF image.  If an incorrect data_type or null
  string is entered, the default data type <i>real</i> is used.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IDSOUT format IDS records are read from a text file and optionally
  converted to a sequence of one dimensional IRAF images.  The text file will
  most likely have been created by reading an IDSOUT tape with <b>rcardimage</b>.
  The IDS records to be read from the file can be specified.
  The IDS header information is printed in either a short or long 
  form.  The pixels values can be listed as well.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  [1] Convert all records in the IDSOUT file to IRAF images, with the root image 
  name being <span style="font-family: monospace;">"aug83"</span>.  The IDSOUT file is the first file on the tape, which is 
  mounted on mtb.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rcardimage mtb[1] | ridsout aug83
  </pre></div>
  <p>
  [2] List the headers from the same IDSOUT file read in example 1, but don't make
  output images.  A <b>long_header</b> will be listed; sample output is shown.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rcardimage mtb[1] | ridsout make_image=no
  RECORD = 2317, label = "CALLISTO  2297/2298  CLEAR/2.5ND",
  oflag = OBJECT, beam_number = 0,   alpha_ID = NEW,   companion = 2318,
  airmass = 1.524,        W0 = 3430.735,    WPC = 1.032,     ITM =  960,
  NP1 = 0, NP2 = 1024,    UT = 3:36:20.0,    ST = 15:36:43.0,
  HA = 1:39:48.5,         RA = 13:56:55.5,  DEC = -10:42:37.1,
  df = -1, sm = -1, qf = -1, dc = 0, qd = 0, ex = 0, bs = 1, ca = 0, co = -1
  </pre></div>
  <p>
  [3] Print the pixel values for records 5086 and 5087.  No output image will
  be written, and only the short header listed.  Again, the IDSOUT file is the
  first file on the tape, which is mounted on mtb.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rcard mtb[1] | ridsout make- long- print+ rec = 5086,5087
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The current version of IRAF magtape I/O does not read beyond the first
  volume of a multivolume tape.
  <br>
  Task <b>ridsout</b> allows for converting more than one IDSOUT file per 
  execution.  In cases where a given record number occurs in more than one
  IDSOUT file being read and <i>make_image = yes</i>, this creates a problem, as
  the images being written will have the same name for the duplicate record 
  numbers (<span style="font-family: monospace;">"iraf_name.record_number"</span>).  The action taken in this situation depends
  on the value of <span style="font-family: monospace;">"noclobber"</span>; the user should be aware of the potential
  problem.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ridsfile, ridsmtn
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

.. _ridsmtn:

ridsmtn: Convert mountain format IDS/IRS data to IRAF images
============================================================

**Package: mtlocal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ridsmtn ids_file iraf_file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_ids_file">
  <dt><b>ids_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ids_file' Line='ids_file' -->
  <dd>The IDS data source.
  </dd>
  </dl>
  <dl id="l_iraf_file">
  <dt><b>iraf_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='iraf_file' Line='iraf_file' -->
  <dd>The IRAF file which will receive the data if the <i>make_image</i> parameter
  is set.  If multiple records are being read, the output
  filename is concatenated from this parameter and the IDS record number.
  IRAF images with these names would be created from IDS records 1, 2 and 3 if
  <i>iraf_file</i> = <span style="font-family: monospace;">"ids"</span> (and offset = 0; see below):  ids.0001, ids.0002, 
  ids.0003.
  </dd>
  </dl>
  <dl id="l_file_number">
  <dt><b>file_number = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file_number' Line='file_number = 1' -->
  <dd>If <i>ids_file</i> is a tape device, this parameter tells which tape file
  will be read.  In almost all cases, the IDS data will occupy the first
  and only file on the tape.
  </dd>
  </dl>
  <dl id="l_record_numbers">
  <dt><b>record_numbers = <span style="font-family: monospace;">"1-9999"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='record_numbers' Line='record_numbers = "1-9999"' -->
  <dd>A string listing the IDS records to be read.  
  </dd>
  </dl>
  <dl id="l_reduced_data">
  <dt><b>reduced_data = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reduced_data' Line='reduced_data = yes' -->
  <dd>A boolean parameter which indicates the data is mountain reduced if set
  to yes, and that the data is raw (unreduced) if set to no.
  </dd>
  </dl>
  <dl id="l_np1">
  <dt><b>np1 = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='np1' Line='np1 = 0' -->
  <dd>The starting pixel to extract in the image. If set to 0, the
  record header parameter NP1 will be used to determine the
  starting pixel.
  This and the following parameter are in effect only when reduced_data
  is set to no. If reduced_data=yes, then the entire spectrum (1024 points)
  is copied.
  </dd>
  </dl>
  <dl id="l_np2">
  <dt><b>np2 = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='np2' Line='np2 = 0' -->
  <dd>The ending pixel to extract. If set to 0, the record
  header parameter NP2 will be used to determine the
  starting pixel.
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
  <dt><b>long_header = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='long_header' Line='long_header = no' -->
  <dd>This parameter determines whether a long or short header is printed.  The
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
  <dl id="l_offset">
  <dt><b>offset = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='offset' Line='offset = 0' -->
  <dd>The integer value of this parameter is added to each IDS record number when
  generating output filenames.  Filenames are of the form 
  <div class="highlight-default-notranslate"><pre>
  <i>iraf_file</i>.record_number+<i>offset</i>
  </pre></div>
  The offset parameter can be used to create a sequence of output IRAF 
  filenames with continuous, sequential suffixes over more than one night's data.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The IDS records from either a raw or reduced IDS mountain tape are read and
  optionally converted to a sequence of one dimensional IRAF images.  The records
  to be read can be specified.  The IDS header information is printed in either 
  a short or long form.  The pixel values can be listed as well.
  </p>
  <p>
  The entire image may be extracted (default for reduced data) by specifying
  the parameters np1=1 and np2=1024 (IIDS and IRS). Otherwise, the
  header parameters NP1 and NP2 will be used to indicate the useful
  portion of the spectrum. For raw data these values are 6 and 1024 for the
  IIDS and 68 and 888 for the IRS (your IRS values may vary).
  </p>
  <p>
  On the mountain, the NEW-TAPE command writes a dummy record on tape with a
  record number equal to the starting record number minus 1.  If this dummy
  record number is included in the <i>record_numbers</i> range, a meaningless
  IRAF image will be written.  In most cases, the dummy record number = 0.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  [1] Convert all records on the IDS tape to IRAF images, with the root image name
  being <span style="font-family: monospace;">"aug83"</span>.  The data is mountain reduced, and all records will be
  converted.  The IDS tape is mounted on mtb.
  </p>
  <p>
  	.nf
  	cl&gt; ridsmtn mtb aug83
  </p>
  <p>
  [2] List the headers from the same mountain tape read in example 1 but don't
  make output images.  A <i>long_header</i> will be listed; sample output is shown.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ridsmtn mtb make_image=no long_header=yes
  
  RECORD = 79, label = "NGC 7662 7.4E 10S AUG 23/24 84 CLOUDS",
  oflag = OBJECT, beam_number = 0,  W0 = 4588.503,  WPC = 2.598, ITM = 120,
  NP1 = 0, NP2 = 1024,  UT = 7:37:04.0,  ST = 22:21:46.0,  HA = -1:03:25.7,
  RA = 23:25:12.6,   DEC = 42:26:37.0,   DRA = 7.4,   DDEC = -10.,
  df =-1, sm =-1, qf =-1, dc = 0, qd = 0, ex =-1, bs = -1, ca = -1, co = 0
  
  RECORD = 238, label = "HENEAR AUG 23/24 84 END 8.4" ENT",
  oflag = SKY,  beam_number = 1,  W0 = 4585.501,  WPC = 2.602, ITM = 400,
  NP1 = 8, NP2 = 1019,  UT = 12:31:01.0,  ST = 3:16:33.0,  HA = 0:17:16.3,
  RA = 2:59:16.7,   DEC = 31:57:30.0
  df = 6, sm = -1, qf = -1, dc = -1, qd =-1, ex =-1, bs =-1, ca =-1, co = -1,
  df[1] =  5889.2139, df[2] =  1355.6821, df[3] =  23.1303, df[4] = -2.85366,
  df[5] =  3.0472932, df[6] =  -4.541831
  </pre></div>
  <p>
  [3] Print the pixel values for records 5086 and 5087.  No output image will
  be written, and only the short header listed.  This time, the IDS tape 
  contains raw data, not reduced.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ridsmtn mtb red- make_im- rec=5086,5087 print_pix-
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ridsout, ridsfile
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

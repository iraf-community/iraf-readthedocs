.. _ridsfile:

ridsfile: Convert IDSFILES from a DUMPF tape to IRAF images
===========================================================

**Package: mtlocal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ridsfile dumpf_file file_number iraf_file
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
  <dl id="l_file_number">
  <dt><b>file_number</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file_number' Line='file_number' -->
  <dd>The ordinal of the DUMPF permanent file containing the IDSFILE to
  be read.  A listing of permanent files on the DUMPF tape can be
  obtained with the <b>ldumpf</b> task.
  </dd>
  </dl>
  <dl id="l_iraf_file">
  <dt><b>iraf_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='iraf_file' Line='iraf_file' -->
  <dd>The IRAF file which will receive the data if the <i>make_image</i> parameter
  is set.  If multiple records are being read, the output
  filename is concatenated from this parameter and the IDS record number.
  That is, images with these names would be created if <i>iraf_file</i> = <span style="font-family: monospace;">"ids"</span>:
  ids.1001, ids.1002, ids.1003, ..., ids.2001, ids.2002, ..., ids.3001 ....
  </dd>
  </dl>
  <dl id="l_record_numbers">
  <dt><b>record_numbers = <span style="font-family: monospace;">"1001-9999"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='record_numbers' Line='record_numbers = "1001-9999"' -->
  <dd>A string listing the IDS records to be read from the IDSFILE.  
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
  The IDS records in an IDSFILE are read from a Cyber DUMPF tape and optionally
  converted to a sequence of one dimensional IRAF images.  The records to be
  read from the IDSFILE can be 
  specified.  The IDS header information is printed in either a short or long 
  form.  The pixels values can be listed as well.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  [1] Convert all records in the IDSFILE to IRAF images, with the root image name
  being <span style="font-family: monospace;">"aug83"</span>.  From running task LDUMPF, it is known that the IDSFILE is the 
  fourth permanent file on the DUMPF tape.  The DUMPF tape is mounted on mtb.
  </p>
  <p>
  	.nf
  	cl&gt; ridsfile mtb 4 aug83
  </p>
  <p>
  [2] List the headers from the same IDSFILE read in example 1, but don't make
  output images.  A <b>long_header</b> will be listed; sample output is shown.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ridsfile mtb 4 make_image=no long_header=yes
  </pre></div>
  <div class="highlight-default-notranslate"><pre>
  RECORD = 2317, label = "CALLISTO  2297/2298  CLEAR/2.5ND",
  oflag = OBJECT, beam_number = 0,   alpha_ID = NEW,   companion = 2318,
  airmass = 1.524,        W0 = 3430.735,    WPC = 1.032,      ITM = 960,
  NP1 = 0, NP2 = 1024,    UT = 3:36:20.0,    ST = 15:36:43.0,
  HA = 1:39:48.5,         RA = 13:56:55.5,  DEC = -10:42:37.1,
  df = -1, sm = -1, qf = -1, dc = 0, qd = 0, ex = 0, bs = 1, ca = 0, co = -1
  </pre></div>
  <p>
  [3] Print the pixel values for records 5086 and 5087.  No output image will
  be written, and only the short header listed.  Again, the IDSFILE is the 
  fourth permanent file on the DUMPF tape, which is mounted on mtb.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ridsfile mtb 4 make_im- rec=5086,5087 print+
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The current version of IRAF magtape I/O does not read beyond the first
  volume of a multivolume tape.
  <br>
  The record structure of a DUMPF tape is used to
  filter out noise records and extraneous bits that fill out a tape byte;
  this tape structure information is lost when the tape is copied to disk,
  and so <b>ridsfile</b> may not be able to convert some DUMPF format disk files.
  <br>
  Task <b>ridsfile</b> allows for converting only one IDSFILE per execution.
  If you wish to read more than one IDSFILE
  from a DUMPF tape, <b>ridsfile</b> must be executed more than once.
  <br>
  The Cyber format readers, including <i>ridsfile</i>, have not been implemented
  on SUN/IRAF and AOS/IRAF.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ldumpf, ridsout, ridsmtn
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

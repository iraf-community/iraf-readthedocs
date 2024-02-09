.. _mscrfits:

mscrfits: Read mosaic data from a FITS tape
===========================================

**Package: msctools**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  FITS files from tape are copied to disk with a possible renaming
  to restore the filename the file had when written by <b>mscwfits</b>.
  One may also just list the contents of the tape.
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  mscrfits input [output]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The input IRAF tape specification with no position; e.g. mta.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output root name for the files.  Multiple files will be written with a
  four digit numeric extension based on the <i>offset</i> parameter and the
  tape position.  Once the file is written to disk the file name may be
  changed to the name specified by the FILENAME keyword (provided a file
  doesn't already exist with that name) if the <i>original</i> parameter is
  set.  If only listing the contents of the tape this parameter need not
  be specified.
  </dd>
  </dl>
  <dl id="l_tapefiles">
  <dt><b>tapefiles = <span style="font-family: monospace;">"1-"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tapefiles' Line='tapefiles = "1-"' -->
  <dd>A range list of tape file numbers to read or list.  See the help topic
  <span style="font-family: monospace;">"ranges"</span> for information about the range list syntax.
  </dd>
  </dl>
  <dl id="l_listonly">
  <dt><b>listonly = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listonly' Line='listonly = no' -->
  <dd>List the specified tape files only?  If <span style="font-family: monospace;">"yes"</span> then no output files will
  be created and a short or long listing of each selected tape file will
  be printed to the standard output.  If both <i>shortlist</i> and
  <i>longlist</i> are <span style="font-family: monospace;">"no"</span> then the short listing will be produced.
  Note that a short listing is considerable faster than the long listing
  because only the first header needs to be read.
  </dd>
  </dl>
  <dl id="l_shortlist">
  <dt><b>shortlist = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shortlist' Line='shortlist = yes' -->
  <dd>List one line of information for each tape file?  This includes the the
  tape specification with position, the output file name if reading files,
  the stored original filename if present, the value of the NEXTEND keyword
  if present, and the value of the OBJECT keyword if present.
  </dd>
  </dl>
  <dl id="l_longlist">
  <dt><b>longlist = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='longlist' Line='longlist = no' -->
  <dd>List the short listing information plus additional information about each
  FITS header?  The information includes the extension index, extension type,
  extension name, BITPIX, and NAXIS values.
  </dd>
  </dl>
  <dl id="l_offset">
  <dt><b>offset = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='offset' Line='offset = 0' -->
  <dd>Offset for numbering of output disk filenames.  The output file name
  is the output rootname with four appended digits made from adding
  the offset and the tape position (which starts with 1).  The offset
  parameter is useful when not restoring the original filenames and when
  reading data from multiple tapes. 
  </dd>
  </dl>
  <dl id="l_original">
  <dt><b>original = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='original' Line='original = yes' -->
  <dd>Restore the original filename?  If a FILENAME or IRAFNAME keyword is
  found in the FITS file then when the file has been written to disk
  using the specified output name the output file is renamed to the
  original filename with a <span style="font-family: monospace;">".fits"</span> extension.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The specified tape files are either copied from tape to disk or just a
  summary listing is printed to the standard output.  The tape files are
  checked to make sure they appear to be FITS format (they must begin with a
  SIMPLE card) and then directly copied to disk without change if not simply
  listing.  Any FITS tape file can be read including multiextension files
  with any extension types.
  </p>
  <p>
  When reading the files to disk (<i>listonly</i>=no) the tape file is
  copied to a disk file with filename given by the output file root name,
  followed by a four digit number composed of the <i>offset</i> value plus
  the tape file position, and then with a <span style="font-family: monospace;">".fits"</span> extension.  If
  the <i>original</i> parameter is set and a FILENAME or IRAFNAME keyword
  is found the disk file is ultimately renamed to filename specified
  by those keywords.  If the desired original filename is already in use
  then a warning is given and the output file is not renamed.
  </p>
  <p>
  Summary information for the selected tape files may be written to
  the standard output whether or not a disk file is created.  A short
  listing includes the tape identification and the output filename
  (if creating an output file), the original file name if the FILENAME
  or IRAFNAME keyword is present, the value of the NEXTEND keyword if
  present, and the value of the OBJECT keyword if present.  The long
  list includes the short listing plus information from each FITS
  header unit.  This information consists of the extension index
  (0 for the primary header), and the values of the following keywords
  if present: XTENSION, EXTNAME, EXTVER, BITPIX, and NAXIS#.
  </p>
  <p>
  One common use of MSCRFITS is to list the contents of the tape.  This
  is done by setting the <i>listonly</i> parameter.  This turns off creating
  a disk file and forces at least the short listing.  Note that if
  just the short listing is selected the listing is most efficient since
  only the first header unit needs to be read.  The long listing
  requires the entire file to be read.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Read a set of files with the default short listing.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mscrfits mta data
  mta[1]  -&gt;  data0001.fits: abc     nextend=8 NGC ABC
      Rename data0001.fits -&gt; abc.fits
  mta[2]  -&gt;  data0002.fits: def     nextend=8 NGC DEF
      Rename data0002.fits -&gt; def.fits
  ...
  </pre></div>
  <p>
  2. List a tape with the default short listing.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mscrfits mta list+
  mta[1]: abc     nextend=8 NGC ABC
  mta[2]: def     nextend=8 NGC DEF
  ...
  </pre></div>
  <p>
  4. List a tape with the default short listing and save the listing in a file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mscrfits mta list+ &gt;&gt; fitslog
  </pre></div>
  <p>
  4. Read a set of Mosaic files with a long listing without restoring the
  original names.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mscrfits mta data tape=4,9,12 long+ original-
  mta[4]  -&gt;  data0004.fits: abc     nextend=8 NGC ABC
     0 PRIMARY
     1   IMAGE im1  16 2044x4096
     2   IMAGE im2  16 2044x4096
     3   IMAGE im3  16 2044x4096
     4   IMAGE im4  16 2044x4096
     5   IMAGE im5  16 2044x4096
     6   IMAGE im6  16 2044x4096
     7   IMAGE im7  16 2044x4096
     8   IMAGE im8  16 2044x4096
  mta[9]  -&gt;  data0009.fits: def     nextend=8 NGC DEF
     0 PRIMARY
     1   IMAGE im1  16 2044x4096
  ...
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MSCRFITS">
  <dt><b>MSCRFITS - V2.11 external package</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MSCRFITS' Line='MSCRFITS - V2.11 external package' -->
  <dd>First release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mscwfits
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

.. _mscwfits:

mscwfits: Write mosaic data to a FITS tape
==========================================

**Package: msctools**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  Mosaic data, in FITS format, as well as any other FITS format files are
  written to a FITS tape.  If a FILENAME keyword is present it is updated to
  the name of the disk file for use in later restoring the data with
  <b>mscrfits</b>.
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  mscwfits input output newtape
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of FITS files to write to tape.  This includes Mosaic multiextension
  FITS files as well as any other FITS format files.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output IRAF tape specification.  This may be a simple tape name, such
  as <span style="font-family: monospace;">"mta"</span>, or include additional specifiers.  A tape file number may be
  specified, e.g. mta[5] or mta[EOT], to position the tape otherwise the
  <i>newtape</i> parameter defines the starting position.  Note that
  specifying any position other than the next tape file number (the number of
  files on the tape plus one) or EOT will cause data to be clobbered if the
  tape file position is less than the next file or behave in an unspecified
  way if it is greater than the next file.  However, specifying the next tape
  file number is the most efficient way to skip to the end of tape to begin
  writing.
  </dd>
  </dl>
  <dl id="l_newtape">
  <dt><b>newtape</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newtape' Line='newtape' -->
  <dd>Is the tape a new or blank tape?  If <span style="font-family: monospace;">"yes"</span> and no file position
  is specified in the output tape name the FITS files will be written starting
  at the beginning of the tape.  If <span style="font-family: monospace;">"no"</span> and no file position  is specified
  the task will skip to the end of the tape to write the files.
  Note that this parameter is queried for if not given
  on the command line regardless of whether it is needed or not.
  </dd>
  </dl>
  <dl id="l_shortlist">
  <dt><b>shortlist = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shortlist' Line='shortlist = yes' -->
  <dd>List one line of information for each file written?  This includes the
  input filename, the tape specification with position, the filename
  stored in the FITS file for later restoration (the same as
  the input filename with path and extensions removed), the value of
  the NEXTEND keyword if present, and the value of the OBJECT keyword if
  present.
  </dd>
  </dl>
  <dl id="l_longlist">
  <dt><b>longlist = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='longlist' Line='longlist = yes' -->
  <dd>List the short listing information plus additional information about each
  FITS header?  The information includes the extension index, extension type,
  extension name, BITPIX, and NAXIS values.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A list of input FITS files are copied to tape.  The files are checked to
  make sure they appear to be FITS format (they must begin with a SIMPLE
  card) and then directly copied to the tape in FITS format blocking with a
  blocking factor of 10.  The only change made to the file is that if a
  FILENAME or IRAFNAME keyword is found then the value of the keyword is set
  to the input file name with any directory and extension removed.  Any FITS
  file can be written including multiextension files with any extension
  types.
  </p>
  <p>
  The files are written to the tape file position given by the output tape
  specification if one is given.  If only the tape name is given without
  a position specification then the files are either written to the beginning
  of the tape if <i>newtape</i> = yes or after the end of tape
  mark if <i>newtape</i> = no.
  </p>
  <p>
  A listing of the operations may be selected.  The listing information
  includes the input files and the tape position being written.  A short
  listing provides one line per input file written while the long listing
  includes additional lines for each FITS header block.  Keywords which
  will appear in the listing if found are NEXTEND and OBJECT in the
  first line and XTENSION, EXTNAME, EXTVER, BITPIX, and the NAXIS# in
  the long listing for each FITS header.  Note that there is no attempt
  to check that NEXTEND matches the actual number of extensions.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Write a set of files, given by an @file, to a new tape with the default
  short listing.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mscwfits @data1 mta yes
  abc.fits  -&gt;  mta[1]: abc     nextend=8 NGC ABC
  def.fits  -&gt;  mta[EOT]: def   nextend=8 NGC DEF
  ...
  </pre></div>
  <p>
  2. Write a set of Mosaic files, given by a wildcard template, to the end of
  a tape with the long listing.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mscwfits @data1 mta no long+
  efg.fits  -&gt;  mta[EOT]: efg   nextend=8 NGC EFG
     0 PRIMARY
     1   IMAGE im1  16 2044x4096
     2   IMAGE im2  16 2044x4096
     3   IMAGE im3  16 2044x4096
     4   IMAGE im4  16 2044x4096
     5   IMAGE im5  16 2044x4096
     6   IMAGE im6  16 2044x4096
     7   IMAGE im7  16 2044x4096
     8   IMAGE im8  16 2044x4096
  hij.fits  -&gt;  mta[EOT]: hij   nextend=8 NGC HIJ
  ...
  </pre></div>
  <p>
  3. Given that you know a tape has 40 files on it and you want to append
  to the file and save the listing information to a file:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mscwfits @data2 mta[41] no &gt;&gt; fitslog
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MSCWFITS">
  <dt><b>MSCWFITS - V2.11 external package</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MSCWFITS' Line='MSCWFITS - V2.11 external package' -->
  <dd>First release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mscrfits
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

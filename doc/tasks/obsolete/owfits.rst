.. _owfits:

owfits: Convert an IRAF image into a FITS image (dataio V2.10.4)
================================================================

**Package: obsolete**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  owfits iraf_files fits_files
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_iraf_files">
  <dt><b>iraf_files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='iraf_files' Line='iraf_files' -->
  <dd>String parameter specifying the input file(s), e.g. <span style="font-family: monospace;">"file1"</span> or <span style="font-family: monospace;">"file*"</span>.
  </dd>
  </dl>
  <dl id="l_fits_files">
  <dt><b>fits_files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fits_files' Line='fits_files' -->
  <dd>String parameter specifying the output destination.
  Magnetic tape output is assumed if the first two characters of fits_files
  are <span style="font-family: monospace;">"mt"</span>, otherwise the output destination defaults to disk.
  Tape output will begin at the file
  number specified in fits_files, e.g. file 5 if fits_files =
  <span style="font-family: monospace;">"mtb1600[5]"</span>. Data in file 5 and succeeding files will be overwritten.
  If no tape file number is specified in fits_files, the newtape parameter
  is requested. Tape output will begin at BOT (beginning of tape) if
  newtape = yes, otherwise at EOT (after the double EOF).
  Requesting a tape write at EOT on a blank tape may cause severe problems
  like tape runaway.
  In the case of disk output fits_files may be either a file name template
  or a root filename. In the former case there must be an output fits file
  name for every image. In the latter case the image sequence number is
  appended to fits_files if the number of input images &gt; 1.
  </dd>
  </dl>
  <dl id="l_newtape">
  <dt><b>newtape</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newtape' Line='newtape' -->
  <dd>Boolean parameter specifying whether an output tape is blank or contains
  data. Newtape is requested only if no tape file number is specified in
  fits_files, e.g. fits_files = <span style="font-family: monospace;">"mtb1600"</span>.
  </dd>
  </dl>
  <dl id="l_bscale">
  <dt><b>bscale</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bscale' Line='bscale' -->
  <dd>The FITS bscale parameter, defined as p = i * bscale + bzero, where
  p and i are the physical and tape data values respectively.
  The bscale parameter is only requested if the scale switch is set
  and the autoscale switch is turned off.
  </dd>
  </dl>
  <dl id="l_bzero">
  <dt><b>bzero</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bzero' Line='bzero' -->
  <dd>The FITS bzero parameter (see bscale for a definition).
  Bzero is only requested if the scale switch is set and the autoscale
  switch is turned off.
  </dd>
  </dl>
  <dl id="l_make_image">
  <dt><b>make_image = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='make_image' Line='make_image = yes' -->
  <dd>By default owfits writes the FITS image(s) to the output destination.
  If the make_image switch is turned off, owfits prints the FITS headers
  on the standard output and no output file is created. In this way the
  output FITS headers can be examined before actually writing a FITS tape.
  </dd>
  </dl>
  <dl id="l_long_header">
  <dt><b>long_header = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='long_header' Line='long_header = no' -->
  <dd>If this switch is set the full FITS header will be printed on the standard
  output for each IRAF image converted.
  </dd>
  </dl>
  <dl id="l_short_header">
  <dt><b>short_header = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='short_header' Line='short_header = yes' -->
  <dd>If this switch is set only a short header, listing files processed and
  their dimensions will be printed on the standard output.
  The long_header switch must be turned off.
  </dd>
  </dl>
  <dl id="l_bitpix">
  <dt><b>bitpix = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bitpix' Line='bitpix = 0' -->
  <dd>A bitpix of 8, 16, or 32 will produce either an unsigned byte,
  twos-complement 16 bit integer, or twos-complement 32 bit integer FITS
  image. If bitpix is -32 or
  -64 IEEE real or double precision floating point FITS images are produced.
  If bitpix is set to 0 (the default), owfits will choose one of 8,
  16, 32, -32 or -64 based on the data type of the IRAF image.
  For example a short integer and real image will default to bitpix 16 and 
  -32 respectively.
  Users should be wary or overriding the default value of bitpix as loss
  of precision in their data may result. In this case owfits will issue a
  warning message and an estimate of the maximum loss of precision to be
  expected.
  </dd>
  </dl>
  <dl id="l_blocking_factor">
  <dt><b>blocking_factor = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blocking_factor' Line='blocking_factor = 0' -->
  <dd>The tape blocking factor for FITS.
  Wfits normally writes <i>blocking_factor</i> * 2880 byte records,
  where <i>blocking_factor</i> is an integer from 1 to 10.
  If <i>blocking_factor</i> = 0, owfits uses the default FITS blocking
  factor specified for the device  by the <span style="font-family: monospace;">"fb"</span> parameter in the
  file dev$tapecap, or 1 if the <span style="font-family: monospace;">"fb"</span> parameter is not present. For
  devices which support variable block sizes, e.g. 9-track tapes, exabytes
  and dats, <span style="font-family: monospace;">"fb"</span> is normally set to 10.
  The user may override this value by setting <i>blocking_factor</i>
  &gt;= 1 or &lt;= 10. If the device does not support variable block sizes, e.g.
  various types of cartridge drives, blocks of the size defined for the
  device by the <span style="font-family: monospace;">"bs"</span> parameter in the dev$tapecap file are written
  and <i>blocking_factor</i> is ignored.
  </dd>
  </dl>
  <dl id="l_scale">
  <dt><b>scale = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='scale' Line='scale = yes' -->
  <dd>If the scale switch is set, the IRAF image will be scaled before output.
  Two types of scaling are available. The scaling parameters bscale and
  bzero may be entered by the user (autoscale = no), or the program can
  calculate the appropriate bscale and bzero factors (autoscale = yes).
  If the scale switch is turned off, the IRAF image data is converted
  directly to integers of the specified bitpix with possible loss of
  precision.
  </dd>
  </dl>
  <dl id="l_autoscale">
  <dt><b>autoscale = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='autoscale' Line='autoscale = yes' -->
  <dd>If the autoscale switch is set, owfits calculates the appropriate bscale and
  bzero  factors
  based on the IRAF image data type, and the maximum and minimum
  values of the data.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  IRAF data is read from disk and written to the specified destination,
  either disk or magnetic tape. The FITS header may optionally be printed
  on the standard output as either a full listing or a short description,
  with or without creating an output image file. If a the default value
  of bitpix (default = 0) is entered, owfits will select the appropriate
  bitpix value based on the precision of the IRAF data. Otherwise the
  user value is used with possible loss of precision. Two data scaling
  options are available. In autoscale mode owfits calculates the appropriate
  scaling factors based on the maximum and minimum data values in the
  IRAF image and the FITS bits per pixel. Alternatively the scaling factors
  can be entered directly. If no scaling is requested the IRAF data values
  will be converted directly to FITS integers or floating point values
  with possible loss of precision.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convert a series of IRAF image files to FITS image files on a blank
  magnetic tape, allowing owfits to select the appropriate bitpix
  and scaling parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; owfits iraf_file* mtb1600[1]
  </pre></div>
  <p>
  2. Convert a series of IRAF image files to FITS image files on disk,
  allowing owfits to select the appropriate bitpix and scaling parameters.
  In the first case the images specified by the template are written
  to fits001, fits002 etc. In the second case the list of input images
  specified one per line in the text file imlist are written to the
  files specified one per line in the text file fitslist.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; owfits iraf_file* fits
  
  cl&gt; owfits @imlist @fitslist
  </pre></div>
  <p>
  3. Convert an IRAF image file to a 32 bits per pixel FITS file with no
  scaling and append to a tape already containing data.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; owfits iraf_file mtb1600[EOT] bi=32 sc-
  </pre></div>
  <p>
  4. Convert an IRAF image to a 16 bit FITS image on disk, specifying
  bscale and bzero.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; owfits iraf_file fits_file bi=16 au- bs=4.0 bz=0.0
  </pre></div>
  <p>
  5. Print the FITS headers on the standard output.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; owfits iraf_file* ma-
  </pre></div>
  <p>
  6. Create a disk file called headers containing the FITS headers for a set
  of IRAF image files.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; owfits iraf_file* ma- &gt; headers
  </pre></div>
  <p>
  7. Write a FITS tape with 14400 bytes per record (5 2880 FITS records per
  tape block) on a 9-track tape.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; owfits images* mtb[1] block=5
  </pre></div>
  <p>
  8. Write a FITS Exabyte tape with a blocking factor of 1 (1 2880 FITS record
  per block). Note that owfits will normally by default write a 28000 (
  10 2880 FITS logical records per block) byte record.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; owfits images* mtb[1] block=1
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  OWFITS does not attempt to recover from write errors. When an error is
  detected, OWFITS issues an error message and attempts to write a double
  EOF at the end of the last good record. In this case the last file on
  the tape will be a partial file. IF OWFITS is not successful in writing
  the double EOF, the message <span style="font-family: monospace;">"Cannot close magtape file (name)"</span> will be
  issued. Problems occur as some drives permit the double EOF to be
  written after the physical end of tape and some do not. Similarly
  some drives can read a double EOF after end of tape and some cannot. Depending
  on operating system and device driver, an attempt to read or write past
  end of tape may or may not be distinguishable from a normal write error.
  </p>
  <p>
  Blank pixel values are not correctly handled.
  </p>
  <p>
  Attempting to write at EOT on a blank tape will at best result in numerous
  error messages being issued and at worst result in tape runaway depending
  on the driver.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  orfits, reblock
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

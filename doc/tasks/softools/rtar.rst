.. _rtar:

rtar: Read a TAR format archive file
====================================

**Package: softools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rtar [ flags ] [ archive ] [ after ] [ files ]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>-a</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-a' -->
  <dd>Advance to the archive file named by the <i>after</i> argument before
  performing the main operation.  The extract or list operation will begin with
  the file <i>after</i> and continue to the end of the archive.
  </dd>
  </dl>
  <dl>
  <dt><b>-b</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-b' -->
  <dd>Output only binary byte stream files.  By default, <i>rtar</i> outputs text
  files in the host system textfile format.  The conversion from the byte stream
  <i>tar</i> format to host textfile format may involve modification of the
  file, e.g., conversion from ASCII to EBCDIC.  A binary extraction copies
  the file to disk without modification.
  </dd>
  </dl>
  <dl>
  <dt><b>-d</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-d' -->
  <dd>Print detailed information about what <i>rtar</i> is doing.
  </dd>
  </dl>
  <dl>
  <dt><b>-e</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-e' -->
  <dd>Extract the entire contents of the tape <i>excluding</i> the files or directories
  listed in <i>files</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>-f filename</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-f filename' -->
  <dd><i>Rtar</i> uses the first filename argument as the host filename of the
  archive instead of reading from <i>stdin</i>.   Magtape devices should be
  specified using the host device name, e.g., <span style="font-family: monospace;">"/dev/nrmt8"</span> or <span style="font-family: monospace;">"MSA0"</span>.
  Since <i>rtar</i> is a host level program and does not read the IRAF tapecap
  file, IRAF device names such as <span style="font-family: monospace;">"mta"</span> cannot be used.
  </dd>
  </dl>
  <dl>
  <dt><b>-l</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-l' -->
  <dd>Do not try to resolve file links by a disk to disk file copy.  By default,
  if file A appears in the archive as a link to file B,
  <i>rtar</i> trys to resolve the link by performing a disk to disk copy of
  file B to A.  This is valid providing file B was present in the archive and
  has already been extracted.  If the <b>l</b> flag is present linked files
  will not be extracted.
  </dd>
  </dl>
  <dl>
  <dt><b>-m</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-m' -->
  <dd>Do not restore the file modify time.
  </dd>
  </dl>
  <dl>
  <dt><b>-n</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-n' -->
  <dd>Do not strip trailing blank lines from text files read from the tape.
  The default is to strip any blank lines at the ends of files.
  This is necessary when the file was written by <i>wtar</i> on a system
  like VMS, where the size of the file is not known before it has been
  read.  The <i>wtar</i> utility must guess at the final size and pad the
  file at the end with spaces to ensure that the size of the file actually
  written agrees with the file header.
  </dd>
  </dl>
  <dl>
  <dt><b>-o</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-o' -->
  <dd>Omit binary files when performing the extraction.  A binary file is any
  file containing ASCII values other than 040 through 0176 (the printable
  ASCII characters), tab, or newline in the first 512 byte block of the file.
  </dd>
  </dl>
  <dl>
  <dt><b>-p pathprefix</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-p pathprefix' -->
  <dd>When creating directories and files from the pathnames recorded in the archive,
  omit the given path prefix if it matches the pathname given in the archive.
  This feature is used to relocate directories, or to read tar archives
  containing absolute pathnames.  For example, given <span style="font-family: monospace;">"-p /usr/"</span>, the archive
  pathname <span style="font-family: monospace;">"/usr/me/file"</span> would be written to the file <span style="font-family: monospace;">"me/file"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>-r</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-r' -->
  <dd>The extracted file replaces any existing file of the same name, i.e.,
  <i>rtar</i> performs a delete before creating the extracted file.
  </dd>
  </dl>
  <dl>
  <dt><b>-t</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-t' -->
  <dd>The names of the specified files are listed each time they occur on
  the tape.  If no <i>files</i> argument is given, all of the names on the tape
  are listed.
  </dd>
  </dl>
  <dl>
  <dt><b>-u</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-u' -->
  <dd>Do not attempt to restore the owner and group identification of each file.
  </dd>
  </dl>
  <dl>
  <dt><b>-v</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-v' -->
  <dd>Print more information about the tape entries than just their names.
  The verbose file list format gives the file permissions, the link flag
  (zero if there were no links to the file), the owner and group identification
  numbers of the file on the system that wrote the archive, the file size in
  bytes, the date of last modification of the file, and the file name.
  </dd>
  </dl>
  <dl>
  <dt><b>-x</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-x' -->
  <dd>The named files are extracted from the tape.  If the named file
  matches a directory whose contents had been written onto the tape, this
  directory is (recursively) extracted.  The owner, modification time, and mode
  are restored (if possible).  If no file argument is given, the entire content
  of the tape is extracted.  Note that if multiple entries specifying the same
  file are on the tape, the last one overwrites all earlier.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Rtar</i> reads multiple files from a UNIX <i>tar</i> format file,
  restoring the files to disk on the local host machine.
  Output filenames are mapped according to the IRAF filenaming conventions
  of the local host operating system.
  </p>
  <p>
  <i>Rtar</i>'s actions are controlled by the <i>flags</i> argument. 
  <i>Flags</i> consists of a minus sign followed by a string of characters
  containing any combination of the function flags described below.
  Other arguments to <i>rtar</i> are the name of the archive file to be read,
  the name of the file on the archive at which reading is to begin,
  and the names of the files or directories to be read or to be excluded
  from the read.  In all cases, appearance of a directory name refers to
  the files and (recursively) subdirectories of that directory.
  </p>
  <p>
  All <i>rtar</i> filename arguments are IRAF virtual filenames (or host
  filenames), except the prefix strings, which pertain to the tape format and
  hence are UNIX pathnames.  Magtape devices must be specified using a host
  physical or logical device name (i.e., IRAF device names like <span style="font-family: monospace;">"mta"</span> will not
  work).
  </p>
  <p>
  If the input archive file is a tape the blocksize must be a multiple
  of 512 bytes, with a maximum blocksize of 10240 bytes.  Each archived file
  occupies an integral number of 512 byte blocks in the archive (this is
  required by the <i>tar</i> format).
  </p>
  <p>
  Filenames appearing in the file list are interpreted as prefix strings,
  i.e., a match occurs if the given string is a prefix of an actual filename
  in the archive.  If the last character in the <i>files</i> filename is
  a <b>$</b> then an exact match is required (excluding the $ meta-character).
  </p>
  </section>
  <section id="s_diagnostics">
  <h3>Diagnostics</h3>
  <p>
  A file read error occurring while reading the archive file is fatal unless
  caught and corrected by the host system.
  File header checksum errors result in skipping of the archive file
  currently being read, with execution continuing with the next archive
  file if possible.
  File write errors on the output file are reported but do not cause
  termination of <i>rtar</i>.  The output file being written will be corrupted.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Since <i>rtar</i> is a bootstrap utility implemented as a foreign task in
  the CL, it may be called either from within the CL (as in the examples),
  or at the host system level.  The command syntax is identical on both cases.
  </p>
  <p>
  1. List the contents of the disk archive file <span style="font-family: monospace;">"foo.tar"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rtar -tvf foo.tar
  </pre></div>
  <p>
  2. Unpack the tape archive on unix device /dev/nrmt8 in the current
  directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rtar -xf /dev/nrmt8
  </pre></div>
  <p>
  3. Unpack the tape archive on the VMS device MSA0: in the current
  directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rtar -xf msa0
  </pre></div>
  <p>
  When working within the CL, commands such as <i>rewind</i> may be used
  with <i>rtar</i>, but switching between IRAF and host device names may be
  confusing.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The current limit on file name length is 100 characters (this restriction
  is imposed by the standard UNIX <i>tar</i> format).
  File links are not recreated.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  wtar, rmbin
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'DIAGNOSTICS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

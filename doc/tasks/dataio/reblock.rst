.. _reblock:

reblock: Copy a binary file, optionally reblocking
==================================================

**Package: dataio**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  reblock infiles outfiles file_list
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_infiles">
  <dt><b>infiles  </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='infiles' Line='infiles  ' -->
  <dd>The input file list or device name, e.g. <span style="font-family: monospace;">"mta1600[2]"</span> or <span style="font-family: monospace;">"mta800"</span>, <span style="font-family: monospace;">"file1"</span>,
  <span style="font-family: monospace;">"file1,file2"</span>, or <span style="font-family: monospace;">"@infiles"</span>.
  </dd>
  </dl>
  <dl id="l_outfiles">
  <dt><b>outfiles  </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outfiles' Line='outfiles  ' -->
  <dd>The list of output files or device name, e.g. <span style="font-family: monospace;">"gemini!mtb"</span>, <span style="font-family: monospace;">"out1"</span>,
  <span style="font-family: monospace;">"out1,out2"</span>, or <span style="font-family: monospace;">"@outfiles"</span>.
  If multiple file output to disk is requested,  and the specified number
  of output files is 1, the output file names will be generated
  by concatenating the tape file number (the input files are on tape) or
  a sequence number (the input files are on disk) onto the output file
  name.
  </dd>
  </dl>
  <dl id="l_file_list">
  <dt><b>file_list</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file_list' Line='file_list' -->
  <dd>List of tape file numbers or ranges delimited by commas,
  e.g. <span style="font-family: monospace;">"1-3,5_8"</span>.
  File_list is requested only if the magtape input device is specified.
  Files will be read in ascending order regardless of the ordering of the list.
  Reading will terminate silently if EOT is reached, thus a list such as
  <span style="font-family: monospace;">"1-999"</span> may be used to read all files on the tape.
  </dd>
  </dl>
  <dl id="l_newtape">
  <dt><b>newtape  </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newtape' Line='newtape  ' -->
  <dd>If the output device is magtape, newtape specifies whether the tape is
  blank or contains data.
  Newtape is requested only if no tape file number is specified, e.g. <span style="font-family: monospace;">"mta1600"</span>.
  </dd>
  </dl>
  <dl id="l_outblock">
  <dt><b>outblock = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outblock' Line='outblock = INDEF' -->
  <dd>Size of the output block  bytes.
  In the  default case and for disk output, the output block size is set to the
  file i/o disk default buffer size.
  </dd>
  </dl>
  <dl id="l_inrecord">
  <dt><b>inrecord = INDEF, outrecord = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inrecord' Line='inrecord = INDEF, outrecord = INDEF' -->
  <dd>The sizes of the input and output logical records in bytes.
  The default input and output record sizes are set equal to
  the input and output block sizes respectively. If inrecord &gt; outrecord,
  records are trimmed; if inrecord &lt; outrecord, records are padded; if
  inrecord = outrecord, records are simply counted. If only one of inrecord or
  outrecord is set, the undefined parameter defaults to the value of the
  other.
  </dd>
  </dl>
  <dl id="l_skipn">
  <dt><b>skipn = 0    </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='skipn' Line='skipn = 0    ' -->
  <dd>The number of input blocks (tape input) or records (disk input, size inrecord)
  to be skipped.
  </dd>
  </dl>
  <dl id="l_copyn">
  <dt><b>copyn = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='copyn' Line='copyn = INDEF' -->
  <dd>The number of input blocks (tape input) or records
  (disk input, size inrecord) to be copied. Copyn defaults to a very large number.
  </dd>
  </dl>
  <dl id="l_byteswap">
  <dt><b>byteswap = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='byteswap' Line='byteswap = no' -->
  <dd>Swap every other byte. For example if byteswap is enabled, bytes 1 2 3 4 5 6
  would become bytes 2 1 4 3 6 5 on output.
  </dd>
  </dl>
  <dl id="l_wordswap">
  <dt><b>wordswap = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wordswap' Line='wordswap = no' -->
  <dd>Swap every 4 bytes. For example if byteswap is enabled, bytes 1 2 3 4 5 6 7 8
  would become 4 3 2 1 8 7 6 5 on output.
  </dd>
  </dl>
  <dl id="l_pad_block">
  <dt><b>pad_block = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pad_block' Line='pad_block = no' -->
  <dd>If pad_block is set, reblock pads trailing blocks until they are outblock
  bytes long, otherwise trailing blocks may be short.
  </dd>
  </dl>
  <dl id="l_padchar">
  <dt><b>padchar  = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='padchar' Line='padchar  = 0' -->
  <dd>Single character used to pad blocks or records.
  Padchar is only requested if pad_record or pad_block
  is set. If padchar equals one of the digits 0 through nine, records and
  blocks are padded with the face value of the character, otherwise the
  ASCII value is used.
  </dd>
  </dl>
  <dl id="l_offset">
  <dt><b>offset = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='offset' Line='offset = 0' -->
  <dd>The number which added to the tape file number is appended to <i>outfiles</i>
  to produce the output file name. For example if file_list = <span style="font-family: monospace;">"1-3"</span>, outfiles =
  <span style="font-family: monospace;">"out"</span> and offset = 100, the three files out101, out102, out103 would
  be produced rather than out001, out002 and out003.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes  </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes  ' -->
  <dd>Print messages about files, blocks copied etc.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  REBLOCK is a procedure to copy disk or tape resident files to
  disk or tape. Multiple input tape or disk files may be specified.
  If multiple files are output to disk, and only one output file name is
  specified, the output file names will be
  generated by concatenating the tape file number (the input files are on tape)
  or a sequence number (the input files are on disk) onto the output file name.
  The user may request magnetic tape output to begin at a specific file on
  tape, e.g. mta1600[5] in which case file five will be overwritten if it
  exists, or at BOT or EOT. If no file number is specified REBLOCK asks
  whether the tape is new or old and begin writing at BOT or EOT as
  appropriate.
  </p>
  <p>
  Before beginning the copy, the user may request reblock to skip
  n (default 0) blocks (tape input) or logical records (disk input).
  The user can also specify that
  only n (default all) blocks (tape input) or records (disk input)
  are to be copied. Before the copy the data may be optionally word-swapped
  (default no) and/or byte-swapped (default no). If verbose is specified
  (default yes) reblock prints the input and output file names,
  the number of blocks read and written and the number of records read and
  written.
  </p>
  <p>
  Reblock
  uses the default buffer sizes supplied by mtio and file i/o to determine the 
  maximum number of bytes which can be read in a single read call. For tapes
  this corresponds to the maximum number of bytes per block permitted by the
  device. Mtio will not read more than one block per read call. Therefore the
  actual number of bytes read will be less than or equal to the mtio buffer size.
  For disk files the default buffer size set by IRAF is a multiple of the
  disk block size. If the disk file is smaller than one block
  or the last block is partially full, the number of bytes read
  will be less than the default buffer size. All magtape and disk reads are
  done with the file i/o read procedure and a call to fstati determines the number
  of bytes actually read.
  </p>
  <p>
  If all the defaults are set, a binary copy is performed.
  In tape to tape copies the block and record sizes are preserved,
  but the density may
  be changed by specifying the appropriate output file name e.g. mta800 or
  mta1600.
  Reblocking occurs in tape to disk transfers, if records, are trimmed,
  padded or counted, or if blocks are padded.
  If a disk to tape transfer is requested
  the output block size will be the default file i/o  buffer size.
  The last block in a file may be short. If uniform sized blocks are
  desired, pad_block must be set, in which case trailing partially filled
  blocks will be padded with padchar.
  </p>
  <p>
  Logical records are distinguished from blocks (physical records).
  The input and output record sizes default to
  the size of the input and output blocks respectively.
  Logical records may be shorter or longer than the  block sizes.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Copy a magnetic tape preserving the record sizes but changing
  the density from 800 bpi to 1600 bpi.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; reblock mtb800 mta1600[1] 1-999
  </pre></div>
  <p>
  2. Reblock a magnetic tape changing the block size from 4000 bytes to 8000
  bytes and padding the last block.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; reblock mtb1600 mta1600[1] 1-999 outb=8000 padb+
  </pre></div>
  <p>
  3. Copy a series of disk fits files to tape
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; reblock @fitsfiles mta[1] outb=28800
  </pre></div>
  <p>
  4. Trim the records of a disk file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; reblock infile outfile inrec=80 outrec=72
  </pre></div>
  <p>
  5. Pad the records of a disk file with blanks.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; reblock input output inrec=81 outrec=82 padchar=" "
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  t2d
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

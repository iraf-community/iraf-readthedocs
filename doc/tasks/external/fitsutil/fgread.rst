.. _fgread:

fgread: Read a MEF file with FOREIGN extensions
===============================================

**Package: fitsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fgread input list output 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>Multiextension FITS file (MEF).
  </dd>
  </dl>
  <dl id="l_list">
  <dt><b>list</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='list' Line='list' -->
  <dd>List or range of extensions numbers to extract. To get a listing of the
  MEF file to find out the exact numbering, please use 'fgread extract=no'; this
  output listing is the one to use. Other listing like 'fxheader' should
  not be use since they will expand the MEF FILE, giving a larger running
  numbering.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of filenames to extract
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print information about each input file processed.
  </dd>
  </dl>
  <dl id="l_extract">
  <dt><b>extract = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extract' Line='extract = yes' -->
  <dd>Extract the listed extension from the input MEF
  </dd>
  </dl>
  <dl id="l_replace">
  <dt><b>replace = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='replace' Line='replace = yes' -->
  <dd>Replace existing files
  </dd>
  </dl>
  <dl id="l_types">
  <dt><b>types = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='types' Line='types = ""' -->
  <dd>Select input filenames by file type. The possible types are:
  <div class="highlight-default-notranslate"><pre>
  t: text
  b: binary
  d: directory
  s: symbolic link
  f: single FITS file
  m: Multiple Extension FITS file (MEF)
  
  </pre></div>
  The default value is to select all types.
  </dd>
  </dl>
  <dl id="l_exclude">
  <dt><b>exclude = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exclude' Line='exclude = ""' -->
  <dd>Exclude input filenames by file type. The file type are the same as above.
  Default action is to not exclude any type.
  </dd>
  </dl>
  <dl id="l_checksum">
  <dt><b>checksum = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='checksum' Line='checksum = no' -->
  <dd>Computes CHECKSUM and DATASUM. The default value is no. If the value is 'yes'
  the task looks for the keyword CHECKSUM and DATASUM and then calculates
  the checksum for the data portion and for the whole file and compares these
  values with the above mentioned keywords values.
  For the algoritm to calculate checksum, please see:
  <span style="font-family: monospace;">"ftp://iraf.noao.edu/misc/checksum/checksum.ps"</span>
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Fgread is the program to dearchive a MEF file created by fgwrite. Mainly
  FOREIGN extension are handled properly by filtering all the FG keyword
  and restoring the properties of the extracted file as close as possible
  to the original's.
  No count of the number of extensions is given, rather, the MEF group
  consist of all subsequent extensions until an EHU is encountered which
  starts a new file.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1) Restore extension 2 and 5 from the MEF file 'mef.fits'. First look at
  listing for the exact extension numbers.
  </p>
  <div class="highlight-default-notranslate"><pre>
  
  cl&gt; fgread mef.fits "" "" extract-
  cl&gt; fgread mef.fits 2,5 ""
  
  Notice the double quote symbols to indicate a null list of output
  files since we want to extract extension 2 and 5.
  
  </pre></div>
  <p>
  2) Extract 'log1.txt', 'log2.txt' and 'obs23.fits' extensions from the
  input MEF file.
  </p>
  <p>
     cl&gt; fgread mef.fits <span style="font-family: monospace;">""</span> log1.txt,log2.txt,obs23.fits
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fgwrite
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

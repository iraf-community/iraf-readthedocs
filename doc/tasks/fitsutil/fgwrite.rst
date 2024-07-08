.. _fgwrite:

fgwrite: Create a MEF file with FOREIGN extensions
==================================================

**Package: fitsutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fgwrite input output 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [string]' -->
  <dd>List of filenames to be archive in the output FITS file.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [string] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [string] ' -->
  <dd>Output Multiextension FITS file.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print information about each input file processed.
  </dd>
  </dl>
  <dl id="l_group">
  <dt><b>group = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='group' Line='group = ""' -->
  <dd>The value of the FITS keyword FG_GROUP. It applies to all the FITS
  extensions in the MEF file. Its default value is the name of the
  current working directory.
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
  <dl id="l_phu">
  <dt><b>phu = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='phu' Line='phu = yes' -->
  <dd>Creates a Primary header unit (PHU). This is just a dummy header unit with
  no data to comply with a regular MEF structure file. A value of 'no' will
  create a MEF file without a PHU.
  </dd>
  </dl>
  <dl id="l_checksum">
  <dt><b>checksum = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='checksum' Line='checksum = no' -->
  <dd>Computes CHECKSUM and DATASUM. The default value is no. If the value is 'yes'
  the task creates the keyword CHECKSUM with 
  the checksum for the entire FITS unit as value and DATASUM keyword with
  the checksum of the data portion of the unit as value. For a description
  and algorithm that calculates these values please look in:
  <span style="font-family: monospace;">"ftp://iraf.noao.edu/misc/checksum/checksum.ps"</span>
  </dd>
  </dl>
  <dl id="l_toc">
  <dt><b>toc = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='toc' Line='toc = no' -->
  <dd>Creates a table of content in the PHU. There is one line descriptor per
  input file. Here is a simple example:
  <div class="highlight-default-notranslate"><pre>
  
  Counter  offset size type level filename
    1       1      1   ft   1     m.c
    2       3      1   fb   1     t.o
  
  
  - 'offset' is the beginning of the extension header in units
     of 2880 bytes.
  - 'size' is the size of the input file in units of 2880 bytes.
  - 'type' is the input filename type. The 2 character pnemonic
     describes the kind of input file; <span style="font-family: monospace;">'f'</span> is for FOREIGN FITS
     Xtension type and the second character is the type define
     above in 'types' parameters description. If the input file
     is a MEF file the 'type' is one character: <span style="font-family: monospace;">'i'</span> IMAGE, <span style="font-family: monospace;">'t'</span>
     TABLE, <span style="font-family: monospace;">'b'</span> BINTABLE, <span style="font-family: monospace;">'f'</span> FOREIGN and <span style="font-family: monospace;">'o'</span> for OTHER FITS
     XTENSION types.
  - 'level' is the directory depth in which the input file is located.
  - 'filename' is the input filename.
  
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Fgwrite is a program to encapsulate one file into a
  wrapper FITS Xtension called FOREIGN. If the input
  list has more than one input file, a MEF (Mutiple Extension FITS) file is
  created with one FOREIGN extension per input file.
  </p>
  <p>
  To accurately describe the input file within the FOREIGN extension, a set
  of FG keywords is created in the extension header in such a way that
  an extraction of the file is possible with all its properties restore.
  </p>
  <p>
  The FG keyword present in the FOREIGN extension header are:
  </p>
  <dl id="l_FG_GROUP">
  <dt><b>FG_GROUP</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='FG_GROUP' Line='FG_GROUP' -->
  <dd>The group name that associates all of the elements of the MEF file. 
  The group name
  is arbitrary and is assigned by the user when the file group is written.
  </dd>
  </dl>
  <dl id="l_FG_FNAME">
  <dt><b>FG_FNAME</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='FG_FNAME' Line='FG_FNAME' -->
  <dd>The filename of the file associated with the current extension. The
  maximum filename lenght is 67 characters. For an extension of type
  foreign where the file type is a directory, FNAME is the name of the
  directory.
  </dd>
  </dl>
  <dl id="l_FG_FTYPE">
  <dt><b>FG_FTYPE</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='FG_FTYPE' Line='FG_FTYPE' -->
  <dd>The physical file type ('text', 'binary', 'directory', or 'symlink'),
  or for native FITS extension, the FITS type ('FITS' or 'FITS-MEF').
  In the case of FITS-MEF, the EHU is the first element of a MEF group.
  No count of the number of extensions is given, rather, the MEF group
  consist of all subsequent extensions until an EHU is encountered which
  starts a new file.
  </dd>
  </dl>
  <dl id="l_FG_LEVEL">
  <dt><b>FG_LEVEL</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='FG_LEVEL' Line='FG_LEVEL' -->
  <dd>The directory nesting level. All of the files in a directory are at the 
  same level. Level 1 is the root directory level.
  </dd>
  </dl>
  <dl id="l_FG_FSIZE">
  <dt><b>FG_FSIZE</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='FG_FSIZE' Line='FG_FSIZE' -->
  <dd>The size in bytes of the input disk file.
  </dd>
  </dl>
  <dl id="l_FG_FMODE">
  <dt><b>FG_FMODE</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='FG_FMODE' Line='FG_FMODE' -->
  <dd>The file mode as a string ('rwx-rwx-rwx').
  </dd>
  </dl>
  <dl id="l_FG_FUOWN">
  <dt><b>FG_FUOWN</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='FG_FUOWN' Line='FG_FUOWN' -->
  <dd>The file UID (user ID) as the file owner name string
  </dd>
  </dl>
  <dl id="l_FG_FUGRP">
  <dt><b>FG_FUGRP</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='FG_FUGRP' Line='FG_FUGRP' -->
  <dd>The file GID (group ID).
  </dd>
  </dl>
  <dl id="l_FG_CTIME">
  <dt><b>FG_CTIME</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='FG_CTIME' Line='FG_CTIME' -->
  <dd>The file creation GMT time. 
  </dd>
  </dl>
  <dl id="l_FG_MTIME">
  <dt><b>FG_MTIME</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='FG_MTIME' Line='FG_MTIME' -->
  <dd>The file modification GMT time.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Creates a MEF file 'mef.fits' with the default setup.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fgwrite file1.for,test.c,obs.log mef.fits
  </pre></div>
  <p>
  2. Create an archive of the current directory and its subdirectories
     excluding any symbolic links.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; fgwrite . ../zzd_arc.fits exclude=s checksum=yes
  </pre></div>
  <p>
  The ckecksum option is set, so the keyword CHECKSUM, DATASUM and
  CHECKVER will be present in all unit headers.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  fgread
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

.. _wtar:

wtar: Write a TAR format archive file
=====================================

**Package: softools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  wtar [-flags] [-f archive] [files]
  </p>
  </section>
  <section id="s_arguments">
  <h3>Arguments</h3>
  <dl>
  <dt><b>-d</b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='' Line='-d' -->
  <dd>Print debug messages.
  </dd>
  </dl>
  <dl>
  <dt><b>-o</b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='' Line='-o' -->
  <dd>Omit binary files.
  </dd>
  </dl>
  <dl>
  <dt><b>-t</b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='' Line='-t' -->
  <dd>Print the name of each file as it is written or omitted.
  </dd>
  </dl>
  <dl>
  <dt><b>-v</b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='' Line='-v' -->
  <dd>Verbose mode; print more information about each file.
  </dd>
  </dl>
  <dl>
  <dt><b>-f archive</b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='' Line='-f archive' -->
  <dd>The tar format file to be written, i.e., <span style="font-family: monospace;">"stdout"</span>, a host magtape device
  name (e.g., <span style="font-family: monospace;">"/dev/nrmt8"</span> or <span style="font-family: monospace;">"MSA0"</span>), or the IRAF virtual filename of a disk
  file.  The default is the standard output.
  </dd>
  </dl>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='ARGUMENTS' Level=0 Label='files' Line='files' -->
  <dd>The names of the files or root directories of directory trees to be written
  to the archive file.  If no files are specified <span style="font-family: monospace;">"."</span> (the directory tree
  rooted at the current directory) is assumed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The named files and directories are written to the indicated
  UNIX <span style="font-family: monospace;">"tar"</span> format output file.  Any directories in the file list are
  recursively descended.  The named directories should be subdirectories of
  the current directory when <i>wtar</i> is called.  Binary files may be
  omitted if desired, e.g., when transporting software to a different host, or
  when making a backup of a large system which would otherwise exceed the
  capacity of a single reel of tape.  All file, directory, and magtape names
  conform to the IRAF standard.
  </p>
  <p>
  The output file is normally either a disk file (e.g., if the transport
  medium is an electronic network), or a magtape file.  If the output file is
  a magtape multiple files, i.e., wtar archives, may be written on the tape.
  The blocking factor is fixed at 10240 bytes per record.
  </p>
  <p>
  The TAR format file written by <i>wtar</i> conforms to the UNIX standard except
  that [1] no link information is preserved, [2] the user and group numbers
  may not be preserved (they are preserved in the UNIX version of <i>wtar</i>),
  and [3] some versions of <i>wtar</i> (e.g., VMS) pad text files at the end
  with extra blank lines.
  </p>
  <p>
  All <i>wtar</i> filename arguments are IRAF virtual filenames (or host
  filenames).  Magtape devices should be specified by their host (not IRAF)
  device name, e.g., <span style="font-family: monospace;">"/dev/nrmt8"</span> or <span style="font-family: monospace;">"MSA0"</span>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Make a source-only archive of the IRAF system on the UNIX device
  /dev/nrmt8.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cd iraf
  cl&gt; wtar -of /dev/nrmt8
  </pre></div>
  <p>
  2. Archive the <span style="font-family: monospace;">"uparm"</span> directory to the VMS logical device MSA0:.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wtar -f msa0 uparm
  </pre></div>
  <p>
  3. Make a disk archive of the LIB and PKG directory trees in your home
  directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wtar -f home$archive.tar lib pkg
  </pre></div>
  <p>
  4. Examine the resultant file to make sure everything worked correctly.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rtar -tvf home$archive.tar
  </pre></div>
  <p>
  5. Make a disk archive, using a host filename for the output file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; wtar -f /tmp2/arc lib pkg sys
  </pre></div>
  <p>
  IRAF magtape commands such as <i>rewind</i> may be used with <i>wtar</i>,
  but switching between IRAF and host device names can be confusing.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rtar, rmbin
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'ARGUMENTS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

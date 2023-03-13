.. _directory:

directory: List the files in a directory
========================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  directory [files]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files' -->
  <dd>A file template specifying the files to be listed, or the name of the directory
  whose contents are to be listed.  If omitted entirely, the contents of the
  current directory are listed.
  </dd>
  </dl>
  <dl id="l_long">
  <dt><b>long = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='long' Line='long = no' -->
  <dd>Long format listing.  The long format listing lists each file on a separate
  line, noting the file permissions, file type, file size, modify date, owner,
  etc. of each file.
  </dd>
  </dl>
  <dl id="l_ncols">
  <dt><b>ncols = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncols' Line='ncols = 0' -->
  <dd>If nonzero, the number of columns of output in multicolumn format.
  </dd>
  </dl>
  <dl id="l_maxch">
  <dt><b>maxch = 18</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxch' Line='maxch = 18' -->
  <dd>The maximum number of characters to be displayed in each filename.
  Truncation may be desirable when listing a directory containing one or two
  files with very long filenames.
  </dd>
  </dl>
  <dl id="l_sort">
  <dt><b>sort = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sort' Line='sort = yes' -->
  <dd>Sort the file list alphabetically.  If sorting is disabled the directory
  program lists the files in the order in which they are read from the
  directory, which may or may not be sorted.  The directory listing is produced
  line by line as files are read from the directory, rather than accumulating
  the entire file list in memory before composing the table, hence this is the
  fastest method of listing a directory, particularly if the directory is very
  large.
  </dd>
  </dl>
  <dl id="l_all">
  <dt><b>all = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='all' Line='all = no' -->
  <dd>List all files, including the hidden (<span style="font-family: monospace;">"."</span> prefixed) files, and files with
  reserved filename extensions used internally by the VOS.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <b>directory</b> task lists or prints information describing some subset
  of the files in a directory or directories.  If no name template is given,
  <span style="font-family: monospace;">"."</span> is assumed, i.e., all files in the current directory are listed.
  </p>
  <p>
  The long format listing gives a file type string, followed by
  the name of the owner of the file, the file size, date and time at which
  the file was last modified, and lastly the file name.
  The file type string has fields noting if the file is a directory file (d),
  an executable file (x), a text or binary file (t or b), a protected file (p),
  and summarizing the file permissions (read or write, r or b) for the owner,
  the group, and the rest of the world.  A minus sign indicates that the file
  does not have that particular attribute.
  </p>
  <p>
  All file names are printed in the IRAF virtual filename syntax, which is the
  same on all host machines.  IRAF filenames may be up to 32 characters in
  length, may contain any combination of alphanumeric characters, underscore,
  or period, and are case sensitive.  Some of the common filename extensions
  are listed below; these are mapped to and from the host filename extensions
  when a file is accessed, a directory is listed, or a filename template is
  expanded.
  </p>
  <div class="highlight-default-notranslate"><pre>
  .a      object library
  .c      C source file
  .cl     CL source file
  .e      executable (runnable) file
  .f      Fortran source file
  .gX     generic source file (X=[cx])
  .h      global header file
  .hlp    help file
  .o      object file
  .par    CL parameter file
  .s      assembler source file
  .x      SPP source file
  </pre></div>
  <p>
  When listing large directories, the time required to accumulate and sort the
  entire directory in memory before producing the output listing may become
  significant (i.e., more than a few seconds).  If this happens, try setting
  the <i>sort</i> option to <i>no</i>, and the directory listing should appear
  immediately.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List all the files in the current directory in tabular format.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dir
  </pre></div>
  <p>
  2. Print detailed information on all files in the current directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dir l+
  -t-rwr-r- iraf         269 Oct 16  1983 README
  dt-rwrwr- iraf        1024 Feb  7 12:48 doc
  -t-rwr-r- iraf          60 Jan 30  1984 files.par
  -t-rwr-r- iraf         420 Jan 30  1984 files.x
  -b-rwrwr- system    187338 Jan 29 19:27 libpkg.a
  xb-rwr-r- iraf      363520 Jan 29 19:29 x_system.e
  -b-rwrwr- system      5037 Jan 19 22:15 x_system.o
  -t-rwr-r- iraf         633 Jan 19 22:01 x_system.x
  </pre></div>
  <p>
  3. Print a single column listing of all the files with extension <span style="font-family: monospace;">".h"</span>
  in the logical directory <span style="font-family: monospace;">"lib$"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dir lib$*.h l+
  lib$chars.h
  lib$clio.h
  lib$clpopn.h
      (etc)
  </pre></div>
  <p>
  4. While in the <span style="font-family: monospace;">"system"</span> directory, print the contents of the parallel
  directory <span style="font-family: monospace;">"dataio"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cd pkg$system
  cl&gt; dir ../dataio
  </pre></div>
  <p>
  5. Test if the file <span style="font-family: monospace;">"alpha"</span> exists in the current directory.  In the example,
  the output given indicates that the file was not found.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dir alpha
  no files found
  </pre></div>
  <p>
  6. Print the contents of the directory USR$2:[IRAF.LOCAL] on the remote VMS
  node <span style="font-family: monospace;">"draco"</span> (requires IRAF network access to the remote node).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dir draco!usr\$2:\[iraf.local]
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  There is no provision for wildcarding directories, e.g., <span style="font-family: monospace;">"dir */*.x"</span>.
  The long format listing can currently only be sorted by filename (although
  the <i>sort</i> program may be used in a pipe).  The file existence test will
  not be performed if individual files are named as list elements within
  a filename template.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  files, pathnames
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

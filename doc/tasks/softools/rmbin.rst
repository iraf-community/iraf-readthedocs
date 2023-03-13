.. _rmbin:

rmbin: Find/delete binary files in subdirectories
=================================================

**Package: softools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rmbin [-dinrv] [-o extns] [-e extns] dir1 dir2 ... dirN
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>-d</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-d' -->
  <dd>Disable recursive descent into subdirectories.
  </dd>
  </dl>
  <dl>
  <dt><b>-e extns</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-e extns' -->
  <dd>Exclude files with the listed extensions (whitespace delimited).
  </dd>
  </dl>
  <dl>
  <dt><b>-i</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-i' -->
  <dd>Verify before deleting files without extensions.  Files with well known
  extensions like <span style="font-family: monospace;">".[aoe]"</span> are deleted without a query.  A heuristic (ZFACSS)
  is used to determine the filetype of files with unknown extensions, and
  it can fail, though in practice it works quite well.
  </dd>
  </dl>
  <dl>
  <dt><b>-n</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-n' -->
  <dd>No execute; do not delete files.  This option may be used to generate
  a list of binary files for some purpose other than deletion.  For example,
  on a UNIX host, the following command will compute the disk space used
  by the binary files in a directory tree:
  	% du `rmbin -n .`
  The -n option, of course, is also useful for verifying the delete operation
  before destroying the files.
  </dd>
  </dl>
  <dl>
  <dt><b>-o extns</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-o extns' -->
  <dd>Delete only files with the listed extensions (whitespace delimited).
  </dd>
  </dl>
  <dl>
  <dt><b>-r</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-r' -->
  <dd>Reenable recursive descent.  Recursive descent is the default, however
  it may be turned off at one point in the command line, and later reenabled
  with this switch.
  </dd>
  </dl>
  <dl>
  <dt><b>-v</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='-v' -->
  <dd>Print names of files as they are deleted.
  </dd>
  </dl>
  <p>
  Note that flags may be inserted between directory name arguments to change
  switches for different directories.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>rmbin</i> task is used to descend a directory tree, deleting (or listing)
  all the binary files therein.  The task may also be used to delete or list
  nonbinary files by explicitly listing their extensions.
  </p>
  <p>
  <i>Rmbin</i> is used the strip the IRAF system down to the sources, prior to
  a full system rebuild.  After changing to the IRAF root directory, one runs
  <i>rmbin</i> to delete all the binaries in lib, sys, pkg, etc. (but <i>not</i>
  in hlib, else a bootstrap will be necessary too).  <i>Mkpkg</i> is then run
  to recompile the system; this currently takes about 20 hours on our UNIX
  11/750 development system, provided nothing else is running on the system.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Delete all binaries in the pkg and sys directories of IRAF.  The example
  is for a UNIX host, but this works for all other IRAF hosts as well.
  </p>
  <div class="highlight-default-notranslate"><pre>
  % cd $iraf
  % rmbin -v pkg sys
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rtar, wtar, mkpkg
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

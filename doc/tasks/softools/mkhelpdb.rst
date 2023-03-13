.. _mkhelpdb:

mkhelpdb: Make (compile) a help database
========================================

**Package: softools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkhelpdb helpdir helpdb
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_helpdir">
  <dt><b>helpdir = <span style="font-family: monospace;">"lib$root.hd"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='helpdir' Line='helpdir = "lib$root.hd"' -->
  <dd>The filename of the root help directory file (<span style="font-family: monospace;">".hd"</span> file) defining the
  help tree to be updated.  By convention this is <i>root.hd</i> in some
  directory.
  </dd>
  </dl>
  <dl id="l_helpdb">
  <dt><b>helpdb = <span style="font-family: monospace;">"lib$helpdb.mip"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='helpdb' Line='helpdb = "lib$helpdb.mip"' -->
  <dd>The filename of the help database file to be written.  By convention this
  is <i>helpdb.mip</i> in some directory (the <span style="font-family: monospace;">".mip"</span> signifies that the file
  format is machine independent).
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>If this switch is enabled, <i>mkhelpdb</i> will print a detailed description
  of the help database as it is being compiled.  A more concise summary listing
  only the packages and the number of help modules in each package is printed
  by default.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>mkhelpdb</i> task descends a tree of help directory (<span style="font-family: monospace;">".hd"</span>) files and
  compiles a binary help database from the information therein.  The help
  database is used to speed global searches when help is requested for a
  module, the <span style="font-family: monospace;">".hlp"</span> file for which might be anywhere in the system.
  The help database defines the packages and modules in the help database,
  and stores the filenames of the associated help files.  No actual help text
  is stored in the help database, only sufficient index information to find
  the help files when the <i>help</i> task is run.  The help directory files
  are text files which define the packages and modules in the help database.
  The format of these files is self explanatory hence is documented by example
  only.
  </p>
  <p>
  By default, <i>mkhelpdb</i> recompiles the standard IRAF help database,
  although any other similar database may be recompiled by changing the values
  of the parameters <i>helpdir</i> and <i>helpdb</i>.  The standard
  IRAF help database is rooted in the file <b>lib$root.hd</b>.
  </p>
  <p>
  The help database must be updated whenever a new help module (e.g., manual
  page) is added, deleted, or renamed.  It is also necessary for sites receiving
  a source only version of IRAF to run <i>mkhelpdb</i> to rebuild the help
  database once the system is up, since the database is a binary file and
  is not included in a source only distribution.  It is not necessary to rerun
  <i>mkhelpdb</i> when an existing manual page is edited, since only index
  information is stored in the database.
  </p>
  <p>
  The <i>help</i> utilities make use of the following types of files.  Examples
  of these files will be found throughout the IRAF directories.
  </p>
  <div class="highlight-default-notranslate"><pre>
  .hd             help directory file (tree structured)
  .hlp            manual page
  .men            package menu (module listing)
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Update the standard IRAF help database.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; softools
  so&gt; mkhelpdb helpdir=lib$root.hd helpdb=lib$helpdb.mip
  </pre></div>
  <p>
  2. Update the NOAO package help database.
  </p>
  <div class="highlight-default-notranslate"><pre>
  so&gt; mkhelpdb helpdir=noao$lib/root.hd helpdb=noao$lib/helpdb.mip
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  hdbexamine, help
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

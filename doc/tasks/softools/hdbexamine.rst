.. _hdbexamine:

hdbexamine: Examine a help database
===================================

**Package: softools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  hdbexamine
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_helpdb">
  <dt><b>helpdb = <span style="font-family: monospace;">"helpdb"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='helpdb' Line='helpdb = "helpdb"' -->
  <dd>The filename of the help database to be examined.  The reserved name <span style="font-family: monospace;">"helpdb"</span>
  causes the actual filename to be taken from the environment variable of
  the same name.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>If this switch is enabled, <i>hdbexamine</i> will print a detailed description
  of the help database listing the modules in each package, the date the entry
  for the package was last modified, and other information.  A more concise
  summary listing only the packages and the number of help modules in each
  package is printed by default.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>hdbexamine</i> task is used to examine the contents of a help
  database.  By default the standard IRAF help database is examined.
  Examining the help database with <i>hdbexamine</i> verifies that it can
  be read by <i>help</i>, and may be useful as a diagnostic in the event
  that an invalid help directory file (<span style="font-family: monospace;">".hd"</span>) somewhere in the help
  directory tree, causes the database to be compiled incorrectly.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print a concise summary of the contents and structure of the standard
  help database.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hdbexamine
  Help database dev$help.db created Feb 14 21:34 by tody
  Database contains 794 modules in 43 packages, file size 105460 bytes
  
  _clpackage   Nov  4  1984 tody     clpackage$_clpackage.hd
  clpackage    May 29 17:44 rooke    clpackage$clpackage.hd
  os           Feb 13 11:06 tody     host$os/doc/os.hd
  root         Nov  4  1984 tody     lib$root.hd
  _math        Apr  1 13:38 tody     math$_math.hd
  curfit       Jan  6 16:23 tody     math$curfit/doc/curfit.hd
  gsurfit      Jan  2 14:46 davis    math$gsurfit/doc/gsurfit.hd
  iminterp     Aug  6 16:31 davis    math$iminterp/doc/iminterp.hd
  bias         Dec 17  8:53 valdes   pkg$imred/bias/bias.hd
  coude        Dec 31 14:38 valdes   pkg$imred/coude/coude.hd
  vtel         Jan 22  8:36 lytle    pkg$imred/vtel/vtel.hd
  plot         Jan 28 14:04 hammond  pkg$plot/plot.hd
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mkhelpdb, help
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

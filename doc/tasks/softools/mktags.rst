.. _mktags:

mktags: Tag all procedure declarations in a set of files
========================================================

**Package: softools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mktags
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_files">
  <dt><b>files = <span style="font-family: monospace;">"*.x"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='files' Line='files = "*.x"' -->
  <dd>The files to be tagged, e.g., <span style="font-family: monospace;">"*.x"</span>.
  </dd>
  </dl>
  <dl id="l_listing">
  <dt><b>listing = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listing' Line='listing = no' -->
  <dd>If this switch is enabled a sorted list of all procedures declared in the
  set of files will be printed on the standard output, giving the procedure
  name, line and file number, and procedure declaration on each output line.
  </dd>
  </dl>
  <dl id="l_tags">
  <dt><b>tags = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tags' Line='tags = yes' -->
  <dd>If this switch is enabled a <span style="font-family: monospace;">"tags"</span> file will be written in the current
  directory for use with the VI editor.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The named files are scanned for procedure declarations.  Each such declaration
  found is buffered internally.  When all files have been scanned the internal
  tag database is sorted and the output files are generated.  Two types of
  output are provided:
  </p>
  <dl>
  <dt><b></b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line=' ' -->
  <dd><dl>
  <dt><b>[1]</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='[1]' -->
  <dd>A summary of all procedures defined in the given set of files may be printed
  on the standard output.  This output may be used as a printed index to manually
  find procedures in the given file set.
  </dd>
  </dl>
  <dl>
  <dt><b>[2]</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='[2]' -->
  <dd>A <span style="font-family: monospace;">"tags"</span> format database file (a text file) may be written.  This file is
  read by the VI editor when a command of the form <span style="font-family: monospace;">":ta tag"</span> is entered.
  This command is used to edit procedures regardless of the file in which they
  reside.  For example, to edit procedure <span style="font-family: monospace;">"maxmin"</span>, enter command <span style="font-family: monospace;">":ta maxmin"</span>
  when in VI.
  </dd>
  </dl>
  </dd>
  </dl>
  <p>
  By default the operation of <i>mktags</i> is to silently update the tags
  database.  If a printed listing is desired the <i>listing</i> switch must
  be enabled.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  A fixed amount of storage is allocated internally and overflow will occur if
  there are too many tags (procedures) or if there is too much text (the string
  buffer will overflow).
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'BUGS' 'SEE ALSO'  -->
  

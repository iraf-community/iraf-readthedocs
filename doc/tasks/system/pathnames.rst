.. _pathnames:

pathnames: Expand a file template into a list of OS pathnames
=============================================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pathnames [template]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_template">
  <dt><b>template</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='template' Line='template' -->
  <dd>A filename template specifying the set of files for which pathnames
  are desired.  If omitted, the pathname of the current working or default
  directory is printed.  The list of file names can come from the standard input.
  </dd>
  </dl>
  <dl id="l_sort">
  <dt><b>sort = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sort' Line='sort = yes' -->
  <dd>Sort the output in ASCII collating sequence.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Pathnames</i> converts a list of IRAF virtual file names into their host
  system equivalents.  When called with no arguments, the function of
  <i>pathnames</i> is to print the current default directory.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print the pathname of the current default directory (sample output for
  a VMS host system).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; path
  draco!DRB1:[IRAF.SYS.FIO]
  </pre></div>
  <p>
  2. Translate the file <span style="font-family: monospace;">"vfiles"</span>, containing a list of virtual filenames, into
  the equivalent list of host system filenames, e.g., for use as input to a
  foreign task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; path @vfiles &gt; hfiles
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  directory, files
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

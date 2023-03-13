.. _mkttydata:

mkttydata: Build cache for termcap/graphcap device entries
==========================================================

**Package: softools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkttydata devices termcap_file output_file
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_devlist">
  <dt><b>devlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='devlist' Line='devlist' -->
  <dd>A comma delimited list of the devices whose termcap or graphcap entries
  are to be compiled.
  </dd>
  </dl>
  <dl id="l_termcap_file">
  <dt><b>termcap_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='termcap_file' Line='termcap_file' -->
  <dd>The name of the termcap or graphcap file be searched, e.g., <span style="font-family: monospace;">"dev$termcap"</span>,
  or <span style="font-family: monospace;">"dev$graphcap"</span>.
  </dd>
  </dl>
  <dl id="l_output_file">
  <dt><b>output_file</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output_file' Line='output_file' -->
  <dd>The name of the output file to be written, an SPP include file containing
  a number of declarations and data initialization statements.
  This should be <span style="font-family: monospace;">"dev$cachet.dat"</span> if the standard termcap is being compiled,
  and <span style="font-family: monospace;">"dev$cacheg.dat"</span> if the standard graphcap is being compiled.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Causes a message to be printed for each device entry compiled.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>mkttydata</i> task is used by the IRAF system manager to precompile
  the <i>termcap</i> or <i>graphcap</i> entries for commonly used video or
  graphics terminals.  This can be advantageous on slow systems since otherwise
  the termcap or graphcap file must be searched at runtime every time the
  screen is cleared or a graph is plotted, reducing the performance and
  interactive response of the system.  Since each IRAF site will commonly use
  a different set of devices, entries can only be cached by the local system
  manager after the system is installed.  [NOTE, Jun 1990: the above is
  still true, but with the addition of features such as shared libraries and
  multiple architecture support to some versions of IRAF, relinking IRAF is
  more difficult and it is easier to make mistakes.  Furthermore, modern
  systems are getting very fast.  For most sites it will be easier, and safer,
  to merely copy frequently referenced device entries to the head of the
  termcap or graphcap file and skip the sysgen.]
  </p>
  <p>
  The input to <i>mkttydata</i> consists of a list of devices and a reference
  to either the termcap or graphcap file.  The output is an SPP include file
  which is referenced by the procedures in the TTY package.  After updating
  the cache files, a full system sysgen is required to recompile the affected
  modules, update them in the system libraries, and relink all executables.
  </p>
  <p>
  Enter the following values for the <i>termcap_file</i> and <i>output_file</i>
  parameters to build the termcap and graphcap cache files.  Note that for
  caching to work the value of <i>termcap_file</i> must match that of
  the <i>termcap</i> or <i>graphcap</i> environment variable, hence do not
  enter <span style="font-family: monospace;">"graphcap"</span> rather than <span style="font-family: monospace;">"dev$graphcap"</span>, just because you happen to
  be in the dev directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
                  <i>termcap_file</i>     <i>output_file</i>
  
  termcap         dev$termcap     dev$cachet.dat
  graphcap        dev$graphcap    dev$cacheg.dat
  </pre></div>
  <p>
  After updating these files, perform a sysgen-relink to update the
  system libraries and relink all executables (this takes a while, and
  requires IRAF permissions and full sources).  Instructions for performing
  the sysgen-relink are given in the <i>Site Manager's Guide</i> for your
  IRAF system.  The exact procedure for performing a sysgen-relink depends
  upon the host system.  In particular, if the system support multiple
  architectures, each architecture must be restored and relinked separately.
  Note that systems configured for multiple architecture support are
  shipped configured <span style="font-family: monospace;">"generic"</span>, and you must restore an architecture before
  relinking or the entire IRAF system will be recompiled (which is time
  consuming, and inadvisable due to the possibility of system or compiler
  differences introducing bugs into IRAF).
  </p>
  <p>
  After this finishes, log out and back in and you should notice the
  difference when running tasks like <i>page</i>, <i>clear</i>, and <i>implot</i>.
  </p>
  <p>
  Note that once a device entry is cached it cannot be modified without
  going through this all over again, while if the entry is not cached it
  can be edited and the new entry used immediately.  It is therefore not
  desirable to cache new termcap or graphcap entries until they have stopped
  changing.  Even after a device entry has been cached, however, it is possible
  to test new entries by changing the entry name, or by changing the value
  of the <i>termcap</i> or <i>graphcap</i> environment variable.  If these
  values are different than they were when the entries were cached, the cached
  entries will not be used, even if the device name matches that of a cached
  entry.
  </p>
  <p>
  For additional information on graphcap see the <span style="font-family: monospace;">"GIO Design"</span> document.
  For additional information on termcap see the Berkeley UNIX <span style="font-family: monospace;">"Programmer's
  Guide: Reference Manual"</span>, section 5.  IRAF uses a standard UNIX termcap.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Update the graphcap cache.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mktty vt640,vt240,4012,cit414a dev$graphcap dev$cacheg.dat
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  There is a fixed limit on the amount of data that can be cached.
  If the limit is exceedd the affected TTY modules will fail to compile.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  showcap, IRAF Site Manager's Guide
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

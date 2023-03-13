.. _dematch:

dematch: Match a list of density values to exposure values
==========================================================

**Package: dtoi**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  dematch database 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>Database containing density list, probably from <i>spotlist</i>.
  </dd>
  </dl>
  <dl id="l_wedge">
  <dt><b>wedge = <span style="font-family: monospace;">""</span>, filter = <span style="font-family: monospace;">""</span>, emulsion = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wedge' Line='wedge = "", filter = "", emulsion = ""' -->
  <dd>Information used to retrieve log exposure values from <b>wedgefile</b>.
  </dd>
  </dl>
  <dl id="l_wedgefile">
  <dt><b>wedgefile = <span style="font-family: monospace;">"noao$lib/hdwedge.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wedgefile' Line='wedgefile = "noao$lib/hdwedge.dat"' -->
  <dd>Name of file containing wedge intensity information.
  </dd>
  </dl>
  <dl id="l_nskip">
  <dt><b>nskip = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nskip' Line='nskip = 0' -->
  <dd>Number of faint spots skipped, used as an offset into the list of
  log exposure values.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print the log exposure information to STDOUT as well as to <b>database</b>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <i>dematch</i> matches density values to log exposure values.  A database
  of density values is input, as well as information needed to 
  retrieve log exposure values from a reference file.  The two sources of 
  information are matched, and the matching log exposure values are added 
  as a record in the database.
  </p>
  <p>
  Parameter <b>nskip</b> tells how many faint spots were not
  included in the density <b>database</b>.  This information is
  used to align the density, exposure values.  It doesn't matter if the 
  densities are listed in a monotonically increasing or decreasing
  order, as long as no spots were omitted between the first and last
  measured.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Match densities in db1 to log exposure values for wedge#117
  with a IIIAJ emulsion and a GG385 filter.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dematch db1 wedge=117 filt=gg385 emulsion=IIIAJ
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  spotlist, hdfit, hdtoi
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

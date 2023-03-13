.. _afiltcat:

afiltcat: Filter astrometry files derived from astrometric catalogs
===================================================================

**Package: astcat**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  afiltcat input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The list of input astrometry files. Astrometry files may be created by
  other astcat tasks, e.g. agetcat, in which case they are preceded by a
  header describing the format of the input astrometry file, or by
  other IRAF or user tasks in which case the <i>acatpars</i> parameter set
  must be used to describe them.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output ' -->
  <dd>The list of output astrometry files. The number of output astrometry files
  must be equal to the number of input astrometry files. If the output file
  name equals the input file name then the original astrometry file is
  overwritten.
  </dd>
  </dl>
  <dl id="l_acatpars">
  <dt><b>acatpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='acatpars' Line='acatpars = ""' -->
  <dd>The default input astrometry file format parameters. The acatpars parameters
  are used only if the input astrometry file does not have a header. Type
  <span style="font-family: monospace;">"help acatpars"</span> for a detailed description of the acatpars parameters.
  </dd>
  </dl>
  <dl id="l_catalogs">
  <dt><b>catalogs = <span style="font-family: monospace;">"filename@noao"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catalogs' Line='catalogs = "filename@noao"' -->
  <dd>The dummy input catalog name. Afiltcat task users should leave this
  parameter at its default setting.
  </dd>
  </dl>
  <dl id="l_standard">
  <dt><b>standard = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='standard' Line='standard = yes' -->
  <dd>Output a standard astrometry file ? If standard = yes then a header describing
  the format of the output astrometry file is written to the output file.
  Astcat package tasks use this information to decode the astrometry file. If
  standard = no, no header is written and astcat tasks must use the acatpars
  parameters to decode the astrometry file.
  </dd>
  </dl>
  <dl id="l_filter">
  <dt><b>filter = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filter' Line='filter = yes' -->
  <dd>Filter rather than copy the input astrometry file to the output astrometry
  file ?
  </dd>
  </dl>
  <dl id="l_afiltpars">
  <dt><b>afiltpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='afiltpars' Line='afiltpars = ""' -->
  <dd>The astrometry file filtering parameter set. Afiltpars parameters permit the
  user to sort the output on a field or field expression, select or reject
  catalog records using a boolean expression, select or reject fields
  to output, add new fields to the output that are expressions of existing
  fields, and perform simple coordinate transformations.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = no' -->
  <dd>Update the default values of the algorithm parameter sets, e.g. acatpars and
  afiltpars, on task termination ?
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print status messages on the terminal as the task proceeds ?
  </dd>
  </dl>
  <dl id="l_catdb">
  <dt><b>catdb = <span style="font-family: monospace;">")_.catdb"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catdb' Line='catdb = ")_.catdb"' -->
  <dd>The catalog configuration file. Catdb defaults to the value of the
  package parameters catdb. The default catalog configuration file is
  <span style="font-family: monospace;">"astcat$lib/catdb.dat"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Afiltcat filters the list of input astrometry files <i>input</i>
  and writes the results to the output files <i>output</i>. The number of input
  astrometry files must equal the number of output astrometry files.
  </p>
  <p>
  The format of the input astrometry files is defined by the file header
  if the file was written by an astcat package task, or by the
  <i>acatpars</i> parameter set. The acatpars parameters <i>ftype</i> and
  <i>csystem</i> define the input astrometry file type and coordinate system.
  The position, size, and units of the standard astrometry file fields
  the associated error fields are defined by the parameters:
  <i>id</i>, <i>ra</i>, <i>dec</i>, <i>pmra</i>, <i>pmdec</i>, <i>catsystem</i>,
  <i>equinox</i>, <i>epoch</i>, <i>px</i>, <i>rv</i>, <i>mag</i>, <i>color</i>,
  <i>xp</i>, <i>yp</i>, <i>xc</i>, <i>yc</i>, and <i>imag</i>, and:
   <i>era</i>, <i>edec</i>,
  <i>epmra</i>, <i>epmdec</i>, <i>epx</i>, <i>erv</i>, <i>emag</i>, <i>ecolor</i>,
  <i>exc</i>, <i>eyc</i>, <i>eimag</i>.  More detailed information on astrometry
  files and the acatpars parameters can be found by typing <span style="font-family: monospace;">"help files"</span>
  and <span style="font-family: monospace;">"help acatpars"</span>.
  </p>
  <p>
  If <i>filter</i> = yes, the input astrometry file is filtered before being
  written to the outputfile. The filtering parameters are defined by the
  filtering parameter set <i>afiltpars</i>.
  The afilterpars parameters permit the user to sort the query results by setting
  the sort field parameter <i>fsort</i>, select or reject
  catalog records by setting the selection expression parameter <i>fexpr</i>,
  select or reject fields for output by setting the output field
  list parameter <i>afields</i>, and change the coordinate system, units,
  and format of the output coordinates by setting the <i>fosystem</i>,
  <i>foraunits</i>, <i>fodecunits</i>, <i>foraformat</i>, and <i>fodecformat</i>
  parameters. A more detailed description of the filtering
  parameters can be obtained by typing <span style="font-family: monospace;">"help afiltpars"</span>.
  </p>
  <p>
  If <i>standard</i> = yes a header is written to the output file which
  defines the contents and format of the output astrometry file. The astcat
  tasks use this header to decode the astrometry files. If the header is
  missing or has been modified by non-astcat tasks the user must set
  standard = no, and use the <i>acatpars</i> parameters to define the
  astrometry file format. Most non-astcat tasks will interpret the catalog
  header as documentation and skip it.
  </p>
  <p>
  If <i>update</i> = yes the values of the <i>acatpars</i> and <i>afiltpars</i>
  parameters are updated at task termination. If <i>verbose</i> = yes
  then detailed status reports are issued as the task executes.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Sort the input astrometry file using the value of the magnitude field.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; page reg001.cat.1
  cl&gt; afiltcat reg001.cat.1 reg001.cat.2 fsort=mag1
  </pre></div>
  <p>
  2. Repeat example 1 but only output records for which mag1 &lt;= 16.0.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; afiltcat reg001.cat.1 reg001.cat.3 fsort=mag1 fexpr="mag1 &lt;= 16.0"
  </pre></div>
  <p>
  3. Repeat example 2 but since the input astrometry file has 2 magnitude
  columns output a new color field equal to <span style="font-family: monospace;">"mag2 - mag1"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; afiltcat reg001.cat.1 reg001.cat.4 fsort=mag1 fexpr="mag1 &lt;= 16.0" \
  fields="f[*],mag2-mag1"
  </pre></div>
  <p>
  4. Repeat example 1 but overwrite the input astrometry file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; page reg001.cat.1
  cl&gt; afiltcat reg001.cat.1 reg001.cat.1 fsort=mag1
  </pre></div>
  <p>
  5. Filter a list of input astrometry files by extracting columns 1-4
  but reversing the order of fields 3 and 4.  Overwrite the input files.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; afiltcat @inlist @inlist fields="f[1-2],f4,f3"
  </pre></div>
  <p>
  6. Repeat the previous example for a list of text files which have no catalog
  headers but contain the ras and decs in hours and degrees in J2000
  coordinates of a list of source  in columns 1 and 2 of a simple text file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; afiltcat @inlist @inlist ftype="stext" csystem=j2000 ra="1 hours" \
      dec="2 degrees" mag="3-4" fields="f[1-2],f4,f3"
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  aclist, agetcat, acatpars, afiltpars
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

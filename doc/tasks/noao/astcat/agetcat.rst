.. _agetcat:

agetcat: Extract astrometry files from astrometric catalogs
===========================================================

**Package: astcat**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  agetcat regions output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_regions">
  <dt><b>regions</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='regions' Line='regions' -->
  <dd>The source  of the extraction region definitions. The options are:
  <dl>
  <dt><b>&lt;filename&gt;</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='&lt;filename&gt;' -->
  <dd>The name of a text file containing a list of region definitions, one
  region definition per line. The format of the regions file is described
  in detail below.
  </dd>
  </dl>
  <dl>
  <dt><b>&lt;image list&gt;</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='' Line='&lt;image list&gt;' -->
  <dd>The list of images containing the region definition. The input images
  must have a valid FITS world coordinate system in order to be used
  for region definition.
  </dd>
  </dl>
  <dl>
  <dt><b>pars</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='pars' Line='pars' -->
  <dd>If regions is set to the reserved keyword <span style="font-family: monospace;">"pars"</span> then a single region
  definition is read from the <i>aregpars</i> parameter set. By default a region
  ten arc minutes in size around coordinates ra = <span style="font-family: monospace;">"00:00:00.0"</span> and
  dec = <span style="font-family: monospace;">"+00:00:00"</span> in the query coordinate system is extracted.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output ' -->
  <dd>The list of output astrometry files. The number of output files must be equal
  to the number regions in the regions list times the number of astrometry
  catalogs in the catalog list. By default the output files are assigned names of
  the form <span style="font-family: monospace;">"reg#[.cat#].cat.#"</span> if the region definition source is <span style="font-family: monospace;">"pars"</span> or
  a file e.g. <span style="font-family: monospace;">"reg002.cat.1"</span>, or <span style="font-family: monospace;">"image[.cat#].cat.#"</span> if the region
  definition source is an image list, e.g. <span style="font-family: monospace;">"image.cat.1"</span>. The catalog number
  is only inserted if there is more than one catalog in the catalog list.
  </dd>
  </dl>
  <dl id="l_aregpars">
  <dt><b>aregpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='aregpars' Line='aregpars = ""' -->
  <dd>The region definition parameter set. The aregpars parameters define the
  extraction region center, region width, region center units, and the region
  center coordinate system. The region definition parameters are used if
  <i>regions</i> = <span style="font-family: monospace;">"pars"</span>.
  </dd>
  </dl>
  <dl id="l_catalogs">
  <dt><b>catalogs = <span style="font-family: monospace;">")_.catalogs"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catalogs' Line='catalogs = ")_.catalogs"' -->
  <dd>The list of input astrometry catalogs. By default the catalog name is set to the
  value of the package parameter catalogs. 
  </dd>
  </dl>
  <dl id="l_standard">
  <dt><b>standard = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='standard' Line='standard = yes' -->
  <dd>Output a standard astrometry file ? If standard = yes then a header describing
  the format of the astrometry file is written to the output file. The
  astcat package
  tasks use this information to decode the file. If standard = no, no
  header is written and the user must instruct the astcat tasks how to decode the
  file.
  </dd>
  </dl>
  <dl id="l_filter">
  <dt><b>filter = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filter' Line='filter = no' -->
  <dd>Filter the results of the catalog query before writing the final results
  to the output astrometry file ?
  </dd>
  </dl>
  <dl id="l_afiltpars">
  <dt><b>afiltpars = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='afiltpars' Line='afiltpars = ""' -->
  <dd>The astrometry file filtering parameter set. These parameters permit the user
  to sort the output on a field or field expression, select or reject
  catalog records using a boolean expression, select or reject fields
  to output, add new fields that are expressions of existing fields to
  the output, and perform simple coordinate transformations.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = no' -->
  <dd>Update the default values of the algorithm parameters, e.g. aregpars and
  afiltpars, at task termination ?
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
  package parameter catdb. The default catalog configuration file is
  <span style="font-family: monospace;">"astcat$lib/catdb.dat"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Agetcat extracts astrometry files from local or remote astrometry catalogs
  <i>catalogs</i> using a list of region definitions <i>regions</i> supplied by
  the user and writes the results of each catalog query to the output astrometry
  files <i>output</i>.
  </p>
  <p>
  A region definition consists of the coordinates of the field center,
  the field size, the units of the field center, and the coordinate system of
  the field center. If <i>regions</i> = <span style="font-family: monospace;">"pars"</span> these quantities are read
  from the <i>aregpars</i> parameters <i>rcra</i>, <i>rcdec</i>, <i>rcrawidth</i>,
  <i>rcdecwidth</i> <i>rcraunits</i>, <i>rcdecunits</i>., and <i>rcsystem</i>. 
  If <i>regions</i> is an image they are read from the FITS world coordinate
  system in the image header.  If <i>regions</i> is a file name they are
  read from a file whose format is the following.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Optional comment
  
  ra1 dec1 xwidth1 ywidth1 [raunits1 [decunits1 [system1]]]
  ra2 dec2 xwidth2 ywidth2 [raunits2 [decunits2 [system2]]]
  raN decN xwidthN ywidthN [raunitsN [decunitsN [systemN]]]
  </pre></div>
  <p>
  Quantities in square brackets are optional. If system is undefined the
  coordinate system defaults to the query coordinate system, i.e. if the
  catalog query expects coordinates in J2000.0 then ra and dec will be
  interpreted as though they were in the J2000.0 system. If undefined 
  the ra and dec units default to the preferred units of the coordinate
  system, i.e. hours and degrees for equatorial coordinate systems,
  and degrees and degrees for ecliptic, galactic, and supergalactic 
  coordinate systems.
  </p>
  <p>
  A sample regions file  is shown below. If the catalog query system is
  J2000.0 then all four region definitions are equivalent, since J2000.0
  is assumed in examples 1 and 2, is specified in example 3, and example 4
  is same region as example 3 but expressed in the B1950.0 coordinate system.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # List of targets
  
  13:29:53.27 +47:11:48.4 10.0 10.0
  13:29:53.27 +47:11:48.4 10.0 10.0 hours degrees
  13:29:53.27 +47:11:48.4 10.0 10.0 hours degrees J2000.0
  13:27:46.90 +47:27:16.0 10.0 10.0 hours degrees B1950.0
  </pre></div>
  <p>
  For each specified astrometry catalog in <i>catalog</i> agetcat loops through the
  regions list, formats the catalog query, makes a local or remote
  connection to the catalog server using the catalog description in the
  catalog configuration file <i>catdb</i>, and captures the results.
  Catalog names must be of the forms catalog@site, e.g. usno2@noao.
  Catalog names without entries in the catalog configuration file
  are skipped.
  </p>
  <p>
  If <i>filter</i> = yes, the captured results are filtered using the
  values of the parameters in the filtering parameter set <i>afiltpars</i>.
  The afilterpars parameters permits the user to sort the query results by setting
  the sort field parameter <i>fsort</i>, select or reject
  catalog records by setting the selection expression parameter <i>fexpr</i>,
  select or reject fields for output by setting the output field
  list parameter <i>fields</i>, and change the coordinate system, units,
  and format of the catalog coordinates by setting the <i>fosystem</i>,
  <i>foraunits</i>, <i>fodecunits</i>, <i>foraformat</i>, and <i>fodecformat</i>
  parameters. A more detailed description of the region filtering
  parameters can be obtained by typing <span style="font-family: monospace;">"help afiltpars"</span>.
  </p>
  <p>
  If <i>standard</i> = yes a header is written to the output astrometry file which
  defines the contents and format of the output object list. The astcat
  tasks use this header to decode the input catalog files. If it is
  missing or has been modified by non-astcat tasks the user must use
  the <i>acatpars</i> parameters to define the astrometry file format. Most
  non-astcat tasks will interpret the astrometry file header as documentation
  and skip it.
  </p>
  <p>
  If <i>update</i> = yes the values of the <i>aregpars</i> and <i>afilterpars</i>
  parameters will be updated at task termination. If <i>verbose</i> = yes
  then detailed status reports are issued as the task executes.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Extract data from the default catalog using the default region definition
  and page the results to determine the catalog format, i.e. the number and
  names of the default output fields.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; agetcat pars default
  cl&gt; page reg001.cat.1
  </pre></div>
  <p>
  2. Repeat the previous example but sort the output on the sort field <span style="font-family: monospace;">"mag1"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; agetcat pars default filter+ fsort=mag1
  cl&gt; page reg001.cat.2
  </pre></div>
  <p>
  3. Repeat example 2 but output only those records for which mag &lt;= 16.0.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; agetcat pars default filter+ fsort=mag1 fexpr="mag1 &lt;= 16.0"
  cl&gt; page reg001.cat.3
  </pre></div>
  <p>
  4. Repeat example 3 but output a new field equal to mag2 - mag3.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; agetcat pars default filter+ fsort=mag1 fexpr="mag1 &lt;= 16.0" \
  fields="f[*],mag2-mag1"
  cl&gt; page reg001.cat.4
  </pre></div>
  <p>
  5. Run agetcat on the text file regions which contains a list of region
  definitions. Note that the coordinate system and coordinate units default
  to those expected by the catalog query. The latter information can be
  determined by running aclist on the default catalog.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; page regions
  00:00:00.0 -90:00:00 10.0 10.0
  00:00:00.0 -60:00:00 10.0 10.0
  00:00:00.0 -30:00:00 10.0 10.0
  00:00:00.0 +00:00:00 10.0 10.0
  00:00:00.0 +30:00:00 10.0 10.0
  00:00:00.0 +60:00:00 10.0 10.0
  00:00:00.0 +90:00:00 10.0 10.0
  cl&gt; agetcat regions default
  cl&gt; page reg001.cat.5
  cl&gt; page reg002.cat.1
  cl&gt; page reg003.cat.1
  cl&gt; page reg004.cat.1
  cl&gt; page reg005.cat.1
  cl&gt; page reg006.cat.1
  cl&gt; page reg007.cat.1
  </pre></div>
  <p>
  6. Repeat example 5 but find data for two catalogs the usno2@noao and
  gsc@cadc.
  </p>
  <div class="highlight-default-notranslate"><pre>
  page regions
  00:00:00.0 -90:00:00 10.0 10.0
  00:00:00.0 -60:00:00 10.0 10.0
  00:00:00.0 -30:00:00 10.0 10.0
  00:00:00.0 +00:00:00 10.0 10.0
  00:00:00.0 +30:00:00 10.0 10.0
  00:00:00.0 +60:00:00 10.0 10.0
  00:00:00.0 +90:00:00 10.0 10.0
  cl&gt; agetcat regions default catalogs="usno2@noao,gsc@noao"
  </pre></div>
  <p>
  7. Run agetcat on a list of images containing valid FITS WCS information.
  Note that in the following example the test image dev$pix does not
  have a FITS WCS so no data is extracted for it.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; page imlist
  dev$pix
  dev$ypix
  cl&gt; agetcat @imlist default
  cl&gt; page wpix.cat.1
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
  aclist, adumpcat, aregpars, afiltpars
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

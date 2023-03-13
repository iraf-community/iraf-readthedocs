.. _aimfind:

aimfind: Select images containing catalog objects
=================================================

**Package: astcat**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  aimfind images output imfile
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>The input image list. The input images must contain a valid fits world
  coordinate system which is used to determine the catalog extraction region.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output ' -->
  <dd>The list of output astrometry file names.  The number of output file names
  must be equal to the number of input images. Output files are only created
  if at least one catalog object is in the image. By default the output files
  are assigned names of the form <span style="font-family: monospace;">"image.cat.#"</span>, e.g. <span style="font-family: monospace;">"image.cat.1"</span>. 
  </dd>
  </dl>
  <dl id="l_imfile">
  <dt><b>imfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imfile' Line='imfile' -->
  <dd>The list of images containing catalog data.
  </dd>
  </dl>
  <dl id="l_catalogs">
  <dt><b>catalogs = <span style="font-family: monospace;">")_.catalogs"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catalogs' Line='catalogs = ")_.catalogs"' -->
  <dd>The input astrometry catalog. By default the catalog name is set to the
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
  <dl id="l_append">
  <dt><b>append = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = no' -->
  <dd>By default the predicted pixel coordinates are prepended to each selected
  output file record. If append = yes they are appended to each selected
  record instead.
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
  Aimfind selects those images from the input image list <i>images</i>
  which contain one or more  catalog <i>catalogs</i> objects and writes
  the resulting catalog records along with predicted pixel coordinates to
  <i>output</i> and the selected image name to <i>imfile</i>. The input images
  must contain a valid FITs wcs.
  </p>
  <p>
  For each input image aimfind determines the region of the sky covered 
  by the image, formats the appropriate catalog query, makes a local or remote
  connection to the catalog server using the catalog description in the
  catalog configuration file <i>catdb</i>, and captures the results.
  Catalog names must be of the form catalog@site, e.g. lan92@noao.
  </p>
  <p>
  If <i>filter</i> = yes, the captured results are filtered using the
  values of the parameters in the filtering parameter set <i>afiltpars</i>.
  The afilterpars parameters permit the user to sort the query results by setting
  the sort field parameter <i>fsort</i>, select or reject
  catalog records by setting the selection expression parameter <i>fexpr</i>,
  select or reject fields for output by setting the output field
  list parameter <i>fields</i>, and change the coordinate system, units,
  and format of the catalog coordinates by setting the <i>fosystem</i>,
  <i>foraunits</i>, <i>fodecunits</i>, <i>foraformat</i>, and <i>fodecformat</i>
  parameters. At present the names, data types, units, and format of the
  predicted pixel coordinates computed by aimfind are fixed at <span style="font-family: monospace;">"xp,yp"</span>,
  <span style="font-family: monospace;">"d,d"</span>, <span style="font-family: monospace;">"pixels,pixels"</span>, and <span style="font-family: monospace;">"%10.3f,%10.3f"</span> respectively. A more detailed
  description of the region filtering parameters can be obtained by typing
  <span style="font-family: monospace;">"help afiltpars"</span>.
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
  If <i>append</i> = no then the values of the predicted pixel coordinates
  are prepended to each selected catalog record. If append = tes they
  are appended instead.
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
  1. Determine which images in the input image list contain Landolt standards.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; aimfind *.imh "" imlist catalogs=lan92@noao
  cl&gt; page imlist
  </pre></div>
  <p>
  2. Repeat the previous example but write an output astrometry file for
  each selected image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; aimfind *.imh default imlist catalogs=lan92@noao
  </pre></div>
  <p>
  3. Repeat example 2 but sort the output on a field called v.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; aimfind *.imh default filter+ fsort="v"
  </pre></div>
  <p>
  4. Repeat example 2 but transform the catalog coordinates to the B1950
  system.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; aimfind *.imh default filter+ fosystem="B1950"
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
  aclist, adumpcat, agetcat, afiltpars
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

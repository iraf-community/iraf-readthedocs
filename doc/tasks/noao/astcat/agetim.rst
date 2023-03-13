.. _agetim:

agetim: Extract FITS images from image surveys
==============================================

**Package: astcat**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  agetim regions output
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
  ten arc minutes in size centered on coordinates ra = <span style="font-family: monospace;">"00:00:00.0"</span> and
  dec = <span style="font-family: monospace;">"+00:00:00"</span> in the query coordinate system is extracted.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>The list of output FITS image files. The number of output files must be equal
  to the number regions in the regions list times the number of astrometry
  catalogs in the catalog list. By default the output images are assigned names of
  the form <span style="font-family: monospace;">"reg#[.sv#].#.fits"</span> if the region definition source is <span style="font-family: monospace;">"pars"</span> or
  a file, e.g. <span style="font-family: monospace;">"reg002.1.fits"</span>, or <span style="font-family: monospace;">"image[.sv#].#.fits"</span> if the region
  definition source is an image list, e.g. <span style="font-family: monospace;">"image.1.fits"</span>. The image survey
  number is only inserted if there is more than one image survey
  in the image survey list.
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
  <dl id="l_imsurveys">
  <dt><b>imsurveys = <span style="font-family: monospace;">")_.imsurveys"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imsurveys' Line='imsurveys = ")_.imsurveys"' -->
  <dd>The list of input image surveys. By default the image survey name is set to the
  value of the package parameter imsurveys. 
  </dd>
  </dl>
  <dl id="l_wcsedit">
  <dt><b>wcsedit = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcsedit' Line='wcsedit = no' -->
  <dd>Convert a DSS WCS to a FITS WCS or add an approximate FITS style WCS to the
  output image headers if they don't already possess one ?  The WCS status
  of the survey images  plus approximate coordinate, scale, orientation, and
  projection information is stored in the image surveys configuration
  file <i>imdb</i>.
  </dd>
  </dl>
  <dl id="l_hdredit">
  <dt><b>hdredit = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hdredit' Line='hdredit = no' -->
  <dd>Add a set of standard keywords to the image header which may be required or
  useful in the later astrometric analysis steps ?  These parameters divide
  into two groups, those concerned with locating objects in an image and
  those required to transform from mean place to observed coordinates.
  Default settings for these parameters are stored in the images surveys
  configuration file.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = no' -->
  <dd>Update the default values of the algorithm parameters, e.g. aregpars
  on task termination ?
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print status messages on the terminal as the task proceeds ?
  </dd>
  </dl>
  <dl id="l_imdb">
  <dt><b>imdb = <span style="font-family: monospace;">")_.imdb"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imdb' Line='imdb = ")_.imdb"' -->
  <dd>The image surveys configuration file. Imdb defaults to the value of the
  package parameter imdb. The default image surveys configuration file is
  <span style="font-family: monospace;">"astcat$lib/imdb.dat"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Agetim extracts fits images from local or remote image surveys
  <i>imsurveys</i> using a list of region definitions supplied by the user
  <i>regions</i> and writes the results of each image survey query to the output
  images <i>output</i>.
  </p>
  <p>
  A regions definition consists of the coordinates of the field center,
  the field size, the units of the field center, and the coordinate system of
  the field center. If <i>regions</i> = <span style="font-family: monospace;">"pars"</span> these quantities are read
  from the <i>aregpars</i> parameters <i>rcra</i>, <i>rcdec</i>, <i>rcrawidth</i>,
  <i>rcdecwidth</i> <i>rcraunits</i>, <i>rcdecunits</i>., and <i>rcsystem</i>. 
  If <i>regions</i> is an input image
  list they are read from the FITS world coordinate system in the image header.
  If <i>regions</i> is a file name they are read from file whose format is
  the following.
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
  A sample regions file  is shown below. If the image query system is
  J2000.0 then all four regions definitions are equivalent, since J2000.0
  is assumed in examples 1 and 2, is specified in example 3, and example
  is same target as example but expressed in the B1950.0 coordinate system.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # List of targets
  
  13:29:53.27 +47:11:48.4 10.0 10.0
  13:29:53.27 +47:11:48.4 10.0 10.0 hours degrees
  13:29:53.27 +47:11:48.4 10.0 10.0 hours degrees J2000.0
  13:27:46.90 +47:27:16.0 10.0 10.0 hours degrees B1950.0
  </pre></div>
  <p>
  For each specified image survey in <i>imsurvey</i> agetim loops through the
  regions list, formats the image survey query, makes a local or remote
  connection to the image server using the image survey description in the
  image survey configuration file <i>imdb</i>, and captures the results.
  Image survey names must be of the form imsurvey@site, e.g. dss1@cadc.
  Image survey names without entries in the image survey configuration file
  are skipped.
  </p>
  <p>
  If <i>wcsedit</i> = yes  then DSS coordinate systems are converted
  into FITS coordinate systems or an approximate FITS WCS is added
  to the image using information in the image surveys configuration file.
  The quantities of interest are the values, units, and coordinates
  system of the reference point <i>wxref</i>, <i>wyref</i>, <i>wraref</i>,
  <i>wdecref</i>, <i>wraunits</i>, <i>wdecunits</i>, and <i>wsystem</i>, and the
  scale, orientation, and projection information <i>wxmag</i>, <i>wymag</i>,
  <i>wxrot</i>, <i>wyrot</i>, and <i>wproj</i>. For more information on how these
  quantities are defined in the image surveys configuration file 
  type <span style="font-family: monospace;">"help imsurveys"</span>.
  </p>
  <p>
  If <i>hdredit</i> = yes then a standard set of keyword equal values
  pairs will be added to the image headers using information in the
  image surveys configuration file.  The parameters divide into two groups
  those concerned with locating stars in the image and computing accurate
  pixel centers: <i>edatamin</i>, <i>edatamax</i>, <i>egain</i>, and <i>erdnoise</i>,
  and those required for transforming mean place coordinates to observed
  plate coordinates as may be required to compute very accurate image scales,
  <i>observat</i>, <i>esitelng</i>, <i>esitelat</i>, <i>esitealt</i>, <i>esitetz</i>,
  <i>emjdobs</i>, <i>ewavlen</i>, <i>etemp</i>, and <i>epress</i>. New keyword
  values are only added to the header if keywords of the same name do not
  already exist and if appropriate values for the keywords exists, i.e.
  <span style="font-family: monospace;">"INDEF"</span> valued parameters will not be added to the header.
  </p>
  <p>
  If <i>update</i> = yes the values of the <i>aregpars</i> parameters will be
  updated at task termination. If <i>verbose</i> = yes then detailed status
  reports are issued as the task executes.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Extract data from the default image survey using the default region
  definition, display the resulting image,  and examine its header.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; agetim pars default
  cl&gt; display reg001.1.fits 1 fi+
  cl&gt; imheader reg001.1.fits lo+ | page
  </pre></div>
  <p>
  2. Repeat the previous example but convert the DSS WCS to a FITS WCS.
  The DSS WCS is unaltered.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; agetim pars default wcsedit+
  cl&gt; display reg001.2.fits 1 fi+
  cl&gt; imheader reg001.2.fits
  </pre></div>
  <p>
  3. Repeat example 2 but extract data for two surveys.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; agetim pars default wcsedit+ imsurveys="dss1@cadc,dss2@cadc"
  cl&gt; display reg001.3.fits 1 fi+
  cl&gt; imheader reg001.3.fits
  cl&gt; display reg002.1.fits 2 fi+
  cl&gt; imheader reg002.1.fits
  </pre></div>
  <p>
  4. Repeat example 2 but add the values of the standard astrometry image
  keywords if these do not already exist in the image header and are defined.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; agetim pars default wcsedit+ hdredit+
  cl&gt; display reg001.4.fits 1 fi+
  cl&gt; imheader reg001.4.fits
  </pre></div>
  <p>
  5. Extract images for a list of regions in a text file.  Note that the
  coordinate system and coordinate units are not specified in this regions
  list and default to those expected by the image survey query.
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
  cl&gt; agetim regions default
  </pre></div>
  <p>
  6. Run agetim on a list of images containing valid FITS WCS information.
  Note that in the following example the test image dev$pix does not
  have a FITS WCS so no data is extracted for it.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; page imlist
  dev$pix
  dev$ypix
  cl&gt; agetim @imlist default
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  If output file is not a fits file, as may be the case if an error occurred
  in the network transfer, and header editing is enabled agetim will
  crash with a file seek error. The bug is due to missing error check 
  statements in the FITS kernel and will be fixed for the next release.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  aslist, adumpim, aregpars
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

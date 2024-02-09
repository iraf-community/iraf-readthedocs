.. _mscgetcatalog:

mscgetcatalog: Get coordinates from a Web server covering mosaic exposures
==========================================================================

**Package: msctools**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  MSCGETCATALOG is a task for getting coordinates and magnitudes from
  Web-based catalog servers.  The task returns a text file of coordinates and
  magnitudes for a field centered on the specified mosaic exposure(s).
  </p>
  </section>
  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mscgetcatalog input output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of mosaic exposures.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>Output text file containing catalog coordinates and magnitudes.
  </dd>
  </dl>
  <dl id="l_magmin">
  <dt><b>magmin = 0., magmax = 25.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='magmin' Line='magmin = 0., magmax = 25.' -->
  <dd>Range of magnitudes to select from the catalog.
  </dd>
  </dl>
  <dl id="l_catalog">
  <dt><b>catalog = <span style="font-family: monospace;">"NOAO:USNO-A2"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catalog' Line='catalog = "NOAO:USNO-A2"' -->
  <dd>Catalog to be used.  With IRAF V2.11 and earlier the choices are:
  <dl>
  <dt><b>NOAO:USNO-A2</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='NOAO' Line='NOAO:USNO-A2' -->
  <dd>The USNO A2 catalog using a server from NOAO.
  </dd>
  </dl>
  <dl>
  <dt><b>CADC:USNO-A2</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='CADC' Line='CADC:USNO-A2' -->
  <dd>The USNO A2 catalog using a server from the CADC.
  </dd>
  </dl>
  With IRAF V2.12 the catalogs supported by the <b>astcat</b> package may
  also be used.  For a list of catalogs use the command:
  <div class="highlight-default-notranslate"><pre>
  cl&gt; aclist * verbose-
  </pre></div>
  </dd>
  </dl>
  <dl id="l_rmin">
  <dt><b>rmin = 21.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rmin' Line='rmin = 21.' -->
  <dd>Minimum radius in arc minutes from the center of the input exposures
  to include in the output file.  The actual radius used is the maximum
  of this parameter and the maximum radius to the corners of all the
  input extensions.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Mscgetcatalog</b> is a task for getting coordinates and magnitudes from
  Web-based catalog servers.  This requires that you can make http requests
  from the system where this task is executed.  Proxy servers are not
  supported.  Note that if the server does not respond this task may
  not return and would need to be interupted.
  </p>
  <p>
  <b>Mscgetcatalog</b> returns a text file, specified by the <i>output</i>
  parameter, of coordinates and magnitudes for a field centered on the mosaic
  exposure(s), specified by the <i>input</i> .  This requires that the mosaic
  exposures have an approximate world coordinate system (WCS).  The catalog
  of sources is generally used to calibrate the WCS provided there is
  sufficient overlap between the field and the approximate WCS.  This file
  can be used with various <b>mscred</b> tasks such as <b>msccmatch</b>,
  <b>mscimatch</b>, <b>msczero</b>, and <b>msctvmark</b>.
  </p>
  <p>
  Currently all coordinates, input and output, are J2000.
  </p>
  <p>
  The task <b>msccmatch</b> may execute this task to generate the coordinates
  to use by specifying
  </p>
  <div class="highlight-default-notranslate"><pre>
  !mscgetcatalog $I $C
  </pre></div>
  <p>
  for the <i>coords</i> parameter.  The <span style="font-family: monospace;">"$I"</span> field is replaced by the
  mosaic exposure being calibrated and <span style="font-family: monospace;">"$C"</span> is replaced by a temporary
  filename used by the task.
  </p>
  <p>
  The center of the circular region to be extracted from the catalog is
  determined by the midpoint of the coordinates of all the extension corners
  in the list of input mosaic exposures.  The maximum radius from this point
  to all the corners determines a minimum radius for the region.  The
  <i>rmin</i> parameter may be used to force a minimum radius though if the
  radius including all the corners is larger then that radius is used.
  </p>
  <p>
  The currently supported catalogs include approximate magnitudes.  When
  magnitudes are available the <i>magmin</i> and <i>magmax</i> parameters may
  be used to restrict the output coordinates to a specified magnitude
  range.
  </p>
  <p>
  The selection of catalogs in IRAF V2.11 and earlier is limited to
  <span style="font-family: monospace;">"NOAO:USNO-A2"</span> and <span style="font-family: monospace;">"CADC:USNO-A2"</span>.  In V2.12 the catalogs supported
  by the new catalog access package <b>astcat</b> may also be used.  A list
  of catalogs may be obtained using the command:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; aclist * verbose-
  </pre></div>
  <p>
  The catalog names must be specified exactly as shown in the list.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  This example illustrates getting coordinates for the brightest stars in an
  NOAO mosaic exposure using the default USNO-A2 server at NOAO.  This
  specifies the output as <span style="font-family: monospace;">"STDOUT"</span> to print to the terminally.  More commonly
  this would be a filename and the magnitude limit would include fainter
  stars.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; mscgetcat obj110 STDOUT magmax=11
   15:23:19.94   -0:08:41.8 10.60 12.20
   15:23:41.25   -0:16:17.8  8.60 11.60
   15:24:57.69   -0:06:16.8 10.90 12.10
   15:25:34.79   -0:01:02.8 10.60 12.30
   15:25:40.38   -0:01:11.5 10.60 11.50
   15:25:54.55   -0:17:02.8 10.40 11.80
   15:22:58.95    0:05:55.9 10.40 13.90
   15:23:05.07    0:04:17.0 11.00 12.10
   15:24:09.96    0:03:04.2 11.00 11.90
   15:26:00.73    0:17:46.3  8.60  9.40
  </pre></div>
  <p>
  2.  To use the Guide Star Catalog 2 (in IRAF V2.12):
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; mscgetcat obj110 STDOUT catalog=gsc2@stsci magmax=11
   15:23:19.94   -0:08:41.8 10.60 12.20
   15:23:41.25   -0:16:17.8  8.60 11.60
   15:24:57.69   -0:06:16.8 10.90 12.10
   15:25:34.79   -0:01:02.8 10.60 12.30
   15:25:40.38   -0:01:11.5 10.60 11.50
   15:25:54.55   -0:17:02.8 10.40 11.80
   15:22:58.95    0:05:55.9 10.40 13.90
   15:23:05.07    0:04:17.0 11.00 12.10
   15:24:09.96    0:03:04.2 11.00 11.90
   15:26:00.73    0:17:46.3  8.60  9.40
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MSCGETCATALOG">
  <dt><b>MSCGETCATALOG - V4.7: April, 2002</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MSCGETCATALOG' Line='MSCGETCATALOG - V4.7: April, 2002' -->
  <dd>Modified to allow use of the ASTCAT package which provides access to
  a larger variety of catalogs.
  </dd>
  </dl>
  <dl id="l_MSCGETCATALOG">
  <dt><b>MSCGETCATALOG - V4.0: August 22, 2000</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MSCGETCATALOG' Line='MSCGETCATALOG - V4.0: August 22, 2000' -->
  <dd>This task is new in this release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  msccmatch, mscimatch, msczero, msctvmark
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

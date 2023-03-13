.. _hpctran:

hpctran: Convert between HEALPix row and spherical coordinate
=============================================================

**Package: imcoords**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  hpctran lng=xxx lat=xxx
  <br>
  hpctran row=xxx
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_row">
  <dt><b>row     </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='row' Line='row     ' -->
  <dd>HEALPix table row (1 indexed).
  This is used as input if the direction
  is <span style="font-family: monospace;">"row2ang"</span> or is used to store the value if the direction is
  <span style="font-family: monospace;">"ang2row"</span>.
  </dd>
  </dl>
  <dl id="l_lng">
  <dt><b>lng, lat</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lng' Line='lng, lat' -->
  <dd>Spherical coordinate consisting of a longitude and latitude.
  These are used as input if the direction
  is <span style="font-family: monospace;">"ang2row"</span> or is used to store the value if the direction is
  <span style="font-family: monospace;">"row2ang"</span>.  The units are interpreted as selected by the <i>cunits</i>
  parameter.  The type of coordinates appropriate for a particular map
  is defined by the map provider.
  </dd>
  </dl>
  <dl id="l_nside">
  <dt><b>nside = 512</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nside' Line='nside = 512' -->
  <dd>The number of pixels per face side.
  </dd>
  </dl>
  <dl id="l_cunits">
  <dt><b>cunits = <span style="font-family: monospace;">"degrees"</span> (degrees|hourdegree|radians)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cunits' Line='cunits = "degrees" (degrees|hourdegree|radians)' -->
  <dd>The units of the longitude and latitude.  The <span style="font-family: monospace;">"hourdegree"</span> is for
  longitude in hours and latitude in degrees.
  </dd>
  </dl>
  <dl id="l_maptype">
  <dt><b>maptype = <span style="font-family: monospace;">"nest"</span> (nest|ring)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maptype' Line='maptype = "nest" (nest|ring)' -->
  <dd>The map pixelization type which may be <span style="font-family: monospace;">"nest"</span> or <span style="font-family: monospace;">"ring"</span>.
  </dd>
  </dl>
  <dl id="l_direction">
  <dt><b>direction = <span style="font-family: monospace;">"ang2row"</span> (ang2row|row2ang)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='direction' Line='direction = "ang2row" (ang2row|row2ang)' -->
  <dd>The conversion direction.  <span style="font-family: monospace;">"ang2row"</span> converts a spherical coordinate
  to a map row or pixel number.  <span style="font-family: monospace;">"row2ang"</span> converts a map row or pixel
  number to a spherical coordinate.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  HEALPix is an acronym for Hierarchical Equal Area isoLatitude Pixelization
  of a sphere.  See the reference section for a technical description of the
  pixelization and mathematics.  As suggested in the name, this pixelization,
  or tiling, produces a subdivision of a spherical surface in which each
  <span style="font-family: monospace;">"pixel"</span> covers the same surface area as every other pixel.  A HEALPix FITS
  <span style="font-family: monospace;">"map"</span> is a table where each row contains <span style="font-family: monospace;">"pixel"</span> data for a region on the
  sphere.  It is a table because the pixels don't form a raster as in an
  image.
  </p>
  <p>
  The pixelization is defined by a resolution parameter which may be expressed
  in various ways.  This task uses the number of pixels along a side of one of
  the 12 basic faces.  The number of pixels/rows is 12 * nside * nside.  The
  pixelization has two forms supported by this task.  These are called
  <span style="font-family: monospace;">"nested"</span> and <span style="font-family: monospace;">"ring"</span>.
  </p>
  <p>
  The HEALPix WCS task, <b>hpctran</b>, provides a translation between
  the table row number and a spherical coordinate.  It is up to the
  creator of the table to choose the spherical coordinate system.  This
  might be an equatorial, galactic, or super-galactic system.  There may
  be a keyword specifying the system.  This is the case with WMAP data.
  </p>
  <p>
  This task only provides the conversion.  Access to the <span style="font-family: monospace;">"pixel"</span> data
  requires other tools.  For binary tables the <b>tables</b> may be used.
  </p>
  <p>
  This task allows the spherical coordinates to be input and output in three
  forms, as hours and degrees (e.g. RA/DEC), as degrees (e.g.  l/b), and as
  radians.  On input one may use sexagesimal since IRAF automatically converts
  this to decimal.  On output the values are produced in decimal form.
  </p>
  <p>
  The output is provide in two ways to provide flexibility in scripting.  One
  is writing the results to the task parameters.  Note that it is recommended
  that tasks which write to there parameter be <span style="font-family: monospace;">"cached"</span> with the <b>cache</b>
  command to avoid problems with background submission or multiple scripts
  running in parallel.  The other output is printed to the standard output.
  Regardless of the direction of conversion the printed output is in the same
  order of row number, longitude, and latitude.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  A CMB WMAP file is obtained and one wants the temperature at a particular
  point on the sky.  Note that the WMAP format is <span style="font-family: monospace;">"nested"</span> and
  coordinate system is galactic.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hpctran lng=50.12 lat=-33.45
  2298092 50.12 -33.45000000000001
  cl&gt; = hpctran.row
  2298092
  cl&gt; tdump wmap_iqusmap_r9_5yr_K1_v3.fits col=TEMPERATURE row=2298092
  cl&gt; tdump ("wmap_iqusmap_r9_5yr_K1_v3.fits", col="TEMPERATURE",
  &gt;&gt;&gt; row=hpctran.row)
  </pre></div>
  </section>
  <section id="s_reference">
  <h3>Reference</h3>
  <p>
  <i>HEALPIX - a Framework for High Resolution Discretization, and Fast
  Analysis of Data Distributed on the Sphere</i>,
  by K.M. Gorski, Eric Hivon, A.J. Banday, B.D. Wandelt, F.K. Hansen, M.
  Reinecke, M. Bartelmann, 2005, ApJ 622, 759.
  </p>
  </section>
  <section id="s_credit">
  <h3>Credit</h3>
  <p>
  Some code from the HEALPix distribution at http://healpix.jpl.nasa.gov
  was translated to SPP for use in this routine.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ttools
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REFERENCE' 'CREDIT' 'SEE ALSO'  -->
  

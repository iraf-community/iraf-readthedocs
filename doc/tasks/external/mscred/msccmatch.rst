.. _msccmatch:

msccmatch: Match coordinates from list by adjusting WCS
=======================================================

**Package: mscred**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  A list of reference celestial coordinates, either from an astrometry
  catalog or measured from a reference image, for stars in the field is
  matched against objects in the mosaic data.  A linear relation between the
  observed positions and the reference coordinates is fit.  The relation may
  include a zero point shift, scale change, and axis rotation for both
  coordinate axes.  The removes pointing errors, rotation errors, and
  atmospheric refraction effects.  The fit is used to update the image world
  coordinate system to register the WCS to the input coordinate system.
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  msccmatch input coords
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input mosaic exposures to be calibrated.
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords' -->
  <dd>Coordinate filename or command to execute to produce a coordinate file.
  The file contains the right ascension and declination in the first two
  columns.  Any other columns are ignored.  When an explicit file is
  specified it used for all input exposures.
  A command to execute is specified by beginning the parameter string with
  <span style="font-family: monospace;">"!"</span>.  The special arguments $I will be replaced by the input mosaic
  exposure and $C by the filename for the coordinate file to be used.
  A typical command is
  <div class="highlight-default-notranslate"><pre>
  !mscgetcatalog $I $C
  </pre></div>
  Note that any hidden parameters either need to be set first or be given
  explicitly as part of the command.
  </dd>
  </dl>
  <dl id="l_outcoords">
  <dt><b>outcoords = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outcoords' Line='outcoords = ""' -->
  <dd>Optional list of updated coordinate files to output.  The list is matched
  with the input list of mosaic exposures.  If the list is shorter than the
  input list then no output files are created for the remaining exposures.
  The output coordinate file consists of those lines in the input coordinates
  which were used; i.e. were found to be in the field, were not rejected due
  to bad pixels, and which where centered without error.
  </dd>
  </dl>
  <dl id="l_usebpm">
  <dt><b>usebpm = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='usebpm' Line='usebpm = yes' -->
  <dd>Use bad pixel masks given by the BPM header keywords to reject sources
  that contain bad pixels?
  </dd>
  </dl>
  <p>
  The following parameters are for a coarse correlation search with large
  offsets but small rotation.
  </p>
  <dl id="l_nsearch">
  <dt><b>nsearch = 50</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsearch' Line='nsearch = 50' -->
  <dd>Maximum number of positions to use in search.  If this is zero then the
  coarse search is skipped and the coordinates are assumed to be close enough
  to centroid directly on the objects.  If the coarse search is selected then
  this number should not be too large, otherwise the execution time will
  become long.
  </dd>
  </dl>
  <dl id="l_search">
  <dt><b>search = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='search' Line='search = 0.' -->
  <dd>Translation search radius in arcsec.  If this is zero then the coarse
  serach is skipped and the coordinates are assumed to be close enough to
  centroid directly.  This defines how far from the initial coordinates to
  search using the <i>nsearch</i> objects.  It should be just large enough to
  include the expected error in the initial coordinates.
  </dd>
  </dl>
  <dl id="l_rsearch">
  <dt><b>rsearch = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rsearch' Line='rsearch = 0.' -->
  <dd>Rotation search radius in degrees.  This defines a range of rotations about
  the current tangent point that might be needed to find the correlation match.
  The correlation algorithm only works with small rotations or order a
  degree.
  </dd>
  </dl>
  <p>
  The follwoing parameters are for the fine centroiding and coordinate
  solution based on the centroiding.
  </p>
  <dl id="l_nfit">
  <dt><b>nfit = 4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nfit' Line='nfit = 4' -->
  <dd>The minimum number of sources which must be found and centroided for an
  acceptable coordinate fit.  If the value is negative then this is the
  maximum number of objects which failed to be found for an acceptable
  solution.
  </dd>
  </dl>
  <dl id="l_rms">
  <dt><b>rms = 2.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rms' Line='rms = 2.' -->
  <dd>The maximum RMS in arcsec for an acceptable solution. 
  </dd>
  </dl>
  <dl id="l_maxshift">
  <dt><b>maxshift = 5</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxshift' Line='maxshift = 5' -->
  <dd>Maximum centering shift in arcsec when centroiding.  Sources that produce
  centroids (from the <b>center</b> task) that differ from the initial
  position by more than this amount are considered to have failed to be
  centroided.
  </dd>
  </dl>
  <dl id="l_fitgeometry">
  <dt><b>fitgeometry = <span style="font-family: monospace;">"general"</span> (shift|xyscale|rotate|rscale|rxyscale|general)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fitgeometry' Line='fitgeometry = "general" (shift|xyscale|rotate|rscale|rxyscale|general)' -->
  <dd>Fitting geometry for the coordinate adjustment.  This should normally be
  <span style="font-family: monospace;">"general"</span> to all allow for all effects of atmospheric refraction.  The
  other options are only used when looking for specific effects.
  </dd>
  </dl>
  <dl id="l_reject">
  <dt><b>reject = 3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='reject' Line='reject = 3.' -->
  <dd>Iterative rejection sigma for fitting the position residuals as a function
  of arcsec from the field tangent point.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = yes' -->
  <dd>Update the coordinate system in the mosaic exposures?  If the value is no then
  the input data is not modified.  This option might be used just to check
  the coordinate system.  If the the value is yes and the fit satisfies the
  parameters defining an acceptable solution the coordinate system will be
  updated if <i>interactive</i>=no, otherwise there is a query whether to
  accept the solution and update the input data.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = yes' -->
  <dd>Is this task to be run interactively?  If yes then the fitting can be
  examined and adjusted interactively if the <i>fit</i> parameter is yes and
  the final solution will be printed followed by a query to accept the
  solution provided the <i>update</i> parameter is yes.
  </dd>
  </dl>
  <dl id="l_fit">
  <dt><b>fit = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fit' Line='fit = yes' -->
  <dd>Do the coordinate fitting interactively?  This required the <i>interactive</i>
  parameter to be yes.  If the fitting is done interactively the <b>geomap</b>
  task used to do the fitting will be executed interactively.  The graphical
  fitting is exited using the <span style="font-family: monospace;">'q'</span> key.  See the help for <b>geomap</b>
  for more on the interactive fitting.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Verbose output?  This determines whether various terminal output is
  produced.
  </dd>
  </dl>
  <dl id="l_listcoords">
  <dt><b>listcoords = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listcoords' Line='listcoords = yes' -->
  <dd>List centroiding results for all sources in verbose mode?
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Graphics device for the interactive fitting.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input for the interactive fitting.  The default null
  string value selects the graphics window cursor.
  </dd>
  </dl>
  <dl id="l_accept">
  <dt><b>accept = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='accept' Line='accept = yes' -->
  <dd>This is a query parameter when <i>update</i> and <i>interactive</i> are yes.
  You are queried after printing the statistics of the coordinate fit whether
  to accept the solution and update the coordinate system of the mosaic
  exposure.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A list of reference celestial coordinates, either from an astrometry
  catalog or measured from a reference image, for stars in the field is
  matched against objects in the mosaic data.  A linear relation between the
  observed positions and the reference coordinates is fit.  The relation may
  include a zero point shift, scale change, and axis rotation for both
  coordinate axes.  The removes pointing errors, rotation errors, and
  atmospheric refraction effects.  The fit is used to update the image world
  coordinate system to register the WCS to the input coordinate system.
  </p>
  <p>
  A full description of this task remains to be written.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MSCCMATCH">
  <dt><b>MSCCMATCH - V4.0: August 22, 2000</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MSCCMATCH' Line='MSCCMATCH - V4.0: August 22, 2000' -->
  <dd>This version includes the ability to get the list of catalogs directly from
  a web-based catalog server and to find large offsets (provided any rotation
  is small) using a correlation algorithm.
  </dd>
  </dl>
  <dl id="l_MSCCMATCH">
  <dt><b>MSCCMATCH - V2.11 external package</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MSCCMATCH' Line='MSCCMATCH - V2.11 external package' -->
  <dd>First release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  msczero, mscgetcatalog, geomap, center
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

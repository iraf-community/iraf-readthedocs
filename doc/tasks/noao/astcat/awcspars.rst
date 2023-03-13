.. _awcspars:

awcspars: Default image wcs parameters
======================================

**Package: astcat**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  awcspars 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_wxref">
  <dt><b>wxref = <span style="font-family: monospace;">"INDEF"</span>, wyref = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wxref' Line='wxref = "INDEF", wyref = "INDEF"' -->
  <dd>The image header keyword names or the numerical values of the x and y reference
  point in pixels. If wxref = <span style="font-family: monospace;">"INDEF"</span> and wyref = <span style="font-family: monospace;">"INDEF"</span> the reference
  point defaults to the center of the image.
  </dd>
  </dl>
  <dl id="l_wxmag">
  <dt><b>wxmag = <span style="font-family: monospace;">"INDEF"</span>, wymag = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wxmag' Line='wxmag = "INDEF", wymag = "INDEF"' -->
  <dd>The image header keyword names or the numerical values of the x and y scale
  factors in arcseconds per pixel. If wxmag  or wymag = are undefined a new
  wcs cannot be created.
  </dd>
  </dl>
  <dl id="l_wxrot">
  <dt><b>wxrot = <span style="font-family: monospace;">"180.0"</span>, wyrot = <span style="font-family: monospace;">"0.0"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wxrot' Line='wxrot = "180.0", wyrot = "0.0"' -->
  <dd>The image header keyword names or the numerical values of the x and y rotation
  angles in degrees measured counter-clockwise to the positive x and y image
  axes. The default orientation is east=left, north=up. Wxrot values of 0.0,
  90.0, 180.0, and 270.0 correspond to east=right, up, left, and down
  respectively. Wyrot values of 0.0, 90.0, 180.0, and 270.0 correspond to
  north=up, left, down, and right respectively.
  </dd>
  </dl>
  <dl id="l_wraref">
  <dt><b>wraref = <span style="font-family: monospace;">"RA"</span>, wdecref = <span style="font-family: monospace;">"DEC"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wraref' Line='wraref = "RA", wdecref = "DEC"' -->
  <dd>The image header keyword names or the numerical values of the reference
  point in celestial coordinates. If wraref and wdecref are undefined
  a new wcs cannot be created.
  </dd>
  </dl>
  <dl id="l_wraunits">
  <dt><b>wraunits = <span style="font-family: monospace;">""</span>, wdecunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wraunits' Line='wraunits = "", wdecunits = ""' -->
  <dd>The units of the reference point celestial coordinates. The options are
  <span style="font-family: monospace;">"hours"</span>, <span style="font-family: monospace;">"degrees"</span>, and <span style="font-family: monospace;">"radians"</span> for the ra coordinate and <span style="font-family: monospace;">"degrees"</span>
  and <span style="font-family: monospace;">"radians"</span> for the dec coordinate. If wraunits and wdecunits are undefined
  they default to the preferred units of the reference system.
  </dd>
  </dl>
  <dl id="l_wproj">
  <dt><b>wproj = <span style="font-family: monospace;">"tan"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wproj' Line='wproj = "tan"' -->
  <dd>The sky projection geometry. The most commonly used projections are <span style="font-family: monospace;">"tan"</span>,
  <span style="font-family: monospace;">"arc"</span>, <span style="font-family: monospace;">"sin"</span>, and <span style="font-family: monospace;">"lin"</span>. Other supported projections are <span style="font-family: monospace;">"ait"</span>,<span style="font-family: monospace;">"car"</span>, <span style="font-family: monospace;">"csc"</span>,
  <span style="font-family: monospace;">"gls"</span>, <span style="font-family: monospace;">"mer"</span>, <span style="font-family: monospace;">"mol"</span>, <span style="font-family: monospace;">"par"</span>, <span style="font-family: monospace;">"pco"</span>, <span style="font-family: monospace;">"qsc"</span>, <span style="font-family: monospace;">"stg"</span>, <span style="font-family: monospace;">"tsc"</span>, and <span style="font-family: monospace;">"zea"</span>.
  </dd>
  </dl>
  <dl id="l_wsystem">
  <dt><b>wsystem = <span style="font-family: monospace;">"EQUINOX"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wsystem' Line='wsystem = "EQUINOX"' -->
  <dd>The image header keyword name or string defining the celestial coordinate
  system of the reference point. The most common values for wsystem are
  <span style="font-family: monospace;">"2000.0"</span>, <span style="font-family: monospace;">"1950.0"</span>, <span style="font-family: monospace;">"J2000.0"</span>, and <span style="font-family: monospace;">"B1950.0"</span>. Type <span style="font-family: monospace;">"help ccssytems"</span> to get
  a full list of options.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The default wcs parameters are used to create an approximate  FITS wcs for
  an images which do not have one. Creating an approximate header
  from the telescope pointing position and the known scale and orientation
  of the detector can make later steps like locating the catalog stars
  for computing an accurate plate solution simpler.
  </p>
  <p>
  In coordinates of the reference point in pixels and celestial coordinates
  <i>wxref</i>, <i>wyref</i>, <i>wraref</i>, <i>wdecref</i>, the scale factors
  <i>wxmag</i> and <i>wymag</i>, and the orientation <i>wxrot</i> and <i>wyrot</i>
  can be read from the image header or set by value. The coordinate system
  and units of the celestial coordinates of the reference point <i>wsystem</i>
  and <i>wraunits</i> and <i>wdecunits</i> must be set explicitly. The image
  projection function <i>wproj</i> must also be set separately.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the default wcs parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lpar awcspars
  </pre></div>
  <p>
  2. Edit the default wcs parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; awcspars
  </pre></div>
  <p>
  3. Edit the default wcs parameters from the agetim task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epar agetim
  </pre></div>
  <p>
  4. Save the current awcspars parameter values in a text file called
  awcs1.par.  Use the saved parameter set in the next call to the agetim
  task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epar awcspars
  cl&gt; agetim ... awcspars=awcs1.par ...
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
  agetim, ahedit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

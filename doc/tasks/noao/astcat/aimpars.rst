.. _aimpars:

aimpars: Default image data parameters
======================================

**Package: astcat**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  aimpars
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_observat">
  <dt><b>observat = <span style="font-family: monospace;">"OBSERVAT"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observat' Line='observat = "OBSERVAT"' -->
  <dd>The image header keyword defining the observatory at which the data
  was taken or the name of the observatory. If the observatory is defined then
  the keyword <span style="font-family: monospace;">"OBSERVAT"</span> is written to the image header if it does not
  already exist. 
  </dd>
  </dl>
  <dl id="l_esitelng">
  <dt><b>esitelng = <span style="font-family: monospace;">"INDEF"</span>, esitelat = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='esitelng' Line='esitelng = "INDEF", esitelat = "INDEF"' -->
  <dd>The image header keywords defining the longitude and latitude of the
  observatory in degrees or the longitude and latitude values in degrees.
  If the longitude and latitude are defined the keywords <span style="font-family: monospace;">"ESITELNG"</span> and
  <span style="font-family: monospace;">"ESITELAT"</span> are written to the image header if they do not already exist.
  </dd>
  </dl>
  <dl id="l_esitealt">
  <dt><b>esitealt = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='esitealt' Line='esitealt = "INDEF"' -->
  <dd>The image header keyword defining the altitude of the observatory in meters
  or the altitude itself in meters. If the altitude is defined the keyword
  <span style="font-family: monospace;">"ESITEALT"</span> is written to the image header if it does not already exist.
  </dd>
  </dl>
  <dl id="l_esitetz">
  <dt><b>esitetz = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='esitetz' Line='esitetz = "INDEF"' -->
  <dd>The image header keyword defining the timezone of the observatory 
  in hours from the Greenwich meridian or the timezone value 
  in hours from the Greenwich meridian. Positive values correspond to time
  zones west of the meridian. If the time zone is defined the keyword
  <span style="font-family: monospace;">"ESITETZ"</span> is written to the image header if it does not already exist.
  </dd>
  </dl>
  <dl id="l_emjdobs">
  <dt><b>emjdobs = <span style="font-family: monospace;">"MJD-OBS"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='emjdobs' Line='emjdobs = "MJD-OBS"' -->
  <dd>The image header keyword defining the effective MJD of the observation
  or the MJD. MJD-OBS normally defines the time of the beginning
  of the observation. Users may wish to change this value to represent
  the MJD at mid-exposure.  If the effective MJD is defined the keyword
  <span style="font-family: monospace;">"EMJDOBS"</span> is written to the image header if it does not already exist.
  </dd>
  </dl>
  <dl id="l_edatamin">
  <dt><b>edatamin = <span style="font-family: monospace;">"INDEF"</span>, edatamax = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='edatamin' Line='edatamin = "INDEF", edatamax = "INDEF"' -->
  <dd>The image header keywords defining the minimum and maximum good data
  limits in ADU or the minimum and maximum good data values in ADU.
  If these limits are defined the keywords <span style="font-family: monospace;">"EDATAMIN"</span> and <span style="font-family: monospace;">"EDATAMAX"</span> 
  are written to the image header if they do not already exist.
  </dd>
  </dl>
  <dl id="l_egain">
  <dt><b>egain = <span style="font-family: monospace;">"GAIN"</span>, erdnoise = <span style="font-family: monospace;">"RDNOISE"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='egain' Line='egain = "GAIN", erdnoise = "RDNOISE"' -->
  <dd>The image header keywords defining the effective gain in electrons per ADU 
  and readout noise in electrons or the gain and readout noise values in 
  electrons per ADU and electrons. If the gain and readout noise are defined
  the keywords <span style="font-family: monospace;">"EGAIN"</span> and <span style="font-family: monospace;">"ERDNOISE"</span> are written to the image header if they do
  not already exist.
  </dd>
  </dl>
  <dl id="l_ewavlen">
  <dt><b>ewavlen = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ewavlen' Line='ewavlen = "INDEF"' -->
  <dd>The image header keyword defining the effective wavelength in microns or
  the effective wavelength value in microns. If the effective wavelength is
  defined the keyword <span style="font-family: monospace;">"EWAVLEN"</span> is written to the image header if it does
  not already exist.
  </dd>
  </dl>
  <dl id="l_etemp">
  <dt><b>etemp = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='etemp' Line='etemp = "INDEF"' -->
  <dd>The image header keyword defining the effective temperature in degrees
  or the effective temperature values in degrees. If the effective wavelength
  is defined the keyword <span style="font-family: monospace;">"ETEMP"</span> is written to the image header it does
  not already exist.
  </dd>
  </dl>
  <dl id="l_epress">
  <dt><b>epress = <span style="font-family: monospace;">"INDEF"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='epress' Line='epress = "INDEF"' -->
  <dd>The image header keyword defining the effective pressure in millibars or
  the effective pressure values in millibars. If the effective pressure is
  defined the keyword <span style="font-family: monospace;">"EPRESS"</span> is written to the image header if it does
  not already exist.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The standard image parameter set is used to encode quantities in the image
  headers that may be required by the astrometric analysis tasks. The current
  parameter set divides into two parameter groups: parameters
  concerned with locating stars in an image and computing accurate pixel
  coordinates and instrumental magnitudes <i>edatamin</i>, <i>edatamax</i>,
  <i>egain</i>, and <i>erdnoise</i>, and parameters required to transform
  from mean to observed place <i>observat</i>, <i>esiteng</i>,
  <i>esitelat</i>, <i>esitealt</i>, <i>esitetz</i>, <i>ewavlen</i>,
  <i>etem</i>, <i>epress</i>. The latter group of parameter is required for
  astrometric analyses carried out in observed place rather than
  mean place.
  </p>
  <p>
  If the quantity defined by the aimpars parameter is defined, i.e. the
  parameter value is an image header keyword which defines a valid value,
  or the parameter value is itself a valid value, then a keyword 
  with the same name as the parameter name is inserted into the image
  header, if one with that name does not already exist.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the default image header parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lpar aimpars
  </pre></div>
  <p>
  2. Edit the default image header parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; aimpars
  </pre></div>
  <p>
  3. Edit the default image header parameters from the agetim task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epar agetim
  </pre></div>
  <p>
  4. Save the current awcspars parameter values in a text file called
  aimhdr1.par.  Use the saved parameter set in the next call to the agetim
  task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epar aimpars
  cl&gt; agetim ... aimpars=aimhdr1.par ...
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
  agetim
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

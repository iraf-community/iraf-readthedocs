.. _sapertures:

sapertures: Set or change aperture header information
=====================================================

**Package: kpnocoude**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  sapertures input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of spectral images to be modified.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>List of apertures to be modified.  The null list
  selects all apertures.  A list consists of comma separated
  numbers and ranges of numbers.  A range is specified by a hyphen.  An
  optional step size may be given by using the <span style="font-family: monospace;">'x'</span> followed by a number.
  See <b>xtools.ranges</b> for more information.
  </dd>
  </dl>
  <dl id="l_apidtable">
  <dt><b>apidtable = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apidtable' Line='apidtable = ""' -->
  <dd>Aperture table.  This may be either a text file or an image.
  A text file consisting of lines with an aperture number,
  beam number, dispersion type code, coordinate of the first physical
  pixel, coordinate interval per physical pixel, redshift factor,
  lower extraction aperture position, upper extraction aperture position,
  and aperture title or identification.  An image will contain the
  keywords SLFIBnnn with string value consisting of aperture number,
  beam number, optional right ascension and declination, and aperture title.
  Any field except the aperture number may be given the value INDEF to
  indicate that the value is not to be changed from the current value.  Any
  apertures not in this table are assigned the values given by the task
  parameters described below.
  As a special case a file having just the aperture number, beam number, and
  spectrum aperture identification may be used.  This file format as well as
  use of an image header is the same as that in the <b>apextract</b> package.
  </dd>
  </dl>
  <dl id="l_wcsreset">
  <dt><b>wcsreset = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wcsreset' Line='wcsreset = no' -->
  <dd>Reset the world coordinate system (WCS) of the selected apertures to
  uncorrected pixels.  If this parameter is set the <i>apidtable</i> and task
  aperture parameters are ignored.  This option sets the dispersion type flag
  to -1, the starting coordinate value to 1, the interval per pixel to 1, and
  no redshift factor and leaves the other parameters unchanged.  The option
  is useful when it is desired to apply a second dispersion correction using
  <b>identify</b> and <b>dispcor</b>.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print a record of each aperture modified?  Only those apertures 
  in which the beam number or label are changed are printed.
  </dd>
  </dl>
  <p>
  If no aperture table is specified or if there is not an aperture
  entry in the table for a selected aperture the following parameter
  values are used.  A value of INDEF will leave the corresponding
  parameter unchanged.
  </p>
  <dl id="l_beam">
  <dt><b>beam = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='beam' Line='beam = INDEF' -->
  <dd>Beam number.
  </dd>
  </dl>
  <dl id="l_dtype">
  <dt><b>dtype = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dtype' Line='dtype = INDEF' -->
  <dd>Dispersion type.  The dispersion types are:
  <div class="highlight-default-notranslate"><pre>
  -1  Linear with dispersion correction flag off
   0  Linear with dispersion correction flag on
   1  Log-linear with dispersion correction flag on
  </pre></div>
  </dd>
  </dl>
  <dl id="l_w1">
  <dt><b>w1 = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='w1' Line='w1 = INDEF' -->
  <dd>Coordinate of the first physical pixel.  Note that it is possible
  that the physical pixels are not the same as the logical pixels if
  an image section has been extracted.
  </dd>
  </dl>
  <dl id="l_dw">
  <dt><b>dw = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dw' Line='dw = INDEF' -->
  <dd>Coordinate interval per physical pixel.  Note that it is possible
  that the physical pixels intervals are not the same as the logical pixels
  intervals if an image section has been extracted.
  </dd>
  </dl>
  <dl id="l_z">
  <dt><b>z = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='z' Line='z = INDEF' -->
  <dd>Redshift factor.  This is usually set with the task <b>dopcor</b>.
  Coordinates are divided by one plus the redshift factor (1+z).
  </dd>
  </dl>
  <dl id="l_aplow">
  <dt><b>aplow = INDEF, aphigh = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='aplow' Line='aplow = INDEF, aphigh = INDEF' -->
  <dd>The aperture extraction limits.  These are set when the <b>apextract</b>
  package is used and it is unlikely that one would use this task to
  change them.
  </dd>
  </dl>
  <dl id="l_title">
  <dt><b>title = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='title' Line='title = INDEF' -->
  <dd>Aperture title or identification string.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task sets or changes any of the aperture specific parameters except
  the aperture number and the number of  valid pixels.  It is particularly
  useful for images which use the <span style="font-family: monospace;">"multispec"</span> world coordinate system
  attribute strings which are not readily accessible with other header
  editors.  A list of images and a list of apertures is used to select which
  spectra are to be modified.  The default empty string for the apertures
  selects all apertures.  The new values are specified either in an aperture
  table file or with task parameters.  The aperture table is used to give
  different values to specific apertures.  If all apertures are to have the
  same values this file need not be used.
  </p>
  <p>
  The aperture parameters which may be modified are the beam number, the
  dispersion type, the coordinate of the first physical pixel, the coordinate
  interval per physical pixel, the redshift factor, the aperture extraction
  limits, and the title.  The task has parameters for each of these and the
  aperture table consists of lines starting with an aperture number followed
  by the above parameters in the list order and separated by whitespace.  As
  a special case the aperture table may be a file abbreviated to aperture
  number, beam number, and title or an image with keywords SLFIBnnn
  containing the aperture number, beam number, optional right ascension and
  declination, and title.  These special cases allow use of the same file
  orimage used in the <b>apextract</b> package.  If any of the parameters are
  specified as INDEF then the value will be unchanged.
  </p>
  <p>
  If the <i>wcsreset</i> parameter is set then the aperture table and
  task aperture parameters are ignored and the selected apertures are
  reset to have a dispersion type of -1, a starting coordinate of 1,
  a coordinate interval of 1, and a redshift factor of 0.  This other
  parameters are not changed.  These choice of parameters has the effect
  of resetting the spectrum to physical pixel coordinates and flagging
  the spectra as not being dispersion calibrated.  One use of this option
  is to allow the <b>dispcor</b> task to be reapplied to previously
  dispersion calibrated spectra.
  </p>
  <p>
  The <i>verbose</i> parameter lists the old and new values when there is
  a change.  If there are no changes there will be no output.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To add titles to a multifiber extraction and change one of the
  beam numbers:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type m33aps
  36 2 Henear
  37 0 Sky
  38 1 New title
  39 1 Another title
  41 0 Sky
  42 1 Yet another title
  43 1 YAT
  44 1 Was a sky but actually has an object
  45 1 Wow
  46 1 Important new discovery
  47 0 Sky
  48 2 Henear
  cl&gt; saper m33.ms apid=m33aps v+
  demoobj1.ms:
    Aperture 37:  --&gt; Sky
    Aperture 38:  --&gt; New title
    Aperture 39:  --&gt; Another title
    Aperture 41:  --&gt; Sky
    Aperture 42:  --&gt; Yet another title
    Aperture 43:  --&gt; YAT
    Aperture 44: beam 0 --&gt; beam 1
    Aperture 44:  --&gt; Was a sky but actually has an object
    Aperture 45:  --&gt; Wow
    Aperture 46:  --&gt; Important new discovery
    Aperture 47:  --&gt; Sky
  </pre></div>
  <p>
  2.  To reset a dispersion calibrated multifiber spectrum:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; saper test.ms wcsreset+ verbose+
  test.ms:
    Aperture 1:
      w1 4321. --&gt; 1.
      dw 1.23 --&gt; 1.
    Aperture 2:
      w1 4321. --&gt; 1.
      dw 1.23 --&gt; 1.
    &lt;etc.&gt;
  </pre></div>
  <p>
  3.  To set a constant wavelength length scale (with the default parameters):
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; saper test.ms dtype=0 w1=4321 dw=1.23 v+
  test.ms:
    Aperture 1:
      w1 1. --&gt; 4321.
      dw 1. --&gt; 1.23
    Aperture 2:
      w1 1. --&gt; 4321.
      dw 1. --&gt; 1.23
    &lt;etc.&gt;
  </pre></div>
  <p>
  4. To reset the wavelengths and title of only aperture 3:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; saper test.ms aper=3 w1=4325 dw=1.22 title=HD12345 v+
  test.ms:
    Aperture 3:
      w1 4321. --&gt; 4325.
      dw 1.23 --&gt; 1.22
      apid  --&gt; HD12345
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_SAPERTURES">
  <dt><b>SAPERTURES V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SAPERTURES' Line='SAPERTURES V2.11' -->
  <dd>This task has been modified to allow use of image header keywords
  as done in the APEXTRACT package.
  </dd>
  </dl>
  <dl id="l_SAPERTURES">
  <dt><b>SAPERTURES V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SAPERTURES' Line='SAPERTURES V2.10.3' -->
  <dd>This task has been greatly expanded to allow changing any of the WCS
  parameters as well as the beam number and aperture title.
  </dd>
  </dl>
  <dl id="l_SAPERTURES">
  <dt><b>SAPERTURES V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SAPERTURES' Line='SAPERTURES V2.10' -->
  <dd>This task is new.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  specshift, imcoords.wcsreset, hedit, ranges, onedspec.package
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

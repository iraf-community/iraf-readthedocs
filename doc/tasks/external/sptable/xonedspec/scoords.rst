.. _scoords:

scoords: Set spectral coordinates as a pixel array (1D spectra only)
====================================================================

**Package: xonedspec**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  scoords images coords
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of one dimensional spectrum image names.
  </dd>
  </dl>
  <dl id="l_coords">
  <dt><b>coords</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coords' Line='coords' -->
  <dd>List of file names containing the coordinate values.  There may be
  one file which applies to all input images or a matching list
  of one coordinate file for each input image.  The coordinate files
  are a list of coordinate values with one coordinate per line.
  The coordinates must be ordered in increasing or decreasing value.
  The number of coordinates must match the number of pixels in the image.
  </dd>
  </dl>
  <dl id="l_label">
  <dt><b>label = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='label' Line='label = ""' -->
  <dd>Optional coordinate axis label.  A typical value is <span style="font-family: monospace;">"Wavelength"</span>
  for wavelength coordinates.
  </dd>
  </dl>
  <dl id="l_units">
  <dt><b>units = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='units' Line='units = ""' -->
  <dd>Optional coordinate axis units.  A typical value is <span style="font-family: monospace;">"Angstroms"</span>.  In
  order to allow coordinate conversions by other IRAF spectra tasks
  the value should be specified as one of the known units
  (see units description in <b>onedspec.package</b>).
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print a line as each spectrum is processed?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Scoords</b> sets spectral coordinates in one dimensional spectral
  images as a list of coordinates in the image header.  The
  coordinate file(s) consists of coordinate values given one per line.
  Each coordinate value is assigned to an image pixel in the order given
  and so the number of coordinate values must match the number of pixels
  in the spectrum.  Also the coordinates must be monotonically increasing
  or decreasing.
  </p>
  <p>
  When multiple spectra are to be set a matching list of coordinates can
  be specified or a single coordinate file for all images may be used.
  </p>
  <p>
  The coordinate system set in the header is an example of the <span style="font-family: monospace;">"multispec"</span>
  world coordinate system.  This is understood by all the standard
  IRAF tasks.  It is described under the help topic <span style="font-family: monospace;">"onedspec.specwcs"</span>.
  Once the coordinates are set one may resample the spectrum to a
  more compact linear description using the task <b>dispcor</b>.
  </p>
  <p>
  Since the coordinate values are stored in the header (double
  precision numbers) the header can become quite large if the spectrum
  is long.  Be sure the environment variable <span style="font-family: monospace;">"min_lenuserarea"</span> which
  defines the maximum size of the image header in number of characters
  is large enough to hold all the coordinates.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Set the coordinates for a spectrum.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type coords.dat
  4000.
  4010.123
  4020.246
  4031.7
  &lt;etc&gt;
  cl&gt; scoords spec coords.dat label=Wavelength units=Angstroms
  cl&gt; listpix spec wcs=world
  4000.       124.
  4010.123    543
  &lt;etc&gt;
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_SCOORDS">
  <dt><b>SCOORDS V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SCOORDS' Line='SCOORDS V2.11' -->
  <dd>This is a new task with this version.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  rtextimage, dispcor, specwcs, onedspec.package
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

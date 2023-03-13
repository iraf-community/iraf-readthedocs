.. _specshift:

specshift: Shift spectral dispersion coordinate systems
=======================================================

**Package: kpnoslit**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  specshift spectra shift
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_spectra">
  <dt><b>spectra</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectra' Line='spectra' -->
  <dd>List of spectra to be modified.
  </dd>
  </dl>
  <dl id="l_shift">
  <dt><b>shift</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shift' Line='shift' -->
  <dd>Dispersion coordinate shift to be added to the current dispersion coordinate
  system.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>List of apertures to be modified.  The null list
  selects all apertures.  A list consists of comma separated
  numbers and ranges of numbers.  A range is specified by a hyphen.  An
  optional step size may be given by using the <span style="font-family: monospace;">'x'</span> followed by a number.
  See <b>xtools.ranges</b> for more information.  This parameter is ignored
  for N-dimensional spatial spectra such as long slit and Fabry-Perot.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print a record of each aperture modified?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task applies a shift to the dispersion coordinate system of selected
  spectra.  The image data is not modified as with <b>imshift</b> but rather
  the coordinate system is shifted relative to the data.  The spectra to be
  modified are selected by specifying a list of images and apertures.  If no
  aperture list is specified then all apertures in the images are modified.
  For N-dimensional spatial spectra such as long slit and Fabry-Perot the
  aperture list is ignored.
  </p>
  <p>
  The specified shift is added to the existing world coordinates.  For linear
  coordinate systems this has the effect of modifying CRVAL1, for linear
  <span style="font-family: monospace;">"multispec"</span> coordinate systems this modifies the dispersion coordinate of
  the first physical pixel, and for nonlinear <span style="font-family: monospace;">"multispec"</span> coordinate systems
  this modifies the shift coefficient(s).
  </p>
  <p>
  It is also possible to shift the linearized coordinate systems (but not the
  nonlinear coordinate systems) with <b>sapertures</b> or possibly with
  <b>wcsedit</b> or <b>hedit</b> if the coordinate system is stored with a
  global linear system.
  </p>
  <p>
  The <i>verbose</i> parameter lists the images, the apertures, the shift, and
  the old and new values for the first physical pixel are printed.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To add 1.23 Angstroms to the coordinates of all apertures in the
  image <span style="font-family: monospace;">"ngc456.ms"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; specshift ngc456.ms 1.23
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_SPECSHIFT">
  <dt><b>SPECSHIFT V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='SPECSHIFT' Line='SPECSHIFT V2.10.3' -->
  <dd>First version.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  sapertures, dopcor, imcoords.wcsreset, hedit, ranges, onedspec.package
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

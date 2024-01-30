.. _emplot:

emplot: Plot a spectrum with emission velocity and labelled lines
=================================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  emplot spectra
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_spectra">
  <dt><b>spectra = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectra' Line='spectra = ""' -->
  <dd>List of file names of spectra to plot
  </dd>
  </dl>
  <dl id="l_specband">
  <dt><b>specband = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specband' Line='specband = 0' -->
  <dd>Spectrum band to plot. If 0, plot the first or only spectrum in the file.
  </dd>
  </dl>
  <dl id="l_specnum">
  <dt><b>specnum = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specnum' Line='specnum = ""' -->
  <dd>Spectrum aperture range to plot
  </dd>
  </dl>
  <dl id="l_specdir">
  <dt><b>specdir = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='specdir' Line='specdir = ""' -->
  <dd>Directory for spectrum to plot
  </dd>
  </dl>
  <dl id="l_emlines">
  <dt><b>emlines = <span style="font-family: monospace;">"emlines.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='emlines' Line='emlines = "emlines.dat"' -->
  <dd>File of emission lines to label.
  </dd>
  </dl>
  <dl id="l_ablines">
  <dt><b>ablines = <span style="font-family: monospace;">"ablines.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ablines' Line='ablines = "ablines.dat"' -->
  <dd>File of absorption lines to label.
  </dd>
  </dl>
  <dl id="l_linedir">
  <dt><b>linedir = <span style="font-family: monospace;">"rvsao$lib/"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linedir' Line='linedir = "rvsao$lib/"' -->
  <dd>Directory for lines to label
  </dd>
  </dl>
  <p>
   
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  EMPLOT runs EMSAO without fitting lines in the spectrum and displays
  the spectrum with lines labelled and previously-obtained results, if any.
  Type <span style="font-family: monospace;">"q"</span> to go on to the next spectrum in a list.
  Type <span style="font-family: monospace;">"?"</span> or space to get a menu of cursor commands.
  </p>
  </section>
  <section id="s_cursor_commands">
  <h3>Cursor commands</h3>
  <div class="highlight-default-notranslate"><pre>
  a  Set redshift guess from absorption line
  b  Set blue limit of line search
  c  Change continuum parameters
  d  Delete data between 1st and 2nd positions
  e  Set redshift guess from emission line
  f  Refit redshift
  g  Number of times to smooth plotted spectrum
  h  Toggle print of heading with filename and redshift
  i  Change initial velocity for search
  j  Conditional velocity
  k  Plot continuum-subtracted spectrum
  l  Line search parameters
  m  Number of times to smooth fit spectrum
  n  Disapprove velocity
  o  Turn line labelling on and off
  p  Replot current graph
  q  Leave plot
  r  Set red limit of line search
  s  Set VELOCITY to a specific value
  t  Switch template for correlation velocity
  u  Unzoom
  v  Plot at e&gt;mission x&gt;correlation c&gt;ombined velocity
  w  Show rest and observed wavelengths
  x  Plot correlation if available or exit
  y  Approve velocity
  z  Zoom between 1st and 2nd positions
  .  Cancel delete or zoom
  /  Toggle plot between full screen and lines
  +  Add emission line to fit
  -  Subtract emission line from fit
  (  Plot previous aperture or order
  &gt;  Plot next aperture or order
  @  Make hard copy of screen
  ?  Display this menu
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To plot a spectrum,
  </p>
  <p>
          cl&gt; emplot galaxy.ms.fits
  </p>
  <p>
  To plot a whole night's worth of spectra:
  </p>
  <p>
          cl&gt; emplot @nite1.ls
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'CURSOR COMMANDS' 'EXAMPLES' 'BUGS'  -->
  

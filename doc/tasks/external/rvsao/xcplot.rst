.. _xcplot:

xcplot: Plot a spectrum with xc velocity and labelled lines
===========================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  xcplot spectra
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
  <p>
   
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  XCPLOT runs XCSAO without correlating the spectrum with a template
  and simply displays the spectrum.  Parameters for line labelling
  and other functions are those already set in XCSAO.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To plot a spectrum,
  </p>
  <p>
          cl&gt; xcplot galaxy.ms.fits
  </p>
  <p>
  To plot the spectra for a whole night's worth of spectra:
  </p>
  <p>
          cl&gt; skyplot @nite1.ls
  </p>
  <p>
  Type <span style="font-family: monospace;">"q"</span> to move on to the next spectrum.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS'  -->
  

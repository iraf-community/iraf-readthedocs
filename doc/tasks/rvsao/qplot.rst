.. _qplot:

qplot: Check results of previously-run xcsao and emsao
======================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  qplot spectra
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_spectra">
  <dt><b>spectra = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectra' Line='spectra = ""' -->
  <dd>List of file names of spectra to analyze. @filename indicates list should
  come from file filename. As of version 1.3, apertures of multispec
  spectrum files can be entered as numbers, lists, or ranges enclosed in
  brackets after each file name in the list or file.  This parameter is
  directly passed to the task chosen below.
  </dd>
  </dl>
  <dl id="l_qtask">
  <dt><b>qtask = <span style="font-family: monospace;">"xcsao"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='qtask' Line='qtask = "xcsao"' -->
  <dd>Task to run (xcsao or emsao)<span style="font-family: monospace;">"}
  </dd>
  </dl>
  <dl id="l_velplot">
  <dt><b>velplot = "</span>combination<span style="font-family: monospace;">"</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='velplot' Line='velplot = "combination"' -->
  <dd>Velocity to plot (combination or emission or correlation
  </dd>
  </dl>
  <p>
   
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  QPLOT runs either XCSAO without correlating or EMSAO with finding new
  lines, then displays the spectrum with lines labelled and
  previously-obtained results.  These results should have been written
  to the image headers using save_vel=yes when XCSAO and EMSAO were run.
  The cursor mode is turned on, so that initial conditions can be changed
  (such as a new redshift guess or deleted cosmic ray) and the program
  (XCSAO or EMSAO) can be rerun.  The main reason for using QPLOT is to
  set a quality flag in the spectrum image header.  If the task is not
  rerun, only the summary information is rewritten.  If the spectrum is
  recorrelated or refit, the new results are only written to the spectrum
  header if a quality flag (y=OK, n=bad, j=questionable) is set.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To check the redshift of a single galaxy
  </p>
  <p>
          cl&gt; qplot galaxy
  </p>
  <p>
  To check redshifts for a whole night's worth of galaxy spectra:
  </p>
  <p>
          cl&gt; qplot @nite1.ls
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS'  -->
  

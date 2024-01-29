.. _qplotc:

qplotc: Check results of previously-run xcsao and emsao (-continuum and bad lines)
==================================================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  qplotc spectra
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
  <dt><b>velplot = "</span>combination<span style="font-family: monospace;">"   </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='velplot' Line='velplot = "combination"   ' -->
  <dd>Velocity to plot (combination or emission or correlation
  </dd>
  </dl>
  <dl id="l_dispmode">
  <dt><b>dispmode = 4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispmode' Line='dispmode = 4' -->
  <dd>Format in which to display summary page on an interactive display device
  and on the hard-copy device plotter. If the format code is negated, the
  spectrum is plotted with the intensity scaled from zero rather than the
  spectrum minimum.  2 or 4 are best for qplotting, although 3 and 5 will
  give better resolution of the spectrum.  cursor zoom works in all 4 of
  these modes.
  =-1 Display all of spectrum, with portion used marked, scaled from an
  intensity of zero, and cross-correlation with template information.
  =0 Display only part of spectrum used in correlation and cross-correlation
  with template information. (2.0)
  =1 Display all of spectrum, with portion used marked, and cross-correlation
  with template information.
  =2 Display spectrum with absorption and known emission lines labelled
  and both template and emission line information.
  =3 Display spectrum with absorption and known emission lines labelled
  using the entire display without the table of results
  =4 Display continuum-subtracted spectrum with absorption and known emission
  lines labelled and tables of template and emission line information.
  =5 Display continuum-subtracted spectrum with absorption and known emission
  lines labelled using the entire display without the table of results. 
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
  The results are plotted by default in display mode 4 which displays the
  spectrum with the continuum fit subtracted and lines in the bad line list
  removed, if xcsao.fixbad=yes or emsao.fixbad=yes, as appropriate.
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
          cl&gt; qplotc galaxy
  </p>
  <p>
  To check redshifts for a whole night's worth of galaxy spectra:
  </p>
  <p>
          cl&gt; qplotc @nite1.ls
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS'  -->
  

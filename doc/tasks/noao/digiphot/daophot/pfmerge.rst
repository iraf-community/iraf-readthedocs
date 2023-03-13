.. _pfmerge:

pfmerge: Merge a list of photometry databases
=============================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pfmerge inphotfiles outphotfile
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_inphotfiles">
  <dt><b>inphotfiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='inphotfiles' Line='inphotfiles' -->
  <dd>The list of photometry files to be merged. Inphotfiles may be the output of the
  DAOPHOT tasks PHOT, PSTSELECT, PSF, PEAK, GROUP, GRPSELECT, NSTAR, or ALLSTAR.
  Inphotfiles may be either a list of APPHOT/DAOPHOT text databases or a list of
  STSDAS binary tables.
  </dd>
  </dl>
  <dl id="l_outphotfile">
  <dt><b>outphotfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outphotfile' Line='outphotfile' -->
  <dd>The output photometry file. Outphotfile consists of the header of the first
  input photometry file, followed by a list of records, one per input file
  record, each consisting of five fields: ID, XCENTER, YCENTER, MAG, and MSKY.
  Outphotfile is a an APPHOT/DAOPHOT text database if the first photometry file
  is a text database, an STSDAS binary table if the first photometry file is an
  ST table.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose' -->
  <dd>Print messages about the progress of the task ?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  PFMERGE creates a new photometry file suitable for input to PSF, PEAK, GROUP,
  or ALLSTAR by extracting the header of the first input photometry file and the
  values of the five fields: ID, XCENTER, YCENTER, MAG, and MSKY from each
  photometry record in each input file, and writing them to <i>outphotfile</i>.
  <i>Inphotfiles</i> may be either APPHOT/DAOPHOT text databases or STSDAS binary
  tables, but <i>outphotfile</i> inherits the type of the first input photometry
  file.
  </p>
  <p>
  The principal application of PFMERGE is to combine the results of one of the
  DAOPHOT fitting tasks, e.g. ALLSTAR, with the results of the aperture photometry
  task PHOT, to create a new photometry file suitable for input to the fitting
  task. e.g. ALLSTAR, since it if often the case that the user wishes to combine
  preliminary results for a few additional stars with the best fit results to
  date on the original star list. 
  </p>
  <p>
  PFMERGE is intended to combine photometry files from different DAOPHOT tasks.
  The task PCONCAT can be used to combine photometry files produced by the same
  task.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Combine the results of the first allstar run with phot task results
  on a small list of stars detected after the first list of stars was
  subtracted from the original image.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; pfmerge m92.als.1,m92.mag.5 m92.als.2
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
  pconcat
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

.. _showfiles:

showfiles: Print a list of filenames used in a synphot expression.
==================================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  showfiles expr
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task produces a list of filenames used in evaluating a synphot
  expression. The purpose of this task is to allow the user to better
  understand the results that synphot produces by listing the files that
  go into computing this result.
  </p>
  <p>
  There are several functions in synphot expressions which use
  files. The principal functions are the band() and cat() functions. The
  band() function evaluates the combined throughput for an observation
  mode by multiplying the individual throughputs of the components in
  the optical path together. These component throughputs are stored in
  SDAS tables. This task shows you the component tables that synphot
  uses for a specified observation mode. The cat() and icat() functions
  select a spectrum from a catalog of spectra. This task prints the name
  of the spectrum or spectra. This task will also print he names of
  files used by other functions, such as the grid(), spec(), and thru()
  functions, as well as filenames embedded in the synphot expression.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_expr">
  <dt><b>expr [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expr' Line='expr [string]' -->
  <dd>An expression used by the synphot expression evaluator to compute a
  synthetic spectrum or passband. If the expression consists of a single
  call to the band() function, only the arguments to the function need
  be given. For example, the expression <span style="font-family: monospace;">"band(wfpc,f555w)"</span> can also be
  given as <span style="font-family: monospace;">"wfpc,f555w"</span>. The syntax and functions available in the
  synphot expression evaluator are explained in the calcspec help file
  and the Synphot User's Guide.
  </dd>
  </dl>
  <dl>
  <dt><b>(refdata = <span style="font-family: monospace;">""</span>) [pset name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(refdata = "") [pset name]' -->
  <dd>Parameter set for reference data used in calculations.
  This pset contains the following parameters:
  <div class="highlight-default-notranslate"><pre>
  
  area = 45238.93416:  HST telescope area in cm**2.
  
  grtbl = "mtab$*.tmg":  HST graph table.  By default, this
          uses the most recent version.
  
  cmptbl = "mtab$*.tmc"  Instrument component table.  By
          default, this uses the most recent version.
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create the list of component table names for the FOC f/96 observing mode:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; showfiles foc,f/96
  </pre></div>
  <p>
  2. Show the files used to renormalize the vega spectrum in the
  wfpc,f55w passband:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; showfiles "rn(crcalspec$alpha_lyr_stis_002.fits,band(wfpc,f555w),10,stmag)"
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by B.Simon based on XCAL code written by Keith Horne
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  calcspec
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

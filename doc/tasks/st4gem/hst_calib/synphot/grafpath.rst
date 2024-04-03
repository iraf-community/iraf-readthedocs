.. _grafpath:

grafpath: Print keywords and component names for a path through
===============================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  grafpath obsmode
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task produces a list of component table names for the components
  which lie in the optical path of a specified observation mode. The
  other taks in the synphot package compute the combined throughput for
  an observation mode by multiplying the individual throughputs of the
  components in the optical path together. These component throughputs
  are stored in SDAS tables. This task shows you the component tables
  that synphot uses for a specified observation mode if you want to
  investigate why the other synphot tasks produce the results they do.
  </p>
  <p>
  An observation mode is a list of keywords separated by blanks or
  commas which uniquely specifies an optical path through the telescope.
  The keywords which make up the observing mode specify the instrument,
  detector, aperture, filters, and/or gratings used. These keywords may
  occur in any order and in either lower or upper case. Defaults are
  available in many cases so that if some keywords are omitted, the
  defaults will be used.
  </p>
  <p>
  This task and other tasks in the synphot package determine the
  components in the optical path for an observing mode from the graph
  table. The tasks then find the ST4GEM tables containing the
  throughputs for these components in the component lookup table. The
  names of these two tables are read from the 'grtbl' and 'cmptbl'
  parameters in the refdata parameter set. The default values of these
  parameters are set to get the tables most recently installed in the
  CDBS database.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_obsmode">
  <dt><b>obsmode [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obsmode' Line='obsmode [string]' -->
  <dd>A string containing observation mode keywords. Keywords within the
  string are separated by whitespace or commas. Keywords are used to
  match optical components from the graph table. Matching is not case
  sensitive. A warning message is printed if the keyword is not found in
  the optical path. At the user's option, the observation mode string
  may be placed within the band() function.
  </dd>
  </dl>
  <dl>
  <dt><b>(refdata = <span style="font-family: monospace;">""</span>) [pset name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(refdata = "") [pset name]' -->
  <dd>Parameter set for reference data used in calculations.
  This pset contains the following parameters:
  <div class="highlight-default-notranslate"><pre>
  
  area = 45238.93416:  HST telescope area in cm**2.
  
  grtbl = "crcomp$hstgraph_*":  HST graph table.  By default, this
          uses the most recent version.
  
  cmptbl = "crcomp$hstcomp_*"  Instrument component table.  By
          default, this uses the most recent version.
  </pre></div>
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Write a list of component table names for the default observing mode
  of the WFPC:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; grafpath wfpc
  </pre></div>
  <p>
  2. Create the list of component table names for the FOC f/96 observing mode:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; grafpath foc,f/96
  </pre></div>
  <p>
  3. Enclose the obsmode expression in a band function:
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; grafpath "band(foc,f/96)"
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
  calcband
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

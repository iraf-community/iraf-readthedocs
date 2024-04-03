.. _obsmode:

obsmode: List observation mode keywords
=======================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  obsmode obsmode 
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task displays a list of the observation mode keywords. Usually
  this task is run for a single instrument. For example <span style="font-family: monospace;">"obsmode wfpc"</span>
  displays the observation mode keywords for the wfpc. The output is
  structured so that alternate keywords are placed on the same line. For
  example, the output for <span style="font-family: monospace;">"obsmode johnson"</span> displays the single line 
  <span style="font-family: monospace;">"b i r u v"</span>. These are the Johnson filter keywords in the graph table 
  and an observation mode string should contain no more than one of
  these. Long lists of keywords are wrapped, however, so they will
  display on the terminal screen. It should be obvious from the keyword
  names when a long list of keywords has been wrapped.
  </p>
  <p>
  The observation mode path string is a comma separated list of keywords
  The path string specifies a unique light path through the
  telescope. The throughputs of the components in the light path are
  combined to compute a total throughput. The keywords contained in the
  path string are dependent on the structure of the graph table.
  Default keywords are allowed in the path string, but is safest to
  include all the components you wish explicitly unless you are familiar
  with the structure of the graph table. In particular, in the current
  graph table, johnson is the default filter system and nocostar is the
  default value of costar.
  </p>
  <p>
  Available observation mode keywords for all HST instruments and supported
  non-HST bandpasses may also be obtained by consulting the Synphot Data 
  User's Guide, which discusses usage in addition to simply listing available
  keywords.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_path">
  <dt><b>path [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='path' Line='path [string]' -->
  <dd>An incomplete observation mode which specifies the starting node of
  the output. The keywords displayed will be the descendants of the last
  node matched by any of the keywords in the string. The usual value of
  this parameter is a single keyword and this is usually an instrument
  name. For example, <span style="font-family: monospace;">"wfpc"</span> specifies that all the keywords displayed
  should be from descendants of the wfpc node in the graph table. If
  this parameter is left blank or set to <span style="font-family: monospace;">"none"</span>, all the keywords in the
  table will be displayed.
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
  Only the graph table name is used by this task.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Display the observation mode keywords for the hsp:
  </p>
  <p>
  sy&gt; obsmode hsp
  </p>
  <p>
  2.Display the echelle orders for the hrs echelle a:
  </p>
  <p>
  sy&gt; obsmode hrs,ssa,echa
  </p>
  <p>
  3. Display all the keywords in the graph table:
  </p>
  <p>
  sy&gt; obsmode none
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by B.Simon 
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  calcband, calcspec
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

.. _grpselect:

grpselect: Select groups of a specified size from a daophot database
====================================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  grpselect ingroupfile outgroupfile min_group max_group
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_ingroupfile">
  <dt><b>ingroupfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ingroupfile' Line='ingroupfile' -->
  <dd>The list of input group files. Ingroupfile must have been written by the
  DAOPHOT PSF, GROUP, or NSTAR tasks. Ingroupfile may be an APPHOT/DAOPHOT text
  database or an STSDAS table.
  </dd>
  </dl>
  <dl id="l_outgroupfile">
  <dt><b>outgroupfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outgroupfile' Line='outgroupfile' -->
  <dd>The list of output group files. There must be one output group file for every
  input group file. Outgroupfile has the same file type as <i>ingroupfile</i>.
  </dd>
  </dl>
  <dl id="l_min_group">
  <dt><b>min_group</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='min_group' Line='min_group' -->
  <dd>The minimum group size to select from the input group file(s).
  </dd>
  </dl>
  <dl id="l_max_group">
  <dt><b>max_group</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='max_group' Line='max_group' -->
  <dd>The maximum group size to select from the input group file(s).
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = <span style="font-family: monospace;">")_.verbose"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = ")_.verbose"' -->
  <dd>Print messages about the progress of the task? Verbose may be set to the value
  of the daophot package parameter (the default), <span style="font-family: monospace;">"yes"</span>, or <span style="font-family: monospace;">"no"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  GRPSELECT creates a new GROUP file <i>outgroupfile</i> by selecting groups from
  the input GROUP file <i>ingroupfile</i> within a range of group sizes specified
  by <i>min_group</i> and <i>max_group</i>. If <i>ingroupfile</i> is a DAOPHOT text
  database, <i>outgroupfile</i> is a text database. Conversely if <i>ingroupfile</i>
  is a DAOPHOT STSDAS table database, <i>outgroupfile</i> is an STSDAS table 
  database.
  </p>
  <p>
  A typical use for GRPSELECT is to create a new database containing only groups
  which are less than the value of the <i>maxgroup</i> parameter in the DAOPARS
  task for direct input into the NSTAR task.  The remaining stars in the larger
  groups are reduced by running GRPSELECT once more, selecting only groups
  greater than <i>maxgroup</i>, rerunning GROUP on the output with a less
  stringent value of the DAOPARS parameter task <i>critovlap</i> to reduce the
  group sizes and inputting the result into NSTAR.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Select groups with between 1 and 70 stars from the GROUP task output file
  ypix.grp.1 and write them into a new file named ypixsmall.grp.
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; grpselect ypix.grp.1 ypixsmall.grp 1 70
  </pre></div>
  <p>
  2. Select groups larger than 70 from the same input group file and rerun
  group with a new value of the critoverlap parameter on the results. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  da&gt; grpselect ypix.grp.1 ypixlarge.grp 71 400
  da&gt; group dev$ypix ypixlarge.grp ypix.psf.1 default crit=5.0
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
  group
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

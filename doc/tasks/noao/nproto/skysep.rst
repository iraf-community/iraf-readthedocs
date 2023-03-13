.. _skysep:

skysep: Compute arc separation of two RA/Dec values
===================================================

**Package: nproto**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  Given two RA/Dec value pairs the spherical separation is computed.  This
  task can be used in scripts and has both text and parameter output.
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  skysep ra1 dec1 ra2 dec2
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_ra1">
  <dt><b>ra1, dec1, ra2, dec2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ra1' Line='ra1, dec1, ra2, dec2' -->
  <dd>The RA and Dec of two points on the sky for which a separation is to be
  computed.  The RA may be in hours or degrees and the Dec is in degrees.
  The values may be in decimal or sexagesimal format.
  </dd>
  </dl>
  <dl id="l_raunit">
  <dt><b>raunit = <span style="font-family: monospace;">"hr"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='raunit' Line='raunit = "hr"' -->
  <dd>Units for right ascension.  The value <span style="font-family: monospace;">"hr"</span> selects hours and <span style="font-family: monospace;">"deg"</span>
  selects degrees.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print a verbose output to the standard output?
  </dd>
  </dl>
  <dl id="l_sep">
  <dt><b>sep</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sep' Line='sep' -->
  <dd>This output parameter will contain the separation in arc seconds after
  the task is run.  It may then be referenced as the variable skysep.sep.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This simple script task computes the separation between two celestial
  coordinates given as RA and Dec.  The RA units may be hours or degrees,
  as selected by a parameter, and the Dec units must be degrees.  The result
  may be printed to the standard output (in restricted precision) and is
  also record in a task parameter for later use.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. The verbose output appears as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; skysep 12:12:12 32:32:32 12:12:24 32:32:52 verb+
  153.05 arcsec = (12:12:12.00, 32:32:32.0) - (12:12:24.00, 32:32:52.0)
  cl&gt; = skysep.sep
  153.04686934468
  </pre></div>
  <p>
  2. To use in a script:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cache skysep   # Cache to avoid problems with updating par files
  
  # To use scan to get the value.
  skysep (r1, d1, r2, d2, raunit="deg", verbose+) | scan (sep)
  printf ("The separation is %f\n", sep)
  
  # To use the saved value.
  skysep (r1, d1, r2, d2, raunit="deg", verbose-)
  printf ("The separation is %.5f\n", skysep.sep)
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  astcalc, asthedit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

.. _istable:

istable: Is a file a table or text database file ?
==================================================

**Package: ptools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  istable infile
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_infile">
  <dt><b>infile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='infile' Line='infile' -->
  <dd>The name of the input file whose status is to be determined.
  </dd>
  </dl>
  <dl id="l_table">
  <dt><b>table = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table = no' -->
  <dd>An output variable which is <span style="font-family: monospace;">"yes"</span> if <i>infile</i> is an STSDAS table
  and <span style="font-family: monospace;">"no"</span> otherwise.
  </dd>
  </dl>
  <dl id="l_text">
  <dt><b>text = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='text' Line='text = no' -->
  <dd>An output variable which is <span style="font-family: monospace;">"yes"</span> if <i>infile</i> is an APPHOT/DAOPHOT
  text database and <span style="font-family: monospace;">"no"</span> otherwise.
  </dd>
  </dl>
  <dl id="l_other">
  <dt><b>other = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='other' Line='other = no' -->
  <dd>An output variable which is <span style="font-family: monospace;">"yes"</span> if <i>infile</i> is neither of the
  above and <span style="font-family: monospace;">"no"</span> otherwise.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  ISTABLE is a very simple task which determines whether a specified
  input file is an STSDAS table, an APPHOT/DAOPHOT text database file or 
  neither of the above. ISTABLE first tries to open the input file as an 
  STSDAS table. If successful ISTABLE returns <span style="font-family: monospace;">"yes"</span> in the
  variable <i>table</i> and <span style="font-family: monospace;">"no"</span> in <i>text</i> and <i>other</i>. Otherwise
  ISTABLE  tries to open the input file as an APPHOT/DAOPHOT text database
  file by checking for the <span style="font-family: monospace;">"#K IRAF"</span> keyword.
  If the check is positive ISTABLE return <span style="font-family: monospace;">"yes"</span> in
  the variable <i>text</i> and <span style="font-family: monospace;">"no"</span> in <i>table</i> and <i>other</i>. If the input
  file is neither an STSDAS table or an APPHOT/DAOPHOT text database
  ISTABLE returns <span style="font-family: monospace;">"yes"</span> in the variable <i>other</i> and <span style="font-family: monospace;">"no"</span> in <i>text</i>
  and <i>table</i>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Determine whether the file n4147.mag.1 is an STSDAS table.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; istable n4147.mag
  pt&gt; =istable.table
  
      ... answer will appear on the screen
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Users should be wary of running ISTABLE in background as the output
  CL parameters may not be properly updated. 
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

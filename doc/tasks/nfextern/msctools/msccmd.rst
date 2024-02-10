.. _msccmd:

msccmd: Execute general command with image extension expansion
==============================================================

**Package: msctools**

.. raw:: html

  <section id="s_synopsis">
  <h3>Synopsis</h3>
  <p>
  This tasks executes a command where any input and output image list
  arguments specified by $input, $in2, and $output are replaced by an
  expanded list of image extensions.  If there are no command line
  arguments the task runs as an interpreter with prompts until the
  command <span style="font-family: monospace;">'q'</span> or 'quit' is entered.
  </p>
  </section>
  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  msccmd [command input output]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Do image statistics.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; msccmd "imstat $input" obj*fits
  </pre></div>
  <p>
  Since this is a common operation see <b>mscstat</b> instead.
  </p>
  <p>
  2. Do image arithmetic.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; msccmd "imarith $input + $in2 $output"
  List of input files: obj001
  Second list of input files: obj002
  List of output files: sum
  </pre></div>
  <p>
  Since this is a common operation see <b>mscarith</b> instead.
  </p>
  <p>
  3. Do HSELECT on the command line with no prompts.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; msccmd "hselect $input $I,filter yes" obj001,obj002
  [output]
  </pre></div>
  <p>
  4. Use in interpretive mode.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; msccmd
  msccmd&gt; Command: imhead $input l-
  [output]
  msccmd&gt; Command: hselect $input $I,filter
  msccmd&gt; Input files: obj001,obj002
  [output]
  msccmd&gt; Command: hedit $input filter B verify-
  msccmd&gt; Input files (obj001,obj002):
  msccmd&gt; Command: print "This command has not input or output files."
  This command has not input or output files.
  msccmd&gt; Command: q
  cl&gt;
  </pre></div>
  </section>
  <section id="s_restriction">
  <h3>Restriction</h3>
  <p>
  Image sections are not allowed in the mosaic filenames.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_MSCSTAT">
  <dt><b>MSCSTAT - V2.11 external package</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='MSCSTAT' Line='MSCSTAT - V2.11 external package' -->
  <dd>First release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mscarith, mscstat
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNOPSIS' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'RESTRICTION' 'REVISIONS' 'SEE ALSO'  -->
  

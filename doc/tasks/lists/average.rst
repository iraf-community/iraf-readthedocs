.. _average:

average: Compute the mean and standard deviation of a list
==========================================================

**Package: lists**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  average option
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_option">
  <dt><b>option</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='option' Line='option' -->
  <dd>Chosen from <span style="font-family: monospace;">"add"</span>, <span style="font-family: monospace;">"subtract"</span> or <span style="font-family: monospace;">"new_sample"</span>, 
  in which case the numbers averaged are those in STDIN.
  If no argument is given on the command line, <span style="font-family: monospace;">"new_sample"</span> is assumed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Task <i>average</i> computes the average and standard deviation of a list
  of numbers.  Numeric input is read from STDIN with one number per line.
  The mean, sigma and number of samples are written to the standard
  output.
  </p>
  <p>
  By default, the sample is taken to be
  the set of numbers in the standard input when <i>average</i> is run. 
  Additional points can be added to or deleted from the sample by rerunning
  <i>average</i> with <b>option</b> equal to one of the following:
  </p>
  <dl id="l_add">
  <dt><b>add</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='add' Line='add' -->
  <dd>add points to the sample, recalculate mean and sigma
  </dd>
  </dl>
  <dl id="l_sub">
  <dt><b>sub</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='sub' Line='sub' -->
  <dd>subtract points from the sample
  </dd>
  </dl>
  <p>
  The sample is reinitialized by setting <b>option</b> = <span style="font-family: monospace;">"new_sample"</span>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Run <i>average</i> on the list of numbers in file <span style="font-family: monospace;">"numbers"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type numbers | average
  </pre></div>
  <p>
  Add in to the sample the list of numbers in file <span style="font-family: monospace;">"numbers.2"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; average add &lt; numbers.2
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  lintran
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

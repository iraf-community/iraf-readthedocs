.. _history:

history: Display  commands previously executed
==============================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  history [[-]ncommands]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_ncommands">
  <dt><b>ncommands</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ncommands' Line='ncommands' -->
  <dd>The number of commands to be displayed.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>history</i> task prints a list of the last few commands executed.
  Only commands which terminated normally are included.
  The number of commands to be printed may be specified on the command line
  if desired.  If the number is preceded by a minus sign the default
  number of lines is not changed, otherwise <i>history</i> will take the
  value given as the new default number of commands to be printed.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print the last few commands.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; history
  </pre></div>
  <p>
  2. Print the entire history list.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; history -999
  </pre></div>
  <p>
  3. Change the default number of history lines to be printed to 5 (and print
  the last five commands).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; history 5
  </pre></div>
  <p>
  4. Save the history in the file <span style="font-family: monospace;">"commands"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; history -999 &gt; commands
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ehistory
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

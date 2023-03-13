.. _translit:

translit: Replace or delete specified characters in a file
==========================================================

**Package: utilities**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  translit infile from_string [to_string]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_infile">
  <dt><b>infile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='infile' Line='infile' -->
  <dd>The input file name or template, e.g. <span style="font-family: monospace;">"abc"</span> or <span style="font-family: monospace;">"abc.*"</span>.
  </dd>
  </dl>
  <dl id="l_from_string">
  <dt><b>from_string</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='from_string' Line='from_string' -->
  <dd>String containing characters to be mapped. 
  If delete is yes then the characters in from_string are deleted from the input
  file(s). The from_string may specify a range of characters, e.g. <span style="font-family: monospace;">"a-z"</span> or <span style="font-family: monospace;">"A-Z"</span>.
  If the first character of from_string is ^ then the program will operate
  on all but the specified characters, e.g. <span style="font-family: monospace;">"^a-z"</span> means all but lower case
  alphabetic characters.
  </dd>
  </dl>
  <dl id="l_to_string">
  <dt><b>to_string</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='to_string' Line='to_string' -->
  <dd>Requested if delete is no, otherwise set to the null string.
  Characters in from_string are mapped into characters in to_string.
  When to_string is short with respect to from_string, it is padded
  by duplicating the last character.
  </dd>
  </dl>
  <dl id="l_delete">
  <dt><b>delete = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='delete' Line='delete = no' -->
  <dd>If delete is yes the characters in from_string are deleted from the input
  file(s) and no to_string is requested.
  </dd>
  </dl>
  <dl id="l_collapse">
  <dt><b>collapse = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='collapse' Line='collapse = no' -->
  <dd>If this switch is set all strings of repeatedly mapped output characters
  are squeezed to a single character.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To change all the alphabetic characters in a file from lower to upper
  case, writing the result on the standard output:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; translit filename a-z A-Z
  </pre></div>
  <p>
  To delete the letters a, b, and c from a file:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; translit filename abc de=yes
  </pre></div>
  <p>
  To replace all but the letters abc in a file with A:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; translit filename ^abc A
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'EXAMPLES'  -->
  

.. _parkey:

parkey: Put an IRAF parameter into an image or table header keyword.
====================================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  parkey value output keyword
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task changes the value of a header keyword in either a table or an
  image. If the value of the task parameter 'add' is <span style="font-family: monospace;">"yes"</span>, the task will
  allow you to add a new keyword to the header, otherwise, adding a new
  keyword will cause an error. Type conversion is performed if the data type of
  the header keyword differs from the data type of the input parameter 'value'. 
  If a new
  keyword is added to the file, the type is determined 
  from the input value. The
  strings <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"y"</span>, <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"n"</span>, <span style="font-family: monospace;">"true"</span>, <span style="font-family: monospace;">"t"</span>, <span style="font-family: monospace;">"false"</span>, and <span style="font-family: monospace;">"f"</span>, in either
  upper or lower case, are interpreted as boolean values.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_value">
  <dt><b>value [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='value' Line='value [string]' -->
  <dd>Input value to be written to the header keyword. (Strings are case sensitive.)
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name]' -->
  <dd>Name of the file whose header keyword is to be changed.
  </dd>
  </dl>
  <dl id="l_keyword">
  <dt><b>keyword [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='keyword' Line='keyword [string]' -->
  <dd>Name of the header keyword to be changed. (The name is not case sensitive.)
  </dd>
  </dl>
  <dl>
  <dt><b>(add = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(add = no) [boolean]' -->
  <dd>Allow new header keywords to be added?  
  If 'add = no', then existing keywords
  can take new values but no new keywords can be added to the file.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Set the header keyword 'OVERSCAN' in the file 'image.hhh' to 5:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; parkey 5 image.hhh overscan
  </pre></div>
  <p>
  2. Set the group parameter 'CTYPE1' in the second group of the same
  file to <span style="font-family: monospace;">"ANGSTROM"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; parkey ANGSTROM image.hhh[2] ctype1
  </pre></div>
  <p>
  3. Set the header keyword 'YSTEP' to the value stored 
  in the IRAF parameter <span style="font-family: monospace;">'x'</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; parkey (x) image.hhh ystep
  </pre></div>
  <p>
  4. Add the keyword 'COMPNAME' to the table header and put the value <span style="font-family: monospace;">"FILTER1"</span>
  in it:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; parkey FILTER1 graph.tab compname add+
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Bernie Simon.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  keypar, keytab, partab, tabkey, tabpar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

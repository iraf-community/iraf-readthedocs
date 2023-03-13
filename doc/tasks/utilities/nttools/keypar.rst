.. _keypar:

keypar: Copy an image or table header keyword to an IRAF parameter.
===================================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  keypar input keyword
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task reads a header keyword from an image or table file. The
  keyword is written to the IRAF parameter 'value' as a character
  string. If the header keyword is boolean, the value of 'value' will
  either be <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"no"</span>.  If the header keyword is not found, 'value'
  will be set to a null string.  String parameters, such as 'value', can
  be converted to numeric data types with the built in functions real()
  and int().
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name]' -->
  <dd>Name of the file containing the header keyword.
  </dd>
  </dl>
  <dl id="l_keyword">
  <dt><b>keyword [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='keyword' Line='keyword [string]' -->
  <dd>Name of the header keyword to be retrieved. (The keyword 
  name is not case sensitive.)
  </dd>
  </dl>
  <dl>
  <dt><b>(silent = no) [bool]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(silent = no) [bool]' -->
  <dd>If this parameter is set to no (the default) a warning message will be
  printed if the keyword is not found in the header. If it is set to
  yes, the warning message is suppressed.
  </dd>
  </dl>
  <dl>
  <dt><b>(value) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(value) [string]' -->
  <dd>An output  parameter that will contain the value passed from the header
  keyword.
  </dd>
  </dl>
  <dl>
  <dt><b>(found) [bool]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(found) [bool]' -->
  <dd>An output parameter that will be set to yes if the keyword is found in
  the header and no if it is not.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print the number of groups (i.e., the 'GCOUNT' keyword)
  in the image file 'image.hhh':
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; keypar image.hhh gcount
  tt&gt; print(keypar.value)
  </pre></div>
  <p>
  2. Print the range of the data in the second group of the same image by 
  reading the values of the 'DATAMIN' and 'DATAMAX' keywords:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; keypar image.hhh[2] datamin
  tt&gt; x = real(keypar.value)
  tt&gt; keypar image.hhh[2] datamax
  tt&gt; y = real(keypar.value)
  tt&gt; print(y-x)
  </pre></div>
  <p>
  3. Print the component name (i.e., the 'COMPNAME' header keyword)
  for the table 'thruput.tab':
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; keypar thruput.tab compname
  tt&gt; print(keypar.value)
  </pre></div>
  <p>
  4. Check for the existence of the exposure time in an image header:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; keypar image.hhh exptime silent+
  tt&gt; if (keypar.found) {
  &gt;&gt;&gt; print keypar.value
  &gt;&gt;&gt; } else {
  &gt;&gt;&gt; print INDEF
  &gt;&gt;&gt; }
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Bernie Simon.
  SEE ALSO
  keytab, parkey, partab, tabkey, tabpar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES'  -->
  

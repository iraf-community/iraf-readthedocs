.. _partab:

partab: Transfer an IRAF parameter to a table element.
======================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  partab value table column row
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task changes the value of a table element to the value of the input
  parameter 'value'.  If 'value' is set to <span style="font-family: monospace;">"INDEF"</span>, the table element will be
  set to undefined.  If the data type of the table element is different from
  that of the input parameter 'value', this task will perform 
  type conversion.  The strings
  <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"y"</span>, <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"n"</span>, <span style="font-family: monospace;">"true"</span>, <span style="font-family: monospace;">"t"</span>, <span style="font-family: monospace;">"false"</span>, and <span style="font-family: monospace;">"f"</span>, in either upper or
  lower case are interpreted as boolean values.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_value">
  <dt><b>value [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='value' Line='value [string]' -->
  <dd>The IRAF parameter that will be copied into the table element.
  </dd>
  </dl>
  <dl id="l_table">
  <dt><b>table [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file name]' -->
  <dd>Name of the table.
  </dd>
  </dl>
  <dl id="l_column">
  <dt><b>column [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='column' Line='column [string]' -->
  <dd>Column name. (Column names are not case sensitive).
  </dd>
  </dl>
  <dl id="l_row">
  <dt><b>row [integer, min=1, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='row' Line='row [integer, min=1, max=INDEF]' -->
  <dd>Row number.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Set the twelfth component (i.e., row 12 of column 'COMPNAME') 
  in the file 'graph.tab' to <span style="font-family: monospace;">"FILTER1"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; partab FILTER1 graph.tab COMPNAME 12
  </pre></div>
  <p>
  2. Set the first wavelength (i.e., row 1 of column 'WAVELENGTH') in 
  the file 'spectrum.tab' to the value contained in parameter
  <span style="font-family: monospace;">'x'</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; partab (x) spectrum.tab WAVELENGTH 1
  </pre></div>
  <p>
  3. Set the hundreth wavelength (i.e., row 100 of column 'WAVELENGTH')
  in 'spectrum.tab' to undefined:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; partab INDEF spectrum.tab WAVELENGTH 100
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
  keypar, keytab, parkey, tabkey, tabpar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

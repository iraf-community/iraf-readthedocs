.. _keytab:

keytab: Copy an image or table header keyword to a table element.
=================================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  keytab input keyword table column row
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task reads a header keyword from either an image or a table file
  and writes it to a table element (row and column position). If the
  data type of the header keyword differs from that of the table
  element, then the value is converted to the appropriate data type. If
  the keyword is not found in the header, the element will be set to the
  null value appropriate for the column type.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [file name]' -->
  <dd>Name of the file containing header keyword.
  </dd>
  </dl>
  <dl id="l_keyword">
  <dt><b>keyword [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='keyword' Line='keyword [string]' -->
  <dd>Name of the header keyword to be read. (Keyword names are not case sensitive.)
  </dd>
  </dl>
  <dl id="l_table">
  <dt><b>table [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file name]' -->
  <dd>Name of the table to which the value will be written.
  </dd>
  </dl>
  <dl id="l_column">
  <dt><b>column [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='column' Line='column [string]' -->
  <dd>Name of table column. (Column names are not case sensitive.)
  </dd>
  </dl>
  <dl id="l_row">
  <dt><b>row [integer, min=1, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='row' Line='row [integer, min=1, max=INDEF]' -->
  <dd>Table row number.
  </dd>
  </dl>
  <dl>
  <dt><b>(silent = no) [bool]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(silent = no) [bool]' -->
  <dd>If this parameter is set to no (the default) a warning message will be
  printed if the keyword is not found in the header. If it is set
  to yes, the warning message is suppressed.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Copy the component name (i.e., the 'COMPNAME' header keyword) 
  from the table 'thruput.tab' to the
  first row of the table 'graph.tab'.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; keytab thruput.tab COMPNAME graph.tab COMPNAME 1
  </pre></div>
  <p>
  2. Copy the zero point of the second group (i.e., the 'CRVAL1' keyword)
  in the image file 'image.hhh' to the first
  wavelength in the table 'spectrum.tab'.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; keytab image.hhh[2] CRVAL1 spectrum.tab WAVELENGTH 1
  </pre></div>
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
  keypar, parkey, partab, tabkey, tabpar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

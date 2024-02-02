.. _countfiles:

countfiles: Count how many files are in the input file template.
================================================================

**Package: imgtools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  countfiles input
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Countfiles is a simple task to count how many input files are in the template.
  It works with wild card.  Together with the task pickfile, it provides an 
  intuitive alternative for scan in IRAF script writing.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input [string]' -->
  <dd>Input file template.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output [int] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [int] ' -->
  <dd>Output parameter: number of files in the input string.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. im&gt; countfiles <span style="font-family: monospace;">"a,b,c,d"</span>
  </p>
  <p>
  	The output will be 4.
  	
  2. im&gt; countfiles @list
  </p>
  <p>
  3. im&gt; countfiles *
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  pickfile, scan
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'BUGS' 'SEE ALSO'  -->
  

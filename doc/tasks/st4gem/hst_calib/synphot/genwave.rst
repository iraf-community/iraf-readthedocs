.. _genwave:

genwave: Interactively generate a wavelength set.
=================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  genwave output minwave maxwave dwave
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task creates a wavelength set based on user specified values for
  the minimum and maximum of the desired wavelength range and the sampling
  interval.  The sampling interval may be expressed in terms of Angstroms 
  per pixel ('dwave') or in terms of km/s/pixel ('dvelocity').  The
  default is to use the value passed to the 'dwave' parameter, unless the
  value of 'dwave' is INDEF.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_output">
  <dt><b>output [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output [file name]' -->
  <dd>File name for the wavelength table that will be created by this task.
  The wavelength table is a set of sampling points for both spectral flux
  and throughput transmission, and is used by various tasks in the 'synphot'
  package.
  </dd>
  </dl>
  <dl id="l_minwave">
  <dt><b>minwave [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minwave' Line='minwave [real]' -->
  <dd>Minimum value for wavelength range (in Angstroms).
  </dd>
  </dl>
  <dl id="l_maxwave">
  <dt><b>maxwave [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxwave' Line='maxwave [real]' -->
  <dd>Maximum value for wavelength range (in Angstroms).
  </dd>
  </dl>
  <dl id="l_dwave">
  <dt><b>dwave = INDEF [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dwave' Line='dwave = INDEF [real]' -->
  <dd>Wavelength interval between sampling points (in Angstroms/sample).
  The value of this parameter is ignored if it is set to INDEF, and the
  value of 'dvelocity' is used instead.
  </dd>
  </dl>
  <dl>
  <dt><b>(dvelocity = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(dvelocity = INDEF) [real]' -->
  <dd>Velocity interval between sampling points (in km/s/sample).  If set to
  INDEF, this parameter is ignored and the wavelength interval is
  calculated from the value of 'dwave'.
  </dd>
  </dl>
  <dl>
  <dt><b>(wavecol = <span style="font-family: monospace;">"WAVELENGTH"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wavecol = "WAVELENGTH") [string]' -->
  <dd>Name for the column in 'waveset' that will contain the wavelength
  values. Values written to this column will be in Angstrom units. The
  default column name <span style="font-family: monospace;">"WAVELENGTH"</span> creates a wavelength table that can
  be used by other task in the synphot package.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Generate a wavelength set having a range of 3000 
  to 8000 Angstroms, and an interval of 10 A per sample.
  Results will be written to the column 'WAVELENGTH' in the table file 
  'samplset.tab'.
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; genwave samplset.tab 3000. 8000. 10.
  </pre></div>
  <p>
  2. Generate a wavelength set having the same range as above, but set
  the sampling interval to be 100 km/s/pixel.
  </p>
  <div class="highlight-default-notranslate"><pre>
  sy&gt; genwave samplset.tab 3000. 8000. INDEF dv=100.
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  Written by B.Simon based on XCAL code written by Keith Horne
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  Type <span style="font-family: monospace;">"help synphot opt=sys"</span> for a description of table structures used
  by synthetic photometry tasks.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

.. _hdshift:

hdshift: Align related HD curves
================================

**Package: dtoi**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  hdshift database
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_database">
  <dt><b>database</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database' -->
  <dd>Input list of databases containing density, exposure and fit information.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  For each file in <b>database</b>, procedure <b>hdshift</b> calculates and 
  subtracts a zero point shift to bring several related HD curves into
  alignment.  The individual shifts are calculated by elimination of the 
  first coefficient (Bevington, eqn 9-3):
  </p>
  <div class="highlight-default-notranslate"><pre>
       _      _      _               _
  a0 = y - a1*X - a2*X**2 - ... - an*X**n
  </pre></div>
  <p>
  Here, the averages over y and X refer to individual <b>database</b> averages; 
  the coefficients a1, ... an were previously calculated using data from all 
  <b>database</b>s, in task <i>hdfit</i>, and stored in the database.  The
  a0 term is calculated individually for each database; this term represents
  the zero point shift in log exposure and will be different for each database.
  </p>
  <p>
  On output, the log exposure values in each <b>database</b> have been 
  shifted to the zero point shift of the first database in the list.  The
  log exposure records are now aligned and it would be appropriate
  to run task <i>hdfit</i> on the modified <b>database</b> list and
  determine the common solution.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  Shift the curves in four databases to a common zero point.
  
          cl&gt; hdshift db1,db2,db3,db4
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  hdfit, hdtoi
  <br>
  <span style="font-family: monospace;">"Averaging Photographic Characteristic Curves"</span>, John Kormendy, from
  <span style="font-family: monospace;">"ESO Workshop on Two Dimensional Photometry"</span>, Edited by P. Crane and
  K.Kjar, p 69, (1980), an ESO Publication.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

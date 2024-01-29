.. _demos:

demos: Xdimsum demo data script
===============================

**Package: xdimsum**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  demos demoname
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_demoname">
  <dt><b>demoname</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='demoname' Line='demoname' -->
  <dd>The name of the demo data set to be created. At present the only option
  is <span style="font-family: monospace;">"mkxdimsum"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Demos creates a set of artificial test data for the XDIMSUM package.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create the demo data for the xdimsum package and run the xmosaic task on it.
  Define the parameters to give results as close as possible to the original
  DIMSUM.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cd &lt;testdir&gt;
  ... move to an empty test directory which has write permission
  
  cl&gt; demos mkxdimsum
  ... create the demo data
  
  cl&gt; xmosaic @demo.list demo13  mosaic ".exp"  nsigrej=5.0 maxiter=10     \
      bpmask=demo.pl shiftslist=demo.slist
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  xmosaic, xfirstpass, xmaskpass
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

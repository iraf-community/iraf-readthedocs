.. _demos:

demos: Demonstrations and tests
===============================

**Package: kpnoslit**

.. raw:: html

  <section id="s_packages">
  <h3>Packages</h3>
  <p>
  noao.imred.argus, noao.imred.goldcams, noao.imred.kpcoude.fiber
  noao.imred.kpcoude.slit, noao.imred.nessie, noao.imred.specred
  noao.twodspec.longslit
  </p>
  </section>
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
  <dd>Demonstration or test procedure name.  Each package may have a different
  set of demonstrations.  If the demo name is not specified on the command
  line a menu of names is printed and then the name is queried.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Many packages have demonstration and test procedures.  These are generally
  based on artificial data and use the <i>stty playback</i> (see <b>stty</b>)
  mechanism of the CL.  A playback replaces interactive terminal input 
  with previously stored input but otherwise is an actual execution of
  the entered commands.  This allows both demonstration of various types
  and an actual test of the software on a particular IRAF system.
  </p>
  <p>
  Generally the <b>demos</b> procedures create their own data if not present
  from a previous execution.  After the procedure is completed the data,
  logfiles, etc. are left so that they may be examined further and
  the user may try some experiments.  Thus, it might be useful to create
  a new directory for the demo using <b>mkdir</b> and <span style="font-family: monospace;">"cd"</span> to it.
  </p>
  <p>
  Currently, most of the demos are test procedures which do not contain
  comments and suitable delays to act as a demonstration.  These will
  be added in time.  Also some of the demos just create the demo/test
  data if one just wants some relevant data for experimentation with
  the package.
  </p>
  <p>
  One should be aware that since the tasks are actually run parameters
  are sometimes changed.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  From the <b>goldcam</b> package list the menu and execute the
  qtest demo.
  </p>
  <div class="highlight-default-notranslate"><pre>
  go&gt; mkdir demo
  go&gt; cd demo
  go&gt; demos
          MENU of GOLDCAM Demonstrations
  
          qtest - Quick test of GOLDCAM (no comments, no delays)
  
  Demo name (qtest):
  &lt;Demo follows&gt;
  </pre></div>
  <p>
  2.  From the <b>nessie</b> package create some simple test data.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ne&gt; demos mkqdata
  Creating image demoobj ...
  Creating image demoflat ...
  Creating image demoarc1 ...
  Creating image demoarc2 ...
  ne&gt; demos mkqdata
  ne&gt;
  </pre></div>
  <p>
  Note that the second execution does not create the data again.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  artdata.mkexamples, ccdred.ccdtest.demo
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'PACKAGES' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

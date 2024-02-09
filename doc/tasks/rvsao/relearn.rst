.. _relearn:

relearn: Set parameter values in parameter file of new version
==============================================================

**Package: rvsao**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  relearn task
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_task">
  <dt><b>task = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='task' Line='task = ""' -->
  <dd>Name of task of which parameter file is to be updated
  </dd>
  </dl>
  <p>
   
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>relearn</i> saves the current parameter values for the named task,
  unlearns it, and reassigns the old parameter values to the new file.
  Instead of typing
  <br>
  	dpar task &gt;temp.file
  <br>
  	unlearn task
  <br>
  	cl &lt;temp.file
  <br>
  you type
  <br>
  	relearn task
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  none
   
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'BUGS'  -->
  

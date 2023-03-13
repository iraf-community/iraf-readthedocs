.. _osfn:

osfn: Return the host system equivalent of an IRAF filename
===========================================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  string = osfn (vfn)
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_vfn">
  <dt><b>vfn  </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='vfn' Line='vfn  ' -->
  <dd>The IRAF virtual filename to be translated into a host filename.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Osfn</i> is a string valued intrinsic function which takes an IRAF virtual
  filename as input and returns the equivalent host system filename as output.
  <i>Osfn</i> can only be called as a function.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print the host equivalent of the vfn <span style="font-family: monospace;">"hlib$login.cl"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; = osfn ("hlib$login.cl")
  </pre></div>
  <p>
  2. Compute a host filename for use as an argument to a foreign task
  (see help <i>task</i> for more information on foreign tasks).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; task $vdir = "$directory"   # VMS directory lister
  cl&gt; vdir /size osfn("bin$")
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  pathnames, task
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

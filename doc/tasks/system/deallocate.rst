.. _deallocate:

deallocate: Deallocate a previously allocated device
====================================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  deallocate device
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_device">
  <dt><b>device</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device' -->
  <dd>The device to be deallocated.
  </dd>
  </dl>
  <dl id="l_rewind">
  <dt><b>rewind = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rewind' Line='rewind = yes' -->
  <dd>Rewind the device before deallocating?
  Ignored for devices other than magtape.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Deallocate a previously allocated device.  The CL will print an error
  message if one attempts to logout while devices are still allocated,
  but if <i>logout</i> is typed several times you will be allowed to logout
  with the devices still allocated.  The CL does not automatically
  deallocate devices upon logout.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Deallocate logical magtape drive B.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dealloc mtb
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  allocate, devstatus, file dev$devices, dev$tapecap
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

.. _allocate:

allocate: Allocate a device, i.e., magtape drive mta, mtb, ...
==============================================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  allocate device
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_device">
  <dt><b>device</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device' -->
  <dd>The device to be allocated.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Allocate</b> allocates a device for exclusive access by one user, and
  readies the device for i/o by some other program.  A list of the devices
  available on the local system is maintained in the file <b>dev$tapecap</b>
  which needs to be configured by the site manager before it can be used.
  The status of given device may be obtained by calling <i>devstatus</i>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print a list of the allocatable devices.  The logical device names are
  given at the left in the output text; ignore the information to the right.
  <b>Note</b>: The dev$devices file should be configured by the site manager
  when new tape devices are installed.  Beginning with V2.9 it is used for
  informational purposes only.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type dev$devices
  mta ...
  mtb ...
  mtc ...
  iis ...
  </pre></div>
  <p>
  2. Allocate a tape drive after checking its status.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; devstatus mtb
  device mtb is not currently allocated
  cl&gt;
  cl&gt; allocate mtb
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  deallocate, devstatus
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

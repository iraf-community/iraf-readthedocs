.. _devstatus:

devstatus: Print the status of a device (mta, mtb, ...)
=======================================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  devstatus device
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_device">
  <dt><b>device</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device' -->
  <dd>The device for which status information is requested.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print additional system dependent device information (may not be implemented
  on all systems).
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <b>Devstatus</b> tells whether the named device has been allocated.
  In the case of a magtape drive allocated to the current user, additional
  information is printed noting the tape position and the type of operation
  last performed.  If the device is not currently allocated, i.e., available
  for allocation, or if the device has already been allocated by another user,
  one of the following messages is printed:
  </p>
  <div class="highlight-default-notranslate"><pre>
  device is not currently allocated
  device is allocated to XXXX
  </pre></div>
  <p>
  A list of the allocatable devices, including the host system names for the
  devices, can be obtained by paging the file <b>dev$devices</b> providing
  that file has been properly configure by the Site Manager at installation
  time.  The dev$tapecap file is used to define the tape devices available
  on the system.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Get status information for the logical tape drive <span style="font-family: monospace;">"mta"</span>, which we have
  just allocated.  Note that the tape position is printed only if we are the
  owner of the drive.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; dev mtb
  # Magtape unit `mta' allocated to `smith' Fri 12:04:16 07-Jan-86
  file = 1
  record = 1
  unit just allocated: no i/o has yet occurred
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Information can only be requested for a single device at a time.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  allocate, deallocate
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

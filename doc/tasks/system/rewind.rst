.. _rewind:

rewind: Rewind a device (magtape)
=================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  rewind device
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_device">
  <dt><b>device</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device' -->
  <dd>The device to be rewound.
  </dd>
  </dl>
  <dl id="l_initcache">
  <dt><b>initcache = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='initcache' Line='initcache = yes' -->
  <dd>Initialize the magtape device position cache for the device.  This causes
  the magtape i/o system to <span style="font-family: monospace;">"forget"</span> what it thinks it knows about things
  like the number of files on the tape, the amount of tape used, and so on.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Rewind</i> rewinds the specified device, which is most likely
  a magnetic tape, and which has been previously allocated to the user.
  </p>
  <p>
  By default <i>rewind</i> will initialize the device position cache.  When
  changing tapes, one should always either rewind or deallocate and reallocate
  the device, to force the magtape system to recompute the number of files
  on the tape and to ensure that the tape is left in a defined position.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Rewind logical tape drive a.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; rewind mta
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  allocate, deallocate, devstatus
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

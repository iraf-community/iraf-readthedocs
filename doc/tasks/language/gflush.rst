.. _gflush:

gflush: Flush any buffered graphics output
==========================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  gflush
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <p>
  None.
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Output to graphics plotter devices is normally buffered and then disposed
  of to the plotter as a larger job, to increase the efficiency of the
  graphics system.  The <i>gflush</i> task disposes of any buffered graphics
  output and also initializes the graphics subsystem.  The cursor mode frame
  buffer is cleared, any connected graphics subkernels are disconnected,
  and the memory and file descriptors used by the graphics subsystem are
  freed.  A <i>gflush</i> occurs automatically upon logout from the CL.
  </p>
  <p>
  The number of frames (plots) the graphics system will buffer for a device
  is controlled by the MF (multi-frame) parameter in the <i>graphcap</i> entry
  for the device.  When the multi-frame count is reached the buffered output
  is automatically disposed of to the device.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Flush any graphics output and initialize the graphics system.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; gflush
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  cursor, stdplot
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

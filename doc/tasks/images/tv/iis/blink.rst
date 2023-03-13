.. _blink:

blink: Blink two frames
=======================

**Package: iis**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  blink frame1 frame2 [frame3 [frame4]]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_frame1">
  <dt><b>frame1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='frame1' Line='frame1' -->
  <dd>First frame in blink sequence.
  </dd>
  </dl>
  <dl id="l_frame2">
  <dt><b>frame2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='frame2' Line='frame2' -->
  <dd>Second frame in blink sequence.
  </dd>
  </dl>
  <dl id="l_frame3">
  <dt><b>frame3</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='frame3' Line='frame3' -->
  <dd>Third frame in blink sequence.
  </dd>
  </dl>
  <dl id="l_frame4">
  <dt><b>frame4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='frame4' Line='frame4' -->
  <dd>Fourth frame in blink sequence.
  </dd>
  </dl>
  <dl id="l_rate">
  <dt><b>rate = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rate' Line='rate = 1.' -->
  <dd>Blink rate in seconds per frame.  May be any fraction of a second.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Two or more frames are alternately displayed on the image display monitor
  (<span style="font-family: monospace;">"stdimage"</span>) at a specified rate per frame.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To blink two frames:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; blink 1 2
  </pre></div>
  <p>
  To blink three frames at a rate of 2 seconds per frame:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; blink 3 1 2 rate=2
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The blink rate is measured in
  software and, therefore, will not be exactly even in a time sharing
  environment.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  cv
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

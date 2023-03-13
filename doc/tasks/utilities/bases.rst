.. _bases:

bases: Convert an integer to hex, octal, and binary
===================================================

**Package: utilities**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  bases i
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_i">
  <dt><b>i</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='i' Line='i' -->
  <dd>Integer for base conversion.
  </dd>
  </dl>
  <dl id="l_nbyte">
  <dt><b>nbyte = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nbyte' Line='nbyte = 0' -->
  <dd>Number of bytes of precision.  Allowed values are <span style="font-family: monospace;">"0"</span>, <span style="font-family: monospace;">"1"</span>, <span style="font-family: monospace;">"2"</span>, or <span style="font-family: monospace;">"4"</span>.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print labels for columns?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The BASES task converts an input integer value to equivalent values in
  other base systems.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convert the number 256 (in various bases).  Note the <span style="font-family: monospace;">'x'</span> and <span style="font-family: monospace;">'b'</span> suffix
  appended to the value to change the input base value:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ecl&gt; bases 256                                  # decimal input
    dec    hex    octal   7654 3210 7654 3210
    256   0100x  000400b  0000 0001 0000 0000
  ecl&gt; bases 256x                                 # hex input
    dec    hex    octal   7654 3210 7654 3210
    598   0256x  001126b  0000 0010 0101 0110
  ecl&gt; bases 256b                                 # octal input
    dec  hex  oct   7654 3210
    174  AEx  256b  1010 1110
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

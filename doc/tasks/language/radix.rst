.. _radix:

radix: Encode a number in the specified radix
=============================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  string = radix (number, newradix)
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_number">
  <dt><b>number</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='number' Line='number' -->
  <dd>The integer number to be encoded.
  </dd>
  </dl>
  <dl id="l_newradix">
  <dt><b>newradix</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newradix' Line='newradix' -->
  <dd>The radix or base in which the number is to be printed,
  e.g., 2 (binary), 8 (octal), 10 (decimal), 16 (hex), and so on.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Radix</i> is a string valued intrinsic function which formats an integer
  number in the indicated radix, return the encoded string as the function
  value.  Note that the CL permits numbers to be input in octal or hex format
  (trailing B or X suffix respectively), allowing common numeric conversions
  to decimal to be done directly.  The <i>radix</i> function is however the
  only CL function currently available for printing numbers in bases other
  than 10.  <i>Radix</i> can only be called as a function.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print the hex number 7cde in binary.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; = radix (7cdex, 2)
  </pre></div>
  <p>
  2. Print the hex number 7cde in decimal.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; = 7cdex
  </pre></div>
  <p>
  3. Print the number in variable I in decimal, octal, and hex.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; print (i, radix(i,8), " ", radix(i,16))
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Very large bases produce strange results.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  print
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

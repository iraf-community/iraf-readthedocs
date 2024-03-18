.. _if:

if: If statement
================

**Package: language**

.. raw:: html

  <section id="s_syntax">
  <h3>Syntax</h3>
  <p>
  <i>if</i> (expression) statement1 [<i>else</i> statement2]
  </p>
  </section>
  <section id="s_elements">
  <h3>Elements</h3>
  <dl id="l_expression">
  <dt><b>expression</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='expression' Line='expression' -->
  <dd>A boolean valued expression.
  </dd>
  </dl>
  <dl id="l_statement1">
  <dt><b>statement1, statement2</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='statement1' Line='statement1, statement2' -->
  <dd>The statements to be executed (possibly compound, i.e., enclosed in
  curly braces).
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>if</i> statement is used to execute a statement only if the
  specified condition is true.  An optional <i>else</i> clause may be given
  to execute a different statement if the condition is false.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Add X to Y only if X is less than Y.
  </p>
  <div class="highlight-default-notranslate"><pre>
  if (x &lt; y)
      y += x
  </pre></div>
  <p>
  2. If X is less than 10 print <span style="font-family: monospace;">"small"</span>, else print <span style="font-family: monospace;">"big"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  if (x &lt; 10)
      print ("small")
  else
      print ("big")
  </pre></div>
  <p>
  3. The <i>else if</i> construct.
  </p>
  <div class="highlight-default-notranslate"><pre>
  if (str == "+")
      val += x
  else if (str == "-")
      val -= x
  else if
      ...
  </pre></div>
  <p>
  4. Nesting, use of braces.
  </p>
  <div class="highlight-default-notranslate"><pre>
  if (i &gt; 0) {
      if (i &lt; 10) {
          print ("0")
          sum = sum * 10 + i
      } else
          print (" ")
  }
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  for, case, break, next
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNTAX' 'ELEMENTS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

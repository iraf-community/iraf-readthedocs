.. _while:

while: While loop
=================

**Package: language**

.. raw:: html

  <section id="s_syntax">
  <h3>Syntax</h3>
  <p>
  while (expression) statement
  </p>
  </section>
  <section id="s_elements">
  <h3>Elements</h3>
  <dl id="l_while">
  <dt><b>while</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='while' Line='while' -->
  <dd>Required keyword.
  </dd>
  </dl>
  <dl id="l_expression">
  <dt><b>expression</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='expression' Line='expression' -->
  <dd>A boolean valued expression tested before each iteration.
  </dd>
  </dl>
  <dl id="l_statement">
  <dt><b>statement</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='statement' Line='statement' -->
  <dd>A statement (possibly compound) to be executed in each iteration of the loop.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>while</i> loop executes the enclosed statements while the specified
  condition is true.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. An infinite loop.
  </p>
  <div class="highlight-default-notranslate"><pre>
  while (yes) {
      sleep 30
      time
  }
  </pre></div>
  <p>
  2. Type a file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  list = "home$login.cl"
  while (fscan (list, line) != EOF)
      print (line)
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  for, case, break, next
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNTAX' 'ELEMENTS' 'DESCRIPTION' 'EXAMPLES' 'SEE ALSO'  -->
  

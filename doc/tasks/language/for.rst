.. _for:

for: C-style for loop construct
===============================

**Package: language**

.. raw:: html

  <section id="s_syntax">
  <h3>Syntax</h3>
  <p>
  for ([assign1] ; [bool_expr] ; [assign2]) statement
  </p>
  </section>
  <section id="s_elements">
  <h3>Elements</h3>
  <dl id="l_assign1">
  <dt><b>assign1</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='assign1' Line='assign1' -->
  <dd>An assignment used to initialize the <i>for</i> loop.
  </dd>
  </dl>
  <dl id="l_bool_expr">
  <dt><b>bool_expr</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='bool_expr' Line='bool_expr' -->
  <dd>A boolean valued expression tested before each iteration.
  </dd>
  </dl>
  <dl id="l_assign2">
  <dt><b>assign2</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='assign2' Line='assign2' -->
  <dd>An assignment executed after each iteration of the loop.
  </dd>
  </dl>
  <dl id="l_statement">
  <dt><b>statement</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='statement' Line='statement' -->
  <dd>A statement (possibly compound, i.e., enclosed in curly brackets)
  to be executed in each iteration of the loop.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>for</i> statement provides a looping mechanism similar to the C-language
  for loop.  <i>Assign1</i> and <i>assign2</i> are assignment statements using
  one of the operators <span style="font-family: monospace;">'='</span>, '+=', '-=', '/=', '*='.  Any of the elements of
  the <i>for</i> loop may be omitted, except the parenthesis and colon field
  delimiters.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. For I equals zero to 10 in steps of 2, increment TOTAL by the value of
  array element I.
  </p>
  <div class="highlight-default-notranslate"><pre>
  for (i=0;  i &lt;= 10;  i += 2)
      total += array[i]
  </pre></div>
  <p>
  2. Print the first eight powers of two.
  </p>
  <div class="highlight-default-notranslate"><pre>
  j = 1
  for (i=1;  i &lt;= 8;  i += 1) {
       print (i, j)
       j *= 2
  }
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  A simple assignment of the form i++ will not work.
  Only one assignment statement is permitted in the first and third fields.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  while, case, break, next
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNTAX' 'ELEMENTS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

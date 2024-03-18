.. _switch:

switch: Multiway branch construct
=================================

**Package: language**

.. raw:: html

  <section id="s_syntax">
  <h3>Syntax</h3>
  <div class="highlight-default-notranslate"><pre>
  switch (expr) {
  case val1 [, val1,...]:
      statements
  case val3 [, val3,...]:
      statements
          (etc.)
  default:
      statements
  }
  </pre></div>
  </section>
  <section id="s_elements">
  <h3>Elements</h3>
  <dl id="l_expr">
  <dt><b>expr</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='expr' Line='expr' -->
  <dd>An integer-valued expression tested before entry into the switch block.
  </dd>
  </dl>
  <dl id="l_valN">
  <dt><b>valN</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='valN' Line='valN' -->
  <dd>Integer valued constants used to match expression.
  </dd>
  </dl>
  <dl id="l_statements">
  <dt><b>statements</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='statements' Line='statements' -->
  <dd>Simple or compound statements to be executed when the appropriate case or
  default block is selected.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>switch</i> statement provides a multiway branch capability.
  The switch expression is evaluated and control branches to the matching
  <i>case</i> block.  If there is no match the <i>default</i> block, if present,
  receives control.  If no <i>default</i> block is present, the switch is skipped.
  </p>
  <p>
  Each <i>case</i> statement consists of a list of values defining the case,
  and an executable statement (possibly compound) to be executed if the case
  is selected by the switch.  Execution will continue until the next case is
  reached, at which time a branch out of the <i>switch</i> statement occurs.
  Note this difference from the C switch case, where an explicit <i>break</i>
  statement is required to exit a switch.  If a <i>break</i> is used in a CL
  switch, it will act upon the loop statement containing the switch, not the
  switch itself.
  </p>
  <p>
  Note that both the switch expression and the case constants may
  be integers, or single characters which are evaluated to their
  ASCII equivalents.
  </p>
  <p>
  The <i>default</i> statement must be the last statement in the switch block.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Multiple cases, no default case.
  </p>
  <div class="highlight-default-notranslate"><pre>
  switch (opcode) {
  case 1:
      task1 (args)
  case 2:
      task2 (args)
  case 5:
      task5 (args)
  }
  </pre></div>
  <p>
  2. Multiple values in a case.
  </p>
  <div class="highlight-default-notranslate"><pre>
  switch (digit) {
  case <span style="font-family: monospace;">'1'</span>,<span style="font-family: monospace;">'2'</span>,<span style="font-family: monospace;">'3'</span>,<span style="font-family: monospace;">'4'</span>,<span style="font-family: monospace;">'5'</span>,<span style="font-family: monospace;">'6'</span>,<span style="font-family: monospace;">'7'</span>:
      n = n * 8 + digit - <span style="font-family: monospace;">'0'</span>
  default:
      error (1, "invalid number")
  }
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Only integer values are allowed (no strings).
  The case values must be constants; ranges are not permitted.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  if else, goto
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNTAX' 'ELEMENTS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

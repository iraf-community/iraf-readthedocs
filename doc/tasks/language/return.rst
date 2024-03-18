.. _return:

return: Return from script with an optional value
=================================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  return [value]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_value">
  <dt><b>value</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='value' Line='value' -->
  <dd>An optional value returned to the invoking procedure.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>return</i> statement terminates a script and optionally returns a
  value to the invoking routine.  Any number of <i>return</i> statements
  may be present in a script.  A <i>return</i> statement without a value
  is equivalent to a <i>bye</i>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  return
  return (j+3)
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The return value cannot currently be utilized by the invoking procedure.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  bye
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

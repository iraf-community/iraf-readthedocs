.. _goto:

goto: Goto statement
====================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <div class="highlight-default-notranslate"><pre>
  goto label
    .
    .
    .
  label: statement
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_label">
  <dt><b>label</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='label' Line='label' -->
  <dd>The destination label.  Label names have the same syntax as variable names
  and can duplicate the names of existing variables.
  </dd>
  </dl>
  <dl id="l_statement">
  <dt><b>statement</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='statement' Line='statement' -->
  <dd>The statement executed after the goto statement.  It may be any executable
  statement.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>goto</i> statement interrupts the normal flow of program execution by
  transferring control to the statement following the label.  It may also be
  used to exit from nested loops where the break statement is not adequate.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. The most common use of the <i>goto</i> statement is to branch to an error
  handler if an abnormal condition is detected.
  </p>
  <div class="highlight-default-notranslate"><pre>
  begin
          for (i=1;  i &lt;= 100;  i += 1)
              for (j=1;  j &lt;= 100;  j += 1)
                  for (k=1;  k &lt;= 100;  k += 1)
                      if (pixel[i,j,k] &lt; 0)
                          goto err
                      else
                          total += pixel[i,j,k]
  
          print ("total = ", total)
          return
  err:
          print ("Invalid pixel value at ",i,j,k)
  end
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  No checking is done to see if a jump is made into a loop.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  break, next
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

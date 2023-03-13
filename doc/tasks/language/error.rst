.. _error:

error: Print error code and message and abort
=============================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  error errcode errmsg
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_errcode">
  <dt><b>errcode</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='errcode' Line='errcode' -->
  <dd>An integer code identifying the error (not used at present in the CL since
  error handlers are not supported).
  </dd>
  </dl>
  <dl id="l_errmsg">
  <dt><b>errmsg</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='errmsg' Line='errmsg' -->
  <dd>A string describing the error.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Error</i> may be used to force an error exit from a script.
  The error message will be displayed, and control will return to the
  most recent interactive cl.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Abort the current task if there is an attempt to compute a negative
  square root.
  </p>
  <div class="highlight-default-notranslate"><pre>
  if (x &lt; 0)
      error (1, "sqrt of a negative number (x=" // x // ")")
  else
      y = sqrt (x)
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  There is currently no way to post an error handler to receive control
  if <i>error</i> is called.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  cl, bye, logout
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

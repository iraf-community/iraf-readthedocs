.. _putlog:

putlog: Put a message to the logfile
====================================

**Package: language**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  putlog logmsg
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_logmsg">
  <dt><b>logmsg</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logmsg' Line='logmsg' -->
  <dd>A message to append to the logfile.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>Putlog</i> is used to add user messages to the logfile.  The CL parameter
  <i>keeplog</i> must be set to `yes' for this to take effect.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  For executable tasks, the only way to call <i>putlog</i> currently is via
  the low-level CLIO routine clcmd().
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  cl, logging
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'BUGS' 'SEE ALSO'  -->
  

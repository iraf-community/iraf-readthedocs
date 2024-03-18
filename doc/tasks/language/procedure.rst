.. _procedure:

procedure: Start a procedure script
===================================

**Package: language**

.. raw:: html

  <section id="s_syntax">
  <h3>Syntax</h3>
  <div class="highlight-default-notranslate"><pre>
  <b>procedure</b> proc_name [( [req_par, ...] )]
  
  &lt;query mode parameter declarations&gt;
  &lt;hidden parameter declarations&gt;
  
  <b>begin</b>
          &lt;local variable declarations&gt;
          &lt;executable statements&gt;
  <b>end</b>
  </pre></div>
  </section>
  <section id="s_elements">
  <h3>Elements</h3>
  <dl id="l_proc_name">
  <dt><b>proc_name</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='proc_name' Line='proc_name' -->
  <dd>The name of the procedure.  In the case of a procedure script,
  the script file should have the same name.
  </dd>
  </dl>
  <dl id="l_req_par">
  <dt><b>req_par</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='req_par' Line='req_par' -->
  <dd>A required (query mode) parameter for the procedure.
  Hidden parameters must be declared in the declarations section but do
  not appear in the argument list.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>procedure</i> statement is used to declare a new CL procedure.
  In the current CL, procedures are permitted only in <span style="font-family: monospace;">".cl"</span> script files,
  and there may be only one procedure per file.  The <i>procedure</i> statement
  must be the first non-comment statement in the script file.  Any parameters
  which appear in the procedure argument list must be declared in the parameter
  declarations section as well and will default to mode <span style="font-family: monospace;">"auto"</span>.  Parameters not
  in the required parameter list will default to mode <span style="font-family: monospace;">"hidden"</span>.
  The order of positional parameters is the order in which the parameters
  appear in the argument list.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Declare a no-op procedure.
  </p>
  <div class="highlight-default-notranslate"><pre>
  procedure noop
  begin
  end
  </pre></div>
  <p>
  2. A more complex procedure (hlib$devstatus.cl).
  </p>
  <div class="highlight-default-notranslate"><pre>
  # DEVSTATUS -- Print status info for the named device.
  
  procedure devstatus (device)
  
  string  device  { prompt = "device for which status is desired" }
  bool    verbose = no
  
  string  logname, hostname
  struct  *devlist
  string  dev
  
  begin
          dev = device
          _devstatus (dev)
  
          if (verbose) {
              # Print UNIX device status, too.
  
              devlist = "dev$devices"
              while (fscan (devlist, logname, hostname) != EOF) {
                  if (logname == dev) {
                      print ("ls -l /dev/", hostname) | cl
                      break
                  }
              }
              devlist = ""
          }
  end
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  CL procedures can only be placed in script files, they cannot currently
  be typed in interactively.  Procedures cannot be precompiled.  A procedure
  cannot return a function value.  Arguments are passed only by value, not
  by reference.  Procedure interpretation (and expression evaluation) is
  currently rather slow.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  declarations, task
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNTAX' 'ELEMENTS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

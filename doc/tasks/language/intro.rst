.. _intro:

intro: A brief introduction to IRAF
===================================

**Package: language**

.. raw:: html

  <section id="s_description">
  <h3>Description</h3>
  <p>
  1. <b>General</b>
  </p>
  <p>
      The CL (or Command Language) is the command interpreter of the IRAF
  environment.  Among it's responsibilities are: task initiation and
  termination; parameter retrieval and updating; and error handling.
  In addition the CL has certain `builtin' utility functions which enable
  monitoring and changing of the IRAF environment, control flow features
  roughly modeled after C and Ratfor as well as fairly sophisticated
  capabilities for performing mathematical calculations and string manipulation.
  The CL environment may easily be extended by the user.
  </p>
  <p>
  2. <i>Task Initiation and Termination</i>
  </p>
  <p>
      IRAF organizes tasks into groups called <i>packages</i>.  When a package
  (which is itself a special kind of task) is invoked, it defines
  all the tasks which belong to that package, and the user may
  then execute any of the tasks in the package.  Some of these new
  tasks may themselves be packages.  Normally at the start of a
  CL session, the <i>language</i> package, including all functions built directly
  into the CL, and the <i>system</i> package, which contains basic system
  utilities, are automatically invoked.  The user may configure their 
  <span style="font-family: monospace;">"login.cl"</span> file to automatically invoke other packages.
  </p>
  <p>
  Within the CL a task is invoked by entering its name, e.g.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; reduce args
  </pre></div>
  <p>
  If two tasks in different packages have the same name, then the
  package name may be included:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; spectra.reduce args
  </pre></div>
  <p>
  The task name may be followed by a parameter list and tasks
  may be linked together by pipes (see parameters).  The task initiates
  execution of either a script file, an ASCII file containing further
  CL commands, or an executable image, an external program linked with
  IRAF libraries so that it may be called as a sub-process from the
  CL process.  The correspondence between the task name and the name
  of the script or image file is made using the task and redefine builtin
  commands.
  </p>
  <p>
  When a script is run the CL effectively calls itself recursively
  with the new incarnation of the CL having its standard input
  not from the terminal, but from the script file.  When the script
  terminates the recursion unwinds, and the CL returns to an interactive
  mode.  A script may itself call another script or executable.
  </p>
  <p>
  An executable is run as a separate process with communication
  and synchronization maintained using an inter-process communication
  link (a pipe in UNIX or a shared memory region in VMS).  When
  the executable requires a parameter a request is sent across the
  link, and the CL replies in the same fashion.  When the process terminates
  it informs the CL and then hibernates.  Normally the executable's
  process is not terminated, but is maintained in a process cache
  so that the executable may be used again without the overhead of
  re-initiating the process.  The process finally terminates when the CL
  finishes, when the space in the cache is needed by a new executable
  image, or when the user explicitly clears the cache using the flprcache
  command.  The size of the process cache is small, usually only
  three executables can be maintained in the cache.
  </p>
  <p>
  3. <i>Parameter Retrieval and Update</i>
  </p>
  <p>
      Most CL tasks have a parameter list associated with them.  When the task
  starts up, the CL looks to see if the user has a private copy of the
  parameters from the last time he ran this task.  If so these parameters
  are loaded into memory.  Otherwise the CL looks for the default values
  of the parameters and loads these.  While the task is active
  the parameters are maintained in memory, but when it finishes the CL
  checks if any `learned' parameters have been modified.  If so
  a new private copy of the parameters is stored into the directory
  pointed to by the IRAF logical name `uparm'.  A number of
  builtins are used to control the handling of parameters including
  lparam, eparam, update and unlearn.
  </p>
  <p>
  4. <i>Error Handling</i>
  </p>
  <p>
      The CL attempts to trap most kinds of errors that may occur and
  to keep the user in a viable IRAF environment.  When an error occurs in
  a script, execution of the script is terminated and the CL returns to an
  interactive level.  The user may force an error using the <i>error</i>
  builtin.  When a executable image encounters an error it cannot handle
  itself, it sends an error message to the CL and then hibernates in the
  process cache until its next invocation.  If executable was called by
  a script, the script is terminated and the CL returns to an interactive mode.
  The error message from the executable is relayed to the user.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  commands, mathfcns, strings
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'DESCRIPTION' 'SEE ALSO'  -->
  

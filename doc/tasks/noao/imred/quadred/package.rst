.. _package:

package: Package parameters and overview
========================================

**Package: quadred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  package	pkgname
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_pkgname">
  <dt><b>pkgname</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pkgname' Line='pkgname' -->
  <dd>The name of the new package to be created.  If called with no arguments,
  <i>package</i> lists the currently defined packages in task search order.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <i>package</i> task creates a new package.
  The newly defined package becomes the current package, and the prompt
  is changed to use the first two characters of the package name.
  The package command does not define any tasks within the package, that
  is done by subsequent <i>task</i> declarations.  Subsequent <i>task</i>
  declarations will add tasks to the task list for the new package.
  </p>
  <p>
  The new package remains the <span style="font-family: monospace;">"current package"</span> until another <i>package</i>
  command is entered, or until the task in which the package command was
  entered is terminated.
  Normally <i>package</i> will be used at the beginning of a script to define
  the package name.  It will be followed by one or more task definitions,
  and then by a <i>cl</i> or <i>clbye</i> to interpret user commands,
  until the command <i>bye</i> is entered by the user, at which time the
  package script task terminates, discarding the package and any associated
  definitions.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. The use of <i>package</i> in a package script task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  package lists
  
  set     lists           = "pkg$lists/"
  
  task    table,
          tokens,
          unique,
          lintran,
          columns,
          words           = "lists$x_lists.e"
  
  task    $gcursor        = "lists$gcursor.cl"
  task    $imcursor       = "lists$imcursor.cl"
  task    average         = "lists$average.cl"
  
  clbye()
  </pre></div>
  <p>
  2. List the currently defined packages in the order in which they will
  be searched for tasks.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; pack
  clpackage
  language
  user
  system
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  All active packages must have unique names.  To eliminate the possibility
  of parameter file name collisions in UPARM, the three character string
  formed by concatenating the first two and final characters of the package
  name should be unique.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  task, redefine
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

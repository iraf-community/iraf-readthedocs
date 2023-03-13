.. _mkscript:

mkscript: Make a command script
===============================

**Package: system**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  mkscript script task submit
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_script">
  <dt><b>script</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='script' Line='script' -->
  <dd>Script file name.  Commands will be successively added to this file.
  </dd>
  </dl>
  <dl id="l_task">
  <dt><b>task   </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='task' Line='task   ' -->
  <dd>Task name of command to be added to the script.  If given on the command
  line then only commands for this task may be added to the script.
  If not given on the command line then the task will query for a task
  name for each new command.  Currently the task name must not be abbreviated.
  </dd>
  </dl>
  <dl id="l_submit">
  <dt><b>submit</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='submit' Line='submit' -->
  <dd>Submit the completed script as a background job as the last act of the task?
  If not given on the command line the task will query before submitting the
  script.
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = no' -->
  <dd>Append new commands to an existing script file?
  If no the file will be deleted first.   If <i>verify</i> = yes
  the user will be asked to confirm the deletion.
  </dd>
  </dl>
  <dl id="l_hidden">
  <dt><b>hidden = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='hidden' Line='hidden = yes' -->
  <dd>Include hidden parameters in each command?
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = yes' -->
  <dd>Verify each command, any file deletions, and the final script?
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">"script.log"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = "script.log"' -->
  <dd>Script log file name.  When the script is submitted as a background job
  by this task any command and error output is directed to this file.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  A command script is created consisting of a number of commands to be
  executed sequentially.  The task assumes the responsibility of formatting
  the command and placing it in the script file.  The user sets the
  parameter values using the parameter editor <b>eparam</b>.  As an optional
  final stage the task will optionally submit the script as a background job.
  </p>
  <p>
  The sequence of steps are outline as follows:
  </p>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(1)' -->
  <dd>If the script already exists and <i>append</i> = no the script file
  is deleted.  When <i>verify</i> = yes the deletion is verified with the
  user.
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(2)' -->
  <dd>If the task is not specified on the command line then the user
  is queried for a task name.
  <dl>
  <dt><b>(2a)</b></dt>
  <!-- Sec='DESCRIPTION' Level=1 Label='' Line='(2a)' -->
  <dd>The task must be loaded.  If it has not been loaded a message is printed
  and the task query is repeated.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl>
  <dt><b>(3)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(3)' -->
  <dd><b>Eparam</b> is now invoked to allow the user to set the task
  parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>(4)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(4)' -->
  <dd>If <i>verify</i> = yes the command is printed and the user is asked if the
  command is ok.  If ok the command is added to the script.
  </dd>
  </dl>
  <dl>
  <dt><b>(5)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(5)' -->
  <dd>The user is asked if another command is to be added to the script.  While
  the response is yes steps 2 to 5 are repeated.
  </dd>
  </dl>
  <dl>
  <dt><b>(6)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(6)' -->
  <dd>If <i>verify</i> = yes the script is paged and the user is asked if the
  script is ok.  If not ok the script is deleted, with user confirmation,
  and steps 2 to 6 are repeated.
  </dd>
  </dl>
  <dl>
  <dt><b>(7)</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='' Line='(7)' -->
  <dd>If the submit parameter is not specified on the command line the user
  is asked if the script should be submitted as a background job.
  </dd>
  </dl>
  <p>
  The parameter <i>hidden</i> is important for the following reason.  If
  the hidden parameters are not explicitly included in the script commands
  then the values of the hidden parameters will be those in the parameter
  file at the time of execution.  Thus, in changes in the hidden parameters
  with <b>eparam</b> or explicit changes may produce unexpected results.
  However, if the hidden parameters are never changed then the commands
  are more readable when the hidden parameters are not included.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  One of the most common usages in data reductions is to create repeated
  commands with different input data or parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkscript script.cl transform
  
  [<i>eparam</i> is called to set the parameter values for <i>transform</i>]
  
  transform ("n1r.008", "n1r.008a", "disp012,distort,disp013",
  database="identify.db", interptype="spline3", x1=1., x2=256., dx=1.,
  nx=256., xlog=no, y1=4300., y2=6300., dy=INDEF, ny=800., ylog=no,
  flux=yes, logfiles="STDOUT,logfile")
  
  Is the command ok? (yes):
  Add another command? (yes):
  
  [<i>eparam</i> is called again for task <i>transform</i>]
  
  transform ("n1r.010", "n1r.010a", "disp013,distort",
  database="identify.db", interptype="spline3", x1=1., x2=256., dx=1.,
  nx=256., xlog=no, y1=4300., y2=6300., dy=INDEF, ny=800., ylog=no,
  flux=yes, logfiles="STDOUT,logfile")
  
  Is the command ok? (yes):
  Add another command? (yes): no
  
  [The script is paged]
  
  Is the script ok? (yes):
  Submit the script as a background job? (yes):
  Script script.cl submitted at:
  Fri 10:32:57 01-Nov-85
  [1]
  </pre></div>
  <p>
  To combine several tasks:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; mkscript script.cl ver- sub- hid-
  Task name of command to be added to script: response
  
  [<i>eparam</i> is called for <i>response</i> and parameter values are set]
  
  Add another command? (yes):
  Task name of command to be added to script: imarith
  Add another command? (yes): no
  </pre></div>
  <p>
  To run the command script as a foreground job:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cl &lt; script.cl
  </pre></div>
  <p>
  To run the command script as a background job:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; cl &lt; script.cl &gt;&amp; logfile &amp;
  </pre></div>
  <p>
  Note that the output including possible error output is redirected to a logfile.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The current implementation is preliminary.  It is done with a script which
  makes it seem somewhat slow.  The most important bug is that the command
  formatter is based on the output of <b>lparam</b>.  If a task parameter
  name exceeds 12 characters it is truncated by <b>lparam</b> and is then
  also truncated by the command formatter.  The script will then fail when
  executed!  Also the task name may not be abbreviated.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  eparam
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

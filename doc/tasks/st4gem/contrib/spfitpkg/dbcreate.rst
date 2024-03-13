.. _dbcreate:

dbcreate: Task for interactively creating specfit database files
================================================================

**Package: spfitpkg**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  dbcreate namedata
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_namedata">
  <dt><b>namedata</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='namedata' Line='namedata' -->
  <dd>This is the name of the new database file.  The resulting file will be saved 
  automatically with the leading <span style="font-family: monospace;">"sf"</span> extension in the current directory.
  </dd>
  </dl>
  <dl id="l_low_mult">
  <dt><b>low_mult</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_mult' Line='low_mult' -->
  <dd>This number multiplied by the parameter value will create the default lower 
  limit.
  </dd>
  </dl>
  <dl id="l_high_mult">
  <dt><b>high_mult</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='high_mult' Line='high_mult' -->
  <dd>Same as low_mult but used to create the upper parameter limit.
  </dd>
  </dl>
  <dl id="l_step_mult">
  <dt><b>step_mult</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='step_mult' Line='step_mult' -->
  <dd>Used to create the default step size.
  </dd>
  </dl>
  <dl id="l_comp_name">
  <dt><b>comp_name</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='comp_name' Line='comp_name' -->
  <dd>Enter the name for the type of component desired.  See the help for <span style="font-family: monospace;">"specfit"</span>
  for a description of the available component types.
  </dd>
  </dl>
  <dl id="l_comment">
  <dt><b>comment</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='comment' Line='comment' -->
  <dd>A descriptive comment for this component may be entered.  For example,
  <span style="font-family: monospace;">"Broad component of Halpha emission"</span>.
  </dd>
  </dl>
  <dl id="l_parambool">
  <dt><b>parambool</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='parambool' Line='parambool' -->
  <dd>yes or no.  Used to affirm a correct entry.
  </dd>
  </dl>
  <dl id="l_parameters">
  <dt><b>parameters</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='parameters' Line='parameters' -->
  <dd>Enter the number of parameters associated with the chosen component type.
  See the help for <span style="font-family: monospace;">"specfit"</span> for details.
  </dd>
  </dl>
  <dl id="l_new_par_value">
  <dt><b>new_par_value</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='new_par_value' Line='new_par_value' -->
  <dd>The value for the new parameter to be entered in the database.
  </dd>
  </dl>
  <dl id="l_lower_limit">
  <dt><b>lower_limit</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lower_limit' Line='lower_limit' -->
  <dd>Lower limit for the new parameter
  </dd>
  </dl>
  <dl id="l_upper_limit">
  <dt><b>upper_limit</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='upper_limit' Line='upper_limit' -->
  <dd>Upper limit for the new parameter
  </dd>
  </dl>
  <dl id="l_step_size">
  <dt><b>step_size</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='step_size' Line='step_size' -->
  <dd>Step size for the new parameter
  </dd>
  </dl>
  <dl id="l_param_tolerance">
  <dt><b>param_tolerance</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='param_tolerance' Line='param_tolerance' -->
  <dd>Tolerance for the new parameter.  Values of 0.01 to 1.e-6 are recommended.
  </dd>
  </dl>
  <dl id="l_fix_or_free">
  <dt><b>fix_or_free</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fix_or_free' Line='fix_or_free' -->
  <dd>For freely varying parameters, enter 0.  For fixed parameters, enter -1.
  For parameters linked to another component, enter the positive integer
  giving that component's number.
  (See the help for specfit for details on linking.)
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This program will create a database file for use by specfit.  It will 
  prompt you for all the required values and write out the new database in the
  correct format.  This is a simpler and more error-free method for creating a new
  database than the usual way of editing a text file.   It calls the task dbcheck
  to verify the new database file.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION'  -->
  

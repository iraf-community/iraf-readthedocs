.. _refdata:

refdata: Pset to specify common synphot parameters.
===================================================

**Package: synphot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  refdata
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The 'refdata' parameters specify certain quantities that are common to
  all tasks in the synphot package.
  </p>
  <p>
  Note that this is a pset, not an executable task;  it defines a set of 
  parameters used by other tasks.  Invoking the pset by name runs
  'eparam' on the parameter set, allowing the user to modify the
  parameters.  Alternatively, the parameters may be modified on the
  command line by specifying the pset name and parameter name.
  For example, you can type <span style="font-family: monospace;">"refdata.area=7853.98"</span> to set the
  collecting area to that of a 1-meter telescope.
  Parameters can also be edited by using
  'eparam' on the calling task (e.g., by typing <span style="font-family: monospace;">"eparam calcphot"</span>), in 
  which case, 'refdata' will appear as one of the task parameters. The
  'refdata' parameters may then be edited by positioning the cursor on
  the line containing the 'refdata' name and typing <span style="font-family: monospace;">":e"</span>.  After editing
  the pset parameters, type Control-D (or :q) to return to the main task 
  parameter menu.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>(area = 45238.93416) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(area = 45238.93416) [real]' -->
  <dd>Telescope area in square centimeters.  The default is the value for the HST.
  </dd>
  </dl>
  <dl>
  <dt><b>(grtbl = <span style="font-family: monospace;">"mtab$*.tmg"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(grtbl = "mtab$*.tmg") [string]' -->
  <dd>File name template specifying the name of the instrument graph table.
  The default string, containing the <span style="font-family: monospace;">"*"</span> wildcard, will search for the
  latest available version of the table.
  </dd>
  </dl>
  <dl>
  <dt><b>(cmptbl = <span style="font-family: monospace;">"mtab$*.tmc"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(cmptbl = "mtab$*.tmc") [string]' -->
  <dd>File name template specifying the name of the instrument component table.
  The default string, containing the <span style="font-family: monospace;">"*"</span> wildcard, will search for the
  latest available version of the table.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  Type <span style="font-family: monospace;">"help synphot opt=sys"</span> for a more detailed description of the
  format and contents of the instrument graph and component tables.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

.. _diagcols:

diagcols: Pset for zone temperature & density column names
==========================================================

**Package: nebular**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  fluxcols
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The `diagcols' parameters specify the names of the table columns 
  containing electron temperatures and densities in each of three 
  ionization zones.  These values are computed by the `zones' task 
  and used by the `abund' nebular modelling task.  The default values 
  are usable even if these columns are not present in the input 
  table, and are really intended to give the user some flexibility in 
  naming the table columns.  If a column with the specified name 
  already exists in the input table when running `zones' its contents 
  will be overwritten. 
  </p>
  <p>
  Note that this is a pset, not an executable task; it defines a set 
  of parameters used by other tasks.  Invoking the pset by name runs 
  `eparam' on the parameter set, allowing the user to modify the 
  parameters.  Alternatively, the parameters may be modified on the 
  command line by specifying the pset name and parameter name.  For 
  example, the user can type `diagcols.te_med_col=<span style="font-family: monospace;">"Te_Med"</span>' to set 
  the name of the table column containing the electron temperature 
  for the medium-ionization zone to the string <span style="font-family: monospace;">"Te_Med"</span>.  (Note that 
  the column names are always converted to upper-case in the table.)  
  Parameters can also be edited by using `eparam' on the calling task 
  (e.g., by typing <span style="font-family: monospace;">"eparam abund"</span>), in which case `diagcols' will 
  appear as one of the task parameters; the `diagcols' parameters may 
  then be edited by positioning the cursor on the line containing the 
  pset name and typing <span style="font-family: monospace;">":e"</span>.  After editing the pset parameters, exit 
  normally from eparam (with an EOF, usually &lt;cntr-Z&gt;) to return to 
  the main task parameter menu.  
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>(ne_low_col = <span style="font-family: monospace;">"Ne_Low"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ne_low_col = "Ne_Low") [string]' -->
  <dd>Name of the column containing the electron density in the low-
  ionization zone.  
  </dd>
  </dl>
  <dl>
  <dt><b>(ne_med_col = <span style="font-family: monospace;">"Ne_Med"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ne_med_col = "Ne_Med") [string]' -->
  <dd>Name of the column containing the electron density in the 
  medium-ionization zone.  
  </dd>
  </dl>
  <dl>
  <dt><b>(ne_hi_col = <span style="font-family: monospace;">"Ne_Hi"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(ne_hi_col = "Ne_Hi") [string]' -->
  <dd>Name of the column containing the electron density in the 
  high-ionization zone.  
  </dd>
  </dl>
  <dl>
  <dt><b>(te_low_col = <span style="font-family: monospace;">"Te_Low"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(te_low_col = "Te_Low") [string]' -->
  <dd>Name of the column containing the electron temperature in the 
  low-ionization zone.  
  </dd>
  </dl>
  <dl>
  <dt><b>(te_med_col = <span style="font-family: monospace;">"Te_Med"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(te_med_col = "Te_Med") [string]' -->
  <dd>Name of the column containing the electron temperature in the 
  medium-ionization zone.  
  </dd>
  </dl>
  <dl>
  <dt><b>(te_hi_col = <span style="font-family: monospace;">"Te_Hi"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(te_hi_col = "Te_Hi") [string]' -->
  <dd>Name of the column containing the electron temperature in the 
  high-ionization zone.  
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  abund, nlevel, fluxcols, zones
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'SEE ALSO'  -->
  

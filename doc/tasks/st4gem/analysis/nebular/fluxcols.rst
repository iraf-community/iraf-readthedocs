.. _fluxcols:

fluxcols: Pset for line flux column names
=========================================

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
  The `fluxcols' parameters specify the column names in the table 
  used in the `zones' and `abund' nebular modelling tasks.  These 
  columns include the object name and region code, the nebular 
  extinction constant and extinction correction flag, an optical-to-
  UV scale factor, and the line fluxes or line ratios that will be 
  used for computing the electron temperature and density.  
  </p>
  <p>
  The default values are usable even if these columns are not present 
  in the input table, and are really intended to give the user some 
  flexibility in naming the table columns.  If a column with the 
  specified name already exists in the input table its contents will 
  be used; if one does not exist the line flux is assumed to be 
  INDEF, and the corresponding physical diagnostic and/or ionic 
  abundance will not be based upon that line unless its value can be 
  otherwise calculated.  
  </p>
  <p>
  Note that this is a pset, not an executable task; it defines a set 
  of parameters used by other tasks.  Invoking the pset by name runs 
  `eparam' on the parameter set, allowing the user to modify the 
  parameters.  Alternatively, the parameters may be modified on the 
  command line by specifying the pset name and parameter name.  For 
  example, the user can type `fluxcols.o5007_col=<span style="font-family: monospace;">"Oiii(5007)"</span>' to set 
  the name of the table column containing the [O iii] 5007 A flux to 
  the string <span style="font-family: monospace;">"Oiii(5007)"</span>.  (Note that the column names are always 
  converted to upper-case in the table.)  Parameters can also be 
  edited by using `eparam' on the calling task (e.g., by typing 
  <span style="font-family: monospace;">"eparam zones"</span>), in which case `fluxcols' will appear as one of the 
  task parameters; the `fluxcols' parameters may then be edited by 
  positioning the cursor on the line containing the pset name and 
  typing <span style="font-family: monospace;">":e"</span>.  After editing the pset parameters, exit normally from 
  eparam (with an EOF, usually &lt;cntr-Z&gt;) to return to the main task 
  parameter menu.  
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl>
  <dt><b>(object_col = <span style="font-family: monospace;">"Object_ID"</span>, region_col = <span style="font-family: monospace;">"Region"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(object_col = "Object_ID", region_col = "Region") [string]' -->
  <dd>Names of columns containing the target name, and the region 
  within the target, if any.  
  </dd>
  </dl>
  <dl>
  <dt><b>(opt2uv_col = <span style="font-family: monospace;">"Scale(Opt/UV)"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(opt2uv_col = "Scale(Opt/UV)") [string]' -->
  <dd>Name of the table column containing the optical-to-UV flux 
  scale factor.  Often the nebular fluxes are listed on a scale 
  of F(H-beta) = 100, but UV fluxes are given in scaled physical 
  units (such as 10^{-14} erg/cm^2/s).  This parameter can be 
  used to relate the two relative scales; the default is 1.0, 
  even if this column is not found in the input table.  
  </dd>
  </dl>
  <dl>
  <dt><b>(c_ext_col = <span style="font-family: monospace;">"c_Extinct"</span>, extcorr_col = <span style="font-family: monospace;">"Ext_Corr"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(c_ext_col = "c_Extinct", extcorr_col = "Ext_Corr") [string]' -->
  <dd>Names of columns containing the logarithmic extinction at 
  H-Beta (traditionally denoted by <span style="font-family: monospace;">"c"</span> in the literature), and 
  the flag indicating whether the correction for I.S. extinction 
  has already been applied to the fluxes.  If the <span style="font-family: monospace;">"c_Extinct"</span> and 
  <span style="font-family: monospace;">"Ext_Corr"</span> columns are both missing, no reddening correction is 
  applied.  
  </dd>
  </dl>
  <dl>
  <dt><b>(redlaw_col = <span style="font-family: monospace;">"Ext_Law"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(redlaw_col = "Ext_Law") [string]' -->
  <dd>Name of the column containing the choice of interstellar extinction 
  law to apply.  If the <span style="font-family: monospace;">"Ext_Law"</span> column is missing, the average 
  extinction law for the Galaxy (Savage &amp; Mathis 1979) will be 
  used if the reddening correction is performed.  
  </dd>
  </dl>
  <dl>
  <dt><b>(h4861_col = <span style="font-family: monospace;">"Hi(4861)"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(h4861_col = "Hi(4861)") [string]' -->
  <dd>Name of the column containing the flux of H-beta, 4861.3 Ang. 
  Emission line fluxes are normalized to H(beta)=100 during the 
  abundance calculations.  
  </dd>
  </dl>
  <dl>
  <dt><b>(faluminum = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(faluminum = "") [pset]' -->
  <dd>Parameter set to specify column names for aluminum line fluxes.  
  </dd>
  </dl>
  <dl>
  <dt><b>(fargon = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fargon = "") [pset]' -->
  <dd>Parameter set to specify column names for argon line fluxes.  
  </dd>
  </dl>
  <dl>
  <dt><b>(fcalcium = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fcalcium = "") [pset]' -->
  <dd>Parameter set to specify column names for calcium line fluxes.  
  </dd>
  </dl>
  <dl>
  <dt><b>(fcarbon = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fcarbon = "") [pset]' -->
  <dd>Parameter set to specify column names for carbon line fluxes.  
  </dd>
  </dl>
  <dl>
  <dt><b>(fchlorine = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fchlorine = "") [pset]' -->
  <dd>Parameter set to specify column names for chlorine line fluxes.  
  </dd>
  </dl>
  <dl>
  <dt><b>(fmagnesium = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fmagnesium = "") [pset]' -->
  <dd>Parameter set to specify column names for magnesium line fluxes.  
  </dd>
  </dl>
  <dl>
  <dt><b>(fneon = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fneon = "") [pset]' -->
  <dd>Parameter set to specify column names for neon line fluxes.  
  </dd>
  </dl>
  <dl>
  <dt><b>(fnitrogen = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fnitrogen = "") [pset]' -->
  <dd>Parameter set to specify column names for nitrogen line fluxes.  
  </dd>
  </dl>
  <dl>
  <dt><b>(foxygen = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(foxygen = "") [pset]' -->
  <dd>Parameter set to specify column names for oxygen line fluxes.  
  </dd>
  </dl>
  <dl>
  <dt><b>(fpotassium = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fpotassium = "") [pset]' -->
  <dd>Parameter set to specify column names for potassium line fluxes.  
  </dd>
  </dl>
  <dl>
  <dt><b>(fsilicon = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fsilicon = "") [pset]' -->
  <dd>Parameter set to specify column names for silicon line fluxes.  
  </dd>
  </dl>
  <dl>
  <dt><b>(fsodium = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fsodium = "") [pset]' -->
  <dd>Parameter set to specify column names for sodium line fluxes.  
  </dd>
  </dl>
  <dl>
  <dt><b>(fsulfur = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fsulfur = "") [pset]' -->
  <dd>Parameter set to specify column names for sulfur line fluxes.  
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  abund, nlevel, zones
  </p>
  <p>
  Type <span style="font-family: monospace;">"help nebular opt=sys"</span> for a general description of the tasks 
  in the `nebular' package.  
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'SEE ALSO'  -->
  

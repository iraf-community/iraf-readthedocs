.. _ntplot:

ntplot: Construct N_e vs. T_e plot for observed diagnostic ratios
=================================================================

**Package: nebular**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  ntplot intable
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task computes and plots curves that show the range of electron 
  temperatures (T_e) and electron densities (N_e) that are consistent 
  with various observed diagnostic line ratios.  The diagnostics from 
  an ionized nebular gas are computed within the N-level atom 
  approximation.  (For more details about this approximation, type 
  <span style="font-family: monospace;">"help nlevel"</span>.)  The user specifies the name of the STSDAS binary 
  table containing the observed line fluxes and ratios, and the task 
  plots one curve in the N_e, T_e plane for each diagnostic.  An 
  optional output table will contain each of the computed curves, one 
  per column.  The output table is useful for identifying the 
  individual curves, and for customized plotting (with, e.g., the 
  `stplot.igi' task).  This task is particularly useful for flagging 
  unreasonable input line ratios, and for determining whether a 
  detailed photoionization model is necessary for calculating the 
  physical conditions and ionic abundances.  If a detailed model is 
  necessary, the output from this task will be useful for specifying 
  the initial conditions; if not, the `zones' and `abund' tasks may 
  be sufficient for determining the physical conditions and the ionic 
  abundances.  
  </p>
  <p>
  The input table may contain line fluxes for many nebulae and/or 
  many regions within a nebula, one object/region per row. A 
  particular object in the table is selected with the <span style="font-family: monospace;">"object"</span> 
  parameter. The flux for each emission line or line ratio must be 
  given in separate columns.  The task locates particular emission 
  line fluxes via names of specific columns in the input table. 
  These columns have suggestive default names, but are entirely 
  user-definable; type <span style="font-family: monospace;">"help fluxcols"</span> for more details. (An example 
  of an input table can be found in the file <span style="font-family: monospace;">"nebular$data/flux.fits"</span>.) 
  Note that the input table need not actually contain all the 
  diagnostic lines specified in this p-set: if a named column is not 
  found, the corresponding curve will be skipped. The plot limits 
  can also be specified. 
  </p>
  <p>
  The diagnostic line ratios are derived from the input line fluxes, 
  corrected for interstellar reddening.  The reddening corrected line 
  flux <span style="font-family: monospace;">"I"</span> is derived from the input line flux <span style="font-family: monospace;">"F"</span> by: 
  </p>
  <div class="highlight-default-notranslate"><pre>
                        {-c * f(lambda)}
  I(line) = F(line) * 10
  </pre></div>
  <p>
  where <span style="font-family: monospace;">"c"</span> is the extinction constant (i.e. the logarithmic 
  extinction at H-beta, 4861 Ang), and <span style="font-family: monospace;">"f(lambda)"</span> is derived from 
  one of a few possible extinction functions.  The choices for 
  Galactic extinction are: Savage &amp; Mathis (1979), Cardelli, Clayton, 
  &amp; Mathis (1989), and the function of Kaler (1976), which is based 
  on Whitford (1958).  The choices for extra-Galactic extinction laws 
  are Howarth (1983) for the LMC, and Prevot et al. (1984) for the 
  SMC.  The value of <span style="font-family: monospace;">"c"</span> must be given in the input table if a 
  correction for reddening is desired.  However, the correction may 
  be disabled if a correction flag (stored in another table column), 
  is set to <span style="font-family: monospace;">"yes"</span>.  By default no reddening correction is performed 
  unless a valid value for <span style="font-family: monospace;">"c"</span> is available, and unless the correction 
  flag is set to <span style="font-family: monospace;">"no"</span> or is not present.  The extinction law will 
  default to that of Savage &amp; Mathis (<span style="font-family: monospace;">"gal"</span>) unless another choice is 
  specified (one of <span style="font-family: monospace;">"gal"</span>, <span style="font-family: monospace;">"ccm"</span>, <span style="font-family: monospace;">"jbk"</span>, <span style="font-family: monospace;">"lmc"</span>, or <span style="font-family: monospace;">"smc"</span>) in the 
  input table.  
  </p>
  <p>
  The available diagnostic line ratios and the ionization potential of 
  the associated ion are listed by ion below.  The line ratio is in 
  the form I(wave1)/I(wave2), where <span style="font-family: monospace;">"wave1"</span> and <span style="font-family: monospace;">"wave2"</span> are in units 
  of Angstroms; ratios involving sums of line strengths are given as 
  I(wave1+wave2)/I(wave3+wave4).  
  </p>
  <div class="highlight-default-notranslate"><pre>
              Table 1. Electron Density Diagnostics
  
    Ion    Spectrum       Line Ratio              I.P.   Zone
  -------------------------------------------------------------
    C(+1)    C ii]        I(2326) / I(2328)       11.3   Low
    C(+2)    C iii]       I(1907) / I(1909)       24.4   Med
    N(0)    [N i]         I(5198) / I(5200)        0.0   Low
    N(+2)    N iii]       I(1749) / I(1752)       29.6   Med
    O(+1)   [O ii]        I(3726) / I(3729)       13.6   Low
    O(+3)    O iv]        I(1401) / I(1405)       54.9   High
   Ne(+3)  [Ne iv]        I(2423) / I(2425)       63.5   High
   Al(+1)  [Al ii]        I(2661) / I(2670)              Low
   Si(+2)   Si iii]       I(1883) / I(1892)       16.3   Low
    S(+1)   [S ii]        I(6716) / I(6731)       10.4   Low
   Cl(+2)  [Cl iii]       I(5517) / I(5537)       23.8   Med
   Ar(+3)  [Ar iv]        I(4711) / I(4740)       40.9   Med
    K(+4)   [K v]         I(6223) / I(6349)              High
   -------------------------------------------------------------
  </pre></div>
  <div class="highlight-default-notranslate"><pre>
             Table 2. Electron Temperature Diagnostics
  
    Ion    Spectrum       Line Ratio              I.P.   Zone
  -------------------------------------------------------------
    N(+1)   [N ii]   I(6548+6583) / I(5755)       14.5   Low
    O(+0)   [O i]    I(6300+6363) / I(5577)        0.0   Low
    O(+1)   [O ii]   I(3726+3729) / I(7320+7330)  13.6   Low
    O(+2)   [O iii]  I(4959+5007) / I(4363)       35.1   Med
   Ne(+2)  [Ne iii]  I(3869+3969) / I(3342)       41.1   Med
   Ne(+3)  [Ne iv]   I(2422+2425) / I(1601+1602)  63.5   High
   Ne(+4)  [Ne v]    I(3426+3346) / I(2975)       97.0   High
   Al(+1)  [Al ii]   I(2661+2670) / I(1671)        6.0   Low
   Si(+2)   Si iii]  I(1883+1892) / I(1206)       16.3   Low
    S(+1)   [S ii]   I(6716+6731) / I(4068+4076)  10.4   Low
    S(+2)   [S iii]  I(9069+9532) / I(6312)       23.4   Med
   Cl(+3)  [Cl iv]   I(7530+8045) / I(5323)       39.9   Med
   Ar(+2)  [Ar iii]  I(7136+7751) / I(5192)       27.6   Med
   Ar(+3)  [Ar iv]   I(4711+4740) / I(2854+2868)  40.9   Med
   Ar(+4)  [Ar v]    I(6435+7006) / I(4626)       59.8   High
    K(+3)   [K iv]   I(6102+6796) / I(4511)       46.0   Med
  -------------------------------------------------------------
  </pre></div>
  <p>
  Different line types in the plot are used to denote diagnostics 
  from ions with different ionization potential, organized into three 
  zones.  Solid lines are used for low ionization species (I.P. &lt; 20 
  eV), dashed lines for intermediate ionization (20 &lt; I.P. &lt; 50 eV), 
  and dotted lines for the highest ionization diagnostics (I.P. &gt; 50 
  eV).
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_fluxtab">
  <dt><b>fluxtab = <span style="font-family: monospace;">""</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fluxtab' Line='fluxtab = "" [string]' -->
  <dd>Input table of diagnostic line fluxes. 
  </dd>
  </dl>
  <dl>
  <dt><b>(outtab = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(outtab = "") [string]' -->
  <dd>Optional output table of computed diagnostic curves.  If blank, no 
  output table will be produced. 
  </dd>
  </dl>
  <dl>
  <dt><b>(object = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(object = "") [string]' -->
  <dd>Object to select within the input table, if more than one is 
  present.  Individual objects, and regions within objects, must be 
  stored one per row in the input table. 
  </dd>
  </dl>
  <dl>
  <dt><b>(min_dens = 10.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(min_dens = 10.) [real]' -->
  <dd>Minimum density for plot, in units of 1/cm^3; must lie in the range 
  1. to 1.e+6, and must be less than <span style="font-family: monospace;">"max_dens"</span>.  
  </dd>
  </dl>
  <dl>
  <dt><b>(max_dens = 1.e+6) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(max_dens = 1.e+6) [real]' -->
  <dd>Maximum density for plot, in units of 1/cm^3; must lie in the range 
  100. to 1.e+8, and must exceed <span style="font-family: monospace;">"min_dens"</span>.  
  </dd>
  </dl>
  <dl>
  <dt><b>(min_temp = 5000.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(min_temp = 5000.) [real]' -->
  <dd>Minimum temperature for plot, in units of Kelvins; must lie in the 
  range 1000. to 30,000 K, and must be less than <span style="font-family: monospace;">"max_temp"</span>.  
  </dd>
  </dl>
  <dl>
  <dt><b>(max_temp = 2.0e+4) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(max_temp = 2.0e+4) [real]' -->
  <dd>Maximum temperature for plot, in units of Kelvins; must lie in the 
  range 10,000. to 100,000 K, and must exceed <span style="font-family: monospace;">"min_temp"</span>.  
  </dd>
  </dl>
  <dl>
  <dt><b>(log_ne = yes) [boolean] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(log_ne = yes) [boolean] ' -->
  <dd>Plot the electron density (X-axis) with a log scale? 
  </dd>
  </dl>
  <dl>
  <dt><b>(log_te = no) [boolean] </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(log_te = no) [boolean] ' -->
  <dd>Plot the electron temperature (Y-axis) with a log scale? 
  </dd>
  </dl>
  <dl>
  <dt><b>(resolution = 201) [int]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(resolution = 201) [int]' -->
  <dd>Max number of data points to plot per curve.  Increasing this 
  number improves the fidelity of the curve, at the expense of 
  execution time.  
  </dd>
  </dl>
  <dl>
  <dt><b>(fluxcols = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(fluxcols = "") [pset]' -->
  <dd>Parameter set to specify column names for certain line fluxes, 
  the nebula name and the region code (which must both be present) 
  in the input table.  Otherwise, no error is generated if a 
  named column does not exist in the input table; rather, the 
  calculation proceeds as if the associated line flux is INDEF.
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
  <dl>
  <dt><b>(device = stdgraph) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(device = stdgraph) [string]' -->
  <dd>Output device for plot. 
  </dd>
  </dl>
  <dl>
  <dt><b>(at_data = at_data) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(at_data = at_data) [string]' -->
  <dd>Atomic reference data directory name.  
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Plot the range of electron densities and temperatures that 
  are consistent with the diagnostic ratios found in the example 
  input table for the object <span style="font-family: monospace;">"Test_123"</span>. Adjust the density 
  limits to 500 &lt; N_e &lt; 1.e4. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tcopy nebular$data/flux.fits .
  cl&gt; ntplot flux.tab object=Test_123 min_dens=500. max_dens=1.e4
  </pre></div>
  <p>
  2. Plot curves in the N_e, T_e plane that are consistent with the 
  diagnostic ratios found in the table nebula.tab, and store the 
  results in the table curves.tab.  Adjust the default plot limits to 
  100 &lt; N_e &lt; 1.e+6/cm^3 and 5000 &lt; T_e &lt; 30,000 K. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ntplot nebula.tab outtab=curves.tab min_dens=100. \
  &gt;&gt;&gt; max_temp=3.e+4
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  The 5-level atom program, upon which this package is based, was 
  originally written by M.M. DeRobertis, R. Dufour, and R. Hunt.  
  This package was written by R.A. Shaw (STScI); a description was 
  published by R.A. Shaw &amp; R.J. Dufour (1994).  Type <span style="font-family: monospace;">"help nlevel"</span> 
  for additional information about the N-level atom approximation, 
  and for references to the atomic parameters and the other 
  literature references.  Support for this software development was 
  provided by the Astrophysics Data Program through NASA grant 
  NAG5-1432, and through STScI internal research funds.  
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  nlevel, temden, zones 
  </p>
  <p>
  For general information about this package, type <span style="font-family: monospace;">"help nebular 
  opt=sysdoc"</span>.  
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

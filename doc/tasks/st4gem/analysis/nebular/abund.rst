.. _abund:

abund: Derive ionic abundances relative to H+ in 3-zone nebula
==============================================================

**Package: nebular**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  abund fluxtab diagtab 
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task computes abundances in a nebular gas for several ions, 
  given the electron temperatures (T_e) and densities (N_e) in three 
  zones of low- medium- and high-ionization, and given the H-beta and 
  ionic emission line fluxes.  The abundances for each available ion 
  are calculated within the 5-level atom approximation.  (For more 
  details about this approximation, type <span style="font-family: monospace;">"help nlevel"</span>.)  The user can 
  specify a constant T_e and N_e for all calculations, or the T_e and 
  N_e for each zone can be taken from the input table; these 
  diagnostics can be calculated easily with the `zones' task.  
  </p>
  <p>
  The user specifies the names of an input table of emission line 
  fluxes, and a table of electron temperatures and densities for each 
  of three zones; the latter table will also serve as output for the 
  results.  If the two input table names are the same, then the all 
  of the input columns are assumed to come from one table.  The input 
  tables may contain line fluxes for many nebulae and/or many regions 
  within nebulae, one object/region per row.  The flux for each 
  emission line must be given in separate columns.  The task locates 
  particular emission line fluxes and temeratures/densities via names 
  of specific columns in the input table(s).  These columns have 
  suggestive default names, but are entirely user-definable; see the 
  <span style="font-family: monospace;">"help"</span> file for the `fluxcols' and `diagcols' psets.  NOTE: the 
  target name, region name, and the H-beta flux are required for 
  all nebulae, and columns with that information must exist in the 
  input table.  
  </p>
  <p>
  The emission line fluxes are derived from the input line fluxes, 
  corrected for interstellar reddening.  The reddening corrected line 
  flux <span style="font-family: monospace;">"I"</span> is derived from the input line flux <span style="font-family: monospace;">"F"</span> by: 
  </p>
  <div class="highlight-default-notranslate"><pre>
  I(line) = F(line) * dex {-c * f(lambda)}
  </pre></div>
  <p>
  where <span style="font-family: monospace;">"c"</span> is the extinction constant (i.e. the logarithmic 
  extinction at H-beta, 4861 Ang), and <span style="font-family: monospace;">"f(lambda)"</span> is derived from 
  one of a few possible extinction functions.  The choices for 
  Galactic extinction are: Savage &amp; Mathis (1979), Cardelli, Clayton, 
  &amp; Mathis (1989), and the function of Kaler (1976) which is based 
  on Whitford (1958).  The choices for extra-Galactic extinction laws 
  are Howarth (1983) for the LMC, and Prevot et al. (1984) for the 
  SMC.  The value of <span style="font-family: monospace;">"c"</span> must be given in the input table if a 
  correction for reddening is desired.  However, the correction may 
  be disabled if a correction flag (stored in another table column), 
  is set to <span style="font-family: monospace;">"yes"</span>.  By default no reddening correction is performed 
  unless a valid value for <span style="font-family: monospace;">"c"</span> is available, and unless the 
  correction flag is set to <span style="font-family: monospace;">"no"</span> or is not present.  The extinction 
  law will default to that of Savage &amp; Mathis (<span style="font-family: monospace;">"gal"</span>) unless another 
  choice is specified (one of <span style="font-family: monospace;">"gal"</span>, <span style="font-family: monospace;">"ccm"</span>, <span style="font-family: monospace;">"jbk"</span>, <span style="font-family: monospace;">"lmc"</span>, or <span style="font-family: monospace;">"smc"</span>) 
  in the input table.  
  </p>
  <p>
  The available ions, the emission line fluxes used, and the nebular 
  ionization zone to which that ion is attributed, are listed below.  
  Note that the calculated ionic abundance is the average of that 
  derived from each of the emission lines for that ion.  The emission 
  lines used for each ion are listed by wavelength in Angstroms.  It 
  is often the case that some emission lines are unresolved at 
  typical spectral resolutions.  This circumstance is accomodated to 
  some degree by specifying some fluxes as sums from closely spaced 
  line pairs, which are denoted in the table below with a <span style="font-family: monospace;">"+"</span> sign 
  between the two affected wavelengths.  
  </p>
  <div class="highlight-default-notranslate"><pre>
  
             Line Fluxes Often Used for Ionic Abundances
  
                                               Ionization
        Ion    Spectrum    Lines Used             Zone
      ----------------------------------------------------
        C(0)    [C i]      9823 9849               Low
        C(+1)    C ii]     2326+28                 Low
        C(+2)    C iii]    1907+09                 Med
  
        N(0)    [N i]      5198+5200               Low
        N(+1)   [N ii]     5755, 6548, 6583        Low
        N(+2)    N iii]    1749+52                 Med
        N(+2)   [N iv]     1483+1487               Med
  
        O(0)    [O i]      6300, 6363              Low
        O(+1)   [O ii]     3726+29, 7320+30        Low
        O(+2)   [O iii]    4363, 4959, 5007        Med
        O(+3)   [O iv]     1400+01+05+07           High
        O(+4)   [O v]      1214+1218               High
  
       Ne(+2)  [Ne iii]    3342, 3869, 3968        Med
       Ne(+3)  [Ne iv]     2423+25, 4724+25        High
       Ne(+4)  [Ne v]      2975, 3426, 3346        High
  
       Na(+3)  [Na iv]     2805, 3242, 3362        Med
       Na(+5)  [Na vi]     2569, 2871, 2970        High
  
       Mg(+4)  [Mg v]      2418, 2783, 2928        High
       Mg(+6)  [Mg vii]    2262, 2506, 2626        High
  
       Al(+1)  [Al ii]     1671, 2661+2670         Low
  
       Si(+1)  [Si ii]     2335+45+51              Low
       Si(+2)   Si iii]    1206, 1883+92           Low
  
        S(+1)   [S ii]     4068+76, 6716+31        Low
        S(+2)   [S iii]    6312, 9069, 9532        Med
        S(+3)   [S iv]     1405+1406+1417          High
  
       Cl(+1)  [Cl ii]     3679, 5807, 9383        Low
       Cl(+2)  [Cl iii]    3348, 5517+37           Med
       Cl(+3)  [Cl iv]     5323, 7531, 8045        Med
  
       Ar(+2)  [Ar iii]    5192, 7136, 7751        Med
       Ar(+3)  [Ar iv]     2854+68, 4711, 4740,
                           7170                    Med
       Ar(+4)  [Ar v]      4626, 6435, 7006        High
  
        K(+3)   [K iv]     4511, 6102, 6796        High
        K(+4)   [K v]      2495, 2515, 4123, 4163  High
  
       Ca(+4)  [Ca v]      3996, 5309, 6087        High
  ---------------------------------------------------------
  </pre></div>
  <p>
  If a particular emission line flux is unavailable (e.g. the 
  relevant line fluxes are INDEF, or the column name for that line 
  flux is not found), that emission line is excluded from the 
  calculations.  If more than one emission line is available for a 
  given ion, the task will compute a weighted average of the ionic 
  abundance as determined for each of the input line fluxes; the 
  weighting is approximately proportional to the relative line 
  strengths.  
  </p>
  <p>
  The electron temperature and density is taken from the task 
  parameters <span style="font-family: monospace;">"t_e"</span> and <span style="font-family: monospace;">"n_e"</span> if the parameter <span style="font-family: monospace;">"constant=yes"</span>.  In 
  this case the T_e and N_e are assumed to be constant throughout the 
  nebula.  Alternatively, the electron temperature and density may be 
  specified for each of three zones, in which case T_e and N_e are 
  taken from the <span style="font-family: monospace;">"diagtab"</span> table from the columns named <span style="font-family: monospace;">"Te_Low"</span>, 
  <span style="font-family: monospace;">"Ne_Low"</span>, etc.  The column names can match the output of the 
  `zones' task, if desired.  If there is no valid T_e or N_e for a 
  given zone, values are taken from the next-lowest ionization zone.  
  It is therefore essential that a valid T_e and N_e exist for the 
  low-ionization zone.  
  </p>
  <p>
  The output is to the <span style="font-family: monospace;">"diagtab"</span> table; the abundance for each ion is 
  written to a separate column with names like, e.g. <span style="font-family: monospace;">"Ni_(Si^+2)"</span> for 
  twice-ionized Silicon.  The units are per unit ionized Hydrogen.  
  The ionic abundances for each nebula/region are placed in separate 
  rows.  
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [string]' -->
  <dd>Input table of emission line fluxes.  The line fluxes for 
  different ions are stored in separate columns, and measurements 
  for different objects are stored in separate rows.  
  </dd>
  </dl>
  <dl id="l_diagtab">
  <dt><b>diagtab [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='diagtab' Line='diagtab [string]' -->
  <dd>Input table of electron temperatures and densities for each 
  nebular zone.  The T_e and N_e for each zone are stored in 
  separate columns, and measurements for different objects are 
  stored in separate rows.  If the same as <span style="font-family: monospace;">"fluxtab"</span>, all input 
  will be taken from one table.  This table also serves as the 
  output for the ionic abundances for each object/region.  
  </dd>
  </dl>
  <dl>
  <dt><b>(diagcols = <span style="font-family: monospace;">""</span>) [pset]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(diagcols = "") [pset]' -->
  <dd>Parameter set to specify column names for electron temperatures 
  and densities for each nebular zone.  No error is generated if a 
  at least one T_e and one N_e column exists in the input table; 
  rather, the calculation proceeds with fewer zones.  
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
  <dt><b>(constant = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(constant = no) [boolean]' -->
  <dd>Assume a constant T_e and N_e for the whole nebula?  If set, the 
  values will be obtained from the <span style="font-family: monospace;">"t_e"</span> and <span style="font-family: monospace;">"n_e"</span> task parameters.  
  </dd>
  </dl>
  <dl>
  <dt><b>(t_e = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(t_e = INDEF) [real]' -->
  <dd>If <span style="font-family: monospace;">"constant=yes"</span>, T_e is assumed to have this constant value 
  throughout the nebula, and diagnostics from the input table will 
  be ignored.  
  </dd>
  </dl>
  <dl>
  <dt><b>(n_e = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(n_e = INDEF) [real]' -->
  <dd>If <span style="font-family: monospace;">"constant=yes"</span>, N_e is assumed to have this constant value 
  throughout the nebula, and diagnostics from the input table will 
  be ignored.  
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
  To see how STSDAS binary Tables are used for this task, copy these 
  example files to your IRAF current directory:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; copy nebular$data/flux.dat .
  cl&gt; copy nebular$data/flux.cols .
  cl&gt; tcreate flux.tab flux.cols flux.dat
  </pre></div>
  <p>
  (Type <span style="font-family: monospace;">"help tcreate"</span> for more information about making binary 
  tables from ascii files.)  You now have a test binary table called 
  <span style="font-family: monospace;">"flux.tab"</span> in your current directory which can be used as input for 
  the `zones' task. 
  </p>
  <p>
  1. Find the electron temperature and density, and then the ionic 
  abundances in each of three zones from various diagnostic line 
  fluxes for all objects in the table <span style="font-family: monospace;">"flux.tab"</span>.  The input/output 
  table <span style="font-family: monospace;">"abund.tab"</span> contain columns listing T_e and N_e for each 
  zone. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; zones flux.tab abund.tab objects="*"
  cl&gt; abund flux.tab abund.tab
  </pre></div>
  <p>
  You may wish to review &amp; edit the adopted N_e and/or T_e with 
  `tedit' after running `zones', but before running `abund'.  You may 
  then view the output table with `tread', or produce a printable 
  ASCII file with, e.g.:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tprint abund.tab &gt; abund.ascii
  </pre></div>
  <p>
  2. Find the ionic abundances from various diagnostic line fluxes 
  for objects in the table <span style="font-family: monospace;">"flux.tab"</span>, assuming a constant T_e = 
  14,000 K, and N_e = 1500/cm^3 applies throughout the nebula.  Store 
  the results in new columns in the table <span style="font-family: monospace;">"abund.tab"</span>.  
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; abund flux.tab abund.tab const+ t_e=14000. n_e=1500.
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
  diagcols, nlevel, fluxcols, ionic, temden, zones
  </p>
  <p>
  For general information about tasks in the `nebular' package, type 
  <span style="font-family: monospace;">"help nebular opt=sysdoc"</span>.  
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

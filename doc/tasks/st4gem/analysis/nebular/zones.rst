.. _zones:

zones: Determine electron temps & densities in 3-zone nebula
============================================================

**Package: nebular**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  zones fluxtab outtab
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task computes the electron temperatures (T_e) and densities 
  (N_e) of an ionized nebular gas in separate zones of low- medium- 
  and high-ionization from a variety of diagnostic emission line 
  fluxes.  The diagnostics for each available ion are calculated 
  within the N-level atom approximation.  (For more details about 
  this approximation, type <span style="font-family: monospace;">"help nlevel"</span>.)  The output from this task 
  can be used to compute the ionic abundances for all available ions 
  with the `abund' task.  The point of having two separate tasks is 
  to permit the user to inspect and evaluate the results from `zones' 
  before proceding with the abundance calculations.  
  </p>
  <p>
  The user specifies the names of an input table of emission line 
  fluxes, and an output table for the results.  If these names are 
  identical, then new columns will be added (if necessary) to the 
  input table to contain the calculated densitites and temperatures.  
  The input table may contain line fluxes for many nebulae and/or 
  many regions within nebulae, one object/region per row.  The flux 
  for each emission line or line ratio must be given in separate 
  columns.  The task locates particular emission line fluxes via 
  names of specific columns in the input table.  These columns have 
  suggestive default names, but are entirely user-definable; type 
  <span style="font-family: monospace;">"help fluxcols"</span> for more details.  Note that the input table need 
  not actually contain all the diagnostic lines specified in this 
  p-set: if a named column is not found, the corresponding 
  calculation may be skipped.  HOWEVER, the target name and region 
  name ARE required for all nebulae, and columns with that information 
  must exist in the input table.  
  </p>
  <p>
  The diagnostic line ratios are derived from the input line fluxes, 
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
  The available diagnostic line ratios, the ionization potential of 
  the associated ion, and the nebular ionization zone to which they 
  are attributed, are listed by ion below.  The line ratio is in the 
  form I(wave1)/I(wave2), where <span style="font-family: monospace;">"wave1"</span> and <span style="font-family: monospace;">"wave2"</span> are in units of 
  Angstroms; ratios involving sums of line strengths are given as 
  I(wave1+wave2)/I(wave3+wave4).  
  </p>
  <div class="highlight-default-notranslate"><pre>
  Electron density diagnostics:
  
        Ion           Line Ratio             I.P.   Zone
      ---------------------------------------------------
        C iii]       I(1907) / I(1909)       47.9   Med
       [O ii]        I(3726) / I(3729)       13.6   Low
      [Ne iv]        I(2423) / I(2425)       63.5   High
       [S ii]        I(6716) / I(6731)       10.4   Low
      [Cl iii]       I(5517) / I(5537)       23.8   Med
      [Ar iv]        I(4711) / I(4740)       40.9   Med
      ---------------------------------------------------
  
  Electron temperature diagnostics:
  
        Ion           Line Ratio             I.P.   Zone
      ---------------------------------------------------
       [N ii]   I(6548+6583) / I(5755)       14.5   Low
       [O ii]   I(3726+3729) / I(7320+7330)  13.6   Low
       [O iii]  I(4959+5007) / I(4363)       35.1   Med
      [Ne iii]  I(3869+3969) / I(3342)       41.1   Med
      [Ne v]    I(3426+3346) / I(2975)       97.0   High
       [S ii]   I(6716+6731) / I(4068+4076)  10.4   Low
       [S iii]  I(9069+9532) / I(6312)       23.4   Med
      [Ar iii]  I(7136+7751) / I(5192)       27.6   Med
      [Ar v]    I(6435+7006) / I(4626)       59.8   High
      ---------------------------------------------------
  </pre></div>
  <p>
  These are only the most commonly used ratios, and do NOT include 
  all of the diagnostics available in the `temden' task.  
  </p>
  </section>
  <section id="s_algorithm">
  <h3>Algorithm</h3>
  <p>
  The method of computing T_e given N_e (or N_e given T_e) for given 
  diagnostic line ratio is described in the on-line help for <span style="font-family: monospace;">"nlevel"</span>, 
  and in the references given below.  This task makes use of an 
  iterative technique to derive both the temperature AND the density 
  within each of three zones by using simultaneous use of temperature- 
  and density-sensitive line ratios from different ions with similar 
  ionization potentials.  The procedure is as follows:
  </p>
  <dl id="l_ZONE">
  <dt><b>ZONE 1:</b></dt>
  <!-- Sec='ALGORITHM' Level=0 Label='ZONE' Line='ZONE 1:' -->
  <dd><dl>
  <dt><b>a)</b></dt>
  <!-- Sec='ALGORITHM' Level=1 Label='a' Line='a)' -->
  <dd>Assume N_e = 1000/cm^3 and calculate T_e from the [N ii] and 
  [O iii] ratios.  
  </dd>
  </dl>
  <dl>
  <dt><b>b)</b></dt>
  <!-- Sec='ALGORITHM' Level=1 Label='b' Line='b)' -->
  <dd>Average these two temperatures (or assume T_e = 10,000 K if 
  unavailable) and calculate N_e from the [O ii] and [S ii] 
  ratios.  
  </dd>
  </dl>
  <dl>
  <dt><b>c)</b></dt>
  <!-- Sec='ALGORITHM' Level=1 Label='c' Line='c)' -->
  <dd>Average these two densities (or assume N_e = 1000/cm^3 if 
  unavailable) and re-calculate T_e from the [N ii] ratio.  
  (If the [N ii] ratio is unavailable, default back to the 
  [O iii] ratio.)  
  </dd>
  </dl>
  <dl>
  <dt><b>d)</b></dt>
  <!-- Sec='ALGORITHM' Level=1 Label='d' Line='d)' -->
  <dd>Re-calculate N_e from [O ii] and [S ii], and use the average 
  to calculate T_e from the [O ii] and [S ii] ratios.  
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_ZONE">
  <dt><b>ZONE 2:</b></dt>
  <!-- Sec='ALGORITHM' Level=0 Label='ZONE' Line='ZONE 2:' -->
  <dd><dl>
  <dt><b>a)</b></dt>
  <!-- Sec='ALGORITHM' Level=1 Label='a' Line='a)' -->
  <dd>Assume N_e = 1000/cm^3 and calculate T_e from the [O iii] 
  ratio; if not, assume T_e = 10,000 K.  
  </dd>
  </dl>
  <dl>
  <dt><b>b)</b></dt>
  <!-- Sec='ALGORITHM' Level=1 Label='b' Line='b)' -->
  <dd>Use this approximate temperature to calculate N_e from [Ar iv], 
  [Cl iii], and C iii].  
  </dd>
  </dl>
  <dl>
  <dt><b>c)</b></dt>
  <!-- Sec='ALGORITHM' Level=1 Label='c' Line='c)' -->
  <dd>Now use the average N_e from [Ar iv], [Cl iii], and C iii] (if 
  available, use N_e = 1000 if not) to calculate T_e from [O iii], 
  [Ne iii], [Ar iii], [S iii], and [Ar iv].  
  </dd>
  </dl>
  <dl>
  <dt><b>d)</b></dt>
  <!-- Sec='ALGORITHM' Level=1 Label='d' Line='d)' -->
  <dd>Now use the average T_e (if available, use T_e = 10,000 if 
  not) to re-calculate N_e from [Ar iv], [Cl iii], and C iii].  
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_ZONE">
  <dt><b>ZONE 3:</b></dt>
  <!-- Sec='ALGORITHM' Level=0 Label='ZONE' Line='ZONE 3:' -->
  <dd><dl>
  <dt><b>a)</b></dt>
  <!-- Sec='ALGORITHM' Level=1 Label='a' Line='a)' -->
  <dd>Assume T_e = T_[O iii] (calculated in zone 2) if available, 
  or 10,000 K if not.  
  </dd>
  </dl>
  <dl>
  <dt><b>b)</b></dt>
  <!-- Sec='ALGORITHM' Level=1 Label='b' Line='b)' -->
  <dd>Calculate N_e from the [Ne iv] ratio, if available, otherwise 
  assume N_e = 1000/cm^3.  
  </dd>
  </dl>
  <dl>
  <dt><b>c)</b></dt>
  <!-- Sec='ALGORITHM' Level=1 Label='c' Line='c)' -->
  <dd>Now calculate T_e from the [Ar v] and [Ne v] ratios.  Then 
  recalculate N_e based upon the improved T_e, if either 
  temperature ratio is available.  
  </dd>
  </dl>
  </dd>
  </dl>
  <p>
  The electron temerature and density for all available ions are 
  written to the output table, along with those adopted for each 
  zone.  T_e and N_e for a given zone is the weighted average of the 
  temperatures and densities derived for all ions assigned to that 
  zone.  If a particular temperature/density diagnostic is 
  unavailable (e.g. the relevant line fluxes are INDEF, or the line 
  ratio does not yield a valid result), that temperature/density is 
  excluded from the average for that zone.  If there are no valid 
  diagnostic line fluxes available for a given zone, the result is 
  INDEF.  The weights for each diagnostic are given below; the 
  weights exceed unity when they are clearly more reliable and/or 
  more commonly used.  
  </p>
  <div class="highlight-default-notranslate"><pre>
               Weights for Nebular Diagnostics
  
               |     LOW      |    MEDIUM     |     HIGH
   Diagnostic  |   Ions   Wt  |   Ions    Wt  |   Ions    Wt
  -------------+--------------+---------------+--------------
      N_e      |  [O ii]   1  |  [Cl iii]  2  |  [Ne iv]   1
               |  [S ii]   1  |  [Ar iv]   1  |
               |              |    C iii]  1  |
               |              |               |
      T_e      |  [N ii]   5  |   [O iii]  4  |  [Ar v]    1
               |  [O ii]   1  |  [Ne iii]  2  |  [Ne v]    1
               |  [S ii]   1  |  [Ar iii]  2  |
               |              |   [S iii]  1  |
  </pre></div>
  <p>
  It is possible that one or more ratios may not be useful for a 
  given nebula if the actual T_e or N_e lies outside the range of 
  that diagnostic.  Therefore, the derived T_e and N_e for all 
  diagnostic ratios are written to the output table, along with the 
  average values for each zone.  Thus, the user can review the 
  results (e.g., using `tedit') to exclude suspicious values before 
  using `abund' to calculate the ionic abundances.  
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_fluxtab">
  <dt><b>fluxtab [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fluxtab' Line='fluxtab [string]' -->
  <dd>Input table of emission line fluxes.  The line fluxes for different 
  ions are stored in separate columns, and measurements for different 
  objects are stored in separate rows.  
  </dd>
  </dl>
  <dl id="l_outtab">
  <dt><b>outtab [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtab' Line='outtab [string]' -->
  <dd>Output table of electron temperature and density for each of 
  three zones.  If the same as input table, new columns will be 
  appended if necessary.  
  </dd>
  </dl>
  <dl>
  <dt><b>(objects = <span style="font-family: monospace;">"*"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(objects = "*") [string]' -->
  <dd>List of object names in input table for which to compute 
  temperatures and densities.  Separate object names by whitespace 
  or commas.  Specifying <span style="font-family: monospace;">"*"</span> will select all objects in the 
  input table.  
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
  <dt><b>(at_data = at_data) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(at_data = at_data) [string]' -->
  <dd>Atomic reference data directory name.  
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  To see how STSDAS binary Tables are used for this task, copy the 
  example files to your IRAF current directory and run `tcreate':
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
  1. Find the electron temperatures/densities from various diagnostic 
  line ratios for the object <span style="font-family: monospace;">"TEST_123"</span> in the table <span style="font-family: monospace;">"flux.tab"</span>, and 
  put the output in the table <span style="font-family: monospace;">"diag.tab"</span>.  
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; zones flux.tab diag.tab objects="TEST_123"
  </pre></div>
  <p>
  You may wish to review &amp; edit the adopted N_e and/or T_e with 
  `tedit' after running `zones', but before running `abund'.  You may 
  view the output table with `tread', or produce a printable ASCII 
  file with, e.g.:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; tprint diag.tab &gt; diag.ascii
  </pre></div>
  <p>
  2. Find the electron temperatures/densities from various diagnostic 
  line ratios for all objects in the table <span style="font-family: monospace;">"flux.tab"</span>.  Obtain the 
  extinction constant from the input column called <span style="font-family: monospace;">"c_ext"</span>.  Store 
  the results in new columns in the input table.  
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; zones flux.tab flux.tab objects="*" c_ext_col="c_ext"
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
  nlevel, fluxcols, ionic, temden 
  </p>
  <p>
  For general information about the `nebular' package, type <span style="font-family: monospace;">"help 
  nebular opt=sysdoc"</span>.  
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'DESCRIPTION' 'ALGORITHM' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

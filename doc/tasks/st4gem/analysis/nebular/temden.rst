.. _temden:

temden: Determine electron temperature or density from diagnostic ratio
=======================================================================

**Package: nebular**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  temden option ratio
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task computes the electron temperature (T_e) given an electron 
  density (N_e), or N_e given T_e, of an ionized nebular gas within 
  the N-level atom approximation.  The user specifies the quantity to 
  be calculated, the reddening-corrected diagnostic line ratio, the 
  name and the spectrum of the atom, and an assumed value for the 
  quantity NOT being calculated.  The task output lists the ion and 
  the line ratio for which the calculation is performed, followed by 
  the result of the calculation.  These input task parameters, 
  including those that are <span style="font-family: monospace;">"hidden"</span>, are written back to the parameter
  file.  The result is also stored in the task parameter <span style="font-family: monospace;">"result"</span> for 
  ease of use in CL scripts.  
  </p>
  <p>
  The following table lists the default diagnostic line ratios in the 
  form I(wave1)/I(wave2), where <span style="font-family: monospace;">"wave1"</span> and <span style="font-family: monospace;">"wave2"</span> are given in 
  units of Angstroms. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  Table 1. Electron density diagnostics:
  
    Ion             Line Ratio
  -------------------------------------
    C ii]        I(2326) / I(2328)
    C iii]       I(1907) / I(1909)
   [N i]         I(5198) / I(5200)
    N iii]       I(1749) / I(1752)
    N iv]        I(1483) / I(1487)
   [O ii]        I(3726) / I(3729)
   [O iv]        I(1401) / I(1405)
   [O v]         I(1214) / I(1218)
  [Ne iv]        I(2423) / I(2425)
  [Al ii]        I(2661) / I(2670)
  [Si ii]        I(2335) / I(2345)
   Si iii]       I(1883) / I(1892)
   [S ii]        I(6716) / I(6731)
   [S iv]        I(1406) / I(1417)
  [Cl iii]       I(5517) / I(5537)
  [Ar iv]        I(4711) / I(4740)
   [K v]         I(6223) / I(6349)
  
  Table 2. Electron temperature diagnostics:
  
    Ion             Line Ratio
  -------------------------------------
   [C i]    I(9823+9849) / I(8728)
   [N i]    I(5198+5200) / I(10397+10407)
   [N ii]   I(6548+6583) / I(5755)
   [O i]    I(6300+6363) / I(5577)
   [O ii]   I(3726+3729) / I(7320+7330)
   [O iii]  I(4959+5007) / I(4363)
  [Ne iii]  I(3869+3969) / I(3342)
  [Ne iv]   I(2422+2425) / I(1601+1602)
  [Ne v]    I(3426+3346) / I(2975)
  [Na iv]   I(3242+3362) / I(2805)
  [Na vi]   I(2871+2970) / I(2569)
  [Mg v]    I(2783+2928) / I(2418)
  [Mg vii]  I(2506+2626) / I(2262)
  [Al ii]   I(2661+2670) / I(1671)
   Si iii]  I(1883+1892) / I(1206)
   [S ii]   I(6716+6731) / I(4068+4076)
   [S iii]  I(9069+9532) / I(6312)
  [Cl iii]  I(5517+5537) / I(3353+3343)
  [Cl iv]   I(7530+8045) / I(5323)
  [Ar iii]  I(7136+7751) / I(5192)
  [Ar iv]   I(4711+4740) / I(2854+2868)
  [Ar v]    I(6435+7006) / I(4626)
   [K iv]   I(6102+6796) / I(4511)
   [K v]    I(4123+4163) / I(2515+2495)
  [Ca v]    I(5309+6087) / I(3996)
  </pre></div>
  <p>
  It is possible to customize the line ratio using the <span style="font-family: monospace;">"transition"</span> 
  parameter and an expression for the ratio of interest. See the 
  description of the <span style="font-family: monospace;">"transition"</span> parameter and the examples below. 
  Note that the wavelengths corresponding to the various transitions 
  can be obtained by running the <span style="font-family: monospace;">"ionic"</span> task. 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_option">
  <dt><b>option <span style="font-family: monospace;">"density"</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='option' Line='option "density" [string]' -->
  <dd>Quantity to calculate: <span style="font-family: monospace;">"temperature"</span> or <span style="font-family: monospace;">"density"</span>.
  </dd>
  </dl>
  <dl id="l_flxratio">
  <dt><b>flxratio = <span style="font-family: monospace;">""</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flxratio' Line='flxratio = "" [string]' -->
  <dd>Algebraic expression for the ratio of diagnostic line fluxes.  The 
  expression is evaluated with FORTRAN-like rules for supported 
  operators and the order of their evaluation.  
  </dd>
  </dl>
  <dl>
  <dt><b>(atom = <span style="font-family: monospace;">"oxygen"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(atom = "oxygen") [string]' -->
  <dd>Name of the atom, which is one of: carbon, nitrogen, oxygen, 
  neon, sodium, magnesium, aluminum, silicon, sulfur, chlorine, 
  argon, potassium, or calcium. 
  </dd>
  </dl>
  <dl>
  <dt><b>(spectrum = 2) [int]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(spectrum = 2) [int]' -->
  <dd>Spectrum number of the atom, e.g. <span style="font-family: monospace;">"3"</span> for [O iii], <span style="font-family: monospace;">"2"</span> for [S ii], 
  etc.  Must lie in the range 1 &lt;= ion_stage &lt;= 8.  
  </dd>
  </dl>
  <dl>
  <dt><b>(transition = <span style="font-family: monospace;">"default"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(transition = "default") [string]' -->
  <dd>Expression for the transition, if not the <span style="font-family: monospace;">"default"</span>. Transitions
  are specified with the special function <span style="font-family: monospace;">"J"</span> (for the emissivity): 
  the arguments are the upper and lower levels of the transition. For 
  example, the traditional density diagnostic of [O II] is the ratio 
  of the intensities for the transition I(3-&gt;1) to that of 
  I(2-&gt;1)--i.e., I(3726)/I(3729). The corresponding expression for 
  would be <span style="font-family: monospace;">"J(3,1)/J(2,1)"</span>. The expression is evaluated with 
  FORTRAN-like expression rules.
  </dd>
  </dl>
  <dl>
  <dt><b>(assume = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(assume = INDEF) [real]' -->
  <dd>Value to assume for the quantity NOT being calculated.  The units 
  are 1/cm^3 if T_e is being calculated, or Kelvins if N_e is being 
  calculated.  Temperatures must lie in the range 500 to 1.e+5 K, 
  and densities must lie in the range 1. to 1.e+8.  
  </dd>
  </dl>
  <dl>
  <dt><b>(result = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(result = INDEF) [real]' -->
  <dd>Result of the calculation.  The units are 1/cm^3 if N_e is being 
  calculated, or Kelvins if T_e is being calculated.  
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = no) [boolean]' -->
  <dd>Print verbose output for each iteration?  
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
  1. Find the electron density from the [S II] diagnostic ratio 
  I(6716)/I(6731) = 0.9 assuming an electron temerature of 10000 K.  
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; temden density 0.9 atom=sulfur spectrum=2 assume=10000.
  Density ratio [S ii]: I(6716)/I(6731) =   0.9
  Density: 910.344 /cm^3
  </pre></div>
  <p>
  2. Find the electron temperature from the [O III] diagnostic ratio 
  I(4959+5007)/I(4363), given I(4959)=100., I(5007)=288., and 
  I(4363)=7.405, and  assuming an electron density of 1000/cm^3. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; temden temerature "(100.+288.)/7.40" atom=oxygen \
  &gt;&gt;&gt; spec=3 assume=1000.
  Temperature ratio [O iii]: I(4959+5007)/I(4363) = 52.432
  Temperature: 17158.3 K
  </pre></div>
  <p>
  3. Find the electron temperature from the custom [O III] 
  diagnostic ratio I(1660+1666)/I(4363)=1.0, and assuming an 
  electron density of 10,000/cm^3. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; temden temerature 1.0 atom=oxygen spec=3 assume=1.e4 \
  &gt;&gt;&gt; transition="(j(6,2)+j(6,3))/j(5,4)"
  Temperature ratio [O iii]: (J(6,2)+J(6,3))/J(5,4) = 1.
  Temperature: 17158.3 K
  </pre></div>
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
  nlevel, ionic, zones 
  </p>
  <p>
  For further information type <span style="font-family: monospace;">"help nebular opt=sysdoc"</span>.  
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

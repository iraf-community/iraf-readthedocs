.. _ionic:

ionic: Determine ionic abundance relative to H+
===============================================

**Package: nebular**

.. raw:: html

  <section id="s_usage_">
  <h3>Usage	</h3>
  <p>
  ionic atom spectrum
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task computes atomic energy-level populations, critical 
  densities, and line emissivities for a nebular (i.e., low density) 
  gas, within the N-level atom approximation, given the electron 
  temperature (T_e) and density (N_e).  The user specifies the name 
  and the spectrum of the atom, the assumed values for T_e and 
  N_e, and (optionally) the wavelength and relative flux of a 
  particular emission line (or range of lines) of interest.  The task 
  output lists the level populations, critical densities, line 
  emissivities, and optionally the ionic abundance relative to 
  ionized hydrogen.  
  </p>
  <p>
  The critical density for a level <span style="font-family: monospace;">"i"</span> is defined as the density at 
  which the collisional de-excitation rate balances the radiative 
  transition rate:
  </p>
  <div class="highlight-default-notranslate"><pre>
                ___
                \    A
                /__   ij
                j&lt;i
  N_crit(i) =  ----------
                ___
                \   q
                /__  ij
                j!=i
  </pre></div>
  <p>
  In the low density limit the emissivity is proportional to the 
  product N_e * N_ion, whereas for densities exceeding the critical 
  density, the emissivity is proportional to N_ion.  Thus, line 
  emission in a nebula occurs most efficiently near the critical 
  density.  
  </p>
  <p>
  Note that the output line emissivities are per unit ion density per 
  unit electron density.  That is, true volume emissivity is related 
  to the output emissivities by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  4 * pi * j(true) = N_e * N_ion * j(output)
  </pre></div>
  <p>
  The emissivities are listed by atomic transition, as are the 
  calculated wavelengths.  If the wavelength of a particular line 
  of interest and the observed line flux are also provided, the 
  task will compute the ionic abundance, relative to ionized 
  hydrogen, as: 
  </p>
  <div class="highlight-default-notranslate"><pre>
  N(X_i)    I(line)    j(H-beta)
  ------ = --------- * ---------
  N(H+)    I(H-beta)    j(lines)
  </pre></div>
  <p>
  In this case the calculated wavelength is really the sum of all 
  lines lying within a specified range of the wavelength of interest; 
  that range is specified with the <span style="font-family: monospace;">"wv_toler"</span> parameter. The H-beta 
  emissivity is derived from a formula by Aller (1984):
  </p>
  <div class="highlight-default-notranslate"><pre>
  4 * PI * j(H-beta) = 1.387E-25 * N_e N_(H+) * T_4 ^(-0.983)
                            * dex (-0.0424/T_4),   erg/s/cm^3
  </pre></div>
  <p>
  Where T_4 = T_e / 10^4 K.  This formula is accurate to within 4% 
  for densities less than 10^6.  The result of the abundance 
  calculation is stored in the task parameter <span style="font-family: monospace;">"result"</span> for ease of 
  use in CL scripts.  
  </p>
  <p>
  The available combinations of atoms and spectra are listed below:  
  </p>
  <div class="highlight-default-notranslate"><pre>
   C I        C II       C III
   N I        N II       N III     N IV
   O I        O II       O III     O IV    O V
  Ne III     Ne IV      Ne V      Ne VI
  Na IV                 Na VI
  Mg V                  Mg VII
  Al II
  Si II      Si III
   S II       S III      S IV
  Cl II      Cl III     Cl IV
  Ar III     Ar IV      Ar V
   K IV       K V
             Ca V
  </pre></div>
  <p>
  A CAUTION ABOUT THE WAVELENGTHS:  Please note that the wavelengths 
  used throughout these help files are those commonly used in the 
  astronomical literature.  However, the wavelengths used in the 
  program are derived from the published atomic data for each ion.  
  These derived wavelengths are used partly for consistency with the 
  models, and partly because there is as yet no good reference for 
  ALL the wavelengths of all the ions used in these tasks.  But be 
  aware that there are differences with the accepted values (usually 
  around +1 Angstroms).  The wavelength discrepancy is only likely 
  to cause confusion when using the <span style="font-family: monospace;">"ionic"</span> task to compute an ionic 
  abundance from a particular line.  In this case, be sure the 
  <span style="font-family: monospace;">"wave"</span> or <span style="font-family: monospace;">"wv_toler"</span> parameters are set appropriately.  
  </p>
  <p>
  These wavelength discrepancies (in the fourth decimal place) are a 
  reminder of the imperfections inherent in all the models from 
  which the atomic data are derived, although the uncertainties in 
  the cross-sections range from 5% to 50%.  
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_atom">
  <dt><b>atom = <span style="font-family: monospace;">"oxygen"</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='atom' Line='atom = "oxygen" [string]' -->
  <dd>Name of the atom, which is one of: carbon, nitrogen, oxygen, 
  neon, sodium, magnesium, aluminum, silicon, sulfur, chlorine, 
  argon, potassium, or calcium. 
  </dd>
  </dl>
  <dl id="l_spectrum">
  <dt><b>spectrum = 2 [int]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='spectrum' Line='spectrum = 2 [int]' -->
  <dd>Spectrum number of the atom, e.g. <span style="font-family: monospace;">"3"</span> for [O iii], <span style="font-family: monospace;">"2"</span> for [S ii], 
  etc.  Must lie in the range 1 &lt;= spectrum &lt;= 8.  
  </dd>
  </dl>
  <dl>
  <dt><b>(temperature = 10000.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(temperature = 10000.) [real]' -->
  <dd>Assumed nebular electron temperature, in Kelvins.  Must lie in 
  the range 500. &lt;= T_e &lt;= 1.e+5.  (NB: some collision strengths 
  in the literature are only given between 5000 K and 20,000 K, so 
  use caution.)  
  </dd>
  </dl>
  <dl>
  <dt><b>(density = 1000.) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(density = 1000.) [real]' -->
  <dd>Assumed nebular electron density, in units of 1/cm^3.  Must lie 
  in the range 1. &lt;= N_e &lt;= 1.E+8.    
  </dd>
  </dl>
  <dl>
  <dt><b>(wave = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wave = INDEF) [real]' -->
  <dd>Wavelength for a (semi-) forbidden line of interest, in Angstroms.  
  When this and the <span style="font-family: monospace;">"flxratio"</span> parameter are specified, the ionic 
  abundance relative to ionized hydrogen is calculated and stored in 
  the <span style="font-family: monospace;">"result"</span> parameter.  
  </dd>
  </dl>
  <dl>
  <dt><b>(wv_toler = 1.0) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(wv_toler = 1.0) [real]' -->
  <dd>Tolerance for <span style="font-family: monospace;">"wave"</span> parameter: all emission lines with wavelengths 
  within <span style="font-family: monospace;">"wv_toler"</span> of <span style="font-family: monospace;">"wave"</span> will be included in the abundance 
  calculation when both <span style="font-family: monospace;">"wave"</span> and <span style="font-family: monospace;">"flxratio"</span> are specified.  This 
  parameter can be used to calculate an accurate abundance even when 
  the observed line flux is really a blend of two or more closely 
  spaced lines.  If the tolerance is zero, the <span style="font-family: monospace;">"wave"</span> parameter must 
  match the calculated wavelength exactly, or the calculated 
  abundance will be given as zero.  
  </dd>
  </dl>
  <dl>
  <dt><b>(flxratio = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(flxratio = INDEF) [real]' -->
  <dd>Emission line flux, relative to I(H-beta) = 100.  When this and 
  the <span style="font-family: monospace;">"wave"</span> parameter are specified, the ionic abundance relative 
  to ionized hydrogen is calculated and stored in the <span style="font-family: monospace;">"result"</span> 
  parameter.  
  </dd>
  </dl>
  <dl>
  <dt><b>(result = INDEF) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(result = INDEF) [real]' -->
  <dd>Ionic abundance relative to H+.  Calculated only if the <span style="font-family: monospace;">"flxratio"</span> 
  and <span style="font-family: monospace;">"wave"</span> parameters are both specified.  
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>Print level populations and critical densities as well?  The 
  critical density for a level <span style="font-family: monospace;">"i"</span> is the density at which the 
  collisional de-excitation rate from this upper level balances the 
  radiative transition rate. 
  </dd>
  </dl>
  <dl>
  <dt><b>(at_data = at_data) [real]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(at_data = at_data) [real]' -->
  <dd>Atomic reference data directory name.  
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Find the level populations, critical densities, and line 
  emissivities for the S+ ion, assuming an electron temperature of 
  9200 K and a density of 1500/cm^3.  
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ionic sulfur 2 temper=9200 density=1500. verb+
  
  # Volume Emissivities for: S^1+
     T_e:   9200.0;  N_e: 1.500E3
  
  # Level Populations - Critical Densities (/cm^3)
  
   Level 1:   9.6E-1
   Level 2: 1.200E-2       1.413E4
   Level 3: 3.025E-2       1.551E3
   Level 4: 4.481E-6       1.252E6
   Level 5: 5.341E-6       1.678E6
   Level 6: 1.16E-17      4.245E14
   Level 7: 7.10E-18      1.798E14
   Level 8: 3.37E-18      1.297E14
  
    6730.87   # Wavelength
    (2--&gt;1)   # Upper-&gt;Lower Level
  1.079E-20   # Volume Emissivity
  
    6716.42   3148614.6
    (3--&gt;1)     (3--&gt;2)
  1.628E-20   4.262E-26
  
    4076.35    10336.31    10370.36
    (4--&gt;1)     (4--&gt;2)     (4--&gt;3)
  1.319E-21   8.096E-22   3.588E-22
  
    4068.60    10286.63    10320.34   2139952.9
    (5--&gt;1)     (5--&gt;2)     (5--&gt;3)     (5--&gt;4)
  3.912E-21   8.321E-22   1.042E-21   3.405E-29
  
    1259.52     1549.47     1550.23     1822.70     1824.25
    (6--&gt;1)     (6--&gt;2)     (6--&gt;3)     (6--&gt;4)     (6--&gt;5)
  5.290E-24       INDEF       INDEF       INDEF       INDEF
  
    1253.81     1540.84     1541.59     1810.77     1812.30   276663.44
    (7--&gt;1)     (7--&gt;2)     (7--&gt;3)     (7--&gt;4)     (7--&gt;5)     (7--&gt;6)
  3.294E-24       INDEF       INDEF       INDEF       INDEF       INDEF
  
    1250.58     1535.97     1536.72     1804.05     1805.57   176289.11   485908.65
    (8--&gt;1)     (8--&gt;2)     (8--&gt;3)     (8--&gt;4)     (8--&gt;5)     (8--&gt;6)     (8--&gt;7)
  1.581E-24       INDEF       INDEF       INDEF       INDEF       INDEF       INDEF
  
  # H-beta Volume Emissivity:
   1.354E-25 N(H+) * N(e-) ergs/s
  
   Log10(x) =   1.194E0
  </pre></div>
  <p>
  2. Find the abundance of the O(+) ion, relative to ionized 
  hydrogen.  The observed flux in the [O ii] 3727.1 + 3729.8 AA 
  emission line doublet (relative to I(H-beta) = 100) is provided, 
  along with a wavelength tolerance large enough to accomodate both 
  lines in the pair, to relate volume emissivities to ionic abundance.
  </p>
  <div class="highlight-default-notranslate"><pre>
     cl&gt; ionic oxygen 2 temper=1.e4 dens=1000. wave=3728 wv_tol=2.0 \
     &gt;&gt;&gt; flx=0.7 verb-
  
  # Volume Emissivities for: O^1+
     T_e:  10000.0; N_e:  1.000E3
  
    3728.80   # Wavelength
    (2--&gt;1)   # Upper-&gt;Lower Level
  1.156E-21   # Volume Emissivity
  
    3726.05   5053057.1
    (3--&gt;1)     (3--&gt;2)
  1.670E-21   8.995E-28
  
    2470.33     7319.50     7330.12
    (4--&gt;1)     (4--&gt;2)     (4--&gt;3)
  6.706E-23   4.297E-23   2.312E-23
  
    2470.21     7318.44     7329.06   50761421.3
    (5--&gt;1)     (5--&gt;2)     (5--&gt;3)     (5--&gt;4)
  1.663E-23   1.374E-23   2.293E-23   5.383E-36
  
     834.47     1075.05     1075.28     1260.13     1260.17
    (6--&gt;1)     (6--&gt;2)     (6--&gt;3)     (6--&gt;4)     (6--&gt;5)
  2.002E-26       INDEF       INDEF       INDEF       INDEF
  
     833.33     1073.17     1073.40     1257.55     1257.58   612745.10
    (7--&gt;1)     (7--&gt;2)     (7--&gt;3)     (7--&gt;4)     (7--&gt;5)     (7--&gt;6)
  1.306E-26       INDEF       INDEF       INDEF       INDEF       INDEF
  
     832.76     1072.22     1072.45     1256.25     1256.28   407664.08   1218026.8
    (8--&gt;1)     (8--&gt;2)     (8--&gt;3)     (8--&gt;4)     (8--&gt;5)     (8--&gt;6)     (8--&gt;7)
  6.456E-27       INDEF       INDEF       INDEF       INDEF       INDEF       INDEF
  
  # H-beta Volume Emissivity:
   1.258E-25 N(H+) * N(e-)  (erg/s)
  
   Log10(x) =   1.000E0
  
   Ionic Abundance: N(O^1+) / N(H+) =  3.116E-7
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Extremely small volume emissivities, those less than about 1.E-36, 
  are treated as INDEF.  
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  The 5-level atom program, upon which this package is based, was 
  originally written by M.M. DeRobertis, R. Dufour, and R. Hunt.  
  This package was written by R.A. Shaw (STScI).  A description was 
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
  For further information type <span style="font-family: monospace;">"help nebular opt=sysdoc"</span>.  
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE	' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

.. _nlevel:

nlevel: Documentation on the N-level atom approximation
=======================================================

**Package: nebular**

.. raw:: html

  <section id="s_introduction">
  <h3>Introduction</h3>
  <p>
  Some of the tasks in the `nebular' package are based upon the FIVEL 
  program developed by De Robertis, Dufour &amp; Hunt (1987).  They can 
  be used to calculate the physical conditions in a low density 
  (nebular) gas given appropriate diagnostic emission line ratios; 
  and line emissivities given appropriate emission line fluxes, the 
  electron temeperature (T_e), and density (N_e).  These tasks have 
  been extended beyond the original FIVEL program to provide 
  diagnostics from a greater set of ions and emission lines, most 
  particularly those in the vacuum ultraviolet that are now available 
  from the IUE and HST archives.  In addition, more than 5 levels are 
  now accomodated for most of the ions.  
  </p>
  <p>
  It should be noted that these routines are not intended as a full 
  nebular photoionization model, such as G. Ferland's CLOUDY. Rather, 
  they are intended for the fairly common instances where one has 
  somewhat incomplete information about a complicated physical system 
  (such as a narrow-line region in an active galactic nucleus), or 
  somewhat more information about a physically simple system, such as 
  a fairly evolved planetary nebula.  In these cases it is useful to 
  calculate nebular densities or temperatures from the traditional 
  diagnostic line ratios, either to provide some resonable input 
  parameters for a more complicated physical model, or to calculate 
  ionic abundances (or other quantities) within some simplifying 
  assumptions.  
  </p>
  <p>
  The physical basis for line emission from a photoionized nebula has 
  been discussed in many excellent references and will not be 
  repeated here.  A detailed description of the methodology of this 
  software, and the appropriate astrophysical problem domain, can 
  be found in Shaw &amp; Dufour (1995).  A link to the on-line and 
  PostSCript versions of this paper may be found on the Web page for 
  the nebular package, at URL http://ra.stsci.edu/nebular/.  
  </p>
  </section>
  <section id="s_nebular_diagnostics_and_ionic_abundances">
  <h3>Nebular diagnostics and ionic abundances</h3>
  <p>
  Certain emission line ratios in five-level atoms are very useful as 
  diagnostics of electron temperature or density.  The p^2 and p^4 
  ions have ground state configurations such that some transitions 
  from upper levels have very different excitation energies; ratios 
  of the resulting emission lines can serve as very effective 
  temperature indicators because they are insensitive to density.  
  Conversely, in p^3 ions some transitions to the ground state have 
  upper levels with nearly the same excitation energy.  Ratios of 
  these lines can serve as very effective density indicators because 
  the level populations are quite insensitive to temperature.  The 
  available diagnostic line ratios for the FIVEL tasks are tabulated 
  in the next section. 
  </p>
  <p>
  The ionic abundances, relative to H+, can be derived from the 
  observed ratio of a forbidden line intensity relative to H-beta.  
  Aller (1984) provides a convenient fitting formula for the H-beta 
  emissivity which is accurate to within about 4% for densities less 
  than about 10**6/cm^3.  The formula:
  </p>
  <div class="highlight-default-notranslate"><pre>
  4(pi) j(H-beta) =
                                     -0.983
                1.387E-25 N_e N(H+) t       dex(-0.0424/t)
  </pre></div>
  <p>
  in units of (erg/cm^3/s), is used within the nebular routines; here, 
  t = T_e / 10^4 K.  The H-beta emissivity is calculated for the same 
  temperature as the specified ion, and the ionic abundance ratio is 
  calculated from:
  </p>
  <div class="highlight-default-notranslate"><pre>
     i
  N(X )    I(line)    j(H-beta)
  ----- = --------- * ---------
  N(H+)   I(H-beta)    j(line)
  </pre></div>
  <p>
  where I(line)/I(H-beta) is the observed line ratio.  Note that ALL 
  of the line emissivities output by the <span style="font-family: monospace;">"ionic"</span> task are per unit 
  ion density per unit electron density.  That is, the true volume 
  emissivity (j_true) is related to by:
  </p>
  <div class="highlight-default-notranslate"><pre>
  4 * pi * j(true) = N_e * N(X^i) * j(task)
  </pre></div>
  <p>
  Any of the transitions for any of the ions can be used to derive the 
  ionic abundance, but the strongest lines that are typically used in 
  the nebular tasks are tabulated in the next section. 
  </p>
  <p>
  It should be noted that the nebular routines give line emissivities
  and diagnostic ratios for metastable-level magnetic dipole or 
  electric quadrapole transitions under the assumption of pure 
  statistical equilibrium and do not account for radiation transfer 
  effects such as self-absorption in some levels.  For some 
  astrophysical situations such as giant H ii regions and AGNs, the 
  optical depths of the ^3P multiplet levels of p^2 and p^4 ions such 
  as [O iii], [N ii], and [Ne iii] can become significant, which will 
  affect the observed far-infrared line strengths for such objects 
  compared to the program predictions.  While no nebular task currently 
  makes use of N_e and T_e diagnostics from the far-infrared lines, 
  one can make use of these lines with the 
  <span style="font-family: monospace;">"abund"</span> task (see below) for low-density H II regions and planetary
  nebulae. However, caution is advised for such use on giant H II 
  regions or dense, highly ionized planetary nebulae for which the 
  optical depth in the ^3P levels could become important.  
  </p>
  </section>
  <section id="s_3_zone_nebular_model">
  <h3>3-zone nebular model</h3>
  <p>
  In order to calculate ionic abundances in a real nebula, it is 
  necessary to know the electron temperature and density where the 
  various ionic emissions are produced.  In some physical contexts 
  it makes sense to view the structure of a nebula an an <span style="font-family: monospace;">"onion 
  skin"</span>, where the ionization drops off radially from some central 
  source of ionizing radiation, and T_e drops somewhat as N_e 
  increases (on average) with distance.  Different ions are found 
  in spherical shells of various radii, depending on the ionization 
  potential of the ion.  
  </p>
  <p>
  Two tasks in this package were designed to model nebulae in just 
  this way, with 3 zones of low-, intermediate-, and high-ionization. 
  The nebular physical parameters are derived within each zone by 
  making simultaneous use of temperature- and density-sensitive line 
  ratios from different ions with similar ionization potentials.  The 
  small dependence of the temperature indicators upon N_e, and of the 
  density indicators upon T_e, is removed with an iterative technique 
  and ultimately results in an average T_e and N_e within each zone.  
  </p>
  <p>
  The modelling tasks are layered upon the TABLES external package in 
  order to provide a simple and powerful data structure and ancillary 
  tools for access to the observed data and the derived results.  The 
  input tables may contain line fluxes for many nebulae and/or many 
  regions within nebulae, one object/region per row.  The flux(es) 
  for a given emission line (usually, but not necessarily, given 
  relative to I(H-beta)=100) are placed in separate columns.  The 
  tasks locate particular emission line fluxes and temeratures/
  densities via names of specific columns in the input table(s).  
  These columns have suggestive default names, but are entirely 
  user-definable.  
  </p>
  <p>
  Since it is often difficult to provide a complete set of diagnostic 
  line ratios (owing to limited signal-to-noise ratio, spectral 
  resolution, wavelength coverage, etc., of the observed spectra) 
  these tasks were designed to make use of whatever information is 
  available, and to use reasonable defaults (e.g., T_e = 10,000 K, 
  N_e = 1000/cm^3) when necessary.  In particular, any emission line 
  flux that is unavailable (e.g. the relevant line fluxes are INDEF, 
  or the column name for that line flux is not found) is excluded 
  from the calculations.  If there are no valid diagnostic line 
  fluxes available for a given ion, the result for that ion is INDEF. 
  </p>
  <p>
  The available diagnostic line ratios, the ionization potential of 
  the associated ion, and the nebular ionization zone to which they 
  are attributed, are listed by ion below.  The line ratio is in the 
  form I(wave1)/I(wave2), where <span style="font-family: monospace;">"wave1"</span> and <span style="font-family: monospace;">"wave2"</span> are in units of 
  Angstroms; ratios involving sums of line strengths are given as 
  I(wave1+wave2)/I(wave3+wave4).  Diagnostics marked with an asterisk 
  are not currently used in the 3-zone nebular model, described 
  below.  
  </p>
  <div class="highlight-default-notranslate"><pre>
          Table 1. Ions Included in NEBULAR
  
                      Ground   No.
    Ion    Spectrum   Config  Levels  I.P.  Zone
  -------------------------------------------------
    C(0)     C I        p^2     5      0.0   Low
    C(+1)    C II       p^1     8     11.3   Low
    C(+2)    C III      s^2     5     24.4   Med
    N(0)     N I        p^3     5      0.0   Low
    N(+1)    N II       p^2     6     14.5   Low
    N(+2)    N III      p^1     8     29.6   Med
    N(+3)    N IV       s^2     5     47.4   Med
    O(0)     O I        p^4     5      0.0   Low
    O(+1)    O II       p^3     5     13.6   Low
    O(+2)    O III      P^2     6     35.1   Med
    O(+3)    O IV       P^1     8     54.9   High
    O(+4)    O V        s^2     5     77.4   High
   Ne(+2)   Ne III      p^4     5     41.1   Med
   Ne(+3)   Ne IV       P^3     5     63.5   High
   Ne(+4)   Ne V        P^2     6     97.0   High
   Ne(+5)   Ne VI       p^1     7    126.3   High
   Na(+3)   Na IV       p^4     5     71.7   High
   Na(+5)   Na VI       p^2     5    138.4   High
   Mg(+4)   Mg V        p^4     5    109.3   High
   Mg(+6)   Mg VII      p^2     6    186.5   High
   Al(+1)   Al II       s^2     5      6.0   Low
   Si(+1)   Si II       p^1     7      8.2   Low
   Si(+2)   Si III      S^2     5     16.3   Low
    S(+1)    S II       P^3     8     10.4   Low
    S(+2)    S III      p^2     5     23.4   Med
    S(+3)    S IV       p^1     5     35.0   Med
   Cl(+2)   Cl III      P^3     5     23.8   Med
   Cl(+3)   Cl IV       p^2     5     39.9   Med
   Ar(+2)   Ar III      p^4     5     27.6   Med
   Ar(+3)   Ar IV       P^3     5     40.9   Med
   Ar(+4)   Ar V        p^2     5     59.8   High
    K(+3)    K IV       p^4     5     46.0   Med
    K(+4)    K V        p^3     5     60.9   High
   Ca(+4)   Ca V        p^4     5     67.0   High
  -------------------------------------------------
  </pre></div>
  <div class="highlight-default-notranslate"><pre>
       Table 2. Electron Density Diagnostics
  
   Spectrum       Line Ratio              Zone
  ----------------------------------------------
     C ii]        I(2326) / I(2328)       Low  *
     C iii]       I(1907) / I(1909)       Med
    [N i]         I(5198) / I(5200)       Low  *
     N iii]       I(1749) / I(1752)       Med  *
     N iv]        I(1483) / I(1487)       Med
    [O ii]        I(3726) / I(3729)       Low
     O iv]        I(1401) / I(1405)       High *
    [O v]         I(1214) / I(1218)       High
   [Ne iv]        I(2423) / I(2425)       High
   [Al ii]        I(2661) / I(2670)       Low
   [Si ii]        I(2335) / I(2345)       Low
    Si iii]       I(1883) / I(1892)       Low  *
    [S ii]        I(6716) / I(6731)       Low
    [S iv]        I(1406) / I(1417)       Med
   [Cl iii]       I(5517) / I(5537)       Med
   [Ar iv]        I(4711) / I(4740)       Med
    [K v]         I(6223) / I(6349)       High
  ----------------------------------------------
  </pre></div>
  <div class="highlight-default-notranslate"><pre>
      Table 3. Electron Temperature Diagnostics
  
   Spectrum       Line Ratio              Zone
  ----------------------------------------------
    [C i]    I(9823+9849) / I(8728)        Low
    [N i]    I(5198+5200) / I(10397+10407) Low
    [N ii]   I(6548+6583) / I(5755)        Low
    [O i]    I(6300+6363) / I(5577)        Low
    [O ii]   I(3726+3729) / I(7320+7330)   Low
    [O iii]  I(4959+5007) / I(4363)        Med
   [Ne iii]  I(3869+3969) / I(3342)        Med
   [Ne iv]   I(2422+2425) / I(1601+1602)   High
   [Ne v]    I(3426+3346) / I(2975)        High
   [Na iv]   I(3242+3362) / I(2805)        High
   [Na vi]   I(2871+2970) / I(2569)        High
   [Mg v]    I(2783+2928) / I(2418)        High
   [Mg vii]  I(2506+2626) / I(2262)        High
   [Al ii]   I(2661+2670) / I(1671)        Low
    Si iii]  I(1883+1892) / I(1206)        Low  *
    [S ii]   I(6716+6731) / I(4068+4076)   Low
    [S iii]  I(9069+9532) / I(6312)        Med
   [Cl iii]  I(5517+5537) / I(3353+3343)   Med
   [Cl iv]   I(7530+8045) / I(5323)        Med  *
   [Ar iii]  I(7136+7751) / I(5192)        Med
   [Ar iv]   I(4711+4740) / I(2854+2868)   Med  *
   [Ar v]    I(6435+7006) / I(4626)        High
    [K iv]   I(6102+6796) / I(4511)        High
    [K v]    I(4123+4163) / I(2515+2495)   High
   [Ca v]    I(5309+6087) / I(3996)        High
  ----------------------------------------------
  </pre></div>
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
  &amp; Mathis (1989), and the function of Kaler (1976), which is based 
  on Whitford (1958).  The choices for extra-Galactic extinction laws 
  are Howarth (1983) for the LMC, and Prevot et al. (1984) for the 
  SMC.  
  </p>
  <p>
  The abundance calculations in the 3-zone model are based upon the 
  diagnostics appropriate for each ion, and are listed below in the 
  <span style="font-family: monospace;">"Ionization Zone"</span> column.  The emission lines that are actually 
  used in the 3-zone model (which are generally also the strongest) 
  can be found in the file nebular$atomic_data/abund.tab, but most 
  are also tabulated below (wavelengths are in Angstroms) by ion: 
  </p>
  <div class="highlight-default-notranslate"><pre>
      Table 4. Line Fluxes Often Used for Ionic Abundances
  
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
  Note that some fluxes are really sums from closely spaced line 
  pairs.  The calculated ionic abundance is the weighted average of
  that derived from each of the emission lines for that ion.  
  </p>
  <p>
  A CAUTION ABOUT THE WAVELENGTHS:  Please note that the wavelengths 
  used throughout these help files are those commonly used in the 
  astronomical literature.  However, some of the wavelengths do not 
  have particularly precisely measured values.  References for the 
  wavelengths used in this package may be found in the atomic data 
  files in nebular$atomic_data.  The wavelength uncertainties are 
  only likely to cause confusion when using the <span style="font-family: monospace;">"ionic"</span> task to 
  compute an ionic abundance from a particular line.  In this case, 
  be sure the <span style="font-family: monospace;">"wave"</span> or <span style="font-family: monospace;">"wv_toler"</span> parameters are set appropriately.  
  </p>
  <p>
  A CAUTION ABOUT ACCURACIES:  The ultimate accuracy of the line 
  emissivities or ionic abundances calculated by this software is  
  inherently limited by the accuracies in the published atomic data: 
  the collision strengths (and their variation with temperature) and 
  the oscillator strengths generally have accuracies of ~10%, 
  although some are as high as 30%.  We have endeavored to use the 
  best, recent atomic data as of mid-1996.  However, it is possible 
  for this data to be updated easily by the user, if necessary.  
  See the README file in nebular$data.   
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  The atomic data for hydrogen were taken from Brocklehurst (1970, 
  1971); in particular, we adopt an empirical formula from Aller 
  (1984) for the H-beta line emissivity.  References for the other 
  atomic data may be found by typing <span style="font-family: monospace;">"help at_data"</span>. 
  </p>
  <p>
  The 5-level atom program was originally published by DeRobertis, 
  Dufour &amp; Hunt (1987).  Although the nebular tasks are intended to 
  provide all the functionality of their original <span style="font-family: monospace;">"FIVEL"</span> FORTRAN 
  program, the code has been entirely re-engineered, and essentially 
  all the atomic data have been updated since that code was 
  published. These tasks also offer additional options and 
  flexibility, including tasks for computing all available 
  diagnostics at once within a simple physical context.  Additional 
  enhancements and a discussion of the scientific problem domain are 
  described by Shaw &amp; Dufour (1995). Support for this software 
  development was provided from the NASA Astrophysics Data Program 
  through grant NAG5-1432 to Space Telescope Science Institute, and 
  supplemented by a grant from the STScI Director's Discretionary 
  Research Fund.  
  </p>
  <div class="highlight-default-notranslate"><pre>
                          LITERATURE CITED
  
  Aller, 1984, "Physics of Thermal Gaseous Nebulae" (Dordrecht:D. Reidel)
  
  Brocklehurst, 1970, MNRAS, 148, 417
  
  Brocklehurst, 1971, MNRAS, 153, 471
  
  Cardelli, Clayton &amp; Mathis, 1989, ApJ, 345, 245
  
  De Robertis, Dufour &amp; Hunt, 1987, J. Roy. Astron. Soc. Canada, 81, 195
  
  Hayes &amp; Nussbaumer, 1984, A&amp;A, 134, 193
  
  Howarth, 1983, MNRAS, 203, 301
  
  Kaler, 1976, ApJS, 31, 517
  
  Osterbrock, D. 1989, "Astrophysics of Gaseous Nebulae and Active
  Galactic Nuclei" (Mill Valley:University Science Books)
  
  Prevot, Lequeux, Maurice, Prevot &amp; Rocca-Volmerange, 1984, A&amp;A, 132, 389
  
  Savage &amp; Mathis, 1979, ARA&amp;A, 17, 73
  
  Shaw, &amp; Dufour, 1995, PASP, 107, 896
  
  Whitford, 1958, AJ, 63, 201
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  at_data. 
  </p>
  <p>
  Type <span style="font-family: monospace;">"help nebular opt=sys"</span> for a general description 
  of the tasks in the `nebular' package.  
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'INTRODUCTION' 'NEBULAR DIAGNOSTICS AND IONIC ABUNDANCES' '3-ZONE NEBULAR MODEL' 'REFERENCES' 'SEE ALSO'  -->
  

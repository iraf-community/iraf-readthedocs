nebular: Tasks for analyzing nebular emission lines
===================================================

.. toctree:: :maxdepth: 1

   abund
   at_data
   diagcols
   fluxcols
   ionic
   nlevel
   ntcontour
   ntplot
   redcorr
   temden
   zones
.. raw:: html

  <section id="s_introduction">
  <h3>Introduction</h3>
  <p>
  Tasks in this package can be used to derive various physical 
  quantities from the emission line fluxes of a low-density (nebular) 
  gas.  These quantities include the electron temperature (T_e) and 
  density (N_e) from various diagnostic line flux ratios, and level 
  populations, critical densities, line emissivities and abundances 
  for several common ions.  A brief summary of the tasks is given in 
  the table below; details may be found in the following sections.  
  </p>
  <div class="highlight-default-notranslate"><pre>
                      Table 1. NEBULAR Tasks
  +----------------------------------------------------------------+
  | Task      | Description                                        |
  +----------------------------------------------------------------+
  | abund     | Derive ionic abundances in a 3-zone nebula         |
  | at_data   | Documentation on the atomic reference data         |
  | diagcols  | P-set of table column names for computed T_e &amp; N_e |
  |           |    for each zone                                   |
  | fluxcols  | P-set of table column names for input emission     |
  |           |    line fluxes                                     |
  | ionic     | Compute level populations, critical densities,     |
  |           | line emissivities &amp; abundance for a single ion     |
  | nlevel    | Documentation on the N-level atom approximation    |
  | ntcontour | Plot contours of line ratios on the N_e, Te plane  |
  | ntplot    | Construct a N_e, Te plot for observed diagnostic   |
  |           |    line ratios                                     |
  | redcorr   | Correct line flux for interstellar reddening       |
  | temden    | Compute T_e or N_e from diagnostic line ratios     |
  | zones     | Derive T_e &amp; N_e in 3-zone nebula from diagnostic  |
  |           |    emission line ratios                            |
  +----------------------------------------------------------------+
  </pre></div>
  <p>
  This package is not intended to offer a full nebular modelling 
  program, such as G. Ferland's CLOUDY.  Rather, it is intended for 
  the fairly common instances where one has somewhat incomplete 
  information about a complicated physical system (such as a narrow-
  line region in an active galactic nucleus), or somewhat more 
  information about a physically simple system, such as a fairly 
  evolved planetary nebula.  In these cases it is useful to calculate 
  nebular densities or temperatures from the traditional diagnostic 
  line ratios, either to provide some resonable input parameters for 
  a more complicated physical model, or to calculate ionic abundances 
  (or other quantities) within some simplifying assumptions.  
  </p>
  <p>
  Some of the tasks in this package make use of STSDAS binary tables 
  for accessing potentially large lists of emission line fluxes for 
  many nebulae.  The various line fluxes are contained in different 
  columns, and data for different nebulae (or different regions 
  within nebulae) are contained in separate rows. The `tables.ttools' 
  tasks provide all the needed utilities for generating, editing, and 
  printing the table contents.  Examples of test tables can be found 
  in the directory nebular$data. Generally, the user has control of 
  the table column names through named parameter sets.  
  </p>
  </section>
  <section id="s_nebular_diagnostics_and_abundances">
  <h3>Nebular diagnostics and abundances</h3>
  <p>
  Several of the tasks are based upon the FIVEL program developed by 
  De Robertis, Dufour, and Hunt (1987).  These routines make use of 
  the fact that that most of the common ions that dominate the 
  nebular cooling rate have either p^2, p^3, or p^4 ground-state 
  electron configurations, which have five low-lying levels.  The 
  major physical assumption within this algorithm is that only these 
  five levels are physically relevant for calculating the observed 
  emission line spectrum.  These tasks have been extended beyond the 
  original FIVEL program to provide diagnostics from a greater set of 
  emission lines, most particularly those in the vacuum ultraviolet 
  that are now available from the IUE and HST archives.  
  </p>
  <p>
  The `temden' task will calculate N_e given T_e, or T_e given N_e, 
  for a given ion and the associated diagnostic flux ratio.  The 
  result is displayed and stored in a task parameter.  The `ionic' 
  task will calculate the level populations, critical densities, and 
  line emissivities for a specified ion, given N_e and T_e.  It will 
  also calculate the ionic abundance relative to H+ if the wavelength 
  and relative flux (on the scale I[H-beta] = 100) of one of the 
  emission lines are also specified.  
  </p>
  <p>
  The available ions from which abundances and/or diagnostics can be 
  derived, and the ionization potential of that ion, can be found by 
  typing <span style="font-family: monospace;">"help nlevel"</span>. 
  </p>
  </section>
  <section id="s_3_zone_nebular_model">
  <h3>3-zone nebular model</h3>
  <p>
  The `zones' task calculates T_e and N_e within each of 3 zones of 
  low-, medium-, and high-ionization.  It uses iteration to make 
  simultaneous use of temperature- and density-sensitive line ratios 
  from different ions with similar ionization potential.  The `abund' 
  task computes the abundances for several ions using T_e and N_e as 
  computed by `zones'. The ionization potential of the ion determines 
  which T_e and N_e is used.  The input line fluxes are taken from a 
  specified table.  UV fluxes can be given on a separate scale, 
  provided that the UV-to-optical scale factor is specified.  The 
  input line fluxes can optionally be corrected for interstellar 
  reddening.  
  </p>
  </section>
  <section id="s_future_development">
  <h3>Future development</h3>
  <p>
  Additional tasks are planned for this package which will derive the 
  interstellar extinction coefficient from (among other methods) the 
  hydrogen Balmer decrement, as well as compute ionic abundances 
  (relative to H+) from recombination lines.  
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
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
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  nlevel; also tcreate, tedit, tcalc in the TABLES external package.  
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'INTRODUCTION' 'NEBULAR DIAGNOSTICS AND ABUNDANCES' '3-ZONE NEBULAR MODEL' 'FUTURE DEVELOPMENT' 'REFERENCES' 'SEE ALSO'  -->
  

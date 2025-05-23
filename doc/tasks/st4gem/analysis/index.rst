analysis: Data analysis packages.
=================================

.. toctree:: :maxdepth: 1

   dither/index
   fitting/index
   fourier/index
   isophote/index
   nebular/index
.. raw:: html

  <section id="s_description">
  <h3>Description</h3>
  <p>
  The `st4gem.analysis' package contains eight packages of tasks for 
  general image and spectral analysis, image restoration, statistics, 
  and access to the Guide Star Catalog.  These tasks are not 
  necessarily specific to HST data, but they do address some of the 
  most common anaylsis needs at Space Telescope Science Institute.  In 
  addition, these tasks are designed to make use of both IRAF images, 
  and ST4GEM binary tables for task I/O.  A quick summary of the 
  available packages is given in Table 1 below; a more detailed summary 
  can be found in the following sections.  
  </p>
  <div class="highlight-default-notranslate"><pre>
  
              Table 1.  HST Analysis Packages
  +-----------------------------------------------------------+
  | Package    | Description                                  |
  +-----------------------------------------------------------+
  | dither     | Combine images using the "drizzle" algorithm |
  | fitting    | General image and spectrum feature fitting   |
  | fourier    | Utilities for Fourier analysis               |
  | isophote   | Elliptical isophote fitting                  |
  | nebular    | Tasks for analyzing nebular emission lines   |
  +-----------------------------------------------------------+
  </pre></div>
  <p>
  DITHERED IMAGE COMBINATION
  </p>
  <p>
  The `dither' package contains tasks which can be used to combine dithered 
  images using the <span style="font-family: monospace;">"drizzle"</span> algorithm.
  </p>
  <p>
  Two basic procedures are available, depending on the existence of only 
  linear shifts between the images to be combined, or linear shifts plus 
  a (small) rotation angle. Both procedures rely on cross-correlation to 
  derive the relative shifts and rotation angles. 
  </p>
  <p>
  The `drizzle' task can be used to process any image format supported by 
  IRAF, the remaining tasks are specific for WFPC data.
  The `drizzle' task must be supplied with the linear shifts in X and Y and 
  the rotation angle in between images to be combined. It also supports 
  rescaling the pixel grid and corrections for geometric distortions, but 
  only coefficients appropriate for WFPC-II data are currently available.
  </p>
  <p>
  GENERAL FEATURE FITTING
  </p>
  <p>
  There are two packages with tasks that are useful for fitting features 
  in images, and both are layered on the IRAF 'icfit' utilities.  That 
  is, the majority of the 'cursor' commands that are defined for 
  'icfit' will function for these fitting tasks as well.  Both packages 
  use the 'tables' external package for storing and accessing the fitted 
  parameters.  
  </p>
  <p>
  The `isophote' package is intended for fitting galaxy brightness 
  profiles in 2-D images with elliptical isophotes.  The more general 
  `fitting' package can fit elliptical Gaussians to two-dimensional 
  images.   It can also fit one-dimensional Gaussians, Planck or 
  power-law functions, and composite profiles to spectra or image 
  sections.  The `fitting' tasks can optionally set or solve for any 
  of the function coefficients.  The functions are fit using a downhill 
  simplex (or <span style="font-family: monospace;">"amoeba"</span>) method, and the coefficient errors can be 
  estimated using a <span style="font-family: monospace;">"bootstrap"</span> technique.  
  </p>
  <p>
  FOURIER ANALYSIS
  </p>
  <p>
  The `fourier' package contains tasks for forward and inverse Fourier 
  transforms, as well as related tasks for computing power spectra, 
  cross-correlations, convolutions, etc.  Other auxiliary tasks can 
  find the prime factors of a number, perform complex image arithmetic, 
  or taper image edges.  At present, these tasks operate only on images, 
  not on tables or lists.  
  </p>
  <p>
  NEBULAR ANALYSIS
  </p>
  <p>
  Tasks in the `nebular' package can be used to derive various 
  physical quantities from the emission line fluxes of a low-density 
  (nebular) gas.  These quantities include the electron temperature 
  (T_e) and density (N_e) from various diagnostic line flux ratios, 
  and level populations, critical densities, line emissivities and 
  abundances for most common ions.  
  </p>
  <p>
  OTHER ANALYSIS TASKS
  </p>
  <p>
  Some analysis tasks have been written outside the ST4GEM group, but 
  are potentially very useful for the HST community.  We make these 
  tasks available in the `contrib' package, although the responsibility 
  for the accuracy and utility of these tasks rests with the authors.  
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  dither, fitting, fourier, isophote, nebular, toolbox.ttools
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'DESCRIPTION' 'SEE ALSO'  -->
  

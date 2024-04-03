hst_calib: HST Science Instrument calibration packages.
=======================================================

.. toctree:: :maxdepth: 1

   synphot/index
.. raw:: html

  <section id="s_introduction">
  <h3>Introduction</h3>
  <p>
  The `st4gem.hst_calib' package contains the tasks that are used to 
  calibrate data from each of the HST Science Instruments (SIs), and 
  to model the combined response of the various detectors and 
  optical elements.  It also contains tasks to derive the instrument 
  calibrations and construct the calibration reference files.  The 
  tasks are divided into nine packages: seven that are specific to a 
  particular instrument, and two that contain more general HST 
  calibration tools.  A quick summary is given in Table 1 below; a 
  more detailed summary can be found in the following sections.  
  </p>
  <div class="highlight-default-notranslate"><pre>
  
              Table 1.  HST Calibration Packages
  +-----------------------------------------------------------+
  | Package | Description                                     |
  +-----------------------------------------------------------+
  | synphot | General tools for modelling instrument response |
  +-----------------------------------------------------------+
  </pre></div>
  <p>
  USING GEIS FILES
  </p>
  <p>
  Perhaps the most daunting aspect of HST data reduction and analysis 
  for novice users of ST4GEM is the complexity of the data structures.  
  GEIS format (also called ST format or <span style="font-family: monospace;">"group"</span> format) data is 
  described in some detail in the <span style="font-family: monospace;">"ST4GEM Users Guide"</span> and in the 
  on-line help file (type <span style="font-family: monospace;">"help geis"</span>).  The most important point is 
  that GEIS files can contain more than one image in a single datafile; 
  each image is stored in a separate <span style="font-family: monospace;">"group"</span> within the file.  
  As well, the parameters (or descriptors) that are common for all 
  groups in the image are stored in FITS-style keywords in the ASCII 
  header, but parameters that are group-specific are stored within the 
  binary image data.  While this subtlety is transparent to most ST4GEM 
  tasks, it is an important point to remember.  
  </p>
  <p>
  It is also important to realize how GEIS files are used for 
  each instrument.  FOC data files have only one group per 
  file, and WFPC and WFPC-2 files usually have four groups---one 
  per CCD detector.  The spectrographs (FOS and HRS), on the other 
  hand, store each read of the diode array in a separate group.  
  Thus, one file could contain hundreds of groups, and the sequence 
  could define a spectral time series, a single spectrum as the counts 
  accumulate, or an acquisition image, depending upon the instrument 
  observing mode.  Table 2 summarizes the way that groups are used 
  for each HST instrument.  
  </p>
  <div class="highlight-default-notranslate"><pre>
  
              Table 2.  HST Data Structure Summary
  +--------------------------------------------------------------+
  | Instrument | Group Use                                       |
  +--------------------------------------------------------------+
  |   FOC      | One group per file                              |
  |   FOS      | One group per scan, possibly hundreds per file  |
  |   HRS      | One group per scan, possibly hundreds per file  |
  |   WFPC     | One group per CCD detector, up to four per file |
  |   WFPC-2   | One group per CCD detector, up to four per file |
  +--------------------------------------------------------------+
  </pre></div>
  <p>
  If you use non-ST4GEM tasks in the IRAF environment for your 
  analysis, be aware that operations must be performed explicitly on 
  each group in the data file; the default is usually to operate on 
  only the first group of multi-group files.  On the other hand, most 
  ST4GEM tasks either perform the specified operation on all groups, 
  or make some explicit provision (usually in the task parameters) to 
  define the group(s) on which they operate.  Novice users may find 
  the tasks in the `toolbox' packages especially useful, and may 
  profit from practicing some basic operations on test HST data, 
  examples of which can be found in the directory <span style="font-family: monospace;">"scidata$"</span>.  
  </p>
  <p>
  GENERAL CALIBRATION UTILITIES
  </p>
  <p>
  There are two packages with tasks that are useful for two or more 
  HST science instruments, and both are implicitly loaded when 
  `hst_calib' is loaded.  Placing these tasks in a separate package 
  merely serves (in this case) to emphasize their utility for more 
  than one instrument, and to make the instrument package menus 
  manageable.  
  </p>
  <p>
  The `ctools' package contains several general, 
  calibration-related tools, such as a generic calibration parameter 
  editor, a vacuum-to-air wavelength correction task, and a task for 
  computing encircled energy in a PSF, etc.  See the `ctools' 
  package help for details.  
  </p>
  <p>
  The `synphot' package provides a number of very powerful utilities 
  for computing the throughput of all optical pathways in the OTA, 
  COSTAR, and the instruments themselves (including all the gratings and 
  filters).  It can also model the response of each instrument to a 
  variety of sources, including standard stars, black-body and 
  power-law spectra, and user-defined spectra.  Since the instrument 
  sensitivities are part of the `synphot' database, it is particularly 
  useful for deriving count-rates and exposure times for observing 
  proposals.  Further details can be found in the package help 
  file, and in the <span style="font-family: monospace;">"Synphot Users Guide"</span> (available from the ST4GEM
  Group, send e-mail to: hotseat@stsci.edu).  
  </p>
  <p>
  Most of the general plotting and analysis tools that users need to 
  display, analyze and interpret their HST data are available within 
  other packages, such as the `graphics', `analysis', and `toolbox', 
  packages.  
  </p>
  <p>
  INSTRUMENT-SPECIFIC PACKAGES
  </p>
  <p>
  Tasks that are usually useful for only one SI can be found in a 
  package named after that instrument.  It is within these packages 
  that the Routine Science Data Processing (RSDP) calibration code 
  (i.e., the <span style="font-family: monospace;">"calXXX"</span> or <span style="font-family: monospace;">"calibration pipeline"</span> tasks) can be found.  
  Other tasks in the instrument-specific packages enable users to, 
  e.g., examine FOS or HRS acquisition images, perform post-pipeline 
  data reduction (e.g., for spectropolarimetry), or derive accurate 
  coordinates for stars on WFPC images.  
  </p>
  <p>
  Tasks that are used to derive the instrument calibrations, and to 
  produce the calibration reference files for the Calibration Data 
  Base System (CDBS), are usually found 
  in sub-packages within the instrument packges.  Generally, these 
  tasks are of little interest to any except the instrument teams, as they 
  are used to analyze the health and quantum efficiency of the 
  instruments, perform trend analysis, and re-format data for CDBS.  
  However, these tasks are distributed off-site for users who wish to 
  create their own reference files (e.g., WFPC flat fields), or who 
  wish to know more about how the calibrations are derived.  See 
  the package help for each instrument, the HST instrument 
  handbooks, and the <span style="font-family: monospace;">"ST4GEM Calibration Guide"</span> for further details.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  acs, cos, ctools, foc, fos, hrs, nicmos, stis, synphot, wfc3, wfpc 
  </p>
  <p>
  Type <span style="font-family: monospace;">"help geis"</span> for more information about GEIS format files.  
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'INTRODUCTION' 'SEE ALSO'  -->
  

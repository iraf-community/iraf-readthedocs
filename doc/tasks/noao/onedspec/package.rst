.. _package:

package: Discussion and overview of package including sections on:
==================================================================

**Package: onedspec**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  onedspec
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_observatory">
  <dt><b>observatory = <span style="font-family: monospace;">"observatory"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observatory' Line='observatory = "observatory"' -->
  <dd>Observatory at which the spectra were obtained if not specified in the
  image header by the keyword OBSERVAT.  This parameter is used by several
  tasks in the package through parameter redirection so this parameter may be
  used to affect all these tasks at the same time.  The observatory may be
  one of the observatories in the observatory database, <span style="font-family: monospace;">"observatory"</span> to
  select the observatory defined by the environment variable <span style="font-family: monospace;">"observatory"</span> or
  the parameter <b>observatory.observatory</b>, or <span style="font-family: monospace;">"obspars"</span> to select the
  current parameters set in the <b>observatory</b> task.  See help for
  <b>observatory</b> for additional information.
  </dd>
  </dl>
  <dl id="l_caldir">
  <dt><b>caldir = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='caldir' Line='caldir = ""' -->
  <dd>Calibration directory containing standard star data.  This parameter
  is used by several tasks in the package through redirection.  A list of
  standard calibration directories may be obtained by listing the file
  <span style="font-family: monospace;">"onedstds$README"</span>; for example:
  <div class="highlight-default-notranslate"><pre>
  cl&gt; page onedstds$README
  </pre></div>
  The user may copy or create their own calibration files and specify
  the directory.  The directory <span style="font-family: monospace;">""</span> refers to the current working directory.
  </dd>
  </dl>
  <dl id="l_interp">
  <dt><b>interp = <span style="font-family: monospace;">"poly5"</span> (nearest|linear|poly3|poly5|spline3|sinc)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interp' Line='interp = "poly5" (nearest|linear|poly3|poly5|spline3|sinc)' -->
  <dd>Spectrum interpolation type used when spectra are resampled.  The choices are:
  <div class="highlight-default-notranslate"><pre>
  nearest - nearest neighbor
   linear - linear
    poly3 - 3rd order polynomial
    poly5 - 5th order polynomial
  spline3 - cubic spline
     sinc - sinc function
  </pre></div>
  </dd>
  </dl>
  <p>
  The following parameters apply to two and three dimensional images
  such as long slit or Fabry-Perot spectra.  They allow selection of
  a line or column as the spectrum <span style="font-family: monospace;">"aperture"</span> and summing of neighboring
  elements to form a one dimensional spectrum as the tasks in the
  ONEDSPEC package expect.
  </p>
  <dl id="l_dispaxis">
  <dt><b>dispaxis = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='dispaxis' Line='dispaxis = 1' -->
  <dd>The image axis corresponding to the dispersion.  If there is an image
  header keyword DISPAXIS then the value of the keyword will be used
  otherwise this package parameter is used.  The dispersion coordinates
  are a function of column, line, or band when this parameter is 1, 2
  or 3.
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = <span style="font-family: monospace;">"1"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = "1"' -->
  <dd>The number of neighboring elements to sum.  This is a string parameter
  that can have one or two numbers.  For two dimensional images only
  one number is needed and specifies the number of lines or columns
  to sum depending on the dispersion axis.  For three dimensional
  images two numbers may be given (if only one is given it defaults
  to the same value for both spatial axes) to specify the summing of
  the two spatial axes.  The order is the lower dimensional spatial
  axis first.
  For an even value the elements summed are the central specified
  <span style="font-family: monospace;">"aperture"</span>, nsum / 2 - 1 below, and nsum /2 above; i.e the
  central value is closer to the lower element than the upper.
  For example, for nsum=4 and an aperture of 10 for a dispersion
  axis of 1 in a two dimensional image the spectrum used will be
  the sum of lines 9 to 12.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records = ""' -->
  <dd>This is a dummy parameter.  It is applicable only in the <b>imred.irs</b>
  and <b>imred.iids</b> packages.
  </dd>
  </dl>
  <dl id="l_version">
  <dt><b>version = <span style="font-family: monospace;">"ONEDSPEC V3: November 1991"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='version' Line='version = "ONEDSPEC V3: November 1991"' -->
  <dd>Package version identification.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The <b>onedspec</b> package contains generic tasks for the reduction,
  analysis, and display of one dimensional spectra.  The specifics of
  individual tasks may be found in their IRAF <span style="font-family: monospace;">"help"</span> pages.  This document
  describes the general and common features of the tasks.
  </p>
  <p>
  The functions provided in the <b>onedspec</b> package with applicable tasks
  are summarized in Table 1.
  </p>
  <p style="text-align:center">Table 1:  Functions provided in the <b>onedspec</b> package
  
  </p>
  <div class="highlight-default-notranslate"><pre>
  1.  Graphical display of spectra
            bplot - Batch plots of spectra
         identify - Identify features and fit dispersion functions
         specplot - Stack and plot multiple spectra
            splot - Interactive spectral plot/analysis
  
  2.  Determining and applying dispersion calibrations
          dispcor - Dispersion correct spectra
           dopcor - Apply doppler corrections
         identify - Identify features and fit dispersion functions
       refspectra - Assign reference spectra to other spectra
       reidentify - Automatically identify features in spectra
        specshift - Shift spectral dispersion coordinate system
  
  3.  Determining and applying flux calibrations
        calibrate - Apply extinction and flux calibrations to spectra
         deredden - Apply interstellar extinction correction
           dopcor - Apply doppler corrections
           lcalib - List calibration file data
         sensfunc - Create sensitivity function
         standard - Tabulate standard star data
  
  4.  Fitting spectral features and continua
        continuum - Fit the continuum in spectra
         fitprofs - Fit gaussian profiles
             sfit - Fit spectra and output fit, ratio, or difference
            splot - Interactive spectral plot/analysis
  
  5.  Arithmetic and combining of spectra
           sarith - Spectrum arithmetic
         scombine - Combine spectra
            splot - Interactive spectral plot/analysis
  
  6.  Miscellaneous functions
           mkspec - Generate an artificial spectrum
            names - Generate a list of image names from a string
       sapertures - Set or change aperture header information
            scopy - Select and copy spectra
          sinterp - Interpolate a table of x,y to create a spectrum
            slist - List spectrum header parameters
            splot - Interactive spectral plot/analysis
  </pre></div>
  <p>
  There are other packages which provide additional functions or specialized
  tasks for spectra.  Radial velocity measurements are available in the
  <b>noao.rv</b> package.  The <b>noao.imred</b> package contains a number
  of packages for specific types of data or instruments.  These packages
  are listed in Table 2.
  </p>
  <p style="text-align:center">Table 2:  <b>Imred</b> spectroscopy packages
  
  </p>
  <div class="highlight-default-notranslate"><pre>
      argus - CTIO ARGUS reduction package
   ctioslit - CTIO spectrophotometric reduction package
    echelle - Echelle spectral reductions (slit and FOE)
      hydra - KPNO HYDRA (and NESSIE) reduction package
       iids - KPNO IIDS spectral reductions
        irs - KPNO IRS spectral reductions
  kpnocoude - KPNO coude reduction package (slit and 3 fiber)
   kpnoslit - KPNO low/moderate dispersion slits (Goldcam, RCspec, Whitecam)
    specred - Generic slit and fiber spectral reduction package
  </pre></div>
  <p>
  Finally, there are non-NOAO packages which may contain generally useful
  software for spectra.  Currently available packages are <b>stsdas</b>
  and <b>xray</b>.
  </p>
  </section>
  <section id="s_spectrum_image_formats_and_coordinate_systems">
  <h3>Spectrum image formats and coordinate systems</h3>
  <p>
  See the separate help topic <i>specwcs</i>.
  </p>
  </section>
  <section id="s_interpolation">
  <h3>Interpolation</h3>
  <p>
  Changing the dispersion sampling of spectra, such as when converting to a
  constant sampling interval per pixel or a common sampling for combining or
  doing arithmetic on spectra, requires interpolation.  The tasks which
  reinterpolate spectra, if needed, are <b>dispcor, sarith, scombine,</b> and
  <b>splot</b>.
  </p>
  <p>
  The interpolation type is set by the package parameter <i>interp</i>.
  The available interpolation types are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  nearest - nearest neighbor
   linear - linear
    poly3 - 3rd order polynomial
    poly5 - 5th order polynomial
  spline3 - cubic spline
     sinc - sinc function
  </pre></div>
  <p>
  The default interpolation type is a 5th order polynomial.
  </p>
  <p>
  The choice of interpolation type depends on the type of data, smooth
  verses strong, sharp, undersampled features, and the requirements of
  the user.  The <span style="font-family: monospace;">"nearest"</span> and <span style="font-family: monospace;">"linear"</span> interpolation are somewhat
  crude and simple but they avoid <span style="font-family: monospace;">"ringing"</span> near sharp features.  The
  polynomial interpolations are smoother but have noticible ringing
  near sharp features.  They are, unlike the sinc function described
  below, localized.
  </p>
  <p>
  In V2.10 a <span style="font-family: monospace;">"sinc"</span> interpolation option is available.  This function
  has advantages and disadvantages.  It is important to realize that
  there are disadvantages!  Sinc interpolation approximates applying a phase
  shift to the fourier transform of the spectrum.  Thus, repeated
  interpolations do not accumulate errors (or nearly so) and, in particular,
  a forward and reverse interpolation will recover the original spectrum
  much more closely than other interpolation types.  However, for
  undersampled, strong features, such as cosmic rays or narrow emission or
  absorption lines, the ringing can be more severe than the polynomial
  interpolations.  The ringing is especially a concern because it extends
  a long way from the feature causing the ringing; 30 pixels with the
  truncated algorithm used.  Note that it is not the truncation of the
  interpolation function which is at fault!
  </p>
  <p>
  Because of the problems seen with sinc interpolation it should be used with
  care.  Specifically, if there are no undersampled, narrow features it is a
  good choice but when there are such features the contamination of the
  spectrum by ringing is much more severe than with other interpolation
  types.
  </p>
  </section>
  <section id="s_units">
  <h3>Units</h3>
  <p>
  In versions of the NOAO spectroscopy packages prior to V2.10 the dispersion
  units used were restricted to Angstroms.  In V2.10 the first,
  experimental, step of generalizing to other units was taken by
  allowing the two principle spectral plotting tasks, <b>splot</b> and
  <b>specplot</b>, to plot in various units.  Dispersion functions are still
  assumed to be in Angstroms but in the future the generalization will be
  completed to all the NOAO spectroscopy tasks.
  </p>
  <p>
  The dispersion units capability of the plotting tasks allows specifying
  the units with the <span style="font-family: monospace;">"units"</span> task parameter and interactively changing the
  units with the <span style="font-family: monospace;">":units"</span> command.  In addition the <span style="font-family: monospace;">'v'</span> key allows plotting
  in velocity units with the zero point velocity defined by the cursor
  position.
  </p>
  <p>
  The units are specified by strings having a unit type from the list below
  along with the possible preceding modifiers, <span style="font-family: monospace;">"inverse"</span>, to select the
  inverse of the unit and <span style="font-family: monospace;">"log"</span> to select logarithmic units. For example <span style="font-family: monospace;">"log
  angstroms"</span> to plot the logarithm of wavelength in Angstroms and <span style="font-family: monospace;">"inv
  microns"</span> to plot inverse microns.  The various identifiers may be
  abbreviated as words but the syntax is not sophisticated enough to
  recognized standard scientific abbreviations except as noted below.
  </p>
  <div class="highlight-default-notranslate"><pre>
          Table 1:  Unit Types
  
     angstroms - Wavelength in Angstroms
    nanometers - Wavelength in nanometers
  millimicrons - Wavelength in millimicrons
       microns - Wavelength in microns
   millimeters - Wavelength in millimeters
    centimeter - Wavelength in centimeters
        meters - Wavelength in meters
         hertz - Frequency in hertz (cycles per second)
     kilohertz - Frequency in kilohertz
     megahertz - Frequency in megahertz
     gigahertz - Frequency in gigahertz
           m/s - Velocity in meters per second
          km/s - Velocity in kilometers per second
            ev - Energy in electron volts
           kev - Energy in kilo electron volts
           mev - Energy in mega electron volts
             z - Redshift
  
            nm - Wavelength in nanometers
            mm - Wavelength in millimeters
            cm - Wavelength in centimeters
             m - Wavelength in meters
            Hz - Frequency in hertz (cycles per second)
           KHz - Frequency in kilohertz
           MHz - Frequency in megahertz
           GHz - Frequency in gigahertz
            wn - Wave number (inverse centimeters)
  </pre></div>
  <p>
  The velocity and redshift units require a trailing value and unit defining the
  velocity zero point.  For example to plot velocity relative to
  a wavelength of 1 micron the unit string would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  km/s 1 micron
  </pre></div>
  <p>
  Some additional examples of units strings are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  milliang
  megahertz
  inv mic
  log hertz
  m/s 3 inv mic
  z 5015 ang
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  apextract, longslit, rv, imred, specwcs
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'SPECTRUM IMAGE FORMATS AND COORDINATE SYSTEMS' 'INTERPOLATION' 'UNITS' 'SEE ALSO'  -->
  

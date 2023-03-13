.. _disptrans:

disptrans: Transform dispersion units and apply air correction
==============================================================

**Package: onedspec**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  disptrans input output units
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of dispersion calibrated input spectra to be dispersion transformed.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of output dispersion transformed spectra.  If given the input names
  (or a null list), each input spectrum will be replaced by the transformed
  output spectrum.
  </dd>
  </dl>
  <dl id="l_units">
  <dt><b>units</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='units' Line='units' -->
  <dd>Output dispersion units.  A wide range of dispersion units may be
  specified and they are described in the UNITS section.
  </dd>
  </dl>
  <dl id="l_error">
  <dt><b>error = 0.01</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='error' Line='error = 0.01' -->
  <dd>Maximum error allowed in the output dispersion transformation expressed
  as a pixel error; that is, the equivalent pixel shift in the output
  dispersion function corresponding to the maximum difference between
  the exact transformation and the dispersion function approximation.
  The smaller the allowed error the higher the order of dispersion
  function used.
  </dd>
  </dl>
  <dl id="l_linearize">
  <dt><b>linearize = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linearize' Line='linearize = no' -->
  <dd>Resample the spectrum data to linear increments in the output dispersion
  system?  If no then the output dispersion function is stored in the
  spectrum header and if yes the spectrum is resampled into the same
  number of pixels over the same dispersion range but in even steps
  of the output dispersion units.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print a log of each spectrum transformed to the standard output?
  </dd>
  </dl>
  <dl id="l_air">
  <dt><b>air = <span style="font-family: monospace;">"none"</span> (none|air2vac|vac2air)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='air' Line='air = "none" (none|air2vac|vac2air)' -->
  <dd>Apply an air to vacuum or vacuum to air conversion?  It is the
  responsibility of the user to know whether the input dispersion
  is in air or vacuum units and to select the appropriate conversion.
  The conversion types are <span style="font-family: monospace;">"none"</span> for no conversion, <span style="font-family: monospace;">"air2vac"</span> to
  convert from air to vacuum, and <span style="font-family: monospace;">"vac2air"</span> to convert from vacuum
  to air.
  </dd>
  </dl>
  <dl id="l_t">
  <dt><b>t = 15, p = 760, f = 4</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='t' Line='t = 15, p = 760, f = 4' -->
  <dd>Temperature t in degrees C, pressure p in mmHg, and water vapour pressure f
  in mmHg for the air index of refraction.
  </dd>
  </dl>
  <p>
  OTHER PARAMETERS
  </p>
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
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The dispersion function in the input spectra, y = f(x) where x is the
  pixel coordinate and y is the input dispersion coordinate, is
  transformed to y' = g(x) where y' is in the new dispersion units.  This is done
  by evaluating the input dispersion coordinate y at each pixel, applying an
  air to vacuum or vacuum to air conversion if desired, and applying the
  specified unit transformation y' = h(y).  Since the transformations are
  nonlinear functions and the output dispersion function must be expressed in
  polynomial form, the function g(x) is determined by fitting a cubic spline
  to the set of x and y' values.  The lowest number of spline pieces is used
  which satisfies the specified error.  Note that this error is not a random
  error but difference between the smooth fitted function and the smooth
  dispersion function in the header.  As a special case, the first
  fit tried is a linear function.  If this satisfies the error condition
  then a simpler dispersion description is possible.  Also this is
  appropriate for dispersion units which are simply related by a
  scale change such as Angstroms to nanometers or Hertz to Mev.
  </p>
  <p>
  The error condition is that the maximum difference between the exact or
  analytic (the air/vacuum conversion is never exact) transformation and the
  fitted function value at any pixel be less than the equivalent shift in
  pixel coordinate evaluated at that point.  The reason for using an error
  condition in terms of pixels is that it is independent of the dispersion of
  the spectra and the resolution of spectra is ultimately limited by the
  pixel sampling.
  </p>
  <p>
  After the new dispersion function is determined the function is either
  stored in the coordinate system description for the spectrum or used to
  resample the pixels to linear increments in the output dispersion units.
  The resampling is not done if the new dispersion function is already linear
  as noted above.  The sampling uses the mean value over the input spectrum
  covered by an output spectrum pixel (it is flux per unit dispersion element
  preserving as opposed to flux/counts preserving).  The linear sampling
  parameters are limited to producing the same number of output pixels as
  input pixels over the same range of dispersion.  If one wants to have more
  control over the resampling then the <i>linearize</i> parameter should be
  set to no and the task <b>dispcor</b> used on the output spectrum.
  </p>
  <p>
  Note that an alternative to using this task is to do the original
  dispersion calibration (based on calibration spectra) with IDENTIFY
  and DISPCOR in the desired units.  However, currently the standard
  lines lists are in Angstroms.  There are, however, linelists for
  He-Ne-Ar, Th-Ar, and Th in vacuum wavelengths.
  </p>
  </section>
  <section id="s_units">
  <h3>Units</h3>
  <p>
  The dispersion units are specified by strings having a unit type from the
  list below along with the possible preceding modifiers, <span style="font-family: monospace;">"inverse"</span>, to
  select the inverse of the unit and <span style="font-family: monospace;">"log"</span> to select logarithmic units. For
  example <span style="font-family: monospace;">"log angstroms"</span> to select the logarithm of wavelength in Angstroms
  and <span style="font-family: monospace;">"inv microns"</span> to select inverse microns.  The various identifiers may
  be abbreviated as words but the syntax is not sophisticated enough to
  recognized standard scientific abbreviations except for those given
  explicitly below.
  </p>
  <div class="highlight-default-notranslate"><pre>
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
  The velocity units require a trailing value and unit defining the
  velocity zero point.  For example to transform to velocity relative to
  a wavelength of 1 micron the unit string would be:
  </p>
  <div class="highlight-default-notranslate"><pre>
  km/s 1 micron
  </pre></div>
  </section>
  <section id="s_air_vacuum_conversion">
  <h3>Air/vacuum conversion</h3>
  <p>
  The air to vacuum and vacuum to air conversions are obtained by multiplying
  or dividing by the air index of refraction as computed from the
  formulas in Allen's Astrophysical Quantities (p. 124 in 1973 edition).
  These formulas include temperature, pressure, and water vapour terms
  with the default values being the standard ones.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convert a spectrum dispersion calibrated in Angstroms to electron
  volts and resample to a linear sampling.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; disptrans spec1 evspec1 ev linear+
  evspec1: Dispersion transformed to ev.
  </pre></div>
  <p>
  2. Apply an air to vacuum correction to an echelle spectrum using the
  default standard temperature and pressure.  Don't resample but rather use
  a nonlinear dispersion function.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; disptrans highres.ec vac.ec angs air=air2vac
  vac.ec: Dispersion transformed to angstroms in vacuum with
    t = 15. C, p = 760. mmHg, f = 4. mmHg.
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_DISPTRANS">
  <dt><b>DISPTRANS V2.10.4</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DISPTRANS' Line='DISPTRANS V2.10.4' -->
  <dd>New task with this release.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  dispcor, identify, scopy, dopcor
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'UNITS' 'AIR/VACUUM CONVERSION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

.. _dispcor:

dispcor: Dispersion correct spectra
===================================

**Package: hydra**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  dispcor input output [records]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input spectra or root names to be dispersion corrected.  These may
  be echelle or non-echelle spectra, the task will determine which from the
  database dispersion functions.  When using the record number extension
  format, record number extensions will be appended to each root name in the
  list.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>List of dispersion corrected output spectra or root names.  When using the
  record number extension format, record number extensions will be appended
  to each root name in the list.  The output extension will be the same as
  the input extension.  If <span style="font-family: monospace;">"no"</span> output list is specified then the output
  spectrum will replace the input spectrum after dispersion correction.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records (imred.irs and imred.iids only)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records (imred.irs and imred.iids only)' -->
  <dd>List of records or ranges of records to be appended to the input and output
  root names when using record number extension format.  The syntax of this
  list is comma separated record numbers or ranges of record numbers.  A
  range consists of two numbers separated by a hyphen.  A null list may be
  used if no record number extensions are desired.  This is a positional
  query parameter only if the record format is specified.
  </dd>
  </dl>
  <dl id="l_linearize">
  <dt><b>linearize = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='linearize' Line='linearize = yes' -->
  <dd>Interpolate the spectra to a linear dispersion sampling?  If yes, the
  spectra will be interpolated to a linear or log linear sampling using
  the linear dispersion parameters specified by other parameters.  If
  no, the nonlinear dispersion function(s) from the dispersion function
  database are assigned to the input image world coordinate system
  and the spectral data are not interpolated.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"database"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "database"' -->
  <dd>Database containing dispersion solutions created by <b>identify</b> or
  <b>ecidentify</b>.  If the spectra have been previous dispersion corrected
  this parameter is ignored unless a new reference spectra are defined.
  </dd>
  </dl>
  <dl id="l_table">
  <dt><b>table = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table = ""' -->
  <dd>Wavelength coordinate table or reference image.  Elements in this optional
  table or reference image override the wavelength coordinates given below
  for specified apertures.  See the DISCUSSION for additional information.
  </dd>
  </dl>
  <dl id="l_w1">
  <dt><b>w1 = INDEF, w2 = INDEF, dw = INDEF, nw = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='w1' Line='w1 = INDEF, w2 = INDEF, dw = INDEF, nw = INDEF' -->
  <dd>The starting wavelength, ending wavelength, wavelength interval per pixel,
  and the number of pixels in the output spectra.  Any combination of these
  parameters may be used to restrict the wavelength coordinates of the output
  spectra.  If two or more have the value INDEF then suitable defaults based
  on the number of input pixels and the wavelength range of the reference
  dispersion solutions are used.  These defaults may either come from all
  spectra, all spectra of the same aperture, or individually for each
  spectrum depending on the values of the <i>global</i> and <i>samedisp</i>
  parameters.  Note that these parameters are specified in linear units even
  if a logarithmic wavelength scale is selected.  The conversion between
  linear and logarithmic intervals between pixels is given below.  These
  values may be overridden for specified apertures by a wavelength table or
  reference image.  Otherwise these values apply to all apertures.
  </dd>
  </dl>
  <dl id="l_log">
  <dt><b>log = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='log' Line='log = no' -->
  <dd>Transform to linear logarithmic wavelength coordinates?  Linear logarithmic
  wavelength coordinates have wavelength intervals which are constant
  in the logarithm (base 10) of the wavelength.  Note that if conserving flux
  this will change the flux units to flux per log lambda interval.
  Note that if the input spectra are in log sampling then <i>log</i>=no will
  resample back to linear sampling and <i>log</i>=yes will resample keeping
  the output spectra in log sampling.
  </dd>
  </dl>
  <dl id="l_flux">
  <dt><b>flux = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='flux' Line='flux = yes' -->
  <dd>Conserve the total flux during interpolation rather than the flux density?
  If <span style="font-family: monospace;">"no"</span>, the output spectrum is average of the input spectrum across each
  output wavelength coordinate.  This conserves flux density.  If <span style="font-family: monospace;">"yes"</span> the
  input spectrum is integrated over the extent of each output pixel.  This
  conserves the total flux.  Note that in this case units of the flux will
  change; for example rebinning to logarithmic wavelengths will produce flux
  per log lambda.  For flux calibrated data you most likely would not want to
  conserve flux.
  </dd>
  </dl>
  <dl id="l_blank">
  <dt><b>blank = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='blank' Line='blank = 0.' -->
  <dd>Output value corresponding to points outside the range of the input
  data.  In other words, the out of bounds value.  This only has an
  effect when linearizing and the output spectral coordinates extend
  beyond the input spectral range.
  </dd>
  </dl>
  <dl id="l_samedisp">
  <dt><b>samedisp = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='samedisp' Line='samedisp = no' -->
  <dd>Use the same dispersion parameters for all apertures?  If yes then all
  apertures in a single image will have the same dispersion parameters.
  If the <i>global</i> parameter is all selected then all spectra in all
  images will have the same dispersion paramters.  This parameter
  would not normally be used with echelle spectra where each order
  has a different wavelength coverage.
  </dd>
  </dl>
  <dl id="l_global">
  <dt><b>global = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='global' Line='global = no' -->
  <dd>Apply global wavelength defaults?  Defaults for the INDEF wavelength
  coordinate parameters are determined if two or less of the wavelength
  parameters are specified.  The defaults are based on the number of
  pixels and the wavelengths of the first and last pixel as given by the
  dispersion solution.  If this parameter is <span style="font-family: monospace;">"no"</span> this is done
  independently for each input spectrum.  If this parameter is <span style="font-family: monospace;">"yes"</span>
  then the maximum number of pixels and the minimum and maximum
  wavelengths of all the input spectra or those of the same aperture are
  used to provide defaults for the spectra.  The parameter
  <i>samedisp</i> determines whether the global coordinates are over all
  spectra or only those with the same aperture number.  The global option
  is used to have all the dispersion corrected spectra have the same
  wavelength coordinates without actually specifying the wavelength
  parameters.
  </dd>
  </dl>
  <dl id="l_ignoreaps">
  <dt><b>ignoreaps = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ignoreaps' Line='ignoreaps = no' -->
  <dd>If a reference dispersion solution is not found for an aperture
  use the first reference dispersion solution and ignore the aperture
  number?  If not ignoring the apertures all spectra must have a matching
  aperture for the dispersion solution and the task aborts if this is
  not the case.  Ignoring the apertures avoids this abort and instead
  the first dispersion solution is used.  Note this parameter does not
  mean ignore matches between reference and spectrum aperture numbers
  but only ignore the aperture number if no matching reference is
  found.
  Also if a reference table or image is given and <i>ignoreaps</i>=yes
  then the default dispersion parameters for any aperture not defined
  by the table or image will be that of the first defined aperture.
  This can still be overridden by giving explicit values for
  <i>w1, w2, dw</i> and <i>nw</i>.
  </dd>
  </dl>
  <dl id="l_confirm">
  <dt><b>confirm = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='confirm' Line='confirm = no' -->
  <dd>Confirm the wavelength parameters for each spectrum?  If <i>yes</i>
  the wavelength parameters will be printed and the user will be asked
  whether to accept them.  If the parameters are not acceptable the
  user will be queried for new values.  The confirmation and parameter
  changes are repeated until an acceptable set of parameters is obtained.
  When the <i>global</i> parameter is <i>yes</i> changes to the wavelength
  parameters will remain in effect until changed again.
  </dd>
  </dl>
  <dl id="l_listonly">
  <dt><b>listonly = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='listonly' Line='listonly = no' -->
  <dd>List the dispersion coordinates only?  If set then the dispersion coordinates
  are listed but the spectra are not dispersion corrected.  This may be used
  to determine what the default wavelengths would be based on the dispersion
  solutions.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print the dispersion function and coordinate assignments?
  </dd>
  </dl>
  <dl id="l_logfile">
  <dt><b>logfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfile' Line='logfile = ""' -->
  <dd>Log file for recording the dispersion correction operations.  If no file
  name is given then no log information is recorded.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The dispersion coordinate systems of the input spectra are set or changed
  in the output spectra.  The output spectra may be the same as the input
  spectra if no output spectra are specified or the output name is the
  same as the input name.  The input and output spectra are specified
  by image templates or lists.  In the <b>irs/iids</b> packages the
  input and output spectra are specified as root names and the record
  numbers are specified by the <i>record</i> parameter.  The records are
  given as a set of comma separate single numbers or ranges of hyphen
  separated numbers.  If no records are specified then the input and output
  images are assumed to be full names.
  </p>
  <p>
  The dispersion coordinate system is defined either in the image header or
  by dispersion functions in the specified database.  To use reference
  spectra dispersion functions they must first be assigned to the image with
  <b>identify (reidentify)</b>, <b>ecidentify (ecreidentify)</b>,
  <b>refspectra</b>, or <b>hedit</b>.  These tasks define the image header
  keywords REFSPEC1, REFSPEC2, REFSHFT1, and REFSHFT2.  The test which
  determines whether to use the current dispersion coordinate system or
  reference spectra dispersion solutions is the presence of the REFSPEC1
  keyword.  Since it is an error to apply a dispersion function to data which
  have already been dispersion corrected the any dispersion function keywords
  are deleted after use and a record of them entered in sequential image
  header keywords beginning with DCLOG.
  </p>
  <p>
  Dispersion functions are specified by one or both of the reference spectrum
  image header keywords REFSPEC1 and REFSPEC2 containing the name of
  calibration spectra with dispersion function solutions (either echelle
  dispersion functions from <b>ecidentify</b> or non-echelle dispersion
  functions from <b>identify</b>) in the database.  There must be a dispersion
  function for each aperture in the input spectrum unless the <i>ignoreaps</i>
  flag is set.  If the flag is not set the task will abort if a matching
  aperture is not found while if it is set spectra without a matching
  aperture in the reference dispersion solutions will use the first
  dispersion solution.  Note that aperture number matching is done in both
  cases and the <i>ignoreaps</i> parameter only applies to non-matching
  spectra.  The common situation for using the <i>ignoreaps</i> option is when
  there is a single reference dispersion solution which is to be applied to a
  number of spectra with different aperture numbers; hence effectively
  ignoring the reference spectrum aperture number.
  </p>
  <p>
  If two reference spectra are specified the names may be followed by a
  weighting factor (assumed to be 1 if missing).  The wavelength of a pixel
  is then the weighted averge of the wavelengths of the two dispersion
  functions.  The task <b>refspectra</b> provides a number of ways to assign
  reference spectra.  Note, however, that these assignments may be made
  directly using the task <b>hedit</b> or with some other task or script if
  none of the methods are suitable.  Also note that <b>identify</b> and
  <b>reidentify</b> add the REFSPEC1 keyword refering to the image itself
  when a database entry is written.
  </p>
  <p>
  In addition to the one or two reference dispersion functions for each input
  aperture there may also be image header keywords REFSHFT1 and REFSHFT2
  specifying reference spectra whose dispersion function zero point shifts
  (the <span style="font-family: monospace;">"shift"</span> parameter in the database files) are to be applied to the
  reference dispersion functions.  The shifts from REFSHFT1 will be applied
  to the dispersion functions from REFSPEC1 and similarly for the second
  dispersion functions.  The reference shifts need not be present for every
  aperture in a multispectrum image.  By default the mean shift from all the
  reference apertures having a zero point shift is applied to all the
  reference dispersion functions.  If the REFSHFT keyword has the modifier
  word <span style="font-family: monospace;">"nearest"</span> following the spectrum name then the shift from the nearest
  aperture in spatial position (from the aperture extraction limits in the
  original 2D spectrum as recorded in the 6th and 7th fields of the APNUM
  keywords) is used for a particular input aperture.  If the modifier word is
  <span style="font-family: monospace;">"interp"</span> then the nearest two apertures are used to interpolate a zero
  point shift spatially.
  </p>
  <p>
  The purpose of the reference shift keywords is to apply a wavelength zero
  point correction to the reference dispersion functions determined from
  separate arc calibration observations using a few apertures taken at the
  same time as object observations.  For example, consider multifiber
  observations in which one or more fibers are assigned to arc lamps at the
  same time the other fibers are used to observe various objects.  The basic
  dispersion reference, the REFSPEC keywords, will come from arc observations
  taken through all the fibers.  The arc fibers used during an object
  observation are then calibrated against their corresponding fibers in the
  arc calibration observations to determine a zero point shift.  The REFSHFT
  keywords will contain the name of the object spectrum itself and the shifts
  from the simultaneous arc fibers will be interpolated spatially to the
  nonarc object fibers and applied to the dispersion functions from the arc
  calibrations for those fibers.
  </p>
  <p>
  The reference shift keywords are currently added with <b>hedit</b> and zero
  point shifts computed with <b>identify/reidentify</b>.  The complexities of
  this have been hidden in the multifiber <b>imred</b> instrument reduction
  packages.  The reference shift correction feature was added primarily for
  use in those reduction packages.
  </p>
  <p>
  If the <i>linearize</i> parameter is no the dispersion functions, weights,
  and shifts are transferred from the database to the world coordinate system
  keywords in the image header.  Except for printing processing information
  that is all that is done to the spectra.
  </p>
  <p>
  If the <i>linearize</i> parameter is yes the spectra are interpolated to a
  linear wavelength scale and the dispersion coordinate system in the header
  is set apprpriately.  A linear wavelength coordinate system is defined by a
  starting wavelength, an ending wavelength, a wavelength interval per pixel,
  and the number of pixels.  These four parameters actually overspecify the
  coordinate system and only three of these values are needed to define it.
  The output coordinate system is specified by giving a set or subset of
  these parameters using the parameters <i>w1</i>, <i>w2</i>, <i>dw</i>, and
  <i>nw</i>.
  </p>
  <p>
  When the <i>log</i> option is used these parameters are still specified and
  computed in non-log units but the effective interval per pixel is
  </p>
  <div class="highlight-default-notranslate"><pre>
  dw_log = (log10(w2) - log10(w1)) / (nw - 1)
  dw_log = (log10(w1+dw*(nw-1)) - log10(w1)) / (nw - 1)
  </pre></div>
  <p>
  In other words, the logarithmic interval divides the starting and ending
  wavelength into the required number of pixels in log step.  To avoid
  confusion in this case it is best to specify the starting and ending
  wavelengths (in non-log units) and the number of pixels.
  </p>
  <p>
  Note that if <i>log</i>=yes the input spectra in either linear
  or log sampling will be resampled to produces an output spectrum in
  log sampling.  Similarly, if <i>log</i>=no the input spectra will
  be resampled to linear sampling.  This means that log sampled input
  spectra will be resampled to linear sampling.
  </p>
  <p>
  Default values for any parameters which are not specified, by using the
  value INDEF, are supplied based on the wavelengths of the first and last
  pixel as given by the dispersion function and the number of pixels in the
  input image.  The defaults may either be determined separately for each
  spectrum (<i>global</i> = <i>no</i>), from all spectra with the same aperture
  (<i>global</i> = <i>yes</i> and <i>samedisp</i> = <i>no</i>), or from all the
  spectra (<i>global</i> = <i>yes</i> and <i>samedisp</i> = <i>yes</i>).  As
  indicated, the parameter <i>samedisp</i> determines whether defaults are
  determined independently for each aperture or set the same for all
  apertures.
  </p>
  <p>
  Another way to specify the wavelengths when there are many apertures is to
  use a wavelength table or reference image.  If an spectrum image name is
  specified with the <i>table</i> parameter then the dispersion parameters for
  each apertures are set to be the same as the reference spectrum.
  Alternatively, a text file table consisting of lines containing an aperture
  number, the starting wavelength, the ending wavelength, the wavelength
  interval per pixel, and the number of output pixels may be specified.  Any
  of these values may be specified as INDEF (though usually the aperture
  number is not).  One way to view the wavelength table/reference spectrum is
  that an entry in the wavelength table/reference spectrum overrides the
  values of the parameters <i>w1</i>, <i>w2</i>, <i>dw</i>, and <i>nw</i>, which
  normally apply to all apertures, for the specified aperture.  The
  wavelength table is used to specify explicit independent values for
  apertures.  The global mechanism can supply independent values for the
  INDEF parameters when the <i>samedisp</i> parameter is no.
  </p>
  <p>
  If one wishes to verify and possibly change the defaults assigned,
  either globally or individually, the <i>confirm</i> flag may be set.  The
  user is asked whether to accept these values.  By responding with no the
  user is given the chance to change each parameter value.  Then the new
  parameters are printed and the user is again asked to confirm the
  parameters.  This is repeated until the desired parameters are set.  When
  the defaults are not global the changed parameters will not be used for the
  next spectrum.  When the global option is used any changes made are
  retained (either for all apertures or independently for each aperture)
  until changed again.
  </p>
  <p>
  When adjusting the wavelengths the user should specify which parameter is
  free to change by entering INDEF.  If none of the parameters are specified
  as INDEF then those values which were not changed, i.e. by accepting the
  current value, are the first to be changed.
  </p>
  <p>
  Once the wavelength scale has been defined the input spectrum is
  interpolated for each output pixel.  Output wavelengths outside the range
  of the input spectrum are set to the value given by the <i>blank</i> parameter
  value.  The default interpolation function
  is a 5th order polynomial.  The choice of interpolation type is made
  with the package parameter <span style="font-family: monospace;">"interp"</span>.  It may be set to <span style="font-family: monospace;">"nearest"</span>,
  <span style="font-family: monospace;">"linear"</span>, <span style="font-family: monospace;">"spline3"</span>, <span style="font-family: monospace;">"poly5"</span>, or <span style="font-family: monospace;">"sinc"</span>.  Remember that this
  applies to all tasks which might need to interpolate spectra in the
  <b>onedspec</b> and associated packages.  For a discussion of interpolation
  types see <b>onedspec</b>.
  </p>
  <p>
  When it is desired to conserve total flux, particularly when the dispersion is
  significantly reduced, the parameter <i>flux</i> is set to yes and the
  output pixel value is obtained by integrating the interpolation function
  across the wavelength limits of the output pixel.  If it is set to no
  then the flux density is conserved by averaging across the output pixel
  limits.
  </p>
  <p>
  The input spectrum name, reference spectra, and the wavelength parameters
  will be printed on the standard output if the <i>verbose</i> parameter is
  set and printed to a log file if one is specified with the <i>logfile</i>
  parameter.  If one wishes to only check what wavelengths will be determined
  for the defaults without actually dispersion correcting the spectra the
  <i>listonly</i> flag may be set.
  </p>
  <p>
  Other tasks which may be used to change the dispersion coordinate system
  are <b>scopy</b>, <b>specshift</b>, and <b>sapertures</b>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  In the examples when the task is used in the IRS and IIDS packages,
  shown with the <span style="font-family: monospace;">"ir&gt;"</span> prompt the spectra have a record number extension
  image name format and the records parameter must be specified.  In
  the other case shown with the <span style="font-family: monospace;">"on&gt;"</span> prompt the records parameter is
  not used.
  </p>
  <p>
  1.  Dispersion correct spectra so that they have the same number of pixels
  and the wavelengths limits are set by the reference spectra.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ir&gt; dispcor spec dcspec 9,10,447-448
  dcspec.0009: ap = 0, w1 = 5078.84, w2 = 6550.54, dw = 1.797, nw = 820
  dcspec.0010: ap = 1, w1 = 5078.71, w2 = 6552.81, dw = 1.800, nw = 820
  dcspec.0447: ap = 0, w1 = 5082.57, w2 = 6551.45, dw = 1.794, nw = 820
  dcspec.0448: ap = 1, w1 = 5082.03, w2 = 6553.66, dw = 1.797, nw = 820
  
  on&gt; dispcor allspec.ms dcallspec.ms
  dcallspec.ms: ap = 1, w1 = 5078.84, w2 = 6550.54, dw = 1.797, nw = 820
  dcallspec.ms: ap = 2, w1 = 5078.71, w2 = 6552.81, dw = 1.800, nw = 820
  dcallspec.ms: ap = 3, w1 = 5082.57, w2 = 6551.45, dw = 1.794, nw = 820
  dcallspec.ms: ap = 4, w1 = 5082.03, w2 = 6553.66, dw = 1.797, nw = 820
  </pre></div>
  <p>
  2.  Confirm and change assignments.
  </p>
  <div class="highlight-default-notranslate"><pre>
  on&gt; dispcor spec* %spec%new%* confirm+
  new009: ap = 0, w1 = 5078.84, w2 = 6550.54, dw = 1.797, nw = 820
    Change wavelength coordinate assignments? (yes):
    Starting wavelength (5078.8421234): 5070
    Ending wavelength (6550.535123):
    Wavelength interval per pixel (1.79693812):
    Number of output pixels (820): INDEF
  new009: ap = 0, w1 = 5070., w2 = 6550.53, dw = 1.795, nw = 826
    Change wavelength coordinate assignments? (yes): no
  new010: ap = 1, w1 = 5078.71, w2 = 6552.81, dw = 1.800, nw = 820
    Change wavelength coordinate assignments? (no): yes
    Starting wavelength (5078.7071234): 5100
    Ending wavelength (6550.805123): 6500
    Wavelength interval per pixel (1.79987512): INDEF
    Number of output pixels (820): INDEF
  new010: ap = 1, w1 = 5100., w2 = 6500., dw = 1.797, nw = 780
    Change wavelength coordinate assignments? (yes): no
  new447: ap = 0, w1 = 5082.57, w2 = 6551.45, dw = 1.793, nw = 820
    Change wavelength coordinate assignments? (yes): no
  new448: ap = 1, w1 = 5082.03, w2 = 6553.66, dw = 1.797, nw = 820
    Change wavelength coordinate assignments? (no):
  </pre></div>
  <p>
  3. Confirm global assignments and do dispersion correction in place.
  record format.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ir&gt; dispcor irs "" 9,10,447,448 confirm+ global+ samedisp+
  irs.0009: ap = 0, w1 = 5078.71, w2 = 6553.66, dw = 1.801, nw = 820
    Change wavelength coordinate assignments? (yes):
    Starting wavelength (5078.7071234): 5100
    Ending wavelength (6553.664123): 6500
    Wavelength interval per pixel (1.80092412):
    Number of output pixels (820):
  irs.0009: ap = 0, w1 = 5100., w2 = 6500., dw = 1.799, nw = 779
    Change wavelength coordinate assignments? (yes): no
  irs.0010: ap = 1, w1 = 5100., w2 = 6500., dw = 1.799, nw = 779
    Change wavelength coordinate assignments? (no):
  irs.0447: ap = 0, w1 = 5100., w2 = 6500., dw = 1.799, nw = 779
    Change wavelength coordinate assignments? (no):
  irs.0448: ap = 1, w1 = 5100., w2 = 6500., dw = 1.799, nw = 779
    Change wavelength coordinate assignments? (no):
  </pre></div>
  <p>
  4. Make a nonlinear dispersion correction in place.
  </p>
  <div class="highlight-default-notranslate"><pre>
  on&gt; dispcor spec* ""  linearize=no verbose- logfile=logfile
  </pre></div>
  <p>
  5. Apply a single dispersion solution to a set of record number format
  images.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ir&gt; dispcor nite101 dcnite101 "1-10" ignore+ confirm-
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_DISPCOR">
  <dt><b>DISPCOR V2.12.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DISPCOR' Line='DISPCOR V2.12.3' -->
  <dd>Added the blank parameter value.
  </dd>
  </dl>
  <dl id="l_DISPCOR">
  <dt><b>DISPCOR V2.11.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DISPCOR' Line='DISPCOR V2.11.3' -->
  <dd>Long slit and data cubes can be used with this task to either resample
  using the existing WCS or to use a single dispersion function from
  IDENTIFY.  It uses the first one found.
  </dd>
  </dl>
  <dl id="l_DISPCOR">
  <dt><b>DISPCOR V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DISPCOR' Line='DISPCOR V2.10.3' -->
  <dd>Provision was added for IDENTIFY dispersion solutions consisting of
  only a shift (as produced by the <span style="font-family: monospace;">'g'</span> key in IDENTIFY or the refit=no
  flag in REIDENTIFY) to be applied to previously LINEARIZED spectra.
  Thus it is possible to use IDENIFY/REIDENTIFY to automatically
  compute a zero point shift based on 1 or more lines and then shift
  all the spectra to that zero point.
  DISPCOR will now allow multiple uses of IDENTIFY dispersion solutions
  in a simple way with but with continuing protection against accidental
  multiple uses of the same dispersion solutions.  When a spectrum is
  first dispersion corrected using one or more reference spectra keywords
  the dispersion flag is set and the reference spectra keywords are moved to
  DCLOGn keywords.  If DISPCOR is called again without setting new
  reference spectra keywords then the spectra are resampled (rebinned)
  using the current coordinate system.  If new reference spectra are set
  then DISPCOR will apply these new dispersion functions.  Thus the user
  now explicitly enables multiple dispersion functions by adding
  reference spectra keywords and DISPCOR eliminates accidental multiple
  uses of the same dispersion function by renaming the reference
  spectra.  The renamed keywords also provide a history.
  The flux conservation option now computes an average across the
  output pixel rather than interpolating to the middle of the output
  pixel when <i>flux</i> is no.  This preserves the flux density and
  includes all the data; i.e. a coarse resampling will not eliminate
  features which don't fall at the output pixel coordinates.
  Some additional log and verbose output was added to better inform the
  user about what is done.
  Better error information is now printed if a database dispersion function
  is not found.
  </dd>
  </dl>
  <dl id="l_DISPCOR">
  <dt><b>DISPCOR V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='DISPCOR' Line='DISPCOR V2.10' -->
  <dd>This is a new version with many differences.  It replaces the previous
  three tasks <b>dispcor, ecdispcor</b> and <b>msdispcor</b>.  It applies both
  one dimensional and echelle dispersion functions.  The new parameter
  <i>linearize</i> selects whether to interpolate the spectra to a uniform
  linear dispersion (the only option available previously) or to assign a
  nonlinear dispersion function to the image without any interpolation.  The
  interpolation function parameter has been eliminated and the package
  parameter <i>interp</i> is used to select the interpolation function.  The
  new interpolation type <span style="font-family: monospace;">"sinc"</span> may be used but care should be exercised.
  The new task supports applying a secondary zero point shift spectrum to a
  master dispersion function and a spatial interpolation of the shifts when
  calibration spectra are taken at the same time on a different region of the
  same 2D image.  The optional wavelength table may now also be an image to
  match dispersion parameters.  The <i>apertures</i> and <i>rebin</i>
  parameters have been eliminated.  If an input spectrum has been previously
  dispersion corrected it will be resampled as desired.  Verbose and log file
  parameters have been added to log the dispersion operations as desired.
  The record format syntax is available in the <b>irs/iids</b> packages.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  package, refspectra, scopy, specshift, sapertures
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

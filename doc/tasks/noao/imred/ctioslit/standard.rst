.. _standard:

standard: Identify standard stars to be used in sensitivity calc
================================================================

**Package: ctioslit**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  standard input [records] output
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input standard star spectra or root names if using the record number
  extension format.  All spectra of the same aperture must be of the same
  standard star.  In beam switch mode or when the same star parameter is set
  all spectra must be of the same standard star regardless of aperture number.
  Normally the spectra will not be extinction corrected but if they are
  then the extinction file should also be given and the same extinction
  file should be used with <b>sensfunc</b>.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records (imred.irs and imred.iids only)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records (imred.irs and imred.iids only)' -->
  <dd>List of records or ranges of records to be appended to the input spectra
  names when using record number extension format.  The
  syntax of this list is comma separated record numbers or ranges of record
  numbers.  A range consists of two numbers separated by a hyphen.
  A null list may be used if no record number extensions are
  desired.  This is a positional query parameter only if the record
  format is specified.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The name of a text file which will contain the output from <b>standard</b>.
  Each execution of <b>standard</b> appends to this file information about the
  standard stars, the calibration bandpasses, and observed counts (see the
  DESCRIPTION section for more details).  The output must be explicitly
  deleted by the user if the filename is to be reused.
  </dd>
  </dl>
  <dl id="l_samestar">
  <dt><b>samestar = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='samestar' Line='samestar = yes' -->
  <dd>Is the same star in all apertures?  If set to no then each aperture may
  contain a different standard star.  The standard star name is queried
  each time a new aperture is encountered.  Note that this occurs only
  once per aperture and multiple spectra with the same aperture number
  must be of the same star.  If set to yes the standard star name is only
  queried once.  When in beam switch mode this parameter is ignored since
  all apertures must contain the same star.
  </dd>
  </dl>
  <dl id="l_beam_switch">
  <dt><b>beam_switch = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='beam_switch' Line='beam_switch = no' -->
  <dd>Beam switch the spectra?  If yes then a beam switch mode is used for the spectra
  in which successive pairs of object and sky observations from the same aperture
  are sky subtracted.  This requires that the object type flag OFLAG be present
  and that the spectra are appropriately ordered.  All object observations must be
  of the same standard star and the <i>samestar</i> parameter is ignored.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>List of apertures to be selected from the input list of spectra.  If no list
  is specified then all apertures are selected.  The syntax is the same as the
  record number extensions.
  </dd>
  </dl>
  <dl id="l_bandwidth">
  <dt><b>bandwidth = INDEF, bandsep = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='bandwidth' Line='bandwidth = INDEF, bandsep = INDEF' -->
  <dd>Bandpass widths and separations in wavelength units.  If INDEF then the
  default bandpasses are those given in the standard star calibration
  file.  If values for these parameters are specified then a default set
  of bandpasses of equal width and separation are defined over the range
  of the input spectrum.  In both cases the default bandpasses can be
  changed interactively if desired.
  </dd>
  </dl>
  <dl id="l_fnuzero">
  <dt><b>fnuzero = 3.68e-20</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fnuzero' Line='fnuzero = 3.68e-20' -->
  <dd>The absolute flux per unit frequency at an AB magnitude of zero.  This is used
  to convert the calibration  AB magnitudes to absolute flux by the formula
  <div class="highlight-default-notranslate"><pre>
  f_nu = fnuzero * 10. ** (-0.4 * m_AB)
  </pre></div>
  The flux units are also determined by this parameter.  However, the
  frequency to wavelength interval conversion assumes frequency in hertz.
  The default value is based on a calibration of Vega at 5556 Angstroms of
  3.52e-20 ergs/cm2/s/Hz for an AB magnitude of 0.0336.  This default value
  is that used in earlier versions of this task which did not allow the
  user to change this calibration.
  </dd>
  </dl>
  <dl id="l_extinction">
  <dt><b>extinction = &lt;no default&gt;</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extinction' Line='extinction = &lt;no default&gt;' -->
  <dd>Extinction file used to make second order extinction corrections across
  the bandpasses.  The default value is  redirected to the package
  parameter of the same name.  See <b>lcalib</b> for a list of standard
  extinction files.  Normally the input spectra will not be extinction
  corrected.  But if they are this file will be used to remove the
  extinction and then the same file should be specified in <b>sensfunc</b>.
  Note that one can choose to use a null extinction file in both.
  </dd>
  </dl>
  <dl id="l_caldir">
  <dt><b>caldir = <span style="font-family: monospace;">")_.caldir"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='caldir' Line='caldir = ")_.caldir"' -->
  <dd>Calibration directory containing standard star data.  The
  default value of <span style="font-family: monospace;">")_.caldir"</span> means to use the package parameter <span style="font-family: monospace;">"caldir"</span>.
  A list of standard calibration directories may be obtained by listing the
  file <span style="font-family: monospace;">"onedstds$README"</span>; for example:
  <div class="highlight-default-notranslate"><pre>
  cl&gt; page onedstds$README
  </pre></div>
  The user may copy or create their own calibration files and specify the
  directory.  The directory <span style="font-family: monospace;">""</span> refers to the current working directory.  The
  standard calibration directory for blackbody curves is
  <span style="font-family: monospace;">"onedstds$blackbody/"</span>.
  </dd>
  </dl>
  <dl id="l_observatory">
  <dt><b>observatory = <span style="font-family: monospace;">")_.observatory"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observatory' Line='observatory = ")_.observatory"' -->
  <dd>Observatory at which the spectra were obtained if not specified in the
  image header by the keyword OBSERVAT.  The default is a redirection to look
  in the parameters for the parent package for a value.  The observatory may
  be one of the observatories in the observatory database, <span style="font-family: monospace;">"observatory"</span> to
  select the observatory defined by the environment variable <span style="font-family: monospace;">"observatory"</span> or
  the parameter <b>observatory.observatory</b>, or <span style="font-family: monospace;">"obspars"</span> to select the
  current parameters set in the <b>observatory</b> task.  See help for
  <b>observatory</b> for additional information.
  </dd>
  </dl>
  <dl id="l_interact">
  <dt><b>interact = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interact' Line='interact = no' -->
  <dd>If set to no, then the default wavelength set (either that from the star
  calibration file or the set given by the <i>bandwidth</i> and <i>bandsep</i>
  parameters) is used to select wavelength points along the spectrum where the
  sensitivity is measured. If set to yes, the spectra may be plotted
  and the bandpasses adjusted.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Graphics output device for use with the interactive mode.  Normally this is
  the user's graphics terminal.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Graphics cursor input for use with the interactive mode.  When null the
  standard graphics cursor is used otherwise the specified file is used.
  </dd>
  </dl>
  <dl id="l_star_name">
  <dt><b>star_name</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='star_name' Line='star_name' -->
  <dd>The name of the star observed in the current series of spectra.  Calibration
  data for the star must be in the specified calibration directory <span style="font-family: monospace;">"caldir"</span>.
  This is normally a interactive query parameter and should not be specified on
  the command line unless all spectra are of the same standard star.
  </dd>
  </dl>
  <p>
  The following three queried parameters apply if the selected calibration
  file is for a blackbody.
  </p>
  <dl id="l_mag">
  <dt><b>mag</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='mag' Line='mag' -->
  <dd>The magnitude of the observed star in the band given by the
  <i>magband</i> parameter.  If the magnitude is not in the same band as
  the blackbody calibration file then the magnitude may be converted to
  the calibration band provided the <span style="font-family: monospace;">"params.dat"</span> file containing relative
  magnitudes between the two bands is in the calibration directory
  </dd>
  </dl>
  <dl id="l_magband">
  <dt><b>magband</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='magband' Line='magband' -->
  <dd>The standard band name for the input magnitude.  This should generally
  be the same band as the blackbody calibration file.  If it is
  not the magnitude will be converted to the calibration band.
  </dd>
  </dl>
  <dl id="l_teff">
  <dt><b>teff</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='teff' Line='teff' -->
  <dd>The effective temperature (deg K) or the spectral type of the star being
  calibrated.  If a spectral type is specified a <span style="font-family: monospace;">"params.dat"</span> file must exist
  in the calibration directory.  The spectral types are specified in the same
  form as in the <span style="font-family: monospace;">"params.dat"</span> file.  For the standard blackbody calibration
  directory the spectral types are specified as A0I, A0III, or A0V, where A
  can be any letter OBAFGKM, the single digit subclass is between 0 and 9,
  and the luminousity class is one of I, III, or V.  If no luminousity class
  is given it defaults to dwarf.
  </dd>
  </dl>
  <p>
  The following two parameters are queried if the image does not contain
  the information.
  </p>
  <dl id="l_airmass">
  <dt><b>airmass, exptime</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='airmass' Line='airmass, exptime' -->
  <dd>If the airmass and exposure time are not in the header nor can they be
  determined from other keywords in the header then these query parameters
  are used to request the airmass and exposure time.  The values are updated
  in the image.
  </dd>
  </dl>
  <p>
  The following parameter is for the task to make queries.
  </p>
  <dl id="l_answer">
  <dt><b>answer</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='answer' Line='answer' -->
  <dd>Interactive query parameter.
  </dd>
  </dl>
  </section>
  <section id="s_cursor_keys">
  <h3>Cursor keys</h3>
  <div class="highlight-default-notranslate"><pre>
  ?  Display help page
  a  Add a new band by marking the endpoints
  d  Delete band nearest the cursor in wavelength
  r  Redraw current plot
  q  Quit with current bandpass definitions
  w  Window plot  (follow with <span style="font-family: monospace;">'?'</span> for help)
  I  Interrupt task immediately
  
  :show   Show current bandpass data
  </pre></div>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Observations of standard stars are integrated over calibration bandpasses
  and written to an output file along with the associated calibration
  fluxes.  The fluxes are obtained from tabulated standard star calibration
  files or a model flux distribution (currently just a blackbody) based on
  the magnitude and spectral type of the star.  The output data is used by
  the task <b>sensfunc</b> to determine the detector sensitivity function and
  possibly the extinction.  The spectra are required to be dispersion
  corrected.  The input spectra may be in either <span style="font-family: monospace;">"onedspec"</span> or <span style="font-family: monospace;">"echelle"</span>
  format and may have many different observation apertures.  The spectra may
  also be beam switched and use the a record number extension format.
  </p>
  <p>
  The input spectra are specified by a list of names or root names if using
  the record number extension format.  In the latter case each name in the
  list has each of the specified record numbers appended.  A subset of the
  input spectra may be selected by their aperture numbers using the parameter
  <i>apertures</i>.  The spectrum name, aperture number, and title are printed
  to the standard output.  The airmass is required but if absent from the image
  header it may be computed from the observation header parameters and the
  latitude task parameter (normally obtained from the <b>observatory</b> task).
  If the airmass cannot be computed, due to missing keywords, then a
  query is made for the airmass.  The airmass is then updated in the header.
  </p>
  <p>
  The name of the standard star or blackbody curve is obtained by querying
  the user.  If the parameter <i>samestar</i> is yes or beam switch mode is
  selected then all spectra are assumed to be of the same standard star and
  the query is made once.  If the parameter is no then a query is made for
  each aperture.  This allows each aperture to contain a different standard
  star.  Note however that multiple observations with the same aperture
  number must be of the same standard star.
  </p>
  <p>
  The standard star name is either the name of an actual standard star or of
  a blackbody calibration.  The latter generally have a star name consisting
  of just the standard bandpass identifier.  If the standard star name is not
  recognized a menu of the available standard stars in the calibration
  directory, the file <span style="font-family: monospace;">"standards.men"</span>, is printed and then the query is
  repeated.  Thus, to get a list you can type ?  or help.
  </p>
  <p>
  The standard star names must map to a file containing tabulated
  calibration data.  The calibration filename is formed from the star
  name with blanks, <span style="font-family: monospace;">"+"</span>, and <span style="font-family: monospace;">"-"</span> removed, converted to lower case, and
  the extension <span style="font-family: monospace;">".dat"</span> added.  This name is appended to a calibration
  directory, so the directory name must have an appropriate directory
  delimiter such as <span style="font-family: monospace;">"$"</span> or <span style="font-family: monospace;">"/"</span>.  Generally one of the system calibration
  directories is used but one may copy and modify or create new
  calibration files in a personal directory.  For the current working
  directory the calibration directory is either null or <span style="font-family: monospace;">"./"</span>.
  </p>
  <p>
  The calibration files may include comment parameter information consisting
  of the comment character <span style="font-family: monospace;">'#'</span>, a parameter name, and the parameter value.
  These elements are separated by whitespace.  Any other comment where the
  first word does not match one of the allowed parameter names is ignored by
  the program.  The parameter names are <span style="font-family: monospace;">"type"</span> identifying the type of
  calibration file, <span style="font-family: monospace;">"units"</span> identifying wavelength units, <span style="font-family: monospace;">"band"</span> identifying
  the band for magnitudes, and <span style="font-family: monospace;">"weff"</span> identifying the effective wavelength of
  the band.
  </p>
  <p>
  There are two types of standard star calibration files as described
  below.
  </p>
  <dl id="l_STANDARD">
  <dt><b>STANDARD STAR CALIBRATION FILES</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='STANDARD' Line='STANDARD STAR CALIBRATION FILES' -->
  <dd>This type of file is any file that does not contain the parameter <span style="font-family: monospace;">"type"</span>
  with a value of <span style="font-family: monospace;">"blackbody"</span>.  The only other parameter used by this type of
  calibration file is the <span style="font-family: monospace;">"units"</span> parameter for the wavelength units.  If the
  units are not specified then the wavelengths default to Angstroms.  All
  older calibration files will have no parameter information so they are
  interpreted as standard star calibration files with wavelengths in
  Angstroms.
  The calibration files consist of lines with wavelengths, calibration
  magnitudes, and bandpass widths.  The magnitudes are m_AB defined as
  <div class="highlight-default-notranslate"><pre>
  m_AB(star) = -2.5 * log10 (f_nu) - 48.60
  </pre></div>
  where f_nu is in erg/cm^2/s/Hz.  The m_AB calibration magnitudes
  are converted to absolute flux per unit frequency using the
  parameter <i>fnuzero</i> defined by
  <div class="highlight-default-notranslate"><pre>
  f_nu = fnuzero * 10. ** (-0.4 * m_AB)
  </pre></div>
  Thus, <i>fnuzero</i> is the flux at m_AB of zero.  The flux units are
  determined by this number.  The default value was chosen such that Vega
  at 5556 Angstroms has an AB magnitude of 0.0336 and a flux of 3.52e-20
  ergs/cm2/s/Hz.  This is the same value that was used by all previous
  versions of this task.
  </dd>
  </dl>
  <dl id="l_BLACKBODY">
  <dt><b>BLACKBODY CALIBRATION FILES</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='BLACKBODY' Line='BLACKBODY CALIBRATION FILES' -->
  <dd>This type of file has the comment parameter <span style="font-family: monospace;">"type"</span> with a value of
  <span style="font-family: monospace;">"blackbody"</span>.  It must also include the <span style="font-family: monospace;">"band"</span> and <span style="font-family: monospace;">"weff"</span>
  comment parameters.  If no <span style="font-family: monospace;">"units"</span> comment parameter is given then
  the default units are Angstroms.
  The rest of the file consists of lines with wavelengths, m_AB of a zero
  magnitude star (in that band magnitude system), and the bandpass widths.
  The m_AB are defined as described previously.  Normally all the m_AB values
  will be the same though it is possible to adjust them to produce a
  departure from a pure blackbody flux distribution.
  The actual m_AB calibration magnitudes for the star are obtained by
  the relation
  <div class="highlight-default-notranslate"><pre>
  m_AB(star) = mag + m_AB(m=0) -
      2.5 * log10 (B(weff,teff)/B(w,teff))
  </pre></div>
  where m is the magnitude of the star in the calibration band, m_AB(m=0) is
  the calibration value in the calibration file representing the magnitude of
  a m=0 star (basically the m_AB of Vega), weff is the effective wavelength
  for the calibration file, and teff is the effective temperature of the
  star.  The function B(w,T) is the blackbody function in f_nu that provides
  the shape of the calibration.  Note how the normalization is such that at
  weff the last term is zero and m_AB(star) = m + m_AB(m=0).
  The m_AB(star) computed using the calibration values and the blackbody
  function are then in the same units and form as for the standard
  star files.  The conversion to f_nu and the remaining processing
  proceeds in the same way as for standard star calibration data.
  The parameters \Imag and <i>teff</i> are specified by the user for each
  star as described in the section BLACKBODY PARAMETERS.  These parameters
  are queried by the task for each star (unless forced to a value on the
  command line).
  </dd>
  </dl>
  <p>
  The beam switch mode is selected with the <i>beam_switch</i> parameter.
  This mode requires that all apertures are of the same star, the header
  keyword OFLAG be present to identify object and sky spectra, and that
  the sequence of spectra specified are paired such that if an object
  spectrum is encountered first the next spectrum for that aperture
  (spectra from other apertures may appear in between) is a sky spectrum
  or the reverse.  These restrictions are not fundamental but are made so
  that this mode behaves the same as with the previous version of this
  task.  The sky spectrum is subtracted from the object spectrum and the
  result is then used in generating the observed intensities in the calibration
  bandpasses.
  </p>
  <p>
  If the spectra have been extinction corrected (EX-FLAG = 0) the
  extinction correction is removed.  The specified extinction file is
  used for this operation and so must be the same as that used when the
  extinction correction was made.  The airmass is also required in this step
  and, if needed to compute the airmass, the observatory specified in the
  image or observatory parameter is used.  The
  treatment of extinction in this task is subtle.  The aim of this task
  is to produce observed integrated instrumental intensities without
  extinction correction.  Thus, the extinction correction is removed from
  extinction corrected spectra.  However, a correction is made for an
  extinction gradient across the bandpasses.  This is done by applying an
  extinction correction, integrating across the bandpass, and then
  correcting the integrated intensity for the extinction at the center of
  the bandpass.  An alternative way to look at this is that the integral
  is weighted by the ratio of the extinction correction at each pixel to
  the extinction correction at the center of the bandpass.  This
  correction or weighting is why the extinction file and latitude are
  parameters in this task even though for nonextinction corrected spectra
  they appear not to be needed.
  </p>
  <p>
  The observed instrumental intensities are integrated within a set of
  bandpasses by summing the pixels using partial pixels at the bandpass
  edges.  Initial bandpasses are defined in one of two ways.  A set of
  evenly spaced bandpasses of constant width covering the range of the
  input spectrum may be specified using the parameters <i>bandwidth</i>
  and <i>bandsep</i> in the same units as the spectrum dispersion.  If
  these parameters have the value INDEF then the bandpasses from the
  calibration file which are entirely within the spectrum are selected.
  Generally these bandpasses are the actual measured bandpasses though
  one is free to make calibration files using estimated points.  The
  calibration bandpasses are preferable because they have been directly
  measured and they have been placed to avoid troubles with spectral
  lines.  However, when the coverage or resolution is such that these
  bandpasses do not allow a good determination of the instrumental
  response the evenly spaced bandpasses may be needed.  The calibration
  fluxes are linearly interpolated (or extrapolated) from the calibration
  data points to the defined bandpasses.
  </p>
  <p>
  Each spectrum adds a line to the output file containing the spectrum image
  name, the sky spectrum image name if beam switching, the aperture or beam
  number, the number of points in the spectrum, the exposure time, airmass,
  wavelength range, and title.  If the airmass is not found in the image
  header it is computed using the latitude parameter and observation
  information from the header.  If the airmass cannot be computed, due to
  missing keywords, then a query is made for the airmass.
  </p>
  <p>
  Following the spectrum information, calibration data is added for each
  bandpass.  The bandpass wavelength, absolute flux (per Angstrom),
  bandpass width, and observed instrumental intensity in the bandpass are
  added to the output file.  As discussed above, the observed intensity
  does not include an extinction term but does apply a small correction
  or weighting for the variation of the extinction across the bandpass.
  </p>
  <p>
  The setting and editing of the bandpasses may be performed
  interactively if the <i>interact</i> flag is set.  In this case the user
  is queried for each spectrum.  The answers to this query may be <span style="font-family: monospace;">"no"</span> or
  <span style="font-family: monospace;">"yes"</span> to skip editing or edit the bandpasses for this spectrum, <span style="font-family: monospace;">"NO"</span> or
  <span style="font-family: monospace;">"YES"</span> to skip or not skip editing all spectra of the same aperture with
  no further queries for this aperture, and <span style="font-family: monospace;">"NO!"</span> or <span style="font-family: monospace;">"YES!"</span> to skip
  editing or edit all spectra with no further queries.
  </p>
  <p>
  When editing the bandpasses a graph of the spectrum is made with the
  bandpasses plotted at the computed intensity per pixel.  The cursor and
  colon commands available are summarized in the section CURSOR KEYS.
  Basically bandpasses may be added or deleted and the current bandpass
  data may be examined.  Additional keys allow the usual windowing and
  cursor mode operations.  When satisfied with the bandpasses exit with
  <span style="font-family: monospace;">'q'</span>.  The edited bandpasses for that aperture remain in effect until
  changed again by the user.  Thus if there are many spectra from the
  same aperture one may reply with <span style="font-family: monospace;">"NO"</span> to queries for the next spectra
  to accept the current bandpasses for all other spectra of the same
  aperture.
  </p>
  <p>
  BLACKBODY PARAMETERS
  </p>
  <p>
  When a blackbody calibration is selected (the calibration file selected by
  the <i>star_name</i> parameter has <span style="font-family: monospace;">"# type blackbody"</span>) there are two
  quantities needed to scale the blackbody to the observation.  These are the
  magnitude of the star in the same band as the observation and the effective
  temperature.  The magnitude is used for the flux scaling and the effective
  temperature for the shape of the flux distribution.  The values are
  obtained or derived from the user specified parameters <i>mag</i>,
  <i>magband</i>, and <i>teff</i>.  This section describes how the the
  values are derived from other parameters using the data file <span style="font-family: monospace;">"params.dat"</span>
  in the calibration directory.
  </p>
  <p>
  The effective temperature in degrees Kelvin may be specified directly or it
  may be derived from a spectral type for the star.  In the latter case the
  file <span style="font-family: monospace;">"params.dat"</span> is searched for the effective temperature.  The file
  consists of lines with the first value being the spectral type and the
  second the effective temperature.  Other columns are described later.  The
  spectral type can be any string without whitespace that matches what is in
  the file.  However, the program finds the last spectral type that matches
  the first two characters when there is no complete match.  This scheme is
  intended for the case where the spectral types are of the form A0I, A0III,
  or A0V, where A can be any spectral type letter OBAFGKM, the single digit
  subtype is between 0 and 9, and the luminousity class is one of I, III, or
  V.  The two character match selects the last spectral type independent of
  the luminosity class.  The standard file <span style="font-family: monospace;">"onedstds$blackbody/params.dat"</span>
  uses these spectral type identifiers with the dwarf class acting as the
  default.
  </p>
  <p>
  The magnitude band is specified along with the input magnitude.  If the
  band is the same as the calibration band given in the calibration file then
  no further transformation is required.  However if the magnitude is
  specified in a different band, a conversion is performed using information
  from the <span style="font-family: monospace;">"params.dat"</span> file based on the spectral type of the star.
  </p>
  <p>
  When an effective temperature is specified rather and a spectral type then
  the nearest tabulated temperature for the spectral types that have <span style="font-family: monospace;">"V"</span> as
  the third character is used.  For the standard spectral type designations
  this means that when an effective temperature is specified the dwarf
  spectral type is used for the magnitude transformation.
  </p>
  <p>
  As mentioned previously, the <span style="font-family: monospace;">"params.dat"</span> data file has additional columns
  following the spectral type and effective temperature.  These columns are
  relative magnitudes in various bands.  The standard file has V magnitudes
  of zero so in this case the columns are also the X-V colors (where X is the
  appropriate magnitude).  Given the spectral type the relative magnitudes
  for the calibration band, m_1, and the input magnitude band, m_2, are found
  and the calibration magnitude for the star is given by
  </p>
  <div class="highlight-default-notranslate"><pre>
  m_calibration = m_input + m_1 - m_2
  </pre></div>
  <p>
  If one of the magnitudes is missing,  given as <span style="font-family: monospace;">"INDEF"</span> because the
  transformation is not available for the spectral type, the last spectral
  type matching the first two characters which does specify the two
  magnitudes will be used.  For example if there is no information for a
  B3III star for a M-J color then the spectral type B3V might be used.
  </p>
  <p>
  In order for the program to determine the bands for each column in the data
  file there must be a comment before the data with the column names.  It must
  begin with <span style="font-family: monospace;">"# Type Teff"</span> and then be followed by the same band identifiers
  used in the blackbody calibration files and as specified by the
  <i>magband</i> parameter.  Any amount whitespace (space or tab) is used to
  separate the various fields in the comment and in the fields of the table.
  For example the file might have the comment
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Type    Teff     V      J      H      K      L   Lprime    M
  </pre></div>
  <p>
  identifying the third column of the file as the V magnitude and the
  ninth file as the M magnitude.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  To compile observations of three standard stars using a beam
  switched instrument like the IIDS:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; standard.recformat=yes
  cl&gt; standard nite1 1001-1008 std beam_switch+ interact-
  [nite1.1001][0]: HZ 44 - Night 1
  [nite1.1004][0]: HZ 44 - Night 1
  [nite1.1005][0]: HZ 44 - Night 1
  [nite1.1008][0]: HZ 44 - Night 1
  Star name in calibration list: hz 44
  cl&gt; standard nite1 1009-1016 std beam_switch+ interact-
      ...
  cl&gt; standard nite1 1017-1024 std beam_switch+ interact-
      ...
  </pre></div>
  <p>
  This will create a file <span style="font-family: monospace;">"std"</span> which will contain sensitivity measurements
  from the beam-switched observations of the three standard stars given.
  Note that <b>standard</b> is run separately for each standard star.
  </p>
  <p>
  The spectra will be from the images: nite1.1001, nite.1002 ... nite1.1024,
  and the default calibration file, <span style="font-family: monospace;">"onedstds$irscal.dat"</span> will be used.
  </p>
  <p>
  2.  For echelle spectra all apertures, the orders, are of the same star and
  so the samestar parameter is set.  Usually the resolution is much higher than
  the calibration data so in order to get sufficient coverage bandpasses must
  be interpolated from the calibration data.  Therefore the evenly spaced
  bandpasses are used.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; standard.recformat=no
  cl&gt; standard.samestar=yes
  cl&gt; standard ech001.ec std bandwidth=10 bandsep=15
  [ech001.ec][0]: Feige 110
  Star name in calibration list: feige 110
  [ech001.ec][0]: Edit bandpasses? (no|yes|NO|YES|NO!|YES!): yes
  [ech001.ec][1]: Edit bandpasses? (no|yes|NO|YES|NO!|YES!): yes
  [ech001.ec][2]: Edit bandpasses? (no|yes|NO|YES|NO!|YES!): NO!
  </pre></div>
  <p>
  3. To use a blackbody infrared calibration where the V magnitude of
  the star is known.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; standard std1.ms std caldir=onedstds$blackbody/
  std1.ms(1): Standard Star
  Star name in calibration list: J
  Magnitude of star: 10.3
  Magnitude type (|V|J|H|K|L|Lprime|M|): V
  Effective temperature or spectral type: B3III
  WARNING: Effective temperature for B3III not found - using B3V
  Blackbody: V = 10.30, J = 10.32, Teff = 19000
  std1[1]: Edit bandpasses? (no|yes|NO|YES|NO!|YES!) (yes):
  </pre></div>
  <p>
  Note the warning message and the confirmation information.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_STANDARD">
  <dt><b>STANDARD V2.10.4</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='STANDARD' Line='STANDARD V2.10.4' -->
  <dd>The calibration files can be defined to compute blackbody values.
  </dd>
  </dl>
  <dl id="l_STANDARD">
  <dt><b>STANDARD V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='STANDARD' Line='STANDARD V2.10.3' -->
  <dd>A query for the airmass and exposure time is now made if the information
  is not in the header and cannot be computed from other header keywords.
  </dd>
  </dl>
  <dl id="l_STANDARD">
  <dt><b>STANDARD V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='STANDARD' Line='STANDARD V2.10' -->
  <dd>Giving an unrecognized standard star name will page a list of standard
  stars available in the calibration directory and then repeat the
  query.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  observatory, lcalib, sensfunc
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'CURSOR KEYS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

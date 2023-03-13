.. _bswitch:

bswitch: Beam-switch strings of spectra to make obj-sky pairs
=============================================================

**Package: irs**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  bswitch input records
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The root name for the input spectra to be beam-switched.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records' -->
  <dd>The range of spectra to be included in the beam-switch operation.
  Each range item will be appended to the root name to form an image
  name. For example, if <span style="font-family: monospace;">"input"</span> is <span style="font-family: monospace;">"nite1"</span> and records is <span style="font-family: monospace;">"1011-1018"</span>,
  then spectra nite1.1011, nite.1012 ... nite1.1018 will be included.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>New spectra are created by the beam-switch operation. This parameter
  specifies the root name to be used for the created spectra.
  </dd>
  </dl>
  <dl id="l_start_rec">
  <dt><b>start_rec = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='start_rec' Line='start_rec = 1' -->
  <dd>Each new spectrum created has <span style="font-family: monospace;">"output"</span> as its root name and a trailing
  number appended. The number begins with start_rec and is incremented
  for each new spectrum. For example, if <span style="font-family: monospace;">"output"</span> is given as <span style="font-family: monospace;">"nite1b"</span>
  and start_rec is given as 1001, then new spectra will be created as
  nite1b.1001, nite1b.1002 ...
  </dd>
  </dl>
  <dl id="l_stats">
  <dt><b>stats = <span style="font-family: monospace;">"stats"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='stats' Line='stats = "stats"' -->
  <dd>A file by this name will have statistical data appended to it, or created
  if necessary. If a null file name is given (<span style="font-family: monospace;">""</span>), no statistical output
  is given. For each aperture, a listing of countrates for each
  observation is given relative to the observation with the highest rate.
  </dd>
  </dl>
  <dl id="l_ids_mode">
  <dt><b>ids_mode = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ids_mode' Line='ids_mode = yes' -->
  <dd>If the data are taken under the usual IIDS <span style="font-family: monospace;">"beam-switch"</span> mode, this
  parameter should be set to yes so that accumulations will be performed
  in pairs. But if the data are taken where there is no sky observation
  or different numbers of sky observations, ids_mode should be set to no.
  If weighting is in effect, ids_mode=yes implies weighting of the
  object-sky sum; if ids_mode=no, then weighting is applied to the
  object and sky independently because then there is no guarantee that
  an object and sky observation are related.
  </dd>
  </dl>
  <dl id="l_extinct">
  <dt><b>extinct = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extinct' Line='extinct = yes' -->
  <dd>If set to yes, a correction for atmospheric extinction is applied.
  The image header must have either a valid entry for AIRMASS or
  for hour angle (or right ascension and sidereal time) and declination.
  </dd>
  </dl>
  <dl id="l_weighting">
  <dt><b>weighting = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='weighting' Line='weighting = no' -->
  <dd>If set to yes, the entire spectrum or a specified region will be used
  to obtain a countrate indicative of the statistical weight to be
  applied to the spectrum during the accumulations.
  </dd>
  </dl>
  <dl id="l_subset">
  <dt><b>subset = 32767</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='subset' Line='subset = 32767' -->
  <dd>A subset value larger than the number of independent spectra to be
  added indicates that the operation is to produce a single spectrum
  for each aperture regardless of how many input spectra are entered.
  If subset is a smaller number, say 4, then the accumulations
  are written out after every 4 spectra and then re-initialized to zero
  for the next 4.
  </dd>
  </dl>
  <dl id="l_wave1">
  <dt><b>wave1 = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wave1' Line='wave1 = 0.0' -->
  <dd>If weighting=yes, this parameter indicates the starting point in the
  spectrum for the countrate to be assessed. For emission-line objects,
  this is particularly useful because the regime of information is then
  confined to a narrow spectral region rather than the entire spectrum.
  Defaults to the beginning of the spectrum.
  </dd>
  </dl>
  <dl id="l_wave2">
  <dt><b>wave2 = 0.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wave2' Line='wave2 = 0.0' -->
  <dd>This provides the ending wavelength for the countrate determination.
  Defaults to the endpoint of the spectrum.
  </dd>
  </dl>
  <dl id="l_observatory">
  <dt><b>observatory = <span style="font-family: monospace;">"observatory"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observatory' Line='observatory = "observatory"' -->
  <dd>Observatory at which the spectra were obtained if
  not specified in the image header by the keyword OBSERVAT.  The
  observatory may be one of the observatories in the observatory
  database, <span style="font-family: monospace;">"observatory"</span> to select the observatory defined by the
  environment variable <span style="font-family: monospace;">"observatory"</span> or the task <b>observatory</b>, or
  <span style="font-family: monospace;">"obspars"</span> to select the current parameters set in the <b>observatory</b>
  task.  See help for <b>observatory</b> for additional information.
  </dd>
  </dl>
  <dl id="l_extinction">
  <dt><b>extinction = <span style="font-family: monospace;">")_.extinction"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='extinction' Line='extinction = ")_.extinction"' -->
  <dd>The the name of the file containing extinction values.
  Required if extinct=yes.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Data from multiaperture spectrographs are summed according to
  aperture number and sky subtracted if sky observations are available.
  Data for up to 50 apertures may be simultaneously accumulated.
  The accumulated spectra are written to new images. 
  </p>
  <p>
  The exposure times for each observation may be different. All
  internal computations are performed in terms of count rates,
  and converted back to counts (for statistical analysis) prior to writing
  the new image. Therefore, the time on the sky and object may
  be different as well. When these extensions to the normal
  mode are required, the flag ids_mode must be set to no.
  Then object and sky accumulations are performed totally
  independently and a difference is derived at the conclusion
  of the operation.
  </p>
  <p>
  If ids_mode is set to yes, then the usual IIDS/IRS <span style="font-family: monospace;">"beam-switch"</span>
  observing mode is assumed. This implies that an equal number of
  sky and object spectra are obtained through each aperture
  after 2N spectra have been accumulated, where N is the number
  of instrument apertures (2 for the IIDS/IRS). It is also assumed
  that the object and sky exposure times are equal for each aperture.
  Note that the <span style="font-family: monospace;">"nebular"</span> mode (where all instrument apertures
  point at an extended object simultaneously, and then all apertures
  point at sky simultaneously) is an acceptable form for
  beam-switched data in ids_mode.
  </p>
  <p>
  The accumulations are optionally weighted by the countrate
  over a region of the spectrum to improve the statistics during
  variable conditions. The user may specify the region of spectrum
  by wavelength. In ids_mode, the statistics are obtained from
  object-sky differences; otherwise, the statistics are performed
  on object+sky and sky spectra separately.
  </p>
  <p>
  The spectra may be extinction corrected if this has not already
  been performed.
  In order to perform either the extinction correction or the
  weighting process, the spectra must have been placed on a linear
  wavelength scale (or linear in the base 10 logarithm).
  </p>
  <p>
  Strings of spectra are  accumulated to produce a single
  summed spectrum for each observing aperture. But in some cases
  it is desirable to produce summed spectra from subsets of the
  entire string to evaluate the presence of variations either due
  to observing conditions or due to the physical nature of the
  object. A subset parameter may be set to the frequency at which
  spectra are to be summed.
  </p>
  <p>
  In order that the processing occur with minimal user interaction,
  elements from the extended image header are used to direct the
  flow of operation and to obtain key observing parameters.
  The required parameters are: object/sky flag (OFLAG=1/0), exposure
  time in seconds (ITM), beam (that is, aperture) number (BEAM-NUM), airmass (AIRMASS)
  or alternatively hour angle (HA) and declination (DEC), or
  right ascension (RA), sidereal time (ST), declination (DEC), and the
  observatory (OBSERVAT),
  starting wavelength (W0), and wavelength increment per channel (WPC),
  where the names in parenthesis are the expected keywords in the
  header.  If the observatory is not specified in the image the
  observatory parameter is used.  See <b>observatory</b> for further
  details on the observatory database.
  </p>
  <p>
  The following header flags are used as well: DC_FLAG
  for dispersion corrected data (must=0), BS_FLAG for beam-switching
  (must not be 1 which indicates the operation was already done),
  EX_FLAG for extinction correction (if = 0 extinction is assumed already
  done).  
  </p>
  <p>
  The headers may be listed with the IMHEADER task, setting
  the parameter <span style="font-family: monospace;">"long"</span> = yes. The values for the parameters follow 
  the rules used for IIDS and IRS data.
  </p>
  <p>
  After the beam-switch operation, the newly created spectra will
  have header elements taken from the last object spectrum.
  A few parameters will be updated to reflect the operation
  (e.g. integration time, processing flags).
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The following example will accumulate a series of 16 spectra obtained
  in the normal beam-switched mode and create two new extinction corrected
  spectra having names nite1bs.1 and nite1bs.2:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bswitch nite1 1011-1026 nite1bs 1
  </pre></div>
  <p>
  The following example performs the same functions but accumulates the data
  to produce 8 new spectra representing the individual object-sky pairs:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bswitch nite1 1011-1026 nite1bs 1 subset=4
  </pre></div>
  <p>
  The following example produces an extinction corrected spectrum for every
  input spectrum. Note that ids_mode is set to off to generate separate object and
  sky sums, and subset is set to 2 so that every pair of spectra (one object and
  one sky) are written out as two new spectra:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bswitch nite1 1011-1026 nite1bs 1 subset=2 ids_mode-
  </pre></div>
  <p>
  The next example produces a pair of spectra for each of 3 independent
  objects observed, provided that each was observed for the same number
  of observations (16 in this case).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bswitch nite1 1011-1026,1051-1066,1081-1096 nite1bs 1 \
  &gt;&gt;&gt; subset=16
  </pre></div>
  <p>
  The next example shows how to use the weighting parameters where
  the indicative flux is derived from the region around the emission-line
  of 5007A.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; bswitch nite1 1011-1026 nite1bs 1 weighting- \
  &gt;&gt;&gt; wave1=4990, wave2=5020
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  <p>
  The principle time expenditure goes toward extinction correcting the
  data. For IIDS type spectra (length=1024 pixels), approximately 30 cpu
  seconds are required to beam-switch a series of 16 spectra.
  </p>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The number of apertures is restricted to 50 and must be labeled
  between 0 and 49 in the image header (the IIDS uses 0 and 1).
  </p>
  <p>
  Until an image header editor is available, BSWITCH 
  can be applied only to data with properly prepared headers
  such as IIDS/IRS data read by RIDSMTN, RIDSFILE and some data via RFITS.
  </p>
  <p>
  When used to perform the function of extinction correction only (the
  third example above), the statistics file fails to note the output
  image name for the sky spectrum.
  </p>
  <p>
  The data must be on a linear wavelength scale.
  The starting wavelength, W0, and a wavelength
  per channel, WPC, are required header information, and the DC_FLAG
  must be set to 0.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  observatory, sensfunc, imheader, lcalib, ridsmtn, ridsfile, rfits
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

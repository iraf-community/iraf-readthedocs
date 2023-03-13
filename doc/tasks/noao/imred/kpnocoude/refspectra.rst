.. _refspectra:

refspectra: Assign reference spectra to observations
====================================================

**Package: kpnocoude**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  refspectra input [records]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input spectra or root names to be assigned reference spectra.
  When using the record number extension format, record number extensions
  will be appended to each root name in the list.
  </dd>
  </dl>
  <dl id="l_records">
  <dt><b>records (imred.irs and imred.iids packages only)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='records' Line='records (imred.irs and imred.iids packages only)' -->
  <dd>List of records or ranges of records to be appended to the input root
  names when using record number extension format.  The syntax of this
  list is comma separated record numbers or ranges of record numbers.  A
  range consists of two numbers separated by a hyphen. An example of this
  syntax is <span style="font-family: monospace;">"1-5,13,17-19"</span>.  A null list (<span style="font-family: monospace;">""</span>) may
  be used if no record number extensions are desired.  This is a
  positional query parameter only if the record format is specified with
  the <i>recformat</i> parameter.
  </dd>
  </dl>
  <dl id="l_references">
  <dt><b>references = <span style="font-family: monospace;">"*.imh"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='references' Line='references = "*.imh"' -->
  <dd>List of reference spectra to be assigned or a <span style="font-family: monospace;">"reference spectra assignment
  table"</span> (see DESCRIPTION section).
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>List of apertures to be SELECTED from the input list of spectra.  If no list
  is specified then all apertures are selected.  The syntax is the same as the
  record number extensions.
  </dd>
  </dl>
  <dl id="l_refaps">
  <dt><b>refaps = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='refaps' Line='refaps = ""' -->
  <dd>List of reference spectra apertures to be SELECTED.  If no list is specified
  then all apertures are selected.  The syntax is the same as the record number
  extensions.
  </dd>
  </dl>
  <dl id="l_ignoreaps">
  <dt><b>ignoreaps = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ignoreaps' Line='ignoreaps = yes' -->
  <dd>Ignore the input and reference apertures when ASSIGNING reference spectra.
  If the aperture numbers are not ignored then only the reference spectra with
  the same aperture number as a particular input spectra are used when assigning
  reference spectra.  Otherwise all the reference spectra are used.  This does
  not apply to the <span style="font-family: monospace;">"match"</span> and <span style="font-family: monospace;">"average"</span> options which always ignore the aperture
  numbers.  Note that this parameter applies to relating reference spectra to
  input spectra and does not override the aperture selections on the input
  spectra and reference spectra.
  </dd>
  </dl>
  <dl id="l_select">
  <dt><b>select = <span style="font-family: monospace;">"interp"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='select' Line='select = "interp"' -->
  <dd>Selection method for assigning reference spectra.  The methods are:
  <dl>
  <dt><b>average</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='average' Line='average' -->
  <dd>Average two reference spectra without regard to any aperture,
  sort, or group parameters.
  If only one reference spectrum is specified then it is assigned with a
  warning.  If more than two reference spectra are specified then only the
  first two are used and a warning is given.  There is no checking of the
  aperture numbers or group values.
  </dd>
  </dl>
  <dl>
  <dt><b>following</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='following' Line='following' -->
  <dd>Select the nearest following spectrum in the reference list based on the
  sort and group parameters.  If there is no following spectrum use the
  nearest preceding spectrum.
  </dd>
  </dl>
  <dl>
  <dt><b>interp</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='interp' Line='interp' -->
  <dd>Interpolate between the preceding and following spectra in the reference
  list based on the sort and group parameters.  If there is no preceding and
  following spectrum use the nearest spectrum.  The interpolation is weighted
  by the relative distances of the sorting parameter (see cautions in
  DESCRIPTION section).
  </dd>
  </dl>
  <dl>
  <dt><b>match</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='match' Line='match' -->
  <dd>Match each input spectrum with the reference spectrum list in order.
  This overrides any aperture or group values.
  </dd>
  </dl>
  <dl>
  <dt><b>nearest</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='nearest' Line='nearest' -->
  <dd>Select the nearest spectrum in the reference list based on the sort and
  group parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>preceding</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='preceding' Line='preceding' -->
  <dd>Select the nearest preceding spectrum in the reference list based on the
  sort and group parameters.  If there is no preceding spectrum use the
  nearest following spectrum.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_sort">
  <dt><b>sort = <span style="font-family: monospace;">"jd"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sort' Line='sort = "jd"' -->
  <dd>Image header keyword to be used as the sorting parameter for selection
  based on order.  The header parameter must be numeric but otherwise may
  be anything.  Common sorting parameters are times or positions.
  A null string, <span style="font-family: monospace;">""</span>, or the word <span style="font-family: monospace;">"none"</span> may be use to disable the sorting
  parameter.
  </dd>
  </dl>
  <dl id="l_group">
  <dt><b>group = <span style="font-family: monospace;">"ljd"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='group' Line='group = "ljd"' -->
  <dd>Image header keyword to be used to group spectra.  For those selection
  methods which use the group parameter the reference and object spectra must
  have identical values for this keyword.  This can be anything but it must
  be constant within a group.  Common grouping parameters are the date of
  observation <span style="font-family: monospace;">"date-obs"</span> (provided it does not change over a night) or the
  local Julian day number.  A null string, <span style="font-family: monospace;">""</span>, or the word <span style="font-family: monospace;">"none"</span> may be use
  to disable the grouping parameter.
  </dd>
  </dl>
  <dl id="l_time">
  <dt><b>time = no, timewrap = 17.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='time' Line='time = no, timewrap = 17.' -->
  <dd>Is the sorting parameter a 24 hour time?  If so then the time orgin
  for the sorting is specified by the timewrap parameter.  This time
  should precede the first observation and follow the last observation
  in a 24 hour cycle.
  </dd>
  </dl>
  <dl id="l_override">
  <dt><b>override = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='override' Line='override = no' -->
  <dd>Override previous assignments?  If an input spectrum has reference
  spectra assigned previously the assignment will not be changed unless
  this flag is set.
  </dd>
  </dl>
  <dl id="l_confirm">
  <dt><b>confirm = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='confirm' Line='confirm = yes' -->
  <dd>Confirm reference spectrum assignments?  If <i>yes</i> then the reference
  spectra assignments for each input spectrum are printed and the user may
  either accept the assignment or not.  Rejected assignments leave the
  input spectrum unchanged.
  </dd>
  </dl>
  <dl id="l_assign">
  <dt><b>assign = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='assign' Line='assign = yes' -->
  <dd>Assign the reference spectrum by entering it in the image header?
  The input spectra are only modified if this parameter is <i>yes</i>.
  This parameter may be set to <i>no</i> to get a list of assignments
  without actually entering the assignments in the image headers.
  </dd>
  </dl>
  <dl id="l_logfiles">
  <dt><b>logfiles = <span style="font-family: monospace;">"STDOUT,logfile"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='logfiles' Line='logfiles = "STDOUT,logfile"' -->
  <dd>List of log files for recording reference spectra assignments.
  The file STDOUT prints to the standard output.  If not specified (<span style="font-family: monospace;">""</span>)
  then no logs will be recorded.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Verbose log output?  This prints additional information about the input
  and reference spectra.  This is useful for diagnosing why certain spectra
  are ignored or not assigned as intended.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task allows the user to define which reference spectra are to be 
  used in the calculation of the dispersion solution of object spectra.
  The assignment of reference spectra to object spectra is often
  a complex task because of the number of spectra, the use of many distinct
  apertures, and different modes of observing such as interspersed arc
  calibration spectra or just one calibration for a night.  This task
  provides a number of methods to cover many of the common cases.
  </p>
  <p>
  A reference spectrum is defined to be a spectrum that has been used to
  calculate a wavelength solution with the tasks IDENTIFY or REIDENTIFY.
  These tasks have set the keyword REFSPEC1 in the image header
  equal to the spectrum's own name.
  </p>
  <p>
  Wavelength reference spectra are assigned to input spectra by entering
  the reference spectrum name or pair of names in the image
  header under the keywords REFSPEC1 and REFSPEC2.  When two reference
  spectra are assigned, the spectrum names may be followed by a weighting
  factor (assumed to be 1 if missing).  The wavelength of a pixel is
  then the weighted average of the wavelengths from the reference
  spectra dispersion solutions.  The weighting factors are calculated
  by choosing an appropriate selection method, ie average, interpolation,
  etc. Note, however, that these assignments may be made directly using
  the task <b>hedit</b> or with some other task or script if none of the
  methods are suitable. 
  </p>
  <p>
  The spectra to be assigned references are specified by an input list.
  Optional numeric record format extensions may be appended to each name
  (used as a root name) in the input list in the <b>iids/irs</b> packages.
  The input spectra may be restricted to a particular set of aperture numbers
  by the parameter <i>apertures</i>; the spectra not in the list of apertures
  are skipped.  If the aperture list is null (i.e. specified as <span style="font-family: monospace;">""</span>) then all
  apertures are selected.  One further selection may be made on the input
  spectra.  If the parameter <i>override</i> is no then input spectra which
  have existing reference spectra assignments (which includes the reference
  spectra) are skipped.
  </p>
  <p>
  The reference spectra parameter <i>references</i> may take two forms.
  It may be an image list of spectra or a text file containing
  a <span style="font-family: monospace;">"reference spectrum assignment table"</span>.  The table consists of pairs
  of strings/lists with the first string being a list of object spectra
  and the second string being a list of reference spectra.  If this
  table is used, then only those object spectra in the table that are also
  listed in the input parameter list are processed.  The example below
  illustrates the reference spectrum assignment table:
  </p>
  <div class="highlight-default-notranslate"><pre>
  spec1           spec2,spec3,spec4
  spec5
  spec6,spec7     spect8,spec9
  spec10          spec11
  spec12          spec13
  spec14          spec15
  </pre></div>
  <p>
  As a convenience, if a reference list in the table is missing, the preceding
  reference list is implied. This table may be used to make arbitrary assignments.
  </p>
  <p>
  The reference spectra in the specified list may also be restricted to a
  subset of aperture numbers.  However, in the case of averaging, the
  reference aperture selection is ignored. In the case of matching, if
  a reference spectrum is not selected then the matching input spectrum
  is also skipped (in order to maintain a one-to-one correspondence).
  Spectra in the reference list which are not reference spectra (as
  defined earlier) are also ignored and a warning is printed.  Note that
  no check is made that a dispersion solution actually exists in the
  dispersion solution database.
  </p>
  <p>
  There may be cases where there are only reference spectra for some
  apertures and it is desired to apply these reference spectra to the
  other apertures.  The <i>ignoreaps</i> flag may be used to force an
  assignment between reference and object spectra with different
  aperture numbers.  Note that this flag is applied after the input and
  reference list aperture number selections are made; in other words this
  applies only to the assignments and not the input selection process.
  </p>
  <p>
  Once the appropriate reference spectra from the reference list have been
  determined for an input spectrum they are assigned using one of the
  methods selected by the parameter <i>select</i>.  The <span style="font-family: monospace;">"match"</span> method
  simply pairs each element of the input spectrum list with each element
  in the reference spectrum list.  If a reference assignment table
  is used with <span style="font-family: monospace;">"match"</span>, then only the first spectrum in the reference
  list for each input spectrum is assigned.
  </p>
  <p>
  The <span style="font-family: monospace;">"average"</span> method assigns the first two spectra in the reference list
  ignoring aperture numbers or groups. The spectra are averaged by assigning
  equal weights.  There is no weighting based on any sort parameter.  If
  there are more than two spectra in the reference list then only the first
  two spectra are used and the remainder are ignored.  If a reference
  assignment table is used only the first two reference spectra listed for
  each object in the table are averaged.
  </p>
  <p>
  The remaining selection methods group the spectra using a header keyword
  which must be constant within a group.  If no group parameter is specfied
  (the null string <span style="font-family: monospace;">""</span> or the word <span style="font-family: monospace;">"none"</span>)
  then grouping does not occur.  Only reference spectra with the same
  group header value as the object are assigned to an object spectrum.
  One likely group parameter is the <span style="font-family: monospace;">"date-obs"</span> keyword.  This is usually
  constant over a night at CTIO and KPNO.  At other sites this may not
  be the case.  Therefore, the task <b>setjd</b> may be used to set a
  local Julian day number which is constant over a night at any
  observatory.
  </p>
  <p>
  Within a group the spectra are ordered based on a numeric image header
  parameter specified by the <i>sort</i> parameter.  A null string <span style="font-family: monospace;">""</span> or the
  word <span style="font-family: monospace;">"null"</span> may be used to select no sort parameter.  Parameters which are
  times, as indicated by the <i>time</i> parameter, are assumed to be cyclic
  with a period of 24 hours.  The time wrap parameter defines the origin of a
  cycle and should precede the first observation and follow the last
  observation in a 24 hour period; i.e. for nighttime observations this
  parameter value should bee sometime during the day.  Particularly with
  interpolating or choosing the nearest reference spectrum it is important
  that the sorting parameter refer to the middle of the exposure.  A Julian
  date at the middle of an exposure may be calculated with the task
  <b>setjd</b> or a middle UT time may be computed with the task
  <b>setairmass</b>.
  </p>
  <p>
  The selection methods may choose the <span style="font-family: monospace;">"nearest"</span>, <span style="font-family: monospace;">"preceding"</span>, or <span style="font-family: monospace;">"following"</span>
  reference spectrum.  Alternatively, the reference wavelengths may be
  interpolated between the preceding and following reference spectra with
  weights given by the relative distances measured by the sorting parameter.
  In the cases where a preceding or following spectrum is required and one is
  not found then the nearest reference spectrum is used.  These methods are
  used for observing sequences where the reference spectra are taken either
  nearby in time or space.
  </p>
  <p>
  The option <span style="font-family: monospace;">"interp"</span> should not be used without some thought as to the
  nature of the interpolation.  If the sorting parameter is a time (a 24 hour
  cyclic parameter as opposed to a continuous parameter such as a Julian
  date) then the user must be aware of when these times were recorded in the
  header.  For example, let us assume that the sort parameter is <span style="font-family: monospace;">"ut"</span> and
  that this time was recorded in the header at the beginning of the
  exposure.  If the object spectrum exposure time is longer than the
  reference spectra exposure times, then interpolation will weight the
  preceding reference spectrum too heavily.  This problem can be circumvented
  by using the <span style="font-family: monospace;">"average"</span> selection method along with the reference assignment
  table.  Or the sort time parameter in the headers of the spectra can be
  changes with <i>setjd</i> or <i>setairmass</i> or edited to reflect the
  values at mid-exposure (see EXAMPLES).
  </p>
  <p>
  Once the reference spectrum or spectra for a input spectrum have been 
  identified the user may also chose to override any previous reference
  assignments, to accept or not accept the current reference assignments
  (in the case of not accepting the reference assignment the image header
  is not updated), to only list the current reference assignments and not
  update any image headers, as well as to record the reference assignments
  to log files.  These options are separately controlled by the remaining
  task parameters. 
  </p>
  </section>
  <section id="s_keywords">
  <h3>Keywords</h3>
  <p>
  This task uses the header keyword BEAM-NUM to sort the apertures.  It
  has an integer value.  If the keyword does not exist then all apertures
  are assumed to be 1.
  </p>
  <p>
  The keyword REFSPEC1 is used to search for reference spectra. This 
  keyword can be previously created by the tasks IDENTIFY and REIDENTIFY.
  </p>
  <p>
  The two keywords REFSPEC1 and optionally REFSPEC2 are created by the
  task when the assign parameter is set to yes.  They take the form:
  </p>
  <div class="highlight-default-notranslate"><pre>
  REFSPEC1='d1.0001'  or
  
  REFSPEC1='d5.0001 0.756'
  REFSPEC2='d5.0002 0.244'
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Compute a Julian date at the midpoint of the exposure for sorting
  and a local Julian day number for grouping and then assign spectra
  using interpolation.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; setjd *.imh jd=jd ljd=ljd
  cl&gt; refspec *.imh sort=jd group=ljd select=interp
  </pre></div>
  <p>
  2.  Specifically assign reference spectra to input spectra.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; refspectra spec1,spec3 refe=spec2,spec4 select=match
  </pre></div>
  <p>
  3.  Use a reference assignment table to assign reference spectra to input
  spectra using the <span style="font-family: monospace;">"average"</span> option.  First a table is created using an
  editor.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type reftable
  spec1               spec2,spec3,spec4
  spec5
  spec6,spec7         spect8,spec9
  spec10              spec11
  spec12              spec13
  spec14              spec15
  cl&gt; refspec spec*.imh recfor- select=average refe=reftable
  </pre></div>
  <p>
  4.  Assign the nearest reference spectrum in zenith distance using
  wildcard lists.  By default the aperture numbers must match.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; refspec *.imh "" sort=zd select=nearest time-
  </pre></div>
  <p>
  5.  Assign a specific reference spectrum to all apertures.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; refspec *.imh "" refer=refnite1 ignoreaps+
  </pre></div>
  <p>
  6.  Confirm assignments.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hselect irs.*.imh "$I,beam-num,ut,refspec1" yes
  irs.0009.imh        0       0:22:55         irs.0009
  irs.0010.imh        1       0:22:53         irs.0010
  irs.0100.imh        0       8:22:55
  irs.0101.imh        1       8:22:53
  irs.0447.imh        0       13:00:07        irs.0447
  irs.0448.imh        1       13:00:05        irs.0448
  cl&gt; refspec irs 100-101 refer=irs.*.imh conf+ ver+ select=nearest\
     &gt;&gt;&gt; ignoreaps-
  [irs.0100] Not a reference spectrum
  [irs.0101] Not a reference spectrum
  [irs.0100] refspec1='irs.0447'   Accept assignment (yes)?
  [irs.0101] refspec1='irs.0448'   Accept assignment (yes)?
  </pre></div>
  <p>
  Because the reference spectrum list includes all spectra the
  warning messages <span style="font-family: monospace;">"Not a reference spectrum"</span> are printed with verbose
  output.  Remember a reference spectrum is any spectrum which has a
  reference spectrum assigned which refers to itself.
  </p>
  <p>
  7.  Assign reference spectra with weights using interpolation.  In this
  example we want to sort by <span style="font-family: monospace;">"ut"</span> but this keyword value was 
  recorded at the beginning of the integration. So we first create an
  new keyword and then compute its value to be that of mid-exposure.  The
  new keyword is then used as the sorting parameter.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit *.imh utmid 0. add+ ver- show-
  cl&gt; hedit *.imh utmid "(ut)" ver- show-
  cl&gt; hedit *.imh utmid "(mod(utmid+exptime/7200.,24.))" ver- show-
  cl&gt; refspec *.imh refer=*.imh recfor- select=interp sort=utmid
  </pre></div>
  <p>
  8.  Assign reference spectra using the <span style="font-family: monospace;">"average"</span> option and the reference
  assignment table with data with record number extensions.  First edit
  the file reftable:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; type reftable
         spec.0001     arc1.0001,arc2.0001
         spec.0002     arc1.0002,arc2.0002
         spec.0003     arc1.0003,arc2.0003
         spec.0004     arc1.0004,arc2.0004
  cl&gt; refspec spec.*.imh recfor- refer=reftable select=average
  </pre></div>
  <p>
  9.  Assign a reference spectrum for aperture 1 to the object spectra
  for apertures 2 thru 5.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; refspec spec 2-5 recfor+ refer=arc.*.imh refaps=1 ignoreaps+
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_REFSPECTRA">
  <dt><b>REFSPECTRA V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='REFSPECTRA' Line='REFSPECTRA V2.10.3' -->
  <dd>If no reference spectrum is found in the interp, nearest, following,
  preceding methods then a list of the reference spectra is given
  showing why each was not acceptable.
  </dd>
  </dl>
  <dl id="l_REFSPECTRA">
  <dt><b>REFSPECTRA V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='REFSPECTRA' Line='REFSPECTRA V2.10' -->
  <dd>A group parameter was added to allow restricting assignments by observing
  period; for example by night.  The record format option was removed and
  the record format syntax is available in the <b>irs/iids</b> packages.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  identify, reidentify, dispcor, setjd, setairmass
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'KEYWORDS' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

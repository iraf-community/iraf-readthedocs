.. _mscotfflat:

mscotfflat: Built on-the-fly flat field calibrations
====================================================

**Package: msctools**

.. raw:: html

  <section id="s_overview">
  <h3>Overview</h3>
  <p>
  MSCDISPLAY and the real-time display based on this task applies an
  on-the-fly (OTF) calibration to raw mosaic exposures as they are being
  displayed.  This does not change the actual data files and the calibration
  is intended to be quick and approximate.  The calibration steps performed
  are a line-by-line bias subtraction using the overscan region of the data
  and a division by a flat field.  If the data have been overscan corrected
  or flat field corrected by CCDPROC then the task will automatically skip
  those steps.  The title of the display will indicate if the data have been
  calibrated by adding <span style="font-family: monospace;">"[bias]"</span> for bias subtraction and <span style="font-family: monospace;">"[bias,flat=XXX]"</span>
  for bias subtraction and flat fielding using an OTF flat field called XXX.
  </p>
  <p>
  The bias subtraction is performed by averaging the overscan pixels in a
  line and subtracting this average from all the pixels in the line.  This
  removes the amplifier bias and line-by-line patterns.
  </p>
  <p>
  The flat field or response calibration is performed by reading special flat
  field calibration data which provides an approximate relative response for
  each pixel in each amplifier readout.  Depending on how the calibration
  file is derived this will approximately correct for pixel sensitivity
  variations, gain variations between the amplifiers, sky illumination
  variations, and any pupil ghost pattern (as occurs with NOAO Mosaic data
  from the KPNO 4meter telescope).  Note that this is not the correct way to
  remove the pupil ghost but for the purposes of flattening the display in
  order to see faint objects this is useful.
  </p>
  <p>
  The other display related tasks, MSCEXAMINE and MSCFOCUS, must perform the
  same correction when the display and cursor are used to select data to
  measure.  Currently they do not know if the data have been calibrated in
  the display.  Instead, one must make sure to use the same parameters
  relating to the display in the MIMPARS parameter set.
  </p>
  </section>
  <section id="s_creating_and_installing_otf_flat_fields_at_noao">
  <h3>Creating and installing otf flat fields at noao</h3>
  <p>
  1.  Take one or more flat fields.  The count levels have to be below 30000.
  If not divide the values by a number either before or after processing
  using MSCARITH.  Since the OTF flats are spatially binned and digitized to
  reduce size it probably is not very useful to create a high quality flat
  from multiple exposures, a single exposure should be fine.
  </p>
  <p>
  2. Process the flat(s).  The processing should be only overscan and trim.
  If combining multiple flats with FLATCOMBINE set the processing as noted.
  The processing should save the raw exposures in the Raw subdirectory (or
  whatever is set for the <span style="font-family: monospace;">"backup"</span> parameter in MSCRED).
  </p>
  <p>
  3. Run MSCOTFFLAT with the default values.  The output name must be one
  word (that is an acceptible directory name) and should be the standard
  identifier for the filter.  Typically this would be the first word of the
  filter name recorded in the header (with any characters which are not
  letters, numbers, or <span style="font-family: monospace;">'.'</span> replaced with <span style="font-family: monospace;">'_'</span>).  The template name is one of
  the raw exposures.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; mscotfflat flat001 B Raw/flat001
  </pre></div>
  <p>
  This will create a subdirectory, B in this example, with the number of
  pl files equal to the number of extensions.
  </p>
  <p>
  3a. You can check if things make sense by the size of the pl files being
  approximately 0.6-1.6Mb.  You can also display the files and compare
  with the original data using:
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; display B/flat1 1 fill+ ...
  ms&gt; display flat00[1] 2 fill+ ...
  </pre></div>
  <p>
  They should be very similar to the flat from which they were derived.
  </p>
  <p>
  4. To use during your run with the real-time DCA display you would set
  the calibration directory in the DCA GUI to point to the parent
  directory containing the subdirectories of pl files (the directory you
  were in when you ran MSCOTFFLAT).  This is done from the <span style="font-family: monospace;">"Edit"</span> menu,
  selecting <span style="font-family: monospace;">"Path Params"</span>, editing the <span style="font-family: monospace;">"Calibration Dir"</span> field, and
  finally clicking <span style="font-family: monospace;">"Apply"</span>.  Also if you are going to use MSCDISPLAY with
  <span style="font-family: monospace;">"process=yes"</span> then go to the <span style="font-family: monospace;">"mimpars"</span> parameters and set the <span style="font-family: monospace;">"caldir"</span>
  directory parameter there too.  Remember that directories in IRAF must
  end with <span style="font-family: monospace;">'/'</span> (or <span style="font-family: monospace;">'$'</span> for logical directories).
  </p>
  <p>
  If you do nothing else the software will look in the specified calibration
  directory for a subdirectory which matches the first word of the filter
  string in the image header (with any characters that are not letters,
  numbers, or <span style="font-family: monospace;">'.'</span> changed to <span style="font-family: monospace;">'_'</span>).  If you want to translate the header
  filter name to some other (directory) name you can add a <span style="font-family: monospace;">"cal.men"</span> file
  where the first column is the filter name (quoted if there are blanks) and
  the second column is the directory name.  This file is also used to set the
  override choices for the filter in the DCA GUI.
  </p>
  <p>
  The following is done to install the OTF directory for general use and
  requires the IRAF login.
  </p>
  <p>
  5. Login as IRAF and go to the standard calibration directory:
  </p>
  <div class="highlight-default-notranslate"><pre>
  /iraf/extern/mscdb/noao/ctio/4meter/caldir/Mosaic2A     # CTIO 4m (8 A amps)
  /iraf/extern/mscdb/noao/ctio/4meter/caldir/Mosaic2B     # CTIO 4m (8 B amps)
  /iraf/extern/mscdb/noao/ctio/4meter/caldir/Mosaic2      # CTIO 4m (16 amps)
  /iraf/extern/mscdb/noao/kpno/4meter/caldir              # KPNO 4m
  /iraf/extern/mscdb/noao/kpno/36inch/caldir              # KPNO 36inch
  /iraf/extern/mscdb/noao/kpno/wiyn/caldir                # KPNO WIYN
  </pre></div>
  <p>
  Transfer the OTF directory to that calibration directory.  One way is
  </p>
  <div class="highlight-default-notranslate"><pre>
  % (cd /md1/4meter/nite1; wtar B) | rtar -xv
  </pre></div>
  <p>
  6.  Edit the cal.men file.  The first column is the filter name as
  given in the data files under the FILTER keyword.  The second name is
  the directory name.  The order of the entries in the order in which the
  filters will appear in the DCA list.  Note the DCA list is only used to
  override the automatic filter selection based on the filter keyword.
  </p>
  <p>
  7. Remove the OTF directory in your data area.  One way is with <span style="font-family: monospace;">"!rm -rf
  &lt;dir&gt;"</span>.  You can also restore the original raw flats for taping by moving
  the files from the Raw subdirectory back to the data directory.
  </p>
  <p>
  8.  I am maintaining a master MSCDB directory that includes current
  OTF flats.  This serves the purpose of a backup, the source to generate
  installation files, and the source to generate distribution files for
  users who might want them.  So if you create OTF files please notify
  me.
  </p>
  </section>
  <section id="s_otf_flat_field_calibration_format">
  <h3>Otf flat field calibration format</h3>
  <p>
  The flat field calibration is a special, more compact format than a regular
  mosaic flat field.  The small size is important both to save disk space in a
  standard calibration directory with lots of filters and to allow more
  efficient I/O and in-memory storage of the flat field data.  For instance,
  the NOAO Mosaic has 14 filters and two telescopes.
  </p>
  <p>
  The compression relies on two factors.  First is that pixel values can be
  quantized and still produce a good approximate calibration.  The second is
  that the quantized values often have the same values over contiguous
  regions.  These factors allow use of the IRAF pixel list format which
  represents integer values which are constant over segments of each line by
  fewer bytes than the individual values.
  </p>
  <p>
  The algorithm for creating the compressed flat field format consists of two
  simple steps with two parameters.  The first step is to block average the
  original real-valued flat field specified by a block average factor.
  This brings neighboring values to the same value which aids the pixel
  list representation.  Then the quantization is performed using the
  equation:
  </p>
  <div class="highlight-default-notranslate"><pre>
  quantized integer value = int (nint (value / scale) * scale)
  </pre></div>
  <p>
  where <span style="font-family: monospace;">"value"</span> is the real flat field pixel value and <span style="font-family: monospace;">"scale"</span> is
  a quantization factor.  The nint function takes the nearest integer value
  of its argument and the int function truncates its argument to an integer.
  The scale factor is defined by
  </p>
  <div class="highlight-default-notranslate"><pre>
  scale = &lt;value&gt; * resolution
  </pre></div>
  <p>
  where <span style="font-family: monospace;">"&lt;value&gt;"</span> is the mean flat field value and <span style="font-family: monospace;">"resolution"</span> is a parameter
  of the algorithm.  The resolution is then a fractional resolution of the
  mean flat field.
  </p>
  <p>
  For example, suppose the mean flat field value is 5001.23 and the
  resolution is 0.5%.  The digitization quantum is then 25.006.  A flat field
  value of 5123.45 would be quantized to 5126 and all values between 5113.8
  to 5138.8 also quantize to 5126.
  </p>
  <p>
  The NOAO Mosaic has significant flat field variations, which prompted the
  development of the OTF calibration.  The variations are on the order of
  10%.  The size of a full flat field exposure, reduced to real values, is
  256 Mb.  Applying the algorithm above with a 2x2 block average and a
  0.5% resolution produces an IRAF pixel list format, OTF flat field which
  is ~5 Mb.  Application of this OTF flat field shows virtually no artifacts.
  </p>
  </section>
  <section id="s_mimpars_parameters">
  <h3>Mimpars parameters</h3>
  <p>
  The parameters controlling the OTF calibration are set in the MIMPARS
  parameter set.  This parameter set is a subset of the MSCDISPLAY,
  MSCEXAMINE, and MSCFOCUS tasks.  As such they can be edited from EPAR
  on these task by typing <span style="font-family: monospace;">":e"</span> when over the <span style="font-family: monospace;">"mimpars"</span> parameter or the
  values can be given on the command line for those tasks.  Typing <span style="font-family: monospace;">"mimpars"</span>
  or <span style="font-family: monospace;">"epar mimpars"</span> will also let you edit these parameters and <span style="font-family: monospace;">"lpar mimpars"</span>
  will display the parameters.  The EPAR display looks like
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; mimpars
                             I R A F
              Image Reduction and Analysis Facility
  PACKAGE = mscred
     TASK = mimpars
  
  (extname=             ) extension name pattern
  (exttmpl= _![1-9]![1-9]![1-9].*) extension template for ...
  
  (xgap   =           72) minimum X gap between images
  (ygap   =           36) minimum Y gap between images
  
  (process=           no) do calibration processing?
  (oversca=          yes) do line-by-line overscan subtraction?
  (flatfie=          yes) do flat field correction?
  (caldir =             ) calibration directory
  (filter =             ) filter
  </pre></div>
  <p>
  The first two groups of parameters have to do with selecting data to be
  displayed and the gaps between the mosaic pieces added during display.  It
  is the last set of parameters that deal with the OTF calibration.
  </p>
  <p>
  For the NOAO Mosaic, running SETINSTRUMENT or using the parameters set at
  the  telescope will set some of these parameters appropriately to reference
  a calibration directory supplied by the instrument team.  For example, at
  the Kitt Peak 4meter telescope the parameters would be
  </p>
  <div class="highlight-default-notranslate"><pre>
  (caldir = mscdb$noao/kpno/4meter/caldir/) cal...
  (filter =              !filter) filter
  </pre></div>
  <p>
  The <i>process</i> parameter selects whether to turn on or off the OTF
  processing.  If it is no then regardless of the <i>overscan</i> or
  <i>flatfield</i> values no calibration will be done.  If it is yes then
  one or both calibration operations can be selected.
  </p>
  <p>
  The flat field calibration requires special calibration files.  The
  <i>caldir</i> parameter defines a directory containing the calibration
  files.  This can be a standard directory or a user directory.  Note
  that if a directory is specified it must end with $ or /.  In this directory,
  which could include other files, the calibrations are given by some
  set of names.  Currently these are the names of directories containing
  pixel list files for each amplifier.  Creating these files is done with
  the task MSCOTFFLAT which is described below.  The <i>filter</i> parameter
  can be set to one of these names.
  </p>
  <p>
  For more automatic selection of calibrations, the calibrations can be
  selected by the filter string in the header (or by giving the same filter
  string in the <i>filter</i> parameter).  To use the filter string in the
  header the value of the filter parameter is set to <span style="font-family: monospace;">"!&lt;keyword&gt;"</span> where
  &lt;keyword&gt; is the keyword for the filter string.  The filter string often
  contains some general description.  The OTF calibration software goes
  through the following steps to resolve the string to a calibration file in
  the calibration directory.
  </p>
  <dl id="l_1">
  <dt><b>1.</b></dt>
  <!-- Sec='MIMPARS Parameters' Level=0 Label='1' Line='1.' -->
  <dd>If the file <span style="font-family: monospace;">"cal.men"</span> is present in the calibration directory it
  is read to find translations between the filter string and the calibration
  name.  The translations consist of two columns with the full filter string
  and the calibration name.  If either contains spaces then it must be
  quoted.  For example:
  <div class="highlight-default-notranslate"><pre>
  "OIII Mosaic N2"    O3
  </pre></div>
  </dd>
  </dl>
  <dl id="l_2">
  <dt><b>2.</b></dt>
  <!-- Sec='MIMPARS Parameters' Level=0 Label='2' Line='2.' -->
  <dd>If the file is not present or a match to the filter string is not
  found then the first word of the filter string is used with non-alphanumeric
  characters replaced by <span style="font-family: monospace;">'_'</span>.  For example, <span style="font-family: monospace;">"OIII Mosaic N2"</span> is mapped to
  OIII.
  </dd>
  </dl>
  <dl id="l_3">
  <dt><b>3.</b></dt>
  <!-- Sec='MIMPARS Parameters' Level=0 Label='3' Line='3.' -->
  <dd>If the name arrived at by the first two methods fails then a calibration
  called <span style="font-family: monospace;">"default"</span> in the calibration directory is sought.
  </dd>
  </dl>
  <p>
  Note that one may use the <span style="font-family: monospace;">"cal.men"</span> file or not and one can use logical
  links to provide explicit mappings between filters for which a calibration
  has been generated and those which have not in addition to making <span style="font-family: monospace;">"default"</span>
  link to some particular filter calibration.
  </p>
  </section>
  <section id="s_real_time_display_with_the_dca">
  <h3>Real-time display with the dca</h3>
  <p>
  At the telescope with the NOAO Mosaic, the data capture agent (DCA) has
  controls to select processing during the readout automatic display.  One
  toggle is equivalent to the <i>process</i> parameter.  If the processing is
  turned on the DCA automatically selects only overscan bias subtraction for
  non-object exposures and selects both bias subtraction and flat field
  division for object exposures.  The <i>filter</i> parameter is set by
  passing through the filter string from the data acquisition system or by
  overriding this and using the filter menu to select one of the available
  calibrations.
  </p>
  </section>
  <section id="s_creation_of_otf_flat_fields">
  <h3>Creation of otf flat fields</h3>
  <p>
  Begin by reducing the flat field data.  This could be from combining a
  sequence of dome flat exposures or it could be more ambitious super sky
  flat field.  The reduced flat field would normally be trimmed to remove the
  bias.  A template raw flat field exposure needs to be kept to define the
  final OTF flat field size and keywords.  The OTF flat field needs to be
  the same size as the common raw exposures for efficiency since if the OTF
  flat field is a different size it will be adjusted to match the
  data being calibrated but at some computation expense.
  </p>
  <p>
  The OTF flat field is prepared from a real flat field using the task
  MSCOTFFLAT.  The parameters are
  </p>
  <div class="highlight-default-notranslate"><pre>
                             I R A F
              Image Reduction and Analysis Facility
  PACKAGE = mscred
     TASK = mscotfflat
  
  input   =               Input processed mosaic flat field
  output  =               Output OTF flat field
  template=               Template raw mosaic flat field
  (bin    =            2) Binning size
  (resolut=        0.005) Resolution
  </pre></div>
  <p>
  The input is the name of the reduced flat field exposure.  The output
  name is typically an abbreviated version of the filter name though
  it could be anything.  The template parameter is the name of a raw
  exposure.  Finally the two algorithm parameters described previously.
  </p>
  <p>
  An example showing the reduction of a sequence of flat field exposures
  to an OTF flat field for the <span style="font-family: monospace;">"V Mosaic"</span> filter follows.  This assumes the
  MSCRED, CCDPROC, and FLATCOMBINE parameters have been set as desired (
  basically the default values).
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; flatcombine flat*
  ms&gt; mscotfflat FlatV V Raw/flat001
  ms&gt; dir V
  flat1.pl     flat3.pl     flat5.pl     flat7.pl
  flat2.pl     flat4.pl     flat6.pl     flat8.pl
  </pre></div>
  <p>
  Note that the individual pixel list (pl files) can be examined using IRAF
  image tasks.  In particular, they can be display with <b>display</b>.
  </p>
  <p>
  To use this OTF flat field in the current directory
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; mscdisplay obj123 1 proc+ caldir="" filter=V
  </pre></div>
  <p>
  To use a standard directory and setup the filter name translation create
  or move the OTF directory and contents in the desired standard directory.
  In that directory create a file <span style="font-family: monospace;">"cal.men"</span> which has the filter name followed
  by the OTF calibration directory names.
  </p>
  <p>
  To place the OTF flat field in a standard directory and setup the filter
  name translation
  </p>
  <div class="highlight-default-notranslate"><pre>
  ms&gt; dir home$otfdir
  V       B       cal.men
  ms&gt; page home$otfdir/cal.men
  "V Mosaic"      V
  "B Mosaic"      B
  ms&gt; mscdisplay obj123 1 proc+ caldir=home$otfdir/ filter=!filter
  </pre></div>
  <p>
  If you are creating OTF flat field for users of the NOAO Mosaic at
  Kitt Peak the calibration directories are mscdb$noao/kpno/4meter/caldir/
  and mscdb$noao/kpno/36inch/caldir/.
  </p>
  
  </section>
  
  <!-- Contents: 'Overview' 'Creating and Installing OTF Flat Fields at NOAO' 'OTF Flat Field Calibration Format' 'MIMPARS Parameters' 'Real-time Display with the DCA' 'Creation of OTF Flat Fields'  -->
  

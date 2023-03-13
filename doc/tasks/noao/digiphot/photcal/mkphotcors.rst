.. _mkphotcors:

mkphotcors: Prepare the photometric corrections files
=====================================================

**Package: photcal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkphotcors imsets idfilters obsparams shifts apercors
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_imsets">
  <dt><b>imsets</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imsets' Line='imsets' -->
  <dd>The name of the input/output text file of observations, where  a complete
  observation consists of an observation name usually the name of
  the observed star field,
  followed by a list of images of that star field taken through the filters
  <i>idfilters</i>.
  If <i>imsets</i> does not exist, MKPHOTCORS prompts the user for
  input and writes the results to a new image set file <i>imsets</i>.
  If <i>imsets</i> does exist, MKPHOTCORS reads the file and prints messages
  about any errors or inconsistencies it finds in it. If <i>imsets</i> is <span style="font-family: monospace;">""</span>,
  MKPHOTCORS prompts the user for input, but does not create a new <i>imsets</i>
  file.
  </dd>
  </dl>
  <dl id="l_idfilters">
  <dt><b>idfilters</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='idfilters' Line='idfilters' -->
  <dd>The list of filters separated by whitespace or commas which define a complete
  observation. If <i>imsets</i> is entered interactively by the user,
  <i>idfilters</i> defines the number of images in an
  observation. If <i>imsets</i> is an existing file, MKPHOTCORS uses
  the number of filters specified by <i>idfilters</i> to
  check that there are the correct number of images in each observation.
  </dd>
  </dl>
  <dl id="l_obsparams">
  <dt><b>obsparams</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obsparams' Line='obsparams' -->
  <dd>The name of the input/output text file containing the quantities filter id,
  exposure time, airmass, and time of observation, for each image in <i>imsets</i>.
  If <i>obsparams</i> does not exist, MKPHOTCORS prompts the user for input
  and writes the results to the new observing parameters file <i>obsparams</i>.
  If <i>obsparams</i> already exists, MKPHOTCORS reads the file using the format
  specified by <i>obscolumns</i>, and prints out messages about any
  errors and inconsistencies it finds.
  If <i>obsparams</i>
  is <span style="font-family: monospace;">""</span>, the user is not prompted for input and no output file is created.
  </dd>
  </dl>
  <dl id="l_shifts">
  <dt><b>shifts</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shifts' Line='shifts' -->
  <dd>The name of the input/output text file containing the x-y shifts to be applied
  to the measured x-y coordinates of each object in each image in <i>imsets</i>.
  If <i>shifts</i> does not exist, MKPHOTCORS prompts the user for input
  and writes the results to the new shifts file <i>shifts</i>.
  If <i>shifts</i> already exists, MKPHOTCORS reads the file and prints out
  messages about any errors and inconsistencies it finds.
  If <i>shifts</i> is <span style="font-family: monospace;">""</span>, the user is not prompted for input and no output
  file is created.
  </dd>
  </dl>
  <dl id="l_apercors">
  <dt><b>apercors</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apercors' Line='apercors' -->
  <dd>The name of the input/output text file containing the aperture corrections
  to be applied
  to the measured magnitudes of each object in each image in <i>imsets</i>.
  If <i>apercors</i> does not exist, MKPHOTCORS prompts the user for input
  and writes the results to the new aperture corrections file <i>apercors</i>.
  If <i>apercors</i> already exists, MKPHOTCORS reads the file and prints out
  messages about any errors and inconsistencies it finds.
  If <i>apercors</i> is <span style="font-family: monospace;">""</span>, the user is not prompted for input and no output
  file is created.
  </dd>
  </dl>
  <dl id="l_obscolumns">
  <dt><b>obscolumns = <span style="font-family: monospace;">"2 3 4 5"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obscolumns' Line='obscolumns = "2 3 4 5"' -->
  <dd>The list of numbers separated by commas or whitespace specifying which 
  columns in <i>obsparams</i> contain the filter ids, exposure times,
  airmasses, and times of observation, respectively of the images listed in column 1.
  <i>Obscolumns</i> is only used if <i>obsparams</i> already exists on disk.
  The number 0 may be used as a place holder in the <i>obscolumns</i> string.
  For example to read in only the airmass values, <i>obscolumns</i> should be
  set to <span style="font-family: monospace;">"0 0 column"</span> if the airmass values are in column.
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = no' -->
  <dd>Verify all data entered interactively ?
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about actions taken by MKPHOTCORS, and any warning or error
  messages generated.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MKPHOTCORS takes an image set file <i>imsets</i> and a list of filter ids
  <i>idfilters</i> and writes one or more of the photometric corrections files
  <i>obsparams</i>, <i>shifts</i> and <i>apercors</i> required by the
  preprocessor tasks MKNOBSFILE and MKOBSFILE. MKPHOTCORS is intended as
  a simple tool to assist the user in creating and/or checking the input
  required by the MKNOBSFILE and MKOBSFILE tasks.
  </p>
  <p>
  <i>Imsets</i> is the name of the input/output text file which tells
  MKNOBSFILE or MKOBSFILE which
  observations are to be extracted from the photometry files.
  A complete observation consists of the observation name,
  for example <span style="font-family: monospace;">"M92"</span>, followed by a list of images
  taken through the filters <i>idfilters</i>, for example <span style="font-family: monospace;">"m92u m92b m92v"</span>. 
  Observations are listed in <i>imsets</i>, 1 observation per line, with the
  observation name in column 1, a colon in column 2, followed by, in filter
  order and separated by whitespace, the names of the images belonging
  to that observation. A sample image set file is shown in the next section.
  </p>
  <p>
  <i>Imsets</i> may be an existing file created with the MKIMSETS task, a file
  typed in by hand by the user, or a new file to be created by MKPHOTCORS.
  If <i>imsets</i> already exists, MKPHOTCORS reads the file and prints warning
  messages if it cannot decode the observations specification, or if the
  number of images in the observation does not match the number specified
  by <i>idfilters</i>. If imsets does not exist, MKPHOTCORS prompts the user
  for input using <i>idfilters</i> to determine the number of images
  there should be in each observation, and writes the results to the new
  image set file <i>imsets</i>. If <i>imsets</i> is <span style="font-family: monospace;">""</span>, MKPHOTCORS prompts
  the user for input but does not save the results.
  </p>
  <p>
  <i>Obsparams</i> is the name of the input/output text file listing the
  observing parameters filter id, exposure time, airmass, and time of observation,
  for the images in
  <i>imsets</i>. <i>Obsparams</i> is used to correct missing or incorrect
  filter ids, exposure times, airmasses, and times of observation in the photometry files, and
  is not required if all these values are correctly recorded in the photometry
  files. The observing parameters for each image are listed in
  <i>obsparams</i>, 1 image per line, with the image name in column 1, and the
  filter id, exposure time, airmass, and time of observation in the columns <i>obscolumns</i>.
  A sample observing parameters file is shown in the next section.
  </p>
  <p>
  <i>Obsparams</i> may be an existing file created with the MKIMSETS task,
  a file typed in by hand by the user, or a new file to be created by
  MKPHOTCORS. If <i>obsparams</i> already exists, MKPHOTCORS reads the file
  and prints warning messages if it cannot decode the observing parameters,
  or if the there is an entry which does not correspond to one of the images
  listed in <i>imsets</i>. If <i>obsparams</i> does not exist, MKPHOTCORS
  prompts the user for input for each image in <i>imsets</i> and
  writes the results to a new observing parameters file <i>obsparams</i>.
  If <i>obsparams</i> is <span style="font-family: monospace;">""</span>,  MKPHOTCORS does not prompt for input and no new
  file is written.
  </p>
  <p>
  <i>Shifts</i> is the name of the text file specifying the x-y shifts, as
  a function of image, to be
  added to the x-y positions of all objects in the images listed in <i>imsets</i>.
  These shifts are
  used to brings frames of the same star field taken through different
  filters into rough alignment before matching individual objects.
  <i>Shifts</i> is not required if the frame to frame shifts are
  small, as is usually the case if the filters are of comparable thickness,
  and the exposures are short or well-guided.  The x-y shifts are listed 1
  per line with the name of the image in column 1, and the x and y shifts in
  columns 2 and 3 respectively.
  A sample shifts file is shown in the next section.
  </p>
  <p>
  <i>Shifts</i> may be an existing file created with the IMCENTROID task and
  edited by the user,
  a file typed in by hand by the user, or a new file to be created by
  MKPHOTCORS. If <i>shifts</i> already exists, MKPHOTCORS reads the file
  and prints warning messages if it cannot decode the shifts,
  or if the there is an entry which does not correspond to one of the images
  listed in <i>imsets</i>. If <i>shifts</i> does not exist, MKPHOTCORS
  prompts the user for input for each of the images in <i>imsets</i> and
  writes the results to a new shifts file <i>shifts</i>.
  If <i>shifts</i> is <span style="font-family: monospace;">""</span>,  MKPHOTCORS does not prompt for input and no new
  file is written.
  </p>
  <p>
  <i>Apercors</i> is the name of the text file specifying the aperture
  corrections, as a function of image,  to be added to the magnitudes of all
  objects in the images listed in <i>imsets</i>.
  The aperture corrections are most often used to correct the instrumental
  magnitudes of stars
  measured through a small aperture to minimize crowding affects, to the
  instrumental magnitudes of standard stars measured through a larger
  aperture. These aperture corrections will normally be a function of filter
  and of seeing and focus which can change throughout the night.
  Aperture corrections are normally not required for standard star measurements.
  Aperture corrections are listed 1 per line with
  the name of the image in column 1, and the aperture correction in column 2.
  A sample aperture corrections file is shown in the next section.
  </p>
  <p>
  <i>Apercors</i> may be an existing file
  typed in by hand by the user, or a new file to be created by
  MKPHOTCORS. If <i>apercors</i> already exists, MKPHOTCORS reads the file
  and prints warning messages if it cannot decode the aperture corrections,
  or if the there is an entry which does not correspond to one of the images
  listed in <i>imsets</i>. If <i>apercors</i> does not exist, MKPHOTCORS
  prompts the user for input for each of the images in <i>imsets</i> and
  writes the results to a aperture corrections file <i>apercors</i>.
  If <i>apercors</i> is <span style="font-family: monospace;">""</span>,  MKPHOTCORS does not prompt for input and no new
  file is written.
  </p>
  </section>
  <section id="s_output">
  <h3>Output</h3>
  <p>
  A sample image set file for a set of UBV 100 second, 600 seconds, and 
  1800 second exposure images of the globular cluster m92 is shown below.
  The labels <span style="font-family: monospace;">"M92S"</span>, <span style="font-family: monospace;">"M92M"</span>, and <span style="font-family: monospace;">"M92L"</span> stand for the  100, 600, 1800 second
  exposure observations sets respectively. The names which follow the labels are
  the names of the actual IRAF images comprising each data set. The image names
  must match those in the photometry files.
  </p>
  <div class="highlight-default-notranslate"><pre>
  M92S : m92us  m92bs m92vs
  M92M : m92um  m92bm m92vm
  M92L : m92ul  m92bl m92vl
  </pre></div>
  <p>
  A sample observing parameters file is shown for the above data set. In this
  example the user forgot to tell the photometry code to pick up the filter ids,
  exposure times, airmasses, and times of observation from the image headers and
  so is obliged to
  correct them after the fact via the observing parameters file. The filters
  U B V are represented by the numbers 1 2 3. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  m92us  1  100   1.10 03:10:53
  m92bs  2  100   1.09 03:14:06
  m92vs  3  100   1.06 03:18:54
  m92um  1  600   1.03 04:15:05
  m92bm  2  600   1.03 04:29:43
  m92vm  3  600   1.03 04:44:56
  m92ul  1  1800  1.06 06:10:33
  m92bl  2  1800  1.12 06:45:32
  m92vl  3  1800  1.18 07:23:02
  </pre></div>
  <p>
  A sample shifts file for the above data set is shown below.
  Only the long exposure frames have significant frame to frame shifts
  so only those images are included in the shifts file.
  The long u frame is used a position reference so its x-y shift is zero.
  </p>
  <div class="highlight-default-notranslate"><pre>
  m92ul  0.0  0.0
  m92bl  5.4  8.4
  m92vl  9.6  17.1
  </pre></div>
  <p>
  A sample aperture corrections file for the above data set is shown below.
  Note that the aperture correction appears to vary in a systematic
  way  with filter.
  </p>
  <div class="highlight-default-notranslate"><pre>
  m92us  -.153
  m92bs  -.110
  m92vs  -.083
  m92um  -.149
  m92bm  -.108
  m92vm  -.090
  m92ul  -.160
  m92bl  -.123
  m92vl  -.079
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Type in the image set file and accompanying shifts and aperture corrections
  files  for a set of UBV observations of a crowded field in NGC4147. The filter
  ids <span style="font-family: monospace;">"1 2 3"</span> stand
  for <span style="font-family: monospace;">"U B V"</span>. The photometry programs picked up the correct values of
  the filter id, exposure time, and airmass from the image headers
  and wrote them to the photometry
  files so the observing parameters file is not required.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; mkphotcors n4147.imsets "1,2,3" "" n4147.shifts n4147.apcors
  </pre></div>
  <p>
  2. Type in the shifts and aperture corrections files for the already
  existing image set file m17.imsets. In this case the filter set is <span style="font-family: monospace;">"J H K"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; mkphotcors m17.imsets "J,H,K" "" m17.shifts m17.apcors
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  mkimsets,mknobsfile,mkobsfile
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'OUTPUT' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

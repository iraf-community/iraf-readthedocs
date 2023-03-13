.. _obsfile:

obsfile: Prepare an observations file from a text file
======================================================

**Package: photcal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  obsfile photfiles incolumns idfilters imsets observations
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_photfiles">
  <dt><b>photfiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='photfiles' Line='photfiles' -->
  <dd>A list of text files containing the image names or an image id, x-y positions,
  magnitudes, magnitude errors, airmasses, filter ids, exposure times, and time
  of observation of all the measured objects. <i>Photfiles</i> are assumed to be
  the output of the user's own digital photometry program. All the files in the
  list must have the format specified by <i>incolumns</i>.
  </dd>
  </dl>
  <dl id="l_incolumns">
  <dt><b>incolumns</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='incolumns' Line='incolumns' -->
  <dd>A list of ten numbers separated by commas or whitespace specifying which
  columns in <i>photfiles</i> contain the following fields: the image name or id,
  x coordinate, y coordinate, filter id, exposure time, airmass, time of
  observation, instrumental magnitude, magnitude error, and object id
  respectively.  
  </dd>
  </dl>
  <dl id="l_idfilters">
  <dt><b>idfilters</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='idfilters' Line='idfilters' -->
  <dd>The list of filter ids separated by whitespace or commas which define a
  complete observation. The filter ids must correspond to those in
  <i>photfiles</i>.
  </dd>
  </dl>
  <dl id="l_imsets">
  <dt><b>imsets</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imsets' Line='imsets' -->
  <dd>The name of the text file which lists the observations of each field, assigns a
  name to each field, and tells OBSFILE which images belong to the same
  observation of that field. Only observations corresponding to the images
  specified in <i>imsets</i> will be extracted from <i>photfiles</i>. Observations
  are listed in <i>imsets</i>, 1 observation per line with the field name in
  column 1, a colon in column 2, followed by, in filter order and separated by
  whitespace, the names of the images of that field belonging to that
  observation. The format of <i>imsets</i> is described in detail below.
  </dd>
  </dl>
  <dl id="l_observations">
  <dt><b>observations</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observations' Line='observations' -->
  <dd>The output observations file suitable for input to FITPARAMS or
  EVALFIT/INVERTFIT.
  </dd>
  </dl>
  <dl id="l_wrap">
  <dt><b>wrap = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='wrap' Line='wrap = yes' -->
  <dd>Format the output observations file for easy reading ? If wrap = yes then the
  observation in each filter are written on a separate line and the * character
  in column 1 is interpreted as a continuation character. Otherwise all the
  observations for a single filter are written on a single line where the maximum
  length of a line is SZ_LINE characters.
  </dd>
  </dl>
  <dl id="l_obsparams">
  <dt><b>obsparams = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obsparams' Line='obsparams = ""' -->
  <dd>The name of an optional text file containing the correct filter ids, exposure
  times, airmasses, and time of observations for each image whose values are
  either undefined or incorrectly stored in <i>photfiles</i>. The observing
  parameters for each image are listed in the file <i>obsparams</i>, 1 image per
  line with the image name in column 1 and the filter ids, exposure times,
  airmasses, and times of observation listed in columns <i>obscolumns</i>. The
  image names must match those in <i>imsets</i>. Images which have no entries in
  <i>obsparams</i> are assigned the values stored in <i>photfiles</i>.
  </dd>
  </dl>
  <dl id="l_obscolumns">
  <dt><b>obscolumns = <span style="font-family: monospace;">"2 3 4 5"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='obscolumns' Line='obscolumns = "2 3 4 5"' -->
  <dd>The list of numbers separated by commas or whitespace specifying which columns
  in the text file <i>obsparams</i> contain the correct filter ids, exposure
  times, airmasses, and times of observation respectively. The number 0 can be
  used as a place holder in the <i>obscolumns</i> string. For example, to correct
  only  the <i>photfiles</i> airmass values, <i>obscolumns</i> should be set to
  <span style="font-family: monospace;">"0 0 column 0"</span>, where column is the airmass column number. The default value of
  <i>obscolumns</i> corresponds to the format of the default <i>obsparams</i> file
  produced by MKIMSETS.
  </dd>
  </dl>
  <dl id="l_minmagerr">
  <dt><b>minmagerr = 0.001</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minmagerr' Line='minmagerr = 0.001' -->
  <dd>The error that will be assigned to a non-INDEF valued magnitude measurement
  whose recorded error is less than <i>minmagerr</i>.
  </dd>
  </dl>
  <dl id="l_shifts">
  <dt><b>shifts = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='shifts' Line='shifts = ""' -->
  <dd>The name of the text file specifying the x and y shifts to be ADDED to the x-y
  positions of all objects in an image before position matching (the original x's
  and y's are retained in the output). Shifts are listed for each image, 1 image
  per line with the name of the image in column 1, followed by the x and y shifts
  in columns 2 and 3 respectively. Image names must match those in <i>imsets</i>.
  Images for which no shift is supplied are assigned x and y shifts of zero.
  </dd>
  </dl>
  <dl id="l_apercors">
  <dt><b>apercors = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apercors' Line='apercors = ""' -->
  <dd>The name of the text file specifying the aperture corrections to be ADDED to
  the extracted magnitudes. Aperture corrections are listed for each image, 1
  image per line with the name of the image in column 1, followed by the aperture
  correction in magnitudes in column 2.  The image names must match those in
  <i>imsets</i>. Images for which no aperture correction is supplied are assigned
  a default value of zero.
  </dd>
  </dl>
  <dl id="l_normtime">
  <dt><b>normtime = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='normtime' Line='normtime = no' -->
  <dd>Normalize the magnitudes to an exposure time of one time unit using the
  exposure times in <i>photfiles</i>.
  </dd>
  </dl>
  <dl id="l_tolerance">
  <dt><b>tolerance = 5.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tolerance' Line='tolerance = 5.0' -->
  <dd>The tolerance in pixels for matching objects in the same observation, but
  different images.  OBSFILE extracts the x and y coordinates of each object
  in each image of a given observation from <i>photfiles</i>, adds the shift for
  that image in <i>shifts</i> to the extracted x-y coordinates, and matches the
  objects to within <i>tolerance</i> pixels. Missing objects are assigned INDEF
  entries in <i>observations</i>. If <i>tolerance</i> is less than or equal to 0
  no coordinate matching is done, and objects are matched in order of occurrence
  with missing objects being assigned INDEF values.
  </dd>
  </dl>
  <dl id="l_allfilters">
  <dt><b>allfilters = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='allfilters' Line='allfilters = no' -->
  <dd>Output only objects which are successfully matched in all the filters specified
  by <i>idfilters</i>?
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = no' -->
  <dd>Verify interactive user input? This option is used only if any of <i>imsets</i>,
  <i>obsparams</i>, <i>shifts</i>, or <i> apercors</i> are set to the standard input
  <span style="font-family: monospace;">"STDIN"</span>.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages about actions taken by the task or any warnings or errors
  encountered?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  OBSFILE takes a list of user generated text files <i>photfiles</i>, where each
  file contains  observations of one or more objects taken through one or more
  filters, and the image set file <i>imsets</i>, and prepares a single
  observations file <i>observations</i>. OBSFILE is intended for use with any
  user digital stellar photometry program which writes its output in simple text
  files format.
  </p>
  <p>
  OBSFILE performs the following functions: 1) extracts the quantities
  image name or image id, x and y position, filter id, exposure time, airmass,
  time of observation, magnitude, and magnitude error from
  <i>photfiles</i>, 2) corrects any erroneous or missing values of filter id,
  exposure time, airmass, or time of observation in <i>photfiles</i>,  3) associates each 
  field with one or more sets of images of that
  field taken through different filters 4) matches individual objects within
  a given observation by order of occurrence or x-y position, and
  5) assigns a unique name to each object in each field.
  </p>
  <p>
  The parameter <i>incolumns</i> describes the format of <i>photfiles</i>.
  <i>Incolumns</i> is a list of ten numbers separated by commas or whitespace
  which specify the columns containing the following fields: the
  image name or id,
  the x coordinate, the y coordinate, the filter id, the exposure time, 
  the airmass, the time of observation the instrumental magnitude, the
  magnitude error, and the object id.
  For example
  if <i>incolumns</i> is <span style="font-family: monospace;">"10 2 3 6 8 7 9 4 5 1"</span>, the object id is assumed to
  be in column 1, the image id in column 10, the x and y positions in columns 2 and 3, the filter id,
  exposure time, airmass, and time of observation in columns 6, 8, 7 and 9,
  and the instrumental
  magnitude and magnitude error in columns 4 and 5. The image names must
  match those in <i>imsets</i> or the corresponding input data is skipped.
  The columns image name, x coordinate, y coordinate, and magnitude
  are mandatory and must be present in <i>photfiles</i>. 
  Other missing columns in the data may be represented by a <span style="font-family: monospace;">"0"</span> in the
  appropriate place in <i>incolumns</i>.
  For example, if there is no magnitude error
  column in <i>photfiles</i> a value of INDEF will be written in the appropriate
  column in <i>observations</i>. 
  If there is no airmass column in <i>photfiles</i> the value in
  <i>obspararms</i> if any, or the value INDEF will be written to the appropriate
  column in <i>observations</i>. 
  If there is no filter id column in <i>photfiles</i> the value in
  <i>obspararms</i> if any, or one of the values in <i>idfilters</i>
  will be written to the appropriate column in <i>observations</i>. 
  If there is no exposure time column in <i>photfiles</i> the value in
  <i>obspararms</i> if any, or a value of one will be assumed.
  If there is no time of observation time column in <i>photfiles</i> the value in
  <i>obspararms</i> if any, or a value of INDEF will be assumed.
  </p>
  <p>
  The image set file <i>imsets</i> assigns a name to each field.
  For fields containing only a single standard star this name should
  match the name of the standard star in the standard star catalog.
  For fields containing more than one star, OBSFILE constructs a unique
  name for each object in the field by adding a sequence number to the 
  field name in <i>imsets</i>, which if the star is a standard star, the
  user must later edit. For example the fourth star in the field <span style="font-family: monospace;">"M92"</span>
  will be assigned the name <span style="font-family: monospace;">"M92-4"</span> in <i>observations</i>.
  If this star is a standard star and its true name is <span style="font-family: monospace;">"IX-10"</span> in the
  standard star catalog, then the user must change <span style="font-family: monospace;">"M92-4"</span> to <span style="font-family: monospace;">"IX-10"</span>
  in <i>observations</i>.
  <i>Imsets</i> also tells OBSFILE which images
  in <i>photfiles</i> are images of the same region of the sky belonging
  to the same observation.
  The format of <i>imsets</i> is described in detail below.
  If the number of observations is small the user may wish to simply type
  in <i>imsets</i> by hand. If the number of observations is large, a 
  separate task MKIMSETS is available to assist users in preparing
  <i>imsets</i>.
  </p>
  <p>
  Values of the filter ids, exposure times, airmasses, and times of observation,
  which are undefined or incorrect in <i>photfiles</i>,
  can be corrected by reading values listed in the columns <i>obscolumns</i>
  in the file <i>obsparams</i>. The format of <i>obsparams</i> is described
  in detail below.
  </p>
  <p>
  OBSFILE matches the objects in different images within the same observation
  either
  by order of occurrence if <i>tolerance</i> is less than or equal to 0.0,
  or by x-y position. Matching by position is done by identifying which objects
  in each of the
  images of a given field and observation set are within <i>tolerance</i>
  pixels of each other.  The user may supply an optional file of x and y
  shifts <i>shifts</i> to be added to the object positions prior to
  matching. The format of <i>shifts</i> is described in detail below.
  If the parameter <i>allfilters</i> is <span style="font-family: monospace;">"yes"</span>, only objects which are matched
  in all the filters <i>idfilters</i> are output to <i>observations</i>.
  </p>
  <p>
  OBSFILE permits the user to supply 
  an optional file of aperture corrections <i>apercors</i> containing
  magnitude corrections which are added to the instrumental
  magnitudes in <i>photfiles</i>.
  The format of <i>apercors</i> is described in detail below.
  </p>
  <p>
  Each new observations file created by OBSFILE has an associated format
  description file listing the column names and numbers in <i>observations</i>,
  of the fields extracted from <i>photfiles</i>. This file, referenced 
  by its parent observations file name, can be used as input to the
  MKCONFIG task. The actual name of the format description file on disk is
  constructed by prepending the string <span style="font-family: monospace;">"f"</span> and appending the string <span style="font-family: monospace;">".dat"</span>
  to <i>observations</i>.
  For example if a new observations file called <span style="font-family: monospace;">"nite1"</span> is created by
  OBSFILE, a format description file called <span style="font-family: monospace;">"fnite1.dat"</span> will also be
  created. Any pre-existing format description file of that name, which does
  not have an associated observations file, will be deleted.
  </p>
  <p>
  THE IMSETS FILE
  </p>
  <p>
  The <i>imsets</i> file lists the 
  the observations of each field, assigns a name to each
  field, and informs OBSFILE which images belong to the same
  observation of that field.
  Observations are listed in <i>imsets</i>, 1 observation
  per line with the field name in column 1, a colon in column 2,
  followed by the names of the
  images of that field for that observation separated by whitespace.
  Only data for image names in <i>imsets</i> which match those in
  <i>photfiles</i> will be extracted.
  </p>
  <p>
  The field name is used to generate the output object name in <i>observations</i>.
  If there is only a single measured object in the field, then the name
  of that object in <i>observations</i> will be the name of the field. If
  the single object is a standard star, the user should edit <i>imsets</i>
  so that the field name is the same as the name of the standard star in
  the standard star catalog. If a stellar field contains more than one
  measured object, OBSFILE generates names of the form <span style="font-family: monospace;">"field-#"</span> where
  <span style="font-family: monospace;">"field"</span> is the field name and <span style="font-family: monospace;">"#"</span> is a sequence number. For example the
  fourth star in the field <span style="font-family: monospace;">"M92"</span> will be assigned the name <span style="font-family: monospace;">"M92-4"</span> in
  <i>observations</i>. If the star is a standard star, the user must edit
  the object names in <i>observations</i> to match those in the standard
  star catalog.
  </p>
  <p>
  Any number of observations may have the same field name. This normally occurs,
  for example, when multiple observations of a single standard star of
  standard star field are made at several airmasses.
  </p>
  <p>
  If there
  are no filter ids in <i>photfiles</i> or <i>obsparams</i> then the images in
  each image set are assigned the filter ids in <i>idfilters</i> in order
  of occurrence.
  </p>
  <p>
  The <i>imsets</i> file for a  set of 50 UBV frames of fifteen standard star
  fields is listed below. There is only a single bright star per field.
  The name of star field in column 1 has been edited to be identical
  to the name of the standard in the standard star catalog. Column 2 contains
  a <span style="font-family: monospace;">':'</span>. The U, B and V
  images for each field are listed in columns 3, 4 and 5 respectively.
  The missing U image for field <span style="font-family: monospace;">"STD7"</span> is represented by the name <span style="font-family: monospace;">"INDEF"</span>.
  Standard stars <span style="font-family: monospace;">"STD1"</span> and <span style="font-family: monospace;">"STD2"</span> were observed twice in the same night
  at different airmasses.
  </p>
  <div class="highlight-default-notranslate"><pre>
  STD1 :  nite001   nite002  nite003
  STD1 :  nite045   nite046  nite047
  STD2 :  nite004   nite005  nite006
  STD2 :  nite048   nite049  nite050
  ...
  STD7 :  INDEF     nite019  nite020
  ...
  STD14 : nite039   nite040  nite041
  STD15 : nite042   nite043  nite044
  </pre></div>
  <p>
  THE OBSPARAMS FILE
  </p>
  <p>
  A sample corrections file <i>obsparams</i> for the previous set of
  UBV standards observations is shown below.
  The filter ids, exposure times, airmasses, and times of observation for all the images were
  correctly read
  from the image headers with the exception of the filter id, exposure time,
  and airmass for the first  <span style="font-family: monospace;">"STD2"</span> V frame.
  The correct filter id, exposure time, airmass, and time of observation, is supplied
  in <i>obsparams</i>  and <i>obscolumns</i> is set to <span style="font-family: monospace;">"2 3 4 5"</span>
  </p>
  <div class="highlight-default-notranslate"><pre>
  nite006    3 8 1.256 14:30:02.3
  </pre></div>
  <p>
  Zero can be used as a place holder in <i>obscolumns</i>,
  as in the following example where
  the user only wants to correct the exposure time and the airmass and
  leave the filter id alone. In this case <i>obscolumns</i> is <span style="font-family: monospace;">"0 2 3 0"</span>
  and <i>obsparams</i> looks as follows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  nite006    8 1.256
  </pre></div>
  <p>
  Only images listed in <i>imsets</i> can have their observing parameters
  modified by <i>obsparams</i>.
  </p>
  <p>
  THE SHIFTS FILE
  </p>
  <p>
  The file <i>shifts</i> lists the shifts for each image, 1 shift per line,
  with the image name in column 1 and the x and y shifts in columns 2 and
  3 respectively.
  The image names in <i>shifts</i> must match those in <i>imsets</i>.
  </p>
  <p>
  A sample shifts file for the previous set of UBV standards
  observations is shown below. All the standards except for <span style="font-family: monospace;">"STD14"</span> are assumed
  to have no significant shifts from filter to filter. The B and V frames
  for <span style="font-family: monospace;">"STD14"</span> are shifted -10 pixels in x and -5 pixels
  in y with respect to the U frame. Therefore +10 and +5 pixels should be
  added to the <span style="font-family: monospace;">"STD14"</span> B and V frame positions respectively before
  position matching.
  </p>
  <div class="highlight-default-notranslate"><pre>
  nite040   10.0   5.0
  nite041   10.0   5.0
  </pre></div>
  <p>
  An alternate way of listing the same observations would be the following.
  </p>
  <div class="highlight-default-notranslate"><pre>
  nite039   -10.0 -5.0
  </pre></div>
  <p>
  THE APERCORS FILE
  </p>
  <p>
  The file <i>apercors</i> lists the aperture corrections for each image,
  1 aperture correction per line,
  with the image name in column 1 and the aperture correction in magnitudes
  in column 2 respectively.
  The image names in <i>apercors</i> must match those in <i>imsets</i>.
  </p>
  <p>
  The <i>apercors</i> file for the previous set of UBV observations is shown
  below.
  The aperture corrections for all the standard stars are assumed to be
  zero except for <span style="font-family: monospace;">"STD14"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  nite039    -0.150
  nite040    -0.100
  nite041    -0.090
  </pre></div>
  </section>
  <section id="s_output">
  <h3>Output</h3>
  <p>
  For the previous set of UBV observations the output file
  <i>observations</i> produced by OBSFILE will look like the following.
  The filter ids for the U,B,V filters are assumed to be 1,2,3.
  Note that the exposure times are assumed to have been normalized either
  prior to running OBSFILE or by OBSFILE itself,
  and so are not included in <i>observations</i>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # FIELD   FILTER   OTIME  AIRMASS  X     Y     MAG   MERR
  
    STD1    1        .      .        .     .     .     .
    *       2        .      .        .     .     .     .
    *       3        .      .        .     .     .     .
    STD1    1        .      .        .     .     .     .
    *       2        .      .        .     .     .     .
    *       3        .      .        .     .     .     .
    STD2    1        .      .        .     .     .     .
    *       2        .      .        .     .     .     .
    *       3        .      .        .     .     .     .
    STD2    1        .      .        .     .     .     .
    *       2        .      .        .     .     .     .
    *       3        .      .        .     .     .     .
    ........................................................
    STD7    INDEF    INDEF  INDEF    INDEF INDEF INDEF INDEF
    *       2        .      .        .     .     .     .
    *       3        .      .        .     .     .     .
    .......................................................
    STD14   1        .      .        .     .     .     .
    *       2        .      .        .     .     .     .
    *       3        .      .        .     .     .     .
    STD15   1        .      .        .     .     .     .
    *       2        .      .        .     .     .     .
    *       3        .      .        .     .     .     .
  </pre></div>
  <p>
  The accompanying format description file has the following form.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Declare the observations file variables
  
  observations
  
  X1            3              # airmass in filter 1
  T1            4              # time of observation in filter 1
  x1            5              # x coordinate in filter 1
  y1            6              # y coordinate in filter 1
  m1            7              # instrumental magnitude in filter 1
  error(m1)     8              # magnitude error in filter 1
  
  X2            10             # airmass in filter 2
  T2            11             # time of observation in filter 2
  x2            12             # x coordinate in filter 2
  y2            13             # y coordinate in filter 2
  m2            14             # instrumental magnitude in filter 2
  error(m2)     15             # magnitude error in filter 2
  
  X3            16             # airmass in filter 3
  T3            17             # time of observation in filter 3
  x3            18             # x coordinate in filter 3
  y3            19             # y coordinate in filter 3
  m3            20             # instrumental magnitude in filter 3
  error(m3)     21             # magnitude error in filter 3
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Prepare an observations file, from a set of standard star observations
  in a file output by the user's own digital stellar photometry program,
  for input to FITPARAMS. A sample of the file illustrating the format
  is shown below.
  Since there is only one star per field, position matching is not necessary.
  The magnitudes have already been normalized to unit exposure time by the
  user's program, and the filter ids and airmasses are correct. However the
  observing time column is missing and represented by a zero in the incolumns
  parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; head magsfile
  
      ... print out the first few lines of the photometry file
  
      std1u   40.4   50.3   18.059   0.043   U   1.030   1.0
      std1b   42.5   53.1   17.089   0.023   B   1.032   1.0
      std1v   43.8   56.9   16.023   0.020   V   1.034   1.0
      std2u   39.4   55.3   17.029   0.040   U   1.135   1.0
      std2b   41.5   57.3   15.905   0.020   B   1.140   1.0
      std2v   42.6   58.9   14.899   0.018   V   1.144   1.0
      .....   ....   ....   ......   .....   .   .....   ...
      .....   ....   ....   ......   .....   .   .....   ...
  
  ph&gt; type fields
  
      ... print out the corresponding image set file
  
      std1 : std1u  std1b  std1v
      std2 : std2u  std2b  std2v
      ..... .....  .....  .....
      ..... .....  .....  .....
  
  ph&gt; obsfile magsfile "1 2 3 6 8 7 0 4 5" "U,B,V" fields standards.obs\
      tol=0.0
  
      ... create the observations file
  
  ph&gt; edit standards.obs
  
      ... edit the observations file so that the object names
          match those in the standard star catalog
  </pre></div>
  <p>
  2. Prepare an observations file from a set of program star observations
  of a crowded field in the globular cluster M92 computed by the same
  digital photometry
  program as above, for input to FITPARAMS.  The 3 input files contain UBV
  measurements of over 2000 stars in the M92 field. Since the same stars
  were not measured in all filters position matching is necessary.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; head m92umags,m92bmags,m92vmags
  
      ... print the first few lines of the input files on the
          standard output
  
      m92u    80.4   42.3   17.046   0.046   U   1.056   1.0
      m92u    ....   ....   ......   .....   U   1.056   1.0
  
      m92b    62.6   81.1   18.071   0.041   B   1.030   1.0
      m92b    ....   ....   ......   .....   B   1.030   1.0
  
      m92v    33.8   26.9   16.023   0.022   V   1.034   1.0
      m92v    ....   ....   ......   .....   V   1.034   1.0
  
  ph&gt; type fields
  
      ... print out the image set file
  
      m92 : m92u  m92b  m92v
  
  ph&gt; obsfile m92umags,m92bmags,m92vmags "1 2 3 6 8 7 0 4 5" "U,B,V"\
      fields standards.obs tolerance=8.0
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
  

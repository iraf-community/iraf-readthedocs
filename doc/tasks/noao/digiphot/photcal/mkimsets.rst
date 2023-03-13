.. _mkimsets:

mkimsets: Prepare an image set file for input to (mk)(n)obsfile
===============================================================

**Package: photcal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkimsets imlist idfilters imsets 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_imlist">
  <dt><b>imlist</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imlist' Line='imlist' -->
  <dd>The file(s) containing all the image names and filter ids associated with
  the observations.
  <i>Imlist</i> is a list of APPHOT/DAOPHOT databases if <i>input</i> =
  <span style="font-family: monospace;">"photfiles"</span>, a list of images if <i>input</i> = <span style="font-family: monospace;">"images"</span>, or the name
  of a user text file if <i>input</i> = <span style="font-family: monospace;">"user"</span>.
  The default input is a list of APPHOT/DAOPHOT databases.
  </dd>
  </dl>
  <dl id="l_idfilters">
  <dt><b>idfilters</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='idfilters' Line='idfilters' -->
  <dd>The ids of the filters, separated by whitespace or
  commas, which define a complete observation.
  The order in which the filter ids are listed in the string <i>idfilters</i>
  determines the order in which the image names associated with each observation
  are written in <i>imsets</i>.
  </dd>
  </dl>
  <dl id="l_imsets">
  <dt><b>imsets</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imsets' Line='imsets' -->
  <dd>The name of the output image set file which lists each observation of
  each star field, assigns a name
  to each observation, and specifies which images belong to the same
  observation of that star field.
  </dd>
  </dl>
  <dl id="l_imobsparams">
  <dt><b>imobsparams = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='imobsparams' Line='imobsparams = ""' -->
  <dd>The name of the output image list file containing the image name,
  the filter id,
  and the quantities specified by <i>fields</i>, for each
  unique image referenced in <i>imlist</i>.
  <i>Imobsparams</i> includes changes made by the user if <i>edit</i> is
  <span style="font-family: monospace;">"yes"</span>. If <i>imobsparams</i> is <span style="font-family: monospace;">""</span> the output image list
  is not saved.
  </dd>
  </dl>
  <dl id="l_input">
  <dt><b>input = photfiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input = photfiles' -->
  <dd>The source of the information used to create the image set file.
  The options are:
  <dl>
  <dt><b>photfiles</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='photfiles' Line='photfiles' -->
  <dd>Extract the image list from the APPHOT/DAOPHOT 
  databases containing
  the photometry. This option uses the PTOOLS task DUMP to extract
  the image name, the filter id, the exposure time, the airmass,  the
  time of observation, and
  other user selected fields <i>fields</i> from the database files.
  </dd>
  </dl>
  <dl>
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='images' Line='images' -->
  <dd>Extract the image list from the headers of the images containing
  the objects measured
  with APPHOT or DAOPHOT. This option uses the IMAGES task HSELECT to extract
  the image name, the filter id <i>filter</i>, and other user selected
  fields <i>fields</i> from the image headers. Useful additional fields
  might be the image title and the time of the observation.
  </dd>
  </dl>
  <dl>
  <dt><b>user</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='user' Line='user' -->
  <dd>Extract the image list from a user created file which has the
  image name in the first column, the filter id in the column
  <i>filter</i>, and 
  other useful information in the columns specified by <i>fields</i>.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_filter">
  <dt><b>filter</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='filter' Line='filter' -->
  <dd>The filter id keyword.
  <i>Filter</i> is always the APPHOT/DAOPHOT database keyword <span style="font-family: monospace;">"IFILTER"</span>
  if <i>input</i> is <span style="font-family: monospace;">"photfiles"</span>,
  the image header keyword which defines the filter id if <i>input</i> is
  <span style="font-family: monospace;">"images"</span>, or the number of the column
  containing the filter id, if <i>input</i> is <span style="font-family: monospace;">"user"</span>.
  </dd>
  </dl>
  <dl id="l_fields">
  <dt><b>fields = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fields' Line='fields = ""' -->
  <dd>The list of additional fields, besides the image name and filter id,
  to be extracted from <i>imlist</i>, separated by whitespace or commas.
  If <i>input</i> is <span style="font-family: monospace;">"photfiles"</span> <i>fields</i> is a list of APPHOT/DAOPHOT
  keywords including <span style="font-family: monospace;">"itime,xairmass"</span>; if <i>input</i> is <span style="font-family: monospace;">"images"</span>
  <i>fields</i> is a list of image
  header keywords; if <i>input</i> is <span style="font-family: monospace;">"user"</span> <i>fields</i> is a list of the
  column numbers defining the fields to be extracted from the user file.
  <i>Fields</i> may include any quantities, for example airmass, image title, or
  the time of the observation, which aid the user in the interactive
  image name grouping process.
  </dd>
  </dl>
  <dl id="l_sort">
  <dt><b>sort = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sort' Line='sort = ""' -->
  <dd>Sort the extracted image list in order of the value of the quantity <i>sort</i>.
  <i>Sort</i> must be one of the fields
  <i>"image"</i>, <i>filter</i>, or <i>fields</i> if <i>input</i>
  is <span style="font-family: monospace;">"images"</span> or <span style="font-family: monospace;">"photfiles"</span>, or the column number in the user file of the
  field to be sorted on if <i>input</i> is <span style="font-family: monospace;">"user"</span>.
  <i>Sort</i> is used to reorder the image list 
  before entering the editor.
  </dd>
  </dl>
  <dl id="l_edit">
  <dt><b>edit = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='edit' Line='edit = yes' -->
  <dd>Edit the extracted image name list interactively, checking that the images
  belonging to a single observation are adjacent to one another in the list,
  and that the filter ids are present and match those in <i>idfilters</i>.
  For each observation there must be an image name for every filter
  in <i>idfilters</i>.
  Missing set members must be assigned the image name <span style="font-family: monospace;">"INDEF"</span> for undefined
  and the filter id of the missing observation.
  </dd>
  </dl>
  <dl id="l_rename">
  <dt><b>rename = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rename' Line='rename = yes' -->
  <dd>Enter new names for each observation of each field interactively.
  If <i>rename</i> is <span style="font-family: monospace;">"no"</span>, default names
  of the form <span style="font-family: monospace;">"OBS1"</span>, <span style="font-family: monospace;">"OBS2"</span>, ..., <span style="font-family: monospace;">"OBSN"</span> are assigned. If <i>rename</i> is <span style="font-family: monospace;">"yes"</span>,
  MKIMSETS prints each image set
  on the terminal and prompts the user for the new name.
  Images sets containing a single standard star observation should be assigned
  the name of the standard star in the standard star catalog.
  </dd>
  </dl>
  <dl id="l_review">
  <dt><b>review = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='review' Line='review = yes' -->
  <dd>Review and edit <i>imsets</i> to check that the image set names are correct
  and that the images names have been properly grouped into sets.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MKIMSETS is a script task which takes as input a list of
  the image names and filter ids, <i>imlist</i>, associated
  with objects whose magnitudes have been measured with APPHOT, DAOPHOT,
  or a user program, and produces the image set file <i>imsets</i> 
  required as input by the preprocessor tasks MKNOBSFILE or OBSFILE.
  MKIMSETS is used in conjunction with MKNOBSFILE OR OBSFILE to combine many
  individual digital photometry measurements, for example standard star
  measurements,
  into a single observations file. The source of the input image list is
  a list of IRAF images if <i>input</i> is <span style="font-family: monospace;">"images"</span>,
  a list of APPHOT or DAOPHOT database files if <i>input</i> is <span style="font-family: monospace;">"photfiles"</span>,
  or a user supplied text file if <i>input</i> is <span style="font-family: monospace;">"user"</span>.
  </p>
  <p>
  The output image set file <i>imsets</i> lists each observation of
  each star field, assigns a name supplied by the user
  to each observation, and specifies which images belong to the same
  observation of that star field.
  In the case of image sets which contain a single standard star measurement,
  the image set name should
  match the name of the standard star in the standard star catalog.
  </p>
  <p>
  The optional output image observing parameters file <i>imobsparams</i>
  lists each unique image in <i>imlist</i>, its
  filter id <i>filter</i>, and other user specified fields <i>fields</i>.
  <i>Imobsparams</i> may be edited by
  the user, and used by the preprocessor tasks MKNOBSFILE or OBSFILE
  to correct erroneous or undefined values of
  filter id, exposure time, airmass and time of observation in the input
  databases.  By default <i>imobsparams</i> is not written.
  </p>
  <p>
  After task initialization, MKIMSETS extracts each unique image name,
  the corresponding filter id stored in column <i>filter</i>,
  and the corresponding values of the user defined fields <i>fields</i>,
  from the input list <i>imlist</i>, and writes the resulting image list
  in tabular form to a temporary file.
  The temporary image list file contains the image name in column 1,
  the value of <i>filter</i> in column 2, and the values of
  any additional fields in succeeding columns in the order they were
  specified in <i>fields</i>.
  </p>
  <p>
  If <i>sort</i> is one of the extracted
  fields <span style="font-family: monospace;">"image"</span>, <i>filter</i>, or <i>fields</i>, MKIMSETS sorts the image
  list based on the values of <i>sort</i>, before writing the results to the
  the temporary image list file.
  </p>
  <p>
  If <i>edit</i> is <span style="font-family: monospace;">"yes"</span>, the user enters the text editor and edits the
  temporary image list interactively.
  The image list must be arranged so that members of each image set are
  adjacent to each other in the image list.
  Missing images may be represented by
  an INDEF in column 1, the appropriate filter id in column 2, and
  INDEF in any other columns.
  The edit step is necessary if the image names are not in any logical
  order in <i>imlist</i> for <i>input</i> = <span style="font-family: monospace;">"images"</span>,
  do not occur in any logical order in the APPHOT/DAOPHOT 
  databases for <i>input</i> = <span style="font-family: monospace;">"photfiles"</span>, or are not listed logically
  in <i>imlist</i> for <i>input</i> = <span style="font-family: monospace;">"user"</span>.
  At this point MKIMSETS saves the temporary image list in the text file
  <i>imobsparams</i>, if <i>imobsparams</i> is defined.
  </p>
  <p>
  After the initial edit, MKIMSETS groups the images in the temporary image list,
  by using the filter ids in <i>idfilters</i>, and assuming that the image
  names are in logical order.
  If <i>rename</i> is <span style="font-family: monospace;">"yes"</span>, MKIMSETS prompts the user for the name of each 
  image set. Otherwise the default names OBS1, OBS2, ..., OBSN are
  assigned.
  If <i>review</i> is <span style="font-family: monospace;">"yes"</span>, MKIMSETS enters the editor, permitting the user
  to review <i>imsets</i> and interactively
  correct any mistakes.
  Image sets are written to <i>imsets</i>, 1 set
  per line with the image set name in column 1, a colon in column 2,
  followed by, in filter order and separated by whitespace, the names of the
  images of that field, for that  observation.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Create an image set file from a list of APPHOT databases which
  contain UBV observations of 5 standard stars. The UBV filters are
  identified in the APPHOT databases by the filters ids <span style="font-family: monospace;">"1"</span>,<span style="font-family: monospace;">"2"</span>, <span style="font-family: monospace;">"3"</span> 
  respectively. There is one database file
  for each star measured. Since data for each of the stars was taken
  sequentially and the images were read sequentially off tape, the user
  requests MKIMSETS to sort the extracted data by image name. Note that
  the time of observation field was undefined in the input data sets.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; mkimsets *.mag.* "1,2,3" jan10.stdim sort="image"
  
     ... MKIMSETS constructs the image list and sorts on
         the image name
  
     ... MKIMSETS enters the editor and lists the first few
         lines of the intermediate image list file
  
     im001  1  3.0  1.150 INDEF
     im002  2  2.0  1.150 INDEF
     im003  3  2.0  1.140 INDEF
     im004  1  6.0  1.300 INDEF
     im005  2  4.0  1.300 INDEF
     im006  3  2.0  1.300 INDEF
     im007  1  5.0  1.263 INDEF
     im008  3  1.0  1.270 INDEF
     im009  2  3.0  1.270 INDEF
     im010  1  2.0  1.030 INDEF
     im011  3  10.0  1.030 INDEF
     im012  1  30.0  1.093 INDEF
     im013  2  20.0  1.110 INDEF
     im014  3  10.0  1.110 INDEF
  
     ... the user notices that standard 4 is missing a B
         observation and that the observations of standard 3
         are out of order and edits the file as follows
  
     im001  1  3.0  1.150 INDEF
     im002  2  2.0  1.150 INDEF
     im003  3  2.0  1.140 INDEF
     im004  1  6.0  1.300 INDEF
     im005  2  4.0  1.300 INDEF
     im006  3  2.0  1.300 INDEF
     im007  1  5.0  1.263 INDEF
     im009  2  3.0  1.270 INDEF
     im008  3  1.0  1.270 INDEF
     im010  1  2.0  1.030 INDEF
     INDEF  2  INDEF  INDEF INDEF
     im011  3  10.0  1.030 INDEF
     im012  1  30.0  1.093 INDEF
     im013  2  20.0  1.110 INDEF
     im014  3  10.0  1.110 INDEF
  
     ... the user quits the editor
  
     ... MKIMSETS groups the image list prompting for a
         name for each image set
  
     ... MKIMSETS enters the editor, displays the first few
         lines of the imsets file, and allows the user to
         correct any mistakes
  
     STD1 :    im001  im002  im003
     STD2 :    im004  im005  im006
     STD3 :    im007  im009  im008
     STD4 :    im010  INDEF  im011
     STD5 :    im012  im013  im014
  
     ... quit the editor
  </pre></div>
  <p>
  2. Create the image set file from the list of IRAF images associated with
  the APPHOT databases in example 1.  The images contain the image
  header keyword <span style="font-family: monospace;">"f1pos"</span> which specifies the filter id and which may assume
  the values <span style="font-family: monospace;">"1,2,3"</span> where <span style="font-family: monospace;">"1,2,3"</span> stand for <span style="font-family: monospace;">"U,B,V"</span>. 
  Since the data for the individual stars was taken sequentially the user
  requests MKIMSETS to print out value of the sidereal time stored in the
  image header keyword <span style="font-family: monospace;">"ST"</span>, and to sort on that
  parameter. The image title is also printed out as an image grouping
  aid to the user. It is placed last in the fields parameter because  any
  internal blanks in the title would otherwise confuse the sorting routine.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; mkimsets *.imh "1,2,3" jan10.stdim input="images" \
      filter="f1pos" fields="ST,i_title" sort="ST"
  
     ... MKIMSETS constructs the image list and sorts on
         the column containing the sidereal time
  
     ... MKIMSETS enters the editor and lists the first
         few lines of the temporary image list file, the sidereal
         time is in column 3 and the image title containing
         some blanks is in column 4
  
     im001  1  12:30:50.2   STD1 U filter
     im002  2  12:35:40.1   STD1 B
     im003  3  12:40:16.2   STD1 v filter
     im004  1  12:50:50.2   STD2
     im005  2  12:55:40.1   STD2 B
     im006  3  12:59:58.2   STD2 V
     im007  1  13:10:50.2   STD3 U
     im008  3  13:15:40.1   STD3 V
     im009  2  13:20:16.2   STD3 B
     im010  1  13:30:50.2   STD4 u
     im011  3  13:40:40.1   STD4 V
     im012  1  13:50:50.2   STD5 U
     im013  2  13:55:40.1   STD5 B
     im014  3  13:59:58.2   STD5 V
  
     ... the user notices that standard 4 is missing a B
         observation and that the observations of standard 3
         are out of order and edits the file as follows
  
     im001  1  12:30:50.2   STD1 U filter
     im002  2  12:35:40.1   STD1 B
     im003  3  12:40:16.2   STD1 v filter
     im004  1  12:50:50.2   STD2
     im005  2  12:55:40.1   STD2 B
     im006  3  12:59:58.2   STD2 V
     im007  1  13:10:50.2   STD3 U
     im009  2  13:20:16.2   STD3 B
     im008  3  13:15:40.1   STD3 V
     im010  1  13:30:50.2   STD4 u
     INDEF  2  INDEF        INDEF
     im011  3  13:40:40.1   STD4 V
     im012  1  13:50:50.2   STD5 U
     im013  2  13:55:40.1   STD5 B
     im014  3  13:59:58.2   STD5 V
  
     ... the user quits the editor
  
     ... MKIMSETS groups the edited image list prompting for a
         name for each image set
  
     ... MKIMSETS enters the editor, displays the first few
         lines of the image set file and permits the
         user to correct any mistakes
  
     STD1 :    im001  im002  im003
     STD2 :    im004  im005  im006
     STD3 :    im007  im009  im008
     STD4 :    im010  INDEF  im011
     STD5 :    im012  im013  im014
  
     ... quit the editor
  
     ... note that MKIMSETS did not save the output image list
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
  images.hselect,ptools.dump,mknobsfile,mkobsfile
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

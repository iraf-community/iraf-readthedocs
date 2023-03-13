.. _apedit:

apedit: Edit apertures interactively
====================================

**Package: kpnocoude**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  apedit input
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>List of input images for which apertures are to be edited.
  </dd>
  </dl>
  <dl id="l_apertures">
  <dt><b>apertures = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='apertures' Line='apertures = ""' -->
  <dd>Apertures to recenter, resize, trace, and extract.  This only applies
  to apertures read from the input or reference database.  Any new
  apertures defined with the automatic finding algorithm or interactively
  are always selected.  The syntax is a list comma separated ranges
  where a range can be a single aperture number, a hyphen separated
  range of aperture numbers, or a range with a step specified by <span style="font-family: monospace;">"x&lt;step&gt;"</span>;
  for example, <span style="font-family: monospace;">"1,3-5,9-12x2"</span>.
  </dd>
  </dl>
  <dl id="l_references">
  <dt><b>references = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='references' Line='references = ""' -->
  <dd>List of reference images to be used to define apertures for the input
  images.  When a reference image is given it supersedes apertures
  previously defined for the input image. The list may be null, <span style="font-family: monospace;">""</span>, or
  any number of images less than or equal to the list of input images.
  If the reference image list is shorter than the input image list the
  last reference image is used for the remaining input images.
  There are three special words which may be used in place of an image
  name.  The word <span style="font-family: monospace;">"last"</span> refers to the last set of apertures written to
  the database.  The word <span style="font-family: monospace;">"OLD"</span> requires that an entry exist
  and the word <span style="font-family: monospace;">"NEW"</span> requires that the entry not exist for each input image.
  </dd>
  </dl>
  <dl id="l_interactive">
  <dt><b>interactive = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='interactive' Line='interactive = no' -->
  <dd>Run this task interactively?  If the task is not run interactively then
  all user queries are suppressed and interactive aperture editing is
  disabled.
  </dd>
  </dl>
  <dl id="l_find">
  <dt><b>find = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='find' Line='find = no' -->
  <dd>Find the spectra and define apertures automatically?  In order for
  spectra to be found automatically there must be no apertures for the
  input image or reference image defined in the database.
  </dd>
  </dl>
  <dl id="l_recenter">
  <dt><b>recenter = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='recenter' Line='recenter = no' -->
  <dd>Recenter the apertures?
  </dd>
  </dl>
  <dl id="l_resize">
  <dt><b>resize = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='resize' Line='resize = no' -->
  <dd>Resize the apertures?
  </dd>
  </dl>
  <dl id="l_edit">
  <dt><b>edit = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='edit' Line='edit = yes' -->
  <dd>Edit the apertures?  The <i>interactive</i> parameter must also be yes.
  </dd>
  </dl>
  <dl id="l_line">
  <dt><b>line = INDEF</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='line' Line='line = INDEF' -->
  <dd>The dispersion line (line or column perpendicular to the dispersion axis) to
  be graphed.  A value of INDEF uses the middle of the image.
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = 10</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = 10' -->
  <dd>Number of dispersion lines to be summed or medianed.  The lines are taken
  around the specified dispersion line.  A positive nsum selects a sum of
  lines and a negative selects a median of lines.
  </dd>
  </dl>
  <dl id="l_width">
  <dt><b>width = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='width' Line='width = 5.' -->
  <dd>Width of spectrum profiles.  This parameter is used for the profile
  centering algorithm in this and other tasks.
  </dd>
  </dl>
  <dl id="l_radius">
  <dt><b>radius = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='radius' Line='radius = 5.' -->
  <dd>The profile centering error radius for the centering algorithm.
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 0.' -->
  <dd>Centering threshold for the centering algorithm.  The range of pixel intensities
  near the initial centering position must exceed this threshold.
  </dd>
  </dl>
  </section>
  <section id="s_additional_parameters">
  <h3>Additional parameters</h3>
  <p>
  I/O parameters and the default dispersion axis are taken from the
  package parameters, the default aperture parameters are taken from the
  task <b>apdefault</b>.  Parameters for the various functions of finding,
  recentering, and resizing are taken from the parameters for the
  appropriate task.
  </p>
  <p>
  When this operation is performed from the task <b>apall</b> all parameters
  except the package parameters are included in that task.
  </p>
  </section>
  <section id="s_cursor_keys">
  <h3>Cursor keys</h3>
  <p>
  When editing the apertures interactively the following cursor keys are
  available.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ?    Print help
  a    Toggle the ALL flag
  b an Set background fitting parameters
  c an Center aperture(s)
  d an Delete aperture(s)
  e an Extract spectra (see APSUM)
  f    Find apertures up to the requested number (see APFIND)
  g an Recenter aperture(s) (see APRECENTER)
  i  n Set aperture ID
  j  n Set aperture beam number
  l ac Set lower limit of current aperture at cursor position
  m    Define and center a new aperture on the profile near the cursor
  n    Define a new aperture centered at the cursor
  o  n Enter desired aperture number for cursor selected aperture and
       remaining apertures are reordered using apidtable and maxsep
       parameters (see APFIND for ordering algorithm)
  q    Quit
  r    Redraw the graph
  s an Shift the center(s) of the current aperture to the cursor
       position
  t ac Trace aperture positions (see APTRACE)
  u ac Set upper limit of current aperture at cursor position
  w    Window the graph using the window cursor keys
  y an Set aperture limits to intercept the data at the cursor y
       position
  z an Resize aperture(s) (see APRESIZE)
  +  c Select the next aperture (in ID) to be the current aperture
  -  c Select the previous aperture (in ID) to be the current aperture
  I    Interrupt task immediately.  Database information is not saved.
  </pre></div>
  <p>
  The letter a following the key indicates if all apertures are affected when
  the ALL flag is set.  The letter c indicates that the key affects the
  current aperture while the letter n indicates that the key affects the
  aperture whose center is nearest the cursor.
  </p>
  </section>
  <section id="s_colon_commands">
  <h3>Colon commands</h3>
  <div class="highlight-default-notranslate"><pre>
  :show [file]       Print a list of the apertures (default STDOUT)
  :parameters [file] Print current parameter values (default STDOUT)
  :read [name]       Read from database (default current image)
  :write [name]      Write to database (default current image)
  </pre></div>
  <p>
  The remaining colon commands are task parameters and print the current
  value if no value is given or reset the current value to that specified.
  Use :parameters to see current parameter values.
  </p>
  <div class="highlight-default-notranslate"><pre>
  :apertures      :apidtable      :avglimits      :b_function
  :b_grow         :b_high_reject  :b_low_reject   :b_naverage
  :b_niterate     :b_order        :b_sample       :background
  :bkg            :center         :clean          :database
  :extras         :gain           :image          :line
  :llimit         :logfile        :lower          :lsigma
  :maxsep         :minsep         :npeaks         :nsubaps
  :nsum           :order          :parameters     :peak
  :plotfile       :r_grow         :radius         :read
  :readnoise      :saturation     :shift          :show
  :skybox         :t_function     :t_grow         :t_high_reject
  :t_low_reject   :t_naverage     :t_niterate     :t_nsum
  :t_order        :t_sample       :t_step         :t_width
  :threshold      :title          :ulimit         :upper
  :usigma         :weights        :width          :write
  :ylevel         :t_nlost
  </pre></div>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  For each image in the input image list, apertures are defined and edited
  interactively.  The aperture editor is invoked when the parameters
  <i>interactive</i> and <i>edit</i> are both yes.  When this is the case
  the task will query whether to edit each image.  The responses are
  <span style="font-family: monospace;">"yes"</span>, <span style="font-family: monospace;">"no"</span>, <span style="font-family: monospace;">"YES"</span>, and <span style="font-family: monospace;">"NO"</span>, where the upper case responses suppress
  queries for all following images.
  </p>
  <p>
  When the aperture editor is entered a graph of the image lines or
  columns specified by the parameters <i>line</i> and <i>nsum</i> is
  drawn.  In the <b>apextract</b> package a dispersion line is either a
  line or column in the image at one point along the dispersion axis.
  The dispersion axis may be defined in the image header under the
  keyword DISPAXIS or by the package parameter <i>dispaxis</i>.  The
  parameter <b>nsum</b> determines how many dispersion lines surrounding
  the specified dispersion line are summed or medianed.  This improves the
  signal in the profiles of weaker spectra.  Once the graph is drawn an
  interactive cursor loop is entered.  The set of cursor keys and colon
  commands is given above and may be printed when the task is running using
  the <span style="font-family: monospace;">'?'</span> key.  The CURSOR MODE keys and graph formatting options are also
  available (see <b>cursor</b> and <b>gtools</b>).
  </p>
  <p>
  A status line, usually at the bottom of the graphics terminal,
  indicates the current aperture and shows the ALL flag, <span style="font-family: monospace;">'a'</span> key, if set.  The
  concept of the current aperture is used by several of the aperture
  editing commands.  Other commands operate on the aperture whose center
  is nearest the cursor.  It is important to know which commands operate
  on the current aperture and which operate on the nearest aperture to
  the cursor.
  </p>
  <p>
  The cursor keys and colon commands are used to define new apertures,
  delete existing apertures, modify the aperture number, beam number,
  title, center, and limits, set background fitting parameters, trace the
  positions of the spectra in the apertures, and extract aperture
  spectra.  When creating new apertures default parameters are supplied
  in two ways; if no apertures are defined then the default parameters
  are taken from the task <b>apdefault</b> while if there is a current
  aperture then a copy of its parameters are made.
  </p>
  <p>
  The keys for creating a new aperture are <span style="font-family: monospace;">'m'</span> and <span style="font-family: monospace;">'n'</span> and <span style="font-family: monospace;">'f'</span>.  The key
  <span style="font-family: monospace;">'m'</span> marks a new aperture and centers the aperture on the profile
  nearest the cursor.  The centering algorithm is described under the
  help topic <b>center1d</b> and the parameters controlling the centering are
  <i>width</i>, <i>radius</i>, and <i>threshold</i>.  The key <span style="font-family: monospace;">'n'</span> defines a
  new aperture at the position of the cursor without centering.  This is
  used if there is no spectrum profile such as when defining sky apertures
  or when defining apertures in extended profiles.  The <span style="font-family: monospace;">'f'</span> key finds new
  apertures using the algorithm described in the task <b>apfind</b>.  The
  number of apertures found in this way is limited by the parameter
  <b>nfind</b> and the number includes any previously defined
  apertures.  The new aperture number, beam number, and title are assigned using
  the aperture assignment algorithm described in <b>apfind</b>.
  </p>
  <p>
  The aperture number for the aperture <i>nearest</i> the cursor is changed
  with the <span style="font-family: monospace;">'j'</span> key and the beam number is changed with the <span style="font-family: monospace;">'k'</span> key.  The
  user is prompted for a new aperture number or beam number.  The
  aperture title may be set or changed with the :title colon command.
  </p>
  <p>
  The <span style="font-family: monospace;">'o'</span> key may be used to reorder or correct the aperture
  identifications and beam numbers.  This is useful if the aperture
  numbers become disordered due to deletions and additions or if the
  first spectrum is missing when using the automatic identification
  algorithm.  An aperture number is requested for the aperture pointed to
  by the cursor.  The remaining apertures are reordered relative to this
  aperture number.  There is a aperture number, beam number, and title
  assignment algorithm which uses information about the maximum
  separation between consecutive apertures, the direction of increasing
  aperture numbers, and an optional aperture identification table.  See
  <b>apfind</b> for a description of the algorithm.
  </p>
  <p>
  After defining a new aperture it becomes the current aperture.  The
  current aperture is indicated on the status line and the <span style="font-family: monospace;">'.'</span>, <span style="font-family: monospace;">'+'</span>, and
  <span style="font-family: monospace;">'-'</span> keys are used to select a new current aperture.
  </p>
  <p>
  Apertures are deleted with <span style="font-family: monospace;">'d'</span> key.  The aperture <i>nearest</i> the
  cursor is deleted.
  </p>
  <p>
  The aperture center may be changed with the <span style="font-family: monospace;">'c'</span>, <span style="font-family: monospace;">'s'</span>, and <span style="font-family: monospace;">'g'</span> keys and the
  <span style="font-family: monospace;">":center value"</span> colon command.  The <span style="font-family: monospace;">'c'</span> key applies the centering algorithm
  to the aperture <i>nearest</i> the colon.  The <span style="font-family: monospace;">'s'</span> key shifts the center
  of the <i>current</i> aperture to the position of the cursor.  The <span style="font-family: monospace;">'g'</span>
  applies the <b>aprecenter</b> algorithm.  The :center command sets the
  center of the <i>current</i> aperture to the value specified.  Except
  for the last option these commands may be applied to all apertures
  if the ALL flag is set.
  </p>
  <p>
  The aperture limits are defined relative to the aperture center.  The
  limits may be changed with the <span style="font-family: monospace;">'l'</span>, <span style="font-family: monospace;">'u'</span>, <span style="font-family: monospace;">'y'</span>, and <span style="font-family: monospace;">'z'</span> keys and with the
  <span style="font-family: monospace;">":lower value"</span> and <span style="font-family: monospace;">":upper value"</span> commands.  The <span style="font-family: monospace;">'l'</span> and <span style="font-family: monospace;">'u'</span> keys set
  the lower and upper limits of the <i>current</i> aperture at the position
  of the cursor.  The colon commands allow setting the limits explicitly.
  The <span style="font-family: monospace;">'y'</span> key defines both limits for the <i>nearest</i> aperture as
  points at which the y cursor position intercepts the data profile.
  This requires that the aperture include a spectrum profile and that
  the y cursor value lie below the peak of the profile.  The <span style="font-family: monospace;">'z'</span>
  key applies the <b>apresize</b> algorithm.  Except for the colon
  commands these commands may be applied to all apertures if the ALL
  flag is set.
  </p>
  <p>
  The key <span style="font-family: monospace;">'b'</span> modifies the background fitting parameters for the aperture
  <i>nearest</i> the cursor.  The default background parameters are
  specified by the task <b>apdefault</b>.  Note that even though
  background parameters are defined, background subtraction is not
  performed during extraction unless specified.
  When the <span style="font-family: monospace;">'b'</span> key is used the <b>icfit</b> graphical interface is entered
  showing the background regions and function fit for the current image
  line.  Note that the background regions are specified relative to
  the aperture center and follows changes in the aperture position.
  </p>
  <p>
  The two types of
  extraction which may be specified are to average all points within
  a set of background regions or fit a function to the points in
  the background regions.  In the first case only the background sample
  parameter is used.  In the latter case the other parameters are
  also used in conjunction with the <b>icfit</b> function fitting commands.
  See <b>apbackground</b> for more on the background parameters.
  </p>
  <p>
  Each aperture may have different background
  fitting parameters but newly defined apertures inherit the background
  fitting parameters of the last current aperture.  This will usually be
  satisfactory since the background regions are defined relative to the
  aperture center rather than in absolute coordinates.  If the ALL flag
  is set then all apertures will be given the same background
  parameters.
  </p>
  <p>
  The algorithms used in the tasks <b>apfind, aprecenter, apresize, aptrace</b>,
  and <b>apsum</b> are available from the editor with the keys <span style="font-family: monospace;">'f'</span>, <span style="font-family: monospace;">'g'</span>, <span style="font-family: monospace;">'z'</span>,
  <span style="font-family: monospace;">'t'</span>, and <span style="font-family: monospace;">'e'</span>
  respectively.  Excluding finding, if the ALL flag is not set then the
  nearest aperture
  to the cursor is used.  This allows selective recentering, resizing,
  tracing and extracting.
  If the ALL flag is set then all apertures are traced or extracted.
  When extracting the output, rootname and profile name are queried.
  </p>
  <p>
  Some general purpose keys window the graph <span style="font-family: monospace;">'w'</span> using the <b>gtools</b>
  commands, redraw the graph <span style="font-family: monospace;">'r'</span>, and quit <span style="font-family: monospace;">'q'</span>.
  </p>
  <p>
  The final cursor key is the <span style="font-family: monospace;">'a'</span> key.  The cursor keys which modify the
  apertures were defined as operating on either the aperture nearest the
  cursor or the current aperture.  The <span style="font-family: monospace;">'a'</span> key allows these keys to
  affect all the apertures simultaneously.  The <span style="font-family: monospace;">'a'</span> key sets a flag which
  is shown on the status line when it is set.  When set, the operation on
  one aperture is duplicated on the remaining apertures.  The operations
  which apply to all apertures are set background <span style="font-family: monospace;">'b'</span>, center <span style="font-family: monospace;">'c'</span>, delete
  <span style="font-family: monospace;">'d'</span>, extract <span style="font-family: monospace;">'e'</span>, recenter <span style="font-family: monospace;">'g'</span>, set lower limit <span style="font-family: monospace;">'l'</span>, shift <span style="font-family: monospace;">'s'</span>, trace
  <span style="font-family: monospace;">'t'</span>, set upper limit <span style="font-family: monospace;">'u'</span>, set limits at the y cursor <span style="font-family: monospace;">'y'</span>, and resize
  <span style="font-family: monospace;">'z'</span>.  The <span style="font-family: monospace;">'b'</span>, <span style="font-family: monospace;">'l'</span>, <span style="font-family: monospace;">'s'</span>, and <span style="font-family: monospace;">'u'</span> keys first set the background,
  aperture limits, or shift for the appropriate aperture and then are
  applied to the other apertures relative to their centers.
  </p>
  <p>
  All the parameters used in any of the operations may be examined or
  changed through colon commands.  The :parameters command lists all
  parameter values and :show lists the apertures.  The :read and :write
  are used to force an update or save the current apertures and to read
  apertures for the current image or from some other image.  The commands
  all have optional arguments.  For the commands which show information
  the argument specifies a file to which the information is to be
  written.  The default is the standard output.  The database read and
  write and the change image commands take an image name.  If an image
  name is not given for the read and write commands the
  current image name is used.  The change image command default is to
  print the current image name.  The remaining commands take a value.  If
  a value is not given then the current value is printed.
  </p>
  <p>
  The aperture editor may be selected from nearly every task using the
  <b>edit</b> parameter.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  The aperture editor is a very flexible and interactive tool
  for which it is impossible illustrate all likely uses.  The following
  give some simple examples.
  </p>
  <p>
  1.  To define and edit apertures for image <span style="font-family: monospace;">"n1.001"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; apedit n1.001
  </pre></div>
  <p>
  2.  To define apertures for one image and then apply them to several other
  images:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; apedit n1.* ref=n1.001
  Edit apertures for n1.001? (yes)
  Edit apertures for n1.002? (yes) NO
  </pre></div>
  <p>
  Answer <span style="font-family: monospace;">"yes"</span> to the first query for editing n1.001.  To
  the next query (for n1.002) respond with <span style="font-family: monospace;">"NO"</span>.  The remaining
  images then will not be edited interactively.  Note that after
  defining the apertures for n1.001 they are recorded in the database
  and subsequent images will be able to use them as reference apertures.
  </p>
  <p>
  3.  Using the <span style="font-family: monospace;">":image name"</span> and <span style="font-family: monospace;">":read image"</span> colon commands and the
  <span style="font-family: monospace;">'f'</span>, <span style="font-family: monospace;">'g'</span>, <span style="font-family: monospace;">'z'</span>, <span style="font-family: monospace;">'t'</span> and <span style="font-family: monospace;">'e'</span> keys the user can perform all the functions
  available in the package without ever leaving the editor.  The <span style="font-family: monospace;">'a'</span> key
  to set the ALL flag is very useful when dealing with many spectra in a
  single image.
  </p>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_APEDIT">
  <dt><b>APEDIT V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='APEDIT' Line='APEDIT V2.11' -->
  <dd>The <span style="font-family: monospace;">"apertures"</span> parameter can be used to select apertures for resizing,
  recentering, tracing, and extraction.  This parameter name was previously
  used for selecting apertures in the recentering algorithm.  The new
  parameter name for this is now <span style="font-family: monospace;">"aprecenter"</span>.
  The aperture ID table information may now be contained in the
  image header under the keywords SLFIBnnn.
  </dd>
  </dl>
  <p>
  SEE ALSO
  </p>
  <div class="highlight-default-notranslate"><pre>
  apdefault, apfind, aprecenter, apresize, aptrace, apsum, apall
  center1d, cursor, gtools, icfit
  </pre></div>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'ADDITIONAL PARAMETERS' 'CURSOR KEYS' 'COLON COMMANDS' 'DESCRIPTION' 'EXAMPLES' 'REVISIONS'  -->
  

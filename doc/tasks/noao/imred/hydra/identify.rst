.. _identify:

identify: Identify features in spectrum for dispersion solution
===============================================================

**Package: hydra**

.. raw:: html

  <section id="s_summary">
  <h3>Summary</h3>
  <p>
  Features are interactively marked in one dimensional image vectors.
  The features may be spectral lines when the vector is a spectrum
  or profile positions when the vector is a spatial cut.  A function
  may be fit to the user coordinates as a function of pixel coordinates.
  This is primarily used to find dispersion functions for spectra
  such as arc-line calibration spectra.  The profile position measurements
  are generally used for geometric calibrations.
  </p>
  </section>
  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  identify images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of images in which to identify features and fit coordinate functions.
  </dd>
  </dl>
  <dl id="l_section">
  <dt><b>section = <span style="font-family: monospace;">"middle line"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='section' Line='section = "middle line"' -->
  <dd>If an image is not one dimensional or specified as a one dimensional image
  section then the image section given by this parameter is used.  The
  section defines a one dimensional vector.  The image is still considered to
  be two or three dimensional.  It is possible to change the data vector
  within the program.
  The section parameter may be specified directly as an image section or
  in one of the following forms
  <div class="highlight-default-notranslate"><pre>
  line|column|x|y|z first|middle|last|# [first|middle|last|#]]
  first|middle|last|# [first|middle|last|#] line|column|x|y|z
  </pre></div>
  where each field can be one of the strings separated by | except for #
  which is an integer number.  The field in [] is a second designator
  which is used with three dimensional data.  See the example section for
  examples of this syntax.  Abbreviations are allowed though beware that <span style="font-family: monospace;">'l'</span>
  is not a sufficient abbreviation.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"database"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "database"' -->
  <dd>Database in which the feature data and coordinate functions are recorded.
  </dd>
  </dl>
  <dl id="l_coordlist">
  <dt><b>coordlist = <span style="font-family: monospace;">"linelists$idhenear.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coordlist' Line='coordlist = "linelists$idhenear.dat"' -->
  <dd>User coordinate list consisting of an list of line coordinates.  A
  comment line of the form <span style="font-family: monospace;">"# units &lt;units&gt;"</span>, where &lt;units&gt; is one of the
  understood units names, defines the units of the line list.  If no units
  are specified then Angstroms are assumed.  Some standard line lists are
  available in the directory <span style="font-family: monospace;">"linelists$"</span>.  The standard line lists are
  described under the topic <i>linelists</i>.
  </dd>
  </dl>
  <dl id="l_units">
  <dt><b>units = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='units' Line='units = ""' -->
  <dd>The units to use if no database entry exists.  The units are specified as
  described in
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help onedspec.package section=units
  </pre></div>
  If no units are specified and a coordinate list is used then the units of
  the coordinate list are selected.  If a database entry exists then the
  units defined there override both this parameter and the coordinate list.
  </dd>
  </dl>
  <dl id="l_nsum">
  <dt><b>nsum = <span style="font-family: monospace;">"10"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nsum' Line='nsum = "10"' -->
  <dd>Number of lines, columns, or bands across the designated vector axis to be
  summed when the image is a two or three dimensional spatial spectrum.
  It does not apply to multispec format spectra.  If the image is three
  dimensional an optional second number can be specified for the higher
  dimensional axis  (the first number applies to the lower axis number and
  the second to the higher axis number).  If a second number is not specified
  the first number is used for both axes.
  </dd>
  </dl>
  <dl id="l_match">
  <dt><b>match = -3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='match' Line='match = -3.' -->
  <dd>The maximum difference for a match between the feature coordinate function
  value and a coordinate in the coordinate list.  Positive values
  are in user coordinate units and negative values are in units of pixels.
  </dd>
  </dl>
  <dl id="l_maxfeatures">
  <dt><b>maxfeatures = 50</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxfeatures' Line='maxfeatures = 50' -->
  <dd>Maximum number of the strongest features to be selected automatically from
  the coordinate list (function <span style="font-family: monospace;">'l'</span>) or from the image data (function <span style="font-family: monospace;">'y'</span>).
  </dd>
  </dl>
  <dl id="l_zwidth">
  <dt><b>zwidth = 100.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zwidth' Line='zwidth = 100.' -->
  <dd>Width of graphs, in user coordinates, when in zoom mode (function <span style="font-family: monospace;">'z'</span>).
  </dd>
  </dl>
  <p>
  The following parameters are used in determining feature positions.
  </p>
  <dl id="l_ftype">
  <dt><b>ftype = <span style="font-family: monospace;">"emission"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='ftype' Line='ftype = "emission"' -->
  <dd>Type of features to be identified.  The possibly abbreviated choices are
  <span style="font-family: monospace;">"emission"</span> and <span style="font-family: monospace;">"absorption"</span>.
  </dd>
  </dl>
  <dl id="l_fwidth">
  <dt><b>fwidth = 4.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fwidth' Line='fwidth = 4.' -->
  <dd>Full-width at the base (in pixels) of features to be identified.
  </dd>
  </dl>
  <dl id="l_cradius">
  <dt><b>cradius = 5.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cradius' Line='cradius = 5.' -->
  <dd>The maximum distance, in pixels, allowed between a feature position
  and the initial estimate when defining a new feature.
  </dd>
  </dl>
  <dl id="l_threshold">
  <dt><b>threshold = 0.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 0.' -->
  <dd>In order for a feature center to be determined the range of pixel intensities
  around the feature must exceed this threshold.
  </dd>
  </dl>
  <dl id="l_minsep">
  <dt><b>minsep = 2.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='minsep' Line='minsep = 2.' -->
  <dd>The minimum separation, in pixels, allowed between feature positions
  when defining a new feature.
  </dd>
  </dl>
  <p>
  The following parameters are used to fit a function to the user coordinates.
  The <b>icfit</b> package is used and further descriptions about these parameters
  may be found under that package.
  </p>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"spline3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "spline3"' -->
  <dd>The function to be fit to the user coordinates as a function of the pixel
  coordinate.  The choices are <span style="font-family: monospace;">"chebyshev"</span>, <span style="font-family: monospace;">"legendre"</span>, <span style="font-family: monospace;">"spline1"</span>, or <span style="font-family: monospace;">"spline3"</span>.
  </dd>
  </dl>
  <dl id="l_order">
  <dt><b>order = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='order' Line='order = 1' -->
  <dd>Order of the fitting function.  The order is the number of polynomial terms
  or number of spline pieces.
  </dd>
  </dl>
  <dl id="l_sample">
  <dt><b>sample = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='sample' Line='sample = "*"' -->
  <dd>Sample regions for fitting. This is in pixel coordinates and not the user
  coordinates.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 0' -->
  <dd>Number of rejection iterations.
  </dd>
  </dl>
  <dl id="l_low_reject">
  <dt><b>low_reject = 3.0, high_reject = 3.0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='low_reject' Line='low_reject = 3.0, high_reject = 3.0' -->
  <dd>Lower and upper residual rejection in terms of the RMS of the fit.
  </dd>
  </dl>
  <dl id="l_grow">
  <dt><b>grow = 0</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='grow' Line='grow = 0' -->
  <dd>Distance from a rejected point in which additional points are automatically
  rejected regardless of their residuals.
  </dd>
  </dl>
  <p>
  The following parameters control the input and output.
  </p>
  <dl id="l_autowrite">
  <dt><b>autowrite = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='autowrite' Line='autowrite = no' -->
  <dd>Automatically write or update the database?  If <span style="font-family: monospace;">"no"</span> then when exiting the
  program a query is given if the feature data and fit have been modified.
  The query is answered with <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"no"</span> to save or not save the results.
  If <i>autowrite</i> is <span style="font-family: monospace;">"yes"</span> exiting the program automatically updates the
  database.
  </dd>
  </dl>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Graphics device.  The default is the standard graphics device which is
  generally a graphics terminal.
  </dd>
  </dl>
  <dl id="l_cursor">
  <dt><b>cursor = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cursor' Line='cursor = ""' -->
  <dd>Cursor input file.  If a cursor file is not given then the standard graphics
  cursor is read.
  </dd>
  </dl>
  <p>
  The following parameters are queried when the <span style="font-family: monospace;">'b'</span> key is used.
  </p>
  <dl id="l_crval">
  <dt><b>crval, cdelt</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='crval' Line='crval, cdelt' -->
  <dd>These parameters specify an approximate coordinate value and coordinate
  interval per pixel when the automatic line identification
  algorithm (<span style="font-family: monospace;">'b'</span> key) is used.  The coordinate value is for the
  pixel specified by the <i>crpix</i> parameter in the <b>aidpars</b>
  parameter set.  The default value of <i>crpix</i> is INDEF which then
  refers the coordinate value to the middle of the spectrum.  By default
  only the magnitude of the coordinate interval is used.  Either value
  may be given as INDEF.  In this case the search for a solution will
  be slower and more likely to fail.  The values may also be given as
  keywords in the image header whose values are to be used.
  </dd>
  </dl>
  <dl id="l_aidpars">
  <dt><b>aidpars = <span style="font-family: monospace;">""</span> (parameter set)</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='aidpars' Line='aidpars = "" (parameter set)' -->
  <dd>This parameter points to a parameter set for the automatic line
  identification algorithm.  See <i>aidpars</i> for further information.
  </dd>
  </dl>
  </section>
  <section id="s_cursor_keys">
  <h3>Cursor keys</h3>
  <dl>
  <dt><b>?</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line='?' -->
  <dd>Clear the screen and print a menu of options.
  </dd>
  </dl>
  <dl id="l_a">
  <dt><b>a</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='a' Line='a' -->
  <dd>Apply next (c)enter or (d)elete operation to (a)ll features
  </dd>
  </dl>
  <dl id="l_b">
  <dt><b>b</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='b' Line='b' -->
  <dd>Identify features and find a dispersion function automatically using
  the coordinate line list and approximate values for the dispersion.
  </dd>
  </dl>
  <dl id="l_c">
  <dt><b>c</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='c' Line='c' -->
  <dd>(C)enter the feature nearest the cursor.  Used when changing the position
  finding parameters or when features are defined from a previous feature list.
  </dd>
  </dl>
  <dl id="l_d">
  <dt><b>d</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='d' Line='d' -->
  <dd>(D)elete the feature nearest the cursor.  (D)elete all features when preceded
  by the (a)ll key.  This does not affect the dispersion function.
  </dd>
  </dl>
  <dl id="l_e">
  <dt><b>e</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='e' Line='e' -->
  <dd>Find features from a coordinate list without doing any fitting.  This is
  like the <span style="font-family: monospace;">'l'</span> key without any fitting.
  </dd>
  </dl>
  <dl id="l_f">
  <dt><b>f</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='f' Line='f' -->
  <dd>(F)it a function of the pixel coordinates to the user coordinates.  This enters
  the interactive function fitting package.
  </dd>
  </dl>
  <dl id="l_g">
  <dt><b>g</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='g' Line='g' -->
  <dd>Fit a zero point shift to the user coordinates by minimizing the difference
  between the user and fitted coordinates.  The coordinate function is
  not changed.
  </dd>
  </dl>
  <dl id="l_i">
  <dt><b>i</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='i' Line='i' -->
  <dd>(I)nitialize (delete features and coordinate fit).
  </dd>
  </dl>
  <dl id="l_j">
  <dt><b>j</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='j' Line='j' -->
  <dd>Go to the preceding line, column, or band in a 2D/3D or multispec image.
  </dd>
  </dl>
  <dl id="l_k">
  <dt><b>k</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='k' Line='k' -->
  <dd>Go to the next line, column, or band in a 2D/3D or multispec image.
  </dd>
  </dl>
  <dl id="l_l">
  <dt><b>l</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='l' Line='l' -->
  <dd>(L)ocate features in the coordinate list.  A coordinate function must be
  defined or at least two features must have user coordinates from which a
  coordinate function can be determined.  If there are features an
  initial fit is done, then features are added from the coordinate list,
  and then a final fit is done.
  </dd>
  </dl>
  <dl id="l_m">
  <dt><b>m</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='m' Line='m' -->
  <dd>(M)ark a new feature using the cursor position as the initial position
  estimate.
  </dd>
  </dl>
  <dl id="l_n">
  <dt><b>n</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='n' Line='n' -->
  <dd>Move the cursor or zoom window to the (n)ext feature (same as +).
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='o' Line='o' -->
  <dd>Go to the specified line, column, or band in a 2D/3D or multispec image.
  For 3D images two numbers are specified.
  </dd>
  </dl>
  <dl id="l_p">
  <dt><b>p</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='p' Line='p' -->
  <dd>(P)an to the original window after (z)ooming on a feature.
  </dd>
  </dl>
  <dl id="l_q">
  <dt><b>q</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='q' Line='q' -->
  <dd>(Q)uit and continue with next image.
  </dd>
  </dl>
  <dl id="l_r">
  <dt><b>r</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='r' Line='r' -->
  <dd>(R)edraw the graph.
  </dd>
  </dl>
  <dl id="l_s">
  <dt><b>s</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='s' Line='s' -->
  <dd>(S)hift the fit coordinates relative to the pixel coordinates.  The
  user specifies the desired fit coordinate at the position of the cursor
  and a zero point shift to the fit coordinates is applied.  If features
  are defined then they are recentered and the shift is the average shift.
  The shift in pixels, user coordinates, and z (fractional shift) is printed.
  </dd>
  </dl>
  <dl id="l_t">
  <dt><b>t</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='t' Line='t' -->
  <dd>Reset the current feature to the position of the cursor.  The feature
  is <i>not</i> recentered.  This is used to mark an arbitrary position.
  </dd>
  </dl>
  <dl id="l_u">
  <dt><b>u</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='u' Line='u' -->
  <dd>Enter a new (u)ser coordinate for the current feature.
  When (m)arking a new feature the user coordinate is also requested.
  </dd>
  </dl>
  <dl id="l_v">
  <dt><b>v</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='v' Line='v' -->
  <dd>Modify the fitting weight of the current feature.  The weights are
  integers with the lowest weight being the default of 1.
  </dd>
  </dl>
  <dl id="l_w">
  <dt><b>w</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='w' Line='w' -->
  <dd>(W)indow the graph.  A window prompt is given and a number of windowing
  options may be given.  For more help type <span style="font-family: monospace;">'?'</span> to the window prompt or
  see help under <i>gtools</i>.
  </dd>
  </dl>
  <dl id="l_x">
  <dt><b>x</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='x' Line='x' -->
  <dd>Find a zero point shift for the current dispersion function.  This is used
  by starting with the dispersion solution and features from a different
  spectrum.  The mean shift in user coordinates, mean shift in pixels, and
  the fractional shift in user coordinates is printed.
  </dd>
  </dl>
  <dl id="l_y">
  <dt><b>y</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='y' Line='y' -->
  <dd>Up to <i>maxfeatures</i> emission peaks are found automatically (in order of
  peak intensity) and, if a dispersion solution is defined, the peaks are
  identified from the coordinate list.
  </dd>
  </dl>
  <dl id="l_z">
  <dt><b>z</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='z' Line='z' -->
  <dd>(Z)oom on the feature nearest the cursor.  The width of the zoom window
  is determined by the parameter <i>zwidth</i>.
  </dd>
  </dl>
  <dl>
  <dt><b>.</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line='.' -->
  <dd>Move the cursor or zoom window to the feature nearest the cursor.
  </dd>
  </dl>
  <dl>
  <dt><b>+</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line='+' -->
  <dd>Move the cursor or zoom window to the (n)ext feature.
  </dd>
  </dl>
  <dl>
  <dt><b>-</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line='-' -->
  <dd>Move the cursor or zoom window to the previous feature.
  </dd>
  </dl>
  <p>
  Parameters are shown or set with the following <span style="font-family: monospace;">"colon commands"</span>, which may be
  abbreviated.  To show the value of a parameter type the parameter name alone
  and to set a new value follow the parameter name by the value.
  </p>
  <dl>
  <dt><b>:show file</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':show file' -->
  <dd>Show the values of all the parameters.  If a file name is given then the
  output is appended to that file.  If no file is given then the terminal
  is cleared and the output is sent to the terminal.
  </dd>
  </dl>
  <dl>
  <dt><b>:features file</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':features file' -->
  <dd>Print the feature list and the fit rms.  If a file name is given then the
  output is appended to that file.  If no file is given then the terminal
  is cleared and the output is sent to the terminal.
  </dd>
  </dl>
  <dl>
  <dt><b>:coordlist file</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':coordlist file' -->
  <dd>Set or show the coordinate list file.
  </dd>
  </dl>
  <dl>
  <dt><b>:cradius value</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':cradius value' -->
  <dd>Set or show the centering radius in pixels.
  </dd>
  </dl>
  <dl>
  <dt><b>:threshold value</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':threshold value' -->
  <dd>Set or show the detection threshold for centering.
  </dd>
  </dl>
  <dl>
  <dt><b>:database name</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':database name' -->
  <dd>Set or show the database for recording feature records.
  </dd>
  </dl>
  <dl>
  <dt><b>:ftype value</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':ftype value' -->
  <dd>Set or show the feature type (emission or absorption).
  </dd>
  </dl>
  <dl>
  <dt><b>:fwidth value</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':fwidth value' -->
  <dd>Set or show the feature width in pixels.
  </dd>
  </dl>
  <dl>
  <dt><b>:image imagename</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':image imagename' -->
  <dd>Set a new image or show the current image.
  </dd>
  </dl>
  <dl>
  <dt><b>:labels value</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':labels value' -->
  <dd>Set or show the feature label type (none, index, pixel, coord, user, or both).
  None produces no labeling, index labels the features sequentially in order
  of pixel position, pixel labels the features by their pixel coordinates,
  coord labels the features by their user coordinates (such as wavelength),
  user labels the features by the user or line list supplied string, and
  both labels the features by both the user coordinates and user strings.
  </dd>
  </dl>
  <dl>
  <dt><b>:match value</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':match value' -->
  <dd>Set or show the coordinate list matching distance.
  </dd>
  </dl>
  <dl>
  <dt><b>:maxfeatures value</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':maxfeatures value' -->
  <dd>Set or show the maximum number of features automatically found.
  </dd>
  </dl>
  <dl>
  <dt><b>:minsep value</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':minsep value' -->
  <dd>Set or show the minimum separation allowed between features.
  </dd>
  </dl>
  <dl>
  <dt><b>:read name ap</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':read name ap' -->
  <dd>Read a record from the database.  The record name defaults to the image name
  and, for 1D spectra, the aperture number defaults to aperture of
  the current image.
  </dd>
  </dl>
  <dl>
  <dt><b>:write name ap</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':write name ap' -->
  <dd>Write a record to the database.  The record name defaults to the image name
  and, for 1D spectra, the aperture number defaults to aperture of
  the current image.
  </dd>
  </dl>
  <dl>
  <dt><b>:add name ap</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':add name ap' -->
  <dd>Add features from a database record.  The record name defaults to the image name
  and, for 1D spectra, the aperture number defaults to aperture of
  the current image.  Only the features are added to any existing list
  of features.  The dispersion function is not read.
  </dd>
  </dl>
  <dl>
  <dt><b>:zwidth value</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':zwidth value' -->
  <dd>Set or show the zoom width in user units.
  </dd>
  </dl>
  <dl>
  <dt><b>:/help</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':/help' -->
  <dd>Print additional help for formatting graphs.  See help under <span style="font-family: monospace;">"gtools"</span>.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Features in the input images are identified interactively and assigned
  user coordinates.  A <span style="font-family: monospace;">"coordinate function"</span> mapping pixel coordinates to
  user coordinates may be determined from the identified features.  A
  user coordinate list may be defined to automatically identify additional
  features.  This task is used to measure positions of features,
  determine dispersion solutions for spectra, and to identify features in
  two and three dimensional images for mapping a two or three dimensional
  coordinate transformation.  Because of this dual use the terms vector
  and feature are used rather than spectrum and spectral line.
  </p>
  <p>
  Each image in the input list is considered in turn.  If the image is
  not one dimensional or a one dimensional section of an image
  then the image section given by the parameter
  <i>section</i> is used.  This parameter may be specified in several ways as
  described in the PARAMETERS and EXAMPLES sections.  The image section is used
  to select a starting vector and image axis.
  </p>
  <p>
  If the image is not one dimensional or in multispec format then the number
  of lines, columns, or bands given by the parameter <i>nsum</i> are summed.
  The one dimensional image vector is graphed.  The initial feature list and
  coordinate function are read from the database if an entry exists.  The
  features are marked on the graph.  The image coordinates are in pixels
  unless a coordinate function is defined, in which case they are in user
  coordinate units.  The pixel coordinate, coordinate function value, and
  user coordinate for the current feature are printed.
  </p>
  <p>
  The graphics cursor is used to select features and perform various
  functions.  A menu of the keystroke options and functions is printed
  with the key <span style="font-family: monospace;">'?'</span>.  The cursor keys and their functions are defined in
  the CURSOR KEYS section and described further below.  The standard
  cursor mode keys are also available to window and redraw the graph and
  to produce hardcopy <span style="font-family: monospace;">"snaps"</span>.
  </p>
  <p>
  There are a number of ways of defining features.  They fall into
  two categories; interactively defining features with the cursor
  and using automatic algorithms.
  </p>
  <p>
  The <span style="font-family: monospace;">'m'</span> key is the principle interactive feature marking method.  Typing
  <span style="font-family: monospace;">'m'</span> near the position of a feature applies a feature centering algorithm
  (see <b>center1d</b>) and, if a center is found, the feature is entered in
  the feature list and marked on the spectrum.  If the new position is within
  a distance given by the parameter <i>minsep</i> of a previous feature it is
  considered to be the same feature and replaces the old feature.  Normally
  the position of a new feature will be exactly the same as the original
  feature.  The coordinate list is searched for a match between the
  coordinate function value (when defined) and a user coordinate in the
  list.  If a match is found it becomes the default user coordinate which the
  user may override.  The new feature is marked on the graph and it becomes
  the current feature.  The redefinition of a feature which is within the
  minimum separation may be used to set the user coordinate from the
  coordinate list.  The <span style="font-family: monospace;">'t'</span> key allows setting the position of a feature to
  other than that found by the centering algorithm.
  </p>
  <p>
  The principle automatic feature identification algorithm is executed
  with the <span style="font-family: monospace;">'b'</span> key.  The user is queried for an approximate coordinate
  value and coordinate interval per pixel.  The coordinate value
  is for the center of the spectrum by default though this may be changed
  with the <b>aidpars</b> parameters.  Only the magnitude of the
  coordinate interval per pixel is used by default though this also
  may be changed.  Either value may be given as INDEF to do an unconstrained
  search, however, this will be much slower and more likely to fail.
  The algorithm searches for matches between the strong lines in the
  spectrum and lines in the coordinate list.  The algorithm is described
  in the documentation for <b>aidpars</b>.
  </p>
  <p>
  The <span style="font-family: monospace;">'b'</span> key works with no predefined dispersion solution or features.  If
  two or more features are identified, with <span style="font-family: monospace;">'m'</span>, spanning the range of the
  data or if a coordinate function is defined, from a previous solution, then
  the <span style="font-family: monospace;">'e'</span>, <span style="font-family: monospace;">'l'</span>, and <span style="font-family: monospace;">'y'</span> keys may be used to identify additional features from
  a coordinate list.  The <span style="font-family: monospace;">'e'</span> key only adds features at the coordinates of
  the line lists if the centering algorithm finds a feature at that
  wavelength (as described below).  The <span style="font-family: monospace;">'y'</span> key works in reverse by finding
  the prominent features using a peak finding algorithm and then looking in
  the coordinate list for entries near the estimated position.  Up to a
  maximum number of features (<i>maxfeatures</i>) will be selected.  If there
  are more peaks only the strongest are kept.  In either of these cases there
  is no automatic fitting and refitting of the dispersion function.
  </p>
  <p>
  The <span style="font-family: monospace;">'l'</span> key combines automatic fits with locating lines from the coordinate
  list.  If two or more features are defined an initial fit is made.  Then
  for each coordinate value in the coordinate list the pixel coordinate is
  determined and a search for a feature at that point is made.  If a feature
  is found (based on the parameters <i>ftype, fwidth</i>, <i>cradius</i>, and
  <b>threshold</b>) its user coordinate value based on the coordinate function
  is determined.  If the coordinate function value matches the user
  coordinate from the coordinate list within the error limit set by the
  parameter <i>match</i> then the new feature is entered in the feature list.
  Up to a maximum number of features, set by the parameter <i>maxfeatures</i>,
  may be defined in this way.  A new user coordinate function is fit to all
  the located features.  Finally, the graph is redrawn in user coordinates
  with the additional features found from the coordinate list marked.
  </p>
  <p>
  A minimum of two features must be defined for the <span style="font-family: monospace;">'l'</span> key algorithm to
  work.  However, three or more features are preferable to determine changes
  in the dispersion as a function of position.
  </p>
  <p>
  The <span style="font-family: monospace;">'f'</span> key fits a function of the pixel coordinates to the user
  coordinates.  The type of function, order and other fitting parameters
  are initially set with the parameters <i>function, order, sample,
  niterate, low_reject, high_reject</i> and <i>grow</i>..  The value of the
  function for a particular pixel coordinate is called the function
  coordinate and each feature in the feature list has a function
  coordinate value.  The fitted function also is used to convert pixel
  coordinates to user coordinates in the graph.  The fitting is done
  within the interactive curve fitting package which has its own set of
  interactive commands.  For further information on this package see the
  help material under <b>icfit</b>.
  </p>
  <p>
  If a zero point shift is desired without changing the coordinate function
  the user may specify the coordinate of a point in the spectrum with
  the <span style="font-family: monospace;">'s'</span> key from which a shift is determined.  The <span style="font-family: monospace;">'g'</span> key also
  determines a shift by minimizing the difference between the user
  coordinates and the fitted coordinates.  This is used when a previously
  determined coordinate function is applied to a new spectrum having
  fewer or poorer lines and only a zero point shift can reasonably be
  determined.  Note that the zero point shift is in user coordinates.
  This is only an approximate correction for shifts in the raw spectra
  since these shifts are in pixels and the coordinate function should
  also be appropriately shifted.
  </p>
  <p>
  One a set of features is defined one may select features for various
  operations.  To select feature as the current feature the keys <span style="font-family: monospace;">'.'</span>, <span style="font-family: monospace;">'n'</span>,
  <span style="font-family: monospace;">'+'</span>, and <span style="font-family: monospace;">'-'</span> are used.  The <span style="font-family: monospace;">'.'</span> selects the feature nearest the cursor, the
  <span style="font-family: monospace;">'n'</span> and <span style="font-family: monospace;">'+'</span> select the next feature, and the <span style="font-family: monospace;">'-'</span> selects the previous
  feature relative to the current feature in the feature list as ordered by
  pixel coordinate.  These keys are useful when redefining the user
  coordinate with the <span style="font-family: monospace;">'u'</span> key, changing the fitting weight of a feature with
  <span style="font-family: monospace;">'v'</span>, and when examining features in zoom mode.
  </p>
  <p>
  Features may be deleted with the key <span style="font-family: monospace;">'d'</span>.  All features are deleted
  when the <span style="font-family: monospace;">'a'</span> key immediately precedes the delete key.  Deleting the
  features does not delete the coordinate function.  Features deleted in the
  curve fitting package also are removed from the feature list upon
  exiting the curve fitting package.
  </p>
  <p>
  It is common to transfer the feature identifications and coordinate function
  from one image to another.  When a new image without a database entry
  is examined, such as when going to the next image in the input list,
  changing image lines or columns with <span style="font-family: monospace;">'j'</span>, <span style="font-family: monospace;">'k'</span> and <span style="font-family: monospace;">'o'</span>, or selecting
  a new image with the <span style="font-family: monospace;">":image"</span> command, the current feature list and coordinate
  function are kept.  Alternatively, a database record from a different
  image may be read with the <span style="font-family: monospace;">":read"</span> command.  When transferring feature
  identifications between images the feature coordinates will not agree exactly
  with the new image feature positions and several options are available to
  reregister the feature positions.  The key <span style="font-family: monospace;">'c'</span> centers the feature nearest
  the cursor using the current position as the starting point.  When preceded
  with the <span style="font-family: monospace;">'a'</span> key all the features are recentered (the user must refit
  the coordinate function if desired).  As an aside, the recentering
  function is also useful when the parameters governing the feature
  centering algorithm are changed.  An additional options is the <span style="font-family: monospace;">":add"</span>
  command to add features from a database record.  This does not overwrite
  previous features (or the fitting functions) as does <span style="font-family: monospace;">":read"</span>.
  </p>
  <p>
  The (c)entering function is applicable when the shift between the current
  and true feature positions is small.  Larger shifts may be determined
  automatically with the <span style="font-family: monospace;">'s'</span> or <span style="font-family: monospace;">'x'</span> keys.
  </p>
  <p>
  A zero point shift is specified interactively with the <span style="font-family: monospace;">'s'</span> key by using the
  cursor to indicate the coordinate of a point in the spectrum.  If there are
  no features then the shift is exactly as marked by the cursor.  If there
  are features the specified shift is applied, the features are recentered,
  and the mean shift for all the features is determined.
  </p>
  <p>
  The <span style="font-family: monospace;">'x'</span> key uses the automatic line identification algorithm (see
  <b>aidpars</b>) with the constraint that the dispersion is nearly the
  same and the is primarily a shift in the coordinate zero point.  If
  features are defined, normally by inheritance from another spectrum, then a
  first pass is done to identify those features in the spectrum.  Since this
  only works when the shifts are significantly less than the dispersion range
  of the spectrum (i.e. a significant number of features are in common) a
  second pass using the full coordinate line list is performed if a shift
  based on the features is not found.  After a shift is found any features
  remaining from the original list are recentered and a mean shift is
  computed.
  </p>
  <p>
  In addition to the single keystroke commands there are commands initiated
  by the key <span style="font-family: monospace;">':'</span> (colon commands).  As with the keystroke commands there are
  a number of standard graphics features available beginning with <span style="font-family: monospace;">":."</span>
  (type <span style="font-family: monospace;">":.help"</span> for these commands).  The identify colon commands
  allow the task parameter values to be listed and to be reset
  within the task.  A parameter is listed by typing its name.  The colon command
  <span style="font-family: monospace;">":show"</span> lists all the parameters.  A parameter value is reset by
  typing the parameter name followed by the new value; for example
  <span style="font-family: monospace;">":match 10"</span>.  Other colon commands display the feature list (:features),
  control reading and writing records to the database (:read and :write),
  and set the graph display format.
  </p>
  <p>
  The feature identification process for an image is completed by typing
  <span style="font-family: monospace;">'q'</span> to quit.  Attempting to quit an image without explicitly
  recording changes in the feature database produces a warning message
  unless the <i>autowrite</i> parameter is set.  If this parameter is
  not set a prompt is given asking whether to save the results otherwise
  the results are automatically saved.  Also
  the reference spectrum keyword REFSPEC is added to the image header at
  this time.  This is used by <b>refspectra</b> and <b>dispcor</b>.
  As an immediate exit the <span style="font-family: monospace;">'I'</span> interrupt key may be used.  This does not save
  the feature information and may leave the graphics in a confused state.
  </p>
  </section>
  <section id="s_database_records">
  <h3>Database records</h3>
  <p>
  The database specified by the parameter <i>database</i> is a directory of
  simple text files.  The text files have names beginning with 'id' followed
  by the entry name, usually the name of the image.  The database text files
  consist of a number of records.  A record begins with a line starting with the
  keyword <span style="font-family: monospace;">"begin"</span>.  The rest of the line is the record identifier.  Records
  read and written by <b>identify</b> have <span style="font-family: monospace;">"identify"</span> as the first word of the
  identifier.  Following this is a name which may be specified following the
  <span style="font-family: monospace;">":read"</span> or <span style="font-family: monospace;">":write"</span> commands.  If no name is specified then the image name
  is used.  For 1D spectra the database entry includes the aperture number
  and so to read a solution from a aperture different than the current image
  and aperture number must be specified.  For 2D/3D images the entry name
  has the 1D image section which is what is specified to read the entry.
  The lines following the record identifier contain
  the feature information and dispersion function coefficients.
  </p>
  <p>
  The dispersion function is saved in the database as a series of
  coefficients.  The section containing the coefficients starts with the
  keyword <span style="font-family: monospace;">"coefficients"</span> and the number of coefficients.
  </p>
  <p>
  The first four coefficients define the type of function, the order
  or number of spline pieces, and the range of the independent variable
  (the line or column coordinate along the dispersion).  The first
  coefficient is the function type code with values:
  </p>
  <div class="highlight-default-notranslate"><pre>
  Code    Type
     1    Chebyshev polynomial
     2    Legendre polynomial
     3    Cubic spline
     4    Linear spline
  </pre></div>
  <p>
  The second coefficient is the order (actually the number of terms) of
  the polynomial or the number of pieces in the spline.
  </p>
  <p>
  The next two coefficients are the range of the independent variable over
  which the function is defined.  These values are used to normalize the
  input variable to the range -1 to 1 in the polynomial functions.  If the
  independent variable is x and the normalized variable is n, then
  </p>
  <div class="highlight-default-notranslate"><pre>
  n = (2 * x - (xmax + xmin)) / (xmax - xmin)
  </pre></div>
  <p>
  where xmin and xmax are the two coefficients.
  </p>
  <p>
  The spline functions divide the range into the specified number of
  pieces.  A spline coordinate s and the nearest integer below s,
  denoted as j, are defined by
  </p>
  <div class="highlight-default-notranslate"><pre>
  s = (x - xmin) / (xmax - xmin) * npieces
  j = integer part of s
  </pre></div>
  <p>
  where npieces are the number of pieces.
  </p>
  <p>
  The remaining coefficients are those for the appropriate function.
  The number of coefficients is either the same as the function order
  for the polynomials, npieces+1 for the linear spline, or npieces + 3
  for the cubic spline.
  </p>
  <p>
  1. Chebyshev Polynomial
  </p>
  <p>
  The polynomial can be expressed as the sum
  </p>
  <div class="highlight-default-notranslate"><pre>
  y = sum from i=1 to order {c_i * z_i}
  </pre></div>
  <p>
  where the c_i are the coefficients and the z_i are defined
  interactively as:
  </p>
  <div class="highlight-default-notranslate"><pre>
  z_1 = 1
  z_2 = n
  z_i = 2 * n * z_{i-1} - z_{i-2}
  </pre></div>
  <p>
  2. Legendre Polynomial
  </p>
  <p>
  The polynomial can be expressed as the sum
  </p>
  <div class="highlight-default-notranslate"><pre>
  y = sum from i=1 to order {c_i * z_i}
  </pre></div>
  <p>
  where the c_i are the coefficients and the z_i are defined
  interactively as:
  </p>
  <div class="highlight-default-notranslate"><pre>
  z_1 = 1
  z_2 = n
  z_i = ((2*i-3) * n * z_{i-1} - (i-2) * z_{i-2}) / (i-1)
  </pre></div>
  <p>
  3. Linear Spline
  </p>
  <p>
  The linear spline is evaluated as
  </p>
  <div class="highlight-default-notranslate"><pre>
  y = c_j * a + c_{j+1} * b
  </pre></div>
  <p>
  where j is as defined earlier and a and b are fractional difference
  between s and the nearest integers above and below
  </p>
  <div class="highlight-default-notranslate"><pre>
  a = (j + 1) - s
  b = s - j
  </pre></div>
  <p>
  4.  Cubic Spline
  </p>
  <p>
  The cubic spline is evaluated as
  </p>
  <div class="highlight-default-notranslate"><pre>
  y = sum from i=0 to 3 {c_{i+j} * z_i}
  </pre></div>
  <p>
  where j is as defined earlier.  The term z_i are computed from
  a and b, as defined earlier, as follows
  </p>
  <div class="highlight-default-notranslate"><pre>
  z_0 = a**3
  z_1 = 1 + 3 * a * (1 + a * b)
  z_2 = 1 + 3 * b * (1 + a * b)
  z_3 = b**3
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Because this task is interactive and has many possible applications
  it is difficult to provide actual examples.  Instead some uses of the task
  are described.
  </p>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='o' Line='o' -->
  <dd>For defining distortions in the slit dimension as a function of
  wavelength the positions of objects are marked at some wavelength.
  The task <b>reidentify</b> is then used to trace the features to other
  wavelengths.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='o' Line='o' -->
  <dd>For determining dispersion solutions in a one dimensional
  spectrum an arc calibration is used.  Three emission features are marked
  and the (l)ocate key is used to find additional features from a
  coordinate list of arc lines.  The dispersion solution is fit interactively
  and badly determined or misidentified lines are deleted.  The
  solution may be written to the database or transferred to the object
  spectrum by reading the object image and deleting all the features.
  Deleting the features does not delete the coordinate function.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='o' Line='o' -->
  <dd>For determining a two or three dimensional coordinate transformation a
  dispersion solution is determined at one slit position in a long slit arc
  spectrum or one spatial position in a Fabry-Perot spectrum as in the
  previous example.  The features are then traced to other positions with the
  task <b>reidentify</b>.
  </dd>
  </dl>
  <p>
  2.  For images which are two or three dimensional it is necessary to
  specify the image axis for the data vector and the number of pixels at each
  point across the vector direction to sum.  One way specify a vector is to
  use an image section to define a vector.  For example, to select column
  20:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; identify obj[20,*]
  </pre></div>
  <p>
  The alternative is to use the section parameter.  Below are some examples
  of the section parameter syntax for an image <span style="font-family: monospace;">"im2d"</span> which is 100x200
  and <span style="font-family: monospace;">"im3d"</span> which is 100x200x50.  On the left is the section string syntax
  and on the right is the image section
  </p>
  <div class="highlight-default-notranslate"><pre>
  Section parameter |  Image section      |  Description
  ------------------|---------------------|---------------------
  first line        |  im2d[*,1]          |  First image line
  middle column     |  im2d[50,*]         |  Middle image column
  last z            |  im3d[100,200,*]    |  Last image z vector
  middle last y     |  im3d[50,*,50]      |  Image y vector
  line 20           |  im2d[*,20]         |  Line 20
  column 20         |  im2d[20,*]         |  Column 20
  x 20              |  im2d[*,20]         |  Line 20
  y 20              |  im2d[20,*]         |  Column 20
  y 20 30           |  im2d[20,*,30]      |  Column 20
  z 20 30           |  im3d[20,30,*]      |  Image z vector
  x middle          |  im3d[*,100,25]     |  Middle of image
  y middle          |  im3d[50,*,25]      |  Middle of image
  z middle          |  im3d[50,100,*]     |  Middle of image
  </pre></div>
  <p>
  The most common usage should be <span style="font-family: monospace;">"middle line"</span>, <span style="font-family: monospace;">"middle column"</span> or <span style="font-family: monospace;">"middle z"</span>.
  </p>
  <p>
  The summing factors apply to the axes across the specified vector.  For
  3D images there may be one or two values.  The following shows which axes
  are summed, the second and third columns, when the vector axis is that shown
  in the first column.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Vector axis       |   Sum axis in 2D    |  Sum axes in 3D
  ------------------|---------------------|--------------------
       1            |         2           |      2 3
       2            |         1           |      1 3
       3            |         -           |      1 2
  </pre></div>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_IDENTIFY">
  <dt><b>IDENTIFY V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IDENTIFY' Line='IDENTIFY V2.11' -->
  <dd>The dispersion units are now determined from a user parameter,
  the coordinate list, or the database entry.
  A new key, <span style="font-family: monospace;">'e'</span>, has been added to add features from a line list without
  doing any fits.  This is like the <span style="font-family: monospace;">'l'</span> but without the automatic
  fitting before and after adding new features.
  A new key, <span style="font-family: monospace;">'b'</span>, has been added to apply an automatic line identification
  algorithm.
  The <span style="font-family: monospace;">'x'</span> key has been changed to use the automatic line identification
  algorithm.  The allows finding much larger shifts.
  The match parameter may now be specified either in user coordinates or
  in pixels.  The default is now 3 pixels.
  The default threshold value has been changed to 0.
  </dd>
  </dl>
  <dl id="l_IDENTIFY">
  <dt><b>IDENTIFY V2.10.3</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IDENTIFY' Line='IDENTIFY V2.10.3' -->
  <dd>The section and nsum parameter syntax was extended to apply to 3D
  images.  The previous values and defaults may still be used.
  The <span style="font-family: monospace;">'v'</span> key was added to allow assigning weights to features.
  </dd>
  </dl>
  <dl id="l_IDENTIFY">
  <dt><b>IDENTIFY V2.10</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='IDENTIFY' Line='IDENTIFY V2.10' -->
  <dd>The principle revision is to allow multiple aperture images and long slit
  spectra to be treated as a unit.  New keystrokes allow jumping or scrolling
  within multiple spectra in a single image.  For aperture spectra the
  database entries are referenced by image name and aperture number and not
  with image sections.  Thus, IDENTIFY solutions are not tied to specific
  image lines in this case.  There is a new autowrite parameter which may
  be set to eliminate the save to database query upon exiting.  The new
  colon command <span style="font-family: monospace;">"add"</span> may be used to add features based on some other
  spectrum or arc type and then apply the fit to the combined set of features.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  autoidentify, reidentify, aidpars, center1d, linelists, fitcoords, icfit,
  gtools
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SUMMARY' 'USAGE' 'PARAMETERS' 'CURSOR KEYS' 'DESCRIPTION' 'DATABASE RECORDS' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

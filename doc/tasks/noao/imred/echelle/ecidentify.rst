.. _ecidentify:

ecidentify: Identify features in spectrum for dispersion solution
=================================================================

**Package: echelle**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ecidentify images
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>List of echelle format spectra in which to identify lines and fit
  dispersion functions.
  </dd>
  </dl>
  <dl id="l_database">
  <dt><b>database = <span style="font-family: monospace;">"database"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='database' Line='database = "database"' -->
  <dd>Database in which the feature data and dispersion functions are recorded.
  </dd>
  </dl>
  <dl id="l_coordlist">
  <dt><b>coordlist = <span style="font-family: monospace;">"linelists$idhenear.dat"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='coordlist' Line='coordlist = "linelists$idhenear.dat"' -->
  <dd>User coordinate list consisting of an ordered list of line coordinates.  A
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
  <dl id="l_match">
  <dt><b>match = 1.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='match' Line='match = 1.' -->
  <dd>The maximum difference for a match between the feature coordinate function
  value and a coordinate in the coordinate list.  The unit of this parameter
  is that of the user coordinates.
  </dd>
  </dl>
  <dl id="l_maxfeatures">
  <dt><b>maxfeatures = 100</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='maxfeatures' Line='maxfeatures = 100' -->
  <dd>Maximum number of the strongest features to be selected automatically from
  the coordinate list (function <span style="font-family: monospace;">'l'</span>) or from the image data (function <span style="font-family: monospace;">'y'</span>).
  </dd>
  </dl>
  <dl id="l_zwidth">
  <dt><b>zwidth = 10.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='zwidth' Line='zwidth = 10.' -->
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
  <dd>Width in pixels of features to be identified.
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
  <dt><b>threshold = 10.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='threshold' Line='threshold = 10.' -->
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
  The following default parameters are used when fitting a function to
  the user coordinates.  If a previous solution is read from the database
  then the parameters from that solution override the defaults below.
  </p>
  <dl id="l_function">
  <dt><b>function = <span style="font-family: monospace;">"chebyshev"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='function' Line='function = "chebyshev"' -->
  <dd>The function to be fit to the user coordinates as a function of the pixel
  coordinate and aperture number.  The choices are bi-dimensional
  <span style="font-family: monospace;">"chebyshev"</span> and <span style="font-family: monospace;">"legendre"</span> polynomials.
  </dd>
  </dl>
  <dl id="l_xorder">
  <dt><b>xorder = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='xorder' Line='xorder = 2' -->
  <dd>Order of the fitting function along each echelle order.
  The order is the number of polynomial terms; i.e. xorder = 2 is a linear
  function.
  </dd>
  </dl>
  <dl id="l_yorder">
  <dt><b>yorder = 2</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='yorder' Line='yorder = 2' -->
  <dd>Order of the fitting function with respect to the aperture number.
  The order is the number of polynomial terms; i.e. yorder = 2 is a linear
  function.
  </dd>
  </dl>
  <dl id="l_niterate">
  <dt><b>niterate = 0, lowreject = 3, highreject = 3.</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='niterate' Line='niterate = 0, lowreject = 3, highreject = 3.' -->
  <dd>Default number of rejection iterations and the sigma clipping thresholds.  If
  <i>niterate</i> is zero then no rejection is done.
  </dd>
  </dl>
  <p>
  The following parameters control the graphics input and output.
  </p>
  <dl id="l_graphics">
  <dt><b>graphics = <span style="font-family: monospace;">"stdgraph"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='graphics' Line='graphics = "stdgraph"' -->
  <dd>Graphics device.  The default is the standard graphics device which is
  generally a graphics terminal.
  </dd>
  </dl>
  <dl id="l_curosr">
  <dt><b>curosr = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='curosr' Line='curosr = ""' -->
  <dd>Cursor input file.  If a cursor file is not given then the standard graphics
  cursor is read.
  </dd>
  </dl>
  </section>
  <section id="s_cursor_keys">
  <h3>Cursor keys</h3>
  <div class="highlight-default-notranslate"><pre>
             ECIDENTIFY CURSOR KEY AND COLON COMMAND SUMMARY
  
  ?  Help                   a  Affect all features     c  Center feature(s)
  d  Delete feature(s)      f  Fit dispersion          g  Fit zero point shift
  i  Initialize             j  Go to previous order    k  Go to next order
  l  Match coordinate list  m  Mark feature            n  Next feature
  o  Go to specified order  p  Pan graph               q  Quit
  r  Redraw graph           s  Shift feature           t  Reset position
  u  Enter user coordinate  w  Window graph            x  Crosscorrelate peaks
  y  Find peaks             z  Zoom graph              .  Nearest feature
  +  Next feature           -  Previous feature        I  Interrupt
  
  :show [file]              :features [file]           :coordlist [file]
  :cradius [value]          :threshold [value]         :database [file]
  :ftype [type]             :fwidth [value]            :image [image]
  :labels [type]            :match [value]             :maxfeatures [value]
  :minsep [value]           :read [image]              :write [image]
  :zwidth [value]
  
         ECHELLE DISPERSION FUNCTION FITTING COMMAND SUMMARY
  
  ?  Help             c  Print coordinates             d  Delete point
  f  Fit dispersion   o  Fit with fixed order offset   q  Quit
  r  Redraw graph     u  Undelete point                w  Window graph
  x  Set ordinate     y  Set abscissa                  I  Interrupt
  
  :show               :function [value]   :highreject [value]   :lowreject [value]
  :niterate [value]   :xorder [value]     :yorder [value]
  </pre></div>
  <p>
              ECIDENTIFY CURSOR KEYS AND COLON COMMANDS
  </p>
  <dl>
  <dt><b>?</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line='?' -->
  <dd>Clear the screen and print a menu of cursor and colon commands.
  </dd>
  </dl>
  <dl id="l_a">
  <dt><b>a</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='a' Line='a' -->
  <dd>Apply next (c)enter or (d)elete operation to (a)ll features
  </dd>
  </dl>
  <dl id="l_c">
  <dt><b>c</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='c' Line='c' -->
  <dd>(C)enter the feature nearest the cursor.  Used when changing the position
  finding parameters or when features are defined from a previous feature list.
  May be used in combination with the (a)ll key.
  </dd>
  </dl>
  <dl id="l_d">
  <dt><b>d</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='d' Line='d' -->
  <dd>(D)elete the feature nearest the cursor.  (D)elete all features when preceded
  by the (a)ll key.  This does not affect the dispersion function.
  </dd>
  </dl>
  <dl id="l_f">
  <dt><b>f</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='f' Line='f' -->
  <dd>(F)it a function of the pixel coordinates and aperture numbers to the user
  coordinates.  This enters an interactive function fitting package.
  </dd>
  </dl>
  <dl id="l_g">
  <dt><b>g</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='g' Line='g' -->
  <dd>Fit a zero point shift to the user coordinates by minimizing the difference
  between the user and fitted coordinates.  The coordinate dispersion function
  is not changed.
  </dd>
  </dl>
  <dl id="l_i">
  <dt><b>i</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='i' Line='i' -->
  <dd>(I)nitialize (delete features and dispersion function fit).
  </dd>
  </dl>
  <dl id="l_j">
  <dt><b>j</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='j' Line='j' -->
  <dd>Go to the next aperture in decreasing line number in the echelle format image.
  Wrap around to the last line from the first line.
  </dd>
  </dl>
  <dl id="l_k">
  <dt><b>k</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='k' Line='k' -->
  <dd>Go to the next aperture in increasing line number in the echelle format image.
  Wrap around to the first line from the last line.
  </dd>
  </dl>
  <dl id="l_l">
  <dt><b>l</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='l' Line='l' -->
  <dd>(L)ocate features in the coordinate list.  A coordinate function must be
  defined or at least four features in more than one aperture must have user
  coordinates from which a coordinate function can be determined by an
  initial automatic function fit.
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
  <dd>Move the cursor or zoom to the (n)ext feature (same as +).
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='o' Line='o' -->
  <dd>Go to a specific aperture (related to an echelle (o)rder).  The user
  is queried for the aperture number.
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
  user specifies the desired coordinate at the position of the cursor
  and a zero point shift to the fit coordinates is applied.  If features
  are defined then they are recentered and the shift is the average shift.
  The shift in pixels, user coordinates, and z (fractional shift) is printed.
  The user shift is for the fundamental order and the shift for each order
  is then given by this shift divided by the order number.
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
  <dd>Crosscorrelate features with the data peaks and reregister.  This is
  generally used with a feature list from a different image.
  The mean shift in user coordinates, mean shift in pixels, and the fractional
  shift in user coordinates is printed.  The user shift is scaled to the
  fundamental order.
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
  This does not automatically move to the next aperture.
  </dd>
  </dl>
  <dl>
  <dt><b>-</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line='-' -->
  <dd>Move the cursor or zoom window to the previous feature.
  This does not automatically move to the next aperture.
  </dd>
  </dl>
  <dl id="l_I">
  <dt><b>I</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='I' Line='I' -->
  <dd>Interrupt the task immediately.  The database is not updated.
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
  <dd>Set or show the feature label type (none, index, pixel, or user).
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
  <dt><b>:read name</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':read name' -->
  <dd>Read a record from the database.  The record name defaults to the image name.
  </dd>
  </dl>
  <dl>
  <dt><b>:threshold value</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':threshold value' -->
  <dd>Set or show the centering threshold.
  </dd>
  </dl>
  <dl>
  <dt><b>:write name</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':write name' -->
  <dd>Write a record to the database.  The record name defaults to the image name.
  </dd>
  </dl>
  <dl>
  <dt><b>:zwidth value</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':zwidth value' -->
  <dd>Set or show the zoom width in user units.
  </dd>
  </dl>
  <p>
                DISPERSION FUNCTION FITTING COMMANDS
  </p>
  <dl>
  <dt><b>?</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line='?' -->
  <dd>Page help information.
  </dd>
  </dl>
  <dl id="l_c">
  <dt><b>c</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='c' Line='c' -->
  <dd>Print input and fitted coordinates of point nearest the cursor.
  </dd>
  </dl>
  <dl id="l_d">
  <dt><b>d</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='d' Line='d' -->
  <dd>Delete the nearest undeleted point to the cursor.
  </dd>
  </dl>
  <dl id="l_f">
  <dt><b>f</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='f' Line='f' -->
  <dd>Fit a dispersion function including determining the order offset.
  </dd>
  </dl>
  <dl id="l_o">
  <dt><b>o</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='o' Line='o' -->
  <dd>Fit a dispersion function with the order offset fixed.  The user is queried
  for the order offset.  This is faster than the interactive fit to also
  determine the order.
  </dd>
  </dl>
  <dl id="l_q">
  <dt><b>q</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='q' Line='q' -->
  <dd>Quit and return to the spectrum display.
  </dd>
  </dl>
  <dl id="l_r">
  <dt><b>r</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='r' Line='r' -->
  <dd>Redraw the graph.
  </dd>
  </dl>
  <dl id="l_u">
  <dt><b>u</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='u' Line='u' -->
  <dd>Undelete the nearest deleted point to the cursor (which may be outside the
  graph window).
  </dd>
  </dl>
  <dl id="l_w">
  <dt><b>w</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='w' Line='w' -->
  <dd>Window the graph (type ? to the window prompt for more help).
  </dd>
  </dl>
  <dl id="l_x">
  <dt><b>x</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='x' Line='x' -->
  <dd>Set the quantity plotted along the ordinate (x axis).
  </dd>
  </dl>
  <dl id="l_y">
  <dt><b>y</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='y' Line='y' -->
  <dd>Set the quantity plotted along the abscissa (y axis).
  </dd>
  </dl>
  <dl id="l_I">
  <dt><b>I</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='I' Line='I' -->
  <dd>Interrupt the task immediately.  No information is saved in the database.
  </dd>
  </dl>
  <dl>
  <dt><b>:function [value]</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':function [value]' -->
  <dd>Print or set the function type (chebyshev|legendre).
  </dd>
  </dl>
  <dl>
  <dt><b>:show</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':show' -->
  <dd>Print current function and orders.
  </dd>
  </dl>
  <dl>
  <dt><b>:niterate [value], :lowreject [value], :highreject [value]</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':niterate [value], :lowreject [value], :highreject [value]' -->
  <dd>Print or set the iterative rejection parameters.
  </dd>
  </dl>
  <dl>
  <dt><b>:xorder [value]</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':xorder [value]' -->
  <dd>Print or set the order for the dispersion dependence.
  </dd>
  </dl>
  <dl>
  <dt><b>:yorder [value]</b></dt>
  <!-- Sec='CURSOR KEYS' Level=0 Label='' Line=':yorder [value]' -->
  <dd>Print or set the order for the echelle order dependence.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Emission and absorption features in echelle format spectra (see <i>apsum</i>)
  are identified interactively and from a line list and a dispersion
  function is determined.  The results of the line identifications and
  dispersion function are stored in a database for further reference and
  for use with the tasks <b>ecreidentify</b> and <b>ecdispcor</b>.  Also
  the reference spectrum keyword REFSPEC is added to the image header.
  This is used by <b>refspectra</b> and <b>ecdispcor</b>.
  </p>
  <p>
  Each spectrum in the input list is identified in turn.  Initially the
  order in the first image line is graphed.  The user may change the
  displayed order with the <span style="font-family: monospace;">'j'</span>, <span style="font-family: monospace;">'k'</span>, and <span style="font-family: monospace;">'o'</span> keys.  The initial feature
  list and dispersion function are read from the database if an entry
  exists.  The features are marked on the graph.  The image coordinates
  are in pixels unless a dispersion function is defined, in which case
  they are in user coordinate units (usually wavelength in Angstroms).
  The aperture number, pixel coordinate, coordinate function value, and
  user coordinate for the current feature are displayed on the status
  line.
  </p>
  <p>
  For consistency the orders are always identified by their aperture
  numbers in this task and all other tasks.  These are the
  identifications assigned when extracting the orders using the task
  <i>apsum</i>.  If the user has assigned true order numbers as the
  aperture numbers then there is no distinction between aperture and
  order number.  However, it is often the case that the aperture numbers
  are simply assigned sequentially and the true order numbers may not
  even be known.  Initially the orders are the same as the apertures
  numbers but after fitting a dispersion function the true order numbers
  will be determined.  This information is also recorded in the database
  and indicated in the graph titles but selecting an order to be graphed
  with <span style="font-family: monospace;">'o'</span> and the status line information is always in terms of the
  aperture number.
  </p>
  <p>
  The graphics cursor is used to select features and perform various
  functions.  A menu of the keystroke options and functions is printed
  with the key <span style="font-family: monospace;">'?'</span>.  The cursor keys and their functions are defined in
  the CURSOR KEYS sections and described further below.  The standard
  cursor mode keys are also available to window and redraw the graph and
  to produce hardcopy <span style="font-family: monospace;">"snaps"</span>.
  </p>
  <p>
  There are two types of feature selection functions;  defining new
  features and selecting previously defined features.  The key <span style="font-family: monospace;">'m'</span> marks
  a new feature nearest the cursor position.  The feature position is
  determined by the feature centering algorithm (see help for
  <b>center1d</b>).  The type of feature, emission or absorption, is set
  by the <i>ftype</i> parameter.  If the new position is within a distance
  given by the parameter <i>minsep</i> of a previous feature it is
  considered to be the same feature and replaces the old feature
  (normally the position of the new feature will be exactly the same as
  the original feature).  The coordinate list is searched for a match
  between the coordinate function value (when defined) and a user
  coordinate in the list.  If a match is found it becomes the default
  user coordinate which the user may override.  The new feature is marked
  on the graph and it becomes the current feature.  The redefinition of a
  feature which is within the minimum separation may be used to set the
  user coordinate from the coordinate list.  The key <span style="font-family: monospace;">'t'</span> allows setting
  the position of a feature to other than that found by the centering
  algorithm.
  </p>
  <p>
  The <span style="font-family: monospace;">'y'</span> key applies a peak finding algorithm and up to the maximum
  number of features (<i>maxfeatures</i>) are found.  If there are more
  peaks only the strongest are kept.  The peaks are then matched against
  the coordinate list to find user coordinate values.
  </p>
  <p>
  To select a different feature as the current feature the keys <span style="font-family: monospace;">'.'</span>, <span style="font-family: monospace;">'n'</span>,
  <span style="font-family: monospace;">'+'</span>, and <span style="font-family: monospace;">'-'</span> are used.  The <span style="font-family: monospace;">'.'</span> selects the feature nearest the cursor,
  the <span style="font-family: monospace;">'n'</span> and <span style="font-family: monospace;">'+'</span> select the next feature, and the <span style="font-family: monospace;">'-'</span> selects the
  previous feature relative to the current feature in the feature list as
  ordered by pixel coordinate.  These keys are useful when redefining the
  user coordinate with the <span style="font-family: monospace;">'u'</span> key and when examining features in zoom
  mode.  To change apertures (orders) the <span style="font-family: monospace;">'j'</span>, <span style="font-family: monospace;">'k'</span>, and <span style="font-family: monospace;">'o'</span> keys are
  used.
  </p>
  <p>
  If four or more features are identified spanning the range of the data
  (in pixel coordinates and in order number) or if a coordinate function
  is defined then the <span style="font-family: monospace;">'l'</span> key may be used to identify additional features
  from a coordinate list.  If a coordinate function is not defined the
  default function is fit to the user coordinates of the currently
  defined features.  Then for each coordinate value in the coordinate
  list the pixel coordinate is determined and a search for a feature at
  that point is made.  If a feature is found (based on the parameters
  <i>ftype, fwidth</i>, <i>cradius</i>, and <b>threshold</b>) its user
  coordinate value based on the coordinate function is determined.  If
  the coordinate function value matches the user coordinate from the
  coordinate list within the error limit set by the parameter <i>match</i>
  then the new feature is entered in the feature list.  Up to a maximum
  number of features, set by the parameter <i>maxfeatures</i>, may be
  defined in this way.  A new user coordinate function is fit to all the
  located features.  Finally, the graph is redrawn in user coordinates
  with the additional features found from the coordinate list marked.
  </p>
  <p>
  The <span style="font-family: monospace;">'f'</span> key fits a two dimensional function of the pixel coordinates
  and aperture number to the user coordinates.  The type of function and
  the orders are initially set with the parameters <i>function</i>,
  <i>xorder</i>, and <i>yorder</i>.  The value of the function for a
  particular pixel coordinate is called the function coordinate and each
  feature in the feature list has a function coordinate value.  The
  fitted function also is used to convert pixel coordinates to user
  coordinates in the graph.  Depending on the orders of the function
  four or more features are required covering at least two orders.
  A description of the dispersion function fitting is given the section
  ECHELLE DISPERSION FUNCTION FITTING.
  </p>
  <p>
  If a zero point shift is desired without changing the coordinate function
  the user may specify the coordinate of a point in the spectrum with
  the <span style="font-family: monospace;">'s'</span> key from which a shift is determined.  The <span style="font-family: monospace;">'g'</span> key also
  determines a shift by minimizing the difference between the user
  coordinates and the fitted coordinates.  This is used when a previously
  determined coordinate function is applied to a new spectrum having
  fewer or poorer lines and only a zero point shift can reasonably be
  determined.  Note that the zero point shift is in user coordinates
  for the fundamental order.  The shift for any particular order is then
  the zero point shift divided by the order number.
  </p>
  <p>
  Features may be delete with the key <span style="font-family: monospace;">'d'</span>.  All features are deleted when
  the <span style="font-family: monospace;">'a'</span> key immediately precedes the delete key.  Deleting the features
  does not delete the coordinate function.  To delete both the features
  and the dispersion function the initialize key <span style="font-family: monospace;">'i'</span> is used.  Note
  features deleted during dispersion function fitting also are removed
  from the feature list upon exiting the fitting package.
  </p>
  <p>
  It is common to transfer the feature identifications and coordinate
  function from one image to another.  When a new image without a
  database entry is examined, such as when going to the next image in the
  input list or selecting a new image with the <span style="font-family: monospace;">":image"</span> command, the
  current feature list and coordinate function are kept.  Alternatively,
  a database record from a different image may be read with the <span style="font-family: monospace;">":read"</span>
  command.  When transferring feature identifications between images the
  feature coordinates will not agree exactly with the new image feature
  positions and several options are available to reregister the feature
  positions.  The key <span style="font-family: monospace;">'c'</span> centers the feature nearest the cursor using
  the current position as the starting point.  When preceded with the <span style="font-family: monospace;">'a'</span>
  key all the features are recentered (the user must refit the coordinate
  function if desired).  As an aside, the recentering function is also
  useful when the parameters governing the feature centering algorithm
  are changed.
  </p>
  <p>
  The (c)entering function is applicable when the shift between the
  current and true feature positions is small.  Larger shifts may be
  determined automatically with the <span style="font-family: monospace;">'x'</span> function which correlates
  features in the image with the feature list.  The features are then
  recentered.  A zero point shift may also be given interactively with
  the <span style="font-family: monospace;">'s'</span> key by using the cursor to indicate the coordinate of a point
  in the spectrum.  If there are no features then the shift is exactly as
  marked by the cursor but if there are features the approximate shift is
  applied and then the features are recentered.  The shift is then the
  mean shift of the features after recentering.  The shift is used as a
  zero point offset added to the dispersion function.  The shift is
  computed in user coordinates for the fundamental order.  Shifts for
  each order are given by scaling of this shift.
  </p>
  <p>
  In addition to the single keystroke commands there are commands
  initiated by the key <span style="font-family: monospace;">':'</span> (colon commands).  As with the keystroke
  commands there are a number of standard graphics features available
  begining with <span style="font-family: monospace;">":."</span> (type <span style="font-family: monospace;">":.help"</span> for these commands).  The colon
  commands allow the task parameter values to be listed and to be reset
  within the task.  A parameter is listed by typing its name.  The colon
  command <span style="font-family: monospace;">":show"</span> lists all the parameters.  A parameter value is reset
  by typing the parameter name followed by the new value; for example
  <span style="font-family: monospace;">":match 10"</span>.  Other colon commands display the feature list
  (:features), control reading and writing records to the database (:read
  and :write), and set the graph display format.
  </p>
  <p>
  The feature identification process for an image is completed by typing
  <span style="font-family: monospace;">'q'</span> to quit.  Attempting to quit an image without explicitly recording
  changes in the feature database produces a warning message and an
  opportunity to record the information in the database.  As an immediate
  exit the <span style="font-family: monospace;">'I'</span> interrupt key may be used.  This does not save the feature
  information.
  </p>
  </section>
  <section id="s_echelle_dispersion_function_fitting">
  <h3>Echelle dispersion function fitting</h3>
  <p>
  If a minimum of four features over at least two orders, depending on
  the default function orders, have been identified a dispersion function
  relating the user coordinates to the extracted pixel coordinate and
  aperture number may be fit.  However, more features are preferable to
  determine changes in the dispersion as a function of position and
  order.
  </p>
  <p>
  The form of the function fit explicitly includes the basic order number
  dependence of echelle spectra; namely the wavelength of a particular
  point along the dispersion direction in different orders varies as the
  reciprocal of the order number.  Because of distortions, the differing
  extraction paths through the two dimensional image, and rotations of
  the spectra relative to the axis of constant dispersion (i.e. aligning
  the orders with the image columns or lines instead of aligning the
  emission and absorption features) there will be residual dependancies on
  the extracted pixel positions and orders.  These residual dependancies
  are fit by a two dimensional polynomial of arbitrary order including
  cross terms.  Because the basic order number dependence has been
  removed the orders should be relatively low.  Currently the functions
  are bi-dimensional chebyshev and legendre polynomials though other
  function may be added in the future.
  </p>
  <p>
  Since the true order number may not be known initially a linear
  relation between the aperture numbers and the order numbers is also
  determined which minimizes the residuals.  This relation allows an
  unknown offset and possible a reversed direction of increasing order.
  The fitted function is then represented as:
  </p>
  <div class="highlight-default-notranslate"><pre>
  y = offset +/- aperture
  
  wavelength = f (x, y) / y
  </pre></div>
  <p>
  where y is the order number and x is the extracted pixel coordinate along the
  dispersion.
   
  If the order offset is known initially or as a result of previous the <span style="font-family: monospace;">'o'</span>
  fit may be used.  The dispersion minimization for the order offset is
  then not done.  This will, therefore, be faster than using the full
  fit, key <span style="font-family: monospace;">'f'</span>, to also determine the order offset.
  </p>
  <p>
  The fitting is done interactively as a submode of <b>ecidentify</b> with its
  own set of cursor commands.  It is entered using the <span style="font-family: monospace;">'f'</span> key and exited using
  the <span style="font-family: monospace;">'q'</span> key.  The list of commands is given the CURSOR KEY section and is
  available from the fitting mode with <span style="font-family: monospace;">'?'</span>.  The functionality of this fitting
  is fairly simple; the function and orders may be changed, points may be deleted
  and undeleted, and the results of the fit may be displayed in various formats
  by selecting quantities to be plotted along either axis.  Generally one
  changes plotting of the pixel coordinate, order number, and wavelength
  along the x axis and residuals or radial velocity errors along the y axis.
  One switches between increasing the x order and the y order while switching
  between plotting verses x positions and order number until the residuals
  have been reduced to remove all systematic trends.
  </p>
  </section>
  <section id="s_database_records">
  <h3>Database records</h3>
  <p>
  The database specified by the parameter <i>database</i> is a directory of
  simple text files.  The text files have names beginning with 'ec' followed
  by the entry name, usually the name of the image.  The database text files
  consist of a number of records.  A record begins with a line starting with the
  keyword <span style="font-family: monospace;">"begin"</span>.  The rest of the line is the record identifier.  Records
  read and written by <b>ecidentify</b> have <span style="font-family: monospace;">"ecidentify"</span> as the first word of the
  identifier.  Following this is a name which may be specified following the
  <span style="font-family: monospace;">":read"</span> or <span style="font-family: monospace;">":write"</span> commands.  If no name is specified then the image name
  is used.  The lines following the record identifier contain
  the feature information and dispersion function coefficients.
  </p>
  </section>
  <section id="s_echelle_dispersion_functions">
  <h3>Echelle dispersion functions</h3>
  <p>
  The fitted echelle dispersion functions are evaluated as described in
  this section.  The basic equations are
  </p>
  <div class="highlight-default-notranslate"><pre>
  (1)  w = (f(x,o) + shift) / o
  (2)  o = ap * slope + offset
  </pre></div>
  <p>
  where w is the wavelength, x is the pixel coordinate along the order, o is
  the order, and ap is the aperture number.  The database parameter <span style="font-family: monospace;">"shift"</span>
  provides a wavelength zero point shift and the parameters <span style="font-family: monospace;">"slope"</span> and
  <span style="font-family: monospace;">"offset"</span> provide the transformation between aperture number and order.
  Note that the function f(x,o) and the shift are in terms of first order
  wavelengths.
  </p>
  <p>
  The database entries contain <span style="font-family: monospace;">"parameter value"</span> pairs.  This includes the
  parameters <span style="font-family: monospace;">"shift"</span>, <span style="font-family: monospace;">"offset"</span>, and <span style="font-family: monospace;">"slope"</span> defined above.  The default
  values for these if they are absent are 0, 0, and 1 respectively.  The
  <span style="font-family: monospace;">"coefficients"</span> parameter specifies the number of coefficients that follow
  and define the first order wavelength dispersion function.  The
  coefficients and functions are described below.
  </p>
  <p>
  The numerical values following the <span style="font-family: monospace;">"coefficients"</span> parameter, shown in
  the order in which they appear, have the following meaning.
  </p>
  <div class="highlight-default-notranslate"><pre>
  type        Function type: 1=chebychev, 2=legendre
  xpow        Highest power of x
  opow        Highest power of o
  xterms      Type of cross terms: Always 1 for echelle functions
  xmin        Minimum x for normalization
  xmax        Maximum x for normalization
  omin        Minimum o for normalization
  omax        Maximum o for normalization
  Cmn         Coefficients: m=0-xpow, n=0-opow, m varies first
  </pre></div>
  <p>
  The functions are evaluated by a sum over m and n up to the specified
  highest powers.
  </p>
  <div class="highlight-default-notranslate"><pre>
  (3)  f(x,o) = sum {Cmn * Pm * Pn}   m=0-xpow, n=0-opow
  </pre></div>
  <p>
  The Cmn are the coefficients of the polynomial terms Pm and Pn which
  are defined as follows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  Chebyshev:
      xnorm = (2 * x - (xmax + xmin)) / (xmax - xmin)
      P0 = 1.0
      P1 = xnorm
      Pm+1 = 2.0 * xnorm * Pm - Pm-1
  
      onorm = (2 * o - (omax + omin)) / (omax - omin)
      P0 = 1.0
      P1 = onorm
      Pn+1 = 2.0 * onorm * Pn - Pn-1
  
  Legendre:
      xnorm = (2 * x - (xmax + xmin)) / (xmax - xmin)
      P0 = 1.0
      P1 = xnorm
      Pm+1 = ((2m + 1) * xnorm * Pm - m * Pm-1)/ (m + 1)
  
      onorm = (2 * o - (omax + omin)) / (omax - omin)
      P0 = 1.0
      P1 = onorm
      Pn+1 = ((2n + 1) * onorm * Pn - n * Pn-1)/ (n + 1)
  </pre></div>
  <p>
  Note that the polynomial terms are obtained by first normalizing the x and
  o values to the range -1 to 1 and then iteratively evaluating them.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Because this task is interactive it is difficult to provide an actual
  example.  The following describes a typical usage on arc spectra.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ecidentify arc1.ec,arc2.ec
  </pre></div>
  <dl>
  <dt><b>(1)</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='' Line='(1)' -->
  <dd>The database is searched for an entry for arc1.ec.  None is found and
  the first order is plotted as a function of pixel coordinate.
  </dd>
  </dl>
  <dl>
  <dt><b>(2)</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='' Line='(2)' -->
  <dd>Using a line identification chart or vast experience one of the
  emission lines is identified and marked with the <span style="font-family: monospace;">'m'</span> key.  Using the
  cursor position a center is found by the centering algorithm.  The
  aperture number, pixel position, wavelength (which is currently the
  same as the pixel position), and a prompt for the true value with the
  default value INDEF is printed.  The true wavelength is typed in and the
  status line is redrawn with the information for the feature.
  </dd>
  </dl>
  <dl>
  <dt><b>(3)</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='' Line='(3)' -->
  <dd>The orders are changed with the <span style="font-family: monospace;">'j'</span>, <span style="font-family: monospace;">'k'</span>, or <span style="font-family: monospace;">'o'</span> key and further lines are
  identified with the <span style="font-family: monospace;">'m'</span> key.
  </dd>
  </dl>
  <dl>
  <dt><b>(4)</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='' Line='(4)' -->
  <dd>After a number of lines have been marked spanning the full range of the orders
  and pixel coordinates the key <span style="font-family: monospace;">'l'</span> is typed.  The program now fits a preliminary
  dispersion solution using the current function and function orders.  Using this
  function it examines each line in the line list and checks to see if there is
  an emission line at that point.  With many orders and lots of lines this may
  take some time.  After additional lines have been identified (up to
  <i>maxfeatures</i> lines) the function is refit.  Finally the current order
  is regraphed in user coordinates.
  </dd>
  </dl>
  <dl>
  <dt><b>(5)</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='' Line='(5)' -->
  <dd>Again we look at some orders and see if the automatic line identifications
  make sense.
  </dd>
  </dl>
  <dl>
  <dt><b>(6)</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='' Line='(6)' -->
  <dd>We next enter the dispersion function fitting mode with <span style="font-family: monospace;">'f'</span>.  A plot of the
  residuals vs. pixel position is drawn.  Some obvious misidentifications may
  be deleted with the <span style="font-family: monospace;">'d'</span> key.  One way to proceed with determining the
  function orders is to start at the lowest orders (xorder = 2 for linear
  and yorder = 1 for no order dependence beyond the basic dependence).  We then
  increase each order one at a time.  The x axis is changed between order
  number and pixel position using the <span style="font-family: monospace;">'x'</span> key to see the dependence on each
  dimension.  The orders are increased until there are no systematic trends
  apparent.  Normally the y order (for the aperture or order number dependence)
  is low such as 2 to 4 while the x order (for the dispersion direction) is
  whatever is needed to account for distortions.  Also one can prune deviant
  points with the <span style="font-family: monospace;">'d'</span> key.  Note that the order offset derived from the
  aperture number is given in the title block along with the RMS.  When done
  we exit with <span style="font-family: monospace;">'q'</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>(7)</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='' Line='(7)' -->
  <dd>The new function fit is then evaluated for all orders and the current order
  is redrawn based on the new dispersion.  Note also that the status line
  information for the current feature has both the fitted wavelength and the
  user identified wavelength.  We can add or delete lines and iterate with the
  fitting until we are happy with the feature list and dispersion function.
  </dd>
  </dl>
  <dl>
  <dt><b>(8)</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='' Line='(8)' -->
  <dd>Typing <span style="font-family: monospace;">'q'</span> exits the graph and prints a query about saving the information
  in the database.  We answer yes to this query.  Note that information can
  also be saved while still in the graphics loop using <span style="font-family: monospace;">":write"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>(9)</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='' Line='(9)' -->
  <dd>The next image in the list is then graphed but the last dispersion solution
  and feature list is maintained.  If the shift is small for the new arc we
  type <span style="font-family: monospace;">'a'</span> <span style="font-family: monospace;">'c'</span> to recenter all the features.  This does not refit the dispersion
  automatically so we then do <span style="font-family: monospace;">'f'</span>.  Alternatively, we could use the <span style="font-family: monospace;">'s'</span> or <span style="font-family: monospace;">'x'</span>
  keys to determine a large shift and do the recentering.
  </dd>
  </dl>
  <dl>
  <dt><b>(10)</b></dt>
  <!-- Sec='EXAMPLES' Level=0 Label='' Line='(10)' -->
  <dd>Finally we can exit with <span style="font-family: monospace;">'q'</span> or examine further images with the <span style="font-family: monospace;">":image"</span>
  command.
  </dd>
  </dl>
  </section>
  <section id="s_revisions">
  <h3>Revisions</h3>
  <dl id="l_ECIDENTIFY">
  <dt><b>ECIDENTIFY V2.11</b></dt>
  <!-- Sec='REVISIONS' Level=0 Label='ECIDENTIFY' Line='ECIDENTIFY V2.11' -->
  <dd>The dispersion units are now determined from a user parameter,
  the coordinate list, or the database entry.
  </dd>
  </dl>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  apsum, center1d, gtools, ecreidentify, identify
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'CURSOR KEYS' 'DESCRIPTION' 'ECHELLE DISPERSION FUNCTION FITTING' 'DATABASE RECORDS' 'ECHELLE DISPERSION FUNCTIONS' 'EXAMPLES' 'REVISIONS' 'SEE ALSO'  -->
  

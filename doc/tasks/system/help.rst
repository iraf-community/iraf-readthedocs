.. _help:

help: Print online documentation
================================

**Package: system**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  help [template]
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_template">
  <dt><b>template</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='template' Line='template' -->
  <dd>A string listing the modules or packages for which help is desired.
  Each list element may be a simple name or a pattern matching template.
  Abbreviations are permitted.  If <i>template</i> is omitted a long format
  menu will be printed for the current package, listing each task (or
  subpackage) and describing briefly what it is.
  </dd>
  </dl>
  <dl id="l_file_template">
  <dt><b>file_template = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='file_template' Line='file_template = no' -->
  <dd>If this switch is set the template is interpreted as a filename matching
  template, and all help blocks found in the named files are output.  The help
  database is not searched, hence manual pages can be printed or documents
  may be formatted without entering the files into a help database.
  In other words, <span style="font-family: monospace;">"help file.hlp fi+"</span> makes it possible to use <i>help</i> as
  a conventional text formatter.
  </dd>
  </dl>
  <dl id="l_all">
  <dt><b>all = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='all' Line='all = no' -->
  <dd>Print help for all help modules matching <i>template</i>, rather than only the
  first one found.
  </dd>
  </dl>
  <dl id="l_parameter">
  <dt><b>parameter = <span style="font-family: monospace;">"all"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='parameter' Line='parameter = "all"' -->
  <dd>If the value of this parameter is not <span style="font-family: monospace;">"all"</span>, only the help text
  for the given parameter will be printed.
  </dd>
  </dl>
  <dl id="l_section">
  <dt><b>section = <span style="font-family: monospace;">"all"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='section' Line='section = "all"' -->
  <dd>If the value of this parameter is not <span style="font-family: monospace;">"all"</span>, only the help text for the
  given section (e.g. <span style="font-family: monospace;">"usage"</span>, <span style="font-family: monospace;">"description"</span>, <span style="font-family: monospace;">"examples"</span>) will be printed.
  </dd>
  </dl>
  <dl id="l_option">
  <dt><b>option = help</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='option' Line='option = help' -->
  <dd>The option parameter specifies the type of help desired, chosen from
  the following:
  <dl>
  <dt><b>help</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='help' Line='help' -->
  <dd>Print the full help block for the named module.
  </dd>
  </dl>
  <dl>
  <dt><b>source</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='source' Line='source' -->
  <dd>Print the source code for the module (which often contains additional
  detailed comments).
  </dd>
  </dl>
  <dl>
  <dt><b>sysdoc</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='sysdoc' Line='sysdoc' -->
  <dd>Print the technical system documentation for the named module.
  </dd>
  </dl>
  <dl>
  <dt><b>directory</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='directory' Line='directory' -->
  <dd>Print a directory of all help blocks available for the named package.
  </dd>
  </dl>
  <dl>
  <dt><b>alldoc</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='alldoc' Line='alldoc' -->
  <dd>Print all help blocks in the file containing the help block for
  the named procedure (i.e., both the user and system documentation).
  </dd>
  </dl>
  <dl>
  <dt><b>files</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='files' Line='files' -->
  <dd>Print the names of all help files associated with the named modules or
  packages.
  </dd>
  </dl>
  <dl>
  <dt><b>summary</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='summary' Line='summary' -->
  <dd>Print only the titles and sizes of help blocks in referenced help files.
  The contents of the blocks are skipped.  Titles are printed for <i>all</i>
  help blocks found in the file containing the help block for the named module.
  </dd>
  </dl>
  </dd>
  </dl>
  <dl id="l_page">
  <dt><b>page = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='page' Line='page = yes' -->
  <dd>Pause after every page of output text.  Turning this off for large documents
  speeds up output considerably.
  </dd>
  </dl>
  <dl id="l_nlpp">
  <dt><b>nlpp = 59</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='nlpp' Line='nlpp = 59' -->
  <dd>The number of lines per page if output is redirected, e.g., to <i>lprint</i>.
  </dd>
  </dl>
  <dl id="l_lmargin">
  <dt><b>lmargin = 1</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lmargin' Line='lmargin = 1' -->
  <dd>Left margin on output.
  </dd>
  </dl>
  <dl id="l_rmargin">
  <dt><b>rmargin = 72</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rmargin' Line='rmargin = 72' -->
  <dd>Right margin on output.
  </dd>
  </dl>
  <dl id="l_search">
  <dt><b>search = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='search' Line='search = no' -->
  <dd>If enabled the 
  <a href="#l_template">template</A>
  is interpreted as a search string and the task
  is started with the search panel open with the results of the search.  The
  <a href="#l_file_template">file_template</A>
  parameter is ignored with search turned on.
  </dd>
  </dl>
  <dl id="l_home">
  <dt><b>home = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='home' Line='home = ""' -->
  <dd>The home page for the task.  If not set and no 
  <a href="#l_template">template</A>
  is specified
  the task will start with the online help in the main window, otherwise it
  may be set to a filename to be displayed when the task starts.  This file
  may contain a text help block which will be formatted before display,  or
  it may be a valid HTML file.  See below for a description of the format of
  a homepage file which provides links to tasks.
  </dd>
  </dl>
  <dl id="l_printer">
  <dt><b>printer = <span style="font-family: monospace;">"printer"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='printer' Line='printer = "printer"' -->
  <dd>Default hardcopy printer name. If the <i>value</i> of the parameter is the
  reserved string <span style="font-family: monospace;">"printer"</span>, the actual device is the value of the CL
  environment variable <i>printer</i>.
  </dd>
  </dl>
  <dl id="l_showtype">
  <dt><b>showtype = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='showtype' Line='showtype = no' -->
  <dd>Add task-type suffix in package menus?
  </dd>
  </dl>
  <dl id="l_quickref">
  <dt><b>quickref = <span style="font-family: monospace;">"uparm$quick.ref"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='quickref' Line='quickref = "uparm$quick.ref"' -->
  <dd>Name of the quick-reference file used for searching.  This file is created
  the first time the task is run in GUI mode or whenever it doesn't exist, 
  or when any help database file has been updated.
  </dd>
  </dl>
  <dl id="l_uifname">
  <dt><b>uifname = <span style="font-family: monospace;">"lib$scr/help.gui"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='uifname' Line='uifname = "lib$scr/help.gui"' -->
  <dd>The user interface file.   This file is what defines the look and behavior
  of all the graphical user interface elements.   Experts may create variants
  of this file.
  </dd>
  </dl>
  <dl id="l_helpdb">
  <dt><b>helpdb = <span style="font-family: monospace;">"helpdb"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='helpdb' Line='helpdb = "helpdb"' -->
  <dd>The filename of the help database to be searched.  If the <i>value</i> of the
  parameter is the reserved string <span style="font-family: monospace;">"helpdb"</span>, the actual filename is the value
  of the CL environment variable <i>helpdb</i>.
  </dd>
  </dl>
  <dl id="l_device">
  <dt><b>device = <span style="font-family: monospace;">"terminal"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='device' Line='device = "terminal"' -->
  <dd>Output device if the standard output is not redirected.  Allowable values
  include:
  <dl>
  <dt><b>terminal</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='terminal' Line='terminal' -->
  <dd>If the <i>value</i> of
  the parameter is the reserved string <span style="font-family: monospace;">"terminal"</span>,  the actual device name is
  the value of the CL environment variable <i>terminal</i>.  
  </dd>
  </dl>
  <dl>
  <dt><b>text</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='text' Line='text' -->
  <dd>Output the formatted help page as plain text.
  </dd>
  </dl>
  <dl>
  <dt><b>gui</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='gui' Line='gui' -->
  <dd>Invoke the GUI for browsing the help system.  This option will only work if
  the <i>stdgraph</i> environment variable is set the <i>xgterm</i>, and the
  user is running IRAF from an <i>XGterm</i> window.
  </dd>
  </dl>
  <dl>
  <dt><b>html</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='html' Line='html' -->
  <dd>Output the formatted help page as HTML text.
  </dd>
  </dl>
  <dl>
  <dt><b>ps (or postscript)</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='ps' Line='ps (or postscript)' -->
  <dd>Output the formatted help page as postscript.
  </dd>
  </dl>
  </dd>
  </dl>
  </section>
  <section id="s_basic_usage">
  <h3>Basic usage</h3>
  <p>
  Despite the complex appearing hidden parameters, <b>help</b> is easy to use
  for simple tasks.  <b>Help</b> is most commonly used to get help on the current
  package, and to get help on a program named in a CL menu.  To get help on
  the current package one need only type <b>help</b> without any arguments.
  For example, if the current package is <b>plot</b>, the command and its output
  might appear as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  pl&gt; help
          contour - Make a contour plot of an image
            graph - Graph one or more image sections or lists
             pcol - Plot a column of an image
            pcols - Plot the average of a range of image columns
             prow - Plot a line (row) of an image
            prows - Plot the average of a range of image lines
          surface - Make a surface plot of an image
  pl&gt;
  </pre></div>
  <p>
  To get help on a module one supplies the module name as an argument,
  </p>
  <div class="highlight-default-notranslate"><pre>
  pl&gt; help graph
  </pre></div>
  <p>
  and the manual page for the <b>plot.graph</b> program will be printed on the
  terminal.  To get a hardcopy of the manual page on the printer, the output
  may be redirected to the line printer, as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  pl&gt; help graph | lprint
  </pre></div>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The function of the <b>help</b> program is to perform a depth first search
  of the help database <i>helpdb</i>, printing help for all packages and modules
  matching the template.  By default the standard IRAF help database is searched,
  but any other help database may be searched if desired.  A help database is
  precompiled with the <b>mkhelpdb</b> program to speed up runtime searches for
  help modules.  The standard IRAF help database contains the documentation and
  source for all CL programs and system and math library procedures installed
  in IRAF.
  </p>
  <p>
  A help template is a string type parameter to the CL.  The form of a template
  is a list of patterns delimited by commas, i.e.,
  </p>
  <p>
  	<span style="font-family: monospace;">"pattern1, pattern2, ..., patternN"</span>
  </p>
  <p>
  The form of a pattern is
  </p>
  <p>
  	package_pattern.module_pattern
  </p>
  <p>
  If the <span style="font-family: monospace;">"."</span> is omitted <i>module_pattern</i> is assumed.  The standard pattern
  matching meta-characters, i.e., <span style="font-family: monospace;">"*?[]"</span>, are permitted in patterns.
  Simple patterns are assumed to be abbreviations.
  </p>
  </section>
  <section id="s_gui_operation">
  <h3>Gui operation</h3>
  <p>
  The GUI component of the task is a front-end to the IRAF 
  <a href="system.help"><b>help</b></A>
  task which provides on-the-fly conversion of help documents to HTML for
  presentation in the GUI or formatted PostScript for hardcopy.  
  The GUI is started by setting the 
  <a href="#l_device"><i>device</i></A>
  parameter to the special value <i>gui</i>, it is only available when using
  an XGterm window to start IRAF and assuming the <i>stdgraph</i> environment
  variable is set to xgterm.
  </p>
  <p>
  Help pages may be loaded on the command line, through use of a
  file browser, or by navigating the help databases using a familiar CL
  package menu scheme.   It also features a search capability similar to the 
  <a href="system.references"><b>references</b></A>
  task and a complete history mechanism. 
  </p>
  <p>
  When invoked with no command line arguments the task starts as a browser
  and the user is presented with a GUI that has the toplevel CL package menu
  in the upper navigation window.  The main display window below will contain
  any help page specified in the 
  <a href="#l_template">template</A>
  parameter or loaded on
  the command line by specifying the 
  <a href="#l_template">template</A>
  and 
  <a href="#l_file_template">file_template</A>
  parameters. If the 
  <a href="#l_search">search</A>
  parameter is enabled the 
  <a href="#l_template">template</A>
  is taken to be a search phrase and the database is searched for tasks
  matching the keyword and the GUI will appear with the search panel mapped
  so the user can select the task help to
  view.  When no 
  <a href="#l_template">template</A>
  is given the main display window will start with the page specified by the 
  <a href="#l_home">home</A>
  parameter, this can be a user-defined HTML file giving links to specific tasks
  (see below for details) or if 
  <a href="#l_home">home</A>
  is empty the display will contain the online help for the task.
  </p>
  <p>
  The first time the task is run, or whenever the help database is updated,
  a quick reference file (specified by the task 
  <a href="#l_quickref">quickref </A>
  parameter) and package menu file will be created in the user's <i>uparm</i>
  directory to speed up help searching and subsequent startups of the task.
  </p>
  </section>
  <section id="s_navigating_the_help_system">
  <h3>Navigating the help system</h3>
  <p>
  When run as a GUI browser <i>HELP</i> works very much like any WWW browser.
  The top panel is a list widget that will always contain a CL package listing,
  at startup this will be the toplevel <i>"Home"</i> package menu one would see
  when first logging into the CL containing the core system packages, NOAO
  package, and any site-specific external package, or in the case of starting
  with a specific task it will be the parent package for the task.  Additionally,
  system documents for the 
  <a href="os"><b>os</b></A>
  HSI routines and the 
  <a href="sys.imfort"><b>imfort</b></A>
  and
  <a href="math"><b>math</b></A>
  interfaces will be available in the <i>Home</i> package although
  these are programmatic interfaces and not tasks which can be executed.
  </p>
  <p>
  New packages or task help pages are loaded by selecting an item from the 
  package menu list using the left mouse button.  If the requested item is a 
  package, the menu listing will change as though the package were loaded in
  the CL, and the help display panel will contain a listing of the package
  tasks with a one-line description for each task such as would be seen with 
  a <i>"help &lt;package&gt;"</i> command using the standard task.  New items may then
  be selected using either the menu list or links in the display panel.  If the
  item is a task, the help page for the task will appear in the display panel.
  In either case new pages may be selected from the menu listing.  
  </p>
  <p>
  Specific help documents may also be requested by entering the task/package
  name in the <b>Topic</b> text widget above the menu list.  As when selecting
  from the package menu list, items selected this way will cause the menu
  list to change to the package menu for the parent package if the item is a
  task (displaying the help page in the display panel) or the package menu
  if the item is a package (displaying the one-liner package listing in the
  display panel).
  </p>
  <p>
  Using the <b>Back</b> button will revert to the previous page in the history
  list which will either be the previously loaded package or help page.
  Similarly, selecting the <b>Forward</b> button will move the next page further
  down in the history list, either button will become insensitive when the 
  end of the list on either end is reached.  Selecting the <b>Up</b> button will
  cause the browser to immediately jump up the previous package, skipping 
  over any help pages that were loaded in between.  The <b>Home</b> button will
  cause the default homepage (either the user-defined page if specified by the
  task <i>home</i> parameter or the online help) to be displayed.  Browsing
  in this way can also be done using the navigation menu created by hitting
  the right mouse button while in the main display panel.
  </p>
  <p>
  Users can also jump to specific pages in the history list using the
  <b>History</b> button on the main menubar.   The right column of the menu
  will indicate whether the item is a task, package, internal link or a text
  file.  The history list is truncated at about 40 entries in the menu but
  the user may work back incrementally by selecting the last item of the 
  menu, after which the History button will display the previous 40 entries.
  The history list may be cleared except for the current page by selecting
  the <i>Clear History</i> menu item.
  </p>
  </section>
  <section id="s_browsing_a_help_document">
  <h3>Browsing a help document</h3>
  <p>
  Once a help page is loaded the middle menubar above the display panel
  will change to activate widgets based on the position within the history
  list and options available for a particular page.  The left-most group
  of buttons are the standard navigation buttons described above.
  The middle group of buttons contains the <b>Sections</b> and
  <b>Parameters</b> buttons which are used to browse within a help document.
  The <i>Sections</i> button is a menu listing all of the sections found
  within a help page, allowing the user to jump to a specific section
  rather than scrolling through the entire document. The <i>Sections</i>
  menu is also available using the middle mouse button from the
  main display area.  The <i>Parameters</i> button is similarly a menu
  listing of all task parameter help sections found within the document.
  Both or either of these buttons will become insensitive when no section
  or parameter information is found in the document.
  </p>
  <p>
  The right-most group of buttons represent the various help options available
  for each page.  The default is to get the task help, however help pages
  may have an associated <b>source</b> file or <b>sysdoc</b> (e.g. if the task is
  a CL script there may be a pointer to the script source itself, or a package
  may have a general overview document listed as the system document).  Once
  a help page is loaded these buttons will change become sensitive if that option
  is available, simply select the button to view the option.  Selecting the
  <b>Files</b> button will bring up a panel listing all the files associated
  with a particular help topic.  When a help topic is selected and an option is
  defined but the file does not exist, the options button will display a yellow
  diamond icon even if the button is insensitive, a green icon indicates the
  currently selected option.  This feature may be disabled by selecting the
  <span style="font-family: monospace;">"Show missing files"</span> item from the main menubar <b>Options</b> menu.
  </p>
  </section>
  <section id="s_searching">
  <h3>Searching</h3>
  <p>
  Searching the help database is done by selecting the <b>Search</b> button
  from the main menubar to bring up the search panel.  Users may then enter 
  one or more keywords into the <b>Topic</b> field at the bottom of the panel
  and initiate the search with either a carriage return or hitting the
  <i>Search</i> button just beside it.  The panel will then show a list of all
  tasks and packages which match the search phrase along with a one-line
  description of the task.  Help pages may be displayed by selecting either the
  task or package link with the left mouse button, in both case the package
  menu list on the main help window will be updated to list the package
  contents allowing other tasks from that package to be selected in the normal
  way.
  </p>
  <p>
  By default the exact phrase entered in the topic window will be used for the
  search.  This can be relaxed by toggling the  <span style="font-family: monospace;">"Require exact match"</span> button
  at the top of the panel.  For example,  to search for all tasks matching
  <i>either</i> the keyword <span style="font-family: monospace;">"flat"</span> or <span style="font-family: monospace;">"field"</span> turn off the exact match
  toggle and the search will return not only tasks matching <span style="font-family: monospace;">"flat field"</span> but 
  also any task description containing only one of the words such as the
  VELVECT task which plots velocity <i>field</i>s.
  </p>
  <p>
  Within a help document itself one can search for a string by selecting
  the <b>Find</b> button from the main menubar to bring up a panel used to
  enter the search string.  When the text is entered the main display 
  window will reposition itself and highlight the text found within the
  document.  Searches can be repeated and will wrap around the document
  automatically, searches can be done either forward or backward through
  the text and may be case insensitive.
  </p>
  </section>
  <section id="s_user_defined_home_pages">
  <h3>User_defined home pages</h3>
  <p>
  By default the <i>help</i> GUI will start with the online help page displayed
  in the main help window.  The user can change this by setting the task
  <b>home</b> parameter to be a path to any valid file.  This file may be plain
  text, a help document in LROFF format which will be converted to HTML for
  display, or a native HTML document.
  </p>
  <p>
  HTML files may contain URLs of the form
  </p>
  <div class="highlight-default-notranslate"><pre>
  <b>&lt;a href=</b><i>[package.]task</i><b>&gt;</b><i>url_text</i><b>&lt;/a&gt;</b>
  </pre></div>
  <p>
  where <i>url_text</i> is the text to appear in the window and the URL itself
  consists of an optional package and task name delimited by a period.  For
  example, to create a link to the 
  <a href="onedspec.splot"><b>splot</b></A>
  task in a document one would use the URL
  </p>
  <div class="highlight-default-notranslate"><pre>
  <b>&lt;a href=onedspec.splot&gt;splot&lt;/a&gt;</b>
  </pre></div>
  <p>
  In this way users can create a homepage which serves as a <i>"bookmark"</i>
  file or index of shortcuts to the most commonly accessed help pages.
  </p>
  </section>
  <section id="s_loading_files">
  <h3>Loading files</h3>
  <p>
  Text files may be loaded on the command line when starting the task by
  specifying the filename and setting the
  <a href="#l_file_template">file_template</A>
  task parameter.  The named file
  will be searched for a <i>.help</i> LROFF directing indicating it contains
  a help block that will be converted to HTML for display.  If no help
  block is found the file will be displayed as-is, meaning existing
  HTML documents can be loaded and will be formatted correctly.
  </p>
  <p>
  Once the task is running users may load a file by selecting the <b>Open
  File...</b> menu item from the main menubar <b>File</b> menu or the
  right-mouse-button menu from within the main display area.  This will
  open a file browser allowing users to change directories by using the
  navigation buttons at the top of the panel, or selecting items from the
  leftmost directory listing.  Selecting a file on the rightmost list will
  cause it to be loaded and automatically formatted if it contains a help
  block.  The file list may be filtered to select only those files matching
  a particular template by changing the <b>Filter</b> box at the top of
  the panel.  Filenames or directories may be entered directly using the
  <b>Selection</b> box at the bottom of the panel.
  </p>
  </section>
  <section id="s_saving_files">
  <h3>Saving files</h3>
  <p>
  Once a file has been loaded in the browser it may be saved to disk as 
  either <i>source</i> (i.e. the original LROFF file if that was converted
  for the display, or whatever file is currently displayed regardless of
  format), <i>text</i> to save formatted plain text such as that produced
  by the standard <b>help</b> task, <i>HTML</i> to save the converted HTML
  used in the display, or <i>PostScript</i> to save formatted PostScript of
  the document such as that sent to the printer using the <b>Print</b> 
  button.  Not all options will be available depending on the format of the
  input text, unavailable options will be insensitive in the GUI.
  </p>
  <p>
  The <b>Save</b> panel is opened by selecting the <b>Save As...</b> menu
  item from the  main menubar <b>File</b> menu or the right-mouse-button
  menu from within the main display area.   The file browser operates the
  same as when loading images, the only difference is that file selection 
  simply defines the filename to be used and does not cause the save to
  occur automatically.  Users can overwrite existing files by selecting the
  <i>Options</i> toggle at the bottom of the panel.
  </p>
  </section>
  <section id="s_hardcopy_output_and_saving_disk_files_">
  <h3>Hardcopy output and saving disk files.</h3>
  <p>
  Help pages may be output to any configured IRAF printer by selecting the
  main menubar <b>Print</b> button to bring up the print panel.  Task help pages
  will be converted to formatted PostScript and may be sent to either a
  printer or saved to disk depending on the selection made in the printer 
  panel.  If the printer name is set to the special value <i>"printer"</i> then
  the device named by the CL <i>printer</i> environment variable will be used.
  When saving to disk files the default action is to save to a filename whose
  name is the task name plus a <span style="font-family: monospace;">".ps"</span> extension.  Either of these are changeable
  within the GUI as is the default page size to be used when generating the
  PostScript.
  </p>
  <p>
  The main menubar <b>File</b> button can also be used to bring up the file
  browser in order to save the current document to disk.  Help pages may be
  saved as either the origin LROFF source for the file, formatted text as you
  would get from the standard help task, HTML as is displayed in the GUI, or
  formatted PostScript.  The choice of formats is dictated by the type of file
  being displayed (e.g. you cannot save PostScript of a program source).
  </p>
  </section>
  <section id="s_lroff_directive_extensions_for_html">
  <h3>Lroff directive extensions for html</h3>
  <p>
  To better support HTML links within documents and to other help pages two
  new directives have been added to the LROFF text formatter.  These are
  <b>.hr</b> to specify a link (an HTML <i>HREF</i> directive) and <b>.hn</b>
  to specify a name (an HTML <i>NAME</i> directive).  The syntax for these are
  as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  <b>.hn</b><i> &lt;name&gt;</i>
  <b>.hr</b><i> &lt;link&gt; &lt;text&gt; </i>
  </pre></div>
  <p>
  where <i>&lt;name&gt;</i> is the destination name of an internal link, <i>&lt;link&gt;</i>
  is the URL of the link to be created, and <i>&lt;text&gt;</i> is the text to be
  displayed in the HTML.  The URL syntax is either a <span style="font-family: monospace;">'#'</span> character followed
  by a destination name, a simple <i>task</i> name or <i>package</i> name,
  or a <i>package.task</i> pair giving a more precise task.  For internal links
  the current document is repositioned so the name is at the top of the display,
  for task help links new help pages will be loaded in the browser.  
  </p>
  <p>
  These directives are ignored when converting the LROFF to either formatted
  plain text or PostScript.
  </p>
  <span id="examples_target"></span>
  </section>
  <section id="s_gui_examples">
  <h3>Gui examples</h3>
  <p>
  1) Start <i>help</i> as a GUI browser:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help dev=gui
  </pre></div>
  <p>
  2) Begin by searching for the phrase 'gauss', tasks and packages may be
  selected from the search panel which will appear when the task starts:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help gauss dev=gui search+
  </pre></div>
  <p>
  3) Load an LROFF help page in the browser at startup
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help mytask.hlp dev=gui file+
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Print the help text for the program <i>delete</i> in the package
  <i>system</i> (output will be directed to the terminal):
  </p>
  <div class="highlight-default-notranslate"><pre>
          cl&gt; help system.delete
  or
          cl&gt; help delete
  or
          cl&gt; help del
  </pre></div>
  <p>
  2. Print the help text on the line printer:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help delete | lprint
  </pre></div>
  <p>
  3. Print help for the current package:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help
  </pre></div>
  <p>
  4. Print the usage section of all modules in the package <b>images</b>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help images.* section=usage
  </pre></div>
  <p>
  5. Print a directory of all help blocks in the packages <b>clpackage</b>
  and <b>clio</b> (and any others whose names begin with the string <span style="font-family: monospace;">"cl"</span>):
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help cl* op=dir
  </pre></div>
  <p>
  6. Print a directory of each package in the database (useful for getting an
  overview of the contents of a help database):
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help * op=dir
  </pre></div>
  <p>
  7. Print the source for all of the string utilities in the system library
  package <b>fmtio</b>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help fmtio.str* op=source
  </pre></div>
  <p>
  8. Find all tasks that delete something:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help * | match delete
  </pre></div>
  <p>
  9. Print the manual pages for the <i>help</i> and <i>lprint</i> tasks on the
  default printer device:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help help,lprint | lpr
  </pre></div>
  <p>
  10. Capture the manual page for task <i>hedit</i> in a text file, in a form
  suitable for printing on any device.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help hedit dev=text &gt; hedit.txt
  </pre></div>
  <p>
  11. Print the manual page for task <i>hedit</i> as a Postscript file. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; help hedit dev=ps | lprint
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  On some systems, typing the next command keystroke before the end-of-page
  prompt is printed may result in the character being echoed (messing up the
  output) and then ignored when raw mode is enabled for the prompt.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <a href="system.references">references</A>
  <p>
  ,
  <a href="system.phelp">phelp</A>
  ,
  <a href="system.mkhelpdb">mkhelpdb</A>
  ,
  <a href="system.hdbexamine">hdbexamine</A>
  ,
  <a href="system.lroff">lroff</A>
  , the online task help documents.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'BASIC USAGE' 'DESCRIPTION' 'GUI OPERATION' 'NAVIGATING THE HELP SYSTEM' 'BROWSING A HELP DOCUMENT' 'SEARCHING' 'USER_DEFINED HOME PAGES' 'LOADING FILES' 'SAVING FILES' 'HARDCOPY OUTPUT AND SAVING DISK FILES.' 'LROFF DIRECTIVE EXTENSIONS FOR HTML' 'GUI EXAMPLES' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

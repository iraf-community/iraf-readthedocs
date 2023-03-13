.. _mkconfig:

mkconfig: Prepare a configuration file
======================================

**Package: photcal**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  mkconfig config 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_config">
  <dt><b>config</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='config' Line='config' -->
  <dd>The name of the new configuration file.
  </dd>
  </dl>
  <dl id="l_catalog">
  <dt><b>catalog</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catalog' Line='catalog' -->
  <dd>The source of the standard star catalog format description.
  <i>Catalog</i> may be one of the supported standard star
  catalogs maintained
  in the directory <span style="font-family: monospace;">"photcal$catalogs/"</span>, a catalog created with
  MKCATALOG, the standard input <span style="font-family: monospace;">"STDIN"</span>,
  or a file created by the user containing the catalog
  format description.
  <i>Catalog</i> is not prompted for if <i>template</i> is <span style="font-family: monospace;">""</span>.
  </dd>
  </dl>
  <dl id="l_observations">
  <dt><b>observations</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='observations' Line='observations' -->
  <dd>The source of the observations file format description.
  <i>Observations</i> may be a catalog created by MKNOBSFILE,
  MKOBSFILE, OBSFILE, or MKCATALOG, the standard input <span style="font-family: monospace;">"STDIN"</span>,
  or a file created by the user containing the observations file format
  description. <i>Observations</i> is not prompted for if <i>template</i> is <span style="font-family: monospace;">""</span>.
  </dd>
  </dl>
  <dl id="l_transform">
  <dt><b>transform </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='transform' Line='transform ' -->
  <dd>The source of the transformation equations definition.
  <i>Transform</i> may be the name of one of the supported standard star
  catalogs maintained in the directory <span style="font-family: monospace;">"photcal$catalogs/"</span>,
  the standard input <span style="font-family: monospace;">"STDIN"</span>, or a file created by the user
  containing the transformation equations definition.
  <i>Transform</i> is not prompted for if <i>template</i> is <span style="font-family: monospace;">""</span>.
  </dd>
  </dl>
  <dl id="l_template">
  <dt><b>template = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='template' Line='template = ""' -->
  <dd>The name of an existing configuration file that can be used as a template
  for the new configuration file.
  If <i>template</i> is the null string <span style="font-family: monospace;">""</span>, then MKCONFIG
  prompts the user for the source of the standard star catalog 
  and observations file format descriptions
  <i>catalog</i> and <i>observations</i>, and the source of the transformation
  equation definitions <i>transform</i>.
  If <i>template</i> exists,
  MKCONFIG copies <i>template</i> into <i>config</i> and enters the editor
  if <i>edit</i> is <span style="font-family: monospace;">"yes"</span>.
  </dd>
  </dl>
  <dl id="l_catdir">
  <dt><b>catdir = <span style="font-family: monospace;">")_.catdir"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catdir' Line='catdir = ")_.catdir"' -->
  <dd>The directory containing the supported standard star catalogs.
  The default parameter value  redirects <i>catdir</i>
  to a package parameter of the same name. A list of standard
  catalogs may be obtained by printing the file <span style="font-family: monospace;">"photcal$catalogs/README"</span>.
  Alternatively the user may create their own standard star catalogs 
  and standard star catalog directory.
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = no' -->
  <dd>Verify each new entry in the configuration file as it is entered?
  </dd>
  </dl>
  <dl id="l_edit">
  <dt><b>edit = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='edit' Line='edit = yes' -->
  <dd>Enter the editor and review the new configuration file?
  </dd>
  </dl>
  <dl id="l_check">
  <dt><b>check = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='check' Line='check = yes' -->
  <dd>Check the new configuration file for semantic and syntax errors?
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = no' -->
  <dd>Print detailed information about the results of the check step instead
  of only a short summary?
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  MKCONFIG is a script task which creates and/or edits the configuration
  file <i>config</i>. If the configuration file already
  exists MKCONFIG, quits with a warning message. If the configuration file is
  a new file, MKCONFIG either prompts the
  user for input if <i>template</i> = <span style="font-family: monospace;">""</span>, or copies the existing configuration
  file <i>template</i> into <i>config</i>.
  </p>
  <p>
  If <i>template</i>  is <span style="font-family: monospace;">""</span>, MKCONFIG prompts the user for:
  1) the source of the standard star catalog format description
  <i>catalog</i>, which assigns names to the columns of the standard star
  catalog,
  2) the source of the observations file format description
  <i>observations</i>, which assigns names to the columns of the observations file,
  3) and the source of the transformation equations <i>transform</i>, which
  defines the form of the transformation equations from the
  instrumental to the standard system.
  </p>
  <p>
  If <i>catalog</i>, <i>observations</i>, or <i>transform</i>
  are set to the standard input <span style="font-family: monospace;">"STDIN"</span>, MKCONFIG prompts for input from
  the terminal, verifying the input as it is entered if <i>verify</i> is <span style="font-family: monospace;">"yes"</span>. 
  </p>
  <p>
  If <i>catalog</i> is a standard star catalog name or a file name,
  MKCONFIG searches 1) the current directory for the associated format
  description file <span style="font-family: monospace;">"fcatalog.dat"</span>, 2) the directory
  <i>catdir</i> for the format description file <span style="font-family: monospace;">"fcatalog.dat"</span>,
  and 3) the current directory for a file called <span style="font-family: monospace;">"catalog"</span>, in that order.
  <i>Catalog</i> is usually one of the supported standard star catalogs or
  a standard star catalog created by the user with MKCATALOG. 
  </p>
  <p>
  If <i>observations</i> is an observations file name or a file name,
  MKCONFIG searches 1) the current directory for the format
  description file <span style="font-family: monospace;">"fobservations.dat"</span>, and 2)
  the current directory for a file called <span style="font-family: monospace;">"observations"</span>, in that order.
  <i>Observations</i> is usually created by the user with MKNOBSFILE or MKOBSFILE.
  </p>
  <p>
  If <i>transform</i> is assigned a standard star catalog name or a file name,
  MKCONFIG searches 1) the directory
  <i>catdir</i> for the transformation equations definition file
  <span style="font-family: monospace;">"ttransform.dat"</span>, and 2)
  the current directory for a file called <span style="font-family: monospace;">"transform"</span>, in that order.
  <i>Transform</i> is usually one of the supported standard star catalogs or
  <span style="font-family: monospace;">"STDIN"</span>.
  </p>
  <p>
  The default photometric standards directory is <span style="font-family: monospace;">"photcal$catalogs/"</span>.
  A list of supported catalogs is shown below.
  The standard catalog format description files may be listed or
  printed with the commands
  <span style="font-family: monospace;">"dir photcal$catalogs/f*.dat"</span> or <span style="font-family: monospace;">"lprint photcal$catalogs/f*.dat"</span> respectively.
  The standard transformation equation definition files may be listed or
  printed with
  the commands <span style="font-family: monospace;">"dir photcal$catalogs/t*.dat"</span> or <span style="font-family: monospace;">"lprint photcal$catalogs/t*.dat"</span>
  respectively.
  </p>
  <p>
  After data entry, and if <i>edit</i> is <span style="font-family: monospace;">"yes"</span>,
  MKCONFIG enters the default text editor defined by the
  IRAF environment variable <i>editor</i>.  Small
  corrections to the configuration file may be made at this point.
  Next the configuration file is checked for semantic and syntax errors
  if <i>check</i> is <span style="font-family: monospace;">"yes"</span> and the results are written on the terminal. 
  </p>
  </section>
  <section id="s_standard_catalog_format_and_transform_files">
  <h3>Standard catalog format and transform files</h3>
  <p>
  The list of standard star catalog files, catalog format description files
  and transformation equation definitions files is presented below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # catalogs      # formats               # transformations
  
  landolt.dat     flandolt.dat            tlandolt.dat
  </pre></div>
  </section>
  <section id="s_the_configuration_file">
  <h3>The configuration file</h3>
  <p>
  The <i>configuration file</i> is a text file which describes how the input data
  is organized in the input files, and defines the form of the transformation
  equations required to convert from the instrumental to the standard system.
  </p>
  <p>
  The input data is assumed to come from two sources,
  standard star catalogs known as <i>catalogs</i>
  and <i>observations</i> files.
  The <i>catalog</i> files contain the standard indices of a set of standard
  stars, referenced in the catalog by a name called the
  matching name.
  The <i>observations</i> files contain the instrumental magnitudes or colors of
  a subset of the standard stars and/or program stars, also referenced by a
  matching name.
  The names of the observed standard stars must match the names in the
  standard star catalog.  The matching names must be stored in column 1
  in both the catalog and observations files.
  </p>
  <p>
  The configuration file is divided up into three sections: the <i>catalog
  section</i> which describes the format of the catalog files, the
  <i>observations section</i> which describes the format of the observation 
  files, and the <i>transformation section</i> which defines the
  transformation equations. The catalog section must always appear before the
  observation section, and the observation section must always appear before the
  transformation section.
  </p>
  <p>
  The <i>catalog and observations sections</i> are used to assign
  names to the columns in the input catalog and observations files. 
  These columns may later be referenced by name and the names used
  as variables in the transformation equations.
  </p>
  <p>
  The <i>transformation section</i> is used to define the
  transformation equations,
  to specify which parameters are to be varied and which are to be held constant
  during the fitting process,
  and to assign initial values to all the parameters.
  Any number of transformation equations may be defined in
  the transformation section.
  </p>
  <p>
  The transformation section may also be used to, OPTIONALLY,
  define temporary variables (the set equations), define explicitly
  the derivatives of the transformation equations to be fit with respect
  to the parameters (derivative equations
  and delta declarations), define expressions for the weights and
  errors (weight and error equations), and define an expression to be
  plotted (the plot equation).
  </p>
  <p>
  For a detailed description
  of the grammar and syntax of the configuration file type <i>"help config"</i>.
  </p>
  <p>
  The following examples show typical configuration files for two different types
  of photometric calibrations.
  </p>
  <p>
  <i>Example 1</i>. A sample configuration file for reducing UBV photoelectric
  photometry. Note that the instrumental magnitudes are all on the right-hand
  side of the transformation equation and that the standard magnitudes and colors
  are all
  on the left-hand side. Once the values of the transformation equation
  parameters are computed by FITPARAMS using observations of the standard stars,
  standard magnitudes and colors for the program stars can be computed simply by
  evaluating the right-hand side of the transformation equation using
  the task EVALFIT. In this type of setup the equations are fit separately
  and evaluated separately. Note also the use of the error column declarations
  in the observation section, and the use of the const statement to fix the
  values of some parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Configuration file for reducing UBV photoelectric photometry.
  
  catalog
  
  V       2               # V magnitude
  BV      3               # B - V color
  UB      4               # U - B color
  
  observation
  
  v               2               # v instrumental magnitude
  b               3               # b instrumental magnitude
  u               4               # u instrumental magnitude
  error(v)        5               # error in v instrumental magnitude
  error(b)        6               # error in b instrumental magnitude
  error(u)        7               # error in u instrumental magnitude
  X               8               # airmass
  
  transformation
  
  fit     v1 = 0.0, v2=0.16, v3=-0.043
  const   v4 = 0.0
  VFIT:   V = v1 + v - v2 * X + v3 * (b - v) + v4 * X * (b - v)
  
  fit     b1 = 0.0, b2=0.09, b3=1.266
  const   b4 = 0.0
  BVFIT:  BV = b1 - b2 * X + b3 * (b - v) + b4 * X * (b - v)
  
  fit     u1 = 0.0, u2=0.300, u3=0.861
  const   u4 = 0.0
  UBFIT:  UB = u1 - u2 * X + u3 * (u - b) + u4 * X * (u - b)
  </pre></div>
  <p>
  <i>Example 2</i>. A sample configuration file for reducing UBV CCD photometry.
  Note that the instrumental magnitudes are all on the left-hand side of the
  transformation equations and the standard star magnitudes and colors
  are all on the right-hand
  side. Once the values of the transformation equation parameters have been
  computed by FITPARAMS using observations of the standard stars, the
  standard magnitudes and colors of the program stars
  can be computed by inverting the system of equations using the task
  INVERTFIT.
  In this type of setup the equations are fit independently, but evaluated
  as a system.
  Note also that the telescope filter slots 1, 2 and 3 were assigned to
  filters v, b and u respectively which is why MKNOBSFILE assigned the names
  m1, m2, m3 to v, b, and u respectively. The user can change these if desired.
  Note also the use of the error declaration statements in both the catalog
  and the observations section.
  </p>
  <div class="highlight-default-notranslate"><pre>
  catalog
  
  V               2       # V magnitude
  BV              3       # B - V color
  UB              4       # U - B color
  error(V)        5       # error in V magnitude
  error(BV)       6       # error in B-V color
  error(UB)       7       # error in U-B color
  
  observation
  
  ut1             3       # ut time of filter 1 observation
  X1              4       # airmass of filter 1 observation
  m1              7       # filter 1 instrumental magnitude
  error(m1)       8       # error in filter 1 instrumental magnitude
  ut2             10      # ut time of filter 2 observation
  X2              11      # airmass of filter 2 observation
  m2              14      # filter 2 instrumental magnitude
  error(m2)       15      # error in filter 2 instrumental magnitude
  ut3             17      # ut time of filter 3 observation
  X3              18      # airmass of filter 3 observation
  m3              19      # filter 3 instrumental magnitude
  error(m3)       20      # error in filter 3 instrumental magnitude
  
  transformation
  
  fit   u1 = 0.0, u2=0.68, u3=0.060
  UFIT: m3 = u1 + V + BV + UB + u2 * X3 + u3 * UB
  
  fit   b1 = 0.0, b2=0.30, b3=0.010
  BFIT: m2 = b1 + V + BV + b2 * X2 + b3 * BV
  
  fit   v1 = 0.0, v2=0.15, v3=0.000
  VFIT: m3 = v1 + V + v2 * X3 + v3 * BV
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Type in from scratch a new configuration file to reduce some UBV
  photoelectric photometry. The catalog and observations file are simple
  text files written with the user's own data acquisition software, whose
  format is known by the user.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; mkconfig ubv.cfg
  
      ... answer "STDIN" in response to the query for the catalog
          parameter, and enter the standard star catalog format
          description as prompted
  
      ... a sample input session is shown below, note that in this
          examine &lt;EOF&gt; is implemented as ^Z
  
  ENTER THE STANDARD STAR CATALOG FORMAT DESCRIPTION
  
  Enter column definition (name number, ?=help, &lt;EOF&gt;=quit entry): V 2
  Enter column definition (name number, ?=help, &lt;EOF&gt;=quit entry): BV 3
  Enter column definition (name number, ?=help, &lt;EOF&gt;=quit entry): UB 4
  Enter column definition (name number, ?=help, &lt;EOF&gt;=quit entry): ^Z
  
      ... answer "STDIN" in response to the query for the
          observations parameter, and enter the observations file
          format description as prompted
  
      ... a sample input session is shown below, note that in this
          example &lt;EOF&gt; is implemented as ^Z
  
  ENTER THE OBSERVATIONS FILE FORMAT DESCRIPTION
  
  Enter column definition (name number, ?=help, &lt;EOF&gt;=quit entry): v 2
  Enter column definition (name number, ?=help, &lt;EOF&gt;=quit entry): b 3
  Enter column definition (name number, ?=help, &lt;EOF&gt;=quit entry): u 4
  Enter column definition (name number, ?=help, &lt;EOF&gt;=quit entry): X 5
  Enter column definition (name number, ?=help, &lt;EOF&gt;=quit entry): ^Z
  
      ... answer "STDIN" in response to the query for the
          transform parameter, and enter the transformation
          equations as prompted
  
      ... a sample input session is shown below for a single equation is
          shown below, note that in this example &lt;EOF&gt; is implemented as
          ^Z
  
  ENTER THE TRANSFORMATION EQUATIONS
  
  Enter the label and functional form for EQUATION 1
  
  Enter label (e.g. VFIT) (label, ?=help, &lt;EOF&gt;=quit entry): VFIT
  Enter equation (equation, equation\=continue, ?=help, &lt;EOF&gt;=quit entry):
  V = v + v1 + v2 * X + v3 * (b - v)
  
  Enter initial values for the parameters to be fit in EQUATION 1
  
  Enter parameter 1 (name value, ?=help, &lt;EOF&gt;=quit entry):v1 25.
  Enter parameter 2 (name value, ?=help, &lt;EOF&gt;=quit entry):v2 -.15
  Enter parameter 3 (name value, ?=help, &lt;EOF&gt;=quit entry):v3 1.06
  Enter parameter 4 (name value, ?=help, &lt;EOF&gt;=quit entry):^Z
  
  Enter initial values for the parameters to be held constant in
  EQUATION 1
  
  Enter parameter1 and value (name value, ?=help, &lt;EOF&gt;=quit entry):^Z
  
  Enter the label and functional form for EQUATION 2
  
  Enter label (e.g. VFIT) (label, ?=help, &lt;EOF&gt;=quit entry): BFIT
  
      ... after the program enters the editor make any small changes
          required
  
      ... examine the final output for errors
  
  ph&gt; edit ubv.cfg
  
      ... correct any errors with the editor
  
  ph&gt; chkconfig ubv.cfg
  
      ... check the newly edited file for errors
  </pre></div>
  <p>
  2. Create a configuration file to reduce some JHK photometry. In this
  example the user has created a JHK standard star catalog called jhkcat
  using the task MKCATALOG, an observations file called jhkobs
  using the task MKNOBSFILE, and has decided to type in the transformation
  equations by hand using the default editor.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; mkconfig jhk.cfg jhkcat jhkobs
  
      ... answer "STDIN" in response to the query for the
          transform parameter, followed by &lt;EOF&gt;, usually ^Z
          to terminate prompting for the transformation equations
  
      ... use the editor to enter the transformation equations
  
      ... check the result for errors
  
  ph&gt; edit jhk.cfg
  
      ... correct errors found in previous run using the editor
  
  ph&gt; chkconfig jhk.cfg
  
      ... check the edited file for errors
  </pre></div>
  <p>
  3. Create a new configuration file for reducing some UBVR photometry, using 
  the UBVR standards in the landolt UBVRI standard star catalog. The standard
  star observations file <span style="font-family: monospace;">"stdobs"</span> was created with the task MKNOBSFILE.
  </p>
  <div class="highlight-default-notranslate"><pre>
  ph&gt; mkconfig ubvr.cfg landolt stdobs landolt
  
      ... read in the catalog format description for the
          landolt UBVRI standards catalog
  
      ... read in the observations file format description
          created by a previous run of mknobsfile
  
      ... read in the sample transformation description file for the
          landolt UBVRI system
  
      ... use the editor to delete any references to catalog
          variables that are not going to be used in the
          transformation equations, and to edit the transformation
          equations as desired
  
      ... check the result for errors
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
  edit,chkconfig,mknobsfile,mkobsfile
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'STANDARD CATALOG FORMAT AND TRANSFORM FILES' 'THE CONFIGURATION FILE' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

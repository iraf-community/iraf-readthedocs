.. _parameters:

parameters: Discussion of parameter attributes
==============================================

**Package: language**

.. raw:: html

  <section id="s_discussion">
  <h3>Discussion</h3>
  <p>
  1. <i>Introduction</i>
  </p>
  <p>
      Parameters are the primary means of communicating information between
  the user and IRAF tasks, and between separate IRAF tasks.  Each user
  effectively has their own copy of the parameters for the tasks they run,
  and by tailoring these as they wish, they may customize the IRAF environment.
  Here we describe characteristics of IRAF parameters.
  The syntax of parameter declarations is described elsewhere.
  </p>
  <p>
  2. <i>Parameter Types</i>
  </p>
  <p>
      The CL supports a variety of parameter datatypes, from the conventional
  string, integer, and floating point types, to the exotic struct and cursor
  types.  There is no complex type in the CL.
  </p>
  <dl id="l_char">
  <dt><b>char</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='char' Line='char' -->
  <dd>Character parameters are used to store strings of ASCII characters.
  By default character parameters have a maximum length of 64 characters,
  but this may be extended using the <i>length</i> option when the parameter
  is declared.  A character parameter consisting of a single character can
  usually be treated as an integer, with a value equal to the ASCII value
  of the character.
  </dd>
  </dl>
  <dl id="l_int">
  <dt><b>int</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='int' Line='int' -->
  <dd>Integer parameters are used to store integer information.  Integer parameters
  are stored internally as a long integer, permitting at least 32 bits of
  precision.
  </dd>
  </dl>
  <dl id="l_real">
  <dt><b>real</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='real' Line='real' -->
  <dd>Real parameters are stored internally as double's.
  In general they may be entered with or without a decimal point,
  and with or without an exponent.  Note that the exponent should be
  entered using an E not a D.
  </dd>
  </dl>
  <dl id="l_bool">
  <dt><b>bool</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='bool' Line='bool' -->
  <dd>Boolean parameters may only have the values <i>yes</i> or <i>no</i>.
  </dd>
  </dl>
  <dl id="l_file">
  <dt><b>file</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='file' Line='file' -->
  <dd>File parameters are basically character parameters which are required
  to be valid file names.  All operations legal on characters are legal
  on file parameters.  Various checks on the accessibility or existence
  of a file may be automatically performed when a <i>file</i> type parameter
  is used at runtime.
  </dd>
  </dl>
  <dl id="l_struct">
  <dt><b>struct</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='struct' Line='struct' -->
  <dd>Struct parameters are characters strings which are treated specially by
  the scan and fscan functions.  Scan and fscan set structs to the
  remainder of the line being scanned without further parsing.
  </dd>
  </dl>
  <dl id="l_gcur">
  <dt><b>gcur, imcur</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='gcur' Line='gcur, imcur' -->
  <dd>The cursor parameters have a character string value with a predefined cursor
  value format.  When a cursor type parameter is read in <span style="font-family: monospace;">"query"</span> mode, the
  hardware cursor on the graphics terminal or image display is physically read.
  If the cursor parameter is list-structured, cursor input may also be taken
  from a list (text file).  For a more detailed discussion of cursor control
  in the CL, type <i>help cursors</i>.
  </dd>
  </dl>
  <p>
  3. <i>List-Directed Parameters</i>
  </p>
  <p>
      Frequently one may have a list of values, e.g. numbers or file names,
  which one wishes to analyze in turn.  To do this one may use a list-directed
  parameter.  The parameter is defined with its value field set
  to the name of a file containing the list.  The next time it is referenced
  its value will not be the string containing the file name, but rather
  the first value in the list.  Subsequent calls will return later
  values in the list until an end-of-file is reached, at which point
  the parameter will appear to be undefined.  The file may be
  rewound using the p_filename attribute of the parameter.  Assigning the
  null string to a list parameter closes the associated list file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  int     *list = "listfile.lis"
  int     cur_val
  
  for (i=1;  i &lt; nlist;  i+=1) {
      cur_val = list
      analyze (cur_val)
  }
  </pre></div>
  <p>
  A common usage of struct list-directed parameters is to read files in
  conjunction with the <i>fscan</i> function.  The following example prints
  out a file.
  </p>
  <div class="highlight-default-notranslate"><pre>
  struct  *slist = "filer.lis"
  struct  line
  
  while (fscan (slist, line) != EOF)
      print (line)
  </pre></div>
  <p>
  4. <i>Modes</i>
  </p>
  <p>
      The mode of a parameter determines two qualities: whether the parameter
  is prompted for when it is accessed, and whether the parameter is <span style="font-family: monospace;">"learned"</span>,
  i.e. whether its value is saved between invocations of a task.
  </p>
  <p>
  A hidden parameter is never prompted for unless it is undefined
  or has an illegal value.  A query parameter is prompted for every time
  it is referenced, except that a query parameter which is set on a
  command line is not queried for when it is accessed within that task.
  </p>
  <p>
  These are the two basic modes, but a parameter may also be defined
  to be automatic.  This means that the parameter will use the mode
  not of the task, but of the package the task is part of, or by the CL.
  When an automatic parameter is referenced the CL searches
  up this hierarchy to find a mode which is not automatic and uses
  this for the mode.  If the mode switch at all levels is automatic
  then the mode is set to hidden.  The mode switch at the task, package
  and CL levels is determined by the VALUE, not the mode, of the
  parameter with the name <span style="font-family: monospace;">"mode"</span> associated with the task, package or CL.
  </p>
  <p>
  Query and automatic parameters are learned by default, while hidden parameters
  are not.
  </p>
  <p>
  5. <i>Ranges</i>
  </p>
  <p>
      The CL supports ranges for integer and real variables, and enumeration
  lists for character strings.  A user may specify either or both of a minimum
  and maximum for numbers, and the CL will reject
  any values which fall out of this range.  Range checking is only
  performed during querying, or inside <i>eparam</i>, not when a value
  is assigned directly.  For an enumerated string the input string
  is matched against any of the enumerated possibilities
  using a minimum-matching technique.  A value with no match is rejected.
  </p>
  <p>
  6. <i>Parameter Attributes</i>
  </p>
  <p>
      The user may access the different elements of a parameter using
  the parameter attributes.  For some parameters certain of the
  attributes will be meaningless or undefined.
  </p>
  <dl id="l_p_name">
  <dt><b>p_name</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='p_name' Line='p_name' -->
  <dd>The name of the parameter.
  </dd>
  </dl>
  <dl id="l_p_type">
  <dt><b>p_type</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='p_type' Line='p_type' -->
  <dd>A string indicating the basic type of the parameter:
  <div class="highlight-default-notranslate"><pre>
  b       -- boolean
  i       -- int
  r       -- real
  s       -- string/char
  f       -- file
  struct  -- struct
  gcur    -- graphics cursor
  imcur   -- image cursor=
  </pre></div>
  </dd>
  </dl>
  <dl id="l_p_xtype">
  <dt><b>p_xtype</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='p_xtype' Line='p_xtype' -->
  <dd>This is the same as p_type except that the string is prefixed by <span style="font-family: monospace;">"*"</span>
  if the parameter is list directed.
  </dd>
  </dl>
  <dl id="l_p_mode">
  <dt><b>p_mode</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='p_mode' Line='p_mode' -->
  <dd>A string indicating the mode of the parameter composed of the characters:
  <div class="highlight-default-notranslate"><pre>
  q  --  query
  a  --  automatic
  h  --  hidden
  l  --  learned
  </pre></div>
  </dd>
  </dl>
  <dl id="l_p_value">
  <dt><b>p_value</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='p_value' Line='p_value' -->
  <dd>The value of the parameter.  For a list-directed parameter this is a
  element in the file, not the file name.  Generally this is what is accessed
  when the parameter attribute is not specified.
  </dd>
  </dl>
  <dl id="l_p_length">
  <dt><b>p_length</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='p_length' Line='p_length' -->
  <dd>For string type parameters (i.e. char, struct, file, gcur, imcur),
  the maximum length of the string.
  </dd>
  </dl>
  <dl id="l_p_mimimum">
  <dt><b>p_mimimum</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='p_mimimum' Line='p_mimimum' -->
  <dd>The minimum value for a parameter.  Also for enumerated strings
  the enumeration list.
  </dd>
  </dl>
  <dl id="l_p_maximum">
  <dt><b>p_maximum</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='p_maximum' Line='p_maximum' -->
  <dd>The maximum value for a parameter.
  </dd>
  </dl>
  <dl id="l_p_filename">
  <dt><b>p_filename</b></dt>
  <!-- Sec='DISCUSSION' Level=0 Label='p_filename' Line='p_filename' -->
  <dd>For list-directed parameters the file name associated with the parameter.
  </dd>
  </dl>
  <p>
  Attributes may appear on either side of an equals sign, e.g.
  </p>
  <div class="highlight-default-notranslate"><pre>
  list.p_filename = "test.fil"
  = str.p_length
  range = integ.p_maximum - integ.p_minimum
  list.p_xtype =
  = system.page.first_page.p_minimum      # Fully qualified.
  </pre></div>
  <p>
  It is illegal to assign to the p_name, p_type and p_xtype fields.
  Most of the direct use of the parameter attributes is expected to be
  in systems level programming.
  </p>
  <p>
  7. <i>Arrays</i>
  </p>
  <p>
      The user may define arrays of arbitrary dimensionality within the CL.
  The arrays are referenced in the conventional fashion with
  the index list enclosed in square brackets, and the individual
  elements separated by commas.  In their internal representation,
  arrays are similar to those in Fortran, with the first element
  changing fastest as one traverses memory.  The limits of
  each index may be specified.
  </p>
  <p>
  In general the CL can only access one element of the array at a time
  but there is an automatic looping feature which permits the
  appearance of array arithmetic.  Any executable statement
  in which an array is referenced but  in which the exact element of the array
  is not defined (an <span style="font-family: monospace;">"open"</span> array reference)
  will cause the CL to implicitly execute that
  statement within a loop over all the elements of the array.  More
  than one <span style="font-family: monospace;">"open"</span> array may appear in the expression but they
  agree on the limits of the loop.  For example,
  </p>
  <div class="highlight-default-notranslate"><pre>
  real x[20,20], y[20], z[10,20], t[20]
  
  y = x[1,*]
  t = log(y)
  z = x[1:10,*]
  </pre></div>
  <p>
  8. <i>Scope</i>
  </p>
  <p>
      A parameter is known via an implicit reference if the task in which
  it is defined is active.  In an implicit reference the parameter
  name only, without a task or package qualifier, is given.  The CL
  is always active, so that its parameters are always known.  In a
  script, the script itself is active, so its parameters may be used
  implicitly.  If the script calls another task, that sub-task may
  reference the invoking tasks parameters implicitly.
  </p>
  <p>
  For an explicit reference, i.e. with task and package qualifiers,
  the parameter is known if the package in which the task is defined
  is active.  For example, when starting the CL, the <span style="font-family: monospace;">"lists"</span> package
  is not active, thus the parameters of the <span style="font-family: monospace;">"sort"</span> task may not
  be referenced even in the form <span style="font-family: monospace;">"lists.sort.param"</span>.  However since
  the system package is activated during login to the CL, the parameters
  of <span style="font-family: monospace;">"page"</span> may be referenced by <span style="font-family: monospace;">"page.param"</span>.  In general a package
  qualifier is used only to remove ambiguity between tasks with the
  same name in two different packages.
  </p>
  <p>
  9. <i>Storage</i>
  </p>
  <p>
      There are several places in which parameters are stored.
  On disk the CL searches
  for the parameters for a task in three locations.  For a procedure
  script, the default parameters are found in the script file itself, while
  other scripts and executables have a parameter file with defaults in
  the same directory as the script or executable.  These default values
  are used the first time a task is run, or whenever the default values
  have been updated more recently than the user's copy of the parameters.
  The user's copy is created when a task terminates, and retains any
  <span style="font-family: monospace;">"learned"</span> changes to the parameters.  It is created in a directory
  pointed to by the IRAF logical <span style="font-family: monospace;">"uparm"</span> which is usually a sub-directory
  of the default IRAF directory for the user.
  </p>
  <p>
  The user may also use in-core storage for the parameters using
  the cache command.  This keeps parameters for frequently used tasks
  available without requiring disk access.  Cached parameters
  are copied to disk when the CL exits, or when the update command
  is used.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  lparam, eparam, cache, unlearn, update, cursor
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'DISCUSSION' 'SEE ALSO'  -->
  

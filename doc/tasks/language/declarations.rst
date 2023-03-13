.. _declarations:

declarations: Parameter/variable declarations
=============================================

**Package: language**

.. raw:: html

  <section id="s_syntax">
  <h3>Syntax</h3>
  <div class="highlight-default-notranslate"><pre>
  vartype [*]varname[index_list] [= init_value] [{options}] [, ...]
  
    or
  
  vartype [*]varname[index_list] [{init_value [, options]}] [, ...]
  </pre></div>
  </section>
  <section id="s_elements">
  <h3>Elements</h3>
  <dl id="l_vartype">
  <dt><b>vartype</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='vartype' Line='vartype' -->
  <dd>One of the legal variable types, i.e.:
  	int, bool, char, real, gcur, imcur, struct, file
  </dd>
  </dl>
  <dl id="l_varname">
  <dt><b>varname</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='varname' Line='varname' -->
  <dd>The name of the variable or parameter.  The name must begin with
  an alphabetic character or <span style="font-family: monospace;">'_'</span> and should be fewer than 64 characters
  in length.  If the name is preceded by a <span style="font-family: monospace;">'*'</span>, then the variable
  is 'list-directed', meaning that a new value is taken from a list
  each time the parameter is read.
  </dd>
  </dl>
  <dl id="l_index_list">
  <dt><b>index_list</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='index_list' Line='index_list' -->
  <dd>The index_list consists of a series of ranges enclosed in square brackets.
  A range may be a single integer in which case the range is from 1 to
  that integer, or two integers separated by a colon.  The second integer
  must be larger than the first.  Ranges are separated by commas. In
  the special case that no ranges are specified by the user, the variable
  is assumed to be a one-dimensional array with a  range from 1 to the
  number of elements in the initialization list.
  </dd>
  </dl>
  <dl id="l_init_value">
  <dt><b>init_value</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='init_value' Line='init_value' -->
  <dd>The initialization value is a single value for scalar parameters but
  may be a list for array.  A repetition count may be specified in the form
  	rep_count (value)
  which is equivalent to value repeated the rep_count times.
  The values in the initialization list are separated by commas.
  </dd>
  </dl>
  <dl id="l_options">
  <dt><b>options</b></dt>
  <!-- Sec='ELEMENTS' Level=0 Label='options' Line='options' -->
  <dd><br>
  Options define certain characteristics of the variables.  Each
  options has the form opt_name=value where value is a constant.
  The current options are:
  <dl>
  <dt><b>mode</b></dt>
  <!-- Sec='ELEMENTS' Level=1 Label='mode' Line='mode' -->
  <dd>Determines whether the parameter is queried for and whether
  it is learned after task execution.  The default mode for parameters
  declared in the argument list of a CL procedure is <span style="font-family: monospace;">"a"</span>, and <span style="font-family: monospace;">"h"</span> otherwise.
  </dd>
  </dl>
  <dl>
  <dt><b>min</b></dt>
  <!-- Sec='ELEMENTS' Level=1 Label='min' Line='min' -->
  <dd>The minimum allowable value for the parameter.  If omitted, no min checking
  is performed.
  </dd>
  </dl>
  <dl>
  <dt><b>max</b></dt>
  <!-- Sec='ELEMENTS' Level=1 Label='max' Line='max' -->
  <dd>The maximum allowable value for the parameter.  If omitted, no max checking
  is performed.
  </dd>
  </dl>
  <dl>
  <dt><b>prompt</b></dt>
  <!-- Sec='ELEMENTS' Level=1 Label='prompt' Line='prompt' -->
  <dd><br>
  The prompt to be used when the parameter is queried for.
  </dd>
  </dl>
  <dl>
  <dt><b>enum</b></dt>
  <!-- Sec='ELEMENTS' Level=1 Label='enum' Line='enum' -->
  <dd>The set of allowable string values for a string valued parameter.
  The character <span style="font-family: monospace;">'|'</span> delimits successive enumerated strings.
  </dd>
  </dl>
  <dl>
  <dt><b>filetype</b></dt>
  <!-- Sec='ELEMENTS' Level=1 Label='filetype' Line='filetype' -->
  <dd>For a <i>file</i> type parameter, a string containing characters giving
  file characteristics to be checked for when the file parameter is used.
  <dl>
  <dt><b></b></dt>
  <!-- Sec='ELEMENTS' Level=2 Label='' Line=' ' -->
  <dd><div class="highlight-default-notranslate"><pre>
  r       file exists and is readable
  w       file exists and is writable
  n       file does not exist
  b       file is a binary file
  t       file is a text file
  </pre></div>
  </dd>
  </dl>
  </dd>
  </dl>
  <dl>
  <dt><b>length</b></dt>
  <!-- Sec='ELEMENTS' Level=1 Label='length' Line='length' -->
  <dd>For a string type parameter, the number of characters of storage to
  allocate for the string.  If the actual length of a string later exceeds
  the allocated value the string will be silently truncated.
  </dd>
  </dl>
  Note that all string constants in an options list must be enclosed in
  quotes.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Declaration statements are used for inline declaration of parameters and
  local variables.   A declaration after the begin statement of a procedure
  script is a declaration of a local variable, but any other declaration
  defines a parameter.  Parameters are generally saved between invocations
  of a script while local variables are not.
  </p>
  <p>
  Parameter and variable declarations should always precede executable
  statements with a script.  Certain functions are legal before
  declarations, but this depends upon certain hidden aspects of
  declarations which are not obvious to the user.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  real    x
  int     ii=32
  int     y {min=0, max=14}
  char    z="abc" {enum="abc|def|ghi", mode="q"}
  
  bool    isotest {YES, mode="ql",
              prompt="Do you want to test for isotropy?"}
  
  int     ii=1 {min=0,max=10, prompt="Number of images", mode="h"}
  file    infile="testfile" {filetype="r"}
  struct  line {length=80, mode="h"}
  
  real    array[10]
  int     iarray[15]=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 {min=0, max=100}
  int     jarray[15] { 5(0), 5(2), 5(4), min=0, max=400}
  char    carray[5]= 5("Junk")
  bool    flags[4,-3:3] = 28(NO) {mode="h", prompt="Value set"}
  file    inp_files[3]= "fil1.inp", "fil2.inp", "fil3.inp"
  
  int     karray[3]=1     # (note second and third elements are undefined)
  struct  *list="inputfile.list" {mode="q"}
  int     *ilist="infile.inp" {mode="h", min=0, max=100}
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <div class="highlight-default-notranslate"><pre>
  Options are only permitted for parameters, not local variables.
  The filetype options are recognized but are not implemented internally.
  </pre></div>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  parameters, procedure
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'SYNTAX' 'ELEMENTS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

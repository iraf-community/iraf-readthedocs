.. _hedit:

hedit: Header editor
====================

**Package: imutil**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  hedit images fields value
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_images">
  <dt><b>images</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='images' Line='images' -->
  <dd>Template specifying the images to be edited.
  </dd>
  </dl>
  <dl id="l_fields">
  <dt><b>fields</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fields' Line='fields' -->
  <dd>Template specifying the fields to be edited in each image.  The template is
  expanded independently for each image against the set of all fields in the
  image header.
  </dd>
  </dl>
  <dl id="l_value">
  <dt><b>value</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='value' Line='value' -->
  <dd>Either a string constant or a general expression (if the first character is
  a left parenthesis) to be evaluated to compute the new value of each field.
  A single expression is used for all fields.  The special value <span style="font-family: monospace;">"."</span> causes the
  value of each field to be printed rather than edited.
  </dd>
  </dl>
  <dl id="l_add">
  <dt><b>add = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='add' Line='add = no' -->
  <dd>Change the operation of the editor from update to add new field. If the
  field already exists it is edited.  If this option is selected the field
  list may name only a single field. The add switch takes precedence
  over the addonly and delete switches.
  </dd>
  </dl>
  <dl id="l_addonly">
  <dt><b>addonly = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='addonly' Line='addonly = no' -->
  <dd>Change the operation of the editor from update to add a new field. If the
  field already exists it is not changed.  If this option is selected the field
  list may name only a single field. The addonly switch takes precedence over
  the delete switch.
  </dd>
  </dl>
  <dl id="l_delete">
  <dt><b>delete = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='delete' Line='delete = no' -->
  <dd>Change the operation of the editor from update to delete field.
  The listed fields are deleted from each image.
  </dd>
  </dl>
  <dl id="l_verify">
  <dt><b>verify = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verify' Line='verify = yes' -->
  <dd>Interactively verify all operations which modify the image database.
  The editor will describe the operation to be performed, prompting with the
  new value of the parameter in the case of a field edit.  Type carriage
  return or <span style="font-family: monospace;">"yes"</span> to complete the operation, or enter a new value explicitly
  as a string.  Respond with <span style="font-family: monospace;">"no"</span> if you do not wish to change the value of
  the parameter.
  </dd>
  </dl>
  <dl id="l_show">
  <dt><b>show = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='show' Line='show = yes' -->
  <dd>Print a record of each operation which modifies the database upon the standard
  output.  Old values are given as well as new values, making it possible to
  undo an edit operation.
  </dd>
  </dl>
  <dl id="l_update">
  <dt><b>update = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='update' Line='update = yes' -->
  <dd>Enable updating of the image database.  If updating is disabled the edit
  operations are performed in memory but image headers will not be updated
  on disk.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  1. Basic Usage
  </p>
  <p>
      The most basic functions of the image header editor are modification and
  inspection of the fields of an image header.  Both the <span style="font-family: monospace;">"standard"</span> and
  <span style="font-family: monospace;">"user"</span> fields may be edited in the same fashion, although not all standard
  fields are writable.  For example, to change the value of the standard field
  <span style="font-family: monospace;">"title"</span> of the image <span style="font-family: monospace;">"m74"</span> to <span style="font-family: monospace;">"sky flat"</span> we would enter the following command.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit m74 title "sky flat"
  </pre></div>
  <p>
  If <i>verify</i> mode is selected the editor will print the old value of the
  field and query with the new value, allowing some other value to be entered
  instead, e.g.:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit m74 title "sky flat"
  m74,i_title ("old title" -&gt; "sky flat"):
  </pre></div>
  <p>
  To accept the new value shown to the right of the arrow, type carriage
  return or <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"y"</span> followed by carriage return.  To continue without
  changing the value of the field in question enter <span style="font-family: monospace;">"no"</span> or <span style="font-family: monospace;">"n"</span> followed by
  carriage return.  To enter some other value merely type in the new value.
  If the new value is one of the reserved strings, e.g., <span style="font-family: monospace;">"yes"</span> or <span style="font-family: monospace;">"no"</span>,
  enter it preceded by a backslash.  If verification is enabled you will
  also be asked if you want to update the header, once all header fields
  have been edited.  This is your last chance to change your mind before
  the header is modified on disk.  If you respond negatively the image header
  will not be updated, and editing will continue with the next image.
  If the response is <span style="font-family: monospace;">"q"</span> the editor will exit entirely.
  </p>
  <p>
  To conveniently print the value of the field <span style="font-family: monospace;">"title"</span> without modifying the
  image header, we repeat the command with the special value <span style="font-family: monospace;">"."</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit m74 title .
  </pre></div>
  <p>
  To print (or edit) the values of all header fields a field template may be
  given.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit m74 * .
  </pre></div>
  <p>
  To print (or edit) the values of only a few fields the field template may
  be given as a list.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit m74 w0,wpc .
  </pre></div>
  <p>
  To print the value of one or more fields in a set of images, an image template
  may be given.  Both image templates and field templates may be given if
  desired.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit n1.* exp .
  </pre></div>
  <p>
  Abbreviations are not permitted for field names, i.e., the given template
  must match the full field name.  Currently, field name matches are case
  insensitive since image headers are often converted to and from FITS headers,
  which are case insensitive.
  </p>
  <p>
  2. Advanced Usage
  </p>
  <p>
      The header editor is capable of performing global edits on entire image
  databases wherein the new value of each field is computed automatically at
  edit time and may depend on the values of other fields in the image header.
  Editing may be performed in either batch or interactive mode.  An audit trail
  may be maintained (via the <i>show</i> switch and i/o redirection), permitting
  restoration of the database in the event of an error.  Trial runs may be made
  with updating disabled, before committing to an actual edit which modifies the
  database.
  </p>
  <p>
  The major editing functions of the <i>hedit</i> task are the following:
  </p>
  <div class="highlight-default-notranslate"><pre>
  update          modify the value of a field or fields
  addonly         add a new field
  add             add a new field or modify an old one
  delete          delete a set of fields
  </pre></div>
  <p>
  In addition, <i>hedit</i> may be used merely to inspect the values of the header
  fields, without modification of the image database.
  </p>
  <p>
  2.1 Standard header fields
  </p>
  <p>
      The header editor may be used to access both the standard image header
  fields and any user or application defined fields.  The standard header fields
  currently defined are shown below.  There is no guarantee that the names and/or
  usage of these fields will not change in the future.
  </p>
  <div class="highlight-default-notranslate"><pre>
  i_ctime         int             create time
  i_history       string          history comments
  i_limtime       int             time when min,max last updated
  i_maxpixval     real            maximum pixel value
  i_minpixval     real            minimum pixel value
  i_mtime         int             time of last modify
  i_naxis         int             number of axes (dimensionality)
  i_naxis[1-7]    int             length of each axis
  i_pixfile       string          pathname of pixel storage file
  i_pixtype       int             pixel datatype code
  i_title         string          title string
  </pre></div>
  <p>
  The standard header field names have an <span style="font-family: monospace;">"i_"</span> prefix to reduce the possibility
  of a name collision with a user field name, and to distinguish the two classes
  of parameters in templates.  The prefix may be omitted provided the simple
  name is unique.
  </p>
  <p>
  2.2 Field name template
  </p>
  <p>
      The form of the field name list or template parameter <i>fields</i> is
  equivalent to that of a filename template except that <span style="font-family: monospace;">"@listfile"</span> is not
  supported, and of course the template is expanded upon the field name list
  of an image, rather than upon a directory.  Abbreviations are not permitted
  in field names and case is not significant.  Case is ignored in this context
  due to the present internal storage format for the user parameters (FITS),
  which also limits the length of a user field name to 8 characters.
  </p>
  <p>
  2.3 Value expression
  </p>
  <p>
      The <i>value</i> parameter is a string type parameter.  If the first
  character in the string is a left parenthesis the string is interpreted as
  an algebraic expression wherein the operands may be constants, image header
  variables (field names), special variables (defined below), or calls to
  intrinsic functions.  The expression syntax is equivalent to that used in
  the CL and SPP languages.  If the value string is not parenthesized it is
  assumed to be a string constant.  The <i>value</i> string will often contain
  blanks, quotes, parenthesis, etc., and hence must usually be quoted to avoid
  interpretation by the CL rather than by the header editor.
  </p>
  <p>
  For example, the command
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit m74 title "title // ';ss'"
  </pre></div>
  <p>
  would change the title to the literal string constant <span style="font-family: monospace;">"title // ';ss'"</span>,
  whereas the command
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit m74 title "(title // ';ss')"
  </pre></div>
  <p>
  would concatenate the string <span style="font-family: monospace;">";ss"</span> to the old title string.  We require
  parenthesis for expression evaluation to avoid the need to doubly quote
  simple string constant values, which would be even more confusing for the
  user than using parenthesis.  For example, if expressions did not have to
  be parenthesized, the first example in the basic usage section would have
  to be entered as shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit m74 title '"sky flat"'        # invalid command
  </pre></div>
  <p>
  Expression evaluation for <i>hedit</i>, <i>hselect</i>, and similar tasks
  is carried out internally by the FMTIO library routine <b>evexpr</b>.
  For completeness minimal documentation is given here, but the documentation
  for <i>evexpr</i> itself should be consulted if additional detail is required
  or if problems occur.
  </p>
  <p>
  2.3.1 operators
  </p>
  <p>
      The following operators are recognized in value expressions.  With the
  exception of the operators <span style="font-family: monospace;">"?"</span>, <span style="font-family: monospace;">"?="</span>, and <span style="font-family: monospace;">"@"</span>, the operator set is equivalent
  to that available in the CL and SPP languages.
  </p>
  <div class="highlight-default-notranslate"><pre>
  +  -  *  /              arithmetic operators
  **                      exponentiation
  //                      string concatenation
  !  -                    boolean not, unary negation
  &lt;  &lt;= &gt;  &gt;=             order comparison (works for strings)
  == != &amp;&amp; ||             equals, not equals, and, or
  ?=                      string equals pattern
  ? :                     conditional expression
  @                       reference a variable
  </pre></div>
  <p>
  The operators <span style="font-family: monospace;">"=="</span>, <span style="font-family: monospace;">"&amp;&amp;"</span>, and <span style="font-family: monospace;">"||"</span> may be abbreviated as <span style="font-family: monospace;">"="</span>, <span style="font-family: monospace;">"&amp;"</span>, and <span style="font-family: monospace;">"|"</span>
  if desired.  The ?= operator performs pattern matching upon strings.
  For example, the boolean expression shown below will be true whenever the
  field <span style="font-family: monospace;">"title"</span> contains the substring <span style="font-family: monospace;">"sky"</span>.
  </p>
  <p>
  	(title ?= '*sky*')
  </p>
  <p>
  The conditional expression operator <span style="font-family: monospace;">'?'</span>, which is patterned after a similar
  operator in C, is used to make IF ELSE like decisions within an expression.
  The syntax is as follows:
  </p>
  <p>
  	&lt;bool_expr&gt; <span style="font-family: monospace;">'?'</span> &lt;true_expr&gt; <span style="font-family: monospace;">':'</span> &lt;false_expr&gt; 
  </p>
  <p>
  e.g., the expression
  </p>
  <p>
  	((a &gt; b) ? 1 : 0)
  </p>
  <p>
  has the value 1 if A is greater than B, and 0 otherwise.  The datatypes
  of the true and false expressions need not be the same, unlike a compiled
  language.  Note that if the parenthesis are omitted ambiguous forms of
  the expression are possible, e.g.:
  </p>
  <p>
  	(a &gt; b) ? 1 : a + 1
  </p>
  <p>
  could be interpreted either as
  </p>
  <p>
  	((a &gt; b) ? 1 : a) + 1
  or as
  	(a &gt; b) ? 1 : (a + 1)
  </p>
  <p>
  If the parenthesis are omitted the latter interpretation is assumed.
  </p>
  <p>
  The operator @ must be used to dereference variables that have names with
  funny (non-alphanumeric) characters in them, forcing the variable name to
  be given as a string constant.  For example, the value of the expression
  </p>
  <p>
  	@<span style="font-family: monospace;">"co-flag"</span>
  </p>
  <p>
  is the value of the variable <span style="font-family: monospace;">"co-flag"</span>.  If the variable were referenced
  directly by name the <span style="font-family: monospace;">"-"</span> would be interpreted as the subtraction operator,
  causing an unknown variable reference (e.g., to <span style="font-family: monospace;">"co"</span>).
  The operand following the @ may be any string valued expression.
  The @ operator is right associative, hence the construct <span style="font-family: monospace;">"@@param"</span> is the
  value of the parameter named by the value of the parameter <span style="font-family: monospace;">"param"</span>.
  </p>
  <p>
  An expression may contain operands of datatypes bool, int, real, and string.
  Mixed mode expressions are permitted with automatic type coercion.  Most type
  coercions from boolean or string to other datatypes are illegal.  The boolean
  constants <span style="font-family: monospace;">"yes"</span> and <span style="font-family: monospace;">"no"</span> are predefined and may be used within expressions.
  </p>
  <p>
  2.3.2 intrinsic functions
  </p>
  <p>
      A number of standard intrinsic functions are recognized within expressions.
  The set of functions currently supported is shown below.
  </p>
  <div class="highlight-default-notranslate"><pre>
  abs     acos    asin    atan    atan2   bool    cos
  exp     int     log     log10   max     min     mod
  nint    real    sin     sqrt    str     tan
  </pre></div>
  <p>
  The trigonometric functions operate in units of degrees rather than radians.
  The <i>min</i> and <i>max</i> functions may have any number of arguments up
  to a maximum of sixteen or so (configurable).  The arguments need not all
  be of the same datatype.
  </p>
  <p>
  A function call may take either of the following forms:
  </p>
  <div class="highlight-default-notranslate"><pre>
          &lt;identifier&gt; <span style="font-family: monospace;">'('</span> arglist <span style="font-family: monospace;">')'</span>
  or
          &lt;string_expr&gt; <span style="font-family: monospace;">'('</span> arglist <span style="font-family: monospace;">')'</span>
  </pre></div>
  <p>
  The first form is the conventional form found in all programming languages.
  The second permits the generation of function names by string valued
  expressions and might be useful on rare occasions.
  </p>
  <p>
  2.3.3 special operands
  </p>
  <p>
      As noted earlier, expression operands may be constants, variables (header
  fields), function calls, or references to any of the special variables.
  The following special variables are recognized within expressions:
  </p>
  <div class="highlight-default-notranslate"><pre>
  .               A string constant, used to flag printing
  $               The value of the "current field"
  $F              The name of the "current field"
  $I              The name of the "current image"
  $T              The current clock time (an integer value)
  </pre></div>
  <p>
  These builtin variables are especially useful for constructing context
  dependent expressions.  For example, the value of a field may be incremented
  by 100 by assigning it the value <span style="font-family: monospace;">"$ + 100"</span>.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Globally edit the database <span style="font-family: monospace;">"n1"</span>, setting the value of the string parameter
  <span style="font-family: monospace;">"obs"</span> to <span style="font-family: monospace;">"sky"</span> if <span style="font-family: monospace;">"s-flag"</span> is 1, to <span style="font-family: monospace;">"obj"</span> otherwise.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit n1.* obs '(@"s-flag" == 1 ? "sky" : "obj")'
  </pre></div>
  <p>
  2. Globally edit the same database, replacing the value of the parameter
  <span style="font-family: monospace;">"variance"</span> by the square root of the original value.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit n1.* var '(sqrt(var))'
  </pre></div>
  <p>
  3. Replace the values of the fields A and B by the absolute value of the
  original value:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; hedit n1.* a,b '(abs($))'
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The internal storage format is currently FITS card image, hence field names
  are limited to 8 characters with no case sensitivity.  String values are
  limited to 63 characters.  There is an upper limit on the number of fields
  in a header but it is quite large - assume it is 1024 or so.  Global operations
  on databases are currently quite slow because the individual records (image
  headers) are stored in separate files.
  </p>
  <p>
  A task is needed which would take the audit trail produced by the <i>show</i>
  option and use it to undo an edit.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  hselect, imgets, imheader
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

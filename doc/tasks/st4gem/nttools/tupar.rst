.. _tupar:

tupar: Edit table header keywords.
==================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tupar table
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task is an interactive editor that allows the user to modify table
  header parameters.
  Prompts are written to STDERR rather than
  STDOUT so that STDOUT can be redirected to a file.
  If STDERR is redirected, no prompts will appear.
  Prompting is also turned off if the input is redirected from a file.
  </p>
  <p>
  The table to be edited is copied to a temporary table
  in the same directory as the original table
  (or in tmp$ if the first copy attempt fails),
  and the changes are made to that copy.
  When you exit 'tupar',
  the copy is renamed back to the name of the original table.
  If you quit rather than exit,
  then the copy is deleted, so the original table will remain unchanged.
  </p>
  <p>
  The prompt <span style="font-family: monospace;">":"</span> is used by the task when it is waiting for user input.
  At this prompt the user can enter any editor command.
  The <span style="font-family: monospace;">"e"</span> command (or end of file, e.g. Control-Z) will exit the editor.
  The following commands are available:  e, q, g, p, d, r, k, t, l.
  These commands are interpreted as exit, quit (without saving changes),
  get, put, delete, replace, change keyword name, type, and list respectively.
  Each of these commands is described in detail below:
  </p>
  <p>
  The exit command, specified by <span style="font-family: monospace;">"e"</span> or end of file,
  will close the file--saving all changes,
  and open the next file if more than one file was specified
  for the 'table' input parameter.
  </p>
  <p>
  The quit command is similar to exit except that changes that were made
  to the header parameters will not take effect,
  unless 'inplace = yes'.
  If changes were made to the table header
  you will be prompted for confirmation
  unless the command was given followed by <span style="font-family: monospace;">"!"</span>;
  for example, <span style="font-family: monospace;">"q!"</span> or <span style="font-family: monospace;">"quit!"</span>.
  </p>
  <p>
  The type command, specified by <span style="font-family: monospace;">"t"</span>, and the list command,
  specified by <span style="font-family: monospace;">"l"</span>,
  both display header parameters---one header per line of output.
  The difference between the two commands is that list will show the parameter
  number and type will not.
  Entering the command <span style="font-family: monospace;">"t"</span> or <span style="font-family: monospace;">"l"</span> will produce
  a listing of all header parameters.
  Optionally, an integer may follow
  the command indicating that only a particular parameter is to be displayed.
  Two integers following the command indicate a range of parameters.
  If a number is specified that is beyond the range of valid headers,
  an error message will be displayed.
  The output consists of the name of the header parameter,
  its data type (indicated by a single letter,
  <span style="font-family: monospace;">"r"</span> for real, <span style="font-family: monospace;">"b"</span> for boolean, <span style="font-family: monospace;">"i"</span> for integer, or <span style="font-family: monospace;">"d"</span> for double),
  and its current value.
  If the keyword has an associated comment,
  the comment will be displayed following the value.
  The following are examples of valid syntax for listing header parameters:
  </p>
  <div class="highlight-default-notranslate"><pre>
  t
  l
  t 3
  l 300 310
  </pre></div>
  <p>
  The get command, indicated by <span style="font-family: monospace;">"g"</span>, will look for a specific keyword and
  display its current value.
  Optionally, the data type can be specified
  using the letter <span style="font-family: monospace;">"r"</span> for real, <span style="font-family: monospace;">"i"</span> for integer, <span style="font-family: monospace;">"d"</span> for double, or
  <span style="font-family: monospace;">"b"</span> for boolean.
  If no data type is specified, then the type is assumed to be text.
  If the data type is specified,
  the type immediately follows the <span style="font-family: monospace;">"g"</span> command;
  for example, typing the command <span style="font-family: monospace;">"gd X"</span> will get the value 
  contained in the header keyword <span style="font-family: monospace;">"X"</span> and display it as a double-precision
  real value.
  If <span style="font-family: monospace;">"X"</span> does not exist, no output will be produced.
  If the keyword has an associated comment,
  the get command displays the comment following the value;
  a text string value will be enclosed in quotes
  to distinguish the value from the comment.
  Examples of valid syntax follow:
  </p>
  <div class="highlight-default-notranslate"><pre>
  g history
  gd coeff0
  gi numpts
  </pre></div>
  <p>
  The put command, specified by <span style="font-family: monospace;">"p"</span>, will either replace the value of an
  existing parameter,
  or it will create a new parameter if the specified parameter is not found.
  The <span style="font-family: monospace;">"p"</span> command is followed on the command line by a keyword
  name and the parameter value.
  A comment may optionally follow the value.
  The <span style="font-family: monospace;">"p"</span> command itself should
  be followed by a single letter type specifier, <span style="font-family: monospace;">"i"</span> for integer,
  <span style="font-family: monospace;">"r"</span> for real, <span style="font-family: monospace;">"d"</span> for double, or <span style="font-family: monospace;">"b"</span> for boolean.
  If no type is specified, then the data type is assumed to be text.
  In order to specify a comment with a parameter of type text,
  the parameter value must be enclosed in quotes
  in order to distinguish it from the comment.  (Keyword names
  HISTORY and COMMENT are already comments,
  and further comments cannot be added to them.)
  Examples of valid put command syntax follow:
  </p>
  <div class="highlight-default-notranslate"><pre>
  p comment Created for testing.
  gd coeff0
  pd coeff0 3.141592653589793
  pi ncoeff 7 number of coefficients
  pt fittype chebychev
  pt fittype "chebychev" type of fit that these coefficients represent
  </pre></div>
  <p>
  The replace command, specified by <span style="font-family: monospace;">"r"</span>, works much like the put command
  described above; however, it will prompt the user for confirmation before
  actually changing any values in the table.
  A parameter can be specified by name or by number.
  The <span style="font-family: monospace;">"r"</span> command will not change a keyword name or a data type,
  whereas the <span style="font-family: monospace;">"p"</span> command can.
  After the command is entered,
  the current value of the keyword is displayed and
  the editor waits for a new value to be entered by the user.
  Pressing the return key indicates that no change is to be made.
  Pressing the space bar will blank the current value.
  You will then be prompted for
  confirmation unless the command was issued as <span style="font-family: monospace;">"r!"</span> or the input was
  redirected from a file.
  The default action is given by the 'delete_default' parameter.
  </p>
  <p>
  A range of contiguous parameters can be replaced at one time by giving
  the names or numbers of the first and last parameters to be replaced.
  This can involve a lot of prompting for confirmation,
  especially if several tables are being edited with 'same=yes'.
  In this context, <span style="font-family: monospace;">"contiguous"</span> means adjacent in the table header.
  Thus, when replacing a range by name,
  it is not the parameters that fall alphabetically within the limits
  that will be replaced
  but rather the parameters that are numerically within the limits.
  When editing a list of tables with 'same=yes',
  the same replacement string is used for each table.
  Thus it is essential that there be the same number of parameters in
  the range in all tables being edited.
  When no replacement value is given (i.e., just hit the return key),
  then the current keyword value is not changed,
  either in the first table or in subsequent tables.
  </p>
  <p>
  Sample replace commands follow:
  </p>
  <div class="highlight-default-notranslate"><pre>
  r coeff0
  r 17
  r! 17
  r junk dummy
  r junk 12
  r 5 12
  </pre></div>
  <p>
  The delete command, specified by <span style="font-family: monospace;">"d"</span>, will delete a header parameter by
  either name or number.
  The editor prompts for confirmation of delete,
  unless input is redirected from a file.
  The default action is given by the 'delete_default' parameter.
  If you do not want to be prompted for confirmation, enter the command as <span style="font-family: monospace;">"d!"</span>.
  If you want to delete a history or comment record other than the first,
  you can identify the parameter by number rather than name.
  </p>
  <p>
  A range of contiguous parameters can be deleted at one time by giving
  the names or numbers of the first and last parameters to be deleted.
  As with replacing a range of parameters,
  a contiguous block of parameters will be deleted.
  </p>
  <p>
  Examples of valid delete commands follow:
  </p>
  <div class="highlight-default-notranslate"><pre>
  d testflag
  d 17
  d! 17
  d junk dummy
  d junk 12
  d 5 12
  </pre></div>
  <p>
  The <span style="font-family: monospace;">"k"</span> command changes the name of a keyword
  without changing the data type, value, or comment.
  Give the current and new keyword names following the <span style="font-family: monospace;">"k"</span>.
  Note that keywords are limited to eight characters.
  If the name of a COMMENT or HISTORY keyword is changed,
  only the first occurrence of that keyword will be changed.
  </p>
  <p>
  Examples of valid change keyword commands follow:
  </p>
  <div class="highlight-default-notranslate"><pre>
  k history comment
  k dummy test
  </pre></div>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file name template]' -->
  <dd>A table name or list of table names whose header parameters are to be edited.
  Unless 'inplace = yes',
  each table will be copied (one at a time) to a temporary table,
  and changes are made to the copy until you exit.
  This can cause problems if there is not enough disk space for the copy;
  however, the 'inplace' parameter can
  be set to <span style="font-family: monospace;">"yes"</span> so that the tables are opened in-place.
  </dd>
  </dl>
  <dl>
  <dt><b>(same = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(same = no) [boolean]' -->
  <dd>Apply the same set of instructions to all tables?  
  This is only relevant when more than one table is being edited.
  If 'same = no', instructions are processed separately for each table,
  with the <span style="font-family: monospace;">"e"</span> command used to end processing of a table and open
  the next table.
  If 'same = yes', the same instruction set is applied to all tables.
  These instructions will be read from STDIN (which may be redirected)
  and saved in a local buffer while the first table in the list is open.
  For each subsequent table the instructions will be read from the local buffer.
  Caution is advised when deleting or replacing parameters, especially by
  number; remember that prompting for confirmation is turned off if the
  input is redirected or if the instruction is given as <span style="font-family: monospace;">"d!"</span> or <span style="font-family: monospace;">"r!"</span>.
  If 'same = yes' and you quit (rather than exit) from editing the first table,
  the behavior of the task depends on whether changes were made before quitting.
  If changes were made then the task aborts immediately
  without opening the other tables in the input list.
  If no change was made then the other tables are processed.
  The idea is to allow <span style="font-family: monospace;">"g"</span>, <span style="font-family: monospace;">"t"</span>, and <span style="font-family: monospace;">"l"</span> commands
  and still be able to quit rather than exit,
  since nothing was modified.
  If changes were made but you quit,
  that's interpreted as trying to recover from an error,
  so we don't change the first table and we don't continue.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>Display the name of each table when it is opened?  
  If STDOUT is redirected
  then these file names will be written to STDERR as well as to STDOUT.
  </dd>
  </dl>
  <dl>
  <dt><b>(readonly = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(readonly = no) [boolean]' -->
  <dd>Prevent changes from being made to the file?  
  If 'readonly = yes', then the
  table is opened with read only access.  This is useful for viewing the
  contents of the table while at the same time preventing changes from
  being made to it.  (Only the <span style="font-family: monospace;">"g"</span>, <span style="font-family: monospace;">"t"</span>, and <span style="font-family: monospace;">"l"</span> commands are useful in
  read only mode).
  </dd>
  </dl>
  <dl>
  <dt><b>(inplace = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inplace = no) [boolean]' -->
  <dd>Edit the original table in-place?
  By default a copy of the original table is made,
  either in the same directory or in tmp$.
  This makes it possible to quit without saving changes.
  If the table is large, however,
  it may be undesirable to make a copy,
  so the 'inplace' parameter gives you the option
  of editing the original table.
  In this case, however, it will not be possible to quit without saving changes.
  </dd>
  </dl>
  <dl>
  <dt><b>(quit_default = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(quit_default = no) [boolean]' -->
  <dd>The value of this parameter is the default response to the prompt
  for confirmation if you give the quit command.
  </dd>
  </dl>
  <dl>
  <dt><b>(delete_default = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(delete_default = yes) [boolean]' -->
  <dd>The value of this parameter is the default response to the prompt
  for confirmation for the delete and replace commands.
  </dd>
  </dl>
  <dl id="l_go_ahead">
  <dt><b>go_ahead [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='go_ahead' Line='go_ahead [boolean]' -->
  <dd>The user does not set this explicitly.
  It is the parameter which is actually gotten in response to a prompt.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. This example reads all history records from all tables in the default
  directory and writes them to 'history.lis'.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tupar *.tab same=yes verbose=no readonly=yes &gt;history.lis
          (The task writes a ":" prompt and waits for input.)
  :g history
  :q
  tt&gt;
  </pre></div>
  <p>
  2. This example illustrates the use of each of the commands when editing
  parameters in one table.  This kind of interactive use of the task
  would not be appropriate when operating on a list of tables unless
  the 'same' parameter is set to <span style="font-family: monospace;">"no"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tupar junk
          (The task writes the table name and a ":" prompt and waits for input.)
  junk.lis
  :g garvage
          (The keyword was not found, so nothing was displayed.)
  :g garbage
  GARBAGE = 3.1416926535
  :pd garbage 3.1415926535
  :p comment yet another comment
  :t
  GARBAGE  d 3.1415926535
  COMMENT  t This is the first comment.
  PI       t 3.1415926535  not an accurate value
  COMMENT  t yet another comment
  :l 3 999
   3 PI       t '3.1415926535'  not an accurate value
   4 COMMENT  t yet another comment
  :g pi
  PI = '3.1415926535'  not an accurate value
  :gd pi
  PI = 3.1415926535  not an accurate value
  :pd pi 3.14159265358979323846 a more accurate value
  :l
   1 GARBAGE  d 3.1415926535
   2 COMMENT  t This is the first comment.
   3 PI       d 3.141592653589793  a more accurate value
   4 COMMENT  t yet another comment
  :d garbage
  The following parameter is to be deleted:
  GARBAGE  d 3.1415926535
     ...   OK to delete ? (yes):                  (user hits return)
  :d comment
  The following parameter is to be deleted:
  COMMENT  t This is the first comment.
     ...   OK to delete ? (yes): n                (user types n)
  :l 4
  parameter out of range; max is 3
  :d 3
  The following parameter is to be deleted:
  COMMENT  t yet another comment
     ...   OK to delete ? (yes):                  (user hits return)
  :t
  COMMENT  t This is the first comment.
  PI       d 3.141592653589793  a more accurate value
  :r 1
  keyword COMMENT, type t; give replacement value:
  This is the first comment.                      (TUPAR writes this &amp; waits)
  this is a comment                               (this line entered by user)
  Current parameter and its replacement are:
  COMMENT  t This is the first comment.
  COMMENT  t this is a comment
     ...   OK to replace ? (yes): n               (user types n)
  no action taken
  :q
  tt&gt;
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Phil Hodge.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  tprint, tdump, tedit
  </p>
  <p>
  Type <span style="font-family: monospace;">"help tables opt=sys"</span> for a higher-level description of the 'tables' 
  package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

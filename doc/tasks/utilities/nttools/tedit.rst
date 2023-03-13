.. _tedit:

tedit: Edit a table.
====================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tedit table
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task is a screen editor for STSDAS tables. You edit a table by
  moving the cursor around the screen with the cursor keys and typing in
  the new value of the table element. The screen scrolls both sideways
  and up and down as you move the cursor, so all elements of the table
  can be reached. Other editing commands are entered on the command
  line. To switch from table editing mode to command line mode, you
  press the EXIT key (usually Control-Z, however, you can change this). After
  performing your command, the editor returns to table editing mode,
  unless the command exits the editor. The most important commands in
  command mode are `help', `exit', and `quit'. The `help' command
  displays all the editing key bindings and the command line commands.
  The `exit' command will get you out of the editor and automatically
  save the edited table. The `quit' command will get you out of the
  editor after asking you whether you want to save the table. By
  default, the editor modifies a copy instead of the original table, so
  if you quit without saving the table, the original table is still
  there without any modifications.
  </p>
  <p>
  If you try to edit a table that does not exist, the editor will ask if
  you want to create the table. If you answer <span style="font-family: monospace;">"no"</span>, the editor will
  exit.  If you answer <span style="font-family: monospace;">"yes"</span>, the editor will ask you for each column
  name, type, unit, and print format. When you have finished entering
  all the columns, press the return key instead of entering another
  column name. The editor will create the table and put you in table
  editing mode.
  </p>
  <p>
  To add a new, blank line to the end of a table, press the return key
  while you are on the last line of the table. You can add blank lines
  anywhere in the table with the `add row' command, which will be
  described later.
  </p>
  <p>
  Some editing commands are entered from the command line in command
  mode. To get to command line mode, press the exit key. This key is
  bound to Control-Z by default. If you enter a blank line, the editor will
  return to table editing mode. Some commands take arguments. They can
  be included when the command is entered, or if they are omitted, the
  editor will prompt you for their values. If the argument has embedded
  blanks, the argument should be enclosed in quotes if passed on the
  command line. No quotes should be used if the argument is entered
  interactively. When the editor interactively prompts you for a command
  argument it will also display a default value for the argument.
  Pressing the return key gets the default value. Some command names are
  two words long, for example, <span style="font-family: monospace;">"add row"</span>. Usually the second word is
  optional and modifies the meaning of the first, for example <span style="font-family: monospace;">"copy
  append"</span>. If the second word is not optional and you omit it, the
  editor will prompt you for it. All command names can be abbreviated to
  one or more letters. If the command name is two words long, both words
  can be abbreviated to one or more letters.
  </p>
  <p>
  The following is a list of the available commands:
  </p>
  <dl id="l_add">
  <dt><b>add column &lt;name&gt; &lt;type&gt; &lt;format&gt; &lt;units&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='add' Line='add column &lt;name&gt; &lt;type&gt; &lt;format&gt; &lt;units&gt;' -->
  <dd>Add a new column to the table with the specified name and data type.
  </dd>
  </dl>
  <dl id="l_add">
  <dt><b>add row &lt;row&gt; &lt;number&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='add' Line='add row &lt;row&gt; &lt;number&gt;' -->
  <dd>Add new, blank rows after row number &lt;row&gt;. The legal range of &lt;row&gt; is
  0 to the number of rows in the table. The number of blank rows to add is 
  &lt;number&gt;.
  </dd>
  </dl>
  <dl id="l_copy">
  <dt><b>copy &lt;first&gt; &lt;last&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='copy' Line='copy &lt;first&gt; &lt;last&gt;' -->
  <dd>Copy the rows between &lt;first&gt; and &lt;last&gt; into the paste buffer. The 
  current contents of the paste buffer are destroyed before the copy.
  The table is not modified by this command. The contents of the paste 
  buffer can be put back into the table by the 'insert' command.
  </dd>
  </dl>
  <dl id="l_copy">
  <dt><b>copy append &lt;first&gt; &lt;last&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='copy' Line='copy append &lt;first&gt; &lt;last&gt;' -->
  <dd>Copy the rows between &lt;first&gt; and &lt;last&gt; into the paste buffer. The 
  current contents of the paste buffer are preserved and the new rows
  are inserted after them.
  </dd>
  </dl>
  <dl id="l_delete">
  <dt><b>delete &lt;first&gt; &lt;last&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='delete' Line='delete &lt;first&gt; &lt;last&gt;' -->
  <dd>Delete the rows between &lt;first&gt; and &lt;last&gt;. The deleted rows are placed
  into the paste buffer and the current contents of the paste buffer are
  destroyed.
  </dd>
  </dl>
  <dl id="l_delete">
  <dt><b>delete append &lt;first&gt; &lt;last&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='delete' Line='delete append &lt;first&gt; &lt;last&gt;' -->
  <dd>Delete the rows between &lt;first&gt; and &lt;last&gt;. The deleted rows are appended 
  to the paste buffer.
  </dd>
  </dl>
  <dl id="l_exit">
  <dt><b>exit</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='exit' Line='exit' -->
  <dd>Exit the table editor, saving any changes made to the table.
  </dd>
  </dl>
  <dl id="l_find">
  <dt><b>find &lt;expression&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='find' Line='find &lt;expression&gt;' -->
  <dd>Find the next row in the table which makes &lt;expression&gt; true and move
  the cursor to that row. The expression has the same syntax as an
  expression in a Fortran if statement.  The variables in the expression
  are column names. For more information on the syntax of the
  expression, read the help for 'tselect'. The direction of the search depends 
  upon previous 'find' commands. By default the search direction is forward;
  however, if a <span style="font-family: monospace;">"find backwards"</span> command has been executed previously, 
  searches will be done in a backwards direction until a <span style="font-family: monospace;">"find forward"</span>
  command is executed.
  </dd>
  </dl>
  <dl id="l_find">
  <dt><b>find forward &lt;expression&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='find' Line='find forward &lt;expression&gt;' -->
  <dd>Find the next row in the table which makes &lt;expression&gt; true and move the
  cursor to that row. The search is done in the forwards direction.
  </dd>
  </dl>
  <dl id="l_find">
  <dt><b>find backwards &lt;expression&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='find' Line='find backwards &lt;expression&gt;' -->
  <dd>Find the next row in the table which makes &lt;expression&gt; true and move the
  cursor to that row. The search is done in the backwards direction.
  </dd>
  </dl>
  <dl id="l_goto">
  <dt><b>goto &lt;row&gt; &lt;column&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='goto' Line='goto &lt;row&gt; &lt;column&gt;' -->
  <dd>Move the cursor to &lt;row&gt; and &lt;column&gt;.
  </dd>
  </dl>
  <dl id="l_help">
  <dt><b>help</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='help' Line='help' -->
  <dd>Display online help information for the table editor. The help includes 
  a brief description of each command line command and the key bindings 
  for table editing commands.
  </dd>
  </dl>
  <dl id="l_insert">
  <dt><b>insert &lt;row&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='insert' Line='insert &lt;row&gt;' -->
  <dd>Insert the contents of the paste buffer after row number &lt;row&gt;. The 
  contents of the paste buffer are not changed.
  </dd>
  </dl>
  <dl id="l_lower">
  <dt><b>lower &lt;column&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='lower' Line='lower &lt;column&gt;' -->
  <dd>Convert &lt;column&gt; to lower case. Only string columns can be converted.
  </dd>
  </dl>
  <dl id="l_next">
  <dt><b>next</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='next' Line='next' -->
  <dd>Repeat the previous find command, using the same expression and search 
  direction that was used with it.
  </dd>
  </dl>
  <dl id="l_next">
  <dt><b>next forward</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='next' Line='next forward' -->
  <dd>Repeat the previous find command, changing the search direction to 
  forwards.
  </dd>
  </dl>
  <dl id="l_next">
  <dt><b>next backwards</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='next' Line='next backwards' -->
  <dd>Repeat the previous find command, changing the search direction to 
  backwards.
  </dd>
  </dl>
  <dl id="l_quit">
  <dt><b>quit</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='quit' Line='quit' -->
  <dd>Exit the table editor. If the table has been changed, the table editor 
  will ask you whether to save it before exiting.
  </dd>
  </dl>
  <dl id="l_set">
  <dt><b>set &lt;column&gt; &lt;expression&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='set' Line='set &lt;column&gt; &lt;expression&gt;' -->
  <dd>Set a column equal to an expression. If the column is a string column,
  the expression must be a constant. If the column is numeric, the
  expression can either be a constant or a Fortran-like expression. For
  the exact syntax of the expression, see the help file for tcalc.
  </dd>
  </dl>
  <dl id="l_substitute">
  <dt><b>substitute &lt;column&gt; &lt;target&gt; &lt;replacement&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='substitute' Line='substitute &lt;column&gt; &lt;target&gt; &lt;replacement&gt;' -->
  <dd>Search for and replace text patterns in a column.  The syntax for the
  target and replacement pattern strings largely follows that used in
  the substitute command by the Unix text editors `ed' and `ex'. The
  pattern consists of a sequence of ordinary characters, which match
  themselves, and meta-characters, which match a set of characters. A
  meta-character can be matched as if it were an ordinary character by
  preceding it with the escape character, <span style="font-family: monospace;">`\'</span>. For example, the escape
  character itself is indicated in a pattern by `\\'. The meta-characters
  which can be used in the target pattern are:
  <div class="highlight-default-notranslate"><pre>
  beginning of string     ^       end of string           $
  white space             #       escape character        \
  ignore case             {       end ignore case         }
  begin character class   [       end character class     ]
  not, in char class      ^       range, in char class    -
  one character           ?       zero or more occurrences *
  begin tagged string     \(      end tagged string       \)
  </pre></div>
  A set of characters is indicated in the target string by the character
  class construct. For example, punctuation could be indicated by
  `[,;.!]'.  A range of characters contiguous in the underlying
  character set can be abbreviated by the range construct. For example,
  `[a-z]' matches any lower case character. The complement of a
  character set is indicated by making <span style="font-family: monospace;">`^'</span> the first character in a
  class. For example, `[^0-9]' matches any non-digit. Repetition of a
  character or character class is indicated by the following it with the
  <span style="font-family: monospace;">`*'</span> meta-character. Thus, zero or more occurrences of a lower case
  character is indicated by `[a-z]*'. The tagged string meta-characters
  have no effect on the match, they only serve to identify portions of
  the matched string for the replacement pattern. The meta-characters
  which are used in the replacement pattern are the following:
  <div class="highlight-default-notranslate"><pre>
  entire string           &amp;       tagged string           \n
  capitalize              \u      upper case              \U
  lower case              \L      end case conversion     \e \E
  </pre></div>
  The ditto meta-character, <span style="font-family: monospace;">`&amp;`</span>, indicates that the entire portion of the
  string that was matched by the target pattern. The tag meta-character
  indicates that the n-th tagged string.  For example, `\1' indicates
  the first tagged string and `\2' the second. The remaining
  meta-characters affect the case of the output string. The
  capitalization meta-character only affects the immediately following
  meta-character, but the upper and lower case meta-characters must be
  turned off explicitly with `\e' or `\E'.
  </dd>
  </dl>
  <dl id="l_upper">
  <dt><b>upper &lt;column&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='upper' Line='upper &lt;column&gt;' -->
  <dd>Convert &lt;column&gt; to upper case. Only string columns can be converted.
  </dd>
  </dl>
  <p>
  The bindings to the table editing keys are read from the edcap file.
  This is the same file which is used to define the key bindings for the
  parameter editor and history editor. The edcap file defines key
  bindings which resemble those of commonly used text editors. Three
  edcap files are distributed with IRAF. They define key bindings which
  resemble EDT, Emacs, and vi. These edcap files are located in the 'dev$'
  directory and have the extension '.ed'. The appropriate file is chosen
  according to the value of the environment variable 'EDITOR'. If you
  want to customize the key bindings of the table editor, copy the
  appropriate edcap file from the 'dev$' directory to your 'home$' directory
  and edit the second column of the file. The table editor searches your
  home directory first for the edcap file and if it does not find it,
  then it searches the 'dev$' directory.
  </p>
  <p>
  The table editor also uses the termcap file to determine the screen
  size and the escape sequences used to modify the screen. There are
  entries in the termcap file for almost all terminal types. The proper
  entry is selected according to the environment variable 'TERMINAL'. To
  change your terminal type or the screen size, use the IRAF 'stty'
  command. 
  </p>
  <p>
  The 'tread' task can also be used to view a file in readonly mode.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [string]' -->
  <dd>The name of the table to be edited. The editor checks for the
  existence of the table and its access mode before editing. If the 
  table does not exist, the editor will ask whether you want to create
  a new table. If you do not have write access to a table you can only
  edit it by setting 'rdonly=yes'.
  </dd>
  </dl>
  <dl>
  <dt><b>(columns = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(columns = "") [string]' -->
  <dd>The names of the columns to be edited.
  A null or blank string means edit all columns.
  A column template consists of a list of either
  column names or column patterns containing the usual pattern matching
  meta-characters.  The names or patterns are separated by commas or
  white space.  The list can be placed in a file and the name of the
  file preceded by an <span style="font-family: monospace;">"@"</span> given in its place.
  If the first character in the column template is a bang (!),
  all columns NOT named will be displayed.
  The 'tlcol' task (with the 'nlist' parameter set to 1)  may be used to generate 
  a list of
  column names so there is no question about spelling.  This list may be
  edited to rearrange or delete the names, and then the list
  file is given preceded by an <span style="font-family: monospace;">'@'</span> sign, for example:
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tedit junk columns=@colnames.lis
  </pre></div>
  </dd>
  </dl>
  <dl>
  <dt><b>(silent = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(silent = no) [boolean]' -->
  <dd>Turn off the bell indicating warning messages? 
  </dd>
  </dl>
  <dl>
  <dt><b>(rdonly = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(rdonly = no) [boolean]' -->
  <dd>View a table without modifying it?  This parameter prevents you from 
  executing
  any command that would modify the file.
  </dd>
  </dl>
  <dl>
  <dt><b>(inplace = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(inplace = no) [boolean]' -->
  <dd>Replace existing table?  If 'rdonly' is
  set to <span style="font-family: monospace;">"yes"</span> the table is always edited in place.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Make a copy of the table 'm12b.tab' (if it exists) and edit the copy. 
  If the table does not exist
  then a temporary table is created, and you will be prompted for the
  name of the first column to be created.  In either case, if you
  exit (rather than quitting) the temporary table will be renamed to
  'm12b.tab'.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tedit m12b
  </pre></div>
  <p>
  2. Display the columns 'SHARP' and 'ROUND' in an existing table. Rows may 
  be added or deleted, and columns may be added.  
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tedit m12b columns="SHARP,ROUND"
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Bernie Simon.
  </p>
  </section>
  <section id="s_see_also_">
  <h3>See also </h3>
  <p>
  tread, tprint, tselect, stty
  </p>
  <p>
  Type <span style="font-family: monospace;">"help tables opt=sys"</span> for a description of the 'tables' package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO '  -->
  

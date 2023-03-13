.. _tread:

tread: Browse through a table.
==============================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tread table
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The 'tread' task is a read-only version of 'tedit', the screen editor for STSDAS
  tables.  'tread' lets you view a table by moving the cursor around the
  screen with the cursor keys.  The screen scrolls both sideways and up
  and down as you move the cursor, so all elements of the table can be
  reached. Other editing commands are entered on the command line. To
  switch from table editing mode to command line mode, you press the
  exit key (generally bound to Control-Z, though this can be changed).  
  When your 
  command is completed, the editor returns to table editing mode, unless
  the command exits the editor. The most important commands in command
  mode are `help' and `exit'. The `help' command displays all the
  editing key bindings and the command line commands. The `exit' command
  will get you out of the editor.
  </p>
  <p>
  Some editing commands are entered from the command line in command
  mode. To get to command line mode, press the exit key (Control-Z). 
  If you enter a 
  blank line, the editor will
  return to table editing mode. Some commands take arguments. They can
  be included when the command is entered, or if they are omitted, the
  editor will prompt you for their values. If the argument has embedded
  blanks, the argument should be enclosed in quotes if passed on the
  command line. No quotes should be used if the argument is entered
  interactively. When the editor interactively prompts you for a command
  argument it will also display a default value for the argument.
  Pressing the return key gets the default value. Some command names are 
  two
  words long, for example, <span style="font-family: monospace;">"find forward"</span>. Usually the second word is
  optional and modifies the meaning of the first.  If the second word is
  not optional and you omit it, the editor will prompt you for it. All
  command names can be abbreviated to one or more letters. If the
  command name is two words long, both words can be abbreviated to one
  or more letters.
  </p>
  <p>
  The following commands are used by 'tread':
  </p>
  <dl id="l_exit">
  <dt><b>exit</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='exit' Line='exit' -->
  <dd>Exit the table editor.
  </dd>
  </dl>
  <dl id="l_find">
  <dt><b>find &lt;expression&gt;</b></dt>
  <!-- Sec='DESCRIPTION' Level=0 Label='find' Line='find &lt;expression&gt;' -->
  <dd>Find the next row in the table which makes &lt;expression&gt; true and move
  the cursor to that row. The expression has the same syntax as an
  expression in a Fortran if statement.  The variables in the expression
  are column names. For more information on the syntax of the
  expression, read the help for the 'tselect' task. The direction of the search 
  depends 
  upon previous find commands. By default the search direction is forward;
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
  <dd>Exit the table editor.
  </dd>
  </dl>
  <p>
  The bindings to the table editing keys are read from the edcap file.
  This is the file that defines key bindings for the
  parameter editor and history editor. The edcap file defines key
  bindings that resemble those of commonly used text editors. Three
  edcap files are distributed with IRAF. They define key bindings which
  resemble EDT, Emacs, and vi. These edcap files are located in the 'dev$'
  directory and have the extension '.ed'. The appropriate file is chosen
  according to the value of the environment variable 'EDITOR'. If you
  want to customize the key bindings of the table editor, copy the
  appropriate edcap file from the 'dev$' directory to your 'home$' directory
  and edit the second column. The table editor searches your
  home directory first for the edcap file and if it does not find it,
  searches the 'dev$' directory.
  </p>
  <p>
  The table editor also uses the termcap file to determine the screen
  size and the escape sequences used to modify the screen. There are
  entries in the termcap file for almost all terminal types. The proper
  entry is selected according to the environment variable terminal. To
  change your terminal type or the screen size, use the IRAF 'stty'
  command. 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [string]' -->
  <dd>Name of the table to be edited. The editor checks for the
  existence of the table and its access mode before editing. The table
  must exist in order to edit it with 'tread'.
  </dd>
  </dl>
  <dl>
  <dt><b>(columns = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(columns = "") [string]' -->
  <dd>Names of the columns to be edited.
  A null or blank string means edit all columns.
  A column template consists of a list of either
  column names or column patterns containing the usual pattern matching
  meta-characters.  The names or patterns are separated by commas or
  white space.  The list can be placed in a file and the name of the
  file preceded by an <span style="font-family: monospace;">"@"</span> character.
  If the first character in the column template is a bang (!),
  all columns NOT named will be displayed.
  The 'tlcol' task (with the 'nlist' parameter set to 1) may be used to generate a 
  list of
  column names so there is no question about spelling.  This list may be
  edited to rearrange (or delete) the names, and then pass the list to this task 
  by preceding the its file name with an <span style="font-family: monospace;">"@"</span>, for example,  
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
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Display only the columns 'SHARP' and 'ROUND' from the table 'm12b.tab':
   
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tread m12b columns="SHARP,ROUND"
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
  tedit, tprint, tselect, stty
  </p>
  <p>
  Type <span style="font-family: monospace;">"help tables opt=sys"</span> for a description of the 'tables' package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO '  -->
  

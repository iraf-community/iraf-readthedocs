.. _thedit:

thedit: Edit or print table header keywords.
============================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  thedit table keywords value
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This table header editor can be used to add, delete, edit,
  or just print the values of table header keywords.
  </p>
  <p>
  Although this task was based on 'hedit',
  there are significant differences.
  The 'add', 'verify', and 'update' parameters of 'hedit'
  are not included in 'thedit'.
  If a specified keyword does not already exist,
  then it will be added
  (equivalent to add=yes in 'hedit').
  If a keyword does not exist,
  and the value expression is <span style="font-family: monospace;">"."</span>,
  a warning will be printed
  ('hedit' is silent in this case).
  </p>
  <p>
  Such parameters as the number of rows or columns in the table
  are stored differently in FITS, STSDAS, and text tables.
  The following special <span style="font-family: monospace;">"keywords"</span> can be used
  to reference such information regardless of table type.
  These may be used in the 'keywords' parameter when value=<span style="font-family: monospace;">"."</span>,
  or they can be used in the 'value' parameter as part of an expression.
  </p>
  <div class="highlight-default-notranslate"><pre>
  i_table   string    table name (may include extension ID)
  i_file    string    name of the file containing the table
  i_ctime   string    file modification (or creation) time
  i_nrows   int       number of rows in the table
  i_ncols   int       number of columns in the table
  i_npar    int       number of keywords in the table header
  i_type    string    table type
  </pre></div>
  <p>
  'thedit' supports two of the special operands
  that are available in 'hedit':  <span style="font-family: monospace;">"$"</span> and <span style="font-family: monospace;">"$I"</span>.
  When 'value' is an expression,
  <span style="font-family: monospace;">"$"</span> gives the value of the current keyword.
  <span style="font-family: monospace;">"$I"</span> is equivalent to <span style="font-family: monospace;">"i_table"</span>,
  the name of the current table.
  <span style="font-family: monospace;">"$I"</span> can be used as a keyword or as part of an expression.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file name template]' -->
  <dd>A list of tables for which keywords are to be edited or printed.
  If 'value' is <span style="font-family: monospace;">"."</span>, each table will be opened read-only;
  otherwise, each table will be opened read-write.
  </dd>
  </dl>
  <dl id="l_keywords">
  <dt><b>keywords [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='keywords' Line='keywords [string]' -->
  <dd>One or more keywords, separated by commas and/or blanks,
  which are to be added, modified, or printed.
  If the value expression (see 'value') is not <span style="font-family: monospace;">"."</span>,
  any keyword in 'keywords' that is not already present
  will be added to the header.
  Wildcards are supported; however,
  the <span style="font-family: monospace;">"@filename"</span> syntax is not supported.
  Do not use wildcard or other special characters
  if a keyword is to be added to the header.
  </dd>
  </dl>
  <dl id="l_value">
  <dt><b>value = <span style="font-family: monospace;">"."</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='value' Line='value = "." [string]' -->
  <dd>This is the value to be assigned to each keyword in 'keywords'.
  The special value <span style="font-family: monospace;">"."</span> means that
  the keywords should be printed rather than edited,
  and in this case the table will be opened read-only.
  If 'value' is not equal to <span style="font-family: monospace;">"."</span>,
  the same value will be assigned to all the keywords
  matching the template 'keywords'.
  In order to set a keyword value to <span style="font-family: monospace;">"."</span> or <span style="font-family: monospace;">","</span>,
  specify the value as <span style="font-family: monospace;">"\."</span> or <span style="font-family: monospace;">"\,"</span> respectively.
  (Note that if given on the command line,
  the quotes are required in this case.)  Requiring <span style="font-family: monospace;">","</span> to be escaped
  was added as protection against accidentally typing <span style="font-family: monospace;">","</span> instead of <span style="font-family: monospace;">"."</span>.
  As with 'hedit',
  a general expression may be given for 'value'
  by enclosing the expression in parentheses.
  The expression may include constants and/or keyword names;
  it will be evaluated and then assigned to each keyword in 'keywords'.
  Note that if delete = yes, then 'value' will be ignored.
  </dd>
  </dl>
  <dl>
  <dt><b>(delete = no) [bool]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(delete = no) [bool]' -->
  <dd>If delete = yes, the specified keywords will be deleted.
  All the keywords listed in 'keywords' will be deleted,
  for each table in 'table'.
  </dd>
  </dl>
  <dl>
  <dt><b>(show = yes) [bool]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(show = yes) [bool]' -->
  <dd>Print a record of each edit operation?
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Display all the header keywords (except blank) in <span style="font-family: monospace;">"example.tab"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thedit example.tab * .
  </pre></div>
  <p>
  2.  Display only the special keywords for <span style="font-family: monospace;">"timetag.fits[events]"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thedit timetag.fits[events] i_* .
  
  timetag.fits[events],i_table = timetag.fits[events]
  timetag.fits[events],i_file = timetag.fits
  timetag.fits[events],i_ctime = "Wed 12:07:58 31-May-2000"
  timetag.fits[events],i_nrows = 337824
  timetag.fits[events],i_ncols = 6
  timetag.fits[events],i_npar = 58
  timetag.fits[events],i_type = "fits, binary"
  </pre></div>
  <p>
  3.  Print all HISTORY keywords in <span style="font-family: monospace;">"example.txt"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thedit example.txt history .
  </pre></div>
  <p>
  4.  Add a new HISTORY keyword to <span style="font-family: monospace;">"example.tab"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thedit example.tab history \
  "('file name is ' // i_file) // '; number of rows = ' // str (i_nrows)"
  </pre></div>
  <p>
  5.  Increment the value of COUNT.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thedit example.tab count "($ + 1)"
  </pre></div>
  <p>
  6.  Delete all HISTORY and COMMENT keywords in <span style="font-family: monospace;">"example.fits[1]"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thedit example.fits history,comment delete+
  </pre></div>
  <p>
  7.  Evaluate a simple expression
  and assign the result to keyword WAVELEN.
  Keywords TCRVL1, TCDLT1, and NELEM
  are assumed to be already present in the header.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thedit example.fits wavelen "(tcrvl1 + tcdlt1 * nelem/2.)"
  </pre></div>
  <p>
  8.  A keyword can be renamed by using a two-step process,
  first creating a new keyword with the old value, and then
  deleting the old keyword.
  Note that while this procedure does copy the value,
  the comment will be lost.
  (The <span style="font-family: monospace;">"k"</span> instruction in 'tupar' can also be used to rename a keyword.)
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thedit example.tab newkey "(oldkey)"
  tt&gt; thedit example.tab oldkey delete+
  </pre></div>
  <p>
  9.  The primary header or an image extension of a FITS file
  can also be opened as a table in order to access the keywords.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thedit o47s01kdm_raw.fits[0] rootname .
  tt&gt; thedit o47s01kdm_flt.fits[1] bunit "COUNTS/S"
  </pre></div>
  <p>
  10.  This could have been a big mistake.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; thedit abc.fits[1] * ,
  
  ERROR: In order to set a keyword value to <span style="font-family: monospace;">','</span> you must use value='\,'
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Expressions are evaluated using EVEXPR,
  which does not support double precision.
  </p>
  <p>
  Header lines with keyword = '        ' cannot be displayed.
  </p>
  <p>
  The 'value' parameter is of type string,
  and 'thedit' interprets the value
  to determine what data type to use
  when writing the value to the table.
  This can fail when a value appears to be a number
  but really should be treated as a string.
  For example, a date and time could be written as <span style="font-family: monospace;">"19940531:11515000"</span>.
  'thedit' would interpret this as hours and minutes (HH:MMss)
  and convert the value to 1994053. + 11515000./60.
  A workaround for this case is to use 'tupar' instead of 'thedit';
  use the <span style="font-family: monospace;">"pt"</span> instruction, meaning put a keyword of type text.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Phil Hodge,
  based on the 'hedit' task.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  hedit, tupar
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

.. _tprint:

tprint: Print tables--both headers and data.
============================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tprint table
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task is similar to the 'tdump' task in that it takes an STSDAS
  table and produces a file in ASCII format;
  however, this task offers more control over the appearance
  of the final product and better prepares it for printing.
  Formatting options are available
  to control the width and length of a page,
  and to produce the output in HTML, TeX or LaTeX format.
  </p>
  <p>
  By default, all rows and columns in the input tables will be printed,
  but the 'rows' and 'columns' parameters can be used
  to limit the range of rows and columns, respectively, that will be used.
  When using the TeX or LaTeX options,
  the number of output columns is limited to 52.
  For the HTML option,
  all the rows and columns that are to be printed
  will be written to one HTML table,
  rather than broken into pages.
  There is no limit to the number of columns in ASCII format;
  however, if the aggregate column width exceeds the page width
  the output will be produced in sections
  with columns kept together on a page--lines will not wrap.
  If different columns for each row are printed on separate pages,
  the row number will appear on each page, if 'showrow = yes'.
  </p>
  <p>
  The output will be printed to the standard output.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file name template]' -->
  <dd>The file names of tables to be printed.
  This parameter will accept a general file name template,
  containing wildcard characters,
  individual file names with each file name separated by a comma,
  or the name of a list file (preceded by the <span style="font-family: monospace;">"@"</span> character)
  containing the file names of all tables to be processed.
  If more than one table is to be processed,
  a blank line will be printed between tables.
  </dd>
  </dl>
  <dl>
  <dt><b>(prparam = no) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(prparam = no) [boolean]' -->
  <dd>Should the header parameters be printed?
  </dd>
  </dl>
  <dl>
  <dt><b>(prdata = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(prdata = yes) [boolean]' -->
  <dd>Should the table data be printed?
  </dd>
  </dl>
  <dl>
  <dt><b>(pwidth = 80) [integer, min=40, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(pwidth = 80) [integer, min=40, max=INDEF]' -->
  <dd>If the output is redirected,
  'pwidth' specifies the width of the output page;
  otherwise, the screen size is taken from the environment variable 'ttyncols'.
  Columns that are too wide to fit within this page size
  (allowing also for the row number) will be truncated.
  This parameter is not used if option = <span style="font-family: monospace;">"html"</span>.
  </dd>
  </dl>
  <dl>
  <dt><b>(plength = 0) [integer, min=0, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(plength = 0) [integer, min=0, max=INDEF]' -->
  <dd>Lines of data per page.
  This is the number of rows from the table to be printed on each page;
  it does not include the line of column names.
  It does, however, include any blank lines inserted in the data
  because the user specified a value for 'lgroup'.
  The default of zero gives no page breaks.
  This parameter is not used if option = <span style="font-family: monospace;">"html"</span>.
  If the 'sp_col' parameter is not null
  or if the 'lgroup' parameter is greater than zero,
  the blank lines between groups are included in the count of lines per page.
  Thus 'lgroup = 50' and 'plength = 51' would be consistent
  and would give the same result as 'lgroup = 0', 'plength = 50'.
  </dd>
  </dl>
  <dl>
  <dt><b>(showrow = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(showrow = yes) [boolean]' -->
  <dd>Print the number of each row?
  If more than one page is needed in order to print all the columns specified,
  then the row numbers will be printed on each page.
  If 'showrow = no' then row numbers are not printed.
  </dd>
  </dl>
  <dl>
  <dt><b>(orig_row = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(orig_row = yes) [boolean]' -->
  <dd>Print row numbers of the underlying table?
  This parameter only has an effect if a row selector expression
  was included with the table name,
  in which case the table appears to have fewer rows
  than are actually present in the underlying table
  (the complete table, including all rows).
  When 'orig_row' is yes, the default,
  the row numbers printed are those in the underlying table;
  when 'orig_row' is no,
  the selected rows are numbered sequentially starting with one,
  as if those were the only rows in the table.
  </dd>
  </dl>
  <dl>
  <dt><b>(showhdr = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(showhdr = yes) [boolean]' -->
  <dd>Print header information?
  The table name, date of last modification,
  and column names are printed only if 'showhdr = yes'.
  If the 'option' parameter (see below) is set to either <span style="font-family: monospace;">"latex"</span> or <span style="font-family: monospace;">"tex"</span>,
  then 'showhdr' will affect the printing of
  the default macro definitions for column separators
  and the end-of-line string as well as the begin-table string
  (i.e., <span style="font-family: monospace;">"\begin{tabular}..."</span> or <span style="font-family: monospace;">"\halign..."</span>).
  </dd>
  </dl>
  <dl>
  <dt><b>(showunits = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(showunits = yes) [boolean]' -->
  <dd>Print the units for each column?  If 'showunits = yes'
  then the column units will be printed on the line below the column names.
  </dd>
  </dl>
  <dl>
  <dt><b>(columns = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(columns = "") [string]' -->
  <dd>The names of the columns to be printed.
  An alternative way to do this
  is to use a column selector with the table name
  (type <span style="font-family: monospace;">"help selectors"</span> for more information).
  A null or blank string means print all columns.
  This parameter is a column template--that is,
  either a list of column names
  or a template that can contain wildcard characters.
  The column names should be separated by commas or white space.
  The list of column names can be placed in a file
  and the name of the file preceded by <span style="font-family: monospace;">"@"</span> passed to 'columns'.
  If the first character in the column template
  is the negation character (either <span style="font-family: monospace;">"~"</span> or <span style="font-family: monospace;">"!"</span>),
  all columns NOT named will be printed.
  If you want to use a list file for this parameter,
  the 'tlcol' task can be used to make the list
  (be sure to set the 'nlist' parameter to 1).
  Using the 'tlcol' task can eliminate potential problems
  caused by incorrect spelling.
  The list produced by 'tlcol' can also be edited to
  rearrange column names (to change the order for printing)
  or to delete unwanted columns.
  </dd>
  </dl>
  <dl>
  <dt><b>(rows = <span style="font-family: monospace;">"-"</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(rows = "-") [string]' -->
  <dd>The range of rows which are to be printed.
  An alternative way to do this
  is to use a row selector with the table name
  (type <span style="font-family: monospace;">"help selectors"</span> for more information).
  This parameter takes a character string
  defining either specific rows to be printed,
  a range of rows, or upper or lower limits on row numbers.
  The default value <span style="font-family: monospace;">"-"</span> means print all rows.
  The first ten rows could be specified as rows=<span style="font-family: monospace;">"1-10"</span> or just rows=<span style="font-family: monospace;">"-10"</span>.
  To print the first ten rows
  and all rows from 900 through the last (inclusive), use rows=<span style="font-family: monospace;">"-10,900-"</span>.
  Setting rows=<span style="font-family: monospace;">"1,3,7,23"</span> will print only those four rows.
  It is not an error to specify rows larger than the largest row number;
  excess row numbers will simply be ignored.
  (For more information type <span style="font-family: monospace;">"help ranges"</span>.)
  </dd>
  </dl>
  <dl>
  <dt><b>(option = <span style="font-family: monospace;">"plain"</span>) [string, allowed values: plain | html | latex | tex]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(option = "plain") [string, allowed values: plain | html | latex | tex]' -->
  <dd>The format in which output will be produced.
  If option = <span style="font-family: monospace;">"plain"</span>, the output will be ordinary ASCII text which may
  be read or printed directly.
  (See also the 'align' parameter, below.)
  If option = <span style="font-family: monospace;">"html"</span>,
  the output will be formatted with HTML tags,
  and the output should be redirected to a file having the extension <span style="font-family: monospace;">".html"</span>.
  If option = <span style="font-family: monospace;">"latex"</span>,
  the output will be formatted for use as input to LaTeX,
  and if option = <span style="font-family: monospace;">"tex"</span>,
  the output will be formatted for use as input to TeX.
  In these two cases the output should be redirected to a file having
  the extension <span style="font-family: monospace;">".tex"</span>.
  Each value in each row will be preceded by a column-separator of the
  form <span style="font-family: monospace;">"\cola"</span> through <span style="font-family: monospace;">"\colz"</span>, <span style="font-family: monospace;">"\colA"</span> through <span style="font-family: monospace;">"\colZ"</span>.
  (Yes, there
  is a limit of 52 columns to be printed on one page.)  If the row number
  is printed (i.e., by using the 'showrow' parameter) it will
  be preceded by the string <span style="font-family: monospace;">"\colzero"</span>; the string <span style="font-family: monospace;">"\cola"</span> always
  precedes the first column from the table.
  The default definitions assign <span style="font-family: monospace;">"\null"</span> to the first of these
  (either <span style="font-family: monospace;">"\colzero"</span> or <span style="font-family: monospace;">"\cola"</span>) and assign <span style="font-family: monospace;">"&amp;"</span> to all the rest.
  Each row may span several physical rows and is terminated by <span style="font-family: monospace;">"\eol"</span>,
  which has the default definition of <span style="font-family: monospace;">"\\"</span> or <span style="font-family: monospace;">"\cr"</span> as appropriate.
  (See also the description of the parameter 'showhdr').
  </dd>
  </dl>
  <dl>
  <dt><b>(align = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(align = yes) [boolean]' -->
  <dd>Increase column width to align with header?  This parameter is only useful
  when option = <span style="font-family: monospace;">"plain"</span>.
  If 'align = no', the print format stored in the table for each column
  will be used without modification.
  This can cause a problem in that some
  column names may be longer that the field width for those columns,
  consequently, the column names and their values will be misaligned
  (this is especially true of subsequent columns).
  The default value 'align = yes' will force the columns to be aligned
  with the column names regardless of the print format.
  Note that you can set 'showhdr = no' but 'align = yes', in which case the
  column names will not be printed, but the columns will be spaced the
  same as if the names were printed.
  </dd>
  </dl>
  <dl>
  <dt><b>(sp_col = <span style="font-family: monospace;">""</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(sp_col = "") [string]' -->
  <dd>This is the name of a column in the table.
  If it is specified (non-null),
  and if the column is found in the input table,
  a blank line will be printed
  whenever the value in this column changes
  from the value in the preceding row
  (or from the preceding element,
  if 'sp_col' contains arrays).
  The equality test is made on formatted
  values in the column so that the user has more control over spacing
  when the data type of 'sp_col' is either real or double.
  The print format may be changed using either the 'tedit' or 'tchcol' tasks.
  Both 'sp_col' and 'lgroup' may be used together,
  which may be useful if the 'sp_col' column does not change very often.
  </dd>
  </dl>
  <dl>
  <dt><b>(lgroup = 0) [integer, min=0, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(lgroup = 0) [integer, min=0, max=INDEF]' -->
  <dd>Print a blank line after each 'lgroup' lines.
  If 'lgroup' is greater than zero,
  a blank line will be printed between each block of 'lgroup' lines.
  These blank lines are included in the count for 'plength' (page length).
  For example, if lgroup = 10 and plength = 55,
  five groups of ten lines will be produced for each page;
  lgroup = 5, plength = 60 will
  give ten groups of five lines per page.
  The count of lines for these groups is reset at the beginning of each page,
  so even if lgroup+1 does not divide into 'plength',
  the first group on each page will have 'lgroup' lines.
  If any column that is being printed contains array elements
  rather than just scalar values,
  grouping by 'lgroup' will be applied to array elements
  rather than to row numbers.
  If option = <span style="font-family: monospace;">"plain"</span>
  and the window width (or 'pwidth' if output is redirected)
  is not large enough for all the columns,
  the spacing can be by row number on some pages
  and element number on other pages,
  depending on which columns fit on those pages
  (i.e. whether the columns contain arrays).
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Print all tables in the default directory.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tprint *.tab
  </pre></div>
  <p>
  2.  Print 'junk.tab', but rearrange the columns.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tlcol junk nlist=1 &gt;colnames.lis
  tt&gt; edit colnames.lis
  (Rearrange the column names and perhaps delete some of them.)
  tt&gt; tprint junk columns=@colnames.lis
  </pre></div>
  <p>
  3.  After using the 'tinfo' task to find that 'big.tab' has 100000 rows,
  print the first five and last five rows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tprint big rows="1-5,99996-"
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
  tdump, ranges
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

.. _tbdump:

tbdump: Print selected columns of a list of tables databases
============================================================

**Package: ptools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tbdump tables columns expr
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_tables">
  <dt><b>tables</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='tables' Line='tables' -->
  <dd>The name of the APPHOT/DAOPHOT table database(s) to be dumped.
  </dd>
  </dl>
  <dl id="l_columns">
  <dt><b>columns</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='columns' Line='columns' -->
  <dd>The template specifying the names of the columns to be dumped.
  A null or blank string means
  dump all columns.  A column template consists of a list
  of either column names or column patterns containing the usual pattern matching
  meta-characters.  The names or patterns are separated by commas or white space.
  Column names must be spelled in full but may be upper or lower case.
  The columns list can be placed in a file and the name of the file preceded
  by an <span style="font-family: monospace;">'@'</span> character given in place of the column template.
  If the first non-white character in the column template
  is the negation character <span style="font-family: monospace;">'~'</span>, the output will contain those columns
  NOT named in the remainder of the column template.
  </dd>
  </dl>
  <dl id="l_expr">
  <dt><b>expr</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expr' Line='expr' -->
  <dd>The boolean expression to be evaluated once per record.
  Only the fields in those records for which the boolean expression
  evaluates to yes are printed.
  If <i>expr</i> = <span style="font-family: monospace;">"yes"</span>, the specified columns in all the records are
  printed.
  </dd>
  </dl>
  <dl id="l_datafile">
  <dt><b>datafile = STDOUT</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datafile' Line='datafile = STDOUT' -->
  <dd>If <i>Datafile</i> is not null (<span style="font-family: monospace;">""</span>) then the table data will be written
  to an output file with this name. By default the table data is written
  on the standard output.
  <i>Datafile</i> will not be created if the table is empty.
  </dd>
  </dl>
  <dl id="l_cdfile">
  <dt><b>cdfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cdfile' Line='cdfile = ""' -->
  <dd>If <i>Cdfile</i> is not null (<span style="font-family: monospace;">""</span>) then the column definitions will be written
  to an output file with this name.
  The column definitions consist of the column name, data type (R, D, I, B,
  or C), print format, and units.
  </dd>
  </dl>
  <dl id="l_pfile">
  <dt><b>pfile = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pfile' Line='pfile = ""' -->
  <dd>If <i>Pfile</i> is not null (<span style="font-family: monospace;">""</span>) then the header parameters will be written
  to an output file with this name.
  <i>Pfile</i> will not be created if there are no header parameters.
  </dd>
  </dl>
  <dl id="l_rows">
  <dt><b>rows = <span style="font-family: monospace;">"-"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='rows' Line='rows = "-"' -->
  <dd><i>Rows</i> is a string which may be used to specify ranges of rows which are
  to be dumped.  The default of <span style="font-family: monospace;">"-"</span> means dump all rows.  The first
  ten rows could be specified as <i>rows</i> = <span style="font-family: monospace;">"1-10"</span> or just <i>rows</i> = <span style="font-family: monospace;">"-10"</span>.
  To dump the first ten rows and all rows from 900 through the last,
  use <i>rows</i> = <span style="font-family: monospace;">"-10,900-"</span>.  <i>Rows</i> = <span style="font-family: monospace;">"1,3,7,23"</span> will print only
  those four rows.  It is not an error to specify rows larger than the largest
  row number as they will simply be ignored.
  See the help for RANGES in XTOOLS for further information.
  </dd>
  </dl>
  <dl id="l_pagwidth">
  <dt><b>pagwidth = 158</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='pagwidth' Line='pagwidth = 158' -->
  <dd>The width of the output for printing the table data.  If any of the columns
  to be printed is wider than this an error message will be displayed, and
  the data will not be dumped.  The width of each character column is
  increased by two to include a pair of enclosing quotes.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task converts selected records from an APPHOT/DAOPHOT STSDAS table
  database to ASCII format
  and by default prints the result on the standard output.
  TBDUMP  output does not include row numbers or column names.
  The TABLES package task TPRINT can be used for more readable output.
  </p>
  <p>
  The PTOOLS version of TBDUMP described here is 
  actually a combination of the STSDAS TABLES package tasks TSELECT and TDUMP.
  </p>
  <p>
  The three primary uses for TBDUMP are to format STSDAS tables for input to
  applications
  which expect simple text input, allow editing that would be
  difficult or impossible with the TABLES package TEDIT task, such as
  global substitutions,
  and facilitate copying a table over a network to another computer.
  For the latter two applications the table can be dumped to three separate files
  containing column definitions, header parameters, and table data,
  edited, column data types changed, etc.
  The TABLES package TCREATE can be used to create a new table from the three
  ASCII files produced by TBDUMP.
  By default only the column data is dumped.
  </p>
  <p>
  TBDUMP queries for the columns to be dumped. If <i>columns</i> is null (<span style="font-family: monospace;">""</span>)
  then all the columns are dumped.
  All the rows are dumped by default, but ranges of
  rows may be specified with the <i>rows</i> parameter.
  If the table is wider than will fit on a page,
  the output will consist of more than one line per row of the table,
  but all the columns will be printed before moving on to the next row.
  This is in contrast to TPRINT,
  which prints all rows for those columns that will fit on a page,
  then prints all rows for the next set of columns, etc.
  Character columns with multiple words are printed with enclosing quotes.
  </p>
  <p>
  The TABLES package TLCOL task (with TLCOL.NLIST=1) may be used to generate
  a list of
  column names so there is no question about spelling or case.  This list may
  be edited to rearrange the names and/or delete some, the list
  file preceded by an <span style="font-family: monospace;">'@'</span> and used as the value of the <i>columns</i>
  parameter.
  </p>
  <p>
  The output records are selected on the basis of an input boolean
  expression <i>expr</i> whose variables are the tables column names.
  If after substituting the values associated
  with a particular record into the field name variables the
  expression evaluates
  to yes, that record is included in the output table.
  </p>
  <p>
  The supported
  operators and functions are briefly described below. A detailed description
  of the boolean expression evaluator and its syntax can be found
  in the manual page for the IMAGES package HEDIT task.
  </p>
  <p>
  The following logical operators can be used in the boolean expression. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  equal             ==    not equal               !=
  less than         &lt;     less than or equal      &lt;=
  greater than      &gt;     greater than or equal   &gt;=
  or                ||    and                     &amp;&amp;
  negation          !     pattern match           ?=
  concatenation     //
  </pre></div>
  <p>
  The pattern match character ?=  takes a
  string expression as its first argument and a pattern as its second argument.
  The result is yes if the pattern is contained in the string expression.
  Patterns are strings which may contain pattern matching meta-characters.
  The meta-characters themselves can be matched by preceeding them with the escape
  character.  The meta-characters listed below. 
  </p>
  <div class="highlight-default-notranslate"><pre>
  beginning of string     ^       end of string           $
  one character           ?       zero or more characters *
  white space             #       escape character        \
  ignore case             {       end ignore case         }
  begin character class   [       end character class     ]
  not, in char class      ^       range, in char class    -
  </pre></div>
  <p>
  The expression may also include arithmetic operators and functions.
  The following arithmetic operators and functions are supported.
  </p>
  <div class="highlight-default-notranslate"><pre>
  addition                +               subtraction             -
  multiplication          *               division                /
  negation                -               exponentiation          **
  absolute value          abs(x)          cosine                  cos(x)
  sine                    sin(x)          tangent                 tan(x)
  arc cosine              acos(x)         arc sine                asin(x)
  arc tangent             atan(x)         arc tangent             atan2(x,y)
  exponential             exp(x)          square root             sqrt(x)
  natural log             log(x)          common log              log10(x)
  minimum                 min(x,y)        maximum                 max(x,y)
  convert to integer      int(x)          convert to real         real(x)
  nearest integer         nint(x)         modulo                  mod(x)
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <div class="highlight-default-notranslate"><pre>
  1. Dump the "ID", "MAG" and "MAGERR" columns of the DAOPHOT package NSTAR
  output to the standard output.
  
      pt&gt; tbdump n4147.nst.1 "ID,MAG,MAGERR" yes
  
  2. Dump the "ID", "MAG", and "MAGERR" columns of the above file for records
  which have  "MAG &lt;= 20.0".
  
      pt&gt; tbdump n4147.nst.1 "ID,MAG,MAGERR" "MAG &lt;= 20.0"
  
  3. Dump the "MAG" and "MAGERR" columns of the above file and pipe the
  result to graph.
  
      pt&gt; tbdump n4147.nst.1 "MAG,MAGERR" yes | graph STDIN
  
  4.  Dump all the columns in the first 100 rows of the above file.
  
      pt&gt; tbdump n4147.nst.1 "" yes rows="1-100"
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  tables.tdump,tables.tprint,tables.tlcol,tables.tcreate,ptools.txdump,ptools.pdump
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

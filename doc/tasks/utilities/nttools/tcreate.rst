.. _tcreate:

tcreate: Create a STSDAS table from an ASCII descriptor table.
==============================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tcreate table cdfile datafile
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task reads an ASCII file containing column descriptions for a new table.
  The columns are defined and the table created;
  data are read in from a file specified by
  the 'datafile' parameter
  (a specified number of lines may be skipped when reading in data).
  There may be several lines of data per table row.
  Blanks and tabs are skipped.
  Blank lines and lines beginning with # are ignored.
  In-line comments using # are permitted.
  The lines in the input files may be up to 8195 characters long,
  plus one character for the carriage return.
  The input 'datafile' is read free-format.
  </p>
  <p>
  Undefined values require a place holder in the data file.
  The word INDEF should be used as the place holder
  for undefined (indefinite) numerical values,
  the word <span style="font-family: monospace;">"no"</span> for boolean values,
  and a pair of adjacent quotes (<span style="font-family: monospace;">""</span>) for undefined character strings.
  If a value for a character string contains one or more blanks,
  or the comment character (#),
  then the entire value must be enclosed in quotes, e.g., <span style="font-family: monospace;">"R CrB"</span>.
  </p>
  <p>
  This task can also read a file containing header parameters for the table.
  </p>
  <p>
  If a problem occurs when reading a particular data field,
  the execution continues, and the table entry is marked as undefined.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file name]' -->
  <dd>Output file name for the table created by this task.
  Note that, if 'table' is an existing FITS file,
  the table that is created will be appended
  as a new extension to the end of the file.
  </dd>
  </dl>
  <dl id="l_cdfile">
  <dt><b>cdfile = STDIN [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='cdfile' Line='cdfile = STDIN [file name]' -->
  <dd>The name of the column definition file.
  The column definition file contains one line for each column to be created.
  Each line contains up to four values giving attributes of the particular column.
  Every line must have a column name; optionally, it may have a data type,
  display format, and units.  (Embedded blanks in any of these
  attributes must be enclosed in quotes.)  Adjacent quotes are used as
  place holders and let you skip an attribute while defining the next one.
  Column names and data types are NOT case sensitive.
  Neither the format nor data type may contain embedded blanks.
  Display formats may be of the type used by Fortran or those used by SPP.
  If the format is not defined, a default format will be used.
  The format is not used for internal representation of the data and
  is ignored when reading data---it is used only for display purposes,
  for example, by tasks such as 'tedit', 'tread', and 'tprint'.
  Type <span style="font-family: monospace;">"help ttools opt=sysdoc"</span> for detailed information about print formats.
  Comment lines may be included in this file
  by beginning the line with the comment symbol (#).
  The following data types are recognized by this parameter
  (the default data type is single-precision real):
  <div class="highlight-default-notranslate"><pre>
  r - Single-precision real.
  d - Double-precision real.
  i - Integer.
  s - Short integer.
  b - Boolean.
  ch*n - Character string of maximum length n.
  </pre></div>
  A column of arrays can be created by giving the array length
  in square brackets appended to the data type.
  For example, a data type of r[400] would mean that the column
  contains an array of 400 single-precision real numbers in each row.
  r[20,5,4] would also mean an array of 400 reals,
  but in this case a TDIMi keyword will be written (for column number i)
  that gives the numbers 20, 5 and 4,
  indicating that the array should be regarded as 3-D,
  with 20 elements along the most rapidly varying axis
  and four elements along the least rapidly varying axis.
  Up to seven dimensions may be specified, separated by commas.
  For both of these cases, the data file must contain 400 values
  for that column for each row;
  the values need not all be on the same line of the data file.
  Text tables and column-ordered stsdas tables
  cannot contain arrays; see 'tbltype'.
  If you have an existing table
  with columns similar to those
  in the table you would like to create,
  you can use the 'tlcol' task to generate a file
  which can be edited and used as the input 'cdfile' for 'tcreate'.
  That is, the output of 'tlcol' is exactly the format
  that is expected for 'tcreate.cdfile'.
  The syntax is also the same as
  for column definitions in text tables,
  except for the leading <span style="font-family: monospace;">"#c "</span> in text tables.
  If cdfile = <span style="font-family: monospace;">"STDIN"</span> and the input is not redirected,
  the task prints a prompt asking for input.
  Press Control-Z (or Control-D, i.e. your EOF character)
  to terminate the list of column definitions;
  note that the Control-Z must NOT occur on the same line as the last
  column definition.
  </dd>
  </dl>
  <dl id="l_datafile">
  <dt><b>datafile = <span style="font-family: monospace;">"STDIN"</span> [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='datafile' Line='datafile = "STDIN" [file name]' -->
  <dd>The name of the input ASCII data file.
  The values in the file must be in the order of the columns
  as given in the column-definitions file 'cdfile'.
  Undefined values should have INDEF or <span style="font-family: monospace;">""</span> as place holders
  for numerical or character values, respectively.
  Each row for the table must begin with a new line in 'datafile',
  but there can be multiple lines in 'datafile' for each table row
  (see also 'nlines').
  If all data for a table row have been read from an input line
  but there are additional data on the line,
  or if there is a data type mismatch,
  the following warning will be
  printed:  <span style="font-family: monospace;">"out of synch or extra data in line &lt;number&gt;"</span>.
  Lines in the input data file are limited to 8196 characters,
  including the newline at the end of each line.
  If a longer line is encountered, the task will stop with an error.
  As with 'cdfile',
  if datafile = <span style="font-family: monospace;">"STDIN"</span> and the input is not redirected,
  the task prints a prompt asking for input.
  Enter a carriage return before ending the last line
  and then press Control-Z (or Control-D, i.e. EOF) to close the file.
  </dd>
  </dl>
  <dl>
  <dt><b>(uparfile) [file name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(uparfile) [file name]' -->
  <dd>The name of the input ASCII file of header parameters.
  This file is optional.
  Each line of this file defines one header parameter,
  except that blank lines and lines beginning with # will be ignored.
  Each line should contain three parts:  keyword, datatype, and value;
  an optional comment may be added following the value.
  The keyword is a string (no embedded blanks) of up to eight characters.
  The datatype is a single letter (t, b, i, r, or d) that indicates the type.
  The value is limited to 70 characters.
  If the type is text (t) it may contain more than one word,
  but in that case it must be enclosed in quotes;
  otherwise, the portion of the value following the first word
  will be interpreted as a comment.
  Note that the syntax is not the same as
  for header keywords in text tables.
  The latter uses the much more reasonable <span style="font-family: monospace;">"#k keyword = value comment"</span>.
  The datatype shouldn't need to be specified,
  since keywords are stored in the table as text strings anyway;
  the current syntax has been retained for backward compatibility.
  It is possible, though not recommended, to set uparfile = <span style="font-family: monospace;">"STDIN"</span>.
  The problem is that it is read twice,
  once just to count the number of entries, and once to read the values,
  so you would have to type in the values twice.
  </dd>
  </dl>
  <dl>
  <dt><b>(nskip = 0) [integer, min=0, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nskip = 0) [integer, min=0, max=INDEF]' -->
  <dd>Number of lines to skip at the beginning of the data file.
  The 'tcreate' task will also skip blank lines and lines beginning with #;
  it will therefore not usually be necessary to specify 'nskip',
  as header lines may be commented out by inserting a leading #.
  Note that if 'nskip &gt; 0' then exactly 'nskip' lines will be skipped,
  even if some of them are blank or comment lines.
  </dd>
  </dl>
  <dl>
  <dt><b>(nlines = 0) [integer, min=0, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nlines = 0) [integer, min=0, max=INDEF]' -->
  <dd>The number of lines in the input data file
  corresponding to one row in the output table.
  If 'nlines = 0' (the default) then lines will
  be read from the data file until every column in the row is filled.
  If 'nlines &gt; 0' then exactly this many lines will be read for each row;
  if for some rows the input data are compressed into fewer than this
  many lines, extra dummy lines must be included following the good data.
  Note that comment lines and blank lines are not counted.
  </dd>
  </dl>
  <dl>
  <dt><b>(nrows = 0) [integer, min=0, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nrows = 0) [integer, min=0, max=INDEF]' -->
  <dd>The number of rows to write into the table.
  If this value is zero, then the entire input data file will be read.
  If this value is greater than zero then
  no more than 'nrows' will be written to the table,
  even if the data file contains enough data to fill more than
  'nrows' rows of data.
  For a column-ordered table (see the 'tbltype' parameter),
  'nrows' is the number of rows that will be allocated,
  and the actual number in the data file may be smaller.
  </dd>
  </dl>
  <dl>
  <dt><b>(hist = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(hist = yes) [boolean]' -->
  <dd>Add a history record containing a creation date?
  If 'hist = yes', a header parameter will be written to the table with the
  keyword 'HISTORY' that gives the date and time that 'tcreate' was run.
  This parameter is added after those that were read from the 'uparfile', if any.
  </dd>
  </dl>
  <dl>
  <dt><b>(extrapar = 5) [integer, min=0, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(extrapar = 5) [integer, min=0, max=INDEF]' -->
  <dd>Extra space to be reserved for header-parameter records.
  This is the number of records for header parameters that will be allocated,
  in addition to the number needed to hold the parameters
  specified in the 'uparfile' parameter file.
  The default is five,
  which means that after the table is created
  up to five more parameters may be added
  (e.g., by using the 'tupar' task)
  without the table being rewritten to reallocate space.
  </dd>
  </dl>
  <dl>
  <dt><b>(tbltype = <span style="font-family: monospace;">"default"</span>) [string, allowed values:  default | row | </b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(tbltype = "default") [string, allowed values:  default | row | ' -->
  <dd>column | text]
  Type of table to create.
  The default is row-ordered stsdas format.
  To create a FITS table,
  use tbltype = <span style="font-family: monospace;">"default"</span>
  and specify a table name ('table')
  with filename extension <span style="font-family: monospace;">".fits"</span>, <span style="font-family: monospace;">".fit"</span>, or <span style="font-family: monospace;">".??f"</span>
  (<span style="font-family: monospace;">'?'</span> is any single character).
  </dd>
  </dl>
  <dl>
  <dt><b>(extracol = 0) [integer, min=0, max=INDEF]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(extracol = 0) [integer, min=0, max=INDEF]' -->
  <dd>Extra space to be reserved for columns in the output table.
  This parameter is relevant only for a row-ordered stsdas format table.
  This is in addition to the number required to contain those columns
  described by 'cdfile'.
  One unit of space is taken by each
  single-precision, integer, or boolean column.
  A double-precision column requires two units of allocated space,
  and a character-string column takes one unit of space for each four
  characters, or fraction thereof.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Wait for the user to type in column definitions and data,
  each of which will be terminated by a Control-Z (or Control-D, i.e. EOF).
  The prompts are printed by the 'tcreate' task;
  these are the lines beginning with <span style="font-family: monospace;">"Give column definitions"</span>
  and <span style="font-family: monospace;">"Give table data"</span>.
  The table will have 4 columns and 2 rows.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tcreate test STDIN STDIN
  
  Give column definitions (name, datatype, print format, units)
   ... then newline &amp; EOF to finish.
  name  ch*12
  ra    d     h12.1   hours
  dec   d     h12.0   degrees
  mag   r     f8.2
  ^Z
  
  Give table data ... then newline &amp; EOF to finish.
  nameless      3:18:47   42:24   INDEF
  "SA0 123456"  19:00:06.3  -0:00:01  3.5
  ^Z
  </pre></div>
  <p>
  2. Create a table called <span style="font-family: monospace;">"outfile.tab"</span> using the columns specified
  in <span style="font-family: monospace;">"columns.cd"</span> and the data in <span style="font-family: monospace;">"data.dat"</span>.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tcreate outfile columns.cd data.dat nskip=3
  </pre></div>
  <p>
  <span style="font-family: monospace;">"columns.cd"</span> may contain just the following:
  <br>
  </p>
  <div class="highlight-default-notranslate"><pre>
  STARno I  i5
  X       r      "F6.2"  pixels
  Y       R    F6.2     "pixels"
  MAG R   ""   magnitude
                  SHARP     R
                                  ROUND           r
  STARNAME   ch*15
  </pre></div>
  <p>
  Note the free format of, and embedded tabs in, the column definitions file
  itself.  The format for display of MAG is not specified, but the unit is
  given as magnitude, so adjacent quotes are used to mark the position where
  the display format is expected.
  </p>
  <p>
  The file <span style="font-family: monospace;">"data.dat"</span> may contain (if 'nskip=3', 'nlines=2'):
  <br>
  </p>
  <div class="highlight-default-notranslate"><pre>
  This is a header
        header2
         header3
   1      3.0     4.0
             5.0  6.0     7.0 HD12345
     2 10.0 11.0 12.0 13.0
  14.0 "HD 122"
  3 20.0    21.0        22.0         23.0     24.0  ""
  dummy line
  </pre></div>
  <p>
  Note the tabbed and free format of the data file
  and the specification of the character strings.
  If the character data contain embedded blanks
  then the whole string should be quoted,
  otherwise this is not necessary.
  The final entry is the null character string.
  </p>
  <p>
  3. The following column definitions:
  <br>
  </p>
  <div class="highlight-default-notranslate"><pre>
  STARno   i i6
  X        r f9.2  pixels
  Y        r f9.2  pixels
  MAG      r f9.3
  SHARP    r f9.3
  ROUND    r f9.3
  STARNAME ch*15
  
  could be used with the following data file:
  
       1     7.92     2.64   -3.075    0.436    0.019   XXXXXXXXXXXXXXX
       2    33.89     3.14   -1.162    0.419    0.223
       3     3.68     5.07   -2.454    0.421   -0.123   HD12345
       4    42.70     5.08   -1.285    0.445    0.195   HD 123
  </pre></div>
  <p>
  4. The aperture photometry file from the 'daophot' task
  may have the following data:
  <br>
  </p>
  <div class="highlight-default-notranslate"><pre>
           1     6.95     2.61   99.999   99.999   99.999   99.999 . . .
            464.618  9.71  0.52   9.999    9.999    9.999    9.999 . . .
           2   200.06     2.80   99.999   99.999   99.999   99.999
            465.180  7.79  0.16   9.999    9.999    9.999    9.999
           3   156.25     5.17   14.610   14.537   14.483   14.438
            462.206  7.26  0.37   0.013    0.014    0.015    0.016
  
  and could have the following column-definition file:
  
  STARno  i
  X       r
  Y       r
  MAG1    r
  MAG2    r
  MAG3    r
   .
   .
   .
  MAG15   r
  SKYMOD  r
  SKYSD   r
  </pre></div>
  <p>
  The following could be used as an input file to define header parameters.
  <br>
  </p>
  <div class="highlight-default-notranslate"><pre>
  comment t Created 1987 July 22
  NL      i 2
  NX      i 284
  NY      i 492
  THRESH  r 27.0
  AP1     r 3.0
  PH/ADU  r 20.0
  RNOISE  r 6.50
  BAD     r 300.0
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
  Type <span style="font-family: monospace;">"help ttools opt=sysdoc"</span> for a higher-level description of the 'ttools'
  package.
  See also the files in <span style="font-family: monospace;">"tables$doc/"</span>.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

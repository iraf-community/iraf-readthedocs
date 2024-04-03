.. _tselect:

tselect: Create a new table from selected rows of a table.
==========================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tselect intable outtable expr
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task creates a new table from a subset of rows in an input table.  
  The rows are selected on the basis of a boolean expression whose
  variables are table column names.  If, after substituting the values associated
  with a particular row into the column name variables, the expression evaluates
  to yes, that row is included in the output table.  Boolean operators can be used
  in the expression in either their Fortran or SPP forms.  The following boolean
  operators can be used in the expression: 
  </p>
  <div class="highlight-default-notranslate"><pre>
  equal           .eq.  ==        not equal               .ne.  !=
  less than       .lt.  &lt;         less than or equal      .le.  &lt;=
  greater than    .gt.  &gt;         greater than or equal   .ge.  &gt;=
  or              .or.  ||        and                     .and. &amp;&amp;
  negation        .not. !         pattern match                 ?=
  </pre></div>
  <p>
  The pattern match operator (?=) has no corresponding Fortran form.  It takes a
  string expression as its first argument and a pattern as its second argument.
  The result is <span style="font-family: monospace;">"yes"</span> if the pattern is contained in the string expression.
  Patterns are strings which may contain meta-characters (i.e., wildcard 
  characters used in pattern matching).
  The meta-characters themselves can be matched by preceeding them with the escape
  character (\).
  The meta-characters are: 
  </p>
  <div class="highlight-default-notranslate"><pre>
  beginning of string     ^       end of string           $
  one character           ?       zero or more characters *
  white space             #       escape character        \
  begin ignoring case     {       end ignore case         }
  begin character class   [       end character class     ]
  not, in char class      ^       range, in char class    -
  </pre></div>
  <p>
  The expression may also include arithmetic operators and functions.
  Trigonometric functions use degrees, not radians.  The following arithmetic
  operators and functions can be used in the expression:
  </p>
  <div class="highlight-default-notranslate"><pre>
  addition                +       subtraction             -
  multiplication          *       division                /
  negation                -       exponentiation          **
  concatenation           //      date difference         delta(x,y)
  absolute value          abs(x)  cosine                  cos(x)
  sine                    sin(x)  tangent                 tan(x)
  arc cosine              acos(x) arc sine                asin(x)
  arc tangent             atan(x) arc tangent             atan2(x,y)
  exponential             exp(x)  square root             sqrt(x)
  natural log             log(x)  common log              log10(x)
  modulo                  mod(x)  minimum                 min(x,y)
  row number              row()   maximum                 max(x,y)
  nearest integer         nint(x) convert to integer      int(x)
  convert to real         real(x) convert to string       str(x)
  </pre></div>
  <p>
  The row number function returns an integer value corresponding to the
  row number in the table.  The date difference function returns a real
  value corresponding to the Julian date of the first argument minus the
  Julian date of the second argument; the arguments to the data function
  must be in CDBS date format:  i.e., character strings of the form
  YYYYMMDD:HHMMSSCC.  Any field after the colon is optional.  The last
  date field (CC) is hundreths of a second.
  </p>
  <p>
  One concept in most databases and in STSDAS tables is the concept of a
  null value: a value which indicates that the element is unknown or
  non-existent.  An element in an STSDAS table is null if it is INDEF in a
  numeric column or a zero length string in a text column. Evaluating
  expressions involving nulls requires a three valued logic:  true,
  false, and unknown. Any arithmetic operation on a null element should
  return another null and any comparison operation should return an
  unknown.  Unfortunately, tselect does not implement a true three
  valued logic correctly.  The code instead evaluates any expression
  containing a null element as unknown.  Since tselect only returns rows
  for which the expression is true, all such rows are excluded from the
  output of tselect.  This is usually right, but sometimes wrong, as in
  the case where two comparisons are joined by an or and one evaluates
  to true and the other evaluates to unknown.  It also sometimes returns
  nonintuitive results, as when checking that a column is not equal to
  INDEF.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [file name template]' -->
  <dd>Table(s) from which rows are copied. If input is redirected, this
  parameter will ignored and input will be read from STDIN instead.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [file name template]' -->
  <dd>The new table(s) containing the copied rows.
  If more than one input table was used, then the number of output 
  tables must equal the number of input tables.
  </dd>
  </dl>
  <dl id="l_expr">
  <dt><b>expr [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expr' Line='expr [string]' -->
  <dd>The boolean expression which determines which rows are copied to the new
  table.  The expression may be placed in a list file and the name of the file
  passed to this parameter (preceded by the <span style="font-family: monospace;">"@"</span> character).
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Extract all binary stars brighter than fifth magnitude from a catalog:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tselect starcat.tab binary.tab "binary &amp;&amp; mag &lt;= 5."
  </pre></div>
  <p>
  2. Create a new set of spectra where all measurements with errors greater
  than ten percent are excluded. Use file name editing to create new tables
  with the extension <span style="font-family: monospace;">".tbl"</span> instead of <span style="font-family: monospace;">".tab"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tselect  *.tab  *.%tab%tbl%  "ERROR / (FLUX + .001) &lt; .1"
  </pre></div>
  <p>
  3. Create a table of engineering parameters whose names begin with a digit:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tselect datalog.tab sublog.tab "name ?= '^[0-9]'"
  </pre></div>
  <p>
  4. Return all observations in a schedule for the day of Dec 31, 1989:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tselect schedule.tab week.tab "abs(delta(date,'19891231:12'))&lt;.5"
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Column names must be set off from operators by blanks in the
  expression so that they can be correctly parsed by the expression
  evaluator.  Expressions involving nulls may evaluate incorrectly, see
  above for a discussion.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Bernie Simon.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  tproject, tjoin, tproduct
  </p>
  <p>
  Type <span style="font-family: monospace;">"help tables opt=sys"</span> for a higher-level description of the 'tables' 
  package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

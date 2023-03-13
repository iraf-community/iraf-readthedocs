.. _pconvert:

pconvert: Convert from an apphot/daophot text to tables database
================================================================

**Package: ptools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pconvert textfile table fields
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_textfile">
  <dt><b>textfile</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='textfile' Line='textfile' -->
  <dd>The APPHOT/DAOPHOT text database which is to be converted into an
  APPHOT/DAOPHOT STSDAS table database.
  </dd>
  </dl>
  <dl id="l_table">
  <dt><b>table</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table' -->
  <dd>The name of the output STSDAS table database.
  </dd>
  </dl>
  <dl id="l_fields">
  <dt><b>fields = <span style="font-family: monospace;">"*"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fields' Line='fields = "*"' -->
  <dd>Template defining the fields to be selected from each record. By default
  all the fields are output. Fields
  are specified by using the names defined in the APPHOT/DAOPHOT text
  database by the
  #N entries. Upper or lower case and minimum match abbreviations are
  permissible. For those fields which have multiple entries such as 
  magnitude, an individual value can be referenced by specifying an array
  index, e.g. MAG[2] or several values can be selected by specifying a
  range of elements, e.g. MAG[1-4].
  </dd>
  </dl>
  <dl id="l_expr">
  <dt><b>expr = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expr' Line='expr = yes' -->
  <dd>The boolean expression, evaluated independently for each record,
  which serves as a selection criterion. By default all records are selected.
  </dd>
  </dl>
  <dl id="l_append">
  <dt><b>append = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='append' Line='append = no' -->
  <dd>If append is yes then the converted APPHOT/DAOPHOT text file is appended to an 
  existing output STSDAS table database.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  PCONVERT selects a subset of the fields from each record of an
  APPHOT/DAOPHOT text database and writes these into an STSDAS tabl database.
  The #K keyword parameters in the text database are
  stored as header parameters in the STSDAS table while the selected fields
  are stored in fields (columns) with the names specified by the text
  database #N keywords, units specified
  by the #U keywords, and print format specified by the #F keywords.
  </p>
  <p>
  The output records are selected on the basis of the boolean
  expression <i>expr</i> whose variables are the field (column) names
  specified by the #N keywords in the APPHOT/DAOPHOT text database.
  If after substituting the values associated
  with a particular record into the field name variables the
  expression evaluates to yes, that record is included in the output table.
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
  character.  The meta-characters are described below. 
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
  The boolean expression may also include arithmetic operators and functions.
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
  <p>
  If the append parameter is <span style="font-family: monospace;">"yes"</span> then the converted input text database is
  appended to the specified output table. When appending to a table each of the
  output fields must already exist in the output table.
  </p>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Convert the text output from the DAOPHOT PHOT task in the file n4147.mag.1
  to an STSDAS table, selecting only the fields ID, XCENTER, YCENTER,
  MAG,and MSKY ncessary for input to the DAOPHOT fitting routines.
  Put the output in an STSDAS table named n4147.tmag.1.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; pconvert n4147.mag.1 n4147.tmag.1 "ID,XCENTER,YCENTER,MAG,MSKY"
  </pre></div>
  <p>
  If there were 4 magnitude fields in n4147.mag.1
  then there would be 4 columns in the output table with names of 
  MAG[1], MAG[2], MAG[3] and MAG[4]
  </p>
  <p>
  2. Convert the same file as in example 1. but append the output to
     n4147.tmag.1 and only select records with YCENTER &lt;= 200.0.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; pconvert n4147.mag.1 n4147.tmag.1 "ID,XCENTER,YCENTER,MAG,MSKY" \
      expr="YCENTER &lt; 200.0" append+
  </pre></div>
  <p>
  3. Convert all the records in the NSTAR text database n4147.nst.1 to
     an STSDAS table.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; pconvert n4147.nst.1 n4147.tnst.1 "*"
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Changes in the values of the #K keyword quantities which are permitted by
  the APPHOT/DAOPHOT text database format will be lost in the conversion to
  STSDAS table format which does not permit such changes. For example users
  who have
  set up and run PHOT interactively and changed the values of the parameters
  after writing the first record to the text database will see only the initial
  values of the #K keywords in the STSDAS table headers after conversion.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  images.hedit
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

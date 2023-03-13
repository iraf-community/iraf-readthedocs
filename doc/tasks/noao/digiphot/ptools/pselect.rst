.. _pselect:

pselect: Select records from a list of apphot/daophot databases
===============================================================

**Package: ptools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pselect infiles outfiles expr
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_infiles">
  <dt><b>infiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='infiles' Line='infiles' -->
  <dd>The APPHOT/DAOPHOT databases containing the records from which the
  selection is to be made.
  </dd>
  </dl>
  <dl id="l_outfiles">
  <dt><b>outfiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outfiles' Line='outfiles' -->
  <dd>The output APPHOT/DAOPHOT databases containing the selected records.
  </dd>
  </dl>
  <dl id="l_expr">
  <dt><b>expr</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expr' Line='expr' -->
  <dd>The boolean expression to be evaluated.  The expression
  is evaluated once for each record.  If <i>expr</i> = yes,
  a copy is made of the input file.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  PSELECT selects a subset of the records
  from an APPHOT/DAOPHOT database or a list of databases 
  and writes the new records out to another database or list of
  databases.
  </p>
  <p>
  The output records are selected on the basis of an input boolean
  expression <i>expr</i> whose variables are in the case of text
  databases the field names
  specified by the #N keywords or the parameters specified by the
  #K keywords and in the case of an STSDAS table database the
  column names.
  If after substituting the values associated
  with a particular record into the field name variables the
  expression evaluates
  to yes, that record is included in the output database.
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
  character.  The meta-characters are listed below. 
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
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. Select the records from the output of the APPHOT CENTER task for
  which 100. &lt;= XCENTER &lt;= 200. and 300. &lt;= YCENTER &lt;= 400.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; pselect m92.ctr.3 m92out \
      "XCE &gt;= 100. &amp;&amp; XCE &lt;= 200. &amp;&amp; YCE &gt;= 300. &amp;&amp; YCE &lt;= 400."
  </pre></div>
  <p>
  2. Select the records from the output of the APPHOT PHOT task for which
  the first magnitude is not equal to INDEF. In the case of the
  an STSDAS table database it may be necessary to escape the
  leading square bracket.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; pselect n4147.mag.3 n4147out "MAG[1] != INDEF"
  
                      or
  
  pt&gt; pselect n4147.mag.3 n4147out "MAG\[1] != INDEF"
  </pre></div>
  <p>
  3. Select the records from the output of the DAOPHOT ALLSTAR task
  for which CHI &lt;= 5.0 and MERR &lt;= .10 magnitudes.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; pselect m92b.al.2 m92out "CHI &lt;= 5.0 &amp;&amp; MERR &lt;= 1.0"
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Array valued fields in text databases are not allowed in the expression
  field.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  images.hedit,ptools.tbselect,tables.tselect,ptools.txselect
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

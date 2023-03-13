.. _pdump:

pdump: Print selected fields from a list of daophot databases
=============================================================

**Package: daophot**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  pdump infiles fields expr
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_infiles">
  <dt><b>infiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='infiles' Line='infiles' -->
  <dd>The APPHOT/DAOPHOT databases containing the fields to be dumped.
  </dd>
  </dl>
  <dl id="l_fields">
  <dt><b>fields</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fields' Line='fields' -->
  <dd>A template defining the fields to be dumped from each record.
  In the case of APPHOT/DAOPHOT text databases, the fields are specified by
  keywords defined by the
  #K and #N entries in the database. Upper or lower case and minimum match
  abbreviations are permissible. Some fields such as <span style="font-family: monospace;">"mag"</span> may have
  multiple entries. An individual entry can be referenced by specifying an
  array index, e.g. <span style="font-family: monospace;">"MAG[2]"</span> or several values can be selected by
  specifying a range of elements, e.g. <span style="font-family: monospace;">"MAG[1-3]"</span>.
  In the case of STSDAS table APPHOT/DAOPHOT databases the fields are the
  column names. Names must be spelled in full but upper or lower case is allowed.
  In the case of STSDAS table databases, it may be necessary to escape the
  leading square bracket so that field <span style="font-family: monospace;">"MAG[2]"</span> would be referred to as
  <span style="font-family: monospace;">"MAG\[2]"</span>.  The fields are output in
  the order in which they are specified in the template.
  </dd>
  </dl>
  <dl id="l_expr">
  <dt><b>expr</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='expr' Line='expr' -->
  <dd>The boolean expression to be evaluated once per record.
  Only the fields in those records for which the boolean expression
  evaluates to yes are printed.
  If <i>expr</i> = <span style="font-family: monospace;">"yes"</span>, the specified fields in all the records are
  printed.
  </dd>
  </dl>
  <dl id="l_headers">
  <dt><b>headers = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='headers' Line='headers = no' -->
  <dd>Dump the APPHOT/DAOPHOT database field headers. The selected
  fields are printed on the standard output, preceded by the parameters list,
  if <i>parameters</i> = yes, and the keyword, units,
  and format information.
  </dd>
  </dl>
  <dl id="l_parameters">
  <dt><b>parameters = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='parameters' Line='parameters = yes' -->
  <dd>Print the keyword parameters records on the
  standard output if <i>headers</i> = yes.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  PDUMP selects a subset of fields specified by the <i>fields</i>
  parameter from an APPHOT/DAOPHOT database or a list of databases
  and prints the results on the standard output.
  If <i>headers</i> = no, the output is in simple list format
  with adjacent fields
  separated by whitespace. The fields are printed in the order in
  which they appear in <i>ields</i>. If <i>headers</i> = yes, the
  selected fields are printed on the standard output, preceded by
  the parameter list, if <i>parameters</i> = yes, and the keyword, units,
  and format information.
  Newlines will not be inserted in the output if the input database
  was an APPHOT/DAOPHOT text file, so users should take
  care not specify so many output fields as to exceed the IRAF text file
  line limit of 161 characters.
  Newlines will be inserted if the original database was an
  STSDAS table.
  </p>
  <p>
  PDUMP is a simple CL script which calls TXDUMP if the APPHOT/DAOPHOT
  database was a text file and TBDUMP if it was an STSDAS table.
  Although the parameters of TBDUMP and TXDUMP have been tailored to
  make the two tasks appear as similar as possible each task
  offers some capabilities that the other does not. In some
  situations users may wish to use the individual tasks instead of the
  generic script.
  </p>
  <p>
  The output records are selected on the basis of an input boolean
  expression <i>expr</i> whose variables are the field names
  specified by the #N keywords or the parameters specified by the
  #K keywords in the APPHOT/DAOPHOT text database or the column names
  in an ST tables database.
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
  <p>
  1. Select the fields XCENTER and YCENTER from the output of the APPHOT
  CENTER task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; pdump image.ctr.3 "XCENTER,YCENTER" yes
  </pre></div>
  <p>
  2. Select the fields XCENTER and YCENTER from the output of the APPHOT
  CENTER task for all records with YCENTER &gt; 100.0.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; pdump image.ctr.3 "XCENTER,YCENTER" "YCENTER &gt; 100.0"
  </pre></div>
  <p>
  3. Select the fields ID, XCENTER, YCENTER and the first three magnitudes
  from the output of the APPHOT PHOT task. In the case of STSDAS table
  databases it may be necessary to escape the leading square bracket.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; pdump image.mag.3 "ID,XCEN,YCEN,MAG[1],MAG[2],MAG[3]" yes
  
                 or
  
  pt&gt; pdump image.mag.3 "ID,XCEN,YCEN,MAG\[1],MAG\[2],MAG\[3]" yes
  </pre></div>
  <p>
  4. Select the ID, XCENTER, YCENTER, MSKY and MAG fields from the output
  of the DAOPHOT NSTAR task. Print the headers and parameters as well.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; pdump image.nst.3 "ID,XCENTER,YCENTER,MSKY,MAG"  \
      yes headers+ parameters+
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  Users should not dump more fields than fill a 161 character textline
  as IRAF does not currently fully support longer text lines.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  ptools.txdump,ptools.tbdump,tables.tdump
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

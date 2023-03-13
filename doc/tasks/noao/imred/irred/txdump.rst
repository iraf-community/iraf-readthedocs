.. _txdump:

txdump: Select fields from the center task output text file
===========================================================

**Package: irred**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  txdump textfiles fields expr
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_textfiles">
  <dt><b>textfiles</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='textfiles' Line='textfiles' -->
  <dd>The APPHOT/DAOPHOT text database whose fields from selected records are to
  be printed.
  </dd>
  </dl>
  <dl id="l_fields">
  <dt><b>fields</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fields' Line='fields' -->
  <dd>A template defining the fields to be printed from each selected record.
  The fields are specified by keywords defined in the text database output
  files #K and #N entries. Upper or lower case and minimum match
  abbreviations are permissible. Some fields such as <span style="font-family: monospace;">"mag"</span> may have
  multiple entries. An individual entry can be referenced by specifying an
  array index, e.g. <span style="font-family: monospace;">"mag[2]"</span> or several values can be selected by
  specifying a range of elements, e.g. <span style="font-family: monospace;">"mag[1-3]"</span>. The fields are output in
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
  <dd>Preserve the APPHOT/DAOPHOT text database output format. The selected
  fields are printed on the standard output, preceded by parameters list,
  if <i>parameters</i> = yes, and the keyword, units,
  and format information, exactly as they appear in the text database.
  </dd>
  </dl>
  <dl id="l_parameters">
  <dt><b>parameters = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='parameters' Line='parameters = yes' -->
  <dd>Print the keyword parameters records in APPHOT/DAOPHOT format on the
  standard output if <i>headers</i> = yes.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  <i>TXDUMP</i> selects a subset of fields specified by the <i>fields</i>
  parameter from an APPHOT/DAOPHOT text database or a list of databases by
  evaluating a boolean expression supplied by the user and prints the
  results on the standard output.
  If <i>headers</i> = no, the resultant output is in simple list format
  with all the specified fields in one line of text and adjacent fields
  separated by whitespace. The fields are printed in the order in
  which they appear in <i>expr</i>. If <i>headers</i> = yes, the
  selected fields are printed on the standard output, preceded by
  the parameter list, if <i>parameters</i> = yes, and the keyword, units,
  and format information, exactly as they appear in the text database.
  Newlines will not be inserted in the output so users should take
  care not to exceed the IRAF text file line limit of 161 characters.
  </p>
  <p>
  The output records are selected on the basis of an input boolean
  expression <i>expr</i> whose variables are the field names
  specified by the #N keywords or the parameters specified by the
  #K keywords in the APPHOT/DAOPHOT text database.
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
  1. Print the fields XCENTER and YCENTER from the output of the APPHOT
  CENTER task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; txdump image.ctr.1 XCENTER,YCENTER yes
  </pre></div>
  <p>
  2. Select the fields ID, XCENTER, YCENTER and the first three magnitudes
  MAG{1-3] from the output of the APPHOT PHOT task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; txdump image.mag.2 "ID,XCEN,YCEN,MAG[1-3]" yes
  </pre></div>
  <p>
  3. Print all fields for all records in the above file with a magnitude
  through the first aperture of less than 20.0.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; txdump image.mag.2 * "MAG[1] &lt; 20.0"
  </pre></div>
  <p>
  4. Print the id and all magnitudes for which magnitudes 1 and 2 are &lt; 20.0
  from a file which is the output of the APPHOT PHOT task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; txdump image.mag.3 ID,MAG "MAG[1] &lt; 20.0 &amp;&amp; MAG[2] &lt; 20.0"
  </pre></div>
  <p>
  5. Select the ID, XCENTER, YCENTER, MSKY and MAG fields from the output
     of the DAOPHOT NSTAR task for records where the magnitude is not
     INDEF, while preserving the format of the text database so it
     is suitable for input into a rerun of NSTAR.
  </p>
  <div class="highlight-default-notranslate"><pre>
  pt&gt; txdump image.nst.1 "ID,XCENTER,YCENTER,MSKY,MAG"  \
      "MAG[1] != INDEF" headers+
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  TXDUMP does not allow arrays in the expression field.
  </p>
  <p>
  Users should not dump more fields than fill a 161 character textline
  as IRAF does not currently fully support longer text lines.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  images.hedit,ptools.tbdump,tables.tdump,ptools.pdump
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXAMPLES' 'BUGS' 'SEE ALSO'  -->
  

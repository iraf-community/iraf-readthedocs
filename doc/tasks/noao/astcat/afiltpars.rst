.. _afiltpars:

afiltpars: Default astrometry file filtering parameters
=======================================================

**Package: astcat**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  afiltpars
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_fsort">
  <dt><b>fsort = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fsort' Line='fsort = ""' -->
  <dd>The field or field expression on which to sort the catalog / file records.
  The sort may be numeric or character. Sort fields may be expressed by name,
  e.g. <span style="font-family: monospace;">"mag1"</span> or field number, e.g. <span style="font-family: monospace;">"f3"</span>. Sort expressions must be a combination
  of existing fields, e. g. <span style="font-family: monospace;">"mag2 - mag1"</span> or <span style="font-family: monospace;">"f4 - f3"</span>. By default the records
  are not sorted.
  </dd>
  </dl>
  <dl id="l_freverse">
  <dt><b>freverse = no</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='freverse' Line='freverse = no' -->
  <dd>Sort in descending order ?
  </dd>
  </dl>
  <dl id="l_fexpr">
  <dt><b>fexpr = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fexpr' Line='fexpr = yes' -->
  <dd>The boolean record selection expression. By default all catalog / file records
  are selected, otherwise only records matching the selection expression
  are selected. Selection expressions must be combination of existing fields
  and field expressions, e.g. <span style="font-family: monospace;">"mag1 &lt; 16.0"</span>, or <span style="font-family: monospace;">"(f4 - f3) &lt; 1.5"</span>.
  </dd>
  </dl>
  <dl id="l_fields">
  <dt><b>fields = <span style="font-family: monospace;">"f[*]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fields' Line='fields = "f[*]"' -->
  <dd>The list of output fields and field expressions. By default the sorted and
  selected records are output as is. Output fields may be field names, e.g.
  <span style="font-family: monospace;">"mag1"</span>, field numbers e.g. <span style="font-family: monospace;">"f3"</span>, or field ranges e.g. <span style="font-family: monospace;">"f[1-4]"</span>. Output field
  expressions must be a combination of existing fields, e.g. <span style="font-family: monospace;">"mag2 - mag1"</span>,
  or <span style="font-family: monospace;">"f4 - f3"</span>.
  </dd>
  </dl>
  <dl id="l_fnames">
  <dt><b>fnames = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fnames' Line='fnames = ""' -->
  <dd>The list of new field names separated by commas. By default new fields, e.g.
  fields that are expressions of existing fields are assigned names of the form
  <span style="font-family: monospace;">"f#"</span> where # is the field sequence number. Field names must be valid tokens,
  i.e. they cannot be expressions or contain embedded blanks.
  </dd>
  </dl>
  <dl id="l_fntypes">
  <dt><b>fntypes = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fntypes' Line='fntypes = ""' -->
  <dd>The list of new field types separated by commas. By default new fields are
  assigned type real. Permitted field types are <span style="font-family: monospace;">"s"</span> for string, <span style="font-family: monospace;">"i"</span> for
  integer, <span style="font-family: monospace;">"r"</span> for real, or <span style="font-family: monospace;">"d"</span> for double.
  </dd>
  </dl>
  <dl id="l_fnunits">
  <dt><b>fnunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fnunits' Line='fnunits = ""' -->
  <dd>The list of new field units separated by commas. By default new fields are
  assigned units of INDEF. Units specifications may not contain embedded blanks.
  </dd>
  </dl>
  <dl id="l_fnformats">
  <dt><b>fnformats = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fnformats' Line='fnformats = ""' -->
  <dd>The list of new field formats. By default string, integer, and floating
  point fields are assigned formats of <span style="font-family: monospace;">"%10s"</span>, <span style="font-family: monospace;">"%10d"</span>, and <span style="font-family: monospace;">"%10g"</span> respectively.
  </dd>
  </dl>
  <dl id="l_fosystem">
  <dt><b>fosystem = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fosystem' Line='fosystem = ""' -->
  <dd>The output celestial coordinate system. If fosystem is undefined
  it defaults to the catalog celestial coordinate system. Popular options
  are <span style="font-family: monospace;">"icrs"</span>, <span style="font-family: monospace;">"j2000.0"</span>, <span style="font-family: monospace;">"b1950.0"</span>. The full set of options can be examined
  by typing <span style="font-family: monospace;">"help ccsystems"</span>.
  </dd>
  </dl>
  <dl id="l_fira">
  <dt><b>fira = <span style="font-family: monospace;">"ra"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fira' Line='fira = "ra"' -->
  <dd>The name of the catalog field containing the right ascension / longitude
  of an object. Most users should leave fira set to <span style="font-family: monospace;">"ra"</span>. If the user knows
  the number of the right ascension / longitude field the generic field name
  <span style="font-family: monospace;">"f#"</span>, e.g. <span style="font-family: monospace;">"f1"</span> can be used.
  </dd>
  </dl>
  <dl id="l_fidec">
  <dt><b>fidec = <span style="font-family: monospace;">"dec"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fidec' Line='fidec = "dec"' -->
  <dd>The name of the catalog field containing the declination / latitude
  of an object. Most users should leave fidec set to <span style="font-family: monospace;">"dec"</span>. If the user knows
  the number of the declination / latitude field the generic field name <span style="font-family: monospace;">"f#"</span>,
  e.g. <span style="font-family: monospace;">"f2"</span> can be used.
  </dd>
  </dl>
  <dl id="l_foraunits">
  <dt><b>foraunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='foraunits' Line='foraunits = ""' -->
  <dd>The units of fira. Permitted values are <span style="font-family: monospace;">"hours"</span>, <span style="font-family: monospace;">"degrees"</span>, and <span style="font-family: monospace;">"radians"</span>. If
  foraunits is undefined it defaults to the preferred units of the
  output celestial coordinate system fosystem, e.g. hours for equatorial
  coordinate systems and degrees for ecliptic, galactic, and super-galactic
  coordinate systems.
  </dd>
  </dl>
  <dl id="l_fodecunits">
  <dt><b>fodecunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fodecunits' Line='fodecunits = ""' -->
  <dd>The units of fidec. Permitted values are <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"radians"</span>. If 
  fodecunits is undefined it defaults to the preferred units of the
  output celestial coordinate system fosystem, e.g. degrees for all systems.
  </dd>
  </dl>
  <dl id="l_foraformat">
  <dt><b>foraformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='foraformat' Line='foraformat = ""' -->
  <dd>The format of fira. If undefined foraformat defaults to the equivalent catalog
  format.
  </dd>
  </dl>
  <dl id="l_fodecformat">
  <dt><b>fodecformat = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fodecformat' Line='fodecformat = ""' -->
  <dd>The format of fidec. If undefined fodecformat defaults to the equivalent
  catalog format.
  </dd>
  </dl>
  <dl id="l_fixp">
  <dt><b>fixp = <span style="font-family: monospace;">"xp"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fixp' Line='fixp = "xp"' -->
  <dd>The name of the catalog field containing the predicted x coordinate
  of an object. Most users should leave fixp set to <span style="font-family: monospace;">"xp"</span>. If the user knows
  the number of the predicted x coordinate field the generic field name
  <span style="font-family: monospace;">"f#"</span>, e.g. <span style="font-family: monospace;">"f1"</span> can be used.
  </dd>
  </dl>
  <dl id="l_fiyp">
  <dt><b>fiyp = <span style="font-family: monospace;">"yp"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fiyp' Line='fiyp = "yp"' -->
  <dd>The name of the catalog field containing the predicted y coordinate
  of an object. Most users should leave fiyp set to <span style="font-family: monospace;">"yp"</span>. If the user knows
  the number of the predicted y coordinate field the generic field name
  <span style="font-family: monospace;">"f#"</span>, e.g. <span style="font-family: monospace;">"f2"</span> can be used.
  </dd>
  </dl>
  <dl id="l_fixc">
  <dt><b>fixc = <span style="font-family: monospace;">"xc"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fixc' Line='fixc = "xc"' -->
  <dd>The name of the catalog field containing the centered x coordinate
  of an object. Most users should leave fixc set to <span style="font-family: monospace;">"xc"</span>. If the user knows
  the number of the centered x coordinate field the generic field name
  <span style="font-family: monospace;">"f#"</span>, e.g. <span style="font-family: monospace;">"f1"</span> can be used.
  </dd>
  </dl>
  <dl id="l_fiyc">
  <dt><b>fiyc = <span style="font-family: monospace;">"yc"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fiyc' Line='fiyc = "yc"' -->
  <dd>The name of the catalog field containing the centered y coordinate
  of an object. Most users should leave fiyc set to <span style="font-family: monospace;">"yc"</span>. If the user knows
  the number of the centered y coordinate field the generic field name
  <span style="font-family: monospace;">"f#"</span>, e.g. <span style="font-family: monospace;">"f2"</span> can be used.
  </dd>
  </dl>
  <dl id="l_foxformat">
  <dt><b>foxformat = <span style="font-family: monospace;">"%10.3f"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='foxformat' Line='foxformat = "%10.3f"' -->
  <dd>The format of fixp and fixc. 
  </dd>
  </dl>
  <dl id="l_foyformat">
  <dt><b>foyformat = <span style="font-family: monospace;">"%10.3f"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='foyformat' Line='foyformat = "%10.3f"' -->
  <dd>The format of fiyp and fiyc.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  The catalog / file filtering parameters  are used to filter the results
  of a catalog query before writing the results to disk. Catalog / file filtering
  options include: sorting on a field or field expression,
  selecting and rejecting records by evaluating a boolean expression
  for each record, selecting a subset of the fields for output,
  transforming the coordinates from the catalog / file celestial coordinate
  system to a user specified celestial coordinate system, and computing new
  fields from existing fields.
  </p>
  <p>
  <i>fsort</i> and <i>freverse</i> define the sort field or field expression and
  the sort order. Sort fields may be field names or field numbers, e.g.
  <span style="font-family: monospace;">"mag1"</span> or <span style="font-family: monospace;">"f3"</span>. By default the sort order is ascending.
  </p>
  <p>
  Records are selected or rejected based on the value of the boolean expression
  <i>fexpr</i>. By default all catalog / file records are selected. The boolean 
  selection expression must be function of existing catalog fields, e.g.
  the expression <span style="font-family: monospace;">"mag1 &lt;= 16.0"</span> will select all records for which the mag1
  field is &lt;= 16.0, and the expression <span style="font-family: monospace;">"(f4 - f3) &gt;= 0.0 &amp;&amp; (f4 - f3) &lt;= 1.0"</span>
  will select all records for which the difference between fields 4 and 3
  is &gt;= 0.0 but &lt;= 1.0.
  </p>
  <p>
  The <i>fields</i> parameter defines the list output fields and field 
  expressions. By default all the
  input fields are output. By setting <i>fields</i> appropriately the user
  can select a subset of the input fields for output, rearrange the order
  of the input fields, and compute new fields. For example setting
  fields to <span style="font-family: monospace;">"f[2-5]"</span> selects fields 2 to 5 for output; setting fields
  to <span style="font-family: monospace;">"f[2-3],f5,f4"</span> select fields 2 to 5 but reverses the order of fields
  4 and 5; setting fields to <span style="font-family: monospace;">"f[2-5],f5-f4"</span> selects fields 2 to 5 and
  adds a new field which is the difference between fields 5 and 4.
  </p>
  <p>
  By default new fields are assigned names of the form <span style="font-family: monospace;">"f#"</span> where # is the field
  number, a data type of real, units of INDEF, and formats of %10s, %10d, or
  %10g if they are character, integer, or real respectively. Users can define
  names, data types, units, and formats for the new fields by  setting
  the <i>fnames</i>, <i>fntypes</i>, <i>fnunits</i>, and <i>fnformats</i>
  parameters.
  </p>
  <p>
  The coordinate system, units, or format of the output coordinates may
  be changed by setting one or more of the <i>fosystem</i>, <i>foraunits</i>,
  <i>fodecunits</i>, <i>foraformat</i>, <i>fodecformat</i>. By default the
  filtering code expects the input coordinates to be located in fields
  called <span style="font-family: monospace;">"ra"</span> and <span style="font-family: monospace;">"dec"</span>. If these fields do not have valid names then
  generic field names of the form <span style="font-family: monospace;">"f#"</span> can be substituted.
  </p>
  <p>
  The names and format of any newly computed pixel coordinate fields may
  be specified by setting one or more of the <i>fixp</i>, <i>fiyp</i>,
  <i>fixc</i>, <i>fiyc</i>, <i>foxformat</i>, or <i>foyformat</i> parameters.
  By default the filtering code expects the pixel coordinates to be located
  in fields called <span style="font-family: monospace;">"xp"</span>, <span style="font-family: monospace;">"yp"</span>, <span style="font-family: monospace;">"xc"</span>, and <span style="font-family: monospace;">"yc"</span>. If these fields do not have
  standard names then generic field names of the form <span style="font-family: monospace;">"f#"</span> can be substituted.
  </p>
  </section>
  <section id="s_expressions">
  <h3>Expressions</h3>
  <p>
  The output records are selected on the basis of the input boolean
  expression <i>fexpr</i> whose variables are the field names specified
  in the configuration file or the generic equivalents f#.  If after
  substituting the values associated with a particular record into the
  field name variables the expression evaluates to yes, that record is
  included in the output catalog. Numeric expressions can also be used
  to define the sort expression <i>fsort</i> or to define new fields in
  <i>fields</i>.
  </p>
  <p>
  The supported operators and functions are briefly described below. A detailed
  description of the boolean expression evaluator and its syntax can be found
  in the manual page for the images package hedit task.
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
  The meta-characters themselves can be matched by preceding them with the escape
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
  <section id="s_formats">
  <h3>Formats</h3>
  <p>
  A format  specification has the form <span style="font-family: monospace;">"%w.dCn"</span>, where w is the field
  width, d is the number of decimal places or the number of digits  of
  precision,  C  is  the  format  code,  and  n is radix character for
  format code <span style="font-family: monospace;">"r"</span> only.  The w and d fields are optional.  The  format
  codes C are as follows:
  </p>
  <div class="highlight-default-notranslate"><pre>
  b       boolean (YES or NO)
  c       single character (c or '\c' or '\0nnn')
  d       decimal integer
  e       exponential format (D specifies the precision)
  f       fixed format (D specifies the number of decimal places)
  g       general format (D specifies the precision)
  h       hms format (hh:mm:ss.ss, D = no. decimal places)
  m       minutes, seconds (or hours, minutes) (mm:ss.ss)
  o       octal integer
  rN      convert integer in any radix N
  s       string (D field specifies max chars to print)
  t       advance To column given as field W
  u       unsigned decimal integer
  w       output the number of spaces given by field W
  x       hexadecimal integer
  z       complex format (r,r) (D = precision)
  
  Conventions for w (field width) specification:
  
      W =  n      right justify in field of N characters, blank fill
          -n      left justify in field of N characters, blank fill
          0n      zero fill at left (only if right justified)
  absent, 0       use as much space as needed (D field sets precision)
  
  Escape sequences (e.g. "\n" for newline):
  
  \b      backspace   (not implemented)
       formfeed
  \n      newline (crlf)
  \r      carriage return
  \t      tab
  \"      string delimiter character
  \'      character constant delimiter character
  \\      backslash character
  \nnn    octal value of character
  
  Examples
  
  %s          format a string using as much space as required
  %-10s       left justify a string in a field of 10 characters
  %-10.10s    left justify and truncate a string in a field of 10 characters
  %10s        right justify a string in a field of 10 characters
  %10.10s     right justify and truncate a string in a field of 10 characters
  
  %7.3f       print a real number right justified in floating point format
  %-7.3f      same as above but left justified
  %15.7e      print a real number right justified in exponential format
  %-15.7e     same as above but left justified
  %12.5g      print a real number right justified in general format
  %-12.5g     same as above but left justified
  
  %h          format as nn:nn:nn.n
  %15h        right justify nn:nn:nn.n in field of 15 characters
  %-15h       left justify nn:nn:nn.n in a field of 15 characters
  %12.2h      right justify nn:nn:nn.nn
  %-12.2h     left justify nn:nn:nn.nn
  
  %H          / by 15 and format as nn:nn:nn.n
  %15H        / by 15 and right justify nn:nn:nn.n in field of 15 characters
  %-15H       / by 15 and left justify nn:nn:nn.n in field of 15 characters
  %12.2H      / by 15 and right justify nn:nn:nn.nn
  %-12.2H     / by 15 and left justify nn:nn:nn.nn
  
  \n          insert a newline
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1. List the catalog / file filtering parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; lpar afiltpars
  </pre></div>
  <p>
  2. Edit the catalog / file filtering parameters.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; afiltpars
  </pre></div>
  <p>
  3. Edit the catalog filtering parameters from the agetcat task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epar agetcat
  </pre></div>
  <p>
  4. Save the current afiltpars parameter values in a text file called
  afilt1.par.  Use the saved parameter set in the next call to the agetcat 
  task.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; epar afiltpars
  cl&gt; agetcat ... afiltpars=afilt1.par ...
  </pre></div>
  </section>
  <section id="s_time_requirements">
  <h3>Time requirements</h3>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  agetcat, afiltcat
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'EXPRESSIONS' 'FORMATS' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

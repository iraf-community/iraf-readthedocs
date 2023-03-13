.. _ccget:

ccget: Extract objects from a text file catalog
===============================================

**Package: imcoords**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ccget input output lngcenter latcenter lngwidth latwidth
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_input">
  <dt><b>input</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='input' Line='input' -->
  <dd>The input text file catalog(s). The text file columns must be
  delimited by whitespace and all the input catalogs must have the same format.
  </dd>
  </dl>
  <dl id="l_output">
  <dt><b>output</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='output' Line='output' -->
  <dd>The output catalogs containing the extracted objects. The number of
  output catalogs must be one or equal to the number of input catalogs.
  </dd>
  </dl>
  <dl id="l_lngcenter">
  <dt><b>lngcenter, latcenter</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngcenter' Line='lngcenter, latcenter' -->
  <dd>The center of the field containing the objects to be extracted. Lngcenter and
  latcenter are assumed to be in the coordinate system specified by
  <i>fcsystem</i>, e.g. ra and dec for equatorial systems, galactic longitude and
  latitude for galactic systems, etc. and in the units specified by
  <i>fclngunits</i> and <i>latunits</i>.
  </dd>
  </dl>
  <dl id="l_lngwidth">
  <dt><b>lngwidth, latwidth</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngwidth' Line='lngwidth, latwidth' -->
  <dd>The width of the user specified field in degrees.
  </dd>
  </dl>
  <dl id="l_fcsystem">
  <dt><b>fcsystem = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fcsystem' Line='fcsystem = ""' -->
  <dd>The celestial coordinate system of the field center. If undefined fcsystem
  defaults to the catalog celestial coordinate system specified by
  <i>catsystem</i>. The two systems of
  most interest to users are <span style="font-family: monospace;">"j2000"</span> and <span style="font-family: monospace;">"b1950"</span>. The full set of options is:
  <dl>
  <dt><b>equinox [epoch]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='equinox' Line='equinox [epoch]' -->
  <dd>The equatorial mean place post-IAU 1976 (FK5) system if equinox is a
  Julian epoch, e.g. J2000.0 or 2000.0, or the equatorial mean place
  pre-IAU 1976 system (FK4) if equinox is a Besselian epoch, e.g. B1950.0
  or 1950.0. Julian equinoxes are prefixed by a J or j, Besselian equinoxes
  by a B or b. Equinoxes without the J / j or B / b prefix are treated as
  Besselian epochs if they are &lt; 1984.0, Julian epochs if they are &gt;= 1984.0.
  Epoch is the epoch of the observation and may be a Julian
  epoch, a Besselian epoch, or a Julian date. Julian epochs
  are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to the epoch type of
  equinox if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian date.  If undefined epoch defaults to equinox.
  </dd>
  </dl>
  <dl>
  <dt><b>fk5 [equinox] [epoch]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='fk5' Line='fk5 [equinox] [epoch]' -->
  <dd>The equatorial mean place post-IAU 1976 (FK5) system where equinox is
  a Julian or Besselian epoch e.g. J2000.0  or B1980.0.
  Equinoxes without the J / j or B / b prefix are treated as Julian epochs.
  The default value of equinox is J2000.0.
  Epoch is a Besselian epoch, a Julian epoch, or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Julian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian date.  If undefined epoch defaults to equinox.
  </dd>
  </dl>
  <dl>
  <dt><b>fk4 [equinox] [epoch]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='fk4' Line='fk4 [equinox] [epoch]' -->
  <dd>The equatorial mean place pre-IAU 1976 (FK4) system where equinox is a
  Besselian or Julian epoch e.g. B1950.0  or J2000.0,
  and epoch is the Besselian epoch, the Julian epoch, or the Julian date of the
  observation.
  Equinoxes without the J / j or B / b prefix are treated
  as Besselian epochs. The default value of equinox is B1950.0. Epoch
  is a Besselian epoch, a Julian epoch, or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Besselian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian date.  If undefined epoch defaults to equinox.
  </dd>
  </dl>
  <dl>
  <dt><b>noefk4 [equinox] [epoch]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='noefk4' Line='noefk4 [equinox] [epoch]' -->
  <dd>The equatorial mean place pre-IAU 1976 (FK4) system but without the E-terms
  where equinox is a Besselian or Julian epoch e.g. B1950.0 or J2000.0,
  and epoch is the Besselian epoch, the Julian epoch, or the Julian date of the
  observation.
  Equinoxes without the J / j or B / b prefix are treated
  as Besselian epochs. The default value of equinox is B1950.0.
  Epoch is a Besselian epoch, a Julian epoch, or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Besselian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian day.  If undefined epoch defaults to equinox.
  </dd>
  </dl>
  <dl>
  <dt><b>apparent epoch</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='apparent' Line='apparent epoch' -->
  <dd>The equatorial geocentric apparent place post-IAU 1976 system where
  epoch is the epoch of observation.
  Epoch is a Besselian epoch, a Julian epoch or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Besselian
  epochs if the epoch value &lt; 1984.0, Julian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian date.
  </dd>
  </dl>
  <dl>
  <dt><b>ecliptic epoch</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='ecliptic' Line='ecliptic epoch' -->
  <dd>The ecliptic coordinate system where epoch is the epoch of observation.
  Epoch is a Besselian epoch, a Julian epoch, or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Besselian epochs
  if the epoch values &lt; 1984.0, Julian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian day.
  </dd>
  </dl>
  <dl>
  <dt><b>galactic [epoch]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='galactic' Line='galactic [epoch]' -->
  <dd>The IAU 1958 galactic coordinate system.
  Epoch is a Besselian epoch, a Julian epoch or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Besselian
  epochs if the epoch value &lt; 1984.0, Julian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian date. The default value of epoch is B1950.0.
  </dd>
  </dl>
  <dl>
  <dt><b>supergalactic [epoch]</b></dt>
  <!-- Sec='PARAMETERS' Level=1 Label='supergalactic' Line='supergalactic [epoch]' -->
  <dd>The deVaucouleurs supergalactic coordinate system.
  Epoch is a Besselian epoch, a Julian epoch or a Julian date.
  Julian epochs are prefixed by a J or j, Besselian epochs by a B or b.
  Epochs without the J / j or B / b prefix default to Besselian
  epochs if the epoch value &lt; 1984.0, Julian epochs
  if the epoch value &lt;= 3000.0, otherwise epoch is interpreted as
  a Julian date. The default value of epoch is B1950.0.
  </dd>
  </dl>
  In all the above cases fields in [] are optional with the defaults as
  described. The epoch field for the fk5, galactic, and supergalactic
  coordinate systems is only used if the input coordinates are in the
  equatorial fk4, noefk4, or fk5 systems and proper motions are supplied.
  Since ccget does not currently support proper motions these fields are
  not required.
  </dd>
  </dl>
  <dl id="l_fclngunits">
  <dt><b>fclngunits = <span style="font-family: monospace;">""</span>, fclatunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='fclngunits' Line='fclngunits = "", fclatunits = ""' -->
  <dd>The units of the field center coordinates. The options are <span style="font-family: monospace;">"hours"</span>, <span style="font-family: monospace;">"degrees"</span>,
  and <span style="font-family: monospace;">"radians"</span> for the ra / longitude coordinate and <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"radians"</span>
  for the dec / latitude coordinates. If fclngunits and fclatunits are undefined
  they default to the preferred units for the given system, e.g. <span style="font-family: monospace;">"hours"</span> and
  <span style="font-family: monospace;">"degrees"</span> for equatorial systems and <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"degrees"</span> for ecliptic,
  galactic, and supergalactic systems.
  </dd>
  </dl>
  <dl id="l_colaliases">
  <dt><b>colaliases = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='colaliases' Line='colaliases = ""' -->
  <dd>The list of input catalog column aliases separated by commas. By default the
  catalog columns are <span style="font-family: monospace;">"c1"</span>, <span style="font-family: monospace;">"c2"</span>, <span style="font-family: monospace;">"c10"</span>, etc. If colaliases is defined then
  the aliases are assigned to the columns in order. For example if colaliases
  is <span style="font-family: monospace;">"id,ra,dec,v,bv"</span> then columns c1, c2, c3, c4, c5 will be assigned
  the names id, ra, dec, v, and bv and any remaining columns in the input catalog
  file will be assigned default names beginning with c6.
  </dd>
  </dl>
  <dl id="l_lngcolumn">
  <dt><b>lngcolumn = <span style="font-family: monospace;">"c2"</span>, latcolumn = <span style="font-family: monospace;">"c3"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='lngcolumn' Line='lngcolumn = "c2", latcolumn = "c3"' -->
  <dd>The input catalog columns containing the coordinates of catalog objects.
  </dd>
  </dl>
  <dl id="l_catsystem">
  <dt><b>catsystem = <span style="font-family: monospace;">"j2000"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catsystem' Line='catsystem = "j2000"' -->
  <dd>The celestial coordinate system of the input catalog(s). The two systems of
  most interest to users are <span style="font-family: monospace;">"j2000"</span> and <span style="font-family: monospace;">"b1950"</span>. The full set of options is
  described in the <i>fcsystem</i> parameter section.
  </dd>
  </dl>
  <dl id="l_catlngunits">
  <dt><b>catlngunits = <span style="font-family: monospace;">""</span>, catlatunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='catlngunits' Line='catlngunits = "", catlatunits = ""' -->
  <dd>The units of the catalog coordinates. The options are <span style="font-family: monospace;">"hours"</span>, <span style="font-family: monospace;">"degrees"</span>,
  and <span style="font-family: monospace;">"radians"</span> for the ra / longitude coordinate and <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"radians"</span>
  for the dec / latitude coordinates. If catlngunits and catlatunits are undefined
  they default to the preferred units for the catalog system, e.g. <span style="font-family: monospace;">"hours"</span> and
  <span style="font-family: monospace;">"degrees"</span> for equatorial systems and <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"degrees"</span> for ecliptic,
  galactic, and supergalactic systems.
  </dd>
  </dl>
  <dl id="l_outsystem">
  <dt><b>outsystem = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outsystem' Line='outsystem = ""' -->
  <dd>The celestial coordinate system of the output coordinates. If undefined
  outsystem defaults to the celestial coordinate system of the catalog.
  The two systems of most interest to users are <span style="font-family: monospace;">"j2000"</span> and <span style="font-family: monospace;">"b1950"</span>. The
  full set of options is described under the <i>fcsystem</i> parameter
  section.
  </dd>
  </dl>
  <dl id="l_olngunits">
  <dt><b>olngunits = <span style="font-family: monospace;">""</span>, olatunits = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='olngunits' Line='olngunits = "", olatunits = ""' -->
  <dd>The units of the output coordinates. The options are <span style="font-family: monospace;">"hours"</span>, <span style="font-family: monospace;">"degrees"</span>,
  and <span style="font-family: monospace;">"radians"</span> for the ra / longitude coordinate and <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"radians"</span>
  for the dec / latitude coordinates. If olngunits and olatunits are undefined
  they default to the preferred units for outsystem, e.g. <span style="font-family: monospace;">"hours"</span> and <span style="font-family: monospace;">"degrees"</span> for
  equatorial systems and <span style="font-family: monospace;">"degrees"</span> and <span style="font-family: monospace;">"degrees"</span> for ecliptic, galactic, and
  supergalactic systems.
  </dd>
  </dl>
  <dl id="l_olngformat">
  <dt><b>olngformat = <span style="font-family: monospace;">""</span>, olatformat=<span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='olngformat' Line='olngformat = "", olatformat=""' -->
  <dd>The output ra / longitude and dec / latitude formats if the output
  celestial coordinate system is different from the catalog celestial
  coordinate system. The defaults are <span style="font-family: monospace;">"  %010.1h"</span> for hours, <span style="font-family: monospace;">"  %9h"</span> for degrees
  and <span style="font-family: monospace;">"  %9.7g"</span> for radians.
  </dd>
  </dl>
  <dl id="l_exprs">
  <dt><b>exprs = <span style="font-family: monospace;">"c[*]"</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='exprs' Line='exprs = "c[*]"' -->
  <dd>The list of output columns and column expressions separated by commas.
  By default the entire record for the extracted object is output exactly
  as it is. The output columns can be individual columns e.g. c1 or c5
  or column ranges, e.g. c[1-10] or c[2-4]. Column expressions are
  expressions of the catalog columns, e.g c4 + c5.  Columns and column
  expression are output in the order in which they appear in exprs.
  </dd>
  </dl>
  <dl id="l_formats">
  <dt><b>formats = <span style="font-family: monospace;">""</span></b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='formats' Line='formats = ""' -->
  <dd>An optional list of column formats separated by commas. Column formats must
  be placeholders, e.g. the letter f for existing columns which are not
  reformatted (with the possible exception of the coordinate columns).
  Column expression formats may be any regular formatting expression.
  For example if <i>exprs</i> is <span style="font-family: monospace;">"c[1-3],c4+c5,c5+c7"</span>, then formats might be
  <span style="font-family: monospace;">"f,%7.3f,%7.3f"</span>.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes' -->
  <dd>Print messages on the standard output about actions taken by the task.
  </dd>
  </dl>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Ccget extracts objects in a user specified field from the input catalogs
  <i>input</i> and writes the extracted records to the output
  catalogs <i>output</i>.
  </p>
  <p>
  The user field is specified by the parameters <i>lngcenter</i>, <i>latcenter</i>,
  <i>lngwidth</i>, and <i>latwidth</i>, where the field center is entered in
  the celestial coordinate system specified by <i>fcsystem</i> and the
  units are specified by <i>fclngunits</i> and <i>fclatunits</i>. If fcsystem
  is undefined it defaults to the value of the catalog coordinate system
  <i>catsystem</i>.
  </p>
  <p>
  The input catalogs must be text files containing 2 or more columns separated
  by whitespace. By default these columns are assigned names of the form
  c1, c2, ..., cn. Legal columns names must have the form described
  in the following column names section. Users may assign their own names
  to the columns by setting
  the <i>colaliases</i> parameter. The input catalog columns <i>lngcolumn</i> and
  <i>latcolumn</i> must contain the ra / longitude and dec / latitude coordinates
  of the catalog objects respectively. The parameters <i>catsystem</i>,
  <i>catlngunits</i>, and <i>catlatunits</i> specify the coordinate system
  of the input catalog and its coordinate units respectively.
  </p>
  <p>
  At task startup the user field center is transformed from the coordinate
  system defined by <i>fcsystem</i> to the catalog coordinate system
  <i>catsystem</i> and the ra / longitude and dec / latitude limits of the
  user field are computed. As each input catalog record is read, the catalog
  coordinates are decoded and tested against these limits. If the 
  object is inside the user field then the column and column
  expressions specified by <i>exprs</i> are extracted from the input catalogs
  and written to the output catalogs.
  </p>
  <p>
  If the output celestial coordinate system <i>outsystem</i> is
  different from <i>catsystem</i>, then the catalog coordinates are transformed
  and to the output coordinates system, and written to the output catalog
  in the units specified
  by <i>olngunits</i> and <i>olatunits</i>, with the formats specified by
  <i>olngformat</i> and <i>olatformat</i>. Existing columns are written to
  the output catalog in the same
  format they have in the input catalog. Column expressions are written
  using the formats specified by <i>formats</i> or the builtin defaults
  of %5b, %10d, %10g, or %s for boolean, integer, floating point, or
  string columns  respectively.
  </p>
  </section>
  <section id="s_column_names">
  <h3>Column names</h3>
  <p>
  By default column names are of the form c1, c2, ..., cN. However users can
  also define their own column names, which must have the following syntax
  </p>
  <div class="highlight-default-notranslate"><pre>
  {a-zA-Z}[{a-zA-Z0-9._$}]*
  </pre></div>
  <p>
  where [] indicates optional, {} indicates a class, - indicates an ascii
  range of characters, and * indicates zero or more occurrences. In words
  a column name must begin with an alphabetic character and be followed
  by any combination of alphabetic, digit, or <span style="font-family: monospace;">'.'</span>, <span style="font-family: monospace;">'_'</span>, and <span style="font-family: monospace;">'$'</span> characters.
  The ccget task imposes a 19 character limit on the columns names so it is
  best to keep them short.
  </p>
  </section>
  <section id="s_column_expressions">
  <h3>Column expressions</h3>
  <p>
  Expressions must consist of operands and operators. The operands may be
  column names, numeric constants, functions, and quoted string constants.
  Values given as sexagesimal strings are automatically converted to
  decimal numbers. The operators are arithmetic, logical, and string.
  </p>
  <p>
  The following operators are supported:
  </p>
  <div class="highlight-default-notranslate"><pre>
  +  -  *  /              arithmetic operators
  **                      exponentiation
  //                      string concatenation
  !  -                    boolean not, unary negation
  &lt;  &lt;= &gt;  &gt;=             order comparison (works for strings)
  == != &amp;&amp; ||             equals, not equals, and, or
  ?=                      string equals pattern
  ? :                     conditional expression
  </pre></div>
  <p>
  The following intrinsic functions are supported:
  </p>
  <div class="highlight-default-notranslate"><pre>
  abs     atan2   deg     log     min     real    sqrt
  acos    bool    double  log10   mod     short   str
  asin    cos     exp     long    nint    sin     tan
  atan    cosh    int     max     rad     sinh    tanh
  </pre></div>
  </section>
  <section id="s_column_formats">
  <h3>Column formats</h3>
  <p>
  A  format  specification has the form <span style="font-family: monospace;">"%w.dCn"</span>, where w is the field
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
  <section id="s_some_builtin_catalog_formats">
  <h3>Some builtin catalog formats</h3>
  <p>
  The nlandolt.dat catalog in noao$photcal/catalogs/ has the following format.
  </p>
  <div class="highlight-default-notranslate"><pre>
  # Column     Quantity
  
         1           id
         2           ra
         3          dec
         4            v
         5          b-v
         6          u-b
         7          v-r
         8          r-i
         9          v-i
        10            n
        11            m
        12       err(v)
        13     err(b-v)
        14     err(u-b)
        15     err(v-r)
        16     err(r-i)
        17     err(v-i)
  </pre></div>
  <p>
  where the coordinates are in j2000, the errors are all mean errors of the mean,
  and n and m are the number of observations and number of independent nights
  of observations respectively.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  The catalog references are
  </p>
  <div class="highlight-default-notranslate"><pre>
  nlandolt.dat - Landolt, A.U. 1992, A.J. 104, 340
  </pre></div>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Example 1. Extract all Landolt standard stars within a 1 degree field
  surrounding the position ra = 3:55:00 dec = 0:00:00 (J2000).
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccget nlandolt.dat output 03:55:00.0 0:00:00 1.0 1.0
  </pre></div>
  <p>
  Example 2. Repeat example 1 but output the coordinates in the b1950
  celestial coordinate system.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccget nlandolt.dat output 03:55:00.0 0:00:00 1.0 1.0 \
  outsystem=b1950
  </pre></div>
  <p>
  Example 3. Repeat example 1 but extract only the id, ra, dec, v, 
  and b-v fields from the Landolt catalog.  Note that since these
  columns are the first five in the catalog they can be specified
  as a range.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccget nlandolt.dat output 03:55:00.0 0:00:00 1.0 1.0 \
  exprs="c[1-5]"
  </pre></div>
  <p>
  Example 4. Repeat example 1 but extract the id, ra, dec, b and
  b-r colors. Note that b and b-r are not columns in the input catalog
  but may be computed from them. Note also that formats should be
  specified to give the desired spacing, although defaults will be
  supplied.
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; ccget nlandolt.dat output 03:55:00.0 0:00:00 1.0 1.0 \
  exprs="c[1-3],c4+c5,c5+c7" formats="%7.3f,%7.3f
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
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'PARAMETERS' 'DESCRIPTION' 'COLUMN NAMES' 'COLUMN EXPRESSIONS' 'COLUMN FORMATS' 'SOME BUILTIN CATALOG FORMATS' 'REFERENCES' 'EXAMPLES' 'TIME REQUIREMENTS' 'BUGS' 'SEE ALSO'  -->
  

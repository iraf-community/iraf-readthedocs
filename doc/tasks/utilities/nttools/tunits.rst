.. _tunits:

tunits: Convert table column from one set of units to another
=============================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tunits table column newunits
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  Tunits converts a column in a table from one set of units to
  another. It supports both scalar and array columns. You supply the
  table and column name and the new units you want the column to be
  in. Optionally, you can apply the current column units if the units
  string stored in the table is missing or incorrect. Tunits only
  supports multiplicative conversions, conversions that involve additive
  changes, like Kelvin to Celsius, are not supported. Unit names and
  conversions are read from two tables. You can copy these tables and
  edit them if you want to add new conversions.
  </p>
  <p>
  You can find out the current units for a table column by running
  tlcol. If a units conversion is not supported by this task and you
  know the conversion formula, you can run tcalc.
  </p>
  <p>
  Tunits must parse the unit strings you pass it, which requires that
  they follow a certain set of rules. Units can be a simple units name,
  such as ergs, or a units name raised to a power, such as meters^2, or
  the product or quotient of units names raised to a power, such as
  feet/sec or gm*cm/s^2. If two units names are next to each other
  without any operator between them, a multiplication is assumed. If a
  units name is followed by a number, the units name is assumed to be
  raised to that power.
  </p>
  <p>
  Powers can also be specified by preceding the unit name with the
  string <span style="font-family: monospace;">"square"</span>, <span style="font-family: monospace;">"sq"</span>, <span style="font-family: monospace;">"cubic"</span>, or <span style="font-family: monospace;">"cu"</span>. For example, <span style="font-family: monospace;">"square meter"</span>
  is equivalent to <span style="font-family: monospace;">"meter^2"</span>.
  </p>
  <p>
  The operators recognized are:
  </p>
  <div class="highlight-default-notranslate"><pre>
  division        / or per
  multiplication  *
  exponentiation  ^ or **
  </pre></div>
  <p>
  Division has the lowest priority and exponentiation the highest. This
  means ergs/sec*angstrom is interpreted as ergs/(sec*angstrom) and not
  (ergs/sec)*angstrom, as it would be in most computer languages. The
  default priority can be changed by changed by grouping terms with
  parentheses. 
  </p>
  <p>
  Each set of units can have several synonymous names. These names are
  listed in the abbreviations table. Case is not significant in names
  and regular plurals (made by adding an <span style="font-family: monospace;">"s"</span>) are converted to the
  singular. Names should contain only alphabetic characters.  Blanks,
  underscores and digits are not allowed.
  </p>
  <p>
  The conversions supported by this task are read from the units
  conversion table. The table lists the old and new units and a
  conversion factor. Only one conversion is allowed for each set of
  units. 
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table [file]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file]' -->
  <dd>The name of the table the conversion is applied to.
  </dd>
  </dl>
  <dl id="l_column">
  <dt><b>column [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='column' Line='column [string]' -->
  <dd>The column to be converted. Both scalar and array columns are
  supported.
  </dd>
  </dl>
  <dl id="l_newunits">
  <dt><b>newunits [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='newunits' Line='newunits [string]' -->
  <dd>The new set of units for the column. The format of this parameter is
  described above. This task writes the new units to the units field in
  the table column.
  </dd>
  </dl>
  <dl>
  <dt><b>(oldunits = <span style="font-family: monospace;">" "</span>) [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(oldunits = " ") [string]' -->
  <dd>The units that the table column is currently in. If the value of this
  parameter is blank, the units will be read from the table.
  </dd>
  </dl>
  <dl>
  <dt><b>(abrevtab = <span style="font-family: monospace;">"ttools$tunits/abrev.tab"</span>) [file]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(abrevtab = "ttools$tunits/abrev.tab") [file]' -->
  <dd>A table of alternate names for each unit. This table contains two
  columns. The first column is the name of the units and the second
  column is the standard abbreviation. Because the default table is an
  ascii file, columns are read positionally and not by column names
  Many units have more than one name or abbreviation. Using a standard
  abbreviation allows units to be converted to a standard form, which
  simplifies calculations. The standard abbreviation is used internally
  when computing the conversion factor. Case is not significant in names
  and regular plurals (made by adding an <span style="font-family: monospace;">"s"</span>) are converted to the
  singular before looking them up in the table. Names should contain
  only alphabetic characters.  Blanks, underscores and digits are not
  allowed.
  The name of this table is a parameter to allow you to create your own
  table of standard abbreviations, with additional units.
  </dd>
  </dl>
  <dl>
  <dt><b>(unittab = <span style="font-family: monospace;">"ttools$tunits/units.tab"</span>) [file]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(unittab = "ttools$tunits/units.tab") [file]' -->
  <dd>A table of conversion factors from one set of units into another.
  This table contains four columns. The first is the conversion factor,
  a double precision number. The second is the units the task tries to
  convert from. The third column is the units the task tries to convert
  to. The fourth column is contains the boolean variable swap, explained
  a little later. 
  The table is interpreted as <span style="font-family: monospace;">"There are &lt;factor&gt; &lt;from&gt; in a &lt;to&gt;."</span>
  For example, <span style="font-family: monospace;">"There are 100 centimeters in a meter."</span>  The last column,
  swap, does not change the sense of the sentence but does change the
  direction that the conversion is applied, For example, <span style="font-family: monospace;">"60 seconds in
  a minute"</span> is actually a conversion from minutes to seconds because
  swap is yes. Unit conversions should set swap to yes when the desired
  conversion is not an exact value, but its inverse is. Only one
  conversion is allowed per unit, which simplifies the program logic
  considerably. Conversions should be chosen so that they ultimately
  resolve to MKS units. To prevent endless loops conversions from the
  fundamental units of MKS are checked for and forbidden. However, the
  program does not check for other loops, so be careful when adding new
  conversions!
  As in the case of the abbreviation table, the table name is a
  parameter to allow you to create your own table with additional unit
  conversions. 
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = no) [bool]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = no) [bool]' -->
  <dd>If you set this parameter to yes, the task will print a message to
  STDERR for each units conversion utilized in computing the conversion
  factor.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Convert watts to ergs per second. Print the diagnostic messages:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tunits source.tab power "ergs/sec" old=watts verb+
  </pre></div>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by Bernie Simon
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  tlcol, tcalc
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'REFERENCES' 'SEE ALSO'  -->
  

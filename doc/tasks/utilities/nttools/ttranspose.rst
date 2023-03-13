.. _ttranspose:

ttranspose: Transpose or flip a table.
======================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  ttranspose intable outtable action
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task can be used to transpose a table
  so that input rows become output columns
  and input columns become output rows.
  Another option is to flip the table horizontally,
  that is, the first input column is the last output column.
  Finally, the table can be flipped vertically,
  i.e., the first input row is the last output row.
  Any combination of these operations may be performed.
  </p>
  <p>
  If the table is actually transposed
  (rather than just flipped horizontally and/or vertically),
  the data types of all input columns must be the same.
  In addition, if the columns contain arrays rather than scalars,
  all the array lengths must be the same.
  The data type and array size will be preserved in the output table,
  but the column names of the output table will be <span style="font-family: monospace;">"c1"</span>, <span style="font-family: monospace;">"c2"</span>, <span style="font-family: monospace;">"c3"</span>, etc,
  with default print format and null units.
  Actually, some mixing of data types is permitted.
  If some columns are type real and others are double precision,
  the output data type will be double precision.
  Similarly, short integers will be promoted to integers.
  Boolean columns can be mixed with any other data type;
  for numeric columns, yes becomes 1 and no becomes 0.
  When the columns in the input table are character strings,
  different maximum string lengths are permitted,
  and the output length will be the maximum of the input lengths.
  The restrictions on data type are not imposed on text tables,
  which can contain mixed integer, double precision and text columns.
  </p>
  <p>
  If the table is only flipped but not transposed,
  the above restrictions on data type do not apply,
  and the column names, units and print formats will be preserved.
  Note that an operation such as <span style="font-family: monospace;">"tht"</span>
  (which happens to be equivalent to <span style="font-family: monospace;">"v"</span>)
  does not actually transpose the table,
  so the data types of the columns need not all be the same.
  </p>
  <p>
  The 'tstat' task gives statistics for the values in a column,
  so one application of 'ttranspose' is to get statistics on
  the values in a row by first transposing the table and then running 'tstat'.
  </p>
  <p>
  Text tables with too many rows cannot be transposed
  due to the limit of 1024 on the length of each row of a text table.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [file name template]' -->
  <dd>The list of input table names.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [file name template]' -->
  <dd>The list of output table names.
  There must be the same number of input and output names.
  If the output is to be written to the standard output, however,
  you can use outtable = <span style="font-family: monospace;">"STDOUT"</span> even if there several input tables.
  </dd>
  </dl>
  <dl id="l_action">
  <dt><b>action = <span style="font-family: monospace;">"t"</span> [string]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='action' Line='action = "t" [string]' -->
  <dd>This is a string made up of the letters <span style="font-family: monospace;">"t"</span>, <span style="font-family: monospace;">"h"</span>, and <span style="font-family: monospace;">"v"</span>
  which specify the operations to perform on the tables.
  <span style="font-family: monospace;">"t"</span> means transpose (input rows become output columns),
  <span style="font-family: monospace;">"h"</span> means flip horizontally (reverse the order of the columns),
  and <span style="font-family: monospace;">"v"</span> means flip vertically (reverse the order of the rows).
  The operations are performed in the order given from left to right.
  Any combination of <span style="font-family: monospace;">"t"</span>, <span style="font-family: monospace;">"h"</span>, and <span style="font-family: monospace;">"v"</span> may be used,
  in any order, and the letters may be repeated.
  Operations such as <span style="font-family: monospace;">"tt"</span>, <span style="font-family: monospace;">"hh"</span> or <span style="font-family: monospace;">"vv"</span> are valid,
  and they result in a simple copy of input to output.
  The symbols <span style="font-family: monospace;">"/"</span>, <span style="font-family: monospace;">"-"</span> and <span style="font-family: monospace;">"|"</span> are equivalent to
  the letters <span style="font-family: monospace;">"t"</span>, <span style="font-family: monospace;">"h"</span> and <span style="font-family: monospace;">"v"</span> respectively.
  </dd>
  </dl>
  <dl id="l_verbose">
  <dt><b>verbose = yes [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='verbose' Line='verbose = yes [boolean]' -->
  <dd>Print the names of the tables as they are processed?
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  The input is the text file <span style="font-family: monospace;">"in"</span>,
  and the output is to be displayed on the screen.
  Each of the three operations (<span style="font-family: monospace;">"t"</span>, <span style="font-family: monospace;">"h"</span>, <span style="font-family: monospace;">"v"</span>)
  and some combinations are illustrated.
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; type in
  one     two     three
  four    five    six
  seven   eight   nine
  ten     eleven  twelve
  
  tt&gt; ttranspose in STDOUT t
  in --&gt; STDOUT
  one    four   seven  ten
  two    five   eight  eleven
  three  six    nine   twelve
  
  tt&gt; ttranspose in STDOUT h
  in --&gt; STDOUT
  three  two    one
  six    five   four
  nine   eight  seven
  twelve eleven ten
  
  tt&gt; ttranspose in STDOUT v
  in --&gt; STDOUT
  ten   eleven twelve
  seven eight  nine
  four  five   six
  one   two    three
  
  tt&gt; ttranspose in STDOUT hv
  in --&gt; STDOUT
  twelve eleven ten
  nine   eight  seven
  six    five   four
  three  two    one
  
  tt&gt; ttranspose in STDOUT th
  in --&gt; STDOUT
  ten    seven  four   one
  eleven eight  five   two
  twelve nine   six    three
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
  Type <span style="font-family: monospace;">"help ttools opt=sys"</span> for a description of the 'tables' package.
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

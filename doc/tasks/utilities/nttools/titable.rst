.. _titable:

titable: Insert 2-D tables into rows of a 3-D table.
====================================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  titable intable outtable
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task performs the inverse operation of task txtable: it inserts one or 
  more 2-D tables into rows of a 3-D table  The input may be a filename 
  template, including wildcard characters, or the name of a file (preceded by 
  an @ sign) containing table names.  The output is a single 3-D table name.
  If the output table exists, insertion will be done in place. If the output 
  table does not exist, it will be created. The input and output tables must 
  not be the same.
  </p>
  <p>
  This task supports row/column selectors in the input table names. These
  may be used to select subsets of both rows and columns from the input table.
  If no selectors are used, all columns and rows will be processed, 
  Type 'help selectors' to see a description of the selector syntax. 
  </p>
  <p>
  When creating a new output table, the information describing its columns
  can be taken from two sources. If parameter 'template' has the name of an
  existing 3-D table, the column descriptions, including maximum array sizes,
  will be taken from that table. If 'template' has an invalid or null (<span style="font-family: monospace;">""</span>)
  value, the column-defining information will be take from the first table 
  in the input list, where its number of rows will define the maximum array
  size allowed in the table being created. Column selectors are allowed in
  the template table.
  </p>
  <p>
  NOTE: Both the output and template table names must always be supplied 
  complete, including their extension. Otherwise the task may get confused 
  on the existence of an already existing table.
  </p>
  <p>
  Insertion is performed by first verifying if column names in both input
  and output tables match. If a match is found, values taken from that column
  and all selected rows from the input table will be stored as a 1-dimensional 
  array in a single cell in the corresponding column in the output 3-D table. 
  The row in this table where the insertion takes place is selected by the 
  <span style="font-family: monospace;">"row"</span> task parameter. It points to the row where the first table in the input 
  list will be inserted, subsequent tables in the list will be inserted into 
  subsequent rows. This mechanism is superseded if the <span style="font-family: monospace;">"row"</span> parameter is set 
  to INDEF or a negative value, and the keyword <span style="font-family: monospace;">"ORIG_ROW"</span> is found in the 
  header of the input table. This keyword is created by task txtable and its 
  value supersedes the row counter in the task.
  </p>
  <p>
  If the maximum array size in a target column in the output 3-D table is
  larger than the number of selected input rows, the array will be filled 
  up starting from its first element, and the empty elements at the end will 
  be set to INDEF (or <span style="font-family: monospace;">""</span> if it is a character string column). If the maximum 
  array size is smaller than the number of selected rows, insertion begins by
  the first selected row up to the maximum allowable size, the remaining rows
  being ignored.
  </p>
  <p>
  This task correctly handles scalars stored in the input table header
  by task txtable. Since the selector mechanism does not work with these
  scalars, the task will always insert them into the output table, provided
  there is a match in column names.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_intable">
  <dt><b>intable [file name list/template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='intable' Line='intable [file name list/template]' -->
  <dd>A list of one or more tables to be inserted. Row/column selectors are supported.
  </dd>
  </dl>
  <dl id="l_outtable">
  <dt><b>outtable [table name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='outtable' Line='outtable [table name]' -->
  <dd>Name of 3-D output table, including extension. No support exists for 
  <span style="font-family: monospace;">"STDOUT"</span> (ASCII output).
  </dd>
  </dl>
  <dl>
  <dt><b>(template = <span style="font-family: monospace;">""</span>) [table name]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(template = "") [table name]' -->
  <dd>Name of 3-D table to be used as template when creating a new output table.
  </dd>
  </dl>
  <dl>
  <dt><b>(row = INDEF) [int]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(row = INDEF) [int]' -->
  <dd>Row where insertion begins. If set to INDEF or a negative value, the row
  number will be looked for in the input table header.
  </dd>
  </dl>
  <dl>
  <dt><b>(verbose = yes) [boolean]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(verbose = yes) [boolean]' -->
  <dd>Display names of input and output tables as files are processed ?
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  Insert columns named FLUX and WAVELENGTH from input tables into a 3-D table:
  </p>
  <div class="highlight-default-notranslate"><pre>
  cl&gt; titable "itable*.tab[c:FLUX,WAVELENGTH]" otable.tab
  </pre></div>
  </section>
  <section id="s_bugs">
  <h3>Bugs</h3>
  <p>
  The output and template table names must be supplied in full, including 
  the extension (e.g. <span style="font-family: monospace;">".tab"</span>). If the output table name is not typed in full, 
  the task will create a new table in place of the existing one, with only the 
  rows actually inserted. This behavior relates to the way the underlying 
  <span style="font-family: monospace;">"access"</span> routine in IRAF's fio library works.
  </p>
  </section>
  <section id="s_references">
  <h3>References</h3>
  <p>
  This task was written by I. Busko.
  </p>
  </section>
  <section id="s_see_also">
  <h3>See also</h3>
  <p>
  txtable, selectors
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  

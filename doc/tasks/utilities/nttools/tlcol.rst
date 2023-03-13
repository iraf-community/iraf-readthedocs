.. _tlcol:

tlcol: List column information for a table.
===========================================

**Package: nttools**

.. raw:: html

  <section id="s_usage">
  <h3>Usage</h3>
  <p>
  tlcol table
  </p>
  </section>
  <section id="s_description">
  <h3>Description</h3>
  <p>
  This task is used to list column information for a table.  The output is
  written to STDOUT, which may be redirected to a file.  There will be one line
  of output for each column in the table, and each output line may contain the
  column name, data type, print format, and units.
  The first line of output for each table in the input list is the table
  name preceded by a # sign.
  </p>
  <p>
  The output from this task may be used as input to various tasks such
  as 'tcreate', 'tprint', and 'tproject'.
  </p>
  </section>
  <section id="s_parameters">
  <h3>Parameters</h3>
  <dl id="l_table">
  <dt><b>table [file name template]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='table' Line='table [file name template]' -->
  <dd>A list of tables for which column info is to be printed.
  </dd>
  </dl>
  <dl>
  <dt><b>(nlist = 4) [integer, min=1, max=4]</b></dt>
  <!-- Sec='PARAMETERS' Level=0 Label='' Line='(nlist = 4) [integer, min=1, max=4]' -->
  <dd>The number of items to list.
  The output will consist of 'nlist' columns,
  one line for each column that is defined in the table.
  The items listed out are column name (displayed for all 'nlist' values),
  data type (displayed if 'nlist' is 2 or higher),
  display format (if 'nlist' is 3 or higher),
  units (if 'nlist' is 4).
  If 'nlist = 1', only the column name will be displayed;
  the output list may be edited and used as input to
  'tprint', 'tdump,<span style="font-family: monospace;">' '</span>tedit', 'tread', 'tproject', or 'tquery'.
  The default of 4 can be used to generate
  a column-description file for the 'tcreate' task.
  If a column contains an array of values at each row,
  rather than just a single element,
  the array size is shown in square brackets appended to the data type.
  </dd>
  </dl>
  </section>
  <section id="s_examples">
  <h3>Examples</h3>
  <p>
  1.  Display the names, data types, print formats, and units of all the
  columns in the table <span style="font-family: monospace;">"example.tab"</span>:
  </p>
  <div class="highlight-default-notranslate"><pre>
  tt&gt; tlcol example.tab
  </pre></div>
  <p>
  2.  Print (using the 'tprint' task) specific columns:
  </p>
  <div class="highlight-default-notranslate"><pre>
          tt&gt; tlcol example.tab nlist=1 &gt;colnames.lis
          tt&gt; edit colnames.lis
          (Rearrange the column names and perhaps delete some of them.)
          tt&gt; tprint example.tab columns=@colnames.lis
  
  3.  Create a new table based on the columns in "example.tab":
  
          tt&gt; tlcol example.tab nlist=4 &gt;colnames.lis
          tt&gt; edit colnames.lis
          (Delete or modify some column descriptions and/or add new ones.)
          tt&gt; tcreate ex2.tab cdfile=colnames.lis ...
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
  tinfo, tcreate, tdump
  </p>
  
  </section>
  
  <!-- Contents: 'NAME' 'USAGE' 'DESCRIPTION' 'PARAMETERS' 'EXAMPLES' 'BUGS' 'REFERENCES' 'SEE ALSO'  -->
  
